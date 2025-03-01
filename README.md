# IS-Assignment 

IS assignment. Loan management system created using Django, HTML, and Bootstrap 4 CSS.

## Features

- **Customer Management**: Register and manage customer details.
- **Loan Management**: Apply for loans, track loan status, and make payments.
- **Admin Interface**: Loan officers can manage customers, loans, and payments.
- **Loan Prediction**: Predict the likelihood of a loan applicant defaulting using a logistic regression model.


## Prerequisites

- Python 3.10 or later
- Jupyter Notebook
- Visual Studio Code


## Setup 

1. Clone the repository:
    ```bash
    git clone https://github.com/brandonkongwe/IS-Assignment.git
    cd IS-Assignment
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate  
    ```

3. Install dependencies:
    ```bash
    python -m pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Create a superuser (for admin access):
    ```bash
    python manage.py createsuperuser 
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Access the application:
   
    Open your browser and go to http://127.0.0.1:8000/ 

    Admin interface: http://127.0.0.1:8000/admin/


## Usage

### Customer Features

- **Register**: Create a new account.
- **Login**: Access your dashboard.
- **Apply for Loan**: Submit a loan application.
- **Loan Payments**: Make payments towards your loan.

### Admin Features

- **Manage Customers**: Add, update, or delete customer records.
- **Manage Loans**: Approve, reject, or update loan applications.
- **Manage Payments**: Review and process loan payments.
- **Predict Defaulters**: Use the loan prediction model to assess the likelihood of loan default.
