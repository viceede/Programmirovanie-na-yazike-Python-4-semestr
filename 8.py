def main(hex_str):
    num = int(hex_str, 16)
    b1 = num & 0xF
    rest = num >> 4
    result = (b1 << 20) | rest
    return '0x' + format(result, 'x')

print(main('0x7ece'))
print(main('0x525e'))
print(main('0x608a'))
print(main('0x7bc5'))