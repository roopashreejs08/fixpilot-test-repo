def normalize_csv_row(row):
    """Trim CSV fields and convert empty fields to None."""
    return [value.strip() for value in row]
