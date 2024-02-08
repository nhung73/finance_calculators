This Capstone Project is a task executed during HyperionDev/CoGrammar Data Science Bootcamp November 2023/March 2024.

The user should be allowed to choose which calculation they want to do.
investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan

If the user selects ‘investment’:
● Ask the user to input:
○ The amount of money that they are depositing.
○ The interest rate (as a percentage). Only the number of the interest rate should be entered. Example, the user should enter 8 and not 8%.
○ The number of years they plan on investing.
○ Then ask the user to input if they want “simple” or “compound” interest, and store this in a variable called interest. Depending on whether or not they typed “simple” or “compound”, output the
appropriate amount that they will get back after the given period, at the specified interest rate.
○ Print out the answer!

Interest formula:
The total amount when simple interest is applied is calculated as follows: 𝐴 = 𝑃(1 + 𝑟 × 𝑡)
The Python equivalent is very similar: A = P *(1 + r*t)
The total amount when compound interest is applied is calculated as follows: 𝐴 = 𝑃(1 + 𝑟)𝑡
The Python equivalent is slightly different: A = P * math.pow((1+r),t)

If the user selects ‘bond’:
● Ask the user to input:
○ The present value of the house. e.g. 100000
○ The interest rate. e.g. 7
○ The number of months they plan to take to repay the bond. e.g. 120
○ Calculate how much money the user will have to repay each month

Bond repayment formula:
The amount that a person will have to be repaid on a home loan each month is calculated as follows: 𝑟𝑒𝑝𝑎𝑦𝑚𝑒𝑛𝑡 = 𝑖 × 𝑃1− (1+𝑖)−𝑛
The Python equivalent is slightly different: repayment = (i * P)/(1 - (1 + i)**(-n))
In the formula above:
● ‘P’ is the present value of the house.
● ‘i’ is the monthly interest rate, calculated by dividing the annual interest rate by 12. Divide the interest entered by the user by 100 e.g. (8 / 100) before dividing by 12.
● ‘n’ is the number of months over which the bond will be repaid.
