from embuilder.builder import EMB

prefixes = dict(
  rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#" ,
  rdfs = "http://www.w3.org/2000/01/rdf-schema#" ,
  obo = "http://purl.obolibrary.org/obo/" ,
  sio = "http://semanticscience.org/resource/" ,
  xsd = "http://www.w3.org/2001/XMLSchema#",
  biolink = "https://w3id.org/biolink/vocab/",
  this = "http://my_example1.com/")


triplets = [

# Nodes
["this:$(pid)_$(uniqid)#ID","sio:denotes","this:$(pid)_$(uniqid)#Role","iri"],
["this:$(pid)_$(uniqid)#Entity","sio:has-role","this:$(pid)_$(uniqid)#Role","iri"],

# Types
["this:$(pid)_$(uniqid)#ID","rdf:type","sio:SIO_000115","iri"],
["this:$(pid)_$(uniqid)#Entity","rdf:type","sio:SIO_000498","iri"],
["this:$(pid)_$(uniqid)#Role","rdf:type","obo:OBI_0000093","iri"],

# Biolink types
["this:$(pid)_$(uniqid)#Entity","rdf:type","biolink:Case","iri"],
["this:$(pid)_$(uniqid)#ID","rdf:type","biolink:ID","iri"],


# Values
["this:$(pid)_$(uniqid)#ID","sio:SIO_000300","$(pid2)","xsd:string"]]

config = dict(
  source_name = "source_cde_test",
  configuration = "ejp",    # Two options for this parameter:
                            # ejp: it defines CDE-in-a-Box references, being compatible with this workflow  
                            # csv: No workflow defined, set the source configuration for been used by CSV as data source
                            
  csv_name = "source_1" # parameter only needed in case you pick "csv" as configuration
)

builder = EMB(config, prefixes, triplets)
test = builder.transform_YARRRML()
print(test)