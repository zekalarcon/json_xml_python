import json
import requests
import matplotlib.pyplot as plt
import matplotlib.axes
import numpy as np
import re
from itertools import groupby

def fetch(page_number, location_id):

    url = 'https://jsonmock.hackerrank.com/api/transactions/search?txnType=debit&page={}'.format(page_number)
    response = requests.get(url)
    data = response.json()

    filter_data = [data['data']]

    dataset = [[x['userId'], x['amount']] for x in filter_data[0] if x['location']['id'] == location_id ]
    
    return dataset


def transform(dataset):
    
    lista_str =[[x[0],float(re.sub(r'[^\d\-.]', '', x[1]))] for x in dataset]
   
    f = lambda x: x[:1]
   
    lista_filtrada = [[*x, *map(sum, zip(*(i[1:] for i in y)))]for x, y in groupby(sorted(lista_str, key=f), f)]
    
    return lista_filtrada


def report(data):   

    # Bar Plot

    x = [x[0] for x in data]
    y = [x[1] for x in data]

    fig, ax = plt.subplots()
    fig.suptitle('Filtered Debits by location')
    
    pos_x = np.linspace(1,len(x), len(x))
    
    colors = ['red', 'orange', 'green', 'blue', 'mediumturquoise', 'gold']
    ax.bar(pos_x, y, color = [color for color in colors])
    ax.grid(c = 'silver', ls = 'dotted')
    ax.set_facecolor('aliceblue')
    ax.set_ylabel('Debits $')
    ax.set_xlabel('UserId')
    ax.set_xticks(pos_x)
    ax.set_xticklabels(x)
    
    plt.show()

    
if __name__ == "__main__":
    page_number = 7
    location_id = 7
    dataset = fetch(page_number, location_id)
    data = transform(dataset)
    report(data)