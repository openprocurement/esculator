# -*- coding: utf-8 -*-
from datetime import datetime


DISCOUNT_RATE = 0.125

BASE_BID = {'NBUdiscountRate': DISCOUNT_RATE,
            'annualCostsReduction': [92.47] + [250] * 20,
            'yearlyPaymentsPercentage': 0.70,
            'contractDuration': {'years': 2, 'days': 10},
            'announcementDate': datetime(2017, 8, 18)}

CONTRACT_DURATION = {
    'input': [
        {'years': 0, 'days': 0}, {'years': 0, 'days': 1},
        {'years': 0, 'days': 8}, {'years': 0, 'days': 31},
        {'years': 0, 'days': 91}, {'years': 0, 'days': 92},
        {'years': 0, 'days': 180}, {'years': 0, 'days': 182},
        {'years': 0, 'days': 184}, {'years': 0, 'days': 256},
        {'years': 0, 'days': 360}, {'years': 0, 'days': 361},
        {'years': 0, 'days': 362}, {'years': 0, 'days': 363},
        {'years': 0, 'days': 364}, {'years': 1, 'days': 0},
        {'years': 2, 'days': 1}, {'years': 1, 'days': 8},
        {'years': 2, 'days': 31},{'years': 1, 'days': 91},
        {'years': 2, 'days': 92}, {'years': 1, 'days': 180},
        {'years': 2, 'days': 182}, {'years': 1, 'days': 184},
        {'years': 2, 'days': 256}, {'years': 1, 'days': 360},
        {'years': 2, 'days': 361}, {'years': 1, 'days': 362},
        {'years': 2, 'days': 363}, {'years': 1, 'days': 364},
        {'years': 3, 'days': 0}, {'years': 7, 'days': 1},
        {'years': 3, 'days': 8}, {'years': 8, 'days': 31},
        {'years': 4, 'days': 91}, {'years': 9, 'days': 92},
        {'years': 5, 'days': 180}, {'years': 10, 'days': 182},
        {'years': 6, 'days': 184}, {'years': 11, 'days': 256},
        {'years': 7, 'days': 360}, {'years': 12, 'days': 361},
        {'years': 8, 'days': 362}, {'years': 13, 'days': 363},
        {'years': 9, 'days': 364}, {'years': 10, 'days': 0},
        {'years': 10, 'days': 1}, {'years': 11, 'days': 8},
        {'years': 14, 'days': 30},{'years': 14, 'days': 31},
        {'years': 14, 'days': 90}, {'years': 14, 'days': 91},
        {'years': 14, 'days': 92}, {'years': 14, 'days': 180},
        {'years': 14, 'days': 181}, {'years': 14, 'days': 182},
        {'years': 14, 'days': 361}, {'years': 14, 'days': 362},
        {'years': 14, 'days': 363}, {'years': 14, 'days': 364},
        {'years': 15, 'days': 0}
    ],
    'expected_results': [
        {'amountContract': '0.00000000000',
         'amountPerformance': '1810.95435405817'},
        {'amountContract': '0.47947407407',
         'amountPerformance': '1810.49606787280'},
        {'amountContract': '3.83579259259',
         'amountPerformance': '1807.28806457523'},
        {'amountContract': '14.86369629630',
         'amountPerformance': '1796.74748231179'},
        {'amountContract': '43.63214074074',
         'amountPerformance': '1769.25031118977'},
        {'amountContract': '44.11161481481',
         'amountPerformance': '1768.79202500440'},
        {'amountContract': '86.30434246575',
         'amountPerformance': '1730.75511346897'},
        {'amountContract': '87.26324657534',
         'amountPerformance': '1729.94041988832'},
        {'amountContract': '88.22215068493',
         'amountPerformance': '1729.12572630767'},
        {'amountContract': '122.74269863014',
         'amountPerformance': '1699.79675740423'},
        {'amountContract': '172.60571232877',
         'amountPerformance': '1657.43269121038'},
        {'amountContract': '173.08516438356',
         'amountPerformance': '1657.02534442005'},
        {'amountContract': '173.56461643836',
         'amountPerformance': '1656.61799762973'},
        {'amountContract': '174.04406849315',
         'amountPerformance': '1656.21065083940'},
        {'amountContract': '174.52352054795',
         'amountPerformance': '1655.80330404908'},
        {'amountContract': '175.00297260274',
         'amountPerformance': '1655.39595725875'},
        {'amountContract': '350.48242465753',
         'amountPerformance': '1516.76226628463'},
        {'amountContract': '178.83858904110',
         'amountPerformance': '1652.13718293615'},
        {'amountContract': '364.86598630137',
         'amountPerformance': '1505.89968520929'},
        {'amountContract': '218.63310958904',
         'amountPerformance': '1618.32739933913'},
        {'amountContract': '394.11256164384',
         'amountPerformance': '1483.81243702275'},
        {'amountContract': '261.30434246575',
         'amountPerformance': '1584.11026895179'},
        {'amountContract': '437.26324657534',
         'amountPerformance': '1453.11558753945'},
        {'amountContract': '263.22215068493',
         'amountPerformance': '1582.66192480841'},
        {'amountContract': '472.74269863014',
         'amountPerformance': '1429.29837273721'},
        {'amountContract': '347.60571232877',
         'amountPerformance': '1518.93478249970'},
        {'amountContract': '523.08516438356',
         'amountPerformance': '1395.50367605835'},
        {'amountContract': '348.56461643836',
         'amountPerformance': '1518.21061042801'},
        {'amountContract': '524.04406849315',
         'amountPerformance': '1394.85996755018'},
        {'amountContract': '349.52352054795',
         'amountPerformance': '1517.48643835632'},
        {'amountContract': '525.00297260274',
         'amountPerformance': '1394.21625904202'},
        {'amountContract': '1225.48242465753',
         'amountPerformance': '1024.59792121607'},
        {'amountContract': '528.83858904110',
         'amountPerformance': '1391.64142500934'},
        {'amountContract': '1414.86598630137',
         'amountPerformance': '951.05679958049'},
        {'amountContract': '743.63310958904',
         'amountPerformance': '1258.93018757522'},
        {'amountContract': '1619.11256164384',
         'amountPerformance': '881.36067351043'},
        {'amountContract': '961.30434246575',
         'amountPerformance': '1143.34874877515'},
        {'amountContract': '1837.26324657534',
         'amountPerformance': '817.12906555064'},
        {'amountContract': '1138.22215068493',
         'amountPerformance': '1061.16755000753'},
        {'amountContract': '2047.74269863014',
         'amountPerformance': '763.74700436815'},
        {'amountContract': '1397.60571232877',
         'amountPerformance': '957.48662442295'},
        {'amountContract': '2273.08516438356',
         'amountPerformance': '714.14055865311'},
        {'amountContract': '1573.56461643836',
         'amountPerformance': '896.44297869644'},
        {'amountContract': '2449.04406849315',
         'amountPerformance': '680.27668462186'},
        {'amountContract': '1749.52352054795',
         'amountPerformance': '842.21724051892'},
        {'amountContract': '1750.00297260274',
         'amountPerformance': '842.07611953472'},
        {'amountContract': '1750.48242465753',
         'amountPerformance': '841.93499855052'},
        {'amountContract': '1928.83858904110',
         'amountPerformance': '793.16985845594'},
        {'amountContract': '2464.38653424658',
         'amountPerformance': '677.45744827975'},
        {'amountContract': '2464.86598630137',
         'amountPerformance': '677.36934714405'},
        {'amountContract': '2493.15365753425',
         'amountPerformance': '672.17138013828'},
        {'amountContract': '2493.63310958904',
         'amountPerformance': '672.08327900259'},
        {'amountContract': '2494.11256164384',
         'amountPerformance': '671.99517786690'},
        {'amountContract': '2536.30434246575',
         'amountPerformance': '664.68278360454'},
        {'amountContract': '2536.78379452055',
         'amountPerformance': '664.60447148393'},
        {'amountContract': '2537.26324657534',
         'amountPerformance': '664.52615936331'},
        {'amountContract': '2623.08516438356',
         'amountPerformance': '650.50828977336'},
        {'amountContract': '2623.56461643836',
         'amountPerformance': '650.42997765275'},
        {'amountContract': '2624.04406849315',
         'amountPerformance': '650.35166553213'},
        {'amountContract': '2624.52352054795',
         'amountPerformance': '650.27335341152'},
        {'amountContract': '2625.00297260274',
         'amountPerformance': '650.19504129090'}
    ]
}

