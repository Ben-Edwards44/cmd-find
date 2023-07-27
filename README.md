# cmd-find

cmd-find is a command line tool that finds linux commands from their descriptions.


# Installation

Use pip to install cmd-find by running the following command:

    pip install cmd-find


# Usage

Run the `cmd-find` command followed by a description enclosed in single or double quotes to use the tool.

An example would look like this:

    cmd-find "change the current working directory"

Using single quotes is also allowed:

    cmd-find 'change the current working directory'

# Help

## The command takes too long

The command takes a long time to run **when it is first used**. This is because the transformer model used needs to be downloaded.

After the first use, the command will be much faster because the model will have been cached.

## An incorrect command is outputted

cmd-find works better if short descriptions that directly describe what a command does are used.

- Use `cmd-find "list all files in a directory"`
- Do not use `cmd-find "I want a command that lists the files in a directory"`

cmd-find can only find commands within **page 1** of the [Linux man pages](https://github.com/mkerrisk/man-pages) or those covered by the `help` command.

If the command you are looking for is not within this list, it will not be found by the tool.

## Installation failed

Ensure that both python and pip are installed. 

Run `pip --version` and `python3 --version` to check that they are both installed.

Ensure that you are connected to the internet and run

    pip install cmd-find

## The command results in an error

Ensure that the given description is enclosed within either single or double quotes:

- `cmd-find "create a new directory"` is correct.
- `cmd-find 'create a new directory'` is also correct.
- `cmd-find create a new directory` is incorrect.