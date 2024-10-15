# SNMP MIB module (CPM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:11 2024
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

(dialaccess,) = mibBuilder.importSymbols(
    "CPM-NORTEL-MIB",
    "dialaccess")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

cpm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cpm_conf_ObjectIdentity = ObjectIdentity
cpm_conf = _Cpm_conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 1)
)
if mibBuilder.loadTexts:
    cpm_conf.setStatus("current")
_Cpm_sysconf_ObjectIdentity = ObjectIdentity
cpm_sysconf = _Cpm_sysconf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cpm_sysconf.setStatus("current")
_SysAbsStartTime_Type = Integer32
_SysAbsStartTime_Object = MibScalar
sysAbsStartTime = _SysAbsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 1, 1, 1),
    _SysAbsStartTime_Type()
)
sysAbsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAbsStartTime.setStatus("current")


class _SysMibRevision_Type(DisplayString):
    """Custom type sysMibRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SysMibRevision_Type.__name__ = "DisplayString"
_SysMibRevision_Object = MibScalar
sysMibRevision = _SysMibRevision_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 1, 1, 2),
    _SysMibRevision_Type()
)
sysMibRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMibRevision.setStatus("current")


class _SysSoftwareRevision_Type(DisplayString):
    """Custom type sysSoftwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SysSoftwareRevision_Type.__name__ = "DisplayString"
_SysSoftwareRevision_Object = MibScalar
sysSoftwareRevision = _SysSoftwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 1, 1, 3),
    _SysSoftwareRevision_Type()
)
sysSoftwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSoftwareRevision.setStatus("current")


class _SysConfigFile_Type(DisplayString):
    """Custom type sysConfigFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_SysConfigFile_Type.__name__ = "DisplayString"
_SysConfigFile_Object = MibScalar
sysConfigFile = _SysConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 1, 1, 4),
    _SysConfigFile_Type()
)
sysConfigFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysConfigFile.setStatus("current")


class _SysLogFile_Type(DisplayString):
    """Custom type sysLogFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_SysLogFile_Type.__name__ = "DisplayString"
_SysLogFile_Object = MibScalar
sysLogFile = _SysLogFile_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 1, 1, 5),
    _SysLogFile_Type()
)
sysLogFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLogFile.setStatus("current")
_SysLogFileMaxSize_Type = Integer32
_SysLogFileMaxSize_Object = MibScalar
sysLogFileMaxSize = _SysLogFileMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 1, 1, 6),
    _SysLogFileMaxSize_Type()
)
sysLogFileMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLogFileMaxSize.setStatus("current")
_SysTraceLevel_Type = Integer32
_SysTraceLevel_Object = MibScalar
sysTraceLevel = _SysTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 1, 1, 7),
    _SysTraceLevel_Type()
)
sysTraceLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTraceLevel.setStatus("current")


