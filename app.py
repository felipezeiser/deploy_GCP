# biblioteca para criar ids de string unicas
import uuid

# importa a biblioteca Flask
# jsonify: transforma objetos, como dicionários, em json
# request: captura a informação da requisição recebida pelas rotas
# make_response: usado para criar as respostas ao usuário
from flask import Flask, jsonify, request

from functools import wraps

import joblib
import pandas as pd

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():

    data = request.get_json()

    if not data:
        return jsonify({'message': 'Envie os dados para fazer a predicão'}), 500
    # print(data)

    try:
        X_test = {key: float(value) for key, value in data.items()}
        X_test = pd.DataFrame([X_test])
        prediction = model.predict(X_test)
        # print(prediction)

        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        print(e)
        return jsonify({'message': 'Erro durante a predição. \
                        Consulte a documentação para verificar \
                         as chaves dos dados.'}), 500

if __name__ == '__main__':

    print("Carregando o modelo.....")
    model = joblib.load('rf_opt.joblib')
    print("Modelo carregado!")
    app.run(debug=True)