# CGT Data Analysis Script STUDY 2
#
# Script to analyze the data collected online during Winter 2023 (01/2023)
# (Control & Gambling Task) study.

rm(list=ls()); # Clear the workspace

# identify the working directory paths
main_wd = '/Volumes/shlab/Projects/CGT/CGT_study2/';
processeddata_wd = paste0(main_wd,'processeddata_study2/');

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
  
  # Plot the choice data
  plot(tmpdata$riskyopt1[tmpdata$choice == 1],tmpdata$safe[tmpdata$choice == 1], col = 'green', 
       xlab = 'Risky Gain $', ylab = 'Safe $', main = paste0('All Subjects; Subj ', subj),
       xlim = c(0,30), ylim = c(0,12))
  points(tmpdata$riskyopt1[tmpdata$choice == 0],tmpdata$safe[tmpdata$choice == 0], col = 'red')
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
mean_rts[keep_dm_rt] # only shows 3 particpants ( mean 1.7 sec, 1.3 sec, 1.28 sec)
hist(mean_rts[keep_dm_rt]) # histogram of mean rts
mean(mean_rts[keep_dm_rt]) # new mean rt 1.43 seconds

# exclude on the basis of WM task performance
#max_span = array(dim = c(number_of_subjects, 1));
#keep_max_span= max_span < 12

#for (subj in 1:number_of_subjects){
  #tmpdata = data_wm[data_wm$subjectnumber == subj,];
  #max_span[subj]= max(tmpdata$number_digits, na.rm = T) #attempting to set a max on the span capactity to be 12 arbitrarily 
#}  

# >>>Create clean data frames<<<
keep_participants = which(keep_check_trial & keep_dm_rt);

# Create clean data frames for data!
clean_data_dm = data_dm[data_dm$subjectnumber %in% keep_participants,]
clean_data_wm = data_wm[data_wm$subjectnumber %in% keep_participants,]

number_of_clean_subjects = length(keep_participants);

#### BASIC DATA ANALYSIS ####
# (Separately for DM & WM data)
# Descriptives & simple averages of task performance

#### DM task Analysis ####
# Analysis for static trials: Mean p(gamble), optimization
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
  
  # Plot the choice data
  plot(tmpdata$riskyopt1[tmpdata$choice == 1],tmpdata$safe[tmpdata$choice == 1], col = 'green', 
       xlab = 'Risky Gain $', ylab = 'Safe $', main = paste0('Kept Subjects; Subj ', subj_id),
       xlim = c(0,30), ylim = c(0,12))
  points(tmpdata$riskyopt1[tmpdata$choice == 0],tmpdata$safe[tmpdata$choice == 0], col = 'red')
}

column_names_rdm = c(
  'mean_pgamble',
  'static_mean_pgamble',
  'dynamic_mean_pgamble', 
  'easy_mean_pgamble',
  'diff_mean_pgamble', 
  'easyACC_mean_pgamble', 
  'easyREJ_mean_pgamble'
);

data_rdm = array(data = NA, dim = c(0, length(column_names_rdm)));
colnames(data_rdm) <-column_names_rdm
data_rdm <- data.frame(mean_pgamble,static_mean_pgamble,dynamic_mean_pgamble,easy_mean_pgamble,diff_mean_pgamble,easyACC_mean_pgamble,easyREJ_mean_pgamble)


# Plot static vs. dynamic gambling

# Q: How did risk-taking compare from static to dynamic conditions?
par(pty="s")
plot(static_mean_pgamble,dynamic_mean_pgamble,xlim = c(0,1), ylim = c(0,1), asp = 1)
lines(x = c(0,1), y = c(0,1), col = 'red')

pgambleDiff = static_mean_pgamble - dynamic_mean_pgamble
# A: positive numbers, suggesting people gambled less in dynamic than static 


# Q: How did risk-taking compare across the different dynamic trial types?
# e.g. easy accept vs. easy reject vs. difficult
hist(easyACC_mean_pgamble,
     col = rgb(0,1,0,.5), breaks = seq(from = 0, to = 1, by = 0.05), xlim = c(0,1), );
