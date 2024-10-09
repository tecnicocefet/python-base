#!/usr/bin/env python3
"""Hello World multi Linguas.

Dependendo da lingua configurada no ambiente o programa
exibe a menssagem correspondente.

Como usar:

Tenha a variável LANG devidamente configurada exemplo:

    export LANG=pt_BR.UTF-8

Execução


    python3 hello.py
    ou
    ./hello.py    

"""
__version__ = "0.0.1"
__author__ = "João Carlos"
__licence__ = "Unlicence"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Olá, Mundo!"

if current_language == "en_US":
    msg = "Hello, World!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "fr_FR":
    msg = "Bonjour, le monde!"  
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
       
print(msg)
