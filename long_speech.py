tab1 = ["Caros colegas", "Por outro lado", "Assim mesmo", "Não poderemos esquecer que", "Do mesmo modo",
        "A prática mostra que", "Nunca é demais insistir, uma vez que", "A experiência mostra que",
        "É fundamental ressaltar que", "O incentivo ao avançar tecnológico, assim como"]
tab2 = ["a execução deste processo", "a complexidade dos estudos efectuados", "a expansão da nossa actividade",
        "a actual estrutura da organização", "o novo modelo estrutural aqui preconizado",
        "o desenvolvimento de formas distintas de actuação", "a constante divulgação das informações",
        "a consolidação das estruturas", "a análise dos diversos resultados",
        "o inicio do programa de formação de atitudes"]
tab3 = ["obriga-nos à análise", "cumpre um papel essencial de formação", "exige a precisão e a definição",
        "auxilia a preparação e a definição", "contribui para a correcta determinação",
        "assume a importante posição na definição", "facilita a definição", "prejudica a percepção da importância",
        "oferece uma oportunidade de verificação", "accareta um processo de reformulação"]
tab4 = ["das nossas opções de desenvolvimento no futuro", "das nossas metas financeiras e administrativas",
        "dos conceitos de participação geral", "das atitudes e das atribuições da directoria", "das novas proposições",
        "das opções básicas para o sucesso do programa", "do nosso sistema de formação de quadros", "das condições apropriadas para os negócios", "dos índices pretendidos", "das formas de acção   "]

for word1 in tab1:
    for word2 in tab2:
        for word3 in tab3:
            for word4 in tab4:
                print(word1 + " " + word2 + " " + word3 + " " + word4)
