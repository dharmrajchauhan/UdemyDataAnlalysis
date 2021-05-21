import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import difflib
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')

'''---------------------------------------------------------------Importing Data------------------------------------------------------------------------------------'''
path = r'data/7. Udemy Courses.csv'
df = pd.read_csv(path)
df.info()
df.describe(include='all') #its all about data in which 

# 1932 courses are for 'ALL LEVEL' of students
# 268323 is max subscribers
# there are 1200 course of webdevelopment #highest
# most of courses are paid
# etc..............

'''---------------------------------------------------------------Data Cleaning----------------------------------------------------------------------------------'''
dff = df.drop(columns=['course_id','published_timestamp'])
dff.head(5)
dff = dff.drop_duplicates(['course_title'],keep='last')
dff.shape
print(f"Total len of columns in givern dataset:- {df.shape[0]}\nAfter removing duplicate,len of columns:- {dff.shape[0]}\nTotal no of Duplicate columns:-\t{df.shape[0]-dff.shape[0]}")
s0 = dff.sample(1000)
s0.head(5)
'''---------------------------------------------------------------Data visulization & Answering Questions----------------------------------------------------------------------------------'''

# (1) Show all the courses which are free?
s0[s0.is_paid == False]

# analysis_data = s0.groupby(s0.is_paid == False)
# analysis_data.describe()
tft = pd.crosstab(index=s0["is_paid"],columns="Total")
tft

'''------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# (2) Which subject has the maximum number of courses?

s0.subject.value_counts()
analysis_data = s0.groupby('subject')
analysis_data.describe()

fig = px.bar(s0,
             x='subject',
             y='num_subscribers',
             color='subject',
             orientation='v',
             barmode="overlay",
             title="Long-Form Input")
fig.show()

'''------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# (3) List out all the courses that are related to 'Java’

searchfor = ['java', 'Java','Jquery','JQuery','jquery']
s0[s0.course_title.str.contains('|'.join(searchfor))]

'''------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# (4) Which are top selling courses?

# lets quick look of the dataset 
subject = s0['subject']
level = s0['level']
paid = s0['is_paid']
subs = s0['num_subscribers']
fig =px.sunburst(s0,
                 path=[subject,level,paid],
                values = subs,
                title = "Complete overview babe")
fig.update_layout(title_font_size=42,
                 title_font_family = 'Arial')
fig.update_layout(margin = dict(t=100, l=0, r=400, b=0),
                  title_font_size=42,
                  title_font_family = 'Arial')
fig.show()

'''------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# #### see which specific term more affect most selling courses

heat_mapp = s0.copy()
heat_mapp['price'] = heat_mapp['price'].str.replace('Free|TRUE','0')
heat_mapp['price'] = heat_mapp['price'].astype('int')
heat_mapp['is_paid'] = heat_mapp['is_paid'].astype('int')

heat_mapp['subject'] = s0['subject'].replace(['Musical Instruments', 'Web Development', 'Business Finance', 'Graphic Design'],[0,1,2,3])
heat_mapp['level'] = s0['level'].replace(['All Levels', 'Beginner Level', 'Intermediate Level', 'Expert Level'],[0,1,2,3])

heat_mapp = heat_mapp.drop(columns=['course_title','content_duration'])
drop_rank = heat_mapp.drop("num_subscribers", axis = 1)

corr_matrix_happy = drop_rank.corr()
trace_corr_price = go.Heatmap(z=np.array(corr_matrix_happy),
                             x = corr_matrix_happy.columns,
                             y= corr_matrix_happy.columns)
data_effect = [trace_corr_price]
iplot(data_effect)

plt.figure(figsize=(20,10))
plt.title("Does Price matter!!")
# s0['price'] = s0['price'].str.replace('Free|TRUE','0')
# s0['price'] = s0['price'].astype('int')
sns.lineplot(data=s0,x='price',y='num_subscribers',hue='subject')
plt.show()

plt.figure(figsize=(20,10))
df1 = s0.copy()
df1['published_timestamp'] = pd.to_datetime(df['published_timestamp'])
df1["year"] = df1['published_timestamp'].dt.year
plt.title("Does Price matter!!")
sns.lineplot(data=df1,y='num_subscribers',x='year',hue='subject')
plt.show()

train = df1.sort_values(by='num_subscribers', ascending=False)[:30]
fig = px.bar(df1,
             y = train['course_title'],
             x = train['num_subscribers'],
             color = train['subject'],
             orientation='h',
             barmode="overlay",
             title="Top 30 courses by num_subscribers")
fig.show()

train = df1.sort_values(by='num_reviews', ascending=False)[:30]
fig = px.bar(df,
             y = train['course_title'],
             x = train['num_reviews'],
             color = train['subject'],
             orientation='h',
             barmode="overlay",
             title="Top 30 courses by review")
fig.show()


