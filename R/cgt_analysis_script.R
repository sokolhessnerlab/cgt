# CGT Analysis Script
#
# Script to analyze data collected online during Summer 2022 in the CGT
# (Control & Gambling Task) study.

# identify the working directory paths
rawdata_wd = '/Volumes/shlab/Projects/CGT/rawdata/';
main_wd = '/Volumes/shlab/Projects/CGT/';

# set the working directory
setwd(rawdata_wd);

# List all the data files
fn = dir(pattern = glob2rx('CGTgamblingSpanTasks_2022-09*.csv'),full.names = T);

# Identify the number of participants from the file listing
number_of_subjects = length(fn);

num_static_trials = 50;
num_dynamic_trials = 120;
number_of_dm_trials_per_person = num_static_trials + num_dynamic_trials; # static = 50, dynamic = 120

column_names_dm = c(
  'trialnumber',
  'subjectnumber',
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



# Prepare a place for the compiled data to live
# - WM capacity data

# data_wm; includes FS & BS

column_names_wm = c(
  'digitsForTrial', #both FS & BS digits
  'textbox.text', #FS response
  'textboxBS.text', #BS response
  'trialNumber', #both trial number
  'digitLoop.thisRepN', #FS number of digits
  'digitLoopBS.thisRepN', #BS number of digits
  'correct' #both FS & BS
);

data_wm = array(data = NA, dim = c(0, length(column_names_wm)));
colnames(data_wm) <- column_names_wm

# Loop
for(s in 1:number_of_subjects){
  tmpdata = read.csv(fn[s]);
  dm_data_to_add = array(data = NA, dim = c(number_of_dm_trials_per_person,length(column_names_dm)));

  dm_index_static = is.finite(tmpdata$staticRDM.thisTrialN);
  dm_index_dynamic = is.finite(tmpdata$dynamicRDM.thisTrialN);

  tmp_trialnum = c(tmpdata$staticRDM.thisTrialN[dm_index_static] + 1,
                   tmpdata$dynamicRDM.thisTrialN[dm_index_dynamic] + num_static_trials + 1);

  dm_data_to_add[,1] = tmp_trialnum; # trial number
  dm_data_to_add[,2] = s; # subject number

  tmp_riskyopt1 = c(tmpdata$riskyoption1[dm_index_static],
                    tmpdata$riskyoption1[dm_index_dynamic]);
  tmp_riskyopt2 = c(tmpdata$riskyoption2[dm_index_static],
                    tmpdata$riskyoption2[dm_index_dynamic]);
  tmp_safe = c(tmpdata$safeoption[dm_index_static],
               tmpdata$safeoption[dm_index_dynamic]);

  dm_data_to_add[,3:5] = cbind(tmp_riskyopt1,tmp_riskyopt2,tmp_safe) # dollar amounts

  dm_data_to_add[,6] = c(tmpdata$choices[dm_index_static],
                         tmpdata$choices[dm_index_dynamic]); # choices

  dm_data_to_add[,7] = c(tmpdata$realChoice.rt[dm_index_static],
                         tmpdata$realChoice.rt[dm_index_dynamic]); # RTs

  dm_data_to_add[,8] = c(tmpdata$outcomes[dm_index_static],
                         tmpdata$outcomes[dm_index_dynamic]); # outcomes

  dm_data_to_add[,9] = c(tmpdata$ischecktrial[dm_index_static],
                         array(data = 0, dim = c(1,num_dynamic_trials))); # is check trial

  dm_data_to_add[,10] = c(array(data = 0, dim = c(1,num_static_trials)),
                         array(data = 1, dim = c(1,num_dynamic_trials))); # static 0, dynamic 1

  dm_data_to_add[,11] = c(array(data = 0, dim = c(1,num_static_trials)),
                          tmpdata$easy0difficult1[dm_index_dynamic]*-2 + 1); # easy +1, difficult -1

  dm_data_to_add[,12] = c(array(data = NA, dim = c(1,num_static_trials)),
                          tmpdata$choiceP[dm_index_dynamic]); # choice probability on easy/diff dynamic trials

  dm_data_to_add[,13] = tmpdata$bestRho[is.finite(tmpdata$bestRho)];
  dm_data_to_add[,14] = tmpdata$bestMu[is.finite(tmpdata$bestMu)];


  # Pull out the data we need

  # Add this person's data to the total data.

  data_dm = rbind(data_dm,dm_data_to_add);
}

data_dm = as.data.frame(data_dm) # make it a data frame so it plays nice

# save out CSVs with the clean, compiled data!
