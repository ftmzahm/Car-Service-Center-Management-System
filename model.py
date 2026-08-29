# Car Service Center Management
import mysql.connector
import os

class Database:
    def _connect(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv("MYSQL_PASSWORD"),
            database="car_service"
        )
        return db

class User(Database):
    #id,username,password,role
    def __init__(self, username="", password="", role="", user_id=""):
        self.username = username
        self.password = password
        self.role = role
        self.user_id = user_id

    def add_user(self):
        db = self._connect()
        cursor = db.cursor()

        query = "INSERT INTO car_service.users (username, password, role) VALUES (%s, %s, %s)"
        values = (self.username, self.password, self.role)
        cursor.execute(query, values)

        db.commit()
        cursor.close()
        db.close()

    def remove_user(self):
        db = self._connect()
        cursor = db.cursor()

        query = "delete from car_service.users where user_id = %s"
        value = (self.user_id, )
        cursor.execute(query, value)
        db.commit()
        cursor.close()
        db.close()

    def edit_user(self):
        db = self._connect()
        cursor = db.cursor()
        query = "update car_service.users set username = %s, password = %s, role = %s where user_id = %s"
        values = (self.username, self.password, self.role, self.user_id)

        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()

    def get_all_users(self):

        """ administration """

        db = self._connect()
        cursor = db.cursor()

        query = "select * from car_service.users"
        cursor.execute(query)

        results = cursor.fetchall()
        cursor.close()
        db.close()
        return results

    def login_user(self):

        """ authentication if a user with specific username and password exists """

        db = self._connect()
        cursor = db.cursor()

        query = "select * from car_service.users where username = %s and password = %s"
        values = (self.username, self.password)
        cursor.execute(query, values)
        result = cursor.fetchone()
        cursor.close()
        db.close()
        return result

    def search_user(self):
        db = self._connect()
        cursor = db.cursor()

        query = "select * from car_service.users where user_id = %s"
        value = (self.user_id, )

        cursor.execute(query, value)
        result = cursor.fetchone() #fetchone function retrieves only one row from the result set

        cursor.close()
        db.close()
        return result


class Customer(Database):
    #customer_id,name,phone,email

    def __init__(self, name="", phone="", email="", customer_id=""):
        self.name = name
        self.phone = phone
        self.email = email
        self.customer_id = customer_id

    def add_customer(self):
        db = self._connect()
        cursor = db.cursor()

        query = "insert into car_service.customers (name, phone, email) VALUES (%s, %s, %s)"
        values = (self.name, self.phone, self.email)

        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()

    def remove_customer(self):
        db = self._connect()
        cursor = db.cursor()

        query = "delete from car_service.customers where customer_id = %s"
        value = (self.customer_id, )

        cursor.execute(query, value)

        db.commit()
        cursor.close()
        db.close()

    def edit_customer(self):
        db = self._connect()
        cursor = db.cursor()

        query = "update car_service.customers set name = %s, phone = %s, email = %s where customer_id = %s"
        values = (self.name, self.phone, self.email, self.customer_id)

        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()

    def get_all_customers(self):
        db = self._connect()
        cursor = db.cursor()

        query = "select * from car_service.customers"
        cursor.execute(query)

        results = cursor.fetchall()
        cursor.close()

        db.close()
        return results

    def search_customer(self):
        db = self._connect()
        cursor = db.cursor()

        query = "select * from car_service.customers where customer_id = %s"
        value = (self.customer_id, )

        cursor.execute(query, value)
        result = cursor.fetchone() #fetchone function retrieves only one row from the result set

        cursor.close()
        db.close()
        return result

    def add_customer_return_id(self):
        """
        creates a new customer and returns the generated customer_id
        """
        db = self._connect()
        cursor = db.cursor()

        query = "INSERT INTO car_service.customers(name, phone, email)VALUES (%s, %s, %s) "
        values = (self.name, self.phone, self.email)

        cursor.execute(query, values)
        db.commit()
        customer_id = cursor.lastrowid  # This read-only property returns the value generated for an AUTO_INCREMENT
        cursor.close()
        db.close()

        return True, customer_id

    def find_customer_by_phone(self):
        db = self._connect()
        cursor = db.cursor()

        query = " SELECT customer_id FROM car_service.customers WHERE phone = %s "
        values = (self.phone,)
        cursor.execute(query, values)
        result = cursor.fetchone()

        cursor.close()
        db.close()

        return result

    def login_customer(self):
        db = self._connect()
        cursor = db.cursor()

        query = " SELECT customer_id, name, phone, email FROM customers WHERE name=%s AND phone=%s"
        values = (self.name, self.phone)

        cursor.execute(query, values)

        result = cursor.fetchone()

        cursor.close()
        db.close()

        return result

    def get_customer_info(self, phone):
        db = self._connect()
        cursor = db.cursor()

        query = "SELECT name, phone, email FROM customers WHERE phone = %s "

        cursor.execute(query, (phone,))
        result = cursor.fetchone()

        cursor.close()
        db.close()

        return result

