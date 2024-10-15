# SNMP MIB module (GDC-SC553-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GDC-SC553-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:09 2024
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

(gdc,) = mibBuilder.importSymbols(
    "GDCCMN-MIB",
    "gdc")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dsx1_ObjectIdentity = ObjectIdentity
dsx1 = _Dsx1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6)
)
_Sc553_ObjectIdentity = ObjectIdentity
sc553 = _Sc553_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11)
)
_Sc553Version_ObjectIdentity = ObjectIdentity
sc553Version = _Sc553Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 1)
)


class _Sc553MIBversion_Type(DisplayString):
    """Custom type sc553MIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Sc553MIBversion_Type.__name__ = "DisplayString"
_Sc553MIBversion_Object = MibScalar
sc553MIBversion = _Sc553MIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 1, 1),
    _Sc553MIBversion_Type()
)
sc553MIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553MIBversion.setStatus("mandatory")
_Sc553VersionTable_Object = MibTable
sc553VersionTable = _Sc553VersionTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 1, 2)
)
if mibBuilder.loadTexts:
    sc553VersionTable.setStatus("mandatory")
_Sc553VersionEntry_Object = MibTableRow
sc553VersionEntry = _Sc553VersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 1, 2, 1)
)
sc553VersionEntry.setIndexNames(
    (0, "GDC-SC553-MIB", "sc553VersionIndex"),
)
if mibBuilder.loadTexts:
    sc553VersionEntry.setStatus("mandatory")
_Sc553VersionIndex_Type = SCinstance
_Sc553VersionIndex_Object = MibTableColumn
sc553VersionIndex = _Sc553VersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 1, 2, 1, 1),
    _Sc553VersionIndex_Type()
)
sc553VersionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553VersionIndex.setStatus("mandatory")


class _Sc553ActiveFirmwareRev_Type(DisplayString):
    """Custom type sc553ActiveFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Sc553ActiveFirmwareRev_Type.__name__ = "DisplayString"
_Sc553ActiveFirmwareRev_Object = MibTableColumn
sc553ActiveFirmwareRev = _Sc553ActiveFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 1, 2, 1, 2),
    _Sc553ActiveFirmwareRev_Type()
)
sc553ActiveFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553ActiveFirmwareRev.setStatus("mandatory")


class _Sc553StoredFirmwareRev_Type(DisplayString):
    """Custom type sc553StoredFirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Sc553StoredFirmwareRev_Type.__name__ = "DisplayString"
_Sc553StoredFirmwareRev_Object = MibTableColumn
sc553StoredFirmwareRev = _Sc553StoredFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 1, 2, 1, 3),
    _Sc553StoredFirmwareRev_Type()
)
sc553StoredFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553StoredFirmwareRev.setStatus("mandatory")


class _Sc553BootRev_Type(DisplayString):
    """Custom type sc553BootRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Sc553BootRev_Type.__name__ = "DisplayString"
_Sc553BootRev_Object = MibTableColumn
sc553BootRev = _Sc553BootRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 1, 2, 1, 4),
    _Sc553BootRev_Type()
)
sc553BootRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553BootRev.setStatus("mandatory")


class _Sc553StoredFirmwareStatus_Type(Integer32):
    """Custom type sc553StoredFirmwareStatus based on Integer32"""
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


_Sc553StoredFirmwareStatus_Type.__name__ = "Integer32"
_Sc553StoredFirmwareStatus_Object = MibTableColumn
sc553StoredFirmwareStatus = _Sc553StoredFirmwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 1, 2, 1, 5),
    _Sc553StoredFirmwareStatus_Type()
)
sc553StoredFirmwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553StoredFirmwareStatus.setStatus("mandatory")


class _Sc553SwitchActiveFirmware_Type(Integer32):
    """Custom type sc553SwitchActiveFirmware based on Integer32"""
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


_Sc553SwitchActiveFirmware_Type.__name__ = "Integer32"
_Sc553SwitchActiveFirmware_Object = MibTableColumn
sc553SwitchActiveFirmware = _Sc553SwitchActiveFirmware_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 1, 2, 1, 6),
    _Sc553SwitchActiveFirmware_Type()
)
sc553SwitchActiveFirmware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553SwitchActiveFirmware.setStatus("mandatory")


class _Sc553DownloadingMode_Type(Integer32):
    """Custom type sc553DownloadingMode based on Integer32"""
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


_Sc553DownloadingMode_Type.__name__ = "Integer32"
_Sc553DownloadingMode_Object = MibTableColumn
sc553DownloadingMode = _Sc553DownloadingMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 1, 2, 1, 7),
    _Sc553DownloadingMode_Type()
)
sc553DownloadingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553DownloadingMode.setStatus("mandatory")
_Sc553Configuration_ObjectIdentity = ObjectIdentity
sc553Configuration = _Sc553Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2)
)
_Sc553ChannelConfigTable_Object = MibTable
sc553ChannelConfigTable = _Sc553ChannelConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 1)
)
if mibBuilder.loadTexts:
    sc553ChannelConfigTable.setStatus("mandatory")
_Sc553ChannelConfigEntry_Object = MibTableRow
sc553ChannelConfigEntry = _Sc553ChannelConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 1, 1)
)
sc553ChannelConfigEntry.setIndexNames(
    (0, "GDC-SC553-MIB", "sc553ChannelConfigIndex"),
)
if mibBuilder.loadTexts:
    sc553ChannelConfigEntry.setStatus("mandatory")
_Sc553ChannelConfigIndex_Type = SCinstance
_Sc553ChannelConfigIndex_Object = MibTableColumn
sc553ChannelConfigIndex = _Sc553ChannelConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 1, 1, 1),
    _Sc553ChannelConfigIndex_Type()
)
sc553ChannelConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553ChannelConfigIndex.setStatus("mandatory")


class _Sc553ChannelDS0AllocationScheme_Type(Integer32):
    """Custom type sc553ChannelDS0AllocationScheme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 2),
          ("consecutive", 1))
    )


_Sc553ChannelDS0AllocationScheme_Type.__name__ = "Integer32"
_Sc553ChannelDS0AllocationScheme_Object = MibTableColumn
sc553ChannelDS0AllocationScheme = _Sc553ChannelDS0AllocationScheme_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 1, 1, 2),
    _Sc553ChannelDS0AllocationScheme_Type()
)
sc553ChannelDS0AllocationScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553ChannelDS0AllocationScheme.setStatus("mandatory")


class _Sc553ChannelBaseRate_Type(Integer32):
    """Custom type sc553ChannelBaseRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nx56k", 1),
          ("nx64k", 2))
    )


_Sc553ChannelBaseRate_Type.__name__ = "Integer32"
_Sc553ChannelBaseRate_Object = MibTableColumn
sc553ChannelBaseRate = _Sc553ChannelBaseRate_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 1, 1, 3),
    _Sc553ChannelBaseRate_Type()
)
sc553ChannelBaseRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553ChannelBaseRate.setStatus("mandatory")


class _Sc553ChannelStartingDS0_Type(Integer32):
    """Custom type sc553ChannelStartingDS0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_Sc553ChannelStartingDS0_Type.__name__ = "Integer32"
_Sc553ChannelStartingDS0_Object = MibTableColumn
sc553ChannelStartingDS0 = _Sc553ChannelStartingDS0_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 1, 1, 4),
    _Sc553ChannelStartingDS0_Type()
)
sc553ChannelStartingDS0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553ChannelStartingDS0.setStatus("mandatory")


class _Sc553ChannelNumberOfDS0s_Type(Integer32):
    """Custom type sc553ChannelNumberOfDS0s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Sc553ChannelNumberOfDS0s_Type.__name__ = "Integer32"
_Sc553ChannelNumberOfDS0s_Object = MibTableColumn
sc553ChannelNumberOfDS0s = _Sc553ChannelNumberOfDS0s_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 1, 1, 5),
    _Sc553ChannelNumberOfDS0s_Type()
)
sc553ChannelNumberOfDS0s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553ChannelNumberOfDS0s.setStatus("mandatory")


class _Sc553ChannelInbandDccMode_Type(Integer32):
    """Custom type sc553ChannelInbandDccMode based on Integer32"""
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


_Sc553ChannelInbandDccMode_Type.__name__ = "Integer32"
_Sc553ChannelInbandDccMode_Object = MibTableColumn
sc553ChannelInbandDccMode = _Sc553ChannelInbandDccMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 1, 1, 6),
    _Sc553ChannelInbandDccMode_Type()
)
sc553ChannelInbandDccMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553ChannelInbandDccMode.setStatus("mandatory")


class _Sc553ChannelSplitTiming_Type(Integer32):
    """Custom type sc553ChannelSplitTiming based on Integer32"""
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


_Sc553ChannelSplitTiming_Type.__name__ = "Integer32"
_Sc553ChannelSplitTiming_Object = MibTableColumn
sc553ChannelSplitTiming = _Sc553ChannelSplitTiming_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 1, 1, 7),
    _Sc553ChannelSplitTiming_Type()
)
sc553ChannelSplitTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553ChannelSplitTiming.setStatus("mandatory")


class _Sc553ChannelChannelType_Type(Integer32):
    """Custom type sc553ChannelChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eia530", 3),
          ("none", 1),
          ("v35", 2))
    )


_Sc553ChannelChannelType_Type.__name__ = "Integer32"
_Sc553ChannelChannelType_Object = MibTableColumn
sc553ChannelChannelType = _Sc553ChannelChannelType_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 1, 1, 8),
    _Sc553ChannelChannelType_Type()
)
sc553ChannelChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553ChannelChannelType.setStatus("mandatory")


class _Sc553ChannelAdminClkInvert_Type(Integer32):
    """Custom type sc553ChannelAdminClkInvert based on Integer32"""
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
        *(("autoTxinvertRx", 6),
          ("autoTxnormRx", 5),
          ("both", 4),
          ("invertRx", 2),
          ("invertTx", 3),
          ("none", 1))
    )


_Sc553ChannelAdminClkInvert_Type.__name__ = "Integer32"
_Sc553ChannelAdminClkInvert_Object = MibTableColumn
sc553ChannelAdminClkInvert = _Sc553ChannelAdminClkInvert_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 1, 1, 9),
    _Sc553ChannelAdminClkInvert_Type()
)
sc553ChannelAdminClkInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553ChannelAdminClkInvert.setStatus("mandatory")


class _Sc553ChannelOperClkInvert_Type(Integer32):
    """Custom type sc553ChannelOperClkInvert based on Integer32"""
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
        *(("both", 4),
          ("invertRx", 2),
          ("invertTx", 3),
          ("none", 1))
    )


_Sc553ChannelOperClkInvert_Type.__name__ = "Integer32"
_Sc553ChannelOperClkInvert_Object = MibTableColumn
sc553ChannelOperClkInvert = _Sc553ChannelOperClkInvert_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 1, 1, 10),
    _Sc553ChannelOperClkInvert_Type()
)
sc553ChannelOperClkInvert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553ChannelOperClkInvert.setStatus("mandatory")


class _Sc553ChannelDataInvert_Type(Integer32):
    """Custom type sc553ChannelDataInvert based on Integer32"""
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
        *(("both", 4),
          ("invertRx", 2),
          ("invertTx", 3),
          ("none", 1))
    )


_Sc553ChannelDataInvert_Type.__name__ = "Integer32"
_Sc553ChannelDataInvert_Object = MibTableColumn
sc553ChannelDataInvert = _Sc553ChannelDataInvert_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 1, 1, 11),
    _Sc553ChannelDataInvert_Type()
)
sc553ChannelDataInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553ChannelDataInvert.setStatus("mandatory")


class _Sc553ChannelLocalDCD_Type(Integer32):
    """Custom type sc553ChannelLocalDCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("followsSignal", 1),
          ("forcedOn", 2))
    )


_Sc553ChannelLocalDCD_Type.__name__ = "Integer32"
_Sc553ChannelLocalDCD_Object = MibTableColumn
sc553ChannelLocalDCD = _Sc553ChannelLocalDCD_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 1, 1, 12),
    _Sc553ChannelLocalDCD_Type()
)
sc553ChannelLocalDCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553ChannelLocalDCD.setStatus("mandatory")


