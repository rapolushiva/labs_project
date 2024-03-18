import sqlite3

#======================CustomerTransaction_Details===========================#


# Define the insert_transaction function
def insert_transaction(data):
    try:
        conn = sqlite3.connect('kdb.db')
        cursor = conn.cursor()

      

        # Customer_id exists, fetch Customer_name and Customer_mobile
        customer_name, customer_mobile = "kiran",919281981
        # Insert transaction data into Customer_Transaction_DB
        cursor.execute('''
            INSERT INTO Customer_Transaction_DB (
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
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
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
        return True
    except Exception as e:
        conn.rollback()
        conn.close()
        return str(e)
    
# Create a customer with a generated Customer ID
def create_customer(data):
    try:
        conn = sqlite3.connect('kdb.db')
        cursor = conn.cursor()
        
        # Generate a random number (e.g., 4 digits)
        import random

# Generate a random 6-digit number
        customer_id = random.randint(100000, 999999)
        
        cursor.execute('''
            INSERT INTO customer_info_DB (
                Customer_id, Customer_name, Customer_mail, Customer_mobile,
                Customer_alternate_mobile, Customer_whatsapp_number, Customer_age,
                Customer_gender, Customer_location, Customer_pincode, client_id, client_name
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            customer_id, data['Customer_name'], data['Customer_mail'], data['Customer_mobile'],
            data['Customer_alternate_mobile'], data['Customer_whatsapp_number'], data['Customer_age'],
            data['Customer_gender'], data['Customer_location'], data['Customer_pincode'],
            data['client_id'], data['client_name']
        ))
        
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        return False





import sqlite3

def insert_client_info(data):
    try:
        # Connect to the database
        with sqlite3.connect('kdb.db') as conn:
            # Create a cursor
            cursor = conn.cursor()

            # Execute the INSERT statement
            cursor.execute('''
                INSERT INTO client_info
                (email_id, name, mobile, location, biz_name, est_date, dob, gender, domain_name, plan, pincode, Referred_by, Referal_Code, Referral_Self, Created_date, Expire_date, Plan_duration, As_branch, password_hash)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                data['email_id'], data['name'], data['mobile'], data['location'], data['biz_name'],
                data['est_date'], data['dob'], data['gender'], data['domain_name'], data['plan'],
                data['pincode'], data['Referred_by'], data['Referal_Code'], data['Referral_Self'],
                data['Created_date'], data['Expire_date'], data['Plan_duration'], data['As_branch'], data['password']
            ))

            # Check if the insert was successful
            if cursor.rowcount > 0:
                print("Record inserted successfully.")
            else:
                print("Failed to insert record. No rows affected.")

            # Commit the transaction
            conn.commit()

    except sqlite3.Error as e:
        print("SQLite error:", e)

    finally:
        # Close the connection in the finally block to ensure it's always closed
        conn.close()

    return True
    