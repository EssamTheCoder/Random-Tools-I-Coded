let root = document.querySelector(`:root`).style;

//Banner Easter Egg
let colourTheme = `pink`;
const banner = document.getElementById("rticBanner")
banner.addEventListener("click", () => {
    if(colourTheme == `pink`){
        colourTheme = `red`;
        root.setProperty(`--banner-gradient`,`radial-gradient(at bottom, #ff9c9c, #fe7272 10%, #ff8754, #ffcfcf 85%)`);
        root.setProperty(`--banner-border`,`2px solid #ff6363`);
        root.setProperty(`--tool-border`,`2px solid #fc413e`);
    }
    else{
        colourTheme = `pink`;
        root.setProperty(`--banner-gradient`,`radial-gradient(at bottom, #f2abff, #e88fff 10%, #cdabff, #f6cfff 85%)`);
        root.setProperty(`--banner-border`,`2px solid #e88fff`);
        root.setProperty(`--tool-border`,`2px solid #d843fd`);
    }
});