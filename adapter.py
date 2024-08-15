"""The Adapter design pattern is a structural pattern that allows objects with 
        incompatible interfaces to work together. 
    Purpose:
        1. Converts the interface of a class into another interface that clients expect.
        2. Enables classes to work together that couldn't otherwise due to incompatible interfaces.
"""

# Existing class (Adaptee)
class XMLData:
    def getXML(self):
        return "<data> Example </data> "

#Target interface
class JSONData:
    def getJSON(self):
        pass

#Adapter class
class XMLToJSONAdapter(JSONData):
    def __init__(self, xml_data):
        self.xml_data = xml_data
    def getJSON(self):
        xml = self.xml_data.getXML()
        json_data = {"item": "Example"} #Simplified Example
        return json_data

#Client Code 
xml_data = XMLData()
adapter = XMLToJSONAdapter(xml_data)
json_data = adapter.getJSON()
print(json_data)

"""
This code showcases:

1. XMLData (Adaptee): The existing class that provides XML data.
2. JSONData (Target Interface): The interface that the client expects to work with.
3. XMLToJSONAdapter (Adapter): The class that adapts XMLData to the JSONData interface.
4. Client code that uses the adapter to get JSON data from an XML source.


Benefits:
Increases reusability of existing code
Improves interoperability between different systems
Provides a way to retrofit legacy code to work with new systems
"""