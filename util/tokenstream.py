"""Classes for tokens and token streams"""
from typing import Generator, NamedTuple, List, Optional
from enum import Enum


class TokenType(Enum):
    SQUARE_BRACKET_OPEN = 1
    SQUARE_BRACKET_CLOSE = 2
    COMMA = 3
    INTEGER = 4

    def toString(self) -> str:
        if self == TokenType.SQUARE_BRACKET_OPEN:
            return '['
        if self == TokenType.SQUARE_BRACKET_CLOSE:
            return ']'
        if self == TokenType.COMMA:
            return ','
        if self == TokenType.INTEGER:
            return 'I'
        raise ValueError(f'{self} has unknown TokenType')


class Token(NamedTuple):

    type: TokenType
    intvalue: int

    @classmethod
    def createBasic(cls, tokenString: str) -> 'Token':
        if tokenString == '[':
            tokenType = TokenType.SQUARE_BRACKET_OPEN
        elif tokenString == ']':
            tokenType = TokenType.SQUARE_BRACKET_CLOSE
        elif tokenString == ',':
            tokenType = TokenType.COMMA
        else:
            raise ValueError(f'{tokenString} has unknown TokenType')

        return Token(tokenType, 0)

    @classmethod
    def createInteger(cls, value: int) -> 'Token':
        return Token(TokenType.INTEGER, value)

    def isInteger(self):
        return self.type == TokenType.INTEGER

    def __str__(self):
        string = ''
        if self.type == TokenType.INTEGER:
            string = f'{self.type}({self.intvalue})'
        else:
            string = str(self.type)
        return string


class TokenStream:
    # pylint: disable=too-few-public-methods

    def __init__(self, tokenString: str, debugPrefix: Optional[str] = None) -> None:
        self._tokens: List[Token] = []
        self._debugPrefix: Optional[str] = debugPrefix
        i = 0
        while i < len(tokenString):
            if not str.isdecimal(tokenString[i]):
                self._tokens.append(Token.createBasic(tokenString[i]))
                i += 1
            else:
                value = 0
                while i < len(tokenString) and str.isdecimal(tokenString[i]):
                    value *= 10
                    value += int(tokenString[i])
                    i += 1
                self._tokens.append(Token.createInteger(value))

    def stream(self) -> Generator:
        for token in self._tokens:
            if self._debugPrefix is not None:
                print(self._debugPrefix, token, sep='')
            yield token
