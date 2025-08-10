from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Bank(db.Model):
    """Bank model representing a bank entity"""
    __tablename__ = 'banks'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(10), nullable=False, unique=True)
    
    # Relationship with branches
    branches = db.relationship('Branch', backref='bank', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        """Convert bank object to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code
        }
    
    def to_dict_with_branches(self):
        """Convert bank object to dictionary including branches"""
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'branches': [branch.to_dict() for branch in self.branches]
        }
    
    def __repr__(self):
        return f'<Bank {self.name}>'


class Branch(db.Model):
    """Branch model representing a bank branch"""
    __tablename__ = 'branches'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ifsc = db.Column(db.String(11), nullable=False, unique=True)
    address = db.Column(db.Text, nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    
    # Foreign key to bank
    bank_id = db.Column(db.Integer, db.ForeignKey('banks.id'), nullable=False)
    
    def to_dict(self):
        """Convert branch object to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'ifsc': self.ifsc,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'bank_id': self.bank_id
        }
    
    def to_dict_with_bank(self):
        """Convert branch object to dictionary including bank details"""
        return {
            'id': self.id,
            'name': self.name,
            'ifsc': self.ifsc,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'bank': self.bank.to_dict() if self.bank else None
        }
    
    def __repr__(self):
        return f'<Branch {self.name} - {self.ifsc}>'
