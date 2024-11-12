#!/bin/bash

# Autograder Source Dir
AGSDIR=/autograder/source
# MATLAB directory (default install)
MATLABDIR=/usr/local/MATLAB/R2022b

# Put the URL for your MATLAB zip file here
MATLAB_INSTALLER_URL="https://drive.google.com/file/d/13bYZ09uJJc706omAFYHnZka0OuDNESUO/view"

echo "Downloading MATLAB"
wget --quiet --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=13bYZ09uJJc706omAFYHnZka0OuDNESUO' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=13bYZ09uJJc706omAFYHnZka0OuDNESUO" -O $AGSDIR/matlab-installer.zip && rm -rf /tmp/cookies.txt

# Extract MATLAB
echo "Unzipping MATLAB"
unzip -q $AGSDIR/matlab-installer.zip -d $AGSDIR/matlab-installer

# Delete zip file to save space
rm -f $AGSDIR/matlab-installer.zip

echo "Installing MATLAB"
# Set permissions on installer
chmod +x $AGSDIR/matlab-installer/install
# chmod +x $AGSDIR/matlab-installer/bin/glnxa64/install_unix
# chmod +x $AGSDIR/matlab-installer/sys/java/jre/glnxa64/jre/bin/java
# Call installer
$AGSDIR/matlab-installer/install -inputFile $AGSDIR/matlab-installer/installer_input.txt

# Put license file in place
mkdir -p $MATLABDIR/licenses
mv $AGSDIR/network.lic $MATLABDIR/licenses

# Delete installer directory to save space
rm -rf $AGSDIR/matlab-installer

# Add ssh key for tunneling
mv $AGSDIR/{id_rsa,known_hosts} ~/.ssh

# Give proper permissions for supplementary files
chmod 0600 ~/.ssh/id_rsa

# Install any libraries needed by MATLAB
apt-get install -y libxt6

# Install the matlab engine package for calling matlab from Python
echo "Installing MATLAB engine python package"
# apt-get install -y python3.10
# python3.10 -m pip uninstall -y matlab
cd $MATLABDIR/extern/engines/python
python3 setup.py install

echo "malab_setup.sh completed"
