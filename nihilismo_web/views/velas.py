import reflex as rx
from nihilismo_web.styles.styles import Size, Color
import nihilismo_web.styles.styles as styles

def velas() -> rx.Component:
    return rx.container(
    rx.html(
        '''
            <style>
                .holder {
                    margin: 12rem auto 0;
                    width: 150px;
                    height: 400px;
                    position: relative;
                }

                .holder *, .holder *:before, .holder *:after {
                    position: absolute;
                    content: "";
                }

                .candle {
                    bottom: 0;
                    width: 150px;
                    height: 300px;
                    border-radius: 150px / 40px;
                    -webkit-box-shadow: inset 20px -30px 50px 0 rgba(0, 0, 0, 0.4), inset -20px 0 50px 0 rgba(0, 0, 0, 0.4);
                    box-shadow: inset 20px -30px 50px 0 rgba(0, 0, 0, 0.4), inset -20px 0 50px 0 rgba(0, 0, 0, 0.4);
                    background: #190f02;
                    background: -webkit-gradient(linear, left top, left bottom, from(#e48825), color-stop(#e78e0e), color-stop(#833c03), color-stop(50%, #4c1a03), to(#1c0900));
                    background: linear-gradient(#e48825, #e78e0e, #833c03, #4c1a03 50%, #1c0900);
                }

                .candle:before {
                    width: 100%;
                    height: 40px;
                    border-radius: 50%;
                    border: 2px solid #d47401;
                    background: #b86409;
                    background: radial-gradient(#ffef80, #b86409 60%);
                    background: radial-gradient(#eaa121, #8e4901 45%, #b86409 80%);
                }

                .candle:after {
                    width: 34px;
                    height: 10px;
                    left: 50%;
                    -webkit-transform: translateX(-50%);
                    -ms-transform: translateX(-50%);
                    transform: translateX(-50%);
                    border-radius: 50%;
                    top: 14px;
                    -webkit-box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.5);
                    box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.5);
                    background: radial-gradient(rgba(0, 0, 0, 0.6), transparent 45%);
                }

                .thread {
                    width: 6px;
                    height: 36px;
                    top: -17px;
                    left: 50%;
                    z-index: 1;
                    border-radius: 40% 40% 0 0;
                    -webkit-transform: translateX(-50%);
                    -ms-transform: translateX(-50%);
                    transform: translateX(-50%);
                    background: #121212;
                    background: -webkit-gradient(linear, left top, left bottom, from(#d6994a), color-stop(#4b232c), color-stop(#121212), color-stop(black), color-stop(90%, #e8bb31));
                    background: linear-gradient(#d6994a, #4b232c, #121212, black, #e8bb31 90%);
                }
            
                .flame {
                    width: 24px;
                    height: 120px;
                    left: 50%;
                    -webkit-transform-origin: 50% 100%;
                    -ms-transform-origin: 50% 100%;
                    transform-origin: 50% 100%;
                    -webkit-transform: translateX(-50%);
                    -ms-transform: translateX(-50%);
                    transform: translateX(-50%);
                    bottom: 100%;
                    border-radius: 50% 50% 20% 20%;
                    background: rgba(255, 255, 255, 1);
                    background: -webkit-gradient(linear, left top, left bottom, color-stop(80%, white), to(transparent));
                    background: linear-gradient(white 80%, transparent);
                    -webkit-animation: moveFlame 6s linear infinite, enlargeFlame 5s linear infinite;
                    animation: moveFlame 6s linear infinite, enlargeFlame 5s linear infinite;
                }

                .flame:before {
                    width: 100%;
                    height: 100%;
                    border-radius: 50% 50% 20% 20%;
                    -webkit-box-shadow: 0 0 15px 0 rgba(247, 93, 0, .4), 0 -6px 4px 0 rgba(247, 128, 0, .7);
                    box-shadow: 0 0 15px 0 rgba(247, 93, 0, .4), 0 -6px 4px 0 rgba(247, 128, 0, .7);
                }

                @-webkit-keyframes moveFlame {
                    0%, 100% {
                        -webkit-transform: translateX(-50%) rotate(-2deg);
                        transform: translateX(-50%) rotate(-2deg);
                    }

                    50% {
                        -webkit-transform: translateX(-50%) rotate(2deg);
                        transform: translateX(-50%) rotate(2deg);
                    }
                    }

                    @keyframes moveFlame {
                    0%, 100% {
                        -webkit-transform: translateX(-50%) rotate(-2deg);
                        transform: translateX(-50%) rotate(-2deg);
                    }

                    50% {
                        -webkit-transform: translateX(-50%) rotate(2deg);
                        transform: translateX(-50%) rotate(2deg);
                    }
                    }

                    @-webkit-keyframes enlargeFlame {
                    0%, 100% {
                        height: 120px;
                    }

                    50% {
                        height: 140px;
                    }
                    }

                    @keyframes enlargeFlame {
                    0%, 100% {
                        height: 120px;
                    }

                    50% {
                        height: 140px;
                    }
                    }
                .glow {
                    width: 26px;
                    height: 60px;
                    border-radius: 50% 50% 35% 35%;
                    left: 50%;
                    top: -48px;
                    -webkit-transform: translateX(-50%);
                    -ms-transform: translateX(-50%);
                    transform: translateX(-50%);
                    background: rgba(0, 133, 255, .7);
                    -webkit-box-shadow: 0 -40px 30px 0 #dc8a0c, 0 40px 50px 0 #dc8a0c, inset 3px 0 2px 0 rgba(0, 133, 255, .6), inset -3px 0 2px 0 rgba(0, 133, 255, .6);
                    box-shadow: 0 -40px 30px 0 #dc8a0c, 0 40px 50px 0 #dc8a0c, inset 3px 0 2px 0 rgba(0, 133, 255, .6), inset -3px 0 2px 0 rgba(0, 133, 255, .6);
                }

                .glow:before {
                    width: 70%;
                    height: 60%;
                    left: 50%;
                    -webkit-transform: translateX(-50%);
                    -ms-transform: translateX(-50%);
                    transform: translateX(-50%);
                    bottom: 0;
                    border-radius: 50%;
                    background: rgba(0, 0, 0, 0.35);
                }

                .blinking-glow {
                    width: 100px;
                    height: 180px;
                    left: 50%;
                    top: -55%;
                    -webkit-transform: translateX(-50%);
                    -ms-transform: translateX(-50%);
                    transform: translateX(-50%);
                    border-radius: 50%;
                    background: #ff6000;
                    -webkit-filter: blur(50px);
                    -moz-filter: blur(60px);
                    -o-filter: blur(60px);
                    -ms-filter: blur(60px);
                    filter: blur(60px);
                    -webkit-animation: blinkIt .1s infinite;
                    animation: blinkIt .1s infinite;
                }

                @-webkit-keyframes blinkIt {
                    50% {
                        opacity: .8;
                    }
                }

                @keyframes blinkIt {
                    50% {
                        opacity: .8;
                    }
                }    
            </style>
            
             <div class="holder">
                <div class="candle">
                <div class="blinking-glow"></div>
                <div class="thread"></div>
                <div class="glow"></div>
                <div class="flame"></div>
                </div>
            </div>
        '''
    ),
    )