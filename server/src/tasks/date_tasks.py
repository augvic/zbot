from src.modules.date_utility import DateUtility
from datetime import date, datetime

class DateTasks:
    
    def __init__(self,
        date_utility: DateUtility
    ) -> None:
        self.date_utility = date_utility
    
    def get_today_str(self) -> str:
        try:
            return self.date_utility.get_today_str()
        except Exception as error:
            raise Exception(f"Error in (DateTasks) task in (get_today_str) method: {error}.")
        
    def get_today_str_with_time(self) -> str:
        try:
            return self.date_utility.get_today_str_with_time()
        except Exception as error:
            raise Exception(f"Error in (DateTasks) task in (get_today_str_with_time) method: {error}.")
    
    def get_today_datetime(self) -> date:
        try:
            return self.date_utility.get_today_datetime()
        except Exception as error:
            raise Exception(f"Error in (DateTasks) task in (get_today_datetime) method: {error}.")
        
    def convert_to_datetime(self, date: str) -> date:
        try:
            return self.date_utility.convert_to_datetime(date)
        except Exception as error:
            raise Exception(f"Error in (DateTasks) task in (convert_to_datetime) method: {error}.")
        
    def convert_to_string(self, date: datetime) -> str:
        try:
            return self.date_utility.convert_to_string(date)
        except Exception as error:
            raise Exception(f"Error in (DateTasks) task in (convert_to_datetime) method: {error}.")
        
    def is_date(self, date: str) -> bool:
        try:
            return self.date_utility.is_date(date)
        except Exception as error:
            raise Exception(f"Error in (DateTasks) task in (convert_to_datetime) method: {error}.")
