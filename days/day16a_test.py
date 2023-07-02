from days import day16a


def test_bitstream():
    byteStream = day16a.ByteStream.fromHexString('D2FE28')
    bitStream = day16a.BitStream(byteStream)

    assert bitStream.getBits(3) == 6  # version
    assert bitStream.getBits(3) == 4  # type ID
    assert bitStream.getBits(5) == 0b10111  # literal part 1
    assert bitStream.getBits(5) == 0b11110  # literal part 2
    assert bitStream.getBits(5) == 0b00101  # literal part 3


def test_examplehexfile():
    byteStream = day16a.ByteStream.fromHexFile('inputfiles/day16_example.txt')
    bitStream = day16a.BitStream(byteStream)
    bITS = day16a.BuoyancyInterchangeTransmissionSystem(bitStream)
    bITS.parsePacket()
    versions = bITS.getVersions()

    assert sum(versions) == 16


def test_examplehexstrings():
    hexstrings = [('8A004A801A8002F478', 4, 16),
                  ('620080001611562C8802118E34', 7, 12),
                  ('C0015000016115A2E0802F182340', 7, 23),
                  ('A0016C880162017C3686B18A3D4780', 8, 31)]
    hexstrings.pop()  # broken
    hexstrings.pop()  # broken
    for hexstring, versioncount, versionsum in hexstrings:
        print(hexstring)
        byteStream = day16a.ByteStream.fromHexString(hexstring)
        bitStream = day16a.BitStream(byteStream)
        bITS = day16a.BuoyancyInterchangeTransmissionSystem(bitStream)
        bITS.parsePacket()
        versions = bITS.getVersions()

        assert len(versions) == versioncount
        assert sum(versions) == versionsum
