<script setup>
import { ref } from "vue";
const products = ref(null);
const name = defineModel("name")
const quantity = defineModel("quantity")
async function getProducts() {
    const response = await fetch(
        "http://127.0.0.1:8000/getProducts",
        {
            method: "POST",
            headers: {
                //Accept: 'application/json',
                "Content-Type": "application/json",
                //"Access-Control-Allow-Origin": "http://0.0.0.0"
            },
            credentials: "include",
            mode: "cors",
            //body: JSON.stringify({ login: login.value, password: password.value })
        }
    );
    return await response.json()
}

async function addProduct() {
    const response = await fetch(
        "http://127.0.0.1:8000/addProduct",
        {
            method: "POST",
            headers: {
                //Accept: 'application/json',
                "Content-Type": "application/json",
                //"Access-Control-Allow-Origin": "http://0.0.0.0"
            },
            credentials: "include",
            mode: "cors",
            body: JSON.stringify({ name: name.value, quantity: quantity.value })
        }
    );
    products.value = await getProducts();
}

async function deleteAll() {
    const response = await fetch(
        "http://127.0.0.1:8000/deleteAll",
        {
            method: "POST",
            headers: {
                //Accept: 'application/json',
                "Content-Type": "application/json",
                //"Access-Control-Allow-Origin": "http://0.0.0.0"
            },
            credentials: "include",
            mode: "cors",
        }
    );
    products.value = await getProducts();
}

products.value = await getProducts();
</script>

<template>
  <div class="flexBox">
      <div class="leftBlock">
        <form @submit.prevent class="formBlock">
            <input v-model="name" type="text" placeholder="name" required class="glow-on-hover">
            <input v-model="quantity" placeholder="quantity" type="text" class="glow-on-hover">
            <button @click="addProduct" class="glow-on-hover">Добавить в список продуктов</button>
          <button @click="deleteAll" class="glow-on-hover">Удалить все</button>

          </form>
      </div>
        <div class="blocktext">
          <div v-for="item in products" >

            <p class="ptext">{{ item.name }}  {{ item.quantity }} шт.</p>

          </div>
        </div>

  </div>



</template>
<style>
  .blocktext {
    margin: auto;
    width: 20%
  }
  .formBlock {
    padding-bottom: 15px;
  }
  .ptext {
    font-size: 24px;
  }
  .flexBox {
    display: flex;
  }
  .leftBlock {
    margin: auto;
    width: 20%;
  }
.glow-on-hover {
    width: 220px;
    height: 50px;
    border: none;
    outline: none;
    color: #fff;
    background: #111;
    cursor: pointer;
    position: relative;
    z-index: 0;
    border-radius: 10px;
}

.glow-on-hover:before {
    content: '';
    background: linear-gradient(45deg, #ff0000, #ff7300, #fffb00, #48ff00, #00ffd5, #002bff, #7a00ff, #ff00c8, #ff0000);
    position: absolute;
    top: -2px;
    left:-2px;
    background-size: 400%;
    z-index: -1;
    filter: blur(5px);
    width: calc(100% + 4px);
    height: calc(100% + 4px);
    animation: glowing 20s linear infinite;
    opacity: 0;
    transition: opacity .3s ease-in-out;
    border-radius: 10px;
}

.glow-on-hover:active {
    color: #000
}

.glow-on-hover:active:after {
    background: transparent;
}

.glow-on-hover:hover:before {
    opacity: 1;
}

.glow-on-hover:after {
    z-index: -1;
    content: '';
    position: absolute;
    width: 100%;
    height: 100%;
    background: #111;
    left: 0;
    top: 0;
    border-radius: 10px;
}

@keyframes glowing {
    0% { background-position: 0 0; }
    50% { background-position: 400% 0; }
    100% { background-position: 0 0; }
}
</style>