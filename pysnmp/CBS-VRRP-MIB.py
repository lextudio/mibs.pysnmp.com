# SNMP MIB module (CBS-VRRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CBS-VRRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:49 2024
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

(ModuleState,
 cbsHwModuleID,
 cbsTrapSeverity) = mibBuilder.importSymbols(
    "CBS-HARDWARE-MIB",
    "ModuleState",
    "cbsHwModuleID",
    "cbsTrapSeverity")

(cbsVgVapGroupID,
 cbsVgVapGroupName) = mibBuilder.importSymbols(
    "CBS-VAPGROUP-MIB",
    "cbsVgVapGroupID",
    "cbsVgVapGroupName")

(cbsMIBs,
 cbsMgmt,
 cbsTraps) = mibBuilder.importSymbols(
    "CROSSBEAM-SYSTEMS-MIB",
    "cbsMIBs",
    "cbsMgmt",
    "cbsTraps")

(KBytes,
 ProductID) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "KBytes",
    "ProductID")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cbsVrrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 3, 5)
)
cbsVrrpMIB.setRevisions(
        ("2005-08-30 00:00",
         "2010-07-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FailGroupStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("backup", 2),
          ("down", 3),
          ("init", 0),
          ("master", 1))
    )



class RemoteBoxPathStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("active", 3),
          ("down", 0),
          ("secondary", 1),
          ("standby", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CbsVrrp_ObjectIdentity = ObjectIdentity
cbsVrrp = _CbsVrrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5)
)
_CbsVrrpOperations_ObjectIdentity = ObjectIdentity
cbsVrrpOperations = _CbsVrrpOperations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 1)
)


class _CbsVrrpTrapNewMasterReason_Type(Integer32):
    """Custom type cbsVrrpTrapNewMasterReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("masterNoResponse", 2),
          ("preempted", 1),
          ("priority", 0))
    )


_CbsVrrpTrapNewMasterReason_Type.__name__ = "Integer32"
_CbsVrrpTrapNewMasterReason_Object = MibScalar
cbsVrrpTrapNewMasterReason = _CbsVrrpTrapNewMasterReason_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 1, 1),
    _CbsVrrpTrapNewMasterReason_Type()
)
cbsVrrpTrapNewMasterReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cbsVrrpTrapNewMasterReason.setStatus("current")
_CbsVrrpTrapNewMasterFailGrName_Type = DisplayString
_CbsVrrpTrapNewMasterFailGrName_Object = MibScalar
cbsVrrpTrapNewMasterFailGrName = _CbsVrrpTrapNewMasterFailGrName_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 1, 2),
    _CbsVrrpTrapNewMasterFailGrName_Type()
)
cbsVrrpTrapNewMasterFailGrName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cbsVrrpTrapNewMasterFailGrName.setStatus("current")
_CbsVrrpTrapNewMasterVrId_Type = Integer32
_CbsVrrpTrapNewMasterVrId_Object = MibScalar
cbsVrrpTrapNewMasterVrId = _CbsVrrpTrapNewMasterVrId_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 1, 3),
    _CbsVrrpTrapNewMasterVrId_Type()
)
cbsVrrpTrapNewMasterVrId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cbsVrrpTrapNewMasterVrId.setStatus("current")
_CbsVrrpTrapNewMasterCirId_Type = Integer32
_CbsVrrpTrapNewMasterCirId_Object = MibScalar
cbsVrrpTrapNewMasterCirId = _CbsVrrpTrapNewMasterCirId_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 1, 4),
    _CbsVrrpTrapNewMasterCirId_Type()
)
cbsVrrpTrapNewMasterCirId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cbsVrrpTrapNewMasterCirId.setStatus("current")
_CbsVrrpTrapNewMasterCirName_Type = DisplayString
_CbsVrrpTrapNewMasterCirName_Object = MibScalar
cbsVrrpTrapNewMasterCirName = _CbsVrrpTrapNewMasterCirName_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 1, 5),
    _CbsVrrpTrapNewMasterCirName_Type()
)
cbsVrrpTrapNewMasterCirName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cbsVrrpTrapNewMasterCirName.setStatus("current")


class _CbsVrrpTrapProtoErrReason_Type(Integer32):
    """Custom type cbsVrrpTrapProtoErrReason based on Integer32"""
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
        *(("checksumError", 2),
          ("hopLimitError", 0),
          ("versionError", 1),
          ("vridError", 3))
    )


_CbsVrrpTrapProtoErrReason_Type.__name__ = "Integer32"
_CbsVrrpTrapProtoErrReason_Object = MibScalar
cbsVrrpTrapProtoErrReason = _CbsVrrpTrapProtoErrReason_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 1, 6),
    _CbsVrrpTrapProtoErrReason_Type()
)
cbsVrrpTrapProtoErrReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cbsVrrpTrapProtoErrReason.setStatus("current")
_CbsVrrpTrapFailGrOldStatus_Type = FailGroupStatus
_CbsVrrpTrapFailGrOldStatus_Object = MibScalar
cbsVrrpTrapFailGrOldStatus = _CbsVrrpTrapFailGrOldStatus_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 1, 7),
    _CbsVrrpTrapFailGrOldStatus_Type()
)
cbsVrrpTrapFailGrOldStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVrrpTrapFailGrOldStatus.setStatus("current")
_CbsVrrpTrapFailGrNewStatus_Type = FailGroupStatus
_CbsVrrpTrapFailGrNewStatus_Object = MibScalar
cbsVrrpTrapFailGrNewStatus = _CbsVrrpTrapFailGrNewStatus_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 1, 8),
    _CbsVrrpTrapFailGrNewStatus_Type()
)
cbsVrrpTrapFailGrNewStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVrrpTrapFailGrNewStatus.setStatus("current")
_CbsVrrpTrapFailGrStatusChgReason_Type = DisplayString
_CbsVrrpTrapFailGrStatusChgReason_Object = MibScalar
cbsVrrpTrapFailGrStatusChgReason = _CbsVrrpTrapFailGrStatusChgReason_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 1, 9),
    _CbsVrrpTrapFailGrStatusChgReason_Type()
)
cbsVrrpTrapFailGrStatusChgReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVrrpTrapFailGrStatusChgReason.setStatus("current")


class _CbsVrrpTrapFailGrOldPriority_Type(Integer32):
    """Custom type cbsVrrpTrapFailGrOldPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CbsVrrpTrapFailGrOldPriority_Type.__name__ = "Integer32"
