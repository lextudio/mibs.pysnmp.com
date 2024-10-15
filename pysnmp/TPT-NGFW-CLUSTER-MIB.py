# SNMP MIB module (TPT-NGFW-CLUSTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPT-NGFW-CLUSTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:00 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")

(Severity,
 tpt_ngfw_compls,
 tpt_ngfw_eventsV2,
 tpt_ngfw_groups,
 tpt_ngfw_objs,
 tpt_ngfw_params,
 tptNgfwNotifySeverity) = mibBuilder.importSymbols(
    "TPT-NGFW-REG-MIB",
    "Severity",
    "tpt-ngfw-compls",
    "tpt-ngfw-eventsV2",
    "tpt-ngfw-groups",
    "tpt-ngfw-objs",
    "tpt-ngfw-params",
    "tptNgfwNotifySeverity")

(tptNgfwSystemSerial,) = mibBuilder.importSymbols(
    "TPT-NGFW-SYSTEM-INFO-MIB",
    "tptNgfwSystemSerial")

(AutoNegotiation,
 DuplexSetting,
 LineSpeed) = mibBuilder.importSymbols(
    "TPT-PORT-CONFIG-MIB",
    "AutoNegotiation",
    "DuplexSetting",
    "LineSpeed")


# MODULE-IDENTITY

tptNgfwCluster = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2)
)
tptNgfwCluster.setRevisions(
        ("2016-05-25 18:54",
         "2015-03-19 09:30",
         "2013-01-17 10:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FailoverGrpMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activeActive", 2),
          ("activePassive", 1))
    )



class LinkState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )



class CfgControl(Integer32, TextualConvention):
    status = "current"
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
        *(("disabled", 1),
          ("local", 3),
          ("none", 2),
          ("remote", 4))
    )



class SyncState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("error", 4),
          ("inSync", 1),
          ("notInit", 3),
          ("outOfSync", 2),
          ("pending", 5))
    )



class HaState(Integer32, TextualConvention):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("activeNoPartner", 7),
          ("disabled", 5),
          ("failed", 3),
          ("passive", 2),
          ("standby", 4),
          ("starting", 8),
          ("stopping", 9),
          ("unknown", 6))
    )



class HealthState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("normal", 1),
          ("warning", 2))
    )



class ClusterMemberRejectReason(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("duplicateNodeId", 1)
    )



class FailoverGroupState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 2),
          ("running", 1),
          ("stopped", 3))
    )



class ComponentType(Integer32, TextualConvention):
    status = "current"
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("cpu", 2),
          ("hwAny", 10),
          ("hwFan", 6),
          ("hwPsu", 11),
          ("hwTmp", 7),
          ("hwVid", 9),
          ("hwVol", 8),
          ("memory", 3),
          ("swDisk", 4),
          ("swLink", 5),
          ("swSal", 1),
          ("unknown", 12))
    )



class ThresholdLimitType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lower", 2),
          ("upper", 1))
    )



class ThresholdRelation(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("above", 1),
          ("below", 2))
    )



class ConsistencyCheckType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("configuration", 1),
          ("hardware", 3),
          ("software", 2))
    )



class MasterLocation(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )



# MIB Managed Objects in the order of their OIDs



class _TptNgfwClusterName_Type(SnmpAdminString):
    """Custom type tptNgfwClusterName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_TptNgfwClusterName_Type.__name__ = "SnmpAdminString"
_TptNgfwClusterName_Object = MibScalar
tptNgfwClusterName = _TptNgfwClusterName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 1),
    _TptNgfwClusterName_Type()
)
tptNgfwClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterName.setStatus("current")
_TptNgfwClusterEnabled_Type = TruthValue
_TptNgfwClusterEnabled_Object = MibScalar
tptNgfwClusterEnabled = _TptNgfwClusterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 2),
    _TptNgfwClusterEnabled_Type()
)
tptNgfwClusterEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterEnabled.setStatus("current")


class _TptNgfwClusterMemberId_Type(Unsigned32):
    """Custom type tptNgfwClusterMemberId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_TptNgfwClusterMemberId_Type.__name__ = "Unsigned32"
_TptNgfwClusterMemberId_Object = MibScalar
tptNgfwClusterMemberId = _TptNgfwClusterMemberId_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 3),
    _TptNgfwClusterMemberId_Type()
)
tptNgfwClusterMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterMemberId.setStatus("current")


class _TptNgfwClusterMemberName_Type(SnmpAdminString):
    """Custom type tptNgfwClusterMemberName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_TptNgfwClusterMemberName_Type.__name__ = "SnmpAdminString"
_TptNgfwClusterMemberName_Object = MibScalar
tptNgfwClusterMemberName = _TptNgfwClusterMemberName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 4),
    _TptNgfwClusterMemberName_Type()
)
tptNgfwClusterMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterMemberName.setStatus("current")
_TptNgfwClusterStandby_Type = TruthValue
_TptNgfwClusterStandby_Object = MibScalar
tptNgfwClusterStandby = _TptNgfwClusterStandby_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 5),
    _TptNgfwClusterStandby_Type()
)
tptNgfwClusterStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterStandby.setStatus("current")
_TptNgfwClusterSwConstChecks_Type = TruthValue
_TptNgfwClusterSwConstChecks_Object = MibScalar
tptNgfwClusterSwConstChecks = _TptNgfwClusterSwConstChecks_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 6),
    _TptNgfwClusterSwConstChecks_Type()
)
tptNgfwClusterSwConstChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterSwConstChecks.setStatus("current")
_TptNgfwClusterHwConstChecks_Type = TruthValue
_TptNgfwClusterHwConstChecks_Object = MibScalar
tptNgfwClusterHwConstChecks = _TptNgfwClusterHwConstChecks_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 7),
    _TptNgfwClusterHwConstChecks_Type()
)
tptNgfwClusterHwConstChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterHwConstChecks.setStatus("current")
_TptNgfwClusterCfgConstChecks_Type = TruthValue
_TptNgfwClusterCfgConstChecks_Object = MibScalar
tptNgfwClusterCfgConstChecks = _TptNgfwClusterCfgConstChecks_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 8),
    _TptNgfwClusterCfgConstChecks_Type()
)
tptNgfwClusterCfgConstChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterCfgConstChecks.setStatus("current")
_TptNgfwClusterMemberStatusTable_Object = MibTable
tptNgfwClusterMemberStatusTable = _TptNgfwClusterMemberStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 9)
)
if mibBuilder.loadTexts:
    tptNgfwClusterMemberStatusTable.setStatus("current")
_TptNgfwClusterMemberStatusTableEntry_Object = MibTableRow
tptNgfwClusterMemberStatusTableEntry = _TptNgfwClusterMemberStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 9, 1)
)
tptNgfwClusterMemberStatusTableEntry.setIndexNames(
    (0, "TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterMemberStatusId"),
)
if mibBuilder.loadTexts:
    tptNgfwClusterMemberStatusTableEntry.setStatus("current")


class _TptNgfwClusterMemberStatusId_Type(Unsigned32):
    """Custom type tptNgfwClusterMemberStatusId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_TptNgfwClusterMemberStatusId_Type.__name__ = "Unsigned32"
_TptNgfwClusterMemberStatusId_Object = MibTableColumn
tptNgfwClusterMemberStatusId = _TptNgfwClusterMemberStatusId_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 9, 1, 1),
    _TptNgfwClusterMemberStatusId_Type()
)
tptNgfwClusterMemberStatusId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tptNgfwClusterMemberStatusId.setStatus("current")


class _TptNgfwClusterMemberStatusName_Type(SnmpAdminString):
    """Custom type tptNgfwClusterMemberStatusName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_TptNgfwClusterMemberStatusName_Type.__name__ = "SnmpAdminString"
_TptNgfwClusterMemberStatusName_Object = MibTableColumn
tptNgfwClusterMemberStatusName = _TptNgfwClusterMemberStatusName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 9, 1, 2),
    _TptNgfwClusterMemberStatusName_Type()
)
tptNgfwClusterMemberStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterMemberStatusName.setStatus("current")


class _TptNgfwClusterMemberStatusSerialNo_Type(SnmpAdminString):
    """Custom type tptNgfwClusterMemberStatusSerialNo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TptNgfwClusterMemberStatusSerialNo_Type.__name__ = "SnmpAdminString"
