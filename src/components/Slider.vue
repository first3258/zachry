<template>
    <div class="container">
        <carousel class="carousel" :autoplay=4000 :transition=2000 :changeDelay=2000 >
            <slide class="slide">
                <img src='../assets/icon/Slide1.png' alt="">
            </slide>
            <slide class="slide">
                <img src='../assets/icon/Slide2.png' alt="">
            </slide>
            <slide class="slide">
                <img src='../assets/icon/Slide3.png' alt="">
            </slide>

            <template #addons>
                <navigation />
                <pagination />
            </template>

            
        </carousel>
    </div>
 
</template>

<script>
    import 'vue3-carousel/dist/carousel.css';
    import { Carousel, Slide, Navigation, Pagination} from 'vue3-carousel';
    export default {
        name: 'Slider',
        components: {
            Carousel,
            Slide,
            Navigation,
            Pagination
        }
    }
</script>

<style>
    .container{
        max-width: 1440px;
        margin: 25px auto 0 auto;
    }

    .carousel * {
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
