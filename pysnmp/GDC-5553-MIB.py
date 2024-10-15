# SNMP MIB module (GDC-5553-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GDC-5553-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:07 2024
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
_Sc5553_ObjectIdentity = ObjectIdentity
sc5553 = _Sc5553_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 5)
)
_Sc5553Version_ObjectIdentity = ObjectIdentity
sc5553Version = _Sc5553Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 1)
)


class _Sc5553MIBversion_Type(DisplayString):
    """Custom type sc5553MIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Sc5553MIBversion_Type.__name__ = "DisplayString"
_Sc5553MIBversion_Object = MibScalar
sc5553MIBversion = _Sc5553MIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 1, 1),
    _Sc5553MIBversion_Type()
)
sc5553MIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5553MIBversion.setStatus("mandatory")
_Sc5553VersionTable_Object = MibTable
sc5553VersionTable = _Sc5553VersionTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 1, 2)
)
if mibBuilder.loadTexts:
    sc5553VersionTable.setStatus("mandatory")
_Sc5553VersionEntry_Object = MibTableRow
sc5553VersionEntry = _Sc5553VersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 1, 2, 1)
)
sc5553VersionEntry.setIndexNames(
    (0, "GDC-5553-MIB", "sc5553VersionIndex"),
)
if mibBuilder.loadTexts:
    sc5553VersionEntry.setStatus("mandatory")
_Sc5553VersionIndex_Type = SCinstance
_Sc5553VersionIndex_Object = MibTableColumn
sc5553VersionIndex = _Sc5553VersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 1, 2, 1, 1),
    _Sc5553VersionIndex_Type()
)
sc5553VersionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5553VersionIndex.setStatus("mandatory")


class _Sc5553FirmwareRev_Type(DisplayString):
    """Custom type sc5553FirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Sc5553FirmwareRev_Type.__name__ = "DisplayString"
_Sc5553FirmwareRev_Object = MibTableColumn
sc5553FirmwareRev = _Sc5553FirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 1, 2, 1, 2),
    _Sc5553FirmwareRev_Type()
)
sc5553FirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5553FirmwareRev.setStatus("obsolete")


class _Sc5553ActiveFirmwareRev_Type(DisplayString):
    """Custom type sc5553ActiveFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Sc5553ActiveFirmwareRev_Type.__name__ = "DisplayString"
_Sc5553ActiveFirmwareRev_Object = MibTableColumn
sc5553ActiveFirmwareRev = _Sc5553ActiveFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 1, 2, 1, 3),
    _Sc5553ActiveFirmwareRev_Type()
)
sc5553ActiveFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5553ActiveFirmwareRev.setStatus("mandatory")


class _Sc5553StoredFirmwareRev_Type(DisplayString):
    """Custom type sc5553StoredFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Sc5553StoredFirmwareRev_Type.__name__ = "DisplayString"
_Sc5553StoredFirmwareRev_Object = MibTableColumn
sc5553StoredFirmwareRev = _Sc5553StoredFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 1, 2, 1, 4),
    _Sc5553StoredFirmwareRev_Type()
)
sc5553StoredFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5553StoredFirmwareRev.setStatus("mandatory")


class _Sc5553StoredFirmwareStatus_Type(Integer32):
    """Custom type sc5553StoredFirmwareStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("statBadUnZip", 6),
          ("statBlank", 1),
          ("statCheckSumBad", 4),
          ("statDownLoading", 2),
          ("statDownloadAborted", 7),
          ("statOK", 3),
          ("statUnZipping", 5))
    )


_Sc5553StoredFirmwareStatus_Type.__name__ = "Integer32"
_Sc5553StoredFirmwareStatus_Object = MibTableColumn
sc5553StoredFirmwareStatus = _Sc5553StoredFirmwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 1, 2, 1, 5),
    _Sc5553StoredFirmwareStatus_Type()
)
sc5553StoredFirmwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5553StoredFirmwareStatus.setStatus("mandatory")


class _Sc5553SwitchActiveFirmware_Type(Integer32):
    """Custom type sc5553SwitchActiveFirmware based on Integer32"""
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


_Sc5553SwitchActiveFirmware_Type.__name__ = "Integer32"
_Sc5553SwitchActiveFirmware_Object = MibTableColumn
sc5553SwitchActiveFirmware = _Sc5553SwitchActiveFirmware_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 1, 2, 1, 6),
    _Sc5553SwitchActiveFirmware_Type()
)
sc5553SwitchActiveFirmware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5553SwitchActiveFirmware.setStatus("mandatory")


class _Sc5553DownloadingMode_Type(Integer32):
    """Custom type sc5553DownloadingMode based on Integer32"""
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


_Sc5553DownloadingMode_Type.__name__ = "Integer32"
_Sc5553DownloadingMode_Object = MibTableColumn
sc5553DownloadingMode = _Sc5553DownloadingMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 1, 2, 1, 7),
    _Sc5553DownloadingMode_Type()
)
sc5553DownloadingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5553DownloadingMode.setStatus("mandatory")
_Sc5553Allocation_ObjectIdentity = ObjectIdentity
sc5553Allocation = _Sc5553Allocation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 2)
)
_Sc5553Ds0AllocationTable_Object = MibTable
sc5553Ds0AllocationTable = _Sc5553Ds0AllocationTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 2, 1)
)
if mibBuilder.loadTexts:
    sc5553Ds0AllocationTable.setStatus("mandatory")
_Sc5553Ds0AllocationEntry_Object = MibTableRow
sc5553Ds0AllocationEntry = _Sc5553Ds0AllocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 2, 1, 1)
)
sc5553Ds0AllocationEntry.setIndexNames(
    (0, "GDC-5553-MIB", "sc5553Ds0AllocationIndex"),
)
if mibBuilder.loadTexts:
    sc5553Ds0AllocationEntry.setStatus("mandatory")
_Sc5553Ds0AllocationIndex_Type = SCinstance
_Sc5553Ds0AllocationIndex_Object = MibTableColumn
sc5553Ds0AllocationIndex = _Sc5553Ds0AllocationIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 2, 1, 1, 1),
    _Sc5553Ds0AllocationIndex_Type()
)
sc5553Ds0AllocationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5553Ds0AllocationIndex.setStatus("mandatory")


class _Sc5553DS0BaseRate_Type(Integer32):
    """Custom type sc5553DS0BaseRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nx56k", 2),
          ("nx64k", 1))
    )


