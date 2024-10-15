# SNMP MIB module (UTM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/UTM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:12 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sni_ObjectIdentity = ObjectIdentity
sni = _Sni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231)
)
_SniProductMibs_ObjectIdentity = ObjectIdentity
sniProductMibs = _SniProductMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2)
)
_SniUTM_ObjectIdentity = ObjectIdentity
sniUTM = _SniUTM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 19)
)
_UtmApplTabNum_Type = Integer32
_UtmApplTabNum_Object = MibScalar
utmApplTabNum = _UtmApplTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 1),
    _UtmApplTabNum_Type()
)
utmApplTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmApplTabNum.setStatus("mandatory")
_UtmApplTable_Object = MibTable
utmApplTable = _UtmApplTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 2)
)
if mibBuilder.loadTexts:
    utmApplTable.setStatus("mandatory")
_UtmApplEntry_Object = MibTableRow
utmApplEntry = _UtmApplEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 2, 1)
)
utmApplEntry.setIndexNames(
    (0, "UTM-MIB", "utmApplIndex"),
)
if mibBuilder.loadTexts:
    utmApplEntry.setStatus("mandatory")
_UtmApplIndex_Type = Integer32
_UtmApplIndex_Object = MibTableColumn
utmApplIndex = _UtmApplIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 2, 1, 1),
    _UtmApplIndex_Type()
)
utmApplIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmApplIndex.setStatus("mandatory")
_UtmApplName_Type = DisplayString
_UtmApplName_Object = MibTableColumn
utmApplName = _UtmApplName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 2, 1, 2),
    _UtmApplName_Type()
)
utmApplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmApplName.setStatus("mandatory")


class _UtmApplStatus_Type(Integer32):
    """Custom type utmApplStatus based on Integer32"""
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


_UtmApplStatus_Type.__name__ = "Integer32"
_UtmApplStatus_Object = MibTableColumn
utmApplStatus = _UtmApplStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 2, 1, 3),
    _UtmApplStatus_Type()
)
utmApplStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmApplStatus.setStatus("mandatory")
_UtmApplSharedMemKey_Type = Gauge32
_UtmApplSharedMemKey_Object = MibTableColumn
utmApplSharedMemKey = _UtmApplSharedMemKey_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 2, 1, 4),
    _UtmApplSharedMemKey_Type()
)
utmApplSharedMemKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmApplSharedMemKey.setStatus("mandatory")
_UtmApplSharedMemSegSize_Type = Gauge32
_UtmApplSharedMemSegSize_Object = MibTableColumn
utmApplSharedMemSegSize = _UtmApplSharedMemSegSize_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 2, 1, 5),
    _UtmApplSharedMemSegSize_Type()
)
utmApplSharedMemSegSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmApplSharedMemSegSize.setStatus("mandatory")
_UtmApplSemId_Type = Gauge32
_UtmApplSemId_Object = MibTableColumn
utmApplSemId = _UtmApplSemId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 2, 1, 6),
    _UtmApplSemId_Type()
)
utmApplSemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmApplSemId.setStatus("mandatory")
_UtmApplHomeDir_Type = DisplayString
_UtmApplHomeDir_Object = MibTableColumn
utmApplHomeDir = _UtmApplHomeDir_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 2, 1, 7),
    _UtmApplHomeDir_Type()
)
utmApplHomeDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmApplHomeDir.setStatus("mandatory")
_UtmApplicationData_ObjectIdentity = ObjectIdentity
utmApplicationData = _UtmApplicationData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3)
)
_UtmMainData_ObjectIdentity = ObjectIdentity
utmMainData = _UtmMainData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 1)
)
_UtmMainApplName_Type = DisplayString
_UtmMainApplName_Object = MibScalar
utmMainApplName = _UtmMainApplName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 1, 1),
    _UtmMainApplName_Type()
)
utmMainApplName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmMainApplName.setStatus("mandatory")
_UtmMainBCAMAppl_Type = DisplayString
_UtmMainBCAMAppl_Object = MibScalar
utmMainBCAMAppl = _UtmMainBCAMAppl_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 1, 2),
    _UtmMainBCAMAppl_Type()
)
utmMainBCAMAppl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmMainBCAMAppl.setStatus("mandatory")
_UtmMainUTMversion_Type = DisplayString
_UtmMainUTMversion_Object = MibScalar
utmMainUTMversion = _UtmMainUTMversion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 1, 3),
    _UtmMainUTMversion_Type()
)
utmMainUTMversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmMainUTMversion.setStatus("mandatory")


class _UtmMainApplStartStop_Type(Integer32):
    """Custom type utmMainApplStartStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2),
          ("undefined", 255))
    )


_UtmMainApplStartStop_Type.__name__ = "Integer32"
_UtmMainApplStartStop_Object = MibScalar
utmMainApplStartStop = _UtmMainApplStartStop_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 1, 4),
    _UtmMainApplStartStop_Type()
)
utmMainApplStartStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmMainApplStartStop.setStatus("mandatory")
_UtmMainApplHomeDir_Type = DisplayString
_UtmMainApplHomeDir_Object = MibScalar
utmMainApplHomeDir = _UtmMainApplHomeDir_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 1, 5),
    _UtmMainApplHomeDir_Type()
)
utmMainApplHomeDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmMainApplHomeDir.setStatus("mandatory")
_UtmMainSubagentVersion_Type = DisplayString
_UtmMainSubagentVersion_Object = MibScalar
utmMainSubagentVersion = _UtmMainSubagentVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 1, 6),
    _UtmMainSubagentVersion_Type()
)
utmMainSubagentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmMainSubagentVersion.setStatus("mandatory")
_UtmStatData_ObjectIdentity = ObjectIdentity
utmStatData = _UtmStatData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 2)
)
_UtmStatStartDateAndTime_Type = DateAndTime
_UtmStatStartDateAndTime_Object = MibScalar
utmStatStartDateAndTime = _UtmStatStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 2, 1),
    _UtmStatStartDateAndTime_Type()
)
utmStatStartDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmStatStartDateAndTime.setStatus("mandatory")
_UtmStatStartDateAndTimeString_Type = DisplayString
_UtmStatStartDateAndTimeString_Object = MibScalar
utmStatStartDateAndTimeString = _UtmStatStartDateAndTimeString_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 2, 2),
    _UtmStatStartDateAndTimeString_Type()
)
utmStatStartDateAndTimeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmStatStartDateAndTimeString.setStatus("mandatory")
_UtmStatTermInMsgs_Type = Integer32
_UtmStatTermInMsgs_Object = MibScalar
utmStatTermInMsgs = _UtmStatTermInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 2, 3),
    _UtmStatTermInMsgs_Type()
)
utmStatTermInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmStatTermInMsgs.setStatus("mandatory")
_UtmStatTermOutMsgs_Type = Integer32
_UtmStatTermOutMsgs_Object = MibScalar
utmStatTermOutMsgs = _UtmStatTermOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 2, 4),
    _UtmStatTermOutMsgs_Type()
)
utmStatTermOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmStatTermOutMsgs.setStatus("mandatory")
_UtmStatCurrTasks_Type = Integer32
_UtmStatCurrTasks_Object = MibScalar
utmStatCurrTasks = _UtmStatCurrTasks_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 2, 5),
    _UtmStatCurrTasks_Type()
)
utmStatCurrTasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmStatCurrTasks.setStatus("mandatory")
_UtmStatConnUsers_Type = Integer32
_UtmStatConnUsers_Object = MibScalar
utmStatConnUsers = _UtmStatConnUsers_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 2, 6),
    _UtmStatConnUsers_Type()
)
utmStatConnUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmStatConnUsers.setStatus("mandatory")
_UtmStatOpenDialConv_Type = Integer32
_UtmStatOpenDialConv_Object = MibScalar
utmStatOpenDialConv = _UtmStatOpenDialConv_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 2, 7),
    _UtmStatOpenDialConv_Type()
)
utmStatOpenDialConv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmStatOpenDialConv.setStatus("mandatory")
_UtmStatOpenAsynConv_Type = Integer32
_UtmStatOpenAsynConv_Object = MibScalar
utmStatOpenAsynConv = _UtmStatOpenAsynConv_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 2, 8),
    _UtmStatOpenAsynConv_Type()
)
utmStatOpenAsynConv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmStatOpenAsynConv.setStatus("mandatory")
_UtmStatDialTAperSec_Type = Gauge32
_UtmStatDialTAperSec_Object = MibScalar
utmStatDialTAperSec = _UtmStatDialTAperSec_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 2, 9),
    _UtmStatDialTAperSec_Type()
)
utmStatDialTAperSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmStatDialTAperSec.setStatus("mandatory")
_UtmStatAsynTAperSec_Type = Gauge32
_UtmStatAsynTAperSec_Object = MibScalar
utmStatAsynTAperSec = _UtmStatAsynTAperSec_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 2, 10),
    _UtmStatAsynTAperSec_Type()
)
utmStatAsynTAperSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmStatAsynTAperSec.setStatus("mandatory")
_UtmStatDialStepSec_Type = Gauge32
_UtmStatDialStepSec_Object = MibScalar
utmStatDialStepSec = _UtmStatDialStepSec_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 2, 11),
    _UtmStatDialStepSec_Type()
)
utmStatDialStepSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmStatDialStepSec.setStatus("mandatory")
_UtmStatMaxPoolSize_Type = Gauge32
_UtmStatMaxPoolSize_Object = MibScalar
utmStatMaxPoolSize = _UtmStatMaxPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 2, 12),
    _UtmStatMaxPoolSize_Type()
)
utmStatMaxPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmStatMaxPoolSize.setStatus("mandatory")
_UtmStatActPoolSize_Type = Gauge32
_UtmStatActPoolSize_Object = MibScalar
utmStatActPoolSize = _UtmStatActPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 2, 13),
    _UtmStatActPoolSize_Type()
)
utmStatActPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmStatActPoolSize.setStatus("mandatory")
_UtmStatAvgPoolSize_Type = Gauge32
_UtmStatAvgPoolSize_Object = MibScalar
utmStatAvgPoolSize = _UtmStatAvgPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 2, 14),
    _UtmStatAvgPoolSize_Type()
)
utmStatAvgPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmStatAvgPoolSize.setStatus("mandatory")
_UtmStatCacheHitRate_Type = Gauge32
_UtmStatCacheHitRate_Object = MibScalar
utmStatCacheHitRate = _UtmStatCacheHitRate_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 2, 15),
    _UtmStatCacheHitRate_Type()
)
utmStatCacheHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmStatCacheHitRate.setStatus("mandatory")
_UtmStatCacheWaits_Type = Gauge32
_UtmStatCacheWaits_Object = MibScalar
utmStatCacheWaits = _UtmStatCacheWaits_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 2, 16),
    _UtmStatCacheWaits_Type()
)
utmStatCacheWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmStatCacheWaits.setStatus("mandatory")
_UtmStatUnprocAtacs_Type = Integer32
_UtmStatUnprocAtacs_Object = MibScalar
utmStatUnprocAtacs = _UtmStatUnprocAtacs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 2, 17),
    _UtmStatUnprocAtacs_Type()
)
utmStatUnprocAtacs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmStatUnprocAtacs.setStatus("mandatory")
_UtmStatUnprocPrints_Type = Integer32
_UtmStatUnprocPrints_Object = MibScalar
utmStatUnprocPrints = _UtmStatUnprocPrints_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 2, 18),
    _UtmStatUnprocPrints_Type()
)
utmStatUnprocPrints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmStatUnprocPrints.setStatus("mandatory")
_UtmStatWaitDPUTs_Type = Integer32
_UtmStatWaitDPUTs_Object = MibScalar
utmStatWaitDPUTs = _UtmStatWaitDPUTs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 2, 19),
    _UtmStatWaitDPUTs_Type()
)
utmStatWaitDPUTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmStatWaitDPUTs.setStatus("mandatory")
_UtmStatAbTermConv_Type = Integer32
_UtmStatAbTermConv_Object = MibScalar
utmStatAbTermConv = _UtmStatAbTermConv_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 2, 20),
    _UtmStatAbTermConv_Type()
)
utmStatAbTermConv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmStatAbTermConv.setStatus("mandatory")
_UtmStatResourcWaits_Type = Gauge32
_UtmStatResourcWaits_Object = MibScalar
utmStatResourcWaits = _UtmStatResourcWaits_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 2, 21),
    _UtmStatResourcWaits_Type()
)
utmStatResourcWaits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmStatResourcWaits.setStatus("mandatory")
_UtmStatDeadlocks_Type = Integer32
_UtmStatDeadlocks_Object = MibScalar
utmStatDeadlocks = _UtmStatDeadlocks_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 2, 22),
    _UtmStatDeadlocks_Type()
)
utmStatDeadlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmStatDeadlocks.setStatus("mandatory")
_UtmStatPeriodWrites_Type = Integer32
_UtmStatPeriodWrites_Object = MibScalar
utmStatPeriodWrites = _UtmStatPeriodWrites_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 2, 23),
    _UtmStatPeriodWrites_Type()
)
utmStatPeriodWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmStatPeriodWrites.setStatus("mandatory")
_UtmStatPagesPWrite_Type = Integer32
_UtmStatPagesPWrite_Object = MibScalar
utmStatPagesPWrite = _UtmStatPagesPWrite_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 2, 24),
    _UtmStatPagesPWrite_Type()
)
utmStatPagesPWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmStatPagesPWrite.setStatus("mandatory")
_UtmStatLogWrites_Type = Integer32
_UtmStatLogWrites_Object = MibScalar
utmStatLogWrites = _UtmStatLogWrites_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 2, 25),
    _UtmStatLogWrites_Type()
)
utmStatLogWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmStatLogWrites.setStatus("mandatory")
_UtmStatActJR_Type = Integer32
_UtmStatActJR_Object = MibScalar
utmStatActJR = _UtmStatActJR_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 2, 26),
    _UtmStatActJR_Type()
)
utmStatActJR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmStatActJR.setStatus("mandatory")
_UtmStatMaxJR_Type = Integer32
_UtmStatMaxJR_Object = MibScalar
utmStatMaxJR = _UtmStatMaxJR_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 2, 27),
    _UtmStatMaxJR_Type()
)
utmStatMaxJR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmStatMaxJR.setStatus("mandatory")
_UtmSyspData_ObjectIdentity = ObjectIdentity
utmSyspData = _UtmSyspData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 3)
)


class _UtmSyspAccount_Type(Integer32):
    """Custom type utmSyspAccount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_UtmSyspAccount_Type.__name__ = "Integer32"
