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
                        <v-toolbar-title>Login</v-toolbar-title>
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
                                    label="Password"
                                    name="password"
                                    :prepend-icon="icons.mdiLock"
                                    :rules="passwordRules"
                                    v-model="password"
                                    :type="show ? 'text' : 'password'"
                                    :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                                    @mousedown="show = !show"
                                    @touchstart="show = !show"
                                    @mouseup="show = !show"
                                    @touchend="show = !show"
                            ></v-text-field>
                            <p class="text-right overline"
                            >
                                <router-link to="/password-reset" class="noLine">Forgot password?</router-link>
                            </p>
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
                            Login
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
            <v-col
                    cols="12"
                    sm="8"
                    md="4"
                    offset-sm="2"
                    offset-md="4"
            >
                <v-card class="elevation-12" style="background-color: #f5f5f5">
                    <v-card-text class="text-center">
                        New to DisCounter? <router-link to="/registration" class="noLine" tag="a">Create an account.</router-link>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import {mdiAccount, mdiLock} from "@mdi/js";

export default {
    name: "Login",
    data: () => ({
        link: '/registration',
        show: false,
        login: '',
        email: '',
        password: '',
        password2: '',
        valid: true,
        icons: {
            mdiLock: mdiLock,
            mdiAccount: mdiAccount
        },
        nameRules: [
            v => !!v || 'Login is required',
            v => v.length >= 4 || 'Login must be equal or more than 4 characters'
        ],
        passwordRules: [
            v => !!v || 'Password is required',
            v => v.length >= 6 || 'Password must be equal or more than 6 characters'
        ]
    }),
    methods: {
        onSubmit () {
            if (this.$refs.form.validate()) {
                const user = {
                    login: this.login,
                    password: this.password
                }
                this.$store.dispatch('login', user)
                        .then(() => {
                            this.$router.push('/?authorized=true', )
                        })
                        .catch(() => {})
            }
        }
    },
    computed: {
        loading () {
            return this.$store.getters.loading
        }
    },
    created () {
        if (this.$route.query['loginError']) {
            this.$store.dispatch('setError', 'Please log in to access this page.')
        }
    }
}
</script>

<style>
.text-right.overline {
    margin-bottom: 0 !important;
}
.noLine {
    text-decoration: none;
}
</style>