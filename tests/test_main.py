# -----------------------By Kit_Angel-------------------------
# ------------------https://t.me/Kit_Angel--------------------
import test_kvzu07, test_kpzu06, test_kpt10
import unittest

if __name__ == '__main__':

    res = unittest.TestLoader().discover(start_dir='.', pattern='test*.py')
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(res)
    """
    testCases = [test_kvzu07, test_kpzu06, test_kpt10]
    suites = []
    testLoad = unittest.TestLoader()

    for tc in testCases:
        suite = testLoad.loadTestsFromModule(tc)
        suites.append(suite)

    res_suite = unittest.TestSuite(suites)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(res_suite)
    """


