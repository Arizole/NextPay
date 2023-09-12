from NextPay import NextPay

next_pay: NextPay = None

def token_login(access_token):
    global next_pay
    next_pay = NextPay(access_token)

def get_balance():
    if next_pay == None:
        print("Please login first!")
        return
    print(str(next_pay.get_balance()["payload"]["walletSummary"]["allTotalBalanceInfo"]["balance"]))

if __name__ == "__main__":
    token_login("PAYPAY TOKEN")
    get_balance()
