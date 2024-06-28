import requests
from Registro import registro, filtro, busqueda, get_user

def get_data():

    # Esta función crea una lista compuesta de los datos correspondientes a los equipos, los estadios y los partidos de Euro 2024.
    
    urls = ["https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json",
            "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json",
            "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json"]
    
    data_list = []

    for url in urls:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            data_list.append(data)
        
    return data_list

def main():
    registro(get_data())
    while True:
        menu = input('Seleccione lo que quiere ver:\n1) Partidos\n2) Comprar entrada\n')
        if menu == '1':
            match_option = input('Escoge el por el cual quiere buscar:\n1) Por país\n2) Por estadio\n3) Por fecha\n')
            filtro(busqueda(match_option))
        elif menu == '2':
            print(get_user().mostrar())
            
            break


main()