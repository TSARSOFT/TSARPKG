mkdir ~/TSARSOFT
mkdir ~/TSARSOFT/TSARPKG
cd ~/TSARSOFT/TSARPKG
rm ~/TSARSOFT/TSARPKG/* -r
wget 'https://github.com/TSARSOFT/TSARPKG/blob/master/TSARPKG-latest.zip?raw=true'
mv ~/TSARSOFT/TSARPKG/TSARPKG-latest.zip\?raw=true ~/TSARSOFT/TSARPKG/TSARPKG-latest.zip
unzip ./TSARPKG-latest.zip
echo 'python3 ~/TSARSOFT/TSARPKG/latest/TSARPKG.py' >> ~/TSARSOFT/TSARPKG/run.sh
chmod 777 ./run.sh
echo 'installation of TSARPKG complete! rus using command ~/TSARSOFT/TSARPKG/run.sh'
