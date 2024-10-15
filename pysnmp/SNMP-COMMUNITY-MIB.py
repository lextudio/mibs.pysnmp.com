# SNMP MIB module (SNMP-COMMUNITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SNMP-COMMUNITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:14:52 2024
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

(SnmpAdminString,
 SnmpEngineID) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString",
    "SnmpEngineID")

(SnmpTagValue,
 snmpTargetAddrEntry) = mibBuilder.importSymbols(
    "SNMP-TARGET-MIB",
    "SnmpTagValue",
    "snmpTargetAddrEntry")

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
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

snmpCommunityMIB = ModuleIdentity(
    (1, 3, 6, 1, 6, 3, 18)
)
snmpCommunityMIB.setRevisions(
        ("2003-08-06 00:00",
         "2000-03-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnmpCommunityMIBObjects_ObjectIdentity = ObjectIdentity
snmpCommunityMIBObjects = _SnmpCommunityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 18, 1)
)
_SnmpCommunityTable_Object = MibTable
snmpCommunityTable = _SnmpCommunityTable_Object(
    (1, 3, 6, 1, 6, 3, 18, 1, 1)
)
if mibBuilder.loadTexts:
    snmpCommunityTable.setStatus("current")
_SnmpCommunityEntry_Object = MibTableRow
snmpCommunityEntry = _SnmpCommunityEntry_Object(
    (1, 3, 6, 1, 6, 3, 18, 1, 1, 1)
)
snmpCommunityEntry.setIndexNames(
    (1, "SNMP-COMMUNITY-MIB", "snmpCommunityIndex"),
)
if mibBuilder.loadTexts:
    snmpCommunityEntry.setStatus("current")


class _SnmpCommunityIndex_Type(SnmpAdminString):
    """Custom type snmpCommunityIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpCommunityIndex_Type.__name__ = "SnmpAdminString"
_SnmpCommunityIndex_Object = MibTableColumn
snmpCommunityIndex = _SnmpCommunityIndex_Object(
    (1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 1),
    _SnmpCommunityIndex_Type()
)
snmpCommunityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpCommunityIndex.setStatus("current")
_SnmpCommunityName_Type = OctetString
_SnmpCommunityName_Object = MibTableColumn
snmpCommunityName = _SnmpCommunityName_Object(
    (1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 2),
    _SnmpCommunityName_Type()
)
snmpCommunityName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpCommunityName.setStatus("current")


class _SnmpCommunitySecurityName_Type(SnmpAdminString):
    """Custom type snmpCommunitySecurityName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SnmpCommunitySecurityName_Type.__name__ = "SnmpAdminString"
_SnmpCommunitySecurityName_Object = MibTableColumn
snmpCommunitySecurityName = _SnmpCommunitySecurityName_Object(
    (1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 3),
    _SnmpCommunitySecurityName_Type()
)
snmpCommunitySecurityName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpCommunitySecurityName.setStatus("current")
_SnmpCommunityContextEngineID_Type = SnmpEngineID
_SnmpCommunityContextEngineID_Object = MibTableColumn
snmpCommunityContextEngineID = _SnmpCommunityContextEngineID_Object(
    (1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 4),
    _SnmpCommunityContextEngineID_Type()
)
snmpCommunityContextEngineID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpCommunityContextEngineID.setStatus("current")


