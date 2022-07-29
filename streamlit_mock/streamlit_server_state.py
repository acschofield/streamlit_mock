class ServerStateLock(dict):
    def __missing__(self, key):
        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class ServerState(dict):
    def __missing__(self, key):
        return None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


server_state_lock = ServerStateLock()
server_state = ServerState()
