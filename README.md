# Python_DNS_check  
A python program to check a variety of DNS entries  

1️⃣ Instalar as dependências  

pip install PyQt6 dnspython  

* PyQt6: To create graphical interface  
* dnspython: To make DNS requests  

2️⃣ Create an interface prototype  

Podemos usar o Qt Designer para montar o layout sem precisar codificar tudo na mão.  
Depois, convertemos o .ui para código Python com:  

pyuic6 layout.ui -o layout.py  
