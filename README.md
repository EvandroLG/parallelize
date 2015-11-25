# parallelize
Simple solution to make parallel download with Python

## Why?
Sometimes we need to download a lot of files and by default Python runs all procedurally, what can take long time for end.
The library is a solution to that problem, `parallelize` downloads all files in parallel using multiprocessing.

## How does it work?
Follow an example:
```python
  from parallelize import parallelize

  parallelize([
    'http://example.com/image-1.jpg',
    'http://example.com/image-2.jpg',
    'http://example.com/image-3.jpg',
    'http://example.com/image-4.jpg',
    'http://example.com/image-5.jpg'
  ])
```
