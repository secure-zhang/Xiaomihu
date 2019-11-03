    $(function () {
        editormd("fancy-editormd", {
            // width: "100%", 请不要添加
            height: 640,
            syncScrolling: "single",
            path: "{{ url_for('static',filename='editor/lib/') }}",
            saveHTMLToTextarea : true
        });
    });
    var uploaderFile = document.querySelector('#uploaderFile');
    uploaderFile.addEventListener('change', function () {
     lrz(this.files[0])
            .then(function (rst) {
                // 处理成功会执行
                console.log(rst.base64);
                var img64base = document.querySelector('#img64base');
                 img64base.value=rst.base64;
                 uploaderFile.value='ok'
            })
            .catch(function (err) {
                // 处理失败会执行
            })
            .always(function () {
                // 不管是成功失败，都会执行
            });
    });