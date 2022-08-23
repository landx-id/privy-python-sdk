# Privy Python SDK
Python SDK for Privy Digital Signature https://console.privy.id/


## API Documentation
Please check [Privy Api Reference](https://console.privy.id/documentation).

## Requirements
Python 3.7 or later

## Installation
```python
pip install privy-python-sdk
```
## Usage

### Initialization

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
**Args**:
- `email` *string* - User's email
- `phone` *string* - User's phone (e.g: 08233324223)
- `selfie` *string* - Close up photo of registrant (.png, .jpg, or .jpeg)
- `ktp` *string* - KTP Photo of the user (.png, .jpg, or .jpeg)
- `nik` *string* - NIK must be 16 digits and the sixteenth digit can't be 0
- `name` *string* - name of the user
- `date_of_birth` *string* - date of birth of the user (1983-01-02)

**Returns**: <br />
    Return reference https://console.privy.id/documentation#registration

```python
prv.register_user(
        date_of_birth="1983-01-02",
        email="foo@bar.com",
        ktp="/upload/ktp.jpg",
        selfie="/upload/selfie.jpg",
        name="foo bar",
        nik="1234567891234567",
        phone="08233324223"
)
```

### Get User's Registration Status
Check registration status of user.

**Args**:
- `token` *string* - User's token from Registration API

**Returns**: <br />
    Return reference https://console.privy.id/documentation#check-registration-status

```python
prv.register_status(token="b3lkdfaoir0294058klkadfk45qeorlkldakfgh")
```

### Upload Document
**Args**:
- `title` *string* - title of the document
- `document_path` *string* - path of the document
- `recipient` *string* - recipient of the document
- `owner` *string* - owner of the document

**Returns**: <br />
Return reference https://console.privy.id/documentation#upload-document

```python
prv.upload_document(
        document_path="/upload/document.jpg",
        title="foo bar",
        recipient="LA1234"
    )
```

### Get Document Status
**Args**:
- `doc_Token` *string* - Document's token

**Returns**: <br />
Return reference https://console.privy.id/documentation#check-document-status
```python
prv.document_status(
        doc_token="b3lkdfaoir0294058klkadfk45qeorlkldakfgh"
    )
```

### update data
for invalid or rejected user who wants to update their data and reregister

1. update data ktp
    ```python
    prv.reregister_ktp(
            ktp="/upload/ktp.jpg",
            user_token="b3lkdfaoir0294058klkadfk45qeorlkldakfgh"
        )
    ```

2. update data selfie
    ```python
    prv.reregister_selfie(
            selfie="/upload/selfie.jpg",
            user_token="b3lkdfaoir0294058klkadfk45qeorlkldakfgh"
        )
    ```

3. update data file support
    ```python
    prv.reregister_file_support(
            file_support="/upload/KK.jpg",
            file_support_category="KK",
            user_token="b3lkdfaoir0294058klkadfk45qeorlkldakfgh"
        )
    ```
## License

**privy-python-sdk** is released under the MIT License. Check License file for detail.