_TptNgfwClusterMemberStatusSerialNo_Object = MibTableColumn
tptNgfwClusterMemberStatusSerialNo = _TptNgfwClusterMemberStatusSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 9, 1, 3),
    _TptNgfwClusterMemberStatusSerialNo_Type()
)
tptNgfwClusterMemberStatusSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterMemberStatusSerialNo.setStatus("current")


class _TptNgfwClusterMemberStatusHwModel_Type(SnmpAdminString):
    """Custom type tptNgfwClusterMemberStatusHwModel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TptNgfwClusterMemberStatusHwModel_Type.__name__ = "SnmpAdminString"
_TptNgfwClusterMemberStatusHwModel_Object = MibTableColumn
tptNgfwClusterMemberStatusHwModel = _TptNgfwClusterMemberStatusHwModel_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 9, 1, 4),
    _TptNgfwClusterMemberStatusHwModel_Type()
)
tptNgfwClusterMemberStatusHwModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterMemberStatusHwModel.setStatus("current")


class _TptNgfwClusterMemberStatusSwVersion_Type(SnmpAdminString):
    """Custom type tptNgfwClusterMemberStatusSwVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TptNgfwClusterMemberStatusSwVersion_Type.__name__ = "SnmpAdminString"
_TptNgfwClusterMemberStatusSwVersion_Object = MibTableColumn
tptNgfwClusterMemberStatusSwVersion = _TptNgfwClusterMemberStatusSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 9, 1, 5),
    _TptNgfwClusterMemberStatusSwVersion_Type()
)
tptNgfwClusterMemberStatusSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterMemberStatusSwVersion.setStatus("current")
_TptNgfwClusterMemberStatusUptime_Type = TimeTicks
_TptNgfwClusterMemberStatusUptime_Object = MibTableColumn
tptNgfwClusterMemberStatusUptime = _TptNgfwClusterMemberStatusUptime_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 9, 1, 6),
    _TptNgfwClusterMemberStatusUptime_Type()
)
tptNgfwClusterMemberStatusUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterMemberStatusUptime.setStatus("current")
_TptNgfwClusterMemberStatusJoinTime_Type = DateAndTime
_TptNgfwClusterMemberStatusJoinTime_Object = MibTableColumn
tptNgfwClusterMemberStatusJoinTime = _TptNgfwClusterMemberStatusJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 9, 1, 7),
    _TptNgfwClusterMemberStatusJoinTime_Type()
)
tptNgfwClusterMemberStatusJoinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterMemberStatusJoinTime.setStatus("current")
_TptNgfwClusterMemberStatusSmsManaged_Type = TruthValue
_TptNgfwClusterMemberStatusSmsManaged_Object = MibTableColumn
tptNgfwClusterMemberStatusSmsManaged = _TptNgfwClusterMemberStatusSmsManaged_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 9, 1, 8),
    _TptNgfwClusterMemberStatusSmsManaged_Type()
)
tptNgfwClusterMemberStatusSmsManaged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterMemberStatusSmsManaged.setStatus("current")
_TptNgfwClusterMemberStatusCfgControl_Type = CfgControl
_TptNgfwClusterMemberStatusCfgControl_Object = MibTableColumn
tptNgfwClusterMemberStatusCfgControl = _TptNgfwClusterMemberStatusCfgControl_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 9, 1, 9),
    _TptNgfwClusterMemberStatusCfgControl_Type()
)
tptNgfwClusterMemberStatusCfgControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterMemberStatusCfgControl.setStatus("current")
_TptNgfwClusterMemberStatusCfgStateSync_Type = SyncState
_TptNgfwClusterMemberStatusCfgStateSync_Object = MibTableColumn
tptNgfwClusterMemberStatusCfgStateSync = _TptNgfwClusterMemberStatusCfgStateSync_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 9, 1, 10),
    _TptNgfwClusterMemberStatusCfgStateSync_Type()
)
tptNgfwClusterMemberStatusCfgStateSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterMemberStatusCfgStateSync.setStatus("current")
_TptNgfwClusterMemberStatusEnabled_Type = TruthValue
_TptNgfwClusterMemberStatusEnabled_Object = MibTableColumn
tptNgfwClusterMemberStatusEnabled = _TptNgfwClusterMemberStatusEnabled_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 9, 1, 11),
    _TptNgfwClusterMemberStatusEnabled_Type()
)
tptNgfwClusterMemberStatusEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterMemberStatusEnabled.setStatus("current")
_TptNgfwClusterMemberStatusHaState_Type = HaState
_TptNgfwClusterMemberStatusHaState_Object = MibTableColumn
tptNgfwClusterMemberStatusHaState = _TptNgfwClusterMemberStatusHaState_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 9, 1, 12),
    _TptNgfwClusterMemberStatusHaState_Type()
)
tptNgfwClusterMemberStatusHaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterMemberStatusHaState.setStatus("current")
_TptNgfwClusterMemberStatusHealthState_Type = HealthState
_TptNgfwClusterMemberStatusHealthState_Object = MibTableColumn
tptNgfwClusterMemberStatusHealthState = _TptNgfwClusterMemberStatusHealthState_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 9, 1, 13),
    _TptNgfwClusterMemberStatusHealthState_Type()
)
tptNgfwClusterMemberStatusHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterMemberStatusHealthState.setStatus("current")


class _TptNgfwClusterMemberStatusHealthScore_Type(Unsigned32):
    """Custom type tptNgfwClusterMemberStatusHealthScore based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TptNgfwClusterMemberStatusHealthScore_Type.__name__ = "Unsigned32"
_TptNgfwClusterMemberStatusHealthScore_Object = MibTableColumn
tptNgfwClusterMemberStatusHealthScore = _TptNgfwClusterMemberStatusHealthScore_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 9, 1, 14),
    _TptNgfwClusterMemberStatusHealthScore_Type()
)
tptNgfwClusterMemberStatusHealthScore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterMemberStatusHealthScore.setStatus("current")
_TptNgfwClusterMemberStatusMaster_Type = TruthValue
_TptNgfwClusterMemberStatusMaster_Object = MibTableColumn
tptNgfwClusterMemberStatusMaster = _TptNgfwClusterMemberStatusMaster_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 9, 1, 15),
    _TptNgfwClusterMemberStatusMaster_Type()
)
tptNgfwClusterMemberStatusMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterMemberStatusMaster.setStatus("current")
_TptNgfwClusterTraffic_ObjectIdentity = ObjectIdentity
tptNgfwClusterTraffic = _TptNgfwClusterTraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 10)
)
_TptNgfwClusterTctIpAddrType_Type = InetAddressType
_TptNgfwClusterTctIpAddrType_Object = MibScalar
tptNgfwClusterTctIpAddrType = _TptNgfwClusterTctIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 10, 1),
    _TptNgfwClusterTctIpAddrType_Type()
)
tptNgfwClusterTctIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterTctIpAddrType.setStatus("current")
_TptNgfwClusterTctIpAddr_Type = InetAddress
_TptNgfwClusterTctIpAddr_Object = MibScalar
tptNgfwClusterTctIpAddr = _TptNgfwClusterTctIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 10, 2),
    _TptNgfwClusterTctIpAddr_Type()
)
tptNgfwClusterTctIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterTctIpAddr.setStatus("current")
_TptNgfwClusterTctMulticastAddrType_Type = InetAddressType
_TptNgfwClusterTctMulticastAddrType_Object = MibScalar
tptNgfwClusterTctMulticastAddrType = _TptNgfwClusterTctMulticastAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 10, 3),
    _TptNgfwClusterTctMulticastAddrType_Type()
)
tptNgfwClusterTctMulticastAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterTctMulticastAddrType.setStatus("current")
_TptNgfwClusterTctMulticastAddr_Type = InetAddress
_TptNgfwClusterTctMulticastAddr_Object = MibScalar
tptNgfwClusterTctMulticastAddr = _TptNgfwClusterTctMulticastAddr_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 10, 4),
    _TptNgfwClusterTctMulticastAddr_Type()
)
tptNgfwClusterTctMulticastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterTctMulticastAddr.setStatus("current")


class _TptNgfwClusterTctPort_Type(Unsigned32):
    """Custom type tptNgfwClusterTctPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_TptNgfwClusterTctPort_Type.__name__ = "Unsigned32"
