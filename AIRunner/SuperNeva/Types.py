from enum import Enum

from datetime import date

from typing import TypedDict, Optional, Any


class FileInput(TypedDict, total=False):
    _id: Optional["str"]
    urls: Optional["FileURLsInput"]
    meta: Optional["FileMetaInput"]
    origin: Optional["str"]
    path: Optional["str"]
    name: Optional["str"]
    key: Optional["str"]
    acl: Optional["str"]
    bucket: Optional["str"]
    createdBy: Optional["FileOwnerInput"]
    order: Optional["int"]


class FileMetaInput(TypedDict, total=False):
    name: Optional["str"]
    size: Optional["float"]
    type: Optional["str"]
    width: Optional["float"]
    height: Optional["float"]
    preview: Optional["bool"]
    color: Optional["str"]
    blurHash: Optional["str"]


class FileStreamInput(TypedDict, total=False):
    _id: Optional["str"]
    url: Optional["str"]
    thumbnails: Optional["None"]


class FileURLsInput(TypedDict, total=False):
    original: Optional["str"]
    thumbnail: Optional["str"]
    medium: Optional["str"]
    large: Optional["str"]
    attribution: Optional["str"]
    tracker: Optional["str"]
    stream: Optional["FileStreamInput"]


class FileOwnerInput(TypedDict, total=False):
    _id: Optional["str"]
    firstName: Optional["str"]
    lastName: Optional["str"]
    url: Optional["str"]
    picture: Optional["str"]


class File(TypedDict, total=False):
    _id: Optional["str"]
    meta: Optional["FileMeta"]
    urls: Optional["FileURLs"]
    cdn: Optional["FileURLs"]
    origin: Optional["str"]
    path: Optional["str"]
    name: Optional["str"]
    key: Optional["str"]
    acl: Optional["str"]
    createdBy: Optional["FileOwner"]
    order: Optional["int"]


class FileOwner(TypedDict, total=False):
    _id: Optional["str"]
    firstName: Optional["str"]
    lastName: Optional["str"]
    url: Optional["str"]
    picture: Optional["str"]


class FileMeta(TypedDict, total=False):
    name: Optional["str"]
    size: Optional["float"]
    type: Optional["str"]
    width: Optional["float"]
    height: Optional["float"]
    preview: Optional["bool"]
    color: Optional["str"]
    blurHash: Optional["str"]


class FileStream(TypedDict, total=False):
    _id: Optional["str"]
    url: Optional["str"]
    thumbnails: Optional["None"]


class FileURLs(TypedDict, total=False):
    original: Optional["str"]
    thumbnail: Optional["str"]
    medium: Optional["str"]
    large: Optional["str"]
    attribution: Optional["str"]
    tracker: Optional["str"]
    thumbnails: Optional["None"]
    stream: Optional["FileStream"]


class FileAuthorization(TypedDict, total=False):
    policy: Optional["Any"]
    signature: Optional["str"]
    accessKey: Optional["str"]
    postUrl: Optional["str"]
    url: Optional["str"]
    secureUrl: Optional["str"]
    relativeUrl: Optional["str"]
    bucket: Optional["str"]
    path: Optional["str"]
    acl: Optional["str"]
    key: Optional["str"]
    fileType: Optional["str"]
    fileName: Optional["str"]
    fileSize: Optional["int"]
    metaUuid: Optional["str"]
    metaDate: Optional["str"]
    metaCredential: Optional["str"]


class FileAuthorizationInput(TypedDict, total=False):
    path: Optional["str"]
    fileType: Optional["None"]
    fileName: Optional["None"]
    fileSize: Optional["None"]


class SimpleResponse(TypedDict, total=False):
    success: Optional["bool"]
    response: Optional["Any"]
    errors: Optional["None"]


class Error(TypedDict, total=False):
    message: Optional["None"]
    code: Optional["None"]
    key: Optional["str"]
    reason: Optional["str"]
    type: Optional["str"]
    name: Optional["str"]
    value: Optional["str"]
    data: Optional["Any"]
    stacktrace: Optional["Any"]


class ErrorInput(TypedDict, total=False):
    message: Optional["None"]
    code: Optional["None"]
    key: Optional["str"]
    reason: Optional["str"]
    type: Optional["str"]
    name: Optional["str"]
    value: Optional["str"]
    data: Optional["Any"]
    stacktrace: Optional["Any"]


class PriceLite(TypedDict, total=False):
    amount: Optional["float"]
    currency: Optional["Currency"]


class Price(TypedDict, total=False):
    amount: Optional["float"]
    currency: Optional["Currency"]
    converted: Optional["PriceLite"]


class PriceInput(TypedDict, total=False):
    amount: Optional["None"]
    currency: Optional["None"]


class Currency(str, Enum):
    AED = "AED"
    AFN = "AFN"
    ALL = "ALL"
    AMD = "AMD"
    ANG = "ANG"
    AOA = "AOA"
    ARS = "ARS"
    AUD = "AUD"
    AWG = "AWG"
    AZN = "AZN"
    BAM = "BAM"
    BBD = "BBD"
    BDT = "BDT"
    BGN = "BGN"
    BHD = "BHD"
    BIF = "BIF"
    BMD = "BMD"
    BND = "BND"
    BOB = "BOB"
    BRL = "BRL"
    BSD = "BSD"
    BTN = "BTN"
    BWP = "BWP"
    BYN = "BYN"
    BYR = "BYR"
    BZD = "BZD"
    CAD = "CAD"
    CDF = "CDF"
    CHF = "CHF"
    CLF = "CLF"
    CLP = "CLP"
    CNY = "CNY"
    COP = "COP"
    CRC = "CRC"
    CUC = "CUC"
    CUP = "CUP"
    CVE = "CVE"
    CZK = "CZK"
    DJF = "DJF"
    DKK = "DKK"
    DOP = "DOP"
    DZD = "DZD"
    EGP = "EGP"
    ERN = "ERN"
    ETB = "ETB"
    EUR = "EUR"
    FJD = "FJD"
    FKP = "FKP"
    GBP = "GBP"
    GEL = "GEL"
    GGP = "GGP"
    GHS = "GHS"
    GIP = "GIP"
    GMD = "GMD"
    GNF = "GNF"
    GTQ = "GTQ"
    GYD = "GYD"
    HKD = "HKD"
    HNL = "HNL"
    HRK = "HRK"
    HTG = "HTG"
    HUF = "HUF"
    IDR = "IDR"
    ILS = "ILS"
    IMP = "IMP"
    INR = "INR"
    IQD = "IQD"
    IRR = "IRR"
    ISK = "ISK"
    JEP = "JEP"
    JMD = "JMD"
    JOD = "JOD"
    JPY = "JPY"
    KES = "KES"
    KGS = "KGS"
    KHR = "KHR"
    KMF = "KMF"
    KPW = "KPW"
    KRW = "KRW"
    KWD = "KWD"
    KYD = "KYD"
    KZT = "KZT"
    LAK = "LAK"
    LBP = "LBP"
    LKR = "LKR"
    LRD = "LRD"
    LSL = "LSL"
    LTL = "LTL"
    LVL = "LVL"
    LYD = "LYD"
    MAD = "MAD"
    MDL = "MDL"
    MGA = "MGA"
    MKD = "MKD"
    MMK = "MMK"
    MNT = "MNT"
    MOP = "MOP"
    MRO = "MRO"
    MUR = "MUR"
    MVR = "MVR"
    MWK = "MWK"
    MXN = "MXN"
    MYR = "MYR"
    MZN = "MZN"
    NAD = "NAD"
    NGN = "NGN"
    NIO = "NIO"
    NOK = "NOK"
    NPR = "NPR"
    NZD = "NZD"
    OMR = "OMR"
    PAB = "PAB"
    PEN = "PEN"
    PGK = "PGK"
    PHP = "PHP"
    PKR = "PKR"
    PLN = "PLN"
    PYG = "PYG"
    QAR = "QAR"
    RON = "RON"
    RSD = "RSD"
    RUB = "RUB"
    RWF = "RWF"
    SAR = "SAR"
    SBD = "SBD"
    SCR = "SCR"
    SDG = "SDG"
    SEK = "SEK"
    SGD = "SGD"
    SHP = "SHP"
    SLL = "SLL"
    SOS = "SOS"
    SRD = "SRD"
    STD = "STD"
    SVC = "SVC"
    SYP = "SYP"
    SZL = "SZL"
    THB = "THB"
    TJS = "TJS"
    TMT = "TMT"
    TND = "TND"
    TOP = "TOP"
    TRY = "TRY"
    TTD = "TTD"
    TWD = "TWD"
    TZS = "TZS"
    UAH = "UAH"
    UGX = "UGX"
    USD = "USD"
    UYU = "UYU"
    UZS = "UZS"
    VEF = "VEF"
    VND = "VND"
    VUV = "VUV"
    WST = "WST"
    XAF = "XAF"
    XAG = "XAG"
    XAU = "XAU"
    XCD = "XCD"
    XDR = "XDR"
    XOF = "XOF"
    XPF = "XPF"
    YER = "YER"
    ZAR = "ZAR"
    ZMK = "ZMK"
    ZMW = "ZMW"
    ZWL = "ZWL"
    BTC = "BTC"
    ETH = "ETH"
    ALGO = "ALGO"
    SOL = "SOL"
    USDT = "USDT"
    USDC = "USDC"
    XRP = "XRP"
    DOGE = "DOGE"
    SHIB = "SHIB"
    DOT = "DOT"
    ADA = "ADA"
    BNB = "BNB"
    BUSD = "BUSD"
    MATIC = "MATIC"
    DAI = "DAI"
    AVAX = "AVAX"
    UNI = "UNI"
    XTZ = "XTZ"


