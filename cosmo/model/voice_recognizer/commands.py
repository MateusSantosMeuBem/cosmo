# ---------- Personal packages ----------
from util import (
    get_variations
)

commands: dict[str, list[str]] = {
    'caller': {
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
    },
    'search': {
        'nome' : [
            *get_variations(
                actions=[
                    'buscar',
                    'busca',
                    'buscando',
                    'buscam',
                    'busques',
                    'busque',
                    'busco',
                    'encontrar',
                    'encontra',
                    'encontrando',
                    'encontram',
                    'encontres',
                    'encontre',
                    'encontro',
                    'pesquisar',
                    'pesquisa',
                    'pesquisando',
                    'pesquisam',
                    'pesquisas',
                    'pesquise',
                    'pesquiso',
                    'procurar',
                    'procura',
                    'procurando',
                    'procuram',
                    'procuras',
                    'procure',
                    'procuro',
                    'quero',
                ],
                middles=[
                    'por',
                    'por um',
                    'um',
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
                    'buscar',
                    'busca',
                    'buscando',
                    'buscam',
                    'busques',
                    'busque',
                    'busco',
                    'encontrar',
                    'encontra',
                    'encontrando',
                    'encontram',
                    'encontres',
                    'encontre',
                    'encontro',
                    'pesquisar',
                    'pesquisa',
                    'pesquisando',
                    'pesquisam',
                    'pesquisas',
                    'pesquise',
                    'pesquiso',
                    'procurar',
                    'procura',
                    'procurando',
                    'procuram',
                    'procuras',
                    'procure',
                    'procuro',
                    'quero',
                ],
                middles=[
                    'por',
                    'por uma',
                    'uma',
                    'pela',
                    'pelas',
                    'a',
                    'as',
                ],
                objects=[
                    'edição',
                    'edições',
                ]
            ),
            
        ]
    }
}