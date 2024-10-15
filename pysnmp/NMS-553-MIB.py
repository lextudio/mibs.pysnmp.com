# SNMP MIB module (NMS-553-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-553-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:37 2024
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
_Nms553_ObjectIdentity = ObjectIdentity
nms553 = _Nms553_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 7)
)
_Nms553Version_ObjectIdentity = ObjectIdentity
nms553Version = _Nms553Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 1)
)


class _Nms553MIBversion_Type(DisplayString):
    """Custom type nms553MIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Nms553MIBversion_Type.__name__ = "DisplayString"
_Nms553MIBversion_Object = MibScalar
nms553MIBversion = _Nms553MIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 1, 1),
    _Nms553MIBversion_Type()
)
nms553MIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553MIBversion.setStatus("mandatory")
_Nms553VersionTable_Object = MibTable
nms553VersionTable = _Nms553VersionTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 1, 2)
)
if mibBuilder.loadTexts:
    nms553VersionTable.setStatus("mandatory")
_Nms553VersionEntry_Object = MibTableRow
nms553VersionEntry = _Nms553VersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 1, 2, 1)
)
nms553VersionEntry.setIndexNames(
    (0, "NMS-553-MIB", "nms553VersionIndex"),
)
if mibBuilder.loadTexts:
    nms553VersionEntry.setStatus("mandatory")
_Nms553VersionIndex_Type = SCinstance
_Nms553VersionIndex_Object = MibTableColumn
nms553VersionIndex = _Nms553VersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 1, 2, 1, 1),
    _Nms553VersionIndex_Type()
)
nms553VersionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553VersionIndex.setStatus("mandatory")


class _Nms553FirmwareRev_Type(DisplayString):
    """Custom type nms553FirmwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Nms553FirmwareRev_Type.__name__ = "DisplayString"
_Nms553FirmwareRev_Object = MibTableColumn
nms553FirmwareRev = _Nms553FirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 1, 2, 1, 2),
    _Nms553FirmwareRev_Type()
)
nms553FirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553FirmwareRev.setStatus("mandatory")
_Nms553DS0Allocation_ObjectIdentity = ObjectIdentity
nms553DS0Allocation = _Nms553DS0Allocation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 2)
)
_Nms553DS0AllocationSchemeTable_Object = MibTable
nms553DS0AllocationSchemeTable = _Nms553DS0AllocationSchemeTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 2, 1)
)
if mibBuilder.loadTexts:
    nms553DS0AllocationSchemeTable.setStatus("mandatory")
_Nms553DS0AllocationSchemeEntry_Object = MibTableRow
nms553DS0AllocationSchemeEntry = _Nms553DS0AllocationSchemeEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 2, 1, 1)
)
nms553DS0AllocationSchemeEntry.setIndexNames(
    (0, "NMS-553-MIB", "nms553DS0AllocationSchemeIndex"),
)
if mibBuilder.loadTexts:
    nms553DS0AllocationSchemeEntry.setStatus("mandatory")
_Nms553DS0AllocationSchemeIndex_Type = SCinstance
_Nms553DS0AllocationSchemeIndex_Object = MibTableColumn
nms553DS0AllocationSchemeIndex = _Nms553DS0AllocationSchemeIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 2, 1, 1, 1),
    _Nms553DS0AllocationSchemeIndex_Type()
)
nms553DS0AllocationSchemeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553DS0AllocationSchemeIndex.setStatus("mandatory")


class _Nms553DS0AllocationScheme_Type(Integer32):
    """Custom type nms553DS0AllocationScheme based on Integer32"""
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


_Nms553DS0AllocationScheme_Type.__name__ = "Integer32"
_Nms553DS0AllocationScheme_Object = MibTableColumn
nms553DS0AllocationScheme = _Nms553DS0AllocationScheme_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 2, 1, 1, 2),
    _Nms553DS0AllocationScheme_Type()
)
nms553DS0AllocationScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553DS0AllocationScheme.setStatus("mandatory")
_Nms553DS0AllocationConfigTable_Object = MibTable
nms553DS0AllocationConfigTable = _Nms553DS0AllocationConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 2, 2)
)
if mibBuilder.loadTexts:
    nms553DS0AllocationConfigTable.setStatus("mandatory")
_Nms553DS0AllocationConfigEntry_Object = MibTableRow
nms553DS0AllocationConfigEntry = _Nms553DS0AllocationConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 2, 2, 1)
)
nms553DS0AllocationConfigEntry.setIndexNames(
    (0, "NMS-553-MIB", "nms553DS0AllocationConfigIndex"),
)
if mibBuilder.loadTexts:
    nms553DS0AllocationConfigEntry.setStatus("mandatory")
_Nms553DS0AllocationConfigIndex_Type = SCinstance
_Nms553DS0AllocationConfigIndex_Object = MibTableColumn
nms553DS0AllocationConfigIndex = _Nms553DS0AllocationConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 2, 2, 1, 1),
    _Nms553DS0AllocationConfigIndex_Type()
)
nms553DS0AllocationConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553DS0AllocationConfigIndex.setStatus("mandatory")


class _Nms553DS0AllocationBaseRate_Type(Integer32):
    """Custom type nms553DS0AllocationBaseRate based on Integer32"""
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


_Nms553DS0AllocationBaseRate_Type.__name__ = "Integer32"
_Nms553DS0AllocationBaseRate_Object = MibTableColumn
nms553DS0AllocationBaseRate = _Nms553DS0AllocationBaseRate_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 2, 2, 1, 2),
    _Nms553DS0AllocationBaseRate_Type()
)
nms553DS0AllocationBaseRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553DS0AllocationBaseRate.setStatus("mandatory")


class _Nms553DS0AllocationStartingDS0_Type(Integer32):
    """Custom type nms553DS0AllocationStartingDS0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_Nms553DS0AllocationStartingDS0_Type.__name__ = "Integer32"
_Nms553DS0AllocationStartingDS0_Object = MibTableColumn
nms553DS0AllocationStartingDS0 = _Nms553DS0AllocationStartingDS0_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 2, 2, 1, 3),
    _Nms553DS0AllocationStartingDS0_Type()
)
nms553DS0AllocationStartingDS0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553DS0AllocationStartingDS0.setStatus("mandatory")


class _Nms553DS0AllocationNumberOfDS0s_Type(Integer32):
    """Custom type nms553DS0AllocationNumberOfDS0s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Nms553DS0AllocationNumberOfDS0s_Type.__name__ = "Integer32"
_Nms553DS0AllocationNumberOfDS0s_Object = MibTableColumn
nms553DS0AllocationNumberOfDS0s = _Nms553DS0AllocationNumberOfDS0s_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 2, 2, 1, 4),
    _Nms553DS0AllocationNumberOfDS0s_Type()
)
nms553DS0AllocationNumberOfDS0s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553DS0AllocationNumberOfDS0s.setStatus("mandatory")


class _Nms553DS0AllocationInbandDccMode_Type(Integer32):
    """Custom type nms553DS0AllocationInbandDccMode based on Integer32"""
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


_Nms553DS0AllocationInbandDccMode_Type.__name__ = "Integer32"
_Nms553DS0AllocationInbandDccMode_Object = MibTableColumn
nms553DS0AllocationInbandDccMode = _Nms553DS0AllocationInbandDccMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 2, 2, 1, 5),
    _Nms553DS0AllocationInbandDccMode_Type()
)
nms553DS0AllocationInbandDccMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553DS0AllocationInbandDccMode.setStatus("mandatory")
_Nms553Configuration_ObjectIdentity = ObjectIdentity
nms553Configuration = _Nms553Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3)
)
_Nms553ChannelConfigTable_Object = MibTable
nms553ChannelConfigTable = _Nms553ChannelConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 1)
)
if mibBuilder.loadTexts:
    nms553ChannelConfigTable.setStatus("mandatory")
_Nms553ChannelConfigEntry_Object = MibTableRow
nms553ChannelConfigEntry = _Nms553ChannelConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 1, 1)
)
nms553ChannelConfigEntry.setIndexNames(
    (0, "NMS-553-MIB", "nms553ChannelConfigIndex"),
)
if mibBuilder.loadTexts:
    nms553ChannelConfigEntry.setStatus("mandatory")
_Nms553ChannelConfigIndex_Type = SCinstance
_Nms553ChannelConfigIndex_Object = MibTableColumn
nms553ChannelConfigIndex = _Nms553ChannelConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 1, 1, 1),
    _Nms553ChannelConfigIndex_Type()
)
nms553ChannelConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553ChannelConfigIndex.setStatus("mandatory")


class _Nms553ChannelSplitTiming_Type(Integer32):
    """Custom type nms553ChannelSplitTiming based on Integer32"""
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


_Nms553ChannelSplitTiming_Type.__name__ = "Integer32"
_Nms553ChannelSplitTiming_Object = MibTableColumn
nms553ChannelSplitTiming = _Nms553ChannelSplitTiming_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 1, 1, 2),
    _Nms553ChannelSplitTiming_Type()
)
nms553ChannelSplitTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553ChannelSplitTiming.setStatus("mandatory")


class _Nms553ChannelChannelType_Type(Integer32):
    """Custom type nms553ChannelChannelType based on Integer32"""
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


_Nms553ChannelChannelType_Type.__name__ = "Integer32"
_Nms553ChannelChannelType_Object = MibTableColumn
nms553ChannelChannelType = _Nms553ChannelChannelType_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 1, 1, 3),
    _Nms553ChannelChannelType_Type()
)
nms553ChannelChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553ChannelChannelType.setStatus("mandatory")


