import datetime
from pathlib import Path
from typing import Any

from rdetoolkit.errors import catch_exception_with_message
from rdetoolkit.rde2util import Meta, write_to_json_file
from rdetoolkit.rdelogger import get_logger
from rdetoolkit.exceptions import StructuredError

logger = get_logger(__name__, file_path="data/logs/rdesys.log")

@catch_exception_with_message(error_message="Test Error Message!!")
def error_modules(a, b):
    raise Exception("Error in modules")

# pandasのDataFrameからグラフを描画する関数


class MetaParser:
    """Template class for parsing and saving metadata.

    This class serves as a template for the development team to parse and save metadata. It implements
    the IMetaParser interface. Developers can use this template class as a foundation for adding
    specific parsing and saving logic for metadata based on the project's requirements.

    Args:
        data (MetaType): The metadata to be parsed and saved.

    Returns:
        tuple[MetaType, MetaType]: A tuple containing the parsed constant and repeated metadata.

    Example:
        meta_parser = MetaParser()
        parsed_const_meta, parsed_repeated_meta = meta_parser.parse(data)
        meta_obj = rde2util.Meta(metaDefFilePath='meta_definition.json')
        saved_info = meta_parser.save_meta('saved_meta.json', meta_obj,
                                        const_meta_info=parsed_const_meta,
                                        repeated_meta_info=parsed_repeated_meta)

    """

    def __init__(self, data: Any = None):
        self.const_meta_info: Any = data
        self.repeated_meta_info: Any = {'analyser_work_function': ['3.700', '3.700', '3.700', '3.700', '3.700']}

    def parse(self, data: Any):
        """Parse and extract constant and repeated metadata from the provided data."""
        # dummy return
        self.const_meta_info: Any = data
        self.repeated_meta_info: Any = {'analyser_work_function': ['3.700', '3.700', '3.700', '3.700', '3.700']}
        return self.const_meta_info, self.repeated_meta_info

    def save_meta(  # noqa: ANN201
        self,
        save_path: Path,
        metaobj: Any,
        *,
        const_meta_info: Any | None = None,
        repeated_meta_info: Any | None = None,
    ) -> Any:
        """Save parsed metadata to a file using the provided Meta object."""
        if const_meta_info is None:
            const_meta_info = self.const_meta_info
        if repeated_meta_info is None:
            repeated_meta_info = self.repeated_meta_info
        metaobj.assign_vals(const_meta_info)
        metaobj.assign_vals(repeated_meta_info)

        # dummy return
        return metaobj.writefile(str(save_path))


@catch_exception_with_message(error_message="Test Error Message!!", verbose=True, error_code=50)
def success_modules(a, b):
    # # import pdb;pdb.set_trace()
    # logger.debug("test")
    # b.meta.joinpath("metadata.json").touch()
    # # data = {"measurement.measured_date": datetime.datetime(2012, 12, 16, 0, 0), 'analyser_work_function_or_acceptance_energy_of_atom_or_ion': ['3.700', '3.700', '3.700', '3.700', '3.700'], }
    # data = {"measurement.measured_date": datetime.datetime(2012, 12, 16, 0, 0), "analyzer_work_function": '3.700'}
    # m = MetaParser(data)
    # meta = Meta(a.tasksupport.joinpath("metadata-def.json"))
    # m.save_meta(b.meta.joinpath("metadata.json"), meta)
    # metaobj.assign_vals(repeated_meta_info)
    # write_to_json_file(b.meta.joinpath("metadata.json"), data)
    # グラフを描画する関数を挿入
    # raise StructuredError("error message in dataset()", 21)
    # raise Exception("error message in dataset()")
    print("Hello RDE!")

    pass
