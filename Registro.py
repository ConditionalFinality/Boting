from Equipo import Equipo
from Estadio import Estadio
from Partido import Partido
from Cliente import Cliente
from Restaurante import Restaurante
from Producto import Producto

team_list = []
stadium_list = []
match_list = []
user_list = []

def registro(db):

    #Esta funcion tranforma los diccionarios obtenidos por medio de la funcion get_data() a listas con objetos de las tres clases establecidas.

    for type in db:
        for instance in type:

            if type == db[0]:
                team_id = instance['id']
                pais = instance['name']
                codigo = instance['code']
                grupo = instance['group']
                team_instance = Equipo(team_id, pais, codigo, grupo)
                team_list.append(team_instance)
                
            elif type == db[1]:
                stadium_id = instance['id']
                nombre = instance['name']
                ubicacion = instance['city']
                capacidad = instance['capacity']
                for restaurant in instance['restaurants']:
                    restaurantes = []
                    name = restaurant['name']
                    for product in restaurant['products']:
                        products = []
                        name = product['name']
                        quantity = product['quantity']
                        price = product['price']
                        stock = product['stock']
                        adicional = product['adicional']
                        product_instance = Producto(name, quantity, price, stock, adicional)
                        products.append(product_instance)
                    restaurant_instance = Restaurante(name, products)
                    restaurantes.append(restaurant_instance)
                stadium_instance = Estadio(stadium_id, nombre, ubicacion, capacidad, restaurantes)
                stadium_list.append(stadium_instance)

            elif type == db[2]:

                match_id = instance['id']

                for i in team_list:
                    if i.team_id == instance['home'].get('id'):
                        local = i
                        break

                for j in team_list:
                    if j.team_id == instance['away'].get('id'):
                        visitante = j
                        break

                fecha = instance['date']

                for k in stadium_list:
                    if k.stadium_id == instance['stadium_id']:
                        estadio = k
                        break

                match_instance = Partido(match_id, local, visitante, fecha, estadio)
                match_list.append(match_instance)

    return team_list, stadium_list, match_list

def valid_obj(atr, list, value):
    # Esta funcion puede validar una entrada en base a si existe como atributo dentro de un objeto, revisando cada uno de los objetos.
    # En caso de encontrar el valor deseado, retorna True, y de lo contrario, retorna False.
    attribute_list = []
    for object in list:
        attribute_list.append(getattr(object, atr))

    for i in attribute_list:
        if value.lower() == i.lower():
            return True
    return False

def busqueda(option):
    # Esta funcion se encarga de buscar las partidas pertenecientes a un pais, independiente de que sea el equipo local o visitante.

    shown_matches = []

    if option == '1':
        
        print('Estos son los equipos:')
        for team in team_list:
            print(getattr(team, 'pais'))
            
        country_choice = input('Escoge el nombre del pais por el cual quiere buscar:\n')
        
        if valid('pais', team_list, country_choice) == True:
            for match in match_list:
                if match.local.pais == country_choice.capitalize():
                    shown_matches.append(match)
                if match.visitante.pais == country_choice.capitalize():
                    shown_matches.append(match)
        else:
            print('Entrada invalida.')

    if option == '2':

        print('Estos son los estadios:')
        for stadium in stadium_list:
            print(getattr(stadium, 'nombre'))

        stadium_choice = input('Escoge el nombre del estadio por el cual quiere buscar:\n')

        if valid('nombre', stadium_list, stadium_choice) == True:
            for stadium in stadium_list:
                if stadium.nombre.lower() == stadium_choice.lower():
                    stadium_choice_id = stadium.stadium_id
                    break
 
            for match in match_list:
                if match.estadio.stadium_id == stadium_choice_id:
                    shown_matches.append(match)

        else:
            print('Entrada invalida.')

    if option == '3':

        dates = []

        print('Estos son las fechas de los partidos:')
        for match in match_list:
                atr = getattr(match, 'fecha')
                if atr not in dates:
                    dates.append(atr)

        for date in dates:
            print(date)
        
        date_day = input('Escoge el dia:\n')
        date_month = input('Escoge el mes:\n')
        if len(date_month) < 2:
            date_month = list(date_month)
            date_month.insert(0, '0')
            date_month = ''.join(date_month)
        date_year = input('Escoge el año:\n')

        date_choice = (f'{date_year}-{date_month}-{date_day}')

        if valid('fecha', match_list, date_choice) == True:
            for match in match_list:
                if match.fecha == date_choice:
                    shown_matches.append(match)

        else:
            print('Entrada invalida.')

    return shown_matches

def filtro(m_list):
    i = 0
    for match in m_list:
        i += 1
        print(f'\n{i}) {match.mostrar()}\n')

def valid_name(value):
    try:
        
        


def valid_dni(value):
    try:
        value = int(value)
        if len(str(value)) < 6 or :
            print('Cedula invalida.')
        return(value)
    except:
        print('Entrada invalida.')
        return None
    
def valid_age(value):
    try:
        value = int(value) > 120
        return value
    except:
        print('Entrada invalida.')
        return None
    
def valid_match(value):
    try:
        value = int(value)
        if value < 1 or value > 36:
            print('Este partido no existe')
            return None
        return value
    except:
        print('Entrada invalida.')
        return None

def valid_user(user):
    for attr in getattr(user, attr):

def get_user():
    print('Introduzca los siguientes datos:')
    nombre = input('Nombre:\n')
    cedula = valid_dni(input('Cedula:\n'))
    edad = valid_age(input('Edad:\n'))
    
    filtro(match_list)
    match_select = input('Seleccione un partido: ')
    valid_match(match_select)

    for match in match_list:
            if match_list.index(match) == match_select - 1:
                partido = match
                break

    tipo = input('Tipo de entrada:\n1) General\n2) VIP\n')
    if tipo == '1':
        vip = False
    elif tipo == '2':
        vip = True
    else:
        print('Entrada invalida.')
        vip = None
        return
    
    user = Cliente(nombre, cedula, edad, partido, vip)
    user_list.append(user)

    return user

#def make_map(rows, columns):
    map = []
    for row in range(rows):
        aux = []
        for column in range(columns):
            aux.append(False)
        map.append(aux)
    return map


#def show_map_general(map):
    print('*' * len(map[1]) + ' Estadio ' + '*' * len(map[1]))
    print('\n')

    seat = '   '
    for i, x in enumerate(map[1]):
        if i > 8:
            seat += str(i+1)+'| '
        else:
            seat += str(i+1)+'| '
    print(seat)

#print(show_map_general(make_map(10,10)))


# def show_map_vip(map):

def ticket_cost(user):
    cost = 0
    if user.vip == False:
        cost += 35
    elif user.vip == True:
        cost += 75
    elif user.vip == None:
        print('Usuario no tiene ticket.')
        return
    





        



    
