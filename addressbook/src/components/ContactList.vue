<template>
  <v-main>
    <v-container>
      <v-row>
        <v-col>
          <h1 class="font-weight-light text-uppercase">Contacts</h1>
          <h6 class="font-weight-light text-uppercase">
            favorite contacts :
            <span> {{ getFavoriteContacts }}</span>
          </h6>
        </v-col>

        <v-col class="text-right" align-self="end">
          <AddEditContactForm v-bind:isNewContact="true"></AddEditContactForm>
        </v-col>
      </v-row>
    </v-container>
    <v-divider></v-divider>
    <ContactListItem
      v-for="c in this.contacts"
      :key="c.ID"
      v-bind:contact="c"
      v-on:UpdateFavoriteContact="updateFavoriteContact($event)"
      v-on:DeleteContact="deleteContact($event)"
    ></ContactListItem>
  </v-main>
</template>

<script>
import ContactListItem from "@/components/ContactListItem.vue";
import AddEditContactForm from "@/components/AddEditContactForm.vue";
export default {
  components: {
    ContactListItem,
    AddEditContactForm,
  },
  data: function() {
    return {
      contacts: [],
    };
  },
  methods: {
    getData: function() {
      fetch("http://192.168.1.6:5000/api/v1/resources/contacts/all", {
        method: "GET",
      })
        .then((response) => response.json())
        .then((contacts) => (this.contacts = contacts));
    },
    updateFavoriteContact: function(id) {
      fetch(
        "http://192.168.1.6:5000/api/v1/resources/contacts/updateFavoriteContact/" +
          id,
        {
          method: "POST",
        }
      )
        .then((response) => response.json())
        .then((contacts) => (this.contacts = contacts));
    },
    deleteContact: function(id) {
      fetch(
        "http://192.168.1.6:5000/api/v1/resources/contacts/deleteContact/" + id,
        {
          method: "POST",
        }
      )
        .then((response) => response.json())
        .then((contacts) => (this.contacts = contacts));
    },
  },
  beforeMount() {
    this.getData();
  },
  computed: {
    getFavoriteContacts: function() {
      var favoriteContacts = 0;
      this.contacts.forEach((contact) => {
        if (contact.FAVORITE == 1) favoriteContacts += 1;
      });
      return favoriteContacts;
    },
  },
};
</script>
