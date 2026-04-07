import molotov


@molotov.scenario(weight=1)
async def scenario_one(session):
    async with session.get("http://localhost:5000/") as resp:
        assert resp.status == 200, resp.status


@molotov.scenario(weight=80)
async def scenario_two(session):
    resp = await session.post(
        "http://localhost:5000", params={'q': 'devops'}
    )
    redirect_status = resp.history[0].status
    error = "unexpected redirect status: %s" % redirect_status
    assert redirect_status == 301, error