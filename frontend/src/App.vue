<script setup lang="ts">
import { ref } from 'vue'
import HelloWorld from './components/HelloWorld.vue'
import Contact from './components/Contact.vue'
import axios from 'axios';


axios.get('http://127.0.0.1:8000/agenda')
.then( (msg:string) => console.log('GET:',msg))



const data = ref([
  {nome: 'teste', email:'teste@teste',telefone:'12313131',date:'12/12/1977'},
  {nome: 'teste1', email:'teste@teste',telefone:'555555',date:'31/11/2023'},
  {nome: 'teste2', email:'teste@teste',telefone:'4444',date:'11/8/222'},
  {nome: 'teste3', email:'teste@teste',telefone:'76755675',date:'24/7/4645'},
  {nome: 'teste3', email:'teste@teste',telefone:'1231231231443',date:'27/5/2000'},
]
)




const showmodal = ref(false)
const titulo = ref('')
const novo_contato = function(title:string) {
  showmodal.value = !showmodal.value
  if (title) {
    titulo.value = title
  }
}

const dados = ref({
  nome:'',
  email:'',
  telefone:'',
  nasc:'',
})




const criar_contato = function() { 
  console.log(dados.value)
  axios.post('http://127.0.0.1:8000/agenda/novo', dados.value)
  .then((response) => {
    console.log("RESPOSTA AQUI:", response)
  })
}


</script>

<template>
  <header class="d-flex flex-wrap justify-content-center py-3 ">
    <h1 class="fw-bold fw-bold text-body-emphasis" >Agenda de Contatos</h1>
  </header>

  <div class="bg-info high-z-index position-fixed top-0 w-100 h-100 d-flex justify-content-center align-items-center"
    v-if="showmodal">
    
    <div class="bg-white border bw-1 b-color-gray d-flex flex-wrap"> 

      <div class="w-100 d-flex align-self-start justify-content-between px-3 py-2  border-bottom bw-3">
        <h3 class="mb-0">{{ titulo }}</h3> 
        <button class="close btn bi bi-x" @click="novo_contato('')"></button>
      </div>

      <form class="container needs-validation p-3 d-flex flex-column gap-2">  
        <div class="d-flex no-wrap gap-4"> 
          <div class="d-flex no-wrap flex-grow-1">
            <label class= "fw-bold  d-flex align-self-center" for=nome>Nome:</label>
            <input type="text" class="form-control p-1" id="nome" 
            v-model="dados.nome"
            @input="console.log(dados)">
          </div>
          
          <div class="d-flex no-wrap flex-grow-1">
            <label class= "fw-bold  d-flex align-self-center" for=nome>Email:</label>
            <input type="email" class="form-control p-1" id="email" 
            v-model="dados.email">
          </div>
        </div>
        <div class="d-flex no-wrap gap-4"> 
          <div class="d-flex no-wrap flex-grow-1">
            <label class= "fw-bold d-flex align-self-center" for=tele>Telefone:</label>
            <input type="text" class="form-control p-1" style="width:14em;" id="tele" v-model="dados.telefone">
          </div>

          <div class="d-flex no-wrap flex-grow-1" >
            <label class="fw-bold" for=data>Data de Nascimento:</label>
            <input type="date" class="form-control p-1" id="data" v-model="dados.nasc">
          </div>
        </div>
        
        <div class="d-flex no-wrap">
          <label class= "fw-bold" for=image>Foto:</label>
          <input type="file" class="form-control p-1" id="image"
          accept=".png,.jpg,.svg,.webp">
        </div>
      </form> 

      <div class="w-100 d-flex align-self-end justify-content-between align-items-center p-3 border-top  bw-3">
        <button class="btn btn-danger fw-bold " @click="novo_contato('')">Cancelar</button>
        <button class="btn btn-success bi bi-plus-lg" @click="criar_contato()">Salvar</button>
      </div>
    </div>

  </div>

  
  <div class="container"> 
    <div class="container d-flex justify-content-between">
      <h2 class="fw-bold text-body-emphasis">Contatos Cadastrados</h2>
      <button class="btn btn-success rounded px-3 mb-2" @click="novo_contato('Novo Contato')">
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
          src="/src/assets/profilebase.jpeg"
          @novo_contato="(msg) => {novo_contato('Editar ' + msg)}"
      ></Contact>
      </div>
''
      
    </div>

  </div>

  
</template>

<style scoped>
</style>
