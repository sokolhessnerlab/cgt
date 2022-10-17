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

#### Data Quality Checks & Exclusions ####

# Exclude on the basis of DM task performance
# (using... check trials, RTs, choices)

# Exclude on the basis of WM task performance
# (using... )

# Exclude on any other basis? 

# >>>Create clean data frames<<<


#### Basic Data Analysis ####
# (Separately for DM & WM data)

# Descriptives & simple averages of task performance


#### Connecting Decision-Making & Working Memory ####

