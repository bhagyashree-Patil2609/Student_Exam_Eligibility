# 🎓 Student Examination Eligibility Evaluation System

A web-based system that evaluates student examination eligibility based on attendance percentage. Built using Python and Gradio.

---

## 📌 Project Overview

This system allows users to upload a `.txt` attendance file containing student roll numbers and attendance percentages. Based on predefined criteria, the system determines whether a student is:

- ✅ Eligible for Exam  
- ⚠️ Condonation Required  
- ❌ Not Eligible  

The eligibility report is displayed instantly in a structured format.

---

## ⚙️ Tech Stack

- Python  
- Gradio (Web Interface)  
- File Handling  
- Conditional Logic Processing  

---

## 📂 Project Structure

Student_Exam_Eligibility/
│
├── ui.py                # Gradio UI
├── backend.py           # Eligibility evaluation logic
├── requirement.txt      # Dependencies
└── README.md

---

## 📄 Input File Format

The uploaded `.txt` file must follow this format:

301, 90  
302, 78  
303, 60  
304, 45  

Format:  
RollNumber, AttendancePercentage

---

## 🧠 Eligibility Criteria

- Attendance ≥ 85% → ELIGIBLE FOR EXAM  
- Attendance between 65% – 84% → CONDONATION REQUIRED  
- Attendance < 65% → NOT ELIGIBLE  

---

## 🚀 How to Run Locally

1. Clone the repository:

git clone https://github.com/your-username/Student_Exam_Eligibility.git  
cd Student_Exam_Eligibility  

2. Install dependencies:

pip install -r requirement.txt  

3. Run the application:

python ui.py  

---

## 🌟 Features

- File upload validation  
- Automatic eligibility evaluation  
- Handles invalid records gracefully  
- Clean, modern UI with custom styling  
- Instant eligibility report generation  

---

## 📈 Future Improvements

- CSV file support  
- Downloadable report  
- Attendance summary dashboard  
- Database integration  

---

## 👩‍💻 Author

Bhagyashree Patil  
M.Tech Artificial Intelligence