class _Nms553ChannelClockInvert_Type(Integer32):
    """Custom type nms553ChannelClockInvert based on Integer32"""
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


_Nms553ChannelClockInvert_Type.__name__ = "Integer32"
_Nms553ChannelClockInvert_Object = MibTableColumn
nms553ChannelClockInvert = _Nms553ChannelClockInvert_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 1, 1, 4),
    _Nms553ChannelClockInvert_Type()
)
nms553ChannelClockInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553ChannelClockInvert.setStatus("mandatory")


class _Nms553ChannelDataInvert_Type(Integer32):
    """Custom type nms553ChannelDataInvert based on Integer32"""
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


_Nms553ChannelDataInvert_Type.__name__ = "Integer32"
_Nms553ChannelDataInvert_Object = MibTableColumn
nms553ChannelDataInvert = _Nms553ChannelDataInvert_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 1, 1, 5),
    _Nms553ChannelDataInvert_Type()
)
nms553ChannelDataInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553ChannelDataInvert.setStatus("mandatory")


class _Nms553ChannelLocalDCD_Type(Integer32):
    """Custom type nms553ChannelLocalDCD based on Integer32"""
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


_Nms553ChannelLocalDCD_Type.__name__ = "Integer32"
_Nms553ChannelLocalDCD_Object = MibTableColumn
nms553ChannelLocalDCD = _Nms553ChannelLocalDCD_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 1, 1, 6),
    _Nms553ChannelLocalDCD_Type()
)
nms553ChannelLocalDCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553ChannelLocalDCD.setStatus("mandatory")


class _Nms553ChannelLocalDSR_Type(Integer32):
    """Custom type nms553ChannelLocalDSR based on Integer32"""
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


_Nms553ChannelLocalDSR_Type.__name__ = "Integer32"
_Nms553ChannelLocalDSR_Object = MibTableColumn
nms553ChannelLocalDSR = _Nms553ChannelLocalDSR_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 1, 1, 7),
    _Nms553ChannelLocalDSR_Type()
)
nms553ChannelLocalDSR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553ChannelLocalDSR.setStatus("mandatory")


class _Nms553ChannelFlowControl_Type(Integer32):
    """Custom type nms553ChannelFlowControl based on Integer32"""
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
        *(("txDtrRxDcd", 3),
          ("txDtrRxDsr", 4),
          ("txRtsRxDcd", 1),
          ("txRtsRxDsr", 2))
    )


_Nms553ChannelFlowControl_Type.__name__ = "Integer32"
_Nms553ChannelFlowControl_Object = MibTableColumn
nms553ChannelFlowControl = _Nms553ChannelFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 1, 1, 8),
    _Nms553ChannelFlowControl_Type()
)
nms553ChannelFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553ChannelFlowControl.setStatus("mandatory")


class _Nms553ChannelRTSCTSControl_Type(Integer32):
    """Custom type nms553ChannelRTSCTSControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ctsDelay10ms", 1),
          ("ctsDelayStandard", 3),
          ("ctsOn", 2))
    )


_Nms553ChannelRTSCTSControl_Type.__name__ = "Integer32"
_Nms553ChannelRTSCTSControl_Object = MibTableColumn
nms553ChannelRTSCTSControl = _Nms553ChannelRTSCTSControl_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 1, 1, 9),
    _Nms553ChannelRTSCTSControl_Type()
)
nms553ChannelRTSCTSControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553ChannelRTSCTSControl.setStatus("mandatory")


class _Nms553ChannelEIAtestLeads_Type(Integer32):
    """Custom type nms553ChannelEIAtestLeads based on Integer32"""
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


_Nms553ChannelEIAtestLeads_Type.__name__ = "Integer32"
_Nms553ChannelEIAtestLeads_Object = MibTableColumn
nms553ChannelEIAtestLeads = _Nms553ChannelEIAtestLeads_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 1, 1, 10),
    _Nms553ChannelEIAtestLeads_Type()
)
nms553ChannelEIAtestLeads.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553ChannelEIAtestLeads.setStatus("mandatory")


class _Nms553ChannelInbandLoop_Type(Integer32):
    """Custom type nms553ChannelInbandLoop based on Integer32"""
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


_Nms553ChannelInbandLoop_Type.__name__ = "Integer32"
_Nms553ChannelInbandLoop_Object = MibTableColumn
nms553ChannelInbandLoop = _Nms553ChannelInbandLoop_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 1, 1, 11),
    _Nms553ChannelInbandLoop_Type()
)
nms553ChannelInbandLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553ChannelInbandLoop.setStatus("mandatory")


class _Nms553ChannelInbandLoopCode_Type(Integer32):
    """Custom type nms553ChannelInbandLoopCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("pn127", 1)
    )


_Nms553ChannelInbandLoopCode_Type.__name__ = "Integer32"
_Nms553ChannelInbandLoopCode_Object = MibTableColumn
nms553ChannelInbandLoopCode = _Nms553ChannelInbandLoopCode_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 1, 1, 12),
    _Nms553ChannelInbandLoopCode_Type()
)
nms553ChannelInbandLoopCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553ChannelInbandLoopCode.setStatus("mandatory")


class _Nms553ChannelInbandLoopdown_Type(Integer32):
    """Custom type nms553ChannelInbandLoopdown based on Integer32"""
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


_Nms553ChannelInbandLoopdown_Type.__name__ = "Integer32"
_Nms553ChannelInbandLoopdown_Object = MibTableColumn
nms553ChannelInbandLoopdown = _Nms553ChannelInbandLoopdown_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 1, 1, 13),
    _Nms553ChannelInbandLoopdown_Type()
)
nms553ChannelInbandLoopdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553ChannelInbandLoopdown.setStatus("mandatory")


class _Nms553ChannelControlModeIdle_Type(Integer32):
    """Custom type nms553ChannelControlModeIdle based on Integer32"""
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


_Nms553ChannelControlModeIdle_Type.__name__ = "Integer32"
_Nms553ChannelControlModeIdle_Object = MibTableColumn
nms553ChannelControlModeIdle = _Nms553ChannelControlModeIdle_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 1, 1, 14),
    _Nms553ChannelControlModeIdle_Type()
)
nms553ChannelControlModeIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553ChannelControlModeIdle.setStatus("mandatory")
_Nms553NetworkConfigTable_Object = MibTable
nms553NetworkConfigTable = _Nms553NetworkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 2)
)
if mibBuilder.loadTexts:
    nms553NetworkConfigTable.setStatus("mandatory")
_Nms553NetworkConfigEntry_Object = MibTableRow
nms553NetworkConfigEntry = _Nms553NetworkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 2, 1)
)
nms553NetworkConfigEntry.setIndexNames(
    (0, "NMS-553-MIB", "nms553NetworkConfigIndex"),
)
if mibBuilder.loadTexts:
    nms553NetworkConfigEntry.setStatus("mandatory")
_Nms553NetworkConfigIndex_Type = SCinstance
_Nms553NetworkConfigIndex_Object = MibTableColumn
nms553NetworkConfigIndex = _Nms553NetworkConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 2, 1, 1),
    _Nms553NetworkConfigIndex_Type()
)
nms553NetworkConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553NetworkConfigIndex.setStatus("mandatory")


class _Nms553NetworkAdminLineType_Type(Integer32):
    """Custom type nms553NetworkAdminLineType based on Integer32"""
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
        *(("auto", 1),
          ("manD4", 3),
          ("manEsf", 2),
          ("unframed", 4))
    )


_Nms553NetworkAdminLineType_Type.__name__ = "Integer32"
_Nms553NetworkAdminLineType_Object = MibTableColumn
nms553NetworkAdminLineType = _Nms553NetworkAdminLineType_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 2, 1, 2),
    _Nms553NetworkAdminLineType_Type()
)
nms553NetworkAdminLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553NetworkAdminLineType.setStatus("mandatory")


class _Nms553NetworkOperLineType_Type(Integer32):
    """Custom type nms553NetworkOperLineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manD4", 2),
          ("manEsf", 1),
          ("unframed", 3))
    )


_Nms553NetworkOperLineType_Type.__name__ = "Integer32"
_Nms553NetworkOperLineType_Object = MibTableColumn
nms553NetworkOperLineType = _Nms553NetworkOperLineType_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 2, 1, 3),
    _Nms553NetworkOperLineType_Type()
)
nms553NetworkOperLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553NetworkOperLineType.setStatus("mandatory")


class _Nms553NetworkInterfaceType_Type(Integer32):
    """Custom type nms553NetworkInterfaceType based on Integer32"""
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


_Nms553NetworkInterfaceType_Type.__name__ = "Integer32"
_Nms553NetworkInterfaceType_Object = MibTableColumn
nms553NetworkInterfaceType = _Nms553NetworkInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 2, 1, 4),
    _Nms553NetworkInterfaceType_Type()
)
nms553NetworkInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553NetworkInterfaceType.setStatus("mandatory")


class _Nms553NetworkPreequalization_Type(Integer32):
    """Custom type nms553NetworkPreequalization based on Integer32"""
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
        *(("none", 1),
          ("preeq130", 2),
          ("preeq260", 3),
          ("preeq390", 4),
          ("preeq530", 5),
          ("preeq655", 6))
    )


_Nms553NetworkPreequalization_Type.__name__ = "Integer32"
_Nms553NetworkPreequalization_Object = MibTableColumn
nms553NetworkPreequalization = _Nms553NetworkPreequalization_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 2, 1, 5),
    _Nms553NetworkPreequalization_Type()
)
nms553NetworkPreequalization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553NetworkPreequalization.setStatus("mandatory")


class _Nms553NetworkAdminLineBuildout_Type(Integer32):
    """Custom type nms553NetworkAdminLineBuildout based on Integer32"""
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
        *(("auto", 1),
          ("man00dB", 2),
          ("man150dB", 4),
          ("man75dB", 3))
    )


_Nms553NetworkAdminLineBuildout_Type.__name__ = "Integer32"
_Nms553NetworkAdminLineBuildout_Object = MibTableColumn
nms553NetworkAdminLineBuildout = _Nms553NetworkAdminLineBuildout_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 2, 1, 6),
    _Nms553NetworkAdminLineBuildout_Type()
)
nms553NetworkAdminLineBuildout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553NetworkAdminLineBuildout.setStatus("mandatory")


class _Nms553NetworkOperLineBuildout_Type(Integer32):
    """Custom type nms553NetworkOperLineBuildout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tx00dB", 1),
          ("tx150dB", 3),
          ("tx75dB", 2))
    )


