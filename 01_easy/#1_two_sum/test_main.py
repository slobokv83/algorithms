from main import Solution
import logging

o = Solution()


def test_main():
    assert o.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert o.twoSum([3, 2, 4], 6) == [1, 2]
    assert o.twoSum([3, 3], 6) == [0, 1]
    assert o.twoSum([3, 3, 4, 8], 6) == [0, 1]
    assert o.twoSum([3, 4, 5, 3, 7, 8], 6) == [0, 3]
    assert o.twoSum([3, 4, 6, 5, 3, 7, 8], 6) == [0, 4]
    assert o.twoSum([6, 3, 4, 5, 3, 7, 8], 6) == [1, 4]
    assert o.twoSum([2, 4, 8, 7, 11, 15, 10**9], 9) == [0, 3]
    assert o.twoSum([2, 4, 8, 7, 11, 15, -10**9], 9) == [0, 3]
    assert o.twoSum([2, 4, 8, 7, 11, 15, 10**9 + 1], 9) is None
    assert o.twoSum([2, 4, 8, 7, 11, 15, -10**9 - 1], 9) is None
    assert o.twoSum([2, 4, 10**9 + 1, 8, 7, 11, 15], 9) is None
    assert o.twoSum([2, 4, -10**9 - 1, 8, 7, 11, 15], 9) is None
    assert o.twoSum([10**9 + 1, 2, 4, 8, 7, 11, 15], 9) is None
    assert o.twoSum([-10**9 - 1, 2, 4, 8, 7, 11, 15], 9) is None
    assert o.twoSum([9], 9) is None
    assert o.twoSum([4, 5, *range(10**4 - 1)], 9) is None
    assert o.twoSum([4, 5, *range(10**4 - 2)], 9) == [0, 1]
    assert o.twoSum([2, 1, 6, 7, 8, 10**9 - 1, 15], 10**9) == [1, 5]
    assert o.twoSum([2, -1, 6, 7, 8, -10**9 + 1, 15], -10**9) == [1, 5]
    assert o.twoSum([2, 2, 6, 7, 8, 10**9 - 1, 15], 10**9 + 1) is None
    assert o.twoSum([2, -2, 6, 7, 8, -10**9 + 1, 15], -10**9 - 1) is None


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
