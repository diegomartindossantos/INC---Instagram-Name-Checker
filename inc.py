import requests


#Creacion de VARIABLES para su posterior uso
instagram_url = "https://www.instagram.com/"
test_users = ["leomessi","cristiano","zz910832hj"]

def try_user(user):
    #Definiendo urls
    url = instagram_url+user
    r = requests.get(url)
    #comienza la comprobacion del status_code de la petición
    if r.status_code == 200:
        print (f"[TAKEN] {user}")
    elif r.status_code == 404:
        print (f"[FREE] {user}")
    else:
        print (f"[ERROR] {user}")



for x in test_users:
    try_user(x)



#Cosas pendientes: 
#PROXIES HEADERS, TIEMPO ENTRE SOLICITUDES, COMPROBACIÓN DE LAS STR DE LOS NOMBRES

