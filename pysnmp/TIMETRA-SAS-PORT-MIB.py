# SNMP MIB module (TIMETRA-SAS-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-SAS-PORT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:04:34 2024
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

(pethPsePortDetectionStatus,
 pethPsePortEntry,
 pethPsePortIndex,
 pethPsePortPowerClassifications) = mibBuilder.importSymbols(
    "POWER-ETHERNET-MIB",
    "pethPsePortDetectionStatus",
    "pethPsePortEntry",
    "pethPsePortIndex",
    "pethPsePortPowerClassifications")

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
 MacAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")

(TmnxAlarmState,
 TmnxMDAChanType,
 TmnxPortAdminStatus,
 tmnxChassisIndex,
 tmnxChassisNotifyChassisId,
 tmnxHwConformance,
 tmnxHwNotification,
 tmnxHwObjs) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "TmnxAlarmState",
    "TmnxMDAChanType",
    "TmnxPortAdminStatus",
    "tmnxChassisIndex",
    "tmnxChassisNotifyChassisId",
    "tmnxHwConformance",
    "tmnxHwNotification",
    "tmnxHwObjs")

(timetraSRMIBModules,) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules")

(tmnxDS1Entry,
 tmnxDS1PortEntry,
 tmnxPortEntry,
 tmnxPortEtherEntry,
 tmnxPortNotifyPortId,
 tmnxPortPortID) = mibBuilder.importSymbols(
    "TIMETRA-PORT-MIB",
    "tmnxDS1Entry",
    "tmnxDS1PortEntry",
    "tmnxPortEntry",
    "tmnxPortEtherEntry",
    "tmnxPortNotifyPortId",
    "tmnxPortPortID")

(timetraSASConfs,
 timetraSASModules,
 timetraSASNotifyPrefix,
 timetraSASObjs) = mibBuilder.importSymbols(
    "TIMETRA-SAS-GLOBAL-MIB",
    "timetraSASConfs",
    "timetraSASModules",
    "timetraSASNotifyPrefix",
    "timetraSASObjs")

(ServObjDesc,
 TFCName,
 TItemDescription,
 TItemLongDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TNetworkIngressMeterId,
 TPortSchedulerCIR,
 TPortSchedulerPIR,
 TQueueId,
 TmnxActionType,
 TmnxEncapVal,
 TmnxOperState,
 TmnxPortID,
 TmnxServId) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "ServObjDesc",
    "TFCName",
    "TItemDescription",
    "TItemLongDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TNetworkIngressMeterId",
    "TPortSchedulerCIR",
    "TPortSchedulerPIR",
    "TQueueId",
    "TmnxActionType",
    "TmnxEncapVal",
    "TmnxOperState",
    "TmnxPortID",
    "TmnxServId")


# MODULE-IDENTITY

tmnxSASPortMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 6)
)
tmnxSASPortMIBModule.setRevisions(
        ("1908-01-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxSASPortConformance_ObjectIdentity = ObjectIdentity
tmnxSASPortConformance = _TmnxSASPortConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 2)
)
_TmnxSASPortCompliances_ObjectIdentity = ObjectIdentity
tmnxSASPortCompliances = _TmnxSASPortCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 2, 1)
)
_TmnxSASPortGroups_ObjectIdentity = ObjectIdentity
tmnxSASPortGroups = _TmnxSASPortGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 2, 2)
)
_TmnxSASPortObjs_ObjectIdentity = ObjectIdentity
tmnxSASPortObjs = _TmnxSASPortObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2)
)
_SasTmnxPortExtnTable_Object = MibTable
sasTmnxPortExtnTable = _SasTmnxPortExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    sasTmnxPortExtnTable.setStatus("current")
_SasTmnxPortExtnEntry_Object = MibTableRow
sasTmnxPortExtnEntry = _SasTmnxPortExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sasTmnxPortExtnEntry.setStatus("current")
_TmnxPortUplinkMode_Type = TruthValue
_TmnxPortUplinkMode_Object = MibTableColumn
tmnxPortUplinkMode = _TmnxPortUplinkMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 2, 1, 1),
    _TmnxPortUplinkMode_Type()
)
tmnxPortUplinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortUplinkMode.setStatus("current")


class _TmnxPortAccessEgressQoSPolicyId_Type(Unsigned32):
    """Custom type tmnxPortAccessEgressQoSPolicyId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxPortAccessEgressQoSPolicyId_Type.__name__ = "Unsigned32"
_TmnxPortAccessEgressQoSPolicyId_Object = MibTableColumn
tmnxPortAccessEgressQoSPolicyId = _TmnxPortAccessEgressQoSPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 2, 1, 2),
    _TmnxPortAccessEgressQoSPolicyId_Type()
)
tmnxPortAccessEgressQoSPolicyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortAccessEgressQoSPolicyId.setStatus("current")


class _TmnxPortNetworkQoSPolicyId_Type(Unsigned32):
    """Custom type tmnxPortNetworkQoSPolicyId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxPortNetworkQoSPolicyId_Type.__name__ = "Unsigned32"
_TmnxPortNetworkQoSPolicyId_Object = MibTableColumn
tmnxPortNetworkQoSPolicyId = _TmnxPortNetworkQoSPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 2, 1, 3),
    _TmnxPortNetworkQoSPolicyId_Type()
)
tmnxPortNetworkQoSPolicyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortNetworkQoSPolicyId.setStatus("current")
_TmnxPortShgName_Type = TNamedItemOrEmpty
_TmnxPortShgName_Object = MibTableColumn
tmnxPortShgName = _TmnxPortShgName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 2, 1, 4),
    _TmnxPortShgName_Type()
)
tmnxPortShgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortShgName.setStatus("current")


class _TmnxPortUseDei_Type(TruthValue):
    """Custom type tmnxPortUseDei based on TruthValue"""


_TmnxPortUseDei_Object = MibTableColumn
tmnxPortUseDei = _TmnxPortUseDei_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 2, 1, 5),
    _TmnxPortUseDei_Type()
)
tmnxPortUseDei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortUseDei.setStatus("current")
_TmnxPortOperGrpName_Type = TNamedItemOrEmpty
_TmnxPortOperGrpName_Object = MibTableColumn
tmnxPortOperGrpName = _TmnxPortOperGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 2, 1, 6),
    _TmnxPortOperGrpName_Type()
)
tmnxPortOperGrpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortOperGrpName.setStatus("current")
_TmnxPortMonitorOperGrpName_Type = TNamedItemOrEmpty
_TmnxPortMonitorOperGrpName_Object = MibTableColumn
tmnxPortMonitorOperGrpName = _TmnxPortMonitorOperGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 2, 1, 7),
    _TmnxPortMonitorOperGrpName_Type()
)
tmnxPortMonitorOperGrpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortMonitorOperGrpName.setStatus("current")
_TmnxSASPortNetIngressStatsTable_Object = MibTable
tmnxSASPortNetIngressStatsTable = _TmnxSASPortNetIngressStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 3)
)
if mibBuilder.loadTexts:
    tmnxSASPortNetIngressStatsTable.setStatus("current")
_TmnxSASPortNetIngressStatsEntry_Object = MibTableRow
tmnxSASPortNetIngressStatsEntry = _TmnxSASPortNetIngressStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 3, 1)
)
tmnxSASPortNetIngressStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-SAS-PORT-MIB", "tmnxSASPortNetIngressMeterIndex"),
)
if mibBuilder.loadTexts:
    tmnxSASPortNetIngressStatsEntry.setStatus("current")
_TmnxSASPortNetIngressMeterIndex_Type = TNetworkIngressMeterId
_TmnxSASPortNetIngressMeterIndex_Object = MibTableColumn
tmnxSASPortNetIngressMeterIndex = _TmnxSASPortNetIngressMeterIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 3, 1, 1),
    _TmnxSASPortNetIngressMeterIndex_Type()
)
tmnxSASPortNetIngressMeterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSASPortNetIngressMeterIndex.setStatus("current")
_TmnxSASPortNetIngressFwdInProfPkts_Type = Counter64
_TmnxSASPortNetIngressFwdInProfPkts_Object = MibTableColumn
tmnxSASPortNetIngressFwdInProfPkts = _TmnxSASPortNetIngressFwdInProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 3, 1, 2),
    _TmnxSASPortNetIngressFwdInProfPkts_Type()
)
tmnxSASPortNetIngressFwdInProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSASPortNetIngressFwdInProfPkts.setStatus("current")
_TmnxSASPortNetIngressFwdOutProfPkts_Type = Counter64
_TmnxSASPortNetIngressFwdOutProfPkts_Object = MibTableColumn
tmnxSASPortNetIngressFwdOutProfPkts = _TmnxSASPortNetIngressFwdOutProfPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 3, 1, 3),
    _TmnxSASPortNetIngressFwdOutProfPkts_Type()
)
tmnxSASPortNetIngressFwdOutProfPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSASPortNetIngressFwdOutProfPkts.setStatus("current")
_TmnxSASPortNetIngressFwdInProfOcts_Type = Counter64
_TmnxSASPortNetIngressFwdInProfOcts_Object = MibTableColumn
tmnxSASPortNetIngressFwdInProfOcts = _TmnxSASPortNetIngressFwdInProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 3, 1, 4),
    _TmnxSASPortNetIngressFwdInProfOcts_Type()
)
tmnxSASPortNetIngressFwdInProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSASPortNetIngressFwdInProfOcts.setStatus("current")
_TmnxSASPortNetIngressFwdOutProfOcts_Type = Counter64
_TmnxSASPortNetIngressFwdOutProfOcts_Object = MibTableColumn
tmnxSASPortNetIngressFwdOutProfOcts = _TmnxSASPortNetIngressFwdOutProfOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 3, 1, 5),
    _TmnxSASPortNetIngressFwdOutProfOcts_Type()
)
tmnxSASPortNetIngressFwdOutProfOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSASPortNetIngressFwdOutProfOcts.setStatus("current")
_SasTmnxPortEtherExtnTable_Object = MibTable
sasTmnxPortEtherExtnTable = _SasTmnxPortEtherExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 4)
)
if mibBuilder.loadTexts:
    sasTmnxPortEtherExtnTable.setStatus("current")
