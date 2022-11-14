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

#### Basic Data Analysis ####
# (Separately for DM & WM data)
# Descriptives & simple averages of task performance

### DM task ###
# Analysis for static trials: Mean p(gamble), optimization
p_gamble = array(dim = c(number_of_subjects,1));
for (subj in 1:number_of_subjects){
  tmpdata = data_dm[data_dm$subjectnumber == subj,];
  
  p_gamble[subj] = sum(tmpdata$choice)/(170) #getting some NA idk why? 
}

# Does optimized analysis match grid search analysis? WORK IN PROGRESS
bestRho = array(dim = c(number_of_subjects,1));

for (subj in 1:number_of_subjects){
  tmpdata = data_dm[data_dm$subjectnumber == subj,];
  
  bestRho[subj] = sum(tmpdata$bestRho)
}
# (should be very close!)


# Did choices align with predictions (re: easy risky and easy safe and hard)


# Reaction times for easy risky, easy safe, and hard (hard > easy (either))



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

