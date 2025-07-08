#!/usr/bin/env python3
"""
Helper script to set up Google Colab secrets for MACRec.

This script provides instructions and validation for setting up API keys
in Google Colab's secret management system.
"""

import os
import sys

def check_colab_environment():
    """Check if running in Google Colab environment."""
    try:
        import google.colab
        return True
    except ImportError:
        return False

def validate_secrets():
    """Validate that required secrets are set up."""
    if not check_colab_environment():
        print("❌ Not running in Google Colab environment.")
        print("This script is designed for Google Colab. For local development, use environment variables or config files.")
        return False
    
    try:
        from google.colab import userdata
        
        secrets_status = {}
        
        # Check DeepSeek API key
        try:
            deepseek_key = userdata.get('DEEPSEEK_API_KEY')
            secrets_status['DEEPSEEK_API_KEY'] = '✅ Set' if deepseek_key else '❌ Not set'
        except:
            secrets_status['DEEPSEEK_API_KEY'] = '❌ Not set'
        
        # Check Google API key
        try:
            google_key = userdata.get('GOOGLE_API_KEY')
            secrets_status['GOOGLE_API_KEY'] = '✅ Set' if google_key else '❌ Not set'
        except:
            secrets_status['GOOGLE_API_KEY'] = '❌ Not set'
        
        # Check Google CSE ID
        try:
            google_cse = userdata.get('GOOGLE_CSE_ID')
            secrets_status['GOOGLE_CSE_ID'] = '✅ Set' if google_cse else '❌ Not set'
        except:
            secrets_status['GOOGLE_CSE_ID'] = '❌ Not set'
        
        print("🔍 Checking Google Colab secrets status:")
        for secret, status in secrets_status.items():
            print(f"  {secret}: {status}")
        
        all_set = all('✅' in status for status in secrets_status.values())
        
        if all_set:
            print("\n🎉 All required secrets are set! You can now run MACRec.")
        else:
            print("\n⚠️  Some secrets are missing. Please set them up:")
            print_setup_instructions()
        
        return all_set
        
    except Exception as e:
        print(f"❌ Error checking secrets: {e}")
        return False

def print_setup_instructions():
    """Print instructions for setting up Google Colab secrets."""
    print("\n📋 How to set up Google Colab secrets:")
    print("1. In your Google Colab notebook, run:")
    print("   from google.colab import userdata")
    print("")
    print("2. Set your DeepSeek API key:")
    print("   userdata.set('DEEPSEEK_API_KEY', 'your-deepseek-api-key-here')")
    print("")
    print("3. Set your Google API key:")
    print("   userdata.set('GOOGLE_API_KEY', 'your-google-api-key-here')")
    print("")
    print("4. Set your Google Custom Search Engine ID:")
    print("   userdata.set('GOOGLE_CSE_ID', 'your-google-cse-id-here')")
    print("")
    print("5. Verify the setup by running this script again:")
    print("   !python setup_colab_secrets.py")
    print("")
    print("💡 Note: You only need to set these secrets once per Colab session.")

def main():
    """Main function."""
    print("🚀 MACRec Google Colab Secrets Setup")
    print("=" * 40)
    
    if len(sys.argv) > 1 and sys.argv[1] == '--instructions':
        print_setup_instructions()
        return
    
    validate_secrets()

if __name__ == '__main__':
    main() 