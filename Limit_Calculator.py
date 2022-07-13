def separate_terms(func):
    terms = []
    x = func.rsplit("+")
    for i in range(len(x)):
        terms += x[i].rsplit("-")
    return terms

def check_degree(term):
    if term.isdigit() == True:
        return 0
    elif term.endswith('x'):
        return 1
    else:
        x = term.rsplit("**")
        return int(x[1])

def biggest_degree(term_list):
    max_degree = 0
    for term in range(len(term_list)):
        if check_degree(term_list[term]) > max_degree:
            max_degree = check_degree(term_list[term])
    return max_degree

def biggest_degree_term(term_list):
    max_degree = 0
    max_pos = 0
    for term in range(len(term_list)):
        if check_degree(term_list[term]) > max_degree:
            max_degree = check_degree(term_list[term])
            max_pos = term
    return term_list[max_pos]


def leading_coeff(big_deg_term):
    y = big_deg_term.rsplit("*")
    return y[0]


def lim_inf(function):
    split = function.rsplit("/")
    num_func = split[0]
    denom_func = split[1]

    num_sep_func = separate_terms(num_func)
    denom_sep_func = separate_terms(denom_func)

    real_num_sep_func = []
    real_denom_sep_func = []
    for i in range(len(num_sep_func)):
        if i == 0:
            real_num_sep_func.append(num_sep_func[0].lstrip("("))
        elif i == len(num_sep_func)-1:
            real_num_sep_func.append(num_sep_func[i].rstrip(")"))
        else:
            real_num_sep_func.append(num_sep_func[i])

    for i in range(len(denom_sep_func)):
        if i == 0:
            real_denom_sep_func.append(denom_sep_func[0].lstrip("("))
        elif i == len(denom_sep_func)-1:
            real_denom_sep_func.append(denom_sep_func[i].rstrip(")"))
        else:
            real_denom_sep_func.append(denom_sep_func[i])


    num_biggest_degree = biggest_degree(real_num_sep_func)
    denom_biggest_degree = biggest_degree(real_denom_sep_func)

    if denom_biggest_degree > num_biggest_degree:
        print("Limit is equal to 0")
    elif denom_biggest_degree < num_biggest_degree:
        print("DNE!")
    else:
        b = biggest_degree_term(real_denom_sep_func)
        a = biggest_degree_term(real_num_sep_func)
        lead_co_num = int(leading_coeff(a))
        lead_co_denom = int(leading_coeff(b))
        print(lead_co_num/lead_co_denom)


def f(x):
    f = eval(func)
    return f

func = input("Enter f(x): ")
limit_infinity = input("Does the limit go to infinity ('yes' or 'no')? ")
if limit_infinity == "yes":
    lim_inf(func)
else:
    limit_value = int(input("Enter a limit value: "))
    print(f(limit_value))










