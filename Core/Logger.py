import datetime


def log_message(filename, message, level):
    list_level = ["INFO", "WARNING", "ERROR"]
    if level not in list_level:
        raise Exception(f"BAD LOGGER LEVEL: Please use {list_level}")
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_output = f"[{time}] [{level}] {message}\n"

    with open(filename, "a") as file:
        file.write(log_output)


log_message("application.log", "User logged in", "INFO")
log_message("application.log", "Failed login attempt", "WARNING")


