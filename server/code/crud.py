from sqlalchemy.orm import Session

import models
from elastic import MyElastic

elastic = MyElastic()


def search_post_by_text(db: Session, search_text: str):
    id_list = [item["id"] for item in elastic.search_by_text(search_text)]
    return db.query(models.Post) \
        .filter(models.Post.id.in_(id_list)) \
        .order_by(models.Post.created_date.desc()) \
        .all()


def delete_by_id(db: Session, id: int) -> bool:
    delete_item = elastic.search_by_id(id)
    if delete_item is not None:
        elastic_result = elastic.delete_by_id(delete_item[0]["_id"])
        db_result = bool(
                db.query(models.Post).filter(models.Post.id == id).delete())
        db.commit()
        return all((elastic_result, db_result))
    return False
