# Recreating WUPHF from The Office
Recreating Ryan's idea - wuphf.com - from The Office.

## Architecture & Notes
This project uses a remote server and a locally running client to handle different connections.

The remote server accepts incoming WUPHFs and makes API calls to Twilio and other cloud-based platforms, while the client runs on the user's desktop and handles things like printing, text to speech, and general messages.

The remove server is django-based (which is almost certainly overkill), and uses postgres as a backend. It's deployed on a kubernetes cluster - but you can simplify it and use anything you like. Really, the database isn't even needed.
