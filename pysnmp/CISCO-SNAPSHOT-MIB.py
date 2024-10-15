# SNMP MIB module (CISCO-SNAPSHOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SNAPSHOT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:30 2024
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

(CiscoNetworkAddress,
 CiscoNetworkProtocol) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoNetworkAddress",
    "CiscoNetworkProtocol")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

ciscoSnapshotMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 19)
)
ciscoSnapshotMIB.setRevisions(
        ("1995-08-15 00:00",
         "1995-03-21 00:00",
         "1995-01-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoSnapshotMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSnapshotMIBObjects = _CiscoSnapshotMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 19, 1)
)
_CiscoSnapshotForceActive_Type = Integer32
_CiscoSnapshotForceActive_Object = MibScalar
ciscoSnapshotForceActive = _CiscoSnapshotForceActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 1),
    _CiscoSnapshotForceActive_Type()
)
ciscoSnapshotForceActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoSnapshotForceActive.setStatus("current")
_CiscoSnapshotInterfaceTable_Object = MibTable
ciscoSnapshotInterfaceTable = _CiscoSnapshotInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoSnapshotInterfaceTable.setStatus("current")
_CiscoSnapshotInterfaceEntry_Object = MibTableRow
ciscoSnapshotInterfaceEntry = _CiscoSnapshotInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 2, 1)
)
ciscoSnapshotInterfaceEntry.setIndexNames(
    (0, "CISCO-SNAPSHOT-MIB", "ciscoSnapshotIfIndex"),
)
if mibBuilder.loadTexts:
    ciscoSnapshotInterfaceEntry.setStatus("current")
_CiscoSnapshotIfIndex_Type = InterfaceIndex
_CiscoSnapshotIfIndex_Object = MibTableColumn
ciscoSnapshotIfIndex = _CiscoSnapshotIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 2, 1, 1),
    _CiscoSnapshotIfIndex_Type()
)
ciscoSnapshotIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoSnapshotIfIndex.setStatus("current")


class _CiscoSnapshotClient_Type(TruthValue):
    """Custom type ciscoSnapshotClient based on TruthValue"""


_CiscoSnapshotClient_Object = MibTableColumn
ciscoSnapshotClient = _CiscoSnapshotClient_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 2, 1, 2),
    _CiscoSnapshotClient_Type()
)
ciscoSnapshotClient.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoSnapshotClient.setStatus("current")


class _CiscoSnapshotDialer_Type(TruthValue):
    """Custom type ciscoSnapshotDialer based on TruthValue"""


_CiscoSnapshotDialer_Object = MibTableColumn
ciscoSnapshotDialer = _CiscoSnapshotDialer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 2, 1, 3),
    _CiscoSnapshotDialer_Type()
)
ciscoSnapshotDialer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoSnapshotDialer.setStatus("current")


class _CiscoSnapshotActiveInterval_Type(Integer32):
    """Custom type ciscoSnapshotActiveInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 1000),
    )


_CiscoSnapshotActiveInterval_Type.__name__ = "Integer32"
_CiscoSnapshotActiveInterval_Object = MibTableColumn
ciscoSnapshotActiveInterval = _CiscoSnapshotActiveInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 2, 1, 4),
    _CiscoSnapshotActiveInterval_Type()
)
ciscoSnapshotActiveInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoSnapshotActiveInterval.setStatus("current")
if mibBuilder.loadTexts:
    ciscoSnapshotActiveInterval.setUnits("minutes")


class _CiscoSnapshotQuietInterval_Type(Integer32):
    """Custom type ciscoSnapshotQuietInterval based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 100000),
    )


_CiscoSnapshotQuietInterval_Type.__name__ = "Integer32"
_CiscoSnapshotQuietInterval_Object = MibTableColumn
ciscoSnapshotQuietInterval = _CiscoSnapshotQuietInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 2, 1, 5),
    _CiscoSnapshotQuietInterval_Type()
)
ciscoSnapshotQuietInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoSnapshotQuietInterval.setStatus("current")
if mibBuilder.loadTexts:
    ciscoSnapshotQuietInterval.setUnits("minutes")
_CiscoSnapshotRetryInterval_Type = Integer32
_CiscoSnapshotRetryInterval_Object = MibTableColumn
ciscoSnapshotRetryInterval = _CiscoSnapshotRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 2, 1, 6),
    _CiscoSnapshotRetryInterval_Type()
)
ciscoSnapshotRetryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSnapshotRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    ciscoSnapshotRetryInterval.setUnits("minutes")