class _SysOperationalState_Type(Integer32):
    """Custom type sysOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discovering", 1),
          ("initializing", 0),
          ("ready", 2))
    )


_SysOperationalState_Type.__name__ = "Integer32"
_SysOperationalState_Object = MibScalar
sysOperationalState = _SysOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 1, 1, 8),
    _SysOperationalState_Type()
)
sysOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysOperationalState.setStatus("current")
_Cpm_performance_ObjectIdentity = ObjectIdentity
cpm_performance = _Cpm_performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 2)
)
if mibBuilder.loadTexts:
    cpm_performance.setStatus("current")
_CpmVpopOMTable_Object = MibTable
cpmVpopOMTable = _CpmVpopOMTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cpmVpopOMTable.setStatus("current")
_CpmVpopOMEntry_Object = MibTableRow
cpmVpopOMEntry = _CpmVpopOMEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1)
)
cpmVpopOMEntry.setIndexNames(
    (0, "CPM-MIB", "cpmVpopOMVpopId"),
)
if mibBuilder.loadTexts:
    cpmVpopOMEntry.setStatus("current")
_CpmVpopOMVpopId_Type = Integer32
_CpmVpopOMVpopId_Object = MibTableColumn
cpmVpopOMVpopId = _CpmVpopOMVpopId_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1, 1),
    _CpmVpopOMVpopId_Type()
)
cpmVpopOMVpopId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVpopOMVpopId.setStatus("current")
_CpmVpopOMPortLimit_Type = Integer32
_CpmVpopOMPortLimit_Object = MibTableColumn
cpmVpopOMPortLimit = _CpmVpopOMPortLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1, 2),
    _CpmVpopOMPortLimit_Type()
)
cpmVpopOMPortLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVpopOMPortLimit.setStatus("current")
_CpmVpopOMOverflowPortLimit_Type = Integer32
_CpmVpopOMOverflowPortLimit_Object = MibTableColumn
cpmVpopOMOverflowPortLimit = _CpmVpopOMOverflowPortLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1, 3),
    _CpmVpopOMOverflowPortLimit_Type()
)
cpmVpopOMOverflowPortLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVpopOMOverflowPortLimit.setStatus("current")
_CpmVpopOMActiveCalls_Type = Integer32
_CpmVpopOMActiveCalls_Object = MibTableColumn
cpmVpopOMActiveCalls = _CpmVpopOMActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1, 4),
    _CpmVpopOMActiveCalls_Type()
)
cpmVpopOMActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVpopOMActiveCalls.setStatus("current")
_CpmVpopOMActivePortLimitCalls_Type = Integer32
_CpmVpopOMActivePortLimitCalls_Object = MibTableColumn
cpmVpopOMActivePortLimitCalls = _CpmVpopOMActivePortLimitCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1, 5),
    _CpmVpopOMActivePortLimitCalls_Type()
)
cpmVpopOMActivePortLimitCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVpopOMActivePortLimitCalls.setStatus("current")
_CpmVpopOMAcceptedCalls_Type = Integer32
_CpmVpopOMAcceptedCalls_Object = MibTableColumn
cpmVpopOMAcceptedCalls = _CpmVpopOMAcceptedCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1, 6),
    _CpmVpopOMAcceptedCalls_Type()
)
cpmVpopOMAcceptedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVpopOMAcceptedCalls.setStatus("current")
_CpmVpopOMAcceptedOverflowCalls_Type = Integer32
_CpmVpopOMAcceptedOverflowCalls_Object = MibTableColumn
cpmVpopOMAcceptedOverflowCalls = _CpmVpopOMAcceptedOverflowCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1, 7),
    _CpmVpopOMAcceptedOverflowCalls_Type()
)
cpmVpopOMAcceptedOverflowCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVpopOMAcceptedOverflowCalls.setStatus("current")
_CpmVpopOMReleasedCalls_Type = Integer32
_CpmVpopOMReleasedCalls_Object = MibTableColumn
cpmVpopOMReleasedCalls = _CpmVpopOMReleasedCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1, 8),
    _CpmVpopOMReleasedCalls_Type()
)
cpmVpopOMReleasedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVpopOMReleasedCalls.setStatus("current")
_CpmVpopOMPortLimitReject_Type = Integer32
_CpmVpopOMPortLimitReject_Object = MibTableColumn
cpmVpopOMPortLimitReject = _CpmVpopOMPortLimitReject_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1, 9),
    _CpmVpopOMPortLimitReject_Type()
)
cpmVpopOMPortLimitReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVpopOMPortLimitReject.setStatus("current")
_CpmVpopOMOverflowPortLimitReject_Type = Integer32
_CpmVpopOMOverflowPortLimitReject_Object = MibTableColumn
cpmVpopOMOverflowPortLimitReject = _CpmVpopOMOverflowPortLimitReject_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1, 10),
    _CpmVpopOMOverflowPortLimitReject_Type()
)
cpmVpopOMOverflowPortLimitReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVpopOMOverflowPortLimitReject.setStatus("current")
_CpmVpopOMClidFilterReject_Type = Integer32
_CpmVpopOMClidFilterReject_Object = MibTableColumn
cpmVpopOMClidFilterReject = _CpmVpopOMClidFilterReject_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1, 11),
    _CpmVpopOMClidFilterReject_Type()
)
cpmVpopOMClidFilterReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVpopOMClidFilterReject.setStatus("current")
_CpmVpopOMProxyReject_Type = Integer32
_CpmVpopOMProxyReject_Object = MibTableColumn
cpmVpopOMProxyReject = _CpmVpopOMProxyReject_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1, 12),
    _CpmVpopOMProxyReject_Type()
)
cpmVpopOMProxyReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVpopOMProxyReject.setStatus("current")
_CpmVpopOMIPAddressReject_Type = Integer32
_CpmVpopOMIPAddressReject_Object = MibTableColumn
cpmVpopOMIPAddressReject = _CpmVpopOMIPAddressReject_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1, 13),
    _CpmVpopOMIPAddressReject_Type()
)
cpmVpopOMIPAddressReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVpopOMIPAddressReject.setStatus("current")
_CpmVpopOMGatewayReject_Type = Integer32
_CpmVpopOMGatewayReject_Object = MibTableColumn
cpmVpopOMGatewayReject = _CpmVpopOMGatewayReject_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1, 14),
    _CpmVpopOMGatewayReject_Type()
)
cpmVpopOMGatewayReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVpopOMGatewayReject.setStatus("current")
_CpmVpopOMGuaranteeReject_Type = Integer32
_CpmVpopOMGuaranteeReject_Object = MibTableColumn
cpmVpopOMGuaranteeReject = _CpmVpopOMGuaranteeReject_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 1, 1, 15),
    _CpmVpopOMGuaranteeReject_Type()
)
cpmVpopOMGuaranteeReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVpopOMGuaranteeReject.setStatus("current")
_CpmVpopOMSnapshotTable_Object = MibTable
cpmVpopOMSnapshotTable = _CpmVpopOMSnapshotTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 2)
)
if mibBuilder.loadTexts:
    cpmVpopOMSnapshotTable.setStatus("current")
_CpmVpopOMSnapshotEntry_Object = MibTableRow
cpmVpopOMSnapshotEntry = _CpmVpopOMSnapshotEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 2, 1)
)
cpmVpopOMSnapshotEntry.setIndexNames(
    (0, "CPM-MIB", "cpmVpopOMSnapshotVpopId"),
    (0, "CPM-MIB", "cpmVpopOMSnapshotTimeStamp"),
)
if mibBuilder.loadTexts:
    cpmVpopOMSnapshotEntry.setStatus("current")
_CpmVpopOMSnapshotVpopId_Type = Integer32
_CpmVpopOMSnapshotVpopId_Object = MibTableColumn
cpmVpopOMSnapshotVpopId = _CpmVpopOMSnapshotVpopId_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 2, 1, 1),
    _CpmVpopOMSnapshotVpopId_Type()
)
cpmVpopOMSnapshotVpopId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVpopOMSnapshotVpopId.setStatus("current")
_CpmVpopOMSnapshotTimeStamp_Type = Integer32
_CpmVpopOMSnapshotTimeStamp_Object = MibTableColumn
cpmVpopOMSnapshotTimeStamp = _CpmVpopOMSnapshotTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 2, 1, 2),
    _CpmVpopOMSnapshotTimeStamp_Type()
)
cpmVpopOMSnapshotTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVpopOMSnapshotTimeStamp.setStatus("current")
_CpmVpopOMSnapshotMinCalls_Type = Integer32
_CpmVpopOMSnapshotMinCalls_Object = MibTableColumn
cpmVpopOMSnapshotMinCalls = _CpmVpopOMSnapshotMinCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 2, 1, 3),
    _CpmVpopOMSnapshotMinCalls_Type()
)
cpmVpopOMSnapshotMinCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVpopOMSnapshotMinCalls.setStatus("current")
_CpmVpopOMSnapshotMaxCalls_Type = Integer32
_CpmVpopOMSnapshotMaxCalls_Object = MibTableColumn
cpmVpopOMSnapshotMaxCalls = _CpmVpopOMSnapshotMaxCalls_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 2, 2, 1, 4),
    _CpmVpopOMSnapshotMaxCalls_Type()
)
cpmVpopOMSnapshotMaxCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmVpopOMSnapshotMaxCalls.setStatus("current")
_Cpm_surv_ObjectIdentity = ObjectIdentity
cpm_surv = _Cpm_surv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 3)
)
if mibBuilder.loadTexts:
    cpm_surv.setStatus("current")
_Cpm_trapVariables_ObjectIdentity = ObjectIdentity
cpm_trapVariables = _Cpm_trapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 1)
)
if mibBuilder.loadTexts:
    cpm_trapVariables.setStatus("current")


class _Trap_severity_Type(Integer32):
    """Custom type trap_severity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("major", 3),
          ("minor", 2),
          ("normal", 0),
          ("warning", 1))
    )


