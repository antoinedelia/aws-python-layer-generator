import requests
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "--module-name", "-m", required=True, help="The module to package as a Lambda Layer", dest="module_name"
)
parser.add_argument(
    "--module-version",
    "-mv",
    required=True,
    help="The module version to package as a Lambda Layer",
    dest="module_version",
)
parser.add_argument(
    "--python-version", "-pv", required=True, help="The Python version used by the Lambda Layer", dest="python_version"
)
parser.add_argument(
    "--layer-name",
    "-name",
    required=False,
    help="The name of the Lambda Layer (defaults to {module_name}-{module_version}-{python_version})",
    dest="layer_name",
)
parser.add_argument(
    "--check-github",
    required=False,
    help="Lookup module's GitHub for a newer release",
    dest="should_check_github",
    action="store_true",
)

# With action='store_true', if arg is specified, it's True, otherwise False.
parser.add_argument(
    "--upload-to-aws",
    "-aws",
    required=False,
    action="store_true",
    help="Upload the generated Lambda Layer to AWS",
    dest="should_upload_to_aws",
)

args = parser.parse_args()

print(args.module_version)
