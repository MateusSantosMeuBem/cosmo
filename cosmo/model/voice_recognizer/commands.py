# ---------- Personal packages ----------
from util import (
    get_variations
)

commands: dict[str, list[str]] = {
    'bot_name': [
        'cosmo',
        ' '.join(['cosmo' for _ in range(2)]),
        ' '.join(['cosmo' for _ in range(3)]),
        ' '.join(['cosmo' for _ in range(4)]),
        'cosmos',
        ' '.join(['cosmos' for _ in range(2)]),
        ' '.join(['cosmos' for _ in range(3)]),
        ' '.join(['cosmos' for _ in range(4)]),
    ],
    'nome' : [
        *get_variations(
            actions=[
                'busca',
                'buscando',
                'busques',
                'busque',
                'busco',
                'encontra',
                'encontrando',
                'encontres',
                'encontre',
                'encontro',
                'pesquisa',
                'pesquisando',
                'pesquisas',
                'pesquise',
                'pesquiso',
                'procura',
                'procurando',
                'procuras',
                'procure',
                'procuro',
                'quero',
            ],
            middles=[
                'por',
                'por um',
                'pelo',
                'pelos',
                'o',
                'os',
            ],
            objects=[
                'livro',
                'livros',
                'exemplar',
                'exemplares',
            ]
        ),
    ],
    'edição' : [
        *get_variations(
            actions=[
                'busca',
                'buscando',
                'busques',
                'busque',
                'busco',
                'encontra',
                'encontrando',
                'encontres',
                'encontre',
                'encontro',
                'pesquisa',
                'pesquisando',
                'pesquisas',
                'pesquise',
                'pesquiso',
                'procura',
                'procurando',
                'procuras',
                'procure',
                'procuro',
                'quero',
            ],
            middles=[
                'por',
                'por um',
                'pelo',
                'pelos',
                'o',
                'os',
            ],
            objects=[
                'edição',
                'edições',
            ]
        ),
        
    ]
}