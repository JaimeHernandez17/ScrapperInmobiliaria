from django.core.exceptions import ValidationError


def validator(file):
    """
    This function is to validate the extension and size of the file

    :param file:
    :return: ValidationError or Boolean
    """
    file_type = file.name[::-1].split('.')[0][::-1]
    if file_type == 'csv':
        if int(file.size) < 100000000:
            return True
        raise ValidationError('The file must weight 100 MB maximum')
    raise ValidationError('The file extension must be .csv')


