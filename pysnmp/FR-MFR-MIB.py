# SNMP MIB module (FR-MFR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FR-MFR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:16 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 transmission) = mibBuilder.importSymbols(
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
    "transmission")

(DisplayString,
 RowStatus,
 TextualConvention,
 TestAndIncr) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr")


# MODULE-IDENTITY

mfrMib = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 47)
)
mfrMib.setRevisions(
        ("2000-11-30 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MfrBundleLinkState(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("mfrBundleLinkStateAddAckRx", 3),
          ("mfrBundleLinkStateAddRx", 2),
          ("mfrBundleLinkStateAddSent", 1),
          ("mfrBundleLinkStateDown", 7),
          ("mfrBundleLinkStateDownIdle", 8),
          ("mfrBundleLinkStateIdle", 6),
          ("mfrBundleLinkStateIdlePending", 5),
          ("mfrBundleLinkStateUp", 4))
    )



# MIB Managed Objects in the order of their OIDs

_MfrMibScalarObjects_ObjectIdentity = ObjectIdentity
mfrMibScalarObjects = _MfrMibScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 47, 1)
)
_MfrBundleMaxNumBundles_Type = Integer32
_MfrBundleMaxNumBundles_Object = MibScalar
mfrBundleMaxNumBundles = _MfrBundleMaxNumBundles_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 1, 1),
    _MfrBundleMaxNumBundles_Type()
)
mfrBundleMaxNumBundles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrBundleMaxNumBundles.setStatus("current")
_MfrBundleNextIndex_Type = TestAndIncr
_MfrBundleNextIndex_Object = MibScalar
mfrBundleNextIndex = _MfrBundleNextIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 1, 2),
    _MfrBundleNextIndex_Type()
)
mfrBundleNextIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrBundleNextIndex.setStatus("current")
_MfrMibBundleObjects_ObjectIdentity = ObjectIdentity
mfrMibBundleObjects = _MfrMibBundleObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 47, 2)
)
_MfrBundleTable_Object = MibTable
mfrBundleTable = _MfrBundleTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 2, 3)
)
if mibBuilder.loadTexts:
    mfrBundleTable.setStatus("current")
_MfrBundleEntry_Object = MibTableRow
mfrBundleEntry = _MfrBundleEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1)
)
mfrBundleEntry.setIndexNames(
    (0, "FR-MFR-MIB", "mfrBundleIndex"),
)
if mibBuilder.loadTexts:
    mfrBundleEntry.setStatus("current")


class _MfrBundleIndex_Type(Integer32):
    """Custom type mfrBundleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MfrBundleIndex_Type.__name__ = "Integer32"
_MfrBundleIndex_Object = MibTableColumn
mfrBundleIndex = _MfrBundleIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 1),
    _MfrBundleIndex_Type()
)
mfrBundleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mfrBundleIndex.setStatus("current")
_MfrBundleIfIndex_Type = InterfaceIndex
_MfrBundleIfIndex_Object = MibTableColumn
mfrBundleIfIndex = _MfrBundleIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 2),
    _MfrBundleIfIndex_Type()
)
mfrBundleIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrBundleIfIndex.setStatus("current")
_MfrBundleRowStatus_Type = RowStatus
_MfrBundleRowStatus_Object = MibTableColumn
mfrBundleRowStatus = _MfrBundleRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 3),
    _MfrBundleRowStatus_Type()
)
mfrBundleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mfrBundleRowStatus.setStatus("current")
_MfrBundleNearEndName_Type = SnmpAdminString
_MfrBundleNearEndName_Object = MibTableColumn
mfrBundleNearEndName = _MfrBundleNearEndName_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 4),
    _MfrBundleNearEndName_Type()
)
mfrBundleNearEndName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mfrBundleNearEndName.setStatus("current")


class _MfrBundleFragmentation_Type(Integer32):
    """Custom type mfrBundleFragmentation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MfrBundleFragmentation_Type.__name__ = "Integer32"
_MfrBundleFragmentation_Object = MibTableColumn
mfrBundleFragmentation = _MfrBundleFragmentation_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 5),
    _MfrBundleFragmentation_Type()
)
mfrBundleFragmentation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mfrBundleFragmentation.setStatus("current")


