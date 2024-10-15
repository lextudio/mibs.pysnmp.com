# SNMP MIB module (HPN-ICF-DOT11-REF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-DOT11-REF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:48 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hpnicfDot11 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75)
)
hpnicfDot11.setRevisions(
        ("2010-01-07 20:00",
         "2009-05-07 20:00",
         "2007-06-21 20:00",
         "2007-04-27 20:00",
         "2006-05-10 19:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfDot11ObjectIDType(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )



class HpnicfDot11RadioScopeType(Integer32, TextualConvention):
    status = "current"


class HpnicfDot11RadioType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 1),
          ("dot11ac", 64),
          ("dot11an", 32),
          ("dot11b", 2),
          ("dot11g", 4),
          ("dot11gn", 16),
          ("dot11n", 8))
    )



class HpnicfDot11RadioType2(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 1),
          ("dot11ac", 32),
          ("dot11an", 8),
          ("dot11b", 2),
          ("dot11g", 4),
          ("dot11gn", 16))
    )



class HpnicfDot11MACModeType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fatAP", 4),
          ("localbridge", 3),
          ("localtunnel", 2),
          ("split", 1))
    )



class HpnicfDot11ChannelScopeType(Integer32, TextualConvention):
    status = "current"


class HpnicfDot11NotifyReasonType(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class HpnicfDot11SSIDStringType(OctetString, TextualConvention):
    status = "current"


class HpnicfDot11ServicePolicyIDType(Integer32, TextualConvention):
    status = "current"


class HpnicfDot11SSIDEncryptModeType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cipher", 2),
          ("cleartxt", 1),
          ("ext", 3))
    )



class HpnicfDot11PreambleType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 1),
          ("short", 2))
    )



class HpnicfDot11TxPwrLevelScopeType(Integer32, TextualConvention):
    status = "current"


class HpnicfDot11RFModeType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("manual", 1))
    )



class HpnicfDot11TunnelSecSchemType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cleartxt", 1),
          ("dtls", 2),
          ("ipsec", 3))
    )



class HpnicfDot11SecIEStatusType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("all", 4),
          ("ext", 5),
          ("none", 1),
          ("rsn", 2),
          ("wpa", 3))
    )



class HpnicfDot11CipherType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              16,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("aesccmp", 16),
          ("none", 1),
          ("tkip", 4),
          ("wep104", 32),
          ("wep128", 128),
          ("wep40", 2),
          ("wpisms4", 64))
    )



class HpnicfDot11AuthenType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("all", 4),
          ("none", 1),
          ("opensystem", 2),
          ("sharedkey", 3))
    )



class HpnicfDot11AKMType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dot1x", 3),
          ("ext", 4),
          ("none", 1),
          ("psk", 2))
    )



class HpnicfDot11AssocFailType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("invalidie", 3),
          ("toomanyassoc", 2),
          ("unknownfailure", 1),
          ("unsupportedcap", 6),
          ("unsupportedpwrcap", 5),
          ("unsupportedrate", 4))
    )



class HpnicfDot11AuthorFailType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("akminvalid", 7),
          ("groupcipherinvalid", 5),
          ("invalidie", 2),
          ("pairwisecipherinvalid", 6),
          ("rsnieversionunsupported", 3),
          ("unknownfailure", 1),
          ("wpaieversionunsupported", 4))
    )



class HpnicfDot11QosAcType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("acbe", 2),
          ("acbk", 1),
          ("acvi", 3),
          ("acvo", 4))
    )



class HpnicfDot11RadioElementIndex(Unsigned32, TextualConvention):
    status = "current"


class HpnicfDot11WorkMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hybrid", 3),
          ("monitor", 2),
          ("normal", 1))
    )



class HpnicfDot11CirMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )



class HpnicfDot11SaIntfDevType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("bluetooth", 3),
          ("fixedFreqAudio", 7),
          ("fixedFreqCordlessPhone", 5),
          ("fixedFreqOthers", 4),
          ("fixedFreqVideo", 6),
          ("freqHopperCordlessBase", 9),
          ("freqHopperCordlessNetwork", 10),
          ("freqHopperOthers", 8),
          ("freqHopperXbox", 11),
          ("genericInterferer", 12),
          ("microwave", 1),
          ("microwaveInverter", 2))
    )



