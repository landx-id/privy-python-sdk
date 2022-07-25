from privy_python_sdk.privy import Privy

def register_user():
    prv = Privy(privy_enterprise_token="key-123",privy_merchant_key="xxxxxxxxxxxxx",privy_password="bar",privy_username="foo",production=False,privy_id='TE1111')
    
    prv.register_user(
        date_of_birth="1983-01-02",
        email="foo@bar.com",
        ktp="/upload/ktp.jgp",
        selfie="/upload/selfie.jgp",
        name="foo bar",
        nik="1234567891234567",
        phone="08233324223"
    )

def check_user_status():
    prv = Privy(privy_enterprise_token="key-123",privy_merchant_key="xxxxxxxxxxxxx",privy_password="bar",privy_username="foo",production=False,privy_id='TE1111')
    
    prv.register_status(
        token="b3lkdfaoir0294058klkadfk45qeorlkldakfgh"
    )
