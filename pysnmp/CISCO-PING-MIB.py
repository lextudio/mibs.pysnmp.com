# SNMP MIB module (CISCO-PING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-PING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:46 2024
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

(OwnerString,) = mibBuilder.importSymbols(
    "IF-MIB",
    "OwnerString")

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

ciscoPingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 16)
)
ciscoPingMIB.setRevisions(
        ("2001-08-28 00:00",
         "2001-05-14 00:00",
         "1999-10-08 00:00",
         "1994-11-11 00:00",
         "1994-07-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoPingMIBObjects_ObjectIdentity = ObjectIdentity
ciscoPingMIBObjects = _CiscoPingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 1)
)
_CiscoPingTable_Object = MibTable
ciscoPingTable = _CiscoPingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoPingTable.setStatus("current")
_CiscoPingEntry_Object = MibTableRow
ciscoPingEntry = _CiscoPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1)
)
ciscoPingEntry.setIndexNames(
    (0, "CISCO-PING-MIB", "ciscoPingSerialNumber"),
)
if mibBuilder.loadTexts:
    ciscoPingEntry.setStatus("current")


class _CiscoPingSerialNumber_Type(Integer32):
    """Custom type ciscoPingSerialNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CiscoPingSerialNumber_Type.__name__ = "Integer32"
_CiscoPingSerialNumber_Object = MibTableColumn
ciscoPingSerialNumber = _CiscoPingSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 1),
    _CiscoPingSerialNumber_Type()
)
ciscoPingSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoPingSerialNumber.setStatus("current")
_CiscoPingProtocol_Type = CiscoNetworkProtocol
_CiscoPingProtocol_Object = MibTableColumn
ciscoPingProtocol = _CiscoPingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 2),
    _CiscoPingProtocol_Type()
)
ciscoPingProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoPingProtocol.setStatus("current")
_CiscoPingAddress_Type = CiscoNetworkAddress
_CiscoPingAddress_Object = MibTableColumn
ciscoPingAddress = _CiscoPingAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 3),
    _CiscoPingAddress_Type()
)
ciscoPingAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoPingAddress.setStatus("current")


class _CiscoPingPacketCount_Type(Integer32):
    """Custom type ciscoPingPacketCount based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CiscoPingPacketCount_Type.__name__ = "Integer32"
_CiscoPingPacketCount_Object = MibTableColumn
ciscoPingPacketCount = _CiscoPingPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 4),
    _CiscoPingPacketCount_Type()
)
ciscoPingPacketCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoPingPacketCount.setStatus("current")


class _CiscoPingPacketSize_Type(Integer32):
    """Custom type ciscoPingPacketSize based on Integer32"""
    defaultValue = 100


_CiscoPingPacketSize_Object = MibTableColumn
ciscoPingPacketSize = _CiscoPingPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 5),
    _CiscoPingPacketSize_Type()
)
ciscoPingPacketSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoPingPacketSize.setStatus("current")


class _CiscoPingPacketTimeout_Type(Integer32):
    """Custom type ciscoPingPacketTimeout based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_CiscoPingPacketTimeout_Type.__name__ = "Integer32"
_CiscoPingPacketTimeout_Object = MibTableColumn
ciscoPingPacketTimeout = _CiscoPingPacketTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 6),
    _CiscoPingPacketTimeout_Type()
)
ciscoPingPacketTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoPingPacketTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ciscoPingPacketTimeout.setUnits("milliseconds")


class _CiscoPingDelay_Type(Integer32):
    """Custom type ciscoPingDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_CiscoPingDelay_Type.__name__ = "Integer32"
_CiscoPingDelay_Object = MibTableColumn
ciscoPingDelay = _CiscoPingDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 7),
    _CiscoPingDelay_Type()
)
ciscoPingDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoPingDelay.setStatus("current")
if mibBuilder.loadTexts:
    ciscoPingDelay.setUnits("milliseconds")


class _CiscoPingTrapOnCompletion_Type(TruthValue):
    """Custom type ciscoPingTrapOnCompletion based on TruthValue"""


_CiscoPingTrapOnCompletion_Object = MibTableColumn
ciscoPingTrapOnCompletion = _CiscoPingTrapOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 8),
    _CiscoPingTrapOnCompletion_Type()
)
ciscoPingTrapOnCompletion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoPingTrapOnCompletion.setStatus("current")
_CiscoPingSentPackets_Type = Counter32
_CiscoPingSentPackets_Object = MibTableColumn
ciscoPingSentPackets = _CiscoPingSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 9),
    _CiscoPingSentPackets_Type()
)
ciscoPingSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoPingSentPackets.setStatus("current")
_CiscoPingReceivedPackets_Type = Counter32
_CiscoPingReceivedPackets_Object = MibTableColumn
ciscoPingReceivedPackets = _CiscoPingReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 10),
    _CiscoPingReceivedPackets_Type()
)
ciscoPingReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoPingReceivedPackets.setStatus("current")
_CiscoPingMinRtt_Type = Integer32
_CiscoPingMinRtt_Object = MibTableColumn
ciscoPingMinRtt = _CiscoPingMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 11),
    _CiscoPingMinRtt_Type()
)
ciscoPingMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoPingMinRtt.setStatus("current")
if mibBuilder.loadTexts:
    ciscoPingMinRtt.setUnits("milliseconds")
