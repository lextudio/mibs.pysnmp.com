# SNMP MIB module (AP553-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AP553-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:06 2024
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

(linkProbe,) = mibBuilder.importSymbols(
    "INNOVX-CORE-MIB",
    "linkProbe")

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

_ProbeConfig_ObjectIdentity = ObjectIdentity
probeConfig = _ProbeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1)
)
_ChanConfig_ObjectIdentity = ObjectIdentity
chanConfig = _ChanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 1)
)


class _LmiOperation_Type(Integer32):
    """Custom type lmiOperation based on Integer32"""
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


_LmiOperation_Type.__name__ = "Integer32"
_LmiOperation_Object = MibScalar
lmiOperation = _LmiOperation_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 1, 1),
    _LmiOperation_Type()
)
lmiOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmiOperation.setStatus("mandatory")


class _LmiDLCI_Type(Integer32):
    """Custom type lmiDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("dlci-0", 1)
    )


_LmiDLCI_Type.__name__ = "Integer32"
_LmiDLCI_Object = MibScalar
lmiDLCI = _LmiDLCI_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 1, 2),
    _LmiDLCI_Type()
)
lmiDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmiDLCI.setStatus("mandatory")


class _IpDLCI_Type(Integer32):
    """Custom type ipDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_IpDLCI_Type.__name__ = "Integer32"
_IpDLCI_Object = MibScalar
ipDLCI = _IpDLCI_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 1, 3),
    _IpDLCI_Type()
)
ipDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDLCI.setStatus("mandatory")


class _IpEncapp_Type(Integer32):
    """Custom type ipEncapp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ietf-IP", 2),
          ("rawIP", 1),
          ("snap-IP", 3))
    )


_IpEncapp_Type.__name__ = "Integer32"
_IpEncapp_Object = MibScalar
ipEncapp = _IpEncapp_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 1, 4),
    _IpEncapp_Type()
)
ipEncapp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipEncapp.setStatus("mandatory")


class _ChanAggregateRate_Type(Integer32):
    """Custom type chanAggregateRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(56000, 2048000),
    )


_ChanAggregateRate_Type.__name__ = "Integer32"
_ChanAggregateRate_Object = MibScalar
chanAggregateRate = _ChanAggregateRate_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 1, 5),
    _ChanAggregateRate_Type()
)
chanAggregateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanAggregateRate.setStatus("mandatory")
_LmiConfig_ObjectIdentity = ObjectIdentity
lmiConfig = _LmiConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 2)
)


class _LmiType_Type(Integer32):
    """Custom type lmiType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("annexA", 1),
          ("annexD", 2))
    )


_LmiType_Type.__name__ = "Integer32"
_LmiType_Object = MibScalar
lmiType = _LmiType_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 2, 1),
    _LmiType_Type()
)
lmiType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmiType.setStatus("mandatory")


class _LmiN391_Type(Integer32):
    """Custom type lmiN391 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LmiN391_Type.__name__ = "Integer32"
_LmiN391_Object = MibScalar
lmiN391 = _LmiN391_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 2, 2),
    _LmiN391_Type()
)
lmiN391.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmiN391.setStatus("mandatory")


class _LmiNet392_Type(Integer32):
    """Custom type lmiNet392 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LmiNet392_Type.__name__ = "Integer32"
_LmiNet392_Object = MibScalar
lmiNet392 = _LmiNet392_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 2, 3),
    _LmiNet392_Type()
)
lmiNet392.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmiNet392.setStatus("mandatory")


class _LmiUser392_Type(Integer32):
    """Custom type lmiUser392 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LmiUser392_Type.__name__ = "Integer32"
_LmiUser392_Object = MibScalar
lmiUser392 = _LmiUser392_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 2, 4),
    _LmiUser392_Type()
)
lmiUser392.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmiUser392.setStatus("mandatory")


class _LmiNet393_Type(Integer32):
    """Custom type lmiNet393 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LmiNet393_Type.__name__ = "Integer32"
_LmiNet393_Object = MibScalar
lmiNet393 = _LmiNet393_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 2, 5),
    _LmiNet393_Type()
)
lmiNet393.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmiNet393.setStatus("mandatory")


class _LmiUser393_Type(Integer32):
    """Custom type lmiUser393 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LmiUser393_Type.__name__ = "Integer32"
_LmiUser393_Object = MibScalar
lmiUser393 = _LmiUser393_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 2, 6),
    _LmiUser393_Type()
)
lmiUser393.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmiUser393.setStatus("mandatory")


class _T391Timer_Type(Integer32):
    """Custom type t391Timer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_T391Timer_Type.__name__ = "Integer32"
_T391Timer_Object = MibScalar
t391Timer = _T391Timer_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 2, 7),
    _T391Timer_Type()
)
t391Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t391Timer.setStatus("mandatory")


class _T392Timer_Type(Integer32):
    """Custom type t392Timer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_T392Timer_Type.__name__ = "Integer32"
_T392Timer_Object = MibScalar
t392Timer = _T392Timer_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 2, 8),
    _T392Timer_Type()
)
t392Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t392Timer.setStatus("mandatory")


class _MaxInfoLength_Type(Integer32):
    """Custom type maxInfoLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 4000),
    )


_MaxInfoLength_Type.__name__ = "Integer32"
_MaxInfoLength_Object = MibScalar
maxInfoLength = _MaxInfoLength_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 2, 9),
    _MaxInfoLength_Type()
)
maxInfoLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxInfoLength.setStatus("mandatory")
_ProFunConfig_ObjectIdentity = ObjectIdentity
proFunConfig = _ProFunConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 3)
)


class _UnitType_Type(Integer32):
    """Custom type unitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("remote", 2))
    )


_UnitType_Type.__name__ = "Integer32"
_UnitType_Object = MibScalar
unitType = _UnitType_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 3, 1),
    _UnitType_Type()
)
unitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitType.setStatus("mandatory")


class _ProbeMode_Type(Integer32):
    """Custom type probeMode based on Integer32"""
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
          ("disabled", 4),
          ("generator", 1),
          ("responder", 2))
    )


_ProbeMode_Type.__name__ = "Integer32"
_ProbeMode_Object = MibScalar
probeMode = _ProbeMode_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 3, 2),
    _ProbeMode_Type()
)
probeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probeMode.setStatus("mandatory")


class _PollPeriod_Type(Integer32):
    """Custom type pollPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_PollPeriod_Type.__name__ = "Integer32"
_PollPeriod_Object = MibScalar
pollPeriod = _PollPeriod_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 3, 3),
    _PollPeriod_Type()
)
pollPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollPeriod.setStatus("mandatory")


class _GlobalTC_Type(Integer32):
    """Custom type globalTC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_GlobalTC_Type.__name__ = "Integer32"
_GlobalTC_Object = MibScalar
globalTC = _GlobalTC_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 3, 4),
    _GlobalTC_Type()
)
globalTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalTC.setStatus("mandatory")


class _PvcCount_Type(Integer32):
    """Custom type pvcCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_PvcCount_Type.__name__ = "Integer32"
_PvcCount_Object = MibScalar
pvcCount = _PvcCount_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 3, 5),
    _PvcCount_Type()
)
pvcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcCount.setStatus("mandatory")


class _ProbeTokenSize_Type(Integer32):
    """Custom type probeTokenSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(19, 4096),
    )


_ProbeTokenSize_Type.__name__ = "Integer32"
_ProbeTokenSize_Object = MibScalar
probeTokenSize = _ProbeTokenSize_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 3, 6),
    _ProbeTokenSize_Type()
)
probeTokenSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeTokenSize.setStatus("mandatory")


class _PvcAdd_Type(Integer32):
    """Custom type pvcAdd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_PvcAdd_Type.__name__ = "Integer32"
_PvcAdd_Object = MibScalar
pvcAdd = _PvcAdd_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 3, 7),
    _PvcAdd_Type()
)
pvcAdd.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    pvcAdd.setStatus("mandatory")


class _PvcDelete_Type(Integer32):
    """Custom type pvcDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_PvcDelete_Type.__name__ = "Integer32"
_PvcDelete_Object = MibScalar
pvcDelete = _PvcDelete_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 3, 8),
    _PvcDelete_Type()
)
pvcDelete.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    pvcDelete.setStatus("mandatory")


class _PvcDiscovery_Type(Integer32):
    """Custom type pvcDiscovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("complete", 3),
          ("inProgress", 2),
          ("initiate", 1))
    )


_PvcDiscovery_Type.__name__ = "Integer32"
_PvcDiscovery_Object = MibScalar
pvcDiscovery = _PvcDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 3, 9),
    _PvcDiscovery_Type()
)
pvcDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcDiscovery.setStatus("mandatory")
_TrapConfig_ObjectIdentity = ObjectIdentity
trapConfig = _TrapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4)
)


class _PvcOperStateChangeTrapSeverity_Type(Integer32):
    """Custom type pvcOperStateChangeTrapSeverity based on Integer32"""
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
        *(("critical", 2),
          ("info", 6),
          ("inhibit", 1),
          ("major", 3),
          ("minor", 4),
          ("warning", 5))
    )


_PvcOperStateChangeTrapSeverity_Type.__name__ = "Integer32"
_PvcOperStateChangeTrapSeverity_Object = MibScalar
pvcOperStateChangeTrapSeverity = _PvcOperStateChangeTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 1),
    _PvcOperStateChangeTrapSeverity_Type()
)
pvcOperStateChangeTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcOperStateChangeTrapSeverity.setStatus("mandatory")


class _RealTimeTrapSeverity_Type(Integer32):
    """Custom type realTimeTrapSeverity based on Integer32"""
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
        *(("critical", 2),
          ("info", 6),
          ("inhibit", 1),
          ("major", 3),
          ("minor", 4),
          ("warning", 5))
    )


_RealTimeTrapSeverity_Type.__name__ = "Integer32"
_RealTimeTrapSeverity_Object = MibScalar
realTimeTrapSeverity = _RealTimeTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 2),
    _RealTimeTrapSeverity_Type()
)
realTimeTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    realTimeTrapSeverity.setStatus("mandatory")


class _RealTimeChanLoadToDCEThresh_Type(Integer32):
    """Custom type realTimeChanLoadToDCEThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RealTimeChanLoadToDCEThresh_Type.__name__ = "Integer32"
_RealTimeChanLoadToDCEThresh_Object = MibScalar
realTimeChanLoadToDCEThresh = _RealTimeChanLoadToDCEThresh_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 3),
    _RealTimeChanLoadToDCEThresh_Type()
)
realTimeChanLoadToDCEThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    realTimeChanLoadToDCEThresh.setStatus("mandatory")


class _RealTimeChanLoadToDCEThreshVar_Type(Integer32):
    """Custom type realTimeChanLoadToDCEThreshVar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RealTimeChanLoadToDCEThreshVar_Type.__name__ = "Integer32"
_RealTimeChanLoadToDCEThreshVar_Object = MibScalar
realTimeChanLoadToDCEThreshVar = _RealTimeChanLoadToDCEThreshVar_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 4),
    _RealTimeChanLoadToDCEThreshVar_Type()
)
realTimeChanLoadToDCEThreshVar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    realTimeChanLoadToDCEThreshVar.setStatus("mandatory")


class _AvgChanLoadToDCETrapSeverity_Type(Integer32):
    """Custom type avgChanLoadToDCETrapSeverity based on Integer32"""
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
        *(("critical", 2),
          ("info", 6),
          ("inhibit", 1),
          ("major", 3),
          ("minor", 4),
          ("warning", 5))
    )


_AvgChanLoadToDCETrapSeverity_Type.__name__ = "Integer32"
_AvgChanLoadToDCETrapSeverity_Object = MibScalar
avgChanLoadToDCETrapSeverity = _AvgChanLoadToDCETrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 5),
    _AvgChanLoadToDCETrapSeverity_Type()
)
avgChanLoadToDCETrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avgChanLoadToDCETrapSeverity.setStatus("mandatory")


class _AvgChanLoadToDCEThresh_Type(Integer32):
    """Custom type avgChanLoadToDCEThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AvgChanLoadToDCEThresh_Type.__name__ = "Integer32"
_AvgChanLoadToDCEThresh_Object = MibScalar
avgChanLoadToDCEThresh = _AvgChanLoadToDCEThresh_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 6),
    _AvgChanLoadToDCEThresh_Type()
)
avgChanLoadToDCEThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avgChanLoadToDCEThresh.setStatus("mandatory")


