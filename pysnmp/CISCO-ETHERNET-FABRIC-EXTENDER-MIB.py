# SNMP MIB module (CISCO-ETHERNET-FABRIC-EXTENDER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ETHERNET-FABRIC-EXTENDER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:01 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoEthernetFabricExtenderMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 691)
)
ciscoEthernetFabricExtenderMIB.setRevisions(
        ("2009-02-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoPortPinningMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("static", 1)
    )



# MIB Managed Objects in the order of their OIDs

_CiscoEthernetFabricExtenderMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoEthernetFabricExtenderMIBNotifs = _CiscoEthernetFabricExtenderMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 691, 0)
)
_CiscoEthernetFabricExtenderObjects_ObjectIdentity = ObjectIdentity
ciscoEthernetFabricExtenderObjects = _CiscoEthernetFabricExtenderObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 691, 1)
)
_CefexConfig_ObjectIdentity = ObjectIdentity
cefexConfig = _CefexConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1)
)
_CefexBindingTable_Object = MibTable
cefexBindingTable = _CefexBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cefexBindingTable.setStatus("current")
_CefexBindingEntry_Object = MibTableRow
cefexBindingEntry = _CefexBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1, 1, 1)
)
cefexBindingEntry.setIndexNames(
    (0, "CISCO-ETHERNET-FABRIC-EXTENDER-MIB", "cefexBindingInterfaceOnCoreSwitch"),
)
if mibBuilder.loadTexts:
    cefexBindingEntry.setStatus("current")
_CefexBindingInterfaceOnCoreSwitch_Type = InterfaceIndex
_CefexBindingInterfaceOnCoreSwitch_Object = MibTableColumn
cefexBindingInterfaceOnCoreSwitch = _CefexBindingInterfaceOnCoreSwitch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1, 1, 1, 1),
    _CefexBindingInterfaceOnCoreSwitch_Type()
)
cefexBindingInterfaceOnCoreSwitch.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cefexBindingInterfaceOnCoreSwitch.setStatus("current")


class _CefexBindingExtenderIndex_Type(Unsigned32):
    """Custom type cefexBindingExtenderIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 999),
    )


_CefexBindingExtenderIndex_Type.__name__ = "Unsigned32"
_CefexBindingExtenderIndex_Object = MibTableColumn
cefexBindingExtenderIndex = _CefexBindingExtenderIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1, 1, 1, 2),
    _CefexBindingExtenderIndex_Type()
)
cefexBindingExtenderIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cefexBindingExtenderIndex.setStatus("current")
_CefexBindingCreationTime_Type = TimeStamp
_CefexBindingCreationTime_Object = MibTableColumn
cefexBindingCreationTime = _CefexBindingCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1, 1, 1, 3),
    _CefexBindingCreationTime_Type()
)
cefexBindingCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefexBindingCreationTime.setStatus("current")
_CefexBindingRowStatus_Type = RowStatus
_CefexBindingRowStatus_Object = MibTableColumn
cefexBindingRowStatus = _CefexBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1, 1, 1, 4),
    _CefexBindingRowStatus_Type()
)
cefexBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cefexBindingRowStatus.setStatus("current")
_CefexConfigTable_Object = MibTable
cefexConfigTable = _CefexConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cefexConfigTable.setStatus("current")
_CefexConfigEntry_Object = MibTableRow
cefexConfigEntry = _CefexConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1, 2, 1)
)
cefexConfigEntry.setIndexNames(
    (0, "CISCO-ETHERNET-FABRIC-EXTENDER-MIB", "cefexBindingExtenderIndex"),
)
if mibBuilder.loadTexts:
    cefexConfigEntry.setStatus("current")


class _CefexConfigExtenderName_Type(SnmpAdminString):
    """Custom type cefexConfigExtenderName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CefexConfigExtenderName_Type.__name__ = "SnmpAdminString"
_CefexConfigExtenderName_Object = MibTableColumn
cefexConfigExtenderName = _CefexConfigExtenderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1, 2, 1, 1),
    _CefexConfigExtenderName_Type()
)
cefexConfigExtenderName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cefexConfigExtenderName.setStatus("current")


class _CefexConfigSerialNumCheck_Type(TruthValue):
    """Custom type cefexConfigSerialNumCheck based on TruthValue"""


_CefexConfigSerialNumCheck_Object = MibTableColumn
cefexConfigSerialNumCheck = _CefexConfigSerialNumCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1, 2, 1, 2),
    _CefexConfigSerialNumCheck_Type()
)
cefexConfigSerialNumCheck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cefexConfigSerialNumCheck.setStatus("current")


class _CefexConfigSerialNum_Type(SnmpAdminString):
    """Custom type cefexConfigSerialNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CefexConfigSerialNum_Type.__name__ = "SnmpAdminString"
_CefexConfigSerialNum_Object = MibTableColumn
cefexConfigSerialNum = _CefexConfigSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1, 2, 1, 3),
    _CefexConfigSerialNum_Type()
)
cefexConfigSerialNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cefexConfigSerialNum.setStatus("current")


class _CefexConfigPinningFailOverMode_Type(CiscoPortPinningMode):
    """Custom type cefexConfigPinningFailOverMode based on CiscoPortPinningMode"""


_CefexConfigPinningFailOverMode_Object = MibTableColumn
cefexConfigPinningFailOverMode = _CefexConfigPinningFailOverMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1, 2, 1, 4),
    _CefexConfigPinningFailOverMode_Type()
)
cefexConfigPinningFailOverMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cefexConfigPinningFailOverMode.setStatus("current")


class _CefexConfigPinningMaxLinks_Type(Unsigned32):
    """Custom type cefexConfigPinningMaxLinks based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CefexConfigPinningMaxLinks_Type.__name__ = "Unsigned32"
