# Eturf

Eturf is a cutting-edge web platform designed to simplify the process of booking turf locations. Users can log in, search for available turf slots, and make reservations with ease. The platform aims to reduce booking errors and enhance user satisfaction.

## Features

- **User Authentication**: Secure login and registration system for users.
- **Turf Search**: Search for available turfs based on location, time, and other preferences.
- **Real-time Availability**: Check turf availability in real-time.
- **Booking Management**: Users can book, cancel, and manage their reservations.
- **Admin Dashboard**: Admin panel to manage turf listings, view bookings, and handle user queries.

## Installation

To set up the project locally, follow these steps:

### Prerequisites

- Python 3.x
- Django
- PostgreSQL (or any preferred database)
- pip (Python package installer)

### Clone the Repository

```bash
git clone https://github.com/shadow-slave/Eturf.git
cd Eturf
```

## Install Dependencies
Install the required Python packages:
``` pip install -r requirements.txt ```

### Database Setup
1. Create a PostgreSQL database:
   ``` createdb eturf_db ```
2. Update the database settings in `settings.py`:
   ```bash
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'eturf_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
      }
    }

3. Migrate the database:
   ``` python manage.py migrate ```
### Run the Server 
Start the Django development server:
  ``` python manage.py runserver ```
  
Visit `http://127.0.0.1:8000/` in your browser to see the application in action.

## Usage
1. **Sign Up / Log In**: Create a new account or log in with your existing credentials.
2. **Search for Turfs**: Use the search feature to find available turf locations based on your preferences.
3. **Book a Slot**: Select an available time slot and confirm your booking.
4. **Manage Bookings**: View, edit, or cancel your bookings from the user dashboard.

## Project Structure 
1. **/eturf**: Core project settings and configurations.
2. **/users**: User authentication and profile management.
3. **/turf**: Turf listings, search functionality, and booking management.
4. **/static**: Static files such as CSS, JavaScript, and images.
5. **/templates**: HTML templates for rendering views.

## Contributing
Contributions are welcome! If you’d like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request

## License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