_SasTmnxPortEtherExtnEntry_Object = MibTableRow
sasTmnxPortEtherExtnEntry = _SasTmnxPortEtherExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    sasTmnxPortEtherExtnEntry.setStatus("current")


class _TmnxPortEtherEgressMaxBurst_Type(Integer32):
    """Custom type tmnxPortEtherEgressMaxBurst based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(32, 16384),
    )


_TmnxPortEtherEgressMaxBurst_Type.__name__ = "Integer32"
_TmnxPortEtherEgressMaxBurst_Object = MibTableColumn
tmnxPortEtherEgressMaxBurst = _TmnxPortEtherEgressMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 4, 1, 1),
    _TmnxPortEtherEgressMaxBurst_Type()
)
tmnxPortEtherEgressMaxBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherEgressMaxBurst.setStatus("current")
_TmnxPortStatsQueue1PktsFwd_Type = TruthValue
_TmnxPortStatsQueue1PktsFwd_Object = MibTableColumn
tmnxPortStatsQueue1PktsFwd = _TmnxPortStatsQueue1PktsFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 4, 1, 2),
    _TmnxPortStatsQueue1PktsFwd_Type()
)
tmnxPortStatsQueue1PktsFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortStatsQueue1PktsFwd.setStatus("current")
_TmnxPortStatsQueue2PktsFwd_Type = TruthValue
_TmnxPortStatsQueue2PktsFwd_Object = MibTableColumn
tmnxPortStatsQueue2PktsFwd = _TmnxPortStatsQueue2PktsFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 4, 1, 3),
    _TmnxPortStatsQueue2PktsFwd_Type()
)
tmnxPortStatsQueue2PktsFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortStatsQueue2PktsFwd.setStatus("current")
_TmnxPortStatsQueue3PktsFwd_Type = TruthValue
_TmnxPortStatsQueue3PktsFwd_Object = MibTableColumn
tmnxPortStatsQueue3PktsFwd = _TmnxPortStatsQueue3PktsFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 4, 1, 4),
    _TmnxPortStatsQueue3PktsFwd_Type()
)
tmnxPortStatsQueue3PktsFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortStatsQueue3PktsFwd.setStatus("current")
_TmnxPortStatsQueue4PktsFwd_Type = TruthValue
_TmnxPortStatsQueue4PktsFwd_Object = MibTableColumn
tmnxPortStatsQueue4PktsFwd = _TmnxPortStatsQueue4PktsFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 4, 1, 5),
    _TmnxPortStatsQueue4PktsFwd_Type()
)
tmnxPortStatsQueue4PktsFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortStatsQueue4PktsFwd.setStatus("current")
_TmnxPortStatsQueue5PktsFwd_Type = TruthValue
_TmnxPortStatsQueue5PktsFwd_Object = MibTableColumn
tmnxPortStatsQueue5PktsFwd = _TmnxPortStatsQueue5PktsFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 4, 1, 6),
    _TmnxPortStatsQueue5PktsFwd_Type()
)
tmnxPortStatsQueue5PktsFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortStatsQueue5PktsFwd.setStatus("current")
_TmnxPortStatsQueue6PktsFwd_Type = TruthValue
_TmnxPortStatsQueue6PktsFwd_Object = MibTableColumn
tmnxPortStatsQueue6PktsFwd = _TmnxPortStatsQueue6PktsFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 4, 1, 7),
    _TmnxPortStatsQueue6PktsFwd_Type()
)
tmnxPortStatsQueue6PktsFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortStatsQueue6PktsFwd.setStatus("current")
_TmnxPortStatsQueue7PktsFwd_Type = TruthValue
_TmnxPortStatsQueue7PktsFwd_Object = MibTableColumn
tmnxPortStatsQueue7PktsFwd = _TmnxPortStatsQueue7PktsFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 4, 1, 8),
    _TmnxPortStatsQueue7PktsFwd_Type()
)
tmnxPortStatsQueue7PktsFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortStatsQueue7PktsFwd.setStatus("current")
_TmnxPortStatsQueue8PktsFwd_Type = TruthValue
_TmnxPortStatsQueue8PktsFwd_Object = MibTableColumn
tmnxPortStatsQueue8PktsFwd = _TmnxPortStatsQueue8PktsFwd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 4, 1, 9),
    _TmnxPortStatsQueue8PktsFwd_Type()
)
tmnxPortStatsQueue8PktsFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortStatsQueue8PktsFwd.setStatus("current")


class _TmnxPortEtherEgrSchedMode_Type(Integer32):
    """Custom type tmnxPortEtherEgrSchedMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fc-based", 1),
          ("sap-based", 2))
    )


_TmnxPortEtherEgrSchedMode_Type.__name__ = "Integer32"
_TmnxPortEtherEgrSchedMode_Object = MibTableColumn
tmnxPortEtherEgrSchedMode = _TmnxPortEtherEgrSchedMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 4, 1, 10),
    _TmnxPortEtherEgrSchedMode_Type()
)
tmnxPortEtherEgrSchedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherEgrSchedMode.setStatus("current")


class _TmnxPortEtherLoopback_Type(Integer32):
    """Custom type tmnxPortEtherLoopback based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 2),
          ("none", 0))
    )


_TmnxPortEtherLoopback_Type.__name__ = "Integer32"
_TmnxPortEtherLoopback_Object = MibTableColumn
tmnxPortEtherLoopback = _TmnxPortEtherLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 4, 1, 11),
    _TmnxPortEtherLoopback_Type()
)
tmnxPortEtherLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherLoopback.setStatus("current")


class _TmnxPortEtherIpMTU_Type(Unsigned32):
    """Custom type tmnxPortEtherIpMTU based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9000),
    )


_TmnxPortEtherIpMTU_Type.__name__ = "Unsigned32"
_TmnxPortEtherIpMTU_Object = MibTableColumn
tmnxPortEtherIpMTU = _TmnxPortEtherIpMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 4, 1, 12),
    _TmnxPortEtherIpMTU_Type()
)
tmnxPortEtherIpMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherIpMTU.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPortEtherIpMTU.setUnits("bytes")


class _TmnxPortEtherClockConfig_Type(Integer32):
    """Custom type tmnxPortEtherClockConfig based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual-master", 2),
          ("manual-slave", 3),
          ("notApplicable", 0))
    )


_TmnxPortEtherClockConfig_Type.__name__ = "Integer32"
_TmnxPortEtherClockConfig_Object = MibTableColumn
tmnxPortEtherClockConfig = _TmnxPortEtherClockConfig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 4, 1, 13),
    _TmnxPortEtherClockConfig_Type()
)
tmnxPortEtherClockConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherClockConfig.setStatus("current")
_TmnxPortLoopbckServId_Type = TmnxServId
_TmnxPortLoopbckServId_Object = MibTableColumn
tmnxPortLoopbckServId = _TmnxPortLoopbckServId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 4, 1, 14),
    _TmnxPortLoopbckServId_Type()
)
tmnxPortLoopbckServId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortLoopbckServId.setStatus("current")
_TmnxPortLoopbckSapPortId_Type = TmnxPortID
_TmnxPortLoopbckSapPortId_Object = MibTableColumn
tmnxPortLoopbckSapPortId = _TmnxPortLoopbckSapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 4, 1, 15),
    _TmnxPortLoopbckSapPortId_Type()
)
tmnxPortLoopbckSapPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortLoopbckSapPortId.setStatus("current")
_TmnxPortLoopbckSapEncapVal_Type = TmnxEncapVal
_TmnxPortLoopbckSapEncapVal_Object = MibTableColumn
tmnxPortLoopbckSapEncapVal = _TmnxPortLoopbckSapEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 4, 1, 16),
    _TmnxPortLoopbckSapEncapVal_Type()
)
tmnxPortLoopbckSapEncapVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortLoopbckSapEncapVal.setStatus("current")
_TmnxPortLoopbckSrcMacAddr_Type = MacAddress
_TmnxPortLoopbckSrcMacAddr_Object = MibTableColumn
tmnxPortLoopbckSrcMacAddr = _TmnxPortLoopbckSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 4, 1, 17),
    _TmnxPortLoopbckSrcMacAddr_Type()
)
tmnxPortLoopbckSrcMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortLoopbckSrcMacAddr.setStatus("current")
_TmnxPortLoopbckDstMacAddr_Type = MacAddress
_TmnxPortLoopbckDstMacAddr_Object = MibTableColumn
tmnxPortLoopbckDstMacAddr = _TmnxPortLoopbckDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 4, 1, 18),
    _TmnxPortLoopbckDstMacAddr_Type()
)
tmnxPortLoopbckDstMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortLoopbckDstMacAddr.setStatus("current")


class _TmnxPortAccEgrSapQosMarking_Type(Integer32):
    """Custom type tmnxPortAccEgrSapQosMarking based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_TmnxPortAccEgrSapQosMarking_Type.__name__ = "Integer32"
