# SNMP MIB module (Nortel-Magellan-Passport-AtmBearerServiceMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-AtmBearerServiceMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:17 2024
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

(atmIfIndex,
 atmIfVcc,
 atmIfVccIndex,
 atmIfVpc,
 atmIfVpcIndex,
 atmIfVptIndex,
 atmIfVptVcc,
 atmIfVptVccIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-AtmCoreMIB",
    "atmIfIndex",
    "atmIfVcc",
    "atmIfVccIndex",
    "atmIfVpc",
    "atmIfVpcIndex",
    "atmIfVptIndex",
    "atmIfVptVcc",
    "atmIfVptVccIndex")

(DisplayString,
 RowStatus,
 StorageType) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "DisplayString",
    "RowStatus",
    "StorageType")

(Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "Link",
    "NonReplicated")

(passportMIBs,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "passportMIBs")

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

_AtmIfVpcNrp_ObjectIdentity = ObjectIdentity
atmIfVpcNrp = _AtmIfVpcNrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 4)
)
_AtmIfVpcNrpRowStatusTable_Object = MibTable
atmIfVpcNrpRowStatusTable = _AtmIfVpcNrpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 4, 1)
)
if mibBuilder.loadTexts:
    atmIfVpcNrpRowStatusTable.setStatus("mandatory")
_AtmIfVpcNrpRowStatusEntry_Object = MibTableRow
atmIfVpcNrpRowStatusEntry = _AtmIfVpcNrpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 4, 1, 1)
)
atmIfVpcNrpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVpcIndex"),
    (0, "Nortel-Magellan-Passport-AtmBearerServiceMIB", "atmIfVpcNrpIndex"),
)
if mibBuilder.loadTexts:
    atmIfVpcNrpRowStatusEntry.setStatus("mandatory")
_AtmIfVpcNrpRowStatus_Type = RowStatus
_AtmIfVpcNrpRowStatus_Object = MibTableColumn
atmIfVpcNrpRowStatus = _AtmIfVpcNrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 4, 1, 1, 1),
    _AtmIfVpcNrpRowStatus_Type()
)
atmIfVpcNrpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVpcNrpRowStatus.setStatus("mandatory")
_AtmIfVpcNrpComponentName_Type = DisplayString
_AtmIfVpcNrpComponentName_Object = MibTableColumn
atmIfVpcNrpComponentName = _AtmIfVpcNrpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 4, 1, 1, 2),
    _AtmIfVpcNrpComponentName_Type()
)
atmIfVpcNrpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVpcNrpComponentName.setStatus("mandatory")
_AtmIfVpcNrpStorageType_Type = StorageType
_AtmIfVpcNrpStorageType_Object = MibTableColumn
atmIfVpcNrpStorageType = _AtmIfVpcNrpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 4, 1, 1, 4),
    _AtmIfVpcNrpStorageType_Type()
)
atmIfVpcNrpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVpcNrpStorageType.setStatus("mandatory")
_AtmIfVpcNrpIndex_Type = NonReplicated
_AtmIfVpcNrpIndex_Object = MibTableColumn
atmIfVpcNrpIndex = _AtmIfVpcNrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 4, 1, 1, 10),
    _AtmIfVpcNrpIndex_Type()
)
atmIfVpcNrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVpcNrpIndex.setStatus("mandatory")
_AtmIfVpcNrpProvTable_Object = MibTable
atmIfVpcNrpProvTable = _AtmIfVpcNrpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 4, 100)
)
if mibBuilder.loadTexts:
    atmIfVpcNrpProvTable.setStatus("mandatory")
_AtmIfVpcNrpProvEntry_Object = MibTableRow
atmIfVpcNrpProvEntry = _AtmIfVpcNrpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 4, 100, 1)
)
atmIfVpcNrpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVpcIndex"),
    (0, "Nortel-Magellan-Passport-AtmBearerServiceMIB", "atmIfVpcNrpIndex"),
)
if mibBuilder.loadTexts:
    atmIfVpcNrpProvEntry.setStatus("mandatory")
