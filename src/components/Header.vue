<template>
    <div class="nav">
        
        <div class="logo" >
            <img src="../assets/icon/menu_book.png" alt="">
            <a href="/">
                <h1>ZACHRY</h1>
            </a>
        </div>

        <div class="search">
            <input id="searchInput" placeholder="Search">
            <img src="../assets/icon/search.png" alt="">
        </div>
        
        <div class="control-group">
            <button class="signup-button">
                <a href="">สมัครสมาชิก</a>
            </button>
            <p>|</p>
            <button class="login-button" @click="openLogin">
                <a >เข้าสู่ระบบ</a>
            </button>
            <p>|</p>
            <img src="../assets/icon/cart.png" alt="">
        </div>

        
        <div>
            
        </div>

        <div class="bg-blur" v-if="show" @click="closeLogin"></div>

        <Login class="login" v-show="show" @close="closeLogin"> </Login>
        
        
        
    </div>
</template>

<script>
    import Login from './Login.vue'
    export default {
        name: 'Header',
        components:{
            Login
        },
        data() {
            return{
                show: false,
            }
        },
        methods:{
            closeLogin(){
                this.show = false
            },
            openLogin(){
                this.show = true
            }
        }
    }
</script>

<style scoped>
    *{
        box-sizing: border-box;
    }
    a{
        text-decoration: none;
        color:white
    }
    .nav{
        min-height: 64px;
        width: 100%;
        background-color: #D63031;
        display: flex;
        align-items: center;
        justify-content: space-evenly;
        
    }

    .logo{
        display: flex;
        align-items: center;
        cursor: pointer;
    }
    .logo>a>h1{
        margin-left: 10px;
        color: white;
        letter-spacing: 3px;
        margin-top: 4px ;
        font-size: 32px;
    }

    .search {
        width: 25%;
        display: flex;
        align-items: center;
        box-shadow: 0 2px 2px 0 rgb(0 0 0 / 14%), 0 1px 5px 0 rgb(0 0 0 / 12%), 0 3px 1px -2px rgb(0 0 0 / 20%);
        background: #FFF;
        border-radius: 10px;
        box-sizing: border-box;
        text-align: center;
        border-radius: 5px;
        box-shadow: 0 1px 6px 0 rgb(32 33 36 / 12%);
        position: relative;
        border: #636E72 solid 1px;
        margin-right: 100px;
    }

    .search>img {
        width: 24px;
        height: 24px;
        position: absolute;
        right: 0;
    }

    #searchInput {
        background: transparent url(/images/search.svg) center left no-repeat;
        border: none;
        color: black;
        font-size: 16px;
        height: 36px;
        outline: none;
        padding: 0px 50px 0px 0px;
        position: relative;
        flex-shrink: 0;
        width: 100%;
        margin-left: 16px;
        margin-right: 16px;
    }

    .control-group{
        display: flex;
        align-items: center;
        color: white;
    }

    .control-group>button>a{
        text-decoration: none;
        color: white;
    }

    .signup-button{
        width: 100px;
        height: 30px;
        margin: 0 10px;
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 5px;
        border: black solid 1px;
    }

    .login-button{
        cursor: pointer;
        width: 100px;
        height: 30px;
        margin: 0 10px;
        background-color: rgba(0, 0, 0, 0.6);
        border-radius: 5px;
        border: white solid 1px;
    }

    .signup-button:hover{
        background-color: rgba(255, 255, 255, 0.25);
    }

    .login-button:hover{
        background-color: rgba(0, 0, 0, 0.4);
    }
    
    

    .control-group>.signup-button>a{
        color:black;
        font-weight: bold;
    }

    .control-group>.login-button>a{
        font-weight: bold;
    }

    .control-group>img{
        margin: 0 10px;
    }

    .login{
        position: fixed;
        height: 635px;
        width: 1075px;
        top: 15vh;
        z-index: 10;
        background-color: white;
        border-radius: 5px;
    }


    .bg-blur{
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(0, 0, 0, 0.4);
        z-index: 10;
    }

    

    @media only screen and (max-width: 1200px) {
        .nav{
            padding: 0 30px;
        }
        .search{
            margin-left: 50px;
        }
    }

    @media only screen and (max-width: 660px) {
        .nav{
            padding: 0 10px;
            width: 100vw;
        }
        .search{
            padding: 0 10px;
            visibility: hidden;
            position: absolute;
        }

        .logo>h1{
            color: white;
            margin-top: 4px ;
            font-size: 24px;
        }
        .logo>img{
            width: 30px;
            height: 30px;
        }
    }


    
    


</style>