_CefexConfigPinningMaxLinks_Object = MibTableColumn
cefexConfigPinningMaxLinks = _CefexConfigPinningMaxLinks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1, 2, 1, 5),
    _CefexConfigPinningMaxLinks_Type()
)
cefexConfigPinningMaxLinks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cefexConfigPinningMaxLinks.setStatus("current")
_CefexConfigCreationTime_Type = TimeStamp
_CefexConfigCreationTime_Object = MibTableColumn
cefexConfigCreationTime = _CefexConfigCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1, 2, 1, 6),
    _CefexConfigCreationTime_Type()
)
cefexConfigCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefexConfigCreationTime.setStatus("current")
_CefexConfigRowStatus_Type = RowStatus
_CefexConfigRowStatus_Object = MibTableColumn
cefexConfigRowStatus = _CefexConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 691, 1, 1, 2, 1, 7),
    _CefexConfigRowStatus_Type()
)
cefexConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cefexConfigRowStatus.setStatus("current")
_CiscoEthernetFabricExtenderMIBConformance_ObjectIdentity = ObjectIdentity
ciscoEthernetFabricExtenderMIBConformance = _CiscoEthernetFabricExtenderMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 691, 2)
)
_CEthernetFabricExtenderMIBCompliances_ObjectIdentity = ObjectIdentity
cEthernetFabricExtenderMIBCompliances = _CEthernetFabricExtenderMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 691, 2, 1)
)
_CEthernetFabricExtenderMIBGroups_ObjectIdentity = ObjectIdentity
cEthernetFabricExtenderMIBGroups = _CEthernetFabricExtenderMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 691, 2, 2)
)

# Managed Objects groups

cefexBindingConformanceObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 691, 2, 2, 1)
)
cefexBindingConformanceObjects.setObjects(
      *(("CISCO-ETHERNET-FABRIC-EXTENDER-MIB", "cefexBindingExtenderIndex"),
        ("CISCO-ETHERNET-FABRIC-EXTENDER-MIB", "cefexBindingCreationTime"),
        ("CISCO-ETHERNET-FABRIC-EXTENDER-MIB", "cefexBindingRowStatus"),
        ("CISCO-ETHERNET-FABRIC-EXTENDER-MIB", "cefexConfigExtenderName"),
        ("CISCO-ETHERNET-FABRIC-EXTENDER-MIB", "cefexConfigSerialNumCheck"),
        ("CISCO-ETHERNET-FABRIC-EXTENDER-MIB", "cefexConfigSerialNum"),
        ("CISCO-ETHERNET-FABRIC-EXTENDER-MIB", "cefexConfigPinningFailOverMode"),
        ("CISCO-ETHERNET-FABRIC-EXTENDER-MIB", "cefexConfigPinningMaxLinks"),
        ("CISCO-ETHERNET-FABRIC-EXTENDER-MIB", "cefexConfigCreationTime"),
        ("CISCO-ETHERNET-FABRIC-EXTENDER-MIB", "cefexConfigRowStatus"))
)
if mibBuilder.loadTexts:
    cefexBindingConformanceObjects.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cEthernetFabricExtenderMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 691, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cEthernetFabricExtenderMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ETHERNET-FABRIC-EXTENDER-MIB",
    **{"CiscoPortPinningMode": CiscoPortPinningMode,
       "ciscoEthernetFabricExtenderMIB": ciscoEthernetFabricExtenderMIB,
       "ciscoEthernetFabricExtenderMIBNotifs": ciscoEthernetFabricExtenderMIBNotifs,
       "ciscoEthernetFabricExtenderObjects": ciscoEthernetFabricExtenderObjects,
       "cefexConfig": cefexConfig,
       "cefexBindingTable": cefexBindingTable,
       "cefexBindingEntry": cefexBindingEntry,
       "cefexBindingInterfaceOnCoreSwitch": cefexBindingInterfaceOnCoreSwitch,
       "cefexBindingExtenderIndex": cefexBindingExtenderIndex,
       "cefexBindingCreationTime": cefexBindingCreationTime,
       "cefexBindingRowStatus": cefexBindingRowStatus,
       "cefexConfigTable": cefexConfigTable,
       "cefexConfigEntry": cefexConfigEntry,
       "cefexConfigExtenderName": cefexConfigExtenderName,
       "cefexConfigSerialNumCheck": cefexConfigSerialNumCheck,
       "cefexConfigSerialNum": cefexConfigSerialNum,
       "cefexConfigPinningFailOverMode": cefexConfigPinningFailOverMode,
       "cefexConfigPinningMaxLinks": cefexConfigPinningMaxLinks,
       "cefexConfigCreationTime": cefexConfigCreationTime,
       "cefexConfigRowStatus": cefexConfigRowStatus,
       "ciscoEthernetFabricExtenderMIBConformance": ciscoEthernetFabricExtenderMIBConformance,
       "cEthernetFabricExtenderMIBCompliances": cEthernetFabricExtenderMIBCompliances,
       "cEthernetFabricExtenderMIBCompliance": cEthernetFabricExtenderMIBCompliance,
       "cEthernetFabricExtenderMIBGroups": cEthernetFabricExtenderMIBGroups,
       "cefexBindingConformanceObjects": cefexBindingConformanceObjects}
)
