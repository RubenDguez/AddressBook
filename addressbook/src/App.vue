<template>
  <v-app>
    <AppBar></AppBar>
    <v-sheet
      id="scrolling-techniques-5"
      class="overflow-y-auto"
      max-height="800px"
    >
      <div class="main-view">
        <v-main>
          <router-view></router-view>
        </v-main>
      </div>
    </v-sheet>
    <v-footer app dark class="font-weight-medium" color="blue darken-2">
      <v-row no-gutters>
        <v-col class="text-center" cols="12" sm="6">
          <p class="my-2">
            {{ new Date().getFullYear() }} —
            <strong>AddressBook</strong>
          </p>
        </v-col>
        <v-col class="text-center" cols="12" sm="6">
          <v-btn class="white--text" small text fab>
            <v-icon>mdi-facebook</v-icon>
          </v-btn>
          <v-btn class="white--text" small text fab>
            <v-icon>mdi-instagram</v-icon>
          </v-btn>
          <v-btn class="white--text" small text fab>
            <v-icon>mdi-youtube</v-icon>
          </v-btn>
          <v-btn class="white--text" small text fab>
            <v-icon>mdi-snapchat</v-icon>
          </v-btn>
        </v-col>
      </v-row>
    </v-footer>
  </v-app>
</template>

<script>
import AppBar from "@/components/app-bar.vue";

export default {
  name: "App",

  components: {
    AppBar,
  },

  data: () => ({
    //
  }),
};
</script>

<style>
.main-view {
  margin-bottom: 50px;
  margin-left: auto;
  margin-right: auto;
  max-width: 650px;
}
</style>

// color="#43a047"
