# SNMP MIB module (SC5002-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SC5002-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:48 2024
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

(SCinstance,) = mibBuilder.importSymbols(
    "GDCMACRO-MIB",
    "SCinstance")

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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Gdc_ObjectIdentity = ObjectIdentity
gdc = _Gdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498)
)
_Dsx1_ObjectIdentity = ObjectIdentity
dsx1 = _Dsx1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6)
)
_Sc5002_ObjectIdentity = ObjectIdentity
sc5002 = _Sc5002_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 8)
)
_Sc5002Version_ObjectIdentity = ObjectIdentity
sc5002Version = _Sc5002Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 1)
)


class _Sc5002MIBversion_Type(DisplayString):
    """Custom type sc5002MIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Sc5002MIBversion_Type.__name__ = "DisplayString"
_Sc5002MIBversion_Object = MibScalar
sc5002MIBversion = _Sc5002MIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 1, 1),
    _Sc5002MIBversion_Type()
)
sc5002MIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002MIBversion.setStatus("mandatory")
_Sc5002VersionTable_Object = MibTable
sc5002VersionTable = _Sc5002VersionTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 1, 2)
)
if mibBuilder.loadTexts:
    sc5002VersionTable.setStatus("mandatory")
_Sc5002VersionEntry_Object = MibTableRow
sc5002VersionEntry = _Sc5002VersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 1, 2, 1)
)
sc5002VersionEntry.setIndexNames(
    (0, "SC5002-MIB", "sc5002VersionIndex"),
)
if mibBuilder.loadTexts:
    sc5002VersionEntry.setStatus("mandatory")
_Sc5002VersionIndex_Type = SCinstance
_Sc5002VersionIndex_Object = MibTableColumn
sc5002VersionIndex = _Sc5002VersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 1, 2, 1, 1),
    _Sc5002VersionIndex_Type()
)
sc5002VersionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002VersionIndex.setStatus("mandatory")


class _Sc5002ActiveFirmwareRev_Type(DisplayString):
    """Custom type sc5002ActiveFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Sc5002ActiveFirmwareRev_Type.__name__ = "DisplayString"
_Sc5002ActiveFirmwareRev_Object = MibTableColumn
sc5002ActiveFirmwareRev = _Sc5002ActiveFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 1, 2, 1, 2),
    _Sc5002ActiveFirmwareRev_Type()
)
sc5002ActiveFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002ActiveFirmwareRev.setStatus("mandatory")


class _Sc5002StoredFirmwareRev_Type(DisplayString):
    """Custom type sc5002StoredFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Sc5002StoredFirmwareRev_Type.__name__ = "DisplayString"
_Sc5002StoredFirmwareRev_Object = MibTableColumn
sc5002StoredFirmwareRev = _Sc5002StoredFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 1, 2, 1, 3),
    _Sc5002StoredFirmwareRev_Type()
)
sc5002StoredFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002StoredFirmwareRev.setStatus("mandatory")


class _Sc5002BootRev_Type(DisplayString):
    """Custom type sc5002BootRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Sc5002BootRev_Type.__name__ = "DisplayString"
_Sc5002BootRev_Object = MibTableColumn
sc5002BootRev = _Sc5002BootRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 1, 2, 1, 4),
    _Sc5002BootRev_Type()
)
sc5002BootRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002BootRev.setStatus("mandatory")


class _Sc5002StoredFirmwareStatus_Type(Integer32):
    """Custom type sc5002StoredFirmwareStatus based on Integer32"""
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
        *(("statBadUnZip", 6),
          ("statBlank", 1),
          ("statCheckSumBad", 4),
          ("statDownLoading", 2),
          ("statOK", 3),
          ("statUnZipping", 5))
    )


_Sc5002StoredFirmwareStatus_Type.__name__ = "Integer32"
_Sc5002StoredFirmwareStatus_Object = MibTableColumn
sc5002StoredFirmwareStatus = _Sc5002StoredFirmwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 1, 2, 1, 5),
    _Sc5002StoredFirmwareStatus_Type()
)
sc5002StoredFirmwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002StoredFirmwareStatus.setStatus("mandatory")


class _Sc5002SwitchActiveFirmware_Type(Integer32):
    """Custom type sc5002SwitchActiveFirmware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switchActive", 2),
          ("switchNorm", 1))
    )


_Sc5002SwitchActiveFirmware_Type.__name__ = "Integer32"
_Sc5002SwitchActiveFirmware_Object = MibTableColumn
sc5002SwitchActiveFirmware = _Sc5002SwitchActiveFirmware_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 1, 2, 1, 6),
    _Sc5002SwitchActiveFirmware_Type()
)
sc5002SwitchActiveFirmware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5002SwitchActiveFirmware.setStatus("mandatory")


class _Sc5002DownloadingMode_Type(Integer32):
    """Custom type sc5002DownloadingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disableAll", 1),
          ("enableAndSwitch", 3),
          ("enableAndWait", 2))
    )


_Sc5002DownloadingMode_Type.__name__ = "Integer32"
_Sc5002DownloadingMode_Object = MibTableColumn
sc5002DownloadingMode = _Sc5002DownloadingMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 1, 2, 1, 7),
    _Sc5002DownloadingMode_Type()
)
sc5002DownloadingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5002DownloadingMode.setStatus("mandatory")


class _Sc5002FirmwareRev_Type(DisplayString):
    """Custom type sc5002FirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Sc5002FirmwareRev_Type.__name__ = "DisplayString"
_Sc5002FirmwareRev_Object = MibTableColumn
sc5002FirmwareRev = _Sc5002FirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 1, 2, 1, 8),
    _Sc5002FirmwareRev_Type()
)
sc5002FirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002FirmwareRev.setStatus("mandatory")
_Sc5002NetworkCfg_ObjectIdentity = ObjectIdentity
sc5002NetworkCfg = _Sc5002NetworkCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 2)
)
_Sc5002NetworkCfgTable_Object = MibTable
sc5002NetworkCfgTable = _Sc5002NetworkCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 2, 1)
)
if mibBuilder.loadTexts:
    sc5002NetworkCfgTable.setStatus("mandatory")
_Sc5002NetworkCfgEntry_Object = MibTableRow
sc5002NetworkCfgEntry = _Sc5002NetworkCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 2, 1, 1)
)
sc5002NetworkCfgEntry.setIndexNames(
    (0, "SC5002-MIB", "sc5002NetworkCfgIndex"),
)
if mibBuilder.loadTexts:
    sc5002NetworkCfgEntry.setStatus("mandatory")
_Sc5002NetworkCfgIndex_Type = SCinstance
_Sc5002NetworkCfgIndex_Object = MibTableColumn
sc5002NetworkCfgIndex = _Sc5002NetworkCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 2, 1, 1, 1),
    _Sc5002NetworkCfgIndex_Type()
)
sc5002NetworkCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002NetworkCfgIndex.setStatus("mandatory")


class _Sc5002E1SignalingMode_Type(Integer32):
    """Custom type sc5002E1SignalingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("assocChanSigNoCRC4", 2),
          ("assocChanSigWithCRC4", 1))
    )


