# SNMP MIB module (CISCO-TRUSTSEC-INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-TRUSTSEC-INTERFACE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:48 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CtsSecurityGroupTag,) = mibBuilder.importSymbols(
    "CISCO-TRUSTSEC-TC-MIB",
    "CtsSecurityGroupTag")

(ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifName")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoTrustSecIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 740)
)
ciscoTrustSecIfMIB.setRevisions(
        ("2014-01-28 00:00",
         "2012-04-06 00:00",
         "2010-05-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CtsiCasheDataSource(Integer32, TextualConvention):
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
        *(("acs", 2),
          ("all", 5),
          ("dram", 3),
          ("nvram", 4),
          ("unknown", 1))
    )



class CtsSapNegMode(Integer32, TextualConvention):
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
        *(("encapNoAuthenNoEncrypt", 1),
          ("gcmAuthenGcmEncrypt", 3),
          ("gcmAuthenNoEncrypt", 2),
          ("noEncap", 4))
    )



class CtsSapNegModeList(OctetString, TextualConvention):
    status = "current"


class CtsiInterfaceControllerState(Integer32, TextualConvention):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("authenticating", 3),
          ("authorizing", 4),
          ("disconnecting", 8),
          ("held", 7),
          ("initialize", 2),
          ("invalid", 9),
          ("licenseError", 10),
          ("open", 6),
          ("sapNegotiating", 5),
          ("unknown", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoTrustSecIfMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoTrustSecIfMIBNotifs = _CiscoTrustSecIfMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 0)
)
_CiscoTrustSecIfMIBObjects_ObjectIdentity = ObjectIdentity
ciscoTrustSecIfMIBObjects = _CiscoTrustSecIfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1)
)
_CtsiIfConfigObjects_ObjectIdentity = ObjectIdentity
ctsiIfConfigObjects = _CtsiIfConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 1)
)
_CtsiIfConfigTable_Object = MibTable
ctsiIfConfigTable = _CtsiIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ctsiIfConfigTable.setStatus("current")
_CtsiIfConfigEntry_Object = MibTableRow
ctsiIfConfigEntry = _CtsiIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 1, 1, 1)
)
ctsiIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ctsiIfConfigEntry.setStatus("current")


class _CtsiIfModeCapability_Type(Bits):
    """Custom type ctsiIfModeCapability based on Bits"""
    namedValues = NamedValues(
        *(("dot1x", 0),
          ("l3Forward", 2),
          ("manual", 1))
    )

_CtsiIfModeCapability_Type.__name__ = "Bits"
_CtsiIfModeCapability_Object = MibTableColumn
ctsiIfModeCapability = _CtsiIfModeCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 1, 1, 1, 1),
    _CtsiIfModeCapability_Type()
)
ctsiIfModeCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiIfModeCapability.setStatus("current")


class _CtsiIfConfiguredMode_Type(Integer32):
    """Custom type ctsiIfConfiguredMode based on Integer32"""
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
        *(("dot1x", 3),
          ("l3Forward", 5),
          ("manual", 4),
          ("none", 2),
          ("unknown", 1))
    )


_CtsiIfConfiguredMode_Type.__name__ = "Integer32"
_CtsiIfConfiguredMode_Object = MibTableColumn
ctsiIfConfiguredMode = _CtsiIfConfiguredMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 1, 1, 1, 2),
    _CtsiIfConfiguredMode_Type()
)
ctsiIfConfiguredMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiIfConfiguredMode.setStatus("current")
_CtsiIfCacheClear_Type = TruthValue
_CtsiIfCacheClear_Object = MibTableColumn
ctsiIfCacheClear = _CtsiIfCacheClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 1, 1, 1, 3),
    _CtsiIfCacheClear_Type()
)
ctsiIfCacheClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsiIfCacheClear.setStatus("current")
_CtsiIfRekey_Type = TruthValue
_CtsiIfRekey_Object = MibTableColumn
ctsiIfRekey = _CtsiIfRekey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 1, 1, 1, 4),
    _CtsiIfRekey_Type()
)
ctsiIfRekey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsiIfRekey.setStatus("current")
_CtsiIfDot1xObjects_ObjectIdentity = ObjectIdentity
ctsiIfDot1xObjects = _CtsiIfDot1xObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 2)
)
_CtsiIfDot1xTable_Object = MibTable
ctsiIfDot1xTable = _CtsiIfDot1xTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ctsiIfDot1xTable.setStatus("current")
_CtsiIfDot1xEntry_Object = MibTableRow
ctsiIfDot1xEntry = _CtsiIfDot1xEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 2, 1, 1)
)
ctsiIfDot1xEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ctsiIfDot1xEntry.setStatus("current")


class _CtsiIfDot1xSgtPropagateEnabled_Type(TruthValue):
    """Custom type ctsiIfDot1xSgtPropagateEnabled based on TruthValue"""


_CtsiIfDot1xSgtPropagateEnabled_Object = MibTableColumn
ctsiIfDot1xSgtPropagateEnabled = _CtsiIfDot1xSgtPropagateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 2, 1, 1, 1),
    _CtsiIfDot1xSgtPropagateEnabled_Type()
)
ctsiIfDot1xSgtPropagateEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsiIfDot1xSgtPropagateEnabled.setStatus("current")


class _CtsiIfDot1xReauthInterval_Type(Integer32):
    """Custom type ctsiIfDot1xReauthInterval based on Integer32"""
    defaultValue = 86400


_CtsiIfDot1xReauthInterval_Object = MibTableColumn
ctsiIfDot1xReauthInterval = _CtsiIfDot1xReauthInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 2, 1, 1, 2),
    _CtsiIfDot1xReauthInterval_Type()
)
ctsiIfDot1xReauthInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsiIfDot1xReauthInterval.setStatus("current")
if mibBuilder.loadTexts:
    ctsiIfDot1xReauthInterval.setUnits("seconds")


class _CtsiIfDot1xSapModeList_Type(CtsSapNegModeList):
    """Custom type ctsiIfDot1xSapModeList based on CtsSapNegModeList"""
    defaultHexValue = "04000000"


_CtsiIfDot1xSapModeList_Object = MibTableColumn
ctsiIfDot1xSapModeList = _CtsiIfDot1xSapModeList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 2, 1, 1, 3),
    _CtsiIfDot1xSapModeList_Type()
)
ctsiIfDot1xSapModeList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsiIfDot1xSapModeList.setStatus("current")


class _CtsiIfDot1xDownloadReauthInterval_Type(Integer32):
    """Custom type ctsiIfDot1xDownloadReauthInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_CtsiIfDot1xDownloadReauthInterval_Type.__name__ = "Integer32"
_CtsiIfDot1xDownloadReauthInterval_Object = MibTableColumn
ctsiIfDot1xDownloadReauthInterval = _CtsiIfDot1xDownloadReauthInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 2, 1, 1, 4),
    _CtsiIfDot1xDownloadReauthInterval_Type()
)
ctsiIfDot1xDownloadReauthInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiIfDot1xDownloadReauthInterval.setStatus("current")
if mibBuilder.loadTexts:
    ctsiIfDot1xDownloadReauthInterval.setUnits("seconds")


class _CtsiIfDot1xOperReauthInterval_Type(Integer32):
    """Custom type ctsiIfDot1xOperReauthInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_CtsiIfDot1xOperReauthInterval_Type.__name__ = "Integer32"
_CtsiIfDot1xOperReauthInterval_Object = MibTableColumn
ctsiIfDot1xOperReauthInterval = _CtsiIfDot1xOperReauthInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 2, 1, 1, 5),
    _CtsiIfDot1xOperReauthInterval_Type()
)
ctsiIfDot1xOperReauthInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiIfDot1xOperReauthInterval.setStatus("current")
if mibBuilder.loadTexts:
    ctsiIfDot1xOperReauthInterval.setUnits("seconds")


