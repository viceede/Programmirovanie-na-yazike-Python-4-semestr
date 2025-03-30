s = [
    {1978, 2003, 'LUA'},
    {1978, 2003, 'HLSL', 2011},
    {1978, 2003, 'HLSL', 1984},
    {1978, 2007, 2011},
    {1978, 2007, 1984, 'LUA'},
    {1978, 2007, 1984, 'HLSL'},
    {2019, 'LUA', 2011, 'ADA'},
    {2019, 'LUA', 2011, 'OX'},
    {2019, 'LUA', 2011, 'FORTH'},
    {2019, 'LUA', 1984},
    {2019, 'HLSL'},
    {1977}
]


def main(r):
    s1 = set(r)
    for i, v in enumerate(s):
        if not (len(v - s1)):
            return i

print(main(['HLSL', 2011, 2003, 'FORTH', 1977]))  # 11
print(main(['HLSL', 2011, 2003, 'FORTH', 1978]))  # 1
print(main(['LUA', 2011, 2003, 'ADA', 1978]))  # 0
print(main(['HLSL', 1984, 2007, 'OX', 2019]))  # 10
print(main(['HLSL', 1984, 2003, 'ADA', 1978]))  # 2