_Nms553NetworkOperLineBuildout_Type.__name__ = "Integer32"
_Nms553NetworkOperLineBuildout_Object = MibTableColumn
nms553NetworkOperLineBuildout = _Nms553NetworkOperLineBuildout_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 2, 1, 7),
    _Nms553NetworkOperLineBuildout_Type()
)
nms553NetworkOperLineBuildout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553NetworkOperLineBuildout.setStatus("mandatory")


class _Nms553NetworkOnesDensity_Type(Integer32):
    """Custom type nms553NetworkOnesDensity based on Integer32"""
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
        *(("inhibit", 1),
          ("max15zeros", 2),
          ("max39zeros", 3),
          ("min1in8", 5),
          ("restrict8XNplus1", 4))
    )


_Nms553NetworkOnesDensity_Type.__name__ = "Integer32"
_Nms553NetworkOnesDensity_Object = MibTableColumn
nms553NetworkOnesDensity = _Nms553NetworkOnesDensity_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 2, 1, 8),
    _Nms553NetworkOnesDensity_Type()
)
nms553NetworkOnesDensity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553NetworkOnesDensity.setStatus("mandatory")


class _Nms553NetworkTransmitClockSource_Type(Integer32):
    """Custom type nms553NetworkTransmitClockSource based on Integer32"""
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
        *(("cascade", 2),
          ("composite", 8),
          ("extChannelClkA", 5),
          ("extChannelClkB", 6),
          ("extChannelClkC", 7),
          ("internal", 3),
          ("receive", 1),
          ("station", 4))
    )


_Nms553NetworkTransmitClockSource_Type.__name__ = "Integer32"
_Nms553NetworkTransmitClockSource_Object = MibTableColumn
nms553NetworkTransmitClockSource = _Nms553NetworkTransmitClockSource_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 2, 1, 9),
    _Nms553NetworkTransmitClockSource_Type()
)
nms553NetworkTransmitClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553NetworkTransmitClockSource.setStatus("mandatory")


class _Nms553NetworkFallbackClockSource_Type(Integer32):
    """Custom type nms553NetworkFallbackClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 2),
          ("receive", 1))
    )


_Nms553NetworkFallbackClockSource_Type.__name__ = "Integer32"
_Nms553NetworkFallbackClockSource_Object = MibTableColumn
nms553NetworkFallbackClockSource = _Nms553NetworkFallbackClockSource_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 2, 1, 10),
    _Nms553NetworkFallbackClockSource_Type()
)
nms553NetworkFallbackClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553NetworkFallbackClockSource.setStatus("mandatory")


class _Nms553NetworkFDLdcc_Type(Integer32):
    """Custom type nms553NetworkFDLdcc based on Integer32"""
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


_Nms553NetworkFDLdcc_Type.__name__ = "Integer32"
_Nms553NetworkFDLdcc_Object = MibTableColumn
nms553NetworkFDLdcc = _Nms553NetworkFDLdcc_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 2, 1, 11),
    _Nms553NetworkFDLdcc_Type()
)
nms553NetworkFDLdcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553NetworkFDLdcc.setStatus("mandatory")


class _Nms553NetworkAISLoopdown_Type(Integer32):
    """Custom type nms553NetworkAISLoopdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 60),
    )


_Nms553NetworkAISLoopdown_Type.__name__ = "Integer32"
_Nms553NetworkAISLoopdown_Object = MibTableColumn
nms553NetworkAISLoopdown = _Nms553NetworkAISLoopdown_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 2, 1, 12),
    _Nms553NetworkAISLoopdown_Type()
)
nms553NetworkAISLoopdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553NetworkAISLoopdown.setStatus("mandatory")


class _Nms553NetworkInbandFrame_Type(Integer32):
    """Custom type nms553NetworkInbandFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("framed", 1),
          ("unframed", 2))
    )


_Nms553NetworkInbandFrame_Type.__name__ = "Integer32"
_Nms553NetworkInbandFrame_Object = MibTableColumn
nms553NetworkInbandFrame = _Nms553NetworkInbandFrame_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 2, 1, 13),
    _Nms553NetworkInbandFrame_Type()
)
nms553NetworkInbandFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553NetworkInbandFrame.setStatus("mandatory")


class _Nms553NetworkLoopbackConfig_Type(Integer32):
    """Custom type nms553NetworkLoopbackConfig based on Integer32"""
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


_Nms553NetworkLoopbackConfig_Type.__name__ = "Integer32"
_Nms553NetworkLoopbackConfig_Object = MibTableColumn
nms553NetworkLoopbackConfig = _Nms553NetworkLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 2, 1, 14),
    _Nms553NetworkLoopbackConfig_Type()
)
nms553NetworkLoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553NetworkLoopbackConfig.setStatus("mandatory")


class _Nms553NetworkLineCoding_Type(Integer32):
    """Custom type nms553NetworkLineCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nms553AMI", 2),
          ("nms553B8ZS", 1))
    )


_Nms553NetworkLineCoding_Type.__name__ = "Integer32"
_Nms553NetworkLineCoding_Object = MibTableColumn
nms553NetworkLineCoding = _Nms553NetworkLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 2, 1, 15),
    _Nms553NetworkLineCoding_Type()
)
nms553NetworkLineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553NetworkLineCoding.setStatus("mandatory")


class _Nms553NetworkFdl_Type(Integer32):
    """Custom type nms553NetworkFdl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nms553Ansi-T1-403", 2),
          ("nms553Att-54016", 3),
          ("nms553Fdl-none", 1))
    )


_Nms553NetworkFdl_Type.__name__ = "Integer32"
_Nms553NetworkFdl_Object = MibTableColumn
nms553NetworkFdl = _Nms553NetworkFdl_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 2, 1, 16),
    _Nms553NetworkFdl_Type()
)
nms553NetworkFdl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553NetworkFdl.setStatus("mandatory")


class _Nms553ConfigurationSave_Type(Integer32):
    """Custom type nms553ConfigurationSave based on Integer32"""
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
        *(("both", 3),
          ("channel", 2),
          ("network", 1),
          ("norm", 4))
    )


_Nms553ConfigurationSave_Type.__name__ = "Integer32"
_Nms553ConfigurationSave_Object = MibScalar
nms553ConfigurationSave = _Nms553ConfigurationSave_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 3, 3),
    _Nms553ConfigurationSave_Type()
)
nms553ConfigurationSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553ConfigurationSave.setStatus("mandatory")
_Nms553DteStatus_ObjectIdentity = ObjectIdentity
nms553DteStatus = _Nms553DteStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 4)
)
_Nms553DteStatusTable_Object = MibTable
nms553DteStatusTable = _Nms553DteStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 4, 1)
)
if mibBuilder.loadTexts:
    nms553DteStatusTable.setStatus("mandatory")
_Nms553DteStatusEntry_Object = MibTableRow
nms553DteStatusEntry = _Nms553DteStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 4, 1, 1)
)
nms553DteStatusEntry.setIndexNames(
    (0, "NMS-553-MIB", "nms553DteStatusIndex"),
)
if mibBuilder.loadTexts:
    nms553DteStatusEntry.setStatus("mandatory")
_Nms553DteStatusIndex_Type = SCinstance
_Nms553DteStatusIndex_Object = MibTableColumn
nms553DteStatusIndex = _Nms553DteStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 4, 1, 1, 1),
    _Nms553DteStatusIndex_Type()
)
nms553DteStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553DteStatusIndex.setStatus("mandatory")


class _Nms553DteStat_Type(OctetString):
    """Custom type nms553DteStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Nms553DteStat_Type.__name__ = "OctetString"
_Nms553DteStat_Object = MibTableColumn
nms553DteStat = _Nms553DteStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 4, 1, 1, 2),
    _Nms553DteStat_Type()
)
nms553DteStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553DteStat.setStatus("mandatory")
_Nms553Diagnostics_ObjectIdentity = ObjectIdentity
nms553Diagnostics = _Nms553Diagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 5)
)
_Nms553DiagTable_Object = MibTable
nms553DiagTable = _Nms553DiagTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 5, 1)
)
if mibBuilder.loadTexts:
    nms553DiagTable.setStatus("mandatory")
_Nms553DiagEntry_Object = MibTableRow
nms553DiagEntry = _Nms553DiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 5, 1, 1)
)
nms553DiagEntry.setIndexNames(
    (0, "NMS-553-MIB", "nms553DiagIndex"),
)
if mibBuilder.loadTexts:
    nms553DiagEntry.setStatus("mandatory")
_Nms553DiagIndex_Type = SCinstance
_Nms553DiagIndex_Object = MibTableColumn
nms553DiagIndex = _Nms553DiagIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 5, 1, 1, 1),
    _Nms553DiagIndex_Type()
)
nms553DiagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553DiagIndex.setStatus("mandatory")


