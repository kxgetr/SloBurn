import argparse
import json
import sys
from pathlib import Path

def analyze(data):
    n, f, s = (data['requests'], data['failures'], data['target'])
    if not 0 <= f <= n or n <= 0 or (not 0 < s < 1):
        raise ValueError('invalid SLO')
    return round(f / n / (1 - s), 8)

def main():
    parser = argparse.ArgumentParser(description='Başarısız istek oranını hedef hata bütçesiyle karşılaştırır.')
    parser.add_argument('file', nargs='?', help='UTF-8 JSON input file (default: stdin)')
    args = parser.parse_args()
    try:
        raw = Path(args.file).read_text(encoding='utf-8-sig') if args.file else sys.stdin.read()
        result = analyze(json.loads(raw))
        print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
    except (SyntaxError, ValueError, KeyError, TypeError, OSError, IndexError, ArithmeticError) as error:
        parser.exit(2, f'Invalid input: {error}\n')
if __name__ == '__main__':
    main()
