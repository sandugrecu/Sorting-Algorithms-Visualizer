import tkinter as tk
from tkinter import ttk
import time 
import threading

class SortVisualizer:
    def __init__(self, window, userList):
        self.window = window
        self.window.title("Sorting visualization")
        self.window.geometry("600x600")

        self.listaNesortata = userList
        self.canvas = None
        self.delayEntry = None
        
        self.create_widgets()
        self.list_visualization(self.listaNesortata)

    #Metoda care creeaza UI-ul
    def create_widgets(self):
        # Descrierea aplicației
        descrierea = ttk.Label(self.window, text="Sorting Algorithms Visualization App.")
        descrierea.pack()

        # Canvas pentru vizualizarea listei
        self.canvas = tk.Canvas(self.window, width = 350, height= 300, bg = "white")
        self.canvas.pack(pady=30)

        #Afisarea numarului de iteratii
        self.numarIteratii = tk.StringVar()
        self.numarIteratii.set("Number of iterations: 0")
        numarIteratiiLabel = tk.Label(self.window, textvariable = self.numarIteratii)
        numarIteratiiLabel.pack()

        # Frame pentru butoanele de sortare
        sortari = tk.Frame(self.window)
        sortari.pack()

        bubbleSortButton = tk.Button(sortari, text="Bubble Sort Start", command=self.start_bubble_sort)
        bubbleSortButton.grid(row=0, column=0, padx=5)

        selectionSortButton = tk.Button(sortari, text="Selection Sort Start", command=self.start_selection_sort)
        selectionSortButton.grid(row=0, column=1, padx=5)

        insertionSortButton = tk.Button(sortari, text="Insertion Sort Start", command=self.start_insertion_sort)
        insertionSortButton.grid(row=0, column=2, padx=5)

        mergeSortButton = tk.Button(sortari, text="Merge Sort Start", command=self.start_merge_sort)
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

        # Frame pentru câmpul de introducere a listei
        listFrame = tk.Frame(self.window)
        listFrame.pack()

        listInputLabel = tk.Label(listFrame, text="Insert numbers (5, 2, 3): ")
        listInputLabel.pack(side='left')

        self.inputList = tk.Entry(listFrame)
        inputList = [10, 2, 4, 9, 8, 5, 7, 6, 3, 1]
        self.inputList.pack(side='left', padx=10, pady=20)

        updateListDelayButton = tk.Button(listFrame, text = "Update list and delay", command=self.updateListDelay)
        updateListDelayButton.pack(side='right')

    def updateListDelay(self):
        try:
            self.delay = float(self.delayEntry.get())
        except ValueError:
            self.delay = 0.1
        
        input_text = self.inputList.get()
        try:
            self.listaNesortata = [int(x) for x in input_text.split(",")]
        except ValueError:
            self.listaNesortata = [10, 2, 4, 9, 8, 5, 7, 6, 3, 1]

        self.list_visualization(self.listaNesortata)

    #Functia pentru vizualizarea unei liste
    def list_visualization(self, lista, a=9999, b=999999):
        self.canvas.delete("all")  
        color = "blue"

        nrPatrate = len(lista)
        latimea = 350 / nrPatrate * 0.95
        gap = 350 / nrPatrate * 0.05
        inaltimeUnitate = 300 / max(lista) * 0.95

        for i, j in enumerate(lista):
            if (i == b) or (i == a):
                color = "green" #Daca suntem pe patratul care il controlam in coloram in verde
            self.canvas.create_rectangle(i * latimea + (i + 1) * gap, 300 - lista[i] * inaltimeUnitate, (i + 1) * latimea + i * gap, 300, fill=color)
            color = "blue"

    #Algoritmul bubble sort 
    def bubble_sort_ascending(self, listaNesortata):
        lista = listaNesortata.copy()
        self.list_visualization(lista)
        delay = float(self.delayEntry.get())
        time.sleep(delay)

        iteratii = 0
        n = len(lista)
        for j in range(n - 1):
            swapped = False
            for i in range(n - 1 - j):
                if lista[i] > lista[i + 1]:
                    #vizualizam lista inainte de shimbari (coloral elementele colorate cu verde)
                    self.list_visualization(lista, i, i+1)
                    time.sleep(delay)

                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
                    swapped = True

                    #vizualizam lista si actualizam nr de iteratii
                    self.list_visualization(lista, i, i+1)
                    iteratii += 1
                    self.numarIteratii.set(f"Numar iteratii: {iteratii}")
                    time.sleep(delay)
            if not swapped:
                break
        return lista

    def start_bubble_sort(self):
        self.updateListDelay()
        #thread-ul pentru bubble sort ca sa nu blocam UI-ul
        threading.Thread(target=self.bubble_sort_ascending, args=(self.listaNesortata,), daemon=True).start()

    #Algoritmul selection sort 
    def selection_sort_ascending(self, listaNesortata):
        lista = listaNesortata.copy()
        self.list_visualization(lista)
        delay = float(self.delayEntry.get())
        time.sleep(delay)

        iteratii = 0
        n = len(lista)
        for i in range(n-1):
            minimIndex = i
            for j in range(i+1, n):
                if lista[j] < lista[minimIndex]:
                    minimIndex = j

                self.list_visualization(lista, i, minimIndex)
                time.sleep(delay)
                
            lista[i], lista[minimIndex] = lista[minimIndex], lista[i]
            iteratii += 1

            self.list_visualization(lista, i, minimIndex)
            iteratii += 1

            self.numarIteratii.set(f"Numar iteratii: {iteratii}")
            self.list_visualization(lista)
            time.sleep(delay)

    def start_selection_sort(self):
        self.updateListDelay()
        threading.Thread(target=self.selection_sort_ascending, args=(self.listaNesortata,), daemon=True).start()

    def insertion_sort_ascending(self, listaNesortata):
        lista = listaNesortata.copy()
        self.list_visualization(lista)
        delay = float(self.delayEntry.get())
        time.sleep(delay)

        #Insertion sort algorithm
        iteratii = 0
        n = len(lista)
        for i in range(1, n):
            key = lista[i]
            j = i - 1

            self.list_visualization(lista, i, j)
            time.sleep(delay)

            while j >= 0 and lista[j] > key:
                lista[j + 1] = lista[j]
                j -= 1

                self.list_visualization(lista, i, j)  # Vizualizare pas cu pas
                iteratii += 1
                self.numarIteratii.set(f"Numar iteratii: {iteratii}")
                time.sleep(delay)

            lista[j + 1] = key
            self.list_visualization(lista, i, j+1)  # Vizualizare pas final pentru acest pas
            time.sleep(delay)

    def start_insertion_sort(self):
        self.updateListDelay()
        threading.Thread(target=self.insertion_sort_ascending, args=(self.listaNesortata,), daemon=True).start()

    def merge_sort_ascending(self, listaNesortata):
        lista = listaNesortata.copy()
        self.list_visualization(lista)
        delay = float(self.delayEntry.get())
        time.sleep(delay)

        #Algoritmul pentru merge sort
        iteratii = [0] 
        def merge_sort(lista, left, right):
            if left < right:
                mid = (left + right) // 2
                merge_sort(lista, left, mid)
                merge_sort(lista, mid + 1, right)
                
                merge(lista, left, mid, right)
                self.list_visualization(lista)
                time.sleep(delay)

        def merge(lista, left, mid, right):
            left_part = lista[left:mid + 1]
            right_part = lista[mid + 1:right + 1]

            i = j = 0
            k = left

            while i < len(left_part) and j < len(right_part):
                if left_part[i] < right_part[j]:
                    lista[k] = left_part[i]
                    i += 1
                else:
                    lista[k] = right_part[j]
                    j += 1
                k += 1
                
                iteratii[0] += 1
                self.numarIteratii.set(f"Numar de iteratii: {iteratii[0]}")

            while i < len(left_part):
                lista[k] = left_part[i]
                i += 1
                k += 1

            while j < len(right_part):
                lista[k] = right_part[j]
                j += 1
                k += 1

        merge_sort(lista, 0, len(lista) - 1)

    def start_merge_sort(self):
        self.updateListDelay()
        threading.Thread(target=self.merge_sort_ascending, args=(self.listaNesortata,), daemon=True).start()


def main():
    # Creăm fereastra și instanțiem aplicația
    window = tk.Tk()

    list = [10, 2, 4, 9, 8, 5, 7, 6, 3, 1]
    app = SortVisualizer(window, list)

    # Rulăm fereastra
    window.mainloop()

main()