_TmnxPortAccEgrSapQosMarking_Object = MibTableColumn
tmnxPortAccEgrSapQosMarking = _TmnxPortAccEgrSapQosMarking_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 4, 1, 19),
    _TmnxPortAccEgrSapQosMarking_Type()
)
tmnxPortAccEgrSapQosMarking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortAccEgrSapQosMarking.setStatus("current")


class _TmnxPortLldpTnlNrstBrdgeDstMac_Type(TruthValue):
    """Custom type tmnxPortLldpTnlNrstBrdgeDstMac based on TruthValue"""


_TmnxPortLldpTnlNrstBrdgeDstMac_Object = MibTableColumn
tmnxPortLldpTnlNrstBrdgeDstMac = _TmnxPortLldpTnlNrstBrdgeDstMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 4, 1, 20),
    _TmnxPortLldpTnlNrstBrdgeDstMac_Type()
)
tmnxPortLldpTnlNrstBrdgeDstMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortLldpTnlNrstBrdgeDstMac.setStatus("current")


class _TmnxPortEtherDe1OutProfile_Type(TruthValue):
    """Custom type tmnxPortEtherDe1OutProfile based on TruthValue"""


_TmnxPortEtherDe1OutProfile_Object = MibTableColumn
tmnxPortEtherDe1OutProfile = _TmnxPortEtherDe1OutProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 4, 1, 22),
    _TmnxPortEtherDe1OutProfile_Type()
)
tmnxPortEtherDe1OutProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherDe1OutProfile.setStatus("current")


class _TmnxPortEtherNwAggRateLimit_Type(Integer32):
    """Custom type tmnxPortEtherNwAggRateLimit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 100000000),
    )


_TmnxPortEtherNwAggRateLimit_Type.__name__ = "Integer32"
_TmnxPortEtherNwAggRateLimit_Object = MibTableColumn
tmnxPortEtherNwAggRateLimit = _TmnxPortEtherNwAggRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 4, 1, 23),
    _TmnxPortEtherNwAggRateLimit_Type()
)
tmnxPortEtherNwAggRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherNwAggRateLimit.setStatus("current")


class _TmnxPortEtherNwAggRateLimitCir_Type(Integer32):
    """Custom type tmnxPortEtherNwAggRateLimitCir based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_TmnxPortEtherNwAggRateLimitCir_Type.__name__ = "Integer32"
_TmnxPortEtherNwAggRateLimitCir_Object = MibTableColumn
tmnxPortEtherNwAggRateLimitCir = _TmnxPortEtherNwAggRateLimitCir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 4, 1, 28),
    _TmnxPortEtherNwAggRateLimitCir_Type()
)
tmnxPortEtherNwAggRateLimitCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherNwAggRateLimitCir.setStatus("current")


class _TmnxPortEtherNwAggRateLimitPir_Type(Integer32):
    """Custom type tmnxPortEtherNwAggRateLimitPir based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 10000000),
    )


_TmnxPortEtherNwAggRateLimitPir_Type.__name__ = "Integer32"
_TmnxPortEtherNwAggRateLimitPir_Object = MibTableColumn
tmnxPortEtherNwAggRateLimitPir = _TmnxPortEtherNwAggRateLimitPir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 4, 1, 29),
    _TmnxPortEtherNwAggRateLimitPir_Type()
)
tmnxPortEtherNwAggRateLimitPir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherNwAggRateLimitPir.setStatus("current")
_TmnxPortEtherDcommStatus_Type = TruthValue
_TmnxPortEtherDcommStatus_Object = MibTableColumn
tmnxPortEtherDcommStatus = _TmnxPortEtherDcommStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 4, 1, 30),
    _TmnxPortEtherDcommStatus_Type()
)
tmnxPortEtherDcommStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortEtherDcommStatus.setStatus("current")


class _TmnxPortEtherMulticastIngress_Type(Integer32):
    """Custom type tmnxPortEtherMulticastIngress based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip-mc", 2),
          ("l2-mc", 1))
    )


_TmnxPortEtherMulticastIngress_Type.__name__ = "Integer32"
_TmnxPortEtherMulticastIngress_Object = MibTableColumn
tmnxPortEtherMulticastIngress = _TmnxPortEtherMulticastIngress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 4, 1, 31),
    _TmnxPortEtherMulticastIngress_Type()
)
tmnxPortEtherMulticastIngress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxPortEtherMulticastIngress.setStatus("current")
_PortShgInfoTable_Object = MibTable
portShgInfoTable = _PortShgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 6)
)
if mibBuilder.loadTexts:
    portShgInfoTable.setStatus("current")
_PortShgInfoEntry_Object = MibTableRow
portShgInfoEntry = _PortShgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 6, 1)
)
portShgInfoEntry.setIndexNames(
    (1, "TIMETRA-SAS-PORT-MIB", "portShgName"),
)
if mibBuilder.loadTexts:
    portShgInfoEntry.setStatus("current")
_PortShgName_Type = TNamedItem
_PortShgName_Object = MibTableColumn
portShgName = _PortShgName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 6, 1, 1),
    _PortShgName_Type()
)
portShgName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portShgName.setStatus("current")
_PortShgRowStatus_Type = RowStatus
_PortShgRowStatus_Object = MibTableColumn
portShgRowStatus = _PortShgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 6, 1, 2),
    _PortShgRowStatus_Type()
)
portShgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portShgRowStatus.setStatus("current")
_PortShgInstanceId_Type = Unsigned32
_PortShgInstanceId_Object = MibTableColumn
portShgInstanceId = _PortShgInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 6, 1, 3),
    _PortShgInstanceId_Type()
)
portShgInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portShgInstanceId.setStatus("current")
_PortShgDescription_Type = ServObjDesc
_PortShgDescription_Object = MibTableColumn
portShgDescription = _PortShgDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 6, 1, 4),
    _PortShgDescription_Type()
)
portShgDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portShgDescription.setStatus("current")
_PortShgLastMgmtChange_Type = TimeStamp
_PortShgLastMgmtChange_Object = MibTableColumn
portShgLastMgmtChange = _PortShgLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 6, 1, 5),
    _PortShgLastMgmtChange_Type()
)
portShgLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portShgLastMgmtChange.setStatus("current")
_TmnxPortAccessEgressQueueStatsTable_Object = MibTable
tmnxPortAccessEgressQueueStatsTable = _TmnxPortAccessEgressQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 7)
)
if mibBuilder.loadTexts:
    tmnxPortAccessEgressQueueStatsTable.setStatus("current")
_TmnxPortAccessEgressQueueStatsEntry_Object = MibTableRow
tmnxPortAccessEgressQueueStatsEntry = _TmnxPortAccessEgressQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 7, 1)
)
tmnxPortAccessEgressQueueStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-SAS-PORT-MIB", "tmnxPortAccessEgressQueueStatsIndex"),
)
if mibBuilder.loadTexts:
    tmnxPortAccessEgressQueueStatsEntry.setStatus("current")


class _TmnxPortAccessEgressQueueStatsIndex_Type(TQueueId):
    """Custom type tmnxPortAccessEgressQueueStatsIndex based on TQueueId"""
    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TmnxPortAccessEgressQueueStatsIndex_Type.__name__ = "TQueueId"
