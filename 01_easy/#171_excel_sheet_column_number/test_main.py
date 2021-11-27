from main import Solution
import logging

o = Solution()


def test_main():
    assert o.titleToNumber() == 0
    assert o.titleToNumber() == 0
    assert o.titleToNumber() == 0
    assert o.titleToNumber() == 0
    assert o.titleToNumber() == 0
    assert o.titleToNumber() == 0
    assert o.titleToNumber() == 0
    assert o.titleToNumber() == 0
    assert o.titleToNumber() == 0
    assert o.titleToNumber() is None
    assert o.titleToNumber() is None
    assert o.titleToNumber() is None
    assert o.titleToNumber() is None
    assert o.titleToNumber() is None


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='\033[36m%Y-%m-%d %H:%M:%S')
    try:
        test_main()
        logger.info('\x1b[32mPASSED')
    except Exception as e:
        logger.error(f"\x1b[31mFAILED \x1b[33m{e}", exc_info=True)