class _Nms553DiagTestDuration_Type(Integer32):
    """Custom type nms553DiagTestDuration based on Integer32"""
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
        *(("noLimit", 16),
          ("testTime10Mins", 11),
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
          ("testTime9Mins", 10))
    )


_Nms553DiagTestDuration_Type.__name__ = "Integer32"
_Nms553DiagTestDuration_Object = MibTableColumn
nms553DiagTestDuration = _Nms553DiagTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 5, 1, 1, 2),
    _Nms553DiagTestDuration_Type()
)
nms553DiagTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553DiagTestDuration.setStatus("mandatory")


class _Nms553DiagProgPattern_Type(Integer32):
    """Custom type nms553DiagProgPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Nms553DiagProgPattern_Type.__name__ = "Integer32"
_Nms553DiagProgPattern_Object = MibTableColumn
nms553DiagProgPattern = _Nms553DiagProgPattern_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 5, 1, 1, 3),
    _Nms553DiagProgPattern_Type()
)
nms553DiagProgPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553DiagProgPattern.setStatus("mandatory")


class _Nms553DiagBeginSelfTest_Type(Integer32):
    """Custom type nms553DiagBeginSelfTest based on Integer32"""
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
        *(("dsu2047Pattern", 6),
          ("dsu511Pattern", 5),
          ("dsuProgPattern", 8),
          ("dsuQRSPattern", 7),
          ("noselftestrunning", 9),
          ("unit2047Pattern", 2),
          ("unit511Pattern", 1),
          ("unitProgPattern", 4),
          ("unitQRSPattern", 3))
    )


_Nms553DiagBeginSelfTest_Type.__name__ = "Integer32"
_Nms553DiagBeginSelfTest_Object = MibTableColumn
nms553DiagBeginSelfTest = _Nms553DiagBeginSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 5, 1, 1, 4),
    _Nms553DiagBeginSelfTest_Type()
)
nms553DiagBeginSelfTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553DiagBeginSelfTest.setStatus("mandatory")


class _Nms553DiagBeginLoopTest_Type(Integer32):
    """Custom type nms553DiagBeginLoopTest based on Integer32"""
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
        *(("digitalLoopback", 2),
          ("localLoopback", 1),
          ("nolooptestrunning", 4),
          ("remoteDigitalLoopback", 3))
    )


_Nms553DiagBeginLoopTest_Type.__name__ = "Integer32"
_Nms553DiagBeginLoopTest_Object = MibTableColumn
nms553DiagBeginLoopTest = _Nms553DiagBeginLoopTest_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 5, 1, 1, 5),
    _Nms553DiagBeginLoopTest_Type()
)
nms553DiagBeginLoopTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553DiagBeginLoopTest.setStatus("mandatory")
_Nms553DiagTestResults_Type = Integer32
_Nms553DiagTestResults_Object = MibTableColumn
nms553DiagTestResults = _Nms553DiagTestResults_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 5, 1, 1, 6),
    _Nms553DiagTestResults_Type()
)
nms553DiagTestResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553DiagTestResults.setStatus("mandatory")


class _Nms553DiagResetTestToNormal_Type(Integer32):
    """Custom type nms553DiagResetTestToNormal based on Integer32"""
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


_Nms553DiagResetTestToNormal_Type.__name__ = "Integer32"
_Nms553DiagResetTestToNormal_Object = MibTableColumn
nms553DiagResetTestToNormal = _Nms553DiagResetTestToNormal_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 5, 1, 1, 7),
    _Nms553DiagResetTestToNormal_Type()
)
nms553DiagResetTestToNormal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553DiagResetTestToNormal.setStatus("mandatory")


class _Nms553DiagTestStatus_Type(Integer32):
    """Custom type nms553DiagTestStatus based on Integer32"""
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
        *(("digitalLoopback", 5),
          ("dsuSelfTest", 3),
          ("localLoopback", 4),
          ("noTestinProgress", 1),
          ("unitSelfTest", 2))
    )


_Nms553DiagTestStatus_Type.__name__ = "Integer32"
_Nms553DiagTestStatus_Object = MibTableColumn
nms553DiagTestStatus = _Nms553DiagTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 5, 1, 1, 8),
    _Nms553DiagTestStatus_Type()
)
nms553DiagTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553DiagTestStatus.setStatus("mandatory")
_Nms553Maintenance_ObjectIdentity = ObjectIdentity
nms553Maintenance = _Nms553Maintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 6)
)
_Nms553MaintenanceTable_Object = MibTable
nms553MaintenanceTable = _Nms553MaintenanceTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 6, 1)
)
if mibBuilder.loadTexts:
    nms553MaintenanceTable.setStatus("mandatory")
_Nms553MaintenanceEntry_Object = MibTableRow
nms553MaintenanceEntry = _Nms553MaintenanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 6, 1, 1)
)
nms553MaintenanceEntry.setIndexNames(
    (0, "NMS-553-MIB", "nms553MaintenanceIndex"),
)
if mibBuilder.loadTexts:
    nms553MaintenanceEntry.setStatus("mandatory")
_Nms553MaintenanceIndex_Type = SCinstance
_Nms553MaintenanceIndex_Object = MibTableColumn
nms553MaintenanceIndex = _Nms553MaintenanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 6, 1, 1, 1),
    _Nms553MaintenanceIndex_Type()
)
nms553MaintenanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553MaintenanceIndex.setStatus("mandatory")


class _Nms553LedStatus_Type(OctetString):
    """Custom type nms553LedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_Nms553LedStatus_Type.__name__ = "OctetString"
_Nms553LedStatus_Object = MibTableColumn
nms553LedStatus = _Nms553LedStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 6, 1, 1, 2),
    _Nms553LedStatus_Type()
)
nms553LedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553LedStatus.setStatus("mandatory")


class _Nms553SoftReset_Type(Integer32):
    """Custom type nms553SoftReset based on Integer32"""
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


_Nms553SoftReset_Type.__name__ = "Integer32"
_Nms553SoftReset_Object = MibTableColumn
nms553SoftReset = _Nms553SoftReset_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 6, 1, 1, 3),
    _Nms553SoftReset_Type()
)
nms553SoftReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553SoftReset.setStatus("mandatory")


class _Nms553DefaultInit_Type(Integer32):
    """Custom type nms553DefaultInit based on Integer32"""
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


_Nms553DefaultInit_Type.__name__ = "Integer32"
_Nms553DefaultInit_Object = MibTableColumn
nms553DefaultInit = _Nms553DefaultInit_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 6, 1, 1, 4),
    _Nms553DefaultInit_Type()
)
nms553DefaultInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553DefaultInit.setStatus("mandatory")


class _Nms553FrontPanel_Type(Integer32):
    """Custom type nms553FrontPanel based on Integer32"""
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


_Nms553FrontPanel_Type.__name__ = "Integer32"
_Nms553FrontPanel_Object = MibTableColumn
nms553FrontPanel = _Nms553FrontPanel_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 6, 1, 1, 5),
    _Nms553FrontPanel_Type()
)
nms553FrontPanel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553FrontPanel.setStatus("mandatory")


class _Nms553ProductType_Type(Integer32):
    """Custom type nms553ProductType based on Integer32"""
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
        *(("nms553c", 4),
          ("nms553cifp", 5),
          ("nms553d1", 1),
          ("nms553d1ifp", 2),
          ("nms553d3ifp", 3))
    )


_Nms553ProductType_Type.__name__ = "Integer32"
_Nms553ProductType_Object = MibTableColumn
nms553ProductType = _Nms553ProductType_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 6, 1, 1, 6),
    _Nms553ProductType_Type()
)
nms553ProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553ProductType.setStatus("mandatory")


class _Nms553ResetStatistics_Type(Integer32):
    """Custom type nms553ResetStatistics based on Integer32"""
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


_Nms553ResetStatistics_Type.__name__ = "Integer32"
_Nms553ResetStatistics_Object = MibTableColumn
nms553ResetStatistics = _Nms553ResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 6, 1, 1, 7),
    _Nms553ResetStatistics_Type()
)
nms553ResetStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553ResetStatistics.setStatus("mandatory")


class _Nms553ValidIntervals_Type(Integer32):
    """Custom type nms553ValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Nms553ValidIntervals_Type.__name__ = "Integer32"
_Nms553ValidIntervals_Object = MibTableColumn
nms553ValidIntervals = _Nms553ValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 6, 1, 1, 8),
    _Nms553ValidIntervals_Type()
)
nms553ValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553ValidIntervals.setStatus("mandatory")


class _Nms553CascadePresent_Type(Integer32):
    """Custom type nms553CascadePresent based on Integer32"""
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


_Nms553CascadePresent_Type.__name__ = "Integer32"
_Nms553CascadePresent_Object = MibTableColumn
nms553CascadePresent = _Nms553CascadePresent_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 6, 1, 1, 9),
    _Nms553CascadePresent_Type()
)
nms553CascadePresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553CascadePresent.setStatus("mandatory")


class _Nms553ReceiveLevel_Type(Integer32):
    """Custom type nms553ReceiveLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 43),
    )


