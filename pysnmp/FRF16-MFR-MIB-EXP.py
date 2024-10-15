# SNMP MIB module (FRF16-MFR-MIB-EXP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FRF16-MFR-MIB-EXP
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:24 2024
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
 experimental,
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
    "experimental",
    "iso")

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
    (1, 3, 6, 1, 3, 555)
)
mfrMib.setRevisions(
        ("1999-10-01 14:40",
         "1999-10-15 13:00",
         "1999-10-21 20:20")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BundleLinkState(Integer32, TextualConvention):
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
        *(("bundleLinkStateAddAckRx", 3),
          ("bundleLinkStateAddRx", 2),
          ("bundleLinkStateAddSent", 1),
          ("bundleLinkStateDown", 7),
          ("bundleLinkStateDownIdle", 8),
          ("bundleLinkStateIdle", 6),
          ("bundleLinkStateIdlePending", 5),
          ("bundleLinkStateUp", 4))
    )



# MIB Managed Objects in the order of their OIDs

_MfrMibObjects_ObjectIdentity = ObjectIdentity
mfrMibObjects = _MfrMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 555, 1)
)
_MfrMibScalarObjects_ObjectIdentity = ObjectIdentity
mfrMibScalarObjects = _MfrMibScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 555, 1, 1)
)
_BundleMaxNumBundles_Type = Integer32
_BundleMaxNumBundles_Object = MibScalar
bundleMaxNumBundles = _BundleMaxNumBundles_Object(
    (1, 3, 6, 1, 3, 555, 1, 1, 1),
    _BundleMaxNumBundles_Type()
)
bundleMaxNumBundles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleMaxNumBundles.setStatus("current")
_BundleNextIndex_Type = TestAndIncr
_BundleNextIndex_Object = MibScalar
bundleNextIndex = _BundleNextIndex_Object(
    (1, 3, 6, 1, 3, 555, 1, 1, 2),
    _BundleNextIndex_Type()
)
bundleNextIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bundleNextIndex.setStatus("current")
_MfrMibBundleObjects_ObjectIdentity = ObjectIdentity
mfrMibBundleObjects = _MfrMibBundleObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 555, 1, 2)
)
_BundleTable_Object = MibTable
bundleTable = _BundleTable_Object(
    (1, 3, 6, 1, 3, 555, 1, 2, 3)
)
if mibBuilder.loadTexts:
    bundleTable.setStatus("current")
_BundleEntry_Object = MibTableRow
bundleEntry = _BundleEntry_Object(
    (1, 3, 6, 1, 3, 555, 1, 2, 3, 1)
)
bundleEntry.setIndexNames(
    (0, "FRF16-MFR-MIB-EXP", "bundleIndex"),
)
if mibBuilder.loadTexts:
    bundleEntry.setStatus("current")


class _BundleIndex_Type(Integer32):
    """Custom type bundleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BundleIndex_Type.__name__ = "Integer32"
_BundleIndex_Object = MibTableColumn
bundleIndex = _BundleIndex_Object(
    (1, 3, 6, 1, 3, 555, 1, 2, 3, 1, 1),
    _BundleIndex_Type()
)
bundleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bundleIndex.setStatus("current")
_BundleIfIndex_Type = InterfaceIndex
_BundleIfIndex_Object = MibTableColumn
bundleIfIndex = _BundleIfIndex_Object(
    (1, 3, 6, 1, 3, 555, 1, 2, 3, 1, 2),
    _BundleIfIndex_Type()
)
bundleIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleIfIndex.setStatus("current")
_BundleRowStatus_Type = RowStatus
_BundleRowStatus_Object = MibTableColumn
bundleRowStatus = _BundleRowStatus_Object(
    (1, 3, 6, 1, 3, 555, 1, 2, 3, 1, 3),
    _BundleRowStatus_Type()
)
bundleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleRowStatus.setStatus("current")


class _BundleNearEndName_Type(SnmpAdminString):
    """Custom type bundleNearEndName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_BundleNearEndName_Type.__name__ = "SnmpAdminString"
_BundleNearEndName_Object = MibTableColumn
bundleNearEndName = _BundleNearEndName_Object(
    (1, 3, 6, 1, 3, 555, 1, 2, 3, 1, 4),
    _BundleNearEndName_Type()
)
bundleNearEndName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleNearEndName.setStatus("current")


