# Autora: Mariana Martignago.
# Feito para o desafio técnico ProWay - parte 1.


valor_em_reais = float(input("Valor a ser investido em anúncios: "))

def calculadora_anuncios(valor_em_reais):
  if valor_em_reais < 0.01:
    print("Erro: Valor inválido. O valor deve ser maior do que 1 centavo.")

  else:
    # Para cada 1 real investido, 30 anúncios originais serão visualizados. .
    alcance_anuncio_original = valor_em_reais * 30

    # A cada 100 pessoas que visualizam o anúncio 12 clicam nele.
    clicam = alcance_anuncio_original / 100 * 12

    # A cada 20 pessoas que clicam no anúncio 3 compartilham nas redes sociais.
    compartilham = clicam / 20 * 3

    # Cada compartilhamento nas redes sociais gera 40 novas visualizações.
    # O mesmo anúncio é compartilhado no máximo 4 vezes em sequência. 
    novas_visualizacoes = (compartilham * 4) * 40

    # Cálculo do máximo de visualizações possível.
    valor_final = round(alcance_anuncio_original + novas_visualizacoes)

    return f"Projeção aproximada da quantidade máxima de pessoas que visualizarão o mesmo anúncio (considerando o anúncio original + os compartilhamentos): {valor_final}"

# Função sendo chamada
calculadora_anuncios(valor_em_reais)