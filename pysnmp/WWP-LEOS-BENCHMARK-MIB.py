# SNMP MIB module (WWP-LEOS-BENCHMARK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-BENCHMARK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:45 2024
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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosBenchmarkMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43)
)
wwpLeosBenchmarkMIB.setRevisions(
        ("2012-02-13 08:00",
         "2012-02-03 08:00",
         "2010-12-14 08:00",
         "2010-11-25 08:00",
         "2010-11-15 08:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BenchmarkLatencyPdvTestState(Integer32, TextualConvention):
    status = "current"
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
        *(("done", 9),
          ("idle", 1),
          ("processingResults", 5),
          ("sendingTraffic", 2),
          ("stoppedByDurationTimer", 7),
          ("stoppedByIntervalTimer", 6),
          ("stoppedByUser", 8),
          ("waitingForResidualPackets", 4),
          ("waitingForTimestampData", 3))
    )



# MIB Managed Objects in the order of their OIDs

_WwpLeosBenchmarkMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosBenchmarkMIBObjects = _WwpLeosBenchmarkMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1)
)
_WwpLeosBenchmarkModule_ObjectIdentity = ObjectIdentity
wwpLeosBenchmarkModule = _WwpLeosBenchmarkModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 1)
)


class _WwpLeosBenchmarkRole_Type(Integer32):
    """Custom type wwpLeosBenchmarkRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("generator", 3),
          ("none", 1),
          ("reflector", 2))
    )


_WwpLeosBenchmarkRole_Type.__name__ = "Integer32"
_WwpLeosBenchmarkRole_Object = MibScalar
wwpLeosBenchmarkRole = _WwpLeosBenchmarkRole_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 1, 1),
    _WwpLeosBenchmarkRole_Type()
)
wwpLeosBenchmarkRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkRole.setStatus("current")


class _WwpLeosBenchmarkPort_Type(Integer32):
    """Custom type wwpLeosBenchmarkPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_WwpLeosBenchmarkPort_Type.__name__ = "Integer32"
_WwpLeosBenchmarkPort_Object = MibScalar
wwpLeosBenchmarkPort = _WwpLeosBenchmarkPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 1, 2),
    _WwpLeosBenchmarkPort_Type()
)
wwpLeosBenchmarkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPort.setStatus("current")


class _WwpLeosBenchmarkMode_Type(Integer32):
    """Custom type wwpLeosBenchmarkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inService", 2),
          ("none", 1),
          ("outOfService", 3))
    )


_WwpLeosBenchmarkMode_Type.__name__ = "Integer32"
_WwpLeosBenchmarkMode_Object = MibScalar
wwpLeosBenchmarkMode = _WwpLeosBenchmarkMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 1, 3),
    _WwpLeosBenchmarkMode_Type()
)
wwpLeosBenchmarkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkMode.setStatus("current")
_WwpLeosBenchmarkEnable_Type = TruthValue
_WwpLeosBenchmarkEnable_Object = MibScalar
wwpLeosBenchmarkEnable = _WwpLeosBenchmarkEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 1, 4),
    _WwpLeosBenchmarkEnable_Type()
)
wwpLeosBenchmarkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkEnable.setStatus("current")
_WwpLeosBenchmarkOperEnable_Type = TruthValue
_WwpLeosBenchmarkOperEnable_Object = MibScalar
wwpLeosBenchmarkOperEnable = _WwpLeosBenchmarkOperEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 1, 5),
    _WwpLeosBenchmarkOperEnable_Type()
)
wwpLeosBenchmarkOperEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkOperEnable.setStatus("current")
_WwpLeosBenchmarkLocalFpgaMac_Type = MacAddress
_WwpLeosBenchmarkLocalFpgaMac_Object = MibScalar
wwpLeosBenchmarkLocalFpgaMac = _WwpLeosBenchmarkLocalFpgaMac_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 1, 6),
    _WwpLeosBenchmarkLocalFpgaMac_Type()
)
wwpLeosBenchmarkLocalFpgaMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkLocalFpgaMac.setStatus("current")
_WwpLeosBenchmarkReflectorModule_ObjectIdentity = ObjectIdentity
wwpLeosBenchmarkReflectorModule = _WwpLeosBenchmarkReflectorModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 2)
)
_WwpLeosBenchmarkReflectorEnable_Type = TruthValue
_WwpLeosBenchmarkReflectorEnable_Object = MibScalar
wwpLeosBenchmarkReflectorEnable = _WwpLeosBenchmarkReflectorEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 2, 1),
    _WwpLeosBenchmarkReflectorEnable_Type()
)
wwpLeosBenchmarkReflectorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkReflectorEnable.setStatus("current")


class _WwpLeosBenchmarkReflectorVid_Type(Integer32):
    """Custom type wwpLeosBenchmarkReflectorVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4095),
    )


_WwpLeosBenchmarkReflectorVid_Type.__name__ = "Integer32"
_WwpLeosBenchmarkReflectorVid_Object = MibScalar
wwpLeosBenchmarkReflectorVid = _WwpLeosBenchmarkReflectorVid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 2, 2),
    _WwpLeosBenchmarkReflectorVid_Type()
)
wwpLeosBenchmarkReflectorVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkReflectorVid.setStatus("current")


class _WwpLeosBenchmarkReflectorVendorType_Type(Integer32):
    """Custom type wwpLeosBenchmarkReflectorVendorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ciena", 2),
          ("other", 1))
    )


_WwpLeosBenchmarkReflectorVendorType_Type.__name__ = "Integer32"
_WwpLeosBenchmarkReflectorVendorType_Object = MibScalar
wwpLeosBenchmarkReflectorVendorType = _WwpLeosBenchmarkReflectorVendorType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 2, 3),
    _WwpLeosBenchmarkReflectorVendorType_Type()
)
wwpLeosBenchmarkReflectorVendorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkReflectorVendorType.setStatus("current")
_WwpLeosBenchmarkGeneratorModule_ObjectIdentity = ObjectIdentity
wwpLeosBenchmarkGeneratorModule = _WwpLeosBenchmarkGeneratorModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 3)
)
_WwpLeosBenchmarkGeneratorEnable_Type = TruthValue
_WwpLeosBenchmarkGeneratorEnable_Object = MibScalar
wwpLeosBenchmarkGeneratorEnable = _WwpLeosBenchmarkGeneratorEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 3, 1),
    _WwpLeosBenchmarkGeneratorEnable_Type()
)
wwpLeosBenchmarkGeneratorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkGeneratorEnable.setStatus("current")


class _WwpLeosBenchmarkGeneratorprofileUnderTest_Type(DisplayString):
    """Custom type wwpLeosBenchmarkGeneratorprofileUnderTest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_WwpLeosBenchmarkGeneratorprofileUnderTest_Type.__name__ = "DisplayString"
_WwpLeosBenchmarkGeneratorprofileUnderTest_Object = MibScalar
wwpLeosBenchmarkGeneratorprofileUnderTest = _WwpLeosBenchmarkGeneratorprofileUnderTest_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 3, 2),
    _WwpLeosBenchmarkGeneratorprofileUnderTest_Type()
)
wwpLeosBenchmarkGeneratorprofileUnderTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkGeneratorprofileUnderTest.setStatus("current")


class _WwpLeosBenchmarkGeneratorThroughputTestState_Type(Integer32):
    """Custom type wwpLeosBenchmarkGeneratorThroughputTestState based on Integer32"""
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
        *(("done", 8),
          ("idle", 1),
          ("processingResults", 4),
          ("running", 2),
          ("stoppedByDurationTimer", 6),
          ("stoppedByIntervalTimer", 5),
          ("stoppedByUser", 7),
          ("waitingForResidualPackets", 3))
    )


_WwpLeosBenchmarkGeneratorThroughputTestState_Type.__name__ = "Integer32"
_WwpLeosBenchmarkGeneratorThroughputTestState_Object = MibScalar
wwpLeosBenchmarkGeneratorThroughputTestState = _WwpLeosBenchmarkGeneratorThroughputTestState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 3, 3),
    _WwpLeosBenchmarkGeneratorThroughputTestState_Type()
)
wwpLeosBenchmarkGeneratorThroughputTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkGeneratorThroughputTestState.setStatus("current")