class _CiscoSnapshotIfUpAction_Type(Integer32):
    """Custom type ciscoSnapshotIfUpAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("goActive", 1),
          ("noAction", 2))
    )


_CiscoSnapshotIfUpAction_Type.__name__ = "Integer32"
_CiscoSnapshotIfUpAction_Object = MibTableColumn
ciscoSnapshotIfUpAction = _CiscoSnapshotIfUpAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 2, 1, 7),
    _CiscoSnapshotIfUpAction_Type()
)
ciscoSnapshotIfUpAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoSnapshotIfUpAction.setStatus("current")
_CiscoSnapshotRowStatus_Type = RowStatus
_CiscoSnapshotRowStatus_Object = MibTableColumn
ciscoSnapshotRowStatus = _CiscoSnapshotRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 2, 1, 8),
    _CiscoSnapshotRowStatus_Type()
)
ciscoSnapshotRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoSnapshotRowStatus.setStatus("current")
_CiscoSnapshotActivityTable_Object = MibTable
ciscoSnapshotActivityTable = _CiscoSnapshotActivityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoSnapshotActivityTable.setStatus("current")
_CiscoSnapshotActivityEntry_Object = MibTableRow
ciscoSnapshotActivityEntry = _CiscoSnapshotActivityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 3, 1)
)
ciscoSnapshotActivityEntry.setIndexNames(
    (0, "CISCO-SNAPSHOT-MIB", "ciscoSnapshotIfIndex"),
    (0, "CISCO-SNAPSHOT-MIB", "ciscoSnapshotActivityIndex"),
)
if mibBuilder.loadTexts:
    ciscoSnapshotActivityEntry.setStatus("current")


class _CiscoSnapshotActivityIndex_Type(Integer32):
    """Custom type ciscoSnapshotActivityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CiscoSnapshotActivityIndex_Type.__name__ = "Integer32"
_CiscoSnapshotActivityIndex_Object = MibTableColumn
ciscoSnapshotActivityIndex = _CiscoSnapshotActivityIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 3, 1, 1),
    _CiscoSnapshotActivityIndex_Type()
)
ciscoSnapshotActivityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoSnapshotActivityIndex.setStatus("current")


class _CiscoSnapshotActivityState_Type(Integer32):
    """Custom type ciscoSnapshotActivityState based on Integer32"""
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
        *(("active", 1),
          ("limbo", 6),
          ("quiet", 2),
          ("serverPostActive", 3),
          ("transitionToActive", 5),
          ("transitionToQuiet", 4))
    )


_CiscoSnapshotActivityState_Type.__name__ = "Integer32"
_CiscoSnapshotActivityState_Object = MibTableColumn
ciscoSnapshotActivityState = _CiscoSnapshotActivityState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 3, 1, 2),
    _CiscoSnapshotActivityState_Type()
)
ciscoSnapshotActivityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSnapshotActivityState.setStatus("current")
_CiscoSnapshotActivityTimer_Type = Integer32
_CiscoSnapshotActivityTimer_Object = MibTableColumn
ciscoSnapshotActivityTimer = _CiscoSnapshotActivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 3, 1, 3),
    _CiscoSnapshotActivityTimer_Type()
)
ciscoSnapshotActivityTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSnapshotActivityTimer.setStatus("current")
if mibBuilder.loadTexts:
    ciscoSnapshotActivityTimer.setUnits("minutes")
_CiscoSnapshotExchangeTimer_Type = Integer32
_CiscoSnapshotExchangeTimer_Object = MibTableColumn
ciscoSnapshotExchangeTimer = _CiscoSnapshotExchangeTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 3, 1, 4),
    _CiscoSnapshotExchangeTimer_Type()
)
ciscoSnapshotExchangeTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSnapshotExchangeTimer.setStatus("current")
if mibBuilder.loadTexts:
    ciscoSnapshotExchangeTimer.setUnits("minutes")
_CiscoSnapshotDialerMap_Type = Integer32
_CiscoSnapshotDialerMap_Object = MibTableColumn
ciscoSnapshotDialerMap = _CiscoSnapshotDialerMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 3, 1, 5),
    _CiscoSnapshotDialerMap_Type()
)
ciscoSnapshotDialerMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSnapshotDialerMap.setStatus("current")
_CiscoSnapshotSourceProtocol_Type = CiscoNetworkProtocol
_CiscoSnapshotSourceProtocol_Object = MibTableColumn
ciscoSnapshotSourceProtocol = _CiscoSnapshotSourceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 3, 1, 6),
    _CiscoSnapshotSourceProtocol_Type()
)
ciscoSnapshotSourceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSnapshotSourceProtocol.setStatus("current")
_CiscoSnapshotSourceAddress_Type = CiscoNetworkAddress
_CiscoSnapshotSourceAddress_Object = MibTableColumn
ciscoSnapshotSourceAddress = _CiscoSnapshotSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 3, 1, 7),
    _CiscoSnapshotSourceAddress_Type()
)
ciscoSnapshotSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSnapshotSourceAddress.setStatus("current")


