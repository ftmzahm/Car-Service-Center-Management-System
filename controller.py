import mysql.connector

from model import User, Customer, Service, Payment,Appointment,Review,Vehicle
import re
from mysql.connector import Error
import datetime
from datetime import date


class UserController :
    #id,username,password,role
    def __init__(self, username="", password="", role="", user_id=""):
        self.username = username
        self.password = password
        self.role = role
        self.user_id = user_id

    def add_user(self):
        username, password, role, user_id = self.username.strip(), self.password.strip(), self.role.strip(), self.user_id.strip()

        if not re.fullmatch(r"^[a-zA-Z0-9_ ]{2,255}$", username):
            return False, "Use a-z A-Z 0-9 _ between 2 and 255 char for username"

        # must contain at least one lower case one upper case one number and a special char
        if not re.fullmatch(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+=\-\[\]{};':\"\\|,.<>/?]).{8,}$",
                            password):
            return False, "Must contain at least one lower case, one upper case, one number and a special char "

        if role not in ["Admin", "Employee", "Mechanic"]:
            return False, "Invalid Role"

        user = User(username,password,role)
        user.add_user()
        return True, "User added successfully"


    def remove_user(self):
        user_id = self.user_id.strip()

        try:
            int_user_id = int(user_id)
            if int_user_id  <= 0:
                return False, "use positive number"
        except (ValueError, TypeError):
            return False, "use positive number"

        user = User(user_id=user_id)
        user.remove_user()
        return True, "user removed successfully"

    def edit_user(self):
        username, password, role, user_id = (self.username.strip(), self.password.strip(), self.role.strip(),
                                             self.user_id.strip())

        if not re.fullmatch(r"^[a-zA-Z0-9_ ]{2,255}$", username):
            return False, "Use a-z A-Z 0-9 _ between 2 and 255 char for username"

        # must contain at least one lower case one upper case one number and a special char
        if not re.fullmatch(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+=\-\[\]{};':\"\\|,.<>/?]).{8,}$",
                            password):
            return False, "Must contain at least one lower case, one upper case, one number and a special char "

        if role not in ["Admin", "Employee","Mechanic"]:
            return False, "Invalid Role"

        try:
            int_user_id = int(user_id)
            if int_user_id  <= 0:
                return False, "use positive number"
        except (ValueError, TypeError):
            return False, "use positive number"

        user = User(username, password, role,user_id)
        user.edit_user()
        return True, "User edited successfully"

    @staticmethod
    def get_all_users():

        """ administration """

        try:
            user = User()
            result = user.get_all_users()
            return result
        except Exception as e:
            print(e)

    def login_user(self):

        """ authentication if a user with specific username and password exists """

        username,password = self.username.strip(), self.password.strip()

        if not re.fullmatch(r"^[a-zA-Z0-9_ ]{2,255}$", username):
            return False, "Use a-z A-Z 0-9 _ between 2 and 255 char for username"

        # must contain at least one lower case one upper case one number and a special char
        if not re.fullmatch(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+=\-\[\]{};':\"\\|,.<>/?]).{8,}$",
                            password):
            return False, "Must contain at least one lower case, one upper case, one number and a special char "

        # we should both validate database authentication and Regex validation

        user = User(username,password)
        result = user.login_user()
        if result:
            return True, result
        else:
            return False, "Invalid username or password"

    def search_user(self):
        user_id = self.user_id.strip()

        try:
            user_id = int(user_id)

            if user_id <= 0:
                return False, "Use positive number"

        except (ValueError, TypeError):
            return False, "Invalid ID"

        user = User(user_id=user_id)

        result = user.search_user()

        if result:
            return True, result

        return False, "User not found"

