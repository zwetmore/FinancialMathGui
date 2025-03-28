import math

class InterestRate():
    def __init__(self, i = 0, delta = 0, d = 0, v = 0):
        self.i = i
        self.delta = delta
        self.d = d
        self.v = v
        self.adjust_all_rates()
        

    def convert_i_to_all(self):
        self.v = (1 + self.i) ** -1
        self.delta = math.log(1 + self.i)
        self.d = self.i / (1 + self.i)

    def convert_delta_to_i(self):
        self.i = math.exp(self.delta) - 1

    def convert_d_to_i(self):
        self.i = ((1 - self.d) ** -1) - 1
        
    def convert_v_to_i(self):
        self.i = (self.v ** -1) - 1

    def adjust_all_rates(self):
        if(self.delta != 0):
            self.convert_delta_to_i()
        elif(self.d != 0):
            self.convert_d_to_i()
        elif(self.v != 0):
            self.convert_v_to_i()
        
        self.convert_i_to_all()
        

class CashFlows():
    def __init__(self):
        self.time_amount_dict = {}
        self.time_period = "yearly"
        self.interest_rate = InterestRate()
        self.npv = 0

    def calculate_npv(self):
        v = (self.interest_rate.v)
        npv = 0

        for key in self.time_amount_dict.keys():
            npv += ((v ** key) * self.time_amount_dict[key])

        return npv

    def add_cashflow(self, time, amount, rate = 0, rate_type = "i"):
        if rate_type not in ["i", "v", "d", "delta"]:
            rate_type = "i"

        if time in self.time_amount_dict:
            self.time_amount_dict[time] += amount
        else :
            self.time_amount_dict[time] = amount
            self.time_amount_dict = dict(sorted(self.time_amount_dict.items()))
        
        if(rate_type == "i"):
            self.interest_rate = InterestRate(i = rate)
        elif(rate_type == "v"):
            self.interest_rate = InterestRate(v = rate)
        elif(rate_type == "d"):
            self.interest_rate = InterestRate(d = rate)
        else:
            self.interest_rate = InterestRate(delta = rate)

        self.npv = self.calculate_npv()
    
    def __repr__(self):
        ret_str = ""
        whitespace = "            "
        dashes = 50*"-"
        ret_str += dashes + "\n"
        #display interest rate and time periods
        ret_str += f'Interest Rate as i = {self.interest_rate.i} {whitespace}Period = {self.time_period}\n'

        #display cash flows
        for key in self.time_amount_dict.keys():
            ret_str += f'Time: {key}    Amount: {self.time_amount_dict[key]}\n'

        ret_str += dashes + "\n"

        #display NPV
        ret_str += f'NPV: {self.npv:.3f}'

        return ret_str

    