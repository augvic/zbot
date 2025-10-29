from datetime import datetime, date

class DateUtility:
    
    def get_today_str(self) -> str:
        return datetime.now().strftime("%d/%m/%Y")
    
    def get_today_datetime(self) -> date:
        return datetime.now().date()
