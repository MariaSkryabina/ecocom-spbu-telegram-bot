from sqlalchemy.ext.asyncio import AsyncSession

from tgbot.db.models.points import Points


async def add_point(
        session: AsyncSession,
        photo_id: str,
        address: str,
        route: str,
        latitude: float,
        longitude: float,
        paper: bool,
        pat: bool,
        glass: bool,
        alum: bool,
        pp_h: bool,
        pp_s: bool,
        batteries: bool,
        cups: bool,
        bulbs: bool,
        notes: str
):

    new_point = Points(photo_id=photo_id, address=address, route=route, latitude=latitude, longitude=longitude,
                       paper=paper, pat=pat, glass=glass, alum=alum, pp_h=pp_h, pp_s=pp_s, batteries=batteries,
                       cups=cups, bulbs=bulbs, notes=notes)
    session.add(new_point)
    await session.commit()