_AtmIfVpcNrpNextHop_Type = Link
_AtmIfVpcNrpNextHop_Object = MibTableColumn
atmIfVpcNrpNextHop = _AtmIfVpcNrpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 4, 100, 1, 10),
    _AtmIfVpcNrpNextHop_Type()
)
atmIfVpcNrpNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVpcNrpNextHop.setStatus("mandatory")


class _AtmIfVpcNrpConnectionPointType_Type(Integer32):
    """Custom type atmIfVpcNrpConnectionPointType based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("autoConfigure", 4),
          ("connectingPoint", 2),
          ("segmentEndPoint", 1))
    )


_AtmIfVpcNrpConnectionPointType_Type.__name__ = "Integer32"
_AtmIfVpcNrpConnectionPointType_Object = MibTableColumn
atmIfVpcNrpConnectionPointType = _AtmIfVpcNrpConnectionPointType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 4, 100, 1, 20),
    _AtmIfVpcNrpConnectionPointType_Type()
)
atmIfVpcNrpConnectionPointType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVpcNrpConnectionPointType.setStatus("obsolete")


class _AtmIfVpcNrpOamSegmentBoundary_Type(Integer32):
    """Custom type atmIfVpcNrpOamSegmentBoundary based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("sameAsInterface", 2),
          ("yes", 1))
    )


_AtmIfVpcNrpOamSegmentBoundary_Type.__name__ = "Integer32"
_AtmIfVpcNrpOamSegmentBoundary_Object = MibTableColumn
atmIfVpcNrpOamSegmentBoundary = _AtmIfVpcNrpOamSegmentBoundary_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 4, 100, 1, 30),
    _AtmIfVpcNrpOamSegmentBoundary_Type()
)
atmIfVpcNrpOamSegmentBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVpcNrpOamSegmentBoundary.setStatus("mandatory")


class _AtmIfVpcNrpTxAal5PartialPacketDiscard_Type(Integer32):
    """Custom type atmIfVpcNrpTxAal5PartialPacketDiscard based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AtmIfVpcNrpTxAal5PartialPacketDiscard_Type.__name__ = "Integer32"
_AtmIfVpcNrpTxAal5PartialPacketDiscard_Object = MibTableColumn
atmIfVpcNrpTxAal5PartialPacketDiscard = _AtmIfVpcNrpTxAal5PartialPacketDiscard_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 4, 100, 1, 31),
    _AtmIfVpcNrpTxAal5PartialPacketDiscard_Type()
)
atmIfVpcNrpTxAal5PartialPacketDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVpcNrpTxAal5PartialPacketDiscard.setStatus("obsolete")


class _AtmIfVpcNrpRxAal5PartialPacketDiscard_Type(Integer32):
    """Custom type atmIfVpcNrpRxAal5PartialPacketDiscard based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("sameAsTx", 2))
    )


_AtmIfVpcNrpRxAal5PartialPacketDiscard_Type.__name__ = "Integer32"
_AtmIfVpcNrpRxAal5PartialPacketDiscard_Object = MibTableColumn
atmIfVpcNrpRxAal5PartialPacketDiscard = _AtmIfVpcNrpRxAal5PartialPacketDiscard_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 4, 100, 1, 32),
    _AtmIfVpcNrpRxAal5PartialPacketDiscard_Type()
)
atmIfVpcNrpRxAal5PartialPacketDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVpcNrpRxAal5PartialPacketDiscard.setStatus("obsolete")


class _AtmIfVpcNrpBandwidthElastic_Type(Integer32):
    """Custom type atmIfVpcNrpBandwidthElastic based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AtmIfVpcNrpBandwidthElastic_Type.__name__ = "Integer32"
_AtmIfVpcNrpBandwidthElastic_Object = MibTableColumn
atmIfVpcNrpBandwidthElastic = _AtmIfVpcNrpBandwidthElastic_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 4, 100, 1, 33),
    _AtmIfVpcNrpBandwidthElastic_Type()
)
atmIfVpcNrpBandwidthElastic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVpcNrpBandwidthElastic.setStatus("mandatory")


class _AtmIfVpcNrpOverrideHoldingPriority_Type(Integer32):
    """Custom type atmIfVpcNrpOverrideHoldingPriority based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4),
          ("noOverride", 6))
    )


