import random
from time import sleep
import math
import datetime
import PySimpleGUI as sg
import pygame
import os, time
from pygame.mixer import Sound
print("\033[7;33;40m-=-" * 54)
jo = ("\033[7;33;40m Jogo de Aventura")
print(jo.center(170))
print("\033[7;33;40m-=-" * 54)
#----------------------------------------------------------------------------------------------------------------------
inicio = input(">APERTE ENTER PARA INICIAR<")
print("\033[7;33;40m-=-" * 54)

porta = int(input(""" Olá viajante, você está em busca da pedra filofal, sua caminhada até aqui te levou para a frente do castelo Rá Tim Bum, você se depara com a porta do castelo, o que voce faz ?
Opção [1]: Abrir a porta.
Opção [2]: Bater na porta.
Opção [3]: Ir embora.
Escolha ="""))
if porta == 1:
    print("Tentando abrir a porta...")
    os.startfile(r'portaTrancada1.mp4')
    time.sleep(4)
    porta = int(input(""" Você tenta abrir a porta, porém esta trancada, o que você faz?
    Opção [1]: Bater na porta.
    Opção [2]: Ir embora.
    Escolha ="""))
    if porta == 1:
      print("Batendo na porta...")
      os.startfile(r'efeito sonoro batendo na porta_Trim.mp4')
      time.sleep(3)
      porta = int(input(""" Voce bate na porta e um porteiro de metal sai do meio da parede com uma charada para abrir a porta, ele diz: Qual a semelhança entre um corvo e uma escrivaninha ?
    Opção [1]: Você diz: Jogue os dois com força na parede, o que gritar é o corvo.
    Opção [2]: Voce diz: Ambos tem pena.
    Opção [3]: Ir embora
    Escolha ="""))
      if porta == 2:
        print("Acertou! Porta se abrindo...")
        os.startfile(r'portaAbrindo.mp4')
        time.sleep(4)
        porta = int(input(""" Voce acertou a charada do porteiro, ele abri a porta para você, o que você faz?
          Opção [1]: Você entra no castelo. 
          Opção [2]: Ir embora
          Escolha ="""))
    if porta == 1:
        print("Entrando no castelo, porta se fecha...")
        os.startfile(r'portafechando_Trim.mp4')
        time.sleep(3)
        os.startfile(r'somcobra_Trim.mp4')
        time.sleep(4)
        porta = int(input(""" Entao voce entra no castelo e a porta atras de voce se tranca deixando voce preso, uma voz misteriosa diz: Olá intruso, qual seu objetivo aqui ? Então uma cobra falante sai de dentro de uma casca de arvore ali proxima, o que respode para ela ?
           Opção [1]: Pergunta a cobra onde esta a pedra filosofal. 
           Opção [2]: Como saio do castelo.
           Escolha ="""))
    if (porta == 1):
            porta = int(input("""Cobra lhe diz: Vejo que veio atras da pedra filosofal, mas sera que esta preparado para encarar os desafios que lhe esperam ? Não sei onde ela esta, porém posso lhe falar por onde começar a procurar ela, quer saber ?
            Opção [1]: Sim, me dia por onde começar!
            Opção [2]: Não, quero saber como saio daqui!
            Escolha ="""))



elif porta == 2:
    print("Batendo na porta...")
    os.startfile(r'efeito sonoro batendo na porta_Trim.mp4')
    time.sleep(3)
    porta = int(input(""" Voce bate na porta e um porteiro de metal sai do meio da parede com uma charada para abrir a porta, ele diz: Qual a semelhança entre um corvo e uma escrivaninha ?
    Opção [1]: Você diz: Jogue os dois com força na parede, o que gritar é o corvo.
    Opção [2]: Voce diz: Ambos tem pena.
    Opção [3]: Ir embora
    Escolha ="""))
    if porta == 2:
          print("Acertou! Porta se abrindo...")
          os.startfile(r'portaAbrindo.mp4')
          time.sleep(4)
          porta = int(input(""" Voce acertou a charada do porteiro, ele abri a porta para você, o que você faz?
          Opção [1]: Você entra no castelo. 
          Opção [2]: Ir embora
          Escolha ="""))
elif porta == 3:
        print(" Você vai embora disistindo de seu sonho de encontrar a pedra filosofal.")