class CustomerController :
    #customer_id,name,phone,email

    def __init__(self, name="", phone="", email="", customer_id=""):
        self.name = name
        self.phone = phone
        self.email = email
        self.customer_id = customer_id

    def add_customer(self):
        name, phone, email = self.name.strip(), self.phone.strip(), self.email.strip()

        if not re.fullmatch(r"^[a-zA-Z0-9_ ]{2,255}$", name):
            return False, "use a-z A-Z 0-9 _ between 2 and 255 char"

        if not re.fullmatch(r"^[\w.-]+@[\w.-]+\.\w+$",email):
            return False , "Invalid email"

        if not re.fullmatch(r"^(09\d{9}|\+989\d{9})$", phone):
            return False, "Invalid phone number"

        try:
            customer = Customer(name,phone,email)
            customer.add_customer()
            return True, "customer added successfully"
        except Error as e:
            if e.errno == 1062:       # for duplicate entries (phone number)
                return False, "Phone number is already used"
            else:
                return False, "Unknown Error"


    def remove_customer(self):
        customer_id = self.customer_id.strip()

        try:
            int_customer_id = int(customer_id)
            if int_customer_id  <= 0:
                return False, "use positive number"

        except (ValueError, TypeError):
            return False, "Invalid id"

        try:
            customer = Customer(customer_id=customer_id)
            customer.remove_customer()
            return True, "customer removed successfully"

        except Error as e:
            if e.errno == 1451: #MySQL foreign key delete restriction error (we didn't delete on cascade in customer)
                return False, "Cannot delete customer because related records exist"
            return False, f"Database error: {e}"


    def edit_customer(self):
        name, phone, email, customer_id = (self.name.strip(), self.phone.strip(), self.email.strip(),
                                           self.customer_id.strip())

        if not re.fullmatch(r"^[a-zA-Z0-9_ ]{2,255}$", name):
            return False, "use a-z A-Z 0-9 _ between 2 and 255 char"

        if not re.fullmatch(r"^[\w.-]+@[\w.-]+\.\w+$", email):
            return False, "Invalid email"

        if not re.fullmatch(r"^(09\d{9}|\+989\d{9})$", phone):
            return False, "Invalid phone number"

        try:
            int_customer_id = int(customer_id)
            if int_customer_id  <= 0:
                return False, "use positive number"
        except (ValueError, TypeError):
            return False, "user valid number"

        customer = Customer(name=name, phone=phone, email=email, customer_id=customer_id)
        customer.edit_customer()
        return True, "customer edited successfully"


    def search_customer(self):
        customer_id = self.customer_id.strip()

        try:
            customer_id = int(customer_id)

            if customer_id <= 0:
                return False, "Use positive number"

        except (ValueError, TypeError):
            return False, "Invalid ID"

        customer = Customer(customer_id=customer_id)

        result = customer.search_customer()

        if result:
            return True, result

        return False, "Customer not found"


    @staticmethod
    def get_all_customers():
        try:
            customer = Customer()
            result = customer.get_all_customers()
            return result
        except Exception as e:
            print(e)

    def add_customer_return_id(self):
        """
        Creates a new customer and returns the generated customer id
        :return: customer_id
        """
        customer = Customer(self.name, self.phone, self.email)

        try:
            success, customer_id = customer.add_customer_return_id()
            return True, customer_id

        except mysql.connector.Error as e:

            if e.errno == 1062:
                return False, "This phone number is already registered"

            return False, f"Database Error: {e}"

    def get_customer_id_by_phone(self):
        """
        Looks for an existing customer before creating a new one it also prevents duplicate customers
        :return:customer_id or None
        """

        customer = Customer(phone=self.phone)

        result = customer.find_customer_by_phone()

        if result:
            return result[0] # fetchone returns tuple we want the number
        return None

    def login_customer(self):

        name = self.name.strip()
        phone = self.phone.strip()

        if not name or not phone:
            return False, "Please fill in both fields"

        customer = Customer(name=name, phone=phone)
        result = customer.login_customer()

        if result:
            return True, {
                "customer_id": result[0],
                "name": result[1],
                "phone": result[2],
                "email": result[3]
            }

        return False, "Name or phone number is incorrect"



