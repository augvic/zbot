from datetime import datetime

class DateUtility:
    
    def get_today(self) -> str:
        return datetime.now().strftime("%d/%m/%Y")
