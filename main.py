from rdetoolkit.config import Config, MultiDataTileSettings, SystemSettings
from rdetoolkit.workflows import run

from container.modules.modules import error_modules, success_modules

# config = Config(
#     system=SystemSettings(extended_mode="MultiDataTile", save_raw=False, save_nonshared_raw=True, save_thumbnail_image=True),
#     multidata_tile=MultiDataTileSettings(ignore_errors="False")
# )
# config.mysetting = "Hello"

results = run(custom_dataset_function=success_modules)

print(results)
