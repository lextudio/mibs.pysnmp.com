# SNMP MIB module (GDCDATX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GDCDATX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:12 2024
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
_Datx_ObjectIdentity = ObjectIdentity
datx = _Datx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 7)
)
_DatxSystem_ObjectIdentity = ObjectIdentity
datxSystem = _DatxSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 7, 1)
)
_DatxVersion_ObjectIdentity = ObjectIdentity
datxVersion = _DatxVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 1)
)


class _DatxMIBversion_Type(DisplayString):
    """Custom type datxMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_DatxMIBversion_Type.__name__ = "DisplayString"
_DatxMIBversion_Object = MibScalar
datxMIBversion = _DatxMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 1, 1),
    _DatxMIBversion_Type()
)
datxMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datxMIBversion.setStatus("mandatory")
_DatxMaintenance_ObjectIdentity = ObjectIdentity
datxMaintenance = _DatxMaintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 2)
)
_DatxMaintTable_Object = MibTable
datxMaintTable = _DatxMaintTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    datxMaintTable.setStatus("mandatory")
_DatxMaintEntry_Object = MibTableRow
datxMaintEntry = _DatxMaintEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 2, 1, 1)
)
datxMaintEntry.setIndexNames(
    (0, "GDCDATX-MIB", "datxMaintIndex"),
)
if mibBuilder.loadTexts:
    datxMaintEntry.setStatus("mandatory")
_DatxMaintIndex_Type = SCinstance
_DatxMaintIndex_Object = MibTableColumn
datxMaintIndex = _DatxMaintIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 2, 1, 1, 1),
    _DatxMaintIndex_Type()
)
datxMaintIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datxMaintIndex.setStatus("mandatory")


class _DatxFirmwareRev_Type(DisplayString):
    """Custom type datxFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_DatxFirmwareRev_Type.__name__ = "DisplayString"
_DatxFirmwareRev_Object = MibTableColumn
datxFirmwareRev = _DatxFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 2, 1, 1, 2),
    _DatxFirmwareRev_Type()
)
datxFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datxFirmwareRev.setStatus("mandatory")


class _DatxDefaultInit_Type(Integer32):
    """Custom type datxDefaultInit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("factoryDefault", 2),
          ("normal", 1))
    )


_DatxDefaultInit_Type.__name__ = "Integer32"
_DatxDefaultInit_Object = MibTableColumn
datxDefaultInit = _DatxDefaultInit_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 2, 1, 1, 3),
    _DatxDefaultInit_Type()
)
datxDefaultInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    datxDefaultInit.setStatus("mandatory")


class _DatxFrontPanel_Type(Integer32):
    """Custom type datxFrontPanel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("inhibit", 1))
    )


_DatxFrontPanel_Type.__name__ = "Integer32"
_DatxFrontPanel_Object = MibTableColumn
datxFrontPanel = _DatxFrontPanel_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 2, 1, 1, 4),
    _DatxFrontPanel_Type()
)
datxFrontPanel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    datxFrontPanel.setStatus("mandatory")


class _DatxLedStatus_Type(OctetString):
    """Custom type datxLedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_DatxLedStatus_Type.__name__ = "OctetString"
_DatxLedStatus_Object = MibTableColumn
datxLedStatus = _DatxLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 2, 1, 1, 5),
    _DatxLedStatus_Type()
)
datxLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datxLedStatus.setStatus("mandatory")
_DatxConfiguration_ObjectIdentity = ObjectIdentity
datxConfiguration = _DatxConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 3)
)
_DatxTransConfigTable_Object = MibTable
datxTransConfigTable = _DatxTransConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 3, 1)
)
if mibBuilder.loadTexts:
    datxTransConfigTable.setStatus("mandatory")
_DatxTransConfigEntry_Object = MibTableRow
datxTransConfigEntry = _DatxTransConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 3, 1, 1)
)
datxTransConfigEntry.setIndexNames(
    (0, "GDCDATX-MIB", "datxTransConfigIndex"),
)
if mibBuilder.loadTexts:
    datxTransConfigEntry.setStatus("mandatory")
_DatxTransConfigIndex_Type = SCinstance
_DatxTransConfigIndex_Object = MibTableColumn
datxTransConfigIndex = _DatxTransConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 3, 1, 1, 1),
    _DatxTransConfigIndex_Type()
)
datxTransConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datxTransConfigIndex.setStatus("mandatory")


class _DatxBaudRate_Type(Integer32):
    """Custom type datxBaudRate based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("asynchronous", 1),
          ("synchronous1200", 2),
          ("synchronous14400", 7),
          ("synchronous19200", 8),
          ("synchronous2400", 3),
          ("synchronous4800", 4),
          ("synchronous7200", 5),
          ("synchronous9600", 6))
    )


