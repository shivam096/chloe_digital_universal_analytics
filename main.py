from models import UAJob
from broadcast import broadcast


def main(request):
    data = request.get_json()
    print(data)

    if "broadcast" in data:
        results = broadcast(data)
    elif "view_id" in data and "broadcast" not in data:
        job = UAJob(
            headers=data["headers"],
            view_id=data["view_id"],
            website=data["website"],
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