class Vehicle(Database):
    # vehicle_id, customer_id, brand, model, plate_number,year

    def __init__(self,customer_id="" , brand="", model="", year="", plate_number=""):
        self.customer_id = customer_id
        self.brand = brand
        self.model = model
        self.year = year
        self.plate_number = plate_number



    def add_vehicle(self):
        db = self._connect()
        cursor = db.cursor()

        query = "insert into car_service.vehicles (customer_id, brand, model, year, plate_number ) VALUES (%s, %s, %s, %s, %s)"
        values = (self.customer_id, self.brand, self.model, self.year, self.plate_number )
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()

    def remove_vehicle(self, vehicle_id):
        db = self._connect()
        cursor = db.cursor()
        query = "delete from car_service.vehicles where vehicle_id = %s"
        values = (vehicle_id, )
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()


    def edit_vehicle(self, vehicle_id):
        db = self._connect()
        cursor = db.cursor()
        query = "update car_service.vehicles set brand = %s, model = %s, year = %s, plate_number = %s where vehicle_id = %s"
        values = (self.brand, self.model, self.year, self.plate_number , vehicle_id)

        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()

    def search_vehicle(self,vehicle_id):
        db = self._connect()
        cursor = db.cursor()

        query = "select * from car_service.vehicles where vehicle_id = %s"
        value = (vehicle_id, )

        cursor.execute(query, value)
        result = cursor.fetchone()  # fetchone function retrieves only one row from the result set

        cursor.close()
        db.close()
        return result


    def get_all_vehicles(self):
        db = self._connect()
        cursor = db.cursor()
        query = "select * from car_service.vehicles"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        db.close()
        return results

    def add_vehicle_return_id(self):
        db = self._connect()
        cursor = db.cursor()

        query = "insert into car_service.vehicles (customer_id, brand, model, year, plate_number ) VALUES (%s, %s, %s, %s, %s)"
        values = (self.customer_id, self.brand, self.model, self.year, self.plate_number)
        cursor.execute(query, values)
        db.commit()
        vehicle_id = cursor.lastrowid # This read-only property returns the value generated for an AUTO_INCREMENT
        cursor.close()
        db.close()

        return vehicle_id

    def find_vehicle_by_plate(self):
        """
        so the same vehicle with same plate number is not added
        """
        db = self._connect()
        cursor = db.cursor()

        query = "SELECT vehicle_id FROM vehicles WHERE customer_id = %s AND plate_number = %s"
        values = (self.customer_id, self.plate_number)
        cursor.execute(query, values)
        result = cursor.fetchone()

        cursor.close()
        db.close()

        return result