_CiscoPingAvgRtt_Type = Integer32
_CiscoPingAvgRtt_Object = MibTableColumn
ciscoPingAvgRtt = _CiscoPingAvgRtt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 12),
    _CiscoPingAvgRtt_Type()
)
ciscoPingAvgRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoPingAvgRtt.setStatus("current")
if mibBuilder.loadTexts:
    ciscoPingAvgRtt.setUnits("milliseconds")
_CiscoPingMaxRtt_Type = Integer32
_CiscoPingMaxRtt_Object = MibTableColumn
ciscoPingMaxRtt = _CiscoPingMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 13),
    _CiscoPingMaxRtt_Type()
)
ciscoPingMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoPingMaxRtt.setStatus("current")
if mibBuilder.loadTexts:
    ciscoPingMaxRtt.setUnits("milliseconds")
_CiscoPingCompleted_Type = TruthValue
_CiscoPingCompleted_Object = MibTableColumn
ciscoPingCompleted = _CiscoPingCompleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 14),
    _CiscoPingCompleted_Type()
)
ciscoPingCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoPingCompleted.setStatus("current")
_CiscoPingEntryOwner_Type = OwnerString
_CiscoPingEntryOwner_Object = MibTableColumn
ciscoPingEntryOwner = _CiscoPingEntryOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 15),
    _CiscoPingEntryOwner_Type()
)
ciscoPingEntryOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoPingEntryOwner.setStatus("current")
_CiscoPingEntryStatus_Type = RowStatus
_CiscoPingEntryStatus_Object = MibTableColumn
ciscoPingEntryStatus = _CiscoPingEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 16),
    _CiscoPingEntryStatus_Type()
)
ciscoPingEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoPingEntryStatus.setStatus("current")


