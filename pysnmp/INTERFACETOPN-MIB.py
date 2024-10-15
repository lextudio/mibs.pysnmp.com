# SNMP MIB module (INTERFACETOPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTERFACETOPN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:32 2024
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(OwnerString,
 rmon) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString",
    "rmon")

(probeConfig,
 rmonConformance) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "probeConfig",
    "rmonConformance")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

interfaceTopNMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 16, 27)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_InterfaceTopNObjects_ObjectIdentity = ObjectIdentity
interfaceTopNObjects = _InterfaceTopNObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 27, 1)
)


class _InterfaceTopNCaps_Type(Bits):
    """Custom type interfaceTopNCaps based on Bits"""
    namedValues = NamedValues(
        *(("dot1dTpPortInDiscards", 74),
          ("dot1dTpPortInFrames", 72),
          ("dot1dTpPortOutFrames", 73),
          ("dot3StatsAlignmentErrors", 24),
          ("dot3StatsCarrierSenseErrors", 33),
          ("dot3StatsDeferredTransmissions", 29),
          ("dot3StatsExcessiveCollisions", 31),
          ("dot3StatsFCSErrors", 25),
          ("dot3StatsFrameTooLongs", 34),
          ("dot3StatsInternalMacReceiveErrors", 35),
          ("dot3StatsInternalMacTransmitErrors", 32),
          ("dot3StatsLateCollisions", 30),
          ("dot3StatsMultipleCollisionFrames", 27),
          ("dot3StatsSQETestErrors", 28),
          ("dot3StatsSingleCollisionFrames", 26),
          ("dot3StatsSymbolErrors", 36),
          ("dot5StatsACErrors", 39),
          ("dot5StatsAbortTransErrors", 40),
          ("dot5StatsBurstErrors", 38),
          ("dot5StatsFrameCopiedErrors", 44),
          ("dot5StatsFreqErrors", 54),
          ("dot5StatsHardErrors", 47),
          ("dot5StatsInternalErrors", 41),
          ("dot5StatsLineErrors", 37),
          ("dot5StatsLobeWires", 51),
          ("dot5StatsLostFrameErrors", 42),
          ("dot5StatsReceiveCongestions", 43),
          ("dot5StatsRecoverys", 50),
          ("dot5StatsRemoves", 52),
          ("dot5StatsSignalLoss", 48),
          ("dot5StatsSingles", 53),
          ("dot5StatsSoftErrors", 46),
          ("dot5StatsTokenErrors", 45),
          ("dot5StatsTransmitBeacons", 49),
          ("etherStatsBroadcastPkts", 58),
          ("etherStatsCRCAlignErrors", 60),
          ("etherStatsCollisions", 65),
          ("etherStatsDropEvents", 55),
          ("etherStatsFragments", 63),
          ("etherStatsJabbers", 64),
          ("etherStatsMulticastPkts", 59),
          ("etherStatsOctets", 56),
          ("etherStatsOversizePkts", 62),
          ("etherStatsPkts", 57),
          ("etherStatsPkts1024to1518Octets", 71),
          ("etherStatsPkts128to255Octets", 68),
          ("etherStatsPkts256to511Octets", 69),
          ("etherStatsPkts512to1023Octets", 70),
          ("etherStatsPkts64Octets", 66),
          ("etherStatsPkts65to127Octets", 67),
          ("etherStatsUndersizePkts", 61),
          ("ifHCInBroadcastPkts", 19),
          ("ifHCInMulticastPkts", 18),
          ("ifHCInOctets", 16),
          ("ifHCInUcastPkts", 17),
          ("ifHCOutBroadcastPkts", 23),
          ("ifHCOutMulticastPkts", 22),
          ("ifHCOutOctets", 20),
          ("ifHCOutUcastPkts", 21),
          ("ifInBroadcastPkts", 13),
          ("ifInDiscards", 4),
          ("ifInErrors", 5),
          ("ifInMulticastPkts", 12),
          ("ifInNUcastPkts", 3),
          ("ifInOctets", 1),
          ("ifInUcastPkts", 2),
          ("ifInUnknownProtos", 6),
          ("ifOutBroadcastPkts", 15),
          ("ifOutDiscards", 10),
          ("ifOutErrors", 11),
          ("ifOutMulticastPkts", 14),
          ("ifOutNUcastPkts", 9),
          ("ifOutOctets", 7),
          ("ifOutUcastPkts", 8),
          ("usrTopN", 0))
    )

