
import os
import sys



resources_path = os.getenv("RMANOUTPUTS")
if os.path.exists(resources_path):
    if resources_path not in sys.path:
        sys.path.append(resources_path)
