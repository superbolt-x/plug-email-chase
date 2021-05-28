"""
plug_email_chase main
---------------------
The Main module

Date: 2021-05-14

Author: Lorenzo Coacci
"""
# + + + Libraries + + +
import json
import os
import click

# + + + Libraries + + +


# + + + Settings + + +
# + + + Settings + + +


# + + + Functions + + +
# - - Plug Config - -
@click.command()
@click.option(
    "--config",
    default="schema/plug_config.json",
    help="The config file with custom pipeline settings.",
)
def parse_plug_config(config_path: str) -> dict:
    """RETURN a dict from the parsed json config"""
    # clean config input
    check = os.path.exists(config_path)
    if not check:
        raise FileNotFoundError(
            f"Plug Config filepath \
            does not exist: {config_path}"
        )

    with open(config_path, "r") as rf:
        config = json.loads(rf.read())

    return config


# - - Plug Credentials - -
@click.command()
@click.option("--credentials", help="The file with credentials.")
def parse_plug_credentials(credentials_path: str) -> dict:
    """RETURN a dict from the parsed json creds"""
    # clean creds input
    check = os.path.exists(credentials_path)
    if not check:
        raise FileNotFoundError(
            f"Plug Credentials filepath \
            does not exist: {credentials_path}"
        )

    with open(credentials_path, "r") as rf:
        creds = json.loads(rf.read())

    return creds


# - - Plug Catalog - -
@click.command()
@click.option("--credentials", help="The file with credentials.")
def parse_plug_catalog(catalog_path: str) -> dict:
    """RETURN a dict from the parsed json catalog"""
    # clean catalog input
    check = os.path.exists(catalog_path)
    if not check:
        raise FileNotFoundError(
            f"Plug Catalog filepath \
            does not exist: {catalog_path}"
        )

    with open(catalog_path, "r") as rf:
        catalog = json.loads(rf.read())

    return catalog


# - - Plug Target - -

# - - Plug State - -

# + + + Functions + + +