_CbsVrrpTrapFailGrOldPriority_Object = MibScalar
cbsVrrpTrapFailGrOldPriority = _CbsVrrpTrapFailGrOldPriority_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 1, 10),
    _CbsVrrpTrapFailGrOldPriority_Type()
)
cbsVrrpTrapFailGrOldPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVrrpTrapFailGrOldPriority.setStatus("current")


class _CbsVrrpTrapFailGrNewPriority_Type(Integer32):
    """Custom type cbsVrrpTrapFailGrNewPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CbsVrrpTrapFailGrNewPriority_Type.__name__ = "Integer32"
_CbsVrrpTrapFailGrNewPriority_Object = MibScalar
cbsVrrpTrapFailGrNewPriority = _CbsVrrpTrapFailGrNewPriority_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 1, 11),
    _CbsVrrpTrapFailGrNewPriority_Type()
)
cbsVrrpTrapFailGrNewPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVrrpTrapFailGrNewPriority.setStatus("current")


class _CbsVrrpTrapFailGrPriorityChgReason_Type(Integer32):
    """Custom type cbsVrrpTrapFailGrPriorityChgReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("activeVapThreshold", 8),
          ("configured", 0),
          ("monitorCircuit", 5),
          ("monitorGroupInterface", 7),
          ("monitorInterface", 6),
          ("verifyNextHop", 4),
          ("virturRouter", 3),
          ("vrDown", 1),
          ("vrUp", 2))
    )


_CbsVrrpTrapFailGrPriorityChgReason_Type.__name__ = "Integer32"
_CbsVrrpTrapFailGrPriorityChgReason_Object = MibScalar
cbsVrrpTrapFailGrPriorityChgReason = _CbsVrrpTrapFailGrPriorityChgReason_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 1, 12),
    _CbsVrrpTrapFailGrPriorityChgReason_Type()
)
cbsVrrpTrapFailGrPriorityChgReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cbsVrrpTrapFailGrPriorityChgReason.setStatus("current")
_CbsVrrpTrapRemoteBoxPathOldStatus_Type = RemoteBoxPathStatus
_CbsVrrpTrapRemoteBoxPathOldStatus_Object = MibScalar
cbsVrrpTrapRemoteBoxPathOldStatus = _CbsVrrpTrapRemoteBoxPathOldStatus_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 1, 13),
    _CbsVrrpTrapRemoteBoxPathOldStatus_Type()
)
cbsVrrpTrapRemoteBoxPathOldStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cbsVrrpTrapRemoteBoxPathOldStatus.setStatus("current")
_CbsVrrpTrapRemoteBoxPathNewStatus_Type = RemoteBoxPathStatus
_CbsVrrpTrapRemoteBoxPathNewStatus_Object = MibScalar
cbsVrrpTrapRemoteBoxPathNewStatus = _CbsVrrpTrapRemoteBoxPathNewStatus_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 1, 14),
    _CbsVrrpTrapRemoteBoxPathNewStatus_Type()
)
cbsVrrpTrapRemoteBoxPathNewStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cbsVrrpTrapRemoteBoxPathNewStatus.setStatus("current")
_CbsVrrpRemBoxPathAddrs_Type = DisplayString
_CbsVrrpRemBoxPathAddrs_Object = MibScalar
cbsVrrpRemBoxPathAddrs = _CbsVrrpRemBoxPathAddrs_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 1, 15),
    _CbsVrrpRemBoxPathAddrs_Type()
)
cbsVrrpRemBoxPathAddrs.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cbsVrrpRemBoxPathAddrs.setStatus("current")
_CbsVrrpFailGrTable_Object = MibTable
cbsVrrpFailGrTable = _CbsVrrpFailGrTable_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 2)
)
if mibBuilder.loadTexts:
    cbsVrrpFailGrTable.setStatus("current")