_Sc5002E1SignalingMode_Type.__name__ = "Integer32"
_Sc5002E1SignalingMode_Object = MibTableColumn
sc5002E1SignalingMode = _Sc5002E1SignalingMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 2, 1, 1, 2),
    _Sc5002E1SignalingMode_Type()
)
sc5002E1SignalingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5002E1SignalingMode.setStatus("mandatory")
_Sc5002Alarms_ObjectIdentity = ObjectIdentity
sc5002Alarms = _Sc5002Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3)
)
_Sc5002AlarmData_ObjectIdentity = ObjectIdentity
sc5002AlarmData = _Sc5002AlarmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 1)
)
_Sc5002NoResponse_ObjectIdentity = ObjectIdentity
sc5002NoResponse = _Sc5002NoResponse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 1, 1)
)
_Sc5002DiagRxErr_ObjectIdentity = ObjectIdentity
sc5002DiagRxErr = _Sc5002DiagRxErr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 1, 2)
)
_Sc5002PowerUp_ObjectIdentity = ObjectIdentity
sc5002PowerUp = _Sc5002PowerUp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 1, 3)
)
_Sc5002NvRamCorrupt_ObjectIdentity = ObjectIdentity
sc5002NvRamCorrupt = _Sc5002NvRamCorrupt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 1, 4)
)
_Sc5002UnitFailure_ObjectIdentity = ObjectIdentity
sc5002UnitFailure = _Sc5002UnitFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 1, 5)
)
_Sc5002TimingLoss_ObjectIdentity = ObjectIdentity
sc5002TimingLoss = _Sc5002TimingLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 1, 6)
)
_Sc5002LossOfSignal_ObjectIdentity = ObjectIdentity
sc5002LossOfSignal = _Sc5002LossOfSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 1, 7)
)
_Sc5002LossOfFrame_ObjectIdentity = ObjectIdentity
sc5002LossOfFrame = _Sc5002LossOfFrame_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 1, 8)
)
_Sc5002AlarmIndSignal_ObjectIdentity = ObjectIdentity
sc5002AlarmIndSignal = _Sc5002AlarmIndSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 1, 9)
)
_Sc5002FallbackTimingActive_ObjectIdentity = ObjectIdentity
sc5002FallbackTimingActive = _Sc5002FallbackTimingActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 1, 10)
)
_Sc5002NearEndLnCodeViol_ObjectIdentity = ObjectIdentity
sc5002NearEndLnCodeViol = _Sc5002NearEndLnCodeViol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 1, 11)
)
_Sc5002NearEndErrSec_ObjectIdentity = ObjectIdentity
sc5002NearEndErrSec = _Sc5002NearEndErrSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 1, 12)
)
_Sc5002NearEndBkdBlkErr_ObjectIdentity = ObjectIdentity
sc5002NearEndBkdBlkErr = _Sc5002NearEndBkdBlkErr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 1, 13)
)
_Sc5002NearEndSevErrSec_ObjectIdentity = ObjectIdentity
sc5002NearEndSevErrSec = _Sc5002NearEndSevErrSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 1, 14)
)
_Sc5002NearEndUnavlSec_ObjectIdentity = ObjectIdentity
sc5002NearEndUnavlSec = _Sc5002NearEndUnavlSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 1, 15)
)
_Sc5002FarEndErrSec_ObjectIdentity = ObjectIdentity
sc5002FarEndErrSec = _Sc5002FarEndErrSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 1, 16)
)
_Sc5002FarEndBkdBlkErr_ObjectIdentity = ObjectIdentity
sc5002FarEndBkdBlkErr = _Sc5002FarEndBkdBlkErr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 1, 17)
)
_Sc5002FarEndSevErrSec_ObjectIdentity = ObjectIdentity
sc5002FarEndSevErrSec = _Sc5002FarEndSevErrSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 1, 18)
)
_Sc5002FarEndUnavlSec_ObjectIdentity = ObjectIdentity
sc5002FarEndUnavlSec = _Sc5002FarEndUnavlSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 1, 19)
)
_Sc5002NearEndAlarmCfgTable_Object = MibTable
sc5002NearEndAlarmCfgTable = _Sc5002NearEndAlarmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 2)
)
if mibBuilder.loadTexts:
    sc5002NearEndAlarmCfgTable.setStatus("mandatory")
_Sc5002NearEndAlarmCfgEntry_Object = MibTableRow
sc5002NearEndAlarmCfgEntry = _Sc5002NearEndAlarmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 2, 1)
)
sc5002NearEndAlarmCfgEntry.setIndexNames(
    (0, "SC5002-MIB", "sc5002NearEndAlarmCfgIndex"),
    (0, "SC5002-MIB", "sc5002NearEndAlarmCfgIdentifier"),
)
if mibBuilder.loadTexts:
    sc5002NearEndAlarmCfgEntry.setStatus("mandatory")
_Sc5002NearEndAlarmCfgIndex_Type = SCinstance
_Sc5002NearEndAlarmCfgIndex_Object = MibTableColumn
sc5002NearEndAlarmCfgIndex = _Sc5002NearEndAlarmCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 2, 1, 1),
    _Sc5002NearEndAlarmCfgIndex_Type()
)
sc5002NearEndAlarmCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002NearEndAlarmCfgIndex.setStatus("mandatory")
_Sc5002NearEndAlarmCfgIdentifier_Type = ObjectIdentifier
_Sc5002NearEndAlarmCfgIdentifier_Object = MibTableColumn
sc5002NearEndAlarmCfgIdentifier = _Sc5002NearEndAlarmCfgIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 2, 1, 2),
    _Sc5002NearEndAlarmCfgIdentifier_Type()
)
sc5002NearEndAlarmCfgIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002NearEndAlarmCfgIdentifier.setStatus("mandatory")


class _Sc5002NearEndAlarmWindow_Type(Integer32):
    """Custom type sc5002NearEndAlarmWindow based on Integer32"""
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
        *(("win15min", 3),
          ("win1hr", 4),
          ("win1min", 2),
          ("win24hr", 5),
          ("win30sec", 1))
    )


_Sc5002NearEndAlarmWindow_Type.__name__ = "Integer32"
_Sc5002NearEndAlarmWindow_Object = MibTableColumn
sc5002NearEndAlarmWindow = _Sc5002NearEndAlarmWindow_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 2, 1, 3),
    _Sc5002NearEndAlarmWindow_Type()
)
sc5002NearEndAlarmWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5002NearEndAlarmWindow.setStatus("mandatory")


class _Sc5002NearEndAlarmThreshold_Type(Integer32):
    """Custom type sc5002NearEndAlarmThreshold based on Integer32"""
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
        *(("thr1", 1),
          ("thr10", 3),
          ("thr100", 4),
          ("thr1000", 5),
          ("thr10000", 6),
          ("thr3", 2))
    )


_Sc5002NearEndAlarmThreshold_Type.__name__ = "Integer32"
_Sc5002NearEndAlarmThreshold_Object = MibTableColumn
sc5002NearEndAlarmThreshold = _Sc5002NearEndAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 2, 1, 4),
    _Sc5002NearEndAlarmThreshold_Type()
)
sc5002NearEndAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5002NearEndAlarmThreshold.setStatus("mandatory")
_Sc5002FarEndAlarmCfgTable_Object = MibTable
sc5002FarEndAlarmCfgTable = _Sc5002FarEndAlarmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 3)
)
if mibBuilder.loadTexts:
    sc5002FarEndAlarmCfgTable.setStatus("mandatory")
