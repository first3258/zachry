<template>
    <div class="container-filter">
        <div class="filter-group">
            <img src="../assets/icon/menu.png" alt="">
            <a href="">สินค้าใหม่</a>
            <a href="">สินค้าขายดี</a>
            <a href="">สินค้าลดราคา</a>
        </div>

    </div>
 
</template>

<script>
    
    export default {
        name: 'FilterMenu',
    }
</script>

<style>
    .container-filter{
        max-width: 1440px;
        margin: 56px auto 0 auto;
    }
    .filter-group{
        display: flex;
    }
    .filter-group>img{
        cursor: pointer;
    }
    .filter-group>a{
        text-decoration: none;
        color:black;
        border: 2px solid black;
        border-radius: 20px;
        width: 124px;
        height: 44px;
        padding: 10px;
        text-align: center;
        margin-left: 20px;
    }
    

    .carousel * {
        margin-top: 10px;
        box-sizing: border-box;
        border-radius: 5px;
        width: 100%;
    }
    
    .carousel__prev{
        width: 40px;
        height: 40px;
        border-radius: 50%;
        margin-top: 0;
        margin-left: 30px;
        padding: 0;
        background-color: #4A4A4A;
    }

    .carousel__next{
        width: 40px;
        height: 40px;
        border-radius: 50%;
        margin-top: 0;
        margin-right: 30px;
        padding: 0;
        background-color: #4A4A4A;
    }

    .carousel__icon{
        width: 40px;
        height: 40px;
        margin-top: 0;
    }

    .carousel__pagination-button{
        background-color: #adadad;
        height: 0.5em;
    }

    .carousel__pagination-button.carousel__pagination-button--active{
        background-color: black;
    }


    .carousel{
        position: relative;
        overflow: hidden;
    }

    .carousel__pagination{
        position: absolute;
        bottom: -5px;
        left: -4px;
        padding: 0;
    }

    

   
    
</style>
