class Solution:
    def interpret(self, command: str) -> str:
        d=[]
        for i in range(len(command)):
            if command[i]=="G":
                d.append("G")
            elif command[i]=="(" and command[i+1]==")":
                d.append("o")
            elif command[i]=="(" and command[i+1]=="a":
                d.append("al")
            else:
                continue
        return "".join(d)