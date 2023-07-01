from typing import Generator


class ByteStream:

    def __init__(self, bs: bytes) -> None:
        self._bs = bs

    @classmethod
    def fromHexString(cls, hexString: str) -> 'ByteStream':
        bs = bytes.fromhex(hexString)
        byteStream = ByteStream(bs)
        return byteStream

    def getBytes(self) -> Generator:
        for b in self._bs:
            yield b


if __name__ == '__main__':
    from days import util

    bs: bytes = util.readhexinputfile('inputfiles/day16_example1.txt')
    # util.readhexinputfile('inputfiles/day16_input.txt')
    for i in range(len(bs)):
        print(bs[i], bin(bs[i]))

    byteStream = ByteStream.fromHexString('D2FE28')
    getBytes = byteStream.getBytes()
    b = next(getBytes, -1)
    while b >= 0:
        print(b)
        b = next(getBytes, -1)
