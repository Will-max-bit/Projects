<template>
    <div class="content" :class="{ active: background }">
        <h2>Our Work</h2>
        <p>lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
            dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex
            ea commodo consequat.
        </p>
        <div class="our-work">
            <img v-for="(photo, idx) in loadPhotos" :key="photo.id" @click="lightBox(idx)" :id="idx" :src="photo"
                alt="picture" :class="{ active: pictureAnimation }" class="pictures">
        </div>
        <transition name="picture" mode="out-in">
            <div v-show="pictureFocus" id="focus-light">
                <button @click="previousPicture">Previous</button>
                <button @click="closeBox">Close</button>
                <button @click="nextPicture">Next</button>
                <img id="light-box" :src="pictureFocus" alt="" :class="{ active: pictureAnimation }" class="pictures">
            </div>
        </transition>
    </div>
</template>
<script>
export default {
    name: 'OurWork',
    data() {
        return {
            index: 0,
            pictureFocus: null,
            background: false,
            pictureAnimation: false,
            leaveInterval: null,
            enterInterval: null,
            previousPictureBtn: null,
            nextPictureBtn: null,
            loadPhotos: [
                'https://images.unsplash.com/photo-1564426622559-5af68da63b96?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8dGF0dG9vfGVufDB8MXwwfHx8MA%3D%3D&auto=format&fit=crop&w=900&q=60',
                'https://plus.unsplash.com/premium_photo-1670431913922-272dfdb46f57?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8dGF0dG9vfGVufDB8MXwwfHx8MA%3D%3D&auto=format&fit=crop&w=900&q=60',
                'https://images.unsplash.com/photo-1568515045052-f9a854d70bfd?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1yZWxhdGVkfDN8fHxlbnwwfHx8fHw%3D&auto=format&fit=crop&w=900&q=60',
                'https://images.unsplash.com/photo-1611501275019-9b5cda994e8d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8dGF0dG9vfGVufDB8MXwwfHx8MA%3D%3D&auto=format&fit=crop&w=900&q=60',
                'https://images.unsplash.com/photo-1586243287039-23f4c8e2e7ab?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fHRhdHRvb3xlbnwwfDF8MHx8fDA%3D&auto=format&fit=crop&w=900&q=60',
                'https://images.unsplash.com/photo-1627458514257-41d0ea46e326?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fHRhdHRvb3xlbnwwfDF8MHx8fDA%3D&auto=format&fit=crop&w=900&q=60',
                'https://images.unsplash.com/photo-1624981015342-37a67019b43b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mjd8fHRhdHRvb3xlbnwwfDF8MHx8fDA%3D&auto=format&fit=crop&w=900&q=60',
                'https://images.unsplash.com/photo-1557286581-db6c124a6e2f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzB8fHRhdHRvb3xlbnwwfDF8MHx8fDA%3D&auto=format&fit=crop&w=900&q=60',
                'https://images.unsplash.com/photo-1617196556242-d0de7c06a13e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzN8fHRhdHRvb3xlbnwwfDF8MHx8fDA%3D&auto=format&fit=crop&w=900&q=60',
                'https://images.unsplash.com/photo-1611216560905-158476a4654c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzZ8fHRhdHRvb3xlbnwwfDF8MHx8fDA%3D&auto=format&fit=crop&w=900&q=60',
                'https://images.unsplash.com/photo-1627458514257-41d0ea46e326?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fHRhdHRvb3xlbnwwfDF8MHx8fDA%3D&auto=format&fit=crop&w=900&q=60',
                'https://images.unsplash.com/photo-1513078094721-e7b6e0394a6a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mjh8fHRhdHRvb3xlbnwwfDF8MHx8fDA%3D&auto=format&fit=crop&w=900&q=60',
            ]
        }
    },
    methods: {
        // Enlarge the picture, center it, and blur the background
        lightBox(idx) {
            this.index = idx
            this.previousPictureBtn = idx - 1
            this.nextPictureBtn = idx + 1
            const picture = this.loadPhotos[idx]
            this.pictureFocus = picture
            let pictureStyle = document.getElementById('light-box')
            let ourWork = document.querySelector('.our-work')
            pictureStyle.style.transform = ''
            pictureStyle.style.position = 'absolute';
            pictureStyle.style.width = '30%';
            pictureStyle.style.top = '30vh';
            pictureStyle.style.left = 'calc(50% - 15rem)';
            pictureStyle.style.height = 'auto';
            pictureStyle.style.marginBottom = '10rem';
            pictureStyle.style.boxShadow = '0 2px 8px rgba(0, 0, 0, 0.26)'
            pictureStyle.style.borderRadius = '2px';
            pictureStyle.style.padding = '1rem';
            pictureStyle.style.backgroundColor = 'white';
            pictureStyle.style.zIndex = 99;
            pictureStyle.style.border = 'none';
            this.background = true;
            this.pictureAnimation = true
            ourWork.style.filter = 'blur(5px)'
        },
        // Close the picture, unblur the background
        closeBox() {
            let pictureStyle = document.getElementById('light-box')
            let round = 1;
            this.leaveInterval = setInterval(() => {
                pictureStyle.style.opacity = 1 - round * 0.01;
                round++
                if (round === 50) {
                    pictureStyle.style.opacity = null;
                    clearInterval(this.leaveInterval)
                    this.pictureFocus = null
                    this.background = false;
                    this.pictureAnimation = false
                    let ourWork = document.querySelector('.our-work')
                    ourWork.style.filter = 'blur(0px)'
                    this.pictureAnimation = true
                }
            }, 10)
        },
        // Previous and next buttons
        previousPicture() {
            this.pictureAnimation = true
            if (this.index === 0) {
                this.index = this.loadPhotos.length - 1
            } else {
                this.index--
            }

            this.pictureFocus = this.loadPhotos[this.index]

        },
        nextPicture() {
            this.pictureAnimation = true
            if (this.index === this.loadPhotos.length - 1) {
                this.index = 0
            } else {
                this.index++
            }

            this.pictureFocus = this.loadPhotos[this.index]
        },

    },
}
</script>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Alfa+Slab+One&family=Handjet&family=Noto+Serif+Display:ital,wght@1,300&family=Sedgwick+Ave+Display&display=swap');

