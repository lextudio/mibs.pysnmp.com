# SNMP MIB module (ZYXEL-IGMP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-IGMP-SNOOPING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:03 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelIgmpSnooping = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelIgmpSnoopingSetup_ObjectIdentity = ObjectIdentity
zyxelIgmpSnoopingSetup = _ZyxelIgmpSnoopingSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1)
)
_ZyIgmpSnoopingState_Type = EnabledStatus
_ZyIgmpSnoopingState_Object = MibScalar
zyIgmpSnoopingState = _ZyIgmpSnoopingState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 1),
    _ZyIgmpSnoopingState_Type()
)
zyIgmpSnoopingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIgmpSnoopingState.setStatus("current")
_ZyIgmpSnoopingGroupHostTimeout_Type = Integer32
_ZyIgmpSnoopingGroupHostTimeout_Object = MibScalar
zyIgmpSnoopingGroupHostTimeout = _ZyIgmpSnoopingGroupHostTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 2),
    _ZyIgmpSnoopingGroupHostTimeout_Type()
)
zyIgmpSnoopingGroupHostTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIgmpSnoopingGroupHostTimeout.setStatus("current")
_ZyIgmpSnooping8021pPriority_Type = Integer32
_ZyIgmpSnooping8021pPriority_Object = MibScalar
zyIgmpSnooping8021pPriority = _ZyIgmpSnooping8021pPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 3),
    _ZyIgmpSnooping8021pPriority_Type()
)
zyIgmpSnooping8021pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIgmpSnooping8021pPriority.setStatus("current")


class _ZyIgmpSnoopingVlanMode_Type(Integer32):
    """Custom type zyIgmpSnoopingVlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("fixed", 2))
    )


_ZyIgmpSnoopingVlanMode_Type.__name__ = "Integer32"
_ZyIgmpSnoopingVlanMode_Object = MibScalar
zyIgmpSnoopingVlanMode = _ZyIgmpSnoopingVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 4),
    _ZyIgmpSnoopingVlanMode_Type()
)
zyIgmpSnoopingVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIgmpSnoopingVlanMode.setStatus("current")
_ZyIgmpSnoopingMaxNumberOfVlans_Type = Integer32
_ZyIgmpSnoopingMaxNumberOfVlans_Object = MibScalar
zyIgmpSnoopingMaxNumberOfVlans = _ZyIgmpSnoopingMaxNumberOfVlans_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 5),
    _ZyIgmpSnoopingMaxNumberOfVlans_Type()
)
zyIgmpSnoopingMaxNumberOfVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingMaxNumberOfVlans.setStatus("current")
_ZyxelIgmpSnoopingVlanTable_Object = MibTable
zyxelIgmpSnoopingVlanTable = _ZyxelIgmpSnoopingVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 6)
)
if mibBuilder.loadTexts:
    zyxelIgmpSnoopingVlanTable.setStatus("current")
_ZyxelIgmpSnoopingVlanEntry_Object = MibTableRow
zyxelIgmpSnoopingVlanEntry = _ZyxelIgmpSnoopingVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 6, 1)
)
zyxelIgmpSnoopingVlanEntry.setIndexNames(
    (0, "ZYXEL-IGMP-SNOOPING-MIB", "zyIgmpSnoopingVlanVid"),
)
if mibBuilder.loadTexts:
    zyxelIgmpSnoopingVlanEntry.setStatus("current")
_ZyIgmpSnoopingVlanVid_Type = Integer32
_ZyIgmpSnoopingVlanVid_Object = MibTableColumn
zyIgmpSnoopingVlanVid = _ZyIgmpSnoopingVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 6, 1, 1),
    _ZyIgmpSnoopingVlanVid_Type()
)
zyIgmpSnoopingVlanVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIgmpSnoopingVlanVid.setStatus("current")
_ZyIgmpSnoopingVlanName_Type = DisplayString
_ZyIgmpSnoopingVlanName_Object = MibTableColumn
zyIgmpSnoopingVlanName = _ZyIgmpSnoopingVlanName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 6, 1, 2),
    _ZyIgmpSnoopingVlanName_Type()
)
zyIgmpSnoopingVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIgmpSnoopingVlanName.setStatus("current")
_ZyIgmpSnoopingVlanRowStatus_Type = RowStatus
_ZyIgmpSnoopingVlanRowStatus_Object = MibTableColumn
zyIgmpSnoopingVlanRowStatus = _ZyIgmpSnoopingVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 6, 1, 3),
    _ZyIgmpSnoopingVlanRowStatus_Type()
)
zyIgmpSnoopingVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyIgmpSnoopingVlanRowStatus.setStatus("current")
_ZyIgmpSnoopingQuerierModeState_Type = EnabledStatus
_ZyIgmpSnoopingQuerierModeState_Object = MibScalar
zyIgmpSnoopingQuerierModeState = _ZyIgmpSnoopingQuerierModeState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 7),
    _ZyIgmpSnoopingQuerierModeState_Type()
)
zyIgmpSnoopingQuerierModeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIgmpSnoopingQuerierModeState.setStatus("current")
_ZyIgmpSnoopingReportProxyState_Type = EnabledStatus
_ZyIgmpSnoopingReportProxyState_Object = MibScalar
zyIgmpSnoopingReportProxyState = _ZyIgmpSnoopingReportProxyState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 8),
    _ZyIgmpSnoopingReportProxyState_Type()
)
zyIgmpSnoopingReportProxyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIgmpSnoopingReportProxyState.setStatus("current")
_ZyxelIgmpSnoopingPortTable_Object = MibTable
zyxelIgmpSnoopingPortTable = _ZyxelIgmpSnoopingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 9)
)
if mibBuilder.loadTexts:
    zyxelIgmpSnoopingPortTable.setStatus("current")
_ZyxelIgmpSnoopingPortEntry_Object = MibTableRow
zyxelIgmpSnoopingPortEntry = _ZyxelIgmpSnoopingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 9, 1)
)
zyxelIgmpSnoopingPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelIgmpSnoopingPortEntry.setStatus("current")
_ZyIgmpSnoopingPortMaxGroupLimitedState_Type = EnabledStatus
_ZyIgmpSnoopingPortMaxGroupLimitedState_Object = MibTableColumn
zyIgmpSnoopingPortMaxGroupLimitedState = _ZyIgmpSnoopingPortMaxGroupLimitedState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 9, 1, 1),
    _ZyIgmpSnoopingPortMaxGroupLimitedState_Type()
)
zyIgmpSnoopingPortMaxGroupLimitedState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIgmpSnoopingPortMaxGroupLimitedState.setStatus("current")
_ZyIgmpSnoopingPortMaxOfGroups_Type = Integer32
_ZyIgmpSnoopingPortMaxOfGroups_Object = MibTableColumn
zyIgmpSnoopingPortMaxOfGroups = _ZyIgmpSnoopingPortMaxOfGroups_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 9, 1, 2),
    _ZyIgmpSnoopingPortMaxOfGroups_Type()
)
zyIgmpSnoopingPortMaxOfGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIgmpSnoopingPortMaxOfGroups.setStatus("current")


class _ZyIgmpSnoopingPortQuerierMode_Type(Integer32):
    """Custom type zyIgmpSnoopingPortQuerierMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("edge", 3),
          ("fixed", 2))
    )


_ZyIgmpSnoopingPortQuerierMode_Type.__name__ = "Integer32"
_ZyIgmpSnoopingPortQuerierMode_Object = MibTableColumn
zyIgmpSnoopingPortQuerierMode = _ZyIgmpSnoopingPortQuerierMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 9, 1, 3),
    _ZyIgmpSnoopingPortQuerierMode_Type()
)
zyIgmpSnoopingPortQuerierMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIgmpSnoopingPortQuerierMode.setStatus("current")