class _Sc553ChannelLocalDSR_Type(Integer32):
    """Custom type sc553ChannelLocalDSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("followsSignal", 1),
          ("forcedOn", 2))
    )


_Sc553ChannelLocalDSR_Type.__name__ = "Integer32"
_Sc553ChannelLocalDSR_Object = MibTableColumn
sc553ChannelLocalDSR = _Sc553ChannelLocalDSR_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 1, 1, 13),
    _Sc553ChannelLocalDSR_Type()
)
sc553ChannelLocalDSR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553ChannelLocalDSR.setStatus("mandatory")


class _Sc553ChannelRTSCTSControl_Type(Integer32):
    """Custom type sc553ChannelRTSCTSControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ctrl", 1),
          ("ctsForcedOn", 2))
    )


_Sc553ChannelRTSCTSControl_Type.__name__ = "Integer32"
_Sc553ChannelRTSCTSControl_Object = MibTableColumn
sc553ChannelRTSCTSControl = _Sc553ChannelRTSCTSControl_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 1, 1, 14),
    _Sc553ChannelRTSCTSControl_Type()
)
sc553ChannelRTSCTSControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553ChannelRTSCTSControl.setStatus("mandatory")


class _Sc553ChannelEIAtestLeads_Type(Integer32):
    """Custom type sc553ChannelEIAtestLeads based on Integer32"""
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


_Sc553ChannelEIAtestLeads_Type.__name__ = "Integer32"
_Sc553ChannelEIAtestLeads_Object = MibTableColumn
sc553ChannelEIAtestLeads = _Sc553ChannelEIAtestLeads_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 1, 1, 15),
    _Sc553ChannelEIAtestLeads_Type()
)
sc553ChannelEIAtestLeads.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553ChannelEIAtestLeads.setStatus("mandatory")


class _Sc553ChannelInbandLoop_Type(Integer32):
    """Custom type sc553ChannelInbandLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enabled", 2))
    )


_Sc553ChannelInbandLoop_Type.__name__ = "Integer32"
_Sc553ChannelInbandLoop_Object = MibTableColumn
sc553ChannelInbandLoop = _Sc553ChannelInbandLoop_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 1, 1, 16),
    _Sc553ChannelInbandLoop_Type()
)
sc553ChannelInbandLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553ChannelInbandLoop.setStatus("mandatory")


class _Sc553ChannelInbandLoopdown_Type(Integer32):
    """Custom type sc553ChannelInbandLoopdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable10Min", 2),
          ("inhibit", 1))
    )


_Sc553ChannelInbandLoopdown_Type.__name__ = "Integer32"
_Sc553ChannelInbandLoopdown_Object = MibTableColumn
sc553ChannelInbandLoopdown = _Sc553ChannelInbandLoopdown_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 1, 1, 17),
    _Sc553ChannelInbandLoopdown_Type()
)
sc553ChannelInbandLoopdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553ChannelInbandLoopdown.setStatus("mandatory")


class _Sc553channelRedundancy_Type(Integer32):
    """Custom type sc553channelRedundancy based on Integer32"""
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


_Sc553channelRedundancy_Type.__name__ = "Integer32"
_Sc553channelRedundancy_Object = MibTableColumn
sc553channelRedundancy = _Sc553channelRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 1, 1, 18),
    _Sc553channelRedundancy_Type()
)
sc553channelRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553channelRedundancy.setStatus("mandatory")


class _Sc553ChannelActivePort_Type(Integer32):
    """Custom type sc553ChannelActivePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cascade", 2),
          ("network", 1))
    )


_Sc553ChannelActivePort_Type.__name__ = "Integer32"
_Sc553ChannelActivePort_Object = MibTableColumn
sc553ChannelActivePort = _Sc553ChannelActivePort_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 1, 1, 19),
    _Sc553ChannelActivePort_Type()
)
sc553ChannelActivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553ChannelActivePort.setStatus("mandatory")


class _Sc553ChannelNetworkNumber_Type(Integer32):
    """Custom type sc553ChannelNetworkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("networkOne", 1),
          ("networkTwo", 2))
    )


_Sc553ChannelNetworkNumber_Type.__name__ = "Integer32"
_Sc553ChannelNetworkNumber_Object = MibTableColumn
sc553ChannelNetworkNumber = _Sc553ChannelNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 1, 1, 20),
    _Sc553ChannelNetworkNumber_Type()
)
sc553ChannelNetworkNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553ChannelNetworkNumber.setStatus("obsolete")


class _Sc553ChannelNetworkPosition_Type(Integer32):
    """Custom type sc553ChannelNetworkPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cascade", 2),
          ("network", 1))
    )


_Sc553ChannelNetworkPosition_Type.__name__ = "Integer32"
_Sc553ChannelNetworkPosition_Object = MibTableColumn
sc553ChannelNetworkPosition = _Sc553ChannelNetworkPosition_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 1, 1, 21),
    _Sc553ChannelNetworkPosition_Type()
)
sc553ChannelNetworkPosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553ChannelNetworkPosition.setStatus("obsolete")


class _Sc553WakeUpRemote_Type(DisplayString):
    """Custom type sc553WakeUpRemote based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Sc553WakeUpRemote_Type.__name__ = "DisplayString"
_Sc553WakeUpRemote_Object = MibTableColumn
sc553WakeUpRemote = _Sc553WakeUpRemote_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 1, 1, 22),
    _Sc553WakeUpRemote_Type()
)
sc553WakeUpRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553WakeUpRemote.setStatus("mandatory")


class _Sc553ChannelInService_Type(Integer32):
    """Custom type sc553ChannelInService based on Integer32"""
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


_Sc553ChannelInService_Type.__name__ = "Integer32"
_Sc553ChannelInService_Object = MibTableColumn
sc553ChannelInService = _Sc553ChannelInService_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 1, 1, 23),
    _Sc553ChannelInService_Type()
)
sc553ChannelInService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553ChannelInService.setStatus("mandatory")
_Sc553NetworkConfigTable_Object = MibTable
sc553NetworkConfigTable = _Sc553NetworkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 2)
)
if mibBuilder.loadTexts:
    sc553NetworkConfigTable.setStatus("mandatory")
_Sc553NetworkConfigEntry_Object = MibTableRow
sc553NetworkConfigEntry = _Sc553NetworkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 2, 1)
)
sc553NetworkConfigEntry.setIndexNames(
    (0, "GDC-SC553-MIB", "sc553NetworkConfigIndex"),
)
if mibBuilder.loadTexts:
    sc553NetworkConfigEntry.setStatus("mandatory")
_Sc553NetworkConfigIndex_Type = SCinstance
_Sc553NetworkConfigIndex_Object = MibTableColumn
sc553NetworkConfigIndex = _Sc553NetworkConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 2, 1, 1),
    _Sc553NetworkConfigIndex_Type()
)
sc553NetworkConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553NetworkConfigIndex.setStatus("mandatory")


class _Sc553NetworkAdminLineType_Type(Integer32):
    """Custom type sc553NetworkAdminLineType based on Integer32"""
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
        *(("auto", 4),
          ("manD4", 3),
          ("manEsf", 2),
          ("unframed", 1))
    )


_Sc553NetworkAdminLineType_Type.__name__ = "Integer32"
_Sc553NetworkAdminLineType_Object = MibTableColumn
sc553NetworkAdminLineType = _Sc553NetworkAdminLineType_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 2, 1, 2),
    _Sc553NetworkAdminLineType_Type()
)
sc553NetworkAdminLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553NetworkAdminLineType.setStatus("mandatory")


class _Sc553NetworkOperLineType_Type(Integer32):
    """Custom type sc553NetworkOperLineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("d4", 3),
          ("esf", 2),
          ("unframed", 1))
    )


_Sc553NetworkOperLineType_Type.__name__ = "Integer32"
_Sc553NetworkOperLineType_Object = MibTableColumn
sc553NetworkOperLineType = _Sc553NetworkOperLineType_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 2, 1, 3),
    _Sc553NetworkOperLineType_Type()
)
sc553NetworkOperLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553NetworkOperLineType.setStatus("mandatory")


class _Sc553NetworkInterfaceType_Type(Integer32):
    """Custom type sc553NetworkInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds1", 1),
          ("dsx1", 2))
    )


_Sc553NetworkInterfaceType_Type.__name__ = "Integer32"
_Sc553NetworkInterfaceType_Object = MibTableColumn
sc553NetworkInterfaceType = _Sc553NetworkInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 2, 1, 4),
    _Sc553NetworkInterfaceType_Type()
)
sc553NetworkInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553NetworkInterfaceType.setStatus("mandatory")


class _Sc553NetworkPreequalization_Type(Integer32):
    """Custom type sc553NetworkPreequalization based on Integer32"""
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
        *(("preeq130", 1),
          ("preeq260", 2),
          ("preeq390", 3),
          ("preeq530", 4),
          ("preeq655", 5))
    )


_Sc553NetworkPreequalization_Type.__name__ = "Integer32"
_Sc553NetworkPreequalization_Object = MibTableColumn
sc553NetworkPreequalization = _Sc553NetworkPreequalization_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 2, 1, 5),
    _Sc553NetworkPreequalization_Type()
)
sc553NetworkPreequalization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553NetworkPreequalization.setStatus("mandatory")


class _Sc553NetworkAdminLineBuildout_Type(Integer32):
    """Custom type sc553NetworkAdminLineBuildout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              11,
              12,
              13,
              16)
        )
    )
    namedValues = NamedValues(
        *(("auto", 16),
          ("man00dB", 10),
          ("man150dB", 12),
          ("man225dB", 13),
          ("man75dB", 11))
    )


_Sc553NetworkAdminLineBuildout_Type.__name__ = "Integer32"
_Sc553NetworkAdminLineBuildout_Object = MibTableColumn
sc553NetworkAdminLineBuildout = _Sc553NetworkAdminLineBuildout_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 2, 1, 6),
    _Sc553NetworkAdminLineBuildout_Type()
)
sc553NetworkAdminLineBuildout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553NetworkAdminLineBuildout.setStatus("mandatory")


class _Sc553NetworkOperLineBuildout_Type(Integer32):
    """Custom type sc553NetworkOperLineBuildout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("tx00dB", 2),
          ("tx150dB", 4),
          ("tx225dB", 5),
          ("tx75dB", 3))
    )


_Sc553NetworkOperLineBuildout_Type.__name__ = "Integer32"
_Sc553NetworkOperLineBuildout_Object = MibTableColumn
sc553NetworkOperLineBuildout = _Sc553NetworkOperLineBuildout_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 2, 1, 7),
    _Sc553NetworkOperLineBuildout_Type()
)
sc553NetworkOperLineBuildout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553NetworkOperLineBuildout.setStatus("mandatory")


class _Sc553NetworkOnesDensity_Type(Integer32):
    """Custom type sc553NetworkOnesDensity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("inhibit", 1),
          ("min1in8", 5),
          ("restrict8XNplus1", 4))
    )


_Sc553NetworkOnesDensity_Type.__name__ = "Integer32"
_Sc553NetworkOnesDensity_Object = MibTableColumn
sc553NetworkOnesDensity = _Sc553NetworkOnesDensity_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 2, 1, 8),
    _Sc553NetworkOnesDensity_Type()
)
sc553NetworkOnesDensity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553NetworkOnesDensity.setStatus("mandatory")


class _Sc553NetworkTransmitClockSource_Type(Integer32):
    """Custom type sc553NetworkTransmitClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cascade", 2),
          ("extChannelClkPPL", 6),
          ("internal", 4),
          ("receive", 1),
          ("station", 5))
    )


_Sc553NetworkTransmitClockSource_Type.__name__ = "Integer32"
_Sc553NetworkTransmitClockSource_Object = MibTableColumn
sc553NetworkTransmitClockSource = _Sc553NetworkTransmitClockSource_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 2, 1, 9),
    _Sc553NetworkTransmitClockSource_Type()
)
sc553NetworkTransmitClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553NetworkTransmitClockSource.setStatus("mandatory")


