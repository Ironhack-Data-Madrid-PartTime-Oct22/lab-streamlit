import calendar

dict_month = dict(zip(list(calendar.month_name)[1:], list(range(1,13))))

dict_keys = {
    0: 'C',
    1: 'C♯',
    2: 'D',
    3: 'D♯',
    4: 'E',
    5: 'F',
    6: 'F♯',
    7: 'G',
    8: 'G♯',
    9: 'A',
    10: 'A♯',
    11: 'B'
}

dict_keys_scale = {
    'C Major': "Innocently Happy. Completely pure. Simplicity and naivety. The key of children. Free of burden, full of imagination. Powerful resolve. Earnestness. Can feel religious.",
    'C Minor': "Innocently Sad, Love-Sick. Declarations of love and lamenting lost love or unhappy relationships. It is languishing and full of longing, a soul in search of something different.",
    'C♯ Minor': "Despair, Wailing, Weeping. A passionate expression of sorrow and deep grief. Full of penance and self-punishment. An intimate conversation with God about recognition of wrongdoing and atonement.",
    'C♯ Major': "Grief, Depressive. Rapture in sadness. A grimacing key of choking back tears. It is capable of a laugh or smile to pacify those around, but the truth is in despair. Fullness of tone, sonority, and euphony.",
    'D Major': "Triumphant, Victorious War-Cries. Screaming hallelujah's, rejoicing in conquering obstacles. War marches, holiday songs, invitations to join the winning team.",
    'D Minor': "Serious, Pious, Ruminating. Melancholy, feminine, brooding worries, contemplation of negativity.",
    'D♯ Minor': "Deep Distress, Existential Angst. Dealing with anxiety and existential terror, deep distress, dark depression. The dark night of the soul. Fear, hesitation, shuddering, goose bumps. The language of ghosts.",
    'D♯ Major': "Cruel, Hard, Yet Full of Devotion. Love, Devotion, Intimacy, Openness, Honest Communion. Conversations with God.",
    'E Major':"Quarrelsome, Boisterous, Incomplete Pleasure. Shouts of Joy, Complete Delight, yet Bickering, Short-fused, Ready to Fight.",
    'E Minor': "Effeminate, Amorous, Restless. This key can carry grief, mournfulness, restlessness. Like a princess locked in a tower longing for her rescuer and future lover.",
    'F Major': "Furious, Quick-Tempered, Passing Regret. Complaisance, Controlled calmness over the readiness to explode. Deeply angry but composed and sociable still. Religious sentiment.",
    'F Minor': "Obscure, Plaintive, Funereal. Deepest depression, lament over death and loss, groans of misery, ready to expire. Harrowing. Melancholic.",
    'F♯ Major': "Conquering Difficulties, Sighs of Relief. Triumph over evil, obstacles, hurdles. Surmounting foes and finally finding rest in victory. Brilliant clarity of thought and feeling.",
    'F♯ Minor': "Gloomy, Passionate Resentment. Tearing at your hair and shirt, discontentment, long periods of lamentation and crying. Still capable of fighting this feeling.",
    'G Major': "Serious, Magnificent, Fantasy. Rustic, Idyllic, Poetic, Lyrical. Calm and satisfied. Tenderness and Gratitude. Friendship and Faith. It is a gentle key full of peace.",
    'G Minor': "Discontent, Uneasiness. Worry of the future, of a failed plan, gnashing of teeth. Concern over a failed plan. Struggling with dislike and malcontent.",
    'G♯ Major': "Death, Eternity, Judgement. Putrefaction, Expansive viewpoints of a dark cosmos and existence. Ghosts, Ghouls, Goblins, Graveyards. Haunting and Lingering.",
    'G♯ Minor': "Grumbling, Moaning, Wailing. Suffocation of the Heart, Lamentations, Life-Long Struggles. A negative look at the experiences of life, competition, growth.",
    'A Major': "Joyful, Pastoral, Declaration of Love. Innocent Love, Satisfaction with the current state of affairs. Optimistic. Belief in Heaven and reuniting with lost loved ones. Youthful and cheerful. Trusting in the spirit of the divine.",
    'A Minor': "Tender, Plaintive, Pious. Womanly, Graceful in character. Capable of soothing.",
    'A♯ Major': "Joyful, Quaint, Cheerful. Love, Clear Conscience, Hopeful Aspirations for the future and a better world. Optimistic and able to take control in order to ensure peace.",
    'A♯ Minor': "Terrible, the Night, Mocking. The Garment of Night, Surly, Blasphemous, Turning away the world and the divine. Preparations for the end. Pessimism and giving up. Belief in darkness.",
    'B Major': "Harsh, Strong, Wild, Rage. Uncontrolled passions. Angry, Jealous, Fury, Despair, Burdened with negative energy. Prepared to fight.",
    'B Minor': "Solitary, Melancholic, Patience. The key of patience, calmly waiting for fate, destiny, and the submission to providence and karma."
}

dict_scale = {
    1: 'Major',
    0: 'Minor',
}

dict_gender = {
    'male': [' his '],
    #'group': ['duo', 'septet', 'trio', 'collective', 'quintet', 'quartet', 'septet', 'its', ' group ', ' band ', '-group', ' members ', ' brothers ', ' duo ', ' trio ', ' collective ', ' group,', ' quartet ', ' superduo ', ' band,', ' quintet '],
    'female': [' she ', ' her ', 'actress', ' she is '],
    'male': [' him ', ' he ', ' his '],
    'group': ['duo', 'septet', 'trio', 'collective', 'quintet', 'quartet', 'septet', 'its', ' group ', ' band ', '-group', ' members ', ' brothers ', ' duo ', ' trio ', ' collective ', ' group,', ' quartet ', ' superduo ', ' band,', ' quintet '],
    'non-binary': [' they ', ' them ', ' their '],
}