_UtmSyspAccount_Object = MibScalar
utmSyspAccount = _UtmSyspAccount_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 3, 1),
    _UtmSyspAccount_Type()
)
utmSyspAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmSyspAccount.setStatus("mandatory")


class _UtmSyspCalcAccount_Type(Integer32):
    """Custom type utmSyspCalcAccount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_UtmSyspCalcAccount_Type.__name__ = "Integer32"
_UtmSyspCalcAccount_Object = MibScalar
utmSyspCalcAccount = _UtmSyspCalcAccount_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 3, 2),
    _UtmSyspCalcAccount_Type()
)
utmSyspCalcAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmSyspCalcAccount.setStatus("mandatory")


class _UtmSyspSM2_Type(Integer32):
    """Custom type utmSyspSM2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_UtmSyspSM2_Type.__name__ = "Integer32"
_UtmSyspSM2_Object = MibScalar
utmSyspSM2 = _UtmSyspSM2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 3, 3),
    _UtmSyspSM2_Type()
)
utmSyspSM2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmSyspSM2.setStatus("mandatory")


class _UtmSyspKDCMON_Type(Integer32):
    """Custom type utmSyspKDCMON based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_UtmSyspKDCMON_Type.__name__ = "Integer32"
_UtmSyspKDCMON_Object = MibScalar
utmSyspKDCMON = _UtmSyspKDCMON_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 3, 4),
    _UtmSyspKDCMON_Type()
)
utmSyspKDCMON.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmSyspKDCMON.setStatus("mandatory")


class _UtmSyspTestmode_Type(Integer32):
    """Custom type utmSyspTestmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_UtmSyspTestmode_Type.__name__ = "Integer32"
_UtmSyspTestmode_Object = MibScalar
utmSyspTestmode = _UtmSyspTestmode_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 3, 5),
    _UtmSyspTestmode_Type()
)
utmSyspTestmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmSyspTestmode.setStatus("mandatory")
_UtmSyspMaxPagRate_Type = Gauge32
_UtmSyspMaxPagRate_Object = MibScalar
utmSyspMaxPagRate = _UtmSyspMaxPagRate_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 3, 6),
    _UtmSyspMaxPagRate_Type()
)
utmSyspMaxPagRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmSyspMaxPagRate.setStatus("mandatory")
_UtmSyspProgFGG_Type = Integer32
_UtmSyspProgFGG_Object = MibScalar
utmSyspProgFGG = _UtmSyspProgFGG_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 3, 7),
    _UtmSyspProgFGG_Type()
)
utmSyspProgFGG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmSyspProgFGG.setStatus("mandatory")
_UtmSyspTermWait_Type = Integer32
_UtmSyspTermWait_Object = MibScalar
utmSyspTermWait = _UtmSyspTermWait_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 3, 8),
    _UtmSyspTermWait_Type()
)
utmSyspTermWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmSyspTermWait.setStatus("mandatory")
_UtmSyspUsLogFGG_Type = Integer32
_UtmSyspUsLogFGG_Object = MibScalar
utmSyspUsLogFGG = _UtmSyspUsLogFGG_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 3, 9),
    _UtmSyspUsLogFGG_Type()
)
utmSyspUsLogFGG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmSyspUsLogFGG.setStatus("mandatory")
_UtmSyspResWaitTA_Type = Integer32
_UtmSyspResWaitTA_Object = MibScalar
utmSyspResWaitTA = _UtmSyspResWaitTA_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 3, 10),
    _UtmSyspResWaitTA_Type()
)
utmSyspResWaitTA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmSyspResWaitTA.setStatus("mandatory")
_UtmSyspMaxTasks_Type = Integer32
_UtmSyspMaxTasks_Object = MibScalar
utmSyspMaxTasks = _UtmSyspMaxTasks_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 3, 11),
    _UtmSyspMaxTasks_Type()
)
utmSyspMaxTasks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmSyspMaxTasks.setStatus("mandatory")
_UtmSyspResWaitPr_Type = Integer32
_UtmSyspResWaitPr_Object = MibScalar
utmSyspResWaitPr = _UtmSyspResWaitPr_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 3, 12),
    _UtmSyspResWaitPr_Type()
)
utmSyspResWaitPr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmSyspResWaitPr.setStatus("mandatory")
_UtmSyspCurrTasks_Type = Integer32
_UtmSyspCurrTasks_Object = MibScalar
utmSyspCurrTasks = _UtmSyspCurrTasks_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 3, 13),
    _UtmSyspCurrTasks_Type()
)
utmSyspCurrTasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmSyspCurrTasks.setStatus("mandatory")
_UtmSyspConRTime_Type = Integer32
_UtmSyspConRTime_Object = MibScalar
utmSyspConRTime = _UtmSyspConRTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 3, 14),
    _UtmSyspConRTime_Type()
)
utmSyspConRTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmSyspConRTime.setStatus("mandatory")
_UtmSyspMaxAsynTasks_Type = Integer32
_UtmSyspMaxAsynTasks_Object = MibScalar
utmSyspMaxAsynTasks = _UtmSyspMaxAsynTasks_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 3, 15),
    _UtmSyspMaxAsynTasks_Type()
)
utmSyspMaxAsynTasks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmSyspMaxAsynTasks.setStatus("mandatory")
_UtmSyspLogAckwait_Type = Integer32
_UtmSyspLogAckwait_Object = MibScalar
utmSyspLogAckwait = _UtmSyspLogAckwait_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 3, 16),
    _UtmSyspLogAckwait_Type()
)
utmSyspLogAckwait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmSyspLogAckwait.setStatus("mandatory")
_UtmSyspPTCTime_Type = Integer32
_UtmSyspPTCTime_Object = MibScalar
utmSyspPTCTime = _UtmSyspPTCTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 3, 17),
    _UtmSyspPTCTime_Type()
)
utmSyspPTCTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmSyspPTCTime.setStatus("mandatory")
_UtmSyspConcTime_Type = Integer32
_UtmSyspConcTime_Object = MibScalar
utmSyspConcTime = _UtmSyspConcTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 3, 18),
    _UtmSyspConcTime_Type()
)
utmSyspConcTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmSyspConcTime.setStatus("mandatory")
_UtmSyspPGWTTime_Type = Integer32
_UtmSyspPGWTTime_Object = MibScalar
utmSyspPGWTTime = _UtmSyspPGWTTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 3, 19),
    _UtmSyspPGWTTime_Type()
)
utmSyspPGWTTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmSyspPGWTTime.setStatus("mandatory")
_UtmSyspTasksWaitPGWT_Type = Integer32
_UtmSyspTasksWaitPGWT_Object = MibScalar
utmSyspTasksWaitPGWT = _UtmSyspTasksWaitPGWT_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 3, 20),
    _UtmSyspTasksWaitPGWT_Type()
)
utmSyspTasksWaitPGWT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmSyspTasksWaitPGWT.setStatus("mandatory")
_UtmSyspTasksinPGWT_Type = Integer32
_UtmSyspTasksinPGWT_Object = MibScalar
utmSyspTasksinPGWT = _UtmSyspTasksinPGWT_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 3, 21),
    _UtmSyspTasksinPGWT_Type()
)
utmSyspTasksinPGWT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmSyspTasksinPGWT.setStatus("mandatory")
_UtmPtermData_ObjectIdentity = ObjectIdentity
utmPtermData = _UtmPtermData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 4)
)
_UtmPtermTabNum_Type = Integer32
_UtmPtermTabNum_Object = MibScalar
utmPtermTabNum = _UtmPtermTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 4, 1),
    _UtmPtermTabNum_Type()
)
utmPtermTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmPtermTabNum.setStatus("mandatory")
_UtmPtermTable_Object = MibTable
utmPtermTable = _UtmPtermTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 4, 2)
)
if mibBuilder.loadTexts:
    utmPtermTable.setStatus("mandatory")
_UtmPtermEntry_Object = MibTableRow
utmPtermEntry = _UtmPtermEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 4, 2, 1)
)
utmPtermEntry.setIndexNames(
    (0, "UTM-MIB", "utmPtermIndex"),
)
if mibBuilder.loadTexts:
    utmPtermEntry.setStatus("mandatory")
_UtmPtermIndex_Type = Integer32
_UtmPtermIndex_Object = MibTableColumn
utmPtermIndex = _UtmPtermIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 4, 2, 1, 1),
    _UtmPtermIndex_Type()
)
utmPtermIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmPtermIndex.setStatus("mandatory")
_UtmPtermName_Type = DisplayString
_UtmPtermName_Object = MibTableColumn
utmPtermName = _UtmPtermName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 4, 2, 1, 2),
    _UtmPtermName_Type()
)
utmPtermName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmPtermName.setStatus("mandatory")
_UtmPtermProname_Type = DisplayString
_UtmPtermProname_Object = MibTableColumn
utmPtermProname = _UtmPtermProname_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 4, 2, 1, 3),
    _UtmPtermProname_Type()
)
utmPtermProname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmPtermProname.setStatus("mandatory")
_UtmPtermLterm_Type = DisplayString
_UtmPtermLterm_Object = MibTableColumn
utmPtermLterm = _UtmPtermLterm_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 4, 2, 1, 4),
    _UtmPtermLterm_Type()
)
utmPtermLterm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmPtermLterm.setStatus("mandatory")
_UtmPtermBCAMAppl_Type = DisplayString
_UtmPtermBCAMAppl_Object = MibTableColumn
utmPtermBCAMAppl = _UtmPtermBCAMAppl_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 4, 2, 1, 5),
    _UtmPtermBCAMAppl_Type()
)
utmPtermBCAMAppl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmPtermBCAMAppl.setStatus("mandatory")
_UtmPtermPtyp_Type = DisplayString
_UtmPtermPtyp_Object = MibTableColumn
utmPtermPtyp = _UtmPtermPtyp_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 4, 2, 1, 6),
    _UtmPtermPtyp_Type()
)
utmPtermPtyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmPtermPtyp.setStatus("mandatory")


class _UtmPtermStatus_Type(Integer32):
    """Custom type utmPtermStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_UtmPtermStatus_Type.__name__ = "Integer32"
_UtmPtermStatus_Object = MibTableColumn
utmPtermStatus = _UtmPtermStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 4, 2, 1, 7),
    _UtmPtermStatus_Type()
)
utmPtermStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmPtermStatus.setStatus("mandatory")


class _UtmPtermConnected_Type(Integer32):
    """Custom type utmPtermConnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("waiting", 3),
          ("yes", 1))
    )


_UtmPtermConnected_Type.__name__ = "Integer32"
_UtmPtermConnected_Object = MibTableColumn
utmPtermConnected = _UtmPtermConnected_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 4, 2, 1, 8),
    _UtmPtermConnected_Type()
)
utmPtermConnected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmPtermConnected.setStatus("mandatory")


