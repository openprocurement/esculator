# -*- coding: utf-8 -*-

from datetime import date
from fractions import Fraction


def discount_rate_days(announcement_date, days_per_year,
                       npv_calculation_duration):

    announcement_date = announcement_date.date()
    first_year_days = (date(announcement_date.year, 12, 31) - announcement_date).days
    days = [first_year_days] + [days_per_year] * (npv_calculation_duration - 1)
    days.append(days_per_year - first_year_days)
    return days


def discount_rates(days_for_discount_rates, nbu_discount_rate, days_per_year):
    '''Calculates discount rates'''
    nbu = Fraction(str(nbu_discount_rate))
    return [nbu * Fraction(x, days_per_year) for x in days_for_discount_rates]


def payments_days(contract_duration_years, contract_duration_days,
                  days_for_discount_rate, days_per_year,
                  npv_calculation_duration):

    contract_duration = contract_duration_years * days_per_year + contract_duration_days
    first_period_duration = min(contract_duration, days_for_discount_rate[0])

    full_periods_count, last_period_duration = divmod(
        contract_duration - first_period_duration,
        days_per_year,
    )

    # The empty periods count is equal to npv_calculation_duration + 1 without
    # all non empty period count (full, first and last periods)
    empty_periods_count = npv_calculation_duration + 1 - full_periods_count - 2

    days_with_payments = [first_period_duration]
    days_with_payments += [days_per_year] * full_periods_count
    days_with_payments += [last_period_duration]
    days_with_payments += [0] * empty_periods_count

    return days_with_payments


def period_payment(yearly_payments_percentage, client_cost_reduction,
                   days_with_payments, days_for_discount_rate):
    """ Calculates period payment for a participant/investor """

    yearly_payments_percentage = Fraction(str(yearly_payments_percentage))
    client_cost_reduction = Fraction(str(client_cost_reduction))

    if days_with_payments == 0:
        payments = Fraction(0)
    else:
        payments = Fraction(days_with_payments, days_for_discount_rate)
    return (yearly_payments_percentage * client_cost_reduction * payments)


def calculate_payments(yearly_payments_percentage, cost_reductions,
                       days_with_payments, days_for_discount_rate):
    """ Calculates payments for a participant/investor """

    return [period_payment(yearly_payments_percentage, ccr,
                           days_with_payments[i], days_for_discount_rate[i])
            for i, ccr in enumerate(cost_reductions)]


def calculate_income(cost_reductions, days_for_discount_rate,
                     client_payments):
    # first period income
    # Fix: YYYY-12-31 bug
    if client_payments[0] == 0:
        income = [Fraction(0)]
    else:
        income = [Fraction(str(cost_reductions[0])) - client_payments[0]]
    # XXX first period income should be calculated as other periods ???
    # contract_duration = contract_duration_years * days_per_year + contract_duration_days
    # first_period_duration = min(contract_duration, days_for_discount_rate[0])
    # first_period_duration = days_for_discount_rate[0]
    # income = [Fraction(str(cost_reductions[0])) * Fraction(days_for_discount_rate[0], first_period_duration) - client_payments[0]]

    count = 1
    for i in cost_reductions[1:]:
        income.append(
            Fraction(str(i)) * Fraction(days_for_discount_rate[count], 365) - client_payments[count])
        count += 1
    return income


def discounted_income(discount_rates, income_customer):
    income = []
    coefficient = 1
    for i, r in enumerate(discount_rates):
        coefficient = Fraction(coefficient, (1 + r))  # discount
        income.append(coefficient * income_customer[i])  # discouunted income
    return income


def npv(contract_duration_years, contract_duration_days,
        yearly_payments_percentage, annual_costs_reduction,
        announcement_date, nbu_discount_rate,
        days_per_year=365, npv_calculation_duration=20):
    """ UA Net Present Value """

    days_for_discount_rate = discount_rate_days(announcement_date,
                                                days_per_year,
                                                npv_calculation_duration)
    days_with_payments = payments_days(
        contract_duration_years, contract_duration_days,
        days_for_discount_rate, days_per_year,
        npv_calculation_duration)
    payments = calculate_payments(yearly_payments_percentage,
                                  annual_costs_reduction,
                                  days_with_payments, days_for_discount_rate)
    income = calculate_income(annual_costs_reduction, days_for_discount_rate,
                              payments)
    disc_rates = discount_rates(days_for_discount_rate, nbu_discount_rate,
                                days_per_year)
    discounted_income_by_periods = discounted_income(disc_rates, income)

    return sum(discounted_income_by_periods)


def escp(contract_duration_years, contract_duration_days,
         yearly_payments_percentage, annual_costs_reduction,
         announcement_date, days_per_year=365, npv_calculation_duration=20):
    """ Contract price """

    days_for_discount_rate = discount_rate_days(announcement_date,
                                                days_per_year,
                                                npv_calculation_duration)
    days_with_payments = payments_days(
        contract_duration_years, contract_duration_days,
        days_for_discount_rate, days_per_year,
        npv_calculation_duration)
    payments = calculate_payments(
        yearly_payments_percentage, annual_costs_reduction,
        days_with_payments, days_for_discount_rate)

    return sum(payments)
