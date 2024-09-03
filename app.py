from flask import Flask, request, jsonify

app = Flask(__name__)

def get_joke(level, language):
    jokes = {
        'en-us': {
            'low': "Why do surfers don't like reheated food? Because they don't like microwave",
            'medium': "Why don't skeletons skydive? They don't have the guts to do it.",
            'high': 'How many programmers does it take to change a light bulb? None. It’s a hardware problem.'
        },
        'pt-br': {
            'low': 'Por que os surfistas não curtem comida requentada? Porque eles não gostam de microondas! kkk',
            'medium': 'Por que os esqueletos não pulam de para-quedas? Porque eles não tem estomago pra isso',
            'high': 'Quantos programadores são necessários para trocar uma lâmpada? Nenhum. É um problema de hardware.'
        }
    }
    
    return jokes.get(language, {}).get(level, None)

@app.route('/joke', methods=['GET'])
def joke():
    level = request.args.get('level', 'medium')
    language = request.headers.get('Accept-Language', 'en')

    joke_text = get_joke(level, language)
    if joke_text is None:
        return jsonify({'error': 'No joke found for the given parameters'}), 404

    return jsonify({'joke': joke_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