hist(easyREJ_mean_pgamble,
     col = rgb(1,0,0,.5), breaks = seq(from = 0, to = 1, by = 0.05), add = T);
hist(diff_mean_pgamble,
     col = rgb(0,0,1,.5), breaks = seq(from = 0, to = 1, by = 0.05), add = T);
# A: As expected red < blue < green (easy reject < difficult < easy acc), blue is more spread out 

# Q: Can we collapse across easy accept & reject trials based on relative distance from 0.5?
plot(abs(easyACC_mean_pgamble-.5),abs(easyREJ_mean_pgamble-.5),xlim = c(0,.5), ylim = c(0,.5),
     xlab = 'Distance from 0.5 for EASY ACC', ylab = 'Distance from 0.5 for EASY REJ')
lines(x = c(0,1), y = c(0,1), col = 'blue')
# ... we want these to be clustered together on the blue line, close to 0.5
# ... and they are! As of 2/27/23, except a few points

# Statistically test relative difficulty observed in easy ACC vs. easy REJ
t.test(abs(easyACC_mean_pgamble-.5), abs(easyREJ_mean_pgamble-.5), paired = T)

# A: Yes, we can treat all easy trials as similarly easy (whether easy ACC or REJ), not sig different


#### Optimization Function Creation ####

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

#### Optimization ####
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
}

### Q: Does optimized analysis match grid search analysis?###

n_rho_values = 200; # SET THIS TO THE DESIRED DEGREE OF FINENESS
n_mu_values = 201; # IBID

rho_values = seq(from = 0.3, to = 2.2, length.out = n_rho_values); # the range of fit-able values
mu_values = seq(from = 7, to = 80, length.out = n_mu_values);

 # CODE TO DO GRID SEARCH FRESH IF YOU WANT!
 
 best_rhos = array(dim = c(number_of_clean_subjects,1));
 best_mus = array(dim = c(number_of_clean_subjects,1));
 
 for (subj in 1:number_of_clean_subjects){
   subj_id = keep_participants[subj];
   print(subj_id)
#   
   tmpdata = clean_data_dm[(clean_data_dm$subjectnumber == subj_id) & 
                             (clean_data_dm$static0dynamic1 == 0) & 
                             is.finite(clean_data_dm$choice),]; # defines this person's data
   
   choiceset = as.data.frame(cbind(tmpdata$riskyopt1, tmpdata$riskyopt2, tmpdata$safe));
   colnames(choiceset) <- c('riskyoption1', 'riskyoption2', 'safeoption');
   
   grid_nll_values = array(dim = c(n_rho_values, n_mu_values));
   
   for(r in 1:n_rho_values){
     for(m in 1:n_mu_values){
       grid_nll_values[r,m] = negLLprospect_cgt(c(rho_values[r],mu_values[m]), choiceset, tmpdata$choice)
     }
   }
   
   min_nll = min(grid_nll_values); # identify the single best value
   indexes = which(grid_nll_values == min_nll, arr.ind = T); # Get indices for that single best value
   
   best_rhos[subj] = rho_values[indexes[1]]; # what are the corresponding rho & mu values?
   best_mus[subj] = mu_values[indexes[2]];
 }

# look at all best rho & mu per participant
grid_bestRho = array(dim = c(number_of_clean_subjects,1));
grid_bestMu = array(dim = c(number_of_clean_subjects,1));
for (subj in 1:number_of_clean_subjects){
  subj_id = keep_participants[subj];
  
  tmpdata = clean_data_dm[clean_data_dm$subjectnumber == subj_id,];
  
  grid_bestRho[subj] = rho_values[unique(tmpdata$bestRho)];
  grid_bestMu[subj] = mu_values[unique(tmpdata$bestMu)];
}

# First, check fresh grid search best Rho & Mu against experiment-executed grid search Rho & Mu
# (should be trivial and match!)

if (any((grid_bestRho - best_rhos) != 0)){
  print('MISMATCH!')
}else{
  print('Grid search values match (as expected)')
}

# Then check estimated parameters vs. grid search parameters
plot(grid_bestRho,estimated_parameters[,1], main = 'RHO', xlim = c(0, 2), ylim = c(0, 2))
lines(c(0, 2), c(0, 2))

