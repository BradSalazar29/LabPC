import requests
import json
from datetime import datetime,date,time

def consultar_clima():
    ciudad = input('ingrese la ciudad que desea buscar')
    APICODE = "f274138c7483cb5369afdba679f96a47"
    url =f'https://api.openweathermap.org/data/2.5/weather?q={ciudad}&units=metric&appid={APICODE}'
    res=requests.get(url)
    data=json.loads(res.content)
    print(data)
    temp = data['main']['temp']
    fecha = datetime.utcfromtimestamp(int(data["dt"])).strftime("%d - %m - %Y %H:%M")
    print('fecha '+str(fecha)+' '+'temperatura '+str(temp))

def clima_ultimos_dias():
    fechas = int(input('cuantas fechas va a constular (solo se puedan hasta 5 dias)'))
    lista_fechas =[]
    for i in range(fechas):
        dia=int(input('ingrse el dia '))
        ano=int(input('ingrse el ano '))
        mes=int(input('ingrse el mes '))
        fecha=datetime(ano,mes,dia,9,0,0)
        unix_time=fecha.timestamp()
        APICODE = "f274138c7483cb5369afdba679f96a47"
        url= f'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={25.6667}&lon={-100.3167}&units=metric&dt={int(unix_time)}&appid={APICODE}'
        res = requests.get(url)
        data = json.loads(res.content)
        temp = data['current']
        temp2 =temp['temp']
        lista_fechas.append(f'{fecha} Temperatura: {temp2} grados')


    print(lista_fechas)



clima_ultimos_dias()