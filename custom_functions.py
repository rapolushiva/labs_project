import sqlite3

# Function to fetch plans from the database
def get_plans():
    conn = sqlite3.connect('kdb.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM plan_mst')
    plans = cursor.fetchall()

    conn.close()

    return [{"plan_name": plan[0], "plan_amount": plan[1], "expiry_date": plan[2], "discount": plan[3]} for plan in plans]

# Function to fetch domains from the database
def get_domains():
    conn = sqlite3.connect('kdb.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM domain_mst')
    domains = cursor.fetchall()

    conn.close()

    return [{"domain_name": domain[0], "domain_id": domain[1]} for domain in domains]



import sqlite3



def create_tenant(tenant_data):
    conn = sqlite3.connect('kdb.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO tenants (tenant_mail,tenant_mobile,tenant_name, client_id, client_name)
            VALUES (?, ?, ?,?,?)
        ''', (
            tenant_data['tenant_mail'],tenant_data['tenant_mobile'],tenant_data['tenant_name'], tenant_data['client_id'], tenant_data['client_name']
        ))

        conn.commit()
        conn.close()
        return True
    except Exception as e:
        conn.rollback()
        conn.close()
        return str(e)

# Function to fetch tenant information by tenant_id
def get_tenant(tenant_id):
    conn = sqlite3.connect('kdb.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM tenants WHERE tenant_id = ?
    ''', (tenant_id,))

    tenant = cursor.fetchone()
    conn.close()

    if tenant:
        tenant_info = {
            'tenant_id': tenant[0],
            'tenant_name': tenant[1],
            'client_id': tenant[2],
            'client_name': tenant[3]
        }
        return tenant_info
    else:
        return None

# Function to update tenant information
def update_tenant(tenant_id, tenant_data):
    conn = sqlite3.connect('kdb.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''
            UPDATE tenants
            SET tenant_name = ?, client_id = ?, client_name = ?
            WHERE tenant_id = ?
        ''', (
            tenant_data['tenant_name'], tenant_data['client_id'], tenant_data['client_name'], tenant_id
        ))

        conn.commit()
        conn.close()
        return True
    except Exception as e:
        conn.rollback()
        conn.close()
        return str(e)

# Function to delete a tenant by tenant_id
def delete_tenant(tenant_id):
    conn = sqlite3.connect('kdb.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''
            DELETE FROM tenants WHERE tenant_id = ?
        ''', (tenant_id,))

        conn.commit()
        conn.close()
        return True
    except Exception as e:
        conn.rollback()
        conn.close()
        return str(e)

#============UU_ID_Function==================
import uuid

def generate_uuid():
    # Generate a UUID and return it as a string
    return str(uuid.uuid4())

# Usage example:
uuid_value = generate_uuid()
print("Generated UUID:", uuid_value)
#===============================
