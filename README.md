Incapsula Workaround
=============================================================================================================
Use this to scrape data off websites using Incapsula.

This is applicable for websites which are able to detect scraping code (urllib requests return ROBOTS.txt or the reCaptcha question)

Methodology:
  - Clear browser cache
  - Load url in firefox
  - Wait for few seconds to let all data load
  - Decode cache data
  - Parse through files for required data
  
  How to find cache dir: http://www.acquireforensics.com/blog/mozilla-cache-folder.html 
  
  
