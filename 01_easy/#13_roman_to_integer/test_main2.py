from time import time
from main2 import Solution
import logging

o = Solution()


def test_main():
    for i in range(1000):
        assert o.romanToInt("III") == 3
        assert o.romanToInt("IV") == 4
        assert o.romanToInt("IX") == 9
        assert o.romanToInt("LVIII") == 58
        assert o.romanToInt("MCMXCIV") == 1994
        # assert o.romanToInt("MCSMXCIV") is None
        assert o.romanToInt("MMMCMXCIX") == 3999
        assert o.romanToInt("MMMM") == 4000
        assert o.romanToInt("MMMDCCCLXXXVIII") == 3888
        assert o.romanToInt("MMMMDCCCLXXXVIII") is None


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
