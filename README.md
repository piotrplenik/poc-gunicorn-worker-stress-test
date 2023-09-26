# Stress test for gunicorn

## Quick start

### Setup

```bash
python3 -m venv venv
source ./venv/bin/activate

pip install -r requirements.txt
```

### Run app

```bash
gunicorn -w 4 myapp:app
```

### Benchmark

Run in one window benchmarking using ApacheBench:

```bash
ab -n 100 -s 50 -c 5 http://127.0.0.1:8000/
```

In parallel try to open status page:

```bash
curl http://127.0.0.1:8000/status
```