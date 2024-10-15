# SNMP MIB module (A3COM-SWITCHING-SYSTEMS-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-SWITCHING-SYSTEMS-BRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:47 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
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

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_SwitchingSystemsMibs_ObjectIdentity = ObjectIdentity
switchingSystemsMibs = _SwitchingSystemsMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29)
)
_A3ComSwitchingSystemsMib_ObjectIdentity = ObjectIdentity
a3ComSwitchingSystemsMib = _A3ComSwitchingSystemsMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4)
)
_A3ComSysBridge_ObjectIdentity = ObjectIdentity
a3ComSysBridge = _A3ComSysBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10)
)
_A3ComSysBridgeCount_Type = Integer32
_A3ComSysBridgeCount_Object = MibScalar
a3ComSysBridgeCount = _A3ComSysBridgeCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 1),
    _A3ComSysBridgeCount_Type()
)
a3ComSysBridgeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgeCount.setStatus("mandatory")
_A3ComSysBridgeTable_Object = MibTable
a3ComSysBridgeTable = _A3ComSysBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2)
)
if mibBuilder.loadTexts:
    a3ComSysBridgeTable.setStatus("mandatory")
_A3ComSysBridgeEntry_Object = MibTableRow
a3ComSysBridgeEntry = _A3ComSysBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1)
)
a3ComSysBridgeEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-BRIDGE-MIB", "a3ComSysBridgeIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysBridgeEntry.setStatus("mandatory")


class _A3ComSysBridgeIndex_Type(Integer32):
    """Custom type a3ComSysBridgeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComSysBridgeIndex_Type.__name__ = "Integer32"
_A3ComSysBridgeIndex_Object = MibTableColumn
a3ComSysBridgeIndex = _A3ComSysBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 1),
    _A3ComSysBridgeIndex_Type()
)
a3ComSysBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgeIndex.setStatus("mandatory")
_A3ComSysBridgePortCount_Type = Integer32
_A3ComSysBridgePortCount_Object = MibTableColumn
a3ComSysBridgePortCount = _A3ComSysBridgePortCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 2),
    _A3ComSysBridgePortCount_Type()
)
a3ComSysBridgePortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortCount.setStatus("mandatory")
_A3ComSysBridgeAddressTableSize_Type = Integer32
_A3ComSysBridgeAddressTableSize_Object = MibTableColumn
a3ComSysBridgeAddressTableSize = _A3ComSysBridgeAddressTableSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 3),
    _A3ComSysBridgeAddressTableSize_Type()
)
a3ComSysBridgeAddressTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgeAddressTableSize.setStatus("mandatory")
_A3ComSysBridgeAddressTableCount_Type = Integer32
_A3ComSysBridgeAddressTableCount_Object = MibTableColumn
a3ComSysBridgeAddressTableCount = _A3ComSysBridgeAddressTableCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 4),
    _A3ComSysBridgeAddressTableCount_Type()
)
a3ComSysBridgeAddressTableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgeAddressTableCount.setStatus("mandatory")
_A3ComSysBridgeAddressTablePeakCount_Type = Integer32
_A3ComSysBridgeAddressTablePeakCount_Object = MibTableColumn
a3ComSysBridgeAddressTablePeakCount = _A3ComSysBridgeAddressTablePeakCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 5),
    _A3ComSysBridgeAddressTablePeakCount_Type()
)
a3ComSysBridgeAddressTablePeakCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgeAddressTablePeakCount.setStatus("mandatory")
_A3ComSysBridgeAddressThreshold_Type = Integer32
_A3ComSysBridgeAddressThreshold_Object = MibTableColumn
a3ComSysBridgeAddressThreshold = _A3ComSysBridgeAddressThreshold_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 6),
    _A3ComSysBridgeAddressThreshold_Type()
)
a3ComSysBridgeAddressThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeAddressThreshold.setStatus("mandatory")


class _A3ComSysBridgeMode_Type(Integer32):
    """Custom type a3ComSysBridgeMode based on Integer32"""
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
        *(("expressMode", 1),
          ("ibmSRBridgeMode", 6),
          ("ieee8021dBridgeMode", 2),
          ("ieee8021dSRBridgeMode", 5),
          ("ieee8021dSRTBridgeMode", 4),
          ("notSupported", 3),
          ("srExpressBridgeMode", 8),
          ("srtBBridgeMode", 7))
    )


_A3ComSysBridgeMode_Type.__name__ = "Integer32"
_A3ComSysBridgeMode_Object = MibTableColumn
a3ComSysBridgeMode = _A3ComSysBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 7),
    _A3ComSysBridgeMode_Type()
)
a3ComSysBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeMode.setStatus("mandatory")
_A3ComSysBridgeBackbonePort_Type = Integer32
_A3ComSysBridgeBackbonePort_Object = MibTableColumn
a3ComSysBridgeBackbonePort = _A3ComSysBridgeBackbonePort_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 8),
    _A3ComSysBridgeBackbonePort_Type()
)
a3ComSysBridgeBackbonePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeBackbonePort.setStatus("mandatory")


class _A3ComSysBridgeIpFragmentationEnabled_Type(Integer32):
    """Custom type a3ComSysBridgeIpFragmentationEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notSupported", 3),
          ("true", 1))
    )


_A3ComSysBridgeIpFragmentationEnabled_Type.__name__ = "Integer32"
_A3ComSysBridgeIpFragmentationEnabled_Object = MibTableColumn
a3ComSysBridgeIpFragmentationEnabled = _A3ComSysBridgeIpFragmentationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 9),
    _A3ComSysBridgeIpFragmentationEnabled_Type()
)
a3ComSysBridgeIpFragmentationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeIpFragmentationEnabled.setStatus("mandatory")


class _A3ComSysBridgeTrFddiTranslationMode_Type(Integer32):
    """Custom type a3ComSysBridgeTrFddiTranslationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backbone", 2),
          ("native", 1))
    )


_A3ComSysBridgeTrFddiTranslationMode_Type.__name__ = "Integer32"
_A3ComSysBridgeTrFddiTranslationMode_Object = MibTableColumn
a3ComSysBridgeTrFddiTranslationMode = _A3ComSysBridgeTrFddiTranslationMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 10),
    _A3ComSysBridgeTrFddiTranslationMode_Type()
)
a3ComSysBridgeTrFddiTranslationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeTrFddiTranslationMode.setStatus("mandatory")


class _A3ComSysBridgeSTPGroupAddress_Type(OctetString):
    """Custom type a3ComSysBridgeSTPGroupAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_A3ComSysBridgeSTPGroupAddress_Type.__name__ = "OctetString"
_A3ComSysBridgeSTPGroupAddress_Object = MibTableColumn
a3ComSysBridgeSTPGroupAddress = _A3ComSysBridgeSTPGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 11),
    _A3ComSysBridgeSTPGroupAddress_Type()
)
a3ComSysBridgeSTPGroupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeSTPGroupAddress.setStatus("mandatory")


class _A3ComSysBridgeSTPEnable_Type(Integer32):
    """Custom type a3ComSysBridgeSTPEnable based on Integer32"""
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


_A3ComSysBridgeSTPEnable_Type.__name__ = "Integer32"
_A3ComSysBridgeSTPEnable_Object = MibTableColumn
a3ComSysBridgeSTPEnable = _A3ComSysBridgeSTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 12),
    _A3ComSysBridgeSTPEnable_Type()
)
a3ComSysBridgeSTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeSTPEnable.setStatus("mandatory")


