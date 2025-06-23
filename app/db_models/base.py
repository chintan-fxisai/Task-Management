from sqlalchemy.ext.declarative import declarative_base

# Create a base class for all models
Base = declarative_base()

# This will be imported by other model files
__all__ = ["Base"]
