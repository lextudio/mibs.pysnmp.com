# SNMP MIB module (GDC-DSU-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GDC-DSU-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:08 2024
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
_Dsu_ObjectIdentity = ObjectIdentity
dsu = _Dsu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8)
)
_T1_ObjectIdentity = ObjectIdentity
t1 = _T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 5)
)
_GdcDsuDS0AllocationSchemeTable_Object = MibTable
gdcDsuDS0AllocationSchemeTable = _GdcDsuDS0AllocationSchemeTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 1)
)
if mibBuilder.loadTexts:
    gdcDsuDS0AllocationSchemeTable.setStatus("mandatory")
_GdcDsuDS0AllocationSchemeEntry_Object = MibTableRow
gdcDsuDS0AllocationSchemeEntry = _GdcDsuDS0AllocationSchemeEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 1, 1)
)
gdcDsuDS0AllocationSchemeEntry.setIndexNames(
    (0, "GDC-DSU-MGMT-MIB", "gdcDsuDS0AllocationIndex"),
)
if mibBuilder.loadTexts:
    gdcDsuDS0AllocationSchemeEntry.setStatus("mandatory")
_GdcDsuDS0AllocationIndex_Type = SCinstance
_GdcDsuDS0AllocationIndex_Object = MibTableColumn
gdcDsuDS0AllocationIndex = _GdcDsuDS0AllocationIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 1, 1, 1),
    _GdcDsuDS0AllocationIndex_Type()
)
gdcDsuDS0AllocationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsuDS0AllocationIndex.setStatus("mandatory")


class _GdcDsuDS0AllocationScheme_Type(Integer32):
    """Custom type gdcDsuDS0AllocationScheme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 3),
          ("consecutive", 2),
          ("other", 1))
    )


_GdcDsuDS0AllocationScheme_Type.__name__ = "Integer32"
_GdcDsuDS0AllocationScheme_Object = MibTableColumn
gdcDsuDS0AllocationScheme = _GdcDsuDS0AllocationScheme_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 1, 1, 2),
    _GdcDsuDS0AllocationScheme_Type()
)
gdcDsuDS0AllocationScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsuDS0AllocationScheme.setStatus("mandatory")
_GdcDsuChannelConfigTable_Object = MibTable
gdcDsuChannelConfigTable = _GdcDsuChannelConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 2)
)
if mibBuilder.loadTexts:
    gdcDsuChannelConfigTable.setStatus("mandatory")
_GdcDsuChannelConfigEntry_Object = MibTableRow
gdcDsuChannelConfigEntry = _GdcDsuChannelConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1)
)
gdcDsuChannelConfigEntry.setIndexNames(
    (0, "GDC-DSU-MGMT-MIB", "gdcDsuChannelConfigIndex"),
)
if mibBuilder.loadTexts:
    gdcDsuChannelConfigEntry.setStatus("mandatory")
_GdcDsuChannelConfigIndex_Type = SCinstance
_GdcDsuChannelConfigIndex_Object = MibTableColumn
gdcDsuChannelConfigIndex = _GdcDsuChannelConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 1),
    _GdcDsuChannelConfigIndex_Type()
)
gdcDsuChannelConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsuChannelConfigIndex.setStatus("mandatory")


class _GdcDsuChannelBaseRate_Type(Integer32):
    """Custom type gdcDsuChannelBaseRate based on Integer32"""
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


_GdcDsuChannelBaseRate_Type.__name__ = "Integer32"
_GdcDsuChannelBaseRate_Object = MibTableColumn
gdcDsuChannelBaseRate = _GdcDsuChannelBaseRate_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 2),
    _GdcDsuChannelBaseRate_Type()
)
gdcDsuChannelBaseRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsuChannelBaseRate.setStatus("mandatory")


class _GdcDsuChannelStartingDS0_Type(Integer32):
    """Custom type gdcDsuChannelStartingDS0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_GdcDsuChannelStartingDS0_Type.__name__ = "Integer32"
_GdcDsuChannelStartingDS0_Object = MibTableColumn
gdcDsuChannelStartingDS0 = _GdcDsuChannelStartingDS0_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 3),
    _GdcDsuChannelStartingDS0_Type()
)
gdcDsuChannelStartingDS0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsuChannelStartingDS0.setStatus("mandatory")