class _UtmPtermConnectStatus_Type(Integer32):
    """Custom type utmPtermConnectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automaticCon", 1),
          ("na", 3),
          ("terminalPool", 2))
    )


_UtmPtermConnectStatus_Type.__name__ = "Integer32"
_UtmPtermConnectStatus_Object = MibTableColumn
utmPtermConnectStatus = _UtmPtermConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 4, 2, 1, 9),
    _UtmPtermConnectStatus_Type()
)
utmPtermConnectStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmPtermConnectStatus.setStatus("mandatory")


class _UtmPtermConnectForced_Type(Integer32):
    """Custom type utmPtermConnectForced based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_UtmPtermConnectForced_Type.__name__ = "Integer32"
_UtmPtermConnectForced_Object = MibTableColumn
utmPtermConnectForced = _UtmPtermConnectForced_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 4, 2, 1, 10),
    _UtmPtermConnectForced_Type()
)
utmPtermConnectForced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmPtermConnectForced.setStatus("mandatory")


class _UtmPtermConnectMultiplexed_Type(Integer32):
    """Custom type utmPtermConnectMultiplexed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_UtmPtermConnectMultiplexed_Type.__name__ = "Integer32"
_UtmPtermConnectMultiplexed_Object = MibTableColumn
utmPtermConnectMultiplexed = _UtmPtermConnectMultiplexed_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 4, 2, 1, 11),
    _UtmPtermConnectMultiplexed_Type()
)
utmPtermConnectMultiplexed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmPtermConnectMultiplexed.setStatus("mandatory")
_UtmPtermConTime_Type = Integer32
_UtmPtermConTime_Object = MibTableColumn
utmPtermConTime = _UtmPtermConTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 4, 2, 1, 12),
    _UtmPtermConTime_Type()
)
utmPtermConTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmPtermConTime.setStatus("mandatory")
_UtmPtermLett_Type = Integer32
_UtmPtermLett_Object = MibTableColumn
utmPtermLett = _UtmPtermLett_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 4, 2, 1, 13),
    _UtmPtermLett_Type()
)
utmPtermLett.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmPtermLett.setStatus("mandatory")
_UtmPtermConb_Type = Integer32
_UtmPtermConb_Object = MibTableColumn
utmPtermConb = _UtmPtermConb_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 4, 2, 1, 14),
    _UtmPtermConb_Type()
)
utmPtermConb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmPtermConb.setStatus("mandatory")
_UtmLtermData_ObjectIdentity = ObjectIdentity
utmLtermData = _UtmLtermData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 5)
)
_UtmLtermTabNum_Type = Integer32
_UtmLtermTabNum_Object = MibScalar
utmLtermTabNum = _UtmLtermTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 5, 1),
    _UtmLtermTabNum_Type()
)
utmLtermTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLtermTabNum.setStatus("mandatory")
_UtmLtermTable_Object = MibTable
utmLtermTable = _UtmLtermTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 5, 2)
)
if mibBuilder.loadTexts:
    utmLtermTable.setStatus("mandatory")
_UtmLtermEntry_Object = MibTableRow
utmLtermEntry = _UtmLtermEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 5, 2, 1)
)
utmLtermEntry.setIndexNames(
    (0, "UTM-MIB", "utmLtermIndex"),
)
if mibBuilder.loadTexts:
    utmLtermEntry.setStatus("mandatory")
_UtmLtermIndex_Type = Integer32
_UtmLtermIndex_Object = MibTableColumn
utmLtermIndex = _UtmLtermIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 5, 2, 1, 1),
    _UtmLtermIndex_Type()
)
utmLtermIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLtermIndex.setStatus("mandatory")
_UtmLtermName_Type = DisplayString
_UtmLtermName_Object = MibTableColumn
utmLtermName = _UtmLtermName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 5, 2, 1, 2),
    _UtmLtermName_Type()
)
utmLtermName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLtermName.setStatus("mandatory")
_UtmLtermPterm_Type = DisplayString
_UtmLtermPterm_Object = MibTableColumn
utmLtermPterm = _UtmLtermPterm_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 5, 2, 1, 3),
    _UtmLtermPterm_Type()
)
utmLtermPterm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmLtermPterm.setStatus("mandatory")
_UtmLtermUser_Type = DisplayString
_UtmLtermUser_Object = MibTableColumn
utmLtermUser = _UtmLtermUser_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 5, 2, 1, 4),
    _UtmLtermUser_Type()
)
utmLtermUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLtermUser.setStatus("mandatory")
_UtmLtermKset_Type = DisplayString
_UtmLtermKset_Object = MibTableColumn
utmLtermKset = _UtmLtermKset_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 5, 2, 1, 5),
    _UtmLtermKset_Type()
)
utmLtermKset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLtermKset.setStatus("mandatory")
_UtmLtermLock_Type = Integer32
_UtmLtermLock_Object = MibTableColumn
utmLtermLock = _UtmLtermLock_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 5, 2, 1, 6),
    _UtmLtermLock_Type()
)
utmLtermLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLtermLock.setStatus("mandatory")


class _UtmLtermUsageType_Type(Integer32):
    """Custom type utmLtermUsageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dialog", 1),
          ("output", 2))
    )


_UtmLtermUsageType_Type.__name__ = "Integer32"
_UtmLtermUsageType_Object = MibTableColumn
utmLtermUsageType = _UtmLtermUsageType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 5, 2, 1, 7),
    _UtmLtermUsageType_Type()
)
utmLtermUsageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLtermUsageType.setStatus("mandatory")


class _UtmLtermUsageBundle_Type(Integer32):
    """Custom type utmLtermUsageBundle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_UtmLtermUsageBundle_Type.__name__ = "Integer32"
_UtmLtermUsageBundle_Object = MibTableColumn
utmLtermUsageBundle = _UtmLtermUsageBundle_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 5, 2, 1, 8),
    _UtmLtermUsageBundle_Type()
)
utmLtermUsageBundle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLtermUsageBundle.setStatus("mandatory")


class _UtmLtermUsageTermPool_Type(Integer32):
    """Custom type utmLtermUsageTermPool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_UtmLtermUsageTermPool_Type.__name__ = "Integer32"
_UtmLtermUsageTermPool_Object = MibTableColumn
utmLtermUsageTermPool = _UtmLtermUsageTermPool_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 5, 2, 1, 9),
    _UtmLtermUsageTermPool_Type()
)
utmLtermUsageTermPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLtermUsageTermPool.setStatus("mandatory")


class _UtmLtermStatus_Type(Integer32):
    """Custom type utmLtermStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_UtmLtermStatus_Type.__name__ = "Integer32"
_UtmLtermStatus_Object = MibTableColumn
utmLtermStatus = _UtmLtermStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 5, 2, 1, 10),
    _UtmLtermStatus_Type()
)
utmLtermStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmLtermStatus.setStatus("mandatory")
_UtmLtermOutq_Type = Integer32
_UtmLtermOutq_Object = MibTableColumn
utmLtermOutq = _UtmLtermOutq_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 5, 2, 1, 11),
    _UtmLtermOutq_Type()
)
utmLtermOutq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLtermOutq.setStatus("mandatory")
_UtmLtermInCnt_Type = Integer32
_UtmLtermInCnt_Object = MibTableColumn
utmLtermInCnt = _UtmLtermInCnt_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 5, 2, 1, 12),
    _UtmLtermInCnt_Type()
)
utmLtermInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLtermInCnt.setStatus("mandatory")
_UtmLtermSecCnt_Type = Integer32
_UtmLtermSecCnt_Object = MibTableColumn
utmLtermSecCnt = _UtmLtermSecCnt_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 5, 2, 1, 13),
    _UtmLtermSecCnt_Type()
)
utmLtermSecCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLtermSecCnt.setStatus("mandatory")
_UtmTacData_ObjectIdentity = ObjectIdentity
utmTacData = _UtmTacData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 6)
)
_UtmTacTabNum_Type = Integer32
_UtmTacTabNum_Object = MibScalar
utmTacTabNum = _UtmTacTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 6, 1),
    _UtmTacTabNum_Type()
)
utmTacTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmTacTabNum.setStatus("mandatory")
_UtmTacTable_Object = MibTable
utmTacTable = _UtmTacTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 6, 2)
)
if mibBuilder.loadTexts:
    utmTacTable.setStatus("mandatory")
_UtmTacEntry_Object = MibTableRow
utmTacEntry = _UtmTacEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 6, 2, 1)
)
utmTacEntry.setIndexNames(
    (0, "UTM-MIB", "utmTacIndex"),
)
if mibBuilder.loadTexts:
    utmTacEntry.setStatus("mandatory")
_UtmTacIndex_Type = Integer32
_UtmTacIndex_Object = MibTableColumn
utmTacIndex = _UtmTacIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 6, 2, 1, 1),
    _UtmTacIndex_Type()
)
utmTacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmTacIndex.setStatus("mandatory")
_UtmTacName_Type = DisplayString
_UtmTacName_Object = MibTableColumn
utmTacName = _UtmTacName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 6, 2, 1, 2),
    _UtmTacName_Type()
)
utmTacName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmTacName.setStatus("mandatory")
_UtmTacLock_Type = Integer32
_UtmTacLock_Object = MibTableColumn
utmTacLock = _UtmTacLock_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 6, 2, 1, 3),
    _UtmTacLock_Type()
)
utmTacLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmTacLock.setStatus("mandatory")


class _UtmTacStatus_Type(Integer32):
    """Custom type utmTacStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("halt", 3),
          ("off", 2),
          ("on", 1))
    )


_UtmTacStatus_Type.__name__ = "Integer32"
_UtmTacStatus_Object = MibTableColumn
utmTacStatus = _UtmTacStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 6, 2, 1, 4),
    _UtmTacStatus_Type()
)
utmTacStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmTacStatus.setStatus("mandatory")
_UtmTacTcl_Type = Integer32
_UtmTacTcl_Object = MibTableColumn
utmTacTcl = _UtmTacTcl_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 6, 2, 1, 5),
    _UtmTacTcl_Type()
)
utmTacTcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmTacTcl.setStatus("mandatory")
_UtmTacInq_Type = Integer32
_UtmTacInq_Object = MibTableColumn
utmTacInq = _UtmTacInq_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 6, 2, 1, 6),
    _UtmTacInq_Type()
)
utmTacInq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmTacInq.setStatus("mandatory")
_UtmTacUsed_Type = Integer32
_UtmTacUsed_Object = MibTableColumn
utmTacUsed = _UtmTacUsed_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 6, 2, 1, 7),
    _UtmTacUsed_Type()
)
utmTacUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmTacUsed.setStatus("mandatory")
_UtmTacError_Type = Integer32
_UtmTacError_Object = MibTableColumn
utmTacError = _UtmTacError_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 6, 2, 1, 8),
    _UtmTacError_Type()
)
utmTacError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmTacError.setStatus("mandatory")
_UtmTacDbcnt_Type = Integer32
_UtmTacDbcnt_Object = MibTableColumn
utmTacDbcnt = _UtmTacDbcnt_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 6, 2, 1, 9),
    _UtmTacDbcnt_Type()
)
utmTacDbcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmTacDbcnt.setStatus("mandatory")
_UtmTacElap_Type = Integer32
_UtmTacElap_Object = MibTableColumn
utmTacElap = _UtmTacElap_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 6, 2, 1, 10),
    _UtmTacElap_Type()
)
utmTacElap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmTacElap.setStatus("mandatory")
_UtmTacDbElap_Type = Integer32
_UtmTacDbElap_Object = MibTableColumn
utmTacDbElap = _UtmTacDbElap_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 6, 2, 1, 11),
    _UtmTacDbElap_Type()
)
utmTacDbElap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmTacDbElap.setStatus("mandatory")
_UtmTacCpu_Type = Integer32
_UtmTacCpu_Object = MibTableColumn
utmTacCpu = _UtmTacCpu_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 6, 2, 1, 12),
    _UtmTacCpu_Type()
)
utmTacCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmTacCpu.setStatus("mandatory")
_UtmTacclassData_ObjectIdentity = ObjectIdentity
utmTacclassData = _UtmTacclassData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 7)
)
_UtmTacclassTable_Object = MibTable
utmTacclassTable = _UtmTacclassTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 7, 1)
)
if mibBuilder.loadTexts:
    utmTacclassTable.setStatus("mandatory")
