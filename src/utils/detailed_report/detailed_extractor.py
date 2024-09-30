#!/usr/bin/env python3

import pandas as pd
import re
from utils.detailed_report.detailed_report_pattern import (
    detailed_report_pattern,
    detailed_report_regex
)


class DetailedReportExtractor:
    """
    """
    def __init__(self, text: str) -> None:
        """
        """
        self.text = text

    def generate_dataframe(self) -> None:
        """
        """
        detailed_report_matches = re.search(detailed_report_pattern, self.text, re.DOTALL)

        if detailed_report_matches:
            detailed_report_data = []

            for match in detailed_report_regex.findall(self.text):
                detailed_report_data.append(
                    {
                        'Batch': int(match[0]),
                        'Seq#': int(match[1]),
                        'Account': match[2],
                        'Amount_Pd': float(match[3].replace(",", "")) if match[3] else None,
                        'Check_Amt': float(match[4].replace(",", "")),
                        'Check#': int(match[5]),
                    }
                )

            detailed_report_df = pd.DataFrame(detailed_report_data).iloc[1:].reset_index(drop=True)

        else:
            detailed_report_df = None

        self.detailed_report_df = detailed_report_df
