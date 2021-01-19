echo "Printing from rpi, maybe?"
echo $1
cd ~/code/blurb-the-absurd
git pull origin $1
ls -la
pip3 install -r requirements.txt
python3


# This script is to be run AFTER following the Readme and configuring the appropriate environment variables
# for the RPI_IP and RPI_USER

if [ -z "$RPI_USER" ]; then echo "RPI_USER environment variable has not been set"; fi
if [ -z "$RPI_IP" ]; then echo "RPI_IP environment variable has not been set"; fi

curr_branch=${git rev-parse --abbrev-ref HEAD}
echo $curr_branch
cd ~/code/blurb_the_absurd
ssh $RPI_USER@$RPI_IP ./rpi_pull_and_run_code.sh $curr_branch
