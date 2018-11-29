import json
import io

def formatadorOPML(itemValida, pai, opmlSaida):
    for i in itemValida:
        if(not isinstance(i, dict)):
            if isinstance(itemValida[i], dict):
                opmlSaida.write(pai + "<outline text=\"" + str(i) + "\" >\r\n")
                formatadorOPML(itemValida[i], pai + "\t", opmlSaida)
                opmlSaida.write(pai + "</outline>\r\n")
            else:
                if isinstance(itemValida[i], list):
                    formatadorOPML(itemValida[i], pai + "\t", opmlSaida)
                else:
                    opmlSaida.write(pai + "<outline text=\"" + str(i) + " " + str(itemValida[i]) + "\" >\r\n")
                    opmlSaida.write(pai + "</outline>\r\n")
        else:
            objectItem = "<outline "
            textItem = ""
            uuidItem = ""
            for j in i.keys():
                if(not isinstance(i[j], list)):
                    if(j == 'uuid'):
                        if(not isinstance(i[j], float)):
                            uuidItem = j + "=\"" + i[j].replace("\"", "'") + "\" "
                        else:
                            uuidItem = j + "=\"" + str(i[j]) + "\" "
                    else:
                        if(not isinstance(i[j], dict)):
                            if (not isinstance(i[j], float)):
                                textItem = textItem + " " + i[j].replace("\"", "'")
                            else:
                                textItem = textItem + " " + str(i[j])
                        else:
                            formatadorOPML(i[j], pai + "\t", opmlSaida)

            objectItem = objectItem + "text=\"" + textItem + "\" " + uuidItem + "> \r\n"
            # print objectItem

            ##################### GERNERATE COMPLETE OPML ####################
            opmlSaida.write(pai + str(objectItem))
            for a in i.keys():
                if isinstance(i[a], dict):
                    formatadorOPML(i[a], pai + "\t", opmlSaida)
                else:
                    if isinstance(i[a], list):
                        formatadorOPML(i[a], pai + "\t", opmlSaida)
            opmlSaida.write(pai + "</outline> \r\n")
            ##################### END OF COMPLETE OPML ######################


def geradorOPML(jsonFileName, opmlFileName, title):
    OPML_HEADER = """<?xml version="1.0" encoding="UTF-8"?>
    <opml version="2.0">
        <head>
            <title>""" + str(title) + """</title>
        </head>
    <body>
"""
    OPML_FOOTER = """</body>
</opml>
"""
    jsonObject = json.load(open(jsonFileName))
    opmlSaida = io.open(opmlFileName, "w", encoding='utf8')
    opmlSaida.write(OPML_HEADER)
    formatadorOPML(jsonObject, "\t\t", opmlSaida)
    opmlSaida.write(OPML_FOOTER)