_DatxBaudRate_Type.__name__ = "Integer32"
_DatxBaudRate_Object = MibTableColumn
datxBaudRate = _DatxBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 3, 1, 1, 2),
    _DatxBaudRate_Type()
)
datxBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    datxBaudRate.setStatus("mandatory")


class _DatxSyncTxClockSource_Type(Integer32):
    """Custom type datxSyncTxClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 3),
          ("internal", 1),
          ("slave", 2))
    )


_DatxSyncTxClockSource_Type.__name__ = "Integer32"
_DatxSyncTxClockSource_Object = MibTableColumn
datxSyncTxClockSource = _DatxSyncTxClockSource_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 3, 1, 1, 3),
    _DatxSyncTxClockSource_Type()
)
datxSyncTxClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    datxSyncTxClockSource.setStatus("mandatory")


class _DatxEiaSyncClock_Type(Integer32):
    """Custom type datxEiaSyncClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_DatxEiaSyncClock_Type.__name__ = "Integer32"
_DatxEiaSyncClock_Object = MibTableColumn
datxEiaSyncClock = _DatxEiaSyncClock_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 3, 1, 1, 4),
    _DatxEiaSyncClock_Type()
)
datxEiaSyncClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    datxEiaSyncClock.setStatus("mandatory")
_DatxEiaConfigTable_Object = MibTable
datxEiaConfigTable = _DatxEiaConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 3, 2)
)
if mibBuilder.loadTexts:
    datxEiaConfigTable.setStatus("mandatory")
_DatxEiaConfigEntry_Object = MibTableRow
datxEiaConfigEntry = _DatxEiaConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 3, 2, 1)
)
datxEiaConfigEntry.setIndexNames(
    (0, "GDCDATX-MIB", "datxEIAIndex"),
)
if mibBuilder.loadTexts:
    datxEiaConfigEntry.setStatus("mandatory")
_DatxEIAIndex_Type = SCinstance
_DatxEIAIndex_Object = MibTableColumn
datxEIAIndex = _DatxEIAIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 3, 2, 1, 1),
    _DatxEIAIndex_Type()
)
datxEIAIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datxEIAIndex.setStatus("mandatory")


class _DatxCarrierControl_Type(Integer32):
    """Custom type datxCarrierControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtr", 1),
          ("rts", 2))
    )


_DatxCarrierControl_Type.__name__ = "Integer32"
_DatxCarrierControl_Object = MibTableColumn
datxCarrierControl = _DatxCarrierControl_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 3, 2, 1, 2),
    _DatxCarrierControl_Type()
)
datxCarrierControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    datxCarrierControl.setStatus("mandatory")


class _DatxRtsMode_Type(Integer32):
    """Custom type datxRtsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forced", 2),
          ("real", 1))
    )


_DatxRtsMode_Type.__name__ = "Integer32"
_DatxRtsMode_Object = MibTableColumn
datxRtsMode = _DatxRtsMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 3, 2, 1, 3),
    _DatxRtsMode_Type()
)
datxRtsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    datxRtsMode.setStatus("mandatory")


class _DatxRtsCtsDelay_Type(Integer32):
    """Custom type datxRtsCtsDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("t75mSec", 2),
          ("t8mSec", 1))
    )


_DatxRtsCtsDelay_Type.__name__ = "Integer32"
_DatxRtsCtsDelay_Object = MibTableColumn
datxRtsCtsDelay = _DatxRtsCtsDelay_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 3, 2, 1, 4),
    _DatxRtsCtsDelay_Type()
)
datxRtsCtsDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    datxRtsCtsDelay.setStatus("mandatory")


class _DatxEiaRdlControl_Type(Integer32):
    """Custom type datxEiaRdlControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_DatxEiaRdlControl_Type.__name__ = "Integer32"