_Sc5002FarEndAlarmCfgEntry_Object = MibTableRow
sc5002FarEndAlarmCfgEntry = _Sc5002FarEndAlarmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 3, 1)
)
sc5002FarEndAlarmCfgEntry.setIndexNames(
    (0, "SC5002-MIB", "sc5002FarEndAlarmCfgIndex"),
    (0, "SC5002-MIB", "sc5002FarEndAlarmCfgIdentifier"),
)
if mibBuilder.loadTexts:
    sc5002FarEndAlarmCfgEntry.setStatus("mandatory")
_Sc5002FarEndAlarmCfgIndex_Type = SCinstance
_Sc5002FarEndAlarmCfgIndex_Object = MibTableColumn
sc5002FarEndAlarmCfgIndex = _Sc5002FarEndAlarmCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 3, 1, 1),
    _Sc5002FarEndAlarmCfgIndex_Type()
)
sc5002FarEndAlarmCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002FarEndAlarmCfgIndex.setStatus("mandatory")
_Sc5002FarEndAlarmCfgIdentifier_Type = ObjectIdentifier
_Sc5002FarEndAlarmCfgIdentifier_Object = MibTableColumn
sc5002FarEndAlarmCfgIdentifier = _Sc5002FarEndAlarmCfgIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 3, 1, 2),
    _Sc5002FarEndAlarmCfgIdentifier_Type()
)
sc5002FarEndAlarmCfgIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002FarEndAlarmCfgIdentifier.setStatus("mandatory")


class _Sc5002FarEndAlarmWindow_Type(Integer32):
    """Custom type sc5002FarEndAlarmWindow based on Integer32"""
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
        *(("win15min", 3),
          ("win1hr", 4),
          ("win1min", 2),
          ("win24hr", 5),
          ("win30sec", 1))
    )


_Sc5002FarEndAlarmWindow_Type.__name__ = "Integer32"
_Sc5002FarEndAlarmWindow_Object = MibTableColumn
sc5002FarEndAlarmWindow = _Sc5002FarEndAlarmWindow_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 3, 1, 3),
    _Sc5002FarEndAlarmWindow_Type()
)
sc5002FarEndAlarmWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5002FarEndAlarmWindow.setStatus("mandatory")


class _Sc5002FarEndAlarmThreshold_Type(Integer32):
    """Custom type sc5002FarEndAlarmThreshold based on Integer32"""
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
        *(("thr1", 1),
          ("thr10", 3),
          ("thr100", 4),
          ("thr1000", 5),
          ("thr10000", 6),
          ("thr3", 2))
    )


_Sc5002FarEndAlarmThreshold_Type.__name__ = "Integer32"
_Sc5002FarEndAlarmThreshold_Object = MibTableColumn
sc5002FarEndAlarmThreshold = _Sc5002FarEndAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 3, 3, 1, 4),
    _Sc5002FarEndAlarmThreshold_Type()
)
sc5002FarEndAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5002FarEndAlarmThreshold.setStatus("mandatory")
_Sc5002Diagnostics_ObjectIdentity = ObjectIdentity
sc5002Diagnostics = _Sc5002Diagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 4)
)
_Sc5002DiagTable_Object = MibTable
sc5002DiagTable = _Sc5002DiagTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 4, 1)
)
if mibBuilder.loadTexts:
    sc5002DiagTable.setStatus("mandatory")
_Sc5002DiagEntry_Object = MibTableRow
sc5002DiagEntry = _Sc5002DiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 4, 1, 1)
)
sc5002DiagEntry.setIndexNames(
    (0, "SC5002-MIB", "sc5002DiagIndex"),
)
if mibBuilder.loadTexts:
    sc5002DiagEntry.setStatus("mandatory")
_Sc5002DiagIndex_Type = SCinstance
_Sc5002DiagIndex_Object = MibTableColumn
sc5002DiagIndex = _Sc5002DiagIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 4, 1, 1, 1),
    _Sc5002DiagIndex_Type()
)
sc5002DiagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002DiagIndex.setStatus("mandatory")


class _Sc5002LoopbackConfig_Type(Integer32):
    """Custom type sc5002LoopbackConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lineLoopBack", 2),
          ("noLoopBack", 1),
          ("unitTest", 3))
    )


_Sc5002LoopbackConfig_Type.__name__ = "Integer32"
_Sc5002LoopbackConfig_Object = MibTableColumn
sc5002LoopbackConfig = _Sc5002LoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 4, 1, 1, 2),
    _Sc5002LoopbackConfig_Type()
)
sc5002LoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5002LoopbackConfig.setStatus("mandatory")


class _Sc5002TestResult_Type(Integer32):
    """Custom type sc5002TestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("pass", 1))
    )


_Sc5002TestResult_Type.__name__ = "Integer32"
_Sc5002TestResult_Object = MibTableColumn
sc5002TestResult = _Sc5002TestResult_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 4, 1, 1, 3),
    _Sc5002TestResult_Type()
)
sc5002TestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002TestResult.setStatus("mandatory")
_Sc5002Maintenance_ObjectIdentity = ObjectIdentity
sc5002Maintenance = _Sc5002Maintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 5)
)
_Sc5002MaintenanceTable_Object = MibTable
sc5002MaintenanceTable = _Sc5002MaintenanceTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 5, 1)
)
if mibBuilder.loadTexts:
    sc5002MaintenanceTable.setStatus("mandatory")
_Sc5002MaintenanceEntry_Object = MibTableRow
sc5002MaintenanceEntry = _Sc5002MaintenanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 5, 1, 1)
)
sc5002MaintenanceEntry.setIndexNames(
    (0, "SC5002-MIB", "sc5002MaintenanceLineIndex"),
)
if mibBuilder.loadTexts:
    sc5002MaintenanceEntry.setStatus("mandatory")
_Sc5002MaintenanceLineIndex_Type = SCinstance
_Sc5002MaintenanceLineIndex_Object = MibTableColumn
sc5002MaintenanceLineIndex = _Sc5002MaintenanceLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 5, 1, 1, 1),
    _Sc5002MaintenanceLineIndex_Type()
)
sc5002MaintenanceLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002MaintenanceLineIndex.setStatus("mandatory")


class _Sc5002SoftReset_Type(Integer32):
    """Custom type sc5002SoftReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norm", 2),
          ("reset", 1))
    )


_Sc5002SoftReset_Type.__name__ = "Integer32"
_Sc5002SoftReset_Object = MibTableColumn
sc5002SoftReset = _Sc5002SoftReset_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 5, 1, 1, 2),
    _Sc5002SoftReset_Type()
)
sc5002SoftReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5002SoftReset.setStatus("mandatory")


class _Sc5002DefaultInit_Type(Integer32):
    """Custom type sc5002DefaultInit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("factoryDefault", 1),
          ("normal", 2))
    )


_Sc5002DefaultInit_Type.__name__ = "Integer32"
_Sc5002DefaultInit_Object = MibTableColumn
sc5002DefaultInit = _Sc5002DefaultInit_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 5, 1, 1, 3),
    _Sc5002DefaultInit_Type()
)
sc5002DefaultInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5002DefaultInit.setStatus("mandatory")


