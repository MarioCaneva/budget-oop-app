# 💸 Budget App (OOP)

This Python project allows you to manage your budget across different categories such as Food, Clothing, and Entertainment using object-oriented programming (OOP). It features a transaction ledger and a text-based bar chart to visualize spending.

---

## 📦 Features

- Deposit and withdraw funds per category
- Transfer funds between budget categories
- Ledger tracking with description and amount
- Balance check and fund availability validation
- Spending bar chart visualization per category

---

## 🔧 How It Works

### ✅ Category Class

Each `Category` object:
- Tracks transactions in a ledger
- Allows deposits, withdrawals, and transfers
- Prints a nicely formatted statement

### 🧮 Spend Chart

The `create_spend_chart()` function:
- Displays a bar chart of percentage spent in each category
- Aligns bars and category names as in the FreeCodeCamp challenge

---

## 📌 Example

```python
food = Category("Food")
clothing = Category("Clothing")
entertainment = Category("Entertainment")

food.deposit(1000, "initial deposit")
food.withdraw(200.50, "groceries")
food.transfer(50, clothing)
entertainment.deposit(500, "bonus")
entertainment.withdraw(100, "movies")

print(food)
print(create_spend_chart([food, clothing, entertainment]))
Output
markdown
Copy
Edit
*************Food*************
initial deposit        1000.00
groceries              -200.50
Transfer to Clothing    -50.00
Total: 749.50

Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o     o  
 20| o     o  o
 10| o  o  o  o
  0| o  o  o  o
    -----------
     F  C  E
     o  l  n
     o  o  t
     d  t  e
        h  r
        i  t
        n  a
        g  i
           n
           m
           e
           n
           t
🧠 Concepts Practiced
Python classes and object-oriented design

Ledger-like data tracking

Formatted text output

Basic data visualization using text
