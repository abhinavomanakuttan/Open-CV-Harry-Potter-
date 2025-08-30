# 🧙‍♂️ Harry Potter Invisibility Cloak (Made with OpenCV)

Have you ever wanted to become invisible like **Harry Potter with his magical Invisibility Cloak**?
Well… now you can! (at least in front of your webcam 😉)

This project uses **Computer Vision (OpenCV)** to create a fun illusion — when you wear a red cloth (acting as the cloak), the computer makes it disappear by replacing it with the background.

Even if you haven’t seen Harry Potter 🎥:
👉 Just imagine you hold a red cloth in front of you, and suddenly you vanish while the room is still visible! ✨

---

## ⚙️ What You Need to Install

Before running this project, make sure you have:

1. **Python 3.x** (preferably Python 3.8 or higher)
   👉 [Download Python](https://www.python.org/downloads/)

2. Required Python Libraries (install using pip):

   ```bash
   pip install opencv-python
   pip install numpy
   ```

3. A working **webcam** (built-in or external).

---

## 🛠 How the Magic Works (Step-by-Step)

This project is designed so even **school students** can follow it easily! 🎓

---

### 🖼️ Process Flow Diagram

```
[ Start Webcam ] 
       |
       v
[ Capture Background ] ---> (stored in memory)
       |
       v
[ Detect Cloak Color (Red in HSV) ]
       |
       v
[ Create Mask for Cloak ]
       |
       v
[ Replace Cloak Region with Background ]
       |
       v
[ Display Final Output (Invisible Cloak) ]
```

---

### 🎨 Cloak Detection (HSV Color Space)

We use **HSV (Hue, Saturation, Value)** because it’s better for detecting colors than RGB.

* **Hue (H):** Type of color (red, blue, green…)
* **Saturation (S):** Intensity of the color
* **Value (V):** Brightness

![HSV Color Wheel](https://raw.githubusercontent.com/opencv/opencv/master/doc/tutorials/imgproc/imgproc_hsv/hsv_colorwheel.png)

For **Red Cloak**, we use two ranges:

* `0°–10°` → Red on one end of wheel
* `170°–180°` → Red wraps around to the other end

---

### 📸 Example Workflow

1. **Normal Frame:** You with red cloth
   ![Input Frame](https://i.ibb.co/z7sB9fJ/red-cloth.jpg)

2. **Cloak Mask:** Computer detects red parts only
   ![Mask Example](https://i.ibb.co/svhPJdM/mask-detection.jpg)

3. **Final Output:** Cloak area replaced with background
   ![Final Output](https://i.ibb.co/DL7Bg7X/invisible.jpg)

---

## 🏃 How to Run

1. Save the code into a file, for example:

   ```
   invisibility_cloak.py
   ```

2. Run it using:

   ```bash
   python invisibility_cloak.py
   ```

3. Wear a **red cloth** and watch yourself disappear! 😱

---

## 🔑 Key Learnings

* Basics of **Computer Vision** 🖥️
* How to work with **OpenCV & NumPy**
* Concept of **color detection** in HSV
* How to combine **masks** and **background replacement**

---

## 🎉 Fun Challenge for You

* Try changing cloak color from **red** to **blue** or **green** by adjusting HSV ranges.
* Add sound effects (like a magic "whoosh" 🎶) when cloak activates.
* Record a fun video and show your friends how you “became invisible”!

---

✨ Have fun coding, and may your cloak always stay invisible! ✨

---