class _BundleFragmentation_Type(Integer32):
    """Custom type bundleFragmentation based on Integer32"""
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


_BundleFragmentation_Type.__name__ = "Integer32"
_BundleFragmentation_Object = MibTableColumn
bundleFragmentation = _BundleFragmentation_Object(
    (1, 3, 6, 1, 3, 555, 1, 2, 3, 1, 5),
    _BundleFragmentation_Type()
)
bundleFragmentation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleFragmentation.setStatus("current")


class _BundleMaxFragSize_Type(Integer32):
    """Custom type bundleMaxFragSize based on Integer32"""
    defaultValue = -1


_BundleMaxFragSize_Object = MibTableColumn
bundleMaxFragSize = _BundleMaxFragSize_Object(
    (1, 3, 6, 1, 3, 555, 1, 2, 3, 1, 6),
    _BundleMaxFragSize_Type()
)
bundleMaxFragSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleMaxFragSize.setStatus("current")


class _BundleTimerHello_Type(Integer32):
    """Custom type bundleTimerHello based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_BundleTimerHello_Type.__name__ = "Integer32"
_BundleTimerHello_Object = MibTableColumn
bundleTimerHello = _BundleTimerHello_Object(
    (1, 3, 6, 1, 3, 555, 1, 2, 3, 1, 7),
    _BundleTimerHello_Type()
)
bundleTimerHello.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleTimerHello.setStatus("current")


class _BundleTimerAck_Type(Integer32):
    """Custom type bundleTimerAck based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_BundleTimerAck_Type.__name__ = "Integer32"
_BundleTimerAck_Object = MibTableColumn
bundleTimerAck = _BundleTimerAck_Object(
    (1, 3, 6, 1, 3, 555, 1, 2, 3, 1, 8),
    _BundleTimerAck_Type()
)
bundleTimerAck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleTimerAck.setStatus("current")


class _BundleCountMaxRetry_Type(Integer32):
    """Custom type bundleCountMaxRetry based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_BundleCountMaxRetry_Type.__name__ = "Integer32"
_BundleCountMaxRetry_Object = MibTableColumn
bundleCountMaxRetry = _BundleCountMaxRetry_Object(
    (1, 3, 6, 1, 3, 555, 1, 2, 3, 1, 9),
    _BundleCountMaxRetry_Type()
)
bundleCountMaxRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleCountMaxRetry.setStatus("current")


class _BundleActivationClass_Type(Integer32):
    """Custom type bundleActivationClass based on Integer32"""
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
        *(("bundleActivationClassA", 1),
          ("bundleActivationClassB", 2),
          ("bundleActivationClassC", 3),
          ("bundleActivationClassD", 4))
    )


_BundleActivationClass_Type.__name__ = "Integer32"
_BundleActivationClass_Object = MibTableColumn
bundleActivationClass = _BundleActivationClass_Object(
    (1, 3, 6, 1, 3, 555, 1, 2, 3, 1, 10),
    _BundleActivationClass_Type()
)
bundleActivationClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleActivationClass.setStatus("current")


class _BundleThreshold_Type(Integer32):
    """Custom type bundleThreshold based on Integer32"""
    defaultValue = -1


_BundleThreshold_Object = MibTableColumn
bundleThreshold = _BundleThreshold_Object(
    (1, 3, 6, 1, 3, 555, 1, 2, 3, 1, 11),
    _BundleThreshold_Type()
)
bundleThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleThreshold.setStatus("current")


class _BundleMaxDiffDelay_Type(Integer32):
    """Custom type bundleMaxDiffDelay based on Integer32"""
    defaultValue = -1


_BundleMaxDiffDelay_Object = MibTableColumn
bundleMaxDiffDelay = _BundleMaxDiffDelay_Object(
    (1, 3, 6, 1, 3, 555, 1, 2, 3, 1, 12),
    _BundleMaxDiffDelay_Type()
)
bundleMaxDiffDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleMaxDiffDelay.setStatus("current")


class _BundleSeqNumSize_Type(Integer32):
    """Custom type bundleSeqNumSize based on Integer32"""
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


_BundleSeqNumSize_Type.__name__ = "Integer32"
_BundleSeqNumSize_Object = MibTableColumn
bundleSeqNumSize = _BundleSeqNumSize_Object(
    (1, 3, 6, 1, 3, 555, 1, 2, 3, 1, 13),
    _BundleSeqNumSize_Type()
)
bundleSeqNumSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleSeqNumSize.setStatus("current")
_BundleMaxBundleLinks_Type = Integer32
_BundleMaxBundleLinks_Object = MibTableColumn
bundleMaxBundleLinks = _BundleMaxBundleLinks_Object(
    (1, 3, 6, 1, 3, 555, 1, 2, 3, 1, 14),
    _BundleMaxBundleLinks_Type()
)
bundleMaxBundleLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleMaxBundleLinks.setStatus("current")


class _BundleFarEndName_Type(SnmpAdminString):
    """Custom type bundleFarEndName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_BundleFarEndName_Type.__name__ = "SnmpAdminString"
