import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import factorial as fact

def comb(n,r):
  return fact(n)/(fact(r)*fact(n-r))

#%% Setup of exp
# For coin tossing case:
base = 2 # {H,T} for coin
ex=int(input("How many times we repeat experiement: "))

iter = []
for i in range(ex):
  ipt = int(input("How many coin to toss {} time : ".format(i+1)))
  iter.append(ipt)

#%% 
plt.figure(1,figsize=(3*ex+1,ex+2))
# Calculation
for z in range(ex):
  macrocount = iter[z]+1 # no. of macrostate
  poss = base**iter[z] # no. of possibility
  
  ## X-> Random variable = no. of heads
  X = np.linspace(0,iter[z],macrocount)
  microcount = np.zeros(macrocount)
  prob = np.zeros(macrocount)
  
  for r in range(macrocount):
    microcount[r] = comb(iter[z],r)
    prob[r] = microcount[r]/poss
  
#%% Displaying Table
  print(f'For {iter[z]} coins:')
  column = ['X','Microcount:','Probability:']
  data = list(zip(X, microcount, prob))
  df = pd.DataFrame(data,columns=column)

  '''   OR
  data = {
      'X': X,
      'Microcount': microcount,
      'Probability': prob   
    }
    df = pd.DataFrame(data)
  '''
  print(df)
#%% Plotting Graphs
  plt.subplot(ex,1,z+1)
  plt.plot(X,prob,'--or')
  plt.xticks(X)  # Set x-axis ticks to only the values in X
  plt.xlabel('No. of Heads:',fontsize=12)
  plt.ylabel('Probability:',fontsize=10)
  plt.ylim(0,max(prob)+0.1)
  plt.grid(True)

# plt.title("Microcount probability in coins",fontsize=14,fontweight=500)
plt.subplots_adjust(top=1)
plt.suptitle('Coin Tossing Experiment Results', fontsize=14)
plt.tight_layout(pad=0.5)
plt.show()
