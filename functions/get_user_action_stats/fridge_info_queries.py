
from __future__ import annotations

import logging
from boto3.dynamodb.types import TypeDeserializer

log = logging.getLogger(__name__)

_deserializer = TypeDeserializer()

def return_fridge_report_notes(client, table_name: str) -> dict | None:

    

    """return fridge report notes in a dictionary for pagination .



    
    Returns the deserialised item, or None if not found.
    """
    response = client.scan(
        TableName=table_name,
    )
    # getting the items in the userpointshistory table
    items = response.get("Item")
    results = []
    #parsing through each for the fridgeid, timestamp, and note. 
    for item in items: 
        deserializedItem = _from_dynamo_item(item)
        newReport = deserializedItem.get("newReport", {})
        results.append({"fridgeId": newReport.get("fridgeId"), "epochTimeStamp": newReport.get("epochTimestamp"), "note": newReport.get("note")})

    return {
        "items": results, 
        "lastEvaluatedKey": response.get("LastEvaluatedKey")
    }