class _CtsiIfDot1xReauthTimeLeft_Type(Integer32):
    """Custom type ctsiIfDot1xReauthTimeLeft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_CtsiIfDot1xReauthTimeLeft_Type.__name__ = "Integer32"
_CtsiIfDot1xReauthTimeLeft_Object = MibTableColumn
ctsiIfDot1xReauthTimeLeft = _CtsiIfDot1xReauthTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 2, 1, 1, 6),
    _CtsiIfDot1xReauthTimeLeft_Type()
)
ctsiIfDot1xReauthTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiIfDot1xReauthTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    ctsiIfDot1xReauthTimeLeft.setUnits("seconds")


class _CtsiIfDot1xStorageType_Type(StorageType):
    """Custom type ctsiIfDot1xStorageType based on StorageType"""


_CtsiIfDot1xStorageType_Object = MibTableColumn
ctsiIfDot1xStorageType = _CtsiIfDot1xStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 2, 1, 1, 7),
    _CtsiIfDot1xStorageType_Type()
)
ctsiIfDot1xStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsiIfDot1xStorageType.setStatus("current")
_CtsiIfDot1xRowStatus_Type = RowStatus
_CtsiIfDot1xRowStatus_Object = MibTableColumn
ctsiIfDot1xRowStatus = _CtsiIfDot1xRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 2, 1, 1, 8),
    _CtsiIfDot1xRowStatus_Type()
)
ctsiIfDot1xRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsiIfDot1xRowStatus.setStatus("current")
_CtsiIfManualObjects_ObjectIdentity = ObjectIdentity
ctsiIfManualObjects = _CtsiIfManualObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 3)
)
_CtsiIfManualTable_Object = MibTable
ctsiIfManualTable = _CtsiIfManualTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ctsiIfManualTable.setStatus("current")
_CtsiIfManualEntry_Object = MibTableRow
ctsiIfManualEntry = _CtsiIfManualEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 3, 1, 1)
)
ctsiIfManualEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ctsiIfManualEntry.setStatus("current")
_CtsiIfManualDynamicPeerId_Type = SnmpAdminString
_CtsiIfManualDynamicPeerId_Object = MibTableColumn
ctsiIfManualDynamicPeerId = _CtsiIfManualDynamicPeerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 3, 1, 1, 1),
    _CtsiIfManualDynamicPeerId_Type()
)
ctsiIfManualDynamicPeerId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsiIfManualDynamicPeerId.setStatus("current")


class _CtsiIfManualStaticSgt_Type(CtsSecurityGroupTag):
    """Custom type ctsiIfManualStaticSgt based on CtsSecurityGroupTag"""
    defaultValue = 0


_CtsiIfManualStaticSgt_Object = MibTableColumn
ctsiIfManualStaticSgt = _CtsiIfManualStaticSgt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 3, 1, 1, 2),
    _CtsiIfManualStaticSgt_Type()
)
ctsiIfManualStaticSgt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsiIfManualStaticSgt.setStatus("current")


class _CtsiIfManualStaticSgtTrusted_Type(TruthValue):
    """Custom type ctsiIfManualStaticSgtTrusted based on TruthValue"""


_CtsiIfManualStaticSgtTrusted_Object = MibTableColumn
ctsiIfManualStaticSgtTrusted = _CtsiIfManualStaticSgtTrusted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 3, 1, 1, 3),
    _CtsiIfManualStaticSgtTrusted_Type()
)
ctsiIfManualStaticSgtTrusted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsiIfManualStaticSgtTrusted.setStatus("current")


class _CtsiIfManualSgtPropagateEnabled_Type(TruthValue):
    """Custom type ctsiIfManualSgtPropagateEnabled based on TruthValue"""


_CtsiIfManualSgtPropagateEnabled_Object = MibTableColumn
ctsiIfManualSgtPropagateEnabled = _CtsiIfManualSgtPropagateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 3, 1, 1, 4),
    _CtsiIfManualSgtPropagateEnabled_Type()
)
ctsiIfManualSgtPropagateEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsiIfManualSgtPropagateEnabled.setStatus("current")


class _CtsiIfManualSapPmk_Type(OctetString):
    """Custom type ctsiIfManualSapPmk based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(32, 32),
    )


_CtsiIfManualSapPmk_Type.__name__ = "OctetString"
_CtsiIfManualSapPmk_Object = MibTableColumn
ctsiIfManualSapPmk = _CtsiIfManualSapPmk_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 3, 1, 1, 5),
    _CtsiIfManualSapPmk_Type()
)
ctsiIfManualSapPmk.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsiIfManualSapPmk.setStatus("current")
_CtsiIfManualSapModeList_Type = CtsSapNegModeList
_CtsiIfManualSapModeList_Object = MibTableColumn
ctsiIfManualSapModeList = _CtsiIfManualSapModeList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 3, 1, 1, 6),
    _CtsiIfManualSapModeList_Type()
)
ctsiIfManualSapModeList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsiIfManualSapModeList.setStatus("current")


class _CtsiIfManualStorageType_Type(StorageType):
    """Custom type ctsiIfManualStorageType based on StorageType"""


_CtsiIfManualStorageType_Object = MibTableColumn
ctsiIfManualStorageType = _CtsiIfManualStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 3, 1, 1, 7),
    _CtsiIfManualStorageType_Type()
)
ctsiIfManualStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsiIfManualStorageType.setStatus("current")
_CtsiIfManualRowStatus_Type = RowStatus
_CtsiIfManualRowStatus_Object = MibTableColumn
ctsiIfManualRowStatus = _CtsiIfManualRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 3, 1, 1, 8),
    _CtsiIfManualRowStatus_Type()
)
ctsiIfManualRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsiIfManualRowStatus.setStatus("current")
_CtsiIfL3ForwardObjects_ObjectIdentity = ObjectIdentity
ctsiIfL3ForwardObjects = _CtsiIfL3ForwardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 4)
)
_CtsiIfL3ForwardTable_Object = MibTable
ctsiIfL3ForwardTable = _CtsiIfL3ForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ctsiIfL3ForwardTable.setStatus("current")
_CtsiIfL3ForwardEntry_Object = MibTableRow
ctsiIfL3ForwardEntry = _CtsiIfL3ForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 4, 1, 1)
)
ctsiIfL3ForwardEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ctsiIfL3ForwardEntry.setStatus("current")


class _CtsiIfL3ForwardMode_Type(Integer32):
    """Custom type ctsiIfL3ForwardMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("l3IpForward", 3),
          ("l3Ipv4Forward", 1),
          ("l3Ipv6Forward", 2))
    )


_CtsiIfL3ForwardMode_Type.__name__ = "Integer32"
_CtsiIfL3ForwardMode_Object = MibTableColumn
ctsiIfL3ForwardMode = _CtsiIfL3ForwardMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 4, 1, 1, 1),
    _CtsiIfL3ForwardMode_Type()
)
ctsiIfL3ForwardMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsiIfL3ForwardMode.setStatus("current")


class _CtsiIfL3ForwardStorageType_Type(StorageType):
    """Custom type ctsiIfL3ForwardStorageType based on StorageType"""


_CtsiIfL3ForwardStorageType_Object = MibTableColumn
ctsiIfL3ForwardStorageType = _CtsiIfL3ForwardStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 4, 1, 1, 2),
    _CtsiIfL3ForwardStorageType_Type()
)
ctsiIfL3ForwardStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsiIfL3ForwardStorageType.setStatus("current")
_CtsiIfL3ForwardRowStatus_Type = RowStatus
_CtsiIfL3ForwardRowStatus_Object = MibTableColumn
ctsiIfL3ForwardRowStatus = _CtsiIfL3ForwardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 4, 1, 1, 3),
    _CtsiIfL3ForwardRowStatus_Type()
)
ctsiIfL3ForwardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctsiIfL3ForwardRowStatus.setStatus("current")
_CtsiIfStatusObjects_ObjectIdentity = ObjectIdentity
ctsiIfStatusObjects = _CtsiIfStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 5)
)
_CtsiIfStatusTable_Object = MibTable
ctsiIfStatusTable = _CtsiIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ctsiIfStatusTable.setStatus("current")
_CtsiIfStatusEntry_Object = MibTableRow
ctsiIfStatusEntry = _CtsiIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 5, 1, 1)
)
ctsiIfStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ctsiIfStatusEntry.setStatus("current")
_CtsiIfControllerState_Type = CtsiInterfaceControllerState
_CtsiIfControllerState_Object = MibTableColumn
ctsiIfControllerState = _CtsiIfControllerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 5, 1, 1, 1),
    _CtsiIfControllerState_Type()
)
ctsiIfControllerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiIfControllerState.setStatus("current")


class _CtsiIfAuthenticationStatus_Type(Integer32):
    """Custom type ctsiIfAuthenticationStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("failed", 8),
          ("incomplete", 7),
          ("logOff", 4),
          ("noRespond", 5),
          ("notApplicable", 6),
          ("rejected", 3),
          ("succeeded", 2),
          ("unknown", 1))
    )


