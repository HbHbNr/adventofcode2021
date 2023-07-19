from days import day16b
from util import bytestream, bitstream


def testExampleHexStrings():
    hexstrings = [('C200B40A82', 3),
                  ('04005AC33890', 54),
                  ('880086C3E88112', 7),
                  ('CE00C43D881120', 9),
                  ('D8005AC2A8F0', 1),
                  ('F600BC2D8F', 0),
                  ('9C005AC2F8F0', 0),
                  ('9C0141080250320F1802104A08', 1)]
    for hexstring, expectedresult in hexstrings:
        print('*****', hexstring)
        byteStream = bytestream.ByteStream.fromHexString(hexstring)
        bitStream = bitstream.BitStream(byteStream)
        bITS = day16b.BuoyancyInterchangeTransmissionSystem(bitStream)
        _, result = bITS.parsePacket()

        assert expectedresult == result


def testInput():
    byteStream = bytestream.ByteStream.fromHexFile('inputfiles/day16_input.txt')
    bitStream = bitstream.BitStream(byteStream)
    bITS = day16b.BuoyancyInterchangeTransmissionSystem(bitStream)
    _, result = bITS.parsePacket()

    assert result == 9485076995911
