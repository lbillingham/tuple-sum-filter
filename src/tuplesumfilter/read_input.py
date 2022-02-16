from tuplesumfilter import types as t


class UnknownFileFormat(ValueError):
    pass


def numbers_in_file(filepath: t.Pathlike) -> t.Sequence[t.Num]:
    with open(filepath, mode="r", encoding="utf8") as infile:
        could_be_numbers = infile.readlines()
    try:
        return [int(s) for s in could_be_numbers]
    except ValueError:
        ## no-op here so we can try parsing as floats
        pass
    try:
        return [float(s) for s in could_be_numbers]
    except ValueError as verr:
        mess = f"Cannot read {filepath}: format is newline-seperated list of numbers"
        raise UnknownFileFormat(mess) from verr
