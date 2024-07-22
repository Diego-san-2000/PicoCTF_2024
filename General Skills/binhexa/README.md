# binhexa
![Descripcion del CTF](img/description.png)

## Descripción
How well can you perfom basic binary operations?  
Additional details will be available after launching your challenge instance.

## Resolución
Una vez que nos conectemos, se nos proporcionarán dos números en binario y deberemos hacer una serie de operaciones con ellos:

![Consola](img/1.png)

Muchas de estas operaciones podremos hacerlas manualmente, sin embargo para otras necesitaremos una consola con python abierta:

```bash
python3
```

1. Para la primera operación se nos pide realizar un &, esto es un 'and' entre los dos números. Lo realizaremos en python de la siguiente forma:

```python
a = int("11000101", 2)
b = int("01011100", 2)
print(bin(a&b))
```
Obteniendo como resultado: '0b1000100', quitando el '0b' tendremos el número a introducir:

![Consola](img/2.png)

2. Ahora nos pide una suma:

```python
print(bin(a+b))
```

![Consola](img/3.png)

Obteniendo como resultado '100100001'.

![Consola](img/4.png)

3. En tercer lugar nos pide un desplazamiento de un bit a la izquierda en el primer binario. Esto se hace moviendo todos los números un lugar a la izquierda:

![Consola](img/5.png)

4. Ahora nos pide un desplazamiento a la derecha en el segundo binario:

![Consola](img/6.png)

5. En penúltimo lugar nos pide una multiplicación, para ello recurriremos a python:

```python
print(bin(a*b))
```

![Consola](img/7.png)

Obteniendo como resultado '100011011001100'.

![Consola](img/8.png)

6. Para finalizar, nos pide que realicemos un 'or':

```python
print(bin(a|b))
```

![Consola](img/9.png)

Obteniendo como resultado: '11011101'.

![Consola](img/10.png)

Y que introduzcamos ese número en hexadecimal:

```python
print(hex(a|b))
```

![Consola](img/11.png)

Obteniendo '0xdd'.

![Consola](img/12.png)

Y devolviendo la flag: 'picoCTF{b1tw^3se_0p3eR@tI0n_su33essFuL_aeaf4b09}'.