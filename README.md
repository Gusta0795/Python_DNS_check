# Python_DNS_check
A python program to check a variety of DNS entries

1️⃣ Instalar as dependências

pip install PyQt6 dnspython

* PyQt6: Para criar a interface gráfica
* dnspython: Para fazer consultas DNS

2️⃣ Criar um protótipo da interface

Podemos usar o Qt Designer para montar o layout sem precisar codificar tudo na mão.
Depois, convertemos o .ui para código Python com:

pyuic6 layout.ui -o layout.py
