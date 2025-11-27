from src.modules.dataframe_handler import DataFrameHandler
from pandas import DataFrame

class ConvertDfToStr:
    
    def __init__(self,
        dataframe_handler: DataFrameHandler
    ) -> None:
        self.dataframe_handler = dataframe_handler
    
    def main(self, df: DataFrame) -> str:
        try:
            return self.dataframe_handler.convert_to_string(df)
        except Exception as error:
            raise Exception(f"Error in (ConvertDfToStr) task in (main) method: {error}.")