class _WwpLeosBenchmarkGeneratorFramelossTestState_Type(Integer32):
    """Custom type wwpLeosBenchmarkGeneratorFramelossTestState based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("done", 11),
          ("idle", 1),
          ("processingFirstResults", 4),
          ("processingSecondResults", 7),
          ("runningFirstTest", 2),
          ("runningSecondTest", 5),
          ("stoppedByDurationTimer", 9),
          ("stoppedByIntervalTimer", 8),
          ("stoppedByUser", 10),
          ("waitingForResidualFirstPackets", 3),
          ("waitingForResidualSecondPackets", 6))
    )


_WwpLeosBenchmarkGeneratorFramelossTestState_Type.__name__ = "Integer32"
_WwpLeosBenchmarkGeneratorFramelossTestState_Object = MibScalar
wwpLeosBenchmarkGeneratorFramelossTestState = _WwpLeosBenchmarkGeneratorFramelossTestState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 3, 4),
    _WwpLeosBenchmarkGeneratorFramelossTestState_Type()
)
wwpLeosBenchmarkGeneratorFramelossTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkGeneratorFramelossTestState.setStatus("current")
_WwpLeosBenchmarkGeneratorLatencyTestState_Type = BenchmarkLatencyPdvTestState
_WwpLeosBenchmarkGeneratorLatencyTestState_Object = MibScalar
wwpLeosBenchmarkGeneratorLatencyTestState = _WwpLeosBenchmarkGeneratorLatencyTestState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 3, 5),
    _WwpLeosBenchmarkGeneratorLatencyTestState_Type()
)
wwpLeosBenchmarkGeneratorLatencyTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkGeneratorLatencyTestState.setStatus("current")
_WwpLeosBenchmarkGeneratorPdvTestState_Type = BenchmarkLatencyPdvTestState
_WwpLeosBenchmarkGeneratorPdvTestState_Object = MibScalar
wwpLeosBenchmarkGeneratorPdvTestState = _WwpLeosBenchmarkGeneratorPdvTestState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 3, 6),
    _WwpLeosBenchmarkGeneratorPdvTestState_Type()
)
wwpLeosBenchmarkGeneratorPdvTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkGeneratorPdvTestState.setStatus("current")


class _WwpLeosBenchmarkGeneratorRfc2544State_Type(Integer32):
    """Custom type wwpLeosBenchmarkGeneratorRfc2544State based on Integer32"""
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
        *(("done", 6),
          ("idle", 1),
          ("running", 2),
          ("stoppedByDurationTimer", 4),
          ("stoppedByIntervalTimer", 3),
          ("stoppedByUser", 5))
    )


_WwpLeosBenchmarkGeneratorRfc2544State_Type.__name__ = "Integer32"
_WwpLeosBenchmarkGeneratorRfc2544State_Object = MibScalar
wwpLeosBenchmarkGeneratorRfc2544State = _WwpLeosBenchmarkGeneratorRfc2544State_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 3, 7),
    _WwpLeosBenchmarkGeneratorRfc2544State_Type()
)
wwpLeosBenchmarkGeneratorRfc2544State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkGeneratorRfc2544State.setStatus("current")
_WwpLeosBenchmarkGeneratorCurrentPktSize_Type = Integer32
_WwpLeosBenchmarkGeneratorCurrentPktSize_Object = MibScalar
wwpLeosBenchmarkGeneratorCurrentPktSize = _WwpLeosBenchmarkGeneratorCurrentPktSize_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 3, 8),
    _WwpLeosBenchmarkGeneratorCurrentPktSize_Type()
)
wwpLeosBenchmarkGeneratorCurrentPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkGeneratorCurrentPktSize.setStatus("current")
_WwpLeosBenchmarkGeneratorCurrentRate_Type = Integer32
_WwpLeosBenchmarkGeneratorCurrentRate_Object = MibScalar
wwpLeosBenchmarkGeneratorCurrentRate = _WwpLeosBenchmarkGeneratorCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 3, 9),
    _WwpLeosBenchmarkGeneratorCurrentRate_Type()
)
wwpLeosBenchmarkGeneratorCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkGeneratorCurrentRate.setStatus("current")
_WwpLeosBenchmarkGeneratorSamplesCompleted_Type = Integer32
_WwpLeosBenchmarkGeneratorSamplesCompleted_Object = MibScalar
wwpLeosBenchmarkGeneratorSamplesCompleted = _WwpLeosBenchmarkGeneratorSamplesCompleted_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 3, 10),
    _WwpLeosBenchmarkGeneratorSamplesCompleted_Type()
)
wwpLeosBenchmarkGeneratorSamplesCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkGeneratorSamplesCompleted.setStatus("current")
_WwpLeosBenchmarkGeneratorCurrentIteration_Type = Integer32
_WwpLeosBenchmarkGeneratorCurrentIteration_Object = MibScalar
wwpLeosBenchmarkGeneratorCurrentIteration = _WwpLeosBenchmarkGeneratorCurrentIteration_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 3, 11),
    _WwpLeosBenchmarkGeneratorCurrentIteration_Type()
)
wwpLeosBenchmarkGeneratorCurrentIteration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkGeneratorCurrentIteration.setStatus("current")
_WwpLeosBenchmarkGeneratorTotalIterations_Type = Integer32
_WwpLeosBenchmarkGeneratorTotalIterations_Object = MibScalar
wwpLeosBenchmarkGeneratorTotalIterations = _WwpLeosBenchmarkGeneratorTotalIterations_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 3, 12),
    _WwpLeosBenchmarkGeneratorTotalIterations_Type()
)
wwpLeosBenchmarkGeneratorTotalIterations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkGeneratorTotalIterations.setStatus("current")
_WwpLeosBenchmarkFpgaStats_ObjectIdentity = ObjectIdentity
wwpLeosBenchmarkFpgaStats = _WwpLeosBenchmarkFpgaStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 4)
)
_WwpLeosBenchmarkFpgaStatsRxPkts_Type = Counter64
_WwpLeosBenchmarkFpgaStatsRxPkts_Object = MibScalar
wwpLeosBenchmarkFpgaStatsRxPkts = _WwpLeosBenchmarkFpgaStatsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 4, 1),
    _WwpLeosBenchmarkFpgaStatsRxPkts_Type()
)
wwpLeosBenchmarkFpgaStatsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkFpgaStatsRxPkts.setStatus("current")
_WwpLeosBenchmarkFpgaStatsCrcPkts_Type = Counter64
_WwpLeosBenchmarkFpgaStatsCrcPkts_Object = MibScalar
wwpLeosBenchmarkFpgaStatsCrcPkts = _WwpLeosBenchmarkFpgaStatsCrcPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 4, 2),
    _WwpLeosBenchmarkFpgaStatsCrcPkts_Type()
)
wwpLeosBenchmarkFpgaStatsCrcPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkFpgaStatsCrcPkts.setStatus("current")
_WwpLeosBenchmarkFpgaStatsUdpChecksumPkts_Type = Counter64
_WwpLeosBenchmarkFpgaStatsUdpChecksumPkts_Object = MibScalar
wwpLeosBenchmarkFpgaStatsUdpChecksumPkts = _WwpLeosBenchmarkFpgaStatsUdpChecksumPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 4, 3),
    _WwpLeosBenchmarkFpgaStatsUdpChecksumPkts_Type()
)
wwpLeosBenchmarkFpgaStatsUdpChecksumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkFpgaStatsUdpChecksumPkts.setStatus("current")
_WwpLeosBenchmarkFpgaStatsDiscardPkts_Type = Counter64
_WwpLeosBenchmarkFpgaStatsDiscardPkts_Object = MibScalar
wwpLeosBenchmarkFpgaStatsDiscardPkts = _WwpLeosBenchmarkFpgaStatsDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 4, 4),
    _WwpLeosBenchmarkFpgaStatsDiscardPkts_Type()
)
wwpLeosBenchmarkFpgaStatsDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkFpgaStatsDiscardPkts.setStatus("current")
_WwpLeosBenchmarkFpgaStatsDuplicatePkts_Type = Counter64
_WwpLeosBenchmarkFpgaStatsDuplicatePkts_Object = MibScalar
wwpLeosBenchmarkFpgaStatsDuplicatePkts = _WwpLeosBenchmarkFpgaStatsDuplicatePkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 4, 5),
    _WwpLeosBenchmarkFpgaStatsDuplicatePkts_Type()
)
wwpLeosBenchmarkFpgaStatsDuplicatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkFpgaStatsDuplicatePkts.setStatus("current")
_WwpLeosBenchmarkFpgaStatsOOSeqPkts_Type = Counter64
_WwpLeosBenchmarkFpgaStatsOOSeqPkts_Object = MibScalar
wwpLeosBenchmarkFpgaStatsOOSeqPkts = _WwpLeosBenchmarkFpgaStatsOOSeqPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 4, 6),
    _WwpLeosBenchmarkFpgaStatsOOSeqPkts_Type()
)
wwpLeosBenchmarkFpgaStatsOOSeqPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkFpgaStatsOOSeqPkts.setStatus("deprecated")
_WwpLeosBenchmarkFpgaStatsTxPkts_Type = Counter64
_WwpLeosBenchmarkFpgaStatsTxPkts_Object = MibScalar
wwpLeosBenchmarkFpgaStatsTxPkts = _WwpLeosBenchmarkFpgaStatsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 4, 7),
    _WwpLeosBenchmarkFpgaStatsTxPkts_Type()
)
wwpLeosBenchmarkFpgaStatsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkFpgaStatsTxPkts.setStatus("current")
_WwpLeosBenchmarkFpgaStatsOOOPkts_Type = Counter64
_WwpLeosBenchmarkFpgaStatsOOOPkts_Object = MibScalar
wwpLeosBenchmarkFpgaStatsOOOPkts = _WwpLeosBenchmarkFpgaStatsOOOPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 4, 8),
    _WwpLeosBenchmarkFpgaStatsOOOPkts_Type()
)
wwpLeosBenchmarkFpgaStatsOOOPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkFpgaStatsOOOPkts.setStatus("current")
_WwpLeosBenchmarkFpgaStatsDiscSeqNumPkts_Type = Counter64
_WwpLeosBenchmarkFpgaStatsDiscSeqNumPkts_Object = MibScalar
wwpLeosBenchmarkFpgaStatsDiscSeqNumPkts = _WwpLeosBenchmarkFpgaStatsDiscSeqNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 4, 9),
    _WwpLeosBenchmarkFpgaStatsDiscSeqNumPkts_Type()
)
wwpLeosBenchmarkFpgaStatsDiscSeqNumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkFpgaStatsDiscSeqNumPkts.setStatus("current")
_WwpLeosBenchmarkPortStats_ObjectIdentity = ObjectIdentity
wwpLeosBenchmarkPortStats = _WwpLeosBenchmarkPortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5)
)
_WwpLeosBenchmarkPortStatsTxBytes_Type = Counter64
_WwpLeosBenchmarkPortStatsTxBytes_Object = MibScalar
wwpLeosBenchmarkPortStatsTxBytes = _WwpLeosBenchmarkPortStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 1),
    _WwpLeosBenchmarkPortStatsTxBytes_Type()
)
wwpLeosBenchmarkPortStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsTxBytes.setStatus("current")
_WwpLeosBenchmarkPortStatsTxPkts_Type = Counter64
_WwpLeosBenchmarkPortStatsTxPkts_Object = MibScalar
wwpLeosBenchmarkPortStatsTxPkts = _WwpLeosBenchmarkPortStatsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 2),
    _WwpLeosBenchmarkPortStatsTxPkts_Type()
)
wwpLeosBenchmarkPortStatsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsTxPkts.setStatus("current")
_WwpLeosBenchmarkPortStatsCrcErrorPkts_Type = Counter64
_WwpLeosBenchmarkPortStatsCrcErrorPkts_Object = MibScalar
wwpLeosBenchmarkPortStatsCrcErrorPkts = _WwpLeosBenchmarkPortStatsCrcErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 3),
    _WwpLeosBenchmarkPortStatsCrcErrorPkts_Type()
)
wwpLeosBenchmarkPortStatsCrcErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsCrcErrorPkts.setStatus("current")
_WwpLeosBenchmarkPortStatsUcastPkts_Type = Counter64
_WwpLeosBenchmarkPortStatsUcastPkts_Object = MibScalar
wwpLeosBenchmarkPortStatsUcastPkts = _WwpLeosBenchmarkPortStatsUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 4),
    _WwpLeosBenchmarkPortStatsUcastPkts_Type()
)
wwpLeosBenchmarkPortStatsUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsUcastPkts.setStatus("current")
_WwpLeosBenchmarkPortStatsMcastPkts_Type = Counter64
_WwpLeosBenchmarkPortStatsMcastPkts_Object = MibScalar
wwpLeosBenchmarkPortStatsMcastPkts = _WwpLeosBenchmarkPortStatsMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 5),
    _WwpLeosBenchmarkPortStatsMcastPkts_Type()
)
wwpLeosBenchmarkPortStatsMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsMcastPkts.setStatus("current")
_WwpLeosBenchmarkPortStatsBcastPkts_Type = Counter64
_WwpLeosBenchmarkPortStatsBcastPkts_Object = MibScalar
wwpLeosBenchmarkPortStatsBcastPkts = _WwpLeosBenchmarkPortStatsBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 6),
    _WwpLeosBenchmarkPortStatsBcastPkts_Type()
)
wwpLeosBenchmarkPortStatsBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsBcastPkts.setStatus("current")
_WwpLeosBenchmarkPortStatsUndersizePkts_Type = Counter64
_WwpLeosBenchmarkPortStatsUndersizePkts_Object = MibScalar
wwpLeosBenchmarkPortStatsUndersizePkts = _WwpLeosBenchmarkPortStatsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 7),
    _WwpLeosBenchmarkPortStatsUndersizePkts_Type()
)
wwpLeosBenchmarkPortStatsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsUndersizePkts.setStatus("current")
_WwpLeosBenchmarkPortStatsOversizePkts_Type = Counter64
_WwpLeosBenchmarkPortStatsOversizePkts_Object = MibScalar
wwpLeosBenchmarkPortStatsOversizePkts = _WwpLeosBenchmarkPortStatsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 8),
    _WwpLeosBenchmarkPortStatsOversizePkts_Type()
)
wwpLeosBenchmarkPortStatsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsOversizePkts.setStatus("current")
_WwpLeosBenchmarkPortStatsFragmentsPkts_Type = Counter64
_WwpLeosBenchmarkPortStatsFragmentsPkts_Object = MibScalar
wwpLeosBenchmarkPortStatsFragmentsPkts = _WwpLeosBenchmarkPortStatsFragmentsPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 9),
    _WwpLeosBenchmarkPortStatsFragmentsPkts_Type()
)
wwpLeosBenchmarkPortStatsFragmentsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsFragmentsPkts.setStatus("current")
_WwpLeosBenchmarkPortStatsJabbersPkts_Type = Counter64
_WwpLeosBenchmarkPortStatsJabbersPkts_Object = MibScalar
wwpLeosBenchmarkPortStatsJabbersPkts = _WwpLeosBenchmarkPortStatsJabbersPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 10),
    _WwpLeosBenchmarkPortStatsJabbersPkts_Type()
)
wwpLeosBenchmarkPortStatsJabbersPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsJabbersPkts.setStatus("current")
_WwpLeosBenchmarkPortStatsTxPausePkts_Type = Counter64
_WwpLeosBenchmarkPortStatsTxPausePkts_Object = MibScalar
wwpLeosBenchmarkPortStatsTxPausePkts = _WwpLeosBenchmarkPortStatsTxPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 11),
    _WwpLeosBenchmarkPortStatsTxPausePkts_Type()
)
wwpLeosBenchmarkPortStatsTxPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsTxPausePkts.setStatus("current")
_WwpLeosBenchmarkPortStatsTxDropPkts_Type = Counter64
_WwpLeosBenchmarkPortStatsTxDropPkts_Object = MibScalar
wwpLeosBenchmarkPortStatsTxDropPkts = _WwpLeosBenchmarkPortStatsTxDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 12),
    _WwpLeosBenchmarkPortStatsTxDropPkts_Type()
)
wwpLeosBenchmarkPortStatsTxDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsTxDropPkts.setStatus("current")
_WwpLeosBenchmarkPortStatsTxDiscardPkts_Type = Counter64
_WwpLeosBenchmarkPortStatsTxDiscardPkts_Object = MibScalar
wwpLeosBenchmarkPortStatsTxDiscardPkts = _WwpLeosBenchmarkPortStatsTxDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 13),
    _WwpLeosBenchmarkPortStatsTxDiscardPkts_Type()
)
wwpLeosBenchmarkPortStatsTxDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsTxDiscardPkts.setStatus("current")
_WwpLeosBenchmarkPortStatsTxLOutRangePkts_Type = Counter64
_WwpLeosBenchmarkPortStatsTxLOutRangePkts_Object = MibScalar
wwpLeosBenchmarkPortStatsTxLOutRangePkts = _WwpLeosBenchmarkPortStatsTxLOutRangePkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 14),
    _WwpLeosBenchmarkPortStatsTxLOutRangePkts_Type()
)
wwpLeosBenchmarkPortStatsTxLOutRangePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsTxLOutRangePkts.setStatus("current")
_WwpLeosBenchmarkPortStatsTx64OctsPkts_Type = Counter64
_WwpLeosBenchmarkPortStatsTx64OctsPkts_Object = MibScalar
wwpLeosBenchmarkPortStatsTx64OctsPkts = _WwpLeosBenchmarkPortStatsTx64OctsPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 15),
    _WwpLeosBenchmarkPortStatsTx64OctsPkts_Type()
)
wwpLeosBenchmarkPortStatsTx64OctsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsTx64OctsPkts.setStatus("current")
_WwpLeosBenchmarkPortStatsTx65To127Pkts_Type = Counter64
_WwpLeosBenchmarkPortStatsTx65To127Pkts_Object = MibScalar
wwpLeosBenchmarkPortStatsTx65To127Pkts = _WwpLeosBenchmarkPortStatsTx65To127Pkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 16),
    _WwpLeosBenchmarkPortStatsTx65To127Pkts_Type()
)
wwpLeosBenchmarkPortStatsTx65To127Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsTx65To127Pkts.setStatus("current")
_WwpLeosBenchmarkPortStatsTx128To255Pkts_Type = Counter64
_WwpLeosBenchmarkPortStatsTx128To255Pkts_Object = MibScalar
wwpLeosBenchmarkPortStatsTx128To255Pkts = _WwpLeosBenchmarkPortStatsTx128To255Pkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 17),
    _WwpLeosBenchmarkPortStatsTx128To255Pkts_Type()
)
wwpLeosBenchmarkPortStatsTx128To255Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsTx128To255Pkts.setStatus("current")
_WwpLeosBenchmarkPortStatsTx256To511Pkts_Type = Counter64
_WwpLeosBenchmarkPortStatsTx256To511Pkts_Object = MibScalar
wwpLeosBenchmarkPortStatsTx256To511Pkts = _WwpLeosBenchmarkPortStatsTx256To511Pkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 18),
    _WwpLeosBenchmarkPortStatsTx256To511Pkts_Type()
)
wwpLeosBenchmarkPortStatsTx256To511Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsTx256To511Pkts.setStatus("current")
_WwpLeosBenchmarkPortStatsTx512To1023Pkts_Type = Counter64
_WwpLeosBenchmarkPortStatsTx512To1023Pkts_Object = MibScalar
wwpLeosBenchmarkPortStatsTx512To1023Pkts = _WwpLeosBenchmarkPortStatsTx512To1023Pkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 19),
    _WwpLeosBenchmarkPortStatsTx512To1023Pkts_Type()
)
wwpLeosBenchmarkPortStatsTx512To1023Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsTx512To1023Pkts.setStatus("current")
_WwpLeosBenchmarkPortStatsTx1024To1518Pkts_Type = Counter64
_WwpLeosBenchmarkPortStatsTx1024To1518Pkts_Object = MibScalar
wwpLeosBenchmarkPortStatsTx1024To1518Pkts = _WwpLeosBenchmarkPortStatsTx1024To1518Pkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 20),
    _WwpLeosBenchmarkPortStatsTx1024To1518Pkts_Type()
)
wwpLeosBenchmarkPortStatsTx1024To1518Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsTx1024To1518Pkts.setStatus("current")
_WwpLeosBenchmarkPortStatsTx1519To2047Pkts_Type = Counter64
_WwpLeosBenchmarkPortStatsTx1519To2047Pkts_Object = MibScalar
wwpLeosBenchmarkPortStatsTx1519To2047Pkts = _WwpLeosBenchmarkPortStatsTx1519To2047Pkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 21),
    _WwpLeosBenchmarkPortStatsTx1519To2047Pkts_Type()
)
wwpLeosBenchmarkPortStatsTx1519To2047Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsTx1519To2047Pkts.setStatus("current")
_WwpLeosBenchmarkPortStatsTx2048To4095Pkts_Type = Counter64
_WwpLeosBenchmarkPortStatsTx2048To4095Pkts_Object = MibScalar
wwpLeosBenchmarkPortStatsTx2048To4095Pkts = _WwpLeosBenchmarkPortStatsTx2048To4095Pkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 22),
    _WwpLeosBenchmarkPortStatsTx2048To4095Pkts_Type()
)
wwpLeosBenchmarkPortStatsTx2048To4095Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsTx2048To4095Pkts.setStatus("current")
_WwpLeosBenchmarkPortStatsTx4096To9216Pkts_Type = Counter64
_WwpLeosBenchmarkPortStatsTx4096To9216Pkts_Object = MibScalar
wwpLeosBenchmarkPortStatsTx4096To9216Pkts = _WwpLeosBenchmarkPortStatsTx4096To9216Pkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 23),
    _WwpLeosBenchmarkPortStatsTx4096To9216Pkts_Type()
)
wwpLeosBenchmarkPortStatsTx4096To9216Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsTx4096To9216Pkts.setStatus("current")
_WwpLeosBenchmarkPortStatsRxBytes_Type = Counter64
_WwpLeosBenchmarkPortStatsRxBytes_Object = MibScalar
wwpLeosBenchmarkPortStatsRxBytes = _WwpLeosBenchmarkPortStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 24),
    _WwpLeosBenchmarkPortStatsRxBytes_Type()
)
wwpLeosBenchmarkPortStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsRxBytes.setStatus("current")
_WwpLeosBenchmarkPortStatsRxPkts_Type = Counter64
_WwpLeosBenchmarkPortStatsRxPkts_Object = MibScalar
wwpLeosBenchmarkPortStatsRxPkts = _WwpLeosBenchmarkPortStatsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 25),
    _WwpLeosBenchmarkPortStatsRxPkts_Type()
)
wwpLeosBenchmarkPortStatsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsRxPkts.setStatus("current")
_WwpLeosBenchmarkPortStatsRxExDeferPkts_Type = Counter64
_WwpLeosBenchmarkPortStatsRxExDeferPkts_Object = MibScalar
wwpLeosBenchmarkPortStatsRxExDeferPkts = _WwpLeosBenchmarkPortStatsRxExDeferPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 26),
    _WwpLeosBenchmarkPortStatsRxExDeferPkts_Type()
)
wwpLeosBenchmarkPortStatsRxExDeferPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsRxExDeferPkts.setStatus("current")
_WwpLeosBenchmarkPortStatsRxDeferPkts_Type = Counter64
_WwpLeosBenchmarkPortStatsRxDeferPkts_Object = MibScalar
wwpLeosBenchmarkPortStatsRxDeferPkts = _WwpLeosBenchmarkPortStatsRxDeferPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 27),
    _WwpLeosBenchmarkPortStatsRxDeferPkts_Type()
)
wwpLeosBenchmarkPortStatsRxDeferPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsRxDeferPkts.setStatus("current")
_WwpLeosBenchmarkPortStatsRxGiantPkts_Type = Counter64
_WwpLeosBenchmarkPortStatsRxGiantPkts_Object = MibScalar
wwpLeosBenchmarkPortStatsRxGiantPkts = _WwpLeosBenchmarkPortStatsRxGiantPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 28),
    _WwpLeosBenchmarkPortStatsRxGiantPkts_Type()
)
wwpLeosBenchmarkPortStatsRxGiantPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsRxGiantPkts.setStatus("current")
_WwpLeosBenchmarkPortStatsRxUnderRunPkts_Type = Counter64
_WwpLeosBenchmarkPortStatsRxUnderRunPkts_Object = MibScalar
wwpLeosBenchmarkPortStatsRxUnderRunPkts = _WwpLeosBenchmarkPortStatsRxUnderRunPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 29),
    _WwpLeosBenchmarkPortStatsRxUnderRunPkts_Type()
)
wwpLeosBenchmarkPortStatsRxUnderRunPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsRxUnderRunPkts.setStatus("current")
_WwpLeosBenchmarkPortStatsRxCrcErrorPkts_Type = Counter64
_WwpLeosBenchmarkPortStatsRxCrcErrorPkts_Object = MibScalar
wwpLeosBenchmarkPortStatsRxCrcErrorPkts = _WwpLeosBenchmarkPortStatsRxCrcErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 30),
    _WwpLeosBenchmarkPortStatsRxCrcErrorPkts_Type()
)
wwpLeosBenchmarkPortStatsRxCrcErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsRxCrcErrorPkts.setStatus("current")
_WwpLeosBenchmarkPortStatsRxLCheckErrorPkts_Type = Counter64
_WwpLeosBenchmarkPortStatsRxLCheckErrorPkts_Object = MibScalar
wwpLeosBenchmarkPortStatsRxLCheckErrorPkts = _WwpLeosBenchmarkPortStatsRxLCheckErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 31),
    _WwpLeosBenchmarkPortStatsRxLCheckErrorPkts_Type()
)
wwpLeosBenchmarkPortStatsRxLCheckErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsRxLCheckErrorPkts.setStatus("current")
_WwpLeosBenchmarkPortStatsRxLOutRangePkts_Type = Counter64
_WwpLeosBenchmarkPortStatsRxLOutRangePkts_Object = MibScalar
wwpLeosBenchmarkPortStatsRxLOutRangePkts = _WwpLeosBenchmarkPortStatsRxLOutRangePkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 32),
    _WwpLeosBenchmarkPortStatsRxLOutRangePkts_Type()
)
wwpLeosBenchmarkPortStatsRxLOutRangePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsRxLOutRangePkts.setStatus("current")
_WwpLeosBenchmarkPortStatsRxPausePkts_Type = Counter64
_WwpLeosBenchmarkPortStatsRxPausePkts_Object = MibScalar
wwpLeosBenchmarkPortStatsRxPausePkts = _WwpLeosBenchmarkPortStatsRxPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 33),
    _WwpLeosBenchmarkPortStatsRxPausePkts_Type()
)
wwpLeosBenchmarkPortStatsRxPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsRxPausePkts.setStatus("current")
_WwpLeosBenchmarkPortStatsRxUcastPkts_Type = Counter64
_WwpLeosBenchmarkPortStatsRxUcastPkts_Object = MibScalar
wwpLeosBenchmarkPortStatsRxUcastPkts = _WwpLeosBenchmarkPortStatsRxUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 34),
    _WwpLeosBenchmarkPortStatsRxUcastPkts_Type()
)
wwpLeosBenchmarkPortStatsRxUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsRxUcastPkts.setStatus("current")
_WwpLeosBenchmarkPortStatsRxMcastPkts_Type = Counter64
_WwpLeosBenchmarkPortStatsRxMcastPkts_Object = MibScalar
wwpLeosBenchmarkPortStatsRxMcastPkts = _WwpLeosBenchmarkPortStatsRxMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 35),
    _WwpLeosBenchmarkPortStatsRxMcastPkts_Type()
)
wwpLeosBenchmarkPortStatsRxMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsRxMcastPkts.setStatus("current")
_WwpLeosBenchmarkPortStatsRxBcastPkts_Type = Counter64
_WwpLeosBenchmarkPortStatsRxBcastPkts_Object = MibScalar
wwpLeosBenchmarkPortStatsRxBcastPkts = _WwpLeosBenchmarkPortStatsRxBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 36),
    _WwpLeosBenchmarkPortStatsRxBcastPkts_Type()
)
wwpLeosBenchmarkPortStatsRxBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsRxBcastPkts.setStatus("current")
_WwpLeosBenchmarkPortStatsRx64Pkts_Type = Counter64
_WwpLeosBenchmarkPortStatsRx64Pkts_Object = MibScalar
wwpLeosBenchmarkPortStatsRx64Pkts = _WwpLeosBenchmarkPortStatsRx64Pkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 37),
    _WwpLeosBenchmarkPortStatsRx64Pkts_Type()
)
wwpLeosBenchmarkPortStatsRx64Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsRx64Pkts.setStatus("current")
_WwpLeosBenchmarkPortStatsRx65To127Pkts_Type = Counter64
_WwpLeosBenchmarkPortStatsRx65To127Pkts_Object = MibScalar
wwpLeosBenchmarkPortStatsRx65To127Pkts = _WwpLeosBenchmarkPortStatsRx65To127Pkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 38),
    _WwpLeosBenchmarkPortStatsRx65To127Pkts_Type()
)
wwpLeosBenchmarkPortStatsRx65To127Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsRx65To127Pkts.setStatus("current")
_WwpLeosBenchmarkPortStatsRx128To255Pkts_Type = Counter64
_WwpLeosBenchmarkPortStatsRx128To255Pkts_Object = MibScalar
wwpLeosBenchmarkPortStatsRx128To255Pkts = _WwpLeosBenchmarkPortStatsRx128To255Pkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 39),
    _WwpLeosBenchmarkPortStatsRx128To255Pkts_Type()
)
wwpLeosBenchmarkPortStatsRx128To255Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsRx128To255Pkts.setStatus("current")
_WwpLeosBenchmarkPortStatsRx256To511Pkts_Type = Counter64
_WwpLeosBenchmarkPortStatsRx256To511Pkts_Object = MibScalar
wwpLeosBenchmarkPortStatsRx256To511Pkts = _WwpLeosBenchmarkPortStatsRx256To511Pkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 40),
    _WwpLeosBenchmarkPortStatsRx256To511Pkts_Type()
)
wwpLeosBenchmarkPortStatsRx256To511Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsRx256To511Pkts.setStatus("current")
_WwpLeosBenchmarkPortStatsRx512To1023Pkts_Type = Counter64
_WwpLeosBenchmarkPortStatsRx512To1023Pkts_Object = MibScalar
wwpLeosBenchmarkPortStatsRx512To1023Pkts = _WwpLeosBenchmarkPortStatsRx512To1023Pkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 41),
    _WwpLeosBenchmarkPortStatsRx512To1023Pkts_Type()
)
wwpLeosBenchmarkPortStatsRx512To1023Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsRx512To1023Pkts.setStatus("current")
_WwpLeosBenchmarkPortStatsRx1024To1518Pkts_Type = Counter64
_WwpLeosBenchmarkPortStatsRx1024To1518Pkts_Object = MibScalar
wwpLeosBenchmarkPortStatsRx1024To1518Pkts = _WwpLeosBenchmarkPortStatsRx1024To1518Pkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 42),
    _WwpLeosBenchmarkPortStatsRx1024To1518Pkts_Type()
)
wwpLeosBenchmarkPortStatsRx1024To1518Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsRx1024To1518Pkts.setStatus("current")
_WwpLeosBenchmarkPortStatsRx1519To2047Pkts_Type = Counter64
_WwpLeosBenchmarkPortStatsRx1519To2047Pkts_Object = MibScalar
wwpLeosBenchmarkPortStatsRx1519To2047Pkts = _WwpLeosBenchmarkPortStatsRx1519To2047Pkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 43),
    _WwpLeosBenchmarkPortStatsRx1519To2047Pkts_Type()
)
wwpLeosBenchmarkPortStatsRx1519To2047Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsRx1519To2047Pkts.setStatus("current")
_WwpLeosBenchmarkPortStatsRx2048To4095Pkts_Type = Counter64
_WwpLeosBenchmarkPortStatsRx2048To4095Pkts_Object = MibScalar
wwpLeosBenchmarkPortStatsRx2048To4095Pkts = _WwpLeosBenchmarkPortStatsRx2048To4095Pkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 44),
    _WwpLeosBenchmarkPortStatsRx2048To4095Pkts_Type()
)
wwpLeosBenchmarkPortStatsRx2048To4095Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsRx2048To4095Pkts.setStatus("current")
_WwpLeosBenchmarkPortStatsRx4096To9216Pkts_Type = Counter64
_WwpLeosBenchmarkPortStatsRx4096To9216Pkts_Object = MibScalar
wwpLeosBenchmarkPortStatsRx4096To9216Pkts = _WwpLeosBenchmarkPortStatsRx4096To9216Pkts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 5, 45),
    _WwpLeosBenchmarkPortStatsRx4096To9216Pkts_Type()
)
wwpLeosBenchmarkPortStatsRx4096To9216Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkPortStatsRx4096To9216Pkts.setStatus("current")
_WwpLeosBenchmarkProfileObjects_ObjectIdentity = ObjectIdentity
wwpLeosBenchmarkProfileObjects = _WwpLeosBenchmarkProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6)
)
_WwpLeosBenchmarkProfileTable_Object = MibTable
wwpLeosBenchmarkProfileTable = _WwpLeosBenchmarkProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 1)
)
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileTable.setStatus("current")
_WwpLeosBenchmarkProfileEntry_Object = MibTableRow
wwpLeosBenchmarkProfileEntry = _WwpLeosBenchmarkProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 1, 1)
)
wwpLeosBenchmarkProfileEntry.setIndexNames(
    (0, "WWP-LEOS-BENCHMARK-MIB", "wwpLeosBenchmarkProfileEntryId"),
)
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileEntry.setStatus("current")


class _WwpLeosBenchmarkProfileEntryId_Type(Integer32):
    """Custom type wwpLeosBenchmarkProfileEntryId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_WwpLeosBenchmarkProfileEntryId_Type.__name__ = "Integer32"
