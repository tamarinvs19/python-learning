import os


def save_graph(edges, name):
    with open(name, 'w') as fout:
        print("digraph {", file=fout)
        for sourse, people in edges:
            for man in people:
                print(f'\t"{sourse}" -> "{man}"', file=fout)
            print(file=fout)
        print("}", file=fout) 

def gen_png(file_in, file_out):
    os.system(f'dot {file_in} -Tpng > {file_out}')

def read_table(name):
    result: list[tuple[str, list[str]]] = []
    with open(name, 'r') as fin:
        for line in fin.readlines():
            names: list[str] = line.strip().split(',')
            result.append((names[0], list(filter(lambda x: x != '', names[1:4]))))
    return result


if __name__ == '__main__':
    output_name = 'graph'
    save_graph(read_table('новогодний флешмоб - Лист1.csv'), output_name)
    gen_png(output_name, 'output.png')