class _GdcDsuChannelNumberOfDS0s_Type(Integer32):
    """Custom type gdcDsuChannelNumberOfDS0s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_GdcDsuChannelNumberOfDS0s_Type.__name__ = "Integer32"
_GdcDsuChannelNumberOfDS0s_Object = MibTableColumn
gdcDsuChannelNumberOfDS0s = _GdcDsuChannelNumberOfDS0s_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 4),
    _GdcDsuChannelNumberOfDS0s_Type()
)
gdcDsuChannelNumberOfDS0s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsuChannelNumberOfDS0s.setStatus("mandatory")


class _GdcDsuChannelSplitTiming_Type(Integer32):
    """Custom type gdcDsuChannelSplitTiming based on Integer32"""
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


_GdcDsuChannelSplitTiming_Type.__name__ = "Integer32"
_GdcDsuChannelSplitTiming_Object = MibTableColumn
gdcDsuChannelSplitTiming = _GdcDsuChannelSplitTiming_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 5),
    _GdcDsuChannelSplitTiming_Type()
)
gdcDsuChannelSplitTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsuChannelSplitTiming.setStatus("mandatory")


class _GdcDsuChannelChannelType_Type(Integer32):
    """Custom type gdcDsuChannelChannelType based on Integer32"""
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
        *(("dra", 5),
          ("eia530", 4),
          ("none", 2),
          ("other", 1),
          ("v35", 3))
    )


_GdcDsuChannelChannelType_Type.__name__ = "Integer32"
_GdcDsuChannelChannelType_Object = MibTableColumn
gdcDsuChannelChannelType = _GdcDsuChannelChannelType_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 6),
    _GdcDsuChannelChannelType_Type()
)
gdcDsuChannelChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsuChannelChannelType.setStatus("mandatory")


class _GdcDsuChannelTransmitClockInvert_Type(Integer32):
    """Custom type gdcDsuChannelTransmitClockInvert based on Integer32"""
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


_GdcDsuChannelTransmitClockInvert_Type.__name__ = "Integer32"
_GdcDsuChannelTransmitClockInvert_Object = MibTableColumn
gdcDsuChannelTransmitClockInvert = _GdcDsuChannelTransmitClockInvert_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 7),
    _GdcDsuChannelTransmitClockInvert_Type()
)
gdcDsuChannelTransmitClockInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsuChannelTransmitClockInvert.setStatus("mandatory")


class _GdcDsuChannelReceiveClockInvert_Type(Integer32):
    """Custom type gdcDsuChannelReceiveClockInvert based on Integer32"""
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


_GdcDsuChannelReceiveClockInvert_Type.__name__ = "Integer32"
_GdcDsuChannelReceiveClockInvert_Object = MibTableColumn
gdcDsuChannelReceiveClockInvert = _GdcDsuChannelReceiveClockInvert_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 8),
    _GdcDsuChannelReceiveClockInvert_Type()
)
gdcDsuChannelReceiveClockInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsuChannelReceiveClockInvert.setStatus("mandatory")


class _GdcDsuChannelTransmitDataInvert_Type(Integer32):
    """Custom type gdcDsuChannelTransmitDataInvert based on Integer32"""
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


_GdcDsuChannelTransmitDataInvert_Type.__name__ = "Integer32"
_GdcDsuChannelTransmitDataInvert_Object = MibTableColumn
gdcDsuChannelTransmitDataInvert = _GdcDsuChannelTransmitDataInvert_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 9),
    _GdcDsuChannelTransmitDataInvert_Type()
)
gdcDsuChannelTransmitDataInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsuChannelTransmitDataInvert.setStatus("mandatory")


class _GdcDsuChannelReceiveDataInvert_Type(Integer32):
    """Custom type gdcDsuChannelReceiveDataInvert based on Integer32"""
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


_GdcDsuChannelReceiveDataInvert_Type.__name__ = "Integer32"
_GdcDsuChannelReceiveDataInvert_Object = MibTableColumn
gdcDsuChannelReceiveDataInvert = _GdcDsuChannelReceiveDataInvert_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 10),
    _GdcDsuChannelReceiveDataInvert_Type()
)
gdcDsuChannelReceiveDataInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsuChannelReceiveDataInvert.setStatus("mandatory")


class _GdcDsuChannelLocalDCD_Type(Integer32):
    """Custom type gdcDsuChannelLocalDCD based on Integer32"""
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


_GdcDsuChannelLocalDCD_Type.__name__ = "Integer32"
_GdcDsuChannelLocalDCD_Object = MibTableColumn
gdcDsuChannelLocalDCD = _GdcDsuChannelLocalDCD_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 11),
    _GdcDsuChannelLocalDCD_Type()
)
gdcDsuChannelLocalDCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsuChannelLocalDCD.setStatus("mandatory")


class _GdcDsuChannelLocalDSR_Type(Integer32):
    """Custom type gdcDsuChannelLocalDSR based on Integer32"""
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


_GdcDsuChannelLocalDSR_Type.__name__ = "Integer32"
_GdcDsuChannelLocalDSR_Object = MibTableColumn
gdcDsuChannelLocalDSR = _GdcDsuChannelLocalDSR_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 12),
    _GdcDsuChannelLocalDSR_Type()
)
gdcDsuChannelLocalDSR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsuChannelLocalDSR.setStatus("mandatory")


class _GdcDsuChannelReceiveControl_Type(Integer32):
    """Custom type gdcDsuChannelReceiveControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dcd", 1),
          ("dsr", 2))
    )


