#!/bin/bash

MODULES=( apache bootstrap mysql other php python )

#---------------------
# Setup
#---------------------
function puppetCreateModule {

    module=$1

    echo "Create ${module}"
    baseMoudleDir="puppet/modules/${module}"

    mkdir ${baseMoudleDir}
    mkdir ${baseMoudleDir}/manifests
    mkdir ${baseMoudleDir}/files

    touch ${baseMoudleDir}/manifests/init.pp

}

function main {

    echo "========================="
    echo "Setup: create directories " 
    echo "-------------------------"

    mkdir puppet/manifests
    mkdir puppet/modules 
    mkdir puppet/scripts
    mkdir puppet/templates

    touch puppet/manifests/default.pp

    for module in "${MODULES[@]}" 
    do
	puppetCreateModule ${module}
    done

}

main
