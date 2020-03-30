#create a blockchain
#postman and flask

#import libraries
import datetime
import hashlib
import json
from flask import Flask,jsonify

# part -1 building a blockchain
class blockchain:
    def __init__(self):
        self.chain=[]
        self.create_block(proof=1,prev_hash='0')
        
    def create_block(self,proof,prev_hash):
        block={'index':len(self.chain)+1,
               'Timestamp':str(datetime.datetime.now()),
              'proof':proof,
              'previous_hash':prev_hash,
              }
        self.chain.append(block)
        return block
    def get_prev_block(self):
        return self.chain[-1]
    
    def proof_of_work(self,prev_proof):
        new_proof=1
        check_proof=False
        while check_proof is False:
            hash_operation=hashlib.sha256(str(new_proof** - prev_proof**2).encode()).hexdigest()
            if hash_operation[:4]=='0000':
                check_proof=True
            else:
                new_proof+=1
        return new_proof
    
    def hash(self,block):
        encoded_block=json.dumps(block,sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self,chain):
        prev_block=chain[0]
        block_index=1
        while block_index<len(chain):
            block=chain[block_index]
            if block['previous_hash']!=self.hash(prev_block):
                return False
            prev_proof=prev_block['proof']
            proof=block['proof']
            hash_operation=hashlib.sha256(str(proof**2 - prev_proof**2).encode()).hexdigest()
            if hash_operation[:4]!='0000':
                return False
            prev_block=block
            block_index+=1
        return True
    
#part 2-Mining our blockchain
#creating a web app
    
app=Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

bchain=blockchain() 
#mining block
@app.route('/mine_block',methods=['GET'])   
def mine_block():
    previous_block=bchain.get_prev_block()
    previous_proof=previous_block['proof']
    proof=bchain.proof_of_work(previous_proof)
    previous_hash=bchain.hash(previous_block)
    block=bchain.create_block(proof,previous_hash)
    response={'message':'Congratulations you just mined a block!',
              'index':block['index'],
              'timestamp':block['Timestamp'],
              'proof':block['proof'],
              'previous_hash':block['previous_hash']}
    return jsonify(response),200

#get full chain

@app.route('/get_chain',methods=['GET'])


def get_chain():
    response={'chain':bchain.chain,
             'length':len(bchain.chain)}
    return jsonify(response),200

@app.route('/is_valid',methods=['GET'])
def is_valid():
    is_valid=bchain.is_chain_valid(bchain.chain)
    if is_valid:
        resopnse={'message':'All good,The blockchain is valid'}
    else:
        response={'message':'Blockchain is not valid'}
    return jsonify(response),200

#running app
app.run(host= '0.0.0.0',port=5000)
    

























              
              
              
              
              
              
              
              
    



















    
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    