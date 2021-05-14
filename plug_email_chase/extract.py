"""
plug_email_chase extract
------------------------
The Extract Submodule

Date: 2021-05-14

Author: Lorenzo Coacci
"""
# + + + Libraries + + +
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
from bs4 import BeautifulSoup
# + + + Libraries + + +


# + + + Settings + + +
# + + + Settings + + +


# + + + Functions + + +
# + + + Functions + + +


# + + + Classes + + +
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

# - - GMail - -
# + + + Classes + + +