class VehicleController :
    # vehicle_id, customer_id, brand, model, plate_number,year

    def __init__(self,customer_id="" , brand="", model="", year="", plate_number=""):
        self.customer_id = customer_id
        self.brand = brand
        self.model = model
        self.year = year
        self.plate_number = plate_number



    def add_vehicle(self):
        brand, model, year, plate_number, customer_id = (self.brand.strip(), self.model.strip(), self.year.strip(),
                                             self.plate_number.strip(), self.customer_id.strip())

        if not re.fullmatch(r"^[a-zA-Z0-9_ ]{2,50}$",brand):
            return False, "use alphanumeric char between 2 and 50 chars for brand"

        if not re.fullmatch(r"^[a-zA-Z0-9_ ]{1,50}$",model):
            return False, "use alphanumeric char between 1 and 50 chars for model"

        try:
            year = int(year)
            if year < 1970 or year > 2026:
                return False, "Year must be between 1970 and 2100"
        except (ValueError, TypeError) as e:
            return False, "Year must be a number"

        if not re.fullmatch(r"^\d{2}\s[ب-ی]\s\d{3}\sایران\s\d{2}$", plate_number):
            print(repr(plate_number))
            return False, "Plate format must be like: 28 ب 444 ایران 12"

        try:
            int_customer_id = int(customer_id)
            if int_customer_id  <= 0:
                return False, "use positive number"
        except (ValueError, TypeError) as e:
            print(e)
            return False, "use valid number"

        vehicle = Vehicle(customer_id=customer_id, brand=brand, model=model, year=year, plate_number=plate_number)
        vehicle.add_vehicle()
        return True, "Vehicle added successfully"


    @staticmethod
    def remove_vehicle(vehicle_id):
        vehicle_id = vehicle_id.strip()

        try:
            int_vehicle_id = int(vehicle_id)
            if int_vehicle_id <= 0:
                return False, "use positive number"
        except (ValueError, TypeError):
            return False, "Invalid id"

        vehicle = Vehicle()
        try:
            vehicle.remove_vehicle(vehicle_id=vehicle_id)
            return True, "vehicle removed successfully"
        except Error as e:
            if e.errno == 1451:
                return False, "This vehicle cannot be deleted because it is linked to an appointment or payment."
            return False,str(e)


    def edit_vehicle(self, vehicle_id):
        brand, model, year, plate_number, vehicle_id, customer_id = (self.brand.strip(), self.model.strip(), self.year,
                                                        self.plate_number.strip(), vehicle_id.strip(), self.customer_id.strip())

        if not re.fullmatch(r"^[a-zA-Z0-9_ ]{2,50}$", brand):
            return (False,
                    "use alphanumeric char between 2 and 50 char for brand")

        if not re.fullmatch(r"^[a-zA-Z0-9_ ]{1,50}$", model):
            return False, "use alphanumeric char between 1 and 50 char for model"

        if not re.fullmatch(r"^\d{2}\s[ب-ی]\s\d{3}\sایران\s\d{2}$", plate_number):
            return False, "Plate format must be like: 28 ب 444 ایران 12"

        try:
            year = int(year)
            if year < 1970 or year > 2026:
                return False, "Year must be between 1970 and 2100"
        except (ValueError, TypeError) as e:
            return False, "Year must be a number"

        try:
            int_vehicle_id = int(vehicle_id)
            if int_vehicle_id <= 0:
                return False, "use positive number"
        except (ValueError, TypeError):
            return False, "use positive number"

        try:
            int_customer_id = int(customer_id)
            if int_customer_id  <= 0:
                return False, "use positive number"
        except (ValueError, TypeError):
            return False, "user valid number"


        vehicle = Vehicle(brand=brand, model=model, year=year, plate_number=plate_number)
        vehicle.edit_vehicle(vehicle_id=vehicle_id)
        return True, "Vehicle edited successfully"

    @staticmethod
    def search_vehicle(vehicle_id):
        vehicle_id = vehicle_id.strip()

        try:
            vehicle_id = int(vehicle_id)

            if vehicle_id <= 0:
                return False, "Use positive number"

        except (ValueError, TypeError):
            return False, "Invalid ID"

        vehicle = Vehicle()

        result = vehicle.search_vehicle(vehicle_id)

        if result:
            return True, result

        return False, "Vehicle not found"

    @staticmethod
    def get_all_vehicles():
        try:
            vehicle = Vehicle()
            result = vehicle.get_all_vehicles()
            return result
        except Exception as e:
            print(e)

    def add_vehicle_return_id(self):
        """
        Adds a vehicle and returns its new vehicle_id
        :return: vehicle_id
        """
        vehicle = Vehicle(self.customer_id, self.brand, self.model, self.year, self.plate_number)
        vehicle_id = vehicle.add_vehicle_return_id()

        return vehicle_id

    def get_vehicle_id_by_plate(self):
        """
        Checks if this customer already owns that vehicle and prevents duplicate vehicles
        :return: vehicle_id or None
        """

        customer_id, plate_number = self.customer_id, self.plate_number.strip()

        vehicle = Vehicle(customer_id=customer_id, plate_number=plate_number)

        result = vehicle.find_vehicle_by_plate()

        if result:
            return result[0] # fetchone returns tuple we want the number

        return None


