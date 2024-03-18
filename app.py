from flask import Flask, request, jsonify, render_template,session
import os
from custom_functions import *
import json
import sqlite3
from flask import Flask, render_template, redirect, url_for, flash
from insert_fun import *
from datetime import datetime, timedelta
from email_sender import send_email  # Assuming you have a separate module for sending emails
import string,random
app = Flask(__name__)
app.secret_key = '34'


#=====================================================================
            # MAIN LOGIN
#=====================================================================


@app.route("/")
def loginregister():
    return render_template("loginregister.html")
@app.route("/homepage")
def homepage():
    return render_template("homepage.html")
# ======================LogIn==============================

@app.route("/loginform")
def loginform():
    return render_template('login.html')

@app.route('/mainpage', methods=['POST'])
def login():
    if request.method == 'POST':
        print("completed")

        
        # If the request is not JSON, assume it's HTML form data
        usernameentered = request.form.get('username')
        passwordentered = request.form.get('password')
        if request.is_json:
            # If the request is JSON, handle it accordingly
            data = request.get_json()
            usernameentered = data.get('username')
            passwordentered = data.get('password')

        connection = sqlite3.connect('kdb.db')
        cursor = connection.cursor()

        query = "SELECT Username, Password FROM User WHERE Username=? AND Password=?"
        cursor.execute(query, (usernameentered, passwordentered))

        result = cursor.fetchall()

        connection.close()
        

        if len(result) == 0:
            flash('Login Unsuccessful. Please check your username and password', 'danger')
            return redirect(url_for('loginform'))
        else:
            flash("Login successful", "success")
            return redirect(url_for('homepage'))

