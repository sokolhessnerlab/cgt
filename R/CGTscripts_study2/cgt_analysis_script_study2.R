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
     col = 'green', breaks = seq(from = 0, to = 1, by = 0.05), xlim = c(0,1), );
hist(easyREJ_mean_pgamble,
     col = 'red',   breaks = seq(from = 0, to = 1, by = 0.05), add = T);
hist(diff_mean_pgamble,
     col = 'blue',  breaks = seq(from = 0, to = 1, by = 0.05), add = T);
# A: As expected red < blue < green (easy reject < difficult < easy acc)

# Q: Can we collapse across easy accept & reject trials based on relative distance from 0.5?
plot(abs(easyACC_mean_pgamble-.5),abs(easyREJ_mean_pgamble-.5),xlim = c(0,.5), ylim = c(0,.5),
     xlab = 'Distance from 0.5 for EASY ACC', ylab = 'Distance from 0.5 for EASY REJ')
lines(x = c(0,1), y = c(0,1), col = 'blue')
# ... we want these to be clustered together on the blue line, close to 0.5
# ... and they are! As of 2/3/23

# Statistically test relative difficulty observed in easy ACC vs. easy REJ
t.test(abs(easyACC_mean_pgamble-.5), abs(easyREJ_mean_pgamble-.5), paired = T)

# A: Yes, we can treat all easy trials as similarly easy (whether easy ACC or REJ)


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
plot(mean_rt_diff, mean_rt_easy, main = 'AVG RT', xlim = c(0, 2), ylim = c(0, 2))
lines(c(0, 2), c(0, 2))

# test easy RTs vs. diff. RTs 
t.test(mean_rt_easy,mean_rt_diff, paired = T); #significant difference between rt easy and hard, WOOHOO! 

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
var.test(mean_rt_easy, mean_rt_diff) # sig difference; RTs more variable across people for diff. than easy trials
#A: HELP SECTION^^ 

# test easy ACC vs. easy REJ RTs (and plot against each other)
# Q: Can we treat easy ACC & REJ RTs as the same kind of thing? 
t.test(mean_rt_easyACC,mean_rt_easyREJ, paired = T); #not sig. diff between easy types
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
# A: Not at this level, not with this dataset so far (2/7/23)

t.test(diff_diff_mean_rt, easy_easy_mean_rt, paired = T); # not sig diff 2/6/23
#A: TO BE DETERMINED, but right now it looks like RT based upon subsequent trials is not sig different 

#plot(diff_diff_mean_rt[subj],diff_easy_mean_rt[subj], main ='diff/diff RT', xlim = c(0,2), ylim = c(0,2))
#lines(c(0,2.0), c(0,2.0))

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

t.test(easy_easy_mean_pgamble, easy_diff_mean_pgamble, paired = T); # not sig diff 2/6/23
t.test(diff_diff_mean_pgamble, easy_diff_mean_pgamble, paired = T); # not sig diff 2/6/23
t.test(diff_diff_mean_pgamble, easy_easy_mean_pgamble, paired = T); # not sig diff 2/6/23
#A:TO BE DETERMINED, but right now it looks like RT based upon subsequent trials is not significant different 

### Regression LM (Contextual) ### 
#RT on trials regressions
#model1_reactiontime_choices <- glmer( XXX?? data = clean_data_dm, family = "binomial")
#model2_difficulty_reactiontimes <- glmer(XXXXX data =clean_data_dm, family = "binomal" )
#summary(model)

library(lme4)

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

#shifted version of easy and difficult 
#create easyP1difficultN1_prev 
easyP1difficultN1_prev = array(dim = c(number_of_clean_subjects, 1));


for (subj in 1:number_of_clean_subjects){
  subj_id = keep_participants[subj]
  tmpdata = data_dm[data_dm$subjectnumber == subj_id,]
  easyP1difficultN1_prev[subj] = slice_head(clean_data_dm, 51, .preserve = FALSE)
}

#install.packages('dplyr')
library(dplyr)

m1 = lm(sqrtRT ~ 1 + easyP1difficultN1_prev, data = clean_data_dm);
summary(m1)

m0rfx = lmer(sqrtRT ~ 1 + easyP1difficultN1_prev + (1 | subjectnumber), data = clean_data_dm);
summary(m0rfx)

m0_dynonly_rfx = lmer(sqrtRT ~ 1 + easyP1difficultN1_prev + (1 | subjectnumber),
                      data = clean_data_dm[clean_data_dm$static0dynamic1 == 1,]);
summary(m0_dynonly_rfx)


### WM Task ### TO BE WORKED ON...

## Probability correct (FS & BS)
FS_correct = array(dim = c(number_of_clean_subjects,1));
BS_correct = array(dim = c(number_of_clean_subjects,1));

for (subj in 1:number_of_clean_subjects){
subj_id = keep_participants[subj];
tmpdata = data_wm[data_wm$subjectnumber == subj_id,]; # defines this person's data
FS_correct[subj] = sum(tmpdata$correct[tmpdata$forward1backward0 == 1], na.rm=T);
BS_correct[subj] = sum(tmpdata$correct[tmpdata$forward1backward0 == 0], na.rm=T);
}
#^^ I think we talked about removing if too high... for people with 14... #

## Forward span
# max correct before 2 errors in a row @ a given length (BEST RELIABLE SPAN)!
best_reliable_span = array(dim = c(number_of_clean_subjects,1));
error_in_a_row = array(dim = c(number_of_clean_subjects,1));

#for (subj in 1:number_of_clean_subjects){
  #subj_id = keep_participants[subj];
  #tmpdata = data_wm[data_wm$subjectnumber == subj_id,];
  #best_reliable_span[subj] = sum(data_wm$correctdigits[data_wm$correct == 1]);
  #filter(error_in_a_row > 0 );
  #summarize(best_reliable_span = max(run_length));
  #filter(error_in_a_row == 2); 
  #summarize(best_reliable_span = max(correctdigits))
  #} 

# ^^ what function do I use here not unique and not max? ^^ 

# total # of trials before 2 errors in a row @ a given length (QUALITY OF EF?)

# max correct ever (BEST SPAN PERIOD)

## Backward span (max correct before 2 errors in a row; max correct ever)
# max correct before 2 errors in a row @ a given length (BEST RELIABLE SPAN)

# total # of trials before 2 errors in a row @ a given length (QUALITY OF EF?)

# max correct ever (BEST SPAN PERIOD)

### Connecting Decision-Making & Working Memory #### (use glmr)
#1st looks at RT and choice difficulty 
#General Linear Regression mixed model analysis (group level analysis)
#account for choice difficulty 
#see how far back if at all previous choice difficulty mattered
#mean Rt after easy vs after hard trials
#account for previous trial RT (ALL trail basis)

#2nd looks at cognitive capacity and choice behavior 
#continuous variable of cog control? 
#see behavioral (rt) variability in the regression based upon inc or dec of capacity?
#see individual and group differences? 