class _A3ComSysBridgeIpxSnapTranslationEnable_Type(Integer32):
    """Custom type a3ComSysBridgeIpxSnapTranslationEnable based on Integer32"""
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


_A3ComSysBridgeIpxSnapTranslationEnable_Type.__name__ = "Integer32"
_A3ComSysBridgeIpxSnapTranslationEnable_Object = MibTableColumn
a3ComSysBridgeIpxSnapTranslationEnable = _A3ComSysBridgeIpxSnapTranslationEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 13),
    _A3ComSysBridgeIpxSnapTranslationEnable_Type()
)
a3ComSysBridgeIpxSnapTranslationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeIpxSnapTranslationEnable.setStatus("mandatory")


class _A3ComSysBridgeLowLatencyEnable_Type(Integer32):
    """Custom type a3ComSysBridgeLowLatencyEnable based on Integer32"""
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


_A3ComSysBridgeLowLatencyEnable_Type.__name__ = "Integer32"
_A3ComSysBridgeLowLatencyEnable_Object = MibTableColumn
a3ComSysBridgeLowLatencyEnable = _A3ComSysBridgeLowLatencyEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 14),
    _A3ComSysBridgeLowLatencyEnable_Type()
)
a3ComSysBridgeLowLatencyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeLowLatencyEnable.setStatus("mandatory")


class _A3ComSysBridgeVlanMode_Type(Integer32):
    """Custom type a3ComSysBridgeVlanMode based on Integer32"""
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
        *(("closed", 2),
          ("mixed", 3),
          ("notSupported", 4),
          ("open", 1))
    )


_A3ComSysBridgeVlanMode_Type.__name__ = "Integer32"
_A3ComSysBridgeVlanMode_Object = MibTableColumn
a3ComSysBridgeVlanMode = _A3ComSysBridgeVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 15),
    _A3ComSysBridgeVlanMode_Type()
)
a3ComSysBridgeVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeVlanMode.setStatus("mandatory")


class _A3ComSysBridgeRateLimitReceiveMulticast_Type(Integer32):
    """Custom type a3ComSysBridgeRateLimitReceiveMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComSysBridgeRateLimitReceiveMulticast_Type.__name__ = "Integer32"
_A3ComSysBridgeRateLimitReceiveMulticast_Object = MibTableColumn
a3ComSysBridgeRateLimitReceiveMulticast = _A3ComSysBridgeRateLimitReceiveMulticast_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 16),
    _A3ComSysBridgeRateLimitReceiveMulticast_Type()
)
a3ComSysBridgeRateLimitReceiveMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeRateLimitReceiveMulticast.setStatus("mandatory")


class _A3ComSysBridgeRateLimitReceiveBroadcast_Type(Integer32):
    """Custom type a3ComSysBridgeRateLimitReceiveBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComSysBridgeRateLimitReceiveBroadcast_Type.__name__ = "Integer32"
_A3ComSysBridgeRateLimitReceiveBroadcast_Object = MibTableColumn
a3ComSysBridgeRateLimitReceiveBroadcast = _A3ComSysBridgeRateLimitReceiveBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 17),
    _A3ComSysBridgeRateLimitReceiveBroadcast_Type()
)
a3ComSysBridgeRateLimitReceiveBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeRateLimitReceiveBroadcast.setStatus("mandatory")


class _A3ComSysBridgeRateLimitReceiveFlood_Type(Integer32):
    """Custom type a3ComSysBridgeRateLimitReceiveFlood based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComSysBridgeRateLimitReceiveFlood_Type.__name__ = "Integer32"
_A3ComSysBridgeRateLimitReceiveFlood_Object = MibTableColumn
a3ComSysBridgeRateLimitReceiveFlood = _A3ComSysBridgeRateLimitReceiveFlood_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 18),
    _A3ComSysBridgeRateLimitReceiveFlood_Type()
)
a3ComSysBridgeRateLimitReceiveFlood.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeRateLimitReceiveFlood.setStatus("mandatory")


class _A3ComSysBridgeAddressLearnMode_Type(Integer32):
    """Custom type a3ComSysBridgeAddressLearnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("secure", 2))
    )


_A3ComSysBridgeAddressLearnMode_Type.__name__ = "Integer32"
_A3ComSysBridgeAddressLearnMode_Object = MibTableColumn
a3ComSysBridgeAddressLearnMode = _A3ComSysBridgeAddressLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 19),
    _A3ComSysBridgeAddressLearnMode_Type()
)
a3ComSysBridgeAddressLearnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeAddressLearnMode.setStatus("mandatory")


class _A3ComSysBridgeAddressAgingInterval_Type(Integer32):
    """Custom type a3ComSysBridgeAddressAgingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComSysBridgeAddressAgingInterval_Type.__name__ = "Integer32"
_A3ComSysBridgeAddressAgingInterval_Object = MibTableColumn
a3ComSysBridgeAddressAgingInterval = _A3ComSysBridgeAddressAgingInterval_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 20),
    _A3ComSysBridgeAddressAgingInterval_Type()
)
a3ComSysBridgeAddressAgingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeAddressAgingInterval.setStatus("mandatory")


class _A3ComSysBridgeLoopDetectMode_Type(Integer32):
    """Custom type a3ComSysBridgeLoopDetectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("immediate", 3))
    )


_A3ComSysBridgeLoopDetectMode_Type.__name__ = "Integer32"
_A3ComSysBridgeLoopDetectMode_Object = MibTableColumn
a3ComSysBridgeLoopDetectMode = _A3ComSysBridgeLoopDetectMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 21),
    _A3ComSysBridgeLoopDetectMode_Type()
)
a3ComSysBridgeLoopDetectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeLoopDetectMode.setStatus("mandatory")
_A3ComSysBridgeLoopDetectSrcAddress_Type = OctetString
_A3ComSysBridgeLoopDetectSrcAddress_Object = MibTableColumn
a3ComSysBridgeLoopDetectSrcAddress = _A3ComSysBridgeLoopDetectSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 2, 1, 22),
    _A3ComSysBridgeLoopDetectSrcAddress_Type()
)
a3ComSysBridgeLoopDetectSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgeLoopDetectSrcAddress.setStatus("mandatory")
_A3ComSysBridgePortTable_Object = MibTable
a3ComSysBridgePortTable = _A3ComSysBridgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3)
)
if mibBuilder.loadTexts:
    a3ComSysBridgePortTable.setStatus("mandatory")
_A3ComSysBridgePortEntry_Object = MibTableRow
a3ComSysBridgePortEntry = _A3ComSysBridgePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1)
)
a3ComSysBridgePortEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-BRIDGE-MIB", "a3ComSysBridgePortBridgeIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-BRIDGE-MIB", "a3ComSysBridgePortIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysBridgePortEntry.setStatus("mandatory")


class _A3ComSysBridgePortBridgeIndex_Type(Integer32):
    """Custom type a3ComSysBridgePortBridgeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComSysBridgePortBridgeIndex_Type.__name__ = "Integer32"
_A3ComSysBridgePortBridgeIndex_Object = MibTableColumn
a3ComSysBridgePortBridgeIndex = _A3ComSysBridgePortBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 1),
    _A3ComSysBridgePortBridgeIndex_Type()
)
a3ComSysBridgePortBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortBridgeIndex.setStatus("mandatory")


class _A3ComSysBridgePortIndex_Type(Integer32):
    """Custom type a3ComSysBridgePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComSysBridgePortIndex_Type.__name__ = "Integer32"
