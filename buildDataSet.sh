#!/bin/bash

CYAN= '\033[0;36m'
WHITE= '\033[0;37m' 
GREEN= '\033[0;32m'   

echo -e "# ${White}Author  :  ${Cyan}Max Lawton${White}"
echo -e "# ${White}Version :  ${Cyan}Apr 22, 2023${White}"

pip3 install pandas
pip3 install mwparserfromhell
pip3 install requests

echo -e "# ${Green}Added all Required Dependencys${White}"
echo -e "# ${Green}Compiling dataset:${White}"

python3 Wikipedia_CSVs.py

echo -e "# ${Green}Setting up dataset segmentation:${White}"

python3 BreakDown.py

echo -e "# ${Green}Finished!${White}"