plot(grid_bestMu,estimated_parameters[,2], main = 'MU', xlim = c(0, 100), ylim = c(0, 100))
lines(c(0, 100), c(0, 100))

hist(grid_bestRho - estimated_parameters[,1], xlim = c(-2,2),
     breaks = seq(from = -2, to = 2, by = 0.05), main = 'Difference in Rho Estimates',
     ylab = 'Participants', xlab = 'Grid estimate - MLE estimate')
hist(grid_bestMu - estimated_parameters[,2], xlim = c(-100,100), 
     breaks = seq(from = -100, to = 100, by = 1), main = 'Difference in Mu Estimates',
     ylab = 'Participants', xlab = 'Grid estimate - MLE estimate')
# This is supposed to look silly! Should cluster around 0
# ... and it does, as of 2/3/23!

t.test(grid_bestRho, estimated_parameters[,1], paired = T) # no sig. diff (rho)
t.test(grid_bestMu, estimated_parameters[,2], paired = T) # no sig. diff (mu)

# A: YES, grid-search values match optimized values very closely.

### Create Continuous difficulty metric ###

clean_data_dm$diff_cont = abs(abs(clean_data_dm$choiceP - 0.5)*2-1);
# EASY = 0
# DIFFICULT = 1

### Create Categorical difficulty metric ###

clean_data_dm$diff_cat = 0; # MEDIUM
clean_data_dm$diff_cat[clean_data_dm$diff_cont < .3] = -1; # EASY (p's < .15 or > .85)
clean_data_dm$diff_cat[clean_data_dm$diff_cont > .7] = 1; # DIFFICULT (p's > .35 AND < .65)
clean_data_dm$diff_cat[clean_data_dm$static0dynamic1 == 0] = NA;

# Q:DO RT differ across condiitions? Reaction times for easy risky, easy safe, and hard (hard > easy (either))
#mean easy RT 
mean_rt_easy = array(dim = c(number_of_clean_subjects, 1));
mean_rt_diff = array(dim = c(number_of_clean_subjects, 1));
mean_rt_easyACC = array(dim = c(number_of_clean_subjects, 1));
mean_rt_easyREJ = array(dim = c(number_of_clean_subjects, 1));

for (subj in 1:number_of_clean_subjects){
  subj_id = keep_participants[subj];
  tmpdata = data_dm[data_dm$subjectnumber == subj_id,];
  tmpdata = tmpdata[tmpdata$easyP1difficultN1 == 1,];
  mean_rt_easy[subj] = mean(tmpdata$reactiontime, na.rm = T)
  mean_rt_easyACC[subj] = mean(tmpdata$reactiontime[(tmpdata$easyP1difficultN1 == 1) & (tmpdata$choiceP > .5)], na.rm = T);
  mean_rt_easyREJ[subj] = mean(tmpdata$reactiontime[(tmpdata$easyP1difficultN1 == 1) & (tmpdata$choiceP < .5)], na.rm = T)
}

for (subj in 1:number_of_clean_subjects){
  subj_id = keep_participants[subj];
  tmpdata = data_dm[data_dm$subjectnumber == subj_id,];
  tmpdata = tmpdata[tmpdata$easyP1difficultN1 == -1,];
  mean_rt_diff[subj] = mean(tmpdata$reactiontime, na.rm = T)
}

#differences between averages
mean_rt_difference = mean_rt_diff - mean_rt_easy;  # a negative number means on average hard was longer, positive number means on average easy was shorter duration 
plot(mean_rt_diff, mean_rt_easy, main = 'AVG RT', xlim = c(0, 4), ylim = c(0, 4))
lines(c(0, 4), c(0, 4))

# test easy RTs vs. diff. RTs 
t.test(mean_rt_easy,mean_rt_diff, paired = T); #significant difference between rt easy and hard, WOOHOO! 2/27/23

#A: yes, looks like on average rt of difficult decisions was slower than avg rt of easy decisions