_A3ComSysBridgePortIndex_Object = MibTableColumn
a3ComSysBridgePortIndex = _A3ComSysBridgePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 2),
    _A3ComSysBridgePortIndex_Type()
)
a3ComSysBridgePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortIndex.setStatus("mandatory")


class _A3ComSysBridgePortIfIndex_Type(Integer32):
    """Custom type a3ComSysBridgePortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComSysBridgePortIfIndex_Type.__name__ = "Integer32"
_A3ComSysBridgePortIfIndex_Object = MibTableColumn
a3ComSysBridgePortIfIndex = _A3ComSysBridgePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 3),
    _A3ComSysBridgePortIfIndex_Type()
)
a3ComSysBridgePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortIfIndex.setStatus("mandatory")


class _A3ComSysBridgePortReceiveMulticastLimit_Type(Integer32):
    """Custom type a3ComSysBridgePortReceiveMulticastLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_A3ComSysBridgePortReceiveMulticastLimit_Type.__name__ = "Integer32"
_A3ComSysBridgePortReceiveMulticastLimit_Object = MibTableColumn
a3ComSysBridgePortReceiveMulticastLimit = _A3ComSysBridgePortReceiveMulticastLimit_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 4),
    _A3ComSysBridgePortReceiveMulticastLimit_Type()
)
a3ComSysBridgePortReceiveMulticastLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgePortReceiveMulticastLimit.setStatus("mandatory")


class _A3ComSysBridgePortAddressAction_Type(Integer32):
    """Custom type a3ComSysBridgePortAddressAction based on Integer32"""
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
        *(("flushAddress", 3),
          ("flushDynamicAddress", 4),
          ("freezeAddress", 2),
          ("other", 1))
    )


_A3ComSysBridgePortAddressAction_Type.__name__ = "Integer32"
_A3ComSysBridgePortAddressAction_Object = MibTableColumn
a3ComSysBridgePortAddressAction = _A3ComSysBridgePortAddressAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 5),
    _A3ComSysBridgePortAddressAction_Type()
)
a3ComSysBridgePortAddressAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgePortAddressAction.setStatus("mandatory")
_A3ComSysBridgePortSpanningTreeFrameReceivedCounts_Type = Counter32
_A3ComSysBridgePortSpanningTreeFrameReceivedCounts_Object = MibTableColumn
a3ComSysBridgePortSpanningTreeFrameReceivedCounts = _A3ComSysBridgePortSpanningTreeFrameReceivedCounts_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 6),
    _A3ComSysBridgePortSpanningTreeFrameReceivedCounts_Type()
)
a3ComSysBridgePortSpanningTreeFrameReceivedCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortSpanningTreeFrameReceivedCounts.setStatus("mandatory")
_A3ComSysBridgePortReceiveBlockedDiscards_Type = Counter32
_A3ComSysBridgePortReceiveBlockedDiscards_Object = MibTableColumn
a3ComSysBridgePortReceiveBlockedDiscards = _A3ComSysBridgePortReceiveBlockedDiscards_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 7),
    _A3ComSysBridgePortReceiveBlockedDiscards_Type()
)
a3ComSysBridgePortReceiveBlockedDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortReceiveBlockedDiscards.setStatus("mandatory")
_A3ComSysBridgePortReceiveMulticastLimitExceededs_Type = Counter32
_A3ComSysBridgePortReceiveMulticastLimitExceededs_Object = MibTableColumn
a3ComSysBridgePortReceiveMulticastLimitExceededs = _A3ComSysBridgePortReceiveMulticastLimitExceededs_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 8),
    _A3ComSysBridgePortReceiveMulticastLimitExceededs_Type()
)
a3ComSysBridgePortReceiveMulticastLimitExceededs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortReceiveMulticastLimitExceededs.setStatus("mandatory")
_A3ComSysBridgePortReceiveMulticastLimitExceededDiscards_Type = Counter32
_A3ComSysBridgePortReceiveMulticastLimitExceededDiscards_Object = MibTableColumn
a3ComSysBridgePortReceiveMulticastLimitExceededDiscards = _A3ComSysBridgePortReceiveMulticastLimitExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 9),
    _A3ComSysBridgePortReceiveMulticastLimitExceededDiscards_Type()
)
a3ComSysBridgePortReceiveMulticastLimitExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortReceiveMulticastLimitExceededDiscards.setStatus("mandatory")
_A3ComSysBridgePortReceiveSecurityDiscards_Type = Counter32
_A3ComSysBridgePortReceiveSecurityDiscards_Object = MibTableColumn
a3ComSysBridgePortReceiveSecurityDiscards = _A3ComSysBridgePortReceiveSecurityDiscards_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 10),
    _A3ComSysBridgePortReceiveSecurityDiscards_Type()
)
a3ComSysBridgePortReceiveSecurityDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortReceiveSecurityDiscards.setStatus("mandatory")
_A3ComSysBridgePortReceiveUnknownDiscards_Type = Counter32
_A3ComSysBridgePortReceiveUnknownDiscards_Object = MibTableColumn
a3ComSysBridgePortReceiveUnknownDiscards = _A3ComSysBridgePortReceiveUnknownDiscards_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 11),
    _A3ComSysBridgePortReceiveUnknownDiscards_Type()
)
a3ComSysBridgePortReceiveUnknownDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortReceiveUnknownDiscards.setStatus("mandatory")
_A3ComSysBridgePortReceiveOtherDiscards_Type = Counter32
_A3ComSysBridgePortReceiveOtherDiscards_Object = MibTableColumn
a3ComSysBridgePortReceiveOtherDiscards = _A3ComSysBridgePortReceiveOtherDiscards_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 12),
    _A3ComSysBridgePortReceiveOtherDiscards_Type()
)
a3ComSysBridgePortReceiveOtherDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortReceiveOtherDiscards.setStatus("mandatory")
_A3ComSysBridgePortReceiveErrorDiscards_Type = Counter32
_A3ComSysBridgePortReceiveErrorDiscards_Object = MibTableColumn
a3ComSysBridgePortReceiveErrorDiscards = _A3ComSysBridgePortReceiveErrorDiscards_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 13),
    _A3ComSysBridgePortReceiveErrorDiscards_Type()
)
a3ComSysBridgePortReceiveErrorDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortReceiveErrorDiscards.setStatus("mandatory")
_A3ComSysBridgePortSameSegmentDiscards_Type = Counter32
_A3ComSysBridgePortSameSegmentDiscards_Object = MibTableColumn
a3ComSysBridgePortSameSegmentDiscards = _A3ComSysBridgePortSameSegmentDiscards_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 14),
    _A3ComSysBridgePortSameSegmentDiscards_Type()
)
a3ComSysBridgePortSameSegmentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortSameSegmentDiscards.setStatus("mandatory")
_A3ComSysBridgePortTransmitBlockedDiscards_Type = Counter32
_A3ComSysBridgePortTransmitBlockedDiscards_Object = MibTableColumn
a3ComSysBridgePortTransmitBlockedDiscards = _A3ComSysBridgePortTransmitBlockedDiscards_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 15),
    _A3ComSysBridgePortTransmitBlockedDiscards_Type()
)
a3ComSysBridgePortTransmitBlockedDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortTransmitBlockedDiscards.setStatus("mandatory")
_A3ComSysBridgePortReceiveAllPathFilteredFrames_Type = Counter32
_A3ComSysBridgePortReceiveAllPathFilteredFrames_Object = MibTableColumn
a3ComSysBridgePortReceiveAllPathFilteredFrames = _A3ComSysBridgePortReceiveAllPathFilteredFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 16),
    _A3ComSysBridgePortReceiveAllPathFilteredFrames_Type()
)
a3ComSysBridgePortReceiveAllPathFilteredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortReceiveAllPathFilteredFrames.setStatus("mandatory")
_A3ComSysBridgePortReceiveMulticastPathFilteredFrames_Type = Counter32
_A3ComSysBridgePortReceiveMulticastPathFilteredFrames_Object = MibTableColumn
a3ComSysBridgePortReceiveMulticastPathFilteredFrames = _A3ComSysBridgePortReceiveMulticastPathFilteredFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 17),
    _A3ComSysBridgePortReceiveMulticastPathFilteredFrames_Type()
)
a3ComSysBridgePortReceiveMulticastPathFilteredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortReceiveMulticastPathFilteredFrames.setStatus("mandatory")
_A3ComSysBridgePortTransmitAllPathFilteredFrames_Type = Counter32
_A3ComSysBridgePortTransmitAllPathFilteredFrames_Object = MibTableColumn
a3ComSysBridgePortTransmitAllPathFilteredFrames = _A3ComSysBridgePortTransmitAllPathFilteredFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 18),
    _A3ComSysBridgePortTransmitAllPathFilteredFrames_Type()
)
a3ComSysBridgePortTransmitAllPathFilteredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortTransmitAllPathFilteredFrames.setStatus("mandatory")
_A3ComSysBridgePortTransmitMulticastPathFilteredFrames_Type = Counter32
_A3ComSysBridgePortTransmitMulticastPathFilteredFrames_Object = MibTableColumn
a3ComSysBridgePortTransmitMulticastPathFilteredFrames = _A3ComSysBridgePortTransmitMulticastPathFilteredFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 19),
    _A3ComSysBridgePortTransmitMulticastPathFilteredFrames_Type()
)
a3ComSysBridgePortTransmitMulticastPathFilteredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortTransmitMulticastPathFilteredFrames.setStatus("mandatory")
_A3ComSysBridgePortForwardedUnicastFrames_Type = Counter32
_A3ComSysBridgePortForwardedUnicastFrames_Object = MibTableColumn
a3ComSysBridgePortForwardedUnicastFrames = _A3ComSysBridgePortForwardedUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 20),
    _A3ComSysBridgePortForwardedUnicastFrames_Type()
)
a3ComSysBridgePortForwardedUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortForwardedUnicastFrames.setStatus("mandatory")
_A3ComSysBridgePortForwardedUnicastOctets_Type = Counter32
_A3ComSysBridgePortForwardedUnicastOctets_Object = MibTableColumn
a3ComSysBridgePortForwardedUnicastOctets = _A3ComSysBridgePortForwardedUnicastOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 21),
    _A3ComSysBridgePortForwardedUnicastOctets_Type()
)
a3ComSysBridgePortForwardedUnicastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortForwardedUnicastOctets.setStatus("mandatory")
_A3ComSysBridgePortForwardedMulticastFrames_Type = Counter32
_A3ComSysBridgePortForwardedMulticastFrames_Object = MibTableColumn
a3ComSysBridgePortForwardedMulticastFrames = _A3ComSysBridgePortForwardedMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 22),
    _A3ComSysBridgePortForwardedMulticastFrames_Type()
)
a3ComSysBridgePortForwardedMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortForwardedMulticastFrames.setStatus("mandatory")
_A3ComSysBridgePortForwardedMulticastOctets_Type = Counter32
_A3ComSysBridgePortForwardedMulticastOctets_Object = MibTableColumn
a3ComSysBridgePortForwardedMulticastOctets = _A3ComSysBridgePortForwardedMulticastOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 23),
    _A3ComSysBridgePortForwardedMulticastOctets_Type()
)
a3ComSysBridgePortForwardedMulticastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortForwardedMulticastOctets.setStatus("mandatory")
_A3ComSysBridgePortFloodedUnicastFrames_Type = Counter32
_A3ComSysBridgePortFloodedUnicastFrames_Object = MibTableColumn
a3ComSysBridgePortFloodedUnicastFrames = _A3ComSysBridgePortFloodedUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 24),
    _A3ComSysBridgePortFloodedUnicastFrames_Type()
)
a3ComSysBridgePortFloodedUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortFloodedUnicastFrames.setStatus("mandatory")
_A3ComSysBridgePortFloodedUnicastOctets_Type = Counter32
_A3ComSysBridgePortFloodedUnicastOctets_Object = MibTableColumn
a3ComSysBridgePortFloodedUnicastOctets = _A3ComSysBridgePortFloodedUnicastOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 25),
    _A3ComSysBridgePortFloodedUnicastOctets_Type()
)
a3ComSysBridgePortFloodedUnicastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortFloodedUnicastOctets.setStatus("mandatory")