_TmnxPortAccessEgressQueueStatsIndex_Object = MibTableColumn
tmnxPortAccessEgressQueueStatsIndex = _TmnxPortAccessEgressQueueStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 7, 1, 1),
    _TmnxPortAccessEgressQueueStatsIndex_Type()
)
tmnxPortAccessEgressQueueStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPortAccessEgressQueueStatsIndex.setStatus("current")
_TmnxPortAccessEgressQueueStatsFwdPkts_Type = Counter64
_TmnxPortAccessEgressQueueStatsFwdPkts_Object = MibTableColumn
tmnxPortAccessEgressQueueStatsFwdPkts = _TmnxPortAccessEgressQueueStatsFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 7, 1, 2),
    _TmnxPortAccessEgressQueueStatsFwdPkts_Type()
)
tmnxPortAccessEgressQueueStatsFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortAccessEgressQueueStatsFwdPkts.setStatus("current")
_TmnxPortAccessEgressQueueStatsFwdOcts_Type = Counter64
_TmnxPortAccessEgressQueueStatsFwdOcts_Object = MibTableColumn
tmnxPortAccessEgressQueueStatsFwdOcts = _TmnxPortAccessEgressQueueStatsFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 7, 1, 3),
    _TmnxPortAccessEgressQueueStatsFwdOcts_Type()
)
tmnxPortAccessEgressQueueStatsFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortAccessEgressQueueStatsFwdOcts.setStatus("current")
_TmnxPortAccessEgressQueueStatsDroPkts_Type = Counter64
_TmnxPortAccessEgressQueueStatsDroPkts_Object = MibTableColumn
tmnxPortAccessEgressQueueStatsDroPkts = _TmnxPortAccessEgressQueueStatsDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 7, 1, 4),
    _TmnxPortAccessEgressQueueStatsDroPkts_Type()
)
tmnxPortAccessEgressQueueStatsDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortAccessEgressQueueStatsDroPkts.setStatus("current")
_TmnxPortAccessEgressQueueStatsDroOcts_Type = Counter64
_TmnxPortAccessEgressQueueStatsDroOcts_Object = MibTableColumn
tmnxPortAccessEgressQueueStatsDroOcts = _TmnxPortAccessEgressQueueStatsDroOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 7, 1, 5),
    _TmnxPortAccessEgressQueueStatsDroOcts_Type()
)
tmnxPortAccessEgressQueueStatsDroOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortAccessEgressQueueStatsDroOcts.setStatus("current")
_TmnxPortNetEgressQueueStatsTable_Object = MibTable
tmnxPortNetEgressQueueStatsTable = _TmnxPortNetEgressQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 8)
)
if mibBuilder.loadTexts:
    tmnxPortNetEgressQueueStatsTable.setStatus("current")
_TmnxPortNetEgressQueueStatsEntry_Object = MibTableRow
tmnxPortNetEgressQueueStatsEntry = _TmnxPortNetEgressQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 8, 1)
)
tmnxPortNetEgressQueueStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-SAS-PORT-MIB", "tmnxPortNetEgressQueueStatsIndex"),
)
if mibBuilder.loadTexts:
    tmnxPortNetEgressQueueStatsEntry.setStatus("current")


class _TmnxPortNetEgressQueueStatsIndex_Type(TQueueId):
    """Custom type tmnxPortNetEgressQueueStatsIndex based on TQueueId"""
    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TmnxPortNetEgressQueueStatsIndex_Type.__name__ = "TQueueId"
_TmnxPortNetEgressQueueStatsIndex_Object = MibTableColumn
tmnxPortNetEgressQueueStatsIndex = _TmnxPortNetEgressQueueStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 8, 1, 1),
    _TmnxPortNetEgressQueueStatsIndex_Type()
)
tmnxPortNetEgressQueueStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPortNetEgressQueueStatsIndex.setStatus("current")
_TmnxPortNetEgressQueueStatsFwdPkts_Type = Counter64
_TmnxPortNetEgressQueueStatsFwdPkts_Object = MibTableColumn
tmnxPortNetEgressQueueStatsFwdPkts = _TmnxPortNetEgressQueueStatsFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 8, 1, 2),
    _TmnxPortNetEgressQueueStatsFwdPkts_Type()
)
tmnxPortNetEgressQueueStatsFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgressQueueStatsFwdPkts.setStatus("current")
_TmnxPortNetEgressQueueStatsFwdOcts_Type = Counter64
_TmnxPortNetEgressQueueStatsFwdOcts_Object = MibTableColumn
tmnxPortNetEgressQueueStatsFwdOcts = _TmnxPortNetEgressQueueStatsFwdOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 8, 1, 3),
    _TmnxPortNetEgressQueueStatsFwdOcts_Type()
)
tmnxPortNetEgressQueueStatsFwdOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgressQueueStatsFwdOcts.setStatus("current")
_TmnxPortNetEgressQueueStatsDroPkts_Type = Counter64
_TmnxPortNetEgressQueueStatsDroPkts_Object = MibTableColumn
tmnxPortNetEgressQueueStatsDroPkts = _TmnxPortNetEgressQueueStatsDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 8, 1, 4),
    _TmnxPortNetEgressQueueStatsDroPkts_Type()
)
tmnxPortNetEgressQueueStatsDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgressQueueStatsDroPkts.setStatus("current")
_TmnxPortNetEgressQueueStatsDroOcts_Type = Counter64
_TmnxPortNetEgressQueueStatsDroOcts_Object = MibTableColumn
tmnxPortNetEgressQueueStatsDroOcts = _TmnxPortNetEgressQueueStatsDroOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 8, 1, 5),
    _TmnxPortNetEgressQueueStatsDroOcts_Type()
)
tmnxPortNetEgressQueueStatsDroOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgressQueueStatsDroOcts.setStatus("current")
_TmnxPortNetEgressQueueStatsInProfDroPkts_Type = Counter64
_TmnxPortNetEgressQueueStatsInProfDroPkts_Object = MibTableColumn
tmnxPortNetEgressQueueStatsInProfDroPkts = _TmnxPortNetEgressQueueStatsInProfDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 8, 1, 6),
    _TmnxPortNetEgressQueueStatsInProfDroPkts_Type()
)
tmnxPortNetEgressQueueStatsInProfDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgressQueueStatsInProfDroPkts.setStatus("current")
_TmnxPortNetEgressQueueStatsInProfDroOcts_Type = Counter64
_TmnxPortNetEgressQueueStatsInProfDroOcts_Object = MibTableColumn
tmnxPortNetEgressQueueStatsInProfDroOcts = _TmnxPortNetEgressQueueStatsInProfDroOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 8, 1, 7),
    _TmnxPortNetEgressQueueStatsInProfDroOcts_Type()
)
tmnxPortNetEgressQueueStatsInProfDroOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgressQueueStatsInProfDroOcts.setStatus("current")
_TmnxPortNetEgressQueueStatsOutProfDroPkts_Type = Counter64
_TmnxPortNetEgressQueueStatsOutProfDroPkts_Object = MibTableColumn
tmnxPortNetEgressQueueStatsOutProfDroPkts = _TmnxPortNetEgressQueueStatsOutProfDroPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 8, 1, 8),
    _TmnxPortNetEgressQueueStatsOutProfDroPkts_Type()
)
tmnxPortNetEgressQueueStatsOutProfDroPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgressQueueStatsOutProfDroPkts.setStatus("current")
_TmnxPortNetEgressQueueStatsOutProfDroOcts_Type = Counter64
_TmnxPortNetEgressQueueStatsOutProfDroOcts_Object = MibTableColumn
tmnxPortNetEgressQueueStatsOutProfDroOcts = _TmnxPortNetEgressQueueStatsOutProfDroOcts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 8, 1, 9),
    _TmnxPortNetEgressQueueStatsOutProfDroOcts_Type()
)
tmnxPortNetEgressQueueStatsOutProfDroOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPortNetEgressQueueStatsOutProfDroOcts.setStatus("current")
_AluExtTmnxDS1PortTable_Object = MibTable
aluExtTmnxDS1PortTable = _AluExtTmnxDS1PortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 9)
)
if mibBuilder.loadTexts:
    aluExtTmnxDS1PortTable.setStatus("current")
_AluExtTmnxDS1PortEntry_Object = MibTableRow
aluExtTmnxDS1PortEntry = _AluExtTmnxDS1PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 9, 1)
)
if mibBuilder.loadTexts:
    aluExtTmnxDS1PortEntry.setStatus("current")