_GdcDsuChannelReceiveControl_Type.__name__ = "Integer32"
_GdcDsuChannelReceiveControl_Object = MibTableColumn
gdcDsuChannelReceiveControl = _GdcDsuChannelReceiveControl_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 13),
    _GdcDsuChannelReceiveControl_Type()
)
gdcDsuChannelReceiveControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsuChannelReceiveControl.setStatus("mandatory")


class _GdcDsuChannelTransmitControl_Type(Integer32):
    """Custom type gdcDsuChannelTransmitControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtr", 2),
          ("rts", 1))
    )


_GdcDsuChannelTransmitControl_Type.__name__ = "Integer32"
_GdcDsuChannelTransmitControl_Object = MibTableColumn
gdcDsuChannelTransmitControl = _GdcDsuChannelTransmitControl_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 14),
    _GdcDsuChannelTransmitControl_Type()
)
gdcDsuChannelTransmitControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsuChannelTransmitControl.setStatus("mandatory")


class _GdcDsuChannelRTSCTScontrol_Type(Integer32):
    """Custom type gdcDsuChannelRTSCTScontrol based on Integer32"""
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
        *(("ctsDelay10ms", 2),
          ("ctsDelayStandard", 4),
          ("ctsOn", 3),
          ("other", 1))
    )


_GdcDsuChannelRTSCTScontrol_Type.__name__ = "Integer32"
_GdcDsuChannelRTSCTScontrol_Object = MibTableColumn
gdcDsuChannelRTSCTScontrol = _GdcDsuChannelRTSCTScontrol_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 15),
    _GdcDsuChannelRTSCTScontrol_Type()
)
gdcDsuChannelRTSCTScontrol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsuChannelRTSCTScontrol.setStatus("mandatory")


class _GdcDsuChannelEIAtestLeads_Type(Integer32):
    """Custom type gdcDsuChannelEIAtestLeads based on Integer32"""
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


_GdcDsuChannelEIAtestLeads_Type.__name__ = "Integer32"
_GdcDsuChannelEIAtestLeads_Object = MibTableColumn
gdcDsuChannelEIAtestLeads = _GdcDsuChannelEIAtestLeads_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 16),
    _GdcDsuChannelEIAtestLeads_Type()
)
gdcDsuChannelEIAtestLeads.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsuChannelEIAtestLeads.setStatus("mandatory")


class _GdcDsuChannelDccMode_Type(Integer32):
    """Custom type gdcDsuChannelDccMode based on Integer32"""
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
          ("normal", 2),
          ("special", 3))
    )


_GdcDsuChannelDccMode_Type.__name__ = "Integer32"
_GdcDsuChannelDccMode_Object = MibTableColumn
gdcDsuChannelDccMode = _GdcDsuChannelDccMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 17),
    _GdcDsuChannelDccMode_Type()
)
gdcDsuChannelDccMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsuChannelDccMode.setStatus("mandatory")


class _GdcDsuChannelInbandLoop_Type(Integer32):
    """Custom type gdcDsuChannelInbandLoop based on Integer32"""
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


_GdcDsuChannelInbandLoop_Type.__name__ = "Integer32"
_GdcDsuChannelInbandLoop_Object = MibTableColumn
gdcDsuChannelInbandLoop = _GdcDsuChannelInbandLoop_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 18),
    _GdcDsuChannelInbandLoop_Type()
)
gdcDsuChannelInbandLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsuChannelInbandLoop.setStatus("mandatory")


class _GdcDsuChannelInbandLoopCode_Type(Integer32):
    """Custom type gdcDsuChannelInbandLoopCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("gdcProprietary", 3),
          ("other", 1),
          ("pn127", 2))
    )