_CtsiIfAuthenticationStatus_Type.__name__ = "Integer32"
_CtsiIfAuthenticationStatus_Object = MibTableColumn
ctsiIfAuthenticationStatus = _CtsiIfAuthenticationStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 5, 1, 1, 2),
    _CtsiIfAuthenticationStatus_Type()
)
ctsiIfAuthenticationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiIfAuthenticationStatus.setStatus("current")
_CtsiIfPeerId_Type = SnmpAdminString
_CtsiIfPeerId_Object = MibTableColumn
ctsiIfPeerId = _CtsiIfPeerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 5, 1, 1, 3),
    _CtsiIfPeerId_Type()
)
ctsiIfPeerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiIfPeerId.setStatus("current")


class _CtsiIfPeerAdvCapability_Type(Bits):
    """Custom type ctsiIfPeerAdvCapability based on Bits"""
    namedValues = NamedValues(
        ("sap", 0)
    )

_CtsiIfPeerAdvCapability_Type.__name__ = "Bits"
_CtsiIfPeerAdvCapability_Object = MibTableColumn
ctsiIfPeerAdvCapability = _CtsiIfPeerAdvCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 5, 1, 1, 4),
    _CtsiIfPeerAdvCapability_Type()
)
ctsiIfPeerAdvCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiIfPeerAdvCapability.setStatus("current")


class _CtsiIfAuthorizationStatus_Type(Integer32):
    """Custom type ctsiIfAuthorizationStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("failed", 4),
          ("fallBackPolicy", 5),
          ("inProgress", 2),
          ("incomplete", 6),
          ("peerSucceeded", 7),
          ("policySucceeded", 9),
          ("rbaclSucceeded", 8),
          ("succeeded", 3),
          ("unknown", 1))
    )


_CtsiIfAuthorizationStatus_Type.__name__ = "Integer32"
_CtsiIfAuthorizationStatus_Object = MibTableColumn
ctsiIfAuthorizationStatus = _CtsiIfAuthorizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 5, 1, 1, 5),
    _CtsiIfAuthorizationStatus_Type()
)
ctsiIfAuthorizationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiIfAuthorizationStatus.setStatus("current")
_CtsiIfPeerSgt_Type = CtsSecurityGroupTag
_CtsiIfPeerSgt_Object = MibTableColumn
ctsiIfPeerSgt = _CtsiIfPeerSgt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 5, 1, 1, 6),
    _CtsiIfPeerSgt_Type()
)
ctsiIfPeerSgt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiIfPeerSgt.setStatus("current")
_CtsiIfPeerSgtTrusted_Type = TruthValue
_CtsiIfPeerSgtTrusted_Object = MibTableColumn
ctsiIfPeerSgtTrusted = _CtsiIfPeerSgtTrusted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 5, 1, 1, 7),
    _CtsiIfPeerSgtTrusted_Type()
)
ctsiIfPeerSgtTrusted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiIfPeerSgtTrusted.setStatus("current")


class _CtsiIfSapNegotiationStatus_Type(Integer32):
    """Custom type ctsiIfSapNegotiationStatus based on Integer32"""
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
        *(("failed", 5),
          ("inProgress", 3),
          ("licenseError", 6),
          ("notApplicable", 1),
          ("succeeded", 4),
          ("unknown", 2))
    )


_CtsiIfSapNegotiationStatus_Type.__name__ = "Integer32"
_CtsiIfSapNegotiationStatus_Object = MibTableColumn
ctsiIfSapNegotiationStatus = _CtsiIfSapNegotiationStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 5, 1, 1, 8),
    _CtsiIfSapNegotiationStatus_Type()
)
ctsiIfSapNegotiationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiIfSapNegotiationStatus.setStatus("current")
_CtsiIfSapNegModeList_Type = CtsSapNegModeList
_CtsiIfSapNegModeList_Object = MibTableColumn
ctsiIfSapNegModeList = _CtsiIfSapNegModeList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 5, 1, 1, 9),
    _CtsiIfSapNegModeList_Type()
)
ctsiIfSapNegModeList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiIfSapNegModeList.setStatus("current")
_CtsiIfCacheExpirationTime_Type = DateAndTime
_CtsiIfCacheExpirationTime_Object = MibTableColumn
ctsiIfCacheExpirationTime = _CtsiIfCacheExpirationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 5, 1, 1, 10),
    _CtsiIfCacheExpirationTime_Type()
)
ctsiIfCacheExpirationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiIfCacheExpirationTime.setStatus("current")
_CtsiIfCacheDataSource_Type = CtsiCasheDataSource
_CtsiIfCacheDataSource_Object = MibTableColumn
ctsiIfCacheDataSource = _CtsiIfCacheDataSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 5, 1, 1, 11),
    _CtsiIfCacheDataSource_Type()
)
ctsiIfCacheDataSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiIfCacheDataSource.setStatus("current")


class _CtsiIfCriticalAuthStatus_Type(Integer32):
    """Custom type ctsiIfCriticalAuthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cache", 2),
          ("default", 3),
          ("disable", 1))
    )


