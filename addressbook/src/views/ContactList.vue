<template>
  <div>
    <h1>Home Page</h1>
    <button v-on:click="getData">Fetch Data</button>
    <h3>Contacts List</h3>
    <ul>
      <li v-for="c in contacts" :key="c.ID">
        {{ c.FIRST_NAME }}
      </li>
    </ul>
  </div>
</template>

<script>
// @ is an alias to /src
//import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: "ContactList",
  components: {},
  data: function () {
    return {
      contacts: null,
    };
  },
  methods: {
    getData: function () {
      fetch("http://127.0.0.1:5000/api/v1/resources/contacts/all")
        .then((response) => response.json())
        .then((contacts) => (this.contacts = contacts));
    },
  },
};
</script>
