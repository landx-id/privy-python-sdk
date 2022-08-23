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

def reregister(type):
    prv = Privy(privy_enterprise_token="key-123",privy_merchant_key="xxxxxxxxxxxxx",privy_password="bar",privy_username="foo",production=False,privy_id='TE1111')
    
    if type == 'ktp':
        return prv.reregister_ktp(
            ktp="/upload/ktp.jpg",
            user_token="b3lkdfaoir0294058klkadfk45qeorlkldakfgh"
        )
         
    if type == 'selfie':
        return prv.reregister_selfie(
                selfie="/upload/selfie.jpg",
                user_token="b3lkdfaoir0294058klkadfk45qeorlkldakfgh"
        )

    if type == 'file_support':
        return prv.reregister_file_support(
                file_support="/upload/KK.jpg",
                file_support_category="KK",
                user_token="b3lkdfaoir0294058klkadfk45qeorlkldakfgh"
        )



def check_user_status():
    prv = Privy(privy_enterprise_token="key-123",privy_merchant_key="xxxxxxxxxxxxx",privy_password="bar",privy_username="foo",production=False,privy_id='TE1111')
    
    prv.register_status(
        token="b3lkdfaoir0294058klkadfk45qeorlkldakfgh"
    )