_CtsiIfCriticalAuthStatus_Type.__name__ = "Integer32"
_CtsiIfCriticalAuthStatus_Object = MibTableColumn
ctsiIfCriticalAuthStatus = _CtsiIfCriticalAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 5, 1, 1, 12),
    _CtsiIfCriticalAuthStatus_Type()
)
ctsiIfCriticalAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiIfCriticalAuthStatus.setStatus("current")
_CtsiIfStatsObjects_ObjectIdentity = ObjectIdentity
ctsiIfStatsObjects = _CtsiIfStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 6)
)
_CtsiIfStatsTable_Object = MibTable
ctsiIfStatsTable = _CtsiIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ctsiIfStatsTable.setStatus("current")
_CtsiIfStatsEntry_Object = MibTableRow
ctsiIfStatsEntry = _CtsiIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 6, 1, 1)
)
ctsiIfStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ctsiIfStatsEntry.setStatus("current")
_CtsiIfAuthenticationSuccess_Type = Counter32
_CtsiIfAuthenticationSuccess_Object = MibTableColumn
ctsiIfAuthenticationSuccess = _CtsiIfAuthenticationSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 6, 1, 1, 1),
    _CtsiIfAuthenticationSuccess_Type()
)
ctsiIfAuthenticationSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiIfAuthenticationSuccess.setStatus("current")
_CtsiIfAuthenticationReject_Type = Counter32
_CtsiIfAuthenticationReject_Object = MibTableColumn
ctsiIfAuthenticationReject = _CtsiIfAuthenticationReject_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 6, 1, 1, 2),
    _CtsiIfAuthenticationReject_Type()
)
ctsiIfAuthenticationReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiIfAuthenticationReject.setStatus("current")
_CtsiIfAuthenticationFailure_Type = Counter32
_CtsiIfAuthenticationFailure_Object = MibTableColumn
ctsiIfAuthenticationFailure = _CtsiIfAuthenticationFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 6, 1, 1, 3),
    _CtsiIfAuthenticationFailure_Type()
)
ctsiIfAuthenticationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiIfAuthenticationFailure.setStatus("current")
_CtsiIfAuthenticationNoResponse_Type = Counter32
_CtsiIfAuthenticationNoResponse_Object = MibTableColumn
ctsiIfAuthenticationNoResponse = _CtsiIfAuthenticationNoResponse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 6, 1, 1, 4),
    _CtsiIfAuthenticationNoResponse_Type()
)
ctsiIfAuthenticationNoResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiIfAuthenticationNoResponse.setStatus("current")
_CtsiIfAuthenticationLogoff_Type = Counter32
_CtsiIfAuthenticationLogoff_Object = MibTableColumn
ctsiIfAuthenticationLogoff = _CtsiIfAuthenticationLogoff_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 6, 1, 1, 5),
    _CtsiIfAuthenticationLogoff_Type()
)
ctsiIfAuthenticationLogoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiIfAuthenticationLogoff.setStatus("current")
_CtsiIfAuthorizationSuccess_Type = Counter32
_CtsiIfAuthorizationSuccess_Object = MibTableColumn
ctsiIfAuthorizationSuccess = _CtsiIfAuthorizationSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 6, 1, 1, 6),
    _CtsiIfAuthorizationSuccess_Type()
)
ctsiIfAuthorizationSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiIfAuthorizationSuccess.setStatus("current")
_CtsiIfAuthorizationPolicyFail_Type = Counter32
_CtsiIfAuthorizationPolicyFail_Object = MibTableColumn
ctsiIfAuthorizationPolicyFail = _CtsiIfAuthorizationPolicyFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 6, 1, 1, 7),
    _CtsiIfAuthorizationPolicyFail_Type()
)
ctsiIfAuthorizationPolicyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiIfAuthorizationPolicyFail.setStatus("current")
_CtsiIfAuthorizationFail_Type = Counter32
_CtsiIfAuthorizationFail_Object = MibTableColumn
ctsiIfAuthorizationFail = _CtsiIfAuthorizationFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 6, 1, 1, 8),
    _CtsiIfAuthorizationFail_Type()
)
ctsiIfAuthorizationFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiIfAuthorizationFail.setStatus("current")
_CtsiIfSapSuccess_Type = Counter32
_CtsiIfSapSuccess_Object = MibTableColumn
ctsiIfSapSuccess = _CtsiIfSapSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 6, 1, 1, 9),
    _CtsiIfSapSuccess_Type()
)
ctsiIfSapSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiIfSapSuccess.setStatus("current")
_CtsiIfSapFail_Type = Counter32
_CtsiIfSapFail_Object = MibTableColumn
ctsiIfSapFail = _CtsiIfSapFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 6, 1, 1, 10),
    _CtsiIfSapFail_Type()
)
ctsiIfSapFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiIfSapFail.setStatus("current")
_CtsiAuthorizationObjects_ObjectIdentity = ObjectIdentity
ctsiAuthorizationObjects = _CtsiAuthorizationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 7)
)
_CtsiAuthorizationTable_Object = MibTable
ctsiAuthorizationTable = _CtsiAuthorizationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 7, 1)
)
if mibBuilder.loadTexts:
    ctsiAuthorizationTable.setStatus("current")
_CtsiAuthorizationEntry_Object = MibTableRow
ctsiAuthorizationEntry = _CtsiAuthorizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 7, 1, 1)
)
ctsiAuthorizationEntry.setIndexNames(
    (1, "CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiAuthorizationPeerId"),
)
if mibBuilder.loadTexts:
    ctsiAuthorizationEntry.setStatus("current")


class _CtsiAuthorizationPeerId_Type(SnmpAdminString):
    """Custom type ctsiAuthorizationPeerId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CtsiAuthorizationPeerId_Type.__name__ = "SnmpAdminString"
_CtsiAuthorizationPeerId_Object = MibTableColumn
ctsiAuthorizationPeerId = _CtsiAuthorizationPeerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 7, 1, 1, 1),
    _CtsiAuthorizationPeerId_Type()
)
ctsiAuthorizationPeerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctsiAuthorizationPeerId.setStatus("current")
_CtsiAuthorizationPeerSgt_Type = CtsSecurityGroupTag
_CtsiAuthorizationPeerSgt_Object = MibTableColumn
ctsiAuthorizationPeerSgt = _CtsiAuthorizationPeerSgt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 7, 1, 1, 2),
    _CtsiAuthorizationPeerSgt_Type()
)
ctsiAuthorizationPeerSgt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiAuthorizationPeerSgt.setStatus("current")


class _CtsiAuthorizationState_Type(Integer32):
    """Custom type ctsiAuthorizationState based on Integer32"""
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
        *(("assessing", 4),
          ("complete", 5),
          ("failure", 6),
          ("start", 2),
          ("unknown", 1),
          ("waitingRespond", 3))
    )


_CtsiAuthorizationState_Type.__name__ = "Integer32"
_CtsiAuthorizationState_Object = MibTableColumn
ctsiAuthorizationState = _CtsiAuthorizationState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 7, 1, 1, 3),
    _CtsiAuthorizationState_Type()
)
ctsiAuthorizationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiAuthorizationState.setStatus("current")
_CtsiAuthorizationLastRefresh_Type = DateAndTime
_CtsiAuthorizationLastRefresh_Object = MibTableColumn
ctsiAuthorizationLastRefresh = _CtsiAuthorizationLastRefresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 7, 1, 1, 4),
    _CtsiAuthorizationLastRefresh_Type()
)
ctsiAuthorizationLastRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiAuthorizationLastRefresh.setStatus("current")


class _CtsiAuthorizationTimeLeft_Type(Integer32):
    """Custom type ctsiAuthorizationTimeLeft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_CtsiAuthorizationTimeLeft_Type.__name__ = "Integer32"
_CtsiAuthorizationTimeLeft_Object = MibTableColumn
ctsiAuthorizationTimeLeft = _CtsiAuthorizationTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 7, 1, 1, 5),
    _CtsiAuthorizationTimeLeft_Type()
)
ctsiAuthorizationTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiAuthorizationTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    ctsiAuthorizationTimeLeft.setUnits("seconds")


