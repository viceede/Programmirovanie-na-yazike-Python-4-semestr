def main(table):
    output = []
    seen = {(None, ) * 6}
    for line in table:
        line = tuple(line)
        if line in seen:
            continue
        seen.add(line)
        date = line[3].split('-')
        output.append([
            '0' if line[0] == 'N' else '1',
            f'{float(line[1]):.4f}',
            f"{date[2]}/{date[1]}/{date[0][2:]}",
            ''.join((i for i in line[-1] if i.isdigit()))
        ])
    return output
