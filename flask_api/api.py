import json

from flask import Flask, request
from flask_restful import Resource, Api

from helper import get_temp_varies

app = Flask(__name__)
api = Api(app)


class GenerateHeatMap(Resource):
    def post(self):

        obj = json.dumps(request.data.decode("utf-8"), indent=4)
        req = json.loads(obj)
        json_data = json.loads(req)

        map_gen = get_temp_varies(
            Density=json_data["density"],
            Specific_heat=json_data["specific_heat"],
            Heat_conductivity_of_walls=json_data["heat_conductivity"],
            Initial_Temperature=json_data["init_temp"],
            Length=json_data["length"],
            Breadth=json_data["breadth"],
            Height=json_data["height"],
            Number_of_hours_to_run_simulation=json_data["num_hours"],
            heatmap_file_path=json_data["image_path"],
        )
        response = {
            "image_path": json_data["image_path"],
            "map_generated": str(map_gen),
        }
        return response, 200


api.add_resource(GenerateHeatMap, "/generate_heat_map")


if __name__ == "__main__":
    app.run(port="8080")
