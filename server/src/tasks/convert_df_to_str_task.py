from src.engines.dataframe_engine import DataFrameEngine
from src.engines.log_engine import LogEngine

from pandas import DataFrame

class ConvertDfToStrTask:
    
    def __init__(self,
        dataframe_engine: DataFrameEngine,
        log_engine: LogEngine
    ) -> None:
        self.dataframe_engine = dataframe_engine
        self.log_engine = log_engine
    
    def main(self, df: DataFrame) -> str:
        try:
            return self.dataframe_engine.convert_to_string(df)
        except Exception as error:
            self.log_engine.write_error(f"❌ Error in (ConvertDfToStrTask) task in (main) method: {error}")
            raise Exception(f"❌ Erro interno ao converter DataFrame em String. Contate o administrador.")
