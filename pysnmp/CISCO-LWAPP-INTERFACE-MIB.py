# SNMP MIB module (CISCO-LWAPP-INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-INTERFACE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:36 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappInterfaceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 686)
)
ciscoLwappInterfaceMIB.setRevisions(
        ("2012-05-30 00:00",
         "2010-08-22 00:00",
         "2009-01-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappInterfaceMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappInterfaceMIBNotifs = _CiscoLwappInterfaceMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 0)
)
_CiscoLwappInterfaceMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappInterfaceMIBObjects = _CiscoLwappInterfaceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1)
)
_CiscoLwappInterfaceConfig_ObjectIdentity = ObjectIdentity
ciscoLwappInterfaceConfig = _CiscoLwappInterfaceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1)
)
_ClInterfaceConfigTable_Object = MibTable
clInterfaceConfigTable = _ClInterfaceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1)
)
if mibBuilder.loadTexts:
    clInterfaceConfigTable.setStatus("current")
_ClInterfaceConfigEntry_Object = MibTableRow
clInterfaceConfigEntry = _ClInterfaceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1, 1)
)
clInterfaceConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-INTERFACE-MIB", "clInterfaceName"),
)
if mibBuilder.loadTexts:
    clInterfaceConfigEntry.setStatus("current")


class _ClInterfaceName_Type(OctetString):
    """Custom type clInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ClInterfaceName_Type.__name__ = "OctetString"
_ClInterfaceName_Object = MibTableColumn
clInterfaceName = _ClInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1, 1, 1),
    _ClInterfaceName_Type()
)
clInterfaceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clInterfaceName.setStatus("current")


class _ClInterfaceWired_Type(TruthValue):
    """Custom type clInterfaceWired based on TruthValue"""


_ClInterfaceWired_Object = MibTableColumn
clInterfaceWired = _ClInterfaceWired_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1, 1, 2),
    _ClInterfaceWired_Type()
)
clInterfaceWired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clInterfaceWired.setStatus("current")


class _ClInterfaceQuarantineVlanId_Type(Unsigned32):
    """Custom type clInterfaceQuarantineVlanId based on Unsigned32"""
    defaultValue = 0


_ClInterfaceQuarantineVlanId_Object = MibTableColumn
clInterfaceQuarantineVlanId = _ClInterfaceQuarantineVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1, 1, 3),
    _ClInterfaceQuarantineVlanId_Type()
)
clInterfaceQuarantineVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clInterfaceQuarantineVlanId.setStatus("current")


class _ClInterfaceDhcpOpt82Enabled_Type(TruthValue):
    """Custom type clInterfaceDhcpOpt82Enabled based on TruthValue"""


_ClInterfaceDhcpOpt82Enabled_Object = MibTableColumn
clInterfaceDhcpOpt82Enabled = _ClInterfaceDhcpOpt82Enabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 1, 1, 4),
    _ClInterfaceDhcpOpt82Enabled_Type()
)
clInterfaceDhcpOpt82Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clInterfaceDhcpOpt82Enabled.setStatus("current")
_ClInterfaceGroupsConfigTable_Object = MibTable
clInterfaceGroupsConfigTable = _ClInterfaceGroupsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 2)
)
if mibBuilder.loadTexts:
    clInterfaceGroupsConfigTable.setStatus("current")
_ClInterfaceGroupsConfigEntry_Object = MibTableRow
clInterfaceGroupsConfigEntry = _ClInterfaceGroupsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 2, 1)
)
clInterfaceGroupsConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-INTERFACE-MIB", "clInterfaceGroupName"),
)
if mibBuilder.loadTexts:
    clInterfaceGroupsConfigEntry.setStatus("current")
_ClInterfaceGroupName_Type = SnmpAdminString
_ClInterfaceGroupName_Object = MibTableColumn
clInterfaceGroupName = _ClInterfaceGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 2, 1, 1),
    _ClInterfaceGroupName_Type()
)
clInterfaceGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clInterfaceGroupName.setStatus("current")
_ClInterfaceGroupDescr_Type = SnmpAdminString
_ClInterfaceGroupDescr_Object = MibTableColumn
clInterfaceGroupDescr = _ClInterfaceGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 2, 1, 2),
    _ClInterfaceGroupDescr_Type()
)
clInterfaceGroupDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clInterfaceGroupDescr.setStatus("current")
_ClInterfaceGroupIsQuarantine_Type = TruthValue
_ClInterfaceGroupIsQuarantine_Object = MibTableColumn
clInterfaceGroupIsQuarantine = _ClInterfaceGroupIsQuarantine_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 2, 1, 3),
    _ClInterfaceGroupIsQuarantine_Type()
)
clInterfaceGroupIsQuarantine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clInterfaceGroupIsQuarantine.setStatus("current")
_ClInterfaceGroupRowStatus_Type = RowStatus
_ClInterfaceGroupRowStatus_Object = MibTableColumn
clInterfaceGroupRowStatus = _ClInterfaceGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 2, 1, 4),
    _ClInterfaceGroupRowStatus_Type()
)
clInterfaceGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clInterfaceGroupRowStatus.setStatus("current")
_ClInterfaceGroupsMappingTable_Object = MibTable
clInterfaceGroupsMappingTable = _ClInterfaceGroupsMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 3)
)
if mibBuilder.loadTexts:
    clInterfaceGroupsMappingTable.setStatus("current")
_ClInterfaceGroupsMappingEntry_Object = MibTableRow
clInterfaceGroupsMappingEntry = _ClInterfaceGroupsMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 3, 1)
)
clInterfaceGroupsMappingEntry.setIndexNames(
    (0, "CISCO-LWAPP-INTERFACE-MIB", "clInterfaceGroupName"),
    (0, "CISCO-LWAPP-INTERFACE-MIB", "clInterfaceName"),
)
if mibBuilder.loadTexts:
    clInterfaceGroupsMappingEntry.setStatus("current")
_ClInterfaceGroupMappingRowStatus_Type = RowStatus
_ClInterfaceGroupMappingRowStatus_Object = MibTableColumn
clInterfaceGroupMappingRowStatus = _ClInterfaceGroupMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 1, 1, 3, 1, 1),
    _ClInterfaceGroupMappingRowStatus_Type()
)
clInterfaceGroupMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clInterfaceGroupMappingRowStatus.setStatus("current")
_CiscoLwappInterfaceMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappInterfaceMIBConform = _CiscoLwappInterfaceMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 2)
)
_CiscoLwappInterfaceMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappInterfaceMIBCompliances = _CiscoLwappInterfaceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 2, 1)
)
_CiscoLwappInterfaceMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappInterfaceMIBGroups = _CiscoLwappInterfaceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 2, 2)
)

# Managed Objects groups

ciscoLwappInterfaceConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 2, 2, 1)
)
ciscoLwappInterfaceConfigGroup.setObjects(
      *(("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceWired"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceQuarantineVlanId"))
)
if mibBuilder.loadTexts:
    ciscoLwappInterfaceConfigGroup.setStatus("current")

ciscoLwappInterfaceGroupConfigSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 2, 2, 2)
)
ciscoLwappInterfaceGroupConfigSup1.setObjects(
      *(("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceGroupDescr"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceGroupIsQuarantine"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceGroupRowStatus"),
        ("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceGroupMappingRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappInterfaceGroupConfigSup1.setStatus("current")

ciscoLwappInterfaceConfigGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 2, 2, 3)
)
ciscoLwappInterfaceConfigGroupSup1.setObjects(
    ("CISCO-LWAPP-INTERFACE-MIB", "clInterfaceDhcpOpt82Enabled")
)
if mibBuilder.loadTexts:
    ciscoLwappInterfaceConfigGroupSup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappInterfaceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappInterfaceMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappInterfaceMIBComplianceRev01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLwappInterfaceMIBComplianceRev01.setStatus(
        "deprecated"
    )

ciscoLwappInterfaceMIBComplianceRev02 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 686, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoLwappInterfaceMIBComplianceRev02.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-INTERFACE-MIB",
    **{"ciscoLwappInterfaceMIB": ciscoLwappInterfaceMIB,
       "ciscoLwappInterfaceMIBNotifs": ciscoLwappInterfaceMIBNotifs,
       "ciscoLwappInterfaceMIBObjects": ciscoLwappInterfaceMIBObjects,
       "ciscoLwappInterfaceConfig": ciscoLwappInterfaceConfig,
       "clInterfaceConfigTable": clInterfaceConfigTable,
       "clInterfaceConfigEntry": clInterfaceConfigEntry,
       "clInterfaceName": clInterfaceName,
       "clInterfaceWired": clInterfaceWired,
       "clInterfaceQuarantineVlanId": clInterfaceQuarantineVlanId,
       "clInterfaceDhcpOpt82Enabled": clInterfaceDhcpOpt82Enabled,
       "clInterfaceGroupsConfigTable": clInterfaceGroupsConfigTable,
       "clInterfaceGroupsConfigEntry": clInterfaceGroupsConfigEntry,
       "clInterfaceGroupName": clInterfaceGroupName,
       "clInterfaceGroupDescr": clInterfaceGroupDescr,
       "clInterfaceGroupIsQuarantine": clInterfaceGroupIsQuarantine,
       "clInterfaceGroupRowStatus": clInterfaceGroupRowStatus,
       "clInterfaceGroupsMappingTable": clInterfaceGroupsMappingTable,
       "clInterfaceGroupsMappingEntry": clInterfaceGroupsMappingEntry,
       "clInterfaceGroupMappingRowStatus": clInterfaceGroupMappingRowStatus,
       "ciscoLwappInterfaceMIBConform": ciscoLwappInterfaceMIBConform,
       "ciscoLwappInterfaceMIBCompliances": ciscoLwappInterfaceMIBCompliances,
       "ciscoLwappInterfaceMIBCompliance": ciscoLwappInterfaceMIBCompliance,
       "ciscoLwappInterfaceMIBComplianceRev01": ciscoLwappInterfaceMIBComplianceRev01,
       "ciscoLwappInterfaceMIBComplianceRev02": ciscoLwappInterfaceMIBComplianceRev02,
       "ciscoLwappInterfaceMIBGroups": ciscoLwappInterfaceMIBGroups,
       "ciscoLwappInterfaceConfigGroup": ciscoLwappInterfaceConfigGroup,
       "ciscoLwappInterfaceGroupConfigSup1": ciscoLwappInterfaceGroupConfigSup1,
       "ciscoLwappInterfaceConfigGroupSup1": ciscoLwappInterfaceConfigGroupSup1}
)
