# SNMP MIB module (SAT-MEGA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SAT-MEGA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:43 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sat_ObjectIdentity = ObjectIdentity
sat = _Sat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038)
)
_Mega_ObjectIdentity = ObjectIdentity
mega = _Mega_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 4)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 4, 1)
)
_MegaPAC_E_cpu_C_ObjectIdentity = ObjectIdentity
megaPAC_E_cpu_C = _MegaPAC_E_cpu_C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 4, 1, 1)
)
_MegaPAC_ESL_ObjectIdentity = ObjectIdentity
megaPAC_ESL = _MegaPAC_ESL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 4, 1, 2)
)
_MegaPAC_E_cpu_D_E_ObjectIdentity = ObjectIdentity
megaPAC_E_cpu_D_E = _MegaPAC_E_cpu_D_E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 4, 1, 3)
)
_MegaPAC_V_cpu_8_ObjectIdentity = ObjectIdentity
megaPAC_V_cpu_8 = _MegaPAC_V_cpu_8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 4, 1, 4)
)
_MegaPAC_V_cpu_16_ObjectIdentity = ObjectIdentity
megaPAC_V_cpu_16 = _MegaPAC_V_cpu_16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 4, 1, 5)
)
_MegaPAC_V_cpu_68040_ObjectIdentity = ObjectIdentity
megaPAC_V_cpu_68040 = _MegaPAC_V_cpu_68040_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 4, 1, 6)
)
_MegaPAC_V_cpu_68060_ObjectIdentity = ObjectIdentity
megaPAC_V_cpu_68060 = _MegaPAC_V_cpu_68060_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 4, 1, 7)
)
_Base_ObjectIdentity = ObjectIdentity
base = _Base_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2)
)


class _BaseVersion_Type(DisplayString):
    """Custom type baseVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BaseVersion_Type.__name__ = "DisplayString"
_BaseVersion_Object = MibScalar
baseVersion = _BaseVersion_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 1),
    _BaseVersion_Type()
)
baseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseVersion.setStatus("mandatory")


class _BaseRestartTime_Type(DisplayString):
    """Custom type baseRestartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_BaseRestartTime_Type.__name__ = "DisplayString"
_BaseRestartTime_Object = MibScalar
baseRestartTime = _BaseRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 2),
    _BaseRestartTime_Type()
)
baseRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseRestartTime.setStatus("mandatory")
_BaseMaxPacketSize_Type = Integer32
_BaseMaxPacketSize_Object = MibScalar
baseMaxPacketSize = _BaseMaxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 3),
    _BaseMaxPacketSize_Type()
)
baseMaxPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseMaxPacketSize.setStatus("mandatory")
_BaseBuffPoolMax_Type = Integer32
_BaseBuffPoolMax_Object = MibScalar
baseBuffPoolMax = _BaseBuffPoolMax_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 4),
    _BaseBuffPoolMax_Type()
)
baseBuffPoolMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseBuffPoolMax.setStatus("mandatory")
_BaseBuffPoolNow_Type = Integer32
_BaseBuffPoolNow_Object = MibScalar
baseBuffPoolNow = _BaseBuffPoolNow_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 5),
    _BaseBuffPoolNow_Type()
)
baseBuffPoolNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseBuffPoolNow.setStatus("mandatory")
_BaseBufferPoolLowest_Type = Integer32
_BaseBufferPoolLowest_Object = MibScalar
baseBufferPoolLowest = _BaseBufferPoolLowest_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 6),
    _BaseBufferPoolLowest_Type()
)
baseBufferPoolLowest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseBufferPoolLowest.setStatus("mandatory")
_BaseBufferPoolEmpty_Type = Integer32
_BaseBufferPoolEmpty_Object = MibScalar
baseBufferPoolEmpty = _BaseBufferPoolEmpty_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 7),
    _BaseBufferPoolEmpty_Type()
)
baseBufferPoolEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseBufferPoolEmpty.setStatus("mandatory")


class _BaseStatBufferThreshold_Type(Integer32):
    """Custom type baseStatBufferThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 1000),
    )


_BaseStatBufferThreshold_Type.__name__ = "Integer32"
_BaseStatBufferThreshold_Object = MibScalar
baseStatBufferThreshold = _BaseStatBufferThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 8),
    _BaseStatBufferThreshold_Type()
)
baseStatBufferThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseStatBufferThreshold.setStatus("mandatory")
_BaseMemorySize_Type = Integer32
_BaseMemorySize_Object = MibScalar
baseMemorySize = _BaseMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 9),
    _BaseMemorySize_Type()
)
baseMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseMemorySize.setStatus("mandatory")
_BaseDataFramesIn_Type = Counter32
_BaseDataFramesIn_Object = MibScalar
baseDataFramesIn = _BaseDataFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 10),
    _BaseDataFramesIn_Type()
)
baseDataFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseDataFramesIn.setStatus("mandatory")
_BaseDataFramesOut_Type = Counter32
_BaseDataFramesOut_Object = MibScalar
baseDataFramesOut = _BaseDataFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 11),
    _BaseDataFramesOut_Type()
)
baseDataFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseDataFramesOut.setStatus("mandatory")
_BaseDataFrameRateIn_Type = Counter32
_BaseDataFrameRateIn_Object = MibScalar
baseDataFrameRateIn = _BaseDataFrameRateIn_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 12),
    _BaseDataFrameRateIn_Type()
)
baseDataFrameRateIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseDataFrameRateIn.setStatus("mandatory")
_BaseDataFrameRateOut_Type = Counter32
_BaseDataFrameRateOut_Object = MibScalar
baseDataFrameRateOut = _BaseDataFrameRateOut_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 13),
    _BaseDataFrameRateOut_Type()
)
baseDataFrameRateOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseDataFrameRateOut.setStatus("mandatory")
_BaseTotalCallSetUps_Type = Counter32
_BaseTotalCallSetUps_Object = MibScalar
baseTotalCallSetUps = _BaseTotalCallSetUps_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 14),
    _BaseTotalCallSetUps_Type()
)
baseTotalCallSetUps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseTotalCallSetUps.setStatus("mandatory")
_BaseCurrentCalls_Type = Counter32
_BaseCurrentCalls_Object = MibScalar
baseCurrentCalls = _BaseCurrentCalls_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 15),
    _BaseCurrentCalls_Type()
)
baseCurrentCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseCurrentCalls.setStatus("mandatory")
_BaseRetransmissions_Type = Counter32
_BaseRetransmissions_Object = MibScalar
baseRetransmissions = _BaseRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 16),
    _BaseRetransmissions_Type()
)
baseRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseRetransmissions.setStatus("mandatory")
_BaseRejects_Type = Counter32
_BaseRejects_Object = MibScalar
baseRejects = _BaseRejects_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 17),
    _BaseRejects_Type()
)
baseRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseRejects.setStatus("mandatory")
_BaseTotalTransportCalls_Type = Counter32
_BaseTotalTransportCalls_Object = MibScalar
baseTotalTransportCalls = _BaseTotalTransportCalls_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 18),
    _BaseTotalTransportCalls_Type()
)
baseTotalTransportCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseTotalTransportCalls.setStatus("mandatory")
_BaseCurrentTransportCalls_Type = Counter32
_BaseCurrentTransportCalls_Object = MibScalar
baseCurrentTransportCalls = _BaseCurrentTransportCalls_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 19),
    _BaseCurrentTransportCalls_Type()
)
baseCurrentTransportCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseCurrentTransportCalls.setStatus("mandatory")


class _BaseRunStatus_Type(Integer32):
    """Custom type baseRunStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("prom", 1),
          ("ram", 2))
    )


_BaseRunStatus_Type.__name__ = "Integer32"
_BaseRunStatus_Object = MibScalar
baseRunStatus = _BaseRunStatus_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 20),
    _BaseRunStatus_Type()
)
baseRunStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseRunStatus.setStatus("mandatory")


class _BaseReports_Type(DisplayString):
    """Custom type baseReports based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BaseReports_Type.__name__ = "DisplayString"
_BaseReports_Object = MibScalar
baseReports = _BaseReports_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 21),
    _BaseReports_Type()
)
baseReports.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baseReports.setStatus("mandatory")


class _BaseSessionStatistics_Type(DisplayString):
    """Custom type baseSessionStatistics based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BaseSessionStatistics_Type.__name__ = "DisplayString"
_BaseSessionStatistics_Object = MibScalar
baseSessionStatistics = _BaseSessionStatistics_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 22),
    _BaseSessionStatistics_Type()
)
baseSessionStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baseSessionStatistics.setStatus("mandatory")


class _BaseBufferThreshold_Type(Integer32):
    """Custom type baseBufferThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 1000),
    )


_BaseBufferThreshold_Type.__name__ = "Integer32"
_BaseBufferThreshold_Object = MibScalar
baseBufferThreshold = _BaseBufferThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 23),
    _BaseBufferThreshold_Type()
)
baseBufferThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baseBufferThreshold.setStatus("mandatory")


class _BaseInitialPresentationTimer_Type(Integer32):
    """Custom type baseInitialPresentationTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_BaseInitialPresentationTimer_Type.__name__ = "Integer32"
_BaseInitialPresentationTimer_Object = MibScalar
baseInitialPresentationTimer = _BaseInitialPresentationTimer_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 24),
    _BaseInitialPresentationTimer_Type()
)
baseInitialPresentationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baseInitialPresentationTimer.setStatus("mandatory")


class _BaseSecondaryPresentationTimer_Type(Integer32):
    """Custom type baseSecondaryPresentationTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_BaseSecondaryPresentationTimer_Type.__name__ = "Integer32"
_BaseSecondaryPresentationTimer_Object = MibScalar
baseSecondaryPresentationTimer = _BaseSecondaryPresentationTimer_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 25),
    _BaseSecondaryPresentationTimer_Type()
)
baseSecondaryPresentationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baseSecondaryPresentationTimer.setStatus("mandatory")


class _BaseInactivityDetectTimer_Type(Integer32):
    """Custom type baseInactivityDetectTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_BaseInactivityDetectTimer_Type.__name__ = "Integer32"
_BaseInactivityDetectTimer_Object = MibScalar
baseInactivityDetectTimer = _BaseInactivityDetectTimer_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 26),
    _BaseInactivityDetectTimer_Type()
)
baseInactivityDetectTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baseInactivityDetectTimer.setStatus("mandatory")


class _BaseSegmentAccounting_Type(Integer32):
    """Custom type baseSegmentAccounting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BaseSegmentAccounting_Type.__name__ = "Integer32"
_BaseSegmentAccounting_Object = MibScalar
baseSegmentAccounting = _BaseSegmentAccounting_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 27),
    _BaseSegmentAccounting_Type()
)
baseSegmentAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baseSegmentAccounting.setStatus("mandatory")


class _BaseTerminalEmulationBuffers_Type(Integer32):
    """Custom type baseTerminalEmulationBuffers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 640),
    )


_BaseTerminalEmulationBuffers_Type.__name__ = "Integer32"
_BaseTerminalEmulationBuffers_Object = MibScalar
baseTerminalEmulationBuffers = _BaseTerminalEmulationBuffers_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 28),
    _BaseTerminalEmulationBuffers_Type()
)
baseTerminalEmulationBuffers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baseTerminalEmulationBuffers.setStatus("mandatory")


class _BaseTransportBuffers_Type(Integer32):
    """Custom type baseTransportBuffers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_BaseTransportBuffers_Type.__name__ = "Integer32"
_BaseTransportBuffers_Object = MibScalar
baseTransportBuffers = _BaseTransportBuffers_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 29),
    _BaseTransportBuffers_Type()
)
baseTransportBuffers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baseTransportBuffers.setStatus("mandatory")


class _BaseCountrySettings_Type(Integer32):
    """Custom type baseCountrySettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("japn", 2),
          ("none", 1))
    )


_BaseCountrySettings_Type.__name__ = "Integer32"
_BaseCountrySettings_Object = MibScalar
baseCountrySettings = _BaseCountrySettings_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 30),
    _BaseCountrySettings_Type()
)
baseCountrySettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baseCountrySettings.setStatus("mandatory")


class _BaseTeleloadEnabled_Type(Integer32):
    """Custom type baseTeleloadEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              129)
        )
    )
    namedValues = NamedValues(
        *(("k160", 129),
          ("k256", 3),
          ("no", 1),
          ("yes", 2))
    )


_BaseTeleloadEnabled_Type.__name__ = "Integer32"
_BaseTeleloadEnabled_Object = MibScalar
baseTeleloadEnabled = _BaseTeleloadEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 31),
    _BaseTeleloadEnabled_Type()
)
baseTeleloadEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baseTeleloadEnabled.setStatus("mandatory")


class _BaseDefaultToPromCompatible_Type(Integer32):
    """Custom type baseDefaultToPromCompatible based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_BaseDefaultToPromCompatible_Type.__name__ = "Integer32"
_BaseDefaultToPromCompatible_Object = MibScalar
baseDefaultToPromCompatible = _BaseDefaultToPromCompatible_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 2, 32),
    _BaseDefaultToPromCompatible_Type()
)
baseDefaultToPromCompatible.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baseDefaultToPromCompatible.setStatus("mandatory")
_Controller_ObjectIdentity = ObjectIdentity
controller = _Controller_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3)
)
_CtrlNumberConfigured_Type = Integer32
_CtrlNumberConfigured_Object = MibScalar
ctrlNumberConfigured = _CtrlNumberConfigured_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 1),
    _CtrlNumberConfigured_Type()
)
ctrlNumberConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlNumberConfigured.setStatus("mandatory")
_CtrlTotalNumber_Type = Integer32
_CtrlTotalNumber_Object = MibScalar
ctrlTotalNumber = _CtrlTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 2),
    _CtrlTotalNumber_Type()
)
ctrlTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlTotalNumber.setStatus("mandatory")
_CtrlStatTable_Object = MibTable
ctrlStatTable = _CtrlStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3)
)
if mibBuilder.loadTexts:
    ctrlStatTable.setStatus("mandatory")
_CtrlStatEntry_Object = MibTableRow
ctrlStatEntry = _CtrlStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1)
)
ctrlStatEntry.setIndexNames(
    (0, "SAT-MEGA-MIB", "ctrlStatIndex"),
)
if mibBuilder.loadTexts:
    ctrlStatEntry.setStatus("mandatory")
_CtrlStatIndex_Type = Integer32
_CtrlStatIndex_Object = MibTableColumn
ctrlStatIndex = _CtrlStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 1),
    _CtrlStatIndex_Type()
)
ctrlStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatIndex.setStatus("mandatory")


class _CtrlStatName_Type(DisplayString):
    """Custom type ctrlStatName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CtrlStatName_Type.__name__ = "DisplayString"
_CtrlStatName_Object = MibTableColumn
ctrlStatName = _CtrlStatName_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 2),
    _CtrlStatName_Type()
)
ctrlStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatName.setStatus("mandatory")


class _CtrlStatType_Type(Integer32):
    """Custom type ctrlStatType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
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
              34,
              35,
              36,
              37,
              38,
              39)
        )
    )
    namedValues = NamedValues(
        *(("clus", 14),
          ("cons", 20),
          ("dlc", 22),
          ("dlcx", 38),
          ("edlc", 39),
          ("epci", 4),
          ("esis", 34),
          ("hdlc", 8),
          ("ilan", 11),
          ("ip", 17),
          ("ipx", 31),
          ("lan", 13),
          ("map", 23),
          ("mult", 15),
          ("mux", 2),
          ("nfrm", 26),
          ("nmsc", 21),
          ("null", 3),
          ("ppp", 30),
          ("qllc", 9),
          ("rout", 29),
          ("sdlc", 16),
          ("smdx", 37),
          ("snmp", 25),
          ("sru", 18),
          ("term", 12),
          ("tesis", 35),
          ("tip", 28),
          ("tipx", 32),
          ("tlan", 24),
          ("v25b", 19),
          ("vfrm", 36),
          ("x25", 1),
          ("xfrm", 27),
          ("xlan", 10))
    )


_CtrlStatType_Type.__name__ = "Integer32"
_CtrlStatType_Object = MibTableColumn
ctrlStatType = _CtrlStatType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 3),
    _CtrlStatType_Type()
)
ctrlStatType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatType.setStatus("mandatory")


class _CtrlStatSubType_Type(Integer32):
    """Custom type ctrlStatSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              17,
              33)
        )
    )
    namedValues = NamedValues(
        *(("generic", 5),
          ("none", 1),
          ("scc", 17),
          ("sio", 2),
          ("vio", 33),
          ("xio", 3),
          ("xio-sio", 4))
    )


_CtrlStatSubType_Type.__name__ = "Integer32"
_CtrlStatSubType_Object = MibTableColumn
ctrlStatSubType = _CtrlStatSubType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 4),
    _CtrlStatSubType_Type()
)
ctrlStatSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatSubType.setStatus("mandatory")
_CtrlStatNumberChannels_Type = Integer32
_CtrlStatNumberChannels_Object = MibTableColumn
ctrlStatNumberChannels = _CtrlStatNumberChannels_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 5),
    _CtrlStatNumberChannels_Type()
)
ctrlStatNumberChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatNumberChannels.setStatus("mandatory")
_CtrlStatFirstChannelIndex_Type = Integer32
_CtrlStatFirstChannelIndex_Object = MibTableColumn
ctrlStatFirstChannelIndex = _CtrlStatFirstChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 6),
    _CtrlStatFirstChannelIndex_Type()
)
ctrlStatFirstChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatFirstChannelIndex.setStatus("mandatory")
_CtrlStatCRCErrors_Type = Counter32
_CtrlStatCRCErrors_Object = MibTableColumn
ctrlStatCRCErrors = _CtrlStatCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 7),
    _CtrlStatCRCErrors_Type()
)
ctrlStatCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatCRCErrors.setStatus("mandatory")
_CtrlStatTotalCallSetUps_Type = Counter32
_CtrlStatTotalCallSetUps_Object = MibTableColumn
ctrlStatTotalCallSetUps = _CtrlStatTotalCallSetUps_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 8),
    _CtrlStatTotalCallSetUps_Type()
)
ctrlStatTotalCallSetUps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatTotalCallSetUps.setStatus("mandatory")
_CtrlStatCurrentCalls_Type = Integer32
_CtrlStatCurrentCalls_Object = MibTableColumn
ctrlStatCurrentCalls = _CtrlStatCurrentCalls_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 9),
    _CtrlStatCurrentCalls_Type()
)
ctrlStatCurrentCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatCurrentCalls.setStatus("mandatory")
_CtrlStatDataIn_Type = Counter32
_CtrlStatDataIn_Object = MibTableColumn
ctrlStatDataIn = _CtrlStatDataIn_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 10),
    _CtrlStatDataIn_Type()
)
ctrlStatDataIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatDataIn.setStatus("mandatory")
_CtrlStatDataOut_Type = Counter32
_CtrlStatDataOut_Object = MibTableColumn
ctrlStatDataOut = _CtrlStatDataOut_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 11),
    _CtrlStatDataOut_Type()
)
ctrlStatDataOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatDataOut.setStatus("mandatory")
_CtrlStatDataFramesIn_Type = Counter32
_CtrlStatDataFramesIn_Object = MibTableColumn
ctrlStatDataFramesIn = _CtrlStatDataFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 12),
    _CtrlStatDataFramesIn_Type()
)
ctrlStatDataFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatDataFramesIn.setStatus("mandatory")
_CtrlStatDataFramesOut_Type = Counter32
_CtrlStatDataFramesOut_Object = MibTableColumn
ctrlStatDataFramesOut = _CtrlStatDataFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 13),
    _CtrlStatDataFramesOut_Type()
)
ctrlStatDataFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatDataFramesOut.setStatus("mandatory")
_CtrlStatDataFrameRateIn_Type = Integer32
_CtrlStatDataFrameRateIn_Object = MibTableColumn
ctrlStatDataFrameRateIn = _CtrlStatDataFrameRateIn_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 14),
    _CtrlStatDataFrameRateIn_Type()
)
ctrlStatDataFrameRateIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatDataFrameRateIn.setStatus("mandatory")
_CtrlStatDataFrameRateOut_Type = Integer32
_CtrlStatDataFrameRateOut_Object = MibTableColumn
ctrlStatDataFrameRateOut = _CtrlStatDataFrameRateOut_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 15),
    _CtrlStatDataFrameRateOut_Type()
)
ctrlStatDataFrameRateOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatDataFrameRateOut.setStatus("mandatory")
_CtrlStatCallsReceived_Type = Counter32
_CtrlStatCallsReceived_Object = MibTableColumn
ctrlStatCallsReceived = _CtrlStatCallsReceived_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 16),
    _CtrlStatCallsReceived_Type()
)
ctrlStatCallsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatCallsReceived.setStatus("mandatory")
_CtrlStatCallsSent_Type = Counter32
_CtrlStatCallsSent_Object = MibTableColumn
ctrlStatCallsSent = _CtrlStatCallsSent_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 17),
    _CtrlStatCallsSent_Type()
)
ctrlStatCallsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatCallsSent.setStatus("mandatory")
_CtrlStatClearsReceived_Type = Counter32
_CtrlStatClearsReceived_Object = MibTableColumn
ctrlStatClearsReceived = _CtrlStatClearsReceived_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 18),
    _CtrlStatClearsReceived_Type()
)
ctrlStatClearsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatClearsReceived.setStatus("mandatory")
_CtrlStatRetransmissions_Type = Counter32
_CtrlStatRetransmissions_Object = MibTableColumn
ctrlStatRetransmissions = _CtrlStatRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 19),
    _CtrlStatRetransmissions_Type()
)
ctrlStatRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatRetransmissions.setStatus("mandatory")
_CtrlStatRejects_Type = Counter32
_CtrlStatRejects_Object = MibTableColumn
ctrlStatRejects = _CtrlStatRejects_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 20),
    _CtrlStatRejects_Type()
)
ctrlStatRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatRejects.setStatus("mandatory")


class _CtrlStatState_Type(Integer32):
    """Custom type ctrlStatState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              9,
              11,
              13,
              15,
              17,
              19,
              21,
              23,
              25)
        )
    )
    namedValues = NamedValues(
        *(("blkd", 13),
          ("cls", 17),
          ("data", 11),
          ("disc", 1),
          ("frmr", 19),
          ("sabm", 9),
          ("stop", 21),
          ("wake", 15),
          ("xidc", 25),
          ("xidr", 23))
    )


