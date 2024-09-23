import uvicorn 
# ASGI server
# hỗ trợ xử lý bất đồng bộ (asynchronous) và giúp các ứng dụng web Python hoạt động hiệu quả hơn, đặc biệt khi cần xử lý nhiều yêu cầu cùng lúc.

if __name__ == '__main__': 
    uvicorn.run('app.main:app',reload=True)