_Nms553ReceiveLevel_Type.__name__ = "Integer32"
_Nms553ReceiveLevel_Object = MibTableColumn
nms553ReceiveLevel = _Nms553ReceiveLevel_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 6, 1, 1, 10),
    _Nms553ReceiveLevel_Type()
)
nms553ReceiveLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553ReceiveLevel.setStatus("mandatory")
_Nms553Alarms_ObjectIdentity = ObjectIdentity
nms553Alarms = _Nms553Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 7)
)
_Nms553AlarmData_ObjectIdentity = ObjectIdentity
nms553AlarmData = _Nms553AlarmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 7, 1)
)
_Nms553NoResponseAlm_ObjectIdentity = ObjectIdentity
nms553NoResponseAlm = _Nms553NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 7, 1, 1)
)
_Nms553DiagRxErrAlm_ObjectIdentity = ObjectIdentity
nms553DiagRxErrAlm = _Nms553DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 7, 1, 2)
)
_Nms553PowerUpAlm_ObjectIdentity = ObjectIdentity
nms553PowerUpAlm = _Nms553PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 7, 1, 3)
)
_Nms553NvRamCorrupt_ObjectIdentity = ObjectIdentity
nms553NvRamCorrupt = _Nms553NvRamCorrupt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 7, 1, 4)
)
_Nms553UnitFailure_ObjectIdentity = ObjectIdentity
nms553UnitFailure = _Nms553UnitFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 7, 1, 5)
)
_Nms553TimingLoss_ObjectIdentity = ObjectIdentity
nms553TimingLoss = _Nms553TimingLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 7, 1, 6)
)
_Nms553StatusChange_ObjectIdentity = ObjectIdentity
nms553StatusChange = _Nms553StatusChange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 7, 1, 7)
)
_Nms553UnsolicitedTest_ObjectIdentity = ObjectIdentity
nms553UnsolicitedTest = _Nms553UnsolicitedTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 7, 1, 8)
)
_Nms553LossOfSignal_ObjectIdentity = ObjectIdentity
nms553LossOfSignal = _Nms553LossOfSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 7, 1, 9)
)
_Nms553LossOfFrame_ObjectIdentity = ObjectIdentity
nms553LossOfFrame = _Nms553LossOfFrame_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 7, 1, 10)
)
_Nms553AlarmIndicationSignal_ObjectIdentity = ObjectIdentity
nms553AlarmIndicationSignal = _Nms553AlarmIndicationSignal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 7, 1, 11)
)
_Nms553ReceivedYellow_ObjectIdentity = ObjectIdentity
nms553ReceivedYellow = _Nms553ReceivedYellow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 7, 1, 12)
)
_Nms553UnavailableSignalState_ObjectIdentity = ObjectIdentity
nms553UnavailableSignalState = _Nms553UnavailableSignalState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 7, 1, 13)
)
_Nms553ExcessiveZeros_ObjectIdentity = ObjectIdentity
nms553ExcessiveZeros = _Nms553ExcessiveZeros_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 7, 1, 14)
)
_Nms553LowAverageDensity_ObjectIdentity = ObjectIdentity
nms553LowAverageDensity = _Nms553LowAverageDensity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 7, 1, 15)
)
_Nms553ControlledSlips_ObjectIdentity = ObjectIdentity
nms553ControlledSlips = _Nms553ControlledSlips_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 7, 1, 16)
)
_Nms553BipolarViolations_ObjectIdentity = ObjectIdentity
nms553BipolarViolations = _Nms553BipolarViolations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 7, 1, 17)
)
_Nms553CrcErrors_ObjectIdentity = ObjectIdentity
nms553CrcErrors = _Nms553CrcErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 7, 1, 18)
)
_Nms553AlarmConfigTable_Object = MibTable
nms553AlarmConfigTable = _Nms553AlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 7, 2)
)
if mibBuilder.loadTexts:
    nms553AlarmConfigTable.setStatus("mandatory")
_Nms553AlarmConfigEntry_Object = MibTableRow
nms553AlarmConfigEntry = _Nms553AlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 7, 2, 1)
)
nms553AlarmConfigEntry.setIndexNames(
    (0, "NMS-553-MIB", "nms553AlarmConfigIndex"),
    (0, "NMS-553-MIB", "nms553AlarmConfigIdentifier"),
)
if mibBuilder.loadTexts:
    nms553AlarmConfigEntry.setStatus("mandatory")
_Nms553AlarmConfigIndex_Type = SCinstance
_Nms553AlarmConfigIndex_Object = MibTableColumn
nms553AlarmConfigIndex = _Nms553AlarmConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 7, 2, 1, 1),
    _Nms553AlarmConfigIndex_Type()
)
nms553AlarmConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553AlarmConfigIndex.setStatus("mandatory")
_Nms553AlarmConfigIdentifier_Type = ObjectIdentifier
_Nms553AlarmConfigIdentifier_Object = MibTableColumn
nms553AlarmConfigIdentifier = _Nms553AlarmConfigIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 7, 2, 1, 2),
    _Nms553AlarmConfigIdentifier_Type()
)
nms553AlarmConfigIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553AlarmConfigIdentifier.setStatus("mandatory")


class _Nms553AlarmCountWindow_Type(Integer32):
    """Custom type nms553AlarmCountWindow based on Integer32"""
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
        *(("disabled", 1),
          ("infinite", 5),
          ("last1hr", 4),
          ("last1min", 3),
          ("last1sec", 2))
    )


_Nms553AlarmCountWindow_Type.__name__ = "Integer32"
_Nms553AlarmCountWindow_Object = MibTableColumn
nms553AlarmCountWindow = _Nms553AlarmCountWindow_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 7, 2, 1, 3),
    _Nms553AlarmCountWindow_Type()
)
nms553AlarmCountWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553AlarmCountWindow.setStatus("mandatory")


class _Nms553AlarmCountThreshold_Type(Integer32):
    """Custom type nms553AlarmCountThreshold based on Integer32"""
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


_Nms553AlarmCountThreshold_Type.__name__ = "Integer32"
_Nms553AlarmCountThreshold_Object = MibTableColumn
nms553AlarmCountThreshold = _Nms553AlarmCountThreshold_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 7, 2, 1, 4),
    _Nms553AlarmCountThreshold_Type()
)
nms553AlarmCountThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553AlarmCountThreshold.setStatus("mandatory")
_Nms553AlarmHistory_ObjectIdentity = ObjectIdentity
nms553AlarmHistory = _Nms553AlarmHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 8)
)
_Nms553AlarmHistoryTable_Object = MibTable
nms553AlarmHistoryTable = _Nms553AlarmHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 8, 1)
)
if mibBuilder.loadTexts:
    nms553AlarmHistoryTable.setStatus("mandatory")
_Nms553AlarmHistoryEntry_Object = MibTableRow
nms553AlarmHistoryEntry = _Nms553AlarmHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 8, 1, 1)
)
nms553AlarmHistoryEntry.setIndexNames(
    (0, "NMS-553-MIB", "nms553AlarmHistoryIndex"),
    (0, "NMS-553-MIB", "nms553AlarmHistoryIdentifier"),
)
if mibBuilder.loadTexts:
    nms553AlarmHistoryEntry.setStatus("mandatory")