class Locale(str, Enum):
    AF_NA = "AF_NA"
    AF_ZA = "AF_ZA"
    AF = "AF"
    AK_GH = "AK_GH"
    AK = "AK"
    SQ_AL = "SQ_AL"
    SQ = "SQ"
    AM_ET = "AM_ET"
    AM = "AM"
    AR_DZ = "AR_DZ"
    AR_BH = "AR_BH"
    AR_EG = "AR_EG"
    AR_IQ = "AR_IQ"
    AR_JO = "AR_JO"
    AR_KW = "AR_KW"
    AR_LB = "AR_LB"
    AR_LY = "AR_LY"
    AR_MA = "AR_MA"
    AR_OM = "AR_OM"
    AR_QA = "AR_QA"
    AR_SA = "AR_SA"
    AR_SD = "AR_SD"
    AR_SY = "AR_SY"
    AR_TN = "AR_TN"
    AR_AE = "AR_AE"
    AR_YE = "AR_YE"
    AR = "AR"
    HY_AM = "HY_AM"
    HY = "HY"
    AS_IN = "AS_IN"
    AS = "AS"
    ASA_TZ = "ASA_TZ"
    ASA = "ASA"
    AZ_CYRL = "AZ_CYRL"
    AZ_CYRL_AZ = "AZ_CYRL_AZ"
    AZ_LATN = "AZ_LATN"
    AZ_LATN_AZ = "AZ_LATN_AZ"
    AZ = "AZ"
    BM_ML = "BM_ML"
    BM = "BM"
    EU_ES = "EU_ES"
    EU = "EU"
    BE_BY = "BE_BY"
    BE = "BE"
    BEM_ZM = "BEM_ZM"
    BEM = "BEM"
    BEZ_TZ = "BEZ_TZ"
    BEZ = "BEZ"
    BN_BD = "BN_BD"
    BN_IN = "BN_IN"
    BN = "BN"
    BS_BA = "BS_BA"
    BS = "BS"
    BG_BG = "BG_BG"
    BG = "BG"
    MY_MM = "MY_MM"
    MY = "MY"
    YUE_HANT_HK = "YUE_HANT_HK"
    CA_ES = "CA_ES"
    CA = "CA"
    TZM_LATN = "TZM_LATN"
    TZM_LATN_MA = "TZM_LATN_MA"
    TZM = "TZM"
    CHR_US = "CHR_US"
    CHR = "CHR"
    CGG_UG = "CGG_UG"
    CGG = "CGG"
    ZH_HANS = "ZH_HANS"
    ZH_HANS_CN = "ZH_HANS_CN"
    ZH_HANS_HK = "ZH_HANS_HK"
    ZH_HANS_MO = "ZH_HANS_MO"
    ZH_HANS_SG = "ZH_HANS_SG"
    ZH_HANT = "ZH_HANT"
    ZH_HANT_HK = "ZH_HANT_HK"
    ZH_HANT_MO = "ZH_HANT_MO"
    ZH_HANT_TW = "ZH_HANT_TW"
    ZH = "ZH"
    KW_GB = "KW_GB"
    KW = "KW"
    HR_HR = "HR_HR"
    HR = "HR"
    CS_CZ = "CS_CZ"
    CS = "CS"
    DA_DK = "DA_DK"
    DA = "DA"
    NL_BE = "NL_BE"
    NL_NL = "NL_NL"
    NL = "NL"
    EBU_KE = "EBU_KE"
    EBU = "EBU"
    EN_AS = "EN_AS"
    EN_AU = "EN_AU"
    EN_BE = "EN_BE"
    EN_BZ = "EN_BZ"
    EN_BW = "EN_BW"
    EN_CA = "EN_CA"
    EN_GU = "EN_GU"
    EN_HK = "EN_HK"
    EN_IN = "EN_IN"
    EN_IE = "EN_IE"
    EN_IL = "EN_IL"
    EN_JM = "EN_JM"
    EN_MT = "EN_MT"
    EN_MH = "EN_MH"
    EN_MU = "EN_MU"
    EN_NA = "EN_NA"
    EN_NZ = "EN_NZ"
    EN_MP = "EN_MP"
    EN_PK = "EN_PK"
    EN_PH = "EN_PH"
    EN_SG = "EN_SG"
    EN_ZA = "EN_ZA"
    EN_TT = "EN_TT"
    EN_UM = "EN_UM"
    EN_VI = "EN_VI"
    EN_GB = "EN_GB"
    EN_US = "EN_US"
    EN_ZW = "EN_ZW"
    EN = "EN"
    EO = "EO"
    ET_EE = "ET_EE"
    ET = "ET"
    EE_GH = "EE_GH"
    EE_TG = "EE_TG"
    EE = "EE"
    FO_FO = "FO_FO"
    FO = "FO"
    FIL_PH = "FIL_PH"
    FIL = "FIL"
    FI_FI = "FI_FI"
    FI = "FI"
    FR_BE = "FR_BE"
    FR_BJ = "FR_BJ"
    FR_BF = "FR_BF"
    FR_BI = "FR_BI"
    FR_CM = "FR_CM"
    FR_CA = "FR_CA"
    FR_CF = "FR_CF"
    FR_TD = "FR_TD"
    FR_KM = "FR_KM"
    FR_CG = "FR_CG"
    FR_CD = "FR_CD"
    FR_CI = "FR_CI"
    FR_DJ = "FR_DJ"
    FR_GQ = "FR_GQ"
    FR_FR = "FR_FR"
    FR_GA = "FR_GA"
    FR_GP = "FR_GP"
    FR_GN = "FR_GN"
    FR_LU = "FR_LU"
    FR_MG = "FR_MG"
    FR_ML = "FR_ML"
    FR_MQ = "FR_MQ"
    FR_MC = "FR_MC"
    FR_NE = "FR_NE"
    FR_RW = "FR_RW"
    FR_RE = "FR_RE"
    FR_BL = "FR_BL"
    FR_MF = "FR_MF"
    FR_SN = "FR_SN"
    FR_CH = "FR_CH"
    FR_TG = "FR_TG"
    FR = "FR"
    FF_SN = "FF_SN"
    FF = "FF"
    GL_ES = "GL_ES"
    GL = "GL"
    LG_UG = "LG_UG"
    LG = "LG"
    KA_GE = "KA_GE"
    KA = "KA"
    DE_AT = "DE_AT"
    DE_BE = "DE_BE"
    DE_DE = "DE_DE"
    DE_LI = "DE_LI"
    DE_LU = "DE_LU"
    DE_CH = "DE_CH"
    DE = "DE"
    EL_CY = "EL_CY"
    EL_GR = "EL_GR"
    EL = "EL"
    GU_IN = "GU_IN"
    GU = "GU"
    GUZ_KE = "GUZ_KE"
    GUZ = "GUZ"
    HA_LATN = "HA_LATN"
    HA_LATN_GH = "HA_LATN_GH"
    HA_LATN_NE = "HA_LATN_NE"
    HA_LATN_NG = "HA_LATN_NG"
    HA = "HA"
    HAW_US = "HAW_US"
    HAW = "HAW"
    HE_IL = "HE_IL"
    HE = "HE"
    HI_IN = "HI_IN"
    HI = "HI"
    HU_HU = "HU_HU"
    HU = "HU"
    IS_IS = "IS_IS"
    IS = "IS"
    IG_NG = "IG_NG"
    IG = "IG"
    ID_ID = "ID_ID"
    ID = "ID"
    GA_IE = "GA_IE"
    GA = "GA"
    IT_IT = "IT_IT"
    IT_CH = "IT_CH"
    IT = "IT"
    JA_JP = "JA_JP"
    JA = "JA"
    KEA_CV = "KEA_CV"
    KEA = "KEA"
    KAB_DZ = "KAB_DZ"
    KAB = "KAB"
    KL_GL = "KL_GL"
    KL = "KL"
    KLN_KE = "KLN_KE"
    KLN = "KLN"
    KAM_KE = "KAM_KE"
    KAM = "KAM"
    KN_IN = "KN_IN"
    KN = "KN"
    KK_CYRL = "KK_CYRL"
    KK_CYRL_KZ = "KK_CYRL_KZ"
    KK = "KK"
    KM_KH = "KM_KH"
    KM = "KM"
    KI_KE = "KI_KE"
    KI = "KI"
    RW_RW = "RW_RW"
    RW = "RW"
    KOK_IN = "KOK_IN"
    KOK = "KOK"
    KO_KR = "KO_KR"
    KO = "KO"
    KHQ_ML = "KHQ_ML"
    KHQ = "KHQ"
    SES_ML = "SES_ML"
    SES = "SES"
    LAG_TZ = "LAG_TZ"
    LAG = "LAG"
    LV_LV = "LV_LV"
    LV = "LV"
    LT_LT = "LT_LT"
    LT = "LT"
    LUO_KE = "LUO_KE"
    LUO = "LUO"
    LUY_KE = "LUY_KE"
    LUY = "LUY"
    MK_MK = "MK_MK"
    MK = "MK"
    JMC_TZ = "JMC_TZ"
    JMC = "JMC"
    KDE_TZ = "KDE_TZ"
    KDE = "KDE"
    MG_MG = "MG_MG"
    MG = "MG"
    MS_BN = "MS_BN"
    MS_MY = "MS_MY"
    MS = "MS"
    ML_IN = "ML_IN"
    ML = "ML"
    MT_MT = "MT_MT"
    MT = "MT"
    GV_GB = "GV_GB"
    GV = "GV"
    MR_IN = "MR_IN"
    MR = "MR"
    MAS_KE = "MAS_KE"
    MAS_TZ = "MAS_TZ"
    MAS = "MAS"
    MER_KE = "MER_KE"
    MER = "MER"
    MFE_MU = "MFE_MU"
    MFE = "MFE"
    NAQ_NA = "NAQ_NA"
    NAQ = "NAQ"
    NE_IN = "NE_IN"
    NE_NP = "NE_NP"
    NE = "NE"
    ND_ZW = "ND_ZW"
    ND = "ND"
    NB_NO = "NB_NO"
    NB = "NB"
    NN_NO = "NN_NO"
    NN = "NN"
    NYN_UG = "NYN_UG"
    NYN = "NYN"
    OR_IN = "OR_IN"
    OR = "OR"
    OM_ET = "OM_ET"
    OM_KE = "OM_KE"
    OM = "OM"
    PS_AF = "PS_AF"
    PS = "PS"
    FA_AF = "FA_AF"
    FA_IR = "FA_IR"
    FA = "FA"
    PL_PL = "PL_PL"
    PL = "PL"
    PT_BR = "PT_BR"
    PT_GW = "PT_GW"
    PT_MZ = "PT_MZ"
    PT_PT = "PT_PT"
    PT = "PT"
    PA_ARAB = "PA_ARAB"
    PA_ARAB_PK = "PA_ARAB_PK"
    PA_GURU = "PA_GURU"
    PA_GURU_IN = "PA_GURU_IN"
    PA = "PA"
    RO_MD = "RO_MD"
    RO_RO = "RO_RO"
    RO = "RO"
    RM_CH = "RM_CH"
    RM = "RM"
    ROF_TZ = "ROF_TZ"
    ROF = "ROF"
    RU_MD = "RU_MD"
    RU_RU = "RU_RU"
    RU_UA = "RU_UA"
    RU = "RU"
    RWK_TZ = "RWK_TZ"
    RWK = "RWK"
    SAQ_KE = "SAQ_KE"
    SAQ = "SAQ"
    SG_CF = "SG_CF"
    SG = "SG"
    SEH_MZ = "SEH_MZ"
    SEH = "SEH"
    SR_CYRL = "SR_CYRL"
    SR_CYRL_BA = "SR_CYRL_BA"
    SR_CYRL_ME = "SR_CYRL_ME"
    SR_CYRL_RS = "SR_CYRL_RS"
    SR_LATN = "SR_LATN"
    SR_LATN_BA = "SR_LATN_BA"
    SR_LATN_ME = "SR_LATN_ME"
    SR_LATN_RS = "SR_LATN_RS"
    SR = "SR"
    SN_ZW = "SN_ZW"
    SN = "SN"
    II_CN = "II_CN"
    II = "II"
    SI_LK = "SI_LK"
    SI = "SI"
    SK_SK = "SK_SK"
    SK = "SK"
    SL_SI = "SL_SI"
    SL = "SL"
    XOG_UG = "XOG_UG"
    XOG = "XOG"
    SO_DJ = "SO_DJ"
    SO_ET = "SO_ET"
    SO_KE = "SO_KE"
    SO_SO = "SO_SO"
    SO = "SO"
    ES_AR = "ES_AR"
    ES_BO = "ES_BO"
    ES_CL = "ES_CL"
    ES_CO = "ES_CO"
    ES_CR = "ES_CR"
    ES_DO = "ES_DO"
    ES_EC = "ES_EC"
    ES_SV = "ES_SV"
    ES_GQ = "ES_GQ"
    ES_GT = "ES_GT"
    ES_HN = "ES_HN"
    ES_419 = "ES_419"
    ES_MX = "ES_MX"
    ES_NI = "ES_NI"
    ES_PA = "ES_PA"
    ES_PY = "ES_PY"
    ES_PE = "ES_PE"
    ES_PR = "ES_PR"
    ES_ES = "ES_ES"
    ES_US = "ES_US"
    ES_UY = "ES_UY"
    ES_VE = "ES_VE"
    ES = "ES"
    SW_KE = "SW_KE"
    SW_TZ = "SW_TZ"
    SW = "SW"
    SV_FI = "SV_FI"
    SV_SE = "SV_SE"
    SV = "SV"
    GSW_CH = "GSW_CH"
    GSW = "GSW"
    SHI_LATN = "SHI_LATN"
    SHI_LATN_MA = "SHI_LATN_MA"
    SHI_TFNG = "SHI_TFNG"
    SHI_TFNG_MA = "SHI_TFNG_MA"
    SHI = "SHI"
    DAV_KE = "DAV_KE"
    DAV = "DAV"
    TA_IN = "TA_IN"
    TA_LK = "TA_LK"
    TA = "TA"
    TE_IN = "TE_IN"
    TE = "TE"
    TEO_KE = "TEO_KE"
    TEO_UG = "TEO_UG"
    TEO = "TEO"
    TH_TH = "TH_TH"
    TH = "TH"
    BO_CN = "BO_CN"
    BO_IN = "BO_IN"
    BO = "BO"
    TI_ER = "TI_ER"
    TI_ET = "TI_ET"
    TI = "TI"
    TO_TO = "TO_TO"
    TO = "TO"
    TR_TR = "TR_TR"
    TR = "TR"
    UK_UA = "UK_UA"
    UK = "UK"
    UR_IN = "UR_IN"
    UR_PK = "UR_PK"
    UR = "UR"
    UZ_ARAB = "UZ_ARAB"
    UZ_ARAB_AF = "UZ_ARAB_AF"
    UZ_CYRL = "UZ_CYRL"
    UZ_CYRL_UZ = "UZ_CYRL_UZ"
    UZ_LATN = "UZ_LATN"
    UZ_LATN_UZ = "UZ_LATN_UZ"
    UZ = "UZ"
    VI_VN = "VI_VN"
    VI = "VI"
    VUN_TZ = "VUN_TZ"
    VUN = "VUN"
    CY_GB = "CY_GB"
    CY = "CY"
    YO_NG = "YO_NG"
    YO = "YO"
    ZU_ZA = "ZU_ZA"
    ZU = "ZU"


class Country(str, Enum):
    AF = "AF"
    AX = "AX"
    AL = "AL"
    DZ = "DZ"
    AS = "AS"
    AD = "AD"
    AO = "AO"
    AI = "AI"
    AQ = "AQ"
    AG = "AG"
    AR = "AR"
    AM = "AM"
    AW = "AW"
    AU = "AU"
    AT = "AT"
    AZ = "AZ"
    BS = "BS"
    BH = "BH"
    BD = "BD"
    BB = "BB"
    BY = "BY"
    BE = "BE"
    BZ = "BZ"
    BJ = "BJ"
    BM = "BM"
    BT = "BT"
    BO = "BO"
    BA = "BA"
    BW = "BW"
    BV = "BV"
    BR = "BR"
    IO = "IO"
    BN = "BN"
    BG = "BG"
    BF = "BF"
    BI = "BI"
    KH = "KH"
    CM = "CM"
    CA = "CA"
    CV = "CV"
    KY = "KY"
    CF = "CF"
    TD = "TD"
    CL = "CL"
    CN = "CN"
    CX = "CX"
    CC = "CC"
    CO = "CO"
    KM = "KM"
    CG = "CG"
    CD = "CD"
    CK = "CK"
    CR = "CR"
    CI = "CI"
    HR = "HR"
    CU = "CU"
    CY = "CY"
    CZ = "CZ"
    DK = "DK"
    DJ = "DJ"
    DM = "DM"
    DO = "DO"
    EC = "EC"
    EG = "EG"
    SV = "SV"
    GQ = "GQ"
    ER = "ER"
    EE = "EE"
    ET = "ET"
    FK = "FK"
    FO = "FO"
    FJ = "FJ"
    FI = "FI"
    FR = "FR"
    GF = "GF"
    PF = "PF"
    TF = "TF"
    GA = "GA"
    GM = "GM"
    GE = "GE"
    DE = "DE"
    GH = "GH"
    GI = "GI"
    GR = "GR"
    GL = "GL"
    GD = "GD"
    GP = "GP"
    GU = "GU"
    GT = "GT"
    GG = "GG"
    GN = "GN"
    GW = "GW"
    GY = "GY"
    HT = "HT"
    HM = "HM"
    VA = "VA"
    HN = "HN"
    HK = "HK"
    HU = "HU"
    IS = "IS"
    IN = "IN"
    ID = "ID"
    IR = "IR"
    IQ = "IQ"
    IE = "IE"
    IM = "IM"
    IL = "IL"
    IT = "IT"
    JM = "JM"
    JP = "JP"
    JE = "JE"
    JO = "JO"
    KZ = "KZ"
    KE = "KE"
    KI = "KI"
    KP = "KP"
    KR = "KR"
    XK = "XK"
    KW = "KW"
    KG = "KG"
    LA = "LA"
    LV = "LV"
    LB = "LB"
    LS = "LS"
    LR = "LR"
    LY = "LY"
    LI = "LI"
    LT = "LT"
    LU = "LU"
    MO = "MO"
    MK = "MK"
    MG = "MG"
    MW = "MW"
    MY = "MY"
    MV = "MV"
    ML = "ML"
    MT = "MT"
    MH = "MH"
    MQ = "MQ"
    MR = "MR"
    MU = "MU"
    YT = "YT"
    MX = "MX"
    FM = "FM"
    MD = "MD"
    MC = "MC"
    MN = "MN"
    ME = "ME"
    MS = "MS"
    MA = "MA"
    MZ = "MZ"
    MM = "MM"
    NA = "NA"
    NR = "NR"
    NP = "NP"
    NL = "NL"
    AN = "AN"
    NC = "NC"
    NZ = "NZ"
    NI = "NI"
    NE = "NE"
    NG = "NG"
    NU = "NU"
    NF = "NF"
    MP = "MP"
    NO = "NO"
    OM = "OM"
    PK = "PK"
    PW = "PW"
    PS = "PS"
    PA = "PA"
    PG = "PG"
    PY = "PY"
    PE = "PE"
    PH = "PH"
    PN = "PN"
    PL = "PL"
    PT = "PT"
    PR = "PR"
    QA = "QA"
    RO = "RO"
    RU = "RU"
    RW = "RW"
    RE = "RE"
    BL = "BL"
    SH = "SH"
    KN = "KN"
    LC = "LC"
    MF = "MF"
    PM = "PM"
    VC = "VC"
    WS = "WS"
    SM = "SM"
    ST = "ST"
    SA = "SA"
    SN = "SN"
    RS = "RS"
    SC = "SC"
    SL = "SL"
    SG = "SG"
    SK = "SK"
    SI = "SI"
    SB = "SB"
    SO = "SO"
    ZA = "ZA"
    SS = "SS"
    GS = "GS"
    ES = "ES"
    LK = "LK"
    SD = "SD"
    SR = "SR"
    SJ = "SJ"
    SZ = "SZ"
    SE = "SE"
    CH = "CH"
    SY = "SY"
    TW = "TW"
    TJ = "TJ"
    TZ = "TZ"
    TH = "TH"
    TL = "TL"
    TG = "TG"
    TK = "TK"
    TO = "TO"
    TT = "TT"
    TN = "TN"
    TR = "TR"
    TM = "TM"
    TC = "TC"
    TV = "TV"
    UG = "UG"
    UA = "UA"
    AE = "AE"
    GB = "GB"
    US = "US"
    UY = "UY"
    UZ = "UZ"
    VU = "VU"
    VE = "VE"
    VN = "VN"
    VG = "VG"
    VI = "VI"
    WF = "WF"
    YE = "YE"
    ZM = "ZM"
    ZW = "ZW"