_TptNgfwClusterTctPort_Object = MibScalar
tptNgfwClusterTctPort = _TptNgfwClusterTctPort_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 10, 5),
    _TptNgfwClusterTctPort_Type()
)
tptNgfwClusterTctPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterTctPort.setStatus("current")


class _TptNgfwClusterTctTtl_Type(Unsigned32):
    """Custom type tptNgfwClusterTctTtl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TptNgfwClusterTctTtl_Type.__name__ = "Unsigned32"
_TptNgfwClusterTctTtl_Object = MibScalar
tptNgfwClusterTctTtl = _TptNgfwClusterTctTtl_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 10, 6),
    _TptNgfwClusterTctTtl_Type()
)
tptNgfwClusterTctTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterTctTtl.setStatus("current")


class _TptNgfwClusterTctMtu_Type(Unsigned32):
    """Custom type tptNgfwClusterTctMtu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(576, 9216),
    )


_TptNgfwClusterTctMtu_Type.__name__ = "Unsigned32"
_TptNgfwClusterTctMtu_Object = MibScalar
tptNgfwClusterTctMtu = _TptNgfwClusterTctMtu_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 10, 7),
    _TptNgfwClusterTctMtu_Type()
)
tptNgfwClusterTctMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterTctMtu.setStatus("current")


class _TptNgfwClusterTctTimeout_Type(Unsigned32):
    """Custom type tptNgfwClusterTctTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_TptNgfwClusterTctTimeout_Type.__name__ = "Unsigned32"
_TptNgfwClusterTctTimeout_Object = MibScalar
tptNgfwClusterTctTimeout = _TptNgfwClusterTctTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 10, 8),
    _TptNgfwClusterTctTimeout_Type()
)
tptNgfwClusterTctTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterTctTimeout.setStatus("current")


class _TptNgfwClusterTctRetries_Type(Unsigned32):
    """Custom type tptNgfwClusterTctRetries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TptNgfwClusterTctRetries_Type.__name__ = "Unsigned32"
_TptNgfwClusterTctRetries_Object = MibScalar
tptNgfwClusterTctRetries = _TptNgfwClusterTctRetries_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 10, 9),
    _TptNgfwClusterTctRetries_Type()
)
tptNgfwClusterTctRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterTctRetries.setStatus("current")
_TptNgfwClusterTctPortSpeed_Type = LineSpeed
_TptNgfwClusterTctPortSpeed_Object = MibScalar
tptNgfwClusterTctPortSpeed = _TptNgfwClusterTctPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 10, 10),
    _TptNgfwClusterTctPortSpeed_Type()
)
tptNgfwClusterTctPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterTctPortSpeed.setStatus("current")
_TptNgfwClusterTctPortDuplex_Type = DuplexSetting
_TptNgfwClusterTctPortDuplex_Object = MibScalar
tptNgfwClusterTctPortDuplex = _TptNgfwClusterTctPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 10, 11),
    _TptNgfwClusterTctPortDuplex_Type()
)
tptNgfwClusterTctPortDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterTctPortDuplex.setStatus("current")
_TptNgfwClusterTctPortAutoNeg_Type = AutoNegotiation
_TptNgfwClusterTctPortAutoNeg_Object = MibScalar
tptNgfwClusterTctPortAutoNeg = _TptNgfwClusterTctPortAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 10, 12),
    _TptNgfwClusterTctPortAutoNeg_Type()
)
tptNgfwClusterTctPortAutoNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterTctPortAutoNeg.setStatus("current")
_TptNgfwClusterTctLinkState_Type = LinkState
_TptNgfwClusterTctLinkState_Object = MibScalar
tptNgfwClusterTctLinkState = _TptNgfwClusterTctLinkState_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 10, 13),
    _TptNgfwClusterTctLinkState_Type()
)
tptNgfwClusterTctLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterTctLinkState.setStatus("current")
_TptNgfwClusterTctEncryptionEnabled_Type = TruthValue
_TptNgfwClusterTctEncryptionEnabled_Object = MibScalar
tptNgfwClusterTctEncryptionEnabled = _TptNgfwClusterTctEncryptionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 10, 14),
    _TptNgfwClusterTctEncryptionEnabled_Type()
)
tptNgfwClusterTctEncryptionEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterTctEncryptionEnabled.setStatus("current")
_TptNgfwClusterHa_ObjectIdentity = ObjectIdentity
tptNgfwClusterHa = _TptNgfwClusterHa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 11)
)
_TptNgfwClusterHaEnabled_Type = TruthValue
_TptNgfwClusterHaEnabled_Object = MibScalar
tptNgfwClusterHaEnabled = _TptNgfwClusterHaEnabled_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 11, 1),
    _TptNgfwClusterHaEnabled_Type()
)
tptNgfwClusterHaEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterHaEnabled.setStatus("current")
_TptNgfwClusterHaGlobalStateSyncEnabled_Type = TruthValue
_TptNgfwClusterHaGlobalStateSyncEnabled_Object = MibScalar
tptNgfwClusterHaGlobalStateSyncEnabled = _TptNgfwClusterHaGlobalStateSyncEnabled_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 11, 2),
    _TptNgfwClusterHaGlobalStateSyncEnabled_Type()
)
tptNgfwClusterHaGlobalStateSyncEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterHaGlobalStateSyncEnabled.setStatus("current")
_TptNgfwClusterHaMode_Type = HaState
_TptNgfwClusterHaMode_Object = MibScalar
tptNgfwClusterHaMode = _TptNgfwClusterHaMode_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 11, 3),
    _TptNgfwClusterHaMode_Type()
)
tptNgfwClusterHaMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterHaMode.setStatus("current")
_TptNgfwClusterHaFeatSyncTable_Object = MibTable
tptNgfwClusterHaFeatSyncTable = _TptNgfwClusterHaFeatSyncTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 11, 4)
)
if mibBuilder.loadTexts:
    tptNgfwClusterHaFeatSyncTable.setStatus("current")
_TptNgfwClusterHaFeatSyncTableEntry_Object = MibTableRow
tptNgfwClusterHaFeatSyncTableEntry = _TptNgfwClusterHaFeatSyncTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 11, 4, 1)
)
tptNgfwClusterHaFeatSyncTableEntry.setIndexNames(
    (0, "TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaFeatSyncFeature"),
)
if mibBuilder.loadTexts:
    tptNgfwClusterHaFeatSyncTableEntry.setStatus("current")


class _TptNgfwClusterHaFeatSyncFeature_Type(SnmpAdminString):
    """Custom type tptNgfwClusterHaFeatSyncFeature based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TptNgfwClusterHaFeatSyncFeature_Type.__name__ = "SnmpAdminString"
_TptNgfwClusterHaFeatSyncFeature_Object = MibTableColumn
tptNgfwClusterHaFeatSyncFeature = _TptNgfwClusterHaFeatSyncFeature_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 11, 4, 1, 1),
    _TptNgfwClusterHaFeatSyncFeature_Type()
)
tptNgfwClusterHaFeatSyncFeature.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tptNgfwClusterHaFeatSyncFeature.setStatus("current")
_TptNgfwClusterHaFeatSyncEnabled_Type = TruthValue
_TptNgfwClusterHaFeatSyncEnabled_Object = MibTableColumn
tptNgfwClusterHaFeatSyncEnabled = _TptNgfwClusterHaFeatSyncEnabled_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 11, 4, 1, 2),
    _TptNgfwClusterHaFeatSyncEnabled_Type()
)
tptNgfwClusterHaFeatSyncEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterHaFeatSyncEnabled.setStatus("current")
_TptNgfwClusterHaFeatSyncLogSeverity_Type = Severity
_TptNgfwClusterHaFeatSyncLogSeverity_Object = MibTableColumn
tptNgfwClusterHaFeatSyncLogSeverity = _TptNgfwClusterHaFeatSyncLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 11, 4, 1, 3),
    _TptNgfwClusterHaFeatSyncLogSeverity_Type()
)
tptNgfwClusterHaFeatSyncLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterHaFeatSyncLogSeverity.setStatus("current")
_TptNgfwClusterHaFgTable_Object = MibTable
tptNgfwClusterHaFgTable = _TptNgfwClusterHaFgTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 11, 5)
)
if mibBuilder.loadTexts:
    tptNgfwClusterHaFgTable.setStatus("current")
_TptNgfwClusterHaFgEntry_Object = MibTableRow
tptNgfwClusterHaFgEntry = _TptNgfwClusterHaFgEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 11, 5, 1)
)
tptNgfwClusterHaFgEntry.setIndexNames(
    (0, "TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaFgIndex"),
)
if mibBuilder.loadTexts:
    tptNgfwClusterHaFgEntry.setStatus("current")
_TptNgfwClusterHaFgIndex_Type = Unsigned32
_TptNgfwClusterHaFgIndex_Object = MibTableColumn
tptNgfwClusterHaFgIndex = _TptNgfwClusterHaFgIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 11, 5, 1, 1),
    _TptNgfwClusterHaFgIndex_Type()
)
tptNgfwClusterHaFgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tptNgfwClusterHaFgIndex.setStatus("current")


class _TptNgfwClusterHaFgId_Type(Unsigned32):
    """Custom type tptNgfwClusterHaFgId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TptNgfwClusterHaFgId_Type.__name__ = "Unsigned32"