class _Sc5002NearEndResetStats_Type(Integer32):
    """Custom type sc5002NearEndResetStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norm", 1),
          ("reset", 2))
    )


_Sc5002NearEndResetStats_Type.__name__ = "Integer32"
_Sc5002NearEndResetStats_Object = MibTableColumn
sc5002NearEndResetStats = _Sc5002NearEndResetStats_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 5, 1, 1, 4),
    _Sc5002NearEndResetStats_Type()
)
sc5002NearEndResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5002NearEndResetStats.setStatus("mandatory")


class _Sc5002NearEndStatLastInitialized_Type(Integer32):
    """Custom type sc5002NearEndStatLastInitialized based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sc5002NearEndStatLastInitialized_Type.__name__ = "Integer32"
_Sc5002NearEndStatLastInitialized_Object = MibTableColumn
sc5002NearEndStatLastInitialized = _Sc5002NearEndStatLastInitialized_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 5, 1, 1, 5),
    _Sc5002NearEndStatLastInitialized_Type()
)
sc5002NearEndStatLastInitialized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002NearEndStatLastInitialized.setStatus("mandatory")


class _Sc5002FarEndResetStats_Type(Integer32):
    """Custom type sc5002FarEndResetStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norm", 1),
          ("reset", 2))
    )


_Sc5002FarEndResetStats_Type.__name__ = "Integer32"
_Sc5002FarEndResetStats_Object = MibTableColumn
sc5002FarEndResetStats = _Sc5002FarEndResetStats_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 5, 1, 1, 6),
    _Sc5002FarEndResetStats_Type()
)
sc5002FarEndResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5002FarEndResetStats.setStatus("mandatory")


class _Sc5002FarEndStatLastInitialized_Type(Integer32):
    """Custom type sc5002FarEndStatLastInitialized based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sc5002FarEndStatLastInitialized_Type.__name__ = "Integer32"
_Sc5002FarEndStatLastInitialized_Object = MibTableColumn
sc5002FarEndStatLastInitialized = _Sc5002FarEndStatLastInitialized_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 5, 1, 1, 7),
    _Sc5002FarEndStatLastInitialized_Type()
)
sc5002FarEndStatLastInitialized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002FarEndStatLastInitialized.setStatus("mandatory")


class _Sc5002LedStatus_Type(OctetString):
    """Custom type sc5002LedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_Sc5002LedStatus_Type.__name__ = "OctetString"
_Sc5002LedStatus_Object = MibTableColumn
sc5002LedStatus = _Sc5002LedStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 5, 1, 1, 8),
    _Sc5002LedStatus_Type()
)
sc5002LedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002LedStatus.setStatus("mandatory")


class _Sc5002NearEndValidIntervals_Type(Integer32):
    """Custom type sc5002NearEndValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Sc5002NearEndValidIntervals_Type.__name__ = "Integer32"
_Sc5002NearEndValidIntervals_Object = MibTableColumn
sc5002NearEndValidIntervals = _Sc5002NearEndValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 5, 1, 1, 9),
    _Sc5002NearEndValidIntervals_Type()
)
sc5002NearEndValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002NearEndValidIntervals.setStatus("mandatory")


class _Sc5002FarEndValidIntervals_Type(Integer32):
    """Custom type sc5002FarEndValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Sc5002FarEndValidIntervals_Type.__name__ = "Integer32"
_Sc5002FarEndValidIntervals_Object = MibTableColumn
sc5002FarEndValidIntervals = _Sc5002FarEndValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 5, 1, 1, 10),
    _Sc5002FarEndValidIntervals_Type()
)
sc5002FarEndValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002FarEndValidIntervals.setStatus("mandatory")


class _Sc5002SysUpTime_Type(Integer32):
    """Custom type sc5002SysUpTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sc5002SysUpTime_Type.__name__ = "Integer32"
_Sc5002SysUpTime_Object = MibTableColumn
sc5002SysUpTime = _Sc5002SysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 5, 1, 1, 11),
    _Sc5002SysUpTime_Type()
)
sc5002SysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002SysUpTime.setStatus("mandatory")
_Sc5002Performance_ObjectIdentity = ObjectIdentity
sc5002Performance = _Sc5002Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6)
)
_Sc5002NearEndCurrent15MinTable_Object = MibTable
sc5002NearEndCurrent15MinTable = _Sc5002NearEndCurrent15MinTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 1)
)
if mibBuilder.loadTexts:
    sc5002NearEndCurrent15MinTable.setStatus("mandatory")
_Sc5002NearEndCurrent15MinEntry_Object = MibTableRow
sc5002NearEndCurrent15MinEntry = _Sc5002NearEndCurrent15MinEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 1, 1)
)
sc5002NearEndCurrent15MinEntry.setIndexNames(
    (0, "SC5002-MIB", "sc5002NearEndCurrent15MinIndex"),
)
if mibBuilder.loadTexts:
    sc5002NearEndCurrent15MinEntry.setStatus("mandatory")
_Sc5002NearEndCurrent15MinIndex_Type = SCinstance
_Sc5002NearEndCurrent15MinIndex_Object = MibTableColumn
sc5002NearEndCurrent15MinIndex = _Sc5002NearEndCurrent15MinIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 1, 1, 1),
    _Sc5002NearEndCurrent15MinIndex_Type()
)
sc5002NearEndCurrent15MinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002NearEndCurrent15MinIndex.setStatus("mandatory")


class _Sc5002NearEndCurrent15MinStat_Type(OctetString):
    """Custom type sc5002NearEndCurrent15MinStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_Sc5002NearEndCurrent15MinStat_Type.__name__ = "OctetString"
_Sc5002NearEndCurrent15MinStat_Object = MibTableColumn
sc5002NearEndCurrent15MinStat = _Sc5002NearEndCurrent15MinStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 1, 1, 2),
    _Sc5002NearEndCurrent15MinStat_Type()
)
sc5002NearEndCurrent15MinStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002NearEndCurrent15MinStat.setStatus("mandatory")
_Sc5002NearEndIntervalTable_Object = MibTable
sc5002NearEndIntervalTable = _Sc5002NearEndIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 2)
)
if mibBuilder.loadTexts:
    sc5002NearEndIntervalTable.setStatus("mandatory")
_Sc5002NearEndIntervalEntry_Object = MibTableRow
sc5002NearEndIntervalEntry = _Sc5002NearEndIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 2, 1)
)
sc5002NearEndIntervalEntry.setIndexNames(
    (0, "SC5002-MIB", "sc5002NearEndIntervalIndex"),
    (0, "SC5002-MIB", "sc5002NearEndIntervalNumber"),
)
if mibBuilder.loadTexts:
    sc5002NearEndIntervalEntry.setStatus("mandatory")
_Sc5002NearEndIntervalIndex_Type = SCinstance
_Sc5002NearEndIntervalIndex_Object = MibTableColumn
sc5002NearEndIntervalIndex = _Sc5002NearEndIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 2, 1, 1),
    _Sc5002NearEndIntervalIndex_Type()
)
sc5002NearEndIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002NearEndIntervalIndex.setStatus("mandatory")


class _Sc5002NearEndIntervalNumber_Type(Integer32):
    """Custom type sc5002NearEndIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Sc5002NearEndIntervalNumber_Type.__name__ = "Integer32"
