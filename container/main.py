# The following script is a template for the source code.
from modules.modules import success_modules
from rdetoolkit.models.config import Config, SystemSettings, MultiDataTileSettings, SmartTableSettings

import rdetoolkit

# cfg = Config(
#           system=SystemSettings(
#               #extended_mode="multidatatile", #NG
#               #extended_mode="multidata_tile", #OK
#             #   extended_mode="rdeformat", #OK
#             #   extended_mode="Multi_Data_Tile", #OK
#             #   extended_mode="MultiDataTile", #NG
#               save_raw=True,
#               save_nonshared_raw=False,
#               save_main_image=False,
#           ),
#           multidata_tile=MultiDataTileSettings(
#               ignore_errors=True
#           ),
#           smarttable=SmartTableSettings(
#                 save_table_file=True,
#           )
# )

rdetoolkit.workflows.run(custom_dataset_function=success_modules)
# rdetoolkit.workflows.run(custom_dataset_function=success_modules, config=cfg)

# path = "/Users/sonokawa/Desktop/work/develop-rdetoolkit/container/data/T3A800 Data.TXT"
# rtn = read_file_with_encoding(path)
# print(rtn)
# enc = detect_encoding(path)
# print(enc)