_CtrlStatState_Type.__name__ = "Integer32"
_CtrlStatState_Object = MibTableColumn
ctrlStatState = _CtrlStatState_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 21),
    _CtrlStatState_Type()
)
ctrlStatState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatState.setStatus("mandatory")


class _CtrlStatSubState_Type(Integer32):
    """Custom type ctrlStatSubState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1,
              3,
              5,
              9,
              129)
        )
    )
    namedValues = NamedValues(
        *(("actv", 3),
          ("disc", 9),
          ("idle", 1),
          ("new", 129),
          ("norm", 1),
          ("rej", 5))
    )


_CtrlStatSubState_Type.__name__ = "Integer32"
_CtrlStatSubState_Object = MibTableColumn
ctrlStatSubState = _CtrlStatSubState_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 22),
    _CtrlStatSubState_Type()
)
ctrlStatSubState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatSubState.setStatus("mandatory")
_CtrlStatNoTries_Type = Counter32
_CtrlStatNoTries_Object = MibTableColumn
ctrlStatNoTries = _CtrlStatNoTries_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 23),
    _CtrlStatNoTries_Type()
)
ctrlStatNoTries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatNoTries.setStatus("mandatory")


class _CtrlStatOptions_Type(Integer32):
    """Custom type ctrlStatOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              9,
              17,
              257,
              513,
              1025,
              2049,
              4097,
              8193,
              16385,
              32769,
              40961)
        )
    )
    namedValues = NamedValues(
        *(("dcd", 513),
          ("dmod", 1025),
          ("dtr", 2),
          ("ext", 8193),
          ("hold", 4097),
          ("iso1984", 16385),
          ("net", 257),
          ("none", 1),
          ("poll", 32769),
          ("poll-ext", 40961),
          ("stat", 2049),
          ("test", 3),
          ("ui", 17),
          ("xidc", 5),
          ("xidr", 9))
    )


_CtrlStatOptions_Type.__name__ = "Integer32"
_CtrlStatOptions_Object = MibTableColumn
ctrlStatOptions = _CtrlStatOptions_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 24),
    _CtrlStatOptions_Type()
)
ctrlStatOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatOptions.setStatus("mandatory")
_CtrlStatLCGN_Type = Integer32
_CtrlStatLCGN_Object = MibTableColumn
ctrlStatLCGN = _CtrlStatLCGN_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 25),
    _CtrlStatLCGN_Type()
)
ctrlStatLCGN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatLCGN.setStatus("mandatory")
_CtrlStatResetsReceived_Type = Counter32
_CtrlStatResetsReceived_Object = MibTableColumn
ctrlStatResetsReceived = _CtrlStatResetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 26),
    _CtrlStatResetsReceived_Type()
)
ctrlStatResetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatResetsReceived.setStatus("mandatory")
_CtrlStatInterruptsReceived_Type = Counter32
_CtrlStatInterruptsReceived_Object = MibTableColumn
ctrlStatInterruptsReceived = _CtrlStatInterruptsReceived_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 27),
    _CtrlStatInterruptsReceived_Type()
)
ctrlStatInterruptsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatInterruptsReceived.setStatus("mandatory")
_CtrlStatOutputQueueLength_Type = Integer32
_CtrlStatOutputQueueLength_Object = MibTableColumn
ctrlStatOutputQueueLength = _CtrlStatOutputQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 28),
    _CtrlStatOutputQueueLength_Type()
)
ctrlStatOutputQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatOutputQueueLength.setStatus("mandatory")


class _CtrlStatStationAddress_Type(DisplayString):
    """Custom type ctrlStatStationAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_CtrlStatStationAddress_Type.__name__ = "DisplayString"
_CtrlStatStationAddress_Object = MibTableColumn
ctrlStatStationAddress = _CtrlStatStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 29),
    _CtrlStatStationAddress_Type()
)
ctrlStatStationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatStationAddress.setStatus("mandatory")


class _CtrlStatDestinationAddress_Type(DisplayString):
    """Custom type ctrlStatDestinationAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_CtrlStatDestinationAddress_Type.__name__ = "DisplayString"
_CtrlStatDestinationAddress_Object = MibTableColumn
ctrlStatDestinationAddress = _CtrlStatDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 30),
    _CtrlStatDestinationAddress_Type()
)
ctrlStatDestinationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatDestinationAddress.setStatus("mandatory")


class _CtrlStatEIA_Type(DisplayString):
    """Custom type ctrlStatEIA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CtrlStatEIA_Type.__name__ = "DisplayString"
_CtrlStatEIA_Object = MibTableColumn
ctrlStatEIA = _CtrlStatEIA_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 31),
    _CtrlStatEIA_Type()
)
ctrlStatEIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatEIA.setStatus("mandatory")


class _CtrlStatSdlcOptions_Type(Integer32):
    """Custom type ctrlStatSdlcOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              17,
              33,
              65,
              129,
              193)
        )
    )
    namedValues = NamedValues(
        *(("idle", 17),
          ("none", 1),
          ("pu4", 33),
          ("wait", 65),
          ("wait-xid", 193),
          ("xid", 129))
    )


_CtrlStatSdlcOptions_Type.__name__ = "Integer32"
_CtrlStatSdlcOptions_Object = MibTableColumn
ctrlStatSdlcOptions = _CtrlStatSdlcOptions_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 32),
    _CtrlStatSdlcOptions_Type()
)
ctrlStatSdlcOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatSdlcOptions.setStatus("mandatory")
_CtrlStatArpRequestRec_Type = Integer32
_CtrlStatArpRequestRec_Object = MibTableColumn
ctrlStatArpRequestRec = _CtrlStatArpRequestRec_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 33),
    _CtrlStatArpRequestRec_Type()
)
ctrlStatArpRequestRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatArpRequestRec.setStatus("mandatory")
_CtrlStatArpRequestSent_Type = Integer32
_CtrlStatArpRequestSent_Object = MibTableColumn
ctrlStatArpRequestSent = _CtrlStatArpRequestSent_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 34),
    _CtrlStatArpRequestSent_Type()
)
ctrlStatArpRequestSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatArpRequestSent.setStatus("mandatory")
_CtrlStatArpResponsesRec_Type = Integer32
_CtrlStatArpResponsesRec_Object = MibTableColumn
ctrlStatArpResponsesRec = _CtrlStatArpResponsesRec_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 35),
    _CtrlStatArpResponsesRec_Type()
)
ctrlStatArpResponsesRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatArpResponsesRec.setStatus("mandatory")
_CtrlStatFRTxSeqLost_Type = Integer32
_CtrlStatFRTxSeqLost_Object = MibTableColumn
ctrlStatFRTxSeqLost = _CtrlStatFRTxSeqLost_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 36),
    _CtrlStatFRTxSeqLost_Type()
)
ctrlStatFRTxSeqLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatFRTxSeqLost.setStatus("mandatory")
_CtrlStatFRRxSeqLost_Type = Integer32
_CtrlStatFRRxSeqLost_Object = MibTableColumn
ctrlStatFRRxSeqLost = _CtrlStatFRRxSeqLost_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 37),
    _CtrlStatFRRxSeqLost_Type()
)
ctrlStatFRRxSeqLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatFRRxSeqLost.setStatus("mandatory")
_CtrlStatFRCurTxSeq_Type = Integer32
_CtrlStatFRCurTxSeq_Object = MibTableColumn
ctrlStatFRCurTxSeq = _CtrlStatFRCurTxSeq_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 38),
    _CtrlStatFRCurTxSeq_Type()
)
ctrlStatFRCurTxSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatFRCurTxSeq.setStatus("mandatory")
_CtrlStatFRCurRxSeq_Type = Integer32
_CtrlStatFRCurRxSeq_Object = MibTableColumn
ctrlStatFRCurRxSeq = _CtrlStatFRCurRxSeq_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 39),
    _CtrlStatFRCurRxSeq_Type()
)
ctrlStatFRCurRxSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatFRCurRxSeq.setStatus("mandatory")
_CtrlStatFRRcvBecn_Type = Integer32
_CtrlStatFRRcvBecn_Object = MibTableColumn
ctrlStatFRRcvBecn = _CtrlStatFRRcvBecn_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 40),
    _CtrlStatFRRcvBecn_Type()
)
ctrlStatFRRcvBecn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatFRRcvBecn.setStatus("mandatory")
_CtrlStatFRRcvFecn_Type = Integer32
_CtrlStatFRRcvFecn_Object = MibTableColumn
ctrlStatFRRcvFecn = _CtrlStatFRRcvFecn_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 41),
    _CtrlStatFRRcvFecn_Type()
)
ctrlStatFRRcvFecn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatFRRcvFecn.setStatus("mandatory")
_CtrlStatFRThroughput_Type = Integer32
_CtrlStatFRThroughput_Object = MibTableColumn
ctrlStatFRThroughput = _CtrlStatFRThroughput_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 42),
    _CtrlStatFRThroughput_Type()
)
ctrlStatFRThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatFRThroughput.setStatus("mandatory")


class _CtrlStatFRLMI_Type(Integer32):
    """Custom type ctrlStatFRLMI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 2))
    )


_CtrlStatFRLMI_Type.__name__ = "Integer32"
_CtrlStatFRLMI_Object = MibTableColumn
ctrlStatFRLMI = _CtrlStatFRLMI_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 43),
    _CtrlStatFRLMI_Type()
)
ctrlStatFRLMI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatFRLMI.setStatus("mandatory")
_CtrlStatFRrespLmi_Type = Integer32
_CtrlStatFRrespLmi_Object = MibTableColumn
ctrlStatFRrespLmi = _CtrlStatFRrespLmi_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 44),
    _CtrlStatFRrespLmi_Type()
)
ctrlStatFRrespLmi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatFRrespLmi.setStatus("mandatory")
_CtrlStatFRCurSndSeq_Type = Integer32
_CtrlStatFRCurSndSeq_Object = MibTableColumn
ctrlStatFRCurSndSeq = _CtrlStatFRCurSndSeq_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 45),
    _CtrlStatFRCurSndSeq_Type()
)
ctrlStatFRCurSndSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatFRCurSndSeq.setStatus("mandatory")
_CtrlStatFRCurRcvSeq_Type = Integer32
_CtrlStatFRCurRcvSeq_Object = MibTableColumn
ctrlStatFRCurRcvSeq = _CtrlStatFRCurRcvSeq_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 46),
    _CtrlStatFRCurRcvSeq_Type()
)
ctrlStatFRCurRcvSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatFRCurRcvSeq.setStatus("mandatory")
_CtrlStatFRRcvDe_Type = Integer32
_CtrlStatFRRcvDe_Object = MibTableColumn
ctrlStatFRRcvDe = _CtrlStatFRRcvDe_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 3, 1, 47),
    _CtrlStatFRRcvDe_Type()
)
ctrlStatFRRcvDe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlStatFRRcvDe.setStatus("mandatory")
_CtrlParamTable_Object = MibTable
ctrlParamTable = _CtrlParamTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4)
)
if mibBuilder.loadTexts:
    ctrlParamTable.setStatus("mandatory")
_CtrlParamEntry_Object = MibTableRow
ctrlParamEntry = _CtrlParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1)
)
ctrlParamEntry.setIndexNames(
    (0, "SAT-MEGA-MIB", "ctrlParamIndex"),
)
if mibBuilder.loadTexts:
    ctrlParamEntry.setStatus("mandatory")
_CtrlParamIndex_Type = Integer32
_CtrlParamIndex_Object = MibTableColumn
ctrlParamIndex = _CtrlParamIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 1),
    _CtrlParamIndex_Type()
)
ctrlParamIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlParamIndex.setStatus("mandatory")


class _CtrlParamName_Type(DisplayString):
    """Custom type ctrlParamName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CtrlParamName_Type.__name__ = "DisplayString"
_CtrlParamName_Object = MibTableColumn
ctrlParamName = _CtrlParamName_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 2),
    _CtrlParamName_Type()
)
ctrlParamName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamName.setStatus("mandatory")


class _CtrlParamType_Type(Integer32):
    """Custom type ctrlParamType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
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
              34,
              35,
              36,
              37,
              38,
              39)
        )
    )
    namedValues = NamedValues(
        *(("clus", 14),
          ("cons", 20),
          ("dlc", 22),
          ("dlcx", 38),
          ("edlc", 39),
          ("epci", 4),
          ("esis", 34),
          ("hdlc", 8),
          ("ilan", 11),
          ("ip", 17),
          ("ipx", 31),
          ("lan", 13),
          ("map", 23),
          ("mult", 15),
          ("mux", 2),
          ("nfrm", 26),
          ("nmsc", 21),
          ("null", 3),
          ("ppp", 30),
          ("qllc", 9),
          ("rout", 29),
          ("sdlc", 16),
          ("smdx", 37),
          ("snmp", 25),
          ("sru", 18),
          ("term", 12),
          ("tesis", 35),
          ("tip", 28),
          ("tipx", 32),
          ("tlan", 24),
          ("v25b", 19),
          ("vfrm", 36),
          ("x25", 1),
          ("xfrm", 27),
          ("xlan", 10))
    )


_CtrlParamType_Type.__name__ = "Integer32"
_CtrlParamType_Object = MibTableColumn
ctrlParamType = _CtrlParamType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 3),
    _CtrlParamType_Type()
)
ctrlParamType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamType.setStatus("mandatory")


class _CtrlParamSubType_Type(Integer32):
    """Custom type ctrlParamSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              17,
              33)
        )
    )
    namedValues = NamedValues(
        *(("generic", 5),
          ("none", 1),
          ("scc", 17),
          ("sio", 2),
          ("vio", 33),
          ("xio", 3),
          ("xio-sio", 4))
    )


_CtrlParamSubType_Type.__name__ = "Integer32"
_CtrlParamSubType_Object = MibTableColumn
ctrlParamSubType = _CtrlParamSubType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 4),
    _CtrlParamSubType_Type()
)
ctrlParamSubType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamSubType.setStatus("mandatory")


class _CtrlParamNoChannels_Type(Integer32):
    """Custom type ctrlParamNoChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_CtrlParamNoChannels_Type.__name__ = "Integer32"
_CtrlParamNoChannels_Object = MibTableColumn
ctrlParamNoChannels = _CtrlParamNoChannels_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 5),
    _CtrlParamNoChannels_Type()
)
ctrlParamNoChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamNoChannels.setStatus("mandatory")


class _CtrlParamSpeed_Type(Integer32):
    """Custom type ctrlParamSpeed based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("ext-clock", 1),
          ("none", 0),
          ("speed-12-75bps", 13),
          ("speed-1200bps", 4),
          ("speed-128kbps", 15),
          ("speed-1800bps", 5),
          ("speed-19200bps", 12),
          ("speed-1mbps", 18),
          ("speed-2000bps", 6),
          ("speed-2400bps", 7),
          ("speed-256kbps", 16),
          ("speed-2mbps", 19),
          ("speed-300bps", 2),
          ("speed-3600bps", 8),
          ("speed-4800bps", 9),
          ("speed-512kbps", 17),
          ("speed-600bps", 3),
          ("speed-64kbps", 14),
          ("speed-7200bps", 10),
          ("speed-9600bps", 11))
    )


_CtrlParamSpeed_Type.__name__ = "Integer32"
_CtrlParamSpeed_Object = MibTableColumn
ctrlParamSpeed = _CtrlParamSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 6),
    _CtrlParamSpeed_Type()
)
ctrlParamSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamSpeed.setStatus("mandatory")


class _CtrlParamInterfaceType_Type(Integer32):
    """Custom type ctrlParamInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v24", 1),
          ("v35", 3),
          ("x21", 2))
    )


_CtrlParamInterfaceType_Type.__name__ = "Integer32"
_CtrlParamInterfaceType_Object = MibTableColumn
ctrlParamInterfaceType = _CtrlParamInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 7),
    _CtrlParamInterfaceType_Type()
)
ctrlParamInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamInterfaceType.setStatus("mandatory")


class _CtrlParamPacketSize_Type(Integer32):
    """Custom type ctrlParamPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              9,
              17,
              33)
        )
    )
    namedValues = NamedValues(
        *(("bytes-1024", 33),
          ("bytes-128", 5),
          ("bytes-256", 9),
          ("bytes-32", 2),
          ("bytes-512", 17),
          ("bytes-64", 3),
          ("tran", 1))
    )


_CtrlParamPacketSize_Type.__name__ = "Integer32"
_CtrlParamPacketSize_Object = MibTableColumn
ctrlParamPacketSize = _CtrlParamPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 8),
    _CtrlParamPacketSize_Type()
)
ctrlParamPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamPacketSize.setStatus("mandatory")


class _CtrlParamV54Modem_Type(Integer32):
    """Custom type ctrlParamV54Modem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              61)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 61))
    )


_CtrlParamV54Modem_Type.__name__ = "Integer32"
_CtrlParamV54Modem_Object = MibTableColumn
ctrlParamV54Modem = _CtrlParamV54Modem_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 9),
    _CtrlParamV54Modem_Type()
)
ctrlParamV54Modem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamV54Modem.setStatus("mandatory")


class _CtrlParamAddress_Type(Integer32):
    """Custom type ctrlParamAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce-b", 2),
          ("dte-a", 1))
    )


_CtrlParamAddress_Type.__name__ = "Integer32"
_CtrlParamAddress_Object = MibTableColumn
ctrlParamAddress = _CtrlParamAddress_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 10),
    _CtrlParamAddress_Type()
)
ctrlParamAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamAddress.setStatus("mandatory")


class _CtrlParamOptions_Type(Integer32):
    """Custom type ctrlParamOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              9,
              17,
              257,
              513,
              1025,
              2049,
              4097,
              8193,
              16385,
              32769,
              33025,
              40961)
        )
    )
    namedValues = NamedValues(
        *(("dcd", 513),
          ("dmod", 1025),
          ("dtr", 2),
          ("ext", 8193),
          ("hold", 4097),
          ("iso1984", 16385),
          ("net", 257),
          ("none", 1),
          ("poll", 32769),
          ("poll-ext", 40961),
          ("poll-net", 33025),
          ("stat", 2049),
          ("test", 3),
          ("ui", 17),
          ("xidc", 5),
          ("xidr", 9))
    )


_CtrlParamOptions_Type.__name__ = "Integer32"
_CtrlParamOptions_Object = MibTableColumn
ctrlParamOptions = _CtrlParamOptions_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 11),
    _CtrlParamOptions_Type()
)
ctrlParamOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamOptions.setStatus("mandatory")


class _CtrlParamInitFrame_Type(Integer32):
    """Custom type ctrlParamInitFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              48,
              64,
              68,
              84)
        )
    )
    namedValues = NamedValues(
        *(("disc", 68),
          ("disc-pbit", 84),
          ("none", 1),
          ("sabm", 48),
          ("sabm-pbit", 64))
    )


_CtrlParamInitFrame_Type.__name__ = "Integer32"
_CtrlParamInitFrame_Object = MibTableColumn
ctrlParamInitFrame = _CtrlParamInitFrame_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 12),
    _CtrlParamInitFrame_Type()
)
ctrlParamInitFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamInitFrame.setStatus("mandatory")


