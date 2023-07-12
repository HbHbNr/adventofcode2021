from typing import Generator, NamedTuple, List
from enum import Enum


class TokenType(Enum):
    SQUARE_BRACKET_OPEN = 1
    SQUARE_BRACKET_CLOSE = 2
    COMMA = 3
    INTEGER = 4


class Token(NamedTuple):

    type: TokenType
    intvalue: int

    @classmethod
    def createBasic(cls, s: str) -> 'Token':
        if s == '[':
            type = TokenType.SQUARE_BRACKET_OPEN
        elif s == ']':
            type = TokenType.SQUARE_BRACKET_CLOSE
        elif s == ',':
            type = TokenType.COMMA
        else:
            raise ValueError(f'{s} has unknown TokenType')

        return Token(type, 0)

    @classmethod
    def createInteger(cls, value: int) -> 'Token':
        return Token(TokenType.INTEGER, value)


class TokenStream:

    def __init__(self, s: str) -> None:
        self._tokens: List[Token] = []
        i = 0
        while i < len(s):
            if not str.isdecimal(s[i]):
                self._tokens.append(Token.createBasic(s[i]))
                i += 1
            else:
                value = 0
                while i < len(s) and str.isdecimal(s[i]):
                    value *= 10
                    value += int(s[i])
                    i += 1
                self._tokens.append(Token.createInteger(value))

    def stream(self) -> Generator:
        for token in self._tokens:
            yield token
