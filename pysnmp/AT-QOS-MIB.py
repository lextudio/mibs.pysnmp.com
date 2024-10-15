# SNMP MIB module (AT-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:31 2024
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

(modules,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "modules")

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

qos = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99)
)
qos.setRevisions(
        ("2004-12-01 15:25",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QosSwitch_ObjectIdentity = ObjectIdentity
qosSwitch = _QosSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1)
)
_QosSwitchPortTable_Object = MibTable
qosSwitchPortTable = _QosSwitchPortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 1)
)
if mibBuilder.loadTexts:
    qosSwitchPortTable.setStatus("current")
_QosSwitchPortEntry_Object = MibTableRow
qosSwitchPortEntry = _QosSwitchPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 1, 1)
)
qosSwitchPortEntry.setIndexNames(
    (0, "AT-QOS-MIB", "qosSwitchPortIndex"),
)
if mibBuilder.loadTexts:
    qosSwitchPortEntry.setStatus("current")


class _QosSwitchPortIndex_Type(Integer32):
    """Custom type qosSwitchPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QosSwitchPortIndex_Type.__name__ = "Integer32"
_QosSwitchPortIndex_Object = MibTableColumn
qosSwitchPortIndex = _QosSwitchPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 1, 1, 1),
    _QosSwitchPortIndex_Type()
)
qosSwitchPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosSwitchPortIndex.setStatus("current")


class _QosSwitchPortPolicyIndex_Type(Integer32):
    """Custom type qosSwitchPortPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_QosSwitchPortPolicyIndex_Type.__name__ = "Integer32"
_QosSwitchPortPolicyIndex_Object = MibTableColumn
qosSwitchPortPolicyIndex = _QosSwitchPortPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 1, 1, 2),
    _QosSwitchPortPolicyIndex_Type()
)
qosSwitchPortPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitchPortPolicyIndex.setStatus("current")
_QosSwitchPolicyTable_Object = MibTable
qosSwitchPolicyTable = _QosSwitchPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 2)
)
if mibBuilder.loadTexts:
    qosSwitchPolicyTable.setStatus("current")
_QosSwitchPolicyEntry_Object = MibTableRow
qosSwitchPolicyEntry = _QosSwitchPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 2, 1)
)
qosSwitchPolicyEntry.setIndexNames(
    (0, "AT-QOS-MIB", "qosSwitchPolicyIndex"),
)
if mibBuilder.loadTexts:
    qosSwitchPolicyEntry.setStatus("current")


class _QosSwitchPolicyIndex_Type(Integer32):
    """Custom type qosSwitchPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_QosSwitchPolicyIndex_Type.__name__ = "Integer32"
_QosSwitchPolicyIndex_Object = MibTableColumn
qosSwitchPolicyIndex = _QosSwitchPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 2, 1, 1),
    _QosSwitchPolicyIndex_Type()
)
qosSwitchPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosSwitchPolicyIndex.setStatus("current")


class _QosSwitchPolicyDescription_Type(OctetString):
    """Custom type qosSwitchPolicyDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_QosSwitchPolicyDescription_Type.__name__ = "OctetString"
_QosSwitchPolicyDescription_Object = MibTableColumn
qosSwitchPolicyDescription = _QosSwitchPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 2, 1, 2),
    _QosSwitchPolicyDescription_Type()
)
qosSwitchPolicyDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitchPolicyDescription.setStatus("current")


class _QosSwitchPolicyDefaultTCDropBWClass3_Type(Integer32):
    """Custom type qosSwitchPolicyDefaultTCDropBWClass3 based on Integer32"""
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


_QosSwitchPolicyDefaultTCDropBWClass3_Type.__name__ = "Integer32"
_QosSwitchPolicyDefaultTCDropBWClass3_Object = MibTableColumn
qosSwitchPolicyDefaultTCDropBWClass3 = _QosSwitchPolicyDefaultTCDropBWClass3_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 2, 1, 3),
    _QosSwitchPolicyDefaultTCDropBWClass3_Type()
)
qosSwitchPolicyDefaultTCDropBWClass3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitchPolicyDefaultTCDropBWClass3.setStatus("current")


class _QosSwitchPolicyDefaultTCIgnoreBWClass_Type(Integer32):
    """Custom type qosSwitchPolicyDefaultTCIgnoreBWClass based on Integer32"""
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


_QosSwitchPolicyDefaultTCIgnoreBWClass_Type.__name__ = "Integer32"
_QosSwitchPolicyDefaultTCIgnoreBWClass_Object = MibTableColumn
qosSwitchPolicyDefaultTCIgnoreBWClass = _QosSwitchPolicyDefaultTCIgnoreBWClass_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 2, 1, 4),
    _QosSwitchPolicyDefaultTCIgnoreBWClass_Type()
)
qosSwitchPolicyDefaultTCIgnoreBWClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitchPolicyDefaultTCIgnoreBWClass.setStatus("current")


