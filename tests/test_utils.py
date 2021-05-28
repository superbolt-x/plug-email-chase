import pytest
import os
from plug_email_chase.utils import get_emails


def test_get_emails():
    """Check if emails are parsed"""
    emails = get_emails(
        host=os.environ.get("EMAIL_HOST"),
        port=os.environ.get("EMAIL_PORT"),
        my_email=os.environ.get("EMAIL"),
        my_password=os.environ.get("EMAIL_PASSWORD"),
        email_section=None,
        only_from=None,
        before_date=None,
        after_date=None,
        tz=None,
    )
    print(emails)
    # captured = capsys.readouterr()
    # assert "Test" in captured.out


if __name__ == "__main__":
    test_get_emails()
