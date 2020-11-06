# _*_ coding:utf-8 _*_

pyinstaller\
    --clean\
    --noconfirm\
    -w\
    build.spec

# or shell
# pyinstaller -F -w --clean -y src/app.py

# sign app
# sudo codesign --force --deep --sign - ./dist/StringUtilities.app
