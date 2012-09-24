#
# Do not change this file directly.
# Import in as the first module change it imperatively.
#

#
# 0 - no randomization
# 1 - mild randomization (no change, first char, none)
# 2 - full randomization (none, arbitrary startstring)

READLINE_LEVEL = 0
READALL_LEVEL = 0
READCHAR_LEVEL = 0

#
# 0 - send message/connect always succeeds
# 1 - send message/connect may fail

WRITE_LEVEL = 0
CONNECT_LEVEL = 0

#
# 0 - no fail
# 1 - response 500
# 2 - random response (1xx, 2xx, 3xx)

SERVER_LEVEL = 2