class _CtsiAuthorizationTimeToRefresh_Type(Integer32):
    """Custom type ctsiAuthorizationTimeToRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_CtsiAuthorizationTimeToRefresh_Type.__name__ = "Integer32"
_CtsiAuthorizationTimeToRefresh_Object = MibTableColumn
ctsiAuthorizationTimeToRefresh = _CtsiAuthorizationTimeToRefresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 7, 1, 1, 6),
    _CtsiAuthorizationTimeToRefresh_Type()
)
ctsiAuthorizationTimeToRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiAuthorizationTimeToRefresh.setStatus("current")
if mibBuilder.loadTexts:
    ctsiAuthorizationTimeToRefresh.setUnits("seconds")
_CtsiAuthorizationCacheDataSource_Type = CtsiCasheDataSource
_CtsiAuthorizationCacheDataSource_Object = MibTableColumn
ctsiAuthorizationCacheDataSource = _CtsiAuthorizationCacheDataSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 7, 1, 1, 7),
    _CtsiAuthorizationCacheDataSource_Type()
)
ctsiAuthorizationCacheDataSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiAuthorizationCacheDataSource.setStatus("current")


class _CtsiAuthorizationStatus_Type(Integer32):
    """Custom type ctsiAuthorizationStatus based on Integer32"""
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
        *(("failed", 4),
          ("fallbackPolicy", 5),
          ("inProgress", 2),
          ("incomplete", 6),
          ("succeeded", 3),
          ("unknown", 1))
    )


_CtsiAuthorizationStatus_Type.__name__ = "Integer32"
_CtsiAuthorizationStatus_Object = MibTableColumn
ctsiAuthorizationStatus = _CtsiAuthorizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 7, 1, 1, 8),
    _CtsiAuthorizationStatus_Type()
)
ctsiAuthorizationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiAuthorizationStatus.setStatus("current")
_CtsiIfcStatsObjects_ObjectIdentity = ObjectIdentity
ctsiIfcStatsObjects = _CtsiIfcStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 8)
)
_CtsiIfcStatsTable_Object = MibTable
ctsiIfcStatsTable = _CtsiIfcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 8, 1)
)
if mibBuilder.loadTexts:
    ctsiIfcStatsTable.setStatus("current")
_CtsiIfcStatsEntry_Object = MibTableRow
ctsiIfcStatsEntry = _CtsiIfcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 8, 1, 1)
)
ctsiIfcStatsEntry.setIndexNames(
    (0, "CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfcState"),
)
if mibBuilder.loadTexts:
    ctsiIfcStatsEntry.setStatus("current")
_CtsiIfcState_Type = CtsiInterfaceControllerState
_CtsiIfcState_Object = MibTableColumn
ctsiIfcState = _CtsiIfcState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 8, 1, 1, 1),
    _CtsiIfcState_Type()
)
ctsiIfcState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctsiIfcState.setStatus("current")
_CtsiIfcStatsIfCount_Type = Unsigned32
_CtsiIfcStatsIfCount_Object = MibTableColumn
ctsiIfcStatsIfCount = _CtsiIfcStatsIfCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 8, 1, 1, 2),
    _CtsiIfcStatsIfCount_Type()
)
ctsiIfcStatsIfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiIfcStatsIfCount.setStatus("current")
_CtsiEventsStatsObjects_ObjectIdentity = ObjectIdentity
ctsiEventsStatsObjects = _CtsiEventsStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 9)
)
_CtsiAuthenticationSuccess_Type = Counter32
_CtsiAuthenticationSuccess_Object = MibScalar
ctsiAuthenticationSuccess = _CtsiAuthenticationSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 9, 1),
    _CtsiAuthenticationSuccess_Type()
)
ctsiAuthenticationSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiAuthenticationSuccess.setStatus("current")
_CtsiAuthenticationReject_Type = Counter32
_CtsiAuthenticationReject_Object = MibScalar
ctsiAuthenticationReject = _CtsiAuthenticationReject_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 9, 2),
    _CtsiAuthenticationReject_Type()
)
ctsiAuthenticationReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiAuthenticationReject.setStatus("current")
_CtsiAuthenticationFailure_Type = Counter32
_CtsiAuthenticationFailure_Object = MibScalar
ctsiAuthenticationFailure = _CtsiAuthenticationFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 9, 3),
    _CtsiAuthenticationFailure_Type()
)
ctsiAuthenticationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiAuthenticationFailure.setStatus("current")
_CtsiAuthenticationLogoff_Type = Counter32
_CtsiAuthenticationLogoff_Object = MibScalar
ctsiAuthenticationLogoff = _CtsiAuthenticationLogoff_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 9, 4),
    _CtsiAuthenticationLogoff_Type()
)
ctsiAuthenticationLogoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiAuthenticationLogoff.setStatus("current")
_CtsiAuthenticationNoRespond_Type = Counter32
_CtsiAuthenticationNoRespond_Object = MibScalar
ctsiAuthenticationNoRespond = _CtsiAuthenticationNoRespond_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 9, 5),
    _CtsiAuthenticationNoRespond_Type()
)
ctsiAuthenticationNoRespond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiAuthenticationNoRespond.setStatus("current")
_CtsiAuthorizationSuccess_Type = Counter32
_CtsiAuthorizationSuccess_Object = MibScalar
ctsiAuthorizationSuccess = _CtsiAuthorizationSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 9, 6),
    _CtsiAuthorizationSuccess_Type()
)
ctsiAuthorizationSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiAuthorizationSuccess.setStatus("current")
_CtsiAuthorizationFailure_Type = Counter32
_CtsiAuthorizationFailure_Object = MibScalar
ctsiAuthorizationFailure = _CtsiAuthorizationFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 9, 7),
    _CtsiAuthorizationFailure_Type()
)
ctsiAuthorizationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiAuthorizationFailure.setStatus("current")
_CtsiAuthorizationPolicyFailure_Type = Counter32
_CtsiAuthorizationPolicyFailure_Object = MibScalar
ctsiAuthorizationPolicyFailure = _CtsiAuthorizationPolicyFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 9, 8),
    _CtsiAuthorizationPolicyFailure_Type()
)
ctsiAuthorizationPolicyFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiAuthorizationPolicyFailure.setStatus("current")
_CtsiSapNegotiationSuccess_Type = Counter32
_CtsiSapNegotiationSuccess_Object = MibScalar
ctsiSapNegotiationSuccess = _CtsiSapNegotiationSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 9, 9),
    _CtsiSapNegotiationSuccess_Type()
)
ctsiSapNegotiationSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiSapNegotiationSuccess.setStatus("current")
_CtsiSapNegotiationFailure_Type = Counter32
_CtsiSapNegotiationFailure_Object = MibScalar
ctsiSapNegotiationFailure = _CtsiSapNegotiationFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 9, 10),
    _CtsiSapNegotiationFailure_Type()
)
ctsiSapNegotiationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiSapNegotiationFailure.setStatus("current")
_CtsiIfModeStatsObjects_ObjectIdentity = ObjectIdentity
ctsiIfModeStatsObjects = _CtsiIfModeStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 10)
)
_CtsiInDot1xModeIfCount_Type = Unsigned32
_CtsiInDot1xModeIfCount_Object = MibScalar
ctsiInDot1xModeIfCount = _CtsiInDot1xModeIfCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 10, 1),
    _CtsiInDot1xModeIfCount_Type()
)
ctsiInDot1xModeIfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiInDot1xModeIfCount.setStatus("current")
_CtsiInManualModeIfCount_Type = Unsigned32
_CtsiInManualModeIfCount_Object = MibScalar
ctsiInManualModeIfCount = _CtsiInManualModeIfCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 10, 2),
    _CtsiInManualModeIfCount_Type()
)
ctsiInManualModeIfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiInManualModeIfCount.setStatus("current")
_CtsiInL3ForwardModeIfCount_Type = Unsigned32
_CtsiInL3ForwardModeIfCount_Object = MibScalar
ctsiInL3ForwardModeIfCount = _CtsiInL3ForwardModeIfCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 10, 3),
    _CtsiInL3ForwardModeIfCount_Type()
)
ctsiInL3ForwardModeIfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsiInL3ForwardModeIfCount.setStatus("current")
_CtsiIfNotifsControlObjects_ObjectIdentity = ObjectIdentity
ctsiIfNotifsControlObjects = _CtsiIfNotifsControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 11)
)
_CtsiAuthorizationFailNotifEnable_Type = TruthValue
_CtsiAuthorizationFailNotifEnable_Object = MibScalar
ctsiAuthorizationFailNotifEnable = _CtsiAuthorizationFailNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 11, 1),
    _CtsiAuthorizationFailNotifEnable_Type()
)
ctsiAuthorizationFailNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsiAuthorizationFailNotifEnable.setStatus("current")
_CtsiIfAddSupplicantFailNotifEnable_Type = TruthValue
_CtsiIfAddSupplicantFailNotifEnable_Object = MibScalar
ctsiIfAddSupplicantFailNotifEnable = _CtsiIfAddSupplicantFailNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 11, 2),
    _CtsiIfAddSupplicantFailNotifEnable_Type()
)
ctsiIfAddSupplicantFailNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsiIfAddSupplicantFailNotifEnable.setStatus("current")
_CtsiIfAuthenticationFailNotifEnable_Type = TruthValue
_CtsiIfAuthenticationFailNotifEnable_Object = MibScalar
ctsiIfAuthenticationFailNotifEnable = _CtsiIfAuthenticationFailNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 11, 3),
    _CtsiIfAuthenticationFailNotifEnable_Type()
)
ctsiIfAuthenticationFailNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsiIfAuthenticationFailNotifEnable.setStatus("current")
_CtsiIfSapNegotiationFailNotifEnable_Type = TruthValue
_CtsiIfSapNegotiationFailNotifEnable_Object = MibScalar
ctsiIfSapNegotiationFailNotifEnable = _CtsiIfSapNegotiationFailNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 11, 4),
    _CtsiIfSapNegotiationFailNotifEnable_Type()
)
ctsiIfSapNegotiationFailNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsiIfSapNegotiationFailNotifEnable.setStatus("current")
_CtsiIfUnauthorizedNotifEnable_Type = TruthValue
_CtsiIfUnauthorizedNotifEnable_Object = MibScalar
ctsiIfUnauthorizedNotifEnable = _CtsiIfUnauthorizedNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 11, 5),
    _CtsiIfUnauthorizedNotifEnable_Type()
)
ctsiIfUnauthorizedNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsiIfUnauthorizedNotifEnable.setStatus("current")
_CtsiIfNotifsOnlyInfoObjects_ObjectIdentity = ObjectIdentity
ctsiIfNotifsOnlyInfoObjects = _CtsiIfNotifsOnlyInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 12)
)
_CtsiIfNotifMessage_Type = SnmpAdminString
_CtsiIfNotifMessage_Object = MibScalar
ctsiIfNotifMessage = _CtsiIfNotifMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 12, 1),
    _CtsiIfNotifMessage_Type()
)
ctsiIfNotifMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ctsiIfNotifMessage.setStatus("current")


class _CtsiIfDot1xPaeRole_Type(Integer32):
    """Custom type ctsiIfDot1xPaeRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authenticator", 2),
          ("notApplicable", 1),
          ("supplicant", 3))
    )


