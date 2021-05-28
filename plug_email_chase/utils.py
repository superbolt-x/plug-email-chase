"""
plug_email_chase utils
----------------------
The utils module

Date: 2021-05-14

Author: Lorenzo Coacci
"""
# + + + Libraries + + +
import os
import imaplib
import email
import base64

# to parse emails with regex
import re
from datetime import datetime, timedelta
from pytz import timezone
import pytz
from alive_progress import alive_bar

# to clean the HTML email
from bs4 import BeautifulSoup

# + + + Libraries + + +


# + + + Settings + + +
# + + + Settings + + +


# + + + Functions + + +
def last_day_of_month(any_day: datetime) -> datetime:
    """RETURN : the last date/day of the month given any date"""

    # get close to the end of the month for any day, and add 4 days 'over'
    next_month = any_day.replace(day=28) + timedelta(days=4)

    # subtract the number of remaining 'overage' days to get last day of current month,
    # or said programattically, the previous day of the first of next month
    return next_month - timedelta(days=next_month.day)


def get_emails(
    host: str,
    port: int,
    my_email: str,
    my_password: str,
    email_section=None,
    only_from=None,
    before_date=None,
    after_date=None,
    tz=None,
) -> list:
    # create mail connection
    mail = imaplib.IMAP4_SSL(host, int(port))
    mail.login(my_email, my_password)
    print(mail)

    # filter box
    if email_section is None:
        email_section = "INBOX"
    mail.select(email_section)

    # add email filter
    filters = [only_from, before_date, after_date]

    if False not in [*filter(lambda x: x is None, filters)]:
        search_criterion = "ALL"
    else:
        criterion_list = []
        if only_from is not None:
            criterion_list.append(f'FROM "{only_from}"')
        if before_date is not None:
            # check date format
            if not isinstance(before_date, datetime):
                before_date = str(before_date)
                # check validity to date
                try:
                    before_date = datetime.strptime(before_date, "%Y-%m-%d")
                except Exception as exc:
                    raise ValueError(
                        f"Cannot parse date 'before_date' {before_date} to date -> {str(exc)}"
                    )

            before_date_str = before_date.strftime("%d-%b-%Y")
            criterion_list.append(f'BEFORE "{before_date_str}"')
        if after_date is not None:
            # check date format
            if not isinstance(after_date, datetime):
                after_date = str(after_date)
                # check validity to date
                try:
                    after_date = datetime.strptime(after_date, "%Y-%m-%d")
                except Exception as exc:
                    raise ValueError(
                        f"Cannot parse date 'after_date' {after_date} to date -> {str(exc)}"
                    )

            after_date_str = after_date.strftime("%d-%b-%Y")
            criterion_list.append(f'SINCE "{after_date_str}"')

        # generate search criterion
        search_criterion = "(" + " ".join(criterion_list) + ")"

    # Email Search
    _, data = mail.search(None, search_criterion)
    mail_ids = data[0]
    id_list = [*map(lambda x: x.decode("utf-8"), mail_ids.split())]

    messages = []
    with alive_bar(len(id_list)) as bar:
        for response_part in id_list:
            try:
                # Email Fetch
                _, data = mail.fetch(response_part, "(RFC822)")
                # raw email
                raw_email = data[0][1].decode("utf-8")  # type: ignore
                # parse string
                msg = email.message_from_string(raw_email)
                # extract date
                email_dt_raw = datetime.strptime(
                    str(msg.get("Date")).split(",")[1].split("-")[0].strip()[:-3],
                    "%d %b %Y %H:%M",
                ).strftime("%m/%d/%Y %I:%M:%S %p")
                email_dt = datetime.strptime(email_dt_raw, "%m/%d/%Y %I:%M:%S %p")
                # make it tz aware
                if tz is not None:
                    timezone_to_use = pytz.timezone(tz)
                else:
                    timezone_to_use = pytz.timezone("UTC")
                email_dt = timezone_to_use.localize(email_dt)

                # subject + sender + msg
                email_subject = msg["subject"]
                email_from = msg["from"]
                email_message = str(msg.get_payload(decode=True))

                # + + + Cleaning + + +
                # start cleaning some chars
                for char in [
                    r"\t",
                    r"\n",
                    r"\r",
                    r"\xe2",
                    r"\x9c",
                    r"\xb7",
                    r"\x90",
                    r"\xc2",
                    r"\x94",
                    r"\x8c",
                    r"\xa057",
                    r"\x80",
                    r"\x9c",
                    r"\\",
                    r"\xa0",
                    r"\xf0",
                    r"\x9f",
                    r"\x93",
                    r"\x9d",
                ]:
                    cleaned_email_message = email_message.replace(char, "")
                # remove links
                cleaned_email_message = re.sub(
                    r"(?P<url>https?:[^\s]+)",
                    "",
                    cleaned_email_message,
                    flags=re.MULTILINE,
                )
                # remove HTML
                cleaned_email_message = BeautifulSoup(
                    cleaned_email_message, "lxml"
                ).text
                # remove extra chars
                cleaned_email_message = re.sub(
                    r"[\r\n\xc2\xb7]", "", cleaned_email_message, flags=re.MULTILINE
                )
                # + + + Cleaning + + +

                # info print
                print(email_dt)
                print(f"id : {response_part}")
                print(str(cleaned_email_message))

                messages.append(
                    {
                        "id": response_part,
                        "from": email_from,
                        "subject": email_subject,
                        "msg": cleaned_email_message,
                        "dt": email_dt,
                    }
                )
            except Exception as exc:
                print(f"Error while parsing email because -> {str(exc)}")
                continue

            # progress bar
            bar()

    return messages


# + + + Functions + + +
