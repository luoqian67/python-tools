##批量移动文件到指定目录
import os
import shutil
from pathlib import Path


def load(*paths, ext=('*.mp4'), r=False, pathh):
    for p in paths:
        path = Path(p)
        if path.is_dir():
            print(path)
            logs = path.rglob(ext) if r else path.glob(ext)
            for log in logs:
                name = os.path.basename(log)
                # full_path = os.path.join(pathh, name)
                des_path = pathh + '\\' + name

                # print(1,log)
                # print(2,des_path)
                shutil.move(log, des_path)

        elif path.is_file():
            pass


s = load("E:\\360Downloads\HTTP协议原理+实践 Web开发工程师必学", r=True, pathh='E:\\360Downloads\HTTP协议原理+实践 Web开发工程师必学')
