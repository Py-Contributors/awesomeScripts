import random
import string


def generate_random_password(
    length: int,
    option_list: list = [
        "number",
        "alpha",
        "specialchar"]) -> str:
    r"""Use this function to generate random password.

    :param {length} length of password

    :param {option_list} valid list option are 1) number 2)alpha 3) specialchar

    pass ["number"] to generate only number ["number","alpha"] to generate both

    Example : generate_random_password(10,["number","alpha","specialchar"])

    """
    letters_dict = {
        "number": string.digits,
        "alpha": string.ascii_letters,
        "specialchar": "[@_!#$%^&*()<>?/|}{~:]"
    }

    letters = ""
    # Iterate Over Option List and generate letters
    for option in option_list:
        # First Check if the option available in letters_dict
        if option in letters_dict.keys():
            # concate string to string
            letters = letters + letters_dict[option]

    # generate random string
    result_str = ''.join(random.choice(letters) for i in range(length))

    return result_str


print(generate_random_password(10, ["number", "alpha", "specialchar"]))
"""
Example How to Use :-
generate_random_password(10,["number"])
"""