# per person basis of easy RTs vs diff. RTs?? HELP, THIS DOESNT WORK WAY I WANT IT TOO!!! 
#Q: are easy choices similarly fast across people & are difficult choices similarly slower across people? 
for (subj in 1:number_of_clean_subjects){
  subj_id = keep_participants[subj];
  tmpdata = clean_data_dm[clean_data_dm$subjectnumber == subj_id,]; # identify this person's data
  
  # test their easy trials vs. their difficult trials
  stat_result = t.test(tmpdata$reactiontime[tmpdata$easyP1difficultN1 == 1], tmpdata$reactiontime[tmpdata$easyP1difficultN1 == -1])
  
  hist(tmpdata$reactiontime[tmpdata$easyP1difficultN1 == -1], 
       breaks = seq(from = 0, to = 4, by = .25), col = rgb(1,0,0,0.6), xlim = c(0,4), ylim = c(0,30),
       main = sprintf('Subject %g: p = %.03f', subj_id, stat_result$p.value));
  hist(tmpdata$reactiontime[tmpdata$easyP1difficultN1 == 1], 
       breaks = seq(from = 0, to = 4, by = .25), col = rgb(0,0,1,0.6), add = T)
}

#Variance test, to see differences in RT per person?? 
var.test(mean_rt_easy, mean_rt_diff) # sig difference 2/27/23
#A:RTs more variable across people for diff. than easy trials


# test easy ACC vs. easy REJ RTs (and plot against each other)
# Q: Can we treat easy ACC & REJ RTs as the same kind of thing? 
t.test(mean_rt_easyACC,mean_rt_easyREJ, paired = T); #not sig. diff between easy types 2/27/23
plot(mean_rt_easyACC, mean_rt_easyREJ, main = 'RT EASY REJ & EASY ACC', xlim = c(0,4), ylim = c(0,4))
lines(c(0,4), c(0,4))

# A: yes they are very similar & not significantly different, what we want to see. CAN collapse easy REJ and easy ACC as "easy"

### SUBSEQUENT DIFFICULTY ANALYSIS ###
#Q:Does RT change depending on subsequent trial types? 
#mean RT subsequent #
diff_diff_mean_rt = array(dim = c(number_of_clean_subjects, 1));
easy_easy_mean_rt = array(dim = c(number_of_clean_subjects, 1));
easy_diff_mean_rt = array(dim = c(number_of_clean_subjects, 1));
diff_easy_mean_rt = array(dim = c(number_of_clean_subjects, 1));

for (subj in 1:number_of_clean_subjects){
  subj_id = keep_participants[subj]
  tmpdata = data_dm[data_dm$subjectnumber == subj_id,]
  easy_easy_mean_rt[subj] = mean(tmpdata$reactiontime[(tmpdata$easyP1difficultN1[52:170] == 1) &
                                                        (tmpdata$easyP1difficultN1[51:169] == 1)], na.rm = T);
  
  diff_diff_mean_rt[subj] = mean(tmpdata$reactiontime[(tmpdata$easyP1difficultN1[52:170] == -1) & 
                                                        (tmpdata$easyP1difficultN1[51:169] == -1)], na.rm = T);
  
  diff_easy_mean_rt[subj] = mean(tmpdata$reactiontime[(tmpdata$easyP1difficultN1[52:170] == 1) & 
                                                        (tmpdata$easyP1difficultN1[51:169] == -1)], na.rm = T);
  
  easy_diff_mean_rt[subj] = mean(tmpdata$reactiontime[(tmpdata$easyP1difficultN1[52:170] == -1) &
                                                        (tmpdata$easyP1difficultN1[51:169] == 1)], na.rm = T);
}

# does prev. trial type influence RT on the current trial
t.test(easy_easy_mean_rt, diff_easy_mean_rt, paired = T); # NOT for easy 
t.test(diff_diff_mean_rt, easy_diff_mean_rt, paired = T); # NOT for difficult
# A: Not at this level, not with this dataset so far (2/27/23)

# Plot the current trial as a function of prev. trial type
plot(easy_easy_mean_rt, diff_easy_mean_rt); lines(c(1,2), c(1,2)); # NOT for easy
plot(diff_diff_mean_rt, easy_diff_mean_rt); lines(c(1,2), c(1,2)); # NOT for difficult

t.test(diff_diff_mean_rt, easy_easy_mean_rt, paired = T); # not sig diff 2/27/23
#A: TO BE DETERMINED, but right now it looks like RT based upon subsequent trials is not sig different 

