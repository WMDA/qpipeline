import os
from .utils import run_cmd
import re


def study_create(study_folder: str, qunex_con_image: str, sub_id: str) -> list:
    """
    Function for the qunex create study command

    Parameteres
    -----------
    study_folder: str
        study folder path
    qunex_con_image: str
        qunex container path
    sub_id: str
        subject id

    Returns
    -------
    list: list object
        list of command
    """

    return [
        f"""qunex_container create_study \\
        --studyfolder={study_folder}/{sub_id}\\
        --bind={study_folder}:{study_folder}\\
        --container={qunex_con_image}
        """
    ]


def import_data(
    study_folder: str, qunex_con_image: str, sub_id: str, raw_data: str
) -> list:
    """
    Function for the qunex import bids command

    Parameteres
    -----------
    study_folder: str
        study folder path
    qunex_con_image: str
        qunex container path
    sub_id: str
        subject id

    Returns
    -------
    list: list object
        list of command
    """

    return [
        f"""qunex_container import_bids \\
    --sessionsfolder={study_folder}/{sub_id}/sessions \\
    --inbox={raw_data} \\
    --action=copy \\
    --archive=leave \\
    --overwrite=no \\
    --bind={study_folder}:{study_folder},{raw_data}:{raw_data} \\
    --container={qunex_con_image}
    """
    ]


def map_files() -> dict:
    """
    Function to map files in qunex format.
    Pipeline dynamically maps diffusion

    Parameters
    ----------
    None

    Returns
    -------
    dict: dictionary
        dict of mapping files
    """
    return {"T1w": "T1w", "T2w": "T2w"}


def map_scans(file_mapping: dict, label: str) -> str:
    """
    Function to map scans to correct quenx file name

    Parameters
    ----------
    file_mapping: dict
        dictionary of file mapping
    label: str
        label of scan name

    Returns
    -------
    str: str object
        string object of file mapping name
    """
    dwi_match = re.match(r"(dir[\d_]*-[AP]{2})_dwi", label)
    if dwi_match:
        return f"DWI:{dwi_match.group(1)}"
    return file_mapping.get(label, label)


def parse_output(output: str) -> None:
    """
    Function to parse through output
    to create mapping file

    Parameters
    ----------
    output: str
        stdout of qunex command

    Returns
    -------
    None
    """
    pattern = re.compile(r"---> linked (\d+\.nii\.gz) <-- sub-[^_]+_(.*)\.nii\.gz")
    mapped_files = {}
    file_mapping = map_files()
    for match in pattern.finditer(output):
        number = match.group(1).split(".")[0]
        label = match.group(2)
        mapped_files[number] = map_scans(file_mapping, label)
    result = [f"{num} => {label}" for num, label in mapped_files.items()]
    for item in result:
        print(item)


def set_up_qunex_study(args: dict) -> None:
    """
    Function for main set up quenx study

    Parameters
    ----------
    args: dict
        dictionary of cmd args

    Returns
    -------
    None
    """
    qunex_con_image = os.environ["QUNEXCONIMAGE"].rstrip()
    create_study = study_create(args["study_folder"], qunex_con_image, args["id"])
    print("Creating study")
    create_study_output = run_cmd(create_study)
    data_importing = import_data(
        args["study_folder"], qunex_con_image, args["id"], args["raw_data"]
    )
    import_data_output = output = run_cmd(data_importing)
    parse_output(import_data_output["stdout"])
