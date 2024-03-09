import sys

if len(sys.argv) < 4:
    print("error!!!!!!!")
else:
    Factor={
        "sol": float(sys.argv[1]),
        "peso_argentino": float(sys.argv[2]),
        "Dollar": float(sys.argv[3])
    }
    
    clp= float(sys.argv[4])
    
    print(f'''
            TABLA DE CONVERSION
            
            CLP {clp:,.0f} equivale a : 
            
            {(Factor["sol"]*clp):.1f}  Soles Peruanos.
            {(Factor["peso_argentino"]*clp):.1f}  Peso Argentino.
            {(Factor["Dollar"]*clp):.1f}  Dolares Americanos.
            ''')
            

