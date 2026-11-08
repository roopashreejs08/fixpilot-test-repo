def normalize_csv_row(row):
    """Trim CSV fields and convert empty fields to None."""
    return [value.strip() if value.strip() != "" else None for value in row]