_WwpLeosBenchmarkProfileEntryId_Object = MibTableColumn
wwpLeosBenchmarkProfileEntryId = _WwpLeosBenchmarkProfileEntryId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 1, 1, 1),
    _WwpLeosBenchmarkProfileEntryId_Type()
)
wwpLeosBenchmarkProfileEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileEntryId.setStatus("current")


class _WwpLeosBenchmarkProfileEntryName_Type(DisplayString):
    """Custom type wwpLeosBenchmarkProfileEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_WwpLeosBenchmarkProfileEntryName_Type.__name__ = "DisplayString"
_WwpLeosBenchmarkProfileEntryName_Object = MibTableColumn
wwpLeosBenchmarkProfileEntryName = _WwpLeosBenchmarkProfileEntryName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 1, 1, 2),
    _WwpLeosBenchmarkProfileEntryName_Type()
)
wwpLeosBenchmarkProfileEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileEntryName.setStatus("current")
_WwpLeosBenchmarkProfileEntryEnabled_Type = TruthValue
_WwpLeosBenchmarkProfileEntryEnabled_Object = MibTableColumn
wwpLeosBenchmarkProfileEntryEnabled = _WwpLeosBenchmarkProfileEntryEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 1, 1, 3),
    _WwpLeosBenchmarkProfileEntryEnabled_Type()
)
wwpLeosBenchmarkProfileEntryEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileEntryEnabled.setStatus("current")
_WwpLeosBenchmarkProfileEntryStarted_Type = TruthValue
_WwpLeosBenchmarkProfileEntryStarted_Object = MibTableColumn
wwpLeosBenchmarkProfileEntryStarted = _WwpLeosBenchmarkProfileEntryStarted_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 1, 1, 4),
    _WwpLeosBenchmarkProfileEntryStarted_Type()
)
wwpLeosBenchmarkProfileEntryStarted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileEntryStarted.setStatus("current")


class _WwpLeosBenchmarkProfileEntryInterval_Type(Integer32):
    """Custom type wwpLeosBenchmarkProfileEntryInterval based on Integer32"""
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
        *(("t15min", 1),
          ("t1hr", 2),
          ("t6hr", 3),
          ("tCompletion", 4))
    )


_WwpLeosBenchmarkProfileEntryInterval_Type.__name__ = "Integer32"
_WwpLeosBenchmarkProfileEntryInterval_Object = MibTableColumn
wwpLeosBenchmarkProfileEntryInterval = _WwpLeosBenchmarkProfileEntryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 1, 1, 5),
    _WwpLeosBenchmarkProfileEntryInterval_Type()
)
wwpLeosBenchmarkProfileEntryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileEntryInterval.setStatus("current")


class _WwpLeosBenchmarkProfileEntryDuration_Type(Integer32):
    """Custom type wwpLeosBenchmarkProfileEntryDuration based on Integer32"""
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
        *(("t15min", 1),
          ("t1hr", 2),
          ("t24hr", 4),
          ("t6hr", 3),
          ("tIndefinite", 5),
          ("tOnce", 6))
    )


_WwpLeosBenchmarkProfileEntryDuration_Type.__name__ = "Integer32"
_WwpLeosBenchmarkProfileEntryDuration_Object = MibTableColumn
wwpLeosBenchmarkProfileEntryDuration = _WwpLeosBenchmarkProfileEntryDuration_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 1, 1, 6),
    _WwpLeosBenchmarkProfileEntryDuration_Type()
)
wwpLeosBenchmarkProfileEntryDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileEntryDuration.setStatus("current")
_WwpLeosBenchmarkProfileEntryThroughputTest_Type = TruthValue
_WwpLeosBenchmarkProfileEntryThroughputTest_Object = MibTableColumn
wwpLeosBenchmarkProfileEntryThroughputTest = _WwpLeosBenchmarkProfileEntryThroughputTest_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 1, 1, 7),
    _WwpLeosBenchmarkProfileEntryThroughputTest_Type()
)
wwpLeosBenchmarkProfileEntryThroughputTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileEntryThroughputTest.setStatus("current")
_WwpLeosBenchmarkProfileEntryFramelossTest_Type = TruthValue
_WwpLeosBenchmarkProfileEntryFramelossTest_Object = MibTableColumn
wwpLeosBenchmarkProfileEntryFramelossTest = _WwpLeosBenchmarkProfileEntryFramelossTest_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 1, 1, 8),
    _WwpLeosBenchmarkProfileEntryFramelossTest_Type()
)
wwpLeosBenchmarkProfileEntryFramelossTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileEntryFramelossTest.setStatus("current")
_WwpLeosBenchmarkProfileEntryLatencyTest_Type = TruthValue
_WwpLeosBenchmarkProfileEntryLatencyTest_Object = MibTableColumn
wwpLeosBenchmarkProfileEntryLatencyTest = _WwpLeosBenchmarkProfileEntryLatencyTest_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 1, 1, 9),
    _WwpLeosBenchmarkProfileEntryLatencyTest_Type()
)
wwpLeosBenchmarkProfileEntryLatencyTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileEntryLatencyTest.setStatus("current")
_WwpLeosBenchmarkProfileEntryPdvTest_Type = TruthValue
_WwpLeosBenchmarkProfileEntryPdvTest_Object = MibTableColumn
wwpLeosBenchmarkProfileEntryPdvTest = _WwpLeosBenchmarkProfileEntryPdvTest_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 1, 1, 10),
    _WwpLeosBenchmarkProfileEntryPdvTest_Type()
)
wwpLeosBenchmarkProfileEntryPdvTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileEntryPdvTest.setStatus("current")
_WwpLeosBenchmarkProfileEntryRfc2544Suite_Type = TruthValue
_WwpLeosBenchmarkProfileEntryRfc2544Suite_Object = MibTableColumn
wwpLeosBenchmarkProfileEntryRfc2544Suite = _WwpLeosBenchmarkProfileEntryRfc2544Suite_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 1, 1, 11),
    _WwpLeosBenchmarkProfileEntryRfc2544Suite_Type()
)
wwpLeosBenchmarkProfileEntryRfc2544Suite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileEntryRfc2544Suite.setStatus("current")
_WwpLeosBenchmarkProfileEntryDstmac_Type = MacAddress
_WwpLeosBenchmarkProfileEntryDstmac_Object = MibTableColumn
wwpLeosBenchmarkProfileEntryDstmac = _WwpLeosBenchmarkProfileEntryDstmac_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 1, 1, 12),
    _WwpLeosBenchmarkProfileEntryDstmac_Type()
)
wwpLeosBenchmarkProfileEntryDstmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileEntryDstmac.setStatus("current")


class _WwpLeosBenchmarkProfileEntryEncapType_Type(Integer32):
    """Custom type wwpLeosBenchmarkProfileEntryEncapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot1q", 2),
          ("untagged", 1))
    )


