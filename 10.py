def is_column_empty(table, col_index):
    """Check if all cells in column are None."""
    return all(row[col_index] is None for row in table)


def remove_empty_columns(table):
    """Remove columns where all cells are None."""
    if not table:
        return table

    empty_cols = [
        i for i in range(len(table[0]))
        if is_column_empty(table, i)
    ]
    for col in reversed(empty_cols):
        for row in table:
            del row[col]
    return table


def remove_duplicate_rows(table):
    """Remove duplicate rows keeping first occurrence."""
    seen = set()
    return [
        row for row in table
        if not (tuple(row) in seen or seen.add(tuple(row)))
    ]


def transform_percentage(value):
    """Convert numeric string to percentage (e.g., 0.37 -> '37%')."""
    try:
        return f"{round(float(value) * 100)}%"
    except (ValueError, TypeError):
        return value


def transform_boolean(value):
    """Convert 'да'/'нет' to 'true'/'false'."""
    if value is None:
        return None
    return 'true' if value.lower() == 'да' else 'false'


def transform_name(name):
    """Format name from 'Ф.И.О.' to 'Фамилия И.О.'."""
    if name is None:
        return None
    parts = name.split()
    if len(parts) >= 2:
        last_name = parts[-1]
        initials = '.'.join(p[0] for p in parts[:-1]) + '.'
        return f"{last_name} {initials}"
    return name


def transform_email(email):
    """Extract domain from email address."""
    if email is None:
        return None
    return email.split('@')[-1] if '@' in email else email


def transform_row(row):
    """Apply all transformations to a single row."""
    return [
        transform_percentage(row[0]),
        transform_boolean(row[1]),
        transform_name(row[2]),
        transform_email(row[3])
    ]


def main(table):
    """Main processing pipeline: clean and transform table data."""
    if not table:
        return []

    table = remove_empty_columns(table)
    table = remove_duplicate_rows(table)
    return [transform_row(row) for row in table]

input_table1 = [
        ["0.368", "нет", "P.C. Дувегев", None, "duvegev57@mail.ru"],
        ["0.335", "да", "C.Y. Гелак", None, "gelak35@mail.ru"],
        ["0.368", "нет", "P.C. Дуветев", None, "duvegev57@mail.ru"],
        ["0.841", "да", "Д.С. Федов", None, "fedov34@yandex.ru"],
        ["0.368", "нет", "P.C. Дуветев", None, "duvegev57@mail.ru"],
        ["0.282", "да", "С.Д. Зофяк", None, "zofak48@yandex.ru"]
    ]

print(main(input_table1))