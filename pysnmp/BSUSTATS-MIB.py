# SNMP MIB module (BSUSTATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BSUSTATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:45 2024
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

(bsu,) = mibBuilder.importSymbols(
    "ANIROOT-MIB",
    "bsu")

(aniBsuWirelessPort,) = mibBuilder.importSymbols(
    "BSUWIRELESSIF-MIB",
    "aniBsuWirelessPort")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

aniBsuStatistics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AniBsuStatsGrp_ObjectIdentity = ObjectIdentity
aniBsuStatsGrp = _AniBsuStatsGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 1)
)
_AniBsuRfStatsTable_Object = MibTable
aniBsuRfStatsTable = _AniBsuRfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 2)
)
if mibBuilder.loadTexts:
    aniBsuRfStatsTable.setStatus("current")
_AniBsuRfStatsEntry_Object = MibTableRow
aniBsuRfStatsEntry = _AniBsuRfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 2, 1)
)
aniBsuRfStatsEntry.setIndexNames(
    (0, "BSUWIRELESSIF-MIB", "aniBsuWirelessPort"),
)
if mibBuilder.loadTexts:
    aniBsuRfStatsEntry.setStatus("current")
_AniBsuRfStatsInPackets_Type = Counter32
_AniBsuRfStatsInPackets_Object = MibTableColumn
aniBsuRfStatsInPackets = _AniBsuRfStatsInPackets_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 2, 1, 1),
    _AniBsuRfStatsInPackets_Type()
)
aniBsuRfStatsInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuRfStatsInPackets.setStatus("current")
_AniBsuRfStatsOutPackets_Type = Counter32
_AniBsuRfStatsOutPackets_Object = MibTableColumn
aniBsuRfStatsOutPackets = _AniBsuRfStatsOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 2, 1, 2),
    _AniBsuRfStatsOutPackets_Type()
)
aniBsuRfStatsOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuRfStatsOutPackets.setStatus("current")
_AniBsuRfStatsInOctets_Type = Counter32
_AniBsuRfStatsInOctets_Object = MibTableColumn
aniBsuRfStatsInOctets = _AniBsuRfStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 2, 1, 3),
    _AniBsuRfStatsInOctets_Type()
)
aniBsuRfStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuRfStatsInOctets.setStatus("current")
_AniBsuRfStatsOutOctets_Type = Counter32
_AniBsuRfStatsOutOctets_Object = MibTableColumn
aniBsuRfStatsOutOctets = _AniBsuRfStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 2, 1, 4),
    _AniBsuRfStatsOutOctets_Type()
)
aniBsuRfStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuRfStatsOutOctets.setStatus("current")


class _AniBsuRfStatsNumSusLinked_Type(Integer32):
    """Custom type aniBsuRfStatsNumSusLinked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_AniBsuRfStatsNumSusLinked_Type.__name__ = "Integer32"
_AniBsuRfStatsNumSusLinked_Object = MibTableColumn
aniBsuRfStatsNumSusLinked = _AniBsuRfStatsNumSusLinked_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 2, 1, 5),
    _AniBsuRfStatsNumSusLinked_Type()
)
aniBsuRfStatsNumSusLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuRfStatsNumSusLinked.setStatus("current")
_AniBsuStatsBWGroup_ObjectIdentity = ObjectIdentity
aniBsuStatsBWGroup = _AniBsuStatsBWGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 3)
)
_AniBsuStatsBWTable_Object = MibTable
aniBsuStatsBWTable = _AniBsuStatsBWTable_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    aniBsuStatsBWTable.setStatus("current")
_AniBsuStatsBWEntry_Object = MibTableRow
aniBsuStatsBWEntry = _AniBsuStatsBWEntry_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 3, 1, 1)
)
aniBsuStatsBWEntry.setIndexNames(
    (0, "BSUWIRELESSIF-MIB", "aniBsuWirelessPort"),
    (0, "BSUSTATS-MIB", "aniBsuStatsBWServiceClass"),
)
if mibBuilder.loadTexts:
    aniBsuStatsBWEntry.setStatus("current")


class _AniBsuStatsBWServiceClass_Type(Integer32):
    """Custom type aniBsuStatsBWServiceClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("besteffort", 1),
          ("cbr", 3),
          ("cir", 2))
    )


