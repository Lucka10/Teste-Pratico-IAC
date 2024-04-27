<script setup lang="ts">
import { ref } from 'vue'
import type { Ref } from 'vue'
import HelloWorld from './components/HelloWorld.vue'
import Contact from './components/Contact.vue'
import axios, { type AxiosResponse } from 'axios';

interface contato {
  id:number
  nome:string
  email:string
  telefone:number
  date:string
}

const data: Ref<contato[]> = ref([])

const alfabetica = function(a:contato,b:contato){
    let nameA = a.nome.toLowerCase(); 
    let nameB = b.nome.toLowerCase();
    if (nameA < nameB) return -1;
    if (nameA > nameB) return 1;
    return 0;
}

axios.get('http://127.0.0.1:8000/agenda')
.then( (response:AxiosResponse) => {
  if (response.status == 200) {
    response.data.sort(alfabetica)
    response.data.forEach( (element:contato) => {
      console.log(element)

      data.value.push(element)
      
    });
  }
})
.catch((response:AxiosResponse) => { 
  console.log('deu ruim',response)
}) 

const id = ref()
const nome = ref('')
const email = ref('')
const telefone = ref()
const date = ref('')
const foto = ref()

const inputTelefone = ref()


const showmodal = ref(false)
const titulo = ref('')
const novo_contato = function(title:string,edit?:contato) {
  showmodal.value = !showmodal.value
  if (title) {
    titulo.value = title
  }
  if (edit) {
    id.value = edit.id
    nome.value = edit.nome
    email.value = edit.email
    telefone.value = edit.telefone
    date.value = edit.date
    }
  else {
    id.value = '',
    nome.value = ''
    email.value = ''
    telefone.value = ''
    date.value = ''
  }
}

function getCSRFTokenFromCookies() {
  const cookies = document.cookie.split(";")
  console.log(cookies)
  for (const cookie of cookies) {
    const [name, value] = cookie.split("=");
    if (name === "csrftoken") { // Replace "csrf_token" with the actual name of your CSRF token cookie
      console.log(name)
      return decodeURIComponent(value);
    }
  }
  console.log('token não existe')
  return null; // CSRF token not found
}
getCSRFTokenFromCookies()


const criar_contato = function() { 
  if (nome.value.length == 0) {
    console.log('nome invalido')
  }
  if (email.value.length == 0) {
    console.log('email invalido')
  }
  if (telefone.value.length < 11) {
    console.log('telefone invalido')
  }
  if (date.value === '') {
    console.log('sem data')
  }
  if (foto.value.files) {
    console.log(foto.value.files)
    console.log('SEM FOTO')
  }

  if (id.value) {
    axios.post('http://127.0.0.1:8000/agenda/novo/', 
      {
      id: id.value,
      nome: nome.value,
      email: email.value,
      telefone: telefone.value,
      date: date.value,
      }
    )
    .then((response) => {
      console.log("RESPOSTA AQUI:", response)
      showmodal.value = false 
      window.location.reload()
      }
    ) 
    
  } else {
    axios.post('http://127.0.0.1:8000/agenda/novo/', 
      {
      nome: nome.value,
      email: email.value,
      telefone: telefone.value,
      date: date.value,
      }
    )
    .then((response) => {
      console.log("RESPOSTA AQUI:", response)
      data.value.push(response.data)
      data.value.sort(alfabetica)
      
      }
    )   
  }
}


const excluido = ref(false)

</script>

<template>
  <header class="d-flex flex-wrap justify-content-center py-3 ">
    <h1 class="fw-bold fw-bold text-body-emphasis" >Agenda de Contatos</h1>
  </header>

  <div class="bg-info high-z-index position-fixed top-0 w-100 h-100 d-flex justify-content-center align-items-center"
    v-if="showmodal">
    
    <div class="bg-white border bw-1 b-color-gray d-flex flex-wrap w-50"> 

      <div class="w-100 d-flex align-self-start justify-content-between px-3 py-2  border-bottom bw-3">
        <h3 class="mb-0">{{ titulo }}</h3> 
        <button class="close btn bi bi-x" @click="novo_contato('')"></button>
      </div>

      <form class="container needs-validation p-3 d-flex flex-column gap-2">  
        <div class="d-flex no-wrap gap-4"> 
          <div class="d-flex no-wrap flex-grow-1">
            <label class= "fw-bold  d-flex align-self-center" for=nome>Nome:</label>
            <input type="text" class="form-control p-1" id="nome" 
            v-model="nome"
            required>
          </div>
          
          <div class="d-flex no-wrap flex-grow-1">
            <label class= "fw-bold  d-flex align-self-center" for=nome>Email:</label>
            <input type="email" class="form-control p-1" id="email" 
            v-model="email">
          </div>
        </div>
        <div class="d-flex no-wrap gap-4"> 
          <div class="d-flex no-wrap flex-grow-1">
            <label class= "fw-bold d-flex align-self-center" for=tele>Telefone:</label>
            <input type="text" class="form-control p-1" id="tele" v-model="telefone"
            ref="inputTelefone"
            >
          </div>

          <div class="d-flex no-wrap flex-grow-1" >
            <label class="fw-bold" for=data>Data de Nascimento:</label>
            <input type="date" class="form-control p-1" id="data" v-model="date">
          </div>
        </div>
        
        <div class="d-flex no-wrap">
          <label class= "fw-bold" for=image>Foto:</label>
          <input type="file" class="form-control p-1" id="image" ref="foto"
          accept=".png,.jpg,.svg,.webp">
        </div>
      </form> 

      <div class="w-100 d-flex align-self-end justify-content-between align-items-center p-3 border-top  bw-3">
        <button class="btn btn-danger fw-bold " @click="novo_contato('')">Cancelar</button>
        <button type='submit' class="btn btn-success bi bi-plus-lg" @click="criar_contato()">Salvar</button>
      </div>
      
    </div>

  </div>

  <div class="bg-transparent high-z-index position-fixed top-0 w-100 h-100 d-flex justify-content-center align-items-center"
    v-if="excluido">
    <div class="bg-white border bw-1 b-color-gray d-flex flex-wrap w-50" @click="excluido=false"> 
      Excluido com sucesso
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
          :id="contato.id"
          :nome="contato.nome"
          :email="contato.email"
          :telefone="contato.telefone"
          :data="contato.date"
          src="/src/assets/profilebase.jpeg"
          @novo_contato="(msg) => {novo_contato('Editar ' + msg ,contato)}"
          @response="(response) =>{console.log(response);excluido=response[0];data.splice(response[1],1)}"
      ></Contact>
      </div>
      
    </div>

  </div>

  
</template>

<style scoped>
</style>
