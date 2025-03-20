# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 13:03:07 2025

@author: Andre
"""
from ubicaciones import ubicaciones
from deep_translator import DeeplTranslator
import pyttsx3
import speech_recognition as sr
import pywhatkit
import pyjokes
import datetime
import time
import webbrowser

languageDefault="es"
language=languageDefault
mic_index = 1  # Asegúrate de que este número coincide con tu dispositivo

def transf_audio_texto():
    r = sr.Recognizer()
    #Configuración microfono
    with sr.Microphone(device_index=mic_index) as origen:
        r.pause_threshold = 1
        print("Grabando")
        audio = r.listen(origen)
        print("Listo")
        try:
            print("en el try")
            pedido = r.recognize_google(audio,language = "es-co")
            print("Audio a texto: ",pedido)
            return pedido
        except sr.UnknownValueError:
            print("Sorry no hablo cetaceo")
            return ""

import os

def hablar(mensaje):
    print(f"Asistente: {mensaje}")
    os.system(f'pico2wave -l es-ES -w temp.wav "{mensaje}" && aplay temp.wav && rm temp.wav')

    
def saludo():
    hora = datetime.datetime.now()
    if hora.hour < 6 and hora.hour >19 :
        saludo = "Buenas noches "
    elif hora.hour >= 6 and hora.hour <13 :
        saludo = "Buenos días"
    else:
        saludo = "Buenas tardes"
    hablar(f"{saludo}")
    
def elegir_idioma():
    hablar("Hola, ¿en qué idioma quieres hablar?")
    idioma=transf_audio_texto()
    global language
    if idioma[0]=='p':
        language="pt"
    elif idioma[0] == 'e':
        language="es"
    elif idioma[0] == 'i':
        language="en"
    else:
        hablar("No entendi cuál idioma deseas")

    
def solicitar_dia():
    dia=datetime.date.today()
    print(dia)
    dia_semana = dia.weekday()
    print(dia_semana)
    semana={0:"Lunes",1:"Martes",2:"Miercoles",3:"Jueves",
            4:"Viernes",5:"Sabado", 6:"Domingo"}
    hablar(f"Hoy es {dia} {semana[dia_semana]}")
    
def solicitar_hora():
    hora = datetime.datetime.now()
    print(hora.hour)
    hablar(f"Son exactament las {hora.hour} con {hora.minute} minutos y {hora.second} segundos")
    
def escuchar_palabra_clave():
    r = sr.Recognizer()
    print("Esperando activación...")
    while True:
        with sr.Microphone(device_index=mic_index) as origen:
            try:
                audio = r.listen(origen)
                texto = r.recognize_google(audio, language="es-co").lower()
                if "hola" in texto:
                    saludo()
                    return True
            except sr.UnknownValueError:
                continue

def iniciar_asistente():
    while True:
        if escuchar_palabra_clave():
            menu()
            

def menu():
    global ultimo_uso
    comenzar = True
    discapacidad_visual = True
    #hablar("Bienvenido al asistente de la Universidad Santo Tomás ubicado en Investigación, recuerda que puedes: saber el día, la hora, puedo contarte una broma, reproducir música y proporcionar información sobre las ubicaciones cercanas de la USTA con los pasos en caso de que tengas alguna discapacidad visual, además de instrucciones, no dudes en preguntar! ")
    hablar("Para acceder a nuestro sistema de ubicaciones tenemos una pregunta: tienes algun tipo de discapacidad visual? responde si o no")
    discapacidad = transf_audio_texto().lower()
    if "si" in discapacidad:
        discapacidad_visual=True
    else:
        discapacidad_visual = False
    while comenzar:
        hablar("¿Cuál es tu solicitud?")
        ultimo_uso = time.time()
        solicitud=transf_audio_texto().lower()
        if "día" in solicitud:
            solicitar_dia()
            continue
        elif "qué hora es" in solicitud:
            solicitar_hora()
            continue
        elif "reproducir" in solicitud:
            hablar("Amo escuchar música... Tienes buen gusto!")
            solicitud=solicitud.replace("busca en internet","")
            webbrowser.open(f"https://www.youtube.com/watch?v=-QkmEVNA-fo")
            time.sleep(15)
            os.system("pkill chromium")
            continue
        elif "broma" in solicitud:
            hablar(pyjokes.get_joke('es'))
            continue
        elif "ubicaciones" in solicitud:
            hablar("Puedes preguntarme por: " + ", ".join(ubicaciones.keys()))
        elif any(lugar in solicitud for lugar in ubicaciones.keys()):
            for lugar in ubicaciones.keys():
                if lugar in solicitud:
                    if discapacidad_visual:
                        hablar(ubicaciones_pasos[lugar])
                    else:
                        hablar(ubicaciones[lugar])
                    break
            continue
        elif "instrucciones" in solicitud:
            hablar("Para hacer tu solicitud recuerda decir al palabra clave de la acción que quieres que realice, puede ser ubicaciones, para saber qué ubicaciones tengo disponible, o dónde queda cafetería, qué hora es hoy, etc.")
            continue
        elif "finalizar" in solicitud:
            hablar("Gracias por usar nuestro servicio")
            break
        else:
            hablar("No entendí")
            continue
        
engine = pyttsx3.init()




import threading

ultimo_uso = time.time()

def verificar_inactividad():
    global ultimo_uso
    while True:
        time.sleep(10)  # Revisa cada 60 segundos
        if time.time() - ultimo_uso > 30:  # Si pasan 5 minutos sin interacción
            ultimo_uso = time.time()
            hablar("Recuerda que estoy aqui, mientras un chistesito: ",pyjokes.get_joke('es'))

#Ejecutar en segundo plano
threading.Thread(target=verificar_inactividad, daemon=True).start()


iniciar_asistente()