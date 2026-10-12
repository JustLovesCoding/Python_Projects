# Budget App

A simple Python budgeting application that tracks category balances, deposits, withdrawals, transfers, and spending summaries.

## Overview

This project models a basic personal finance tracker using a `Category` class. Each category stores a ledger of transactions and can calculate current balance, validate available funds, and display a spending summary.

It is a beginner-friendly project inspired by the classic FreeCodeCamp budget app challenge.

## Features

- Create custom spending categories such as Food, Clothing, Rent, and Entertainment
- Add deposits and withdrawals with optional descriptions
- Check available funds before spending
- Transfer money between categories
- View a formatted ledger for each category
- Generate a simple spending chart by category

## Project Files

- `Budget_app.py` — contains the budget logic and sample usage

## How It Works

The `Category` class includes:

- `deposit(amount, optional_des="")` — adds money to the category
- `withdraw(amount, optional_des="")` — subtracts money if the funds are available
- `transfer(amount, category)` — moves funds from one category to another
- `get_balance()` — returns the current balance
- `check_funds(amount)` — confirms whether enough money is available
- `__str__()` — prints a readable ledger with totals

The `create_spend_chart(categories)` function builds a simple percentage chart based on total spending in each category.

## Example Usage

```python
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(25.50, 'groceries')

clothing = Category('Clothing')
food.transfer(50, clothing)

print(food)
print(create_spend_chart([food, clothing]))
```

## Run the Project

From the project folder:

```bash
python Budget_app.py
```

## Notes

This is a lightweight console-based budgeting app designed to practice Python classes, data handling, and formatted output.
