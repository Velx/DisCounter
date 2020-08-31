<template>
    <v-container
            class="fill-height"
            fluid
    >
        <v-row
                align="center"
                justify="center"
        >
            <v-col
                    cols="12"
                    sm="8"
                    md="4"
            >
                <v-card class="elevation-12" v-if="!afterRegistration" style="background-color: #f5f5f5">
                    <v-toolbar
                            color="#5480e9"
                            dark
                            flat
                    >
                        <v-toolbar-title>Registration</v-toolbar-title>
                    </v-toolbar>
                    <v-card-text>
                        <v-form v-model="valid" ref="form" lazy-validation>
                            <v-text-field
                                    label="Login"
                                    name="login"
                                    hint="Login should contain at least 4 characters"
                                    :prepend-icon="icons.mdiAccount"
                                    type="text"
                                    :rules="nameRules"
                                    v-model="login"
                            ></v-text-field>
                            <v-text-field
                                    label="Email"
                                    name="Email"
                                    hint="Please use your real email, we will send activation email on it"
                                    :prepend-icon="icons.mdiEmail"
                                    type="email"
                                    v-model="email"
                                    :rules="emailRules"
                            ></v-text-field>
                            <v-text-field
                                    label="Password"
                                    name="password"
                                    hint="Password should contain at least 6 characters"
                                    :prepend-icon="icons.mdiLock"
                                    :rules="passwordRules"
                                    v-model="password"
                                    :type="show ? 'text' : 'password'"
                                    :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                                    @mousedown="show = !show"
                                    @mouseup="show = !show"
                                    @touchstart="show = !show"
                                    @touchend="show = !show"
                            ></v-text-field>
                            <v-text-field
                                    label="Confirm password"
                                    name="password2"
                                    :prepend-icon="icons.mdiLock"
                                    :rules="ConfPasswordRules"
                                    v-model="password2"
                                    :type="show ? 'text' : 'password'"
                                    :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                                    @mousedown="show = !show"
                                    @touchstart="show = !show"
                                    @mouseup="show = !show"
                                    @touchend="show = !show"
                            ></v-text-field>
                        </v-form>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="#5480e9"
                               class="white--text"
                               :loading="loading"
                               :disabled="!valid || loading"
                               @click="onSubmit"
                        >
                            Register
                        </v-btn>
                    </v-card-actions>
                </v-card>
                <v-card class="elevation-12" style="background-color: #f5f5f5" v-else>
                    <v-card-text class="text-center"
                                 :class="[$vuetify.breakpoint.mdAndUp ? 'headline' : 'subtitle-2']">
                        Registration succeed
                    </v-card-text>
                    <v-card-text class="text-center font-weight-regular"
                                 :class="[$vuetify.breakpoint.mdAndUp ? 'title ' : 'body-1']"
                    >
                        Activation email was sent on your email
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import { mdiAccount, mdiLock, mdiEmail } from '@mdi/js';
export default {
    name: "Registration",
    data: () => ({
        show: false,
        afterRegistration: false,
        login: '',
        email: '',
        password: '',
        password2: '',
        valid: true,
        icons: {
            mdiLock: mdiLock,
            mdiAccount: mdiAccount,
            mdiEmail: mdiEmail
        },
        nameRules: [
            v => !!v || 'Login is required',
            v => v.length >= 4 || 'Login must be equal or more than 4 characters'
        ],
        emailRules: [
            v => {
                const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
                return pattern.test(v) || 'Invalid e-mail.'
            }
        ],
        passwordRules: [
            v => !!v || 'Password is required',
            v => v.length >= 6 || 'Password must be equal or more than 6 characters'
        ]
    }),
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

    },
    methods: {
        onSubmit () {
            if (this.$refs.form.validate()) {
                let user = {
                  login: this.login,
                  email: this.email,
                  password: this.password
                }
                this.$store.dispatch('register', user)
                    .then(() => {
                      this.afterRegistration = true
                    })
                    .catch(() => {})
            }
        }
    }
}
</script>

<style>

</style>