#!/usr/bin/env python3

import pandas as pd
import re

from utils.summary_report.summary_report_pattern import summary_report_pattern
from utils.summary_report.summary_report_columns import summary_report_columns


class SummaryReportExtractor:
    """
    """
    def __init__(self, text: str) -> None:
        """
        """
        self.text = text

    def generate_dataframe(self) -> None:
        """
        """
        summary_report_matches = re.findall(summary_report_pattern, self.text)
        summary_report_df = pd.DataFrame(summary_report_matches, columns=summary_report_columns)
        self.summary_report_df = summary_report_df

    def convert_column_types(self, numeric_cols: list) -> None:
        """
        """
        for col in numeric_cols:
            self.summary_report_df[col] = pd.to_numeric(self.summary_report_df[col])
            self.summary_report_df[col] = self.summary_report_df[col].str.replace(",", "")
