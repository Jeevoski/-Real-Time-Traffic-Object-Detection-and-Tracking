
markdown
# 🚦 Real-Time Traffic Object Detection and Tracking

This project uses **YOLOv8** and the **SORT tracking algorithm** to detect and track vehicles and pedestrians in real time from video. It draws bounding boxes, assigns unique IDs, and counts objects that cross a virtual line.

![demo](demo.gif) <!-- Optional: attach a demo .gif or image -->

---

## 📌 Features

- ✅ Detects objects like **cars, buses, motorcycles, trucks, and pedestrians**
- ✅ Assigns each object a **unique ID** using the SORT tracker
- ✅ Draws a **counting line** and keeps track of how many objects cross it
- ✅ Displays **object type + ID** (e.g., `car ID 2`)
- ✅ Works on webcam or video files

---

## 🛠️ Tech Stack

- Python 3.8+
- [YOLOv8](https://github.com/ultralytics/ultralytics) (Ultralytics)
- OpenCV
- NumPy
- SORT (Simple Online Realtime Tracking)
- FilterPy (for Kalman Filter used in SORT)

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/traffic-detection-tracking.git
cd traffic-detection-tracking
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> Make sure you also install [YOLOv8](https://docs.ultralytics.com/) via:

bash
pip install ultralytics


### 3. Run the project

```bash
python traffic.py
```

This will run object detection and tracking on `traffic_video.mp4`.

---

## 📁 Folder Structure

```
.
├── traffic.py               # Main program
├── sort.py                  # SORT tracker
├── kalman_filter.py         # Kalman tracking for SORT
├── yolov8n.pt               # YOLOv8 model file
├── traffic_video.mp4        # Your test video
└── README.md
```

---

## 🎥 Output Example

* Class + ID (e.g., `bus ID 3`)
* Count of vehicles/pedestrians crossing a virtual line

![output](sample_output.jpg)

---

## 🧠 Credits

* [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
* [abewley/sort](https://github.com/abewley/sort)

---

## 🙋‍♂️ About Me

👋 Hi, I'm Jeevan George John — a first-year Computer Science student exploring AI and computer vision. This is one of my very first real-world coding projects.
I'm learning one build at a time. 😄

---

## 📬 Contact

* LinkedIn: \[Your LinkedIn Link]
* Email: \[Your email if you'd like]

---

## ⭐️ Support

If you like this project, give it a ⭐️ and follow me for more beginner-friendly builds!
 ✅ Want Bonus?

Let me know if you also want:
- `requirements.txt` generated for this project
- `VideoWriter` added to save output as `.avi` or `.mp4`
- A GitHub repo name suggestion

Just say the word and I’ll get it ready! 🚀
```
