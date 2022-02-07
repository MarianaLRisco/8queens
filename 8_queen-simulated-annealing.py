import math
import random

#Calcula la distancia cubierta por la ruta
def evalua_tablero(tablero):
    numcol=0
    for i in range( len(tablero)):
        for j in range(i+1, len(tablero)):
            if (tablero[i]==tablero[j] or abs(tablero[i] - tablero[j]) == abs(i-j)):
                numcol+=1
    return numcol

def simulated_annealing(tablero):
    T=20
    T_MIM=0
    v_enfriamiento=100
    while T>T_MIM:
        n_coli_actual=evalua_tablero(tablero)
        for i in range(1, v_enfriamiento):
            #intercambio de 2 ciudades aleatoriamente
            j=random.randint(0, len(tablero)-1)
            tablero_tmp=tablero[:]
            tablero_tmp[j]=random.randint(1, len(tablero))
            n_coli=evalua_tablero(tablero_tmp)
            delta=n_coli_actual-n_coli
            if (n_coli<n_coli_actual):
                tablero=tablero_tmp[:]
                break
            elif random.random() < math.exp(delta/T):
                tablero=tablero_tmp[:]
                break
        #enfriamos T linealmente
        T=T-0.005
    return tablero

#Imprime el tablero
def graficar(tablero):
        for i in range(n_reinas):
            for j in range(n_reinas):
                if tablero[i] == j+1:
                    print('R', end = '  ')
                else:
                    print('.', end = '  ')
            print()

if __name__ == '__main__':
    n_reinas=4
    tablero = [2,1,4,3] 
    print("Posiciones iniciales de las reinas",tablero)
    graficar(tablero)
    print("Reinas que se atacan: "+str(evalua_tablero(tablero)))
    
    new_tablero= simulated_annealing(tablero)
    print("\nPosiciones finales de las reinas",new_tablero)
    graficar(new_tablero)
    print("Reinas que se atacan: "+str(evalua_tablero(new_tablero)))

    