class _RealTimeChanLoadToDTEThresh_Type(Integer32):
    """Custom type realTimeChanLoadToDTEThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RealTimeChanLoadToDTEThresh_Type.__name__ = "Integer32"
_RealTimeChanLoadToDTEThresh_Object = MibScalar
realTimeChanLoadToDTEThresh = _RealTimeChanLoadToDTEThresh_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 7),
    _RealTimeChanLoadToDTEThresh_Type()
)
realTimeChanLoadToDTEThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    realTimeChanLoadToDTEThresh.setStatus("mandatory")


class _RealTimeChanLoadToDTEThreshVar_Type(Integer32):
    """Custom type realTimeChanLoadToDTEThreshVar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RealTimeChanLoadToDTEThreshVar_Type.__name__ = "Integer32"
_RealTimeChanLoadToDTEThreshVar_Object = MibScalar
realTimeChanLoadToDTEThreshVar = _RealTimeChanLoadToDTEThreshVar_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 8),
    _RealTimeChanLoadToDTEThreshVar_Type()
)
realTimeChanLoadToDTEThreshVar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    realTimeChanLoadToDTEThreshVar.setStatus("mandatory")


class _AvgChanLoadToDTETrapSeverity_Type(Integer32):
    """Custom type avgChanLoadToDTETrapSeverity based on Integer32"""
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
        *(("critical", 2),
          ("info", 6),
          ("inhibit", 1),
          ("major", 3),
          ("minor", 4),
          ("warning", 5))
    )


_AvgChanLoadToDTETrapSeverity_Type.__name__ = "Integer32"
_AvgChanLoadToDTETrapSeverity_Object = MibScalar
avgChanLoadToDTETrapSeverity = _AvgChanLoadToDTETrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 9),
    _AvgChanLoadToDTETrapSeverity_Type()
)
avgChanLoadToDTETrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avgChanLoadToDTETrapSeverity.setStatus("mandatory")


class _AvgChanLoadToDTEThresh_Type(Integer32):
    """Custom type avgChanLoadToDTEThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AvgChanLoadToDTEThresh_Type.__name__ = "Integer32"
_AvgChanLoadToDTEThresh_Object = MibScalar
avgChanLoadToDTEThresh = _AvgChanLoadToDTEThresh_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 10),
    _AvgChanLoadToDTEThresh_Type()
)
avgChanLoadToDTEThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avgChanLoadToDTEThresh.setStatus("mandatory")


class _RealTimePvcLoadToDCEThresh_Type(Integer32):
    """Custom type realTimePvcLoadToDCEThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_RealTimePvcLoadToDCEThresh_Type.__name__ = "Integer32"
_RealTimePvcLoadToDCEThresh_Object = MibScalar
realTimePvcLoadToDCEThresh = _RealTimePvcLoadToDCEThresh_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 11),
    _RealTimePvcLoadToDCEThresh_Type()
)
realTimePvcLoadToDCEThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    realTimePvcLoadToDCEThresh.setStatus("mandatory")


class _RealTimePvcLoadToDCEThreshVar_Type(Integer32):
    """Custom type realTimePvcLoadToDCEThreshVar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RealTimePvcLoadToDCEThreshVar_Type.__name__ = "Integer32"
_RealTimePvcLoadToDCEThreshVar_Object = MibScalar
realTimePvcLoadToDCEThreshVar = _RealTimePvcLoadToDCEThreshVar_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 12),
    _RealTimePvcLoadToDCEThreshVar_Type()
)
realTimePvcLoadToDCEThreshVar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    realTimePvcLoadToDCEThreshVar.setStatus("mandatory")


class _AvgPvcLoadToDCETrapSeverity_Type(Integer32):
    """Custom type avgPvcLoadToDCETrapSeverity based on Integer32"""
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
        *(("critical", 2),
          ("info", 6),
          ("inhibit", 1),
          ("major", 3),
          ("minor", 4),
          ("warning", 5))
    )


_AvgPvcLoadToDCETrapSeverity_Type.__name__ = "Integer32"
_AvgPvcLoadToDCETrapSeverity_Object = MibScalar
avgPvcLoadToDCETrapSeverity = _AvgPvcLoadToDCETrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 13),
    _AvgPvcLoadToDCETrapSeverity_Type()
)
avgPvcLoadToDCETrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avgPvcLoadToDCETrapSeverity.setStatus("mandatory")


class _AvgPvcLoadToDCEThresh_Type(Integer32):
    """Custom type avgPvcLoadToDCEThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_AvgPvcLoadToDCEThresh_Type.__name__ = "Integer32"
_AvgPvcLoadToDCEThresh_Object = MibScalar
avgPvcLoadToDCEThresh = _AvgPvcLoadToDCEThresh_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 14),
    _AvgPvcLoadToDCEThresh_Type()
)
avgPvcLoadToDCEThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avgPvcLoadToDCEThresh.setStatus("mandatory")


class _RealTimePvcLoadToDTEThresh_Type(Integer32):
    """Custom type realTimePvcLoadToDTEThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_RealTimePvcLoadToDTEThresh_Type.__name__ = "Integer32"
_RealTimePvcLoadToDTEThresh_Object = MibScalar
realTimePvcLoadToDTEThresh = _RealTimePvcLoadToDTEThresh_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 15),
    _RealTimePvcLoadToDTEThresh_Type()
)
realTimePvcLoadToDTEThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    realTimePvcLoadToDTEThresh.setStatus("mandatory")


class _RealTimePvcLoadToDTEThreshVar_Type(Integer32):
    """Custom type realTimePvcLoadToDTEThreshVar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RealTimePvcLoadToDTEThreshVar_Type.__name__ = "Integer32"
_RealTimePvcLoadToDTEThreshVar_Object = MibScalar
realTimePvcLoadToDTEThreshVar = _RealTimePvcLoadToDTEThreshVar_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 16),
    _RealTimePvcLoadToDTEThreshVar_Type()
)
realTimePvcLoadToDTEThreshVar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    realTimePvcLoadToDTEThreshVar.setStatus("mandatory")


class _AvgPvcLoadToDTETrapSeverity_Type(Integer32):
    """Custom type avgPvcLoadToDTETrapSeverity based on Integer32"""
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
        *(("critical", 2),
          ("info", 6),
          ("inhibit", 1),
          ("major", 3),
          ("minor", 4),
          ("warning", 5))
    )


_AvgPvcLoadToDTETrapSeverity_Type.__name__ = "Integer32"
_AvgPvcLoadToDTETrapSeverity_Object = MibScalar
avgPvcLoadToDTETrapSeverity = _AvgPvcLoadToDTETrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 17),
    _AvgPvcLoadToDTETrapSeverity_Type()
)
avgPvcLoadToDTETrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avgPvcLoadToDTETrapSeverity.setStatus("mandatory")


class _AvgPvcLoadToDTEThresh_Type(Integer32):
    """Custom type avgPvcLoadToDTEThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_AvgPvcLoadToDTEThresh_Type.__name__ = "Integer32"
_AvgPvcLoadToDTEThresh_Object = MibScalar
avgPvcLoadToDTEThresh = _AvgPvcLoadToDTEThresh_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 18),
    _AvgPvcLoadToDTEThresh_Type()
)
avgPvcLoadToDTEThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avgPvcLoadToDTEThresh.setStatus("mandatory")


class _RealTimePvcRoundTripDelayThresh_Type(Integer32):
    """Custom type realTimePvcRoundTripDelayThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_RealTimePvcRoundTripDelayThresh_Type.__name__ = "Integer32"
_RealTimePvcRoundTripDelayThresh_Object = MibScalar
realTimePvcRoundTripDelayThresh = _RealTimePvcRoundTripDelayThresh_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 19),
    _RealTimePvcRoundTripDelayThresh_Type()
)
realTimePvcRoundTripDelayThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    realTimePvcRoundTripDelayThresh.setStatus("mandatory")


class _RealTimePvcRoundTripDelayThreshVar_Type(Integer32):
    """Custom type realTimePvcRoundTripDelayThreshVar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RealTimePvcRoundTripDelayThreshVar_Type.__name__ = "Integer32"
_RealTimePvcRoundTripDelayThreshVar_Object = MibScalar
realTimePvcRoundTripDelayThreshVar = _RealTimePvcRoundTripDelayThreshVar_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 20),
    _RealTimePvcRoundTripDelayThreshVar_Type()
)
realTimePvcRoundTripDelayThreshVar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    realTimePvcRoundTripDelayThreshVar.setStatus("mandatory")


class _AvgPvcRoundTripDelayTrapSeverity_Type(Integer32):
    """Custom type avgPvcRoundTripDelayTrapSeverity based on Integer32"""
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
        *(("critical", 2),
          ("info", 6),
          ("inhibit", 1),
          ("major", 3),
          ("minor", 4),
          ("warning", 5))
    )


_AvgPvcRoundTripDelayTrapSeverity_Type.__name__ = "Integer32"
_AvgPvcRoundTripDelayTrapSeverity_Object = MibScalar
avgPvcRoundTripDelayTrapSeverity = _AvgPvcRoundTripDelayTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 21),
    _AvgPvcRoundTripDelayTrapSeverity_Type()
)
avgPvcRoundTripDelayTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avgPvcRoundTripDelayTrapSeverity.setStatus("mandatory")


class _AvgPvcRoundTripDelayThresh_Type(Integer32):
    """Custom type avgPvcRoundTripDelayThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_AvgPvcRoundTripDelayThresh_Type.__name__ = "Integer32"
_AvgPvcRoundTripDelayThresh_Object = MibScalar
avgPvcRoundTripDelayThresh = _AvgPvcRoundTripDelayThresh_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 22),
    _AvgPvcRoundTripDelayThresh_Type()
)
avgPvcRoundTripDelayThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avgPvcRoundTripDelayThresh.setStatus("mandatory")


class _AvgPvcNotAvailToDCETrapSeverity_Type(Integer32):
    """Custom type avgPvcNotAvailToDCETrapSeverity based on Integer32"""
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
        *(("critical", 2),
          ("info", 6),
          ("inhibit", 1),
          ("major", 3),
          ("minor", 4),
          ("warning", 5))
    )


_AvgPvcNotAvailToDCETrapSeverity_Type.__name__ = "Integer32"
_AvgPvcNotAvailToDCETrapSeverity_Object = MibScalar
avgPvcNotAvailToDCETrapSeverity = _AvgPvcNotAvailToDCETrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 23),
    _AvgPvcNotAvailToDCETrapSeverity_Type()
)
avgPvcNotAvailToDCETrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avgPvcNotAvailToDCETrapSeverity.setStatus("mandatory")


class _AvgPvcNotAvailToDCEThresh_Type(Integer32):
    """Custom type avgPvcNotAvailToDCEThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AvgPvcNotAvailToDCEThresh_Type.__name__ = "Integer32"
_AvgPvcNotAvailToDCEThresh_Object = MibScalar
avgPvcNotAvailToDCEThresh = _AvgPvcNotAvailToDCEThresh_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 24),
    _AvgPvcNotAvailToDCEThresh_Type()
)
avgPvcNotAvailToDCEThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avgPvcNotAvailToDCEThresh.setStatus("mandatory")


class _AvgPvcNotAvailToDTETrapSeverity_Type(Integer32):
    """Custom type avgPvcNotAvailToDTETrapSeverity based on Integer32"""
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
        *(("critical", 2),
          ("info", 6),
          ("inhibit", 1),
          ("major", 3),
          ("minor", 4),
          ("warning", 5))
    )


_AvgPvcNotAvailToDTETrapSeverity_Type.__name__ = "Integer32"
_AvgPvcNotAvailToDTETrapSeverity_Object = MibScalar
avgPvcNotAvailToDTETrapSeverity = _AvgPvcNotAvailToDTETrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 25),
    _AvgPvcNotAvailToDTETrapSeverity_Type()
)
avgPvcNotAvailToDTETrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avgPvcNotAvailToDTETrapSeverity.setStatus("mandatory")


class _AvgPvcNotAvailToDTEThresh_Type(Integer32):
    """Custom type avgPvcNotAvailToDTEThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AvgPvcNotAvailToDTEThresh_Type.__name__ = "Integer32"
_AvgPvcNotAvailToDTEThresh_Object = MibScalar
avgPvcNotAvailToDTEThresh = _AvgPvcNotAvailToDTEThresh_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 26),
    _AvgPvcNotAvailToDTEThresh_Type()
)
avgPvcNotAvailToDTEThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avgPvcNotAvailToDTEThresh.setStatus("mandatory")