class _A3ComSysBridgePortStpMode_Type(Integer32):
    """Custom type a3ComSysBridgePortStpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("remove", 3))
    )


_A3ComSysBridgePortStpMode_Type.__name__ = "Integer32"
_A3ComSysBridgePortStpMode_Object = MibTableColumn
a3ComSysBridgePortStpMode = _A3ComSysBridgePortStpMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 26),
    _A3ComSysBridgePortStpMode_Type()
)
a3ComSysBridgePortStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgePortStpMode.setStatus("mandatory")


class _A3ComSysBridgePortReceiveMulticastLimitFrameType_Type(Integer32):
    """Custom type a3ComSysBridgePortReceiveMulticastLimitFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadcastAndMulticast", 1),
          ("broadcastOnly", 2))
    )


_A3ComSysBridgePortReceiveMulticastLimitFrameType_Type.__name__ = "Integer32"
_A3ComSysBridgePortReceiveMulticastLimitFrameType_Object = MibTableColumn
a3ComSysBridgePortReceiveMulticastLimitFrameType = _A3ComSysBridgePortReceiveMulticastLimitFrameType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 27),
    _A3ComSysBridgePortReceiveMulticastLimitFrameType_Type()
)
a3ComSysBridgePortReceiveMulticastLimitFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgePortReceiveMulticastLimitFrameType.setStatus("mandatory")
_A3ComSysBridgePortForwardedFrames_Type = Counter32
_A3ComSysBridgePortForwardedFrames_Object = MibTableColumn
a3ComSysBridgePortForwardedFrames = _A3ComSysBridgePortForwardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 28),
    _A3ComSysBridgePortForwardedFrames_Type()
)
a3ComSysBridgePortForwardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortForwardedFrames.setStatus("mandatory")
_A3ComSysBridgePortReceiveMulticastLimitMultiplier_Type = Integer32
_A3ComSysBridgePortReceiveMulticastLimitMultiplier_Object = MibTableColumn
a3ComSysBridgePortReceiveMulticastLimitMultiplier = _A3ComSysBridgePortReceiveMulticastLimitMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 29),
    _A3ComSysBridgePortReceiveMulticastLimitMultiplier_Type()
)
a3ComSysBridgePortReceiveMulticastLimitMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortReceiveMulticastLimitMultiplier.setStatus("mandatory")