class Language(str, Enum):
    AA = "AA"
    AB = "AB"
    AF = "AF"
    AK = "AK"
    AM = "AM"
    AN = "AN"
    AR = "AR"
    AS = "AS"
    AV = "AV"
    AY = "AY"
    AZ = "AZ"
    BA = "BA"
    BE = "BE"
    BG = "BG"
    BH = "BH"
    BI = "BI"
    BM = "BM"
    BN = "BN"
    BO = "BO"
    BR = "BR"
    BS = "BS"
    CA = "CA"
    CE = "CE"
    CH = "CH"
    CO = "CO"
    CR = "CR"
    CS = "CS"
    CU = "CU"
    CV = "CV"
    CY = "CY"
    DA = "DA"
    DE = "DE"
    DV = "DV"
    DZ = "DZ"
    EE = "EE"
    EL = "EL"
    EN = "EN"
    EO = "EO"
    ES = "ES"
    ET = "ET"
    EU = "EU"
    FA = "FA"
    FF = "FF"
    FI = "FI"
    FJ = "FJ"
    FO = "FO"
    FR = "FR"
    FY = "FY"
    GA = "GA"
    GD = "GD"
    GL = "GL"
    GN = "GN"
    GU = "GU"
    GV = "GV"
    HA = "HA"
    HE = "HE"
    HI = "HI"
    HO = "HO"
    HR = "HR"
    HT = "HT"
    HU = "HU"
    HY = "HY"
    HZ = "HZ"
    IA = "IA"
    ID = "ID"
    IE = "IE"
    IG = "IG"
    II = "II"
    IK = "IK"
    IO = "IO"
    IS = "IS"
    IT = "IT"
    IU = "IU"
    JA = "JA"
    JV = "JV"
    KA = "KA"
    KG = "KG"
    KI = "KI"
    KJ = "KJ"
    KK = "KK"
    KL = "KL"
    KM = "KM"
    KN = "KN"
    KO = "KO"
    KR = "KR"
    KS = "KS"
    KU = "KU"
    KV = "KV"
    KW = "KW"
    KY = "KY"
    LA = "LA"
    LB = "LB"
    LG = "LG"
    LI = "LI"
    LN = "LN"
    LO = "LO"
    LT = "LT"
    LV = "LV"
    MG = "MG"
    MH = "MH"
    MI = "MI"
    MK = "MK"
    ML = "ML"
    MN = "MN"
    MO = "MO"
    MR = "MR"
    MS = "MS"
    MT = "MT"
    MY = "MY"
    NA = "NA"
    ND = "ND"
    NE = "NE"
    NG = "NG"
    NL = "NL"
    NN = "NN"
    NO = "NO"
    NR = "NR"
    NV = "NV"
    NY = "NY"
    OC = "OC"
    OJ = "OJ"
    OM = "OM"
    OR = "OR"
    OS = "OS"
    PA = "PA"
    PI = "PI"
    PL = "PL"
    PS = "PS"
    PT = "PT"
    QU = "QU"
    RM = "RM"
    RN = "RN"
    RO = "RO"
    RU = "RU"
    RW = "RW"
    SA = "SA"
    SC = "SC"
    SD = "SD"
    SE = "SE"
    SG = "SG"
    SH = "SH"
    SI = "SI"
    SK = "SK"
    SL = "SL"
    SM = "SM"
    SN = "SN"
    SO = "SO"
    SQ = "SQ"
    SR = "SR"
    SS = "SS"
    ST = "ST"
    SU = "SU"
    SV = "SV"
    SW = "SW"
    TA = "TA"
    TE = "TE"
    TG = "TG"
    TH = "TH"
    TI = "TI"
    TK = "TK"
    TL = "TL"
    TN = "TN"
    TO = "TO"
    TR = "TR"
    TS = "TS"
    TT = "TT"
    TW = "TW"
    TY = "TY"
    UG = "UG"
    UK = "UK"
    UR = "UR"
    UZ = "UZ"
    VE = "VE"
    VI = "VI"
    VO = "VO"
    WA = "WA"
    WO = "WO"
    XH = "XH"
    YI = "YI"
    YO = "YO"
    ZA = "ZA"
    ZH = "ZH"
    ZU = "ZU"


class Timezone(str, Enum):
    PACIFIC__NIUE = "PACIFIC__NIUE"
    PACIFIC__PAGO_PAGO = "PACIFIC__PAGO_PAGO"
    PACIFIC__HONOLULU = "PACIFIC__HONOLULU"
    PACIFIC__RAROTONGA = "PACIFIC__RAROTONGA"
    PACIFIC__TAHITI = "PACIFIC__TAHITI"
    PACIFIC__MARQUESAS = "PACIFIC__MARQUESAS"
    AMERICA__ANCHORAGE = "AMERICA__ANCHORAGE"
    PACIFIC__GAMBIER = "PACIFIC__GAMBIER"
    AMERICA__LOS_ANGELES = "AMERICA__LOS_ANGELES"
    AMERICA__TIJUANA = "AMERICA__TIJUANA"
    AMERICA__VANCOUVER = "AMERICA__VANCOUVER"
    AMERICA__WHITEHORSE = "AMERICA__WHITEHORSE"
    PACIFIC__PITCAIRN = "PACIFIC__PITCAIRN"
    AMERICA__DENVER = "AMERICA__DENVER"
    AMERICA__PHOENIX = "AMERICA__PHOENIX"
    AMERICA__MAZATLAN = "AMERICA__MAZATLAN"
    AMERICA__DAWSON_CREEK = "AMERICA__DAWSON_CREEK"
    AMERICA__EDMONTON = "AMERICA__EDMONTON"
    AMERICA__HERMOSILLO = "AMERICA__HERMOSILLO"
    AMERICA__YELLOWKNIFE = "AMERICA__YELLOWKNIFE"
    AMERICA__BELIZE = "AMERICA__BELIZE"
    AMERICA__CHICAGO = "AMERICA__CHICAGO"
    AMERICA__MEXICO_CITY = "AMERICA__MEXICO_CITY"
    AMERICA__REGINA = "AMERICA__REGINA"
    AMERICA__TEGUCIGALPA = "AMERICA__TEGUCIGALPA"
    AMERICA__WINNIPEG = "AMERICA__WINNIPEG"
    AMERICA__COSTA_RICA = "AMERICA__COSTA_RICA"
    AMERICA__EL_SALVADOR = "AMERICA__EL_SALVADOR"
    PACIFIC__GALAPAGOS = "PACIFIC__GALAPAGOS"
    AMERICA__GUATEMALA = "AMERICA__GUATEMALA"
    AMERICA__MANAGUA = "AMERICA__MANAGUA"
    AMERICA__CANCUN = "AMERICA__CANCUN"
    AMERICA__BOGOTA = "AMERICA__BOGOTA"
    PACIFIC__EASTER = "PACIFIC__EASTER"
    AMERICA__NEW_YORK = "AMERICA__NEW_YORK"
    AMERICA__IQALUIT = "AMERICA__IQALUIT"
    AMERICA__TORONTO = "AMERICA__TORONTO"
    AMERICA__GUAYAQUIL = "AMERICA__GUAYAQUIL"
    AMERICA__HAVANA = "AMERICA__HAVANA"
    AMERICA__JAMAICA = "AMERICA__JAMAICA"
    AMERICA__LIMA = "AMERICA__LIMA"
    AMERICA__NASSAU = "AMERICA__NASSAU"
    AMERICA__PANAMA = "AMERICA__PANAMA"
    AMERICA__PORT = "AMERICA__PORT"
    AMERICA__RIO_BRANCO = "AMERICA__RIO_BRANCO"
    AMERICA__HALIFAX = "AMERICA__HALIFAX"
    AMERICA__BARBADOS = "AMERICA__BARBADOS"
    ATLANTIC__BERMUDA = "ATLANTIC__BERMUDA"
    AMERICA__BOA_VISTA = "AMERICA__BOA_VISTA"
    AMERICA__CARACAS = "AMERICA__CARACAS"
    AMERICA__CURACAO = "AMERICA__CURACAO"
    AMERICA__GRAND_TURK = "AMERICA__GRAND_TURK"
    AMERICA__GUYANA = "AMERICA__GUYANA"
    AMERICA__LA_PAZ = "AMERICA__LA_PAZ"
    AMERICA__MANAUS = "AMERICA__MANAUS"
    AMERICA__MARTINIQUE = "AMERICA__MARTINIQUE"
    AMERICA__PORT_OF_SPAIN = "AMERICA__PORT_OF_SPAIN"
    AMERICA__PORTO_VELHO = "AMERICA__PORTO_VELHO"
    AMERICA__PUERTO_RICO = "AMERICA__PUERTO_RICO"
    AMERICA__SANTO_DOMINGO = "AMERICA__SANTO_DOMINGO"
    AMERICA__THULE = "AMERICA__THULE"
    AMERICA__ST_JOHNS = "AMERICA__ST_JOHNS"
    AMERICA__ARAGUAINA = "AMERICA__ARAGUAINA"
    AMERICA__ASUNCION = "AMERICA__ASUNCION"
    AMERICA__BELEM = "AMERICA__BELEM"
    AMERICA__ARGENTINA = "AMERICA__ARGENTINA"
    AMERICA__CAMPO_GRANDE = "AMERICA__CAMPO_GRANDE"
    AMERICA__CAYENNE = "AMERICA__CAYENNE"
    AMERICA__CUIABA = "AMERICA__CUIABA"
    AMERICA__FORTALEZA = "AMERICA__FORTALEZA"
    AMERICA__GODTHAB = "AMERICA__GODTHAB"
    AMERICA__MACEIO = "AMERICA__MACEIO"
    AMERICA__MIQUELON = "AMERICA__MIQUELON"
    AMERICA__MONTEVIDEO = "AMERICA__MONTEVIDEO"
    ANTARCTICA__PALMER = "ANTARCTICA__PALMER"
    AMERICA__PARAMARIBO = "AMERICA__PARAMARIBO"
    AMERICA__PUNTA_ARENAS = "AMERICA__PUNTA_ARENAS"
    AMERICA__RECIFE = "AMERICA__RECIFE"
    ANTARCTICA__ROTHERA = "ANTARCTICA__ROTHERA"
    AMERICA__BAHIA = "AMERICA__BAHIA"
    AMERICA__SANTIAGO = "AMERICA__SANTIAGO"
    ATLANTIC__STANLEY = "ATLANTIC__STANLEY"
    AMERICA__NORONHA = "AMERICA__NORONHA"
    AMERICA__SAO_PAULO = "AMERICA__SAO_PAULO"
    ATLANTIC__SOUTH_GEORGIA = "ATLANTIC__SOUTH_GEORGIA"
    ATLANTIC__AZORES = "ATLANTIC__AZORES"
    ATLANTIC__CAPE_VERDE = "ATLANTIC__CAPE_VERDE"
    AMERICA__SCORESBYSUND = "AMERICA__SCORESBYSUND"
    AFRICA__ABIDJAN = "AFRICA__ABIDJAN"
    AFRICA__ACCRA = "AFRICA__ACCRA"
    AFRICA__BISSAU = "AFRICA__BISSAU"
    ATLANTIC__CANARY = "ATLANTIC__CANARY"
    AFRICA__CASABLANCA = "AFRICA__CASABLANCA"
    AMERICA__DANMARKSHAVN = "AMERICA__DANMARKSHAVN"
    EUROPE__DUBLIN = "EUROPE__DUBLIN"
    AFRICA__EL_AAIUN = "AFRICA__EL_AAIUN"
    ATLANTIC__FAROE = "ATLANTIC__FAROE"
    ETC__GMT = "ETC__GMT"
    EUROPE__LISBON = "EUROPE__LISBON"
    EUROPE__LONDON = "EUROPE__LONDON"
    AFRICA__MONROVIA = "AFRICA__MONROVIA"
    ATLANTIC__REYKJAVIK = "ATLANTIC__REYKJAVIK"
    AFRICA__ALGIERS = "AFRICA__ALGIERS"
    EUROPE__AMSTERDAM = "EUROPE__AMSTERDAM"
    EUROPE__ANDORRA = "EUROPE__ANDORRA"
    EUROPE__BERLIN = "EUROPE__BERLIN"
    EUROPE__BRUSSELS = "EUROPE__BRUSSELS"
    EUROPE__BUDAPEST = "EUROPE__BUDAPEST"
    EUROPE__BELGRADE = "EUROPE__BELGRADE"
    EUROPE__PRAGUE = "EUROPE__PRAGUE"
    AFRICA__CEUTA = "AFRICA__CEUTA"
    EUROPE__COPENHAGEN = "EUROPE__COPENHAGEN"
    EUROPE__GIBRALTAR = "EUROPE__GIBRALTAR"
    AFRICA__LAGOS = "AFRICA__LAGOS"
    EUROPE__LUXEMBOURG = "EUROPE__LUXEMBOURG"
    EUROPE__MADRID = "EUROPE__MADRID"
    EUROPE__MALTA = "EUROPE__MALTA"
    EUROPE__MONACO = "EUROPE__MONACO"
    AFRICA__NDJAMENA = "AFRICA__NDJAMENA"
    EUROPE__OSLO = "EUROPE__OSLO"
    EUROPE__PARIS = "EUROPE__PARIS"
    EUROPE__ROME = "EUROPE__ROME"
    EUROPE__STOCKHOLM = "EUROPE__STOCKHOLM"
    EUROPE__TIRANE = "EUROPE__TIRANE"
    AFRICA__TUNIS = "AFRICA__TUNIS"
    EUROPE__VIENNA = "EUROPE__VIENNA"
    EUROPE__WARSAW = "EUROPE__WARSAW"
    EUROPE__ZURICH = "EUROPE__ZURICH"
    ASIA__AMMAN = "ASIA__AMMAN"
    EUROPE__ATHENS = "EUROPE__ATHENS"
    ASIA__BEIRUT = "ASIA__BEIRUT"
    EUROPE__BUCHAREST = "EUROPE__BUCHAREST"
    AFRICA__CAIRO = "AFRICA__CAIRO"
    EUROPE__CHISINAU = "EUROPE__CHISINAU"
    ASIA__DAMASCUS = "ASIA__DAMASCUS"
    ASIA__GAZA = "ASIA__GAZA"
    EUROPE__HELSINKI = "EUROPE__HELSINKI"
    ASIA__JERUSALEM = "ASIA__JERUSALEM"
    AFRICA__JOHANNESBURG = "AFRICA__JOHANNESBURG"
    AFRICA__KHARTOUM = "AFRICA__KHARTOUM"
    EUROPE__KIEV = "EUROPE__KIEV"
    AFRICA__MAPUTO = "AFRICA__MAPUTO"
    EUROPE__KALININGRAD = "EUROPE__KALININGRAD"
    ASIA__NICOSIA = "ASIA__NICOSIA"
    EUROPE__RIGA = "EUROPE__RIGA"
    EUROPE__SOFIA = "EUROPE__SOFIA"
    EUROPE__TALLINN = "EUROPE__TALLINN"
    AFRICA__TRIPOLI = "AFRICA__TRIPOLI"
    EUROPE__VILNIUS = "EUROPE__VILNIUS"
    AFRICA__WINDHOEK = "AFRICA__WINDHOEK"
    ASIA__BAGHDAD = "ASIA__BAGHDAD"
    EUROPE__ISTANBUL = "EUROPE__ISTANBUL"
    EUROPE__MINSK = "EUROPE__MINSK"
    EUROPE__MOSCOW = "EUROPE__MOSCOW"
    AFRICA__NAIROBI = "AFRICA__NAIROBI"
    ASIA__QATAR = "ASIA__QATAR"
    ASIA__RIYADH = "ASIA__RIYADH"
    ANTARCTICA__SYOWA = "ANTARCTICA__SYOWA"
    ASIA__TEHRAN = "ASIA__TEHRAN"
    ASIA__BAKU = "ASIA__BAKU"
    ASIA__DUBAI = "ASIA__DUBAI"
    INDIAN__MAHE = "INDIAN__MAHE"
    INDIAN__MAURITIUS = "INDIAN__MAURITIUS"
    EUROPE__SAMARA = "EUROPE__SAMARA"
    INDIAN__REUNION = "INDIAN__REUNION"
    ASIA__TBILISI = "ASIA__TBILISI"
    ASIA__YEREVAN = "ASIA__YEREVAN"
    ASIA__KABUL = "ASIA__KABUL"
    ASIA__AQTAU = "ASIA__AQTAU"
    ASIA__AQTOBE = "ASIA__AQTOBE"
    ASIA__ASHGABAT = "ASIA__ASHGABAT"
    ASIA__DUSHANBE = "ASIA__DUSHANBE"
    ASIA__KARACHI = "ASIA__KARACHI"
    INDIAN__KERGUELEN = "INDIAN__KERGUELEN"
    INDIAN__MALDIVES = "INDIAN__MALDIVES"
    ANTARCTICA__MAWSON = "ANTARCTICA__MAWSON"
    ASIA__YEKATERINBURG = "ASIA__YEKATERINBURG"
    ASIA__TASHKENT = "ASIA__TASHKENT"
    ASIA__COLOMBO = "ASIA__COLOMBO"
    ASIA__KOLKATA = "ASIA__KOLKATA"
    ASIA__KATHMANDU = "ASIA__KATHMANDU"
    ASIA__ALMATY = "ASIA__ALMATY"
    ASIA__BISHKEK = "ASIA__BISHKEK"
    INDIAN__CHAGOS = "INDIAN__CHAGOS"
    ASIA__DHAKA = "ASIA__DHAKA"
    ASIA__OMSK = "ASIA__OMSK"
    ASIA__THIMPHU = "ASIA__THIMPHU"
    ANTARCTICA__VOSTOK = "ANTARCTICA__VOSTOK"
    INDIAN__COCOS = "INDIAN__COCOS"
    ASIA__YANGON = "ASIA__YANGON"
    ASIA__BANGKOK = "ASIA__BANGKOK"
    INDIAN__CHRISTMAS = "INDIAN__CHRISTMAS"
    ANTARCTICA__DAVIS = "ANTARCTICA__DAVIS"
    ASIA__SAIGON = "ASIA__SAIGON"
    ASIA__HOVD = "ASIA__HOVD"
    ASIA__JAKARTA = "ASIA__JAKARTA"
    ASIA__KRASNOYARSK = "ASIA__KRASNOYARSK"
    ASIA__BRUNEI = "ASIA__BRUNEI"
    ASIA__SHANGHAI = "ASIA__SHANGHAI"
    ASIA__CHOIBALSAN = "ASIA__CHOIBALSAN"
    ASIA__HONG_KONG = "ASIA__HONG_KONG"
    ASIA__KUALA_LUMPUR = "ASIA__KUALA_LUMPUR"
    ASIA__MACAU = "ASIA__MACAU"
    ASIA__MAKASSAR = "ASIA__MAKASSAR"
    ASIA__MANILA = "ASIA__MANILA"
    ASIA__IRKUTSK = "ASIA__IRKUTSK"
    ASIA__SINGAPORE = "ASIA__SINGAPORE"
    ASIA__TAIPEI = "ASIA__TAIPEI"
    ASIA__ULAANBAATAR = "ASIA__ULAANBAATAR"
    AUSTRALIA__PERTH = "AUSTRALIA__PERTH"
    ASIA__PYONGYANG = "ASIA__PYONGYANG"
    ASIA__DILI = "ASIA__DILI"
    ASIA__JAYAPURA = "ASIA__JAYAPURA"
    ASIA__YAKUTSK = "ASIA__YAKUTSK"
    PACIFIC__PALAU = "PACIFIC__PALAU"
    ASIA__SEOUL = "ASIA__SEOUL"
    ASIA__TOKYO = "ASIA__TOKYO"
    AUSTRALIA__DARWIN = "AUSTRALIA__DARWIN"
    ANTARCTICA__DUMONTDURVILLE = "ANTARCTICA__DUMONTDURVILLE"
    AUSTRALIA__BRISBANE = "AUSTRALIA__BRISBANE"
    PACIFIC__GUAM = "PACIFIC__GUAM"
    ASIA__VLADIVOSTOK = "ASIA__VLADIVOSTOK"
    PACIFIC__PORT_MORESBY = "PACIFIC__PORT_MORESBY"
    PACIFIC__CHUUK = "PACIFIC__CHUUK"
    AUSTRALIA__ADELAIDE = "AUSTRALIA__ADELAIDE"
    ANTARCTICA__CASEY = "ANTARCTICA__CASEY"
    AUSTRALIA__HOBART = "AUSTRALIA__HOBART"
    AUSTRALIA__SYDNEY = "AUSTRALIA__SYDNEY"
    PACIFIC__EFATE = "PACIFIC__EFATE"
    PACIFIC__GUADALCANAL = "PACIFIC__GUADALCANAL"
    PACIFIC__KOSRAE = "PACIFIC__KOSRAE"
    ASIA__MAGADAN = "ASIA__MAGADAN"
    PACIFIC__NORFOLK = "PACIFIC__NORFOLK"
    PACIFIC__NOUMEA = "PACIFIC__NOUMEA"
    PACIFIC__POHNPEI = "PACIFIC__POHNPEI"
    PACIFIC__FUNAFUTI = "PACIFIC__FUNAFUTI"
    PACIFIC__KWAJALEIN = "PACIFIC__KWAJALEIN"
    PACIFIC__MAJURO = "PACIFIC__MAJURO"
    ASIA__KAMCHATKA = "ASIA__KAMCHATKA"
    PACIFIC__NAURU = "PACIFIC__NAURU"
    PACIFIC__TARAWA = "PACIFIC__TARAWA"
    PACIFIC__WAKE = "PACIFIC__WAKE"
    PACIFIC__WALLIS = "PACIFIC__WALLIS"
    PACIFIC__AUCKLAND = "PACIFIC__AUCKLAND"
    PACIFIC__ENDERBURY = "PACIFIC__ENDERBURY"
    PACIFIC__FAKAOFO = "PACIFIC__FAKAOFO"
    PACIFIC__FIJI = "PACIFIC__FIJI"
    PACIFIC__TONGATAPU = "PACIFIC__TONGATAPU"
    PACIFIC__APIA = "PACIFIC__APIA"
    PACIFIC__KIRITIMATI = "PACIFIC__KIRITIMATI"


