from ndr.capture import start_capture
from ndr.ml.features import extract_features
from ndr.ml.predict import predict_packet  # Importa a nova função
from scapy.all import Packet

def process_packet(packet: Packet):
    """
    Função de callback para cada pacote capturado.
    Extrai features, faz a predição e imprime o resultado.
    """
    features = extract_features(packet)
    
    if features:  # Apenas processa se features foram extraídas (pacotes IP)
        # Etapa 5: Classificação em Tempo Real
        predicted_label = predict_packet(features)
        
        # Imprime um alerta apenas se não for benigno, para focar nos ataques
        if predicted_label != 'BENIGN':
            print(f"[ALERTA] Ataque detectado! Tipo: {predicted_label} | IP Origem: {features.get('ip_src')} -> IP Destino: {features.get('ip_dst')}")
        else:
            # Opcional: descomente a linha abaixo se quiser ver o tráfego benigno também
            # print(f"[Info] Tráfego benigno detectado de {features.get('ip_src')}")
            pass


def main():
    """
    Ponto de entrada principal do sistema NDR.
    """
    print("Iniciando o sistema NDR em modo de detecção...")
    
    # A interface de rede da VM Vítima (Lubuntu)
    network_interface = "enp0s3"

    # Inicia a captura e o processo de predição em tempo real
    start_capture(callback=process_packet, interface=network_interface)

    print("Sistema NDR finalizado.")

if __name__ == "__main__":
    main()
