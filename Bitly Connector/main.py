import requests

class bitly:
    def __init__(self):
        self.access_token = 'bb31e6a992ab258682a80176c007f3a1ccc6d7ad'
        self.header = {
            "Authorization": "{}".format(self.access_token),
            "Content-Type": "application/json"
        }
        self.path = "https://api-ssl.bitly.com/v4"
        self.query = None
        self.params = None

    def get_groups(self):
        self.params = None
        self.query = self.path+"/groups"
        result = self._run_query()
        return result

    def get_campaings_in_group(self, group_id):
        self.params={"group_guid": group_id}
        self.query = self.path+"/campaigns"
        result = self._run_query()
        return result

    def get_channels_in_group(self, group_id):
        self.params={"group_guid": group_id}
        self.query = self.path+"/channels"
        result = self._run_query()
        return result

    def get_links_in_group(self, group_id, size=100, page=1, created_before=None,created_after=None):
        links=[]
        self.params = {"size": size,
                       "page": page}
        if created_before is not None:
            self.params["created_before"] = created_before
        if created_after is not None:
            self.params["created_after"] = created_after
        self.query = self.path+"/groups/{}/bitlinks".format(group_id)
        result = self._run_query()
        links += result["links"]
        while len(result["links"]) != 0:
            self.params["page"] += 1
            result = self._run_query()
            links += result["links"]
        return links

    def get_links_in_campaign(self, group_id, campaing_id, size=100, page=1, created_before=None,created_after=None):
        links=[]
        self.params = {"size": size,
                       "page": page,
                       "campaign_guid": campaing_id}
        if created_before is not None:
            self.params["created_before"] = created_before
        if created_after is not None:
            self.params["created_after"] = created_after
        self.query = self.path+"/groups/{}/bitlinks".format(group_id)
        result = self._run_query()
        links += result["links"]
        while len(result["links"]) != 0:
            self.params["page"] += 1
            result = self._run_query()
            links += result["links"]
        return links

    def get_links_in_channel(self, group_id, channel_id, size=100, page=1, created_before=None,created_after=None):
        links=[]
        self.params = {"size": size,
                       "page": page,
                       "channel_guid": channel_id}
        if created_before is not None:
            self.params["created_before"] = created_before
        if created_after is not None:
            self.params["created_after"] = created_after
        self.query = self.path+"/groups/{}/bitlinks".format(group_id)
        result = self._run_query()
        links += result["links"]
        while len(result["links"]) != 0:
            self.params["page"] += 1
            result = self._run_query()
            links += result["links"]
        return links

    def get_link_clicks(self, bitlink, unit = None, units = None, size = None, unit_reference = None):
        self.params = {}
        if unit is not None:
            self.params["unit"] = unit
        if units is not None:
            self.params["units"] = units
        if size is not None:
            self.params["size"] = size
        if unit_reference is not None:
            self.params["unit_reference"] = unit_reference
        if len(self.params) == 0:
            self.params = None
        self.query = self.path + "/bitlinks/{bitlink}/clicks".format(bitlink=bitlink)
        result = self._run_query()
        return result

    def get_link_clicks_countries(self, bitlink, unit = None, units = None, size = None, unit_reference = None):
        self.params = {}
        if unit is not None:
            self.params["unit"] = unit
        if units is not None:
            self.params["units"] = units
        if size is not None:
            self.params["size"] = size
        if unit_reference is not None:
            self.params["unit_reference"] = unit_reference
        if len(self.params) == 0:
            self.params = None
        self.query = self.path + "/bitlinks/{bitlink}/countries".format(bitlink=bitlink)
        result = self._run_query()
        return result

    def get_link_clicks_referring_domains(self, bitlink, unit = None, units = None, size = None, unit_reference = None):
        self.params = {}
        if unit is not None:
            self.params["unit"] = unit
        if units is not None:
            self.params["units"] = units
        if size is not None:
            self.params["size"] = size
        if unit_reference is not None:
            self.params["unit_reference"] = unit_reference
        if len(self.params) == 0:
            self.params = None
        self.query = self.path + "/bitlinks/{bitlink}/referring_domains".format(bitlink=bitlink)
        result = self._run_query()
        return result

    def get_link_clicks_referrers(self, bitlink, unit = None, units = None, size = None, unit_reference = None):
        self.params = {}
        if unit is not None:
            self.params["unit"] = unit
        if units is not None:
            self.params["units"] = units
        if size is not None:
            self.params["size"] = size
        if unit_reference is not None:
            self.params["unit_reference"] = unit_reference
        if len(self.params) == 0:
            self.params = None
        self.query = self.path + "/bitlinks/{bitlink}/referrers_by_domains".format(bitlink=bitlink)
        result = self._run_query()
        return result

    def _run_query(self):
        try:
            if self.params is None:
                result = requests.get(self.query, headers=self.header).json()
            else:
                result = requests.get(self.query, headers=self.header, params=self.params).json()
            return result
        except Exception as e:
            print(e)