class _CtrlParamT1_Type(Integer32):
    """Custom type ctrlParamT1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 80),
    )


_CtrlParamT1_Type.__name__ = "Integer32"
_CtrlParamT1_Object = MibTableColumn
ctrlParamT1 = _CtrlParamT1_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 13),
    _CtrlParamT1_Type()
)
ctrlParamT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamT1.setStatus("mandatory")


class _CtrlParamTries_Type(Integer32):
    """Custom type ctrlParamTries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 50),
    )


_CtrlParamTries_Type.__name__ = "Integer32"
_CtrlParamTries_Object = MibTableColumn
ctrlParamTries = _CtrlParamTries_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 14),
    _CtrlParamTries_Type()
)
ctrlParamTries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamTries.setStatus("mandatory")


class _CtrlParamKLevel2_Type(Integer32):
    """Custom type ctrlParamKLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_CtrlParamKLevel2_Type.__name__ = "Integer32"
_CtrlParamKLevel2_Object = MibTableColumn
ctrlParamKLevel2 = _CtrlParamKLevel2_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 15),
    _CtrlParamKLevel2_Type()
)
ctrlParamKLevel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamKLevel2.setStatus("mandatory")


class _CtrlParamKLevel3_Type(Integer32):
    """Custom type ctrlParamKLevel3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_CtrlParamKLevel3_Type.__name__ = "Integer32"
_CtrlParamKLevel3_Object = MibTableColumn
ctrlParamKLevel3 = _CtrlParamKLevel3_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 16),
    _CtrlParamKLevel3_Type()
)
ctrlParamKLevel3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamKLevel3.setStatus("mandatory")


class _CtrlParamLineGroup_Type(Integer32):
    """Custom type ctrlParamLineGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CtrlParamLineGroup_Type.__name__ = "Integer32"
_CtrlParamLineGroup_Object = MibTableColumn
ctrlParamLineGroup = _CtrlParamLineGroup_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 17),
    _CtrlParamLineGroup_Type()
)
ctrlParamLineGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamLineGroup.setStatus("mandatory")


class _CtrlParamLCGN_Type(Integer32):
    """Custom type ctrlParamLCGN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CtrlParamLCGN_Type.__name__ = "Integer32"
_CtrlParamLCGN_Object = MibTableColumn
ctrlParamLCGN = _CtrlParamLCGN_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 18),
    _CtrlParamLCGN_Type()
)
ctrlParamLCGN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamLCGN.setStatus("mandatory")


class _CtrlParamLCNOffset_Type(Integer32):
    """Custom type ctrlParamLCNOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CtrlParamLCNOffset_Type.__name__ = "Integer32"
_CtrlParamLCNOffset_Object = MibTableColumn
ctrlParamLCNOffset = _CtrlParamLCNOffset_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 19),
    _CtrlParamLCNOffset_Type()
)
ctrlParamLCNOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamLCNOffset.setStatus("mandatory")


class _CtrlParamAddressGroup_Type(Integer32):
    """Custom type ctrlParamAddressGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CtrlParamAddressGroup_Type.__name__ = "Integer32"
_CtrlParamAddressGroup_Object = MibTableColumn
ctrlParamAddressGroup = _CtrlParamAddressGroup_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 20),
    _CtrlParamAddressGroup_Type()
)
ctrlParamAddressGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamAddressGroup.setStatus("mandatory")


class _CtrlParamFrameSequence_Type(Integer32):
    """Custom type ctrlParamFrameSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              15)
        )
    )
    namedValues = NamedValues(
        *(("extended", 15),
          ("normal", 7))
    )


_CtrlParamFrameSequence_Type.__name__ = "Integer32"
_CtrlParamFrameSequence_Object = MibTableColumn
ctrlParamFrameSequence = _CtrlParamFrameSequence_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 21),
    _CtrlParamFrameSequence_Type()
)
ctrlParamFrameSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamFrameSequence.setStatus("mandatory")


class _CtrlParamCallTimeOut_Type(Integer32):
    """Custom type ctrlParamCallTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 200),
    )


_CtrlParamCallTimeOut_Type.__name__ = "Integer32"
_CtrlParamCallTimeOut_Object = MibTableColumn
ctrlParamCallTimeOut = _CtrlParamCallTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 22),
    _CtrlParamCallTimeOut_Type()
)
ctrlParamCallTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamCallTimeOut.setStatus("mandatory")


class _CtrlParamErrorThreshold_Type(Integer32):
    """Custom type ctrlParamErrorThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_CtrlParamErrorThreshold_Type.__name__ = "Integer32"
_CtrlParamErrorThreshold_Object = MibTableColumn
ctrlParamErrorThreshold = _CtrlParamErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 23),
    _CtrlParamErrorThreshold_Type()
)
ctrlParamErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamErrorThreshold.setStatus("mandatory")


class _CtrlParamLoopBarPriority_Type(Integer32):
    """Custom type ctrlParamLoopBarPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CtrlParamLoopBarPriority_Type.__name__ = "Integer32"
_CtrlParamLoopBarPriority_Object = MibTableColumn
ctrlParamLoopBarPriority = _CtrlParamLoopBarPriority_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 24),
    _CtrlParamLoopBarPriority_Type()
)
ctrlParamLoopBarPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamLoopBarPriority.setStatus("mandatory")


class _CtrlParamExtendedCallMgmt_Type(Integer32):
    """Custom type ctrlParamExtendedCallMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              13,
              17,
              33)
        )
    )
    namedValues = NamedValues(
        *(("fep", 33),
          ("in", 2),
          ("in-out", 4),
          ("none", 1),
          ("out", 3),
          ("poll", 17),
          ("v25b", 5),
          ("v25m", 13))
    )


_CtrlParamExtendedCallMgmt_Type.__name__ = "Integer32"
_CtrlParamExtendedCallMgmt_Object = MibTableColumn
ctrlParamExtendedCallMgmt = _CtrlParamExtendedCallMgmt_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 25),
    _CtrlParamExtendedCallMgmt_Type()
)
ctrlParamExtendedCallMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamExtendedCallMgmt.setStatus("mandatory")


class _CtrlParamOptionalTimers_Type(Integer32):
    """Custom type ctrlParamOptionalTimers based on Integer32"""
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
          ("t13", 2),
          ("t23", 3))
    )


_CtrlParamOptionalTimers_Type.__name__ = "Integer32"
_CtrlParamOptionalTimers_Object = MibTableColumn
ctrlParamOptionalTimers = _CtrlParamOptionalTimers_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 26),
    _CtrlParamOptionalTimers_Type()
)
ctrlParamOptionalTimers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamOptionalTimers.setStatus("mandatory")


class _CtrlParamOptionalFlags_Type(Integer32):
    """Custom type ctrlParamOptionalFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_CtrlParamOptionalFlags_Type.__name__ = "Integer32"
_CtrlParamOptionalFlags_Object = MibTableColumn
ctrlParamOptionalFlags = _CtrlParamOptionalFlags_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 27),
    _CtrlParamOptionalFlags_Type()
)
ctrlParamOptionalFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamOptionalFlags.setStatus("mandatory")


class _CtrlParamTransportLevelType_Type(Integer32):
    """Custom type ctrlParamTransportLevelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              34)
        )
    )
    namedValues = NamedValues(
        *(("iso", 34),
          ("none", 1))
    )


_CtrlParamTransportLevelType_Type.__name__ = "Integer32"
_CtrlParamTransportLevelType_Object = MibTableColumn
ctrlParamTransportLevelType = _CtrlParamTransportLevelType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 28),
    _CtrlParamTransportLevelType_Type()
)
ctrlParamTransportLevelType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamTransportLevelType.setStatus("mandatory")


class _CtrlParamTransportClass_Type(Integer32):
    """Custom type ctrlParamTransportClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              33,
              49)
        )
    )
    namedValues = NamedValues(
        *(("class2", 33),
          ("class3", 49),
          ("none", 1))
    )


_CtrlParamTransportClass_Type.__name__ = "Integer32"
_CtrlParamTransportClass_Object = MibTableColumn
ctrlParamTransportClass = _CtrlParamTransportClass_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 29),
    _CtrlParamTransportClass_Type()
)
ctrlParamTransportClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamTransportClass.setStatus("mandatory")


class _CtrlParamDefaultWindowSize_Type(Integer32):
    """Custom type ctrlParamDefaultWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CtrlParamDefaultWindowSize_Type.__name__ = "Integer32"
_CtrlParamDefaultWindowSize_Object = MibTableColumn
ctrlParamDefaultWindowSize = _CtrlParamDefaultWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 30),
    _CtrlParamDefaultWindowSize_Type()
)
ctrlParamDefaultWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamDefaultWindowSize.setStatus("mandatory")


class _CtrlParamDisableFlowControl_Type(Integer32):
    """Custom type ctrlParamDisableFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CtrlParamDisableFlowControl_Type.__name__ = "Integer32"
_CtrlParamDisableFlowControl_Object = MibTableColumn
ctrlParamDisableFlowControl = _CtrlParamDisableFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 31),
    _CtrlParamDisableFlowControl_Type()
)
ctrlParamDisableFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamDisableFlowControl.setStatus("mandatory")


class _CtrlParamTSAPFormat_Type(Integer32):
    """Custom type ctrlParamTSAPFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hex", 1),
          ("text", 2))
    )


_CtrlParamTSAPFormat_Type.__name__ = "Integer32"
_CtrlParamTSAPFormat_Object = MibTableColumn
ctrlParamTSAPFormat = _CtrlParamTSAPFormat_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 32),
    _CtrlParamTSAPFormat_Type()
)
ctrlParamTSAPFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamTSAPFormat.setStatus("mandatory")


class _CtrlParamMaximumTPDUSize_Type(Integer32):
    """Custom type ctrlParamMaximumTPDUSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("bytes-1024", 11),
          ("bytes-128", 1),
          ("bytes-256", 9),
          ("bytes-512", 10),
          ("bytes128", 8))
    )


_CtrlParamMaximumTPDUSize_Type.__name__ = "Integer32"
_CtrlParamMaximumTPDUSize_Object = MibTableColumn
ctrlParamMaximumTPDUSize = _CtrlParamMaximumTPDUSize_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 33),
    _CtrlParamMaximumTPDUSize_Type()
)
ctrlParamMaximumTPDUSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamMaximumTPDUSize.setStatus("mandatory")


class _CtrlParamTTRTime_Type(Integer32):
    """Custom type ctrlParamTTRTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_CtrlParamTTRTime_Type.__name__ = "Integer32"
_CtrlParamTTRTime_Object = MibTableColumn
ctrlParamTTRTime = _CtrlParamTTRTime_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 34),
    _CtrlParamTTRTime_Type()
)
ctrlParamTTRTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamTTRTime.setStatus("mandatory")


class _CtrlParamTWRTime_Type(Integer32):
    """Custom type ctrlParamTWRTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_CtrlParamTWRTime_Type.__name__ = "Integer32"
_CtrlParamTWRTime_Object = MibTableColumn
ctrlParamTWRTime = _CtrlParamTWRTime_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 35),
    _CtrlParamTWRTime_Type()
)
ctrlParamTWRTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamTWRTime.setStatus("mandatory")
_CtrlParamDestinationAddress_Type = DisplayString
_CtrlParamDestinationAddress_Object = MibTableColumn
ctrlParamDestinationAddress = _CtrlParamDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 36),
    _CtrlParamDestinationAddress_Type()
)
ctrlParamDestinationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamDestinationAddress.setStatus("mandatory")


class _CtrlParamDSAP_Type(Integer32):
    """Custom type ctrlParamDSAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 254),
    )


_CtrlParamDSAP_Type.__name__ = "Integer32"
_CtrlParamDSAP_Object = MibTableColumn
ctrlParamDSAP = _CtrlParamDSAP_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 37),
    _CtrlParamDSAP_Type()
)
ctrlParamDSAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamDSAP.setStatus("mandatory")


class _CtrlParamSSAP_Type(Integer32):
    """Custom type ctrlParamSSAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 254),
    )


_CtrlParamSSAP_Type.__name__ = "Integer32"
_CtrlParamSSAP_Object = MibTableColumn
ctrlParamSSAP = _CtrlParamSSAP_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 38),
    _CtrlParamSSAP_Type()
)
ctrlParamSSAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamSSAP.setStatus("mandatory")


class _CtrlParamSDLCOptions_Type(Integer32):
    """Custom type ctrlParamSDLCOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              17,
              33,
              65,
              129,
              193)
        )
    )
    namedValues = NamedValues(
        *(("idle", 17),
          ("none", 1),
          ("pu4", 33),
          ("wait", 65),
          ("wait-xid", 193),
          ("xid", 129))
    )


_CtrlParamSDLCOptions_Type.__name__ = "Integer32"
_CtrlParamSDLCOptions_Object = MibTableColumn
ctrlParamSDLCOptions = _CtrlParamSDLCOptions_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 39),
    _CtrlParamSDLCOptions_Type()
)
ctrlParamSDLCOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamSDLCOptions.setStatus("mandatory")


class _CtrlParamPrimaryStation_Type(Integer32):
    """Custom type ctrlParamPrimaryStation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CtrlParamPrimaryStation_Type.__name__ = "Integer32"
_CtrlParamPrimaryStation_Object = MibTableColumn
ctrlParamPrimaryStation = _CtrlParamPrimaryStation_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 40),
    _CtrlParamPrimaryStation_Type()
)
ctrlParamPrimaryStation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamPrimaryStation.setStatus("mandatory")


class _CtrlParamIdleDetectTime_Type(Integer32):
    """Custom type ctrlParamIdleDetectTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CtrlParamIdleDetectTime_Type.__name__ = "Integer32"
_CtrlParamIdleDetectTime_Object = MibTableColumn
ctrlParamIdleDetectTime = _CtrlParamIdleDetectTime_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 41),
    _CtrlParamIdleDetectTime_Type()
)
ctrlParamIdleDetectTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamIdleDetectTime.setStatus("mandatory")


class _CtrlParamPollInterval_Type(Integer32):
    """Custom type ctrlParamPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CtrlParamPollInterval_Type.__name__ = "Integer32"
_CtrlParamPollInterval_Object = MibTableColumn
ctrlParamPollInterval = _CtrlParamPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 42),
    _CtrlParamPollInterval_Type()
)
ctrlParamPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamPollInterval.setStatus("mandatory")


class _CtrlParamDuplex_Type(Integer32):
    """Custom type ctrlParamDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2))
    )


_CtrlParamDuplex_Type.__name__ = "Integer32"
_CtrlParamDuplex_Object = MibTableColumn
ctrlParamDuplex = _CtrlParamDuplex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 43),
    _CtrlParamDuplex_Type()
)
ctrlParamDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamDuplex.setStatus("mandatory")


class _CtrlParamTransmitDelay_Type(Integer32):
    """Custom type ctrlParamTransmitDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_CtrlParamTransmitDelay_Type.__name__ = "Integer32"
_CtrlParamTransmitDelay_Object = MibTableColumn
ctrlParamTransmitDelay = _CtrlParamTransmitDelay_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 44),
    _CtrlParamTransmitDelay_Type()
)
ctrlParamTransmitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamTransmitDelay.setStatus("mandatory")


class _CtrlParamSlowPollTimer_Type(Integer32):
    """Custom type ctrlParamSlowPollTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CtrlParamSlowPollTimer_Type.__name__ = "Integer32"
_CtrlParamSlowPollTimer_Object = MibTableColumn
ctrlParamSlowPollTimer = _CtrlParamSlowPollTimer_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 45),
    _CtrlParamSlowPollTimer_Type()
)
ctrlParamSlowPollTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamSlowPollTimer.setStatus("mandatory")


class _CtrlParamMaxCallInterval_Type(Integer32):
    """Custom type ctrlParamMaxCallInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_CtrlParamMaxCallInterval_Type.__name__ = "Integer32"
_CtrlParamMaxCallInterval_Object = MibTableColumn
ctrlParamMaxCallInterval = _CtrlParamMaxCallInterval_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 46),
    _CtrlParamMaxCallInterval_Type()
)
ctrlParamMaxCallInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamMaxCallInterval.setStatus("mandatory")


class _CtrlParamMaxCallCycles_Type(Integer32):
    """Custom type ctrlParamMaxCallCycles based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CtrlParamMaxCallCycles_Type.__name__ = "Integer32"
_CtrlParamMaxCallCycles_Object = MibTableColumn
ctrlParamMaxCallCycles = _CtrlParamMaxCallCycles_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 47),
    _CtrlParamMaxCallCycles_Type()
)
ctrlParamMaxCallCycles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamMaxCallCycles.setStatus("mandatory")


class _CtrlParamGroupPoll_Type(Integer32):
    """Custom type ctrlParamGroupPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CtrlParamGroupPoll_Type.__name__ = "Integer32"
_CtrlParamGroupPoll_Object = MibTableColumn
ctrlParamGroupPoll = _CtrlParamGroupPoll_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 48),
    _CtrlParamGroupPoll_Type()
)
ctrlParamGroupPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamGroupPoll.setStatus("mandatory")


class _CtrlParamDelayToRTSLow_Type(Integer32):
    """Custom type ctrlParamDelayToRTSLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_CtrlParamDelayToRTSLow_Type.__name__ = "Integer32"
_CtrlParamDelayToRTSLow_Object = MibTableColumn
ctrlParamDelayToRTSLow = _CtrlParamDelayToRTSLow_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 49),
    _CtrlParamDelayToRTSLow_Type()
)
ctrlParamDelayToRTSLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamDelayToRTSLow.setStatus("mandatory")


class _CtrlParamDelayToCTSHigh_Type(Integer32):
    """Custom type ctrlParamDelayToCTSHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_CtrlParamDelayToCTSHigh_Type.__name__ = "Integer32"
_CtrlParamDelayToCTSHigh_Object = MibTableColumn
ctrlParamDelayToCTSHigh = _CtrlParamDelayToCTSHigh_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 50),
    _CtrlParamDelayToCTSHigh_Type()
)
ctrlParamDelayToCTSHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamDelayToCTSHigh.setStatus("mandatory")


class _CtrlParamInputSyncDeletion_Type(Integer32):
    """Custom type ctrlParamInputSyncDeletion based on Integer32"""
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


_CtrlParamInputSyncDeletion_Type.__name__ = "Integer32"
_CtrlParamInputSyncDeletion_Object = MibTableColumn
ctrlParamInputSyncDeletion = _CtrlParamInputSyncDeletion_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 51),
    _CtrlParamInputSyncDeletion_Type()
)
ctrlParamInputSyncDeletion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamInputSyncDeletion.setStatus("mandatory")


class _CtrlParamOutputSyncInsertion_Type(Integer32):
    """Custom type ctrlParamOutputSyncInsertion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CtrlParamOutputSyncInsertion_Type.__name__ = "Integer32"
_CtrlParamOutputSyncInsertion_Object = MibTableColumn
ctrlParamOutputSyncInsertion = _CtrlParamOutputSyncInsertion_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 52),
    _CtrlParamOutputSyncInsertion_Type()
)
ctrlParamOutputSyncInsertion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamOutputSyncInsertion.setStatus("mandatory")


class _CtrlParamDCDFilter_Type(Integer32):
    """Custom type ctrlParamDCDFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_CtrlParamDCDFilter_Type.__name__ = "Integer32"
_CtrlParamDCDFilter_Object = MibTableColumn
ctrlParamDCDFilter = _CtrlParamDCDFilter_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 53),
    _CtrlParamDCDFilter_Type()
)
ctrlParamDCDFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamDCDFilter.setStatus("mandatory")


class _CtrlParamInhibitTimeFill_Type(Integer32):
    """Custom type ctrlParamInhibitTimeFill based on Integer32"""
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


_CtrlParamInhibitTimeFill_Type.__name__ = "Integer32"
_CtrlParamInhibitTimeFill_Object = MibTableColumn
ctrlParamInhibitTimeFill = _CtrlParamInhibitTimeFill_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 54),
    _CtrlParamInhibitTimeFill_Type()
)
ctrlParamInhibitTimeFill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamInhibitTimeFill.setStatus("mandatory")


class _CtrlParamDirectedBroadcasts_Type(Integer32):
    """Custom type ctrlParamDirectedBroadcasts based on Integer32"""
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


_CtrlParamDirectedBroadcasts_Type.__name__ = "Integer32"
_CtrlParamDirectedBroadcasts_Object = MibTableColumn
ctrlParamDirectedBroadcasts = _CtrlParamDirectedBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 55),
    _CtrlParamDirectedBroadcasts_Type()
)
ctrlParamDirectedBroadcasts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamDirectedBroadcasts.setStatus("mandatory")


