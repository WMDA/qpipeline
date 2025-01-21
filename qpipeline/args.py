import argparse

def qpipeline_args() -> dict:
    base_args = argparse.ArgumentParser(
        prog="qpipeline",
        description=print(splash()),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    return 

def splash() -> str:
    return """
               .__                 .__   .__                 
  ____________  |__|______    ____  |  |  |__|  ____    ____  
 / ____/\____ \ |  |\____ \ _/ __ \ |  |  |  | /    \ _/ __ \ 
< <_|  ||  |_> >|  ||  |_> >\  ___/ |  |__|  ||   |  \\  ___/ 
 \__   ||   __/ |__||   __/  \___  >|____/|__||___|  / \___  >
    |__||__|        |__|         \/                \/      \/ 
    """