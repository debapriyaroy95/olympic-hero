# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(columns={'Total' : 'Total_Medals'},inplace=True)
data.head(10)


# --------------
#Code starts here

data['Better_Event']=np.where( data.Total_Summer==data.Total_Winter,"Both", 
         np.where(data.Total_Summer>data.Total_Winter,"Summer","Winter"))

better_event=data['Better_Event'].value_counts(ascending=False).index[0]


# --------------
top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

top_countries.drop(top_countries[top_countries['Country_Name'] == 'Totals'].index,inplace=True)

def top_ten (top_countries,a):  
  country_list =[]
  df = top_countries.nlargest(10, a)
  country_list=list(df.Country_Name)
  return country_list
  
top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')

common =[x for x in top_10_summer if x in top_10_winter and x in top_10]

print(common)



# --------------
#Code starts here

summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

plt.bar(summer_df.Country_Name,summer_df.Total_Medals,color = 'green',edgecolor = 'darkgreen')
plt.grid()
plt.xticks(summer_df.Country_Name,rotation ='vertical')
plt.xlabel('Countries')
plt.ylabel('Medals won')
plt.title('Top 10 countries in Summer Olympics')
plt.show()

plt.bar(winter_df.Country_Name,winter_df.Total_Medals,color = 'blue',edgecolor = 'darkblue')
plt.grid()
plt.xticks(winter_df.Country_Name,rotation ='vertical')
plt.xlabel('Countries')
plt.ylabel('Medals won')
plt.title('Top 10 countries in Winter Olympics')
plt.show()

plt.bar(top_df.Country_Name,top_df.Total_Medals,color = 'red',edgecolor = 'pink')
plt.grid()
plt.xticks(top_df.Country_Name,rotation ='vertical')
plt.xlabel('Countries')
plt.ylabel('Medals won')
plt.title('Top 10 countries in Olympics')
plt.show()



# --------------
#Code starts here
summer_df ['Golden_Ratio']= summer_df['Gold_Summer']/summer_df['Total_Summer']
winter_df ['Golden_Ratio']= winter_df['Gold_Winter']/winter_df['Total_Winter']
top_df ['Golden_Ratio']= top_df['Gold_Total']/top_df['Total_Medals']




summer_country_gold = list(summer_df[summer_df['Golden_Ratio']==summer_df.Golden_Ratio.max()]['Country_Name'])[0]
summer_max_ratio = list(summer_df[summer_df['Golden_Ratio']==summer_df.Golden_Ratio.max()]['Golden_Ratio'])[0]

winter_country_gold = list(winter_df[winter_df['Golden_Ratio']==winter_df.Golden_Ratio.max()]['Country_Name'])[0]
winter_max_ratio = list(winter_df[winter_df['Golden_Ratio']==winter_df.Golden_Ratio.max()]['Golden_Ratio'])[0]

top_country_gold = list(top_df[top_df['Golden_Ratio']==top_df.Golden_Ratio.max()]['Country_Name'])[0]
top_max_ratio = list(top_df[top_df['Golden_Ratio']==top_df.Golden_Ratio.max()]['Golden_Ratio'])[0]


# --------------
#Code starts here
data_1 = data[:-1]

data_1['Total_Points'] = (data_1.Gold_Total*3)+(data_1.Silver_Total*2)+(data_1.Bronze_Total*1)

most_points = data_1.loc[data_1.Total_Points.idxmax(),'Total_Points']
best_country = data_1.loc[data_1.Total_Points.idxmax(),'Country_Name']



# --------------
#Code starts here

best = data[data['Country_Name'] == best_country]

best = best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot(kind = 'bar',stacked=True)
plt.xticks(rotation =45)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.title('Tally of Medals of the best country in Olympics')
plt.show()