class _SnmpCommunityContextName_Type(SnmpAdminString):
    """Custom type snmpCommunityContextName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpCommunityContextName_Type.__name__ = "SnmpAdminString"
_SnmpCommunityContextName_Object = MibTableColumn
snmpCommunityContextName = _SnmpCommunityContextName_Object(
    (1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 5),
    _SnmpCommunityContextName_Type()
)
snmpCommunityContextName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpCommunityContextName.setStatus("current")


class _SnmpCommunityTransportTag_Type(SnmpTagValue):
    """Custom type snmpCommunityTransportTag based on SnmpTagValue"""
    defaultHexValue = ""


_SnmpCommunityTransportTag_Object = MibTableColumn
snmpCommunityTransportTag = _SnmpCommunityTransportTag_Object(
    (1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 6),
    _SnmpCommunityTransportTag_Type()
)
snmpCommunityTransportTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpCommunityTransportTag.setStatus("current")
_SnmpCommunityStorageType_Type = StorageType
_SnmpCommunityStorageType_Object = MibTableColumn
snmpCommunityStorageType = _SnmpCommunityStorageType_Object(
    (1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 7),
    _SnmpCommunityStorageType_Type()
)
snmpCommunityStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpCommunityStorageType.setStatus("current")
_SnmpCommunityStatus_Type = RowStatus
_SnmpCommunityStatus_Object = MibTableColumn
snmpCommunityStatus = _SnmpCommunityStatus_Object(
    (1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 8),
    _SnmpCommunityStatus_Type()
)
snmpCommunityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpCommunityStatus.setStatus("current")
_SnmpTargetAddrExtTable_Object = MibTable
snmpTargetAddrExtTable = _SnmpTargetAddrExtTable_Object(
    (1, 3, 6, 1, 6, 3, 18, 1, 2)
)
if mibBuilder.loadTexts:
    snmpTargetAddrExtTable.setStatus("current")
_SnmpTargetAddrExtEntry_Object = MibTableRow
snmpTargetAddrExtEntry = _SnmpTargetAddrExtEntry_Object(
    (1, 3, 6, 1, 6, 3, 18, 1, 2, 1)
)
if mibBuilder.loadTexts:
    snmpTargetAddrExtEntry.setStatus("current")


class _SnmpTargetAddrTMask_Type(OctetString):
    """Custom type snmpTargetAddrTMask based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnmpTargetAddrTMask_Type.__name__ = "OctetString"
_SnmpTargetAddrTMask_Object = MibTableColumn
snmpTargetAddrTMask = _SnmpTargetAddrTMask_Object(
    (1, 3, 6, 1, 6, 3, 18, 1, 2, 1, 1),
    _SnmpTargetAddrTMask_Type()
)
snmpTargetAddrTMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTargetAddrTMask.setStatus("current")


class _SnmpTargetAddrMMS_Type(Integer32):
    """Custom type snmpTargetAddrMMS based on Integer32"""
    defaultValue = 484

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(484, 2147483647),
    )


_SnmpTargetAddrMMS_Type.__name__ = "Integer32"
_SnmpTargetAddrMMS_Object = MibTableColumn
snmpTargetAddrMMS = _SnmpTargetAddrMMS_Object(
    (1, 3, 6, 1, 6, 3, 18, 1, 2, 1, 2),
    _SnmpTargetAddrMMS_Type()
)
snmpTargetAddrMMS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTargetAddrMMS.setStatus("current")
_SnmpTrapAddress_Type = IpAddress
_SnmpTrapAddress_Object = MibScalar
snmpTrapAddress = _SnmpTrapAddress_Object(
    (1, 3, 6, 1, 6, 3, 18, 1, 3),
    _SnmpTrapAddress_Type()
)
snmpTrapAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    snmpTrapAddress.setStatus("current")
_SnmpTrapCommunity_Type = OctetString
_SnmpTrapCommunity_Object = MibScalar
snmpTrapCommunity = _SnmpTrapCommunity_Object(
    (1, 3, 6, 1, 6, 3, 18, 1, 4),
    _SnmpTrapCommunity_Type()
)
snmpTrapCommunity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    snmpTrapCommunity.setStatus("current")
_SnmpCommunityMIBConformance_ObjectIdentity = ObjectIdentity
snmpCommunityMIBConformance = _SnmpCommunityMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 18, 2)
)
_SnmpCommunityMIBCompliances_ObjectIdentity = ObjectIdentity
snmpCommunityMIBCompliances = _SnmpCommunityMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 18, 2, 1)
)
_SnmpCommunityMIBGroups_ObjectIdentity = ObjectIdentity
snmpCommunityMIBGroups = _SnmpCommunityMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 18, 2, 2)
)
snmpTargetAddrEntry.registerAugmentions(
    ("SNMP-COMMUNITY-MIB",
     "snmpTargetAddrExtEntry")
)
snmpTargetAddrExtEntry.setIndexNames(*snmpTargetAddrEntry.getIndexNames())

