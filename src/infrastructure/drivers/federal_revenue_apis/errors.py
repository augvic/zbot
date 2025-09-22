class PositivoFederalRevenueApiErrors(Exception):
    
    def __init__(self, *args):
        super().__init__(*args)

class RequestError(PositivoFederalRevenueApiErrors):
    
    def __init__(self, error: str):
        super().__init__(f"Error while making request: {error}.")

class RequestResponseError(PositivoFederalRevenueApiErrors):
    
    def __init__(self, response: dict):
        super().__init__(f"Error in request response: {response.status_code} - {response.text}.")