class _QosSwitchPolicyDefaultTCMarkValue_Type(Integer32):
    """Custom type qosSwitchPolicyDefaultTCMarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(256, 256),
    )


_QosSwitchPolicyDefaultTCMarkValue_Type.__name__ = "Integer32"
_QosSwitchPolicyDefaultTCMarkValue_Object = MibTableColumn
qosSwitchPolicyDefaultTCMarkValue = _QosSwitchPolicyDefaultTCMarkValue_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 2, 1, 5),
    _QosSwitchPolicyDefaultTCMarkValue_Type()
)
qosSwitchPolicyDefaultTCMarkValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitchPolicyDefaultTCMarkValue.setStatus("current")


class _QosSwitchPolicyDefaultTCMaxBandwidth_Type(Integer32):
    """Custom type qosSwitchPolicyDefaultTCMaxBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000000),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_QosSwitchPolicyDefaultTCMaxBandwidth_Type.__name__ = "Integer32"
_QosSwitchPolicyDefaultTCMaxBandwidth_Object = MibTableColumn
qosSwitchPolicyDefaultTCMaxBandwidth = _QosSwitchPolicyDefaultTCMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 2, 1, 6),
    _QosSwitchPolicyDefaultTCMaxBandwidth_Type()
)
qosSwitchPolicyDefaultTCMaxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitchPolicyDefaultTCMaxBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    qosSwitchPolicyDefaultTCMaxBandwidth.setUnits("kbps")


class _QosSwitchPolicyDefaultTCMaxBurstSize_Type(Integer32):
    """Custom type qosSwitchPolicyDefaultTCMaxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000000),
    )


_QosSwitchPolicyDefaultTCMaxBurstSize_Type.__name__ = "Integer32"
_QosSwitchPolicyDefaultTCMaxBurstSize_Object = MibTableColumn
qosSwitchPolicyDefaultTCMaxBurstSize = _QosSwitchPolicyDefaultTCMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 2, 1, 7),
    _QosSwitchPolicyDefaultTCMaxBurstSize_Type()
)
qosSwitchPolicyDefaultTCMaxBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitchPolicyDefaultTCMaxBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    qosSwitchPolicyDefaultTCMaxBurstSize.setUnits("kbps")


class _QosSwitchPolicyDefaultTCMinBandwidth_Type(Integer32):
    """Custom type qosSwitchPolicyDefaultTCMinBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000000),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_QosSwitchPolicyDefaultTCMinBandwidth_Type.__name__ = "Integer32"
_QosSwitchPolicyDefaultTCMinBandwidth_Object = MibTableColumn
qosSwitchPolicyDefaultTCMinBandwidth = _QosSwitchPolicyDefaultTCMinBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 2, 1, 8),
    _QosSwitchPolicyDefaultTCMinBandwidth_Type()
)
qosSwitchPolicyDefaultTCMinBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitchPolicyDefaultTCMinBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    qosSwitchPolicyDefaultTCMinBandwidth.setUnits("kbps")


class _QosSwitchPolicyDefaultTCMinBurstSize_Type(Integer32):
    """Custom type qosSwitchPolicyDefaultTCMinBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000000),
    )


_QosSwitchPolicyDefaultTCMinBurstSize_Type.__name__ = "Integer32"
_QosSwitchPolicyDefaultTCMinBurstSize_Object = MibTableColumn
qosSwitchPolicyDefaultTCMinBurstSize = _QosSwitchPolicyDefaultTCMinBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 2, 1, 9),
    _QosSwitchPolicyDefaultTCMinBurstSize_Type()
)
qosSwitchPolicyDefaultTCMinBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitchPolicyDefaultTCMinBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    qosSwitchPolicyDefaultTCMinBurstSize.setUnits("kbps")


class _QosSwitchPolicyDefaultTCPremarking_Type(Integer32):
    """Custom type qosSwitchPolicyDefaultTCPremarking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("usedscp", 2),
          ("usemarkvalue", 1))
    )


_QosSwitchPolicyDefaultTCPremarking_Type.__name__ = "Integer32"
_QosSwitchPolicyDefaultTCPremarking_Object = MibTableColumn
qosSwitchPolicyDefaultTCPremarking = _QosSwitchPolicyDefaultTCPremarking_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 2, 1, 10),
    _QosSwitchPolicyDefaultTCPremarking_Type()
)
qosSwitchPolicyDefaultTCPremarking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitchPolicyDefaultTCPremarking.setStatus("current")