_AtmIfVpcNrpOverrideHoldingPriority_Type.__name__ = "Integer32"
_AtmIfVpcNrpOverrideHoldingPriority_Object = MibTableColumn
atmIfVpcNrpOverrideHoldingPriority = _AtmIfVpcNrpOverrideHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 4, 4, 100, 1, 34),
    _AtmIfVpcNrpOverrideHoldingPriority_Type()
)
atmIfVpcNrpOverrideHoldingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVpcNrpOverrideHoldingPriority.setStatus("mandatory")
_AtmIfVccNrp_ObjectIdentity = ObjectIdentity
atmIfVccNrp = _AtmIfVccNrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 4)
)
_AtmIfVccNrpRowStatusTable_Object = MibTable
atmIfVccNrpRowStatusTable = _AtmIfVccNrpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 4, 1)
)
if mibBuilder.loadTexts:
    atmIfVccNrpRowStatusTable.setStatus("mandatory")
_AtmIfVccNrpRowStatusEntry_Object = MibTableRow
atmIfVccNrpRowStatusEntry = _AtmIfVccNrpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 4, 1, 1)
)
atmIfVccNrpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVccIndex"),
    (0, "Nortel-Magellan-Passport-AtmBearerServiceMIB", "atmIfVccNrpIndex"),
)
if mibBuilder.loadTexts:
    atmIfVccNrpRowStatusEntry.setStatus("mandatory")
_AtmIfVccNrpRowStatus_Type = RowStatus
_AtmIfVccNrpRowStatus_Object = MibTableColumn
atmIfVccNrpRowStatus = _AtmIfVccNrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 4, 1, 1, 1),
    _AtmIfVccNrpRowStatus_Type()
)
atmIfVccNrpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVccNrpRowStatus.setStatus("mandatory")
_AtmIfVccNrpComponentName_Type = DisplayString
_AtmIfVccNrpComponentName_Object = MibTableColumn
atmIfVccNrpComponentName = _AtmIfVccNrpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 4, 1, 1, 2),
    _AtmIfVccNrpComponentName_Type()
)
atmIfVccNrpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVccNrpComponentName.setStatus("mandatory")
_AtmIfVccNrpStorageType_Type = StorageType
_AtmIfVccNrpStorageType_Object = MibTableColumn
atmIfVccNrpStorageType = _AtmIfVccNrpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 4, 1, 1, 4),
    _AtmIfVccNrpStorageType_Type()
)
atmIfVccNrpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVccNrpStorageType.setStatus("mandatory")
_AtmIfVccNrpIndex_Type = NonReplicated
_AtmIfVccNrpIndex_Object = MibTableColumn
atmIfVccNrpIndex = _AtmIfVccNrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 4, 1, 1, 10),
    _AtmIfVccNrpIndex_Type()
)
atmIfVccNrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVccNrpIndex.setStatus("mandatory")
_AtmIfVccNrpProvTable_Object = MibTable
atmIfVccNrpProvTable = _AtmIfVccNrpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 4, 100)
)
if mibBuilder.loadTexts:
    atmIfVccNrpProvTable.setStatus("mandatory")
_AtmIfVccNrpProvEntry_Object = MibTableRow
atmIfVccNrpProvEntry = _AtmIfVccNrpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 4, 100, 1)
)
atmIfVccNrpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVccIndex"),
    (0, "Nortel-Magellan-Passport-AtmBearerServiceMIB", "atmIfVccNrpIndex"),
)
if mibBuilder.loadTexts:
    atmIfVccNrpProvEntry.setStatus("mandatory")
_AtmIfVccNrpNextHop_Type = Link
_AtmIfVccNrpNextHop_Object = MibTableColumn
atmIfVccNrpNextHop = _AtmIfVccNrpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 4, 100, 1, 10),
    _AtmIfVccNrpNextHop_Type()
)
atmIfVccNrpNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVccNrpNextHop.setStatus("mandatory")