_BundleFarEndName_Object = MibTableColumn
bundleFarEndName = _BundleFarEndName_Object(
    (1, 3, 6, 1, 3, 555, 1, 2, 3, 1, 15),
    _BundleFarEndName_Type()
)
bundleFarEndName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleFarEndName.setStatus("current")
_BundleResequencingErrors_Type = Counter32
_BundleResequencingErrors_Object = MibTableColumn
bundleResequencingErrors = _BundleResequencingErrors_Object(
    (1, 3, 6, 1, 3, 555, 1, 2, 3, 1, 16),
    _BundleResequencingErrors_Type()
)
bundleResequencingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleResequencingErrors.setStatus("current")
_BundleIfIndexMappingTable_Object = MibTable
bundleIfIndexMappingTable = _BundleIfIndexMappingTable_Object(
    (1, 3, 6, 1, 3, 555, 1, 2, 4)
)
if mibBuilder.loadTexts:
    bundleIfIndexMappingTable.setStatus("current")
_BundleIfIndexMappingEntry_Object = MibTableRow
bundleIfIndexMappingEntry = _BundleIfIndexMappingEntry_Object(
    (1, 3, 6, 1, 3, 555, 1, 2, 4, 1)
)
bundleIfIndexMappingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    bundleIfIndexMappingEntry.setStatus("current")
_BundleIfIndexMappingIndex_Type = InterfaceIndex
_BundleIfIndexMappingIndex_Object = MibTableColumn
bundleIfIndexMappingIndex = _BundleIfIndexMappingIndex_Object(
    (1, 3, 6, 1, 3, 555, 1, 2, 4, 1, 2),
    _BundleIfIndexMappingIndex_Type()
)
bundleIfIndexMappingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleIfIndexMappingIndex.setStatus("current")
_MfrMibBundleLinkObjects_ObjectIdentity = ObjectIdentity
mfrMibBundleLinkObjects = _MfrMibBundleLinkObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 555, 1, 3)
)
_BundleLinkTable_Object = MibTable
bundleLinkTable = _BundleLinkTable_Object(
    (1, 3, 6, 1, 3, 555, 1, 3, 1)
)
if mibBuilder.loadTexts:
    bundleLinkTable.setStatus("current")
_BundleLinkEntry_Object = MibTableRow
bundleLinkEntry = _BundleLinkEntry_Object(
    (1, 3, 6, 1, 3, 555, 1, 3, 1, 1)
)
bundleLinkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    bundleLinkEntry.setStatus("current")
_BundleLinkRowStatus_Type = RowStatus
_BundleLinkRowStatus_Object = MibTableColumn
bundleLinkRowStatus = _BundleLinkRowStatus_Object(
    (1, 3, 6, 1, 3, 555, 1, 3, 1, 1, 1),
    _BundleLinkRowStatus_Type()
)
bundleLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleLinkRowStatus.setStatus("current")
_BundleLinkConfigBundleIndex_Type = Integer32
_BundleLinkConfigBundleIndex_Object = MibTableColumn
bundleLinkConfigBundleIndex = _BundleLinkConfigBundleIndex_Object(
    (1, 3, 6, 1, 3, 555, 1, 3, 1, 1, 2),
    _BundleLinkConfigBundleIndex_Type()
)
bundleLinkConfigBundleIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleLinkConfigBundleIndex.setStatus("current")


