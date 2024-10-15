# SNMP MIB module (HUAWEI-IF-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-IF-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:01 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwIfQoSMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwQoS_ObjectIdentity = ObjectIdentity
hwQoS = _HwQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32)
)
_QosFIFOTable_Object = MibTable
qosFIFOTable = _QosFIFOTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 1)
)
if mibBuilder.loadTexts:
    qosFIFOTable.setStatus("mandatory")
_QosFIFOEntry_Object = MibTableRow
qosFIFOEntry = _QosFIFOEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 1, 1)
)
qosFIFOEntry.setIndexNames(
    (0, "HUAWEI-IF-QOS-MIB", "qosFIFOIfIndex"),
)
if mibBuilder.loadTexts:
    qosFIFOEntry.setStatus("mandatory")
_QosFIFOIfIndex_Type = Integer32
_QosFIFOIfIndex_Object = MibTableColumn
qosFIFOIfIndex = _QosFIFOIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 1, 1, 1),
    _QosFIFOIfIndex_Type()
)
qosFIFOIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosFIFOIfIndex.setStatus("mandatory")
_QosFIFOIfName_Type = OctetString
_QosFIFOIfName_Object = MibTableColumn
qosFIFOIfName = _QosFIFOIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 1, 1, 2),
    _QosFIFOIfName_Type()
)
qosFIFOIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosFIFOIfName.setStatus("mandatory")


class _QosFIFOMaxQueueLen_Type(Integer32):
    """Custom type qosFIFOMaxQueueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QosFIFOMaxQueueLen_Type.__name__ = "Integer32"
_QosFIFOMaxQueueLen_Object = MibTableColumn
qosFIFOMaxQueueLen = _QosFIFOMaxQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 1, 1, 3),
    _QosFIFOMaxQueueLen_Type()
)
qosFIFOMaxQueueLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosFIFOMaxQueueLen.setStatus("mandatory")
_QosFIFOCurQueueLen_Type = Integer32
_QosFIFOCurQueueLen_Object = MibTableColumn
qosFIFOCurQueueLen = _QosFIFOCurQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 1, 1, 4),
    _QosFIFOCurQueueLen_Type()
)
qosFIFOCurQueueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosFIFOCurQueueLen.setStatus("mandatory")
_QosFIFODiscardPkt_Type = Counter32
_QosFIFODiscardPkt_Object = MibTableColumn
qosFIFODiscardPkt = _QosFIFODiscardPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 1, 1, 5),
    _QosFIFODiscardPkt_Type()
)
qosFIFODiscardPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosFIFODiscardPkt.setStatus("mandatory")


class _QosUndoFIFO_Type(Integer32):
    """Custom type qosUndoFIFO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("qosFIFO", 0),
          ("qosNoFIFO", 1))
    )


_QosUndoFIFO_Type.__name__ = "Integer32"
_QosUndoFIFO_Object = MibTableColumn
qosUndoFIFO = _QosUndoFIFO_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 1, 1, 6),
    _QosUndoFIFO_Type()
)
qosUndoFIFO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosUndoFIFO.setStatus("mandatory")
_QosPqlDefaultTable_Object = MibTable
qosPqlDefaultTable = _QosPqlDefaultTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 2)
)
if mibBuilder.loadTexts:
    qosPqlDefaultTable.setStatus("mandatory")
_QosPqlDefaultEntry_Object = MibTableRow
qosPqlDefaultEntry = _QosPqlDefaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 2, 1)
)
qosPqlDefaultEntry.setIndexNames(
    (0, "HUAWEI-IF-QOS-MIB", "qosPqlDefaultListNum"),
)
if mibBuilder.loadTexts:
    qosPqlDefaultEntry.setStatus("mandatory")


class _QosPqlDefaultListNum_Type(Integer32):
    """Custom type qosPqlDefaultListNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_QosPqlDefaultListNum_Type.__name__ = "Integer32"
_QosPqlDefaultListNum_Object = MibTableColumn
qosPqlDefaultListNum = _QosPqlDefaultListNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 2, 1, 1),
    _QosPqlDefaultListNum_Type()
)
qosPqlDefaultListNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPqlDefaultListNum.setStatus("mandatory")


class _QosPqlDefaultQueueType_Type(Integer32):
    """Custom type qosPqlDefaultQueueType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bottom", 3),
          ("middle", 1),
          ("normal", 2),
          ("top", 0))
    )


_QosPqlDefaultQueueType_Type.__name__ = "Integer32"
_QosPqlDefaultQueueType_Object = MibTableColumn
qosPqlDefaultQueueType = _QosPqlDefaultQueueType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 2, 1, 2),
    _QosPqlDefaultQueueType_Type()
)
qosPqlDefaultQueueType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPqlDefaultQueueType.setStatus("mandatory")


class _QosUndoPqlDefault_Type(Integer32):
    """Custom type qosUndoPqlDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("qosNoPqlDefault", 1),
          ("qosPqlDefault", 0))
    )


_QosUndoPqlDefault_Type.__name__ = "Integer32"
_QosUndoPqlDefault_Object = MibTableColumn
qosUndoPqlDefault = _QosUndoPqlDefault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 2, 1, 3),
    _QosUndoPqlDefault_Type()
)
qosUndoPqlDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosUndoPqlDefault.setStatus("mandatory")
_QosPqlQueueLenTable_Object = MibTable
qosPqlQueueLenTable = _QosPqlQueueLenTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 3)
)
if mibBuilder.loadTexts:
    qosPqlQueueLenTable.setStatus("mandatory")
_QosPqlQueueLenEntry_Object = MibTableRow
qosPqlQueueLenEntry = _QosPqlQueueLenEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 3, 1)
)
qosPqlQueueLenEntry.setIndexNames(
    (0, "HUAWEI-IF-QOS-MIB", "qosPqlQueLenListNum"),
    (0, "HUAWEI-IF-QOS-MIB", "qosPqlQueLenQueueType"),
)
if mibBuilder.loadTexts:
    qosPqlQueueLenEntry.setStatus("mandatory")


class _QosPqlQueLenListNum_Type(Integer32):
    """Custom type qosPqlQueLenListNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_QosPqlQueLenListNum_Type.__name__ = "Integer32"
_QosPqlQueLenListNum_Object = MibTableColumn
qosPqlQueLenListNum = _QosPqlQueLenListNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 3, 1, 1),
    _QosPqlQueLenListNum_Type()
)
qosPqlQueLenListNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPqlQueLenListNum.setStatus("mandatory")


class _QosPqlQueLenQueueType_Type(Integer32):
    """Custom type qosPqlQueLenQueueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bottom", 3),
          ("middle", 1),
          ("normal", 2),
          ("top", 0))
    )


_QosPqlQueLenQueueType_Type.__name__ = "Integer32"
_QosPqlQueLenQueueType_Object = MibTableColumn
qosPqlQueLenQueueType = _QosPqlQueLenQueueType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 3, 1, 2),
    _QosPqlQueLenQueueType_Type()
)
qosPqlQueLenQueueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPqlQueLenQueueType.setStatus("mandatory")


class _QosPqlQueLenValue_Type(Integer32):
    """Custom type qosPqlQueLenValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QosPqlQueLenValue_Type.__name__ = "Integer32"
_QosPqlQueLenValue_Object = MibTableColumn
qosPqlQueLenValue = _QosPqlQueLenValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 3, 1, 3),
    _QosPqlQueLenValue_Type()
)
qosPqlQueLenValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPqlQueLenValue.setStatus("mandatory")


class _QosUndoPqlQueLen_Type(Integer32):
    """Custom type qosUndoPqlQueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("qosNoPqlQueLen", 1),
          ("qosPqlQueLen", 0))
    )


_QosUndoPqlQueLen_Type.__name__ = "Integer32"
_QosUndoPqlQueLen_Object = MibTableColumn
qosUndoPqlQueLen = _QosUndoPqlQueLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 3, 1, 4),
    _QosUndoPqlQueLen_Type()
)
qosUndoPqlQueLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosUndoPqlQueLen.setStatus("mandatory")
_QosPqlIfTable_Object = MibTable
qosPqlIfTable = _QosPqlIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 4)
)
if mibBuilder.loadTexts:
    qosPqlIfTable.setStatus("mandatory")
_QosPqlIfEntry_Object = MibTableRow
qosPqlIfEntry = _QosPqlIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 4, 1)
)
qosPqlIfEntry.setIndexNames(
    (0, "HUAWEI-IF-QOS-MIB", "qosPqlIfListNum"),
    (0, "HUAWEI-IF-QOS-MIB", "qosPqlIfIndex"),
)
if mibBuilder.loadTexts:
    qosPqlIfEntry.setStatus("mandatory")
_QosPqlIfListNum_Type = Integer32
_QosPqlIfListNum_Object = MibTableColumn
qosPqlIfListNum = _QosPqlIfListNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 4, 1, 1),
    _QosPqlIfListNum_Type()
)
qosPqlIfListNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPqlIfListNum.setStatus("mandatory")
_QosPqlIfIndex_Type = Integer32
_QosPqlIfIndex_Object = MibTableColumn
qosPqlIfIndex = _QosPqlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 4, 1, 2),
    _QosPqlIfIndex_Type()
)
qosPqlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPqlIfIndex.setStatus("mandatory")
_QosPqlIfName_Type = OctetString
_QosPqlIfName_Object = MibTableColumn
qosPqlIfName = _QosPqlIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 4, 1, 3),
    _QosPqlIfName_Type()
)
qosPqlIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPqlIfName.setStatus("mandatory")


class _QosPqlIfQueueType_Type(Integer32):
    """Custom type qosPqlIfQueueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bottom", 3),
          ("middle", 1),
          ("normal", 2),
          ("top", 0))
    )


_QosPqlIfQueueType_Type.__name__ = "Integer32"
_QosPqlIfQueueType_Object = MibTableColumn
qosPqlIfQueueType = _QosPqlIfQueueType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 4, 1, 4),
    _QosPqlIfQueueType_Type()
)
qosPqlIfQueueType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPqlIfQueueType.setStatus("mandatory")


class _QosUndoPqlIf_Type(Integer32):
    """Custom type qosUndoPqlIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("qosNoPqlIF", 1),
          ("qosPqlIF", 0))
    )


_QosUndoPqlIf_Type.__name__ = "Integer32"
_QosUndoPqlIf_Object = MibTableColumn
qosUndoPqlIf = _QosUndoPqlIf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 4, 1, 5),
    _QosUndoPqlIf_Type()
)
qosUndoPqlIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosUndoPqlIf.setStatus("mandatory")
_QosPqlProtocolTable_Object = MibTable
qosPqlProtocolTable = _QosPqlProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 5)
)
if mibBuilder.loadTexts:
    qosPqlProtocolTable.setStatus("mandatory")
_QosPqlProtocolEntry_Object = MibTableRow
qosPqlProtocolEntry = _QosPqlProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 5, 1)
)
qosPqlProtocolEntry.setIndexNames(
    (0, "HUAWEI-IF-QOS-MIB", "qosPqlProListNum"),
    (0, "HUAWEI-IF-QOS-MIB", "qosPqlProName"),
    (0, "HUAWEI-IF-QOS-MIB", "qosPqlProQueKey"),
    (0, "HUAWEI-IF-QOS-MIB", "qosPqlProQueKeyValue"),
)
if mibBuilder.loadTexts:
    qosPqlProtocolEntry.setStatus("mandatory")
_QosPqlProListNum_Type = Integer32
_QosPqlProListNum_Object = MibTableColumn
qosPqlProListNum = _QosPqlProListNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 5, 1, 1),
    _QosPqlProListNum_Type()
)
qosPqlProListNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPqlProListNum.setStatus("mandatory")


class _QosPqlProName_Type(Integer32):
    """Custom type qosPqlProName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("mpls", 2))
    )


