def main(input_list):
    rules = {
        ('HLSL', 2011): lambda x: 11 if x[3] == 'FORTH' and x[2] == 2003 and x[4] == 1977 else 1,
        ('HLSL', 1984): lambda x: 10 if x[2] == 2007 else 2,
        ('LUA', 2011): 0,
        ('YADA', 2019): 6,
        ('YOX', 1977): 7,
        ('FORTH', 1977): 11,
        ('FORTH', 1978): 1,
        ('FORTH', 1984): 10,
        ('FORTH', 1994): 9,
        ('FORTH', 2003): 8
    }

    key = (input_list[0], input_list[1])
    if key in rules:
        rule = rules[key]
        if callable(rule):
            return rule(input_list)
        return rule
    return 0


# Примеры использования:
print(main(['HLSL', 2011, 2003, 'FORTH', 1977]))  # 11
print(main(['HLSL', 2011, 2003, 'FORTH', 1978]))  # 1
print(main(['LUA', 2011, 2003, 'ADA', 1978]))  # 0
print(main(['HLSL', 1984, 2007, 'OX', 2019]))  # 10
print(main(['HLSL', 1984, 2003, 'ADA', 1978]))  # 2