_TptNgfwClusterHaFgId_Object = MibTableColumn
tptNgfwClusterHaFgId = _TptNgfwClusterHaFgId_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 11, 5, 1, 2),
    _TptNgfwClusterHaFgId_Type()
)
tptNgfwClusterHaFgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterHaFgId.setStatus("current")


class _TptNgfwClusterHaFgName_Type(SnmpAdminString):
    """Custom type tptNgfwClusterHaFgName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TptNgfwClusterHaFgName_Type.__name__ = "SnmpAdminString"
_TptNgfwClusterHaFgName_Object = MibTableColumn
tptNgfwClusterHaFgName = _TptNgfwClusterHaFgName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 11, 5, 1, 3),
    _TptNgfwClusterHaFgName_Type()
)
tptNgfwClusterHaFgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterHaFgName.setStatus("current")
_TptNgfwClusterHaFgBaseMac_Type = MacAddress
_TptNgfwClusterHaFgBaseMac_Object = MibTableColumn
tptNgfwClusterHaFgBaseMac = _TptNgfwClusterHaFgBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 11, 5, 1, 4),
    _TptNgfwClusterHaFgBaseMac_Type()
)
tptNgfwClusterHaFgBaseMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterHaFgBaseMac.setStatus("current")
_TptNgfwClusterHaFgMode_Type = FailoverGrpMode
_TptNgfwClusterHaFgMode_Object = MibTableColumn
tptNgfwClusterHaFgMode = _TptNgfwClusterHaFgMode_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 11, 5, 1, 5),
    _TptNgfwClusterHaFgMode_Type()
)
tptNgfwClusterHaFgMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterHaFgMode.setStatus("current")
_TptNgfwClusterHaFgMemberTable_Object = MibTable
tptNgfwClusterHaFgMemberTable = _TptNgfwClusterHaFgMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 11, 6)
)
if mibBuilder.loadTexts:
    tptNgfwClusterHaFgMemberTable.setStatus("current")
_TptNgfwClusterHaFgMemberEntry_Object = MibTableRow
tptNgfwClusterHaFgMemberEntry = _TptNgfwClusterHaFgMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 11, 6, 1)
)
tptNgfwClusterHaFgMemberEntry.setIndexNames(
    (0, "TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaFgId"),
)
if mibBuilder.loadTexts:
    tptNgfwClusterHaFgMemberEntry.setStatus("current")


class _TptNgfwClusterHaFgMemberId_Type(Unsigned32):
    """Custom type tptNgfwClusterHaFgMemberId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_TptNgfwClusterHaFgMemberId_Type.__name__ = "Unsigned32"
_TptNgfwClusterHaFgMemberId_Object = MibTableColumn
tptNgfwClusterHaFgMemberId = _TptNgfwClusterHaFgMemberId_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 11, 6, 1, 1),
    _TptNgfwClusterHaFgMemberId_Type()
)
tptNgfwClusterHaFgMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterHaFgMemberId.setStatus("current")


class _TptNgfwClusterHaFgMemberName_Type(SnmpAdminString):
    """Custom type tptNgfwClusterHaFgMemberName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TptNgfwClusterHaFgMemberName_Type.__name__ = "SnmpAdminString"
_TptNgfwClusterHaFgMemberName_Object = MibTableColumn
tptNgfwClusterHaFgMemberName = _TptNgfwClusterHaFgMemberName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 11, 6, 1, 2),
    _TptNgfwClusterHaFgMemberName_Type()
)
tptNgfwClusterHaFgMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterHaFgMemberName.setStatus("current")
_TptNgfwClusterHaFeatSyncStatusTable_Object = MibTable
tptNgfwClusterHaFeatSyncStatusTable = _TptNgfwClusterHaFeatSyncStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 11, 7)
)
if mibBuilder.loadTexts:
    tptNgfwClusterHaFeatSyncStatusTable.setStatus("current")
_TptNgfwClusterHaFeatSyncStatusTableEntry_Object = MibTableRow
tptNgfwClusterHaFeatSyncStatusTableEntry = _TptNgfwClusterHaFeatSyncStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 11, 7, 1)
)
tptNgfwClusterHaFeatSyncStatusTableEntry.setIndexNames(
    (0, "TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaFeatSyncStatusFeature"),
)
if mibBuilder.loadTexts:
    tptNgfwClusterHaFeatSyncStatusTableEntry.setStatus("current")


class _TptNgfwClusterHaFeatSyncStatusFeature_Type(SnmpAdminString):
    """Custom type tptNgfwClusterHaFeatSyncStatusFeature based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TptNgfwClusterHaFeatSyncStatusFeature_Type.__name__ = "SnmpAdminString"
_TptNgfwClusterHaFeatSyncStatusFeature_Object = MibTableColumn
tptNgfwClusterHaFeatSyncStatusFeature = _TptNgfwClusterHaFeatSyncStatusFeature_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 11, 7, 1, 1),
    _TptNgfwClusterHaFeatSyncStatusFeature_Type()
)
tptNgfwClusterHaFeatSyncStatusFeature.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tptNgfwClusterHaFeatSyncStatusFeature.setStatus("current")
_TptNgfwClusterHaFeatSyncStatusEnabled_Type = TruthValue
_TptNgfwClusterHaFeatSyncStatusEnabled_Object = MibTableColumn
tptNgfwClusterHaFeatSyncStatusEnabled = _TptNgfwClusterHaFeatSyncStatusEnabled_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 11, 7, 1, 2),
    _TptNgfwClusterHaFeatSyncStatusEnabled_Type()
)
tptNgfwClusterHaFeatSyncStatusEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterHaFeatSyncStatusEnabled.setStatus("current")
_TptNgfwClusterHaFeatSyncStatusSyncState_Type = SyncState
_TptNgfwClusterHaFeatSyncStatusSyncState_Object = MibTableColumn
tptNgfwClusterHaFeatSyncStatusSyncState = _TptNgfwClusterHaFeatSyncStatusSyncState_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 11, 7, 1, 3),
    _TptNgfwClusterHaFeatSyncStatusSyncState_Type()
)
tptNgfwClusterHaFeatSyncStatusSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterHaFeatSyncStatusSyncState.setStatus("current")


