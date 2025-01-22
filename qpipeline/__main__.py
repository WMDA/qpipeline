from .args import qpipeline_args
from .setup import set_environment


def main():
    arg = qpipeline_args()
    set_environment()


if __name__ == "__main__":
    main()
