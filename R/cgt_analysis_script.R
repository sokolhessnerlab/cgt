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


# Prepare a place for the compiled data to live
# - decision-making data
# - WM capacity data


# Loop
for(s in 1:number_of_subjects){
  tmpdata = read.csv(fn[s]);
  
  # Pull out the data we need
  
  # Add this person's data to the total data.
}

# save out CSVs with the clean, compiled data!