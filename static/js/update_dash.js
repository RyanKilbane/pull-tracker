function wrapper(){
        
    getData()
    function getData(){
        $.ajax({
            type: 'GET',
            url: '/pulls'
        }).done(updateCardContainer)
    }

    function updateCardContainer(data){
        $("#card_container").empty();
        var repos = JSON.parse(data);
        for (var i=0; i < repos.length; i++){
            for (var key in repos[i]){
                for(var j=0; j < repos[i][key].length; j++){
                    console.log(repos[i][key][j].pull_name)
                    var html = `<div class=repo_card><div class=container>`
                    html += `<h4><b>${key}</h4></b>`
                    html += `<p>${repos[i][key][j].pull_name}</p>`
                    html += `</div></div>`;
                    $("#card_container").append(html)
                }
            }
        }
    }
}
setInterval(wrapper, 10000)