_CbsVrrpFailGrEntry_Object = MibTableRow
cbsVrrpFailGrEntry = _CbsVrrpFailGrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 2, 1)
)
cbsVrrpFailGrEntry.setIndexNames(
    (0, "CBS-VRRP-MIB", "cbsVrrpFailGrID"),
)
if mibBuilder.loadTexts:
    cbsVrrpFailGrEntry.setStatus("current")


class _CbsVrrpFailGrID_Type(Integer32):
    """Custom type cbsVrrpFailGrID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CbsVrrpFailGrID_Type.__name__ = "Integer32"
_CbsVrrpFailGrID_Object = MibTableColumn
cbsVrrpFailGrID = _CbsVrrpFailGrID_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 2, 1, 1),
    _CbsVrrpFailGrID_Type()
)
cbsVrrpFailGrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVrrpFailGrID.setStatus("current")
_CbsVrrpFailGrName_Type = DisplayString
_CbsVrrpFailGrName_Object = MibTableColumn
cbsVrrpFailGrName = _CbsVrrpFailGrName_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 2, 1, 2),
    _CbsVrrpFailGrName_Type()
)
cbsVrrpFailGrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVrrpFailGrName.setStatus("current")
_CbsVrrpFailGrStatus_Type = FailGroupStatus
_CbsVrrpFailGrStatus_Object = MibTableColumn
cbsVrrpFailGrStatus = _CbsVrrpFailGrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 2, 1, 3),
    _CbsVrrpFailGrStatus_Type()
)
cbsVrrpFailGrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVrrpFailGrStatus.setStatus("current")


class _CbsVrrpFailGrConfigPriority_Type(Integer32):
    """Custom type cbsVrrpFailGrConfigPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CbsVrrpFailGrConfigPriority_Type.__name__ = "Integer32"
_CbsVrrpFailGrConfigPriority_Object = MibTableColumn
cbsVrrpFailGrConfigPriority = _CbsVrrpFailGrConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 2, 1, 4),
    _CbsVrrpFailGrConfigPriority_Type()
)
cbsVrrpFailGrConfigPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVrrpFailGrConfigPriority.setStatus("current")


class _CbsVrrpFailGrActualPriority_Type(Integer32):
    """Custom type cbsVrrpFailGrActualPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CbsVrrpFailGrActualPriority_Type.__name__ = "Integer32"
_CbsVrrpFailGrActualPriority_Object = MibTableColumn
cbsVrrpFailGrActualPriority = _CbsVrrpFailGrActualPriority_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 2, 1, 5),
    _CbsVrrpFailGrActualPriority_Type()
)
cbsVrrpFailGrActualPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVrrpFailGrActualPriority.setStatus("current")
_CbsVrrpFailGrEnabled_Type = TruthValue
_CbsVrrpFailGrEnabled_Object = MibTableColumn
cbsVrrpFailGrEnabled = _CbsVrrpFailGrEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 2, 1, 6),
    _CbsVrrpFailGrEnabled_Type()
)
cbsVrrpFailGrEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVrrpFailGrEnabled.setStatus("current")
_CbsVrrpFailGrPreemption_Type = TruthValue
_CbsVrrpFailGrPreemption_Object = MibTableColumn
cbsVrrpFailGrPreemption = _CbsVrrpFailGrPreemption_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 2, 1, 7),
    _CbsVrrpFailGrPreemption_Type()
)
cbsVrrpFailGrPreemption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVrrpFailGrPreemption.setStatus("current")
_CbsVrrpFailGrLastChangeTime_Type = TimeTicks
_CbsVrrpFailGrLastChangeTime_Object = MibTableColumn
cbsVrrpFailGrLastChangeTime = _CbsVrrpFailGrLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 2, 1, 8),
    _CbsVrrpFailGrLastChangeTime_Type()
)
cbsVrrpFailGrLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVrrpFailGrLastChangeTime.setStatus("current")
_CbsVrrpFailGrLastChangeReason_Type = DisplayString
_CbsVrrpFailGrLastChangeReason_Object = MibTableColumn
cbsVrrpFailGrLastChangeReason = _CbsVrrpFailGrLastChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 2, 1, 9),
    _CbsVrrpFailGrLastChangeReason_Type()
)
cbsVrrpFailGrLastChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVrrpFailGrLastChangeReason.setStatus("current")


class _CbsVrrpFailGrMasterSysID_Type(Integer32):
    """Custom type cbsVrrpFailGrMasterSysID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CbsVrrpFailGrMasterSysID_Type.__name__ = "Integer32"
