#!/bin/bash

# Script to fetch new data from api and update csv

set -e
set -o pipefail

function cleanup {
  exit $?
}
trap "cleanup" EXIT

DIR="$(cd "$(dirname "$0")" && pwd)"

$DIR/blend_data.py