class _AvgPvcFecnFramesTrapSeverity_Type(Integer32):
    """Custom type avgPvcFecnFramesTrapSeverity based on Integer32"""
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
        *(("critical", 2),
          ("info", 6),
          ("inhibit", 1),
          ("major", 3),
          ("minor", 4),
          ("warning", 5))
    )


_AvgPvcFecnFramesTrapSeverity_Type.__name__ = "Integer32"
_AvgPvcFecnFramesTrapSeverity_Object = MibScalar
avgPvcFecnFramesTrapSeverity = _AvgPvcFecnFramesTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 27),
    _AvgPvcFecnFramesTrapSeverity_Type()
)
avgPvcFecnFramesTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avgPvcFecnFramesTrapSeverity.setStatus("mandatory")


class _AvgPvcFecnFramesThresh_Type(Integer32):
    """Custom type avgPvcFecnFramesThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_AvgPvcFecnFramesThresh_Type.__name__ = "Integer32"
_AvgPvcFecnFramesThresh_Object = MibScalar
avgPvcFecnFramesThresh = _AvgPvcFecnFramesThresh_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 28),
    _AvgPvcFecnFramesThresh_Type()
)
avgPvcFecnFramesThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avgPvcFecnFramesThresh.setStatus("mandatory")


class _AvgPvcBecnFramesTrapSeverity_Type(Integer32):
    """Custom type avgPvcBecnFramesTrapSeverity based on Integer32"""
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
        *(("critical", 2),
          ("info", 6),
          ("inhibit", 1),
          ("major", 3),
          ("minor", 4),
          ("warning", 5))
    )


_AvgPvcBecnFramesTrapSeverity_Type.__name__ = "Integer32"
_AvgPvcBecnFramesTrapSeverity_Object = MibScalar
avgPvcBecnFramesTrapSeverity = _AvgPvcBecnFramesTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 29),
    _AvgPvcBecnFramesTrapSeverity_Type()
)
avgPvcBecnFramesTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avgPvcBecnFramesTrapSeverity.setStatus("mandatory")


class _AvgPvcBecnFramesThresh_Type(Integer32):
    """Custom type avgPvcBecnFramesThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_AvgPvcBecnFramesThresh_Type.__name__ = "Integer32"
_AvgPvcBecnFramesThresh_Object = MibScalar
avgPvcBecnFramesThresh = _AvgPvcBecnFramesThresh_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 30),
    _AvgPvcBecnFramesThresh_Type()
)
avgPvcBecnFramesThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avgPvcBecnFramesThresh.setStatus("mandatory")


class _AvgPvcCIRExceedToDTETrapSeverity_Type(Integer32):
    """Custom type avgPvcCIRExceedToDTETrapSeverity based on Integer32"""
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
        *(("critical", 2),
          ("info", 6),
          ("inhibit", 1),
          ("major", 3),
          ("minor", 4),
          ("warning", 5))
    )


_AvgPvcCIRExceedToDTETrapSeverity_Type.__name__ = "Integer32"
_AvgPvcCIRExceedToDTETrapSeverity_Object = MibScalar
avgPvcCIRExceedToDTETrapSeverity = _AvgPvcCIRExceedToDTETrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 31),
    _AvgPvcCIRExceedToDTETrapSeverity_Type()
)
avgPvcCIRExceedToDTETrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avgPvcCIRExceedToDTETrapSeverity.setStatus("mandatory")


class _AvgPvcEIRExceedToDTETrapSeverity_Type(Integer32):
    """Custom type avgPvcEIRExceedToDTETrapSeverity based on Integer32"""
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
        *(("critical", 2),
          ("info", 6),
          ("inhibit", 1),
          ("major", 3),
          ("minor", 4),
          ("warning", 5))
    )


_AvgPvcEIRExceedToDTETrapSeverity_Type.__name__ = "Integer32"
_AvgPvcEIRExceedToDTETrapSeverity_Object = MibScalar
avgPvcEIRExceedToDTETrapSeverity = _AvgPvcEIRExceedToDTETrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 32),
    _AvgPvcEIRExceedToDTETrapSeverity_Type()
)
avgPvcEIRExceedToDTETrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avgPvcEIRExceedToDTETrapSeverity.setStatus("mandatory")


class _AvgPvcLossFrameTxTrapSeverity_Type(Integer32):
    """Custom type avgPvcLossFrameTxTrapSeverity based on Integer32"""
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
        *(("critical", 2),
          ("info", 6),
          ("inhibit", 1),
          ("major", 3),
          ("minor", 4),
          ("warning", 5))
    )


_AvgPvcLossFrameTxTrapSeverity_Type.__name__ = "Integer32"
_AvgPvcLossFrameTxTrapSeverity_Object = MibScalar
avgPvcLossFrameTxTrapSeverity = _AvgPvcLossFrameTxTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 33),
    _AvgPvcLossFrameTxTrapSeverity_Type()
)
avgPvcLossFrameTxTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avgPvcLossFrameTxTrapSeverity.setStatus("mandatory")


class _AvgPvcLossFrameRxTrapSeverity_Type(Integer32):
    """Custom type avgPvcLossFrameRxTrapSeverity based on Integer32"""
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
        *(("critical", 2),
          ("info", 6),
          ("inhibit", 1),
          ("major", 3),
          ("minor", 4),
          ("warning", 5))
    )


_AvgPvcLossFrameRxTrapSeverity_Type.__name__ = "Integer32"
_AvgPvcLossFrameRxTrapSeverity_Object = MibScalar
avgPvcLossFrameRxTrapSeverity = _AvgPvcLossFrameRxTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 34),
    _AvgPvcLossFrameRxTrapSeverity_Type()
)
avgPvcLossFrameRxTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avgPvcLossFrameRxTrapSeverity.setStatus("mandatory")


class _NetworkLmiInterfaceDownTrapSeverity_Type(Integer32):
    """Custom type networkLmiInterfaceDownTrapSeverity based on Integer32"""
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
        *(("critical", 2),
          ("info", 6),
          ("inhibit", 1),
          ("major", 3),
          ("minor", 4),
          ("warning", 5))
    )


_NetworkLmiInterfaceDownTrapSeverity_Type.__name__ = "Integer32"
_NetworkLmiInterfaceDownTrapSeverity_Object = MibScalar
networkLmiInterfaceDownTrapSeverity = _NetworkLmiInterfaceDownTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 35),
    _NetworkLmiInterfaceDownTrapSeverity_Type()
)
networkLmiInterfaceDownTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkLmiInterfaceDownTrapSeverity.setStatus("mandatory")


class _UserLmiInterfaceDownTrapSeverity_Type(Integer32):
    """Custom type userLmiInterfaceDownTrapSeverity based on Integer32"""
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
        *(("critical", 2),
          ("info", 6),
          ("inhibit", 1),
          ("major", 3),
          ("minor", 4),
          ("warning", 5))
    )


_UserLmiInterfaceDownTrapSeverity_Type.__name__ = "Integer32"
_UserLmiInterfaceDownTrapSeverity_Object = MibScalar
userLmiInterfaceDownTrapSeverity = _UserLmiInterfaceDownTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 4, 36),
    _UserLmiInterfaceDownTrapSeverity_Type()
)
userLmiInterfaceDownTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userLmiInterfaceDownTrapSeverity.setStatus("mandatory")
_PvcConfig_ObjectIdentity = ObjectIdentity
pvcConfig = _PvcConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 5)
)
_PvcCirEirTable_Object = MibTable
pvcCirEirTable = _PvcCirEirTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    pvcCirEirTable.setStatus("mandatory")
_PvcCirEirEntry_Object = MibTableRow
pvcCirEirEntry = _PvcCirEirEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 5, 1, 1)
)
pvcCirEirEntry.setIndexNames(
    (0, "AP553-MIB", "pvcCirEirTableIndex"),
)
if mibBuilder.loadTexts:
    pvcCirEirEntry.setStatus("mandatory")


class _PvcCirEirTableIndex_Type(Integer32):
    """Custom type pvcCirEirTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_PvcCirEirTableIndex_Type.__name__ = "Integer32"
_PvcCirEirTableIndex_Object = MibTableColumn
pvcCirEirTableIndex = _PvcCirEirTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 5, 1, 1, 1),
    _PvcCirEirTableIndex_Type()
)
pvcCirEirTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcCirEirTableIndex.setStatus("mandatory")


class _PvcCirToDTE_Type(Integer32):
    """Custom type pvcCirToDTE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048000),
    )


_PvcCirToDTE_Type.__name__ = "Integer32"
_PvcCirToDTE_Object = MibTableColumn
pvcCirToDTE = _PvcCirToDTE_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 5, 1, 1, 2),
    _PvcCirToDTE_Type()
)
pvcCirToDTE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcCirToDTE.setStatus("mandatory")


class _PvcCirToDCE_Type(Integer32):
    """Custom type pvcCirToDCE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048000),
    )


_PvcCirToDCE_Type.__name__ = "Integer32"
_PvcCirToDCE_Object = MibTableColumn
pvcCirToDCE = _PvcCirToDCE_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 5, 1, 1, 3),
    _PvcCirToDCE_Type()
)
pvcCirToDCE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcCirToDCE.setStatus("mandatory")


class _PvcEirToDTE_Type(Integer32):
    """Custom type pvcEirToDTE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_PvcEirToDTE_Type.__name__ = "Integer32"
_PvcEirToDTE_Object = MibTableColumn
pvcEirToDTE = _PvcEirToDTE_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 5, 1, 1, 4),
    _PvcEirToDTE_Type()
)
pvcEirToDTE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcEirToDTE.setStatus("mandatory")


class _PvcEirToDCE_Type(Integer32):
    """Custom type pvcEirToDCE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048000),
    )


_PvcEirToDCE_Type.__name__ = "Integer32"
_PvcEirToDCE_Object = MibTableColumn
pvcEirToDCE = _PvcEirToDCE_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 5, 1, 1, 5),
    _PvcEirToDCE_Type()
)
pvcEirToDCE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcEirToDCE.setStatus("mandatory")


class _PvcOperation_Type(Integer32):
    """Custom type pvcOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pvcNotProbed", 1),
          ("pvcProbed", 3),
          ("pvcWaitForProbe", 2))
    )


_PvcOperation_Type.__name__ = "Integer32"
_PvcOperation_Object = MibTableColumn
pvcOperation = _PvcOperation_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 5, 1, 1, 6),
    _PvcOperation_Type()
)
pvcOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcOperation.setStatus("mandatory")


class _PvcState_Type(Integer32):
    """Custom type pvcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inactive", 2),
          ("unavailable", 1))
    )


_PvcState_Type.__name__ = "Integer32"
_PvcState_Object = MibTableColumn
pvcState = _PvcState_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 5, 1, 1, 7),
    _PvcState_Type()
)
pvcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcState.setStatus("mandatory")


class _PvcIdentifier_Type(DisplayString):
    """Custom type pvcIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PvcIdentifier_Type.__name__ = "DisplayString"
_PvcIdentifier_Object = MibTableColumn
pvcIdentifier = _PvcIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 5, 1, 1, 8),
    _PvcIdentifier_Type()
)
pvcIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcIdentifier.setStatus("mandatory")
_ProbeVersion_ObjectIdentity = ObjectIdentity
probeVersion = _ProbeVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 6)
)