ANNOUNCEMENT_DATE = {
    'input': [
        datetime(2017, 5, 2), datetime(2017, 5, 3), datetime(2017, 5, 4),
        datetime(2017, 5, 5), datetime(2017, 5, 6), datetime(2017, 5, 7),
        datetime(2017, 5, 8), datetime(2017, 5, 9), datetime(2017, 5, 10),
        datetime(2017, 5, 11), datetime(2017, 12, 30), datetime(2018, 1, 1),
        datetime(2018, 1, 31), datetime(2018, 2, 1), datetime(2018, 12, 30),
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
        {'amountContract': '419.04406849315',
         'amountPerformance': '1540.63620088962'},
        {'amountContract': '245.00297260274',
         'amountPerformance': '1471.31191860622'},
        {'amountContract': '259.38653424658',
         'amountPerformance': '1476.62410121389'},
        {'amountContract': '259.86598630137',
         'amountPerformance': '1476.80218008027'},
        {'amountContract': '419.04406849315',
         'amountPerformance': '1540.63620088962'},
    ]
}

PAYMENTS_PERCENTAGE = {
    'input': [
        0.0000, 0.0001, 0.0009, 0.0010, 0.0100, 0.1000, 0.0499, 0.0500, 0.4900,
        0.4999, 0.5000, 0.7100, 0.7200, 0.7300, 0.7400, 0.7500, 0.7600, 0.7700,
        0.7800, 0.7900, 0.8000, 0.8900, 0.8990, 0.8999, 0.9000
    ],
    'expected_results': [
        {'amountContract': '0.00000000000',
         'amountPerformance': '1810.95435405817'},
        {'amountContract': '0.05068535616',
         'amountPerformance': '1810.91186107787'},
        {'amountContract': '0.45616820548',
         'amountPerformance': '1810.57191723547'},
        {'amountContract': '0.50685356164',
         'amountPerformance': '1810.52942425517'},
        {'amountContract': '5.06853561644',
         'amountPerformance': '1806.70505602822'},
        {'amountContract': '50.68535616438',
         'amountPerformance': '1768.46137375872'},
        {'amountContract': '25.29199272603',
         'amountPerformance': '1789.75035688874'},
        {'amountContract': '25.34267808219',
         'amountPerformance': '1789.70786390844'},
        {'amountContract': '248.35824520548',
         'amountPerformance': '1602.73875059087'},
        {'amountContract': '253.37609546575',
         'amountPerformance': '1598.53194554123'},
        {'amountContract': '253.42678082192',
         'amountPerformance': '1598.48945256093'},
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
        {'amountContract': '451.09966986301',
         'amountPerformance': '1432.76682939308'},
        {'amountContract': '455.66135191781',
         'amountPerformance': '1428.94246116613'},
        {'amountContract': '456.11752012329',
         'amountPerformance': '1428.56002434343'},
        {'amountContract': '456.16820547945',
         'amountPerformance': '1428.51753136313'},
    ]
}


