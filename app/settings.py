# neural_network.py
MODEL_NAME = "all-MiniLM-L6-v2"

# tool.py
INVALID_ARGS_EXCEPTION = Exception("Invalid arguments\nEnsure command calls are in the form: cmd-find '[COMMAND DESCRIPTION]' [NUM OF SUGGESTED COMMANDS]")
DEFAULT_SUGGESTED_NUM = 3

# find_best.py
PROG_BAR_COMPLETE = "#"
PROG_BAR_INCOMPLETE = "~"
PROG_BAR_LENGTH = 50