class _FrProbeMIBversion_Type(DisplayString):
    """Custom type frProbeMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_FrProbeMIBversion_Type.__name__ = "DisplayString"
_FrProbeMIBversion_Object = MibScalar
frProbeMIBversion = _FrProbeMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 1, 6, 1),
    _FrProbeMIBversion_Type()
)
frProbeMIBversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frProbeMIBversion.setStatus("mandatory")
_ProbeStat_ObjectIdentity = ObjectIdentity
probeStat = _ProbeStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2)
)
_ChStCurrent_ObjectIdentity = ObjectIdentity
chStCurrent = _ChStCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 1)
)
_ChCurrDteFrames_Type = Counter32
_ChCurrDteFrames_Object = MibScalar
chCurrDteFrames = _ChCurrDteFrames_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 1, 1),
    _ChCurrDteFrames_Type()
)
chCurrDteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCurrDteFrames.setStatus("mandatory")
_ChCurrDceFrames_Type = Counter32
_ChCurrDceFrames_Object = MibScalar
chCurrDceFrames = _ChCurrDceFrames_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 1, 2),
    _ChCurrDceFrames_Type()
)
chCurrDceFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCurrDceFrames.setStatus("mandatory")
_ChCurrDteOctets_Type = Counter32
_ChCurrDteOctets_Object = MibScalar
chCurrDteOctets = _ChCurrDteOctets_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 1, 3),
    _ChCurrDteOctets_Type()
)
chCurrDteOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCurrDteOctets.setStatus("mandatory")
_ChCurrDceOctets_Type = Counter32
_ChCurrDceOctets_Object = MibScalar
chCurrDceOctets = _ChCurrDceOctets_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 1, 4),
    _ChCurrDceOctets_Type()
)
chCurrDceOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCurrDceOctets.setStatus("mandatory")
_ChCurrLmiTxEnq_Type = Counter32
_ChCurrLmiTxEnq_Object = MibScalar
chCurrLmiTxEnq = _ChCurrLmiTxEnq_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 1, 5),
    _ChCurrLmiTxEnq_Type()
)
chCurrLmiTxEnq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCurrLmiTxEnq.setStatus("mandatory")
_ChCurrLmiTxResp_Type = Counter32
_ChCurrLmiTxResp_Object = MibScalar
chCurrLmiTxResp = _ChCurrLmiTxResp_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 1, 6),
    _ChCurrLmiTxResp_Type()
)
chCurrLmiTxResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCurrLmiTxResp.setStatus("mandatory")
_ChCurrLmiRxEnq_Type = Counter32
_ChCurrLmiRxEnq_Object = MibScalar
chCurrLmiRxEnq = _ChCurrLmiRxEnq_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 1, 7),
    _ChCurrLmiRxEnq_Type()
)
chCurrLmiRxEnq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCurrLmiRxEnq.setStatus("mandatory")
_ChCurrLmiRxResp_Type = Counter32
_ChCurrLmiRxResp_Object = MibScalar
chCurrLmiRxResp = _ChCurrLmiRxResp_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 1, 8),
    _ChCurrLmiRxResp_Type()
)
chCurrLmiRxResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCurrLmiRxResp.setStatus("mandatory")
_ChCurrDTELmiTimeout_Type = Counter32
_ChCurrDTELmiTimeout_Object = MibScalar
chCurrDTELmiTimeout = _ChCurrDTELmiTimeout_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 1, 9),
    _ChCurrDTELmiTimeout_Type()
)
chCurrDTELmiTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCurrDTELmiTimeout.setStatus("mandatory")
_ChCurrDCELmiTimeout_Type = Counter32
_ChCurrDCELmiTimeout_Object = MibScalar
chCurrDCELmiTimeout = _ChCurrDCELmiTimeout_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 1, 10),
    _ChCurrDCELmiTimeout_Type()
)
chCurrDCELmiTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCurrDCELmiTimeout.setStatus("mandatory")
_ChCurrFecnFrames_Type = Counter32
_ChCurrFecnFrames_Object = MibScalar
chCurrFecnFrames = _ChCurrFecnFrames_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 1, 11),
    _ChCurrFecnFrames_Type()
)
chCurrFecnFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCurrFecnFrames.setStatus("mandatory")
_ChCurrBecnFrames_Type = Counter32
_ChCurrBecnFrames_Object = MibScalar
chCurrBecnFrames = _ChCurrBecnFrames_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 1, 12),
    _ChCurrBecnFrames_Type()
)
chCurrBecnFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCurrBecnFrames.setStatus("mandatory")
_ChCurrTxIp_Type = Counter32
_ChCurrTxIp_Object = MibScalar
chCurrTxIp = _ChCurrTxIp_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 1, 13),
    _ChCurrTxIp_Type()
)
chCurrTxIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCurrTxIp.setStatus("mandatory")
_ChCurrRxIp_Type = Counter32
_ChCurrRxIp_Object = MibScalar
chCurrRxIp = _ChCurrRxIp_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 1, 14),
    _ChCurrRxIp_Type()
)
chCurrRxIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCurrRxIp.setStatus("mandatory")
_ChCurrTxPoll_Type = Counter32
_ChCurrTxPoll_Object = MibScalar
chCurrTxPoll = _ChCurrTxPoll_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 1, 15),
    _ChCurrTxPoll_Type()
)
chCurrTxPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCurrTxPoll.setStatus("mandatory")
_ChCurrTxResp_Type = Counter32
_ChCurrTxResp_Object = MibScalar
chCurrTxResp = _ChCurrTxResp_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 1, 16),
    _ChCurrTxResp_Type()
)
chCurrTxResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCurrTxResp.setStatus("mandatory")
_ChCurrRxPoll_Type = Counter32
_ChCurrRxPoll_Object = MibScalar
chCurrRxPoll = _ChCurrRxPoll_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 1, 17),
    _ChCurrRxPoll_Type()
)
chCurrRxPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCurrRxPoll.setStatus("mandatory")
_ChCurrRxResp_Type = Counter32
_ChCurrRxResp_Object = MibScalar
chCurrRxResp = _ChCurrRxResp_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 1, 18),
    _ChCurrRxResp_Type()
)
chCurrRxResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCurrRxResp.setStatus("mandatory")


class _IntervalComplete_Type(Integer32):
    """Custom type intervalComplete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_IntervalComplete_Type.__name__ = "Integer32"
_IntervalComplete_Object = MibScalar
intervalComplete = _IntervalComplete_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 1, 19),
    _IntervalComplete_Type()
)
intervalComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intervalComplete.setStatus("mandatory")
_ChStIntervalTable_Object = MibTable
chStIntervalTable = _ChStIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    chStIntervalTable.setStatus("mandatory")
_ChStIntervalEntry_Object = MibTableRow
chStIntervalEntry = _ChStIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 2, 1)
)
chStIntervalEntry.setIndexNames(
    (0, "AP553-MIB", "chIntvIndex"),
)
if mibBuilder.loadTexts:
    chStIntervalEntry.setStatus("mandatory")


class _ChIntvIndex_Type(Integer32):
    """Custom type chIntvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_ChIntvIndex_Type.__name__ = "Integer32"
_ChIntvIndex_Object = MibTableColumn
chIntvIndex = _ChIntvIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 2, 1, 1),
    _ChIntvIndex_Type()
)
chIntvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chIntvIndex.setStatus("mandatory")
_ChIntvDteFrames_Type = Counter32
_ChIntvDteFrames_Object = MibTableColumn
chIntvDteFrames = _ChIntvDteFrames_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 2, 1, 2),
    _ChIntvDteFrames_Type()
)
chIntvDteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chIntvDteFrames.setStatus("mandatory")
_ChIntvDceFrames_Type = Counter32
_ChIntvDceFrames_Object = MibTableColumn
chIntvDceFrames = _ChIntvDceFrames_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 2, 1, 3),
    _ChIntvDceFrames_Type()
)
chIntvDceFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chIntvDceFrames.setStatus("mandatory")
_ChIntvDteOctets_Type = Counter32
_ChIntvDteOctets_Object = MibTableColumn
chIntvDteOctets = _ChIntvDteOctets_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 2, 1, 4),
    _ChIntvDteOctets_Type()
)
chIntvDteOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chIntvDteOctets.setStatus("mandatory")
_ChIntvDceOctets_Type = Counter32
_ChIntvDceOctets_Object = MibTableColumn
chIntvDceOctets = _ChIntvDceOctets_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 2, 1, 5),
    _ChIntvDceOctets_Type()
)
chIntvDceOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chIntvDceOctets.setStatus("mandatory")
_ChIntvLmiTxEnq_Type = Counter32
_ChIntvLmiTxEnq_Object = MibTableColumn
chIntvLmiTxEnq = _ChIntvLmiTxEnq_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 2, 1, 6),
    _ChIntvLmiTxEnq_Type()
)
chIntvLmiTxEnq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chIntvLmiTxEnq.setStatus("mandatory")
_ChIntvLmiTxResp_Type = Counter32
_ChIntvLmiTxResp_Object = MibTableColumn
chIntvLmiTxResp = _ChIntvLmiTxResp_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 2, 1, 7),
    _ChIntvLmiTxResp_Type()
)
chIntvLmiTxResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chIntvLmiTxResp.setStatus("mandatory")
_ChIntvLmiRxEnq_Type = Counter32
_ChIntvLmiRxEnq_Object = MibTableColumn
chIntvLmiRxEnq = _ChIntvLmiRxEnq_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 2, 1, 8),
    _ChIntvLmiRxEnq_Type()
)
chIntvLmiRxEnq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chIntvLmiRxEnq.setStatus("mandatory")
_ChIntvLmiRxResp_Type = Counter32
_ChIntvLmiRxResp_Object = MibTableColumn
chIntvLmiRxResp = _ChIntvLmiRxResp_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 2, 1, 9),
    _ChIntvLmiRxResp_Type()
)
chIntvLmiRxResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chIntvLmiRxResp.setStatus("mandatory")
_ChIntvDTELmiTimeout_Type = Counter32
_ChIntvDTELmiTimeout_Object = MibTableColumn
chIntvDTELmiTimeout = _ChIntvDTELmiTimeout_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 2, 1, 10),
    _ChIntvDTELmiTimeout_Type()
)
chIntvDTELmiTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chIntvDTELmiTimeout.setStatus("mandatory")
_ChIntvDCELmiTimeout_Type = Counter32
_ChIntvDCELmiTimeout_Object = MibTableColumn
chIntvDCELmiTimeout = _ChIntvDCELmiTimeout_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 2, 1, 11),
    _ChIntvDCELmiTimeout_Type()
)
chIntvDCELmiTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chIntvDCELmiTimeout.setStatus("mandatory")
_ChIntvFecnFrames_Type = Counter32
_ChIntvFecnFrames_Object = MibTableColumn
chIntvFecnFrames = _ChIntvFecnFrames_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 2, 1, 12),
    _ChIntvFecnFrames_Type()
)
chIntvFecnFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chIntvFecnFrames.setStatus("mandatory")
_ChIntvBecnFrames_Type = Counter32
_ChIntvBecnFrames_Object = MibTableColumn
chIntvBecnFrames = _ChIntvBecnFrames_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 2, 1, 13),
    _ChIntvBecnFrames_Type()
)
chIntvBecnFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chIntvBecnFrames.setStatus("mandatory")
_ChIntvTxIp_Type = Counter32
_ChIntvTxIp_Object = MibTableColumn
chIntvTxIp = _ChIntvTxIp_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 2, 1, 14),
    _ChIntvTxIp_Type()
)
chIntvTxIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chIntvTxIp.setStatus("mandatory")
_ChIntvRxIp_Type = Counter32
_ChIntvRxIp_Object = MibTableColumn
chIntvRxIp = _ChIntvRxIp_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 2, 1, 15),
    _ChIntvRxIp_Type()
)
chIntvRxIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chIntvRxIp.setStatus("mandatory")
_ChIntvTxPoll_Type = Counter32
_ChIntvTxPoll_Object = MibTableColumn
chIntvTxPoll = _ChIntvTxPoll_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 2, 1, 16),
    _ChIntvTxPoll_Type()
)
chIntvTxPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chIntvTxPoll.setStatus("mandatory")
_ChIntvTxResp_Type = Counter32
_ChIntvTxResp_Object = MibTableColumn
chIntvTxResp = _ChIntvTxResp_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 2, 1, 17),
    _ChIntvTxResp_Type()
)
chIntvTxResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chIntvTxResp.setStatus("mandatory")
_ChIntvRxPoll_Type = Counter32
_ChIntvRxPoll_Object = MibTableColumn
chIntvRxPoll = _ChIntvRxPoll_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 2, 1, 18),
    _ChIntvRxPoll_Type()
)
chIntvRxPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chIntvRxPoll.setStatus("mandatory")
_ChIntvRxResp_Type = Counter32
_ChIntvRxResp_Object = MibTableColumn
chIntvRxResp = _ChIntvRxResp_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 2, 1, 19),
    _ChIntvRxResp_Type()
)
chIntvRxResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chIntvRxResp.setStatus("mandatory")
_PvcStCurrentTable_Object = MibTable
pvcStCurrentTable = _PvcStCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    pvcStCurrentTable.setStatus("mandatory")
_PvcStCurrentEntry_Object = MibTableRow
pvcStCurrentEntry = _PvcStCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 3, 1)
)
pvcStCurrentEntry.setIndexNames(
    (0, "AP553-MIB", "pvcCurrDlciIndex"),
)
if mibBuilder.loadTexts:
    pvcStCurrentEntry.setStatus("mandatory")


class _PvcCurrDlciIndex_Type(Integer32):
    """Custom type pvcCurrDlciIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_PvcCurrDlciIndex_Type.__name__ = "Integer32"
