# NEW CGT Data Analysis Script!! 
#
# Script to analyze the data collected online during Summer 2022 in the CGT
# (Control & Gambling Task) study

rm(list=ls()); # Clear the workspace

# identify the working directory paths
main_wd = '/Volumes/shlab/Projects/CGT/';
processeddata_wd = paste0(main_wd,'processeddata/')

#### Loading Data ####
setwd(processeddata_wd)
fn = dir(pattern = glob2rx('cgt_processed*.csv'),full.names = T);

data_dm = read.csv(fn[1]) # decision-making data
data_wm = read.csv(fn[2]) # working memory data

number_of_subjects = length(unique(data_dm$subjectnumber));

#### Data Quality Checks & Exclusions ####

# Exclude on the basis of DM task performance
# (using... check trials, RTs, choices)

# Check Trials
check_trial_failure = array(dim = c(number_of_subjects,1));

for (subj in 1:number_of_subjects){
  tmpdata = data_dm[data_dm$subjectnumber == subj,];
  check_trial_index = which(tmpdata$ischecktrial==1);
  correct_answers = (0.5 * tmpdata$riskyopt1[check_trial_index] +
                       0.5 * tmpdata$riskyopt2[check_trial_index]) > tmpdata$safe[check_trial_index];
  check_trial_failure[subj] = length(which(!tmpdata$choice[check_trial_index] == correct_answers))/length(check_trial_index);
}

check_trial_criterion = 0.2; # The maximum percent of check trials that can be missed
# (there were 10 check trials)
# chance is 0.5, perfect is 0.0.

keep_check_trial = check_trial_failure <= check_trial_criterion;

# Missed Choices
# on the basis of is.na(data_dm$choice)
#if missed >75% = exclude, for compensation, if i recall correctly, there should be 1 person who had 60%

# RTs
mean_rts = array(dim = c(number_of_subjects,1));

for (subj in 1:number_of_subjects){
  tmpdata = data_dm[data_dm$subjectnumber == subj,];
  
  mean_rts[subj] = mean(tmpdata$reactiontime, na.rm = T)
}

keep_dm_rt = mean_rts > 0.85;

mean_rts[keep_dm_rt] #participants = 35, 3, 28 have rt less than 0.85
hist(mean_rts[keep_dm_rt]) # histogram of mean rts
mean(mean_rts[keep_dm_rt]) # new mean rt 1.22 seconds

# Cannot exclude on the basis of WM task quality

# >>>Create clean data frames<<<
keep_participants = which(keep_check_trial & keep_dm_rt);

# Create clean data frames for data!
clean_data_dm = data_dm[data_dm$subjectnumber %in% keep_participants,]
clean_data_wm = data_wm[data_wm$subjectnumber %in% keep_participants,]

number_of_clean_subjects = length(keep_participants);

#### BASIC DATA ANALYSIS ####
# (Separately for DM & WM data)
# Descriptive & simple averages of task performance

#### Optimization Function Creation ####
choice_probability <- function(parameters, choiceset) {
  # A function to calculate the probability of taking a risky option
  # using a prospect theory model.
  # Assumes parameters are [rho, mu] as used in S-H 2009, 2013, 2015, etc.
  # Assumes choiceset has columns riskyoption1, riskyoption2, and safeoption
  #
  # PSH & AR June 2022
  
  # extract  parameters
  rho = as.double(parameters[1]); # risk attitudes
  mu = as.double(parameters[2]); # choice consistency
  
  # Correct parameter bounds
  if(rho <= 0){
    rho = .Machine$double.eps;
  }
  
  if(mu < 0){
    mu = 0;
  }
  
  # calculate utility of the two options
  utility_risky_option = 0.5 * choiceset$riskyoption1^rho + 
    0.5 * choiceset$riskyoption2^rho;
  utility_safe_option = choiceset$safeoption^rho;
  
  # normalize values using this term
  div <- max(choiceset[,1:3])^rho; # decorrelates rho & mu
  
  # calculate the probability of selecting the risky option
  p = 1/(1+exp(-mu/div*(utility_risky_option - utility_safe_option)));
  
  return(p)
}

# Likelihood function
negLLprospect_cgt <- function(parameters,choiceset,choices) {
  # A negative log likelihood function for a prospect-theory estimation.
  # Assumes parameters are [rho, mu] as used in S-H 2009, 2013, 2015, etc.
  # Assumes choiceset has columns riskyoption1, riskyoption2, and safeoption
  # Assumes choices are binary/logical, with 1 = risky, 0 = safe.
  #
  # Peter Sokol-Hessner
  # July 2021
  
  choiceP = choice_probability(parameters, choiceset);
  
  likelihood = choices * choiceP + (1 - choices) * (1-choiceP);
  likelihood[likelihood == 0] = 0.000000000000001; # 1e-15, i.e. 14 zeros followed by a 1
  
  nll <- -sum(log(likelihood));
  return(nll)
}

eps = .Machine$double.eps;
lower_bounds = c(eps, 0); # R, M
upper_bounds = c(2,80); 
number_of_parameters = length(lower_bounds);

# Create placeholders for parameters, errors, NLL (and anything else you want)
number_of_iterations = 200; # 100 or more
estimated_parameters = array(dim = c(number_of_clean_subjects,2));
estimated_parameter_errors = array(dim = c(number_of_clean_subjects,2));
NLLs = array(dim = c(number_of_clean_subjects,1));