_WwpLeosBenchmarkProfileEntryEncapType_Type.__name__ = "Integer32"
_WwpLeosBenchmarkProfileEntryEncapType_Object = MibTableColumn
wwpLeosBenchmarkProfileEntryEncapType = _WwpLeosBenchmarkProfileEntryEncapType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 1, 1, 13),
    _WwpLeosBenchmarkProfileEntryEncapType_Type()
)
wwpLeosBenchmarkProfileEntryEncapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileEntryEncapType.setStatus("current")


class _WwpLeosBenchmarkProfileEntryVid_Type(Integer32):
    """Custom type wwpLeosBenchmarkProfileEntryVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_WwpLeosBenchmarkProfileEntryVid_Type.__name__ = "Integer32"
_WwpLeosBenchmarkProfileEntryVid_Object = MibTableColumn
wwpLeosBenchmarkProfileEntryVid = _WwpLeosBenchmarkProfileEntryVid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 1, 1, 14),
    _WwpLeosBenchmarkProfileEntryVid_Type()
)
wwpLeosBenchmarkProfileEntryVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileEntryVid.setStatus("current")


class _WwpLeosBenchmarkProfileEntryPcp_Type(Integer32):
    """Custom type wwpLeosBenchmarkProfileEntryPcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosBenchmarkProfileEntryPcp_Type.__name__ = "Integer32"
_WwpLeosBenchmarkProfileEntryPcp_Object = MibTableColumn
wwpLeosBenchmarkProfileEntryPcp = _WwpLeosBenchmarkProfileEntryPcp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 1, 1, 15),
    _WwpLeosBenchmarkProfileEntryPcp_Type()
)
wwpLeosBenchmarkProfileEntryPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileEntryPcp.setStatus("current")


class _WwpLeosBenchmarkProfileEntryCfi_Type(Integer32):
    """Custom type wwpLeosBenchmarkProfileEntryCfi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_WwpLeosBenchmarkProfileEntryCfi_Type.__name__ = "Integer32"
_WwpLeosBenchmarkProfileEntryCfi_Object = MibTableColumn
wwpLeosBenchmarkProfileEntryCfi = _WwpLeosBenchmarkProfileEntryCfi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 1, 1, 16),
    _WwpLeosBenchmarkProfileEntryCfi_Type()
)
wwpLeosBenchmarkProfileEntryCfi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileEntryCfi.setStatus("current")


class _WwpLeosBenchmarkProfileEntryTpid_Type(Integer32):
    """Custom type wwpLeosBenchmarkProfileEntryTpid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosBenchmarkProfileEntryTpid_Type.__name__ = "Integer32"
_WwpLeosBenchmarkProfileEntryTpid_Object = MibTableColumn
wwpLeosBenchmarkProfileEntryTpid = _WwpLeosBenchmarkProfileEntryTpid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 1, 1, 17),
    _WwpLeosBenchmarkProfileEntryTpid_Type()
)
wwpLeosBenchmarkProfileEntryTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileEntryTpid.setStatus("current")


class _WwpLeosBenchmarkProfileEntryPduType_Type(Integer32):
    """Custom type wwpLeosBenchmarkProfileEntryPduType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("ip", 2),
          ("udpecho", 3))
    )


_WwpLeosBenchmarkProfileEntryPduType_Type.__name__ = "Integer32"
_WwpLeosBenchmarkProfileEntryPduType_Object = MibTableColumn
wwpLeosBenchmarkProfileEntryPduType = _WwpLeosBenchmarkProfileEntryPduType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 1, 1, 18),
    _WwpLeosBenchmarkProfileEntryPduType_Type()
)
wwpLeosBenchmarkProfileEntryPduType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileEntryPduType.setStatus("current")
_WwpLeosBenchmarkProfileEntrySrcIpAddr_Type = IpAddress
_WwpLeosBenchmarkProfileEntrySrcIpAddr_Object = MibTableColumn
wwpLeosBenchmarkProfileEntrySrcIpAddr = _WwpLeosBenchmarkProfileEntrySrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 1, 1, 19),
    _WwpLeosBenchmarkProfileEntrySrcIpAddr_Type()
)
wwpLeosBenchmarkProfileEntrySrcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileEntrySrcIpAddr.setStatus("current")
_WwpLeosBenchmarkProfileEntryDstIpAddr_Type = IpAddress
_WwpLeosBenchmarkProfileEntryDstIpAddr_Object = MibTableColumn
wwpLeosBenchmarkProfileEntryDstIpAddr = _WwpLeosBenchmarkProfileEntryDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 1, 1, 20),
    _WwpLeosBenchmarkProfileEntryDstIpAddr_Type()
)
wwpLeosBenchmarkProfileEntryDstIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileEntryDstIpAddr.setStatus("current")


class _WwpLeosBenchmarkProfileEntryDscp_Type(Integer32):
    """Custom type wwpLeosBenchmarkProfileEntryDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_WwpLeosBenchmarkProfileEntryDscp_Type.__name__ = "Integer32"
