# AWS Python Layer Generator

Simple script that packages a Python library into a layer and uploads it to AWS Lambda.

It can grab the latest version of the library from PyPI or from its Github repository.

## Prerequisites

You need to setup AWS credentials if you wish to upload the layer to AWS Lambda.

## Usage

```shell
$ pip install -r requirements.txt
$ python aws_python_layer_generator.py --help
$ python aws_python_layer_generator.py --module-name pandas --module-version 0.24.1 --python-version 3.7 --layer-name pandas-0.24.1 --check-github --upload-to-aws
```
