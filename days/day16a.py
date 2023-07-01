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


if __name__ == '__main__':
    from days import util

    byteStream = ByteStream.fromHexFile('inputfiles/day16_example1.txt')
    stream = byteStream.stream()
    b = next(stream, -1)
    while b >= 0:
        print(b)
        b = next(stream, -1)

    byteStream = ByteStream.fromHexString('D2FE28')
    stream = byteStream.stream()
    b = next(stream, -1)
    while b >= 0:
        print(b)
        b = next(stream, -1)
