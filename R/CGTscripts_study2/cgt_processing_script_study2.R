# CGT Data Processing Script STUDY 2
#
# Script to process the data collected SONA SYSTEMS 2023
# (Control & Gambling Task) study.

#identify the working directory paths
main_wd = '/Volumes/shlab/Projects/CGT/CGT_study2/';

rawdata_wd = paste0(main_wd,'rawdata_study2/');
processeddata_wd = paste0(main_wd,'processeddata_study2/')

# set the working directory
setwd(rawdata_wd);

# List all the data files
fn = dir(pattern = glob2rx('CGTgamblingSpanTasks_*2023*.csv'),full.names = T);

# Identify the number of participants from the file listing
number_of_subjects = length(fn);

# Store some basic information about size of the decision-making task
num_static_trials = 50;
num_dynamic_trials = 120;
number_of_dm_trials_per_person = num_static_trials + num_dynamic_trials; # static = 50, dynamic = 120

# Set up variables to hold decision-making data
column_names_dm = c(
  'trialnumber',
  'subjectnumber',
  'sonaID',
  'riskyopt1',
  'riskyopt2',
  'safe',
  'choice',
  'reactiontime',
  'outcome',
  'ischecktrial',
  'static0dynamic1',
  'easyP1difficultN1',
  'choiceP',
  'bestRho',
  'bestMu'
);

data_dm = array(data = NA, dim = c(0, length(column_names_dm)));
colnames(data_dm) <- column_names_dm

# Set up variables to hold working memory data
number_of_wm_trials_per_person = 28; # 14 forward, 14 backward

column_names_rawdata_wm = c(
  'digitsForTrial', #both FS & BS digits
  'textbox.text', #FS response
  'textboxBS.text', #BS response
  'trialNumber', #both trial number
  'digitLoop.thisRepN', #FS number of digits
  'digitLoopBS.thisRepN', #BS number of digits
  'correct' #both FS & BS
);

# this will have trials in rows, these will be col. names
column_names_wm = c(
  'trialnumber',
  'subjectnumber',
  'sonaID',
  'number_digits',
  'forward1backward0',
  'correct'
);

data_wm = array(data = NA, dim = c(0, length(column_names_wm)));
colnames(data_wm) <- column_names_wm

