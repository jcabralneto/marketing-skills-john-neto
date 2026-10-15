#!/usr/bin/env python3
"""Compare duas proporções independentes; não decide o vencedor do experimento."""

import argparse
import json
import math
from statistics import NormalDist


def wilson(conversoes, total, z):
    p = conversoes / total
    z2 = z * z
    divisor = 1 + z2 / total
    centro = (p + z2 / (2 * total)) / divisor
    margem = z * math.sqrt(p * (1 - p) / total + z2 / (4 * total**2)) / divisor
    return max(0.0, centro - margem), min(1.0, centro + margem)


def comparar(a_conversoes, a_total, b_conversoes, b_total, confianca=0.95):
    for nome, conversoes, total in [('A', a_conversoes, a_total), ('B', b_conversoes, b_total)]:
        if type(conversoes) is not int or type(total) is not int:
            raise ValueError(f'{nome}: informe contagens inteiras.')
        if total <= 0 or not 0 <= conversoes <= total:
            raise ValueError(f'{nome}: total deve ser positivo e conversões devem ficar entre zero e total.')
    if not isinstance(confianca, (int, float)) or not math.isfinite(confianca) or not 0 < confianca < 1:
        raise ValueError('Confiança deve ficar entre 0 e 1, sem incluir os extremos.')
    quantil = (1 + confianca) / 2
    if not 0.5 < quantil < 1:
        raise ValueError('Confiança fora da precisão numérica suportada.')
    z = NormalDist().inv_cdf(quantil)
    a, b = a_conversoes / a_total, b_conversoes / b_total
    la, ua = wilson(a_conversoes, a_total, z)
    lb, ub = wilson(b_conversoes, b_total, z)
    diferenca = b - a
    inferior = max(-1.0, diferenca - math.sqrt((b - lb)**2 + (ua - a)**2))
    superior = min(1.0, diferenca + math.sqrt((ub - b)**2 + (a - la)**2))
    return {
        'a': {'conversoes': a_conversoes, 'elegiveis': a_total, 'taxa_percentual': a * 100},
        'b': {'conversoes': b_conversoes, 'elegiveis': b_total, 'taxa_percentual': b * 100},
        'diferenca_pontos_percentuais': diferenca * 100,
        'variacao_relativa_percentual': (b / a - 1) * 100 if a else None,
        'confianca': confianca,
        'intervalo_diferenca_pp': [inferior * 100, superior * 100],
        'intervalo_inclui_zero': inferior <= 0 <= superior,
        'metodo': 'Wilson/Newcombe para diferença B-A, sem correção de continuidade',
        'limite': 'Amostras independentes, resultado binário, horizonte definido. Não corrige múltiplos testes, espiadas ou falhas de desenho; não decide vencedor.',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--a-conversoes', type=int, required=True)
    parser.add_argument('--a-total', type=int, required=True)
    parser.add_argument('--b-conversoes', type=int, required=True)
    parser.add_argument('--b-total', type=int, required=True)
    parser.add_argument('--confianca', type=float, default=0.95)
    args = parser.parse_args()
    try:
        result = comparar(args.a_conversoes, args.a_total, args.b_conversoes, args.b_total, args.confianca)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
