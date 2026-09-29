import os
import mysql.connector
from flask import Flask, render_template_string

app = Flask(__name__)

# ============================================================
# DATABASE CONNECTION
# ============================================================

def connect_database():
    connection = mysql.connector.connect(
        host="mysql-2c267845-yaswanthpalli515-edd2.h.aivencloud.com",
        port=25502,
        user="avnadmin",
        password=os.environ.get("DB_PASSWORD"),
        database="defaultdb",
        ssl_disabled=False,
        ssl_verify_cert=False,
        ssl_verify_identity=False
    )
    return connection



# ============================================================
# MAIN HOME PAGE
# ============================================================

HTML = """
<!DOCTYPE html>

<html>

<head>

    <title>KTM Bike Sales Management System</title>

    <style>

        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            margin: 0;
        }

        .header {
            background-color: #111111;
            color: white;
            padding: 25px;
            text-align: center;
        }

        .header h1 {
            margin: 0;
        }

        .menu {
            text-align: center;
            padding: 25px;
        }

        .menu a {
            display: inline-block;
            background-color: #ff6600;
            color: white;
            text-decoration: none;
            padding: 12px 25px;
            margin: 6px;
            border-radius: 5px;
            font-weight: bold;
        }

        .menu a:hover {
            background-color: #cc5200;
        }

        .content {
            width: 90%;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
        }

        .welcome {
            text-align: center;
            padding: 30px;
        }

        .welcome h2 {
            color: #ff6600;
        }

    </style>

</head>


<body>


<div class="header">

    <h1>KTM BIKE SALES MANAGEMENT SYSTEM</h1>

    <p>Bike Company Sales Management System</p>

</div>


<div class="menu">

    <a href="/bikes">Bikes</a>

    <a href="/customers">Customers</a>

    <a href="/employees">Employees</a>

    <a href="/sales">Sales</a>

    <a href="/payments">Payments</a>

    <a href="/reports">Reports</a>

</div>


<div class="content">

    <div class="welcome">

        <h2>Welcome</h2>

        <p>
            Select a module above to view
            information stored in the MySQL database.
        </p>

    </div>

</div>


</body>

</html>
"""


# ============================================================
# CREATE TABLE HTML
# ============================================================

def create_table(title, columns, rows):

    header = ""

    for column in columns:

        header += f"<th>{column}</th>"


    body = ""

    for row in rows:

        body += "<tr>"

        for value in row:

            body += f"<td>{value}</td>"

        body += "</tr>"


    return f"""

<!DOCTYPE html>

<html>

<head>

    <title>{title}</title>

    <style>

        body {{
            font-family: Arial;
            background-color: #f2f2f2;
            margin: 0;
        }}

        .header {{
            background-color: #111;
            color: white;
            padding: 20px;
            text-align: center;
        }}

        .content {{
            width: 90%;
            margin: 30px auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
        }}

        th {{
            background-color: #222;
            color: white;
            padding: 10px;
        }}

        td {{
            padding: 10px;
            border: 1px solid #ddd;
            text-align: center;
        }}

        tr:nth-child(even) {{
            background-color: #f2f2f2;
        }}

        .back {{
            display: inline-block;
            margin-top: 20px;
            background-color: #ff6600;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
        }}

        .menu {{
            text-align: center;
            margin-bottom: 20px;
        }}

        .menu a {{
            display: inline-block;
            background-color: #ff6600;
            color: white;
            text-decoration: none;
            padding: 10px 18px;
            margin: 5px;
            border-radius: 5px;
        }}

    </style>

</head>


<body>


<div class="header">

    <h1>KTM BIKE SALES MANAGEMENT SYSTEM</h1>

</div>


<div class="content">

    <div class="menu">

        <a href="/">Home</a>

        <a href="/bikes">Bikes</a>

        <a href="/customers">Customers</a>

        <a href="/employees">Employees</a>

        <a href="/sales">Sales</a>

        <a href="/payments">Payments</a>

        <a href="/reports">Reports</a>

    </div>


    <h2>{title}</h2>


    <table>

        <tr>

            {header}

        </tr>

        {body}

    </table>


    <a class="back" href="/">
        Back to Home
    </a>


</div>


</body>

</html>

"""


