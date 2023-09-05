#!/usr/bin/python3
# coding: utf-8
# Quick script I wrote for sorting and categorizing Shodan API
# keys 'borrowed' en masse from Github. 
# The reason for discerning between paid and unpaid keys, is we
# can do more with a paid key, so its best to not burn those on
# just blasting out queries all day erry day.
# 
# Forked and updated from: https://github.com/0x27/shodan_key_checker

import shodan
import sys
import crayons

def test(key):
    api = shodan.Shodan(key)
    print("{+} Testing Key: %s" %(key))
    try:
        info = api.info()
    except Exception:
        print(crayons.red(f"[-] Key {key} is invalid!"))
        return False,False
    if info['plan'] == 'dev' or info['plan'] == 'edu': #this seems to be how they are categorized
        print(crayons.green(f"[+] Key {key} appears to be valid, and bonus, paid!"))
        return True,True
    elif info['plan'] == 'oss': # however I might be wrong. oh well.
        print(crayons.cyan(f"[*] Key {key} appears to be valid! Not paid for though!"))
        return True,False


def main(args):
    if len(args) != 2:
        sys.exit("Shodan API Key List Checker (for testing githubbed keys)\nusage: %s keys-to-test.txt" %(args[0]))
    f = open(args[1], "r")
    keys = f.readlines()
    valid_keys = []
    paid_keys = []
    comm_keys = []
    for key in keys:
        key = key.strip()
        is_valid,is_paid = test(key=key)
        if is_valid == True:
            valid_keys.append(key)
            if is_paid == True:
                paid_keys.append(key)
            else:
                comm_keys.append(key)
        else:
            pass
    if len(valid_keys) > 0:
        print (f"\n\n[+] Acquired {len(valid_keys)} valid keys")
        print (crayons.green(f"[+] Acquired {len(paid_keys)} paid-keys"))
        print (crayons.cyan(f"[+] Acquired {len(comm_keys)} community-keys"))
        print ("\n{+} Paid Keys...")
        for key in paid_keys:
            print (key)
        print ("\n{+}Community Keys...")
        for key in comm_keys:
            print (key)
    else:
        print (f"\n\n[-] Zero valid keys acquired (._.)")


if __name__ == "__main__":
    main(args=sys.argv)
