# tax-planning
plan your tax roughly with a couple of questions

Need: Tax Return is done after the year ENDS. One should plan his/her tax liability carefully BEFORE the year ends.
Purpose: Calculate the estimated tax liability. Compare with estimated withhold. Plan accordingly. 
Fact: IRS may charge penalty for over $1000 tax debt. 

So you should pay your taxes such that you do not owe more than $1000. Otherwise, there might be an 8%-9% penalty.

A couple of notes:
- Code asks numbers from you. It does NOT check if you're eligible for the credits, deductions, etc. It just does "calculations"
- Code works in local, not connected, nothing stored in cloud
- When run in terminal or on any IDE (I use PyCharm), it interactively computes tax liability. Very similar to TurboTax
- The difference is that this is very simple, takes a couple minutes, yet doesn't fit to all.
- It only works for people who has W2, but asks if you have other taxable income (after expenses)
- Earned Income Tax Credit (EITC) mechanism is not added yet
- Only works for married jointly filing option so far. 

How to run:
- Download the code in ZIP
- Run get_user_input.py

You may need to install pandas, as I plan to use this library to write the numbers to excel.
Run "pip install pandas" or "pip3 install pandas" in terminal if you have MAC
