# SNMP MIB module (PSAMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PSAMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:55 2024
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

(Unsigned64TC,) = mibBuilder.importSymbols(
    "APPLICATION-MIB",
    "Unsigned64TC")

(Float64TC,) = mibBuilder.importSymbols(
    "FLOAT-TC-MIB",
    "Float64TC")

(ipfixSelectorFunctions,) = mibBuilder.importSymbols(
    "IPFIX-SELECTOR-MIB",
    "ipfixSelectorFunctions")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

psampMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 212)
)
psampMIB.setRevisions(
        ("2012-09-05 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PsampSampCountBased_ObjectIdentity = ObjectIdentity
psampSampCountBased = _PsampSampCountBased_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 2)
)
_PsampSampCountBasedAvail_Type = TruthValue
_PsampSampCountBasedAvail_Object = MibScalar
psampSampCountBasedAvail = _PsampSampCountBasedAvail_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 2, 1),
    _PsampSampCountBasedAvail_Type()
)
psampSampCountBasedAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psampSampCountBasedAvail.setStatus("current")
_PsampSampCountBasedParamSetTable_Object = MibTable
psampSampCountBasedParamSetTable = _PsampSampCountBasedParamSetTable_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    psampSampCountBasedParamSetTable.setStatus("current")
_PsampSampCountBasedParamSetEntry_Object = MibTableRow
psampSampCountBasedParamSetEntry = _PsampSampCountBasedParamSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 2, 2, 1)
)
psampSampCountBasedParamSetEntry.setIndexNames(
    (0, "PSAMP-MIB", "psampSampCountBasedIndex"),
)
if mibBuilder.loadTexts:
    psampSampCountBasedParamSetEntry.setStatus("current")


class _PsampSampCountBasedIndex_Type(Integer32):
    """Custom type psampSampCountBasedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PsampSampCountBasedIndex_Type.__name__ = "Integer32"
_PsampSampCountBasedIndex_Object = MibTableColumn
psampSampCountBasedIndex = _PsampSampCountBasedIndex_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 2, 2, 1, 1),
    _PsampSampCountBasedIndex_Type()
)
psampSampCountBasedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    psampSampCountBasedIndex.setStatus("current")
_PsampSampCountBasedInterval_Type = Unsigned32
_PsampSampCountBasedInterval_Object = MibTableColumn
psampSampCountBasedInterval = _PsampSampCountBasedInterval_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 2, 2, 1, 2),
    _PsampSampCountBasedInterval_Type()
)
psampSampCountBasedInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psampSampCountBasedInterval.setStatus("current")
if mibBuilder.loadTexts:
    psampSampCountBasedInterval.setUnits("packets")
_PsampSampCountBasedSpace_Type = Unsigned32
_PsampSampCountBasedSpace_Object = MibTableColumn
psampSampCountBasedSpace = _PsampSampCountBasedSpace_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 2, 2, 1, 3),
    _PsampSampCountBasedSpace_Type()
)
psampSampCountBasedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psampSampCountBasedSpace.setStatus("current")
if mibBuilder.loadTexts:
    psampSampCountBasedSpace.setUnits("packets")
_PsampSampTimeBased_ObjectIdentity = ObjectIdentity
psampSampTimeBased = _PsampSampTimeBased_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 3)
)
_PsampSampTimeBasedAvail_Type = TruthValue
_PsampSampTimeBasedAvail_Object = MibScalar
psampSampTimeBasedAvail = _PsampSampTimeBasedAvail_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 3, 1),
    _PsampSampTimeBasedAvail_Type()
)
psampSampTimeBasedAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psampSampTimeBasedAvail.setStatus("current")
_PsampSampTimeBasedParamSetTable_Object = MibTable
psampSampTimeBasedParamSetTable = _PsampSampTimeBasedParamSetTable_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    psampSampTimeBasedParamSetTable.setStatus("current")
_PsampSampTimeBasedParamSetEntry_Object = MibTableRow
psampSampTimeBasedParamSetEntry = _PsampSampTimeBasedParamSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 3, 2, 1)
)
psampSampTimeBasedParamSetEntry.setIndexNames(
    (0, "PSAMP-MIB", "psampSampTimeBasedIndex"),
)
if mibBuilder.loadTexts:
    psampSampTimeBasedParamSetEntry.setStatus("current")


class _PsampSampTimeBasedIndex_Type(Integer32):
    """Custom type psampSampTimeBasedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PsampSampTimeBasedIndex_Type.__name__ = "Integer32"