# Loop
for(s in 1:number_of_subjects){
  # Load in the data
  tmpdata = read.csv(fn[s]);
  
  # DECISION-MAKING DATA
  dm_data_to_add = array(data = NA, dim = c(number_of_dm_trials_per_person,length(column_names_dm)));
  
  dm_index_static = is.finite(tmpdata$staticRDM.thisTrialN);
  dm_index_dynamic = is.finite(tmpdata$dynamicRDM.thisTrialN);
  
  tmp_trialnum = c(tmpdata$staticRDM.thisTrialN[dm_index_static] + 1,
                   tmpdata$dynamicRDM.thisTrialN[dm_index_dynamic] + num_static_trials + 1);
  
  dm_data_to_add[,1] = tmp_trialnum; # trial number
  dm_data_to_add[,2] = s; # subject number
  dm_data_to_add[,3] = unique(tmpdata$participant);
  
  tmp_riskyopt1 = c(tmpdata$riskyoption1[dm_index_static],
                    tmpdata$riskyoption1[dm_index_dynamic]);
  tmp_riskyopt2 = c(tmpdata$riskyoption2[dm_index_static],
                    tmpdata$riskyoption2[dm_index_dynamic]);
  tmp_safe = c(tmpdata$safeoption[dm_index_static],
               tmpdata$safeoption[dm_index_dynamic]);
  
  dm_data_to_add[,4:6] = cbind(tmp_riskyopt1,tmp_riskyopt2,tmp_safe) # dollar amounts
  
  dm_data_to_add[,7] = c(tmpdata$choices[dm_index_static],
                         tmpdata$choices[dm_index_dynamic]); # choices
  
  dm_data_to_add[,8] = c(tmpdata$realChoice.rt[dm_index_static],
                         tmpdata$realChoice.rt[dm_index_dynamic]); # RTs
  
  dm_data_to_add[,9] = c(tmpdata$outcomes[dm_index_static],
                         tmpdata$outcomes[dm_index_dynamic]); # outcomes
  
  dm_data_to_add[,10] = c(tmpdata$ischecktrial[dm_index_static],
                         array(data = 0, dim = c(1,num_dynamic_trials))); # is check trial
  
  dm_data_to_add[,11] = c(array(data = 0, dim = c(1,num_static_trials)),
                          array(data = 1, dim = c(1,num_dynamic_trials))); # static 0, dynamic 1
  
  dm_data_to_add[,12] = c(array(data = 0, dim = c(1,num_static_trials)),
                          tmpdata$easy0difficult1[dm_index_dynamic]*-2 + 1); # easy +1, difficult -1
  
  dm_data_to_add[,13] = c(array(data = NA, dim = c(1,num_static_trials)),
                          tmpdata$choiceP[dm_index_dynamic]); # choice probability on easy/diff dynamic trials
  
  dm_data_to_add[,14] = tmpdata$bestRho[is.finite(tmpdata$bestRho)];
  dm_data_to_add[,15] = tmpdata$bestMu[is.finite(tmpdata$bestMu)];
  
  
  # Add this person's DM data to the total DM data.
  data_dm = rbind(data_dm,dm_data_to_add);
  
  # WORKING MEMORY
  wm_data_to_add = array(data = NA, dim = c(number_of_wm_trials_per_person,length(column_names_wm)));
  
  wm_trial_indices = which(!is.na(tmpdata$trialNumber));
  
  wm_data_to_add[,1] = 1:number_of_wm_trials_per_person; # trial numbers
  wm_data_to_add[,2] = s; # subject number
  wm_data_to_add[,3] = unique(tmpdata$participant);
  
  wm_data_to_add[,4] = (nchar(tmpdata$digitsForTrial[wm_trial_indices-1])-1)/2; # number of digits on the trial
  
  wm_data_to_add[1:14,5] = 1; # forward is always first
  wm_data_to_add[15:28,5] = 0; # backward is always second
  
  wm_data_to_add[,6] = tmpdata$correct[wm_trial_indices]; # correct = 1, incorrect = 0
  
  data_wm = rbind(data_wm,wm_data_to_add);
}

data_dm = as.data.frame(data_dm) # make it a data frame so it plays nice
data_wm = as.data.frame(data_wm)


# Load End of Task Questionnaire Data

raw_eot_data <- read.csv("EndOfTaskQ_RawData_CGT.csv") # End Of Task (EOT)
raw_eot_data = raw_eot_data[-1,]

column_names_eot = c(
  'nfc_sum',
  'fraction_attn_check_correct',
  'energy_level_beginning',
  'energy_level_end',
  'performance_riskydecisionmaking',
  'performance_digitspan',
  'age',
  'gender',
  'ethnicity',
  'race',
  'highest_degree_attained',
  'political_orientation',
  'sona_ID'
);

number_of_qualtrics_subjects = dim(raw_eot_data)[1]; # is 64

data_eot = array(data = NA, dim = c(number_of_qualtrics_subjects, length(column_names_eot)));
colnames(data_eot) <- column_names_eot
data_eot = as.data.frame(data_eot)
# Forward coded: 1, 2, 6, 10, 11, 13, 14, 15, 18
# Reverse coded: 3, 4, 5, 7, 8, 9, 12, 16, 17
#
# Final scores can range from 18 (low NFC) to 90 (high NFC)

