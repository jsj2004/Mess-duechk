const xhr=new XMLHttpRequest();
xhr.open('GET','https://reqres.in/api/users')
xhr.responseType='json';
xhr.onload=()=>
{
    const data=xhr.response;
    console.log(data);
}
xhr.send();
