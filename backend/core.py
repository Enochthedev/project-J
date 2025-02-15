from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'J.A.R.V.I.S. AI Backend Running'}

@app.get('/run-rust')
async def run_rust_code():
    result = subprocess.run(['../bridges/rust/target/release/compute'], capture_output=True, text=True)
    return {'rust_output': result.stdout}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
