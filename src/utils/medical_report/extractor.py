import re
from utils.medical_report.patterns import medical_patterns


class MedicalExtractor:
    """
    """
    def __init__(self, text: str) -> None:
        """
        """
        self.text = text

    def base_extractor(self, pattern: str) -> str:
        """
        """
        return re.search(pattern, self.text)

    def extract_clinical_history_id(self) -> str:
        """
        """
        return self.base_extractor(medical_patterns["clinical_history_id"])

    def extract_patient_id(self) -> str:
        """
        """
        return self.base_extractor(medical_patterns["patient_id"])
