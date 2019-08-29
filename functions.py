def remove_non_ascii(text):
    """Removes non-ascii text and returns english vowel or blank in their place."""
    temp = []
    for i in text:
        if ord(i) < 128:
            temp.append(i)
        elif ord(i) in [232,233,234,235]:
            temp.append('e')
        elif ord(i) in [224,225,226,227,228,229]:
            temp.append('a')
        elif ord(i) in [236,237,238,239]:
            temp.append('i')
        elif ord(i) in [242,243,244,245,246]:
            temp.append('o')
        elif ord(i) == 241:
            temp.append('n')
        else:
            temp.append(' ')
    return temp

def list_to_name(list):
    """Converts a list to a name."""
    x = ''.join(list)
    return x
