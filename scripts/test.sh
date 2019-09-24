#!/bin/bash

set -e
set -o pipefail # if any code doesn't return 0, exit the script

function run_tests() {
 echo running tests, three python environments using tox
 tox
}

run_tests

exit 0
