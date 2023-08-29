sudo apt-get update -y
sudo apt-get install --no-install-recommends -y patchelf python3 python3-dev build-essential libfuse-dev
python3 -m pip install nuitka==1.7

python3 -m nuitka --onefile --nofollow-import-to=pytest --include-data-dir=translatepy/data=translatepy/data --include-data-files=translatepy/cli/tui/app.css=translatepy/cli/tui/app.css --python-flag=isolated,nosite,-O --plugin-enable=anti-bloat,implicit-imports,data-files,pylint-warnings --warn-implicit-exceptions --warn-unusual-code --prefer-source-code --static-libpython=yes translatepy