_Sc5553DS0BaseRate_Type.__name__ = "Integer32"
_Sc5553DS0BaseRate_Object = MibTableColumn
sc5553DS0BaseRate = _Sc5553DS0BaseRate_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 2, 1, 1, 2),
    _Sc5553DS0BaseRate_Type()
)
sc5553DS0BaseRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5553DS0BaseRate.setStatus("mandatory")


class _Sc5553Highway_Type(Integer32):
    """Custom type sc5553Highway based on Integer32"""
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
        *(("highway1", 1),
          ("highway2", 2),
          ("highway3", 3),
          ("highway4", 4))
    )


_Sc5553Highway_Type.__name__ = "Integer32"
_Sc5553Highway_Object = MibTableColumn
sc5553Highway = _Sc5553Highway_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 2, 1, 1, 3),
    _Sc5553Highway_Type()
)
sc5553Highway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5553Highway.setStatus("mandatory")


class _Sc5553DccDs0_Type(Integer32):
    """Custom type sc5553DccDs0 based on Integer32"""
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
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("dccDs01", 1),
          ("dccDs010", 10),
          ("dccDs011", 11),
          ("dccDs012", 12),
          ("dccDs013", 13),
          ("dccDs014", 14),
          ("dccDs015", 15),
          ("dccDs016", 16),
          ("dccDs017", 17),
          ("dccDs018", 18),
          ("dccDs019", 19),
          ("dccDs02", 2),
          ("dccDs020", 20),
          ("dccDs021", 21),
          ("dccDs022", 22),
          ("dccDs023", 23),
          ("dccDs024", 24),
          ("dccDs025", 25),
          ("dccDs026", 26),
          ("dccDs027", 27),
          ("dccDs028", 28),
          ("dccDs029", 29),
          ("dccDs03", 3),
          ("dccDs030", 30),
          ("dccDs031", 31),
          ("dccDs032", 32),
          ("dccDs04", 4),
          ("dccDs05", 5),
          ("dccDs06", 6),
          ("dccDs07", 7),
          ("dccDs08", 8),
          ("dccDs09", 9),
          ("noDccDs0", 33))
    )


_Sc5553DccDs0_Type.__name__ = "Integer32"
_Sc5553DccDs0_Object = MibTableColumn
sc5553DccDs0 = _Sc5553DccDs0_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 2, 1, 1, 4),
    _Sc5553DccDs0_Type()
)
sc5553DccDs0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5553DccDs0.setStatus("mandatory")


