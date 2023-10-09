from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import csv
import pandas as pd
import requests


def sort_data(table):
    data = []

    for row in table:
        cols = row.find_all('td width = "151"')
        if len(cols) == 0:
            cols = row.find_all('td')

        cols = [ele.text.strip() for ele in cols]

        data.append([ele for ele in cols if ele])

    del data[43:]
    global trimmed_data_list
    trimmed_data_list = [inner_list[:-2] for inner_list in data]

    for inner_list in trimmed_data_list:
        global initial_list
        initial_list = inner_list

    global headers
    headers = trimmed_data_list[0]
    global data_rows
    data_rows = trimmed_data_list[1:]

    global result_dict
    result_dict = {row[0]: {headers[i]: row[i] for i in range(1, len(headers))} for row in data_rows}
    print(result_dict)


def write_to_csv(result_dict):
    with open('tabel.csv', mode='w', newline='', errors='ignore') as csv_file:
        # Create a CSV writer
        csv_writer = csv.writer(csv_file)
        
        # Write the headers based on the keys of the first dictionary in the values
        headers = trimmed_data_list[0]
        csv_writer.writerow(headers)
        
        # Write data from the dictionary to the CSV file
        for key, values in result_dict.items():
            row = [key] + list(values.values())
            csv_writer.writerow(row)


if __name__ == '__main__':
    items = [
        "https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-1-martie-ora-13-00-2/"
    ]

    for item in items:
        driver = webdriver.Chrome()
        driver.get(item)
        soup = BeautifulSoup(driver.page_source, features='html.parser')
        table = soup.find_all('tr')
        sort_data(table)
        write_to_csv(result_dict)