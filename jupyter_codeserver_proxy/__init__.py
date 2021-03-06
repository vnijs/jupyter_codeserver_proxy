"""
Return config on servers to start for codeserver

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os
import shutil


def setup_codeserver():
    # Make sure codeserver is in $PATH
    def _codeserver_command(port):
        full_path = shutil.which("code-server")
        if not full_path:
            raise FileNotFoundError("Can not find code-server in $PATH")
        working_dir = os.getenv("CODE_WORKINGDIR", None)
        if working_dir is None:
            working_dir = os.getenv("JUPYTER_SERVER_ROOT", ".")
        elif os.path.isdir(working_dir) is False:
            os.mkdir(working_dir)
        data_dir = os.getenv("CODE_USER_DATA_DIR", "")
        if data_dir != "":
            data_dir = "--user-data-dir=" + str(data_dir)
        extensions_dir = os.getenv("CODE_EXTENSIONS_DIR", "")
        if extensions_dir != "":
            extensions_dir = "--extensions-dir=" + str(extensions_dir)
        builtin_extensions_dir = os.getenv("CODE_BUILTIN_EXTENSIONS_DIR", "")
        if builtin_extensions_dir != "":
            builtin_extensions_dir = "--builtin-extensions-dir=" + str(
                builtin_extensions_dir
            )

        return [
            full_path,
            "--port=" + str(port),
            "--allow-http",
            "--no-auth",
            "--vanilla",
            data_dir,
            extensions_dir,
            builtin_extensions_dir,
            working_dir,
        ]

    return {
        "command": _codeserver_command,
        "timeout": 20,
        "launcher_entry": {
            "title": "VS Code",
            "icon_path": os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "icons", "vscode.svg"
            ),
        },
    }
