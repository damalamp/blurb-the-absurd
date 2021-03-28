#! /bin/bash
# See https://google.github.io/styleguide/shellguide.html for script help

echo ${HOME}
proj_dir="${HOME}/blurb-the-absurd"
cd ${proj_dir} || echo "ERROR. No such Dir ${proj_dir}"

if [ "$1" == 'true' ];
then
  pip3 install -r requirements.txt && /usr/bin/python3 start.py;
else
    /usr/bin/python3 start.py
  fi
