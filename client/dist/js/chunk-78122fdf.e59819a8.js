(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-78122fdf"],{"37d1":function(t,e,r){"use strict";r.r(e);var a=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("v-container",[r("v-row",{attrs:{wrap:""}},[r("v-col",{attrs:{cols:"12",sm:"8","offset-sm":"2",md:"8","offset-md":"2"}},[r("v-form",{ref:"form",attrs:{onSubmit:"return false;"},model:{value:t.valid,callback:function(e){t.valid=e},expression:"valid"}},[r("v-text-field",{attrs:{label:"Aliexpress product url",hint:"Enter here Aliexpress product url that you want to track","background-color":"#f5f5f5",type:"url",rules:t.ali_rules,"validate-on-blur":"",success:t.valid,dense:"",outlined:"",solo:"",rounded:"","append-outer-icon":t.mdiSend},on:{"click:append-outer":t.sendURL},model:{value:t.url,callback:function(e){t.url=e},expression:"url"}})],1)],1)],1),t.product?r("v-row",{attrs:{justify:"space-between"}},[r("v-col",{attrs:{cols:"12",sm:"12","offset-sm":"2",md:"8","offset-md":"2"}},[r("v-card",{staticStyle:{"background-color":"#f5f5f5"},attrs:{raised:""}},[r("v-btn",{attrs:{fab:"",top:"",absolute:"",right:"",dark:"",color:"red",small:t.$vuetify.breakpoint.mdAndDown},on:{click:t.deleteProduct}},[r("v-icon",[t._v(t._s(t.mdiDelete))])],1),r("v-row",[r("v-col",{attrs:{cols:"6",sm:"6",md:"6"}},[r("v-img",{staticClass:"ma-3",attrs:{src:t.product.image,contain:""}})],1),r("v-col",{attrs:{cols:"6",sm:"6",md:"6"}},[r("v-row",{attrs:{wrap:"","no-gutters":""}},[r("v-col",{attrs:{cols:"12",sm:"12",md:"12"}},[r("v-card-text",{staticClass:"text-left",class:[t.$vuetify.breakpoint.mdAndUp?"headline":"subtitle-2"]},[t._v(" "+t._s(t.$vuetify.breakpoint.mdAndUp?t.product.name.split(" ").slice(0,22).join(" ")+"...":t.product.name.split(" ").slice(0,8).join(" ")+"...")+" ")])],1),r("v-divider"),r("v-col",{attrs:{cols:"12",sm:"12",md:"12"}},[r("v-card-text",{staticClass:"text-left ",class:[t.$vuetify.breakpoint.mdAndUp?"headline mt-10":"subtitle-2 mt-1"]},[t._v(" Price:"),r("span",{staticClass:"green--text"},[t._v(t._s(t.product.current_price?t.product.current_price:t.product.price)+" ")])])],1)],1)],1)],1)],1)],1)],1):t._e()],1)},s=[],o=r("94ed"),i={name:"Add",data:function(){return{valid:!1,url:"",mdiSend:o["l"],mdiDelete:o["e"],mdiMinus:o["j"],ali_rules:[function(t){return t.length>0||"URL is required"},function(t){var e=/aliexpress\.(com|ru|ua)\/item\/\d+.html/;return e.test(t)||"Wrong url."}]}},methods:{sendURL:function(){this.$refs.form.validate()&&this.$store.dispatch("addProduct",{aliUrl:this.url}).then((function(){})).catch((function(){}))},deleteProduct:function(){this.$store.dispatch("deleteProduct",{api_id:this.product.api_id})}},computed:{product:function(){return this.$store.getters.getProduct},loading:function(){return this.$store.getters.loading}}},n=i,d=(r("be96"),r("2877")),c=r("6544"),l=r.n(c),u=r("8336"),f=r("b0af"),p=r("99d9"),m=r("62ad"),v=r("a523"),b=r("ce7e"),h=r("4bd4"),w=r("132d"),_=r("adda"),g=r("0fd9"),k=r("8654"),x=Object(d["a"])(n,a,s,!1,null,null,null);e["default"]=x.exports;l()(x,{VBtn:u["a"],VCard:f["a"],VCardText:p["b"],VCol:m["a"],VContainer:v["a"],VDivider:b["a"],VForm:h["a"],VIcon:w["a"],VImg:_["a"],VRow:g["a"],VTextField:k["a"]})},"53fa":function(t,e,r){},be96:function(t,e,r){"use strict";var a=r("53fa"),s=r.n(a);s.a}}]);
//# sourceMappingURL=chunk-78122fdf.e59819a8.js.map