_QosPqlProName_Type.__name__ = "Integer32"
_QosPqlProName_Object = MibTableColumn
qosPqlProName = _QosPqlProName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 5, 1, 2),
    _QosPqlProName_Type()
)
qosPqlProName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPqlProName.setStatus("mandatory")


class _QosPqlProQueKey_Type(Integer32):
    """Custom type qosPqlProQueKey based on Integer32"""
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
        *(("acl", 3),
          ("exp-mask", 8),
          ("fragment", 2),
          ("greater-than", 5),
          ("less-than", 4),
          ("null", 1),
          ("tcp", 6),
          ("udp", 7))
    )


_QosPqlProQueKey_Type.__name__ = "Integer32"
_QosPqlProQueKey_Object = MibTableColumn
qosPqlProQueKey = _QosPqlProQueKey_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 5, 1, 3),
    _QosPqlProQueKey_Type()
)
qosPqlProQueKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPqlProQueKey.setStatus("mandatory")


class _QosPqlProQueKeyValue_Type(Integer32):
    """Custom type qosPqlProQueKeyValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QosPqlProQueKeyValue_Type.__name__ = "Integer32"
_QosPqlProQueKeyValue_Object = MibTableColumn
qosPqlProQueKeyValue = _QosPqlProQueKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 5, 1, 4),
    _QosPqlProQueKeyValue_Type()
)
qosPqlProQueKeyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPqlProQueKeyValue.setStatus("mandatory")


class _QosPqlProQueType_Type(Integer32):
    """Custom type qosPqlProQueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bottom", 3),
          ("middle", 1),
          ("normal", 2),
          ("top", 0))
    )


_QosPqlProQueType_Type.__name__ = "Integer32"
_QosPqlProQueType_Object = MibTableColumn
qosPqlProQueType = _QosPqlProQueType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 5, 1, 5),
    _QosPqlProQueType_Type()
)
qosPqlProQueType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPqlProQueType.setStatus("mandatory")


class _QosUndoPqlProtocol_Type(Integer32):
    """Custom type qosUndoPqlProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("qosNoPqlProtocol", 1),
          ("qosPqlProtocol", 0))
    )


_QosUndoPqlProtocol_Type.__name__ = "Integer32"
_QosUndoPqlProtocol_Object = MibTableColumn
qosUndoPqlProtocol = _QosUndoPqlProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 5, 1, 6),
    _QosUndoPqlProtocol_Type()
)
qosUndoPqlProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosUndoPqlProtocol.setStatus("mandatory")
_QosPQTable_Object = MibTable
qosPQTable = _QosPQTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 6)
)
if mibBuilder.loadTexts:
    qosPQTable.setStatus("mandatory")
_QosPQEntry_Object = MibTableRow
qosPQEntry = _QosPQEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 6, 1)
)
qosPQEntry.setIndexNames(
    (0, "HUAWEI-IF-QOS-MIB", "qosPQIfIndex"),
)
if mibBuilder.loadTexts:
    qosPQEntry.setStatus("mandatory")
_QosPQIfIndex_Type = Integer32
_QosPQIfIndex_Object = MibTableColumn
qosPQIfIndex = _QosPQIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 6, 1, 1),
    _QosPQIfIndex_Type()
)
qosPQIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPQIfIndex.setStatus("mandatory")


class _QosPQListNum_Type(Integer32):
    """Custom type qosPQListNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_QosPQListNum_Type.__name__ = "Integer32"
_QosPQListNum_Object = MibTableColumn
qosPQListNum = _QosPQListNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 6, 1, 2),
    _QosPQListNum_Type()
)
qosPQListNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPQListNum.setStatus("mandatory")
_QosPQIfName_Type = OctetString
_QosPQIfName_Object = MibTableColumn
qosPQIfName = _QosPQIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 6, 1, 3),
    _QosPQIfName_Type()
)
qosPQIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPQIfName.setStatus("mandatory")


class _QosPQTopPkt_Type(Integer32):
    """Custom type qosPQTopPkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_QosPQTopPkt_Type.__name__ = "Integer32"
_QosPQTopPkt_Object = MibTableColumn
qosPQTopPkt = _QosPQTopPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 6, 1, 4),
    _QosPQTopPkt_Type()
)
qosPQTopPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPQTopPkt.setStatus("mandatory")
_QosPQTopDiscard_Type = Counter32
_QosPQTopDiscard_Object = MibTableColumn
qosPQTopDiscard = _QosPQTopDiscard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 6, 1, 5),
    _QosPQTopDiscard_Type()
)
qosPQTopDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPQTopDiscard.setStatus("mandatory")


class _QosPQTopMaxQueLen_Type(Integer32):
    """Custom type qosPQTopMaxQueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QosPQTopMaxQueLen_Type.__name__ = "Integer32"
_QosPQTopMaxQueLen_Object = MibTableColumn
qosPQTopMaxQueLen = _QosPQTopMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 6, 1, 6),
    _QosPQTopMaxQueLen_Type()
)
qosPQTopMaxQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPQTopMaxQueLen.setStatus("mandatory")


class _QosPQMiddlePkt_Type(Integer32):
    """Custom type qosPQMiddlePkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_QosPQMiddlePkt_Type.__name__ = "Integer32"
_QosPQMiddlePkt_Object = MibTableColumn
qosPQMiddlePkt = _QosPQMiddlePkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 6, 1, 7),
    _QosPQMiddlePkt_Type()
)
qosPQMiddlePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPQMiddlePkt.setStatus("mandatory")
_QosPQMiddleDiscard_Type = Counter32
_QosPQMiddleDiscard_Object = MibTableColumn
qosPQMiddleDiscard = _QosPQMiddleDiscard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 6, 1, 8),
    _QosPQMiddleDiscard_Type()
)
qosPQMiddleDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPQMiddleDiscard.setStatus("mandatory")


class _QosPQMiddleMaxQueLen_Type(Integer32):
    """Custom type qosPQMiddleMaxQueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QosPQMiddleMaxQueLen_Type.__name__ = "Integer32"
_QosPQMiddleMaxQueLen_Object = MibTableColumn
qosPQMiddleMaxQueLen = _QosPQMiddleMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 6, 1, 9),
    _QosPQMiddleMaxQueLen_Type()
)
qosPQMiddleMaxQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPQMiddleMaxQueLen.setStatus("mandatory")


class _QosPQNormalPkt_Type(Integer32):
    """Custom type qosPQNormalPkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_QosPQNormalPkt_Type.__name__ = "Integer32"
_QosPQNormalPkt_Object = MibTableColumn
qosPQNormalPkt = _QosPQNormalPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 6, 1, 10),
    _QosPQNormalPkt_Type()
)
qosPQNormalPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPQNormalPkt.setStatus("mandatory")
_QosPQNormalDiscard_Type = Counter32
_QosPQNormalDiscard_Object = MibTableColumn
qosPQNormalDiscard = _QosPQNormalDiscard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 6, 1, 11),
    _QosPQNormalDiscard_Type()
)
qosPQNormalDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPQNormalDiscard.setStatus("mandatory")


class _QosPQNormalMaxQueLen_Type(Integer32):
    """Custom type qosPQNormalMaxQueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QosPQNormalMaxQueLen_Type.__name__ = "Integer32"
_QosPQNormalMaxQueLen_Object = MibTableColumn
qosPQNormalMaxQueLen = _QosPQNormalMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 6, 1, 12),
    _QosPQNormalMaxQueLen_Type()
)
qosPQNormalMaxQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPQNormalMaxQueLen.setStatus("mandatory")


class _QosPQBottomPkt_Type(Integer32):
    """Custom type qosPQBottomPkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_QosPQBottomPkt_Type.__name__ = "Integer32"
_QosPQBottomPkt_Object = MibTableColumn
qosPQBottomPkt = _QosPQBottomPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 6, 1, 13),
    _QosPQBottomPkt_Type()
)
qosPQBottomPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPQBottomPkt.setStatus("mandatory")
_QosPQBottomDiscard_Type = Counter32
_QosPQBottomDiscard_Object = MibTableColumn
qosPQBottomDiscard = _QosPQBottomDiscard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 6, 1, 14),
    _QosPQBottomDiscard_Type()
)
qosPQBottomDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPQBottomDiscard.setStatus("mandatory")


class _QosPQBottomMaxQueLen_Type(Integer32):
    """Custom type qosPQBottomMaxQueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QosPQBottomMaxQueLen_Type.__name__ = "Integer32"
_QosPQBottomMaxQueLen_Object = MibTableColumn
qosPQBottomMaxQueLen = _QosPQBottomMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 6, 1, 15),
    _QosPQBottomMaxQueLen_Type()
)
qosPQBottomMaxQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPQBottomMaxQueLen.setStatus("mandatory")


class _QosUndoPQ_Type(Integer32):
    """Custom type qosUndoPQ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("qosNoPQ", 1),
          ("qosPQ", 0))
    )


_QosUndoPQ_Type.__name__ = "Integer32"
_QosUndoPQ_Object = MibTableColumn
qosUndoPQ = _QosUndoPQ_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 6, 1, 16),
    _QosUndoPQ_Type()
)
qosUndoPQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosUndoPQ.setStatus("mandatory")
_QosCqlDefaultTable_Object = MibTable
qosCqlDefaultTable = _QosCqlDefaultTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 7)
)
if mibBuilder.loadTexts:
    qosCqlDefaultTable.setStatus("mandatory")
_QosCqlDefaultEntry_Object = MibTableRow
qosCqlDefaultEntry = _QosCqlDefaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 7, 1)
)
qosCqlDefaultEntry.setIndexNames(
    (0, "HUAWEI-IF-QOS-MIB", "qosCqlListNum"),
)
if mibBuilder.loadTexts:
    qosCqlDefaultEntry.setStatus("mandatory")


class _QosCqlListNum_Type(Integer32):
    """Custom type qosCqlListNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_QosCqlListNum_Type.__name__ = "Integer32"
_QosCqlListNum_Object = MibTableColumn
qosCqlListNum = _QosCqlListNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 7, 1, 1),
    _QosCqlListNum_Type()
)
qosCqlListNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCqlListNum.setStatus("mandatory")


class _QosCqlQueueNum_Type(Integer32):
    """Custom type qosCqlQueueNum based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_QosCqlQueueNum_Type.__name__ = "Integer32"
_QosCqlQueueNum_Object = MibTableColumn
qosCqlQueueNum = _QosCqlQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 7, 1, 2),
    _QosCqlQueueNum_Type()
)
qosCqlQueueNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosCqlQueueNum.setStatus("mandatory")


class _QosUndoCqlDefault_Type(Integer32):
    """Custom type qosUndoCqlDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("qosCqlDefault", 0),
          ("qosNoCqlDefault", 1))
    )


