# 🎓 Data Analysis with Python (2024-2025) - Learning Journey

This repository serves as my personal record of solutions and key takeaways from the **Data Analysis with Python** course offered by the University of Helsinki (MOOC.fi). My goal is to document my progress and solidify my understanding of the entire data analysis pipeline using the Python ecosystem.

## 🗺️ Course Structure and Core Focus

The course is divided into 7 chapters, progressing from Python fundamentals to the application of Machine Learning models. My notes focus on extracting the most powerful and market-relevant concepts for practical data analysis.

| Chapter | Core Topic | Key Tools/Concepts |
| :--- | :--- | :--- |
| **1. Python** | Fundamentals and Data Structures | Lambdas, Generators, Iterables, List Comprehensions |
| **2. More Python & NumPy** | Text Cleaning and Numerical Computing Intro | Regex (`re`), OOP, Exception Handling, `np.array` |
| **3. Advanced NumPy** | Calculation Optimization and Linear Algebra | Broadcasting, Vectorization, Matrix Operations |
| **4. Pandas Essentials** | Tabular Data Manipulation and Indexing | `DataFrame`, `Series`, `.loc`, `.iloc`, Missing Data |
| **5. Advanced Pandas** | Data Transformation and Combination | GroupBy, Merging (Joins), Time Series Analysis |
| **6. Machine Learning** | Predictive Modeling and Statistics | Scikit-Learn, Regression, Classification, Clustering (K-Means) |
| **7. Final Project** | Practical Application | End-to-end integration of all learned libraries |

---

## 📝 Detailed Chapter Insights

### Chapter 1: Python - Beyond the Basics

While an introduction, this chapter emphasizes writing efficient Python code. It's not just about basic syntax, but about features that make code fast and readable for data tasks.
- **Fundamental Concepts:** Review of data types, clear formatting with `f-strings`, and the nature of dynamic typing.
- **Advanced Applications (My Focus):**
    - **Lambda Functions:** Practical use for creating concise, anonymous functions, often applied to DataFrame columns (though vectorized methods are preferred in Pandas).
    - **Iterables and Generators:** Understanding how `generators` (like `range()` or functions using `yield`) save memory, which is crucial when dealing with large datasets.
    - **List Comprehensions:** The Pythonic way to create lists, which is significantly faster and more readable than traditional loops.

### Chapter 2: More Python and NumPy Introduction

This chapter bridges pure Python development with the need for speed in numerical computing.
- **Regular Expressions (Regex):** My key takeaway is that Regex is indispensable for the **Data Cleaning** phase, allowing for standardization and extraction of patterns from unstructured text data using the built-in `re` module.
- **Object-Oriented Programming (OOP):** Focusing on classes and objects helps structure analysis code to be more organized and reusable.
- **Exception Handling:** Using `try-except` is vital for building robust data pipelines that don't crash when encountering unexpected or malformed data.
- **NumPy (Part 1):** The core concept is the `np.array`. The performance difference between Python lists and NumPy arrays is why the entire Python data science stack is built upon this library.

### Chapter 3: Advanced NumPy

The focus here is on optimizing code for maximum performance.
- **Broadcasting:** The most powerful and initially challenging concept. It's the rule that allows NumPy to perform arithmetic operations on arrays of different shapes, eliminating the need for explicit loops.
- **Vectorization:** The key to speed. Learning to replace Python loops with native NumPy array operations is the secret to processing large volumes of data quickly.
- **Linear Algebra:** A review of matrix operations, which are the mathematical foundation for many Machine Learning algorithms.

### Chapter 4: Pandas Essentials

Pandas is the daily workhorse for any Data Analyst. This chapter is about mastering tabular data manipulation.
- **DataFrames and Series:** Understanding the fundamental structures and how Pandas leverages NumPy internally.
- **Indexing and Selection:** Mastering `.loc` (label-based) and `.iloc` (position-based) for efficient and clear data access.
- **Handling Missing Data:** Strategies for imputation (`fillna`) and removal (`dropna`) of null values (`NaN`), a critical step in data preparation.

### Chapter 5: Advanced Pandas

This level introduces complex and powerful data transformation techniques.
- **GroupBy and Aggregation:** The **Split-Apply-Combine** paradigm is the essence of data analysis. Grouping data and applying aggregation functions (mean, sum, count) is the most common way to extract insights.
- **Merging and Joining:** Learning to combine DataFrames using different types of *joins* (inner, outer, left, right), mirroring SQL operations.
- **Time Series:** Focusing on how Pandas handles time-based data, including *resampling* and *rolling windows*, which are essential for financial or sensor data analysis.

### Chapter 6: Machine Learning with Scikit-Learn

The first dive into predictive modeling using the industry-standard library.
- **Scikit-Learn Workflow:** Learning the standard process: import, instantiate, train (`fit`), and predict (`predict`).
- **Supervised Learning:**
    - **Regression:** Understanding modeling for predicting continuous values.
    - **Classification:** Focusing on how to categorize data.
- **Unsupervised Learning:**
    - **Clustering (K-Means):** Grouping data for pattern discovery.
    - **Dimensionality Reduction (PCA):** Simplifying complex data for visualization and model performance improvement.

---

## 📂 Repository Structure

To keep my learning organized, the repository follows a standard data science project structure:

```text
.
├── data/                   # Datasets used in exercises and projects
├── part01-01/              # Solved exercises for Chapter 1, Part 1 (e.g., Python Basics)
├── part01-02/              # Solved exercises for Chapter 1, Part 2, and so on...
├── notebooks/              # Jupyter Notebooks for experiments and detailed analysis
├── notes/                  # Complementary notes and theoretical summaries
├── requirements.txt        # Dependencies needed to run the code
└── README.md               # This learning guide
```

---
*This is a personal learning repository and not a commercial product. All rights to the course material belong to the University of Helsinki / MOOC.fi.*
