# finance_calculators

## Description
This repository has been created following a task executed in the HyperionDev/Cogrammar bootcamp Nov 2023-March 2024
This Python script provides functionalities to calculate returns on investments and monthly payments for bonds. It allows users to input parameters such as deposit amount, interest rate, number of years, and interest type (simple or compound) for investments, as well as present value, interest rate, and repayment period for bonds. The script then computes the corresponding results based on the chosen option.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)

## Installation
1. Clone the repository:
    ```
    git clone https://github.com/yourusername/yourrepository.git
    ```
2. Navigate to the project directory:
    ```
    cd yourrepository
    ```

## Usage
1. Import the required library:
    ```python
    import math
    ```
2. Run the script:
    ```python
    python finance_calculators.py
    ```
3. Follow the on-screen prompts to choose between calculating an investment or a bond and provide the necessary input.
4. View the calculated results.

### Example

```
Your calculator:
investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan
Enter either 'investment' or 'bond' from the menu above to proceed: investment
Please enter the amount of money: 5000
Please enter the interest rate (number only and omit percentage sign): 6.5
Please enter the number of years for investment: 3
Please enter 'simple' or 'compound' interest: compound
Your investment after 3 years at 6.5% compound interest will be: 6076.57
