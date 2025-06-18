from sqlalchemy.orm import Session
from ..models.address import Address
from ..schemas.address import AddressCreate, AddressUpdate

def get_user_addresses(db: Session, user_id: int):
    """獲取指定使用者的所有送貨地址"""
    return db.query(Address).filter(Address.user_id == user_id).all()

def get_address(db: Session, address_id: int):
    """根據地址 ID 獲取地址"""
    return db.query(Address).filter(Address.id == address_id).first()

def create_address(db: Session, address: AddressCreate, user_id: int):
    """創建新送貨地址"""
    if address.is_default:
        current_default = db.query(Address).filter(Address.user_id == user_id, Address.is_default == True).first()
        if current_default:
            current_default.is_default = False
            db.add(current_default)

    db_address = Address(**address.dict(), user_id=user_id)
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address

def update_address(db: Session, address_id: int, address_update: AddressUpdate, user_id: int):
    """更新送貨地址"""
    db_address = db.query(Address).filter(Address.id == address_id, Address.user_id == user_id).first()
    if db_address:
        update_data = address_update.dict(exclude_unset=True)
        if 'is_default' in update_data and update_data['is_default'] == True:
            current_default = db.query(Address).filter(Address.user_id == user_id, Address.is_default == True).first()
            if current_default and current_default.id != address_id:
                current_default.is_default = False
                db.add(current_default)

        for key, value in update_data.items():
            setattr(db_address, key, value)
        db.commit()
        db.refresh(db_address)
    return db_address

def delete_address(db: Session, address_id: int, user_id: int):
    """刪除送貨地址"""
    db_address = db.query(Address).filter(Address.id == address_id, Address.user_id == user_id).first()
    if db_address:
        db.delete(db_address)
        db.commit()
    return db_address