# SNMP MIB module (A3COM-HUAWEI-DOT11-REF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-DOT11-REF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:35 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

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

h3cDot11 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75)
)
h3cDot11.setRevisions(
        ("2010-01-07 20:00",
         "2009-05-07 20:00",
         "2007-06-21 20:00",
         "2007-04-27 20:00",
         "2006-05-10 19:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cDot11ObjectIDType(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )



class H3cDot11RadioScopeType(Integer32, TextualConvention):
    status = "current"


class H3cDot11RadioType(Integer32, TextualConvention):
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
          ("dot11an", 32),
          ("dot11b", 2),
          ("dot11g", 4),
          ("dot11gn", 16),
          ("dot11n", 8))
    )



class H3cDot11RadioType2(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 1),
          ("dot11an", 8),
          ("dot11b", 2),
          ("dot11g", 4),
          ("dot11gn", 16))
    )



class H3cDot11MACModeType(Integer32, TextualConvention):
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



class H3cDot11ChannelScopeType(Integer32, TextualConvention):
    status = "current"


class H3cDot11NotifyReasonType(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class H3cDot11SSIDStringType(OctetString, TextualConvention):
    status = "current"


class H3cDot11ServicePolicyIDType(Integer32, TextualConvention):
    status = "current"


class H3cDot11SSIDEncryptModeType(Integer32, TextualConvention):
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



class H3cDot11PreambleType(Integer32, TextualConvention):
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



class H3cDot11TxPwrLevelScopeType(Integer32, TextualConvention):
    status = "current"


class H3cDot11RFModeType(Integer32, TextualConvention):
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



class H3cDot11TunnelSecSchemType(Integer32, TextualConvention):
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



class H3cDot11SecIEStatusType(Integer32, TextualConvention):
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



class H3cDot11CipherType(Integer32, TextualConvention):
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



class H3cDot11AuthenType(Integer32, TextualConvention):
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



class H3cDot11AKMType(Integer32, TextualConvention):
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



class H3cDot11AssocFailType(Integer32, TextualConvention):
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



class H3cDot11AuthorFailType(Integer32, TextualConvention):
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



class H3cDot11QosAcType(Integer32, TextualConvention):
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



class H3cDot11RadioElementIndex(Unsigned32, TextualConvention):
    status = "current"


class H3cDot11WorkMode(Integer32, TextualConvention):
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



class H3cDot11CirMode(Integer32, TextualConvention):
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



class H3cDot11SaIntfDevType(Integer32, TextualConvention):
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



# MIB Managed Objects in the order of their OIDs

_H3cDot11Common_ObjectIdentity = ObjectIdentity
h3cDot11Common = _H3cDot11Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 12)
)
_H3cDot11ElementGroup_ObjectIdentity = ObjectIdentity
h3cDot11ElementGroup = _H3cDot11ElementGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 12, 1)
)
_H3cDot11APElementTable_Object = MibTable
h3cDot11APElementTable = _H3cDot11APElementTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 12, 1, 1)
)
if mibBuilder.loadTexts:
    h3cDot11APElementTable.setStatus("current")
_H3cDot11APElementEntry_Object = MibTableRow
h3cDot11APElementEntry = _H3cDot11APElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 12, 1, 1, 1)
)
h3cDot11APElementEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-REF-MIB", "h3cDot11APElementIndex"),
)
if mibBuilder.loadTexts:
    h3cDot11APElementEntry.setStatus("current")
_H3cDot11APElementIndex_Type = Integer32
_H3cDot11APElementIndex_Object = MibTableColumn
h3cDot11APElementIndex = _H3cDot11APElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 12, 1, 1, 1, 1),
    _H3cDot11APElementIndex_Type()
)
h3cDot11APElementIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11APElementIndex.setStatus("current")
_H3cDot11APElementTemplateName_Type = OctetString
_H3cDot11APElementTemplateName_Object = MibTableColumn
h3cDot11APElementTemplateName = _H3cDot11APElementTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 12, 1, 1, 1, 2),
    _H3cDot11APElementTemplateName_Type()
)
h3cDot11APElementTemplateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APElementTemplateName.setStatus("current")
_H3cDot11APElementSerialID_Type = OctetString
_H3cDot11APElementSerialID_Object = MibTableColumn
h3cDot11APElementSerialID = _H3cDot11APElementSerialID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 12, 1, 1, 1, 3),
    _H3cDot11APElementSerialID_Type()
)
h3cDot11APElementSerialID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APElementSerialID.setStatus("current")
_H3cDot11APElementModelAlias_Type = OctetString
_H3cDot11APElementModelAlias_Object = MibTableColumn
h3cDot11APElementModelAlias = _H3cDot11APElementModelAlias_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 12, 1, 1, 1, 4),
    _H3cDot11APElementModelAlias_Type()
)
h3cDot11APElementModelAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11APElementModelAlias.setStatus("current")
_H3cDot11RadioElementTable_Object = MibTable
h3cDot11RadioElementTable = _H3cDot11RadioElementTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 12, 1, 2)
)
if mibBuilder.loadTexts:
    h3cDot11RadioElementTable.setStatus("current")
