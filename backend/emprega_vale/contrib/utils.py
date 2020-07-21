def to_camel(string: str) -> str:
    output = ''.join(x for x in string.title() if x.isalnum())
    return output[0].lower() + output[1:]
