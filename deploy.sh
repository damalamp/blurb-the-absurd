#! /bin/bash

# Dev machine's SSH key much be copied to pi for scp to work without requiring password

fresh_install='false'
stop_process='false'

while getopts 'fs' flag; do
  case "${flag}" in
    f) fresh_install='true' ;;
    s) stop_process='true' ;;
    *) error "Unexpected option ${flag}" ;;
  esac
done

if [ -z "$RPI_USER" ]; then echo "RPI_USER environment variable has not been set"; fi
proj_dir="blurb-the-absurd"


if [ $stop_process == 'true' ];
then
  ssh $RPI_USER@pi "./blurb-the-absurd/stop.sh"
else
  rsync -auzr ./deploy/* $RPI_USER@pi:~/${proj_dir}
  ssh $RPI_USER@pi "source ~/.secrets && ./blurb-the-absurd/run.sh $fresh_install"
  fi


