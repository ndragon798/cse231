from proj07 import read_file

fp = open("small_network_data.txt")
network = read_file(fp)
print("network:")
print(network)
print(20*"-")
print("network printed nicely:")
for i, L in enumerate(network):
    print(i,":",L)
