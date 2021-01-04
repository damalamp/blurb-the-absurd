### blurb-the-absurd
A rasperry pi (rpi) project to record and tweet X second spoken blurbs

### Project Road map
1. Setup raspberry pi to be available on the network
2. Streamline processes for deploying code to RPi
3. Manage credentials for all cloud services used
4. Configure rpi to startup and run script
5. Add hardware button to rpi to trigger recording
6. Design and print casing for pi, microphone, and button


### Improvements for V2
1. Add speakers for simple auditory feedback
2. Store all tweet recordings and text in s3 or firebase


### Getting Started
#### Assumptions
A familiarity with git, creating/deleting branches, committing to a branch, push to remote branches etc.
A vague familiarity with networking (ipv4, ipv6, ip address, mac address)
A vague familiarity with SSH and public/private keys

#### Setting up Raspberry Pi
Make a bootable sd card for the raspberry pi (rpi)
Update sd card to connect to the network
Update sd card to enable SSHing on the rpi
Using your router (or other tools), determine the IP address and mac address of the rpi, eg:
`sudo apt-get install arp-scan`
`sudo arp-scan --localnet`
Find the rpi IP in the list, [export that IP address as an environment variable](https://linuxize.com/post/how-to-set-and-list-environment-variables-in-linux/) on your (Unix-based) PC, eg:
`export RPI_IP=192.168.X.X`
Either connect the raspberry pi to a monitor and control it as a computer, or begin an SSH session with the rpi.
Remembering that default Rasbian OS has a root user of ['pi' and a password of 'raspberry'](https://pimylifeup.com/default-raspbian-username-and-password/)
From your PC run:
`ssh pi@$RPI_IP`
Once an SSH session has been initiated between your PC and the rpi, [create a new user](https://raspberrytips.com/new-user-on-raspberry-pi/) on the rpi to use going forward:
`sudo adduser <username> sudo # Creates a user and enables them to perform sudo actions`
Set a password for the new user.
This will be the user that the rpi will run the python code as now.

Install python3 on the rpi, eg:
`sudo apt update`
`sudo apt install python3`
On your PC, export the username as an environment variable `RPI_USER`, eg:
`export RPI_USER=<username>`
And [create an alias](https://www.tecmint.com/create-alias-in-linux/) to facilitate sshing into the rpi from your PC's terminal:
`alias ssh_rpi='ssh "$RPI_USER"@"$RPI_IP"'`

Confirm all the appropriate environment variables and aliases have been set on your PC:
`echo $RPI_IP`
`echo $RPI_USER`
`which ssh_rpi`

Fork this repo to have your own copy of the code
Clone your forked repo to your PC, eg:
`git clone git@github.com:<your-github-account>/blurb-the-absurd.git`
SSH into your rpi as your newly created rpi user and clone the repo onto your rpi as well, in a new directory:
`mkdir ~/code`
`cd code`
`git clone git@github.com:<your-github-account>/blurb-the-absurd.git`

Run the *YET-TO-BE-CREATED* script that will setup rpi for github access
