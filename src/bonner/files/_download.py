from pathlib import Path
import uuid
import requests

from loguru import logger


def download(
    url: str,
    *,
    filepath: Path = None,
    stream: bool = True,
    allow_redirects: bool = True,
    chunk_size: int = 1024**2,
    force: bool = True,
) -> Path:
    if filepath is None:
        filepath = Path("/tmp") / f"{uuid.uuid4()}"
    elif filepath.exists():
        if not force:
            logger.debug(
                "Using previously downloaded file at"
                f" {filepath} instead of downloading from {url}"
            )
            return filepath
        else:
            filepath.unlink()

    logger.debug(f"Downloading from {url} to {filepath}")
    r = requests.Session().get(url, stream=stream, allow_redirects=allow_redirects)
    filepath.parent.mkdir(exist_ok=True, parents=True)
    with open(filepath, "wb") as f:
        for chunk in r.iter_content(chunk_size=chunk_size):
            f.write(chunk)

    return filepath