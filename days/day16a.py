from typing import Generator


class ByteStream:

    def __init__(self, bs: bytes) -> None:
        self._bs = bs

    @classmethod
    def fromHexString(cls, hexString: str) -> 'ByteStream':
        bs: bytes = bytes.fromhex(hexString)
        return ByteStream(bs)

    @classmethod
    def fromHexFile(cls, hexInputfile: str) -> 'ByteStream':
        bs: bytes = util.readhexinputfile(hexInputfile)
        return ByteStream(bs)

    def stream(self) -> Generator:
        for b in self._bs:
            yield b


class BitStream:

    def __init__(self, byteStream: ByteStream):
        self._byteStream = byteStream.stream()
        self._bitmask = (0, 0b1, 0b11, 0b111, 0b1111, 0b11111, 0b111111, 0b1111111)
        self._buffer: int = 0
        self._availableBits: int = 0

    def getBits(self, number: int) -> int:
        print(f'getBits({number})')
        result = 0
        missingBits = number
        while missingBits > 0:
            if self._availableBits == 0:
                self._buffer = next(self._byteStream)
                self._availableBits = 8
                print('refilled')

            print(self._buffer, result, missingBits, self._availableBits)
            if missingBits < self._availableBits:
                buffer2 = self._buffer
                print("{0:b}".format(buffer2))
                buffer2 = buffer2 >> (self._availableBits - missingBits)
                print("{0:b}".format(buffer2))
                buffer2 &= self._bitmask[missingBits]
                print("{0:b}".format(buffer2))
                result = result << missingBits
                print("{0:b}".format(result))
                result |= buffer2
                print("{0:b}".format(result))
                self._availableBits -= missingBits
                missingBits = 0
                print('a')
            # missingBits >= availableBits
            elif self._availableBits == 8:
                result = result << 8
                result += self._buffer
                self._availableBits = 0
                missingBits -= 8
                print('b')
            # missingBits >= availableBits
            else:  # availableBits < 8
                buffer2 = self._buffer
                print("{0:b}".format(buffer2))
                buffer2 &= self._bitmask[self._availableBits]
                print("{0:b}".format(buffer2))
                result = result << self._availableBits
                print("{0:b}".format(result))
                result |= buffer2
                print("{0:b}".format(result))
                missingBits -= self._availableBits
                self._availableBits = 0
                print('c')
                pass
        return result


if __name__ == '__main__':
    from days import util

    # byteStream = ByteStream.fromHexFile('inputfiles/day16_example1.txt')
    # stream = byteStream.stream()
    # b = next(stream, -1)
    # while b >= 0:
    #     print(b)
    #     b = next(stream, -1)

    byteStream = ByteStream.fromHexString('D2FE28')
    bitStream = BitStream(byteStream)
    # b = next(stream, -1)
    # while b >= 0:
    #     print(b)
    #     b = next(stream, -1)
    for number in [3, 3, 5, 5, 5]:
        i = bitStream.getBits(number)
        print('->', i, "({0:b})".format(i))
