from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
import hashlib
import hmac
import base64
import uuid

class EsewaTemplate(TemplateView):
    template_name='esewapayment/esewa.html'

    

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context = super().get_context_data(**kwargs)
        total_amount=str(self.kwargs.get('amount'))
        uid=uuid.uuid4()
        context['uid']=uid
        secret_key=f"8gBm/:&EnhH.1/q" 
        sid=f"total_amount={total_amount},transaction_uuid={uid},product_code=EPAYTEST"
        key=secret_key.encode('utf-8')
        message=sid.encode('utf-8')
        hmac_sha256= hmac.new(key,message,hashlib.sha256)
        hmac_sha256=hmac_sha256.digest()
        context['signature'] = base64.b64encode(hmac_sha256).decode('utf-8')

        
        return context
    
  