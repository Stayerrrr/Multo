# Lyrics Typing Animation in Python

This program is a small **Python text animation project** that prints song lyrics to the terminal with a typing effect, similar to lyric videos or TikTok-style text timing.

---

## 📌 Program Overview

The script prints each lyric **character by character** with a delay, then waits before moving to the next line. This creates a smooth, dramatic lyric-sync effect.

The lyrics used are from:
**"Multo" – Cup of Joe**

---

## ✨ Features

* Character-by-character typing animation
* Custom delay per character
* Custom delay per lyric line
* Clean terminal output
* Beginner-friendly Python code

---

## 🧠 How It Works

### Data Structures

* `lyric` → A list of tuples:

  * Lyric line (string)
  * Character delay (float, in seconds)

* `line_delays` → A list of delays between each lyric line

### Flow

1. Print song title
2. Wait 2 seconds
3. Loop through each lyric line
4. Print characters one by one with delay
5. Pause before printing the next line

---

## ▶️ How to Run

Make sure Python is installed, then run:

```bash
python lyrics.py
```

(Replace `lyrics.py` with the actual filename.)

---

## 📂 Code Structure

* `run_lyrics()` → Main function that handles animation logic
* `sys.stdout.flush()` → Forces characters to appear instantly
* `time.sleep()` → Controls animation timing

---

## 🎯 Learning Objectives

This program helps you practice:

* Python lists and tuples
* Loops and enumeration
* Time-based execution (`sleep`)
* Terminal output control
* Simple animation logic

---

## 📝 Notes

* Timing values can be adjusted to better sync with the song.
* This project is for **learning and fun**, not commercial use.

---

**Code by San-Z**