_UtmTacclassEntry_Object = MibTableRow
utmTacclassEntry = _UtmTacclassEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 7, 1, 1)
)
utmTacclassEntry.setIndexNames(
    (0, "UTM-MIB", "utmTacclassNumber"),
)
if mibBuilder.loadTexts:
    utmTacclassEntry.setStatus("mandatory")
_UtmTacclassNumber_Type = Integer32
_UtmTacclassNumber_Object = MibTableColumn
utmTacclassNumber = _UtmTacclassNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 7, 1, 1, 1),
    _UtmTacclassNumber_Type()
)
utmTacclassNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmTacclassNumber.setStatus("mandatory")
_UtmTacclassTasks_Type = Integer32
_UtmTacclassTasks_Object = MibTableColumn
utmTacclassTasks = _UtmTacclassTasks_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 7, 1, 1, 2),
    _UtmTacclassTasks_Type()
)
utmTacclassTasks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmTacclassTasks.setStatus("mandatory")
_UtmTacclassWtMesg_Type = Integer32
_UtmTacclassWtMesg_Object = MibTableColumn
utmTacclassWtMesg = _UtmTacclassWtMesg_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 7, 1, 1, 3),
    _UtmTacclassWtMesg_Type()
)
utmTacclassWtMesg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmTacclassWtMesg.setStatus("mandatory")
_UtmTacclassAvgWtTime_Type = Integer32
_UtmTacclassAvgWtTime_Object = MibTableColumn
utmTacclassAvgWtTime = _UtmTacclassAvgWtTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 7, 1, 1, 4),
    _UtmTacclassAvgWtTime_Type()
)
utmTacclassAvgWtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmTacclassAvgWtTime.setStatus("mandatory")


class _UtmTacclassPGWT_Type(Integer32):
    """Custom type utmTacclassPGWT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_UtmTacclassPGWT_Type.__name__ = "Integer32"
_UtmTacclassPGWT_Object = MibTableColumn
utmTacclassPGWT = _UtmTacclassPGWT_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 7, 1, 1, 5),
    _UtmTacclassPGWT_Type()
)
utmTacclassPGWT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmTacclassPGWT.setStatus("mandatory")
_UtmUserData_ObjectIdentity = ObjectIdentity
utmUserData = _UtmUserData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 8)
)
_UtmUserTabNum_Type = Integer32
_UtmUserTabNum_Object = MibScalar
utmUserTabNum = _UtmUserTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 8, 1),
    _UtmUserTabNum_Type()
)
utmUserTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmUserTabNum.setStatus("mandatory")
_UtmUserTable_Object = MibTable
utmUserTable = _UtmUserTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 8, 2)
)
if mibBuilder.loadTexts:
    utmUserTable.setStatus("mandatory")
_UtmUserEntry_Object = MibTableRow
utmUserEntry = _UtmUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 8, 2, 1)
)
utmUserEntry.setIndexNames(
    (0, "UTM-MIB", "utmUserIndex"),
)
if mibBuilder.loadTexts:
    utmUserEntry.setStatus("mandatory")
_UtmUserIndex_Type = Integer32
_UtmUserIndex_Object = MibTableColumn
utmUserIndex = _UtmUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 8, 2, 1, 1),
    _UtmUserIndex_Type()
)
utmUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmUserIndex.setStatus("mandatory")
_UtmUserName_Type = DisplayString
_UtmUserName_Object = MibTableColumn
utmUserName = _UtmUserName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 8, 2, 1, 2),
    _UtmUserName_Type()
)
utmUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmUserName.setStatus("mandatory")
_UtmUserKset_Type = DisplayString
_UtmUserKset_Object = MibTableColumn
utmUserKset = _UtmUserKset_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 8, 2, 1, 3),
    _UtmUserKset_Type()
)
utmUserKset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmUserKset.setStatus("mandatory")


class _UtmUserStatus_Type(Integer32):
    """Custom type utmUserStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_UtmUserStatus_Type.__name__ = "Integer32"
_UtmUserStatus_Object = MibTableColumn
utmUserStatus = _UtmUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 8, 2, 1, 4),
    _UtmUserStatus_Type()
)
utmUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmUserStatus.setStatus("mandatory")


class _UtmUserInVg_Type(Integer32):
    """Custom type utmUserInVg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_UtmUserInVg_Type.__name__ = "Integer32"
_UtmUserInVg_Object = MibTableColumn
utmUserInVg = _UtmUserInVg_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 8, 2, 1, 5),
    _UtmUserInVg_Type()
)
utmUserInVg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmUserInVg.setStatus("mandatory")
_UtmUserNrTacs_Type = Integer32
_UtmUserNrTacs_Object = MibTableColumn
utmUserNrTacs = _UtmUserNrTacs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 8, 2, 1, 6),
    _UtmUserNrTacs_Type()
)
utmUserNrTacs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmUserNrTacs.setStatus("mandatory")
_UtmUserCpuTime_Type = Integer32
_UtmUserCpuTime_Object = MibTableColumn
utmUserCpuTime = _UtmUserCpuTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 8, 2, 1, 7),
    _UtmUserCpuTime_Type()
)
utmUserCpuTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmUserCpuTime.setStatus("mandatory")
_UtmUserSecCnt_Type = Integer32
_UtmUserSecCnt_Object = MibTableColumn
utmUserSecCnt = _UtmUserSecCnt_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 8, 2, 1, 8),
    _UtmUserSecCnt_Type()
)
utmUserSecCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmUserSecCnt.setStatus("mandatory")
_UtmUserLterm_Type = DisplayString
_UtmUserLterm_Object = MibTableColumn
utmUserLterm = _UtmUserLterm_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 8, 2, 1, 9),
    _UtmUserLterm_Type()
)
utmUserLterm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmUserLterm.setStatus("mandatory")
_UtmConData_ObjectIdentity = ObjectIdentity
utmConData = _UtmConData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 9)
)
_UtmConTabNum_Type = Integer32
_UtmConTabNum_Object = MibScalar
utmConTabNum = _UtmConTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 9, 1),
    _UtmConTabNum_Type()
)
utmConTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmConTabNum.setStatus("mandatory")
_UtmConTable_Object = MibTable
utmConTable = _UtmConTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 9, 2)
)
if mibBuilder.loadTexts:
    utmConTable.setStatus("mandatory")
_UtmConEntry_Object = MibTableRow
utmConEntry = _UtmConEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 9, 2, 1)
)
utmConEntry.setIndexNames(
    (0, "UTM-MIB", "utmConIndex"),
)
if mibBuilder.loadTexts:
    utmConEntry.setStatus("mandatory")
_UtmConIndex_Type = Integer32
_UtmConIndex_Object = MibTableColumn
utmConIndex = _UtmConIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 9, 2, 1, 1),
    _UtmConIndex_Type()
)
utmConIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmConIndex.setStatus("mandatory")
_UtmConName_Type = DisplayString
_UtmConName_Object = MibTableColumn
utmConName = _UtmConName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 9, 2, 1, 2),
    _UtmConName_Type()
)
utmConName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmConName.setStatus("mandatory")
_UtmConProname_Type = DisplayString
_UtmConProname_Object = MibTableColumn
utmConProname = _UtmConProname_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 9, 2, 1, 3),
    _UtmConProname_Type()
)
utmConProname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmConProname.setStatus("mandatory")
_UtmConLpap_Type = DisplayString
_UtmConLpap_Object = MibTableColumn
utmConLpap = _UtmConLpap_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 9, 2, 1, 4),
    _UtmConLpap_Type()
)
utmConLpap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmConLpap.setStatus("mandatory")
_UtmConBcamAppl_Type = DisplayString
_UtmConBcamAppl_Object = MibTableColumn
utmConBcamAppl = _UtmConBcamAppl_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 9, 2, 1, 5),
    _UtmConBcamAppl_Type()
)
utmConBcamAppl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmConBcamAppl.setStatus("mandatory")


class _UtmConStatus_Type(Integer32):
    """Custom type utmConStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_UtmConStatus_Type.__name__ = "Integer32"
_UtmConStatus_Object = MibTableColumn
utmConStatus = _UtmConStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 9, 2, 1, 6),
    _UtmConStatus_Type()
)
utmConStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmConStatus.setStatus("mandatory")


class _UtmConConnected_Type(Integer32):
    """Custom type utmConConnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("waiting", 3),
          ("yes", 1))
    )


_UtmConConnected_Type.__name__ = "Integer32"
_UtmConConnected_Object = MibTableColumn
utmConConnected = _UtmConConnected_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 9, 2, 1, 7),
    _UtmConConnected_Type()
)
utmConConnected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmConConnected.setStatus("mandatory")


class _UtmConConnectStatus_Type(Integer32):
    """Custom type utmConConnectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automaticCon", 1),
          ("noAutomaticCon", 2))
    )


_UtmConConnectStatus_Type.__name__ = "Integer32"
_UtmConConnectStatus_Object = MibTableColumn
utmConConnectStatus = _UtmConConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 9, 2, 1, 8),
    _UtmConConnectStatus_Type()
)
utmConConnectStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmConConnectStatus.setStatus("mandatory")
_UtmConConTime_Type = Integer32
_UtmConConTime_Object = MibTableColumn
utmConConTime = _UtmConConTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 9, 2, 1, 9),
    _UtmConConTime_Type()
)
utmConConTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmConConTime.setStatus("mandatory")
_UtmConLett_Type = Integer32
_UtmConLett_Object = MibTableColumn
utmConLett = _UtmConLett_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 9, 2, 1, 10),
    _UtmConLett_Type()
)
utmConLett.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmConLett.setStatus("mandatory")
_UtmConConb_Type = Integer32
_UtmConConb_Object = MibTableColumn
utmConConb = _UtmConConb_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 9, 2, 1, 11),
    _UtmConConb_Type()
)
utmConConb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmConConb.setStatus("mandatory")
_UtmLpapData_ObjectIdentity = ObjectIdentity
utmLpapData = _UtmLpapData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 10)
)
_UtmLpapTabNum_Type = Integer32
_UtmLpapTabNum_Object = MibScalar
utmLpapTabNum = _UtmLpapTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 10, 1),
    _UtmLpapTabNum_Type()
)
utmLpapTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLpapTabNum.setStatus("mandatory")
_UtmLpapTable_Object = MibTable
utmLpapTable = _UtmLpapTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 10, 2)
)
if mibBuilder.loadTexts:
    utmLpapTable.setStatus("mandatory")
_UtmLpapEntry_Object = MibTableRow
utmLpapEntry = _UtmLpapEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 10, 2, 1)
)
utmLpapEntry.setIndexNames(
    (0, "UTM-MIB", "utmLpapIndex"),
)
if mibBuilder.loadTexts:
    utmLpapEntry.setStatus("mandatory")
_UtmLpapIndex_Type = Integer32
_UtmLpapIndex_Object = MibTableColumn
utmLpapIndex = _UtmLpapIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 10, 2, 1, 1),
    _UtmLpapIndex_Type()
)
utmLpapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLpapIndex.setStatus("mandatory")
_UtmLpapName_Type = DisplayString
_UtmLpapName_Object = MibTableColumn
utmLpapName = _UtmLpapName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 10, 2, 1, 2),
    _UtmLpapName_Type()
)
utmLpapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLpapName.setStatus("mandatory")
_UtmLpapKset_Type = DisplayString
_UtmLpapKset_Object = MibTableColumn
utmLpapKset = _UtmLpapKset_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 10, 2, 1, 3),
    _UtmLpapKset_Type()
)
utmLpapKset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLpapKset.setStatus("mandatory")


class _UtmLpapStatus_Type(Integer32):
    """Custom type utmLpapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_UtmLpapStatus_Type.__name__ = "Integer32"
_UtmLpapStatus_Object = MibTableColumn
utmLpapStatus = _UtmLpapStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 10, 2, 1, 4),
    _UtmLpapStatus_Type()
)
utmLpapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmLpapStatus.setStatus("mandatory")


class _UtmLpapQuiet_Type(Integer32):
    """Custom type utmLpapQuiet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_UtmLpapQuiet_Type.__name__ = "Integer32"
