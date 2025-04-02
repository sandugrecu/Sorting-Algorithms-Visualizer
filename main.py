import tkinter as tk
from tkinter import ttk
import time 
import threading

#variabilele 
delay = 1

#functia care primeste o lista si afiseaza in canvas patratele 
def listVisualization(lista):
    #curatam canvasul 
    canvas.delete("all")

    nrPatrate = len(lista)
    latimea = 350 / nrPatrate * 0.95
    gap = 350 / nrPatrate * 0.05

    inaltimeUnitate = 300 / max(lista) * 0.95

    for i, j in enumerate(lista):
        canvas.create_rectangle(i * latimea + (i + 1) * gap, 300 - lista[i] * inaltimeUnitate, (i + 1) * latimea + i * gap, 300, fill="blue")


def bubbleSortAscending(lista):
    #vizualizam lista initiala
    listVisualization(lista)
    time.sleep(delay)

    #algoritmul pentru bubble sort
    n = len(lista)
    for j in range(n - 1):
        swapped = False
        for i in range(n - 1 - j):  
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                swapped = True
                #la fiecare schimbare vom vizualiza lista si vom aplica un delay 
                listVisualization(lista)
                time.sleep(delay)
        if not swapped:  
            break
    return lista

def startBubbleSort():
    threading.Thread(target = bubbleSortAscending, args=(listaNesortata,), daemon=True).start()

#creem fereastra in care va fi tot contentul
window = tk.Tk()
window.title("Vizualizare sortari")
window.geometry("600x600")

descrierea = ttk.Label(window, text="Aplicatie de vizualizarea a algoritmilor de sortare. ")
descrierea.pack()

canvas = tk.Canvas(window, width = 350, height= 300, bg = "white")
canvas.pack(pady=30)


listaNesortata = [10, 2, 4, 9, 8, 5, 7, 6, 3, 1, 2]
#listVisualization(listaNesortata)
bubbleSortButton = tk.Button(window, text="Bubble Sort Start", command = startBubbleSort)
bubbleSortButton.pack()

#aici rulam fereastra
window.mainloop()