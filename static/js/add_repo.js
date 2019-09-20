function getRepoName(){
    return $("#repo_name").val()
}

function showMessage(data){
    var message = JSON.parse(data);
    alert(message.message)
}

function addRepo(){
    var repoName = getRepoName();
    var post_url = "/add?repo="
    post_url += repoName;
    $.ajax({
        type: 'POST',
        url: post_url
    }).done(showMessage)
}
$('#add_button').on('click', addRepo)