def try_float_cast(value: str) -> str | float:
    try:
        return float(value)
    except ValueError:
        return value
