from src.modules.date_utility import DateUtility
from src.modules.dataframe_handler import DataFrameHandler

from datetime import date, datetime
from pandas import DataFrame

class Utilities:
    
    def __init__(self,
        date_utility: DateUtility,
        dataframe_handler: DataFrameHandler
    ) -> None:
        self.date_utility = date_utility
        self.dataframe_handler = dataframe_handler
    
    def get_today_str(self) -> str:
        try:
            return self.date_utility.get_today_str()
        except Exception as error:
            raise Exception(f"Error in (Utilities) task in (get_today_str) method: {error}")
        
    def get_today_str_with_time(self) -> str:
        try:
            return self.date_utility.get_today_str_with_time()
        except Exception as error:
            raise Exception(f"Error in (Utilities) task in (get_today_str_with_time) method: {error}")
    
    def get_today_datetime(self) -> date:
        try:
            return self.date_utility.get_today_datetime()
        except Exception as error:
            raise Exception(f"Error in (Utilities) task in (get_today_datetime) method: {error}")
        
    def convert_to_datetime(self, date: str) -> date:
        try:
            return self.date_utility.convert_to_datetime(date)
        except Exception as error:
            raise Exception(f"Error in (Utilities) task in (convert_to_datetime) method: {error}")
        
    def convert_to_string(self, date: datetime) -> str:
        try:
            return self.date_utility.convert_to_string(date)
        except Exception as error:
            raise Exception(f"Error in (Utilities) task in (convert_to_string) method: {error}")
        
    def is_date(self, date: str) -> bool:
        try:
            return self.date_utility.is_date(date)
        except Exception as error:
            raise Exception(f"Error in (Utilities) task in (is_date) method: {error}")
    
    def convert_df_to_str(self, df: DataFrame) -> str:
        try:
            return self.dataframe_handler.convert_to_string(df)
        except Exception as error:
            raise Exception(f"Error in (Utilities) task in (convert_df_to_str) method: {error}")