_UtmLpapQuiet_Object = MibTableColumn
utmLpapQuiet = _UtmLpapQuiet_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 10, 2, 1, 5),
    _UtmLpapQuiet_Type()
)
utmLpapQuiet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmLpapQuiet.setStatus("mandatory")
_UtmLpapOutq_Type = Integer32
_UtmLpapOutq_Object = MibTableColumn
utmLpapOutq = _UtmLpapOutq_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 10, 2, 1, 6),
    _UtmLpapOutq_Type()
)
utmLpapOutq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLpapOutq.setStatus("mandatory")
_UtmLpapIdleTime_Type = Integer32
_UtmLpapIdleTime_Object = MibTableColumn
utmLpapIdleTime = _UtmLpapIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 10, 2, 1, 7),
    _UtmLpapIdleTime_Type()
)
utmLpapIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmLpapIdleTime.setStatus("mandatory")
_UtmPoolData_ObjectIdentity = ObjectIdentity
utmPoolData = _UtmPoolData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 11)
)
_UtmPoolTabNum_Type = Integer32
_UtmPoolTabNum_Object = MibScalar
utmPoolTabNum = _UtmPoolTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 11, 1),
    _UtmPoolTabNum_Type()
)
utmPoolTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmPoolTabNum.setStatus("mandatory")
_UtmPoolTable_Object = MibTable
utmPoolTable = _UtmPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 11, 2)
)
if mibBuilder.loadTexts:
    utmPoolTable.setStatus("mandatory")
_UtmPoolEntry_Object = MibTableRow
utmPoolEntry = _UtmPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 11, 2, 1)
)
utmPoolEntry.setIndexNames(
    (0, "UTM-MIB", "utmPoolIndex"),
)
if mibBuilder.loadTexts:
    utmPoolEntry.setStatus("mandatory")
_UtmPoolIndex_Type = Integer32
_UtmPoolIndex_Object = MibTableColumn
utmPoolIndex = _UtmPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 11, 2, 1, 1),
    _UtmPoolIndex_Type()
)
utmPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmPoolIndex.setStatus("mandatory")
_UtmPoolProname_Type = DisplayString
_UtmPoolProname_Object = MibTableColumn
utmPoolProname = _UtmPoolProname_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 11, 2, 1, 2),
    _UtmPoolProname_Type()
)
utmPoolProname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmPoolProname.setStatus("mandatory")
_UtmPoolBcamAppl_Type = DisplayString
_UtmPoolBcamAppl_Object = MibTableColumn
utmPoolBcamAppl = _UtmPoolBcamAppl_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 11, 2, 1, 3),
    _UtmPoolBcamAppl_Type()
)
utmPoolBcamAppl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmPoolBcamAppl.setStatus("mandatory")
_UtmPoolPtype_Type = DisplayString
_UtmPoolPtype_Object = MibTableColumn
utmPoolPtype = _UtmPoolPtype_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 11, 2, 1, 4),
    _UtmPoolPtype_Type()
)
utmPoolPtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmPoolPtype.setStatus("mandatory")
_UtmPoolStations_Type = Integer32
_UtmPoolStations_Object = MibTableColumn
utmPoolStations = _UtmPoolStations_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 11, 2, 1, 5),
    _UtmPoolStations_Type()
)
utmPoolStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmPoolStations.setStatus("mandatory")
_UtmPoolStatusOn_Type = Integer32
_UtmPoolStatusOn_Object = MibTableColumn
utmPoolStatusOn = _UtmPoolStatusOn_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 11, 2, 1, 6),
    _UtmPoolStatusOn_Type()
)
utmPoolStatusOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmPoolStatusOn.setStatus("mandatory")
_UtmPoolActCon_Type = Integer32
_UtmPoolActCon_Object = MibTableColumn
utmPoolActCon = _UtmPoolActCon_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 11, 2, 1, 7),
    _UtmPoolActCon_Type()
)
utmPoolActCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmPoolActCon.setStatus("mandatory")
_UtmPoolMaxCon_Type = Integer32
_UtmPoolMaxCon_Object = MibTableColumn
utmPoolMaxCon = _UtmPoolMaxCon_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 11, 2, 1, 8),
    _UtmPoolMaxCon_Type()
)
utmPoolMaxCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmPoolMaxCon.setStatus("mandatory")
_UtmPoolKset_Type = DisplayString
_UtmPoolKset_Object = MibTableColumn
utmPoolKset = _UtmPoolKset_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 11, 2, 1, 9),
    _UtmPoolKset_Type()
)
utmPoolKset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmPoolKset.setStatus("mandatory")
_UtmPoolLock_Type = Integer32
_UtmPoolLock_Object = MibTableColumn
utmPoolLock = _UtmPoolLock_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 11, 2, 1, 10),
    _UtmPoolLock_Type()
)
utmPoolLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmPoolLock.setStatus("mandatory")
_UtmLsesData_ObjectIdentity = ObjectIdentity
utmLsesData = _UtmLsesData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 12)
)
_UtmLsesTabNum_Type = Integer32
_UtmLsesTabNum_Object = MibScalar
utmLsesTabNum = _UtmLsesTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 12, 1),
    _UtmLsesTabNum_Type()
)
utmLsesTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLsesTabNum.setStatus("mandatory")
_UtmLsesTable_Object = MibTable
utmLsesTable = _UtmLsesTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 12, 2)
)
if mibBuilder.loadTexts:
    utmLsesTable.setStatus("mandatory")
_UtmLsesEntry_Object = MibTableRow
utmLsesEntry = _UtmLsesEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 12, 2, 1)
)
utmLsesEntry.setIndexNames(
    (0, "UTM-MIB", "utmLsesIndex"),
)
if mibBuilder.loadTexts:
    utmLsesEntry.setStatus("mandatory")
_UtmLsesIndex_Type = Integer32
_UtmLsesIndex_Object = MibTableColumn
utmLsesIndex = _UtmLsesIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 12, 2, 1, 1),
    _UtmLsesIndex_Type()
)
utmLsesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLsesIndex.setStatus("mandatory")
_UtmLsesName_Type = DisplayString
_UtmLsesName_Object = MibTableColumn
utmLsesName = _UtmLsesName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 12, 2, 1, 2),
    _UtmLsesName_Type()
)
utmLsesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLsesName.setStatus("mandatory")
_UtmLsesRses_Type = DisplayString
_UtmLsesRses_Object = MibTableColumn
utmLsesRses = _UtmLsesRses_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 12, 2, 1, 3),
    _UtmLsesRses_Type()
)
utmLsesRses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLsesRses.setStatus("mandatory")
_UtmLsesLpap_Type = DisplayString
_UtmLsesLpap_Object = MibTableColumn
utmLsesLpap = _UtmLsesLpap_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 12, 2, 1, 4),
    _UtmLsesLpap_Type()
)
utmLsesLpap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLsesLpap.setStatus("mandatory")
_UtmLsesCon_Type = DisplayString
_UtmLsesCon_Object = MibTableColumn
utmLsesCon = _UtmLsesCon_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 12, 2, 1, 5),
    _UtmLsesCon_Type()
)
utmLsesCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLsesCon.setStatus("mandatory")
_UtmLsesProname_Type = DisplayString
_UtmLsesProname_Object = MibTableColumn
utmLsesProname = _UtmLsesProname_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 12, 2, 1, 6),
    _UtmLsesProname_Type()
)
utmLsesProname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLsesProname.setStatus("mandatory")
_UtmLsesBcamAppl_Type = DisplayString
_UtmLsesBcamAppl_Object = MibTableColumn
utmLsesBcamAppl = _UtmLsesBcamAppl_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 12, 2, 1, 7),
    _UtmLsesBcamAppl_Type()
)
utmLsesBcamAppl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLsesBcamAppl.setStatus("mandatory")
_UtmLsesAgUser_Type = DisplayString
_UtmLsesAgUser_Object = MibTableColumn
utmLsesAgUser = _UtmLsesAgUser_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 12, 2, 1, 8),
    _UtmLsesAgUser_Type()
)
utmLsesAgUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLsesAgUser.setStatus("mandatory")
_UtmLtacData_ObjectIdentity = ObjectIdentity
utmLtacData = _UtmLtacData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 13)
)
_UtmLtacTabNum_Type = Integer32
_UtmLtacTabNum_Object = MibScalar
utmLtacTabNum = _UtmLtacTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 13, 1),
    _UtmLtacTabNum_Type()
)
utmLtacTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLtacTabNum.setStatus("mandatory")
_UtmLtacTable_Object = MibTable
utmLtacTable = _UtmLtacTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 13, 2)
)
if mibBuilder.loadTexts:
    utmLtacTable.setStatus("mandatory")
_UtmLtacEntry_Object = MibTableRow
utmLtacEntry = _UtmLtacEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 13, 2, 1)
)
utmLtacEntry.setIndexNames(
    (0, "UTM-MIB", "utmLtacIndex"),
)
if mibBuilder.loadTexts:
    utmLtacEntry.setStatus("mandatory")
_UtmLtacIndex_Type = Integer32
_UtmLtacIndex_Object = MibTableColumn
utmLtacIndex = _UtmLtacIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 13, 2, 1, 1),
    _UtmLtacIndex_Type()
)
utmLtacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLtacIndex.setStatus("mandatory")
_UtmLtacName_Type = DisplayString
_UtmLtacName_Object = MibTableColumn
utmLtacName = _UtmLtacName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 13, 2, 1, 2),
    _UtmLtacName_Type()
)
utmLtacName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLtacName.setStatus("mandatory")
_UtmLtacLock_Type = Integer32
_UtmLtacLock_Object = MibTableColumn
utmLtacLock = _UtmLtacLock_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 13, 2, 1, 3),
    _UtmLtacLock_Type()
)
utmLtacLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLtacLock.setStatus("mandatory")


