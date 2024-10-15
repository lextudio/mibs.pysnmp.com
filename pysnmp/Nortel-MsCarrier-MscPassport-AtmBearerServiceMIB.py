# SNMP MIB module (Nortel-MsCarrier-MscPassport-AtmBearerServiceMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-AtmBearerServiceMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:48 2024
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

(mscAtmIfIndex,
 mscAtmIfVcc,
 mscAtmIfVccIndex,
 mscAtmIfVpc,
 mscAtmIfVpcIndex,
 mscAtmIfVptIndex,
 mscAtmIfVptVcc,
 mscAtmIfVptVccIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-AtmCoreMIB",
    "mscAtmIfIndex",
    "mscAtmIfVcc",
    "mscAtmIfVccIndex",
    "mscAtmIfVpc",
    "mscAtmIfVpcIndex",
    "mscAtmIfVptIndex",
    "mscAtmIfVptVcc",
    "mscAtmIfVptVccIndex")

(DisplayString,
 RowStatus,
 StorageType) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "DisplayString",
    "RowStatus",
    "StorageType")

(Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "Link",
    "NonReplicated")

(mscPassportMIBs,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscPassportMIBs")

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

_MscAtmIfVpcNrp_ObjectIdentity = ObjectIdentity
mscAtmIfVpcNrp = _MscAtmIfVpcNrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 4)
)
_MscAtmIfVpcNrpRowStatusTable_Object = MibTable
mscAtmIfVpcNrpRowStatusTable = _MscAtmIfVpcNrpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 4, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVpcNrpRowStatusTable.setStatus("mandatory")
_MscAtmIfVpcNrpRowStatusEntry_Object = MibTableRow
mscAtmIfVpcNrpRowStatusEntry = _MscAtmIfVpcNrpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 4, 1, 1)
)
mscAtmIfVpcNrpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVpcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBearerServiceMIB", "mscAtmIfVpcNrpIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVpcNrpRowStatusEntry.setStatus("mandatory")
_MscAtmIfVpcNrpRowStatus_Type = RowStatus
_MscAtmIfVpcNrpRowStatus_Object = MibTableColumn
mscAtmIfVpcNrpRowStatus = _MscAtmIfVpcNrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 4, 1, 1, 1),
    _MscAtmIfVpcNrpRowStatus_Type()
)
mscAtmIfVpcNrpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVpcNrpRowStatus.setStatus("mandatory")
_MscAtmIfVpcNrpComponentName_Type = DisplayString
_MscAtmIfVpcNrpComponentName_Object = MibTableColumn
mscAtmIfVpcNrpComponentName = _MscAtmIfVpcNrpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 4, 1, 1, 2),
    _MscAtmIfVpcNrpComponentName_Type()
)
mscAtmIfVpcNrpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcNrpComponentName.setStatus("mandatory")
_MscAtmIfVpcNrpStorageType_Type = StorageType
_MscAtmIfVpcNrpStorageType_Object = MibTableColumn
mscAtmIfVpcNrpStorageType = _MscAtmIfVpcNrpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 4, 1, 1, 4),
    _MscAtmIfVpcNrpStorageType_Type()
)
mscAtmIfVpcNrpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcNrpStorageType.setStatus("mandatory")
_MscAtmIfVpcNrpIndex_Type = NonReplicated
_MscAtmIfVpcNrpIndex_Object = MibTableColumn
mscAtmIfVpcNrpIndex = _MscAtmIfVpcNrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 4, 1, 1, 10),
    _MscAtmIfVpcNrpIndex_Type()
)
mscAtmIfVpcNrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVpcNrpIndex.setStatus("mandatory")
_MscAtmIfVpcNrpProvTable_Object = MibTable
mscAtmIfVpcNrpProvTable = _MscAtmIfVpcNrpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 4, 100)
)
if mibBuilder.loadTexts:
    mscAtmIfVpcNrpProvTable.setStatus("mandatory")
_MscAtmIfVpcNrpProvEntry_Object = MibTableRow
mscAtmIfVpcNrpProvEntry = _MscAtmIfVpcNrpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 4, 100, 1)
)
mscAtmIfVpcNrpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVpcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBearerServiceMIB", "mscAtmIfVpcNrpIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVpcNrpProvEntry.setStatus("mandatory")
_MscAtmIfVpcNrpNextHop_Type = Link
_MscAtmIfVpcNrpNextHop_Object = MibTableColumn
mscAtmIfVpcNrpNextHop = _MscAtmIfVpcNrpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 4, 100, 1, 10),
    _MscAtmIfVpcNrpNextHop_Type()
)
mscAtmIfVpcNrpNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVpcNrpNextHop.setStatus("mandatory")


class _MscAtmIfVpcNrpConnectionPointType_Type(Integer32):
    """Custom type mscAtmIfVpcNrpConnectionPointType based on Integer32"""
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


_MscAtmIfVpcNrpConnectionPointType_Type.__name__ = "Integer32"
_MscAtmIfVpcNrpConnectionPointType_Object = MibTableColumn
mscAtmIfVpcNrpConnectionPointType = _MscAtmIfVpcNrpConnectionPointType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 4, 100, 1, 20),
    _MscAtmIfVpcNrpConnectionPointType_Type()
)
mscAtmIfVpcNrpConnectionPointType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVpcNrpConnectionPointType.setStatus("obsolete")


class _MscAtmIfVpcNrpOamSegmentBoundary_Type(Integer32):
    """Custom type mscAtmIfVpcNrpOamSegmentBoundary based on Integer32"""
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


_MscAtmIfVpcNrpOamSegmentBoundary_Type.__name__ = "Integer32"
_MscAtmIfVpcNrpOamSegmentBoundary_Object = MibTableColumn
mscAtmIfVpcNrpOamSegmentBoundary = _MscAtmIfVpcNrpOamSegmentBoundary_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 4, 100, 1, 30),
    _MscAtmIfVpcNrpOamSegmentBoundary_Type()
)
mscAtmIfVpcNrpOamSegmentBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVpcNrpOamSegmentBoundary.setStatus("mandatory")


class _MscAtmIfVpcNrpTxAal5PartialPacketDiscard_Type(Integer32):
    """Custom type mscAtmIfVpcNrpTxAal5PartialPacketDiscard based on Integer32"""
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


_MscAtmIfVpcNrpTxAal5PartialPacketDiscard_Type.__name__ = "Integer32"
_MscAtmIfVpcNrpTxAal5PartialPacketDiscard_Object = MibTableColumn
mscAtmIfVpcNrpTxAal5PartialPacketDiscard = _MscAtmIfVpcNrpTxAal5PartialPacketDiscard_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 4, 100, 1, 31),
    _MscAtmIfVpcNrpTxAal5PartialPacketDiscard_Type()
)
mscAtmIfVpcNrpTxAal5PartialPacketDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVpcNrpTxAal5PartialPacketDiscard.setStatus("obsolete")


class _MscAtmIfVpcNrpRxAal5PartialPacketDiscard_Type(Integer32):
    """Custom type mscAtmIfVpcNrpRxAal5PartialPacketDiscard based on Integer32"""
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


_MscAtmIfVpcNrpRxAal5PartialPacketDiscard_Type.__name__ = "Integer32"
_MscAtmIfVpcNrpRxAal5PartialPacketDiscard_Object = MibTableColumn
mscAtmIfVpcNrpRxAal5PartialPacketDiscard = _MscAtmIfVpcNrpRxAal5PartialPacketDiscard_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 4, 100, 1, 32),
    _MscAtmIfVpcNrpRxAal5PartialPacketDiscard_Type()
)
mscAtmIfVpcNrpRxAal5PartialPacketDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVpcNrpRxAal5PartialPacketDiscard.setStatus("obsolete")