_InterfaceTopNCaps_Type.__name__ = "Bits"
_InterfaceTopNCaps_Object = MibScalar
interfaceTopNCaps = _InterfaceTopNCaps_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 1),
    _InterfaceTopNCaps_Type()
)
interfaceTopNCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTopNCaps.setStatus("current")
_InterfaceTopNControlTable_Object = MibTable
interfaceTopNControlTable = _InterfaceTopNControlTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 2)
)
if mibBuilder.loadTexts:
    interfaceTopNControlTable.setStatus("current")
_InterfaceTopNControlEntry_Object = MibTableRow
interfaceTopNControlEntry = _InterfaceTopNControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1)
)
interfaceTopNControlEntry.setIndexNames(
    (0, "INTERFACETOPN-MIB", "interfaceTopNControlIndex"),
)
if mibBuilder.loadTexts:
    interfaceTopNControlEntry.setStatus("current")


class _InterfaceTopNControlIndex_Type(Integer32):
    """Custom type interfaceTopNControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_InterfaceTopNControlIndex_Type.__name__ = "Integer32"
_InterfaceTopNControlIndex_Object = MibTableColumn
interfaceTopNControlIndex = _InterfaceTopNControlIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 1),
    _InterfaceTopNControlIndex_Type()
)
interfaceTopNControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceTopNControlIndex.setStatus("current")


class _InterfaceTopNObjectVariable_Type(Integer32):
    """Custom type interfaceTopNObjectVariable based on Integer32"""
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
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74)
        )
    )
    namedValues = NamedValues(
        *(("dot1dTpPortInDiscards", 74),
          ("dot1dTpPortInFrames", 72),
          ("dot1dTpPortOutFrames", 73),
          ("dot3StatsAlignmentErrors", 24),
          ("dot3StatsCarrierSenseErrors", 33),
          ("dot3StatsDeferredTransmissions", 29),
          ("dot3StatsExcessiveCollisions", 31),
          ("dot3StatsFCSErrors", 25),
          ("dot3StatsFrameTooLongs", 34),
          ("dot3StatsInternalMacReceiveErrors", 35),
          ("dot3StatsInternalMacTransmitErrors", 32),
          ("dot3StatsLateCollisions", 30),
          ("dot3StatsMultipleCollisionFrames", 27),
          ("dot3StatsSQETestErrors", 28),
          ("dot3StatsSingleCollisionFrames", 26),
          ("dot3StatsSymbolErrors", 36),
          ("dot5StatsACErrors", 39),
          ("dot5StatsAbortTransErrors", 40),
          ("dot5StatsBurstErrors", 38),
          ("dot5StatsFrameCopiedErrors", 44),
          ("dot5StatsFreqErrors", 54),
          ("dot5StatsHardErrors", 47),
          ("dot5StatsInternalErrors", 41),
          ("dot5StatsLineErrors", 37),
          ("dot5StatsLobeWires", 51),
          ("dot5StatsLostFrameErrors", 42),
          ("dot5StatsReceiveCongestions", 43),
          ("dot5StatsRecoverys", 50),
          ("dot5StatsRemoves", 52),
          ("dot5StatsSignalLoss", 48),
          ("dot5StatsSingles", 53),
          ("dot5StatsSoftErrors", 46),
          ("dot5StatsTokenErrors", 45),
          ("dot5StatsTransmitBeacons", 49),
          ("etherStatsBroadcastPkts", 58),
          ("etherStatsCRCAlignErrors", 60),
          ("etherStatsCollisions", 65),
          ("etherStatsDropEvents", 55),
          ("etherStatsFragments", 63),
          ("etherStatsJabbers", 64),
          ("etherStatsMulticastPkts", 59),
          ("etherStatsOctets", 56),
          ("etherStatsOversizePkts", 62),
          ("etherStatsPkts", 57),
          ("etherStatsPkts1024to1518Octets", 71),
          ("etherStatsPkts128to255Octets", 68),
          ("etherStatsPkts256to511Octets", 69),
          ("etherStatsPkts512to1023Octets", 70),
          ("etherStatsPkts64Octets", 66),
          ("etherStatsPkts65to127Octets", 67),
          ("etherStatsUndersizePkts", 61),
          ("ifHCInBroadcastPkts", 19),
          ("ifHCInMulticastPkts", 18),
          ("ifHCInOctets", 16),
          ("ifHCInUcastPkts", 17),
          ("ifHCOutBroadcastPkts", 23),
          ("ifHCOutMulticastPkts", 22),
          ("ifHCOutOctets", 20),
          ("ifHCOutUcastPkts", 21),
          ("ifInBroadcastPkts", 13),
          ("ifInDiscards", 4),
          ("ifInErrors", 5),
          ("ifInMulticastPkts", 12),
          ("ifInNUcastPkts", 3),
          ("ifInOctets", 1),
          ("ifInUcastPkts", 2),
          ("ifInUnknownProtos", 6),
          ("ifOutBroadcastPkts", 15),
          ("ifOutDiscards", 10),
          ("ifOutErrors", 11),
          ("ifOutMulticastPkts", 14),
          ("ifOutNUcastPkts", 9),
          ("ifOutOctets", 7),
          ("ifOutUcastPkts", 8))
    )


_InterfaceTopNObjectVariable_Type.__name__ = "Integer32"
_InterfaceTopNObjectVariable_Object = MibTableColumn
interfaceTopNObjectVariable = _InterfaceTopNObjectVariable_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 2),
    _InterfaceTopNObjectVariable_Type()
)
interfaceTopNObjectVariable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    interfaceTopNObjectVariable.setStatus("current")


class _InterfaceTopNObjectSampleType_Type(Integer32):
    """Custom type interfaceTopNObjectSampleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("bandwidthPercentage", 3),
          ("deltaValue", 2))
    )