_Nms553AlarmHistoryIndex_Type = SCinstance
_Nms553AlarmHistoryIndex_Object = MibTableColumn
nms553AlarmHistoryIndex = _Nms553AlarmHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 8, 1, 1, 1),
    _Nms553AlarmHistoryIndex_Type()
)
nms553AlarmHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553AlarmHistoryIndex.setStatus("mandatory")
_Nms553AlarmHistoryIdentifier_Type = ObjectIdentifier
_Nms553AlarmHistoryIdentifier_Object = MibTableColumn
nms553AlarmHistoryIdentifier = _Nms553AlarmHistoryIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 8, 1, 1, 2),
    _Nms553AlarmHistoryIdentifier_Type()
)
nms553AlarmHistoryIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553AlarmHistoryIdentifier.setStatus("mandatory")
_Nms553AlarmCount_Type = Gauge32
_Nms553AlarmCount_Object = MibTableColumn
nms553AlarmCount = _Nms553AlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 8, 1, 1, 3),
    _Nms553AlarmCount_Type()
)
nms553AlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553AlarmCount.setStatus("mandatory")
_Nms553AlarmFirstOccurrenceHours_Type = Integer32
_Nms553AlarmFirstOccurrenceHours_Object = MibTableColumn
nms553AlarmFirstOccurrenceHours = _Nms553AlarmFirstOccurrenceHours_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 8, 1, 1, 4),
    _Nms553AlarmFirstOccurrenceHours_Type()
)
nms553AlarmFirstOccurrenceHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553AlarmFirstOccurrenceHours.setStatus("mandatory")
_Nms553AlarmFirstOccurrenceMinutes_Type = Integer32
_Nms553AlarmFirstOccurrenceMinutes_Object = MibTableColumn
nms553AlarmFirstOccurrenceMinutes = _Nms553AlarmFirstOccurrenceMinutes_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 8, 1, 1, 5),
    _Nms553AlarmFirstOccurrenceMinutes_Type()
)
nms553AlarmFirstOccurrenceMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553AlarmFirstOccurrenceMinutes.setStatus("mandatory")
_Nms553AlarmFirstOccurrenceSeconds_Type = Integer32
_Nms553AlarmFirstOccurrenceSeconds_Object = MibTableColumn
nms553AlarmFirstOccurrenceSeconds = _Nms553AlarmFirstOccurrenceSeconds_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 8, 1, 1, 6),
    _Nms553AlarmFirstOccurrenceSeconds_Type()
)
nms553AlarmFirstOccurrenceSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553AlarmFirstOccurrenceSeconds.setStatus("mandatory")
_Nms553AlarmFirstOccurrenceMonth_Type = Integer32
_Nms553AlarmFirstOccurrenceMonth_Object = MibTableColumn
nms553AlarmFirstOccurrenceMonth = _Nms553AlarmFirstOccurrenceMonth_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 8, 1, 1, 7),
    _Nms553AlarmFirstOccurrenceMonth_Type()
)
nms553AlarmFirstOccurrenceMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553AlarmFirstOccurrenceMonth.setStatus("mandatory")
_Nms553AlarmFirstOccurrenceDay_Type = Integer32
_Nms553AlarmFirstOccurrenceDay_Object = MibTableColumn
nms553AlarmFirstOccurrenceDay = _Nms553AlarmFirstOccurrenceDay_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 8, 1, 1, 8),
    _Nms553AlarmFirstOccurrenceDay_Type()
)
nms553AlarmFirstOccurrenceDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553AlarmFirstOccurrenceDay.setStatus("mandatory")
_Nms553AlarmFirstOccurrenceYear_Type = Integer32
_Nms553AlarmFirstOccurrenceYear_Object = MibTableColumn
nms553AlarmFirstOccurrenceYear = _Nms553AlarmFirstOccurrenceYear_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 8, 1, 1, 9),
    _Nms553AlarmFirstOccurrenceYear_Type()
)
nms553AlarmFirstOccurrenceYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553AlarmFirstOccurrenceYear.setStatus("mandatory")
_Nms553AlarmLastOccurrenceHours_Type = Integer32
_Nms553AlarmLastOccurrenceHours_Object = MibTableColumn
nms553AlarmLastOccurrenceHours = _Nms553AlarmLastOccurrenceHours_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 8, 1, 1, 10),
    _Nms553AlarmLastOccurrenceHours_Type()
)
nms553AlarmLastOccurrenceHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553AlarmLastOccurrenceHours.setStatus("mandatory")
_Nms553AlarmLastOccurrenceMinutes_Type = Integer32
_Nms553AlarmLastOccurrenceMinutes_Object = MibTableColumn
nms553AlarmLastOccurrenceMinutes = _Nms553AlarmLastOccurrenceMinutes_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 8, 1, 1, 11),
    _Nms553AlarmLastOccurrenceMinutes_Type()
)
nms553AlarmLastOccurrenceMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553AlarmLastOccurrenceMinutes.setStatus("mandatory")
_Nms553AlarmLastOccurrenceSeconds_Type = Integer32
_Nms553AlarmLastOccurrenceSeconds_Object = MibTableColumn
nms553AlarmLastOccurrenceSeconds = _Nms553AlarmLastOccurrenceSeconds_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 8, 1, 1, 12),
    _Nms553AlarmLastOccurrenceSeconds_Type()
)
nms553AlarmLastOccurrenceSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553AlarmLastOccurrenceSeconds.setStatus("mandatory")
_Nms553AlarmLastOccurrenceMonth_Type = Integer32
_Nms553AlarmLastOccurrenceMonth_Object = MibTableColumn
nms553AlarmLastOccurrenceMonth = _Nms553AlarmLastOccurrenceMonth_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 8, 1, 1, 13),
    _Nms553AlarmLastOccurrenceMonth_Type()
)
nms553AlarmLastOccurrenceMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553AlarmLastOccurrenceMonth.setStatus("mandatory")
_Nms553AlarmLastOccurrenceDay_Type = Integer32
_Nms553AlarmLastOccurrenceDay_Object = MibTableColumn
nms553AlarmLastOccurrenceDay = _Nms553AlarmLastOccurrenceDay_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 8, 1, 1, 14),
    _Nms553AlarmLastOccurrenceDay_Type()
)
nms553AlarmLastOccurrenceDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553AlarmLastOccurrenceDay.setStatus("mandatory")
_Nms553AlarmLastOccurrenceYear_Type = Integer32
_Nms553AlarmLastOccurrenceYear_Object = MibTableColumn
nms553AlarmLastOccurrenceYear = _Nms553AlarmLastOccurrenceYear_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 8, 1, 1, 15),
    _Nms553AlarmLastOccurrenceYear_Type()
)
nms553AlarmLastOccurrenceYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553AlarmLastOccurrenceYear.setStatus("mandatory")
_Nms553AlarmMaintenanceTable_Object = MibTable
nms553AlarmMaintenanceTable = _Nms553AlarmMaintenanceTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 8, 2)
)
if mibBuilder.loadTexts:
    nms553AlarmMaintenanceTable.setStatus("mandatory")
_Nms553AlarmMaintenanceEntry_Object = MibTableRow
nms553AlarmMaintenanceEntry = _Nms553AlarmMaintenanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 8, 2, 1)
)
nms553AlarmMaintenanceEntry.setIndexNames(
    (0, "NMS-553-MIB", "nms553AlarmMaintenanceIndex"),
)
if mibBuilder.loadTexts:
    nms553AlarmMaintenanceEntry.setStatus("mandatory")
_Nms553AlarmMaintenanceIndex_Type = SCinstance
_Nms553AlarmMaintenanceIndex_Object = MibTableColumn
nms553AlarmMaintenanceIndex = _Nms553AlarmMaintenanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 8, 2, 1, 1),
    _Nms553AlarmMaintenanceIndex_Type()
)
nms553AlarmMaintenanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553AlarmMaintenanceIndex.setStatus("mandatory")


class _Nms553ClearAlarmHistory_Type(Integer32):
    """Custom type nms553ClearAlarmHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("norm", 2))
    )


_Nms553ClearAlarmHistory_Type.__name__ = "Integer32"
_Nms553ClearAlarmHistory_Object = MibTableColumn
nms553ClearAlarmHistory = _Nms553ClearAlarmHistory_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 8, 2, 1, 2),
    _Nms553ClearAlarmHistory_Type()
)
nms553ClearAlarmHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553ClearAlarmHistory.setStatus("mandatory")
_Nms553RTCHours_Type = Integer32
_Nms553RTCHours_Object = MibTableColumn
nms553RTCHours = _Nms553RTCHours_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 8, 2, 1, 3),
    _Nms553RTCHours_Type()
)
nms553RTCHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553RTCHours.setStatus("mandatory")
_Nms553RTCMinutes_Type = Integer32
_Nms553RTCMinutes_Object = MibTableColumn
nms553RTCMinutes = _Nms553RTCMinutes_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 8, 2, 1, 4),
    _Nms553RTCMinutes_Type()
)
nms553RTCMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553RTCMinutes.setStatus("mandatory")
_Nms553RTCSeconds_Type = Integer32
_Nms553RTCSeconds_Object = MibTableColumn
nms553RTCSeconds = _Nms553RTCSeconds_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 8, 2, 1, 5),
    _Nms553RTCSeconds_Type()
)
nms553RTCSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553RTCSeconds.setStatus("mandatory")
_Nms553RTCMonth_Type = Integer32
_Nms553RTCMonth_Object = MibTableColumn
nms553RTCMonth = _Nms553RTCMonth_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 8, 2, 1, 6),
    _Nms553RTCMonth_Type()
)
nms553RTCMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553RTCMonth.setStatus("mandatory")
_Nms553RTCDay_Type = Integer32
_Nms553RTCDay_Object = MibTableColumn
nms553RTCDay = _Nms553RTCDay_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 8, 2, 1, 7),
    _Nms553RTCDay_Type()
)
nms553RTCDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553RTCDay.setStatus("mandatory")
_Nms553RTCYear_Type = Integer32
_Nms553RTCYear_Object = MibTableColumn
nms553RTCYear = _Nms553RTCYear_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 8, 2, 1, 8),
    _Nms553RTCYear_Type()
)
nms553RTCYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nms553RTCYear.setStatus("mandatory")


class _Nms553TimeOfLastAlarmClear_Type(OctetString):
    """Custom type nms553TimeOfLastAlarmClear based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Nms553TimeOfLastAlarmClear_Type.__name__ = "OctetString"
_Nms553TimeOfLastAlarmClear_Object = MibTableColumn
nms553TimeOfLastAlarmClear = _Nms553TimeOfLastAlarmClear_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 8, 2, 1, 9),
    _Nms553TimeOfLastAlarmClear_Type()
)
nms553TimeOfLastAlarmClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553TimeOfLastAlarmClear.setStatus("mandatory")
_Nms553Performance_ObjectIdentity = ObjectIdentity
nms553Performance = _Nms553Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 9)
)
_Nms553CurrentTable_Object = MibTable
nms553CurrentTable = _Nms553CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 9, 1)
)
if mibBuilder.loadTexts:
    nms553CurrentTable.setStatus("mandatory")
_Nms553CurrentEntry_Object = MibTableRow
nms553CurrentEntry = _Nms553CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 9, 1, 1)
)
nms553CurrentEntry.setIndexNames(
    (0, "NMS-553-MIB", "nms553CurrentIndex"),
)
if mibBuilder.loadTexts:
    nms553CurrentEntry.setStatus("mandatory")