class _Sc553NetworkFallbackClockSource_Type(Integer32):
    """Custom type sc553NetworkFallbackClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cascade", 2),
          ("internal", 4),
          ("receive", 1))
    )


_Sc553NetworkFallbackClockSource_Type.__name__ = "Integer32"
_Sc553NetworkFallbackClockSource_Object = MibTableColumn
sc553NetworkFallbackClockSource = _Sc553NetworkFallbackClockSource_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 2, 1, 10),
    _Sc553NetworkFallbackClockSource_Type()
)
sc553NetworkFallbackClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553NetworkFallbackClockSource.setStatus("mandatory")


class _Sc553NetworkFDLdcc_Type(Integer32):
    """Custom type sc553NetworkFDLdcc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sc553NetworkFDLdcc_Type.__name__ = "Integer32"
_Sc553NetworkFDLdcc_Object = MibTableColumn
sc553NetworkFDLdcc = _Sc553NetworkFDLdcc_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 2, 1, 11),
    _Sc553NetworkFDLdcc_Type()
)
sc553NetworkFDLdcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553NetworkFDLdcc.setStatus("mandatory")


class _Sc553NetworkAISLoopdown_Type(Integer32):
    """Custom type sc553NetworkAISLoopdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60),
    )


_Sc553NetworkAISLoopdown_Type.__name__ = "Integer32"
_Sc553NetworkAISLoopdown_Object = MibTableColumn
sc553NetworkAISLoopdown = _Sc553NetworkAISLoopdown_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 2, 1, 12),
    _Sc553NetworkAISLoopdown_Type()
)
sc553NetworkAISLoopdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553NetworkAISLoopdown.setStatus("mandatory")


class _Sc553NetworkLoopbackConfig_Type(Integer32):
    """Custom type sc553NetworkLoopbackConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lineloop", 3),
          ("none", 1),
          ("payload", 2))
    )


_Sc553NetworkLoopbackConfig_Type.__name__ = "Integer32"
_Sc553NetworkLoopbackConfig_Object = MibTableColumn
sc553NetworkLoopbackConfig = _Sc553NetworkLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 2, 1, 13),
    _Sc553NetworkLoopbackConfig_Type()
)
sc553NetworkLoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553NetworkLoopbackConfig.setStatus("mandatory")


class _Sc553NetworkLineCoding_Type(Integer32):
    """Custom type sc553NetworkLineCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sc553AMI", 2),
          ("sc553B8ZS", 1))
    )


_Sc553NetworkLineCoding_Type.__name__ = "Integer32"
_Sc553NetworkLineCoding_Object = MibTableColumn
sc553NetworkLineCoding = _Sc553NetworkLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 2, 1, 14),
    _Sc553NetworkLineCoding_Type()
)
sc553NetworkLineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553NetworkLineCoding.setStatus("mandatory")


class _Sc553NetworkFdl_Type(Integer32):
    """Custom type sc553NetworkFdl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sc553Ansi-T1-403", 2),
          ("sc553Att-54016", 3),
          ("sc553Fdl-none", 1))
    )


_Sc553NetworkFdl_Type.__name__ = "Integer32"
_Sc553NetworkFdl_Object = MibTableColumn
sc553NetworkFdl = _Sc553NetworkFdl_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 2, 1, 15),
    _Sc553NetworkFdl_Type()
)
sc553NetworkFdl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553NetworkFdl.setStatus("mandatory")


class _Sc553ConfigurationSave_Type(Integer32):
    """Custom type sc553ConfigurationSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norm", 1),
          ("saveall", 2))
    )


_Sc553ConfigurationSave_Type.__name__ = "Integer32"
_Sc553ConfigurationSave_Object = MibScalar
sc553ConfigurationSave = _Sc553ConfigurationSave_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 3),
    _Sc553ConfigurationSave_Type()
)
sc553ConfigurationSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553ConfigurationSave.setStatus("mandatory")
_Sc553CascadeConfigTable_Object = MibTable
sc553CascadeConfigTable = _Sc553CascadeConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 4)
)
if mibBuilder.loadTexts:
    sc553CascadeConfigTable.setStatus("mandatory")
_Sc553CascadeConfigEntry_Object = MibTableRow
sc553CascadeConfigEntry = _Sc553CascadeConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 4, 1)
)
sc553CascadeConfigEntry.setIndexNames(
    (0, "GDC-SC553-MIB", "sc553CascadeConfigIndex"),
)
if mibBuilder.loadTexts:
    sc553CascadeConfigEntry.setStatus("mandatory")
_Sc553CascadeConfigIndex_Type = SCinstance
_Sc553CascadeConfigIndex_Object = MibTableColumn
sc553CascadeConfigIndex = _Sc553CascadeConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 4, 1, 1),
    _Sc553CascadeConfigIndex_Type()
)
sc553CascadeConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553CascadeConfigIndex.setStatus("mandatory")


class _Sc553CascadeAdminLineType_Type(Integer32):
    """Custom type sc553CascadeAdminLineType based on Integer32"""
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
        *(("auto", 4),
          ("manD4", 3),
          ("manEsf", 2),
          ("unframed", 1))
    )


_Sc553CascadeAdminLineType_Type.__name__ = "Integer32"
_Sc553CascadeAdminLineType_Object = MibTableColumn
sc553CascadeAdminLineType = _Sc553CascadeAdminLineType_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 4, 1, 2),
    _Sc553CascadeAdminLineType_Type()
)
sc553CascadeAdminLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553CascadeAdminLineType.setStatus("mandatory")


class _Sc553CascadeOperLineType_Type(Integer32):
    """Custom type sc553CascadeOperLineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("d4", 3),
          ("esf", 2),
          ("unframed", 1))
    )


_Sc553CascadeOperLineType_Type.__name__ = "Integer32"
_Sc553CascadeOperLineType_Object = MibTableColumn
sc553CascadeOperLineType = _Sc553CascadeOperLineType_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 4, 1, 3),
    _Sc553CascadeOperLineType_Type()
)
sc553CascadeOperLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553CascadeOperLineType.setStatus("mandatory")


class _Sc553CascadeInterfaceType_Type(Integer32):
    """Custom type sc553CascadeInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds1", 1),
          ("dsx1", 2))
    )


_Sc553CascadeInterfaceType_Type.__name__ = "Integer32"
_Sc553CascadeInterfaceType_Object = MibTableColumn
sc553CascadeInterfaceType = _Sc553CascadeInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 4, 1, 4),
    _Sc553CascadeInterfaceType_Type()
)
sc553CascadeInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553CascadeInterfaceType.setStatus("mandatory")


class _Sc553CascadePreequalization_Type(Integer32):
    """Custom type sc553CascadePreequalization based on Integer32"""
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
        *(("preeq130", 1),
          ("preeq260", 2),
          ("preeq390", 3),
          ("preeq530", 4),
          ("preeq655", 5))
    )


_Sc553CascadePreequalization_Type.__name__ = "Integer32"
_Sc553CascadePreequalization_Object = MibTableColumn
sc553CascadePreequalization = _Sc553CascadePreequalization_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 4, 1, 5),
    _Sc553CascadePreequalization_Type()
)
sc553CascadePreequalization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553CascadePreequalization.setStatus("mandatory")


class _Sc553CascadeAdminLineBuildout_Type(Integer32):
    """Custom type sc553CascadeAdminLineBuildout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              11,
              12,
              13,
              16)
        )
    )
    namedValues = NamedValues(
        *(("auto", 16),
          ("man00dB", 10),
          ("man150dB", 12),
          ("man225dB", 13),
          ("man75dB", 11))
    )


_Sc553CascadeAdminLineBuildout_Type.__name__ = "Integer32"
_Sc553CascadeAdminLineBuildout_Object = MibTableColumn
sc553CascadeAdminLineBuildout = _Sc553CascadeAdminLineBuildout_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 4, 1, 6),
    _Sc553CascadeAdminLineBuildout_Type()
)
sc553CascadeAdminLineBuildout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553CascadeAdminLineBuildout.setStatus("mandatory")


class _Sc553CascadeOperLineBuildout_Type(Integer32):
    """Custom type sc553CascadeOperLineBuildout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("tx00dB", 2),
          ("tx150dB", 4),
          ("tx225dB", 5),
          ("tx75dB", 3))
    )


_Sc553CascadeOperLineBuildout_Type.__name__ = "Integer32"
_Sc553CascadeOperLineBuildout_Object = MibTableColumn
sc553CascadeOperLineBuildout = _Sc553CascadeOperLineBuildout_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 4, 1, 7),
    _Sc553CascadeOperLineBuildout_Type()
)
sc553CascadeOperLineBuildout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553CascadeOperLineBuildout.setStatus("mandatory")


class _Sc553CascadeFDLdcc_Type(Integer32):
    """Custom type sc553CascadeFDLdcc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_Sc553CascadeFDLdcc_Type.__name__ = "Integer32"
_Sc553CascadeFDLdcc_Object = MibTableColumn
sc553CascadeFDLdcc = _Sc553CascadeFDLdcc_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 4, 1, 8),
    _Sc553CascadeFDLdcc_Type()
)
sc553CascadeFDLdcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553CascadeFDLdcc.setStatus("mandatory")


class _Sc553CascadeLineCoding_Type(Integer32):
    """Custom type sc553CascadeLineCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sc553AMI", 2),
          ("sc553B8ZS", 1))
    )


_Sc553CascadeLineCoding_Type.__name__ = "Integer32"
_Sc553CascadeLineCoding_Object = MibTableColumn
sc553CascadeLineCoding = _Sc553CascadeLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 4, 1, 9),
    _Sc553CascadeLineCoding_Type()
)
sc553CascadeLineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553CascadeLineCoding.setStatus("mandatory")


class _Sc553CascadeFdl_Type(Integer32):
    """Custom type sc553CascadeFdl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sc553Ansi-T1-403", 2),
          ("sc553Att-54016", 3),
          ("sc553Fdl-none", 1))
    )


_Sc553CascadeFdl_Type.__name__ = "Integer32"
_Sc553CascadeFdl_Object = MibTableColumn
sc553CascadeFdl = _Sc553CascadeFdl_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 4, 1, 10),
    _Sc553CascadeFdl_Type()
)
sc553CascadeFdl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553CascadeFdl.setStatus("mandatory")


class _Sc553CascadeInService_Type(Integer32):
    """Custom type sc553CascadeInService based on Integer32"""
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


_Sc553CascadeInService_Type.__name__ = "Integer32"
_Sc553CascadeInService_Object = MibTableColumn
sc553CascadeInService = _Sc553CascadeInService_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 4, 1, 11),
    _Sc553CascadeInService_Type()
)
sc553CascadeInService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553CascadeInService.setStatus("mandatory")


class _Sc553CascadeAISLoopdown_Type(Integer32):
    """Custom type sc553CascadeAISLoopdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60),
    )


_Sc553CascadeAISLoopdown_Type.__name__ = "Integer32"
_Sc553CascadeAISLoopdown_Object = MibTableColumn
sc553CascadeAISLoopdown = _Sc553CascadeAISLoopdown_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 4, 1, 12),
    _Sc553CascadeAISLoopdown_Type()
)
sc553CascadeAISLoopdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553CascadeAISLoopdown.setStatus("mandatory")


class _Sc553CascadeLoopbackConfig_Type(Integer32):
    """Custom type sc553CascadeLoopbackConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lineloop", 3),
          ("none", 1),
          ("payload", 2))
    )


_Sc553CascadeLoopbackConfig_Type.__name__ = "Integer32"
_Sc553CascadeLoopbackConfig_Object = MibTableColumn
sc553CascadeLoopbackConfig = _Sc553CascadeLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 2, 4, 1, 13),
    _Sc553CascadeLoopbackConfig_Type()
)
sc553CascadeLoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553CascadeLoopbackConfig.setStatus("mandatory")
_Sc553Diagnostics_ObjectIdentity = ObjectIdentity
sc553Diagnostics = _Sc553Diagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 3)
)
_Sc553DiagTable_Object = MibTable
sc553DiagTable = _Sc553DiagTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 3, 1)
)
if mibBuilder.loadTexts:
    sc553DiagTable.setStatus("mandatory")