# ============================================================
# HOME
# ============================================================

@app.route("/")
def home():

    return render_template_string(HTML)


# ============================================================
# BIKES
# ============================================================

@app.route("/bikes")
def bikes():

    connection = connect_database()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            bike_id,
            model_name,
            category,
            engine_cc,
            price,
            stock_quantity
        FROM Bike
    """)

    rows = cursor.fetchall()

    cursor.close()

    connection.close()


    columns = [

        "Bike ID",
        "Model Name",
        "Category",
        "Engine CC",
        "Price",
        "Stock"

    ]


    return create_table(
        "Bikes",
        columns,
        rows
    )


# ============================================================
# CUSTOMERS
# ============================================================

@app.route("/customers")
def customers():

    connection = connect_database()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            customer_id,
            customer_name,
            phone,
            email,
            address
        FROM Customer
    """)

    rows = cursor.fetchall()

    cursor.close()

    connection.close()


    columns = [

        "Customer ID",
        "Customer Name",
        "Phone",
        "Email",
        "Address"

    ]


    return create_table(
        "Customers",
        columns,
        rows
    )


# ============================================================
# EMPLOYEES
# ============================================================

@app.route("/employees")
def employees():

    connection = connect_database()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            employee_id,
            employee_name,
            phone,
            designation
        FROM Employee
    """)

    rows = cursor.fetchall()

    cursor.close()

    connection.close()


    columns = [

        "Employee ID",
        "Employee Name",
        "Phone",
        "Designation"

    ]


    return create_table(
        "Employees",
        columns,
        rows
    )


# ============================================================
# SALES
# ============================================================

@app.route("/sales")
def sales():

    connection = connect_database()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            sale_id,
            customer_id,
            bike_id,
            employee_id,
            sale_date,
            quantity,
            total_amount
        FROM Sale
    """)

    rows = cursor.fetchall()

    cursor.close()

    connection.close()


    columns = [

        "Sale ID",
        "Customer ID",
        "Bike ID",
        "Employee ID",
        "Sale Date",
        "Quantity",
        "Total Amount"

    ]


    return create_table(
        "Sales",
        columns,
        rows
    )


# ============================================================
# PAYMENTS
# ============================================================

@app.route("/payments")
def payments():

    connection = connect_database()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            payment_id,
            sale_id,
            payment_date,
            payment_method,
            amount
        FROM Payment
    """)

    rows = cursor.fetchall()

    cursor.close()

    connection.close()


    columns = [

        "Payment ID",
        "Sale ID",
        "Payment Date",
        "Payment Method",
        "Amount"

    ]


    return create_table(
        "Payments",
        columns,
        rows
    )


# ============================================================
# REPORTS
# ============================================================

@app.route("/reports")
def reports():

    connection = connect_database()

    cursor = connection.cursor()


    # Total Bikes

    cursor.execute(
        "SELECT COUNT(*) FROM Bike"
    )

    total_bikes = cursor.fetchone()[0]


    # Total Customers

    cursor.execute(
        "SELECT COUNT(*) FROM Customer"
    )

    total_customers = cursor.fetchone()[0]


    # Total Employees

    cursor.execute(
        "SELECT COUNT(*) FROM Employee"
    )

    total_employees = cursor.fetchone()[0]


    # Total Sales

    cursor.execute(
        "SELECT COUNT(*) FROM Sale"
    )

    total_sales = cursor.fetchone()[0]


    # Total Sales Amount

    cursor.execute(
        "SELECT COALESCE(SUM(total_amount), 0) FROM Sale"
    )

    total_sales_amount = cursor.fetchone()[0]


    # Total Payments

    cursor.execute(
        "SELECT COALESCE(SUM(amount), 0) FROM Payment"
    )

    total_payments = cursor.fetchone()[0]


    # Available Stock

    cursor.execute(
        "SELECT COALESCE(SUM(stock_quantity), 0) FROM Bike"
    )

    available_stock = cursor.fetchone()[0]


    cursor.close()

    connection.close()


    return f"""

