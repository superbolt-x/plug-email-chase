"""
plug_email_chase extract
------------------------
The Extract Submodule

Date: 2021-05-14

Author: Lorenzo Coacci
"""


# + + + Libraries + + +

# + + + Libraries + + +


# + + + Settings + + +
# + + + Settings + + +


# + + + Functions + + +
# + + + Functions + + +


# + + + Classes + + +
def extract():
    """Docstring"""
    pass


class Example:
    """
    Example : the Example Object

    A Example class to manage a Google Mail


    Parameters
    ----------
    example_creds_path (optional): string
        The G Mail Path to the client secret JSON
    example_config_path (optional): string
        The G Mail Path to the token.pickle
    example_client (optional): exampleClient
        The exampleClient Object if already exists
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

    >>> example = example(example_config_path='./token.pickle')

    >>>
    """

    def __init__(
        self,
        example_creds_path=None,
        example_config_path=None,
        example_client=None,
        debug=False,
        base_email="me",
        base_url="https://mail.google.com/mail/u/4",
        scopes=None,
        api_version="v1",
    ):
        """Init example"""
        self.debug = bool(debug)
        self.base_email = str(base_email)
        self.base_url = str(base_url)
        self.api_version = str(api_version)

        # load client
        if example_client is not None:
            self.client = example_client

        self.example = self.client


# + + + Classes + + +
