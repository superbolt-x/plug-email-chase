"""
plug_email_chase extract
------------------------
This script defines the GMail
Class

Date: 2021-04-09

Author: Lorenzo Coacci
"""
# + + + + + Libraries + + + + +
# to manage basic
from golog import (
    se,
    sev,
    is_url,
    print_magenta,
    correct_nonlist,
    filepath_exists,
    error_print,
    warning_print,
    dict_print
)
# to manage gmail
import pickle
import os.path
import base64
import re
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
# + + + + + Libraries + + + + +


# + + + + + Settings + + + + +
# + + + + + Settings + + + + +


# + + + + + Functions + + + + +
# + + + + + Functions + + + + +


# + + + + + Classes + + + + +
# - - GMailClient - -
class GMailClient():
    def __init__(
        self,
        gmail_creds_path=None,
        gmail_config_path=None,
        debug=False,
        base_email="me",
        base_url="https://mail.google.com/mail/u/4",
        scopes=None,
        api_version='v1'
    ):
        """Init the GMail Client"""
        self.base_email = str(base_email)
        self.base_url = str(base_url)
        self.debug = bool(debug)

        # set creds vars
        self.gmail_creds_path = None if gmail_creds_path is None else str(gmail_creds_path)
        self.gmail_config_path = None if gmail_config_path is None else str(gmail_config_path)

        # set scope
        if scopes is None:
            self.scopes = [
                'https://www.googleapis.com/auth/gmail.readonly',
                'https://mail.google.com/',
                'https://www.googleapis.com/auth/gmail.modify',
                #'https://www.googleapis.com/auth/gmail.metadata',
                #'https://www.googleapis.com/auth/gmail.addons.current.message.metadata',
                'https://www.googleapis.com/auth/gmail.addons.current.message.readonly',
                'https://www.googleapis.com/auth/gmail.addons.current.message.action',
                'https://www.googleapis.com/auth/gmail.labels',
                'https://www.googleapis.com/auth/gmail.compose'
            ]
        else:
            self.scopes = correct_nonlist(scopes)

        # load config vars
        if self.gmail_config_path is None:
            # Try the Env Var
            config_path_env = os.environ.get('GMAIL_API_CONFIG_PATH')
            if self.debug:
                print_magenta(f"This is the config path : {config_path_env}")
            if config_path_env is None or not os.path.exists(config_path_env):
                if self.debug:
                    warning_print(f"Config path {config_path_env} is None (or path does not exist) - the default env variable with key 'GMAIL_API_CONFIG_PATH' might be not set")
                    warning_print("Trying with the Creds Path")
                if self.gmail_creds_path is None:
                    creds_path_env = os.environ.get('GMAIL_API_CREDS_PATH')
                    if self.debug:
                        print_magenta(f"This is the creds path : {creds_path_env}")
                    if creds_path_env is None or not os.path.exists(creds_path_env):
                        if self.debug:
                            warning_print(f"Credential path {creds_path_env} is None (or path does not exist) - the default env variable with key 'GMAIL_API_CREDS_PATH' might be not set")
                        error_print("Both Credential Path gmail_creds_path and Config Path gmail_config_path are None, and also could not load the envs.\nPlease set at least the config or creds paths as a secret env var with key = 'GMAIL_API_CONFIG_PATH' and/or GMAIL_API_CREDS_PATH")
                        return None
                    else:
                        self.gmail_creds_path = creds_path_env
            else:
                self.gmail_config_path = config_path_env


        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        # connect
        try:
            config = None
            if self.debug:
               print_magenta(self.gmail_config_path)
            if self.gmail_config_path is not None and os.path.exists(self.gmail_config_path):
                with open(self.gmail_config_path, 'rb') as token:
                    config = pickle.load(token)
            # If there are no (valid) credentials available, let the user log in.
            if not config or not config.valid:
                if config and config.expired and config.refresh_token:
                    config.refresh(Request())
                    # replace token file
                    with open(self.gmail_config_path, 'wb') as token:
                        pickle.dump(config, token)
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        self.gmail_creds_path,
                        self.scopes
                    )
                    config = flow.run_local_server(port=0)
                    # Save the credentials for the next run
                    self.gmail_config_path =  '/'.join(self.gmail_creds_path.split('/')[:-1]) + '/token.pickle'
                    with open(self.gmail_config_path, 'wb') as token:
                        pickle.dump(config, token)
        except Exception as exc:
            error_print(
                f"Cannot connect to the GMail API using",
                exception=exc
            )
            return None

        # load client
        self.client = build('gmail', str(api_version), credentials=config)
# - - GMailClient - -


