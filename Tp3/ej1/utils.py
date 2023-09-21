
INPUT_DATA =  [[-1, 1], [1, -1], [-1, -1], [1, 1]]
EXPECTED_AND_OUTPUT = [-1, -1, -1, 1]
EXPECTED_XOR_OUTPUT = [1, 1, -1, -1]
OPERATIONS = ["AND", "XOR"]

def validate_operation(value, operations, str):
    if value not in operations:
        print(f"Invalid {str} operation")
        exit(1)


def validate_positive_float(value, str):
    try:
        value = float(value)
        if value < 0 or value > 1:
            raise ValueError
    except ValueError:
        print(f"{str} must be a positive float between 0 and 1")
        exit(1)


def validate_positive_int(value, str):
    try:
        value = int(value)
        if value <= 0:
            raise ValueError
    except ValueError:
        print(f"{str} must be a positive integer")
        exit(1)


def get_input_data():
    return INPUT_DATA


def get_expected_outputs(operation):
    if operation == "AND":
        return EXPECTED_AND_OUTPUT
    else:
        return EXPECTED_XOR_OUTPUT


def get_config_params(config):
    operation = config["operation"]
    validate_operation(operation, OPERATIONS, "operation")

    learning_rate = config["learning_rate"]
    validate_positive_float(learning_rate, "learning_rate")

    max_epochs = config["max_epochs"]
    validate_positive_int(max_epochs, "max_epochs")

    bias = config["bias"]
    validate_positive_float(bias, "bias")

    return operation, learning_rate, max_epochs, bias