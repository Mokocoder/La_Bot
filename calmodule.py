import json
import discord

def embedresult(response:json):
    rkrdlsfinal = ""

    for eng in response["Basic"]["Engrave"]:
        if eng == "각인 없음":
            break
        else:
            num = str(eng).find(" Lv.")
            lvl = str(eng)[num+5:]
            eng = str(eng)[:num]
            rkrdlsfinal = rkrdlsfinal+"` "+lvl+" ` : "+eng+"\n"

    if rkrdlsfinal == "":
        rkrdlsfinal = "`각인 없음`\n"
    
    embedresult = discord.Embed(color=discord.Color.from_rgb(255,255,255))
    embedresult.set_author(name=response["Basic"]["Name"],icon_url=response["Basic"]["Class"]["Icon"])
    embedresult.add_field(
        name="**▫️ 기본 정보**",
        value=("`서ㅤ버` : "+response["Basic"]["Server"]+"\n"+
        "`클래스` : "+response["Basic"]["Class"]["Name"]+"\n"+
        "`길ㅤ드` : "+response["Basic"]["Guild"]+"\n"+
        "`칭ㅤ호` : "+response["Basic"]["Title"]+"\n\n"+
        "**▫️ 특성 정보**\n"+
        "`공격력` : "+response["Basic"]["Stat"]["Attack"]+"\n"+
        "`생명력` : "+response["Basic"]["Stat"]["Health"]+"\n\n"+
        "`치ㅤ명` : "+response["Basic"]["Stat"]["Critical"]+"\n"+
        "`특ㅤ화` : "+response["Basic"]["Stat"]["Specialty"]+"\n"+
        "`제ㅤ압` : "+response["Basic"]["Stat"]["Subdue"]+"\n"+
        "`신ㅤ속` : "+response["Basic"]["Stat"]["Agility"]+"\n"+
        "`인ㅤ내` : "+response["Basic"]["Stat"]["Endurance"]+"\n"+
        "`숙ㅤ련` : "+response["Basic"]["Stat"]["Proficiency"]),
        inline=True
    )

    embedresult.add_field(name = chr(173), value = chr(173))

    embedresult.add_field(
        name="**▫️ 레벨 정보**",
        value=("`전ㅤ투` : "+response["Basic"]["Level"]["Battle"]+"\n"+
        "`원정대` : "+response["Basic"]["Level"]["Expedition"]+"\n"+
        "`아이템` : "+response["Basic"]["Level"]["Item"]+"\n"+
        "`영ㅤ지` : "+response["Basic"]["Wisdom"]["Level"]+" "+response["Basic"]["Wisdom"]["Name"]+"\n\n"+
        "**▫️ 각인 효과**\n"+
        rkrdlsfinal+"\n"+
        "**▫️ 성향 정보**\n"+
        "`지ㅤ성` : "+response["Basic"]["Tendency"]["Intellect"]+"\n"+
        "`담ㅤ력` : "+response["Basic"]["Tendency"]["Bravery"]+"\n"+
        "`매ㅤ력` : "+response["Basic"]["Tendency"]["Charm"]+"\n"+
        "`친ㅤ절` : "+response["Basic"]["Tendency"]["Kindness"]),
        inline=True
    )

    embedresult.set_footer(text="Made By 모코코더#3931", icon_url="https://cdn.discordapp.com/avatars/693421981705568346/f7cf118ca37e88b490ad1ac1489416ea.webp")

    return embedresult

def embedresult_lister(response:json):
    lisrrr = ""

    for listers in response["CharacterList"]:
        if int(listers["Level"][listers["Level"].find('Lv.')+3:listers["Level"].rfind('.')].replace(',','')) >= 1000:
            lisrrr = lisrrr + "[`" + listers["Server"] + "`] [`" + listers["Level"] + "`] [`" + listers["Class"] + "`] [`" + listers["Name"] + "`]\n"

    if lisrrr == "":
        lisrrr = "1,000레벨 이상 캐릭터 없음"

    embedresult_lister = discord.Embed(title="캐릭터 목록", color=discord.Color.green())

    embedresult_lister.add_field(
        name="▫️ 1,000레벨 이상 캐릭터만 표기됩니다.",
        value=(lisrrr)
    )

    embedresult_lister.set_footer(text="Made By 모코코더#3931", icon_url="https://cdn.discordapp.com/avatars/693421981705568346/f7cf118ca37e88b490ad1ac1489416ea.webp")

    return embedresult_lister

