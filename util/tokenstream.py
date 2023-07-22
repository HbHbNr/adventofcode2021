"""Classes for tokens and token streams"""
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


class TokenStream:
    # pylint: disable=too-few-public-methods

    def __init__(self, tokenString: str) -> None:
        self._tokens: List[Token] = []
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
            yield token