_GdcDsuChannelInbandLoopCode_Type.__name__ = "Integer32"
_GdcDsuChannelInbandLoopCode_Object = MibTableColumn
gdcDsuChannelInbandLoopCode = _GdcDsuChannelInbandLoopCode_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 19),
    _GdcDsuChannelInbandLoopCode_Type()
)
gdcDsuChannelInbandLoopCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsuChannelInbandLoopCode.setStatus("mandatory")
_GdcDsuChannelInbandLoopdown_Type = Integer32
_GdcDsuChannelInbandLoopdown_Object = MibTableColumn
gdcDsuChannelInbandLoopdown = _GdcDsuChannelInbandLoopdown_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 20),
    _GdcDsuChannelInbandLoopdown_Type()
)
gdcDsuChannelInbandLoopdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsuChannelInbandLoopdown.setStatus("mandatory")


class _GdcDsuChannelTransmitClockSource_Type(Integer32):
    """Custom type gdcDsuChannelTransmitClockSource based on Integer32"""
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


_GdcDsuChannelTransmitClockSource_Type.__name__ = "Integer32"
_GdcDsuChannelTransmitClockSource_Object = MibTableColumn
gdcDsuChannelTransmitClockSource = _GdcDsuChannelTransmitClockSource_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 21),
    _GdcDsuChannelTransmitClockSource_Type()
)
gdcDsuChannelTransmitClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsuChannelTransmitClockSource.setStatus("mandatory")