# Managed Objects groups

snmpCommunityTableGroup = ObjectGroup(
    (1, 3, 6, 1, 6, 3, 18, 2, 2, 1)
)
snmpCommunityTableGroup.setObjects(
      *(("SNMP-COMMUNITY-MIB", "snmpCommunityName"),
        ("SNMP-COMMUNITY-MIB", "snmpCommunitySecurityName"),
        ("SNMP-COMMUNITY-MIB", "snmpCommunityContextEngineID"),
        ("SNMP-COMMUNITY-MIB", "snmpCommunityContextName"),
        ("SNMP-COMMUNITY-MIB", "snmpCommunityTransportTag"),
        ("SNMP-COMMUNITY-MIB", "snmpCommunityStorageType"),
        ("SNMP-COMMUNITY-MIB", "snmpCommunityStatus"),
        ("SNMP-COMMUNITY-MIB", "snmpTargetAddrTMask"),
        ("SNMP-COMMUNITY-MIB", "snmpTargetAddrMMS"))
)
if mibBuilder.loadTexts:
    snmpCommunityTableGroup.setStatus("current")

snmpProxyTrapForwardGroup = ObjectGroup(
    (1, 3, 6, 1, 6, 3, 18, 2, 2, 3)
)
snmpProxyTrapForwardGroup.setObjects(
      *(("SNMP-COMMUNITY-MIB", "snmpTrapAddress"),
        ("SNMP-COMMUNITY-MIB", "snmpTrapCommunity"))
)
if mibBuilder.loadTexts:
    snmpProxyTrapForwardGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

snmpCommunityMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 6, 3, 18, 2, 1, 1)
)
if mibBuilder.loadTexts:
    snmpCommunityMIBCompliance.setStatus(
        "current"
    )

snmpProxyTrapForwardCompliance = ModuleCompliance(
    (1, 3, 6, 1, 6, 3, 18, 2, 1, 2)
)
if mibBuilder.loadTexts:
    snmpProxyTrapForwardCompliance.setStatus(
        "current"
    )

snmpCommunityMIBFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 6, 3, 18, 2, 1, 3)
)
if mibBuilder.loadTexts:
    snmpCommunityMIBFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMP-COMMUNITY-MIB",
    **{"snmpCommunityMIB": snmpCommunityMIB,
       "snmpCommunityMIBObjects": snmpCommunityMIBObjects,
       "snmpCommunityTable": snmpCommunityTable,
       "snmpCommunityEntry": snmpCommunityEntry,
       "snmpCommunityIndex": snmpCommunityIndex,
       "snmpCommunityName": snmpCommunityName,
       "snmpCommunitySecurityName": snmpCommunitySecurityName,
       "snmpCommunityContextEngineID": snmpCommunityContextEngineID,
       "snmpCommunityContextName": snmpCommunityContextName,
       "snmpCommunityTransportTag": snmpCommunityTransportTag,
       "snmpCommunityStorageType": snmpCommunityStorageType,
       "snmpCommunityStatus": snmpCommunityStatus,
       "snmpTargetAddrExtTable": snmpTargetAddrExtTable,
       "snmpTargetAddrExtEntry": snmpTargetAddrExtEntry,
       "snmpTargetAddrTMask": snmpTargetAddrTMask,
       "snmpTargetAddrMMS": snmpTargetAddrMMS,
       "snmpTrapAddress": snmpTrapAddress,
       "snmpTrapCommunity": snmpTrapCommunity,
       "snmpCommunityMIBConformance": snmpCommunityMIBConformance,
       "snmpCommunityMIBCompliances": snmpCommunityMIBCompliances,
       "snmpCommunityMIBCompliance": snmpCommunityMIBCompliance,
       "snmpProxyTrapForwardCompliance": snmpProxyTrapForwardCompliance,
       "snmpCommunityMIBFullCompliance": snmpCommunityMIBFullCompliance,
       "snmpCommunityMIBGroups": snmpCommunityMIBGroups,
       "snmpCommunityTableGroup": snmpCommunityTableGroup,
       "snmpProxyTrapForwardGroup": snmpProxyTrapForwardGroup}
)