class _BundleLinkNearEndName_Type(SnmpAdminString):
    """Custom type bundleLinkNearEndName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_BundleLinkNearEndName_Type.__name__ = "SnmpAdminString"
_BundleLinkNearEndName_Object = MibTableColumn
bundleLinkNearEndName = _BundleLinkNearEndName_Object(
    (1, 3, 6, 1, 3, 555, 1, 3, 1, 1, 3),
    _BundleLinkNearEndName_Type()
)
bundleLinkNearEndName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bundleLinkNearEndName.setStatus("current")
_BundleLinkState_Type = BundleLinkState
_BundleLinkState_Object = MibTableColumn
bundleLinkState = _BundleLinkState_Object(
    (1, 3, 6, 1, 3, 555, 1, 3, 1, 1, 4),
    _BundleLinkState_Type()
)
bundleLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleLinkState.setStatus("current")


class _BundleLinkFarEndName_Type(SnmpAdminString):
    """Custom type bundleLinkFarEndName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_BundleLinkFarEndName_Type.__name__ = "SnmpAdminString"
_BundleLinkFarEndName_Object = MibTableColumn
bundleLinkFarEndName = _BundleLinkFarEndName_Object(
    (1, 3, 6, 1, 3, 555, 1, 3, 1, 1, 5),
    _BundleLinkFarEndName_Type()
)
bundleLinkFarEndName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleLinkFarEndName.setStatus("current")