class Appointment(Database):
    #appointment_id, customer_id, vehicle_id,date,status (pending, in progress, completed, cancelled)

    def __init__(self, customer_id="", vehicle_id="", appointment_date="", status="", service_id=""):
        self.customer_id = customer_id
        self.vehicle_id = vehicle_id
        self.appointment_date = appointment_date
        self.status = status
        self.service_id = service_id

    def add_appointment(self):
        db = self._connect()
        cursor = db.cursor()

        query = "insert into car_service.appointments (vehicle_id, appointment_date, status, customer_id, service_id) VALUES (%s, %s, %s, %s, %s)"
        values = (self.vehicle_id, self.appointment_date, self.status, self.customer_id, self.service_id)
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()


    def cancel_appointment(self, appointment_id):
        db = self._connect()
        cursor = db.cursor()
        query = "update car_service.appointments set status = 'Cancelled' where appointment_id = %s"
        values = (appointment_id, )
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()

    def edit_appointment(self, appointment_id):
        db = self._connect()
        cursor = db.cursor()
        query = "update car_service.appointments set appointment_date = %s, status = %s, customer_id = %s where appointment_id = %s"
        values = (self.appointment_date, self.status, self.customer_id, appointment_id)
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()


    def get_all_appointments(self):
        db = self._connect()
        cursor = db.cursor()
        query = "select * from car_service.appointments"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        db.close()
        return results


    def update_status(self, appointment_id):
        db = self._connect()
        cursor = db.cursor()
        query = "update car_service.appointments set status = %s where appointment_id = %s"
        values = (self.status, appointment_id)

        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()

    def search_appointment(self, appointment_id):
        db = self._connect()
        cursor = db.cursor()

        query = "select * from car_service.appointments where appointment_id = %s "
        value = (appointment_id, )
        cursor.execute(query, value)
        result = cursor.fetchone()

        cursor.close()
        db.close()

        return result

    def get_customer_appointments(self, phone):
        """
        we used this function for appointment table part
        """
        db = self._connect()
        cursor = db.cursor()

        query = ("SELECT appointments.appointment_id, appointments.appointment_date, CONCAT (vehicles.brand, ' ', vehicles.model)"
                 " AS vehicle, services.service_name, appointments.status FROM appointments JOIN customers ON "
                 "appointments.customer_id = customers.customer_id JOIN services ON appointments.service_id = services.service_id"
                 " JOIN vehicles ON appointments.vehicle_id = vehicles.vehicle_id WHERE customers.phone = %s ORDER BY"
                 " appointments.appointment_date DESC ")

        values = (phone,)

        cursor.execute(query, values)
        result = cursor.fetchall()

        cursor.close()
        db.close()

        return result

    def appointment_exists(self):
        """
        so the same appointment won't get booked
        """
        db = self._connect()
        cursor = db.cursor()

        query = (" SELECT appointment_id FROM appointments WHERE customer_id = %s AND vehicle_id = %s AND "
                 "appointment_date = %s  AND service_id = %s AND status <> 'Cancelled' ") # <> Not Equal To, just like !=

        values = (self.customer_id, self.vehicle_id, self.appointment_date, self.service_id)

        cursor.execute(query, values)

        result = cursor.fetchone()

        cursor.close()
        db.close()

        return result

class Service(Database):
    #service_id , service_name, price

    def __init__(self, service_name="", price=""):
        self.service_name = service_name
        self.price = price

    def add_service(self):
        db = self._connect()
        cursor = db.cursor()
        query = "insert into car_service.services (service_name, price) VALUES (%s, %s)"
        values = (self.service_name, self.price)
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()


    def remove_service(self, service_id):
        db = self._connect()
        cursor = db.cursor()
        query = "delete from car_service.services where service_id = %s"
        values = (service_id, )
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()


    def edit_service(self, service_id):
        db = self._connect()
        cursor = db.cursor()
        query = "update car_service.services set service_name = %s, price = %s where service_id = %s"
        values = (self.service_name, self.price, service_id)
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()

    def search_service(self):
        db = self._connect()
        cursor = db.cursor()

        query = "select * from car_service.services where service_name LIKE %s"
        value = (f"%{self.service_name}%", )             # anything before OR service_name OR anything after

        cursor.execute(query, value)
        result = cursor.fetchall()  # fetchone function retrieves only one row from the result set

        cursor.close()
        db.close()
        return result

    def get_all_services(self):
        db = self._connect()
        cursor = db.cursor()
        query = "select * from car_service.services"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        db.close()
        return results

    def get_service_id(self):
        db = self._connect()
        cursor = db.cursor()

        query = " SELECT service_id FROM services WHERE service_name = %s "
        values = (self.service_name, )
        cursor.execute(query, values)
        result = cursor.fetchone()

        cursor.close()
        db.close()

        return result

    def get_all_service_names(self):
        """
        use it to just get back service names so we can use it in service name combobox
        :return: service_name
        """
        db = self._connect()
        cursor = db.cursor()

        cursor.execute("SELECT service_name FROM services ORDER BY service_name")

        rows = cursor.fetchall()

        cursor.close()
        db.close()

        return rows