class _ZyIgmpSnoopingPortThrottlingAction_Type(Integer32):
    """Custom type zyIgmpSnoopingPortThrottlingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("replace", 2))
    )


_ZyIgmpSnoopingPortThrottlingAction_Type.__name__ = "Integer32"
_ZyIgmpSnoopingPortThrottlingAction_Object = MibTableColumn
zyIgmpSnoopingPortThrottlingAction = _ZyIgmpSnoopingPortThrottlingAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 9, 1, 4),
    _ZyIgmpSnoopingPortThrottlingAction_Type()
)
zyIgmpSnoopingPortThrottlingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIgmpSnoopingPortThrottlingAction.setStatus("current")


class _ZyIgmpSnoopingPortLeaveMode_Type(Integer32):
    """Custom type zyIgmpSnoopingPortLeaveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fast", 2),
          ("immediate", 1),
          ("normal", 0))
    )


_ZyIgmpSnoopingPortLeaveMode_Type.__name__ = "Integer32"
_ZyIgmpSnoopingPortLeaveMode_Object = MibTableColumn
zyIgmpSnoopingPortLeaveMode = _ZyIgmpSnoopingPortLeaveMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 9, 1, 5),
    _ZyIgmpSnoopingPortLeaveMode_Type()
)
zyIgmpSnoopingPortLeaveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIgmpSnoopingPortLeaveMode.setStatus("current")
_ZyIgmpSnoopingPortLeaveTimeout_Type = Integer32
_ZyIgmpSnoopingPortLeaveTimeout_Object = MibTableColumn
zyIgmpSnoopingPortLeaveTimeout = _ZyIgmpSnoopingPortLeaveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 9, 1, 6),
    _ZyIgmpSnoopingPortLeaveTimeout_Type()
)
zyIgmpSnoopingPortLeaveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIgmpSnoopingPortLeaveTimeout.setStatus("current")
_ZyIgmpSnoopingPortFastLeaveTimeout_Type = Integer32
_ZyIgmpSnoopingPortFastLeaveTimeout_Object = MibTableColumn
zyIgmpSnoopingPortFastLeaveTimeout = _ZyIgmpSnoopingPortFastLeaveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 1, 9, 1, 7),
    _ZyIgmpSnoopingPortFastLeaveTimeout_Type()
)
zyIgmpSnoopingPortFastLeaveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIgmpSnoopingPortFastLeaveTimeout.setStatus("current")
_ZyxelIgmpSnoopingStatus_ObjectIdentity = ObjectIdentity
zyxelIgmpSnoopingStatus = _ZyxelIgmpSnoopingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2)
)
_ZyxelIgmpSnoopingRecordTable_Object = MibTable
zyxelIgmpSnoopingRecordTable = _ZyxelIgmpSnoopingRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 1)
)
if mibBuilder.loadTexts:
    zyxelIgmpSnoopingRecordTable.setStatus("current")
_ZyxelIgmpSnoopingRecordEntry_Object = MibTableRow
zyxelIgmpSnoopingRecordEntry = _ZyxelIgmpSnoopingRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 1, 1)
)
zyxelIgmpSnoopingRecordEntry.setIndexNames(
    (0, "ZYXEL-IGMP-SNOOPING-MIB", "zyIgmpSnoopingRecordVid"),
    (0, "ZYXEL-IGMP-SNOOPING-MIB", "zyIgmpSnoopingRecordPort"),
    (0, "ZYXEL-IGMP-SNOOPING-MIB", "zyIgmpSnoopingRecordGroup"),
)
if mibBuilder.loadTexts:
    zyxelIgmpSnoopingRecordEntry.setStatus("current")
_ZyIgmpSnoopingRecordIndex_Type = Integer32
_ZyIgmpSnoopingRecordIndex_Object = MibTableColumn
zyIgmpSnoopingRecordIndex = _ZyIgmpSnoopingRecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 1, 1, 1),
    _ZyIgmpSnoopingRecordIndex_Type()
)
zyIgmpSnoopingRecordIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingRecordIndex.setStatus("current")
_ZyIgmpSnoopingRecordVid_Type = Integer32
_ZyIgmpSnoopingRecordVid_Object = MibTableColumn
zyIgmpSnoopingRecordVid = _ZyIgmpSnoopingRecordVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 1, 1, 2),
    _ZyIgmpSnoopingRecordVid_Type()
)
zyIgmpSnoopingRecordVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIgmpSnoopingRecordVid.setStatus("current")
_ZyIgmpSnoopingRecordPort_Type = Integer32
_ZyIgmpSnoopingRecordPort_Object = MibTableColumn
zyIgmpSnoopingRecordPort = _ZyIgmpSnoopingRecordPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 1, 1, 3),
    _ZyIgmpSnoopingRecordPort_Type()
)
zyIgmpSnoopingRecordPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIgmpSnoopingRecordPort.setStatus("current")
_ZyIgmpSnoopingRecordGroup_Type = IpAddress
_ZyIgmpSnoopingRecordGroup_Object = MibTableColumn
zyIgmpSnoopingRecordGroup = _ZyIgmpSnoopingRecordGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 1, 1, 4),
    _ZyIgmpSnoopingRecordGroup_Type()
)
zyIgmpSnoopingRecordGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIgmpSnoopingRecordGroup.setStatus("current")
_ZyIgmpSnoopingRecordTimeout_Type = Integer32
_ZyIgmpSnoopingRecordTimeout_Object = MibTableColumn
zyIgmpSnoopingRecordTimeout = _ZyIgmpSnoopingRecordTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 1, 1, 5),
    _ZyIgmpSnoopingRecordTimeout_Type()
)
zyIgmpSnoopingRecordTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingRecordTimeout.setStatus("current")
_ZyIgmpSnoopingRecordUpTime_Type = Integer32
_ZyIgmpSnoopingRecordUpTime_Object = MibTableColumn
zyIgmpSnoopingRecordUpTime = _ZyIgmpSnoopingRecordUpTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 1, 1, 6),
    _ZyIgmpSnoopingRecordUpTime_Type()
)
zyIgmpSnoopingRecordUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingRecordUpTime.setStatus("current")
_ZyxelIgmpSnoopingInfoVlanTable_Object = MibTable
zyxelIgmpSnoopingInfoVlanTable = _ZyxelIgmpSnoopingInfoVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 2)
)
if mibBuilder.loadTexts:
    zyxelIgmpSnoopingInfoVlanTable.setStatus("current")
_ZyxelIgmpSnoopingInfoVlanEntry_Object = MibTableRow
zyxelIgmpSnoopingInfoVlanEntry = _ZyxelIgmpSnoopingInfoVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 2, 1)
)
zyxelIgmpSnoopingInfoVlanEntry.setIndexNames(
    (0, "ZYXEL-IGMP-SNOOPING-MIB", "zyIgmpSnoopingInfoVlanVid"),
)
if mibBuilder.loadTexts:
    zyxelIgmpSnoopingInfoVlanEntry.setStatus("current")
_ZyIgmpSnoopingInfoVlanVid_Type = Integer32
_ZyIgmpSnoopingInfoVlanVid_Object = MibTableColumn
zyIgmpSnoopingInfoVlanVid = _ZyIgmpSnoopingInfoVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 2, 1, 1),
    _ZyIgmpSnoopingInfoVlanVid_Type()
)
zyIgmpSnoopingInfoVlanVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIgmpSnoopingInfoVlanVid.setStatus("current")