_WwpLeosBenchmarkProfileEntryDscp_Object = MibTableColumn
wwpLeosBenchmarkProfileEntryDscp = _WwpLeosBenchmarkProfileEntryDscp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 1, 1, 21),
    _WwpLeosBenchmarkProfileEntryDscp_Type()
)
wwpLeosBenchmarkProfileEntryDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileEntryDscp.setStatus("current")


class _WwpLeosBenchmarkProfileEntryCustomPayload_Type(OctetString):
    """Custom type wwpLeosBenchmarkProfileEntryCustomPayload based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_WwpLeosBenchmarkProfileEntryCustomPayload_Type.__name__ = "OctetString"
_WwpLeosBenchmarkProfileEntryCustomPayload_Object = MibTableColumn
wwpLeosBenchmarkProfileEntryCustomPayload = _WwpLeosBenchmarkProfileEntryCustomPayload_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 1, 1, 22),
    _WwpLeosBenchmarkProfileEntryCustomPayload_Type()
)
wwpLeosBenchmarkProfileEntryCustomPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileEntryCustomPayload.setStatus("current")


class _WwpLeosBenchmarkProfileEntryBandwidth_Type(Integer32):
    """Custom type wwpLeosBenchmarkProfileEntryBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WwpLeosBenchmarkProfileEntryBandwidth_Type.__name__ = "Integer32"
_WwpLeosBenchmarkProfileEntryBandwidth_Object = MibTableColumn
wwpLeosBenchmarkProfileEntryBandwidth = _WwpLeosBenchmarkProfileEntryBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 1, 1, 23),
    _WwpLeosBenchmarkProfileEntryBandwidth_Type()
)
wwpLeosBenchmarkProfileEntryBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileEntryBandwidth.setStatus("current")
_WwpLeosBenchmarkProfileEntryVidValidation_Type = TruthValue
_WwpLeosBenchmarkProfileEntryVidValidation_Object = MibTableColumn
wwpLeosBenchmarkProfileEntryVidValidation = _WwpLeosBenchmarkProfileEntryVidValidation_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 1, 1, 24),
    _WwpLeosBenchmarkProfileEntryVidValidation_Type()
)
wwpLeosBenchmarkProfileEntryVidValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileEntryVidValidation.setStatus("current")


class _WwpLeosBenchmarkProfileEntryMaxSearches_Type(Integer32):
    """Custom type wwpLeosBenchmarkProfileEntryMaxSearches based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_WwpLeosBenchmarkProfileEntryMaxSearches_Type.__name__ = "Integer32"
_WwpLeosBenchmarkProfileEntryMaxSearches_Object = MibTableColumn
wwpLeosBenchmarkProfileEntryMaxSearches = _WwpLeosBenchmarkProfileEntryMaxSearches_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 1, 1, 25),
    _WwpLeosBenchmarkProfileEntryMaxSearches_Type()
)
wwpLeosBenchmarkProfileEntryMaxSearches.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileEntryMaxSearches.setStatus("current")


class _WwpLeosBenchmarkProfileEntryMaxSamples_Type(Integer32):
    """Custom type wwpLeosBenchmarkProfileEntryMaxSamples based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 20),
    )


_WwpLeosBenchmarkProfileEntryMaxSamples_Type.__name__ = "Integer32"
_WwpLeosBenchmarkProfileEntryMaxSamples_Object = MibTableColumn
wwpLeosBenchmarkProfileEntryMaxSamples = _WwpLeosBenchmarkProfileEntryMaxSamples_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 1, 1, 26),
    _WwpLeosBenchmarkProfileEntryMaxSamples_Type()
)
wwpLeosBenchmarkProfileEntryMaxSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileEntryMaxSamples.setStatus("current")


class _WwpLeosBenchmarkProfileEntrySamplingInterval_Type(Integer32):
    """Custom type wwpLeosBenchmarkProfileEntrySamplingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_WwpLeosBenchmarkProfileEntrySamplingInterval_Type.__name__ = "Integer32"
_WwpLeosBenchmarkProfileEntrySamplingInterval_Object = MibTableColumn
wwpLeosBenchmarkProfileEntrySamplingInterval = _WwpLeosBenchmarkProfileEntrySamplingInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 1, 1, 27),
    _WwpLeosBenchmarkProfileEntrySamplingInterval_Type()
)
wwpLeosBenchmarkProfileEntrySamplingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileEntrySamplingInterval.setStatus("current")


class _WwpLeosBenchmarkProfileEntryFrameLossStartBw_Type(Integer32):
    """Custom type wwpLeosBenchmarkProfileEntryFrameLossStartBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("maximumLineRate", 3),
          ("maximumThroughput", 2),
          ("profileBandwidth", 1))
    )


_WwpLeosBenchmarkProfileEntryFrameLossStartBw_Type.__name__ = "Integer32"
_WwpLeosBenchmarkProfileEntryFrameLossStartBw_Object = MibTableColumn
wwpLeosBenchmarkProfileEntryFrameLossStartBw = _WwpLeosBenchmarkProfileEntryFrameLossStartBw_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 1, 1, 28),
    _WwpLeosBenchmarkProfileEntryFrameLossStartBw_Type()
)
wwpLeosBenchmarkProfileEntryFrameLossStartBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileEntryFrameLossStartBw.setStatus("current")
_WwpLeosBenchmarkProfileThroughputStatisticsTable_Object = MibTable
wwpLeosBenchmarkProfileThroughputStatisticsTable = _WwpLeosBenchmarkProfileThroughputStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 2)
)
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileThroughputStatisticsTable.setStatus("current")
_WwpLeosBenchmarkProfileThroughputStatsEntry_Object = MibTableRow
wwpLeosBenchmarkProfileThroughputStatsEntry = _WwpLeosBenchmarkProfileThroughputStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 2, 1)
)
wwpLeosBenchmarkProfileThroughputStatsEntry.setIndexNames(
    (0, "WWP-LEOS-BENCHMARK-MIB", "wwpLeosBenchmarkProfileThroughputStatsProfileId"),
    (0, "WWP-LEOS-BENCHMARK-MIB", "wwpLeosBenchmarkProfileThroughputStatsFrameSizeIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileThroughputStatsEntry.setStatus("current")


class _WwpLeosBenchmarkProfileThroughputStatsProfileId_Type(Integer32):
    """Custom type wwpLeosBenchmarkProfileThroughputStatsProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_WwpLeosBenchmarkProfileThroughputStatsProfileId_Type.__name__ = "Integer32"
_WwpLeosBenchmarkProfileThroughputStatsProfileId_Object = MibTableColumn
wwpLeosBenchmarkProfileThroughputStatsProfileId = _WwpLeosBenchmarkProfileThroughputStatsProfileId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 2, 1, 1),
    _WwpLeosBenchmarkProfileThroughputStatsProfileId_Type()
)
wwpLeosBenchmarkProfileThroughputStatsProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileThroughputStatsProfileId.setStatus("current")


class _WwpLeosBenchmarkProfileThroughputStatsFrameSizeIndex_Type(Integer32):
    """Custom type wwpLeosBenchmarkProfileThroughputStatsFrameSizeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_WwpLeosBenchmarkProfileThroughputStatsFrameSizeIndex_Type.__name__ = "Integer32"
_WwpLeosBenchmarkProfileThroughputStatsFrameSizeIndex_Object = MibTableColumn
wwpLeosBenchmarkProfileThroughputStatsFrameSizeIndex = _WwpLeosBenchmarkProfileThroughputStatsFrameSizeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 2, 1, 2),
    _WwpLeosBenchmarkProfileThroughputStatsFrameSizeIndex_Type()
)
wwpLeosBenchmarkProfileThroughputStatsFrameSizeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileThroughputStatsFrameSizeIndex.setStatus("current")
_WwpLeosBenchmarkProfileThroughputStatsFrameSize_Type = Integer32
_WwpLeosBenchmarkProfileThroughputStatsFrameSize_Object = MibTableColumn
wwpLeosBenchmarkProfileThroughputStatsFrameSize = _WwpLeosBenchmarkProfileThroughputStatsFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 2, 1, 3),
    _WwpLeosBenchmarkProfileThroughputStatsFrameSize_Type()
)
wwpLeosBenchmarkProfileThroughputStatsFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileThroughputStatsFrameSize.setStatus("current")
_WwpLeosBenchmarkProfileThroughputStatsMin_Type = Unsigned32
_WwpLeosBenchmarkProfileThroughputStatsMin_Object = MibTableColumn
wwpLeosBenchmarkProfileThroughputStatsMin = _WwpLeosBenchmarkProfileThroughputStatsMin_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 2, 1, 4),
    _WwpLeosBenchmarkProfileThroughputStatsMin_Type()
)
wwpLeosBenchmarkProfileThroughputStatsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileThroughputStatsMin.setStatus("current")
_WwpLeosBenchmarkProfileThroughputStatsMax_Type = Unsigned32
_WwpLeosBenchmarkProfileThroughputStatsMax_Object = MibTableColumn
wwpLeosBenchmarkProfileThroughputStatsMax = _WwpLeosBenchmarkProfileThroughputStatsMax_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 2, 1, 5),
    _WwpLeosBenchmarkProfileThroughputStatsMax_Type()
)
wwpLeosBenchmarkProfileThroughputStatsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileThroughputStatsMax.setStatus("current")
_WwpLeosBenchmarkProfileThroughputStatsAvg_Type = Unsigned32
_WwpLeosBenchmarkProfileThroughputStatsAvg_Object = MibTableColumn
wwpLeosBenchmarkProfileThroughputStatsAvg = _WwpLeosBenchmarkProfileThroughputStatsAvg_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 2, 1, 6),
    _WwpLeosBenchmarkProfileThroughputStatsAvg_Type()
)
wwpLeosBenchmarkProfileThroughputStatsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileThroughputStatsAvg.setStatus("current")
_WwpLeosBenchmarkProfileThroughputStatsIterations_Type = Integer32
_WwpLeosBenchmarkProfileThroughputStatsIterations_Object = MibTableColumn
wwpLeosBenchmarkProfileThroughputStatsIterations = _WwpLeosBenchmarkProfileThroughputStatsIterations_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 2, 1, 7),
    _WwpLeosBenchmarkProfileThroughputStatsIterations_Type()
)
wwpLeosBenchmarkProfileThroughputStatsIterations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileThroughputStatsIterations.setStatus("current")


class _WwpLeosBenchmarkProfileThroughputStatsActiveVid_Type(Integer32):
    """Custom type wwpLeosBenchmarkProfileThroughputStatsActiveVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_WwpLeosBenchmarkProfileThroughputStatsActiveVid_Type.__name__ = "Integer32"
_WwpLeosBenchmarkProfileThroughputStatsActiveVid_Object = MibTableColumn
wwpLeosBenchmarkProfileThroughputStatsActiveVid = _WwpLeosBenchmarkProfileThroughputStatsActiveVid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 2, 1, 8),
    _WwpLeosBenchmarkProfileThroughputStatsActiveVid_Type()
)
wwpLeosBenchmarkProfileThroughputStatsActiveVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileThroughputStatsActiveVid.setStatus("current")
_WwpLeosBenchmarkProfileThroughputStatsActiveDstMac_Type = MacAddress
_WwpLeosBenchmarkProfileThroughputStatsActiveDstMac_Object = MibTableColumn
wwpLeosBenchmarkProfileThroughputStatsActiveDstMac = _WwpLeosBenchmarkProfileThroughputStatsActiveDstMac_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 2, 1, 9),
    _WwpLeosBenchmarkProfileThroughputStatsActiveDstMac_Type()
)
wwpLeosBenchmarkProfileThroughputStatsActiveDstMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileThroughputStatsActiveDstMac.setStatus("current")
_WwpLeosBenchmarkProfileFramelossStatisticsTable_Object = MibTable
wwpLeosBenchmarkProfileFramelossStatisticsTable = _WwpLeosBenchmarkProfileFramelossStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 3)
)
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileFramelossStatisticsTable.setStatus("current")
_WwpLeosBenchmarkProfileFramelossStatsEntry_Object = MibTableRow
wwpLeosBenchmarkProfileFramelossStatsEntry = _WwpLeosBenchmarkProfileFramelossStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 3, 1)
)
wwpLeosBenchmarkProfileFramelossStatsEntry.setIndexNames(
    (0, "WWP-LEOS-BENCHMARK-MIB", "wwpLeosBenchmarkProfileFramelossStatsProfileId"),
    (0, "WWP-LEOS-BENCHMARK-MIB", "wwpLeosBenchmarkProfileFramelossStatsFrameSizeIndex"),
    (0, "WWP-LEOS-BENCHMARK-MIB", "wwpLeosBenchmarkProfileFramelossStatsRateIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileFramelossStatsEntry.setStatus("current")


class _WwpLeosBenchmarkProfileFramelossStatsProfileId_Type(Integer32):
    """Custom type wwpLeosBenchmarkProfileFramelossStatsProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_WwpLeosBenchmarkProfileFramelossStatsProfileId_Type.__name__ = "Integer32"
_WwpLeosBenchmarkProfileFramelossStatsProfileId_Object = MibTableColumn
wwpLeosBenchmarkProfileFramelossStatsProfileId = _WwpLeosBenchmarkProfileFramelossStatsProfileId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 3, 1, 1),
    _WwpLeosBenchmarkProfileFramelossStatsProfileId_Type()
)
wwpLeosBenchmarkProfileFramelossStatsProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileFramelossStatsProfileId.setStatus("current")