class _CtrlParamDefaultLocalPrinter_Type(Integer32):
    """Custom type ctrlParamDefaultLocalPrinter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CtrlParamDefaultLocalPrinter_Type.__name__ = "Integer32"
_CtrlParamDefaultLocalPrinter_Object = MibTableColumn
ctrlParamDefaultLocalPrinter = _CtrlParamDefaultLocalPrinter_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 56),
    _CtrlParamDefaultLocalPrinter_Type()
)
ctrlParamDefaultLocalPrinter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamDefaultLocalPrinter.setStatus("mandatory")


class _CtrlParamNewLANInterface_Type(Integer32):
    """Custom type ctrlParamNewLANInterface based on Integer32"""
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


_CtrlParamNewLANInterface_Type.__name__ = "Integer32"
_CtrlParamNewLANInterface_Object = MibTableColumn
ctrlParamNewLANInterface = _CtrlParamNewLANInterface_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 57),
    _CtrlParamNewLANInterface_Type()
)
ctrlParamNewLANInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamNewLANInterface.setStatus("mandatory")


class _CtrlParamNewSerialInterface_Type(Integer32):
    """Custom type ctrlParamNewSerialInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CtrlParamNewSerialInterface_Type.__name__ = "Integer32"
_CtrlParamNewSerialInterface_Object = MibTableColumn
ctrlParamNewSerialInterface = _CtrlParamNewSerialInterface_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 58),
    _CtrlParamNewSerialInterface_Type()
)
ctrlParamNewSerialInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamNewSerialInterface.setStatus("mandatory")


class _CtrlParamDlci_Type(Integer32):
    """Custom type ctrlParamDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1022),
    )


_CtrlParamDlci_Type.__name__ = "Integer32"
_CtrlParamDlci_Object = MibTableColumn
ctrlParamDlci = _CtrlParamDlci_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 59),
    _CtrlParamDlci_Type()
)
ctrlParamDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamDlci.setStatus("mandatory")


class _CtrlParamMode_Type(Integer32):
    """Custom type ctrlParamMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dce", 3),
          ("dte", 2),
          ("dte-dce", 4))
    )


_CtrlParamMode_Type.__name__ = "Integer32"
_CtrlParamMode_Object = MibTableColumn
ctrlParamMode = _CtrlParamMode_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 60),
    _CtrlParamMode_Type()
)
ctrlParamMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamMode.setStatus("mandatory")


class _CtrlParamLmi_Type(Integer32):
    """Custom type ctrlParamLmi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              129)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 129),
          ("no", 1),
          ("yes", 2))
    )


_CtrlParamLmi_Type.__name__ = "Integer32"
_CtrlParamLmi_Object = MibTableColumn
ctrlParamLmi = _CtrlParamLmi_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 61),
    _CtrlParamLmi_Type()
)
ctrlParamLmi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamLmi.setStatus("mandatory")


class _CtrlParamKeepAliveTimer_Type(Integer32):
    """Custom type ctrlParamKeepAliveTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 80),
    )


_CtrlParamKeepAliveTimer_Type.__name__ = "Integer32"
_CtrlParamKeepAliveTimer_Object = MibTableColumn
ctrlParamKeepAliveTimer = _CtrlParamKeepAliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 62),
    _CtrlParamKeepAliveTimer_Type()
)
ctrlParamKeepAliveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamKeepAliveTimer.setStatus("mandatory")


class _CtrlParamFullStatusInterval_Type(Integer32):
    """Custom type ctrlParamFullStatusInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CtrlParamFullStatusInterval_Type.__name__ = "Integer32"
_CtrlParamFullStatusInterval_Object = MibTableColumn
ctrlParamFullStatusInterval = _CtrlParamFullStatusInterval_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 63),
    _CtrlParamFullStatusInterval_Type()
)
ctrlParamFullStatusInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamFullStatusInterval.setStatus("mandatory")


class _CtrlParamBandwidth_Type(Integer32):
    """Custom type ctrlParamBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_CtrlParamBandwidth_Type.__name__ = "Integer32"
_CtrlParamBandwidth_Object = MibTableColumn
ctrlParamBandwidth = _CtrlParamBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 64),
    _CtrlParamBandwidth_Type()
)
ctrlParamBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamBandwidth.setStatus("mandatory")


class _CtrlParamBurstCommit_Type(Integer32):
    """Custom type ctrlParamBurstCommit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_CtrlParamBurstCommit_Type.__name__ = "Integer32"
_CtrlParamBurstCommit_Object = MibTableColumn
ctrlParamBurstCommit = _CtrlParamBurstCommit_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 65),
    _CtrlParamBurstCommit_Type()
)
ctrlParamBurstCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamBurstCommit.setStatus("mandatory")


class _CtrlParamBurstEligibility_Type(Integer32):
    """Custom type ctrlParamBurstEligibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_CtrlParamBurstEligibility_Type.__name__ = "Integer32"
_CtrlParamBurstEligibility_Object = MibTableColumn
ctrlParamBurstEligibility = _CtrlParamBurstEligibility_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 66),
    _CtrlParamBurstEligibility_Type()
)
ctrlParamBurstEligibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamBurstEligibility.setStatus("mandatory")


class _CtrlParamTimerT3_Type(Integer32):
    """Custom type ctrlParamTimerT3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CtrlParamTimerT3_Type.__name__ = "Integer32"
_CtrlParamTimerT3_Object = MibTableColumn
ctrlParamTimerT3 = _CtrlParamTimerT3_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 67),
    _CtrlParamTimerT3_Type()
)
ctrlParamTimerT3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamTimerT3.setStatus("mandatory")
_CtrlParamFlowControl_Type = Integer32
_CtrlParamFlowControl_Object = MibTableColumn
ctrlParamFlowControl = _CtrlParamFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 68),
    _CtrlParamFlowControl_Type()
)
ctrlParamFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamFlowControl.setStatus("mandatory")


class _CtrlParamConfigState_Type(Integer32):
    """Custom type ctrlParamConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CtrlParamConfigState_Type.__name__ = "Integer32"
_CtrlParamConfigState_Object = MibTableColumn
ctrlParamConfigState = _CtrlParamConfigState_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 69),
    _CtrlParamConfigState_Type()
)
ctrlParamConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamConfigState.setStatus("mandatory")


class _CtrlParamTry_Type(Integer32):
    """Custom type ctrlParamTry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_CtrlParamTry_Type.__name__ = "Integer32"
_CtrlParamTry_Object = MibTableColumn
ctrlParamTry = _CtrlParamTry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 3, 4, 1, 70),
    _CtrlParamTry_Type()
)
ctrlParamTry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctrlParamTry.setStatus("mandatory")
_Channel_ObjectIdentity = ObjectIdentity
channel = _Channel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4)
)
_ChanNumberConfigured_Type = Integer32
_ChanNumberConfigured_Object = MibScalar
chanNumberConfigured = _ChanNumberConfigured_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 1),
    _ChanNumberConfigured_Type()
)
chanNumberConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanNumberConfigured.setStatus("mandatory")
_ChanStatTable_Object = MibTable
chanStatTable = _ChanStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2)
)
if mibBuilder.loadTexts:
    chanStatTable.setStatus("mandatory")
_ChanStatEntry_Object = MibTableRow
chanStatEntry = _ChanStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1)
)
chanStatEntry.setIndexNames(
    (0, "SAT-MEGA-MIB", "chanStatIndex"),
)
if mibBuilder.loadTexts:
    chanStatEntry.setStatus("mandatory")
_ChanStatIndex_Type = Integer32
_ChanStatIndex_Object = MibTableColumn
chanStatIndex = _ChanStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 1),
    _ChanStatIndex_Type()
)
chanStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatIndex.setStatus("mandatory")


class _ChanStatName_Type(DisplayString):
    """Custom type chanStatName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_ChanStatName_Type.__name__ = "DisplayString"
_ChanStatName_Object = MibTableColumn
chanStatName = _ChanStatName_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 2),
    _ChanStatName_Type()
)
chanStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatName.setStatus("mandatory")
_ChanStatControllerIndex_Type = Integer32
_ChanStatControllerIndex_Object = MibTableColumn
chanStatControllerIndex = _ChanStatControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 3),
    _ChanStatControllerIndex_Type()
)
chanStatControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatControllerIndex.setStatus("mandatory")


class _ChanStatNameCtrlName_Type(DisplayString):
    """Custom type chanStatNameCtrlName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_ChanStatNameCtrlName_Type.__name__ = "DisplayString"
_ChanStatNameCtrlName_Object = MibTableColumn
chanStatNameCtrlName = _ChanStatNameCtrlName_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 4),
    _ChanStatNameCtrlName_Type()
)
chanStatNameCtrlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatNameCtrlName.setStatus("mandatory")
_ChanStatConnectedToChannelIndex_Type = Integer32
_ChanStatConnectedToChannelIndex_Object = MibTableColumn
chanStatConnectedToChannelIndex = _ChanStatConnectedToChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 5),
    _ChanStatConnectedToChannelIndex_Type()
)
chanStatConnectedToChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatConnectedToChannelIndex.setStatus("mandatory")


class _ChanStatState_Type(Integer32):
    """Custom type chanStatState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              9,
              13,
              17,
              21,
              25,
              29,
              33,
              37,
              41,
              45,
              49,
              57,
              69)
        )
    )
    namedValues = NamedValues(
        *(("addr", 25),
          ("busy", 49),
          ("call", 45),
          ("data", 41),
          ("disc", 1),
          ("emul", 69),
          ("look", 17),
          ("name", 21),
          ("pass", 9),
          ("post", 57),
          ("rout", 29),
          ("rung", 5),
          ("serv", 13),
          ("setup", 33),
          ("wake", 37))
    )


_ChanStatState_Type.__name__ = "Integer32"
_ChanStatState_Object = MibTableColumn
chanStatState = _ChanStatState_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 6),
    _ChanStatState_Type()
)
chanStatState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatState.setStatus("mandatory")


class _ChanStatSessionStatus_Type(Integer32):
    """Custom type chanStatSessionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              9,
              17,
              33,
              65,
              129)
        )
    )
    namedValues = NamedValues(
        *(("call", 9),
          ("disc", 129),
          ("dri", 3),
          ("dro", 5),
          ("none", 1),
          ("pad", 17),
          ("queu", 33),
          ("stat", 65),
          ("tran", 2))
    )


_ChanStatSessionStatus_Type.__name__ = "Integer32"
_ChanStatSessionStatus_Object = MibTableColumn
chanStatSessionStatus = _ChanStatSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 7),
    _ChanStatSessionStatus_Type()
)
chanStatSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatSessionStatus.setStatus("mandatory")


class _ChanStatEIA_Type(Integer32):
    """Custom type chanStatEIA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              9,
              17,
              33,
              65,
              129)
        )
    )
    namedValues = NamedValues(
        *(("closed", 65),
          ("dcd", 2),
          ("down", 129),
          ("iso", 17),
          ("none", 1),
          ("rej", 9),
          ("ring", 3),
          ("tcal", 33),
          ("x28", 5))
    )


_ChanStatEIA_Type.__name__ = "Integer32"
_ChanStatEIA_Object = MibTableColumn
chanStatEIA = _ChanStatEIA_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 8),
    _ChanStatEIA_Type()
)
chanStatEIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatEIA.setStatus("mandatory")
_ChanStatTotalFramesIn_Type = Counter32
_ChanStatTotalFramesIn_Object = MibTableColumn
chanStatTotalFramesIn = _ChanStatTotalFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 9),
    _ChanStatTotalFramesIn_Type()
)
chanStatTotalFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatTotalFramesIn.setStatus("mandatory")
_ChanStatTotalFramesOut_Type = Counter32
_ChanStatTotalFramesOut_Object = MibTableColumn
chanStatTotalFramesOut = _ChanStatTotalFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 10),
    _ChanStatTotalFramesOut_Type()
)
chanStatTotalFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatTotalFramesOut.setStatus("mandatory")
_ChanStatTotalCharsIn_Type = Counter32
_ChanStatTotalCharsIn_Object = MibTableColumn
chanStatTotalCharsIn = _ChanStatTotalCharsIn_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 11),
    _ChanStatTotalCharsIn_Type()
)
chanStatTotalCharsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatTotalCharsIn.setStatus("mandatory")
_ChanStatTotalCharsOut_Type = Counter32
_ChanStatTotalCharsOut_Object = MibTableColumn
chanStatTotalCharsOut = _ChanStatTotalCharsOut_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 12),
    _ChanStatTotalCharsOut_Type()
)
chanStatTotalCharsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatTotalCharsOut.setStatus("mandatory")
_ChanStatTxWindow_Type = Integer32
_ChanStatTxWindow_Object = MibTableColumn
chanStatTxWindow = _ChanStatTxWindow_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 13),
    _ChanStatTxWindow_Type()
)
chanStatTxWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatTxWindow.setStatus("mandatory")
_ChanStatRxWindow_Type = Integer32
_ChanStatRxWindow_Object = MibTableColumn
chanStatRxWindow = _ChanStatRxWindow_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 14),
    _ChanStatRxWindow_Type()
)
chanStatRxWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatRxWindow.setStatus("mandatory")
_ChanStatTxSize_Type = Integer32
_ChanStatTxSize_Object = MibTableColumn
chanStatTxSize = _ChanStatTxSize_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 15),
    _ChanStatTxSize_Type()
)
chanStatTxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatTxSize.setStatus("mandatory")
_ChanStatRxSize_Type = Integer32
_ChanStatRxSize_Object = MibTableColumn
chanStatRxSize = _ChanStatRxSize_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 16),
    _ChanStatRxSize_Type()
)
chanStatRxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatRxSize.setStatus("mandatory")
_ChanStatCause_Type = Integer32
_ChanStatCause_Object = MibTableColumn
chanStatCause = _ChanStatCause_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 17),
    _ChanStatCause_Type()
)
chanStatCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatCause.setStatus("mandatory")
_ChanStatDiagnostic_Type = Integer32
_ChanStatDiagnostic_Object = MibTableColumn
chanStatDiagnostic = _ChanStatDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 18),
    _ChanStatDiagnostic_Type()
)
chanStatDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatDiagnostic.setStatus("mandatory")
_ChanStatResetCause_Type = Integer32
_ChanStatResetCause_Object = MibTableColumn
chanStatResetCause = _ChanStatResetCause_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 19),
    _ChanStatResetCause_Type()
)
chanStatResetCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatResetCause.setStatus("mandatory")
_ChanStatResetDiagnostic_Type = Integer32
_ChanStatResetDiagnostic_Object = MibTableColumn
chanStatResetDiagnostic = _ChanStatResetDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 20),
    _ChanStatResetDiagnostic_Type()
)
chanStatResetDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatResetDiagnostic.setStatus("mandatory")
_ChanStatResetCauseReceived_Type = Integer32
_ChanStatResetCauseReceived_Object = MibTableColumn
chanStatResetCauseReceived = _ChanStatResetCauseReceived_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 21),
    _ChanStatResetCauseReceived_Type()
)
chanStatResetCauseReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatResetCauseReceived.setStatus("mandatory")
_ChanStatResetDiagReceived_Type = Integer32
_ChanStatResetDiagReceived_Object = MibTableColumn
chanStatResetDiagReceived = _ChanStatResetDiagReceived_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 22),
    _ChanStatResetDiagReceived_Type()
)
chanStatResetDiagReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatResetDiagReceived.setStatus("mandatory")


class _ChanStatLevel3State_Type(Integer32):
    """Custom type chanStatLevel3State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              7,
              9,
              11,
              13)
        )
    )
    namedValues = NamedValues(
        *(("call", 5),
          ("clr", 11),
          ("cls", 9),
          ("data", 7),
          ("disc", 1),
          ("reset", 13),
          ("rest", 3))
    )


_ChanStatLevel3State_Type.__name__ = "Integer32"
_ChanStatLevel3State_Object = MibTableColumn
chanStatLevel3State = _ChanStatLevel3State_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 23),
    _ChanStatLevel3State_Type()
)
chanStatLevel3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatLevel3State.setStatus("mandatory")
_ChanStatCallPriority_Type = Integer32
_ChanStatCallPriority_Object = MibTableColumn
chanStatCallPriority = _ChanStatCallPriority_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 24),
    _ChanStatCallPriority_Type()
)
chanStatCallPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatCallPriority.setStatus("mandatory")
_ChanStatResourcePriority_Type = Integer32
_ChanStatResourcePriority_Object = MibTableColumn
chanStatResourcePriority = _ChanStatResourcePriority_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 25),
    _ChanStatResourcePriority_Type()
)
chanStatResourcePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatResourcePriority.setStatus("mandatory")


class _ChanStatPadEnable_Type(Integer32):
    """Custom type chanStatPadEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              17,
              33)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("mask", 17),
          ("prof", 5),
          ("rev", 3),
          ("x28", 33))
    )


_ChanStatPadEnable_Type.__name__ = "Integer32"
_ChanStatPadEnable_Object = MibTableColumn
chanStatPadEnable = _ChanStatPadEnable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 26),
    _ChanStatPadEnable_Type()
)
chanStatPadEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatPadEnable.setStatus("mandatory")


class _ChanStatPortMatch_Type(Integer32):
    """Custom type chanStatPortMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              129,
              137)
        )
    )
    namedValues = NamedValues(
        *(("dest", 129),
          ("no", 1),
          ("srce", 2),
          ("wild", 137))
    )


_ChanStatPortMatch_Type.__name__ = "Integer32"
_ChanStatPortMatch_Object = MibTableColumn
chanStatPortMatch = _ChanStatPortMatch_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 27),
    _ChanStatPortMatch_Type()
)
chanStatPortMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatPortMatch.setStatus("mandatory")


class _ChanStatPrimaryStation_Type(Integer32):
    """Custom type chanStatPrimaryStation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ChanStatPrimaryStation_Type.__name__ = "Integer32"
_ChanStatPrimaryStation_Object = MibTableColumn
chanStatPrimaryStation = _ChanStatPrimaryStation_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 28),
    _ChanStatPrimaryStation_Type()
)
chanStatPrimaryStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatPrimaryStation.setStatus("mandatory")


class _ChanStatSDLCState_Type(Integer32):
    """Custom type chanStatSDLCState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("active", 5),
          ("disc", 9),
          ("idle", 1),
          ("poll", 7),
          ("snrm", 3))
    )


_ChanStatSDLCState_Type.__name__ = "Integer32"
_ChanStatSDLCState_Object = MibTableColumn
chanStatSDLCState = _ChanStatSDLCState_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 29),
    _ChanStatSDLCState_Type()
)
chanStatSDLCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatSDLCState.setStatus("mandatory")


class _ChanStatQLLCState_Type(Integer32):
    """Custom type chanStatQLLCState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              9,
              13,
              17,
              21)
        )
    )
    namedValues = NamedValues(
        *(("clsd", 5),
          ("clsi", 17),
          ("frmr", 13),
          ("inop", 1),
          ("open", 21),
          ("openi", 9))
    )


_ChanStatQLLCState_Type.__name__ = "Integer32"
_ChanStatQLLCState_Object = MibTableColumn
chanStatQLLCState = _ChanStatQLLCState_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 30),
    _ChanStatQLLCState_Type()
)
chanStatQLLCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatQLLCState.setStatus("mandatory")


class _ChanStatSDLCTransmitState_Type(Integer32):
    """Custom type chanStatSDLCTransmitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              7,
              11)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("norm", 3),
          ("rnr", 11),
          ("rtry", 7))
    )


_ChanStatSDLCTransmitState_Type.__name__ = "Integer32"
_ChanStatSDLCTransmitState_Object = MibTableColumn
chanStatSDLCTransmitState = _ChanStatSDLCTransmitState_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 31),
    _ChanStatSDLCTransmitState_Type()
)
chanStatSDLCTransmitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatSDLCTransmitState.setStatus("mandatory")
_ChanStatPolls_Type = Integer32
_ChanStatPolls_Object = MibTableColumn
chanStatPolls = _ChanStatPolls_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 32),
    _ChanStatPolls_Type()
)
chanStatPolls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatPolls.setStatus("mandatory")
_ChanStatStationAddress_Type = Integer32
_ChanStatStationAddress_Object = MibTableColumn
chanStatStationAddress = _ChanStatStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 33),
    _ChanStatStationAddress_Type()
)
chanStatStationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatStationAddress.setStatus("mandatory")
_ChanStatXIDIdentification_Type = DisplayString
_ChanStatXIDIdentification_Object = MibTableColumn
chanStatXIDIdentification = _ChanStatXIDIdentification_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 34),
    _ChanStatXIDIdentification_Type()
)
chanStatXIDIdentification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatXIDIdentification.setStatus("mandatory")
_ChanStatTries_Type = Integer32
_ChanStatTries_Object = MibTableColumn
chanStatTries = _ChanStatTries_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 35),
    _ChanStatTries_Type()
)
chanStatTries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatTries.setStatus("mandatory")
_ChanStatWindow_Type = Integer32
_ChanStatWindow_Object = MibTableColumn
chanStatWindow = _ChanStatWindow_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 36),
    _ChanStatWindow_Type()
)
chanStatWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatWindow.setStatus("mandatory")


class _ChanStatLUActive_Type(Integer32):
    """Custom type chanStatLUActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ChanStatLUActive_Type.__name__ = "Integer32"
