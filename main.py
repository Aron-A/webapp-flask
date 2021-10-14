from flask import Flask
import configs as confg

if __name__ == "__main__":
    print(f'Tela executando em: http://localhost:{confg.Port}/{confg.Name_Project}')
    confg.app.run(host='0.0.0.0', port=confg.Port, debug=True)




