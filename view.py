from controller import UserController, VehicleController, AppointmentController, CustomerController, ReviewController, PaymentController, ServiceController
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from PIL import Image, ImageTk
from tkinter import END


win = tk.Tk()
win.title("Car Service Center")
win.geometry("900x600")
win.resizable(False, False)
win.iconbitmap("images\\car_ico.ico")

#frames

main_frame =tk.Frame(win)

signup_frame = tk.Frame(win)

admin_login_frame = tk.Frame(win)
admin_frame = tk.Frame(win)

customer_frame = tk.Frame(win)



for frame in (main_frame, signup_frame, admin_login_frame, customer_frame, admin_frame):
    frame.place(x=0, y=0, relwidth=1, relheight=1)
# =============================================================================================
#Helper functions

def show_frame(frame):
    frame.tkraise()

show_frame(main_frame)

def move_next(event, current_entry, next_entry, max_length):
    """
    Move to the next Entry only when typing, not when deleting.
    """

    # Ignore Backspace/Delete keys
    if event.keysym in ("BackSpace", "Delete"):
        return

    text = current_entry.get()

    if len(text) > max_length:
        current_entry.delete(max_length, END)

    if len(current_entry.get()) == max_length:
        next_entry.focus_set()


def move_previous(event, current_entry, previous_entry):
    """
    If Backspace is pressed while the current Entry is empty,
    move the cursor back to the previous Entry.
    """
    if event.keysym == "BackSpace" and current_entry.get() == "":
        previous_entry.focus_set()
        previous_entry.icursor(END)

#colors
NAVY = "#0F172A"
TEXT = "#F8FAFC"
CARD = "#1E293B"
ACCENT = "#38BDF8"
label_color = "#bdb9b1"
button_color= "#96abc5"
back_blue = "#3d5da9"

#fonts
my_font = ("Segoe UI", 12)
text_font = ("Segoe UI", 11)
back_btn_font = ("Segoe UI",12,"bold")
title_font = ("Segoe UI", 24, "bold")
count_font = ("Segoe UI", 28, "bold")
times_font = ("times new roman",18,"bold")

main_frame.config(bg=NAVY)
signup_frame.config(bg=NAVY)
admin_login_frame.config(bg=NAVY)
admin_frame.config(bg=NAVY)
customer_frame.config(bg=NAVY)

logged_in_customer = {}

###################################################################################################################################
############################################# LOGIN WINDOW (FIRST PAGE) ###########################################################
###################################################################################################################################

#CUSTOMER BOOK APPOINTMENT SHOW

customer_book_appointment_frame = tk.Frame(customer_frame,bg=NAVY)
customer_book_appointment_frame.place(x=240, y=60, width= 710, height=560)

def open_customer_booking():

    global logged_in_customer

    show_frame(customer_frame)
    customer_book_appointment_frame.tkraise()

    customer_name_entry.delete(0, END)
    customer_phone_entry.delete(0, END)
    customer_email_entry.delete(0, END)

    customer_name_entry.insert(0, logged_in_customer["name"])
    customer_phone_entry.insert(0, logged_in_customer["phone"])
    customer_email_entry.insert(0, logged_in_customer["email"])


def login_click():
    """
    checks if customer name and phone already exist
    """
    global logged_in_customer

    name = login_name_entry.get()
    phone_number = login_phone_entry.get()

    customer = CustomerController(name=name, phone=phone_number)

    success, result = customer.login_customer()

    if success:
        logged_in_customer = result

        open_customer_booking()

        customer_update_appointment_table(logged_in_customer["phone"])
        customer_update_payment_table(logged_in_customer["phone"])
    else:
        msg.showerror("Error", result)


    login_name_entry.delete(0, END)
    login_phone_entry.delete(0, END)

# car service title
title_lbl = tk.Label(main_frame,text="CAR SERVICE CENTER",font=("Segoe UI", 24, "bold"),bg=NAVY,fg="white")
title_lbl.place(x=280, y=30)

subtitle = tk.Label(main_frame,text="Vehicle Maintenance & Repair Management",
                    font=("Segoe UI", 10),bg="#0F172A",fg="#94A3B8")
subtitle.place(x=320, y=90)

#User labels

login_name_lbl = tk.Label(main_frame, text="Name", font=my_font,bg=NAVY,fg=TEXT)
login_name_lbl.place(x=40, y=230)
login_phone_lbl = tk.Label(main_frame, text="Phone Number", font=my_font, bg=NAVY, fg=TEXT)
login_phone_lbl.place(x=40, y=280)


#User entries

# relief="flat" removes the entries border
# using a Canvas as an underline with height 2

