from typing import Dict, Text, Any, List, Union

from rasa_sdk import Tracker, Action
from rasa_sdk.events import UserUtteranceReverted, Restarted, SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from utils.utils import time_finder
import re
from actions.TripApis import get_trip_hotel, get_trip_flight


class TripForm(FormAction):
            
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "trip_form"
    
    def type_db(self) -> List[Text]:
        """Database of supported trip type"""

        return [
            "短期出差",
            "长期出差",
            "研发项目",
            "系统内培训",
            "系统外培训",
            "系统内会议",
            "系统外会议",
        ]
        
    def baoxiaodiqu_db(self) -> List[Text]:
        """Database of supported baoxiaodiqu"""

        return [
            "福州",
            "上海",
            "北京",
            "成都",
            "武汉",
            "深圳",
            "厦门",
            "广州",
            "西安",
            "沈阳",
        ]
        
    def tiaoxian_db(self) -> List[Text]:
        """Database of supported tiaoxian"""

        return [
            "信用卡中心",
            "同业",
            "企金",
            "零售",
            "投金",
            "其他",
        ]
    
    def baoxiaobumen_db(self) -> List[Text]:
        """Database of supported baoxiaobumen"""
        
        return [
            "研发中心_成都",
            "数据中心_福州",
            "信息中心_福州",
            "信息中心_上海",
            "数据中心_上海",
            "数据中心_成都",
            "研发中心_上海",
            "研发中心_福州",
            "数字卓越中心_上海",
            "数字卓越中心_福州",
            "技术与质量管理中心_上海",
            "技术与质量管理中心_福州",
            "本部管理处室",
        ]
        
    def receive_db(self) -> List[Text]:
        """Database of supported receive"""

        return [
            "是",
            "否",
        ]
        
    def person_level_db(self) -> List[Text]:
        """Database of supported person level"""

        return [
            "8级及8级以下",
            "9-12级",
            "13级",
            "14级以上",
        ]  
        
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["start_time", "end_time", "start_address", "end_address",
                "chuxingren", "person_level", "chengjicishu", "ruzhudi",
                "task", "item", "it_item_num", "fin_item_num", "type", 
                "baoxiaodiqu", "tiaoxian", "baoxiaobumen", "receive"]
    
    def validate_start_time(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate start_time value."""
        start_time = tracker.get_slot('start_time')
        if start_time is not None:
            return {"start_time": start_time}
        else:
            match_time = time_finder(value.strip())
            if match_time is None:
                intent = tracker.latest_message['intent'].get('name')
                if intent != "request_trip":
                    dispatcher.utter_template('utter_wrong_start_time', tracker)
                return {"start_time": None}
            else:
                return {"start_time": match_time}
    
    def validate_end_time(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate end_time value."""
        end_time = tracker.get_slot('end_time')
        if end_time is not None:
            return {"end_time": end_time}
        else:
            match_time = time_finder(value.strip())
            if match_time is None:
                intent = tracker.latest_message['intent'].get('name')
                if intent != "request_trip":
                    dispatcher.utter_template('utter_wrong_end_time', tracker)
                return {"end_time": None}
            else:
                return {"end_time": match_time}
    
    def validate_start_address(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate start_address value."""
        start_address = tracker.get_slot('start_address')

        if start_address is not None:
            return {"start_address": start_address}
        else:
            if value.strip() != "":
                return {"end_address": value.strip()}
            else:
                dispatcher.utter_template('utter_wrong_empty_answer', tracker)
                return {"end_address": None}
    
    def validate_end_address(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate end_address value."""
        end_address = tracker.get_slot('end_address')
        
        if end_address is not None:
            return {"end_address": end_address}
        else:
            if value.strip() != "":
                return {"end_address": value.strip()}
            else:
                dispatcher.utter_template('utter_wrong_empty_answer', tracker)
                return {"end_address": None}
    
    def validate_task(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate task."""
        
        if value.strip() != "":
            return {"task": value.strip()}
        else:
            dispatcher.utter_template('utter_wrong_empty_answer', tracker)
            return {"task": None}
        
    def validate_type(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate type value."""
        
        if value.strip() in self.type_db():
            return {"type": value.strip()}
        else:
            dispatcher.utter_template('utter_wrong_trip_type', tracker)
            return {"type": None}
    
    def validate_baoxiaodiqu(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate baoxiaodiqu value."""
        
        if value.strip() in self.baoxiaodiqu_db():
            return {"baoxiaodiqu": value.strip()}
        else:
            dispatcher.utter_template('utter_wrong_baoxiaodiqu', tracker)
            return {"baoxiaodiqu": None}
    
    def validate_tiaoxian(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate tiaoxian."""
        
        if value.strip() in self.tiaoxian_db():
            return {"tiaoxian": value.strip()}
        else:
            dispatcher.utter_template('utter_wrong_tiaoxian', tracker)
            return {"tiaoxian": None}
        
    def validate_baoxiaobumen(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate baoxiaobumen."""

        if value.strip() in self.baoxiaobumen_db():
            return {"baoxiaobumen": value.strip()}
        else:
            dispatcher.utter_template('utter_wrong_baoxiaobumen', tracker)
            return {"baoxiaobumen": None}
    
    def validate_receive(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate receive."""
        
        if value.strip() in self.receive_db():
            return {"receive": value.strip()}
        else:
            dispatcher.utter_template('utter_wrong_receive', tracker)
            return {"receive": None}
        
    def validate_person_level(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate person_level."""
        
        if value.strip() in self.person_level_db():
            return {"person_level": value.strip()}
        else:
            dispatcher.utter_template('utter_wrong_person_level', tracker)
            return {"person_level": None}
        
    def validate_chengjicishu(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate chengjicishu."""
        
        if re.match("[0-9]+$", value.strip()):
            return {"chengjicishu": value.strip()}
        else:
            dispatcher.utter_template('utter_wrong_chengjicishu', tracker)
            return {"chengjicishu": None}
    
    def validate_ruzhudi(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate ruzhudi."""
        
        if value.strip() != "":
            return {"ruzhudi": value.strip()}
        else:
            dispatcher.utter_template('utter_wrong_empty_answer', tracker)
            return {"ruzhudi": None}
        
    def validate_chuxingren(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate chuxingren."""
        
        if value.strip() != "":
            return {"chuxingren": value.strip()}
        else:
            dispatcher.utter_template('utter_wrong_empty_answer', tracker)
            return {"chuxingren": None}
    
    def validate_item(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate item."""
        
        if value.strip() != "":
            return {"item": value.strip()}
        else:
            dispatcher.utter_template('utter_wrong_empty_answer', tracker)
            return {"item": None}
        
    def validate_it_item_num(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate it_item_num."""
        
        if value.strip() == "无":
            return {"it_item_num": value.strip()}
        if re.match("[A-Z]+\[[0-9]{4}\][0-9]+$", value.strip()):
            return {"it_item_num": value.strip()}
        else:
            dispatcher.utter_template('utter_wrong_it_item_num', tracker)
            return {"it_item_num": None}
        
    def validate_fin_item_num(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate fin_item_num."""
        
        if value.strip() == "无":
            return {"fin_item_num": value.strip()}
        if re.match("[0-9]{13}$",value.strip()):
            return {"fin_item_num": value.strip()}
        else:
            dispatcher.utter_template('utter_wrong_fin_item_num', tracker)
            return {"fin_item_num": None}
    
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "start_time": [
                self.from_entity(
                    entity="start_time", intent=["request_trip"]
            ), self.from_text(not_intent=["stop"])],
            "end_time": [
                self.from_entity(
                    entity="end_time", intent=["request_trip"]
            ), self.from_text(not_intent=["stop"])],
            "start_address": [
                self.from_entity(
                    entity="start_address", intent=["request_trip"]
            ), self.from_text(not_intent=["stop"])],
            "end_address": [
                self.from_entity(
                    entity="end_address", intent=["request_trip"]
            ), self.from_text(not_intent=["stop"])],
            "task": self.from_text(not_intent=["stop"]),
            "item": self.from_text(not_intent=["stop"]),
            "it_item_num": self.from_text(not_intent=["stop"]),
            "fin_item_num": self.from_text(not_intent=["stop"]),
            "type": [self.from_entity(entity="type", intent=["choose_inform"]),
                                           self.from_text(not_intent=["stop"])],
            "tiaoxian": [self.from_entity(entity="tiaoxian", intent=["choose_inform"]),
                                           self.from_text(not_intent=["stop"])],
            "baoxiaobumen": [self.from_entity(entity="baoxiaobumen", intent=["choose_inform"]),
                                           self.from_text(not_intent=["stop"])],
            "baoxiaodiqu": [self.from_entity(entity="baoxiaodiqu", intent=["choose_inform"]),
                                           self.from_text(not_intent=["stop"])],
            "receive": [self.from_entity(entity="receive", intent=["choose_inform"]),
                        self.from_intent(intent="affirm", value="是"),
                        self.from_intent(intent="deny", value="否"),
                        self.from_text(not_intent=["stop"])],
            "ruzhudi": self.from_text(not_intent=["stop"]),
            "chengjicishu": self.from_text(not_intent=["stop"]),
            "chuxingren": self.from_text(not_intent=["stop"]),
            "person_level": [self.from_entity(entity="person_level", intent=["choose_inform"]),
                                           self.from_text(not_intent=["stop"])],
        }
    
    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        start_address = tracker.get_slot('start_address')
        end_address = tracker.get_slot('end_address')
        start_time = tracker.get_slot('start_time')
        end_time = tracker.get_slot('end_time')
        task = tracker.get_slot('task')
        item = tracker.get_slot('item')
        it_item_num = tracker.get_slot('it_item_num')
        fin_item_num = tracker.get_slot('fin_item_num')
        trip_type = tracker.get_slot('type')
        baoxiaodiqu = tracker.get_slot('baoxiaodiqu')
        tiaoxian = tracker.get_slot('tiaoxian')
        baoxiaobumen = tracker.get_slot('baoxiaobumen')
        receive = tracker.get_slot('receive')
        ruzhudi = tracker.get_slot('ruzhudi')
        chengjicishu = tracker.get_slot('chengjicishu')
        person_level = tracker.get_slot('person_level')
        chuxingren = tracker.get_slot('chuxingren')
    
        dispatcher.utter_message(
                text="""差旅申请信息如下:
                        出差行程:{} - {},
                        出差时间:{} - {},
                        乘机次数:{},
                        出行人:{},
                        出行人行员等级: {},
                        入住地:{},
                        出行任务:{},
                        项目:{},
                        IT综合管理平台项目编号:{},
                        财务项目编号:{},
                        出差类型:{},
                        报销地区:{},
                        报销部门:{},
                        条线:{},
                        有无接待:{},
                        请确认是否进行文件办理？""".format(
                start_address, end_address, start_time, end_time, 
                chengjicishu, chuxingren, person_level, ruzhudi, 
                task, item, it_item_num, fin_item_num, trip_type, 
                baoxiaodiqu, baoxiaobumen, tiaoxian, receive))
        return []


class JiaobanForm(FormAction):

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "jiaoban_form"
    
    def nextnode_db(self) -> List[Text]:
        """Database of supported nextnode"""

        return [
            "处室负责人审核",
            "部门成员办理",
            "部门负责人审核",
            "办理",
        ]
    
    def validate_nextnode(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate nextnode."""
        
        if value.strip() in self.nextnode_db():
            return {"nextnode": value.strip()}
        else:
            dispatcher.utter_template('utter_wrong_nextnode', tracker)
            return {"nextnode": None}
        
    def validate_nextperson(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate nextperson."""
        
        if value.strip() != "":
            return {"nextperson": value.strip()}
        else:
            dispatcher.utter_template('utter_wrong_empty_answer', tracker)
            return {"nextperson": None}
        
    def validate_banliyijian(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate banliyijian."""
        
        if value.strip() != "":
            return {"banliyijian": value.strip()}
        else:
            dispatcher.utter_template('utter_wrong_empty_answer', tracker)
            return {"banliyijian": None}
        
        
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["banliyijian", "nextnode", "nextperson"]
    
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "banliyijian": self.from_text(not_intent=["stop"]),
            "nextnode": [self.from_entity(entity="nextnode", intent=["choose_inform"]),
                                           self.from_text(not_intent=["stop"])],
            "nextperson": self.from_text(not_intent=["stop"]),
        }
    
    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        banliyijian = tracker.get_slot('banliyijian')
        nextnode = tracker.get_slot('nextnode')
        nextperson = tracker.get_slot('nextperson')
        dispatcher.utter_message(
                text="""差旅申请交办信息如下:
                        办理意见:{},
                        下一处理步骤:{},
                        下一处理人:{},
                        请确认是否交办？""".format(
                     banliyijian, nextnode, nextperson))
        return []
  
class ActionDefaultFallback(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self):
        return 'action_default_fallback'

    def run(self, dispatcher, tracker, domain):

        dispatcher.utter_template('utter_default', tracker, silent_fail=True)
        return [UserUtteranceReverted()]
    
    
class ActionTripJiaoban(Action):
    """Executes the trip jiaoban action"""

    def name(self):
        return 'action_trip_jiaoban'

    def run(self, dispatcher, tracker, domain):

        dispatcher.utter_template('utter_jiaoban_success', tracker)
        return []
        
        
class ActionTripHotelRecommend(Action):
    """Executes the trip hotel recommend"""

    def name(self):
        return 'action_trip_hotel_recommend'

    def run(self, dispatcher, tracker, domain):
        ruzhudi = tracker.get_slot('ruzhudi')
        
        hotel = get_trip_hotel(ruzhudi)
        if hotel is not None:
            dispatcher.utter_message(hotel)
        return []
        
    
class ActionTripFlightRecommend(Action):
    """Executes the trip flight recommend"""

    def name(self):
        return 'action_trip_flight_recommend'

    def run(self, dispatcher, tracker, domain):
        start_time = tracker.get_slot('start_time')
        end_time = tracker.get_slot('end_time')
        start_address = tracker.get_slot('start_address')
        end_address = tracker.get_slot('end_address')
        
        flight = get_trip_flight(start_time, end_time, 
                                 start_address, end_address)
        if flight is not None:
            dispatcher.utter_message(flight)
        return []
