"""
plug_email_chase transform
--------------------------
The Transform Submodule

Date: 2021-05-14

Author: Lorenzo Coacci
"""


# + + + Libraries + + +

# + + + Libraries + + +


# + + + Settings + + +
# + + + Settings + + +


# + + + Functions + + +
def map_categories(category):
    # classify categories
    if category is None:
        return (None, None)
    category_norm = category.lower()
    CATEGORIES = {}
    for key, value in CATEGORIES.items():
        for element in value:
            if element.lower() in category_norm:
                return (key, None)

    return (None, None)


# + + + Functions + + +