_PvcCurrDlciIndex_Object = MibTableColumn
pvcCurrDlciIndex = _PvcCurrDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 3, 1, 1),
    _PvcCurrDlciIndex_Type()
)
pvcCurrDlciIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcCurrDlciIndex.setStatus("mandatory")
_PvcCurrDteFrames_Type = Counter32
_PvcCurrDteFrames_Object = MibTableColumn
pvcCurrDteFrames = _PvcCurrDteFrames_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 3, 1, 2),
    _PvcCurrDteFrames_Type()
)
pvcCurrDteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcCurrDteFrames.setStatus("mandatory")
_PvcCurrDceFrames_Type = Counter32
_PvcCurrDceFrames_Object = MibTableColumn
pvcCurrDceFrames = _PvcCurrDceFrames_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 3, 1, 3),
    _PvcCurrDceFrames_Type()
)
pvcCurrDceFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcCurrDceFrames.setStatus("mandatory")
_PvcCurrDteOctets_Type = Counter32
_PvcCurrDteOctets_Object = MibTableColumn
pvcCurrDteOctets = _PvcCurrDteOctets_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 3, 1, 4),
    _PvcCurrDteOctets_Type()
)
pvcCurrDteOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcCurrDteOctets.setStatus("mandatory")
_PvcCurrDceOctets_Type = Counter32
_PvcCurrDceOctets_Object = MibTableColumn
pvcCurrDceOctets = _PvcCurrDceOctets_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 3, 1, 5),
    _PvcCurrDceOctets_Type()
)
pvcCurrDceOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcCurrDceOctets.setStatus("mandatory")
_PvcCurrDteFramesWithDE_Type = Counter32
_PvcCurrDteFramesWithDE_Object = MibTableColumn
pvcCurrDteFramesWithDE = _PvcCurrDteFramesWithDE_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 3, 1, 6),
    _PvcCurrDteFramesWithDE_Type()
)
pvcCurrDteFramesWithDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcCurrDteFramesWithDE.setStatus("mandatory")
_PvcCurrDceFramesWithDE_Type = Counter32
_PvcCurrDceFramesWithDE_Object = MibTableColumn
pvcCurrDceFramesWithDE = _PvcCurrDceFramesWithDE_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 3, 1, 7),
    _PvcCurrDceFramesWithDE_Type()
)
pvcCurrDceFramesWithDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcCurrDceFramesWithDE.setStatus("mandatory")
_PvcCurrFecnFrames_Type = Counter32
_PvcCurrFecnFrames_Object = MibTableColumn
pvcCurrFecnFrames = _PvcCurrFecnFrames_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 3, 1, 8),
    _PvcCurrFecnFrames_Type()
)
pvcCurrFecnFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcCurrFecnFrames.setStatus("mandatory")
_PvcCurrBecnFrames_Type = Counter32
_PvcCurrBecnFrames_Object = MibTableColumn
pvcCurrBecnFrames = _PvcCurrBecnFrames_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 3, 1, 9),
    _PvcCurrBecnFrames_Type()
)
pvcCurrBecnFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcCurrBecnFrames.setStatus("mandatory")
_PvcCurrTxPoll_Type = Counter32
_PvcCurrTxPoll_Object = MibTableColumn
pvcCurrTxPoll = _PvcCurrTxPoll_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 3, 1, 10),
    _PvcCurrTxPoll_Type()
)
pvcCurrTxPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcCurrTxPoll.setStatus("mandatory")
_PvcCurrTxResp_Type = Counter32
_PvcCurrTxResp_Object = MibTableColumn
pvcCurrTxResp = _PvcCurrTxResp_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 3, 1, 11),
    _PvcCurrTxResp_Type()
)
pvcCurrTxResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcCurrTxResp.setStatus("mandatory")
_PvcCurrRxPoll_Type = Counter32
_PvcCurrRxPoll_Object = MibTableColumn
pvcCurrRxPoll = _PvcCurrRxPoll_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 3, 1, 12),
    _PvcCurrRxPoll_Type()
)
pvcCurrRxPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcCurrRxPoll.setStatus("mandatory")
_PvcCurrRxResp_Type = Counter32
_PvcCurrRxResp_Object = MibTableColumn
pvcCurrRxResp = _PvcCurrRxResp_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 3, 1, 13),
    _PvcCurrRxResp_Type()
)
pvcCurrRxResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcCurrRxResp.setStatus("mandatory")


class _PvcCurrLoopback_Type(Integer32):
    """Custom type pvcCurrLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopback", 1),
          ("noLoopback", 2))
    )


_PvcCurrLoopback_Type.__name__ = "Integer32"
_PvcCurrLoopback_Object = MibTableColumn
pvcCurrLoopback = _PvcCurrLoopback_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 3, 1, 14),
    _PvcCurrLoopback_Type()
)
pvcCurrLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcCurrLoopback.setStatus("mandatory")
_PvcStIntervalTable_Object = MibTable
pvcStIntervalTable = _PvcStIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    pvcStIntervalTable.setStatus("mandatory")
_PvcStIntervalEntry_Object = MibTableRow
pvcStIntervalEntry = _PvcStIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 4, 1)
)
pvcStIntervalEntry.setIndexNames(
    (0, "AP553-MIB", "pvcIntvDlciIndex"),
    (0, "AP553-MIB", "pvcIntvIndex"),
)
if mibBuilder.loadTexts:
    pvcStIntervalEntry.setStatus("mandatory")


class _PvcIntvDlciIndex_Type(Integer32):
    """Custom type pvcIntvDlciIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_PvcIntvDlciIndex_Type.__name__ = "Integer32"
_PvcIntvDlciIndex_Object = MibTableColumn
pvcIntvDlciIndex = _PvcIntvDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 4, 1, 1),
    _PvcIntvDlciIndex_Type()
)
pvcIntvDlciIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcIntvDlciIndex.setStatus("mandatory")


class _PvcIntvIndex_Type(Integer32):
    """Custom type pvcIntvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PvcIntvIndex_Type.__name__ = "Integer32"
_PvcIntvIndex_Object = MibTableColumn
pvcIntvIndex = _PvcIntvIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 4, 1, 2),
    _PvcIntvIndex_Type()
)
pvcIntvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcIntvIndex.setStatus("mandatory")
_PvcIntvDteFrames_Type = Counter32
_PvcIntvDteFrames_Object = MibTableColumn
pvcIntvDteFrames = _PvcIntvDteFrames_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 4, 1, 3),
    _PvcIntvDteFrames_Type()
)
pvcIntvDteFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcIntvDteFrames.setStatus("mandatory")
_PvcIntvDceFrames_Type = Counter32
_PvcIntvDceFrames_Object = MibTableColumn
pvcIntvDceFrames = _PvcIntvDceFrames_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 4, 1, 4),
    _PvcIntvDceFrames_Type()
)
pvcIntvDceFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcIntvDceFrames.setStatus("mandatory")
_PvcIntvDteOctets_Type = Counter32
_PvcIntvDteOctets_Object = MibTableColumn
pvcIntvDteOctets = _PvcIntvDteOctets_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 4, 1, 5),
    _PvcIntvDteOctets_Type()
)
pvcIntvDteOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcIntvDteOctets.setStatus("mandatory")
_PvcIntvDceOctets_Type = Counter32
_PvcIntvDceOctets_Object = MibTableColumn
pvcIntvDceOctets = _PvcIntvDceOctets_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 4, 1, 6),
    _PvcIntvDceOctets_Type()
)
pvcIntvDceOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcIntvDceOctets.setStatus("mandatory")
_PvcIntvDteFramesWithDE_Type = Counter32
_PvcIntvDteFramesWithDE_Object = MibTableColumn
pvcIntvDteFramesWithDE = _PvcIntvDteFramesWithDE_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 4, 1, 7),
    _PvcIntvDteFramesWithDE_Type()
)
pvcIntvDteFramesWithDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcIntvDteFramesWithDE.setStatus("mandatory")
_PvcIntvDceFramesWithDE_Type = Counter32
_PvcIntvDceFramesWithDE_Object = MibTableColumn
pvcIntvDceFramesWithDE = _PvcIntvDceFramesWithDE_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 4, 1, 8),
    _PvcIntvDceFramesWithDE_Type()
)
pvcIntvDceFramesWithDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcIntvDceFramesWithDE.setStatus("mandatory")
_PvcIntvFecnFrames_Type = Counter32
_PvcIntvFecnFrames_Object = MibTableColumn
pvcIntvFecnFrames = _PvcIntvFecnFrames_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 4, 1, 9),
    _PvcIntvFecnFrames_Type()
)
pvcIntvFecnFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcIntvFecnFrames.setStatus("mandatory")
_PvcIntvBecnFrames_Type = Counter32
_PvcIntvBecnFrames_Object = MibTableColumn
pvcIntvBecnFrames = _PvcIntvBecnFrames_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 4, 1, 10),
    _PvcIntvBecnFrames_Type()
)
pvcIntvBecnFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcIntvBecnFrames.setStatus("mandatory")
_PvcIntvTxPoll_Type = Counter32
_PvcIntvTxPoll_Object = MibTableColumn
pvcIntvTxPoll = _PvcIntvTxPoll_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 4, 1, 11),
    _PvcIntvTxPoll_Type()
)
pvcIntvTxPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcIntvTxPoll.setStatus("mandatory")
_PvcIntvTxResp_Type = Counter32
_PvcIntvTxResp_Object = MibTableColumn
pvcIntvTxResp = _PvcIntvTxResp_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 4, 1, 12),
    _PvcIntvTxResp_Type()
)
pvcIntvTxResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcIntvTxResp.setStatus("mandatory")
_PvcIntvRxPoll_Type = Counter32
_PvcIntvRxPoll_Object = MibTableColumn
pvcIntvRxPoll = _PvcIntvRxPoll_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 4, 1, 13),
    _PvcIntvRxPoll_Type()
)
pvcIntvRxPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcIntvRxPoll.setStatus("mandatory")
_PvcIntvRxResp_Type = Counter32
_PvcIntvRxResp_Object = MibTableColumn
pvcIntvRxResp = _PvcIntvRxResp_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 4, 1, 14),
    _PvcIntvRxResp_Type()
)
pvcIntvRxResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcIntvRxResp.setStatus("mandatory")


class _PvcIntvLoopback_Type(Integer32):
    """Custom type pvcIntvLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopback", 1),
          ("noLoopback", 2))
    )


