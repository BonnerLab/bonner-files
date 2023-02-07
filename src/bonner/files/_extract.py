from pathlib import Path
import tarfile
import zipfile

from loguru import logger


def untar(filepath: Path, *, extract_dir: Path = None, remove_tar: bool = True) -> Path:
    if extract_dir is None:
        extract_dir = Path("/tmp")

    logger.debug(f"Extracting from {filepath} to {extract_dir}")
    with tarfile.open(filepath) as tar:
        tar.extractall(path=extract_dir)

    if remove_tar:
        logger.debug(f"Deleting {filepath} after extraction")
        filepath.unlink()

    return extract_dir


def unzip(filepath: Path, *, extract_dir: Path = None, remove_zip: bool = True) -> Path:
    if extract_dir is None:
        extract_dir = Path("/tmp")

    logger.debug(f"Extracting from {filepath} to {extract_dir}")
    with zipfile.ZipFile(filepath, "r") as f:
        f.extractall(extract_dir)

    if remove_zip:
        logger.debug(f"Deleting {filepath} after extraction")
        filepath.unlink()

    return extract_dir