_DatxEiaRdlControl_Object = MibTableColumn
datxEiaRdlControl = _DatxEiaRdlControl_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 3, 2, 1, 5),
    _DatxEiaRdlControl_Type()
)
datxEiaRdlControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    datxEiaRdlControl.setStatus("mandatory")


class _DatxDsrInAl_Type(Integer32):
    """Custom type datxDsrInAl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_DatxDsrInAl_Type.__name__ = "Integer32"
_DatxDsrInAl_Object = MibTableColumn
datxDsrInAl = _DatxDsrInAl_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 3, 2, 1, 6),
    _DatxDsrInAl_Type()
)
datxDsrInAl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    datxDsrInAl.setStatus("mandatory")


class _DatxEiaAlControl_Type(Integer32):
    """Custom type datxEiaAlControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_DatxEiaAlControl_Type.__name__ = "Integer32"
_DatxEiaAlControl_Object = MibTableColumn
datxEiaAlControl = _DatxEiaAlControl_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 3, 2, 1, 7),
    _DatxEiaAlControl_Type()
)
datxEiaAlControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    datxEiaAlControl.setStatus("mandatory")
_DatxMiscConfigTable_Object = MibTable
datxMiscConfigTable = _DatxMiscConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 3, 3)
)
if mibBuilder.loadTexts:
    datxMiscConfigTable.setStatus("mandatory")
_DatxMiscConfigEntry_Object = MibTableRow
datxMiscConfigEntry = _DatxMiscConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 3, 3, 1)
)
datxMiscConfigEntry.setIndexNames(
    (0, "GDCDATX-MIB", "datxMiscIndex"),
)
if mibBuilder.loadTexts:
    datxMiscConfigEntry.setStatus("mandatory")
_DatxMiscIndex_Type = SCinstance
_DatxMiscIndex_Object = MibTableColumn
datxMiscIndex = _DatxMiscIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 3, 3, 1, 1),
    _DatxMiscIndex_Type()
)
datxMiscIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datxMiscIndex.setStatus("mandatory")


class _DatxSystemStatusOption_Type(Integer32):
    """Custom type datxSystemStatusOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_DatxSystemStatusOption_Type.__name__ = "Integer32"
_DatxSystemStatusOption_Object = MibTableColumn
datxSystemStatusOption = _DatxSystemStatusOption_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 3, 3, 1, 2),
    _DatxSystemStatusOption_Type()
)
datxSystemStatusOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    datxSystemStatusOption.setStatus("mandatory")


class _DatxDualSignalingTimer_Type(Integer32):
    """Custom type datxDualSignalingTimer based on Integer32"""
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
        *(("disable", 1),
          ("immediate", 4),
          ("time1Sec", 3),
          ("time3Sec", 2))
    )


_DatxDualSignalingTimer_Type.__name__ = "Integer32"
_DatxDualSignalingTimer_Object = MibTableColumn
datxDualSignalingTimer = _DatxDualSignalingTimer_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 3, 3, 1, 3),
    _DatxDualSignalingTimer_Type()
)
datxDualSignalingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    datxDualSignalingTimer.setStatus("mandatory")


class _DatxRegenCharLength_Type(Integer32):
    """Custom type datxRegenCharLength based on Integer32"""
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
        *(("bits10", 3),
          ("bits11", 4),
          ("bits8", 1),
          ("bits9", 2))
    )


_DatxRegenCharLength_Type.__name__ = "Integer32"
_DatxRegenCharLength_Object = MibTableColumn
datxRegenCharLength = _DatxRegenCharLength_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 3, 3, 1, 4),
    _DatxRegenCharLength_Type()
)
datxRegenCharLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    datxRegenCharLength.setStatus("mandatory")


class _DatxRegenMode_Type(Integer32):
    """Custom type datxRegenMode based on Integer32"""
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


_DatxRegenMode_Type.__name__ = "Integer32"
_DatxRegenMode_Object = MibTableColumn
datxRegenMode = _DatxRegenMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 3, 3, 1, 5),
    _DatxRegenMode_Type()
)
datxRegenMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    datxRegenMode.setStatus("mandatory")


class _DatxAsyncRate_Type(Integer32):
    """Custom type datxAsyncRate based on Integer32"""
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
        *(("async14400", 4),
          ("async19200", 5),
          ("async4800", 1),
          ("async7200", 2),
          ("async9600", 3))
    )


_DatxAsyncRate_Type.__name__ = "Integer32"
_DatxAsyncRate_Object = MibTableColumn
datxAsyncRate = _DatxAsyncRate_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 3, 3, 1, 6),
    _DatxAsyncRate_Type()
)
datxAsyncRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    datxAsyncRate.setStatus("mandatory")
_DatxDiagnostics_ObjectIdentity = ObjectIdentity
datxDiagnostics = _DatxDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 4)
)
_DatxDiagnosticsTable_Object = MibTable
datxDiagnosticsTable = _DatxDiagnosticsTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 4, 1)
)
if mibBuilder.loadTexts:
    datxDiagnosticsTable.setStatus("mandatory")
_DatxDiagEntry_Object = MibTableRow
datxDiagEntry = _DatxDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 4, 1, 1)
)
datxDiagEntry.setIndexNames(
    (0, "GDCDATX-MIB", "datxDiagnosticsIndex"),
)
if mibBuilder.loadTexts:
    datxDiagEntry.setStatus("mandatory")
_DatxDiagnosticsIndex_Type = SCinstance
_DatxDiagnosticsIndex_Object = MibTableColumn
datxDiagnosticsIndex = _DatxDiagnosticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 4, 1, 1, 1),
    _DatxDiagnosticsIndex_Type()
)
datxDiagnosticsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datxDiagnosticsIndex.setStatus("mandatory")


class _DatxDiagTest_Type(Integer32):
    """Custom type datxDiagTest based on Integer32"""
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
        *(("analoop", 3),
          ("analoopSelfTest", 4),
          ("noTest", 1),
          ("remoteDL", 5),
          ("remoteDLselfTest", 6),
          ("selfTest", 2))
    )


_DatxDiagTest_Type.__name__ = "Integer32"
_DatxDiagTest_Object = MibTableColumn
datxDiagTest = _DatxDiagTest_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 4, 1, 1, 2),
    _DatxDiagTest_Type()
)
datxDiagTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    datxDiagTest.setStatus("mandatory")


class _DatxTestError_Type(Integer32):
    """Custom type datxTestError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("testError", 2))
    )


