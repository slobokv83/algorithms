from main import Solution
import logging

o = Solution()


def test_main():
    assert o.mergeTwoLists([1, 2, 4], [1, 3, 4]) == [1, 1, 2, 3, 4, 4]
    # assert o.mergeTwoLists() == 0
    # assert o.mergeTwoLists() == 0
    # assert o.mergeTwoLists() == 0
    # assert o.mergeTwoLists() == 0
    # assert o.mergeTwoLists() == 0
    # assert o.mergeTwoLists() == 0
    # assert o.mergeTwoLists() == 0
    # assert o.mergeTwoLists() == 0
    # assert o.mergeTwoLists() is None
    # assert o.mergeTwoLists() is None
    # assert o.mergeTwoLists() is None
    # assert o.mergeTwoLists() is None
    # assert o.mergeTwoLists() is None


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
