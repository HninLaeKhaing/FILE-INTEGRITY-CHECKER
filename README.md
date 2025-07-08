# FILE-INTEGRITY-CHECKER

# 🔐 File Integrity Checker with Kaggle Dataset Integration

This Python script helps verify the integrity of files using SHA256 hashes. It includes functionality to store file hashes, check for changes, and fetch sample data from a Kaggle dataset.

---

## 👨‍💻 Author

- **Name**: Hnin Lae Khaing  
- **GitHub**: [github.com/hninlaekhaing](https://github.com/hninlaekhaing)  
- **Project**: Built as part of a cybersecurity internship project

---

## 🚀 Features

- ✅ Calculate and store SHA256 hashes for all files in a directory.
- 🔁 Re-check file integrity to detect:
  - Modified files
  - Deleted files
  - Unchanged files
- 📦 Download sample dataset from Kaggle for testing.
- 📝 Saves and loads hashes from a JSON file (`hashes.json`).

---

## 📂 Folder Structure

---
file-integrity-checker/
├── main.py # Python script (this code)
├── hashes.json # (Auto-generated) Hash records
├── README.md # Project documentation

## 🛠️ Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/your-username/file-integrity-checker.git
   cd file-integrity-checker


## 🔒 Use Cases

File integrity monitoring

Data consistency verification

Detect tampering or corruption

Research/academic file backup checking


## 🧾 Output Example

[OK]       example.txt
[MODIFIED] notes.md
[DELETED]  old_data.csv


