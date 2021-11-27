from main import Solution
import logging


o = Solution()


def test_main():
    assert o.twoSum([2,7,11,15], 9) == [0,1]
    assert o.twoSum([3,2,4], 6) == [1,2]
    assert o.twoSum([3,3], 6) == [0,1]
    assert o.twoSum([3,3,4,8], 6) == [0,1]
    assert o.twoSum([3,4,5,3,7,8], 6) == [0,3]
    assert o.twoSum([3,4,6,5,3,7,8], 6) == [0,4]
    assert o.twoSum([6,3,4,5,3,7,8], 6) == [1,4]
    assert o.twoSum([2,4,8,7,11,15,109], 9) == [0,3]
    assert o.twoSum([2,4,8,7,11,15,-109], 9) == [0,3]
    assert o.twoSum([2,4,8,7,11,15,110], 9) == None
    assert o.twoSum([2,4,8,7,11,15,-110], 9) == None
    assert o.twoSum([2,4,110,8,7,11,15], 9) == None
    assert o.twoSum([2,4,-110,8,7,11,15], 9) == None
    assert o.twoSum([110,2,4,8,7,11,15], 9) == None
    assert o.twoSum([-110,2,4,8,7,11,15], 9) == None
    assert o.twoSum([9], 9) == None
    assert o.twoSum([4,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                    1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                    1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                    1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                    1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                    1,1,1,1,1], 9) == None
    assert o.twoSum([4,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                    1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                    1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                    1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                    1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                    1,1,1,1], 9) == [0,1]
    assert o.twoSum([2,1,6,7,8,108,15], 109) == [1,5]
    assert o.twoSum([2,-1,6,7,8,-108,15], -109) == [1,5]
    assert o.twoSum([2,2,6,7,8,108,15], 110) == None
    assert o.twoSum([2,-2,6,7,8,-108,15], -110) == None


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(levelname)-8s %(message)s',
                            datefmt='\033[36m%Y-%m-%d %H:%M:%S')
    try:
        test_main()
        logger.info('\x1b[32mPASSED')
    except:
        logger.error(f"\x1b[31mFAILED", exc_info=True)