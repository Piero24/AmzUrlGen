
def link_choise(final_link, stat_var, list_link):

    if stat_var in ['1']:

        final_link += f"{list_link[1].replace(' ', '+')}/s?k={list_link[1].replace(' ', '+')}&" \
                      f"rh=p_78%3{list_link[0].replace(' ', '')}&" \
                      f"maas=maas_adg_1&ref=aa_maask%3D{list_link[1].replace(' ', '+')}"

    elif stat_var in ['2']:

        final_link += f"s?k={list_link[1].replace(' ', '+')}&dc&hidden-keywords={list_link[0].replace(' ', '')}"

    elif stat_var in ['3']:

        final_link += f"fdp/{list_link[0].replace(' ', '')}/ref=sr_1_2?ie=UTF8&" \
                      f"keywords={list_link[1].replace(' ', '+')}&qid=1637195997&s=gateway&sr=8-2"

    elif stat_var in ['4']:

        final_link += f"s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords={list_link[0].replace(' ', '+')}"

    elif stat_var in ['5']:

        final_link += f"s?k={list_link[1].replace(' ', '+')}&" \
                      f"rh=p_4%3A{list_link[2].replace(' ', '%20')}%2Cp_78" \
                      f"%3A{list_link[0].replace(' ', '')}%2Cp_36%3A1500-2500%2Cssx%3Arelevance&ref=nb_sb_noss_2"

    elif stat_var in ['6']:

        final_link += "gp/aws/cart/add.html?"

        for i in range(1, int(len(list_link) / 2)):
            final_link += f"ASIN.{i}=" + list_link[2 * i].replace(' ', '') + \
                          f"&Quantity.{i}=" + list_link[2 * i + 1].replace(' ', '') + "&"

        final_link = final_link[:-1]

    elif stat_var in ['7']:

        final_link += f"gp/aws/cart/add.html?ASIN.1={list_link[0].replace(' ', '')}&" \
                      f"Quantity.1={list_link[1].replace(' ', '')}"

    elif stat_var in ['8']:

        for i in range(1, len(list_link)):
            final_link += f"{list_link[i].replace(' ', '+')}-"

        final_link = final_link[:-1]
        final_link += f"/dp/{list_link[0].replace(' ', '')}/?maas=ampattrib"

    elif stat_var in ['9']:

        final_link += f"dp/*ASIN{list_link[0].replace(' ', '')}*?"

    elif stat_var in ['10']:

        final_link += f"review/create-review?&asin={list_link[0].replace(' ', '')}:5"

    elif stat_var in ['11']:

        final_link += f"gp/aws/cart/add.html?ASIN.1={list_link[0].replace(' ', '')}&" \
                      f"Quantity.1={list_link[1].replace(' ', '')}"

    elif stat_var in ['12']:

        final_link += f"search?ref=msv_sr&keyword={list_link[1].replace(' ', '+')}&" \
                      f"asins={list_link[0].replace(' ', '')}-C"

    elif stat_var in ['13']:

        final_link += f"search?ref=msv_sr&keyword={list_link[1].replace(' ', '+')}&" \
                      f"asins={list_link[0].replace(' ', '')}-B"

    elif stat_var in ['14']:

        final_link += f"gp/aws/cart/add.html?&ASIN.1={list_link[0].replace(' ', '')}&" \
                      f"Quantity.1={list_link[2].replace(' ', '')}&keywords={list_link[1].replace(' ', '+')}"

    elif stat_var in ['15']:

        pass

    return final_link