# Banking Aggregator

This project is a banking aggregator website designed to help users compare and apply for loans from various banks in Azerbaijan. The platform provides a user-friendly interface for loan comparison, application processes, and access to bank information.

## Features

- **Loan Comparison**: Users can compare different loan products based on various criteria such as loan amount, term, and type.
- **Bank Directory**: A comprehensive list of participating banks with details about their loan products.
- **User Profiles**: Users can create and manage their profiles for a personalized experience.
- **Loan Calculators**: Tools to help users calculate loan affordability, monthly payments, and debt-to-income ratios.
- **Educational Resources**: Articles and guides explaining different loan types, banking terms, and tips for choosing the right loan.

## Project Structure

```
banking_aggregator/
├── banking_aggregator/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── apps/
│   ├── loans/
│   ├── banks/
│   └── users/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── loans/
│   ├── banks/
│   └── users/
├── manage.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd banking_aggregator
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Navigate to `http://127.0.0.1:8000/` in your web browser to access the application.
- Use the loan comparison tool to find the best loan options for your needs.
- Explore the bank directory to learn more about participating banks and their offerings.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.