_InterfaceTopNObjectSampleType_Type.__name__ = "Integer32"
_InterfaceTopNObjectSampleType_Object = MibTableColumn
interfaceTopNObjectSampleType = _InterfaceTopNObjectSampleType_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 3),
    _InterfaceTopNObjectSampleType_Type()
)
interfaceTopNObjectSampleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    interfaceTopNObjectSampleType.setStatus("current")


class _InterfaceTopNNormalization_Type(Integer32):
    """Custom type interfaceTopNNormalization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalizationNotRequired", 2),
          ("normalizationRequired", 1))
    )


_InterfaceTopNNormalization_Type.__name__ = "Integer32"
_InterfaceTopNNormalization_Object = MibTableColumn
interfaceTopNNormalization = _InterfaceTopNNormalization_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 4),
    _InterfaceTopNNormalization_Type()
)
interfaceTopNNormalization.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    interfaceTopNNormalization.setStatus("current")


class _InterfaceTopNNormalizationFactor_Type(Integer32):
    """Custom type interfaceTopNNormalizationFactor based on Integer32"""
    defaultValue = 1


_InterfaceTopNNormalizationFactor_Object = MibTableColumn
interfaceTopNNormalizationFactor = _InterfaceTopNNormalizationFactor_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 5),
    _InterfaceTopNNormalizationFactor_Type()
)
interfaceTopNNormalizationFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    interfaceTopNNormalizationFactor.setStatus("current")
_InterfaceTopNControlGeneratedReports_Type = Counter32
_InterfaceTopNControlGeneratedReports_Object = MibTableColumn
interfaceTopNControlGeneratedReports = _InterfaceTopNControlGeneratedReports_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 6),
    _InterfaceTopNControlGeneratedReports_Type()
)
interfaceTopNControlGeneratedReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTopNControlGeneratedReports.setStatus("current")


class _InterfaceTopNTimeRemaining_Type(Integer32):
    """Custom type interfaceTopNTimeRemaining based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_InterfaceTopNTimeRemaining_Type.__name__ = "Integer32"
_InterfaceTopNTimeRemaining_Object = MibTableColumn
interfaceTopNTimeRemaining = _InterfaceTopNTimeRemaining_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 7),
    _InterfaceTopNTimeRemaining_Type()
)
interfaceTopNTimeRemaining.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    interfaceTopNTimeRemaining.setStatus("current")


