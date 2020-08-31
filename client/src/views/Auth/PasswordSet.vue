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
            <v-toolbar-title>Enter new password</v-toolbar-title>
          </v-toolbar>
          <v-card-text>
            <v-form v-model="valid" ref="form" lazy-validation>
              <v-text-field
                      label="Password"
                      name="password"
                      hint="Password should contain at least 6 characters"
                      :prepend-icon="icons.mdiLock"
                      :rules="passwordRules"
                      v-model="password"
                      :type="show ? 'password' : 'text'"
                      :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                      @mousedown="show = !show"
                      @mouseup="show = !show"
              ></v-text-field>
              <v-text-field
                      label="Confirm password"
                      name="password2"
                      :prepend-icon="icons.mdiLock"
                      :rules="ConfPasswordRules"
                      v-model="password2"
                      :type="show ? 'password' : 'text'"
                      :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                      @mousedown="show = !show"
                      @mouseup="show = !show"
                      @touchstart="show = !show"
                      @touchend="show = !show"
              ></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
                    color="#5480e9"
                    class="white--text"
                    :disabled="!valid"
                    @click="onSubmit"
            >
              Set
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import {mdiLock} from '@mdi/js';
export default {
  name: "PasswordSet",
  data: () => ({
    show: true,
    password: '',
    password2: '',
    valid: true,
    icons: {
      mdiLock: mdiLock
    },
    passwordRules: [
      v => !!v || 'Password is required',
      v => v.length >= 6 || 'Password must be equal or more than 6 characters'
    ]
  }),
  methods: {
    onSubmit () {
      if (this.$refs.form.validate()) {
        this.$store.dispatch('resetPasswordSet', {token: this.$route.params.token ,password: this.password})
            .then(() => {
              this.$router.push('/')
            })
            .catch(() => {
            })
      }
    }
  },
  computed: {
    ConfPasswordRules () {
      return [
        v => !!v || 'Password is required',
        v => v === this.password || 'Password should match'
      ]
    },
    loading () {
      return this.$store.getters.loading
    }
  }
}
</script>

<style scoped>

</style>