"""
plug_email_chase utils
----------------------
The utils module

Date: 2021-05-14

Author: Lorenzo Coacci
"""
# + + + Libraries + + +
import json
import os
# + + + Libraries + + +


# + + + Settings + + +
# + + + Settings + + +


# + + + Functions + + +
# - - Plug Config - -
def parse_plug_config(config_path: str) -> dict:
    """RETURN a dict from the parsed json config"""
    # clean config input
    config_path = str(config_path)
    check = os.path.exists(config_path)
    if not check:
        raise f"Plug Config filepath does not exist: {config_path}"

    with open(config_path, 'r') as f:
        config = json.loads(f.read())

    return config

# - - Plug Catalog - -

# - - Plug Target - -

# - - Plug State - -

# + + + Functions + + +