class _MscAtmIfVpcNrpBandwidthElastic_Type(Integer32):
    """Custom type mscAtmIfVpcNrpBandwidthElastic based on Integer32"""
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


_MscAtmIfVpcNrpBandwidthElastic_Type.__name__ = "Integer32"
_MscAtmIfVpcNrpBandwidthElastic_Object = MibTableColumn
mscAtmIfVpcNrpBandwidthElastic = _MscAtmIfVpcNrpBandwidthElastic_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 4, 100, 1, 33),
    _MscAtmIfVpcNrpBandwidthElastic_Type()
)
mscAtmIfVpcNrpBandwidthElastic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVpcNrpBandwidthElastic.setStatus("mandatory")


class _MscAtmIfVpcNrpOverrideHoldingPriority_Type(Integer32):
    """Custom type mscAtmIfVpcNrpOverrideHoldingPriority based on Integer32"""
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


_MscAtmIfVpcNrpOverrideHoldingPriority_Type.__name__ = "Integer32"
_MscAtmIfVpcNrpOverrideHoldingPriority_Object = MibTableColumn
mscAtmIfVpcNrpOverrideHoldingPriority = _MscAtmIfVpcNrpOverrideHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 4, 100, 1, 34),
    _MscAtmIfVpcNrpOverrideHoldingPriority_Type()
)
mscAtmIfVpcNrpOverrideHoldingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVpcNrpOverrideHoldingPriority.setStatus("mandatory")
_MscAtmIfVpcMnrp_ObjectIdentity = ObjectIdentity
mscAtmIfVpcMnrp = _MscAtmIfVpcMnrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 12)
)
_MscAtmIfVpcMnrpRowStatusTable_Object = MibTable
mscAtmIfVpcMnrpRowStatusTable = _MscAtmIfVpcMnrpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 12, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVpcMnrpRowStatusTable.setStatus("mandatory")
_MscAtmIfVpcMnrpRowStatusEntry_Object = MibTableRow
mscAtmIfVpcMnrpRowStatusEntry = _MscAtmIfVpcMnrpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 12, 1, 1)
)
mscAtmIfVpcMnrpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVpcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBearerServiceMIB", "mscAtmIfVpcMnrpIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVpcMnrpRowStatusEntry.setStatus("mandatory")
_MscAtmIfVpcMnrpRowStatus_Type = RowStatus
_MscAtmIfVpcMnrpRowStatus_Object = MibTableColumn
mscAtmIfVpcMnrpRowStatus = _MscAtmIfVpcMnrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 12, 1, 1, 1),
    _MscAtmIfVpcMnrpRowStatus_Type()
)
mscAtmIfVpcMnrpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVpcMnrpRowStatus.setStatus("mandatory")
_MscAtmIfVpcMnrpComponentName_Type = DisplayString
_MscAtmIfVpcMnrpComponentName_Object = MibTableColumn
mscAtmIfVpcMnrpComponentName = _MscAtmIfVpcMnrpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 12, 1, 1, 2),
    _MscAtmIfVpcMnrpComponentName_Type()
)
mscAtmIfVpcMnrpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcMnrpComponentName.setStatus("mandatory")
_MscAtmIfVpcMnrpStorageType_Type = StorageType
_MscAtmIfVpcMnrpStorageType_Object = MibTableColumn
mscAtmIfVpcMnrpStorageType = _MscAtmIfVpcMnrpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 12, 1, 1, 4),
    _MscAtmIfVpcMnrpStorageType_Type()
)
mscAtmIfVpcMnrpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcMnrpStorageType.setStatus("mandatory")
_MscAtmIfVpcMnrpIndex_Type = NonReplicated
_MscAtmIfVpcMnrpIndex_Object = MibTableColumn
mscAtmIfVpcMnrpIndex = _MscAtmIfVpcMnrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 12, 1, 1, 10),
    _MscAtmIfVpcMnrpIndex_Type()
)
mscAtmIfVpcMnrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVpcMnrpIndex.setStatus("mandatory")
_MscAtmIfVpcMnrpProvTable_Object = MibTable
mscAtmIfVpcMnrpProvTable = _MscAtmIfVpcMnrpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 12, 101)
)
if mibBuilder.loadTexts:
    mscAtmIfVpcMnrpProvTable.setStatus("mandatory")
_MscAtmIfVpcMnrpProvEntry_Object = MibTableRow
mscAtmIfVpcMnrpProvEntry = _MscAtmIfVpcMnrpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 12, 101, 1)
)
mscAtmIfVpcMnrpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVpcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBearerServiceMIB", "mscAtmIfVpcMnrpIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVpcMnrpProvEntry.setStatus("mandatory")


class _MscAtmIfVpcMnrpOamSegmentBoundary_Type(Integer32):
    """Custom type mscAtmIfVpcMnrpOamSegmentBoundary based on Integer32"""
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


_MscAtmIfVpcMnrpOamSegmentBoundary_Type.__name__ = "Integer32"
_MscAtmIfVpcMnrpOamSegmentBoundary_Object = MibTableColumn
mscAtmIfVpcMnrpOamSegmentBoundary = _MscAtmIfVpcMnrpOamSegmentBoundary_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 12, 101, 1, 30),
    _MscAtmIfVpcMnrpOamSegmentBoundary_Type()
)
mscAtmIfVpcMnrpOamSegmentBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVpcMnrpOamSegmentBoundary.setStatus("mandatory")


class _MscAtmIfVpcMnrpBandwidthElastic_Type(Integer32):
    """Custom type mscAtmIfVpcMnrpBandwidthElastic based on Integer32"""
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


_MscAtmIfVpcMnrpBandwidthElastic_Type.__name__ = "Integer32"
_MscAtmIfVpcMnrpBandwidthElastic_Object = MibTableColumn
mscAtmIfVpcMnrpBandwidthElastic = _MscAtmIfVpcMnrpBandwidthElastic_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 12, 101, 1, 33),
    _MscAtmIfVpcMnrpBandwidthElastic_Type()
)
mscAtmIfVpcMnrpBandwidthElastic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVpcMnrpBandwidthElastic.setStatus("mandatory")


class _MscAtmIfVpcMnrpOverrideHoldingPriority_Type(Integer32):
    """Custom type mscAtmIfVpcMnrpOverrideHoldingPriority based on Integer32"""
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


_MscAtmIfVpcMnrpOverrideHoldingPriority_Type.__name__ = "Integer32"
_MscAtmIfVpcMnrpOverrideHoldingPriority_Object = MibTableColumn
mscAtmIfVpcMnrpOverrideHoldingPriority = _MscAtmIfVpcMnrpOverrideHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 12, 101, 1, 34),
    _MscAtmIfVpcMnrpOverrideHoldingPriority_Type()
)
mscAtmIfVpcMnrpOverrideHoldingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVpcMnrpOverrideHoldingPriority.setStatus("mandatory")
_MscAtmIfVpcMnrpNextHopsTable_Object = MibTable
mscAtmIfVpcMnrpNextHopsTable = _MscAtmIfVpcMnrpNextHopsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 12, 658)
)
if mibBuilder.loadTexts:
    mscAtmIfVpcMnrpNextHopsTable.setStatus("mandatory")