JSON = Any
Date = Any
BigInt = Any


class Pong(TypedDict, total=False):
    _id: Optional["str"]
    name: Optional["str"]


class Subscription(TypedDict, total=False):
    onPing: Optional["Pong"]
    onCollectionCreated: Optional["Collection"]
    onCollectionUpdated: Optional["Collection"]
    onCollectionDeleted: Optional["Collection"]
    onContentCreated: Optional["Content"]
    onContentUpdated: Optional["Content"]
    onContentDeleted: Optional["Content"]
    onStateSaved: Optional["State"]
    onStateDeleted: Optional["State"]


class Mutation(TypedDict, total=False):
    ping: Optional["Pong"]
    _enableAccount: Optional["Account"]
    _disableAccount: Optional["Account"]
    _updateAccount: Optional["Account"]
    _updateSuperRoles: Optional["Account"]
    _createSuperAccount: Optional["Account"]
    _createAPIAccount: Optional["Account"]
    _createAPIKey: Optional["APIKey"]
    _deleteAPIKey: Optional["SimpleResponse"]
    _updateAPIKey: Optional["APIKey"]
    _invalidateCache: Optional["SimpleResponse"]
    generateId: Optional["SimpleSession"]
    login: Optional["Session"]
    loginWith2FAT: Optional["Session"]
    loginWith2FAST: Optional["Session"]
    loginWithToken: Optional["Session"]
    loginWithMagic: Optional["Session"]
    createAccount: Optional["Session"]
    setPassword: Optional["Session"]
    resetPassword: Optional["SimpleResponse"]
    checkEmail: Optional["SimpleSession"]
    checkHandle: Optional["HandleCheckResponse"]
    verifyEmail: Optional["Session"]
    sendVerificationEmail: Optional["SimpleResponse"]
    sendMagicLink: Optional["SimpleResponse"]
    generateMagicLink: Optional["SimpleSession"]
    send2FAToken: Optional["SimpleResponse"]
    connectWithService: Optional["Session"]
    isServiceConnected: Optional["SimpleSession"]
    getServiceAuthUrl: Optional["SimpleSession"]
    updateAccount: Optional["Account"]
    claimId: Optional["SimpleResponse"]
    logout: Optional["SimpleSession"]
    changePassword: Optional["Session"]
    deactivateAccount: Optional["SimpleResponse"]
    deleteAccount: Optional["SimpleResponse"]
    registerTargets: Optional["SimpleResponse"]
    _enableCollection: Optional["Collection"]
    _disableCollection: Optional["Collection"]
    _createCollection: Optional["Collection"]
    _updateCollection: Optional["Collection"]
    _deleteCollection: Optional["SimpleResponse"]
    createCollection: Optional["Collection"]
    updateCollection: Optional["Collection"]
    deleteCollection: Optional["SimpleResponse"]
    addContentToCollection: Optional["Collection"]
    removeContentFromCollection: Optional["Collection"]
    _enableContent: Optional["Content"]
    _disableContent: Optional["Content"]
    _createContent: Optional["Content"]
    _updateContent: Optional["Content"]
    createContent: Optional["Content"]
    updateContent: Optional["Content"]
    deleteContent: Optional["SimpleResponse"]
    _saveDevice: Optional["Device"]
    _updateDevice: Optional["Device"]
    _deleteDevice: Optional["SimpleResponse"]
    saveDevice: Optional["Device"]
    updateDevice: Optional["Device"]
    deleteDevice: Optional["SimpleResponse"]
    createInterest: Optional["Interest"]
    deleteInterest: Optional["SimpleResponse"]
    registerLocation: Optional["Location"]
    deleteAllLocations: Optional["SimpleResponse"]
    createLog: Optional["SimpleResponse"]
    _uploadMedia: Optional["Media"]
    _createMedia: Optional["Media"]
    _updateMedia: Optional["Media"]
    createMedia: Optional["Media"]
    updateMedia: Optional["Media"]
    _createMeta: Optional["Meta"]
    _updateMeta: Optional["Meta"]
    _disableMeta: Optional["Meta"]
    _enableMeta: Optional["Meta"]
    _mergeMetas: Optional["Meta"]
    createMeta: Optional["MetaList"]
    _enablePrompt: Optional["Prompt"]
    _disablePrompt: Optional["Prompt"]
    _createPrompt: Optional["Prompt"]
    _updatePrompt: Optional["Prompt"]
    createPrompt: Optional["Prompt"]
    updatePrompt: Optional["Prompt"]
    deletePrompt: Optional["SimpleResponse"]
    runPrompt: Optional["PromptMessage"]
    saveReaction: Optional["Reaction"]
    saveState: Optional["State"]
    _enableTarget: Optional["Target"]
    _disableTarget: Optional["Target"]
    _createTarget: Optional["Target"]
    _updateTarget: Optional["Target"]
    setup: Optional["SetupResponse"]
    upload: Optional["File"]
    signUpload: Optional["FileAuthorization"]


class Query(TypedDict, total=False):
    info: Optional["Info"]
    account: Optional["Account"]
    _account: Optional["Account"]
    _accounts: Optional["AccountList"]
    _apiKeys: Optional["None"]
    _apiEndpoints: Optional["None"]
    _gqlOperations: Optional["None"]
    _collection: Optional["Collection"]
    _collections: Optional["CollectionList"]
    collections: Optional["CollectionList"]
    collection: Optional["Collection"]
    publicCollections: Optional["CollectionList"]
    publicCollection: Optional["Collection"]
    _content: Optional["Content"]
    _contents: Optional["ContentList"]
    contents: Optional["ContentList"]
    content: Optional["Content"]
    likedContents: Optional["ContentList"]
    recentlyViewedContents: Optional["ContentList"]
    interestedContents: Optional["ContentList"]
    publicContents: Optional["ContentList"]
    publicContent: Optional["Content"]
    _device: Optional["Device"]
    _devices: Optional["DeviceList"]
    devices: Optional["DeviceList"]
    device: Optional["Device"]
    _insights: Optional["InsightList"]
    insights: Optional["InsightList"]
    _interest: Optional["Interest"]
    _interests: Optional["InterestList"]
    interest: Optional["Interest"]
    interests: Optional["InterestList"]
    _location: Optional["Location"]
    _locations: Optional["LocationList"]
    locations: Optional["LocationList"]
    location: Optional["Location"]
    _log: Optional["Log"]
    _logs: Optional["LogList"]
    logs: Optional["LogList"]
    _media: Optional["Media"]
    _medias: Optional["MediaList"]
    media: Optional["Media"]
    medias: Optional["MediaList"]
    publicMeta: Optional["Meta"]
    publicMetas: Optional["MetaList"]
    _meta: Optional["Meta"]
    _metas: Optional["MetaList"]
    _prompt: Optional["Prompt"]
    _prompts: Optional["PromptList"]
    prompts: Optional["PromptList"]
    prompt: Optional["Prompt"]
    publicPrompts: Optional["PromptList"]
    publicPrompt: Optional["Prompt"]
    reaction: Optional["Reaction"]
    reactions: Optional["ReactionList"]
    publicReactions: Optional["ReactionList"]
    _state: Optional["State"]
    _states: Optional["StateList"]
    states: Optional["StateList"]
    state: Optional["State"]
    _target: Optional["Target"]
    _targets: Optional["TargetList"]
    publicTarget: Optional["Target"]
    publicTargets: Optional["TargetList"]


class Version(TypedDict, total=False):
    key: Optional["str"]
    min: Optional["str"]
    max: Optional["str"]


class Info(TypedDict, total=False):
    name: Optional["str"]
    version: Optional["str"]
    supportedClients: Optional["None"]
    ip: Optional["str"]
    host: Optional["str"]
    userAgent: Optional["str"]
    locale: Optional["str"]
    stage: Optional["str"]
    translations: Optional["Any"]
    supported: Optional["bool"]
    operational: Optional["bool"]


