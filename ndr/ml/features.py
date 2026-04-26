from scapy.all import Packet
from scapy.layers.inet import IP, TCP, UDP, ICMP

def extract_features(packet: Packet) -> dict:
    """
    Extrai um dicionário de features de um único pacote.
    Retorna um dicionário vazio se não for um pacote IP.
    """
    features = {}

    # Verifica se o pacote tem a camada de IP, que é nosso foco
    if packet.haslayer(IP):
        ip_layer = packet.getlayer(IP)
        features['ip_src'] = ip_layer.src
        features['ip_dst'] = ip_layer.dst
        features['protocol'] = ip_layer.proto

        # Features de TCP (ex: HTTP, FTP)
        if packet.haslayer(TCP):
            tcp_layer = packet.getlayer(TCP)
            features['src_port'] = tcp_layer.sport
            features['dst_port'] = tcp_layer.dport

        # Features de UDP (ex: DNS)
        elif packet.haslayer(UDP):
            udp_layer = packet.getlayer(UDP)
            features['src_port'] = udp_layer.sport
            features['dst_port'] = udp_layer.dport

        # Features de ICMP (ex: Ping)
        elif packet.haslayer(ICMP):
            icmp_layer = packet.getlayer(ICMP)
            features['icmp_type'] = icmp_layer.type
            features['icmp_code'] = icmp_layer.code
            # Para ICMP, podemos zerar as portas para manter a estrutura de dados consistente
            features['src_port'] = 0
            features['dst_port'] = 0

        # Se for um protocolo sobre IP mas não for TCP/UDP/ICMP
        else:
            features['src_port'] = 0
            features['dst_port'] = 0


    return features
