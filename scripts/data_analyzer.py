def analyze_data(data):
    """Analyzes the data and returns a summary."""
    if data is not None:
        summary = {
            "Total Entries": len(data),
            "Columns": list(data.columns),
            "Sample Data": data.head().to_dict(orient="records")
        }
        return summary
    else:
        print("No data to analyze.")
        return None
