# SNMP MIB module (HH3C-DOT11-REF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-DOT11-REF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:49 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cDot11 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75)
)
hh3cDot11.setRevisions(
        ("2010-01-07 20:00",
         "2009-05-07 20:00",
         "2007-06-21 20:00",
         "2007-04-27 20:00",
         "2006-05-10 19:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cDot11ObjectIDType(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )



class Hh3cDot11RadioScopeType(Integer32, TextualConvention):
    status = "current"


class Hh3cDot11RadioType(Integer32, TextualConvention):
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



class Hh3cDot11MACModeType(Integer32, TextualConvention):
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



class Hh3cDot11ChannelScopeType(Integer32, TextualConvention):
    status = "current"


class Hh3cDot11NotifyReasonType(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class Hh3cDot11SSIDStringType(OctetString, TextualConvention):
    status = "current"


class Hh3cDot11ServicePolicyIDType(Integer32, TextualConvention):
    status = "current"


class Hh3cDot11SSIDEncryptModeType(Integer32, TextualConvention):
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
          ("wapi", 3))
    )



class Hh3cDot11PreambleType(Integer32, TextualConvention):
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



class Hh3cDot11TxPwrLevelScopeType(Integer32, TextualConvention):
    status = "current"


class Hh3cDot11RFModeType(Integer32, TextualConvention):
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



class Hh3cDot11TunnelSecSchemType(Integer32, TextualConvention):
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



class Hh3cDot11SecIEStatusType(Integer32, TextualConvention):
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
          ("none", 1),
          ("rsn", 2),
          ("wapi", 5),
          ("wpa", 3))
    )



class Hh3cDot11CipherType(Integer32, TextualConvention):
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



class Hh3cDot11AuthenType(Integer32, TextualConvention):
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



class Hh3cDot11AKMType(Integer32, TextualConvention):
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
          ("none", 1),
          ("psk", 2),
          ("wapi", 4))
    )



class Hh3cDot11AssocFailType(Integer32, TextualConvention):
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



class Hh3cDot11AuthorFailType(Integer32, TextualConvention):
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



class Hh3cDot11QosAcType(Integer32, TextualConvention):
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



class Hh3cDot11RadioElementIndex(Unsigned32, TextualConvention):
    status = "current"


class Hh3cDot11WorkMode(Integer32, TextualConvention):
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



class Hh3cDot11CirMode(Integer32, TextualConvention):
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



# MIB Managed Objects in the order of their OIDs

_Hh3cDot11Common_ObjectIdentity = ObjectIdentity
hh3cDot11Common = _Hh3cDot11Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 12)
)
_Hh3cDot11ElementGroup_ObjectIdentity = ObjectIdentity
hh3cDot11ElementGroup = _Hh3cDot11ElementGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1)
)
_Hh3cDot11APElementTable_Object = MibTable
hh3cDot11APElementTable = _Hh3cDot11APElementTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11APElementTable.setStatus("current")
_Hh3cDot11APElementEntry_Object = MibTableRow
hh3cDot11APElementEntry = _Hh3cDot11APElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 1, 1)
)
hh3cDot11APElementEntry.setIndexNames(
    (0, "HH3C-DOT11-REF-MIB", "hh3cDot11APElementIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11APElementEntry.setStatus("current")
_Hh3cDot11APElementIndex_Type = Integer32
_Hh3cDot11APElementIndex_Object = MibTableColumn
hh3cDot11APElementIndex = _Hh3cDot11APElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 1, 1, 1),
    _Hh3cDot11APElementIndex_Type()
)
hh3cDot11APElementIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11APElementIndex.setStatus("current")
_Hh3cDot11APElementTemplateName_Type = OctetString
_Hh3cDot11APElementTemplateName_Object = MibTableColumn
hh3cDot11APElementTemplateName = _Hh3cDot11APElementTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 1, 1, 2),
    _Hh3cDot11APElementTemplateName_Type()
)
hh3cDot11APElementTemplateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APElementTemplateName.setStatus("current")
_Hh3cDot11APElementSerialID_Type = OctetString
_Hh3cDot11APElementSerialID_Object = MibTableColumn
hh3cDot11APElementSerialID = _Hh3cDot11APElementSerialID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 1, 1, 3),
    _Hh3cDot11APElementSerialID_Type()
)
hh3cDot11APElementSerialID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APElementSerialID.setStatus("current")
_Hh3cDot11APElementModelAlias_Type = OctetString
_Hh3cDot11APElementModelAlias_Object = MibTableColumn
hh3cDot11APElementModelAlias = _Hh3cDot11APElementModelAlias_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 1, 1, 4),
    _Hh3cDot11APElementModelAlias_Type()
)
hh3cDot11APElementModelAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APElementModelAlias.setStatus("current")
_Hh3cDot11RadioElementTable_Object = MibTable
hh3cDot11RadioElementTable = _Hh3cDot11RadioElementTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11RadioElementTable.setStatus("current")
_Hh3cDot11RadioElementEntry_Object = MibTableRow
hh3cDot11RadioElementEntry = _Hh3cDot11RadioElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 2, 1)
)
hh3cDot11RadioElementEntry.setIndexNames(
    (0, "HH3C-DOT11-REF-MIB", "hh3cDot11APElementIndex"),
    (0, "HH3C-DOT11-REF-MIB", "hh3cDot11RadioElementRadioNum"),
)
if mibBuilder.loadTexts:
    hh3cDot11RadioElementEntry.setStatus("current")
