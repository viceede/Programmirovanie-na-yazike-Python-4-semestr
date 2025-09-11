# Каждое множество описывает путь до листа
s = (
    {'YAML', 'POD', 1965, 1958},     # 0
    {'CSV', 'POD', 1965, 1958},      # 1
    {'ASP', 'POD', 1965, 1958},      # 2
    {'POD', 1965, 1974},             # 3
    {'POD', 1965, 2008},             # 4
    {'POD', 1961},                   # 5
    {'YAML', 'REBOL', 1965},         # 6
    {'CSV', 'REBOL', 1965, 1958},    # 7
    {'CSV', 'REBOL', 1965, 1974},    # 8
    {'CSV', 'REBOL', 1965, 2008},    # 9
    {'ASP', 'REBOL', 1965},          # 10
    {'REBOL', 1961},                 # 11
    {'SCSS', 1965, 1958, 'CSV'},     # 12
)

def main(r):
    s1 = set(r)
    for i in range(len(s)):
        if s[i].issubset(s1):
            return i

print(main(['YAML', 2008, 'GRACE', 'POD', 1961]))   # 5
print(main(['CSV', 1958, 'GRACE', 'SCSS', 1965]))   # 12
print(main(['ASP', 2008, 'GRACE', 'POD', 1965]))    # 4
print(main(['ASP', 1974, 'GRACE', 'REBOL', 1961]))  # 11
print(main(['ASP', 2008, 'GRACE', 'REBOL', 1965]))  # 10
