$(document).ready(function () {

    $('#codrops-nav').click(function () {
        $('#codrops-nav').toggleClass('open');
    });

    $(".accordion dd").hide().prev().click(function () {
        $(this).parents(".accordion").find("dd").not(this).slideUp().prev().removeClass("active");
        $(this).next().not(":visible").slideDown().prev().addClass("active");
    });


    // $('input, select').styler();
    // $('.js-example-basic-multiple').styler('destroy');
    // $(".js-example-basic-multiple").select2({
    //     maximumSelectionLength: 1
    // });
    // $('.input-group.date').datetimepicker({
    //     format: 'DD.MM.YYYY',
    //     locale: 'ru'
    // });

    $.validator.addMethod("validName", function (value, element) {
        return this.optional(element) || /^[а-яА-ЯёЁ ]+$/i.test(value);
    }, "Используйте пожалуйста кириллицу");

    $.validator.addMethod("validRegNumber", function (value, element) {
        return this.optional(element) || /^[0-9-а-яА-ЯёЁ]+$/i.test(value);
    }, "Используйте кириллицу и цифры");

    $.validator.methods.email = function (value, element) {
        return this.optional(element) || /[\.\-\_ a-z-0-9]+@[a-z-0-9]+\.[a-z-0-9]+/.test(value);
    };


    $.validator.methods.phone = function (value, element) {
        return this.optional(element) || /[\ \+\-\(\) 0-9]/.test(value);
    };

    $.validator.addMethod("validDate", function (value, element) {
        return this.optional(element) || /(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d/.test(value);
    }, "Не верный формат");


    $(function () {
        $("#id_phone").mask("+7 (999) 999-9999");
        $("#id_Date").mask("99.99.9999", {placeholder: "дд.мм.гггг"});
    });

    $("#form-create-card").validate({
        rules: {
            FName: {
                required: true,
                validName: true
            },
            Name: {
                required: true,
                validName: true
            },
            MName: {
                required: true,
                validName: true
            },
            phone: {
                required: true,
                minlength: 14
            },
            email: {
                required: true,
                email: true
            },
            VehicleCategory2: {
                required: true
            },
            Make: {
                required: true
            },
            Model: {
                required: true
            },
            Year: {
                required: true,
                number: true,
                min: 1950,
                max: 2017
            },
            VIN: {
                minlength: 17,
                maxlength: 17
            },
            BodyNumber: {
                minlength: 17,
                maxlength: 17
            },
            FrameNumber: {
                minlength: 17,
                maxlength: 17
            },
            RegistrationNumber: {
                minlength: 8,
                maxlength: 9,
                validRegNumber: true
            },
            Killometrage: {
                required: true,
                number: true
            },
            EmptyMass: {
                required: true,
                number: true
            },
            MaxMass: {
                number: true
            },
            Fuel: {
                required: true
            },
            Tyres: {
                required: true
            },
            DocumentType: {
                required: true
            },
            Series: {
                required: true,
                validRegNumber: true,
                minlength: 4,
                maxlength: 4

            },
            Number: {
                required: true,
                number: true,
                minlength: 6,
                maxlength: 6
            },
            Organization: {
                required: true
            },
            Date: {
                required: true,
                validDate: true
            }
        },

        messages: {
            FName: {
                required: "Имя должно быть заполнено",
                validName: "Используйте пожалуйста кириллицу"
            },
            Name: {
                required: "Фамилия должна быть заполнена",
                validName: "Используйте пожалуйста кириллицу"
            },
            MName: {
                required: "Отчество должно быть заполнено",
                validName: "Используйте пожалуйста кириллицу"
            },
            phone: {
                required: "Телефон обязателен для заполнения",
                number: "Используйте только цифры",
                minlength: "Введите корректный номер телефона"
            },
            email: {
                required: "E-mail обязателен для заполнения",
                email: "Введите корректный E-mail"
            },
            VehicleCategory2: {
                required: "Выберете категорию"
            },
            Make: {
                required: "Укажите марку ТС"
            },
            Model: {
                required: "Укажите модель ТС"
            },
            Year: {
                required: "Укажите год",
                number: "Используйте только цифры",
                min: "с 1950г.",
                max: "по 2017г."
            },
            VIN: {
                minlength: "VIN состоит из 17-ти символов",
                maxlength: "VIN состоит из 17-ти символов"

            },
            BodyNumber: {
                minlength: "Номер кузова состоит из 17-ти символов",
                maxlength: "Номер кузова состоит из 17-ти символов"
            },
            FrameNumber: {
                minlength: "Номер Раммы/Шасси состоит из 17-ти символов",
                maxlength: "Номер Раммы/Шасси состоит из 17-ти символов"
            },
            RegistrationNumber: {
                minlength: "Мин. кол-во символов 8",
                maxlength: "Макс. кол-во символов 9",
                validRegNumber: "Используйте кириллицу и цифры"
            },
            Killometrage: {
                required: "Пробег должен быть указан",
                number: "Используйте только цифры"
            },
            EmptyMass: {
                required: "Заполните массу без нагрузки",
                number: "Используйте только цифры"
            },
            MaxMass: {
                number: "Используйте только цифры"
            },
            Fuel: {
                required: "Выберете топливо"
            },
            Tyres: {
                required: "Заполните марку шин"
            },
            DocumentType: {
                required: "Выберете тип документа"
            },
            Series: {
                required: "Заполните серию документа",
                validRegNumber: "Используйте кириллицу и цифры",
                minlength: "Должно быть 4 символа",
                maxlength: "Должно быть 4 символа"
            },
            Number: {
                required: "Заполните номер документа",
                number: "Используйте только цифры",
                minlength: "Должно быть 6 цифр",
                maxlength: "Должно быть 6 цифр"
            },
            Organization: {
                required: "Заполните кем выдан документ"
            },
            Date: {
                required: "Заполните дату выдачи",
                validDate: "Не верный формат"
            }
        }
    });


    $('.next-1').click(function () {
        if ($("#id_FName, #id_Name, #id_MName, #id_phone, #id_email").valid()) {
            $('.first-step').fadeOut();
            $('.second-step').fadeIn();
            $('.step-1').removeClass('active');
            $('.step-2').addClass('active');
            $('.step-1').addClass('done');
        } else {
            $('label.error').parent('.jq-selectbox').addClass('error');
            $('label.error').next('.select2').addClass('error');
        }
        return false
    });

    var form = $('#form-create-card');
    var preview = $('#results');

    function writePreview(event) {

        event.preventDefault();

        var field = form.find('.field');

        var previewList = '';

        field.each(function (index, el) {

            var fieldValue = $(el).val();
            var fieldLabel = $(el).prev('label');
            var fieldTitle = fieldLabel.text();

            if (fieldValue.length <= 0) {
                fieldValue = 'ОТСУТСТВУЕТ';
            }

            console.log(fieldValue);

            previewList += '<div class="check-list-info"><b>' + fieldTitle + '</b>: ' + fieldValue + '</div>';

        });

        preview.html(previewList);

    }


    $('.next-2').click(function (event) {
        if ($("#id_VehicleCategory2, #id_Make, #id_Model, #id_Year, #id_VIN, #id_BodyNumber, #id_FrameNumber, #id_RegistrationNumber, #id_Killometrage, #id_EmptyMass, #id_MaxMass, #id_Fuel, #id_Tyres, #id_DocumentType, #id_Series, #id_Number, #id_Organization, #id_Date").valid()) {
            $('.second-step').fadeOut();
            $('.third-step').fadeIn();
            $('.step-2').removeClass('active');
            $('.step-3').addClass('active');
            $('.step-2').addClass('done');

            writePreview(event);

        } else {
            $('label.error').parent('.jq-selectbox').addClass('error');
            $('label.error').next('.select2').addClass('error');
        }
        return false
    });


    $('.next-3').click(function () {
        $('.third-step').fadeOut();
        $('.finish-step').fadeIn();
        $('.step-3').removeClass('active');
        $('.step-3').addClass('done');
        return false
    });

    $('.back-1').click(function () {
        $('.second-step').fadeOut();
        $('.first-step').fadeIn();
        $('.step-1').removeClass('done');
        $('.step-1').addClass('active');
        $('.step-2').removeClass('active');
        return false;
    });

    $('.back-2').click(function () {
        $('.third-step').fadeOut();
        $('.second-step').fadeIn();
        $('.step-2').removeClass('done');
        $('.step-2').addClass('active');
        $('.step-3').removeClass('active');
        return false;
    });


    $('.check-con input').on('change', function () {
        setTimeout(function () {
            $('input, select').trigger('refresh');
        }, 1);

        if ($(this).is(':checked')) {
            $(this).parent().parent().parent().find('input[type=text]').attr('disabled', true);
            var disText = $(this).parent().parent().find('label').text()
            $(this).parent().parent().parent().find('input[type=text]').attr('value', disText);
        } else {
            $(this).parent().parent().parent().find('input[type=text]').attr('disabled', false);
            $(this).parent().parent().parent().find('input[type=text]').attr('value', '');
        }
    });

    $('select').change(function () {
        setTimeout(function () {
            $('input, select').trigger('refresh');
        }, 1);
        $(".js-example-basic-multiple").select2("destroy");
        $(".js-example-basic-multiple").select2({
            maximumSelectionLength: 1
        });
        $(this).parent().find('label.error').hide()
    });

});