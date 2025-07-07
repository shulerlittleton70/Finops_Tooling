# finops_agents/utils/cur_utils.py

from finops_agents.cur_dictionary import describe_field

def list_known_fields():
    """
    Prints all known CUR fields and descriptions.
    """
    for key in sorted(describe_field.keys()):
        print(f"{key}: {describe_field(key)}")