<!DOCTYPE html>

<html>

<head>

    <title>KTM Reports</title>

    <style>

        body {{
            font-family: Arial;
            background-color: #f2f2f2;
            margin: 0;
        }}

        .header {{
            background-color: #111;
            color: white;
            padding: 20px;
            text-align: center;
        }}

        .content {{
            width: 80%;
            margin: 30px auto;
            background: white;
            padding: 25px;
            border-radius: 8px;
        }}

        .menu {{
            text-align: center;
            margin-bottom: 25px;
        }}

        .menu a {{
            display: inline-block;
            background-color: #ff6600;
            color: white;
            padding: 10px 18px;
            margin: 5px;
            text-decoration: none;
            border-radius: 5px;
        }}

        .report {{
            background-color: #eeeeee;
            padding: 18px;
            margin: 12px;
            font-size: 20px;
            border-radius: 5px;
        }}

        .back {{
            display: inline-block;
            margin-top: 20px;
            background-color: #ff6600;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
        }}

    </style>

</head>


<body>


<div class="header">

    <h1>KTM BIKE SALES MANAGEMENT SYSTEM</h1>

</div>


<div class="content">


    <div class="menu">

        <a href="/">Home</a>

        <a href="/bikes">Bikes</a>

        <a href="/customers">Customers</a>

        <a href="/employees">Employees</a>

        <a href="/sales">Sales</a>

        <a href="/payments">Payments</a>

        <a href="/reports">Reports</a>

    </div>


    <h2>Reports</h2>


    <div class="report">
        Total Bikes: {total_bikes}
    </div>


    <div class="report">
        Total Customers: {total_customers}
    </div>


    <div class="report">
        Total Employees: {total_employees}
    </div>


    <div class="report">
        Total Sales: {total_sales}
    </div>


    <div class="report">
        Total Sales Amount: {total_sales_amount}
    </div>


    <div class="report">
        Total Payments: {total_payments}
    </div>


    <div class="report">
        Available Stock: {available_stock}
    </div>


    <a class="back" href="/export-report">
        Export Report
    </a>


</div>


</body>

</html>

"""
@app.route("/export-report")
def export_report():

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM Bike")
    total_bikes = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM Customer")
    total_customers = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM Employee")
    total_employees = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM Sale")
    total_sales = cursor.fetchone()[0]

    cursor.execute("SELECT COALESCE(SUM(total_amount), 0) FROM Sale")
    total_sales_amount = cursor.fetchone()[0]

    cursor.execute("SELECT COALESCE(SUM(amount), 0) FROM Payment")
    total_payments = cursor.fetchone()[0]

    cursor.execute("SELECT COALESCE(SUM(stock_quantity), 0) FROM Bike")
    available_stock = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    from flask import Response
    from datetime import datetime

    generated_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    csv_data = (
        "KTM BIKE SALES MANAGEMENT SYSTEM\n"
        f"Report Generated: {generated_date}\n"
        "\n"
        "Report,Value\n"
        f"Total Bikes,{total_bikes}\n"
        f"Total Customers,{total_customers}\n"
        f"Total Employees,{total_employees}\n"
        f"Total Sales,{total_sales}\n"
        f"Total Sales Amount,{total_sales_amount}\n"
        f"Total Payments,{total_payments}\n"
        f"Available Stock,{available_stock}\n"
    )

    return Response(
        csv_data,
        mimetype="text/csv",
        headers={
            "Content-Disposition": "attachment; filename=KTM_Report.csv"
        }
    )
# ============================================================
# START APPLICATION
# ============================================================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )