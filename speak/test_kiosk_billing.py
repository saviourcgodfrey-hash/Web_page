import pytest
from unittest.mock import patch, MagicMock
from kiosk_billing import charge_payment_card

def test_charge_payment_card_success():
    """Test payment card charges with a mocked HTTP post response."""
    # Temporarily patch requests.post inside payment_gateway
    with patch("requests.post") as mock_post:
        # Create a simulated response object
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": "tx_90812", "status": "approved"}
        
        # Assign our simulated response to our mock post connector
        mock_post.return_value = mock_response
        
        # Execute the function
        result = charge_payment_card("tok_alice123", 450)
        
        # Verify the calculations
        assert result["id"] == "tx_90812"
        assert result["status"] == "approved"
        
        # Verify that the post was called with correct parameters
        mock_post.assert_called_once_with(
            "https://api.merchant.com/charge", 
            json={"token": "tok_alice123", "amount": 450}
        )
 

