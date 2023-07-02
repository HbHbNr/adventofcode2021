from typing import Generator, Tuple, List
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


class BitStream:

    def __init__(self, byteStream: ByteStream):
        self._byteStream = byteStream.stream()
        self._bitmask = (0, 0b1, 0b11, 0b111, 0b1111, 0b11111, 0b111111, 0b1111111)
        self._buffer: int = 0
        self._availableBits: int = 0

    def getBits(self, number: int) -> int:
        # print(f'getBits({number})')
        result = 0
        missingBits = number
        while missingBits > 0:
            if self._availableBits == 0:
                self._buffer = next(self._byteStream)
                self._availableBits = 8
                # print('refilled')

            # print(self._buffer, result, missingBits, self._availableBits)
            if missingBits < self._availableBits:
                buffer2 = self._buffer
                # print("{0:b}".format(buffer2))
                buffer2 = buffer2 >> (self._availableBits - missingBits)
                # print("{0:b}".format(buffer2))
                buffer2 &= self._bitmask[missingBits]
                # print("{0:b}".format(buffer2))
                result = result << missingBits
                # print("{0:b}".format(result))
                result |= buffer2
                # print("{0:b}".format(result))
                self._availableBits -= missingBits
                missingBits = 0
                # print('a')
            # missingBits >= availableBits
            elif self._availableBits == 8:
                result = result << 8
                result += self._buffer
                self._availableBits = 0
                missingBits -= 8
                # print('b')
            # missingBits >= availableBits
            else:  # availableBits < 8
                buffer2 = self._buffer
                # print("{0:b}".format(buffer2))
                buffer2 &= self._bitmask[self._availableBits]
                # print("{0:b}".format(buffer2))
                result = result << self._availableBits
                # print("{0:b}".format(result))
                result |= buffer2
                # print("{0:b}".format(result))
                missingBits -= self._availableBits
                self._availableBits = 0
                # print('c')
                pass
        return result


class BuoyancyInterchangeTransmissionSystem:

    def __init__(self, bitStream: BitStream) -> None:
        self._bitstream = bitStream
        self._versions: List[int] = []

    def parsePacket(self) -> int:
        totalBits = 6
        version = self._bitstream.getBits(3)
        typeID = self._bitstream.getBits(3)
        print('v=', version, ' t=', typeID, sep='')
        self._versions.append(version)
        if typeID == 4:
            bits, literal = self.parseLiteral()
            totalBits += bits
            print(literal)
        else:
            lengthTypeID = self._bitstream.getBits(1)
            totalBits += 1
            if lengthTypeID == 0:
                totalBits += self.parseOperator0()
            else:
                totalBits += self.parseOperator1()
        return totalBits

    def parseLiteral(self) -> Tuple[int, int]:
        print('parseLiteral')
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
        print('parseRawData')
        rawLength = self._bitstream.getBits(15)
        availableBits = rawLength
        while availableBits > 0:
            print('  availableBits=', availableBits, sep='')
            availableBits -= self.parsePacket()
        return rawLength

    def parseOperator1(self) -> int:
        print('parseSubPackets')
        totalBits = 0
        subPacketsNumber = self._bitstream.getBits(11)
        for i in range(subPacketsNumber):
            totalBits += self.parsePacket()
        return totalBits

    def getVersions(self) -> Tuple[int, ...]:
        return tuple(self._versions)


if __name__ == '__main__':
    byteStream = ByteStream.fromHexString('38006F45291200')
    bitStream = BitStream(byteStream)
    bITS = BuoyancyInterchangeTransmissionSystem(bitStream)
    bITS.parsePacket()
    print('sum:', sum(bITS._versions))
    print()

    byteStream = ByteStream.fromHexString('EE00D40C823060')
    bitStream = BitStream(byteStream)
    bITS = BuoyancyInterchangeTransmissionSystem(bitStream)
    bITS.parsePacket()
    print('sum:', sum(bITS._versions))
    print()