class _AtmIfVccNrpConnectionPointType_Type(Integer32):
    """Custom type atmIfVccNrpConnectionPointType based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("autoConfigure", 4),
          ("connectingPoint", 2),
          ("segmentEndPoint", 1))
    )


_AtmIfVccNrpConnectionPointType_Type.__name__ = "Integer32"
_AtmIfVccNrpConnectionPointType_Object = MibTableColumn
atmIfVccNrpConnectionPointType = _AtmIfVccNrpConnectionPointType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 4, 100, 1, 20),
    _AtmIfVccNrpConnectionPointType_Type()
)
atmIfVccNrpConnectionPointType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVccNrpConnectionPointType.setStatus("obsolete")


class _AtmIfVccNrpOamSegmentBoundary_Type(Integer32):
    """Custom type atmIfVccNrpOamSegmentBoundary based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("sameAsInterface", 2),
          ("yes", 1))
    )


_AtmIfVccNrpOamSegmentBoundary_Type.__name__ = "Integer32"
_AtmIfVccNrpOamSegmentBoundary_Object = MibTableColumn
atmIfVccNrpOamSegmentBoundary = _AtmIfVccNrpOamSegmentBoundary_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 4, 100, 1, 30),
    _AtmIfVccNrpOamSegmentBoundary_Type()
)
atmIfVccNrpOamSegmentBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVccNrpOamSegmentBoundary.setStatus("mandatory")


class _AtmIfVccNrpTxAal5PartialPacketDiscard_Type(Integer32):
    """Custom type atmIfVccNrpTxAal5PartialPacketDiscard based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AtmIfVccNrpTxAal5PartialPacketDiscard_Type.__name__ = "Integer32"
_AtmIfVccNrpTxAal5PartialPacketDiscard_Object = MibTableColumn
atmIfVccNrpTxAal5PartialPacketDiscard = _AtmIfVccNrpTxAal5PartialPacketDiscard_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 4, 100, 1, 31),
    _AtmIfVccNrpTxAal5PartialPacketDiscard_Type()
)
atmIfVccNrpTxAal5PartialPacketDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVccNrpTxAal5PartialPacketDiscard.setStatus("obsolete")


class _AtmIfVccNrpRxAal5PartialPacketDiscard_Type(Integer32):
    """Custom type atmIfVccNrpRxAal5PartialPacketDiscard based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("sameAsTx", 2))
    )


_AtmIfVccNrpRxAal5PartialPacketDiscard_Type.__name__ = "Integer32"
_AtmIfVccNrpRxAal5PartialPacketDiscard_Object = MibTableColumn
atmIfVccNrpRxAal5PartialPacketDiscard = _AtmIfVccNrpRxAal5PartialPacketDiscard_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 4, 100, 1, 32),
    _AtmIfVccNrpRxAal5PartialPacketDiscard_Type()
)
atmIfVccNrpRxAal5PartialPacketDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVccNrpRxAal5PartialPacketDiscard.setStatus("obsolete")


class _AtmIfVccNrpBandwidthElastic_Type(Integer32):
    """Custom type atmIfVccNrpBandwidthElastic based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AtmIfVccNrpBandwidthElastic_Type.__name__ = "Integer32"
_AtmIfVccNrpBandwidthElastic_Object = MibTableColumn
atmIfVccNrpBandwidthElastic = _AtmIfVccNrpBandwidthElastic_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 4, 100, 1, 33),
    _AtmIfVccNrpBandwidthElastic_Type()
)
atmIfVccNrpBandwidthElastic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVccNrpBandwidthElastic.setStatus("mandatory")


class _AtmIfVccNrpOverrideHoldingPriority_Type(Integer32):
    """Custom type atmIfVccNrpOverrideHoldingPriority based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4),
          ("noOverride", 6))
    )