for (subj in 1:number_of_clean_subjects){
  subj_id = keep_participants[subj];
  print(subj_id)
  
  tmpdata = clean_data_dm[(clean_data_dm$subjectnumber == subj_id) & 
                            (clean_data_dm$static0dynamic1 == 0) & 
                            is.finite(clean_data_dm$choice),]; # defines this person's data
  
  temp_parameters = array(dim = c(number_of_iterations,number_of_parameters));
  temp_hessians = array(dim = c(number_of_iterations,number_of_parameters,number_of_parameters));
  temp_NLLs = array(dim = c(number_of_iterations,1));
  
  choiceset = as.data.frame(cbind(tmpdata$riskyopt1, tmpdata$riskyopt2, tmpdata$safe));
  colnames(choiceset) <- c('riskyoption1', 'riskyoption2', 'safeoption');
  
  # tic() # start the timer
  
  for(iter in 1:number_of_iterations){
    # Randomly set initial values within supported values
    # using uniformly-distributed values. Many ways to do this!
    
    initial_values = runif(number_of_parameters, min = lower_bounds, max = upper_bounds)
    
    temp_output = optim(initial_values, negLLprospect_cgt,
                        choiceset = choiceset,
                        choices = tmpdata$choice,
                        lower = lower_bounds,
                        upper = upper_bounds,
                        method = "L-BFGS-B",
                        hessian = T)
    
    # Store the output we need access to later
    temp_parameters[iter,] = temp_output$par; # parameter values
    temp_hessians[iter,,] = temp_output$hessian; # SEs
    temp_NLLs[iter,] = temp_output$value; # the NLLs
  }
  
  # Compare output; select the best one
  NLLs[subj] = min(temp_NLLs); # the best NLL for this person
  best_ind = which(temp_NLLs == NLLs[subj])[1]; # the index of that NLL
  
  estimated_parameters[subj,] = temp_parameters[best_ind,] # the parameters
  estimated_parameter_errors[subj,] = sqrt(diag(solve(temp_hessians[best_ind,,]))); # the SEs
  
  
  ### Fix ChoiceP Values in clean_data_dm ###
  
  # 1. Create index to identify this person's static trials in clean_data_dm
  
  subj_index = (clean_data_dm$subjectnumber == subj_id) & (clean_data_dm$static0dynamic1 == 1);
  
  # 2. Pull out choiceset values
  
  dynamic_choiceset = as.data.frame(cbind(clean_data_dm$riskyopt1[subj_index], 
                                  clean_data_dm$riskyopt2[subj_index], 
                                  clean_data_dm$safe[subj_index]));
  colnames(dynamic_choiceset) <- c('riskyoption1', 'riskyoption2', 'safeoption');

  # 3. Calculate new choiceP values with choiceset & parameters

  choiceP_new = choice_probability(estimated_parameters[subj,], dynamic_choiceset)
    
  # 4. Store the values back in clean_data_dm
  
  clean_data_dm$choiceP[subj_index] = choiceP_new;
  
  ###
}

# Does optimized analysis match grid search analysis?

n_rho_values = 200; # SET THIS TO THE DESIRED DEGREE OF FINENESS
n_mu_values = 201; # IBID

rho_values = seq(from = 0.3, to = 2.2, length.out = n_rho_values); # the range of fit-able values
mu_values = seq(from = 7, to = 80, length.out = n_mu_values);

# look at all best rho & mu per participant
grid_bestRho = array(dim = c(number_of_clean_subjects,1));
grid_bestMu = array(dim = c(number_of_clean_subjects,1));
for (subj in 1:number_of_clean_subjects){
  subj_id = keep_participants[subj];
  
  tmpdata = clean_data_dm[clean_data_dm$subjectnumber == subj_id,];
  
  grid_bestRho[subj] = rho_values[unique(tmpdata$bestRho)];
  grid_bestMu[subj] = mu_values[unique(tmpdata$bestMu)];
}

plot(grid_bestRho,estimated_parameters[,1], main = 'RHO')
plot(grid_bestMu,estimated_parameters[,2], main = 'MU')



### Create Continuous difficulty metric ###

clean_data_dm$diff_cont = abs(abs(clean_data_dm$choiceP - 0.5)*2-1);
# EASY = 0
# DIFFICULT = 1

### Create Categorical difficulty metric ###

clean_data_dm$diff_cat = 0; # MEDIUM
clean_data_dm$diff_cat[clean_data_dm$diff_cont < .3] = -1; # EASY (p's < .15 or > .85)
clean_data_dm$diff_cat[clean_data_dm$diff_cont > .7] = 1; # DIFFICULT (p's > .35 AND < .65)
clean_data_dm$diff_cat[clean_data_dm$static0dynamic1 == 0] = NA;







#GENERAL SUBJECT LEVEL ANALYSIS 
#gambling behavior 
mean_pgamble = array(dim = c(number_of_clean_subjects,1));

#RTs (still want to look at these aspects)
mean_rt_easy = array(dim = c(number_of_clean_subjects, 1));
mean_rt_hard = array(dim = c(number_of_clean_subjects, 1));
mean_rt_medium = array(dim = c(number_of_clean_subjects, 1));

for (subj in 1:number_of_clean_subjects){
  subj_id = keep_participants[subj];
  rdmDF = clean_data_dm[clean_data_dm$subjectnumber == subj_id,]; 
  #mean_pgamble[subj_id] = mean(rdmDF$choice, na.rm = T);
  #mean_rt_easy[subj_id] = mean(rdmDF$reactiontime)

}
column_names_rdmDF = c(
  'mean-pgamble',
);

data_rdmDF = array(data = NA, dim = c(0, length(column_names_rdmDF)));
colnames(data_rdmDF) <-column_names_rdmDF
data_rdmDF <- data.frame(#FILL WITH COL NAMES
                         

### MORE COMPLEX ANALYSIS ###
#Generalized Liner Models 