_ChanStatLUActive_Object = MibTableColumn
chanStatLUActive = _ChanStatLUActive_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 37),
    _ChanStatLUActive_Type()
)
chanStatLUActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatLUActive.setStatus("mandatory")


class _ChanStatBindActive_Type(Integer32):
    """Custom type chanStatBindActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_ChanStatBindActive_Type.__name__ = "Integer32"
_ChanStatBindActive_Object = MibTableColumn
chanStatBindActive = _ChanStatBindActive_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 38),
    _ChanStatBindActive_Type()
)
chanStatBindActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatBindActive.setStatus("mandatory")


class _ChanStatLUType_Type(Integer32):
    """Custom type chanStatLUType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ChanStatLUType_Type.__name__ = "Integer32"
_ChanStatLUType_Object = MibTableColumn
chanStatLUType = _ChanStatLUType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 39),
    _ChanStatLUType_Type()
)
chanStatLUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatLUType.setStatus("mandatory")
_ChanStatBreaksReceived_Type = Counter32
_ChanStatBreaksReceived_Object = MibTableColumn
chanStatBreaksReceived = _ChanStatBreaksReceived_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 40),
    _ChanStatBreaksReceived_Type()
)
chanStatBreaksReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatBreaksReceived.setStatus("mandatory")
_ChanStatFramingErrors_Type = Counter32
_ChanStatFramingErrors_Object = MibTableColumn
chanStatFramingErrors = _ChanStatFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 41),
    _ChanStatFramingErrors_Type()
)
chanStatFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatFramingErrors.setStatus("mandatory")
_ChanStatInputOverruns_Type = Counter32
_ChanStatInputOverruns_Object = MibTableColumn
chanStatInputOverruns = _ChanStatInputOverruns_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 42),
    _ChanStatInputOverruns_Type()
)
chanStatInputOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatInputOverruns.setStatus("mandatory")
_ChanStatParityErrors_Type = Counter32
_ChanStatParityErrors_Object = MibTableColumn
chanStatParityErrors = _ChanStatParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 43),
    _ChanStatParityErrors_Type()
)
chanStatParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatParityErrors.setStatus("mandatory")


class _ChanStatTerminalType_Type(Integer32):
    """Custom type chanStatTerminalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              41,
              65,
              81,
              97,
              113,
              129,
              161,
              177,
              209,
              225,
              999)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 177),
          ("asyn", 2),
          ("buf", 81),
          ("ext-ansi", 161),
          ("hp", 225),
          ("mtrm", 113),
          ("slip", 97),
          ("sync", 3),
          ("tpad", 65),
          ("vpad", 129),
          ("vt200", 41),
          ("x28", 209),
          ("x28f", 999))
    )


_ChanStatTerminalType_Type.__name__ = "Integer32"
_ChanStatTerminalType_Object = MibTableColumn
chanStatTerminalType = _ChanStatTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 44),
    _ChanStatTerminalType_Type()
)
chanStatTerminalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatTerminalType.setStatus("mandatory")


class _ChanStatCircuitType_Type(Integer32):
    """Custom type chanStatCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              10,
              17,
              25,
              33,
              65,
              66,
              74,
              81,
              89,
              97)
        )
    )
    namedValues = NamedValues(
        *(("call", 2),
          ("call-pvc", 10),
          ("call-pvc-stat", 74),
          ("call-stat", 66),
          ("none", 1),
          ("osi", 5),
          ("out", 17),
          ("out-pvc", 25),
          ("out-pvc-stat", 89),
          ("out-stat", 81),
          ("queu", 4),
          ("stat", 65),
          ("svc", 33),
          ("svc-stat", 97))
    )


_ChanStatCircuitType_Type.__name__ = "Integer32"
_ChanStatCircuitType_Object = MibTableColumn
chanStatCircuitType = _ChanStatCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 45),
    _ChanStatCircuitType_Type()
)
chanStatCircuitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatCircuitType.setStatus("mandatory")


class _ChanStatOptions_Type(Integer32):
    """Custom type chanStatOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              9,
              17,
              65,
              129,
              257,
              513,
              1025,
              2049,
              4097,
              8193,
              16385,
              32769)
        )
    )
    namedValues = NamedValues(
        *(("arps", 65),
          ("bill", 513),
          ("busy", 5),
          ("gate", 2049),
          ("hold", 9),
          ("idle", 3),
          ("iso", 129),
          ("msgs", 1025),
          ("name", 4097),
          ("nbrk", 17),
          ("none", 1),
          ("pass", 257),
          ("rts", 2),
          ("supr", 32769),
          ("talk", 8193),
          ("x28", 16385))
    )


_ChanStatOptions_Type.__name__ = "Integer32"
_ChanStatOptions_Object = MibTableColumn
chanStatOptions = _ChanStatOptions_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 46),
    _ChanStatOptions_Type()
)
chanStatOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatOptions.setStatus("mandatory")
_ChanStatBuffers_Type = Integer32
_ChanStatBuffers_Object = MibTableColumn
chanStatBuffers = _ChanStatBuffers_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 47),
    _ChanStatBuffers_Type()
)
chanStatBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatBuffers.setStatus("mandatory")
_ChanStatDiscMode_Type = Integer32
_ChanStatDiscMode_Object = MibTableColumn
chanStatDiscMode = _ChanStatDiscMode_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 48),
    _ChanStatDiscMode_Type()
)
chanStatDiscMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatDiscMode.setStatus("mandatory")
_ChanStatMenuNumber_Type = Integer32
_ChanStatMenuNumber_Object = MibTableColumn
chanStatMenuNumber = _ChanStatMenuNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 49),
    _ChanStatMenuNumber_Type()
)
chanStatMenuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatMenuNumber.setStatus("mandatory")
_ChanStatHelpNumber_Type = Integer32
_ChanStatHelpNumber_Object = MibTableColumn
chanStatHelpNumber = _ChanStatHelpNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 50),
    _ChanStatHelpNumber_Type()
)
chanStatHelpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatHelpNumber.setStatus("mandatory")
_ChanStatNewsNumber_Type = Integer32
_ChanStatNewsNumber_Object = MibTableColumn
chanStatNewsNumber = _ChanStatNewsNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 51),
    _ChanStatNewsNumber_Type()
)
chanStatNewsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatNewsNumber.setStatus("mandatory")
_ChanStatPadRecall_Type = Integer32
_ChanStatPadRecall_Object = MibTableColumn
chanStatPadRecall = _ChanStatPadRecall_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 52),
    _ChanStatPadRecall_Type()
)
chanStatPadRecall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatPadRecall.setStatus("mandatory")


class _ChanStatEcho_Type(Integer32):
    """Custom type chanStatEcho based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("controlled", 3),
          ("disable", 2),
          ("enable", 1))
    )


_ChanStatEcho_Type.__name__ = "Integer32"
_ChanStatEcho_Object = MibTableColumn
chanStatEcho = _ChanStatEcho_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 53),
    _ChanStatEcho_Type()
)
chanStatEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatEcho.setStatus("mandatory")
_ChanStatDataForwarding_Type = Integer32
_ChanStatDataForwarding_Object = MibTableColumn
chanStatDataForwarding = _ChanStatDataForwarding_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 54),
    _ChanStatDataForwarding_Type()
)
chanStatDataForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatDataForwarding.setStatus("mandatory")
_ChanStatDelay_Type = Integer32
_ChanStatDelay_Object = MibTableColumn
chanStatDelay = _ChanStatDelay_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 55),
    _ChanStatDelay_Type()
)
chanStatDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatDelay.setStatus("mandatory")


class _ChanStatDRI_Type(Integer32):
    """Custom type chanStatDRI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              33,
              65,
              129)
        )
    )
    namedValues = NamedValues(
        *(("cts", 129),
          ("disabled", 1),
          ("enabled", 2),
          ("init", 65),
          ("init-enable", 3),
          ("rts", 33))
    )


_ChanStatDRI_Type.__name__ = "Integer32"
_ChanStatDRI_Object = MibTableColumn
chanStatDRI = _ChanStatDRI_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 56),
    _ChanStatDRI_Type()
)
chanStatDRI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatDRI.setStatus("mandatory")


class _ChanStatPadSignals_Type(Integer32):
    """Custom type chanStatPadSignals based on Integer32"""
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


_ChanStatPadSignals_Type.__name__ = "Integer32"
_ChanStatPadSignals_Object = MibTableColumn
chanStatPadSignals = _ChanStatPadSignals_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 57),
    _ChanStatPadSignals_Type()
)
chanStatPadSignals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatPadSignals.setStatus("mandatory")
_ChanStatBreak_Type = Integer32
_ChanStatBreak_Object = MibTableColumn
chanStatBreak = _ChanStatBreak_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 58),
    _ChanStatBreak_Type()
)
chanStatBreak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatBreak.setStatus("mandatory")
_ChanStatPadding_Type = Integer32
_ChanStatPadding_Object = MibTableColumn
chanStatPadding = _ChanStatPadding_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 59),
    _ChanStatPadding_Type()
)
chanStatPadding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatPadding.setStatus("mandatory")
_ChanStatFold_Type = Integer32
_ChanStatFold_Object = MibTableColumn
chanStatFold = _ChanStatFold_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 60),
    _ChanStatFold_Type()
)
chanStatFold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatFold.setStatus("mandatory")


class _ChanStatDRO_Type(Integer32):
    """Custom type chanStatDRO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              65,
              129)
        )
    )
    namedValues = NamedValues(
        *(("cts", 129),
          ("disabled", 1),
          ("enabled", 2),
          ("init", 65))
    )


_ChanStatDRO_Type.__name__ = "Integer32"
_ChanStatDRO_Object = MibTableColumn
chanStatDRO = _ChanStatDRO_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 61),
    _ChanStatDRO_Type()
)
chanStatDRO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatDRO.setStatus("mandatory")
_ChanStatLFI_Type = Integer32
_ChanStatLFI_Object = MibTableColumn
chanStatLFI = _ChanStatLFI_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 62),
    _ChanStatLFI_Type()
)
chanStatLFI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatLFI.setStatus("mandatory")
_ChanStatLFPad_Type = Integer32
_ChanStatLFPad_Object = MibTableColumn
chanStatLFPad = _ChanStatLFPad_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 63),
    _ChanStatLFPad_Type()
)
chanStatLFPad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatLFPad.setStatus("mandatory")


class _ChanStatEdit_Type(Integer32):
    """Custom type chanStatEdit based on Integer32"""
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


_ChanStatEdit_Type.__name__ = "Integer32"
_ChanStatEdit_Object = MibTableColumn
chanStatEdit = _ChanStatEdit_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 64),
    _ChanStatEdit_Type()
)
chanStatEdit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatEdit.setStatus("mandatory")
_ChanStatCharDel_Type = Integer32
_ChanStatCharDel_Object = MibTableColumn
chanStatCharDel = _ChanStatCharDel_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 65),
    _ChanStatCharDel_Type()
)
chanStatCharDel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatCharDel.setStatus("mandatory")
_ChanStatBufferDel_Type = Integer32
_ChanStatBufferDel_Object = MibTableColumn
chanStatBufferDel = _ChanStatBufferDel_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 66),
    _ChanStatBufferDel_Type()
)
chanStatBufferDel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatBufferDel.setStatus("mandatory")
_ChanStatDisp_Type = Integer32
_ChanStatDisp_Object = MibTableColumn
chanStatDisp = _ChanStatDisp_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 67),
    _ChanStatDisp_Type()
)
chanStatDisp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatDisp.setStatus("mandatory")
_ChanStatEditServiceSignals_Type = Integer32
_ChanStatEditServiceSignals_Object = MibTableColumn
chanStatEditServiceSignals = _ChanStatEditServiceSignals_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 68),
    _ChanStatEditServiceSignals_Type()
)
chanStatEditServiceSignals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatEditServiceSignals.setStatus("mandatory")
_ChanStatEchoMask_Type = Integer32
_ChanStatEchoMask_Object = MibTableColumn
chanStatEchoMask = _ChanStatEchoMask_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 69),
    _ChanStatEchoMask_Type()
)
chanStatEchoMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatEchoMask.setStatus("mandatory")
_ChanStatParityTreatment_Type = Integer32
_ChanStatParityTreatment_Object = MibTableColumn
chanStatParityTreatment = _ChanStatParityTreatment_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 70),
    _ChanStatParityTreatment_Type()
)
chanStatParityTreatment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatParityTreatment.setStatus("mandatory")
_ChanStatPageWait_Type = Integer32
_ChanStatPageWait_Object = MibTableColumn
chanStatPageWait = _ChanStatPageWait_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 71),
    _ChanStatPageWait_Type()
)
chanStatPageWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatPageWait.setStatus("mandatory")
_ChanStatForce_Type = Integer32
_ChanStatForce_Object = MibTableColumn
chanStatForce = _ChanStatForce_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 72),
    _ChanStatForce_Type()
)
chanStatForce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatForce.setStatus("mandatory")
_ChanStatBreakChar_Type = Integer32
_ChanStatBreakChar_Object = MibTableColumn
chanStatBreakChar = _ChanStatBreakChar_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 73),
    _ChanStatBreakChar_Type()
)
chanStatBreakChar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatBreakChar.setStatus("mandatory")


class _ChanStatNetworkParity_Type(Integer32):
    """Custom type chanStatNetworkParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("even", 1),
          ("mark", 4),
          ("none", 0),
          ("odd", 2),
          ("spac", 8))
    )


_ChanStatNetworkParity_Type.__name__ = "Integer32"
_ChanStatNetworkParity_Object = MibTableColumn
chanStatNetworkParity = _ChanStatNetworkParity_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 74),
    _ChanStatNetworkParity_Type()
)
chanStatNetworkParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatNetworkParity.setStatus("mandatory")
_ChanStatEscapeDelay_Type = Integer32
_ChanStatEscapeDelay_Object = MibTableColumn
chanStatEscapeDelay = _ChanStatEscapeDelay_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 75),
    _ChanStatEscapeDelay_Type()
)
chanStatEscapeDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatEscapeDelay.setStatus("mandatory")


class _ChanStatTransportLevelState_Type(Integer32):
    """Custom type chanStatTransportLevelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              7,
              9,
              11)
        )
    )
    namedValues = NamedValues(
        *(("call", 3),
          ("clr", 11),
          ("cls", 9),
          ("data", 7),
          ("disc", 1),
          ("init", 5))
    )


_ChanStatTransportLevelState_Type.__name__ = "Integer32"
_ChanStatTransportLevelState_Object = MibTableColumn
chanStatTransportLevelState = _ChanStatTransportLevelState_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 76),
    _ChanStatTransportLevelState_Type()
)
chanStatTransportLevelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatTransportLevelState.setStatus("mandatory")


class _ChanStatDestTsap_Type(DisplayString):
    """Custom type chanStatDestTsap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_ChanStatDestTsap_Type.__name__ = "DisplayString"
_ChanStatDestTsap_Object = MibTableColumn
chanStatDestTsap = _ChanStatDestTsap_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 77),
    _ChanStatDestTsap_Type()
)
chanStatDestTsap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatDestTsap.setStatus("mandatory")


class _ChanStatLinkState_Type(Integer32):
    """Custom type chanStatLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              7,
              9,
              11,
              13,
              15)
        )
    )
    namedValues = NamedValues(
        *(("ackr", 11),
          ("acks", 13),
          ("clos", 1),
          ("clsi", 5),
          ("open", 15),
          ("reqs", 9),
          ("stop", 3),
          ("stpi", 7))
    )


_ChanStatLinkState_Type.__name__ = "Integer32"
_ChanStatLinkState_Object = MibTableColumn
chanStatLinkState = _ChanStatLinkState_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 78),
    _ChanStatLinkState_Type()
)
chanStatLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatLinkState.setStatus("mandatory")


class _ChanStatProtocolState_Type(Integer32):
    """Custom type chanStatProtocolState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              7,
              9,
              11,
              13,
              15)
        )
    )
    namedValues = NamedValues(
        *(("ackr", 11),
          ("acks", 13),
          ("clos", 1),
          ("clsi", 5),
          ("open", 15),
          ("reqs", 9),
          ("stop", 3),
          ("stpi", 7))
    )


_ChanStatProtocolState_Type.__name__ = "Integer32"
_ChanStatProtocolState_Object = MibTableColumn
chanStatProtocolState = _ChanStatProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 79),
    _ChanStatProtocolState_Type()
)
chanStatProtocolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatProtocolState.setStatus("mandatory")


class _ChanStatProtocol_Type(Integer32):
    """Custom type chanStatProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32802,
              32812)
        )
    )
    namedValues = NamedValues(
        *(("ip", 32802),
          ("ipx", 32812))
    )


_ChanStatProtocol_Type.__name__ = "Integer32"
_ChanStatProtocol_Object = MibTableColumn
chanStatProtocol = _ChanStatProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 80),
    _ChanStatProtocol_Type()
)
chanStatProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatProtocol.setStatus("mandatory")
_ChanStatIdentity_Type = Integer32
_ChanStatIdentity_Object = MibTableColumn
chanStatIdentity = _ChanStatIdentity_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 81),
    _ChanStatIdentity_Type()
)
chanStatIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatIdentity.setStatus("mandatory")
_ChanStatFrameRelayWait_Type = Integer32
_ChanStatFrameRelayWait_Object = MibTableColumn
chanStatFrameRelayWait = _ChanStatFrameRelayWait_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 2, 1, 82),
    _ChanStatFrameRelayWait_Type()
)
chanStatFrameRelayWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatFrameRelayWait.setStatus("mandatory")
_ChanParamTable_Object = MibTable
chanParamTable = _ChanParamTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3)
)
if mibBuilder.loadTexts:
    chanParamTable.setStatus("mandatory")
_ChanParamEntry_Object = MibTableRow
chanParamEntry = _ChanParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1)
)
chanParamEntry.setIndexNames(
    (0, "SAT-MEGA-MIB", "chanParamIndex"),
)
if mibBuilder.loadTexts:
    chanParamEntry.setStatus("mandatory")
_ChanParamIndex_Type = Integer32
_ChanParamIndex_Object = MibTableColumn
chanParamIndex = _ChanParamIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 1),
    _ChanParamIndex_Type()
)
chanParamIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanParamIndex.setStatus("mandatory")


class _ChanParamName_Type(DisplayString):
    """Custom type chanParamName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_ChanParamName_Type.__name__ = "DisplayString"
_ChanParamName_Object = MibTableColumn
chanParamName = _ChanParamName_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 2),
    _ChanParamName_Type()
)
chanParamName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamName.setStatus("mandatory")


class _ChanParamDRCMask_Type(DisplayString):
    """Custom type chanParamDRCMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_ChanParamDRCMask_Type.__name__ = "DisplayString"
_ChanParamDRCMask_Object = MibTableColumn
chanParamDRCMask = _ChanParamDRCMask_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 3),
    _ChanParamDRCMask_Type()
)
chanParamDRCMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamDRCMask.setStatus("mandatory")


class _ChanParamTerminalType_Type(Integer32):
    """Custom type chanParamTerminalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              41,
              65,
              81,
              97,
              113,
              129,
              161,
              177,
              209,
              225,
              999)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 177),
          ("asyn", 2),
          ("buf", 81),
          ("ext-ansi", 161),
          ("hp", 225),
          ("mtrm", 113),
          ("slip", 97),
          ("sync", 3),
          ("tpad", 65),
          ("vpad", 129),
          ("vt200", 41),
          ("x28", 209),
          ("x28f", 999))
    )


_ChanParamTerminalType_Type.__name__ = "Integer32"
_ChanParamTerminalType_Object = MibTableColumn
chanParamTerminalType = _ChanParamTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 4),
    _ChanParamTerminalType_Type()
)
chanParamTerminalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamTerminalType.setStatus("mandatory")


class _ChanParamCircuitType_Type(Integer32):
    """Custom type chanParamCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              10,
              17,
              25,
              33,
              65,
              66,
              74,
              81,
              89,
              97)
        )
    )
    namedValues = NamedValues(
        *(("call", 2),
          ("call-pvc", 10),
          ("call-pvc-stat", 74),
          ("call-stat", 66),
          ("none", 1),
          ("osi", 5),
          ("out", 17),
          ("out-pvc", 25),
          ("out-pvc-stat", 89),
          ("out-stat", 81),
          ("queu", 4),
          ("stat", 65),
          ("svc", 33),
          ("svc-stat", 97))
    )


