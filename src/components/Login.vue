<template>

<div class = "content">

  <div class="left-logo">
    <img src="../assets/book.svg" alt="">
    <h1>ZACKRY</h1>
  </div>

  <div class="line"></div>

  <div class="login">
    <h1 style="color: #2D3436">Login</h1>

    <div class="input">
      <div class="username">
        <input type="text" placeholder="Username">
        <img src="../assets/icon/People.svg" alt="">
      </div>
      <div class="username">
        <input type="password" placeholder="Password">
        <img src="../assets/icon/password.svg" alt="" >
      </div>
    </div>

    <div class="group">
      <p>Create account </p>
      <p> Forgot your password?</p>
    </div>

    <button class="submit" >
      Log in
    </button>

    <div class="close" @click="$emit('close')">
        <img src="../assets/icon/close.svg" alt="">
    </div>

  </div>

</div>


</template>

<script>
  export default{
      name : "Login",
      data(){
        return{
          show: true
        }
      },
      methods: {
        closeLogin () {
          this.show = false
        }
    }
  }
</script>

<style scoped>
  .content{
    position: relative;
    width: 1075px;
    height: 635;
    background-color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 10;
  }

  .line{
    background-color: black;
    height: 360px;
    width: 3px;
    margin: 0 100px;
  }
 
  .left-logo{
    display: flex;
    align-items: center;
  }

  .left-logo>h1{
    font-size: 54px;
    font-weight: bold;
    letter-spacing: 2px;
    margin-left: 20px;
    color: #F40000;
  }

  .login{
    height: 200px;
    width: 282px;
    
  }

  .username{
    width: 100%;
    height: 40px;
    margin-top: 15px;
    display: flex;
    align-items: center;
    box-shadow: 0 2px 2px 0 rgb(0 0 0 / 14%), 0 1px 5px 0 rgb(0 0 0 / 12%), 0 3px 1px -2px rgb(0 0 0 / 20%);
    background: #FFF;
    border-radius: 10px;
    box-sizing: border-box;
    border-radius: 5px;
    box-shadow: 0 1px 6px 0 rgb(32 33 36 / 12%);
    position: relative;
    border: #636E72 solid 1px;
  }

  .input>div>input{
      background: transparent url(/images/search.svg) center left no-repeat;
      border: none;
      color: black;
      font-size: 16px;
      height: 36px;
      outline: none;
      padding: 0px 50px 0px 0px;
      position: relative;
      flex-shrink: 0;
      width: 80%;
      margin-left: 16px;
      margin-right: 16px;
  }

  .group{
    margin-top: 10px;
    display: flex;
    font-size: 12px;
    justify-content: space-between;
    color: #636E72;
  }

  .submit{
    width: 100%;
    height: 40px;
    font-size: 18px;
    font-weight: bold;
    background-color: #F26D64;
    border:none;
    margin-top: 10px;
    border-radius: 2px;
    color: white;
  }


.close{
  position: absolute;
  z-index: 10;
  top: 20px;
  right: 20px;
  cursor: pointer;
}



</style>