_Nms553CurrentIndex_Type = SCinstance
_Nms553CurrentIndex_Object = MibTableColumn
nms553CurrentIndex = _Nms553CurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 9, 1, 1, 1),
    _Nms553CurrentIndex_Type()
)
nms553CurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553CurrentIndex.setStatus("mandatory")
_Nms553CurrentESs_Type = Gauge32
_Nms553CurrentESs_Object = MibTableColumn
nms553CurrentESs = _Nms553CurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 9, 1, 1, 2),
    _Nms553CurrentESs_Type()
)
nms553CurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553CurrentESs.setStatus("mandatory")
_Nms553CurrentSESs_Type = Gauge32
_Nms553CurrentSESs_Object = MibTableColumn
nms553CurrentSESs = _Nms553CurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 9, 1, 1, 3),
    _Nms553CurrentSESs_Type()
)
nms553CurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553CurrentSESs.setStatus("mandatory")
_Nms553CurrentBESs_Type = Gauge32
_Nms553CurrentBESs_Object = MibTableColumn
nms553CurrentBESs = _Nms553CurrentBESs_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 9, 1, 1, 4),
    _Nms553CurrentBESs_Type()
)
nms553CurrentBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553CurrentBESs.setStatus("mandatory")
_Nms553CurrentUASs_Type = Gauge32
_Nms553CurrentUASs_Object = MibTableColumn
nms553CurrentUASs = _Nms553CurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 9, 1, 1, 5),
    _Nms553CurrentUASs_Type()
)
nms553CurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553CurrentUASs.setStatus("mandatory")
_Nms553CurrentLOFCs_Type = Gauge32
_Nms553CurrentLOFCs_Object = MibTableColumn
nms553CurrentLOFCs = _Nms553CurrentLOFCs_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 9, 1, 1, 6),
    _Nms553CurrentLOFCs_Type()
)
nms553CurrentLOFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553CurrentLOFCs.setStatus("mandatory")
_Nms553CurrentCSSs_Type = Gauge32
_Nms553CurrentCSSs_Object = MibTableColumn
nms553CurrentCSSs = _Nms553CurrentCSSs_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 9, 1, 1, 7),
    _Nms553CurrentCSSs_Type()
)
nms553CurrentCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553CurrentCSSs.setStatus("mandatory")
_Nms553IntervalTable_Object = MibTable
nms553IntervalTable = _Nms553IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 9, 2)
)
if mibBuilder.loadTexts:
    nms553IntervalTable.setStatus("mandatory")
_Nms553IntervalEntry_Object = MibTableRow
nms553IntervalEntry = _Nms553IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 9, 2, 1)
)
nms553IntervalEntry.setIndexNames(
    (0, "NMS-553-MIB", "nms553IntervalIndex"),
    (0, "NMS-553-MIB", "nms553IntervalNumber"),
)
if mibBuilder.loadTexts:
    nms553IntervalEntry.setStatus("mandatory")
_Nms553IntervalIndex_Type = SCinstance
_Nms553IntervalIndex_Object = MibTableColumn
nms553IntervalIndex = _Nms553IntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 9, 2, 1, 1),
    _Nms553IntervalIndex_Type()
)
nms553IntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553IntervalIndex.setStatus("mandatory")


