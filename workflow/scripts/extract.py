from showyourwork import exceptions
from showyourwork.logging import get_logger
import sys
import tarfile
from pathlib import Path
import tempfile
import shutil


# Snakemake config (available automagically)
config = snakemake.config  # type:ignore


# Initialize the logger
logger = get_logger()


# Input/output file names
zipfile = Path(snakemake.input[0])
extracted_file = Path(snakemake.output[0])
compressed_file = snakemake.params["compressed_file"]

# Tar balls
if zipfile.name.endswith(".tar") or zipfile.name.endswith(".tar.gz"):

    # Open the tarball
    with tarfile.open(zipfile) as f:

        # Extract into a temp folder
        with tempfile.TemporaryDirectory() as TEMP:

            try:

                f.extract(compressed_file, TEMP)

            except Exception as e:

                # TODO
                raise exceptions.TarballExtractionError()

            # Move it to target destination
            shutil.move(Path(TEMP) / compressed_file, extracted_file)

else:

    # TODO: Support zip files

    # TODO
    raise exceptions.NotImplementedError()