class _UtmLtacStatus_Type(Integer32):
    """Custom type utmLtacStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_UtmLtacStatus_Type.__name__ = "Integer32"
_UtmLtacStatus_Object = MibTableColumn
utmLtacStatus = _UtmLtacStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 13, 2, 1, 4),
    _UtmLtacStatus_Type()
)
utmLtacStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmLtacStatus.setStatus("mandatory")
_UtmLtacRtac_Type = DisplayString
_UtmLtacRtac_Object = MibTableColumn
utmLtacRtac = _UtmLtacRtac_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 13, 2, 1, 5),
    _UtmLtacRtac_Type()
)
utmLtacRtac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLtacRtac.setStatus("mandatory")
_UtmLtacLpap_Type = DisplayString
_UtmLtacLpap_Object = MibTableColumn
utmLtacLpap = _UtmLtacLpap_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 13, 2, 1, 6),
    _UtmLtacLpap_Type()
)
utmLtacLpap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLtacLpap.setStatus("mandatory")
_UtmLtacAccessWait_Type = Integer32
_UtmLtacAccessWait_Object = MibTableColumn
utmLtacAccessWait = _UtmLtacAccessWait_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 13, 2, 1, 7),
    _UtmLtacAccessWait_Type()
)
utmLtacAccessWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmLtacAccessWait.setStatus("mandatory")
_UtmLtacReplyWait_Type = Integer32
_UtmLtacReplyWait_Object = MibTableColumn
utmLtacReplyWait = _UtmLtacReplyWait_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 13, 2, 1, 8),
    _UtmLtacReplyWait_Type()
)
utmLtacReplyWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmLtacReplyWait.setStatus("mandatory")
_UtmLtacUsed_Type = Integer32
_UtmLtacUsed_Object = MibTableColumn
utmLtacUsed = _UtmLtacUsed_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 13, 2, 1, 9),
    _UtmLtacUsed_Type()
)
utmLtacUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmLtacUsed.setStatus("mandatory")
_UtmOsiAssData_ObjectIdentity = ObjectIdentity
utmOsiAssData = _UtmOsiAssData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 14)
)
_UtmOsiAssTabNum_Type = Integer32
_UtmOsiAssTabNum_Object = MibScalar
utmOsiAssTabNum = _UtmOsiAssTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 14, 1),
    _UtmOsiAssTabNum_Type()
)
utmOsiAssTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmOsiAssTabNum.setStatus("mandatory")
_UtmOsiAssTable_Object = MibTable
utmOsiAssTable = _UtmOsiAssTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 14, 2)
)
if mibBuilder.loadTexts:
    utmOsiAssTable.setStatus("mandatory")
_UtmOsiAssEntry_Object = MibTableRow
utmOsiAssEntry = _UtmOsiAssEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 14, 2, 1)
)
utmOsiAssEntry.setIndexNames(
    (0, "UTM-MIB", "utmOsiAssIndex"),
)
if mibBuilder.loadTexts:
    utmOsiAssEntry.setStatus("mandatory")
_UtmOsiAssIndex_Type = Integer32
_UtmOsiAssIndex_Object = MibTableColumn
utmOsiAssIndex = _UtmOsiAssIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 14, 2, 1, 1),
    _UtmOsiAssIndex_Type()
)
utmOsiAssIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmOsiAssIndex.setStatus("mandatory")
_UtmOsiAssName_Type = DisplayString
_UtmOsiAssName_Object = MibTableColumn
utmOsiAssName = _UtmOsiAssName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 14, 2, 1, 2),
    _UtmOsiAssName_Type()
)
utmOsiAssName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmOsiAssName.setStatus("mandatory")
_UtmOsiAssOsiLpap_Type = DisplayString
_UtmOsiAssOsiLpap_Object = MibTableColumn
utmOsiAssOsiLpap = _UtmOsiAssOsiLpap_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 14, 2, 1, 3),
    _UtmOsiAssOsiLpap_Type()
)
utmOsiAssOsiLpap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmOsiAssOsiLpap.setStatus("mandatory")
_UtmOsiAssOsiCon_Type = DisplayString
_UtmOsiAssOsiCon_Object = MibTableColumn
utmOsiAssOsiCon = _UtmOsiAssOsiCon_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 14, 2, 1, 4),
    _UtmOsiAssOsiCon_Type()
)
utmOsiAssOsiCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmOsiAssOsiCon.setStatus("mandatory")
_UtmOsiAssAgUser_Type = DisplayString
_UtmOsiAssAgUser_Object = MibTableColumn
utmOsiAssAgUser = _UtmOsiAssAgUser_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 14, 2, 1, 5),
    _UtmOsiAssAgUser_Type()
)
utmOsiAssAgUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmOsiAssAgUser.setStatus("mandatory")
_UtmOsiAssConTime_Type = Integer32
_UtmOsiAssConTime_Object = MibTableColumn
utmOsiAssConTime = _UtmOsiAssConTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 14, 2, 1, 6),
    _UtmOsiAssConTime_Type()
)
utmOsiAssConTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmOsiAssConTime.setStatus("mandatory")
_UtmOsiAssLetters_Type = Integer32
_UtmOsiAssLetters_Object = MibTableColumn
utmOsiAssLetters = _UtmOsiAssLetters_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 14, 2, 1, 7),
    _UtmOsiAssLetters_Type()
)
utmOsiAssLetters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmOsiAssLetters.setStatus("mandatory")
_UtmOsiConData_ObjectIdentity = ObjectIdentity
utmOsiConData = _UtmOsiConData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 15)
)
_UtmOsiConTabNum_Type = Integer32
_UtmOsiConTabNum_Object = MibScalar
utmOsiConTabNum = _UtmOsiConTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 15, 1),
    _UtmOsiConTabNum_Type()
)
utmOsiConTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmOsiConTabNum.setStatus("mandatory")
_UtmOsiConTable_Object = MibTable
utmOsiConTable = _UtmOsiConTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 15, 2)
)
if mibBuilder.loadTexts:
    utmOsiConTable.setStatus("mandatory")
_UtmOsiConEntry_Object = MibTableRow
utmOsiConEntry = _UtmOsiConEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 15, 2, 1)
)
utmOsiConEntry.setIndexNames(
    (0, "UTM-MIB", "utmOsiConIndex"),
)
if mibBuilder.loadTexts:
    utmOsiConEntry.setStatus("mandatory")
_UtmOsiConIndex_Type = Integer32
_UtmOsiConIndex_Object = MibTableColumn
utmOsiConIndex = _UtmOsiConIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 15, 2, 1, 1),
    _UtmOsiConIndex_Type()
)
utmOsiConIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmOsiConIndex.setStatus("mandatory")
_UtmOsiConName_Type = DisplayString
_UtmOsiConName_Object = MibTableColumn
utmOsiConName = _UtmOsiConName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 15, 2, 1, 2),
    _UtmOsiConName_Type()
)
utmOsiConName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmOsiConName.setStatus("mandatory")
_UtmOsiConOsiLpap_Type = DisplayString
_UtmOsiConOsiLpap_Object = MibTableColumn
utmOsiConOsiLpap = _UtmOsiConOsiLpap_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 15, 2, 1, 3),
    _UtmOsiConOsiLpap_Type()
)
utmOsiConOsiLpap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmOsiConOsiLpap.setStatus("mandatory")
_UtmOsiConTsel_Type = DisplayString
_UtmOsiConTsel_Object = MibTableColumn
utmOsiConTsel = _UtmOsiConTsel_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 15, 2, 1, 4),
    _UtmOsiConTsel_Type()
)
utmOsiConTsel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmOsiConTsel.setStatus("mandatory")
_UtmOsiConNsel_Type = DisplayString
_UtmOsiConNsel_Object = MibTableColumn
utmOsiConNsel = _UtmOsiConNsel_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 15, 2, 1, 5),
    _UtmOsiConNsel_Type()
)
utmOsiConNsel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmOsiConNsel.setStatus("mandatory")
_UtmOsiConAccPnt_Type = DisplayString
_UtmOsiConAccPnt_Object = MibTableColumn
utmOsiConAccPnt = _UtmOsiConAccPnt_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 15, 2, 1, 6),
    _UtmOsiConAccPnt_Type()
)
utmOsiConAccPnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmOsiConAccPnt.setStatus("mandatory")


class _UtmOsiConActive_Type(Integer32):
    """Custom type utmOsiConActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_UtmOsiConActive_Type.__name__ = "Integer32"
_UtmOsiConActive_Object = MibTableColumn
utmOsiConActive = _UtmOsiConActive_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 15, 2, 1, 7),
    _UtmOsiConActive_Type()
)
utmOsiConActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmOsiConActive.setStatus("mandatory")
_UtmOsiLpapData_ObjectIdentity = ObjectIdentity
utmOsiLpapData = _UtmOsiLpapData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 16)
)
_UtmOsiLpapTabNum_Type = Integer32
_UtmOsiLpapTabNum_Object = MibScalar
utmOsiLpapTabNum = _UtmOsiLpapTabNum_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 16, 1),
    _UtmOsiLpapTabNum_Type()
)
utmOsiLpapTabNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmOsiLpapTabNum.setStatus("mandatory")
_UtmOsiLpapTable_Object = MibTable
utmOsiLpapTable = _UtmOsiLpapTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 16, 2)
)
if mibBuilder.loadTexts:
    utmOsiLpapTable.setStatus("mandatory")
_UtmOsiLpapEntry_Object = MibTableRow
utmOsiLpapEntry = _UtmOsiLpapEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 16, 2, 1)
)
utmOsiLpapEntry.setIndexNames(
    (0, "UTM-MIB", "utmOsiLpapIndex"),
)
if mibBuilder.loadTexts:
    utmOsiLpapEntry.setStatus("mandatory")
_UtmOsiLpapIndex_Type = Integer32
_UtmOsiLpapIndex_Object = MibTableColumn
utmOsiLpapIndex = _UtmOsiLpapIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 16, 2, 1, 1),
    _UtmOsiLpapIndex_Type()
)
utmOsiLpapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmOsiLpapIndex.setStatus("mandatory")
_UtmOsiLpapName_Type = DisplayString
_UtmOsiLpapName_Object = MibTableColumn
utmOsiLpapName = _UtmOsiLpapName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 16, 2, 1, 2),
    _UtmOsiLpapName_Type()
)
utmOsiLpapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmOsiLpapName.setStatus("mandatory")
_UtmOsiLpapKset_Type = DisplayString
_UtmOsiLpapKset_Object = MibTableColumn
utmOsiLpapKset = _UtmOsiLpapKset_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 16, 2, 1, 3),
    _UtmOsiLpapKset_Type()
)
utmOsiLpapKset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmOsiLpapKset.setStatus("mandatory")


class _UtmOsiLpapStatus_Type(Integer32):
    """Custom type utmOsiLpapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_UtmOsiLpapStatus_Type.__name__ = "Integer32"
_UtmOsiLpapStatus_Object = MibTableColumn
utmOsiLpapStatus = _UtmOsiLpapStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 16, 2, 1, 4),
    _UtmOsiLpapStatus_Type()
)
utmOsiLpapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmOsiLpapStatus.setStatus("mandatory")


class _UtmOsiLpapQuiet_Type(Integer32):
    """Custom type utmOsiLpapQuiet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_UtmOsiLpapQuiet_Type.__name__ = "Integer32"