def embedskill(response:json):
    skilllen = 0
    skillspace = 0
    skillfinal = ""

    if response["Skill"]["Skill"][0]["Name"] == "스킬 없음":
        skillfinal = "`스킬 없음`"
    else:
        for skill in response["Skill"]["Skill"]:
            if skilllen < len(skill["Name"]):
                skilllen = len(skill["Name"])
            if skillspace < skill["Name"].count(" "):
                skillspace = skill["Name"].count(" ")

        skilllen = skilllen + 1
        
        for skill in response["Skill"]["Skill"]:
            skfnname = skill["Name"]
            if skillspace > 0:
                while skillspace-skfnname.count(" ") > 0:
                    skfnname = skfnname + "\u0020"
            while len(skfnname) < skilllen:
                skfnname = skfnname + "ㅤ"
            skillfinal = skillfinal+"`"+(skfnname+"` Lv."+skill["Level"]+" `"+skill["Tri"])+"`\n"

        if skillfinal == "":
            skillfinal = "`스킬 없음`"

    embedskill = discord.Embed(title="스킬", color=discord.Color.purple())

    embedskill.add_field(
        name="**▫️ "+"사용 스킬 포인트 "+response["Skill"]["SkillPoint"]["Used"]+" / 보유 스킬 포인트 "+response["Skill"]["SkillPoint"]["Total"]+"**",
        value=(skillfinal)
    )

    embedskill.set_footer(text="Made By 모코코더#3931", icon_url="https://cdn.discordapp.com/avatars/693421981705568346/f7cf118ca37e88b490ad1ac1489416ea.webp")

    return embedskill

def embedresult_jewlist(response:json):
    jewlist = ""

    for jewl in response["Jewl"]:
        if jewl["JewlName"] == "보석 없음":
            break
        else:
            if not jewl["JewlName"].find('멸화') == -1:
                jewl["JewlName"] = "<:aufghk:935346521312997477> `" + jewl["JewlName"] + "`"
            else:
                if not jewl["JewlName"].find('홍염') == -1:
                    jewl["JewlName"] = "<:ghddua:935346521912782878> `" + jewl["JewlName"] + "`"
                else:
                    jewl["JewlName"] = "`" + jewl["JewlName"] + "`"       
                    
            jewlist = jewlist + (jewl["JewlName"] + " : " + jewl["SkillName"] + " > " + jewl["Effect"]) + "\n"

    if jewlist == "":
        jewlist = ("`장착된 보석이 없습니다./보석 데이터를 불러오지 못 했습니다`")

    cardlist = ""

    if response["Card"][0]["Name"] == "카드 없음":
        cardlist = "`카드 없음`"
    else:
        for cards in response["Card"]:
            cardlist = cardlist + ("`" + cards["Name"] + "` : " + cards["Effect"]) + "\n"

    embedresult_jewlist = discord.Embed(title="보석&카드", color=discord.Color.dark_blue())

    embedresult_jewlist.add_field(
        name="▫️ 보석 목록",
        value=(jewlist),
        inline=False
    )

    embedresult_jewlist.add_field(
        name="▫️ 카드 목록",
        value=(cardlist),
        inline=False
    )

    embedresult_jewlist.set_footer(text="Made By 모코코더#3931", icon_url="https://cdn.discordapp.com/avatars/693421981705568346/f7cf118ca37e88b490ad1ac1489416ea.webp")

    return embedresult_jewlist