class HpnicfDot11TruthValueCM(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dot11false", 0),
          ("dot11true", 1))
    )



# MIB Managed Objects in the order of their OIDs

_HpnicfDot11Common_ObjectIdentity = ObjectIdentity
hpnicfDot11Common = _HpnicfDot11Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12)
)
_HpnicfDot11ElementGroup_ObjectIdentity = ObjectIdentity
hpnicfDot11ElementGroup = _HpnicfDot11ElementGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1)
)
_HpnicfDot11APElementTable_Object = MibTable
hpnicfDot11APElementTable = _HpnicfDot11APElementTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfDot11APElementTable.setStatus("current")
_HpnicfDot11APElementEntry_Object = MibTableRow
hpnicfDot11APElementEntry = _HpnicfDot11APElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 1, 1)
)
hpnicfDot11APElementEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-REF-MIB", "hpnicfDot11APElementIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot11APElementEntry.setStatus("current")
_HpnicfDot11APElementIndex_Type = Integer32
_HpnicfDot11APElementIndex_Object = MibTableColumn
hpnicfDot11APElementIndex = _HpnicfDot11APElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 1, 1, 1),
    _HpnicfDot11APElementIndex_Type()
)
hpnicfDot11APElementIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11APElementIndex.setStatus("current")
_HpnicfDot11APElementTemplateName_Type = OctetString
_HpnicfDot11APElementTemplateName_Object = MibTableColumn
hpnicfDot11APElementTemplateName = _HpnicfDot11APElementTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 1, 1, 2),
    _HpnicfDot11APElementTemplateName_Type()
)
hpnicfDot11APElementTemplateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APElementTemplateName.setStatus("current")
_HpnicfDot11APElementSerialID_Type = OctetString
_HpnicfDot11APElementSerialID_Object = MibTableColumn
hpnicfDot11APElementSerialID = _HpnicfDot11APElementSerialID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 1, 1, 3),
    _HpnicfDot11APElementSerialID_Type()
)
hpnicfDot11APElementSerialID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APElementSerialID.setStatus("current")
_HpnicfDot11APElementModelAlias_Type = OctetString
_HpnicfDot11APElementModelAlias_Object = MibTableColumn
hpnicfDot11APElementModelAlias = _HpnicfDot11APElementModelAlias_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 1, 1, 4),
    _HpnicfDot11APElementModelAlias_Type()
)
hpnicfDot11APElementModelAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11APElementModelAlias.setStatus("current")
_HpnicfDot11RadioElementTable_Object = MibTable
hpnicfDot11RadioElementTable = _HpnicfDot11RadioElementTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioElementTable.setStatus("current")
_HpnicfDot11RadioElementEntry_Object = MibTableRow
hpnicfDot11RadioElementEntry = _HpnicfDot11RadioElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 2, 1)
)
hpnicfDot11RadioElementEntry.setIndexNames(
    (0, "HPN-ICF-DOT11-REF-MIB", "hpnicfDot11APElementIndex"),
    (0, "HPN-ICF-DOT11-REF-MIB", "hpnicfDot11RadioElementRadioNum"),
)
if mibBuilder.loadTexts:
    hpnicfDot11RadioElementEntry.setStatus("current")
