from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from emprega_vale.config import settings as stg, load_routes


def create_app() -> FastAPI:
    app = FastAPI(
        debug=stg.DEBUG,
        title='Emprega Vale',
        description='Portal de Emprego da Região do Vale do Paraíba',
        version='1.0.0',
        default_response_class=ORJSONResponse,
    )

    load_routes(app)

    @app.get('/health-check')
    async def health_check():
        return 'ok'

    return app


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(create_app(), host=stg.HOST, port=stg.PORT, debug=stg.DEBUG)
