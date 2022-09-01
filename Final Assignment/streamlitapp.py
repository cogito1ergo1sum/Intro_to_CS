import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


@st.cache
def load_df():
      df = pd.read_csv("/Users/Downloads/archive/crime.csv", encoding='unicode_escape')
      df = df.rename(columns={
          'Lat': 'lat',
          'Long': 'lon'
      })
      df = df.dropna(subset=['lat', 'lon'])

      np.random.seed(40001)

      coords_mask = df['lat'] > 40
      return df[coords_mask].sample(n=20000)

## above was provided script. Question 1: give option to choose hour and map crime locations at that time

df = load_df()

#slider to select the hour to analyze
st.subheader('Crime Location on Map - Choose the hour')
Hour_filter = st.slider('', 0, 23, 12)
Crime_Filter = df[df['HOUR'] == Hour_filter]

# Map to show the physical locations of Crime for the selected hour.
midpoint = (np.average(Crime_Filter["lat"]), np.average(Crime_Filter["lon"]))
st.map(Crime_Filter)


#Question 2:
# find top 10 offenses, convert to list and add as selectbox options
top_ten = df["OFFENSE_CODE_GROUP"].value_counts().sort_values(ascending=False).head(10).reset_index()
top_ten_list = top_ten['index'].tolist()
st.subheader('Choose an offense')

option = st.selectbox('', top_ten_list)
#assign based on user's choice

mask_crime = (df['OFFENSE_CODE_GROUP'] == option)
# calc and plot using matplotlib as that's what was shown in class (can call st.pyplot() at the end)
week_incidents_of_mask = df[mask_crime].groupby(['DAY_OF_WEEK'])['OFFENSE_CODE_GROUP'].count().reset_index()

fig = plt.figure(figsize=(10, 6))
plt.xticks(rotation=90)
plt.bar(x=week_incidents_of_mask['DAY_OF_WEEK'].values, height=week_incidents_of_mask['OFFENSE_CODE_GROUP'].values, color=['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink'])
plt.xlabel('Day of the Week')
plt.ylabel('Count')
st.pyplot()


# question 3:
## choose a police district (drop nan values which are cases reported without a police district
#sorted alphabetically (not alphanumerically) for slightly easier search to user
dframe = df[df['DISTRICT'].notna()]
district = dframe.DISTRICT.unique()
results = np.sort(district)
st.subheader('Choose a police district')
choice = st.selectbox('', results)

## make a new df that keeps only the serious crimes [Larceny, Robbery, Drug Violation, Auto Theft] as the question specified
new_df = df[(df['OFFENSE_CODE_GROUP'] == 'Larceny') | (df['OFFENSE_CODE_GROUP'] == 'Robbery') | (df['OFFENSE_CODE_GROUP'] == 'Drug Violation') | (df['OFFENSE_CODE_GROUP'] == 'Auto Theft')]
new_df.reset_index(inplace=True)

#make 2 further cuts to dataframes for year and district selected by user
new_df2016 = new_df[(new_df['DISTRICT'] == choice) & (new_df['YEAR'] == 2016)]
new_df2017 = new_df[(new_df['DISTRICT'] == choice) & (new_df['YEAR'] == 2017)]

#make 2 dataframes grouped by months for the edited df. count all serious offenses/month and divide by 4 as per example in instructions


data_2016 = new_df2016.groupby(['MONTH'])["OFFENSE_CODE_GROUP"].count().div(4).reset_index()
data_2017 = new_df2017.groupby(['MONTH'])["OFFENSE_CODE_GROUP"].count().div(4).reset_index()

#now that we have our 2 data for 2016/17, we need to plot per instructions. Again, I used matplot and then called with st.pyplot as shown in class
figure = plt.figure(figsize=(7, 3))
figure.tight_layout()
plt.subplot(1, 2, 1)
plt.bar(x=data_2016['MONTH'].values, height=data_2016['OFFENSE_CODE_GROUP'].values, color=['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink'])
plt.xlabel('Month in 2016')
plt.xticks(range(1, 13))
plt.ylabel('Mean Accidents of Serious Crimes per Month in 2016')

plt.subplot(1, 2, 2)
plt.bar(x=data_2017['MONTH'].values, height=data_2017['OFFENSE_CODE_GROUP'].values, color=['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink'])
plt.xlabel('Month in 2017')
plt.xticks(range(1, 13))
plt.ylabel('Mean Accidents of Serious Crimes per Month in 2017')
st.pyplot(figure)