DISCOUNT_RATES = {
    'input': [
        0.0000, 0.0001, 0.0010, 0.0100, 0.1000, 1.0000, 0.1249, 0.1250, 0.1300,
        0.1500, 0.1800, 0.2000, 0.2200, 0.3000, 0.4000, 0.5000, 0.6000, 0.7000,
        0.8000, 0.9000, 0.9900, 0.9909, 0.9990, 0.9999
    ],
    'expected_results': [
        {'amountContract': '354.79749315068',
         'amountPerformance': '4645.20675342466'},
        {'amountContract': '354.79749315068',
         'amountPerformance': '4640.02004460226'},
        {'amountContract': '354.79749315068',
         'amountPerformance': '4593.68225030323'},
        {'amountContract': '354.79749315068',
         'amountPerformance': '4162.36042333301'},
        {'amountContract': '354.79749315068',
         'amountPerformance': '1821.63775269194'},
        {'amountContract': '354.79749315068',
         'amountPerformance': '117.87571646511'},
        {'amountContract': '354.79749315068',
         'amountPerformance': '1514.57663165387'},
        {'amountContract': '354.79749315068',
         'amountPerformance': '1513.50349196203'},
        {'amountContract': '354.79749315068',
         'amountPerformance': '1461.26832468564'},
        {'amountContract': '354.79749315068',
         'amountPerformance': '1277.36248402751'},
        {'amountContract': '354.79749315068',
         'amountPerformance': '1061.29444236423'},
        {'amountContract': '354.79749315068',
         'amountPerformance': '947.18616001753'},
        {'amountContract': '354.79749315068',
         'amountPerformance': '851.26540354660'},
        {'amountContract': '354.79749315068',
         'amountPerformance': '588.29996204648'},
        {'amountContract': '354.79749315068',
         'amountPerformance': '407.85685451746'},
        {'amountContract': '354.79749315068',
         'amountPerformance': '303.61355861378'},
        {'amountContract': '354.79749315068',
         'amountPerformance': '237.36786431275'},
        {'amountContract': '354.79749315068',
         'amountPerformance': '192.32300937991'},
        {'amountContract': '354.79749315068',
         'amountPerformance': '160.12224139859'},
        {'amountContract': '354.79749315068',
         'amountPerformance': '136.19991118181'},
        {'amountContract': '354.79749315068',
         'amountPerformance': '119.50923564960'},
        {'amountContract': '354.79749315068',
         'amountPerformance': '119.36059287924'},
        {'amountContract': '354.79749315068',
         'amountPerformance': '118.03729764291'},
        {'amountContract': '354.79749315068',
         'amountPerformance': '117.89185707063'},
    ]
}

