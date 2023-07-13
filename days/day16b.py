from typing import Tuple, List
from util import util
from util import bytestream, bitstream
from functools import reduce


class BuoyancyInterchangeTransmissionSystem:

    def __init__(self, bitStream: bitstream.BitStream) -> None:
        self._bitstream = bitStream

    def parsePacket(self) -> Tuple[int, int]:
        totalBits = 6
        result = 0
        _ = self._bitstream.getBits(3)  # version
        typeID = self._bitstream.getBits(3)
        # print('v=', version, ' t=', typeID, sep='')
        if typeID == 4:
            bits, result = self.parseLiteral()
            totalBits += bits
        else:
            lengthTypeID = self._bitstream.getBits(1)
            totalBits += 1
            if lengthTypeID == 0:
                bits, results = self.parseOperator0()
                totalBits += bits
            else:
                bits, results = self.parseOperator1()
                totalBits += bits
            result = self.operator(typeID, results)
        # print(result)
        return totalBits, result

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

    def parseOperator0(self) -> Tuple[int, List[int]]:
        # print('parseOperator0')
        results: List[int] = []
        rawLength = self._bitstream.getBits(15)
        availableBits = rawLength
        while availableBits > 0:
            # print('  availableBits=', availableBits, sep='')
            bits, result = self.parsePacket()
            availableBits -= bits
            results.append(result)
        return 15 + rawLength, results

    def parseOperator1(self) -> Tuple[int, List[int]]:
        # print('parseOperator1')
        totalBits = 0
        results: List[int] = []
        subPacketsNumber = self._bitstream.getBits(11)
        for i in range(subPacketsNumber):
            bits, result = self.parsePacket()
            totalBits += bits
            results.append(result)
        return 11 + totalBits, results

    def operator(self, typeID: int, results: List[int]) -> int:
        if typeID == 0:
            return sum(results)
        elif typeID == 1:
            return reduce((lambda x, y: x * y), results)
        elif typeID == 2:
            return min(results)
        elif typeID == 3:
            return max(results)
        elif typeID == 5:
            return 1 if results[0] > results[1] else 0
        elif typeID == 6:
            return 1 if results[0] < results[1] else 0
        else:  # typeID == 7
            return 1 if results[0] == results[1] else 0


if __name__ == '__main__':
    byteStream = bytestream.ByteStream.fromHexFile('inputfiles/day16_input.txt')
    bitStream = bitstream.BitStream(byteStream)
    bITS = BuoyancyInterchangeTransmissionSystem(bitStream)
    _, result = bITS.parsePacket()
    util.printresultline('16b', result)
