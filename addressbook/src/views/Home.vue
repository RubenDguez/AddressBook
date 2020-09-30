<template>
  <div>
    <ContactList />
  </div>
</template>

<script>
// @ is an alias to /src
import ContactList from '@/components/ContactList.vue'

export default {
  name: "Home",
  components: {
    ContactList
  },
};
</script>
