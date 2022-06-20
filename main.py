#!python3

import requests
from zipfile import ZipFile
import os
import csv
from pprint import pprint

if __name__ == '__main__':
    #Downloading ZIP file
    path = 'https://assets.datacamp.com/production/repositories/5899/datasets/19d6cf619d6a771314f0eb489262a31f89c424c2/ppr-all.zip'
    #Get the zip file
    response = requests.get(path)
    #print response status code hope it 200
    print(f'response status code : ',response.status_code)
    #Save to local path
    current_directory=os.getcwd()
    local_path=current_directory+'/PPR-ALL.zip'
    print(f'this is local path : ',local_path)
    
    with open (local_path, mode='wb') as file :
        file.write(response.content)
    #Exploring Zip
    with ZipFile(local_path,mode='r')as file :
        file_names=file.namelist()
        print(file_names)
        csv_file_path=file.extract(file_names[0])
        print(csv_file_path)
    #Reading CSV file
    with open(local_path,mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        row = next(reader)
        print(type(row))
        pprint(row)
    