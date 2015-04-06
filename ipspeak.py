#!/usr/bin/python3

import socket
import fcntl
import struct
import subprocess
import os

def get_ip(ifname):
	try:

		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		return socket.inet_ntoa(
			fcntl.ioctl(
				sock.fileno(), 
				0x8915, #SIOCGIFADDR
				struct.pack('256s', bytes(ifname[:15], 'utf-8'))
			)[20:24])

	except IOError:
		return "NODEV"
	except:
		return "ERROR"

def play(number):
	FNULL = open(os.devnull, 'w')
	player = subprocess.Popen(["aplay", number], stdout=FNULL, stderr=FNULL)
	player.wait()
	
def numberize(ip):
	for i in range(0, len(ip)):
		if ip[i] == "0":
			play("zero.wav")
		
		if ip[i] == "1":
			play("one.wav")

		if ip[i] == "2":
			play("two.wav")

		if ip[i] == "3":
			play("three.wav")

		if ip[i] == "4":
			play("four.wav")

		if ip[i] == "5":
			play("five.wav")

		if ip[i] == "6":
			play("six.wav")

		if ip[i] == "7":
			play("seven.wav")

		if ip[i] == "8":
			play("eight.wav")

		if ip[i] == "9":
			play("nine.wav")

		if ip[i] == ".":
			play("dot.wav")

if __name__ == "__main__":

	play("ethernet.wav")
	ip = get_ip("eth0")
	if ip == "NODEV":
		play("noip.wav")
	if ip == "ERROR":
		play("error.wav")
		quit(1)
	else: 
		numberize(ip)


	play("wireless.wav")
	ip = get_ip("wlp2s0")
	if ip == "NODEV":
		play("noip.wav")
	if ip == "ERROR":
		play("error.wav")
		quit(1)
	else: 
		numberize(ip)