def embedresult_goldget(response:json):
    goldinterval = 0

    for intv in response["Gold"]["GoldList"]:
        if len("[`"+intv["Level"]+"`] [`"+intv["Class"]+"`] ") > goldinterval:
            goldinterval = len("[`"+intv["Level"]+"`] [`"+intv["Class"]+"`] ")

    goldchn = 6

    goldn = ""
    onlygd = ""

    if len(response["Gold"]["GoldList"]) < goldchn:
        goldchn = len(response["Gold"]["GoldList"])

    goldinterval = goldinterval + 4

    for goldlist in response["Gold"]["GoldList"]:
        gold = goldlist["Gold"]
        fnlr = "[`"+goldlist["Level"]+"`] [`"+goldlist["Class"]+"`] "
        fnlr2 = "[`"+goldlist["Name"]+"`]"
        fnlr = fnlr + "`"
        while len(fnlr) < goldinterval:
            fnlr = fnlr + "ㅤ"
        goldn = goldn + (fnlr+"`"+ fnlr2 +"\n")
        onlygd = onlygd + "[🪙`"+ gold +"`]\n"

    embedresult_goldget = discord.Embed(title="주급", color=discord.Color.gold(), description="**총 [💰`"+ str(response["Gold"]["TotalGold"]) +"`💰]**")

    embedresult_goldget.add_field(
        name="▫️ 주간 골드 획득 캐릭터",
        value=(goldn)+"\n\n▫️ 주간 컨텐츠 최저 레벨을 기준으로 계산했습니다.\n▫️ 클리어 골드 이외의 요소는 고려하지 않았습니다.\n▫️ 아브는 4관 까지만 계산했습니다.\n▫️ 도전 가능한 최상위 컨텐츠 기준으로 계산했습니다.",
        inline=True
    )

    embedresult_goldget.add_field(
        name="획득 골드",
        value=(onlygd),
        inline=True
    )

    embedresult_goldget.set_footer(text="Made By 모코코더#3931", icon_url="https://cdn.discordapp.com/avatars/693421981705568346/f7cf118ca37e88b490ad1ac1489416ea.webp")

    return embedresult_goldget

def embedresult_sasalist(response:json, 닉네임:str):
    sasalist = ""

    i=0
    for sasacontext in response["SasaList"]:
        sasalist = sasalist + "▫️ " + sasacontext + "\n"
        i = i+1

    if i == 5:
        sasalist = sasalist + "\n(게시물이 개수가 5개 이상입니다. 5개 까지만 표시)" 

    embedresult_sasalist = discord.Embed(title="사사게 (" + 닉네임 + ")", color=discord.Color.blurple(), description="상단 파란색 사사게 클릭시 이동", url=response["SasaUrl"])

    embedresult_sasalist.add_field(
        name="▫️ 사사게 검색 정보(최근 1만 게시글)",
        value=(sasalist)
    )

    embedresult_sasalist.set_footer(text="Made By 모코코더#3931", icon_url="https://cdn.discordapp.com/avatars/693421981705568346/f7cf118ca37e88b490ad1ac1489416ea.webp")

    return embedresult_sasalist

def embedresult_auction(가격:int):
    embedresult_auction = discord.Embed(title="💰 경매 입찰 최적가(판매시)", color=discord.Color.gold(), description="[🪙`"+str(가격)+"`]")

    embedresult_auction.add_field(
        name="▫️ 손익분기점",
        value=("4인 : [🪙`"+str(int(가격*0.95*3/4))+"`]\n"+
        "8인 : [🪙`"+str(int(가격*0.95*7/8))+"`]"),
        inline=False
    )
    embedresult_auction.add_field(
        name="▫️ 입찰적정가",
        value=("4인 : [🪙`"+str(int(가격*0.95*3/4*100/110))+"`] 🔻\n"+
        "8인 : [🪙`"+str(int(가격*0.95*7/8*100/110))+"`] 🔻"),
        inline=False
    )

    embedresult_auction.set_footer(text="Made By 모코코더#3931", icon_url="https://cdn.discordapp.com/avatars/693421981705568346/f7cf118ca37e88b490ad1ac1489416ea.webp")

    return embedresult_auction

