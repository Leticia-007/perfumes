import streamlit as st
from twilio.rest import Client
st.sidebar.image('logo.png')

tab1,tab2=st.tabs(['femininos','masculinos'])

with tab1:
    femininos = ['glamour','egeo','ilia','her code']
    feminino = st.radio('escolha',femininos,horizontal=True)
    
    col1,col2=st.columns(2)
    with col1:
        st.write('')
        st.image(f'{feminino}.png')
    with col2:
        if feminino == 'glamour':
            st.write('Cheiro:É um perfume feminino clássico,com um perfil floral oriental adocicado e envolvente.')
            st.write('Sensação:sofisticado e romântico,ideal para quem quer transmitir elegância e charme.')
            st.write('Preço: 139.0 R$')
        elif feminino == 'egeo':
            st.write('Cheiro:Um perfume super adocicado gourmand,com uma forte presença de chocolate e baunilha.')
            st.write('sensação:Divertido,doce,jovial e irreverente.Ideal para quem gosta de perfumes bem gourmand,que "dão água na boca".')
            st.write('Preço: 105.79 R$')
        elif feminino == 'ilia':
            st.write('Cheiro:É um floral sofisticado e delicado, que transmite feminilidade com força e suavidade ao mesmo tempo.')
            st.write('sensação:Delicado,feminino,elegante e acolhedor.Ideal para quem gosta de perfumes suaves, mas com personalidade')
            st.write('Preço: 104.8 R$')
        elif feminino == 'her code':
            st.write('Cheiro:É um perfume moderno,marcante e sedutor,com uma pegada oriental floral intensa.')
            st.write('sensação:Sexy,confiante,poderoso.Ideal para eventos,baladas ou encontros,quando se quer deixar uma marca.')
            st.write('Preço: 239.9 R$')
with tab2:


    masculinos = ['essencial','lacoste','aron','mr.grey']
    masculino = st.radio('Escolha', masculinos, horizontal=True)

    col1,col2=st.columns(2)
    with col1:
        st.write('')
        st.image(f'{masculino}.png')
    with col2:
        if masculino == 'essencial':
            st.write('Cheiro:Possui uma fragrância intensa,sofisticada e amadeirada.')
            st.write('sensação:Elegante,marcante,quente e ideal para ocasiões noturnas ou especiais')
            st.write('Preço: 125.0 R$')
        elif masculino == 'lacoste':
            st.write('Cheiro:É um perfume fresco,leve e versátil.')
            st.write('sensação:Refrescante,casual,moderno e ideal para o dia a dia,especialmente em climas quentes.')
            st.write('Preço: 391.46 R$')
        elif masculino == 'aron':
            st.write('Cheiro:Fragrância inspirada em perfis internacionais,com foco no amadeirado aromático.')
            st.write('sensação:Clássico,viril e seguro.Ideal para quem quer algo marcante,mas sem exageros.')
            st.write('Preço: 144.8 R$')
        elif masculino == 'mr.grey':
            st.write('Cheiro:Sedutor,elegante e combinadas a frutas cítricas discretas.')
            st.write('sensação:Fresca como pimenta,madeiradas quente e âmbar,criando um ar sedutor,maduro e sofisticado."perfume inspirado em 50 Tons de Cinza"')
            st.write('Preço: 65.9 R$')

st.markdown('---')

nome = st.text_input('Digite seu nome completo: ')
cpf= st.text_input('Digite seu cpf: ')
nascimento=st.text_input('Sua data de nascimento: ')
endereço=st.text_input('Sua rua:')
bairro=st.text_input('Seu bairro: ')
cidade=st.text_input('Sua cidade: ')
estado=st.text_input('Estado de onde mora: ')
cep=st.text_input('Digite seu cep:')
telefone=st.text_input('Informe seu telefone: ')

opcoes_pagamento = ['Pix', 'Boleto bancária', 'Transferência bancária', 'Carteiras digitais']
opcao_pagamento = st.selectbox('Selecione a opção de pagamento', opcoes_pagamento)
if st.button('Efetuar compra'): 
    
    # Dados da sua conta Twilio
    account_sid = 'AC204f13ac2684fefc3dccc88e7eb7dd55'
    auth_token = '56a55dbb9fa2cac35485b735c263d3b8'

    # Número registrado na sua conta Twilio
    twilio_number = '+16076009556'


    # Número de destino (se for conta trial, precisa estar verificado!)
    destino = f'+55{telefone}'

    client = Client(account_sid, auth_token)

    mensagem = client.messages.create(
        body=f'Olá {nome}! O pedido do seu perfume foi finalizado. Obrigado pela preferência!',
        from_=twilio_number,
        to=destino
    )
    st.write('Sua compra foi efetuada :) ')
