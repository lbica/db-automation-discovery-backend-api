from urllib.parse import urlparse
import uvicorn
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:3001")
    # parser.add_argument("--port", type=int, default=3001)
    args = parser.parse_args()

    parsed = urlparse(args.url)
    host = parsed.hostname
    port = parsed.port

    uvicorn.run(
        "dbad_backend_api.api.main:app",
        host=host,
        port=port,
        reload=False
    )

if __name__ == "__main__":
    main()
