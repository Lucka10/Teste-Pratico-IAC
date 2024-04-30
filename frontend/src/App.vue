<script setup lang="ts">
import { ref } from 'vue'
import type { Ref } from 'vue'
import Contact from './components/Contact.vue'
import axios, { type AxiosResponse } from 'axios';
import Notificacao from './components/Notificacao.vue';

interface contato {
  id:number
  nome:string
  email:string
  telefone:string
  date:string
  foto:string
}


const alfabetica = function(a:contato,b:contato){
    let nameA = a.nome.toLowerCase(); 
    let nameB = b.nome.toLowerCase();
    if (nameA < nameB) return -1;
    if (nameA > nameB) return 1;
    return 0;
}


const text:Ref<[string,boolean][]> = ref([])
const notify = function(mensagem:string,alerta?=false)
{
  text.value.push([mensagem,alerta])
  setTimeout(()=> {text.value = text.value.slice(1)}, 3000);
}


const data: Ref<contato[]> = ref([])
axios.get('http://127.0.0.1:8000/agenda')
.then( (response:AxiosResponse) => {
  console.log(response)
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

const formu = ref()
const inputTelefone = ref()

const mascara = function() 
{
  if (telefone.value.length <= 11){
    var value = telefone.value.replace(/\D/g, '');
    var formattedValue = '';
    
    if (value.length > 0) {
      formattedValue = '(' + value.substring(0, 2);
    }
    if (value.length > 2) {
      formattedValue += ') ' + value.substring(2, 7);
    }
    if (value.length > 7) {
      formattedValue += '-' + value.substring(7, 11);
    }
    
    telefone.value = formattedValue;
  } else {
    telefone.value = telefone.value.substring(0,15)
  }
}
const validaremail = function(){
  if (!email.value.includes('@') || email.value.length > 140) {
    return false
  }
  const userdomain = email.value.split('@')
  if (userdomain.length > 2){
    return false
  }
  const user = userdomain[0]
  const domain = userdomain.slice(1)

  if (user.length === 0){
    console.log('EMAIL: ERROR user vazio')
    return false
  }
  console.log(domain)
  if (domain[0].length === 0){
    console.log('EMAIL: ERROR domain vazio')
    return false  
  } 
  return true
}


const showmodal = ref(false)
const titulo = ref('')
const novo_contato = function(title:string,edit?:contato,mascara?:string) {
  showmodal.value = !showmodal.value
  if (title) {
    titulo.value = title
  }
  if (edit) {
    id.value = edit.id
    nome.value = edit.nome
    email.value = edit.email
    telefone.value = mascara
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

const alterado = ref(false)

const validarformulario = function(){
  if (nome.value.length == 0) {
    notify('Nome vazio',true)
    return false
  }
  if (email.value.length == 0 || !validaremail()) {
    notify('email invalido',true)
    return false
  }
  if (telefone.value.length < 15) {
    notify('Telefone invalido',true)
    return false
  }
  if (date.value === '') {
    notify('Data invalida',true)
    return false
  }
  if (!foto.value.files[0] && !id.value) {
    notify('Escolha uma foto',true)
    return false
  }
  return true
}

const criar_contato = function() { 
  if (!validarformulario()) {
    console.log('CRIAÇÃO INTERROMPIDA')
    return
  }
  telefone.value = telefone.value.replace(/\D/g, '');
  if (id.value) {

    axios.put('http://127.0.0.1:8000/agenda/', 
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
      const editado = data.value.find(contato => contato.id === id.value)
      if (editado) {
        editado.nome = nome.value
        editado.email = email.value
        editado.telefone = telefone.value
        editado.date = date.value
      }
      showmodal.value = false 
      notify('Atualizado com sucesso!')
      }
    ) 
    if (foto.value.files[0]){
      const form = new FormData()
      form.append('id',id.value)
      form.append('foto', foto.value.files[0])
      console.log('mudou a foto');
      axios.post('http://127.0.0.1:8000/agenda/fotos/', 
      form,
      {headers: {
        'Content-Type': 'multipart/form-data'
      }}
      ).then((response) => {
        const editado = data.value.find(contato => contato.id === id.value)
        if (editado) {
          console.log('EDITANDO FOTOS: ',response.data)
          editado.foto = response.data
        }
        showmodal.value = false 
        notify('Atualizado com sucesso!')
      }

      )
    }
    
  } else {
    
    console.log(JSON.stringify({
      nome: nome.value,
      email: email.value,
      telefone: telefone.value,
      date: date.value,
      }))

      const form = new FormData(formu.value)
      form.append('nome',nome.value)
      form.append('email', email.value)
      form.append('telefone', telefone.value)
      form.append('date', date.value)
      form.append('foto',foto.value.files[0])
      console.log(form)
    axios.post('http://127.0.0.1:8000/agenda/', 
      form,{
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        }//{headers:{'X-CSRFToken': csrftoken}}
    )
    .then((response) => {
      console.log("RESPOSTA AQUI:", response)
      data.value.push(response.data)
      data.value.sort(alfabetica)
      showmodal.value = false
      notify('Criado com sucesso!')
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

  <div class="blurred-background high-z-index position-fixed top-0 w-100 h-100 d-flex justify-content-center align-items-center"
    v-if="showmodal">
    
    <div class="bg-white border bw-1 b-color-gray d-flex flex-wrap w-50"> 

      <div class="w-100 d-flex align-self-start justify-content-between px-3 py-2  border-bottom bw-3">
        <h3 class="mb-0">{{ titulo }}</h3> 
        <button class="close btn bi bi-x" @click="novo_contato('')"></button>
      </div>

      <form ref='formu' class="container needs-validation p-3 d-flex flex-column gap-2">  
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
            @input="mascara()"
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
          accept=".png,.jpg,.svg">
        </div>
      </form> 

      <div class="w-100 d-flex align-self-end justify-content-between align-items-center p-3 border-top  bw-3">
        <button class="btn btn-danger fw-bold " @click="novo_contato('')">Cancelar</button>
        <button type='submit' class="btn btn-success bi bi-plus-lg" @click="criar_contato()">Salvar</button>
      </div>
      
    </div>

  </div>

  <div class="blurred-background high-z-index position-fixed top-0 w-100 h-100 d-flex justify-content-center align-items-center"
    v-if="excluido">
    <div class="bg-success fw-bold d-flex justify-content-center align-items-center border border-3 border-dark rounded p-2 w-50 h-25" @click="excluido=false"> 
      <h3>Excluido com sucesso!</h3>
    </div>
  </div>

  <div class="position-fixed top-0 end-0">
    <Notificacao 
    v-for="notifica,k in text"
    :alerta="notifica[1]"
    :text="notifica[0]"
    :id=k
    @fechar="() => text.splice(k,1)"> 
    </Notificacao>
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
          :src="'http://127.0.0.1:8000' + contato.foto"
          @editar="(msg) => {novo_contato('Editar ' + msg[0] ,contato,msg[1])}"
          @excluir="(response) =>{console.log(response);notify('Excluido com sucesso');data.splice(response[1],1)}"
      ></Contact>
      </div>
      
    </div>

  </div>

  
</template>

<style scoped>
.blurred-background {
 
  background-color: transparent;
  backdrop-filter: blur(10px);
}
</style>