_Trap_severity_Type.__name__ = "Integer32"
_Trap_severity_Object = MibScalar
trap_severity = _Trap_severity_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 1, 1),
    _Trap_severity_Type()
)
trap_severity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_severity.setStatus("current")
_Trap_nasIPAddress_Type = IpAddress
_Trap_nasIPAddress_Object = MibScalar
trap_nasIPAddress = _Trap_nasIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 1, 2),
    _Trap_nasIPAddress_Type()
)
trap_nasIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_nasIPAddress.setStatus("current")
_Trap_gatewayIPAddress_Type = IpAddress
_Trap_gatewayIPAddress_Object = MibScalar
trap_gatewayIPAddress = _Trap_gatewayIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 1, 3),
    _Trap_gatewayIPAddress_Type()
)
trap_gatewayIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_gatewayIPAddress.setStatus("current")
_Trap_vpopId_Type = Integer32
_Trap_vpopId_Object = MibScalar
trap_vpopId = _Trap_vpopId_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 1, 4),
    _Trap_vpopId_Type()
)
trap_vpopId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_vpopId.setStatus("current")
_Trap_gennum_Type = Integer32
_Trap_gennum_Object = MibScalar
trap_gennum = _Trap_gennum_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 1, 5),
    _Trap_gennum_Type()
)
trap_gennum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_gennum.setStatus("current")
_Trap_AAAServerIPAddress_Type = IpAddress
_Trap_AAAServerIPAddress_Object = MibScalar
trap_AAAServerIPAddress = _Trap_AAAServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 1, 6),
    _Trap_AAAServerIPAddress_Type()
)
trap_AAAServerIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trap_AAAServerIPAddress.setStatus("current")
_CpmAlarmTable_Object = MibTable
cpmAlarmTable = _CpmAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 2)
)
if mibBuilder.loadTexts:
    cpmAlarmTable.setStatus("current")
