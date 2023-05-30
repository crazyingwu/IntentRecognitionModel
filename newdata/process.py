import json
import random

def get_data():
    train_file = './newdata/my_train.json'
    intents = []
    sentences = []
    slots = []
    with open(train_file, 'r', encoding="UTF-8") as fp:
        train_data = eval(fp.read())
        for t in train_data:
            print(t)
            sentence = t['text']
            sentences.append(sentence)
            intent = t['intent']
            intents.append(intent)
            slots.extend(t['slots'].keys())

    intents = list(set(intents))
    slots = list(set(slots))
    with open('./newdata/sentences.txt','w', encoding="UTF-8") as fp:
        fp.write('\n'.join(sentences))
    with open('./newdata/intents.txt','w') as fp:
        fp.write('\n'.join(intents))
    with open('./newdata/slots.txt','w') as fp:
        fp.write('\n'.join(slots))


def train_test_split(ratio=0.8):
    train_file = './train.json'
    with open(train_file, 'r') as fp:
        data = eval(fp.read())
        random.shuffle(data)
        total = len(data)
        train_data = data[:int(total * ratio)]
        test_data = data[int(total * ratio):]
    with open('train_process.json', 'w') as fp:
        json.dump(train_data, fp, ensure_ascii=False)
    with open('test_process.json', 'w') as fp:
        json.dump(test_data, fp, ensure_ascii=False)


if __name__ == '__main__':
    get_data()
    # train_test_split()
