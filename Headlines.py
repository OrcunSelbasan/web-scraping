{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "fb456875-9183-4cb6-875d-c0af4eb1ac58",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\nStage : Development -01\\n@author : Yiğit Nihat Doğancık , 120200084\\n@author : Lütfü Orçun Selbasan , 119200063\\n@author : Sinan Hacisoyu, 119200060\\n\\n'"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"\"\"\n",
    "Stage : Development -01\n",
    "@author : Yiğit Nihat Doğancık , 120200084\n",
    "@author : Lütfü Orçun Selbasan , 119200063\n",
    "@author : Sinan Hacisoyu, 119200060\n",
    "\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "e30fb343-5942-4469-80f1-94ae6bebe982",
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup\n",
    "import requests\n",
    "import codecs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "90a05a1b-a3e4-463c-a1bd-47105114e60d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#alternative to request\n",
    "\n",
    "#file = codecs.open(\"science.html\", \"r\", \"utf-8\")\n",
    "#soup = BeautifulSoup(file, 'html.parser')\n",
    "\n",
    "#print(file.read())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "4a8ec3e2-4b07-421d-8330-8887c8ece3be",
   "metadata": {},
   "outputs": [],
   "source": [
    "nytimes_sciences = \"https://www.nytimes.com/section/science\"\n",
    "res = requests.get(nytimes_sciences)\n",
    "soup = BeautifulSoup(res.content, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "0542fdb0-8f5d-4194-8f85-db9b92b95d1b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "As Officials Ease Restrictions, China Faces New Pandemic Risks\n",
      "F.D.A. Considering New Approach to Blood Donation by Gay and Bisexual Men\n",
      "Biden Promises Protections for Nevada’s Spirit Mountain\n",
      "Deaths From Substance Abuse Rose Sharply Among Older Americans in 2020\n",
      "Alzheimer’s Drug May Benefit Some Patients, New Data Shows\n",
      "Hurricane Season Ends, Marked by Quiet August and Deadly September\n",
      "One Step Closer to a Universal Flu Vaccine?\n",
      "Can This Man Stop Lying?\n",
      "Whole Foods to Stop Buying Maine Lobster Amid Risk to Endangered Whales\n",
      "Monkeypox Has a New Name: Mpox\n"
     ]
    }
   ],
   "source": [
    "headers = soup.select(\"li.css-112uytv div div a h2\")\n",
    "#dates = soup.select(\"li.css-112uytv div.css-1cp3ece div.css-agsgss span\")\n",
    "#print(dates)\n",
    "for header in headers:\n",
    "    print(header.text)\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "a372398f-d905-42be-a95d-d0b0028e77c1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[]\n"
     ]
    }
   ],
   "source": [
    "#we may get date information using urls in the link tags.\n",
    "dates = soup.select(\"li.css-112uytv div.css-1cp3ece div.css-agsgss span\")\n",
    "print(dates)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3ecbeaa5-8a6d-40bf-b712-d0e806ebde82",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