_PsampSampTimeBasedIndex_Object = MibTableColumn
psampSampTimeBasedIndex = _PsampSampTimeBasedIndex_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 3, 2, 1, 1),
    _PsampSampTimeBasedIndex_Type()
)
psampSampTimeBasedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    psampSampTimeBasedIndex.setStatus("current")
_PsampSampTimeBasedInterval_Type = Unsigned32
_PsampSampTimeBasedInterval_Object = MibTableColumn
psampSampTimeBasedInterval = _PsampSampTimeBasedInterval_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 3, 2, 1, 2),
    _PsampSampTimeBasedInterval_Type()
)
psampSampTimeBasedInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psampSampTimeBasedInterval.setStatus("current")
if mibBuilder.loadTexts:
    psampSampTimeBasedInterval.setUnits("microseconds")
_PsampSampTimeBasedSpace_Type = Unsigned32
_PsampSampTimeBasedSpace_Object = MibTableColumn
psampSampTimeBasedSpace = _PsampSampTimeBasedSpace_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 3, 2, 1, 3),
    _PsampSampTimeBasedSpace_Type()
)
psampSampTimeBasedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psampSampTimeBasedSpace.setStatus("current")
if mibBuilder.loadTexts:
    psampSampTimeBasedSpace.setUnits("microseconds")
_PsampSampRandOutOfN_ObjectIdentity = ObjectIdentity
psampSampRandOutOfN = _PsampSampRandOutOfN_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 4)
)
_PsampSampRandOutOfNAvail_Type = TruthValue
_PsampSampRandOutOfNAvail_Object = MibScalar
psampSampRandOutOfNAvail = _PsampSampRandOutOfNAvail_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 4, 1),
    _PsampSampRandOutOfNAvail_Type()
)
psampSampRandOutOfNAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psampSampRandOutOfNAvail.setStatus("current")
_PsampSampRandOutOfNParamSetTable_Object = MibTable
psampSampRandOutOfNParamSetTable = _PsampSampRandOutOfNParamSetTable_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    psampSampRandOutOfNParamSetTable.setStatus("current")
_PsampSampRandOutOfNParamSetEntry_Object = MibTableRow
psampSampRandOutOfNParamSetEntry = _PsampSampRandOutOfNParamSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 4, 2, 1)
)
psampSampRandOutOfNParamSetEntry.setIndexNames(
    (0, "PSAMP-MIB", "psampSampRandOutOfNIndex"),
)
if mibBuilder.loadTexts:
    psampSampRandOutOfNParamSetEntry.setStatus("current")


