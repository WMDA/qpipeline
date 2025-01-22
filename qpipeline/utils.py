import subprocess


def error_and_exit(
    bool_statement: bool,
    error_message: str = None,
) -> None:
    """
    Function to exit out of script
    with error message if bool statement
    is false.

    Parameters
    ----------
    bool_statement: bool
       statement to evaluate
    error_message: str
        error message to print
        out. Default is None

    Returns
    -------
    None
    """
    if not bool_statement:
        if error_message:
            error_message = re.sub(r"\[Errno 2\]", "", error_message)
            col = colours()
            print("\033[1;31m" + error_message + "\033[0;0m")
        print("Exiting...\n")
        exit(1)


def run_cmd(command: list) -> dict:
    """
    Function to run cmd command
    """
    try:
        run = subprocess.run(command, capture_output=True)
    except subprocess.CalledProcessError as error:
        error_and_exit(False, f"Error in calling commnd due to: {error}")
    except KeyboardInterrupt:
        run.kill()

    output = {
        key: value.decode("utf-8").strip() if isinstance(value, bytes) else value
        for key, value in vars(run).items()
    }
    if output["stderr"]:
        error_and_exit(False, f"Command failed due to {output['stderr']}")
    return output
