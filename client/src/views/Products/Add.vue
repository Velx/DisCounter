<template>
    <v-container>
        <v-row wrap>
            <v-col
                    cols="12"
                    sm="8"
                    offset-sm="2"
                    md="8"
                    offset-md="2"
            >
                <v-form
                        v-model="valid"
                        onSubmit="return false;"
                        ref="form"
                >
                    <v-text-field
                            label="Aliexpress product url"
                            hint="Enter here Aliexpress product url that you want to track"
                            background-color="#f5f5f5"
                            type="url"
                            v-model="url"
                            :rules="ali_rules"
                            validate-on-blur
                            :success="valid"
                            dense
                            outlined
                            solo
                            rounded
                            :append-outer-icon="mdiSend"
                            @click:append-outer="sendURL"
                    >

                    </v-text-field>
                </v-form>
            </v-col>
        </v-row>
        <v-row justify="space-between" v-if="product">
            <v-col
                    cols="12"
                    sm="12"
                    offset-sm="2"
                    md="8"
                    offset-md="2"
            >
                <v-card raised style="background-color: #f5f5f5">
                    <v-btn
                            fab
                            top
                            absolute
                            right dark
                            color="red"
                            :small="$vuetify.breakpoint.mdAndDown"
                            @click="deleteProduct"
                    >
                        <v-icon>{{ mdiDelete }}</v-icon>
                    </v-btn>
<!--                    <v-toolbar color="cyan"-->
<!--                               dark dense>-->
<!--                        <v-toolbar-title class=" text-uppercase" >Added product:</v-toolbar-title>-->
<!--                        <v-spacer></v-spacer>-->
<!--                        <v-btn icon>-->
<!--                            <v-icon>{{mdiMinus}}</v-icon>-->
<!--                        </v-btn>-->
<!--                        <v-btn icon>-->
<!--                            <v-icon>{{mdiDelete}}</v-icon>-->
<!--                        </v-btn>-->
<!--                    </v-toolbar>-->
                    <v-row>
                        <v-col cols="6" sm="6" md="6" >
                            <v-img :src="product.image" contain class="ma-3"></v-img>
                        </v-col>
                        <v-col cols="6" sm="6" md="6">
                            <v-row wrap no-gutters>
                                <v-col cols="12" sm="12" md="12">
                                    <v-card-text :class="[$vuetify.breakpoint.mdAndUp ? 'headline' : 'subtitle-2']"
                                                 class="text-left"
                                    >
                                        {{ $vuetify.breakpoint.mdAndUp ? product.name.split(' ').slice(0,22).join(' ') + '...' : product.name.split(' ').slice(0,8).join(' ') + '...' }}
                                    </v-card-text>
                                </v-col>
                                <v-divider></v-divider>
                                <v-col cols="12" sm="12" md="12">
                                    <v-card-text :class="[$vuetify.breakpoint.mdAndUp ? 'headline mt-10' : 'subtitle-2 mt-1']"
                                                 class="text-left ">
                                        Price:<span class="green--text">{{ product.current_price ? product.current_price : product.price }} </span>
                                    </v-card-text>
                                </v-col>
                            </v-row>
                        </v-col>
                    </v-row>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import {mdiSend, mdiDelete, mdiMinus} from "@mdi/js";
export default {
    name: "Add",
    data: () => ({
        valid: false,
        url: '',
        mdiSend: mdiSend,
        mdiDelete: mdiDelete,
        mdiMinus: mdiMinus,
        ali_rules: [
            v => v.length > 0 || 'URL is required',
            v => {
                const pattern = /aliexpress\.(com|ru|ua)\/item\/\d+.html/
                return pattern.test(v) || 'Wrong url.'
            }
        ],
        // product: {
        //     "api_id": "4000918899813",
        //     "name": "Самостоятельная щетка для грумера для кошек, принадлежности для ухода за домашними животными, расческа для удаления волос для кошек, собак, обрезка волос, массажное устройство для кошек С Кошачьей Мят",
        //     "price": "30345.77",
        //     "current_price": null,
        //     "image": "https://ae01.alicdn.com/kf/H1ac0fed0fcab4b47b03ea555413ae1f3N/-.jpg",
        //     "ali_url": "https://aliexpress.ru/item/4000918899813.html"
        // }
    }),
    methods: {
        sendURL () {
            if (this.$refs.form.validate()) {
                this.$store.dispatch('addProduct', {'aliUrl': this.url})
                        .then(() => {})
                        .catch(() => {})
            }
        },
        deleteProduct () {
            this.$store.dispatch('deleteProduct', {'api_id': this.product.api_id})
        }
    },
    computed: {
        product () {
            return this.$store.getters.getProduct
        },
        loading () {
            return this.$store.getters.loading
        }
    }
}
</script>

<style>
    .v-card__title {
        word-break: normal !important ;
    }
</style>