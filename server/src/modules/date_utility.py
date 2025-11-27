from datetime import datetime, date

class DateUtility:
    
    def get_today_str(self) -> str:
        try:
            return datetime.now().strftime("%d/%m/%Y")
        except Exception as error:
            raise Exception(f"Error in (DateUtility) component in (get_today_str) method: {error}.")
        
    def get_today_str_with_time(self) -> str:
        try:
            return datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")
        except Exception as error:
            raise Exception(f"Error in (DateUtility) component in (get_today_str_with_time) method: {error}.")
    
    def get_today_datetime(self) -> date:
        try:
            return datetime.now().date()
        except Exception as error:
            raise Exception(f"Error in (DateUtility) component in (get_today_datetime) method: {error}.")
        
    def convert_to_datetime(self, date: str) -> date:
        try:
            return datetime.strptime(date, "%d/%m/%Y")
        except Exception as error:
            raise Exception(f"Error in (DateUtility) component in (convert_to_datetime) method: {error}.")
        
    def convert_to_string(self, date: datetime) -> str:
        try:
            return datetime.strftime(date, "%d/%m/%Y")
        except Exception as error:
            raise Exception(f"Error in (DateUtility) component in (convert_to_datetime) method: {error}.")
        
    def is_date(self, date: str) -> bool:
        try:
            datetime.strptime(date, "%d/%m/%Y")
            return True
        except:
            return False
