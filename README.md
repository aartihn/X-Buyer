# XBuyer - Buy & Sell Second-Hand Items

XBuyer is an online platform where users can buy and sell second-hand items. The platform allows users to view products, register an account, log in, and add products to their shop for selling.

## Features
- User registration and authentication
- Browse products for sale
- View product details
- Add and manage products in the shop
- Responsive design using Bootstrap
- Easy-to-navigate user interface

## Table of Contents
1. [Installation](#installation)
2. [Technologies](#technologies)
3. [Setup](#setup)
4. [Usage](#usage)
5. [File Structure](#file-structure)
6. [Contributing](#contributing)
7. [License](#license)

## Installation

### Prerequisites
- Python 3.x
- Django 4.x
- PostgreSQL (or SQLite for development)

### Steps to Install
1. Clone the repository:
   ```bash
   git clone https://github.com/Akash-Agarwal-X/X-Buyer.git
   cd xbuyer
   ```

2. Set up a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser for admin access (optional):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Open your browser and go to `http://127.0.0.1:8000` to view the application.

## Technologies

- **Backend**: Django
- **Frontend**: HTML, CSS (Bootstrap)
- **Database**: SQLite (default for development), PostgreSQL (for production)
- **Authentication**: Django’s built-in authentication system

## Setup

### Database Configuration
- The project is set up with SQLite by default, but you can switch to PostgreSQL by editing the `DATABASES` setting in `settings.py`.
- To configure PostgreSQL:
  1. Install PostgreSQL and create a database.
  2. Update the `DATABASES` setting in `settings.py`:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'yourdbname',
             'USER': 'yourusername',
             'PASSWORD': 'yourpassword',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

### Static Files
- The project uses static files (CSS, JS) that are loaded using Django’s `{% static %}` tag.
- During production, remember to collect static files:
  ```bash
  python manage.py collectstatic
  ```

## Usage

1. **Homepage**: Displays all available products.
2. **Shop**: View products in your shop.
3. **Login/Registration**: Users can log in or create an account to sell or buy products.
4. **Product Pages**: Each product has a detail page showing more information.
5. **Logout**: Users can log out from the site.

### Routes:
- **Home**: `/` - Displays products for sale.
- **Register**: `/register/` - User registration page.
- **Login**: `/login/` - User login page.
- **Shop**: `/shop/` - User’s shop where they can manage their products.
- **Logout**: `/logout/` - Logs the user out and redirects them to the home page.

## File Structure

```bash
xbuyer/
│
├── xbuyer/                  # Main project directory
│   ├── __init__.py
│   ├── settings.py            # Django settings
│   ├── urls.py                # URL routing for the application
│   ├── wsgi.py
│   └── asgi.py
│
├── store/                     # App directory for product management
│   ├── __init__.py
│   ├── admin.py               # Admin configuration for models
│   ├── apps.py
│   ├── models.py              # Product model
│   ├── views.py               # Views for handling user requests
│   ├── templates/             # Template files for rendering HTML
│   │   ├── home.html          # Home page template
│   │   ├── register.html      # Registration page template
│   │   ├── login.html         # Login page template
│   │   ├── shop.html          # Shop page template
│   ├── urls.py                # URL configuration for app-specific views
│   └── migrations/            # Database migrations
│
├── manage.py                  # Django management script
├── requirements.txt           # List of Python packages for the project
└── README.md                  # Project readme
```

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Make your changes and commit them (`git commit -am 'Add new feature'`)
4. Push to your branch (`git push origin feature-name`)
5. Create a pull request

Please ensure your code follows the Django style guide and includes tests where applicable.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