_Hh3cDot11RadioElementRadioNum_Type = Unsigned32
_Hh3cDot11RadioElementRadioNum_Object = MibTableColumn
hh3cDot11RadioElementRadioNum = _Hh3cDot11RadioElementRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 2, 1, 1),
    _Hh3cDot11RadioElementRadioNum_Type()
)
hh3cDot11RadioElementRadioNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RadioElementRadioNum.setStatus("current")
_Hh3cDot11RadioElementRadioPolicy_Type = OctetString
_Hh3cDot11RadioElementRadioPolicy_Object = MibTableColumn
hh3cDot11RadioElementRadioPolicy = _Hh3cDot11RadioElementRadioPolicy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 2, 1, 2),
    _Hh3cDot11RadioElementRadioPolicy_Type()
)
hh3cDot11RadioElementRadioPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioElementRadioPolicy.setStatus("current")
_Hh3cDot11RadioElementRadioIndex_Type = Unsigned32
_Hh3cDot11RadioElementRadioIndex_Object = MibTableColumn
hh3cDot11RadioElementRadioIndex = _Hh3cDot11RadioElementRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 12, 1, 2, 1, 3),
    _Hh3cDot11RadioElementRadioIndex_Type()
)
hh3cDot11RadioElementRadioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RadioElementRadioIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DOT11-REF-MIB",
    **{"Hh3cDot11ObjectIDType": Hh3cDot11ObjectIDType,
       "Hh3cDot11RadioScopeType": Hh3cDot11RadioScopeType,
       "Hh3cDot11RadioType": Hh3cDot11RadioType,
       "Hh3cDot11MACModeType": Hh3cDot11MACModeType,
       "Hh3cDot11ChannelScopeType": Hh3cDot11ChannelScopeType,
       "Hh3cDot11NotifyReasonType": Hh3cDot11NotifyReasonType,
       "Hh3cDot11SSIDStringType": Hh3cDot11SSIDStringType,
       "Hh3cDot11ServicePolicyIDType": Hh3cDot11ServicePolicyIDType,
       "Hh3cDot11SSIDEncryptModeType": Hh3cDot11SSIDEncryptModeType,
       "Hh3cDot11PreambleType": Hh3cDot11PreambleType,
       "Hh3cDot11TxPwrLevelScopeType": Hh3cDot11TxPwrLevelScopeType,
       "Hh3cDot11RFModeType": Hh3cDot11RFModeType,
       "Hh3cDot11TunnelSecSchemType": Hh3cDot11TunnelSecSchemType,
       "Hh3cDot11SecIEStatusType": Hh3cDot11SecIEStatusType,
       "Hh3cDot11CipherType": Hh3cDot11CipherType,
       "Hh3cDot11AuthenType": Hh3cDot11AuthenType,
       "Hh3cDot11AKMType": Hh3cDot11AKMType,
       "Hh3cDot11AssocFailType": Hh3cDot11AssocFailType,
       "Hh3cDot11AuthorFailType": Hh3cDot11AuthorFailType,
       "Hh3cDot11QosAcType": Hh3cDot11QosAcType,
       "Hh3cDot11RadioElementIndex": Hh3cDot11RadioElementIndex,
       "Hh3cDot11WorkMode": Hh3cDot11WorkMode,
       "Hh3cDot11CirMode": Hh3cDot11CirMode,
       "hh3cDot11": hh3cDot11,
       "hh3cDot11Common": hh3cDot11Common,
       "hh3cDot11ElementGroup": hh3cDot11ElementGroup,
       "hh3cDot11APElementTable": hh3cDot11APElementTable,
       "hh3cDot11APElementEntry": hh3cDot11APElementEntry,
       "hh3cDot11APElementIndex": hh3cDot11APElementIndex,
       "hh3cDot11APElementTemplateName": hh3cDot11APElementTemplateName,
       "hh3cDot11APElementSerialID": hh3cDot11APElementSerialID,
       "hh3cDot11APElementModelAlias": hh3cDot11APElementModelAlias,
       "hh3cDot11RadioElementTable": hh3cDot11RadioElementTable,
       "hh3cDot11RadioElementEntry": hh3cDot11RadioElementEntry,
       "hh3cDot11RadioElementRadioNum": hh3cDot11RadioElementRadioNum,
       "hh3cDot11RadioElementRadioPolicy": hh3cDot11RadioElementRadioPolicy,
       "hh3cDot11RadioElementRadioIndex": hh3cDot11RadioElementRadioIndex}
)
