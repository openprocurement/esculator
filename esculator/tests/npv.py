import unittest
from copy import deepcopy
from fractions import Fraction
from esculator import npv, escp
from esculator.tests.data import (
    CONTRACT_DURATION, ANNOUNCEMENT_DATE, PAYMENTS_PERCENTAGE, BASE_BID,
)

class TestCalculationsMixin(object):
    __test__ = False  # nosetests directive

    def test_calculations(self):
        for i, val in enumerate(self.test_data['input']):
            self.bid[self.field_name] = val

            amount_perfomance = npv(
                self.bid['contractDuration']['years'],
                self.bid['contractDuration']['days'],
                self.bid['yearlyPaymentsPercentage'],
                self.bid['annualCostsReduction'],
                self.bid['announcementDate'],
                self.bid['NBUdiscountRate'],
            )

            self.assertTrue(isinstance(amount_perfomance, Fraction))

            expected = self.test_data['expected_results'][i]['amountPerformance']
            self.assertEqual(humanize(amount_perfomance), expected)

            amount_contract = escp(
                self.bid['contractDuration']['years'],
                self.bid['contractDuration']['days'],
                self.bid['yearlyPaymentsPercentage'],
                self.bid['annualCostsReduction'],
                self.bid['announcementDate'],
            )

            self.assertTrue(isinstance(amount_contract, Fraction))

            expected = self.test_data['expected_results'][i]['amountContract']
            self.assertEqual(humanize(amount_contract), expected)


class ContractDurationTest(TestCalculationsMixin, unittest.TestCase):
    __test__ = True
    field_name = 'contractDuration'
    test_data = CONTRACT_DURATION
    bid = deepcopy(BASE_BID)


class YearlyPaymentsPercentageTest(TestCalculationsMixin, unittest.TestCase):
    __test__ = True
    field_name = 'yearlyPaymentsPercentage'
    test_data = PAYMENTS_PERCENTAGE
    bid = deepcopy(BASE_BID)


class AnnouncementDateTest(TestCalculationsMixin, unittest.TestCase):
    __test__ = True
    field_name = 'announcementDate'
    test_data = ANNOUNCEMENT_DATE
    bid = deepcopy(BASE_BID)


def humanize(value, precision=11):
    value = float(value)
    return '{:.{}f}'.format(value, precision)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ContractDurationTest))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