class _A3ComSysBridgePortRateLimitReceiveMulticastEnabled_Type(Integer32):
    """Custom type a3ComSysBridgePortRateLimitReceiveMulticastEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_A3ComSysBridgePortRateLimitReceiveMulticastEnabled_Type.__name__ = "Integer32"
_A3ComSysBridgePortRateLimitReceiveMulticastEnabled_Object = MibTableColumn
a3ComSysBridgePortRateLimitReceiveMulticastEnabled = _A3ComSysBridgePortRateLimitReceiveMulticastEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 30),
    _A3ComSysBridgePortRateLimitReceiveMulticastEnabled_Type()
)
a3ComSysBridgePortRateLimitReceiveMulticastEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgePortRateLimitReceiveMulticastEnabled.setStatus("mandatory")


class _A3ComSysBridgePortRateLimitReceiveBroadcastEnabled_Type(Integer32):
    """Custom type a3ComSysBridgePortRateLimitReceiveBroadcastEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_A3ComSysBridgePortRateLimitReceiveBroadcastEnabled_Type.__name__ = "Integer32"
_A3ComSysBridgePortRateLimitReceiveBroadcastEnabled_Object = MibTableColumn
a3ComSysBridgePortRateLimitReceiveBroadcastEnabled = _A3ComSysBridgePortRateLimitReceiveBroadcastEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 31),
    _A3ComSysBridgePortRateLimitReceiveBroadcastEnabled_Type()
)
a3ComSysBridgePortRateLimitReceiveBroadcastEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgePortRateLimitReceiveBroadcastEnabled.setStatus("mandatory")


class _A3ComSysBridgePortRateLimitReceiveFloodEnabled_Type(Integer32):
    """Custom type a3ComSysBridgePortRateLimitReceiveFloodEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_A3ComSysBridgePortRateLimitReceiveFloodEnabled_Type.__name__ = "Integer32"
_A3ComSysBridgePortRateLimitReceiveFloodEnabled_Object = MibTableColumn
a3ComSysBridgePortRateLimitReceiveFloodEnabled = _A3ComSysBridgePortRateLimitReceiveFloodEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 32),
    _A3ComSysBridgePortRateLimitReceiveFloodEnabled_Type()
)
a3ComSysBridgePortRateLimitReceiveFloodEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgePortRateLimitReceiveFloodEnabled.setStatus("mandatory")


class _A3ComSysBridgePortRateLimitReceiveState_Type(Integer32):
    """Custom type a3ComSysBridgePortRateLimitReceiveState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bmfrl-disabled", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_A3ComSysBridgePortRateLimitReceiveState_Type.__name__ = "Integer32"
_A3ComSysBridgePortRateLimitReceiveState_Object = MibTableColumn
a3ComSysBridgePortRateLimitReceiveState = _A3ComSysBridgePortRateLimitReceiveState_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 33),
    _A3ComSysBridgePortRateLimitReceiveState_Type()
)
a3ComSysBridgePortRateLimitReceiveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortRateLimitReceiveState.setStatus("mandatory")


class _A3ComSysBridgePortLoopDetectState_Type(Integer32):
    """Custom type a3ComSysBridgePortLoopDetectState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("bpduDetected", 3),
          ("loopDetected", 2))
    )


_A3ComSysBridgePortLoopDetectState_Type.__name__ = "Integer32"
_A3ComSysBridgePortLoopDetectState_Object = MibTableColumn
a3ComSysBridgePortLoopDetectState = _A3ComSysBridgePortLoopDetectState_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 34),
    _A3ComSysBridgePortLoopDetectState_Type()
)
a3ComSysBridgePortLoopDetectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortLoopDetectState.setStatus("mandatory")


class _A3ComSysBridgePortAddressMaxLimit_Type(Integer32):
    """Custom type a3ComSysBridgePortAddressMaxLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComSysBridgePortAddressMaxLimit_Type.__name__ = "Integer32"
_A3ComSysBridgePortAddressMaxLimit_Object = MibTableColumn
a3ComSysBridgePortAddressMaxLimit = _A3ComSysBridgePortAddressMaxLimit_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 35),
    _A3ComSysBridgePortAddressMaxLimit_Type()
)
a3ComSysBridgePortAddressMaxLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgePortAddressMaxLimit.setStatus("mandatory")


class _A3ComSysBridgePortAddressState_Type(Integer32):
    """Custom type a3ComSysBridgePortAddressState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("limitationExceeded", 2),
          ("securityViolation", 3))
    )


_A3ComSysBridgePortAddressState_Type.__name__ = "Integer32"
_A3ComSysBridgePortAddressState_Object = MibTableColumn
a3ComSysBridgePortAddressState = _A3ComSysBridgePortAddressState_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 36),
    _A3ComSysBridgePortAddressState_Type()
)
a3ComSysBridgePortAddressState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortAddressState.setStatus("mandatory")
_A3ComSysBridgePortReceiveInternalPathFilteredFrames_Type = Counter32
_A3ComSysBridgePortReceiveInternalPathFilteredFrames_Object = MibTableColumn
a3ComSysBridgePortReceiveInternalPathFilteredFrames = _A3ComSysBridgePortReceiveInternalPathFilteredFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 3, 1, 37),
    _A3ComSysBridgePortReceiveInternalPathFilteredFrames_Type()
)
a3ComSysBridgePortReceiveInternalPathFilteredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortReceiveInternalPathFilteredFrames.setStatus("mandatory")
_A3ComSysBridgePortAddressTable_Object = MibTable
a3ComSysBridgePortAddressTable = _A3ComSysBridgePortAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 5)
)
if mibBuilder.loadTexts:
    a3ComSysBridgePortAddressTable.setStatus("mandatory")
_A3ComSysBridgePortAddressEntry_Object = MibTableRow
a3ComSysBridgePortAddressEntry = _A3ComSysBridgePortAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 5, 1)
)
a3ComSysBridgePortAddressEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-BRIDGE-MIB", "a3ComSysBridgePortAddressBridgeIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-BRIDGE-MIB", "a3ComSysBridgePortAddressPortIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-BRIDGE-MIB", "a3ComSysBridgePortAddressIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysBridgePortAddressEntry.setStatus("mandatory")


class _A3ComSysBridgePortAddressBridgeIndex_Type(Integer32):
    """Custom type a3ComSysBridgePortAddressBridgeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComSysBridgePortAddressBridgeIndex_Type.__name__ = "Integer32"
_A3ComSysBridgePortAddressBridgeIndex_Object = MibTableColumn
a3ComSysBridgePortAddressBridgeIndex = _A3ComSysBridgePortAddressBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 5, 1, 1),
    _A3ComSysBridgePortAddressBridgeIndex_Type()
)
a3ComSysBridgePortAddressBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortAddressBridgeIndex.setStatus("mandatory")


class _A3ComSysBridgePortAddressPortIndex_Type(Integer32):
    """Custom type a3ComSysBridgePortAddressPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComSysBridgePortAddressPortIndex_Type.__name__ = "Integer32"
_A3ComSysBridgePortAddressPortIndex_Object = MibTableColumn
a3ComSysBridgePortAddressPortIndex = _A3ComSysBridgePortAddressPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 5, 1, 2),
    _A3ComSysBridgePortAddressPortIndex_Type()
)
a3ComSysBridgePortAddressPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortAddressPortIndex.setStatus("mandatory")


class _A3ComSysBridgePortAddressIndex_Type(Integer32):
    """Custom type a3ComSysBridgePortAddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComSysBridgePortAddressIndex_Type.__name__ = "Integer32"
_A3ComSysBridgePortAddressIndex_Object = MibTableColumn
a3ComSysBridgePortAddressIndex = _A3ComSysBridgePortAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 5, 1, 3),
    _A3ComSysBridgePortAddressIndex_Type()
)
a3ComSysBridgePortAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortAddressIndex.setStatus("mandatory")


