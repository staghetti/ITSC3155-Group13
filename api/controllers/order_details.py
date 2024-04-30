from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import order_details as model, ingredients as ing_model, recipes as rec_model
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    # Check if sufficient ingredients are available
    menu_item_recipes = db.query(rec_model.Recipe).filter(rec_model.Recipe.menu_item_id == request.menu_item_id).all()
    if not menu_item_recipes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No recipes found for this menu item.")

    # Check each required ingredient's inventory
    for recipe in menu_item_recipes:
        ingredient = db.query(ing_model.Ingredients).filter(ing_model.Ingredients.id == recipe.ingredient_id).first()
        if not ingredient:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Ingredient not found for ID {recipe.ingredient_id}")

        # Check if the available inventory is less than the required amount
        required_amount = recipe.amount * request.amount
        if ingredient.inventory_quantity < required_amount:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail=f"Insufficient inventory for ingredient {ingredient.name}")

        # Deduct the required amount from inventory
        ingredient.inventory_quantity -= required_amount

    # If all checks pass, create the order detail
    new_order_detail = model.OrderDetail(
        order_id=request.order_id,
        menu_item_id=request.menu_item_id,
        amount=request.amount
    )

    try:
        db.add(new_order_detail)
        db.commit()
        db.refresh(new_order_detail)
    except SQLAlchemyError as e:
        db.rollback()
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_order_detail


def read_all(db: Session):
    try:
        result = db.query(model.OrderDetail).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, order_detail_id):
    try:
        order_detail = db.query(model.OrderDetail).filter(model.OrderDetail.id == order_detail_id).first()
        if not order_detail:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order detail Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return order_detail


def update(db: Session, order_detail_id, request):
    try:
        order_detail = db.query(model.OrderDetail).filter(model.OrderDetail.id == order_detail_id)
        if not order_detail.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order detail Id not found!")
        update_data = request.dict(exclude_unset=True)
        order_detail.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return order_detail.first()


def delete(db: Session, order_detail_id):
    try:
        order_detail = db.query(model.OrderDetail).filter(model.OrderDetail.id == order_detail_id)
        if not order_detail.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order detail Id not found!")
        order_detail.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