_DatxTestError_Type.__name__ = "Integer32"
_DatxTestError_Object = MibTableColumn
datxTestError = _DatxTestError_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 4, 1, 1, 3),
    _DatxTestError_Type()
)
datxTestError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datxTestError.setStatus("mandatory")
_DatxTestDuration_Type = TimeTicks
_DatxTestDuration_Object = MibTableColumn
datxTestDuration = _DatxTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 4, 1, 1, 4),
    _DatxTestDuration_Type()
)
datxTestDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datxTestDuration.setStatus("mandatory")
_DatxStatus_ObjectIdentity = ObjectIdentity
datxStatus = _DatxStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 5)
)
_DatxStatusTable_Object = MibTable
datxStatusTable = _DatxStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 5, 1)
)
if mibBuilder.loadTexts:
    datxStatusTable.setStatus("mandatory")
_DatxStatusEntry_Object = MibTableRow
datxStatusEntry = _DatxStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 5, 1, 1)
)
datxStatusEntry.setIndexNames(
    (0, "GDCDATX-MIB", "datxStatusIndex"),
)
if mibBuilder.loadTexts:
    datxStatusEntry.setStatus("mandatory")
_DatxStatusIndex_Type = SCinstance
_DatxStatusIndex_Object = MibTableColumn
datxStatusIndex = _DatxStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 5, 1, 1, 1),
    _DatxStatusIndex_Type()
)
datxStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datxStatusIndex.setStatus("mandatory")


class _DatxDTRstatus_Type(Integer32):
    """Custom type datxDTRstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_DatxDTRstatus_Type.__name__ = "Integer32"
_DatxDTRstatus_Object = MibTableColumn
datxDTRstatus = _DatxDTRstatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 5, 1, 1, 2),
    _DatxDTRstatus_Type()
)
datxDTRstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datxDTRstatus.setStatus("mandatory")


class _DatxRDLstatus_Type(Integer32):
    """Custom type datxRDLstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_DatxRDLstatus_Type.__name__ = "Integer32"
_DatxRDLstatus_Object = MibTableColumn
datxRDLstatus = _DatxRDLstatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 5, 1, 1, 3),
    _DatxRDLstatus_Type()
)
datxRDLstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datxRDLstatus.setStatus("mandatory")


