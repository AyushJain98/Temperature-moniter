import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_temperature():
       return round(random.uniform(20,50),2)
reading= []
for i in range(20):
   reading.append({'Reading_no' : i+1,'Temperature' : get_temperature()})


df = pd.DataFrame(reading)
df['Status'] = df['Temperature'].apply(lambda x : 'Overheating'if x>40 else 'Safe')
df

colors = ['red' if s == 'Overheating' else 'green' for s in df['Status']]
plt.plot(df['Reading_no'],df['Temperature'],color = 'gray', linewidth =1)
plt.scatter(df['Reading_no'],df['Temperature'],c = colors,zorder =5)
plt.axhline(y = 40,color ='red',linestyle = '--',label ='Danger limit 40C')
plt.legend()
df.to_csv('Temperature_log.csv',index =False)
plt.savefig('Temperature_log.png')
plt.show()
print(df.to_markdown(index=False))
