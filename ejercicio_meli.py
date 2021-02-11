import json
import requests
import matplotlib.pyplot as plt
import matplotlib.axes
import numpy as np

def fetch():

    url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20MDQ%20&limit=50'  
    response = requests.get(url)
    data = response.json()
    
    filter_data = [data['results']]
    
    dataset = [{'price':x['price'], 'condition':x['condition']} for x in filter_data[0] if x['currency_id'] == 'ARS']
    
    return dataset
   

def transform(dataset, minimo, maximo):

    precio_min = len([x['price'] for x in dataset if x['price'] < minimo])
    precio_max = len([x['price'] for x in dataset if x['price'] > maximo])
    precios_medios = len([x['price'] for x in dataset if x['price'] > minimo and x['price'] < maximo])

    return [precio_min, precio_max, precios_medios]

    
def report(data, minimo, maximo):
    
    fig, ax = plt.subplots()
    fig.suptitle('ALQUILERES POR RANGO DE PRECIO ESTABLECIDO')

    
    labels = [f'Menores a ${minimo} \nCantidad: {data[0]}',
              f'Mayores a ${maximo} \nCantidad: {data[1]}',
              f'Entre ${minimo,maximo} \nCantidad: {data[2]}']
    
    ax.pie(data, labels = labels, autopct='%1.1f%%', shadow=True, startangle=180)
    ax.axis('equal') 

    plt.show()



if __name__ == '__main__':
    
    minimo = 4000
    maximo = 8000
    dataset = fetch()
    data = transform(dataset, minimo, maximo)
    report(data, minimo, maximo)