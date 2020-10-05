<template>
  <v-app>
    <v-app-bar
      absolute
      color="rgba(55,100,186,1)"
      dark
      shrink-on-scroll
      prominent
      src="@/imgs/nav-bar-main-pic.jpg"
      fade-img-on-scroll
      scroll-target="#scrolling-techniques-5"
      scroll-threshold="500"
    >
      <template v-slot:img="{ props }">
        <v-img
          v-bind="props"
          gradient="to top right, rgba(55,100,186,.7), rgba(25,32,72,.7)"
        ></v-img>
      </template>

      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title class="text-uppercase">Address Book</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-app-bar>
    <v-sheet
      id="scrolling-techniques-5"
      class="overflow-y-auto"
      max-height="700"
    >
      <div class="main-view">
        <v-main>
          <router-view></router-view>
        </v-main>
      </div>
    </v-sheet>
    <v-footer absolute dark class="font-weight-medium" color="blue darken-2">
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
export default {
  name: "App",

  components: {},

  data: () => ({
    //
  }),
};
</script>

<style>
.main-view {
  margin-top: 200px;
  margin-left: auto;
  margin-right: auto;
  max-width: 650px;
}
</style>

// color="#43a047"