class _BundleLinkFarEndBundleName_Type(SnmpAdminString):
    """Custom type bundleLinkFarEndBundleName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_BundleLinkFarEndBundleName_Type.__name__ = "SnmpAdminString"
_BundleLinkFarEndBundleName_Object = MibTableColumn
bundleLinkFarEndBundleName = _BundleLinkFarEndBundleName_Object(
    (1, 3, 6, 1, 3, 555, 1, 3, 1, 1, 6),
    _BundleLinkFarEndBundleName_Type()
)
bundleLinkFarEndBundleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleLinkFarEndBundleName.setStatus("current")
_BundleLinkDelay_Type = Integer32
_BundleLinkDelay_Object = MibTableColumn
bundleLinkDelay = _BundleLinkDelay_Object(
    (1, 3, 6, 1, 3, 555, 1, 3, 1, 1, 7),
    _BundleLinkDelay_Type()
)
bundleLinkDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleLinkDelay.setStatus("current")
_BundleLinkFramesControlTx_Type = Counter32
_BundleLinkFramesControlTx_Object = MibTableColumn
bundleLinkFramesControlTx = _BundleLinkFramesControlTx_Object(
    (1, 3, 6, 1, 3, 555, 1, 3, 1, 1, 8),
    _BundleLinkFramesControlTx_Type()
)
bundleLinkFramesControlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleLinkFramesControlTx.setStatus("current")
_BundleLinkFramesControlRx_Type = Counter32
_BundleLinkFramesControlRx_Object = MibTableColumn
bundleLinkFramesControlRx = _BundleLinkFramesControlRx_Object(
    (1, 3, 6, 1, 3, 555, 1, 3, 1, 1, 9),
    _BundleLinkFramesControlRx_Type()
)
bundleLinkFramesControlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleLinkFramesControlRx.setStatus("current")
_BundleLinkFramesControlInvalid_Type = Counter32
_BundleLinkFramesControlInvalid_Object = MibTableColumn
bundleLinkFramesControlInvalid = _BundleLinkFramesControlInvalid_Object(
    (1, 3, 6, 1, 3, 555, 1, 3, 1, 1, 10),
    _BundleLinkFramesControlInvalid_Type()
)
bundleLinkFramesControlInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleLinkFramesControlInvalid.setStatus("current")
_BundleLinkTimerExpiredCount_Type = Counter32
_BundleLinkTimerExpiredCount_Object = MibTableColumn
bundleLinkTimerExpiredCount = _BundleLinkTimerExpiredCount_Object(
    (1, 3, 6, 1, 3, 555, 1, 3, 1, 1, 11),
    _BundleLinkTimerExpiredCount_Type()
)
bundleLinkTimerExpiredCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleLinkTimerExpiredCount.setStatus("current")
_BundleLinkLoopbackSuspected_Type = Counter32
_BundleLinkLoopbackSuspected_Object = MibTableColumn
bundleLinkLoopbackSuspected = _BundleLinkLoopbackSuspected_Object(
    (1, 3, 6, 1, 3, 555, 1, 3, 1, 1, 12),
    _BundleLinkLoopbackSuspected_Type()
)
bundleLinkLoopbackSuspected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleLinkLoopbackSuspected.setStatus("current")
_BundleLinkUnexpectedSequence_Type = Counter32
_BundleLinkUnexpectedSequence_Object = MibTableColumn
bundleLinkUnexpectedSequence = _BundleLinkUnexpectedSequence_Object(
    (1, 3, 6, 1, 3, 555, 1, 3, 1, 1, 13),
    _BundleLinkUnexpectedSequence_Type()
)
bundleLinkUnexpectedSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleLinkUnexpectedSequence.setStatus("current")
_BundleLinkMismatch_Type = Counter32
_BundleLinkMismatch_Object = MibTableColumn
bundleLinkMismatch = _BundleLinkMismatch_Object(
    (1, 3, 6, 1, 3, 555, 1, 3, 1, 1, 14),
    _BundleLinkMismatch_Type()
)
bundleLinkMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bundleLinkMismatch.setStatus("current")
_MfrMibTraps_ObjectIdentity = ObjectIdentity
mfrMibTraps = _MfrMibTraps_ObjectIdentity(
    (1, 3, 6, 1, 3, 555, 2)
)
_MfrMibTrapsPrefix_ObjectIdentity = ObjectIdentity
mfrMibTrapsPrefix = _MfrMibTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 3, 555, 2, 0)
)
_MfrMibConformance_ObjectIdentity = ObjectIdentity
mfrMibConformance = _MfrMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 555, 3)
)
_MfrMibGroups_ObjectIdentity = ObjectIdentity
mfrMibGroups = _MfrMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 555, 3, 1)
)
_MfrMibCompliances_ObjectIdentity = ObjectIdentity
mfrMibCompliances = _MfrMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 555, 3, 2)
)

# Managed Objects groups

mfrMibBundleGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 555, 3, 1, 1)
)
mfrMibBundleGroup.setObjects(
      *(("FRF16-MFR-MIB-EXP", "bundleMaxNumBundles"),
        ("FRF16-MFR-MIB-EXP", "bundleIfIndex"),
        ("FRF16-MFR-MIB-EXP", "bundleRowStatus"),
        ("FRF16-MFR-MIB-EXP", "bundleNearEndName"),
        ("FRF16-MFR-MIB-EXP", "bundleFragmentation"),
        ("FRF16-MFR-MIB-EXP", "bundleMaxFragSize"),
        ("FRF16-MFR-MIB-EXP", "bundleTimerHello"),
        ("FRF16-MFR-MIB-EXP", "bundleTimerAck"),
        ("FRF16-MFR-MIB-EXP", "bundleCountMaxRetry"),
        ("FRF16-MFR-MIB-EXP", "bundleActivationClass"),
        ("FRF16-MFR-MIB-EXP", "bundleThreshold"),
        ("FRF16-MFR-MIB-EXP", "bundleMaxDiffDelay"),
        ("FRF16-MFR-MIB-EXP", "bundleMaxBundleLinks"),
        ("FRF16-MFR-MIB-EXP", "bundleSeqNumSize"),
        ("FRF16-MFR-MIB-EXP", "bundleFarEndName"),
        ("FRF16-MFR-MIB-EXP", "bundleResequencingErrors"),
        ("FRF16-MFR-MIB-EXP", "bundleIfIndexMappingIndex"),
        ("FRF16-MFR-MIB-EXP", "bundleNextIndex"))
)
if mibBuilder.loadTexts:
    mfrMibBundleGroup.setStatus("current")

mfrMibBundleLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 555, 3, 1, 2)
)
mfrMibBundleLinkGroup.setObjects(
      *(("FRF16-MFR-MIB-EXP", "bundleLinkRowStatus"),
        ("FRF16-MFR-MIB-EXP", "bundleLinkConfigBundleIndex"),
        ("FRF16-MFR-MIB-EXP", "bundleLinkNearEndName"),
        ("FRF16-MFR-MIB-EXP", "bundleLinkState"),
        ("FRF16-MFR-MIB-EXP", "bundleLinkFarEndName"),
        ("FRF16-MFR-MIB-EXP", "bundleLinkFarEndBundleName"),
        ("FRF16-MFR-MIB-EXP", "bundleLinkDelay"),
        ("FRF16-MFR-MIB-EXP", "bundleLinkFramesControlTx"),
        ("FRF16-MFR-MIB-EXP", "bundleLinkFramesControlRx"),
        ("FRF16-MFR-MIB-EXP", "bundleLinkFramesControlInvalid"),
        ("FRF16-MFR-MIB-EXP", "bundleLinkTimerExpiredCount"),
        ("FRF16-MFR-MIB-EXP", "bundleLinkLoopbackSuspected"),
        ("FRF16-MFR-MIB-EXP", "bundleLinkUnexpectedSequence"),
        ("FRF16-MFR-MIB-EXP", "bundleLinkMismatch"))
)
if mibBuilder.loadTexts:
    mfrMibBundleLinkGroup.setStatus("current")


# Notification objects

mfrMibTrapBundleLinkMismatch = NotificationType(
    (1, 3, 6, 1, 3, 555, 2, 0, 1)
)
mfrMibTrapBundleLinkMismatch.setObjects(
      *(("FRF16-MFR-MIB-EXP", "bundleNearEndName"),
        ("FRF16-MFR-MIB-EXP", "bundleFarEndName"),
        ("FRF16-MFR-MIB-EXP", "bundleLinkNearEndName"),
        ("FRF16-MFR-MIB-EXP", "bundleLinkFarEndName"),
        ("FRF16-MFR-MIB-EXP", "bundleLinkFarEndBundleName"))
)
if mibBuilder.loadTexts:
    mfrMibTrapBundleLinkMismatch.setStatus(
        "current"
    )


# Notifications groups

mfrMibTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 3, 555, 3, 1, 3)
)
mfrMibTrapGroup.setObjects(
    ("FRF16-MFR-MIB-EXP", "mfrMibTrapBundleLinkMismatch")
)
if mibBuilder.loadTexts:
    mfrMibTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mfrMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 555, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mfrMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FRF16-MFR-MIB-EXP",
    **{"BundleLinkState": BundleLinkState,
       "mfrMib": mfrMib,
       "mfrMibObjects": mfrMibObjects,
       "mfrMibScalarObjects": mfrMibScalarObjects,
       "bundleMaxNumBundles": bundleMaxNumBundles,
       "bundleNextIndex": bundleNextIndex,
       "mfrMibBundleObjects": mfrMibBundleObjects,
       "bundleTable": bundleTable,
       "bundleEntry": bundleEntry,
       "bundleIndex": bundleIndex,
       "bundleIfIndex": bundleIfIndex,
       "bundleRowStatus": bundleRowStatus,
       "bundleNearEndName": bundleNearEndName,
       "bundleFragmentation": bundleFragmentation,
       "bundleMaxFragSize": bundleMaxFragSize,
       "bundleTimerHello": bundleTimerHello,
       "bundleTimerAck": bundleTimerAck,
       "bundleCountMaxRetry": bundleCountMaxRetry,
       "bundleActivationClass": bundleActivationClass,
       "bundleThreshold": bundleThreshold,
       "bundleMaxDiffDelay": bundleMaxDiffDelay,
       "bundleSeqNumSize": bundleSeqNumSize,
       "bundleMaxBundleLinks": bundleMaxBundleLinks,
       "bundleFarEndName": bundleFarEndName,
       "bundleResequencingErrors": bundleResequencingErrors,
       "bundleIfIndexMappingTable": bundleIfIndexMappingTable,
       "bundleIfIndexMappingEntry": bundleIfIndexMappingEntry,
       "bundleIfIndexMappingIndex": bundleIfIndexMappingIndex,
       "mfrMibBundleLinkObjects": mfrMibBundleLinkObjects,
       "bundleLinkTable": bundleLinkTable,
       "bundleLinkEntry": bundleLinkEntry,
       "bundleLinkRowStatus": bundleLinkRowStatus,
       "bundleLinkConfigBundleIndex": bundleLinkConfigBundleIndex,
       "bundleLinkNearEndName": bundleLinkNearEndName,
       "bundleLinkState": bundleLinkState,
       "bundleLinkFarEndName": bundleLinkFarEndName,
       "bundleLinkFarEndBundleName": bundleLinkFarEndBundleName,
       "bundleLinkDelay": bundleLinkDelay,
       "bundleLinkFramesControlTx": bundleLinkFramesControlTx,
       "bundleLinkFramesControlRx": bundleLinkFramesControlRx,
       "bundleLinkFramesControlInvalid": bundleLinkFramesControlInvalid,
       "bundleLinkTimerExpiredCount": bundleLinkTimerExpiredCount,
       "bundleLinkLoopbackSuspected": bundleLinkLoopbackSuspected,
       "bundleLinkUnexpectedSequence": bundleLinkUnexpectedSequence,
       "bundleLinkMismatch": bundleLinkMismatch,
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
