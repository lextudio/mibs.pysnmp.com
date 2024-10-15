# SNMP MIB module (CISCO-FC-DEVICE-ALIAS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FC-DEVICE-ALIAS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:12 2024
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

(CdpvmDevType,) = mibBuilder.importSymbols(
    "CISCO-DYNAMIC-PORT-VSAN-MIB",
    "CdpvmDevType")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoFcDeviceAliasMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 430)
)
ciscoFcDeviceAliasMIB.setRevisions(
        ("2004-09-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfdaMIBNotifs_ObjectIdentity = ObjectIdentity
cfdaMIBNotifs = _CfdaMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 430, 0)
)
_CfdaMIBObjects_ObjectIdentity = ObjectIdentity
cfdaMIBObjects = _CfdaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 430, 1)
)
_CfdaConfiguration_ObjectIdentity = ObjectIdentity
cfdaConfiguration = _CfdaConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 430, 1, 1)
)
_CfdaConfigTable_Object = MibTable
cfdaConfigTable = _CfdaConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 430, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cfdaConfigTable.setStatus("current")
_CfdaConfigEntry_Object = MibTableRow
cfdaConfigEntry = _CfdaConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 430, 1, 1, 1, 1)
)
cfdaConfigEntry.setIndexNames(
    (0, "CISCO-FC-DEVICE-ALIAS-MIB", "cfdaConfigDeviceAlias"),
)
if mibBuilder.loadTexts:
    cfdaConfigEntry.setStatus("current")


class _CfdaConfigDeviceAlias_Type(SnmpAdminString):
    """Custom type cfdaConfigDeviceAlias based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CfdaConfigDeviceAlias_Type.__name__ = "SnmpAdminString"
_CfdaConfigDeviceAlias_Object = MibTableColumn
cfdaConfigDeviceAlias = _CfdaConfigDeviceAlias_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 430, 1, 1, 1, 1, 1),
    _CfdaConfigDeviceAlias_Type()
)
cfdaConfigDeviceAlias.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfdaConfigDeviceAlias.setStatus("current")


class _CfdaConfigDeviceType_Type(CdpvmDevType):
    """Custom type cfdaConfigDeviceType based on CdpvmDevType"""


_CfdaConfigDeviceType_Object = MibTableColumn
cfdaConfigDeviceType = _CfdaConfigDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 430, 1, 1, 1, 1, 2),
    _CfdaConfigDeviceType_Type()
)
cfdaConfigDeviceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfdaConfigDeviceType.setStatus("current")


class _CfdaConfigDeviceId_Type(OctetString):
    """Custom type cfdaConfigDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CfdaConfigDeviceId_Type.__name__ = "OctetString"
_CfdaConfigDeviceId_Object = MibTableColumn
cfdaConfigDeviceId = _CfdaConfigDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 430, 1, 1, 1, 1, 3),
    _CfdaConfigDeviceId_Type()
)
cfdaConfigDeviceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfdaConfigDeviceId.setStatus("current")
_CfdaConfigRowStatus_Type = RowStatus
_CfdaConfigRowStatus_Object = MibTableColumn
cfdaConfigRowStatus = _CfdaConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 430, 1, 1, 1, 1, 4),
    _CfdaConfigRowStatus_Type()
)
cfdaConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfdaConfigRowStatus.setStatus("current")
_CfdaMIBConform_ObjectIdentity = ObjectIdentity
cfdaMIBConform = _CfdaMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 430, 2)
)
_CiscoFcDaMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoFcDaMIBCompliances = _CiscoFcDaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 430, 2, 1)
)
_CiscoFcDaMIBGroups_ObjectIdentity = ObjectIdentity
ciscoFcDaMIBGroups = _CiscoFcDaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 430, 2, 2)
)

# Managed Objects groups

ciscoFcDaConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 430, 2, 2, 1)
)
ciscoFcDaConfigGroup.setObjects(
      *(("CISCO-FC-DEVICE-ALIAS-MIB", "cfdaConfigDeviceType"),
        ("CISCO-FC-DEVICE-ALIAS-MIB", "cfdaConfigDeviceId"),
        ("CISCO-FC-DEVICE-ALIAS-MIB", "cfdaConfigRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoFcDaConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoFcDaMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 430, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoFcDaMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FC-DEVICE-ALIAS-MIB",
    **{"ciscoFcDeviceAliasMIB": ciscoFcDeviceAliasMIB,
       "cfdaMIBNotifs": cfdaMIBNotifs,
       "cfdaMIBObjects": cfdaMIBObjects,
       "cfdaConfiguration": cfdaConfiguration,
       "cfdaConfigTable": cfdaConfigTable,
       "cfdaConfigEntry": cfdaConfigEntry,
       "cfdaConfigDeviceAlias": cfdaConfigDeviceAlias,
       "cfdaConfigDeviceType": cfdaConfigDeviceType,
       "cfdaConfigDeviceId": cfdaConfigDeviceId,
       "cfdaConfigRowStatus": cfdaConfigRowStatus,
       "cfdaMIBConform": cfdaMIBConform,
       "ciscoFcDaMIBCompliances": ciscoFcDaMIBCompliances,
       "ciscoFcDaMIBCompliance": ciscoFcDaMIBCompliance,
       "ciscoFcDaMIBGroups": ciscoFcDaMIBGroups,
       "ciscoFcDaConfigGroup": ciscoFcDaConfigGroup}
)
