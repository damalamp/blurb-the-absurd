#! /bin/bash

# Dev machine's SSH key much be copied to pi for scp to work without requiring password

fresh_install=''
while getopts 'f' flag; do
  case "${flag}" in
    f) fresh_install='true' ;;
    *) error "Unexpected option ${flag}" ;;
  esac
done
echo "ZZZ fresh_install=$fresh_install"

if [ -z "$RPI_USER" ]; then echo "RPI_USER environment variable has not been set"; fi
proj_dir="blurb-the-absurd"

rsync -auzr ./deploy/* $RPI_USER@pi:~/${proj_dir}
ssh $RPI_USER@pi "source ~/.secrets && ./blurb-the-absurd/run.sh $fresh_install"
