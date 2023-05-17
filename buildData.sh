#!/bin/bash

CYAN="\033[0;36m"
WHITE="\033[0;37m"
GREEN="\033[0;32m" 

echo -e "# ${White}Author  :  ${Cyan}Max Lawton${White}"
echo -e "# ${White}Version :  ${Cyan}May 16, 2023${White}"

pip3 install pandas
pip3 install mwparserfromhell
pip3 install requests

echo -e "# ${Green}Added all Required Dependencys${White}"
echo -e "# ${Green}Compiling dataset:${White}"

python3 main.py

echo -e "# ${Green}Finished!${White}"