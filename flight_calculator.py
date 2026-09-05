"""Drone flight-time calculator module."""

def calculate_flight_time(weight_grams):
    """Calculate active flight time in minutes for a payload weight.

    Args:
        weight_grams: Payload weight in grams.

    Returns:
        Active flight time in minutes.
    """
    if weight_grams < 0:
        raise ValueError("Weight cannot be negative.")

    flight_time = 180 - 0.1 * weight_grams
    return max(0, flight_time)


def flight_time_table(max_weight_grams, step_grams):
    """Create a table of payload weights and their flight times.

    Args:
        max_weight_grams: Maximum payload weight in grams.
        step_grams: Increment between payload weights in grams.

    Returns:
        A list of (weight, flight_time) pairs.
    """
    table = []

    for weight in range(0, max_weight_grams + 1, step_grams):
        table.append((weight, calculate_flight_time(weight)))

    return table