_QosUndoCqlDefault_Type.__name__ = "Integer32"
_QosUndoCqlDefault_Object = MibTableColumn
qosUndoCqlDefault = _QosUndoCqlDefault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 7, 1, 3),
    _QosUndoCqlDefault_Type()
)
qosUndoCqlDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosUndoCqlDefault.setStatus("mandatory")
_QosCqlIfTable_Object = MibTable
qosCqlIfTable = _QosCqlIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 8)
)
if mibBuilder.loadTexts:
    qosCqlIfTable.setStatus("mandatory")
_QosCqlIfEntry_Object = MibTableRow
qosCqlIfEntry = _QosCqlIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 8, 1)
)
qosCqlIfEntry.setIndexNames(
    (0, "HUAWEI-IF-QOS-MIB", "qosCqlIfListNum"),
    (0, "HUAWEI-IF-QOS-MIB", "qosCqlIfIndex"),
)
if mibBuilder.loadTexts:
    qosCqlIfEntry.setStatus("mandatory")
_QosCqlIfListNum_Type = Integer32
_QosCqlIfListNum_Object = MibTableColumn
qosCqlIfListNum = _QosCqlIfListNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 8, 1, 1),
    _QosCqlIfListNum_Type()
)
qosCqlIfListNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCqlIfListNum.setStatus("mandatory")
_QosCqlIfIndex_Type = Integer32
_QosCqlIfIndex_Object = MibTableColumn
qosCqlIfIndex = _QosCqlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 8, 1, 2),
    _QosCqlIfIndex_Type()
)
qosCqlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCqlIfIndex.setStatus("mandatory")
_QosCqlIfName_Type = OctetString
_QosCqlIfName_Object = MibTableColumn
qosCqlIfName = _QosCqlIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 8, 1, 3),
    _QosCqlIfName_Type()
)
qosCqlIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCqlIfName.setStatus("mandatory")


class _QosCqlIfQueueNum_Type(Integer32):
    """Custom type qosCqlIfQueueNum based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_QosCqlIfQueueNum_Type.__name__ = "Integer32"
_QosCqlIfQueueNum_Object = MibTableColumn
qosCqlIfQueueNum = _QosCqlIfQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 8, 1, 4),
    _QosCqlIfQueueNum_Type()
)
qosCqlIfQueueNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosCqlIfQueueNum.setStatus("mandatory")


class _QosUndoCqlIf_Type(Integer32):
    """Custom type qosUndoCqlIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("qosCqlIf", 0),
          ("qosNoCqlIf", 1))
    )


_QosUndoCqlIf_Type.__name__ = "Integer32"
_QosUndoCqlIf_Object = MibTableColumn
qosUndoCqlIf = _QosUndoCqlIf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 8, 1, 5),
    _QosUndoCqlIf_Type()
)
qosUndoCqlIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosUndoCqlIf.setStatus("mandatory")
_QosCqlProtocolTable_Object = MibTable
qosCqlProtocolTable = _QosCqlProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 9)
)
if mibBuilder.loadTexts:
    qosCqlProtocolTable.setStatus("mandatory")
_QosCqlProtocolEntry_Object = MibTableRow
qosCqlProtocolEntry = _QosCqlProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 9, 1)
)
qosCqlProtocolEntry.setIndexNames(
    (0, "HUAWEI-IF-QOS-MIB", "qosCqlProListNum"),
    (0, "HUAWEI-IF-QOS-MIB", "qosCqlProName"),
    (0, "HUAWEI-IF-QOS-MIB", "qosCqlProQueKey"),
    (0, "HUAWEI-IF-QOS-MIB", "qosCqlProQueKeyValue"),
)
if mibBuilder.loadTexts:
    qosCqlProtocolEntry.setStatus("mandatory")
_QosCqlProListNum_Type = Integer32
_QosCqlProListNum_Object = MibTableColumn
qosCqlProListNum = _QosCqlProListNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 9, 1, 1),
    _QosCqlProListNum_Type()
)
qosCqlProListNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCqlProListNum.setStatus("mandatory")


class _QosCqlProName_Type(Integer32):
    """Custom type qosCqlProName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("mpls", 2))
    )


_QosCqlProName_Type.__name__ = "Integer32"
_QosCqlProName_Object = MibTableColumn
qosCqlProName = _QosCqlProName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 9, 1, 2),
    _QosCqlProName_Type()
)
qosCqlProName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCqlProName.setStatus("mandatory")


class _QosCqlProQueKey_Type(Integer32):
    """Custom type qosCqlProQueKey based on Integer32"""
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
        *(("acl", 3),
          ("exp-mask", 8),
          ("fragment", 2),
          ("greater-than", 5),
          ("less-than", 4),
          ("null", 1),
          ("tcp", 6),
          ("udp", 7))
    )


_QosCqlProQueKey_Type.__name__ = "Integer32"
_QosCqlProQueKey_Object = MibTableColumn
qosCqlProQueKey = _QosCqlProQueKey_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 9, 1, 3),
    _QosCqlProQueKey_Type()
)
qosCqlProQueKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCqlProQueKey.setStatus("mandatory")


class _QosCqlProQueKeyValue_Type(Integer32):
    """Custom type qosCqlProQueKeyValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QosCqlProQueKeyValue_Type.__name__ = "Integer32"
_QosCqlProQueKeyValue_Object = MibTableColumn
qosCqlProQueKeyValue = _QosCqlProQueKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 9, 1, 4),
    _QosCqlProQueKeyValue_Type()
)
qosCqlProQueKeyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCqlProQueKeyValue.setStatus("mandatory")


class _QosCqlProQueNum_Type(Integer32):
    """Custom type qosCqlProQueNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_QosCqlProQueNum_Type.__name__ = "Integer32"
_QosCqlProQueNum_Object = MibTableColumn
qosCqlProQueNum = _QosCqlProQueNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 9, 1, 5),
    _QosCqlProQueNum_Type()
)
qosCqlProQueNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosCqlProQueNum.setStatus("mandatory")


class _QosUndoCqlProtocol_Type(Integer32):
    """Custom type qosUndoCqlProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("qosCqlProtocol", 0),
          ("qosNoCqlProtocol", 1))
    )


_QosUndoCqlProtocol_Type.__name__ = "Integer32"
_QosUndoCqlProtocol_Object = MibTableColumn
qosUndoCqlProtocol = _QosUndoCqlProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 9, 1, 6),
    _QosUndoCqlProtocol_Type()
)
qosUndoCqlProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosUndoCqlProtocol.setStatus("mandatory")
_QosCqlQueParaTable_Object = MibTable
qosCqlQueParaTable = _QosCqlQueParaTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 10)
)
if mibBuilder.loadTexts:
    qosCqlQueParaTable.setStatus("mandatory")
_QosCqlQueParaEntry_Object = MibTableRow
qosCqlQueParaEntry = _QosCqlQueParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 10, 1)
)
qosCqlQueParaEntry.setIndexNames(
    (0, "HUAWEI-IF-QOS-MIB", "qosCqlQueParaListNum"),
    (0, "HUAWEI-IF-QOS-MIB", "qosCqlQueParaQueNum"),
)
if mibBuilder.loadTexts:
    qosCqlQueParaEntry.setStatus("mandatory")
_QosCqlQueParaListNum_Type = Integer32
_QosCqlQueParaListNum_Object = MibTableColumn
qosCqlQueParaListNum = _QosCqlQueParaListNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 10, 1, 1),
    _QosCqlQueParaListNum_Type()
)
qosCqlQueParaListNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCqlQueParaListNum.setStatus("mandatory")


class _QosCqlQueParaQueNum_Type(Integer32):
    """Custom type qosCqlQueParaQueNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_QosCqlQueParaQueNum_Type.__name__ = "Integer32"
_QosCqlQueParaQueNum_Object = MibTableColumn
qosCqlQueParaQueNum = _QosCqlQueParaQueNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 10, 1, 2),
    _QosCqlQueParaQueNum_Type()
)
qosCqlQueParaQueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCqlQueParaQueNum.setStatus("mandatory")


class _QosCqlQueParaServing_Type(Integer32):
    """Custom type qosCqlQueParaServing based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_QosCqlQueParaServing_Type.__name__ = "Integer32"
_QosCqlQueParaServing_Object = MibTableColumn
qosCqlQueParaServing = _QosCqlQueParaServing_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 10, 1, 3),
    _QosCqlQueParaServing_Type()
)
qosCqlQueParaServing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosCqlQueParaServing.setStatus("mandatory")


class _QosCqlQueParaMaxQueLen_Type(Integer32):
    """Custom type qosCqlQueParaMaxQueLen based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QosCqlQueParaMaxQueLen_Type.__name__ = "Integer32"
_QosCqlQueParaMaxQueLen_Object = MibTableColumn
qosCqlQueParaMaxQueLen = _QosCqlQueParaMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 10, 1, 4),
    _QosCqlQueParaMaxQueLen_Type()
)
qosCqlQueParaMaxQueLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosCqlQueParaMaxQueLen.setStatus("mandatory")


class _QosUndoCqlQueParaServing_Type(Integer32):
    """Custom type qosUndoCqlQueParaServing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("qosCqlQueParaServing", 0),
          ("qosNoCqlQueParaServing", 1))
    )


_QosUndoCqlQueParaServing_Type.__name__ = "Integer32"
_QosUndoCqlQueParaServing_Object = MibTableColumn
qosUndoCqlQueParaServing = _QosUndoCqlQueParaServing_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 10, 1, 5),
    _QosUndoCqlQueParaServing_Type()
)
qosUndoCqlQueParaServing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosUndoCqlQueParaServing.setStatus("mandatory")


class _QosUndoCqlQueParaMaxQueLen_Type(Integer32):
    """Custom type qosUndoCqlQueParaMaxQueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("qosCqlQueParaMaxQueLen", 0),
          ("qosNoCqlQueParaMaxQueLen", 1))
    )


_QosUndoCqlQueParaMaxQueLen_Type.__name__ = "Integer32"
_QosUndoCqlQueParaMaxQueLen_Object = MibTableColumn
qosUndoCqlQueParaMaxQueLen = _QosUndoCqlQueParaMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 10, 1, 6),
    _QosUndoCqlQueParaMaxQueLen_Type()
)
qosUndoCqlQueParaMaxQueLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosUndoCqlQueParaMaxQueLen.setStatus("mandatory")
_QosCQTable_Object = MibTable
qosCQTable = _QosCQTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 11)
)
if mibBuilder.loadTexts:
    qosCQTable.setStatus("mandatory")
_QosCQEntry_Object = MibTableRow
qosCQEntry = _QosCQEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 11, 1)
)
qosCQEntry.setIndexNames(
    (0, "HUAWEI-IF-QOS-MIB", "qosCQIfIndex"),
)
if mibBuilder.loadTexts:
    qosCQEntry.setStatus("mandatory")
_QosCQIfIndex_Type = Integer32
_QosCQIfIndex_Object = MibTableColumn
qosCQIfIndex = _QosCQIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 11, 1, 1),
    _QosCQIfIndex_Type()
)
qosCQIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCQIfIndex.setStatus("mandatory")


class _QosCQListNum_Type(Integer32):
    """Custom type qosCQListNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_QosCQListNum_Type.__name__ = "Integer32"
_QosCQListNum_Object = MibTableColumn
qosCQListNum = _QosCQListNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 11, 1, 2),
    _QosCQListNum_Type()
)
qosCQListNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosCQListNum.setStatus("mandatory")
_QosCQIfName_Type = OctetString
_QosCQIfName_Object = MibTableColumn
qosCQIfName = _QosCQIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 11, 1, 3),
    _QosCQIfName_Type()
)
qosCQIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCQIfName.setStatus("mandatory")


