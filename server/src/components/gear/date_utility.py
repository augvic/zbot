from datetime import datetime, date

class DateUtility:
    
    def get_today_str(self) -> str:
        try:
            return datetime.now().strftime("%d/%m/%Y")
        except Exception as error:
            raise Exception(f"Error in (DateUtility) component in (get_today_str) method: {error}.")
    
    def get_today_datetime(self) -> date:
        try:
            return datetime.now().date()
        except Exception as error:
            raise Exception(f"Error in (DateUtility) component in (get_today_datetime) method: {error}.")