class _InterfaceTopNDuration_Type(Integer32):
    """Custom type interfaceTopNDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_InterfaceTopNDuration_Type.__name__ = "Integer32"
_InterfaceTopNDuration_Object = MibTableColumn
interfaceTopNDuration = _InterfaceTopNDuration_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 8),
    _InterfaceTopNDuration_Type()
)
interfaceTopNDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTopNDuration.setStatus("current")


class _InterfaceTopNRequestedSize_Type(Integer32):
    """Custom type interfaceTopNRequestedSize based on Integer32"""
    defaultValue = 10


_InterfaceTopNRequestedSize_Object = MibTableColumn
interfaceTopNRequestedSize = _InterfaceTopNRequestedSize_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 9),
    _InterfaceTopNRequestedSize_Type()
)
interfaceTopNRequestedSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    interfaceTopNRequestedSize.setStatus("current")


class _InterfaceTopNGrantedSize_Type(Integer32):
    """Custom type interfaceTopNGrantedSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_InterfaceTopNGrantedSize_Type.__name__ = "Integer32"
_InterfaceTopNGrantedSize_Object = MibTableColumn
interfaceTopNGrantedSize = _InterfaceTopNGrantedSize_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 10),
    _InterfaceTopNGrantedSize_Type()
)
interfaceTopNGrantedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTopNGrantedSize.setStatus("current")
_InterfaceTopNStartTime_Type = TimeStamp
_InterfaceTopNStartTime_Object = MibTableColumn
interfaceTopNStartTime = _InterfaceTopNStartTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 11),
    _InterfaceTopNStartTime_Type()
)
interfaceTopNStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTopNStartTime.setStatus("current")
_InterfaceTopNOwner_Type = OwnerString
_InterfaceTopNOwner_Object = MibTableColumn
interfaceTopNOwner = _InterfaceTopNOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 12),
    _InterfaceTopNOwner_Type()
)
interfaceTopNOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    interfaceTopNOwner.setStatus("current")
_InterfaceTopNRowStatus_Type = RowStatus
_InterfaceTopNRowStatus_Object = MibTableColumn
interfaceTopNRowStatus = _InterfaceTopNRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 2, 1, 13),
    _InterfaceTopNRowStatus_Type()
)
interfaceTopNRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    interfaceTopNRowStatus.setStatus("current")
_InterfaceTopNTable_Object = MibTable
interfaceTopNTable = _InterfaceTopNTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 3)
)
if mibBuilder.loadTexts:
    interfaceTopNTable.setStatus("current")
_InterfaceTopNEntry_Object = MibTableRow
interfaceTopNEntry = _InterfaceTopNEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 3, 1)
)
interfaceTopNEntry.setIndexNames(
    (0, "INTERFACETOPN-MIB", "interfaceTopNControlIndex"),
    (0, "INTERFACETOPN-MIB", "interfaceTopNIndex"),
)
if mibBuilder.loadTexts:
    interfaceTopNEntry.setStatus("current")


class _InterfaceTopNIndex_Type(Integer32):
    """Custom type interfaceTopNIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_InterfaceTopNIndex_Type.__name__ = "Integer32"
_InterfaceTopNIndex_Object = MibTableColumn
interfaceTopNIndex = _InterfaceTopNIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 3, 1, 1),
    _InterfaceTopNIndex_Type()
)
interfaceTopNIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceTopNIndex.setStatus("current")


class _InterfaceTopNDataSourceIndex_Type(Integer32):
    """Custom type interfaceTopNDataSourceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_InterfaceTopNDataSourceIndex_Type.__name__ = "Integer32"
_InterfaceTopNDataSourceIndex_Object = MibTableColumn
interfaceTopNDataSourceIndex = _InterfaceTopNDataSourceIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 3, 1, 2),
    _InterfaceTopNDataSourceIndex_Type()
)
interfaceTopNDataSourceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTopNDataSourceIndex.setStatus("current")
_InterfaceTopNValue_Type = Gauge32
_InterfaceTopNValue_Object = MibTableColumn
interfaceTopNValue = _InterfaceTopNValue_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 3, 1, 3),
    _InterfaceTopNValue_Type()
)
interfaceTopNValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTopNValue.setStatus("current")
_InterfaceTopNValue64_Type = CounterBasedGauge64
_InterfaceTopNValue64_Object = MibTableColumn
interfaceTopNValue64 = _InterfaceTopNValue64_Object(
    (1, 3, 6, 1, 2, 1, 16, 27, 1, 3, 1, 4),
    _InterfaceTopNValue64_Type()
)
interfaceTopNValue64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTopNValue64.setStatus("current")
_InterfaceTopNNotifications_ObjectIdentity = ObjectIdentity
interfaceTopNNotifications = _InterfaceTopNNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 27, 2)
)
_InterfaceTopNConformance_ObjectIdentity = ObjectIdentity
interfaceTopNConformance = _InterfaceTopNConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 27, 3)
)
_InterfaceTopNCompliances_ObjectIdentity = ObjectIdentity
interfaceTopNCompliances = _InterfaceTopNCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 27, 3, 1)
)
_InterfaceTopNGroups_ObjectIdentity = ObjectIdentity
interfaceTopNGroups = _InterfaceTopNGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 27, 3, 2)
)

