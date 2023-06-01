const app = Vue.createApp({
    data() {
        return {
            test: "hello",
        }
    },
    methods: {
  
        toPage: function (page) {
            this.page = page
        },

    },
    mounted() {
    },


})
app.mount('#wrapper')
