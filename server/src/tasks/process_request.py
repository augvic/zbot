from src.components.request_processor.component import RequestProcessor

from src.components.request_processor.models import RequestProcessed

class ProcessRequest:
    
    def __init__(self) -> None:
        self.request_processor = RequestProcessor()
    
    def execute(self, content_type: str, expected_data: list[str], not_expected_data: list[str], expected_files: list[str], not_expected_files: list[str]) -> RequestProcessed:
        return self.request_processor.process(content_type, expected_data, not_expected_data, expected_files, not_expected_files)