_Sc553DiagEntry_Object = MibTableRow
sc553DiagEntry = _Sc553DiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 3, 1, 1)
)
sc553DiagEntry.setIndexNames(
    (0, "GDC-SC553-MIB", "sc553DiagIndex"),
)
if mibBuilder.loadTexts:
    sc553DiagEntry.setStatus("mandatory")
_Sc553DiagIndex_Type = SCinstance
_Sc553DiagIndex_Object = MibTableColumn
sc553DiagIndex = _Sc553DiagIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 3, 1, 1, 1),
    _Sc553DiagIndex_Type()
)
sc553DiagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553DiagIndex.setStatus("mandatory")


class _Sc553DiagTestDuration_Type(Integer32):
    """Custom type sc553DiagTestDuration based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("testTime10Mins", 11),
          ("testTime15Mins", 12),
          ("testTime1Min", 2),
          ("testTime20Mins", 13),
          ("testTime25Mins", 14),
          ("testTime2Mins", 3),
          ("testTime30Mins", 15),
          ("testTime30Secs", 1),
          ("testTime3Mins", 4),
          ("testTime4Mins", 5),
          ("testTime5Mins", 6),
          ("testTime6Mins", 7),
          ("testTime7Mins", 8),
          ("testTime8Mins", 9),
          ("testTime9Mins", 10),
          ("testTimeInfinite", 16))
    )


_Sc553DiagTestDuration_Type.__name__ = "Integer32"
_Sc553DiagTestDuration_Object = MibTableColumn
sc553DiagTestDuration = _Sc553DiagTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 3, 1, 1, 2),
    _Sc553DiagTestDuration_Type()
)
sc553DiagTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553DiagTestDuration.setStatus("mandatory")


class _Sc553DiagProgPattern_Type(Integer32):
    """Custom type sc553DiagProgPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Sc553DiagProgPattern_Type.__name__ = "Integer32"
_Sc553DiagProgPattern_Object = MibTableColumn
sc553DiagProgPattern = _Sc553DiagProgPattern_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 3, 1, 1, 3),
    _Sc553DiagProgPattern_Type()
)
sc553DiagProgPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553DiagProgPattern.setStatus("mandatory")


class _Sc553InsertBitError_Type(Integer32):
    """Custom type sc553InsertBitError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("insertBitErrorNorm", 1),
          ("insertOneBitError", 2))
    )


_Sc553InsertBitError_Type.__name__ = "Integer32"
_Sc553InsertBitError_Object = MibTableColumn
sc553InsertBitError = _Sc553InsertBitError_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 3, 1, 1, 4),
    _Sc553InsertBitError_Type()
)
sc553InsertBitError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553InsertBitError.setStatus("mandatory")


class _Sc553DiagDS0Number_Type(Integer32):
    """Custom type sc553DiagDS0Number based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Sc553DiagDS0Number_Type.__name__ = "Integer32"
_Sc553DiagDS0Number_Object = MibTableColumn
sc553DiagDS0Number = _Sc553DiagDS0Number_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 3, 1, 1, 5),
    _Sc553DiagDS0Number_Type()
)
sc553DiagDS0Number.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553DiagDS0Number.setStatus("mandatory")


class _Sc553DiagT1SelfTestPattern_Type(Integer32):
    """Custom type sc553DiagT1SelfTestPattern based on Integer32"""
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
        *(("t12047Pattern", 2),
          ("t13in24", 5),
          ("t1511Pattern", 1),
          ("t1ProgPattern", 4),
          ("t1QRSPattern", 3))
    )


_Sc553DiagT1SelfTestPattern_Type.__name__ = "Integer32"
_Sc553DiagT1SelfTestPattern_Object = MibTableColumn
sc553DiagT1SelfTestPattern = _Sc553DiagT1SelfTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 3, 1, 1, 6),
    _Sc553DiagT1SelfTestPattern_Type()
)
sc553DiagT1SelfTestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553DiagT1SelfTestPattern.setStatus("mandatory")


class _Sc553DiagT1Test_Type(Integer32):
    """Custom type sc553DiagT1Test based on Integer32"""
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
        *(("t1LineLoopback", 7),
          ("t1LocalSelfTest", 2),
          ("t1LocalTest", 4),
          ("t1NetworkInterface", 6),
          ("t1NoTest", 9),
          ("t1PayLoadLoopback", 8),
          ("t1RemoteSelfTest", 3),
          ("t1RemoteTest", 5),
          ("t1SelfTest", 1))
    )


_Sc553DiagT1Test_Type.__name__ = "Integer32"
_Sc553DiagT1Test_Object = MibTableColumn
sc553DiagT1Test = _Sc553DiagT1Test_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 3, 1, 1, 7),
    _Sc553DiagT1Test_Type()
)
sc553DiagT1Test.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553DiagT1Test.setStatus("mandatory")


class _Sc553DiagDS0SelfTestPattern_Type(Integer32):
    """Custom type sc553DiagDS0SelfTestPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds02047Pattern", 2),
          ("ds0511Pattern", 1))
    )


_Sc553DiagDS0SelfTestPattern_Type.__name__ = "Integer32"
_Sc553DiagDS0SelfTestPattern_Object = MibTableColumn
sc553DiagDS0SelfTestPattern = _Sc553DiagDS0SelfTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 3, 1, 1, 8),
    _Sc553DiagDS0SelfTestPattern_Type()
)
sc553DiagDS0SelfTestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553DiagDS0SelfTestPattern.setStatus("mandatory")


class _Sc553DiagDS0Test_Type(Integer32):
    """Custom type sc553DiagDS0Test based on Integer32"""
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
        *(("ds0CircuitDelay", 2),
          ("ds0Loopback", 3),
          ("ds0NoDS0Test", 4),
          ("ds0SelfTest", 1))
    )


_Sc553DiagDS0Test_Type.__name__ = "Integer32"
_Sc553DiagDS0Test_Object = MibTableColumn
sc553DiagDS0Test = _Sc553DiagDS0Test_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 3, 1, 1, 9),
    _Sc553DiagDS0Test_Type()
)
sc553DiagDS0Test.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553DiagDS0Test.setStatus("mandatory")


class _Sc553DiagChannelSelfTestPattern_Type(Integer32):
    """Custom type sc553DiagChannelSelfTestPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chan2047Pattern", 2),
          ("chan511Pattern", 1))
    )


_Sc553DiagChannelSelfTestPattern_Type.__name__ = "Integer32"
_Sc553DiagChannelSelfTestPattern_Object = MibTableColumn
sc553DiagChannelSelfTestPattern = _Sc553DiagChannelSelfTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 3, 1, 1, 10),
    _Sc553DiagChannelSelfTestPattern_Type()
)
sc553DiagChannelSelfTestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553DiagChannelSelfTestPattern.setStatus("mandatory")


class _Sc553DiagChannelTest_Type(Integer32):
    """Custom type sc553DiagChannelTest based on Integer32"""
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
        *(("chanLocalLoop", 5),
          ("chanLocalSelfTest", 2),
          ("chanNoTest", 7),
          ("chanRemoteDataLoop", 6),
          ("chanRemoteSelfTest", 3),
          ("chanSelfTest", 1),
          ("chandigitalLoop", 4))
    )


_Sc553DiagChannelTest_Type.__name__ = "Integer32"
_Sc553DiagChannelTest_Object = MibTableColumn
sc553DiagChannelTest = _Sc553DiagChannelTest_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 3, 1, 1, 11),
    _Sc553DiagChannelTest_Type()
)
sc553DiagChannelTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553DiagChannelTest.setStatus("mandatory")


class _Sc553DiagTestResults_Type(OctetString):
    """Custom type sc553DiagTestResults based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Sc553DiagTestResults_Type.__name__ = "OctetString"
_Sc553DiagTestResults_Object = MibTableColumn
sc553DiagTestResults = _Sc553DiagTestResults_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 3, 1, 1, 12),
    _Sc553DiagTestResults_Type()
)
sc553DiagTestResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553DiagTestResults.setStatus("mandatory")


class _Sc553DiagTestStatus_Type(Integer32):
    """Custom type sc553DiagTestStatus based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("statChanLocalLoop", 14),
          ("statChanLocalSelfTest", 11),
          ("statChanRemoteDataLoop", 15),
          ("statChanRemoteSelfTest", 12),
          ("statChanSelfTest", 10),
          ("statChandigitalLoop", 13),
          ("statDS0CircuitDelay", 17),
          ("statDS0Loopback", 18),
          ("statDS0SelfTest", 16),
          ("statNoTestinProgress", 1),
          ("statT1LineLoopback", 8),
          ("statT1LocalSelfTest", 3),
          ("statT1LocalTest", 5),
          ("statT1NetworkInterface", 7),
          ("statT1PayLoadLoopback", 9),
          ("statT1RemoteSelfTest", 4),
          ("statT1RemoteTest", 6),
          ("statT1SelfTest", 2))
    )


_Sc553DiagTestStatus_Type.__name__ = "Integer32"
_Sc553DiagTestStatus_Object = MibTableColumn
sc553DiagTestStatus = _Sc553DiagTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 3, 1, 1, 13),
    _Sc553DiagTestStatus_Type()
)
sc553DiagTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553DiagTestStatus.setStatus("mandatory")


class _Sc553DiagResetTestToNormal_Type(Integer32):
    """Custom type sc553DiagResetTestToNormal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("resetTest", 2))
    )


_Sc553DiagResetTestToNormal_Type.__name__ = "Integer32"
_Sc553DiagResetTestToNormal_Object = MibTableColumn
sc553DiagResetTestToNormal = _Sc553DiagResetTestToNormal_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 3, 1, 1, 14),
    _Sc553DiagResetTestToNormal_Type()
)
sc553DiagResetTestToNormal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553DiagResetTestToNormal.setStatus("mandatory")


class _Sc553DiagResetTestResults_Type(Integer32):
    """Custom type sc553DiagResetTestResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("resetTestResult", 2))
    )


_Sc553DiagResetTestResults_Type.__name__ = "Integer32"
_Sc553DiagResetTestResults_Object = MibTableColumn
sc553DiagResetTestResults = _Sc553DiagResetTestResults_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 3, 1, 1, 15),
    _Sc553DiagResetTestResults_Type()
)
sc553DiagResetTestResults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553DiagResetTestResults.setStatus("mandatory")


class _Sc553DiagT1TestDirection_Type(Integer32):
    """Custom type sc553DiagT1TestDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("toCascade", 2),
          ("toNetwork", 1))
    )


_Sc553DiagT1TestDirection_Type.__name__ = "Integer32"
_Sc553DiagT1TestDirection_Object = MibTableColumn
sc553DiagT1TestDirection = _Sc553DiagT1TestDirection_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 3, 1, 1, 16),
    _Sc553DiagT1TestDirection_Type()
)
sc553DiagT1TestDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553DiagT1TestDirection.setStatus("mandatory")


class _Sc553DiagDS0TestDirection_Type(Integer32):
    """Custom type sc553DiagDS0TestDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("toCascade", 2),
          ("toNetwork", 1))
    )


_Sc553DiagDS0TestDirection_Type.__name__ = "Integer32"
_Sc553DiagDS0TestDirection_Object = MibTableColumn
sc553DiagDS0TestDirection = _Sc553DiagDS0TestDirection_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 3, 1, 1, 17),
    _Sc553DiagDS0TestDirection_Type()
)
sc553DiagDS0TestDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553DiagDS0TestDirection.setStatus("mandatory")
_Sc553Maintenance_ObjectIdentity = ObjectIdentity
sc553Maintenance = _Sc553Maintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 4)
)
_Sc553MaintenanceTable_Object = MibTable
sc553MaintenanceTable = _Sc553MaintenanceTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 4, 1)
)
if mibBuilder.loadTexts:
    sc553MaintenanceTable.setStatus("mandatory")
_Sc553MaintenanceEntry_Object = MibTableRow
sc553MaintenanceEntry = _Sc553MaintenanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 4, 1, 1)
)
sc553MaintenanceEntry.setIndexNames(
    (0, "GDC-SC553-MIB", "sc553MaintenanceIndex"),
)
if mibBuilder.loadTexts:
    sc553MaintenanceEntry.setStatus("mandatory")