class _AluExtDS1PortLineImpedance_Type(Integer32):
    """Custom type aluExtDS1PortLineImpedance based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("impedance100Ohms", 2),
          ("impedance120Ohms", 3),
          ("impedance75Ohms", 1),
          ("notApplicable", 0))
    )


_AluExtDS1PortLineImpedance_Type.__name__ = "Integer32"
_AluExtDS1PortLineImpedance_Object = MibTableColumn
aluExtDS1PortLineImpedance = _AluExtDS1PortLineImpedance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 9, 1, 1),
    _AluExtDS1PortLineImpedance_Type()
)
aluExtDS1PortLineImpedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtDS1PortLineImpedance.setStatus("current")
_AluPortAcrClkStatsTable_Object = MibTable
aluPortAcrClkStatsTable = _AluPortAcrClkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 10)
)
if mibBuilder.loadTexts:
    aluPortAcrClkStatsTable.setStatus("current")
_AluPortAcrClkStatsEntry_Object = MibTableRow
aluPortAcrClkStatsEntry = _AluPortAcrClkStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 10, 1)
)
aluPortAcrClkStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
)
if mibBuilder.loadTexts:
    aluPortAcrClkStatsEntry.setStatus("current")
_AluLastUpdateTime_Type = TimeStamp
_AluLastUpdateTime_Object = MibTableColumn
aluLastUpdateTime = _AluLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 10, 1, 1),
    _AluLastUpdateTime_Type()
)
aluLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluLastUpdateTime.setStatus("current")
_AluTotalMinutesIn24Hour_Type = Unsigned32
_AluTotalMinutesIn24Hour_Object = MibTableColumn
aluTotalMinutesIn24Hour = _AluTotalMinutesIn24Hour_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 10, 1, 2),
    _AluTotalMinutesIn24Hour_Type()
)
aluTotalMinutesIn24Hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluTotalMinutesIn24Hour.setStatus("current")
_AluCurrent24HourFreqOffsetMeanPpb_Type = Integer32
_AluCurrent24HourFreqOffsetMeanPpb_Object = MibTableColumn
aluCurrent24HourFreqOffsetMeanPpb = _AluCurrent24HourFreqOffsetMeanPpb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 10, 1, 3),
    _AluCurrent24HourFreqOffsetMeanPpb_Type()
)
aluCurrent24HourFreqOffsetMeanPpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluCurrent24HourFreqOffsetMeanPpb.setStatus("current")
_AluCurrent24HourFreqOffsetStdDevPpb_Type = Unsigned32
_AluCurrent24HourFreqOffsetStdDevPpb_Object = MibTableColumn
aluCurrent24HourFreqOffsetStdDevPpb = _AluCurrent24HourFreqOffsetStdDevPpb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 10, 1, 4),
    _AluCurrent24HourFreqOffsetStdDevPpb_Type()
)
aluCurrent24HourFreqOffsetStdDevPpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluCurrent24HourFreqOffsetStdDevPpb.setStatus("current")
_AluMaxShortIntervalMinutes_Type = Unsigned32
_AluMaxShortIntervalMinutes_Object = MibTableColumn
aluMaxShortIntervalMinutes = _AluMaxShortIntervalMinutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 10, 1, 5),
    _AluMaxShortIntervalMinutes_Type()
)
aluMaxShortIntervalMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluMaxShortIntervalMinutes.setStatus("current")
_AluTotalShortIntervalMinutes_Type = Unsigned32
_AluTotalShortIntervalMinutes_Object = MibTableColumn
aluTotalShortIntervalMinutes = _AluTotalShortIntervalMinutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 10, 1, 6),
    _AluTotalShortIntervalMinutes_Type()
)
aluTotalShortIntervalMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluTotalShortIntervalMinutes.setStatus("current")
_AluCurrent1MinValidData_Type = TruthValue
_AluCurrent1MinValidData_Object = MibTableColumn
aluCurrent1MinValidData = _AluCurrent1MinValidData_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 10, 1, 7),
    _AluCurrent1MinValidData_Type()
)
aluCurrent1MinValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluCurrent1MinValidData.setStatus("current")
_AluCurrent1MinPhaseErrorMeanPpb_Type = Integer32
_AluCurrent1MinPhaseErrorMeanPpb_Object = MibTableColumn
aluCurrent1MinPhaseErrorMeanPpb = _AluCurrent1MinPhaseErrorMeanPpb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 10, 1, 8),
    _AluCurrent1MinPhaseErrorMeanPpb_Type()
)
aluCurrent1MinPhaseErrorMeanPpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluCurrent1MinPhaseErrorMeanPpb.setStatus("current")
_AluCurrent1MinPhaseErrorStdDevNs_Type = Unsigned32
_AluCurrent1MinPhaseErrorStdDevNs_Object = MibTableColumn
aluCurrent1MinPhaseErrorStdDevNs = _AluCurrent1MinPhaseErrorStdDevNs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 10, 1, 9),
    _AluCurrent1MinPhaseErrorStdDevNs_Type()
)
aluCurrent1MinPhaseErrorStdDevNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluCurrent1MinPhaseErrorStdDevNs.setStatus("current")
_AluCurrent1MinPhaseErrorMeanNs_Type = Integer32
_AluCurrent1MinPhaseErrorMeanNs_Object = MibTableColumn
aluCurrent1MinPhaseErrorMeanNs = _AluCurrent1MinPhaseErrorMeanNs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 10, 1, 10),
    _AluCurrent1MinPhaseErrorMeanNs_Type()
)
aluCurrent1MinPhaseErrorMeanNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluCurrent1MinPhaseErrorMeanNs.setStatus("current")
_AluCurrent1MinFreqOffsetMeanPpb_Type = Integer32
_AluCurrent1MinFreqOffsetMeanPpb_Object = MibTableColumn
aluCurrent1MinFreqOffsetMeanPpb = _AluCurrent1MinFreqOffsetMeanPpb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 10, 1, 11),
    _AluCurrent1MinFreqOffsetMeanPpb_Type()
)
aluCurrent1MinFreqOffsetMeanPpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluCurrent1MinFreqOffsetMeanPpb.setStatus("current")
_AluCurrent1MinFreqOffsetStdDevPpb_Type = Unsigned32
_AluCurrent1MinFreqOffsetStdDevPpb_Object = MibTableColumn
aluCurrent1MinFreqOffsetStdDevPpb = _AluCurrent1MinFreqOffsetStdDevPpb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 10, 1, 12),
    _AluCurrent1MinFreqOffsetStdDevPpb_Type()
)
aluCurrent1MinFreqOffsetStdDevPpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluCurrent1MinFreqOffsetStdDevPpb.setStatus("current")
_AluPortAcrClkStatsShortIntervalTable_Object = MibTable
aluPortAcrClkStatsShortIntervalTable = _AluPortAcrClkStatsShortIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 11)
)
if mibBuilder.loadTexts:
    aluPortAcrClkStatsShortIntervalTable.setStatus("current")
_AluPortAcrClkStatsShortIntervalEntry_Object = MibTableRow
aluPortAcrClkStatsShortIntervalEntry = _AluPortAcrClkStatsShortIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 11, 1)
)
aluPortAcrClkStatsShortIntervalEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-PORT-MIB", "tmnxPortPortID"),
    (0, "TIMETRA-SAS-PORT-MIB", "aluIntervalNumber"),
)
if mibBuilder.loadTexts:
    aluPortAcrClkStatsShortIntervalEntry.setStatus("current")


class _AluIntervalNumber_Type(Integer32):
    """Custom type aluIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_AluIntervalNumber_Type.__name__ = "Integer32"
_AluIntervalNumber_Object = MibTableColumn
aluIntervalNumber = _AluIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 11, 1, 1),
    _AluIntervalNumber_Type()
)
aluIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIntervalNumber.setStatus("current")
_AluIntervalValidData_Type = TruthValue
_AluIntervalValidData_Object = MibTableColumn
aluIntervalValidData = _AluIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 11, 1, 2),
    _AluIntervalValidData_Type()
)
aluIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIntervalValidData.setStatus("current")
_AluIntervalUpdateTime_Type = TimeStamp
_AluIntervalUpdateTime_Object = MibTableColumn
aluIntervalUpdateTime = _AluIntervalUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 11, 1, 3),
    _AluIntervalUpdateTime_Type()
)
aluIntervalUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIntervalUpdateTime.setStatus("current")
_AluIntervalPhaseErrorMeanPpb_Type = Integer32
_AluIntervalPhaseErrorMeanPpb_Object = MibTableColumn
aluIntervalPhaseErrorMeanPpb = _AluIntervalPhaseErrorMeanPpb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 11, 1, 4),
    _AluIntervalPhaseErrorMeanPpb_Type()
)
aluIntervalPhaseErrorMeanPpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIntervalPhaseErrorMeanPpb.setStatus("current")
_AluIntervalPhaseErrorStdDevNs_Type = Unsigned32
_AluIntervalPhaseErrorStdDevNs_Object = MibTableColumn
aluIntervalPhaseErrorStdDevNs = _AluIntervalPhaseErrorStdDevNs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 11, 1, 5),
    _AluIntervalPhaseErrorStdDevNs_Type()
)
aluIntervalPhaseErrorStdDevNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIntervalPhaseErrorStdDevNs.setStatus("current")
_AluIntervalPhaseErrorMeanNs_Type = Integer32
_AluIntervalPhaseErrorMeanNs_Object = MibTableColumn
aluIntervalPhaseErrorMeanNs = _AluIntervalPhaseErrorMeanNs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 11, 1, 6),
    _AluIntervalPhaseErrorMeanNs_Type()
)
aluIntervalPhaseErrorMeanNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIntervalPhaseErrorMeanNs.setStatus("current")
_AluIntervalFreqOffsetMeanPpb_Type = Integer32
_AluIntervalFreqOffsetMeanPpb_Object = MibTableColumn
aluIntervalFreqOffsetMeanPpb = _AluIntervalFreqOffsetMeanPpb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 11, 1, 7),
    _AluIntervalFreqOffsetMeanPpb_Type()
)
aluIntervalFreqOffsetMeanPpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIntervalFreqOffsetMeanPpb.setStatus("current")
_AluIntervalFreqOffsetStdDevPpb_Type = Unsigned32
_AluIntervalFreqOffsetStdDevPpb_Object = MibTableColumn
aluIntervalFreqOffsetStdDevPpb = _AluIntervalFreqOffsetStdDevPpb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 11, 1, 8),
    _AluIntervalFreqOffsetStdDevPpb_Type()
)
aluIntervalFreqOffsetStdDevPpb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluIntervalFreqOffsetStdDevPpb.setStatus("current")
_AluExtTmnxDS1Table_Object = MibTable
aluExtTmnxDS1Table = _AluExtTmnxDS1Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 12)
)
if mibBuilder.loadTexts:
    aluExtTmnxDS1Table.setStatus("current")
