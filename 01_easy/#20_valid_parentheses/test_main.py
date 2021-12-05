from main import Solution
import logging
from time import time

o = Solution()


def test_main():
    for i in range(1000):
        assert o.isValid("()") is True
        assert o.isValid("[]") is True
        assert o.isValid("{}") is True
        assert o.isValid("()[]{}") is True
        assert o.isValid("{[]}") is True
        assert o.isValid("([]{})") is True
        assert o.isValid("((([[[[{{{{{()[{}[]]}}}}}]]]])))") is True
        assert o.isValid("((([[[[{{{{{()[{{{}[][]}}]}}}}}]]]])))") is True
        assert o.isValid("((()((([[[]]])))))") is True
        assert o.isValid("((([[[[{{{{{()[{{{}[][]}]}}}}]]]])))") is False
        assert o.isValid("((([[[[{{{{{()[{}[]]}}}}}]]]])))]") is False
        assert o.isValid("(()))(") is False
        assert o.isValid("(]") is False
        assert o.isValid("(}") is False
        assert o.isValid("[)") is False
        assert o.isValid("[}") is False
        assert o.isValid("{)") is False
        assert o.isValid("{]") is False
        assert o.isValid("([)]") is False
        assert o.isValid("([[)]]") is False
        assert o.isValid("((([[[[{{{{{()[{}[][]}]}}}}]]]])))") is False
        assert o.isValid("((()((([[[]]]))))") is False
        assert o.isValid("([]{}]") is False
        assert o.isValid("(") is False
        assert o.isValid("[") is False
        assert o.isValid("{") is False
        assert o.isValid(")") is False
        assert o.isValid("]") is False
        assert o.isValid("}") is False
        assert o.isValid(")(") is False
        assert o.isValid("][") is False
        assert o.isValid("}{") is False
        assert o.isValid("((((((((") is False
        assert o.isValid("([{)(}])") is False
        assert o.isValid("(((([[[[{{{{{()[{}][]}}}}}]]]])))") is False
    # assert o.isValid("()[]{}.") is None
    # assert o.isValid("asdscvvvvvvfgyhjiop;1234567") is None


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='\033[36m%Y-%m-%d %H:%M:%S')
    try:
        start = time()
        test_main()
        logger.info(f'\x1b[32mPASSED time: {(time() - start) * 1000} ms')
    except Exception as e:
        logger.error(f"\x1b[31mFAILED \x1b[33m{e}", exc_info=True)