_Sc553MaintenanceIndex_Type = SCinstance
_Sc553MaintenanceIndex_Object = MibTableColumn
sc553MaintenanceIndex = _Sc553MaintenanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 4, 1, 1, 1),
    _Sc553MaintenanceIndex_Type()
)
sc553MaintenanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553MaintenanceIndex.setStatus("mandatory")


class _Sc553LedStatus_Type(OctetString):
    """Custom type sc553LedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_Sc553LedStatus_Type.__name__ = "OctetString"
_Sc553LedStatus_Object = MibTableColumn
sc553LedStatus = _Sc553LedStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 4, 1, 1, 2),
    _Sc553LedStatus_Type()
)
sc553LedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553LedStatus.setStatus("mandatory")


class _Sc553SoftReset_Type(Integer32):
    """Custom type sc553SoftReset based on Integer32"""
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


_Sc553SoftReset_Type.__name__ = "Integer32"
_Sc553SoftReset_Object = MibTableColumn
sc553SoftReset = _Sc553SoftReset_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 4, 1, 1, 3),
    _Sc553SoftReset_Type()
)
sc553SoftReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553SoftReset.setStatus("mandatory")


class _Sc553DefaultInit_Type(Integer32):
    """Custom type sc553DefaultInit based on Integer32"""
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


_Sc553DefaultInit_Type.__name__ = "Integer32"
_Sc553DefaultInit_Object = MibTableColumn
sc553DefaultInit = _Sc553DefaultInit_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 4, 1, 1, 4),
    _Sc553DefaultInit_Type()
)
sc553DefaultInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553DefaultInit.setStatus("mandatory")


class _Sc553FrontPanel_Type(Integer32):
    """Custom type sc553FrontPanel based on Integer32"""
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


_Sc553FrontPanel_Type.__name__ = "Integer32"
_Sc553FrontPanel_Object = MibTableColumn
sc553FrontPanel = _Sc553FrontPanel_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 4, 1, 1, 5),
    _Sc553FrontPanel_Type()
)
sc553FrontPanel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553FrontPanel.setStatus("mandatory")


class _Sc553ProductType_Type(Integer32):
    """Custom type sc553ProductType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("sc553", 1)
    )


_Sc553ProductType_Type.__name__ = "Integer32"
_Sc553ProductType_Object = MibTableColumn
sc553ProductType = _Sc553ProductType_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 4, 1, 1, 6),
    _Sc553ProductType_Type()
)
sc553ProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553ProductType.setStatus("mandatory")


class _Sc553ResetStatistics_Type(Integer32):
    """Custom type sc553ResetStatistics based on Integer32"""
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


_Sc553ResetStatistics_Type.__name__ = "Integer32"
_Sc553ResetStatistics_Object = MibTableColumn
sc553ResetStatistics = _Sc553ResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 4, 1, 1, 7),
    _Sc553ResetStatistics_Type()
)
sc553ResetStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553ResetStatistics.setStatus("mandatory")


class _Sc553ValidUserIntervals_Type(Integer32):
    """Custom type sc553ValidUserIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Sc553ValidUserIntervals_Type.__name__ = "Integer32"
_Sc553ValidUserIntervals_Object = MibTableColumn
sc553ValidUserIntervals = _Sc553ValidUserIntervals_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 4, 1, 1, 8),
    _Sc553ValidUserIntervals_Type()
)
sc553ValidUserIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553ValidUserIntervals.setStatus("mandatory")


class _Sc553ValidNetworkIntervals_Type(Integer32):
    """Custom type sc553ValidNetworkIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Sc553ValidNetworkIntervals_Type.__name__ = "Integer32"
_Sc553ValidNetworkIntervals_Object = MibTableColumn
sc553ValidNetworkIntervals = _Sc553ValidNetworkIntervals_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 4, 1, 1, 9),
    _Sc553ValidNetworkIntervals_Type()
)
sc553ValidNetworkIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553ValidNetworkIntervals.setStatus("mandatory")


class _Sc553ValidFarEndIntervals_Type(Integer32):
    """Custom type sc553ValidFarEndIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Sc553ValidFarEndIntervals_Type.__name__ = "Integer32"
_Sc553ValidFarEndIntervals_Object = MibTableColumn
sc553ValidFarEndIntervals = _Sc553ValidFarEndIntervals_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 4, 1, 1, 10),
    _Sc553ValidFarEndIntervals_Type()
)
sc553ValidFarEndIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553ValidFarEndIntervals.setStatus("mandatory")


class _Sc553CascadePresent_Type(Integer32):
    """Custom type sc553CascadePresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("present", 2))
    )


_Sc553CascadePresent_Type.__name__ = "Integer32"
_Sc553CascadePresent_Object = MibTableColumn
sc553CascadePresent = _Sc553CascadePresent_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 4, 1, 1, 11),
    _Sc553CascadePresent_Type()
)
sc553CascadePresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553CascadePresent.setStatus("mandatory")


class _Sc553ReceiveLevel_Type(Integer32):
    """Custom type sc553ReceiveLevel based on Integer32"""
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
        *(("invalidNiDSX1", 1),
          ("lessThanNeg22andOneHalf", 6),
          ("neg15toNeg22andOneHalf", 5),
          ("neg7andOneHalftoNeg15", 4),
          ("noSignal", 2),
          ("pos2toNeg7andOneHalf", 3))
    )


_Sc553ReceiveLevel_Type.__name__ = "Integer32"
_Sc553ReceiveLevel_Object = MibTableColumn
sc553ReceiveLevel = _Sc553ReceiveLevel_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 4, 1, 1, 12),
    _Sc553ReceiveLevel_Type()
)
sc553ReceiveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553ReceiveLevel.setStatus("mandatory")


class _Sc553DteStat_Type(OctetString):
    """Custom type sc553DteStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Sc553DteStat_Type.__name__ = "OctetString"
_Sc553DteStat_Object = MibTableColumn
sc553DteStat = _Sc553DteStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 4, 1, 1, 13),
    _Sc553DteStat_Type()
)
sc553DteStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553DteStat.setStatus("mandatory")


class _Sc553CasReceiveLevel_Type(Integer32):
    """Custom type sc553CasReceiveLevel based on Integer32"""
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
        *(("invalidNiDSX1", 1),
          ("lessThanNeg22andOneHalf", 6),
          ("neg15toNeg22andOneHalf", 5),
          ("neg7andOneHalftoNeg15", 4),
          ("noSignal", 2),
          ("pos2toNeg7andOneHalf", 3))
    )


_Sc553CasReceiveLevel_Type.__name__ = "Integer32"
_Sc553CasReceiveLevel_Object = MibTableColumn
sc553CasReceiveLevel = _Sc553CasReceiveLevel_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 4, 1, 1, 14),
    _Sc553CasReceiveLevel_Type()
)
sc553CasReceiveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553CasReceiveLevel.setStatus("mandatory")


class _Sc553ShelfType_Type(Integer32):
    """Custom type sc553ShelfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("spectracomm", 1),
          ("twinPack", 2))
    )


_Sc553ShelfType_Type.__name__ = "Integer32"
_Sc553ShelfType_Object = MibTableColumn
sc553ShelfType = _Sc553ShelfType_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 4, 1, 1, 15),
    _Sc553ShelfType_Type()
)
sc553ShelfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553ShelfType.setStatus("mandatory")


class _Sc553TwinPackPowerSupply_Type(Integer32):
    """Custom type sc553TwinPackPowerSupply based on Integer32"""
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
        *(("both", 4),
          ("bottomOnly", 2),
          ("none", 1),
          ("topOnly", 3))
    )


_Sc553TwinPackPowerSupply_Type.__name__ = "Integer32"
_Sc553TwinPackPowerSupply_Object = MibTableColumn
sc553TwinPackPowerSupply = _Sc553TwinPackPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 4, 1, 1, 16),
    _Sc553TwinPackPowerSupply_Type()
)
sc553TwinPackPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553TwinPackPowerSupply.setStatus("mandatory")


