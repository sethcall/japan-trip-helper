const japaneseWords = [
    { en: "Hello", jp: "こんにちは", phonetic: "Konnichiwa" },
    { en: "Thank you", jp: "ありがとう", phonetic: "Arigatou" },
    { en: "Excuse me", jp: "すみません", phonetic: "Sumimasen" },
    { en: "Yes", jp: "はい", phonetic: "Hai" },
    { en: "No", jp: "いいえ", phonetic: "Iie" },
    { en: "Please", jp: "おねがいします", phonetic: "Onegaishimasu" },
    { en: "Good morning", jp: "おはようございます", phonetic: "Ohayou gozaimasu" },
    { en: "Good evening", jp: "こんばんは", phonetic: "Konbanwa" },
    { en: "Good night", jp: "おやすみなさい", phonetic: "Oyasuminasai" },
    { en: "I don't understand", jp: "わかりません", phonetic: "Wakarimasen" },
    { en: "Water", jp: "みず", phonetic: "Mizu" },
    { en: "Delicious", jp: "おいしい", phonetic: "Oishii" },
    { en: "Toilet", jp: "トイレ", phonetic: "Toire" },
    { en: "Station", jp: "えき", phonetic: "Eki" },
    { en: "Where?", jp: "どこ", phonetic: "Doko" },
    { en: "Train", jp: "でんしゃ", phonetic: "Densha" },
    { en: "Subway", jp: "ちかてつ", phonetic: "Chikatetsu" },
    { en: "Bus", jp: "バス", phonetic: "Basu" },
    { en: "Ticket", jp: "きっぷ", phonetic: "Kippu" },
    { en: "Hotel", jp: "ホテル", phonetic: "Hoteru" },
    { en: "Restaurant", jp: "レストラン", phonetic: "Resutoran" },
    { en: "Menu", jp: "メニュー", phonetic: "Menyuu" },
    { en: "Check/Bill", jp: "おかいけい", phonetic: "Okaikei" },
    { en: "Beer", jp: "ビール", phonetic: "Biiru" },
    { en: "Sake", jp: "おさけ", phonetic: "Osake" },
    { en: "Cheers", jp: "かんぱい", phonetic: "Kanpai" },
    { en: "Convenience Store", jp: "コンビニ", phonetic: "Konbini" },
    { en: "Sorry", jp: "ごめんなさい", phonetic: "Gomennasai" },
    { en: "One", jp: "いち", phonetic: "Ichi" },
    { en: "Two", jp: "に", phonetic: "Ni" },
    { en: "Three", jp: "さん", phonetic: "San" }
];

const japanesePhrases = [
    { en: "Where is the toilet?", jp: "トイレはどこですか？", phonetic: "Toire wa doko desu ka?" },
    { en: "How much is this?", jp: "いくらですか？", phonetic: "Ikura desu ka?" },
    { en: "Check, please.", jp: "おかいけいおねがいします。", phonetic: "Okaikei onegaishimasu." },
    { en: "Do you speak English?", jp: "えいごをはなせますか？", phonetic: "Eigo o hanasemasu ka?" },
    { en: "I am vegetarian.", jp: "わたしはベジタリアンです。", phonetic: "Watashi wa bejitarian desu." },
    { en: "I have an allergy.", jp: "アレルギーがあります。", phonetic: "Arerugii ga arimasu." },
    { en: "Where is the station?", jp: "えきはどこですか？", phonetic: "Eki wa doko desu ka?" },
    { en: "Does this train go to Tokyo?", jp: "このでんしゃはとうきょうにいきますか？", phonetic: "Kono densha wa Tokyo ni ikimasu ka?" },
    { en: "Can I use a credit card?", jp: "クレジットカードはつかえますか？", phonetic: "Kurejitto kaado wa tsukaemasu ka?" },
    { en: "Water, please.", jp: "おみずおねがいします。", phonetic: "Omizu onegaishimasu." },
    { en: "Could you take a photo?", jp: "しゃしんをとってもらえますか？", phonetic: "Shashin o totte moraemasu ka?" },
    { en: "It was delicious.", jp: "おいしかったです。", phonetic: "Oishikatta desu." },
    { en: "Nice to meet you.", jp: "はじめまして。", phonetic: "Hajimemashite." },
    { en: "What do you recommend?", jp: "おすすめはなんですか？", phonetic: "Osusume wa nan desu ka?" },
    { en: "I am lost.", jp: "みちにまよいました。", phonetic: "Michi ni mayoimashita." }
];

// Export for use in Node.js (build scripts) or Browser (via window/global)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { japaneseWords, japanesePhrases };
} else {
    window.japaneseData = { japaneseWords, japanesePhrases };
}