_MscAtmIfVpcMnrpNextHopsEntry_Object = MibTableRow
mscAtmIfVpcMnrpNextHopsEntry = _MscAtmIfVpcMnrpNextHopsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 12, 658, 1)
)
mscAtmIfVpcMnrpNextHopsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVpcIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBearerServiceMIB", "mscAtmIfVpcMnrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBearerServiceMIB", "mscAtmIfVpcMnrpNextHopsValue"),
)
if mibBuilder.loadTexts:
    mscAtmIfVpcMnrpNextHopsEntry.setStatus("mandatory")
_MscAtmIfVpcMnrpNextHopsValue_Type = Link
_MscAtmIfVpcMnrpNextHopsValue_Object = MibTableColumn
mscAtmIfVpcMnrpNextHopsValue = _MscAtmIfVpcMnrpNextHopsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 12, 658, 1, 1),
    _MscAtmIfVpcMnrpNextHopsValue_Type()
)
mscAtmIfVpcMnrpNextHopsValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVpcMnrpNextHopsValue.setStatus("mandatory")
_MscAtmIfVpcMnrpNextHopsRowStatus_Type = RowStatus
_MscAtmIfVpcMnrpNextHopsRowStatus_Object = MibTableColumn
mscAtmIfVpcMnrpNextHopsRowStatus = _MscAtmIfVpcMnrpNextHopsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 4, 12, 658, 1, 2),
    _MscAtmIfVpcMnrpNextHopsRowStatus_Type()
)
mscAtmIfVpcMnrpNextHopsRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscAtmIfVpcMnrpNextHopsRowStatus.setStatus("mandatory")
_MscAtmIfVccNrp_ObjectIdentity = ObjectIdentity
mscAtmIfVccNrp = _MscAtmIfVccNrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 4)
)
_MscAtmIfVccNrpRowStatusTable_Object = MibTable
mscAtmIfVccNrpRowStatusTable = _MscAtmIfVccNrpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 4, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVccNrpRowStatusTable.setStatus("mandatory")
_MscAtmIfVccNrpRowStatusEntry_Object = MibTableRow
mscAtmIfVccNrpRowStatusEntry = _MscAtmIfVccNrpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 4, 1, 1)
)
mscAtmIfVccNrpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBearerServiceMIB", "mscAtmIfVccNrpIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVccNrpRowStatusEntry.setStatus("mandatory")
_MscAtmIfVccNrpRowStatus_Type = RowStatus
_MscAtmIfVccNrpRowStatus_Object = MibTableColumn
mscAtmIfVccNrpRowStatus = _MscAtmIfVccNrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 4, 1, 1, 1),
    _MscAtmIfVccNrpRowStatus_Type()
)
mscAtmIfVccNrpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVccNrpRowStatus.setStatus("mandatory")
_MscAtmIfVccNrpComponentName_Type = DisplayString
_MscAtmIfVccNrpComponentName_Object = MibTableColumn
mscAtmIfVccNrpComponentName = _MscAtmIfVccNrpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 4, 1, 1, 2),
    _MscAtmIfVccNrpComponentName_Type()
)
mscAtmIfVccNrpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccNrpComponentName.setStatus("mandatory")
_MscAtmIfVccNrpStorageType_Type = StorageType
_MscAtmIfVccNrpStorageType_Object = MibTableColumn
mscAtmIfVccNrpStorageType = _MscAtmIfVccNrpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 4, 1, 1, 4),
    _MscAtmIfVccNrpStorageType_Type()
)
mscAtmIfVccNrpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccNrpStorageType.setStatus("mandatory")
_MscAtmIfVccNrpIndex_Type = NonReplicated
_MscAtmIfVccNrpIndex_Object = MibTableColumn
mscAtmIfVccNrpIndex = _MscAtmIfVccNrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 4, 1, 1, 10),
    _MscAtmIfVccNrpIndex_Type()
)
mscAtmIfVccNrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVccNrpIndex.setStatus("mandatory")
_MscAtmIfVccNrpProvTable_Object = MibTable
mscAtmIfVccNrpProvTable = _MscAtmIfVccNrpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 4, 100)
)
if mibBuilder.loadTexts:
    mscAtmIfVccNrpProvTable.setStatus("mandatory")
_MscAtmIfVccNrpProvEntry_Object = MibTableRow
mscAtmIfVccNrpProvEntry = _MscAtmIfVccNrpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 4, 100, 1)
)
mscAtmIfVccNrpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBearerServiceMIB", "mscAtmIfVccNrpIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVccNrpProvEntry.setStatus("mandatory")
_MscAtmIfVccNrpNextHop_Type = Link
_MscAtmIfVccNrpNextHop_Object = MibTableColumn
mscAtmIfVccNrpNextHop = _MscAtmIfVccNrpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 4, 100, 1, 10),
    _MscAtmIfVccNrpNextHop_Type()
)
mscAtmIfVccNrpNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVccNrpNextHop.setStatus("mandatory")


class _MscAtmIfVccNrpConnectionPointType_Type(Integer32):
    """Custom type mscAtmIfVccNrpConnectionPointType based on Integer32"""
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


_MscAtmIfVccNrpConnectionPointType_Type.__name__ = "Integer32"
_MscAtmIfVccNrpConnectionPointType_Object = MibTableColumn
mscAtmIfVccNrpConnectionPointType = _MscAtmIfVccNrpConnectionPointType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 4, 100, 1, 20),
    _MscAtmIfVccNrpConnectionPointType_Type()
)
mscAtmIfVccNrpConnectionPointType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVccNrpConnectionPointType.setStatus("obsolete")


class _MscAtmIfVccNrpOamSegmentBoundary_Type(Integer32):
    """Custom type mscAtmIfVccNrpOamSegmentBoundary based on Integer32"""
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


_MscAtmIfVccNrpOamSegmentBoundary_Type.__name__ = "Integer32"
_MscAtmIfVccNrpOamSegmentBoundary_Object = MibTableColumn
mscAtmIfVccNrpOamSegmentBoundary = _MscAtmIfVccNrpOamSegmentBoundary_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 4, 100, 1, 30),
    _MscAtmIfVccNrpOamSegmentBoundary_Type()
)
mscAtmIfVccNrpOamSegmentBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVccNrpOamSegmentBoundary.setStatus("mandatory")


class _MscAtmIfVccNrpTxAal5PartialPacketDiscard_Type(Integer32):
    """Custom type mscAtmIfVccNrpTxAal5PartialPacketDiscard based on Integer32"""
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


_MscAtmIfVccNrpTxAal5PartialPacketDiscard_Type.__name__ = "Integer32"
_MscAtmIfVccNrpTxAal5PartialPacketDiscard_Object = MibTableColumn
mscAtmIfVccNrpTxAal5PartialPacketDiscard = _MscAtmIfVccNrpTxAal5PartialPacketDiscard_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 4, 100, 1, 31),
    _MscAtmIfVccNrpTxAal5PartialPacketDiscard_Type()
)
mscAtmIfVccNrpTxAal5PartialPacketDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVccNrpTxAal5PartialPacketDiscard.setStatus("obsolete")


class _MscAtmIfVccNrpRxAal5PartialPacketDiscard_Type(Integer32):
    """Custom type mscAtmIfVccNrpRxAal5PartialPacketDiscard based on Integer32"""
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


_MscAtmIfVccNrpRxAal5PartialPacketDiscard_Type.__name__ = "Integer32"
_MscAtmIfVccNrpRxAal5PartialPacketDiscard_Object = MibTableColumn
mscAtmIfVccNrpRxAal5PartialPacketDiscard = _MscAtmIfVccNrpRxAal5PartialPacketDiscard_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 4, 100, 1, 32),
    _MscAtmIfVccNrpRxAal5PartialPacketDiscard_Type()
)
mscAtmIfVccNrpRxAal5PartialPacketDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVccNrpRxAal5PartialPacketDiscard.setStatus("obsolete")