class _A3ComSysBridgePortAddressRemoteAddress_Type(OctetString):
    """Custom type a3ComSysBridgePortAddressRemoteAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_A3ComSysBridgePortAddressRemoteAddress_Type.__name__ = "OctetString"
_A3ComSysBridgePortAddressRemoteAddress_Object = MibTableColumn
a3ComSysBridgePortAddressRemoteAddress = _A3ComSysBridgePortAddressRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 5, 1, 4),
    _A3ComSysBridgePortAddressRemoteAddress_Type()
)
a3ComSysBridgePortAddressRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgePortAddressRemoteAddress.setStatus("mandatory")


class _A3ComSysBridgePortAddressType_Type(Integer32):
    """Custom type a3ComSysBridgePortAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_A3ComSysBridgePortAddressType_Type.__name__ = "Integer32"
_A3ComSysBridgePortAddressType_Object = MibTableColumn
a3ComSysBridgePortAddressType = _A3ComSysBridgePortAddressType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 5, 1, 5),
    _A3ComSysBridgePortAddressType_Type()
)
a3ComSysBridgePortAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgePortAddressType.setStatus("mandatory")


class _A3ComSysBridgePortAddressIsStatic_Type(Integer32):
    """Custom type a3ComSysBridgePortAddressIsStatic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isDynamic", 2),
          ("isStatic", 1))
    )


_A3ComSysBridgePortAddressIsStatic_Type.__name__ = "Integer32"
_A3ComSysBridgePortAddressIsStatic_Object = MibTableColumn
a3ComSysBridgePortAddressIsStatic = _A3ComSysBridgePortAddressIsStatic_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 5, 1, 6),
    _A3ComSysBridgePortAddressIsStatic_Type()
)
a3ComSysBridgePortAddressIsStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgePortAddressIsStatic.setStatus("mandatory")
_A3ComSysBridgePortAddressStaticPort_Type = Integer32
_A3ComSysBridgePortAddressStaticPort_Object = MibTableColumn
a3ComSysBridgePortAddressStaticPort = _A3ComSysBridgePortAddressStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 5, 1, 7),
    _A3ComSysBridgePortAddressStaticPort_Type()
)
a3ComSysBridgePortAddressStaticPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortAddressStaticPort.setStatus("mandatory")
_A3ComSysBridgePortAddressAge_Type = Integer32
_A3ComSysBridgePortAddressAge_Object = MibTableColumn
a3ComSysBridgePortAddressAge = _A3ComSysBridgePortAddressAge_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 5, 1, 8),
    _A3ComSysBridgePortAddressAge_Type()
)
a3ComSysBridgePortAddressAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgePortAddressAge.setStatus("mandatory")


class _A3ComSysBridgeStpGroupAddress_Type(OctetString):
    """Custom type a3ComSysBridgeStpGroupAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_A3ComSysBridgeStpGroupAddress_Type.__name__ = "OctetString"
_A3ComSysBridgeStpGroupAddress_Object = MibScalar
a3ComSysBridgeStpGroupAddress = _A3ComSysBridgeStpGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 6),
    _A3ComSysBridgeStpGroupAddress_Type()
)
a3ComSysBridgeStpGroupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeStpGroupAddress.setStatus("obsolete")


class _A3ComSysBridgeStpEnable_Type(Integer32):
    """Custom type a3ComSysBridgeStpEnable based on Integer32"""
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


_A3ComSysBridgeStpEnable_Type.__name__ = "Integer32"
_A3ComSysBridgeStpEnable_Object = MibScalar
a3ComSysBridgeStpEnable = _A3ComSysBridgeStpEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 7),
    _A3ComSysBridgeStpEnable_Type()
)
a3ComSysBridgeStpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeStpEnable.setStatus("obsolete")
_A3ComSysBridgeVlanPortAddressTable_Object = MibTable
a3ComSysBridgeVlanPortAddressTable = _A3ComSysBridgeVlanPortAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 8)
)
if mibBuilder.loadTexts:
    a3ComSysBridgeVlanPortAddressTable.setStatus("mandatory")
_A3ComSysBridgeVlanPortAddressEntry_Object = MibTableRow
a3ComSysBridgeVlanPortAddressEntry = _A3ComSysBridgeVlanPortAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 8, 1)
)
a3ComSysBridgeVlanPortAddressEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-BRIDGE-MIB", "a3ComSysBridgeVlanPortAddressBridgeIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-BRIDGE-MIB", "a3ComSysBridgeVlanPortAddressVlanIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-BRIDGE-MIB", "a3ComSysBridgeVlanPortAddressPortIndex"),
    (0, "A3COM-SWITCHING-SYSTEMS-BRIDGE-MIB", "a3ComSysBridgeVlanPortAddressIndex"),
)
if mibBuilder.loadTexts:
    a3ComSysBridgeVlanPortAddressEntry.setStatus("mandatory")
_A3ComSysBridgeVlanPortAddressBridgeIndex_Type = Integer32
_A3ComSysBridgeVlanPortAddressBridgeIndex_Object = MibTableColumn
a3ComSysBridgeVlanPortAddressBridgeIndex = _A3ComSysBridgeVlanPortAddressBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 8, 1, 1),
    _A3ComSysBridgeVlanPortAddressBridgeIndex_Type()
)
a3ComSysBridgeVlanPortAddressBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgeVlanPortAddressBridgeIndex.setStatus("mandatory")
_A3ComSysBridgeVlanPortAddressVlanIndex_Type = Integer32
_A3ComSysBridgeVlanPortAddressVlanIndex_Object = MibTableColumn
a3ComSysBridgeVlanPortAddressVlanIndex = _A3ComSysBridgeVlanPortAddressVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 8, 1, 2),
    _A3ComSysBridgeVlanPortAddressVlanIndex_Type()
)
a3ComSysBridgeVlanPortAddressVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgeVlanPortAddressVlanIndex.setStatus("mandatory")
_A3ComSysBridgeVlanPortAddressPortIndex_Type = Integer32
_A3ComSysBridgeVlanPortAddressPortIndex_Object = MibTableColumn
a3ComSysBridgeVlanPortAddressPortIndex = _A3ComSysBridgeVlanPortAddressPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 8, 1, 3),
    _A3ComSysBridgeVlanPortAddressPortIndex_Type()
)
a3ComSysBridgeVlanPortAddressPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgeVlanPortAddressPortIndex.setStatus("mandatory")
_A3ComSysBridgeVlanPortAddressIndex_Type = Integer32
_A3ComSysBridgeVlanPortAddressIndex_Object = MibTableColumn
a3ComSysBridgeVlanPortAddressIndex = _A3ComSysBridgeVlanPortAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 8, 1, 4),
    _A3ComSysBridgeVlanPortAddressIndex_Type()
)
a3ComSysBridgeVlanPortAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgeVlanPortAddressIndex.setStatus("mandatory")


class _A3ComSysBridgeVlanPortAddressRemoteAddress_Type(OctetString):
    """Custom type a3ComSysBridgeVlanPortAddressRemoteAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_A3ComSysBridgeVlanPortAddressRemoteAddress_Type.__name__ = "OctetString"
_A3ComSysBridgeVlanPortAddressRemoteAddress_Object = MibTableColumn
a3ComSysBridgeVlanPortAddressRemoteAddress = _A3ComSysBridgeVlanPortAddressRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 8, 1, 5),
    _A3ComSysBridgeVlanPortAddressRemoteAddress_Type()
)
a3ComSysBridgeVlanPortAddressRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeVlanPortAddressRemoteAddress.setStatus("mandatory")


class _A3ComSysBridgeVlanPortAddressType_Type(Integer32):
    """Custom type a3ComSysBridgeVlanPortAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_A3ComSysBridgeVlanPortAddressType_Type.__name__ = "Integer32"
