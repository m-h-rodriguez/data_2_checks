import pandas as pd
import os

metro_requests = pd.read_csv(os.path.join(
    'DataSource', 'Louisville_Metro_KY_-_311_Service_Requests_2022.csv'), sep=",", low_memory=False)


# correcting column names
metro_requests.columns = ['Record_ID', 'Status', 'Record_Type', 'Opened_Date', 'Street', 'Dir',
                          'Street_Name', 'Type', 'Unit', 'Description', 'Related_Records',
                          'Created_By', 'Assigned_to_Department', 'Assigned_to_Staff',
                          'ObjectId']

# dropping rows where the status field is null/empty
metro_requests = metro_requests[metro_requests['Status'].notna()]

print(metro_requests)

valid_status = ['Closed', 'In Progress', 'Complete-Fixed', 'Assigned',
                'Enforcement', 'Received', 'Submitted', 'Work Order', 'Complete-Referred',
                'Completed', 'Closed-Referred', 'Open']

# removing rows that are not in a valid status type from array above
metro_requests = metro_requests[metro_requests['Status'].isin(valid_status)]

# replacing NaN with blank
metro_requests.fillna('', inplace=True)

print(metro_requests)
