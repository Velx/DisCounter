<template>
  <v-app id="inspire">
<!--    <v-navigation-drawer-->
<!--            v-model="drawer"-->
<!--            app-->
<!--            left-->
<!--    >-->
<!--      <v-list dense flat>-->
<!--        <v-list-item link-->
<!--                     v-for="lin in links"-->
<!--                     :key="lin.title"-->
<!--                     :to="lin.url"-->

<!--        >-->
<!--          <v-list-item-action>-->
<!--            <v-icon>{{ lin.icon }}</v-icon>-->
<!--          </v-list-item-action>-->

<!--          <v-list-item-content>-->
<!--            <v-list-item-title>{{ lin.title }}</v-list-item-title>-->
<!--          </v-list-item-content>-->
<!--        </v-list-item>-->
<!--        <v-list-item link-->
<!--                     v-if="!isUserLoggedIn"-->
<!--                     @click="onLogout">-->
<!--          <v-list-item-action>-->
<!--            <v-icon>{{ mdiLogout }}</v-icon>-->
<!--          </v-list-item-action>-->

<!--          <v-list-item-content>-->
<!--            <v-list-item-title>Logout</v-list-item-title>-->
<!--          </v-list-item-content>-->
<!--        </v-list-item>-->
<!--      </v-list>-->
<!--    </v-navigation-drawer>-->

    <v-app-bar
            app
            color="#f5f5f5"
    >
<!--      <v-app-bar-nav-icon-->
<!--              @click.stop="drawer = !drawer"-->
<!--              class="hidden-md-and-up"-->
<!--      ></v-app-bar-nav-icon>-->
      <v-toolbar-title>
        <router-link to="/" class="toolbar-title black--text">DisCounter</router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items :style="$vuetify.breakpoint.mdAndUp ? 'padding-right: 16px;' : ''">
        <v-btn v-for="lin in links"
               :key="lin.title"
               :to="lin.url"
               text
               active-class="no-active"
               class="black--text"
        >
          <v-icon :left="$vuetify.breakpoint.mdAndUp">{{ lin.icon }}</v-icon>
          <span class="hidden-sm-and-down">{{ lin.title }}</span>
        </v-btn>
        <v-btn v-if="isUserLoggedIn"
                 text
                 active-class="no-active"
                 @click.stop="openSettings"
          >
            <v-icon :left="$vuetify.breakpoint.mdAndUp">{{ mdiAccountCog }}</v-icon>
            <span class="hidden-sm-and-down"> Profile </span>
        </v-btn>
      </v-toolbar-items>
    </v-app-bar>
    <v-dialog v-model="settingsDialog" fullscreen hide-overlay  transition="dialog-bottom-transition" style="background-color: #f5f5f5">
      <v-card >
        <v-toolbar dark color="#5480e9">
          <v-btn icon dark @click="close">
            <v-icon>mdi-close</v-icon>
          </v-btn>
          <v-toolbar-title>Settings</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-toolbar-items>
            <v-btn dark text @click="save">Save</v-btn>
          </v-toolbar-items>
        </v-toolbar>
        <v-list three-line subheader class="ml-2">
          <v-subheader>User Controls</v-subheader>
          <v-list-item >
            <v-list-item-content>
              <v-list-item-title>Change Email</v-list-item-title>
              <v-row>
                <v-col cols="12" sm="12" md="4">
                  <v-form v-model="emailValid"
                          ref="emailForm"
                          lazy-validation
                          onSubmit="return false;"
                  >
                    <v-text-field
                            label="Email"
                            name="Email"
                            hint="Please use your real email, we will send activation email on it"
                            :prepend-icon="mdiEmail"
                            type="email"
                            v-model="email"
                            :rules="emailRules"
                    ></v-text-field>
                  </v-form>
                </v-col>
              </v-row>
            </v-list-item-content>
          </v-list-item>
          <v-list-item >
            <v-list-item-content>
              <v-list-item-title>Change Password</v-list-item-title>
              <v-row>
                <v-col cols="12" sm="12" md="4">
                  <v-form v-model="pasValid"
                          ref="pasForm"
                          lazy-validation
                          onSubmit="return false;"
                  >
                    <v-text-field
                            label="Password"
                            name="password"
                            hint="Password should contain at least 6 characters"
                            :prepend-icon="mdiLock"
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
                            :prepend-icon="mdiLock"
                            :rules="ConfPasswordRules"
                            v-model="password2"
                            :type="show ? 'text' : 'password'"
                            :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                            @mousedown="show = !show"
                            @mouseup="show = !show"
                            @touchstart="show = !show"
                            @touchend="show = !show"
                    ></v-text-field>
                  </v-form>
                </v-col>
              </v-row>
            </v-list-item-content>
          </v-list-item>
        </v-list>
        <v-divider></v-divider>
        <v-list three-line subheader class="ml-2">
          <v-subheader>General</v-subheader>
          <v-list-item>
            <v-list-item-action>
              <v-switch v-model="emailNotifications" inset color="#5480e9"></v-switch>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Email notifications</v-list-item-title>
              <v-list-item-subtitle>Notify me about new sales for selected products with email</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list>
        <v-divider></v-divider>
        <v-btn @click="logout"
               color="red"
               text
               class="ml-3 mt-3 mb-5"
        >
          <v-icon left>{{ mdiLogout }}</v-icon>
          Logout
        </v-btn>
        <v-divider></v-divider>
      </v-card>
    </v-dialog>

    <v-content style="background-color: #c1c8e2">
      <router-view></router-view>
    </v-content>
    <template v-if="error">
      <v-snackbar
              :multi-line="true"
              :timeout="5000"
              :color="errorColor"
              @input="closeError"
              :value = "true"
      >
        {{ error }}
        <v-btn
                dark
                text
                @click="closeError"
        >
          Close
        </v-btn>
      </v-snackbar>
    </template>
  </v-app>
