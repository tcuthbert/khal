def echo(text: str, fmt: str = "") -> str:
    if fmt == "":
        return text.strip()
    return fmt.format(text).strip()
