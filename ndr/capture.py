from scapy.all import sniff, Packet
import sys

def start_capture(callback, packet_count=0, interface=None):
    """
    Inicia a captura de pacotes na interface de rede especificada.

    :param callback: A função a ser chamada para cada pacote capturado.
    :param packet_count: O número de pacotes a serem capturados (0 para infinito).
    :param interface: A interface de rede a ser usada (ex: 'eth0'). Se None, Scapy tentará encontrar uma padrão.
    """
    print(f"[*] Iniciando a captura de pacotes na interface: {interface or 'padrão'}...")
    try:
        # O parâmetro 'prn' de sniff chama a função de callback para cada pacote.
        # 'store=False' evita que os pacotes sejam mantidos na memória.
        sniff(iface=interface, prn=callback, count=packet_count, store=False)
    except PermissionError:
        print("[!] Erro de permissão. Tente executar o script com 'sudo'.", file=sys.stderr)
        sys.exit(1)
    except OSError as e:
        print(f"[!] Erro de captura: A interface '{interface}' não foi encontrada ou está com problemas.", file=sys.stderr)
        print(f"    Detalhe: {e}", file=sys.stderr)
        print(f"    Por favor, verifique o nome da interface de rede da sua VM Vítima.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"[!] Ocorreu um erro inesperado durante a captura: {e}", file=sys.stderr)
        sys.exit(1)