class _MfrBundleMaxFragSize_Type(Integer32):
    """Custom type mfrBundleMaxFragSize based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 8184),
    )


_MfrBundleMaxFragSize_Type.__name__ = "Integer32"
_MfrBundleMaxFragSize_Object = MibTableColumn
mfrBundleMaxFragSize = _MfrBundleMaxFragSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 6),
    _MfrBundleMaxFragSize_Type()
)
mfrBundleMaxFragSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mfrBundleMaxFragSize.setStatus("current")
if mibBuilder.loadTexts:
    mfrBundleMaxFragSize.setUnits("Octets")


class _MfrBundleTimerHello_Type(Integer32):
    """Custom type mfrBundleTimerHello based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_MfrBundleTimerHello_Type.__name__ = "Integer32"
_MfrBundleTimerHello_Object = MibTableColumn
mfrBundleTimerHello = _MfrBundleTimerHello_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 7),
    _MfrBundleTimerHello_Type()
)
mfrBundleTimerHello.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mfrBundleTimerHello.setStatus("current")
if mibBuilder.loadTexts:
    mfrBundleTimerHello.setUnits("Seconds")


class _MfrBundleTimerAck_Type(Integer32):
    """Custom type mfrBundleTimerAck based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MfrBundleTimerAck_Type.__name__ = "Integer32"
_MfrBundleTimerAck_Object = MibTableColumn
mfrBundleTimerAck = _MfrBundleTimerAck_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 8),
    _MfrBundleTimerAck_Type()
)
mfrBundleTimerAck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mfrBundleTimerAck.setStatus("current")
if mibBuilder.loadTexts:
    mfrBundleTimerAck.setUnits("Seconds")


class _MfrBundleCountMaxRetry_Type(Integer32):
    """Custom type mfrBundleCountMaxRetry based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MfrBundleCountMaxRetry_Type.__name__ = "Integer32"
_MfrBundleCountMaxRetry_Object = MibTableColumn
mfrBundleCountMaxRetry = _MfrBundleCountMaxRetry_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 9),
    _MfrBundleCountMaxRetry_Type()
)
mfrBundleCountMaxRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mfrBundleCountMaxRetry.setStatus("current")


class _MfrBundleActivationClass_Type(Integer32):
    """Custom type mfrBundleActivationClass based on Integer32"""
    defaultValue = 1

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
        *(("mfrBundleActivationClassA", 1),
          ("mfrBundleActivationClassB", 2),
          ("mfrBundleActivationClassC", 3),
          ("mfrBundleActivationClassD", 4))
    )


_MfrBundleActivationClass_Type.__name__ = "Integer32"
_MfrBundleActivationClass_Object = MibTableColumn
mfrBundleActivationClass = _MfrBundleActivationClass_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 10),
    _MfrBundleActivationClass_Type()
)
mfrBundleActivationClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mfrBundleActivationClass.setStatus("current")


class _MfrBundleThreshold_Type(Integer32):
    """Custom type mfrBundleThreshold based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_MfrBundleThreshold_Type.__name__ = "Integer32"
_MfrBundleThreshold_Object = MibTableColumn
mfrBundleThreshold = _MfrBundleThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 11),
    _MfrBundleThreshold_Type()
)
mfrBundleThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mfrBundleThreshold.setStatus("current")
if mibBuilder.loadTexts:
    mfrBundleThreshold.setUnits("Bundle Links")


class _MfrBundleMaxDiffDelay_Type(Integer32):
    """Custom type mfrBundleMaxDiffDelay based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_MfrBundleMaxDiffDelay_Type.__name__ = "Integer32"
_MfrBundleMaxDiffDelay_Object = MibTableColumn
mfrBundleMaxDiffDelay = _MfrBundleMaxDiffDelay_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 12),
    _MfrBundleMaxDiffDelay_Type()
)
mfrBundleMaxDiffDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mfrBundleMaxDiffDelay.setStatus("current")
if mibBuilder.loadTexts:
    mfrBundleMaxDiffDelay.setUnits("Milliseconds")