#Q: Does gambling behavior change based upon previous trial difficulty? 
#mean p_gamble subsequent 
diff_diff_mean_pgamble = array(dim = c(number_of_clean_subjects, 1));
easy_easy_mean_pgamble = array(dim = c(number_of_clean_subjects, 1));
easy_diff_mean_pgamble = array(dim = c(number_of_clean_subjects, 1));
diff_easy_mean_pgamble = array(dim = c(number_of_clean_subjects, 1));

for (subj in 1:number_of_clean_subjects){
  subj_id = keep_participants[subj]
  tmpdata = data_dm[data_dm$subjectnumber == subj_id,]
  diff_diff_mean_pgamble[subj] = mean(tmpdata$choice[(tmpdata$easyP1difficultN1[52:170] == -1) &
                                                      (tmpdata$easyP1difficultN1[51:169] == -1)], na.rm = T);
  
  easy_easy_mean_pgamble[subj] = mean(tmpdata$choice[(tmpdata$easyP1difficultN1[52:170] == 1) &
                                                       (tmpdata$easyP1difficultN1[51:169] == 1)], na.rm = T);
    
  
  easy_diff_mean_pgamble[subj] = mean(tmpdata$choice[(tmpdata$easyP1difficultN1[52:170] == 1) &
                                                       (tmpdata$easyP1difficultN1[51:169] == -1)], na.rm = T);
  

  diff_easy_mean_pgamble[subj] = mean(tmpdata$choice[(tmpdata$easyP1difficultN1[52:170] == -1) &
                                                       (tmpdata$easyP1difficultN1[51:169] == 1)], na.rm = T);
}  

t.test(easy_easy_mean_pgamble, easy_diff_mean_pgamble, paired = T); # not sig diff 2/27/23
t.test(diff_diff_mean_pgamble, easy_diff_mean_pgamble, paired = T); # not sig diff 2/27/23
t.test(diff_diff_mean_pgamble, easy_easy_mean_pgamble, paired = T); # not sig diff 2/27/23
#A:TO BE DETERMINED, but right now it looks like pgamble based upon subsequent trials is not significantly differnt  

### Regression LM (Contextual) ### 
#RT on trials regressions
library(lme4)
library(lmerTest)

# ADVICE ON REGRESSIONS
# 1. work on RT instead of decisions
# 2. work on sqrt(RT) instead of RT
clean_data_dm$sqrtRT = sqrt(clean_data_dm$reactiontime);
# 3. focus effort on creating good regressors

m0 = lm(sqrtRT ~ 1 + easyP1difficultN1, data = clean_data_dm);
summary(m0)

m0rfx = lmer(sqrtRT ~ 1 + easyP1difficultN1 + (1 | subjectnumber), data = clean_data_dm);
summary(m0rfx)

m0_dynonly_rfx = lmer(sqrtRT ~ 1 + easyP1difficultN1 + (1 | subjectnumber),
                      data = clean_data_dm[clean_data_dm$static0dynamic1 == 1,]);
summary(m0_dynonly_rfx)

# input shifted version of desired content
clean_data_dm$easyP1difficultN1_prev = c(0,clean_data_dm$easyP1difficultN1[1:(length(clean_data_dm$easyP1difficultN1)-1)])
# fix the few problematic trials (#1)
clean_data_dm$easyP1difficultN1_prev[clean_data_dm$trialnumber == 1] = 0;
# input shifted version of desired content
clean_data_dm$sqrtRT_prev = c(NA,clean_data_dm$sqrtRT[1:(length(clean_data_dm$sqrtRT)-1)])
# fix the few problematic trials (#1)
clean_data_dm$sqrtRT_prev[clean_data_dm$trialnumber == 1] = NA;

#Run Regression
#mean Rt after easy vs after hard trials?
m1_prev = lm(sqrtRT ~ 1 + easyP1difficultN1 + easyP1difficultN1_prev, data = clean_data_dm);
summary(m1_prev)

m1_prev_intxn = lm(sqrtRT ~ 1 + easyP1difficultN1 * easyP1difficultN1_prev, data = clean_data_dm);
summary(m1_prev_intxn)