class _Sc5553DS0Allocation_Type(OctetString):
    """Custom type sc5553DS0Allocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Sc5553DS0Allocation_Type.__name__ = "OctetString"
_Sc5553DS0Allocation_Object = MibTableColumn
sc5553DS0Allocation = _Sc5553DS0Allocation_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 2, 1, 1, 5),
    _Sc5553DS0Allocation_Type()
)
sc5553DS0Allocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5553DS0Allocation.setStatus("mandatory")
_Sc5553Configuration_ObjectIdentity = ObjectIdentity
sc5553Configuration = _Sc5553Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 3)
)
_Sc5553ConfigTable_Object = MibTable
sc5553ConfigTable = _Sc5553ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 3, 1)
)
if mibBuilder.loadTexts:
    sc5553ConfigTable.setStatus("mandatory")
_Sc5553ConfigEntry_Object = MibTableRow
sc5553ConfigEntry = _Sc5553ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 3, 1, 1)
)
sc5553ConfigEntry.setIndexNames(
    (0, "GDC-5553-MIB", "sc5553ConfigIndex"),
)
if mibBuilder.loadTexts:
    sc5553ConfigEntry.setStatus("mandatory")
_Sc5553ConfigIndex_Type = SCinstance
_Sc5553ConfigIndex_Object = MibTableColumn
sc5553ConfigIndex = _Sc5553ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 3, 1, 1, 1),
    _Sc5553ConfigIndex_Type()
)
sc5553ConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5553ConfigIndex.setStatus("mandatory")


class _Sc5553ExternalTiming_Type(Integer32):
    """Custom type sc5553ExternalTiming based on Integer32"""
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


_Sc5553ExternalTiming_Type.__name__ = "Integer32"
_Sc5553ExternalTiming_Object = MibTableColumn
sc5553ExternalTiming = _Sc5553ExternalTiming_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 3, 1, 1, 2),
    _Sc5553ExternalTiming_Type()
)
sc5553ExternalTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5553ExternalTiming.setStatus("mandatory")


class _Sc5553ChannelType_Type(Integer32):
    """Custom type sc5553ChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eia530", 2),
          ("v35", 1))
    )


_Sc5553ChannelType_Type.__name__ = "Integer32"
_Sc5553ChannelType_Object = MibTableColumn
sc5553ChannelType = _Sc5553ChannelType_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 3, 1, 1, 3),
    _Sc5553ChannelType_Type()
)
sc5553ChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5553ChannelType.setStatus("mandatory")


class _Sc5553ClockInvert_Type(Integer32):
    """Custom type sc5553ClockInvert based on Integer32"""
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
        *(("txClockInvertRxClockInvert", 4),
          ("txClockInvertRxClockNorm", 3),
          ("txClockNormRxClockInvert", 2),
          ("txClockNormRxClockNorm", 1))
    )


_Sc5553ClockInvert_Type.__name__ = "Integer32"
_Sc5553ClockInvert_Object = MibTableColumn
sc5553ClockInvert = _Sc5553ClockInvert_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 3, 1, 1, 4),
    _Sc5553ClockInvert_Type()
)
sc5553ClockInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5553ClockInvert.setStatus("mandatory")


class _Sc5553DataInvert_Type(Integer32):
    """Custom type sc5553DataInvert based on Integer32"""
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
        *(("txDataInvertRxDataInvert", 4),
          ("txDataInvertRxDataNorm", 3),
          ("txDataNormRxDataInvert", 2),
          ("txDataNormRxDataNorm", 1))
    )


_Sc5553DataInvert_Type.__name__ = "Integer32"
_Sc5553DataInvert_Object = MibTableColumn
sc5553DataInvert = _Sc5553DataInvert_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 3, 1, 1, 5),
    _Sc5553DataInvert_Type()
)
sc5553DataInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5553DataInvert.setStatus("mandatory")


class _Sc5553ConstantDCD_Type(Integer32):
    """Custom type sc5553ConstantDCD based on Integer32"""
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


_Sc5553ConstantDCD_Type.__name__ = "Integer32"
_Sc5553ConstantDCD_Object = MibTableColumn
sc5553ConstantDCD = _Sc5553ConstantDCD_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 3, 1, 1, 6),
    _Sc5553ConstantDCD_Type()
)
sc5553ConstantDCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5553ConstantDCD.setStatus("mandatory")


class _Sc5553ConstantDSR_Type(Integer32):
    """Custom type sc5553ConstantDSR based on Integer32"""
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


_Sc5553ConstantDSR_Type.__name__ = "Integer32"
_Sc5553ConstantDSR_Object = MibTableColumn
sc5553ConstantDSR = _Sc5553ConstantDSR_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 3, 1, 1, 7),
    _Sc5553ConstantDSR_Type()
)
sc5553ConstantDSR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5553ConstantDSR.setStatus("mandatory")


