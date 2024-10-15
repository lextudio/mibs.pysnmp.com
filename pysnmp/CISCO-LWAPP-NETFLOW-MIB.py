# SNMP MIB module (CISCO-LWAPP-NETFLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-NETFLOW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:49 2024
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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

ciscoLwappNetflowMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996)
)
ciscoLwappNetflowMIB.setRevisions(
        ("2012-06-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappNetflowMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappNetflowMIBNotifs = _CiscoLwappNetflowMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 0)
)
_CiscoLwappNetflowMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappNetflowMIBObjects = _CiscoLwappNetflowMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 1)
)
_CiscoLwappNetflowTableObjects_ObjectIdentity = ObjectIdentity
ciscoLwappNetflowTableObjects = _CiscoLwappNetflowTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1)
)
_CLNetflowMonitorTable_Object = MibTable
cLNetflowMonitorTable = _CLNetflowMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cLNetflowMonitorTable.setStatus("current")
_CLNetflowMonitorEntry_Object = MibTableRow
cLNetflowMonitorEntry = _CLNetflowMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1, 1, 1)
)
cLNetflowMonitorEntry.setIndexNames(
    (0, "CISCO-LWAPP-NETFLOW-MIB", "cLNetflowMonitorName"),
)
if mibBuilder.loadTexts:
    cLNetflowMonitorEntry.setStatus("current")


class _CLNetflowMonitorName_Type(SnmpAdminString):
    """Custom type cLNetflowMonitorName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLNetflowMonitorName_Type.__name__ = "SnmpAdminString"
_CLNetflowMonitorName_Object = MibTableColumn
cLNetflowMonitorName = _CLNetflowMonitorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1, 1, 1, 1),
    _CLNetflowMonitorName_Type()
)
cLNetflowMonitorName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLNetflowMonitorName.setStatus("current")


class _CLNetflowMonitorRecordName_Type(SnmpAdminString):
    """Custom type cLNetflowMonitorRecordName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLNetflowMonitorRecordName_Type.__name__ = "SnmpAdminString"
_CLNetflowMonitorRecordName_Object = MibTableColumn
cLNetflowMonitorRecordName = _CLNetflowMonitorRecordName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1, 1, 1, 2),
    _CLNetflowMonitorRecordName_Type()
)
cLNetflowMonitorRecordName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLNetflowMonitorRecordName.setStatus("current")
_CLNetflowMonitorRowStatus_Type = RowStatus
_CLNetflowMonitorRowStatus_Object = MibTableColumn
cLNetflowMonitorRowStatus = _CLNetflowMonitorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1, 1, 1, 3),
    _CLNetflowMonitorRowStatus_Type()
)
cLNetflowMonitorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLNetflowMonitorRowStatus.setStatus("current")
_CLNetflowExporterTable_Object = MibTable
cLNetflowExporterTable = _CLNetflowExporterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cLNetflowExporterTable.setStatus("current")
_CLNetflowExporterEntry_Object = MibTableRow
cLNetflowExporterEntry = _CLNetflowExporterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1, 2, 1)
)
cLNetflowExporterEntry.setIndexNames(
    (0, "CISCO-LWAPP-NETFLOW-MIB", "cLNetflowExporterName"),
)
if mibBuilder.loadTexts:
    cLNetflowExporterEntry.setStatus("current")


class _CLNetflowExporterName_Type(SnmpAdminString):
    """Custom type cLNetflowExporterName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLNetflowExporterName_Type.__name__ = "SnmpAdminString"
_CLNetflowExporterName_Object = MibTableColumn
cLNetflowExporterName = _CLNetflowExporterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1, 2, 1, 1),
    _CLNetflowExporterName_Type()
)
cLNetflowExporterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLNetflowExporterName.setStatus("current")
_CLNetflowExporterIPAddressType_Type = InetAddressType
_CLNetflowExporterIPAddressType_Object = MibTableColumn
cLNetflowExporterIPAddressType = _CLNetflowExporterIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1, 2, 1, 2),
    _CLNetflowExporterIPAddressType_Type()
)
cLNetflowExporterIPAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLNetflowExporterIPAddressType.setStatus("current")
_CLNetflowExporterIPAddress_Type = InetAddress
_CLNetflowExporterIPAddress_Object = MibTableColumn
cLNetflowExporterIPAddress = _CLNetflowExporterIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1, 2, 1, 3),
    _CLNetflowExporterIPAddress_Type()
)
cLNetflowExporterIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLNetflowExporterIPAddress.setStatus("current")
_CLNetflowExporterPortNumber_Type = InetPortNumber
_CLNetflowExporterPortNumber_Object = MibTableColumn
cLNetflowExporterPortNumber = _CLNetflowExporterPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1, 2, 1, 4),
    _CLNetflowExporterPortNumber_Type()
)
cLNetflowExporterPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLNetflowExporterPortNumber.setStatus("current")
_CLNetflowExporterRowStatus_Type = RowStatus
_CLNetflowExporterRowStatus_Object = MibTableColumn
cLNetflowExporterRowStatus = _CLNetflowExporterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1, 2, 1, 5),
    _CLNetflowExporterRowStatus_Type()
)
cLNetflowExporterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLNetflowExporterRowStatus.setStatus("current")
_CLNetflowMonitorMappingTable_Object = MibTable
cLNetflowMonitorMappingTable = _CLNetflowMonitorMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cLNetflowMonitorMappingTable.setStatus("current")
_CLNetflowMonitorMappingEntry_Object = MibTableRow
cLNetflowMonitorMappingEntry = _CLNetflowMonitorMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1, 3, 1)
)
cLNetflowMonitorMappingEntry.setIndexNames(
    (0, "CISCO-LWAPP-NETFLOW-MIB", "cLNetflowMonitorName"),
    (0, "CISCO-LWAPP-NETFLOW-MIB", "cLNetflowMonitorMappingExporterName"),
)
if mibBuilder.loadTexts:
    cLNetflowMonitorMappingEntry.setStatus("current")


class _CLNetflowMonitorMappingExporterName_Type(SnmpAdminString):
    """Custom type cLNetflowMonitorMappingExporterName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLNetflowMonitorMappingExporterName_Type.__name__ = "SnmpAdminString"