class _DatxCOstatus_Type(Integer32):
    """Custom type datxCOstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_DatxCOstatus_Type.__name__ = "Integer32"
_DatxCOstatus_Object = MibTableColumn
datxCOstatus = _DatxCOstatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 5, 1, 1, 4),
    _DatxCOstatus_Type()
)
datxCOstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datxCOstatus.setStatus("mandatory")


class _DatxCTSstatus_Type(Integer32):
    """Custom type datxCTSstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_DatxCTSstatus_Type.__name__ = "Integer32"
_DatxCTSstatus_Object = MibTableColumn
datxCTSstatus = _DatxCTSstatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 5, 1, 1, 5),
    _DatxCTSstatus_Type()
)
datxCTSstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datxCTSstatus.setStatus("mandatory")


class _DatxRTSstatus_Type(Integer32):
    """Custom type datxRTSstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_DatxRTSstatus_Type.__name__ = "Integer32"
_DatxRTSstatus_Object = MibTableColumn
datxRTSstatus = _DatxRTSstatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 5, 1, 1, 6),
    _DatxRTSstatus_Type()
)
datxRTSstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datxRTSstatus.setStatus("mandatory")


class _DatxTMstatus_Type(Integer32):
    """Custom type datxTMstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_DatxTMstatus_Type.__name__ = "Integer32"
_DatxTMstatus_Object = MibTableColumn
datxTMstatus = _DatxTMstatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 5, 1, 1, 7),
    _DatxTMstatus_Type()
)
datxTMstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datxTMstatus.setStatus("mandatory")


class _DatxALstatus_Type(Integer32):
    """Custom type datxALstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_DatxALstatus_Type.__name__ = "Integer32"
_DatxALstatus_Object = MibTableColumn
datxALstatus = _DatxALstatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 5, 1, 1, 8),
    _DatxALstatus_Type()
)
datxALstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datxALstatus.setStatus("mandatory")


class _DatxDSRstatus_Type(Integer32):
    """Custom type datxDSRstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_DatxDSRstatus_Type.__name__ = "Integer32"
_DatxDSRstatus_Object = MibTableColumn
datxDSRstatus = _DatxDSRstatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 5, 1, 1, 9),
    _DatxDSRstatus_Type()
)
datxDSRstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datxDSRstatus.setStatus("mandatory")


class _DatxRXclock_Type(Integer32):
    """Custom type datxRXclock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_DatxRXclock_Type.__name__ = "Integer32"
_DatxRXclock_Object = MibTableColumn
datxRXclock = _DatxRXclock_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 5, 1, 1, 10),
    _DatxRXclock_Type()
)
datxRXclock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datxRXclock.setStatus("mandatory")


class _DatxTXclock_Type(Integer32):
    """Custom type datxTXclock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_DatxTXclock_Type.__name__ = "Integer32"
_DatxTXclock_Object = MibTableColumn
datxTXclock = _DatxTXclock_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 5, 1, 1, 11),
    _DatxTXclock_Type()
)
datxTXclock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datxTXclock.setStatus("mandatory")


class _DatxEXTclock_Type(Integer32):
    """Custom type datxEXTclock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_DatxEXTclock_Type.__name__ = "Integer32"
_DatxEXTclock_Object = MibTableColumn
datxEXTclock = _DatxEXTclock_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 5, 1, 1, 12),
    _DatxEXTclock_Type()
)
datxEXTclock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datxEXTclock.setStatus("mandatory")


class _DatxAlarmStatus_Type(OctetString):
    """Custom type datxAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DatxAlarmStatus_Type.__name__ = "OctetString"