# ======================Register============================
@app.route('/register', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        conn = sqlite3.connect('kdb.db')
        cursor = conn.cursor()
        emailentered = request.form.get('email')
        usernameentered = request.form.get('username')
        passwordentered = request.form.get('password')
        cursor.execute('SELECT * FROM User WHERE EmailId=? OR Username=?', (emailentered, usernameentered))
        existing_user = cursor.fetchone()
        if existing_user:
            conn.close()
            flash('Email or username already exists', 'error')
            return redirect(url_for('index'))
        cursor.execute('''
            INSERT INTO User (EmailId, Password, Username)
            VALUES (?, ?, ?)
        ''', (emailentered, usernameentered, passwordentered))
        conn.commit()
        conn.close()
        flash('Registration successful', 'success')
        return redirect(url_for('loginform'))
    return render_template('register.html')

#=====================================================================
            #Tenant signup and login
#=====================================================================

@app.route('/tenant_signup')
def tenant_signup():
    return render_template("tenant_info.html")
@app.route('/add_tenant_info', methods=['POST'])
def add_tenant_info():
    content_type = request.headers.get('Content-Type')
    plans = get_plans()  # Placeholder, replace with actual logic

    if content_type == 'application/json':
        data = request.json
    elif content_type in ['application/x-www-form-urlencoded', 'application/x-www-form-urlencoded; charset=UTF-8']:
        data = request.form
        current_date = datetime.now().strftime("%Y-%m-%d")

        print("plan", data['plan'])
        if data['plan'] != None:
            conn = sqlite3.connect("kdb.db")
            cursor = conn.cursor()
            cursor.execute("SELECT plan_duration_days FROM plan_mst WHERE plan_name=?", (data['plan'],))
            plan_duration_days = cursor.fetchone()
            print("plan duration days:", plan_duration_days)
            plan_duration_days_count=int(plan_duration_days[0])
            conn.commit()
            conn.close()
        # Check if plan_duration_days is not None before adding it to the current date
        if plan_duration_days is not None:
            plan_duration_days = int(plan_duration_days[0])
            expire_date = (datetime.now() + timedelta(days=plan_duration_days_count)).strftime("%Y-%m-%d")
        else:
            # Handle the case when plan_duration_days is None
            expire_date = None

        print("expire_date:", expire_date)

        # Check if the email already exists
        conn = sqlite3.connect("kdb.db")
        cursor = conn.cursor()
        tenant_mail_to_check = data.get('tenant_mail')
        plans = get_plans()

        cursor.execute("SELECT COUNT(*) FROM tenant_info WHERE tenant_mail=?", (tenant_mail_to_check,))
        count = cursor.fetchone()[0]

        if count != 0:
            conn.close()
            return jsonify({'error': 'Email already exists'}), 400


        try:
            cursor.execute('''
                INSERT INTO tenant_info 
                (tenant_mail, password_hash, password_hint, tenant_name, tenant_mobile, alternative_mobile, location, biz_name, est_date, dob, gender,
                domain_name, plan, pincode, referred_by, referral_code, self_referral, created_date, expire_date, plan_duration, has_branches)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                data.get('tenant_mail'), data.get('password_hash'), data.get('password_hint'), data.get('tenant_name'),
                data.get('tenant_mobile'), data.get('alternative_mobile'), data.get('location'), data.get('biz_name'), data.get('est_date'),
                data.get('dob'), data.get('gender'), data.get('domain_name'), data.get('plan'), data.get('pincode'),
                data.get('referred_by'), data.get('referral_code'), bool(data.get('self_referral')), current_date,
                expire_date, plan_duration_days_count,  # Use plan_duration_days instead of data.get('plan_duration')
                data.get('has_branches')
            ))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Database Error: {e}")
            return jsonify({'error': f'Database Error: {e}'}), 500
        finally:
            conn.close()

        # Set the session variable
        session['tenant_mail'] = data.get('tenant_mail')

        # Redirect to the add_branch route
        return redirect("/tenant_login_page")

    else:
        return jsonify({'error': 'Unsupported content type'}), 400
# ==================== Login for tenant====================
        
@app.route('/tenant_login_page')
def tenant_login_page():
    return render_template("tenantlogin.html")
import logging
@app.route('/tenant_login', methods=['POST'])
def tenant_login():
    content_type = request.headers.get('Content-Type')

    if content_type == 'application/json':
        data = request.json
    elif content_type in ['application/x-www-form-urlencoded', 'application/x-www-form-urlencoded; charset=UTF-8']:
        data = request.form
    else:
        return jsonify({'error': 'Unsupported content type'}), 400

    tenant_mail_input = data.get('tenant_mail')
    password_hash_input = data.get('password_hash')

    with sqlite3.connect('kdb.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tenant_info WHERE tenant_mail=? AND password_hash=?",
                       (tenant_mail_input, password_hash_input))
        result = cursor.fetchone()

    if result:
        tenant_mail_index = result[1]
        session['tenant_mail'] = tenant_mail_index
        session['tenant_id'] = result[0]
        print("tenant_id",session['tenant_id'],session['tenant_mail'])
        logging.info(f"Login successful for tenant: {tenant_mail_index}")
        return redirect("/branch_login_page")
    else:
        logging.warning(f"Login failed for tenant: {tenant_mail_input}")
        return jsonify({'error': 'Invalid credentials'}), 401
DATABASE="kdb.db"
def get_all_tenants():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tenant_info")
        columns = [col[0] for col in cursor.description]
        tenants = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return tenants

# Route to get all tenants
@app.route('/get_all_tenants', methods=['GET'])
def get_tenants():
    try:
        tenants = get_all_tenants()
        return jsonify({'tenants': tenants})
    except Exception as e:
        return jsonify({'error': str(e)})
@app.route("/get_tenants_details")
def get_tenants_details():
    return render_template("all_tenant_table.html")
#=====================================================================
            #Branch singup and Login and transaction and add branch services 
#=====================================================================


#=====================Branch Login======================

# Branch login routes
@app.route('/branch_login_page')
def branch_login_page():
    return render_template("branchlogin.html")
from flask import flash

@app.route('/branch_login', methods=['POST'])
def branch_login():
    content_type = request.headers.get('Content-Type')

    if content_type == 'application/json':
        data = request.json
    elif content_type in ['application/x-www-form-urlencoded', 'application/x-www-form-urlencoded; charset=UTF-8']:
        data = request.form
    else:
        flash('Unsupported content type', 'error')
        return redirect('/branch_login_page')

    username = data.get('username')
    password = data.get('password')

    with sqlite3.connect('kdb.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM branch_table WHERE username=? AND password=?", (username, password))
        result = cursor.fetchone()

    if result:
        logging.info(f"Login successful for branch: {username}")
        session['branch_id'] = result[1]  # Assuming branch_id is in the first position in the result
        session['branch_name'] = result[2]
        flash('Login successful', 'success')
        return redirect("/customer_searchbar")
    else:
        logging.warning(f"Login failed for branch: {username}")
        flash('Invalid credentials', 'error')
        return redirect('/branch_login_page')

def generate_random_code():
    return ''.join(random.choices(string.digits, k=6))
def code_exists_in_database(code, cursor, table_name, column_name):
    cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE {column_name}=?", (code,))
    count = cursor.fetchone()[0]
    return count > 0
# def generate_random_code():
#     return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
@app.route("/branch_signup")
def branch_signup():
    return render_template("add_branch.html")
@app.route('/add_branch_info', methods=['POST'])
def add_branch_info():
    content_type = request.headers.get('Content-Type')

    if content_type in ['application/x-www-form-urlencoded', 'application/x-www-form-urlencoded; charset=UTF-8']:
        data = request.form
        s_tenant_mail = session.get('tenant_mail')
        s_tenant_id = session.get('tenant_id')

        if s_tenant_id is not None:
            conn = sqlite3.connect("kdb.db")
            cursor = conn.cursor()
            cursor.execute("SELECT expire_date, plan_duration FROM tenant_info WHERE tenant_id=?", (s_tenant_id,))
            result = cursor.fetchone()
            expire_date, plan_duration = result[0], result[1]
            conn.commit()
            conn.close()

            if s_tenant_mail is None or s_tenant_id is None:
                return jsonify({'error': 'Tenant mail or tenant ID not found in session'}), 400

            with sqlite3.connect('kdb.db') as conn:
                cursor = conn.cursor()

                random_branch_id = generate_random_code()

                while code_exists_in_database(random_branch_id, cursor, 'branch_table', 'branch_id'):
                    random_branch_id = generate_random_code()
                
                # Insert data into the branch_table
                cursor.execute('''
                    INSERT INTO branch_table 
                    (branch_id, tenant_id, branch_name, username, password, plan_duration, plan_expiry_date)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    random_branch_id,
                    s_tenant_id,
                    data.get('branch_name'),
                    data.get('username'),
                    data.get('password'),
                    plan_duration,
                    expire_date,
                ))
                conn.commit()
                return redirect("/branch_login_page")


        return jsonify({'error': 'Tenant not found for the given mail'}), 400
    else:
        return jsonify({'error': 'Unsupported content type'}), 400