data_eot$nfc_sum =  as.numeric(raw_eot_data$needForCog_1) + 
                    as.numeric(raw_eot_data$needForCog_2) + 
                    as.numeric(raw_eot_data$needForCog_6) + 
                    as.numeric(raw_eot_data$needForCog_10) + 
                    as.numeric(raw_eot_data$needForCog_11) + 
                    as.numeric(raw_eot_data$needForCog_13) + 
                    as.numeric(raw_eot_data$needForCog_14) + 
                    as.numeric(raw_eot_data$needForCog_15) + 
                    as.numeric(raw_eot_data$needForCog_18) + 
                    -as.numeric(raw_eot_data$needForCog_3) + 6 +
                    -as.numeric(raw_eot_data$needForCog_4) + 6 +
                    -as.numeric(raw_eot_data$needForCog_5) + 6 +
                    -as.numeric(raw_eot_data$needForCog_7) + 6 +
                    -as.numeric(raw_eot_data$needForCog_8) + 6 +
                    -as.numeric(raw_eot_data$needForCog_9) + 6 +
                    -as.numeric(raw_eot_data$needForCog_12) + 6 +
                    -as.numeric(raw_eot_data$needForCog_16) + 6 +
                    -as.numeric(raw_eot_data$needForCog_17) + 6;

data_eot$fraction_attn_check_correct =  (as.numeric(raw_eot_data$attentionCheck1) +
                                        as.numeric(raw_eot_data$attentionCheck2) + 
                                        as.numeric(raw_eot_data$attentionCheck3))/3;


data_eot$energy_level_beginning = as.numeric(raw_eot_data$startEnergy);
#1 = extremely tired 4 = nuetral 7 = extremely energized

data_eot$energy_level_end = as.numeric(raw_eot_data$currentEnergy);
#1 = extremely tired 4 = nuetral 7 = extremely energized

data_eot$performance_riskydecisionmaking = as.numeric(raw_eot_data$rdmPerformance);
#1 = extremely poor 4 = average 7 = extremely great

data_eot$performance_digitspan = as.numeric(raw_eot_data$digitPerformance);
#1 = extremely poor 4 = average 7 = extremely great

data_eot$age = as.numeric(raw_eot_data$Age);

data_eot$gender = as.numeric(raw_eot_data$Gender);
  #1 = male 2 = female

#HELP WITH ETHNICITY COLUMN
#data_eot$ethnicity = as.numeric(raw_eot_data$ethnicity);
#1 = Hispanic/Latinx 2 = Not Hispanic/Latinx 3 = Prefer Not to Say

data_eot$race = as.numeric(raw_eot_data$Race);
#1 = American Indian/Alaska Native 2 = Black/Aftican American 3 = East Asian 4 = Native Hawaiian/Paciifc Islander 
#5 = South Asian 6 = white 7 = Bi-multiracial (please specify) 8 = Other 9 = Prefer Not to Say

data_eot$political_orientation = as.numeric(raw_eot_data$political.o);
#1 = extremely conservative 9 = extremly liberal

data_eot$highest_degree_attained = as.numeric(raw_eot_data$Education.level.);
#1 = no schooling completed 2 = nursey school to 8th grade 3 = some high school, no dipolma 
#4 = high school graduate 5 = trade/technical/vociational traiing 6 = associates degree 
#7 = bacherlors degree 8 = masters degree 9 = professional degree 10 = doctors degree

data_eot$sona_ID = as.numeric(raw_eot_data$id);


# save out CSVs with the clean, compiled data!
setwd(processeddata_wd);

write.csv(data_dm, file=sprintf('cgt_processed_decisionmaking_data_%s.csv',format(Sys.Date(), format="%Y%m%d")),
          row.names = F);
write.csv(data_wm, file=sprintf('cgt_processed_workingmemory_data_%s.csv',format(Sys.Date(), format="%Y%m%d")),
          row.names = F);
# write.csv(data_eot, file=sprintf('cgt_processed_end_of_task_data_%s.csv',format(Sys.Date(), format="%Y%m%d")),
          # row.names = F);


# all done!