class _PsampSampRandOutOfNIndex_Type(Integer32):
    """Custom type psampSampRandOutOfNIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PsampSampRandOutOfNIndex_Type.__name__ = "Integer32"
_PsampSampRandOutOfNIndex_Object = MibTableColumn
psampSampRandOutOfNIndex = _PsampSampRandOutOfNIndex_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 4, 2, 1, 1),
    _PsampSampRandOutOfNIndex_Type()
)
psampSampRandOutOfNIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    psampSampRandOutOfNIndex.setStatus("current")
_PsampSampRandOutOfNSize_Type = Unsigned32
_PsampSampRandOutOfNSize_Object = MibTableColumn
psampSampRandOutOfNSize = _PsampSampRandOutOfNSize_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 4, 2, 1, 2),
    _PsampSampRandOutOfNSize_Type()
)
psampSampRandOutOfNSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psampSampRandOutOfNSize.setStatus("current")
if mibBuilder.loadTexts:
    psampSampRandOutOfNSize.setUnits("packets")
_PsampSampRandOutOfNPopulation_Type = Unsigned32
_PsampSampRandOutOfNPopulation_Object = MibTableColumn
psampSampRandOutOfNPopulation = _PsampSampRandOutOfNPopulation_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 4, 2, 1, 3),
    _PsampSampRandOutOfNPopulation_Type()
)
psampSampRandOutOfNPopulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psampSampRandOutOfNPopulation.setStatus("current")
if mibBuilder.loadTexts:
    psampSampRandOutOfNPopulation.setUnits("packets")
_PsampSampUniProb_ObjectIdentity = ObjectIdentity
psampSampUniProb = _PsampSampUniProb_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 5)
)
_PsampSampUniProbAvail_Type = TruthValue
_PsampSampUniProbAvail_Object = MibScalar
psampSampUniProbAvail = _PsampSampUniProbAvail_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 5, 1),
    _PsampSampUniProbAvail_Type()
)
psampSampUniProbAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psampSampUniProbAvail.setStatus("current")
_PsampSampUniProbParamSetTable_Object = MibTable
psampSampUniProbParamSetTable = _PsampSampUniProbParamSetTable_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    psampSampUniProbParamSetTable.setStatus("current")
_PsampSampUniProbParamSetEntry_Object = MibTableRow
psampSampUniProbParamSetEntry = _PsampSampUniProbParamSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 5, 2, 1)
)
psampSampUniProbParamSetEntry.setIndexNames(
    (0, "PSAMP-MIB", "psampSampUniProbIndex"),
)
if mibBuilder.loadTexts:
    psampSampUniProbParamSetEntry.setStatus("current")


class _PsampSampUniProbIndex_Type(Integer32):
    """Custom type psampSampUniProbIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PsampSampUniProbIndex_Type.__name__ = "Integer32"
_PsampSampUniProbIndex_Object = MibTableColumn
psampSampUniProbIndex = _PsampSampUniProbIndex_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 5, 2, 1, 1),
    _PsampSampUniProbIndex_Type()
)
psampSampUniProbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    psampSampUniProbIndex.setStatus("current")
_PsampSampUniProbProbability_Type = Float64TC
_PsampSampUniProbProbability_Object = MibTableColumn
psampSampUniProbProbability = _PsampSampUniProbProbability_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 5, 2, 1, 2),
    _PsampSampUniProbProbability_Type()
)
psampSampUniProbProbability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psampSampUniProbProbability.setStatus("current")
_PsampFiltPropMatch_ObjectIdentity = ObjectIdentity
psampFiltPropMatch = _PsampFiltPropMatch_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 6)
)
_PsampFiltPropMatchAvail_Type = TruthValue
_PsampFiltPropMatchAvail_Object = MibScalar
psampFiltPropMatchAvail = _PsampFiltPropMatchAvail_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 6, 1),
    _PsampFiltPropMatchAvail_Type()
)
psampFiltPropMatchAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psampFiltPropMatchAvail.setStatus("current")
_PsampFiltHash_ObjectIdentity = ObjectIdentity
psampFiltHash = _PsampFiltHash_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 7)
)
_PsampFiltHashAvail_Type = TruthValue
_PsampFiltHashAvail_Object = MibScalar
psampFiltHashAvail = _PsampFiltHashAvail_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 7, 1),
    _PsampFiltHashAvail_Type()
)
psampFiltHashAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psampFiltHashAvail.setStatus("current")
_PsampFiltHashCapabilities_ObjectIdentity = ObjectIdentity
psampFiltHashCapabilities = _PsampFiltHashCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 7, 2)
)
_PsampFiltHashParamSetTable_Object = MibTable
psampFiltHashParamSetTable = _PsampFiltHashParamSetTable_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 7, 3)
)
if mibBuilder.loadTexts:
    psampFiltHashParamSetTable.setStatus("current")