# Function to execute SQL query and fetch all branches
# Function to get all branches from the database
def get_all_branches():
    with sqlite3.connect(DATABASE) as conn:
        # tenant_id=session['tenant_id']
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM branch_table")
        # cursor.execute("SELECT * FROM branch_table WHERE tenant_id=?",(tenant_id))
        columns = [col[0] for col in cursor.description]
        branches = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return branches

# Route to render the HTML page
@app.route("/get_all_branches")
def get_all_branches_html():
    return render_template("all_branches_table.html")

# Route to fetch all branches as JSON
@app.route('/fetch_all_branches', methods=['GET'])
def get_branches():
    try:
        branches = get_all_branches()
        return jsonify({'branches': branches})
    except Exception as e:
        return jsonify({'error': str(e)})

from flask import session, redirect, url_for

# Existing code ...

@app.route('/branch_logout')
def branch_logout():
    # Clear branch-related session variables
    session.pop('branch_id', None)
    session.pop('branch_name', None)

    # Redirect to the branch login page or any other desired page
    return redirect(url_for('branch_login_page'))


#=====================================================================
            #Customer added to branch
#=====================================================================

@app.route("/add_customer_to_branch")
def add_customer_to_branch():
    # Your logic to fetch and display customer information goes here
    return render_template("cust_info.html")