_AniBsuStatsBWServiceClass_Type.__name__ = "Integer32"
_AniBsuStatsBWServiceClass_Object = MibTableColumn
aniBsuStatsBWServiceClass = _AniBsuStatsBWServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 3, 1, 1, 1),
    _AniBsuStatsBWServiceClass_Type()
)
aniBsuStatsBWServiceClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatsBWServiceClass.setStatus("current")
_AniBsuStatsBWUSMaxAllocation_Type = Counter32
_AniBsuStatsBWUSMaxAllocation_Object = MibTableColumn
aniBsuStatsBWUSMaxAllocation = _AniBsuStatsBWUSMaxAllocation_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 3, 1, 1, 2),
    _AniBsuStatsBWUSMaxAllocation_Type()
)
aniBsuStatsBWUSMaxAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatsBWUSMaxAllocation.setStatus("current")
_AniBsuStatsBWUSMaxAllocPercent_Type = Integer32
_AniBsuStatsBWUSMaxAllocPercent_Object = MibTableColumn
aniBsuStatsBWUSMaxAllocPercent = _AniBsuStatsBWUSMaxAllocPercent_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 3, 1, 1, 3),
    _AniBsuStatsBWUSMaxAllocPercent_Type()
)
aniBsuStatsBWUSMaxAllocPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatsBWUSMaxAllocPercent.setStatus("current")
_AniBsuStatsBWUSCurrAllocation_Type = Counter32
_AniBsuStatsBWUSCurrAllocation_Object = MibTableColumn
aniBsuStatsBWUSCurrAllocation = _AniBsuStatsBWUSCurrAllocation_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 3, 1, 1, 4),
    _AniBsuStatsBWUSCurrAllocation_Type()
)
aniBsuStatsBWUSCurrAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatsBWUSCurrAllocation.setStatus("current")
_AniBsuStatsBWUSSubscrPercent_Type = DisplayString
_AniBsuStatsBWUSSubscrPercent_Object = MibTableColumn
aniBsuStatsBWUSSubscrPercent = _AniBsuStatsBWUSSubscrPercent_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 3, 1, 1, 5),
    _AniBsuStatsBWUSSubscrPercent_Type()
)
aniBsuStatsBWUSSubscrPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatsBWUSSubscrPercent.setStatus("current")
_AniBsuStatsBWDSMaxAllocation_Type = Counter32
_AniBsuStatsBWDSMaxAllocation_Object = MibTableColumn
aniBsuStatsBWDSMaxAllocation = _AniBsuStatsBWDSMaxAllocation_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 3, 1, 1, 6),
    _AniBsuStatsBWDSMaxAllocation_Type()
)
aniBsuStatsBWDSMaxAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatsBWDSMaxAllocation.setStatus("current")
_AniBsuStatsBWDSMaxAllocPercent_Type = Integer32
_AniBsuStatsBWDSMaxAllocPercent_Object = MibTableColumn
aniBsuStatsBWDSMaxAllocPercent = _AniBsuStatsBWDSMaxAllocPercent_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 3, 1, 1, 7),
    _AniBsuStatsBWDSMaxAllocPercent_Type()
)
aniBsuStatsBWDSMaxAllocPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatsBWDSMaxAllocPercent.setStatus("current")
_AniBsuStatsBWDSCurrAllocation_Type = Counter32
_AniBsuStatsBWDSCurrAllocation_Object = MibTableColumn
aniBsuStatsBWDSCurrAllocation = _AniBsuStatsBWDSCurrAllocation_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 3, 1, 1, 8),
    _AniBsuStatsBWDSCurrAllocation_Type()
)
aniBsuStatsBWDSCurrAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatsBWDSCurrAllocation.setStatus("current")
_AniBsuStatsBWDSSubscrPercent_Type = DisplayString
_AniBsuStatsBWDSSubscrPercent_Object = MibTableColumn
aniBsuStatsBWDSSubscrPercent = _AniBsuStatsBWDSSubscrPercent_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 3, 1, 1, 9),
    _AniBsuStatsBWDSSubscrPercent_Type()
)
aniBsuStatsBWDSSubscrPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatsBWDSSubscrPercent.setStatus("current")
_AniBsuStatsBWTotalTable_Object = MibTable
aniBsuStatsBWTotalTable = _AniBsuStatsBWTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 3, 2)
)
if mibBuilder.loadTexts:
    aniBsuStatsBWTotalTable.setStatus("current")
_AniBsuStatsBWTotalEntry_Object = MibTableRow
aniBsuStatsBWTotalEntry = _AniBsuStatsBWTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 3, 2, 1)
)
aniBsuStatsBWTotalEntry.setIndexNames(
    (0, "BSUWIRELESSIF-MIB", "aniBsuWirelessPort"),
)
if mibBuilder.loadTexts:
    aniBsuStatsBWTotalEntry.setStatus("current")