_PsampFiltHashParamSetEntry_Object = MibTableRow
psampFiltHashParamSetEntry = _PsampFiltHashParamSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 7, 3, 1)
)
psampFiltHashParamSetEntry.setIndexNames(
    (0, "PSAMP-MIB", "psampFiltHashIndex"),
)
if mibBuilder.loadTexts:
    psampFiltHashParamSetEntry.setStatus("current")


class _PsampFiltHashIndex_Type(Integer32):
    """Custom type psampFiltHashIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PsampFiltHashIndex_Type.__name__ = "Integer32"
_PsampFiltHashIndex_Object = MibTableColumn
psampFiltHashIndex = _PsampFiltHashIndex_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 7, 3, 1, 1),
    _PsampFiltHashIndex_Type()
)
psampFiltHashIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    psampFiltHashIndex.setStatus("current")


class _PsampFiltHashFunction_Type(Integer32):
    """Custom type psampFiltHashFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bob", 3),
          ("crc32", 1),
          ("ipsx", 2))
    )


_PsampFiltHashFunction_Type.__name__ = "Integer32"
_PsampFiltHashFunction_Object = MibTableColumn
psampFiltHashFunction = _PsampFiltHashFunction_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 7, 3, 1, 2),
    _PsampFiltHashFunction_Type()
)
psampFiltHashFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psampFiltHashFunction.setStatus("current")
_PsampFiltHashInitializerValue_Type = Unsigned64TC
_PsampFiltHashInitializerValue_Object = MibTableColumn
psampFiltHashInitializerValue = _PsampFiltHashInitializerValue_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 7, 3, 1, 3),
    _PsampFiltHashInitializerValue_Type()
)
psampFiltHashInitializerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psampFiltHashInitializerValue.setStatus("current")
_PsampFiltHashIpPayloadOffset_Type = Unsigned64TC
_PsampFiltHashIpPayloadOffset_Object = MibTableColumn
psampFiltHashIpPayloadOffset = _PsampFiltHashIpPayloadOffset_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 7, 3, 1, 4),
    _PsampFiltHashIpPayloadOffset_Type()
)
psampFiltHashIpPayloadOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psampFiltHashIpPayloadOffset.setStatus("current")
_PsampFiltHashIpPayloadSize_Type = Unsigned64TC
_PsampFiltHashIpPayloadSize_Object = MibTableColumn
psampFiltHashIpPayloadSize = _PsampFiltHashIpPayloadSize_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 7, 3, 1, 5),
    _PsampFiltHashIpPayloadSize_Type()
)
psampFiltHashIpPayloadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psampFiltHashIpPayloadSize.setStatus("current")
_PsampFiltHashSelectedRangeMin_Type = Unsigned64TC
_PsampFiltHashSelectedRangeMin_Object = MibTableColumn
psampFiltHashSelectedRangeMin = _PsampFiltHashSelectedRangeMin_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 7, 3, 1, 6),
    _PsampFiltHashSelectedRangeMin_Type()
)
psampFiltHashSelectedRangeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psampFiltHashSelectedRangeMin.setStatus("current")
_PsampFiltHashSelectedRangeMax_Type = Unsigned64TC
_PsampFiltHashSelectedRangeMax_Object = MibTableColumn
psampFiltHashSelectedRangeMax = _PsampFiltHashSelectedRangeMax_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 7, 3, 1, 7),
    _PsampFiltHashSelectedRangeMax_Type()
)
psampFiltHashSelectedRangeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psampFiltHashSelectedRangeMax.setStatus("current")
_PsampFiltHashOutputRangeMin_Type = Unsigned64TC
_PsampFiltHashOutputRangeMin_Object = MibTableColumn
psampFiltHashOutputRangeMin = _PsampFiltHashOutputRangeMin_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 7, 3, 1, 8),
    _PsampFiltHashOutputRangeMin_Type()
)
psampFiltHashOutputRangeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psampFiltHashOutputRangeMin.setStatus("current")
_PsampFiltHashOutputRangeMax_Type = Unsigned64TC
_PsampFiltHashOutputRangeMax_Object = MibTableColumn
psampFiltHashOutputRangeMax = _PsampFiltHashOutputRangeMax_Object(
    (1, 3, 6, 1, 2, 1, 194, 1, 1, 7, 3, 1, 9),
    _PsampFiltHashOutputRangeMax_Type()
)
psampFiltHashOutputRangeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psampFiltHashOutputRangeMax.setStatus("current")
_PsampObjects_ObjectIdentity = ObjectIdentity
psampObjects = _PsampObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 212, 1)
)
_PsampConformance_ObjectIdentity = ObjectIdentity
psampConformance = _PsampConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 212, 2)
)
_PsampCompliances_ObjectIdentity = ObjectIdentity
psampCompliances = _PsampCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 212, 2, 1)
)
_PsampGroups_ObjectIdentity = ObjectIdentity
psampGroups = _PsampGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 212, 2, 2)
)

