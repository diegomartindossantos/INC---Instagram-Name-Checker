import requests
from time import sleep


#Creacion de VARIABLES para su posterior uso
instagram_url = "https://www.instagram.com/"
test_users = ["leomessi\n","cristiano ","zz910832hj"] #El salto de linea y el espacio estan a proposito para forzar la comprobacion

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



for x in test_users: #POR CADA USUARIO...
    if "\n" in x:  #Comprobamos que el usuario no tiene un salto de linea en la string que le guarda. (Al cargar archivos puede pasar)
        x = x.replace("\n","\\n")
        print (f"[ERROR] Fixing lane break error from user: -{x}-") #Replace \n por \\n para poder imprimir el usuario sin un salto de linea en consola
        x = x.replace("\\n","")
        sleep(1)
        print (f"[FIXED] -{x}-")
        print ("#"*50)
        try_user(x)
    elif " " in x: #Comprobamos que el usuario no contiene espacios.
        print (f"[ERROR] Fixing SPACE error from user -{x}-")
        x = x.replace(" ","")
        print (f"[FIXED] -{x}-")
        print ("#"*50)
        try_user(x)
    else: #Si la str del usuario esta limpia...
        try_user(x)



#Cosas pendientes: 
#PROXIES HEADERS, TIEMPO ENTRE SOLICITUDES