class _QosSwitchPolicyDefaultTCRemarking_Type(Integer32):
    """Custom type qosSwitchPolicyDefaultTCRemarking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bwclass", 2),
          ("bwclass-priority", 4),
          ("none", 0),
          ("priority", 3),
          ("usedscpmap", 1))
    )


_QosSwitchPolicyDefaultTCRemarking_Type.__name__ = "Integer32"
_QosSwitchPolicyDefaultTCRemarking_Object = MibTableColumn
qosSwitchPolicyDefaultTCRemarking = _QosSwitchPolicyDefaultTCRemarking_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 2, 1, 11),
    _QosSwitchPolicyDefaultTCRemarking_Type()
)
qosSwitchPolicyDefaultTCRemarking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitchPolicyDefaultTCRemarking.setStatus("current")
_QosSwitchTrafficClassTable_Object = MibTable
qosSwitchTrafficClassTable = _QosSwitchTrafficClassTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 3)
)
if mibBuilder.loadTexts:
    qosSwitchTrafficClassTable.setStatus("current")
_QosSwitchTrafficClassEntry_Object = MibTableRow
qosSwitchTrafficClassEntry = _QosSwitchTrafficClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 3, 1)
)
qosSwitchTrafficClassEntry.setIndexNames(
    (0, "AT-QOS-MIB", "qosSwitchTrafficClassIndex"),
)
if mibBuilder.loadTexts:
    qosSwitchTrafficClassEntry.setStatus("current")


class _QosSwitchTrafficClassIndex_Type(Integer32):
    """Custom type qosSwitchTrafficClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QosSwitchTrafficClassIndex_Type.__name__ = "Integer32"
_QosSwitchTrafficClassIndex_Object = MibTableColumn
qosSwitchTrafficClassIndex = _QosSwitchTrafficClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 3, 1, 1),
    _QosSwitchTrafficClassIndex_Type()
)
qosSwitchTrafficClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosSwitchTrafficClassIndex.setStatus("current")


class _QosSwitchTrafficClassPolicyNumber_Type(Integer32):
    """Custom type qosSwitchTrafficClassPolicyNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_QosSwitchTrafficClassPolicyNumber_Type.__name__ = "Integer32"
_QosSwitchTrafficClassPolicyNumber_Object = MibTableColumn
qosSwitchTrafficClassPolicyNumber = _QosSwitchTrafficClassPolicyNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 3, 1, 2),
    _QosSwitchTrafficClassPolicyNumber_Type()
)
qosSwitchTrafficClassPolicyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitchTrafficClassPolicyNumber.setStatus("current")


class _QosSwitchTrafficClassDescription_Type(OctetString):
    """Custom type qosSwitchTrafficClassDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_QosSwitchTrafficClassDescription_Type.__name__ = "OctetString"
_QosSwitchTrafficClassDescription_Object = MibTableColumn
qosSwitchTrafficClassDescription = _QosSwitchTrafficClassDescription_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 3, 1, 3),
    _QosSwitchTrafficClassDescription_Type()
)
qosSwitchTrafficClassDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitchTrafficClassDescription.setStatus("current")


class _QosSwitchTrafficClassDropBWClass3_Type(Integer32):
    """Custom type qosSwitchTrafficClassDropBWClass3 based on Integer32"""
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


_QosSwitchTrafficClassDropBWClass3_Type.__name__ = "Integer32"
_QosSwitchTrafficClassDropBWClass3_Object = MibTableColumn
qosSwitchTrafficClassDropBWClass3 = _QosSwitchTrafficClassDropBWClass3_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 3, 1, 4),
    _QosSwitchTrafficClassDropBWClass3_Type()
)
qosSwitchTrafficClassDropBWClass3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitchTrafficClassDropBWClass3.setStatus("current")


class _QosSwitchTrafficClassIgnoreBWClass_Type(Integer32):
    """Custom type qosSwitchTrafficClassIgnoreBWClass based on Integer32"""
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


_QosSwitchTrafficClassIgnoreBWClass_Type.__name__ = "Integer32"
_QosSwitchTrafficClassIgnoreBWClass_Object = MibTableColumn
qosSwitchTrafficClassIgnoreBWClass = _QosSwitchTrafficClassIgnoreBWClass_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 3, 1, 5),
    _QosSwitchTrafficClassIgnoreBWClass_Type()
)
qosSwitchTrafficClassIgnoreBWClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitchTrafficClassIgnoreBWClass.setStatus("current")


class _QosSwitchTrafficClassMarkValue_Type(Integer32):
    """Custom type qosSwitchTrafficClassMarkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(256, 256),
    )


_QosSwitchTrafficClassMarkValue_Type.__name__ = "Integer32"
_QosSwitchTrafficClassMarkValue_Object = MibTableColumn
qosSwitchTrafficClassMarkValue = _QosSwitchTrafficClassMarkValue_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 3, 1, 6),
    _QosSwitchTrafficClassMarkValue_Type()
)
qosSwitchTrafficClassMarkValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitchTrafficClassMarkValue.setStatus("current")


class _QosSwitchTrafficClassMaxBandwidth_Type(Integer32):
    """Custom type qosSwitchTrafficClassMaxBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000000),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_QosSwitchTrafficClassMaxBandwidth_Type.__name__ = "Integer32"
