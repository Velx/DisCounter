<template>
    <v-container
            class="fill-height"
            fluid
    >
        <v-row
                v-if="notOnSale.length + onSale.length + notAvailable.length === 0"
                wrap

        >
            <v-col
                    cols="12"
                    sm="8"
                    md="6"
                    offset-sm="2"
                    offset-md="3"

            >
                <v-card style="background-color: #f5f5f5">
                    <v-card-text
                            v-if="isUserLoggedIn"
                            class="text-center"
                            :class="[$vuetify.breakpoint.mdAndUp ? 'headline' : 'subtitle-2']"
                    >
                        You doesn't add any products yet. <router-link to="/add" class="noLine" tag="a">Add it now.</router-link>
                    </v-card-text>
                    <v-card-text
                            v-else
                            class="text-center"
                            :class="[$vuetify.breakpoint.mdAndUp ? 'headline' : 'subtitle-2']"
                    >
                        You are not logged in. Please
                        <router-link to="/login" class="noLine" tag="a">log in</router-link> or
                        <router-link to="/registration" class="noLine" tag="a">create a new account</router-link>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
        <v-row wrap align="start" justify="center"  v-else>
            <v-col cols="12" sm="12" md="12" class="text-center pb-0" v-if="onSale.length !== 0">
                <h1 class="font-weight-light headline text-uppercase">Products on sale</h1>
            </v-col>
            <v-col
                    cols="12"
                    sm="12"
                    md="4"
                    v-for="product in onSale"
                    :key="product.api_id"
            >
                <v-card class="mr-2 ml-2" height="500px" style="background-color: #f5f5f5">
                    <v-img
                            height="250px"
                            @click.stop="openImage(product.image)"
                            :src="product.image"
                            class="ma-3"></v-img>
                    <v-card-title class="text-wrap">
                        {{ $vuetify.breakpoint.mdAndUp ? product.name.slice(0,75) + '...' : product.name.slice(0,65) + '...' }}
                    </v-card-title>
                    <v-card-text :class="[$vuetify.breakpoint.mdAndUp ? 'headline' : 'subtitle-2 mt-2']"
                                 class="text-left font-weight-medium">
                        Price:<span class="green--text">{{ product.current_price ? product.current_price : product.price }} </span>
                        <span
                                class="red--text"
                                style="text-decoration: line-through;"
                                :class="[$vuetify.breakpoint.mdAndUp ? 'subtitle-1' : 'overline']"
                                v-if="product.current_price"
                        >{{product.price }}
                    </span>
                    </v-card-text>
                    <v-card-actions class="mt-2">
                        <v-spacer></v-spacer>
                        <v-btn text color="red">
                            <v-icon left>{{mdiDelete}}</v-icon> Remove
                        </v-btn>
                        <v-btn text color="green" :href="product.ali_url" target="_blank">
                            <v-icon left>{{mdiCart}}</v-icon> Buy
                        </v-btn>

                    </v-card-actions>
                </v-card>
            </v-col>

            <v-col cols="12" sm="12" md="12" class="text-center pb-0" v-if="notOnSale.length !== 0">
                <h1 class="font-weight-light headline text-uppercase">Products without sale price</h1>
            </v-col>
            <v-col
                    cols="12"
                    sm="12"
                    md="4"
                    v-for="product in notOnSale"
                    :key="product.api_id"
            >
                <v-card class="mr-2 ml-2" height="500px" style="background-color: #f5f5f5">
                    <v-img
                            height="250px"
                            @click.stop="openImage(product.image)"
                            :src="product.image"
                            class="ma-3"></v-img>
                    <v-card-title class="text-wrap">
                        {{ $vuetify.breakpoint.mdAndUp ? product.name.slice(0,75) + '...' : product.name.slice(0,65) + '...' }}
                    </v-card-title>
                    <v-card-text :class="[$vuetify.breakpoint.mdAndUp ? 'headline' : 'subtitle-2 mt-2']"
                                 class="text-left font-weight-medium">
                        Price:<span class="green--text">{{ product.current_price ? product.current_price : product.price }} </span>
                        <span
                                class="red--text"
                                style="text-decoration: line-through;"
                                :class="[$vuetify.breakpoint.mdAndUp ? 'subtitle-1' : 'overline']"
                                v-if="product.current_price"
                        >{{product.current_price }}
                    </span>
                    </v-card-text>
                    <v-card-actions class="mt-2">
                        <v-spacer></v-spacer>
                        <v-btn text color="red">
                            <v-icon left>{{mdiDelete}}</v-icon> Remove
                        </v-btn>
                        <v-btn text color="green" :href="product.ali_url" target="_blank">
                            <v-icon left>{{mdiCart}}</v-icon> Buy
                        </v-btn>

                    </v-card-actions>
                </v-card>
            </v-col>

            <v-col cols="12" sm="12" md="12" class="text-center pb-0" v-if="notAvailable.length !== 0">
                <h1 class="font-weight-light headline text-uppercase">Not available products</h1>
            </v-col>
            <v-col
                    cols="12"
                    sm="12"
                    md="4"
                    v-for="product in notAvailable"
                    :key="product.api_id"
            >
                <v-card class="mr-2 ml-2" height="500px" style="background-color: #f5f5f5">
                    <v-img
                            height="250px"
                            @click.stop="openImage(product.image)"
                            :src="product.image"
                            class="ma-3"></v-img>
                    <v-card-title class="text-wrap">
                        {{ $vuetify.breakpoint.mdAndUp ? product.name.slice(0,75) + '...' : product.name.slice(0,65) + '...' }}
                    </v-card-title>
                    <v-card-actions class="mt-2">
                        <v-spacer></v-spacer>
                        <v-btn text color="red">
                            <v-icon left>{{mdiDelete}}</v-icon> Remove
                        </v-btn>
                        <v-btn text color="green" :href="product.ali_url" target="_blank">
                            <v-icon left>{{mdiCart}}</v-icon> Buy
                        </v-btn>

                    </v-card-actions>
                </v-card>
            </v-col>

            <v-dialog
                    v-model="dialog"
            >
                <v-card  max-height="1000px">
                    <v-img :src="openedSrc"
                           class="zoom-out"
                           @click="dialog = false"
                           max-height="1000px"
                           contain
                    ></v-img>
                </v-card>
            </v-dialog>
        </v-row>
    </v-container>
