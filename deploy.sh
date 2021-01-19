#! /bin/bash

# Dev machine's SSH key much be copied to pi for scp to work without requiring password
#scp -r $(pwd)/deploy $RPI_USER@pi:~/tmp_blurb-the-absurd
rsync -auzr ./deploy/* david@pi:~/blurb-the-absurd
ssh $RPI_USER@pi 'python3 ~/blurb-the-absurd/start.py'
