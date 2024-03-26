def getnames(cur):
    head = ""
    cols = list(c for c in cur.description)
    for c in cols:
        si = str(c).find("name=") + 6
        ei = str(c).find("',")
        head += str(c)[si:ei] + " "
    return head