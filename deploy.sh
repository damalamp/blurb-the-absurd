#! /bin/bash

# Dev machine's SSH key much be copied to pi for scp to work without requiring password

if [ -z "$RPI_USER" ]; then echo "RPI_USER environment variable has not been set"; fi
proj_dir="blurb-the-absurd"

rsync -auzr ./deploy/* $RPI_USER@pi:~/${proj_dir}
ssh $RPI_USER@pi './blurb-the-absurd/run.sh'