class _GdcDsuChannelFallbackClockSource_Type(Integer32):
    """Custom type gdcDsuChannelFallbackClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("channel", 2),
          ("other", 1))
    )


_GdcDsuChannelFallbackClockSource_Type.__name__ = "Integer32"
_GdcDsuChannelFallbackClockSource_Object = MibTableColumn
gdcDsuChannelFallbackClockSource = _GdcDsuChannelFallbackClockSource_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 22),
    _GdcDsuChannelFallbackClockSource_Type()
)
gdcDsuChannelFallbackClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsuChannelFallbackClockSource.setStatus("mandatory")


class _GdcDsuChannelControlModeIdle_Type(Integer32):
    """Custom type gdcDsuChannelControlModeIdle based on Integer32"""
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


_GdcDsuChannelControlModeIdle_Type.__name__ = "Integer32"
_GdcDsuChannelControlModeIdle_Object = MibTableColumn
gdcDsuChannelControlModeIdle = _GdcDsuChannelControlModeIdle_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 2, 1, 23),
    _GdcDsuChannelControlModeIdle_Type()
)
gdcDsuChannelControlModeIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsuChannelControlModeIdle.setStatus("mandatory")
_GdcDsuChannelSignalStatusTable_Object = MibTable
gdcDsuChannelSignalStatusTable = _GdcDsuChannelSignalStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 3)
)
if mibBuilder.loadTexts:
    gdcDsuChannelSignalStatusTable.setStatus("mandatory")
_GdcDsuChannelSignalStatusEntry_Object = MibTableRow
gdcDsuChannelSignalStatusEntry = _GdcDsuChannelSignalStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 3, 1)
)
gdcDsuChannelSignalStatusEntry.setIndexNames(
    (0, "GDC-DSU-MGMT-MIB", "gdcDsuChannelSignalStatusIndex"),
)
if mibBuilder.loadTexts:
    gdcDsuChannelSignalStatusEntry.setStatus("mandatory")
_GdcDsuChannelSignalStatusIndex_Type = SCinstance
_GdcDsuChannelSignalStatusIndex_Object = MibTableColumn
gdcDsuChannelSignalStatusIndex = _GdcDsuChannelSignalStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 3, 1, 1),
    _GdcDsuChannelSignalStatusIndex_Type()
)
gdcDsuChannelSignalStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsuChannelSignalStatusIndex.setStatus("mandatory")


class _GdcDsuChannelCTSstatus_Type(Integer32):
    """Custom type gdcDsuChannelCTSstatus based on Integer32"""
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


_GdcDsuChannelCTSstatus_Type.__name__ = "Integer32"
_GdcDsuChannelCTSstatus_Object = MibTableColumn
gdcDsuChannelCTSstatus = _GdcDsuChannelCTSstatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 3, 1, 2),
    _GdcDsuChannelCTSstatus_Type()
)
gdcDsuChannelCTSstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsuChannelCTSstatus.setStatus("mandatory")


class _GdcDsuChannelRTSstatus_Type(Integer32):
    """Custom type gdcDsuChannelRTSstatus based on Integer32"""
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


_GdcDsuChannelRTSstatus_Type.__name__ = "Integer32"
_GdcDsuChannelRTSstatus_Object = MibTableColumn
gdcDsuChannelRTSstatus = _GdcDsuChannelRTSstatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 3, 1, 3),
    _GdcDsuChannelRTSstatus_Type()
)
gdcDsuChannelRTSstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsuChannelRTSstatus.setStatus("mandatory")


class _GdcDsuChannelDTRstatus_Type(Integer32):
    """Custom type gdcDsuChannelDTRstatus based on Integer32"""
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


_GdcDsuChannelDTRstatus_Type.__name__ = "Integer32"
_GdcDsuChannelDTRstatus_Object = MibTableColumn
gdcDsuChannelDTRstatus = _GdcDsuChannelDTRstatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 3, 1, 4),
    _GdcDsuChannelDTRstatus_Type()
)
gdcDsuChannelDTRstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsuChannelDTRstatus.setStatus("mandatory")


class _GdcDsuChannelDSRstatus_Type(Integer32):
    """Custom type gdcDsuChannelDSRstatus based on Integer32"""
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


_GdcDsuChannelDSRstatus_Type.__name__ = "Integer32"
_GdcDsuChannelDSRstatus_Object = MibTableColumn
gdcDsuChannelDSRstatus = _GdcDsuChannelDSRstatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 3, 1, 5),
    _GdcDsuChannelDSRstatus_Type()
)
gdcDsuChannelDSRstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsuChannelDSRstatus.setStatus("mandatory")


class _GdcDsuChannelDCDstatus_Type(Integer32):
    """Custom type gdcDsuChannelDCDstatus based on Integer32"""
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


_GdcDsuChannelDCDstatus_Type.__name__ = "Integer32"
_GdcDsuChannelDCDstatus_Object = MibTableColumn
gdcDsuChannelDCDstatus = _GdcDsuChannelDCDstatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 3, 1, 6),
    _GdcDsuChannelDCDstatus_Type()
)
gdcDsuChannelDCDstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsuChannelDCDstatus.setStatus("mandatory")


class _GdcDsuChannelRXCstatus_Type(Integer32):
    """Custom type gdcDsuChannelRXCstatus based on Integer32"""
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


_GdcDsuChannelRXCstatus_Type.__name__ = "Integer32"
_GdcDsuChannelRXCstatus_Object = MibTableColumn
gdcDsuChannelRXCstatus = _GdcDsuChannelRXCstatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 3, 1, 7),
    _GdcDsuChannelRXCstatus_Type()
)
gdcDsuChannelRXCstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsuChannelRXCstatus.setStatus("mandatory")


class _GdcDsuChannelTXCstatus_Type(Integer32):
    """Custom type gdcDsuChannelTXCstatus based on Integer32"""
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


_GdcDsuChannelTXCstatus_Type.__name__ = "Integer32"
_GdcDsuChannelTXCstatus_Object = MibTableColumn
gdcDsuChannelTXCstatus = _GdcDsuChannelTXCstatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 3, 1, 8),
    _GdcDsuChannelTXCstatus_Type()
)
gdcDsuChannelTXCstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsuChannelTXCstatus.setStatus("mandatory")


class _GdcDsuChannelRXDstatus_Type(Integer32):
    """Custom type gdcDsuChannelRXDstatus based on Integer32"""
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


_GdcDsuChannelRXDstatus_Type.__name__ = "Integer32"
_GdcDsuChannelRXDstatus_Object = MibTableColumn
gdcDsuChannelRXDstatus = _GdcDsuChannelRXDstatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 3, 1, 9),
    _GdcDsuChannelRXDstatus_Type()
)
gdcDsuChannelRXDstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsuChannelRXDstatus.setStatus("mandatory")


class _GdcDsuChannelTXDstatus_Type(Integer32):
    """Custom type gdcDsuChannelTXDstatus based on Integer32"""
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


_GdcDsuChannelTXDstatus_Type.__name__ = "Integer32"
_GdcDsuChannelTXDstatus_Object = MibTableColumn
gdcDsuChannelTXDstatus = _GdcDsuChannelTXDstatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 3, 1, 10),
    _GdcDsuChannelTXDstatus_Type()
)
gdcDsuChannelTXDstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsuChannelTXDstatus.setStatus("mandatory")
_GdcDsuChannelDiagTable_Object = MibTable
gdcDsuChannelDiagTable = _GdcDsuChannelDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 4)
)
if mibBuilder.loadTexts:
    gdcDsuChannelDiagTable.setStatus("mandatory")
_GdcDsuChannelDiagEntry_Object = MibTableRow
gdcDsuChannelDiagEntry = _GdcDsuChannelDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 4, 1)
)
gdcDsuChannelDiagEntry.setIndexNames(
    (0, "GDC-DSU-MGMT-MIB", "gdcDsuChannelDiagIndex"),
)
if mibBuilder.loadTexts:
    gdcDsuChannelDiagEntry.setStatus("mandatory")
_GdcDsuChannelDiagIndex_Type = SCinstance
_GdcDsuChannelDiagIndex_Object = MibTableColumn
gdcDsuChannelDiagIndex = _GdcDsuChannelDiagIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 4, 1, 1),
    _GdcDsuChannelDiagIndex_Type()
)
gdcDsuChannelDiagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsuChannelDiagIndex.setStatus("mandatory")


class _GdcDsuChannelDiagSendCode_Type(Integer32):
    """Custom type gdcDsuChannelDiagSendCode based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("send2047Pattern", 6),
          ("send2047PatternWithLL", 9),
          ("send2047PatternWithRDL", 10),
          ("send3in24Pattern", 4),
          ("send511Pattern", 3),
          ("send511PatternWithLL", 7),
          ("send511PatternWithRDL", 8),
          ("sendNoCode", 1),
          ("sendProgPattern", 5),
          ("sendQRSpattern", 2))
    )


