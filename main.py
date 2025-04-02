import tkinter as tk
from tkinter import ttk
import time 
import threading

class SortVisualizer:
    def __init__(self, window, userList):
        self.window = window
        self.window.title("Vizualizare sortari")
        self.window.geometry("600x600")

        self.listaNesortata = userList
        self.canvas = None
        self.delayEntry = None
        
        self.create_widgets()
        self.list_visualization(self.listaNesortata)

    def create_widgets(self):
        # Descrierea aplicației
        descrierea = ttk.Label(self.window, text="Aplicatie de vizualizarea a algoritmilor de sortare. ")
        descrierea.pack()

        # Canvas pentru vizualizarea listei
        self.canvas = tk.Canvas(self.window, width = 350, height= 300, bg = "white")
        self.canvas.pack(pady=30)

        # Frame pentru butoanele de sortare
        sortari = tk.Frame(self.window)
        sortari.pack()

        bubbleSortButton = tk.Button(sortari, text="Bubble Sort Start", command=self.start_bubble_sort)
        bubbleSortButton.grid(row=0, column=0, padx=5)

        selectionSortButton = tk.Button(sortari, text="Selection Sort Start", command=self.start_selection_sort)
        selectionSortButton.grid(row=0, column=1, padx=5)

        insertionSortButton = tk.Button(sortari, text="Insertion Sort Start", command=self.start_bubble_sort)
        insertionSortButton.grid(row=0, column=2, padx=5)

        mergeSortButton = tk.Button(sortari, text="Merge Sort Start", command=self.start_bubble_sort)
        mergeSortButton.grid(row=0, column=3, padx=5)

        # Frame pentru câmpul de introducere a delay-ului
        delayFrame = tk.Frame(self.window)
        delayFrame.pack()

        delayLabel = tk.Label(delayFrame, text="Delay: ")
        delayLabel.pack(side='left')

        self.delayEntry = tk.Entry(delayFrame)
        delayImplicit = "0.1"
        self.delayEntry.insert(0, delayImplicit)  # Setăm valoarea implicită a delay-ului
        self.delayEntry.pack(side='right', padx=10, pady=20)

    def list_visualization(self, lista):
        #Functia pentru vizualizarea unei liste
        self.canvas.delete("all")  # Curăță canvas-ul

        nrPatrate = len(lista)
        latimea = 350 / nrPatrate * 0.95
        gap = 350 / nrPatrate * 0.05
        inaltimeUnitate = 300 / max(lista) * 0.95

        for i, j in enumerate(lista):
            self.canvas.create_rectangle(i * latimea + (i + 1) * gap, 300 - lista[i] * inaltimeUnitate, (i + 1) * latimea + i * gap, 300, fill="blue")

    def bubble_sort_ascending(self, listaNesortata):
        #Algoritmul selection sort 
        lista = listaNesortata.copy()
        self.list_visualization(lista)
        delay = float(self.delayEntry.get())
        time.sleep(delay)

        n = len(lista)
        for j in range(n - 1):
            swapped = False
            for i in range(n - 1 - j):
                if lista[i] > lista[i + 1]:
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
                    swapped = True
                    self.list_visualization(lista)
                    time.sleep(delay)
            if not swapped:
                break
        return lista

    def start_bubble_sort(self):
        #thread-ul pentru bubble sort ca sa nu blocam UI-ul
        threading.Thread(target=self.bubble_sort_ascending, args=(self.listaNesortata,), daemon=True).start()

    def selection_sort_ascending(self, listaNesortata):
        #Algoritmul selection sort 
        lista = listaNesortata.copy()
        self.list_visualization(lista)
        delay = float(self.delayEntry.get())
        time.sleep(delay)

        n = len(lista)
        for i in range(n-1):
            minimIndex = i
            for j in range(i+1, n):
                if lista[j] < lista[minimIndex]:
                    minimIndex = j
            lista[i], lista[minimIndex] = lista[minimIndex], lista[i]
            self.list_visualization(lista)
            time.sleep(delay)

    def start_selection_sort(self):
        threading.Thread(target=self.selection_sort_ascending, args=(self.listaNesortata,), daemon=True).start()



# Creăm fereastra și instanțiem aplicația
window = tk.Tk()
list = [10, 2, 4, 9, 8, 5, 7, 6, 3, 1, 2]
app = SortVisualizer(window, list)

# Rulăm fereastra
window.mainloop()
