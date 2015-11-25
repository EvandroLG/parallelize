# -*- coding: utf-8 -*-

from multiprocessing import Pool
import urllib.request
import shutil


def _download(url):
    file_name = url.split('/')[-1]
    urlopen = urllib.request.urlopen

    with urlopen(url) as response, open(file_name, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)


def parallelize(url_list):
    if isinstance(url_list, list):
        p = Pool(len(url_list))
        p.map(_download, url_list)
    elif isinstance(url_list, str):
        _download(url_list)
    else:
        raise TypeError()
