#-------------------------------------------------------------------------------
# Log 발췌
#-------------------------------------------------------------------------------
def get_log_extracts(log_exts, rev_logs):
    log_exts.append("===================== [error log extraction] =====================")
    for item in rev_logs:
        if '[CURRENT-CONTENT]' in item:
            log_exts.append(item)
            log_exts.append("===================== [error log extraction] =====================")
            log_exts.append('\n')
            return log_exts
        log_exts.append(item)