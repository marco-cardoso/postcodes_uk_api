# Requirements

<ul>
    <li>Docker 19.03.12</li>
    <li>Docker compose 1.26.2 </li>
</ul>

# How to execute it ?

    docker-compose up
    
# Available ENDPOINTS

    /validate?postcode=ECB1A2
    It validates the given postcode
    
    /format?area=SW&district=1W&sector=0&unit=NY
    It validates each part of the postcode and returns a string with it
    