class _WwpLeosBenchmarkProfileFramelossStatsFrameSizeIndex_Type(Integer32):
    """Custom type wwpLeosBenchmarkProfileFramelossStatsFrameSizeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_WwpLeosBenchmarkProfileFramelossStatsFrameSizeIndex_Type.__name__ = "Integer32"
_WwpLeosBenchmarkProfileFramelossStatsFrameSizeIndex_Object = MibTableColumn
wwpLeosBenchmarkProfileFramelossStatsFrameSizeIndex = _WwpLeosBenchmarkProfileFramelossStatsFrameSizeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 3, 1, 2),
    _WwpLeosBenchmarkProfileFramelossStatsFrameSizeIndex_Type()
)
wwpLeosBenchmarkProfileFramelossStatsFrameSizeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileFramelossStatsFrameSizeIndex.setStatus("current")


class _WwpLeosBenchmarkProfileFramelossStatsRateIndex_Type(Integer32):
    """Custom type wwpLeosBenchmarkProfileFramelossStatsRateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_WwpLeosBenchmarkProfileFramelossStatsRateIndex_Type.__name__ = "Integer32"
_WwpLeosBenchmarkProfileFramelossStatsRateIndex_Object = MibTableColumn
wwpLeosBenchmarkProfileFramelossStatsRateIndex = _WwpLeosBenchmarkProfileFramelossStatsRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 3, 1, 3),
    _WwpLeosBenchmarkProfileFramelossStatsRateIndex_Type()
)
wwpLeosBenchmarkProfileFramelossStatsRateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileFramelossStatsRateIndex.setStatus("current")
_WwpLeosBenchmarkProfileFramelossStatsFrameSize_Type = Integer32
_WwpLeosBenchmarkProfileFramelossStatsFrameSize_Object = MibTableColumn
wwpLeosBenchmarkProfileFramelossStatsFrameSize = _WwpLeosBenchmarkProfileFramelossStatsFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 3, 1, 4),
    _WwpLeosBenchmarkProfileFramelossStatsFrameSize_Type()
)
wwpLeosBenchmarkProfileFramelossStatsFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileFramelossStatsFrameSize.setStatus("current")
_WwpLeosBenchmarkProfileFramelossStatsRate_Type = Integer32
_WwpLeosBenchmarkProfileFramelossStatsRate_Object = MibTableColumn
wwpLeosBenchmarkProfileFramelossStatsRate = _WwpLeosBenchmarkProfileFramelossStatsRate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 3, 1, 5),
    _WwpLeosBenchmarkProfileFramelossStatsRate_Type()
)
wwpLeosBenchmarkProfileFramelossStatsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileFramelossStatsRate.setStatus("current")
_WwpLeosBenchmarkProfileFramelossStatsFirst_Type = Unsigned32
_WwpLeosBenchmarkProfileFramelossStatsFirst_Object = MibTableColumn
wwpLeosBenchmarkProfileFramelossStatsFirst = _WwpLeosBenchmarkProfileFramelossStatsFirst_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 3, 1, 6),
    _WwpLeosBenchmarkProfileFramelossStatsFirst_Type()
)
wwpLeosBenchmarkProfileFramelossStatsFirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileFramelossStatsFirst.setStatus("current")
_WwpLeosBenchmarkProfileFramelossStatsSecond_Type = Unsigned32
_WwpLeosBenchmarkProfileFramelossStatsSecond_Object = MibTableColumn
wwpLeosBenchmarkProfileFramelossStatsSecond = _WwpLeosBenchmarkProfileFramelossStatsSecond_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 3, 1, 7),
    _WwpLeosBenchmarkProfileFramelossStatsSecond_Type()
)
wwpLeosBenchmarkProfileFramelossStatsSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileFramelossStatsSecond.setStatus("current")


class _WwpLeosBenchmarkProfileFramelossStatsActiveVid_Type(Integer32):
    """Custom type wwpLeosBenchmarkProfileFramelossStatsActiveVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_WwpLeosBenchmarkProfileFramelossStatsActiveVid_Type.__name__ = "Integer32"
_WwpLeosBenchmarkProfileFramelossStatsActiveVid_Object = MibTableColumn
wwpLeosBenchmarkProfileFramelossStatsActiveVid = _WwpLeosBenchmarkProfileFramelossStatsActiveVid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 3, 1, 8),
    _WwpLeosBenchmarkProfileFramelossStatsActiveVid_Type()
)
wwpLeosBenchmarkProfileFramelossStatsActiveVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileFramelossStatsActiveVid.setStatus("current")
_WwpLeosBenchmarkProfileFramelossStatsActiveDstMac_Type = MacAddress
_WwpLeosBenchmarkProfileFramelossStatsActiveDstMac_Object = MibTableColumn
wwpLeosBenchmarkProfileFramelossStatsActiveDstMac = _WwpLeosBenchmarkProfileFramelossStatsActiveDstMac_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 3, 1, 9),
    _WwpLeosBenchmarkProfileFramelossStatsActiveDstMac_Type()
)
wwpLeosBenchmarkProfileFramelossStatsActiveDstMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileFramelossStatsActiveDstMac.setStatus("current")
_WwpLeosBenchmarkProfileLatencyStatisticsTable_Object = MibTable
wwpLeosBenchmarkProfileLatencyStatisticsTable = _WwpLeosBenchmarkProfileLatencyStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 4)
)
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileLatencyStatisticsTable.setStatus("current")
_WwpLeosBenchmarkProfileLatencyStatsEntry_Object = MibTableRow
wwpLeosBenchmarkProfileLatencyStatsEntry = _WwpLeosBenchmarkProfileLatencyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 4, 1)
)
wwpLeosBenchmarkProfileLatencyStatsEntry.setIndexNames(
    (0, "WWP-LEOS-BENCHMARK-MIB", "wwpLeosBenchmarkProfileLatencyStatsProfileId"),
    (0, "WWP-LEOS-BENCHMARK-MIB", "wwpLeosBenchmarkProfileLatencyStatsFrameSizeIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileLatencyStatsEntry.setStatus("current")


class _WwpLeosBenchmarkProfileLatencyStatsProfileId_Type(Integer32):
    """Custom type wwpLeosBenchmarkProfileLatencyStatsProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_WwpLeosBenchmarkProfileLatencyStatsProfileId_Type.__name__ = "Integer32"
_WwpLeosBenchmarkProfileLatencyStatsProfileId_Object = MibTableColumn
wwpLeosBenchmarkProfileLatencyStatsProfileId = _WwpLeosBenchmarkProfileLatencyStatsProfileId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 4, 1, 1),
    _WwpLeosBenchmarkProfileLatencyStatsProfileId_Type()
)
wwpLeosBenchmarkProfileLatencyStatsProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileLatencyStatsProfileId.setStatus("current")


class _WwpLeosBenchmarkProfileLatencyStatsFrameSizeIndex_Type(Integer32):
    """Custom type wwpLeosBenchmarkProfileLatencyStatsFrameSizeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_WwpLeosBenchmarkProfileLatencyStatsFrameSizeIndex_Type.__name__ = "Integer32"
_WwpLeosBenchmarkProfileLatencyStatsFrameSizeIndex_Object = MibTableColumn
wwpLeosBenchmarkProfileLatencyStatsFrameSizeIndex = _WwpLeosBenchmarkProfileLatencyStatsFrameSizeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 4, 1, 2),
    _WwpLeosBenchmarkProfileLatencyStatsFrameSizeIndex_Type()
)
wwpLeosBenchmarkProfileLatencyStatsFrameSizeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileLatencyStatsFrameSizeIndex.setStatus("current")
_WwpLeosBenchmarkProfileLatencyStatsFrameSize_Type = Integer32
_WwpLeosBenchmarkProfileLatencyStatsFrameSize_Object = MibTableColumn
wwpLeosBenchmarkProfileLatencyStatsFrameSize = _WwpLeosBenchmarkProfileLatencyStatsFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 4, 1, 3),
    _WwpLeosBenchmarkProfileLatencyStatsFrameSize_Type()
)
wwpLeosBenchmarkProfileLatencyStatsFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileLatencyStatsFrameSize.setStatus("current")
_WwpLeosBenchmarkProfileLatencyStatsMin_Type = Unsigned32
_WwpLeosBenchmarkProfileLatencyStatsMin_Object = MibTableColumn
wwpLeosBenchmarkProfileLatencyStatsMin = _WwpLeosBenchmarkProfileLatencyStatsMin_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 4, 1, 4),
    _WwpLeosBenchmarkProfileLatencyStatsMin_Type()
)
wwpLeosBenchmarkProfileLatencyStatsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileLatencyStatsMin.setStatus("current")
_WwpLeosBenchmarkProfileLatencyStatsMax_Type = Unsigned32
_WwpLeosBenchmarkProfileLatencyStatsMax_Object = MibTableColumn
wwpLeosBenchmarkProfileLatencyStatsMax = _WwpLeosBenchmarkProfileLatencyStatsMax_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 4, 1, 5),
    _WwpLeosBenchmarkProfileLatencyStatsMax_Type()
)
wwpLeosBenchmarkProfileLatencyStatsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileLatencyStatsMax.setStatus("current")
_WwpLeosBenchmarkProfileLatencyStatsAvg_Type = Unsigned32
_WwpLeosBenchmarkProfileLatencyStatsAvg_Object = MibTableColumn
wwpLeosBenchmarkProfileLatencyStatsAvg = _WwpLeosBenchmarkProfileLatencyStatsAvg_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 4, 1, 6),
    _WwpLeosBenchmarkProfileLatencyStatsAvg_Type()
)
wwpLeosBenchmarkProfileLatencyStatsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileLatencyStatsAvg.setStatus("current")
_WwpLeosBenchmarkProfileLatencyStatsSamples_Type = Integer32
_WwpLeosBenchmarkProfileLatencyStatsSamples_Object = MibTableColumn
wwpLeosBenchmarkProfileLatencyStatsSamples = _WwpLeosBenchmarkProfileLatencyStatsSamples_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 4, 1, 7),
    _WwpLeosBenchmarkProfileLatencyStatsSamples_Type()
)
wwpLeosBenchmarkProfileLatencyStatsSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileLatencyStatsSamples.setStatus("current")


class _WwpLeosBenchmarkProfileLatencyStatsActiveVid_Type(Integer32):
    """Custom type wwpLeosBenchmarkProfileLatencyStatsActiveVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_WwpLeosBenchmarkProfileLatencyStatsActiveVid_Type.__name__ = "Integer32"
_WwpLeosBenchmarkProfileLatencyStatsActiveVid_Object = MibTableColumn
wwpLeosBenchmarkProfileLatencyStatsActiveVid = _WwpLeosBenchmarkProfileLatencyStatsActiveVid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 4, 1, 8),
    _WwpLeosBenchmarkProfileLatencyStatsActiveVid_Type()
)
wwpLeosBenchmarkProfileLatencyStatsActiveVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileLatencyStatsActiveVid.setStatus("current")
_WwpLeosBenchmarkProfileLatencyStatsActiveDstMac_Type = MacAddress
_WwpLeosBenchmarkProfileLatencyStatsActiveDstMac_Object = MibTableColumn
wwpLeosBenchmarkProfileLatencyStatsActiveDstMac = _WwpLeosBenchmarkProfileLatencyStatsActiveDstMac_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 4, 1, 9),
    _WwpLeosBenchmarkProfileLatencyStatsActiveDstMac_Type()
)
wwpLeosBenchmarkProfileLatencyStatsActiveDstMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileLatencyStatsActiveDstMac.setStatus("current")
_WwpLeosBenchmarkProfilePdvStatisticsTable_Object = MibTable
wwpLeosBenchmarkProfilePdvStatisticsTable = _WwpLeosBenchmarkProfilePdvStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 5)
)
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfilePdvStatisticsTable.setStatus("current")
_WwpLeosBenchmarkProfilePdvStatsEntry_Object = MibTableRow
wwpLeosBenchmarkProfilePdvStatsEntry = _WwpLeosBenchmarkProfilePdvStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 5, 1)
)
wwpLeosBenchmarkProfilePdvStatsEntry.setIndexNames(
    (0, "WWP-LEOS-BENCHMARK-MIB", "wwpLeosBenchmarkProfilePdvStatsProfileId"),
    (0, "WWP-LEOS-BENCHMARK-MIB", "wwpLeosBenchmarkProfilePdvStatsFrameSizeIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfilePdvStatsEntry.setStatus("current")


class _WwpLeosBenchmarkProfilePdvStatsProfileId_Type(Integer32):
    """Custom type wwpLeosBenchmarkProfilePdvStatsProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_WwpLeosBenchmarkProfilePdvStatsProfileId_Type.__name__ = "Integer32"
_WwpLeosBenchmarkProfilePdvStatsProfileId_Object = MibTableColumn
wwpLeosBenchmarkProfilePdvStatsProfileId = _WwpLeosBenchmarkProfilePdvStatsProfileId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 5, 1, 1),
    _WwpLeosBenchmarkProfilePdvStatsProfileId_Type()
)
wwpLeosBenchmarkProfilePdvStatsProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfilePdvStatsProfileId.setStatus("current")


class _WwpLeosBenchmarkProfilePdvStatsFrameSizeIndex_Type(Integer32):
    """Custom type wwpLeosBenchmarkProfilePdvStatsFrameSizeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_WwpLeosBenchmarkProfilePdvStatsFrameSizeIndex_Type.__name__ = "Integer32"
_WwpLeosBenchmarkProfilePdvStatsFrameSizeIndex_Object = MibTableColumn
wwpLeosBenchmarkProfilePdvStatsFrameSizeIndex = _WwpLeosBenchmarkProfilePdvStatsFrameSizeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 5, 1, 2),
    _WwpLeosBenchmarkProfilePdvStatsFrameSizeIndex_Type()
)
wwpLeosBenchmarkProfilePdvStatsFrameSizeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfilePdvStatsFrameSizeIndex.setStatus("current")
_WwpLeosBenchmarkProfilePdvStatsFrameSize_Type = Integer32
_WwpLeosBenchmarkProfilePdvStatsFrameSize_Object = MibTableColumn
wwpLeosBenchmarkProfilePdvStatsFrameSize = _WwpLeosBenchmarkProfilePdvStatsFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 5, 1, 3),
    _WwpLeosBenchmarkProfilePdvStatsFrameSize_Type()
)
wwpLeosBenchmarkProfilePdvStatsFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfilePdvStatsFrameSize.setStatus("current")
_WwpLeosBenchmarkProfilePdvStatsAvg_Type = Unsigned32
_WwpLeosBenchmarkProfilePdvStatsAvg_Object = MibTableColumn
wwpLeosBenchmarkProfilePdvStatsAvg = _WwpLeosBenchmarkProfilePdvStatsAvg_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 5, 1, 4),
    _WwpLeosBenchmarkProfilePdvStatsAvg_Type()
)
wwpLeosBenchmarkProfilePdvStatsAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfilePdvStatsAvg.setStatus("current")
_WwpLeosBenchmarkProfilePdvStatsSamples_Type = Integer32
_WwpLeosBenchmarkProfilePdvStatsSamples_Object = MibTableColumn
wwpLeosBenchmarkProfilePdvStatsSamples = _WwpLeosBenchmarkProfilePdvStatsSamples_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 5, 1, 5),
    _WwpLeosBenchmarkProfilePdvStatsSamples_Type()
)
wwpLeosBenchmarkProfilePdvStatsSamples.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfilePdvStatsSamples.setStatus("current")