_AtmIfVccNrpOverrideHoldingPriority_Type.__name__ = "Integer32"
_AtmIfVccNrpOverrideHoldingPriority_Object = MibTableColumn
atmIfVccNrpOverrideHoldingPriority = _AtmIfVccNrpOverrideHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 5, 4, 100, 1, 34),
    _AtmIfVccNrpOverrideHoldingPriority_Type()
)
atmIfVccNrpOverrideHoldingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVccNrpOverrideHoldingPriority.setStatus("mandatory")
_AtmIfVptVccNrp_ObjectIdentity = ObjectIdentity
atmIfVptVccNrp = _AtmIfVptVccNrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 4)
)
_AtmIfVptVccNrpRowStatusTable_Object = MibTable
atmIfVptVccNrpRowStatusTable = _AtmIfVptVccNrpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 4, 1)
)
if mibBuilder.loadTexts:
    atmIfVptVccNrpRowStatusTable.setStatus("mandatory")
_AtmIfVptVccNrpRowStatusEntry_Object = MibTableRow
atmIfVptVccNrpRowStatusEntry = _AtmIfVptVccNrpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 4, 1, 1)
)
atmIfVptVccNrpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptVccIndex"),
    (0, "Nortel-Magellan-Passport-AtmBearerServiceMIB", "atmIfVptVccNrpIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptVccNrpRowStatusEntry.setStatus("mandatory")
_AtmIfVptVccNrpRowStatus_Type = RowStatus
_AtmIfVptVccNrpRowStatus_Object = MibTableColumn
atmIfVptVccNrpRowStatus = _AtmIfVptVccNrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 4, 1, 1, 1),
    _AtmIfVptVccNrpRowStatus_Type()
)
atmIfVptVccNrpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptVccNrpRowStatus.setStatus("mandatory")
_AtmIfVptVccNrpComponentName_Type = DisplayString
_AtmIfVptVccNrpComponentName_Object = MibTableColumn
atmIfVptVccNrpComponentName = _AtmIfVptVccNrpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 4, 1, 1, 2),
    _AtmIfVptVccNrpComponentName_Type()
)
atmIfVptVccNrpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptVccNrpComponentName.setStatus("mandatory")
_AtmIfVptVccNrpStorageType_Type = StorageType
_AtmIfVptVccNrpStorageType_Object = MibTableColumn
atmIfVptVccNrpStorageType = _AtmIfVptVccNrpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 4, 1, 1, 4),
    _AtmIfVptVccNrpStorageType_Type()
)
atmIfVptVccNrpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfVptVccNrpStorageType.setStatus("mandatory")
_AtmIfVptVccNrpIndex_Type = NonReplicated
_AtmIfVptVccNrpIndex_Object = MibTableColumn
atmIfVptVccNrpIndex = _AtmIfVptVccNrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 4, 1, 1, 10),
    _AtmIfVptVccNrpIndex_Type()
)
atmIfVptVccNrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfVptVccNrpIndex.setStatus("mandatory")
_AtmIfVptVccNrpProvTable_Object = MibTable
atmIfVptVccNrpProvTable = _AtmIfVptVccNrpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 4, 100)
)
if mibBuilder.loadTexts:
    atmIfVptVccNrpProvTable.setStatus("mandatory")
_AtmIfVptVccNrpProvEntry_Object = MibTableRow
atmIfVptVccNrpProvEntry = _AtmIfVptVccNrpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 4, 100, 1)
)
atmIfVptVccNrpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptIndex"),
    (0, "Nortel-Magellan-Passport-AtmCoreMIB", "atmIfVptVccIndex"),
    (0, "Nortel-Magellan-Passport-AtmBearerServiceMIB", "atmIfVptVccNrpIndex"),
)
if mibBuilder.loadTexts:
    atmIfVptVccNrpProvEntry.setStatus("mandatory")
_AtmIfVptVccNrpNextHop_Type = Link
_AtmIfVptVccNrpNextHop_Object = MibTableColumn
atmIfVptVccNrpNextHop = _AtmIfVptVccNrpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 4, 100, 1, 10),
    _AtmIfVptVccNrpNextHop_Type()
)
atmIfVptVccNrpNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptVccNrpNextHop.setStatus("mandatory")


