from privy_python_sdk.privy import Privy

def upload_doc():
    prv = Privy(privy_enterprise_token="key-123",privy_merchant_key="xxxxxxxxxxxxx",production=False,privy_id='TE1111')
    
    prv.upload_document(
        document_path="/upload/document.jgp",
        title="foo bar",
        recipient="LA1234"
    )


def doc_status():
    prv = Privy(privy_enterprise_token="key-123",privy_merchant_key="xxxxxxxxxxxxx",production=False,privy_id='TE1111')
    
    prv.document_status(
        doc_token="b3lkdfaoir0294058klkadfk45qeorlkldakfgh"
    )
