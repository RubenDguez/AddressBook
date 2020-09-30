<template>
    <v-content>
        <h1 class="font-weight-light text-uppercase">Contacts</h1>
        <v-divider></v-divider>
        <ContactListItem v-bind:contacts=this.contacts></ContactListItem>
    </v-content>
</template>

<script>
import ContactListItem from '@/components/ContactListItem.vue'
export default {
    components: {
        ContactListItem,
    },
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
    beforeMount() {
        this.getData()
    }
    
}
</script>