import json
from pathlib import Path

import AFDB_tools

path = Path(Path(snakemake.input[0]).parent.name).joinpath("structs")
all_structs = {}
for struct in path.iterdir():
    if struct.name.endswith(".pdb"):
        stats_result = AFDB_tools.descr(struct.as_posix())
        stats_dict = {}
        stats_dict["nobs"] = int(stats_result[0])
        stats_dict["min"] = float(stats_result[1][0])
        stats_dict["max"] = float(stats_result[1][1])
        stats_dict["mean"] = float(stats_result[2])
        stats_dict["variance"] = float(stats_result[3])
        stats_dict["skewness"] = float(stats_result[4])
        stats_dict["kurtosis"] = float(stats_result[5])
        all_structs[struct.name] = stats_dict
with open(snakemake.output[0], "w") as rfout:
    rfout.write(json.dumps(all_structs))