<!--    <v-row wrap align="start" justify="center" class="mt-2 mr-4 ml-4">-->
<!--        <v-col cols="12" sm="12" md="12" class="text-center" v-if="onSale.length !== 0">-->
<!--            <h1 class="font-weight-light headline text-uppercase">Products on sale</h1>-->
<!--        </v-col>-->
<!--        <v-col-->
<!--                cols="12"-->
<!--                sm="12"-->
<!--                md="4"-->
<!--                v-for="product in onSale"-->
<!--                :key="product.api_id"-->
<!--        >-->
<!--            <v-card class="mr-2 ml-2" height="500px">-->
<!--                <v-img-->
<!--                        height="250px"-->
<!--                        @click.stop="openImage(product.image)"-->
<!--                        :src="product.image"-->
<!--                        class="ma-3"></v-img>-->
<!--                <v-card-title class="text-wrap">-->
<!--                    {{ $vuetify.breakpoint.mdAndUp ? product.name.slice(0,86) + '...' : product.name.slice(0,65) + '...' }}-->
<!--                </v-card-title>-->
<!--                <v-card-text :class="[$vuetify.breakpoint.mdAndUp ? 'headline' : 'subtitle-2 mt-2']"-->
<!--                             class="text-left font-weight-medium">-->
<!--                    Price:<span class="green&#45;&#45;text">{{ product.current_price ? product.current_price : product.price }} </span>-->
<!--                    <span-->
<!--                            class="red&#45;&#45;text"-->
<!--                            style="text-decoration: line-through;"-->
<!--                            :class="[$vuetify.breakpoint.mdAndUp ? 'subtitle-1' : 'overline']"-->
<!--                            v-if="product.current_price"-->
<!--                    >{{product.current_price }}-->
<!--                    </span>-->
<!--                </v-card-text>-->
<!--                <v-card-actions class="mt-2">-->
<!--                    <v-spacer></v-spacer>-->
<!--                    <v-btn text color="red">-->
<!--                        <v-icon left>{{mdiDelete}}</v-icon> Remove-->
<!--                    </v-btn>-->
<!--                    <v-btn text color="green" :href="product.ali_url" target="_blank">-->
<!--                        <v-icon left>{{mdiCart}}</v-icon> Buy-->
<!--                    </v-btn>-->