_GdcDsuChannelDiagSendCode_Type.__name__ = "Integer32"
_GdcDsuChannelDiagSendCode_Object = MibTableColumn
gdcDsuChannelDiagSendCode = _GdcDsuChannelDiagSendCode_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 4, 1, 2),
    _GdcDsuChannelDiagSendCode_Type()
)
gdcDsuChannelDiagSendCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsuChannelDiagSendCode.setStatus("mandatory")


class _GdcDsuChannelDiagProgPattern_Type(Integer32):
    """Custom type gdcDsuChannelDiagProgPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GdcDsuChannelDiagProgPattern_Type.__name__ = "Integer32"
_GdcDsuChannelDiagProgPattern_Object = MibTableColumn
gdcDsuChannelDiagProgPattern = _GdcDsuChannelDiagProgPattern_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 4, 1, 3),
    _GdcDsuChannelDiagProgPattern_Type()
)
gdcDsuChannelDiagProgPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsuChannelDiagProgPattern.setStatus("mandatory")


class _GdcDsuChannelLoopbackConfig_Type(Integer32):
    """Custom type gdcDsuChannelLoopbackConfig based on Integer32"""
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
        *(("digitalLoop", 3),
          ("localLoop", 2),
          ("noLoop", 1),
          ("otherLoop", 6),
          ("rdl", 4),
          ("rdlReset", 5))
    )


_GdcDsuChannelLoopbackConfig_Type.__name__ = "Integer32"
_GdcDsuChannelLoopbackConfig_Object = MibTableColumn
gdcDsuChannelLoopbackConfig = _GdcDsuChannelLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 4, 1, 4),
    _GdcDsuChannelLoopbackConfig_Type()
)
gdcDsuChannelLoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsuChannelLoopbackConfig.setStatus("mandatory")


class _GdcDsuChannelTestDuration_Type(Integer32):
    """Custom type gdcDsuChannelTestDuration based on Integer32"""
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
        *(("noLimit", 1),
          ("testTime10Mins", 11),
          ("testTime15Mins", 12),
          ("testTime1Min", 2),
          ("testTime20Mins", 13),
          ("testTime25Mins", 14),
          ("testTime2Mins", 3),
          ("testTime30Mins", 15),
          ("testTime30Secs", 16),
          ("testTime3Mins", 4),
          ("testTime4Mins", 5),
          ("testTime5Mins", 6),
          ("testTime6Mins", 7),
          ("testTime7Mins", 8),
          ("testTime8Mins", 9),
          ("testTime9Mins", 10))
    )


_GdcDsuChannelTestDuration_Type.__name__ = "Integer32"
_GdcDsuChannelTestDuration_Object = MibTableColumn
gdcDsuChannelTestDuration = _GdcDsuChannelTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 4, 1, 5),
    _GdcDsuChannelTestDuration_Type()
)
gdcDsuChannelTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsuChannelTestDuration.setStatus("mandatory")


class _GdcDsuChannelDiagTimingSource_Type(Integer32):
    """Custom type gdcDsuChannelDiagTimingSource based on Integer32"""
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
        *(("composite", 5),
          ("currentSource", 1),
          ("localTiming", 3),
          ("loopTiming", 2),
          ("station", 4))
    )


_GdcDsuChannelDiagTimingSource_Type.__name__ = "Integer32"
_GdcDsuChannelDiagTimingSource_Object = MibTableColumn
gdcDsuChannelDiagTimingSource = _GdcDsuChannelDiagTimingSource_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 4, 1, 6),
    _GdcDsuChannelDiagTimingSource_Type()
)
gdcDsuChannelDiagTimingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsuChannelDiagTimingSource.setStatus("mandatory")


class _GdcDsuChannelTestStatus_Type(Integer32):
    """Custom type gdcDsuChannelTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notInTest", 1),
          ("testCompleted", 4),
          ("testCompletedNotInTest", 5),
          ("testInProgress", 2))
    )