_CbsVrrpFailGrMasterSysID_Object = MibTableColumn
cbsVrrpFailGrMasterSysID = _CbsVrrpFailGrMasterSysID_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 2, 1, 10),
    _CbsVrrpFailGrMasterSysID_Type()
)
cbsVrrpFailGrMasterSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVrrpFailGrMasterSysID.setStatus("current")


class _CbsVrrpFailGrMasterPriority_Type(Integer32):
    """Custom type cbsVrrpFailGrMasterPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CbsVrrpFailGrMasterPriority_Type.__name__ = "Integer32"
_CbsVrrpFailGrMasterPriority_Object = MibTableColumn
cbsVrrpFailGrMasterPriority = _CbsVrrpFailGrMasterPriority_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 2, 1, 11),
    _CbsVrrpFailGrMasterPriority_Type()
)
cbsVrrpFailGrMasterPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVrrpFailGrMasterPriority.setStatus("current")
_CbsVrrpFailGrCompTable_Object = MibTable
cbsVrrpFailGrCompTable = _CbsVrrpFailGrCompTable_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 3)
)
if mibBuilder.loadTexts:
    cbsVrrpFailGrCompTable.setStatus("current")
_CbsVrrpFailGrCompEntry_Object = MibTableRow
cbsVrrpFailGrCompEntry = _CbsVrrpFailGrCompEntry_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 3, 1)
)
cbsVrrpFailGrCompEntry.setIndexNames(
    (0, "CBS-VRRP-MIB", "cbsVrrpFailGroupID"),
    (0, "CBS-VRRP-MIB", "cbsVrrpFailGrCompIndex"),
)
if mibBuilder.loadTexts:
    cbsVrrpFailGrCompEntry.setStatus("current")


class _CbsVrrpFailGroupID_Type(Integer32):
    """Custom type cbsVrrpFailGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CbsVrrpFailGroupID_Type.__name__ = "Integer32"
_CbsVrrpFailGroupID_Object = MibTableColumn
cbsVrrpFailGroupID = _CbsVrrpFailGroupID_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 3, 1, 1),
    _CbsVrrpFailGroupID_Type()
)
cbsVrrpFailGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVrrpFailGroupID.setStatus("current")
_CbsVrrpFailGroupName_Type = DisplayString
_CbsVrrpFailGroupName_Object = MibTableColumn
cbsVrrpFailGroupName = _CbsVrrpFailGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 3, 1, 2),
    _CbsVrrpFailGroupName_Type()
)
cbsVrrpFailGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVrrpFailGroupName.setStatus("current")


class _CbsVrrpFailGrCompIndex_Type(Integer32):
    """Custom type cbsVrrpFailGrCompIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CbsVrrpFailGrCompIndex_Type.__name__ = "Integer32"
_CbsVrrpFailGrCompIndex_Object = MibTableColumn
cbsVrrpFailGrCompIndex = _CbsVrrpFailGrCompIndex_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 3, 1, 3),
    _CbsVrrpFailGrCompIndex_Type()
)
cbsVrrpFailGrCompIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVrrpFailGrCompIndex.setStatus("current")


class _CbsVrrpFailGrCompType_Type(Integer32):
    """Custom type cbsVrrpFailGrCompType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("mc", 1),
          ("mg", 3),
          ("mi", 2),
          ("nh", 5),
          ("vg", 4),
          ("vr", 0))
    )


_CbsVrrpFailGrCompType_Type.__name__ = "Integer32"
_CbsVrrpFailGrCompType_Object = MibTableColumn
cbsVrrpFailGrCompType = _CbsVrrpFailGrCompType_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 3, 1, 4),
    _CbsVrrpFailGrCompType_Type()
)
cbsVrrpFailGrCompType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVrrpFailGrCompType.setStatus("current")
_CbsVrrpFailGrCompDescr_Type = DisplayString
_CbsVrrpFailGrCompDescr_Object = MibTableColumn
cbsVrrpFailGrCompDescr = _CbsVrrpFailGrCompDescr_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 3, 1, 5),
    _CbsVrrpFailGrCompDescr_Type()
)
cbsVrrpFailGrCompDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVrrpFailGrCompDescr.setStatus("current")
_CbsVrrpFailGrCompDelta_Type = DisplayString
_CbsVrrpFailGrCompDelta_Object = MibTableColumn
cbsVrrpFailGrCompDelta = _CbsVrrpFailGrCompDelta_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 3, 1, 6),
    _CbsVrrpFailGrCompDelta_Type()
)
cbsVrrpFailGrCompDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVrrpFailGrCompDelta.setStatus("current")
_CbsVrrpRemoteBoxPathTable_Object = MibTable
cbsVrrpRemoteBoxPathTable = _CbsVrrpRemoteBoxPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 4)
)
if mibBuilder.loadTexts:
    cbsVrrpRemoteBoxPathTable.setStatus("current")
