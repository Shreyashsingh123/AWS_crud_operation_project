from .connections import connection 

class salestransaction:
    def __init__(self):
        self.connection=connection()
            
    def Aggregate_function(self):
        conn=self.connection
        curr=conn.cursor()
        query1="""
        select sum(TotalAmount) as sum_amount
        from sales_data
        """
        curr.execute(query1)
        val=curr.fetchone()[0]
        print("\n########## SUM of total amount from data #############\n")
        print("Total amount is:",val)

        query2="""
        select avg(TotalAmount) as avg_amount from sales_data
        """
        curr.execute(query2)
        avg_val=curr.fetchone()[0]
        print("\n##########Average of total amount from data #############\n")
        print("Average of total amoint is:",avg_val)

        query3="""
        select count (*) from sales_data
        """
        curr.execute(query3)
        cnt=curr.fetchone()[0]
        print("\n##########Total number of rows #############\n")
        print("Count of rows is:",cnt)

    def group_by_having(self):
        conn=self.connection
        curr=conn.cursor()

        query1="""
        select City,sum(TotalAmount) as sum_amount from sales_data 
        group by (City) having sum(TotalAmount)>10000
        """
        curr.execute(query1)
        print("\n##########Group  by with having #############\n")
        print("City wise total amount is\n")

        rows=curr.fetchall()
        for row in rows:
            print(row)
            curr.close()
            

    def date_based_filtering(self):
        conn=self.connection
        curr=conn.cursor()
        query="""
        select * from sales_data where
        OrderDate between '2024-06-25' and '2024-07-10'
        """
        curr.execute(query)

        rows=curr.fetchall()
        print("\n########## Date based filtering #############\n")
        for row in rows:
            print(row)
            curr.close()
            

    def sort_data(self):
        conn=self.connection
        curr=conn.cursor()
        query="""
        select * from sales_data
        order by TotalAmount desc limit 20
        """
        curr.execute(query)
        print("\n########## Sorted data based on Total amount #############\n")
        rows=curr.fetchall()
        for row in rows:
            print(row)

        curr.close()
        

    def top_bottom_performer(self):
        conn=self.connection
        curr=conn.cursor()
        query="""
        select * from sales_data
        order by TotalAmount desc limit 1
        """
        curr.execute(query)
        print("\n###### Top performer based on total amount is ######\n")
        top=curr.fetchone()
        print(top)

        query="""
        select * from sales_data
        order by TotalAmount limit 1
        """
        curr.execute(query)
        print("\n###### Bottom performer based on total amount is ######\n")
        bottom=curr.fetchone()
        print(bottom)

        curr.close()
        
    def connection_close(self):
        self.connection.close()