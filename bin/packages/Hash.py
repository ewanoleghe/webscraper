#!/usr/bin/python3

import hashlib
import crcmod
import mmh3
import pydeep  # Replacing ssdeep with pydeep
import tlsh


class Hash(object):
    """docstring for Hash"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "{0}".format(self.name)

    def _get_hash_name(self):
        return self.name

    def _set_hash_name(self, name):
        self.p_hash_name = name

    def Calculate(self, string):
        if self.name == "md5":
            hash = hashlib.md5(string.encode('utf-8')).hexdigest()

        elif self.name == "sha1":
            hash = hashlib.sha1(string.encode('utf-8')).hexdigest()

        elif self.name == "crc":
            crc32 = crcmod.Crc(0x104c11db7, initCrc=0, xorOut=0xFFFFFFFF)
            crc32.update(string.encode('utf-8'))
            hash = crc32.hexdigest()

        elif self.name == "murmur":
            hash = mmh3.hash(string)

        elif self.name == "ssdeep":
            hash = pydeep.hash(string)  # Use pydeep for ssdeep

        elif self.name == "tlsh":
            hash = tlsh.hash(string)

        return hash