.our-work {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    margin: 20px;
    width: 80vw;
}

.pictures {
    transition: scale 2s ease;
}

.pictures:hover {
    scale: 1.1;
    box-shadow: 0 0 2px 2px rgba(0, 0, 0, 0.2);
}




h2 {
    font-family: 'Alfa Slab One', serif;
    color: #b3adad;
    text-align: center;
    margin: 20px;
    font-size: 2rem;
}

p {
    color: #b3adad;
    text-align: center;
    margin: 20px;
    width: 40vw;
    font-size: 1.5rem;
    font-family: 'Playfair Display', serif;
}

img {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 10vw;
    height: auto;
    margin: 0 1rem 0 1rem;
}

button {
    z-index: 100;
    margin-top: 10%;
    margin-bottom: 0 !important;
    border-radius: 30px;
    width: 10%;
    padding: 5px;
    line-height: 2;
    background: gray !important;
    border: gray;
    text-align: center;


}

.active {
    background-color: black !important;
}

.pictures.active {
    animation: picture-in-out 0.8s ease-in;
}

.content {
    display: flex;
    flex-direction: column;
    align-items: center;
}

@keyframes picture-in-out {
    from {
        opacity: 0;
        transform: scale(0.9);
    }

    to {
        opacity: 1;
        transform: scale(1);
    }

}

.picture-enter-active,
.picture-leave-active {
    transition: opacity 1s ease-out;
}

.picture-enter-from,
.picture-leave-to {
    transition: opacity 1s ease-out;
    opacity: 0;
}

#focus-light>button {
    background: white;
    margin-bottom: 10%;

}

#focus-light {
    display: flex;
    justify-content: space-around;
    width: 100vw;
}
</style>