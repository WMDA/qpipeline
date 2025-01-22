import argparse


def qpipeline_args() -> dict:
    """
    Function to take

    Parameters
    ----------
    None

    Returns
    -------
    dict: dictionary
        dict of cmd args
    """
    base_args = argparse.ArgumentParser(
        prog="qpipeline",
        description=print(splash()),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    base_args.add_argument(
        "-s",
        "--study_folder",
        help="Path to study folder",
        required=True,
    )
    base_args.add_argument(
        "-r",
        "--raw_data",
        help="Path to raw data",
        required=True,
    )
    base_args.add_argument(
        "-i",
        "--id",
        help="Subject ID",
        required=True,
    )
    base_args.add_argument(
        "-q",
        "--queue",
        help="Queue name to submit to",
        required=True,
    )

    return vars(base_args.parse_args())


def splash() -> str:
    """
    Function to return Splash

    Parameters
    ---------
    None

    Returns
    -------
    str: string object
        splash string
    """
    return """
               .__                 .__   .__                 
  ____________  |__|______    ____  |  |  |__|  ____    ____  
 / ____/\____ \ |  |\____ \ _/ __ \ |  |  |  | /    \ _/ __ \ 
< <_|  ||  |_> >|  ||  |_> >\  ___/ |  |__|  ||   |  \\  ___/ 
 \__   ||   __/ |__||   __/  \___  >|____/|__||___|  / \___  >
    |__||__|        |__|         \/                \/      \/ 
    """