class _ZyIgmpSnoopingInfoVlanType_Type(Integer32):
    """Custom type zyIgmpSnoopingInfoVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("mvr", 2),
          ("static", 3))
    )


_ZyIgmpSnoopingInfoVlanType_Type.__name__ = "Integer32"
_ZyIgmpSnoopingInfoVlanType_Object = MibTableColumn
zyIgmpSnoopingInfoVlanType = _ZyIgmpSnoopingInfoVlanType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 2, 1, 2),
    _ZyIgmpSnoopingInfoVlanType_Type()
)
zyIgmpSnoopingInfoVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingInfoVlanType.setStatus("current")
_ZyIgmpSnoopingInfoVlanQueryPorts_Type = PortList
_ZyIgmpSnoopingInfoVlanQueryPorts_Object = MibTableColumn
zyIgmpSnoopingInfoVlanQueryPorts = _ZyIgmpSnoopingInfoVlanQueryPorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 2, 1, 3),
    _ZyIgmpSnoopingInfoVlanQueryPorts_Type()
)
zyIgmpSnoopingInfoVlanQueryPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingInfoVlanQueryPorts.setStatus("current")
_ZyxelIgmpSnoopingCountTable_Object = MibTable
zyxelIgmpSnoopingCountTable = _ZyxelIgmpSnoopingCountTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3)
)
if mibBuilder.loadTexts:
    zyxelIgmpSnoopingCountTable.setStatus("current")
_ZyxelIgmpSnoopingCountEntry_Object = MibTableRow
zyxelIgmpSnoopingCountEntry = _ZyxelIgmpSnoopingCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1)
)
zyxelIgmpSnoopingCountEntry.setIndexNames(
    (0, "ZYXEL-IGMP-SNOOPING-MIB", "zyIgmpSnoopingCountIndex"),
)
if mibBuilder.loadTexts:
    zyxelIgmpSnoopingCountEntry.setStatus("current")
_ZyIgmpSnoopingCountIndex_Type = Integer32
_ZyIgmpSnoopingCountIndex_Object = MibTableColumn
zyIgmpSnoopingCountIndex = _ZyIgmpSnoopingCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 1),
    _ZyIgmpSnoopingCountIndex_Type()
)
zyIgmpSnoopingCountIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountIndex.setStatus("current")
_ZyIgmpSnoopingCountV2QueryRx_Type = Integer32
_ZyIgmpSnoopingCountV2QueryRx_Object = MibTableColumn
zyIgmpSnoopingCountV2QueryRx = _ZyIgmpSnoopingCountV2QueryRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 2),
    _ZyIgmpSnoopingCountV2QueryRx_Type()
)
zyIgmpSnoopingCountV2QueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountV2QueryRx.setStatus("current")
_ZyIgmpSnoopingCountV2ReportRx_Type = Integer32
_ZyIgmpSnoopingCountV2ReportRx_Object = MibTableColumn
zyIgmpSnoopingCountV2ReportRx = _ZyIgmpSnoopingCountV2ReportRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 3),
    _ZyIgmpSnoopingCountV2ReportRx_Type()
)
zyIgmpSnoopingCountV2ReportRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountV2ReportRx.setStatus("current")
_ZyIgmpSnoopingCountV2LeaveRx_Type = Integer32
_ZyIgmpSnoopingCountV2LeaveRx_Object = MibTableColumn
zyIgmpSnoopingCountV2LeaveRx = _ZyIgmpSnoopingCountV2LeaveRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 4),
    _ZyIgmpSnoopingCountV2LeaveRx_Type()
)
zyIgmpSnoopingCountV2LeaveRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountV2LeaveRx.setStatus("current")
_ZyIgmpSnoopingCountV2QueryRxDrop_Type = Integer32
_ZyIgmpSnoopingCountV2QueryRxDrop_Object = MibTableColumn
zyIgmpSnoopingCountV2QueryRxDrop = _ZyIgmpSnoopingCountV2QueryRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 5),
    _ZyIgmpSnoopingCountV2QueryRxDrop_Type()
)
zyIgmpSnoopingCountV2QueryRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountV2QueryRxDrop.setStatus("current")
_ZyIgmpSnoopingCountV2ReportRxDrop_Type = Integer32
_ZyIgmpSnoopingCountV2ReportRxDrop_Object = MibTableColumn
zyIgmpSnoopingCountV2ReportRxDrop = _ZyIgmpSnoopingCountV2ReportRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 6),
    _ZyIgmpSnoopingCountV2ReportRxDrop_Type()
)
zyIgmpSnoopingCountV2ReportRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountV2ReportRxDrop.setStatus("current")
_ZyIgmpSnoopingCountV2LeaveRxDrop_Type = Integer32
_ZyIgmpSnoopingCountV2LeaveRxDrop_Object = MibTableColumn
zyIgmpSnoopingCountV2LeaveRxDrop = _ZyIgmpSnoopingCountV2LeaveRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 7),
    _ZyIgmpSnoopingCountV2LeaveRxDrop_Type()
)
zyIgmpSnoopingCountV2LeaveRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountV2LeaveRxDrop.setStatus("current")
_ZyIgmpSnoopingCountV2QueryTx_Type = Integer32
_ZyIgmpSnoopingCountV2QueryTx_Object = MibTableColumn
zyIgmpSnoopingCountV2QueryTx = _ZyIgmpSnoopingCountV2QueryTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 8),
    _ZyIgmpSnoopingCountV2QueryTx_Type()
)
zyIgmpSnoopingCountV2QueryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountV2QueryTx.setStatus("current")
_ZyIgmpSnoopingCountV2ReportTx_Type = Integer32
_ZyIgmpSnoopingCountV2ReportTx_Object = MibTableColumn
zyIgmpSnoopingCountV2ReportTx = _ZyIgmpSnoopingCountV2ReportTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 9),
    _ZyIgmpSnoopingCountV2ReportTx_Type()
)
zyIgmpSnoopingCountV2ReportTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountV2ReportTx.setStatus("current")
_ZyIgmpSnoopingCountV2LeaveTx_Type = Integer32
_ZyIgmpSnoopingCountV2LeaveTx_Object = MibTableColumn
zyIgmpSnoopingCountV2LeaveTx = _ZyIgmpSnoopingCountV2LeaveTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 10),
    _ZyIgmpSnoopingCountV2LeaveTx_Type()
)
zyIgmpSnoopingCountV2LeaveTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountV2LeaveTx.setStatus("current")
_ZyIgmpSnoopingCountV3QueryRx_Type = Integer32
_ZyIgmpSnoopingCountV3QueryRx_Object = MibTableColumn
zyIgmpSnoopingCountV3QueryRx = _ZyIgmpSnoopingCountV3QueryRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 11),
    _ZyIgmpSnoopingCountV3QueryRx_Type()
)
zyIgmpSnoopingCountV3QueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountV3QueryRx.setStatus("current")
_ZyIgmpSnoopingCountV3ReportRx_Type = Integer32
_ZyIgmpSnoopingCountV3ReportRx_Object = MibTableColumn
zyIgmpSnoopingCountV3ReportRx = _ZyIgmpSnoopingCountV3ReportRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 12),
    _ZyIgmpSnoopingCountV3ReportRx_Type()
)
zyIgmpSnoopingCountV3ReportRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountV3ReportRx.setStatus("current")
_ZyIgmpSnoopingCountV3QueryRxDrop_Type = Integer32
_ZyIgmpSnoopingCountV3QueryRxDrop_Object = MibTableColumn
zyIgmpSnoopingCountV3QueryRxDrop = _ZyIgmpSnoopingCountV3QueryRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 13),
    _ZyIgmpSnoopingCountV3QueryRxDrop_Type()
)
zyIgmpSnoopingCountV3QueryRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountV3QueryRxDrop.setStatus("current")
_ZyIgmpSnoopingCountV3ReportRxDrop_Type = Integer32
_ZyIgmpSnoopingCountV3ReportRxDrop_Object = MibTableColumn
zyIgmpSnoopingCountV3ReportRxDrop = _ZyIgmpSnoopingCountV3ReportRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 14),
    _ZyIgmpSnoopingCountV3ReportRxDrop_Type()
)
zyIgmpSnoopingCountV3ReportRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountV3ReportRxDrop.setStatus("current")
_ZyIgmpSnoopingCountV3QueryTx_Type = Integer32
_ZyIgmpSnoopingCountV3QueryTx_Object = MibTableColumn
zyIgmpSnoopingCountV3QueryTx = _ZyIgmpSnoopingCountV3QueryTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 15),
    _ZyIgmpSnoopingCountV3QueryTx_Type()
)
zyIgmpSnoopingCountV3QueryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountV3QueryTx.setStatus("current")
_ZyIgmpSnoopingCountV3ReportTx_Type = Integer32
_ZyIgmpSnoopingCountV3ReportTx_Object = MibTableColumn
zyIgmpSnoopingCountV3ReportTx = _ZyIgmpSnoopingCountV3ReportTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 3, 1, 16),
    _ZyIgmpSnoopingCountV3ReportTx_Type()
)
zyIgmpSnoopingCountV3ReportTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountV3ReportTx.setStatus("current")
_ZyxelIgmpSnoopingCountVlanTable_Object = MibTable
zyxelIgmpSnoopingCountVlanTable = _ZyxelIgmpSnoopingCountVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4)
)
if mibBuilder.loadTexts:
    zyxelIgmpSnoopingCountVlanTable.setStatus("current")
_ZyxelIgmpSnoopingCountVlanEntry_Object = MibTableRow
zyxelIgmpSnoopingCountVlanEntry = _ZyxelIgmpSnoopingCountVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1)
)
zyxelIgmpSnoopingCountVlanEntry.setIndexNames(
    (0, "ZYXEL-IGMP-SNOOPING-MIB", "zyIgmpSnoopingCountVlanVid"),
)
if mibBuilder.loadTexts:
    zyxelIgmpSnoopingCountVlanEntry.setStatus("current")
_ZyIgmpSnoopingCountVlanVid_Type = Integer32
_ZyIgmpSnoopingCountVlanVid_Object = MibTableColumn
zyIgmpSnoopingCountVlanVid = _ZyIgmpSnoopingCountVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 1),
    _ZyIgmpSnoopingCountVlanVid_Type()
)
zyIgmpSnoopingCountVlanVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountVlanVid.setStatus("current")
_ZyIgmpSnoopingCountVlanV2QueryRx_Type = Integer32
_ZyIgmpSnoopingCountVlanV2QueryRx_Object = MibTableColumn
zyIgmpSnoopingCountVlanV2QueryRx = _ZyIgmpSnoopingCountVlanV2QueryRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 2),
    _ZyIgmpSnoopingCountVlanV2QueryRx_Type()
)
zyIgmpSnoopingCountVlanV2QueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountVlanV2QueryRx.setStatus("current")
_ZyIgmpSnoopingCountVlanV2ReportRx_Type = Integer32
_ZyIgmpSnoopingCountVlanV2ReportRx_Object = MibTableColumn
zyIgmpSnoopingCountVlanV2ReportRx = _ZyIgmpSnoopingCountVlanV2ReportRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 3),
    _ZyIgmpSnoopingCountVlanV2ReportRx_Type()
)
zyIgmpSnoopingCountVlanV2ReportRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountVlanV2ReportRx.setStatus("current")
_ZyIgmpSnoopingCountVlanV2LeaveRx_Type = Integer32
_ZyIgmpSnoopingCountVlanV2LeaveRx_Object = MibTableColumn
zyIgmpSnoopingCountVlanV2LeaveRx = _ZyIgmpSnoopingCountVlanV2LeaveRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 4),
    _ZyIgmpSnoopingCountVlanV2LeaveRx_Type()
)
zyIgmpSnoopingCountVlanV2LeaveRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountVlanV2LeaveRx.setStatus("current")
_ZyIgmpSnoopingCountVlanV2QueryRxDrop_Type = Integer32
_ZyIgmpSnoopingCountVlanV2QueryRxDrop_Object = MibTableColumn
zyIgmpSnoopingCountVlanV2QueryRxDrop = _ZyIgmpSnoopingCountVlanV2QueryRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 5),
    _ZyIgmpSnoopingCountVlanV2QueryRxDrop_Type()
)
zyIgmpSnoopingCountVlanV2QueryRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountVlanV2QueryRxDrop.setStatus("current")
_ZyIgmpSnoopingCountVlanV2ReportRxDrop_Type = Integer32
_ZyIgmpSnoopingCountVlanV2ReportRxDrop_Object = MibTableColumn
zyIgmpSnoopingCountVlanV2ReportRxDrop = _ZyIgmpSnoopingCountVlanV2ReportRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 6),
    _ZyIgmpSnoopingCountVlanV2ReportRxDrop_Type()
)
zyIgmpSnoopingCountVlanV2ReportRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountVlanV2ReportRxDrop.setStatus("current")
_ZyIgmpSnoopingCountVlanV2LeaveRxDrop_Type = Integer32
_ZyIgmpSnoopingCountVlanV2LeaveRxDrop_Object = MibTableColumn
zyIgmpSnoopingCountVlanV2LeaveRxDrop = _ZyIgmpSnoopingCountVlanV2LeaveRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 7),
    _ZyIgmpSnoopingCountVlanV2LeaveRxDrop_Type()
)
zyIgmpSnoopingCountVlanV2LeaveRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountVlanV2LeaveRxDrop.setStatus("current")
_ZyIgmpSnoopingCountVlanV2QueryTx_Type = Integer32
_ZyIgmpSnoopingCountVlanV2QueryTx_Object = MibTableColumn
zyIgmpSnoopingCountVlanV2QueryTx = _ZyIgmpSnoopingCountVlanV2QueryTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 8),
    _ZyIgmpSnoopingCountVlanV2QueryTx_Type()
)
zyIgmpSnoopingCountVlanV2QueryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountVlanV2QueryTx.setStatus("current")
_ZyIgmpSnoopingCountVlanV2ReportTx_Type = Integer32
_ZyIgmpSnoopingCountVlanV2ReportTx_Object = MibTableColumn
zyIgmpSnoopingCountVlanV2ReportTx = _ZyIgmpSnoopingCountVlanV2ReportTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 9),
    _ZyIgmpSnoopingCountVlanV2ReportTx_Type()
)
zyIgmpSnoopingCountVlanV2ReportTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountVlanV2ReportTx.setStatus("current")
_ZyIgmpSnoopingCountVlanV2LeaveTx_Type = Integer32
_ZyIgmpSnoopingCountVlanV2LeaveTx_Object = MibTableColumn
zyIgmpSnoopingCountVlanV2LeaveTx = _ZyIgmpSnoopingCountVlanV2LeaveTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 10),
    _ZyIgmpSnoopingCountVlanV2LeaveTx_Type()
)
zyIgmpSnoopingCountVlanV2LeaveTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountVlanV2LeaveTx.setStatus("current")
_ZyIgmpSnoopingCountVlanV3QueryRx_Type = Integer32
_ZyIgmpSnoopingCountVlanV3QueryRx_Object = MibTableColumn
zyIgmpSnoopingCountVlanV3QueryRx = _ZyIgmpSnoopingCountVlanV3QueryRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 11),
    _ZyIgmpSnoopingCountVlanV3QueryRx_Type()
)
zyIgmpSnoopingCountVlanV3QueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountVlanV3QueryRx.setStatus("current")
_ZyIgmpSnoopingCountVlanV3ReportRx_Type = Integer32
_ZyIgmpSnoopingCountVlanV3ReportRx_Object = MibTableColumn
zyIgmpSnoopingCountVlanV3ReportRx = _ZyIgmpSnoopingCountVlanV3ReportRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 12),
    _ZyIgmpSnoopingCountVlanV3ReportRx_Type()
)
zyIgmpSnoopingCountVlanV3ReportRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountVlanV3ReportRx.setStatus("current")
_ZyIgmpSnoopingCountVlanV3QueryRxDrop_Type = Integer32
_ZyIgmpSnoopingCountVlanV3QueryRxDrop_Object = MibTableColumn
zyIgmpSnoopingCountVlanV3QueryRxDrop = _ZyIgmpSnoopingCountVlanV3QueryRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 13),
    _ZyIgmpSnoopingCountVlanV3QueryRxDrop_Type()
)
zyIgmpSnoopingCountVlanV3QueryRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountVlanV3QueryRxDrop.setStatus("current")
_ZyIgmpSnoopingCountVlanV3ReportRxDrop_Type = Integer32
_ZyIgmpSnoopingCountVlanV3ReportRxDrop_Object = MibTableColumn
zyIgmpSnoopingCountVlanV3ReportRxDrop = _ZyIgmpSnoopingCountVlanV3ReportRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 14),
    _ZyIgmpSnoopingCountVlanV3ReportRxDrop_Type()
)
zyIgmpSnoopingCountVlanV3ReportRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountVlanV3ReportRxDrop.setStatus("current")
_ZyIgmpSnoopingCountVlanV3QueryTx_Type = Integer32
_ZyIgmpSnoopingCountVlanV3QueryTx_Object = MibTableColumn
zyIgmpSnoopingCountVlanV3QueryTx = _ZyIgmpSnoopingCountVlanV3QueryTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 15),
    _ZyIgmpSnoopingCountVlanV3QueryTx_Type()
)
zyIgmpSnoopingCountVlanV3QueryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountVlanV3QueryTx.setStatus("current")
_ZyIgmpSnoopingCountVlanV3ReportTx_Type = Integer32
_ZyIgmpSnoopingCountVlanV3ReportTx_Object = MibTableColumn
zyIgmpSnoopingCountVlanV3ReportTx = _ZyIgmpSnoopingCountVlanV3ReportTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 4, 1, 16),
    _ZyIgmpSnoopingCountVlanV3ReportTx_Type()
)
zyIgmpSnoopingCountVlanV3ReportTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountVlanV3ReportTx.setStatus("current")
_ZyxelIgmpSnoopingCountPortTable_Object = MibTable
zyxelIgmpSnoopingCountPortTable = _ZyxelIgmpSnoopingCountPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 5)
)
if mibBuilder.loadTexts:
    zyxelIgmpSnoopingCountPortTable.setStatus("current")
_ZyxelIgmpSnoopingCountPortEntry_Object = MibTableRow
zyxelIgmpSnoopingCountPortEntry = _ZyxelIgmpSnoopingCountPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 5, 1)
)
zyxelIgmpSnoopingCountPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelIgmpSnoopingCountPortEntry.setStatus("current")
_ZyIgmpSnoopingCountPortV2QueryRx_Type = Integer32
_ZyIgmpSnoopingCountPortV2QueryRx_Object = MibTableColumn
zyIgmpSnoopingCountPortV2QueryRx = _ZyIgmpSnoopingCountPortV2QueryRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 5, 1, 1),
    _ZyIgmpSnoopingCountPortV2QueryRx_Type()
)
zyIgmpSnoopingCountPortV2QueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountPortV2QueryRx.setStatus("current")
_ZyIgmpSnoopingCountPortV2ReportRx_Type = Integer32
_ZyIgmpSnoopingCountPortV2ReportRx_Object = MibTableColumn
zyIgmpSnoopingCountPortV2ReportRx = _ZyIgmpSnoopingCountPortV2ReportRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 5, 1, 2),
    _ZyIgmpSnoopingCountPortV2ReportRx_Type()
)
zyIgmpSnoopingCountPortV2ReportRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountPortV2ReportRx.setStatus("current")
_ZyIgmpSnoopingCountPortV2LeaveRx_Type = Integer32
_ZyIgmpSnoopingCountPortV2LeaveRx_Object = MibTableColumn
zyIgmpSnoopingCountPortV2LeaveRx = _ZyIgmpSnoopingCountPortV2LeaveRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 5, 1, 3),
    _ZyIgmpSnoopingCountPortV2LeaveRx_Type()
)
zyIgmpSnoopingCountPortV2LeaveRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountPortV2LeaveRx.setStatus("current")
_ZyIgmpSnoopingCountPortV2ReportRxDrop_Type = Integer32
_ZyIgmpSnoopingCountPortV2ReportRxDrop_Object = MibTableColumn
zyIgmpSnoopingCountPortV2ReportRxDrop = _ZyIgmpSnoopingCountPortV2ReportRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 5, 1, 4),
    _ZyIgmpSnoopingCountPortV2ReportRxDrop_Type()
)
zyIgmpSnoopingCountPortV2ReportRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountPortV2ReportRxDrop.setStatus("current")
_ZyIgmpSnoopingCountPortV2LeaveRxDrop_Type = Integer32
_ZyIgmpSnoopingCountPortV2LeaveRxDrop_Object = MibTableColumn
zyIgmpSnoopingCountPortV2LeaveRxDrop = _ZyIgmpSnoopingCountPortV2LeaveRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 5, 1, 5),
    _ZyIgmpSnoopingCountPortV2LeaveRxDrop_Type()
)
zyIgmpSnoopingCountPortV2LeaveRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountPortV2LeaveRxDrop.setStatus("current")
_ZyIgmpSnoopingCountPortV2ReportTx_Type = Integer32
_ZyIgmpSnoopingCountPortV2ReportTx_Object = MibTableColumn
zyIgmpSnoopingCountPortV2ReportTx = _ZyIgmpSnoopingCountPortV2ReportTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 5, 1, 6),
    _ZyIgmpSnoopingCountPortV2ReportTx_Type()
)
zyIgmpSnoopingCountPortV2ReportTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountPortV2ReportTx.setStatus("current")
_ZyIgmpSnoopingCountPortV2LeaveTx_Type = Integer32
_ZyIgmpSnoopingCountPortV2LeaveTx_Object = MibTableColumn
zyIgmpSnoopingCountPortV2LeaveTx = _ZyIgmpSnoopingCountPortV2LeaveTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 5, 1, 7),
    _ZyIgmpSnoopingCountPortV2LeaveTx_Type()
)
zyIgmpSnoopingCountPortV2LeaveTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountPortV2LeaveTx.setStatus("current")
_ZyIgmpSnoopingCountPortV3QueryRx_Type = Integer32
_ZyIgmpSnoopingCountPortV3QueryRx_Object = MibTableColumn
zyIgmpSnoopingCountPortV3QueryRx = _ZyIgmpSnoopingCountPortV3QueryRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 5, 1, 8),
    _ZyIgmpSnoopingCountPortV3QueryRx_Type()
)
zyIgmpSnoopingCountPortV3QueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountPortV3QueryRx.setStatus("current")
_ZyIgmpSnoopingCountPortV3ReportRx_Type = Integer32
_ZyIgmpSnoopingCountPortV3ReportRx_Object = MibTableColumn
zyIgmpSnoopingCountPortV3ReportRx = _ZyIgmpSnoopingCountPortV3ReportRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 5, 1, 9),
    _ZyIgmpSnoopingCountPortV3ReportRx_Type()
)
zyIgmpSnoopingCountPortV3ReportRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountPortV3ReportRx.setStatus("current")
_ZyIgmpSnoopingCountPortV3ReportRxDrop_Type = Integer32
_ZyIgmpSnoopingCountPortV3ReportRxDrop_Object = MibTableColumn
zyIgmpSnoopingCountPortV3ReportRxDrop = _ZyIgmpSnoopingCountPortV3ReportRxDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 5, 1, 10),
    _ZyIgmpSnoopingCountPortV3ReportRxDrop_Type()
)
zyIgmpSnoopingCountPortV3ReportRxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountPortV3ReportRxDrop.setStatus("current")
_ZyIgmpSnoopingCountPortV3ReportTx_Type = Integer32
_ZyIgmpSnoopingCountPortV3ReportTx_Object = MibTableColumn
zyIgmpSnoopingCountPortV3ReportTx = _ZyIgmpSnoopingCountPortV3ReportTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 5, 1, 11),
    _ZyIgmpSnoopingCountPortV3ReportTx_Type()
)
zyIgmpSnoopingCountPortV3ReportTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingCountPortV3ReportTx.setStatus("current")
_ZyxelIgmpSnoopingGroupCountStatus_ObjectIdentity = ObjectIdentity
zyxelIgmpSnoopingGroupCountStatus = _ZyxelIgmpSnoopingGroupCountStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 6)
)
_ZyIgmpSnoopingGroupCountNumber_Type = Integer32
_ZyIgmpSnoopingGroupCountNumber_Object = MibScalar
zyIgmpSnoopingGroupCountNumber = _ZyIgmpSnoopingGroupCountNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 6, 1),
    _ZyIgmpSnoopingGroupCountNumber_Type()
)
zyIgmpSnoopingGroupCountNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingGroupCountNumber.setStatus("current")
_ZyxelIgmpSnoopingGroupCountVlanTable_Object = MibTable
zyxelIgmpSnoopingGroupCountVlanTable = _ZyxelIgmpSnoopingGroupCountVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 6, 2)
)
if mibBuilder.loadTexts:
    zyxelIgmpSnoopingGroupCountVlanTable.setStatus("current")
_ZyxelIgmpSnoopingGroupCountVlanEntry_Object = MibTableRow
zyxelIgmpSnoopingGroupCountVlanEntry = _ZyxelIgmpSnoopingGroupCountVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 6, 2, 1)
)
zyxelIgmpSnoopingGroupCountVlanEntry.setIndexNames(
    (0, "ZYXEL-IGMP-SNOOPING-MIB", "zyIgmpSnoopingGroupCountVlanVid"),
)
if mibBuilder.loadTexts:
    zyxelIgmpSnoopingGroupCountVlanEntry.setStatus("current")
_ZyIgmpSnoopingGroupCountVlanVid_Type = Integer32
_ZyIgmpSnoopingGroupCountVlanVid_Object = MibTableColumn
zyIgmpSnoopingGroupCountVlanVid = _ZyIgmpSnoopingGroupCountVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 6, 2, 1, 1),
    _ZyIgmpSnoopingGroupCountVlanVid_Type()
)
zyIgmpSnoopingGroupCountVlanVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIgmpSnoopingGroupCountVlanVid.setStatus("current")
_ZyIgmpSnoopingGroupCountVlanNumber_Type = Integer32
_ZyIgmpSnoopingGroupCountVlanNumber_Object = MibTableColumn
zyIgmpSnoopingGroupCountVlanNumber = _ZyIgmpSnoopingGroupCountVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 6, 2, 1, 2),
    _ZyIgmpSnoopingGroupCountVlanNumber_Type()
)
zyIgmpSnoopingGroupCountVlanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingGroupCountVlanNumber.setStatus("current")
_ZyxelIgmpSnoopingGroupCountPortTable_Object = MibTable
zyxelIgmpSnoopingGroupCountPortTable = _ZyxelIgmpSnoopingGroupCountPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 6, 3)
)
if mibBuilder.loadTexts:
    zyxelIgmpSnoopingGroupCountPortTable.setStatus("current")
_ZyxelIgmpSnoopingGroupCountPortEntry_Object = MibTableRow
zyxelIgmpSnoopingGroupCountPortEntry = _ZyxelIgmpSnoopingGroupCountPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 6, 3, 1)
)
zyxelIgmpSnoopingGroupCountPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelIgmpSnoopingGroupCountPortEntry.setStatus("current")
_ZyIgmpSnoopingGroupCountPortNumber_Type = Integer32
_ZyIgmpSnoopingGroupCountPortNumber_Object = MibTableColumn
zyIgmpSnoopingGroupCountPortNumber = _ZyIgmpSnoopingGroupCountPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 6, 3, 1, 1),
    _ZyIgmpSnoopingGroupCountPortNumber_Type()
)
zyIgmpSnoopingGroupCountPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingGroupCountPortNumber.setStatus("current")
_ZyxelIgmpSnoopingGroupStatus_ObjectIdentity = ObjectIdentity
zyxelIgmpSnoopingGroupStatus = _ZyxelIgmpSnoopingGroupStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 7)
)
_ZyxelIgmpSnoopingGroupTable_Object = MibTable
zyxelIgmpSnoopingGroupTable = _ZyxelIgmpSnoopingGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 7, 1)
)
if mibBuilder.loadTexts:
    zyxelIgmpSnoopingGroupTable.setStatus("current")
_ZyxelIgmpSnoopingGroupEntry_Object = MibTableRow
zyxelIgmpSnoopingGroupEntry = _ZyxelIgmpSnoopingGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 7, 1, 1)
)
zyxelIgmpSnoopingGroupEntry.setIndexNames(
    (0, "ZYXEL-IGMP-SNOOPING-MIB", "zyIgmpSnoopingGroupVid"),
    (0, "ZYXEL-IGMP-SNOOPING-MIB", "zyIgmpSnoopingGroupIpAddress"),
)
if mibBuilder.loadTexts:
    zyxelIgmpSnoopingGroupEntry.setStatus("current")
_ZyIgmpSnoopingGroupVid_Type = Integer32
_ZyIgmpSnoopingGroupVid_Object = MibTableColumn
zyIgmpSnoopingGroupVid = _ZyIgmpSnoopingGroupVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 7, 1, 1, 1),
    _ZyIgmpSnoopingGroupVid_Type()
)
zyIgmpSnoopingGroupVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIgmpSnoopingGroupVid.setStatus("current")
_ZyIgmpSnoopingGroupIpAddress_Type = IpAddress
_ZyIgmpSnoopingGroupIpAddress_Object = MibTableColumn
zyIgmpSnoopingGroupIpAddress = _ZyIgmpSnoopingGroupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 7, 1, 1, 2),
    _ZyIgmpSnoopingGroupIpAddress_Type()
)
zyIgmpSnoopingGroupIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIgmpSnoopingGroupIpAddress.setStatus("current")
_ZyIgmpSnoopingGroupPortCount_Type = Integer32
_ZyIgmpSnoopingGroupPortCount_Object = MibTableColumn
zyIgmpSnoopingGroupPortCount = _ZyIgmpSnoopingGroupPortCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 7, 1, 1, 3),
    _ZyIgmpSnoopingGroupPortCount_Type()
)
zyIgmpSnoopingGroupPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingGroupPortCount.setStatus("current")
_ZyIgmpSnoopingGroupPorts_Type = PortList
_ZyIgmpSnoopingGroupPorts_Object = MibTableColumn
zyIgmpSnoopingGroupPorts = _ZyIgmpSnoopingGroupPorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 7, 1, 1, 4),
    _ZyIgmpSnoopingGroupPorts_Type()
)
zyIgmpSnoopingGroupPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingGroupPorts.setStatus("current")
_ZyxelIgmpSnoopingClientTable_Object = MibTable
zyxelIgmpSnoopingClientTable = _ZyxelIgmpSnoopingClientTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 8)
)
if mibBuilder.loadTexts:
    zyxelIgmpSnoopingClientTable.setStatus("current")
_ZyxelIgmpSnoopingClientEntry_Object = MibTableRow
zyxelIgmpSnoopingClientEntry = _ZyxelIgmpSnoopingClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 8, 1)
)
zyxelIgmpSnoopingClientEntry.setIndexNames(
    (0, "ZYXEL-IGMP-SNOOPING-MIB", "zyIgmpSnoopingClientVid"),
    (0, "ZYXEL-IGMP-SNOOPING-MIB", "zyIgmpSnoopingClientPort"),
    (0, "ZYXEL-IGMP-SNOOPING-MIB", "zyIgmpSnoopingClientGroupIpAddress"),
    (0, "ZYXEL-IGMP-SNOOPING-MIB", "zyIgmpSnoopingClientIpAddress"),
)
if mibBuilder.loadTexts:
    zyxelIgmpSnoopingClientEntry.setStatus("current")
_ZyIgmpSnoopingClientVid_Type = Integer32
_ZyIgmpSnoopingClientVid_Object = MibTableColumn
zyIgmpSnoopingClientVid = _ZyIgmpSnoopingClientVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 8, 1, 1),
    _ZyIgmpSnoopingClientVid_Type()
)
zyIgmpSnoopingClientVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIgmpSnoopingClientVid.setStatus("current")
_ZyIgmpSnoopingClientPort_Type = Integer32
_ZyIgmpSnoopingClientPort_Object = MibTableColumn
zyIgmpSnoopingClientPort = _ZyIgmpSnoopingClientPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 8, 1, 2),
    _ZyIgmpSnoopingClientPort_Type()
)
zyIgmpSnoopingClientPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIgmpSnoopingClientPort.setStatus("current")
_ZyIgmpSnoopingClientGroupIpAddress_Type = IpAddress
_ZyIgmpSnoopingClientGroupIpAddress_Object = MibTableColumn
zyIgmpSnoopingClientGroupIpAddress = _ZyIgmpSnoopingClientGroupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 8, 1, 3),
    _ZyIgmpSnoopingClientGroupIpAddress_Type()
)
zyIgmpSnoopingClientGroupIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIgmpSnoopingClientGroupIpAddress.setStatus("current")
_ZyIgmpSnoopingClientIpAddress_Type = IpAddress
_ZyIgmpSnoopingClientIpAddress_Object = MibTableColumn
zyIgmpSnoopingClientIpAddress = _ZyIgmpSnoopingClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 8, 1, 4),
    _ZyIgmpSnoopingClientIpAddress_Type()
)
zyIgmpSnoopingClientIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIgmpSnoopingClientIpAddress.setStatus("current")
_ZyIgmpSnoopingClientUpTime_Type = Integer32
_ZyIgmpSnoopingClientUpTime_Object = MibTableColumn
zyIgmpSnoopingClientUpTime = _ZyIgmpSnoopingClientUpTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 8, 1, 5),
    _ZyIgmpSnoopingClientUpTime_Type()
)
zyIgmpSnoopingClientUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIgmpSnoopingClientUpTime.setStatus("current")
_ZyIgmpSnoopingStatisticsClear_Type = EnabledStatus
_ZyIgmpSnoopingStatisticsClear_Object = MibScalar
zyIgmpSnoopingStatisticsClear = _ZyIgmpSnoopingStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 9),
    _ZyIgmpSnoopingStatisticsClear_Type()
)
zyIgmpSnoopingStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIgmpSnoopingStatisticsClear.setStatus("current")
_ZyIgmpSnoopingStatisticsClearSystem_Type = EnabledStatus
_ZyIgmpSnoopingStatisticsClearSystem_Object = MibScalar
zyIgmpSnoopingStatisticsClearSystem = _ZyIgmpSnoopingStatisticsClearSystem_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 10),
    _ZyIgmpSnoopingStatisticsClearSystem_Type()
)
zyIgmpSnoopingStatisticsClearSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIgmpSnoopingStatisticsClearSystem.setStatus("current")
_ZyIgmpSnoopingStatisticsClearPort_Type = EnabledStatus
_ZyIgmpSnoopingStatisticsClearPort_Object = MibScalar
zyIgmpSnoopingStatisticsClearPort = _ZyIgmpSnoopingStatisticsClearPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 11),
    _ZyIgmpSnoopingStatisticsClearPort_Type()
)
zyIgmpSnoopingStatisticsClearPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIgmpSnoopingStatisticsClearPort.setStatus("current")
_ZyIgmpSnoopingStatisticsClearVlan_Type = EnabledStatus
_ZyIgmpSnoopingStatisticsClearVlan_Object = MibScalar
zyIgmpSnoopingStatisticsClearVlan = _ZyIgmpSnoopingStatisticsClearVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 31, 2, 12),
    _ZyIgmpSnoopingStatisticsClearVlan_Type()
)
zyIgmpSnoopingStatisticsClearVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyIgmpSnoopingStatisticsClearVlan.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-IGMP-SNOOPING-MIB",
    **{"zyxelIgmpSnooping": zyxelIgmpSnooping,
       "zyxelIgmpSnoopingSetup": zyxelIgmpSnoopingSetup,
       "zyIgmpSnoopingState": zyIgmpSnoopingState,
       "zyIgmpSnoopingGroupHostTimeout": zyIgmpSnoopingGroupHostTimeout,
       "zyIgmpSnooping8021pPriority": zyIgmpSnooping8021pPriority,
       "zyIgmpSnoopingVlanMode": zyIgmpSnoopingVlanMode,
       "zyIgmpSnoopingMaxNumberOfVlans": zyIgmpSnoopingMaxNumberOfVlans,
       "zyxelIgmpSnoopingVlanTable": zyxelIgmpSnoopingVlanTable,
       "zyxelIgmpSnoopingVlanEntry": zyxelIgmpSnoopingVlanEntry,
       "zyIgmpSnoopingVlanVid": zyIgmpSnoopingVlanVid,
       "zyIgmpSnoopingVlanName": zyIgmpSnoopingVlanName,
       "zyIgmpSnoopingVlanRowStatus": zyIgmpSnoopingVlanRowStatus,
       "zyIgmpSnoopingQuerierModeState": zyIgmpSnoopingQuerierModeState,
       "zyIgmpSnoopingReportProxyState": zyIgmpSnoopingReportProxyState,
       "zyxelIgmpSnoopingPortTable": zyxelIgmpSnoopingPortTable,
       "zyxelIgmpSnoopingPortEntry": zyxelIgmpSnoopingPortEntry,
       "zyIgmpSnoopingPortMaxGroupLimitedState": zyIgmpSnoopingPortMaxGroupLimitedState,
       "zyIgmpSnoopingPortMaxOfGroups": zyIgmpSnoopingPortMaxOfGroups,
       "zyIgmpSnoopingPortQuerierMode": zyIgmpSnoopingPortQuerierMode,
       "zyIgmpSnoopingPortThrottlingAction": zyIgmpSnoopingPortThrottlingAction,
       "zyIgmpSnoopingPortLeaveMode": zyIgmpSnoopingPortLeaveMode,
       "zyIgmpSnoopingPortLeaveTimeout": zyIgmpSnoopingPortLeaveTimeout,
       "zyIgmpSnoopingPortFastLeaveTimeout": zyIgmpSnoopingPortFastLeaveTimeout,
       "zyxelIgmpSnoopingStatus": zyxelIgmpSnoopingStatus,
       "zyxelIgmpSnoopingRecordTable": zyxelIgmpSnoopingRecordTable,
       "zyxelIgmpSnoopingRecordEntry": zyxelIgmpSnoopingRecordEntry,
       "zyIgmpSnoopingRecordIndex": zyIgmpSnoopingRecordIndex,
       "zyIgmpSnoopingRecordVid": zyIgmpSnoopingRecordVid,
       "zyIgmpSnoopingRecordPort": zyIgmpSnoopingRecordPort,
       "zyIgmpSnoopingRecordGroup": zyIgmpSnoopingRecordGroup,
       "zyIgmpSnoopingRecordTimeout": zyIgmpSnoopingRecordTimeout,
       "zyIgmpSnoopingRecordUpTime": zyIgmpSnoopingRecordUpTime,
       "zyxelIgmpSnoopingInfoVlanTable": zyxelIgmpSnoopingInfoVlanTable,
       "zyxelIgmpSnoopingInfoVlanEntry": zyxelIgmpSnoopingInfoVlanEntry,
       "zyIgmpSnoopingInfoVlanVid": zyIgmpSnoopingInfoVlanVid,
       "zyIgmpSnoopingInfoVlanType": zyIgmpSnoopingInfoVlanType,
       "zyIgmpSnoopingInfoVlanQueryPorts": zyIgmpSnoopingInfoVlanQueryPorts,
       "zyxelIgmpSnoopingCountTable": zyxelIgmpSnoopingCountTable,
       "zyxelIgmpSnoopingCountEntry": zyxelIgmpSnoopingCountEntry,
       "zyIgmpSnoopingCountIndex": zyIgmpSnoopingCountIndex,
       "zyIgmpSnoopingCountV2QueryRx": zyIgmpSnoopingCountV2QueryRx,
       "zyIgmpSnoopingCountV2ReportRx": zyIgmpSnoopingCountV2ReportRx,
       "zyIgmpSnoopingCountV2LeaveRx": zyIgmpSnoopingCountV2LeaveRx,
       "zyIgmpSnoopingCountV2QueryRxDrop": zyIgmpSnoopingCountV2QueryRxDrop,
       "zyIgmpSnoopingCountV2ReportRxDrop": zyIgmpSnoopingCountV2ReportRxDrop,
       "zyIgmpSnoopingCountV2LeaveRxDrop": zyIgmpSnoopingCountV2LeaveRxDrop,
       "zyIgmpSnoopingCountV2QueryTx": zyIgmpSnoopingCountV2QueryTx,
       "zyIgmpSnoopingCountV2ReportTx": zyIgmpSnoopingCountV2ReportTx,
       "zyIgmpSnoopingCountV2LeaveTx": zyIgmpSnoopingCountV2LeaveTx,
       "zyIgmpSnoopingCountV3QueryRx": zyIgmpSnoopingCountV3QueryRx,
       "zyIgmpSnoopingCountV3ReportRx": zyIgmpSnoopingCountV3ReportRx,
       "zyIgmpSnoopingCountV3QueryRxDrop": zyIgmpSnoopingCountV3QueryRxDrop,
       "zyIgmpSnoopingCountV3ReportRxDrop": zyIgmpSnoopingCountV3ReportRxDrop,
       "zyIgmpSnoopingCountV3QueryTx": zyIgmpSnoopingCountV3QueryTx,
       "zyIgmpSnoopingCountV3ReportTx": zyIgmpSnoopingCountV3ReportTx,
       "zyxelIgmpSnoopingCountVlanTable": zyxelIgmpSnoopingCountVlanTable,
       "zyxelIgmpSnoopingCountVlanEntry": zyxelIgmpSnoopingCountVlanEntry,
       "zyIgmpSnoopingCountVlanVid": zyIgmpSnoopingCountVlanVid,
       "zyIgmpSnoopingCountVlanV2QueryRx": zyIgmpSnoopingCountVlanV2QueryRx,
       "zyIgmpSnoopingCountVlanV2ReportRx": zyIgmpSnoopingCountVlanV2ReportRx,
       "zyIgmpSnoopingCountVlanV2LeaveRx": zyIgmpSnoopingCountVlanV2LeaveRx,
       "zyIgmpSnoopingCountVlanV2QueryRxDrop": zyIgmpSnoopingCountVlanV2QueryRxDrop,
       "zyIgmpSnoopingCountVlanV2ReportRxDrop": zyIgmpSnoopingCountVlanV2ReportRxDrop,
       "zyIgmpSnoopingCountVlanV2LeaveRxDrop": zyIgmpSnoopingCountVlanV2LeaveRxDrop,
       "zyIgmpSnoopingCountVlanV2QueryTx": zyIgmpSnoopingCountVlanV2QueryTx,
       "zyIgmpSnoopingCountVlanV2ReportTx": zyIgmpSnoopingCountVlanV2ReportTx,
       "zyIgmpSnoopingCountVlanV2LeaveTx": zyIgmpSnoopingCountVlanV2LeaveTx,
       "zyIgmpSnoopingCountVlanV3QueryRx": zyIgmpSnoopingCountVlanV3QueryRx,
       "zyIgmpSnoopingCountVlanV3ReportRx": zyIgmpSnoopingCountVlanV3ReportRx,
       "zyIgmpSnoopingCountVlanV3QueryRxDrop": zyIgmpSnoopingCountVlanV3QueryRxDrop,
       "zyIgmpSnoopingCountVlanV3ReportRxDrop": zyIgmpSnoopingCountVlanV3ReportRxDrop,
       "zyIgmpSnoopingCountVlanV3QueryTx": zyIgmpSnoopingCountVlanV3QueryTx,
       "zyIgmpSnoopingCountVlanV3ReportTx": zyIgmpSnoopingCountVlanV3ReportTx,
       "zyxelIgmpSnoopingCountPortTable": zyxelIgmpSnoopingCountPortTable,
       "zyxelIgmpSnoopingCountPortEntry": zyxelIgmpSnoopingCountPortEntry,
       "zyIgmpSnoopingCountPortV2QueryRx": zyIgmpSnoopingCountPortV2QueryRx,
       "zyIgmpSnoopingCountPortV2ReportRx": zyIgmpSnoopingCountPortV2ReportRx,
       "zyIgmpSnoopingCountPortV2LeaveRx": zyIgmpSnoopingCountPortV2LeaveRx,
       "zyIgmpSnoopingCountPortV2ReportRxDrop": zyIgmpSnoopingCountPortV2ReportRxDrop,
       "zyIgmpSnoopingCountPortV2LeaveRxDrop": zyIgmpSnoopingCountPortV2LeaveRxDrop,
       "zyIgmpSnoopingCountPortV2ReportTx": zyIgmpSnoopingCountPortV2ReportTx,
       "zyIgmpSnoopingCountPortV2LeaveTx": zyIgmpSnoopingCountPortV2LeaveTx,
       "zyIgmpSnoopingCountPortV3QueryRx": zyIgmpSnoopingCountPortV3QueryRx,
       "zyIgmpSnoopingCountPortV3ReportRx": zyIgmpSnoopingCountPortV3ReportRx,
       "zyIgmpSnoopingCountPortV3ReportRxDrop": zyIgmpSnoopingCountPortV3ReportRxDrop,
       "zyIgmpSnoopingCountPortV3ReportTx": zyIgmpSnoopingCountPortV3ReportTx,
       "zyxelIgmpSnoopingGroupCountStatus": zyxelIgmpSnoopingGroupCountStatus,
       "zyIgmpSnoopingGroupCountNumber": zyIgmpSnoopingGroupCountNumber,
       "zyxelIgmpSnoopingGroupCountVlanTable": zyxelIgmpSnoopingGroupCountVlanTable,
       "zyxelIgmpSnoopingGroupCountVlanEntry": zyxelIgmpSnoopingGroupCountVlanEntry,
       "zyIgmpSnoopingGroupCountVlanVid": zyIgmpSnoopingGroupCountVlanVid,
       "zyIgmpSnoopingGroupCountVlanNumber": zyIgmpSnoopingGroupCountVlanNumber,
       "zyxelIgmpSnoopingGroupCountPortTable": zyxelIgmpSnoopingGroupCountPortTable,
       "zyxelIgmpSnoopingGroupCountPortEntry": zyxelIgmpSnoopingGroupCountPortEntry,
       "zyIgmpSnoopingGroupCountPortNumber": zyIgmpSnoopingGroupCountPortNumber,
       "zyxelIgmpSnoopingGroupStatus": zyxelIgmpSnoopingGroupStatus,
       "zyxelIgmpSnoopingGroupTable": zyxelIgmpSnoopingGroupTable,
       "zyxelIgmpSnoopingGroupEntry": zyxelIgmpSnoopingGroupEntry,
       "zyIgmpSnoopingGroupVid": zyIgmpSnoopingGroupVid,
       "zyIgmpSnoopingGroupIpAddress": zyIgmpSnoopingGroupIpAddress,
       "zyIgmpSnoopingGroupPortCount": zyIgmpSnoopingGroupPortCount,
       "zyIgmpSnoopingGroupPorts": zyIgmpSnoopingGroupPorts,
       "zyxelIgmpSnoopingClientTable": zyxelIgmpSnoopingClientTable,
       "zyxelIgmpSnoopingClientEntry": zyxelIgmpSnoopingClientEntry,
       "zyIgmpSnoopingClientVid": zyIgmpSnoopingClientVid,
       "zyIgmpSnoopingClientPort": zyIgmpSnoopingClientPort,
       "zyIgmpSnoopingClientGroupIpAddress": zyIgmpSnoopingClientGroupIpAddress,
       "zyIgmpSnoopingClientIpAddress": zyIgmpSnoopingClientIpAddress,
       "zyIgmpSnoopingClientUpTime": zyIgmpSnoopingClientUpTime,
       "zyIgmpSnoopingStatisticsClear": zyIgmpSnoopingStatisticsClear,
       "zyIgmpSnoopingStatisticsClearSystem": zyIgmpSnoopingStatisticsClearSystem,
       "zyIgmpSnoopingStatisticsClearPort": zyIgmpSnoopingStatisticsClearPort,
       "zyIgmpSnoopingStatisticsClearVlan": zyIgmpSnoopingStatisticsClearVlan}
)
