# Custom Database Engine

### **Project Overview**
This project is a custom relational database engine implemented in Python, designed to create, store, manipulate, and query in-memory relational data. It supports complex query operations through a terminal-based interface and ensures accuracy and reliability via robust syntax and semantic validation. The engine is modular and extensible, making it capable of handling advanced database features such as joins and aggregations.

---

### **Features**
- **Relational Database Engine**: Create, store, and query in-memory relational data.
- **Foundational Components**: Built-in data storage structures and relational algebra operators for efficient database processing.
- **User-Friendly Interface**: Terminal-based interface to parse, validate, and execute relational algebra queries.
- **Advanced Query Handling**: Supports syntax and semantic validation for complex queries.
- **Modular Design**: Extensible to include advanced features such as joins and aggregations.
- **Flexible Dataset Support**: Works with any dataset formatted according to defined schema requirements.

---

### **Installation and Setup**
1. **Download Files**:
   - Ensure you download all the required project files, excluding `testDrivers`.
   - Place all files, including the ones inside `testQueries`, in the same directory.
2. **Run the Program**:
   - Open a terminal and navigate to the directory containing the files.
   - Execute the Python scripts as shown in the examples below.

---

### **Usage Instructions**
Here are some examples of how to run queries using the terminal and the expected outputs:

#### **Example 1: Running `Query1.py`**
```bash
PS C:\Users\jess\Desktop\DatabaseProject> python3 Query1.py company
ANSWER(FNAME:VARCHAR,LNAME:VARCHAR,ADDRESS:VARCHAR)
Number of tuples: 4

Franklin:Wong:638 Voss, Houston, TX:
John:Smith:731 Fondren, Houston, TX:
Ramesh:Narayan:971 Fire Oak, Humble, TX:
Joyce:English:5631 Rice, Houston, TX:
```

#### **Example 2: Running `Query2.py`**
```bash
PS C:\Users\jess\Desktop\DatabaseProject> python3 Query2.py company
ANSWER(PNUMBER:INTEGER,DNUM:INTEGER,LNAME:VARCHAR,ADDRESS:VARCHAR,BDATE:VARCHAR)
Number of tuples: 2

10:4:Wallace:291 Berry, Bellaire, TX:20-JUN-31:
30:4:Wallace:291 Berry, Bellaire, TX:20-JUN-31:
```

#### **Example 3: Running `Query3.py`**
```bash
PS C:\Users\jess\Desktop\DatabaseProject> python3 Query3.py company
ANSWER(LNAME:VARCHAR,FNAME:VARCHAR)
Number of tuples: 2

Zelaya:Alicia:
Jabbar:Ahmad:
```

---

### **Database Requirements**
The project includes two example dataset files:
- `company`
- `drinks`

This program is compatible with any other database file, provided the file adheres to the same format as these example datasets.

---

### **Technical Details**
- **Language**: Python
- **Core Features**:
  - Data storage structures
  - Relational algebra operators
  - Terminal-based query interface
- **Extensibility**: Designed using modular principles for advanced features like joins and aggregations.

---

### **Future Enhancements**
- Add support for additional relational operations.
- Improve the query parser for more complex queries.
- Optimize performance for handling larger datasets.

---

### **Contact**
For any questions or feedback, feel free to reach out!

---

