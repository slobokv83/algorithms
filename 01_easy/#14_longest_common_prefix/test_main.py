from main import Solution
import logging

o = Solution()


def test_main():
    assert o.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert o.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert o.longestCommonPrefix(["ffflower", "ffflow", "ffflight"]) == "fffl"
    assert o.longestCommonPrefix(["fllowwwer", "fllowww", "fllowwwight"]) ==\
        "fllowww"
    assert o.longestCommonPrefix(["frlower", "fflow", "fflight"]) == "f"
    assert o.longestCommonPrefix(["fllowwwer",
                                  "rllowww",
                                  "fllowwwightaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                  "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
                                  "cccccccccccccccccccccccccccccccccccccccc"
                                  "dddddddddddddddddddddddddddddddddddddddd"
                                  "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"]
                                 ) is None
    assert o.longestCommonPrefix(["flower", "flow", "flight"] * 67) is None
    assert o.longestCommonPrefix([""]) == ""
    assert o.longestCommonPrefix(["a"]) == "a"
    assert o.longestCommonPrefix(["abc"]) == "abc"
    assert o.longestCommonPrefix(["flower", "flower", "flower", "flower"]) ==\
        "flower"
    assert o.longestCommonPrefix(["c", "c"]) == "c"
    assert o.longestCommonPrefix(["abc", "abc"]) == "abc"
    assert o.longestCommonPrefix(["abc", "vabc"]) == ""
    assert o.longestCommonPrefix(["a", "v"]) == ""
    assert o.longestCommonPrefix(["", "v"]) == ""
    assert o.longestCommonPrefix(["a", ""]) == ""
    assert o.longestCommonPrefix(["aaa", "aa", "aaa"]) == "aa"
    assert o.longestCommonPrefix(["a", "a", "b"]) == ""


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
