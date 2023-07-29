# cmd-find

cmd-find is a command line tool that finds linux commands from their descriptions.


# Installation

Use pip to install cmd-find by running the following command:

    pip install cmd-find


# Usage

## Normal command calls

Run the `cmd-find` command followed by a description enclosed in single or double quotes and the number of suggested commands.

The tool should be used in the following way:

    cmd-find [NUM OF SUGGESTED COMMANDS] [COMMAND DESCRIPTION]

An example would look like this:

    cmd-find 2 "change the current working directory"

An example output of this command would look like this:

    Best choice:
    Command name: cd
    Description: change the shell working directory
    Enter 'help cd' to get more information
    
    Other suggestions:
    Command name: git-stash
    Description: stash the changes in a dirty working directory away
    Enter 'man git-stash' to get more information


## Alternative command calls

Using single quotes or swapping the positions of the two arguments is also allowed:

    cmd-find 'change the current working directory' 2

If the number of suggested commands is not specified, its default value is 3.

The following command would result in 3 suggested commands:

    cmd-find "change the current working directory"

# Help

## The command takes too long

The command takes a long time to run **when it is first used**. This is because the transformer model used needs to be downloaded.

After the first use, the command will be much faster because the model will have been cached.

## An incorrect command is outputted

cmd-find works better if short descriptions that directly describe what a command does are used.

- Use `cmd-find 3 "list all files in a directory"`
- Do not use `cmd-find 3 "I want a command that lists the files in a directory"`

cmd-find can only find commands within **page 1** of the [Linux man pages](https://github.com/mkerrisk/man-pages) or those covered by the `help` command.

If the command you are looking for is not within this list, it will not be found by the tool.

The tool can also only output commands once at a time. If the task you are trying to achieve requires multiple different commands to be exectued, these will not all be found by the tool.

## Installation failed

### Check pip and python

Ensure that both python and pip are installed. 

Run `pip --version` and `python3 --version` to check that they are both installed.

Ensure that both of the above commands execute successfully and that you are connected to the internet. If this is the case, retry the installation.

If python and pip are both installed and the installation still fails, try the following commands:

    pip3 install cmd-find

    python3 -m pip install cmd-find

    python -m pip install cmd-find

### Manually install dependencies

If the installation still fails, you can try and manually install the dependencies by running the following commands:

    pip install numpy
    pip install sentence-transformers

If you are trying to install onto something like a raspberry pi, ensure you have a **64-bit** OS installed. This is required for the `sentence-transformers` library.

## The command results in an error

Ensure that the given description is enclosed within either single or double quotes:

- `cmd-find 3 "create a new directory"` is correct.
- `cmd-find 3 'create a new directory'` is also correct.
- `cmd-find 3 create a new directory` is incorrect.