_AniBsuStatsBWTotalUSMaxAllocation_Type = Counter32
_AniBsuStatsBWTotalUSMaxAllocation_Object = MibTableColumn
aniBsuStatsBWTotalUSMaxAllocation = _AniBsuStatsBWTotalUSMaxAllocation_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 3, 2, 1, 1),
    _AniBsuStatsBWTotalUSMaxAllocation_Type()
)
aniBsuStatsBWTotalUSMaxAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatsBWTotalUSMaxAllocation.setStatus("current")
_AniBsuStatsBWTotalDSMaxAllocation_Type = Counter32
_AniBsuStatsBWTotalDSMaxAllocation_Object = MibTableColumn
aniBsuStatsBWTotalDSMaxAllocation = _AniBsuStatsBWTotalDSMaxAllocation_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 3, 2, 1, 2),
    _AniBsuStatsBWTotalDSMaxAllocation_Type()
)
aniBsuStatsBWTotalDSMaxAllocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatsBWTotalDSMaxAllocation.setStatus("current")
_AniBsuRfSigQStatsTable_Object = MibTable
aniBsuRfSigQStatsTable = _AniBsuRfSigQStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 4)
)
if mibBuilder.loadTexts:
    aniBsuRfSigQStatsTable.setStatus("current")
_AniBsuRfSigQStatsEntry_Object = MibTableRow
aniBsuRfSigQStatsEntry = _AniBsuRfSigQStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 4, 1)
)
aniBsuRfSigQStatsEntry.setIndexNames(
    (0, "BSUWIRELESSIF-MIB", "aniBsuWirelessPort"),
)
if mibBuilder.loadTexts:
    aniBsuRfSigQStatsEntry.setStatus("current")
