# SNMP MIB module (EdgeSwitch-MVR-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EdgeSwitch-MVR-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:42:54 2024
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

(fastPath,) = mibBuilder.importSymbols(
    "EdgeSwitch-REF-MIB",
    "fastPath")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

fastpathMvr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50)
)
fastpathMvr.setRevisions(
        ("2011-01-26 00:00",
         "2009-10-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MvrGlobalConfig_ObjectIdentity = ObjectIdentity
mvrGlobalConfig = _MvrGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 1)
)


class _MvrAdminMode_Type(TruthValue):
    """Custom type mvrAdminMode based on TruthValue"""


_MvrAdminMode_Object = MibScalar
mvrAdminMode = _MvrAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 1, 1),
    _MvrAdminMode_Type()
)
mvrAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrAdminMode.setStatus("current")


class _MvrModeType_Type(Integer32):
    """Custom type mvrModeType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("compatible", 1),
          ("dynamic", 2))
    )


_MvrModeType_Type.__name__ = "Integer32"
_MvrModeType_Object = MibScalar
mvrModeType = _MvrModeType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 1, 2),
    _MvrModeType_Type()
)
mvrModeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrModeType.setStatus("current")


class _MvrMulticastVlanId_Type(VlanIndex):
    """Custom type mvrMulticastVlanId based on VlanIndex"""
    defaultValue = 1


_MvrMulticastVlanId_Object = MibScalar
mvrMulticastVlanId = _MvrMulticastVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 1, 3),
    _MvrMulticastVlanId_Type()
)
mvrMulticastVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrMulticastVlanId.setStatus("current")
_MvrMaxMulticastGroupsCount_Type = Integer32
_MvrMaxMulticastGroupsCount_Object = MibScalar
mvrMaxMulticastGroupsCount = _MvrMaxMulticastGroupsCount_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 1, 4),
    _MvrMaxMulticastGroupsCount_Type()
)
mvrMaxMulticastGroupsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrMaxMulticastGroupsCount.setStatus("current")
_MvrCurrentMulticastGroupsCount_Type = Integer32
_MvrCurrentMulticastGroupsCount_Object = MibScalar
mvrCurrentMulticastGroupsCount = _MvrCurrentMulticastGroupsCount_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 1, 5),
    _MvrCurrentMulticastGroupsCount_Type()
)
mvrCurrentMulticastGroupsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrCurrentMulticastGroupsCount.setStatus("current")


class _MvrQueryTime_Type(TimeInterval):
    """Custom type mvrQueryTime based on TimeInterval"""
    defaultValue = 5

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MvrQueryTime_Type.__name__ = "TimeInterval"
_MvrQueryTime_Object = MibScalar
mvrQueryTime = _MvrQueryTime_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 1, 6),
    _MvrQueryTime_Type()
)
mvrQueryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrQueryTime.setStatus("current")
_MvrPortTable_Object = MibTable
mvrPortTable = _MvrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 2)
)
if mibBuilder.loadTexts:
    mvrPortTable.setStatus("current")
_MvrPortEntry_Object = MibTableRow
mvrPortEntry = _MvrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 2, 1)
)
mvrPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mvrPortEntry.setStatus("current")


class _MvrPortMvrEnabled_Type(TruthValue):
    """Custom type mvrPortMvrEnabled based on TruthValue"""


_MvrPortMvrEnabled_Object = MibTableColumn
mvrPortMvrEnabled = _MvrPortMvrEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 2, 1, 1),
    _MvrPortMvrEnabled_Type()
)
mvrPortMvrEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrPortMvrEnabled.setStatus("current")


class _MvrPortType_Type(Integer32):
    """Custom type mvrPortType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("receiver", 2),
          ("source", 1))
    )


_MvrPortType_Type.__name__ = "Integer32"
_MvrPortType_Object = MibTableColumn
mvrPortType = _MvrPortType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 2, 1, 2),
    _MvrPortType_Type()
)
mvrPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrPortType.setStatus("current")


class _MvrPortImmediateLeaveMode_Type(TruthValue):
    """Custom type mvrPortImmediateLeaveMode based on TruthValue"""


_MvrPortImmediateLeaveMode_Object = MibTableColumn
mvrPortImmediateLeaveMode = _MvrPortImmediateLeaveMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 2, 1, 3),
    _MvrPortImmediateLeaveMode_Type()
)
mvrPortImmediateLeaveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrPortImmediateLeaveMode.setStatus("current")


class _MvrPortStatus_Type(Integer32):
    """Custom type mvrPortStatus based on Integer32"""
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
        *(("activeInVlan", 1),
          ("activeNotInVlan", 2),
          ("inactiveInVlan", 3),
          ("inactiveNotInVlan", 4))
    )


_MvrPortStatus_Type.__name__ = "Integer32"
_MvrPortStatus_Object = MibTableColumn
mvrPortStatus = _MvrPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 2, 1, 4),
    _MvrPortStatus_Type()
)
mvrPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrPortStatus.setStatus("current")
_MvrGroupsTable_Object = MibTable
mvrGroupsTable = _MvrGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 3)
)
if mibBuilder.loadTexts:
    mvrGroupsTable.setStatus("current")