_AluExtTmnxDS1Entry_Object = MibTableRow
aluExtTmnxDS1Entry = _AluExtTmnxDS1Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 12, 1)
)
if mibBuilder.loadTexts:
    aluExtTmnxDS1Entry.setStatus("current")


class _AluExtDS1SignalBitsState_Type(OctetString):
    """Custom type aluExtDS1SignalBitsState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_AluExtDS1SignalBitsState_Type.__name__ = "OctetString"
_AluExtDS1SignalBitsState_Object = MibTableColumn
aluExtDS1SignalBitsState = _AluExtDS1SignalBitsState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 12, 1, 3),
    _AluExtDS1SignalBitsState_Type()
)
aluExtDS1SignalBitsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtDS1SignalBitsState.setStatus("current")
_AluExtPethPsePortTable_Object = MibTable
aluExtPethPsePortTable = _AluExtPethPsePortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 13)
)
if mibBuilder.loadTexts:
    aluExtPethPsePortTable.setStatus("current")
_AluExtPethPsePortEntry_Object = MibTableRow
aluExtPethPsePortEntry = _AluExtPethPsePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 13, 1)
)
if mibBuilder.loadTexts:
    aluExtPethPsePortEntry.setStatus("current")


class _AluExtPethPsePortFaultReason_Type(Integer32):
    """Custom type aluExtPethPsePortFaultReason based on Integer32"""
    defaultValue = 1

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
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("dcn", 8),
          ("dcp", 2),
          ("detok", 5),
          ("dis", 12),
          ("hicap", 3),
          ("icv", 10),
          ("none", 1),
          ("open", 7),
          ("pdeny", 14),
          ("rhigh", 6),
          ("rlow", 4),
          ("sup", 13),
          ("tcut", 11),
          ("tstart", 9))
    )


_AluExtPethPsePortFaultReason_Type.__name__ = "Integer32"
_AluExtPethPsePortFaultReason_Object = MibTableColumn
aluExtPethPsePortFaultReason = _AluExtPethPsePortFaultReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 13, 1, 1),
    _AluExtPethPsePortFaultReason_Type()
)
aluExtPethPsePortFaultReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtPethPsePortFaultReason.setStatus("current")


class _AluExtPethPsePortPowerLevel_Type(Integer32):
    """Custom type aluExtPethPsePortPowerLevel based on Integer32"""
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
        *(("none", 1),
          ("plus", 3),
          ("standard", 2))
    )


_AluExtPethPsePortPowerLevel_Type.__name__ = "Integer32"
_AluExtPethPsePortPowerLevel_Object = MibTableColumn
aluExtPethPsePortPowerLevel = _AluExtPethPsePortPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 13, 1, 2),
    _AluExtPethPsePortPowerLevel_Type()
)
aluExtPethPsePortPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtPethPsePortPowerLevel.setStatus("current")


class _AluExtPethPsePortOperStatus_Type(Integer32):
    """Custom type aluExtPethPsePortOperStatus based on Integer32"""
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
        *(("notApplicable", 1),
          ("off", 3),
          ("on", 2))
    )


_AluExtPethPsePortOperStatus_Type.__name__ = "Integer32"
_AluExtPethPsePortOperStatus_Object = MibTableColumn
aluExtPethPsePortOperStatus = _AluExtPethPsePortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 13, 1, 3),
    _AluExtPethPsePortOperStatus_Type()
)
aluExtPethPsePortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtPethPsePortOperStatus.setStatus("current")
_PethPsePortEventInfo_Type = OctetString
_PethPsePortEventInfo_Object = MibScalar
pethPsePortEventInfo = _PethPsePortEventInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 14),
    _PethPsePortEventInfo_Type()
)
pethPsePortEventInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pethPsePortEventInfo.setStatus("current")
_TmnxVirtualPortTable_Object = MibTable
tmnxVirtualPortTable = _TmnxVirtualPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 15)
)
if mibBuilder.loadTexts:
    tmnxVirtualPortTable.setStatus("current")
_TmnxVirtualPortEntry_Object = MibTableRow
tmnxVirtualPortEntry = _TmnxVirtualPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 15, 1)
)
tmnxVirtualPortEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-SAS-PORT-MIB", "tmnxVirtualPortPortID"),
)
if mibBuilder.loadTexts:
    tmnxVirtualPortEntry.setStatus("current")
_TmnxVirtualPortPortID_Type = TmnxPortID
_TmnxVirtualPortPortID_Object = MibTableColumn
tmnxVirtualPortPortID = _TmnxVirtualPortPortID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 15, 1, 1),
    _TmnxVirtualPortPortID_Type()
)
tmnxVirtualPortPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxVirtualPortPortID.setStatus("current")


class _TmnxVirtualPortInUse_Type(Integer32):
    """Custom type tmnxVirtualPortInUse based on Integer32"""
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
        *(("macswap", 3),
          ("mirror", 2),
          ("not-in-use", 1),
          ("testhead", 4))
    )


_TmnxVirtualPortInUse_Type.__name__ = "Integer32"
_TmnxVirtualPortInUse_Object = MibTableColumn
tmnxVirtualPortInUse = _TmnxVirtualPortInUse_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 15, 1, 2),
    _TmnxVirtualPortInUse_Type()
)
tmnxVirtualPortInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVirtualPortInUse.setStatus("current")


class _TmnxVirtualPortSpeed_Type(Integer32):
    """Custom type tmnxVirtualPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one-gig", 1),
          ("ten-gig", 2))
    )


_TmnxVirtualPortSpeed_Type.__name__ = "Integer32"
_TmnxVirtualPortSpeed_Object = MibTableColumn
tmnxVirtualPortSpeed = _TmnxVirtualPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 2, 15, 1, 3),
    _TmnxVirtualPortSpeed_Type()
)
tmnxVirtualPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxVirtualPortSpeed.setStatus("current")
_TmnxSASPortNotificationObjects_ObjectIdentity = ObjectIdentity
tmnxSASPortNotificationObjects = _TmnxSASPortNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 3)
)
_TmnxSASPortStatsObjs_ObjectIdentity = ObjectIdentity
tmnxSASPortStatsObjs = _TmnxSASPortStatsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 4)
)
tmnxPortEntry.registerAugmentions(
    ("TIMETRA-SAS-PORT-MIB",
     "sasTmnxPortExtnEntry")
)
sasTmnxPortExtnEntry.setIndexNames(*tmnxPortEntry.getIndexNames())
tmnxPortEtherEntry.registerAugmentions(
    ("TIMETRA-SAS-PORT-MIB",
     "sasTmnxPortEtherExtnEntry")
)
sasTmnxPortEtherExtnEntry.setIndexNames(*tmnxPortEtherEntry.getIndexNames())
tmnxDS1PortEntry.registerAugmentions(
    ("TIMETRA-SAS-PORT-MIB",
     "aluExtTmnxDS1PortEntry")
)
aluExtTmnxDS1PortEntry.setIndexNames(*tmnxDS1PortEntry.getIndexNames())
tmnxDS1Entry.registerAugmentions(
    ("TIMETRA-SAS-PORT-MIB",
     "aluExtTmnxDS1Entry")
)
aluExtTmnxDS1Entry.setIndexNames(*tmnxDS1Entry.getIndexNames())
pethPsePortEntry.registerAugmentions(
    ("TIMETRA-SAS-PORT-MIB",
     "aluExtPethPsePortEntry")
)
aluExtPethPsePortEntry.setIndexNames(*pethPsePortEntry.getIndexNames())

# Managed Objects groups

