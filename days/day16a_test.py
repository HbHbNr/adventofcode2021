from days import day16a
from util import bytestream, bitstream


def test_examplehexfile():
    byteStream = bytestream.ByteStream.fromHexFile('inputfiles/day16_example.txt')
    bitStream = bitstream.BitStream(byteStream)
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
        byteStream = bytestream.ByteStream.fromHexString(hexstring)
        bitStream = bitstream.BitStream(byteStream)
        bITS = day16a.BuoyancyInterchangeTransmissionSystem(bitStream)
        bITS.parsePacket()
        versions = bITS.getVersions()

        assert len(versions) == versioncount
        assert sum(versions) == versionsum


def test_input():
    byteStream = bytestream.ByteStream.fromHexFile('inputfiles/day16_input.txt')
    bitStream = bitstream.BitStream(byteStream)
    bITS = day16a.BuoyancyInterchangeTransmissionSystem(bitStream)
    bITS.parsePacket()
    versions = bITS.getVersions()

    assert len(versions) == 268
    assert sum(versions) == 897