def generate_cust_id_random():
    return ''.join(random.choices(string.digits, k=6))

def cust_id_exists_in_database(code, cursor, table_name, column_name):
    cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE {column_name}=?", (code,))
    count = cursor.fetchone()[0]
    return count > 0

@app.route('/add_cust_info', methods=['POST'])
def add_cust_info():
    content_type = request.headers.get('Content-Type')

    if content_type == 'application/json':
        data = request.json
    elif content_type in ['application/x-www-form-urlencoded', 'application/x-www-form-urlencoded; charset=UTF-8']:
        data = request.form
    else:
        return jsonify({'error': 'Unsupported content type'}), 400
    
    cust_id = generate_cust_id_random()
    print(cust_id)
    session['cust_id']=cust_id

    try:
        conn = sqlite3.connect("kdb.db")
        cursor = conn.cursor()

        # Check if the generated cust_id already exists in the cust_mst table
        while cust_id_exists_in_database(cust_id, cursor, 'cust_mst', 'cust_id'):
            cust_id = generate_cust_id_random()
        
        new_customer = {
            "tenant_id": session.get('tenant_id'),
            "branch_id": session.get('branch_id'),
            "branch_name": session.get('branch_name'),
            "cust_id": cust_id,
            "cust_name": data.get('cust_name'),
            "cust_mail": data.get('cust_mail'),
            "cust_mobile": data.get('cust_mobile'),
            "cust_whatsapp_number": data.get('cust_whatsapp_number'),
            "cust_age": data.get('cust_age'),
            "cust_gender": data.get('cust_gender'),
            "cust_location": data.get('cust_location'),
            "cust_pincode": data.get('cust_pincode')
        }

        cursor.execute('''
            INSERT INTO cust_mst 
            (tenant_id, branch_id, branch_name, cust_id, cust_name, cust_mail, cust_mobile,
            cust_whatsapp_number, cust_age, cust_gender, cust_location, cust_pincode)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            new_customer["tenant_id"], new_customer["branch_id"], new_customer["branch_name"],
            new_customer["cust_id"], new_customer["cust_name"], new_customer["cust_mail"],
            new_customer["cust_mobile"], new_customer["cust_whatsapp_number"],
            new_customer["cust_age"], new_customer["cust_gender"],
            new_customer["cust_location"], new_customer["cust_pincode"]
        ))
        conn.commit()
        print("Session cust_id",session['cust_id'])
        print("branch id ")
        return render_template("customer_tnx.html", s_cust_id=session['cust_id'])

    except sqlite3.Error as e:
        print("SQLite error:", e)
        return jsonify({'error': 'Database error'}), 500
    finally:
        if conn:
            conn.close()
def classify_user():
    conn=sqlite3.connect("kdb.db")
    cursor=conn.cursor()
    tenant_id=session['tenant_id']
    try:
        cursor.execute("SELECT branch_id FROM branch_table WHERE tenant_id=?",tenant_id)
        data=cursor.fetchone()
        cursor.commit()
        cursor.close()
        if data:
            return {"user_type":"branch"}
        else:
            return {"user_type":None}
    except:
        cursor.execute("SELECT tenant_mail FROM WHERE tenant_info WHERE tenant_id=?", tenant_id)
        data=cursor.fetchone()

        cursor.commit()
        cursor.close()
        if data:
            return {"user_type":"tenant"}
        else:
            return {"user_type":None}

#===============================================================================
           # CustomerTransaction_Details
#===============================================================================

@app.route("/add_customer_tnx")
def add_customer_tnx():
    s_cust_id=session['cust_id']
    return render_template("customer_tnx.html",s_cust_id=s_cust_id)

def customername_mobile():
    conn = sqlite3.connect('kdb.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * from cust_mst where cust_id=?",(session['cust_id'],))
    result=cursor.fetchall()
    print("cust_id",result[0][3])
    print("cust_name",result[0][4])
    print("cust Mobile",result[0][6])
    print("branch_id",result[0][0])
    conn.commit()
    conn.close()
    return result
# Define the add_transaction route
from datetime import datetime 
@app.route('/add_customer_transaction', methods=['POST'])
def add_customer_transaction():
    try:
        # Check the content type of the request
        current_date=datetime.now()
        content_type = request.headers.get('Content-Type')
        def generate_uuid():
            # Generate a UUID and return it as a string
            return str(uuid.uuid4())

        # Usage example:
        uuid_value = generate_uuid()
        print("Generated UUID:", uuid_value)
        if content_type == 'application/json':
            # If the content type is JSON, parse JSON data
            data = request.json

        elif ((content_type == 'application/x-www-form-urlencoded') or (content_type=='application/x-www-form-urlencoded; charset=UTF-8')):
            data = {
                'transaction_id':uuid_value,
                'branch_id':session['branch_id'],
                'Customer_id': session['cust_id'],
                'Service_name': request.form.get('service_dropdown'),
                'Remainder_days': request.form.get('remainder_days'),
                'Current_date': current_date,
                'Current_service_remark': request.form.get('current_service_remark'),
                'Payment_Mode': request.form.get('payment_mode'),
                'Paid_amount': request.form.get('paid_amount'),
                'Discount': request.form.get('discount'),
                'Location': request.form.get('location')
            }
        else:
            return jsonify({'error': 'Unsupported content type'}), 400

        conn = sqlite3.connect('kdb.db')
        cursor = conn.cursor()
        cust=customername_mobile()


        # Customer_id exists, fetch Customer_name and Customer_mobile
        customer_name, customer_mobile = cust[0][4],cust[0][6]
        # Insert transaction data into Customer_Transaction_DB
        cursor.execute('''
            INSERT INTO Customer_Transaction_DB (
                transaction_id,
                branch_id,
                Customer_id,
                Customer_name,
                Customer_mobile,
                Service_name,
                Remainder_days,
                Current_date,
                Current_service_remark,
                Payment_Mode,
                Paid_amount,
                Discount,
                Location
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            data['transaction_id'],
            data['branch_id'],
            data['Customer_id'],
            customer_name,
            customer_mobile,
            data['Service_name'],
            data['Remainder_days'],
            data['Current_date'],
            data['Current_service_remark'],
            data['Payment_Mode'],
            data['Paid_amount'],
            data['Discount'],
            data['Location']
        ))


        conn.commit()
        conn.close()
        return redirect("/customers_tnx")
    except Exception as e:
        print("Error:", str(e))
        return jsonify({'error': str(e)}), 400
    