class Payment(Database):
    #payment_id, appointment_id, total_price, payment_status

    def __init__(self, appointment_id="", total_price="", payment_status=""):
        self.appointment_id = appointment_id
        self.total_price = total_price
        self.payment_status = payment_status

    def add_payment(self):
        db = self._connect()
        cursor = db.cursor()
        query = "insert into car_service.payments (appointment_id, total_price, payment_status) VALUES (%s, %s, %s)"
        values = (self.appointment_id, self.total_price, self.payment_status)
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()

    def edit_payment(self, payment_id):
        db = self._connect()
        cursor = db.cursor()
        query = "update car_service.payments set appointment_id = %s , total_price = %s, payment_status = %s where payment_id = %s"
        values = (self.appointment_id, self.total_price, self.payment_status, payment_id)
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()

    def remove_payment(self, payment_id):
        db = self._connect()
        cursor = db.cursor()
        query = "delete from car_service.payments where payment_id = %s "
        values = (payment_id, )
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()

    def search_payment(self, payment_id):
        db = self._connect()
        cursor = db.cursor()

        query = "select * from car_service.payments where payment_id = %s"
        value = (payment_id, )

        cursor.execute(query, value)
        result = cursor.fetchone()

        cursor.close()
        db.close()
        return result


    def get_all_payments(self):
        db = self._connect()
        cursor = db.cursor()
        query = "select * from car_service.payments"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        db.close()
        return results

    def mark_as_paid(self, payment_id):
        db = self._connect()
        cursor = db.cursor()
        query = "update car_service.payments set payment_status = %s where payment_id = %s"
        values = (self.payment_status, payment_id )
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()

    def get_customer_payments(self, phone):
        db = self._connect()
        cursor = db.cursor()

        query = ("SELECT payments.payment_id, appointments.appointment_date, services.service_name, payments.total_price,"
                 " payments.payment_status FROM payments JOIN appointments ON payments.appointment_id = appointments.appointment_id"
                 "  JOIN customers ON appointments.customer_id = customers.customer_id JOIN services ON"
                 " appointments.service_id = services.service_id WHERE customers.phone = %s ORDER BY"
                 " appointments.appointment_date DESC")
        values = (phone,)
        cursor.execute(query, values)
        result = cursor.fetchall()

        cursor.close()
        db.close()

        return result


class Review(Database):
    # review_id , customer_id, rating, comment, date

    def __init__(self, customer_id="", rating="", comment="", review_date=""):
        self.customer_id = customer_id
        self.rating = rating
        self.comment = comment
        self.review_date = review_date


    def add_review(self):
        db = self._connect()
        cursor = db.cursor()
        query = "insert into car_service.reviews (customer_id, rating, comment, review_date) VALUES (%s, %s, %s, %s)"
        values = (self.customer_id, self.rating, self.comment, self.review_date)
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()


    def remove_review(self,review_id):
        db = self._connect()
        cursor = db.cursor()
        query = "delete from car_service.reviews where review_id = %s "
        values = (review_id, )
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()


    def edit_review(self, review_id):
        db = self._connect()
        cursor = db.cursor()
        query = "update car_service.reviews set  customer_id= %s, rating = %s , comment =%s, review_date = %s where review_id = %s"
        values = (self.customer_id, self.rating, self.comment, self.review_date, review_id)
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()


    def get_all_reviews(self):
        db = self._connect()
        cursor = db.cursor()
        query = "select * from car_service.reviews"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        db.close()
        return results





# customer = Customer("sara", "09122888", "shima@gmail.com", 3)
# customer.remove_customer()

# user = User(username="admin", password="admin321", role="admin", user_id=1)
# print(user.get_all_users())

# vehicle = Vehicle(2, "mazda","3","2015","44r55")
# vehicle.add_vehicle()

# appointment = Appointment("3","6","2018-10-11","in progress",)
# appointment.cancel_appointment(1)

# service = Service("brake pads change","1400")
# service.remove_service(1)

# payment = Payment("1","200","paid")
# payment.add_payment()