def embedresult_crystal(response:json):
    embedresult_crystal = discord.Embed(title="시세", color=discord.Color.gold())

    embedresult_crystal.add_field(
        name="**▫️ 구매가**",
        value=("[🪙`"+ str(response['Buy']).replace(".0","")+"`]"),
        inline=False
    )
    embedresult_crystal.add_field(
        name="**▫️ 판매가**",
        value=("[🪙`"+ str(response['Sell']).replace(".0","")+"`]"),
        inline=False
    )

    embedresult_crystal.set_footer(text="Made By 모코코더#3931", icon_url="https://cdn.discordapp.com/avatars/693421981705568346/f7cf118ca37e88b490ad1ac1489416ea.webp")

    return embedresult_crystal

def embedresult_island(response:json):
    advenisland = ""

    for island in response["Island"]:
        advenisland = advenisland + island["Name"] + " [" + island["Reward"] + "]\n"

    embedresult_island = discord.Embed(title="오늘의 모험섬", color=discord.Color.gold())

    embedresult_island.add_field(
        name="▫️ "+response["IslandDate"],
        value=(advenisland),
        inline=False
    )

    embedresult_island.set_footer(text="Made By 모코코더#3931", icon_url="https://cdn.discordapp.com/avatars/693421981705568346/f7cf118ca37e88b490ad1ac1489416ea.webp")

    return embedresult_island

def embedresult_gearlist(response:json):
    ItemList = ["무기","머리 방어구","상의"]
    ItemList2 = ["하의","장갑","어깨 방어구"]
    
    gearlist = ""
    gearlist2 = ""

    embedresult_gearlist = discord.Embed(title="장비", color=discord.Color.brand_red())

    for items in ItemList:
        try:
            eqname = response["Items"][items]["Name"]
            tri = ""
            if not response["Items"][items]["Tri"] == "트라이포드 효과 적용 불가":
                for t in response["Items"][items]["Tri"]:
                    tri = tri + "[`"+t["SkillName"] +"`] " + t["Effect"] + "\n"
            gearlist = gearlist + ("**◻"+eqname + " | `품질` : " + response["Items"][items]["Quality"] + "**\n" + tri) + "\n"
        except Exception:
            pass

    for items in ItemList2:
        try:
            eqname = response["Items"][items]["Name"]
            tri = ""
            if not response["Items"][items]["Tri"] == "트라이포드 효과 적용 불가":
                for t in response["Items"][items]["Tri"]:
                    tri = tri + "[`"+t["SkillName"] +"`] " + t["Effect"] + "\n"
            gearlist2 = gearlist2 + ("**◻"+eqname + " | `품질` : " + response["Items"][items]["Quality"] + "**\n" + tri) + "\n"
        except Exception:
            pass

    if gearlist+gearlist2 == "":
        gearlist = ("`장착된 장비가 없습니다./장비 데이터를 불러오지 못 했습니다`")

    if gearlist == "`장착된 장비가 없습니다./장비 데이터를 불러오지 못 했습니다`":   
        if gearlist2 == "":
            embedresult_gearlist.add_field(
                name="▫️ 현재 장착중인 장비 목록",
                value=(gearlist),
                inline=True
            )
        else:
            embedresult_gearlist.add_field(
                name="▫️ 현재 장착중인 장비 목록",
                value=(gearlist2),
                inline=True
            )
    else:
        if gearlist2 == "":
            embedresult_gearlist.add_field(
                name="▫️ 현재 장착중인 장비 목록",
                value=(gearlist),
                inline=True
            )
        else:                        
            embedresult_gearlist.add_field(
                name="▫️ 현재 장착중인 장비 목록",
                value=(gearlist),
                inline=True
            )
            embedresult_gearlist.add_field(
                name=chr(173),
                value=(gearlist2),
                inline=True
            )

    embedresult_gearlist.set_footer(text="Made By 모코코더#3931", icon_url="https://cdn.discordapp.com/avatars/693421981705568346/f7cf118ca37e88b490ad1ac1489416ea.webp")

    return embedresult_gearlist

