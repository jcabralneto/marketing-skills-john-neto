#!/usr/bin/env python3
"""Instala cópias locais; nunca sobrescreve uma skill diferente."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil


def inventory(folder):
    return {
        p.relative_to(folder).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sorted(folder.rglob('*'))
        if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc'
    }


def install(source, target, dry_run=False):
    sources = sorted(p for p in source.iterdir() if (p / 'SKILL.md').is_file())
    if not sources:
        raise ValueError('Nenhuma skill encontrada na origem.')
    plan = []
    for item in sources:
        destination = target / item.name
        exists = destination.exists() or destination.is_symlink()
        if exists and (destination.is_symlink() or not destination.is_dir() or inventory(item) != inventory(destination)):
            raise ValueError(f'Destino diferente já existe; nada foi sobrescrito: {destination}')
        plan.append((item, destination, 'identica' if exists else 'nova'))
    if not dry_run:
        target.mkdir(parents=True, exist_ok=True)
        for item, destination, status in plan:
            if status == 'nova':
                shutil.copytree(item, destination, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
            if inventory(item) != inventory(destination):
                raise RuntimeError(f'Conferência de cópia falhou: {destination}')
    return {'simulacao': dry_run, 'destino': str(target), 'skills': [
        {'nome': item.name, 'estado': status, 'arquivos': len(inventory(item))}
        for item, _, status in plan
    ]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--destino', type=Path, default=Path.home() / '.codex' / 'skills')
    parser.add_argument('--simular', action='store_true')
    args = parser.parse_args()
    source = Path(__file__).resolve().parents[1] / 'skills'
    try:
        result = install(source, args.destino.expanduser().resolve(), args.simular)
    except (ValueError, RuntimeError, OSError) as error:
        parser.exit(1, f'{error}\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
