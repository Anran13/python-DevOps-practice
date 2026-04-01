import molotov

@molotov.scenario(100)
async def scenario_post(session):
    resp = await session.post(
        "http://localhost:5000",
        params={'q': 'devops'},
        allow_redirects=False,
    )
    status = resp.status
    error = "unexpected redirect status: %s" % status
    assert status == 301, error
