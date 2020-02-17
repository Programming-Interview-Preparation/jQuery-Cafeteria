<div class="row">
    <div>
        <label for="image" class="control-label">profile Image</label>
        <input type="file" name="profile_image" class="form-control" id="imgInp"
               accept=".jpeg,.png,.jpg,.gif,.svg">

        {% if profile.image %}
            <p>
                <img style="border-radius: 50%;" id="tag_hide"
                     src="/{{ profile.image.url }}" alt="profile Image"
                     height="80px" width="80px"/>
                <span style=" cursor: pointer;" class="close">&times;</span>
            </p>
        {% endif %}

        <img style="border-radius: 50%;visibility: hidden;" id="blah" src=""
             alt="profile Image"
             height="80px" width="80px"/>

        <p></p>
        <input type="hidden" name="checkimage" id="checkimage" value="{% if profile.image %}{{ profile.image }}{% else %}{% endif %}">
    </div>
</div>

<script>
    var closebtns = document.getElementsByClassName("close");
    var i;
    for (i = 0; i < closebtns.length; i++) {
        closebtns[i].addEventListener("click", function () {
            this.parentElement.style.display = 'none';
            document.getElementById("checkimage").value = "";
        });
    }
</script>

<script>
    document.getElementById("imgInp").onclick = function () {
        document.getElementById("blah").style.visibility = "visible";
        $("#tag_hide").hide();
    };

    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#blah').attr('src', e.target.result);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }

    $("#imgInp").change(function () {
        readURL(this);
    });
</script>