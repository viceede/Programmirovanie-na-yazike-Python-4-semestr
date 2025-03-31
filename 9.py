def main(input_string):
    sections = input_string.strip()[2:-2].split('<section>')
    result = {}

    for section in sections:
        if not section.strip():
            continue

        to_part = section.split(')')[1].split('.')[0].strip()
        key = to_part.replace('to', '').strip()

        numbers_part = section.split('(')[1].split(')')[0]
        numbers = [int(num.strip()) for num in numbers_part.split('#')
                   if num.strip()]

        result[key] = numbers

    return result


# Примеры использования
string1 = ("[[<section> def list( #-4429 #-3508)to lein.</section>, "
           "<section>def list(#-7160#8029 #9821 ) to cerein.</section>, ]]")
string2 = ("[[ <section> def list(#323 #4596 ) to riendi. </section>, "
           "<section> def list( #-9665 #-4931 #-964) to lema. </section>, ]]")

print(main(string1))  # {'lein': [-4429, -3508], 'cerein': [-7160, 8029, 9821]}
print(main(string2))  # {'riendi': [323, 4596], 'lema': [-9665, -4931, -964]}