ANNUAL_COSTS_REDUCTION = {
    'input': [
        [0] * 20 + [0.01],
        [0] * 18 + [0.01] * 3,
        [0] * 11 + [0.01] * 10,
        [0] * 3 + [0.01] * 18,
        [0] * 2 + [0.01] * 19,
        [0] + [0.01] * 20,
        [0.01] * 21,
        [0] * 20 + [1],
        [0] * 18 + [1] * 3,
        [0] * 11 + [1] * 10,
        [0] * 3 + [1] * 18,
        [0] * 2 + [1] * 19,
        [0] + [1] * 20,
        [1] * 21,
        [i * 100 for i in (range(1, 22))],
        [2200 - i * 100 for i in (range(1, 22))],
        [123456789] * 21
    ],
    'expected_results': [
        {'amountContract': '0.00000000000',
         'amountPerformance': '0.00059563606'},
        {'amountContract': '0.00000000000',
         'amountPerformance': '0.00276250500'},
        {'amountContract': '0.00000000000',
         'amountPerformance': '0.01598505603'},
        {'amountContract': '0.00000000000',
         'amountPerformance': '0.05285465322'},
        {'amountContract': '0.00460273973',
         'amountPerformance': '0.05693070745'},
        {'amountContract': '0.01160273973',
         'amountPerformance': '0.05947953451'},
        {'amountContract': '0.01860273973',
         'amountPerformance': '0.06234696495'},
        {'amountContract': '0.00000000000',
         'amountPerformance': '0.05956360564'},
        {'amountContract': '0.00000000000',
         'amountPerformance': '0.27625049981'},
        {'amountContract': '0.00000000000',
         'amountPerformance': '1.59850560258'},
        {'amountContract': '0.00000000000',
         'amountPerformance': '5.28546532151'},
        {'amountContract': '0.46027397260',
         'amountPerformance': '5.69307074472'},
        {'amountContract': '1.16027397260',
         'amountPerformance': '5.94795345066'},
        {'amountContract': '1.86027397260',
         'amountPerformance': '6.23469649485'},
        {'amountContract': '348.08219178082',
         'amountPerformance': '5211.30198080864'},
        {'amountContract': '3744.52054794521',
         'amountPerformance': '8505.03030786802'},
        {'amountContract': '229663451.31780821085',
         'amountPerformance': '769715609.64411020279'}
    ]
}