class _Sc5553RTSCTScontrol_Type(Integer32):
    """Custom type sc5553RTSCTScontrol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ctsDelay10ms", 2),
          ("ctsDelayStandard", 3),
          ("ctsOn", 1))
    )


_Sc5553RTSCTScontrol_Type.__name__ = "Integer32"
_Sc5553RTSCTScontrol_Object = MibTableColumn
sc5553RTSCTScontrol = _Sc5553RTSCTScontrol_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 3, 1, 1, 8),
    _Sc5553RTSCTScontrol_Type()
)
sc5553RTSCTScontrol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5553RTSCTScontrol.setStatus("mandatory")


class _Sc5553ExtLLCtrl_Type(Integer32):
    """Custom type sc5553ExtLLCtrl based on Integer32"""
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


_Sc5553ExtLLCtrl_Type.__name__ = "Integer32"
_Sc5553ExtLLCtrl_Object = MibTableColumn
sc5553ExtLLCtrl = _Sc5553ExtLLCtrl_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 3, 1, 1, 9),
    _Sc5553ExtLLCtrl_Type()
)
sc5553ExtLLCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5553ExtLLCtrl.setStatus("mandatory")


class _Sc5553ExtRLCtrl_Type(Integer32):
    """Custom type sc5553ExtRLCtrl based on Integer32"""
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


_Sc5553ExtRLCtrl_Type.__name__ = "Integer32"
_Sc5553ExtRLCtrl_Object = MibTableColumn
sc5553ExtRLCtrl = _Sc5553ExtRLCtrl_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 3, 1, 1, 10),
    _Sc5553ExtRLCtrl_Type()
)
sc5553ExtRLCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5553ExtRLCtrl.setStatus("mandatory")


class _Sc5553InbandDccMode_Type(Integer32):
    """Custom type sc5553InbandDccMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dccDs0", 3),
          ("embedded", 2),
          ("none", 1))
    )


_Sc5553InbandDccMode_Type.__name__ = "Integer32"
_Sc5553InbandDccMode_Object = MibTableColumn
sc5553InbandDccMode = _Sc5553InbandDccMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 3, 1, 1, 11),
    _Sc5553InbandDccMode_Type()
)
sc5553InbandDccMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5553InbandDccMode.setStatus("mandatory")


class _Sc5553InbandLoop_Type(Integer32):
    """Custom type sc5553InbandLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("pn127", 2))
    )


_Sc5553InbandLoop_Type.__name__ = "Integer32"
_Sc5553InbandLoop_Object = MibTableColumn
sc5553InbandLoop = _Sc5553InbandLoop_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 3, 1, 1, 12),
    _Sc5553InbandLoop_Type()
)
sc5553InbandLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5553InbandLoop.setStatus("mandatory")


class _Sc5553InbandLoopdown_Type(Integer32):
    """Custom type sc5553InbandLoopdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("tenMinutes", 2))
    )


_Sc5553InbandLoopdown_Type.__name__ = "Integer32"
_Sc5553InbandLoopdown_Object = MibTableColumn
sc5553InbandLoopdown = _Sc5553InbandLoopdown_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 3, 1, 1, 13),
    _Sc5553InbandLoopdown_Type()
)
sc5553InbandLoopdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5553InbandLoopdown.setStatus("mandatory")


class _Sc5553WakeUpRemote_Type(DisplayString):
    """Custom type sc5553WakeUpRemote based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Sc5553WakeUpRemote_Type.__name__ = "DisplayString"
_Sc5553WakeUpRemote_Object = MibTableColumn
sc5553WakeUpRemote = _Sc5553WakeUpRemote_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 3, 1, 1, 14),
    _Sc5553WakeUpRemote_Type()
)
sc5553WakeUpRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5553WakeUpRemote.setStatus("mandatory")
_Sc5553DTEsignalStat_ObjectIdentity = ObjectIdentity
sc5553DTEsignalStat = _Sc5553DTEsignalStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 4)
)
_Sc5553SignalStatusTable_Object = MibTable
sc5553SignalStatusTable = _Sc5553SignalStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 4, 1)
)
if mibBuilder.loadTexts:
    sc5553SignalStatusTable.setStatus("mandatory")
_Sc5553SignalStatusEntry_Object = MibTableRow
sc5553SignalStatusEntry = _Sc5553SignalStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 4, 1, 1)
)
sc5553SignalStatusEntry.setIndexNames(
    (0, "GDC-5553-MIB", "sc5553SignalStatusIndex"),
)
if mibBuilder.loadTexts:
    sc5553SignalStatusEntry.setStatus("mandatory")
_Sc5553SignalStatusIndex_Type = SCinstance
_Sc5553SignalStatusIndex_Object = MibTableColumn
sc5553SignalStatusIndex = _Sc5553SignalStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 4, 1, 1, 1),
    _Sc5553SignalStatusIndex_Type()
)
sc5553SignalStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5553SignalStatusIndex.setStatus("mandatory")


class _Sc5553CTSstatus_Type(Integer32):
    """Custom type sc5553CTSstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("transitions", 3))
    )


_Sc5553CTSstatus_Type.__name__ = "Integer32"
_Sc5553CTSstatus_Object = MibTableColumn
sc5553CTSstatus = _Sc5553CTSstatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 4, 1, 1, 2),
    _Sc5553CTSstatus_Type()
)
sc5553CTSstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5553CTSstatus.setStatus("mandatory")


