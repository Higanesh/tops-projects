
def switch_case(value):
            switch_dict = {
                1: "Withdraw amt",
                2: "Deposite amt",
                3: "View balance"
            }
            return switch_dict.get(value, "please enter value in range")