class _QosUndoCQ_Type(Integer32):
    """Custom type qosUndoCQ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("qosCQ", 0),
          ("qosNoCQ", 1))
    )


_QosUndoCQ_Type.__name__ = "Integer32"
_QosUndoCQ_Object = MibTableColumn
qosUndoCQ = _QosUndoCQ_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 11, 1, 4),
    _QosUndoCQ_Type()
)
qosUndoCQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosUndoCQ.setStatus("mandatory")
_QosCQRunInfoTable_Object = MibTable
qosCQRunInfoTable = _QosCQRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 12)
)
if mibBuilder.loadTexts:
    qosCQRunInfoTable.setStatus("mandatory")
_QosCQRunInfoEntry_Object = MibTableRow
qosCQRunInfoEntry = _QosCQRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 12, 1)
)
qosCQRunInfoEntry.setIndexNames(
    (0, "HUAWEI-IF-QOS-MIB", "qosCQRunInfoIfIndex"),
    (0, "HUAWEI-IF-QOS-MIB", "qosCQRunInfoQueNum"),
)
if mibBuilder.loadTexts:
    qosCQRunInfoEntry.setStatus("mandatory")
_QosCQRunInfoIfIndex_Type = Integer32
_QosCQRunInfoIfIndex_Object = MibTableColumn
qosCQRunInfoIfIndex = _QosCQRunInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 12, 1, 1),
    _QosCQRunInfoIfIndex_Type()
)
qosCQRunInfoIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCQRunInfoIfIndex.setStatus("mandatory")


class _QosCQRunInfoQueNum_Type(Integer32):
    """Custom type qosCQRunInfoQueNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_QosCQRunInfoQueNum_Type.__name__ = "Integer32"
_QosCQRunInfoQueNum_Object = MibTableColumn
qosCQRunInfoQueNum = _QosCQRunInfoQueNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 12, 1, 2),
    _QosCQRunInfoQueNum_Type()
)
qosCQRunInfoQueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCQRunInfoQueNum.setStatus("mandatory")
_QosCQRunInfoIfName_Type = OctetString
_QosCQRunInfoIfName_Object = MibTableColumn
qosCQRunInfoIfName = _QosCQRunInfoIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 12, 1, 3),
    _QosCQRunInfoIfName_Type()
)
qosCQRunInfoIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCQRunInfoIfName.setStatus("mandatory")


class _QosCQRunInfoQuePkt_Type(Integer32):
    """Custom type qosCQRunInfoQuePkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_QosCQRunInfoQuePkt_Type.__name__ = "Integer32"
_QosCQRunInfoQuePkt_Object = MibTableColumn
qosCQRunInfoQuePkt = _QosCQRunInfoQuePkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 12, 1, 4),
    _QosCQRunInfoQuePkt_Type()
)
qosCQRunInfoQuePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCQRunInfoQuePkt.setStatus("mandatory")
_QosCQRunInfoQueDiscard_Type = Counter32
_QosCQRunInfoQueDiscard_Object = MibTableColumn
qosCQRunInfoQueDiscard = _QosCQRunInfoQueDiscard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 12, 1, 5),
    _QosCQRunInfoQueDiscard_Type()
)
qosCQRunInfoQueDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCQRunInfoQueDiscard.setStatus("mandatory")


class _QosCQRunInfoMaxQueLen_Type(Integer32):
    """Custom type qosCQRunInfoMaxQueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QosCQRunInfoMaxQueLen_Type.__name__ = "Integer32"
_QosCQRunInfoMaxQueLen_Object = MibTableColumn
qosCQRunInfoMaxQueLen = _QosCQRunInfoMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 12, 1, 6),
    _QosCQRunInfoMaxQueLen_Type()
)
qosCQRunInfoMaxQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCQRunInfoMaxQueLen.setStatus("mandatory")
_QosWFQTable_Object = MibTable
qosWFQTable = _QosWFQTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 13)
)
if mibBuilder.loadTexts:
    qosWFQTable.setStatus("mandatory")
_QosWFQEntry_Object = MibTableRow
qosWFQEntry = _QosWFQEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 13, 1)
)
qosWFQEntry.setIndexNames(
    (0, "HUAWEI-IF-QOS-MIB", "qosWFQIfIndex"),
)
if mibBuilder.loadTexts:
    qosWFQEntry.setStatus("mandatory")
_QosWFQIfIndex_Type = Integer32
_QosWFQIfIndex_Object = MibTableColumn
qosWFQIfIndex = _QosWFQIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 13, 1, 1),
    _QosWFQIfIndex_Type()
)
qosWFQIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosWFQIfIndex.setStatus("mandatory")
_QosWFQIfName_Type = OctetString
_QosWFQIfName_Object = MibTableColumn
qosWFQIfName = _QosWFQIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 13, 1, 2),
    _QosWFQIfName_Type()
)
qosWFQIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosWFQIfName.setStatus("mandatory")


class _QosWFQMaxQueLen_Type(Integer32):
    """Custom type qosWFQMaxQueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QosWFQMaxQueLen_Type.__name__ = "Integer32"
_QosWFQMaxQueLen_Object = MibTableColumn
qosWFQMaxQueLen = _QosWFQMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 13, 1, 3),
    _QosWFQMaxQueLen_Type()
)
qosWFQMaxQueLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosWFQMaxQueLen.setStatus("mandatory")


class _QosWFQTotalQueNum_Type(Integer32):
    """Custom type qosWFQTotalQueNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32,
              64,
              128,
              256,
              512,
              1024,
              2048,
              4096)
        )
    )
    namedValues = NamedValues(
        *(("a1024", 1024),
          ("a128", 128),
          ("a16", 16),
          ("a2048", 2048),
          ("a256", 256),
          ("a32", 32),
          ("a4096", 4096),
          ("a512", 512),
          ("a64", 64))
    )


_QosWFQTotalQueNum_Type.__name__ = "Integer32"
_QosWFQTotalQueNum_Object = MibTableColumn
qosWFQTotalQueNum = _QosWFQTotalQueNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 13, 1, 4),
    _QosWFQTotalQueNum_Type()
)
qosWFQTotalQueNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosWFQTotalQueNum.setStatus("mandatory")
_QosWFQCurQueLen_Type = Integer32
_QosWFQCurQueLen_Object = MibTableColumn
qosWFQCurQueLen = _QosWFQCurQueLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 13, 1, 5),
    _QosWFQCurQueLen_Type()
)
qosWFQCurQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosWFQCurQueLen.setStatus("mandatory")
_QosWFQTotalDiscard_Type = Counter32
_QosWFQTotalDiscard_Object = MibTableColumn
qosWFQTotalDiscard = _QosWFQTotalDiscard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 13, 1, 6),
    _QosWFQTotalDiscard_Type()
)
qosWFQTotalDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosWFQTotalDiscard.setStatus("mandatory")


class _QosWFQActiveQueNum_Type(Integer32):
    """Custom type qosWFQActiveQueNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_QosWFQActiveQueNum_Type.__name__ = "Integer32"
_QosWFQActiveQueNum_Object = MibTableColumn
qosWFQActiveQueNum = _QosWFQActiveQueNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 13, 1, 7),
    _QosWFQActiveQueNum_Type()
)
qosWFQActiveQueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosWFQActiveQueNum.setStatus("mandatory")


class _QosWFQMaxActiveQueNum_Type(Integer32):
    """Custom type qosWFQMaxActiveQueNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_QosWFQMaxActiveQueNum_Type.__name__ = "Integer32"
_QosWFQMaxActiveQueNum_Object = MibTableColumn
qosWFQMaxActiveQueNum = _QosWFQMaxActiveQueNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 13, 1, 8),
    _QosWFQMaxActiveQueNum_Type()
)
qosWFQMaxActiveQueNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosWFQMaxActiveQueNum.setStatus("mandatory")


class _QosUndoWFQ_Type(Integer32):
    """Custom type qosUndoWFQ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("qosNoWFQ", 1),
          ("qosWFQ", 0))
    )


_QosUndoWFQ_Type.__name__ = "Integer32"
_QosUndoWFQ_Object = MibTableColumn
qosUndoWFQ = _QosUndoWFQ_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 13, 1, 9),
    _QosUndoWFQ_Type()
)
qosUndoWFQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosUndoWFQ.setStatus("mandatory")
_QosWREDTable_Object = MibTable
qosWREDTable = _QosWREDTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 14)
)
if mibBuilder.loadTexts:
    qosWREDTable.setStatus("mandatory")
_QosWREDEntry_Object = MibTableRow
qosWREDEntry = _QosWREDEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 14, 1)
)
qosWREDEntry.setIndexNames(
    (0, "HUAWEI-IF-QOS-MIB", "qosWREDIfIndex"),
)
if mibBuilder.loadTexts:
    qosWREDEntry.setStatus("mandatory")
_QosWREDIfIndex_Type = Integer32
_QosWREDIfIndex_Object = MibTableColumn
qosWREDIfIndex = _QosWREDIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 14, 1, 1),
    _QosWREDIfIndex_Type()
)
qosWREDIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosWREDIfIndex.setStatus("mandatory")
_QosWREDIfName_Type = OctetString
_QosWREDIfName_Object = MibTableColumn
qosWREDIfName = _QosWREDIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 14, 1, 2),
    _QosWREDIfName_Type()
)
qosWREDIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosWREDIfName.setStatus("mandatory")


class _QosWREDWeightConstant_Type(Integer32):
    """Custom type qosWREDWeightConstant based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_QosWREDWeightConstant_Type.__name__ = "Integer32"
_QosWREDWeightConstant_Object = MibTableColumn
qosWREDWeightConstant = _QosWREDWeightConstant_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 14, 1, 3),
    _QosWREDWeightConstant_Type()
)
qosWREDWeightConstant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosWREDWeightConstant.setStatus("mandatory")


class _QosWREDEnable_Type(Integer32):
    """Custom type qosWREDEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_QosWREDEnable_Type.__name__ = "Integer32"
_QosWREDEnable_Object = MibTableColumn
qosWREDEnable = _QosWREDEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 14, 1, 4),
    _QosWREDEnable_Type()
)
qosWREDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosWREDEnable.setStatus("mandatory")


class _QosUndoWREDWeightConstant_Type(Integer32):
    """Custom type qosUndoWREDWeightConstant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("qosNoWREDExponent", 1),
          ("qosWREDExponent", 0))
    )


_QosUndoWREDWeightConstant_Type.__name__ = "Integer32"
_QosUndoWREDWeightConstant_Object = MibTableColumn
qosUndoWREDWeightConstant = _QosUndoWREDWeightConstant_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 14, 1, 5),
    _QosUndoWREDWeightConstant_Type()
)
qosUndoWREDWeightConstant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosUndoWREDWeightConstant.setStatus("mandatory")
_QosWREDPreTable_Object = MibTable
qosWREDPreTable = _QosWREDPreTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 15)
)
if mibBuilder.loadTexts:
    qosWREDPreTable.setStatus("mandatory")
_QosWREDPreEntry_Object = MibTableRow
qosWREDPreEntry = _QosWREDPreEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 15, 1)
)
qosWREDPreEntry.setIndexNames(
    (0, "HUAWEI-IF-QOS-MIB", "qosWREDPreIfIndex"),
    (0, "HUAWEI-IF-QOS-MIB", "qosWREDPrecedence"),
)
if mibBuilder.loadTexts:
    qosWREDPreEntry.setStatus("mandatory")
