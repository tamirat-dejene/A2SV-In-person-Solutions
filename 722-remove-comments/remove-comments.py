class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        i, size, res = 0, len(source), []
        cmnt_found = False

        while i < size:
            line = source[i]

            slstart = line.index('//') if '//' in line else -1
            mlstart = line.index('/*') if '/*' in line else -1

            before_cmnt, after_cmnt = '', ''

            if slstart != mlstart: # one of the two or both comments exist
                before_cmnt = line[:slstart if mlstart == -1 or (slstart != -1 and slstart < mlstart) else mlstart]

                if mlstart != -1 and (slstart == -1 or mlstart < slstart):
                    tmp = line[mlstart + 2:]
                    if '*/' in tmp:
                        after_cmnt = tmp[tmp.index('*/') + 2:]
                    else:
                        i += 1
                        while i < size:
                            curr_line = source[i]
                            if '*/' in curr_line:
                                after_cmnt = curr_line[curr_line.index('*/') + 2:]
                                break
                            i += 1

                line = before_cmnt + after_cmnt
                cmnt_found = True
            
            if line: res.append(line)
            i += 1

            if i >= size and cmnt_found:
                i, source, res, cmnt_found = 0, res, [], False
                size = len(source)

        return res