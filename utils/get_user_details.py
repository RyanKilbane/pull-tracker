def get_user_details(revewer_json):
    try:
        users = revewer_json["users"]
    except KeyError:
        return {"reviewer": None}
    output_json = []
    for user in users:
        output_json.append({"reviewer": user["login"], "avatar": user["avatar_url"]})
    return output_json