# RFX Versions (good b/c of high indiv. variability in baseline RTs!)
m1_prev_rfx = lmer(sqrtRT ~ 1 + easyP1difficultN1 + easyP1difficultN1_prev + (1 | subjectnumber), data = clean_data_dm);
summary(m1_prev_rfx)

m1_prev_intxn_rfx = lmer(sqrtRT ~ 1 + easyP1difficultN1 * easyP1difficultN1_prev + (1 | subjectnumber), data = clean_data_dm);
summary(m1_prev_intxn_rfx)

m2_prev_intxn = lmer(sqrtRT ~ 1 + easyP1difficultN1 * sqrtRT_prev + (1 | subjectnumber), data = clean_data_dm);
summary(m2_prev_intxn)
# prev. reaction time predicts subsequent reaction time
# BE CAREFUL - lots of things cause autocorrelation in RTs!

m0_dynonly_rfx = lmer(sqrtRT ~ 1 + easyP1difficultN1 + easyP1difficultN1_prev + (1 | subjectnumber),
                      data = clean_data_dm[clean_data_dm$static0dynamic1 == 1,]);
summary(m0_dynonly_rfx)

# ways forward w/ regressions
# - use categorical difficulty metrics instead of easy/difficult design categories (diff_cat), still looking at RT after easy vs hard
#DO I NEED TO FURTHER DEFINE THINGS IN DIFF_CAT/CONT??
  # diff_cat easy = -1, diff_cat hard = 1, diff_cat medium = 0 

m0 = lm(sqrtRT ~ 1 + diff_cat , data = clean_data_dm); # diff_cat easy = -1 
summary(m0) 

m0rfx = lmer(sqrtRT ~ 1 + diff_cat + (1 | subjectnumber), data = clean_data_dm);
summary(m0rfx)

m0_dynonly_rfx = lmer(sqrtRT ~ 1 + diff_cat  + (1 | subjectnumber),
                      data = clean_data_dm[clean_data_dm$static0dynamic1 == 1,]);
summary(m0_dynonly_rfx)
#A:correlation of fixed effects = 0 suggesting no correlation between sqrtRT with diff_cat & subject number
#statistical significant diff_cat and intercept, so they are associated with RT?
# as diff_cat changes,RT changes? 

#use continuous diff metric instead of easy/difficult 
m0 = lm(sqrtRT ~ 1 + diff_cont , data = clean_data_dm);
summary(m0) 

m0rfx = lmer(sqrtRT ~ 1 + diff_cont + (1 | subjectnumber), data = clean_data_dm);
summary(m0rfx)

m0_dynonly_rfx = lmer(sqrtRT ~ 1 + diff_cont + (1 | subjectnumber),
                      data = clean_data_dm[clean_data_dm$static0dynamic1 == 1,]);
summary(m0_dynonly_rfx)

#A: correlation of fixed effects = -0.151, a negative correlation between RT and continuous difficult metric, where easy = 0 diff = 1.
#statistically significant diff_cont and intercept, so they are associated with RT??


#Q: does previous RT predict current rt on normal easy diff & also categorical and continuous diff metrics? 
#RT prev & easy diff and easy diff prev...RFX Versions (good b/c of high indiv. variability in baseline RTs!)
m1_prev_rfx = lmer(sqrtRT_prev ~ 1 + easyP1difficultN1 + easyP1difficultN1_prev + (1 | subjectnumber), data = clean_data_dm);
summary(m1_prev_rfx)

m1_prev_intxn_rfx = lmer(sqrtRT_prev ~ 1 + easyP1difficultN1 * easyP1difficultN1_prev + (1 | subjectnumber), data = clean_data_dm);
summary(m1_prev_intxn_rfx)

m2_prev_intxn = lmer(sqrtRT_prev ~ 1 + easyP1difficultN1 * sqrtRT + (1 | subjectnumber), data = clean_data_dm);
summary(m2_prev_intxn)
#A: THIS MODEL & results  CONFUSED ME...^^^ 
  # goal = to see if previous RT predicts current RT on easy diff trials in cont, cat, and predtermined easy diff trials... 

