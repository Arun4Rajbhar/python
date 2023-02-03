import socket
class resolver:
    def __init__(self) -> None:
        self.cache={}
    def __call__(self, host):
        if host not in self.cache:
            self.cache[host]=socket.gethostbyname(host)
        return self.cache[host]    

        