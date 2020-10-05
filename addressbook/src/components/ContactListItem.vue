<template>
  <div>
    <v-list>
      <v-list-item three-line>
        <v-list-item-content>
          <!-- <v-list-item-icon>
            <v-icon>mdi-account</v-icon>
          </v-list-item-icon> -->
          <v-list-item-title>
            {{ contact.FIRST_NAME }}
            {{ contact.LAST_NAME }}
          </v-list-item-title>
          <v-list-item-subtitle>
            {{ contact.STREET_ADDRESS }}, {{ contact.CITY }}
            {{ contact.STATE }} {{ contact.ZIP }}
          </v-list-item-subtitle>
          <v-list-item-subtitle>
            <v-row>
              <v-col>
                <h6 class="text-uppercase">Email</h6>
                <a
                  class="black--text text-caption font-weight-light"
                  :href="`mailto:${contact.EMAIL}`"
                  >{{ contact.EMAIL }}</a
                >
              </v-col>
              <v-col align="right">
                <h6 class="text-uppercase">Work Phone</h6>
                <a
                  class="black--text text-caption font-weight-light"
                  :href="`tel:${contact.WORK_PHONE}`"
                  >{{ contact.WORK_PHONE }}</a
                >
              </v-col>
              <v-col align="right">
                <h6 class="text-uppercase">Cell Phone</h6>
                <a
                  class="black--text text-caption font-weight-light"
                  :href="`tel:${contact.CELL_PHONE}`"
                  >{{ contact.CELL_PHONE }}</a
                >
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <h6 class="text-uppercase">Birthdate</h6>
                <p
                  class="black--text text-caption font-weight-light text-uppercase"
                >
                  {{ contact.BIRTHDATE }}
                </p>
              </v-col>
              <v-col align="right">
                <h6 class="text-uppercase">Notes</h6>
                <p
                  class="black--text text-caption font-weight-light text-uppercase"
                >
                  {{ contact.NOTE }}
                </p>
              </v-col>
            </v-row>
            <v-row>
              <v-spacer></v-spacer>
              <v-col class="text-right">
                <v-btn
                  class="mx-2"
                  :class="contact.FAVORITE ? 'white--text' : ''"
                  fab
                  x-small
                  :color="contact.FAVORITE ? 'purple' : 'lighte-grey'"
                  v-on:click="updateFavoriteContact"
                >
                  <v-icon dark>
                    mdi-heart
                  </v-icon>
                </v-btn>

                <AddEditContactForm
                  v-bind:isNewContact="false"
                  v-bind:contact="contact"
                ></AddEditContactForm>

                <v-btn
                  class="mx-2"
                  fab
                  dark
                  x-small
                  color="red"
                  @click="dialog = true"
                >
                  <v-icon dark>
                    mdi-delete
                  </v-icon>
                </v-btn>

                <v-dialog v-model="dialog" max-width="290">
                  <v-card>
                    <v-card-title class="headline">
                      DELETE CONTACT
                    </v-card-title>

                    <v-card-text class="caption text-uppercase" align="justify">
                      are you sure you want to
                      <span class="font-weight-bold red-text">delete</span>
                      this contact; this action can only be undone contacting
                      your software developer.
                    </v-card-text>

                    <v-card-actions>
                      <v-spacer></v-spacer>

                      <v-btn color="blue darken-1" text @click="dialog = false">
                        Cancel
                      </v-btn>

                      <v-btn color="red darken-1" text @click="deleteContact">
                        Delete
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
              </v-col>
            </v-row>
          </v-list-item-subtitle>
          <v-divider></v-divider>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </div>
</template>

<script>
import AddEditContactForm from "@/components/AddEditContactForm.vue";

export default {
  name: "ContactListItem",
  data: function() {
    return {
      dialog: false,
    };
  },
  components: {
    AddEditContactForm,
  },
  props: {
    contact: {
      type: Object,
    },
  },
  methods: {
    updateFavoriteContact: function() {
      this.$emit("UpdateFavoriteContact", this.contact.ID);
    },
    deleteContact: function() {
      this.$emit("DeleteContact", this.contact.ID);
      this.dialog = false;
    },
  },
};
</script>

<style>
a {
  text-decoration: none;
  color: black;
}
</style>