_Sc5002NearEndIntervalNumber_Object = MibTableColumn
sc5002NearEndIntervalNumber = _Sc5002NearEndIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 2, 1, 2),
    _Sc5002NearEndIntervalNumber_Type()
)
sc5002NearEndIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002NearEndIntervalNumber.setStatus("mandatory")


class _Sc5002NearEndIntervalStat_Type(OctetString):
    """Custom type sc5002NearEndIntervalStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_Sc5002NearEndIntervalStat_Type.__name__ = "OctetString"
_Sc5002NearEndIntervalStat_Object = MibTableColumn
sc5002NearEndIntervalStat = _Sc5002NearEndIntervalStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 2, 1, 3),
    _Sc5002NearEndIntervalStat_Type()
)
sc5002NearEndIntervalStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002NearEndIntervalStat.setStatus("mandatory")
_Sc5002NearEndCurrent24HrTable_Object = MibTable
sc5002NearEndCurrent24HrTable = _Sc5002NearEndCurrent24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 3)
)
if mibBuilder.loadTexts:
    sc5002NearEndCurrent24HrTable.setStatus("mandatory")
_Sc5002NearEndCurrent24HrEntry_Object = MibTableRow
sc5002NearEndCurrent24HrEntry = _Sc5002NearEndCurrent24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 3, 1)
)
sc5002NearEndCurrent24HrEntry.setIndexNames(
    (0, "SC5002-MIB", "sc5002NearEndCurrent24HrIndex"),
)
if mibBuilder.loadTexts:
    sc5002NearEndCurrent24HrEntry.setStatus("mandatory")
_Sc5002NearEndCurrent24HrIndex_Type = SCinstance
_Sc5002NearEndCurrent24HrIndex_Object = MibTableColumn
sc5002NearEndCurrent24HrIndex = _Sc5002NearEndCurrent24HrIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 3, 1, 1),
    _Sc5002NearEndCurrent24HrIndex_Type()
)
sc5002NearEndCurrent24HrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002NearEndCurrent24HrIndex.setStatus("mandatory")


class _Sc5002NearEndCurrent24HrStat_Type(OctetString):
    """Custom type sc5002NearEndCurrent24HrStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_Sc5002NearEndCurrent24HrStat_Type.__name__ = "OctetString"
_Sc5002NearEndCurrent24HrStat_Object = MibTableColumn
sc5002NearEndCurrent24HrStat = _Sc5002NearEndCurrent24HrStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 3, 1, 2),
    _Sc5002NearEndCurrent24HrStat_Type()
)
sc5002NearEndCurrent24HrStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002NearEndCurrent24HrStat.setStatus("mandatory")
_Sc5002NearEndRecent24HrTable_Object = MibTable
sc5002NearEndRecent24HrTable = _Sc5002NearEndRecent24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 4)
)
if mibBuilder.loadTexts:
    sc5002NearEndRecent24HrTable.setStatus("mandatory")
_Sc5002NearEndRecent24HrEntry_Object = MibTableRow
sc5002NearEndRecent24HrEntry = _Sc5002NearEndRecent24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 4, 1)
)
sc5002NearEndRecent24HrEntry.setIndexNames(
    (0, "SC5002-MIB", "sc5002NearEndRecent24HrIndex"),
)
if mibBuilder.loadTexts:
    sc5002NearEndRecent24HrEntry.setStatus("mandatory")
_Sc5002NearEndRecent24HrIndex_Type = SCinstance
_Sc5002NearEndRecent24HrIndex_Object = MibTableColumn
sc5002NearEndRecent24HrIndex = _Sc5002NearEndRecent24HrIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 4, 1, 1),
    _Sc5002NearEndRecent24HrIndex_Type()
)
sc5002NearEndRecent24HrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002NearEndRecent24HrIndex.setStatus("mandatory")


class _Sc5002NearEndRecent24HrStat_Type(OctetString):
    """Custom type sc5002NearEndRecent24HrStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_Sc5002NearEndRecent24HrStat_Type.__name__ = "OctetString"
_Sc5002NearEndRecent24HrStat_Object = MibTableColumn
sc5002NearEndRecent24HrStat = _Sc5002NearEndRecent24HrStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 4, 1, 2),
    _Sc5002NearEndRecent24HrStat_Type()
)
sc5002NearEndRecent24HrStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002NearEndRecent24HrStat.setStatus("mandatory")
_Sc5002FarEndCurrent15MinTable_Object = MibTable
sc5002FarEndCurrent15MinTable = _Sc5002FarEndCurrent15MinTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 5)
)
if mibBuilder.loadTexts:
    sc5002FarEndCurrent15MinTable.setStatus("mandatory")
_Sc5002FarEndCurrent15MinEntry_Object = MibTableRow
sc5002FarEndCurrent15MinEntry = _Sc5002FarEndCurrent15MinEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 5, 1)
)
sc5002FarEndCurrent15MinEntry.setIndexNames(
    (0, "SC5002-MIB", "sc5002FarEndCurrent15MinIndex"),
)
if mibBuilder.loadTexts:
    sc5002FarEndCurrent15MinEntry.setStatus("mandatory")
_Sc5002FarEndCurrent15MinIndex_Type = SCinstance
_Sc5002FarEndCurrent15MinIndex_Object = MibTableColumn
sc5002FarEndCurrent15MinIndex = _Sc5002FarEndCurrent15MinIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 5, 1, 1),
    _Sc5002FarEndCurrent15MinIndex_Type()
)
sc5002FarEndCurrent15MinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002FarEndCurrent15MinIndex.setStatus("mandatory")


class _Sc5002FarEndCurrent15MinStat_Type(OctetString):
    """Custom type sc5002FarEndCurrent15MinStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )


_Sc5002FarEndCurrent15MinStat_Type.__name__ = "OctetString"
_Sc5002FarEndCurrent15MinStat_Object = MibTableColumn
sc5002FarEndCurrent15MinStat = _Sc5002FarEndCurrent15MinStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 5, 1, 2),
    _Sc5002FarEndCurrent15MinStat_Type()
)
sc5002FarEndCurrent15MinStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002FarEndCurrent15MinStat.setStatus("mandatory")
_Sc5002FarEndIntervalTable_Object = MibTable
sc5002FarEndIntervalTable = _Sc5002FarEndIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 6)
)
if mibBuilder.loadTexts:
    sc5002FarEndIntervalTable.setStatus("mandatory")
_Sc5002FarEndIntervalEntry_Object = MibTableRow
sc5002FarEndIntervalEntry = _Sc5002FarEndIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 6, 1)
)
sc5002FarEndIntervalEntry.setIndexNames(
    (0, "SC5002-MIB", "sc5002FarEndIntervalIndex"),
    (0, "SC5002-MIB", "sc5002FarEndIntervalNumber"),
)
if mibBuilder.loadTexts:
    sc5002FarEndIntervalEntry.setStatus("mandatory")
_Sc5002FarEndIntervalIndex_Type = SCinstance
_Sc5002FarEndIntervalIndex_Object = MibTableColumn
sc5002FarEndIntervalIndex = _Sc5002FarEndIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 6, 1, 1),
    _Sc5002FarEndIntervalIndex_Type()
)
sc5002FarEndIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002FarEndIntervalIndex.setStatus("mandatory")


