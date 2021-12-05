from time import time
from main2 import Solution
import logging

o = Solution()


def test_main():
    for i in range(1):
        assert o.strStr("mississippi", "issip") == 4
        assert o.strStr("aabaabbbaabbbbabaaab", "abaa") == 1
        assert o.strStr("hello", "ll") == 2
        assert o.strStr("aaaaa", "bba") == -1
        assert o.strStr("", "") == 0
        assert o.strStr("a" * 5 * 10**4, "a" * 4 * 10**4 + "b") == -1


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