class _MscAtmIfVccNrpBandwidthElastic_Type(Integer32):
    """Custom type mscAtmIfVccNrpBandwidthElastic based on Integer32"""
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


_MscAtmIfVccNrpBandwidthElastic_Type.__name__ = "Integer32"
_MscAtmIfVccNrpBandwidthElastic_Object = MibTableColumn
mscAtmIfVccNrpBandwidthElastic = _MscAtmIfVccNrpBandwidthElastic_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 4, 100, 1, 33),
    _MscAtmIfVccNrpBandwidthElastic_Type()
)
mscAtmIfVccNrpBandwidthElastic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVccNrpBandwidthElastic.setStatus("mandatory")


class _MscAtmIfVccNrpOverrideHoldingPriority_Type(Integer32):
    """Custom type mscAtmIfVccNrpOverrideHoldingPriority based on Integer32"""
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


_MscAtmIfVccNrpOverrideHoldingPriority_Type.__name__ = "Integer32"
_MscAtmIfVccNrpOverrideHoldingPriority_Object = MibTableColumn
mscAtmIfVccNrpOverrideHoldingPriority = _MscAtmIfVccNrpOverrideHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 4, 100, 1, 34),
    _MscAtmIfVccNrpOverrideHoldingPriority_Type()
)
mscAtmIfVccNrpOverrideHoldingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVccNrpOverrideHoldingPriority.setStatus("mandatory")
_MscAtmIfVccMnrp_ObjectIdentity = ObjectIdentity
mscAtmIfVccMnrp = _MscAtmIfVccMnrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 13)
)
_MscAtmIfVccMnrpRowStatusTable_Object = MibTable
mscAtmIfVccMnrpRowStatusTable = _MscAtmIfVccMnrpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 13, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVccMnrpRowStatusTable.setStatus("mandatory")
_MscAtmIfVccMnrpRowStatusEntry_Object = MibTableRow
mscAtmIfVccMnrpRowStatusEntry = _MscAtmIfVccMnrpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 13, 1, 1)
)
mscAtmIfVccMnrpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBearerServiceMIB", "mscAtmIfVccMnrpIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVccMnrpRowStatusEntry.setStatus("mandatory")
_MscAtmIfVccMnrpRowStatus_Type = RowStatus
_MscAtmIfVccMnrpRowStatus_Object = MibTableColumn
mscAtmIfVccMnrpRowStatus = _MscAtmIfVccMnrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 13, 1, 1, 1),
    _MscAtmIfVccMnrpRowStatus_Type()
)
mscAtmIfVccMnrpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVccMnrpRowStatus.setStatus("mandatory")
_MscAtmIfVccMnrpComponentName_Type = DisplayString
_MscAtmIfVccMnrpComponentName_Object = MibTableColumn
mscAtmIfVccMnrpComponentName = _MscAtmIfVccMnrpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 13, 1, 1, 2),
    _MscAtmIfVccMnrpComponentName_Type()
)
mscAtmIfVccMnrpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccMnrpComponentName.setStatus("mandatory")
_MscAtmIfVccMnrpStorageType_Type = StorageType
_MscAtmIfVccMnrpStorageType_Object = MibTableColumn
mscAtmIfVccMnrpStorageType = _MscAtmIfVccMnrpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 13, 1, 1, 4),
    _MscAtmIfVccMnrpStorageType_Type()
)
mscAtmIfVccMnrpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVccMnrpStorageType.setStatus("mandatory")
_MscAtmIfVccMnrpIndex_Type = NonReplicated
_MscAtmIfVccMnrpIndex_Object = MibTableColumn
mscAtmIfVccMnrpIndex = _MscAtmIfVccMnrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 13, 1, 1, 10),
    _MscAtmIfVccMnrpIndex_Type()
)
mscAtmIfVccMnrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVccMnrpIndex.setStatus("mandatory")
_MscAtmIfVccMnrpProvTable_Object = MibTable
mscAtmIfVccMnrpProvTable = _MscAtmIfVccMnrpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 13, 101)
)
if mibBuilder.loadTexts:
    mscAtmIfVccMnrpProvTable.setStatus("mandatory")
_MscAtmIfVccMnrpProvEntry_Object = MibTableRow
mscAtmIfVccMnrpProvEntry = _MscAtmIfVccMnrpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 13, 101, 1)
)
mscAtmIfVccMnrpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBearerServiceMIB", "mscAtmIfVccMnrpIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVccMnrpProvEntry.setStatus("mandatory")


class _MscAtmIfVccMnrpOamSegmentBoundary_Type(Integer32):
    """Custom type mscAtmIfVccMnrpOamSegmentBoundary based on Integer32"""
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


_MscAtmIfVccMnrpOamSegmentBoundary_Type.__name__ = "Integer32"
_MscAtmIfVccMnrpOamSegmentBoundary_Object = MibTableColumn
mscAtmIfVccMnrpOamSegmentBoundary = _MscAtmIfVccMnrpOamSegmentBoundary_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 13, 101, 1, 30),
    _MscAtmIfVccMnrpOamSegmentBoundary_Type()
)
mscAtmIfVccMnrpOamSegmentBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVccMnrpOamSegmentBoundary.setStatus("mandatory")


class _MscAtmIfVccMnrpBandwidthElastic_Type(Integer32):
    """Custom type mscAtmIfVccMnrpBandwidthElastic based on Integer32"""
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


_MscAtmIfVccMnrpBandwidthElastic_Type.__name__ = "Integer32"
_MscAtmIfVccMnrpBandwidthElastic_Object = MibTableColumn
mscAtmIfVccMnrpBandwidthElastic = _MscAtmIfVccMnrpBandwidthElastic_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 13, 101, 1, 33),
    _MscAtmIfVccMnrpBandwidthElastic_Type()
)
mscAtmIfVccMnrpBandwidthElastic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVccMnrpBandwidthElastic.setStatus("mandatory")


class _MscAtmIfVccMnrpOverrideHoldingPriority_Type(Integer32):
    """Custom type mscAtmIfVccMnrpOverrideHoldingPriority based on Integer32"""
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


_MscAtmIfVccMnrpOverrideHoldingPriority_Type.__name__ = "Integer32"
_MscAtmIfVccMnrpOverrideHoldingPriority_Object = MibTableColumn
mscAtmIfVccMnrpOverrideHoldingPriority = _MscAtmIfVccMnrpOverrideHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 13, 101, 1, 34),
    _MscAtmIfVccMnrpOverrideHoldingPriority_Type()
)
mscAtmIfVccMnrpOverrideHoldingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVccMnrpOverrideHoldingPriority.setStatus("mandatory")
_MscAtmIfVccMnrpNextHopsTable_Object = MibTable
mscAtmIfVccMnrpNextHopsTable = _MscAtmIfVccMnrpNextHopsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 13, 658)
)
if mibBuilder.loadTexts:
    mscAtmIfVccMnrpNextHopsTable.setStatus("mandatory")
_MscAtmIfVccMnrpNextHopsEntry_Object = MibTableRow
mscAtmIfVccMnrpNextHopsEntry = _MscAtmIfVccMnrpNextHopsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 13, 658, 1)
)
mscAtmIfVccMnrpNextHopsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBearerServiceMIB", "mscAtmIfVccMnrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBearerServiceMIB", "mscAtmIfVccMnrpNextHopsValue"),
)
if mibBuilder.loadTexts:
    mscAtmIfVccMnrpNextHopsEntry.setStatus("mandatory")