_ChanParamCircuitType_Type.__name__ = "Integer32"
_ChanParamCircuitType_Object = MibTableColumn
chanParamCircuitType = _ChanParamCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 5),
    _ChanParamCircuitType_Type()
)
chanParamCircuitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamCircuitType.setStatus("mandatory")


class _ChanParamOptions_Type(Integer32):
    """Custom type chanParamOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              9,
              17,
              33,
              65,
              129,
              257,
              513,
              1025,
              1281,
              2049,
              3329,
              4097,
              5121,
              5377,
              8193,
              13313,
              13569,
              15617,
              16385,
              32769)
        )
    )
    namedValues = NamedValues(
        *(("arps", 65),
          ("bill", 513),
          ("busy", 5),
          ("diag", 33),
          ("gate", 2049),
          ("hold", 9),
          ("idle", 3),
          ("iso", 129),
          ("msgs", 1025),
          ("msgs-name", 5121),
          ("msgs-name-pass", 5377),
          ("msgs-name-pass-talk", 13569),
          ("msgs-name-pass-talk-gate", 15617),
          ("msgs-name-talk", 13313),
          ("msgs-pass", 1281),
          ("msgs-pass-gate", 3329),
          ("name", 4097),
          ("nbrk", 17),
          ("none", 1),
          ("pass", 257),
          ("rts", 2),
          ("supr", 32769),
          ("talk", 8193),
          ("x28", 16385))
    )


_ChanParamOptions_Type.__name__ = "Integer32"
_ChanParamOptions_Object = MibTableColumn
chanParamOptions = _ChanParamOptions_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 6),
    _ChanParamOptions_Type()
)
chanParamOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamOptions.setStatus("mandatory")


class _ChanParamBuffers_Type(Integer32):
    """Custom type chanParamBuffers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 240),
    )


_ChanParamBuffers_Type.__name__ = "Integer32"
_ChanParamBuffers_Object = MibTableColumn
chanParamBuffers = _ChanParamBuffers_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 7),
    _ChanParamBuffers_Type()
)
chanParamBuffers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamBuffers.setStatus("mandatory")


class _ChanParamDiscMode_Type(Integer32):
    """Custom type chanParamDiscMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_ChanParamDiscMode_Type.__name__ = "Integer32"
_ChanParamDiscMode_Object = MibTableColumn
chanParamDiscMode = _ChanParamDiscMode_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 8),
    _ChanParamDiscMode_Type()
)
chanParamDiscMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamDiscMode.setStatus("mandatory")


class _ChanParamMenuNumber_Type(Integer32):
    """Custom type chanParamMenuNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_ChanParamMenuNumber_Type.__name__ = "Integer32"
_ChanParamMenuNumber_Object = MibTableColumn
chanParamMenuNumber = _ChanParamMenuNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 9),
    _ChanParamMenuNumber_Type()
)
chanParamMenuNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamMenuNumber.setStatus("mandatory")


class _ChanParamHelpNumber_Type(Integer32):
    """Custom type chanParamHelpNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_ChanParamHelpNumber_Type.__name__ = "Integer32"
_ChanParamHelpNumber_Object = MibTableColumn
chanParamHelpNumber = _ChanParamHelpNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 10),
    _ChanParamHelpNumber_Type()
)
chanParamHelpNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamHelpNumber.setStatus("mandatory")


class _ChanParamNewsNumber_Type(Integer32):
    """Custom type chanParamNewsNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_ChanParamNewsNumber_Type.__name__ = "Integer32"
_ChanParamNewsNumber_Object = MibTableColumn
chanParamNewsNumber = _ChanParamNewsNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 11),
    _ChanParamNewsNumber_Type()
)
chanParamNewsNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamNewsNumber.setStatus("mandatory")


class _ChanParamCallPriority_Type(Integer32):
    """Custom type chanParamCallPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ChanParamCallPriority_Type.__name__ = "Integer32"
_ChanParamCallPriority_Object = MibTableColumn
chanParamCallPriority = _ChanParamCallPriority_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 12),
    _ChanParamCallPriority_Type()
)
chanParamCallPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamCallPriority.setStatus("mandatory")


class _ChanParamResourcePriority_Type(Integer32):
    """Custom type chanParamResourcePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ChanParamResourcePriority_Type.__name__ = "Integer32"
_ChanParamResourcePriority_Object = MibTableColumn
chanParamResourcePriority = _ChanParamResourcePriority_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 13),
    _ChanParamResourcePriority_Type()
)
chanParamResourcePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamResourcePriority.setStatus("mandatory")


class _ChanParamPadEnable_Type(Integer32):
    """Custom type chanParamPadEnable based on Integer32"""
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
              34)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("enable-mask", 8),
          ("enable-prof", 6),
          ("enable-rev", 4),
          ("mask", 7),
          ("prof", 5),
          ("rev", 3),
          ("x28", 34))
    )


_ChanParamPadEnable_Type.__name__ = "Integer32"
_ChanParamPadEnable_Object = MibTableColumn
chanParamPadEnable = _ChanParamPadEnable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 14),
    _ChanParamPadEnable_Type()
)
chanParamPadEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamPadEnable.setStatus("mandatory")


class _ChanParamPadRecall_Type(Integer32):
    """Custom type chanParamPadRecall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )


_ChanParamPadRecall_Type.__name__ = "Integer32"
_ChanParamPadRecall_Object = MibTableColumn
chanParamPadRecall = _ChanParamPadRecall_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 15),
    _ChanParamPadRecall_Type()
)
chanParamPadRecall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamPadRecall.setStatus("mandatory")


class _ChanParamEcho_Type(Integer32):
    """Custom type chanParamEcho based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("controlled", 3),
          ("disable", 2),
          ("enable", 1))
    )


_ChanParamEcho_Type.__name__ = "Integer32"
_ChanParamEcho_Object = MibTableColumn
chanParamEcho = _ChanParamEcho_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 16),
    _ChanParamEcho_Type()
)
chanParamEcho.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamEcho.setStatus("mandatory")
_ChanParamDataForwarding_Type = Integer32
_ChanParamDataForwarding_Object = MibTableColumn
chanParamDataForwarding = _ChanParamDataForwarding_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 17),
    _ChanParamDataForwarding_Type()
)
chanParamDataForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamDataForwarding.setStatus("mandatory")


class _ChanParamDelay_Type(Integer32):
    """Custom type chanParamDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChanParamDelay_Type.__name__ = "Integer32"
_ChanParamDelay_Object = MibTableColumn
chanParamDelay = _ChanParamDelay_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 18),
    _ChanParamDelay_Type()
)
chanParamDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamDelay.setStatus("mandatory")


class _ChanParamDRI_Type(Integer32):
    """Custom type chanParamDRI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              33,
              65,
              129)
        )
    )
    namedValues = NamedValues(
        *(("cts", 129),
          ("disabled", 1),
          ("enabled", 2),
          ("init", 65),
          ("init-enable", 3),
          ("rts", 33))
    )


_ChanParamDRI_Type.__name__ = "Integer32"
_ChanParamDRI_Object = MibTableColumn
chanParamDRI = _ChanParamDRI_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 19),
    _ChanParamDRI_Type()
)
chanParamDRI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamDRI.setStatus("mandatory")


class _ChanParamPadSignals_Type(Integer32):
    """Custom type chanParamPadSignals based on Integer32"""
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


_ChanParamPadSignals_Type.__name__ = "Integer32"
_ChanParamPadSignals_Object = MibTableColumn
chanParamPadSignals = _ChanParamPadSignals_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 20),
    _ChanParamPadSignals_Type()
)
chanParamPadSignals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamPadSignals.setStatus("mandatory")
_ChanParamBreak_Type = Integer32
_ChanParamBreak_Object = MibTableColumn
chanParamBreak = _ChanParamBreak_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 21),
    _ChanParamBreak_Type()
)
chanParamBreak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamBreak.setStatus("mandatory")


class _ChanParamPadding_Type(Integer32):
    """Custom type chanParamPadding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChanParamPadding_Type.__name__ = "Integer32"
_ChanParamPadding_Object = MibTableColumn
chanParamPadding = _ChanParamPadding_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 22),
    _ChanParamPadding_Type()
)
chanParamPadding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamPadding.setStatus("mandatory")


class _ChanParamFold_Type(Integer32):
    """Custom type chanParamFold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChanParamFold_Type.__name__ = "Integer32"
_ChanParamFold_Object = MibTableColumn
chanParamFold = _ChanParamFold_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 23),
    _ChanParamFold_Type()
)
chanParamFold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamFold.setStatus("mandatory")


class _ChanParamDRO_Type(Integer32):
    """Custom type chanParamDRO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              65,
              129)
        )
    )
    namedValues = NamedValues(
        *(("cts", 129),
          ("disabled", 1),
          ("enabled", 2),
          ("init", 65))
    )


_ChanParamDRO_Type.__name__ = "Integer32"
_ChanParamDRO_Object = MibTableColumn
chanParamDRO = _ChanParamDRO_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 24),
    _ChanParamDRO_Type()
)
chanParamDRO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamDRO.setStatus("mandatory")
_ChanParamLFI_Type = Integer32
_ChanParamLFI_Object = MibTableColumn
chanParamLFI = _ChanParamLFI_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 25),
    _ChanParamLFI_Type()
)
chanParamLFI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamLFI.setStatus("mandatory")


class _ChanParamLFPad_Type(Integer32):
    """Custom type chanParamLFPad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ChanParamLFPad_Type.__name__ = "Integer32"
_ChanParamLFPad_Object = MibTableColumn
chanParamLFPad = _ChanParamLFPad_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 26),
    _ChanParamLFPad_Type()
)
chanParamLFPad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamLFPad.setStatus("mandatory")


class _ChanParamEdit_Type(Integer32):
    """Custom type chanParamEdit based on Integer32"""
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


_ChanParamEdit_Type.__name__ = "Integer32"
_ChanParamEdit_Object = MibTableColumn
chanParamEdit = _ChanParamEdit_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 27),
    _ChanParamEdit_Type()
)
chanParamEdit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamEdit.setStatus("mandatory")


class _ChanParamCharDel_Type(Integer32):
    """Custom type chanParamCharDel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_ChanParamCharDel_Type.__name__ = "Integer32"
_ChanParamCharDel_Object = MibTableColumn
chanParamCharDel = _ChanParamCharDel_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 28),
    _ChanParamCharDel_Type()
)
chanParamCharDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamCharDel.setStatus("mandatory")


class _ChanParamBufferDel_Type(Integer32):
    """Custom type chanParamBufferDel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_ChanParamBufferDel_Type.__name__ = "Integer32"
_ChanParamBufferDel_Object = MibTableColumn
chanParamBufferDel = _ChanParamBufferDel_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 29),
    _ChanParamBufferDel_Type()
)
chanParamBufferDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamBufferDel.setStatus("mandatory")


class _ChanParamDisp_Type(Integer32):
    """Custom type chanParamDisp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_ChanParamDisp_Type.__name__ = "Integer32"
_ChanParamDisp_Object = MibTableColumn
chanParamDisp = _ChanParamDisp_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 30),
    _ChanParamDisp_Type()
)
chanParamDisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamDisp.setStatus("mandatory")


class _ChanParamEditServiceSignals_Type(Integer32):
    """Custom type chanParamEditServiceSignals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )


_ChanParamEditServiceSignals_Type.__name__ = "Integer32"
_ChanParamEditServiceSignals_Object = MibTableColumn
chanParamEditServiceSignals = _ChanParamEditServiceSignals_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 31),
    _ChanParamEditServiceSignals_Type()
)
chanParamEditServiceSignals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamEditServiceSignals.setStatus("mandatory")
_ChanParamEchoMask_Type = Integer32
_ChanParamEchoMask_Object = MibTableColumn
chanParamEchoMask = _ChanParamEchoMask_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 32),
    _ChanParamEchoMask_Type()
)
chanParamEchoMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamEchoMask.setStatus("mandatory")


class _ChanParamParityTreatment_Type(Integer32):
    """Custom type chanParamParityTreatment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_ChanParamParityTreatment_Type.__name__ = "Integer32"
_ChanParamParityTreatment_Object = MibTableColumn
chanParamParityTreatment = _ChanParamParityTreatment_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 33),
    _ChanParamParityTreatment_Type()
)
chanParamParityTreatment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamParityTreatment.setStatus("mandatory")


class _ChanParamPageWait_Type(Integer32):
    """Custom type chanParamPageWait based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChanParamPageWait_Type.__name__ = "Integer32"
_ChanParamPageWait_Object = MibTableColumn
chanParamPageWait = _ChanParamPageWait_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 34),
    _ChanParamPageWait_Type()
)
chanParamPageWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamPageWait.setStatus("mandatory")


class _ChanParamForce_Type(Integer32):
    """Custom type chanParamForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChanParamForce_Type.__name__ = "Integer32"
_ChanParamForce_Object = MibTableColumn
chanParamForce = _ChanParamForce_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 35),
    _ChanParamForce_Type()
)
chanParamForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamForce.setStatus("mandatory")


class _ChanParamBreakChar_Type(Integer32):
    """Custom type chanParamBreakChar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_ChanParamBreakChar_Type.__name__ = "Integer32"
_ChanParamBreakChar_Object = MibTableColumn
chanParamBreakChar = _ChanParamBreakChar_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 36),
    _ChanParamBreakChar_Type()
)
chanParamBreakChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamBreakChar.setStatus("mandatory")


class _ChanParamNetworkParity_Type(Integer32):
    """Custom type chanParamNetworkParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("even", 1),
          ("mark", 4),
          ("none", 0),
          ("odd", 2),
          ("spac", 8))
    )


_ChanParamNetworkParity_Type.__name__ = "Integer32"
_ChanParamNetworkParity_Object = MibTableColumn
chanParamNetworkParity = _ChanParamNetworkParity_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 37),
    _ChanParamNetworkParity_Type()
)
chanParamNetworkParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamNetworkParity.setStatus("mandatory")


class _ChanParamEscapeDelay_Type(Integer32):
    """Custom type chanParamEscapeDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ChanParamEscapeDelay_Type.__name__ = "Integer32"
_ChanParamEscapeDelay_Object = MibTableColumn
chanParamEscapeDelay = _ChanParamEscapeDelay_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 38),
    _ChanParamEscapeDelay_Type()
)
chanParamEscapeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamEscapeDelay.setStatus("mandatory")


class _ChanParamStationAddress_Type(Integer32):
    """Custom type chanParamStationAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChanParamStationAddress_Type.__name__ = "Integer32"
_ChanParamStationAddress_Object = MibTableColumn
chanParamStationAddress = _ChanParamStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 39),
    _ChanParamStationAddress_Type()
)
chanParamStationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamStationAddress.setStatus("mandatory")


class _ChanParamProvideXID_Type(Integer32):
    """Custom type chanParamProvideXID based on Integer32"""
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


_ChanParamProvideXID_Type.__name__ = "Integer32"
_ChanParamProvideXID_Object = MibTableColumn
chanParamProvideXID = _ChanParamProvideXID_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 40),
    _ChanParamProvideXID_Type()
)
chanParamProvideXID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamProvideXID.setStatus("mandatory")


class _ChanParamMode_Type(Integer32):
    """Custom type chanParamMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              9,
              17,
              32,
              33,
              65,
              81,
              97,
              129,
              193)
        )
    )
    namedValues = NamedValues(
        *(("auto", 17),
          ("auto-pull-path-push-stop", 32),
          ("data", 65),
          ("hub", 97),
          ("none", 1),
          ("path", 2),
          ("pull", 5),
          ("push", 3),
          ("resp", 129),
          ("sat", 193),
          ("stop", 9),
          ("sym", 33),
          ("wait", 81))
    )


_ChanParamMode_Type.__name__ = "Integer32"
_ChanParamMode_Object = MibTableColumn
chanParamMode = _ChanParamMode_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 41),
    _ChanParamMode_Type()
)
chanParamMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamMode.setStatus("mandatory")


class _ChanParamPortMatch_Type(Integer32):
    """Custom type chanParamPortMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              129,
              137)
        )
    )
    namedValues = NamedValues(
        *(("destination", 129),
          ("no", 1),
          ("source", 2),
          ("wild", 137))
    )


_ChanParamPortMatch_Type.__name__ = "Integer32"
_ChanParamPortMatch_Object = MibTableColumn
chanParamPortMatch = _ChanParamPortMatch_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 42),
    _ChanParamPortMatch_Type()
)
chanParamPortMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamPortMatch.setStatus("mandatory")


class _ChanParamReverseTelnetPort_Type(Integer32):
    """Custom type chanParamReverseTelnetPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_ChanParamReverseTelnetPort_Type.__name__ = "Integer32"
_ChanParamReverseTelnetPort_Object = MibTableColumn
chanParamReverseTelnetPort = _ChanParamReverseTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 43),
    _ChanParamReverseTelnetPort_Type()
)
chanParamReverseTelnetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamReverseTelnetPort.setStatus("mandatory")


class _ChanParamBroadcastFilterTimer_Type(Integer32):
    """Custom type chanParamBroadcastFilterTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12000),
    )


_ChanParamBroadcastFilterTimer_Type.__name__ = "Integer32"
_ChanParamBroadcastFilterTimer_Object = MibTableColumn
chanParamBroadcastFilterTimer = _ChanParamBroadcastFilterTimer_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 44),
    _ChanParamBroadcastFilterTimer_Type()
)
chanParamBroadcastFilterTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamBroadcastFilterTimer.setStatus("mandatory")


class _ChanParamInhibitLearning_Type(Integer32):
    """Custom type chanParamInhibitLearning based on Integer32"""
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


_ChanParamInhibitLearning_Type.__name__ = "Integer32"
_ChanParamInhibitLearning_Object = MibTableColumn
chanParamInhibitLearning = _ChanParamInhibitLearning_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 45),
    _ChanParamInhibitLearning_Type()
)
chanParamInhibitLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamInhibitLearning.setStatus("mandatory")


class _ChanParamRetainSession_Type(Integer32):
    """Custom type chanParamRetainSession based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 3),
          ("notify", 1),
          ("yes", 2))
    )


_ChanParamRetainSession_Type.__name__ = "Integer32"
_ChanParamRetainSession_Object = MibTableColumn
chanParamRetainSession = _ChanParamRetainSession_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 46),
    _ChanParamRetainSession_Type()
)
chanParamRetainSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamRetainSession.setStatus("mandatory")


class _ChanParamPrinterType_Type(Integer32):
    """Custom type chanParamPrinterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ibm", 1),
          ("none", 2))
    )


_ChanParamPrinterType_Type.__name__ = "Integer32"
_ChanParamPrinterType_Object = MibTableColumn
chanParamPrinterType = _ChanParamPrinterType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 47),
    _ChanParamPrinterType_Type()
)
chanParamPrinterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamPrinterType.setStatus("mandatory")


class _ChanParamScreenPrinter_Type(Integer32):
    """Custom type chanParamScreenPrinter based on Integer32"""
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


_ChanParamScreenPrinter_Type.__name__ = "Integer32"
_ChanParamScreenPrinter_Object = MibTableColumn
chanParamScreenPrinter = _ChanParamScreenPrinter_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 48),
    _ChanParamScreenPrinter_Type()
)
chanParamScreenPrinter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamScreenPrinter.setStatus("mandatory")


class _ChanParamLocalPrinter_Type(Integer32):
    """Custom type chanParamLocalPrinter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_ChanParamLocalPrinter_Type.__name__ = "Integer32"
_ChanParamLocalPrinter_Object = MibTableColumn
chanParamLocalPrinter = _ChanParamLocalPrinter_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 49),
    _ChanParamLocalPrinter_Type()
)
chanParamLocalPrinter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamLocalPrinter.setStatus("mandatory")


class _ChanParamBnnDsap_Type(Integer32):
    """Custom type chanParamBnnDsap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_ChanParamBnnDsap_Type.__name__ = "Integer32"
_ChanParamBnnDsap_Object = MibTableColumn
chanParamBnnDsap = _ChanParamBnnDsap_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 50),
    _ChanParamBnnDsap_Type()
)
chanParamBnnDsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamBnnDsap.setStatus("mandatory")


class _ChanParamBnnSsap_Type(Integer32):
    """Custom type chanParamBnnSsap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_ChanParamBnnSsap_Type.__name__ = "Integer32"
_ChanParamBnnSsap_Object = MibTableColumn
chanParamBnnSsap = _ChanParamBnnSsap_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 51),
    _ChanParamBnnSsap_Type()
)
chanParamBnnSsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamBnnSsap.setStatus("mandatory")


class _ChanParamBnnPuTyp_Type(Integer32):
    """Custom type chanParamBnnPuTyp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              130,
              131)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("pu2-0", 130),
          ("pu2-1", 131))
    )


_ChanParamBnnPuTyp_Type.__name__ = "Integer32"
_ChanParamBnnPuTyp_Object = MibTableColumn
chanParamBnnPuTyp = _ChanParamBnnPuTyp_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 52),
    _ChanParamBnnPuTyp_Type()
)
chanParamBnnPuTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamBnnPuTyp.setStatus("mandatory")


class _ChanParamPriority_Type(Integer32):
    """Custom type chanParamPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ChanParamPriority_Type.__name__ = "Integer32"