_MvrGroupEntry_Object = MibTableRow
mvrGroupEntry = _MvrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 3, 1)
)
mvrGroupEntry.setIndexNames(
    (0, "EdgeSwitch-MVR-PRIVATE-MIB", "mvrGroupIPAddress"),
)
if mibBuilder.loadTexts:
    mvrGroupEntry.setStatus("current")
_MvrGroupIPAddress_Type = IpAddress
_MvrGroupIPAddress_Object = MibTableColumn
mvrGroupIPAddress = _MvrGroupIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 3, 1, 1),
    _MvrGroupIPAddress_Type()
)
mvrGroupIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvrGroupIPAddress.setStatus("current")


class _MvrGroupStatus_Type(Integer32):
    """Custom type mvrGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_MvrGroupStatus_Type.__name__ = "Integer32"
_MvrGroupStatus_Object = MibTableColumn
mvrGroupStatus = _MvrGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 3, 1, 2),
    _MvrGroupStatus_Type()
)
mvrGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrGroupStatus.setStatus("current")
_MvrGroupRowStatus_Type = RowStatus
_MvrGroupRowStatus_Object = MibTableColumn
mvrGroupRowStatus = _MvrGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 3, 1, 3),
    _MvrGroupRowStatus_Type()
)
mvrGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvrGroupRowStatus.setStatus("current")
_MvrPortMembershipTable_Object = MibTable
mvrPortMembershipTable = _MvrPortMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 4)
)
if mibBuilder.loadTexts:
    mvrPortMembershipTable.setStatus("current")
_MvrPortMembershipEntry_Object = MibTableRow
mvrPortMembershipEntry = _MvrPortMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 4, 1)
)
mvrPortMembershipEntry.setIndexNames(
    (0, "EdgeSwitch-MVR-PRIVATE-MIB", "mvrPortMembershipGroupIPAddress"),
    (0, "EdgeSwitch-MVR-PRIVATE-MIB", "mvrPortMembershipPortIfIndex"),
)
if mibBuilder.loadTexts:
    mvrPortMembershipEntry.setStatus("current")
_MvrPortMembershipGroupIPAddress_Type = IpAddress
_MvrPortMembershipGroupIPAddress_Object = MibTableColumn
mvrPortMembershipGroupIPAddress = _MvrPortMembershipGroupIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 4, 1, 1),
    _MvrPortMembershipGroupIPAddress_Type()
)
mvrPortMembershipGroupIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvrPortMembershipGroupIPAddress.setStatus("current")
_MvrPortMembershipPortIfIndex_Type = InterfaceIndex
_MvrPortMembershipPortIfIndex_Object = MibTableColumn
mvrPortMembershipPortIfIndex = _MvrPortMembershipPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 4, 1, 2),
    _MvrPortMembershipPortIfIndex_Type()
)
mvrPortMembershipPortIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvrPortMembershipPortIfIndex.setStatus("current")
_MvrPortMembershipRowStatus_Type = RowStatus
_MvrPortMembershipRowStatus_Object = MibTableColumn
mvrPortMembershipRowStatus = _MvrPortMembershipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 4, 1, 3),
    _MvrPortMembershipRowStatus_Type()
)
mvrPortMembershipRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvrPortMembershipRowStatus.setStatus("current")
_MvrStatistics_ObjectIdentity = ObjectIdentity
mvrStatistics = _MvrStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 5)
)
_MvrIGMPQueryReceived_Type = Unsigned32
_MvrIGMPQueryReceived_Object = MibScalar
mvrIGMPQueryReceived = _MvrIGMPQueryReceived_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 5, 1),
    _MvrIGMPQueryReceived_Type()
)
mvrIGMPQueryReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrIGMPQueryReceived.setStatus("current")
_MvrIGMPReportV1Received_Type = Unsigned32
_MvrIGMPReportV1Received_Object = MibScalar
mvrIGMPReportV1Received = _MvrIGMPReportV1Received_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 5, 2),
    _MvrIGMPReportV1Received_Type()
)
mvrIGMPReportV1Received.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrIGMPReportV1Received.setStatus("current")
_MvrIGMPReportV2Received_Type = Unsigned32
_MvrIGMPReportV2Received_Object = MibScalar
mvrIGMPReportV2Received = _MvrIGMPReportV2Received_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 5, 3),
    _MvrIGMPReportV2Received_Type()
)
mvrIGMPReportV2Received.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrIGMPReportV2Received.setStatus("current")
_MvrIGMPLeaveReceived_Type = Unsigned32
_MvrIGMPLeaveReceived_Object = MibScalar
mvrIGMPLeaveReceived = _MvrIGMPLeaveReceived_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 5, 4),
    _MvrIGMPLeaveReceived_Type()
)
mvrIGMPLeaveReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrIGMPLeaveReceived.setStatus("current")
_MvrIGMPQueryTransmitted_Type = Unsigned32
_MvrIGMPQueryTransmitted_Object = MibScalar
mvrIGMPQueryTransmitted = _MvrIGMPQueryTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 5, 5),
    _MvrIGMPQueryTransmitted_Type()
)
mvrIGMPQueryTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrIGMPQueryTransmitted.setStatus("current")
_MvrIGMPReportV1Transmitted_Type = Unsigned32
_MvrIGMPReportV1Transmitted_Object = MibScalar
mvrIGMPReportV1Transmitted = _MvrIGMPReportV1Transmitted_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 5, 6),
    _MvrIGMPReportV1Transmitted_Type()
)
mvrIGMPReportV1Transmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrIGMPReportV1Transmitted.setStatus("current")
_MvrIGMPReportV2Transmitted_Type = Unsigned32
_MvrIGMPReportV2Transmitted_Object = MibScalar
mvrIGMPReportV2Transmitted = _MvrIGMPReportV2Transmitted_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 5, 7),
    _MvrIGMPReportV2Transmitted_Type()
)
mvrIGMPReportV2Transmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrIGMPReportV2Transmitted.setStatus("current")
_MvrIGMPLeaveTransmitted_Type = Unsigned32
_MvrIGMPLeaveTransmitted_Object = MibScalar
mvrIGMPLeaveTransmitted = _MvrIGMPLeaveTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 5, 8),
    _MvrIGMPLeaveTransmitted_Type()
)
mvrIGMPLeaveTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrIGMPLeaveTransmitted.setStatus("current")
_MvrIGMPPacketReceiveFailures_Type = Unsigned32
_MvrIGMPPacketReceiveFailures_Object = MibScalar
mvrIGMPPacketReceiveFailures = _MvrIGMPPacketReceiveFailures_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 5, 9),
    _MvrIGMPPacketReceiveFailures_Type()
)
mvrIGMPPacketReceiveFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrIGMPPacketReceiveFailures.setStatus("current")
_MvrIGMPPacketTransmitFailures_Type = Unsigned32
_MvrIGMPPacketTransmitFailures_Object = MibScalar
mvrIGMPPacketTransmitFailures = _MvrIGMPPacketTransmitFailures_Object(
    (1, 3, 6, 1, 4, 1, 4413, 1, 1, 50, 5, 10),
    _MvrIGMPPacketTransmitFailures_Type()
)
mvrIGMPPacketTransmitFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrIGMPPacketTransmitFailures.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EdgeSwitch-MVR-PRIVATE-MIB",
    **{"fastpathMvr": fastpathMvr,
       "mvrGlobalConfig": mvrGlobalConfig,
       "mvrAdminMode": mvrAdminMode,
       "mvrModeType": mvrModeType,
       "mvrMulticastVlanId": mvrMulticastVlanId,
       "mvrMaxMulticastGroupsCount": mvrMaxMulticastGroupsCount,
       "mvrCurrentMulticastGroupsCount": mvrCurrentMulticastGroupsCount,
       "mvrQueryTime": mvrQueryTime,
       "mvrPortTable": mvrPortTable,
       "mvrPortEntry": mvrPortEntry,
       "mvrPortMvrEnabled": mvrPortMvrEnabled,
       "mvrPortType": mvrPortType,
       "mvrPortImmediateLeaveMode": mvrPortImmediateLeaveMode,
       "mvrPortStatus": mvrPortStatus,
       "mvrGroupsTable": mvrGroupsTable,
       "mvrGroupEntry": mvrGroupEntry,
       "mvrGroupIPAddress": mvrGroupIPAddress,
       "mvrGroupStatus": mvrGroupStatus,
       "mvrGroupRowStatus": mvrGroupRowStatus,
       "mvrPortMembershipTable": mvrPortMembershipTable,
       "mvrPortMembershipEntry": mvrPortMembershipEntry,
       "mvrPortMembershipGroupIPAddress": mvrPortMembershipGroupIPAddress,
       "mvrPortMembershipPortIfIndex": mvrPortMembershipPortIfIndex,
       "mvrPortMembershipRowStatus": mvrPortMembershipRowStatus,
       "mvrStatistics": mvrStatistics,
       "mvrIGMPQueryReceived": mvrIGMPQueryReceived,
       "mvrIGMPReportV1Received": mvrIGMPReportV1Received,
       "mvrIGMPReportV2Received": mvrIGMPReportV2Received,
       "mvrIGMPLeaveReceived": mvrIGMPLeaveReceived,
       "mvrIGMPQueryTransmitted": mvrIGMPQueryTransmitted,
       "mvrIGMPReportV1Transmitted": mvrIGMPReportV1Transmitted,
       "mvrIGMPReportV2Transmitted": mvrIGMPReportV2Transmitted,
       "mvrIGMPLeaveTransmitted": mvrIGMPLeaveTransmitted,
       "mvrIGMPPacketReceiveFailures": mvrIGMPPacketReceiveFailures,
       "mvrIGMPPacketTransmitFailures": mvrIGMPPacketTransmitFailures}
)