# Q: does previous RT depend/relate/interact to categorical difficulty measure?  
m0 = lm(sqrtRT_prev ~ 1 + diff_cat , data = clean_data_dm);
summary(m0)

m0rfx = lmer(sqrtRT_prev ~ 1 + diff_cat + (1 | subjectnumber), data = clean_data_dm);
summary(m0rfx)

m0_dynonly_rfx = lmer(sqrtRT_prev ~ 1 + diff_cat + (1 | subjectnumber),
                      data = clean_data_dm[clean_data_dm$static0dynamic1 == 1,]);
summary(m0_dynonly_rfx)

#A: p = 0.79 not significant, but intercept = significant so the rt is sig when diff_cat = 0(medium)??
  # also no correlation between two predictors diff_cat & subjectnumber with sqrtRT_prev 


# use previous reaction time as an index of EXPERIENCED difficulty # is this correct or do I need to eliminate easy diff measure? 
#max = 4 seconds 
#min = 0.86 seconds
#mean_rt_easy = array(dim = c(number_of_clean_subjects, 1));
#mean_rt_diff

max(tmpdata$number_digits[(tmpdata$forward1backward0 == 1) & (tmpdata$correct == 1)], na.rm = T);

for (subj in 1:number_of_clean_subjects){
  subj_id = keep_participants[subj]
  tmpdata = data_dm[data_dm$subjectnumber == subj_id,]
  slowest_RT_type = mean(tmpdata$reactiontime == 3-4 & (tmpdata$static0dynamic1 == 1);
  next_slowest_RT_type = mean(tmpdata$reactiontime == 2-3) & (tmpdata$static0dynamic1 == 1); 
  faster_RT_type = mean(tmpdata$reactiontime == 1-2) & (tmpdata$static0dynamic1 == 1);
  fastest_RT_type= mean(tmpdata$reactiontime < 1 & (tmpdata$static0dynamic1 == 1);
}


#m1_prev_RT = lm(easyP1difficultN1 ~ 1 + sqrtRT_prev + easyP1difficultN1_prev, data = clean_data_dm);
#summary(m1_prev_RT)

#m1_prev_intxn_RT = lm(easyP1difficultN1 ~ 1 + sqrtRT_prev * easyP1difficultN1_prev, data = clean_data_dm);
#summary(m1_prev_intxn)

#m1_prev_intxn_rfx_RT = lmer(easyP1difficultN1 ~ 1 + sqrtRT_prev * easyP1difficultN1_prev + (1 | subjectnumber), data = clean_data_dm);
#summary(m1_prev_intxn_rfx)

# COG CONTROL REGRESSION & RT- use digit span info to account for capacity...


### WM Task ###

## TOTAL NUMBER FS & BS Correct (FS & BS)
FS_correct = array(dim = c(number_of_clean_subjects,1));
BS_correct = array(dim = c(number_of_clean_subjects,1));

for (subj in 1:number_of_clean_subjects) {
  subj_id = keep_participants[subj]
  tmpdata = data_wm[data_wm$subjectnumber == subj_id, ]
  # defines this person's data
  FS_correct[subj] = sum(tmpdata$correct[tmpdata$forward1backward0 == 1], na.rm =
                           T)
  
  BS_correct[subj] = sum(tmpdata$correct[tmpdata$forward1backward0 == 0], na.rm =
                           T)
}
## Q:is there a statistically sig difference between number of FS and BS #correct/14? 
t.test(FS_correct, BS_correct, paired = T);
#A: not significant diff (2/27/23), suggestive that overall number of trials correct on either fs or bs is similar.

# FS & BS max number_digits/length when correct (BEST SPAN)
#Q: is there a difference in max number of digits correct in FS vs BS (comparing fs max digit length correct to bs)
best_span_FS = array(dim = c(number_of_clean_subjects,1));
best_span_BS = array(dim = c(number_of_clean_subjects,1));

for (subj in 1:number_of_clean_subjects){
  subj_id = keep_participants[subj]
  tmpdata = data_wm[data_wm$subjectnumber == subj_id, ]
  best_span_FS[subj] = max(tmpdata$number_digits[(tmpdata$forward1backward0 == 1) & (tmpdata$correct == 1)], na.rm = T);
  best_span_BS[subj] = max(tmpdata$number_digits[(tmpdata$forward1backward0 == 0) & (tmpdata$correct == 1)], na.rm = T);
}

t.test(max_number_digits_correct_FS, max_number_digits_correct_BS, paired = T);
#A: yes, significant difference between max digit number/length FS correct compared to BS correct (2/27/23)!

#HELP
# Max correct before 2 errors in a row @ a given length (BEST RELIABLE SPAN)! 
best_reliable_span = array(dim = c(number_of_clean_subjects, 1));

for (subj in 1:number_of_clean_subjects){
  subj_id = keep_participants[subj];
  tmpdata = data_wm[data_wm$subjectnumber == subj_id,];
  best_reliable_span_FS[subj] = max(tmpdata$number_digits[(tmpdata$forward1backward0 == 1) & (tmpdata$correct == 1) & (tmpdata$correct[2:14]- 1 == 1)], na.rm = T);
}

# total # of trials before 2 errors in a row @ a given length (QUALITY OF EFFORT?)
quality_of_span_FS = array(dim = c(number_of_clean_subjects,1));
quality_of_span_BS = array(dim = c(number_of_clean_subjects,1));

n_trials <- 14 
n_errors <- 0 
last_error <-FALSE

if (last_error){
  n_errors <- 2;
  print("number of trials before 2 errors in a row", n_trials)
  } else{
    n_errors <-1
    last_error <-TRUE
  #} else { 
   # n_errors <-0 
   # last_error <- FALSE
    }

for (subj in 1:number_of_clean_subjects){
  subj_id = keep_participants[subj];
  tmpdata = data_wm[data_wm$subjectnumber == subj_id,]; # defines this person's data
  
  quality_of_span_FS[subj] = sum(tmpdata$correct[tmpdata$forward1backward0 == 1], na.rm=T);
  quality_of_span_BS[subj] =sum(tmpdata$correct[tmpdata$forward1backward0 == 0], na.rm=T);
}

### Connecting Decision-Making & Working Memory #### 
#see how far back if at all previous choice difficulty mattered to cog capacity measures
#see how RT as measure of choice diff relates to cog capacity 

#Q: Do high controllers have diff avg RT (predicted faster avg) compared to low controllers? 
MedianValueFS = array(dim = c(number_of_clean_subjects,1));
MedianValueBS = array(dim = c(number_of_clean_subjects,1));
highcontroller_FS_avgRT = array(dim = c(number_of_clean_subjects,1));
lowcontroller_FS_avgRT = array(dim = c(number_of_clean_subjects,1));
highcontroller_BS_avgRT = array(dim = c(number_of_clean_subjects,1));
lowcontroller_BS_avgRT = array(dim = c(number_of_clean_subjects,1));

#median value = 7.5 so want to do median split. 
highcontroller_FS = best_span_FS > 7.5
lowcontroller_FS = best_span_FS < 7.5

highcontroller_BS = best_span_BS > 6.5
lowcontroller_BS = best_span_BS < 6.5 

for (subj in 1:number_of_clean_subjects){
  subj_id = keep_participants[subj];
  tmpdata = data_wm[data_wm$subjectnumber == subj_id,];
  MedianValueFS[subj] <- median(best_span_FS);
  MedianValueBS[subj] <- median(best_span_BS);
  highcontroller_FS_avgRT = mean(tmpdata$reactiontime[tmpdata$highcontroller_FS = T]); # goal: mean RT for particpants who = highcontroller_FS
  #lowcontroller_FS_avgRT = 
  #highcontroller_BS_avgRT =
  #lowcontroller_BS_avgRT =
}


#Q; Range of gap between easy/diff RT on per person basis is this related to cog capacity, high vs low controllers and thier behaivor on diff vs easy choices 

#Q: how does capacity relate to trial types (static/dynamic, easy only, hard only)

#Q: 

#2nd looks at cognitive capacity and choice behavior, do high controllers experince less gambling behvaior ie less risky? 
#continuous variable of cog control? 
#see behavioral (rt) variability in the regression based upon inc or dec of capacity?
#see individual and group differences? 