tmnxSASPortV1v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 2, 2, 1)
)
tmnxSASPortV1v0Group.setObjects(
      *(("TIMETRA-SAS-PORT-MIB", "tmnxPortUplinkMode"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortAccessEgressQoSPolicyId"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortNetworkQoSPolicyId"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortShgName"),
        ("TIMETRA-SAS-PORT-MIB", "portShgRowStatus"),
        ("TIMETRA-SAS-PORT-MIB", "portShgInstanceId"),
        ("TIMETRA-SAS-PORT-MIB", "portShgDescription"),
        ("TIMETRA-SAS-PORT-MIB", "portShgLastMgmtChange"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxSASPortNetIngressFwdInProfPkts"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxSASPortNetIngressFwdOutProfPkts"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxSASPortNetIngressFwdInProfOcts"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxSASPortNetIngressFwdOutProfOcts"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortEtherEgressMaxBurst"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortStatsQueue1PktsFwd"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortStatsQueue2PktsFwd"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortStatsQueue3PktsFwd"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortStatsQueue4PktsFwd"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortStatsQueue5PktsFwd"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortStatsQueue6PktsFwd"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortStatsQueue7PktsFwd"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortStatsQueue8PktsFwd"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortEtherLoopback"))
)
if mibBuilder.loadTexts:
    tmnxSASPortV1v0Group.setStatus("current")

tmnxSASPortV1v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 2, 2, 2)
)
tmnxSASPortV1v1Group.setObjects(
      *(("TIMETRA-SAS-PORT-MIB", "tmnxPortAccessEgressQueueStatsFwdPkts"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortAccessEgressQueueStatsFwdOcts"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortAccessEgressQueueStatsDroPkts"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortAccessEgressQueueStatsDroOcts"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortNetEgressQueueStatsFwdPkts"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortNetEgressQueueStatsFwdOcts"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortNetEgressQueueStatsDroPkts"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortNetEgressQueueStatsDroOcts"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortNetEgressQueueStatsInProfDroPkts"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortNetEgressQueueStatsInProfDroOcts"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortNetEgressQueueStatsOutProfDroPkts"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortNetEgressQueueStatsOutProfDroOcts"))
)
if mibBuilder.loadTexts:
    tmnxSASPortV1v1Group.setStatus("current")

tmnxSASPortV2v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 2, 2, 3)
)
tmnxSASPortV2v0Group.setObjects(
      *(("TIMETRA-SAS-PORT-MIB", "aluExtDS1PortLineImpedance"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortEtherEgrSchedMode"))
)
if mibBuilder.loadTexts:
    tmnxSASPortV2v0Group.setStatus("current")

aluPortAcrClkStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 2, 2, 4)
)
aluPortAcrClkStatsGroup.setObjects(
      *(("TIMETRA-SAS-PORT-MIB", "aluLastUpdateTime"),
        ("TIMETRA-SAS-PORT-MIB", "aluTotalMinutesIn24Hour"),
        ("TIMETRA-SAS-PORT-MIB", "aluCurrent24HourFreqOffsetMeanPpb"),
        ("TIMETRA-SAS-PORT-MIB", "aluCurrent24HourFreqOffsetStdDevPpb"),
        ("TIMETRA-SAS-PORT-MIB", "aluMaxShortIntervalMinutes"),
        ("TIMETRA-SAS-PORT-MIB", "aluTotalShortIntervalMinutes"),
        ("TIMETRA-SAS-PORT-MIB", "aluCurrent1MinValidData"),
        ("TIMETRA-SAS-PORT-MIB", "aluCurrent1MinPhaseErrorMeanPpb"),
        ("TIMETRA-SAS-PORT-MIB", "aluCurrent1MinPhaseErrorStdDevNs"),
        ("TIMETRA-SAS-PORT-MIB", "aluCurrent1MinPhaseErrorMeanNs"),
        ("TIMETRA-SAS-PORT-MIB", "aluCurrent1MinFreqOffsetMeanPpb"),
        ("TIMETRA-SAS-PORT-MIB", "aluCurrent1MinFreqOffsetStdDevPpb"),
        ("TIMETRA-SAS-PORT-MIB", "aluIntervalNumber"),
        ("TIMETRA-SAS-PORT-MIB", "aluIntervalValidData"),
        ("TIMETRA-SAS-PORT-MIB", "aluIntervalUpdateTime"),
        ("TIMETRA-SAS-PORT-MIB", "aluIntervalPhaseErrorMeanPpb"),
        ("TIMETRA-SAS-PORT-MIB", "aluIntervalPhaseErrorStdDevNs"),
        ("TIMETRA-SAS-PORT-MIB", "aluIntervalPhaseErrorMeanNs"),
        ("TIMETRA-SAS-PORT-MIB", "aluIntervalFreqOffsetMeanPpb"),
        ("TIMETRA-SAS-PORT-MIB", "aluIntervalFreqOffsetStdDevPpb"))
)
if mibBuilder.loadTexts:
    aluPortAcrClkStatsGroup.setStatus("current")

tmnxSASPortV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 2, 2, 5)
)
tmnxSASPortV4v0Group.setObjects(
      *(("TIMETRA-SAS-PORT-MIB", "tmnxPortAccessEgressQueueStatsFwdPkts"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortAccessEgressQueueStatsFwdOcts"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortAccessEgressQueueStatsDroPkts"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortAccessEgressQueueStatsDroOcts"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortNetEgressQueueStatsFwdPkts"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortNetEgressQueueStatsFwdOcts"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortNetEgressQueueStatsDroPkts"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortNetEgressQueueStatsDroOcts"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortNetEgressQueueStatsInProfDroPkts"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortNetEgressQueueStatsInProfDroOcts"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortNetEgressQueueStatsOutProfDroPkts"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortNetEgressQueueStatsOutProfDroOcts"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortEtherIpMTU"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortEtherClockConfig"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortLoopbckServId"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortLoopbckSapPortId"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortLoopbckSapEncapVal"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortLoopbckSrcMacAddr"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortLoopbckDstMacAddr"),
        ("TIMETRA-SAS-PORT-MIB", "tmnxPortAccEgrSapQosMarking"))
)
if mibBuilder.loadTexts:
    tmnxSASPortV4v0Group.setStatus("current")

tmnxSASPortV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 2, 2, 6)
)
tmnxSASPortV3v0Group.setObjects(
    ("TIMETRA-SAS-PORT-MIB", "tmnxPortEtherClockConfig")
)
if mibBuilder.loadTexts:
    tmnxSASPortV3v0Group.setStatus("current")

tmnxSASPortV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 2, 2, 7)
)
tmnxSASPortV5v0Group.setObjects(
    ("TIMETRA-SAS-PORT-MIB", "tmnxPortLldpTnlNrstBrdgeDstMac")
)
if mibBuilder.loadTexts:
    tmnxSASPortV5v0Group.setStatus("current")

tmnxSASPortV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 2, 2, 8)
)
tmnxSASPortV6v0Group.setObjects(
    ("TIMETRA-SAS-PORT-MIB", "tmnxPortEtherNwAggRateLimit")
)
if mibBuilder.loadTexts:
    tmnxSASPortV6v0Group.setStatus("current")


# Notification objects

aluExtPethPsePortStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 3, 1)
)
aluExtPethPsePortStatusChange.setObjects(
      *(("POWER-ETHERNET-MIB", "pethPsePortDetectionStatus"),
        ("POWER-ETHERNET-MIB", "pethPsePortPowerClassifications"),
        ("TIMETRA-SAS-PORT-MIB", "aluExtPethPsePortFaultReason"),
        ("TIMETRA-SAS-PORT-MIB", "aluExtPethPsePortOperStatus"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"))
)
if mibBuilder.loadTexts:
    aluExtPethPsePortStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-SAS-PORT-MIB",
    **{"tmnxSASPortMIBModule": tmnxSASPortMIBModule,
       "tmnxSASPortConformance": tmnxSASPortConformance,
       "tmnxSASPortCompliances": tmnxSASPortCompliances,
       "tmnxSASPortGroups": tmnxSASPortGroups,
       "tmnxSASPortV1v0Group": tmnxSASPortV1v0Group,
       "tmnxSASPortV1v1Group": tmnxSASPortV1v1Group,
       "tmnxSASPortV2v0Group": tmnxSASPortV2v0Group,
       "aluPortAcrClkStatsGroup": aluPortAcrClkStatsGroup,
       "tmnxSASPortV4v0Group": tmnxSASPortV4v0Group,
       "tmnxSASPortV3v0Group": tmnxSASPortV3v0Group,
       "tmnxSASPortV5v0Group": tmnxSASPortV5v0Group,
       "tmnxSASPortV6v0Group": tmnxSASPortV6v0Group,
       "tmnxSASPortObjs": tmnxSASPortObjs,
       "sasTmnxPortExtnTable": sasTmnxPortExtnTable,
       "sasTmnxPortExtnEntry": sasTmnxPortExtnEntry,
       "tmnxPortUplinkMode": tmnxPortUplinkMode,
       "tmnxPortAccessEgressQoSPolicyId": tmnxPortAccessEgressQoSPolicyId,
       "tmnxPortNetworkQoSPolicyId": tmnxPortNetworkQoSPolicyId,
       "tmnxPortShgName": tmnxPortShgName,
       "tmnxPortUseDei": tmnxPortUseDei,
       "tmnxPortOperGrpName": tmnxPortOperGrpName,
       "tmnxPortMonitorOperGrpName": tmnxPortMonitorOperGrpName,
       "tmnxSASPortNetIngressStatsTable": tmnxSASPortNetIngressStatsTable,
       "tmnxSASPortNetIngressStatsEntry": tmnxSASPortNetIngressStatsEntry,
       "tmnxSASPortNetIngressMeterIndex": tmnxSASPortNetIngressMeterIndex,
       "tmnxSASPortNetIngressFwdInProfPkts": tmnxSASPortNetIngressFwdInProfPkts,
       "tmnxSASPortNetIngressFwdOutProfPkts": tmnxSASPortNetIngressFwdOutProfPkts,
       "tmnxSASPortNetIngressFwdInProfOcts": tmnxSASPortNetIngressFwdInProfOcts,
       "tmnxSASPortNetIngressFwdOutProfOcts": tmnxSASPortNetIngressFwdOutProfOcts,
       "sasTmnxPortEtherExtnTable": sasTmnxPortEtherExtnTable,
       "sasTmnxPortEtherExtnEntry": sasTmnxPortEtherExtnEntry,
       "tmnxPortEtherEgressMaxBurst": tmnxPortEtherEgressMaxBurst,
       "tmnxPortStatsQueue1PktsFwd": tmnxPortStatsQueue1PktsFwd,
       "tmnxPortStatsQueue2PktsFwd": tmnxPortStatsQueue2PktsFwd,
       "tmnxPortStatsQueue3PktsFwd": tmnxPortStatsQueue3PktsFwd,
       "tmnxPortStatsQueue4PktsFwd": tmnxPortStatsQueue4PktsFwd,
       "tmnxPortStatsQueue5PktsFwd": tmnxPortStatsQueue5PktsFwd,
       "tmnxPortStatsQueue6PktsFwd": tmnxPortStatsQueue6PktsFwd,
       "tmnxPortStatsQueue7PktsFwd": tmnxPortStatsQueue7PktsFwd,
       "tmnxPortStatsQueue8PktsFwd": tmnxPortStatsQueue8PktsFwd,
       "tmnxPortEtherEgrSchedMode": tmnxPortEtherEgrSchedMode,
       "tmnxPortEtherLoopback": tmnxPortEtherLoopback,
       "tmnxPortEtherIpMTU": tmnxPortEtherIpMTU,
       "tmnxPortEtherClockConfig": tmnxPortEtherClockConfig,
       "tmnxPortLoopbckServId": tmnxPortLoopbckServId,
       "tmnxPortLoopbckSapPortId": tmnxPortLoopbckSapPortId,
       "tmnxPortLoopbckSapEncapVal": tmnxPortLoopbckSapEncapVal,
       "tmnxPortLoopbckSrcMacAddr": tmnxPortLoopbckSrcMacAddr,
       "tmnxPortLoopbckDstMacAddr": tmnxPortLoopbckDstMacAddr,
       "tmnxPortAccEgrSapQosMarking": tmnxPortAccEgrSapQosMarking,
       "tmnxPortLldpTnlNrstBrdgeDstMac": tmnxPortLldpTnlNrstBrdgeDstMac,
       "tmnxPortEtherDe1OutProfile": tmnxPortEtherDe1OutProfile,
       "tmnxPortEtherNwAggRateLimit": tmnxPortEtherNwAggRateLimit,
       "tmnxPortEtherNwAggRateLimitCir": tmnxPortEtherNwAggRateLimitCir,
       "tmnxPortEtherNwAggRateLimitPir": tmnxPortEtherNwAggRateLimitPir,
       "tmnxPortEtherDcommStatus": tmnxPortEtherDcommStatus,
       "tmnxPortEtherMulticastIngress": tmnxPortEtherMulticastIngress,
       "portShgInfoTable": portShgInfoTable,
       "portShgInfoEntry": portShgInfoEntry,
       "portShgName": portShgName,
       "portShgRowStatus": portShgRowStatus,
       "portShgInstanceId": portShgInstanceId,
       "portShgDescription": portShgDescription,
       "portShgLastMgmtChange": portShgLastMgmtChange,
       "tmnxPortAccessEgressQueueStatsTable": tmnxPortAccessEgressQueueStatsTable,
       "tmnxPortAccessEgressQueueStatsEntry": tmnxPortAccessEgressQueueStatsEntry,
       "tmnxPortAccessEgressQueueStatsIndex": tmnxPortAccessEgressQueueStatsIndex,
       "tmnxPortAccessEgressQueueStatsFwdPkts": tmnxPortAccessEgressQueueStatsFwdPkts,
       "tmnxPortAccessEgressQueueStatsFwdOcts": tmnxPortAccessEgressQueueStatsFwdOcts,
       "tmnxPortAccessEgressQueueStatsDroPkts": tmnxPortAccessEgressQueueStatsDroPkts,
       "tmnxPortAccessEgressQueueStatsDroOcts": tmnxPortAccessEgressQueueStatsDroOcts,
       "tmnxPortNetEgressQueueStatsTable": tmnxPortNetEgressQueueStatsTable,
       "tmnxPortNetEgressQueueStatsEntry": tmnxPortNetEgressQueueStatsEntry,
       "tmnxPortNetEgressQueueStatsIndex": tmnxPortNetEgressQueueStatsIndex,
       "tmnxPortNetEgressQueueStatsFwdPkts": tmnxPortNetEgressQueueStatsFwdPkts,
       "tmnxPortNetEgressQueueStatsFwdOcts": tmnxPortNetEgressQueueStatsFwdOcts,
       "tmnxPortNetEgressQueueStatsDroPkts": tmnxPortNetEgressQueueStatsDroPkts,
       "tmnxPortNetEgressQueueStatsDroOcts": tmnxPortNetEgressQueueStatsDroOcts,
       "tmnxPortNetEgressQueueStatsInProfDroPkts": tmnxPortNetEgressQueueStatsInProfDroPkts,
       "tmnxPortNetEgressQueueStatsInProfDroOcts": tmnxPortNetEgressQueueStatsInProfDroOcts,
       "tmnxPortNetEgressQueueStatsOutProfDroPkts": tmnxPortNetEgressQueueStatsOutProfDroPkts,
       "tmnxPortNetEgressQueueStatsOutProfDroOcts": tmnxPortNetEgressQueueStatsOutProfDroOcts,
       "aluExtTmnxDS1PortTable": aluExtTmnxDS1PortTable,
       "aluExtTmnxDS1PortEntry": aluExtTmnxDS1PortEntry,
       "aluExtDS1PortLineImpedance": aluExtDS1PortLineImpedance,
       "aluPortAcrClkStatsTable": aluPortAcrClkStatsTable,
       "aluPortAcrClkStatsEntry": aluPortAcrClkStatsEntry,
       "aluLastUpdateTime": aluLastUpdateTime,
       "aluTotalMinutesIn24Hour": aluTotalMinutesIn24Hour,
       "aluCurrent24HourFreqOffsetMeanPpb": aluCurrent24HourFreqOffsetMeanPpb,
       "aluCurrent24HourFreqOffsetStdDevPpb": aluCurrent24HourFreqOffsetStdDevPpb,
       "aluMaxShortIntervalMinutes": aluMaxShortIntervalMinutes,
       "aluTotalShortIntervalMinutes": aluTotalShortIntervalMinutes,
       "aluCurrent1MinValidData": aluCurrent1MinValidData,
       "aluCurrent1MinPhaseErrorMeanPpb": aluCurrent1MinPhaseErrorMeanPpb,
       "aluCurrent1MinPhaseErrorStdDevNs": aluCurrent1MinPhaseErrorStdDevNs,
       "aluCurrent1MinPhaseErrorMeanNs": aluCurrent1MinPhaseErrorMeanNs,
       "aluCurrent1MinFreqOffsetMeanPpb": aluCurrent1MinFreqOffsetMeanPpb,
       "aluCurrent1MinFreqOffsetStdDevPpb": aluCurrent1MinFreqOffsetStdDevPpb,
       "aluPortAcrClkStatsShortIntervalTable": aluPortAcrClkStatsShortIntervalTable,
       "aluPortAcrClkStatsShortIntervalEntry": aluPortAcrClkStatsShortIntervalEntry,
       "aluIntervalNumber": aluIntervalNumber,
       "aluIntervalValidData": aluIntervalValidData,
       "aluIntervalUpdateTime": aluIntervalUpdateTime,
       "aluIntervalPhaseErrorMeanPpb": aluIntervalPhaseErrorMeanPpb,
       "aluIntervalPhaseErrorStdDevNs": aluIntervalPhaseErrorStdDevNs,
       "aluIntervalPhaseErrorMeanNs": aluIntervalPhaseErrorMeanNs,
       "aluIntervalFreqOffsetMeanPpb": aluIntervalFreqOffsetMeanPpb,
       "aluIntervalFreqOffsetStdDevPpb": aluIntervalFreqOffsetStdDevPpb,
       "aluExtTmnxDS1Table": aluExtTmnxDS1Table,
       "aluExtTmnxDS1Entry": aluExtTmnxDS1Entry,
       "aluExtDS1SignalBitsState": aluExtDS1SignalBitsState,
       "aluExtPethPsePortTable": aluExtPethPsePortTable,
       "aluExtPethPsePortEntry": aluExtPethPsePortEntry,
       "aluExtPethPsePortFaultReason": aluExtPethPsePortFaultReason,
       "aluExtPethPsePortPowerLevel": aluExtPethPsePortPowerLevel,
       "aluExtPethPsePortOperStatus": aluExtPethPsePortOperStatus,
       "pethPsePortEventInfo": pethPsePortEventInfo,
       "tmnxVirtualPortTable": tmnxVirtualPortTable,
       "tmnxVirtualPortEntry": tmnxVirtualPortEntry,
       "tmnxVirtualPortPortID": tmnxVirtualPortPortID,
       "tmnxVirtualPortInUse": tmnxVirtualPortInUse,
       "tmnxVirtualPortSpeed": tmnxVirtualPortSpeed,
       "tmnxSASPortNotificationObjects": tmnxSASPortNotificationObjects,
       "aluExtPethPsePortStatusChange": aluExtPethPsePortStatusChange,
       "tmnxSASPortStatsObjs": tmnxSASPortStatsObjs}
)
