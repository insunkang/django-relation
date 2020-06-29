const likeButton = document.querySelectorAll('.like-button')
likeButton.forEach(button => {
    button.addEventListener('click', function(event){
        console.log(event)
        const articleId = event.target.dataset.id
        const likeCount = document.querySelector(`.like-count-${articleId}`)
        axios.defaults.xsrfCookieName = 'csrftoken';
        axios.defaults.xsrfHeaderName = 'X-CSRFToken';

        // axios.get(`/articles/${articleId}/like/`)
        axios.post(`/articles/${articleId}/like/`)
        .then(response => {
            likeCount.innerText = response.data.count
            if (response.data.liked){
                event.target.className = 'fas fa-heart fa-lg like-button'
                event.target.style.color = 'crimson'
            }else{
                event.target.className = 'far fa-heart fa-lg like-button'
                event.target.style.color = 'black'
            }
        })
    })
})