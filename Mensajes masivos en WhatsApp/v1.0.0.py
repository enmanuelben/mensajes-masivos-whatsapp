"""
whatsapp_mass_messaging v1.0.0.py :
Un código de Python para automatizar el envío de mensajes masivos de WhatsApp.
La lista de números de teléfono se almacena en moblie_no_list en formato de lista.
Los números de teléfono se importan del archivo test_numbers.csv.
Para automatizar los procesos web se utiliza selenio. Asegúrate de instalar 
los drivers web de Chrome para permitir que el selenio automatice el proceso.
"""

__author__ = "Enmanuel Benavides"
__copyright__ = "Copyright (c) 2020 Enmanuel Benavides"
__credits__ = ["Enmanuel Benavides"]
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Enmanuel Benavides"
__email__ = "ebr@criptext.com"
__status__ = "En desarrollo"

from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket

message_text = 'Este es un mensaje de prueba'
# mensaje que quieres enviar.

no_of_message = 1
# Número de veces que deseas que se envíe el mensaje.

moblie_no_list = [13025143149]
# la lista de números de teléfono puede ser de cualquier tamaño

def element_presence(by, xpath, time):

    '''
    @author Enmanuel Benavides
    Determina la presencia de drivers web.
    '''

    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)

def is_connected():

    '''
    @author Enmanuel Benavides
    Devuelve True si hace ping a www.google.com
    en el puerto 80 es exitoso.
    '''
    try:
        # conectarse al host: nos dice si el host es realmente accesible
        socket.create_connection(("www.google.com", 80))
        return True
    except BaseException:
        is_connected()

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://web.whatsapp.com")
sleep(10)
# tiempo de espera para escanear el código en segundos

def send_whatsapp_msg(phone_no, text):

    '''
    @author Enmanuel Benavides
    send_whatsapp_msg() acepta 2 argumentos: phone_no y text integer y string respectivamente.
    Para argumentos de palabras clave use send_whatsapp_msg(phone_no= ,test='').
    Conéctate a WhatsApp web y ten cuidado de ingresar números de teléfono incorrectos.
    Llame al método isConnected antes de esta función.
    '''

    driver.get(
        "https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))

    try:
        driver.switch_to_alert().accept()

    except Exception as e:
        pass

    try:
        element_presence(
            By.XPATH,
            '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',
            30)
        txt_box = driver.find_element(
            By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        global no_of_message
        for x in range(no_of_message):

            txt_box.send_keys(text)
            txt_box.send_keys("\n")

    except Exception as e:
        print("invailid phone no :" + str(phone_no))

def main():

    '''
    @author Enmanuel Benavides
    Itera a través del número de teléfono y los envía
    a la función send_whatsapp_msg
    '''

    for moblie_no in moblie_no_list:
        try:
            send_whatsapp_msg(moblie_no, message_text)

        except Exception as e:

            sleep(10)
            is_connected()


# print("functions- main, element_presence, is_connected, send_whatsapp_msg")
# print("Docs")
# print(main.__doc__)
# print(element_presence.__doc__)
# print(is_connected.__doc__)
# print(send_whatsapp_msg.__doc__)


if __name__ == '__main__':
    main()
