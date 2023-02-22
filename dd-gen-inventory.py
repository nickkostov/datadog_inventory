#!/usr/bin/env python3
import pandas as pd
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.list_monitors()

    data = [(monitor['name'], monitor['priority'], f"https://toyotaeurope.datadoghq.eu/monitors/{monitor['id']}", monitor['tags'], monitor['creator']) for monitor in response]
    headers = ['Name', 'Priority', 'Link', 'Tags', 'Creator']

    # Create a DataFrame from the data and headers
    df = pd.DataFrame(data, columns=headers)

    # Write the DataFrame to an Excel file
    with pd.ExcelWriter('monitors.xlsx') as writer:
        df.to_excel(writer, index=False)