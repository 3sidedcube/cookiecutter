import os
import shutil

REMOVE_PATHS = [
    "{% if not cookiecutter.include_docs_dir %}docs{% endif %}",
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        (
            os.unlink(path)
            if os.path.isfile(path)
            else shutil.rmtree(path, ignore_errors=True)
        )