class AppointmentController :
    #appointment_id, customer_id, vehicle_id,date,status (pending, in progress, completed, cancelled)

    def __init__(self, customer_id="", vehicle_id="", appointment_date="", status="", service_id=""):
        self.customer_id = customer_id
        self.vehicle_id = vehicle_id
        self.appointment_date = appointment_date
        self.status = status
        self.service_id = service_id

    def add_appointment(self):

        customer_id, vehicle_id, appointment_date, status, service_id = (self.customer_id.strip(), self.vehicle_id.strip(),
                                            self.appointment_date.strip(), self.status.strip(), self.service_id)

        try:
            appointment_date = datetime.datetime.strptime(self.appointment_date, "%Y-%m-%d").date()
        except (ValueError, TypeError):
            return False, "Date format must be YYYY-MM-DD"

        try:
            customer_id = int(customer_id)
            if customer_id <= 0:
                return False, "use positive number"
        except (ValueError, TypeError):
            return False, "Invalid Customer ID"

        try:
            vehicle_id = int(vehicle_id)
            if vehicle_id <= 0:
                return False, "use positive number"
        except (ValueError, TypeError):
            return False, "Invalid Vehicle ID"

        if status not in ["Pending", "In Progress", "Completed","Cancelled"]:
            return False, "Appointment status must valid"


        appointment = Appointment(customer_id=customer_id, vehicle_id=vehicle_id, appointment_date=appointment_date,
                                  status=status,service_id=service_id)

        if appointment.appointment_exists():
            return False, "You already have this appointment booked."

        appointment.add_appointment()

        return True, "Appointment added successfully"



    def cancel_appointment(self,appointment_id):

        try:
            appointment_id = int(appointment_id)
            if appointment_id <= 0:
                return False, "use positive number"
        except (ValueError, TypeError):
            return False, "Invalid Appointment ID"

        try:
            appointment = Appointment()
            appointment.cancel_appointment(appointment_id=appointment_id)
            return True, "Appointment canceled successfully"

        except Error as e:
            if e.errno == 1452: # The values we are attempting to insert into the table are not present in the referencing (parent) table
                # (Trying to insert child without parent)
                return False, "Customer ID or Vehicle ID does not exist"
            else:
                return False, str(e)

    def edit_appointment(self, appointment_id):
        customer_id, vehicle_id, appointment_date, status, appointment_id = (self.customer_id.strip(),
            self.vehicle_id.strip(), self.appointment_date.strip(), self.status.strip(), appointment_id.strip())

        try:
            appointment_date = datetime.datetime.strptime(self.appointment_date, "%Y-%m-%d").date()
        except (ValueError, TypeError):
            return False, "Date format must be YYYY-MM-DD"

        try:
            customer_id = int(customer_id)
            if customer_id <= 0:
                return False, "use positive number"
        except (ValueError, TypeError):
            return False, "Invalid Customer ID"

        try:
            vehicle_id = int(vehicle_id)
            if vehicle_id <= 0:
                return False, "use positive number"
        except (ValueError, TypeError):
            return False, "Invalid Vehicle ID"

        if status not in ["Pending", "In Progress", "Completed", "Cancelled"]:
            return False, "Appointment status must valid"

        try:
            appointment_id = int(appointment_id)
            if appointment_id <= 0:
                return False, "use positive number"
        except (ValueError, TypeError):
            return False, "Invalid Appointment ID"

        appointment = Appointment(customer_id, vehicle_id, appointment_date, status)
        appointment.edit_appointment(appointment_id)

        return True, "Appointment edited successfully"

    @staticmethod
    def get_all_appointments():
        try:
            appointment = Appointment()
            result = appointment.get_all_appointments()
            return result
        except Exception as e:
            print(e)

    def update_status(self, appointment_id):

        status , appointment_id = self.status.strip(), appointment_id.strip()

        if status not in ["Pending", "In Progress", "Completed", "Cancelled"]:
            return False, "Appointment status must be valid"

        try:
            appointment_id = int(appointment_id)
            if appointment_id <= 0:
                return False, "Please select a status"
        except (ValueError, TypeError):
            return False, "Invalid Appointment ID"

        appointment = Appointment(status= status)
        appointment.update_status(appointment_id)
        return True, "Appointment status updated successfully"

    @staticmethod
    def search_appointment(appointment_id):

        appointment_id = appointment_id.strip()

        try:
            appointment_id = int(appointment_id)

            if appointment_id <= 0:
                return False, "Invalid ID"

        except (ValueError, TypeError):
            return False, "Invalid ID"

        appointment = Appointment()

        result = appointment.search_appointment(appointment_id=appointment_id)

        if result:
            return True, result

        return False, "Appointment not found"


    def book_appointment(self, name, phone, email, brand, model, year, plate_number, service_name, appointment_date):

        # ---------- Basic validation ----------

        if not name or not phone or not brand or not model or not year \
                or not plate_number or not service_name:
            return False, "Please fill all required fields"

        try:
            year = int(year)
            if year < 1970 or year > 2026:
                return False, "Year must be between 1970 and 2026"
        except (ValueError, TypeError):
            return False, "Year must be a number"

        # ---------- Validate service FIRST ----------

        service = ServiceController(service_name=service_name)

        service_id = service.get_service_id()

        if service_id is None:
            return False, "Please select a valid service from the list."

        # Creating customer
        customer = CustomerController(name=name, phone=phone, email=email)
        customer_id = customer.get_customer_id_by_phone()

        # if it finds it and None = False skips line 629 and uses customer_id ,if not call add_customer_return_id() to create them and get the new ID
        if customer_id is None:
            success, customer_id = customer.add_customer_return_id() # mysql creates customer_id

            if not success:
                return False, "Could not create customer"

        # Create vehicle
        vehicle = VehicleController(customer_id=customer_id, brand=brand, model=model, year=year, plate_number=plate_number)

        vehicle_id = vehicle.get_vehicle_id_by_plate()

        # call get_vehicle_id_by_plate() using customer_id , plate if the car isn't registered, call add_vehicle_return_id() to add it
        if vehicle_id is None:
            vehicle_id = vehicle.add_vehicle_return_id()

        # Create appointment
        appointment = Appointment(customer_id=customer_id, vehicle_id=vehicle_id, appointment_date=appointment_date,
                                  service_id=service_id, status="Pending")
        appointment.add_appointment()
        return True, "Appointment booked successfully."


    def get_customer_appointments(self, phone):
        """
        customer appointment table
        """

        appointment = Appointment()

        return appointment.get_customer_appointments(phone=phone)


