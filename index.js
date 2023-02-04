const xhr=new XMLHttpRequest();
xhr.open('GET','https://127.0.0.1:8000/rinp')
xhr.responseType='json';
xhr.onload=()=>
{
    const data=xhr.response;
    console.log(data);
}
xhr.send();