class _Sc553TestAllLeds_Type(Integer32):
    """Custom type sc553TestAllLeds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allLedsOFF", 2),
          ("allLedsON", 1))
    )


_Sc553TestAllLeds_Type.__name__ = "Integer32"
_Sc553TestAllLeds_Object = MibTableColumn
sc553TestAllLeds = _Sc553TestAllLeds_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 4, 1, 1, 17),
    _Sc553TestAllLeds_Type()
)
sc553TestAllLeds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553TestAllLeds.setStatus("mandatory")
_Sc553Alarms_ObjectIdentity = ObjectIdentity
sc553Alarms = _Sc553Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5)
)
_Sc553AlarmData_ObjectIdentity = ObjectIdentity
sc553AlarmData = _Sc553AlarmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 1)
)
_Sc553NoResponseAlm_ObjectIdentity = ObjectIdentity
sc553NoResponseAlm = _Sc553NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 1, 1)
)
_Sc553DiagRxErrAlm_ObjectIdentity = ObjectIdentity
sc553DiagRxErrAlm = _Sc553DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 1, 2)
)
_Sc553PowerUpAlm_ObjectIdentity = ObjectIdentity
sc553PowerUpAlm = _Sc553PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 1, 3)
)
_Sc553NvRamCorruptAlm_ObjectIdentity = ObjectIdentity
sc553NvRamCorruptAlm = _Sc553NvRamCorruptAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 1, 4)
)
_Sc553UnitFailureAlm_ObjectIdentity = ObjectIdentity
sc553UnitFailureAlm = _Sc553UnitFailureAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 1, 5)
)
_Sc553StatusChangeAlm_ObjectIdentity = ObjectIdentity
sc553StatusChangeAlm = _Sc553StatusChangeAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 1, 6)
)
_Sc553UnsolicitedTestAlm_ObjectIdentity = ObjectIdentity
sc553UnsolicitedTestAlm = _Sc553UnsolicitedTestAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 1, 7)
)
_Sc553FrontPanelTestAlm_ObjectIdentity = ObjectIdentity
sc553FrontPanelTestAlm = _Sc553FrontPanelTestAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 1, 8)
)
_Sc553ConfigChangeAlm_ObjectIdentity = ObjectIdentity
sc553ConfigChangeAlm = _Sc553ConfigChangeAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 1, 9)
)
_Sc553TimingLossAlm_ObjectIdentity = ObjectIdentity
sc553TimingLossAlm = _Sc553TimingLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 1, 10)
)
_Sc553LossOfSignalAlm_ObjectIdentity = ObjectIdentity
sc553LossOfSignalAlm = _Sc553LossOfSignalAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 1, 11)
)
_Sc553LossOfFrameAlm_ObjectIdentity = ObjectIdentity
sc553LossOfFrameAlm = _Sc553LossOfFrameAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 1, 12)
)
_Sc553AlarmIndicationSignalAlm_ObjectIdentity = ObjectIdentity
sc553AlarmIndicationSignalAlm = _Sc553AlarmIndicationSignalAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 1, 13)
)
_Sc553ReceivedYellowAlm_ObjectIdentity = ObjectIdentity
sc553ReceivedYellowAlm = _Sc553ReceivedYellowAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 1, 14)
)
_Sc553UnavailableSignalStateAlm_ObjectIdentity = ObjectIdentity
sc553UnavailableSignalStateAlm = _Sc553UnavailableSignalStateAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 1, 15)
)
_Sc553CrcErrorsAlm_ObjectIdentity = ObjectIdentity
sc553CrcErrorsAlm = _Sc553CrcErrorsAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 1, 16)
)
_Sc553BipolarViolationsAlm_ObjectIdentity = ObjectIdentity
sc553BipolarViolationsAlm = _Sc553BipolarViolationsAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 1, 17)
)
_Sc553LowAverageDensityAlm_ObjectIdentity = ObjectIdentity
sc553LowAverageDensityAlm = _Sc553LowAverageDensityAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 1, 18)
)
_Sc553ExternalTXClockLossAlm_ObjectIdentity = ObjectIdentity
sc553ExternalTXClockLossAlm = _Sc553ExternalTXClockLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 1, 19)
)
_Sc553DCDLossAlm_ObjectIdentity = ObjectIdentity
sc553DCDLossAlm = _Sc553DCDLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 1, 20)
)
_Sc553DSRLossAlm_ObjectIdentity = ObjectIdentity
sc553DSRLossAlm = _Sc553DSRLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 1, 21)
)
_Sc553DTRLossAlm_ObjectIdentity = ObjectIdentity
sc553DTRLossAlm = _Sc553DTRLossAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 1, 22)
)
_Sc553RXDNoTransitionsAlm_ObjectIdentity = ObjectIdentity
sc553RXDNoTransitionsAlm = _Sc553RXDNoTransitionsAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 1, 23)
)
_Sc553TXDNoTransitionsAlm_ObjectIdentity = ObjectIdentity
sc553TXDNoTransitionsAlm = _Sc553TXDNoTransitionsAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 1, 24)
)
_Sc553RedundancyOn_ObjectIdentity = ObjectIdentity
sc553RedundancyOn = _Sc553RedundancyOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 1, 25)
)
_Sc553RemoteNotResponding_ObjectIdentity = ObjectIdentity
sc553RemoteNotResponding = _Sc553RemoteNotResponding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 1, 26)
)
_Sc553TopPowerSupplyFail_ObjectIdentity = ObjectIdentity
sc553TopPowerSupplyFail = _Sc553TopPowerSupplyFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 1, 27)
)
_Sc553BottomPowerSupplyFail_ObjectIdentity = ObjectIdentity
sc553BottomPowerSupplyFail = _Sc553BottomPowerSupplyFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 1, 28)
)
_Sc553AlarmConfigTable_Object = MibTable
sc553AlarmConfigTable = _Sc553AlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 2)
)
if mibBuilder.loadTexts:
    sc553AlarmConfigTable.setStatus("mandatory")
_Sc553AlarmConfigEntry_Object = MibTableRow
sc553AlarmConfigEntry = _Sc553AlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 2, 1)
)
sc553AlarmConfigEntry.setIndexNames(
    (0, "GDC-SC553-MIB", "sc553AlarmConfigIndex"),
    (0, "GDC-SC553-MIB", "sc553AlarmConfigIdentifier"),
)
if mibBuilder.loadTexts:
    sc553AlarmConfigEntry.setStatus("mandatory")
_Sc553AlarmConfigIndex_Type = SCinstance
_Sc553AlarmConfigIndex_Object = MibTableColumn
sc553AlarmConfigIndex = _Sc553AlarmConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 2, 1, 1),
    _Sc553AlarmConfigIndex_Type()
)
sc553AlarmConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553AlarmConfigIndex.setStatus("mandatory")
_Sc553AlarmConfigIdentifier_Type = ObjectIdentifier
_Sc553AlarmConfigIdentifier_Object = MibTableColumn
sc553AlarmConfigIdentifier = _Sc553AlarmConfigIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 2, 1, 2),
    _Sc553AlarmConfigIdentifier_Type()
)
sc553AlarmConfigIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553AlarmConfigIdentifier.setStatus("mandatory")


class _Sc553AlarmCountWindow_Type(Integer32):
    """Custom type sc553AlarmCountWindow based on Integer32"""
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
        *(("last1hr", 4),
          ("last1min", 3),
          ("last1sec", 2),
          ("reportAll", 1),
          ("reportWhen", 5))
    )


_Sc553AlarmCountWindow_Type.__name__ = "Integer32"
_Sc553AlarmCountWindow_Object = MibTableColumn
sc553AlarmCountWindow = _Sc553AlarmCountWindow_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 2, 1, 3),
    _Sc553AlarmCountWindow_Type()
)
sc553AlarmCountWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553AlarmCountWindow.setStatus("mandatory")


class _Sc553AlarmCountThreshold_Type(Integer32):
    """Custom type sc553AlarmCountThreshold based on Integer32"""
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
        *(("thresGT10", 1),
          ("thresGT100", 2),
          ("thresGT1000", 3),
          ("thresGT10000", 4))
    )


_Sc553AlarmCountThreshold_Type.__name__ = "Integer32"
_Sc553AlarmCountThreshold_Object = MibTableColumn
sc553AlarmCountThreshold = _Sc553AlarmCountThreshold_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 5, 2, 1, 4),
    _Sc553AlarmCountThreshold_Type()
)
sc553AlarmCountThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553AlarmCountThreshold.setStatus("mandatory")
_Sc553Performance_ObjectIdentity = ObjectIdentity
sc553Performance = _Sc553Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6)
)
_Sc553CurrentUserTable_Object = MibTable
sc553CurrentUserTable = _Sc553CurrentUserTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 1)
)
if mibBuilder.loadTexts:
    sc553CurrentUserTable.setStatus("mandatory")
_Sc553CurrentUserEntry_Object = MibTableRow
sc553CurrentUserEntry = _Sc553CurrentUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 1, 1)
)
sc553CurrentUserEntry.setIndexNames(
    (0, "GDC-SC553-MIB", "sc553CurrentUserIndex"),
)
if mibBuilder.loadTexts:
    sc553CurrentUserEntry.setStatus("mandatory")
_Sc553CurrentUserIndex_Type = SCinstance
_Sc553CurrentUserIndex_Object = MibTableColumn
sc553CurrentUserIndex = _Sc553CurrentUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 1, 1, 1),
    _Sc553CurrentUserIndex_Type()
)
sc553CurrentUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553CurrentUserIndex.setStatus("mandatory")


class _Sc553CurrentUserStat_Type(OctetString):
    """Custom type sc553CurrentUserStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_Sc553CurrentUserStat_Type.__name__ = "OctetString"
_Sc553CurrentUserStat_Object = MibTableColumn
sc553CurrentUserStat = _Sc553CurrentUserStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 1, 1, 2),
    _Sc553CurrentUserStat_Type()
)
sc553CurrentUserStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553CurrentUserStat.setStatus("mandatory")
_Sc553CurrentNetworkTable_Object = MibTable
sc553CurrentNetworkTable = _Sc553CurrentNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 2)
)
if mibBuilder.loadTexts:
    sc553CurrentNetworkTable.setStatus("mandatory")
_Sc553CurrentNetworkEntry_Object = MibTableRow
sc553CurrentNetworkEntry = _Sc553CurrentNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 2, 1)
)
sc553CurrentNetworkEntry.setIndexNames(
    (0, "GDC-SC553-MIB", "sc553CurrentNetworkIndex"),
)
if mibBuilder.loadTexts:
    sc553CurrentNetworkEntry.setStatus("mandatory")
_Sc553CurrentNetworkIndex_Type = SCinstance
_Sc553CurrentNetworkIndex_Object = MibTableColumn
sc553CurrentNetworkIndex = _Sc553CurrentNetworkIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 2, 1, 1),
    _Sc553CurrentNetworkIndex_Type()
)
sc553CurrentNetworkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553CurrentNetworkIndex.setStatus("mandatory")


class _Sc553CurrentNetworkStat_Type(OctetString):
    """Custom type sc553CurrentNetworkStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_Sc553CurrentNetworkStat_Type.__name__ = "OctetString"
_Sc553CurrentNetworkStat_Object = MibTableColumn
sc553CurrentNetworkStat = _Sc553CurrentNetworkStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 2, 1, 2),
    _Sc553CurrentNetworkStat_Type()
)
sc553CurrentNetworkStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553CurrentNetworkStat.setStatus("mandatory")
_Sc553CurrentFarEndTable_Object = MibTable
sc553CurrentFarEndTable = _Sc553CurrentFarEndTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 3)
)
if mibBuilder.loadTexts:
    sc553CurrentFarEndTable.setStatus("mandatory")
_Sc553CurrentFarEndEntry_Object = MibTableRow
sc553CurrentFarEndEntry = _Sc553CurrentFarEndEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 3, 1)
)
sc553CurrentFarEndEntry.setIndexNames(
    (0, "GDC-SC553-MIB", "sc553CurrentFarEndIndex"),
)
if mibBuilder.loadTexts:
    sc553CurrentFarEndEntry.setStatus("mandatory")
_Sc553CurrentFarEndIndex_Type = SCinstance
_Sc553CurrentFarEndIndex_Object = MibTableColumn
sc553CurrentFarEndIndex = _Sc553CurrentFarEndIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 3, 1, 1),
    _Sc553CurrentFarEndIndex_Type()
)
sc553CurrentFarEndIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553CurrentFarEndIndex.setStatus("mandatory")


class _Sc553CurrentFarEndStat_Type(OctetString):
    """Custom type sc553CurrentFarEndStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_Sc553CurrentFarEndStat_Type.__name__ = "OctetString"
_Sc553CurrentFarEndStat_Object = MibTableColumn
sc553CurrentFarEndStat = _Sc553CurrentFarEndStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 3, 1, 2),
    _Sc553CurrentFarEndStat_Type()
)
sc553CurrentFarEndStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553CurrentFarEndStat.setStatus("mandatory")
_Sc553TotalUserTable_Object = MibTable
sc553TotalUserTable = _Sc553TotalUserTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 4)
)
if mibBuilder.loadTexts:
    sc553TotalUserTable.setStatus("mandatory")
_Sc553TotalUserEntry_Object = MibTableRow
sc553TotalUserEntry = _Sc553TotalUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 4, 1)
)
sc553TotalUserEntry.setIndexNames(
    (0, "GDC-SC553-MIB", "sc553TotalUserIndex"),
)
if mibBuilder.loadTexts:
    sc553TotalUserEntry.setStatus("mandatory")
_Sc553TotalUserIndex_Type = SCinstance
_Sc553TotalUserIndex_Object = MibTableColumn
sc553TotalUserIndex = _Sc553TotalUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 4, 1, 1),
    _Sc553TotalUserIndex_Type()
)
sc553TotalUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553TotalUserIndex.setStatus("mandatory")


class _Sc553TotalUserStat_Type(OctetString):
    """Custom type sc553TotalUserStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_Sc553TotalUserStat_Type.__name__ = "OctetString"
_Sc553TotalUserStat_Object = MibTableColumn
sc553TotalUserStat = _Sc553TotalUserStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 4, 1, 2),
    _Sc553TotalUserStat_Type()
)
sc553TotalUserStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553TotalUserStat.setStatus("mandatory")
_Sc553TotalNetworkTable_Object = MibTable
sc553TotalNetworkTable = _Sc553TotalNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 5)
)
if mibBuilder.loadTexts:
    sc553TotalNetworkTable.setStatus("mandatory")
_Sc553TotalNetworkEntry_Object = MibTableRow
sc553TotalNetworkEntry = _Sc553TotalNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 5, 1)
)
sc553TotalNetworkEntry.setIndexNames(
    (0, "GDC-SC553-MIB", "sc553TotalNetworkIndex"),
)
if mibBuilder.loadTexts:
    sc553TotalNetworkEntry.setStatus("mandatory")
_Sc553TotalNetworkIndex_Type = SCinstance
_Sc553TotalNetworkIndex_Object = MibTableColumn
sc553TotalNetworkIndex = _Sc553TotalNetworkIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 5, 1, 1),
    _Sc553TotalNetworkIndex_Type()
)
sc553TotalNetworkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553TotalNetworkIndex.setStatus("mandatory")


class _Sc553TotalNetworkStat_Type(OctetString):
    """Custom type sc553TotalNetworkStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_Sc553TotalNetworkStat_Type.__name__ = "OctetString"
_Sc553TotalNetworkStat_Object = MibTableColumn
sc553TotalNetworkStat = _Sc553TotalNetworkStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 5, 1, 2),
    _Sc553TotalNetworkStat_Type()
)
sc553TotalNetworkStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553TotalNetworkStat.setStatus("mandatory")
_Sc553TotalFarEndTable_Object = MibTable
sc553TotalFarEndTable = _Sc553TotalFarEndTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 6)
)
if mibBuilder.loadTexts:
    sc553TotalFarEndTable.setStatus("mandatory")
_Sc553TotalFarEndEntry_Object = MibTableRow
sc553TotalFarEndEntry = _Sc553TotalFarEndEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 6, 1)
)
sc553TotalFarEndEntry.setIndexNames(
    (0, "GDC-SC553-MIB", "sc553TotalFarEndIndex"),
)
if mibBuilder.loadTexts:
    sc553TotalFarEndEntry.setStatus("mandatory")
