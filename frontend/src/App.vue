<script setup lang="ts">
import { ref } from 'vue'
import HelloWorld from './components/HelloWorld.vue'
import Contact from './components/Contact.vue'

const data = ref([
  {nome: 'teste', email:'teste@teste',telefone:'12313131',date:'12/12/1977'},
  {nome: 'teste1', email:'teste@teste',telefone:'555555',date:'31/11/2023'},
  {nome: 'teste2', email:'teste@teste',telefone:'4444',date:'11/8/222'},
  {nome: 'teste3', email:'teste@teste',telefone:'76755675',date:'24/7/4645'},
  {nome: 'teste3', email:'teste@teste',telefone:'1231231231443',date:'27/5/2000'},
]
)
</script>

<template>
  <header class="d-flex flex-wrap justify-content-center py-3 ">
    <h1 class="fw-bold fw-bold text-body-emphasis" >Agenda de Contatos</h1>
  </header>

  <div class="container"> 
    <div class="container d-flex justify-content-between">
      <h2 class="fw-bold text-body-emphasis">Contatos Cadastrados</h2>
      <button class="btn btn-success rounded px-3 mb-2" >
        <img src="/src/assets/whiteplus.png" width="10px" height="10px">
        Novo
      </button>
    </div>
    <div class="container">
      <div class="mb-3" v-for="contato,key in data" >
        <Contact :numero="key+1"
          :nome="contato.nome"
          :email="contato.email"
          :telefone="contato.telefone"
          :date="contato.date"
      ></Contact>
      </div>

      
    </div>

  </div>

  
</template>

<style scoped>
</style>
