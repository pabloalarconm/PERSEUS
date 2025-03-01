from embuilder.builder import EMB

prefixes = dict(
  rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#" ,
  rdfs = "http://www.w3.org/2000/01/rdf-schema#" ,
  obo = "http://purl.obolibrary.org/obo/" ,
  sio = "http://semanticscience.org/resource/" ,
  xsd = "http://www.w3.org/2001/XMLSchema#",
  this = "http://my_example.com/")


triplets = [

    ####################### Personal Information ######################################

# Nodes
["this:$(pid)_ID","sio:SIO_000020","this:$(pid)_$(uniqid)_Birthdate_Role","iri"],
["this:$(pid)_Entity","sio:SIO_000228","this:$(pid)_$(uniqid)_Birthdate_Role","iri"],
["this:$(pid)_Entity","sio:SIO_000008","this:$(pid)_$(uniqid)_Birthdate_Attribute","iri"],
["this:$(pid)_$(uniqid)_Birthdate_Role","sio:SIO_000356","this:$(pid)_$(uniqid)_Birthdate_Process","iri"],
["this:$(pid)_$(uniqid)_Birthdate_Process","sio:SIO_000229","this:$(pid)_$(uniqid)_Birthdate_Output","iri"],
["this:$(pid)_$(uniqid)_Birthdate_Output","sio:SIO_000628","this:$(pid)_$(uniqid)_Birthdate_Attribute","iri"],

["this:$(pid)_ID","sio:SIO_000020","this:$(pid)_$(uniqid)_Sex_Role","iri"],
["this:$(pid)_Entity","sio:SIO_000228","this:$(pid)_$(uniqid)_Sex_Role","iri"],
["this:$(pid)_Entity","sio:SIO_000008","this:$(pid)_$(uniqid)_Sex_Attribute","iri"],
["this:$(pid)_$(uniqid)_Sex_Role","sio:SIO_000356","this:$(pid)_$(uniqid)_Sex_Process","iri"],
["this:$(pid)_$(uniqid)_Sex_Process","sio:SIO_000229","this:$(pid)_$(uniqid)_Sex_Output","iri"],
["this:$(pid)_$(uniqid)_Sex_Output","sio:SIO_000628","this:$(pid)_$(uniqid)_Sex_Attribute","iri"],

# Types
["this:$(pid)_ID","rdf:type","sio:SIO_000115","iri"],
["this:$(pid)_Entity","rdf:type","sio:SIO_000498","iri"],
["this:$(pid)_$(uniqid)_Birthdate_Role","rdf:type","sio:SIO_000016","iri"],
["this:$(pid)_$(uniqid)_Birthdate_Role","rdf:type","obo:OBI_0000093","iri"],
["this:$(pid)_$(uniqid)_Birthdate_Process","rdf:type","sio:SIO_000006","iri"],
["this:$(pid)_$(uniqid)_Birthdate_Output","rdf:type","sio:SIO_000015","iri"],
["this:$(pid)_$(uniqid)_Birthdate_Attribute","rdf:type","sio:SIO_000614","iri"],
["this:$(pid)_$(uniqid)_Birthdate_Attribute","rdf:type","obo:NCIT_C68615","iri"],

["this:$(pid)_$(uniqid)_Sex_Role","rdf:type","sio:SIO_000016","iri"],
["this:$(pid)_$(uniqid)_Sex_Role","rdf:type","obo:OBI_0000093","iri"],
["this:$(pid)_$(uniqid)_Sex_Process","rdf:type","sio:SIO_000006","iri"],
["this:$(pid)_$(uniqid)_Sex_Output","rdf:type","sio:SIO_000015","iri"],
["this:$(pid)_$(uniqid)_Sex_Attribute","rdf:type","sio:SIO_000614","iri"],
["this:$(pid)_$(uniqid)_Sex_Attribute","rdf:type","$(sexURI)","iri"],
["this:$(pid)_$(uniqid)_Sex_Attribute","rdf:type","obo:NCIT_C28421","iri"],

# Labels
["this:$(pid)_$(uniqid)_Birthdate_Role","rdfs:label","Role: Patient for age assessment","xsd:string"],
["this:$(pid)_$(uniqid)_Birthdate_Process","rdfs:label","Process: age measuring process","xsd:string"],
["this:$(pid)_$(uniqid)_Birthdate_Output","rdfs:label","Output type: Birth date","xsd:string"],
["this:$(pid)_$(uniqid)_Birthdate_Attribute","rdfs:label","Attribute type: Birth date","xsd:string"],
["this:$(pid)_$(uniqid)_Sex_Role","rdfs:label","Role: Patient for gender assessment","xsd:string"],
["this:$(pid)_$(uniqid)_Sex_Process","rdfs:label","Process: sex measuring process","xsd:string"],
["this:$(pid)_$(uniqid)_Sex_Output","rdfs:label","Output type: $(sexLabel)","xsd:string"],
["this:$(pid)_$(uniqid)_Sex_Attribute","rdfs:label","Attribute type: $(sexLabel)","xsd:string"],

# Values
["this:$(pid)_ID","sio:SIO_000300","$(pid)","xsd:string"],
["this:$(pid)_$(uniqid)_Birthdate_Output","sio:SIO_000300","$(birthdate)","xsd:date"],
["this:$(pid)_$(uniqid)_Sex_Output","sio:SIO_000300","$(sexLabel)","xsd:string"],

    ############################ Diagnosis ##############################################

["this:$(pid)_ID","sio:SIO_000020","this:$(pid)_$(uniqid)_Diagnosis_Role","iri"],
["this:$(pid)_Entity","sio:SIO_000228","this:$(pid)_$(uniqid)_Diagnosis_Role","iri"],
["this:$(pid)_Entity","sio:SIO_000008","this:$(pid)_$(uniqid)_Diagnosis_Attribute","iri"],
["this:$(pid)_$(uniqid)_Diagnosis_Role","sio:SIO_000356","this:$(pid)_$(uniqid)_Diagnosis_Process","iri"],
["this:$(pid)_$(uniqid)_Diagnosis_Process","sio:SIO_000680","this:$(pid)_$(uniqid)_Diagnosis_Startdate","iri"],
["this:$(pid)_$(uniqid)_Diagnosis_Process","sio:SIO_000681","this:$(pid)_$(uniqid)_Diagnosis_Enddate","iri"],
["this:$(pid)_$(uniqid)_Diagnosis_Process","sio:SIO_000229","this:$(pid)_$(uniqid)_Diagnosis_Output","iri"],
["this:$(pid)_$(uniqid)_Diagnosis_Output","sio:SIO_000628","this:$(pid)_$(uniqid)_Diagnosis_Attribute","iri"],

# Types
#["this:$(pid)_ID","rdf:type","sio:SIO_000115","iri"],
#["this:$(pid)_Entity","rdf:type","sio:SIO_000498","iri"],
["this:$(pid)_$(uniqid)_Diagnosis_Role","rdf:type","sio:SIO_000016","iri"],
["this:$(pid)_$(uniqid)_Diagnosis_Role","rdf:type","obo:OBI_0000093","iri"],
["this:$(pid)_$(uniqid)_Diagnosis_Process","rdf:type","sio:SIO_000006","iri"],
["this:$(pid)_$(uniqid)_Diagnosis_Process","rdf:type","sio:SIO_001001","iri"],
["this:$(pid)_$(uniqid)_Diagnosis_Startdate","rdf:type","sio:SIO_000031","iri"],
["this:$(pid)_$(uniqid)_Diagnosis_Enddate","rdf:type","sio:SIO_000032","iri"],
["this:$(pid)_$(uniqid)_Diagnosis_Output","rdf:type","sio:SIO_000015","iri"],
["this:$(pid)_$(uniqid)_Diagnosis_Output","rdf:type","sio:SIO_001003","iri"],
["this:$(pid)_$(uniqid)_Diagnosis_Attribute","rdf:type","sio:SIO_000614","iri"],
["this:$(pid)_$(uniqid)_Diagnosis_Attribute","rdf:type","$(ordo_uri)","iri"],

# Labels
["this:$(pid)_$(uniqid)_Diagnosis_Role","rdfs:label","Role: Diagnosis patient","xsd:string"],
["this:$(pid)_$(uniqid)_Diagnosis_Process","rdfs:label","Process: Medical diagnosis","xsd:string"],
["this:$(pid)_$(uniqid)_Diagnosis_Startdate","rdfs:label","Startdate: $(date)","xsd:string"],
["this:$(pid)_$(uniqid)_Diagnosis_Enddate","rdfs:label","Enddate: $(date)","xsd:string"],
["this:$(pid)_$(uniqid)_Diagnosis_Output","rdfs:label","Output type: Diagnosis","xsd:string"],
["this:$(pid)_$(uniqid)_Diagnosis_Attribute","rdfs:label","Attribute type: $(diagnostic_opinion)","xsd:string"],

# Values
#["this:$(pid)_ID","sio:SIO_000300","$(pid)","xsd:string"],
["this:$(pid)_$(uniqid)_Diagnosis_Startdate","sio:SIO_000300","$(date)","xsd:date"],
["this:$(pid)_$(uniqid)_Diagnosis_Enddate","sio:SIO_000300","$(date)","xsd:date"],
["this:$(pid)_$(uniqid)_Diagnosis_Output","sio:SIO_000300","$(diagnostic_opinion)","xsd:string"]


]

config = dict(
  source_name = "source_cde_test",
  configuration = "ejp",    # Two options for this parameter:
                            # ejp: it defines CDE-in-a-Box references, being compatible with this workflow  
                            # csv: No workflow defined, set the source configuration for been used by CSV as data source
                            
  csv_name = "source_1", # parameter only needed in case you pick "csv" as configuration
  basicURI = "this"
)

builder = EMB(config, prefixes, triplets)
test = builder.transform_SPARQL()
print(test)