_CpmAlarmTableEntry_Object = MibTableRow
cpmAlarmTableEntry = _CpmAlarmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 2, 1)
)
cpmAlarmTableEntry.setIndexNames(
    (0, "CPM-MIB", "cpmAlarmTableTrapGenNum"),
)
if mibBuilder.loadTexts:
    cpmAlarmTableEntry.setStatus("current")
_CpmAlarmTableTrapGenNum_Type = Integer32
_CpmAlarmTableTrapGenNum_Object = MibTableColumn
cpmAlarmTableTrapGenNum = _CpmAlarmTableTrapGenNum_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 2, 1, 1),
    _CpmAlarmTableTrapGenNum_Type()
)
cpmAlarmTableTrapGenNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAlarmTableTrapGenNum.setStatus("current")


class _CpmAlarmTableTrapType_Type(Integer32):
    """Custom type cpmAlarmTableTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              6,
              8,
              10,
              12,
              14)
        )
    )
    namedValues = NamedValues(
        *(("gatewayRemovedFromService", 4),
          ("gatewaysUnavailable", 6),
          ("ipAddressExhausted", 10),
          ("mpGatewaysUnavailable", 8),
          ("nasNotResponding", 2),
          ("overflowPortsInUse", 14),
          ("portsUnavailable", 12))
    )


_CpmAlarmTableTrapType_Type.__name__ = "Integer32"
_CpmAlarmTableTrapType_Object = MibTableColumn
cpmAlarmTableTrapType = _CpmAlarmTableTrapType_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 2, 1, 2),
    _CpmAlarmTableTrapType_Type()
)
cpmAlarmTableTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAlarmTableTrapType.setStatus("current")


class _CpmAlarmTableTrapSeverity_Type(Integer32):
    """Custom type cpmAlarmTableTrapSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("warning", 1))
    )


_CpmAlarmTableTrapSeverity_Type.__name__ = "Integer32"
_CpmAlarmTableTrapSeverity_Object = MibTableColumn
cpmAlarmTableTrapSeverity = _CpmAlarmTableTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 2, 1, 3),
    _CpmAlarmTableTrapSeverity_Type()
)
cpmAlarmTableTrapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAlarmTableTrapSeverity.setStatus("current")
_CpmAlarmTableTrapTimeTicks_Type = Integer32
_CpmAlarmTableTrapTimeTicks_Object = MibTableColumn
cpmAlarmTableTrapTimeTicks = _CpmAlarmTableTrapTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 2, 1, 4),
    _CpmAlarmTableTrapTimeTicks_Type()
)
cpmAlarmTableTrapTimeTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAlarmTableTrapTimeTicks.setStatus("current")