_QosWREDPreIfIndex_Type = Integer32
_QosWREDPreIfIndex_Object = MibTableColumn
qosWREDPreIfIndex = _QosWREDPreIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 15, 1, 1),
    _QosWREDPreIfIndex_Type()
)
qosWREDPreIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosWREDPreIfIndex.setStatus("mandatory")


class _QosWREDPrecedence_Type(Integer32):
    """Custom type qosWREDPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosWREDPrecedence_Type.__name__ = "Integer32"
_QosWREDPrecedence_Object = MibTableColumn
qosWREDPrecedence = _QosWREDPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 15, 1, 2),
    _QosWREDPrecedence_Type()
)
qosWREDPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosWREDPrecedence.setStatus("mandatory")
_QosWREDPreIfName_Type = OctetString
_QosWREDPreIfName_Object = MibTableColumn
qosWREDPreIfName = _QosWREDPreIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 15, 1, 3),
    _QosWREDPreIfName_Type()
)
qosWREDPreIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosWREDPreIfName.setStatus("mandatory")


class _QosWREDPreLowLimit_Type(Integer32):
    """Custom type qosWREDPreLowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QosWREDPreLowLimit_Type.__name__ = "Integer32"
_QosWREDPreLowLimit_Object = MibTableColumn
qosWREDPreLowLimit = _QosWREDPreLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 15, 1, 4),
    _QosWREDPreLowLimit_Type()
)
qosWREDPreLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosWREDPreLowLimit.setStatus("mandatory")


class _QosWREDPreHighLimit_Type(Integer32):
    """Custom type qosWREDPreHighLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QosWREDPreHighLimit_Type.__name__ = "Integer32"
_QosWREDPreHighLimit_Object = MibTableColumn
qosWREDPreHighLimit = _QosWREDPreHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 15, 1, 5),
    _QosWREDPreHighLimit_Type()
)
qosWREDPreHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosWREDPreHighLimit.setStatus("mandatory")


class _QosWREDPreDiscardProbability_Type(Integer32):
    """Custom type qosWREDPreDiscardProbability based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_QosWREDPreDiscardProbability_Type.__name__ = "Integer32"
_QosWREDPreDiscardProbability_Object = MibTableColumn
qosWREDPreDiscardProbability = _QosWREDPreDiscardProbability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 15, 1, 6),
    _QosWREDPreDiscardProbability_Type()
)
qosWREDPreDiscardProbability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosWREDPreDiscardProbability.setStatus("mandatory")
_QosWREDPreRandomDropNum_Type = Counter32
_QosWREDPreRandomDropNum_Object = MibTableColumn
qosWREDPreRandomDropNum = _QosWREDPreRandomDropNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 15, 1, 7),
    _QosWREDPreRandomDropNum_Type()
)
qosWREDPreRandomDropNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosWREDPreRandomDropNum.setStatus("mandatory")
_QosWREDPreTailDropNum_Type = Counter32
_QosWREDPreTailDropNum_Object = MibTableColumn
qosWREDPreTailDropNum = _QosWREDPreTailDropNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 15, 1, 8),
    _QosWREDPreTailDropNum_Type()
)
qosWREDPreTailDropNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosWREDPreTailDropNum.setStatus("mandatory")


class _QosUndoWREDPre_Type(Integer32):
    """Custom type qosUndoWREDPre based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("qosNoWREDPre", 1),
          ("qosWREDPre", 0))
    )


_QosUndoWREDPre_Type.__name__ = "Integer32"
_QosUndoWREDPre_Object = MibTableColumn
qosUndoWREDPre = _QosUndoWREDPre_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 15, 1, 9),
    _QosUndoWREDPre_Type()
)
qosUndoWREDPre.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosUndoWREDPre.setStatus("mandatory")
_QosCarlTable_Object = MibTable
qosCarlTable = _QosCarlTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 16)
)
if mibBuilder.loadTexts:
    qosCarlTable.setStatus("mandatory")
_QosCarlEntry_Object = MibTableRow
qosCarlEntry = _QosCarlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 16, 1)
)
qosCarlEntry.setIndexNames(
    (0, "HUAWEI-IF-QOS-MIB", "qosCarlListNum"),
)
if mibBuilder.loadTexts:
    qosCarlEntry.setStatus("mandatory")
_QosCarlListNum_Type = Integer32
_QosCarlListNum_Object = MibTableColumn
qosCarlListNum = _QosCarlListNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 16, 1, 1),
    _QosCarlListNum_Type()
)
qosCarlListNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCarlListNum.setStatus("mandatory")


class _QosCarlParaType_Type(Integer32):
    """Custom type qosCarlParaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dscp-mask", 3),
          ("mac-address", 1),
          ("prec-mask", 2))
    )


_QosCarlParaType_Type.__name__ = "Integer32"
_QosCarlParaType_Object = MibTableColumn
qosCarlParaType = _QosCarlParaType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 16, 1, 2),
    _QosCarlParaType_Type()
)
qosCarlParaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosCarlParaType.setStatus("mandatory")
_QosCarlParaValue_Type = OctetString
_QosCarlParaValue_Object = MibTableColumn
qosCarlParaValue = _QosCarlParaValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 16, 1, 3),
    _QosCarlParaValue_Type()
)
qosCarlParaValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosCarlParaValue.setStatus("mandatory")


class _QosUndoCarl_Type(Integer32):
    """Custom type qosUndoCarl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("qosCARL", 0),
          ("qosNoCARL", 1))
    )


_QosUndoCarl_Type.__name__ = "Integer32"
_QosUndoCarl_Object = MibTableColumn
qosUndoCarl = _QosUndoCarl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 16, 1, 4),
    _QosUndoCarl_Type()
)
qosUndoCarl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosUndoCarl.setStatus("mandatory")
_QosCARTable_Object = MibTable
qosCARTable = _QosCARTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 17)
)
if mibBuilder.loadTexts:
    qosCARTable.setStatus("mandatory")
_QosCAREntry_Object = MibTableRow
qosCAREntry = _QosCAREntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 17, 1)
)
qosCAREntry.setIndexNames(
    (0, "HUAWEI-IF-QOS-MIB", "qosCARIfIndex"),
    (0, "HUAWEI-IF-QOS-MIB", "qosCARPktDirection"),
    (0, "HUAWEI-IF-QOS-MIB", "qosCARType"),
    (0, "HUAWEI-IF-QOS-MIB", "qosCARListNum"),
    (0, "HUAWEI-IF-QOS-MIB", "qosCARCIR"),
    (0, "HUAWEI-IF-QOS-MIB", "qosCARBurstSize"),
    (0, "HUAWEI-IF-QOS-MIB", "qosCARExcessBurstSize"),
)
if mibBuilder.loadTexts:
    qosCAREntry.setStatus("mandatory")
_QosCARIfIndex_Type = Integer32
_QosCARIfIndex_Object = MibTableColumn
qosCARIfIndex = _QosCARIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 17, 1, 1),
    _QosCARIfIndex_Type()
)
qosCARIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCARIfIndex.setStatus("mandatory")
_QosCARIfName_Type = OctetString
_QosCARIfName_Object = MibTableColumn
qosCARIfName = _QosCARIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 17, 1, 2),
    _QosCARIfName_Type()
)
qosCARIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCARIfName.setStatus("mandatory")


class _QosCARPktDirection_Type(Integer32):
    """Custom type qosCARPktDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_QosCARPktDirection_Type.__name__ = "Integer32"
_QosCARPktDirection_Object = MibTableColumn
qosCARPktDirection = _QosCARPktDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 17, 1, 3),
    _QosCARPktDirection_Type()
)
qosCARPktDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCARPktDirection.setStatus("mandatory")


class _QosCARType_Type(Integer32):
    """Custom type qosCARType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acl", 1),
          ("all", 3),
          ("carl", 2))
    )


_QosCARType_Type.__name__ = "Integer32"
_QosCARType_Object = MibTableColumn
qosCARType = _QosCARType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 17, 1, 4),
    _QosCARType_Type()
)
qosCARType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCARType.setStatus("mandatory")


class _QosCARListNum_Type(Integer32):
    """Custom type qosCARListNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
        ValueRangeConstraint(2000, 3999),
    )


_QosCARListNum_Type.__name__ = "Integer32"
_QosCARListNum_Object = MibTableColumn
qosCARListNum = _QosCARListNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 17, 1, 5),
    _QosCARListNum_Type()
)
qosCARListNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCARListNum.setStatus("mandatory")


class _QosCARCIR_Type(Integer32):
    """Custom type qosCARCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8000, 155000000),
    )


_QosCARCIR_Type.__name__ = "Integer32"
_QosCARCIR_Object = MibTableColumn
qosCARCIR = _QosCARCIR_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 17, 1, 6),
    _QosCARCIR_Type()
)
qosCARCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCARCIR.setStatus("mandatory")


class _QosCARBurstSize_Type(Integer32):
    """Custom type qosCARBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15000, 155000000),
    )


_QosCARBurstSize_Type.__name__ = "Integer32"
_QosCARBurstSize_Object = MibTableColumn
qosCARBurstSize = _QosCARBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 17, 1, 7),
    _QosCARBurstSize_Type()
)
qosCARBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCARBurstSize.setStatus("mandatory")


class _QosCARExcessBurstSize_Type(Integer32):
    """Custom type qosCARExcessBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000000),
    )


_QosCARExcessBurstSize_Type.__name__ = "Integer32"
_QosCARExcessBurstSize_Object = MibTableColumn
qosCARExcessBurstSize = _QosCARExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 17, 1, 8),
    _QosCARExcessBurstSize_Type()
)
qosCARExcessBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCARExcessBurstSize.setStatus("mandatory")


class _QosCARConformAction_Type(Integer32):
    """Custom type qosCARConformAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("continue", 1),
          ("discard", 2),
          ("pass", 5),
          ("remark-mplsexp-continue", 6),
          ("remark-mplsexp-pass", 7),
          ("remark-prec-continue", 3),
          ("remark-prec-pass", 4))
    )


_QosCARConformAction_Type.__name__ = "Integer32"
_QosCARConformAction_Object = MibTableColumn
qosCARConformAction = _QosCARConformAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 17, 1, 9),
    _QosCARConformAction_Type()
)
qosCARConformAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosCARConformAction.setStatus("mandatory")


class _QosCARExceedAction_Type(Integer32):
    """Custom type qosCARExceedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("continue", 1),
          ("discard", 2),
          ("pass", 5),
          ("remark-mplsexp-continue", 6),
          ("remark-mplsexp-pass", 7),
          ("remark-prec-continue", 3),
          ("remark-prec-pass", 4))
    )


_QosCARExceedAction_Type.__name__ = "Integer32"
_QosCARExceedAction_Object = MibTableColumn
qosCARExceedAction = _QosCARExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 17, 1, 10),
    _QosCARExceedAction_Type()
)
qosCARExceedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosCARExceedAction.setStatus("mandatory")


class _QosCARConformNewPrec_Type(Integer32):
    """Custom type qosCARConformNewPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosCARConformNewPrec_Type.__name__ = "Integer32"
_QosCARConformNewPrec_Object = MibTableColumn
qosCARConformNewPrec = _QosCARConformNewPrec_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 17, 1, 11),
    _QosCARConformNewPrec_Type()
)
qosCARConformNewPrec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosCARConformNewPrec.setStatus("mandatory")