class _TptNgfwClusterHaFeatSyncStatusSyncStateReason_Type(SnmpAdminString):
    """Custom type tptNgfwClusterHaFeatSyncStatusSyncStateReason based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TptNgfwClusterHaFeatSyncStatusSyncStateReason_Type.__name__ = "SnmpAdminString"
_TptNgfwClusterHaFeatSyncStatusSyncStateReason_Object = MibTableColumn
tptNgfwClusterHaFeatSyncStatusSyncStateReason = _TptNgfwClusterHaFeatSyncStatusSyncStateReason_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 11, 7, 1, 4),
    _TptNgfwClusterHaFeatSyncStatusSyncStateReason_Type()
)
tptNgfwClusterHaFeatSyncStatusSyncStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterHaFeatSyncStatusSyncStateReason.setStatus("current")
_TptNgfwClusterHaFeatSyncStatusTotalEntries_Type = Counter64
_TptNgfwClusterHaFeatSyncStatusTotalEntries_Object = MibTableColumn
tptNgfwClusterHaFeatSyncStatusTotalEntries = _TptNgfwClusterHaFeatSyncStatusTotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 11, 7, 1, 5),
    _TptNgfwClusterHaFeatSyncStatusTotalEntries_Type()
)
tptNgfwClusterHaFeatSyncStatusTotalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterHaFeatSyncStatusTotalEntries.setStatus("current")
_TptNgfwClusterHaFeatSyncStatusAddEntries_Type = Counter64
_TptNgfwClusterHaFeatSyncStatusAddEntries_Object = MibTableColumn
tptNgfwClusterHaFeatSyncStatusAddEntries = _TptNgfwClusterHaFeatSyncStatusAddEntries_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 11, 7, 1, 6),
    _TptNgfwClusterHaFeatSyncStatusAddEntries_Type()
)
tptNgfwClusterHaFeatSyncStatusAddEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterHaFeatSyncStatusAddEntries.setStatus("current")
_TptNgfwClusterHaFeatSyncStatusDelEntries_Type = Counter64
_TptNgfwClusterHaFeatSyncStatusDelEntries_Object = MibTableColumn
tptNgfwClusterHaFeatSyncStatusDelEntries = _TptNgfwClusterHaFeatSyncStatusDelEntries_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 2, 11, 7, 1, 7),
    _TptNgfwClusterHaFeatSyncStatusDelEntries_Type()
)
tptNgfwClusterHaFeatSyncStatusDelEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptNgfwClusterHaFeatSyncStatusDelEntries.setStatus("current")
_TptNgfwClusterMemberRejectNotifyReason_Type = ClusterMemberRejectReason
_TptNgfwClusterMemberRejectNotifyReason_Object = MibScalar
tptNgfwClusterMemberRejectNotifyReason = _TptNgfwClusterMemberRejectNotifyReason_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 1),
    _TptNgfwClusterMemberRejectNotifyReason_Type()
)
tptNgfwClusterMemberRejectNotifyReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwClusterMemberRejectNotifyReason.setStatus("current")


class _TptNgfwClusterHaStateSyncNotifyFeature_Type(SnmpAdminString):
    """Custom type tptNgfwClusterHaStateSyncNotifyFeature based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TptNgfwClusterHaStateSyncNotifyFeature_Type.__name__ = "SnmpAdminString"
_TptNgfwClusterHaStateSyncNotifyFeature_Object = MibScalar
tptNgfwClusterHaStateSyncNotifyFeature = _TptNgfwClusterHaStateSyncNotifyFeature_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 2),
    _TptNgfwClusterHaStateSyncNotifyFeature_Type()
)
tptNgfwClusterHaStateSyncNotifyFeature.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwClusterHaStateSyncNotifyFeature.setStatus("current")
_TptNgfwClusterHealthChangeNotifyState_Type = HealthState
_TptNgfwClusterHealthChangeNotifyState_Object = MibScalar
tptNgfwClusterHealthChangeNotifyState = _TptNgfwClusterHealthChangeNotifyState_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 3),
    _TptNgfwClusterHealthChangeNotifyState_Type()
)
tptNgfwClusterHealthChangeNotifyState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwClusterHealthChangeNotifyState.setStatus("current")


class _TptNgfwClusterHealthChangeNotifyScore_Type(Unsigned32):
    """Custom type tptNgfwClusterHealthChangeNotifyScore based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TptNgfwClusterHealthChangeNotifyScore_Type.__name__ = "Unsigned32"
_TptNgfwClusterHealthChangeNotifyScore_Object = MibScalar
tptNgfwClusterHealthChangeNotifyScore = _TptNgfwClusterHealthChangeNotifyScore_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 4),
    _TptNgfwClusterHealthChangeNotifyScore_Type()
)
tptNgfwClusterHealthChangeNotifyScore.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwClusterHealthChangeNotifyScore.setStatus("current")


class _TptNgfwClusterHealthChangeNotifyStateUpperLimit_Type(Unsigned32):
    """Custom type tptNgfwClusterHealthChangeNotifyStateUpperLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TptNgfwClusterHealthChangeNotifyStateUpperLimit_Type.__name__ = "Unsigned32"
_TptNgfwClusterHealthChangeNotifyStateUpperLimit_Object = MibScalar
tptNgfwClusterHealthChangeNotifyStateUpperLimit = _TptNgfwClusterHealthChangeNotifyStateUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 5),
    _TptNgfwClusterHealthChangeNotifyStateUpperLimit_Type()
)
tptNgfwClusterHealthChangeNotifyStateUpperLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwClusterHealthChangeNotifyStateUpperLimit.setStatus("current")


class _TptNgfwClusterHealthChangeNotifyStateLowerLimit_Type(Unsigned32):
    """Custom type tptNgfwClusterHealthChangeNotifyStateLowerLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TptNgfwClusterHealthChangeNotifyStateLowerLimit_Type.__name__ = "Unsigned32"
_TptNgfwClusterHealthChangeNotifyStateLowerLimit_Object = MibScalar
tptNgfwClusterHealthChangeNotifyStateLowerLimit = _TptNgfwClusterHealthChangeNotifyStateLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 6),
    _TptNgfwClusterHealthChangeNotifyStateLowerLimit_Type()
)
tptNgfwClusterHealthChangeNotifyStateLowerLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwClusterHealthChangeNotifyStateLowerLimit.setStatus("current")
_TptNgfwClusterHaFgStateChangeNotifyState_Type = FailoverGroupState
_TptNgfwClusterHaFgStateChangeNotifyState_Object = MibScalar
tptNgfwClusterHaFgStateChangeNotifyState = _TptNgfwClusterHaFgStateChangeNotifyState_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 7),
    _TptNgfwClusterHaFgStateChangeNotifyState_Type()
)
tptNgfwClusterHaFgStateChangeNotifyState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwClusterHaFgStateChangeNotifyState.setStatus("current")


class _TptNgfwClusterHaFgStateChangeNotifyActiveDeviceId_Type(Unsigned32):
    """Custom type tptNgfwClusterHaFgStateChangeNotifyActiveDeviceId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TptNgfwClusterHaFgStateChangeNotifyActiveDeviceId_Type.__name__ = "Unsigned32"
_TptNgfwClusterHaFgStateChangeNotifyActiveDeviceId_Object = MibScalar
tptNgfwClusterHaFgStateChangeNotifyActiveDeviceId = _TptNgfwClusterHaFgStateChangeNotifyActiveDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 8),
    _TptNgfwClusterHaFgStateChangeNotifyActiveDeviceId_Type()
)
tptNgfwClusterHaFgStateChangeNotifyActiveDeviceId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwClusterHaFgStateChangeNotifyActiveDeviceId.setStatus("current")


class _TptNgfwClusterHaFgStateChangeNotifyPassiveDeviceId_Type(Unsigned32):
    """Custom type tptNgfwClusterHaFgStateChangeNotifyPassiveDeviceId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_TptNgfwClusterHaFgStateChangeNotifyPassiveDeviceId_Type.__name__ = "Unsigned32"
_TptNgfwClusterHaFgStateChangeNotifyPassiveDeviceId_Object = MibScalar
tptNgfwClusterHaFgStateChangeNotifyPassiveDeviceId = _TptNgfwClusterHaFgStateChangeNotifyPassiveDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 9),
    _TptNgfwClusterHaFgStateChangeNotifyPassiveDeviceId_Type()
)
tptNgfwClusterHaFgStateChangeNotifyPassiveDeviceId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwClusterHaFgStateChangeNotifyPassiveDeviceId.setStatus("current")
_TptNgfwClusterCmpStateChangeNotifyType_Type = ComponentType
_TptNgfwClusterCmpStateChangeNotifyType_Object = MibScalar
tptNgfwClusterCmpStateChangeNotifyType = _TptNgfwClusterCmpStateChangeNotifyType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 10),
    _TptNgfwClusterCmpStateChangeNotifyType_Type()
)
tptNgfwClusterCmpStateChangeNotifyType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwClusterCmpStateChangeNotifyType.setStatus("current")


class _TptNgfwClusterCmpStateChangeNotifyName_Type(SnmpAdminString):
    """Custom type tptNgfwClusterCmpStateChangeNotifyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TptNgfwClusterCmpStateChangeNotifyName_Type.__name__ = "SnmpAdminString"
