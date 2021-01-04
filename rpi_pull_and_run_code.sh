echo "Printing from rpi, maybe?"
echo $1
cd ~/code/blurb-the-absurd
git pull origin $1
ls -la
pip3 install -r requirements.txt
python3