#===================================== add services services

@app.route('/get_services', methods=['GET'])
def get_services():
    branch_id = session.get('branch_id')
    if branch_id:
        conn = sqlite3.connect("kdb.db")
        cursor = conn.cursor()

        cursor.execute('SELECT service_name FROM skus WHERE branch_id=?', (branch_id,))
        services = [{'service_name': row[0]} for row in cursor.fetchall()]

        conn.commit()
        conn.close()

        return jsonify({'services': services})

    return jsonify({'error': 'Branch ID not found'})



@app.route('/add_branch_services')
def add_branch_services():
    return render_template("add_branch_services.html")
@app.route("/add_branch_services_data" ,methods=['POST'])
def add_branch_services_data():
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect("kdb.db")
        cursor = connection.cursor()
        created_date= datetime.now().strftime("%d-%m-%Y")
        tenant_id=session['tenant_id']
        branch_id=session['branch_id']
        print("branch Id:",branch_id)
        content_type = request.headers.get('Content-Type')

        print(content_type)
        if content_type == 'application/json':
            # If the content type is JSON, parse JSON data
            data = request.json
        elif content_type.startswith('application/x-www-form-urlencoded'):
            data={       # Get data from the form
        "tenant_id" : tenant_id,
        "branch_id" : branch_id,
        "service_name":request.form['service_name'],
        "is_active" : request.form.get('is_active', 0) , # 1 if checked, 0 if not checked
        "selling_price" : request.form['selling_price'],
        "mrp" : request.form['mrp'],
        "service_category" : request.form['service_category'],
        "service_code" : request.form['service_code'],
        "created_date" : created_date,
        "modified_date" : request.form['modified_date'],
        "modified_by" : request.form['modified_by']
        }
        else:
            return jsonify({'error': 'Unsupported content type'}), 400



        # SQL query to insert data into the table
        insert_query = """
            INSERT INTO skus
            (tenant_id, branch_id, is_active, selling_price, mrp, service_name, service_category,service_code, created_date, modified_date, modified_by)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?);
        """

        # Execute the query with data
        cursor.execute(insert_query, (tenant_id, branch_id, data['is_active'], data['selling_price'], data['mrp'],data['service_name'], data ['service_category'], data['service_code'], created_date, data['modified_date'], data['modified_by']))
        # Commit the changes
        connection.commit()
        return redirect("/customer_searchbar")

    except Exception as e:
        return f'Error inserting data: {e}'

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