class _MfrBundleSeqNumSize_Type(Integer32):
    """Custom type mfrBundleSeqNumSize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("seqNumSize12bit", 1),
          ("seqNumSize24bit", 2))
    )


_MfrBundleSeqNumSize_Type.__name__ = "Integer32"
_MfrBundleSeqNumSize_Object = MibTableColumn
mfrBundleSeqNumSize = _MfrBundleSeqNumSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 13),
    _MfrBundleSeqNumSize_Type()
)
mfrBundleSeqNumSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mfrBundleSeqNumSize.setStatus("current")


class _MfrBundleMaxBundleLinks_Type(Integer32):
    """Custom type mfrBundleMaxBundleLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MfrBundleMaxBundleLinks_Type.__name__ = "Integer32"
_MfrBundleMaxBundleLinks_Object = MibTableColumn
mfrBundleMaxBundleLinks = _MfrBundleMaxBundleLinks_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 14),
    _MfrBundleMaxBundleLinks_Type()
)
mfrBundleMaxBundleLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrBundleMaxBundleLinks.setStatus("current")
if mibBuilder.loadTexts:
    mfrBundleMaxBundleLinks.setUnits("Bundle Links")


class _MfrBundleLinksConfigured_Type(Integer32):
    """Custom type mfrBundleLinksConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MfrBundleLinksConfigured_Type.__name__ = "Integer32"
_MfrBundleLinksConfigured_Object = MibTableColumn
mfrBundleLinksConfigured = _MfrBundleLinksConfigured_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 15),
    _MfrBundleLinksConfigured_Type()
)
mfrBundleLinksConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrBundleLinksConfigured.setStatus("current")
if mibBuilder.loadTexts:
    mfrBundleLinksConfigured.setUnits("Bundle Links")


class _MfrBundleLinksActive_Type(Integer32):
    """Custom type mfrBundleLinksActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_MfrBundleLinksActive_Type.__name__ = "Integer32"
_MfrBundleLinksActive_Object = MibTableColumn
mfrBundleLinksActive = _MfrBundleLinksActive_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 16),
    _MfrBundleLinksActive_Type()
)
mfrBundleLinksActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrBundleLinksActive.setStatus("current")
if mibBuilder.loadTexts:
    mfrBundleLinksActive.setUnits("Bundle Links")
_MfrBundleBandwidth_Type = Integer32
_MfrBundleBandwidth_Object = MibTableColumn
mfrBundleBandwidth = _MfrBundleBandwidth_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 17),
    _MfrBundleBandwidth_Type()
)
mfrBundleBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrBundleBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    mfrBundleBandwidth.setUnits("Bits/Sec")
_MfrBundleFarEndName_Type = SnmpAdminString
_MfrBundleFarEndName_Object = MibTableColumn
mfrBundleFarEndName = _MfrBundleFarEndName_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 18),
    _MfrBundleFarEndName_Type()
)
mfrBundleFarEndName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrBundleFarEndName.setStatus("current")
_MfrBundleResequencingErrors_Type = Counter32
_MfrBundleResequencingErrors_Object = MibTableColumn
mfrBundleResequencingErrors = _MfrBundleResequencingErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 19),
    _MfrBundleResequencingErrors_Type()
)
mfrBundleResequencingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrBundleResequencingErrors.setStatus("current")
if mibBuilder.loadTexts:
    mfrBundleResequencingErrors.setUnits("Error Events")
_MfrBundleIfIndexMappingTable_Object = MibTable
mfrBundleIfIndexMappingTable = _MfrBundleIfIndexMappingTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 2, 4)
)
if mibBuilder.loadTexts:
    mfrBundleIfIndexMappingTable.setStatus("current")
_MfrBundleIfIndexMappingEntry_Object = MibTableRow
mfrBundleIfIndexMappingEntry = _MfrBundleIfIndexMappingEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 2, 4, 1)
)
mfrBundleIfIndexMappingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mfrBundleIfIndexMappingEntry.setStatus("current")