_CLNetflowMonitorMappingExporterName_Object = MibTableColumn
cLNetflowMonitorMappingExporterName = _CLNetflowMonitorMappingExporterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1, 3, 1, 1),
    _CLNetflowMonitorMappingExporterName_Type()
)
cLNetflowMonitorMappingExporterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLNetflowMonitorMappingExporterName.setStatus("current")
_CLNetflowMonitorMappingRowStatus_Type = RowStatus
_CLNetflowMonitorMappingRowStatus_Object = MibTableColumn
cLNetflowMonitorMappingRowStatus = _CLNetflowMonitorMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1, 3, 1, 2),
    _CLNetflowMonitorMappingRowStatus_Type()
)
cLNetflowMonitorMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLNetflowMonitorMappingRowStatus.setStatus("current")
_CiscoLwappNetflowMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappNetflowMIBConform = _CiscoLwappNetflowMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 2)
)
_CiscoLwappNetflowMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappNetflowMIBCompliances = _CiscoLwappNetflowMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 2, 1)
)
_CiscoLwappNetflowMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappNetflowMIBGroups = _CiscoLwappNetflowMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 2, 2)
)

# Managed Objects groups

cLNetflowConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 2, 2, 1)
)
cLNetflowConfigGroup.setObjects(
      *(("CISCO-LWAPP-NETFLOW-MIB", "cLNetflowMonitorName"),
        ("CISCO-LWAPP-NETFLOW-MIB", "cLNetflowMonitorRecordName"),
        ("CISCO-LWAPP-NETFLOW-MIB", "cLNetflowMonitorRowStatus"),
        ("CISCO-LWAPP-NETFLOW-MIB", "cLNetflowExporterName"),
        ("CISCO-LWAPP-NETFLOW-MIB", "cLNetflowExporterIPAddressType"),
        ("CISCO-LWAPP-NETFLOW-MIB", "cLNetflowExporterIPAddress"),
        ("CISCO-LWAPP-NETFLOW-MIB", "cLNetflowExporterPortNumber"),
        ("CISCO-LWAPP-NETFLOW-MIB", "cLNetflowExporterRowStatus"),
        ("CISCO-LWAPP-NETFLOW-MIB", "cLNetflowMonitorMappingExporterName"),
        ("CISCO-LWAPP-NETFLOW-MIB", "cLNetflowMonitorMappingRowStatus"))
)
if mibBuilder.loadTexts:
    cLNetflowConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappNetflowMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappNetflowMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-NETFLOW-MIB",
    **{"ciscoLwappNetflowMIB": ciscoLwappNetflowMIB,
       "ciscoLwappNetflowMIBNotifs": ciscoLwappNetflowMIBNotifs,
       "ciscoLwappNetflowMIBObjects": ciscoLwappNetflowMIBObjects,
       "ciscoLwappNetflowTableObjects": ciscoLwappNetflowTableObjects,
       "cLNetflowMonitorTable": cLNetflowMonitorTable,
       "cLNetflowMonitorEntry": cLNetflowMonitorEntry,
       "cLNetflowMonitorName": cLNetflowMonitorName,
       "cLNetflowMonitorRecordName": cLNetflowMonitorRecordName,
       "cLNetflowMonitorRowStatus": cLNetflowMonitorRowStatus,
       "cLNetflowExporterTable": cLNetflowExporterTable,
       "cLNetflowExporterEntry": cLNetflowExporterEntry,
       "cLNetflowExporterName": cLNetflowExporterName,
       "cLNetflowExporterIPAddressType": cLNetflowExporterIPAddressType,
       "cLNetflowExporterIPAddress": cLNetflowExporterIPAddress,
       "cLNetflowExporterPortNumber": cLNetflowExporterPortNumber,
       "cLNetflowExporterRowStatus": cLNetflowExporterRowStatus,
       "cLNetflowMonitorMappingTable": cLNetflowMonitorMappingTable,
       "cLNetflowMonitorMappingEntry": cLNetflowMonitorMappingEntry,
       "cLNetflowMonitorMappingExporterName": cLNetflowMonitorMappingExporterName,
       "cLNetflowMonitorMappingRowStatus": cLNetflowMonitorMappingRowStatus,
       "ciscoLwappNetflowMIBConform": ciscoLwappNetflowMIBConform,
       "ciscoLwappNetflowMIBCompliances": ciscoLwappNetflowMIBCompliances,
       "ciscoLwappNetflowMIBCompliance": ciscoLwappNetflowMIBCompliance,
       "ciscoLwappNetflowMIBGroups": ciscoLwappNetflowMIBGroups,
       "cLNetflowConfigGroup": cLNetflowConfigGroup}
)
