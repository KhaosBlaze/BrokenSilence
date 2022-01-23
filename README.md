# BrokenSilence
Breaks up silence with random noises. Commands use the '&' prefix for commands.

Commands:

Ping
    Testing messaging functionality, added custom messages for myself and friend

Fard (arg1, arg2)
    Command will have bot join same vc channel as command user. Will return error if user not in voice. Will default to
    playing sound on loop every 10 minutes, if no arguments are provided. Can be supplied with two arguments for minimum
    and maximum time, command will sort times if out of order. May provide 'm' or 's' to specify time length, assumes
    seconds if neither are given.

Annoy (arg1, arg2)
    Command will have bot repeatedly wait to join and play sound to then disconnect. Arguments are used for timing in the
    same manner as Fard.

Bai
    Command will disconnect bot from VC.

Dependencies:
PyNaCl
Discord.py

ffmepg
