def main(value: int) -> str:
    """Transcode 27-bit word (fields S1..S6) and return decimal string.

    Field widths (bits, from least significant to most):
      S1: 3 bits   (bits 0..2)
      S2: 7 bits   (bits 3..9)
      S3: 1 bit    (bit 10)
      S4: 2 bits   (bits 11..12)
      S5: 6 bits   (bits 13..18)
      S6: 8 bits   (bits 19..26)

    Output layout (from most significant to least):
      S6 | S5 | S2 | S1 | S3 | S4
    """
    # extract source fields
    s1 = value & 0b111               # 3 bits
    s2 = (value >> 3) & 0x7F         # 7 bits
    s3 = (value >> 10) & 0x1         # 1 bit
    s4 = (value >> 11) & 0b11        # 2 bits
    s5 = (value >> 13) & 0x3F        # 6 bits
    s6 = (value >> 19) & 0xFF        # 8 bits

    # assemble result: shifts computed from target field positions
    result = (s6 << 19) | (s5 << 13) | (s2 << 6) | (s1 << 3) | (s3 << 2) | s4

    return str(result)


