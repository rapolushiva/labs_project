import sqlite3

# Create a SQLite database connection
conn = sqlite3.connect('kdb.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS tenant_info (
    tenant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    tenant_mail TEXT UNIQUE,
    tenant_name TEXT,
    password_hash TEXT,
    password_hint TEXT,
    tenant_mobile TEXT,
    alternative_mobile TEXT,
    location TEXT,
    biz_name TEXT,
    est_date DATE,
    dob DATE,
    gender TEXT,
    domain_name TEXT,
    plan TEXT,
    pincode TEXT,
    referred_by TEXT,
    referral_code TEXT,
    self_referral BOOLEAN,
    created_date DATE,
    expire_date DATE,
    plan_duration TEXT,
    has_branches BOOLEAN
)
''')



# Create the plan_mst table
cursor.execute('''CREATE TABLE IF NOT EXISTS plan_mst (
    plan_id INTEGER PRIMARY KEY AUTOINCREMENT,
    plan_name TEXT,
    plan_amount REAL,
    discount REAL,
    plan_duration_days INTEGER,
    enable_SMS_reminder BOOLEAN,
    enable_whatsapp_reminder BOOLEAN,
    enable_basic_dashboard BOOLEAN,
    enable_advanced_dashboard BOOLEAN,
    enable_monthly_reports BOOLEAN,
    enable_weekly_reports BOOLEAN,
    data_download_permission BOOLEAN,
    created_date DATE,
    created_by TEXT
)
''') 

# Create the domain_mst table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS domain_mst (
        domain_name TEXT PRIMARY KEY,
        domain_id INTEGER
    )
''')

# Assuming you already have a SQLite database connection and cursor
cursor.execute('''
    -- Create the 'tenants' table
    CREATE TABLE IF NOT EXISTS tenants (
        tenant_id INTEGER PRIMARY KEY,
        tenant_mail TEXT,
        tenant_mobile TEXT,
        tenant_name TEXT,
        FOREIGN KEY (tenant_id) REFERENCES client_info(email_id)
    )
''')
    
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cust_mst (
        tenant_id TEXT,
        branch_id TEXT,
        branch_name TEXT,
        cust_id TEXT,
        cust_name TEXT,
        cust_mail TEXT,
        cust_mobile TEXT,
        cust_alternate_mobile TEXT,
        cust_whatsapp_number TEXT,
        cust_age INT,
        cust_gender TEXT,
        cust_location TEXT,
        cust_pincode TEXT,
        FOREIGN KEY (tenant_id) REFERENCES client_info(tenant_id)               
    )
''')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS User (
    EmailId TEXT NOT NULL UNIQUE,
    Username TEXT NOT NULL UNIQUE,
    Password TEXT NOT NULL
)'''
)

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Customer_Transaction_DB (
    branch_id TEXT,
    Cust_id TEXT,
    Cust_name TEXT,
    Cust_mobile TEXT,
    Service_name TEXT,
    Remainder_days INT,
    Current_date DATE,
    Current_service_remark TEXT,
    Payment_Mode TEXT CHECK (Payment_Mode IN ('online', 'Card', 'UPI')),
    Paid_amount FLOAT,
    Discount FLOAT,
    Location TEXT
)''')




# Create the client_txn table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS client_txn (
        transactionId TEXT PRIMARY KEY,
        tenant_id INT,
        tenant_name TEXT,
        start_date DATE,
        end_date DATE,
        duration TEXT,
        plan_name TEXT,
        plan_amount FLOAT,
        paid_amount FLOAT,
        mode_of_payment TEXT,
        modified_date DATE,
        created_date DATE,
        payment_date DATE
    )
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS tenant_service_db (
    service_id INTEGER PRIMARY KEY,
    tenant_id TEXT,
    branch_id TEXT,
    service_name TEXT,
    category TEXT,
    selling_price FLOAT,
    mrp FLOAT,
    discount FLOAT,
    is_active BOOLEAN,
    created_by TEXT,
    created_at DATE,
    modified_by TEXT,
    modified_date DATE,
    sub_category TEXT,
    FOREIGN KEY (tenant_id) REFERENCES client_info(tenant_id)
)
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS branch_table(
        tenant_id TEXT,
        branch_id AUTO INCREMENT INTEGER,
        branch_name TEXT,
        username TEXT,
        password TEXT,
        plan_duration TEXT,
        plan_expiry_date DATE,
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS skus (
        tenant_id TEXT,
        branch_id TEXT,
        is_active INTEGER,  -- SQLite does not have a separate BOOLEAN type
        selling_price REAL,  -- SQLite uses REAL for floating-point numbers
        mrp REAL,
        service_name TEXT,
        service_category TEXT,
        service_code UNIQUE,
        created_date DATE,
        modified_date DATE,
        modified_by TEXT
    )
''')
conn.commit()
conn.close()
print("Tables created successfully.")