_TptNgfwClusterCmpStateChangeNotifyName_Object = MibScalar
tptNgfwClusterCmpStateChangeNotifyName = _TptNgfwClusterCmpStateChangeNotifyName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 11),
    _TptNgfwClusterCmpStateChangeNotifyName_Type()
)
tptNgfwClusterCmpStateChangeNotifyName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwClusterCmpStateChangeNotifyName.setStatus("current")
_TptNgfwClusterCmpStateChangeNotifyState_Type = HealthState
_TptNgfwClusterCmpStateChangeNotifyState_Object = MibScalar
tptNgfwClusterCmpStateChangeNotifyState = _TptNgfwClusterCmpStateChangeNotifyState_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 12),
    _TptNgfwClusterCmpStateChangeNotifyState_Type()
)
tptNgfwClusterCmpStateChangeNotifyState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwClusterCmpStateChangeNotifyState.setStatus("current")


class _TptNgfwClusterCmpStateChangeNotifyValue_Type(SnmpAdminString):
    """Custom type tptNgfwClusterCmpStateChangeNotifyValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TptNgfwClusterCmpStateChangeNotifyValue_Type.__name__ = "SnmpAdminString"
_TptNgfwClusterCmpStateChangeNotifyValue_Object = MibScalar
tptNgfwClusterCmpStateChangeNotifyValue = _TptNgfwClusterCmpStateChangeNotifyValue_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 13),
    _TptNgfwClusterCmpStateChangeNotifyValue_Type()
)
tptNgfwClusterCmpStateChangeNotifyValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwClusterCmpStateChangeNotifyValue.setStatus("current")


class _TptNgfwClusterCmpStateChangeNotifyUnits_Type(SnmpAdminString):
    """Custom type tptNgfwClusterCmpStateChangeNotifyUnits based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_TptNgfwClusterCmpStateChangeNotifyUnits_Type.__name__ = "SnmpAdminString"
_TptNgfwClusterCmpStateChangeNotifyUnits_Object = MibScalar
tptNgfwClusterCmpStateChangeNotifyUnits = _TptNgfwClusterCmpStateChangeNotifyUnits_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 14),
    _TptNgfwClusterCmpStateChangeNotifyUnits_Type()
)
tptNgfwClusterCmpStateChangeNotifyUnits.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwClusterCmpStateChangeNotifyUnits.setStatus("current")