_CbsVrrpRemoteBoxPathEntry_Object = MibTableRow
cbsVrrpRemoteBoxPathEntry = _CbsVrrpRemoteBoxPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 4, 1)
)
cbsVrrpRemoteBoxPathEntry.setIndexNames(
    (0, "CBS-VRRP-MIB", "cbsVrrpRemoteBoxID"),
    (0, "CBS-VRRP-MIB", "cbsVrrpRemoteBoxPathIndex"),
)
if mibBuilder.loadTexts:
    cbsVrrpRemoteBoxPathEntry.setStatus("current")


class _CbsVrrpRemoteBoxID_Type(Integer32):
    """Custom type cbsVrrpRemoteBoxID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CbsVrrpRemoteBoxID_Type.__name__ = "Integer32"
_CbsVrrpRemoteBoxID_Object = MibTableColumn
cbsVrrpRemoteBoxID = _CbsVrrpRemoteBoxID_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 4, 1, 1),
    _CbsVrrpRemoteBoxID_Type()
)
cbsVrrpRemoteBoxID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVrrpRemoteBoxID.setStatus("current")


class _CbsVrrpRemoteBoxPathIndex_Type(Integer32):
    """Custom type cbsVrrpRemoteBoxPathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_CbsVrrpRemoteBoxPathIndex_Type.__name__ = "Integer32"
_CbsVrrpRemoteBoxPathIndex_Object = MibTableColumn
cbsVrrpRemoteBoxPathIndex = _CbsVrrpRemoteBoxPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 4, 1, 2),
    _CbsVrrpRemoteBoxPathIndex_Type()
)
cbsVrrpRemoteBoxPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVrrpRemoteBoxPathIndex.setStatus("current")
_CbsVrrpRemoteBoxPathAddr_Type = IpAddress
_CbsVrrpRemoteBoxPathAddr_Object = MibTableColumn
cbsVrrpRemoteBoxPathAddr = _CbsVrrpRemoteBoxPathAddr_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 4, 1, 3),
    _CbsVrrpRemoteBoxPathAddr_Type()
)
cbsVrrpRemoteBoxPathAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVrrpRemoteBoxPathAddr.setStatus("current")
_CbsVrrpRemoteBoxPathLocalIntf_Type = DisplayString
_CbsVrrpRemoteBoxPathLocalIntf_Object = MibTableColumn
cbsVrrpRemoteBoxPathLocalIntf = _CbsVrrpRemoteBoxPathLocalIntf_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 4, 1, 4),
    _CbsVrrpRemoteBoxPathLocalIntf_Type()
)
cbsVrrpRemoteBoxPathLocalIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVrrpRemoteBoxPathLocalIntf.setStatus("current")
_CbsVrrpRemoteBoxPathLocalAddr_Type = IpAddress
_CbsVrrpRemoteBoxPathLocalAddr_Object = MibTableColumn
cbsVrrpRemoteBoxPathLocalAddr = _CbsVrrpRemoteBoxPathLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 4, 1, 5),
    _CbsVrrpRemoteBoxPathLocalAddr_Type()
)
cbsVrrpRemoteBoxPathLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVrrpRemoteBoxPathLocalAddr.setStatus("current")
_CbsVrrpRemoteBoxPathStatus_Type = RemoteBoxPathStatus
_CbsVrrpRemoteBoxPathStatus_Object = MibTableColumn
cbsVrrpRemoteBoxPathStatus = _CbsVrrpRemoteBoxPathStatus_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 4, 1, 6),
    _CbsVrrpRemoteBoxPathStatus_Type()
)
cbsVrrpRemoteBoxPathStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVrrpRemoteBoxPathStatus.setStatus("current")
_CbsVrrpRemoteBoxPathLastChangeTime_Type = TimeTicks
_CbsVrrpRemoteBoxPathLastChangeTime_Object = MibTableColumn
cbsVrrpRemoteBoxPathLastChangeTime = _CbsVrrpRemoteBoxPathLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 4, 1, 7),
    _CbsVrrpRemoteBoxPathLastChangeTime_Type()
)
cbsVrrpRemoteBoxPathLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVrrpRemoteBoxPathLastChangeTime.setStatus("current")


