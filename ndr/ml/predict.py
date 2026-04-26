import joblib
import os
import pandas as pd

# Caminhos para os artefatos do modelo
MODEL_DIR = 'models'
MODEL_PATH = os.path.join(MODEL_DIR, 'decision_tree_model.pkl')
ENCODER_PATH = os.path.join(MODEL_DIR, 'label_encoder.pkl')

# Carrega o modelo e o encoder uma vez quando o módulo é importado
try:
    print("[Predição] Carregando modelo e encoder...")
    model = joblib.load(MODEL_PATH)
    label_encoder = joblib.load(ENCODER_PATH)
    print("[Predição] Modelo e encoder carregados com sucesso.")
except FileNotFoundError:
    print(f"[!] Erro Crítico: Arquivos de modelo não encontrados em '{MODEL_DIR}'.")
    print("    Por favor, execute o script de treinamento (training.py) primeiro.")
    model = None
    label_encoder = None

def predict_packet(packet_features: dict) -> str:
    """
    Prevê o tipo de tráfego de um pacote com base em suas features.

    :param packet_features: Dicionário de features extraído do pacote.
    :return: String com o nome da classe prevista (ex: 'BENIGN', 'DDoS').
    """
    if not model or not label_encoder:
        return "ERRO: Modelo não carregado"

    # 1. Verifica se temos as features necessárias
    if 'dst_port' not in packet_features:
        return "Não-IP ou features insuficientes"

    # 2. Prepara os dados para o modelo
    # O modelo foi treinado com a coluna 'Destination Port'.
    # Criamos um DataFrame com a mesma estrutura.
    dst_port = packet_features['dst_port']
    data_for_prediction = pd.DataFrame([[dst_port]], columns=['Destination Port'])

    # 3. Faz a predição
    prediction_numeric = model.predict(data_for_prediction)
    
    # 4. Decodifica o resultado numérico para texto
    prediction_label = label_encoder.inverse_transform(prediction_numeric)

    # Retorna a primeira (e única) predição como uma string
    return prediction_label[0]
