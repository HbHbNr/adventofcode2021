from util import tokenstream


def test_tokenstreamstring1():
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
    try:
        # buffer is empty now and raises StopIteration exception
        next(stream)
        assert False
    except StopIteration:
        assert True


def test_tokenstreamstring2():
    # test edge case where integer is end of string
    stream = tokenstream.TokenStream('[[119').stream()

    assert next(stream) == tokenstream.Token(tokenstream.TokenType.SQUARE_BRACKET_OPEN, 0)
    assert next(stream) == tokenstream.Token(tokenstream.TokenType.SQUARE_BRACKET_OPEN, 0)
    assert next(stream) == tokenstream.Token(tokenstream.TokenType.INTEGER, 119)
    try:
        # buffer is empty now and raises StopIteration exception
        next(stream)
        assert False
    except StopIteration:
        assert True