class ServiceController :
    #service_id , service_name, price

    def __init__(self, service_name="", price=""):
        self.service_name = service_name
        self.price = price

    def add_service(self):

        service_name , price = self.service_name.strip(), self.price.strip()

        if not re.fullmatch(r"^[a-zA-Z_ ]{2,100}$", service_name):
            return False, "Service name must contain only letters"

        try:
            price = float(price)
            if price < 0.0:
                return False, "use positive number"
        except (ValueError, TypeError):
            return False, "user valid number"

        service = Service(service_name,price)
        service.add_service()
        return True, "Service added successfully"

    @staticmethod
    def remove_service(service_id):

        service_id = service_id.strip()

        try:
            service_id = int(service_id)
            if service_id <= 0:
                return False, "use positive number"
        except (ValueError, TypeError):
            return False, "Invalid service ID"

        service = Service()
        service.remove_service(service_id)
        return True, "Service removed successfully"

    def edit_service(self, service_id):
        service_name, price, service_id = self.service_name.strip(), self.price.strip(), service_id.strip()

        if not re.fullmatch(r"^[a-zA-Z_ ]{2,100}$", service_name):
            return False, "Service name must contain only letters"

        try:
            price = float(price)
            if price <= 0.0:
                return False, "use positive number"
        except (ValueError, TypeError):
            return False, "user valid number"

        try:
            service_id = int(service_id)
            if service_id <= 0:
                return False, "use positive number"
        except (ValueError, TypeError):
            return False, "Invalid service ID"

        service = Service(service_name=service_name, price=price)
        service.edit_service(service_id)
        return True, "Service edited successfully"


    def search_service(self):
        service_name = self.service_name.strip()

        if len(service_name) < 1:
            return False, "Enter a service name"

        service = Service(service_name=service_name)

        result = service.search_service()

        if result:
            return True, result

        return False, "No services found"


    @staticmethod
    def get_all_services():

        try:
            service = Service()
            result = service.get_all_services()
            return result
        except Exception as e:
            print(e)

    def get_service_id(self):
        """
        Converts a service name like "Oil Change" into its database id
        :return: service_id
        """

        service_name = self.service_name.strip()
        service = Service(service_name=service_name)

        result = service.get_service_id()

        if result:
            return result[0] # fetchone returns (3,) we want 3

        return None

    def get_all_service_names(self):
        """
        use it to just get back service names so we can use it in service name combobox
        :return: service_name
        """

        service = Service()
        rows = service.get_all_service_names()
        return [row[0] for row in rows] # bc it'll return tuple and [0] is service name





