# -*- coding: utf-8 -*-
import scrapy
import json
class NbaspiderSpider(scrapy.Spider):
    name = 'nbaspider'
    start_urls = ['http://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode\
    =PerGame&Scope=S&Season=2016-17&SeasonType=Playoffs&StatCategory=PTS']
    headers = 'Mozilla/5.0'
    def parse(self, response):
        js = json.loads(response.body)
        for i in js["resultSet"]["rowSet"]:
            yield {
                "PLAYER_ID":i[0],
                "RANK":i[1],
                "PLAYER":i[2],
                "TEAM":i[3],
                "GP":i[4],
                "MIN":i[5],
                "FGM":i[6],
                "FGA":i[7],
                "FG_PCT":i[8],
                "FG3M":i[9],
                "FG3A":i[10],
                "FG3_PCT":i[11],
                "FTM":i[12],
                "FTA":i[13],
                "FT_PCT":i[14],
                "OREB":i[15],
                "DREB":i[16],
                "REB":i[17],
                "AST":i[18],
                "STL":i[19],
                "BLK":i[20],
                "TOV":i[21],
                "PTS":i[22],
                "EFF":i[23],
            }

