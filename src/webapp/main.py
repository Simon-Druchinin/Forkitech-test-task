from fastapi import FastAPI

from tron_api.router import router as tron_api_router


def add_routers(app: FastAPI) -> FastAPI:
    routers = (tron_api_router,)
    for router in routers:
        app.include_router(router)
    return app


def create_app() -> FastAPI:
    return add_routers(FastAPI())


app = create_app()


@app.get("/health")
def health() -> dict:
    return {}