class _Sc5553RTSstatus_Type(Integer32):
    """Custom type sc5553RTSstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("transitions", 3))
    )


_Sc5553RTSstatus_Type.__name__ = "Integer32"
_Sc5553RTSstatus_Object = MibTableColumn
sc5553RTSstatus = _Sc5553RTSstatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 4, 1, 1, 3),
    _Sc5553RTSstatus_Type()
)
sc5553RTSstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5553RTSstatus.setStatus("mandatory")


class _Sc5553DTRstatus_Type(Integer32):
    """Custom type sc5553DTRstatus based on Integer32"""
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


_Sc5553DTRstatus_Type.__name__ = "Integer32"
_Sc5553DTRstatus_Object = MibTableColumn
sc5553DTRstatus = _Sc5553DTRstatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 4, 1, 1, 4),
    _Sc5553DTRstatus_Type()
)
sc5553DTRstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5553DTRstatus.setStatus("mandatory")


class _Sc5553DSRstatus_Type(Integer32):
    """Custom type sc5553DSRstatus based on Integer32"""
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


_Sc5553DSRstatus_Type.__name__ = "Integer32"
_Sc5553DSRstatus_Object = MibTableColumn
sc5553DSRstatus = _Sc5553DSRstatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 4, 1, 1, 5),
    _Sc5553DSRstatus_Type()
)
sc5553DSRstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5553DSRstatus.setStatus("mandatory")


class _Sc5553DCDstatus_Type(Integer32):
    """Custom type sc5553DCDstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("transitions", 3))
    )


_Sc5553DCDstatus_Type.__name__ = "Integer32"
_Sc5553DCDstatus_Object = MibTableColumn
sc5553DCDstatus = _Sc5553DCDstatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 4, 1, 1, 6),
    _Sc5553DCDstatus_Type()
)
sc5553DCDstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5553DCDstatus.setStatus("mandatory")


class _Sc5553RXCstatus_Type(Integer32):
    """Custom type sc5553RXCstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("transitions", 2))
    )


_Sc5553RXCstatus_Type.__name__ = "Integer32"
_Sc5553RXCstatus_Object = MibTableColumn
sc5553RXCstatus = _Sc5553RXCstatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 4, 1, 1, 7),
    _Sc5553RXCstatus_Type()
)
sc5553RXCstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5553RXCstatus.setStatus("mandatory")


class _Sc5553TXCstatus_Type(Integer32):
    """Custom type sc5553TXCstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("transitions", 2))
    )


_Sc5553TXCstatus_Type.__name__ = "Integer32"
_Sc5553TXCstatus_Object = MibTableColumn
sc5553TXCstatus = _Sc5553TXCstatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 4, 1, 1, 8),
    _Sc5553TXCstatus_Type()
)
sc5553TXCstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5553TXCstatus.setStatus("mandatory")


class _Sc5553RXDstatus_Type(Integer32):
    """Custom type sc5553RXDstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mark", 2),
          ("space", 1),
          ("transitions", 3))
    )


_Sc5553RXDstatus_Type.__name__ = "Integer32"
_Sc5553RXDstatus_Object = MibTableColumn
sc5553RXDstatus = _Sc5553RXDstatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 4, 1, 1, 9),
    _Sc5553RXDstatus_Type()
)
sc5553RXDstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5553RXDstatus.setStatus("mandatory")


class _Sc5553TXDstatus_Type(Integer32):
    """Custom type sc5553TXDstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mark", 2),
          ("space", 1),
          ("transitions", 3))
    )


_Sc5553TXDstatus_Type.__name__ = "Integer32"
_Sc5553TXDstatus_Object = MibTableColumn
sc5553TXDstatus = _Sc5553TXDstatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 4, 1, 1, 10),
    _Sc5553TXDstatus_Type()
)
sc5553TXDstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5553TXDstatus.setStatus("mandatory")


class _Sc5553ALTestLeadStatus_Type(Integer32):
    """Custom type sc5553ALTestLeadStatus based on Integer32"""
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


_Sc5553ALTestLeadStatus_Type.__name__ = "Integer32"
_Sc5553ALTestLeadStatus_Object = MibTableColumn
sc5553ALTestLeadStatus = _Sc5553ALTestLeadStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 4, 1, 1, 11),
    _Sc5553ALTestLeadStatus_Type()
)
sc5553ALTestLeadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5553ALTestLeadStatus.setStatus("mandatory")


class _Sc5553RLTestLeadStatus_Type(Integer32):
    """Custom type sc5553RLTestLeadStatus based on Integer32"""
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


_Sc5553RLTestLeadStatus_Type.__name__ = "Integer32"
_Sc5553RLTestLeadStatus_Object = MibTableColumn
sc5553RLTestLeadStatus = _Sc5553RLTestLeadStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 4, 1, 1, 12),
    _Sc5553RLTestLeadStatus_Type()
)
sc5553RLTestLeadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5553RLTestLeadStatus.setStatus("mandatory")
_Sc5553Diagnostics_ObjectIdentity = ObjectIdentity
sc5553Diagnostics = _Sc5553Diagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 5)
)
_Sc5553DiagTable_Object = MibTable
sc5553DiagTable = _Sc5553DiagTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 5, 1)
)
if mibBuilder.loadTexts:
    sc5553DiagTable.setStatus("mandatory")