_UtmOsiLpapQuiet_Object = MibTableColumn
utmOsiLpapQuiet = _UtmOsiLpapQuiet_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 16, 2, 1, 5),
    _UtmOsiLpapQuiet_Type()
)
utmOsiLpapQuiet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmOsiLpapQuiet.setStatus("mandatory")
_UtmOsiLpapOutq_Type = Integer32
_UtmOsiLpapOutq_Object = MibTableColumn
utmOsiLpapOutq = _UtmOsiLpapOutq_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 16, 2, 1, 6),
    _UtmOsiLpapOutq_Type()
)
utmOsiLpapOutq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmOsiLpapOutq.setStatus("mandatory")
_UtmOsiLpapIdleTime_Type = Integer32
_UtmOsiLpapIdleTime_Object = MibTableColumn
utmOsiLpapIdleTime = _UtmOsiLpapIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 16, 2, 1, 7),
    _UtmOsiLpapIdleTime_Type()
)
utmOsiLpapIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmOsiLpapIdleTime.setStatus("mandatory")
_UtmOsiLpapOsiCon_Type = DisplayString
_UtmOsiLpapOsiCon_Object = MibTableColumn
utmOsiLpapOsiCon = _UtmOsiLpapOsiCon_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 16, 2, 1, 8),
    _UtmOsiLpapOsiCon_Type()
)
utmOsiLpapOsiCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmOsiLpapOsiCon.setStatus("mandatory")
_UtmOsiLpapAssoc_Type = Integer32
_UtmOsiLpapAssoc_Object = MibTableColumn
utmOsiLpapAssoc = _UtmOsiLpapAssoc_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 16, 2, 1, 9),
    _UtmOsiLpapAssoc_Type()
)
utmOsiLpapAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmOsiLpapAssoc.setStatus("mandatory")
_UtmOsiLpapConnect_Type = Integer32
_UtmOsiLpapConnect_Object = MibTableColumn
utmOsiLpapConnect = _UtmOsiLpapConnect_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 16, 2, 1, 10),
    _UtmOsiLpapConnect_Type()
)
utmOsiLpapConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmOsiLpapConnect.setStatus("mandatory")
_UtmOsiLpapAutoCon_Type = Integer32
_UtmOsiLpapAutoCon_Object = MibTableColumn
utmOsiLpapAutoCon = _UtmOsiLpapAutoCon_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 16, 2, 1, 11),
    _UtmOsiLpapAutoCon_Type()
)
utmOsiLpapAutoCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utmOsiLpapAutoCon.setStatus("mandatory")
_UtmMiscData_ObjectIdentity = ObjectIdentity
utmMiscData = _UtmMiscData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 17)
)
_UtmTrapControl_ObjectIdentity = ObjectIdentity
utmTrapControl = _UtmTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 4)
)
_UtmTrapCtrlCheckCaseNOW_Type = Integer32
_UtmTrapCtrlCheckCaseNOW_Object = MibScalar
utmTrapCtrlCheckCaseNOW = _UtmTrapCtrlCheckCaseNOW_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 4, 1),
    _UtmTrapCtrlCheckCaseNOW_Type()
)
utmTrapCtrlCheckCaseNOW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmTrapCtrlCheckCaseNOW.setStatus("mandatory")
_UtmTrapCtrlAbortedPeriod_Type = Integer32
_UtmTrapCtrlAbortedPeriod_Object = MibScalar
utmTrapCtrlAbortedPeriod = _UtmTrapCtrlAbortedPeriod_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 4, 2),
    _UtmTrapCtrlAbortedPeriod_Type()
)
utmTrapCtrlAbortedPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmTrapCtrlAbortedPeriod.setStatus("mandatory")
_UtmTrapCtrlPENDERPeriod_Type = Integer32
_UtmTrapCtrlPENDERPeriod_Object = MibScalar
utmTrapCtrlPENDERPeriod = _UtmTrapCtrlPENDERPeriod_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 4, 3),
    _UtmTrapCtrlPENDERPeriod_Type()
)
utmTrapCtrlPENDERPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmTrapCtrlPENDERPeriod.setStatus("mandatory")
_UtmTrapCtrlDeadlockPeriod_Type = Integer32
_UtmTrapCtrlDeadlockPeriod_Object = MibScalar
utmTrapCtrlDeadlockPeriod = _UtmTrapCtrlDeadlockPeriod_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 4, 4),
    _UtmTrapCtrlDeadlockPeriod_Type()
)
utmTrapCtrlDeadlockPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmTrapCtrlDeadlockPeriod.setStatus("mandatory")
_UtmTrapCtrlSecurViolPeriod_Type = Integer32
_UtmTrapCtrlSecurViolPeriod_Object = MibScalar
utmTrapCtrlSecurViolPeriod = _UtmTrapCtrlSecurViolPeriod_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 4, 5),
    _UtmTrapCtrlSecurViolPeriod_Type()
)
utmTrapCtrlSecurViolPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmTrapCtrlSecurViolPeriod.setStatus("mandatory")
_UtmTrapCtrlSecurViolLimit_Type = Integer32
_UtmTrapCtrlSecurViolLimit_Object = MibScalar
utmTrapCtrlSecurViolLimit = _UtmTrapCtrlSecurViolLimit_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 4, 6),
    _UtmTrapCtrlSecurViolLimit_Type()
)
utmTrapCtrlSecurViolLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmTrapCtrlSecurViolLimit.setStatus("mandatory")
_UtmTrapCtrlConnLossPeriod_Type = Integer32
_UtmTrapCtrlConnLossPeriod_Object = MibScalar
utmTrapCtrlConnLossPeriod = _UtmTrapCtrlConnLossPeriod_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 4, 7),
    _UtmTrapCtrlConnLossPeriod_Type()
)
utmTrapCtrlConnLossPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmTrapCtrlConnLossPeriod.setStatus("mandatory")
_UtmTrapCtrlConnLossLimit_Type = Integer32
_UtmTrapCtrlConnLossLimit_Object = MibScalar
utmTrapCtrlConnLossLimit = _UtmTrapCtrlConnLossLimit_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 4, 8),
    _UtmTrapCtrlConnLossLimit_Type()
)
utmTrapCtrlConnLossLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmTrapCtrlConnLossLimit.setStatus("mandatory")
_UtmTrapCtrlConnUsersPeriod_Type = Integer32
_UtmTrapCtrlConnUsersPeriod_Object = MibScalar
utmTrapCtrlConnUsersPeriod = _UtmTrapCtrlConnUsersPeriod_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 4, 9),
    _UtmTrapCtrlConnUsersPeriod_Type()
)
utmTrapCtrlConnUsersPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmTrapCtrlConnUsersPeriod.setStatus("mandatory")
_UtmTrapCtrlConnUsersLimit_Type = Integer32
_UtmTrapCtrlConnUsersLimit_Object = MibScalar
utmTrapCtrlConnUsersLimit = _UtmTrapCtrlConnUsersLimit_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 4, 10),
    _UtmTrapCtrlConnUsersLimit_Type()
)
utmTrapCtrlConnUsersLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmTrapCtrlConnUsersLimit.setStatus("mandatory")
_UtmTrapCtrlActiveTasksPeriod_Type = Integer32
_UtmTrapCtrlActiveTasksPeriod_Object = MibScalar
utmTrapCtrlActiveTasksPeriod = _UtmTrapCtrlActiveTasksPeriod_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 4, 11),
    _UtmTrapCtrlActiveTasksPeriod_Type()
)
utmTrapCtrlActiveTasksPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmTrapCtrlActiveTasksPeriod.setStatus("mandatory")
_UtmTrapCtrlActiveTasksLimit_Type = Integer32
_UtmTrapCtrlActiveTasksLimit_Object = MibScalar
utmTrapCtrlActiveTasksLimit = _UtmTrapCtrlActiveTasksLimit_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 4, 12),
    _UtmTrapCtrlActiveTasksLimit_Type()
)
utmTrapCtrlActiveTasksLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmTrapCtrlActiveTasksLimit.setStatus("mandatory")
_UtmTrapCtrlCacheHitPeriod_Type = Integer32
_UtmTrapCtrlCacheHitPeriod_Object = MibScalar
utmTrapCtrlCacheHitPeriod = _UtmTrapCtrlCacheHitPeriod_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 4, 13),
    _UtmTrapCtrlCacheHitPeriod_Type()
)
utmTrapCtrlCacheHitPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmTrapCtrlCacheHitPeriod.setStatus("mandatory")
_UtmTrapCtrlCacheHitLimit_Type = Integer32
_UtmTrapCtrlCacheHitLimit_Object = MibScalar
utmTrapCtrlCacheHitLimit = _UtmTrapCtrlCacheHitLimit_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 4, 14),
    _UtmTrapCtrlCacheHitLimit_Type()
)
utmTrapCtrlCacheHitLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmTrapCtrlCacheHitLimit.setStatus("mandatory")
_UtmTrapCtrlPoolSizePeriod_Type = Integer32
_UtmTrapCtrlPoolSizePeriod_Object = MibScalar
utmTrapCtrlPoolSizePeriod = _UtmTrapCtrlPoolSizePeriod_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 4, 15),
    _UtmTrapCtrlPoolSizePeriod_Type()
)
utmTrapCtrlPoolSizePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmTrapCtrlPoolSizePeriod.setStatus("mandatory")
_UtmTrapCtrlPoolSizeLimit_Type = Integer32
_UtmTrapCtrlPoolSizeLimit_Object = MibScalar
utmTrapCtrlPoolSizeLimit = _UtmTrapCtrlPoolSizeLimit_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 4, 16),
    _UtmTrapCtrlPoolSizeLimit_Type()
)
utmTrapCtrlPoolSizeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmTrapCtrlPoolSizeLimit.setStatus("mandatory")
_UtmTrapCtrlTclWaitMsgsPeriod_Type = Integer32
_UtmTrapCtrlTclWaitMsgsPeriod_Object = MibScalar
utmTrapCtrlTclWaitMsgsPeriod = _UtmTrapCtrlTclWaitMsgsPeriod_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 4, 17),
    _UtmTrapCtrlTclWaitMsgsPeriod_Type()
)
utmTrapCtrlTclWaitMsgsPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmTrapCtrlTclWaitMsgsPeriod.setStatus("mandatory")
_UtmTrapCtrlTclWaitMsgsLimit_Type = Integer32
_UtmTrapCtrlTclWaitMsgsLimit_Object = MibScalar
utmTrapCtrlTclWaitMsgsLimit = _UtmTrapCtrlTclWaitMsgsLimit_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 4, 18),
    _UtmTrapCtrlTclWaitMsgsLimit_Type()
)
utmTrapCtrlTclWaitMsgsLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmTrapCtrlTclWaitMsgsLimit.setStatus("mandatory")
_UtmTrapCtrlLtermWaitOutMsgsPeriod_Type = Integer32
_UtmTrapCtrlLtermWaitOutMsgsPeriod_Object = MibScalar
utmTrapCtrlLtermWaitOutMsgsPeriod = _UtmTrapCtrlLtermWaitOutMsgsPeriod_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 4, 19),
    _UtmTrapCtrlLtermWaitOutMsgsPeriod_Type()
)
utmTrapCtrlLtermWaitOutMsgsPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmTrapCtrlLtermWaitOutMsgsPeriod.setStatus("mandatory")
_UtmTrapCtrlLtermWaitOutMsgsLimit_Type = Integer32
_UtmTrapCtrlLtermWaitOutMsgsLimit_Object = MibScalar
utmTrapCtrlLtermWaitOutMsgsLimit = _UtmTrapCtrlLtermWaitOutMsgsLimit_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 4, 20),
    _UtmTrapCtrlLtermWaitOutMsgsLimit_Type()
)
utmTrapCtrlLtermWaitOutMsgsLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    utmTrapCtrlLtermWaitOutMsgsLimit.setStatus("mandatory")

# Managed Objects groups


# Notification objects

utmApplAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 0, 1)
)
if mibBuilder.loadTexts:
    utmApplAborted.setStatus(
        ""
    )

utmApplPENDER = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 0, 2)
)
if mibBuilder.loadTexts:
    utmApplPENDER.setStatus(
        ""
    )

utmApplDeadlock = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 0, 3)
)
if mibBuilder.loadTexts:
    utmApplDeadlock.setStatus(
        ""
    )

utmApplUserSecurityViolations = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 0, 4)
)
if mibBuilder.loadTexts:
    utmApplUserSecurityViolations.setStatus(
        ""
    )

utmApplConnectionLosses = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 0, 5)
)
if mibBuilder.loadTexts:
    utmApplConnectionLosses.setStatus(
        ""
    )

utmApplConnectedUsers = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 0, 6)
)
if mibBuilder.loadTexts:
    utmApplConnectedUsers.setStatus(
        ""
    )

utmApplActiveTasks = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 0, 7)
)
if mibBuilder.loadTexts:
    utmApplActiveTasks.setStatus(
        ""
    )

utmApplCacheHits = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 0, 8)
)
if mibBuilder.loadTexts:
    utmApplCacheHits.setStatus(
        ""
    )

utmApplPoolSize = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 0, 9)
)
if mibBuilder.loadTexts:
    utmApplPoolSize.setStatus(
        ""
    )

utmApplTacclassWaitMsgs = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 0, 10)
)
if mibBuilder.loadTexts:
    utmApplTacclassWaitMsgs.setStatus(
        ""
    )

