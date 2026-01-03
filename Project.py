from datetime import datetime,timedelta
from DataBase import Database as db

class Record_system:
    def __init__(self):

        self.Date = datetime.today().strftime("%Y-%m-%d")
        self.Time = datetime.now().strftime("%I:%M %p")
        self.Database = db()
        self.data = []

    def transaction(self): 
        # ang purpose ng function na ito mag tract ng user input
        database = db()
        information = database.view_data()
        return information
    
    def view_date(self):
        data = self.Database.view_date_and_time()
        date_list = []
        for dates in data:
            date_list.append(dates)
        return date_list
    
    def InsertToDatabase(self,item,quantity,amount):
        # itong function na ito para mag insert ng data sa database
        data = [item,quantity,amount,self.Date,self.Time]
        Store = db()
        Store.insert_data(data)
        print("Successfully insert")

    def delete(self,Product_number):
        self.Database.delete_data((Product_number,))

    def update(self,Item,quantity,amount,product_id):
        self.Database.update(Item,quantity,amount,product_id)
        print("successfull")

    # gumawa ako ng function para mag compute ng mga expenses at mag return ng mga
    # overall data 

    def today_expenses(self,need):
        start_date = self.Date
        end_date = self.Date
        total_amount = self.Database.get_expenses_by_date(start_date,end_date)
        all_data = self.Database.get_data_by_date(start_date,end_date)
        if need == "total expenses":return total_amount
        elif need == "all data":return all_data

    def weekly_expenses(self,need):
        end_date = self.transaction()[-1][4]
        latest_date = datetime.strptime(end_date,"%Y-%m-%d")
        start_date = latest_date - timedelta(days=6)
        total_expenses = self.Database.get_expenses_by_date(str(start_date),str(latest_date))
        all_data = self.Database.get_data_by_date(str(start_date),str(latest_date))
        if need == "total expenses":return total_expenses
        elif need == "all data":return all_data

    def monthly_expenses(self,need):
        end_date = self.transaction()[-1][4]
        latest_date = datetime.strptime(end_date,"%Y-%m-%d")
        start_date = latest_date - timedelta(days=30)
        total_expenses = self.Database.get_expenses_by_date(str(start_date),str(latest_date))
        all_data = self.Database.get_data_by_date(str(start_date),str(latest_date))
        if need == "total expenses":return total_expenses
        elif need == "all data":return all_data

    def yearly_expenses(self,need):
        end_date = self.transaction()[-1][4]
        latest_date = datetime.strptime(end_date,"%Y-%m-%d")
        start_date = latest_date - timedelta(days=365)
        total_expenses = self.Database.get_expenses_by_date(str(start_date),str(latest_date))
        all_data = self.Database.get_data_by_date(str(start_date),str(latest_date))
        if need == "total expenses":return total_expenses
        elif need == "all data":return all_data

app = Record_system()