_MscAtmIfVccMnrpNextHopsValue_Type = Link
_MscAtmIfVccMnrpNextHopsValue_Object = MibTableColumn
mscAtmIfVccMnrpNextHopsValue = _MscAtmIfVccMnrpNextHopsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 13, 658, 1, 1),
    _MscAtmIfVccMnrpNextHopsValue_Type()
)
mscAtmIfVccMnrpNextHopsValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVccMnrpNextHopsValue.setStatus("mandatory")
_MscAtmIfVccMnrpNextHopsRowStatus_Type = RowStatus
_MscAtmIfVccMnrpNextHopsRowStatus_Object = MibTableColumn
mscAtmIfVccMnrpNextHopsRowStatus = _MscAtmIfVccMnrpNextHopsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 5, 13, 658, 1, 2),
    _MscAtmIfVccMnrpNextHopsRowStatus_Type()
)
mscAtmIfVccMnrpNextHopsRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscAtmIfVccMnrpNextHopsRowStatus.setStatus("mandatory")
_MscAtmIfVptVccNrp_ObjectIdentity = ObjectIdentity
mscAtmIfVptVccNrp = _MscAtmIfVptVccNrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 4)
)
_MscAtmIfVptVccNrpRowStatusTable_Object = MibTable
mscAtmIfVptVccNrpRowStatusTable = _MscAtmIfVptVccNrpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 4, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccNrpRowStatusTable.setStatus("mandatory")
_MscAtmIfVptVccNrpRowStatusEntry_Object = MibTableRow
mscAtmIfVptVccNrpRowStatusEntry = _MscAtmIfVptVccNrpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 4, 1, 1)
)
mscAtmIfVptVccNrpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBearerServiceMIB", "mscAtmIfVptVccNrpIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccNrpRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptVccNrpRowStatus_Type = RowStatus
_MscAtmIfVptVccNrpRowStatus_Object = MibTableColumn
mscAtmIfVptVccNrpRowStatus = _MscAtmIfVptVccNrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 4, 1, 1, 1),
    _MscAtmIfVptVccNrpRowStatus_Type()
)
mscAtmIfVptVccNrpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptVccNrpRowStatus.setStatus("mandatory")
_MscAtmIfVptVccNrpComponentName_Type = DisplayString
_MscAtmIfVptVccNrpComponentName_Object = MibTableColumn
mscAtmIfVptVccNrpComponentName = _MscAtmIfVptVccNrpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 4, 1, 1, 2),
    _MscAtmIfVptVccNrpComponentName_Type()
)
mscAtmIfVptVccNrpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccNrpComponentName.setStatus("mandatory")
_MscAtmIfVptVccNrpStorageType_Type = StorageType
_MscAtmIfVptVccNrpStorageType_Object = MibTableColumn
mscAtmIfVptVccNrpStorageType = _MscAtmIfVptVccNrpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 4, 1, 1, 4),
    _MscAtmIfVptVccNrpStorageType_Type()
)
mscAtmIfVptVccNrpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccNrpStorageType.setStatus("mandatory")
_MscAtmIfVptVccNrpIndex_Type = NonReplicated
_MscAtmIfVptVccNrpIndex_Object = MibTableColumn
mscAtmIfVptVccNrpIndex = _MscAtmIfVptVccNrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 4, 1, 1, 10),
    _MscAtmIfVptVccNrpIndex_Type()
)
mscAtmIfVptVccNrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptVccNrpIndex.setStatus("mandatory")
_MscAtmIfVptVccNrpProvTable_Object = MibTable
mscAtmIfVptVccNrpProvTable = _MscAtmIfVptVccNrpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 4, 100)
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccNrpProvTable.setStatus("mandatory")
_MscAtmIfVptVccNrpProvEntry_Object = MibTableRow
mscAtmIfVptVccNrpProvEntry = _MscAtmIfVptVccNrpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 4, 100, 1)
)
mscAtmIfVptVccNrpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBearerServiceMIB", "mscAtmIfVptVccNrpIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccNrpProvEntry.setStatus("mandatory")
_MscAtmIfVptVccNrpNextHop_Type = Link
_MscAtmIfVptVccNrpNextHop_Object = MibTableColumn
mscAtmIfVptVccNrpNextHop = _MscAtmIfVptVccNrpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 4, 100, 1, 10),
    _MscAtmIfVptVccNrpNextHop_Type()
)
mscAtmIfVptVccNrpNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptVccNrpNextHop.setStatus("mandatory")


class _MscAtmIfVptVccNrpConnectionPointType_Type(Integer32):
    """Custom type mscAtmIfVptVccNrpConnectionPointType based on Integer32"""
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


_MscAtmIfVptVccNrpConnectionPointType_Type.__name__ = "Integer32"
_MscAtmIfVptVccNrpConnectionPointType_Object = MibTableColumn
mscAtmIfVptVccNrpConnectionPointType = _MscAtmIfVptVccNrpConnectionPointType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 4, 100, 1, 20),
    _MscAtmIfVptVccNrpConnectionPointType_Type()
)
mscAtmIfVptVccNrpConnectionPointType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptVccNrpConnectionPointType.setStatus("obsolete")


class _MscAtmIfVptVccNrpOamSegmentBoundary_Type(Integer32):
    """Custom type mscAtmIfVptVccNrpOamSegmentBoundary based on Integer32"""
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


_MscAtmIfVptVccNrpOamSegmentBoundary_Type.__name__ = "Integer32"
_MscAtmIfVptVccNrpOamSegmentBoundary_Object = MibTableColumn
mscAtmIfVptVccNrpOamSegmentBoundary = _MscAtmIfVptVccNrpOamSegmentBoundary_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 4, 100, 1, 30),
    _MscAtmIfVptVccNrpOamSegmentBoundary_Type()
)
mscAtmIfVptVccNrpOamSegmentBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptVccNrpOamSegmentBoundary.setStatus("mandatory")


class _MscAtmIfVptVccNrpTxAal5PartialPacketDiscard_Type(Integer32):
    """Custom type mscAtmIfVptVccNrpTxAal5PartialPacketDiscard based on Integer32"""
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


_MscAtmIfVptVccNrpTxAal5PartialPacketDiscard_Type.__name__ = "Integer32"
_MscAtmIfVptVccNrpTxAal5PartialPacketDiscard_Object = MibTableColumn
mscAtmIfVptVccNrpTxAal5PartialPacketDiscard = _MscAtmIfVptVccNrpTxAal5PartialPacketDiscard_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 4, 100, 1, 31),
    _MscAtmIfVptVccNrpTxAal5PartialPacketDiscard_Type()
)
mscAtmIfVptVccNrpTxAal5PartialPacketDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptVccNrpTxAal5PartialPacketDiscard.setStatus("obsolete")


class _MscAtmIfVptVccNrpRxAal5PartialPacketDiscard_Type(Integer32):
    """Custom type mscAtmIfVptVccNrpRxAal5PartialPacketDiscard based on Integer32"""
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


_MscAtmIfVptVccNrpRxAal5PartialPacketDiscard_Type.__name__ = "Integer32"
_MscAtmIfVptVccNrpRxAal5PartialPacketDiscard_Object = MibTableColumn
mscAtmIfVptVccNrpRxAal5PartialPacketDiscard = _MscAtmIfVptVccNrpRxAal5PartialPacketDiscard_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 4, 100, 1, 32),
    _MscAtmIfVptVccNrpRxAal5PartialPacketDiscard_Type()
)
mscAtmIfVptVccNrpRxAal5PartialPacketDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptVccNrpRxAal5PartialPacketDiscard.setStatus("obsolete")


