import json
from fastapi import APIRouter, UploadFile
from rules import rules

router = APIRouter()

@router.get("/admin/rules")
def get_rules() -> dict:
    return rules.get_rules()

@router.put("/admin/rules")
async def update_rules(rules_file: UploadFile) -> dict:
    try:
        rules.update_rules(json.load(rules_file.file))
    except Exception as e:
        message = f"Error occured while importing rules. Error message: {e}"
        print(message)
        raise Exception(message)
    
    return {"message" : "Updated rules succesfully"}