<!--                </v-card-actions>-->
<!--            </v-card>-->
<!--        </v-col>-->

<!--        <v-col cols="12" sm="12" md="12" class="text-center" v-if="notOnSale.length !== 0">-->
<!--            <h1 class="font-weight-light headline text-uppercase">Products without sale price</h1>-->
<!--        </v-col>-->
<!--        <v-col-->
<!--                cols="12"-->
<!--                sm="12"-->
<!--                md="4"-->
<!--                v-for="product in notOnSale"-->
<!--                :key="product.api_id"-->
<!--        >-->
<!--            <v-card class="mr-2 ml-2" height="500px">-->
<!--                <v-img-->
<!--                        height="250px"-->
<!--                        @click.stop="openImage(product.image)"-->
<!--                        :src="product.image"-->
<!--                        class="ma-3"></v-img>-->
<!--                <v-card-title class="text-wrap">-->
<!--                    {{ $vuetify.breakpoint.mdAndUp ? product.name.slice(0,86) + '...' : product.name.slice(0,65) + '...' }}-->
<!--                </v-card-title>-->
<!--                <v-card-text :class="[$vuetify.breakpoint.mdAndUp ? 'headline' : 'subtitle-2 mt-2']"-->
<!--                             class="text-left font-weight-medium">-->
<!--                    Price:<span class="green&#45;&#45;text">{{ product.current_price ? product.current_price : product.price }} </span>-->
<!--                    <span-->
<!--                            class="red&#45;&#45;text"-->
<!--                            style="text-decoration: line-through;"-->
<!--                            :class="[$vuetify.breakpoint.mdAndUp ? 'subtitle-1' : 'overline']"-->
<!--                            v-if="product.current_price"-->
<!--                    >{{product.current_price }}-->
<!--                    </span>-->
<!--                </v-card-text>-->
<!--                <v-card-actions class="mt-2">-->
<!--                    <v-spacer></v-spacer>-->
<!--                    <v-btn text color="red">-->
<!--                        <v-icon left>{{mdiDelete}}</v-icon> Remove-->
<!--                    </v-btn>-->
<!--                    <v-btn text color="green" :href="product.ali_url" target="_blank">-->
<!--                        <v-icon left>{{mdiCart}}</v-icon> Buy-->
<!--                    </v-btn>-->

<!--                </v-card-actions>-->
<!--            </v-card>-->
<!--        </v-col>-->

<!--        <v-col cols="12" sm="12" md="4" class="text-center fill-height"  v-if="notOnSale.length + onSale.length === 0">-->
<!--&lt;!&ndash;            <h1 class="font-weight-light headline text-uppercase">Products on sale</h1>&ndash;&gt;-->
<!--            <v-card>test</v-card>-->
<!--        </v-col>-->

<!--        <v-dialog-->
<!--                v-model="dialog"-->
<!--        >-->
<!--            <v-card>-->
<!--                <v-img :src="openedSrc"-->
<!--                       class="zoom-out"-->
<!--                       @click="dialog = false"-->
<!--                       max-height="100%"-->
<!--                       contain-->
<!--                ></v-img>-->
<!--            </v-card>-->
<!--        </v-dialog>-->
<!--    </v-row>-->
</template>

