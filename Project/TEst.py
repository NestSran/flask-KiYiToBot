import requests
import json

def Covid_Thai():


    data = requests.get('https://covid19.th-stat.com/api/open/today')
    
    print(data.content.decode('utf-8'))
    
    # Bit To String
    data_str = data.content.decode('utf-8')
    data_covid =  data_str.split(',')
    '''
    data_json = json.loads(data_str)
    
    '''
    return data_covid

    x= "รายงานสถานการณ์โควิด-19,ประเทศไทย {}".format(Covid_Thai)
    print(x)