_Sc5553DiagEntry_Object = MibTableRow
sc5553DiagEntry = _Sc5553DiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 5, 1, 1)
)
sc5553DiagEntry.setIndexNames(
    (0, "GDC-5553-MIB", "sc5553DiagIndex"),
)
if mibBuilder.loadTexts:
    sc5553DiagEntry.setStatus("mandatory")
_Sc5553DiagIndex_Type = SCinstance
_Sc5553DiagIndex_Object = MibTableColumn
sc5553DiagIndex = _Sc5553DiagIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 5, 1, 1, 1),
    _Sc5553DiagIndex_Type()
)
sc5553DiagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5553DiagIndex.setStatus("mandatory")


class _Sc5553DiagPattern_Type(Integer32):
    """Custom type sc5553DiagPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("send2047Pattern", 2),
          ("send511Pattern", 1))
    )


_Sc5553DiagPattern_Type.__name__ = "Integer32"
_Sc5553DiagPattern_Object = MibTableColumn
sc5553DiagPattern = _Sc5553DiagPattern_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 5, 1, 1, 2),
    _Sc5553DiagPattern_Type()
)
sc5553DiagPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5553DiagPattern.setStatus("mandatory")
_Sc5553DiagTestResults_Type = Integer32
_Sc5553DiagTestResults_Object = MibTableColumn
sc5553DiagTestResults = _Sc5553DiagTestResults_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 5, 1, 1, 3),
    _Sc5553DiagTestResults_Type()
)
sc5553DiagTestResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5553DiagTestResults.setStatus("mandatory")


class _Sc5553DiagTestDuration_Type(Integer32):
    """Custom type sc5553DiagTestDuration based on Integer32"""
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
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("testTime10Mins", 10),
          ("testTime15Mins", 11),
          ("testTime1Min", 1),
          ("testTime20Mins", 12),
          ("testTime25Mins", 13),
          ("testTime2Mins", 2),
          ("testTime30Mins", 14),
          ("testTime30Secs", 15),
          ("testTime3Mins", 3),
          ("testTime4Mins", 4),
          ("testTime5Mins", 5),
          ("testTime6Mins", 6),
          ("testTime7Mins", 7),
          ("testTime8Mins", 8),
          ("testTime9Mins", 9))
    )


_Sc5553DiagTestDuration_Type.__name__ = "Integer32"
_Sc5553DiagTestDuration_Object = MibTableColumn
sc5553DiagTestDuration = _Sc5553DiagTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 5, 1, 1, 4),
    _Sc5553DiagTestDuration_Type()
)
sc5553DiagTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5553DiagTestDuration.setStatus("mandatory")


class _Sc5553DiagTestSelection_Type(Integer32):
    """Custom type sc5553DiagTestSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("digitalLoop", 4),
          ("localloop", 2),
          ("localloopselftest", 3),
          ("networkdelay", 7),
          ("remoteloop", 5),
          ("remoteloopselftest", 6),
          ("stopTestorNoTest", 1))
    )


_Sc5553DiagTestSelection_Type.__name__ = "Integer32"
_Sc5553DiagTestSelection_Object = MibTableColumn
sc5553DiagTestSelection = _Sc5553DiagTestSelection_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 5, 1, 1, 5),
    _Sc5553DiagTestSelection_Type()
)
sc5553DiagTestSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5553DiagTestSelection.setStatus("mandatory")
_Sc5553Maintenance_ObjectIdentity = ObjectIdentity
sc5553Maintenance = _Sc5553Maintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 6)
)
_Sc5553MaintTable_Object = MibTable
sc5553MaintTable = _Sc5553MaintTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 6, 1)
)
if mibBuilder.loadTexts:
    sc5553MaintTable.setStatus("mandatory")
_Sc5553MaintEntry_Object = MibTableRow
sc5553MaintEntry = _Sc5553MaintEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 6, 1, 1)
)
sc5553MaintEntry.setIndexNames(
    (0, "GDC-5553-MIB", "sc5553MaintIndex"),
)
if mibBuilder.loadTexts:
    sc5553MaintEntry.setStatus("mandatory")
_Sc5553MaintIndex_Type = SCinstance
_Sc5553MaintIndex_Object = MibTableColumn
sc5553MaintIndex = _Sc5553MaintIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 6, 1, 1, 1),
    _Sc5553MaintIndex_Type()
)
sc5553MaintIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5553MaintIndex.setStatus("mandatory")


