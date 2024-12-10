import addcust
import viewcust
import searchcust
import viewallcust
import totalamtinbank

def switch_case(value):
            switch_dict = {
                1: addcust.addcustomer(),
                # 2: viewcust.viewcustomer(0),
                # 3: searchcust.searchcustomer(0),
                # 4: viewallcust.viewallcustomer(0),
                # 5: totalamtinbank.totalamtinbank(0)
            }
            return switch_dict.get(value, "please enter value in range")

