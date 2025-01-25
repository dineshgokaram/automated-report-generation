import os
from data_reader import read_data
from data_analyzer import analyze_data
from pdf_report_generator import generate_pdf_report

def main():
    # Define file paths
    data_file = "./data/sample_data.csv"
    report_file = "./reports/report.pdf"

    # Step 1: Read data
    data = read_data(data_file)

    # Step 2: Analyze data
    summary = analyze_data(data)

    # Step 3: Generate PDF report
    generate_pdf_report(summary, report_file)

if __name__ == "__main__":
    # Ensure directories exist
    os.makedirs("reports", exist_ok=True)
    main()