class _QosCARExceedNewPrec_Type(Integer32):
    """Custom type qosCARExceedNewPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosCARExceedNewPrec_Type.__name__ = "Integer32"
_QosCARExceedNewPrec_Object = MibTableColumn
qosCARExceedNewPrec = _QosCARExceedNewPrec_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 17, 1, 12),
    _QosCARExceedNewPrec_Type()
)
qosCARExceedNewPrec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosCARExceedNewPrec.setStatus("mandatory")
_QosCARConformPkt_Type = Counter32
_QosCARConformPkt_Object = MibTableColumn
qosCARConformPkt = _QosCARConformPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 17, 1, 13),
    _QosCARConformPkt_Type()
)
qosCARConformPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCARConformPkt.setStatus("mandatory")
_QosCARConformByte_Type = Counter32
_QosCARConformByte_Object = MibTableColumn
qosCARConformByte = _QosCARConformByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 17, 1, 14),
    _QosCARConformByte_Type()
)
qosCARConformByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCARConformByte.setStatus("mandatory")
_QosCARExceedPkt_Type = Counter32
_QosCARExceedPkt_Object = MibTableColumn
qosCARExceedPkt = _QosCARExceedPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 17, 1, 15),
    _QosCARExceedPkt_Type()
)
qosCARExceedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCARExceedPkt.setStatus("mandatory")
_QosCARExceedByte_Type = Counter32
_QosCARExceedByte_Object = MibTableColumn
qosCARExceedByte = _QosCARExceedByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 17, 1, 16),
    _QosCARExceedByte_Type()
)
qosCARExceedByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCARExceedByte.setStatus("mandatory")


class _QosUndoCAR_Type(Integer32):
    """Custom type qosUndoCAR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("qosCAR", 0),
          ("qosNoCAR", 1))
    )


_QosUndoCAR_Type.__name__ = "Integer32"
_QosUndoCAR_Object = MibTableColumn
qosUndoCAR = _QosUndoCAR_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 17, 1, 17),
    _QosUndoCAR_Type()
)
qosUndoCAR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosUndoCAR.setStatus("mandatory")
_QosGTSTable_Object = MibTable
qosGTSTable = _QosGTSTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 18)
)
if mibBuilder.loadTexts:
    qosGTSTable.setStatus("mandatory")
_QosGTSEntry_Object = MibTableRow
qosGTSEntry = _QosGTSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 18, 1)
)
qosGTSEntry.setIndexNames(
    (0, "HUAWEI-IF-QOS-MIB", "qosGTSIfIndex"),
    (0, "HUAWEI-IF-QOS-MIB", "qosGTSType"),
    (0, "HUAWEI-IF-QOS-MIB", "qosGTSACLNum"),
)
if mibBuilder.loadTexts:
    qosGTSEntry.setStatus("mandatory")
_QosGTSIfIndex_Type = Integer32
_QosGTSIfIndex_Object = MibTableColumn
qosGTSIfIndex = _QosGTSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 18, 1, 1),
    _QosGTSIfIndex_Type()
)
qosGTSIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosGTSIfIndex.setStatus("mandatory")
_QosGTSIfName_Type = OctetString
_QosGTSIfName_Object = MibTableColumn
qosGTSIfName = _QosGTSIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 18, 1, 2),
    _QosGTSIfName_Type()
)
qosGTSIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosGTSIfName.setStatus("mandatory")


class _QosGTSType_Type(Integer32):
    """Custom type qosGTSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acl", 1),
          ("all", 2))
    )


_QosGTSType_Type.__name__ = "Integer32"
_QosGTSType_Object = MibTableColumn
qosGTSType = _QosGTSType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 18, 1, 3),
    _QosGTSType_Type()
)
qosGTSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosGTSType.setStatus("mandatory")


class _QosGTSACLNum_Type(Integer32):
    """Custom type qosGTSACLNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
    )


_QosGTSACLNum_Type.__name__ = "Integer32"
_QosGTSACLNum_Object = MibTableColumn
qosGTSACLNum = _QosGTSACLNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 18, 1, 4),
    _QosGTSACLNum_Type()
)
qosGTSACLNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosGTSACLNum.setStatus("mandatory")


class _QosGTSCIR_Type(Integer32):
    """Custom type qosGTSCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8000, 155000000),
    )


_QosGTSCIR_Type.__name__ = "Integer32"
_QosGTSCIR_Object = MibTableColumn
qosGTSCIR = _QosGTSCIR_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 18, 1, 5),
    _QosGTSCIR_Type()
)
qosGTSCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosGTSCIR.setStatus("mandatory")


class _QosGTSBurstSize_Type(Integer32):
    """Custom type qosGTSBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15000, 155000000),
    )


_QosGTSBurstSize_Type.__name__ = "Integer32"
_QosGTSBurstSize_Object = MibTableColumn
qosGTSBurstSize = _QosGTSBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 18, 1, 6),
    _QosGTSBurstSize_Type()
)
qosGTSBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosGTSBurstSize.setStatus("mandatory")


class _QosGTSExcessBurstSize_Type(Integer32):
    """Custom type qosGTSExcessBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000000),
    )


_QosGTSExcessBurstSize_Type.__name__ = "Integer32"
_QosGTSExcessBurstSize_Object = MibTableColumn
qosGTSExcessBurstSize = _QosGTSExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 18, 1, 7),
    _QosGTSExcessBurstSize_Type()
)
qosGTSExcessBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosGTSExcessBurstSize.setStatus("mandatory")


class _QosGTSMaxQueLen_Type(Integer32):
    """Custom type qosGTSMaxQueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QosGTSMaxQueLen_Type.__name__ = "Integer32"
_QosGTSMaxQueLen_Object = MibTableColumn
qosGTSMaxQueLen = _QosGTSMaxQueLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 18, 1, 8),
    _QosGTSMaxQueLen_Type()
)
qosGTSMaxQueLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosGTSMaxQueLen.setStatus("mandatory")
_QosGTSCurQueLen_Type = Integer32
_QosGTSCurQueLen_Object = MibTableColumn
qosGTSCurQueLen = _QosGTSCurQueLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 18, 1, 9),
    _QosGTSCurQueLen_Type()
)
qosGTSCurQueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosGTSCurQueLen.setStatus("mandatory")
_QosGTSPassPkt_Type = Counter32
_QosGTSPassPkt_Object = MibTableColumn
qosGTSPassPkt = _QosGTSPassPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 18, 1, 10),
    _QosGTSPassPkt_Type()
)
qosGTSPassPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosGTSPassPkt.setStatus("mandatory")
_QosGTSPassByte_Type = Counter32
_QosGTSPassByte_Object = MibTableColumn
qosGTSPassByte = _QosGTSPassByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 18, 1, 11),
    _QosGTSPassByte_Type()
)
qosGTSPassByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosGTSPassByte.setStatus("mandatory")
_QosGTSDelayPkt_Type = Counter32
_QosGTSDelayPkt_Object = MibTableColumn
qosGTSDelayPkt = _QosGTSDelayPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 18, 1, 12),
    _QosGTSDelayPkt_Type()
)
qosGTSDelayPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosGTSDelayPkt.setStatus("mandatory")
_QosGTSDelayByte_Type = Counter32
_QosGTSDelayByte_Object = MibTableColumn
qosGTSDelayByte = _QosGTSDelayByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 18, 1, 13),
    _QosGTSDelayByte_Type()
)
qosGTSDelayByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosGTSDelayByte.setStatus("mandatory")
_QosGTSDiscardPkt_Type = Counter32
_QosGTSDiscardPkt_Object = MibTableColumn
qosGTSDiscardPkt = _QosGTSDiscardPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 18, 1, 14),
    _QosGTSDiscardPkt_Type()
)
qosGTSDiscardPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosGTSDiscardPkt.setStatus("mandatory")
_QosGTSDiscardByte_Type = Counter32
_QosGTSDiscardByte_Object = MibTableColumn
qosGTSDiscardByte = _QosGTSDiscardByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 18, 1, 15),
    _QosGTSDiscardByte_Type()
)
qosGTSDiscardByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosGTSDiscardByte.setStatus("mandatory")


class _QosUndoGTS_Type(Integer32):
    """Custom type qosUndoGTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("qosGTS", 0),
          ("qosNoGTS", 1))
    )


_QosUndoGTS_Type.__name__ = "Integer32"
_QosUndoGTS_Object = MibTableColumn
qosUndoGTS = _QosUndoGTS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 18, 1, 16),
    _QosUndoGTS_Type()
)
qosUndoGTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosUndoGTS.setStatus("mandatory")
_QosLRTable_Object = MibTable
qosLRTable = _QosLRTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 19)
)
if mibBuilder.loadTexts:
    qosLRTable.setStatus("mandatory")
_QosLREntry_Object = MibTableRow
qosLREntry = _QosLREntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 19, 1)
)
qosLREntry.setIndexNames(
    (0, "HUAWEI-IF-QOS-MIB", "qosLRIfIndex"),
)
if mibBuilder.loadTexts:
    qosLREntry.setStatus("mandatory")
_QosLRIfIndex_Type = Integer32
_QosLRIfIndex_Object = MibTableColumn
qosLRIfIndex = _QosLRIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 19, 1, 1),
    _QosLRIfIndex_Type()
)
qosLRIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosLRIfIndex.setStatus("mandatory")
_QosLRIfName_Type = OctetString
_QosLRIfName_Object = MibTableColumn
qosLRIfName = _QosLRIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 19, 1, 2),
    _QosLRIfName_Type()
)
qosLRIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosLRIfName.setStatus("mandatory")


class _QosLRCIR_Type(Integer32):
    """Custom type qosLRCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8000, 155000000),
    )


_QosLRCIR_Type.__name__ = "Integer32"
_QosLRCIR_Object = MibTableColumn
qosLRCIR = _QosLRCIR_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 19, 1, 3),
    _QosLRCIR_Type()
)
qosLRCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosLRCIR.setStatus("mandatory")


class _QosLRBurstSize_Type(Integer32):
    """Custom type qosLRBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15000, 155000000),
    )


_QosLRBurstSize_Type.__name__ = "Integer32"
_QosLRBurstSize_Object = MibTableColumn
qosLRBurstSize = _QosLRBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 19, 1, 4),
    _QosLRBurstSize_Type()
)
qosLRBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosLRBurstSize.setStatus("mandatory")


class _QosLRExcessBurstSize_Type(Integer32):
    """Custom type qosLRExcessBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 155000000),
    )


_QosLRExcessBurstSize_Type.__name__ = "Integer32"
_QosLRExcessBurstSize_Object = MibTableColumn
qosLRExcessBurstSize = _QosLRExcessBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 19, 1, 5),
    _QosLRExcessBurstSize_Type()
)
qosLRExcessBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosLRExcessBurstSize.setStatus("mandatory")
_QosLRPassPkt_Type = Counter32
_QosLRPassPkt_Object = MibTableColumn
qosLRPassPkt = _QosLRPassPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 19, 1, 6),
    _QosLRPassPkt_Type()
)
qosLRPassPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosLRPassPkt.setStatus("mandatory")
_QosLRPassByte_Type = Counter32
_QosLRPassByte_Object = MibTableColumn
qosLRPassByte = _QosLRPassByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 19, 1, 7),
    _QosLRPassByte_Type()
)
qosLRPassByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosLRPassByte.setStatus("mandatory")
_QosLRDelayPkt_Type = Counter32
_QosLRDelayPkt_Object = MibTableColumn
qosLRDelayPkt = _QosLRDelayPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 19, 1, 8),
    _QosLRDelayPkt_Type()
)
qosLRDelayPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosLRDelayPkt.setStatus("mandatory")
_QosLRDelayByte_Type = Counter32
_QosLRDelayByte_Object = MibTableColumn
qosLRDelayByte = _QosLRDelayByte_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 19, 1, 9),
    _QosLRDelayByte_Type()
)
qosLRDelayByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosLRDelayByte.setStatus("mandatory")