class _AtmIfVptVccNrpConnectionPointType_Type(Integer32):
    """Custom type atmIfVptVccNrpConnectionPointType based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("autoConfigure", 4),
          ("connectingPoint", 2),
          ("segmentEndPoint", 1))
    )


_AtmIfVptVccNrpConnectionPointType_Type.__name__ = "Integer32"
_AtmIfVptVccNrpConnectionPointType_Object = MibTableColumn
atmIfVptVccNrpConnectionPointType = _AtmIfVptVccNrpConnectionPointType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 4, 100, 1, 20),
    _AtmIfVptVccNrpConnectionPointType_Type()
)
atmIfVptVccNrpConnectionPointType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptVccNrpConnectionPointType.setStatus("obsolete")


class _AtmIfVptVccNrpOamSegmentBoundary_Type(Integer32):
    """Custom type atmIfVptVccNrpOamSegmentBoundary based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("sameAsInterface", 2),
          ("yes", 1))
    )


_AtmIfVptVccNrpOamSegmentBoundary_Type.__name__ = "Integer32"
_AtmIfVptVccNrpOamSegmentBoundary_Object = MibTableColumn
atmIfVptVccNrpOamSegmentBoundary = _AtmIfVptVccNrpOamSegmentBoundary_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 4, 100, 1, 30),
    _AtmIfVptVccNrpOamSegmentBoundary_Type()
)
atmIfVptVccNrpOamSegmentBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptVccNrpOamSegmentBoundary.setStatus("mandatory")


class _AtmIfVptVccNrpTxAal5PartialPacketDiscard_Type(Integer32):
    """Custom type atmIfVptVccNrpTxAal5PartialPacketDiscard based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AtmIfVptVccNrpTxAal5PartialPacketDiscard_Type.__name__ = "Integer32"
_AtmIfVptVccNrpTxAal5PartialPacketDiscard_Object = MibTableColumn
atmIfVptVccNrpTxAal5PartialPacketDiscard = _AtmIfVptVccNrpTxAal5PartialPacketDiscard_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 4, 100, 1, 31),
    _AtmIfVptVccNrpTxAal5PartialPacketDiscard_Type()
)
atmIfVptVccNrpTxAal5PartialPacketDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptVccNrpTxAal5PartialPacketDiscard.setStatus("obsolete")


class _AtmIfVptVccNrpRxAal5PartialPacketDiscard_Type(Integer32):
    """Custom type atmIfVptVccNrpRxAal5PartialPacketDiscard based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("sameAsTx", 2))
    )


_AtmIfVptVccNrpRxAal5PartialPacketDiscard_Type.__name__ = "Integer32"
_AtmIfVptVccNrpRxAal5PartialPacketDiscard_Object = MibTableColumn
atmIfVptVccNrpRxAal5PartialPacketDiscard = _AtmIfVptVccNrpRxAal5PartialPacketDiscard_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 4, 100, 1, 32),
    _AtmIfVptVccNrpRxAal5PartialPacketDiscard_Type()
)
atmIfVptVccNrpRxAal5PartialPacketDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptVccNrpRxAal5PartialPacketDiscard.setStatus("obsolete")


class _AtmIfVptVccNrpBandwidthElastic_Type(Integer32):
    """Custom type atmIfVptVccNrpBandwidthElastic based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AtmIfVptVccNrpBandwidthElastic_Type.__name__ = "Integer32"
_AtmIfVptVccNrpBandwidthElastic_Object = MibTableColumn
atmIfVptVccNrpBandwidthElastic = _AtmIfVptVccNrpBandwidthElastic_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 4, 100, 1, 33),
    _AtmIfVptVccNrpBandwidthElastic_Type()
)
atmIfVptVccNrpBandwidthElastic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptVccNrpBandwidthElastic.setStatus("mandatory")


class _AtmIfVptVccNrpOverrideHoldingPriority_Type(Integer32):
    """Custom type atmIfVptVccNrpOverrideHoldingPriority based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("n0", 0),
          ("n1", 1),
          ("n2", 2),
          ("n3", 3),
          ("n4", 4),
          ("noOverride", 6))
    )