login_name_entry = tk.Entry(main_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat" ,font=text_font, width=24)
login_name_entry.place(x=180, y=228)
login_name_line = tk.Canvas(main_frame, bg=label_color, width=200, height=2.0, highlightthickness=0)
login_name_line.place(x=180, y=254)

login_phone_entry = tk.Entry(main_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat" ,font=text_font, width=24)
login_phone_entry.place(x=180, y=278)
login_name_line = tk.Canvas(main_frame, bg=label_color, width=200, height=2.0, highlightthickness=0)
login_name_line.place(x=180, y=304)


#Login button

login_img = ImageTk.PhotoImage(file="images\\login1.png")

login_button_label = tk.Button(main_frame, image=login_img, bg='#98a65d', cursor="hand2",
                borderwidth=0, background=NAVY, activebackground=NAVY, command=login_click)
login_button_label.place(x= 90, y= 360)

login_back_btn = tk.Button(
    customer_frame,text="← Back",bg=NAVY,fg=TEXT,activebackground=NAVY,activeforeground="white",
    borderwidth=0,cursor="hand2",font=back_btn_font, command=lambda :show_frame(main_frame))
login_back_btn.place(x=20, y=550)

#admin login button
admin_img = ImageTk.PhotoImage(file="images\\adminb.png")

admin_button_label = tk.Button(main_frame, image=admin_img, bg='#98a65d', cursor="hand2",
                borderwidth=0, background=NAVY, activebackground=NAVY, command=lambda :show_frame(admin_login_frame))
admin_button_label.place(x= 134, y= 500)

#signup button
signup_label = tk.Label(main_frame, text='No account yet?', font=text_font,relief="flat", borderwidth=0, background=NAVY, fg='white')
signup_label.place(x=120, y=420)

main_signup_img = ImageTk.PhotoImage(file='images\\register.png')
main_signup_button_label = tk.Button(main_frame, image=main_signup_img, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background=NAVY, activebackground=NAVY, command=lambda :show_frame(signup_frame))
main_signup_button_label.place(x=235, y=420, width=111, height=35)

signup_back_btn = tk.Button(
    signup_frame,text="← Back",bg=NAVY,fg=TEXT,activebackground=NAVY,activeforeground="white",
    borderwidth=0,cursor="hand2",font=back_btn_font, command=lambda :show_frame(main_frame))
signup_back_btn.place(x=20, y=550)

"""
style = ttk.Style()

style.theme_use("clam")

style.configure("Custom.TButton",font=("Segoe UI", 11, "bold"),padding=8)
ttk.Button(main_frame,text="Customer Portal",style="Custom.TButton")
"""


#login picture

login_pic = Image.open("images\\car4.png")
photo = ImageTk.PhotoImage(login_pic)  # converting PIL image to Tkinter image
login_pic = tk.Label(main_frame, image=photo, bg=NAVY)   #Creates a widget to show image
login_pic.image = photo       #keeps a reference to the image so python won't delete it
login_pic.place(x=450, y=160 )



###############################################################################################################################################################
###################################################################### SIGN UP PAGE ###########################################################################
###############################################################################################################################################################

def clear_signup():
    signup_name_entry.delete(0, END)
    signup_phone_entry.delete(0, END)
    signup_email_entry.delete(0, END)

def signup_click():
    name = signup_name_entry.get()
    phone = signup_phone_entry.get()
    email = signup_email_entry.get()

    customer = CustomerController(name,phone,email)
    status, message = customer.add_customer()

    if status:
        msg.showinfo("Success", "Successfully registered")
        show_frame(main_frame)
        clear_signup()
    else:
        msg.showerror("Error", message)


#SIGN UP PIC
login_pic = Image.open("images\\hyy.png")
photo = ImageTk.PhotoImage(login_pic)
login_pic = tk.Label(signup_frame, image=photo, bg=NAVY)
login_pic.image = photo
login_pic.place(x=380, y=50 )


# car service title

title_lbl = tk.Label(signup_frame,text="SIGN UP",font= title_font,bg=NAVY,fg="white")
title_lbl.place(x=390, y=170)


#User labels

signup_name_lbl = tk.Label(signup_frame, text="Name", font=my_font,bg=NAVY,fg=TEXT)
signup_name_lbl.place(x=280, y=300)
signup_phone_lbl = tk.Label(signup_frame, text="Phone Number", font=my_font, bg=NAVY, fg=TEXT)
signup_phone_lbl.place(x=280, y=350)
signup_email_lbl = tk.Label(signup_frame, text="Email", font=my_font, bg=NAVY, fg=TEXT)
signup_email_lbl.place(x=280, y=400)

#User entries

signup_name_entry = tk.Entry(signup_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat" ,font=text_font, width=24)
signup_name_entry.place(x=430, y=298)
signup_name_line = tk.Canvas(signup_frame, bg=label_color, width=200, height=2.0, highlightthickness=0)
signup_name_line.place(x=430, y=324)

signup_phone_entry = tk.Entry(signup_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat" ,font=text_font, width=24)
signup_phone_entry.place(x=430, y=348)
signup_phone_line = tk.Canvas(signup_frame, bg=label_color, width=200, height=2.0, highlightthickness=0)
signup_phone_line.place(x=430, y=374)


signup_email_entry = tk.Entry(signup_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat" ,font=text_font, width=24)
signup_email_entry.place(x=430, y=398)
signup_phone_line = tk.Canvas(signup_frame, bg=label_color, width=200, height=2.0, highlightthickness=0)
signup_phone_line.place(x=430, y=424)

# SIGN UP BUTTON
signup_img = ImageTk.PhotoImage(file='images\\signup1.png')
signup_button_label = tk.Button(signup_frame, image=signup_img, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background=NAVY, activebackground=NAVY, command=signup_click)
signup_button_label.place(x= 330, y= 490)

#################################################################################################################################################################
######################################################################## ADMIN LOGIN ############################################################################
#################################################################################################################################################################

# functions

def clear_admin_login():
    admin_login_username_entry.delete(0, END)
    admin_login_password_entry.delete(0, END)

############# change login admin to this func
def admin_login():

    login_username = admin_login_username_entry.get().strip()
    login_password = admin_login_password_entry.get().strip()
    # login_role = admin_role.get()

    controller = UserController(username=login_username,password=login_password)

    status, result = controller.login_user()

    if status:
        #
        # db_role = result[3]
        #
        # if db_role == login_role:

        msg.showinfo("Success", "Login successful")
        show_frame(admin_frame)
        update_dashboard()
        show_frame(admin_main_frame)
        clear_admin_login()
        return

    else:
        # msg.showerror("Error","Wrong role selected")
        # return

        msg.showerror("Error","Invalid username or password")
        return
# ============= SHOW/ HIDE PASSWORD ==============


show_img = Image.open("images\\show.png").resize((25, 25))
show_photo = ImageTk.PhotoImage(show_img)

# Hide image
hide_img = Image.open("images\\hide.png").resize((25, 25))
hide_photo = ImageTk.PhotoImage(hide_img)

password_visible = False  # we call this a flag ,and it's just a variable that stores True or False

def toggle_password():
    """
    if the password is hidden, it becomes visible and the button icon
    changes to the 'hide' icon

    if the password is visible, it becomes hidden again and the button
    icon changes back to the 'show' icon
    """
    global password_visible

    if password_visible:
        admin_login_password_entry.config(show="*")
        admin_toggle_button.config(image=show_photo)
        password_visible = False # updating the flag value
    else:
        admin_login_password_entry.config(show="")
        admin_toggle_button.config(image=hide_photo)
        password_visible = True


admin_toggle_button = tk.Button(admin_login_frame,image=show_photo,bg=NAVY,activebackground=NAVY,borderwidth=0,
                                cursor="hand2",command=toggle_password)

admin_toggle_button.place(x=655, y=351)




# car service title

admin_login_title_lbl = tk.Label(admin_login_frame,text="Admin Panel",font=title_font,bg=NAVY,fg="white")
admin_login_title_lbl.place(x=350, y=80)

#User labels

admin_login_username_lbl = tk.Label(admin_login_frame, text="Username", font=my_font,bg=NAVY,fg=TEXT)
admin_login_username_lbl.place(x=280, y=250)
admin_login_password_lbl = tk.Label(admin_login_frame, text="Password", font=my_font, bg=NAVY, fg=TEXT)
admin_login_password_lbl.place(x=280, y=340)

# admin_login_role_lbl = tk.Label(admin_login_frame, text="Role", font=my_font, bg=NAVY, fg=TEXT)
# admin_login_role_lbl.place(x=280, y=374)

#User entries

admin_login_username_entry = tk.Entry(admin_login_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat" ,font=text_font, width=24)
admin_login_username_entry.place(x=430, y=248)
admin_login_username_line = tk.Canvas(admin_login_frame, bg=label_color, width=200, height=2.0, highlightthickness=0)
admin_login_username_line.place(x=430, y=274)
# ==========
admin_login_password_entry = tk.Entry(admin_login_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=24, show="*")
admin_login_password_entry.place(x=430, y=338)
admin_login_password_line = tk.Canvas(admin_login_frame, bg=label_color, width=200, height=2.0, highlightthickness=0)
admin_login_password_line.place(x=430, y=364)

# ==========
# drop down option for roles
# admin_role = ttk.Combobox(
#     admin_login_frame,
#     values=["Admin", "Mechanic", "Employee"],
#     state="readonly",width=26, font = ("Segoe UI", 10), justify="center")
#
# admin_role.set("Choose Your Role")   # set it to a default value (without this even with an option they should click it again)
# admin_role.place(x=428, y=376)


# admin panel BUTTON
admin_login_img = ImageTk.PhotoImage(file='images\\login1.png')
admin_login_button_label = tk.Button(admin_login_frame, image=admin_login_img, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background=NAVY, activebackground=NAVY, command=admin_login)
admin_login_button_label.place(x= 340, y= 470)

# ADMIN LOGIN BACK BUTTON

admin_login_back_btn = tk.Button(
    admin_login_frame,text="← Back",bg=NAVY,fg=TEXT,activebackground=NAVY,activeforeground="white",
    borderwidth=0,cursor="hand2",font=back_btn_font, command=lambda :show_frame(main_frame))
admin_login_back_btn.place(x=20, y=550)

#############################################################################################################################################################################
############################################################## ADMIN PAGE (MAIN controller PAGE) ############################################################################
#############################################################################################################################################################################

"""
 ADMIN DASHBOARD

 Customers
 Vehicles
 Appointments
 Services
 Payments
 Reviews

 [Logout]
"""
#frames
admin_sidebar = tk.Frame(admin_frame,bg="white")
admin_sidebar.place(x=0, y=0, width= 190, height=600)

admin_customer_frame = tk.Frame(admin_frame,bg=NAVY)
admin_customer_frame.place(x=190, y=60, width= 710, height=560)

admin_vehicle_frame = tk.Frame(admin_frame,bg=NAVY)
admin_vehicle_frame.place(x=190, y=60, width= 710, height=560)

admin_appointment_frame = tk.Frame(admin_frame,bg=NAVY)
admin_appointment_frame.place(x=190, y=60, width= 710, height=560)

admin_service_frame = tk.Frame(admin_frame,bg=NAVY)
admin_service_frame.place(x=190, y=60, width= 710, height=560)

admin_payment_frame = tk.Frame(admin_frame,bg=NAVY)
admin_payment_frame.place(x=190, y=60, width= 710, height=560)

admin_review_frame = tk.Frame(admin_frame,bg=NAVY)
admin_review_frame.place(x=190, y=60, width= 710, height=560)

admin_main_frame = tk.Frame(admin_frame,bg=NAVY)
admin_main_frame.place(x=190, y=60, width= 710, height=560)

admin_user_frame = tk.Frame(admin_frame,bg=NAVY)
admin_user_frame.place(x=190, y=60, width= 710, height=560)



#title of page
admin_title = tk.Label(admin_frame, text="Admin Management Dashboard", bg=back_blue, fg="black", font = ("times new roman",30,"bold"))
admin_title.place(x=0, y=0, relwidth=1)



# ================================================================================================================================  SIDEBAR BUTTONS  ====================================================================================================================================================================

admin_menu = tk.Label(admin_sidebar, text="MENU", font =times_font , bg=back_blue, fg="black")
admin_menu.place(x=0, y=60, relwidth=1, height=40)

# ============================================================================================================================================
# CUSTOMER SIDEBAR BUTTON
admin_customer_icon = Image.open("images\\customer.png")
admin_customer_icon = admin_customer_icon.resize((40, 40))

photo = ImageTk.PhotoImage(admin_customer_icon)

admin_customer_button = tk.Button(admin_sidebar,text="Customers", image=photo, compound="left",
    anchor="w", # Aligns content to the left instead of centered
    padx=15, font=back_btn_font, bg="white", fg=NAVY, activebackground="white",relief="flat",borderwidth=0,
                                  command=lambda:show_frame(admin_customer_frame))

admin_customer_button.image = photo
admin_customer_button.place(x=4, y=120)


# =============================================================================================================================================

# VEHICLES SIDEBAR BUTTON
admin_vehicle_icon = Image.open("images\\vehicle.png")
admin_vehicle_icon = admin_vehicle_icon.resize((40, 40))

photo = ImageTk.PhotoImage(admin_vehicle_icon)

admin_vehicle_button = tk.Button(admin_sidebar,text="Vehicles", image=photo, compound="left",
    anchor="w", # Aligns content to the left instead of centered
    padx=15, font=back_btn_font, bg="white", fg=NAVY, activebackground="white",relief="flat",borderwidth=0,
                                 command=lambda:show_frame(admin_vehicle_frame))

admin_vehicle_button.image = photo
admin_vehicle_button.place(x=5, y=175)

# =============================================================================================================================================

# APPOINTMENTS SIDEBAR BUTTON
admin_appointment_icon = Image.open("images\\appointment.png")
admin_appointment_icon = admin_appointment_icon.resize((40, 40))

photo = ImageTk.PhotoImage(admin_appointment_icon)

admin_appointment_button = tk.Button(admin_sidebar,text="Appointments", image=photo, compound="left",
    anchor="w", # Aligns content to the left instead of centered
    padx=15, font=back_btn_font, bg="white", fg=NAVY, activebackground="white",relief="flat",borderwidth=0,
                                     command=lambda:show_frame(admin_appointment_frame))

admin_appointment_button.image = photo
admin_appointment_button.place(x=5, y=235)

# =============================================================================================================================================

# SERVICES SIDEBAR BUTTON
admin_service_icon = Image.open("images\\service.png")
admin_service_icon = admin_service_icon.resize((40, 40))

photo = ImageTk.PhotoImage(admin_service_icon)

admin_service_button = tk.Button(admin_sidebar,text="Services", image=photo, compound="left",
    anchor="w", # Aligns content to the left instead of centered
    padx=15, font=back_btn_font, bg="white", fg=NAVY, activebackground="white",relief="flat",borderwidth=0,
                                 command=lambda:show_frame(admin_service_frame))

admin_service_button.image = photo
admin_service_button.place(x=5, y=295)

# =============================================================================================================================================

# PAYMENTS SIDEBAR BUTTON
admin_payment_icon = Image.open("images\\payment.png")
admin_payment_icon = admin_payment_icon.resize((40, 40))

photo = ImageTk.PhotoImage(admin_payment_icon)

admin_payment_button = tk.Button(admin_sidebar,text="Payments", image=photo, compound="left",
    anchor="w", # Aligns content to the left instead of centered
    padx=15, font=back_btn_font, bg="white", fg=NAVY, activebackground="white",relief="flat",borderwidth=0,
                                 command=lambda:show_frame(admin_payment_frame))

admin_payment_button.image = photo
admin_payment_button.place(x=5, y=355)

# =============================================================================================================================================

# REVIEWS SIDEBAR BUTTON
admin_review_icon = Image.open("images\\rating.png")
admin_review_icon = admin_review_icon.resize((40, 40))

photo = ImageTk.PhotoImage(admin_review_icon)

admin_review_button = tk.Button(admin_sidebar,text="Reviews", image=photo, compound="left",
    anchor="w", # Aligns content to the left instead of centered
    padx=15, font=back_btn_font, bg="white", fg=NAVY, activebackground="white",relief="flat",borderwidth=0,
                                command=lambda:show_frame(admin_review_frame))

admin_review_button.image = photo
admin_review_button.place(x=5, y=415)


# =============================================================================================================================================

# USER SIDEBAR BUTTON
admin_user_icon = Image.open("images\\users.png")
admin_user_icon = admin_user_icon.resize((40, 40))

photo = ImageTk.PhotoImage(admin_user_icon)

admin_user_button = tk.Button(admin_sidebar,text="Users", image=photo, compound="left",
    anchor="w", # Aligns content to the left instead of centered
    padx=15, font=back_btn_font, bg="white", fg=NAVY, activebackground="white",relief="flat",borderwidth=0,
                              command=lambda:show_frame(admin_user_frame))

admin_user_button.image = photo
admin_user_button.place(x=5, y=475)


# =============================================================================================================================================

# EXIT SIDEBAR BUTTON
admin_exit_icon = Image.open("images\\exit.png")
admin_exit_icon = admin_exit_icon.resize((40, 40))

photo = ImageTk.PhotoImage(admin_exit_icon)

admin_exit_button = tk.Button(admin_sidebar,text="EXIT", image=photo, compound="left",
    anchor="w", # Aligns content to the left instead of centered
    padx=15, font=back_btn_font, bg="white", fg=NAVY, activebackground="white",relief="flat",borderwidth=0,
                              command= lambda: show_frame(admin_login_frame))

admin_exit_button.image = photo
admin_exit_button.place(x=5, y=540)


# =============================================================================================================== MAIN ADMIN CONTROL PANEL PAGE  ==========================================================================================================================================================

customer_card = tk.Frame(admin_main_frame, bg = back_blue)
customer_card.place(x=30, y=190, width=180, height=120)

vehicle_card=tk.Frame(admin_main_frame, bg = back_blue)
vehicle_card.place(x=265, y=190, width=180, height=120)

appointment_card=tk.Frame(admin_main_frame, bg = back_blue)
appointment_card.place(x=500, y=190, width=180, height=120)

def update_dashboard():

    customer = CustomerController()
    vehicle = VehicleController()
    appointment = AppointmentController()
    customer_count = len(customer.get_all_customers())
    vehicle_count = len(vehicle.get_all_vehicles())
    appointment_count = len(appointment.get_all_appointments())

    customer_count_lbl.config(text=str(customer_count))
    vehicle_count_lbl.config(text=str(vehicle_count))
    appointment_count_lbl.config(text=str(appointment_count))



tk.Label(customer_card, text="Customers", bg=back_blue, fg="black", font=times_font).pack(pady=10)
customer_count_lbl = tk.Label(customer_card, text="0",  bg=back_blue, fg=ACCENT, font=count_font)
customer_count_lbl.pack()


tk.Label(vehicle_card, text="Vehicles", bg=back_blue, fg="black", font=times_font).pack(pady=10)
vehicle_count_lbl = tk.Label(vehicle_card, text="0",  bg=back_blue, fg=ACCENT, font=count_font)
vehicle_count_lbl.pack()


tk.Label(appointment_card, text="Appointments", bg=back_blue, fg="black", font=times_font).pack(pady=10)
appointment_count_lbl = tk.Label(appointment_card, text="0",  bg=back_blue, fg=ACCENT, font=count_font)
appointment_count_lbl.pack()



# =============================================================================================================== ADMIN CUSTOMER PART  ==========================================================================================================================================================

admin_customer_top_lbl = tk.Label(admin_customer_frame, text="Customer Management", bg="white", fg="black" , font = ("times new roman",15))
admin_customer_top_lbl.place(x=0, y=0, width= 710, height=23)

# =========================================================================================================== ADMIN CUSTOMER FUNCTIONS  ==========================================================================================================================================================

def admin_update_customer_table():
    for item in admin_customer_table.get_children():
        admin_customer_table.delete(item)
    user = CustomerController
    users = user.get_all_customers()
    for user in users:
        admin_customer_table.insert("","end", values=user)


def on_select_admin_customer_table(event):
    select_item = admin_customer_table.focus()
    if not select_item:
        return
    customer_values = admin_customer_table.item(select_item,"values")
    if not customer_values:
        return
    admin_customer_id_entry.delete(0,END)
    admin_customer_id_entry.insert(0,customer_values[0])

    admin_customer_name_entry.delete(0,END)
    admin_customer_name_entry.insert(0,customer_values[1])

    admin_customer_phone_entry.delete(0,END)
    admin_customer_phone_entry.insert(0,customer_values[2])

    admin_customer_email_entry.delete(0, END)
    admin_customer_email_entry.insert(0, customer_values[3])



def admin_customer_save_click():
    name = admin_customer_name_entry.get()
    phone = admin_customer_phone_entry.get()
    email = admin_customer_email_entry.get()

    if name == "" or phone == "" or email == "":
        msg.showerror("Error", "All fields are required")
        return

    customer = CustomerController(name, phone, email)
    status,message = customer.add_customer()

    if status:
        msg.showinfo("Saved", message)
        admin_update_customer_table()
        update_dashboard()
    else:
        msg.showerror("Error", message)

    admin_customer_name_entry.delete(0,END)
    admin_customer_phone_entry.delete(0,END)
    admin_customer_email_entry.delete(0,END)


def admin_customer_remove_click():
    admin_customer_id = admin_customer_id_entry.get()

    admin_customer = CustomerController(customer_id=admin_customer_id)
    status,message = admin_customer.remove_customer()

    if status:
        msg.showinfo("Removed", message)
        admin_update_customer_table()
        update_dashboard()
    else:
        msg.showerror("Error", message)

    admin_customer_id_entry.delete(0,END)

def admin_customer_clear_click():

    admin_customer_id_entry.delete(0, END)
    admin_customer_name_entry.delete(0, END)
    admin_customer_phone_entry.delete(0, END)
    admin_customer_email_entry.delete(0, END)

def admin_customer_search_click():

    admin_customer_id = admin_customer_search_ent.get()

    admin_customer = CustomerController(customer_id=admin_customer_id)
    status, result = admin_customer.search_customer() # tuple of records

    if status:
        admin_customer_table.delete(*admin_customer_table.get_children())
        admin_customer_table.insert("", "end", values=result)

    else :
            msg.showerror("Error", "No records were found")
def admin_customer_show_click():

    customer = CustomerController()
    results = customer.get_all_customers()
    admin_customer_table.delete(*admin_customer_table.get_children())
    for row in results:
        admin_customer_table.insert("", "end", values=row)

def admin_customer_update_click():
    admin_customer_id = admin_customer_id_entry.get()
    name = admin_customer_name_entry.get()
    phone = admin_customer_phone_entry.get()
    email = admin_customer_email_entry.get()

    customer = CustomerController(name, phone, email, admin_customer_id)
    status , message = customer.edit_customer()

    if status:
        msg.showinfo("Data got Updated", message)
        admin_update_customer_table()
    else:
        msg.showerror("Error", message)

    admin_customer_id_entry.delete(0,END)
    admin_customer_name_entry.delete(0,END)
    admin_customer_phone_entry.delete(0,END)
    admin_customer_email_entry.delete(0,END)



# search part
admin_customer_search_lbl = tk.Label(admin_customer_frame, text="Search by Customer id :", font=text_font , bg=NAVY, fg="white")
admin_customer_search_lbl.place(x=15, y=130)
admin_customer_search_ent = tk.Entry(admin_customer_frame, width=8, bg="white", font=text_font)
admin_customer_search_ent.place(x=185, y=132)

admin_customer_search_btn = tk.Button(admin_customer_frame, text="Search" , font=text_font, bg=button_color ,activebackground=button_color,
                                      command=admin_customer_search_click)
admin_customer_search_btn.place(x=280, y=127)

admin_customer_show_btn = tk.Button(admin_customer_frame, text="Show All", font=text_font, bg=button_color,activebackground=button_color ,
                                    command=admin_customer_show_click)
admin_customer_show_btn.place(x=356, y=127)


# ================================================================= ADMIN CUSTOMER TABLE  ==========================================================


admin_customer_table = ttk.Treeview(admin_customer_frame,columns=(1,2,3,4),show="headings")
admin_customer_table.heading(1, text="Customer_id")
admin_customer_table.heading(2, text="Name")
admin_customer_table.heading(3, text="Phone")
admin_customer_table.heading(4, text="Email")


admin_customer_table.column(1, width=90)
admin_customer_table.column(2, width=90)
admin_customer_table.column(3, width=110)
admin_customer_table.column(4, width=120)

admin_customer_table.place(x=15,y=180)

admin_update_customer_table()
admin_customer_table.bind("<<TreeviewSelect>>", on_select_admin_customer_table)


customer_scroll_y = ttk.Scrollbar(admin_customer_frame,orient="vertical",command=admin_customer_table.yview)

customer_scroll_y.place(x=417, y=180, height=225)

admin_customer_table.configure(yscrollcommand=customer_scroll_y.set)


# ============================================================= ADMIN CUSTOMER labels and entries ==========================================================

#Customer labels

admin_customer_id_lbl = tk.Label(admin_customer_frame, text="Customer id", font=my_font, bg=NAVY, fg=TEXT)
admin_customer_id_lbl.place(x=440, y=175)
admin_customer_name_lbl = tk.Label(admin_customer_frame, text="Name", font=my_font,bg=NAVY,fg=TEXT)
admin_customer_name_lbl.place(x=440, y=235)
admin_customer_phone_lbl = tk.Label(admin_customer_frame, text="Phone Number", font=my_font, bg=NAVY, fg=TEXT)
admin_customer_phone_lbl.place(x=440, y=295)
admin_customer_email_lbl = tk.Label(admin_customer_frame, text="Email", font=my_font, bg=NAVY, fg=TEXT)
admin_customer_email_lbl.place(x=440, y=355)

#customer entries
admin_customer_id_line = tk.Canvas(admin_customer_frame, bg=label_color, width=120, height=2.0, highlightthickness=0)
admin_customer_id_line.place(x=565, y=201)

admin_customer_id_entry = tk.Entry(admin_customer_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=13)
admin_customer_id_entry.place(x=565, y=175)

admin_customer_name_line = tk.Canvas(admin_customer_frame, bg=label_color, width=120, height=2.0, highlightthickness=0)
admin_customer_name_line.place(x=565, y=261)

admin_customer_name_entry = tk.Entry(admin_customer_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=13)
admin_customer_name_entry.place(x=565, y=235)

admin_customer_phone_line = tk.Canvas(admin_customer_frame, bg=label_color, width=120, height=2.0, highlightthickness=0)
admin_customer_phone_line.place(x=565, y=321)

admin_customer_phone_entry = tk.Entry(admin_customer_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=13)
admin_customer_phone_entry.place(x=565, y=295)

admin_customer_email_line = tk.Canvas(admin_customer_frame, bg=label_color, width=120, height=2.0, highlightthickness=0)
admin_customer_email_line.place(x=565, y=381)

admin_customer_email_entry = tk.Entry(admin_customer_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=13)
admin_customer_email_entry.place(x=565, y=355)





############################################################# CUSTOMER ACTION BUTTONS ###########################################################

admin_customer_save_btn = tk.Button(admin_customer_frame, text="Save", font=text_font, bg=button_color ,activebackground=button_color,
                                    height=1, width=8, pady=6 , command=admin_customer_save_click)
admin_customer_save_btn.place(x=170, y=460)

admin_customer_update_btn = tk.Button(admin_customer_frame, text="Update", font=text_font, bg=button_color ,activebackground=button_color,
                                      height=1, width=8, pady=6, command=admin_customer_update_click)
admin_customer_update_btn.place(x=270, y=460)

admin_customer_delete_btn = tk.Button(admin_customer_frame, text="Delete", font=text_font, bg=button_color ,activebackground=button_color,
                                      height=1, width=8, pady=6, command=admin_customer_remove_click)
admin_customer_delete_btn.place(x=370, y=460)

admin_customer_clear_btn = tk.Button(admin_customer_frame, text="Clear", font=text_font, bg=button_color ,activebackground=button_color,
                                     height=1, width=8, pady=6, command=admin_customer_clear_click)
admin_customer_clear_btn.place(x=470, y=460)

admin_customer_back_btn = tk.Button(
    admin_customer_frame,text="← Back",bg=NAVY,fg=TEXT,activebackground=NAVY,activeforeground="white",
    borderwidth=0,cursor="hand2",font=back_btn_font, command=lambda :show_frame(admin_main_frame))
admin_customer_back_btn.place(x=20, y=500)


# =================================================================================================================================================================================================================================================================================================
# =========================================================================================================================== ADMIN VEHICLES TABLE ==================================================================================================================================================

admin_vehicle_top_lbl = tk.Label(admin_vehicle_frame, text="Vehicle Management", bg="white", fg="black" , font = ("times new roman",15))
admin_vehicle_top_lbl.place(x=0, y=0, width= 710, height=23)

# ============================================================= ADMIN VEHICLE FUNCTIONS  ==========================================================


def admin_update_vehicle_table():
    for item in admin_vehicle_table.get_children():
        admin_vehicle_table.delete(item)
    user = VehicleController
    users = user.get_all_vehicles()
    for user in users:
        admin_vehicle_table.insert("","end", values=user)


def on_select_admin_vehicle_table(event):
    select_item = admin_vehicle_table.focus()
    if not select_item:
        return
    vehicle_values = admin_vehicle_table.item(select_item,"values")
    if not vehicle_values:
        return

    admin_vehicle_id_ent.delete(0, END)
    admin_vehicle_id_ent.insert(0, vehicle_values[0])

    admin_vehicle_customer_id_ent.delete(0,END)
    admin_vehicle_customer_id_ent.insert(0,vehicle_values[1])

    admin_vehicle_brand_ent.delete(0,END)
    admin_vehicle_brand_ent.insert(0,vehicle_values[2])

    admin_vehicle_model_ent.delete(0, END)
    admin_vehicle_model_ent.insert(0, vehicle_values[3])

    admin_vehicle_year_ent.delete(0, END)
    admin_vehicle_year_ent.insert(0, vehicle_values[4])

    parts = vehicle_values[5].split()

    admin_plate_part1.delete(0, END)
    admin_plate_part1.insert(0, parts[0])

    admin_plate_part2.delete(0, END)
    admin_plate_part2.insert(0, parts[1])

    admin_plate_part3.delete(0, END)
    admin_plate_part3.insert(0, parts[2])

    admin_plate_part4.delete(0, END)
    admin_plate_part4.insert(0, parts[4])





def admin_vehicle_save_click():

    # do we need customer id to add a car can it be automatically imported ???????????

    customer_id = admin_vehicle_customer_id_ent.get()
    brand = admin_vehicle_brand_ent.get()
    model = admin_vehicle_model_ent.get()
    year = admin_vehicle_year_ent.get()

    plate_number_raw = (
    admin_plate_part1.get().strip() + " "
    + admin_plate_part2.get().strip() + " "
    + admin_plate_part3.get().strip() + " ایران "
    + admin_plate_part4.get().strip()
)
    plate_number = plate_number_raw

    if "" in plate_number:
        return False, "all plate fields required"

    if customer_id == "" or brand == "" or model == "" or year == "":
        msg.showerror("Error", "All fields are required")
        return

    vehicle = VehicleController(customer_id=customer_id,brand=brand,model=model,year=year,plate_number=plate_number)
    status,message = vehicle.add_vehicle()

    if status:
        msg.showinfo("Saved", message)
        admin_update_vehicle_table()
        update_dashboard()
    else:
        msg.showerror("Error", message)

    admin_vehicle_brand_ent.delete(0, END)
    admin_vehicle_model_ent.delete(0, END)
    admin_vehicle_year_ent.delete(0, END)

    admin_plate_part1.delete(0, END)
    admin_plate_part2.delete(0, END)
    admin_plate_part3.delete(0, END)
    admin_plate_part4.delete(0, END)



def admin_vehicle_remove_click():
    admin_vehicle_id = admin_vehicle_id_ent.get()

    admin_vehicle = VehicleController()
    status,message = admin_vehicle.remove_vehicle(vehicle_id=admin_vehicle_id)

    if status:
        msg.showinfo("Removed", message)
        admin_update_vehicle_table()
        update_dashboard()
    else:
        msg.showerror("Error", message)

    admin_vehicle_id_ent.delete(0, END)


def admin_vehicle_clear_click():

    admin_vehicle_id_ent.delete(0, END)
    admin_vehicle_customer_id_ent.delete(0, END)
    admin_vehicle_brand_ent.delete(0, END)
    admin_vehicle_model_ent.delete(0, END)
    admin_vehicle_year_ent.delete(0, END)

    admin_plate_part1.delete(0, END)
    admin_plate_part2.delete(0, END)
    admin_plate_part3.delete(0, END)
    admin_plate_part4.delete(0, END)


def admin_vehicle_search_click():

    admin_vehicle_id = admin_vehicle_search_ent.get()

    admin_vehicle = VehicleController()
    status, result = admin_vehicle.search_vehicle(vehicle_id=admin_vehicle_id) # tuple of records

    if status:
        admin_vehicle_table.delete(*admin_vehicle_table.get_children())
        admin_vehicle_table.insert("", "end", values=result)

    else :
            msg.showerror("Error", "No records were found")


def admin_vehicle_show_click():

    vehicle = VehicleController()
    results = vehicle.get_all_vehicles()
    admin_vehicle_table.delete(*admin_vehicle_table.get_children())
    for row in results:
        admin_vehicle_table.insert("", "end", values=row)


def admin_vehicle_update_click():
    customer_id = admin_vehicle_customer_id_ent.get()
    vehicle_id = admin_vehicle_id_ent.get()
    brand = admin_vehicle_brand_ent.get()
    model = admin_vehicle_model_ent.get()
    year = admin_vehicle_year_ent.get()

    plate_number_raw = (
            admin_plate_part1.get().strip() + " "
            + admin_plate_part2.get().strip() + " "
            + admin_plate_part3.get().strip() + " ایران "
            + admin_plate_part4.get().strip()
    )

    vehicle = VehicleController(customer_id=customer_id, brand=brand, model=model, year=year, plate_number=plate_number_raw)
    status, message = vehicle.edit_vehicle(vehicle_id=vehicle_id)

    if status:
        msg.showinfo("Data got Updated", message)
        admin_update_vehicle_table()
    else:
        msg.showerror("Error", message)

    admin_vehicle_id_ent.delete(0, END)
    admin_vehicle_customer_id_ent.delete(0, END)
    admin_vehicle_brand_ent.delete(0, END)
    admin_vehicle_model_ent.delete(0, END)
    admin_vehicle_year_ent.delete(0, END)

    admin_plate_part1.delete(0, END)
    admin_plate_part2.delete(0, END)
    admin_plate_part3.delete(0, END)
    admin_plate_part4.delete(0, END)




#======================================== TOP SEARCH PART FOR VEHICLE =============================================

admin_vehicle_search_lbl = tk.Label(admin_vehicle_frame, text="Search by Vehicle id :", font=text_font , bg=NAVY, fg="white")
admin_vehicle_search_lbl.place(x=15, y=50)
admin_vehicle_search_ent = tk.Entry(admin_vehicle_frame, width=8, bg="white", font=text_font)
admin_vehicle_search_ent.place(x=185, y=50)

admin_vehicle_search_btn = tk.Button(admin_vehicle_frame, text="Search" , font=text_font, bg=button_color ,activebackground=button_color,
                                     command=admin_vehicle_search_click)
admin_vehicle_search_btn.place(x=280, y=47)

admin_vehicle_show_btn = tk.Button(admin_vehicle_frame, text="Show All", font=text_font, bg=button_color,activebackground=button_color ,
                                   command=admin_vehicle_show_click)
admin_vehicle_show_btn.place(x=356, y=47)




# ============================================================= ADMIN VEHICLE TABLE ==========================================================

# vehicle_id, customer_id, brand, model, plate_number,year


admin_vehicle_table = ttk.Treeview(admin_vehicle_frame,columns=(1,2,3,4,5,6),show="headings")
admin_vehicle_table.heading(1, text="vehicle_id")
admin_vehicle_table.heading(2, text="customer_id")
admin_vehicle_table.heading(3, text="brand")
admin_vehicle_table.heading(4, text="model")
admin_vehicle_table.heading(5, text="year")
admin_vehicle_table.heading(6, text="plate_number")


admin_vehicle_table.column(1, width=90)
admin_vehicle_table.column(2, width=90)
admin_vehicle_table.column(3, width=110)
admin_vehicle_table.column(4, width=120)
admin_vehicle_table.column(5, width=120)
admin_vehicle_table.column(6, width=120)

admin_vehicle_table.place(x=0,y=90, relwidth=1)

admin_update_vehicle_table()
admin_vehicle_table.bind("<<TreeviewSelect>>", on_select_admin_vehicle_table)



############################################################# VEHICLE ACTION BUTTONS ###########################################################

admin_vehicle_save_btn = tk.Button(admin_vehicle_frame, text="Save", font=text_font, bg=button_color ,activebackground=button_color,
                                   height=1, width=8, pady=6 , command=admin_vehicle_save_click)
admin_vehicle_save_btn.place(x=170, y=460)

admin_vehicle_update_btn = tk.Button(admin_vehicle_frame, text="Update", font=text_font, bg=button_color ,activebackground=button_color,
                                     height=1, width=8, pady=6, command=admin_vehicle_update_click)
admin_vehicle_update_btn.place(x=270, y=460)

admin_vehicle_delete_btn = tk.Button(admin_vehicle_frame, text="Delete", font=text_font, bg=button_color ,activebackground=button_color,
                                     height=1, width=8, pady=6, command=admin_vehicle_remove_click)
admin_vehicle_delete_btn.place(x=370, y=460)

admin_vehicle_clear_btn = tk.Button(admin_vehicle_frame, text="Clear", font=text_font, bg=button_color ,activebackground=button_color,
                                    height=1, width=8, pady=6, command=admin_vehicle_clear_click)
admin_vehicle_clear_btn.place(x=470, y=460)

admin_vehicle_back_btn = tk.Button(
    admin_vehicle_frame,text="← Back",bg=NAVY,fg=TEXT,activebackground=NAVY,activeforeground="white",
    borderwidth=0,cursor="hand2",font=back_btn_font, command=lambda :show_frame(admin_main_frame))
admin_vehicle_back_btn.place(x=20, y=500)



# ============================================================= ADMIN VEHICLE labels and entries ==========================================================

#vehicle labels

admin_vehicle_id_lbl = tk.Label(admin_vehicle_frame, text="Vehicle id", font=my_font, bg=NAVY, fg=TEXT)
admin_vehicle_id_lbl.place(x=25, y=340)

admin_vehicle_customer_id_lbl = tk.Label(admin_vehicle_frame, text="Customer id", font=my_font,bg=NAVY,fg=TEXT)
admin_vehicle_customer_id_lbl.place(x=25, y=400)

admin_vehicle_brand_lbl = tk.Label(admin_vehicle_frame, text="Brand", font=my_font, bg=NAVY, fg=TEXT)
admin_vehicle_brand_lbl.place(x=240, y=340)

admin_vehicle_model_lbl = tk.Label(admin_vehicle_frame, text="Model", font=my_font, bg=NAVY, fg=TEXT)
admin_vehicle_model_lbl.place(x=440, y=340)

admin_vehicle_year_lbl = tk.Label(admin_vehicle_frame, text="Year", font=my_font, bg=NAVY, fg=TEXT)
admin_vehicle_year_lbl.place(x=240, y=400)

admin_vehicle_plate_lbl = tk.Label(admin_vehicle_frame, text="Plate Number", font=my_font, bg=NAVY, fg=TEXT)
admin_vehicle_plate_lbl.place(x=440, y=400)

#vehicel entries

admin_vehicle_id_ent = tk.Entry(admin_vehicle_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=7)
admin_vehicle_id_ent.place(x=140, y=340)

admin_vehicle_id_ent_line = tk.Canvas(admin_vehicle_frame, bg=label_color, width=60, height=2.0, highlightthickness=0)
admin_vehicle_id_ent_line.place(x=140, y=366)

# =======

admin_vehicle_customer_id_ent = tk.Entry(admin_vehicle_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=7)
admin_vehicle_customer_id_ent.place(x=140, y=400)

admin_vehicle_customer_id_ent_line = tk.Canvas(admin_vehicle_frame, bg=label_color, width=60, height=2.0, highlightthickness=0)
admin_vehicle_customer_id_ent_line.place(x=140, y=426)

# =======

admin_vehicle_brand_ent = tk.Entry(admin_vehicle_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=10)
admin_vehicle_brand_ent.place(x=310, y=340)

admin_vehicle_brand_ent_line = tk.Canvas(admin_vehicle_frame, bg=label_color, width=80, height=2.0, highlightthickness=0)
admin_vehicle_brand_ent_line.place(x=310, y=366)

# =======

admin_vehicle_model_ent = tk.Entry(admin_vehicle_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=11)
admin_vehicle_model_ent.place(x=565, y=340)

admin_vehicle_model_ent_line = tk.Canvas(admin_vehicle_frame, bg=label_color, width=95, height=2.0, highlightthickness=0)
admin_vehicle_model_ent_line.place(x=565, y=366)

# =======

admin_vehicle_year_ent = tk.Entry(admin_vehicle_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=10)
admin_vehicle_year_ent.place(x=310, y=400)


admin_vehicle_year_ent_line = tk.Canvas(admin_vehicle_frame, bg=label_color, width=80, height=2.0, highlightthickness=0)
admin_vehicle_year_ent_line.place(x=310, y=426)

# # =======

admin_plate_part1 = tk.Entry(admin_vehicle_frame, bg="white", fg=NAVY, highlightthickness=0,font=text_font, width=2)
admin_plate_part1.place(x=565, y=400)

admin_plate_part2 = tk.Entry(admin_vehicle_frame, bg="white", fg=NAVY, highlightthickness=0,font=text_font, width=3)
admin_plate_part2.place(x=595, y=400)

admin_plate_part3 = tk.Entry(admin_vehicle_frame, bg="white", fg=NAVY, highlightthickness=0,font=text_font, width=3)
admin_plate_part3.place(x=630, y=400)

admin_plate_part4 = tk.Entry(admin_vehicle_frame, bg="white", fg=NAVY, highlightthickness=0,font=text_font, width=2)
admin_plate_part4.place(x=665, y=400)



# ---------- Auto Move Customer Plate ----------

admin_plate_part1.bind(
    "<KeyRelease>", lambda e: move_next(e, admin_plate_part1, admin_plate_part2, 2))

admin_plate_part2.bind(
    "<KeyRelease>", lambda e: move_next(e, admin_plate_part2, admin_plate_part3, 1))

admin_plate_part3.bind("<KeyRelease>",
                          lambda e: move_next(e, admin_plate_part3, admin_plate_part4, 3))

# ---------- Backspace ----------

admin_plate_part2.bind("<KeyPress>",
    lambda e: move_previous(e, admin_plate_part2, admin_plate_part1))

admin_plate_part3.bind("<KeyPress>",
    lambda e: move_previous(e, admin_plate_part3, admin_plate_part2))

admin_plate_part4.bind("<KeyPress>",
    lambda e: move_previous(e, admin_plate_part4, admin_plate_part3))


# =================================================================================================================================================================================================================================================================================================
# =============================================================================================================== ADMIN APPOINTMENT PART  ==========================================================================================================================================================
#
admin_appointment_top_lbl = tk.Label(admin_appointment_frame, text="Appointments Management", bg="white", fg="black" , font = ("times new roman",15))
admin_appointment_top_lbl.place(x=0, y=0, width= 710, height=23)

# # =========================================================================================================== ADMIN APPOINTMENT FUNCTIONS  ==========================================================================================================================================================
#
def admin_update_appointment_table():

    for item in admin_appointment_table.get_children():
        admin_appointment_table.delete(item)
    appointment = AppointmentController()
    appointments = appointment.get_all_appointments()
    for service in appointments:
        admin_appointment_table.insert("","end", values=service)


def on_select_admin_appointment_table(event):

    select_item = admin_appointment_table.focus()
    if not select_item:
        return
    appointment_values = admin_appointment_table.item(select_item,"values")
    if not appointment_values:
        return
    admin_appointment_id_entry.delete(0,END)
    admin_appointment_id_entry.insert(0,appointment_values[0])

    admin_appointment_customer_id_entry.delete(0,END)
    admin_appointment_customer_id_entry.insert(0,appointment_values[1])

    admin_appointment_vehicle_id_entry.delete(0,END)
    admin_appointment_vehicle_id_entry.insert(0,appointment_values[2])

    appointment_date = str(appointment_values[3])
    year, month, day = appointment_date.split("-")

    year_combo.set(year)
    month_combo.set(month)
    day_combo.set(day)

    appointment_status_combo.set("")
    appointment_status_combo.set(appointment_values[4])



def admin_appointment_save_click():

    customer_id = admin_appointment_customer_id_entry.get()
    vehicle_id = admin_appointment_vehicle_id_entry.get()
    appointment_status = appointment_status_combo.get()

    year = year_combo.get()
    month = month_combo.get()
    day = day_combo.get()
    appointment_date = f"{year}-{month}-{day}"


    appointment = AppointmentController(customer_id=customer_id, vehicle_id= vehicle_id, appointment_date=appointment_date,status=appointment_status)
    success, message = appointment.add_appointment()

    if customer_id=="" or vehicle_id=="" or appointment_date == "" or appointment_status == "":
        msg.showerror("Error", "All fields are required")
        return

    if success:
        msg.showinfo("Saved", message)
        admin_update_appointment_table()
        update_dashboard()
    else:
        msg.showerror("Error", message)


    admin_appointment_customer_id_entry.delete(0,END)
    admin_appointment_vehicle_id_entry.delete(0,END)
    year_combo.set("Year")
    month_combo.set("Month")
    day_combo.set("Day")
    appointment_status_combo.set("")



def admin_appointment_remove_click():

    appointment_id = admin_appointment_id_entry.get()

    if appointment_id == "":
        msg.showerror("Error", "ID required")
        return

    appointment = AppointmentController()
    status,message = appointment.cancel_appointment(appointment_id=appointment_id)

    if status:
        msg.showinfo("Appointment got Cancelled", message)
        admin_update_appointment_table()
        update_dashboard()
    else:
        msg.showerror("Error", message)

    admin_appointment_id_entry.delete(0,END)
    appointment_status_combo.set("")
    admin_appointment_customer_id_entry.delete(0, END)
    admin_appointment_vehicle_id_entry.delete(0, END)
    year_combo.set("Year")
    month_combo.set("Month")
    day_combo.set("Day")

def admin_appointment_clear_click():

    admin_appointment_id_entry.delete(0, END)
    admin_appointment_customer_id_entry.delete(0, END)
    admin_appointment_vehicle_id_entry.delete(0, END)
    year_combo.set("Year")
    month_combo.set("Month")
    day_combo.set("Day")
    appointment_status_combo.set("Choose Status")



def admin_appointment_update_click():

    appointment_id = admin_appointment_id_entry.get()
    customer_id = admin_appointment_customer_id_entry.get()
    vehicle_id = admin_appointment_vehicle_id_entry.get()
    year = year_combo.get()
    month = month_combo.get()
    day = day_combo.get()

    appointment_date = f"{year}-{month}-{day}"
    status = appointment_status_combo.get()

    appointment = AppointmentController(customer_id=customer_id, vehicle_id=vehicle_id, appointment_date=appointment_date, status=status)
    status , message = appointment.edit_appointment(appointment_id=appointment_id)

    if status:
        msg.showinfo("Data got Updated", message)
        admin_update_appointment_table()
    else:
        msg.showerror("Error", message)

    admin_appointment_id_entry.delete(0, END)
    admin_appointment_customer_id_entry.delete(0, END)
    admin_appointment_vehicle_id_entry.delete(0, END)
    year_combo.set("Year")
    month_combo.set("Month")
    day_combo.set("Day")
    appointment_status_combo.set("")

def appointment_update_status_click():

    appointment_id = admin_appointment_id_entry.get()
    appointment_status = appointment_status_combo.get()

    appointment = AppointmentController(status=appointment_status)


    success, message = appointment.update_status(appointment_id)

    if success:
        msg.showinfo("Success", message)
        admin_update_appointment_table()

    else:
        msg.showerror("Error", message)

def admin_appointment_search_click():

    admin_appointment_id = admin_appointment_search_ent.get()

    admin_appointment = AppointmentController()
    status, result = admin_appointment.search_appointment(appointment_id=admin_appointment_id) # tuple of records

    if status:
        admin_appointment_table.delete(*admin_appointment_table.get_children())
        admin_appointment_table.insert("", "end", values=result)

    else :
        msg.showerror("Error", "No records were found")

def admin_appointment_show_click():

    appointment = AppointmentController()
    results = appointment.get_all_appointments()
    admin_appointment_table.delete(*admin_appointment_table.get_children())
    for row in results:
        admin_appointment_table.insert("", "end", values=row)


# search part for appointments
admin_appointment_search_lbl = tk.Label(admin_appointment_frame, text="Search by appointment id :", font=text_font , bg=NAVY, fg="white")
admin_appointment_search_lbl.place(x=15, y=50)
admin_appointment_search_ent = tk.Entry(admin_appointment_frame, width=8, bg="white", font=text_font)
admin_appointment_search_ent.place(x=215, y=50)

admin_appointment_search_btn = tk.Button(admin_appointment_frame, text="Search" , font=text_font, bg=button_color ,activebackground=button_color,
                                         command=admin_appointment_search_click)
admin_appointment_search_btn.place(x=310, y=47)

admin_appointment_show_btn = tk.Button(admin_appointment_frame, text="Show All", font=text_font, bg=button_color,activebackground=button_color ,
                                       command=admin_appointment_show_click)
admin_appointment_show_btn.place(x=386, y=47)



# # ================================================================= ADMIN APPOINTMENT TABLE  ==========================================================


admin_appointment_table = ttk.Treeview(admin_appointment_frame,columns=(1,2,3,4,5),show="headings")
admin_appointment_table.heading(1, text="Appointment id")
admin_appointment_table.heading(2, text="Customer id")
admin_appointment_table.heading(3, text="Vehicle id")
admin_appointment_table.heading(4, text="Appointment Date")
admin_appointment_table.heading(5, text="Status")


admin_appointment_table.column(1, width=80)
admin_appointment_table.column(2, width=80)
admin_appointment_table.column(3, width=80)
admin_appointment_table.column(4, width=120)
admin_appointment_table.column(5, width=80)

admin_appointment_table.place(x=0,y=90, relwidth=1)

admin_update_appointment_table()
admin_appointment_table.bind("<<TreeviewSelect>>", on_select_admin_appointment_table)



#  ============================================================= ADMIN APPOINTMENT labels and entries ==========================================================

# #APPOINTMENT labels

admin_appointment_id_lbl = tk.Label(admin_appointment_frame, text="Appointment id", font=my_font, bg=NAVY, fg=TEXT)
admin_appointment_id_lbl.place(x=25, y=340)

admin_appointment_customer_id_lbl = tk.Label(admin_appointment_frame, text="Customer id", font=my_font,bg=NAVY,fg=TEXT)
admin_appointment_customer_id_lbl.place(x=240, y=340)

admin_appointment_vehicle_id_lbl = tk.Label(admin_appointment_frame, text="Vehicle id", font=my_font, bg=NAVY, fg=TEXT)
admin_appointment_vehicle_id_lbl.place(x=440, y=340)

admin_appointment_date_lbl = tk.Label(admin_appointment_frame, text="Appointment Date", font=my_font, bg=NAVY, fg=TEXT)
admin_appointment_date_lbl.place(x=300, y=400)

admin_appointment_status_lbl = tk.Label(admin_appointment_frame, text="Status", font=my_font, bg=NAVY, fg=TEXT)
admin_appointment_status_lbl.place(x=80, y=400)

# APPOINTMENT entries
admin_appointment_id_line = tk.Canvas(admin_appointment_frame, bg=label_color, width=60, height=2.0, highlightthickness=0)
admin_appointment_id_line.place(x=160, y=366)

admin_appointment_id_entry = tk.Entry(admin_appointment_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=7)
admin_appointment_id_entry.place(x=160, y=340)
# =====================
admin_appointment_customer_id_line = tk.Canvas(admin_appointment_frame, bg=label_color, width=60, height=2.0, highlightthickness=0)
admin_appointment_customer_id_line.place(x=355, y=366)

admin_appointment_customer_id_entry = tk.Entry(admin_appointment_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=7)
admin_appointment_customer_id_entry.place(x=355, y=340)
# =====================
admin_appointment_vehicle_id_line = tk.Canvas(admin_appointment_frame, bg=label_color, width=60, height=2.0, highlightthickness=0)
admin_appointment_vehicle_id_line.place(x=540, y=366)

admin_appointment_vehicle_id_entry = tk.Entry(admin_appointment_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=7)
admin_appointment_vehicle_id_entry.place(x=540, y=340)
# =====================

year_combo = ttk.Combobox(admin_appointment_frame,values=[str(y) for y in range(2025, 2031)], state="readonly", width=6)
year_combo.place(x=460, y=403)
year_combo.set("Year")

month_combo = ttk.Combobox(admin_appointment_frame, values=[f"{m:02d}" for m in range(1, 13)], state="readonly", width=6)
month_combo.place(x=530, y=403)
month_combo.set("Month")

day_combo = ttk.Combobox(admin_appointment_frame, values=[f"{d:02d}" for d in range(1, 32)], state="readonly", width=5)
day_combo.place(x=600, y=403)
day_combo.set("Day")


# =====================
appointment_status_combo = ttk.Combobox(admin_appointment_frame, values=["Pending", "In Progress", "Completed", "Cancelled"],
                state="readonly", width=13, font = ("Segoe UI", 10), justify="center")

appointment_status_combo.set("Choose Status")   # set it to a default value (without this even with an option they should click it again)

appointment_status_combo.place(x=150, y=403)


update_status_btn = tk.Button(admin_appointment_frame, text="Update Status",font=text_font, bg=button_color ,activebackground=button_color,
                              height=1, width=13, pady=6, command=appointment_update_status_click)
update_status_btn.place(x=500,y=460)


# ############################################################# APPOINTMENT ACTION BUTTONS ###########################################################

admin_appointment_save_btn = tk.Button(admin_appointment_frame, text="Save", font=text_font, bg=button_color ,activebackground=button_color,
                                       height=1, width=8, pady=6 , command=admin_appointment_save_click)
admin_appointment_save_btn.place(x=100, y=460)

admin_appointment_update_btn = tk.Button(admin_appointment_frame, text="Update", font=text_font, bg=button_color ,activebackground=button_color,
                                         height=1, width=8, pady=6, command=admin_appointment_update_click)
admin_appointment_update_btn.place(x=200, y=460)

admin_appointment_delete_btn = tk.Button(admin_appointment_frame, text="Delete", font=text_font, bg=button_color ,activebackground=button_color,
                                         height=1, width=8, pady=6, command=admin_appointment_remove_click)
admin_appointment_delete_btn.place(x=300, y=460)

admin_appointment_clear_btn = tk.Button(admin_appointment_frame, text="Clear", font=text_font, bg=button_color ,activebackground=button_color,
                                        height=1, width=8, pady=6, command=admin_appointment_clear_click)
admin_appointment_clear_btn.place(x=400, y=460)


admin_appointment_back_btn = tk.Button(
    admin_appointment_frame,text="← Back",bg=NAVY,fg=TEXT,activebackground=NAVY,activeforeground="white",
    borderwidth=0,cursor="hand2",font=back_btn_font, command=lambda :show_frame(admin_main_frame))
admin_appointment_back_btn.place(x=20, y=500)



# ===============================================================================================================================================================================================================================================================================================
# =============================================================================================================== ADMIN SERVICES PART  ==========================================================================================================================================================

admin_service_top_lbl = tk.Label(admin_service_frame, text="Services Management", bg="white", fg="black" , font = ("times new roman",15))
admin_service_top_lbl.place(x=0, y=0, width= 710, height=23)

# =========================================================================================================== ADMIN SERVICES FUNCTIONS  ==========================================================================================================================================================

def admin_update_service_table():
    for item in admin_service_table.get_children():
        admin_service_table.delete(item)
    service = ServiceController()
    services = service.get_all_services()
    for service in services:
        admin_service_table.insert("","end", values=service)


def on_select_admin_service_table(event):
    select_item = admin_service_table.focus()
    if not select_item:
        return
    service_values = admin_service_table.item(select_item,"values")
    if not service_values:
        return
    admin_service_id_entry.delete(0,END)
    admin_service_id_entry.insert(0,service_values[0])

    admin_service_name_entry.delete(0,END)
    admin_service_name_entry.insert(0,service_values[1])

    admin_service_price_entry.delete(0,END)
    admin_service_price_entry.insert(0,service_values[2])




def admin_service_save_click():

    service_name = admin_service_name_entry.get()
    price = admin_service_price_entry.get()

    service = ServiceController(service_name, price)
    status, message = service.add_service()

    if service_name == "" or price == "" :
        msg.showerror("Error", "All fields are required")
        return

    if status:
        msg.showinfo("Saved", message)
        admin_update_service_table()
    else:
        msg.showerror("Error", message)

    admin_service_name_entry.delete(0, END)
    admin_service_price_entry.delete(0, END)


def admin_service_remove_click():
    service_id = admin_service_id_entry.get()

    service = ServiceController()
    status,message = service.remove_service(service_id)

    if status:
        msg.showinfo("Removed", message)
        admin_update_service_table()
    else:
        msg.showerror("Error", message)

    admin_service_id_entry.delete(0,END)

def admin_service_clear_click():

    admin_service_id_entry.delete(0, END)
    admin_service_name_entry.delete(0, END)
    admin_service_price_entry.delete(0, END)

def admin_service_update_click():

    service_id = admin_service_id_entry.get()
    service_name = admin_service_name_entry.get()
    price = admin_service_price_entry.get()


    service = ServiceController(service_name, price)
    status , message = service.edit_service(service_id)

    if status:
        msg.showinfo("Data got Updated", message)
        admin_update_service_table()
    else:
        msg.showerror("Error", message)

    admin_service_id_entry.delete(0,END)
    admin_service_name_entry.delete(0,END)
    admin_service_price_entry.delete(0,END)


def admin_service_search_click():

    service_name = admin_service_search_ent.get()

    admin_service = ServiceController(service_name=service_name)
    status, result = admin_service.search_service() # tuple of records

    if status:
        admin_service_table.delete(*admin_service_table.get_children())
        for row in result:
            admin_service_table.insert("", "end", values=row)

    else :
            msg.showerror("Error", "No records were found")


def admin_service_show_click():

    service = ServiceController()
    results = service.get_all_services()
    admin_service_table.delete(*admin_service_table.get_children())
    for row in results:
        admin_service_table.insert("", "end", values=row)





# search part for service
admin_service_search_lbl = tk.Label(admin_service_frame, text="Search by service name :", font=text_font , bg=NAVY, fg="white")
admin_service_search_lbl.place(x=15, y=130)

admin_service_search_ent = tk.Entry(admin_service_frame, width=8, bg="white", font=text_font)
admin_service_search_ent.place(x=195, y=132)

admin_service_search_btn = tk.Button(admin_service_frame, text="Search" , font=text_font, bg=button_color ,activebackground=button_color,
                                     command=admin_service_search_click)
admin_service_search_btn.place(x=290, y=127)

admin_service_show_btn = tk.Button(admin_service_frame, text="Show All", font=text_font, bg=button_color,activebackground=button_color ,
                                   command=admin_service_show_click)
admin_service_show_btn.place(x=366, y=127)



# ================================================================= ADMIN SERVICES TABLE  ==========================================================


admin_service_table = ttk.Treeview(admin_service_frame,columns=(1,2,3),show="headings")
admin_service_table.heading(1, text="Service id")
admin_service_table.heading(2, text="Service Name")
admin_service_table.heading(3, text="Price")



admin_service_table.column(1, width=90)
admin_service_table.column(2, width=170)
admin_service_table.column(3, width=90)

admin_service_table.place(x=20,y=180)

admin_update_service_table()
admin_service_table.bind("<<TreeviewSelect>>", on_select_admin_service_table)


service_scroll_y = ttk.Scrollbar(admin_service_frame,orient="vertical",command=admin_service_table.yview)

service_scroll_y.place(x=354, y=180, height=225)

admin_service_table.configure(yscrollcommand=service_scroll_y.set)

# ============================================================= ADMIN SERVICES labels and entries ==========================================================

#service labels

admin_service_id_lbl = tk.Label(admin_service_frame, text="Service id", font=my_font, bg=NAVY, fg=TEXT)
admin_service_id_lbl.place(x=395, y=210)

admin_service_name_lbl = tk.Label(admin_service_frame, text="Service Name", font=my_font,bg=NAVY,fg=TEXT)
admin_service_name_lbl.place(x=395, y=270)

admin_service_price_lbl = tk.Label(admin_service_frame, text="Price", font=my_font, bg=NAVY, fg=TEXT)
admin_service_price_lbl.place(x=395, y=330)


#services entries
admin_service_id_line = tk.Canvas(admin_service_frame, bg=label_color, width=120, height=2.0, highlightthickness=0)
admin_service_id_line.place(x=530, y=234)

admin_service_id_entry = tk.Entry(admin_service_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=13)
admin_service_id_entry.place(x=530, y=208)
# ===================
admin_service_name_line = tk.Canvas(admin_service_frame, bg=label_color, width=150, height=2.0, highlightthickness=0)
admin_service_name_line.place(x=530, y=294)

admin_service_name_entry = tk.Entry(admin_service_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=18)
admin_service_name_entry.place(x=530, y=268)
# ===================
admin_service_price_line = tk.Canvas(admin_service_frame, bg=label_color, width=120, height=2.0, highlightthickness=0)
admin_service_price_line.place(x=530, y=354)

admin_service_price_entry = tk.Entry(admin_service_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=13)
admin_service_price_entry.place(x=530, y=328)
# ===================



############################################################# SERVICES ACTION BUTTONS ###########################################################

admin_service_save_btn = tk.Button(admin_service_frame, text="Save", font=text_font, bg=button_color ,activebackground=button_color,
                                   height=1, width=8, pady=6 , command=admin_service_save_click)
admin_service_save_btn.place(x=170, y=460)

admin_service_update_btn = tk.Button(admin_service_frame, text="Update", font=text_font, bg=button_color ,activebackground=button_color,
                                     height=1, width=8, pady=6, command=admin_service_update_click)
admin_service_update_btn.place(x=270, y=460)

admin_service_delete_btn = tk.Button(admin_service_frame, text="Delete", font=text_font, bg=button_color ,activebackground=button_color,
                                     height=1, width=8, pady=6, command=admin_service_remove_click)
admin_service_delete_btn.place(x=370, y=460)

admin_service_clear_btn = tk.Button(admin_service_frame, text="Clear", font=text_font, bg=button_color ,activebackground=button_color,
                                    height=1, width=8, pady=6, command=admin_service_clear_click)
admin_service_clear_btn.place(x=470, y=460)


admin_service_back_btn = tk.Button(
    admin_service_frame,text="← Back",bg=NAVY,fg=TEXT,activebackground=NAVY,activeforeground="white",
    borderwidth=0,cursor="hand2",font=back_btn_font, command=lambda :show_frame(admin_main_frame))
admin_service_back_btn.place(x=20, y=500)


# =================================================================================================================================================================================================================================================================================================
# =============================================================================================================== ADMIN PAYMENT PART  ==========================================================================================================================================================

admin_payment_top_lbl = tk.Label(admin_payment_frame, text="Payment Management", bg="white", fg="black" , font = ("times new roman",15))
admin_payment_top_lbl.place(x=0, y=0, width= 710, height=23)

# # =========================================================================================================== ADMIN PAYMENT FUNCTIONS  ==========================================================================================================================================================

def admin_update_payment_table():
    for item in admin_payment_table.get_children():
        admin_payment_table.delete(item)
    payment = PaymentController()
    payments = payment.get_all_payments()
    for service in payments:
        admin_payment_table.insert("","end", values=service)


def on_select_admin_payment_table(event):

    select_item = admin_payment_table.focus()
    if not select_item:
        return
    payment_values = admin_payment_table.item(select_item,"values")
    if not payment_values:
        return
    admin_payment_id_entry.delete(0,END)
    admin_payment_id_entry.insert(0,payment_values[0])

    admin_payment_appointment_id_entry.delete(0,END)
    admin_payment_appointment_id_entry.insert(0,payment_values[1])

    admin_payment_total_price_entry.delete(0,END)
    admin_payment_total_price_entry.insert(0,payment_values[2])

    payment_status_combo.set("")
    payment_status_combo.set(payment_values[3])



def admin_payment_save_click():

    appointment_id = admin_payment_appointment_id_entry.get()
    total_price = admin_payment_total_price_entry.get()
    payment_status = payment_status_combo.get()

    payment = PaymentController(appointment_id=appointment_id, total_price=total_price,payment_status=payment_status)
    status,message = payment.add_payment()


    if status:
        msg.showinfo("Saved", message)
        admin_update_payment_table()
    else:
        msg.showerror("Error", message)

    admin_payment_appointment_id_entry.delete(0, END)
    admin_payment_total_price_entry.delete(0, END)
    payment_status_combo.set("")

def admin_payment_remove_click():

    payment_id = admin_payment_id_entry.get()

    admin_payment = PaymentController()
    status,message = admin_payment.remove_payment(payment_id)

    if status:
        msg.showinfo("Removed", message)
        admin_update_payment_table()
    else:
        msg.showerror("Error", message)

    admin_payment_id_entry.delete(0,END)

def admin_payment_clear_click():

    admin_payment_id_entry.delete(0, END)
    admin_payment_appointment_id_entry.delete(0, END)
    admin_payment_total_price_entry.delete(0, END)
    payment_status_combo.set("")

def admin_payment_search_click():

    admin_payment_id = admin_payment_search_ent.get()

    admin_payment = PaymentController()
    status, result = admin_payment.search_payment(payment_id=admin_payment_id) # tuple of records

    if status:
        admin_payment_table.delete(*admin_payment_table.get_children())
        admin_payment_table.insert("", "end", values=result)

    else :
            msg.showerror("Error", "No records were found")

def admin_payment_show_click():

    payment = PaymentController()
    results = payment.get_all_payments()
    admin_payment_table.delete(*admin_payment_table.get_children())
    for row in results:
        admin_payment_table.insert("", "end", values=row)

def admin_payment_update_click():

    payment_id = admin_payment_id_entry.get()
    appointment_id = admin_payment_appointment_id_entry.get()
    total_price = admin_payment_total_price_entry.get()
    payment_status = payment_status_combo.get()

    payment = PaymentController(appointment_id=appointment_id, total_price=total_price,payment_status=payment_status)
    status , message = payment.edit_payment(payment_id=payment_id)

    if status:
        msg.showinfo("Data got Updated", message)
        admin_update_payment_table()
    else:
        msg.showerror("Error", message)

    admin_payment_id_entry.delete(0, END)
    admin_payment_appointment_id_entry.delete(0, END)
    admin_payment_total_price_entry.delete(0, END)
    payment_status_combo.set("")



# search part FOR PAYMENT
admin_payment_search_lbl = tk.Label(admin_payment_frame, text="Search by payment id :", font=text_font , bg=NAVY, fg="white")
admin_payment_search_lbl.place(x=15, y=130)
admin_payment_search_ent = tk.Entry(admin_payment_frame, width=8, bg="white", font=text_font)
admin_payment_search_ent.place(x=185, y=132)

admin_payment_search_btn = tk.Button(admin_payment_frame, text="Search" , font=text_font, bg=button_color ,activebackground=button_color,
                                     command=admin_payment_search_click)
admin_payment_search_btn.place(x=280, y=127)

admin_payment_show_btn = tk.Button(admin_payment_frame, text="Show All", font=text_font, bg=button_color,activebackground=button_color ,
                                   command=admin_payment_show_click)
admin_payment_show_btn.place(x=356, y=127)


# # ================================================================= ADMIN PAYMENT TABLE  ==========================================================


admin_payment_table = ttk.Treeview(admin_payment_frame,columns=(1,2,3,4),show="headings")
admin_payment_table.heading(1, text="Payment id")
admin_payment_table.heading(2, text="Appointment id")
admin_payment_table.heading(3, text="Total Price")
admin_payment_table.heading(4, text="Payment Status")



admin_payment_table.column(1, width=85)
admin_payment_table.column(2, width=105)
admin_payment_table.column(3, width=90)
admin_payment_table.column(4, width=110)


admin_payment_table.place(x=15,y=180)

admin_update_payment_table()
admin_payment_table.bind("<<TreeviewSelect>>", on_select_admin_payment_table)


payment_scroll_y = ttk.Scrollbar(admin_payment_frame,orient="vertical",command=admin_payment_table.yview)

payment_scroll_y.place(x=403, y=180, height=225)

admin_payment_table.configure(yscrollcommand=payment_scroll_y.set)


# # ============================================================= ADMIN PAYMENT labels and entries ==========================================================

# #PAYMENT labels

admin_payment_id_lbl = tk.Label(admin_payment_frame, text="Payment id", font=my_font, bg=NAVY, fg=TEXT)
admin_payment_id_lbl.place(x=440, y=175)

admin_payment_appointment_id_lbl = tk.Label(admin_payment_frame, text="Appointment id", font=my_font,bg=NAVY,fg=TEXT)
admin_payment_appointment_id_lbl.place(x=440, y=235)

admin_payment_total_price_lbl = tk.Label(admin_payment_frame, text="Total Price", font=my_font, bg=NAVY, fg=TEXT)
admin_payment_total_price_lbl.place(x=440, y=295)

admin_payment_status_lbl = tk.Label(admin_payment_frame, text="Payment Status", font=my_font, bg=NAVY, fg=TEXT)
admin_payment_status_lbl.place(x=440, y=355)


# #PAYMENT entries
admin_payment_id_line = tk.Canvas(admin_payment_frame, bg=label_color, width=120, height=2.0, highlightthickness=0)
admin_payment_id_line.place(x=565, y=201)

admin_payment_id_entry = tk.Entry(admin_payment_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=13)
admin_payment_id_entry.place(x=565, y=175)
# # =====================
admin_payment_appointment_id_line = tk.Canvas(admin_payment_frame, bg=label_color, width=120, height=2.0, highlightthickness=0)
admin_payment_appointment_id_line.place(x=565, y=261)

admin_payment_appointment_id_entry = tk.Entry(admin_payment_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=13)
admin_payment_appointment_id_entry.place(x=565, y=235)
# # =====================
admin_payment_total_price_line = tk.Canvas(admin_payment_frame, bg=label_color, width=120, height=2.0, highlightthickness=0)
admin_payment_total_price_line.place(x=565, y=321)

admin_payment_total_price_entry = tk.Entry(admin_payment_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=13)
admin_payment_total_price_entry.place(x=565, y=295)
# # =====================
payment_status_combo = ttk.Combobox(admin_payment_frame, values=["Paid", "UnPaid"],
                state="readonly", width=13, font = ("Segoe UI", 10), justify="center")

payment_status_combo.set("Choose Status")   # set it to a default value (without this even with an option they should click it again)

payment_status_combo.place(x=565, y=355)




# ############################################################# PAYMENT ACTION BUTTONS ###########################################################

admin_payment_save_btn = tk.Button(admin_payment_frame, text="Save", font=text_font, bg=button_color ,activebackground=button_color,
                                   height=1, width=8, pady=6 , command=admin_payment_save_click)
admin_payment_save_btn.place(x=170, y=460)

admin_payment_update_btn = tk.Button(admin_payment_frame, text="Update", font=text_font, bg=button_color ,activebackground=button_color,
                                     height=1, width=8, pady=6, command=admin_payment_update_click)
admin_payment_update_btn.place(x=270, y=460)

admin_payment_delete_btn = tk.Button(admin_payment_frame, text="Delete", font=text_font, bg=button_color ,activebackground=button_color,
                                     height=1, width=8, pady=6, command=admin_payment_remove_click)
admin_payment_delete_btn.place(x=370, y=460)

admin_payment_clear_btn = tk.Button(admin_payment_frame, text="Clear", font=text_font, bg=button_color ,activebackground=button_color,
                                    height=1, width=8, pady=6, command=admin_payment_clear_click)
admin_payment_clear_btn.place(x=470, y=460)


admin_payment_back_btn = tk.Button(
    admin_payment_frame,text="← Back",bg=NAVY,fg=TEXT,activebackground=NAVY,activeforeground="white",
    borderwidth=0,cursor="hand2",font=back_btn_font, command=lambda :show_frame(admin_main_frame))
admin_payment_back_btn.place(x=20, y=500)



# =================================================================================================================================================================================================================================================================================================
# =============================================================================================================== ADMIN REVIEW PART  ==========================================================================================================================================================

admin_review_top_lbl = tk.Label(admin_review_frame, text="Review Management", bg="white", fg="black" , font = ("times new roman",15))
admin_review_top_lbl.place(x=0, y=0, width= 710, height=23)

# # =========================================================================================================== ADMIN REVIEW FUNCTIONS  ==========================================================================================================================================================

def admin_update_review_table():

    for item in admin_review_table.get_children():
        admin_review_table.delete(item)
    review = ReviewController()
    reviews = review.get_all_reviews()
    for review in reviews:
        admin_review_table.insert("","end", values=review)


def on_select_admin_review_table(event):

    select_item = admin_review_table.focus()
    if not select_item:
        return
    review_values = admin_review_table.item(select_item,"values")
    if not review_values:
        return
    admin_review_id_entry.delete(0,END)
    admin_review_id_entry.insert(0,review_values[0])

    admin_review_customer_id_entry.delete(0,END)
    admin_review_customer_id_entry.insert(0,review_values[1])

    admin_review_rating_entry.delete(0,END)
    admin_review_rating_entry.insert(0,review_values[2])

    admin_review_comment_entry.delete(0, END)
    admin_review_comment_entry.insert(0, review_values[3])

    admin_review_date_entry.delete(0, END)
    admin_review_date_entry.insert(0, review_values[4])



def admin_review_save_click():

    customer_id = admin_review_customer_id_entry.get()
    rating = admin_review_rating_entry.get()
    comment = admin_review_comment_entry.get()
    review_date = admin_review_date_entry.get()

    review = ReviewController(customer_id, rating, comment, review_date)
    status,message = review.add_review()

    if customer_id == "" or rating == "" or comment == "" or review_date == "":
        msg.showerror("Error", "All fields are required")
        return

    if status:
        msg.showinfo("Saved", message)
        admin_update_review_table()
    else:
        msg.showerror("Error", message)

    admin_review_customer_id_entry.delete(0,END)
    admin_review_rating_entry.delete(0,END)
    admin_review_comment_entry.delete(0, END)
    admin_review_date_entry.delete(0, END)


def admin_review_remove_click():

    admin_review_id = admin_review_id_entry.get()

    admin_review = ReviewController()
    status,message = admin_review.remove_review(review_id=admin_review_id)

    if status:
        msg.showinfo("Removed", message)
        admin_update_review_table()
    else:
        msg.showerror("Error", message)

    admin_review_id_entry.delete(0,END)

def admin_review_clear_click():
    
    admin_review_id_entry.delete(0,END)
    admin_review_customer_id_entry.delete(0, END)
    admin_review_rating_entry.delete(0, END)
    admin_review_comment_entry.delete(0, END)
    admin_review_date_entry.delete(0, END)


def admin_review_update_click():

    review_id = admin_review_id_entry.get()
    customer_id = admin_review_customer_id_entry.get()
    rating = admin_review_rating_entry.get()
    comment = admin_review_comment_entry.get()
    review_date = admin_review_date_entry.get()

    review = ReviewController(customer_id=customer_id, rating=rating, comment=comment, review_date=review_date)
    status , message = review.edit_review(review_id=review_id)

    if status:
        msg.showinfo("Data got Updated", message)
        admin_update_review_table()
    else:
        msg.showerror("Error", message)

    admin_review_id_entry.delete(0, END)
    admin_review_customer_id_entry.delete(0, END)
    admin_review_rating_entry.delete(0, END)
    admin_review_comment_entry.delete(0, END)
    admin_review_date_entry.delete(0, END)



# ================================================================= ADMIN REVIEW TABLE  ==========================================================


admin_review_table = ttk.Treeview(admin_review_frame,columns=(1,2,3,4,5),show="headings")
admin_review_table.heading(1, text="Review id")
admin_review_table.heading(2, text="Customer id")
admin_review_table.heading(3, text="Rating")
admin_review_table.heading(4, text="Comment")
admin_review_table.heading(5, text="Review Date")


admin_review_table.column(1, width=80)
admin_review_table.column(2, width=80)
admin_review_table.column(3, width=100)
admin_review_table.column(4, width=120)
admin_review_table.column(5, width=100)

admin_review_table.place(x=0,y=80, relwidth=1)

admin_update_review_table()
admin_review_table.bind("<<TreeviewSelect>>", on_select_admin_review_table)


# ============================================================= ADMIN REVIEW labels and entries ==========================================================

# review labels

admin_review_id_lbl = tk.Label(admin_review_frame, text="Review id", font=my_font, bg=NAVY, fg=TEXT)
admin_review_id_lbl.place(x=25, y=340)

admin_review_customer_id_lbl = tk.Label(admin_review_frame, text="Customer id", font=my_font,bg=NAVY,fg=TEXT)
admin_review_customer_id_lbl.place(x=240, y=340)

admin_review_rating_lbl = tk.Label(admin_review_frame, text="Rating", font=my_font, bg=NAVY, fg=TEXT)
admin_review_rating_lbl.place(x=440, y=340)

admin_review_comment_lbl = tk.Label(admin_review_frame, text="Comment", font=my_font, bg=NAVY, fg=TEXT)
admin_review_comment_lbl.place(x=25, y=400)

admin_review_date_lbl = tk.Label(admin_review_frame, text="Review Date", font=my_font, bg=NAVY, fg=TEXT)
admin_review_date_lbl.place(x=380, y=400)


# review entries
admin_review_id_line = tk.Canvas(admin_review_frame, bg=label_color, width=60, height=2.0, highlightthickness=0)
admin_review_id_line.place(x=130, y=366)

admin_review_id_entry = tk.Entry(admin_review_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=7)
admin_review_id_entry.place(x=130, y=340)
# =====================
admin_review_customer_id_line = tk.Canvas(admin_review_frame, bg=label_color, width=60, height=2.0, highlightthickness=0)
admin_review_customer_id_line.place(x=355, y=366)

admin_review_customer_id_entry = tk.Entry(admin_review_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=7)
admin_review_customer_id_entry.place(x=355, y=340)
# =====================
admin_review_rating_line = tk.Canvas(admin_review_frame, bg=label_color, width=60, height=2.0, highlightthickness=0)
admin_review_rating_line.place(x=520, y=366)

admin_review_rating_entry = tk.Entry(admin_review_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=7)
admin_review_rating_entry.place(x=520, y=340)
# =====================
admin_review_comment_line = tk.Canvas(admin_review_frame, bg=label_color, width=200, height=2.0, highlightthickness=0)
admin_review_comment_line.place(x=120, y=426)

admin_review_comment_entry = tk.Entry(admin_review_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=25)
admin_review_comment_entry.place(x=120, y=400)
# # =====================
admin_review_date_line = tk.Canvas(admin_review_frame, bg=label_color, width=130, height=2.0, highlightthickness=0)
admin_review_date_line.place(x=500, y=426)

admin_review_date_entry = tk.Entry(admin_review_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=15)
admin_review_date_entry.place(x=500, y=400)





# ############################################################# REVIEW ACTION BUTTONS ###########################################################

admin_review_save_btn = tk.Button(admin_review_frame, text="Save", font=text_font, bg=button_color ,activebackground=button_color,
                                  height=1, width=8, pady=6 , command=admin_review_save_click)
admin_review_save_btn.place(x=170, y=460)

admin_review_update_btn = tk.Button(admin_review_frame, text="Update", font=text_font, bg=button_color ,activebackground=button_color,
                                    height=1, width=8, pady=6, command=admin_review_update_click)
admin_review_update_btn.place(x=270, y=460)

admin_review_delete_btn = tk.Button(admin_review_frame, text="Delete", font=text_font, bg=button_color ,activebackground=button_color,
                                    height=1, width=8, pady=6, command=admin_review_remove_click)
admin_review_delete_btn.place(x=370, y=460)

admin_review_clear_btn = tk.Button(admin_review_frame, text="Clear", font=text_font, bg=button_color ,activebackground=button_color,
                                   height=1, width=8, pady=6, command=admin_review_clear_click)
admin_review_clear_btn.place(x=470, y=460)



admin_review_back_btn = tk.Button(
    admin_review_frame,text="← Back",bg=NAVY,fg=TEXT,activebackground=NAVY,activeforeground="white",
    borderwidth=0,cursor="hand2",font=back_btn_font, command=lambda :show_frame(admin_main_frame))
admin_review_back_btn.place(x=20, y=500)


# =============================================================================================================================================================================================================================================================================
# =============================================================================================================================== ADMIN USERS TABLE ============================================================================================================================

admin_user_top_lbl = tk.Label(admin_user_frame, text="Users Management", bg="white", fg="black" , font = ("times new roman",15))
admin_user_top_lbl.place(x=0, y=0, width= 710, height=23)

# ==========================================  remember in remove user button to admin_user_id = user_id ============================================
# def admin_user_remove_click():
#     admin_user_id = admin_user_id_entry.get()
#
#     admin_user = UserController(user_id=admin_user_id)
#     status,message = admin_user.remove_customer()


# # =========================================================================================================== ADMIN REVIEW FUNCTIONS  ==========================================================================================================================================================

def admin_update_user_table():
    for item in admin_user_table.get_children():
        admin_user_table.delete(item)

    user = UserController()
    users = user.get_all_users()

    for user in users:
        admin_user_table.insert("", "end", values=user)


def on_select_admin_user_table(event):

    select_item = admin_user_table.focus()
    if not select_item:
        return
    user_values = admin_user_table.item(select_item, "values")
    if not user_values:
        return
    admin_user_id_entry.delete(0, END)
    admin_user_id_entry.insert(0, user_values[0])

    admin_user_username_entry.delete(0, END)
    admin_user_username_entry.insert(0, user_values[1])

    admin_user_password_entry.delete(0, END)
    admin_user_password_entry.insert(0, user_values[2])

    admin_user_role_combo.set("")
    admin_user_role_combo.set(user_values[3])


def admin_user_save_click():

    username = admin_user_username_entry.get()
    password = admin_user_password_entry.get()
    role = admin_user_role_combo.get()

    user = UserController(username, password, role)
    status, message = user.add_user()

    if  username == "" or password == "" or role == "":
        msg.showerror("Error", "All fields are required")
        return

    if status:
        msg.showinfo("Saved", message)
        admin_update_user_table()
    else:
        msg.showerror("Error", message)

    admin_user_username_entry.delete(0, END)
    admin_user_password_entry.delete(0, END)
    admin_user_role_combo.set("")


def admin_user_remove_click():

    admin_user_id = admin_user_id_entry.get()

    admin_user = UserController(user_id=admin_user_id)
    status, message = admin_user.remove_user()

    if status:
        msg.showinfo("Removed", message)
        admin_update_user_table()
    else:
        msg.showerror("Error", message)

    admin_user_id_entry.delete(0, END)


def admin_user_clear_click():

    admin_user_id_entry.delete(0, END)
    admin_user_username_entry.delete(0, END)
    admin_user_password_entry.delete(0, END)
    admin_user_role_combo.set("")

def admin_user_update_click():

    user_id = admin_user_id_entry.get()
    username = admin_user_username_entry.get()
    password = admin_user_password_entry.get()
    role = admin_user_role_combo.get()

    user = UserController(user_id=user_id, username=username, password=password, role=role)
    status, message = user.edit_user()

    if status:
        msg.showinfo("Data got Updated", message)
        admin_update_user_table()
    else:
        msg.showerror("Error", message)

    admin_user_id_entry.delete(0, END)
    admin_user_username_entry.delete(0, END)
    admin_user_password_entry.delete(0, END)
    admin_user_role_combo.set("")

def admin_user_search_click():

    admin_user_id = admin_user_search_ent.get()

    admin_user = UserController(user_id=admin_user_id)
    status, result = admin_user.search_user() # tuple of records

    if status:
        admin_user_table.delete(*admin_user_table.get_children())
        admin_user_table.insert("", "end", values=result)

    else :
            msg.showerror("Error", "No records were found")

def admin_user_show_click():

    user = UserController()
    results = user.get_all_users()
    admin_user_table.delete(*admin_user_table.get_children())
    for row in results:
        admin_user_table.insert("", "end", values=row)

# # ================================================================= ADMIN USER TABLE  ==========================================================


admin_user_table = ttk.Treeview(admin_user_frame, columns=(1, 2, 3, 4), show="headings")
admin_user_table.heading(1, text="User id")
admin_user_table.heading(2, text="Username")
admin_user_table.heading(3, text="Password")
admin_user_table.heading(4, text="Role")

admin_user_table.column(1, width=80)
admin_user_table.column(2, width=100)
admin_user_table.column(3, width=100)
admin_user_table.column(4, width=110)


admin_user_table.place(x=15,y=170)

admin_update_user_table()
admin_user_table.bind("<<TreeviewSelect>>", on_select_admin_user_table)


user_scroll_y = ttk.Scrollbar(admin_user_frame,orient="vertical",command=admin_user_table.yview)

user_scroll_y.place(x=402, y=170, height=225)

admin_user_table.configure(yscrollcommand=user_scroll_y.set)


# # ============================================================= ADMIN USERS labels and entries ==========================================================

# #PAYMENT labels

admin_user_id_lbl = tk.Label(admin_user_frame, text="User id", font=my_font, bg=NAVY, fg=TEXT)
admin_user_id_lbl.place(x=440, y=175)

admin_user_username_lbl = tk.Label(admin_user_frame, text="Username", font=my_font,bg=NAVY,fg=TEXT)
admin_user_username_lbl.place(x=440, y=235)

admin_user_password_lbl = tk.Label(admin_user_frame, text="Password", font=my_font, bg=NAVY, fg=TEXT)
admin_user_password_lbl.place(x=440, y=295)

admin_user_role_lbl = tk.Label(admin_user_frame, text="Role", font=my_font, bg=NAVY, fg=TEXT)
admin_user_role_lbl.place(x=440, y=355)


# #PAYMENT entries
admin_user_id_line = tk.Canvas(admin_user_frame, bg=label_color, width=120, height=2.0, highlightthickness=0)
admin_user_id_line.place(x=565, y=201)

admin_user_id_entry = tk.Entry(admin_user_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=13)
admin_user_id_entry.place(x=565, y=175)
# # =====================
admin_user_username_line = tk.Canvas(admin_user_frame, bg=label_color, width=120, height=2.0, highlightthickness=0)
admin_user_username_line.place(x=565, y=261)

admin_user_username_entry = tk.Entry(admin_user_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=13)
admin_user_username_entry.place(x=565, y=235)
# # =====================
admin_user_password_line = tk.Canvas(admin_user_frame, bg=label_color, width=120, height=2.0, highlightthickness=0)
admin_user_password_line.place(x=565, y=321)

admin_user_password_entry = tk.Entry(admin_user_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=13)
admin_user_password_entry.place(x=565, y=295)
# # =====================
admin_user_role_combo = ttk.Combobox(admin_user_frame, values=["Admin", "Mechanic", "Employee"],
                state="readonly", width=13, font = ("Segoe UI", 10), justify="center")

admin_user_role_combo.set("Choose Role")

admin_user_role_combo.place(x=565, y=355)



############################################################# USERS ACTION BUTTONS ###########################################################

admin_user_save_btn = tk.Button(admin_user_frame, text="Save", font=text_font, bg=button_color ,activebackground=button_color,
                                height=1, width=8, pady=6 , command=admin_user_save_click)
admin_user_save_btn.place(x=170, y=460)

admin_user_update_btn = tk.Button(admin_user_frame, text="Update", font=text_font, bg=button_color ,activebackground=button_color,
                                  height=1, width=8, pady=6, command=admin_user_update_click)
admin_user_update_btn.place(x=270, y=460)

admin_user_delete_btn = tk.Button(admin_user_frame, text="Delete", font=text_font, bg=button_color ,activebackground=button_color,
                                  height=1, width=8, pady=6, command=admin_user_remove_click)
admin_user_delete_btn.place(x=370, y=460)

admin_user_clear_btn = tk.Button(admin_user_frame, text="Clear", font=text_font, bg=button_color ,activebackground=button_color,
                                 height=1, width=8, pady=6, command=admin_user_clear_click)
admin_user_clear_btn.place(x=470, y=460)

admin_user_back_btn = tk.Button(
    admin_user_frame,text="← Back",bg=NAVY,fg=TEXT,activebackground=NAVY,activeforeground="white",
    borderwidth=0,cursor="hand2",font=back_btn_font, command=lambda :show_frame(admin_main_frame))
admin_user_back_btn.place(x=20, y=500)


# search part FOR Users
admin_user_search_lbl = tk.Label(admin_user_frame, text="Search by user id :", font=text_font , bg=NAVY, fg="white")
admin_user_search_lbl.place(x=15, y=110)

admin_user_search_ent = tk.Entry(admin_user_frame, width=8, bg="white", font=text_font)
admin_user_search_ent.place(x=185, y=112)

admin_user_search_btn = tk.Button(admin_user_frame, text="Search" , font=text_font, bg=button_color ,activebackground=button_color,
                                  command=admin_user_search_click)
admin_user_search_btn.place(x=280, y=107)

admin_user_show_btn = tk.Button(admin_user_frame, text="Show All", font=text_font, bg=button_color,activebackground=button_color ,
                                command=admin_user_show_click)
admin_user_show_btn.place(x=356, y=107)



# =================================================================================================================================================================================================================================================================================================
# ========================================================================================================================== CUSTOMER ACTION PAGE =================================================================================================================================================
# =================================================================================================================================================================================================================================================================================================



# CUSTOMER FRAMES

customer_sidebar = tk.Frame(customer_frame,bg="white")
customer_sidebar.place(x=0, y=0, width= 240, height=600)


customer_my_appointment_frame = tk.Frame(customer_frame,bg=NAVY)
customer_my_appointment_frame.place(x=240, y=60, width= 710, height=560)


customer_payment_frame = tk.Frame(customer_frame,bg=NAVY)
customer_payment_frame.place(x=240, y=60, width= 710, height=560)

customer_review_frame = tk.Frame(customer_frame,bg=NAVY)
customer_review_frame.place(x=240, y=60, width= 710, height=560)



# =========================================================================================================================  SIDEBAR BUTTONS  ===================================================================================================================================================

customer_menu = tk.Label(customer_sidebar, text="MENU", font =times_font , bg=back_blue, fg="black")
customer_menu.place(x=0, y=60, relwidth=1, height=40)

# =============================================================================================================================================

# MY APPOINTMENTS SIDEBAR BUTTON
customer_appointment_icon = Image.open("images\\appointment.png")
customer_appointment_icon = customer_appointment_icon.resize((40, 40))

photo = ImageTk.PhotoImage(customer_appointment_icon)

customer_appointment_button = tk.Button(customer_sidebar,text="My Appointments", image=photo, compound="left",
    anchor="w", # Aligns content to the left instead of centered
    padx=15, font=back_btn_font, bg="white", fg=NAVY, activebackground="white",relief="flat",borderwidth=0,
                                        command=lambda:show_frame(customer_my_appointment_frame))

customer_appointment_button.image = photo
customer_appointment_button.place(x=5, y=180)

# =============================================================================================================================================

# BOOK APPOINTMENTS SIDEBAR BUTTON
customer_book_appointment_icon = Image.open("images\\appointment.png")
customer_book_appointment_icon = customer_book_appointment_icon.resize((40, 40))

photo = ImageTk.PhotoImage(customer_book_appointment_icon)

customer_book_appointment_button = tk.Button(customer_sidebar,text="Book Appointment", image=photo, compound="left",
    anchor="w", # Aligns content to the left instead of centered
    padx=15, font=back_btn_font, bg="white", fg=NAVY, activebackground="white",relief="flat",borderwidth=0,
                                             command=open_customer_booking)

customer_book_appointment_button.image = photo
customer_book_appointment_button.place(x=5, y=260)


# =============================================================================================================================================

# PAYMENTS SIDEBAR BUTTON
customer_payment_icon = Image.open("images\\payment.png")
customer_payment_icon = customer_payment_icon.resize((40, 40))

photo = ImageTk.PhotoImage(customer_payment_icon)

customer_payment_button = tk.Button(customer_sidebar,text="Payments", image=photo, compound="left",
    anchor="w", # Aligns content to the left instead of centered
    padx=15, font=back_btn_font, bg="white", fg=NAVY, activebackground="white",relief="flat",borderwidth=0,
                                    command=lambda:show_frame(customer_payment_frame))

customer_payment_button.image = photo
customer_payment_button.place(x=5, y=340)

# =============================================================================================================================================

# REVIEWS SIDEBAR BUTTON
customer_review_icon = Image.open("images\\rating.png")
customer_review_icon = customer_review_icon.resize((40, 40))

photo = ImageTk.PhotoImage(customer_review_icon)

customer_review_button = tk.Button(customer_sidebar,text="Reviews", image=photo, compound="left",
    anchor="w", # Aligns content to the left instead of centered
    padx=15, font=back_btn_font, bg="white", fg=NAVY, activebackground="white",relief="flat",borderwidth=0,
                                   command=lambda:show_frame(customer_review_frame))

customer_review_button.image = photo
customer_review_button.place(x=5, y=420)


# =============================================================================================================================================

# EXIT SIDEBAR BUTTON
customer_exit_icon = Image.open("images\\exit.png")
customer_exit_icon = customer_exit_icon.resize((40, 40))

photo = ImageTk.PhotoImage(customer_exit_icon)

customer_exit_button = tk.Button(customer_sidebar,text="EXIT", image=photo, compound="left",
    anchor="w", # Aligns content to the left instead of centered
    padx=15, font=back_btn_font, bg="white", fg=NAVY, activebackground="white",relief="flat",borderwidth=0, command= lambda: show_frame(main_frame))

customer_exit_button.image = photo
customer_exit_button.place(x=5, y=530)


# =========================================================================================================================================================================================================================================================================================================
# ==================================================================================================================== CUSTOMER BOOK APPOINTMENT  ==========================================================================================================================================================

customer_book_appointment_top_lbl = tk.Label(customer_book_appointment_frame, text="Book Appointment", bg="white",
                                             fg="black" , font = ("times new roman",15))
customer_book_appointment_top_lbl.place(x=0, y=0, width= 710, height=23)

# =========================================================================================================== CUSTOMER BOOK APPOINTMENT FUNCTIONS  ==========================================================================================================================================================

def filter_services(event=None):

    keyword = customer_service_entry.get().lower().strip()

    customer_service_listbox.delete(0, END)

    if keyword == "":
        customer_service_listbox.place_forget()
        return

    found = False

    for service in all_services:

        if keyword in service.lower():

            customer_service_listbox.insert(END, service)

            found = True

    if found:
        customer_service_listbox.place(x=160, y=335)
    else:
        customer_service_listbox.place_forget()

def choose_service(event):

    selection = customer_service_listbox.curselection()

    if not selection:
        return

    service = customer_service_listbox.get(selection)

    customer_service_entry.delete(0, END)

    customer_service_entry.insert(0, service)

    customer_service_listbox.place_forget()


def customer_book_appointment_click():

    name = customer_name_entry.get()
    phone = customer_phone_entry.get()
    email = customer_email_entry.get()

    brand = vehicle_brand_ent.get()
    model = vehicle_model_ent.get()
    year = vehicle_year_ent.get()

    service_name = customer_service_entry.get()


    plate_number = (
            customer_plate_part1.get().strip() + " "
            + customer_plate_part2.get().strip() + " "
            + customer_plate_part3.get().strip() + " ایران "
            + customer_plate_part4.get().strip()
    )


    appointment_date = (
        customer_year_combo.get() + "-"
        + customer_month_combo.get() + "-"
        + customer_day_combo.get())

    appointment = AppointmentController()

    success, message = appointment.book_appointment(name=name, phone=phone, email=email, brand=brand, model=model,
                      year=year, plate_number=plate_number, service_name=service_name, appointment_date=appointment_date)

    if success:
        msg.showinfo("Success", message)
        customer_update_appointment_table(phone)
        admin_update_vehicle_table()
        admin_update_customer_table()
        admin_update_appointment_table()

        # deleting entries

        vehicle_brand_ent.delete(0, END)
        vehicle_model_ent.delete(0, END)
        vehicle_year_ent.delete(0, END)

        customer_plate_part1.delete(0, END)
        customer_plate_part2.delete(0, END)
        customer_plate_part3.delete(0, END)
        customer_plate_part4.delete(0, END)

        customer_year_combo.set("Year")
        customer_month_combo.set("Month")
        customer_day_combo.set("Day")

        customer_service_entry.delete(0, END)


    else:
        msg.showerror("Error", message)



#Customer labels


customer_name_lbl = tk.Label(customer_book_appointment_frame, text="Name", font=my_font,bg=NAVY,fg=TEXT)
customer_name_lbl.place(x=30, y=70)

customer_phone_lbl = tk.Label(customer_book_appointment_frame, text="Phone Number", font=my_font, bg=NAVY, fg=TEXT)
customer_phone_lbl.place(x=30, y=130)

customer_email_lbl = tk.Label(customer_book_appointment_frame, text="Email", font=my_font, bg=NAVY, fg=TEXT)
customer_email_lbl.place(x=30, y=190)

#customer entries

customer_name_line = tk.Canvas(customer_book_appointment_frame, bg=label_color, width=120, height=2.0, highlightthickness=0)
customer_name_line.place(x=170, y=96)

customer_name_entry = tk.Entry(customer_book_appointment_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=13)
customer_name_entry.place(x=170, y=70)

customer_phone_line = tk.Canvas(customer_book_appointment_frame, bg=label_color, width=120, height=2.0, highlightthickness=0)
customer_phone_line.place(x=170, y=156)

customer_phone_entry = tk.Entry(customer_book_appointment_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=13)
customer_phone_entry.place(x=170, y=130)


customer_email_line = tk.Canvas(customer_book_appointment_frame, bg=label_color, width=150, height=2.0, highlightthickness=0)
customer_email_line.place(x=170, y=216)

customer_email_entry = tk.Entry(customer_book_appointment_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=16)
customer_email_entry.place(x=170, y=190)




vehicle_brand_lbl = tk.Label(customer_book_appointment_frame, text="Brand", font=my_font, bg=NAVY, fg=TEXT)
vehicle_brand_lbl.place(x=390, y=70)

vehicle_model_lbl = tk.Label(customer_book_appointment_frame, text="Model", font=my_font, bg=NAVY, fg=TEXT)
vehicle_model_lbl.place(x=390, y=130)

vehicle_year_lbl = tk.Label(customer_book_appointment_frame, text="Year", font=my_font, bg=NAVY, fg=TEXT)
vehicle_year_lbl.place(x=390, y=190)

customer_plate_lbl = tk.Label(customer_book_appointment_frame, text="Plate Number", font=my_font, bg=NAVY, fg=TEXT)
customer_plate_lbl.place(x=390, y=250)



vehicle_brand_ent = tk.Entry(customer_book_appointment_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=10)
vehicle_brand_ent.place(x=490, y=70)

vehicle_brand_ent_line = tk.Canvas(customer_book_appointment_frame, bg=label_color, width=80, height=2.0, highlightthickness=0)
vehicle_brand_ent_line.place(x=490, y=96)

# =======

vehicle_model_ent = tk.Entry(customer_book_appointment_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=10)
vehicle_model_ent.place(x=490, y=130)

vehicle_model_ent_line = tk.Canvas(customer_book_appointment_frame, bg=label_color, width=80, height=2.0, highlightthickness=0)
vehicle_model_ent_line.place(x=490, y=156)

# =======

vehicle_year_ent = tk.Entry(customer_book_appointment_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=10)
vehicle_year_ent.place(x=490, y=190)


vehicle_year_ent_line = tk.Canvas(customer_book_appointment_frame, bg=label_color, width=80, height=2.0, highlightthickness=0)
vehicle_year_ent_line.place(x=490, y=216)

# # =======


customer_plate_part1 = tk.Entry(customer_book_appointment_frame, bg="white", fg=NAVY, highlightthickness=0,font=text_font, width=2)
customer_plate_part1.place(x=510, y=251)

customer_plate_part2 = tk.Entry(customer_book_appointment_frame, bg="white", fg=NAVY, highlightthickness=0,font=text_font, width=3)
customer_plate_part2.place(x=540, y=251)

customer_plate_part3 = tk.Entry(customer_book_appointment_frame, bg="white", fg=NAVY, highlightthickness=0,font=text_font, width=3)
customer_plate_part3.place(x=575, y=251)

customer_plate_part4 = tk.Entry(customer_book_appointment_frame, bg="white", fg=NAVY, highlightthickness=0,font=text_font, width=2)
customer_plate_part4.place(x=610, y=251)

# ===================================================================

# ---------- Auto Move Customer Plate ----------

customer_plate_part1.bind(
    "<KeyRelease>", lambda e: move_next(e, customer_plate_part1, customer_plate_part2, 2))

customer_plate_part2.bind(
    "<KeyRelease>", lambda e: move_next(e, customer_plate_part2, customer_plate_part3, 1))

customer_plate_part3.bind("<KeyRelease>",
                          lambda e: move_next(e, customer_plate_part3, customer_plate_part4, 3))

# ---------- Backspace ----------

customer_plate_part2.bind("<KeyPress>",
    lambda e: move_previous(e, customer_plate_part2, customer_plate_part1))

customer_plate_part3.bind("<KeyPress>",
    lambda e: move_previous(e, customer_plate_part3, customer_plate_part2))

customer_plate_part4.bind("<KeyPress>",
    lambda e: move_previous(e, customer_plate_part4, customer_plate_part3))



# ===================================================================

# ===========

customer_appointment_date_lbl = tk.Label(customer_book_appointment_frame, text="Appointment Date", font=my_font, bg=NAVY, fg=TEXT)
customer_appointment_date_lbl.place(x=30, y=390)


customer_year_combo = ttk.Combobox(customer_book_appointment_frame,values=[str(y) for y in range(2025, 2031)], state="readonly", width=6)
customer_year_combo.place(x=190, y=393)
customer_year_combo.set("Year")

customer_month_combo = ttk.Combobox(customer_book_appointment_frame, values=[f"{m:02d}" for m in range(1, 13)], state="readonly", width=6)
customer_month_combo.place(x=260, y=393)
customer_month_combo.set("Month")

customer_day_combo = ttk.Combobox(customer_book_appointment_frame, values=[f"{d:02d}" for d in range(1, 32)], state="readonly", width=5)
customer_day_combo.place(x=330, y=393)
customer_day_combo.set("Day")

# ================================
# SERVICE SEARCH
# ================================

customer_service_name_lbl = tk.Label(customer_book_appointment_frame, text="Service Name", font=my_font,bg=NAVY,fg=TEXT)
customer_service_name_lbl.place(x=30, y=300)

customer_service_entry = tk.Entry(customer_book_appointment_frame, bg=NAVY, fg=TEXT, highlightthickness=0, relief="flat"
                                      ,font=text_font, width=14)
customer_service_entry.place(x=160, y=302)

customer_service_line = tk.Canvas(customer_book_appointment_frame, bg=label_color, width=150, height=2.0, highlightthickness=0)
customer_service_line.place(x=160, y=328)

customer_service_entry.bind("<KeyRelease>", filter_services)

customer_service_listbox = tk.Listbox(customer_book_appointment_frame,width=20,height=4,font=text_font)
customer_service_listbox.place(x=160, y=335)

customer_service_listbox.place_forget()

service_controller = ServiceController()
all_services = service_controller.get_all_service_names()

customer_service_listbox.bind("<<ListboxSelect>>", choose_service)
# ===========
book_appointment_btn = tk.Button(customer_book_appointment_frame, text="Book Appointment", font=text_font, bg=button_color
                                ,activebackground=button_color, height=1, width=25, pady=6 ,command=customer_book_appointment_click)
book_appointment_btn.place(x=220, y=460)



# ===================================================================================================================================================================================================================================================================================================

# =============================================================================================================== CUSTOMER MY APPOINTMENT  ==========================================================================================================================================================

customer_my_appointment_top_lbl = tk.Label(customer_my_appointment_frame, text="My Appointments", bg="white", fg="black" , font = ("times new roman",15))
customer_my_appointment_top_lbl.place(x=0, y=0, width= 710, height=23)

# =========================================================================================================== CUSTOMER MY APPOINTMENT FUNCTIONS  ==========================================================================================================================================================


def customer_update_appointment_table(phone):

    appointment = AppointmentController()

    rows = appointment.get_customer_appointments(phone)

    customer_appointment_table.delete(*customer_appointment_table.get_children())

    for row in rows:
        customer_appointment_table.insert("", "end", values=row)


def cancel_my_appointment_click():
    """
    customer canceling their appointment by selecting appointment row
    """
    global logged_in_customer

    selected = customer_appointment_table.focus()

    if not selected:
        msg.showerror("Error", "Please select an appointment")
        return

    values = customer_appointment_table.item(selected)["values"]

    appointment_id = values[0]

    appointment = AppointmentController()

    status,message = appointment.cancel_appointment(appointment_id)

    if status:
        msg.showinfo("Appointment got Cancelled", message)
        customer_update_appointment_table(logged_in_customer["phone"])
        admin_update_appointment_table()
        update_dashboard()

    else:
        msg.showerror("Error", message)




customer_appointment_table = ttk.Treeview(customer_my_appointment_frame, columns=(1,2,3,4,5), show="headings", height=8)

customer_appointment_table.heading(1, text="Appointment ID")
customer_appointment_table.heading(2, text="Appointment Date")
customer_appointment_table.heading(3, text="Vehicle")
customer_appointment_table.heading(4, text="Service")
customer_appointment_table.heading(5, text="Status")

customer_appointment_table.column(1, width=100, anchor="center")
customer_appointment_table.column(2, width=120, anchor="center")
customer_appointment_table.column(3, width=130, anchor="center")
customer_appointment_table.column(4, width=150, anchor="center")
customer_appointment_table.column(5, width=130, anchor="center")


customer_appointment_table.place(x=0, y=180, relwidth=1)



# ===========
cancel_my_appointment_btn = tk.Button(customer_my_appointment_frame, text="Cancel Appointment", font=text_font, bg=button_color
                                ,activebackground=button_color, height=1, width=27, pady=6 ,command=cancel_my_appointment_click)
cancel_my_appointment_btn.place(x=220, y=460)



# ===================================================================================================================================================================================================================================================================================================

# =============================================================================================================== CUSTOMER PAYMENT  ==========================================================================================================================================================

customer_my_appointment_top_lbl = tk.Label(customer_payment_frame, text="My Payments", bg="white", fg="black" , font = ("times new roman",15))
customer_my_appointment_top_lbl.place(x=0, y=0, width= 710, height=23)

# ===================================================================================================================================================================================================================================================================================================


def customer_update_payment_table(phone):

    payment = PaymentController()

    rows = payment.get_customer_payments(phone)

    customer_payment_table.delete(*customer_payment_table.get_children())

    for row in rows:
        customer_payment_table.insert("","end",values=row)





customer_payment_table = ttk.Treeview(
    customer_payment_frame,
    columns=(1,2,3,4,5),
    show="headings"
)

customer_payment_table.heading(1,text="Payment ID")
customer_payment_table.heading(2,text="Appointment Date")
customer_payment_table.heading(3,text="Service")
customer_payment_table.heading(4,text="Price")
customer_payment_table.heading(5,text="Status")


customer_payment_table.column(1, width=90, anchor="center")
customer_payment_table.column(2, width=120, anchor="center")
customer_payment_table.column(3, width=110, anchor="center")
customer_payment_table.column(4, width=110, anchor="center")
customer_payment_table.column(5, width=110, anchor="center")

customer_payment_table.place(x=0, y=180, relwidth=1)






# ===================================================================================================================================================================================================================================================================================================

# =============================================================================================================== CUSTOMER REVIEW  ==========================================================================================================================================================

customer_my_appointment_top_lbl = tk.Label(customer_review_frame, text="Review", bg="white", fg="black" , font = ("times new roman",15))
customer_my_appointment_top_lbl.place(x=0, y=0, width= 710, height=23)

# ===================================================================================================================================================================================================================================================================================================



def customer_submit_review_click():

    global logged_in_customer

    rating = customer_rating_combo.get()

    comment = customer_comment_text.get("1.0",END).strip()


    review = ReviewController()

    success,message = review.customer_add_review(logged_in_customer["phone"], rating, comment)

    if success:

        msg.showinfo("Success",message)

        customer_rating_combo.set("Rating")

        customer_comment_text.delete("1.0",END)
        admin_update_review_table()

    else:

        msg.showerror("Error",message)



customer_rating_lbl = tk.Label(customer_review_frame,text="Rate your experience :", font=my_font, bg=NAVY, fg=TEXT)
customer_rating_lbl.place(x=20,y=100)

customer_rating_combo = ttk.Combobox(customer_review_frame, values=["1","2","3","4","5"], state="readonly")

customer_rating_combo.set("Rating")
customer_rating_combo.place(x=250,y=108)

customer_comment_lbl = tk.Label(customer_review_frame,text="Comment section", font=my_font, bg=NAVY, fg=TEXT)
customer_comment_lbl.place(x=260,y=190)

customer_comment_text = tk.Text(customer_review_frame, width=50, height=10, bg="#A9B9E0",bd=5)
customer_comment_text.place(x=120,y=230)


submit_review_btn = tk.Button(customer_review_frame, text="Submit Review", font=text_font, bg=button_color
                        ,activebackground=button_color, height=1, width=18, pady=6, command=customer_submit_review_click)
submit_review_btn.place(x=255,y=465)






win.mainloop()