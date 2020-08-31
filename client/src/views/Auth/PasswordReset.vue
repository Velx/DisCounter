<template>
  <v-container
          class="fill-height"
          fluid
  >
    <v-row
            wrap
    >
      <v-col
              cols="12"
              sm="8"
              md="4"
              offset-sm="2"
              offset-md="4"

      >
        <v-card class="elevation-12" style="background-color: #f5f5f5">
          <v-toolbar
                  color="#5480e9"
                  dark
                  flat
          >
            <v-toolbar-title>Password Reset Form</v-toolbar-title>
          </v-toolbar>
          <v-card-text>
            <v-form v-model="valid" ref="form" lazy-validation>
              <v-text-field
                      label="Email"
                      name="Email"
                      hint="Please enter email of your account"
                      :prepend-icon="icons.mdiEmail"
                      type="email"
                      v-model="email"
                      :rules="emailRules"
              ></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
                    color="#5480e9"
                    class="white--text"
                    :loading="loading"
                    :disabled="!valid || loading"
                    @click="onSubmit"
            >
              Reset
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import {mdiEmail } from '@mdi/js';
export default {
  name: "PasswordReset",
  data: () => ({
    valid: true,
    email: '',
    icons: {
      mdiEmail: mdiEmail
    },
    emailRules: [
      v => {
        const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        return pattern.test(v) || 'Invalid e-mail.'
      }
    ]
  }),
  methods: {
    onSubmit () {
      if (this.$refs.form.validate()) {
        this.$store.dispatch('resetRequest', {email: this.email})
            .then(() => {
              this.$router.push('/')
            })
            .catch(() => {
            })
      }
    }
  },
  computed: {
    loading () {
      return this.$store.getters.loading
    }
  }
}
</script>

<style scoped>

</style>