#=====================================================================
            #client_intimation
#=====================================================================

import sqlite3
# Celery task to process plans

def process_plans():
    past_three_days = datetime.now().date() - timedelta(days=3)
    future_three_days = datetime.now().date() + timedelta(days=3)
    conn = sqlite3.connect("kdb.db")
    cursor = conn.cursor()

    # Fetch clients with plans in the past 3 days
    cursor.execute('SELECT email_id, plan_duration FROM client_info WHERE Expire_date >= ? AND Expire_date < ?', (past_three_days, datetime.now().date()))
    expired_clients = cursor.fetchall()
    print("expire_client",expired_clients)
    conn.commit()
    conn.close()

    for client in expired_clients:
        email_id, plan_duration = client
        message = f"Dear {email_id}, your plan has expired. Please renew your subscription."
        send_email(email_id, "Plan Expiration Notification", message)

    # Fetch clients with plans in the next 3 days
    cursor.execute('SELECT email_id, plan_duration FROM client_info WHERE Expire_date > ? AND Expire_date <= ?', (datetime.now().date(), future_three_days))
    upcoming_clients = cursor.fetchall()

    for client in upcoming_clients:
        email_id, plan_duration = client
        message = f"Dear {email_id}, your plan will expire soon. Please renew your subscription."
        send_email(email_id, "Upcoming Plan Notification", message)


#=====================================================================
            #customer_transaction_based on branch_id
#=====================================================================



@app.route("/customers_tnx")
def customers_tnx():
    try:
        # Open a connection to the database
        conn = sqlite3.connect("kdb.db")
        cursor = conn.cursor()

        # Fetch customer transactions based on branch_id
        branch_id = session.get('branch_id')
        cursor.execute('''
            SELECT 
                transaction_id, 
                branch_id,
                Customer_id,
                Customer_name,
                Customer_mobile,
                Service_name,
                Remainder_days,
                Current_date,
                Current_service_remark,
                Payment_Mode,
                Paid_amount,
                Discount,
                Location
            FROM Customer_Transaction_DB
            WHERE branch_id = ? 
        ''', (branch_id,))

        transactions = cursor.fetchall()

        # Close the database connection
        conn.close()

        # Render the template with customer transaction information
        return render_template("customers_tnx.html", transactions=transactions)

    except sqlite3.Error as e:
        print("SQLite error:", e)
        return jsonify({'error': 'Database error'}), 500



#===========================e======================================
                #Client_info
#===================================================================


# Route to host the client information input page
@app.route('/client_info_form')
def client_info_form():
    return render_template('client_info.html')

# Function to insert client_info data into the database


#===============================================================================
           #ADD PLAN