class _MfrBundleIfIndexMappingIndex_Type(Integer32):
    """Custom type mfrBundleIfIndexMappingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MfrBundleIfIndexMappingIndex_Type.__name__ = "Integer32"
_MfrBundleIfIndexMappingIndex_Object = MibTableColumn
mfrBundleIfIndexMappingIndex = _MfrBundleIfIndexMappingIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 2, 4, 1, 2),
    _MfrBundleIfIndexMappingIndex_Type()
)
mfrBundleIfIndexMappingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrBundleIfIndexMappingIndex.setStatus("current")
_MfrMibBundleLinkObjects_ObjectIdentity = ObjectIdentity
mfrMibBundleLinkObjects = _MfrMibBundleLinkObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 47, 3)
)
_MfrBundleLinkTable_Object = MibTable
mfrBundleLinkTable = _MfrBundleLinkTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 3, 1)
)
if mibBuilder.loadTexts:
    mfrBundleLinkTable.setStatus("current")
_MfrBundleLinkEntry_Object = MibTableRow
mfrBundleLinkEntry = _MfrBundleLinkEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1)
)
mfrBundleLinkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mfrBundleLinkEntry.setStatus("current")
_MfrBundleLinkRowStatus_Type = RowStatus
_MfrBundleLinkRowStatus_Object = MibTableColumn
mfrBundleLinkRowStatus = _MfrBundleLinkRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 1),
    _MfrBundleLinkRowStatus_Type()
)
mfrBundleLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mfrBundleLinkRowStatus.setStatus("current")


class _MfrBundleLinkConfigBundleIndex_Type(Integer32):
    """Custom type mfrBundleLinkConfigBundleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MfrBundleLinkConfigBundleIndex_Type.__name__ = "Integer32"
_MfrBundleLinkConfigBundleIndex_Object = MibTableColumn
mfrBundleLinkConfigBundleIndex = _MfrBundleLinkConfigBundleIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 2),
    _MfrBundleLinkConfigBundleIndex_Type()
)
mfrBundleLinkConfigBundleIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mfrBundleLinkConfigBundleIndex.setStatus("current")
_MfrBundleLinkNearEndName_Type = SnmpAdminString
_MfrBundleLinkNearEndName_Object = MibTableColumn
mfrBundleLinkNearEndName = _MfrBundleLinkNearEndName_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 3),
    _MfrBundleLinkNearEndName_Type()
)
mfrBundleLinkNearEndName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mfrBundleLinkNearEndName.setStatus("current")
_MfrBundleLinkState_Type = MfrBundleLinkState
_MfrBundleLinkState_Object = MibTableColumn
mfrBundleLinkState = _MfrBundleLinkState_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 4),
    _MfrBundleLinkState_Type()
)
mfrBundleLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrBundleLinkState.setStatus("current")
_MfrBundleLinkFarEndName_Type = SnmpAdminString
_MfrBundleLinkFarEndName_Object = MibTableColumn
mfrBundleLinkFarEndName = _MfrBundleLinkFarEndName_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 5),
    _MfrBundleLinkFarEndName_Type()
)
mfrBundleLinkFarEndName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrBundleLinkFarEndName.setStatus("current")
_MfrBundleLinkFarEndBundleName_Type = SnmpAdminString
_MfrBundleLinkFarEndBundleName_Object = MibTableColumn
mfrBundleLinkFarEndBundleName = _MfrBundleLinkFarEndBundleName_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 6),
    _MfrBundleLinkFarEndBundleName_Type()
)
mfrBundleLinkFarEndBundleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrBundleLinkFarEndBundleName.setStatus("current")


