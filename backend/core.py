import ctypes
import os
import ctypes
from fastapi import FastAPI

app = FastAPI()

# Load the C++ shared library
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../bridges/cpp/libcompute.so"))
cpp_lib = ctypes.CDLL(lib_path)


@app.get("/")
async def root():
    return {"message": "J.A.R.V.I.S. AI Backend Running"}

@app.get("/run-cpp")
async def run_cpp():
    cpp_lib.compute()  # Call the C++ function
    return {"message": "C++ function executed"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