#===============================================================================
@app.route("/add_plan_page")
def add_plan_page():
    return render_template("add_plan.html")

@app.route('/add_plan', methods=['POST'])
def add_plan():
    try:

        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            data = request.json
        elif content_type in ['application/x-www-form-urlencoded', 'application/x-www-form-urlencoded; charset=UTF-8']:
            data = request.form
        else:
            return jsonify({'error': 'Unsupported content type'}), 400
        conn = sqlite3.connect('kdb.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO plan_mst (
                plan_name, plan_amount, discount, plan_duration_days,
                enable_SMS_reminder, enable_whatsapp_reminder,
                enable_basic_dashboard, enable_advanced_dashboard,
                enable_monthly_reports, enable_weekly_reports,
                data_download_permission, created_date, created_by
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            data['planname'], data['planamount'], data['discount'],
            data['plandurationdays'], data['enablesmsreminder'],
            data['enablewhatsappreminder'], data['enablebasicdashboard'],
            data['enableadvanceddashboard'], data['enablemonthlyreports'],
            data['enableweeklyreports'], data['datadownloadpermission'],
            data['createddate'], data['createdby']
        ))

        conn.commit()
        conn.close()
        return jsonify({'message': 'New plan added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400
#===============================================================================
           # ADD DOMAIN
#===============================================================================
# Route to get list of domains
@app.route('/get_domains_api', methods=['GET'])
def get_domains_api():
    domains = get_domains()
    return jsonify({"domains": domains})

@app.route('/add_domain', methods=['POST'])
def add_domain():
    try:
        data = request.json
        conn = sqlite3.connect('kdb.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO domain_mst (domain_name, domain_id)
            VALUES (?, ?)
        ''', (
            data['domain_name'], data['domain_id']
        ))

        conn.commit()
        conn.close()
        return jsonify({'message': 'New domain information added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400
# Route to get list of plans
@app.route('/get_plans_api', methods=['GET'])
def get_plans_api():
    plans = get_plans()
    return jsonify({"plans": plans})
#===============================================================================
           # TENANT
#===============================================================================    

#==================================tenant_service=======================
DATABASE="kdb.db"
@app.route('/tenant_service')
def tenant_service():
    s_cust_id=session['cust_id']
    return render_template("add_tenant_service.html",s_cust_id=s_cust_id)
# Define the route for adding tenant service data
# Handle form submission and insert data into the 'client_txn' table
@app.route('/Add_tenant_service', methods=['POST'])
def Add_tenant_service():
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Check the content type of the request
        content_type = request.headers.get('Content-Type')
        print(content_type)
        if content_type == 'application/json':
            # If the content type is JSON, parse JSON dat

            data = request.json
        elif content_type.startswith('application/x-www-form-urlencoded'):
 
            # If the content type is form data, parse form data
            data = {
            'client_email_id': request.form.get('client_email_id'),
            'service_name': request.form.get('service_name'),
            'category': request.form.get('category'),
            'selling_price': request.form.get('selling_price'),
            'MRP': request.form.get('MRP'),
            'discount': request.form.get('discount'),
            'is_active': request.form.get('is_active'),
            'created_by': request.form.get('created_by'),
            'created_at':request.form.get('created_at'),
            'modified_by': request.form.get('modified_by'),
            'modified_date': request.form.get('modified_date'),
            'sub_category':request.form.get('sub_category')
        }
        else:
            return jsonify({'error': 'Unsupported content type'}), 400
        conn = sqlite3.connect('kdb.db')  # Replace 'your_database.db' with your database file path
        cursor = conn.cursor()

        # Verify if the 'client_email_id' exists in 'client_info'
        client_email_id = data.get('client_email_id', None)
        if client_email_id:
            cursor.execute('SELECT email_id FROM client_info WHERE email_id = ?', (client_email_id,))
            client_exists = cursor.fetchone()
            if not client_exists:
                conn.close()
                return jsonify({'error': 'Client email_id does not exist'}), 400

            # Insert data into 'tenant_service_db' if client email_id matches
            if client_email_id == data.get('client_email_id'):
                cursor.execute('''
                    INSERT INTO tenant_service_db (client_email_id, service_name, category, selling_price, MRP, discount, is_active, created_by, created_at, modified_by, modified_date, sub_category)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    client_email_id, data['service_name'], data['category'], data['selling_price'], data['MRP'],
                    data['discount'], data['is_active'], data['created_by'], data['created_at'], data['modified_by'],
                    data['modified_date'], data['sub_category']
                ))

                conn.commit()
                conn.close()
                return jsonify({'message': 'New tenant service information added successfully'}), 201
            else:
                conn.close()
                return jsonify({'error': 'Client email_id does not match tenant_id'}), 400
        else:
            conn.close()
            return jsonify({'error': 'Client email_id is missing in JSON data'}), 400

    except Exception as e:
        return str(e)

# Define a route to get plan information by plan name
@app.route('/get_plan_info', methods=['GET'])
def get_plan_info():
    try:
        # Get the plan name from the query parameters
        plan_name = request.args.get('plan_name')

        if not plan_name:
            return jsonify({'error': 'Plan name is required as a query parameter'}), 400

        conn = sqlite3.connect('kdb.db')  # Replace 'your_database.db' with your database file path
        cursor = conn.cursor()

        # Retrieve plan information by plan name
        cursor.execute('SELECT * FROM plan_mst WHERE plan_name = ?', (plan_name,))
        plan_info = cursor.fetchone()

        conn.close()

        if plan_info:
            # Convert the result to a dictionary for JSON response
            plan_dict = {
                'plan_name': plan_info[0],
                'plan_amount': plan_info[1],
                'discount': plan_info[2],
                'created_date': plan_info[3],
                'created_by': plan_info[4]
            }
            return jsonify(plan_dict)
        else:
            return jsonify({'error': 'Plan not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    




#=======================================================================
    

                     #MODIFIED CODE
    

#====================================================================

#=================================================================
            #customer_info 
#==================================================================
@app.route("/customer_searchbar")
def customer_searchbar():
    return render_template("searchbar.html")
@app.route('/search', methods=['POST'])
def search():
    try:
        cust_mobile = request.form.get('searchMobile')
        session["cust_mobile"] = cust_mobile
        branch_id=session['branch_id']

        conn = sqlite3.connect('kdb.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM cust_mst WHERE cust_mobile=? and branch_id=?", (cust_mobile,branch_id))
        customer_data = cursor.fetchall()

        conn.commit()
        conn.close()
        print("cust assigned branch",session['branch_id'])

        return jsonify({'customer_data': customer_data})

    except sqlite3.Error as e:
        print("SQLite error:", e)
        return jsonify({'error': 'Database error'}), 500
@app.route("/get_search_data")
def get_search_data():
    try:
        cust_mobile = session.get('cust_mobile')

        if not cust_mobile:
            return redirect("/customer_searchbar")

        conn = sqlite3.connect('kdb.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM cust_mst WHERE cust_mobile=?", (cust_mobile,))
        customer_data = cursor.fetchall()

        conn.commit()
        conn.close()

        return render_template("searchbar.html", customer_data=customer_data)

    except sqlite3.Error as e:
        print("SQLite error:", e)
        return jsonify({'error': 'Database error'}), 500
@app.route('/add_tnx_cust')
def add_tnx_cust():
    # Get cust_id from query parameters
    cust_id = request.args.get('cust_id')
    print("cust_id from transaction table :",cust_id)
    conn = sqlite3.connect('kdb.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * from cust_mst where cust_id=?",(cust_id,))
    result=cursor.fetchall()
    print("results based on cust_id",result)
    session['cust_id']=result[0][3]
    session["cust_name"]=result[0][4]
    session["cust Mobile"]=result[0][6]
    session["branch_id"]=result[0][0]
    conn.commit()
    conn.close()
    return add_customer_tnx()
    
if __name__ == '__main__':
    app.run(debug=True)
