from time import sleep

class TimeUtility:
    
    def sleep(self, seconds: float) -> None:
        try:
            sleep(seconds)
        except Exception as error:
            raise Exception(f"Error in (TimeUtility) component in (sleep) method: {error}.")