BIDS = {
    'input': [
        {
            'contractDuration': {'years': 0, 'days': 1},
            'NBUdiscountRate': 0.0000,
            'yearlyPaymentsPercentage': 0.7000,
            'annualCostsReduction': [0] * 20 + [0.01]
        },
        {
            'contractDuration': {'years': 0, 'days': 1},
            'NBUdiscountRate': 0.1250,
            'yearlyPaymentsPercentage': 0.8999,
            'annualCostsReduction': [0] * 20 + [10000]
        },
        {
            'contractDuration': {'years': 0, 'days': 1},
            'NBUdiscountRate': 0.1250,
            'yearlyPaymentsPercentage': 0.8999,
            'annualCostsReduction': [0] * 10 + [10000] * 11
        },
        {
            'contractDuration': {'years': 9, 'days': 1},
            'NBUdiscountRate': 0.1250,
            'yearlyPaymentsPercentage': 0.8999,
            'annualCostsReduction': [0] * 10 + [10000] * 11
        },
        {
            'contractDuration': {'years': 9, 'days': 135},
            'NBUdiscountRate': 0.1250,
            'yearlyPaymentsPercentage': 0.8999,
            'annualCostsReduction': [0] * 10 + [10000] * 11
        },
        {
            'contractDuration': {'years': 9, 'days': 136},
            'NBUdiscountRate': 0.1250,
            'yearlyPaymentsPercentage': 0.8999,
            'annualCostsReduction': [0] * 10 + [10000] * 11
        },
        {
            'contractDuration': {'years': 9, 'days': 136},
            'NBUdiscountRate': 0.1250,
            'yearlyPaymentsPercentage': 0.8999,
            'annualCostsReduction': [0] * 11 + [10000] * 10
        },
        {
            'contractDuration': {'years': 10, 'days': 136},
            'NBUdiscountRate': 0.1250,
            'yearlyPaymentsPercentage': 0.8999,
            'annualCostsReduction': [0] * 11 + [10000] * 10
        },
        {
            'contractDuration': {'years': 2, 'days': 10},
            'NBUdiscountRate': 0.1250,
            'yearlyPaymentsPercentage': 0.7000,
            'annualCostsReduction': [92.47] + [250] * 20,
            'announcementDate': datetime(2017, 12, 30)
        },
        {
            'contractDuration': {'years': 2, 'days': 10},
            'NBUdiscountRate': 0.1250,
            'yearlyPaymentsPercentage': 0.7000,
            'annualCostsReduction': [92.47] + [250] * 20,
            'announcementDate': datetime(2017, 12, 31)
        },
        {
            'contractDuration': {'years': 2, 'days': 10},
            'NBUdiscountRate': 0.1250,
            'yearlyPaymentsPercentage': 0.7000,
            'annualCostsReduction': [92.47] + [250] * 20,
            'announcementDate': datetime(2018, 1, 1)
        },
        {
            'contractDuration': {'years': 2, 'days': 10},
            'NBUdiscountRate': 0.1250,
            'yearlyPaymentsPercentage': 0.7000,
            'annualCostsReduction': [0] + [250] * 20,
            'announcementDate': datetime(2018, 12, 31)
        },
    ],
    'expected_results': [
        {'amountContract': '0.00000000000',
         'amountPerformance': '0.00630136986'},
        {'amountContract': '0.00000000000',
         'amountPerformance': '595.63605641337'},
        {'amountContract': '0.00000000000',
         'amountPerformance': '18928.43655328417'},
        {'amountContract': '0.00000000000',
         'amountPerformance': '18928.43655328417'},
        {'amountContract': '0.00000000000',
         'amountPerformance': '18928.43655328417'},
        {'amountContract': '24.65479452055',
         'amountPerformance': '18921.17970907397'},
        {'amountContract': '0.00000000000',
         'amountPerformance': '15985.05602575644'},
        {'amountContract': '24.65479452055',
         'amountPerformance': '15978.60549756960'},
        {'amountContract': '419.04406849315',
         'amountPerformance': '1540.63620088962'},
        {'amountContract': '354.79452054795',
         'amountPerformance': '1513.14383477073'},
        {'amountContract': '245.00297260274',
         'amountPerformance': '1471.31191860622'},
        {'amountContract': '354.79452054795',
         'amountPerformance': '1513.14383477073'},
    ]
}
