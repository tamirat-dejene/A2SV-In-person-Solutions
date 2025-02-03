class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        j, size, result = 0, len(source), []
        in_comment = False
        temp = []

        for line in source:
            after_removing = []
            i = 0
            while i < len(line):
                if in_comment:
                    # inside of a comment
                    # */ -> we are looking for
                    if line[i] == "*" and i+1 < len(line) and line[i+1] == "/":
                        in_comment = False
                        after_removing = temp
                        i += 1
                else:
                    # if we encouter normal value
                    if line[i] != "/":
                        after_removing.append(line[i])
                    else:
                        if i + 1 < len(line) and line[i+1] in ["*", "/"]:
                            # start of a comment
                            if line[i+1] == "*":
                                # multi-line comments
                                temp = after_removing[::]
                                after_removing = []
                                in_comment = True
                                i += 1
                            else:
                                # one line comment won't consider anything
                                break
                        else:
                            after_removing.append(line[i])
                i += 1

            if after_removing:
                
                result.append(''.join(after_removing))
            
        return result




            # if '/*' in line:
            #     before_comment = line[:line.index('/*')]
            #     after_comment = ''
            #     while i < size:
            #         curr_line = source[i]
            #         if '*/' in curr_line:
            #             after_comment = curr_line[curr_line.index('*/') + 2:]
            #             break
            #         i += 1
                
            #     after_removing = ''.join([before_comment, after_comment])
            #     if after_removing: result.append(after_removing)

            # elif "//" in line:
            #     after_removing = line[:line.index('//')]
            #     if after_removing: result.append(after_removing)
            # else:
            #     result.append(line)
            
            # i += 1
        
        # return result