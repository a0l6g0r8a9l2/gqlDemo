import uvicorn

from demoGql.settings import settings

if __name__ == '__main__':
    uvicorn.run(
        'demoGql.app:app',
        host=settings.server_host,
        port=settings.server_port,
        reload=True,
    )