_QosSwitchTrafficClassMaxBandwidth_Object = MibTableColumn
qosSwitchTrafficClassMaxBandwidth = _QosSwitchTrafficClassMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 3, 1, 7),
    _QosSwitchTrafficClassMaxBandwidth_Type()
)
qosSwitchTrafficClassMaxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitchTrafficClassMaxBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    qosSwitchTrafficClassMaxBandwidth.setUnits("kbps")


class _QosSwitchTrafficClassMaxBurstSize_Type(Integer32):
    """Custom type qosSwitchTrafficClassMaxBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000000),
    )


_QosSwitchTrafficClassMaxBurstSize_Type.__name__ = "Integer32"
_QosSwitchTrafficClassMaxBurstSize_Object = MibTableColumn
qosSwitchTrafficClassMaxBurstSize = _QosSwitchTrafficClassMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 3, 1, 8),
    _QosSwitchTrafficClassMaxBurstSize_Type()
)
qosSwitchTrafficClassMaxBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitchTrafficClassMaxBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    qosSwitchTrafficClassMaxBurstSize.setUnits("kbps")


class _QosSwitchTrafficClassMinBandwidth_Type(Integer32):
    """Custom type qosSwitchTrafficClassMinBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000000),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_QosSwitchTrafficClassMinBandwidth_Type.__name__ = "Integer32"
_QosSwitchTrafficClassMinBandwidth_Object = MibTableColumn
qosSwitchTrafficClassMinBandwidth = _QosSwitchTrafficClassMinBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 3, 1, 9),
    _QosSwitchTrafficClassMinBandwidth_Type()
)
qosSwitchTrafficClassMinBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitchTrafficClassMinBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    qosSwitchTrafficClassMinBandwidth.setUnits("kbps")


class _QosSwitchTrafficClassMinBurstSize_Type(Integer32):
    """Custom type qosSwitchTrafficClassMinBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000000),
    )


_QosSwitchTrafficClassMinBurstSize_Type.__name__ = "Integer32"
_QosSwitchTrafficClassMinBurstSize_Object = MibTableColumn
qosSwitchTrafficClassMinBurstSize = _QosSwitchTrafficClassMinBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 3, 1, 10),
    _QosSwitchTrafficClassMinBurstSize_Type()
)
qosSwitchTrafficClassMinBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitchTrafficClassMinBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    qosSwitchTrafficClassMinBurstSize.setUnits("kbps")


class _QosSwitchTrafficClassPremarking_Type(Integer32):
    """Custom type qosSwitchTrafficClassPremarking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("usedscp", 2),
          ("usemarkvalue", 1))
    )


_QosSwitchTrafficClassPremarking_Type.__name__ = "Integer32"
_QosSwitchTrafficClassPremarking_Object = MibTableColumn
qosSwitchTrafficClassPremarking = _QosSwitchTrafficClassPremarking_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 3, 1, 11),
    _QosSwitchTrafficClassPremarking_Type()
)
qosSwitchTrafficClassPremarking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitchTrafficClassPremarking.setStatus("current")


