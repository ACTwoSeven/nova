# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 07:10:50 2025

@author: Andre
"""

ubicaciones = {
    "cafetería": "Desde la salida de Investigación, sube 12 escalones y gira a la izquierda. Luego, sube 10 escalones más. Desde allí, camina 19 pasos a la derecha y baja 5 escalones. Sigue recto 44 pasos, gira a la derecha y avanza 13 pasos. Luego, gira a la izquierda, camina 10 pasos más y habrás llegado a la cafetería.",
    
    "baño": "Para ir al baño más cercano, sube 12 escalones, gira a la izquierda y sube 10 escalones más. Da 2 pasos, luego gira nuevamente a la izquierda y avanza 24 pasos. Baja un escalón a tu izquierda y habrás llegado al baño.",
    
    "capilla": "Desde la salida de Investigación, sube 12 escalones, gira a la izquierda y sube otros 10 escalones. Da 2 pasos y gira a la izquierda para caminar 24 pasos más. Baja un escalón, camina 6 pasos y sube 12 escalones hacia la rampa. Avanza 6 pasos más y sube una escalera de 9 escalones. Luego, gira a la izquierda y llegarás a la capilla.",
    
    "talento humano": "Desde la salida de Investigación, sube 12 escalones, gira a la izquierda y sube otros 10 escalones. Luego, gira nuevamente a la izquierda y sube 10 escalones más. Continúa por una escalera en espiral de dos niveles, sube otros 10 escalones y gira a la derecha. Allí encontrarás la oficina de talento humano.",
    
    "ascensor": "Desde la salida de Investigación, sube 12 escalones, gira a la izquierda y sube otros 10 escalones. Luego, gira a la izquierda, camina 9 pasos y gira nuevamente a la izquierda. Avanza 12 pasos, vuelve a girar a la izquierda y camina 6 pasos más. Allí encontrarás el ascensor del primer piso.",
    
    "cafetería abierta": "Desde la salida de Investigación, sube 12 escalones, gira a la izquierda y sube 10 escalones más. Camina 20 pasos al frente, sube un escalón y en 12 pasos habrás llegado a la cafetería de espacio abierto, donde puedes disfrutar de un buen jugo.",
    
    "enfermería": "Desde la salida de Investigación, sube 12 escalones, gira a la izquierda y sube otros 10 escalones. Luego, gira a la derecha y avanza 19 pasos. Baja 5 escalones, sigue recto 44 pasos y gira a la izquierda. Camina 10 pasos, baja 8 escalones y sigue recto 9 pasos más. Luego, baja 7 escalones, avanza otros 9 pasos, gira a la derecha y camina 6 pasos para llegar a enfermería.",
    
    "clínica": "Desde la salida de Investigación, sube 12 escalones, gira a la izquierda y sube 10 escalones más. Luego, gira a la derecha, camina 19 pasos y baja 5 escalones. Sigue recto 44 pasos, gira a la izquierda y avanza 10 pasos. Baja 8 escalones y camina 9 pasos más. Luego, baja 7 escalones, sigue recto 32 pasos, gira a la izquierda y avanza 6 pasos. Después, gira a la derecha, camina 13 pasos, vuelve a girar a la derecha y avanza 4 pasos más. Allí encontrarás las clínicas odontológicas.",
    
    "entrada": "Desde la salida de Investigación, sube 12 escalones, gira a la izquierda y sube otros 10 escalones. Camina 2 pasos, gira a la derecha y avanza 18 pasos. Luego, baja 6 escalones y camina 5 pasos más. Baja un escalón, camina 33 pasos, baja 2 escalones y avanza 19 pasos. Baja otros 10 escalones, camina 8 pasos más y habrás llegado a la entrada."
}
ubicaciones_pasos = {
    "cafetería": "Sube la escalera, gira a la derecha y encontrarás primero la cafetería de administración. Más adelante, está la cafetería estudiantil.",
    
    "baño": "Sube la escalera, gira a la izquierda y sigue el pasillo. A mitad de camino, a la izquierda, encontrarás el baño.",
    
    "capilla": "Sube las escaleras, gira a la izquierda y sigue el pasillo. Al final, a la izquierda, está la capilla.",
    
    "talento humano": "Sube las escaleras, gira dos veces a la izquierda y sigue subiendo. Después de la escalera en espiral, gira a la derecha y llegarás a talento humano.",
    
    "ascensor": "Sube las escaleras, gira a la izquierda y sigue hasta el pasillo. En la esquina, detrás de las escaleras, encontrarás el ascensor.",
    
    "cafetería abierta": "Sube las escaleras y al frente verás una rampa que lleva a la cafetería al aire libre, ideal para tomar jugos.",
    
    "enfermería": "Sube las escaleras y gira a la derecha para bajar a la zona de la cafetería. Luego, sigue recto y, antes de las escaleras del bloque B, gira a la izquierda y baja. La enfermería está a la derecha.",
    
    "clínica": "Sube las escaleras, gira a la derecha y baja a la zona de la cafetería. Luego, gira a la izquierda y sigue derecho hacia la entrada. Antes de salir, a la izquierda, están las clínicas.",
    
    "entrada": "Sube las escaleras, gira a la derecha y baja a la zona de la cafetería. Luego, gira a la izquierda y sigue recto hasta la entrada."
}
