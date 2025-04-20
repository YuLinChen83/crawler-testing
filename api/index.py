from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/")
def get_kobo_99_book():
    url = "https://www.kobo.com/tw/zh"
    headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "cookie": "slot=61f5a8cb374264e3e2997180c38fa54a; session=ipCountry=TW&ip=118.160.51.87&affiliateid=514c8b9a-1fd8-4e35-9ffb-907fef14eee2&partnerid=00000000-0000-0000-0000-000000000001&platformid=00000000-0000-0000-0000-ffffffff0000&currency=TWD&merchcountry=TW&ult=&uid=cC00ppxFsPRpF7DxNSjqB6Tb5EQ=; sin=isnew=True; persistent-httponly=originsessionid=77f0ddac-c576-41aa-afe1-16eba76bbc9b&utm_source=&utm_campaign=&utm_medium=; persistent=language_locale=zh-TW; PrivacyPermissions=permissions=feature.recommendation|analytics.user|analytics.platform.features|analytics.catalog|analytics.platform.crashreporting|analytics.platform.AB|readingstats.social|analytics.tracking.campaigns|analytics.tracking|analytics.tracking.googleAnalytics|analytics.tracking.googleTagManager|analytics.tracking.maxymiser|analytics.tracking.crashlytics|analytics.tracking.hotjar|analytics.tracking.firebase|analytics.tracking.googleadwords|analytics.tracking.facebookConnect|analytics.tracking.googlePlusPlatform|analytics.tracking.twitterButton|analytics.tracking.adjust|analytics.tracking.facebook|analytics.tracking.criteo|analytics.tracking.bing|analytics.tracking.talkable|analytics.tracking.pinterest|analytics.tracking.rakutenLinkshare|analytics.tracking.branch|analytics.tracking.button|analytics.tracking.rakutenAdvertising|analytics.tracking.linkedIn|analytics.tracking.drop|analytics.tracking.iChannel|analytics.tracking.responsys|analytics.tracking.eBay|analytics.tracking.teads|analytics.tracking.onetag|analytics.tracking.rtbHouse|analytics.tracking.cision|analytics.tracking.xandr|analytics.tracking.adform|analytics.tracking.quantcast|analytics.tracking.builderio|analytics.tracking.tikTok|analytics.tracking.alkemy|analytics.tracking.VWO|analytics.tracking.datadog&is_defined=False&scope=Session&question_keys=CCPA-ClassA|CCPA-ClassB|CCPA-ClassC|CCPA-ClassD|GoogleAnalytics|GoogleTagManager|Maxymiser|Crashlytics|Hotjar|Firebase|Builderio|VWO|DataDog|GoogleAdwords|FacebookConnect|GooglePlusPlatform|TwitterButton|Adjust|Facebook|Criteo|Bing|Talkable|Pinterest|RakutenLinkshare|Branch|Button|RakutenAdvertising|LinkedIn|Drop|iChannel|Responsys|eBay|Teads|OneTag|RtbHouse|Cision|Xandr|Adform|Quantcast|TikTok|Alkemy&consented=&geo=tw; __RequestVerificationToken=iVt6V9rBdLfB6YdpcSZnV8sVlHTXWsotCBE9TRJLtNcm959Jzoy8HcMhcSy9m4q3FumR_UIC5nn7Tvgr_nuasjAwMpA1; isZarazLoaded=False; _vwo_uuid=DE8A2FC6869A090EE5CF33E1A29CBDA43; _mall_uuid=t7uizq2crx-9yzi69jsche-hpxrvvkkcr; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid_v2=DE8A2FC6869A090EE5CF33E1A29CBDA43|2f3086b4da833323b26962b3652e7e51; _gcl_gs=2.1.k1$i1745150108$u208361608; _gcl_au=1.1.1916590994.1745150114; _ga=GA1.1.1325861400.1745150114; _vwo_ds=3%3At_0%2Ca_0%3A0%241745150114%3A0.86028043%3A%3A%3A%3A2; _tt_enable_cookie=1; _ttp=01JS9GTZ60B6SNRQHT5JB32ED9_.tt.1; _ra=1745150115179|7d8d5e26-21d6-4c9d-b438-097ade845adc; FPGCLAW=2.1.kCj0KCQjwtpLABhC7ARIsALBOCVqVU9ERC5eQjfAGtgrRA3uGiEw_blEEsoXpqvJ-pLr-GtKCYMT7GRkaAm4NEALw_wcB$i1745150118; FPGCLGS=2.1.k1$i1745150111$u208361608; FPAU=1.1.1916590994.1745150114; _fbp=fb.1.1745150117560.1713113555; _gtmeec=eyJjdCI6Ijk1M2Q3YWZkMTQ0MmZjYWViN2I4MTMwNjM2ZThjMWJiNjBjNGM5YWM0MmJiNGM4N2IwMzc3MjlhOTYzZDJkYWMiLCJjb3VudHJ5IjoiYjYzOTljYzI2ZjRkNzZiYWFjZjkzODMwMjQwYWUxYThiMGI1NDA2MGVkYTFlNzYwZDllM2E4NmQ0ZDNjYjYxOCJ9; _pin_unauth=dWlkPU5UYzFaR1k0WVRFdE9UQXhNaTAwTkRNd0xUbGxPV1F0T1Rka1lUWmlNbVEwTVRobA; sessionId=sessionid=a2947016-b4d4-430f-9f87-608feafaca89; session-httponly=appversion=1.0.0.0&deviceid=&searchdiscriminator=0&lt=&carrierName=; _gcl_aw=GCL.1745154505.Cj0KCQjwtpLABhC7ARIsALBOCVqVU9ERC5eQjfAGtgrRA3uGiEw_blEEsoXpqvJ-pLr-GtKCYMT7GRkaAm4NEALw_wcB; _hjSessionUser_343404=eyJpZCI6Ijk1MjVhNTEwLTQ4NTctNWE1Mi1iMzUwLTAzYTkwNmI1N2NhZiIsImNyZWF0ZWQiOjE3NDUxNTAxMTU3MzEsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_343404=eyJpZCI6IjVlNzkyYTdkLWJjZmMtNDEzNy05ODljLTJmMzE0MmU1NzYzMiIsImMiOjE3NDUxNTQ1MDUxNTUsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _schk=a2947016-b4d4-430f-9f87-608feafaca89; _uetsid=541461901dde11f080d8eff294116ce9; _uetvid=541490e01dde11f0a4ecdd5f6d108366; __cf_bm=S.3MvzgyBcmzZKpwBCD1qX.bvGcj2VkI3VgojQqBrQk-1745155993-1.0.1.1-3zqoP7gfhqd6_R5j0.3WXCfFlEg4PsQzkvJuE.hs3r6aanhhUuS5yvRP10HOCtJ1oG1nudfSXM411XmV9fDO2BYMIS8b0C.Zvs.0IZnNeP8; _vwo_sn=4386%3A2; _derived_epik=dj0yJnU9SGJyekx1ZmpOTFJGZS10NFU0T0R6bXMzVjF4bTAySVcmbj1ieHFYeVYxbmp3R2VtNlZ4SlZqX29RJm09MSZ0PUFBQUFBR2dFLUFNJnJtPTEmcnQ9QUFBQUFHZ0UtQU0mc3A9Mg; ttcsid=1745154505307.2.1745156099556; ttcsid_COC4UMBC77U70QG2VJ1G=1745154502628.2.1745156099761; cto_bundle=SSIB019xT0J0TjBvSFY5RlNYRWVDNHYwUm9VN0N0SzNTZ25KeEZUOXBJbUtaZCUyRlh4b05qUmRIVkwlMkJpcWdqZ2xMUWxnalg4cjY4dWJXJTJGVyUyQkhyJTJGTDVHWjUxeUgyWCUyQkp6R3o1ZmxMUzhTSlJxWDZ0MTd2WGlzWXlJbzdPVSUyQjd2dmhEWjVKYUljNHFYMXk2YlhqZVBzbmNCa1pQWXZQM3I1S0hDaVA4cTcwOFBXZ2NmeUplN3o4Umc0JTJCRjhrTkthSU5WOGdxVUJ0UEJVbHR6S1lVSkhIZlhOJTJCeSUyRkElM0QlM0Q; _ga_TSZTR6GCCP=GS1.1.1745154498.2.1.1745156105.0.0.2031516856",
    "Referer": "https://www.kobo.com/tw/zh?utm_content=GSMSC&gad_source=1&gclid=Cj0KCQjwtpLABhC7ARIsALBOCVqVU9ERC5eQjfAGtgrRA3uGiEw_blEEsoXpqvJ-pLr-GtKCYMT7GRkaAm4NEALw_wcB",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  }

    res = requests.get("https://www.kobo.com/tw/zh", headers=headers)
    print(res.status_code)
    print(res.text)  # 印前面一段 HTML 看有沒有抓到

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # 找到第一個 .spotlight-content 區塊
        spotlight = soup.select_one(".spotlight-content")

        # 抓第一個 a tag
        a_tag = spotlight.find("a")
        link = a_tag["href"]
        if not link.startswith("http"):
            link = "https://www.kobo.com" + link

        # 抓圖片
        img_tag = a_tag.find("img")
        cover = img_tag["src"]

        # 抓標題
        h3_tag = a_tag.find("h3")
        title = h3_tag.get_text(strip=True)

        return JSONResponse(content={
            "title": title,
            "cover": cover,
            "link": link
        })

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
