from util import bytestream, bitstream


def test_bitstream1():
    byteStream = bytestream.ByteStream.fromHexString('D2FE28')
    bitStream = bitstream.BitStream(byteStream)

    assert bitStream.getBits(3) == 6  # version
    assert bitStream.getBits(3) == 4  # type ID
    assert bitStream.getBits(5) == 0b10111  # literal part 1
    assert bitStream.getBits(5) == 0b11110  # literal part 2
    assert bitStream.getBits(5) == 0b00101  # literal part 3


def test_bitstream2():
    byteStream = bytestream.ByteStream.fromHexString('38006F45291200')
    bitStream = bitstream.BitStream(byteStream)

    assert bitStream.getBits(3) == 1  # version
    assert bitStream.getBits(3) == 6  # type ID
    assert bitStream.getBits(1) == 0  # type length ID
    assert bitStream.getBits(15) == 27  # length of sub packages
    assert bitStream.getBits(11) == 0b11010001010  # literal A
    assert bitStream.getBits(16) == 0b0101001000100100  # literal B
    assert bitStream.getBits(7) == 0  # padding


def test_bitstream3():
    byteStream = bytestream.ByteStream.fromHexString('EE00D40C823060')
    bitStream = bitstream.BitStream(byteStream)

    assert bitStream.getBits(3) == 7  # version
    assert bitStream.getBits(3) == 3  # type ID
    assert bitStream.getBits(1) == 1  # type length ID
    assert bitStream.getBits(11) == 3  # number of sub packages
    assert bitStream.getBits(11) == 0b01010000001  # literal A
    assert bitStream.getBits(11) == 0b10010000010  # literal A
    assert bitStream.getBits(11) == 0b00110000011  # literal A
    assert bitStream.getBits(5) == 0  # padding
