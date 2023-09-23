TYPES = ["LINEAR", "HIPERBOLIC", "LOGISTIC"]

def validate_type(value, types, str):
    if value not in types:
        print(f"Invalid {str} operation")
        exit(1)


def validate_learning_rate(value):
    try:
        value = float(value)
        if value <= 0 or value > 1:
            raise ValueError
    except ValueError:
        print("Learning rate must be a positive float between 0 and 1")
        exit(1)


def validate_training_amount(value):
    try:
        value = float(value)
        if value <= 0 or value > 29:
            raise ValueError
    except ValueError:
        print("Training Amount must be a positive float")
        exit(1)


def validate_positive_int(value, str):
    try:
        value = int(value)
        if value <= 0:
            raise ValueError
    except ValueError:
        print(f"{str} must be a positive integer")
        exit(1)


def validate_bias(value):
    try:
        value = float(value)
    except ValueError:
        print("Bias must be a float")
        exit(1)


def get_input_data():
    pass


def get_expected_outputs():
    pass


def get_config_params(config):
    type = config["type"]
    validate_type(type, TYPES, "type")

    learning_rate = config["learning_rate"]
    validate_learning_rate(learning_rate)

    training_amount = config["training_amount"]
    validate_training_amount(training_amount)

    max_epochs = config["max_epochs"]
    validate_positive_int(max_epochs, "max_epochs")

    bias = config["bias"]
    validate_bias(bias)

    return type, learning_rate, training_amount, max_epochs, bias