class _QosSwitchTrafficClassRemarking_Type(Integer32):
    """Custom type qosSwitchTrafficClassRemarking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bwclass", 2),
          ("bwclass-priority", 4),
          ("none", 0),
          ("priority", 3),
          ("usedscpmap", 1))
    )


_QosSwitchTrafficClassRemarking_Type.__name__ = "Integer32"
_QosSwitchTrafficClassRemarking_Object = MibTableColumn
qosSwitchTrafficClassRemarking = _QosSwitchTrafficClassRemarking_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 3, 1, 12),
    _QosSwitchTrafficClassRemarking_Type()
)
qosSwitchTrafficClassRemarking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitchTrafficClassRemarking.setStatus("current")
_QosSwitch8948_ObjectIdentity = ObjectIdentity
qosSwitch8948 = _QosSwitch8948_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 4)
)
_QosSwitch8948PortTable_Object = MibTable
qosSwitch8948PortTable = _QosSwitch8948PortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 4, 1)
)
if mibBuilder.loadTexts:
    qosSwitch8948PortTable.setStatus("current")
_QosSwitch8948PortEntry_Object = MibTableRow
qosSwitch8948PortEntry = _QosSwitch8948PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    qosSwitch8948PortEntry.setStatus("current")
_QosSwitch8948PortDefaultTCCountersAggregateBytes_Type = Counter64
_QosSwitch8948PortDefaultTCCountersAggregateBytes_Object = MibTableColumn
qosSwitch8948PortDefaultTCCountersAggregateBytes = _QosSwitch8948PortDefaultTCCountersAggregateBytes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 4, 1, 1, 1),
    _QosSwitch8948PortDefaultTCCountersAggregateBytes_Type()
)
qosSwitch8948PortDefaultTCCountersAggregateBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitch8948PortDefaultTCCountersAggregateBytes.setStatus("current")
_QosSwitch8948PortDefaultTCCountersBwConformanceClass1Bytes_Type = Counter64
_QosSwitch8948PortDefaultTCCountersBwConformanceClass1Bytes_Object = MibTableColumn
qosSwitch8948PortDefaultTCCountersBwConformanceClass1Bytes = _QosSwitch8948PortDefaultTCCountersBwConformanceClass1Bytes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 4, 1, 1, 2),
    _QosSwitch8948PortDefaultTCCountersBwConformanceClass1Bytes_Type()
)
qosSwitch8948PortDefaultTCCountersBwConformanceClass1Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitch8948PortDefaultTCCountersBwConformanceClass1Bytes.setStatus("current")
_QosSwitch8948PortDefaultTCCountersBwConformanceClass2Bytes_Type = Counter64
_QosSwitch8948PortDefaultTCCountersBwConformanceClass2Bytes_Object = MibTableColumn
qosSwitch8948PortDefaultTCCountersBwConformanceClass2Bytes = _QosSwitch8948PortDefaultTCCountersBwConformanceClass2Bytes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 4, 1, 1, 3),
    _QosSwitch8948PortDefaultTCCountersBwConformanceClass2Bytes_Type()
)
qosSwitch8948PortDefaultTCCountersBwConformanceClass2Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitch8948PortDefaultTCCountersBwConformanceClass2Bytes.setStatus("current")
_QosSwitch8948PortDefaultTCCountersBwConformanceClass3Bytes_Type = Counter64
_QosSwitch8948PortDefaultTCCountersBwConformanceClass3Bytes_Object = MibTableColumn
qosSwitch8948PortDefaultTCCountersBwConformanceClass3Bytes = _QosSwitch8948PortDefaultTCCountersBwConformanceClass3Bytes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 4, 1, 1, 4),
    _QosSwitch8948PortDefaultTCCountersBwConformanceClass3Bytes_Type()
)
qosSwitch8948PortDefaultTCCountersBwConformanceClass3Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitch8948PortDefaultTCCountersBwConformanceClass3Bytes.setStatus("current")
_QosSwitch8948PortDefaultTCCountersDroppedBytes_Type = Counter64
_QosSwitch8948PortDefaultTCCountersDroppedBytes_Object = MibTableColumn
qosSwitch8948PortDefaultTCCountersDroppedBytes = _QosSwitch8948PortDefaultTCCountersDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 4, 1, 1, 5),
    _QosSwitch8948PortDefaultTCCountersDroppedBytes_Type()
)
qosSwitch8948PortDefaultTCCountersDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitch8948PortDefaultTCCountersDroppedBytes.setStatus("current")
_QosSwitch8948PortQueueLength_Type = Gauge32
_QosSwitch8948PortQueueLength_Object = MibTableColumn
qosSwitch8948PortQueueLength = _QosSwitch8948PortQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 4, 1, 1, 6),
    _QosSwitch8948PortQueueLength_Type()
)
qosSwitch8948PortQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitch8948PortQueueLength.setStatus("current")
_QosSwitch8948PortQueue0Length_Type = Gauge32
_QosSwitch8948PortQueue0Length_Object = MibTableColumn
qosSwitch8948PortQueue0Length = _QosSwitch8948PortQueue0Length_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 4, 1, 1, 7),
    _QosSwitch8948PortQueue0Length_Type()
)
qosSwitch8948PortQueue0Length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitch8948PortQueue0Length.setStatus("current")
_QosSwitch8948PortQueue1Length_Type = Gauge32
_QosSwitch8948PortQueue1Length_Object = MibTableColumn
qosSwitch8948PortQueue1Length = _QosSwitch8948PortQueue1Length_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 4, 1, 1, 8),
    _QosSwitch8948PortQueue1Length_Type()
)
qosSwitch8948PortQueue1Length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitch8948PortQueue1Length.setStatus("current")
_QosSwitch8948PortQueue2Length_Type = Gauge32
_QosSwitch8948PortQueue2Length_Object = MibTableColumn
qosSwitch8948PortQueue2Length = _QosSwitch8948PortQueue2Length_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 4, 1, 1, 9),
    _QosSwitch8948PortQueue2Length_Type()
)
qosSwitch8948PortQueue2Length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitch8948PortQueue2Length.setStatus("current")
_QosSwitch8948PortQueue3Length_Type = Gauge32
_QosSwitch8948PortQueue3Length_Object = MibTableColumn
qosSwitch8948PortQueue3Length = _QosSwitch8948PortQueue3Length_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 4, 1, 1, 10),
    _QosSwitch8948PortQueue3Length_Type()
)
qosSwitch8948PortQueue3Length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitch8948PortQueue3Length.setStatus("current")
_QosSwitch8948PortQueue4Length_Type = Gauge32
_QosSwitch8948PortQueue4Length_Object = MibTableColumn
qosSwitch8948PortQueue4Length = _QosSwitch8948PortQueue4Length_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 4, 1, 1, 11),
    _QosSwitch8948PortQueue4Length_Type()
)
qosSwitch8948PortQueue4Length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitch8948PortQueue4Length.setStatus("current")
_QosSwitch8948PortQueue5Length_Type = Gauge32
_QosSwitch8948PortQueue5Length_Object = MibTableColumn
qosSwitch8948PortQueue5Length = _QosSwitch8948PortQueue5Length_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 4, 1, 1, 12),
    _QosSwitch8948PortQueue5Length_Type()
)
qosSwitch8948PortQueue5Length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitch8948PortQueue5Length.setStatus("current")
_QosSwitch8948PortQueue6Length_Type = Gauge32
_QosSwitch8948PortQueue6Length_Object = MibTableColumn
qosSwitch8948PortQueue6Length = _QosSwitch8948PortQueue6Length_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 4, 1, 1, 13),
    _QosSwitch8948PortQueue6Length_Type()
)
qosSwitch8948PortQueue6Length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitch8948PortQueue6Length.setStatus("current")
_QosSwitch8948PortQueue7Length_Type = Gauge32
_QosSwitch8948PortQueue7Length_Object = MibTableColumn
qosSwitch8948PortQueue7Length = _QosSwitch8948PortQueue7Length_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 4, 1, 1, 14),
    _QosSwitch8948PortQueue7Length_Type()
)
qosSwitch8948PortQueue7Length.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitch8948PortQueue7Length.setStatus("current")
_QosSwitch8948TrafficClassCountersTable_Object = MibTable
qosSwitch8948TrafficClassCountersTable = _QosSwitch8948TrafficClassCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 4, 2)
)
if mibBuilder.loadTexts:
    qosSwitch8948TrafficClassCountersTable.setStatus("current")
_QosSwitch8948TrafficClassCountersEntry_Object = MibTableRow
qosSwitch8948TrafficClassCountersEntry = _QosSwitch8948TrafficClassCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 4, 2, 1)
)
qosSwitch8948TrafficClassCountersEntry.setIndexNames(
    (0, "AT-QOS-MIB", "qosSwitch8948TCCountersPortIndex"),
    (0, "AT-QOS-MIB", "qosSwitch8948TCCountersPolicyIndex"),
    (0, "AT-QOS-MIB", "qosSwitch8948TCCountersTrafficClassIndex"),
)
if mibBuilder.loadTexts:
    qosSwitch8948TrafficClassCountersEntry.setStatus("current")


class _QosSwitch8948TCCountersPortIndex_Type(Integer32):
    """Custom type qosSwitch8948TCCountersPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QosSwitch8948TCCountersPortIndex_Type.__name__ = "Integer32"
