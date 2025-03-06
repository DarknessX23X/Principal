import docker

try:
    client = docker.from_env()
    # ... seu código aqui ...
except Exception as e:
    print(f"Um erro ocorreu: {e}")