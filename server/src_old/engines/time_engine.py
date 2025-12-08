from time import sleep

class TimeEngine:
    
    def sleep(self, seconds: float) -> None:
        try:
            sleep(seconds)
        except Exception as error:
            raise Exception(f"❌ Error in (TimeEngine) engine in (sleep) method: {error}")
