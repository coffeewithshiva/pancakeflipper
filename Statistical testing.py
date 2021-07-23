
# To check if pancake flippers: Arielle and Boris have any signicantly differences using t-test
#Null hypothesis: Arielle and Boris are both equally competent pancake flippers
#Alternate hypothesis: Both are not equal in terms of pancake flipping performance 

from math import sqrt
from numpy import mean
from scipy.stats import sem
from scipy.stats import t
import pandas as pd
 
# function for calculating the t-test for two independent samples
def independent_ttest(data1, data2, alpha):
	# calculate means
	mean1, mean2 = mean(data1), mean(data2)
	# calculate standard errors
	se1, se2 = sem(data1), sem(data2)
	sed = sqrt(se1**2.0 + se2**2.0)
	# calculate the t statistic
	t_stat = (mean1 - mean2) / sed
	# degrees of freedom
	df = len(data1) + len(data2) - 2
	# calculate the critical value
	cv = t.ppf(1.0 - alpha, df)
	# calculate the p-value
	p = (1.0 - t.cdf(abs(t_stat), df)) * 2.0
	return t_stat, df, cv, p
 
#download the csv data
dataset = pd.read_csv('C:\\Users\\siva.palanisamy\\Downloads\\dataset.csv')

#split the dataset into two: Arielle (data1) and Boris (data2)
data1 = dataset['score'][0:50]
data2 = dataset['score'][50:100]

# calculate t-test
alpha = 0.05
t_stat, df, cv, p = independent_ttest(data1, data2, alpha)
print('t=%.3f, df=%d, cv=%.3f, p=%.3f' % (t_stat, df, cv, p))

# interpret via critical value
if abs(t_stat) <= cv:
	print('Accept null hypothesis that both pancake flippers are equal.')
else:
	print('Reject the null hypothesis that both pancake flippers are equal.')
    
# interpret via p-value
if p > alpha:
	print('Accept null hypothesis that both pancake flippers are equal.')
else:
	print('Reject the null hypothesis that both pancake flippers are equal.')