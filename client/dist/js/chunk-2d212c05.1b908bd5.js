(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d212c05"],{aa6e:function(s,o,t){"use strict";t.r(o);var a=function(){var s=this,o=s.$createElement,t=s._self._c||o;return t("v-container",{staticClass:"fill-height",attrs:{fluid:""}},[t("v-row",{attrs:{wrap:""}},[t("v-col",{attrs:{cols:"12",sm:"8",md:"4","offset-sm":"2","offset-md":"4"}},[t("v-card",{staticClass:"elevation-12",staticStyle:{"background-color":"#f5f5f5"}},[t("v-toolbar",{attrs:{color:"#5480e9",dark:"",flat:""}},[t("v-toolbar-title",[s._v("Enter new password")])],1),t("v-card-text",[t("v-form",{ref:"form",attrs:{"lazy-validation":""},model:{value:s.valid,callback:function(o){s.valid=o},expression:"valid"}},[t("v-text-field",{attrs:{label:"Password",name:"password",hint:"Password should contain at least 6 characters","prepend-icon":s.icons.mdiLock,rules:s.passwordRules,type:s.show?"password":"text","append-icon":s.show?"mdi-eye":"mdi-eye-off"},on:{mousedown:function(o){s.show=!s.show},mouseup:function(o){s.show=!s.show}},model:{value:s.password,callback:function(o){s.password=o},expression:"password"}}),t("v-text-field",{attrs:{label:"Confirm password",name:"password2","prepend-icon":s.icons.mdiLock,rules:s.ConfPasswordRules,type:s.show?"password":"text","append-icon":s.show?"mdi-eye":"mdi-eye-off"},on:{mousedown:function(o){s.show=!s.show},mouseup:function(o){s.show=!s.show},touchstart:function(o){s.show=!s.show},touchend:function(o){s.show=!s.show}},model:{value:s.password2,callback:function(o){s.password2=o},expression:"password2"}})],1)],1),t("v-card-actions",[t("v-spacer"),t("v-btn",{staticClass:"white--text",attrs:{color:"#5480e9",disabled:!s.valid},on:{click:s.onSubmit}},[s._v(" Set ")])],1)],1)],1)],1)],1)},e=[],r=t("94ed"),n={name:"PasswordSet",data:function(){return{show:!0,password:"",password2:"",valid:!0,icons:{mdiLock:r["g"]},passwordRules:[function(s){return!!s||"Password is required"},function(s){return s.length>=6||"Password must be equal or more than 6 characters"}]}},methods:{onSubmit:function(){var s=this;this.$refs.form.validate()&&this.$store.dispatch("resetPasswordSet",{token:this.$route.params.token,password:this.password}).then((function(){s.$router.push("/")})).catch((function(){}))}},computed:{ConfPasswordRules:function(){var s=this;return[function(s){return!!s||"Password is required"},function(o){return o===s.password||"Password should match"}]},loading:function(){return this.$store.getters.loading}}},d=n,i=t("2877"),c=t("6544"),l=t.n(c),u=t("8336"),w=t("b0af"),f=t("99d9"),p=t("62ad"),h=t("a523"),m=t("4bd4"),v=t("0fd9"),b=t("2fa4"),k=t("8654"),x=t("71d9"),V=t("2a7f"),C=Object(i["a"])(d,a,e,!1,null,"01431a33",null);o["default"]=C.exports;l()(C,{VBtn:u["a"],VCard:w["a"],VCardActions:f["a"],VCardText:f["b"],VCol:p["a"],VContainer:h["a"],VForm:m["a"],VRow:v["a"],VSpacer:b["a"],VTextField:k["a"],VToolbar:x["a"],VToolbarTitle:V["b"]})}}]);
//# sourceMappingURL=chunk-2d212c05.1b908bd5.js.map