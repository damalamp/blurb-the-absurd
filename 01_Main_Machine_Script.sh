
git add .
git commit -m "wip"
git push origin dev
# RPI_USER, RPI_IP, and RPI_PROJ_DIR can be set as environment variables
ssh -l ${RPI_USER} ${RPI_IP} "~/code/02_rpi_gitpull.sh"
