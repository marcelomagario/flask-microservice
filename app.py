from flask import Flask, request, jsonify
from sqlalchemy import create_engine, text

app = Flask(__name__)

# Configuração da URL de conexão com o banco de dados PostgreSQL
DATABASE_URL = 'postgresql://user:password@db:5432/jokesdb'
engine = create_engine(DATABASE_URL)

def get_joke(level, language):
    query = text("""
        SELECT joke FROM jokes 
        WHERE level = :level AND language = :language
    """)

    with engine.connect() as connection:
        result = connection.execute(query, {'level': level, 'language': language}).fetchone()

    return result[0] if result else None

@app.route('/joke', methods=['GET'])
def joke():
    level = request.args.get('level', 'medium')
    language = request.headers.get('Accept-Language', 'en-us')

    joke_text = get_joke(level, language)
    if joke_text is None:
        return jsonify({'error': 'No joke found'}), 404

    return jsonify({'joke': joke_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
