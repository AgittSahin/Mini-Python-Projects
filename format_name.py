def format_name(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    return f"Formatted name: {f_name} {l_name}"

formated_string = format_name("aGiT", "sAhIn")

print(formated_string)