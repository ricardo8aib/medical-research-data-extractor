import re

detailed_report_pattern = r"Detail Report.*\* Grand Totals.*"
detailed_report_regex = re.compile(
    r"(\d+)\s+(\d+)\s+(\d+)\s+([\d,]+\.\d+|)\s+([\d,]+\.\d+)\s+(\d+)"
)
