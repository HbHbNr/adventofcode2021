"""A class for byte streams"""
from typing import Generator
from util import util


class ByteStream:

    def __init__(self, _bytes: bytes) -> None:
        self._bytes = _bytes

    @classmethod
    def fromHexString(cls, hexString: str) -> 'ByteStream':
        _bytes: bytes = bytes.fromhex(hexString)
        return ByteStream(_bytes)

    @classmethod
    def fromHexFile(cls, hexInputfile: str) -> 'ByteStream':
        _bytes: bytes = util.readhexinputfile(hexInputfile)
        return ByteStream(_bytes)

    def stream(self) -> Generator:
        for byte in self._bytes:
            yield byte