<script>
import {mdiCart, mdiDelete} from "@mdi/js";
import firebase from 'firebase/app'
import 'firebase/app'
import 'firebase/messaging'
export default {
    name: "List",
    data: () => ({
        dialog: false,
        mdiCart: mdiCart,
        mdiDelete: mdiDelete,
        openedSrc: '',
        products: [
            {
                "api_id": "4000918899813",
                "name": "DOOGEE S95 Pro 8 Гб 256 ГБ модульный прочный мобильный телефон IP68/IP69K 6,3-дюймовый дисплей 5150 мАч Helio P90 Восьмиядерный 48 МП камера Android 9",
                "price": "30345.77",
                "current_price": null,
                "image": "https://ae01.alicdn.com/kf/H94d5587dc2724f0e86bfe4a5cd759987R/DOOGEE-S95-Pro-8-256-IP68-IP69K.jpg",
                "ali_url": "https://aliexpress.ru/item/4000918899813.html"
            },
            {
                "api_id": "4000918899814",
                "name": "DOOGEE S95 Pro 8 Гб 256 ГБ модульный прочный мобильный телефон IP68/IP69K 6,3-дюймовый дисплей 5150 мАч Helio P90 Восьмиядерный 48 МП камера Android 9",
                "price": "30345.77",
                "current_price": "30345.77",
                "image": "https://ae01.alicdn.com/kf/H94d5587dc2724f0e86bfe4a5cd759987R/DOOGEE-S95-Pro-8-256-IP68-IP69K.jpg",
                "ali_url": "https://aliexpress.ru/item/4000918899813.html"
            },
            {
                "api_id": "4000918899815",
                "name": "DOOGEE S95 Pro 8 Гб 256 ГБ модульный прочный мобильный телефон IP68/IP69K 6,3-дюймовый дисплей 5150 мАч Helio P90 Восьмиядерный 48 МП камера Android 9",
                "price": "30345.77",
                "current_price": null,
                "image": "https://ae01.alicdn.com/kf/H94d5587dc2724f0e86bfe4a5cd759987R/DOOGEE-S95-Pro-8-256-IP68-IP69K.jpg",
                "ali_url": "https://aliexpress.ru/item/4000918899813.html"
            },
            {
                "api_id": "4000918899816",
                "name": "Самостоятельная щетка для грумера для кошек, принадлежности для ухода за домашними животными, расческа для удаления волос для кошек, собак, обрезка волос, массажное устройство для кошек С Кошачьей Мятой",
                "price": "272.71",
                "current_price": "0.77",
                "image": "https://ae01.alicdn.com/kf/H1ac0fed0fcab4b47b03ea555413ae1f3N/-.jpg",
                "ali_url": "https://aliexpress.ru/item/4000417010920.html"
            }
        ]
    }),
    methods: {
        openImage (src) {
            this.dialog = true;
            this.openedSrc = src;
        }
    },
    computed: {
        onSale () {
            return this.$store.getters.getDiscountedProducts
        },
        isUserLoggedIn () {
            return this.$store.getters.isUserLoggedIn
        },
        notOnSale () {
            return this.$store.getters.getNormalProducts
        },
        notAvailable () {
            return this.$store.getters.getNAProducts
        }
    },
    mounted () {
        if (this.$route.query.authorized && this.isUserLoggedIn) {
            const config = {
                apiKey: "AIzaSyBEj1Soso2Un1_9d-QnjQI7vLVYL6E4HqQ",
                authDomain: "discounter.firebaseapp.com",
                databaseURL: "https://discounter.firebaseio.com",
                projectId: "discounter",
                storageBucket: "discounter.appspot.com",
                messagingSenderId: "642427961332",
                appId: "1:642427961332:web:3ded7ef52f192355afc3a1",
                measurementId: "G-7YKGMVBD1R"
            };

            firebase.initializeApp(config)

            const messaging = firebase.messaging()

            messaging.usePublicVapidKey("BPjeQ8MLtiKImF4yFG7tSKu3kB2dv8WvfQOZpj13PKzP_8BNAuMWf4W2_zBSca1PY_BdWbQF0i-0WwU9p2RpI40")

            Notification.requestPermission().then(() => {
                console.log('Notification permission granted.')
                messaging.getToken().then((token) => {
                    this.$store.dispatch('saveNotificationToken', {token: token})
                })
            }).catch((err) => {
                console.log('Unable to retrieve refreshed token ', err)
            })
            messaging.onTokenRefresh(function () {
                messaging.getToken().then(function (newToken) {
                    this.$store.dispatch('saveNotificationToken', {token: newToken})
                }).catch(function (err) {
                    console.log('Unable to retrieve refreshed token ', err)
                })
            })
        }
    }
}
</script>

<style>
.zoom-in {
    cursor: zoom-out;
}
.zoom-out {
    cursor: zoom-out;
}
</style>