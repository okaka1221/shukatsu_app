from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status
from api.entrysheet.models import EntrySheet
import numpy as np

class EntrySheetAPITest(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('api.entrysheet.urls'))
    ]

    def test_post_valid_entrysheet(self):
        prev_count = EntrySheet.objects.all().count()

        url = reverse('entrysheet')
        data = {
            'keywords': 'キー１　キー２　キー３',
            'text': '私の強みは、行動力にあると考えています。大学2年生の8月から大学3年生の12月まで、不動産の会社でインターン生として投資用の中古物件の販売を経験しました。当初はアポを取ることもできず、営業成績は12人いた同期のインターン生の中でも最下位でした。しかしこのままではいけないと思い、自分の課題・弱点をリストアップして、それらを克服するための行動を起こしていきました。具体的には、①営業やコミュニケーション系のセミナーへの参加。②関連書籍の読み込み。③社内の先輩や上司の方々にアドバイスを求める。この3点を地道に継続したことで、自分の課題・弱点を一つずつ潰すことができ、営業力を着実に向上していきました。その結果、1年後には同期の中でTOPの営業成績を修めることができました。この経験を通して、課題解決のために現状と理想の差を分析して、その差を埋めるための具体的な行動を起こすことの重要性を学びました。貴社の業務においても、課題に対する打ち手を冷静に分析し、問題解決や目標達成のための行動を自発的に起こせればと考えております。',
            'label': True
        }

        response = self.client.post(url, data, format='json')
        res_data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(res_data['encoded_wordcloud']), bytes)
        self.assertEqual(type(res_data['keyword_sim_score']), np.float64)
        self.assertEqual(type(res_data['jikoPR_score']), np.float64)
        self.assertEqual(EntrySheet.objects.all().count(), prev_count+1)
    
    def test_post_valid_entrysheet_with_short_text(self):
        prev_count = EntrySheet.objects.all().count()

        url = reverse('entrysheet')
        data = {
            'keywords': 'キー１　キー２　キー３',
            'text': '私の強みは、行動力にあると考えています。大学2年生の8月から大学3年生の12月まで、不動産の会社でインターン生として投資用の中古物件の販売を経験しました。',
            'label': True
        }

        response = self.client.post(url, data, format='json')
        res_data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(res_data['encoded_wordcloud']), bytes)
        self.assertEqual(type(res_data['keyword_sim_score']), np.float64)
        self.assertEqual(type(res_data['jikoPR_score']), np.float64)
        self.assertEqual(EntrySheet.objects.all().count(), prev_count)

    def test_post_valid_entrysheet_without_key(self):
        prev_count = EntrySheet.objects.all().count()
        
        url = reverse('entrysheet')
        data = {
            'keywords': '',
            'text': '私の強みは、行動力にあると考えています。大学2年生の8月から大学3年生の12月まで、不動産の会社でインターン生として投資用の中古物件の販売を経験しました。当初はアポを取ることもできず、営業成績は12人いた同期のインターン生の中でも最下位でした。しかしこのままではいけないと思い、自分の課題・弱点をリストアップして、それらを克服するための行動を起こしていきました。具体的には、①営業やコミュニケーション系のセミナーへの参加。②関連書籍の読み込み。③社内の先輩や上司の方々にアドバイスを求める。この3点を地道に継続したことで、自分の課題・弱点を一つずつ潰すことができ、営業力を着実に向上していきました。その結果、1年後には同期の中でTOPの営業成績を修めることができました。この経験を通して、課題解決のために現状と理想の差を分析して、その差を埋めるための具体的な行動を起こすことの重要性を学びました。貴社の業務においても、課題に対する打ち手を冷静に分析し、問題解決や目標達成のための行動を自発的に起こせればと考えております。',
            'label': True
        }

        response = self.client.post(url, data, format='json')
        res_data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(res_data['encoded_wordcloud']), bytes)
        self.assertEqual(res_data['keyword_sim_score'], None)
        self.assertEqual(type(res_data['jikoPR_score']), np.float64)
        self.assertEqual(EntrySheet.objects.all().count(), prev_count+1)

    def test_post_valid_entrysheet_with_null_label(self):
        prev_count = EntrySheet.objects.all().count()
        
        url = reverse('entrysheet')
        data = {
            'keywords': 'キー１　キー２　キー３',
            'text': '私の強みは、行動力にあると考えています。大学2年生の8月から大学3年生の12月まで、不動産の会社でインターン生として投資用の中古物件の販売を経験しました。当初はアポを取ることもできず、営業成績は12人いた同期のインターン生の中でも最下位でした。しかしこのままではいけないと思い、自分の課題・弱点をリストアップして、それらを克服するための行動を起こしていきました。具体的には、①営業やコミュニケーション系のセミナーへの参加。②関連書籍の読み込み。③社内の先輩や上司の方々にアドバイスを求める。この3点を地道に継続したことで、自分の課題・弱点を一つずつ潰すことができ、営業力を着実に向上していきました。その結果、1年後には同期の中でTOPの営業成績を修めることができました。この経験を通して、課題解決のために現状と理想の差を分析して、その差を埋めるための具体的な行動を起こすことの重要性を学びました。貴社の業務においても、課題に対する打ち手を冷静に分析し、問題解決や目標達成のための行動を自発的に起こせればと考えております。',
            'label': None
        }

        response = self.client.post(url, data, format='json')
        res_data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(res_data['encoded_wordcloud']), bytes)
        self.assertEqual(type(res_data['keyword_sim_score']), np.float64)
        self.assertEqual(type(res_data['jikoPR_score']), np.float64)
        self.assertEqual(EntrySheet.objects.all().count(), prev_count)
    
    def test_post_invalid_entrysheet(self):
        prev_count = EntrySheet.objects.all().count()
        
        url = reverse('entrysheet')
        data = {
            'keywords': 'キー１　キー２　キー３',
            'text': '',
            'label': True
        }

        response = self.client.post(url, data, format='json')
        res_data = response.data

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(EntrySheet.objects.all().count(), prev_count)