class _MfrBundleLinkDelay_Type(Integer32):
    """Custom type mfrBundleLinkDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_MfrBundleLinkDelay_Type.__name__ = "Integer32"
_MfrBundleLinkDelay_Object = MibTableColumn
mfrBundleLinkDelay = _MfrBundleLinkDelay_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 7),
    _MfrBundleLinkDelay_Type()
)
mfrBundleLinkDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrBundleLinkDelay.setStatus("current")
if mibBuilder.loadTexts:
    mfrBundleLinkDelay.setUnits("Milliseconds")
_MfrBundleLinkFramesControlTx_Type = Counter32
_MfrBundleLinkFramesControlTx_Object = MibTableColumn
mfrBundleLinkFramesControlTx = _MfrBundleLinkFramesControlTx_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 8),
    _MfrBundleLinkFramesControlTx_Type()
)
mfrBundleLinkFramesControlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrBundleLinkFramesControlTx.setStatus("current")
if mibBuilder.loadTexts:
    mfrBundleLinkFramesControlTx.setUnits("Frames")
_MfrBundleLinkFramesControlRx_Type = Counter32
_MfrBundleLinkFramesControlRx_Object = MibTableColumn
mfrBundleLinkFramesControlRx = _MfrBundleLinkFramesControlRx_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 9),
    _MfrBundleLinkFramesControlRx_Type()
)
mfrBundleLinkFramesControlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrBundleLinkFramesControlRx.setStatus("current")
if mibBuilder.loadTexts:
    mfrBundleLinkFramesControlRx.setUnits("Frames")
_MfrBundleLinkFramesControlInvalid_Type = Counter32
_MfrBundleLinkFramesControlInvalid_Object = MibTableColumn
mfrBundleLinkFramesControlInvalid = _MfrBundleLinkFramesControlInvalid_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 10),
    _MfrBundleLinkFramesControlInvalid_Type()
)
mfrBundleLinkFramesControlInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrBundleLinkFramesControlInvalid.setStatus("current")
if mibBuilder.loadTexts:
    mfrBundleLinkFramesControlInvalid.setUnits("Frames")
_MfrBundleLinkTimerExpiredCount_Type = Counter32
_MfrBundleLinkTimerExpiredCount_Object = MibTableColumn
mfrBundleLinkTimerExpiredCount = _MfrBundleLinkTimerExpiredCount_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 11),
    _MfrBundleLinkTimerExpiredCount_Type()
)
mfrBundleLinkTimerExpiredCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrBundleLinkTimerExpiredCount.setStatus("current")
if mibBuilder.loadTexts:
    mfrBundleLinkTimerExpiredCount.setUnits("Timer Expiration Events")
_MfrBundleLinkLoopbackSuspected_Type = Counter32
_MfrBundleLinkLoopbackSuspected_Object = MibTableColumn
mfrBundleLinkLoopbackSuspected = _MfrBundleLinkLoopbackSuspected_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 12),
    _MfrBundleLinkLoopbackSuspected_Type()
)
mfrBundleLinkLoopbackSuspected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrBundleLinkLoopbackSuspected.setStatus("current")
if mibBuilder.loadTexts:
    mfrBundleLinkLoopbackSuspected.setUnits("Loopback Suspected Events")
_MfrBundleLinkUnexpectedSequence_Type = Counter32
_MfrBundleLinkUnexpectedSequence_Object = MibTableColumn
mfrBundleLinkUnexpectedSequence = _MfrBundleLinkUnexpectedSequence_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 13),
    _MfrBundleLinkUnexpectedSequence_Type()
)
mfrBundleLinkUnexpectedSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrBundleLinkUnexpectedSequence.setStatus("current")
if mibBuilder.loadTexts:
    mfrBundleLinkUnexpectedSequence.setUnits("Frames")
_MfrBundleLinkMismatch_Type = Counter32
_MfrBundleLinkMismatch_Object = MibTableColumn
mfrBundleLinkMismatch = _MfrBundleLinkMismatch_Object(
    (1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 14),
    _MfrBundleLinkMismatch_Type()
)
mfrBundleLinkMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfrBundleLinkMismatch.setStatus("current")
if mibBuilder.loadTexts:
    mfrBundleLinkMismatch.setUnits("Bundle Name Mismatch Events")
_MfrMibTraps_ObjectIdentity = ObjectIdentity
mfrMibTraps = _MfrMibTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 47, 4)
)
_MfrMibTrapsPrefix_ObjectIdentity = ObjectIdentity
mfrMibTrapsPrefix = _MfrMibTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 47, 4, 0)
)
_MfrMibConformance_ObjectIdentity = ObjectIdentity
mfrMibConformance = _MfrMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 47, 5)
)
_MfrMibGroups_ObjectIdentity = ObjectIdentity
mfrMibGroups = _MfrMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 47, 5, 1)
)
_MfrMibCompliances_ObjectIdentity = ObjectIdentity
mfrMibCompliances = _MfrMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 47, 5, 2)
)

# Managed Objects groups

mfrMibBundleGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 47, 5, 1, 1)
)
mfrMibBundleGroup.setObjects(
      *(("FR-MFR-MIB", "mfrBundleMaxNumBundles"),
        ("FR-MFR-MIB", "mfrBundleNextIndex"),
        ("FR-MFR-MIB", "mfrBundleIfIndex"),
        ("FR-MFR-MIB", "mfrBundleRowStatus"),
        ("FR-MFR-MIB", "mfrBundleNearEndName"),
        ("FR-MFR-MIB", "mfrBundleFragmentation"),
        ("FR-MFR-MIB", "mfrBundleMaxFragSize"),
        ("FR-MFR-MIB", "mfrBundleTimerHello"),
        ("FR-MFR-MIB", "mfrBundleTimerAck"),
        ("FR-MFR-MIB", "mfrBundleCountMaxRetry"),
        ("FR-MFR-MIB", "mfrBundleActivationClass"),
        ("FR-MFR-MIB", "mfrBundleThreshold"),
        ("FR-MFR-MIB", "mfrBundleMaxDiffDelay"),
        ("FR-MFR-MIB", "mfrBundleMaxBundleLinks"),
        ("FR-MFR-MIB", "mfrBundleLinksConfigured"),
        ("FR-MFR-MIB", "mfrBundleLinksActive"),
        ("FR-MFR-MIB", "mfrBundleBandwidth"),
        ("FR-MFR-MIB", "mfrBundleSeqNumSize"),
        ("FR-MFR-MIB", "mfrBundleFarEndName"),
        ("FR-MFR-MIB", "mfrBundleResequencingErrors"),
        ("FR-MFR-MIB", "mfrBundleIfIndexMappingIndex"))
)
if mibBuilder.loadTexts:
    mfrMibBundleGroup.setStatus("current")

mfrMibBundleLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 47, 5, 1, 2)
)
mfrMibBundleLinkGroup.setObjects(
      *(("FR-MFR-MIB", "mfrBundleLinkRowStatus"),
        ("FR-MFR-MIB", "mfrBundleLinkConfigBundleIndex"),
        ("FR-MFR-MIB", "mfrBundleLinkNearEndName"),
        ("FR-MFR-MIB", "mfrBundleLinkState"),
        ("FR-MFR-MIB", "mfrBundleLinkFarEndName"),
        ("FR-MFR-MIB", "mfrBundleLinkFarEndBundleName"),
        ("FR-MFR-MIB", "mfrBundleLinkDelay"),
        ("FR-MFR-MIB", "mfrBundleLinkFramesControlTx"),
        ("FR-MFR-MIB", "mfrBundleLinkFramesControlRx"),
        ("FR-MFR-MIB", "mfrBundleLinkFramesControlInvalid"),
        ("FR-MFR-MIB", "mfrBundleLinkTimerExpiredCount"),
        ("FR-MFR-MIB", "mfrBundleLinkLoopbackSuspected"),
        ("FR-MFR-MIB", "mfrBundleLinkUnexpectedSequence"),
        ("FR-MFR-MIB", "mfrBundleLinkMismatch"))
)
if mibBuilder.loadTexts:
    mfrMibBundleLinkGroup.setStatus("current")


# Notification objects

mfrMibTrapBundleLinkMismatch = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 47, 4, 0, 1)
)
mfrMibTrapBundleLinkMismatch.setObjects(
      *(("FR-MFR-MIB", "mfrBundleNearEndName"),
        ("FR-MFR-MIB", "mfrBundleFarEndName"),
        ("FR-MFR-MIB", "mfrBundleLinkNearEndName"),
        ("FR-MFR-MIB", "mfrBundleLinkFarEndName"),
        ("FR-MFR-MIB", "mfrBundleLinkFarEndBundleName"))
)
if mibBuilder.loadTexts:
    mfrMibTrapBundleLinkMismatch.setStatus(
        "current"
    )


# Notifications groups

mfrMibTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 47, 5, 1, 3)
)
mfrMibTrapGroup.setObjects(
    ("FR-MFR-MIB", "mfrMibTrapBundleLinkMismatch")
)
if mibBuilder.loadTexts:
    mfrMibTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mfrMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 47, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mfrMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FR-MFR-MIB",
    **{"MfrBundleLinkState": MfrBundleLinkState,
       "mfrMib": mfrMib,
       "mfrMibScalarObjects": mfrMibScalarObjects,
       "mfrBundleMaxNumBundles": mfrBundleMaxNumBundles,
       "mfrBundleNextIndex": mfrBundleNextIndex,
       "mfrMibBundleObjects": mfrMibBundleObjects,
       "mfrBundleTable": mfrBundleTable,
       "mfrBundleEntry": mfrBundleEntry,
       "mfrBundleIndex": mfrBundleIndex,
       "mfrBundleIfIndex": mfrBundleIfIndex,
       "mfrBundleRowStatus": mfrBundleRowStatus,
       "mfrBundleNearEndName": mfrBundleNearEndName,
       "mfrBundleFragmentation": mfrBundleFragmentation,
       "mfrBundleMaxFragSize": mfrBundleMaxFragSize,
       "mfrBundleTimerHello": mfrBundleTimerHello,
       "mfrBundleTimerAck": mfrBundleTimerAck,
       "mfrBundleCountMaxRetry": mfrBundleCountMaxRetry,
       "mfrBundleActivationClass": mfrBundleActivationClass,
       "mfrBundleThreshold": mfrBundleThreshold,
       "mfrBundleMaxDiffDelay": mfrBundleMaxDiffDelay,
       "mfrBundleSeqNumSize": mfrBundleSeqNumSize,
       "mfrBundleMaxBundleLinks": mfrBundleMaxBundleLinks,
       "mfrBundleLinksConfigured": mfrBundleLinksConfigured,
       "mfrBundleLinksActive": mfrBundleLinksActive,
       "mfrBundleBandwidth": mfrBundleBandwidth,
       "mfrBundleFarEndName": mfrBundleFarEndName,
       "mfrBundleResequencingErrors": mfrBundleResequencingErrors,
       "mfrBundleIfIndexMappingTable": mfrBundleIfIndexMappingTable,
       "mfrBundleIfIndexMappingEntry": mfrBundleIfIndexMappingEntry,
       "mfrBundleIfIndexMappingIndex": mfrBundleIfIndexMappingIndex,
       "mfrMibBundleLinkObjects": mfrMibBundleLinkObjects,
       "mfrBundleLinkTable": mfrBundleLinkTable,
       "mfrBundleLinkEntry": mfrBundleLinkEntry,
       "mfrBundleLinkRowStatus": mfrBundleLinkRowStatus,
       "mfrBundleLinkConfigBundleIndex": mfrBundleLinkConfigBundleIndex,
       "mfrBundleLinkNearEndName": mfrBundleLinkNearEndName,
       "mfrBundleLinkState": mfrBundleLinkState,
       "mfrBundleLinkFarEndName": mfrBundleLinkFarEndName,
       "mfrBundleLinkFarEndBundleName": mfrBundleLinkFarEndBundleName,
       "mfrBundleLinkDelay": mfrBundleLinkDelay,
       "mfrBundleLinkFramesControlTx": mfrBundleLinkFramesControlTx,
       "mfrBundleLinkFramesControlRx": mfrBundleLinkFramesControlRx,
       "mfrBundleLinkFramesControlInvalid": mfrBundleLinkFramesControlInvalid,
       "mfrBundleLinkTimerExpiredCount": mfrBundleLinkTimerExpiredCount,
       "mfrBundleLinkLoopbackSuspected": mfrBundleLinkLoopbackSuspected,
       "mfrBundleLinkUnexpectedSequence": mfrBundleLinkUnexpectedSequence,
       "mfrBundleLinkMismatch": mfrBundleLinkMismatch,
       "mfrMibTraps": mfrMibTraps,
       "mfrMibTrapsPrefix": mfrMibTrapsPrefix,
       "mfrMibTrapBundleLinkMismatch": mfrMibTrapBundleLinkMismatch,
       "mfrMibConformance": mfrMibConformance,
       "mfrMibGroups": mfrMibGroups,
       "mfrMibBundleGroup": mfrMibBundleGroup,
       "mfrMibBundleLinkGroup": mfrMibBundleLinkGroup,
       "mfrMibTrapGroup": mfrMibTrapGroup,
       "mfrMibCompliances": mfrMibCompliances,
       "mfrMibCompliance": mfrMibCompliance}
)
