"""unleash Get Feature Flag."""

from requests import post
from requests.auth import HTTPBasicAuth
from json import dumps


class Privy:
    def __init__(self, privy_id=(str), privy_username=(str), privy_password=(str),privy_merchant_key=(str),privy_enterprise_token=(str),production=(bool)):
        if privy_username is None:
            raise ValueError("privyid_username must be provided")
        if privy_password is None:
            raise ValueError("privyid_password must be provided")
        if privy_merchant_key is None:
            raise ValueError("privyid_merchant_key must be provided")
        if privy_enterprise_token is None:
            raise ValueError("privy_id_enterprise_token must be provided")
        if production is None:
            raise ValueError("production status must be provided")

        self.privy_base_url = 'https://core.privy.id/v3/merchant' if production else 'https://stg-core.privy.id/v3/merchant'
        self.privy_id = privy_id
        self.privy_username = privy_username
        self.privy_password = privy_password
        self.privy_merchant_key = privy_merchant_key
        self.privy_enterprise_token = privy_enterprise_token


    def register_user(self ,email=(str), phone=(str), selfie=(str), ktp=(str), nik=(str), name=(str), date_of_birth=(str)):
        """Register user to privy.

        Args:
            email: (String) email of the user 
            phone: (String) phone of the user (ex format: 08233324223)
            selfie: (String) file path of selfie of the user, Face close up photo of Registrant on image format (.png / .jpg / .jpeg)
            ktp: (String) file path of ktp of the user, User's Identity card on image format (.png / .jpg / .jpeg)
            nik: (String) NIK must be 16 digits and the sixteenth digit can't be 0
            name: (String) name of the user
            date_of_birth: (String) date of birth of the user (1983-01-02)

        Returns:
            Return reference https://console.privy.id/documentation#registration

        """
        response = post(
            f'{self.privy_base_url}/registration',
            auth=HTTPBasicAuth(username=self.privy_username,password=self.privy_password),
            headers={'Merchant-Key': self.privy_merchant_key},
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

    def register_status(self,token=(str)):
        """Check registration status of user.

        Args:
            token: User's token from Registration API

        Returns:
            Return reference https://console.privy.id/documentation#check-registration-status

        """
        response = post(
            f'{self.privy_base_url}/registration/status',
            auth=HTTPBasicAuth(username=self.privy_username,password=self.privy_password),
            headers={'Merchant-Key': self.privy_merchant_key},
            data={
                'token': token,
            }
        )
        response_json = response.json()
        return response_json

    def upload_document(self ,title=(str), document_path=(str), recipient=(str)):
        """Upload document to privy.

        Args:
            title: title of the document
            document_path: path of the document
            recipient: recipient of the document
            owner: owner of the document

        Returns:
            Return reference https://console.privy.id/documentation#upload-document
        """
        response = post(
            f'{self.privy_base_url}/document/upload',
            auth=HTTPBasicAuth(username=self.privy_username,password=self.privy_password),
            headers={'Merchant-Key': self.privy_merchant_key},
            data={
                'documentTitle': title,
                'docType': 'Parallel',
                'recipients' : dumps([{
                    'privyId': recipient,
                    'type': 'Signer'
                }]),
                'owner': dumps({
                    'privyId': self.privy_id,
                    'enterpriseToken': self.privy_enterprise_token
                })
            },
            files={'document': open(document_path, 'rb')}
        )

        response_json = response.json()
        return response_json

    def document_status(self, doc_token=(str)):
        """Check registration status of user.

        Args:
            doc_Token: (String) token of the document

        Returns:
            Return reference https://console.privy.id/documentation#check-document-status

        """
        response = post(
            f'{self.privy_base_url}/document/status/:docToken',
            auth=HTTPBasicAuth(username=self.privy_username,password=self.privy_password),
            headers={'Merchant-Key': self.privy_merchant_key},
            data={
                'token': doc_token,
            }
        )
        response_json = response.json()
        return response_json

    
    def reregister_ktp(self, ktp=(str), user_token=(str)):
        """re-registration ktp if user is invalid or rejected.

        Args:
            ktp: (String) ktp file directory

        Returns:
            code : HTTP Status Code
            data : 
            errors : Message of error
            message : Message of response

        """
        response = post(
            f'{self.privy_base_url}/reregister/:ktp',
            auth=HTTPBasicAuth(username=self.privy_username,password=self.privy_password),
            headers={'Merchant-Key': self.privy_merchant_key,'Token': user_token,'Content-Type':'form-data'},
            files={
                'ktp': open(ktp,'rb')
            }
        )
        response_json = response.json()
        return response_json
    
    def reregister_selfie(self, selfie=(str), user_token=(str)):
        """re-registration selfie if user is invalid or rejected.

        Args:
            selfie: (String) selfie file directory

        Returns:
            code : HTTP Status Code
            data : 
            errors : Message of error
            message : Message of response

        """
        response = post(
            f'{self.privy_base_url}/reregister/:selfie',
            auth=HTTPBasicAuth(username=self.privy_username,password=self.privy_password),
            headers={'Merchant-Key': self.privy_merchant_key,'Token': user_token,'Content-Type':'form-data'},
            files={
                'ktp': open(selfie,'rb')
            }
        )
        response_json = response.json()
        return response_json

    def reregister_file_support(self, file_support=(str),file_support_category=(str), user_token=(str)):
        """re-registration file support if user is invalid or rejected.

        Args:
            file_support: (String) file support dir
            file_support_category: (String) category of requested file support
            user_token: (String) user token

        Returns:
            code : HTTP Status Code
            data : 
            errors : Message of error
            message : Message of response

        """
        response = post(
            f'{self.privy_base_url}/reregister/:file-support',
            auth=HTTPBasicAuth(username=self.privy_username,password=self.privy_password),
            headers={'Merchant-Key': self.privy_merchant_key,'Token': user_token,'Content-Type':'form-data'},
            data={
                'fileSupport[][category]': file_support_category
            },
            files={
                'fileSupport[][attachment]': open(file_support,'rb')
            }
        )
        response_json = response.json()
        return response_json