utmApplLtermWaitOutpMsgs = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 19, 3, 0, 11)
)
if mibBuilder.loadTexts:
    utmApplLtermWaitOutpMsgs.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UTM-MIB",
    **{"sni": sni,
       "sniProductMibs": sniProductMibs,
       "sniUTM": sniUTM,
       "utmApplTabNum": utmApplTabNum,
       "utmApplTable": utmApplTable,
       "utmApplEntry": utmApplEntry,
       "utmApplIndex": utmApplIndex,
       "utmApplName": utmApplName,
       "utmApplStatus": utmApplStatus,
       "utmApplSharedMemKey": utmApplSharedMemKey,
       "utmApplSharedMemSegSize": utmApplSharedMemSegSize,
       "utmApplSemId": utmApplSemId,
       "utmApplHomeDir": utmApplHomeDir,
       "utmApplicationData": utmApplicationData,
       "utmApplAborted": utmApplAborted,
       "utmApplPENDER": utmApplPENDER,
       "utmApplDeadlock": utmApplDeadlock,
       "utmApplUserSecurityViolations": utmApplUserSecurityViolations,
       "utmApplConnectionLosses": utmApplConnectionLosses,
       "utmApplConnectedUsers": utmApplConnectedUsers,
       "utmApplActiveTasks": utmApplActiveTasks,
       "utmApplCacheHits": utmApplCacheHits,
       "utmApplPoolSize": utmApplPoolSize,
       "utmApplTacclassWaitMsgs": utmApplTacclassWaitMsgs,
       "utmApplLtermWaitOutpMsgs": utmApplLtermWaitOutpMsgs,
       "utmMainData": utmMainData,
       "utmMainApplName": utmMainApplName,
       "utmMainBCAMAppl": utmMainBCAMAppl,
       "utmMainUTMversion": utmMainUTMversion,
       "utmMainApplStartStop": utmMainApplStartStop,
       "utmMainApplHomeDir": utmMainApplHomeDir,
       "utmMainSubagentVersion": utmMainSubagentVersion,
       "utmStatData": utmStatData,
       "utmStatStartDateAndTime": utmStatStartDateAndTime,
       "utmStatStartDateAndTimeString": utmStatStartDateAndTimeString,
       "utmStatTermInMsgs": utmStatTermInMsgs,
       "utmStatTermOutMsgs": utmStatTermOutMsgs,
       "utmStatCurrTasks": utmStatCurrTasks,
       "utmStatConnUsers": utmStatConnUsers,
       "utmStatOpenDialConv": utmStatOpenDialConv,
       "utmStatOpenAsynConv": utmStatOpenAsynConv,
       "utmStatDialTAperSec": utmStatDialTAperSec,
       "utmStatAsynTAperSec": utmStatAsynTAperSec,
       "utmStatDialStepSec": utmStatDialStepSec,
       "utmStatMaxPoolSize": utmStatMaxPoolSize,
       "utmStatActPoolSize": utmStatActPoolSize,
       "utmStatAvgPoolSize": utmStatAvgPoolSize,
       "utmStatCacheHitRate": utmStatCacheHitRate,
       "utmStatCacheWaits": utmStatCacheWaits,
       "utmStatUnprocAtacs": utmStatUnprocAtacs,
       "utmStatUnprocPrints": utmStatUnprocPrints,
       "utmStatWaitDPUTs": utmStatWaitDPUTs,
       "utmStatAbTermConv": utmStatAbTermConv,
       "utmStatResourcWaits": utmStatResourcWaits,
       "utmStatDeadlocks": utmStatDeadlocks,
       "utmStatPeriodWrites": utmStatPeriodWrites,
       "utmStatPagesPWrite": utmStatPagesPWrite,
       "utmStatLogWrites": utmStatLogWrites,
       "utmStatActJR": utmStatActJR,
       "utmStatMaxJR": utmStatMaxJR,
       "utmSyspData": utmSyspData,
       "utmSyspAccount": utmSyspAccount,
       "utmSyspCalcAccount": utmSyspCalcAccount,
       "utmSyspSM2": utmSyspSM2,
       "utmSyspKDCMON": utmSyspKDCMON,
       "utmSyspTestmode": utmSyspTestmode,
       "utmSyspMaxPagRate": utmSyspMaxPagRate,
       "utmSyspProgFGG": utmSyspProgFGG,
       "utmSyspTermWait": utmSyspTermWait,
       "utmSyspUsLogFGG": utmSyspUsLogFGG,
       "utmSyspResWaitTA": utmSyspResWaitTA,
       "utmSyspMaxTasks": utmSyspMaxTasks,
       "utmSyspResWaitPr": utmSyspResWaitPr,
       "utmSyspCurrTasks": utmSyspCurrTasks,
       "utmSyspConRTime": utmSyspConRTime,
       "utmSyspMaxAsynTasks": utmSyspMaxAsynTasks,
       "utmSyspLogAckwait": utmSyspLogAckwait,
       "utmSyspPTCTime": utmSyspPTCTime,
       "utmSyspConcTime": utmSyspConcTime,
       "utmSyspPGWTTime": utmSyspPGWTTime,
       "utmSyspTasksWaitPGWT": utmSyspTasksWaitPGWT,
       "utmSyspTasksinPGWT": utmSyspTasksinPGWT,
       "utmPtermData": utmPtermData,
       "utmPtermTabNum": utmPtermTabNum,
       "utmPtermTable": utmPtermTable,
       "utmPtermEntry": utmPtermEntry,
       "utmPtermIndex": utmPtermIndex,
       "utmPtermName": utmPtermName,
       "utmPtermProname": utmPtermProname,
       "utmPtermLterm": utmPtermLterm,
       "utmPtermBCAMAppl": utmPtermBCAMAppl,
       "utmPtermPtyp": utmPtermPtyp,
       "utmPtermStatus": utmPtermStatus,
       "utmPtermConnected": utmPtermConnected,
       "utmPtermConnectStatus": utmPtermConnectStatus,
       "utmPtermConnectForced": utmPtermConnectForced,
       "utmPtermConnectMultiplexed": utmPtermConnectMultiplexed,
       "utmPtermConTime": utmPtermConTime,
       "utmPtermLett": utmPtermLett,
       "utmPtermConb": utmPtermConb,
       "utmLtermData": utmLtermData,
       "utmLtermTabNum": utmLtermTabNum,
       "utmLtermTable": utmLtermTable,
       "utmLtermEntry": utmLtermEntry,
       "utmLtermIndex": utmLtermIndex,
       "utmLtermName": utmLtermName,
       "utmLtermPterm": utmLtermPterm,
       "utmLtermUser": utmLtermUser,
       "utmLtermKset": utmLtermKset,
       "utmLtermLock": utmLtermLock,
       "utmLtermUsageType": utmLtermUsageType,
       "utmLtermUsageBundle": utmLtermUsageBundle,
       "utmLtermUsageTermPool": utmLtermUsageTermPool,
       "utmLtermStatus": utmLtermStatus,
       "utmLtermOutq": utmLtermOutq,
       "utmLtermInCnt": utmLtermInCnt,
       "utmLtermSecCnt": utmLtermSecCnt,
       "utmTacData": utmTacData,
       "utmTacTabNum": utmTacTabNum,
       "utmTacTable": utmTacTable,
       "utmTacEntry": utmTacEntry,
       "utmTacIndex": utmTacIndex,
       "utmTacName": utmTacName,
       "utmTacLock": utmTacLock,
       "utmTacStatus": utmTacStatus,
       "utmTacTcl": utmTacTcl,
       "utmTacInq": utmTacInq,
       "utmTacUsed": utmTacUsed,
       "utmTacError": utmTacError,
       "utmTacDbcnt": utmTacDbcnt,
       "utmTacElap": utmTacElap,
       "utmTacDbElap": utmTacDbElap,
       "utmTacCpu": utmTacCpu,
       "utmTacclassData": utmTacclassData,
       "utmTacclassTable": utmTacclassTable,
       "utmTacclassEntry": utmTacclassEntry,
       "utmTacclassNumber": utmTacclassNumber,
       "utmTacclassTasks": utmTacclassTasks,
       "utmTacclassWtMesg": utmTacclassWtMesg,
       "utmTacclassAvgWtTime": utmTacclassAvgWtTime,
       "utmTacclassPGWT": utmTacclassPGWT,
       "utmUserData": utmUserData,
       "utmUserTabNum": utmUserTabNum,
       "utmUserTable": utmUserTable,
       "utmUserEntry": utmUserEntry,
       "utmUserIndex": utmUserIndex,
       "utmUserName": utmUserName,
       "utmUserKset": utmUserKset,
       "utmUserStatus": utmUserStatus,
       "utmUserInVg": utmUserInVg,
       "utmUserNrTacs": utmUserNrTacs,
       "utmUserCpuTime": utmUserCpuTime,
       "utmUserSecCnt": utmUserSecCnt,
       "utmUserLterm": utmUserLterm,
       "utmConData": utmConData,
       "utmConTabNum": utmConTabNum,
       "utmConTable": utmConTable,
       "utmConEntry": utmConEntry,
       "utmConIndex": utmConIndex,
       "utmConName": utmConName,
       "utmConProname": utmConProname,
       "utmConLpap": utmConLpap,
       "utmConBcamAppl": utmConBcamAppl,
       "utmConStatus": utmConStatus,
       "utmConConnected": utmConConnected,
       "utmConConnectStatus": utmConConnectStatus,
       "utmConConTime": utmConConTime,
       "utmConLett": utmConLett,
       "utmConConb": utmConConb,
       "utmLpapData": utmLpapData,
       "utmLpapTabNum": utmLpapTabNum,
       "utmLpapTable": utmLpapTable,
       "utmLpapEntry": utmLpapEntry,
       "utmLpapIndex": utmLpapIndex,
       "utmLpapName": utmLpapName,
       "utmLpapKset": utmLpapKset,
       "utmLpapStatus": utmLpapStatus,
       "utmLpapQuiet": utmLpapQuiet,
       "utmLpapOutq": utmLpapOutq,
       "utmLpapIdleTime": utmLpapIdleTime,
       "utmPoolData": utmPoolData,
       "utmPoolTabNum": utmPoolTabNum,
       "utmPoolTable": utmPoolTable,
       "utmPoolEntry": utmPoolEntry,
       "utmPoolIndex": utmPoolIndex,
       "utmPoolProname": utmPoolProname,
       "utmPoolBcamAppl": utmPoolBcamAppl,
       "utmPoolPtype": utmPoolPtype,
       "utmPoolStations": utmPoolStations,
       "utmPoolStatusOn": utmPoolStatusOn,
       "utmPoolActCon": utmPoolActCon,
       "utmPoolMaxCon": utmPoolMaxCon,
       "utmPoolKset": utmPoolKset,
       "utmPoolLock": utmPoolLock,
       "utmLsesData": utmLsesData,
       "utmLsesTabNum": utmLsesTabNum,
       "utmLsesTable": utmLsesTable,
       "utmLsesEntry": utmLsesEntry,
       "utmLsesIndex": utmLsesIndex,
       "utmLsesName": utmLsesName,
       "utmLsesRses": utmLsesRses,
       "utmLsesLpap": utmLsesLpap,
       "utmLsesCon": utmLsesCon,
       "utmLsesProname": utmLsesProname,
       "utmLsesBcamAppl": utmLsesBcamAppl,
       "utmLsesAgUser": utmLsesAgUser,
       "utmLtacData": utmLtacData,
       "utmLtacTabNum": utmLtacTabNum,
       "utmLtacTable": utmLtacTable,
       "utmLtacEntry": utmLtacEntry,
       "utmLtacIndex": utmLtacIndex,
       "utmLtacName": utmLtacName,
       "utmLtacLock": utmLtacLock,
       "utmLtacStatus": utmLtacStatus,
       "utmLtacRtac": utmLtacRtac,
       "utmLtacLpap": utmLtacLpap,
       "utmLtacAccessWait": utmLtacAccessWait,
       "utmLtacReplyWait": utmLtacReplyWait,
       "utmLtacUsed": utmLtacUsed,
       "utmOsiAssData": utmOsiAssData,
       "utmOsiAssTabNum": utmOsiAssTabNum,
       "utmOsiAssTable": utmOsiAssTable,
       "utmOsiAssEntry": utmOsiAssEntry,
       "utmOsiAssIndex": utmOsiAssIndex,
       "utmOsiAssName": utmOsiAssName,
       "utmOsiAssOsiLpap": utmOsiAssOsiLpap,
       "utmOsiAssOsiCon": utmOsiAssOsiCon,
       "utmOsiAssAgUser": utmOsiAssAgUser,
       "utmOsiAssConTime": utmOsiAssConTime,
       "utmOsiAssLetters": utmOsiAssLetters,
       "utmOsiConData": utmOsiConData,
       "utmOsiConTabNum": utmOsiConTabNum,
       "utmOsiConTable": utmOsiConTable,
       "utmOsiConEntry": utmOsiConEntry,
       "utmOsiConIndex": utmOsiConIndex,
       "utmOsiConName": utmOsiConName,
       "utmOsiConOsiLpap": utmOsiConOsiLpap,
       "utmOsiConTsel": utmOsiConTsel,
       "utmOsiConNsel": utmOsiConNsel,
       "utmOsiConAccPnt": utmOsiConAccPnt,
       "utmOsiConActive": utmOsiConActive,
       "utmOsiLpapData": utmOsiLpapData,
       "utmOsiLpapTabNum": utmOsiLpapTabNum,
       "utmOsiLpapTable": utmOsiLpapTable,
       "utmOsiLpapEntry": utmOsiLpapEntry,
       "utmOsiLpapIndex": utmOsiLpapIndex,
       "utmOsiLpapName": utmOsiLpapName,
       "utmOsiLpapKset": utmOsiLpapKset,
       "utmOsiLpapStatus": utmOsiLpapStatus,
       "utmOsiLpapQuiet": utmOsiLpapQuiet,
       "utmOsiLpapOutq": utmOsiLpapOutq,
       "utmOsiLpapIdleTime": utmOsiLpapIdleTime,
       "utmOsiLpapOsiCon": utmOsiLpapOsiCon,
       "utmOsiLpapAssoc": utmOsiLpapAssoc,
       "utmOsiLpapConnect": utmOsiLpapConnect,
       "utmOsiLpapAutoCon": utmOsiLpapAutoCon,
       "utmMiscData": utmMiscData,
       "utmTrapControl": utmTrapControl,
       "utmTrapCtrlCheckCaseNOW": utmTrapCtrlCheckCaseNOW,
       "utmTrapCtrlAbortedPeriod": utmTrapCtrlAbortedPeriod,
       "utmTrapCtrlPENDERPeriod": utmTrapCtrlPENDERPeriod,
       "utmTrapCtrlDeadlockPeriod": utmTrapCtrlDeadlockPeriod,
       "utmTrapCtrlSecurViolPeriod": utmTrapCtrlSecurViolPeriod,
       "utmTrapCtrlSecurViolLimit": utmTrapCtrlSecurViolLimit,
       "utmTrapCtrlConnLossPeriod": utmTrapCtrlConnLossPeriod,
       "utmTrapCtrlConnLossLimit": utmTrapCtrlConnLossLimit,
       "utmTrapCtrlConnUsersPeriod": utmTrapCtrlConnUsersPeriod,
       "utmTrapCtrlConnUsersLimit": utmTrapCtrlConnUsersLimit,
       "utmTrapCtrlActiveTasksPeriod": utmTrapCtrlActiveTasksPeriod,
       "utmTrapCtrlActiveTasksLimit": utmTrapCtrlActiveTasksLimit,
       "utmTrapCtrlCacheHitPeriod": utmTrapCtrlCacheHitPeriod,
       "utmTrapCtrlCacheHitLimit": utmTrapCtrlCacheHitLimit,
       "utmTrapCtrlPoolSizePeriod": utmTrapCtrlPoolSizePeriod,
       "utmTrapCtrlPoolSizeLimit": utmTrapCtrlPoolSizeLimit,
       "utmTrapCtrlTclWaitMsgsPeriod": utmTrapCtrlTclWaitMsgsPeriod,
       "utmTrapCtrlTclWaitMsgsLimit": utmTrapCtrlTclWaitMsgsLimit,
       "utmTrapCtrlLtermWaitOutMsgsPeriod": utmTrapCtrlLtermWaitOutMsgsPeriod,
       "utmTrapCtrlLtermWaitOutMsgsLimit": utmTrapCtrlLtermWaitOutMsgsLimit}
)