_Sc553TotalFarEndIndex_Type = SCinstance
_Sc553TotalFarEndIndex_Object = MibTableColumn
sc553TotalFarEndIndex = _Sc553TotalFarEndIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 6, 1, 1),
    _Sc553TotalFarEndIndex_Type()
)
sc553TotalFarEndIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553TotalFarEndIndex.setStatus("mandatory")


class _Sc553TotalFarEndStat_Type(OctetString):
    """Custom type sc553TotalFarEndStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_Sc553TotalFarEndStat_Type.__name__ = "OctetString"
_Sc553TotalFarEndStat_Object = MibTableColumn
sc553TotalFarEndStat = _Sc553TotalFarEndStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 6, 1, 2),
    _Sc553TotalFarEndStat_Type()
)
sc553TotalFarEndStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553TotalFarEndStat.setStatus("mandatory")
_Sc553UserIntervalTable_Object = MibTable
sc553UserIntervalTable = _Sc553UserIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 7)
)
if mibBuilder.loadTexts:
    sc553UserIntervalTable.setStatus("mandatory")
_Sc553UserIntervalEntry_Object = MibTableRow
sc553UserIntervalEntry = _Sc553UserIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 7, 1)
)
sc553UserIntervalEntry.setIndexNames(
    (0, "GDC-SC553-MIB", "sc553UserIntervalIndex"),
    (0, "GDC-SC553-MIB", "sc553UserIntervalNumber"),
)
if mibBuilder.loadTexts:
    sc553UserIntervalEntry.setStatus("mandatory")
_Sc553UserIntervalIndex_Type = SCinstance
_Sc553UserIntervalIndex_Object = MibTableColumn
sc553UserIntervalIndex = _Sc553UserIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 7, 1, 1),
    _Sc553UserIntervalIndex_Type()
)
sc553UserIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553UserIntervalIndex.setStatus("mandatory")


class _Sc553UserIntervalNumber_Type(Integer32):
    """Custom type sc553UserIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Sc553UserIntervalNumber_Type.__name__ = "Integer32"
_Sc553UserIntervalNumber_Object = MibTableColumn
sc553UserIntervalNumber = _Sc553UserIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 7, 1, 2),
    _Sc553UserIntervalNumber_Type()
)
sc553UserIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553UserIntervalNumber.setStatus("mandatory")


class _Sc553UserIntervalStats_Type(OctetString):
    """Custom type sc553UserIntervalStats based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_Sc553UserIntervalStats_Type.__name__ = "OctetString"
_Sc553UserIntervalStats_Object = MibTableColumn
sc553UserIntervalStats = _Sc553UserIntervalStats_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 7, 1, 3),
    _Sc553UserIntervalStats_Type()
)
sc553UserIntervalStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553UserIntervalStats.setStatus("mandatory")
_Sc553NetworkIntervalTable_Object = MibTable
sc553NetworkIntervalTable = _Sc553NetworkIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 8)
)
if mibBuilder.loadTexts:
    sc553NetworkIntervalTable.setStatus("mandatory")
_Sc553NetworkIntervalEntry_Object = MibTableRow
sc553NetworkIntervalEntry = _Sc553NetworkIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 8, 1)
)
sc553NetworkIntervalEntry.setIndexNames(
    (0, "GDC-SC553-MIB", "sc553NetworkIntervalIndex"),
    (0, "GDC-SC553-MIB", "sc553NetworkIntervalNumber"),
)
if mibBuilder.loadTexts:
    sc553NetworkIntervalEntry.setStatus("mandatory")
_Sc553NetworkIntervalIndex_Type = SCinstance
_Sc553NetworkIntervalIndex_Object = MibTableColumn
sc553NetworkIntervalIndex = _Sc553NetworkIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 8, 1, 1),
    _Sc553NetworkIntervalIndex_Type()
)
sc553NetworkIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553NetworkIntervalIndex.setStatus("mandatory")


class _Sc553NetworkIntervalNumber_Type(Integer32):
    """Custom type sc553NetworkIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Sc553NetworkIntervalNumber_Type.__name__ = "Integer32"
_Sc553NetworkIntervalNumber_Object = MibTableColumn
sc553NetworkIntervalNumber = _Sc553NetworkIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 8, 1, 2),
    _Sc553NetworkIntervalNumber_Type()
)
sc553NetworkIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553NetworkIntervalNumber.setStatus("mandatory")


class _Sc553NetworkIntervalStats_Type(OctetString):
    """Custom type sc553NetworkIntervalStats based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_Sc553NetworkIntervalStats_Type.__name__ = "OctetString"
_Sc553NetworkIntervalStats_Object = MibTableColumn
sc553NetworkIntervalStats = _Sc553NetworkIntervalStats_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 8, 1, 3),
    _Sc553NetworkIntervalStats_Type()
)
sc553NetworkIntervalStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553NetworkIntervalStats.setStatus("mandatory")
_Sc553FarEndIntervalTable_Object = MibTable
sc553FarEndIntervalTable = _Sc553FarEndIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 9)
)
if mibBuilder.loadTexts:
    sc553FarEndIntervalTable.setStatus("mandatory")
_Sc553FarEndIntervalEntry_Object = MibTableRow
sc553FarEndIntervalEntry = _Sc553FarEndIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 9, 1)
)
sc553FarEndIntervalEntry.setIndexNames(
    (0, "GDC-SC553-MIB", "sc553FarEndIntervalIndex"),
    (0, "GDC-SC553-MIB", "sc553FarEndIntervalNumber"),
)
if mibBuilder.loadTexts:
    sc553FarEndIntervalEntry.setStatus("mandatory")
_Sc553FarEndIntervalIndex_Type = SCinstance
_Sc553FarEndIntervalIndex_Object = MibTableColumn
sc553FarEndIntervalIndex = _Sc553FarEndIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 9, 1, 1),
    _Sc553FarEndIntervalIndex_Type()
)
sc553FarEndIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553FarEndIntervalIndex.setStatus("mandatory")


class _Sc553FarEndIntervalNumber_Type(Integer32):
    """Custom type sc553FarEndIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Sc553FarEndIntervalNumber_Type.__name__ = "Integer32"
_Sc553FarEndIntervalNumber_Object = MibTableColumn
sc553FarEndIntervalNumber = _Sc553FarEndIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 9, 1, 2),
    _Sc553FarEndIntervalNumber_Type()
)
sc553FarEndIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553FarEndIntervalNumber.setStatus("mandatory")


class _Sc553FarEndIntervalStats_Type(OctetString):
    """Custom type sc553FarEndIntervalStats based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_Sc553FarEndIntervalStats_Type.__name__ = "OctetString"
_Sc553FarEndIntervalStats_Object = MibTableColumn
sc553FarEndIntervalStats = _Sc553FarEndIntervalStats_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 9, 1, 3),
    _Sc553FarEndIntervalStats_Type()
)
sc553FarEndIntervalStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553FarEndIntervalStats.setStatus("mandatory")


class _Sc553StoreUserTotals_Type(Integer32):
    """Custom type sc553StoreUserTotals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("store", 2))
    )


_Sc553StoreUserTotals_Type.__name__ = "Integer32"
_Sc553StoreUserTotals_Object = MibScalar
sc553StoreUserTotals = _Sc553StoreUserTotals_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 10),
    _Sc553StoreUserTotals_Type()
)
sc553StoreUserTotals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553StoreUserTotals.setStatus("mandatory")


class _Sc553StoreUserIntervals_Type(Integer32):
    """Custom type sc553StoreUserIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("store", 2))
    )


_Sc553StoreUserIntervals_Type.__name__ = "Integer32"
_Sc553StoreUserIntervals_Object = MibScalar
sc553StoreUserIntervals = _Sc553StoreUserIntervals_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 11),
    _Sc553StoreUserIntervals_Type()
)
sc553StoreUserIntervals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc553StoreUserIntervals.setStatus("mandatory")


class _Sc553ShelfUserTotals_Type(OctetString):
    """Custom type sc553ShelfUserTotals based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 465),
    )


_Sc553ShelfUserTotals_Type.__name__ = "OctetString"
_Sc553ShelfUserTotals_Object = MibScalar
sc553ShelfUserTotals = _Sc553ShelfUserTotals_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 12),
    _Sc553ShelfUserTotals_Type()
)
sc553ShelfUserTotals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553ShelfUserTotals.setStatus("mandatory")
_Sc553ShelfUserIntvlsTable_Object = MibTable
sc553ShelfUserIntvlsTable = _Sc553ShelfUserIntvlsTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 13)
)
if mibBuilder.loadTexts:
    sc553ShelfUserIntvlsTable.setStatus("mandatory")
_Sc553ShelfUserIntervalsEntry_Object = MibTableRow
sc553ShelfUserIntervalsEntry = _Sc553ShelfUserIntervalsEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 13, 1)
)
sc553ShelfUserIntervalsEntry.setIndexNames(
    (0, "GDC-SC553-MIB", "sc553ShelfUserIntvlsIndex"),
)
if mibBuilder.loadTexts:
    sc553ShelfUserIntervalsEntry.setStatus("mandatory")


class _Sc553ShelfUserIntvlsIndex_Type(Integer32):
    """Custom type sc553ShelfUserIntvlsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Sc553ShelfUserIntvlsIndex_Type.__name__ = "Integer32"
_Sc553ShelfUserIntvlsIndex_Object = MibTableColumn
sc553ShelfUserIntvlsIndex = _Sc553ShelfUserIntvlsIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 13, 1, 1),
    _Sc553ShelfUserIntvlsIndex_Type()
)
sc553ShelfUserIntvlsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553ShelfUserIntvlsIndex.setStatus("mandatory")


class _Sc553ShelfUserIntervals_Type(OctetString):
    """Custom type sc553ShelfUserIntervals based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 465),
    )