_PvcIntvLoopback_Type.__name__ = "Integer32"
_PvcIntvLoopback_Object = MibTableColumn
pvcIntvLoopback = _PvcIntvLoopback_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 2, 4, 1, 15),
    _PvcIntvLoopback_Type()
)
pvcIntvLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcIntvLoopback.setStatus("mandatory")
_ProbePerform_ObjectIdentity = ObjectIdentity
probePerform = _ProbePerform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3)
)
_ChanPerfCurr_ObjectIdentity = ObjectIdentity
chanPerfCurr = _ChanPerfCurr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 1)
)
_ChPerfCurrUnavailToDte_Type = Integer32
_ChPerfCurrUnavailToDte_Object = MibScalar
chPerfCurrUnavailToDte = _ChPerfCurrUnavailToDte_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 1, 1),
    _ChPerfCurrUnavailToDte_Type()
)
chPerfCurrUnavailToDte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPerfCurrUnavailToDte.setStatus("mandatory")
_ChPerfCurrUnavailToDce_Type = Integer32
_ChPerfCurrUnavailToDce_Object = MibScalar
chPerfCurrUnavailToDce = _ChPerfCurrUnavailToDce_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 1, 2),
    _ChPerfCurrUnavailToDce_Type()
)
chPerfCurrUnavailToDce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPerfCurrUnavailToDce.setStatus("mandatory")
_ChPerfCurrTxLoad_Type = Integer32
_ChPerfCurrTxLoad_Object = MibScalar
chPerfCurrTxLoad = _ChPerfCurrTxLoad_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 1, 3),
    _ChPerfCurrTxLoad_Type()
)
chPerfCurrTxLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPerfCurrTxLoad.setStatus("mandatory")
_ChPerfCurrRxLoad_Type = Integer32
_ChPerfCurrRxLoad_Object = MibScalar
chPerfCurrRxLoad = _ChPerfCurrRxLoad_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 1, 4),
    _ChPerfCurrRxLoad_Type()
)
chPerfCurrRxLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPerfCurrRxLoad.setStatus("mandatory")
_ChPerfCurrTotalTxLoad_Type = Integer32
_ChPerfCurrTotalTxLoad_Object = MibScalar
chPerfCurrTotalTxLoad = _ChPerfCurrTotalTxLoad_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 1, 5),
    _ChPerfCurrTotalTxLoad_Type()
)
chPerfCurrTotalTxLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPerfCurrTotalTxLoad.setStatus("mandatory")
_ChPerfCurrTotalRxLoad_Type = Integer32
_ChPerfCurrTotalRxLoad_Object = MibScalar
chPerfCurrTotalRxLoad = _ChPerfCurrTotalRxLoad_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 1, 6),
    _ChPerfCurrTotalRxLoad_Type()
)
chPerfCurrTotalRxLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPerfCurrTotalRxLoad.setStatus("mandatory")
_ChPerfCurrLoadToDceRealTime_Type = Integer32
_ChPerfCurrLoadToDceRealTime_Object = MibScalar
chPerfCurrLoadToDceRealTime = _ChPerfCurrLoadToDceRealTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 1, 7),
    _ChPerfCurrLoadToDceRealTime_Type()
)
chPerfCurrLoadToDceRealTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPerfCurrLoadToDceRealTime.setStatus("mandatory")
_ChPerfCurrLoadToDteRealTime_Type = Integer32
_ChPerfCurrLoadToDteRealTime_Object = MibScalar
chPerfCurrLoadToDteRealTime = _ChPerfCurrLoadToDteRealTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 1, 8),
    _ChPerfCurrLoadToDteRealTime_Type()
)
chPerfCurrLoadToDteRealTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPerfCurrLoadToDteRealTime.setStatus("mandatory")
_ChanPerfIntvTable_Object = MibTable
chanPerfIntvTable = _ChanPerfIntvTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    chanPerfIntvTable.setStatus("mandatory")
_ChanPerfIntvEntry_Object = MibTableRow
chanPerfIntvEntry = _ChanPerfIntvEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 2, 1)
)
chanPerfIntvEntry.setIndexNames(
    (0, "AP553-MIB", "chPerfIntvIndex"),
)
if mibBuilder.loadTexts:
    chanPerfIntvEntry.setStatus("mandatory")


class _ChPerfIntvIndex_Type(Integer32):
    """Custom type chPerfIntvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_ChPerfIntvIndex_Type.__name__ = "Integer32"
_ChPerfIntvIndex_Object = MibTableColumn
chPerfIntvIndex = _ChPerfIntvIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 2, 1, 1),
    _ChPerfIntvIndex_Type()
)
chPerfIntvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPerfIntvIndex.setStatus("mandatory")
_ChPerfIntvUnavailToDte_Type = Integer32
_ChPerfIntvUnavailToDte_Object = MibTableColumn
chPerfIntvUnavailToDte = _ChPerfIntvUnavailToDte_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 2, 1, 2),
    _ChPerfIntvUnavailToDte_Type()
)
chPerfIntvUnavailToDte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPerfIntvUnavailToDte.setStatus("mandatory")
_ChPerfIntvUnavailToDce_Type = Integer32
_ChPerfIntvUnavailToDce_Object = MibTableColumn
chPerfIntvUnavailToDce = _ChPerfIntvUnavailToDce_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 2, 1, 3),
    _ChPerfIntvUnavailToDce_Type()
)
chPerfIntvUnavailToDce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPerfIntvUnavailToDce.setStatus("mandatory")
_ChPerfIntvTxLoad_Type = Integer32
_ChPerfIntvTxLoad_Object = MibTableColumn
chPerfIntvTxLoad = _ChPerfIntvTxLoad_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 2, 1, 4),
    _ChPerfIntvTxLoad_Type()
)
chPerfIntvTxLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPerfIntvTxLoad.setStatus("mandatory")
_ChPerfIntvRxLoad_Type = Integer32
_ChPerfIntvRxLoad_Object = MibTableColumn
chPerfIntvRxLoad = _ChPerfIntvRxLoad_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 2, 1, 5),
    _ChPerfIntvRxLoad_Type()
)
chPerfIntvRxLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPerfIntvRxLoad.setStatus("mandatory")
_ChPerfIntvTotalTxLoad_Type = Integer32
_ChPerfIntvTotalTxLoad_Object = MibTableColumn
chPerfIntvTotalTxLoad = _ChPerfIntvTotalTxLoad_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 2, 1, 6),
    _ChPerfIntvTotalTxLoad_Type()
)
chPerfIntvTotalTxLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPerfIntvTotalTxLoad.setStatus("mandatory")
_ChPerfIntvTotalRxLoad_Type = Integer32
_ChPerfIntvTotalRxLoad_Object = MibTableColumn
chPerfIntvTotalRxLoad = _ChPerfIntvTotalRxLoad_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 2, 1, 7),
    _ChPerfIntvTotalRxLoad_Type()
)
chPerfIntvTotalRxLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPerfIntvTotalRxLoad.setStatus("mandatory")
_PvcPerfCurrTable_Object = MibTable
pvcPerfCurrTable = _PvcPerfCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    pvcPerfCurrTable.setStatus("mandatory")
_PvcPerfCurrEntry_Object = MibTableRow
pvcPerfCurrEntry = _PvcPerfCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 3, 1)
)
pvcPerfCurrEntry.setIndexNames(
    (0, "AP553-MIB", "pvcPerfCurrDlciIndex"),
)
if mibBuilder.loadTexts:
    pvcPerfCurrEntry.setStatus("mandatory")


class _PvcPerfCurrDlciIndex_Type(Integer32):
    """Custom type pvcPerfCurrDlciIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_PvcPerfCurrDlciIndex_Type.__name__ = "Integer32"
_PvcPerfCurrDlciIndex_Object = MibTableColumn
pvcPerfCurrDlciIndex = _PvcPerfCurrDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 3, 1, 1),
    _PvcPerfCurrDlciIndex_Type()
)
pvcPerfCurrDlciIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfCurrDlciIndex.setStatus("mandatory")
_PvcPerfCurrRtd_Type = Integer32
_PvcPerfCurrRtd_Object = MibTableColumn
pvcPerfCurrRtd = _PvcPerfCurrRtd_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 3, 1, 2),
    _PvcPerfCurrRtd_Type()
)
pvcPerfCurrRtd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfCurrRtd.setStatus("mandatory")
_PvcPerfCurrUnavailToDte_Type = Integer32
_PvcPerfCurrUnavailToDte_Object = MibTableColumn
pvcPerfCurrUnavailToDte = _PvcPerfCurrUnavailToDte_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 3, 1, 3),
    _PvcPerfCurrUnavailToDte_Type()
)
pvcPerfCurrUnavailToDte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfCurrUnavailToDte.setStatus("mandatory")
_PvcPerfCurrUnavailToDce_Type = Integer32
_PvcPerfCurrUnavailToDce_Object = MibTableColumn
pvcPerfCurrUnavailToDce = _PvcPerfCurrUnavailToDce_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 3, 1, 4),
    _PvcPerfCurrUnavailToDce_Type()
)
pvcPerfCurrUnavailToDce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfCurrUnavailToDce.setStatus("mandatory")
_PvcPerfCurrTxLoad_Type = Integer32
_PvcPerfCurrTxLoad_Object = MibTableColumn
pvcPerfCurrTxLoad = _PvcPerfCurrTxLoad_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 3, 1, 5),
    _PvcPerfCurrTxLoad_Type()
)
pvcPerfCurrTxLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfCurrTxLoad.setStatus("mandatory")
_PvcPerfCurrRxLoad_Type = Integer32
_PvcPerfCurrRxLoad_Object = MibTableColumn
pvcPerfCurrRxLoad = _PvcPerfCurrRxLoad_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 3, 1, 6),
    _PvcPerfCurrRxLoad_Type()
)
pvcPerfCurrRxLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfCurrRxLoad.setStatus("mandatory")
_PvcPerfCurrTotalTxLoad_Type = Integer32
_PvcPerfCurrTotalTxLoad_Object = MibTableColumn
pvcPerfCurrTotalTxLoad = _PvcPerfCurrTotalTxLoad_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 3, 1, 7),
    _PvcPerfCurrTotalTxLoad_Type()
)
pvcPerfCurrTotalTxLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfCurrTotalTxLoad.setStatus("mandatory")
_PvcPerfCurrTotalRxLoad_Type = Integer32
_PvcPerfCurrTotalRxLoad_Object = MibTableColumn
pvcPerfCurrTotalRxLoad = _PvcPerfCurrTotalRxLoad_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 3, 1, 8),
    _PvcPerfCurrTotalRxLoad_Type()
)
pvcPerfCurrTotalRxLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfCurrTotalRxLoad.setStatus("mandatory")
_PvcPerfCurrCirToNetExceed_Type = Integer32
_PvcPerfCurrCirToNetExceed_Object = MibTableColumn
pvcPerfCurrCirToNetExceed = _PvcPerfCurrCirToNetExceed_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 3, 1, 9),
    _PvcPerfCurrCirToNetExceed_Type()
)
pvcPerfCurrCirToNetExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfCurrCirToNetExceed.setStatus("mandatory")
_PvcPerfCurrEirToNetExceed_Type = Integer32
_PvcPerfCurrEirToNetExceed_Object = MibTableColumn
pvcPerfCurrEirToNetExceed = _PvcPerfCurrEirToNetExceed_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 3, 1, 10),
    _PvcPerfCurrEirToNetExceed_Type()
)
pvcPerfCurrEirToNetExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfCurrEirToNetExceed.setStatus("mandatory")


class _PvcPerfCurrTxFrameLoss_Type(Integer32):
    """Custom type pvcPerfCurrTxFrameLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("notAvail", 255)
    )


_PvcPerfCurrTxFrameLoss_Type.__name__ = "Integer32"
_PvcPerfCurrTxFrameLoss_Object = MibTableColumn
pvcPerfCurrTxFrameLoss = _PvcPerfCurrTxFrameLoss_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 3, 1, 11),
    _PvcPerfCurrTxFrameLoss_Type()
)
pvcPerfCurrTxFrameLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfCurrTxFrameLoss.setStatus("mandatory")


class _PvcPerfCurrRxFrameLoss_Type(Integer32):
    """Custom type pvcPerfCurrRxFrameLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("notAvail", 255)
    )


_PvcPerfCurrRxFrameLoss_Type.__name__ = "Integer32"
_PvcPerfCurrRxFrameLoss_Object = MibTableColumn
pvcPerfCurrRxFrameLoss = _PvcPerfCurrRxFrameLoss_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 3, 1, 12),
    _PvcPerfCurrRxFrameLoss_Type()
)
pvcPerfCurrRxFrameLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfCurrRxFrameLoss.setStatus("mandatory")
_PvcPerfIntvTable_Object = MibTable
pvcPerfIntvTable = _PvcPerfIntvTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 4)
)
if mibBuilder.loadTexts:
    pvcPerfIntvTable.setStatus("mandatory")
_PvcPerfIntvEntry_Object = MibTableRow
pvcPerfIntvEntry = _PvcPerfIntvEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 4, 1)
)
pvcPerfIntvEntry.setIndexNames(
    (0, "AP553-MIB", "pvcPerfIntvDlciIndex"),
    (0, "AP553-MIB", "pvcPerfIntvIndex"),
)
if mibBuilder.loadTexts:
    pvcPerfIntvEntry.setStatus("mandatory")


class _PvcPerfIntvDlciIndex_Type(Integer32):
    """Custom type pvcPerfIntvDlciIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_PvcPerfIntvDlciIndex_Type.__name__ = "Integer32"
_PvcPerfIntvDlciIndex_Object = MibTableColumn
pvcPerfIntvDlciIndex = _PvcPerfIntvDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 4, 1, 1),
    _PvcPerfIntvDlciIndex_Type()
)
pvcPerfIntvDlciIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfIntvDlciIndex.setStatus("mandatory")


class _PvcPerfIntvIndex_Type(Integer32):
    """Custom type pvcPerfIntvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PvcPerfIntvIndex_Type.__name__ = "Integer32"
