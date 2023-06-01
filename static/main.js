const app = Vue.createApp({
    data() {
        return {
            bots:[{"name":"bot 3","subs":11},{"name":"bot 2","subs":100}],
            users:[],
            cur_bot:null,
            add_bot_wuit_s:0,
            ofset:0,
            users_s:0
        }
    },
    methods: {
  
    
        quit_add_bot: function (state){
            this.add_bot_wuit_s = state
        },
        quit_users: function(state){
            this.users_s = state

        },
        add_bot: function (state){
            axios.post('/add_bot', {
                name: this.name_input,
                token: this.token_input
              })
              .then(response => {
                if (response.status == 200){

                     this.get_bots();
                }

              })
        },
        get_bots: function(){
            axios.get('/get_bots')
              .then(response => {
                if (response.status == 200){
                    this.bots = response.data
                }
                
              })
        },
        user_list: function(id,ofset){
            this.ofset = ofset;
            this.cur_bot = id;
            this.users_s = 1;
            axios.get('/get_users',{params:{"ofset":ofset,"id":id}})
              .then(response => {
                this.users = response.data
              })
        },
        users_page: function(page){
            if (page == 0){
                this.ofset -= 10
                this.ofset < 0 ? this.ofset = 0 : ""
            }else{
                this.ofset += 10
            }
            this.user_list(this.cur_bot,this.ofset)
        }

    },
    mounted() {
        this.get_bots()
    },


})
app.mount('#wrapper')
