# Sorting Algorithms Visualizer

A Python GUI app for visualizing how popular sorting algorithms work in real time. Built using **Tkinter**, this tool lets users input custom lists, control animation delay, and observe the inner workings of **Bubble Sort**, **Selection Sort**, **Insertion Sort**, and **Merge Sort**.

---

## 📸 Preview

<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=11qzJAim93WC0-lkjace74PWMRFc7iwB9" width="400" />
</p>

---

## 🚀 Features

- Real-time visualization of sorting processes
- Supports 4 classic algorithms:  
  ✔ Bubble Sort  
  ✔ Selection Sort  
  ✔ Insertion Sort  
  ✔ Merge Sort
- Custom input for list values
- Adjustable animation delay
- Tracks and displays number of iterations per sort

---

## 🛠️ Technologies Used

- **Python 3**
- **Tkinter** – for GUI and canvas-based animation
- **Threading** – to keep UI responsive during sorting

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/sandugrecu/Sorting-Algorithms-Visualizer

# Navigate into the directory
cd Sorting-Algorithms-Visualizer

# Run the project
python main.py
```

## 💡 How It Works

- **Visualization**: The list is represented as rectangles, where the height of each rectangle corresponds to the value it represents.
- **Step-by-Step Sorting**: Sorting is animated with a delay (`time.sleep(delay)`) between each step to show the sorting process in action.
- **Background Threads**: Algorithms run on background threads, ensuring that the GUI remains interactive throughout the sorting process.
- **Key Comparisons**: During the sorting process, key comparisons are highlighted in green to make them stand out.

## 🧠 Future Improvements

- **More Algorithms**: Plan to add more sorting algorithms, such as Quick Sort and Heap Sort.
- **Sound Effects**: Add sound effects for comparisons and swaps to make the process more engaging.
- **Custom Sorting Options**: Implement options to sort in descending order or toggle between different themes.