class _QosUndoLR_Type(Integer32):
    """Custom type qosUndoLR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("qosLR", 0),
          ("qosNoLR", 1))
    )


_QosUndoLR_Type.__name__ = "Integer32"
_QosUndoLR_Object = MibTableColumn
qosUndoLR = _QosUndoLR_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 19, 1, 10),
    _QosUndoLR_Type()
)
qosUndoLR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosUndoLR.setStatus("mandatory")
_QosIfBandwidthTable_Object = MibTable
qosIfBandwidthTable = _QosIfBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 20)
)
if mibBuilder.loadTexts:
    qosIfBandwidthTable.setStatus("current")
_QosIfBandwidthEntry_Object = MibTableRow
qosIfBandwidthEntry = _QosIfBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 20, 1)
)
qosIfBandwidthEntry.setIndexNames(
    (0, "HUAWEI-IF-QOS-MIB", "qosIfBandwidthIfIndex"),
)
if mibBuilder.loadTexts:
    qosIfBandwidthEntry.setStatus("current")
_QosIfBandwidthIfIndex_Type = Integer32
_QosIfBandwidthIfIndex_Object = MibTableColumn
qosIfBandwidthIfIndex = _QosIfBandwidthIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 20, 1, 1),
    _QosIfBandwidthIfIndex_Type()
)
qosIfBandwidthIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIfBandwidthIfIndex.setStatus("current")


class _QosIFBandwidthMaxBW_Type(Integer32):
    """Custom type qosIFBandwidthMaxBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_QosIFBandwidthMaxBW_Type.__name__ = "Integer32"
_QosIFBandwidthMaxBW_Object = MibTableColumn
qosIFBandwidthMaxBW = _QosIFBandwidthMaxBW_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 20, 1, 2),
    _QosIFBandwidthMaxBW_Type()
)
qosIFBandwidthMaxBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosIFBandwidthMaxBW.setStatus("current")


class _QosIFBandwidthMaxReservedBWPct_Type(Integer32):
    """Custom type qosIFBandwidthMaxReservedBWPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_QosIFBandwidthMaxReservedBWPct_Type.__name__ = "Integer32"
_QosIFBandwidthMaxReservedBWPct_Object = MibTableColumn
qosIFBandwidthMaxReservedBWPct = _QosIFBandwidthMaxReservedBWPct_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 20, 1, 3),
    _QosIFBandwidthMaxReservedBWPct_Type()
)
qosIFBandwidthMaxReservedBWPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosIFBandwidthMaxReservedBWPct.setStatus("current")
_QosIFBandwidthMaxReservedBW_Type = Integer32
_QosIFBandwidthMaxReservedBW_Object = MibTableColumn
qosIFBandwidthMaxReservedBW = _QosIFBandwidthMaxReservedBW_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 20, 1, 4),
    _QosIFBandwidthMaxReservedBW_Type()
)
qosIFBandwidthMaxReservedBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIFBandwidthMaxReservedBW.setStatus("current")
_QosIFBandwidthAvailable_Type = Integer32
_QosIFBandwidthAvailable_Object = MibTableColumn
qosIFBandwidthAvailable = _QosIFBandwidthAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 20, 1, 5),
    _QosIFBandwidthAvailable_Type()
)
qosIFBandwidthAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIFBandwidthAvailable.setStatus("current")
_QosIFBandwidthRowStatus_Type = RowStatus
_QosIFBandwidthRowStatus_Object = MibTableColumn
qosIFBandwidthRowStatus = _QosIFBandwidthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 20, 1, 6),
    _QosIFBandwidthRowStatus_Type()
)
qosIFBandwidthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIFBandwidthRowStatus.setStatus("current")
_QosRTPIfApplyTable_Object = MibTable
qosRTPIfApplyTable = _QosRTPIfApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 21)
)
if mibBuilder.loadTexts:
    qosRTPIfApplyTable.setStatus("current")
_QosRTPIfApplyEntry_Object = MibTableRow
qosRTPIfApplyEntry = _QosRTPIfApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 21, 1)
)
qosRTPIfApplyEntry.setIndexNames(
    (0, "HUAWEI-IF-QOS-MIB", "qosRTPIfApplyIfIndex"),
)
if mibBuilder.loadTexts:
    qosRTPIfApplyEntry.setStatus("current")
_QosRTPIfApplyIfIndex_Type = Integer32
_QosRTPIfApplyIfIndex_Object = MibTableColumn
qosRTPIfApplyIfIndex = _QosRTPIfApplyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 21, 1, 1),
    _QosRTPIfApplyIfIndex_Type()
)
qosRTPIfApplyIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosRTPIfApplyIfIndex.setStatus("current")


class _QosRTPIfApplyStartPort_Type(Integer32):
    """Custom type qosRTPIfApplyStartPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 65535),
    )


_QosRTPIfApplyStartPort_Type.__name__ = "Integer32"
_QosRTPIfApplyStartPort_Object = MibTableColumn
qosRTPIfApplyStartPort = _QosRTPIfApplyStartPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 21, 1, 2),
    _QosRTPIfApplyStartPort_Type()
)
qosRTPIfApplyStartPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosRTPIfApplyStartPort.setStatus("current")


class _QosRTPIfApplyEndPort_Type(Integer32):
    """Custom type qosRTPIfApplyEndPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 65535),
    )


_QosRTPIfApplyEndPort_Type.__name__ = "Integer32"
_QosRTPIfApplyEndPort_Object = MibTableColumn
qosRTPIfApplyEndPort = _QosRTPIfApplyEndPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 21, 1, 3),
    _QosRTPIfApplyEndPort_Type()
)
qosRTPIfApplyEndPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosRTPIfApplyEndPort.setStatus("current")


class _QosRTPIfApplyBandWidth_Type(Integer32):
    """Custom type qosRTPIfApplyBandWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 1000000),
    )


_QosRTPIfApplyBandWidth_Type.__name__ = "Integer32"
_QosRTPIfApplyBandWidth_Object = MibTableColumn
qosRTPIfApplyBandWidth = _QosRTPIfApplyBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 21, 1, 4),
    _QosRTPIfApplyBandWidth_Type()
)
qosRTPIfApplyBandWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosRTPIfApplyBandWidth.setStatus("current")