class _CiscoSnapshotProtocolsExchanged_Type(OctetString):
    """Custom type ciscoSnapshotProtocolsExchanged based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CiscoSnapshotProtocolsExchanged_Type.__name__ = "OctetString"
_CiscoSnapshotProtocolsExchanged_Object = MibTableColumn
ciscoSnapshotProtocolsExchanged = _CiscoSnapshotProtocolsExchanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 19, 1, 3, 1, 8),
    _CiscoSnapshotProtocolsExchanged_Type()
)
ciscoSnapshotProtocolsExchanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSnapshotProtocolsExchanged.setStatus("current")
_CiscoSnapshotMIBConformance_ObjectIdentity = ObjectIdentity
ciscoSnapshotMIBConformance = _CiscoSnapshotMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 19, 2)
)
_CiscoSnapshotMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSnapshotMIBCompliances = _CiscoSnapshotMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 19, 2, 1)
)
_CiscoSnapshotMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSnapshotMIBGroups = _CiscoSnapshotMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 19, 2, 2)
)

# Managed Objects groups

ciscoSnapshotMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 19, 2, 2, 1)
)
ciscoSnapshotMIBGroup.setObjects(
      *(("CISCO-SNAPSHOT-MIB", "ciscoSnapshotForceActive"),
        ("CISCO-SNAPSHOT-MIB", "ciscoSnapshotClient"),
        ("CISCO-SNAPSHOT-MIB", "ciscoSnapshotDialer"),
        ("CISCO-SNAPSHOT-MIB", "ciscoSnapshotActiveInterval"),
        ("CISCO-SNAPSHOT-MIB", "ciscoSnapshotQuietInterval"),
        ("CISCO-SNAPSHOT-MIB", "ciscoSnapshotRetryInterval"),
        ("CISCO-SNAPSHOT-MIB", "ciscoSnapshotIfUpAction"),
        ("CISCO-SNAPSHOT-MIB", "ciscoSnapshotRowStatus"),
        ("CISCO-SNAPSHOT-MIB", "ciscoSnapshotActivityState"),
        ("CISCO-SNAPSHOT-MIB", "ciscoSnapshotActivityTimer"),
        ("CISCO-SNAPSHOT-MIB", "ciscoSnapshotExchangeTimer"),
        ("CISCO-SNAPSHOT-MIB", "ciscoSnapshotDialerMap"),
        ("CISCO-SNAPSHOT-MIB", "ciscoSnapshotSourceProtocol"),
        ("CISCO-SNAPSHOT-MIB", "ciscoSnapshotSourceAddress"),
        ("CISCO-SNAPSHOT-MIB", "ciscoSnapshotProtocolsExchanged"))
)
if mibBuilder.loadTexts:
    ciscoSnapshotMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoSnapshotMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 19, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSnapshotMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SNAPSHOT-MIB",
    **{"ciscoSnapshotMIB": ciscoSnapshotMIB,
       "ciscoSnapshotMIBObjects": ciscoSnapshotMIBObjects,
       "ciscoSnapshotForceActive": ciscoSnapshotForceActive,
       "ciscoSnapshotInterfaceTable": ciscoSnapshotInterfaceTable,
       "ciscoSnapshotInterfaceEntry": ciscoSnapshotInterfaceEntry,
       "ciscoSnapshotIfIndex": ciscoSnapshotIfIndex,
       "ciscoSnapshotClient": ciscoSnapshotClient,
       "ciscoSnapshotDialer": ciscoSnapshotDialer,
       "ciscoSnapshotActiveInterval": ciscoSnapshotActiveInterval,
       "ciscoSnapshotQuietInterval": ciscoSnapshotQuietInterval,
       "ciscoSnapshotRetryInterval": ciscoSnapshotRetryInterval,
       "ciscoSnapshotIfUpAction": ciscoSnapshotIfUpAction,
       "ciscoSnapshotRowStatus": ciscoSnapshotRowStatus,
       "ciscoSnapshotActivityTable": ciscoSnapshotActivityTable,
       "ciscoSnapshotActivityEntry": ciscoSnapshotActivityEntry,
       "ciscoSnapshotActivityIndex": ciscoSnapshotActivityIndex,
       "ciscoSnapshotActivityState": ciscoSnapshotActivityState,
       "ciscoSnapshotActivityTimer": ciscoSnapshotActivityTimer,
       "ciscoSnapshotExchangeTimer": ciscoSnapshotExchangeTimer,
       "ciscoSnapshotDialerMap": ciscoSnapshotDialerMap,
       "ciscoSnapshotSourceProtocol": ciscoSnapshotSourceProtocol,
       "ciscoSnapshotSourceAddress": ciscoSnapshotSourceAddress,
       "ciscoSnapshotProtocolsExchanged": ciscoSnapshotProtocolsExchanged,
       "ciscoSnapshotMIBConformance": ciscoSnapshotMIBConformance,
       "ciscoSnapshotMIBCompliances": ciscoSnapshotMIBCompliances,
       "ciscoSnapshotMIBCompliance": ciscoSnapshotMIBCompliance,
       "ciscoSnapshotMIBGroups": ciscoSnapshotMIBGroups,
       "ciscoSnapshotMIBGroup": ciscoSnapshotMIBGroup}
)
