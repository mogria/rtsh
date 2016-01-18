#!/bin/bash

set_attr_str() {
    jq --arg attr "$2" ".$1 = \$attr"
}

set_attr() {
    jq --argjson attr "$2" ".$1 = \$attr"
}


