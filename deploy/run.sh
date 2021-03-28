# See https://google.github.io/styleguide/shellguide.html for script help

proj_dir="blurb-the-absurd"
cd ${proj_dir} || echo "ERROR. No such Dir ${proj_dir}"
echo "\$0=$0"

if [ "$1" == 'true' ];
then
  pip3 install -r requirements.txt && python3 start.py;
else
    python3 start.py
  fi