class PaymentController :
    #payment_id, appointment_id, total_price, payment_status

    def __init__(self, appointment_id="", total_price="", payment_status=""):
        self.appointment_id = appointment_id
        self.total_price = total_price
        self.payment_status = payment_status

    def add_payment(self):
        appointment_id, total_price, payment_status = self.appointment_id.strip(), self.total_price.strip(), self.payment_status.strip()

        try:
            appointment_id = int(appointment_id)
            if appointment_id <= 0:
                return False, "use positive number"
        except (ValueError, TypeError):
            return False, "Invalid Appointment ID"

        try:
            total_price = float(total_price)
            if total_price < 0.0:
                return False, "use positive number"
        except (ValueError, TypeError):
            return False, "user valid number"

        appointment = Appointment()


        payment = Payment(appointment_id=appointment_id, total_price=total_price, payment_status=payment_status)
        payment.add_payment()

        return True, "Payment added successfully"

    def edit_payment(self, payment_id):
        appointment_id, total_price, payment_status, payment_id = (self.appointment_id.strip(), self.total_price.strip(),
                                                                self.payment_status.strip() , payment_id.strip())

        try:
            appointment_id = int(appointment_id)
            if appointment_id <= 0:
                return False, "use positive number"
        except (ValueError, TypeError):
            return False, "Invalid Appointment ID"

        try:
            total_price = float(total_price)
            if total_price < 0.0:
                return False, "use positive number"
        except (ValueError, TypeError):
            return False, "user valid number"

        try:
            payment_id = int(payment_id)
            if payment_id <= 0:
                return False, "use positive number"
        except (ValueError, TypeError):
            return False, "Invalid payment ID"

        if payment_status not in ["Paid", "UnPaid"]:
            return False, "Appointment status  must valid"

        payment = Payment(appointment_id=appointment_id, total_price=total_price, payment_status=payment_status)
        payment.edit_payment(payment_id=payment_id)
        return True, "Payment edited successfully"

    @staticmethod
    def remove_payment(payment_id):
        payment_id = payment_id.strip()

        try:
            payment_id = int(payment_id)
            if payment_id <= 0:
                return False, "use positive number"
        except (ValueError, TypeError):
            return False, "Invalid payment ID"

        payment = Payment()
        payment.remove_payment(payment_id)
        return True, "Payment removed successfully"

    @staticmethod
    def search_payment(payment_id):
        payment_id = payment_id.strip()

        try:
            payment_id = int(payment_id)

            if payment_id <= 0:
                return False, "Use positive number"

        except (ValueError, TypeError):
            return False, "Invalid ID"

        payment = Payment()

        result = payment.search_payment(payment_id=payment_id)

        if result:
            return True, result

        return False, "No payments found"


    @staticmethod
    def get_all_payments():
        try:
            payment = Payment()
            result = payment.get_all_payments()
            return result
        except Exception as e:
            print(e)

    def get_customer_payments(self, phone):

        payment = Payment()

        return payment.get_customer_payments(phone)


    def mark_as_paid(self, payment_id):
        payment_status , payment_id =  self.payment_status.strip(), payment_id.strip()

        if payment_status not in ["Paid", "UnPaid"]:
            return False, "Payment status must be valid"

        try:
            payment_id = int(payment_id)
            if payment_id <= 0:
                return False, "use positive number"
        except (ValueError, TypeError):
            return False, "Invalid payment ID"

        payment = Payment(payment_status)
        payment.mark_as_paid(payment_id)
        return True, "Payment marked successfully"



