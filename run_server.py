import uvicorn
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=3001)
    args = parser.parse_args()

    uvicorn.run("app.main:app", host=args.host, port=args.port, reload=True)

if __name__ == "__main__":
    main()
