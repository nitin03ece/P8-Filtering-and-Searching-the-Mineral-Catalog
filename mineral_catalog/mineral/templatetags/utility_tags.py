from django import template

register = template.Library()


@register.inclusion_tag('mineral/display_groups.html')
def filter_group(bold_group):
    groups = ['Silicates', 'Oxides', 'Sulfates', 'Sulfides', 'Carbonates', 'Halides', 'Sulfosalts',
            'Phosphates', 'Borates', 'Organic Minerals', 'Arsenates', 'Native Elements', 'Other']
    return {'groups' : groups, 'bold_group' : bold_group}


@register.inclusion_tag('mineral/display_alphabets.html')
def filter_alphabet(bold_alphabet):
    groups = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabets = []
    for alphabet in groups:
        alphabets += alphabet
    return {'alphabets' : alphabets, 'bold_alphabet' : bold_alphabet}
