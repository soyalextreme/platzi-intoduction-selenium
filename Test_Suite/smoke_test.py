from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertion_test import AssertionTest
from search_test import SearchTest

assertion_test = TestLoader().loadTestsFromTestCase(AssertionTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTest)

smoke_test = TestSuite([assertion_test, search_test])

kwargs = {
    "output": "smoke report"
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)