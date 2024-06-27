/* 첨부파일 처리 핸들러 */

// csrf_token 초기화
$(function(){ // jquery(비동기 통신) 문법은 $로 시작
    var csrf_token = $('#csrf_token').val();
    $.ajaxSetup({
        beforeSend: function(xhr, settings) { // 통신하기 전에 할 것
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrf_token);
            }
        }
    });
});

var FILE_NUM = 0; // 첨부된 파일 개수
var FILE_ARRAY = new Array(); // 첨부 파일 저장

/* 파일 추가 함수 */
function add_file(obj){
    let max_flie_count = 10; // 해커들이 막 보낼 수 있어서
    let attach_file_count = $('.filebox').length;
    let remain_file_count = max_flie_count - attach_file_count;
    let current_file_count = obj.files.length;
    $('#attached-file-list').attr('hidden', false);

    if(current_file_count > remain_file_count){
        alert(`첨부파일은 최대 ${max_file_count}개 까지 첨부 가능합니다.`);
    } else{
        for (const file of obj.files){
            // 파일 검증
            if (validation(file)){
                let reader = new FileReader();
                reader.readAsDataURL(file); // 파일 읽기
                reader.onload = function(){ // form에서 파일 로드가 끝났을 때
                    FILE_ARRAY.push(file) // 읽기 성공 -> 배열에 저장
                } 

                // 파일 목록을 화면에 추가
                const img_path = '<img src="/static/imgs/delete-doc.ico" width="20px" alt="문서 삭제">'
                let html_data =`
                <div class="filebox my-2 ml-2" id="file${FILE_NUM}">
                    <p class="name">
                        첨부${FILE_NUM + 1}: ${file.name}
                        <span>
                            <a class="delete" onclick="deleteFile(${FILE_NUM});">${img_path}</a>
                        </span>
                    </p>
                </div>`
                $('.file-list').append(html_data);
                FILE_NUM++;
            } else {
                continue;
            }
        }

    }
}

function validation(obj){
    const fileTypes = [
        'application/pdf',
        'application/haansofthwp',
        'application/x-hwp',
        'application/msword', // .doc
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document', // .docx
        'application/vnd.ms-excel', // .xls
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', // .xlsx
        'video/x-msvideo', // .avi
        'application/zip',
        'audio/mpeg',
        'video/mp4',
        'video/mpeg',
        'image/gif',
        'image/jpeg',
        'image/png',
        'image/bmp',
        'image/tif',
        'text/plain', // .txt
        'text/csv', // .csv
    ];

    // 해킹 방지
    if (obj.name.length > 200){ 
        alert("파일명이 200글자 이상인 파일은 제외되었습니다.")
        return false;
    } else if (obj.size > (500 * 1024 * 1024)){
        alert('최대 파일 용량이 500MB를 초과한 파일은 제외되었습니다.')
        return false;
    } else if (obj.name.lastIndexOf('.') == -1){
        alert('확장자가 없는 파일은 제외되었습니다.')
        return false;        
    }else if (!fileTypes.includes(obj.type)){
        alert('지원하지 않는 파일 형식입니다. 첨부 불가 파일은 제외되었습니다.')
        return false;        
    }else{
        return true;
    }
}