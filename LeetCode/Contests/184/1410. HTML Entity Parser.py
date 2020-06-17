# Quotation Mark: the entity is &quot; and symbol character is ".
# Single Quote Mark: the entity is &apos; and symbol character is '.
# Ampersand: the entity is &amp; and symbol character is &.
# Greater Than Sign: the entity is &gt; and symbol character is >.
# Less Than Sign: the entity is &lt; and symbol character is <.
# Slash: the entity is &frasl; and symbol character is /.

class Solution:
    def entityParser(self, text: str) -> str:
        dic = {
            'quot': '"',
            'apos': "'",
            'amp' : '&',
            'gt' : '>',
            'lt' : '<',
            'frasl': '/'
        }

        i = 0
        andStart = -1
        while i < len(text):
            if text[i] == '&':
                andStart = i
            if text[i] == ';' and andStart != -1:
                symbolLen = i - andStart - 1
                if symbolLen <= 5 and text[andStart+1:i] in dic:
                    text = text[0:andStart] + dic[text[andStart+1:i]] + text[i+1:]
                    i -= symbolLen + 1
                    andStart = -1
            i += 1
        return text

a = Solution()
print(a.entityParser("&amp; is an HTML entity but &ambassador; is not."))
print(a.entityParser("and I quote: &quot;...&quot;"))
print(a.entityParser("x &gt; y &amp;&amp; x &lt; y is always false"))