_CtsiIfDot1xPaeRole_Type.__name__ = "Integer32"
_CtsiIfDot1xPaeRole_Object = MibScalar
ctsiIfDot1xPaeRole = _CtsiIfDot1xPaeRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 1, 12, 2),
    _CtsiIfDot1xPaeRole_Type()
)
ctsiIfDot1xPaeRole.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ctsiIfDot1xPaeRole.setStatus("current")
_CiscoTrustSecIfMIBConform_ObjectIdentity = ObjectIdentity
ciscoTrustSecIfMIBConform = _CiscoTrustSecIfMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 2)
)
_CiscoTrustSecIfMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoTrustSecIfMIBCompliances = _CiscoTrustSecIfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 2, 1)
)
_CiscoTrustSecIfMIBGroups_ObjectIdentity = ObjectIdentity
ciscoTrustSecIfMIBGroups = _CiscoTrustSecIfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 2, 2)
)

# Managed Objects groups

ciscoTrustSecIfMIBIfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 2, 2, 1)
)
ciscoTrustSecIfMIBIfConfigGroup.setObjects(
      *(("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfModeCapability"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfConfiguredMode"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfCacheClear"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfRekey"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecIfMIBIfConfigGroup.setStatus("current")

ciscoTrustSecIfMIBDot1xGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 2, 2, 2)
)
ciscoTrustSecIfMIBDot1xGroup.setObjects(
      *(("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfDot1xSgtPropagateEnabled"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfDot1xReauthInterval"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfDot1xSapModeList"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfDot1xDownloadReauthInterval"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfDot1xOperReauthInterval"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfDot1xReauthTimeLeft"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfDot1xStorageType"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfDot1xRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecIfMIBDot1xGroup.setStatus("current")

ciscoTrustSecIfMIBManualGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 2, 2, 3)
)
ciscoTrustSecIfMIBManualGroup.setObjects(
      *(("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfManualDynamicPeerId"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfManualStaticSgt"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfManualStaticSgtTrusted"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfManualSgtPropagateEnabled"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfManualSapPmk"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfManualSapModeList"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfManualStorageType"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfManualRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecIfMIBManualGroup.setStatus("current")

ciscoTrustSecIfMIBL3ForwardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 2, 2, 4)
)
ciscoTrustSecIfMIBL3ForwardGroup.setObjects(
      *(("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfL3ForwardMode"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfL3ForwardStorageType"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfL3ForwardRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecIfMIBL3ForwardGroup.setStatus("current")

ciscoTrustSecIfMIBStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 2, 2, 5)
)
ciscoTrustSecIfMIBStatusGroup.setObjects(
      *(("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfControllerState"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfAuthenticationStatus"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfPeerId"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfPeerAdvCapability"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfAuthorizationStatus"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfPeerSgt"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfPeerSgtTrusted"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfCacheExpirationTime"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfCacheDataSource"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfSapNegotiationStatus"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfSapNegModeList"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecIfMIBStatusGroup.setStatus("current")

ciscoTrustSecIfMIBStatisticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 2, 2, 6)
)
ciscoTrustSecIfMIBStatisticGroup.setObjects(
      *(("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfAuthenticationSuccess"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfAuthenticationReject"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfAuthenticationFailure"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfAuthenticationNoResponse"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfAuthenticationLogoff"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfAuthorizationSuccess"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfAuthorizationPolicyFail"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfAuthorizationFail"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfSapSuccess"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfSapFail"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecIfMIBStatisticGroup.setStatus("current")

ciscoTrustSecIfMIBAuthorizationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 2, 2, 7)
)
ciscoTrustSecIfMIBAuthorizationGroup.setObjects(
      *(("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiAuthorizationPeerSgt"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiAuthorizationState"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiAuthorizationLastRefresh"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiAuthorizationTimeLeft"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiAuthorizationTimeToRefresh"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiAuthorizationCacheDataSource"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiAuthorizationStatus"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecIfMIBAuthorizationGroup.setStatus("current")

ciscoTrustSecIfMIBIfcStatisticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 2, 2, 8)
)
ciscoTrustSecIfMIBIfcStatisticGroup.setObjects(
    ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfcStatsIfCount")
)
if mibBuilder.loadTexts:
    ciscoTrustSecIfMIBIfcStatisticGroup.setStatus("current")

ciscoTrustSecIfMIBEventStatisticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 2, 2, 9)
)
ciscoTrustSecIfMIBEventStatisticGroup.setObjects(
      *(("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiAuthenticationSuccess"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiAuthenticationReject"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiAuthenticationFailure"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiAuthenticationLogoff"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiAuthenticationNoRespond"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiAuthorizationSuccess"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiAuthorizationFailure"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiAuthorizationPolicyFailure"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiSapNegotiationSuccess"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiSapNegotiationFailure"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecIfMIBEventStatisticGroup.setStatus("current")

ciscoTrustSecIfMIBIfModeStatisticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 2, 2, 10)
)
ciscoTrustSecIfMIBIfModeStatisticGroup.setObjects(
      *(("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiInDot1xModeIfCount"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiInManualModeIfCount"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiInL3ForwardModeIfCount"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecIfMIBIfModeStatisticGroup.setStatus("current")

ciscoTrustSecIfMIBNotifsCtrlGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 2, 2, 11)
)
ciscoTrustSecIfMIBNotifsCtrlGrp.setObjects(
      *(("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiAuthorizationFailNotifEnable"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfAddSupplicantFailNotifEnable"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfAuthenticationFailNotifEnable"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfSapNegotiationFailNotifEnable"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfUnauthorizedNotifEnable"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecIfMIBNotifsCtrlGrp.setStatus("current")

ciscoTrustSecIfMIBNotifsOnlyInfoGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 2, 2, 12)
)
ciscoTrustSecIfMIBNotifsOnlyInfoGrp.setObjects(
      *(("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfNotifMessage"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfDot1xPaeRole"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecIfMIBNotifsOnlyInfoGrp.setStatus("current")

ciscoTrustSecIfMIBCriticalAuthStatusGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 2, 2, 14)
)
ciscoTrustSecIfMIBCriticalAuthStatusGrp.setObjects(
    ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfCriticalAuthStatus")
)
if mibBuilder.loadTexts:
    ciscoTrustSecIfMIBCriticalAuthStatusGrp.setStatus("current")


# Notification objects

ctsiAuthorizationFailNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 0, 1)
)
ctsiAuthorizationFailNotif.setObjects(
    ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiAuthorizationPeerSgt")
)
if mibBuilder.loadTexts:
    ctsiAuthorizationFailNotif.setStatus(
        "current"
    )

ctsiIfAddSupplicantFailNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 0, 2)
)
ctsiIfAddSupplicantFailNotif.setObjects(
    ("IF-MIB", "ifName")
)
if mibBuilder.loadTexts:
    ctsiIfAddSupplicantFailNotif.setStatus(
        "current"
    )

ctsiIfAuthenticationFailNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 0, 3)
)
ctsiIfAuthenticationFailNotif.setObjects(
      *(("IF-MIB", "ifName"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfPeerId"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfDot1xPaeRole"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfAuthenticationStatus"))
)
if mibBuilder.loadTexts:
    ctsiIfAuthenticationFailNotif.setStatus(
        "current"
    )

ctsiIfSapNegotiationFailNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 0, 4)
)
ctsiIfSapNegotiationFailNotif.setObjects(
      *(("IF-MIB", "ifName"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfNotifMessage"))
)
if mibBuilder.loadTexts:
    ctsiIfSapNegotiationFailNotif.setStatus(
        "current"
    )

ctsiIfUnauthorizedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 0, 5)
)
ctsiIfUnauthorizedNotif.setObjects(
    ("IF-MIB", "ifName")
)
if mibBuilder.loadTexts:
    ctsiIfUnauthorizedNotif.setStatus(
        "current"
    )


# Notifications groups

ciscoTrustSecIfMIBNotifsGrp = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 2, 2, 13)
)
ciscoTrustSecIfMIBNotifsGrp.setObjects(
      *(("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiAuthorizationFailNotif"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfAddSupplicantFailNotif"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfAuthenticationFailNotif"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfSapNegotiationFailNotif"),
        ("CISCO-TRUSTSEC-INTERFACE-MIB", "ctsiIfUnauthorizedNotif"))
)
if mibBuilder.loadTexts:
    ciscoTrustSecIfMIBNotifsGrp.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoTrustSecIfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoTrustSecIfMIBCompliance.setStatus(
        "deprecated"
    )

ciscoTrustSecIfMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoTrustSecIfMIBCompliance2.setStatus(
        "deprecated"
    )

ciscoTrustSecIfMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 740, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoTrustSecIfMIBCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-TRUSTSEC-INTERFACE-MIB",
    **{"CtsiCasheDataSource": CtsiCasheDataSource,
       "CtsSapNegMode": CtsSapNegMode,
       "CtsSapNegModeList": CtsSapNegModeList,
       "CtsiInterfaceControllerState": CtsiInterfaceControllerState,
       "ciscoTrustSecIfMIB": ciscoTrustSecIfMIB,
       "ciscoTrustSecIfMIBNotifs": ciscoTrustSecIfMIBNotifs,
       "ctsiAuthorizationFailNotif": ctsiAuthorizationFailNotif,
       "ctsiIfAddSupplicantFailNotif": ctsiIfAddSupplicantFailNotif,
       "ctsiIfAuthenticationFailNotif": ctsiIfAuthenticationFailNotif,
       "ctsiIfSapNegotiationFailNotif": ctsiIfSapNegotiationFailNotif,
       "ctsiIfUnauthorizedNotif": ctsiIfUnauthorizedNotif,
       "ciscoTrustSecIfMIBObjects": ciscoTrustSecIfMIBObjects,
       "ctsiIfConfigObjects": ctsiIfConfigObjects,
       "ctsiIfConfigTable": ctsiIfConfigTable,
       "ctsiIfConfigEntry": ctsiIfConfigEntry,
       "ctsiIfModeCapability": ctsiIfModeCapability,
       "ctsiIfConfiguredMode": ctsiIfConfiguredMode,
       "ctsiIfCacheClear": ctsiIfCacheClear,
       "ctsiIfRekey": ctsiIfRekey,
       "ctsiIfDot1xObjects": ctsiIfDot1xObjects,
       "ctsiIfDot1xTable": ctsiIfDot1xTable,
       "ctsiIfDot1xEntry": ctsiIfDot1xEntry,
       "ctsiIfDot1xSgtPropagateEnabled": ctsiIfDot1xSgtPropagateEnabled,
       "ctsiIfDot1xReauthInterval": ctsiIfDot1xReauthInterval,
       "ctsiIfDot1xSapModeList": ctsiIfDot1xSapModeList,
       "ctsiIfDot1xDownloadReauthInterval": ctsiIfDot1xDownloadReauthInterval,
       "ctsiIfDot1xOperReauthInterval": ctsiIfDot1xOperReauthInterval,
       "ctsiIfDot1xReauthTimeLeft": ctsiIfDot1xReauthTimeLeft,
       "ctsiIfDot1xStorageType": ctsiIfDot1xStorageType,
       "ctsiIfDot1xRowStatus": ctsiIfDot1xRowStatus,
       "ctsiIfManualObjects": ctsiIfManualObjects,
       "ctsiIfManualTable": ctsiIfManualTable,
       "ctsiIfManualEntry": ctsiIfManualEntry,
       "ctsiIfManualDynamicPeerId": ctsiIfManualDynamicPeerId,
       "ctsiIfManualStaticSgt": ctsiIfManualStaticSgt,
       "ctsiIfManualStaticSgtTrusted": ctsiIfManualStaticSgtTrusted,
       "ctsiIfManualSgtPropagateEnabled": ctsiIfManualSgtPropagateEnabled,
       "ctsiIfManualSapPmk": ctsiIfManualSapPmk,
       "ctsiIfManualSapModeList": ctsiIfManualSapModeList,
       "ctsiIfManualStorageType": ctsiIfManualStorageType,
       "ctsiIfManualRowStatus": ctsiIfManualRowStatus,
       "ctsiIfL3ForwardObjects": ctsiIfL3ForwardObjects,
       "ctsiIfL3ForwardTable": ctsiIfL3ForwardTable,
       "ctsiIfL3ForwardEntry": ctsiIfL3ForwardEntry,
       "ctsiIfL3ForwardMode": ctsiIfL3ForwardMode,
       "ctsiIfL3ForwardStorageType": ctsiIfL3ForwardStorageType,
       "ctsiIfL3ForwardRowStatus": ctsiIfL3ForwardRowStatus,
       "ctsiIfStatusObjects": ctsiIfStatusObjects,
       "ctsiIfStatusTable": ctsiIfStatusTable,
       "ctsiIfStatusEntry": ctsiIfStatusEntry,
       "ctsiIfControllerState": ctsiIfControllerState,
       "ctsiIfAuthenticationStatus": ctsiIfAuthenticationStatus,
       "ctsiIfPeerId": ctsiIfPeerId,
       "ctsiIfPeerAdvCapability": ctsiIfPeerAdvCapability,
       "ctsiIfAuthorizationStatus": ctsiIfAuthorizationStatus,
       "ctsiIfPeerSgt": ctsiIfPeerSgt,
       "ctsiIfPeerSgtTrusted": ctsiIfPeerSgtTrusted,
       "ctsiIfSapNegotiationStatus": ctsiIfSapNegotiationStatus,
       "ctsiIfSapNegModeList": ctsiIfSapNegModeList,
       "ctsiIfCacheExpirationTime": ctsiIfCacheExpirationTime,
       "ctsiIfCacheDataSource": ctsiIfCacheDataSource,
       "ctsiIfCriticalAuthStatus": ctsiIfCriticalAuthStatus,
       "ctsiIfStatsObjects": ctsiIfStatsObjects,
       "ctsiIfStatsTable": ctsiIfStatsTable,
       "ctsiIfStatsEntry": ctsiIfStatsEntry,
       "ctsiIfAuthenticationSuccess": ctsiIfAuthenticationSuccess,
       "ctsiIfAuthenticationReject": ctsiIfAuthenticationReject,
       "ctsiIfAuthenticationFailure": ctsiIfAuthenticationFailure,
       "ctsiIfAuthenticationNoResponse": ctsiIfAuthenticationNoResponse,
       "ctsiIfAuthenticationLogoff": ctsiIfAuthenticationLogoff,
       "ctsiIfAuthorizationSuccess": ctsiIfAuthorizationSuccess,
       "ctsiIfAuthorizationPolicyFail": ctsiIfAuthorizationPolicyFail,
       "ctsiIfAuthorizationFail": ctsiIfAuthorizationFail,
       "ctsiIfSapSuccess": ctsiIfSapSuccess,
       "ctsiIfSapFail": ctsiIfSapFail,
       "ctsiAuthorizationObjects": ctsiAuthorizationObjects,
       "ctsiAuthorizationTable": ctsiAuthorizationTable,
       "ctsiAuthorizationEntry": ctsiAuthorizationEntry,
       "ctsiAuthorizationPeerId": ctsiAuthorizationPeerId,
       "ctsiAuthorizationPeerSgt": ctsiAuthorizationPeerSgt,
       "ctsiAuthorizationState": ctsiAuthorizationState,
       "ctsiAuthorizationLastRefresh": ctsiAuthorizationLastRefresh,
       "ctsiAuthorizationTimeLeft": ctsiAuthorizationTimeLeft,
       "ctsiAuthorizationTimeToRefresh": ctsiAuthorizationTimeToRefresh,
       "ctsiAuthorizationCacheDataSource": ctsiAuthorizationCacheDataSource,
       "ctsiAuthorizationStatus": ctsiAuthorizationStatus,
       "ctsiIfcStatsObjects": ctsiIfcStatsObjects,
       "ctsiIfcStatsTable": ctsiIfcStatsTable,
       "ctsiIfcStatsEntry": ctsiIfcStatsEntry,
       "ctsiIfcState": ctsiIfcState,
       "ctsiIfcStatsIfCount": ctsiIfcStatsIfCount,
       "ctsiEventsStatsObjects": ctsiEventsStatsObjects,
       "ctsiAuthenticationSuccess": ctsiAuthenticationSuccess,
       "ctsiAuthenticationReject": ctsiAuthenticationReject,
       "ctsiAuthenticationFailure": ctsiAuthenticationFailure,
       "ctsiAuthenticationLogoff": ctsiAuthenticationLogoff,
       "ctsiAuthenticationNoRespond": ctsiAuthenticationNoRespond,
       "ctsiAuthorizationSuccess": ctsiAuthorizationSuccess,
       "ctsiAuthorizationFailure": ctsiAuthorizationFailure,
       "ctsiAuthorizationPolicyFailure": ctsiAuthorizationPolicyFailure,
       "ctsiSapNegotiationSuccess": ctsiSapNegotiationSuccess,
       "ctsiSapNegotiationFailure": ctsiSapNegotiationFailure,
       "ctsiIfModeStatsObjects": ctsiIfModeStatsObjects,
       "ctsiInDot1xModeIfCount": ctsiInDot1xModeIfCount,
       "ctsiInManualModeIfCount": ctsiInManualModeIfCount,
       "ctsiInL3ForwardModeIfCount": ctsiInL3ForwardModeIfCount,
       "ctsiIfNotifsControlObjects": ctsiIfNotifsControlObjects,
       "ctsiAuthorizationFailNotifEnable": ctsiAuthorizationFailNotifEnable,
       "ctsiIfAddSupplicantFailNotifEnable": ctsiIfAddSupplicantFailNotifEnable,
       "ctsiIfAuthenticationFailNotifEnable": ctsiIfAuthenticationFailNotifEnable,
       "ctsiIfSapNegotiationFailNotifEnable": ctsiIfSapNegotiationFailNotifEnable,
       "ctsiIfUnauthorizedNotifEnable": ctsiIfUnauthorizedNotifEnable,
       "ctsiIfNotifsOnlyInfoObjects": ctsiIfNotifsOnlyInfoObjects,
       "ctsiIfNotifMessage": ctsiIfNotifMessage,
       "ctsiIfDot1xPaeRole": ctsiIfDot1xPaeRole,
       "ciscoTrustSecIfMIBConform": ciscoTrustSecIfMIBConform,
       "ciscoTrustSecIfMIBCompliances": ciscoTrustSecIfMIBCompliances,
       "ciscoTrustSecIfMIBCompliance": ciscoTrustSecIfMIBCompliance,
       "ciscoTrustSecIfMIBCompliance2": ciscoTrustSecIfMIBCompliance2,
       "ciscoTrustSecIfMIBCompliance3": ciscoTrustSecIfMIBCompliance3,
       "ciscoTrustSecIfMIBGroups": ciscoTrustSecIfMIBGroups,
       "ciscoTrustSecIfMIBIfConfigGroup": ciscoTrustSecIfMIBIfConfigGroup,
       "ciscoTrustSecIfMIBDot1xGroup": ciscoTrustSecIfMIBDot1xGroup,
       "ciscoTrustSecIfMIBManualGroup": ciscoTrustSecIfMIBManualGroup,
       "ciscoTrustSecIfMIBL3ForwardGroup": ciscoTrustSecIfMIBL3ForwardGroup,
       "ciscoTrustSecIfMIBStatusGroup": ciscoTrustSecIfMIBStatusGroup,
       "ciscoTrustSecIfMIBStatisticGroup": ciscoTrustSecIfMIBStatisticGroup,
       "ciscoTrustSecIfMIBAuthorizationGroup": ciscoTrustSecIfMIBAuthorizationGroup,
       "ciscoTrustSecIfMIBIfcStatisticGroup": ciscoTrustSecIfMIBIfcStatisticGroup,
       "ciscoTrustSecIfMIBEventStatisticGroup": ciscoTrustSecIfMIBEventStatisticGroup,
       "ciscoTrustSecIfMIBIfModeStatisticGroup": ciscoTrustSecIfMIBIfModeStatisticGroup,
       "ciscoTrustSecIfMIBNotifsCtrlGrp": ciscoTrustSecIfMIBNotifsCtrlGrp,
       "ciscoTrustSecIfMIBNotifsOnlyInfoGrp": ciscoTrustSecIfMIBNotifsOnlyInfoGrp,
       "ciscoTrustSecIfMIBNotifsGrp": ciscoTrustSecIfMIBNotifsGrp,
       "ciscoTrustSecIfMIBCriticalAuthStatusGrp": ciscoTrustSecIfMIBCriticalAuthStatusGrp}
)
