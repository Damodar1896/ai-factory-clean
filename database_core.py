import os
import json
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

DB_PATH = "enterprise_empire.db"
Base = declarative_base()

class LeadModel(Base):
    __tablename__ = 'leads'
    id = Column(Integer, primary_key=True, autoincrement=True)
    business_name = Column(String, index=True)
    niche = Column(String, index=True)
    city = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    status = Column(String, default="Fresh")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

def init_enterprise_db():
    engine = create_engine(f"sqlite:///{DB_PATH}", echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Migrate existing JSON data if available
    json_file = "business_empire_master_db.json"
    if os.path.exists(json_file):
        try:
            with open(json_file, "r") as f:
                old_leads = json.load(f)
                migrated_count = 0
                for l in old_leads:
                    existing = session.query(LeadModel).filter_by(email=l.get("email")).first()
                    if not existing:
                        new_lead = LeadModel(
                            business_name=l.get("business_name", "N/A"),
                            niche=l.get("niche", "N/A"),
                            city=l.get("city", "N/A"),
                            email=l.get("email", "unknown@domain.com"),
                            status=l.get("status", "Fresh")
                        )
                        session.add(new_lead)
                        migrated_count += 1
                session.commit()
                print(f"[Database Core] Successfully migrated {migrated_count} records from JSON to Enterprise SQLAlchemy DB.")
        except Exception as e:
            print(f"[Database Error during migration]: {e}")
    else:
        print("[Database Core] Enterprise SQLite DB initialized fresh (No legacy JSON found).")
    
    session.close()

if __name__ == "__main__":
    init_enterprise_db()
