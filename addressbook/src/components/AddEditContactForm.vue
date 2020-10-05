<template>
  <v-dialog v-model="dialog" persistent scrollable max-width="400px">
    <template v-slot:activator="{ on, attrs }">
      <v-btn
        v-if="isNewContact"
        color="green"
        fab
        dark
        v-bind="attrs"
        v-on="on"
      >
        <v-icon>mdi-plus</v-icon>
      </v-btn>
      <v-btn
        v-else
        color="blue"
        fab
        dark
        class="mx-2"
        x-small
        v-bind="attrs"
        v-on="on"
      >
        <v-icon dark>
          mdi-pen
        </v-icon>
      </v-btn>
    </template>
    <v-card elevation="9">
      <v-card-title>
        <span v-if="isNewContact" class="headline">NEW CONTACT</span>
        <span v-else class="headline">EDIT CONTACT</span>
      </v-card-title>
      <v-divider></v-divider>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col cols="12" sm="12" md="12">
              <v-text-field
                label="First Name *"
                required
                dense
                v-model="Contact.FIRST_NAME"
              ></v-text-field>
            </v-col>

            <v-col cols="12" sm="12" md="12">
              <v-text-field
                label="Last Name *"
                required
                dense
                v-model="Contact.LAST_NAME"
              ></v-text-field>
            </v-col>
            <v-col cols="12" sm="6" md="6">
              <v-text-field
                label="Work Phone *"
                required
                dense
                v-model="Contact.WORK_PHONE"
              ></v-text-field>
            </v-col>
            <v-col cols="12" sm="6" md="6">
              <v-text-field
                label="Cell Phone *"
                required
                dense
                v-model="Contact.CELL_PHONE"
              ></v-text-field>
            </v-col>
            <v-col cols="12" sm="6" md="6">
              <v-text-field
                label="Email*"
                required
                dense
                v-model="Contact.EMAIL"
              ></v-text-field>
            </v-col>

            <!-- START - birthdate with date picker -->

            <v-col cols="12" sm="6" md="6">
              <v-dialog
                ref="dialog"
                v-model="modal"
                :return-value.sync="Contact.BIRTHDATE"
                persistent
                width="290px"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                    v-model="Contact.BIRTHDATE"
                    label="Birthdate *"
                    prepend-icon="mdi-calendar"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                    dense
                  ></v-text-field>
                </template>
                <v-date-picker v-model="Contact.BIRTHDATE" scrollable>
                  <v-spacer></v-spacer>
                  <v-btn text color="primary" @click="modal = false" small>
                    Cancel
                  </v-btn>
                  <v-btn
                    text
                    color="primary"
                    @click="$refs.dialog.save(Contact.BIRTHDATE)"
                    small
                  >
                    OK
                  </v-btn>
                </v-date-picker>
              </v-dialog>
            </v-col>

            <!-- END - birthdate with date picker -->

            <!-- START - Address Section-->

            <v-col cols="12" sm="12" md="12">
              <v-text-field
                label="Street Address *"
                required
                v-model="Contact.STREET_ADDRESS"
              ></v-text-field>
            </v-col>

            <v-col cols="12" sm="12" md="4">
              <v-text-field
                label="City *"
                required
                v-model="Contact.CITY"
              ></v-text-field>
            </v-col>

            <v-col cols="12" sm="12" md="4">
              <v-text-field
                label="State *"
                required
                v-model="Contact.STATE"
              ></v-text-field>
            </v-col>

            <v-col cols="12" sm="12" md="4">
              <v-text-field
                label="ZIP *"
                required
                v-model="Contact.ZIP"
              ></v-text-field>
            </v-col>

            <!-- END - Address Section-->

            <v-col cols="12" sm="12" md="12">
              <v-textarea label="Notes" v-model="Contact.NOTE"></v-textarea>
            </v-col>
          </v-row>
        </v-container>
        <small>*indicates required field</small>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="dialog = false">
          Close
        </v-btn>
        <v-btn color="blue darken-1" text @click="updateContact">
          Save
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
export default {
  name: "AddEditContactForm",
  props: {
    contact: {
      type: Object,
    },
    isNewContact: Boolean,
  },
  data: function() {
    return {
      Contact: { ...this.contact },
      // date: new Date().toISOString().substr(0, 10),
      dialog: false,
      modal: false,
    };
  },
  methods: {
    updateContact: function() {
      this.dialog = false;
      //   console.log("Contact.BIRTHDATE: " + this.Contact.BIRTHDATE);
      //   console.log("date: " + this.date);
    },
  },
};
</script>
