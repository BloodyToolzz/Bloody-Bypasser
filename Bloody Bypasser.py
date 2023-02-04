# Original Creator: WTSTiNy
# Revamped by Bloody

import requests, os, time

from pystyle import Write, Colors
from os import system as breh
from console.utils import set_title

sup_links = """
Ad links:
linkvertise.com (all of their domains)
adf.ly (all of their domains)
exe.io/exey.io/exee.io/exe.app/eio.io
ouo.io/ouo.press
adfoc.us
ay.live
bc.vc/bcvc.live
fc.lc/fc-lc.com
za.gl/za.uy/zee.gl
freehottip.com
ph.apps2app.com
gestyy.com
shortconnect.com
shorte.st/sh.st
aylink.co

Socials:
sub2get.com
sub2unlock.net/sub2unlock.com
rekonise.com
letsboost.net
mboost.me
sub4unlock.com
ytsubme.com
steps2unlock.com
social-unlock.com
boost.ink
boostme.link/boost.fusedgt.com

Shorteners:
bit.ly/bitly.com
cutt.ly
shrto.ml
goo.gl
t.co
tinyurl.com
onlyme.ga

Redirects:
youtube.com
justpaste.it
"""

def cls():
  breh('cls' if os.name == 'nt' else 'clear')

def pause():
  breh('pause <nul')

def bypass():
  cls()
  set_title("Bloody Bypasser | Made By: WTSTiNy | Revamped By: Bloody | Main")
  Write.Print("[1] Bypass One URL\n", Colors.purple_to_blue, interval=0) 
  Write.Print("[2] Bypass Multiple URLs\n", Colors.purple_to_blue, interval=0)
  Write.Print("[3] Supported Links\n", Colors.purple_to_blue, interval=0)
  Write.Print("[3] Exit\n\n", Colors.red_to_yellow, interval=0)
  o = Write.Input("[+] Choice: ", Colors.purple_to_blue, interval=0)
  cls()
  if o == "1":
    set_title("Bloody Bypasser | Made By: WTSTiNy | Revamped By: Bloody | Enter URL")
    url = Write.Input("[+] Enter URL to Bypass: ", Colors.red_to_yellow, interval=0)
    print()
    payload = {"url": url}
    url_bypass = requests.post("https://api.bypass.vip/", data=payload)
    bypassed = url_bypass.json()
    haram = bypassed["destination"]
    Write.Print(f"Bypassed URL: {haram}\n", Colors.green_to_white, interval=0)
    time.sleep(60)
    try:
      open("bypassed.txt", "x")
    except FileExistsError:
      pass
      bypassed_url = open("bypassed.txt", "a")
    try:
        bypassed_url.write(bypassed["destination"] + "\n")
    except KeyError:
        Write.Print("[-] Invalid URL Found", Colors.red_to_yellow, interval=0)
        pause()
        pass

  elif o == "2":
    set_title("Bloody Bypasser | Made By: WTSTiNy | Revamped By: Bloody | Enter File With URLs")
    urls_file = Write.Print("""Bypassing Links in "urls.txt"\n\n""", Colors.red_to_yellow, interval=0)
    urls = open("urls.txt", "r")
    for i in urls:
      url_bypass = {"url": i}
      Write.Print((f"[-] URL: {url_bypass}" + ""), Colors.red_to_yellow, interval=0)
      bypass = requests.post("https://api.bypass.vip/", data=url_bypass)
      bypassed = bypass.json()
      halal = bypassed["destination"]
      try:
        open("bypassed.txt", "x")
      except FileExistsError:
        pass
      bypassed_url = open("bypassed.txt", "a")
      try:
        Write.Print((f"[+] Bypassed URL: {halal}\n"), Colors.green_to_white, interval=0)
        bypassed_url.write(bypassed["destination"] + "\n")
      except KeyError:
        Write.Print("[-] Invalid URL Found", Colors.red_to_yellow, interval=0)
        pass

  elif o == "3":
    Write.Print("Supported Links:\n", Colors.purple_to_blue, interval=0.008)
    Write.Print(f"{sup_links}\n", Colors.green_to_white, interval=0.000000000000000000000000000000000000000000000000000001)
    try:
      f = open("Supported Links.txt", "w")
      f.write(f"{sup_links}")
      Write.Print("Written links to Supported Links.txt", Colors.purple_to_blue, interval=0.008)
    finally:
      pass

  elif o == "4":
    os.system("exit")

if __name__ == "__main__":
  bypass()

# Original: https://github.com/WTSTiNy/URL-Bypasser