</template>

<script>
import { mdiLogin, mdiAccountPlus, mdiPlusCircleOutline, mdiAccountCog, mdiLock, mdiEmail, mdiLogout } from '@mdi/js';
export default {
  data: () => ({
    show: false,
    drawer: false,
    pasValid: false,
    emailValid: false,
    password: '',
    password2: '',
    email: '',
    mdiLock: mdiLock,
    mdiEmail: mdiEmail,
    mdiLogout: mdiLogout,
    checkboxChanged: false,
    settingsDialog: false,
    mdiAccountCog: mdiAccountCog,
    passwordRules: [
      v => !!v || 'Password is required',
      v => v.length >= 6 || 'Password must be equal or more than 6 characters'
    ],
    emailRules: [
      v => {
        const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        return pattern.test(v) || 'Invalid e-mail.'
      }
    ]
  }),
  computed: {
    isUserLoggedIn () {
      return this.$store.getters.isUserLoggedIn
    },
    error () {
      return this.$store.getters.error
    },
    errorColor () {
      return this.$store.getters.errorColor
    },
    links () {
      if (this.isUserLoggedIn) {
        return [
            // {title: 'Log out ', icon: 'exit_to_app', url: '/logout'},
            { title: 'Add product', icon: mdiPlusCircleOutline, url: '/add' },
            // { title: 'Profile', icon: mdiAccountCog, url: '' }
        ]
      } else {
        return [
            { title: 'Register', icon: mdiAccountPlus, url: '/registration' },
            { title: 'Login', icon: mdiLogin, url: '/login' },
        ]
      }
    },
    ConfPasswordRules () {
      return [
        v => !!v || 'Password is required',
        v => v === this.password || 'Password should match'
      ]
    },
    emailNotifications : {
      get () {
        return this.$store.getters.emailNotification
      },
      set (value) {
        this.checkboxChanged = true
        this.$store.commit('setEmailNotification', value)
      }
    }
  },
  methods: {
    onLogout () {
      console.log('HI')
    },
    closeError () {
      this.$store.dispatch('clearError')
    },
    openSettings () {
      this.settingsDialog = true
    },
    save () {
      let canClose = true
      if (this.password !== '' && this.password2 !== '') {
        if (this.$refs.pasForm.validate()) {
          console.log('New password validated')
        } else {
          canClose = false
        }
      } else {
        this.$refs.pasForm.resetValidation()
      }
      if (this.email !== '') {
        if (this.$refs.emailForm.validate()) {
          console.log('New password validated')
        } else {
          canClose = false
        }
      } else {
        this.$refs.emailForm.resetValidation()
      }
      if (canClose) {
        if (this.email || this. password || this.checkboxChanged) {
          this.$store.dispatch('updateUser',
              {email: this.email ? this.email : null,
                password: this.password ? this.password : null,
                emailNotification: this.emailNotifications
              })
              .then(() => {})
              .catch(() => {})
        }
        this.settingsDialog = false
        this.checkboxChanged = false
        this.$refs.emailForm.resetValidation()
        this.$refs.pasForm.resetValidation()
        this.password = this.password2 = this.email =  ''
      }
    },
    close () {
      this.settingsDialog = false
      this.checkboxChanged = false
      this.$refs.emailForm.resetValidation()
      this.$refs.pasForm.resetValidation()
      this.password = this.password2 = this.email =  ''
    },
    logout () {
      this.$store.dispatch('logout')
      this.settingsDialog = false
    }
  },
  created() {
    if (this.isUserLoggedIn) {
      this.$store.dispatch('loadProducts')
          .then(() => {})
          .catch(() => {})
    }
  }
};
</script>

<style>
  .v-btn--active.no-active::before {
    opacity: 0 !important;
  }
  .toolbar-title {
    color: inherit !important;
    text-decoration: inherit;
  }
  .v-toolbar__content {
    padding-right: 0px !important;
  }
  html {
    scrollbar-width: thin;
  }
  .v-dialog {
    scrollbar-width: thin;
  }
</style>