_HpnicfDot11RadioElementRadioNum_Type = Unsigned32
_HpnicfDot11RadioElementRadioNum_Object = MibTableColumn
hpnicfDot11RadioElementRadioNum = _HpnicfDot11RadioElementRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 2, 1, 1),
    _HpnicfDot11RadioElementRadioNum_Type()
)
hpnicfDot11RadioElementRadioNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDot11RadioElementRadioNum.setStatus("current")
_HpnicfDot11RadioElementRadioPolicy_Type = OctetString
_HpnicfDot11RadioElementRadioPolicy_Object = MibTableColumn
hpnicfDot11RadioElementRadioPolicy = _HpnicfDot11RadioElementRadioPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 2, 1, 2),
    _HpnicfDot11RadioElementRadioPolicy_Type()
)
hpnicfDot11RadioElementRadioPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDot11RadioElementRadioPolicy.setStatus("current")
_HpnicfDot11RadioElementRadioIndex_Type = Unsigned32
_HpnicfDot11RadioElementRadioIndex_Object = MibTableColumn
hpnicfDot11RadioElementRadioIndex = _HpnicfDot11RadioElementRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 75, 12, 1, 2, 1, 3),
    _HpnicfDot11RadioElementRadioIndex_Type()
)
hpnicfDot11RadioElementRadioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDot11RadioElementRadioIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-DOT11-REF-MIB",
    **{"HpnicfDot11ObjectIDType": HpnicfDot11ObjectIDType,
       "HpnicfDot11RadioScopeType": HpnicfDot11RadioScopeType,
       "HpnicfDot11RadioType": HpnicfDot11RadioType,
       "HpnicfDot11RadioType2": HpnicfDot11RadioType2,
       "HpnicfDot11MACModeType": HpnicfDot11MACModeType,
       "HpnicfDot11ChannelScopeType": HpnicfDot11ChannelScopeType,
       "HpnicfDot11NotifyReasonType": HpnicfDot11NotifyReasonType,
       "HpnicfDot11SSIDStringType": HpnicfDot11SSIDStringType,
       "HpnicfDot11ServicePolicyIDType": HpnicfDot11ServicePolicyIDType,
       "HpnicfDot11SSIDEncryptModeType": HpnicfDot11SSIDEncryptModeType,
       "HpnicfDot11PreambleType": HpnicfDot11PreambleType,
       "HpnicfDot11TxPwrLevelScopeType": HpnicfDot11TxPwrLevelScopeType,
       "HpnicfDot11RFModeType": HpnicfDot11RFModeType,
       "HpnicfDot11TunnelSecSchemType": HpnicfDot11TunnelSecSchemType,
       "HpnicfDot11SecIEStatusType": HpnicfDot11SecIEStatusType,
       "HpnicfDot11CipherType": HpnicfDot11CipherType,
       "HpnicfDot11AuthenType": HpnicfDot11AuthenType,
       "HpnicfDot11AKMType": HpnicfDot11AKMType,
       "HpnicfDot11AssocFailType": HpnicfDot11AssocFailType,
       "HpnicfDot11AuthorFailType": HpnicfDot11AuthorFailType,
       "HpnicfDot11QosAcType": HpnicfDot11QosAcType,
       "HpnicfDot11RadioElementIndex": HpnicfDot11RadioElementIndex,
       "HpnicfDot11WorkMode": HpnicfDot11WorkMode,
       "HpnicfDot11CirMode": HpnicfDot11CirMode,
       "HpnicfDot11SaIntfDevType": HpnicfDot11SaIntfDevType,
       "HpnicfDot11TruthValueCM": HpnicfDot11TruthValueCM,
       "hpnicfDot11": hpnicfDot11,
       "hpnicfDot11Common": hpnicfDot11Common,
       "hpnicfDot11ElementGroup": hpnicfDot11ElementGroup,
       "hpnicfDot11APElementTable": hpnicfDot11APElementTable,
       "hpnicfDot11APElementEntry": hpnicfDot11APElementEntry,
       "hpnicfDot11APElementIndex": hpnicfDot11APElementIndex,
       "hpnicfDot11APElementTemplateName": hpnicfDot11APElementTemplateName,
       "hpnicfDot11APElementSerialID": hpnicfDot11APElementSerialID,
       "hpnicfDot11APElementModelAlias": hpnicfDot11APElementModelAlias,
       "hpnicfDot11RadioElementTable": hpnicfDot11RadioElementTable,
       "hpnicfDot11RadioElementEntry": hpnicfDot11RadioElementEntry,
       "hpnicfDot11RadioElementRadioNum": hpnicfDot11RadioElementRadioNum,
       "hpnicfDot11RadioElementRadioPolicy": hpnicfDot11RadioElementRadioPolicy,
       "hpnicfDot11RadioElementRadioIndex": hpnicfDot11RadioElementRadioIndex}
)
