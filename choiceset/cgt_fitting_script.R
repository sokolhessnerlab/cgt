rm(list = ls()); # clear the workspace
setwd('/Users/sokolhessner/Documents/gitrepos/cgt/choiceset/');

# Code to load choiceset
choiceset = read.csv('CGT-choice-set.csv')

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
  div <- max(choiceset)^rho; # decorrelates rho & mu
  
  # calculate the probability of selecting the risky option
  p = 1/(1+exp(-mu/div*(utility_risky_option - utility_safe_option)));
  
  return(p)
}

choiceP = choice_probability(c(.8,20), choiceset)
simulatedchoices = as.integer(runif(n = length(choiceP)) < choiceP);

# Likelihood function
negLLprospect_cgt <- function(parameters,choiceset,choices) {
  # A negative log likelihood function for a prospect-theory estimation.
  # Assumes parameters are [rho, mu] as used in S-H 2009, 2013, 2015, etc.
  # Assumes choiceset has columns riskyoption1, riskyoption2, and safeoption
  # Assumes choices are binary/logical, with 1 = risky, 0 = safe.
  #
  # Peter Sokol-Hessner
  # July 2021
  
  eps = .Machine$double.eps;

  choiceP = choice_probability(parameters, choiceset);
  
  likelihood = choices * choiceP + (1 - choices) * 1-choiceP;
  likelihood[likelihood == 0] = eps;
  
  nll <- -sum(log(likelihood));
  return(nll)
}




negLLprospect_cgt(c(1.2, 20), choiceset, simulatedchoices)







##### CODE BELOW HERE IS NON-FUNCTIONAL #####


eps = .Machine$double.eps;
lower_bounds = c(eps, eps, eps); # L, R, M
upper_bounds = c(5,2,50); 

# Initial values
initial_values = c(3,1,20); # pick something within 
# "support" (btwn lower_bounds 
# and upper_bounds)

# Call optim()
output = optim(initial_values, pt_nll, 
               riskygain = data_subject1$riskygain,
               riskyloss = data_subject1$riskyloss,
               cert = data_subject1$cert,
               choice = data_subject1$choice,
               lower = lower_bounds,
               upper = upper_bounds,
               method = 'L-BFGS-B',
               hessian = T)

# Look at the output!
output$par
se = sqrt(diag(solve(output$hessian)));

#### Make Fitting More Robust: Iterations ####

# Create placeholders for parameters, errors, NLL (and anything else you want)
number_of_iterations = 200; # 100 or more
temp_parameters = array(dim = c(number_of_iterations,3));
temp_hessians = array(dim = c(number_of_iterations,3,3));
temp_NLLs = array(dim = c(number_of_iterations,1));

tic() # start the timer

for(iter in 1:number_of_iterations){
  # Randomly set initial values within supported values
  # using uniformly-distributed values. Many ways to do this!
  
  # initial_values = 
  #   runif(3)*(upper_bounds - lower_bounds) + lower_bounds;
  initial_values = runif(3, min = lower_bounds, max = upper_bounds)
  
  temp_output = optim(initial_values, pt_nll,
                      riskygain = data_subject1$riskygain,
                      riskyloss = data_subject1$riskyloss,
                      cert = data_subject1$cert,
                      choice = data_subject1$choice,
                      lower = lower_bounds,
                      upper = upper_bounds,
                      method = "L-BFGS-B",
                      hessian = T)
  
  # Store the output we need access to later
  temp_parameters[iter,] = temp_output$par; # parameter values
  temp_hessians[iter,,] = temp_output$hessian; # SEs
  temp_NLLs[iter,] = temp_output$value; # the NLLs
}

toc() # stop the timer; how long did it take? Use this to plan!

# How'd we do? Look at the NLLs to gauge quality of fit
unique(temp_NLLs) # they look the same but are not...

# Compare output; select the best one
s1_nll = min(temp_NLLs); # the best NLL for this person
s1_best_ind = which(temp_NLLs == s1_nll); # the index of that NLL

s1_parameters = temp_parameters[s1_best_ind,] # the parameters
s1_parameter_errors = sqrt(diag(solve(temp_hessians[s1_best_ind,,]))); # the SEs