class SuperRole(str, Enum):
    MASTER = "MASTER"
    MANAGER = "MANAGER"
    OBSERVER = "OBSERVER"
    ANALYTICS = "ANALYTICS"
    FINANCE = "FINANCE"
    LOGOBSERVER = "LOGOBSERVER"
    ACCOUNTOBSERVER = "ACCOUNTOBSERVER"
    ACCOUNTMANAGER = "ACCOUNTMANAGER"
    COLLECTIONOBSERVER = "COLLECTIONOBSERVER"
    COLLECTIONMANAGER = "COLLECTIONMANAGER"
    CONTENTOBSERVER = "CONTENTOBSERVER"
    CONTENTMANAGER = "CONTENTMANAGER"
    TARGETOBSERVER = "TARGETOBSERVER"
    TARGETMANAGER = "TARGETMANAGER"
    TARGETOWNER = "TARGETOWNER"
    PROMPTOBSERVER = "PROMPTOBSERVER"
    PROMPTMANAGER = "PROMPTMANAGER"
    STATEOBSERVER = "STATEOBSERVER"
    STATEMANAGER = "STATEMANAGER"
    DEVICEOBSERVER = "DEVICEOBSERVER"
    DEVICEMANAGER = "DEVICEMANAGER"
    LOCATIONOBSERVER = "LOCATIONOBSERVER"
    METAOBSERVER = "METAOBSERVER"
    METAMANAGER = "METAMANAGER"


class LoginMethod(str, Enum):
    PASSWORD = "PASSWORD"
    GOOGLE = "GOOGLE"
    FACEBOOK = "FACEBOOK"
    APPLE = "APPLE"
    LINKEDIN = "LINKEDIN"
    TRUID = "TRUID"


class AccountType(str, Enum):
    SUPER = "SUPER"
    USER = "USER"
    GUEST = "GUEST"
    API = "API"


class APIKeyType(str, Enum):
    SECRET = "SECRET"
    PUBLIC = "PUBLIC"


class Session(TypedDict, total=False):
    token: Optional["None"]
    account: Optional["Account"]


class SimpleSession(TypedDict, total=False):
    token: Optional["str"]
    _id: Optional["str"]
    name: Optional["str"]
    url: Optional["str"]
    type: Optional["AccountType"]


class ServiceInput(TypedDict, total=False):
    name: Optional["None"]
    _id: Optional["str"]
    token: Optional["str"]


class SimpleAccount(TypedDict, total=False):
    _id: Optional["str"]
    type: Optional["AccountType"]
    profile: Optional["AccountProfile"]
    createdAt: Optional["date"]


class APIScopeEndpoint(TypedDict, total=False):
    _id: Optional["str"]
    path: Optional["str"]


class APIScopeOperation(TypedDict, total=False):
    _id: Optional["str"]
    name: Optional["str"]


class APIKey(TypedDict, total=False):
    _id: Optional["str"]
    type: Optional["APIKeyType"]
    token: Optional["str"]
    scope: Optional["APIScope"]
    name: Optional["str"]
    description: Optional["str"]
    account: Optional["SimpleAccount"]
    createdAt: Optional["date"]


class APIScopeImpersonation(TypedDict, total=False):
    services: Optional["None"]
    requireToken: Optional["bool"]


class APIScope(TypedDict, total=False):
    targets: Optional["None"]
    endpoints: Optional["None"]
    operations: Optional["None"]
    impersonation: Optional["APIScopeImpersonation"]


class APIScopeEndpointInput(TypedDict, total=False):
    _id: Optional["str"]
    path: Optional["str"]


class APIScopeOperationInput(TypedDict, total=False):
    _id: Optional["str"]
    name: Optional["str"]


class APIScopeImpersonationInput(TypedDict, total=False):
    services: Optional["None"]
    requireToken: Optional["bool"]


class APIScopeInput(TypedDict, total=False):
    targets: Optional["None"]
    endpoints: Optional["None"]
    operations: Optional["None"]
    impersonation: Optional["APIScopeImpersonationInput"]


class Account(TypedDict, total=False):
    _id: Optional["str"]
    type: Optional["AccountType"]
    emails: Optional["None"]
    profile: Optional["AccountProfile"]
    settings: Optional["AccountSettings"]
    loginMethods: Optional["None"]
    createdAt: Optional["date"]
    updatedAt: Optional["date"]
    passwordUpdatedAt: Optional["date"]
    deactivatedAt: Optional["date"]
    disabled: Optional["bool"]
    disableReason: Optional["str"]
    super: Optional["None"]
    targets: Optional["None"]
    features: Optional["None"]
    availableTargets: Optional["None"]
    lastKnownLocation: Optional["GeoLocation"]


class AccountProfile(TypedDict, total=False):
    _id: Optional["str"]
    handle: Optional["str"]
    email: Optional["str"]
    firstName: Optional["str"]
    lastName: Optional["str"]
    name: Optional["str"]
    timezone: Optional["Timezone"]
    city: Optional["str"]
    country: Optional["Country"]
    picture: Optional["File"]
    order: Optional["int"]
    bio: Optional["str"]


class AccountProfileInput(TypedDict, total=False):
    handle: Optional["str"]
    email: Optional["str"]
    firstName: Optional["str"]
    lastName: Optional["str"]
    name: Optional["str"]
    timezone: Optional["Timezone"]
    city: Optional["str"]
    country: Optional["Country"]
    picture: Optional["FileInput"]
    bio: Optional["str"]


class AccountListFilter(TypedDict, total=False):
    _id: Optional["None"]
    keyword: Optional["str"]
    createdAt: Optional["DateRange"]
    exclude: Optional["None"]
    types: Optional["None"]


class AccountListSort(TypedDict, total=False):
    key: Optional["str"]
    order: Optional["int"]


class AccountListFilterInput(TypedDict, total=False):
    _id: Optional["None"]
    keyword: Optional["str"]
    createdAt: Optional["DateRangeInput"]
    exclude: Optional["None"]
    types: Optional["None"]


class AccountListSortInput(TypedDict, total=False):
    key: Optional["None"]
    order: Optional["None"]


class AccountList(TypedDict, total=False):
    items: Optional["None"]
    limit: Optional["int"]
    skip: Optional["int"]
    count: Optional["int"]
    sort: Optional["None"]
    filters: Optional["AccountListFilter"]
    queryStartedAt: Optional["date"]
    queryEndedAt: Optional["date"]
    duration: Optional["float"]
    _id: Optional["str"]


class Email(TypedDict, total=False):
    address: Optional["None"]
    verified: Optional["bool"]
    primary: Optional["bool"]


class EmailLite(TypedDict, total=False):
    address: Optional["None"]
    primary: Optional["bool"]


class CommunicationSettings(TypedDict, total=False):
    promotional: Optional["bool"]
    transactional: Optional["bool"]


class CommunicationSettingsInput(TypedDict, total=False):
    promotional: Optional["bool"]
    transactional: Optional["bool"]


class AccountSettings(TypedDict, total=False):
    timezone: Optional["Timezone"]
    locale: Optional["Locale"]
    currency: Optional["Currency"]
    email: Optional["CommunicationSettings"]
    sms: Optional["CommunicationSettings"]
    notification: Optional["CommunicationSettings"]
    theme: Optional["str"]


class AccountSettingsInput(TypedDict, total=False):
    locale: Optional["Locale"]
    currency: Optional["Currency"]
    timezone: Optional["Timezone"]
    email: Optional["CommunicationSettingsInput"]
    sms: Optional["CommunicationSettingsInput"]
    notification: Optional["CommunicationSettingsInput"]
    theme: Optional["str"]


class EmailInput(TypedDict, total=False):
    address: Optional["None"]
    primary: Optional["bool"]
    verified: Optional["bool"]


class HandleCheckResponse(TypedDict, total=False):
    isAvailable: Optional["bool"]


class Collection(TypedDict, total=False):
    _id: Optional["str"]
    title: Optional["MLString"]
    description: Optional["MLString"]
    picture: Optional["MLFile"]
    color: Optional["str"]
    location: Optional["GeoLocation"]
    targets: Optional["None"]
    tags: Optional["None"]
    showcase: Optional["None"]
    contents: Optional["None"]
    publishedAt: Optional["date"]
    publishedUntil: Optional["date"]
    published: Optional["bool"]
    disabled: Optional["bool"]
    disableReason: Optional["str"]
    disabledAt: Optional["date"]
    createdBy: Optional["SimpleAccount"]
    updatedBy: Optional["SimpleAccount"]
    createdAt: Optional["date"]
    updatedAt: Optional["date"]
    version: Optional["int"]


class CollectionInput(TypedDict, total=False):
    title: Optional["MLStringInput"]
    description: Optional["MLStringInput"]
    picture: Optional["MLFileInput"]
    color: Optional["str"]
    location: Optional["GeoLocationInput"]
    contents: Optional["None"]
    targets: Optional["None"]
    tags: Optional["None"]
    publishedAt: Optional["date"]
    publishedUntil: Optional["date"]
    published: Optional["bool"]


class CollectionListFilter(TypedDict, total=False):
    _id: Optional["None"]
    keyword: Optional["str"]
    promptId: Optional["str"]
    targets: Optional["None"]
    tags: Optional["None"]
    createdAt: Optional["DateRange"]
    exclude: Optional["None"]
    accountId: Optional["str"]
    custom: Optional["str"]
    contentId: Optional["str"]


class CollectionListSort(TypedDict, total=False):
    key: Optional["str"]
    order: Optional["int"]


class CollectionListFilterInput(TypedDict, total=False):
    _id: Optional["None"]
    keyword: Optional["str"]
    promptId: Optional["str"]
    targets: Optional["None"]
    tags: Optional["None"]
    createdAt: Optional["DateRangeInput"]
    exclude: Optional["None"]
    accountId: Optional["str"]
    custom: Optional["str"]
    contentId: Optional["str"]


class CollectionListSortInput(TypedDict, total=False):
    key: Optional["None"]
    order: Optional["None"]


class CollectionList(TypedDict, total=False):
    items: Optional["None"]
    limit: Optional["int"]
    skip: Optional["int"]
    count: Optional["int"]
    sort: Optional["None"]
    filters: Optional["CollectionListFilter"]
    queryStartedAt: Optional["date"]
    queryEndedAt: Optional["date"]
    duration: Optional["float"]
    _id: Optional["str"]


class ContentStatus(str, Enum):
    FAILED = "FAILED"
    PROCESSING = "PROCESSING"
    READY = "READY"


class ContentFieldType(str, Enum):
    TEXT = "TEXT"
    NUMBER = "NUMBER"
    BOOLEAN = "BOOLEAN"
    SELECTION = "SELECTION"


class ContentBlockType(str, Enum):
    GENERIC = "GENERIC"
    STACK = "STACK"


class ContentBlockAppearance(str, Enum):
    GRID = "GRID"
    HORIZONTAL = "HORIZONTAL"
    VERTICAL = "VERTICAL"


class ContentCredit(TypedDict, total=False):
    _id: Optional["str"]
    subject: Optional["Meta"]
    role: Optional["Meta"]
    primary: Optional["bool"]


class ContentCreditInput(TypedDict, total=False):
    _id: Optional["str"]
    subject: Optional["str"]
    role: Optional["str"]
    primary: Optional["bool"]


class ContentField(TypedDict, total=False):
    _id: Optional["str"]
    label: Optional["MLString"]
    key: Optional["str"]
    defaultValue: Optional["Any"]
    type: Optional["ContentFieldType"]
    min: Optional["int"]
    max: Optional["int"]


class ContentFieldInput(TypedDict, total=False):
    _id: Optional["str"]
    label: Optional["MLStringInput"]
    key: Optional["str"]
    defaultValue: Optional["Any"]
    type: Optional["ContentFieldType"]
    min: Optional["int"]
    max: Optional["int"]


class ContentAsset(TypedDict, total=False):
    _id: Optional["str"]
    title: Optional["MLString"]
    description: Optional["MLString"]
    key: Optional["str"]
    file: Optional["File"]
    tags: Optional["None"]
    version: Optional["str"]
    maxVersion: Optional["str"]
    minVersion: Optional["str"]


class ContentAssetInput(TypedDict, total=False):
    _id: Optional["str"]
    title: Optional["MLStringInput"]
    description: Optional["MLStringInput"]
    key: Optional["str"]
    file: Optional["FileInput"]
    tags: Optional["None"]
    version: Optional["str"]
    maxVersion: Optional["str"]
    minVersion: Optional["str"]


class ContentSourceQuery(TypedDict, total=False):
    filters: Optional["ContentSourceFilter"]
    sort: Optional["None"]


class ContentSourceQueryInput(TypedDict, total=False):
    filters: Optional["ContentSourceFilterInput"]
    sort: Optional["None"]


class ContentSourceFilter(TypedDict, total=False):
    keyword: Optional["str"]
    promptId: Optional["str"]
    targets: Optional["None"]
    tags: Optional["None"]
    interested: Optional["bool"]
    recently: Optional["bool"]
    liked: Optional["bool"]
    random: Optional["bool"]


class ContentSourceFilterInput(TypedDict, total=False):
    keyword: Optional["str"]
    promptId: Optional["str"]
    targets: Optional["None"]
    tags: Optional["None"]
    interested: Optional["bool"]
    recently: Optional["bool"]
    liked: Optional["bool"]
    random: Optional["bool"]


class ContentSource(TypedDict, total=False):
    _id: Optional["str"]
    title: Optional["MLString"]
    description: Optional["MLString"]
    key: Optional["str"]
    picture: Optional["MLFile"]
    color: Optional["str"]
    contents: Optional["None"]
    query: Optional["ContentSourceQuery"]


class ContentSourceInput(TypedDict, total=False):
    _id: Optional["str"]
    title: Optional["MLStringInput"]
    description: Optional["MLStringInput"]
    key: Optional["str"]
    picture: Optional["MLFileInput"]
    color: Optional["str"]
    contents: Optional["None"]
    query: Optional["ContentSourceQueryInput"]


class ContentVariant(TypedDict, total=False):
    _id: Optional["str"]
    title: Optional["MLString"]
    description: Optional["MLString"]
    key: Optional["str"]
    picture: Optional["MLFile"]
    color: Optional["str"]
    assets: Optional["None"]
    tags: Optional["None"]
    disabled: Optional["bool"]
    payload: Optional["Any"]
    sources: Optional["None"]
    fields: Optional["None"]


class ContentVariantInput(TypedDict, total=False):
    _id: Optional["str"]
    title: Optional["MLStringInput"]
    description: Optional["MLStringInput"]
    key: Optional["str"]
    picture: Optional["MLFileInput"]
    color: Optional["str"]
    assets: Optional["None"]
    tags: Optional["None"]
    payload: Optional["Any"]
    sources: Optional["None"]
    fields: Optional["None"]


class ContentAction(TypedDict, total=False):
    _id: Optional["str"]
    key: Optional["str"]
    label: Optional["MLString"]
    url: Optional["str"]
    content: Optional["Content"]


class ContentNodeAsset(TypedDict, total=False):
    _id: Optional["str"]
    key: Optional["str"]
    file: Optional["MLFile"]
    caption: Optional["MLString"]
    alt: Optional["MLString"]


