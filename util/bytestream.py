from typing import Generator
from days import util


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
