#!/usr/bin/env python3

def print_table(site_url, table_class):
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd

    response = requests.get(site_url)

    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', attrs={'class': table_class})
    table_rows = table.find_all('tr')

    header = []
    for row in table.find_all('th'):
        header.append(row.text)

    df = pd.DataFrame(columns=header)

    # Create a for loop to fill mydata
    for j in table.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [i.text for i in row_data]
        length = len(df)
        df.loc[length] = row

    print(df)
    return


print_table('https://www.w3schools.com/html/html_tables.asp', 'ws-table-all')
