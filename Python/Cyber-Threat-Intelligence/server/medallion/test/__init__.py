# Medallion TAXII endpoints
DISCOVERY_EP = "/taxii2/"
API_ROOT_EP = "/trustgroup1/"  # there are other API roots, but this is the one used in tests

COLLECTIONS_EP = API_ROOT_EP + "collections/"
GET_COLLECTION_EP = COLLECTIONS_EP + "91a7b528-80eb-42ed-a74d-c6fbd5a26116/"
ADD_COLLECTION_EP = COLLECTIONS_EP + "365fed99-08fa-fdcd-a1b3-fb247eb41d01/"
NON_EXISTENT_COLLECTION_EP = COLLECTIONS_EP + "12345678-1234-1234-1234-123456789012/"
FORBIDDEN_COLLECTION_EP = COLLECTIONS_EP + "64993447-4d7e-4f70-b94d-d7f33742ee63/"
EMPTY_COLLECTION_EP = COLLECTIONS_EP + "472c94ae-3113-4e3e-a4dd-a9f4ac7471d4/"

ADD_OBJECTS_EP = ADD_COLLECTION_EP + "objects/"
ADD_MANIFESTS_EP = ADD_COLLECTION_EP + "manifest/"

GET_MANIFESTS_EP = GET_COLLECTION_EP + "manifest/"
GET_OBJECTS_EP = GET_COLLECTION_EP + "objects/"