class ContentNode(TypedDict, total=False):
    _id: Optional["str"]
    key: Optional["str"]
    title: Optional["MLString"]
    subtitle: Optional["MLString"]
    body: Optional["MLString"]
    date: Optional["date"]
    assets: Optional["None"]
    resources: Optional["None"]
    actions: Optional["None"]
    url: Optional["str"]
    meta: Optional["Meta"]
    content: Optional["Content"]
    collection: Optional["Collection"]
    prompt: Optional["Prompt"]
    sort: Optional["int"]


class ContentBlock(TypedDict, total=False):
    _id: Optional["str"]
    key: Optional["str"]
    title: Optional["MLString"]
    subtitle: Optional["MLString"]
    actions: Optional["None"]
    type: Optional["ContentBlockType"]
    appearance: Optional["ContentBlockAppearance"]
    size: Optional["int"]
    nodes: Optional["None"]
    sort: Optional["int"]


class Content(TypedDict, total=False):
    _id: Optional["str"]
    key: Optional["str"]
    status: Optional["ContentStatus"]
    title: Optional["MLString"]
    description: Optional["MLString"]
    picture: Optional["MLFile"]
    color: Optional["str"]
    assets: Optional["None"]
    body: Optional["MLString"]
    blocks: Optional["None"]
    sources: Optional["None"]
    variants: Optional["None"]
    fields: Optional["None"]
    prompt: Optional["Prompt"]
    callbackUrl: Optional["str"]
    callbackTriggerAttempts: Optional["int"]
    promptParams: Optional["Any"]
    promptResults: Optional["Any"]
    targets: Optional["None"]
    collections: Optional["None"]
    tags: Optional["None"]
    disabled: Optional["bool"]
    disableReason: Optional["str"]
    disabledAt: Optional["date"]
    publishedAt: Optional["date"]
    publishedUntil: Optional["date"]
    published: Optional["bool"]
    createdBy: Optional["SimpleAccount"]
    updatedBy: Optional["SimpleAccount"]
    createdAt: Optional["date"]
    updatedAt: Optional["date"]
    version: Optional["int"]
    credits: Optional["None"]
    resources: Optional["None"]
    liked: Optional["bool"]
    location: Optional["GeoLocation"]
    input: Optional["File"]


class ContentActionInput(TypedDict, total=False):
    _id: Optional["str"]
    key: Optional["str"]
    label: Optional["MLStringInput"]
    url: Optional["str"]
    content: Optional["str"]


class ContentNodeAssetInput(TypedDict, total=False):
    _id: Optional["str"]
    key: Optional["str"]
    file: Optional["MLFileInput"]
    caption: Optional["MLStringInput"]
    alt: Optional["MLStringInput"]


class ContentNodeInput(TypedDict, total=False):
    _id: Optional["str"]
    key: Optional["str"]
    title: Optional["MLStringInput"]
    subtitle: Optional["MLStringInput"]
    body: Optional["MLStringInput"]
    date: Optional["date"]
    assets: Optional["None"]
    resources: Optional["None"]
    actions: Optional["None"]
    url: Optional["str"]
    meta: Optional["str"]
    content: Optional["str"]
    collection: Optional["str"]
    prompt: Optional["str"]
    sort: Optional["int"]


class ContentBlockInput(TypedDict, total=False):
    _id: Optional["str"]
    key: Optional["str"]
    title: Optional["MLStringInput"]
    subtitle: Optional["MLStringInput"]
    actions: Optional["None"]
    type: Optional["ContentBlockType"]
    appearance: Optional["ContentBlockAppearance"]
    size: Optional["int"]
    nodes: Optional["None"]
    sort: Optional["int"]


class ContentInput(TypedDict, total=False):
    key: Optional["str"]
    title: Optional["MLStringInput"]
    description: Optional["MLStringInput"]
    picture: Optional["MLFileInput"]
    color: Optional["str"]
    variants: Optional["None"]
    fields: Optional["None"]
    body: Optional["MLStringInput"]
    blocks: Optional["None"]
    locale: Optional["Locale"]
    assets: Optional["None"]
    sources: Optional["None"]
    prompt: Optional["str"]
    targets: Optional["None"]
    collections: Optional["None"]
    publishedAt: Optional["date"]
    publishedUntil: Optional["date"]
    published: Optional["bool"]
    credits: Optional["None"]
    resources: Optional["None"]
    location: Optional["GeoLocationInput"]
    tags: Optional["None"]


class ContentListFilter(TypedDict, total=False):
    _id: Optional["None"]
    keyword: Optional["str"]
    promptId: Optional["str"]
    collections: Optional["None"]
    targets: Optional["None"]
    tags: Optional["None"]
    createdAt: Optional["DateRange"]
    exclude: Optional["None"]
    accountId: Optional["str"]
    custom: Optional["str"]
    status: Optional["ContentStatus"]
    interested: Optional["bool"]
    recently: Optional["bool"]
    liked: Optional["bool"]
    random: Optional["bool"]


class ContentListSort(TypedDict, total=False):
    key: Optional["str"]
    order: Optional["int"]


class ContentListFilterInput(TypedDict, total=False):
    _id: Optional["None"]
    keyword: Optional["str"]
    promptId: Optional["str"]
    collections: Optional["None"]
    targets: Optional["None"]
    tags: Optional["None"]
    createdAt: Optional["DateRangeInput"]
    exclude: Optional["None"]
    accountId: Optional["str"]
    custom: Optional["str"]
    status: Optional["ContentStatus"]
    random: Optional["bool"]
    includeExpired: Optional["bool"]


class ContentListSortInput(TypedDict, total=False):
    key: Optional["None"]
    order: Optional["None"]


class ContentList(TypedDict, total=False):
    items: Optional["None"]
    limit: Optional["int"]
    skip: Optional["int"]
    count: Optional["int"]
    sort: Optional["None"]
    filters: Optional["ContentListFilter"]
    queryStartedAt: Optional["date"]
    queryEndedAt: Optional["date"]
    duration: Optional["float"]
    _id: Optional["str"]


class DeviceType(str, Enum):
    CAR = "CAR"
    PHONE = "PHONE"
    TABLET = "TABLET"
    TV = "TV"
    SIGNAGE = "SIGNAGE"


class Device(TypedDict, total=False):
    _id: Optional["str"]
    title: Optional["str"]
    brand: Optional["str"]
    model: Optional["str"]
    color: Optional["str"]
    type: Optional["DeviceType"]
    identifier: Optional["str"]
    picture: Optional["File"]
    createdBy: Optional["SimpleAccount"]
    updatedBy: Optional["SimpleAccount"]
    createdAt: Optional["date"]
    updatedAt: Optional["date"]
    disabled: Optional["bool"]
    disableReason: Optional["str"]
    disabledAt: Optional["date"]


class DeviceInput(TypedDict, total=False):
    title: Optional["str"]
    brand: Optional["str"]
    model: Optional["str"]
    color: Optional["str"]
    type: Optional["DeviceType"]
    identifier: Optional["str"]
    picture: Optional["FileInput"]


class DeviceListFilter(TypedDict, total=False):
    _id: Optional["None"]
    keyword: Optional["str"]
    createdAt: Optional["DateRange"]
    exclude: Optional["None"]
    accountId: Optional["str"]
    custom: Optional["str"]


class DeviceListSort(TypedDict, total=False):
    key: Optional["str"]
    order: Optional["int"]


class DeviceListFilterInput(TypedDict, total=False):
    _id: Optional["None"]
    keyword: Optional["str"]
    createdAt: Optional["DateRangeInput"]
    exclude: Optional["None"]
    accountId: Optional["str"]
    custom: Optional["str"]


class DeviceListSortInput(TypedDict, total=False):
    key: Optional["None"]
    order: Optional["None"]


class DeviceList(TypedDict, total=False):
    items: Optional["None"]
    limit: Optional["int"]
    skip: Optional["int"]
    count: Optional["int"]
    sort: Optional["None"]
    filters: Optional["DeviceListFilter"]
    queryStartedAt: Optional["date"]
    queryEndedAt: Optional["date"]
    duration: Optional["float"]
    _id: Optional["str"]


class Insight(TypedDict, total=False):
    _id: Optional["str"]
    hash: Optional["str"]
    filter: Optional["InsightFilter"]
    value: Optional["float"]
    price: Optional["Price"]
    items: Optional["None"]
    createdBy: Optional["SimpleAccount"]
    createdAt: Optional["date"]
    updatedAt: Optional["date"]


class InsightItem(TypedDict, total=False):
    _id: Optional["str"]
    content: Optional["Content"]
    meta: Optional["Meta"]
    collection: Optional["Collection"]
    prompt: Optional["Prompt"]
    state: Optional["State"]
    reaction: Optional["Reaction"]
    device: Optional["Device"]
    location: Optional["Location"]
    price: Optional["Price"]
    value: Optional["float"]


class InsightList(TypedDict, total=False):
    items: Optional["None"]
    filters: Optional["None"]
    queryStartedAt: Optional["date"]
    queryEndedAt: Optional["date"]
    duration: Optional["float"]
    _id: Optional["str"]


class InsightListSort(TypedDict, total=False):
    key: Optional["None"]
    order: Optional["None"]


class InsightListSortInput(TypedDict, total=False):
    key: Optional["None"]
    order: Optional["None"]


class InsightFilter(TypedDict, total=False):
    _id: Optional["str"]
    operation: Optional["str"]
    dateRange: Optional["DateRange"]
    targets: Optional["None"]
    tags: Optional["None"]
    createdBy: Optional["str"]
    deviceId: Optional["str"]
    custom: Optional["None"]
    sort: Optional["None"]
    limit: Optional["int"]


class InsightFilterInput(TypedDict, total=False):
    _id: Optional["str"]
    operation: Optional["str"]
    dateRange: Optional["DateRangeInput"]
    targets: Optional["None"]
    tags: Optional["None"]
    createdBy: Optional["str"]
    deviceId: Optional["str"]
    custom: Optional["None"]
    sort: Optional["None"]
    limit: Optional["int"]


class InterestType(str, Enum):
    DIRECT = "DIRECT"
    RELATED = "RELATED"


class Interest(TypedDict, total=False):
    _id: Optional["str"]
    meta: Optional["Meta"]
    type: Optional["InterestType"]
    score: Optional["int"]
    createdAt: Optional["date"]


class InterestInput(TypedDict, total=False):
    metaId: Optional["str"]
    type: Optional["InterestType"]


class InterestListFilter(TypedDict, total=False):
    _id: Optional["None"]
    keyword: Optional["str"]
    createdAt: Optional["DateRange"]
    types: Optional["None"]
    accountId: Optional["str"]
    exclude: Optional["None"]
    tags: Optional["None"]


class InterestListFilterInput(TypedDict, total=False):
    _id: Optional["None"]
    keyword: Optional["str"]
    createdAt: Optional["DateRangeInput"]
    types: Optional["None"]
    accountId: Optional["str"]
    exclude: Optional["None"]
    tags: Optional["None"]


class InterestListSort(TypedDict, total=False):
    key: Optional["str"]
    order: Optional["int"]


class InterestListSortInput(TypedDict, total=False):
    key: Optional["None"]
    order: Optional["None"]


class InterestList(TypedDict, total=False):
    items: Optional["None"]
    limit: Optional["int"]
    skip: Optional["int"]
    count: Optional["int"]
    sort: Optional["None"]
    filters: Optional["InterestListFilter"]
    queryStartedAt: Optional["date"]
    queryEndedAt: Optional["date"]
    duration: Optional["float"]
    _id: Optional["str"]


class WeatherConditionCode(str, Enum):
    BLOWINGDUST = "BLOWINGDUST"
    CLEAR = "CLEAR"
    CLOUDY = "CLOUDY"
    FOGGY = "FOGGY"
    HAZE = "HAZE"
    MOSTLYCLEAR = "MOSTLYCLEAR"
    MOSTLYCLOUDY = "MOSTLYCLOUDY"
    PARTLYCLOUDY = "PARTLYCLOUDY"
    SMOKY = "SMOKY"
    BREEZY = "BREEZY"
    WINDY = "WINDY"
    DRIZZLE = "DRIZZLE"
    HEAVYRAIN = "HEAVYRAIN"
    ISOLATEDTHUNDERSTORMS = "ISOLATEDTHUNDERSTORMS"
    RAIN = "RAIN"
    SUNSHOWERS = "SUNSHOWERS"
    SCATTEREDTHUNDERSTORMS = "SCATTEREDTHUNDERSTORMS"
    STRONGSTORMS = "STRONGSTORMS"
    THUNDERSTORMS = "THUNDERSTORMS"
    FRIGID = "FRIGID"
    HAIL = "HAIL"
    HOT = "HOT"
    FLURRIES = "FLURRIES"
    SLEET = "SLEET"
    SNOW = "SNOW"
    SUNFLURRIES = "SUNFLURRIES"
    WINTRYMIX = "WINTRYMIX"
    BLIZZARD = "BLIZZARD"
    BLOWINGSNOW = "BLOWINGSNOW"
    FREEZINGDRIZZLE = "FREEZINGDRIZZLE"
    FREEZINGRAIN = "FREEZINGRAIN"
    HEAVYSNOW = "HEAVYSNOW"
    HURRICANE = "HURRICANE"
    TROPICALSTORM = "TROPICALSTORM"


class PressureTrend(str, Enum):
    FALLING = "FALLING"
    RISING = "RISING"
    STEADY = "STEADY"


class WeatherData(TypedDict, total=False):
    cloudCover: Optional["float"]
    cloudCoverLowAltPct: Optional["float"]
    cloudCoverMidAltPct: Optional["float"]
    cloudCoverHighAltPct: Optional["float"]
    conditionCode: Optional["WeatherConditionCode"]
    daylight: Optional["bool"]
    humidity: Optional["float"]
    precipitationIntensity: Optional["float"]
    pressure: Optional["float"]
    pressureTrend: Optional["PressureTrend"]
    temperature: Optional["float"]
    temperatureApparent: Optional["float"]
    temperatureDewPoint: Optional["float"]
    uvIndex: Optional["float"]
    visibility: Optional["float"]
    windDirection: Optional["float"]
    windGust: Optional["float"]
    windSpeed: Optional["float"]


class Weather(TypedDict, total=False):
    current: Optional["WeatherData"]


class Location(TypedDict, total=False):
    _id: Optional["str"]
    geo: Optional["GeoLocation"]
    device: Optional["Device"]
    weather: Optional["Weather"]
    createdBy: Optional["SimpleAccount"]
    updatedBy: Optional["SimpleAccount"]
    createdAt: Optional["date"]
    updatedAt: Optional["date"]
    disabled: Optional["bool"]
    disableReason: Optional["str"]
    disabledAt: Optional["date"]
    city: Optional["str"]
    country: Optional["Country"]


class LocationInput(TypedDict, total=False):
    latitude: Optional["str"]
    longitude: Optional["str"]
    deviceId: Optional["str"]
    includeWeather: Optional["bool"]


class LocationListFilter(TypedDict, total=False):
    _id: Optional["None"]
    keyword: Optional["str"]
    createdAt: Optional["DateRange"]
    exclude: Optional["None"]
    accountId: Optional["str"]
    deviceId: Optional["str"]
    custom: Optional["str"]


