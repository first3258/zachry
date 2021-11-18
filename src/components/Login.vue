<template>

<div class = "content">
    <div class="text">
      <img src="../assets/book.svg" />
      <h1>ZACKRY</h1>
    </div>

    <div class = "tab">
        <h1 style="color:#2D3436; font-size: 36px;">Log in</h1>
        <input
          type="text"
          placeholder="Username"
        />
        <input
          type="text"
          placeholder="Password"
        />
        <h1 class = "forget" style="color:#636E72; font-size: 12px; right :0px;">Forgot your password?</h1>
        <div class = "login">
            Log In
        </div>
        <h1 style="color:#636E72; font-size: 12px;">Create account</h1>
    </div>
  
</div>


</template>

<script>
  export default{
      name : "Login",
  }
</script>

<style scoped>

.forget {
  text-align: end;
}

h1 {
  font-family: "IBM Plex", Times, serif;
}

input {
  cursor: pointer;
  width: 240px;
  border-radius: 2px;
  font-size: 18px;
  color: #2D3436;
  border: 1px solid #636E72;
  padding: 10px;
}

.content {
  
  height: calc(100vh - 64px);
  width:100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

}

.login {
  margin-top: 60px;
  width: 240px;
  padding: 10px;
  background-color: #F26D64;
  border-radius: 2px;
  color :white;
  display: flex;
  font-size: 18px;
  align-items: center;
  justify-content: center;
}


.text {
  display: flex;
  color: #F40000;
  display: flex;
  padding: 0 18vw;
  align-items: center;
  font-size: 16px;

}
.tab {
  display:flex;
  flex-direction: column;
  margin: 20px;
  left:0px;
  justify-content: space-between;
  height: 300px;

}
</style>
