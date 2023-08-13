def mf_parser():
    with open("./file.fin", "r") as finfile:
        lines = finfile.read()

    for line in lines.split("\n"):
        print(line.split("=")[1])
              
if __name__ == "__main__":
    mf_parser()