# - - GMail - -
class GMail():
    """
    GMail : the GMail Object

    A GMail class to manage a Google Mail


    Parameters
    ----------
    gmail_creds_path (optional): string
        The G Mail Path to the client secret JSON
    gmail_config_path (optional): string
        The G Mail Path to the token.pickle
    gmail_client (optional): GMailClient
        The GMailClient Object if already exists
    debug (optional): bool
        Show debug info?
    base_email (optional): string
        The base email
    base_url (optional): string
        The base url
    scopes (optional): list of strings
        The list with API scopes
    api_version (optional): string
        The API version


    See Also
    --------
    TODO: see also

    Examples
    --------

    >>> gmail = GMail(gmail_config_path='./token.pickle')

    >>> 
    """
    def __init__(
        self, 
        gmail_creds_path=None,
        gmail_config_path=None,
        gmail_client=None,
        debug=False,
        base_email="me",
        base_url="https://mail.google.com/mail/u/4",
        scopes=None,
        api_version='v1'
    ):
        """Init GMail"""
        self.debug = bool(debug)
        self.base_email = str(base_email)
        self.base_url = str(base_url)
        self.api_version = str(api_version)

        # load client
        if gmail_client is not None:
            self.client = gmail_client
        else:
            self.client = GMailClient(
                gmail_creds_path=gmail_creds_path,
                gmail_config_path=gmail_config_path,
                debug=self.debug,
                base_email=self.base_email,
                base_url=self.base_url,
                scopes=scopes,
                api_version=self.api_version
            ).client
            if self.client is None:
                error_print(
                    f"Cannot connect to the GMail API - Client is None"
                )
                return None

        self.gmail = self.client


    def _get_id_from_link(self, link):
        # validate and sanitize link
        if is_url(link):
            # get id
            # TODO -> GMAIL MESSGAE LINK DOES NOT WORK - NOT SAME ID
            id = str(link).replace(self.base_url, '').split('/')[2]
        else:
            # user input is not a link - try to use as an id
            id = str(link)
        return id

    @sev
    def get_labels(self):
        # Call the Gmail API
        results = self.gmail.users().labels().list(
            userId=self.base_email
        ).execute()
        labels = results.get('labels', [])

        if not labels:
            warning_print('No labels found.')
            return None
        else:
            return labels

    @sev
    def get_messages(
        self,
        which_email=None,
        from_who=None,
        only_unread=False,
        start_date=None
    ):
        # Call the Gmail API
        if which_email is None:
            which_email = self.base_email
        q = ""
        if from_who is not None:
            q += f"from:{str(from_who)} "
        if only_unread:
            q += "is:unread "
        if start_date is not None:
            q += f"after:{str(start_date).replace('-', '/')} "
        
        if q != "":
            results = self.gmail.users().messages().list(
                userId=str(which_email),
                q=q
            ).execute()
        else:
            results = self.gmail.users().messages().list(
                userId=str(which_email)
            ).execute()

        messages = results.get('messages', [])

        if not messages:
            warning_print('No messages found.')
            return None
        else:
            return messages

    @sev
    def get_message(
        self,
        id,
        which_email=None,
        clean=True
    ):
        # Call the Gmail API
        if which_email is None:
            which_email = self.base_email
        # extract id if id is a link
        id = self._get_id_from_link(id)
        msg = self.gmail.users().messages().get(
            userId=str(which_email),
            id=id
        ).execute()

        # get headers
        headers = { 
            f"{str(header.get('name')).lower().strip()}": str(header.get('value'))
            for header in msg.get('payload').get('headers')
            if str(header.get('name')).lower().strip() in ['to', 'from', 'subject']
        }

        # assemble message
        data_body = msg.get('payload').get('body').get('data')
        data_multipart = msg.get('payload').get('parts')

        message = ""
        if data_body is not None:
            body = base64.urlsafe_b64decode(data_body)
            message += str(body)
        if data_multipart is not None:
            for part in data_multipart:
                multi_part = base64.urlsafe_b64decode(part.get('body').get('data'))
                message += str(multi_part)

        if clean:
            # remove links
            message = re.sub(r'(?P<url>https?:[^\s]+)', '', message, flags=re.MULTILINE)
            # remove HTML
            message = BeautifulSoup(message, "lxml").text
            # remove extra chars
            message = re.sub(r'[\r\n\xc2\xb7]', '', message, flags=re.MULTILINE)
            # clean object
            for element in [
                r'\n', r'\r', r'\xe2', r'\x9c', r'\xb7',
                r'\x90', r'\xc2', r'\x94', r'\x8c', r'\xa057',
                r'\x80', r'\x9c', r'\\', r'\xa0', r'\xf0',
                r'\x9f', r'\x93', r'\x9d'
            ]:
                message = message.replace(element, ' ')

            message = ' '.join([*map(lambda x: x.strip(), message.split(' '))])

        result = {
            'message': message,
            **headers
        }

        return result
# - - GMail - -
# + + + + + Classes + + + + +
