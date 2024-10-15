# SNMP MIB module (HJ-PNNI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HJ-PNNI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:49 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(pnniLinkPortId,
 pnniNbrPeerRemoteNodeId,
 pnniNodeIndex) = mibBuilder.importSymbols(
    "PNNI-MIB",
    "pnniLinkPortId",
    "pnniNbrPeerRemoteNodeId",
    "pnniNodeIndex")

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
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "mgmt")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class Counter32(Counter32):
    """Custom type Counter32 based on Counter32"""




class Integer32(Integer32):
    """Custom type Integer32 based on Integer32"""




class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )





class Unsigned32(Gauge32):
    """Custom type Unsigned32 based on Gauge32"""




class PnniPortId(Unsigned32):
    """Custom type PnniPortId based on Unsigned32"""




class HjPnniIfResourceIndex(Integer32):
    """Custom type HjPnniIfResourceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Harrisjeffries_ObjectIdentity = ObjectIdentity
harrisjeffries = _Harrisjeffries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 603)
)
_HjStdExtensions_ObjectIdentity = ObjectIdentity
hjStdExtensions = _HjStdExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 603, 2)
)
_HjTransmission_ObjectIdentity = ObjectIdentity
hjTransmission = _HjTransmission_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 603, 2, 10)
)
_HjAtm_ObjectIdentity = ObjectIdentity
hjAtm = _HjAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2)
)
_HjAtmPnni_ObjectIdentity = ObjectIdentity
hjAtmPnni = _HjAtmPnni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7)
)
_HjPnniBaseGroup_ObjectIdentity = ObjectIdentity
hjPnniBaseGroup = _HjPnniBaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 2)
)
_HjPnniLoggingFile_Type = DisplayString
_HjPnniLoggingFile_Object = MibScalar
hjPnniLoggingFile = _HjPnniLoggingFile_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 2, 1),
    _HjPnniLoggingFile_Type()
)
hjPnniLoggingFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniLoggingFile.setStatus("mandatory")


class _HjPnniLoggingMask_Type(Unsigned32):
    """Custom type hjPnniLoggingMask based on Unsigned32"""
    defaultValue = 0


_HjPnniLoggingMask_Object = MibScalar
hjPnniLoggingMask = _HjPnniLoggingMask_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 2, 2),
    _HjPnniLoggingMask_Type()
)
hjPnniLoggingMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniLoggingMask.setStatus("mandatory")


class _HjPnniAddressRoundRobin_Type(TruthValue):
    """Custom type hjPnniAddressRoundRobin based on TruthValue"""


_HjPnniAddressRoundRobin_Object = MibScalar
hjPnniAddressRoundRobin = _HjPnniAddressRoundRobin_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 2, 3),
    _HjPnniAddressRoundRobin_Type()
)
hjPnniAddressRoundRobin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniAddressRoundRobin.setStatus("mandatory")


class _HjPnniRoundRobinNbrPortUse_Type(TruthValue):
    """Custom type hjPnniRoundRobinNbrPortUse based on TruthValue"""


_HjPnniRoundRobinNbrPortUse_Object = MibScalar
hjPnniRoundRobinNbrPortUse = _HjPnniRoundRobinNbrPortUse_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 2, 4),
    _HjPnniRoundRobinNbrPortUse_Type()
)
hjPnniRoundRobinNbrPortUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniRoundRobinNbrPortUse.setStatus("mandatory")


class _HjPnniCacheTimerFreq_Type(Integer32):
    """Custom type hjPnniCacheTimerFreq based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_HjPnniCacheTimerFreq_Type.__name__ = "Integer32"
_HjPnniCacheTimerFreq_Object = MibScalar
hjPnniCacheTimerFreq = _HjPnniCacheTimerFreq_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 2, 5),
    _HjPnniCacheTimerFreq_Type()
)
hjPnniCacheTimerFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniCacheTimerFreq.setStatus("mandatory")


class _HjPnniCacheAge_Type(Integer32):
    """Custom type hjPnniCacheAge based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_HjPnniCacheAge_Type.__name__ = "Integer32"
_HjPnniCacheAge_Object = MibScalar
hjPnniCacheAge = _HjPnniCacheAge_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 2, 6),
    _HjPnniCacheAge_Type()
)
hjPnniCacheAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniCacheAge.setStatus("mandatory")


class _HjPnniCacheRecentInt_Type(Integer32):
    """Custom type hjPnniCacheRecentInt based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_HjPnniCacheRecentInt_Type.__name__ = "Integer32"
_HjPnniCacheRecentInt_Object = MibScalar
hjPnniCacheRecentInt = _HjPnniCacheRecentInt_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 2, 7),
    _HjPnniCacheRecentInt_Type()
)
hjPnniCacheRecentInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniCacheRecentInt.setStatus("mandatory")


