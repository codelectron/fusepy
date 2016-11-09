#!/usr/bin/env python
# Example code for handling IOCTLs in FUSE client

import ctypes
import struct
from errno import ENOTTY
from ioctl_opt import IOWR

def ioctl(self, path, cmd, arg, fh, flags, data):
    M_IOWR = IOWR(ord('M'), 1, ctypes.c_uint32)
    if cmd == M_IOWR:
        inbuf = ctypes.create_string_buffer(4)
        ctypes.memmove(inbuf, data, 4)
        data_in = struct.unpack('<I', inbuf)[0]
        data_out = data_in + 1
        outbuf = struct.pack('<I', data_out)
        ctypes.memmove(data, outbuf, 4)
    else:
        raise FuseOSError(ENOTTY)
    return 0
