from data_processor import normalize_csv_row


def test_normalize_csv_row_handles_empty_fields():
    row = ["  Alice  ", "", "  42  "]

    result = normalize_csv_row(row)

    assert result == ["Alice", None, "42"]