class _MscAtmIfVptVccNrpBandwidthElastic_Type(Integer32):
    """Custom type mscAtmIfVptVccNrpBandwidthElastic based on Integer32"""
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


_MscAtmIfVptVccNrpBandwidthElastic_Type.__name__ = "Integer32"
_MscAtmIfVptVccNrpBandwidthElastic_Object = MibTableColumn
mscAtmIfVptVccNrpBandwidthElastic = _MscAtmIfVptVccNrpBandwidthElastic_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 4, 100, 1, 33),
    _MscAtmIfVptVccNrpBandwidthElastic_Type()
)
mscAtmIfVptVccNrpBandwidthElastic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptVccNrpBandwidthElastic.setStatus("mandatory")


class _MscAtmIfVptVccNrpOverrideHoldingPriority_Type(Integer32):
    """Custom type mscAtmIfVptVccNrpOverrideHoldingPriority based on Integer32"""
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


_MscAtmIfVptVccNrpOverrideHoldingPriority_Type.__name__ = "Integer32"
_MscAtmIfVptVccNrpOverrideHoldingPriority_Object = MibTableColumn
mscAtmIfVptVccNrpOverrideHoldingPriority = _MscAtmIfVptVccNrpOverrideHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 4, 100, 1, 34),
    _MscAtmIfVptVccNrpOverrideHoldingPriority_Type()
)
mscAtmIfVptVccNrpOverrideHoldingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptVccNrpOverrideHoldingPriority.setStatus("mandatory")
_MscAtmIfVptVccMnrp_ObjectIdentity = ObjectIdentity
mscAtmIfVptVccMnrp = _MscAtmIfVptVccMnrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 13)
)
_MscAtmIfVptVccMnrpRowStatusTable_Object = MibTable
mscAtmIfVptVccMnrpRowStatusTable = _MscAtmIfVptVccMnrpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 13, 1)
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccMnrpRowStatusTable.setStatus("mandatory")
_MscAtmIfVptVccMnrpRowStatusEntry_Object = MibTableRow
mscAtmIfVptVccMnrpRowStatusEntry = _MscAtmIfVptVccMnrpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 13, 1, 1)
)
mscAtmIfVptVccMnrpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBearerServiceMIB", "mscAtmIfVptVccMnrpIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccMnrpRowStatusEntry.setStatus("mandatory")
_MscAtmIfVptVccMnrpRowStatus_Type = RowStatus
_MscAtmIfVptVccMnrpRowStatus_Object = MibTableColumn
mscAtmIfVptVccMnrpRowStatus = _MscAtmIfVptVccMnrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 13, 1, 1, 1),
    _MscAtmIfVptVccMnrpRowStatus_Type()
)
mscAtmIfVptVccMnrpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptVccMnrpRowStatus.setStatus("mandatory")
_MscAtmIfVptVccMnrpComponentName_Type = DisplayString
_MscAtmIfVptVccMnrpComponentName_Object = MibTableColumn
mscAtmIfVptVccMnrpComponentName = _MscAtmIfVptVccMnrpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 13, 1, 1, 2),
    _MscAtmIfVptVccMnrpComponentName_Type()
)
mscAtmIfVptVccMnrpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccMnrpComponentName.setStatus("mandatory")
_MscAtmIfVptVccMnrpStorageType_Type = StorageType
_MscAtmIfVptVccMnrpStorageType_Object = MibTableColumn
mscAtmIfVptVccMnrpStorageType = _MscAtmIfVptVccMnrpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 13, 1, 1, 4),
    _MscAtmIfVptVccMnrpStorageType_Type()
)
mscAtmIfVptVccMnrpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccMnrpStorageType.setStatus("mandatory")
_MscAtmIfVptVccMnrpIndex_Type = NonReplicated
_MscAtmIfVptVccMnrpIndex_Object = MibTableColumn
mscAtmIfVptVccMnrpIndex = _MscAtmIfVptVccMnrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 13, 1, 1, 10),
    _MscAtmIfVptVccMnrpIndex_Type()
)
mscAtmIfVptVccMnrpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscAtmIfVptVccMnrpIndex.setStatus("mandatory")
_MscAtmIfVptVccMnrpProvTable_Object = MibTable
mscAtmIfVptVccMnrpProvTable = _MscAtmIfVptVccMnrpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 13, 101)
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccMnrpProvTable.setStatus("mandatory")
_MscAtmIfVptVccMnrpProvEntry_Object = MibTableRow
mscAtmIfVptVccMnrpProvEntry = _MscAtmIfVptVccMnrpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 13, 101, 1)
)
mscAtmIfVptVccMnrpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBearerServiceMIB", "mscAtmIfVptVccMnrpIndex"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccMnrpProvEntry.setStatus("mandatory")


class _MscAtmIfVptVccMnrpOamSegmentBoundary_Type(Integer32):
    """Custom type mscAtmIfVptVccMnrpOamSegmentBoundary based on Integer32"""
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


_MscAtmIfVptVccMnrpOamSegmentBoundary_Type.__name__ = "Integer32"
_MscAtmIfVptVccMnrpOamSegmentBoundary_Object = MibTableColumn
mscAtmIfVptVccMnrpOamSegmentBoundary = _MscAtmIfVptVccMnrpOamSegmentBoundary_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 13, 101, 1, 30),
    _MscAtmIfVptVccMnrpOamSegmentBoundary_Type()
)
mscAtmIfVptVccMnrpOamSegmentBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptVccMnrpOamSegmentBoundary.setStatus("mandatory")


class _MscAtmIfVptVccMnrpBandwidthElastic_Type(Integer32):
    """Custom type mscAtmIfVptVccMnrpBandwidthElastic based on Integer32"""
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


_MscAtmIfVptVccMnrpBandwidthElastic_Type.__name__ = "Integer32"
_MscAtmIfVptVccMnrpBandwidthElastic_Object = MibTableColumn
mscAtmIfVptVccMnrpBandwidthElastic = _MscAtmIfVptVccMnrpBandwidthElastic_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 13, 101, 1, 33),
    _MscAtmIfVptVccMnrpBandwidthElastic_Type()
)
mscAtmIfVptVccMnrpBandwidthElastic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptVccMnrpBandwidthElastic.setStatus("mandatory")


class _MscAtmIfVptVccMnrpOverrideHoldingPriority_Type(Integer32):
    """Custom type mscAtmIfVptVccMnrpOverrideHoldingPriority based on Integer32"""
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


_MscAtmIfVptVccMnrpOverrideHoldingPriority_Type.__name__ = "Integer32"
_MscAtmIfVptVccMnrpOverrideHoldingPriority_Object = MibTableColumn
mscAtmIfVptVccMnrpOverrideHoldingPriority = _MscAtmIfVptVccMnrpOverrideHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 13, 101, 1, 34),
    _MscAtmIfVptVccMnrpOverrideHoldingPriority_Type()
)
mscAtmIfVptVccMnrpOverrideHoldingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptVccMnrpOverrideHoldingPriority.setStatus("mandatory")
_MscAtmIfVptVccMnrpNextHopsTable_Object = MibTable
mscAtmIfVptVccMnrpNextHopsTable = _MscAtmIfVptVccMnrpNextHopsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 13, 658)
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccMnrpNextHopsTable.setStatus("mandatory")
_MscAtmIfVptVccMnrpNextHopsEntry_Object = MibTableRow
mscAtmIfVptVccMnrpNextHopsEntry = _MscAtmIfVptVccMnrpNextHopsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 13, 658, 1)
)
mscAtmIfVptVccMnrpNextHopsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmCoreMIB", "mscAtmIfVptVccIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBearerServiceMIB", "mscAtmIfVptVccMnrpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-AtmBearerServiceMIB", "mscAtmIfVptVccMnrpNextHopsValue"),
)
if mibBuilder.loadTexts:
    mscAtmIfVptVccMnrpNextHopsEntry.setStatus("mandatory")
