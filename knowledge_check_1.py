import pandas as pd
import json
import requests
from pandas import json_normalize
from pprint import pprint

# step 1:  pullin data from an API:
url = requests.get('https://services1.arcgis.com/79kfd2K6fskCAkyg/arcgis/rest/services/Louisville_Metro_KY_Inspection_Violations_of_Failed_Restaurants/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson')

print(url.status_code)

data = url.json()
print(data.keys())
print(type(data['features']))
print(type(data['features'][0]))
df = pd.json_normalize(url.json(), 'features')


# dropping unnecessary columns to view the data fields
df.drop(columns=['properties.ObjectId', 'properties.EstablishmentID',
        'properties.rpt_area_id', 'geometry', 'id', 'properties.InspTypeSpecificViolID', 'properties.InspectionID', 'type', 'id'], inplace=True)
#df.drop_duplicates(subset='properties.premise_name', inplace=True)

print(df.columns)

# step 2:  find and print two descriptive stats about the data

# provides the average score for resturants with food violations
resturants_avg = df.groupby('properties.premise_name')[
    'properties.score'].mean()
print(resturants_avg)

# prints off the unique list of resturants included in the dataset
names = list(df['properties.premise_name'].unique())
print(names)

# counts the number of occurrences for each resturant in the data by name
df_size = df.groupby(['properties.premise_name']).size()
print(df_size)


# step 3: Write a query in Pandas to select a particular set of your data. You can use a mask or with .query(), but we want you to pull out a subset based on any parameter


def type_violations(estType):
    filterdata = df['properties.EstTypeDesc'].isin([estType])
    filtertype = df[filterdata]
    groupFilter = filtertype.groupby(
        filtertype['properties.premise_name']).agg(['count'])

    return print(groupFilter)


type_violations('SCHOOL CAFETERIA OR FOOD SERVICE')

# step 4:  select and print the second and third columns
print(df[df.columns[1:3]])

# step 5: print the first 4 rows of dataframe

print(df.iloc[:4])