class _Sc5553LedStatus_Type(OctetString):
    """Custom type sc5553LedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Sc5553LedStatus_Type.__name__ = "OctetString"
_Sc5553LedStatus_Object = MibTableColumn
sc5553LedStatus = _Sc5553LedStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 6, 1, 1, 2),
    _Sc5553LedStatus_Type()
)
sc5553LedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc5553LedStatus.setStatus("mandatory")


class _Sc5553SoftReset_Type(Integer32):
    """Custom type sc5553SoftReset based on Integer32"""
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


_Sc5553SoftReset_Type.__name__ = "Integer32"
_Sc5553SoftReset_Object = MibTableColumn
sc5553SoftReset = _Sc5553SoftReset_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 6, 1, 1, 3),
    _Sc5553SoftReset_Type()
)
sc5553SoftReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5553SoftReset.setStatus("mandatory")


class _Sc5553FrontPanel_Type(Integer32):
    """Custom type sc5553FrontPanel based on Integer32"""
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


_Sc5553FrontPanel_Type.__name__ = "Integer32"
_Sc5553FrontPanel_Object = MibTableColumn
sc5553FrontPanel = _Sc5553FrontPanel_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 6, 1, 1, 4),
    _Sc5553FrontPanel_Type()
)
sc5553FrontPanel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5553FrontPanel.setStatus("mandatory")


class _Sc5553DefaultInit_Type(Integer32):
    """Custom type sc5553DefaultInit based on Integer32"""
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


_Sc5553DefaultInit_Type.__name__ = "Integer32"
_Sc5553DefaultInit_Object = MibTableColumn
sc5553DefaultInit = _Sc5553DefaultInit_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 6, 1, 1, 5),
    _Sc5553DefaultInit_Type()
)
sc5553DefaultInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc5553DefaultInit.setStatus("mandatory")
_Sc5553Alarms_ObjectIdentity = ObjectIdentity
sc5553Alarms = _Sc5553Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 7)
)
_Sc5553AlarmData_ObjectIdentity = ObjectIdentity
sc5553AlarmData = _Sc5553AlarmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 7, 1)
)
_Sc5553NoResponseAlm_ObjectIdentity = ObjectIdentity
sc5553NoResponseAlm = _Sc5553NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 7, 1, 1)
)
_Sc5553DiagRxErrAlm_ObjectIdentity = ObjectIdentity
sc5553DiagRxErrAlm = _Sc5553DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 7, 1, 2)
)
_Sc5553PowerUpAlm_ObjectIdentity = ObjectIdentity
sc5553PowerUpAlm = _Sc5553PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 7, 1, 3)
)
_Sc5553DTRLossAlarm_ObjectIdentity = ObjectIdentity
sc5553DTRLossAlarm = _Sc5553DTRLossAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 7, 1, 4)
)
_Sc5553DSRLossAlarm_ObjectIdentity = ObjectIdentity
sc5553DSRLossAlarm = _Sc5553DSRLossAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 7, 1, 5)
)
_Sc5553DCDLossAlarm_ObjectIdentity = ObjectIdentity
sc5553DCDLossAlarm = _Sc5553DCDLossAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 7, 1, 6)
)
_Sc5553TxCLossAlarm_ObjectIdentity = ObjectIdentity
sc5553TxCLossAlarm = _Sc5553TxCLossAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 7, 1, 7)
)
_Sc5553TimingLoss_ObjectIdentity = ObjectIdentity
sc5553TimingLoss = _Sc5553TimingLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 7, 1, 8)
)
_Sc5553EEPROMCheckAlarm_ObjectIdentity = ObjectIdentity
sc5553EEPROMCheckAlarm = _Sc5553EEPROMCheckAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 7, 1, 9)
)
_Sc5553EIATestAlarm_ObjectIdentity = ObjectIdentity
sc5553EIATestAlarm = _Sc5553EIATestAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 7, 1, 10)
)
_Sc5553FrontPanelTestAlarm_ObjectIdentity = ObjectIdentity
sc5553FrontPanelTestAlarm = _Sc5553FrontPanelTestAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 7, 1, 11)
)
_Sc5553TxDNoTransAlarm_ObjectIdentity = ObjectIdentity
sc5553TxDNoTransAlarm = _Sc5553TxDNoTransAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 7, 1, 12)
)
_Sc5553RxDNoTransAlarm_ObjectIdentity = ObjectIdentity
sc5553RxDNoTransAlarm = _Sc5553RxDNoTransAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 5, 7, 1, 13)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GDC-5553-MIB",
    **{"gdc": gdc,
       "dsx1": dsx1,
       "sc5553": sc5553,
       "sc5553Version": sc5553Version,
       "sc5553MIBversion": sc5553MIBversion,
       "sc5553VersionTable": sc5553VersionTable,
       "sc5553VersionEntry": sc5553VersionEntry,
       "sc5553VersionIndex": sc5553VersionIndex,
       "sc5553FirmwareRev": sc5553FirmwareRev,
       "sc5553ActiveFirmwareRev": sc5553ActiveFirmwareRev,
       "sc5553StoredFirmwareRev": sc5553StoredFirmwareRev,
       "sc5553StoredFirmwareStatus": sc5553StoredFirmwareStatus,
       "sc5553SwitchActiveFirmware": sc5553SwitchActiveFirmware,
       "sc5553DownloadingMode": sc5553DownloadingMode,
       "sc5553Allocation": sc5553Allocation,
       "sc5553Ds0AllocationTable": sc5553Ds0AllocationTable,
       "sc5553Ds0AllocationEntry": sc5553Ds0AllocationEntry,
       "sc5553Ds0AllocationIndex": sc5553Ds0AllocationIndex,
       "sc5553DS0BaseRate": sc5553DS0BaseRate,
       "sc5553Highway": sc5553Highway,
       "sc5553DccDs0": sc5553DccDs0,
       "sc5553DS0Allocation": sc5553DS0Allocation,
       "sc5553Configuration": sc5553Configuration,
       "sc5553ConfigTable": sc5553ConfigTable,
       "sc5553ConfigEntry": sc5553ConfigEntry,
       "sc5553ConfigIndex": sc5553ConfigIndex,
       "sc5553ExternalTiming": sc5553ExternalTiming,
       "sc5553ChannelType": sc5553ChannelType,
       "sc5553ClockInvert": sc5553ClockInvert,
       "sc5553DataInvert": sc5553DataInvert,
       "sc5553ConstantDCD": sc5553ConstantDCD,
       "sc5553ConstantDSR": sc5553ConstantDSR,
       "sc5553RTSCTScontrol": sc5553RTSCTScontrol,
       "sc5553ExtLLCtrl": sc5553ExtLLCtrl,
       "sc5553ExtRLCtrl": sc5553ExtRLCtrl,
       "sc5553InbandDccMode": sc5553InbandDccMode,
       "sc5553InbandLoop": sc5553InbandLoop,
       "sc5553InbandLoopdown": sc5553InbandLoopdown,
       "sc5553WakeUpRemote": sc5553WakeUpRemote,
       "sc5553DTEsignalStat": sc5553DTEsignalStat,
       "sc5553SignalStatusTable": sc5553SignalStatusTable,
       "sc5553SignalStatusEntry": sc5553SignalStatusEntry,
       "sc5553SignalStatusIndex": sc5553SignalStatusIndex,
       "sc5553CTSstatus": sc5553CTSstatus,
       "sc5553RTSstatus": sc5553RTSstatus,
       "sc5553DTRstatus": sc5553DTRstatus,
       "sc5553DSRstatus": sc5553DSRstatus,
       "sc5553DCDstatus": sc5553DCDstatus,
       "sc5553RXCstatus": sc5553RXCstatus,
       "sc5553TXCstatus": sc5553TXCstatus,
       "sc5553RXDstatus": sc5553RXDstatus,
       "sc5553TXDstatus": sc5553TXDstatus,
       "sc5553ALTestLeadStatus": sc5553ALTestLeadStatus,
       "sc5553RLTestLeadStatus": sc5553RLTestLeadStatus,
       "sc5553Diagnostics": sc5553Diagnostics,
       "sc5553DiagTable": sc5553DiagTable,
       "sc5553DiagEntry": sc5553DiagEntry,
       "sc5553DiagIndex": sc5553DiagIndex,
       "sc5553DiagPattern": sc5553DiagPattern,
       "sc5553DiagTestResults": sc5553DiagTestResults,
       "sc5553DiagTestDuration": sc5553DiagTestDuration,
       "sc5553DiagTestSelection": sc5553DiagTestSelection,
       "sc5553Maintenance": sc5553Maintenance,
       "sc5553MaintTable": sc5553MaintTable,
       "sc5553MaintEntry": sc5553MaintEntry,
       "sc5553MaintIndex": sc5553MaintIndex,
       "sc5553LedStatus": sc5553LedStatus,
       "sc5553SoftReset": sc5553SoftReset,
       "sc5553FrontPanel": sc5553FrontPanel,
       "sc5553DefaultInit": sc5553DefaultInit,
       "sc5553Alarms": sc5553Alarms,
       "sc5553AlarmData": sc5553AlarmData,
       "sc5553NoResponseAlm": sc5553NoResponseAlm,
       "sc5553DiagRxErrAlm": sc5553DiagRxErrAlm,
       "sc5553PowerUpAlm": sc5553PowerUpAlm,
       "sc5553DTRLossAlarm": sc5553DTRLossAlarm,
       "sc5553DSRLossAlarm": sc5553DSRLossAlarm,
       "sc5553DCDLossAlarm": sc5553DCDLossAlarm,
       "sc5553TxCLossAlarm": sc5553TxCLossAlarm,
       "sc5553TimingLoss": sc5553TimingLoss,
       "sc5553EEPROMCheckAlarm": sc5553EEPROMCheckAlarm,
       "sc5553EIATestAlarm": sc5553EIATestAlarm,
       "sc5553FrontPanelTestAlarm": sc5553FrontPanelTestAlarm,
       "sc5553TxDNoTransAlarm": sc5553TxDNoTransAlarm,
       "sc5553RxDNoTransAlarm": sc5553RxDNoTransAlarm}
)
