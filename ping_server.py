from mcp.server.fastmcp import FastMCP
import subprocess
import platform

mcp = FastMCP("ping-server")

@mcp.tool()
def ping(host: str) -> str:
    system = platform.system().lower()
    if system == "windows":
        cmd = ["ping", "-n", "1", host]
    else:
        cmd = ["ping", "-c", "1", host]

    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout or result.stderr


def main():
    # entrypoint untuk exe
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