class _CpmAlarmTableTrapArg1_Type(DisplayString):
    """Custom type cpmAlarmTableTrapArg1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_CpmAlarmTableTrapArg1_Type.__name__ = "DisplayString"
_CpmAlarmTableTrapArg1_Object = MibTableColumn
cpmAlarmTableTrapArg1 = _CpmAlarmTableTrapArg1_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 2, 1, 5),
    _CpmAlarmTableTrapArg1_Type()
)
cpmAlarmTableTrapArg1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAlarmTableTrapArg1.setStatus("current")


class _CpmAlarmTableTrapArg2_Type(DisplayString):
    """Custom type cpmAlarmTableTrapArg2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_CpmAlarmTableTrapArg2_Type.__name__ = "DisplayString"
_CpmAlarmTableTrapArg2_Object = MibTableColumn
cpmAlarmTableTrapArg2 = _CpmAlarmTableTrapArg2_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 2, 1, 6),
    _CpmAlarmTableTrapArg2_Type()
)
cpmAlarmTableTrapArg2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAlarmTableTrapArg2.setStatus("current")


class _CpmAlarmTableTrapArg3_Type(DisplayString):
    """Custom type cpmAlarmTableTrapArg3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_CpmAlarmTableTrapArg3_Type.__name__ = "DisplayString"
_CpmAlarmTableTrapArg3_Object = MibTableColumn
cpmAlarmTableTrapArg3 = _CpmAlarmTableTrapArg3_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 3, 2, 1, 7),
    _CpmAlarmTableTrapArg3_Type()
)
cpmAlarmTableTrapArg3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAlarmTableTrapArg3.setStatus("current")

# Managed Objects groups


# Notification objects

cpmStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 0, 1)
)
cpmStateChangeTrap.setObjects(
      *(("CPM-MIB", "trap_gennum"),
        ("CPM-MIB", "trap_severity"),
        ("CPM-MIB", "sysOperationalState"))
)
if mibBuilder.loadTexts:
    cpmStateChangeTrap.setStatus(
        ""
    )

nasNotRespondingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 0, 2)
)
nasNotRespondingTrap.setObjects(
      *(("CPM-MIB", "trap_gennum"),
        ("CPM-MIB", "trap_severity"),
        ("CPM-MIB", "trap_nasIPAddress"))
)
if mibBuilder.loadTexts:
    nasNotRespondingTrap.setStatus(
        ""
    )

nasNowRespondingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 0, 3)
)
nasNowRespondingTrap.setObjects(
      *(("CPM-MIB", "trap_gennum"),
        ("CPM-MIB", "trap_severity"),
        ("CPM-MIB", "trap_nasIPAddress"))
)
if mibBuilder.loadTexts:
    nasNowRespondingTrap.setStatus(
        ""
    )

gatewayRemovedFromService = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 0, 4)
)
gatewayRemovedFromService.setObjects(
      *(("CPM-MIB", "trap_gennum"),
        ("CPM-MIB", "trap_severity"),
        ("CPM-MIB", "trap_gatewayIPAddress"))
)
if mibBuilder.loadTexts:
    gatewayRemovedFromService.setStatus(
        ""
    )

gatewayReturnedToService = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 0, 5)
)
gatewayReturnedToService.setObjects(
      *(("CPM-MIB", "trap_gennum"),
        ("CPM-MIB", "trap_severity"),
        ("CPM-MIB", "trap_gatewayIPAddress"))
)
if mibBuilder.loadTexts:
    gatewayReturnedToService.setStatus(
        ""
    )

gatewaysUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 0, 6)
)
gatewaysUnavailable.setObjects(
      *(("CPM-MIB", "trap_gennum"),
        ("CPM-MIB", "trap_severity"),
        ("CPM-MIB", "trap_vpopId"))
)
if mibBuilder.loadTexts:
    gatewaysUnavailable.setStatus(
        ""
    )

gatewaysAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 0, 7)
)
gatewaysAvailable.setObjects(
      *(("CPM-MIB", "trap_gennum"),
        ("CPM-MIB", "trap_severity"),
        ("CPM-MIB", "trap_vpopId"))
)
if mibBuilder.loadTexts:
    gatewaysAvailable.setStatus(
        ""
    )

mpGatewaysUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 0, 8)
)
mpGatewaysUnavailable.setObjects(
      *(("CPM-MIB", "trap_gennum"),
        ("CPM-MIB", "trap_severity"),
        ("CPM-MIB", "trap_vpopId"))
)
if mibBuilder.loadTexts:
    mpGatewaysUnavailable.setStatus(
        ""
    )

mpGatewaysAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 0, 9)
)
mpGatewaysAvailable.setObjects(
      *(("CPM-MIB", "trap_gennum"),
        ("CPM-MIB", "trap_severity"),
        ("CPM-MIB", "trap_vpopId"))
)
if mibBuilder.loadTexts:
    mpGatewaysAvailable.setStatus(
        ""
    )

ipAddressesExhausted = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 0, 10)
)
ipAddressesExhausted.setObjects(
      *(("CPM-MIB", "trap_gennum"),
        ("CPM-MIB", "trap_severity"),
        ("CPM-MIB", "trap_vpopId"),
        ("CPM-MIB", "trap_nasIPAddress"))
)
if mibBuilder.loadTexts:
    ipAddressesExhausted.setStatus(
        ""
    )

ipAddressesAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 0, 11)
)
ipAddressesAvailable.setObjects(
      *(("CPM-MIB", "trap_gennum"),
        ("CPM-MIB", "trap_severity"),
        ("CPM-MIB", "trap_vpopId"),
        ("CPM-MIB", "trap_nasIPAddress"))
)
if mibBuilder.loadTexts:
    ipAddressesAvailable.setStatus(
        ""
    )

portsUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 0, 12)
)
portsUnavailable.setObjects(
      *(("CPM-MIB", "trap_gennum"),
        ("CPM-MIB", "trap_severity"),
        ("CPM-MIB", "trap_vpopId"))
)
if mibBuilder.loadTexts:
    portsUnavailable.setStatus(
        ""
    )

portsAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 0, 13)
)
portsAvailable.setObjects(
      *(("CPM-MIB", "trap_gennum"),
        ("CPM-MIB", "trap_severity"),
        ("CPM-MIB", "trap_vpopId"))
)
if mibBuilder.loadTexts:
    portsAvailable.setStatus(
        ""
    )

overflowPortsInUse = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 0, 14)
)
overflowPortsInUse.setObjects(
      *(("CPM-MIB", "trap_gennum"),
        ("CPM-MIB", "trap_severity"),
        ("CPM-MIB", "trap_vpopId"))
)
if mibBuilder.loadTexts:
    overflowPortsInUse.setStatus(
        ""
    )

overflowPortsNotInUse = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 0, 15)
)
overflowPortsNotInUse.setObjects(
      *(("CPM-MIB", "trap_gennum"),
        ("CPM-MIB", "trap_severity"),
        ("CPM-MIB", "trap_vpopId"))
)
if mibBuilder.loadTexts:
    overflowPortsNotInUse.setStatus(
        ""
    )

disconnectRequestDiscarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 3, 0, 16)
)
disconnectRequestDiscarded.setObjects(
      *(("CPM-MIB", "trap_gennum"),
        ("CPM-MIB", "trap_severity"),
        ("CPM-MIB", "trap_AAAServerIPAddress"))
)
if mibBuilder.loadTexts:
    disconnectRequestDiscarded.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPM-MIB",
    **{"cpm": cpm,
       "cpmStateChangeTrap": cpmStateChangeTrap,
       "nasNotRespondingTrap": nasNotRespondingTrap,
       "nasNowRespondingTrap": nasNowRespondingTrap,
       "gatewayRemovedFromService": gatewayRemovedFromService,
       "gatewayReturnedToService": gatewayReturnedToService,
       "gatewaysUnavailable": gatewaysUnavailable,
       "gatewaysAvailable": gatewaysAvailable,
       "mpGatewaysUnavailable": mpGatewaysUnavailable,
       "mpGatewaysAvailable": mpGatewaysAvailable,
       "ipAddressesExhausted": ipAddressesExhausted,
       "ipAddressesAvailable": ipAddressesAvailable,
       "portsUnavailable": portsUnavailable,
       "portsAvailable": portsAvailable,
       "overflowPortsInUse": overflowPortsInUse,
       "overflowPortsNotInUse": overflowPortsNotInUse,
       "disconnectRequestDiscarded": disconnectRequestDiscarded,
       "cpm-conf": cpm_conf,
       "cpm-sysconf": cpm_sysconf,
       "sysAbsStartTime": sysAbsStartTime,
       "sysMibRevision": sysMibRevision,
       "sysSoftwareRevision": sysSoftwareRevision,
       "sysConfigFile": sysConfigFile,
       "sysLogFile": sysLogFile,
       "sysLogFileMaxSize": sysLogFileMaxSize,
       "sysTraceLevel": sysTraceLevel,
       "sysOperationalState": sysOperationalState,
       "cpm-performance": cpm_performance,
       "cpmVpopOMTable": cpmVpopOMTable,
       "cpmVpopOMEntry": cpmVpopOMEntry,
       "cpmVpopOMVpopId": cpmVpopOMVpopId,
       "cpmVpopOMPortLimit": cpmVpopOMPortLimit,
       "cpmVpopOMOverflowPortLimit": cpmVpopOMOverflowPortLimit,
       "cpmVpopOMActiveCalls": cpmVpopOMActiveCalls,
       "cpmVpopOMActivePortLimitCalls": cpmVpopOMActivePortLimitCalls,
       "cpmVpopOMAcceptedCalls": cpmVpopOMAcceptedCalls,
       "cpmVpopOMAcceptedOverflowCalls": cpmVpopOMAcceptedOverflowCalls,
       "cpmVpopOMReleasedCalls": cpmVpopOMReleasedCalls,
       "cpmVpopOMPortLimitReject": cpmVpopOMPortLimitReject,
       "cpmVpopOMOverflowPortLimitReject": cpmVpopOMOverflowPortLimitReject,
       "cpmVpopOMClidFilterReject": cpmVpopOMClidFilterReject,
       "cpmVpopOMProxyReject": cpmVpopOMProxyReject,
       "cpmVpopOMIPAddressReject": cpmVpopOMIPAddressReject,
       "cpmVpopOMGatewayReject": cpmVpopOMGatewayReject,
       "cpmVpopOMGuaranteeReject": cpmVpopOMGuaranteeReject,
       "cpmVpopOMSnapshotTable": cpmVpopOMSnapshotTable,
       "cpmVpopOMSnapshotEntry": cpmVpopOMSnapshotEntry,
       "cpmVpopOMSnapshotVpopId": cpmVpopOMSnapshotVpopId,
       "cpmVpopOMSnapshotTimeStamp": cpmVpopOMSnapshotTimeStamp,
       "cpmVpopOMSnapshotMinCalls": cpmVpopOMSnapshotMinCalls,
       "cpmVpopOMSnapshotMaxCalls": cpmVpopOMSnapshotMaxCalls,
       "cpm-surv": cpm_surv,
       "cpm-trapVariables": cpm_trapVariables,
       "trap-severity": trap_severity,
       "trap-nasIPAddress": trap_nasIPAddress,
       "trap-gatewayIPAddress": trap_gatewayIPAddress,
       "trap-vpopId": trap_vpopId,
       "trap-gennum": trap_gennum,
       "trap-AAAServerIPAddress": trap_AAAServerIPAddress,
       "cpmAlarmTable": cpmAlarmTable,
       "cpmAlarmTableEntry": cpmAlarmTableEntry,
       "cpmAlarmTableTrapGenNum": cpmAlarmTableTrapGenNum,
       "cpmAlarmTableTrapType": cpmAlarmTableTrapType,
       "cpmAlarmTableTrapSeverity": cpmAlarmTableTrapSeverity,
       "cpmAlarmTableTrapTimeTicks": cpmAlarmTableTrapTimeTicks,
       "cpmAlarmTableTrapArg1": cpmAlarmTableTrapArg1,
       "cpmAlarmTableTrapArg2": cpmAlarmTableTrapArg2,
       "cpmAlarmTableTrapArg3": cpmAlarmTableTrapArg3}
)