class _HjPnniCacheNumEntries_Type(Integer32):
    """Custom type hjPnniCacheNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HjPnniCacheNumEntries_Type.__name__ = "Integer32"
_HjPnniCacheNumEntries_Object = MibScalar
hjPnniCacheNumEntries = _HjPnniCacheNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 2, 8),
    _HjPnniCacheNumEntries_Type()
)
hjPnniCacheNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hjPnniCacheNumEntries.setStatus("mandatory")


class _HjPnniCacheMaxPaths_Type(Integer32):
    """Custom type hjPnniCacheMaxPaths based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_HjPnniCacheMaxPaths_Type.__name__ = "Integer32"
_HjPnniCacheMaxPaths_Object = MibScalar
hjPnniCacheMaxPaths = _HjPnniCacheMaxPaths_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 2, 9),
    _HjPnniCacheMaxPaths_Type()
)
hjPnniCacheMaxPaths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniCacheMaxPaths.setStatus("mandatory")


class _HjPnniCacheMaxEntries_Type(Integer32):
    """Custom type hjPnniCacheMaxEntries based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_HjPnniCacheMaxEntries_Type.__name__ = "Integer32"
_HjPnniCacheMaxEntries_Object = MibScalar
hjPnniCacheMaxEntries = _HjPnniCacheMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 2, 10),
    _HjPnniCacheMaxEntries_Type()
)
hjPnniCacheMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniCacheMaxEntries.setStatus("mandatory")


class _HjPnniCacheEnable_Type(TruthValue):
    """Custom type hjPnniCacheEnable based on TruthValue"""


_HjPnniCacheEnable_Object = MibScalar
hjPnniCacheEnable = _HjPnniCacheEnable_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 2, 11),
    _HjPnniCacheEnable_Type()
)
hjPnniCacheEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniCacheEnable.setStatus("mandatory")


class _HjPnniAllowLGNPathLoops_Type(TruthValue):
    """Custom type hjPnniAllowLGNPathLoops based on TruthValue"""


_HjPnniAllowLGNPathLoops_Object = MibScalar
hjPnniAllowLGNPathLoops = _HjPnniAllowLGNPathLoops_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 2, 12),
    _HjPnniAllowLGNPathLoops_Type()
)
hjPnniAllowLGNPathLoops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniAllowLGNPathLoops.setStatus("mandatory")
_HjPnniNodeTable_Object = MibTable
hjPnniNodeTable = _HjPnniNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 3)
)
if mibBuilder.loadTexts:
    hjPnniNodeTable.setStatus("mandatory")
_HjPnniNodeEntry_Object = MibTableRow
hjPnniNodeEntry = _HjPnniNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 3, 1)
)
hjPnniNodeEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
)
if mibBuilder.loadTexts:
    hjPnniNodeEntry.setStatus("mandatory")


class _HjPnniNodeLoggingMask_Type(Unsigned32):
    """Custom type hjPnniNodeLoggingMask based on Unsigned32"""
    defaultValue = 0


_HjPnniNodeLoggingMask_Object = MibTableColumn
hjPnniNodeLoggingMask = _HjPnniNodeLoggingMask_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 3, 1, 1),
    _HjPnniNodeLoggingMask_Type()
)
hjPnniNodeLoggingMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniNodeLoggingMask.setStatus("mandatory")


class _HjPnniNodeMinDynamicPortId_Type(PnniPortId):
    """Custom type hjPnniNodeMinDynamicPortId based on PnniPortId"""
    defaultValue = 2147483648


_HjPnniNodeMinDynamicPortId_Object = MibTableColumn
hjPnniNodeMinDynamicPortId = _HjPnniNodeMinDynamicPortId_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 3, 1, 2),
    _HjPnniNodeMinDynamicPortId_Type()
)
hjPnniNodeMinDynamicPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniNodeMinDynamicPortId.setStatus("mandatory")


class _HjPnniNodeMaxDynamicPortId_Type(PnniPortId):
    """Custom type hjPnniNodeMaxDynamicPortId based on PnniPortId"""
    defaultValue = 4294967294


_HjPnniNodeMaxDynamicPortId_Object = MibTableColumn
hjPnniNodeMaxDynamicPortId = _HjPnniNodeMaxDynamicPortId_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 3, 1, 3),
    _HjPnniNodeMaxDynamicPortId_Type()
)
hjPnniNodeMaxDynamicPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniNodeMaxDynamicPortId.setStatus("mandatory")


class _HjPnniNodeSvccCellTransferDelay_Type(Integer32):
    """Custom type hjPnniNodeSvccCellTransferDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HjPnniNodeSvccCellTransferDelay_Type.__name__ = "Integer32"