class ReviewController:
    # review_id , customer_id, rating, comment, date

    def __init__(self, customer_id="", rating="", comment="", review_date=""):
        self.customer_id = customer_id
        self.rating = rating
        self.comment = comment
        self.review_date = review_date


    def add_review(self):

        customer_id, rating, comment = self.customer_id.strip(), self.rating.strip(), self.comment.strip()

        try:
            customer_id = int(customer_id)
            if customer_id <= 0:
                return False, "use positive number"
        except (ValueError, TypeError):
            return False, "Invalid customer ID"

        review_date = date.today()

        try:
            rating = int(rating)
            if rating < 1 or rating > 5:
                return False, "rating must be between 1 and 5"
        except (ValueError, TypeError):
            return False, "rating must be a number"

        if len(comment) < 3:
            return False, "comment must contain at least 3 characters"
        if len(comment) > 500:
            return False, "comment must be less than 500 characters"

        review = Review(customer_id=customer_id, rating=rating, comment=comment, review_date=review_date)
        review.add_review()
        return True, "Review added successfully"


    @staticmethod
    def remove_review(review_id):
        try:
            review_id = int(review_id)
            if review_id <= 0:
                return False, "use positive number"
        except (ValueError, TypeError):
            return False, "Invalid review ID"

        review = Review()
        review.remove_review(review_id=review_id)
        return True, "Review removed successfully"


    def edit_review(self, review_id):

        customer_id, rating, comment, review_id = (self.customer_id.strip(), self.rating.strip(), self.comment.strip()
                                                       ,review_id.strip())

        try:
            customer_id = int(customer_id)
            if customer_id <= 0:
                return False, "use positive number"
        except (ValueError, TypeError):
            return False, "Invalid customer ID"

        review_date = date.today()

        try:
            rating = int(rating)
            if rating < 1 or rating > 5:
                return False, "rating must be between 1 and 5"
        except (ValueError, TypeError):
            return False, "rating must be a number"

        if len(comment) < 3:
            return False, "comment must contain at least 3 characters"
        if len(comment) > 500:
            return False, "comment must be less than 500 characters"

        try:
            review_id = int(review_id)
            if review_id <= 0:
                return False, "use positive number"
        except (ValueError, TypeError):
            return False, "Invalid review ID"

        review = Review(customer_id=customer_id, rating=rating, comment=comment, review_date=review_date)
        review.edit_review(review_id=review_id)
        return True, "Review edited successfully"

    @staticmethod
    def get_all_reviews():
        try:
            reviews = Review()
            result = reviews.get_all_reviews()
            return result
        except Exception as e:
            print(e)

    def customer_add_review(self, phone, rating, comment):

        customer = CustomerController(phone=phone)

        customer_id = customer.get_customer_id_by_phone()

        if customer_id is None:
            return False, "Customer not found"

        review = Review(customer_id=customer_id, rating=rating, comment=comment, review_date=date.today())

        review.add_review()

        return True, "Review submitted successfully."


# user = UserController("sara","123","admin2")
# status, message = user.add_user()
# print(status)
# print(message)

# print(user.get_all_users())


# CustomerController(customer_id="11").remove_customer()
# customer_1 = CustomerController(customer_id="2")
# status, message = customer_1.remove_customer()
# print(status)
# print(message)