class _CbsVrrpRemoteBoxPathLinkQuality_Type(Gauge32):
    """Custom type cbsVrrpRemoteBoxPathLinkQuality based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CbsVrrpRemoteBoxPathLinkQuality_Type.__name__ = "Gauge32"
_CbsVrrpRemoteBoxPathLinkQuality_Object = MibTableColumn
cbsVrrpRemoteBoxPathLinkQuality = _CbsVrrpRemoteBoxPathLinkQuality_Object(
    (1, 3, 6, 1, 4, 1, 6848, 2, 5, 4, 1, 8),
    _CbsVrrpRemoteBoxPathLinkQuality_Type()
)
cbsVrrpRemoteBoxPathLinkQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbsVrrpRemoteBoxPathLinkQuality.setStatus("current")
_CbsVrrpTraps_ObjectIdentity = ObjectIdentity
cbsVrrpTraps = _CbsVrrpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6848, 4, 4)
)

# Managed Objects groups


# Notification objects

cbsVrrpTrapNewMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 4, 1)
)
cbsVrrpTrapNewMaster.setObjects(
      *(("CBS-VRRP-MIB", "cbsVrrpTrapNewMasterFailGrName"),
        ("CBS-VRRP-MIB", "cbsVrrpTrapNewMasterVrId"),
        ("CBS-VRRP-MIB", "cbsVrrpTrapNewMasterCirId"),
        ("CBS-VRRP-MIB", "cbsVrrpTrapNewMasterCirName"),
        ("CBS-VRRP-MIB", "cbsVrrpTrapNewMasterReason"))
)
if mibBuilder.loadTexts:
    cbsVrrpTrapNewMaster.setStatus(
        "current"
    )

cbsVrrpTrapProtoError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 4, 2)
)
cbsVrrpTrapProtoError.setObjects(
    ("CBS-VRRP-MIB", "cbsVrrpTrapProtoErrReason")
)
if mibBuilder.loadTexts:
    cbsVrrpTrapProtoError.setStatus(
        "current"
    )

cbsVrrpTrapFailGrStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 4, 3)
)
cbsVrrpTrapFailGrStatusChanged.setObjects(
      *(("CBS-VRRP-MIB", "cbsVrrpFailGrID"),
        ("CBS-VRRP-MIB", "cbsVrrpFailGrName"),
        ("CBS-VRRP-MIB", "cbsVrrpTrapFailGrOldStatus"),
        ("CBS-VRRP-MIB", "cbsVrrpTrapFailGrNewStatus"),
        ("CBS-VRRP-MIB", "cbsVrrpTrapFailGrStatusChgReason"),
        ("CBS-HARDWARE-MIB", "cbsTrapSeverity"))
)
if mibBuilder.loadTexts:
    cbsVrrpTrapFailGrStatusChanged.setStatus(
        "current"
    )

cbsVrrpTrapFailGrPriorityChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 4, 4)
)
cbsVrrpTrapFailGrPriorityChanged.setObjects(
      *(("CBS-VRRP-MIB", "cbsVrrpFailGrID"),
        ("CBS-VRRP-MIB", "cbsVrrpFailGrName"),
        ("CBS-VRRP-MIB", "cbsVrrpTrapFailGrOldPriority"),
        ("CBS-VRRP-MIB", "cbsVrrpTrapFailGrNewPriority"),
        ("CBS-VRRP-MIB", "cbsVrrpTrapFailGrPriorityChgReason"),
        ("CBS-HARDWARE-MIB", "cbsTrapSeverity"))
)
if mibBuilder.loadTexts:
    cbsVrrpTrapFailGrPriorityChanged.setStatus(
        "current"
    )

cbsVrrpTrapRemoteBoxPathStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 4, 5)
)
cbsVrrpTrapRemoteBoxPathStatusChanged.setObjects(
      *(("CBS-VRRP-MIB", "cbsVrrpRemoteBoxID"),
        ("CBS-VRRP-MIB", "cbsVrrpRemoteBoxPathAddr"),
        ("CBS-VRRP-MIB", "cbsVrrpRemoteBoxPathLocalIntf"),
        ("CBS-VRRP-MIB", "cbsVrrpRemoteBoxPathLocalAddr"),
        ("CBS-VRRP-MIB", "cbsVrrpTrapRemoteBoxPathOldStatus"),
        ("CBS-VRRP-MIB", "cbsVrrpTrapRemoteBoxPathNewStatus"),
        ("CBS-HARDWARE-MIB", "cbsTrapSeverity"))
)
if mibBuilder.loadTexts:
    cbsVrrpTrapRemoteBoxPathStatusChanged.setStatus(
        "current"
    )

cbsVrrpTrapRemoteBoxNoActivePath = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 4, 6)
)
cbsVrrpTrapRemoteBoxNoActivePath.setObjects(
      *(("CBS-VRRP-MIB", "cbsVrrpRemoteBoxID"),
        ("CBS-HARDWARE-MIB", "cbsTrapSeverity"))
)
if mibBuilder.loadTexts:
    cbsVrrpTrapRemoteBoxNoActivePath.setStatus(
        "current"
    )

cbsVrrpTrapRemoteBoxNoSecondaryPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 4, 7)
)
cbsVrrpTrapRemoteBoxNoSecondaryPath.setObjects(
      *(("CBS-VRRP-MIB", "cbsVrrpRemoteBoxID"),
        ("CBS-HARDWARE-MIB", "cbsTrapSeverity"))
)
if mibBuilder.loadTexts:
    cbsVrrpTrapRemoteBoxNoSecondaryPath.setStatus(
        "current"
    )

cbsVrrpTrapRemoteBoxNoStandbyPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 4, 8)
)
cbsVrrpTrapRemoteBoxNoStandbyPath.setObjects(
      *(("CBS-VRRP-MIB", "cbsVrrpRemoteBoxID"),
        ("CBS-HARDWARE-MIB", "cbsTrapSeverity"))
)
if mibBuilder.loadTexts:
    cbsVrrpTrapRemoteBoxNoStandbyPath.setStatus(
        "current"
    )

cbsVrrpTrapRemoteBoxPathSharedIntf = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 4, 9)
)
cbsVrrpTrapRemoteBoxPathSharedIntf.setObjects(
      *(("CBS-VRRP-MIB", "cbsVrrpRemoteBoxID"),
        ("CBS-VRRP-MIB", "cbsVrrpRemBoxPathAddrs"),
        ("CBS-VRRP-MIB", "cbsVrrpRemoteBoxPathLocalIntf"),
        ("CBS-HARDWARE-MIB", "cbsTrapSeverity"))
)
if mibBuilder.loadTexts:
    cbsVrrpTrapRemoteBoxPathSharedIntf.setStatus(
        "current"
    )

cbsVrrpTrapNoRemoteBoxConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 4, 10)
)
cbsVrrpTrapNoRemoteBoxConfigured.setObjects(
      *(("CBS-HARDWARE-MIB", "cbsHwModuleID"),
        ("CBS-HARDWARE-MIB", "cbsTrapSeverity"))
)
if mibBuilder.loadTexts:
    cbsVrrpTrapNoRemoteBoxConfigured.setStatus(
        "current"
    )

cbsVrrpTrapOnlyOnePathDefined = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 4, 11)
)
cbsVrrpTrapOnlyOnePathDefined.setObjects(
      *(("CBS-VRRP-MIB", "cbsVrrpRemoteBoxID"),
        ("CBS-HARDWARE-MIB", "cbsTrapSeverity"))
)
if mibBuilder.loadTexts:
    cbsVrrpTrapOnlyOnePathDefined.setStatus(
        "current"
    )

cbsVrrpTrapRemoteBoxRunLegacyXOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 6848, 4, 4, 12)
)
cbsVrrpTrapRemoteBoxRunLegacyXOS.setObjects(
      *(("CBS-VRRP-MIB", "cbsVrrpRemoteBoxID"),
        ("CBS-HARDWARE-MIB", "cbsTrapSeverity"))
)
if mibBuilder.loadTexts:
    cbsVrrpTrapRemoteBoxRunLegacyXOS.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CBS-VRRP-MIB",
    **{"FailGroupStatus": FailGroupStatus,
       "RemoteBoxPathStatus": RemoteBoxPathStatus,
       "cbsVrrp": cbsVrrp,
       "cbsVrrpOperations": cbsVrrpOperations,
       "cbsVrrpTrapNewMasterReason": cbsVrrpTrapNewMasterReason,
       "cbsVrrpTrapNewMasterFailGrName": cbsVrrpTrapNewMasterFailGrName,
       "cbsVrrpTrapNewMasterVrId": cbsVrrpTrapNewMasterVrId,
       "cbsVrrpTrapNewMasterCirId": cbsVrrpTrapNewMasterCirId,
       "cbsVrrpTrapNewMasterCirName": cbsVrrpTrapNewMasterCirName,
       "cbsVrrpTrapProtoErrReason": cbsVrrpTrapProtoErrReason,
       "cbsVrrpTrapFailGrOldStatus": cbsVrrpTrapFailGrOldStatus,
       "cbsVrrpTrapFailGrNewStatus": cbsVrrpTrapFailGrNewStatus,
       "cbsVrrpTrapFailGrStatusChgReason": cbsVrrpTrapFailGrStatusChgReason,
       "cbsVrrpTrapFailGrOldPriority": cbsVrrpTrapFailGrOldPriority,
       "cbsVrrpTrapFailGrNewPriority": cbsVrrpTrapFailGrNewPriority,
       "cbsVrrpTrapFailGrPriorityChgReason": cbsVrrpTrapFailGrPriorityChgReason,
       "cbsVrrpTrapRemoteBoxPathOldStatus": cbsVrrpTrapRemoteBoxPathOldStatus,
       "cbsVrrpTrapRemoteBoxPathNewStatus": cbsVrrpTrapRemoteBoxPathNewStatus,
       "cbsVrrpRemBoxPathAddrs": cbsVrrpRemBoxPathAddrs,
       "cbsVrrpFailGrTable": cbsVrrpFailGrTable,
       "cbsVrrpFailGrEntry": cbsVrrpFailGrEntry,
       "cbsVrrpFailGrID": cbsVrrpFailGrID,
       "cbsVrrpFailGrName": cbsVrrpFailGrName,
       "cbsVrrpFailGrStatus": cbsVrrpFailGrStatus,
       "cbsVrrpFailGrConfigPriority": cbsVrrpFailGrConfigPriority,
       "cbsVrrpFailGrActualPriority": cbsVrrpFailGrActualPriority,
       "cbsVrrpFailGrEnabled": cbsVrrpFailGrEnabled,
       "cbsVrrpFailGrPreemption": cbsVrrpFailGrPreemption,
       "cbsVrrpFailGrLastChangeTime": cbsVrrpFailGrLastChangeTime,
       "cbsVrrpFailGrLastChangeReason": cbsVrrpFailGrLastChangeReason,
       "cbsVrrpFailGrMasterSysID": cbsVrrpFailGrMasterSysID,
       "cbsVrrpFailGrMasterPriority": cbsVrrpFailGrMasterPriority,
       "cbsVrrpFailGrCompTable": cbsVrrpFailGrCompTable,
       "cbsVrrpFailGrCompEntry": cbsVrrpFailGrCompEntry,
       "cbsVrrpFailGroupID": cbsVrrpFailGroupID,
       "cbsVrrpFailGroupName": cbsVrrpFailGroupName,
       "cbsVrrpFailGrCompIndex": cbsVrrpFailGrCompIndex,
       "cbsVrrpFailGrCompType": cbsVrrpFailGrCompType,
       "cbsVrrpFailGrCompDescr": cbsVrrpFailGrCompDescr,
       "cbsVrrpFailGrCompDelta": cbsVrrpFailGrCompDelta,
       "cbsVrrpRemoteBoxPathTable": cbsVrrpRemoteBoxPathTable,
       "cbsVrrpRemoteBoxPathEntry": cbsVrrpRemoteBoxPathEntry,
       "cbsVrrpRemoteBoxID": cbsVrrpRemoteBoxID,
       "cbsVrrpRemoteBoxPathIndex": cbsVrrpRemoteBoxPathIndex,
       "cbsVrrpRemoteBoxPathAddr": cbsVrrpRemoteBoxPathAddr,
       "cbsVrrpRemoteBoxPathLocalIntf": cbsVrrpRemoteBoxPathLocalIntf,
       "cbsVrrpRemoteBoxPathLocalAddr": cbsVrrpRemoteBoxPathLocalAddr,
       "cbsVrrpRemoteBoxPathStatus": cbsVrrpRemoteBoxPathStatus,
       "cbsVrrpRemoteBoxPathLastChangeTime": cbsVrrpRemoteBoxPathLastChangeTime,
       "cbsVrrpRemoteBoxPathLinkQuality": cbsVrrpRemoteBoxPathLinkQuality,
       "cbsVrrpMIB": cbsVrrpMIB,
       "cbsVrrpTraps": cbsVrrpTraps,
       "cbsVrrpTrapNewMaster": cbsVrrpTrapNewMaster,
       "cbsVrrpTrapProtoError": cbsVrrpTrapProtoError,
       "cbsVrrpTrapFailGrStatusChanged": cbsVrrpTrapFailGrStatusChanged,
       "cbsVrrpTrapFailGrPriorityChanged": cbsVrrpTrapFailGrPriorityChanged,
       "cbsVrrpTrapRemoteBoxPathStatusChanged": cbsVrrpTrapRemoteBoxPathStatusChanged,
       "cbsVrrpTrapRemoteBoxNoActivePath": cbsVrrpTrapRemoteBoxNoActivePath,
       "cbsVrrpTrapRemoteBoxNoSecondaryPath": cbsVrrpTrapRemoteBoxNoSecondaryPath,
       "cbsVrrpTrapRemoteBoxNoStandbyPath": cbsVrrpTrapRemoteBoxNoStandbyPath,
       "cbsVrrpTrapRemoteBoxPathSharedIntf": cbsVrrpTrapRemoteBoxPathSharedIntf,
       "cbsVrrpTrapNoRemoteBoxConfigured": cbsVrrpTrapNoRemoteBoxConfigured,
       "cbsVrrpTrapOnlyOnePathDefined": cbsVrrpTrapOnlyOnePathDefined,
       "cbsVrrpTrapRemoteBoxRunLegacyXOS": cbsVrrpTrapRemoteBoxRunLegacyXOS}
)
