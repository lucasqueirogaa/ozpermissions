# Manual do Bot de Gerenciamento de Canais

## 🤖 O que é este bot?

Este bot foi criado por Lucas Queiroga para facilitar o gerenciamento de canais privados no Discord do OZMap. Com ele, você pode:

- Adicionar pessoas a canais privados
- Remover pessoas de canais privados
- Gerenciar acessos de forma simples usando comandos

## 🚀 Começando

### 1. Adicionando o Bot ao Servidor

1. Clique <a href="https://discord.com/oauth2/authorize?client_id=1305490732605374535&permissions=268504080&integration_type=0&scope=bot+applications.commands" target="_blank">neste link</a> para convidar o bot
2. Selecione o servidor onde deseja adicionar o bot
3. Clique em "Autorizar"
4. Complete a verificação do CAPTCHA se solicitado

### 2. Configurando Permissões

O bot funciona com um sistema de cargos (roles). Por padrão, você precisa:

1. Criar um cargo para controle:
   ```
   👉 Servidor > Configurações > Cargos > Criar Cargo
   Nome sugerido: "channel_manager"
   ```
2. Dar este cargo para quem poderá usar o bot:
   ```
   👉 Clique com botão direito no usuário > Cargos > Selecione "channel_manager"
   ```
3. No código do bot, o cargo permitido está definido em:
   ```python
   CARGOS_PERMITIDOS = ["channel_manager"]
   ```
   Você pode mudar este nome para qualquer outro de sua preferência!

## 📋 Usando o Bot

### Comandos Básicos

#### Adicionar Alguém:

```
!adicionar @lucas_queiroga
```

- Use este comando no canal onde quer adicionar a pessoa
- Mencione o usuário usando @
- Exemplo: `!adicionar @lucas_queiroga`

#### Remover Alguém:

```
!remover @lucas_queiroga
```

- Use este comando no canal onde quer remover a pessoa
- Mencione o usuário usando @
- Exemplo: `!remover @lucas_queiroga`

## ⚠️ Avisos e Erros Comuns

### O bot vai te avisar quando:

1. Você não tiver permissão
   ```
   ❌ Você não tem permissão para usar este comando!
   ```
2. Faltar mencionar o usuário
   ```
   ❌ Mencione o usuário! Exemplo: !adicionar @usuário
   ```
3. O usuário já estiver no canal
   ```
   ❌ Este usuário já tem acesso ao canal!
   ```
4. O usuário já estiver removido
   ```
   ❌ Este usuário já não tem acesso ao canal!
   ```

## 🔒 Segurança

### O que o bot NÃO permite:

- Usar @everyone ou @here
- Adicionar o mesmo usuário duas vezes
- Usar comandos sem ter o cargo correto

### O que o bot PERMITE:

- Adicionar usuários individuais
- Remover usuários individuais
- Ver feedback de todas as ações

## 💡 Dicas e Truques

1. **Mencionando Usuários**

   - Comece digitando @ e as primeiras letras do nome
   - Selecione o usuário da lista que aparece
   - Certifique-se que o nome ficou azul/destacado

2. **Canais Corretos**

   - Use os comandos dentro do canal que quer gerenciar
   - Verifique se o bot tem acesso ao canal

3. **Permissões**
   - O bot precisa ter permissões no canal
   - Os usuários precisam ter o cargo correto

## ❓ Problemas Comuns

### "Não consigo usar os comandos"

✅ Verifique se:

- Você tem o cargo correto
- Está usando @ para mencionar
- O bot está online

### "O bot não responde"

✅ Verifique se:

- O bot está online (deve aparecer na lista de membros)
- Você está usando o comando correto
- O bot tem permissões no canal

### "Não consigo adicionar alguém"

✅ Verifique se:

- A pessoa não está já no canal
- Você mencionou corretamente
- O bot tem permissões de gerenciar o canal

## 📞 Precisa de Ajuda?

Se encontrar algum problema:

1. Verifique se seguiu todos os passos
2. Confira as permissões
3. Tente remover e adicionar o usuário novamente
4. Entre em contato com Lucas Queiroga