class _WwpLeosBenchmarkProfilePdvStatsActiveVid_Type(Integer32):
    """Custom type wwpLeosBenchmarkProfilePdvStatsActiveVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_WwpLeosBenchmarkProfilePdvStatsActiveVid_Type.__name__ = "Integer32"
_WwpLeosBenchmarkProfilePdvStatsActiveVid_Object = MibTableColumn
wwpLeosBenchmarkProfilePdvStatsActiveVid = _WwpLeosBenchmarkProfilePdvStatsActiveVid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 5, 1, 6),
    _WwpLeosBenchmarkProfilePdvStatsActiveVid_Type()
)
wwpLeosBenchmarkProfilePdvStatsActiveVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfilePdvStatsActiveVid.setStatus("current")
_WwpLeosBenchmarkProfilePdvStatsActiveDstMac_Type = MacAddress
_WwpLeosBenchmarkProfilePdvStatsActiveDstMac_Object = MibTableColumn
wwpLeosBenchmarkProfilePdvStatsActiveDstMac = _WwpLeosBenchmarkProfilePdvStatsActiveDstMac_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 5, 1, 7),
    _WwpLeosBenchmarkProfilePdvStatsActiveDstMac_Type()
)
wwpLeosBenchmarkProfilePdvStatsActiveDstMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfilePdvStatsActiveDstMac.setStatus("current")
_WwpLeosBenchmarkProfileFrameSizeTable_Object = MibTable
wwpLeosBenchmarkProfileFrameSizeTable = _WwpLeosBenchmarkProfileFrameSizeTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 6)
)
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileFrameSizeTable.setStatus("current")
_WwpLeosBenchmarkProfileFrameSizeEntry_Object = MibTableRow
wwpLeosBenchmarkProfileFrameSizeEntry = _WwpLeosBenchmarkProfileFrameSizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 6, 1)
)
wwpLeosBenchmarkProfileFrameSizeEntry.setIndexNames(
    (0, "WWP-LEOS-BENCHMARK-MIB", "wwpLeosBenchmarkProfileFrameSizeProfileId"),
    (0, "WWP-LEOS-BENCHMARK-MIB", "wwpLeosBenchmarkProfileFrameSizeIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileFrameSizeEntry.setStatus("current")


class _WwpLeosBenchmarkProfileFrameSizeProfileId_Type(Integer32):
    """Custom type wwpLeosBenchmarkProfileFrameSizeProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_WwpLeosBenchmarkProfileFrameSizeProfileId_Type.__name__ = "Integer32"
_WwpLeosBenchmarkProfileFrameSizeProfileId_Object = MibTableColumn
wwpLeosBenchmarkProfileFrameSizeProfileId = _WwpLeosBenchmarkProfileFrameSizeProfileId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 6, 1, 1),
    _WwpLeosBenchmarkProfileFrameSizeProfileId_Type()
)
wwpLeosBenchmarkProfileFrameSizeProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileFrameSizeProfileId.setStatus("current")


