from tabulate import tabulate

from pandas import DataFrame

class DataFrameEngine:
    
    def convert_to_string(self, df: DataFrame) -> str:
        try:
            return tabulate(df.to_dict("records"), headers="keys", tablefmt="github", showindex=False)
        except Exception as error:
            raise Exception(f"❌ Error in (DataFrameEngine) engine in (convert_to_string) method: {error}")
