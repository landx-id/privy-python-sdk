"""unleash Get Feature Flag."""

from requests import post
from requests.auth import HTTPBasicAuth
from json import dumps

def upload_document(title, document_path, recipient, owner, privy_base_url, privyid_username, privyid_password, privyid_merchant_key, privy_id_enterprise_token ):
    """Upload document to privy.

    Args:
        title: title of the document
        document_path: path of the document
        recipient: recipient of the document
        owner: owner of the document
        privy_base_url: owner of the document
        privyid_username: owner of the document
        privyid_password: owner of the document
        privyid_merchant_key: owner of the document
        privy_id_enterprise_token: owner of the document

    Returns:
        Return reference https://console.privy.id/documentation#upload-document
    """
    response = post(
        f'{privy_base_url}/document/upload',
        auth=HTTPBasicAuth(username=privyid_username,password=privyid_password),
        headers={'Merchant-Key': privyid_merchant_key},
        data={
            'documentTitle': title,
            'docType': 'Parallel',
            'recipients' : dumps([{
                'privyId': recipient,
                'type': 'Signer'
            }]),
            'owner': dumps({
                'privyId': owner,
                'enterpriseToken': privy_id_enterprise_token
            })
        },
        files={'document': open(document_path, 'rb')}
    )

    response_json = response.json()
    return response_json



def register_user(email, phone, selfie, ktp, nik, name, date_of_birth, privy_base_url, privyid_username, privyid_password, privyid_merchant_key):
    """Register user to privy.

    Args:
        email: (String) email of the user 
        phone: (String) phone of the user (ex format: 08233324223)
        selfie: (File) selfie of the user, Face close up photo of Registrant on image format (.png / .jpg / .jpeg)
        ktp: (File) ktp of the user, User's Identity card on image format (.png / .jpg / .jpeg)
        nik: (String) NIK must be 16 digits and the sixteenth digit can't be 0
        name: (String) name of the user
        date_of_birth: date of birth of the user
        privy_base_url: owner of the document
        privyid_username: owner of the document
        privyid_password: owner of the document
        privyid_merchant_key: owner of the document

    Returns:
        Return reference https://console.privy.id/documentation#registration

    """
    response = post(
        f'{privy_base_url}/registration',
        auth=HTTPBasicAuth(username=privyid_username,password=privyid_password),
        headers={'Merchant-Key': privyid_merchant_key},
        data={
            'email': email,
            'phone': phone,
            'identity': dumps({
                'nik': nik,
                'nama': name,
                'tanggalLahir':date_of_birth
            })
        },
        files={
            'selfie': open(selfie, 'rb'),
	        'ktp': open(ktp,'rb')
              }
    )
    response_json = response.json()
    return response_json

def register_status(user_token, privy_base_url, privyid_username, privyid_password, privyid_merchant_key):
    """Check registration status of user.

    Args:
        user_token: token of the user
        privy_base_url: owner of the document
        privyid_username: owner of the document
        privyid_password: owner of the document
        privyid_merchant_key: owner of the document

    Returns:
        Return reference https://console.privy.id/documentation#check-registration-status

    """
    response = post(
        f'{privy_base_url}/registration/status',
        auth=HTTPBasicAuth(username=privyid_username,password=privyid_password),
        headers={'Merchant-Key': privyid_merchant_key},
        data={
            'token': user_token,
        }
    )
    response_json = response.json()
    return response_json

def document_status(doc_token, privy_base_url, privyid_username, privyid_password, privyid_merchant_key):
    """Check registration status of user.

    Args:
        doc_Token: (String) token of the document
        privy_base_url: owner of the document
        privyid_username: owner of the document
        privyid_password: owner of the document
        privyid_merchant_key: owner of the document

    Returns:
        Return reference https://console.privy.id/documentation#check-registration-status

    """
    response = post(
        f'{privy_base_url}/document/status/:docToken',
        auth=HTTPBasicAuth(username=privyid_username,password=privyid_password),
        headers={'Merchant-Key': privyid_merchant_key},
        data={
            'token': doc_token,
        }
    )
    response_json = response.json()
    return response_json




