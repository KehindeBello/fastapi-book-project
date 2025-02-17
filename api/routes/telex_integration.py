from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

integration_data = {
    "data": {
        "date": {"created_at": "2025-02-16", "updated_at": "2025-02-16"},
        "descriptions": {
            "app_name": "fastapiCiCD",
            "app_description": "A ci-cd slack notifier",
            "app_logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTj1aRtcV9UdFO3mfUOMjjXGxGLbZH3w1byPQ&s",
            "app_url": "http://ec2-34-228-162-152.compute-1.amazonaws.com", 
            "background_color": "#fff",
        },
        "is_active": True,
        "integration_type": "modifier",
        "key_features": ["Real time updates for slack"],
        "author": "KehindeBello",
        "settings": [
            {
                "label": "channel-name",
                "type": "text",
                "required": True,
                "default": "#devopsalert",
            },
            {
                "label": "time interval",
                "type": "dropdown",
                "required": True,
                "default": "immediate",
                "options": ["immediate", "Every 5-min", "Every 10-min"],
            },
            {
                "label": "event_type",
                "type": "dropdown",
                "required": True,
                "default": "ci_pipeline",
                "options": ["ci_pipeline", "cd_pipeline", "deployment", "error"],
            },
            {
                "label": "message",
                "type": "text",
                "required": True,
                "default": "success",
            },
            {
                "label": "include_log",
                "type": "checkbox",
                "required": True,
                "default": "True",
            },
        ],
        "target_url": "https://hooks.slack.com/services/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",
        "tick_url": "http://ec2-34-228-162-152.compute-1.amazonaws.com/api/v1/test/telex-webhook",
    }
}

router = APIRouter()


@router.get("/telex-webhook", status_code=status.HTTP_200_OK)
async def telex_webhook():
    return JSONResponse(status_code=status.HTTP_200_OK, content=integration_data)
