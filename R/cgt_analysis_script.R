# CGT Data Analysis Script
#
# Script to analyze the data collected online during Summer 2022 in the CGT
# (Control & Gambling Task) study.

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
  # correct_answers = (reactiontime >= 0.25) #I don't think we need a top cut off based upon distribution mainly around 1 second, anything above 0.2 seconds
  # incorrect_answers = (reactiontime == is.NaN) #if no response and not correct answers
  #reactiontime_criterion = (length((correct_answers)/(num_static_trials + num_dynamic_trials)) >= .80) #RT per participant must mostly be correct, so at least 80% of the RT must be greater than or equal to 250 ms.
  #keep_reactiontime == reactiontime_criterion
  # QUESTION: WHAT DO WE DO WITH NA TRIALS (MISSED, OR TOO FAST)? KEEP? DISCARD?

keep_dm_rt = mean_rts > 0.85;

#this way worked 
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

#### Basic Data Analysis ####
# (Separately for DM & WM data)
# Descriptives & simple averages of task performance

### DM task ###
# Analysis for static trials: Mean p(gamble), optimization
# mean_pgamble over all trials, static, and dynamic
mean_pgamble = array(dim = c(number_of_clean_subjects,1));
static_mean_pgamble = array(dim = c(number_of_clean_subjects, 1));
dynamic_mean_pgamble = array(dim = c(number_of_clean_subjects, 1));
easy_mean_pgamble = array(dim = c(number_of_clean_subjects, 1));
diff_mean_pgamble = array(dim = c(number_of_clean_subjects, 1));
easyACC_mean_pgamble = array(dim = c(number_of_clean_subjects, 1));
easyREJ_mean_pgamble = array(dim = c(number_of_clean_subjects, 1));

for (subj in 1:number_of_clean_subjects){
  subj_id = keep_participants[subj];
  tmpdata = clean_data_dm[clean_data_dm$subjectnumber == subj_id,]; # defines this person's data
  mean_pgamble[subj] = mean(tmpdata$choice, na.rm = T);
  static_mean_pgamble[subj] = mean(tmpdata$choice[tmpdata$static0dynamic1 == 0], na.rm=T);
  dynamic_mean_pgamble[subj] = mean(tmpdata$choice[tmpdata$static0dynamic1 == 1], na.rm=T);
  easy_mean_pgamble[subj] = mean(tmpdata$choice[tmpdata$easyP1difficultN1 == 1], na.rm = T);
  diff_mean_pgamble[subj] = mean(tmpdata$choice[tmpdata$easyP1difficultN1 == -1], na.rm = T);
  easyACC_mean_pgamble[subj] = mean(tmpdata$choice[(tmpdata$easyP1difficultN1 == 1) & (tmpdata$choiceP > .5)], na.rm = T);
  easyREJ_mean_pgamble[subj] = mean(tmpdata$choice[(tmpdata$easyP1difficultN1 == 1) & (tmpdata$choiceP < .5)], na.rm = T);
}

# Plot static vs. dynamic gambling
plot(static_mean_pgamble,dynamic_mean_pgamble,xlim = c(0,1), ylim = c(0,1))
lines(x = c(0,1), y = c(0,1), col = 'red')

pgambleDiff = static_mean_pgamble - dynamic_mean_pgamble # most are negative, suggesting people gambled more in dyanmic, but also more chioces... 

plot(easy_mean_pgamble,diff_mean_pgamble,xlim = c(0,1), ylim = c(0,1))
lines(x = c(0,1), y = c(0,1), col = 'blue')
# Lots of people taking risks on ALL (or nearly all) of the 'difficult' trials
# --> Will limit inferences we can draw about risk-taking on difficult trials b/c of low variability in behavior.

plot(easyACC_mean_pgamble,easyREJ_mean_pgamble,xlim = c(0,1), ylim = c(0,1))
# Almost all choices predicted to be accepted, ARE (p(gamble) = 0.97)
# Many choices predicted to be rejected, are (p(gamble) = 0.23)


# Optimization
#### Function Creation ####

# Function to calculate choice probabilities
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
upper_bounds = c(2,50); 
number_of_parameters = length(lower_bounds);

# Create placeholders for parameters, errors, NLL (and anything else you want)
number_of_iterations = 200; # 100 or more
estimated_parameters = array(dim = c(number_of_subjects,2));
estimated_parameter_errors = array(dim = c(number_of_subjects,2));
NLLs = array(dim = c(number_of_subjects,1));

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
}

#^^should we look at this and choice probability^^? 

#Does optimized analysis match grid search analysis? WORK IN PROGRESS

#look at all best rho per participant
bestRho = array(dim = c(number_of_subjects,1));
for (subj in 1:number_of_subjects){
  tmpdata = data_dm[data_dm$subjectnumber == subj,];
  bestRho[subj] = mean(tmpdata$bestRho)
}
#look at all best mu per participant 
bestMu = array(dim = c(number_of_subjects,1));
for (subj in 1:number_of_subjects){
  tmpdata = data_dm[data_dm$subjectnumber == subj,];
  bestMu[subj] = mean(tmpdata$bestMu)
}
#unsure how to pull other data, do we look at bespoke choice sets, or calculation from other code?
# (should be very close!)


# Did choices align with predictions (re: easy risky and easy safe and hard)


# Reaction times for easy risky, easy safe, and hard (hard > easy (either))
#mean easy RT 
mean_rt_easy = array(dim = c(number_of_subjects, 1));
for (subj in 1:number_of_subjects){
  tmpdata = data_dm[data_dm$subjectnumber == subj,];
  tmpdata = tmpdata[tmpdata$easyP1difficultN1 == 1,];
  mean_rt_easy[subj] = mean(tmpdata$reactiontime, na.rm = T)
}
#mean hard RT 
mean_rt_hard = array(dim = c(number_of_subjects, 1));
for (subj in 1:number_of_subjects){
  tmpdata = data_dm[data_dm$subjectnumber == subj,];
  tmpdata = tmpdata[tmpdata$easyP1difficultN1 == -1,];
  mean_rt_hard[subj] = mean(tmpdata$reactiontime, na.rm = T)
}
#differences between averages
mean_rtDiff = mean_rt_easy - mean_rt_hard # a negative number means on average hard was longer, positive number means on average easy was shorter duration 
# i don't know if this makes sense^^, b/c lots of ppl have a positive number, maybe average is not way to compare. 


### WM Task ###

## Probability correct (FS & BS)


## Forward span
# max correct before 2 errors in a row @ a given length (BEST RELIABLE SPAN)

# total # of trials before 2 errors in a row @ a given length (QUALITY OF EF?)

# max correct ever (BEST SPAN PERIOD)


## Backward span (max correct before 2 errors in a row; max correct ever)
# max correct before 2 errors in a row @ a given length (BEST RELIABLE SPAN)

# total # of trials before 2 errors in a row @ a given length (QUALITY OF EF?)

# max correct ever (BEST SPAN PERIOD)


#### Connecting Decision-Making & Working Memory ####

