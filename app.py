from flask import Flask, jsonify, request
from data_preparation import create_json_response
import re

from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from

#Create flask obj
app = Flask(__name__)
app.json_encoder = LazyJSONEncoder

title = str(LazyString(lambda: 'API Documentation for Data processing dan Modelling'))
version = str(LazyString(lambda: '1.0.0'))
description = str(LazyString(lambda: 'Dokumentasi API untuk data processing dan Modelling'))
host = LazyString(lambda: request.host)

#Create swagger template
#swagger_template = { 'info':{'title' : title,
#							'version': version,
#							'description': description
#						 	},
#					 'host': host
#					}

swagger_config = {
	"headers":[],
	"specs": [{"endpoint":"docs", "route": '/docs.json'}],
	"static_url_path":"/flasgger_static",
	"swagger_ui":True,
	"specs_route":"/docs/"
}

swagger = Swagger(app,
#				  template = swagger_template,
				  config = swagger_config
				  )


@swag_from("docs/hello_world.yml", methods=['GET'])
@app.route('/', methods= ['GET'])
def hello():
	json_response = create_json_response(description="Menyapa Hello World",
										 data= "Hello world yahoo")
	response_data = jsonify(json_response)
	return response_data


@app.route('/text', methods= ['GET'])
def text():
	json_response = create_json_response(description="Original Text",
										 data="Halo, apa kabar semua?")
	response_data = jsonify(json_response)
	return response_data

@app.route('/text-clean', methods= ['GET'])
def text_clean():
	cleaned_text  = re.sub(r'[^a-zA-z0-9]',' ', 'Halo, apa kabar semua?')
	json_response = create_json_response(description="Original Text",
										 data=cleaned_text)
	response_data = jsonify(json_response)
	return response_data

if __name__ == '__main__':
	app.run(debug=True)
	 