_HjPnniNodeSvccCellTransferDelay_Object = MibTableColumn
hjPnniNodeSvccCellTransferDelay = _HjPnniNodeSvccCellTransferDelay_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 3, 1, 4),
    _HjPnniNodeSvccCellTransferDelay_Type()
)
hjPnniNodeSvccCellTransferDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniNodeSvccCellTransferDelay.setStatus("mandatory")


class _HjPnniNodeSvccCellDelayVariation_Type(Integer32):
    """Custom type hjPnniNodeSvccCellDelayVariation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HjPnniNodeSvccCellDelayVariation_Type.__name__ = "Integer32"
_HjPnniNodeSvccCellDelayVariation_Object = MibTableColumn
hjPnniNodeSvccCellDelayVariation = _HjPnniNodeSvccCellDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 3, 1, 5),
    _HjPnniNodeSvccCellDelayVariation_Type()
)
hjPnniNodeSvccCellDelayVariation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniNodeSvccCellDelayVariation.setStatus("mandatory")


class _HjPnniNodeSvccCellLossRatio_Type(Integer32):
    """Custom type hjPnniNodeSvccCellLossRatio based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HjPnniNodeSvccCellLossRatio_Type.__name__ = "Integer32"
_HjPnniNodeSvccCellLossRatio_Object = MibTableColumn
hjPnniNodeSvccCellLossRatio = _HjPnniNodeSvccCellLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 3, 1, 6),
    _HjPnniNodeSvccCellLossRatio_Type()
)
hjPnniNodeSvccCellLossRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniNodeSvccCellLossRatio.setStatus("mandatory")


