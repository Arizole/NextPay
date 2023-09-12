from NextPay import NextPay

def get_paypay_token(phone_number, password):
    next_pay = NextPay()
    try:
        next_pay.login_start(phone_number, password)
    except:
        return None
    otp = input("Enter OTP > ")
    try:
        login_result = next_pay.login_otp(otp)
    except:
        return None
    return login_result["payload"]["accessToken"]

if __name__ == "__main__":
    token = get_paypay_token("PAYPAY USERNAME(PHONE NUMBER)", "PAYPAY PASSWORD")
    print(token)