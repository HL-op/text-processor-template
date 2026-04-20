class TextProcessor:
    def word_count(self, text):
        """统计文本中的单词数量（中英文混合文本）
        
        Args:
            text: 输入文本
            
        Returns:
            int: 单词数量
        """
        # TODO: 实现单词统计功能
        # 提示：可以使用split()方法分割单词，注意处理中英文混合的情况
        pass
    
    def char_frequency(self, text):
        """统计每个字符出现的频率，返回前5个高频字符
        
        Args:
            text: 输入文本
            
        Returns:
            list: 前5个高频字符及其频率的列表，格式为[(char, frequency), ...]
        """
        # TODO: 实现字符频率统计功能
        # 提示：可以使用字典统计每个字符的出现次数，然后排序并返回前5个
        pass
    
    def sentiment_analysis(self, text):
        """简单的情感分析（基于关键词匹配）
        
        Args:
            text: 输入文本
            
        Returns:
            str: 情感倾向，'positive', 'negative' 或 'neutral'
        """
        # TODO: 实现情感分析功能
        # 提示：可以定义积极和消极的关键词列表，根据匹配情况判断情感倾向
        pass
    
    def text_summary(self, text, n=3):
        """提取文本摘要（取前n个句子）
        
        Args:
            text: 输入文本
            n: 要提取的句子数量，默认为3
            
        Returns:
            str: 文本摘要
        """
        # TODO: 实现文本摘要功能
        # 提示：可以使用split('.')方法分割句子，然后取前n个句子
        pass

# 示例使用
if __name__ == "__main__":
    processor = TextProcessor()
    
    # 测试word_count
    print("Word count test:")
    print(processor.word_count("Hello 世界"))
    print(processor.word_count("This is a test"))
    
    # 测试char_frequency
    print("\nChar frequency test:")
    print(processor.char_frequency("hello world"))
    
    # 测试sentiment_analysis
    print("\nSentiment analysis test:")
    print(processor.sentiment_analysis("I love this"))
    print(processor.sentiment_analysis("I hate this"))
    print(processor.sentiment_analysis("This is a test"))
    
    # 测试text_summary
    print("\nText summary test:")
    text = "This is the first sentence. This is the second sentence. This is the third sentence. This is the fourth sentence."
    print(processor.text_summary(text))
    print(processor.text_summary(text, n=2))