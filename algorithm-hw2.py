# Split in Half

def split_half(string):
    second_half_index = int((len(string)/2)+0.5) if len(string) % 2 != 0 else int((len(string)/2))
    return string[second_half_index:]+string[:second_half_index]

print(split_half("bbbbbcaaaaa")) # aaaaabbbbbc
print(split_half("bbbbbaaaaa")) # aaaaabbbbb


# Unique Characters in String

def is_unique(string):
    string_array = [*''.join(sorted(string))]
    this_char = ''
    for i in string_array:
        if this_char == i:
            return False
        else:
            this_char = i
    return True

print(is_unique("Toni")) # True
print(is_unique("Soontornsing")) # False -- I am not unique
print(is_unique("Erokhin")) # You are unique!