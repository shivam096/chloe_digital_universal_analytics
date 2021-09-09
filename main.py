import base64
import json

from models import UAJob
from broadcast import broadcast


def main(request):
    request_json = request.get_json()
    message = request_json["message"]
    data_bytes = message["data"]
    data = json.loads(base64.b64decode(data_bytes).decode("utf-8"))
    print(data)

    if "broadcast" in data:
        results = broadcast(data)
    elif "view_id" in data and "broadcast" not in data:
        job = UAJob(
            headers=data["headers"],
            view_id=data["view_id"],
            principal_content_type=data["principal_content_type"],
            start=data.get("start"),
            end=data.get("end"),
        )
        results = job.run()
    else:
        raise NotImplementedError(data)

    response = {
        "pipelines": "GA",
        "results": results,
    }
    print(response)
    return response