_DatxAlarmStatus_Object = MibTableColumn
datxAlarmStatus = _DatxAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 7, 1, 5, 1, 1, 13),
    _DatxAlarmStatus_Type()
)
datxAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datxAlarmStatus.setStatus("mandatory")
_Dtx2011_ObjectIdentity = ObjectIdentity
dtx2011 = _Dtx2011_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 7, 2)
)
_Dtx2011AlarmData_ObjectIdentity = ObjectIdentity
dtx2011AlarmData = _Dtx2011AlarmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 7, 2, 1)
)
_Dtx2011NoResponseAlm_ObjectIdentity = ObjectIdentity
dtx2011NoResponseAlm = _Dtx2011NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 7, 2, 1, 1)
)
_Dtx2011DiagRxErrAlm_ObjectIdentity = ObjectIdentity
dtx2011DiagRxErrAlm = _Dtx2011DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 7, 2, 1, 2)
)
_Dtx2011PowerUpAlm_ObjectIdentity = ObjectIdentity
dtx2011PowerUpAlm = _Dtx2011PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 7, 2, 1, 3)
)
_Dtx2011DCDLossAlm_ObjectIdentity = ObjectIdentity
dtx2011DCDLossAlm = _Dtx2011DCDLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 7, 2, 1, 4)
)
_Dtx2011NoExtClockAlm_ObjectIdentity = ObjectIdentity
dtx2011NoExtClockAlm = _Dtx2011NoExtClockAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 7, 2, 1, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GDCDATX-MIB",
    **{"gdc": gdc,
       "datx": datx,
       "datxSystem": datxSystem,
       "datxVersion": datxVersion,
       "datxMIBversion": datxMIBversion,
       "datxMaintenance": datxMaintenance,
       "datxMaintTable": datxMaintTable,
       "datxMaintEntry": datxMaintEntry,
       "datxMaintIndex": datxMaintIndex,
       "datxFirmwareRev": datxFirmwareRev,
       "datxDefaultInit": datxDefaultInit,
       "datxFrontPanel": datxFrontPanel,
       "datxLedStatus": datxLedStatus,
       "datxConfiguration": datxConfiguration,
       "datxTransConfigTable": datxTransConfigTable,
       "datxTransConfigEntry": datxTransConfigEntry,
       "datxTransConfigIndex": datxTransConfigIndex,
       "datxBaudRate": datxBaudRate,
       "datxSyncTxClockSource": datxSyncTxClockSource,
       "datxEiaSyncClock": datxEiaSyncClock,
       "datxEiaConfigTable": datxEiaConfigTable,
       "datxEiaConfigEntry": datxEiaConfigEntry,
       "datxEIAIndex": datxEIAIndex,
       "datxCarrierControl": datxCarrierControl,
       "datxRtsMode": datxRtsMode,
       "datxRtsCtsDelay": datxRtsCtsDelay,
       "datxEiaRdlControl": datxEiaRdlControl,
       "datxDsrInAl": datxDsrInAl,
       "datxEiaAlControl": datxEiaAlControl,
       "datxMiscConfigTable": datxMiscConfigTable,
       "datxMiscConfigEntry": datxMiscConfigEntry,
       "datxMiscIndex": datxMiscIndex,
       "datxSystemStatusOption": datxSystemStatusOption,
       "datxDualSignalingTimer": datxDualSignalingTimer,
       "datxRegenCharLength": datxRegenCharLength,
       "datxRegenMode": datxRegenMode,
       "datxAsyncRate": datxAsyncRate,
       "datxDiagnostics": datxDiagnostics,
       "datxDiagnosticsTable": datxDiagnosticsTable,
       "datxDiagEntry": datxDiagEntry,
       "datxDiagnosticsIndex": datxDiagnosticsIndex,
       "datxDiagTest": datxDiagTest,
       "datxTestError": datxTestError,
       "datxTestDuration": datxTestDuration,
       "datxStatus": datxStatus,
       "datxStatusTable": datxStatusTable,
       "datxStatusEntry": datxStatusEntry,
       "datxStatusIndex": datxStatusIndex,
       "datxDTRstatus": datxDTRstatus,
       "datxRDLstatus": datxRDLstatus,
       "datxCOstatus": datxCOstatus,
       "datxCTSstatus": datxCTSstatus,
       "datxRTSstatus": datxRTSstatus,
       "datxTMstatus": datxTMstatus,
       "datxALstatus": datxALstatus,
       "datxDSRstatus": datxDSRstatus,
       "datxRXclock": datxRXclock,
       "datxTXclock": datxTXclock,
       "datxEXTclock": datxEXTclock,
       "datxAlarmStatus": datxAlarmStatus,
       "dtx2011": dtx2011,
       "dtx2011AlarmData": dtx2011AlarmData,
       "dtx2011NoResponseAlm": dtx2011NoResponseAlm,
       "dtx2011DiagRxErrAlm": dtx2011DiagRxErrAlm,
       "dtx2011PowerUpAlm": dtx2011PowerUpAlm,
       "dtx2011DCDLossAlm": dtx2011DCDLossAlm,
       "dtx2011NoExtClockAlm": dtx2011NoExtClockAlm}
)