class _Sc5002FarEndIntervalNumber_Type(Integer32):
    """Custom type sc5002FarEndIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Sc5002FarEndIntervalNumber_Type.__name__ = "Integer32"
_Sc5002FarEndIntervalNumber_Object = MibTableColumn
sc5002FarEndIntervalNumber = _Sc5002FarEndIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 6, 1, 2),
    _Sc5002FarEndIntervalNumber_Type()
)
sc5002FarEndIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002FarEndIntervalNumber.setStatus("mandatory")


class _Sc5002FarEndIntervalStat_Type(OctetString):
    """Custom type sc5002FarEndIntervalStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )


_Sc5002FarEndIntervalStat_Type.__name__ = "OctetString"
_Sc5002FarEndIntervalStat_Object = MibTableColumn
sc5002FarEndIntervalStat = _Sc5002FarEndIntervalStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 6, 1, 3),
    _Sc5002FarEndIntervalStat_Type()
)
sc5002FarEndIntervalStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002FarEndIntervalStat.setStatus("mandatory")
_Sc5002CurrentFarEnd24HrTable_Object = MibTable
sc5002CurrentFarEnd24HrTable = _Sc5002CurrentFarEnd24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 7)
)
if mibBuilder.loadTexts:
    sc5002CurrentFarEnd24HrTable.setStatus("mandatory")
_Sc5002CurrentFarEnd24HrEntry_Object = MibTableRow
sc5002CurrentFarEnd24HrEntry = _Sc5002CurrentFarEnd24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 7, 1)
)
sc5002CurrentFarEnd24HrEntry.setIndexNames(
    (0, "SC5002-MIB", "sc5002CurrentFarEnd24HrIndex"),
)
if mibBuilder.loadTexts:
    sc5002CurrentFarEnd24HrEntry.setStatus("mandatory")
_Sc5002CurrentFarEnd24HrIndex_Type = SCinstance
_Sc5002CurrentFarEnd24HrIndex_Object = MibTableColumn
sc5002CurrentFarEnd24HrIndex = _Sc5002CurrentFarEnd24HrIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 7, 1, 1),
    _Sc5002CurrentFarEnd24HrIndex_Type()
)
sc5002CurrentFarEnd24HrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002CurrentFarEnd24HrIndex.setStatus("mandatory")


class _Sc5002CurrentFarEnd24HrStat_Type(OctetString):
    """Custom type sc5002CurrentFarEnd24HrStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_Sc5002CurrentFarEnd24HrStat_Type.__name__ = "OctetString"
_Sc5002CurrentFarEnd24HrStat_Object = MibTableColumn
sc5002CurrentFarEnd24HrStat = _Sc5002CurrentFarEnd24HrStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 7, 1, 2),
    _Sc5002CurrentFarEnd24HrStat_Type()
)
sc5002CurrentFarEnd24HrStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002CurrentFarEnd24HrStat.setStatus("mandatory")
_Sc5002RecentFarEnd24HrTable_Object = MibTable
sc5002RecentFarEnd24HrTable = _Sc5002RecentFarEnd24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 8)
)
if mibBuilder.loadTexts:
    sc5002RecentFarEnd24HrTable.setStatus("mandatory")
_Sc5002RecentFarEnd24HrEntry_Object = MibTableRow
sc5002RecentFarEnd24HrEntry = _Sc5002RecentFarEnd24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 8, 1)
)
sc5002RecentFarEnd24HrEntry.setIndexNames(
    (0, "SC5002-MIB", "sc5002RecentFarEnd24HrIndex"),
)
if mibBuilder.loadTexts:
    sc5002RecentFarEnd24HrEntry.setStatus("mandatory")
_Sc5002RecentFarEnd24HrIndex_Type = SCinstance
_Sc5002RecentFarEnd24HrIndex_Object = MibTableColumn
sc5002RecentFarEnd24HrIndex = _Sc5002RecentFarEnd24HrIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 8, 1, 1),
    _Sc5002RecentFarEnd24HrIndex_Type()
)
sc5002RecentFarEnd24HrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002RecentFarEnd24HrIndex.setStatus("mandatory")


class _Sc5002RecentFarEnd24HrStat_Type(OctetString):
    """Custom type sc5002RecentFarEnd24HrStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_Sc5002RecentFarEnd24HrStat_Type.__name__ = "OctetString"
_Sc5002RecentFarEnd24HrStat_Object = MibTableColumn
sc5002RecentFarEnd24HrStat = _Sc5002RecentFarEnd24HrStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 8, 1, 2),
    _Sc5002RecentFarEnd24HrStat_Type()
)
sc5002RecentFarEnd24HrStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002RecentFarEnd24HrStat.setStatus("mandatory")
_Sc5002NearEndUnavailableTimeRegTable_Object = MibTable
sc5002NearEndUnavailableTimeRegTable = _Sc5002NearEndUnavailableTimeRegTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 9)
)
if mibBuilder.loadTexts:
    sc5002NearEndUnavailableTimeRegTable.setStatus("mandatory")
_Sc5002NearEndUnavailableTimeRegEntry_Object = MibTableRow
sc5002NearEndUnavailableTimeRegEntry = _Sc5002NearEndUnavailableTimeRegEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 9, 1)
)
sc5002NearEndUnavailableTimeRegEntry.setIndexNames(
    (0, "SC5002-MIB", "sc5002NearEndUnavailableTimeRegIndex"),
    (0, "SC5002-MIB", "sc5002NearEndUnavailableTimeRegNumber"),
)
if mibBuilder.loadTexts:
    sc5002NearEndUnavailableTimeRegEntry.setStatus("mandatory")
_Sc5002NearEndUnavailableTimeRegIndex_Type = SCinstance
_Sc5002NearEndUnavailableTimeRegIndex_Object = MibTableColumn
sc5002NearEndUnavailableTimeRegIndex = _Sc5002NearEndUnavailableTimeRegIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 9, 1, 1),
    _Sc5002NearEndUnavailableTimeRegIndex_Type()
)
sc5002NearEndUnavailableTimeRegIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002NearEndUnavailableTimeRegIndex.setStatus("mandatory")


class _Sc5002NearEndUnavailableTimeRegNumber_Type(Integer32):
    """Custom type sc5002NearEndUnavailableTimeRegNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Sc5002NearEndUnavailableTimeRegNumber_Type.__name__ = "Integer32"
_Sc5002NearEndUnavailableTimeRegNumber_Object = MibTableColumn
sc5002NearEndUnavailableTimeRegNumber = _Sc5002NearEndUnavailableTimeRegNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 9, 1, 2),
    _Sc5002NearEndUnavailableTimeRegNumber_Type()
)
sc5002NearEndUnavailableTimeRegNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002NearEndUnavailableTimeRegNumber.setStatus("mandatory")


class _Sc5002NearEndUnavailableTimeRegStart_Type(Integer32):
    """Custom type sc5002NearEndUnavailableTimeRegStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sc5002NearEndUnavailableTimeRegStart_Type.__name__ = "Integer32"