_A3ComSysBridgeVlanPortAddressType_Object = MibTableColumn
a3ComSysBridgeVlanPortAddressType = _A3ComSysBridgeVlanPortAddressType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 8, 1, 6),
    _A3ComSysBridgeVlanPortAddressType_Type()
)
a3ComSysBridgeVlanPortAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeVlanPortAddressType.setStatus("mandatory")


class _A3ComSysBridgeVlanPortAddressIsStatic_Type(Integer32):
    """Custom type a3ComSysBridgeVlanPortAddressIsStatic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isDynamic", 2),
          ("isStatic", 1))
    )


_A3ComSysBridgeVlanPortAddressIsStatic_Type.__name__ = "Integer32"
_A3ComSysBridgeVlanPortAddressIsStatic_Object = MibTableColumn
a3ComSysBridgeVlanPortAddressIsStatic = _A3ComSysBridgeVlanPortAddressIsStatic_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 8, 1, 7),
    _A3ComSysBridgeVlanPortAddressIsStatic_Type()
)
a3ComSysBridgeVlanPortAddressIsStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComSysBridgeVlanPortAddressIsStatic.setStatus("mandatory")
_A3ComSysBridgeVlanPortAddressStaticPort_Type = Integer32
_A3ComSysBridgeVlanPortAddressStaticPort_Object = MibTableColumn
a3ComSysBridgeVlanPortAddressStaticPort = _A3ComSysBridgeVlanPortAddressStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 8, 1, 8),
    _A3ComSysBridgeVlanPortAddressStaticPort_Type()
)
a3ComSysBridgeVlanPortAddressStaticPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgeVlanPortAddressStaticPort.setStatus("mandatory")
_A3ComSysBridgeVlanPortAddressAge_Type = Integer32
_A3ComSysBridgeVlanPortAddressAge_Object = MibTableColumn
a3ComSysBridgeVlanPortAddressAge = _A3ComSysBridgeVlanPortAddressAge_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 8, 1, 9),
    _A3ComSysBridgeVlanPortAddressAge_Type()
)
a3ComSysBridgeVlanPortAddressAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComSysBridgeVlanPortAddressAge.setStatus("mandatory")

# Managed Objects groups


# Notification objects

a3ComSysBridgeAddressThresholdEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 0, 6)
)
a3ComSysBridgeAddressThresholdEvent.setObjects(
    ("A3COM-SWITCHING-SYSTEMS-BRIDGE-MIB", "a3ComSysBridgeIndex")
)
if mibBuilder.loadTexts:
    a3ComSysBridgeAddressThresholdEvent.setStatus(
        ""
    )

a3ComSysBridgePortLearnEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 0, 60)
)
a3ComSysBridgePortLearnEvent.setObjects(
      *(("A3COM-SWITCHING-SYSTEMS-BRIDGE-MIB", "a3ComSysBridgePortIndex"),
        ("A3COM-SWITCHING-SYSTEMS-BRIDGE-MIB", "a3ComSysBridgePortAddressState"))
)
if mibBuilder.loadTexts:
    a3ComSysBridgePortLearnEvent.setStatus(
        ""
    )

a3ComSysBridgePortRateLimitEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 0, 61)
)
a3ComSysBridgePortRateLimitEvent.setObjects(
      *(("A3COM-SWITCHING-SYSTEMS-BRIDGE-MIB", "a3ComSysBridgePortIndex"),
        ("A3COM-SWITCHING-SYSTEMS-BRIDGE-MIB", "a3ComSysBridgePortRateLimitReceiveState"))
)
if mibBuilder.loadTexts:
    a3ComSysBridgePortRateLimitEvent.setStatus(
        ""
    )

a3ComSysBridgePortLoopDetectEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 10, 0, 62)
)
a3ComSysBridgePortLoopDetectEvent.setObjects(
      *(("A3COM-SWITCHING-SYSTEMS-BRIDGE-MIB", "a3ComSysBridgePortIndex"),
        ("A3COM-SWITCHING-SYSTEMS-BRIDGE-MIB", "a3ComSysBridgePortLoopDetectState"))
)
if mibBuilder.loadTexts:
    a3ComSysBridgePortLoopDetectEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-SWITCHING-SYSTEMS-BRIDGE-MIB",
    **{"a3Com": a3Com,
       "switchingSystemsMibs": switchingSystemsMibs,
       "a3ComSwitchingSystemsMib": a3ComSwitchingSystemsMib,
       "a3ComSysBridgeAddressThresholdEvent": a3ComSysBridgeAddressThresholdEvent,
       "a3ComSysBridge": a3ComSysBridge,
       "a3ComSysBridgePortLearnEvent": a3ComSysBridgePortLearnEvent,
       "a3ComSysBridgePortRateLimitEvent": a3ComSysBridgePortRateLimitEvent,
       "a3ComSysBridgePortLoopDetectEvent": a3ComSysBridgePortLoopDetectEvent,
       "a3ComSysBridgeCount": a3ComSysBridgeCount,
       "a3ComSysBridgeTable": a3ComSysBridgeTable,
       "a3ComSysBridgeEntry": a3ComSysBridgeEntry,
       "a3ComSysBridgeIndex": a3ComSysBridgeIndex,
       "a3ComSysBridgePortCount": a3ComSysBridgePortCount,
       "a3ComSysBridgeAddressTableSize": a3ComSysBridgeAddressTableSize,
       "a3ComSysBridgeAddressTableCount": a3ComSysBridgeAddressTableCount,
       "a3ComSysBridgeAddressTablePeakCount": a3ComSysBridgeAddressTablePeakCount,
       "a3ComSysBridgeAddressThreshold": a3ComSysBridgeAddressThreshold,
       "a3ComSysBridgeMode": a3ComSysBridgeMode,
       "a3ComSysBridgeBackbonePort": a3ComSysBridgeBackbonePort,
       "a3ComSysBridgeIpFragmentationEnabled": a3ComSysBridgeIpFragmentationEnabled,
       "a3ComSysBridgeTrFddiTranslationMode": a3ComSysBridgeTrFddiTranslationMode,
       "a3ComSysBridgeSTPGroupAddress": a3ComSysBridgeSTPGroupAddress,
       "a3ComSysBridgeSTPEnable": a3ComSysBridgeSTPEnable,
       "a3ComSysBridgeIpxSnapTranslationEnable": a3ComSysBridgeIpxSnapTranslationEnable,
       "a3ComSysBridgeLowLatencyEnable": a3ComSysBridgeLowLatencyEnable,
       "a3ComSysBridgeVlanMode": a3ComSysBridgeVlanMode,
       "a3ComSysBridgeRateLimitReceiveMulticast": a3ComSysBridgeRateLimitReceiveMulticast,
       "a3ComSysBridgeRateLimitReceiveBroadcast": a3ComSysBridgeRateLimitReceiveBroadcast,
       "a3ComSysBridgeRateLimitReceiveFlood": a3ComSysBridgeRateLimitReceiveFlood,
       "a3ComSysBridgeAddressLearnMode": a3ComSysBridgeAddressLearnMode,
       "a3ComSysBridgeAddressAgingInterval": a3ComSysBridgeAddressAgingInterval,
       "a3ComSysBridgeLoopDetectMode": a3ComSysBridgeLoopDetectMode,
       "a3ComSysBridgeLoopDetectSrcAddress": a3ComSysBridgeLoopDetectSrcAddress,
       "a3ComSysBridgePortTable": a3ComSysBridgePortTable,
       "a3ComSysBridgePortEntry": a3ComSysBridgePortEntry,
       "a3ComSysBridgePortBridgeIndex": a3ComSysBridgePortBridgeIndex,
       "a3ComSysBridgePortIndex": a3ComSysBridgePortIndex,
       "a3ComSysBridgePortIfIndex": a3ComSysBridgePortIfIndex,
       "a3ComSysBridgePortReceiveMulticastLimit": a3ComSysBridgePortReceiveMulticastLimit,
       "a3ComSysBridgePortAddressAction": a3ComSysBridgePortAddressAction,
       "a3ComSysBridgePortSpanningTreeFrameReceivedCounts": a3ComSysBridgePortSpanningTreeFrameReceivedCounts,
       "a3ComSysBridgePortReceiveBlockedDiscards": a3ComSysBridgePortReceiveBlockedDiscards,
       "a3ComSysBridgePortReceiveMulticastLimitExceededs": a3ComSysBridgePortReceiveMulticastLimitExceededs,
       "a3ComSysBridgePortReceiveMulticastLimitExceededDiscards": a3ComSysBridgePortReceiveMulticastLimitExceededDiscards,
       "a3ComSysBridgePortReceiveSecurityDiscards": a3ComSysBridgePortReceiveSecurityDiscards,
       "a3ComSysBridgePortReceiveUnknownDiscards": a3ComSysBridgePortReceiveUnknownDiscards,
       "a3ComSysBridgePortReceiveOtherDiscards": a3ComSysBridgePortReceiveOtherDiscards,
       "a3ComSysBridgePortReceiveErrorDiscards": a3ComSysBridgePortReceiveErrorDiscards,
       "a3ComSysBridgePortSameSegmentDiscards": a3ComSysBridgePortSameSegmentDiscards,
       "a3ComSysBridgePortTransmitBlockedDiscards": a3ComSysBridgePortTransmitBlockedDiscards,
       "a3ComSysBridgePortReceiveAllPathFilteredFrames": a3ComSysBridgePortReceiveAllPathFilteredFrames,
       "a3ComSysBridgePortReceiveMulticastPathFilteredFrames": a3ComSysBridgePortReceiveMulticastPathFilteredFrames,
       "a3ComSysBridgePortTransmitAllPathFilteredFrames": a3ComSysBridgePortTransmitAllPathFilteredFrames,
       "a3ComSysBridgePortTransmitMulticastPathFilteredFrames": a3ComSysBridgePortTransmitMulticastPathFilteredFrames,
       "a3ComSysBridgePortForwardedUnicastFrames": a3ComSysBridgePortForwardedUnicastFrames,
       "a3ComSysBridgePortForwardedUnicastOctets": a3ComSysBridgePortForwardedUnicastOctets,
       "a3ComSysBridgePortForwardedMulticastFrames": a3ComSysBridgePortForwardedMulticastFrames,
       "a3ComSysBridgePortForwardedMulticastOctets": a3ComSysBridgePortForwardedMulticastOctets,
       "a3ComSysBridgePortFloodedUnicastFrames": a3ComSysBridgePortFloodedUnicastFrames,
       "a3ComSysBridgePortFloodedUnicastOctets": a3ComSysBridgePortFloodedUnicastOctets,
       "a3ComSysBridgePortStpMode": a3ComSysBridgePortStpMode,
       "a3ComSysBridgePortReceiveMulticastLimitFrameType": a3ComSysBridgePortReceiveMulticastLimitFrameType,
       "a3ComSysBridgePortForwardedFrames": a3ComSysBridgePortForwardedFrames,
       "a3ComSysBridgePortReceiveMulticastLimitMultiplier": a3ComSysBridgePortReceiveMulticastLimitMultiplier,
       "a3ComSysBridgePortRateLimitReceiveMulticastEnabled": a3ComSysBridgePortRateLimitReceiveMulticastEnabled,
       "a3ComSysBridgePortRateLimitReceiveBroadcastEnabled": a3ComSysBridgePortRateLimitReceiveBroadcastEnabled,
       "a3ComSysBridgePortRateLimitReceiveFloodEnabled": a3ComSysBridgePortRateLimitReceiveFloodEnabled,
       "a3ComSysBridgePortRateLimitReceiveState": a3ComSysBridgePortRateLimitReceiveState,
       "a3ComSysBridgePortLoopDetectState": a3ComSysBridgePortLoopDetectState,
       "a3ComSysBridgePortAddressMaxLimit": a3ComSysBridgePortAddressMaxLimit,
       "a3ComSysBridgePortAddressState": a3ComSysBridgePortAddressState,
       "a3ComSysBridgePortReceiveInternalPathFilteredFrames": a3ComSysBridgePortReceiveInternalPathFilteredFrames,
       "a3ComSysBridgePortAddressTable": a3ComSysBridgePortAddressTable,
       "a3ComSysBridgePortAddressEntry": a3ComSysBridgePortAddressEntry,
       "a3ComSysBridgePortAddressBridgeIndex": a3ComSysBridgePortAddressBridgeIndex,
       "a3ComSysBridgePortAddressPortIndex": a3ComSysBridgePortAddressPortIndex,
       "a3ComSysBridgePortAddressIndex": a3ComSysBridgePortAddressIndex,
       "a3ComSysBridgePortAddressRemoteAddress": a3ComSysBridgePortAddressRemoteAddress,
       "a3ComSysBridgePortAddressType": a3ComSysBridgePortAddressType,
       "a3ComSysBridgePortAddressIsStatic": a3ComSysBridgePortAddressIsStatic,
       "a3ComSysBridgePortAddressStaticPort": a3ComSysBridgePortAddressStaticPort,
       "a3ComSysBridgePortAddressAge": a3ComSysBridgePortAddressAge,
       "a3ComSysBridgeStpGroupAddress": a3ComSysBridgeStpGroupAddress,
       "a3ComSysBridgeStpEnable": a3ComSysBridgeStpEnable,
       "a3ComSysBridgeVlanPortAddressTable": a3ComSysBridgeVlanPortAddressTable,
       "a3ComSysBridgeVlanPortAddressEntry": a3ComSysBridgeVlanPortAddressEntry,
       "a3ComSysBridgeVlanPortAddressBridgeIndex": a3ComSysBridgeVlanPortAddressBridgeIndex,
       "a3ComSysBridgeVlanPortAddressVlanIndex": a3ComSysBridgeVlanPortAddressVlanIndex,
       "a3ComSysBridgeVlanPortAddressPortIndex": a3ComSysBridgeVlanPortAddressPortIndex,
       "a3ComSysBridgeVlanPortAddressIndex": a3ComSysBridgeVlanPortAddressIndex,
       "a3ComSysBridgeVlanPortAddressRemoteAddress": a3ComSysBridgeVlanPortAddressRemoteAddress,
       "a3ComSysBridgeVlanPortAddressType": a3ComSysBridgeVlanPortAddressType,
       "a3ComSysBridgeVlanPortAddressIsStatic": a3ComSysBridgeVlanPortAddressIsStatic,
       "a3ComSysBridgeVlanPortAddressStaticPort": a3ComSysBridgeVlanPortAddressStaticPort,
       "a3ComSysBridgeVlanPortAddressAge": a3ComSysBridgeVlanPortAddressAge}
)
