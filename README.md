### blurb-the-absurd
A raspperry pi (pi) project to record and tweet X second spoken blurbs

### Project Road map
1. Setup raspberry pi to be available on the network
2. Streamline processes for copying code to RPi and executing
3. Manage credentials for all cloud services used
4. Configure rpi to startup and run script
5. Add hardware button to rpi to trigger recording
6. Design and print casing for pi, microphone, and button


### Improvements for V2
1. Add speakers for simple auditory feedback
2. Store all tweet recordings and text in s3 or firebase


### Getting Started
#### Assumptions
A familiarity with git, creating/deleting branches, committing to a branch, pushing to a remote branches etc.  
A vague familiarity with networking (ipv4, ipv6, ip address, mac address)  
A vague familiarity with SSH and public/private keys  

#### Setting up Raspberry Pi  
Make a bootable sd card for the raspberry pi (aka 'pi')  
Update sd card to connect to the network
Update sd card to enable SSHing on the rpi  
Using your router (or other tools), determine the IP address and mac address of the rpi, eg:  
`sudo apt-get install arp-scan`  
`sudo arp-scan --localnet`  
Find the rpi IP in the list, [export that IP address as an environment variable](https://linuxize.com/post/how-to-set-and-list-environment-variables-in-linux/) on your (Unix-based) PC, eg:  
`export RPI_IP=192.168.X.X`  
Either connect the raspberry pi to a monitor and control it as a computer, or begin an SSH session with the rpi.  
Remembering that default Rasbian OS has a root user of ['pi' and a password of 'raspberry'](https://pimylifeup.com/default-raspbian-username-and-password/)  
To ssh into  your pi from your PC run:  
`ssh pi@$RPI_IP`  
Once an SSH session has been initiated between your PC and the rpi, [create a new user](https://raspberrytips.com/new-user-on-raspberry-pi/) on the rpi to use going forward:  
`sudo adduser <username> sudo # Creates a user and enables them to perform sudo actions`  
`sudo usermod -aG sound,gpio <username> # to give <username> permissions to 1) record and play audio with audio devices attached to the rpi and 2) Control GPIO pins`
``
Confirm user was added to 'audio' group:
`groups <username>`

Set a password for the new user. 
This will be the user that the rpi will run the python code as now. 
Update 

Install python3 on the rpi, eg:
`sudo apt update`
`sudo apt install python3`
On your PC, export the username as an environment variable `RPI_USER`, eg:
`export RPI_USER=<username>`
And [create an alias](https://www.tecmint.com/create-alias-in-linux/) to facilitate sshing into the rpi from your PC's terminal:
`alias ssh_rpi='ssh "$RPI_USER"@"$RPI_IP"'`

And update the /etc/hosts file on your development machine to add a line aliasing the Pi's IP address for easier sshing, adding:
`196.168.0.### pi`  

Confirm all the appropriate environment variables and aliases have been set on your PC:
`echo $RPI_IP`
`echo $RPI_USER`
`which ssh_rpi`

Generate an SSH key on your PC. The public key needs to be copied to the Pi to enable sshing without providing a password every time.
On development machine, if you don't have an ssh key in ~/.ssh/ then, on your PC, run:  
`ssh-keygen -t rsa`

Copy your PC's public key to your rpi's list of known hosts, from your PC run:
`ssh-copy-id $RPI_USER@pi`

SSH into your Pi as the user you created:  
`ssh $RPI_USER@pi` (if you've updated the /etc/hosts file)

Once sshed into the pi, install:
Portaudio for recording functionality on the pi: `sudo apt-get install portaudio19-dev`
RPi.GPIO for controlling the GPIO pins: `sudo apt-get install python-rpi.gpio`


To transcribe audio you will need a google cloud account to transcribe audio recorded by your pi (TODO: explore using [Jasper](https://jasperproject.github.io)). 
Create a [google cloud account (GC)](https://support.google.com/a/answer/7389973?hl=en&ref_topic=7386475) to use their voice-to-text cloud API.
From your GC account, [go about getting a private json key](https://cloud.google.com/speech-to-text/docs/quickstart-protocol?hl=en_US).
Once you've downloaded the generated key to you PC, copy it to your rpi:
`rsync -auzr /path/to/downloaded/json/key $RPI_USER@pi:~/google-cloud-api-key.json`

On the pi, update the ~/.secrets file to export an environment variable pointing to that json key's location. Add the following to ~/.secrets on the pi:
`export GOOGLE_APPLICATION_CREDENTIALS=/home/<username>/google-cloud-api-key.json`

### Tweeting
Make/Login with a twitter account and visit [twitter's developer portal](https://developer.twitter.com/en) to create a twitter project which is needed to be issued the tokens needed to post tweets from the pi.
Having made a new twitter project, save the API Key, API Secret Key, and Bearer Token somewhere secure and NOT in your code.
Also generate a read & write [Access Token and Access Token Secret](https://www.slickremix.com/docs/how-to-get-api-keys-and-tokens-for-twitter/) for this project.
Finally add the keys/tokens to the ~/.secrets file on the pi ('Bearer Token' is not needed):
`export TWITTER_API_KEY=1mtaXXXXXXXXXXXXXXXXx1dQL`
`export TWITTER_API_SECRET=31K4KXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXvPG`
`export TWITTER_ACCESS_TOKEN=10000000000000000-zXXXXXXXXXXXXXXXXXXXXXXy`
`export TWITTER_ACCESS_TOKEN_SECRET=VfwXXXXXXXXXXXXXXXXXXXXXXXPoR`

Having set these keys/tokens as environment variables on the pi, now these credentials can be used by the [TwitterAPI](https://github.com/geduldig/TwitterAPI) package.


Fork this repo to have your own copy of the code
Clone your forked repo to your PC, eg:
`git clone git@github.com:<your-github-account>/blurb-the-absurd.git`

https://raspberrypi.stackexchange.com/questions/9951/pyaudio-recording-sound-on-pi-getting-errors
On your PC, run the `./deploy.sh` script (from this repo) to copy and run the files on your pi:  
`./deploy.sh -f` for a fresh run and pip install
or
`./deploy.sh -s` to stop all running python3 processes named 'start.py'

## Setting up Pi to auto run script:
See: https://www.wikihow.com/Execute-a-Script-at-Startup-on-the-Raspberry-Pi 
If you get ALSA errors when executing PyAudio, [try this](https://stackoverflow.com/questions/7088672/pyaudio-working-but-spits-out-error-messages-each-time).

https://stackoverflow.com/questions/7088672/pyaudio-working-but-spits-out-error-messages-each-time 