_AtmIfVptVccNrpOverrideHoldingPriority_Type.__name__ = "Integer32"
_AtmIfVptVccNrpOverrideHoldingPriority_Object = MibTableColumn
atmIfVptVccNrpOverrideHoldingPriority = _AtmIfVptVccNrpOverrideHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 114, 9, 20, 4, 100, 1, 34),
    _AtmIfVptVccNrpOverrideHoldingPriority_Type()
)
atmIfVptVccNrpOverrideHoldingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIfVptVccNrpOverrideHoldingPriority.setStatus("mandatory")
_AtmBearerServiceMIB_ObjectIdentity = ObjectIdentity
atmBearerServiceMIB = _AtmBearerServiceMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 64)
)
_AtmBearerServiceGroup_ObjectIdentity = ObjectIdentity
atmBearerServiceGroup = _AtmBearerServiceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 64, 1)
)
_AtmBearerServiceGroupBE_ObjectIdentity = ObjectIdentity
atmBearerServiceGroupBE = _AtmBearerServiceGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 64, 1, 5)
)
_AtmBearerServiceGroupBE00_ObjectIdentity = ObjectIdentity
atmBearerServiceGroupBE00 = _AtmBearerServiceGroupBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 64, 1, 5, 1)
)
_AtmBearerServiceGroupBE00A_ObjectIdentity = ObjectIdentity
atmBearerServiceGroupBE00A = _AtmBearerServiceGroupBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 64, 1, 5, 1, 2)
)
_AtmBearerServiceCapabilities_ObjectIdentity = ObjectIdentity
atmBearerServiceCapabilities = _AtmBearerServiceCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 64, 3)
)
_AtmBearerServiceCapabilitiesBE_ObjectIdentity = ObjectIdentity
atmBearerServiceCapabilitiesBE = _AtmBearerServiceCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 64, 3, 5)
)
_AtmBearerServiceCapabilitiesBE00_ObjectIdentity = ObjectIdentity
atmBearerServiceCapabilitiesBE00 = _AtmBearerServiceCapabilitiesBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 64, 3, 5, 1)
)
_AtmBearerServiceCapabilitiesBE00A_ObjectIdentity = ObjectIdentity
atmBearerServiceCapabilitiesBE00A = _AtmBearerServiceCapabilitiesBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 64, 3, 5, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-AtmBearerServiceMIB",
    **{"atmIfVpcNrp": atmIfVpcNrp,
       "atmIfVpcNrpRowStatusTable": atmIfVpcNrpRowStatusTable,
       "atmIfVpcNrpRowStatusEntry": atmIfVpcNrpRowStatusEntry,
       "atmIfVpcNrpRowStatus": atmIfVpcNrpRowStatus,
       "atmIfVpcNrpComponentName": atmIfVpcNrpComponentName,
       "atmIfVpcNrpStorageType": atmIfVpcNrpStorageType,
       "atmIfVpcNrpIndex": atmIfVpcNrpIndex,
       "atmIfVpcNrpProvTable": atmIfVpcNrpProvTable,
       "atmIfVpcNrpProvEntry": atmIfVpcNrpProvEntry,
       "atmIfVpcNrpNextHop": atmIfVpcNrpNextHop,
       "atmIfVpcNrpConnectionPointType": atmIfVpcNrpConnectionPointType,
       "atmIfVpcNrpOamSegmentBoundary": atmIfVpcNrpOamSegmentBoundary,
       "atmIfVpcNrpTxAal5PartialPacketDiscard": atmIfVpcNrpTxAal5PartialPacketDiscard,
       "atmIfVpcNrpRxAal5PartialPacketDiscard": atmIfVpcNrpRxAal5PartialPacketDiscard,
       "atmIfVpcNrpBandwidthElastic": atmIfVpcNrpBandwidthElastic,
       "atmIfVpcNrpOverrideHoldingPriority": atmIfVpcNrpOverrideHoldingPriority,
       "atmIfVccNrp": atmIfVccNrp,
       "atmIfVccNrpRowStatusTable": atmIfVccNrpRowStatusTable,
       "atmIfVccNrpRowStatusEntry": atmIfVccNrpRowStatusEntry,
       "atmIfVccNrpRowStatus": atmIfVccNrpRowStatus,
       "atmIfVccNrpComponentName": atmIfVccNrpComponentName,
       "atmIfVccNrpStorageType": atmIfVccNrpStorageType,
       "atmIfVccNrpIndex": atmIfVccNrpIndex,
       "atmIfVccNrpProvTable": atmIfVccNrpProvTable,
       "atmIfVccNrpProvEntry": atmIfVccNrpProvEntry,
       "atmIfVccNrpNextHop": atmIfVccNrpNextHop,
       "atmIfVccNrpConnectionPointType": atmIfVccNrpConnectionPointType,
       "atmIfVccNrpOamSegmentBoundary": atmIfVccNrpOamSegmentBoundary,
       "atmIfVccNrpTxAal5PartialPacketDiscard": atmIfVccNrpTxAal5PartialPacketDiscard,
       "atmIfVccNrpRxAal5PartialPacketDiscard": atmIfVccNrpRxAal5PartialPacketDiscard,
       "atmIfVccNrpBandwidthElastic": atmIfVccNrpBandwidthElastic,
       "atmIfVccNrpOverrideHoldingPriority": atmIfVccNrpOverrideHoldingPriority,
       "atmIfVptVccNrp": atmIfVptVccNrp,
       "atmIfVptVccNrpRowStatusTable": atmIfVptVccNrpRowStatusTable,
       "atmIfVptVccNrpRowStatusEntry": atmIfVptVccNrpRowStatusEntry,
       "atmIfVptVccNrpRowStatus": atmIfVptVccNrpRowStatus,
       "atmIfVptVccNrpComponentName": atmIfVptVccNrpComponentName,
       "atmIfVptVccNrpStorageType": atmIfVptVccNrpStorageType,
       "atmIfVptVccNrpIndex": atmIfVptVccNrpIndex,
       "atmIfVptVccNrpProvTable": atmIfVptVccNrpProvTable,
       "atmIfVptVccNrpProvEntry": atmIfVptVccNrpProvEntry,
       "atmIfVptVccNrpNextHop": atmIfVptVccNrpNextHop,
       "atmIfVptVccNrpConnectionPointType": atmIfVptVccNrpConnectionPointType,
       "atmIfVptVccNrpOamSegmentBoundary": atmIfVptVccNrpOamSegmentBoundary,
       "atmIfVptVccNrpTxAal5PartialPacketDiscard": atmIfVptVccNrpTxAal5PartialPacketDiscard,
       "atmIfVptVccNrpRxAal5PartialPacketDiscard": atmIfVptVccNrpRxAal5PartialPacketDiscard,
       "atmIfVptVccNrpBandwidthElastic": atmIfVptVccNrpBandwidthElastic,
       "atmIfVptVccNrpOverrideHoldingPriority": atmIfVptVccNrpOverrideHoldingPriority,
       "atmBearerServiceMIB": atmBearerServiceMIB,
       "atmBearerServiceGroup": atmBearerServiceGroup,
       "atmBearerServiceGroupBE": atmBearerServiceGroupBE,
       "atmBearerServiceGroupBE00": atmBearerServiceGroupBE00,
       "atmBearerServiceGroupBE00A": atmBearerServiceGroupBE00A,
       "atmBearerServiceCapabilities": atmBearerServiceCapabilities,
       "atmBearerServiceCapabilitiesBE": atmBearerServiceCapabilitiesBE,
       "atmBearerServiceCapabilitiesBE00": atmBearerServiceCapabilitiesBE00,
       "atmBearerServiceCapabilitiesBE00A": atmBearerServiceCapabilitiesBE00A}
)
