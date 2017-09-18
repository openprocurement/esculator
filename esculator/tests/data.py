# -*- coding: utf-8 -*-
from datetime import datetime


DISCOUNT_RATE = 0.125
ANNUAL_COSTS_REDUCTION = [92.47] + [250] * 20

BASE_BID = {'NBUdiscountRate': DISCOUNT_RATE,
            'annualCostsReduction': ANNUAL_COSTS_REDUCTION,
            'yearlyPaymentsPercentage': 0.70,
            'contractDuration': {'years': 2, 'days': 10},
            'announcementDate': datetime(2017, 8, 18)}

CONTRACT_DURATION = {
    'input': [
        {'years': 15, 'days': 0}, {'years': 0, 'days': 1},
        {'years': 3, 'days': 11}, {'years': 3, 'days': 12},
        {'years': 3, 'days': 13}, {'years': 3, 'days': 14},
        {'years': 3, 'days': 15}, {'years': 4, 'days': 15},
        {'years': 5, 'days': 15}, {'years': 6, 'days': 15},
        {'years': 7, 'days': 15},
    ],
    'expected_results': [
        {'amountContract': '2625.00297260274',
         'amountPerformance': '650.19504129090'},
        {'amountContract': '0.47947407407',
         'amountPerformance': '1810.49606787280'},
        {'amountContract': '530.27694520548',
         'amountPerformance': '1390.67586224709'},
        {'amountContract': '530.75639726027',
         'amountPerformance': '1390.35400799300'},
        {'amountContract': '531.23584931507',
         'amountPerformance': '1390.03215373892'},
        {'amountContract': '531.71530136986',
         'amountPerformance': '1389.71029948483'},
        {'amountContract': '532.19475342466',
         'amountPerformance': '1389.38844523075'},
        {'amountContract': '707.19475342466',
         'amountPerformance': '1280.67323051781'},
        {'amountContract': '882.19475342466',
         'amountPerformance': '1184.03748410631'},
        {'amountContract': '1057.19475342466',
         'amountPerformance': '1098.13904285164'},
        {'amountContract': '1232.19475342466',
         'amountPerformance': '1021.78487284750'},
    ]
}

ANNOUNCEMENT_DATE = {
    'input': [
        datetime(2017, 5, 2), datetime(2017, 5, 3), datetime(2017, 5, 4),
        datetime(2017, 5, 5), datetime(2017, 5, 6), datetime(2017, 5, 7),
        datetime(2017, 5, 8), datetime(2017, 5, 9), datetime(2017, 5, 10),
        datetime(2017, 5, 11),
    ],
    'expected_results': [
        {'amountContract': '303.01667123288',
         'amountPerformance': '1493.11261864549'},
        {'amountContract': '303.49612328767',
         'amountPerformance': '1493.29714530232'},
        {'amountContract': '303.97557534247',
         'amountPerformance': '1493.48174786072'},
        {'amountContract': '304.45502739726',
         'amountPerformance': '1493.66642643300'},
        {'amountContract': '304.93447945205',
         'amountPerformance': '1493.85118113158'},
        {'amountContract': '305.41393150685',
         'amountPerformance': '1494.03601206895'},
        {'amountContract': '305.89338356164',
         'amountPerformance': '1494.22091935769'},
        {'amountContract': '306.37283561644',
         'amountPerformance': '1494.40590311049'},
        {'amountContract': '306.85228767123',
         'amountPerformance': '1494.59096344011'},
        {'amountContract': '307.33173972603',
         'amountPerformance': '1494.77610045941'},
    ]
}

PAYMENTS_PERCENTAGE = {
    'input': [
        0.7100, 0.7200, 0.7300, 0.7400, 0.7500,
        0.7600, 0.7700, 0.7800, 0.7900, 0.8000
    ],
    'expected_results': [
        {'amountContract': '359.86602876712',
         'amountPerformance': '1509.25419393209'},
        {'amountContract': '364.93456438356',
         'amountPerformance': '1505.00489590214'},
        {'amountContract': '370.00310000000',
         'amountPerformance': '1500.75559787220'},
        {'amountContract': '375.07163561644',
         'amountPerformance': '1496.50629984225'},
        {'amountContract': '380.14017123288',
         'amountPerformance': '1492.25700181231'},
        {'amountContract': '385.20870684932',
         'amountPerformance': '1488.00770378236'},
        {'amountContract': '390.27724246575',
         'amountPerformance': '1483.75840575242'},
        {'amountContract': '395.34577808219',
         'amountPerformance': '1479.50910772247'},
        {'amountContract': '400.41431369863',
         'amountPerformance': '1475.25980969253'},
        {'amountContract': '405.48284931507',
         'amountPerformance': '1471.01051166258'},
    ]
}
