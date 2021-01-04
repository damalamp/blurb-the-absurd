# This script is to be run AFTER following the Readme and configuring the appropriate environment variables
# for the RPI_IP and RPI_USER
curr_git_branch=$(git branch --show-current )
SCRIPT="cd ~/code/blurb-the-absurd && ./rpi_pull_and_run_code.sh $curr_git_branch"
if [ -z "$RPI_USER" ]; then echo "RPI_USER environment variable has not been set"; fi
if [ -z "$RPI_USER" ]; then echo "RPI_USER environment variable has not been set"; fi
echo $RPI_USER
echo $RPI_IP
ssh -t $RPI_USER@$RPI_IP "${SCRIPT}"