_MscAtmIfVptVccMnrpNextHopsValue_Type = Link
_MscAtmIfVptVccMnrpNextHopsValue_Object = MibTableColumn
mscAtmIfVptVccMnrpNextHopsValue = _MscAtmIfVptVccMnrpNextHopsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 13, 658, 1, 1),
    _MscAtmIfVptVccMnrpNextHopsValue_Type()
)
mscAtmIfVptVccMnrpNextHopsValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscAtmIfVptVccMnrpNextHopsValue.setStatus("mandatory")
_MscAtmIfVptVccMnrpNextHopsRowStatus_Type = RowStatus
_MscAtmIfVptVccMnrpNextHopsRowStatus_Object = MibTableColumn
mscAtmIfVptVccMnrpNextHopsRowStatus = _MscAtmIfVptVccMnrpNextHopsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 114, 9, 20, 13, 658, 1, 2),
    _MscAtmIfVptVccMnrpNextHopsRowStatus_Type()
)
mscAtmIfVptVccMnrpNextHopsRowStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mscAtmIfVptVccMnrpNextHopsRowStatus.setStatus("mandatory")
_AtmBearerServiceMIB_ObjectIdentity = ObjectIdentity
atmBearerServiceMIB = _AtmBearerServiceMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 64)
)
_AtmBearerServiceGroup_ObjectIdentity = ObjectIdentity
atmBearerServiceGroup = _AtmBearerServiceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 64, 1)
)
_AtmBearerServiceGroupCA_ObjectIdentity = ObjectIdentity
atmBearerServiceGroupCA = _AtmBearerServiceGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 64, 1, 1)
)
_AtmBearerServiceGroupCA02_ObjectIdentity = ObjectIdentity
atmBearerServiceGroupCA02 = _AtmBearerServiceGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 64, 1, 1, 3)
)
_AtmBearerServiceGroupCA02A_ObjectIdentity = ObjectIdentity
atmBearerServiceGroupCA02A = _AtmBearerServiceGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 64, 1, 1, 3, 2)
)
_AtmBearerServiceCapabilities_ObjectIdentity = ObjectIdentity
atmBearerServiceCapabilities = _AtmBearerServiceCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 64, 3)
)
_AtmBearerServiceCapabilitiesCA_ObjectIdentity = ObjectIdentity
atmBearerServiceCapabilitiesCA = _AtmBearerServiceCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 64, 3, 1)
)
_AtmBearerServiceCapabilitiesCA02_ObjectIdentity = ObjectIdentity
atmBearerServiceCapabilitiesCA02 = _AtmBearerServiceCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 64, 3, 1, 3)
)
_AtmBearerServiceCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
atmBearerServiceCapabilitiesCA02A = _AtmBearerServiceCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 64, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-AtmBearerServiceMIB",
    **{"mscAtmIfVpcNrp": mscAtmIfVpcNrp,
       "mscAtmIfVpcNrpRowStatusTable": mscAtmIfVpcNrpRowStatusTable,
       "mscAtmIfVpcNrpRowStatusEntry": mscAtmIfVpcNrpRowStatusEntry,
       "mscAtmIfVpcNrpRowStatus": mscAtmIfVpcNrpRowStatus,
       "mscAtmIfVpcNrpComponentName": mscAtmIfVpcNrpComponentName,
       "mscAtmIfVpcNrpStorageType": mscAtmIfVpcNrpStorageType,
       "mscAtmIfVpcNrpIndex": mscAtmIfVpcNrpIndex,
       "mscAtmIfVpcNrpProvTable": mscAtmIfVpcNrpProvTable,
       "mscAtmIfVpcNrpProvEntry": mscAtmIfVpcNrpProvEntry,
       "mscAtmIfVpcNrpNextHop": mscAtmIfVpcNrpNextHop,
       "mscAtmIfVpcNrpConnectionPointType": mscAtmIfVpcNrpConnectionPointType,
       "mscAtmIfVpcNrpOamSegmentBoundary": mscAtmIfVpcNrpOamSegmentBoundary,
       "mscAtmIfVpcNrpTxAal5PartialPacketDiscard": mscAtmIfVpcNrpTxAal5PartialPacketDiscard,
       "mscAtmIfVpcNrpRxAal5PartialPacketDiscard": mscAtmIfVpcNrpRxAal5PartialPacketDiscard,
       "mscAtmIfVpcNrpBandwidthElastic": mscAtmIfVpcNrpBandwidthElastic,
       "mscAtmIfVpcNrpOverrideHoldingPriority": mscAtmIfVpcNrpOverrideHoldingPriority,
       "mscAtmIfVpcMnrp": mscAtmIfVpcMnrp,
       "mscAtmIfVpcMnrpRowStatusTable": mscAtmIfVpcMnrpRowStatusTable,
       "mscAtmIfVpcMnrpRowStatusEntry": mscAtmIfVpcMnrpRowStatusEntry,
       "mscAtmIfVpcMnrpRowStatus": mscAtmIfVpcMnrpRowStatus,
       "mscAtmIfVpcMnrpComponentName": mscAtmIfVpcMnrpComponentName,
       "mscAtmIfVpcMnrpStorageType": mscAtmIfVpcMnrpStorageType,
       "mscAtmIfVpcMnrpIndex": mscAtmIfVpcMnrpIndex,
       "mscAtmIfVpcMnrpProvTable": mscAtmIfVpcMnrpProvTable,
       "mscAtmIfVpcMnrpProvEntry": mscAtmIfVpcMnrpProvEntry,
       "mscAtmIfVpcMnrpOamSegmentBoundary": mscAtmIfVpcMnrpOamSegmentBoundary,
       "mscAtmIfVpcMnrpBandwidthElastic": mscAtmIfVpcMnrpBandwidthElastic,
       "mscAtmIfVpcMnrpOverrideHoldingPriority": mscAtmIfVpcMnrpOverrideHoldingPriority,
       "mscAtmIfVpcMnrpNextHopsTable": mscAtmIfVpcMnrpNextHopsTable,
       "mscAtmIfVpcMnrpNextHopsEntry": mscAtmIfVpcMnrpNextHopsEntry,
       "mscAtmIfVpcMnrpNextHopsValue": mscAtmIfVpcMnrpNextHopsValue,
       "mscAtmIfVpcMnrpNextHopsRowStatus": mscAtmIfVpcMnrpNextHopsRowStatus,
       "mscAtmIfVccNrp": mscAtmIfVccNrp,
       "mscAtmIfVccNrpRowStatusTable": mscAtmIfVccNrpRowStatusTable,
       "mscAtmIfVccNrpRowStatusEntry": mscAtmIfVccNrpRowStatusEntry,
       "mscAtmIfVccNrpRowStatus": mscAtmIfVccNrpRowStatus,
       "mscAtmIfVccNrpComponentName": mscAtmIfVccNrpComponentName,
       "mscAtmIfVccNrpStorageType": mscAtmIfVccNrpStorageType,
       "mscAtmIfVccNrpIndex": mscAtmIfVccNrpIndex,
       "mscAtmIfVccNrpProvTable": mscAtmIfVccNrpProvTable,
       "mscAtmIfVccNrpProvEntry": mscAtmIfVccNrpProvEntry,
       "mscAtmIfVccNrpNextHop": mscAtmIfVccNrpNextHop,
       "mscAtmIfVccNrpConnectionPointType": mscAtmIfVccNrpConnectionPointType,
       "mscAtmIfVccNrpOamSegmentBoundary": mscAtmIfVccNrpOamSegmentBoundary,
       "mscAtmIfVccNrpTxAal5PartialPacketDiscard": mscAtmIfVccNrpTxAal5PartialPacketDiscard,
       "mscAtmIfVccNrpRxAal5PartialPacketDiscard": mscAtmIfVccNrpRxAal5PartialPacketDiscard,
       "mscAtmIfVccNrpBandwidthElastic": mscAtmIfVccNrpBandwidthElastic,
       "mscAtmIfVccNrpOverrideHoldingPriority": mscAtmIfVccNrpOverrideHoldingPriority,
       "mscAtmIfVccMnrp": mscAtmIfVccMnrp,
       "mscAtmIfVccMnrpRowStatusTable": mscAtmIfVccMnrpRowStatusTable,
       "mscAtmIfVccMnrpRowStatusEntry": mscAtmIfVccMnrpRowStatusEntry,
       "mscAtmIfVccMnrpRowStatus": mscAtmIfVccMnrpRowStatus,
       "mscAtmIfVccMnrpComponentName": mscAtmIfVccMnrpComponentName,
       "mscAtmIfVccMnrpStorageType": mscAtmIfVccMnrpStorageType,
       "mscAtmIfVccMnrpIndex": mscAtmIfVccMnrpIndex,
       "mscAtmIfVccMnrpProvTable": mscAtmIfVccMnrpProvTable,
       "mscAtmIfVccMnrpProvEntry": mscAtmIfVccMnrpProvEntry,
       "mscAtmIfVccMnrpOamSegmentBoundary": mscAtmIfVccMnrpOamSegmentBoundary,
       "mscAtmIfVccMnrpBandwidthElastic": mscAtmIfVccMnrpBandwidthElastic,
       "mscAtmIfVccMnrpOverrideHoldingPriority": mscAtmIfVccMnrpOverrideHoldingPriority,
       "mscAtmIfVccMnrpNextHopsTable": mscAtmIfVccMnrpNextHopsTable,
       "mscAtmIfVccMnrpNextHopsEntry": mscAtmIfVccMnrpNextHopsEntry,
       "mscAtmIfVccMnrpNextHopsValue": mscAtmIfVccMnrpNextHopsValue,
       "mscAtmIfVccMnrpNextHopsRowStatus": mscAtmIfVccMnrpNextHopsRowStatus,
       "mscAtmIfVptVccNrp": mscAtmIfVptVccNrp,
       "mscAtmIfVptVccNrpRowStatusTable": mscAtmIfVptVccNrpRowStatusTable,
       "mscAtmIfVptVccNrpRowStatusEntry": mscAtmIfVptVccNrpRowStatusEntry,
       "mscAtmIfVptVccNrpRowStatus": mscAtmIfVptVccNrpRowStatus,
       "mscAtmIfVptVccNrpComponentName": mscAtmIfVptVccNrpComponentName,
       "mscAtmIfVptVccNrpStorageType": mscAtmIfVptVccNrpStorageType,
       "mscAtmIfVptVccNrpIndex": mscAtmIfVptVccNrpIndex,
       "mscAtmIfVptVccNrpProvTable": mscAtmIfVptVccNrpProvTable,
       "mscAtmIfVptVccNrpProvEntry": mscAtmIfVptVccNrpProvEntry,
       "mscAtmIfVptVccNrpNextHop": mscAtmIfVptVccNrpNextHop,
       "mscAtmIfVptVccNrpConnectionPointType": mscAtmIfVptVccNrpConnectionPointType,
       "mscAtmIfVptVccNrpOamSegmentBoundary": mscAtmIfVptVccNrpOamSegmentBoundary,
       "mscAtmIfVptVccNrpTxAal5PartialPacketDiscard": mscAtmIfVptVccNrpTxAal5PartialPacketDiscard,
       "mscAtmIfVptVccNrpRxAal5PartialPacketDiscard": mscAtmIfVptVccNrpRxAal5PartialPacketDiscard,
       "mscAtmIfVptVccNrpBandwidthElastic": mscAtmIfVptVccNrpBandwidthElastic,
       "mscAtmIfVptVccNrpOverrideHoldingPriority": mscAtmIfVptVccNrpOverrideHoldingPriority,
       "mscAtmIfVptVccMnrp": mscAtmIfVptVccMnrp,
       "mscAtmIfVptVccMnrpRowStatusTable": mscAtmIfVptVccMnrpRowStatusTable,
       "mscAtmIfVptVccMnrpRowStatusEntry": mscAtmIfVptVccMnrpRowStatusEntry,
       "mscAtmIfVptVccMnrpRowStatus": mscAtmIfVptVccMnrpRowStatus,
       "mscAtmIfVptVccMnrpComponentName": mscAtmIfVptVccMnrpComponentName,
       "mscAtmIfVptVccMnrpStorageType": mscAtmIfVptVccMnrpStorageType,
       "mscAtmIfVptVccMnrpIndex": mscAtmIfVptVccMnrpIndex,
       "mscAtmIfVptVccMnrpProvTable": mscAtmIfVptVccMnrpProvTable,
       "mscAtmIfVptVccMnrpProvEntry": mscAtmIfVptVccMnrpProvEntry,
       "mscAtmIfVptVccMnrpOamSegmentBoundary": mscAtmIfVptVccMnrpOamSegmentBoundary,
       "mscAtmIfVptVccMnrpBandwidthElastic": mscAtmIfVptVccMnrpBandwidthElastic,
       "mscAtmIfVptVccMnrpOverrideHoldingPriority": mscAtmIfVptVccMnrpOverrideHoldingPriority,
       "mscAtmIfVptVccMnrpNextHopsTable": mscAtmIfVptVccMnrpNextHopsTable,
       "mscAtmIfVptVccMnrpNextHopsEntry": mscAtmIfVptVccMnrpNextHopsEntry,
       "mscAtmIfVptVccMnrpNextHopsValue": mscAtmIfVptVccMnrpNextHopsValue,
       "mscAtmIfVptVccMnrpNextHopsRowStatus": mscAtmIfVptVccMnrpNextHopsRowStatus,
       "atmBearerServiceMIB": atmBearerServiceMIB,
       "atmBearerServiceGroup": atmBearerServiceGroup,
       "atmBearerServiceGroupCA": atmBearerServiceGroupCA,
       "atmBearerServiceGroupCA02": atmBearerServiceGroupCA02,
       "atmBearerServiceGroupCA02A": atmBearerServiceGroupCA02A,
       "atmBearerServiceCapabilities": atmBearerServiceCapabilities,
       "atmBearerServiceCapabilitiesCA": atmBearerServiceCapabilitiesCA,
       "atmBearerServiceCapabilitiesCA02": atmBearerServiceCapabilitiesCA02,
       "atmBearerServiceCapabilitiesCA02A": atmBearerServiceCapabilitiesCA02A}
)