class _TptNgfwClusterCmpStateChangeNotifyThreshold_Type(SnmpAdminString):
    """Custom type tptNgfwClusterCmpStateChangeNotifyThreshold based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TptNgfwClusterCmpStateChangeNotifyThreshold_Type.__name__ = "SnmpAdminString"
_TptNgfwClusterCmpStateChangeNotifyThreshold_Object = MibScalar
tptNgfwClusterCmpStateChangeNotifyThreshold = _TptNgfwClusterCmpStateChangeNotifyThreshold_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 15),
    _TptNgfwClusterCmpStateChangeNotifyThreshold_Type()
)
tptNgfwClusterCmpStateChangeNotifyThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwClusterCmpStateChangeNotifyThreshold.setStatus("current")
_TptNgfwClusterCmpStateChangeNotifyLimitType_Type = ThresholdLimitType
_TptNgfwClusterCmpStateChangeNotifyLimitType_Object = MibScalar
tptNgfwClusterCmpStateChangeNotifyLimitType = _TptNgfwClusterCmpStateChangeNotifyLimitType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 16),
    _TptNgfwClusterCmpStateChangeNotifyLimitType_Type()
)
tptNgfwClusterCmpStateChangeNotifyLimitType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwClusterCmpStateChangeNotifyLimitType.setStatus("current")
_TptNgfwClusterCmpStateChangeNotifyRelation_Type = ThresholdRelation
_TptNgfwClusterCmpStateChangeNotifyRelation_Object = MibScalar
tptNgfwClusterCmpStateChangeNotifyRelation = _TptNgfwClusterCmpStateChangeNotifyRelation_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 17),
    _TptNgfwClusterCmpStateChangeNotifyRelation_Type()
)
tptNgfwClusterCmpStateChangeNotifyRelation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwClusterCmpStateChangeNotifyRelation.setStatus("current")
_TptNgfwClusterConstChkFailedNotifyType_Type = ConsistencyCheckType
_TptNgfwClusterConstChkFailedNotifyType_Object = MibScalar
tptNgfwClusterConstChkFailedNotifyType = _TptNgfwClusterConstChkFailedNotifyType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 18),
    _TptNgfwClusterConstChkFailedNotifyType_Type()
)
tptNgfwClusterConstChkFailedNotifyType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwClusterConstChkFailedNotifyType.setStatus("current")
_TptNgfwClusterConstChkFailedNotifyMaster_Type = MasterLocation
_TptNgfwClusterConstChkFailedNotifyMaster_Object = MibScalar
tptNgfwClusterConstChkFailedNotifyMaster = _TptNgfwClusterConstChkFailedNotifyMaster_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 19),
    _TptNgfwClusterConstChkFailedNotifyMaster_Type()
)
tptNgfwClusterConstChkFailedNotifyMaster.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwClusterConstChkFailedNotifyMaster.setStatus("current")

# Managed Objects groups

tptNgfwClusterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 1, 2)
)
tptNgfwClusterGroup.setObjects(
      *(("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterName"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterEnabled"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterMemberId"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterMemberName"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterStandby"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterSwConstChecks"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHwConstChecks"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterCfgConstChecks"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterMemberStatusName"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterMemberStatusSerialNo"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterMemberStatusHwModel"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterMemberStatusSwVersion"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterMemberStatusUptime"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterMemberStatusJoinTime"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterMemberStatusSmsManaged"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterMemberStatusCfgControl"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterMemberStatusCfgStateSync"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterMemberStatusEnabled"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterMemberStatusHaState"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterMemberStatusHealthState"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterMemberStatusHealthScore"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterMemberStatusMaster"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterMemberRejectNotifyReason"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHealthChangeNotifyState"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHealthChangeNotifyScore"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHealthChangeNotifyStateUpperLimit"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHealthChangeNotifyStateLowerLimit"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterCmpStateChangeNotifyType"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterCmpStateChangeNotifyName"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterCmpStateChangeNotifyState"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterCmpStateChangeNotifyValue"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterCmpStateChangeNotifyUnits"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterCmpStateChangeNotifyThreshold"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterCmpStateChangeNotifyLimitType"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterCmpStateChangeNotifyRelation"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterConstChkFailedNotifyType"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterConstChkFailedNotifyMaster"))
)
if mibBuilder.loadTexts:
    tptNgfwClusterGroup.setStatus("current")

tptNgfwClusterTrafficGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 1, 3)
)
tptNgfwClusterTrafficGroup.setObjects(
      *(("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterTctIpAddrType"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterTctIpAddr"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterTctMulticastAddrType"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterTctMulticastAddr"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterTctPort"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterTctTtl"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterTctMtu"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterTctTimeout"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterTctRetries"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterTctPortSpeed"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterTctPortDuplex"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterTctPortAutoNeg"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterTctLinkState"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterTctEncryptionEnabled"))
)
if mibBuilder.loadTexts:
    tptNgfwClusterTrafficGroup.setStatus("current")

tptNgfwClusterHaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 1, 4)
)
tptNgfwClusterHaGroup.setObjects(
      *(("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaEnabled"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaGlobalStateSyncEnabled"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaMode"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaFeatSyncEnabled"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaFeatSyncLogSeverity"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaFgId"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaFgName"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaFgBaseMac"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaFgMode"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaFgMemberId"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaFgMemberName"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaFeatSyncStatusEnabled"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaFeatSyncStatusSyncState"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaFeatSyncStatusSyncStateReason"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaFeatSyncStatusTotalEntries"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaFeatSyncStatusAddEntries"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaFeatSyncStatusDelEntries"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaStateSyncNotifyFeature"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaFgStateChangeNotifyState"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaFgStateChangeNotifyActiveDeviceId"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaFgStateChangeNotifyPassiveDeviceId"))
)
if mibBuilder.loadTexts:
    tptNgfwClusterHaGroup.setStatus("current")


# Notification objects

tptNgfwClusterMemberJoinNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 1)
)
tptNgfwClusterMemberJoinNotify.setObjects(
      *(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterName"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterMemberId"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterMemberName"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterTctIpAddrType"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterTctIpAddr"),
        ("TPT-NGFW-REG-MIB", "tptNgfwNotifySeverity"))
)
if mibBuilder.loadTexts:
    tptNgfwClusterMemberJoinNotify.setStatus(
        "current"
    )

tptNgfwClusterMemberLeaveNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 2)
)
tptNgfwClusterMemberLeaveNotify.setObjects(
      *(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterName"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterMemberId"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterMemberName"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterTctIpAddrType"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterTctIpAddr"),
        ("TPT-NGFW-REG-MIB", "tptNgfwNotifySeverity"))
)
if mibBuilder.loadTexts:
    tptNgfwClusterMemberLeaveNotify.setStatus(
        "current"
    )

tptNgfwClusterMemberRejectNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 3)
)
tptNgfwClusterMemberRejectNotify.setObjects(
      *(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterTctIpAddrType"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterTctIpAddr"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterMemberId"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterMemberRejectNotifyReason"),
        ("TPT-NGFW-REG-MIB", "tptNgfwNotifySeverity"))
)
if mibBuilder.loadTexts:
    tptNgfwClusterMemberRejectNotify.setStatus(
        "current"
    )

tptNgfwClusterHaStateSyncMessageLossNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 4)
)
tptNgfwClusterHaStateSyncMessageLossNotify.setObjects(
      *(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaStateSyncNotifyFeature"),
        ("TPT-NGFW-REG-MIB", "tptNgfwNotifySeverity"))
)
if mibBuilder.loadTexts:
    tptNgfwClusterHaStateSyncMessageLossNotify.setStatus(
        "current"
    )

tptNgfwClusterHaStateSyncQueueFullNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 5)
)
tptNgfwClusterHaStateSyncQueueFullNotify.setObjects(
      *(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaStateSyncNotifyFeature"),
        ("TPT-NGFW-REG-MIB", "tptNgfwNotifySeverity"))
)
if mibBuilder.loadTexts:
    tptNgfwClusterHaStateSyncQueueFullNotify.setStatus(
        "current"
    )

tptNgfwClusterHealthChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 6)
)
tptNgfwClusterHealthChangeNotify.setObjects(
      *(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHealthChangeNotifyState"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHealthChangeNotifyScore"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHealthChangeNotifyStateUpperLimit"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHealthChangeNotifyStateLowerLimit"),
        ("TPT-NGFW-REG-MIB", "tptNgfwNotifySeverity"))
)
if mibBuilder.loadTexts:
    tptNgfwClusterHealthChangeNotify.setStatus(
        "current"
    )

tptNgfwClusterHaFgStateChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 7)
)
tptNgfwClusterHaFgStateChangeNotify.setObjects(
      *(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaFgName"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaFgId"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaFgStateChangeNotifyState"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaFgStateChangeNotifyActiveDeviceId"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaFgStateChangeNotifyPassiveDeviceId"),
        ("TPT-NGFW-REG-MIB", "tptNgfwNotifySeverity"))
)
if mibBuilder.loadTexts:
    tptNgfwClusterHaFgStateChangeNotify.setStatus(
        "current"
    )

tptNgfwClusterCmpStateChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 8)
)
tptNgfwClusterCmpStateChangeNotify.setObjects(
      *(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterCmpStateChangeNotifyType"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterCmpStateChangeNotifyName"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterCmpStateChangeNotifyState"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterCmpStateChangeNotifyValue"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterCmpStateChangeNotifyUnits"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterCmpStateChangeNotifyThreshold"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterCmpStateChangeNotifyLimitType"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterCmpStateChangeNotifyRelation"),
        ("TPT-NGFW-REG-MIB", "tptNgfwNotifySeverity"))
)
if mibBuilder.loadTexts:
    tptNgfwClusterCmpStateChangeNotify.setStatus(
        "current"
    )

tptNgfwClusterConstChkFailedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 9)
)
tptNgfwClusterConstChkFailedNotify.setObjects(
      *(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterConstChkFailedNotifyType"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterConstChkFailedNotifyMaster"),
        ("TPT-NGFW-REG-MIB", "tptNgfwNotifySeverity"))
)
if mibBuilder.loadTexts:
    tptNgfwClusterConstChkFailedNotify.setStatus(
        "current"
    )


# Notifications groups

tptNgfwClusterNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 1, 5)
)
tptNgfwClusterNotificationGroup.setObjects(
      *(("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterMemberJoinNotify"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterMemberLeaveNotify"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterMemberRejectNotify"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaStateSyncMessageLossNotify"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaStateSyncQueueFullNotify"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHealthChangeNotify"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterHaFgStateChangeNotify"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterCmpStateChangeNotify"),
        ("TPT-NGFW-CLUSTER-MIB", "tptNgfwClusterConstChkFailedNotify"))
)
if mibBuilder.loadTexts:
    tptNgfwClusterNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tptNgfwClusterCfgCompl = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tptNgfwClusterCfgCompl.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-NGFW-CLUSTER-MIB",
    **{"FailoverGrpMode": FailoverGrpMode,
       "LinkState": LinkState,
       "CfgControl": CfgControl,
       "SyncState": SyncState,
       "HaState": HaState,
       "HealthState": HealthState,
       "ClusterMemberRejectReason": ClusterMemberRejectReason,
       "FailoverGroupState": FailoverGroupState,
       "ComponentType": ComponentType,
       "ThresholdLimitType": ThresholdLimitType,
       "ThresholdRelation": ThresholdRelation,
       "ConsistencyCheckType": ConsistencyCheckType,
       "MasterLocation": MasterLocation,
       "tptNgfwClusterGroup": tptNgfwClusterGroup,
       "tptNgfwClusterTrafficGroup": tptNgfwClusterTrafficGroup,
       "tptNgfwClusterHaGroup": tptNgfwClusterHaGroup,
       "tptNgfwClusterNotificationGroup": tptNgfwClusterNotificationGroup,
       "tptNgfwClusterCfgCompl": tptNgfwClusterCfgCompl,
       "tptNgfwCluster": tptNgfwCluster,
       "tptNgfwClusterName": tptNgfwClusterName,
       "tptNgfwClusterEnabled": tptNgfwClusterEnabled,
       "tptNgfwClusterMemberId": tptNgfwClusterMemberId,
       "tptNgfwClusterMemberName": tptNgfwClusterMemberName,
       "tptNgfwClusterStandby": tptNgfwClusterStandby,
       "tptNgfwClusterSwConstChecks": tptNgfwClusterSwConstChecks,
       "tptNgfwClusterHwConstChecks": tptNgfwClusterHwConstChecks,
       "tptNgfwClusterCfgConstChecks": tptNgfwClusterCfgConstChecks,
       "tptNgfwClusterMemberStatusTable": tptNgfwClusterMemberStatusTable,
       "tptNgfwClusterMemberStatusTableEntry": tptNgfwClusterMemberStatusTableEntry,
       "tptNgfwClusterMemberStatusId": tptNgfwClusterMemberStatusId,
       "tptNgfwClusterMemberStatusName": tptNgfwClusterMemberStatusName,
       "tptNgfwClusterMemberStatusSerialNo": tptNgfwClusterMemberStatusSerialNo,
       "tptNgfwClusterMemberStatusHwModel": tptNgfwClusterMemberStatusHwModel,
       "tptNgfwClusterMemberStatusSwVersion": tptNgfwClusterMemberStatusSwVersion,
       "tptNgfwClusterMemberStatusUptime": tptNgfwClusterMemberStatusUptime,
       "tptNgfwClusterMemberStatusJoinTime": tptNgfwClusterMemberStatusJoinTime,
       "tptNgfwClusterMemberStatusSmsManaged": tptNgfwClusterMemberStatusSmsManaged,
       "tptNgfwClusterMemberStatusCfgControl": tptNgfwClusterMemberStatusCfgControl,
       "tptNgfwClusterMemberStatusCfgStateSync": tptNgfwClusterMemberStatusCfgStateSync,
       "tptNgfwClusterMemberStatusEnabled": tptNgfwClusterMemberStatusEnabled,
       "tptNgfwClusterMemberStatusHaState": tptNgfwClusterMemberStatusHaState,
       "tptNgfwClusterMemberStatusHealthState": tptNgfwClusterMemberStatusHealthState,
       "tptNgfwClusterMemberStatusHealthScore": tptNgfwClusterMemberStatusHealthScore,
       "tptNgfwClusterMemberStatusMaster": tptNgfwClusterMemberStatusMaster,
       "tptNgfwClusterTraffic": tptNgfwClusterTraffic,
       "tptNgfwClusterTctIpAddrType": tptNgfwClusterTctIpAddrType,
       "tptNgfwClusterTctIpAddr": tptNgfwClusterTctIpAddr,
       "tptNgfwClusterTctMulticastAddrType": tptNgfwClusterTctMulticastAddrType,
       "tptNgfwClusterTctMulticastAddr": tptNgfwClusterTctMulticastAddr,
       "tptNgfwClusterTctPort": tptNgfwClusterTctPort,
       "tptNgfwClusterTctTtl": tptNgfwClusterTctTtl,
       "tptNgfwClusterTctMtu": tptNgfwClusterTctMtu,
       "tptNgfwClusterTctTimeout": tptNgfwClusterTctTimeout,
       "tptNgfwClusterTctRetries": tptNgfwClusterTctRetries,
       "tptNgfwClusterTctPortSpeed": tptNgfwClusterTctPortSpeed,
       "tptNgfwClusterTctPortDuplex": tptNgfwClusterTctPortDuplex,
       "tptNgfwClusterTctPortAutoNeg": tptNgfwClusterTctPortAutoNeg,
       "tptNgfwClusterTctLinkState": tptNgfwClusterTctLinkState,
       "tptNgfwClusterTctEncryptionEnabled": tptNgfwClusterTctEncryptionEnabled,
       "tptNgfwClusterHa": tptNgfwClusterHa,
       "tptNgfwClusterHaEnabled": tptNgfwClusterHaEnabled,
       "tptNgfwClusterHaGlobalStateSyncEnabled": tptNgfwClusterHaGlobalStateSyncEnabled,
       "tptNgfwClusterHaMode": tptNgfwClusterHaMode,
       "tptNgfwClusterHaFeatSyncTable": tptNgfwClusterHaFeatSyncTable,
       "tptNgfwClusterHaFeatSyncTableEntry": tptNgfwClusterHaFeatSyncTableEntry,
       "tptNgfwClusterHaFeatSyncFeature": tptNgfwClusterHaFeatSyncFeature,
       "tptNgfwClusterHaFeatSyncEnabled": tptNgfwClusterHaFeatSyncEnabled,
       "tptNgfwClusterHaFeatSyncLogSeverity": tptNgfwClusterHaFeatSyncLogSeverity,
       "tptNgfwClusterHaFgTable": tptNgfwClusterHaFgTable,
       "tptNgfwClusterHaFgEntry": tptNgfwClusterHaFgEntry,
       "tptNgfwClusterHaFgIndex": tptNgfwClusterHaFgIndex,
       "tptNgfwClusterHaFgId": tptNgfwClusterHaFgId,
       "tptNgfwClusterHaFgName": tptNgfwClusterHaFgName,
       "tptNgfwClusterHaFgBaseMac": tptNgfwClusterHaFgBaseMac,
       "tptNgfwClusterHaFgMode": tptNgfwClusterHaFgMode,
       "tptNgfwClusterHaFgMemberTable": tptNgfwClusterHaFgMemberTable,
       "tptNgfwClusterHaFgMemberEntry": tptNgfwClusterHaFgMemberEntry,
       "tptNgfwClusterHaFgMemberId": tptNgfwClusterHaFgMemberId,
       "tptNgfwClusterHaFgMemberName": tptNgfwClusterHaFgMemberName,
       "tptNgfwClusterHaFeatSyncStatusTable": tptNgfwClusterHaFeatSyncStatusTable,
       "tptNgfwClusterHaFeatSyncStatusTableEntry": tptNgfwClusterHaFeatSyncStatusTableEntry,
       "tptNgfwClusterHaFeatSyncStatusFeature": tptNgfwClusterHaFeatSyncStatusFeature,
       "tptNgfwClusterHaFeatSyncStatusEnabled": tptNgfwClusterHaFeatSyncStatusEnabled,
       "tptNgfwClusterHaFeatSyncStatusSyncState": tptNgfwClusterHaFeatSyncStatusSyncState,
       "tptNgfwClusterHaFeatSyncStatusSyncStateReason": tptNgfwClusterHaFeatSyncStatusSyncStateReason,
       "tptNgfwClusterHaFeatSyncStatusTotalEntries": tptNgfwClusterHaFeatSyncStatusTotalEntries,
       "tptNgfwClusterHaFeatSyncStatusAddEntries": tptNgfwClusterHaFeatSyncStatusAddEntries,
       "tptNgfwClusterHaFeatSyncStatusDelEntries": tptNgfwClusterHaFeatSyncStatusDelEntries,
       "tptNgfwClusterMemberJoinNotify": tptNgfwClusterMemberJoinNotify,
       "tptNgfwClusterMemberLeaveNotify": tptNgfwClusterMemberLeaveNotify,
       "tptNgfwClusterMemberRejectNotify": tptNgfwClusterMemberRejectNotify,
       "tptNgfwClusterHaStateSyncMessageLossNotify": tptNgfwClusterHaStateSyncMessageLossNotify,
       "tptNgfwClusterHaStateSyncQueueFullNotify": tptNgfwClusterHaStateSyncQueueFullNotify,
       "tptNgfwClusterHealthChangeNotify": tptNgfwClusterHealthChangeNotify,
       "tptNgfwClusterHaFgStateChangeNotify": tptNgfwClusterHaFgStateChangeNotify,
       "tptNgfwClusterCmpStateChangeNotify": tptNgfwClusterCmpStateChangeNotify,
       "tptNgfwClusterConstChkFailedNotify": tptNgfwClusterConstChkFailedNotify,
       "tptNgfwClusterMemberRejectNotifyReason": tptNgfwClusterMemberRejectNotifyReason,
       "tptNgfwClusterHaStateSyncNotifyFeature": tptNgfwClusterHaStateSyncNotifyFeature,
       "tptNgfwClusterHealthChangeNotifyState": tptNgfwClusterHealthChangeNotifyState,
       "tptNgfwClusterHealthChangeNotifyScore": tptNgfwClusterHealthChangeNotifyScore,
       "tptNgfwClusterHealthChangeNotifyStateUpperLimit": tptNgfwClusterHealthChangeNotifyStateUpperLimit,
       "tptNgfwClusterHealthChangeNotifyStateLowerLimit": tptNgfwClusterHealthChangeNotifyStateLowerLimit,
       "tptNgfwClusterHaFgStateChangeNotifyState": tptNgfwClusterHaFgStateChangeNotifyState,
       "tptNgfwClusterHaFgStateChangeNotifyActiveDeviceId": tptNgfwClusterHaFgStateChangeNotifyActiveDeviceId,
       "tptNgfwClusterHaFgStateChangeNotifyPassiveDeviceId": tptNgfwClusterHaFgStateChangeNotifyPassiveDeviceId,
       "tptNgfwClusterCmpStateChangeNotifyType": tptNgfwClusterCmpStateChangeNotifyType,
       "tptNgfwClusterCmpStateChangeNotifyName": tptNgfwClusterCmpStateChangeNotifyName,
       "tptNgfwClusterCmpStateChangeNotifyState": tptNgfwClusterCmpStateChangeNotifyState,
       "tptNgfwClusterCmpStateChangeNotifyValue": tptNgfwClusterCmpStateChangeNotifyValue,
       "tptNgfwClusterCmpStateChangeNotifyUnits": tptNgfwClusterCmpStateChangeNotifyUnits,
       "tptNgfwClusterCmpStateChangeNotifyThreshold": tptNgfwClusterCmpStateChangeNotifyThreshold,
       "tptNgfwClusterCmpStateChangeNotifyLimitType": tptNgfwClusterCmpStateChangeNotifyLimitType,
       "tptNgfwClusterCmpStateChangeNotifyRelation": tptNgfwClusterCmpStateChangeNotifyRelation,
       "tptNgfwClusterConstChkFailedNotifyType": tptNgfwClusterConstChkFailedNotifyType,
       "tptNgfwClusterConstChkFailedNotifyMaster": tptNgfwClusterConstChkFailedNotifyMaster}
)
