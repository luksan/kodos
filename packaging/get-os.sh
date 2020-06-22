#!/bin/sh

UBUNTU_OS="$(grep -oP '(?<=DISTRIB_ID=)[a-zA-Z]+' /etc/lsb-release)-$(grep -oP '(?<=DISTRIB_CODENAME=)[a-zA-Z]+' /etc/lsb-release)"
UBUNTU_OS=$(echo "${UBUNTU_OS}" | tr '[:upper:]' '[:lower:]')

echo "${UBUNTU_OS}"