class LocationListSort(TypedDict, total=False):
    key: Optional["str"]
    order: Optional["int"]


class LocationListFilterInput(TypedDict, total=False):
    _id: Optional["None"]
    keyword: Optional["str"]
    createdAt: Optional["DateRangeInput"]
    exclude: Optional["None"]
    accountId: Optional["str"]
    deviceId: Optional["str"]
    custom: Optional["str"]


class LocationListSortInput(TypedDict, total=False):
    key: Optional["None"]
    order: Optional["None"]


class LocationList(TypedDict, total=False):
    items: Optional["None"]
    limit: Optional["int"]
    skip: Optional["int"]
    count: Optional["int"]
    sort: Optional["None"]
    filters: Optional["LocationListFilter"]
    queryStartedAt: Optional["date"]
    queryEndedAt: Optional["date"]
    duration: Optional["float"]
    _id: Optional["str"]


class LogType(str, Enum):
    ACCESS = "ACCESS"
    EVENT = "EVENT"
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
    REPLACE = "REPLACE"
    ARCHIVE = "ARCHIVE"
    ENABLE = "ENABLE"
    DISABLE = "DISABLE"
    CHANGE = "CHANGE"
    HIGHLIGHT = "HIGHLIGHT"
    UNHIGHLIGHT = "UNHIGHLIGHT"
    SIGN = "SIGN"
    FAIL = "FAIL"
    SUCCESS = "SUCCESS"
    ERROR = "ERROR"
    LIKE = "LIKE"
    DISLIKE = "DISLIKE"
    UNPUBLISH = "UNPUBLISH"
    PUBLISH = "PUBLISH"
    INVITE = "INVITE"
    ACCEPT = "ACCEPT"
    REJECT = "REJECT"
    WITHDRAW = "WITHDRAW"
    KICK = "KICK"
    LEAVE = "LEAVE"
    UPGRADE = "UPGRADE"
    DOWNGRADE = "DOWNGRADE"
    INTEGRATE = "INTEGRATE"
    REVOKE = "REVOKE"
    USAGE = "USAGE"
    CANCEL = "CANCEL"
    IGNORE = "IGNORE"
    UPLOAD = "UPLOAD"
    FOLLOW = "FOLLOW"
    UNFOLLOW = "UNFOLLOW"
    BLOCK = "BLOCK"
    UNBLOCK = "UNBLOCK"
    SUBSCRIBE = "SUBSCRIBE"
    UNSUBSCRIBE = "UNSUBSCRIBE"
    REACTIVATE = "REACTIVATE"
    DEACTIVATE = "DEACTIVATE"
    VIEW = "VIEW"


class LogTopic(str, Enum):
    SUPER = "SUPER"
    COMMUNICATION = "COMMUNICATION"
    STORAGE = "STORAGE"
    CLIENT = "CLIENT"
    AUTH = "AUTH"
    COLLECTION = "COLLECTION"
    CONTENT = "CONTENT"
    ASSET = "ASSET"
    META = "META"
    PROMPT = "PROMPT"
    TARGET = "TARGET"
    DEVICE = "DEVICE"
    STATE = "STATE"
    REACTION = "REACTION"
    LOCATION = "LOCATION"
    INTEREST = "INTEREST"


class LogAction(str, Enum):
    CLICK = "CLICK"
    SEARCH = "SEARCH"
    SUBMIT = "SUBMIT"
    PLAY = "PLAY"
    PAUSE = "PAUSE"
    STOP = "STOP"
    EXIT = "EXIT"
    DOWNLOAD = "DOWNLOAD"
    SESSION = "SESSION"
    VIEW = "VIEW"
    REACH = "REACH"
    IMPRESSION = "IMPRESSION"
    SHARE = "SHARE"


class LogDemographics(TypedDict, total=False):
    birthday: Optional["date"]
    country: Optional["Country"]
    city: Optional["str"]
    location: Optional["GeoLocation"]


class LogDemographicsInput(TypedDict, total=False):
    birthday: Optional["date"]
    country: Optional["Country"]
    city: Optional["str"]
    location: Optional["GeoLocationInput"]


class LogViewport(TypedDict, total=False):
    width: Optional["int"]
    height: Optional["int"]
    dpi: Optional["float"]


class LogViewportInput(TypedDict, total=False):
    width: Optional["int"]
    height: Optional["int"]
    dpi: Optional["float"]


class LogUTM(TypedDict, total=False):
    source: Optional["str"]
    medium: Optional["str"]
    campaign: Optional["str"]
    term: Optional["str"]
    content: Optional["str"]


class LogUTMInput(TypedDict, total=False):
    source: Optional["str"]
    medium: Optional["str"]
    campaign: Optional["str"]
    term: Optional["str"]
    content: Optional["str"]


class LogClient(TypedDict, total=False):
    ip: Optional["str"]
    host: Optional["str"]
    userAgent: Optional["str"]
    viewport: Optional["LogViewport"]
    locale: Optional["Locale"]
    currency: Optional["Currency"]
    browser: Optional["Any"]
    engine: Optional["Any"]
    os: Optional["Any"]
    device: Optional["Any"]
    cpu: Optional["Any"]
    location: Optional["GeoLocation"]


class LogClientInput(TypedDict, total=False):
    ip: Optional["str"]
    host: Optional["str"]
    userAgent: Optional["str"]
    viewport: Optional["LogViewportInput"]
    locale: Optional["Locale"]
    currency: Optional["Currency"]
    browser: Optional["Any"]
    engine: Optional["Any"]
    os: Optional["Any"]
    device: Optional["Any"]
    cpu: Optional["Any"]
    location: Optional["GeoLocationInput"]


class LogProfile(TypedDict, total=False):
    _id: Optional["str"]
    email: Optional["str"]
    firstName: Optional["str"]
    lastName: Optional["str"]


class LogProfileInput(TypedDict, total=False):
    _id: Optional["str"]
    email: Optional["str"]
    firstName: Optional["str"]
    lastName: Optional["str"]


class LogPayload(TypedDict, total=False):
    _id: Optional["str"]
    __from: Optional["str"]
    to: Optional["str"]
    owner: Optional["str"]
    type: Optional["str"]
    name: Optional["str"]
    profile: Optional["LogProfile"]
    demographics: Optional["LogDemographics"]
    slug: Optional["str"]
    price: Optional["Price"]
    basePrice: Optional["PriceLite"]
    related: Optional["Any"]
    key: Optional["str"]
    action: Optional["LogAction"]
    duration: Optional["float"]
    value: Optional["Any"]
    utm: Optional["LogUTM"]
    referrer: Optional["str"]
    client: Optional["LogClient"]
    method: Optional["str"]
    previous: Optional["Any"]
    winner: Optional["Any"]
    loser: Optional["Any"]
    code: Optional["str"]
    message: Optional["str"]
    details: Optional["None"]
    raw: Optional["Any"]


class LogPayloadInput(TypedDict, total=False):
    _id: Optional["str"]
    __from: Optional["str"]
    to: Optional["str"]
    owner: Optional["str"]
    type: Optional["str"]
    name: Optional["str"]
    slug: Optional["str"]
    related: Optional["Any"]
    duration: Optional["float"]
    key: Optional["str"]
    action: Optional["LogAction"]
    value: Optional["Any"]
    utm: Optional["LogUTMInput"]
    referrer: Optional["str"]
    client: Optional["LogClientInput"]
    method: Optional["str"]
    previous: Optional["Any"]
    winner: Optional["Any"]
    loser: Optional["Any"]
    code: Optional["str"]
    message: Optional["str"]
    details: Optional["None"]
    raw: Optional["Any"]
    price: Optional["PriceInput"]
    basePrice: Optional["PriceInput"]
    demographics: Optional["LogDemographicsInput"]


class Log(TypedDict, total=False):
    _id: Optional["str"]
    type: Optional["LogType"]
    topic: Optional["LogTopic"]
    payload: Optional["LogPayload"]
    description: Optional["str"]
    createdAt: Optional["date"]
    createdBy: Optional["SimpleAccount"]
    updatedAt: Optional["date"]
    updatedBy: Optional["SimpleAccount"]
    disabled: Optional["bool"]
    disableReason: Optional["str"]


class LogInput(TypedDict, total=False):
    type: Optional["LogType"]
    topic: Optional["LogTopic"]
    description: Optional["str"]
    payload: Optional["LogPayloadInput"]


class LogListFilterTypeItem(TypedDict, total=False):
    value: Optional["None"]
    operator: Optional["ListFilterOperator"]


class LogListFilterTypeItemInput(TypedDict, total=False):
    value: Optional["None"]
    operator: Optional["ListFilterOperator"]


class LogListFilterTopicItem(TypedDict, total=False):
    value: Optional["None"]
    operator: Optional["ListFilterOperator"]


class LogListFilterTopicItemInput(TypedDict, total=False):
    value: Optional["None"]
    operator: Optional["ListFilterOperator"]


class LogListFilterActionItem(TypedDict, total=False):
    value: Optional["None"]
    operator: Optional["ListFilterOperator"]


class LogListFilterActionItemInput(TypedDict, total=False):
    value: Optional["None"]
    operator: Optional["ListFilterOperator"]


class LogListFilter(TypedDict, total=False):
    _id: Optional["None"]
    keyword: Optional["str"]
    createdAt: Optional["DateRange"]
    exclude: Optional["None"]
    accountId: Optional["str"]
    types: Optional["None"]
    topics: Optional["None"]
    actions: Optional["None"]
    targets: Optional["None"]
    related: Optional["None"]
    custom: Optional["str"]


class LogListSort(TypedDict, total=False):
    key: Optional["str"]
    order: Optional["int"]


class LogListFilterInput(TypedDict, total=False):
    _id: Optional["None"]
    keyword: Optional["str"]
    createdAt: Optional["DateRangeInput"]
    exclude: Optional["None"]
    accountId: Optional["str"]
    types: Optional["None"]
    topics: Optional["None"]
    actions: Optional["None"]
    targets: Optional["None"]
    related: Optional["None"]
    custom: Optional["str"]


class LogListSortInput(TypedDict, total=False):
    key: Optional["None"]
    order: Optional["None"]


class LogList(TypedDict, total=False):
    items: Optional["None"]
    limit: Optional["int"]
    skip: Optional["int"]
    count: Optional["int"]
    sort: Optional["None"]
    filters: Optional["LogListFilter"]
    queryStartedAt: Optional["date"]
    queryEndedAt: Optional["date"]
    duration: Optional["float"]
    _id: Optional["str"]


class MediaStatus(str, Enum):
    UPLOADING = "UPLOADING"
    UPLOADED = "UPLOADED"
    FAILED = "FAILED"


class Media(TypedDict, total=False):
    _id: Optional["str"]
    file: Optional["File"]
    targets: Optional["None"]
    tags: Optional["None"]
    createdBy: Optional["SimpleAccount"]
    updatedBy: Optional["SimpleAccount"]
    createdAt: Optional["date"]
    updatedAt: Optional["date"]
    status: Optional["MediaStatus"]
    version: Optional["int"]
    description: Optional["str"]
    title: Optional["str"]
    keywords: Optional["None"]
    disableReason: Optional["str"]
    disabled: Optional["bool"]


class MediaInput(TypedDict, total=False):
    _id: Optional["str"]
    contentType: Optional["str"]
    data: Optional["str"]
    path: Optional["str"]
    filename: Optional["str"]
    key: Optional["str"]
    targets: Optional["None"]
    tags: Optional["None"]
    description: Optional["str"]
    title: Optional["str"]
    keywords: Optional["None"]


class MediaListFilter(TypedDict, total=False):
    _id: Optional["None"]
    keyword: Optional["str"]
    contentTypes: Optional["None"]
    createdAt: Optional["DateRange"]
    exclude: Optional["None"]
    accountId: Optional["str"]
    targets: Optional["None"]
    tags: Optional["None"]
    custom: Optional["str"]


class MediaListSort(TypedDict, total=False):
    key: Optional["str"]
    order: Optional["int"]


class MediaListFilterInput(TypedDict, total=False):
    _id: Optional["None"]
    keyword: Optional["str"]
    contentTypes: Optional["None"]
    createdAt: Optional["DateRangeInput"]
    exclude: Optional["None"]
    accountId: Optional["str"]
    targets: Optional["None"]
    tags: Optional["None"]
    custom: Optional["str"]


class MediaListSortInput(TypedDict, total=False):
    key: Optional["None"]
    order: Optional["None"]


class MediaList(TypedDict, total=False):
    items: Optional["None"]
    limit: Optional["int"]
    skip: Optional["int"]
    count: Optional["int"]
    sort: Optional["None"]
    filters: Optional["MediaListFilter"]
    queryStartedAt: Optional["date"]
    queryEndedAt: Optional["date"]
    duration: Optional["float"]
    _id: Optional["str"]


class MetaInsights(TypedDict, total=False):
    usage: Optional["int"]


class MetaVariant(TypedDict, total=False):
    _id: Optional["str"]
    key: Optional["str"]
    label: Optional["MLString"]
    description: Optional["MLString"]
    color: Optional["str"]
    picture: Optional["MLFile"]
    tags: Optional["None"]
    resources: Optional["None"]


class MetaVariantInput(TypedDict, total=False):
    _id: Optional["str"]
    key: Optional["str"]
    label: Optional["MLStringInput"]
    description: Optional["MLStringInput"]
    color: Optional["str"]
    picture: Optional["MLFileInput"]
    tags: Optional["None"]
    resources: Optional["None"]


class Meta(TypedDict, total=False):
    _id: Optional["str"]
    type: Optional["str"]
    key: Optional["str"]
    label: Optional["MLString"]
    description: Optional["MLString"]
    color: Optional["str"]
    location: Optional["GeoLocation"]
    picture: Optional["MLFile"]
    targets: Optional["None"]
    resources: Optional["None"]
    variants: Optional["None"]
    tags: Optional["None"]
    insights: Optional["MetaInsights"]
    createdAt: Optional["date"]
    disabled: Optional["bool"]
    disableReason: Optional["str"]
    disabledAt: Optional["date"]
    published: Optional["bool"]


class MetaInput(TypedDict, total=False):
    label: Optional["MLStringInput"]
    description: Optional["MLStringInput"]
    color: Optional["str"]
    key: Optional["str"]
    type: Optional["str"]
    picture: Optional["MLFileInput"]
    location: Optional["GeoLocationInput"]
    tags: Optional["None"]
    targets: Optional["None"]
    published: Optional["bool"]
    resources: Optional["None"]
    variants: Optional["None"]


class MetaListFilter(TypedDict, total=False):
    _id: Optional["None"]
    keyword: Optional["str"]
    createdAt: Optional["DateRange"]
    exclude: Optional["None"]
    types: Optional["None"]
    targets: Optional["None"]
    tags: Optional["None"]


class MetaListFilterInput(TypedDict, total=False):
    _id: Optional["None"]
    keyword: Optional["str"]
    createdAt: Optional["DateRangeInput"]
    exclude: Optional["None"]
    types: Optional["None"]
    targets: Optional["None"]
    tags: Optional["None"]
    keys: Optional["None"]


class MetaListSort(TypedDict, total=False):
    key: Optional["str"]
    order: Optional["int"]