_H3cDot11RadioElementEntry_Object = MibTableRow
h3cDot11RadioElementEntry = _H3cDot11RadioElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 12, 1, 2, 1)
)
h3cDot11RadioElementEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DOT11-REF-MIB", "h3cDot11APElementIndex"),
    (0, "A3COM-HUAWEI-DOT11-REF-MIB", "h3cDot11RadioElementRadioNum"),
)
if mibBuilder.loadTexts:
    h3cDot11RadioElementEntry.setStatus("current")
_H3cDot11RadioElementRadioNum_Type = Unsigned32
_H3cDot11RadioElementRadioNum_Object = MibTableColumn
h3cDot11RadioElementRadioNum = _H3cDot11RadioElementRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 12, 1, 2, 1, 1),
    _H3cDot11RadioElementRadioNum_Type()
)
h3cDot11RadioElementRadioNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDot11RadioElementRadioNum.setStatus("current")
_H3cDot11RadioElementRadioPolicy_Type = OctetString
_H3cDot11RadioElementRadioPolicy_Object = MibTableColumn
h3cDot11RadioElementRadioPolicy = _H3cDot11RadioElementRadioPolicy_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 12, 1, 2, 1, 2),
    _H3cDot11RadioElementRadioPolicy_Type()
)
h3cDot11RadioElementRadioPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDot11RadioElementRadioPolicy.setStatus("current")
_H3cDot11RadioElementRadioIndex_Type = Unsigned32
_H3cDot11RadioElementRadioIndex_Object = MibTableColumn
h3cDot11RadioElementRadioIndex = _H3cDot11RadioElementRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 75, 12, 1, 2, 1, 3),
    _H3cDot11RadioElementRadioIndex_Type()
)
h3cDot11RadioElementRadioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDot11RadioElementRadioIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-DOT11-REF-MIB",
    **{"H3cDot11ObjectIDType": H3cDot11ObjectIDType,
       "H3cDot11RadioScopeType": H3cDot11RadioScopeType,
       "H3cDot11RadioType": H3cDot11RadioType,
       "H3cDot11RadioType2": H3cDot11RadioType2,
       "H3cDot11MACModeType": H3cDot11MACModeType,
       "H3cDot11ChannelScopeType": H3cDot11ChannelScopeType,
       "H3cDot11NotifyReasonType": H3cDot11NotifyReasonType,
       "H3cDot11SSIDStringType": H3cDot11SSIDStringType,
       "H3cDot11ServicePolicyIDType": H3cDot11ServicePolicyIDType,
       "H3cDot11SSIDEncryptModeType": H3cDot11SSIDEncryptModeType,
       "H3cDot11PreambleType": H3cDot11PreambleType,
       "H3cDot11TxPwrLevelScopeType": H3cDot11TxPwrLevelScopeType,
       "H3cDot11RFModeType": H3cDot11RFModeType,
       "H3cDot11TunnelSecSchemType": H3cDot11TunnelSecSchemType,
       "H3cDot11SecIEStatusType": H3cDot11SecIEStatusType,
       "H3cDot11CipherType": H3cDot11CipherType,
       "H3cDot11AuthenType": H3cDot11AuthenType,
       "H3cDot11AKMType": H3cDot11AKMType,
       "H3cDot11AssocFailType": H3cDot11AssocFailType,
       "H3cDot11AuthorFailType": H3cDot11AuthorFailType,
       "H3cDot11QosAcType": H3cDot11QosAcType,
       "H3cDot11RadioElementIndex": H3cDot11RadioElementIndex,
       "H3cDot11WorkMode": H3cDot11WorkMode,
       "H3cDot11CirMode": H3cDot11CirMode,
       "H3cDot11SaIntfDevType": H3cDot11SaIntfDevType,
       "h3cDot11": h3cDot11,
       "h3cDot11Common": h3cDot11Common,
       "h3cDot11ElementGroup": h3cDot11ElementGroup,
       "h3cDot11APElementTable": h3cDot11APElementTable,
       "h3cDot11APElementEntry": h3cDot11APElementEntry,
       "h3cDot11APElementIndex": h3cDot11APElementIndex,
       "h3cDot11APElementTemplateName": h3cDot11APElementTemplateName,
       "h3cDot11APElementSerialID": h3cDot11APElementSerialID,
       "h3cDot11APElementModelAlias": h3cDot11APElementModelAlias,
       "h3cDot11RadioElementTable": h3cDot11RadioElementTable,
       "h3cDot11RadioElementEntry": h3cDot11RadioElementEntry,
       "h3cDot11RadioElementRadioNum": h3cDot11RadioElementRadioNum,
       "h3cDot11RadioElementRadioPolicy": h3cDot11RadioElementRadioPolicy,
       "h3cDot11RadioElementRadioIndex": h3cDot11RadioElementRadioIndex}
)
