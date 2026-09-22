# Hand Landmark Detection ✋

A real-time hand detection program built with **OpenCV** and **MediaPipe**. It detects hand landmarks from a webcam feed, recognizes which fingers are raised, and displays the message **"I LOVE YOU SO MUCH"** on screen based on the finger combination (inspired by the ASL "I Love You" hand sign).

## Features

- Real-time hand detection from webcam using MediaPipe Hands
- Supports detecting up to 2 hands at once
- Draws hand landmarks & connections on the video frame
- Detects whether each finger (thumb, index, middle, ring, pinky) is raised
- Displays on-screen text based on which fingers are raised

## Project Structure

```
handrecognt/
├── handDetection.py   # HandDetection class (wrapper around MediaPipe Hands)
├── utama.py           # Main program: reads webcam, detects fingers, displays text
└── README.md
```

## How It Works

- **`handDetection.py`** contains the `HandDetection` class, which wraps `mediapipe.solutions.hands`. Its `findHandLandMarks()` method takes an image frame, processes it, and returns the resulting frame (with landmarks drawn if `draw=True`) along with a list of landmark coordinates for each detected hand.
- **`utama.py`** reads frames from the webcam, calls `HandDetection` to get the hand landmarks, then compares the Y position of each fingertip against its base to determine whether that finger is raised.

## Requirements

- Python 3.10
- [OpenCV](https://pypi.org/project/opencv-python/) (`opencv-python`)
- [MediaPipe](https://pypi.org/project/mediapipe/) (`mediapipe`)
- A webcam

## Installation

1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd handrecognt
   ```

2. (Optional but recommended) create a virtual environment:
   ```bash
   python -m venv env
   # Windows
   env\Scripts\activate
   # macOS/Linux
   source env/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install opencv-python mediapipe
   ```

## Usage

```bash
python utama.py
```

- A webcam window will open showing the hand detection results.
- Raise your fingers to see the corresponding text appear on screen.
- Press **`a`** to quit the program.

## Notes

- The `env/` (virtual environment) and `__pycache__/` folders should **not** be committed to GitHub. Add them to `.gitignore`:
  ```
  env/
  __pycache__/
  *.pyc
  ```

## License

Free to use and modify for learning purposes.
