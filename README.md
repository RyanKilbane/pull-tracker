# Pull Tracker

This is a simple Python (and at some point React) app that will keep track of pull requests for individuals and groups.

# Inital Setup
The first run of this script will look for a file (setup.yml), if the programme doesn't find it then the setput.py script will run. This is just to setup the database tables and add the git token. Speaking of which, you'll need a Git api key.

# Future Improvements
There are a couple of improvements that I'm hoping to add:
* React.js: I'm really hoping that adding React will help me make the UI no longer look like it comes out of the 90s
* Slack integration: I'm hoping to add a thin wrapper around the Slack API to make integration with arbitary Slack bots easy.
* Team management: This is already in progress, but I want to be able to have what is basically a mailing list. This links into the above.