_ChanParamPriority_Object = MibTableColumn
chanParamPriority = _ChanParamPriority_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 4, 3, 1, 53),
    _ChanParamPriority_Type()
)
chanParamPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanParamPriority.setStatus("mandatory")
_X25File_ObjectIdentity = ObjectIdentity
x25File = _X25File_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 4, 5)
)
_X25FileSize_Type = Integer32
_X25FileSize_Object = MibScalar
x25FileSize = _X25FileSize_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 5, 1),
    _X25FileSize_Type()
)
x25FileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25FileSize.setStatus("mandatory")
_X25Table_Object = MibTable
x25Table = _X25Table_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 5, 2)
)
if mibBuilder.loadTexts:
    x25Table.setStatus("mandatory")
_X25Entry_Object = MibTableRow
x25Entry = _X25Entry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 5, 2, 1)
)
x25Entry.setIndexNames(
    (0, "SAT-MEGA-MIB", "x25Index"),
)
if mibBuilder.loadTexts:
    x25Entry.setStatus("mandatory")
_X25Index_Type = Integer32
_X25Index_Object = MibTableColumn
x25Index = _X25Index_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 5, 2, 1, 1),
    _X25Index_Type()
)
x25Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25Index.setStatus("mandatory")


class _X25Name_Type(DisplayString):
    """Custom type x25Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_X25Name_Type.__name__ = "DisplayString"
_X25Name_Object = MibTableColumn
x25Name = _X25Name_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 5, 2, 1, 2),
    _X25Name_Type()
)
x25Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Name.setStatus("mandatory")


class _X25AddressGroup_Type(Integer32):
    """Custom type x25AddressGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_X25AddressGroup_Type.__name__ = "Integer32"
_X25AddressGroup_Object = MibTableColumn
x25AddressGroup = _X25AddressGroup_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 5, 2, 1, 3),
    _X25AddressGroup_Type()
)
x25AddressGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25AddressGroup.setStatus("mandatory")


class _X25Address_Type(DisplayString):
    """Custom type x25Address based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_X25Address_Type.__name__ = "DisplayString"
_X25Address_Object = MibTableColumn
x25Address = _X25Address_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 5, 2, 1, 4),
    _X25Address_Type()
)
x25Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25Address.setStatus("mandatory")


class _X25UserData_Type(DisplayString):
    """Custom type x25UserData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_X25UserData_Type.__name__ = "DisplayString"
_X25UserData_Object = MibTableColumn
x25UserData = _X25UserData_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 5, 2, 1, 5),
    _X25UserData_Type()
)
x25UserData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25UserData.setStatus("mandatory")
_NameFile_ObjectIdentity = ObjectIdentity
nameFile = _NameFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 4, 6)
)
_NameFileSize_Type = Integer32
_NameFileSize_Object = MibScalar
nameFileSize = _NameFileSize_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 6, 1),
    _NameFileSize_Type()
)
nameFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nameFileSize.setStatus("mandatory")
_NameTable_Object = MibTable
nameTable = _NameTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 6, 2)
)
if mibBuilder.loadTexts:
    nameTable.setStatus("mandatory")
_NameEntry_Object = MibTableRow
nameEntry = _NameEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 6, 2, 1)
)
nameEntry.setIndexNames(
    (0, "SAT-MEGA-MIB", "nameIndex"),
)
if mibBuilder.loadTexts:
    nameEntry.setStatus("mandatory")
_NameIndex_Type = Integer32
_NameIndex_Object = MibTableColumn
nameIndex = _NameIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 6, 2, 1, 1),
    _NameIndex_Type()
)
nameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nameIndex.setStatus("mandatory")


class _NameName_Type(DisplayString):
    """Custom type nameName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_NameName_Type.__name__ = "DisplayString"
_NameName_Object = MibTableColumn
nameName = _NameName_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 6, 2, 1, 2),
    _NameName_Type()
)
nameName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nameName.setStatus("mandatory")


class _NameDRCMask_Type(DisplayString):
    """Custom type nameDRCMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_NameDRCMask_Type.__name__ = "DisplayString"
_NameDRCMask_Object = MibTableColumn
nameDRCMask = _NameDRCMask_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 6, 2, 1, 3),
    _NameDRCMask_Type()
)
nameDRCMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nameDRCMask.setStatus("mandatory")


class _NameCallPriority_Type(Integer32):
    """Custom type nameCallPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NameCallPriority_Type.__name__ = "Integer32"
_NameCallPriority_Object = MibTableColumn
nameCallPriority = _NameCallPriority_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 6, 2, 1, 4),
    _NameCallPriority_Type()
)
nameCallPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nameCallPriority.setStatus("mandatory")


class _NameBilling_Type(Integer32):
    """Custom type nameBilling based on Integer32"""
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


_NameBilling_Type.__name__ = "Integer32"
_NameBilling_Object = MibTableColumn
nameBilling = _NameBilling_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 6, 2, 1, 5),
    _NameBilling_Type()
)
nameBilling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nameBilling.setStatus("mandatory")


class _NameOptions_Type(Integer32):
    """Custom type nameOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              9,
              33,
              49,
              65,
              129)
        )
    )
    namedValues = NamedValues(
        *(("icl7561", 9),
          ("iso", 2),
          ("none", 1),
          ("ppp", 33),
          ("ppp-pap", 49),
          ("prof", 5),
          ("rev-teln", 129),
          ("teln", 65))
    )


_NameOptions_Type.__name__ = "Integer32"
_NameOptions_Object = MibTableColumn
nameOptions = _NameOptions_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 6, 2, 1, 6),
    _NameOptions_Type()
)
nameOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nameOptions.setStatus("mandatory")
_PassFile_ObjectIdentity = ObjectIdentity
passFile = _PassFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 4, 7)
)
_PassFileSize_Type = Integer32
_PassFileSize_Object = MibScalar
passFileSize = _PassFileSize_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 7, 1),
    _PassFileSize_Type()
)
passFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passFileSize.setStatus("mandatory")
_MacFile_ObjectIdentity = ObjectIdentity
macFile = _MacFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 4, 8)
)
_MacFileSize_Type = Integer32
_MacFileSize_Object = MibScalar
macFileSize = _MacFileSize_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 8, 1),
    _MacFileSize_Type()
)
macFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macFileSize.setStatus("mandatory")
_MacTable_Object = MibTable
macTable = _MacTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 8, 2)
)
if mibBuilder.loadTexts:
    macTable.setStatus("mandatory")
_MacEntry_Object = MibTableRow
macEntry = _MacEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 8, 2, 1)
)
macEntry.setIndexNames(
    (0, "SAT-MEGA-MIB", "macIndex"),
)
if mibBuilder.loadTexts:
    macEntry.setStatus("mandatory")
_MacIndex_Type = Integer32
_MacIndex_Object = MibTableColumn
macIndex = _MacIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 8, 2, 1, 1),
    _MacIndex_Type()
)
macIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macIndex.setStatus("mandatory")


class _MacName_Type(DisplayString):
    """Custom type macName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_MacName_Type.__name__ = "DisplayString"
_MacName_Object = MibTableColumn
macName = _MacName_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 8, 2, 1, 2),
    _MacName_Type()
)
macName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macName.setStatus("mandatory")


class _MacFunction_Type(Integer32):
    """Custom type macFunction based on Integer32"""
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
              16386,
              16387,
              16388,
              16389,
              16390,
              16391,
              16392,
              32769,
              32770,
              32771,
              32772,
              32773,
              32774,
              32775,
              32776,
              32777,
              32778,
              32781,
              32782,
              32783,
              32784,
              32785,
              32786)
        )
    )
    namedValues = NamedValues(
        *(("add", 32783),
          ("bar", 32784),
          ("cad", 2),
          ("copy", 16388),
          ("cpr", 7),
          ("cud", 4),
          ("dad", 3),
          ("data", 16391),
          ("dele", 16387),
          ("dhcp", 32786),
          ("dpr", 8),
          ("else", 5),
          ("eof", 16392),
          ("fac", 6),
          ("ibeg", 32769),
          ("iend", 32770),
          ("inse", 16386),
          ("list", 32775),
          ("mark", 16390),
          ("mask", 32776),
          ("nop", 1),
          ("nvmt", 32782),
          ("obeg", 32771),
          ("oend", 32772),
          ("posn", 16389),
          ("pu", 32773),
          ("rout", 32781),
          ("sync", 32777),
          ("tab", 32778),
          ("time", 32785),
          ("xid", 32774))
    )


_MacFunction_Type.__name__ = "Integer32"
_MacFunction_Object = MibTableColumn
macFunction = _MacFunction_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 8, 2, 1, 3),
    _MacFunction_Type()
)
macFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macFunction.setStatus("mandatory")


class _MacOptions_Type(Integer32):
    """Custom type macOptions based on Integer32"""
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
              65,
              99,
              129,
              133,
              161,
              8193)
        )
    )
    namedValues = NamedValues(
        *(("bill", 8),
          ("cad", 5),
          ("ccit-1980", 9),
          ("copy", 12),
          ("disc", 8193),
          ("expe", 10),
          ("iso", 4),
          ("jump", 11),
          ("none", 1),
          ("not", 129),
          ("rej", 2),
          ("sap", 133),
          ("talk", 7),
          ("tcal", 3),
          ("thru", 6),
          ("tlat", 99),
          ("wipx", 161),
          ("y13", 65))
    )


_MacOptions_Type.__name__ = "Integer32"
_MacOptions_Object = MibTableColumn
macOptions = _MacOptions_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 8, 2, 1, 4),
    _MacOptions_Type()
)
macOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macOptions.setStatus("mandatory")


class _MacSelector_Type(DisplayString):
    """Custom type macSelector based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MacSelector_Type.__name__ = "DisplayString"
_MacSelector_Object = MibTableColumn
macSelector = _MacSelector_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 8, 2, 1, 5),
    _MacSelector_Type()
)
macSelector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macSelector.setStatus("mandatory")


class _MacGenerator_Type(DisplayString):
    """Custom type macGenerator based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MacGenerator_Type.__name__ = "DisplayString"
_MacGenerator_Object = MibTableColumn
macGenerator = _MacGenerator_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 8, 2, 1, 6),
    _MacGenerator_Type()
)
macGenerator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macGenerator.setStatus("mandatory")
_IlanFile_ObjectIdentity = ObjectIdentity
ilanFile = _IlanFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 4, 9)
)
_IlanFileSize_Type = Integer32
_IlanFileSize_Object = MibScalar
ilanFileSize = _IlanFileSize_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 9, 1),
    _IlanFileSize_Type()
)
ilanFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilanFileSize.setStatus("mandatory")
_IlanTable_Object = MibTable
ilanTable = _IlanTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 9, 2)
)
if mibBuilder.loadTexts:
    ilanTable.setStatus("mandatory")
_IlanEntry_Object = MibTableRow
ilanEntry = _IlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 9, 2, 1)
)
ilanEntry.setIndexNames(
    (0, "SAT-MEGA-MIB", "ilanIndex"),
)
if mibBuilder.loadTexts:
    ilanEntry.setStatus("mandatory")
_IlanIndex_Type = Integer32
_IlanIndex_Object = MibTableColumn
ilanIndex = _IlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 9, 2, 1, 1),
    _IlanIndex_Type()
)
ilanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ilanIndex.setStatus("mandatory")


class _IlanName_Type(DisplayString):
    """Custom type ilanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IlanName_Type.__name__ = "DisplayString"
_IlanName_Object = MibTableColumn
ilanName = _IlanName_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 9, 2, 1, 2),
    _IlanName_Type()
)
ilanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilanName.setStatus("mandatory")


class _IlanOptions_Type(Integer32):
    """Custom type ilanOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("dbit", 4),
          ("expe", 2),
          ("iso", 1),
          ("none", 3),
          ("talk", 8),
          ("y13", 16))
    )


_IlanOptions_Type.__name__ = "Integer32"
_IlanOptions_Object = MibTableColumn
ilanOptions = _IlanOptions_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 9, 2, 1, 3),
    _IlanOptions_Type()
)
ilanOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilanOptions.setStatus("mandatory")


class _IlanEthernetAddress_Type(DisplayString):
    """Custom type ilanEthernetAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_IlanEthernetAddress_Type.__name__ = "DisplayString"
_IlanEthernetAddress_Object = MibTableColumn
ilanEthernetAddress = _IlanEthernetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 9, 2, 1, 4),
    _IlanEthernetAddress_Type()
)
ilanEthernetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilanEthernetAddress.setStatus("mandatory")


class _IlanTSAP_Type(DisplayString):
    """Custom type ilanTSAP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_IlanTSAP_Type.__name__ = "DisplayString"
_IlanTSAP_Object = MibTableColumn
ilanTSAP = _IlanTSAP_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 9, 2, 1, 5),
    _IlanTSAP_Type()
)
ilanTSAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilanTSAP.setStatus("mandatory")
_ElogFile_ObjectIdentity = ObjectIdentity
elogFile = _ElogFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 4, 10)
)
_ElogFileSize_Type = Integer32
_ElogFileSize_Object = MibScalar
elogFileSize = _ElogFileSize_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 10, 1),
    _ElogFileSize_Type()
)
elogFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elogFileSize.setStatus("mandatory")
_ElogTable_Object = MibTable
elogTable = _ElogTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 10, 2)
)
if mibBuilder.loadTexts:
    elogTable.setStatus("mandatory")
_ElogEntry_Object = MibTableRow
elogEntry = _ElogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 10, 2, 1)
)
elogEntry.setIndexNames(
    (0, "SAT-MEGA-MIB", "elogIndex"),
)
if mibBuilder.loadTexts:
    elogEntry.setStatus("mandatory")
_ElogIndex_Type = Integer32
_ElogIndex_Object = MibTableColumn
elogIndex = _ElogIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 10, 2, 1, 1),
    _ElogIndex_Type()
)
elogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elogIndex.setStatus("mandatory")


class _ElogRecord_Type(DisplayString):
    """Custom type elogRecord based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_ElogRecord_Type.__name__ = "DisplayString"
_ElogRecord_Object = MibTableColumn
elogRecord = _ElogRecord_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 10, 2, 1, 2),
    _ElogRecord_Type()
)
elogRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elogRecord.setStatus("mandatory")
_BillFile_ObjectIdentity = ObjectIdentity
billFile = _BillFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 4, 11)
)
_BillFileSize_Type = Integer32
_BillFileSize_Object = MibScalar
billFileSize = _BillFileSize_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 11, 1),
    _BillFileSize_Type()
)
billFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    billFileSize.setStatus("mandatory")
_BillTable_Object = MibTable
billTable = _BillTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 11, 2)
)
if mibBuilder.loadTexts:
    billTable.setStatus("mandatory")
_BillEntry_Object = MibTableRow
billEntry = _BillEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 11, 2, 1)
)
billEntry.setIndexNames(
    (0, "SAT-MEGA-MIB", "billIndex"),
)
if mibBuilder.loadTexts:
    billEntry.setStatus("mandatory")
_BillIndex_Type = Integer32
_BillIndex_Object = MibTableColumn
billIndex = _BillIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 11, 2, 1, 1),
    _BillIndex_Type()
)
billIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    billIndex.setStatus("mandatory")
_BillPass_Type = DisplayString
_BillPass_Object = MibTableColumn
billPass = _BillPass_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 11, 2, 1, 2),
    _BillPass_Type()
)
billPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    billPass.setStatus("mandatory")


class _BillDay_Type(Integer32):
    """Custom type billDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_BillDay_Type.__name__ = "Integer32"
_BillDay_Object = MibTableColumn
billDay = _BillDay_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 11, 2, 1, 3),
    _BillDay_Type()
)
billDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    billDay.setStatus("mandatory")


class _BillMonth_Type(Integer32):
    """Custom type billMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_BillMonth_Type.__name__ = "Integer32"
_BillMonth_Object = MibTableColumn
billMonth = _BillMonth_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 11, 2, 1, 4),
    _BillMonth_Type()
)
billMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    billMonth.setStatus("mandatory")
_BillYear_Type = Integer32
_BillYear_Object = MibTableColumn
billYear = _BillYear_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 11, 2, 1, 5),
    _BillYear_Type()
)
billYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    billYear.setStatus("mandatory")
_BillHour_Type = Integer32
_BillHour_Object = MibTableColumn
billHour = _BillHour_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 11, 2, 1, 6),
    _BillHour_Type()
)
billHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    billHour.setStatus("mandatory")
_BillMins_Type = Integer32
_BillMins_Object = MibTableColumn
billMins = _BillMins_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 11, 2, 1, 7),
    _BillMins_Type()
)
billMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    billMins.setStatus("mandatory")
_BillCause_Type = Integer32
_BillCause_Object = MibTableColumn
billCause = _BillCause_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 11, 2, 1, 8),
    _BillCause_Type()
)
billCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    billCause.setStatus("mandatory")
_BillDiagn_Type = Integer32
_BillDiagn_Object = MibTableColumn
billDiagn = _BillDiagn_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 11, 2, 1, 9),
    _BillDiagn_Type()
)
billDiagn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    billDiagn.setStatus("mandatory")
_BillRev_Type = Integer32
_BillRev_Object = MibTableColumn
billRev = _BillRev_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 11, 2, 1, 10),
    _BillRev_Type()
)
billRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    billRev.setStatus("mandatory")
_BillCallm_Type = Integer32
_BillCallm_Object = MibTableColumn
billCallm = _BillCallm_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 11, 2, 1, 11),
    _BillCallm_Type()
)
billCallm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    billCallm.setStatus("mandatory")
_BillCalls_Type = Integer32
_BillCalls_Object = MibTableColumn
billCalls = _BillCalls_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 11, 2, 1, 12),
    _BillCalls_Type()
)
billCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    billCalls.setStatus("mandatory")


class _BillCname_Type(DisplayString):
    """Custom type billCname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BillCname_Type.__name__ = "DisplayString"
_BillCname_Object = MibTableColumn
billCname = _BillCname_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 11, 2, 1, 13),
    _BillCname_Type()
)
billCname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    billCname.setStatus("mandatory")


class _BillRname_Type(DisplayString):
    """Custom type billRname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BillRname_Type.__name__ = "DisplayString"
_BillRname_Object = MibTableColumn
billRname = _BillRname_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 11, 2, 1, 14),
    _BillRname_Type()
)
billRname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    billRname.setStatus("mandatory")


class _BillPrx_Type(DisplayString):
    """Custom type billPrx based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BillPrx_Type.__name__ = "DisplayString"
_BillPrx_Object = MibTableColumn
billPrx = _BillPrx_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 11, 2, 1, 15),
    _BillPrx_Type()
)
billPrx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    billPrx.setStatus("mandatory")


class _BillPtx_Type(DisplayString):
    """Custom type billPtx based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BillPtx_Type.__name__ = "DisplayString"
_BillPtx_Object = MibTableColumn
billPtx = _BillPtx_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 11, 2, 1, 16),
    _BillPtx_Type()
)
billPtx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    billPtx.setStatus("mandatory")


class _BillCrx_Type(DisplayString):
    """Custom type billCrx based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BillCrx_Type.__name__ = "DisplayString"
_BillCrx_Object = MibTableColumn
billCrx = _BillCrx_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 11, 2, 1, 17),
    _BillCrx_Type()
)
billCrx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    billCrx.setStatus("mandatory")


class _BillCtx_Type(DisplayString):
    """Custom type billCtx based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BillCtx_Type.__name__ = "DisplayString"
_BillCtx_Object = MibTableColumn
billCtx = _BillCtx_Object(
    (1, 3, 6, 1, 4, 1, 1038, 4, 11, 2, 1, 18),
    _BillCtx_Type()
)
billCtx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    billCtx.setStatus("mandatory")

# Managed Objects groups


# Notification objects

