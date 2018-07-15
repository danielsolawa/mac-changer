#!/usr/bin/env python

import subprocess
import optparse
import re


def get_options():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="The name of the interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please specify an interface. Use -h for more info.")

    if not options.new_mac:
        parser.error("[-] Please specify mac address. Use -h for more info.")

    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    # subprocess.call("ifconfig " + interface + " down", shell=True)
    # subprocess.call("ifconfig " + interface + "  hw ether " + new_mac, shell=True)
    # subprocess.call("ifconfig " + interface + " up", shell=True)
    # subprocess.call("ifconfig", shell=True)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    #subprocess.call(["ifconfig"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_match = re.search(r"\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}", ifconfig_result)

    if mac_address_match:
        return mac_address_match.group(0)
    else:
        print("[-] Could not read MAC address")


def match_mac(new_mac, current):
    if new_mac == current:
        print("[+] MAC address has been changed properly.")
    else:
        print("[-] MAC did not change. Please try again.")


options = get_options()
current_mac = get_current_mac(options.interface)
print("Current MAC address = " + str(current_mac))
change_mac(options.interface, options.new_mac)
match_mac(options.new_mac, get_current_mac(options.interface))