_Sc553ShelfUserIntervals_Type.__name__ = "OctetString"
_Sc553ShelfUserIntervals_Object = MibTableColumn
sc553ShelfUserIntervals = _Sc553ShelfUserIntervals_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 11, 6, 13, 1, 2),
    _Sc553ShelfUserIntervals_Type()
)
sc553ShelfUserIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc553ShelfUserIntervals.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GDC-SC553-MIB",
    **{"dsx1": dsx1,
       "sc553": sc553,
       "sc553Version": sc553Version,
       "sc553MIBversion": sc553MIBversion,
       "sc553VersionTable": sc553VersionTable,
       "sc553VersionEntry": sc553VersionEntry,
       "sc553VersionIndex": sc553VersionIndex,
       "sc553ActiveFirmwareRev": sc553ActiveFirmwareRev,
       "sc553StoredFirmwareRev": sc553StoredFirmwareRev,
       "sc553BootRev": sc553BootRev,
       "sc553StoredFirmwareStatus": sc553StoredFirmwareStatus,
       "sc553SwitchActiveFirmware": sc553SwitchActiveFirmware,
       "sc553DownloadingMode": sc553DownloadingMode,
       "sc553Configuration": sc553Configuration,
       "sc553ChannelConfigTable": sc553ChannelConfigTable,
       "sc553ChannelConfigEntry": sc553ChannelConfigEntry,
       "sc553ChannelConfigIndex": sc553ChannelConfigIndex,
       "sc553ChannelDS0AllocationScheme": sc553ChannelDS0AllocationScheme,
       "sc553ChannelBaseRate": sc553ChannelBaseRate,
       "sc553ChannelStartingDS0": sc553ChannelStartingDS0,
       "sc553ChannelNumberOfDS0s": sc553ChannelNumberOfDS0s,
       "sc553ChannelInbandDccMode": sc553ChannelInbandDccMode,
       "sc553ChannelSplitTiming": sc553ChannelSplitTiming,
       "sc553ChannelChannelType": sc553ChannelChannelType,
       "sc553ChannelAdminClkInvert": sc553ChannelAdminClkInvert,
       "sc553ChannelOperClkInvert": sc553ChannelOperClkInvert,
       "sc553ChannelDataInvert": sc553ChannelDataInvert,
       "sc553ChannelLocalDCD": sc553ChannelLocalDCD,
       "sc553ChannelLocalDSR": sc553ChannelLocalDSR,
       "sc553ChannelRTSCTSControl": sc553ChannelRTSCTSControl,
       "sc553ChannelEIAtestLeads": sc553ChannelEIAtestLeads,
       "sc553ChannelInbandLoop": sc553ChannelInbandLoop,
       "sc553ChannelInbandLoopdown": sc553ChannelInbandLoopdown,
       "sc553channelRedundancy": sc553channelRedundancy,
       "sc553ChannelActivePort": sc553ChannelActivePort,
       "sc553ChannelNetworkNumber": sc553ChannelNetworkNumber,
       "sc553ChannelNetworkPosition": sc553ChannelNetworkPosition,
       "sc553WakeUpRemote": sc553WakeUpRemote,
       "sc553ChannelInService": sc553ChannelInService,
       "sc553NetworkConfigTable": sc553NetworkConfigTable,
       "sc553NetworkConfigEntry": sc553NetworkConfigEntry,
       "sc553NetworkConfigIndex": sc553NetworkConfigIndex,
       "sc553NetworkAdminLineType": sc553NetworkAdminLineType,
       "sc553NetworkOperLineType": sc553NetworkOperLineType,
       "sc553NetworkInterfaceType": sc553NetworkInterfaceType,
       "sc553NetworkPreequalization": sc553NetworkPreequalization,
       "sc553NetworkAdminLineBuildout": sc553NetworkAdminLineBuildout,
       "sc553NetworkOperLineBuildout": sc553NetworkOperLineBuildout,
       "sc553NetworkOnesDensity": sc553NetworkOnesDensity,
       "sc553NetworkTransmitClockSource": sc553NetworkTransmitClockSource,
       "sc553NetworkFallbackClockSource": sc553NetworkFallbackClockSource,
       "sc553NetworkFDLdcc": sc553NetworkFDLdcc,
       "sc553NetworkAISLoopdown": sc553NetworkAISLoopdown,
       "sc553NetworkLoopbackConfig": sc553NetworkLoopbackConfig,
       "sc553NetworkLineCoding": sc553NetworkLineCoding,
       "sc553NetworkFdl": sc553NetworkFdl,
       "sc553ConfigurationSave": sc553ConfigurationSave,
       "sc553CascadeConfigTable": sc553CascadeConfigTable,
       "sc553CascadeConfigEntry": sc553CascadeConfigEntry,
       "sc553CascadeConfigIndex": sc553CascadeConfigIndex,
       "sc553CascadeAdminLineType": sc553CascadeAdminLineType,
       "sc553CascadeOperLineType": sc553CascadeOperLineType,
       "sc553CascadeInterfaceType": sc553CascadeInterfaceType,
       "sc553CascadePreequalization": sc553CascadePreequalization,
       "sc553CascadeAdminLineBuildout": sc553CascadeAdminLineBuildout,
       "sc553CascadeOperLineBuildout": sc553CascadeOperLineBuildout,
       "sc553CascadeFDLdcc": sc553CascadeFDLdcc,
       "sc553CascadeLineCoding": sc553CascadeLineCoding,
       "sc553CascadeFdl": sc553CascadeFdl,
       "sc553CascadeInService": sc553CascadeInService,
       "sc553CascadeAISLoopdown": sc553CascadeAISLoopdown,
       "sc553CascadeLoopbackConfig": sc553CascadeLoopbackConfig,
       "sc553Diagnostics": sc553Diagnostics,
       "sc553DiagTable": sc553DiagTable,
       "sc553DiagEntry": sc553DiagEntry,
       "sc553DiagIndex": sc553DiagIndex,
       "sc553DiagTestDuration": sc553DiagTestDuration,
       "sc553DiagProgPattern": sc553DiagProgPattern,
       "sc553InsertBitError": sc553InsertBitError,
       "sc553DiagDS0Number": sc553DiagDS0Number,
       "sc553DiagT1SelfTestPattern": sc553DiagT1SelfTestPattern,
       "sc553DiagT1Test": sc553DiagT1Test,
       "sc553DiagDS0SelfTestPattern": sc553DiagDS0SelfTestPattern,
       "sc553DiagDS0Test": sc553DiagDS0Test,
       "sc553DiagChannelSelfTestPattern": sc553DiagChannelSelfTestPattern,
       "sc553DiagChannelTest": sc553DiagChannelTest,
       "sc553DiagTestResults": sc553DiagTestResults,
       "sc553DiagTestStatus": sc553DiagTestStatus,
       "sc553DiagResetTestToNormal": sc553DiagResetTestToNormal,
       "sc553DiagResetTestResults": sc553DiagResetTestResults,
       "sc553DiagT1TestDirection": sc553DiagT1TestDirection,
       "sc553DiagDS0TestDirection": sc553DiagDS0TestDirection,
       "sc553Maintenance": sc553Maintenance,
       "sc553MaintenanceTable": sc553MaintenanceTable,
       "sc553MaintenanceEntry": sc553MaintenanceEntry,
       "sc553MaintenanceIndex": sc553MaintenanceIndex,
       "sc553LedStatus": sc553LedStatus,
       "sc553SoftReset": sc553SoftReset,
       "sc553DefaultInit": sc553DefaultInit,
       "sc553FrontPanel": sc553FrontPanel,
       "sc553ProductType": sc553ProductType,
       "sc553ResetStatistics": sc553ResetStatistics,
       "sc553ValidUserIntervals": sc553ValidUserIntervals,
       "sc553ValidNetworkIntervals": sc553ValidNetworkIntervals,
       "sc553ValidFarEndIntervals": sc553ValidFarEndIntervals,
       "sc553CascadePresent": sc553CascadePresent,
       "sc553ReceiveLevel": sc553ReceiveLevel,
       "sc553DteStat": sc553DteStat,
       "sc553CasReceiveLevel": sc553CasReceiveLevel,
       "sc553ShelfType": sc553ShelfType,
       "sc553TwinPackPowerSupply": sc553TwinPackPowerSupply,
       "sc553TestAllLeds": sc553TestAllLeds,
       "sc553Alarms": sc553Alarms,
       "sc553AlarmData": sc553AlarmData,
       "sc553NoResponseAlm": sc553NoResponseAlm,
       "sc553DiagRxErrAlm": sc553DiagRxErrAlm,
       "sc553PowerUpAlm": sc553PowerUpAlm,
       "sc553NvRamCorruptAlm": sc553NvRamCorruptAlm,
       "sc553UnitFailureAlm": sc553UnitFailureAlm,
       "sc553StatusChangeAlm": sc553StatusChangeAlm,
       "sc553UnsolicitedTestAlm": sc553UnsolicitedTestAlm,
       "sc553FrontPanelTestAlm": sc553FrontPanelTestAlm,
       "sc553ConfigChangeAlm": sc553ConfigChangeAlm,
       "sc553TimingLossAlm": sc553TimingLossAlm,
       "sc553LossOfSignalAlm": sc553LossOfSignalAlm,
       "sc553LossOfFrameAlm": sc553LossOfFrameAlm,
       "sc553AlarmIndicationSignalAlm": sc553AlarmIndicationSignalAlm,
       "sc553ReceivedYellowAlm": sc553ReceivedYellowAlm,
       "sc553UnavailableSignalStateAlm": sc553UnavailableSignalStateAlm,
       "sc553CrcErrorsAlm": sc553CrcErrorsAlm,
       "sc553BipolarViolationsAlm": sc553BipolarViolationsAlm,
       "sc553LowAverageDensityAlm": sc553LowAverageDensityAlm,
       "sc553ExternalTXClockLossAlm": sc553ExternalTXClockLossAlm,
       "sc553DCDLossAlm": sc553DCDLossAlm,
       "sc553DSRLossAlm": sc553DSRLossAlm,
       "sc553DTRLossAlm": sc553DTRLossAlm,
       "sc553RXDNoTransitionsAlm": sc553RXDNoTransitionsAlm,
       "sc553TXDNoTransitionsAlm": sc553TXDNoTransitionsAlm,
       "sc553RedundancyOn": sc553RedundancyOn,
       "sc553RemoteNotResponding": sc553RemoteNotResponding,
       "sc553TopPowerSupplyFail": sc553TopPowerSupplyFail,
       "sc553BottomPowerSupplyFail": sc553BottomPowerSupplyFail,
       "sc553AlarmConfigTable": sc553AlarmConfigTable,
       "sc553AlarmConfigEntry": sc553AlarmConfigEntry,
       "sc553AlarmConfigIndex": sc553AlarmConfigIndex,
       "sc553AlarmConfigIdentifier": sc553AlarmConfigIdentifier,
       "sc553AlarmCountWindow": sc553AlarmCountWindow,
       "sc553AlarmCountThreshold": sc553AlarmCountThreshold,
       "sc553Performance": sc553Performance,
       "sc553CurrentUserTable": sc553CurrentUserTable,
       "sc553CurrentUserEntry": sc553CurrentUserEntry,
       "sc553CurrentUserIndex": sc553CurrentUserIndex,
       "sc553CurrentUserStat": sc553CurrentUserStat,
       "sc553CurrentNetworkTable": sc553CurrentNetworkTable,
       "sc553CurrentNetworkEntry": sc553CurrentNetworkEntry,
       "sc553CurrentNetworkIndex": sc553CurrentNetworkIndex,
       "sc553CurrentNetworkStat": sc553CurrentNetworkStat,
       "sc553CurrentFarEndTable": sc553CurrentFarEndTable,
       "sc553CurrentFarEndEntry": sc553CurrentFarEndEntry,
       "sc553CurrentFarEndIndex": sc553CurrentFarEndIndex,
       "sc553CurrentFarEndStat": sc553CurrentFarEndStat,
       "sc553TotalUserTable": sc553TotalUserTable,
       "sc553TotalUserEntry": sc553TotalUserEntry,
       "sc553TotalUserIndex": sc553TotalUserIndex,
       "sc553TotalUserStat": sc553TotalUserStat,
       "sc553TotalNetworkTable": sc553TotalNetworkTable,
       "sc553TotalNetworkEntry": sc553TotalNetworkEntry,
       "sc553TotalNetworkIndex": sc553TotalNetworkIndex,
       "sc553TotalNetworkStat": sc553TotalNetworkStat,
       "sc553TotalFarEndTable": sc553TotalFarEndTable,
       "sc553TotalFarEndEntry": sc553TotalFarEndEntry,
       "sc553TotalFarEndIndex": sc553TotalFarEndIndex,
       "sc553TotalFarEndStat": sc553TotalFarEndStat,
       "sc553UserIntervalTable": sc553UserIntervalTable,
       "sc553UserIntervalEntry": sc553UserIntervalEntry,
       "sc553UserIntervalIndex": sc553UserIntervalIndex,
       "sc553UserIntervalNumber": sc553UserIntervalNumber,
       "sc553UserIntervalStats": sc553UserIntervalStats,
       "sc553NetworkIntervalTable": sc553NetworkIntervalTable,
       "sc553NetworkIntervalEntry": sc553NetworkIntervalEntry,
       "sc553NetworkIntervalIndex": sc553NetworkIntervalIndex,
       "sc553NetworkIntervalNumber": sc553NetworkIntervalNumber,
       "sc553NetworkIntervalStats": sc553NetworkIntervalStats,
       "sc553FarEndIntervalTable": sc553FarEndIntervalTable,
       "sc553FarEndIntervalEntry": sc553FarEndIntervalEntry,
       "sc553FarEndIntervalIndex": sc553FarEndIntervalIndex,
       "sc553FarEndIntervalNumber": sc553FarEndIntervalNumber,
       "sc553FarEndIntervalStats": sc553FarEndIntervalStats,
       "sc553StoreUserTotals": sc553StoreUserTotals,
       "sc553StoreUserIntervals": sc553StoreUserIntervals,
       "sc553ShelfUserTotals": sc553ShelfUserTotals,
       "sc553ShelfUserIntvlsTable": sc553ShelfUserIntvlsTable,
       "sc553ShelfUserIntervalsEntry": sc553ShelfUserIntervalsEntry,
       "sc553ShelfUserIntvlsIndex": sc553ShelfUserIntvlsIndex,
       "sc553ShelfUserIntervals": sc553ShelfUserIntervals}
)
