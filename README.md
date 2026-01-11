# Lab 02: Reading Markdown Files

## 🎯 Learning Objectives

By the end of this lab, you will be able to:
- Read text files using Python's `open()` function
- Handle file encoding (UTF-8 for Thai text)
- Count characters, words, and lines in a file
- Search for specific text within files

## ⏰ Time Allocation (3 hours)

| Activity | Duration |
|----------|----------|
| 🎯 Lecture & Slides | 30 min |
| 📖 Tutorial Notebook | 60 min |
| ☕ Break | 15 min |
| ✍️ Exercise Notebook | 45 min |
| 📤 Submit & Auto-grade | 15 min |
| 💬 Q&A | 15 min |

## 📁 Files in This Lab

```
template-lab02-read-file/
├── README.md
├── slides/
│   └── Lab02_Slides.tex
├── tutorial/
│   └── Lab02_Tutorial.ipynb
├── exercise/
│   └── Lab02_Exercise.ipynb
├── data/
│   ├── rubella.md
│   └── cholera.md
└── tests/
    └── test_lab02.py
```

## 🚀 Getting Started

1. Open `tutorial/Lab02_Tutorial.ipynb` to learn the concepts
2. Complete `exercise/Lab02_Exercise.ipynb`
3. Push to GitHub and check your score

## 📚 Key Concepts

### Reading Files in Python
```python
# Open and read entire file
with open("data/rubella.md", "r", encoding="utf-8") as f:
    content = f.read()

# Read line by line
with open("data/rubella.md", "r", encoding="utf-8") as f:
    lines = f.readlines()
```

### Why This Matters for RAG
RAG systems need to:
1. **Read** documents from various sources
2. **Process** the text content
3. **Index** for later retrieval

This lab teaches the foundation: reading files!

## 🏆 Grading

| Exercise | Points |
|----------|--------|
| Exercise 1: Read file content | 25 |
| Exercise 2: Count characters | 25 |
| Exercise 3: Count lines | 25 |
| Exercise 4: Find text in file | 25 |
| **Total** | **100** |

---
**Course:** CSI403 - Full Stack Program Development  
**Lab:** 02 - Reading Markdown Files
