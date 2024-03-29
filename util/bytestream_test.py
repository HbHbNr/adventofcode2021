"""Unit tests for the ByteStream class"""
import unittest
from util import bytestream


class TestByteStream(unittest.TestCase):

    def testByteStreamFromHexString(self):
        stream = bytestream.ByteStream.fromHexString('D2FE28').stream()

        assert next(stream) == 0xd2
        assert next(stream) == 0xfe
        assert next(stream) == 0x28
        with self.assertRaises(StopIteration):
            # buffer is empty now and raises StopIteration exception
            next(stream)

    def testByteStreamFromHexFile(self):
        # 8A004A801A8002F478
        stream = bytestream.ByteStream.fromHexFile('inputfiles/day16_example.txt').stream()

        assert next(stream) == 0x8a
        assert next(stream) == 0x00
        assert next(stream) == 0x4a
        assert next(stream) == 0x80
        assert next(stream) == 0x1a
        assert next(stream) == 0x80
        assert next(stream) == 0x02
        assert next(stream) == 0xf4
        assert next(stream) == 0x78
        with self.assertRaises(StopIteration):
            # buffer is empty now and raises StopIteration exception
            next(stream)
