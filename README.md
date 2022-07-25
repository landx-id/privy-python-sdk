# privy-python-sdk
Python SDK for Privy Digital Signature https://console.privy.id/


## API Documentation
Please check [Privy Api Reference](https://console.privy.id/documentation).

## Requirements
Python 3.7 or later

## Installation

## usage

### initialization
```python
from privy_python_sdk.privy import Privy

prv = Privy(
    privy_enterprise_token="key-123",
    privy_merchant_key="xxxxxxxxxxxxx",
    privy_username="foo",
    privy_password="bar",
    privy_id='TE1111',
    production=False
)
```
### Privy User Registration
Args:
- email: (String) email of the user 
- phone: (String) phone of the user (ex format: 08233324223)
- selfie: (String) file path of selfie of the user, Face close up photo of Registrant on image format (.png / .jpg / .jpeg)
- ktp: (String) file path of ktp of the user, User's Identity card on image format (.png / .jpg / .jpeg)
- nik: (String) NIK must be 16 digits and the sixteenth digit can't be 0
- name: (String) name of the user
- date_of_birth: (String) date of birth of the user (1983-01-02)

Returns:
    Return reference https://console.privy.id/documentation#registration

```python
prv.register_user(
        date_of_birth="1983-01-02",
        email="foo@bar.com",
        ktp="/upload/ktp.jgp",
        selfie="/upload/selfie.jgp",
        name="foo bar",
        nik="1234567891234567",
        phone="08233324223"
)
```

### get user registration status
Check registration status of user.

Args:
- token: User's token from Registration API

Returns:
    Return reference https://console.privy.id/documentation#check-registration-status

```python
prv.register_status(token="b3lkdfaoir0294058klkadfk45qeorlkldakfgh")
```

### Upload Document
Args:
- title: title of the document
- document_path: path of the document
- recipient: recipient of the document
- owner: owner of the document

Returns:
Return reference https://console.privy.id/documentation#upload-document
```python
prv.upload_document(
        document_path="/upload/document.jgp",
        title="foo bar",
        recipient="LA1234"
    )
```

### Get Document Status
Args:
- doc_Token: (String) token of the document

Returns:
Return reference https://console.privy.id/documentation#check-document-status
```python
prv.document_status(
        doc_token="b3lkdfaoir0294058klkadfk45qeorlkldakfgh"
    )
```