class _WwpLeosBenchmarkProfileFrameSizeIndex_Type(Integer32):
    """Custom type wwpLeosBenchmarkProfileFrameSizeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_WwpLeosBenchmarkProfileFrameSizeIndex_Type.__name__ = "Integer32"
_WwpLeosBenchmarkProfileFrameSizeIndex_Object = MibTableColumn
wwpLeosBenchmarkProfileFrameSizeIndex = _WwpLeosBenchmarkProfileFrameSizeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 6, 1, 2),
    _WwpLeosBenchmarkProfileFrameSizeIndex_Type()
)
wwpLeosBenchmarkProfileFrameSizeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileFrameSizeIndex.setStatus("current")
_WwpLeosBenchmarkProfileFrameSize_Type = Integer32
_WwpLeosBenchmarkProfileFrameSize_Object = MibTableColumn
wwpLeosBenchmarkProfileFrameSize = _WwpLeosBenchmarkProfileFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 43, 1, 6, 6, 1, 3),
    _WwpLeosBenchmarkProfileFrameSize_Type()
)
wwpLeosBenchmarkProfileFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosBenchmarkProfileFrameSize.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-BENCHMARK-MIB",
    **{"BenchmarkLatencyPdvTestState": BenchmarkLatencyPdvTestState,
       "wwpLeosBenchmarkMIB": wwpLeosBenchmarkMIB,
       "wwpLeosBenchmarkMIBObjects": wwpLeosBenchmarkMIBObjects,
       "wwpLeosBenchmarkModule": wwpLeosBenchmarkModule,
       "wwpLeosBenchmarkRole": wwpLeosBenchmarkRole,
       "wwpLeosBenchmarkPort": wwpLeosBenchmarkPort,
       "wwpLeosBenchmarkMode": wwpLeosBenchmarkMode,
       "wwpLeosBenchmarkEnable": wwpLeosBenchmarkEnable,
       "wwpLeosBenchmarkOperEnable": wwpLeosBenchmarkOperEnable,
       "wwpLeosBenchmarkLocalFpgaMac": wwpLeosBenchmarkLocalFpgaMac,
       "wwpLeosBenchmarkReflectorModule": wwpLeosBenchmarkReflectorModule,
       "wwpLeosBenchmarkReflectorEnable": wwpLeosBenchmarkReflectorEnable,
       "wwpLeosBenchmarkReflectorVid": wwpLeosBenchmarkReflectorVid,
       "wwpLeosBenchmarkReflectorVendorType": wwpLeosBenchmarkReflectorVendorType,
       "wwpLeosBenchmarkGeneratorModule": wwpLeosBenchmarkGeneratorModule,
       "wwpLeosBenchmarkGeneratorEnable": wwpLeosBenchmarkGeneratorEnable,
       "wwpLeosBenchmarkGeneratorprofileUnderTest": wwpLeosBenchmarkGeneratorprofileUnderTest,
       "wwpLeosBenchmarkGeneratorThroughputTestState": wwpLeosBenchmarkGeneratorThroughputTestState,
       "wwpLeosBenchmarkGeneratorFramelossTestState": wwpLeosBenchmarkGeneratorFramelossTestState,
       "wwpLeosBenchmarkGeneratorLatencyTestState": wwpLeosBenchmarkGeneratorLatencyTestState,
       "wwpLeosBenchmarkGeneratorPdvTestState": wwpLeosBenchmarkGeneratorPdvTestState,
       "wwpLeosBenchmarkGeneratorRfc2544State": wwpLeosBenchmarkGeneratorRfc2544State,
       "wwpLeosBenchmarkGeneratorCurrentPktSize": wwpLeosBenchmarkGeneratorCurrentPktSize,
       "wwpLeosBenchmarkGeneratorCurrentRate": wwpLeosBenchmarkGeneratorCurrentRate,
       "wwpLeosBenchmarkGeneratorSamplesCompleted": wwpLeosBenchmarkGeneratorSamplesCompleted,
       "wwpLeosBenchmarkGeneratorCurrentIteration": wwpLeosBenchmarkGeneratorCurrentIteration,
       "wwpLeosBenchmarkGeneratorTotalIterations": wwpLeosBenchmarkGeneratorTotalIterations,
       "wwpLeosBenchmarkFpgaStats": wwpLeosBenchmarkFpgaStats,
       "wwpLeosBenchmarkFpgaStatsRxPkts": wwpLeosBenchmarkFpgaStatsRxPkts,
       "wwpLeosBenchmarkFpgaStatsCrcPkts": wwpLeosBenchmarkFpgaStatsCrcPkts,
       "wwpLeosBenchmarkFpgaStatsUdpChecksumPkts": wwpLeosBenchmarkFpgaStatsUdpChecksumPkts,
       "wwpLeosBenchmarkFpgaStatsDiscardPkts": wwpLeosBenchmarkFpgaStatsDiscardPkts,
       "wwpLeosBenchmarkFpgaStatsDuplicatePkts": wwpLeosBenchmarkFpgaStatsDuplicatePkts,
       "wwpLeosBenchmarkFpgaStatsOOSeqPkts": wwpLeosBenchmarkFpgaStatsOOSeqPkts,
       "wwpLeosBenchmarkFpgaStatsTxPkts": wwpLeosBenchmarkFpgaStatsTxPkts,
       "wwpLeosBenchmarkFpgaStatsOOOPkts": wwpLeosBenchmarkFpgaStatsOOOPkts,
       "wwpLeosBenchmarkFpgaStatsDiscSeqNumPkts": wwpLeosBenchmarkFpgaStatsDiscSeqNumPkts,
       "wwpLeosBenchmarkPortStats": wwpLeosBenchmarkPortStats,
       "wwpLeosBenchmarkPortStatsTxBytes": wwpLeosBenchmarkPortStatsTxBytes,
       "wwpLeosBenchmarkPortStatsTxPkts": wwpLeosBenchmarkPortStatsTxPkts,
       "wwpLeosBenchmarkPortStatsCrcErrorPkts": wwpLeosBenchmarkPortStatsCrcErrorPkts,
       "wwpLeosBenchmarkPortStatsUcastPkts": wwpLeosBenchmarkPortStatsUcastPkts,
       "wwpLeosBenchmarkPortStatsMcastPkts": wwpLeosBenchmarkPortStatsMcastPkts,
       "wwpLeosBenchmarkPortStatsBcastPkts": wwpLeosBenchmarkPortStatsBcastPkts,
       "wwpLeosBenchmarkPortStatsUndersizePkts": wwpLeosBenchmarkPortStatsUndersizePkts,
       "wwpLeosBenchmarkPortStatsOversizePkts": wwpLeosBenchmarkPortStatsOversizePkts,
       "wwpLeosBenchmarkPortStatsFragmentsPkts": wwpLeosBenchmarkPortStatsFragmentsPkts,
       "wwpLeosBenchmarkPortStatsJabbersPkts": wwpLeosBenchmarkPortStatsJabbersPkts,
       "wwpLeosBenchmarkPortStatsTxPausePkts": wwpLeosBenchmarkPortStatsTxPausePkts,
       "wwpLeosBenchmarkPortStatsTxDropPkts": wwpLeosBenchmarkPortStatsTxDropPkts,
       "wwpLeosBenchmarkPortStatsTxDiscardPkts": wwpLeosBenchmarkPortStatsTxDiscardPkts,
       "wwpLeosBenchmarkPortStatsTxLOutRangePkts": wwpLeosBenchmarkPortStatsTxLOutRangePkts,
       "wwpLeosBenchmarkPortStatsTx64OctsPkts": wwpLeosBenchmarkPortStatsTx64OctsPkts,
       "wwpLeosBenchmarkPortStatsTx65To127Pkts": wwpLeosBenchmarkPortStatsTx65To127Pkts,
       "wwpLeosBenchmarkPortStatsTx128To255Pkts": wwpLeosBenchmarkPortStatsTx128To255Pkts,
       "wwpLeosBenchmarkPortStatsTx256To511Pkts": wwpLeosBenchmarkPortStatsTx256To511Pkts,
       "wwpLeosBenchmarkPortStatsTx512To1023Pkts": wwpLeosBenchmarkPortStatsTx512To1023Pkts,
       "wwpLeosBenchmarkPortStatsTx1024To1518Pkts": wwpLeosBenchmarkPortStatsTx1024To1518Pkts,
       "wwpLeosBenchmarkPortStatsTx1519To2047Pkts": wwpLeosBenchmarkPortStatsTx1519To2047Pkts,
       "wwpLeosBenchmarkPortStatsTx2048To4095Pkts": wwpLeosBenchmarkPortStatsTx2048To4095Pkts,
       "wwpLeosBenchmarkPortStatsTx4096To9216Pkts": wwpLeosBenchmarkPortStatsTx4096To9216Pkts,
       "wwpLeosBenchmarkPortStatsRxBytes": wwpLeosBenchmarkPortStatsRxBytes,
       "wwpLeosBenchmarkPortStatsRxPkts": wwpLeosBenchmarkPortStatsRxPkts,
       "wwpLeosBenchmarkPortStatsRxExDeferPkts": wwpLeosBenchmarkPortStatsRxExDeferPkts,
       "wwpLeosBenchmarkPortStatsRxDeferPkts": wwpLeosBenchmarkPortStatsRxDeferPkts,
       "wwpLeosBenchmarkPortStatsRxGiantPkts": wwpLeosBenchmarkPortStatsRxGiantPkts,
       "wwpLeosBenchmarkPortStatsRxUnderRunPkts": wwpLeosBenchmarkPortStatsRxUnderRunPkts,
       "wwpLeosBenchmarkPortStatsRxCrcErrorPkts": wwpLeosBenchmarkPortStatsRxCrcErrorPkts,
       "wwpLeosBenchmarkPortStatsRxLCheckErrorPkts": wwpLeosBenchmarkPortStatsRxLCheckErrorPkts,
       "wwpLeosBenchmarkPortStatsRxLOutRangePkts": wwpLeosBenchmarkPortStatsRxLOutRangePkts,
       "wwpLeosBenchmarkPortStatsRxPausePkts": wwpLeosBenchmarkPortStatsRxPausePkts,
       "wwpLeosBenchmarkPortStatsRxUcastPkts": wwpLeosBenchmarkPortStatsRxUcastPkts,
       "wwpLeosBenchmarkPortStatsRxMcastPkts": wwpLeosBenchmarkPortStatsRxMcastPkts,
       "wwpLeosBenchmarkPortStatsRxBcastPkts": wwpLeosBenchmarkPortStatsRxBcastPkts,
       "wwpLeosBenchmarkPortStatsRx64Pkts": wwpLeosBenchmarkPortStatsRx64Pkts,
       "wwpLeosBenchmarkPortStatsRx65To127Pkts": wwpLeosBenchmarkPortStatsRx65To127Pkts,
       "wwpLeosBenchmarkPortStatsRx128To255Pkts": wwpLeosBenchmarkPortStatsRx128To255Pkts,
       "wwpLeosBenchmarkPortStatsRx256To511Pkts": wwpLeosBenchmarkPortStatsRx256To511Pkts,
       "wwpLeosBenchmarkPortStatsRx512To1023Pkts": wwpLeosBenchmarkPortStatsRx512To1023Pkts,
       "wwpLeosBenchmarkPortStatsRx1024To1518Pkts": wwpLeosBenchmarkPortStatsRx1024To1518Pkts,
       "wwpLeosBenchmarkPortStatsRx1519To2047Pkts": wwpLeosBenchmarkPortStatsRx1519To2047Pkts,
       "wwpLeosBenchmarkPortStatsRx2048To4095Pkts": wwpLeosBenchmarkPortStatsRx2048To4095Pkts,
       "wwpLeosBenchmarkPortStatsRx4096To9216Pkts": wwpLeosBenchmarkPortStatsRx4096To9216Pkts,
       "wwpLeosBenchmarkProfileObjects": wwpLeosBenchmarkProfileObjects,
       "wwpLeosBenchmarkProfileTable": wwpLeosBenchmarkProfileTable,
       "wwpLeosBenchmarkProfileEntry": wwpLeosBenchmarkProfileEntry,
       "wwpLeosBenchmarkProfileEntryId": wwpLeosBenchmarkProfileEntryId,
       "wwpLeosBenchmarkProfileEntryName": wwpLeosBenchmarkProfileEntryName,
       "wwpLeosBenchmarkProfileEntryEnabled": wwpLeosBenchmarkProfileEntryEnabled,
       "wwpLeosBenchmarkProfileEntryStarted": wwpLeosBenchmarkProfileEntryStarted,
       "wwpLeosBenchmarkProfileEntryInterval": wwpLeosBenchmarkProfileEntryInterval,
       "wwpLeosBenchmarkProfileEntryDuration": wwpLeosBenchmarkProfileEntryDuration,
       "wwpLeosBenchmarkProfileEntryThroughputTest": wwpLeosBenchmarkProfileEntryThroughputTest,
       "wwpLeosBenchmarkProfileEntryFramelossTest": wwpLeosBenchmarkProfileEntryFramelossTest,
       "wwpLeosBenchmarkProfileEntryLatencyTest": wwpLeosBenchmarkProfileEntryLatencyTest,
       "wwpLeosBenchmarkProfileEntryPdvTest": wwpLeosBenchmarkProfileEntryPdvTest,
       "wwpLeosBenchmarkProfileEntryRfc2544Suite": wwpLeosBenchmarkProfileEntryRfc2544Suite,
       "wwpLeosBenchmarkProfileEntryDstmac": wwpLeosBenchmarkProfileEntryDstmac,
       "wwpLeosBenchmarkProfileEntryEncapType": wwpLeosBenchmarkProfileEntryEncapType,
       "wwpLeosBenchmarkProfileEntryVid": wwpLeosBenchmarkProfileEntryVid,
       "wwpLeosBenchmarkProfileEntryPcp": wwpLeosBenchmarkProfileEntryPcp,
       "wwpLeosBenchmarkProfileEntryCfi": wwpLeosBenchmarkProfileEntryCfi,
       "wwpLeosBenchmarkProfileEntryTpid": wwpLeosBenchmarkProfileEntryTpid,
       "wwpLeosBenchmarkProfileEntryPduType": wwpLeosBenchmarkProfileEntryPduType,
       "wwpLeosBenchmarkProfileEntrySrcIpAddr": wwpLeosBenchmarkProfileEntrySrcIpAddr,
       "wwpLeosBenchmarkProfileEntryDstIpAddr": wwpLeosBenchmarkProfileEntryDstIpAddr,
       "wwpLeosBenchmarkProfileEntryDscp": wwpLeosBenchmarkProfileEntryDscp,
       "wwpLeosBenchmarkProfileEntryCustomPayload": wwpLeosBenchmarkProfileEntryCustomPayload,
       "wwpLeosBenchmarkProfileEntryBandwidth": wwpLeosBenchmarkProfileEntryBandwidth,
       "wwpLeosBenchmarkProfileEntryVidValidation": wwpLeosBenchmarkProfileEntryVidValidation,
       "wwpLeosBenchmarkProfileEntryMaxSearches": wwpLeosBenchmarkProfileEntryMaxSearches,
       "wwpLeosBenchmarkProfileEntryMaxSamples": wwpLeosBenchmarkProfileEntryMaxSamples,
       "wwpLeosBenchmarkProfileEntrySamplingInterval": wwpLeosBenchmarkProfileEntrySamplingInterval,
       "wwpLeosBenchmarkProfileEntryFrameLossStartBw": wwpLeosBenchmarkProfileEntryFrameLossStartBw,
       "wwpLeosBenchmarkProfileThroughputStatisticsTable": wwpLeosBenchmarkProfileThroughputStatisticsTable,
       "wwpLeosBenchmarkProfileThroughputStatsEntry": wwpLeosBenchmarkProfileThroughputStatsEntry,
       "wwpLeosBenchmarkProfileThroughputStatsProfileId": wwpLeosBenchmarkProfileThroughputStatsProfileId,
       "wwpLeosBenchmarkProfileThroughputStatsFrameSizeIndex": wwpLeosBenchmarkProfileThroughputStatsFrameSizeIndex,
       "wwpLeosBenchmarkProfileThroughputStatsFrameSize": wwpLeosBenchmarkProfileThroughputStatsFrameSize,
       "wwpLeosBenchmarkProfileThroughputStatsMin": wwpLeosBenchmarkProfileThroughputStatsMin,
       "wwpLeosBenchmarkProfileThroughputStatsMax": wwpLeosBenchmarkProfileThroughputStatsMax,
       "wwpLeosBenchmarkProfileThroughputStatsAvg": wwpLeosBenchmarkProfileThroughputStatsAvg,
       "wwpLeosBenchmarkProfileThroughputStatsIterations": wwpLeosBenchmarkProfileThroughputStatsIterations,
       "wwpLeosBenchmarkProfileThroughputStatsActiveVid": wwpLeosBenchmarkProfileThroughputStatsActiveVid,
       "wwpLeosBenchmarkProfileThroughputStatsActiveDstMac": wwpLeosBenchmarkProfileThroughputStatsActiveDstMac,
       "wwpLeosBenchmarkProfileFramelossStatisticsTable": wwpLeosBenchmarkProfileFramelossStatisticsTable,
       "wwpLeosBenchmarkProfileFramelossStatsEntry": wwpLeosBenchmarkProfileFramelossStatsEntry,
       "wwpLeosBenchmarkProfileFramelossStatsProfileId": wwpLeosBenchmarkProfileFramelossStatsProfileId,
       "wwpLeosBenchmarkProfileFramelossStatsFrameSizeIndex": wwpLeosBenchmarkProfileFramelossStatsFrameSizeIndex,
       "wwpLeosBenchmarkProfileFramelossStatsRateIndex": wwpLeosBenchmarkProfileFramelossStatsRateIndex,
       "wwpLeosBenchmarkProfileFramelossStatsFrameSize": wwpLeosBenchmarkProfileFramelossStatsFrameSize,
       "wwpLeosBenchmarkProfileFramelossStatsRate": wwpLeosBenchmarkProfileFramelossStatsRate,
       "wwpLeosBenchmarkProfileFramelossStatsFirst": wwpLeosBenchmarkProfileFramelossStatsFirst,
       "wwpLeosBenchmarkProfileFramelossStatsSecond": wwpLeosBenchmarkProfileFramelossStatsSecond,
       "wwpLeosBenchmarkProfileFramelossStatsActiveVid": wwpLeosBenchmarkProfileFramelossStatsActiveVid,
       "wwpLeosBenchmarkProfileFramelossStatsActiveDstMac": wwpLeosBenchmarkProfileFramelossStatsActiveDstMac,
       "wwpLeosBenchmarkProfileLatencyStatisticsTable": wwpLeosBenchmarkProfileLatencyStatisticsTable,
       "wwpLeosBenchmarkProfileLatencyStatsEntry": wwpLeosBenchmarkProfileLatencyStatsEntry,
       "wwpLeosBenchmarkProfileLatencyStatsProfileId": wwpLeosBenchmarkProfileLatencyStatsProfileId,
       "wwpLeosBenchmarkProfileLatencyStatsFrameSizeIndex": wwpLeosBenchmarkProfileLatencyStatsFrameSizeIndex,
       "wwpLeosBenchmarkProfileLatencyStatsFrameSize": wwpLeosBenchmarkProfileLatencyStatsFrameSize,
       "wwpLeosBenchmarkProfileLatencyStatsMin": wwpLeosBenchmarkProfileLatencyStatsMin,
       "wwpLeosBenchmarkProfileLatencyStatsMax": wwpLeosBenchmarkProfileLatencyStatsMax,
       "wwpLeosBenchmarkProfileLatencyStatsAvg": wwpLeosBenchmarkProfileLatencyStatsAvg,
       "wwpLeosBenchmarkProfileLatencyStatsSamples": wwpLeosBenchmarkProfileLatencyStatsSamples,
       "wwpLeosBenchmarkProfileLatencyStatsActiveVid": wwpLeosBenchmarkProfileLatencyStatsActiveVid,
       "wwpLeosBenchmarkProfileLatencyStatsActiveDstMac": wwpLeosBenchmarkProfileLatencyStatsActiveDstMac,
       "wwpLeosBenchmarkProfilePdvStatisticsTable": wwpLeosBenchmarkProfilePdvStatisticsTable,
       "wwpLeosBenchmarkProfilePdvStatsEntry": wwpLeosBenchmarkProfilePdvStatsEntry,
       "wwpLeosBenchmarkProfilePdvStatsProfileId": wwpLeosBenchmarkProfilePdvStatsProfileId,
       "wwpLeosBenchmarkProfilePdvStatsFrameSizeIndex": wwpLeosBenchmarkProfilePdvStatsFrameSizeIndex,
       "wwpLeosBenchmarkProfilePdvStatsFrameSize": wwpLeosBenchmarkProfilePdvStatsFrameSize,
       "wwpLeosBenchmarkProfilePdvStatsAvg": wwpLeosBenchmarkProfilePdvStatsAvg,
       "wwpLeosBenchmarkProfilePdvStatsSamples": wwpLeosBenchmarkProfilePdvStatsSamples,
       "wwpLeosBenchmarkProfilePdvStatsActiveVid": wwpLeosBenchmarkProfilePdvStatsActiveVid,
       "wwpLeosBenchmarkProfilePdvStatsActiveDstMac": wwpLeosBenchmarkProfilePdvStatsActiveDstMac,
       "wwpLeosBenchmarkProfileFrameSizeTable": wwpLeosBenchmarkProfileFrameSizeTable,
       "wwpLeosBenchmarkProfileFrameSizeEntry": wwpLeosBenchmarkProfileFrameSizeEntry,
       "wwpLeosBenchmarkProfileFrameSizeProfileId": wwpLeosBenchmarkProfileFrameSizeProfileId,
       "wwpLeosBenchmarkProfileFrameSizeIndex": wwpLeosBenchmarkProfileFrameSizeIndex,
       "wwpLeosBenchmarkProfileFrameSize": wwpLeosBenchmarkProfileFrameSize}
)
