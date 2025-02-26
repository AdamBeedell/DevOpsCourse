### lesson 3 notes

def subtract2(a: int, b: int):
    return int((a-b))

print(subtract2(6,2))

print(subtract2(6,2,4))

print(subtract2("jeff",[]))




## import stuff
import random
import platform
import subprocess
import time


if platform.system() != "Windows":
    print("fail, not windows")
    exit()


## prep list
ips = []
unreachable = []
reached = []
shutdown_command_success_slash_should_be_shut_down = []
shutdown_command_failed = []
unreachable_after = []
reachable_after = []


for i in range(0,100):
    ip=(f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}")
    ips.append(ip)


## prep commands

def pingit(ip):
    #command = ['ping', ip]
    #result = (subprocess.call(command))
    print(f"Sent 4 pings to {ip}, assuming greater than 0 successes is success")
    return(random.choice([True, False]))

def shutdownmachine(ip):
    print(f"Sent Shutdown to {ip}")
    return(random.choice([True, False]))


## do stuff

for ip in ips:
    result = pingit(ip)
    if result == True:
        unreachable.append(ip)
    else:
        reached.append(ip)


print(f"reached {len(reached)}/{len(ips)}.")

for ip in reached:
    result = shutdownmachine(ip)
    if result == True:
        shutdown_command_success_slash_should_be_shut_down.append(ip)
    else: 
        shutdown_command_failed.append(ip)

print(f"sent a shutdown to {len(reached)} ips, of which {len(shutdown_command_failed)} failed.")

time.sleep(120)

for ip in shutdown_command_success_slash_should_be_shut_down:
    result = pingit(ip)
    if result == True:
        unreachable_after.append(ip)
    else: 
        reachable_after.append(ip)


print(f"{len(unreachable_after)} machines have been shut down, or have happened to go offline at the same time, {len(reachable_after)} failed and are still up.")


print("final results:")

print("input IPs")
print(ips)

print("unreachable IPs")
print(unreachable)

print("initially pingable IPs")
print(reached)

print("sent shutdown to these IPs")
print(shutdown_command_success_slash_should_be_shut_down)

print("shutdown command failed on these IPs")
print(shutdown_command_failed)

print("Appears to have shutdown IPs")
print(unreachable_after)

print("Machines which have refused to shut down, or been swiftly autorebooted")
print(reachable_after)

print(f"{len(unreachable_after)}/{len(ips)} shutdowns")
print(f"{len(reachable_after)}/{len(unreachable)+len(unreachable_after)} likely offline")


