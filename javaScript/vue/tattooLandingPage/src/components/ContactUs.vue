<template>
    <div class="contact-us">
        <div class="contact-blurb">
            <h2>Contact Us</h2>
            <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Maxime voluptates facere placeat quis natus saepe
                autem
                consectetur recusandae? Soluta veritatis enim mollitia doloremque dicta id pariatur voluptates ratione eius
                sequi.
                Iste nesciunt ullam reprehenderit, laboriosam at quod consectetur, unde maiores, vero deserunt labore animi
                minus ipsa aliquid temporibus ea eius doloremque obcaecati eaque deleniti quia aspernatur. Nesciunt
                molestias
                repellendus iusto.
                Animi recusandae commodi tempora praesentium hic, fuga veniam repudiandae? Quidem molestiae suscipit in
                distinctio amet, deserunt quibusdam fuga sint ullam beatae? Fugit, nihil incidunt repellat dolor distinctio
                sed
                architecto maiores?</p>
        </div>
        <div class="links">
            <a href="http://" target="_blank" rel="noopener noreferrer"><span class="material-symbols-outlined">
                    photo_camera
                </span></a>
            <a href="http://" target="_blank" rel="noopener noreferrer"><span class="material-symbols-outlined">
                    person
                </span></a>
            <a href="http://" target="_blank" rel="noopener noreferrer"><span class="material-symbols-outlined">
                    music_note
                </span></a>
            <a href="http://" target="_blank" @click="showContactUs" rel="noopener noreferrer"><span
                    class="material-symbols-outlined">
                    mail
                </span></a>
        </div>
        <form action="" id="contact-form" v-show="formFocus">
            <label for="name">Name</label>
            <input v-model="name" type="text" name="name" class="inputs" id="name" placeholder="Enter your name">

            <label for="email">Email</label>
            <input v-model="email" type="email" name="email" class="inputs" id="email" placeholder="Enter your email">

            <label for="message">Message</label>
            <textarea v-model="message" name="message" id="message" cols="30" rows="10" placeholder="Enter your message"
                class="inputs"></textarea>
            <input class="btn-form" @click.prevent="submitForm(); closeContactUs()" type="submit" value="Submit">
        </form>
        <div class="thanks">
            <transition mode="out-in" name="thanks-contacting">
                <h2 open v-if="thanks">Thanks for contacting us!</h2>
            </transition>
        </div>
    </div>
</template>
<script>
export default {
    name: 'ContactUs',
    data() {
        return {
            formFocus: false,
            name: '',
            email: '',
            message: '',
            thanks: false,
            leaveInterval: null,
            enterInterval: null,
        }
    },
    methods: {
        submitForm() {
            this.thanks = true
            this.name = ''
            this.email = ''
            this.message = ''
            setTimeout(() => {
                this.thanks = false
            }, 1500)
        },
        showContactUs() {
            let form = document.getElementById('contact-form')
            let round = 1;
            this.enterInterval = setInterval(() => {
                this.formFocus = true
                form.style.opacity = round * 0.01;
                round++
                if (round === 50) {
                    form.style.opacity = null;
                    clearInterval(this.enterInterval)
                    this.pictureFocus = null
                    this.background = true;
                    this.pictureAnimation = true
                }
            }, 10)
            form.style.position = 'absolute'
            form.style.width = '30%';
            form.style.top = '30vh';
            form.style.left = 'calc(50% - 15rem)';
            form.style.height = 'auto';
            form.style.marginBottom = '10rem';
            form.style.boxShadow = '0 2px 8px rgba(0, 0, 0, 0.26)'
            form.style.borderRadius = '2px';
            form.style.padding = '1rem';
            form.style.zIndex = 99;
            form.style.border = 'none';
            form.style.opacity = 0.8;
            form.style.borderRadius = '30px';
            let background = document.querySelector('.contact-blurb')
            let links = document.querySelector('.links')
            links.style.filter = 'blur(5px)'
            background.style.filter = 'blur(5px)'
        },
        closeContactUs() {
            let form = document.getElementById('contact-form')
            let round = 1;
            this.leaveInterval = setInterval(() => {
                this.formFocus = false
                form.style.opacity = 1 - round * 0.01;
                round++
                if (round === 50) {
                    form.style.opacity = null;
                    clearInterval(this.leaveInterval)
                    this.pictureFocus = null
                    this.background = false;
                    this.pictureAnimation = false
                    let background = document.querySelector('.contact-blurb')
                    let links = document.querySelector('.links')
                    links.style.filter = 'blur(0px)'
                    background.style.filter = 'blur(0px)'
                }
            }, 10)


        },
    }
}
</script>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Alfa+Slab+One&family=Handjet&family=Noto+Serif+Display:ital,wght@1,300&family=Sedgwick+Ave+Display&display=swap');

.contact-us {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.thanks-contacting-enter-active {
    animation: thanks-contacting 0.5s ease-out;
}

.thanks-contacting-leave-active {
    animation: thanks-contacting 0.5s ease-in reverse;
}

@keyframes thanks-contacting {
    from {
        opacity: 0;
        transform: scale(0.9);
    }

    to {
        opacity: 1;
        transform: scale(1);
    }

}

h2 {
    font-family: 'Alfa Slab One', serif;
    font-size: 2rem;
    color: #b3adad;
    text-align: center;
}

p {
    font-family: 'Playfair Display', serif;
    font-size: 1.5em;
    width: 60vw;
}

.inputs {
    border-radius: 30px;
    width: 76%;
    padding: 5px;
    line-height: 2;
    background: gray;
    border: gray;
    text-align: center;
}

.links {
    display: flex;
    justify-content: center;
}

p {
    margin: 0 4em 1rem 4em;
}

.material-symbols-outlined {
    font-size: 2rem;
}

.btn-form {
    font-size: 2rem;
    margin: 1rem auto;
    border: none;
    padding: 15px 20px;
    border-radius: 25px;
    background: rgba(238, 231, 231, 0.58);
}

.links a {
    text-decoration: none;
    color: #b3adad;
    font-size: 2rem;
    margin: 1rem;
}

form {
    display: flex;
    flex-direction: column;
    align-items: center;
}
</style>