_PvcPerfIntvIndex_Object = MibTableColumn
pvcPerfIntvIndex = _PvcPerfIntvIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 4, 1, 2),
    _PvcPerfIntvIndex_Type()
)
pvcPerfIntvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfIntvIndex.setStatus("mandatory")
_PvcPerfIntvRtd_Type = Integer32
_PvcPerfIntvRtd_Object = MibTableColumn
pvcPerfIntvRtd = _PvcPerfIntvRtd_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 4, 1, 3),
    _PvcPerfIntvRtd_Type()
)
pvcPerfIntvRtd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfIntvRtd.setStatus("mandatory")
_PvcPerfIntvUnavailToDte_Type = Integer32
_PvcPerfIntvUnavailToDte_Object = MibTableColumn
pvcPerfIntvUnavailToDte = _PvcPerfIntvUnavailToDte_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 4, 1, 4),
    _PvcPerfIntvUnavailToDte_Type()
)
pvcPerfIntvUnavailToDte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfIntvUnavailToDte.setStatus("mandatory")
_PvcPerfIntvUnavailToDce_Type = Integer32
_PvcPerfIntvUnavailToDce_Object = MibTableColumn
pvcPerfIntvUnavailToDce = _PvcPerfIntvUnavailToDce_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 4, 1, 5),
    _PvcPerfIntvUnavailToDce_Type()
)
pvcPerfIntvUnavailToDce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfIntvUnavailToDce.setStatus("mandatory")
_PvcPerfIntvTxLoad_Type = Integer32
_PvcPerfIntvTxLoad_Object = MibTableColumn
pvcPerfIntvTxLoad = _PvcPerfIntvTxLoad_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 4, 1, 6),
    _PvcPerfIntvTxLoad_Type()
)
pvcPerfIntvTxLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfIntvTxLoad.setStatus("mandatory")
_PvcPerfIntvRxLoad_Type = Integer32
_PvcPerfIntvRxLoad_Object = MibTableColumn
pvcPerfIntvRxLoad = _PvcPerfIntvRxLoad_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 4, 1, 7),
    _PvcPerfIntvRxLoad_Type()
)
pvcPerfIntvRxLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfIntvRxLoad.setStatus("mandatory")
_PvcPerfIntvTotalTxLoad_Type = Integer32
_PvcPerfIntvTotalTxLoad_Object = MibTableColumn
pvcPerfIntvTotalTxLoad = _PvcPerfIntvTotalTxLoad_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 4, 1, 8),
    _PvcPerfIntvTotalTxLoad_Type()
)
pvcPerfIntvTotalTxLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfIntvTotalTxLoad.setStatus("mandatory")
_PvcPerfIntvTotalRxLoad_Type = Integer32
_PvcPerfIntvTotalRxLoad_Object = MibTableColumn
pvcPerfIntvTotalRxLoad = _PvcPerfIntvTotalRxLoad_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 4, 1, 9),
    _PvcPerfIntvTotalRxLoad_Type()
)
pvcPerfIntvTotalRxLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfIntvTotalRxLoad.setStatus("mandatory")
_PvcPerfIntvCirToNetExceed_Type = Integer32
_PvcPerfIntvCirToNetExceed_Object = MibTableColumn
pvcPerfIntvCirToNetExceed = _PvcPerfIntvCirToNetExceed_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 4, 1, 10),
    _PvcPerfIntvCirToNetExceed_Type()
)
pvcPerfIntvCirToNetExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfIntvCirToNetExceed.setStatus("mandatory")
_PvcPerfIntvEirToNetExceed_Type = Integer32
_PvcPerfIntvEirToNetExceed_Object = MibTableColumn
pvcPerfIntvEirToNetExceed = _PvcPerfIntvEirToNetExceed_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 4, 1, 11),
    _PvcPerfIntvEirToNetExceed_Type()
)
pvcPerfIntvEirToNetExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfIntvEirToNetExceed.setStatus("mandatory")


class _PvcPerfIntvTxFrameLoss_Type(Integer32):
    """Custom type pvcPerfIntvTxFrameLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("notAvail", 255)
    )


_PvcPerfIntvTxFrameLoss_Type.__name__ = "Integer32"
_PvcPerfIntvTxFrameLoss_Object = MibTableColumn
pvcPerfIntvTxFrameLoss = _PvcPerfIntvTxFrameLoss_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 4, 1, 12),
    _PvcPerfIntvTxFrameLoss_Type()
)
pvcPerfIntvTxFrameLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfIntvTxFrameLoss.setStatus("mandatory")


class _PvcPerfIntvRxFrameLoss_Type(Integer32):
    """Custom type pvcPerfIntvRxFrameLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("notAvail", 255)
    )


_PvcPerfIntvRxFrameLoss_Type.__name__ = "Integer32"
_PvcPerfIntvRxFrameLoss_Object = MibTableColumn
pvcPerfIntvRxFrameLoss = _PvcPerfIntvRxFrameLoss_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 4, 1, 13),
    _PvcPerfIntvRxFrameLoss_Type()
)
pvcPerfIntvRxFrameLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfIntvRxFrameLoss.setStatus("mandatory")
_PvcPerfRealTimeTable_Object = MibTable
pvcPerfRealTimeTable = _PvcPerfRealTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 5)
)
if mibBuilder.loadTexts:
    pvcPerfRealTimeTable.setStatus("mandatory")
_PvcPerfRealTimeEntry_Object = MibTableRow
pvcPerfRealTimeEntry = _PvcPerfRealTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 5, 1)
)
pvcPerfRealTimeEntry.setIndexNames(
    (0, "AP553-MIB", "pvcPerfRealTimeDlciIndex"),
)
if mibBuilder.loadTexts:
    pvcPerfRealTimeEntry.setStatus("mandatory")


class _PvcPerfRealTimeDlciIndex_Type(Integer32):
    """Custom type pvcPerfRealTimeDlciIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_PvcPerfRealTimeDlciIndex_Type.__name__ = "Integer32"
_PvcPerfRealTimeDlciIndex_Object = MibTableColumn
pvcPerfRealTimeDlciIndex = _PvcPerfRealTimeDlciIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 5, 1, 1),
    _PvcPerfRealTimeDlciIndex_Type()
)
pvcPerfRealTimeDlciIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfRealTimeDlciIndex.setStatus("mandatory")
_PvcPerfRealTimeRtd_Type = Integer32
_PvcPerfRealTimeRtd_Object = MibTableColumn
pvcPerfRealTimeRtd = _PvcPerfRealTimeRtd_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 5, 1, 2),
    _PvcPerfRealTimeRtd_Type()
)
pvcPerfRealTimeRtd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfRealTimeRtd.setStatus("mandatory")
_PvcPerfRealTimeLoadToDCE_Type = Integer32
_PvcPerfRealTimeLoadToDCE_Object = MibTableColumn
pvcPerfRealTimeLoadToDCE = _PvcPerfRealTimeLoadToDCE_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 5, 1, 3),
    _PvcPerfRealTimeLoadToDCE_Type()
)
pvcPerfRealTimeLoadToDCE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfRealTimeLoadToDCE.setStatus("mandatory")
_PvcPerfRealTimeLoadToDTE_Type = Integer32
_PvcPerfRealTimeLoadToDTE_Object = MibTableColumn
pvcPerfRealTimeLoadToDTE = _PvcPerfRealTimeLoadToDTE_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 3, 5, 1, 4),
    _PvcPerfRealTimeLoadToDTE_Type()
)
pvcPerfRealTimeLoadToDTE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPerfRealTimeLoadToDTE.setStatus("mandatory")
_TrapStatus_ObjectIdentity = ObjectIdentity
trapStatus = _TrapStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 4)
)
_AlarmStatus_ObjectIdentity = ObjectIdentity
alarmStatus = _AlarmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 4, 1)
)


class _AlarmCurrentStatusBitsMap_Type(Integer32):
    """Custom type alarmCurrentStatusBitsMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AlarmCurrentStatusBitsMap_Type.__name__ = "Integer32"
_AlarmCurrentStatusBitsMap_Object = MibScalar
alarmCurrentStatusBitsMap = _AlarmCurrentStatusBitsMap_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 4, 1, 1),
    _AlarmCurrentStatusBitsMap_Type()
)
alarmCurrentStatusBitsMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmCurrentStatusBitsMap.setStatus("mandatory")
_AlarmCurrentStatusTable_Object = MibTable
alarmCurrentStatusTable = _AlarmCurrentStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    alarmCurrentStatusTable.setStatus("mandatory")
_AlarmStatusEntry_Object = MibTableRow
alarmStatusEntry = _AlarmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 4, 1, 2, 1)
)
alarmStatusEntry.setIndexNames(
    (0, "AP553-MIB", "alarmStatusTableIndex"),
)
if mibBuilder.loadTexts:
    alarmStatusEntry.setStatus("mandatory")


class _AlarmStatusTableIndex_Type(Integer32):
    """Custom type alarmStatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_AlarmStatusTableIndex_Type.__name__ = "Integer32"
_AlarmStatusTableIndex_Object = MibTableColumn
alarmStatusTableIndex = _AlarmStatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 4, 1, 2, 1, 1),
    _AlarmStatusTableIndex_Type()
)
alarmStatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStatusTableIndex.setStatus("mandatory")


class _CurrentStatusBitsMap_Type(Integer32):
    """Custom type currentStatusBitsMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CurrentStatusBitsMap_Type.__name__ = "Integer32"
