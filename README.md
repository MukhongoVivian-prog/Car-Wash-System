Car Wash System ProjectDescriptionThis is a web-based car wash system that allows customers to book and pay for car wash services. The system manages the entire workflow, from booking and payment to service completion and customer feedback.Key features:User Authentication: Secure login system for customers, administrators, and workers.Service Management: Display available services with pricing.Booking and Payment: Customers can book services and pay online.Booking Cancellation: Customers can cancel their bookings (within a specific time frame, e.g., 24 hours).Receipt Generation: Customers receive receipts upon successful payment (printable or digital).Task Management: Administrators assign service tasks to workers.Service Completion: Workers notify customers and administrators upon service completion.Notifications: Automated notifications and confirmations for customers and administrators.Customer Reviews: Customers can leave reviews after service completion.Admin Dashboard: Administrators can track the entire process.Project StructureThe project is built using Django and is organized into the following apps:Car/
├── Authentic/       # User authentication
├── Booking/         # Customer booking management
├── dashboard/       # Admin, customer, and worker dashboards
├── main/            # Main application logic
├── notification/    # Notifications and confirmations
├── payment/         # Payment processing
├── review/          # Customer reviews
├── services/        # Service definitions
├── templates/      # HTML templates
├── static/         # CSS, JavaScript, and vendor files
└── media/          # Storage for uploaded media (e.g., images)
Setup InstructionsFollow these steps to set up the project:Clone the Repository:git clone https://github.com/MukhongoVivian-prog/Car-Wash-System
cd Car-Wash-System
Create a Virtual Environment:Linux and macOS:python3 -m venv venv
source venv/bin/activate
Windows:python -m venv venv
.\venv\Scripts\activate
Install Dependencies:pip install django
# Install other project dependencies (if any).  For example:
# pip install -r requirements.txt
Run Migrations:python3 manage.py migrate
Create a Superuser (Admin):python3 manage.py createsuperuser
Run the Development Server:python3 manage.py runserver
The server will start at http://127.0.0.1:8000/.ContributionsPrepared by Vivian and Eureliah.
