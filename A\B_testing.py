import codecademylib3
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
# Inspect first few rows of ad_clicks
print(ad_clicks.head(3))
# Find the source of most views
print(ad_clicks.groupby('utm_source')\
     .user_id.count()\
     .reset_index())
# Create new column to show if the ad was actually clicked on
ad_clicks['is_click'] = ~ad_clicks\
   .ad_click_timestamp.isnull()
# Find number of people that clicked on ads for each source
clicks_by_source = ad_clicks\
   .groupby(['utm_source', 'is_click'])\
   .user_id.count()\
   .reset_index()
print(clicks_by_source)
# Create pivot table with columns = is_click, index = utm_source and values = user_id
clicks_pivot = clicks_by_source\
   .pivot(columns = 'is_click', 
          index = 'utm_source', 
          values = 'user_id')\
   .reset_index()
  
# Create a column showing percentage of clicks for each source
clicks_pivot['percent_clicked'] = \
   clicks_pivot[True] / \
   (clicks_pivot[True] + 
    clicks_pivot[False])
print(clicks_pivot)
# Number of users shown ad A or ad B
print(ad_clicks.groupby('experimental_group')\
    .user_id.count()\
    .reset_index())
# Number of users clicked on ad A or ad B
print(ad_clicks.groupby(['experimental_group', 'is_click'])\
     .user_id.count()\
     .reset_index()\
     .pivot(columns = 'is_click',
            index = 'experimental_group',
            values = 'user_id')\
     .reset_index()  )     
# Create dataframes for group A and B clicks

# Group A
a_clicks = ad_clicks[
   ad_clicks.experimental_group
   == 'A']
print(a_clicks)
# Percent of user clicks by day group A
a_clicks_pivot = a_clicks.groupby(['is_click', 'day'])\
     .user_id\
     .count()\
     .reset_index()\
     .pivot(index = 'day',
            columns = 'is_click',
            values = 'user_id')\
     .reset_index()
a_clicks_pivot['percent_clicked'] = \
     a_clicks_pivot[True] / \
     (a_clicks_pivot[True] + a_clicks_pivot[False])
print(a_clicks_pivot)
# Group B
b_clicks = ad_clicks[
   ad_clicks.experimental_group
   == 'B']   
print(b_clicks)
# Percent of user clicks by day group B
b_clicks_pivot = b_clicks.groupby(['is_click', 'day'])\
     .user_id\
     .count()\
     .reset_index()\
     .pivot(index = 'day',
            columns = 'is_click',
            values = 'user_id')\
     .reset_index()
b_clicks_pivot['percent_clicked'] = \
     b_clicks_pivot[True] / \
     (b_clicks_pivot[True] + b_clicks_pivot[False])
print(b_clicks_pivot)
# Display ad_clicks dataframe
print(ad_clicks)