_CurrentStatusBitsMap_Object = MibTableColumn
currentStatusBitsMap = _CurrentStatusBitsMap_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2, 4, 1, 2, 1, 2),
    _CurrentStatusBitsMap_Type()
)
currentStatusBitsMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentStatusBitsMap.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AP553-MIB",
    **{"probeConfig": probeConfig,
       "chanConfig": chanConfig,
       "lmiOperation": lmiOperation,
       "lmiDLCI": lmiDLCI,
       "ipDLCI": ipDLCI,
       "ipEncapp": ipEncapp,
       "chanAggregateRate": chanAggregateRate,
       "lmiConfig": lmiConfig,
       "lmiType": lmiType,
       "lmiN391": lmiN391,
       "lmiNet392": lmiNet392,
       "lmiUser392": lmiUser392,
       "lmiNet393": lmiNet393,
       "lmiUser393": lmiUser393,
       "t391Timer": t391Timer,
       "t392Timer": t392Timer,
       "maxInfoLength": maxInfoLength,
       "proFunConfig": proFunConfig,
       "unitType": unitType,
       "probeMode": probeMode,
       "pollPeriod": pollPeriod,
       "globalTC": globalTC,
       "pvcCount": pvcCount,
       "probeTokenSize": probeTokenSize,
       "pvcAdd": pvcAdd,
       "pvcDelete": pvcDelete,
       "pvcDiscovery": pvcDiscovery,
       "trapConfig": trapConfig,
       "pvcOperStateChangeTrapSeverity": pvcOperStateChangeTrapSeverity,
       "realTimeTrapSeverity": realTimeTrapSeverity,
       "realTimeChanLoadToDCEThresh": realTimeChanLoadToDCEThresh,
       "realTimeChanLoadToDCEThreshVar": realTimeChanLoadToDCEThreshVar,
       "avgChanLoadToDCETrapSeverity": avgChanLoadToDCETrapSeverity,
       "avgChanLoadToDCEThresh": avgChanLoadToDCEThresh,
       "realTimeChanLoadToDTEThresh": realTimeChanLoadToDTEThresh,
       "realTimeChanLoadToDTEThreshVar": realTimeChanLoadToDTEThreshVar,
       "avgChanLoadToDTETrapSeverity": avgChanLoadToDTETrapSeverity,
       "avgChanLoadToDTEThresh": avgChanLoadToDTEThresh,
       "realTimePvcLoadToDCEThresh": realTimePvcLoadToDCEThresh,
       "realTimePvcLoadToDCEThreshVar": realTimePvcLoadToDCEThreshVar,
       "avgPvcLoadToDCETrapSeverity": avgPvcLoadToDCETrapSeverity,
       "avgPvcLoadToDCEThresh": avgPvcLoadToDCEThresh,
       "realTimePvcLoadToDTEThresh": realTimePvcLoadToDTEThresh,
       "realTimePvcLoadToDTEThreshVar": realTimePvcLoadToDTEThreshVar,
       "avgPvcLoadToDTETrapSeverity": avgPvcLoadToDTETrapSeverity,
       "avgPvcLoadToDTEThresh": avgPvcLoadToDTEThresh,
       "realTimePvcRoundTripDelayThresh": realTimePvcRoundTripDelayThresh,
       "realTimePvcRoundTripDelayThreshVar": realTimePvcRoundTripDelayThreshVar,
       "avgPvcRoundTripDelayTrapSeverity": avgPvcRoundTripDelayTrapSeverity,
       "avgPvcRoundTripDelayThresh": avgPvcRoundTripDelayThresh,
       "avgPvcNotAvailToDCETrapSeverity": avgPvcNotAvailToDCETrapSeverity,
       "avgPvcNotAvailToDCEThresh": avgPvcNotAvailToDCEThresh,
       "avgPvcNotAvailToDTETrapSeverity": avgPvcNotAvailToDTETrapSeverity,
       "avgPvcNotAvailToDTEThresh": avgPvcNotAvailToDTEThresh,
       "avgPvcFecnFramesTrapSeverity": avgPvcFecnFramesTrapSeverity,
       "avgPvcFecnFramesThresh": avgPvcFecnFramesThresh,
       "avgPvcBecnFramesTrapSeverity": avgPvcBecnFramesTrapSeverity,
       "avgPvcBecnFramesThresh": avgPvcBecnFramesThresh,
       "avgPvcCIRExceedToDTETrapSeverity": avgPvcCIRExceedToDTETrapSeverity,
       "avgPvcEIRExceedToDTETrapSeverity": avgPvcEIRExceedToDTETrapSeverity,
       "avgPvcLossFrameTxTrapSeverity": avgPvcLossFrameTxTrapSeverity,
       "avgPvcLossFrameRxTrapSeverity": avgPvcLossFrameRxTrapSeverity,
       "networkLmiInterfaceDownTrapSeverity": networkLmiInterfaceDownTrapSeverity,
       "userLmiInterfaceDownTrapSeverity": userLmiInterfaceDownTrapSeverity,
       "pvcConfig": pvcConfig,
       "pvcCirEirTable": pvcCirEirTable,
       "pvcCirEirEntry": pvcCirEirEntry,
       "pvcCirEirTableIndex": pvcCirEirTableIndex,
       "pvcCirToDTE": pvcCirToDTE,
       "pvcCirToDCE": pvcCirToDCE,
       "pvcEirToDTE": pvcEirToDTE,
       "pvcEirToDCE": pvcEirToDCE,
       "pvcOperation": pvcOperation,
       "pvcState": pvcState,
       "pvcIdentifier": pvcIdentifier,
       "probeVersion": probeVersion,
       "frProbeMIBversion": frProbeMIBversion,
       "probeStat": probeStat,
       "chStCurrent": chStCurrent,
       "chCurrDteFrames": chCurrDteFrames,
       "chCurrDceFrames": chCurrDceFrames,
       "chCurrDteOctets": chCurrDteOctets,
       "chCurrDceOctets": chCurrDceOctets,
       "chCurrLmiTxEnq": chCurrLmiTxEnq,
       "chCurrLmiTxResp": chCurrLmiTxResp,
       "chCurrLmiRxEnq": chCurrLmiRxEnq,
       "chCurrLmiRxResp": chCurrLmiRxResp,
       "chCurrDTELmiTimeout": chCurrDTELmiTimeout,
       "chCurrDCELmiTimeout": chCurrDCELmiTimeout,
       "chCurrFecnFrames": chCurrFecnFrames,
       "chCurrBecnFrames": chCurrBecnFrames,
       "chCurrTxIp": chCurrTxIp,
       "chCurrRxIp": chCurrRxIp,
       "chCurrTxPoll": chCurrTxPoll,
       "chCurrTxResp": chCurrTxResp,
       "chCurrRxPoll": chCurrRxPoll,
       "chCurrRxResp": chCurrRxResp,
       "intervalComplete": intervalComplete,
       "chStIntervalTable": chStIntervalTable,
       "chStIntervalEntry": chStIntervalEntry,
       "chIntvIndex": chIntvIndex,
       "chIntvDteFrames": chIntvDteFrames,
       "chIntvDceFrames": chIntvDceFrames,
       "chIntvDteOctets": chIntvDteOctets,
       "chIntvDceOctets": chIntvDceOctets,
       "chIntvLmiTxEnq": chIntvLmiTxEnq,
       "chIntvLmiTxResp": chIntvLmiTxResp,
       "chIntvLmiRxEnq": chIntvLmiRxEnq,
       "chIntvLmiRxResp": chIntvLmiRxResp,
       "chIntvDTELmiTimeout": chIntvDTELmiTimeout,
       "chIntvDCELmiTimeout": chIntvDCELmiTimeout,
       "chIntvFecnFrames": chIntvFecnFrames,
       "chIntvBecnFrames": chIntvBecnFrames,
       "chIntvTxIp": chIntvTxIp,
       "chIntvRxIp": chIntvRxIp,
       "chIntvTxPoll": chIntvTxPoll,
       "chIntvTxResp": chIntvTxResp,
       "chIntvRxPoll": chIntvRxPoll,
       "chIntvRxResp": chIntvRxResp,
       "pvcStCurrentTable": pvcStCurrentTable,
       "pvcStCurrentEntry": pvcStCurrentEntry,
       "pvcCurrDlciIndex": pvcCurrDlciIndex,
       "pvcCurrDteFrames": pvcCurrDteFrames,
       "pvcCurrDceFrames": pvcCurrDceFrames,
       "pvcCurrDteOctets": pvcCurrDteOctets,
       "pvcCurrDceOctets": pvcCurrDceOctets,
       "pvcCurrDteFramesWithDE": pvcCurrDteFramesWithDE,
       "pvcCurrDceFramesWithDE": pvcCurrDceFramesWithDE,
       "pvcCurrFecnFrames": pvcCurrFecnFrames,
       "pvcCurrBecnFrames": pvcCurrBecnFrames,
       "pvcCurrTxPoll": pvcCurrTxPoll,
       "pvcCurrTxResp": pvcCurrTxResp,
       "pvcCurrRxPoll": pvcCurrRxPoll,
       "pvcCurrRxResp": pvcCurrRxResp,
       "pvcCurrLoopback": pvcCurrLoopback,
       "pvcStIntervalTable": pvcStIntervalTable,
       "pvcStIntervalEntry": pvcStIntervalEntry,
       "pvcIntvDlciIndex": pvcIntvDlciIndex,
       "pvcIntvIndex": pvcIntvIndex,
       "pvcIntvDteFrames": pvcIntvDteFrames,
       "pvcIntvDceFrames": pvcIntvDceFrames,
       "pvcIntvDteOctets": pvcIntvDteOctets,
       "pvcIntvDceOctets": pvcIntvDceOctets,
       "pvcIntvDteFramesWithDE": pvcIntvDteFramesWithDE,
       "pvcIntvDceFramesWithDE": pvcIntvDceFramesWithDE,
       "pvcIntvFecnFrames": pvcIntvFecnFrames,
       "pvcIntvBecnFrames": pvcIntvBecnFrames,
       "pvcIntvTxPoll": pvcIntvTxPoll,
       "pvcIntvTxResp": pvcIntvTxResp,
       "pvcIntvRxPoll": pvcIntvRxPoll,
       "pvcIntvRxResp": pvcIntvRxResp,
       "pvcIntvLoopback": pvcIntvLoopback,
       "probePerform": probePerform,
       "chanPerfCurr": chanPerfCurr,
       "chPerfCurrUnavailToDte": chPerfCurrUnavailToDte,
       "chPerfCurrUnavailToDce": chPerfCurrUnavailToDce,
       "chPerfCurrTxLoad": chPerfCurrTxLoad,
       "chPerfCurrRxLoad": chPerfCurrRxLoad,
       "chPerfCurrTotalTxLoad": chPerfCurrTotalTxLoad,
       "chPerfCurrTotalRxLoad": chPerfCurrTotalRxLoad,
       "chPerfCurrLoadToDceRealTime": chPerfCurrLoadToDceRealTime,
       "chPerfCurrLoadToDteRealTime": chPerfCurrLoadToDteRealTime,
       "chanPerfIntvTable": chanPerfIntvTable,
       "chanPerfIntvEntry": chanPerfIntvEntry,
       "chPerfIntvIndex": chPerfIntvIndex,
       "chPerfIntvUnavailToDte": chPerfIntvUnavailToDte,
       "chPerfIntvUnavailToDce": chPerfIntvUnavailToDce,
       "chPerfIntvTxLoad": chPerfIntvTxLoad,
       "chPerfIntvRxLoad": chPerfIntvRxLoad,
       "chPerfIntvTotalTxLoad": chPerfIntvTotalTxLoad,
       "chPerfIntvTotalRxLoad": chPerfIntvTotalRxLoad,
       "pvcPerfCurrTable": pvcPerfCurrTable,
       "pvcPerfCurrEntry": pvcPerfCurrEntry,
       "pvcPerfCurrDlciIndex": pvcPerfCurrDlciIndex,
       "pvcPerfCurrRtd": pvcPerfCurrRtd,
       "pvcPerfCurrUnavailToDte": pvcPerfCurrUnavailToDte,
       "pvcPerfCurrUnavailToDce": pvcPerfCurrUnavailToDce,
       "pvcPerfCurrTxLoad": pvcPerfCurrTxLoad,
       "pvcPerfCurrRxLoad": pvcPerfCurrRxLoad,
       "pvcPerfCurrTotalTxLoad": pvcPerfCurrTotalTxLoad,
       "pvcPerfCurrTotalRxLoad": pvcPerfCurrTotalRxLoad,
       "pvcPerfCurrCirToNetExceed": pvcPerfCurrCirToNetExceed,
       "pvcPerfCurrEirToNetExceed": pvcPerfCurrEirToNetExceed,
       "pvcPerfCurrTxFrameLoss": pvcPerfCurrTxFrameLoss,
       "pvcPerfCurrRxFrameLoss": pvcPerfCurrRxFrameLoss,
       "pvcPerfIntvTable": pvcPerfIntvTable,
       "pvcPerfIntvEntry": pvcPerfIntvEntry,
       "pvcPerfIntvDlciIndex": pvcPerfIntvDlciIndex,
       "pvcPerfIntvIndex": pvcPerfIntvIndex,
       "pvcPerfIntvRtd": pvcPerfIntvRtd,
       "pvcPerfIntvUnavailToDte": pvcPerfIntvUnavailToDte,
       "pvcPerfIntvUnavailToDce": pvcPerfIntvUnavailToDce,
       "pvcPerfIntvTxLoad": pvcPerfIntvTxLoad,
       "pvcPerfIntvRxLoad": pvcPerfIntvRxLoad,
       "pvcPerfIntvTotalTxLoad": pvcPerfIntvTotalTxLoad,
       "pvcPerfIntvTotalRxLoad": pvcPerfIntvTotalRxLoad,
       "pvcPerfIntvCirToNetExceed": pvcPerfIntvCirToNetExceed,
       "pvcPerfIntvEirToNetExceed": pvcPerfIntvEirToNetExceed,
       "pvcPerfIntvTxFrameLoss": pvcPerfIntvTxFrameLoss,
       "pvcPerfIntvRxFrameLoss": pvcPerfIntvRxFrameLoss,
       "pvcPerfRealTimeTable": pvcPerfRealTimeTable,
       "pvcPerfRealTimeEntry": pvcPerfRealTimeEntry,
       "pvcPerfRealTimeDlciIndex": pvcPerfRealTimeDlciIndex,
       "pvcPerfRealTimeRtd": pvcPerfRealTimeRtd,
       "pvcPerfRealTimeLoadToDCE": pvcPerfRealTimeLoadToDCE,
       "pvcPerfRealTimeLoadToDTE": pvcPerfRealTimeLoadToDTE,
       "trapStatus": trapStatus,
       "alarmStatus": alarmStatus,
       "alarmCurrentStatusBitsMap": alarmCurrentStatusBitsMap,
       "alarmCurrentStatusTable": alarmCurrentStatusTable,
       "alarmStatusEntry": alarmStatusEntry,
       "alarmStatusTableIndex": alarmStatusTableIndex,
       "currentStatusBitsMap": currentStatusBitsMap}
)