# Managed Objects groups

interfaceTopNGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 27, 3, 2, 1)
)
interfaceTopNGroup.setObjects(
      *(("INTERFACETOPN-MIB", "interfaceTopNCaps"),
        ("INTERFACETOPN-MIB", "interfaceTopNControlIndex"),
        ("INTERFACETOPN-MIB", "interfaceTopNObjectVariable"),
        ("INTERFACETOPN-MIB", "interfaceTopNObjectSampleType"),
        ("INTERFACETOPN-MIB", "interfaceTopNNormalization"),
        ("INTERFACETOPN-MIB", "interfaceTopNNormalizationFactor"),
        ("INTERFACETOPN-MIB", "interfaceTopNControlGeneratedReports"),
        ("INTERFACETOPN-MIB", "interfaceTopNTimeRemaining"),
        ("INTERFACETOPN-MIB", "interfaceTopNDuration"),
        ("INTERFACETOPN-MIB", "interfaceTopNRequestedSize"),
        ("INTERFACETOPN-MIB", "interfaceTopNGrantedSize"),
        ("INTERFACETOPN-MIB", "interfaceTopNStartTime"),
        ("INTERFACETOPN-MIB", "interfaceTopNOwner"),
        ("INTERFACETOPN-MIB", "interfaceTopNRowStatus"),
        ("INTERFACETOPN-MIB", "interfaceTopNIndex"),
        ("INTERFACETOPN-MIB", "interfaceTopNDataSourceIndex"),
        ("INTERFACETOPN-MIB", "interfaceTopNValue"),
        ("INTERFACETOPN-MIB", "interfaceTopNValue64"))
)
if mibBuilder.loadTexts:
    interfaceTopNGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

interfaceTopNCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 16, 27, 3, 1, 1)
)
if mibBuilder.loadTexts:
    interfaceTopNCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTERFACETOPN-MIB",
    **{"interfaceTopNMIB": interfaceTopNMIB,
       "interfaceTopNObjects": interfaceTopNObjects,
       "interfaceTopNCaps": interfaceTopNCaps,
       "interfaceTopNControlTable": interfaceTopNControlTable,
       "interfaceTopNControlEntry": interfaceTopNControlEntry,
       "interfaceTopNControlIndex": interfaceTopNControlIndex,
       "interfaceTopNObjectVariable": interfaceTopNObjectVariable,
       "interfaceTopNObjectSampleType": interfaceTopNObjectSampleType,
       "interfaceTopNNormalization": interfaceTopNNormalization,
       "interfaceTopNNormalizationFactor": interfaceTopNNormalizationFactor,
       "interfaceTopNControlGeneratedReports": interfaceTopNControlGeneratedReports,
       "interfaceTopNTimeRemaining": interfaceTopNTimeRemaining,
       "interfaceTopNDuration": interfaceTopNDuration,
       "interfaceTopNRequestedSize": interfaceTopNRequestedSize,
       "interfaceTopNGrantedSize": interfaceTopNGrantedSize,
       "interfaceTopNStartTime": interfaceTopNStartTime,
       "interfaceTopNOwner": interfaceTopNOwner,
       "interfaceTopNRowStatus": interfaceTopNRowStatus,
       "interfaceTopNTable": interfaceTopNTable,
       "interfaceTopNEntry": interfaceTopNEntry,
       "interfaceTopNIndex": interfaceTopNIndex,
       "interfaceTopNDataSourceIndex": interfaceTopNDataSourceIndex,
       "interfaceTopNValue": interfaceTopNValue,
       "interfaceTopNValue64": interfaceTopNValue64,
       "interfaceTopNNotifications": interfaceTopNNotifications,
       "interfaceTopNConformance": interfaceTopNConformance,
       "interfaceTopNCompliances": interfaceTopNCompliances,
       "interfaceTopNCompliance": interfaceTopNCompliance,
       "interfaceTopNGroups": interfaceTopNGroups,
       "interfaceTopNGroup": interfaceTopNGroup}
)
