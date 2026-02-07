
"""Example reusable function for pipelines/notebooks."""

def transform(values):
    """Simple transform: return unique, sorted values.
    Args:
        values (list): list of hashable items
    Returns:
        list: unique sorted values
    """
    return sorted(set(values))
