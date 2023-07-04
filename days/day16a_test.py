from days import day16a


def test_bitstream1():
    byteStream = day16a.ByteStream.fromHexString('D2FE28')
    bitStream = day16a.BitStream(byteStream)

    assert bitStream.getBits(3) == 6  # version
    assert bitStream.getBits(3) == 4  # type ID
    assert bitStream.getBits(5) == 0b10111  # literal part 1
    assert bitStream.getBits(5) == 0b11110  # literal part 2
    assert bitStream.getBits(5) == 0b00101  # literal part 3


def test_bitstream2():
    byteStream = day16a.ByteStream.fromHexString('38006F45291200')
    bitStream = day16a.BitStream(byteStream)

    assert bitStream.getBits(3) == 1  # version
    assert bitStream.getBits(3) == 6  # type ID
    assert bitStream.getBits(1) == 0  # type length ID
    assert bitStream.getBits(15) == 27  # length of sub packages
    assert bitStream.getBits(11) == 0b11010001010  # literal A
    assert bitStream.getBits(16) == 0b0101001000100100  # literal B
    assert bitStream.getBits(7) == 0  # padding


def test_bitstream3():
    byteStream = day16a.ByteStream.fromHexString('EE00D40C823060')
    bitStream = day16a.BitStream(byteStream)

    assert bitStream.getBits(3) == 7  # version
    assert bitStream.getBits(3) == 3  # type ID
    assert bitStream.getBits(1) == 1  # type length ID
    assert bitStream.getBits(11) == 3  # number of sub packages
    assert bitStream.getBits(11) == 0b01010000001  # literal A
    assert bitStream.getBits(11) == 0b10010000010  # literal A
    assert bitStream.getBits(11) == 0b00110000011  # literal A
    assert bitStream.getBits(5) == 0  # padding


def test_examplehexfile():
    byteStream = day16a.ByteStream.fromHexFile('inputfiles/day16_example.txt')
    bitStream = day16a.BitStream(byteStream)
    bITS = day16a.BuoyancyInterchangeTransmissionSystem(bitStream)
    bITS.parsePacket()
    versions = bITS.getVersions()

    assert sum(versions) == 16


def test_examplehexstrings():
    hexstrings = [('D2FE28', 1, 6),
                  ('38006F45291200', 3, 9),
                  ('EE00D40C823060', 4, 14),
                  ('8A004A801A8002F478', 4, 16),
                  ('620080001611562C8802118E34', 7, 12),
                  ('C0015000016115A2E0802F182340', 7, 23),
                  ('A0016C880162017C3686B18A3D4780', 8, 31)]
    for hexstring, versioncount, versionsum in hexstrings:
        print('*****', hexstring)
        byteStream = day16a.ByteStream.fromHexString(hexstring)
        bitStream = day16a.BitStream(byteStream)
        bITS = day16a.BuoyancyInterchangeTransmissionSystem(bitStream)
        bITS.parsePacket()
        versions = bITS.getVersions()

        assert len(versions) == versioncount
        assert sum(versions) == versionsum