_Sc5002NearEndUnavailableTimeRegStart_Object = MibTableColumn
sc5002NearEndUnavailableTimeRegStart = _Sc5002NearEndUnavailableTimeRegStart_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 9, 1, 3),
    _Sc5002NearEndUnavailableTimeRegStart_Type()
)
sc5002NearEndUnavailableTimeRegStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002NearEndUnavailableTimeRegStart.setStatus("mandatory")


class _Sc5002NearEndUnavailableTimeRegStop_Type(Integer32):
    """Custom type sc5002NearEndUnavailableTimeRegStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sc5002NearEndUnavailableTimeRegStop_Type.__name__ = "Integer32"
_Sc5002NearEndUnavailableTimeRegStop_Object = MibTableColumn
sc5002NearEndUnavailableTimeRegStop = _Sc5002NearEndUnavailableTimeRegStop_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 9, 1, 4),
    _Sc5002NearEndUnavailableTimeRegStop_Type()
)
sc5002NearEndUnavailableTimeRegStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002NearEndUnavailableTimeRegStop.setStatus("mandatory")
_Sc5002FarEndUnavailableTimeRegTable_Object = MibTable
sc5002FarEndUnavailableTimeRegTable = _Sc5002FarEndUnavailableTimeRegTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 10)
)
if mibBuilder.loadTexts:
    sc5002FarEndUnavailableTimeRegTable.setStatus("mandatory")
_Sc5002FarEndUnavailableTimeRegEntry_Object = MibTableRow
sc5002FarEndUnavailableTimeRegEntry = _Sc5002FarEndUnavailableTimeRegEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 10, 1)
)
sc5002FarEndUnavailableTimeRegEntry.setIndexNames(
    (0, "SC5002-MIB", "sc5002FarEndUnavailableTimeRegIndex"),
    (0, "SC5002-MIB", "sc5002FarEndUnavailableTimeRegNumber"),
)
if mibBuilder.loadTexts:
    sc5002FarEndUnavailableTimeRegEntry.setStatus("mandatory")
_Sc5002FarEndUnavailableTimeRegIndex_Type = SCinstance
_Sc5002FarEndUnavailableTimeRegIndex_Object = MibTableColumn
sc5002FarEndUnavailableTimeRegIndex = _Sc5002FarEndUnavailableTimeRegIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 10, 1, 1),
    _Sc5002FarEndUnavailableTimeRegIndex_Type()
)
sc5002FarEndUnavailableTimeRegIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002FarEndUnavailableTimeRegIndex.setStatus("mandatory")


class _Sc5002FarEndUnavailableTimeRegNumber_Type(Integer32):
    """Custom type sc5002FarEndUnavailableTimeRegNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Sc5002FarEndUnavailableTimeRegNumber_Type.__name__ = "Integer32"
_Sc5002FarEndUnavailableTimeRegNumber_Object = MibTableColumn
sc5002FarEndUnavailableTimeRegNumber = _Sc5002FarEndUnavailableTimeRegNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 10, 1, 2),
    _Sc5002FarEndUnavailableTimeRegNumber_Type()
)
sc5002FarEndUnavailableTimeRegNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002FarEndUnavailableTimeRegNumber.setStatus("mandatory")


class _Sc5002FarEndUnavailableTimeRegStart_Type(Integer32):
    """Custom type sc5002FarEndUnavailableTimeRegStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sc5002FarEndUnavailableTimeRegStart_Type.__name__ = "Integer32"
_Sc5002FarEndUnavailableTimeRegStart_Object = MibTableColumn
sc5002FarEndUnavailableTimeRegStart = _Sc5002FarEndUnavailableTimeRegStart_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 10, 1, 3),
    _Sc5002FarEndUnavailableTimeRegStart_Type()
)
sc5002FarEndUnavailableTimeRegStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002FarEndUnavailableTimeRegStart.setStatus("mandatory")


class _Sc5002FarEndUnavailableTimeRegStop_Type(Integer32):
    """Custom type sc5002FarEndUnavailableTimeRegStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sc5002FarEndUnavailableTimeRegStop_Type.__name__ = "Integer32"
