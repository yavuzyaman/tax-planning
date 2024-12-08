from constants import constants

def calculate_401k(contribution_percentage,w2_income):

    cont_401k = w2_income * (contribution_percentage / 100)
    return cont_401k


def calculate_net_income(w2_income, cont_401k, hsa_cont_amount, dcfsa_cont_amount, hcfsa_cont_amount,
                         stock_short_gain, stock_short_loss, dividend_gain,other_income):
    net_income = (w2_income - cont_401k - hsa_cont_amount - dcfsa_cont_amount
                  - hcfsa_cont_amount + stock_short_gain - stock_short_loss + dividend_gain + other_income)
    return net_income


def calculate_tax_liability(agi):
    tax_brackets, tax_bracket_limits = constants()
    tax_liability = 0
    i = 0
    while agi > tax_bracket_limits[i]:
        if i > 0:
            tax = (tax_bracket_limits[i] - tax_bracket_limits[i - 1]) * tax_brackets[i]
        else:
            tax = tax_bracket_limits[i] * tax_brackets[i]
        tax_liability = tax_liability + tax
        i = i + 1
    remaining = agi - tax_bracket_limits[i - 1]
    tax_liability = tax_liability + remaining * tax_brackets[i]
    return tax_liability


def calculate_net_tax_liability(tax_liability, child_credit_amount, other_credit_amount):
    net_tax_liability = tax_liability - child_credit_amount - other_credit_amount
    return net_tax_liability