class _Nms553IntervalNumber_Type(Integer32):
    """Custom type nms553IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Nms553IntervalNumber_Type.__name__ = "Integer32"
_Nms553IntervalNumber_Object = MibTableColumn
nms553IntervalNumber = _Nms553IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 9, 2, 1, 2),
    _Nms553IntervalNumber_Type()
)
nms553IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553IntervalNumber.setStatus("mandatory")
_Nms553IntervalESs_Type = Gauge32
_Nms553IntervalESs_Object = MibTableColumn
nms553IntervalESs = _Nms553IntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 9, 2, 1, 3),
    _Nms553IntervalESs_Type()
)
nms553IntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553IntervalESs.setStatus("mandatory")
_Nms553IntervalSESs_Type = Gauge32
_Nms553IntervalSESs_Object = MibTableColumn
nms553IntervalSESs = _Nms553IntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 9, 2, 1, 4),
    _Nms553IntervalSESs_Type()
)
nms553IntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553IntervalSESs.setStatus("mandatory")
_Nms553IntervalBESs_Type = Gauge32
_Nms553IntervalBESs_Object = MibTableColumn
nms553IntervalBESs = _Nms553IntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 9, 2, 1, 5),
    _Nms553IntervalBESs_Type()
)
nms553IntervalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553IntervalBESs.setStatus("mandatory")
_Nms553IntervalUASs_Type = Gauge32
_Nms553IntervalUASs_Object = MibTableColumn
nms553IntervalUASs = _Nms553IntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 9, 2, 1, 6),
    _Nms553IntervalUASs_Type()
)
nms553IntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553IntervalUASs.setStatus("mandatory")
_Nms553IntervalLOFCs_Type = Gauge32
_Nms553IntervalLOFCs_Object = MibTableColumn
nms553IntervalLOFCs = _Nms553IntervalLOFCs_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 9, 2, 1, 7),
    _Nms553IntervalLOFCs_Type()
)
nms553IntervalLOFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553IntervalLOFCs.setStatus("mandatory")
_Nms553IntervalCSSs_Type = Gauge32
_Nms553IntervalCSSs_Object = MibTableColumn
nms553IntervalCSSs = _Nms553IntervalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 9, 2, 1, 8),
    _Nms553IntervalCSSs_Type()
)
nms553IntervalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553IntervalCSSs.setStatus("mandatory")
_Nms553TotalTable_Object = MibTable
nms553TotalTable = _Nms553TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 9, 3)
)
if mibBuilder.loadTexts:
    nms553TotalTable.setStatus("mandatory")
_Nms553TotalEntry_Object = MibTableRow
nms553TotalEntry = _Nms553TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 9, 3, 1)
)
nms553TotalEntry.setIndexNames(
    (0, "NMS-553-MIB", "nms553TotalIndex"),
)
if mibBuilder.loadTexts:
    nms553TotalEntry.setStatus("mandatory")
_Nms553TotalIndex_Type = SCinstance
_Nms553TotalIndex_Object = MibTableColumn
nms553TotalIndex = _Nms553TotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 9, 3, 1, 1),
    _Nms553TotalIndex_Type()
)
nms553TotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553TotalIndex.setStatus("mandatory")
_Nms553TotalESs_Type = Gauge32
_Nms553TotalESs_Object = MibTableColumn
nms553TotalESs = _Nms553TotalESs_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 9, 3, 1, 2),
    _Nms553TotalESs_Type()
)
nms553TotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553TotalESs.setStatus("mandatory")
_Nms553TotalSESs_Type = Gauge32
_Nms553TotalSESs_Object = MibTableColumn
nms553TotalSESs = _Nms553TotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 9, 3, 1, 3),
    _Nms553TotalSESs_Type()
)
nms553TotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553TotalSESs.setStatus("mandatory")
_Nms553TotalBESs_Type = Gauge32
_Nms553TotalBESs_Object = MibTableColumn
nms553TotalBESs = _Nms553TotalBESs_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 9, 3, 1, 4),
    _Nms553TotalBESs_Type()
)
nms553TotalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553TotalBESs.setStatus("mandatory")
_Nms553TotalUASs_Type = Gauge32
_Nms553TotalUASs_Object = MibTableColumn
nms553TotalUASs = _Nms553TotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 9, 3, 1, 5),
    _Nms553TotalUASs_Type()
)
nms553TotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553TotalUASs.setStatus("mandatory")
_Nms553TotalLOFCs_Type = Gauge32
_Nms553TotalLOFCs_Object = MibTableColumn
nms553TotalLOFCs = _Nms553TotalLOFCs_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 9, 3, 1, 6),
    _Nms553TotalLOFCs_Type()
)
nms553TotalLOFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553TotalLOFCs.setStatus("mandatory")
_Nms553TotalCSSs_Type = Gauge32
_Nms553TotalCSSs_Object = MibTableColumn
nms553TotalCSSs = _Nms553TotalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 498, 6, 7, 9, 3, 1, 7),
    _Nms553TotalCSSs_Type()
)
nms553TotalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nms553TotalCSSs.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-553-MIB",
    **{"dsx1": dsx1,
       "nms553": nms553,
       "nms553Version": nms553Version,
       "nms553MIBversion": nms553MIBversion,
       "nms553VersionTable": nms553VersionTable,
       "nms553VersionEntry": nms553VersionEntry,
       "nms553VersionIndex": nms553VersionIndex,
       "nms553FirmwareRev": nms553FirmwareRev,
       "nms553DS0Allocation": nms553DS0Allocation,
       "nms553DS0AllocationSchemeTable": nms553DS0AllocationSchemeTable,
       "nms553DS0AllocationSchemeEntry": nms553DS0AllocationSchemeEntry,
       "nms553DS0AllocationSchemeIndex": nms553DS0AllocationSchemeIndex,
       "nms553DS0AllocationScheme": nms553DS0AllocationScheme,
       "nms553DS0AllocationConfigTable": nms553DS0AllocationConfigTable,
       "nms553DS0AllocationConfigEntry": nms553DS0AllocationConfigEntry,
       "nms553DS0AllocationConfigIndex": nms553DS0AllocationConfigIndex,
       "nms553DS0AllocationBaseRate": nms553DS0AllocationBaseRate,
       "nms553DS0AllocationStartingDS0": nms553DS0AllocationStartingDS0,
       "nms553DS0AllocationNumberOfDS0s": nms553DS0AllocationNumberOfDS0s,
       "nms553DS0AllocationInbandDccMode": nms553DS0AllocationInbandDccMode,
       "nms553Configuration": nms553Configuration,
       "nms553ChannelConfigTable": nms553ChannelConfigTable,
       "nms553ChannelConfigEntry": nms553ChannelConfigEntry,
       "nms553ChannelConfigIndex": nms553ChannelConfigIndex,
       "nms553ChannelSplitTiming": nms553ChannelSplitTiming,
       "nms553ChannelChannelType": nms553ChannelChannelType,
       "nms553ChannelClockInvert": nms553ChannelClockInvert,
       "nms553ChannelDataInvert": nms553ChannelDataInvert,
       "nms553ChannelLocalDCD": nms553ChannelLocalDCD,
       "nms553ChannelLocalDSR": nms553ChannelLocalDSR,
       "nms553ChannelFlowControl": nms553ChannelFlowControl,
       "nms553ChannelRTSCTSControl": nms553ChannelRTSCTSControl,
       "nms553ChannelEIAtestLeads": nms553ChannelEIAtestLeads,
       "nms553ChannelInbandLoop": nms553ChannelInbandLoop,
       "nms553ChannelInbandLoopCode": nms553ChannelInbandLoopCode,
       "nms553ChannelInbandLoopdown": nms553ChannelInbandLoopdown,
       "nms553ChannelControlModeIdle": nms553ChannelControlModeIdle,
       "nms553NetworkConfigTable": nms553NetworkConfigTable,
       "nms553NetworkConfigEntry": nms553NetworkConfigEntry,
       "nms553NetworkConfigIndex": nms553NetworkConfigIndex,
       "nms553NetworkAdminLineType": nms553NetworkAdminLineType,
       "nms553NetworkOperLineType": nms553NetworkOperLineType,
       "nms553NetworkInterfaceType": nms553NetworkInterfaceType,
       "nms553NetworkPreequalization": nms553NetworkPreequalization,
       "nms553NetworkAdminLineBuildout": nms553NetworkAdminLineBuildout,
       "nms553NetworkOperLineBuildout": nms553NetworkOperLineBuildout,
       "nms553NetworkOnesDensity": nms553NetworkOnesDensity,
       "nms553NetworkTransmitClockSource": nms553NetworkTransmitClockSource,
       "nms553NetworkFallbackClockSource": nms553NetworkFallbackClockSource,
       "nms553NetworkFDLdcc": nms553NetworkFDLdcc,
       "nms553NetworkAISLoopdown": nms553NetworkAISLoopdown,
       "nms553NetworkInbandFrame": nms553NetworkInbandFrame,
       "nms553NetworkLoopbackConfig": nms553NetworkLoopbackConfig,
       "nms553NetworkLineCoding": nms553NetworkLineCoding,
       "nms553NetworkFdl": nms553NetworkFdl,
       "nms553ConfigurationSave": nms553ConfigurationSave,
       "nms553DteStatus": nms553DteStatus,
       "nms553DteStatusTable": nms553DteStatusTable,
       "nms553DteStatusEntry": nms553DteStatusEntry,
       "nms553DteStatusIndex": nms553DteStatusIndex,
       "nms553DteStat": nms553DteStat,
       "nms553Diagnostics": nms553Diagnostics,
       "nms553DiagTable": nms553DiagTable,
       "nms553DiagEntry": nms553DiagEntry,
       "nms553DiagIndex": nms553DiagIndex,
       "nms553DiagTestDuration": nms553DiagTestDuration,
       "nms553DiagProgPattern": nms553DiagProgPattern,
       "nms553DiagBeginSelfTest": nms553DiagBeginSelfTest,
       "nms553DiagBeginLoopTest": nms553DiagBeginLoopTest,
       "nms553DiagTestResults": nms553DiagTestResults,
       "nms553DiagResetTestToNormal": nms553DiagResetTestToNormal,
       "nms553DiagTestStatus": nms553DiagTestStatus,
       "nms553Maintenance": nms553Maintenance,
       "nms553MaintenanceTable": nms553MaintenanceTable,
       "nms553MaintenanceEntry": nms553MaintenanceEntry,
       "nms553MaintenanceIndex": nms553MaintenanceIndex,
       "nms553LedStatus": nms553LedStatus,
       "nms553SoftReset": nms553SoftReset,
       "nms553DefaultInit": nms553DefaultInit,
       "nms553FrontPanel": nms553FrontPanel,
       "nms553ProductType": nms553ProductType,
       "nms553ResetStatistics": nms553ResetStatistics,
       "nms553ValidIntervals": nms553ValidIntervals,
       "nms553CascadePresent": nms553CascadePresent,
       "nms553ReceiveLevel": nms553ReceiveLevel,
       "nms553Alarms": nms553Alarms,
       "nms553AlarmData": nms553AlarmData,
       "nms553NoResponseAlm": nms553NoResponseAlm,
       "nms553DiagRxErrAlm": nms553DiagRxErrAlm,
       "nms553PowerUpAlm": nms553PowerUpAlm,
       "nms553NvRamCorrupt": nms553NvRamCorrupt,
       "nms553UnitFailure": nms553UnitFailure,
       "nms553TimingLoss": nms553TimingLoss,
       "nms553StatusChange": nms553StatusChange,
       "nms553UnsolicitedTest": nms553UnsolicitedTest,
       "nms553LossOfSignal": nms553LossOfSignal,
       "nms553LossOfFrame": nms553LossOfFrame,
       "nms553AlarmIndicationSignal": nms553AlarmIndicationSignal,
       "nms553ReceivedYellow": nms553ReceivedYellow,
       "nms553UnavailableSignalState": nms553UnavailableSignalState,
       "nms553ExcessiveZeros": nms553ExcessiveZeros,
       "nms553LowAverageDensity": nms553LowAverageDensity,
       "nms553ControlledSlips": nms553ControlledSlips,
       "nms553BipolarViolations": nms553BipolarViolations,
       "nms553CrcErrors": nms553CrcErrors,
       "nms553AlarmConfigTable": nms553AlarmConfigTable,
       "nms553AlarmConfigEntry": nms553AlarmConfigEntry,
       "nms553AlarmConfigIndex": nms553AlarmConfigIndex,
       "nms553AlarmConfigIdentifier": nms553AlarmConfigIdentifier,
       "nms553AlarmCountWindow": nms553AlarmCountWindow,
       "nms553AlarmCountThreshold": nms553AlarmCountThreshold,
       "nms553AlarmHistory": nms553AlarmHistory,
       "nms553AlarmHistoryTable": nms553AlarmHistoryTable,
       "nms553AlarmHistoryEntry": nms553AlarmHistoryEntry,
       "nms553AlarmHistoryIndex": nms553AlarmHistoryIndex,
       "nms553AlarmHistoryIdentifier": nms553AlarmHistoryIdentifier,
       "nms553AlarmCount": nms553AlarmCount,
       "nms553AlarmFirstOccurrenceHours": nms553AlarmFirstOccurrenceHours,
       "nms553AlarmFirstOccurrenceMinutes": nms553AlarmFirstOccurrenceMinutes,
       "nms553AlarmFirstOccurrenceSeconds": nms553AlarmFirstOccurrenceSeconds,
       "nms553AlarmFirstOccurrenceMonth": nms553AlarmFirstOccurrenceMonth,
       "nms553AlarmFirstOccurrenceDay": nms553AlarmFirstOccurrenceDay,
       "nms553AlarmFirstOccurrenceYear": nms553AlarmFirstOccurrenceYear,
       "nms553AlarmLastOccurrenceHours": nms553AlarmLastOccurrenceHours,
       "nms553AlarmLastOccurrenceMinutes": nms553AlarmLastOccurrenceMinutes,
       "nms553AlarmLastOccurrenceSeconds": nms553AlarmLastOccurrenceSeconds,
       "nms553AlarmLastOccurrenceMonth": nms553AlarmLastOccurrenceMonth,
       "nms553AlarmLastOccurrenceDay": nms553AlarmLastOccurrenceDay,
       "nms553AlarmLastOccurrenceYear": nms553AlarmLastOccurrenceYear,
       "nms553AlarmMaintenanceTable": nms553AlarmMaintenanceTable,
       "nms553AlarmMaintenanceEntry": nms553AlarmMaintenanceEntry,
       "nms553AlarmMaintenanceIndex": nms553AlarmMaintenanceIndex,
       "nms553ClearAlarmHistory": nms553ClearAlarmHistory,
       "nms553RTCHours": nms553RTCHours,
       "nms553RTCMinutes": nms553RTCMinutes,
       "nms553RTCSeconds": nms553RTCSeconds,
       "nms553RTCMonth": nms553RTCMonth,
       "nms553RTCDay": nms553RTCDay,
       "nms553RTCYear": nms553RTCYear,
       "nms553TimeOfLastAlarmClear": nms553TimeOfLastAlarmClear,
       "nms553Performance": nms553Performance,
       "nms553CurrentTable": nms553CurrentTable,
       "nms553CurrentEntry": nms553CurrentEntry,
       "nms553CurrentIndex": nms553CurrentIndex,
       "nms553CurrentESs": nms553CurrentESs,
       "nms553CurrentSESs": nms553CurrentSESs,
       "nms553CurrentBESs": nms553CurrentBESs,
       "nms553CurrentUASs": nms553CurrentUASs,
       "nms553CurrentLOFCs": nms553CurrentLOFCs,
       "nms553CurrentCSSs": nms553CurrentCSSs,
       "nms553IntervalTable": nms553IntervalTable,
       "nms553IntervalEntry": nms553IntervalEntry,
       "nms553IntervalIndex": nms553IntervalIndex,
       "nms553IntervalNumber": nms553IntervalNumber,
       "nms553IntervalESs": nms553IntervalESs,
       "nms553IntervalSESs": nms553IntervalSESs,
       "nms553IntervalBESs": nms553IntervalBESs,
       "nms553IntervalUASs": nms553IntervalUASs,
       "nms553IntervalLOFCs": nms553IntervalLOFCs,
       "nms553IntervalCSSs": nms553IntervalCSSs,
       "nms553TotalTable": nms553TotalTable,
       "nms553TotalEntry": nms553TotalEntry,
       "nms553TotalIndex": nms553TotalIndex,
       "nms553TotalESs": nms553TotalESs,
       "nms553TotalSESs": nms553TotalSESs,
       "nms553TotalBESs": nms553TotalBESs,
       "nms553TotalUASs": nms553TotalUASs,
       "nms553TotalLOFCs": nms553TotalLOFCs,
       "nms553TotalCSSs": nms553TotalCSSs}
)
