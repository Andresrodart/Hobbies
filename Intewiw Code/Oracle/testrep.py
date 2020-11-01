import subprocess
import sys

if __name__ == "__main__":
    # Definimos todos los casos a probar
    cases = [
        ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaab', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'),
        ('abcabcabctabcabcabctabcabcabct', 'abcabcabct'),
        ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'a'),
        ('baaaaaabaaaaaa', 'baaaaaa'),
        ('abcabcabct', 'abcabcabct'),
        ('ababababababababab', 'ab'),
        ('abaxabax', 'abax'),
        ('abcabcabc', 'abc'),
        ('1234', '1234'),
        ('ab', 'ab'),
        ('a', 'a'),
        ('', ''),
    ]
    i = 1
    # Por cada caso llamamos al programa norep
    for pair in cases:
        result = subprocess.run(["py", sys.argv[1], pair[0]], capture_output=True)
        result = result.stdout.decode("utf-8").strip()
        print('case #{} was'.format(i), ('successful' if result == pair[1] else 'wrong'))
        i += 1
