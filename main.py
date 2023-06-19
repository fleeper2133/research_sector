import uvicorn
from fastapi import FastAPI
from v1.routers import group as group_router, phase as phase_router, project as project_router, \
    employee as employee_router, operation as operation_router, stage as stage_router, db as db_router
from views.routers import project_view, stage_view, phase_view, operation_view, group_view, employee_view, employee_group_view, db_view
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="views/static"), name="static")
app.include_router(project_router.router, prefix='/api/v1/project')
app.include_router(stage_router.router, prefix='/api/v1/stage')
app.include_router(phase_router.router, prefix='/api/v1/phase')
app.include_router(operation_router.router, prefix='/api/v1/operation')
app.include_router(group_router.router, prefix='/api/v1/group')
app.include_router(employee_router.router, prefix='/api/v1/employee')
app.include_router(project_view.router)
app.include_router(stage_view.router)
app.include_router(phase_view.router)
app.include_router(operation_view.router)
app.include_router(group_view.router)
app.include_router(employee_view.router)
app.include_router(employee_group_view.router)
app.include_router(db_router.router, prefix='/api/v1')
app.include_router(db_view.router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, host='127.0.0.1', port=8080, workers=2)
