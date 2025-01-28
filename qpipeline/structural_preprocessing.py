from .qunex_commands import pre_freesurfer
from .utils import run_cmd
import os


def strucutral_hcp(args):
    qunex_con_image = os.environ["QUNEXCONIMAGE"].rstrip()
    pre_sufer_command = pre_freesurfer(
        args["study_folder"], args["id"], qunex_con_image, args["queue"]
    )
    run_cmd(pre_sufer_command)
