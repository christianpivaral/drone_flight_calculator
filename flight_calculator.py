# Drone Flight-Time Calculator

# Calculate flight time using T(w) = 180 - 0.1w.
# Raise ValueError if weight_grams is negative and never return less than 0.
# Copilot wrote "seconds" in the docstring. Changed it to "minutes".
def calculate_flight_time(weight_grams):
    """
    Calculate the flight time of a drone based on its weight.

    Args:
        weight_grams (float): The weight of the drone in grams.

    Returns:
        float: The flight time in minutes.

    Raises:
        ValueError: If the weight is negative.
    """
    if weight_grams < 0:
        raise ValueError("Weight cannot be negative.")

    flight_time = 180 - 0.1 * weight_grams
    return max(flight_time, 0)


# Create a table of flight times from 0 to the max weight using the given step.
# Use calculate_flight_time() to get the flight time for each weight.
# Copilot suggested this function. Accepted as-is.
def flight_time_table(max_weight_grams, step_grams):
    """
    Generate a table of flight times for weights from 0 to max_weight_grams.

    Args:
        max_weight_grams (float): The maximum weight in grams.
        step_grams (float): The step size in grams.

    Returns:
        list of tuples: A list containing tuples of (weight, flight_time).
    """
    if max_weight_grams < 0 or step_grams <= 0:
        raise ValueError("Max weight must be non-negative and step must be positive.")

    table = []
    for weight in range(0, int(max_weight_grams) + 1, int(step_grams)):
        flight_time = calculate_flight_time(weight)
        table.append((weight, flight_time))

    return table