# pyrallelize
[![Build
Status](https://travis-ci.org/EvandroLG/pyrallelize.svg?branch=master)](https://travis-ci.org/EvandroLG/pyrallelize)

Simple solution to make parallel download with Python

## Why?
Sometimes we need to download a lot of files and by default Python runs all procedurally, what can take long time for end.
The library is a solution to that problem, `pyrallelize` downloads all files in parallel using multiprocessing.

## Install
To install `pyrallelize`, simply:
```shell
$ pip install pyrallelize
```

## How does it work?
Follow an example:
```python
  from pyrallelize import pyrallelize

  pyrallelize([
    'http://example.com/image-1.jpg',
    'http://example.com/image-2.jpg',
    'http://example.com/image-3.jpg',
    'http://example.com/image-4.jpg',
    'http://example.com/image-5.jpg'
  ])
```

## Parameters
* **url_list** <code>list</code>
* **directory** <code>str</code>

## Contributing

### Install Dependencies

```shell
$ make install_dependencies
```

### Running tests

```shell
$ make test
```
