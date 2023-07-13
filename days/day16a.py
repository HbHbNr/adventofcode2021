from typing import Tuple, List
from util import util
from util import bytestream, bitstream


class BuoyancyInterchangeTransmissionSystem:

    def __init__(self, bitStream: bitstream.BitStream) -> None:
        self._bitstream = bitStream
        self._versions: List[int] = []

    def parsePacket(self) -> int:
        totalBits = 6
        version = self._bitstream.getBits(3)
        typeID = self._bitstream.getBits(3)
        # print('v=', version, ' t=', typeID, sep='')
        self._versions.append(version)
        if typeID == 4:
            bits, literal = self.parseLiteral()
            totalBits += bits
            # print(literal)
        else:
            lengthTypeID = self._bitstream.getBits(1)
            totalBits += 1
            if lengthTypeID == 0:
                totalBits += self.parseOperator0()
            else:
                totalBits += self.parseOperator1()
        return totalBits

    def parseLiteral(self) -> Tuple[int, int]:
        # print('parseLiteral')
        totalBits = 0
        result = 0
        readMore = True
        while readMore:
            part = self._bitstream.getBits(5)
            result = result << 4
            result |= (part & 0b1111)
            totalBits += 5
            readMore = bool(part & 0b10000)
        return totalBits, result

    def parseOperator0(self) -> int:
        # print('parseOperator0')
        rawLength = self._bitstream.getBits(15)
        availableBits = rawLength
        while availableBits > 0:
            # print('  availableBits=', availableBits, sep='')
            availableBits -= self.parsePacket()
        return 15 + rawLength

    def parseOperator1(self) -> int:
        # print('parseOperator1')
        totalBits = 0
        subPacketsNumber = self._bitstream.getBits(11)
        for i in range(subPacketsNumber):
            totalBits += self.parsePacket()
        return 11 + totalBits

    def getVersions(self) -> Tuple[int, ...]:
        return tuple(self._versions)


if __name__ == '__main__':
    byteStream = bytestream.ByteStream.fromHexFile('inputfiles/day16_input.txt')
    bitStream = bitstream.BitStream(byteStream)
    bITS = BuoyancyInterchangeTransmissionSystem(bitStream)
    bITS.parsePacket()
    versions = bITS.getVersions()
    util.printresultline('16a', sum(versions))
