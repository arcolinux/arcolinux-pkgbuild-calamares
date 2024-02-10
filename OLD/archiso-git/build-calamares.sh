#!/bin/bash
#https://wiki.archlinux.org/index.php/DeveloperWiki:Building_in_a_Clean_Chroot

destination1=$HOME"/ARCO/ARCOLINUX-REPO/arcolinux_repo/x86_64/"
destination2=$HOME"/ARCO/ARCOLINUX-REPO/arcolinux_repo_3party/x86_64/"
destination3=$HOME"/ARCO/ARCOLINUX-REPO/arcolinux_repo_iso/x86_64/"
destination4=$HOME"/ARCO/ARCOLINUX-REPO/arcolinux_repo_testing/x86_64/"
destination5=$HOME"/ARCO/ARCOLINUX-REPO/arcolinux_repo_xlarge/x86_64/"
destination6=$HOME"/ARCO/TEST/"

destiny=$destination4

# 2. makepkg"
# 1. chroot"


search1=$(basename "$PWD")
search2=arcolinux

search=$search1

tput setaf 2
echo "#############################################################################################"
echo "#########        Let us build the package "$(basename `pwd`)
echo "#############################################################################################"
tput sgr0

makepkg --sign

echo "Moving created files to " $destiny
echo "#############################################################################################"
mv $search*pkg.tar.zst $destiny
mv $search*pkg.tar.zst.sig $destiny
echo "Cleaning up"
echo "#############################################################################################"
echo "deleting unnecessary folders"
echo "#############################################################################################"

rm -rf pkg src

echo "deleting unnecessary files"
echo "#############################################################################################"

rm calamares-*

tput setaf 8
echo "#############################################################################################"
echo "###################                       build done                   ######################"
echo "#############################################################################################"
tput sgr0
