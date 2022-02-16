from tuplesumfilter import types as t
from tuplesumfilter.app_logging import get_logger

logger = get_logger()


class UnknownFileFormat(ValueError):
    pass


def numbers_in_file(filepath: t.Pathlike) -> t.Sequence[t.Num]:
    logger.bind(input_filename=filepath)
    logger.debug("read inputfile")
    with open(filepath, mode="r", encoding="utf8") as infile:
        could_be_numbers = infile.readlines()
    try:
        logger.debug("trying to read file-contents as ints")
        return [int(s) for s in could_be_numbers]
    except ValueError:
        logger.debug("failed to read file as ints")
        ## no-op here so we can try parsing as floats
    try:
        logger.debug("trying to read file-contents as floats")
        return [float(s) for s in could_be_numbers]
    except ValueError as verr:
        mess = f"Cannot read {filepath}: format is newline-seperated list of numbers"
        logger.error(f"Failed to read file::: {mess}")
        raise UnknownFileFormat(mess) from verr