def embedresult_gear2list(response:json):
    ItemList = ["목걸이","귀걸이1","귀걸이2"]
    ItemList2 = ["반지1","반지2"]
    
    gearlist = ""
    gearlist2 = ""
    gearlist3 = ""

    embedresult_gear2list = discord.Embed(title="악세서리", color=discord.Color.brand_red())

    for items in ItemList:
        try:
            eqname = response["Items"][items]["Name"]
            plus = ""
            eng = ""
            for p in response["Items"][items]["Plus"]:
                plus = plus + p + "\n"
            for e in response["Items"][items]["Engrave"]:
                if e["EngraveName"] == "각인 효과 없음":
                    pass
                else:
                    eng = eng + "[`" + e["EngraveName"] + "`] " + e["Effect"] + "\n"                 
            gearlist = gearlist + ("**◻"+eqname + " | `품질` : " + response["Items"][items]["Quality"] + "**\n" + plus + eng) + "\n"
        except Exception:
            pass

    for items in ItemList2:
        try:
            eqname = response["Items"][items]["Name"]
            plus = ""
            eng = ""
            for p in response["Items"][items]["Plus"]:
                plus = plus + p + "\n"
            for e in response["Items"][items]["Engrave"]:
                if e["EngraveName"] == "각인 효과 없음":
                    pass
                else:
                    eng = eng + "[`" + e["EngraveName"] + "`] " + e["Effect"] + "\n"                    
            gearlist2 = gearlist2 + ("**◻"+eqname + " | `품질` : " + response["Items"][items]["Quality"] + "**\n" + plus + eng) + "\n"
        except Exception:
            pass

    try:
        eqname = response["Items"]["어빌리티 스톤"]["Name"]
        addHP = "[`기본효과`] " + response["Items"]["어빌리티 스톤"]["Basic"] + "\n"
        if not response["Items"]["어빌리티 스톤"]["Plus"] == "없음":
            addHP = addHP + "[`추과효과`] " + response["Items"]["어빌리티 스톤"]["Plus"] + "\n"
        eng = ""
        for e in response["Items"]["어빌리티 스톤"]["Engrave"]:
            eng = eng + "[`" + e["EngraveName"] + "`] " + e["Effect"] + "\n"
        gearlist2 = gearlist2 + ("**◻"+eqname + "**\n" + addHP + eng) + "\n"
    except Exception:
        pass

    try:
        eqname = response["Items"]["팔찌"]["Name"]
        bracfn = ""
        for s in response["Items"]["팔찌"]["Plus"]:
            if "[잠김]" in s:
                bracfn = bracfn + str(s).replace("[잠김]","<:L:935790216365621308>") +"\n"
            else:
                if "[변경가능]" in s:
                    bracfn = bracfn + str(s).replace("[변경가능]","<:C:935790216218804235>") +"\n"
        gearlist3 = ("**◻"+eqname + "**\n" + bracfn) + "\n"
    except Exception:
        pass

    if gearlist+gearlist2 == "":
        gearlist = ("`장착된 악세서리가 없습니다./악세서리 데이터를 불러오지 못 했습니다`")

    if gearlist == "`장착된 악세서리가 없습니다./악세서리 데이터를 불러오지 못 했습니다`":   
        if gearlist2 == "":
            embedresult_gear2list.add_field(
                name="▫️ 현재 장착중인 악세서리 목록",
                value=(gearlist),
                inline=True
            )
        else:
            embedresult_gear2list.add_field(
                name="▫️ 현재 장착중인 악세서리 목록",
                value=(gearlist2),
                inline=True
            )
    else:
        if gearlist2 == "":
            embedresult_gear2list.add_field(
                name="▫️ 현재 장착중인 악세서리 목록",
                value=(gearlist),
                inline=True
            )
        else:                        
            embedresult_gear2list.add_field(
                name="▫️ 현재 장착중인 악세서리 목록",
                value=(gearlist),
                inline=True
            )
            embedresult_gear2list.add_field(
                name=chr(173),
                value=(gearlist2),
                inline=True
            )

    if not gearlist3 == "":
        embedresult_gear2list.add_field(
            name=chr(173),
            value=(gearlist3),
            inline=False
        )

    embedresult_gear2list.set_footer(text="Made By 모코코더#3931", icon_url="https://cdn.discordapp.com/avatars/693421981705568346/f7cf118ca37e88b490ad1ac1489416ea.webp")

    return embedresult_gear2list
