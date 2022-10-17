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

