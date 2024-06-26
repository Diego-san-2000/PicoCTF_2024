# Scan Surprise
![Descripcion del CTF](img/description.png)

## Descripción
People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate. You can download the challenge files here:

- [challenge.zip](https://artifacts.picoctf.net/c_rhea/10/challenge.zip)

Additional details will be available after launching your challenge instance.

## Resolución
Extraemos el contenido del archivo comprimido:

´´´bash
unzip challenge.zip
´´´

Se nos creará la estructura de carpetas 'home/ctf-player/drop-in' con el siguiente contenido:

![Contenido de drop-in](img/1.png)

![Contenido de drop-in](img/2.png)

Si escaneamos el código nos dará el siguiente resultado:

![Contenido de drop-in](img/3.png)

A mi no me ha funcionado ningún servicio de escaneo de qr online, así que he tenido que usar Google lens.

La flag obtenida es 'picoCTF{p33k_@_b00_3f7cf1ae}'.