class MetaListSortInput(TypedDict, total=False):
    key: Optional["None"]
    order: Optional["None"]


class MetaList(TypedDict, total=False):
    items: Optional["None"]
    limit: Optional["int"]
    skip: Optional["int"]
    count: Optional["int"]
    sort: Optional["None"]
    filters: Optional["MetaListFilter"]
    queryStartedAt: Optional["date"]
    queryEndedAt: Optional["date"]
    duration: Optional["float"]
    _id: Optional["str"]


class PromptMessage(TypedDict, total=False):
    _id: Optional["str"]
    prompt: Optional["Prompt"]
    content: Optional["Content"]
    params: Optional["Any"]
    results: Optional["Any"]


class PromptRunInput(TypedDict, total=False):
    contentInitialParams: Optional["ContentInput"]
    attachment: Optional["FileInput"]
    params: Optional["Any"]


class PromptSQS(TypedDict, total=False):
    url: Optional["str"]
    secret: Optional["str"]
    key: Optional["str"]
    region: Optional["str"]


class PromptSQSInput(TypedDict, total=False):
    url: Optional["str"]
    secret: Optional["str"]
    key: Optional["str"]
    region: Optional["str"]


class Prompt(TypedDict, total=False):
    _id: Optional["str"]
    targets: Optional["None"]
    collections: Optional["None"]
    title: Optional["MLString"]
    description: Optional["MLString"]
    picture: Optional["MLFile"]
    color: Optional["str"]
    key: Optional["str"]
    prompt: Optional["str"]
    negativePrompt: Optional["str"]
    resources: Optional["None"]
    fn: Optional["str"]
    tags: Optional["None"]
    sqs: Optional["PromptSQS"]
    webhookUrl: Optional["str"]
    createdBy: Optional["SimpleAccount"]
    updatedBy: Optional["SimpleAccount"]
    createdAt: Optional["date"]
    updatedAt: Optional["date"]
    disabled: Optional["bool"]
    disableReason: Optional["str"]
    disabledAt: Optional["date"]
    publishedAt: Optional["date"]
    publishedUntil: Optional["date"]
    published: Optional["bool"]
    version: Optional["int"]
    contentInitialParams: Optional["Content"]


class PromptInput(TypedDict, total=False):
    key: Optional["str"]
    title: Optional["MLStringInput"]
    description: Optional["MLStringInput"]
    picture: Optional["MLFileInput"]
    color: Optional["str"]
    prompt: Optional["str"]
    negativePrompt: Optional["str"]
    fn: Optional["str"]
    resources: Optional["None"]
    sqs: Optional["PromptSQSInput"]
    webhookUrl: Optional["str"]
    collections: Optional["None"]
    targets: Optional["None"]
    tags: Optional["None"]
    publishedAt: Optional["date"]
    publishedUntil: Optional["date"]
    published: Optional["bool"]
    contentInitialParams: Optional["ContentInput"]


class PromptListFilter(TypedDict, total=False):
    _id: Optional["None"]
    keyword: Optional["str"]
    createdAt: Optional["DateRange"]
    exclude: Optional["None"]
    accountId: Optional["str"]
    targets: Optional["None"]
    collections: Optional["None"]
    tags: Optional["None"]
    custom: Optional["str"]
    contentId: Optional["str"]


class PromptListSort(TypedDict, total=False):
    key: Optional["str"]
    order: Optional["int"]


class PromptListFilterInput(TypedDict, total=False):
    _id: Optional["None"]
    keyword: Optional["str"]
    createdAt: Optional["DateRangeInput"]
    exclude: Optional["None"]
    accountId: Optional["str"]
    targets: Optional["None"]
    collections: Optional["None"]
    tags: Optional["None"]
    custom: Optional["str"]
    contentId: Optional["str"]


class PromptListSortInput(TypedDict, total=False):
    key: Optional["None"]
    order: Optional["None"]


class PromptList(TypedDict, total=False):
    items: Optional["None"]
    limit: Optional["int"]
    skip: Optional["int"]
    count: Optional["int"]
    sort: Optional["None"]
    filters: Optional["PromptListFilter"]
    queryStartedAt: Optional["date"]
    queryEndedAt: Optional["date"]
    duration: Optional["float"]
    _id: Optional["str"]


class ReactionType(str, Enum):
    LIKEMETA = "LIKEMETA"
    LIKEPROMPT = "LIKEPROMPT"
    LIKECOLLECTION = "LIKECOLLECTION"
    LIKECONTENT = "LIKECONTENT"
    LIKEREACTION = "LIKEREACTION"
    COMMENT = "COMMENT"


ReactionPayload = Any


class Reaction(TypedDict, total=False):
    _id: Optional["str"]
    key: Optional["str"]
    type: Optional["ReactionType"]
    to: Optional["ReactionPayload"]
    body: Optional["str"]
    attachments: Optional["None"]
    liked: Optional["bool"]
    value: Optional["int"]
    createdBy: Optional["SimpleAccount"]
    createdAt: Optional["date"]
    updatedAt: Optional["date"]


class ReactionInput(TypedDict, total=False):
    _id: Optional["str"]
    key: Optional["str"]
    type: Optional["ReactionType"]
    to: Optional["str"]
    body: Optional["str"]
    value: Optional["int"]
    attachments: Optional["None"]


class ReactionListFilter(TypedDict, total=False):
    _id: Optional["None"]
    keys: Optional["ListFilterItem"]
    keyword: Optional["str"]
    createdAt: Optional["DateRange"]
    exclude: Optional["None"]
    types: Optional["None"]
    createdBy: Optional["str"]
    to: Optional["str"]


class ReactionListFilterInput(TypedDict, total=False):
    _id: Optional["None"]
    keys: Optional["ListFilterItemInput"]
    keyword: Optional["str"]
    createdAt: Optional["DateRangeInput"]
    exclude: Optional["None"]
    types: Optional["None"]
    createdBy: Optional["str"]
    to: Optional["str"]


class ReactionListSort(TypedDict, total=False):
    key: Optional["str"]
    order: Optional["int"]


class ReactionListSortInput(TypedDict, total=False):
    key: Optional["None"]
    order: Optional["None"]


class ReactionList(TypedDict, total=False):
    items: Optional["None"]
    limit: Optional["int"]
    skip: Optional["int"]
    count: Optional["int"]
    sort: Optional["None"]
    filters: Optional["ReactionListFilter"]
    queryStartedAt: Optional["date"]
    queryEndedAt: Optional["date"]
    duration: Optional["float"]
    _id: Optional["str"]


class State(TypedDict, total=False):
    _id: Optional["str"]
    key: Optional["str"]
    targets: Optional["None"]
    target: Optional["Target"]
    values: Optional["None"]
    tags: Optional["None"]
    content: Optional["Content"]
    device: Optional["Device"]
    createdBy: Optional["SimpleAccount"]
    updatedBy: Optional["SimpleAccount"]
    createdAt: Optional["date"]
    updatedAt: Optional["date"]
    disabled: Optional["bool"]
    disableReason: Optional["str"]
    disabledAt: Optional["date"]


class StateInput(TypedDict, total=False):
    _id: Optional["str"]
    key: Optional["str"]
    targets: Optional["None"]
    tags: Optional["None"]
    values: Optional["None"]
    contentId: Optional["str"]
    deviceId: Optional["str"]
    targetId: Optional["str"]


class StateListSort(TypedDict, total=False):
    key: Optional["str"]
    order: Optional["int"]


class StateListFilter(TypedDict, total=False):
    _id: Optional["None"]
    keyword: Optional["str"]
    tags: Optional["None"]
    createdAt: Optional["DateRange"]
    targets: Optional["None"]
    exclude: Optional["None"]
    accountId: Optional["str"]
    custom: Optional["str"]


class StateListFilterInput(TypedDict, total=False):
    _id: Optional["None"]
    keyword: Optional["str"]
    tags: Optional["None"]
    createdAt: Optional["DateRangeInput"]
    targets: Optional["None"]
    exclude: Optional["None"]
    accountId: Optional["str"]
    custom: Optional["str"]


class StateListSortInput(TypedDict, total=False):
    key: Optional["None"]
    order: Optional["None"]


class StateList(TypedDict, total=False):
    items: Optional["None"]
    limit: Optional["int"]
    skip: Optional["int"]
    count: Optional["int"]
    sort: Optional["None"]
    filters: Optional["StateListFilter"]
    queryStartedAt: Optional["date"]
    queryEndedAt: Optional["date"]
    duration: Optional["float"]
    _id: Optional["str"]


class TargetClient(TypedDict, total=False):
    _id: Optional["str"]
    name: Optional["str"]
    key: Optional["str"]
    currentVersion: Optional["str"]
    minVersion: Optional["str"]
    maxVersion: Optional["str"]


class TargetClientInput(TypedDict, total=False):
    _id: Optional["str"]
    name: Optional["str"]
    key: Optional["str"]
    currentVersion: Optional["str"]
    minVersion: Optional["str"]
    maxVersion: Optional["str"]


class TargetEmailConfig(TypedDict, total=False):
    welcome: Optional["bool"]


class TargetEmailConfigInput(TypedDict, total=False):
    welcome: Optional["bool"]


class TargetConfig(TypedDict, total=False):
    email: Optional["TargetEmailConfig"]
    clients: Optional["None"]


class TargetConfigInput(TypedDict, total=False):
    email: Optional["TargetEmailConfigInput"]
    clients: Optional["None"]


class Target(TypedDict, total=False):
    _id: Optional["str"]
    key: Optional["str"]
    title: Optional["MLString"]
    description: Optional["MLString"]
    picture: Optional["MLFile"]
    color: Optional["str"]
    createdBy: Optional["SimpleAccount"]
    updatedBy: Optional["SimpleAccount"]
    createdAt: Optional["date"]
    updatedAt: Optional["date"]
    disabled: Optional["bool"]
    disableReason: Optional["str"]
    disabledAt: Optional["date"]
    tags: Optional["None"]
    lastUsed: Optional["date"]
    config: Optional["TargetConfig"]


class TargetInput(TypedDict, total=False):
    key: Optional["str"]
    title: Optional["MLStringInput"]
    description: Optional["MLStringInput"]
    picture: Optional["MLFileInput"]
    color: Optional["str"]
    tags: Optional["None"]
    config: Optional["TargetConfigInput"]


class TargetListFilter(TypedDict, total=False):
    _id: Optional["None"]
    keys: Optional["None"]
    keyword: Optional["str"]
    createdAt: Optional["DateRange"]
    exclude: Optional["None"]
    accountId: Optional["str"]
    custom: Optional["str"]
    tags: Optional["None"]


class TargetListSort(TypedDict, total=False):
    key: Optional["str"]
    order: Optional["int"]


class TargetListFilterInput(TypedDict, total=False):
    _id: Optional["None"]
    keys: Optional["None"]
    keyword: Optional["str"]
    createdAt: Optional["DateRangeInput"]
    exclude: Optional["None"]
    accountId: Optional["str"]
    custom: Optional["str"]
    tags: Optional["None"]


class TargetListSortInput(TypedDict, total=False):
    key: Optional["None"]
    order: Optional["None"]


class TargetList(TypedDict, total=False):
    items: Optional["None"]
    limit: Optional["int"]
    skip: Optional["int"]
    count: Optional["int"]
    sort: Optional["None"]
    filters: Optional["TargetListFilter"]
    queryStartedAt: Optional["date"]
    queryEndedAt: Optional["date"]
    duration: Optional["float"]
    _id: Optional["str"]


class KeyValue(TypedDict, total=False):
    _id: Optional["str"]
    key: Optional["str"]
    value: Optional["str"]
    attachment: Optional["File"]


class KeyValueInput(TypedDict, total=False):
    _id: Optional["str"]
    key: Optional["str"]
    value: Optional["str"]
    attachment: Optional["FileInput"]


class CacheControlScope(str, Enum):
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"


class GeoLocationType(str, Enum):
    POINT = "POINT"
    LINESTRING = "LINESTRING"
    POLYGON = "POLYGON"
    MULTIPOINT = "MULTIPOINT"
    MULTILINESTRING = "MULTILINESTRING"
    MULTIPOLYGON = "MULTIPOLYGON"
    GEOMETRYCOLLECTION = "GEOMETRYCOLLECTION"


class ListExclude(str, Enum):
    DISABLED = "DISABLED"
    COUNT = "COUNT"


class SetupResponse(TypedDict, total=False):
    success: Optional["bool"]
    report: Optional["Any"]


class GeoLocation(TypedDict, total=False):
    type: Optional["GeoLocationType"]
    coordinates: Optional["Any"]


class GeoLocationInput(TypedDict, total=False):
    type: Optional["None"]
    coordinates: Optional["None"]


class Phone(TypedDict, total=False):
    code: Optional["None"]
    number: Optional["None"]
    verified: Optional["bool"]


class PhoneInput(TypedDict, total=False):
    code: Optional["str"]
    number: Optional["str"]


class MLString(TypedDict, total=False):
    current: Optional["str"]
    en: Optional["str"]
    tr: Optional["str"]
    es: Optional["str"]
    de: Optional["str"]
    fr: Optional["str"]
    it: Optional["str"]


class MLArrayOfString(TypedDict, total=False):
    current: Optional["None"]
    en: Optional["None"]
    tr: Optional["None"]
    es: Optional["None"]
    de: Optional["None"]
    fr: Optional["None"]
    it: Optional["None"]


class MLStringInput(TypedDict, total=False):
    en: Optional["str"]
    tr: Optional["str"]
    es: Optional["str"]
    de: Optional["str"]
    fr: Optional["str"]
    it: Optional["str"]


class MLArrayOfStringInput(TypedDict, total=False):
    en: Optional["None"]
    tr: Optional["None"]
    es: Optional["None"]
    de: Optional["None"]
    fr: Optional["None"]
    it: Optional["None"]


class MLFile(TypedDict, total=False):
    current: Optional["File"]
    en: Optional["File"]
    tr: Optional["File"]
    es: Optional["File"]
    de: Optional["File"]
    fr: Optional["File"]
    it: Optional["File"]


class MLFileInput(TypedDict, total=False):
    en: Optional["FileInput"]
    tr: Optional["FileInput"]
    es: Optional["FileInput"]
    de: Optional["FileInput"]
    fr: Optional["FileInput"]
    it: Optional["FileInput"]


class DateRange(TypedDict, total=False):
    __from: Optional["date"]
    to: Optional["date"]


class DateRangeInput(TypedDict, total=False):
    __from: Optional["date"]
    to: Optional["date"]


class ListFilterOperator(str, Enum):
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"
    ALL = "ALL"
    NOT_ALL = "NOT_ALL"
    INCLUDE_OPTIONAL = "INCLUDE_OPTIONAL"
    EXCLUDE_OPTIONAL = "EXCLUDE_OPTIONAL"
    ALL_OPTIONAL = "ALL_OPTIONAL"
    NOT_ALL_OPTIONAL = "NOT_ALL_OPTIONAL"


class ListFilterItem(TypedDict, total=False):
    value: Optional["None"]
    operator: Optional["ListFilterOperator"]
    key: Optional["str"]


class ListFilterItemInput(TypedDict, total=False):
    value: Optional["None"]
    operator: Optional["ListFilterOperator"]
    key: Optional["str"]
