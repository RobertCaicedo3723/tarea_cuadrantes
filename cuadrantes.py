print("--------------------------------")
print("---------HOLA MUNDO!------------")
print("--------------------------------")




## input

a = input("Digite la coordenada en X: ")
a = int(a)
b = input("Digite la coordenada en Y: ")
b = int(b)
c = (a, b)

### Procesing

if a>0 and b>0: 
    print("La coordenada" + str(c) + " está en el cuadrante 1") ### output

if a<0 and b>0: 
    print("La coordenada" + str(c) + " está en el cuadrante 2") ### output

if a<0 and b<0: 
    print("La coordenada" + str(c) + " está en el cuadrante 3") ### output

if a>0 and b<0: 
    print("La coordenada" + str(c) + " está en el cuadrante 4") ### output

if a==0 and b==0: 
    print("La coordenada" + str(c) + " está en el punto de origen") ### output

if a==0 and b!=0: 
    print("La coordenada" + str(c) + " está en el eje Y") ### output

if a!=0 and b==0: 
    print("La coordenada" + str(c) + " está en el eje x") ### output







