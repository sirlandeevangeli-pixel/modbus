import time
from pymodbus.client import ModbusTcpClient

# Configurações do Servidor (Modbus Slave)
# IMPORTANTE: Altere para o IP correto se a máquina simuladora mudar de endereço
SERVER_IP = "10.1.20.103"
SERVER_PORT = 502
SLAVE_ID = 1  # Definido como 'Slave ID: 1' na sua tela

def rodar_teste():
    # Inicializa o cliente Modbus TCP
    client = ModbusTcpClient(SERVER_IP, port=SERVER_PORT)
    
    print(f"Tentando conectar ao Modbus Slave em {SERVER_IP}:{SERVER_PORT}...")
    if not client.connect():
        print("Erro: Não foi possível conectar ao servidor. Verifique o IP, porta e o Firewall.")
        return

    print("Conectado com sucesso!\n")
    
    try:
        # Loop para ler os dados simulando o monitoramento do inversor
        for i in range(5):
            print(f"--- Leitura {i+1} ---")
            
            # Lê 10 Holding Registers a partir do endereço 0 (conforme seu print)
            result = client.read_holding_registers(
                address=0,
                count=10,
                device_id=SLAVE_ID
            )
            
            if result.isError():
                print("Erro ao ler os registradores:", result)
            else:
                # Exibe a lista com os 10 valores lidos
                valores = result.registers
                print(f"Valores lidos (Reg 40001 a 40010): {valores}")
                print(f"Frequência atual (Exemplo Reg 0): {valores[0]} Hz")
            
            time.sleep(2) # Aguarda 2 segundos antes da próxima leitura
            
    except Exception as e:
        print(f"Ocorreu um erro durante a comunicação: {e}")
    finally:
        # Fecha a conexão
        client.close()
        print("\nConexão encerrada.")

if __name__ == "__main__":
    rodar_teste()
