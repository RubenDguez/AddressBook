<template>
    <div>

        <v-list>
            <v-list-item three-line v-for="contact in contacts" :key="contact.ID">
                <v-list-item-content>
                    <v-list-item-icon>
                        <v-icon>mdi-account</v-icon>
                    </v-list-item-icon>
                    <v-list-item-title>
                        {{ contact.FIRST_NAME }} 
                        {{ contact.LAST_NAME }}
                    </v-list-item-title>
                    <v-list-item-subtitle>
                        {{ contact.STREET_ADDRESS }}, {{ contact.CITY }} {{ contact.STATE }} {{ contact.ZIP }}
                    </v-list-item-subtitle>
                    <v-list-item-subtitle>
                        <v-row>
                            <v-col>
                                <h6>Email: </h6><a :href="`mailto:${contact.EMAIL}`">{{ contact.EMAIL }}</a>
                            </v-col>
                            <v-col>
                                <h6>Work Phone: </h6><a :href="`tel:${contact.WORK_PHONE}`">{{ contact.WORK_PHONE }}</a>
                            </v-col>
                            <v-col>
                                <h6>Cell Phone: </h6><a :href="`tel:${contact.CELL_PHONE}`">{{ contact.CELL_PHONE }}</a>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col>
                                <h6>Birthdate:</h6><p class="text-caption font-weight-light text-uppercase">{{ contact.BIRTHDATE }}</p>
                            </v-col>
                            <v-col>
                                <h6>Notes:</h6><p class="text-caption font-weight-light text-uppercase">{{ contact.NOTE }}</p>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-spacer></v-spacer>
                            <v-col class="text-right">
                                <v-btn
                                class="mx-2"
                                fab
                                dark
                                x-small
                                color="purple"
                                >
                                <v-icon dark>
                                    mdi-heart
                                </v-icon>
                                </v-btn>
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
export default {
    name: "ContactListItem",
    props: {
        contacts: [],
    }
}
</script>

<style>
a {
    text-decoration: none;
    color: black;
}
</style>