errorLogReport = NotificationType(
    (1, 3, 6, 1, 4, 1, 1038, 0, 0)
)
if mibBuilder.loadTexts:
    errorLogReport.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SAT-MEGA-MIB",
    **{"sat": sat,
       "errorLogReport": errorLogReport,
       "mega": mega,
       "products": products,
       "megaPAC-E-cpu-C": megaPAC_E_cpu_C,
       "megaPAC-ESL": megaPAC_ESL,
       "megaPAC-E-cpu-D-E": megaPAC_E_cpu_D_E,
       "megaPAC-V-cpu-8": megaPAC_V_cpu_8,
       "megaPAC-V-cpu-16": megaPAC_V_cpu_16,
       "megaPAC-V-cpu-68040": megaPAC_V_cpu_68040,
       "megaPAC-V-cpu-68060": megaPAC_V_cpu_68060,
       "base": base,
       "baseVersion": baseVersion,
       "baseRestartTime": baseRestartTime,
       "baseMaxPacketSize": baseMaxPacketSize,
       "baseBuffPoolMax": baseBuffPoolMax,
       "baseBuffPoolNow": baseBuffPoolNow,
       "baseBufferPoolLowest": baseBufferPoolLowest,
       "baseBufferPoolEmpty": baseBufferPoolEmpty,
       "baseStatBufferThreshold": baseStatBufferThreshold,
       "baseMemorySize": baseMemorySize,
       "baseDataFramesIn": baseDataFramesIn,
       "baseDataFramesOut": baseDataFramesOut,
       "baseDataFrameRateIn": baseDataFrameRateIn,
       "baseDataFrameRateOut": baseDataFrameRateOut,
       "baseTotalCallSetUps": baseTotalCallSetUps,
       "baseCurrentCalls": baseCurrentCalls,
       "baseRetransmissions": baseRetransmissions,
       "baseRejects": baseRejects,
       "baseTotalTransportCalls": baseTotalTransportCalls,
       "baseCurrentTransportCalls": baseCurrentTransportCalls,
       "baseRunStatus": baseRunStatus,
       "baseReports": baseReports,
       "baseSessionStatistics": baseSessionStatistics,
       "baseBufferThreshold": baseBufferThreshold,
       "baseInitialPresentationTimer": baseInitialPresentationTimer,
       "baseSecondaryPresentationTimer": baseSecondaryPresentationTimer,
       "baseInactivityDetectTimer": baseInactivityDetectTimer,
       "baseSegmentAccounting": baseSegmentAccounting,
       "baseTerminalEmulationBuffers": baseTerminalEmulationBuffers,
       "baseTransportBuffers": baseTransportBuffers,
       "baseCountrySettings": baseCountrySettings,
       "baseTeleloadEnabled": baseTeleloadEnabled,
       "baseDefaultToPromCompatible": baseDefaultToPromCompatible,
       "controller": controller,
       "ctrlNumberConfigured": ctrlNumberConfigured,
       "ctrlTotalNumber": ctrlTotalNumber,
       "ctrlStatTable": ctrlStatTable,
       "ctrlStatEntry": ctrlStatEntry,
       "ctrlStatIndex": ctrlStatIndex,
       "ctrlStatName": ctrlStatName,
       "ctrlStatType": ctrlStatType,
       "ctrlStatSubType": ctrlStatSubType,
       "ctrlStatNumberChannels": ctrlStatNumberChannels,
       "ctrlStatFirstChannelIndex": ctrlStatFirstChannelIndex,
       "ctrlStatCRCErrors": ctrlStatCRCErrors,
       "ctrlStatTotalCallSetUps": ctrlStatTotalCallSetUps,
       "ctrlStatCurrentCalls": ctrlStatCurrentCalls,
       "ctrlStatDataIn": ctrlStatDataIn,
       "ctrlStatDataOut": ctrlStatDataOut,
       "ctrlStatDataFramesIn": ctrlStatDataFramesIn,
       "ctrlStatDataFramesOut": ctrlStatDataFramesOut,
       "ctrlStatDataFrameRateIn": ctrlStatDataFrameRateIn,
       "ctrlStatDataFrameRateOut": ctrlStatDataFrameRateOut,
       "ctrlStatCallsReceived": ctrlStatCallsReceived,
       "ctrlStatCallsSent": ctrlStatCallsSent,
       "ctrlStatClearsReceived": ctrlStatClearsReceived,
       "ctrlStatRetransmissions": ctrlStatRetransmissions,
       "ctrlStatRejects": ctrlStatRejects,
       "ctrlStatState": ctrlStatState,
       "ctrlStatSubState": ctrlStatSubState,
       "ctrlStatNoTries": ctrlStatNoTries,
       "ctrlStatOptions": ctrlStatOptions,
       "ctrlStatLCGN": ctrlStatLCGN,
       "ctrlStatResetsReceived": ctrlStatResetsReceived,
       "ctrlStatInterruptsReceived": ctrlStatInterruptsReceived,
       "ctrlStatOutputQueueLength": ctrlStatOutputQueueLength,
       "ctrlStatStationAddress": ctrlStatStationAddress,
       "ctrlStatDestinationAddress": ctrlStatDestinationAddress,
       "ctrlStatEIA": ctrlStatEIA,
       "ctrlStatSdlcOptions": ctrlStatSdlcOptions,
       "ctrlStatArpRequestRec": ctrlStatArpRequestRec,
       "ctrlStatArpRequestSent": ctrlStatArpRequestSent,
       "ctrlStatArpResponsesRec": ctrlStatArpResponsesRec,
       "ctrlStatFRTxSeqLost": ctrlStatFRTxSeqLost,
       "ctrlStatFRRxSeqLost": ctrlStatFRRxSeqLost,
       "ctrlStatFRCurTxSeq": ctrlStatFRCurTxSeq,
       "ctrlStatFRCurRxSeq": ctrlStatFRCurRxSeq,
       "ctrlStatFRRcvBecn": ctrlStatFRRcvBecn,
       "ctrlStatFRRcvFecn": ctrlStatFRRcvFecn,
       "ctrlStatFRThroughput": ctrlStatFRThroughput,
       "ctrlStatFRLMI": ctrlStatFRLMI,
       "ctrlStatFRrespLmi": ctrlStatFRrespLmi,
       "ctrlStatFRCurSndSeq": ctrlStatFRCurSndSeq,
       "ctrlStatFRCurRcvSeq": ctrlStatFRCurRcvSeq,
       "ctrlStatFRRcvDe": ctrlStatFRRcvDe,
       "ctrlParamTable": ctrlParamTable,
       "ctrlParamEntry": ctrlParamEntry,
       "ctrlParamIndex": ctrlParamIndex,
       "ctrlParamName": ctrlParamName,
       "ctrlParamType": ctrlParamType,
       "ctrlParamSubType": ctrlParamSubType,
       "ctrlParamNoChannels": ctrlParamNoChannels,
       "ctrlParamSpeed": ctrlParamSpeed,
       "ctrlParamInterfaceType": ctrlParamInterfaceType,
       "ctrlParamPacketSize": ctrlParamPacketSize,
       "ctrlParamV54Modem": ctrlParamV54Modem,
       "ctrlParamAddress": ctrlParamAddress,
       "ctrlParamOptions": ctrlParamOptions,
       "ctrlParamInitFrame": ctrlParamInitFrame,
       "ctrlParamT1": ctrlParamT1,
       "ctrlParamTries": ctrlParamTries,
       "ctrlParamKLevel2": ctrlParamKLevel2,
       "ctrlParamKLevel3": ctrlParamKLevel3,
       "ctrlParamLineGroup": ctrlParamLineGroup,
       "ctrlParamLCGN": ctrlParamLCGN,
       "ctrlParamLCNOffset": ctrlParamLCNOffset,
       "ctrlParamAddressGroup": ctrlParamAddressGroup,
       "ctrlParamFrameSequence": ctrlParamFrameSequence,
       "ctrlParamCallTimeOut": ctrlParamCallTimeOut,
       "ctrlParamErrorThreshold": ctrlParamErrorThreshold,
       "ctrlParamLoopBarPriority": ctrlParamLoopBarPriority,
       "ctrlParamExtendedCallMgmt": ctrlParamExtendedCallMgmt,
       "ctrlParamOptionalTimers": ctrlParamOptionalTimers,
       "ctrlParamOptionalFlags": ctrlParamOptionalFlags,
       "ctrlParamTransportLevelType": ctrlParamTransportLevelType,
       "ctrlParamTransportClass": ctrlParamTransportClass,
       "ctrlParamDefaultWindowSize": ctrlParamDefaultWindowSize,
       "ctrlParamDisableFlowControl": ctrlParamDisableFlowControl,
       "ctrlParamTSAPFormat": ctrlParamTSAPFormat,
       "ctrlParamMaximumTPDUSize": ctrlParamMaximumTPDUSize,
       "ctrlParamTTRTime": ctrlParamTTRTime,
       "ctrlParamTWRTime": ctrlParamTWRTime,
       "ctrlParamDestinationAddress": ctrlParamDestinationAddress,
       "ctrlParamDSAP": ctrlParamDSAP,
       "ctrlParamSSAP": ctrlParamSSAP,
       "ctrlParamSDLCOptions": ctrlParamSDLCOptions,
       "ctrlParamPrimaryStation": ctrlParamPrimaryStation,
       "ctrlParamIdleDetectTime": ctrlParamIdleDetectTime,
       "ctrlParamPollInterval": ctrlParamPollInterval,
       "ctrlParamDuplex": ctrlParamDuplex,
       "ctrlParamTransmitDelay": ctrlParamTransmitDelay,
       "ctrlParamSlowPollTimer": ctrlParamSlowPollTimer,
       "ctrlParamMaxCallInterval": ctrlParamMaxCallInterval,
       "ctrlParamMaxCallCycles": ctrlParamMaxCallCycles,
       "ctrlParamGroupPoll": ctrlParamGroupPoll,
       "ctrlParamDelayToRTSLow": ctrlParamDelayToRTSLow,
       "ctrlParamDelayToCTSHigh": ctrlParamDelayToCTSHigh,
       "ctrlParamInputSyncDeletion": ctrlParamInputSyncDeletion,
       "ctrlParamOutputSyncInsertion": ctrlParamOutputSyncInsertion,
       "ctrlParamDCDFilter": ctrlParamDCDFilter,
       "ctrlParamInhibitTimeFill": ctrlParamInhibitTimeFill,
       "ctrlParamDirectedBroadcasts": ctrlParamDirectedBroadcasts,
       "ctrlParamDefaultLocalPrinter": ctrlParamDefaultLocalPrinter,
       "ctrlParamNewLANInterface": ctrlParamNewLANInterface,
       "ctrlParamNewSerialInterface": ctrlParamNewSerialInterface,
       "ctrlParamDlci": ctrlParamDlci,
       "ctrlParamMode": ctrlParamMode,
       "ctrlParamLmi": ctrlParamLmi,
       "ctrlParamKeepAliveTimer": ctrlParamKeepAliveTimer,
       "ctrlParamFullStatusInterval": ctrlParamFullStatusInterval,
       "ctrlParamBandwidth": ctrlParamBandwidth,
       "ctrlParamBurstCommit": ctrlParamBurstCommit,
       "ctrlParamBurstEligibility": ctrlParamBurstEligibility,
       "ctrlParamTimerT3": ctrlParamTimerT3,
       "ctrlParamFlowControl": ctrlParamFlowControl,
       "ctrlParamConfigState": ctrlParamConfigState,
       "ctrlParamTry": ctrlParamTry,
       "channel": channel,
       "chanNumberConfigured": chanNumberConfigured,
       "chanStatTable": chanStatTable,
       "chanStatEntry": chanStatEntry,
       "chanStatIndex": chanStatIndex,
       "chanStatName": chanStatName,
       "chanStatControllerIndex": chanStatControllerIndex,
       "chanStatNameCtrlName": chanStatNameCtrlName,
       "chanStatConnectedToChannelIndex": chanStatConnectedToChannelIndex,
       "chanStatState": chanStatState,
       "chanStatSessionStatus": chanStatSessionStatus,
       "chanStatEIA": chanStatEIA,
       "chanStatTotalFramesIn": chanStatTotalFramesIn,
       "chanStatTotalFramesOut": chanStatTotalFramesOut,
       "chanStatTotalCharsIn": chanStatTotalCharsIn,
       "chanStatTotalCharsOut": chanStatTotalCharsOut,
       "chanStatTxWindow": chanStatTxWindow,
       "chanStatRxWindow": chanStatRxWindow,
       "chanStatTxSize": chanStatTxSize,
       "chanStatRxSize": chanStatRxSize,
       "chanStatCause": chanStatCause,
       "chanStatDiagnostic": chanStatDiagnostic,
       "chanStatResetCause": chanStatResetCause,
       "chanStatResetDiagnostic": chanStatResetDiagnostic,
       "chanStatResetCauseReceived": chanStatResetCauseReceived,
       "chanStatResetDiagReceived": chanStatResetDiagReceived,
       "chanStatLevel3State": chanStatLevel3State,
       "chanStatCallPriority": chanStatCallPriority,
       "chanStatResourcePriority": chanStatResourcePriority,
       "chanStatPadEnable": chanStatPadEnable,
       "chanStatPortMatch": chanStatPortMatch,
       "chanStatPrimaryStation": chanStatPrimaryStation,
       "chanStatSDLCState": chanStatSDLCState,
       "chanStatQLLCState": chanStatQLLCState,
       "chanStatSDLCTransmitState": chanStatSDLCTransmitState,
       "chanStatPolls": chanStatPolls,
       "chanStatStationAddress": chanStatStationAddress,
       "chanStatXIDIdentification": chanStatXIDIdentification,
       "chanStatTries": chanStatTries,
       "chanStatWindow": chanStatWindow,
       "chanStatLUActive": chanStatLUActive,
       "chanStatBindActive": chanStatBindActive,
       "chanStatLUType": chanStatLUType,
       "chanStatBreaksReceived": chanStatBreaksReceived,
       "chanStatFramingErrors": chanStatFramingErrors,
       "chanStatInputOverruns": chanStatInputOverruns,
       "chanStatParityErrors": chanStatParityErrors,
       "chanStatTerminalType": chanStatTerminalType,
       "chanStatCircuitType": chanStatCircuitType,
       "chanStatOptions": chanStatOptions,
       "chanStatBuffers": chanStatBuffers,
       "chanStatDiscMode": chanStatDiscMode,
       "chanStatMenuNumber": chanStatMenuNumber,
       "chanStatHelpNumber": chanStatHelpNumber,
       "chanStatNewsNumber": chanStatNewsNumber,
       "chanStatPadRecall": chanStatPadRecall,
       "chanStatEcho": chanStatEcho,
       "chanStatDataForwarding": chanStatDataForwarding,
       "chanStatDelay": chanStatDelay,
       "chanStatDRI": chanStatDRI,
       "chanStatPadSignals": chanStatPadSignals,
       "chanStatBreak": chanStatBreak,
       "chanStatPadding": chanStatPadding,
       "chanStatFold": chanStatFold,
       "chanStatDRO": chanStatDRO,
       "chanStatLFI": chanStatLFI,
       "chanStatLFPad": chanStatLFPad,
       "chanStatEdit": chanStatEdit,
       "chanStatCharDel": chanStatCharDel,
       "chanStatBufferDel": chanStatBufferDel,
       "chanStatDisp": chanStatDisp,
       "chanStatEditServiceSignals": chanStatEditServiceSignals,
       "chanStatEchoMask": chanStatEchoMask,
       "chanStatParityTreatment": chanStatParityTreatment,
       "chanStatPageWait": chanStatPageWait,
       "chanStatForce": chanStatForce,
       "chanStatBreakChar": chanStatBreakChar,
       "chanStatNetworkParity": chanStatNetworkParity,
       "chanStatEscapeDelay": chanStatEscapeDelay,
       "chanStatTransportLevelState": chanStatTransportLevelState,
       "chanStatDestTsap": chanStatDestTsap,
       "chanStatLinkState": chanStatLinkState,
       "chanStatProtocolState": chanStatProtocolState,
       "chanStatProtocol": chanStatProtocol,
       "chanStatIdentity": chanStatIdentity,
       "chanStatFrameRelayWait": chanStatFrameRelayWait,
       "chanParamTable": chanParamTable,
       "chanParamEntry": chanParamEntry,
       "chanParamIndex": chanParamIndex,
       "chanParamName": chanParamName,
       "chanParamDRCMask": chanParamDRCMask,
       "chanParamTerminalType": chanParamTerminalType,
       "chanParamCircuitType": chanParamCircuitType,
       "chanParamOptions": chanParamOptions,
       "chanParamBuffers": chanParamBuffers,
       "chanParamDiscMode": chanParamDiscMode,
       "chanParamMenuNumber": chanParamMenuNumber,
       "chanParamHelpNumber": chanParamHelpNumber,
       "chanParamNewsNumber": chanParamNewsNumber,
       "chanParamCallPriority": chanParamCallPriority,
       "chanParamResourcePriority": chanParamResourcePriority,
       "chanParamPadEnable": chanParamPadEnable,
       "chanParamPadRecall": chanParamPadRecall,
       "chanParamEcho": chanParamEcho,
       "chanParamDataForwarding": chanParamDataForwarding,
       "chanParamDelay": chanParamDelay,
       "chanParamDRI": chanParamDRI,
       "chanParamPadSignals": chanParamPadSignals,
       "chanParamBreak": chanParamBreak,
       "chanParamPadding": chanParamPadding,
       "chanParamFold": chanParamFold,
       "chanParamDRO": chanParamDRO,
       "chanParamLFI": chanParamLFI,
       "chanParamLFPad": chanParamLFPad,
       "chanParamEdit": chanParamEdit,
       "chanParamCharDel": chanParamCharDel,
       "chanParamBufferDel": chanParamBufferDel,
       "chanParamDisp": chanParamDisp,
       "chanParamEditServiceSignals": chanParamEditServiceSignals,
       "chanParamEchoMask": chanParamEchoMask,
       "chanParamParityTreatment": chanParamParityTreatment,
       "chanParamPageWait": chanParamPageWait,
       "chanParamForce": chanParamForce,
       "chanParamBreakChar": chanParamBreakChar,
       "chanParamNetworkParity": chanParamNetworkParity,
       "chanParamEscapeDelay": chanParamEscapeDelay,
       "chanParamStationAddress": chanParamStationAddress,
       "chanParamProvideXID": chanParamProvideXID,
       "chanParamMode": chanParamMode,
       "chanParamPortMatch": chanParamPortMatch,
       "chanParamReverseTelnetPort": chanParamReverseTelnetPort,
       "chanParamBroadcastFilterTimer": chanParamBroadcastFilterTimer,
       "chanParamInhibitLearning": chanParamInhibitLearning,
       "chanParamRetainSession": chanParamRetainSession,
       "chanParamPrinterType": chanParamPrinterType,
       "chanParamScreenPrinter": chanParamScreenPrinter,
       "chanParamLocalPrinter": chanParamLocalPrinter,
       "chanParamBnnDsap": chanParamBnnDsap,
       "chanParamBnnSsap": chanParamBnnSsap,
       "chanParamBnnPuTyp": chanParamBnnPuTyp,
       "chanParamPriority": chanParamPriority,
       "x25File": x25File,
       "x25FileSize": x25FileSize,
       "x25Table": x25Table,
       "x25Entry": x25Entry,
       "x25Index": x25Index,
       "x25Name": x25Name,
       "x25AddressGroup": x25AddressGroup,
       "x25Address": x25Address,
       "x25UserData": x25UserData,
       "nameFile": nameFile,
       "nameFileSize": nameFileSize,
       "nameTable": nameTable,
       "nameEntry": nameEntry,
       "nameIndex": nameIndex,
       "nameName": nameName,
       "nameDRCMask": nameDRCMask,
       "nameCallPriority": nameCallPriority,
       "nameBilling": nameBilling,
       "nameOptions": nameOptions,
       "passFile": passFile,
       "passFileSize": passFileSize,
       "macFile": macFile,
       "macFileSize": macFileSize,
       "macTable": macTable,
       "macEntry": macEntry,
       "macIndex": macIndex,
       "macName": macName,
       "macFunction": macFunction,
       "macOptions": macOptions,
       "macSelector": macSelector,
       "macGenerator": macGenerator,
       "ilanFile": ilanFile,
       "ilanFileSize": ilanFileSize,
       "ilanTable": ilanTable,
       "ilanEntry": ilanEntry,
       "ilanIndex": ilanIndex,
       "ilanName": ilanName,
       "ilanOptions": ilanOptions,
       "ilanEthernetAddress": ilanEthernetAddress,
       "ilanTSAP": ilanTSAP,
       "elogFile": elogFile,
       "elogFileSize": elogFileSize,
       "elogTable": elogTable,
       "elogEntry": elogEntry,
       "elogIndex": elogIndex,
       "elogRecord": elogRecord,
       "billFile": billFile,
       "billFileSize": billFileSize,
       "billTable": billTable,
       "billEntry": billEntry,
       "billIndex": billIndex,
       "billPass": billPass,
       "billDay": billDay,
       "billMonth": billMonth,
       "billYear": billYear,
       "billHour": billHour,
       "billMins": billMins,
       "billCause": billCause,
       "billDiagn": billDiagn,
       "billRev": billRev,
       "billCallm": billCallm,
       "billCalls": billCalls,
       "billCname": billCname,
       "billRname": billRname,
       "billPrx": billPrx,
       "billPtx": billPtx,
       "billCrx": billCrx,
       "billCtx": billCtx}
)