_AniBsuRfSigQStatsNoFecErrorCount_Type = Counter32
_AniBsuRfSigQStatsNoFecErrorCount_Object = MibTableColumn
aniBsuRfSigQStatsNoFecErrorCount = _AniBsuRfSigQStatsNoFecErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 4, 1, 1),
    _AniBsuRfSigQStatsNoFecErrorCount_Type()
)
aniBsuRfSigQStatsNoFecErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuRfSigQStatsNoFecErrorCount.setStatus("current")
_AniBsuRfSigQStatsCorrFecErrorCount_Type = Counter32
_AniBsuRfSigQStatsCorrFecErrorCount_Object = MibTableColumn
aniBsuRfSigQStatsCorrFecErrorCount = _AniBsuRfSigQStatsCorrFecErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 4, 1, 2),
    _AniBsuRfSigQStatsCorrFecErrorCount_Type()
)
aniBsuRfSigQStatsCorrFecErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuRfSigQStatsCorrFecErrorCount.setStatus("current")
_AniBsuRfSigQStatsUncorrFecErrorCount_Type = Counter32
_AniBsuRfSigQStatsUncorrFecErrorCount_Object = MibTableColumn
aniBsuRfSigQStatsUncorrFecErrorCount = _AniBsuRfSigQStatsUncorrFecErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 4, 1, 3),
    _AniBsuRfSigQStatsUncorrFecErrorCount_Type()
)
aniBsuRfSigQStatsUncorrFecErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuRfSigQStatsUncorrFecErrorCount.setStatus("current")
_AniBsuRfSigQStatsNoUniqueWordCount_Type = Counter32
_AniBsuRfSigQStatsNoUniqueWordCount_Object = MibTableColumn
aniBsuRfSigQStatsNoUniqueWordCount = _AniBsuRfSigQStatsNoUniqueWordCount_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 4, 1, 4),
    _AniBsuRfSigQStatsNoUniqueWordCount_Type()
)
aniBsuRfSigQStatsNoUniqueWordCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuRfSigQStatsNoUniqueWordCount.setStatus("current")
_AniBsuRfSigQStatsCollidedBurstCount_Type = Counter32
_AniBsuRfSigQStatsCollidedBurstCount_Object = MibTableColumn
aniBsuRfSigQStatsCollidedBurstCount = _AniBsuRfSigQStatsCollidedBurstCount_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 4, 1, 5),
    _AniBsuRfSigQStatsCollidedBurstCount_Type()
)
aniBsuRfSigQStatsCollidedBurstCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuRfSigQStatsCollidedBurstCount.setStatus("current")
_AniBsuRfSigQStatsNoEnergyCount_Type = Counter32
_AniBsuRfSigQStatsNoEnergyCount_Object = MibTableColumn
aniBsuRfSigQStatsNoEnergyCount = _AniBsuRfSigQStatsNoEnergyCount_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 4, 1, 6),
    _AniBsuRfSigQStatsNoEnergyCount_Type()
)
aniBsuRfSigQStatsNoEnergyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuRfSigQStatsNoEnergyCount.setStatus("current")
_AniBsuRfSigQStatsPayloadLenErrorCount_Type = Counter32
_AniBsuRfSigQStatsPayloadLenErrorCount_Object = MibTableColumn
aniBsuRfSigQStatsPayloadLenErrorCount = _AniBsuRfSigQStatsPayloadLenErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 4, 1, 7),
    _AniBsuRfSigQStatsPayloadLenErrorCount_Type()
)
aniBsuRfSigQStatsPayloadLenErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuRfSigQStatsPayloadLenErrorCount.setStatus("current")
_AniBsuRfSigQStatsBurstErrorRate_Type = DisplayString
_AniBsuRfSigQStatsBurstErrorRate_Object = MibTableColumn
aniBsuRfSigQStatsBurstErrorRate = _AniBsuRfSigQStatsBurstErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 4, 1, 8),
    _AniBsuRfSigQStatsBurstErrorRate_Type()
)
aniBsuRfSigQStatsBurstErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuRfSigQStatsBurstErrorRate.setStatus("current")
_AniBsuRfSigQStatsResetCounter_Type = TruthValue
_AniBsuRfSigQStatsResetCounter_Object = MibTableColumn
aniBsuRfSigQStatsResetCounter = _AniBsuRfSigQStatsResetCounter_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 3, 4, 1, 9),
    _AniBsuRfSigQStatsResetCounter_Type()
)
aniBsuRfSigQStatsResetCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuRfSigQStatsResetCounter.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BSUSTATS-MIB",
    **{"aniBsuStatistics": aniBsuStatistics,
       "aniBsuStatsGrp": aniBsuStatsGrp,
       "aniBsuRfStatsTable": aniBsuRfStatsTable,
       "aniBsuRfStatsEntry": aniBsuRfStatsEntry,
       "aniBsuRfStatsInPackets": aniBsuRfStatsInPackets,
       "aniBsuRfStatsOutPackets": aniBsuRfStatsOutPackets,
       "aniBsuRfStatsInOctets": aniBsuRfStatsInOctets,
       "aniBsuRfStatsOutOctets": aniBsuRfStatsOutOctets,
       "aniBsuRfStatsNumSusLinked": aniBsuRfStatsNumSusLinked,
       "aniBsuStatsBWGroup": aniBsuStatsBWGroup,
       "aniBsuStatsBWTable": aniBsuStatsBWTable,
       "aniBsuStatsBWEntry": aniBsuStatsBWEntry,
       "aniBsuStatsBWServiceClass": aniBsuStatsBWServiceClass,
       "aniBsuStatsBWUSMaxAllocation": aniBsuStatsBWUSMaxAllocation,
       "aniBsuStatsBWUSMaxAllocPercent": aniBsuStatsBWUSMaxAllocPercent,
       "aniBsuStatsBWUSCurrAllocation": aniBsuStatsBWUSCurrAllocation,
       "aniBsuStatsBWUSSubscrPercent": aniBsuStatsBWUSSubscrPercent,
       "aniBsuStatsBWDSMaxAllocation": aniBsuStatsBWDSMaxAllocation,
       "aniBsuStatsBWDSMaxAllocPercent": aniBsuStatsBWDSMaxAllocPercent,
       "aniBsuStatsBWDSCurrAllocation": aniBsuStatsBWDSCurrAllocation,
       "aniBsuStatsBWDSSubscrPercent": aniBsuStatsBWDSSubscrPercent,
       "aniBsuStatsBWTotalTable": aniBsuStatsBWTotalTable,
       "aniBsuStatsBWTotalEntry": aniBsuStatsBWTotalEntry,
       "aniBsuStatsBWTotalUSMaxAllocation": aniBsuStatsBWTotalUSMaxAllocation,
       "aniBsuStatsBWTotalDSMaxAllocation": aniBsuStatsBWTotalDSMaxAllocation,
       "aniBsuRfSigQStatsTable": aniBsuRfSigQStatsTable,
       "aniBsuRfSigQStatsEntry": aniBsuRfSigQStatsEntry,
       "aniBsuRfSigQStatsNoFecErrorCount": aniBsuRfSigQStatsNoFecErrorCount,
       "aniBsuRfSigQStatsCorrFecErrorCount": aniBsuRfSigQStatsCorrFecErrorCount,
       "aniBsuRfSigQStatsUncorrFecErrorCount": aniBsuRfSigQStatsUncorrFecErrorCount,
       "aniBsuRfSigQStatsNoUniqueWordCount": aniBsuRfSigQStatsNoUniqueWordCount,
       "aniBsuRfSigQStatsCollidedBurstCount": aniBsuRfSigQStatsCollidedBurstCount,
       "aniBsuRfSigQStatsNoEnergyCount": aniBsuRfSigQStatsNoEnergyCount,
       "aniBsuRfSigQStatsPayloadLenErrorCount": aniBsuRfSigQStatsPayloadLenErrorCount,
       "aniBsuRfSigQStatsBurstErrorRate": aniBsuRfSigQStatsBurstErrorRate,
       "aniBsuRfSigQStatsResetCounter": aniBsuRfSigQStatsResetCounter}
)