class _QosRTPIfApplyCbs_Type(Integer32):
    """Custom type qosRTPIfApplyCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 2000000),
    )


_QosRTPIfApplyCbs_Type.__name__ = "Integer32"
_QosRTPIfApplyCbs_Object = MibTableColumn
qosRTPIfApplyCbs = _QosRTPIfApplyCbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 21, 1, 5),
    _QosRTPIfApplyCbs_Type()
)
qosRTPIfApplyCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosRTPIfApplyCbs.setStatus("current")
_QosRTPIfApplyRowStatus_Type = RowStatus
_QosRTPIfApplyRowStatus_Object = MibTableColumn
qosRTPIfApplyRowStatus = _QosRTPIfApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 21, 1, 6),
    _QosRTPIfApplyRowStatus_Type()
)
qosRTPIfApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosRTPIfApplyRowStatus.setStatus("current")
_QosRTPIfQueueRunInfoTable_Object = MibTable
qosRTPIfQueueRunInfoTable = _QosRTPIfQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 22)
)
if mibBuilder.loadTexts:
    qosRTPIfQueueRunInfoTable.setStatus("current")
_QosRTPIfQueueRunInfoEntry_Object = MibTableRow
qosRTPIfQueueRunInfoEntry = _QosRTPIfQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 22, 1)
)
qosRTPIfQueueRunInfoEntry.setIndexNames(
    (0, "HUAWEI-IF-QOS-MIB", "qosRTPIfApplyIfIndex"),
)
if mibBuilder.loadTexts:
    qosRTPIfQueueRunInfoEntry.setStatus("current")
_QosRTPIfQueueSize_Type = Counter32
_QosRTPIfQueueSize_Object = MibTableColumn
qosRTPIfQueueSize = _QosRTPIfQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 22, 1, 1),
    _QosRTPIfQueueSize_Type()
)
qosRTPIfQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosRTPIfQueueSize.setStatus("current")
_QosRTPIfQueueMaxSize_Type = Counter32
_QosRTPIfQueueMaxSize_Object = MibTableColumn
qosRTPIfQueueMaxSize = _QosRTPIfQueueMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 22, 1, 2),
    _QosRTPIfQueueMaxSize_Type()
)
qosRTPIfQueueMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosRTPIfQueueMaxSize.setStatus("current")
_QosRTPIfQueueOutputs_Type = Counter32
_QosRTPIfQueueOutputs_Object = MibTableColumn
qosRTPIfQueueOutputs = _QosRTPIfQueueOutputs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 22, 1, 3),
    _QosRTPIfQueueOutputs_Type()
)
qosRTPIfQueueOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosRTPIfQueueOutputs.setStatus("current")
_QosRTPIfQueueDiscards_Type = Counter32
_QosRTPIfQueueDiscards_Object = MibTableColumn
qosRTPIfQueueDiscards = _QosRTPIfQueueDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 32, 2, 22, 1, 4),
    _QosRTPIfQueueDiscards_Type()
)
qosRTPIfQueueDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosRTPIfQueueDiscards.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-IF-QOS-MIB",
    **{"hwQoS": hwQoS,
       "hwIfQoSMib": hwIfQoSMib,
       "qosFIFOTable": qosFIFOTable,
       "qosFIFOEntry": qosFIFOEntry,
       "qosFIFOIfIndex": qosFIFOIfIndex,
       "qosFIFOIfName": qosFIFOIfName,
       "qosFIFOMaxQueueLen": qosFIFOMaxQueueLen,
       "qosFIFOCurQueueLen": qosFIFOCurQueueLen,
       "qosFIFODiscardPkt": qosFIFODiscardPkt,
       "qosUndoFIFO": qosUndoFIFO,
       "qosPqlDefaultTable": qosPqlDefaultTable,
       "qosPqlDefaultEntry": qosPqlDefaultEntry,
       "qosPqlDefaultListNum": qosPqlDefaultListNum,
       "qosPqlDefaultQueueType": qosPqlDefaultQueueType,
       "qosUndoPqlDefault": qosUndoPqlDefault,
       "qosPqlQueueLenTable": qosPqlQueueLenTable,
       "qosPqlQueueLenEntry": qosPqlQueueLenEntry,
       "qosPqlQueLenListNum": qosPqlQueLenListNum,
       "qosPqlQueLenQueueType": qosPqlQueLenQueueType,
       "qosPqlQueLenValue": qosPqlQueLenValue,
       "qosUndoPqlQueLen": qosUndoPqlQueLen,
       "qosPqlIfTable": qosPqlIfTable,
       "qosPqlIfEntry": qosPqlIfEntry,
       "qosPqlIfListNum": qosPqlIfListNum,
       "qosPqlIfIndex": qosPqlIfIndex,
       "qosPqlIfName": qosPqlIfName,
       "qosPqlIfQueueType": qosPqlIfQueueType,
       "qosUndoPqlIf": qosUndoPqlIf,
       "qosPqlProtocolTable": qosPqlProtocolTable,
       "qosPqlProtocolEntry": qosPqlProtocolEntry,
       "qosPqlProListNum": qosPqlProListNum,
       "qosPqlProName": qosPqlProName,
       "qosPqlProQueKey": qosPqlProQueKey,
       "qosPqlProQueKeyValue": qosPqlProQueKeyValue,
       "qosPqlProQueType": qosPqlProQueType,
       "qosUndoPqlProtocol": qosUndoPqlProtocol,
       "qosPQTable": qosPQTable,
       "qosPQEntry": qosPQEntry,
       "qosPQIfIndex": qosPQIfIndex,
       "qosPQListNum": qosPQListNum,
       "qosPQIfName": qosPQIfName,
       "qosPQTopPkt": qosPQTopPkt,
       "qosPQTopDiscard": qosPQTopDiscard,
       "qosPQTopMaxQueLen": qosPQTopMaxQueLen,
       "qosPQMiddlePkt": qosPQMiddlePkt,
       "qosPQMiddleDiscard": qosPQMiddleDiscard,
       "qosPQMiddleMaxQueLen": qosPQMiddleMaxQueLen,
       "qosPQNormalPkt": qosPQNormalPkt,
       "qosPQNormalDiscard": qosPQNormalDiscard,
       "qosPQNormalMaxQueLen": qosPQNormalMaxQueLen,
       "qosPQBottomPkt": qosPQBottomPkt,
       "qosPQBottomDiscard": qosPQBottomDiscard,
       "qosPQBottomMaxQueLen": qosPQBottomMaxQueLen,
       "qosUndoPQ": qosUndoPQ,
       "qosCqlDefaultTable": qosCqlDefaultTable,
       "qosCqlDefaultEntry": qosCqlDefaultEntry,
       "qosCqlListNum": qosCqlListNum,
       "qosCqlQueueNum": qosCqlQueueNum,
       "qosUndoCqlDefault": qosUndoCqlDefault,
       "qosCqlIfTable": qosCqlIfTable,
       "qosCqlIfEntry": qosCqlIfEntry,
       "qosCqlIfListNum": qosCqlIfListNum,
       "qosCqlIfIndex": qosCqlIfIndex,
       "qosCqlIfName": qosCqlIfName,
       "qosCqlIfQueueNum": qosCqlIfQueueNum,
       "qosUndoCqlIf": qosUndoCqlIf,
       "qosCqlProtocolTable": qosCqlProtocolTable,
       "qosCqlProtocolEntry": qosCqlProtocolEntry,
       "qosCqlProListNum": qosCqlProListNum,
       "qosCqlProName": qosCqlProName,
       "qosCqlProQueKey": qosCqlProQueKey,
       "qosCqlProQueKeyValue": qosCqlProQueKeyValue,
       "qosCqlProQueNum": qosCqlProQueNum,
       "qosUndoCqlProtocol": qosUndoCqlProtocol,
       "qosCqlQueParaTable": qosCqlQueParaTable,
       "qosCqlQueParaEntry": qosCqlQueParaEntry,
       "qosCqlQueParaListNum": qosCqlQueParaListNum,
       "qosCqlQueParaQueNum": qosCqlQueParaQueNum,
       "qosCqlQueParaServing": qosCqlQueParaServing,
       "qosCqlQueParaMaxQueLen": qosCqlQueParaMaxQueLen,
       "qosUndoCqlQueParaServing": qosUndoCqlQueParaServing,
       "qosUndoCqlQueParaMaxQueLen": qosUndoCqlQueParaMaxQueLen,
       "qosCQTable": qosCQTable,
       "qosCQEntry": qosCQEntry,
       "qosCQIfIndex": qosCQIfIndex,
       "qosCQListNum": qosCQListNum,
       "qosCQIfName": qosCQIfName,
       "qosUndoCQ": qosUndoCQ,
       "qosCQRunInfoTable": qosCQRunInfoTable,
       "qosCQRunInfoEntry": qosCQRunInfoEntry,
       "qosCQRunInfoIfIndex": qosCQRunInfoIfIndex,
       "qosCQRunInfoQueNum": qosCQRunInfoQueNum,
       "qosCQRunInfoIfName": qosCQRunInfoIfName,
       "qosCQRunInfoQuePkt": qosCQRunInfoQuePkt,
       "qosCQRunInfoQueDiscard": qosCQRunInfoQueDiscard,
       "qosCQRunInfoMaxQueLen": qosCQRunInfoMaxQueLen,
       "qosWFQTable": qosWFQTable,
       "qosWFQEntry": qosWFQEntry,
       "qosWFQIfIndex": qosWFQIfIndex,
       "qosWFQIfName": qosWFQIfName,
       "qosWFQMaxQueLen": qosWFQMaxQueLen,
       "qosWFQTotalQueNum": qosWFQTotalQueNum,
       "qosWFQCurQueLen": qosWFQCurQueLen,
       "qosWFQTotalDiscard": qosWFQTotalDiscard,
       "qosWFQActiveQueNum": qosWFQActiveQueNum,
       "qosWFQMaxActiveQueNum": qosWFQMaxActiveQueNum,
       "qosUndoWFQ": qosUndoWFQ,
       "qosWREDTable": qosWREDTable,
       "qosWREDEntry": qosWREDEntry,
       "qosWREDIfIndex": qosWREDIfIndex,
       "qosWREDIfName": qosWREDIfName,
       "qosWREDWeightConstant": qosWREDWeightConstant,
       "qosWREDEnable": qosWREDEnable,
       "qosUndoWREDWeightConstant": qosUndoWREDWeightConstant,
       "qosWREDPreTable": qosWREDPreTable,
       "qosWREDPreEntry": qosWREDPreEntry,
       "qosWREDPreIfIndex": qosWREDPreIfIndex,
       "qosWREDPrecedence": qosWREDPrecedence,
       "qosWREDPreIfName": qosWREDPreIfName,
       "qosWREDPreLowLimit": qosWREDPreLowLimit,
       "qosWREDPreHighLimit": qosWREDPreHighLimit,
       "qosWREDPreDiscardProbability": qosWREDPreDiscardProbability,
       "qosWREDPreRandomDropNum": qosWREDPreRandomDropNum,
       "qosWREDPreTailDropNum": qosWREDPreTailDropNum,
       "qosUndoWREDPre": qosUndoWREDPre,
       "qosCarlTable": qosCarlTable,
       "qosCarlEntry": qosCarlEntry,
       "qosCarlListNum": qosCarlListNum,
       "qosCarlParaType": qosCarlParaType,
       "qosCarlParaValue": qosCarlParaValue,
       "qosUndoCarl": qosUndoCarl,
       "qosCARTable": qosCARTable,
       "qosCAREntry": qosCAREntry,
       "qosCARIfIndex": qosCARIfIndex,
       "qosCARIfName": qosCARIfName,
       "qosCARPktDirection": qosCARPktDirection,
       "qosCARType": qosCARType,
       "qosCARListNum": qosCARListNum,
       "qosCARCIR": qosCARCIR,
       "qosCARBurstSize": qosCARBurstSize,
       "qosCARExcessBurstSize": qosCARExcessBurstSize,
       "qosCARConformAction": qosCARConformAction,
       "qosCARExceedAction": qosCARExceedAction,
       "qosCARConformNewPrec": qosCARConformNewPrec,
       "qosCARExceedNewPrec": qosCARExceedNewPrec,
       "qosCARConformPkt": qosCARConformPkt,
       "qosCARConformByte": qosCARConformByte,
       "qosCARExceedPkt": qosCARExceedPkt,
       "qosCARExceedByte": qosCARExceedByte,
       "qosUndoCAR": qosUndoCAR,
       "qosGTSTable": qosGTSTable,
       "qosGTSEntry": qosGTSEntry,
       "qosGTSIfIndex": qosGTSIfIndex,
       "qosGTSIfName": qosGTSIfName,
       "qosGTSType": qosGTSType,
       "qosGTSACLNum": qosGTSACLNum,
       "qosGTSCIR": qosGTSCIR,
       "qosGTSBurstSize": qosGTSBurstSize,
       "qosGTSExcessBurstSize": qosGTSExcessBurstSize,
       "qosGTSMaxQueLen": qosGTSMaxQueLen,
       "qosGTSCurQueLen": qosGTSCurQueLen,
       "qosGTSPassPkt": qosGTSPassPkt,
       "qosGTSPassByte": qosGTSPassByte,
       "qosGTSDelayPkt": qosGTSDelayPkt,
       "qosGTSDelayByte": qosGTSDelayByte,
       "qosGTSDiscardPkt": qosGTSDiscardPkt,
       "qosGTSDiscardByte": qosGTSDiscardByte,
       "qosUndoGTS": qosUndoGTS,
       "qosLRTable": qosLRTable,
       "qosLREntry": qosLREntry,
       "qosLRIfIndex": qosLRIfIndex,
       "qosLRIfName": qosLRIfName,
       "qosLRCIR": qosLRCIR,
       "qosLRBurstSize": qosLRBurstSize,
       "qosLRExcessBurstSize": qosLRExcessBurstSize,
       "qosLRPassPkt": qosLRPassPkt,
       "qosLRPassByte": qosLRPassByte,
       "qosLRDelayPkt": qosLRDelayPkt,
       "qosLRDelayByte": qosLRDelayByte,
       "qosUndoLR": qosUndoLR,
       "qosIfBandwidthTable": qosIfBandwidthTable,
       "qosIfBandwidthEntry": qosIfBandwidthEntry,
       "qosIfBandwidthIfIndex": qosIfBandwidthIfIndex,
       "qosIFBandwidthMaxBW": qosIFBandwidthMaxBW,
       "qosIFBandwidthMaxReservedBWPct": qosIFBandwidthMaxReservedBWPct,
       "qosIFBandwidthMaxReservedBW": qosIFBandwidthMaxReservedBW,
       "qosIFBandwidthAvailable": qosIFBandwidthAvailable,
       "qosIFBandwidthRowStatus": qosIFBandwidthRowStatus,
       "qosRTPIfApplyTable": qosRTPIfApplyTable,
       "qosRTPIfApplyEntry": qosRTPIfApplyEntry,
       "qosRTPIfApplyIfIndex": qosRTPIfApplyIfIndex,
       "qosRTPIfApplyStartPort": qosRTPIfApplyStartPort,
       "qosRTPIfApplyEndPort": qosRTPIfApplyEndPort,
       "qosRTPIfApplyBandWidth": qosRTPIfApplyBandWidth,
       "qosRTPIfApplyCbs": qosRTPIfApplyCbs,
       "qosRTPIfApplyRowStatus": qosRTPIfApplyRowStatus,
       "qosRTPIfQueueRunInfoTable": qosRTPIfQueueRunInfoTable,
       "qosRTPIfQueueRunInfoEntry": qosRTPIfQueueRunInfoEntry,
       "qosRTPIfQueueSize": qosRTPIfQueueSize,
       "qosRTPIfQueueMaxSize": qosRTPIfQueueMaxSize,
       "qosRTPIfQueueOutputs": qosRTPIfQueueOutputs,
       "qosRTPIfQueueDiscards": qosRTPIfQueueDiscards}
)
