const app = Vue.createApp({
    el: '#app',
    // app.config.compilerOptions.delimiters = ['${', '}'],
    delimiters: ['[[', ']]'],
    data() {
        return {
            bodyNoteRaw: '',
            titleNoteRaw: '',
            savedNotes: [],
            focusedNote: [],
            currentFocus: 0,
        }
    },
    methods: {
        notes() {
            let localTitle = this.titleNoteRaw
            let localBody = this.bodyNoteRaw
            console.log(localTitle)
            if (localTitle && localBody != ''){
                let noteObj = {
                    'title': localTitle,
                    'body': localBody
                }
                this.savedNotes.push(noteObj)
                this.saveNote(localTitle, localBody)
                this.bodyNoteRaw = ''
                this.titleNoteRaw = ''
            }
            // Move this to it's own function
            
        },
        load_notes(){
            axios({
                url: "{% url 'keepCloneApp:db_notes' %}",
                method: 'get',
            }).then(response => {
                console.log(response.data.notes)
                this.savedNotes = response.data.notes
            })
        },
        saveNote(title, body){
            let form_data = new FormData()
            form_data.append('title', title)
            form_data.append('note_body', body)

            axios({
                url: "{% url 'keepCloneApp:save_note' %}",
                method: 'post',
                data: form_data,
                headers: {
                    "X-CSRFToken": "{{ csrf_token }}"
                }
            }).then(response => {
                console.log('this')
            })

        },
        noteModal(target) {
            let focusTitle = this.savedNotes[target].title
            let focusBody = this.savedNotes[target].body
            this.currentFocus = target
            this.focusedNote.pop(0)
            this.focusedNote.pop(1)
            this.focusedNote.push(focusTitle)
            this.focusedNote.push(focusBody)
        },
        editFocusedNote(){
            let editedNoteObj = {
                'title': this.focusedNote[0],
                'body': this.focusedNote[1]
            }
            this.savedNotes[this.currentFocus] = editedNoteObj
            this.currentFocus = 0
        },
        deleteNote(index){
            let deletedNote = this.savedNotes[index]
            this.savedNotes.pop(index)
        }
    },
    created() {
        this.load_notes()
        // this.note()
    }
}).mount('#app')