_QosSwitch8948TCCountersPortIndex_Object = MibTableColumn
qosSwitch8948TCCountersPortIndex = _QosSwitch8948TCCountersPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 4, 2, 1, 1),
    _QosSwitch8948TCCountersPortIndex_Type()
)
qosSwitch8948TCCountersPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosSwitch8948TCCountersPortIndex.setStatus("current")


class _QosSwitch8948TCCountersPolicyIndex_Type(Integer32):
    """Custom type qosSwitch8948TCCountersPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_QosSwitch8948TCCountersPolicyIndex_Type.__name__ = "Integer32"
_QosSwitch8948TCCountersPolicyIndex_Object = MibTableColumn
qosSwitch8948TCCountersPolicyIndex = _QosSwitch8948TCCountersPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 4, 2, 1, 2),
    _QosSwitch8948TCCountersPolicyIndex_Type()
)
qosSwitch8948TCCountersPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosSwitch8948TCCountersPolicyIndex.setStatus("current")


class _QosSwitch8948TCCountersTrafficClassIndex_Type(Integer32):
    """Custom type qosSwitch8948TCCountersTrafficClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QosSwitch8948TCCountersTrafficClassIndex_Type.__name__ = "Integer32"
_QosSwitch8948TCCountersTrafficClassIndex_Object = MibTableColumn
qosSwitch8948TCCountersTrafficClassIndex = _QosSwitch8948TCCountersTrafficClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 4, 2, 1, 3),
    _QosSwitch8948TCCountersTrafficClassIndex_Type()
)
qosSwitch8948TCCountersTrafficClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosSwitch8948TCCountersTrafficClassIndex.setStatus("current")
_QosSwitch8948TCCountersAggregateBytes_Type = Counter32
_QosSwitch8948TCCountersAggregateBytes_Object = MibTableColumn
qosSwitch8948TCCountersAggregateBytes = _QosSwitch8948TCCountersAggregateBytes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 4, 2, 1, 4),
    _QosSwitch8948TCCountersAggregateBytes_Type()
)
qosSwitch8948TCCountersAggregateBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitch8948TCCountersAggregateBytes.setStatus("current")
_QosSwitch8948TCCountersBwConformanceClass1Bytes_Type = Counter32
_QosSwitch8948TCCountersBwConformanceClass1Bytes_Object = MibTableColumn
qosSwitch8948TCCountersBwConformanceClass1Bytes = _QosSwitch8948TCCountersBwConformanceClass1Bytes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 4, 2, 1, 5),
    _QosSwitch8948TCCountersBwConformanceClass1Bytes_Type()
)
qosSwitch8948TCCountersBwConformanceClass1Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitch8948TCCountersBwConformanceClass1Bytes.setStatus("current")
_QosSwitch8948TCCountersBwConformanceClass2Bytes_Type = Counter32
_QosSwitch8948TCCountersBwConformanceClass2Bytes_Object = MibTableColumn
qosSwitch8948TCCountersBwConformanceClass2Bytes = _QosSwitch8948TCCountersBwConformanceClass2Bytes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 4, 2, 1, 6),
    _QosSwitch8948TCCountersBwConformanceClass2Bytes_Type()
)
qosSwitch8948TCCountersBwConformanceClass2Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitch8948TCCountersBwConformanceClass2Bytes.setStatus("current")
_QosSwitch8948TCCountersBwConformanceClass3Bytes_Type = Counter32
_QosSwitch8948TCCountersBwConformanceClass3Bytes_Object = MibTableColumn
qosSwitch8948TCCountersBwConformanceClass3Bytes = _QosSwitch8948TCCountersBwConformanceClass3Bytes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 4, 2, 1, 7),
    _QosSwitch8948TCCountersBwConformanceClass3Bytes_Type()
)
qosSwitch8948TCCountersBwConformanceClass3Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitch8948TCCountersBwConformanceClass3Bytes.setStatus("current")
_QosSwitch8948TCCountersDroppedBytes_Type = Counter32
_QosSwitch8948TCCountersDroppedBytes_Object = MibTableColumn
qosSwitch8948TCCountersDroppedBytes = _QosSwitch8948TCCountersDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 99, 1, 4, 2, 1, 8),
    _QosSwitch8948TCCountersDroppedBytes_Type()
)
qosSwitch8948TCCountersDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSwitch8948TCCountersDroppedBytes.setStatus("current")
qosSwitchPortEntry.registerAugmentions(
    ("AT-QOS-MIB",
     "qosSwitch8948PortEntry")
)
qosSwitch8948PortEntry.setIndexNames(*qosSwitchPortEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-QOS-MIB",
    **{"qos": qos,
       "qosSwitch": qosSwitch,
       "qosSwitchPortTable": qosSwitchPortTable,
       "qosSwitchPortEntry": qosSwitchPortEntry,
       "qosSwitchPortIndex": qosSwitchPortIndex,
       "qosSwitchPortPolicyIndex": qosSwitchPortPolicyIndex,
       "qosSwitchPolicyTable": qosSwitchPolicyTable,
       "qosSwitchPolicyEntry": qosSwitchPolicyEntry,
       "qosSwitchPolicyIndex": qosSwitchPolicyIndex,
       "qosSwitchPolicyDescription": qosSwitchPolicyDescription,
       "qosSwitchPolicyDefaultTCDropBWClass3": qosSwitchPolicyDefaultTCDropBWClass3,
       "qosSwitchPolicyDefaultTCIgnoreBWClass": qosSwitchPolicyDefaultTCIgnoreBWClass,
       "qosSwitchPolicyDefaultTCMarkValue": qosSwitchPolicyDefaultTCMarkValue,
       "qosSwitchPolicyDefaultTCMaxBandwidth": qosSwitchPolicyDefaultTCMaxBandwidth,
       "qosSwitchPolicyDefaultTCMaxBurstSize": qosSwitchPolicyDefaultTCMaxBurstSize,
       "qosSwitchPolicyDefaultTCMinBandwidth": qosSwitchPolicyDefaultTCMinBandwidth,
       "qosSwitchPolicyDefaultTCMinBurstSize": qosSwitchPolicyDefaultTCMinBurstSize,
       "qosSwitchPolicyDefaultTCPremarking": qosSwitchPolicyDefaultTCPremarking,
       "qosSwitchPolicyDefaultTCRemarking": qosSwitchPolicyDefaultTCRemarking,
       "qosSwitchTrafficClassTable": qosSwitchTrafficClassTable,
       "qosSwitchTrafficClassEntry": qosSwitchTrafficClassEntry,
       "qosSwitchTrafficClassIndex": qosSwitchTrafficClassIndex,
       "qosSwitchTrafficClassPolicyNumber": qosSwitchTrafficClassPolicyNumber,
       "qosSwitchTrafficClassDescription": qosSwitchTrafficClassDescription,
       "qosSwitchTrafficClassDropBWClass3": qosSwitchTrafficClassDropBWClass3,
       "qosSwitchTrafficClassIgnoreBWClass": qosSwitchTrafficClassIgnoreBWClass,
       "qosSwitchTrafficClassMarkValue": qosSwitchTrafficClassMarkValue,
       "qosSwitchTrafficClassMaxBandwidth": qosSwitchTrafficClassMaxBandwidth,
       "qosSwitchTrafficClassMaxBurstSize": qosSwitchTrafficClassMaxBurstSize,
       "qosSwitchTrafficClassMinBandwidth": qosSwitchTrafficClassMinBandwidth,
       "qosSwitchTrafficClassMinBurstSize": qosSwitchTrafficClassMinBurstSize,
       "qosSwitchTrafficClassPremarking": qosSwitchTrafficClassPremarking,
       "qosSwitchTrafficClassRemarking": qosSwitchTrafficClassRemarking,
       "qosSwitch8948": qosSwitch8948,
       "qosSwitch8948PortTable": qosSwitch8948PortTable,
       "qosSwitch8948PortEntry": qosSwitch8948PortEntry,
       "qosSwitch8948PortDefaultTCCountersAggregateBytes": qosSwitch8948PortDefaultTCCountersAggregateBytes,
       "qosSwitch8948PortDefaultTCCountersBwConformanceClass1Bytes": qosSwitch8948PortDefaultTCCountersBwConformanceClass1Bytes,
       "qosSwitch8948PortDefaultTCCountersBwConformanceClass2Bytes": qosSwitch8948PortDefaultTCCountersBwConformanceClass2Bytes,
       "qosSwitch8948PortDefaultTCCountersBwConformanceClass3Bytes": qosSwitch8948PortDefaultTCCountersBwConformanceClass3Bytes,
       "qosSwitch8948PortDefaultTCCountersDroppedBytes": qosSwitch8948PortDefaultTCCountersDroppedBytes,
       "qosSwitch8948PortQueueLength": qosSwitch8948PortQueueLength,
       "qosSwitch8948PortQueue0Length": qosSwitch8948PortQueue0Length,
       "qosSwitch8948PortQueue1Length": qosSwitch8948PortQueue1Length,
       "qosSwitch8948PortQueue2Length": qosSwitch8948PortQueue2Length,
       "qosSwitch8948PortQueue3Length": qosSwitch8948PortQueue3Length,
       "qosSwitch8948PortQueue4Length": qosSwitch8948PortQueue4Length,
       "qosSwitch8948PortQueue5Length": qosSwitch8948PortQueue5Length,
       "qosSwitch8948PortQueue6Length": qosSwitch8948PortQueue6Length,
       "qosSwitch8948PortQueue7Length": qosSwitch8948PortQueue7Length,
       "qosSwitch8948TrafficClassCountersTable": qosSwitch8948TrafficClassCountersTable,
       "qosSwitch8948TrafficClassCountersEntry": qosSwitch8948TrafficClassCountersEntry,
       "qosSwitch8948TCCountersPortIndex": qosSwitch8948TCCountersPortIndex,
       "qosSwitch8948TCCountersPolicyIndex": qosSwitch8948TCCountersPolicyIndex,
       "qosSwitch8948TCCountersTrafficClassIndex": qosSwitch8948TCCountersTrafficClassIndex,
       "qosSwitch8948TCCountersAggregateBytes": qosSwitch8948TCCountersAggregateBytes,
       "qosSwitch8948TCCountersBwConformanceClass1Bytes": qosSwitch8948TCCountersBwConformanceClass1Bytes,
       "qosSwitch8948TCCountersBwConformanceClass2Bytes": qosSwitch8948TCCountersBwConformanceClass2Bytes,
       "qosSwitch8948TCCountersBwConformanceClass3Bytes": qosSwitch8948TCCountersBwConformanceClass3Bytes,
       "qosSwitch8948TCCountersDroppedBytes": qosSwitch8948TCCountersDroppedBytes}
)