# Managed Objects groups

psampGroupSampCountBased = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 212, 2, 2, 1)
)
psampGroupSampCountBased.setObjects(
      *(("PSAMP-MIB", "psampSampCountBasedAvail"),
        ("PSAMP-MIB", "psampSampCountBasedInterval"),
        ("PSAMP-MIB", "psampSampCountBasedSpace"))
)
if mibBuilder.loadTexts:
    psampGroupSampCountBased.setStatus("current")

psampGroupSampTimeBased = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 212, 2, 2, 2)
)
psampGroupSampTimeBased.setObjects(
      *(("PSAMP-MIB", "psampSampTimeBasedAvail"),
        ("PSAMP-MIB", "psampSampTimeBasedInterval"),
        ("PSAMP-MIB", "psampSampTimeBasedSpace"))
)
if mibBuilder.loadTexts:
    psampGroupSampTimeBased.setStatus("current")

psampGroupSampRandOutOfN = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 212, 2, 2, 3)
)
psampGroupSampRandOutOfN.setObjects(
      *(("PSAMP-MIB", "psampSampRandOutOfNAvail"),
        ("PSAMP-MIB", "psampSampRandOutOfNSize"),
        ("PSAMP-MIB", "psampSampRandOutOfNPopulation"))
)
if mibBuilder.loadTexts:
    psampGroupSampRandOutOfN.setStatus("current")

psampGroupSampUniProb = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 212, 2, 2, 4)
)
psampGroupSampUniProb.setObjects(
      *(("PSAMP-MIB", "psampSampUniProbAvail"),
        ("PSAMP-MIB", "psampSampUniProbProbability"))
)
if mibBuilder.loadTexts:
    psampGroupSampUniProb.setStatus("current")

psampGroupFiltPropMatch = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 212, 2, 2, 5)
)
psampGroupFiltPropMatch.setObjects(
    ("PSAMP-MIB", "psampFiltPropMatchAvail")
)
if mibBuilder.loadTexts:
    psampGroupFiltPropMatch.setStatus("current")

psampGroupFiltHash = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 212, 2, 2, 6)
)
psampGroupFiltHash.setObjects(
      *(("PSAMP-MIB", "psampFiltHashAvail"),
        ("PSAMP-MIB", "psampFiltHashFunction"),
        ("PSAMP-MIB", "psampFiltHashInitializerValue"),
        ("PSAMP-MIB", "psampFiltHashIpPayloadOffset"),
        ("PSAMP-MIB", "psampFiltHashIpPayloadSize"),
        ("PSAMP-MIB", "psampFiltHashSelectedRangeMin"),
        ("PSAMP-MIB", "psampFiltHashSelectedRangeMax"),
        ("PSAMP-MIB", "psampFiltHashOutputRangeMin"),
        ("PSAMP-MIB", "psampFiltHashOutputRangeMax"))
)
if mibBuilder.loadTexts:
    psampGroupFiltHash.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

psampCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 212, 2, 1, 1)
)
if mibBuilder.loadTexts:
    psampCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PSAMP-MIB",
    **{"psampSampCountBased": psampSampCountBased,
       "psampSampCountBasedAvail": psampSampCountBasedAvail,
       "psampSampCountBasedParamSetTable": psampSampCountBasedParamSetTable,
       "psampSampCountBasedParamSetEntry": psampSampCountBasedParamSetEntry,
       "psampSampCountBasedIndex": psampSampCountBasedIndex,
       "psampSampCountBasedInterval": psampSampCountBasedInterval,
       "psampSampCountBasedSpace": psampSampCountBasedSpace,
       "psampSampTimeBased": psampSampTimeBased,
       "psampSampTimeBasedAvail": psampSampTimeBasedAvail,
       "psampSampTimeBasedParamSetTable": psampSampTimeBasedParamSetTable,
       "psampSampTimeBasedParamSetEntry": psampSampTimeBasedParamSetEntry,
       "psampSampTimeBasedIndex": psampSampTimeBasedIndex,
       "psampSampTimeBasedInterval": psampSampTimeBasedInterval,
       "psampSampTimeBasedSpace": psampSampTimeBasedSpace,
       "psampSampRandOutOfN": psampSampRandOutOfN,
       "psampSampRandOutOfNAvail": psampSampRandOutOfNAvail,
       "psampSampRandOutOfNParamSetTable": psampSampRandOutOfNParamSetTable,
       "psampSampRandOutOfNParamSetEntry": psampSampRandOutOfNParamSetEntry,
       "psampSampRandOutOfNIndex": psampSampRandOutOfNIndex,
       "psampSampRandOutOfNSize": psampSampRandOutOfNSize,
       "psampSampRandOutOfNPopulation": psampSampRandOutOfNPopulation,
       "psampSampUniProb": psampSampUniProb,
       "psampSampUniProbAvail": psampSampUniProbAvail,
       "psampSampUniProbParamSetTable": psampSampUniProbParamSetTable,
       "psampSampUniProbParamSetEntry": psampSampUniProbParamSetEntry,
       "psampSampUniProbIndex": psampSampUniProbIndex,
       "psampSampUniProbProbability": psampSampUniProbProbability,
       "psampFiltPropMatch": psampFiltPropMatch,
       "psampFiltPropMatchAvail": psampFiltPropMatchAvail,
       "psampFiltHash": psampFiltHash,
       "psampFiltHashAvail": psampFiltHashAvail,
       "psampFiltHashCapabilities": psampFiltHashCapabilities,
       "psampFiltHashParamSetTable": psampFiltHashParamSetTable,
       "psampFiltHashParamSetEntry": psampFiltHashParamSetEntry,
       "psampFiltHashIndex": psampFiltHashIndex,
       "psampFiltHashFunction": psampFiltHashFunction,
       "psampFiltHashInitializerValue": psampFiltHashInitializerValue,
       "psampFiltHashIpPayloadOffset": psampFiltHashIpPayloadOffset,
       "psampFiltHashIpPayloadSize": psampFiltHashIpPayloadSize,
       "psampFiltHashSelectedRangeMin": psampFiltHashSelectedRangeMin,
       "psampFiltHashSelectedRangeMax": psampFiltHashSelectedRangeMax,
       "psampFiltHashOutputRangeMin": psampFiltHashOutputRangeMin,
       "psampFiltHashOutputRangeMax": psampFiltHashOutputRangeMax,
       "psampMIB": psampMIB,
       "psampObjects": psampObjects,
       "psampConformance": psampConformance,
       "psampCompliances": psampCompliances,
       "psampCompliance": psampCompliance,
       "psampGroups": psampGroups,
       "psampGroupSampCountBased": psampGroupSampCountBased,
       "psampGroupSampTimeBased": psampGroupSampTimeBased,
       "psampGroupSampRandOutOfN": psampGroupSampRandOutOfN,
       "psampGroupSampUniProb": psampGroupSampUniProb,
       "psampGroupFiltPropMatch": psampGroupFiltPropMatch,
       "psampGroupFiltHash": psampGroupFiltHash}
)