class _CiscoPingVrfName_Type(OctetString):
    """Custom type ciscoPingVrfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CiscoPingVrfName_Type.__name__ = "OctetString"
_CiscoPingVrfName_Object = MibTableColumn
ciscoPingVrfName = _CiscoPingVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 1, 1, 1, 17),
    _CiscoPingVrfName_Type()
)
ciscoPingVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoPingVrfName.setStatus("current")
_CiscoPingMIBTrapPrefix_ObjectIdentity = ObjectIdentity
ciscoPingMIBTrapPrefix = _CiscoPingMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 2)
)
_CiscoPingMIBTraps_ObjectIdentity = ObjectIdentity
ciscoPingMIBTraps = _CiscoPingMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 2, 0)
)
_CiscoPingMIBConformance_ObjectIdentity = ObjectIdentity
ciscoPingMIBConformance = _CiscoPingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 3)
)
_CiscoPingMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoPingMIBCompliances = _CiscoPingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 3, 1)
)
_CiscoPingMIBGroups_ObjectIdentity = ObjectIdentity
ciscoPingMIBGroups = _CiscoPingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 3, 2)
)

# Managed Objects groups

ciscoPingMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 3, 2, 1)
)
ciscoPingMIBGroup.setObjects(
      *(("CISCO-PING-MIB", "ciscoPingProtocol"),
        ("CISCO-PING-MIB", "ciscoPingAddress"),
        ("CISCO-PING-MIB", "ciscoPingPacketCount"),
        ("CISCO-PING-MIB", "ciscoPingPacketSize"),
        ("CISCO-PING-MIB", "ciscoPingPacketTimeout"),
        ("CISCO-PING-MIB", "ciscoPingDelay"),
        ("CISCO-PING-MIB", "ciscoPingTrapOnCompletion"),
        ("CISCO-PING-MIB", "ciscoPingSentPackets"),
        ("CISCO-PING-MIB", "ciscoPingReceivedPackets"),
        ("CISCO-PING-MIB", "ciscoPingMinRtt"),
        ("CISCO-PING-MIB", "ciscoPingAvgRtt"),
        ("CISCO-PING-MIB", "ciscoPingMaxRtt"),
        ("CISCO-PING-MIB", "ciscoPingCompleted"),
        ("CISCO-PING-MIB", "ciscoPingEntryOwner"),
        ("CISCO-PING-MIB", "ciscoPingEntryStatus"))
)
if mibBuilder.loadTexts:
    ciscoPingMIBGroup.setStatus("obsolete")

ciscoPingMIBGroupVpn = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 3, 2, 2)
)
ciscoPingMIBGroupVpn.setObjects(
      *(("CISCO-PING-MIB", "ciscoPingProtocol"),
        ("CISCO-PING-MIB", "ciscoPingAddress"),
        ("CISCO-PING-MIB", "ciscoPingPacketCount"),
        ("CISCO-PING-MIB", "ciscoPingPacketSize"),
        ("CISCO-PING-MIB", "ciscoPingPacketTimeout"),
        ("CISCO-PING-MIB", "ciscoPingDelay"),
        ("CISCO-PING-MIB", "ciscoPingTrapOnCompletion"),
        ("CISCO-PING-MIB", "ciscoPingSentPackets"),
        ("CISCO-PING-MIB", "ciscoPingReceivedPackets"),
        ("CISCO-PING-MIB", "ciscoPingMinRtt"),
        ("CISCO-PING-MIB", "ciscoPingAvgRtt"),
        ("CISCO-PING-MIB", "ciscoPingMaxRtt"),
        ("CISCO-PING-MIB", "ciscoPingCompleted"),
        ("CISCO-PING-MIB", "ciscoPingEntryOwner"),
        ("CISCO-PING-MIB", "ciscoPingEntryStatus"),
        ("CISCO-PING-MIB", "ciscoPingVrfName"))
)
if mibBuilder.loadTexts:
    ciscoPingMIBGroupVpn.setStatus("current")


# Notification objects

ciscoPingCompletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 2, 0, 1)
)
ciscoPingCompletion.setObjects(
      *(("CISCO-PING-MIB", "ciscoPingCompleted"),
        ("CISCO-PING-MIB", "ciscoPingSentPackets"),
        ("CISCO-PING-MIB", "ciscoPingReceivedPackets"))
)
if mibBuilder.loadTexts:
    ciscoPingCompletion.setStatus(
        "current"
    )


# Notifications groups

ciscoPingMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 3, 2, 3)
)
ciscoPingMIBNotificationGroup.setObjects(
    ("CISCO-PING-MIB", "ciscoPingCompletion")
)
if mibBuilder.loadTexts:
    ciscoPingMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoPingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoPingMIBCompliance.setStatus(
        "obsolete"
    )

ciscoPingMIBComplianceVpn = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 16, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoPingMIBComplianceVpn.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PING-MIB",
    **{"ciscoPingMIB": ciscoPingMIB,
       "ciscoPingMIBObjects": ciscoPingMIBObjects,
       "ciscoPingTable": ciscoPingTable,
       "ciscoPingEntry": ciscoPingEntry,
       "ciscoPingSerialNumber": ciscoPingSerialNumber,
       "ciscoPingProtocol": ciscoPingProtocol,
       "ciscoPingAddress": ciscoPingAddress,
       "ciscoPingPacketCount": ciscoPingPacketCount,
       "ciscoPingPacketSize": ciscoPingPacketSize,
       "ciscoPingPacketTimeout": ciscoPingPacketTimeout,
       "ciscoPingDelay": ciscoPingDelay,
       "ciscoPingTrapOnCompletion": ciscoPingTrapOnCompletion,
       "ciscoPingSentPackets": ciscoPingSentPackets,
       "ciscoPingReceivedPackets": ciscoPingReceivedPackets,
       "ciscoPingMinRtt": ciscoPingMinRtt,
       "ciscoPingAvgRtt": ciscoPingAvgRtt,
       "ciscoPingMaxRtt": ciscoPingMaxRtt,
       "ciscoPingCompleted": ciscoPingCompleted,
       "ciscoPingEntryOwner": ciscoPingEntryOwner,
       "ciscoPingEntryStatus": ciscoPingEntryStatus,
       "ciscoPingVrfName": ciscoPingVrfName,
       "ciscoPingMIBTrapPrefix": ciscoPingMIBTrapPrefix,
       "ciscoPingMIBTraps": ciscoPingMIBTraps,
       "ciscoPingCompletion": ciscoPingCompletion,
       "ciscoPingMIBConformance": ciscoPingMIBConformance,
       "ciscoPingMIBCompliances": ciscoPingMIBCompliances,
       "ciscoPingMIBCompliance": ciscoPingMIBCompliance,
       "ciscoPingMIBComplianceVpn": ciscoPingMIBComplianceVpn,
       "ciscoPingMIBGroups": ciscoPingMIBGroups,
       "ciscoPingMIBGroup": ciscoPingMIBGroup,
       "ciscoPingMIBGroupVpn": ciscoPingMIBGroupVpn,
       "ciscoPingMIBNotificationGroup": ciscoPingMIBNotificationGroup}
)