_GdcDsuChannelTestStatus_Type.__name__ = "Integer32"
_GdcDsuChannelTestStatus_Object = MibTableColumn
gdcDsuChannelTestStatus = _GdcDsuChannelTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 4, 1, 7),
    _GdcDsuChannelTestStatus_Type()
)
gdcDsuChannelTestStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gdcDsuChannelTestStatus.setStatus("mandatory")


class _GdcDsuChannelTestExceptions_Type(Integer32):
    """Custom type gdcDsuChannelTestExceptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_GdcDsuChannelTestExceptions_Type.__name__ = "Integer32"
_GdcDsuChannelTestExceptions_Object = MibTableColumn
gdcDsuChannelTestExceptions = _GdcDsuChannelTestExceptions_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 4, 1, 8),
    _GdcDsuChannelTestExceptions_Type()
)
gdcDsuChannelTestExceptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsuChannelTestExceptions.setStatus("mandatory")
_GdcDsuChannelTestResults_Type = Integer32
_GdcDsuChannelTestResults_Object = MibTableColumn
gdcDsuChannelTestResults = _GdcDsuChannelTestResults_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 4, 1, 9),
    _GdcDsuChannelTestResults_Type()
)
gdcDsuChannelTestResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsuChannelTestResults.setStatus("mandatory")


class _GdcDsuSystemMIBversion_Type(DisplayString):
    """Custom type gdcDsuSystemMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_GdcDsuSystemMIBversion_Type.__name__ = "DisplayString"