_Sc5002FarEndUnavailableTimeRegStop_Object = MibTableColumn
sc5002FarEndUnavailableTimeRegStop = _Sc5002FarEndUnavailableTimeRegStop_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 8, 6, 10, 1, 4),
    _Sc5002FarEndUnavailableTimeRegStop_Type()
)
sc5002FarEndUnavailableTimeRegStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5002FarEndUnavailableTimeRegStop.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SC5002-MIB",
    **{"gdc": gdc,
       "dsx1": dsx1,
       "sc5002": sc5002,
       "sc5002Version": sc5002Version,
       "sc5002MIBversion": sc5002MIBversion,
       "sc5002VersionTable": sc5002VersionTable,
       "sc5002VersionEntry": sc5002VersionEntry,
       "sc5002VersionIndex": sc5002VersionIndex,
       "sc5002ActiveFirmwareRev": sc5002ActiveFirmwareRev,
       "sc5002StoredFirmwareRev": sc5002StoredFirmwareRev,
       "sc5002BootRev": sc5002BootRev,
       "sc5002StoredFirmwareStatus": sc5002StoredFirmwareStatus,
       "sc5002SwitchActiveFirmware": sc5002SwitchActiveFirmware,
       "sc5002DownloadingMode": sc5002DownloadingMode,
       "sc5002FirmwareRev": sc5002FirmwareRev,
       "sc5002NetworkCfg": sc5002NetworkCfg,
       "sc5002NetworkCfgTable": sc5002NetworkCfgTable,
       "sc5002NetworkCfgEntry": sc5002NetworkCfgEntry,
       "sc5002NetworkCfgIndex": sc5002NetworkCfgIndex,
       "sc5002E1SignalingMode": sc5002E1SignalingMode,
       "sc5002Alarms": sc5002Alarms,
       "sc5002AlarmData": sc5002AlarmData,
       "sc5002NoResponse": sc5002NoResponse,
       "sc5002DiagRxErr": sc5002DiagRxErr,
       "sc5002PowerUp": sc5002PowerUp,
       "sc5002NvRamCorrupt": sc5002NvRamCorrupt,
       "sc5002UnitFailure": sc5002UnitFailure,
       "sc5002TimingLoss": sc5002TimingLoss,
       "sc5002LossOfSignal": sc5002LossOfSignal,
       "sc5002LossOfFrame": sc5002LossOfFrame,
       "sc5002AlarmIndSignal": sc5002AlarmIndSignal,
       "sc5002FallbackTimingActive": sc5002FallbackTimingActive,
       "sc5002NearEndLnCodeViol": sc5002NearEndLnCodeViol,
       "sc5002NearEndErrSec": sc5002NearEndErrSec,
       "sc5002NearEndBkdBlkErr": sc5002NearEndBkdBlkErr,
       "sc5002NearEndSevErrSec": sc5002NearEndSevErrSec,
       "sc5002NearEndUnavlSec": sc5002NearEndUnavlSec,
       "sc5002FarEndErrSec": sc5002FarEndErrSec,
       "sc5002FarEndBkdBlkErr": sc5002FarEndBkdBlkErr,
       "sc5002FarEndSevErrSec": sc5002FarEndSevErrSec,
       "sc5002FarEndUnavlSec": sc5002FarEndUnavlSec,
       "sc5002NearEndAlarmCfgTable": sc5002NearEndAlarmCfgTable,
       "sc5002NearEndAlarmCfgEntry": sc5002NearEndAlarmCfgEntry,
       "sc5002NearEndAlarmCfgIndex": sc5002NearEndAlarmCfgIndex,
       "sc5002NearEndAlarmCfgIdentifier": sc5002NearEndAlarmCfgIdentifier,
       "sc5002NearEndAlarmWindow": sc5002NearEndAlarmWindow,
       "sc5002NearEndAlarmThreshold": sc5002NearEndAlarmThreshold,
       "sc5002FarEndAlarmCfgTable": sc5002FarEndAlarmCfgTable,
       "sc5002FarEndAlarmCfgEntry": sc5002FarEndAlarmCfgEntry,
       "sc5002FarEndAlarmCfgIndex": sc5002FarEndAlarmCfgIndex,
       "sc5002FarEndAlarmCfgIdentifier": sc5002FarEndAlarmCfgIdentifier,
       "sc5002FarEndAlarmWindow": sc5002FarEndAlarmWindow,
       "sc5002FarEndAlarmThreshold": sc5002FarEndAlarmThreshold,
       "sc5002Diagnostics": sc5002Diagnostics,
       "sc5002DiagTable": sc5002DiagTable,
       "sc5002DiagEntry": sc5002DiagEntry,
       "sc5002DiagIndex": sc5002DiagIndex,
       "sc5002LoopbackConfig": sc5002LoopbackConfig,
       "sc5002TestResult": sc5002TestResult,
       "sc5002Maintenance": sc5002Maintenance,
       "sc5002MaintenanceTable": sc5002MaintenanceTable,
       "sc5002MaintenanceEntry": sc5002MaintenanceEntry,
       "sc5002MaintenanceLineIndex": sc5002MaintenanceLineIndex,
       "sc5002SoftReset": sc5002SoftReset,
       "sc5002DefaultInit": sc5002DefaultInit,
       "sc5002NearEndResetStats": sc5002NearEndResetStats,
       "sc5002NearEndStatLastInitialized": sc5002NearEndStatLastInitialized,
       "sc5002FarEndResetStats": sc5002FarEndResetStats,
       "sc5002FarEndStatLastInitialized": sc5002FarEndStatLastInitialized,
       "sc5002LedStatus": sc5002LedStatus,
       "sc5002NearEndValidIntervals": sc5002NearEndValidIntervals,
       "sc5002FarEndValidIntervals": sc5002FarEndValidIntervals,
       "sc5002SysUpTime": sc5002SysUpTime,
       "sc5002Performance": sc5002Performance,
       "sc5002NearEndCurrent15MinTable": sc5002NearEndCurrent15MinTable,
       "sc5002NearEndCurrent15MinEntry": sc5002NearEndCurrent15MinEntry,
       "sc5002NearEndCurrent15MinIndex": sc5002NearEndCurrent15MinIndex,
       "sc5002NearEndCurrent15MinStat": sc5002NearEndCurrent15MinStat,
       "sc5002NearEndIntervalTable": sc5002NearEndIntervalTable,
       "sc5002NearEndIntervalEntry": sc5002NearEndIntervalEntry,
       "sc5002NearEndIntervalIndex": sc5002NearEndIntervalIndex,
       "sc5002NearEndIntervalNumber": sc5002NearEndIntervalNumber,
       "sc5002NearEndIntervalStat": sc5002NearEndIntervalStat,
       "sc5002NearEndCurrent24HrTable": sc5002NearEndCurrent24HrTable,
       "sc5002NearEndCurrent24HrEntry": sc5002NearEndCurrent24HrEntry,
       "sc5002NearEndCurrent24HrIndex": sc5002NearEndCurrent24HrIndex,
       "sc5002NearEndCurrent24HrStat": sc5002NearEndCurrent24HrStat,
       "sc5002NearEndRecent24HrTable": sc5002NearEndRecent24HrTable,
       "sc5002NearEndRecent24HrEntry": sc5002NearEndRecent24HrEntry,
       "sc5002NearEndRecent24HrIndex": sc5002NearEndRecent24HrIndex,
       "sc5002NearEndRecent24HrStat": sc5002NearEndRecent24HrStat,
       "sc5002FarEndCurrent15MinTable": sc5002FarEndCurrent15MinTable,
       "sc5002FarEndCurrent15MinEntry": sc5002FarEndCurrent15MinEntry,
       "sc5002FarEndCurrent15MinIndex": sc5002FarEndCurrent15MinIndex,
       "sc5002FarEndCurrent15MinStat": sc5002FarEndCurrent15MinStat,
       "sc5002FarEndIntervalTable": sc5002FarEndIntervalTable,
       "sc5002FarEndIntervalEntry": sc5002FarEndIntervalEntry,
       "sc5002FarEndIntervalIndex": sc5002FarEndIntervalIndex,
       "sc5002FarEndIntervalNumber": sc5002FarEndIntervalNumber,
       "sc5002FarEndIntervalStat": sc5002FarEndIntervalStat,
       "sc5002CurrentFarEnd24HrTable": sc5002CurrentFarEnd24HrTable,
       "sc5002CurrentFarEnd24HrEntry": sc5002CurrentFarEnd24HrEntry,
       "sc5002CurrentFarEnd24HrIndex": sc5002CurrentFarEnd24HrIndex,
       "sc5002CurrentFarEnd24HrStat": sc5002CurrentFarEnd24HrStat,
       "sc5002RecentFarEnd24HrTable": sc5002RecentFarEnd24HrTable,
       "sc5002RecentFarEnd24HrEntry": sc5002RecentFarEnd24HrEntry,
       "sc5002RecentFarEnd24HrIndex": sc5002RecentFarEnd24HrIndex,
       "sc5002RecentFarEnd24HrStat": sc5002RecentFarEnd24HrStat,
       "sc5002NearEndUnavailableTimeRegTable": sc5002NearEndUnavailableTimeRegTable,
       "sc5002NearEndUnavailableTimeRegEntry": sc5002NearEndUnavailableTimeRegEntry,
       "sc5002NearEndUnavailableTimeRegIndex": sc5002NearEndUnavailableTimeRegIndex,
       "sc5002NearEndUnavailableTimeRegNumber": sc5002NearEndUnavailableTimeRegNumber,
       "sc5002NearEndUnavailableTimeRegStart": sc5002NearEndUnavailableTimeRegStart,
       "sc5002NearEndUnavailableTimeRegStop": sc5002NearEndUnavailableTimeRegStop,
       "sc5002FarEndUnavailableTimeRegTable": sc5002FarEndUnavailableTimeRegTable,
       "sc5002FarEndUnavailableTimeRegEntry": sc5002FarEndUnavailableTimeRegEntry,
       "sc5002FarEndUnavailableTimeRegIndex": sc5002FarEndUnavailableTimeRegIndex,
       "sc5002FarEndUnavailableTimeRegNumber": sc5002FarEndUnavailableTimeRegNumber,
       "sc5002FarEndUnavailableTimeRegStart": sc5002FarEndUnavailableTimeRegStart,
       "sc5002FarEndUnavailableTimeRegStop": sc5002FarEndUnavailableTimeRegStop}
)