class _HjPnniNodeSvccAbrInitialCellRate_Type(Integer32):
    """Custom type hjPnniNodeSvccAbrInitialCellRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_HjPnniNodeSvccAbrInitialCellRate_Type.__name__ = "Integer32"
_HjPnniNodeSvccAbrInitialCellRate_Object = MibTableColumn
hjPnniNodeSvccAbrInitialCellRate = _HjPnniNodeSvccAbrInitialCellRate_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 3, 1, 7),
    _HjPnniNodeSvccAbrInitialCellRate_Type()
)
hjPnniNodeSvccAbrInitialCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniNodeSvccAbrInitialCellRate.setStatus("mandatory")


class _HjPnniNodeSvccAbrTransientBufferExposure_Type(Integer32):
    """Custom type hjPnniNodeSvccAbrTransientBufferExposure based on Integer32"""
    defaultValue = 16777215

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_HjPnniNodeSvccAbrTransientBufferExposure_Type.__name__ = "Integer32"
_HjPnniNodeSvccAbrTransientBufferExposure_Object = MibTableColumn
hjPnniNodeSvccAbrTransientBufferExposure = _HjPnniNodeSvccAbrTransientBufferExposure_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 3, 1, 8),
    _HjPnniNodeSvccAbrTransientBufferExposure_Type()
)
hjPnniNodeSvccAbrTransientBufferExposure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniNodeSvccAbrTransientBufferExposure.setStatus("mandatory")


class _HjPnniNodeSvccAbrRateIncreaseFactor_Type(Integer32):
    """Custom type hjPnniNodeSvccAbrRateIncreaseFactor based on Integer32"""
    defaultValue = 11

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HjPnniNodeSvccAbrRateIncreaseFactor_Type.__name__ = "Integer32"
_HjPnniNodeSvccAbrRateIncreaseFactor_Object = MibTableColumn
hjPnniNodeSvccAbrRateIncreaseFactor = _HjPnniNodeSvccAbrRateIncreaseFactor_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 3, 1, 9),
    _HjPnniNodeSvccAbrRateIncreaseFactor_Type()
)
hjPnniNodeSvccAbrRateIncreaseFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniNodeSvccAbrRateIncreaseFactor.setStatus("mandatory")


class _HjPnniNodeSvccAbrRateDecreaseFactor_Type(Integer32):
    """Custom type hjPnniNodeSvccAbrRateDecreaseFactor based on Integer32"""
    defaultValue = 11

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HjPnniNodeSvccAbrRateDecreaseFactor_Type.__name__ = "Integer32"
_HjPnniNodeSvccAbrRateDecreaseFactor_Object = MibTableColumn
hjPnniNodeSvccAbrRateDecreaseFactor = _HjPnniNodeSvccAbrRateDecreaseFactor_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 3, 1, 10),
    _HjPnniNodeSvccAbrRateDecreaseFactor_Type()
)
hjPnniNodeSvccAbrRateDecreaseFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniNodeSvccAbrRateDecreaseFactor.setStatus("mandatory")
_HjPnniIfTable_Object = MibTable
hjPnniIfTable = _HjPnniIfTable_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 4)
)
if mibBuilder.loadTexts:
    hjPnniIfTable.setStatus("mandatory")
_HjPnniIfEntry_Object = MibTableRow
hjPnniIfEntry = _HjPnniIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 4, 1)
)
hjPnniIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hjPnniIfEntry.setStatus("mandatory")


class _HjPnniIfLoggingMask_Type(Unsigned32):
    """Custom type hjPnniIfLoggingMask based on Unsigned32"""
    defaultValue = 0


_HjPnniIfLoggingMask_Object = MibTableColumn
hjPnniIfLoggingMask = _HjPnniIfLoggingMask_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 4, 1, 1),
    _HjPnniIfLoggingMask_Type()
)
hjPnniIfLoggingMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniIfLoggingMask.setStatus("mandatory")


class _HjPnniIfMaxRccPacketSize_Type(Integer32):
    """Custom type hjPnniIfMaxRccPacketSize based on Integer32"""
    defaultValue = 8192

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 8192),
    )


_HjPnniIfMaxRccPacketSize_Type.__name__ = "Integer32"
_HjPnniIfMaxRccPacketSize_Object = MibTableColumn
hjPnniIfMaxRccPacketSize = _HjPnniIfMaxRccPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 4, 1, 2),
    _HjPnniIfMaxRccPacketSize_Type()
)
hjPnniIfMaxRccPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniIfMaxRccPacketSize.setStatus("mandatory")
_HjPnniIfCbrResourceIndex_Type = HjPnniIfResourceIndex
_HjPnniIfCbrResourceIndex_Object = MibTableColumn
hjPnniIfCbrResourceIndex = _HjPnniIfCbrResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 4, 1, 3),
    _HjPnniIfCbrResourceIndex_Type()
)
hjPnniIfCbrResourceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniIfCbrResourceIndex.setStatus("mandatory")
_HjPnniIfRtVbrResourceIndex_Type = HjPnniIfResourceIndex
_HjPnniIfRtVbrResourceIndex_Object = MibTableColumn
hjPnniIfRtVbrResourceIndex = _HjPnniIfRtVbrResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 4, 1, 4),
    _HjPnniIfRtVbrResourceIndex_Type()
)
hjPnniIfRtVbrResourceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniIfRtVbrResourceIndex.setStatus("mandatory")
_HjPnniIfNrtVbrResourceIndex_Type = HjPnniIfResourceIndex
_HjPnniIfNrtVbrResourceIndex_Object = MibTableColumn
hjPnniIfNrtVbrResourceIndex = _HjPnniIfNrtVbrResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 4, 1, 5),
    _HjPnniIfNrtVbrResourceIndex_Type()
)
hjPnniIfNrtVbrResourceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniIfNrtVbrResourceIndex.setStatus("mandatory")
_HjPnniIfAbrResourceIndex_Type = HjPnniIfResourceIndex
_HjPnniIfAbrResourceIndex_Object = MibTableColumn
hjPnniIfAbrResourceIndex = _HjPnniIfAbrResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 4, 1, 6),
    _HjPnniIfAbrResourceIndex_Type()
)
hjPnniIfAbrResourceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniIfAbrResourceIndex.setStatus("mandatory")
_HjPnniIfUbrResourceIndex_Type = HjPnniIfResourceIndex
_HjPnniIfUbrResourceIndex_Object = MibTableColumn
hjPnniIfUbrResourceIndex = _HjPnniIfUbrResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 4, 1, 7),
    _HjPnniIfUbrResourceIndex_Type()
)
hjPnniIfUbrResourceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniIfUbrResourceIndex.setStatus("mandatory")
_HjPnniNbrPeerTable_Object = MibTable
hjPnniNbrPeerTable = _HjPnniNbrPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 5)
)
if mibBuilder.loadTexts:
    hjPnniNbrPeerTable.setStatus("mandatory")
_HjPnniNbrPeerEntry_Object = MibTableRow
hjPnniNbrPeerEntry = _HjPnniNbrPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 5, 1)
)
hjPnniNbrPeerEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "PNNI-MIB", "pnniNbrPeerRemoteNodeId"),
)
if mibBuilder.loadTexts:
    hjPnniNbrPeerEntry.setStatus("mandatory")
_HjPnniNbrPeerRcvPtses_Type = Counter32
_HjPnniNbrPeerRcvPtses_Object = MibTableColumn
hjPnniNbrPeerRcvPtses = _HjPnniNbrPeerRcvPtses_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 5, 1, 1),
    _HjPnniNbrPeerRcvPtses_Type()
)
hjPnniNbrPeerRcvPtses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hjPnniNbrPeerRcvPtses.setStatus("mandatory")
_HjPnniNbrPeerXmtPtses_Type = Counter32
_HjPnniNbrPeerXmtPtses_Object = MibTableColumn
hjPnniNbrPeerXmtPtses = _HjPnniNbrPeerXmtPtses_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 5, 1, 2),
    _HjPnniNbrPeerXmtPtses_Type()
)
hjPnniNbrPeerXmtPtses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hjPnniNbrPeerXmtPtses.setStatus("mandatory")
_HjPnniNbrPeerRcvPtseErrs_Type = Counter32
_HjPnniNbrPeerRcvPtseErrs_Object = MibTableColumn
hjPnniNbrPeerRcvPtseErrs = _HjPnniNbrPeerRcvPtseErrs_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 5, 1, 3),
    _HjPnniNbrPeerRcvPtseErrs_Type()
)
hjPnniNbrPeerRcvPtseErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hjPnniNbrPeerRcvPtseErrs.setStatus("mandatory")
_HjPnniNbrPeerRcvDbSummErrs_Type = Counter32
_HjPnniNbrPeerRcvDbSummErrs_Object = MibTableColumn
hjPnniNbrPeerRcvDbSummErrs = _HjPnniNbrPeerRcvDbSummErrs_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 5, 1, 4),
    _HjPnniNbrPeerRcvDbSummErrs_Type()
)
hjPnniNbrPeerRcvDbSummErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hjPnniNbrPeerRcvDbSummErrs.setStatus("mandatory")
_HjPnniNbrPeerRcvPtspErrs_Type = Counter32
_HjPnniNbrPeerRcvPtspErrs_Object = MibTableColumn
hjPnniNbrPeerRcvPtspErrs = _HjPnniNbrPeerRcvPtspErrs_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 5, 1, 5),
    _HjPnniNbrPeerRcvPtspErrs_Type()
)
hjPnniNbrPeerRcvPtspErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hjPnniNbrPeerRcvPtspErrs.setStatus("mandatory")
_HjPnniNbrPeerRcvPtseReqErrs_Type = Counter32
_HjPnniNbrPeerRcvPtseReqErrs_Object = MibTableColumn
hjPnniNbrPeerRcvPtseReqErrs = _HjPnniNbrPeerRcvPtseReqErrs_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 5, 1, 6),
    _HjPnniNbrPeerRcvPtseReqErrs_Type()
)
hjPnniNbrPeerRcvPtseReqErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hjPnniNbrPeerRcvPtseReqErrs.setStatus("mandatory")
_HjPnniNbrPeerRcvPtseAckErrs_Type = Counter32
_HjPnniNbrPeerRcvPtseAckErrs_Object = MibTableColumn
hjPnniNbrPeerRcvPtseAckErrs = _HjPnniNbrPeerRcvPtseAckErrs_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 5, 1, 7),
    _HjPnniNbrPeerRcvPtseAckErrs_Type()
)
hjPnniNbrPeerRcvPtseAckErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hjPnniNbrPeerRcvPtseAckErrs.setStatus("mandatory")
_HjPnniNbrPeerDSMismatches_Type = Counter32
_HjPnniNbrPeerDSMismatches_Object = MibTableColumn
hjPnniNbrPeerDSMismatches = _HjPnniNbrPeerDSMismatches_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 5, 1, 8),
    _HjPnniNbrPeerDSMismatches_Type()
)
hjPnniNbrPeerDSMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hjPnniNbrPeerDSMismatches.setStatus("mandatory")
_HjPnniNbrPeerBadPtseReqs_Type = Counter32
_HjPnniNbrPeerBadPtseReqs_Object = MibTableColumn
hjPnniNbrPeerBadPtseReqs = _HjPnniNbrPeerBadPtseReqs_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 5, 1, 9),
    _HjPnniNbrPeerBadPtseReqs_Type()
)
hjPnniNbrPeerBadPtseReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hjPnniNbrPeerBadPtseReqs.setStatus("mandatory")
_HjPnniLinkTable_Object = MibTable
hjPnniLinkTable = _HjPnniLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 6)
)
if mibBuilder.loadTexts:
    hjPnniLinkTable.setStatus("mandatory")
_HjPnniLinkEntry_Object = MibTableRow
hjPnniLinkEntry = _HjPnniLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 6, 1)
)
hjPnniLinkEntry.setIndexNames(
    (0, "PNNI-MIB", "pnniNodeIndex"),
    (0, "PNNI-MIB", "pnniLinkPortId"),
)
if mibBuilder.loadTexts:
    hjPnniLinkEntry.setStatus("mandatory")
_HjPnniLinkRcvUnknownPkts_Type = Counter32
_HjPnniLinkRcvUnknownPkts_Object = MibTableColumn
hjPnniLinkRcvUnknownPkts = _HjPnniLinkRcvUnknownPkts_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 6, 1, 1),
    _HjPnniLinkRcvUnknownPkts_Type()
)
hjPnniLinkRcvUnknownPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hjPnniLinkRcvUnknownPkts.setStatus("mandatory")
_HjPnniLinkRcvHelloMismatches_Type = Counter32
_HjPnniLinkRcvHelloMismatches_Object = MibTableColumn
hjPnniLinkRcvHelloMismatches = _HjPnniLinkRcvHelloMismatches_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 6, 1, 2),
    _HjPnniLinkRcvHelloMismatches_Type()
)
hjPnniLinkRcvHelloMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hjPnniLinkRcvHelloMismatches.setStatus("mandatory")
_HjPnniLinkRcvHelloErrors_Type = Counter32
_HjPnniLinkRcvHelloErrors_Object = MibTableColumn
hjPnniLinkRcvHelloErrors = _HjPnniLinkRcvHelloErrors_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 6, 1, 3),
    _HjPnniLinkRcvHelloErrors_Type()
)
hjPnniLinkRcvHelloErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hjPnniLinkRcvHelloErrors.setStatus("mandatory")
_HjPnniIfResourceTable_Object = MibTable
hjPnniIfResourceTable = _HjPnniIfResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 7)
)
if mibBuilder.loadTexts:
    hjPnniIfResourceTable.setStatus("mandatory")
_HjPnniIfResourceEntry_Object = MibTableRow
hjPnniIfResourceEntry = _HjPnniIfResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 7, 1)
)
hjPnniIfResourceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HJ-PNNI-MIB", "hjPnniIfResourceIndex"),
)
if mibBuilder.loadTexts:
    hjPnniIfResourceEntry.setStatus("mandatory")
_HjPnniIfResourceIndex_Type = HjPnniIfResourceIndex
_HjPnniIfResourceIndex_Object = MibTableColumn
hjPnniIfResourceIndex = _HjPnniIfResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 7, 1, 1),
    _HjPnniIfResourceIndex_Type()
)
hjPnniIfResourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hjPnniIfResourceIndex.setStatus("mandatory")


class _HjPnniIfResourceGCACCLPAttribute_Type(TruthValue):
    """Custom type hjPnniIfResourceGCACCLPAttribute based on TruthValue"""


_HjPnniIfResourceGCACCLPAttribute_Object = MibTableColumn
hjPnniIfResourceGCACCLPAttribute = _HjPnniIfResourceGCACCLPAttribute_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 7, 1, 2),
    _HjPnniIfResourceGCACCLPAttribute_Type()
)
hjPnniIfResourceGCACCLPAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniIfResourceGCACCLPAttribute.setStatus("mandatory")


class _HjPnniIfResourceAdmWeight_Type(Unsigned32):
    """Custom type hjPnniIfResourceAdmWeight based on Unsigned32"""
    defaultValue = 5040


_HjPnniIfResourceAdmWeight_Object = MibTableColumn
hjPnniIfResourceAdmWeight = _HjPnniIfResourceAdmWeight_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 7, 1, 3),
    _HjPnniIfResourceAdmWeight_Type()
)
hjPnniIfResourceAdmWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniIfResourceAdmWeight.setStatus("mandatory")
_HjPnniIfResourceMaximumCellRate_Type = Unsigned32
_HjPnniIfResourceMaximumCellRate_Object = MibTableColumn
hjPnniIfResourceMaximumCellRate = _HjPnniIfResourceMaximumCellRate_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 7, 1, 4),
    _HjPnniIfResourceMaximumCellRate_Type()
)
hjPnniIfResourceMaximumCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniIfResourceMaximumCellRate.setStatus("mandatory")
_HjPnniIfResourceAvailableCellRate_Type = Unsigned32
_HjPnniIfResourceAvailableCellRate_Object = MibTableColumn
hjPnniIfResourceAvailableCellRate = _HjPnniIfResourceAvailableCellRate_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 7, 1, 5),
    _HjPnniIfResourceAvailableCellRate_Type()
)
hjPnniIfResourceAvailableCellRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniIfResourceAvailableCellRate.setStatus("mandatory")
_HjPnniIfResourceCellTransferDelay_Type = Unsigned32
_HjPnniIfResourceCellTransferDelay_Object = MibTableColumn
hjPnniIfResourceCellTransferDelay = _HjPnniIfResourceCellTransferDelay_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 7, 1, 6),
    _HjPnniIfResourceCellTransferDelay_Type()
)
hjPnniIfResourceCellTransferDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniIfResourceCellTransferDelay.setStatus("mandatory")
_HjPnniIfResourceCellDelayVariation_Type = Unsigned32
_HjPnniIfResourceCellDelayVariation_Object = MibTableColumn
hjPnniIfResourceCellDelayVariation = _HjPnniIfResourceCellDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 7, 1, 7),
    _HjPnniIfResourceCellDelayVariation_Type()
)
hjPnniIfResourceCellDelayVariation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniIfResourceCellDelayVariation.setStatus("mandatory")
_HjPnniIfResourceCellLossRatioCLP0_Type = Unsigned32
_HjPnniIfResourceCellLossRatioCLP0_Object = MibTableColumn
hjPnniIfResourceCellLossRatioCLP0 = _HjPnniIfResourceCellLossRatioCLP0_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 7, 1, 8),
    _HjPnniIfResourceCellLossRatioCLP0_Type()
)
hjPnniIfResourceCellLossRatioCLP0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniIfResourceCellLossRatioCLP0.setStatus("mandatory")
_HjPnniIfResourceCellLossRatioCLP01_Type = Unsigned32
_HjPnniIfResourceCellLossRatioCLP01_Object = MibTableColumn
hjPnniIfResourceCellLossRatioCLP01 = _HjPnniIfResourceCellLossRatioCLP01_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 7, 1, 9),
    _HjPnniIfResourceCellLossRatioCLP01_Type()
)
hjPnniIfResourceCellLossRatioCLP01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniIfResourceCellLossRatioCLP01.setStatus("mandatory")
_HjPnniIfResourceUseOptionalGCAC_Type = TruthValue
_HjPnniIfResourceUseOptionalGCAC_Object = MibTableColumn
hjPnniIfResourceUseOptionalGCAC = _HjPnniIfResourceUseOptionalGCAC_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 7, 1, 10),
    _HjPnniIfResourceUseOptionalGCAC_Type()
)
hjPnniIfResourceUseOptionalGCAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniIfResourceUseOptionalGCAC.setStatus("mandatory")
_HjPnniIfResourceCellRateMargin_Type = Unsigned32
_HjPnniIfResourceCellRateMargin_Object = MibTableColumn
hjPnniIfResourceCellRateMargin = _HjPnniIfResourceCellRateMargin_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 7, 1, 11),
    _HjPnniIfResourceCellRateMargin_Type()
)
hjPnniIfResourceCellRateMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniIfResourceCellRateMargin.setStatus("mandatory")
_HjPnniIfResourceVarianceFactor_Type = Unsigned32
_HjPnniIfResourceVarianceFactor_Object = MibTableColumn
hjPnniIfResourceVarianceFactor = _HjPnniIfResourceVarianceFactor_Object(
    (1, 3, 6, 1, 4, 1, 603, 2, 10, 2, 7, 7, 1, 12),
    _HjPnniIfResourceVarianceFactor_Type()
)
hjPnniIfResourceVarianceFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hjPnniIfResourceVarianceFactor.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HJ-PNNI-MIB",
    **{"DisplayString": DisplayString,
       "Counter32": Counter32,
       "Integer32": Integer32,
       "TruthValue": TruthValue,
       "Unsigned32": Unsigned32,
       "PnniPortId": PnniPortId,
       "HjPnniIfResourceIndex": HjPnniIfResourceIndex,
       "org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "harrisjeffries": harrisjeffries,
       "hjStdExtensions": hjStdExtensions,
       "hjTransmission": hjTransmission,
       "hjAtm": hjAtm,
       "hjAtmPnni": hjAtmPnni,
       "hjPnniBaseGroup": hjPnniBaseGroup,
       "hjPnniLoggingFile": hjPnniLoggingFile,
       "hjPnniLoggingMask": hjPnniLoggingMask,
       "hjPnniAddressRoundRobin": hjPnniAddressRoundRobin,
       "hjPnniRoundRobinNbrPortUse": hjPnniRoundRobinNbrPortUse,
       "hjPnniCacheTimerFreq": hjPnniCacheTimerFreq,
       "hjPnniCacheAge": hjPnniCacheAge,
       "hjPnniCacheRecentInt": hjPnniCacheRecentInt,
       "hjPnniCacheNumEntries": hjPnniCacheNumEntries,
       "hjPnniCacheMaxPaths": hjPnniCacheMaxPaths,
       "hjPnniCacheMaxEntries": hjPnniCacheMaxEntries,
       "hjPnniCacheEnable": hjPnniCacheEnable,
       "hjPnniAllowLGNPathLoops": hjPnniAllowLGNPathLoops,
       "hjPnniNodeTable": hjPnniNodeTable,
       "hjPnniNodeEntry": hjPnniNodeEntry,
       "hjPnniNodeLoggingMask": hjPnniNodeLoggingMask,
       "hjPnniNodeMinDynamicPortId": hjPnniNodeMinDynamicPortId,
       "hjPnniNodeMaxDynamicPortId": hjPnniNodeMaxDynamicPortId,
       "hjPnniNodeSvccCellTransferDelay": hjPnniNodeSvccCellTransferDelay,
       "hjPnniNodeSvccCellDelayVariation": hjPnniNodeSvccCellDelayVariation,
       "hjPnniNodeSvccCellLossRatio": hjPnniNodeSvccCellLossRatio,
       "hjPnniNodeSvccAbrInitialCellRate": hjPnniNodeSvccAbrInitialCellRate,
       "hjPnniNodeSvccAbrTransientBufferExposure": hjPnniNodeSvccAbrTransientBufferExposure,
       "hjPnniNodeSvccAbrRateIncreaseFactor": hjPnniNodeSvccAbrRateIncreaseFactor,
       "hjPnniNodeSvccAbrRateDecreaseFactor": hjPnniNodeSvccAbrRateDecreaseFactor,
       "hjPnniIfTable": hjPnniIfTable,
       "hjPnniIfEntry": hjPnniIfEntry,
       "hjPnniIfLoggingMask": hjPnniIfLoggingMask,
       "hjPnniIfMaxRccPacketSize": hjPnniIfMaxRccPacketSize,
       "hjPnniIfCbrResourceIndex": hjPnniIfCbrResourceIndex,
       "hjPnniIfRtVbrResourceIndex": hjPnniIfRtVbrResourceIndex,
       "hjPnniIfNrtVbrResourceIndex": hjPnniIfNrtVbrResourceIndex,
       "hjPnniIfAbrResourceIndex": hjPnniIfAbrResourceIndex,
       "hjPnniIfUbrResourceIndex": hjPnniIfUbrResourceIndex,
       "hjPnniNbrPeerTable": hjPnniNbrPeerTable,
       "hjPnniNbrPeerEntry": hjPnniNbrPeerEntry,
       "hjPnniNbrPeerRcvPtses": hjPnniNbrPeerRcvPtses,
       "hjPnniNbrPeerXmtPtses": hjPnniNbrPeerXmtPtses,
       "hjPnniNbrPeerRcvPtseErrs": hjPnniNbrPeerRcvPtseErrs,
       "hjPnniNbrPeerRcvDbSummErrs": hjPnniNbrPeerRcvDbSummErrs,
       "hjPnniNbrPeerRcvPtspErrs": hjPnniNbrPeerRcvPtspErrs,
       "hjPnniNbrPeerRcvPtseReqErrs": hjPnniNbrPeerRcvPtseReqErrs,
       "hjPnniNbrPeerRcvPtseAckErrs": hjPnniNbrPeerRcvPtseAckErrs,
       "hjPnniNbrPeerDSMismatches": hjPnniNbrPeerDSMismatches,
       "hjPnniNbrPeerBadPtseReqs": hjPnniNbrPeerBadPtseReqs,
       "hjPnniLinkTable": hjPnniLinkTable,
       "hjPnniLinkEntry": hjPnniLinkEntry,
       "hjPnniLinkRcvUnknownPkts": hjPnniLinkRcvUnknownPkts,
       "hjPnniLinkRcvHelloMismatches": hjPnniLinkRcvHelloMismatches,
       "hjPnniLinkRcvHelloErrors": hjPnniLinkRcvHelloErrors,
       "hjPnniIfResourceTable": hjPnniIfResourceTable,
       "hjPnniIfResourceEntry": hjPnniIfResourceEntry,
       "hjPnniIfResourceIndex": hjPnniIfResourceIndex,
       "hjPnniIfResourceGCACCLPAttribute": hjPnniIfResourceGCACCLPAttribute,
       "hjPnniIfResourceAdmWeight": hjPnniIfResourceAdmWeight,
       "hjPnniIfResourceMaximumCellRate": hjPnniIfResourceMaximumCellRate,
       "hjPnniIfResourceAvailableCellRate": hjPnniIfResourceAvailableCellRate,
       "hjPnniIfResourceCellTransferDelay": hjPnniIfResourceCellTransferDelay,
       "hjPnniIfResourceCellDelayVariation": hjPnniIfResourceCellDelayVariation,
       "hjPnniIfResourceCellLossRatioCLP0": hjPnniIfResourceCellLossRatioCLP0,
       "hjPnniIfResourceCellLossRatioCLP01": hjPnniIfResourceCellLossRatioCLP01,
       "hjPnniIfResourceUseOptionalGCAC": hjPnniIfResourceUseOptionalGCAC,
       "hjPnniIfResourceCellRateMargin": hjPnniIfResourceCellRateMargin,
       "hjPnniIfResourceVarianceFactor": hjPnniIfResourceVarianceFactor}
)
