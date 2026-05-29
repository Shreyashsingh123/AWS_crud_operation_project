from connections import connection

class Crudoperation:
    def __init__(self):
        self.connection=connection()

    def create_table():
        conn=connection()
        curr=conn.cursor()
        create_query="""
        CREATE TABLE IF NOT EXISTS sales_data(
            OrderId varchar(50) primary key,
            CustomerId varchar(50),
            OrderDate Date,
            ProductCategory varchar(50),
            Quantity int,
            UnitPrice decimal(10,2),
            TotalAmount decimal(10,2),
            PaymentMethod varchar(50),
            City varchar(50)
                
                    );
        """
        curr.execute(create_query)
        print(" Table created successfully")
        conn.commit()
        curr.close()
        conn.close()
    
    def insert_data(df):

        # Database connection
        conn = connection()
        curr = conn.cursor()

        # Insert query
        insert_query = """
        INSERT INTO sales_data(
            orderid,
            customerid,
            orderdate,
            productcategory,
            quantity,
            unitprice,
            totalamount,
            paymentmethod,
            city
        )
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT (orderid) DO NOTHING;
        """

        # Convert dataframe rows into tuples
        data = []

        for index, row in df.iterrows():

            values = (
                row["Order_ID"],
                row["Customer_ID"],
                row["Order_Date"],
                row["Product_Category"],
                int(row["Quantity"]),
                float(row["Unit_Price"]),
                float(row["Total_Amount"]),
                row["Payment_Method"],
                row["City"]
            )

            data.append(values)

        curr.executemany(insert_query, data)
        conn.commit()

        print("Data inserted successfully")
        
        curr.close()
        conn.close()

    def update_data():
        conn=connection()
        curr=conn.cursor()
        query="""
        update sales_data
        set TotalAmount=%s,
        PaymentMethod=%s
        where OrderId=%s

        """
        payment_method="Debit_card"
        Total_amount="150000"
        order_id="ORD00001"
        curr.execute(query,(Total_amount,payment_method,order_id))
        conn.commit()

        conn.close()
        curr.close()
        print("Data updated successfully")

    def delete_record_by_city():
        conn=connection()
        curr=conn.cursor()

        query="""
        delete from sales_data
        where city=%s
        """
        city="North Kimberly"
        curr.execute(query,(city,))
        conn.commit()

        print("Data deleted successfully")
        curr.close()
        conn.close()
    
    def filter_by_city():
        conn=connection()
        curr=conn.cursor()
        create_query="""
        select * from sales_data where city=%s;
        """

        curr.execute(create_query,("Alexanderhaven",))
        
        rows=curr.fetchall()
        print(len(rows))
        for row in rows:
            print(row)

        curr.close()
        conn.close()


