"""Unit tests for the Token and TokenStream classes"""
import pytest
from util import tokenstream


def testTokenStreamNormal():
    stream = tokenstream.TokenStream('[[1,9],[18,105]]').stream()

    assert next(stream) == tokenstream.Token(tokenstream.TokenType.SQUARE_BRACKET_OPEN, 0)
    assert next(stream) == tokenstream.Token(tokenstream.TokenType.SQUARE_BRACKET_OPEN, 0)
    assert next(stream) == tokenstream.Token(tokenstream.TokenType.INTEGER, 1)
    assert next(stream) == tokenstream.Token(tokenstream.TokenType.COMMA, 0)
    assert next(stream) == tokenstream.Token(tokenstream.TokenType.INTEGER, 9)
    assert next(stream) == tokenstream.Token(tokenstream.TokenType.SQUARE_BRACKET_CLOSE, 0)
    assert next(stream) == tokenstream.Token(tokenstream.TokenType.COMMA, 0)
    assert next(stream) == tokenstream.Token(tokenstream.TokenType.SQUARE_BRACKET_OPEN, 0)
    assert next(stream) == tokenstream.Token(tokenstream.TokenType.INTEGER, 18)
    assert next(stream) == tokenstream.Token(tokenstream.TokenType.COMMA, 0)
    assert next(stream) == tokenstream.Token(tokenstream.TokenType.INTEGER, 105)
    assert next(stream) == tokenstream.Token(tokenstream.TokenType.SQUARE_BRACKET_CLOSE, 0)
    assert next(stream) == tokenstream.Token(tokenstream.TokenType.SQUARE_BRACKET_CLOSE, 0)
    with pytest.raises(StopIteration):
        # buffer is empty now and raises StopIteration exception
        next(stream)


def testTokenStreamIntegerAtEnd():
    stream = tokenstream.TokenStream('[[119').stream()

    assert next(stream) == tokenstream.Token(tokenstream.TokenType.SQUARE_BRACKET_OPEN, 0)
    assert next(stream) == tokenstream.Token(tokenstream.TokenType.SQUARE_BRACKET_OPEN, 0)
    assert next(stream) == tokenstream.Token(tokenstream.TokenType.INTEGER, 119)
    with pytest.raises(StopIteration):
        # buffer is empty now and raises StopIteration exception
        next(stream)


def testTokenStreamUnknownToken():
    # test unknown token within the string
    with pytest.raises(ValueError):
        tokenstream.TokenStream('[[1,9]#[18,105]]').stream()


def testTokenStr():
    assert str(tokenstream.Token(tokenstream.TokenType.SQUARE_BRACKET_OPEN, 0)) == 'TokenType.SQUARE_BRACKET_OPEN'
    assert str(tokenstream.Token(tokenstream.TokenType.INTEGER, 1)) == 'TokenType.INTEGER(1)'
