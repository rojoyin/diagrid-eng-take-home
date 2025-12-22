import pkgutil
import importlib

ALL_TOOLS = []

for _, modname, _ in pkgutil.walk_packages(
    path=__path__, prefix=f"{__name__}."
):
    module = importlib.import_module(modname)
    # Export the tool function (assumes function name matches module name)
    tool_name = modname.split('.')[-1]  # e.g., "tools.read_file" -> "read_file"
    if hasattr(module, tool_name):
        tool_func = getattr(module, tool_name)
        ALL_TOOLS.append(tool_func)
