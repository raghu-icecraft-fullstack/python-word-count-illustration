def read_file(file: str) -> list:
    try:
        f = open(file, "r", encoding="utf-8")
        result = f.read()
        return result
    except IOError as e:
        print(f"Unable to read file {file}")
        print(e)