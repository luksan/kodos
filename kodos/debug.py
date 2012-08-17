#  debug.py: -*- Python -*-  DESCRIPTIVE TEXT.

################################# DEBUGGING CONSTANTS ######################################

# debugging constants ... set debug to one of these
# if adding new debug levels make sure the new ones are
# a unique power of 2 (1, 2, 4, 8, 16...). Also, the new
# ones should be added to DEBUG_ALL
DEBUG_NONE          = 0
DEBUG_AUTO_COMPLETE = 1
DEBUG_ANIMATE       = 2
DEBUG_CONNECT       = 4
DEBUG_SESSION       = 8
DEBUG_PIXMAP        = 16
DEBUG_HISTORY       = 32
DEBUG_SSTM          = 64
DEBUG_MISC          = 128
DEBUG_CMDLINE_ARGS  = 256
DEBUG_PRINT         = 512
DEBUG_PREFS         = 1024
DEBUG_PS_TPL        = 2048

# convenience constant
DEBUG_ALL  = (
    DEBUG_AUTO_COMPLETE | DEBUG_ANIMATE |
    DEBUG_CONNECT | DEBUG_SESSION |
    DEBUG_PIXMAP | DEBUG_HISTORY |
    DEBUG_SSTM | DEBUG_MISC | DEBUG_CMDLINE_ARGS |
    DEBUG_PRINT | DEBUG_PREFS | DEBUG_PS_TPL
    )

# use a bitwise or (|) to use multiple debug levels
# debug = DEBUG_AUTO_COMPLETE | DEBUG_SESSION
debug = DEBUG_NONE