_GdcDsuSystemMIBversion_Object = MibScalar
gdcDsuSystemMIBversion = _GdcDsuSystemMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 5, 5),
    _GdcDsuSystemMIBversion_Type()
)
gdcDsuSystemMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdcDsuSystemMIBversion.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GDC-DSU-MGMT-MIB",
    **{"gdc": gdc,
       "dsu": dsu,
       "t1": t1,
       "gdcDsuDS0AllocationSchemeTable": gdcDsuDS0AllocationSchemeTable,
       "gdcDsuDS0AllocationSchemeEntry": gdcDsuDS0AllocationSchemeEntry,
       "gdcDsuDS0AllocationIndex": gdcDsuDS0AllocationIndex,
       "gdcDsuDS0AllocationScheme": gdcDsuDS0AllocationScheme,
       "gdcDsuChannelConfigTable": gdcDsuChannelConfigTable,
       "gdcDsuChannelConfigEntry": gdcDsuChannelConfigEntry,
       "gdcDsuChannelConfigIndex": gdcDsuChannelConfigIndex,
       "gdcDsuChannelBaseRate": gdcDsuChannelBaseRate,
       "gdcDsuChannelStartingDS0": gdcDsuChannelStartingDS0,
       "gdcDsuChannelNumberOfDS0s": gdcDsuChannelNumberOfDS0s,
       "gdcDsuChannelSplitTiming": gdcDsuChannelSplitTiming,
       "gdcDsuChannelChannelType": gdcDsuChannelChannelType,
       "gdcDsuChannelTransmitClockInvert": gdcDsuChannelTransmitClockInvert,
       "gdcDsuChannelReceiveClockInvert": gdcDsuChannelReceiveClockInvert,
       "gdcDsuChannelTransmitDataInvert": gdcDsuChannelTransmitDataInvert,
       "gdcDsuChannelReceiveDataInvert": gdcDsuChannelReceiveDataInvert,
       "gdcDsuChannelLocalDCD": gdcDsuChannelLocalDCD,
       "gdcDsuChannelLocalDSR": gdcDsuChannelLocalDSR,
       "gdcDsuChannelReceiveControl": gdcDsuChannelReceiveControl,
       "gdcDsuChannelTransmitControl": gdcDsuChannelTransmitControl,
       "gdcDsuChannelRTSCTScontrol": gdcDsuChannelRTSCTScontrol,
       "gdcDsuChannelEIAtestLeads": gdcDsuChannelEIAtestLeads,
       "gdcDsuChannelDccMode": gdcDsuChannelDccMode,
       "gdcDsuChannelInbandLoop": gdcDsuChannelInbandLoop,
       "gdcDsuChannelInbandLoopCode": gdcDsuChannelInbandLoopCode,
       "gdcDsuChannelInbandLoopdown": gdcDsuChannelInbandLoopdown,
       "gdcDsuChannelTransmitClockSource": gdcDsuChannelTransmitClockSource,
       "gdcDsuChannelFallbackClockSource": gdcDsuChannelFallbackClockSource,
       "gdcDsuChannelControlModeIdle": gdcDsuChannelControlModeIdle,
       "gdcDsuChannelSignalStatusTable": gdcDsuChannelSignalStatusTable,
       "gdcDsuChannelSignalStatusEntry": gdcDsuChannelSignalStatusEntry,
       "gdcDsuChannelSignalStatusIndex": gdcDsuChannelSignalStatusIndex,
       "gdcDsuChannelCTSstatus": gdcDsuChannelCTSstatus,
       "gdcDsuChannelRTSstatus": gdcDsuChannelRTSstatus,
       "gdcDsuChannelDTRstatus": gdcDsuChannelDTRstatus,
       "gdcDsuChannelDSRstatus": gdcDsuChannelDSRstatus,
       "gdcDsuChannelDCDstatus": gdcDsuChannelDCDstatus,
       "gdcDsuChannelRXCstatus": gdcDsuChannelRXCstatus,
       "gdcDsuChannelTXCstatus": gdcDsuChannelTXCstatus,
       "gdcDsuChannelRXDstatus": gdcDsuChannelRXDstatus,
       "gdcDsuChannelTXDstatus": gdcDsuChannelTXDstatus,
       "gdcDsuChannelDiagTable": gdcDsuChannelDiagTable,
       "gdcDsuChannelDiagEntry": gdcDsuChannelDiagEntry,
       "gdcDsuChannelDiagIndex": gdcDsuChannelDiagIndex,
       "gdcDsuChannelDiagSendCode": gdcDsuChannelDiagSendCode,
       "gdcDsuChannelDiagProgPattern": gdcDsuChannelDiagProgPattern,
       "gdcDsuChannelLoopbackConfig": gdcDsuChannelLoopbackConfig,
       "gdcDsuChannelTestDuration": gdcDsuChannelTestDuration,
       "gdcDsuChannelDiagTimingSource": gdcDsuChannelDiagTimingSource,
       "gdcDsuChannelTestStatus": gdcDsuChannelTestStatus,
       "gdcDsuChannelTestExceptions": gdcDsuChannelTestExceptions,
       "gdcDsuChannelTestResults": gdcDsuChannelTestResults,
       "gdcDsuSystemMIBversion": gdcDsuSystemMIBversion}
)
