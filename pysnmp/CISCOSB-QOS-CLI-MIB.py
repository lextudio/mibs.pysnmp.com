# SNMP MIB module (CISCOSB-QOS-CLI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCOSB-QOS-CLI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:14:43 2024
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

(Percents,
 switch001) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "Percents",
    "switch001")

(StatisticsClearActionType,
 StatisticsDPType) = mibBuilder.importSymbols(
    "CISCOSB-POLICY-MIB",
    "StatisticsClearActionType",
    "StatisticsDPType")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PortList,
 VlanId) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId")

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
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlQosCliMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88)
)
rlQosCliMib.setRevisions(
        ("2006-02-12 00:00",
         "2006-02-12 00:00",
         "2005-03-14 00:00",
         "2005-02-07 00:00",
         "2005-01-27 00:00",
         "2004-11-15 00:00",
         "2003-09-29 00:00",
         "2003-09-21 00:00",
         "2005-04-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ClassOffsetType(Integer32, TextualConvention):
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
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("ethertype", 11),
          ("in-port", 8),
          ("inner-vlan", 12),
          ("layer2-start", 2),
          ("layer3-ipv6-start", 13),
          ("layer3-start", 4),
          ("layer4-start", 5),
          ("layer5-start", 6),
          ("mpls-start", 3),
          ("out-port", 9),
          ("packetStart", 1),
          ("vlan", 7),
          ("vpt", 10))
    )



class ClassTupleType(Integer32, TextualConvention):
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32)
        )
    )
    namedValues = NamedValues(
        *(("dscp", 4),
          ("ether-type", 17),
          ("general", 15),
          ("icmp-code", 20),
          ("icmp-type", 19),
          ("igmp-type", 21),
          ("in-port", 13),
          ("inner-vlan", 22),
          ("ip-dest", 3),
          ("ip-precedence", 5),
          ("ip-src", 2),
          ("ipv6-dest", 24),
          ("ipv6-src", 23),
          ("mac-dest", 11),
          ("mac-src", 10),
          ("out-port", 14),
          ("protocol", 1),
          ("tcp-flags", 18),
          ("tcp-port-dest", 9),
          ("tcp-port-range-end-dest", 32),
          ("tcp-port-range-end-src", 30),
          ("tcp-port-range-start-dest", 31),
          ("tcp-port-range-start-src", 29),
          ("tcp-port-src", 8),
          ("udp-port-dest", 7),
          ("udp-port-range-end-dest", 28),
          ("udp-port-range-end-src", 26),
          ("udp-port-range-start-dest", 27),
          ("udp-port-range-start-src", 25),
          ("udp-port-src", 6),
          ("vlan", 12),
          ("vpt", 16))
    )



class AceActionType(Integer32, TextualConvention):
    status = "current"
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
        *(("deny", 2),
          ("deny-DisablePort", 3),
          ("deny-LogInput", 4),
          ("permit", 1))
    )



class AceObjectType(Integer32, TextualConvention):
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
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("ip-ICMP", 7),
          ("ip-IGMP", 8),
          ("ip-Offset", 4),
          ("ip-TCP", 2),
          ("ip-UDP", 3),
          ("ipv6", 9),
          ("ipv6-ICMP", 13),
          ("ipv6-Offset", 12),
          ("ipv6-TCP", 10),
          ("ipv6-UDP", 11),
          ("mac", 5),
          ("mac-Offset", 6))
    )



class AclObjectType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 2),
          ("ipv6", 3),
          ("mac", 1))
    )



class ClassMapType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("matchAll", 1),
          ("matchAny", 2))
    )



class ClassMapAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("setCos", 5),
          ("setDSCP", 3),
          ("setIP-Precedence", 2),
          ("setQueue", 4),
          ("trust", 6))
    )



class MarkVlanAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mark", 2),
          ("markNestedVlan", 3),
          ("noMark", 1))
    )



class RedirectAction(Integer32, TextualConvention):
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
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("analyzerPort", 6),
          ("disabled", 1),
          ("loopback", 7),
          ("mirror", 5),
          ("mirrorAndRedirectToInterface", 9),
          ("mirrorAndRedirectToInterfacesGroup", 10),
          ("redirectToAllPorts", 4),
          ("redirectToInterface", 3),
          ("redirectToPortGroup", 8),
          ("trap", 2))
    )



class PolicerType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aggregate", 2),
          ("cascade", 3),
          ("single", 1))
    )



class PolicerAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cascadePointer", 5),
          ("drop", 2),
          ("explicit-remark", 4),
          ("none", 1),
          ("remark", 3))
    )



class QosGlobalMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("advance", 3),
          ("basic", 2),
          ("disable", 1))
    )



class QosTrustMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cos", 1),
          ("cos-dscp", 3),
          ("dscp", 2))
    )



class BinaryStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )



class QueueType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ef", 1),
          ("wrr", 2))
    )



class AclDefaultAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("application-specific", 3),
          ("deny-all", 1),
          ("forward-all", 2))
    )



class InterfaceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port", 2),
          ("vlan", 1))
    )



class StatisticsCntrNumOfBitsType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32,
              48,
              64)
        )
    )
    namedValues = NamedValues(
        *(("uint32", 32),
          ("uint48", 48),
          ("uint64", 64))
    )



class StatisticsCntrType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("statisticsCntrTypeDeny", 2),
          ("statisticsCntrTypeSetDSCP", 1))
    )



class RlQosTimeBasedAclWeekPeriodicList(Bits, TextualConvention):
    status = "current"


class RlQosAceTidxActionDropType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardDrop", 1),
          ("softDrop", 2))
    )



class RlQosApplicationDefaultActionType(Integer32, TextualConvention):
    status = "current"
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
        *(("forward", 1),
          ("hard-Drop", 2),
          ("soft-Drop", 3),
          ("trap", 4))
    )



# MIB Managed Objects in the order of their OIDs

_RlQosCliQosMode_Type = QosGlobalMode
_RlQosCliQosMode_Object = MibScalar
rlQosCliQosMode = _RlQosCliQosMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 1),
    _RlQosCliQosMode_Type()
)
rlQosCliQosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosCliQosMode.setStatus("deprecated")
_RlQosCliBasicModeCfg_Type = QosTrustMode
_RlQosCliBasicModeCfg_Object = MibScalar
rlQosCliBasicModeCfg = _RlQosCliBasicModeCfg_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 2),
    _RlQosCliBasicModeCfg_Type()
)
rlQosCliBasicModeCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosCliBasicModeCfg.setStatus("deprecated")
_RlQosMaxNumOfAce_Type = Integer32
_RlQosMaxNumOfAce_Object = MibScalar
rlQosMaxNumOfAce = _RlQosMaxNumOfAce_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 3),
    _RlQosMaxNumOfAce_Type()
)
rlQosMaxNumOfAce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosMaxNumOfAce.setStatus("current")
_RlQosOffsetTable_Object = MibTable
rlQosOffsetTable = _RlQosOffsetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 4)
)
if mibBuilder.loadTexts:
    rlQosOffsetTable.setStatus("deprecated")
_RlQosOffsetEntry_Object = MibTableRow
rlQosOffsetEntry = _RlQosOffsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 4, 1)
)
rlQosOffsetEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosOffsetIndex"),
)
if mibBuilder.loadTexts:
    rlQosOffsetEntry.setStatus("deprecated")
_RlQosOffsetIndex_Type = Integer32
_RlQosOffsetIndex_Object = MibTableColumn
rlQosOffsetIndex = _RlQosOffsetIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 4, 1, 1),
    _RlQosOffsetIndex_Type()
)
rlQosOffsetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosOffsetIndex.setStatus("deprecated")
_RlQosOffsetType_Type = ClassOffsetType
_RlQosOffsetType_Object = MibTableColumn
rlQosOffsetType = _RlQosOffsetType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 4, 1, 2),
    _RlQosOffsetType_Type()
)
rlQosOffsetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosOffsetType.setStatus("deprecated")
_RlQosOffsetValue_Type = Integer32
_RlQosOffsetValue_Object = MibTableColumn
rlQosOffsetValue = _RlQosOffsetValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 4, 1, 3),
    _RlQosOffsetValue_Type()
)
rlQosOffsetValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosOffsetValue.setStatus("deprecated")


class _RlQosOffsetMask_Type(Integer32):
    """Custom type rlQosOffsetMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlQosOffsetMask_Type.__name__ = "Integer32"
_RlQosOffsetMask_Object = MibTableColumn
rlQosOffsetMask = _RlQosOffsetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 4, 1, 4),
    _RlQosOffsetMask_Type()
)
rlQosOffsetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosOffsetMask.setStatus("deprecated")


class _RlQosOffsetPattern_Type(Integer32):
    """Custom type rlQosOffsetPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlQosOffsetPattern_Type.__name__ = "Integer32"
_RlQosOffsetPattern_Object = MibTableColumn
rlQosOffsetPattern = _RlQosOffsetPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 4, 1, 5),
    _RlQosOffsetPattern_Type()
)
rlQosOffsetPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosOffsetPattern.setStatus("deprecated")
_RlQosOffsetTuplePointer_Type = Integer32
_RlQosOffsetTuplePointer_Object = MibTableColumn
rlQosOffsetTuplePointer = _RlQosOffsetTuplePointer_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 4, 1, 6),
    _RlQosOffsetTuplePointer_Type()
)
rlQosOffsetTuplePointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosOffsetTuplePointer.setStatus("deprecated")
_RlQosOffsetStatus_Type = RowStatus
_RlQosOffsetStatus_Object = MibTableColumn
rlQosOffsetStatus = _RlQosOffsetStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 4, 1, 7),
    _RlQosOffsetStatus_Type()
)
rlQosOffsetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosOffsetStatus.setStatus("deprecated")
_RlQosTupleTable_Object = MibTable
rlQosTupleTable = _RlQosTupleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 5)
)
if mibBuilder.loadTexts:
    rlQosTupleTable.setStatus("current")
_RlQosTupleEntry_Object = MibTableRow
rlQosTupleEntry = _RlQosTupleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 5, 1)
)
rlQosTupleEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosTupleIndex"),
)
if mibBuilder.loadTexts:
    rlQosTupleEntry.setStatus("current")
_RlQosTupleIndex_Type = Integer32
_RlQosTupleIndex_Object = MibTableColumn
rlQosTupleIndex = _RlQosTupleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 5, 1, 1),
    _RlQosTupleIndex_Type()
)
rlQosTupleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosTupleIndex.setStatus("current")
_RlQosTupleType_Type = ClassTupleType
_RlQosTupleType_Object = MibTableColumn
rlQosTupleType = _RlQosTupleType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 5, 1, 2),
    _RlQosTupleType_Type()
)
rlQosTupleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosTupleType.setStatus("current")
_RlQosTupleValue1_Type = Integer32
_RlQosTupleValue1_Object = MibTableColumn
rlQosTupleValue1 = _RlQosTupleValue1_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 5, 1, 3),
    _RlQosTupleValue1_Type()
)
rlQosTupleValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosTupleValue1.setStatus("current")


class _RlQosTupleValue2_Type(OctetString):
    """Custom type rlQosTupleValue2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlQosTupleValue2_Type.__name__ = "OctetString"
_RlQosTupleValue2_Object = MibTableColumn
rlQosTupleValue2 = _RlQosTupleValue2_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 5, 1, 4),
    _RlQosTupleValue2_Type()
)
rlQosTupleValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosTupleValue2.setStatus("current")
_RlQosTupleStatus_Type = RowStatus
_RlQosTupleStatus_Object = MibTableColumn
rlQosTupleStatus = _RlQosTupleStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 5, 1, 5),
    _RlQosTupleStatus_Type()
)
rlQosTupleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosTupleStatus.setStatus("current")
_RlQosAceTable_Object = MibTable
rlQosAceTable = _RlQosAceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 6)
)
if mibBuilder.loadTexts:
    rlQosAceTable.setStatus("current")
_RlQosAceEntry_Object = MibTableRow
rlQosAceEntry = _RlQosAceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 6, 1)
)
rlQosAceEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosAceIndex"),
)
if mibBuilder.loadTexts:
    rlQosAceEntry.setStatus("current")
_RlQosAceIndex_Type = Integer32
_RlQosAceIndex_Object = MibTableColumn
rlQosAceIndex = _RlQosAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 6, 1, 1),
    _RlQosAceIndex_Type()
)
rlQosAceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosAceIndex.setStatus("current")
_RlQosAceAction_Type = AceActionType
_RlQosAceAction_Object = MibTableColumn
rlQosAceAction = _RlQosAceAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 6, 1, 2),
    _RlQosAceAction_Type()
)
rlQosAceAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceAction.setStatus("current")
_RlQosAceType_Type = AceObjectType
_RlQosAceType_Object = MibTableColumn
rlQosAceType = _RlQosAceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 6, 1, 3),
    _RlQosAceType_Type()
)
rlQosAceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceType.setStatus("current")
_RlQosAceTuple1_Type = Integer32
_RlQosAceTuple1_Object = MibTableColumn
rlQosAceTuple1 = _RlQosAceTuple1_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 6, 1, 4),
    _RlQosAceTuple1_Type()
)
rlQosAceTuple1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTuple1.setStatus("current")
_RlQosAceTuple2_Type = Integer32
_RlQosAceTuple2_Object = MibTableColumn
rlQosAceTuple2 = _RlQosAceTuple2_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 6, 1, 5),
    _RlQosAceTuple2_Type()
)
rlQosAceTuple2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTuple2.setStatus("current")
_RlQosAceTuple3_Type = Integer32
_RlQosAceTuple3_Object = MibTableColumn
rlQosAceTuple3 = _RlQosAceTuple3_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 6, 1, 6),
    _RlQosAceTuple3_Type()
)
rlQosAceTuple3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTuple3.setStatus("current")
_RlQosAceTuple4_Type = Integer32
_RlQosAceTuple4_Object = MibTableColumn
rlQosAceTuple4 = _RlQosAceTuple4_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 6, 1, 7),
    _RlQosAceTuple4_Type()
)
rlQosAceTuple4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTuple4.setStatus("current")
_RlQosAceTuple5_Type = Integer32
_RlQosAceTuple5_Object = MibTableColumn
rlQosAceTuple5 = _RlQosAceTuple5_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 6, 1, 8),
    _RlQosAceTuple5_Type()
)
rlQosAceTuple5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTuple5.setStatus("current")
_RlQosAceTuple6_Type = Integer32
_RlQosAceTuple6_Object = MibTableColumn
rlQosAceTuple6 = _RlQosAceTuple6_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 6, 1, 9),
    _RlQosAceTuple6_Type()
)
rlQosAceTuple6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTuple6.setStatus("current")
_RlQosAceTuple7_Type = Integer32
_RlQosAceTuple7_Object = MibTableColumn
rlQosAceTuple7 = _RlQosAceTuple7_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 6, 1, 10),
    _RlQosAceTuple7_Type()
)
rlQosAceTuple7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTuple7.setStatus("current")
_RlQosAceTuple8_Type = Integer32
_RlQosAceTuple8_Object = MibTableColumn
rlQosAceTuple8 = _RlQosAceTuple8_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 6, 1, 11),
    _RlQosAceTuple8_Type()
)
rlQosAceTuple8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTuple8.setStatus("current")
_RlQosAceAccount_Type = BinaryStatus
_RlQosAceAccount_Object = MibTableColumn
rlQosAceAccount = _RlQosAceAccount_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 6, 1, 12),
    _RlQosAceAccount_Type()
)
rlQosAceAccount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceAccount.setStatus("current")
_RlQosAceStatus_Type = RowStatus
_RlQosAceStatus_Object = MibTableColumn
rlQosAceStatus = _RlQosAceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 6, 1, 13),
    _RlQosAceStatus_Type()
)
rlQosAceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceStatus.setStatus("current")
_RlQosAclTable_Object = MibTable
rlQosAclTable = _RlQosAclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 7)
)
if mibBuilder.loadTexts:
    rlQosAclTable.setStatus("current")
_RlQosAclEntry_Object = MibTableRow
rlQosAclEntry = _RlQosAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 7, 1)
)
rlQosAclEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosAclIndex"),
)
if mibBuilder.loadTexts:
    rlQosAclEntry.setStatus("current")
_RlQosAclIndex_Type = Integer32
_RlQosAclIndex_Object = MibTableColumn
rlQosAclIndex = _RlQosAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 7, 1, 1),
    _RlQosAclIndex_Type()
)
rlQosAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosAclIndex.setStatus("current")


class _RlQosAclName_Type(DisplayString):
    """Custom type rlQosAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlQosAclName_Type.__name__ = "DisplayString"
_RlQosAclName_Object = MibTableColumn
rlQosAclName = _RlQosAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 7, 1, 2),
    _RlQosAclName_Type()
)
rlQosAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAclName.setStatus("current")
_RlQosAclType_Type = AclObjectType
_RlQosAclType_Object = MibTableColumn
rlQosAclType = _RlQosAclType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 7, 1, 3),
    _RlQosAclType_Type()
)
rlQosAclType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAclType.setStatus("current")
_RlQosAclStatus_Type = RowStatus
_RlQosAclStatus_Object = MibTableColumn
rlQosAclStatus = _RlQosAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 7, 1, 4),
    _RlQosAclStatus_Type()
)
rlQosAclStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAclStatus.setStatus("current")
_RlQosAclNumOfAces_Type = Integer32
_RlQosAclNumOfAces_Object = MibTableColumn
rlQosAclNumOfAces = _RlQosAclNumOfAces_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 7, 1, 5),
    _RlQosAclNumOfAces_Type()
)
rlQosAclNumOfAces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosAclNumOfAces.setStatus("current")
_RlQosAclAceRefTable_Object = MibTable
rlQosAclAceRefTable = _RlQosAclAceRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 8)
)
if mibBuilder.loadTexts:
    rlQosAclAceRefTable.setStatus("current")
_RlQosAclAceRefEntry_Object = MibTableRow
rlQosAclAceRefEntry = _RlQosAclAceRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 8, 1)
)
rlQosAclAceRefEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosAclAceRefAcePointer"),
)
if mibBuilder.loadTexts:
    rlQosAclAceRefEntry.setStatus("current")
_RlQosAclAceRefAcePointer_Type = Integer32
_RlQosAclAceRefAcePointer_Object = MibTableColumn
rlQosAclAceRefAcePointer = _RlQosAclAceRefAcePointer_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 8, 1, 1),
    _RlQosAclAceRefAcePointer_Type()
)
rlQosAclAceRefAcePointer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosAclAceRefAcePointer.setStatus("current")
_RlQosAclAceRefAclPointer_Type = Integer32
_RlQosAclAceRefAclPointer_Object = MibTableColumn
rlQosAclAceRefAclPointer = _RlQosAclAceRefAclPointer_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 8, 1, 2),
    _RlQosAclAceRefAclPointer_Type()
)
rlQosAclAceRefAclPointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAclAceRefAclPointer.setStatus("current")
_RlQosAclAceRefStatus_Type = RowStatus
_RlQosAclAceRefStatus_Object = MibTableColumn
rlQosAclAceRefStatus = _RlQosAclAceRefStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 8, 1, 3),
    _RlQosAclAceRefStatus_Type()
)
rlQosAclAceRefStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAclAceRefStatus.setStatus("current")
_RlQosClassMapTable_Object = MibTable
rlQosClassMapTable = _RlQosClassMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 9)
)
if mibBuilder.loadTexts:
    rlQosClassMapTable.setStatus("current")
_RlQosClassMapEntry_Object = MibTableRow
rlQosClassMapEntry = _RlQosClassMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 9, 1)
)
rlQosClassMapEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosClassMapIndex"),
)
if mibBuilder.loadTexts:
    rlQosClassMapEntry.setStatus("current")
_RlQosClassMapIndex_Type = Integer32
_RlQosClassMapIndex_Object = MibTableColumn
rlQosClassMapIndex = _RlQosClassMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 9, 1, 1),
    _RlQosClassMapIndex_Type()
)
rlQosClassMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosClassMapIndex.setStatus("current")


class _RlQosClassMapName_Type(DisplayString):
    """Custom type rlQosClassMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlQosClassMapName_Type.__name__ = "DisplayString"
_RlQosClassMapName_Object = MibTableColumn
rlQosClassMapName = _RlQosClassMapName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 9, 1, 2),
    _RlQosClassMapName_Type()
)
rlQosClassMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosClassMapName.setStatus("current")


class _RlQosClassMapType_Type(ClassMapType):
    """Custom type rlQosClassMapType based on ClassMapType"""
    defaultValue = 1


_RlQosClassMapType_Object = MibTableColumn
rlQosClassMapType = _RlQosClassMapType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 9, 1, 3),
    _RlQosClassMapType_Type()
)
rlQosClassMapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosClassMapType.setStatus("current")


class _RlQosClassMapAction_Type(ClassMapAction):
    """Custom type rlQosClassMapAction based on ClassMapAction"""
    defaultValue = 1


_RlQosClassMapAction_Object = MibTableColumn
rlQosClassMapAction = _RlQosClassMapAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 9, 1, 4),
    _RlQosClassMapAction_Type()
)
rlQosClassMapAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosClassMapAction.setStatus("current")


class _RlQosClassMapMarkValue_Type(Integer32):
    """Custom type rlQosClassMapMarkValue based on Integer32"""
    defaultValue = 0


_RlQosClassMapMarkValue_Object = MibTableColumn
rlQosClassMapMarkValue = _RlQosClassMapMarkValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 9, 1, 5),
    _RlQosClassMapMarkValue_Type()
)
rlQosClassMapMarkValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosClassMapMarkValue.setStatus("current")


class _RlQosClassMapPolicer_Type(Integer32):
    """Custom type rlQosClassMapPolicer based on Integer32"""
    defaultValue = 0


_RlQosClassMapPolicer_Object = MibTableColumn
rlQosClassMapPolicer = _RlQosClassMapPolicer_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 9, 1, 6),
    _RlQosClassMapPolicer_Type()
)
rlQosClassMapPolicer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosClassMapPolicer.setStatus("current")
_RlQosClassMapMatch1_Type = Integer32
_RlQosClassMapMatch1_Object = MibTableColumn
rlQosClassMapMatch1 = _RlQosClassMapMatch1_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 9, 1, 7),
    _RlQosClassMapMatch1_Type()
)
rlQosClassMapMatch1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosClassMapMatch1.setStatus("current")


class _RlQosClassMapMatch2_Type(Integer32):
    """Custom type rlQosClassMapMatch2 based on Integer32"""
    defaultValue = 0


_RlQosClassMapMatch2_Object = MibTableColumn
rlQosClassMapMatch2 = _RlQosClassMapMatch2_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 9, 1, 8),
    _RlQosClassMapMatch2_Type()
)
rlQosClassMapMatch2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosClassMapMatch2.setStatus("current")


class _RlQosClassMapMarkVlan_Type(MarkVlanAction):
    """Custom type rlQosClassMapMarkVlan based on MarkVlanAction"""
    defaultValue = 1


_RlQosClassMapMarkVlan_Object = MibTableColumn
rlQosClassMapMarkVlan = _RlQosClassMapMarkVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 9, 1, 9),
    _RlQosClassMapMarkVlan_Type()
)
rlQosClassMapMarkVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosClassMapMarkVlan.setStatus("current")


class _RlQosClassMapNewVlan_Type(Integer32):
    """Custom type rlQosClassMapNewVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RlQosClassMapNewVlan_Type.__name__ = "Integer32"
_RlQosClassMapNewVlan_Object = MibTableColumn
rlQosClassMapNewVlan = _RlQosClassMapNewVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 9, 1, 10),
    _RlQosClassMapNewVlan_Type()
)
rlQosClassMapNewVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosClassMapNewVlan.setStatus("current")


class _RlQosClassMapRedirectAction_Type(RedirectAction):
    """Custom type rlQosClassMapRedirectAction based on RedirectAction"""


_RlQosClassMapRedirectAction_Object = MibTableColumn
rlQosClassMapRedirectAction = _RlQosClassMapRedirectAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 9, 1, 11),
    _RlQosClassMapRedirectAction_Type()
)
rlQosClassMapRedirectAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosClassMapRedirectAction.setStatus("current")


class _RlQosClassMapDestInterface_Type(Integer32):
    """Custom type rlQosClassMapDestInterface based on Integer32"""
    defaultValue = 0


_RlQosClassMapDestInterface_Object = MibTableColumn
rlQosClassMapDestInterface = _RlQosClassMapDestInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 9, 1, 12),
    _RlQosClassMapDestInterface_Type()
)
rlQosClassMapDestInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosClassMapDestInterface.setStatus("current")
_RlQosClassMapStatus_Type = RowStatus
_RlQosClassMapStatus_Object = MibTableColumn
rlQosClassMapStatus = _RlQosClassMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 9, 1, 13),
    _RlQosClassMapStatus_Type()
)
rlQosClassMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosClassMapStatus.setStatus("current")


class _RlQosClassMapMatch3_Type(Integer32):
    """Custom type rlQosClassMapMatch3 based on Integer32"""
    defaultValue = 0


_RlQosClassMapMatch3_Object = MibTableColumn
rlQosClassMapMatch3 = _RlQosClassMapMatch3_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 9, 1, 14),
    _RlQosClassMapMatch3_Type()
)
rlQosClassMapMatch3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosClassMapMatch3.setStatus("current")


class _RlQosClassMapTrapId_Type(Integer32):
    """Custom type rlQosClassMapTrapId based on Integer32"""
    defaultValue = 0


_RlQosClassMapTrapId_Object = MibTableColumn
rlQosClassMapTrapId = _RlQosClassMapTrapId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 9, 1, 15),
    _RlQosClassMapTrapId_Type()
)
rlQosClassMapTrapId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosClassMapTrapId.setStatus("current")


class _RlQosClassMapCounterEnable_Type(TruthValue):
    """Custom type rlQosClassMapCounterEnable based on TruthValue"""


_RlQosClassMapCounterEnable_Object = MibTableColumn
rlQosClassMapCounterEnable = _RlQosClassMapCounterEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 9, 1, 16),
    _RlQosClassMapCounterEnable_Type()
)
rlQosClassMapCounterEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosClassMapCounterEnable.setStatus("current")


class _RlQosClassMapTunnelIdx_Type(Unsigned32):
    """Custom type rlQosClassMapTunnelIdx based on Unsigned32"""
    defaultValue = 0


_RlQosClassMapTunnelIdx_Object = MibTableColumn
rlQosClassMapTunnelIdx = _RlQosClassMapTunnelIdx_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 9, 1, 17),
    _RlQosClassMapTunnelIdx_Type()
)
rlQosClassMapTunnelIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosClassMapTunnelIdx.setStatus("current")
_RlQosPolicerTable_Object = MibTable
rlQosPolicerTable = _RlQosPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 10)
)
if mibBuilder.loadTexts:
    rlQosPolicerTable.setStatus("current")
_RlQosPolicerEntry_Object = MibTableRow
rlQosPolicerEntry = _RlQosPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 10, 1)
)
rlQosPolicerEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosPolicerIndex"),
)
if mibBuilder.loadTexts:
    rlQosPolicerEntry.setStatus("current")
_RlQosPolicerIndex_Type = Integer32
_RlQosPolicerIndex_Object = MibTableColumn
rlQosPolicerIndex = _RlQosPolicerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 10, 1, 1),
    _RlQosPolicerIndex_Type()
)
rlQosPolicerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosPolicerIndex.setStatus("current")


class _RlQosPolicerName_Type(DisplayString):
    """Custom type rlQosPolicerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlQosPolicerName_Type.__name__ = "DisplayString"
_RlQosPolicerName_Object = MibTableColumn
rlQosPolicerName = _RlQosPolicerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 10, 1, 2),
    _RlQosPolicerName_Type()
)
rlQosPolicerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPolicerName.setStatus("current")
_RlQosPolicerType_Type = PolicerType
_RlQosPolicerType_Object = MibTableColumn
rlQosPolicerType = _RlQosPolicerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 10, 1, 3),
    _RlQosPolicerType_Type()
)
rlQosPolicerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPolicerType.setStatus("current")
_RlQosPolicerCir_Type = Unsigned32
_RlQosPolicerCir_Object = MibTableColumn
rlQosPolicerCir = _RlQosPolicerCir_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 10, 1, 4),
    _RlQosPolicerCir_Type()
)
rlQosPolicerCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPolicerCir.setStatus("current")
if mibBuilder.loadTexts:
    rlQosPolicerCir.setUnits("kbps")
_RlQosPolicerCbs_Type = Unsigned32
_RlQosPolicerCbs_Object = MibTableColumn
rlQosPolicerCbs = _RlQosPolicerCbs_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 10, 1, 5),
    _RlQosPolicerCbs_Type()
)
rlQosPolicerCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPolicerCbs.setStatus("current")
if mibBuilder.loadTexts:
    rlQosPolicerCbs.setUnits("bytes")
_RlQosPolicerAction_Type = PolicerAction
_RlQosPolicerAction_Object = MibTableColumn
rlQosPolicerAction = _RlQosPolicerAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 10, 1, 6),
    _RlQosPolicerAction_Type()
)
rlQosPolicerAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPolicerAction.setStatus("current")
_RlQosPolicerCasPointerRemVal_Type = Integer32
_RlQosPolicerCasPointerRemVal_Object = MibTableColumn
rlQosPolicerCasPointerRemVal = _RlQosPolicerCasPointerRemVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 10, 1, 7),
    _RlQosPolicerCasPointerRemVal_Type()
)
rlQosPolicerCasPointerRemVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPolicerCasPointerRemVal.setStatus("current")
_RlQosPolicerStatus_Type = RowStatus
_RlQosPolicerStatus_Object = MibTableColumn
rlQosPolicerStatus = _RlQosPolicerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 10, 1, 8),
    _RlQosPolicerStatus_Type()
)
rlQosPolicerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPolicerStatus.setStatus("current")
_RlQosPolicyMapTable_Object = MibTable
rlQosPolicyMapTable = _RlQosPolicyMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 11)
)
if mibBuilder.loadTexts:
    rlQosPolicyMapTable.setStatus("current")
_RlQosPolicyMapEntry_Object = MibTableRow
rlQosPolicyMapEntry = _RlQosPolicyMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 11, 1)
)
rlQosPolicyMapEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosPolicyMapIndex"),
)
if mibBuilder.loadTexts:
    rlQosPolicyMapEntry.setStatus("current")
_RlQosPolicyMapIndex_Type = Integer32
_RlQosPolicyMapIndex_Object = MibTableColumn
rlQosPolicyMapIndex = _RlQosPolicyMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 11, 1, 1),
    _RlQosPolicyMapIndex_Type()
)
rlQosPolicyMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosPolicyMapIndex.setStatus("current")


class _RlQosPolicyMapName_Type(DisplayString):
    """Custom type rlQosPolicyMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlQosPolicyMapName_Type.__name__ = "DisplayString"
_RlQosPolicyMapName_Object = MibTableColumn
rlQosPolicyMapName = _RlQosPolicyMapName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 11, 1, 2),
    _RlQosPolicyMapName_Type()
)
rlQosPolicyMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPolicyMapName.setStatus("current")
_RlQosPolicyMapStatus_Type = RowStatus
_RlQosPolicyMapStatus_Object = MibTableColumn
rlQosPolicyMapStatus = _RlQosPolicyMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 11, 1, 3),
    _RlQosPolicyMapStatus_Type()
)
rlQosPolicyMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPolicyMapStatus.setStatus("current")
_RlQosPolicyClassRefTable_Object = MibTable
rlQosPolicyClassRefTable = _RlQosPolicyClassRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 12)
)
if mibBuilder.loadTexts:
    rlQosPolicyClassRefTable.setStatus("current")
_RlQosPolicyClassRefEntry_Object = MibTableRow
rlQosPolicyClassRefEntry = _RlQosPolicyClassRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 12, 1)
)
rlQosPolicyClassRefEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosPolicyClassRefClassPointer"),
)
if mibBuilder.loadTexts:
    rlQosPolicyClassRefEntry.setStatus("current")
_RlQosPolicyClassRefClassPointer_Type = Integer32
_RlQosPolicyClassRefClassPointer_Object = MibTableColumn
rlQosPolicyClassRefClassPointer = _RlQosPolicyClassRefClassPointer_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 12, 1, 1),
    _RlQosPolicyClassRefClassPointer_Type()
)
rlQosPolicyClassRefClassPointer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosPolicyClassRefClassPointer.setStatus("current")
_RlQosPolicyClassRefPolicyPointer_Type = Integer32
_RlQosPolicyClassRefPolicyPointer_Object = MibTableColumn
rlQosPolicyClassRefPolicyPointer = _RlQosPolicyClassRefPolicyPointer_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 12, 1, 2),
    _RlQosPolicyClassRefPolicyPointer_Type()
)
rlQosPolicyClassRefPolicyPointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPolicyClassRefPolicyPointer.setStatus("current")
_RlQosPolicyClassRefStatus_Type = RowStatus
_RlQosPolicyClassRefStatus_Object = MibTableColumn
rlQosPolicyClassRefStatus = _RlQosPolicyClassRefStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 12, 1, 3),
    _RlQosPolicyClassRefStatus_Type()
)
rlQosPolicyClassRefStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPolicyClassRefStatus.setStatus("current")
_RlQosIfPolicyTable_Object = MibTable
rlQosIfPolicyTable = _RlQosIfPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 13)
)
if mibBuilder.loadTexts:
    rlQosIfPolicyTable.setStatus("current")
_RlQosIfPolicyEntry_Object = MibTableRow
rlQosIfPolicyEntry = _RlQosIfPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 13, 1)
)
rlQosIfPolicyEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlIfIndex"),
    (0, "CISCOSB-QOS-CLI-MIB", "rlIfType"),
)
if mibBuilder.loadTexts:
    rlQosIfPolicyEntry.setStatus("current")
_RlIfIndex_Type = Integer32
_RlIfIndex_Object = MibTableColumn
rlIfIndex = _RlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 13, 1, 1),
    _RlIfIndex_Type()
)
rlIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIfIndex.setStatus("current")
_RlIfType_Type = InterfaceType
_RlIfType_Object = MibTableColumn
rlIfType = _RlIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 13, 1, 2),
    _RlIfType_Type()
)
rlIfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIfType.setStatus("current")
_RlQosIfPolicyMapPointerIn_Type = Integer32
_RlQosIfPolicyMapPointerIn_Object = MibTableColumn
rlQosIfPolicyMapPointerIn = _RlQosIfPolicyMapPointerIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 13, 1, 3),
    _RlQosIfPolicyMapPointerIn_Type()
)
rlQosIfPolicyMapPointerIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosIfPolicyMapPointerIn.setStatus("current")
_RlQosIfPolicyMapPointerOut_Type = Integer32
_RlQosIfPolicyMapPointerOut_Object = MibTableColumn
rlQosIfPolicyMapPointerOut = _RlQosIfPolicyMapPointerOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 13, 1, 4),
    _RlQosIfPolicyMapPointerOut_Type()
)
rlQosIfPolicyMapPointerOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosIfPolicyMapPointerOut.setStatus("current")
_RlQosIfTrustActive_Type = BinaryStatus
_RlQosIfTrustActive_Object = MibTableColumn
rlQosIfTrustActive = _RlQosIfTrustActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 13, 1, 5),
    _RlQosIfTrustActive_Type()
)
rlQosIfTrustActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosIfTrustActive.setStatus("current")
_RlQosPortShaperStatus_Type = BinaryStatus
_RlQosPortShaperStatus_Object = MibTableColumn
rlQosPortShaperStatus = _RlQosPortShaperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 13, 1, 6),
    _RlQosPortShaperStatus_Type()
)
rlQosPortShaperStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPortShaperStatus.setStatus("current")
_RlQosCirPortShaper_Type = Integer32
_RlQosCirPortShaper_Object = MibTableColumn
rlQosCirPortShaper = _RlQosCirPortShaper_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 13, 1, 7),
    _RlQosCirPortShaper_Type()
)
rlQosCirPortShaper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCirPortShaper.setStatus("current")
if mibBuilder.loadTexts:
    rlQosCirPortShaper.setUnits("bps")
_RlQosCbsPortShaper_Type = Integer32
_RlQosCbsPortShaper_Object = MibTableColumn
rlQosCbsPortShaper = _RlQosCbsPortShaper_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 13, 1, 8),
    _RlQosCbsPortShaper_Type()
)
rlQosCbsPortShaper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCbsPortShaper.setStatus("current")
if mibBuilder.loadTexts:
    rlQosCbsPortShaper.setUnits("bytes")


class _RlQosIfProfilePointer_Type(DisplayString):
    """Custom type rlQosIfProfilePointer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlQosIfProfilePointer_Type.__name__ = "DisplayString"
_RlQosIfProfilePointer_Object = MibTableColumn
rlQosIfProfilePointer = _RlQosIfProfilePointer_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 13, 1, 9),
    _RlQosIfProfilePointer_Type()
)
rlQosIfProfilePointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosIfProfilePointer.setStatus("current")


class _RlQosQueueProfilePointer_Type(DisplayString):
    """Custom type rlQosQueueProfilePointer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlQosQueueProfilePointer_Type.__name__ = "DisplayString"
_RlQosQueueProfilePointer_Object = MibTableColumn
rlQosQueueProfilePointer = _RlQosQueueProfilePointer_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 13, 1, 10),
    _RlQosQueueProfilePointer_Type()
)
rlQosQueueProfilePointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosQueueProfilePointer.setStatus("current")
_RlQosQueueShapeProfilePointer_Type = Integer32
_RlQosQueueShapeProfilePointer_Object = MibTableColumn
rlQosQueueShapeProfilePointer = _RlQosQueueShapeProfilePointer_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 13, 1, 11),
    _RlQosQueueShapeProfilePointer_Type()
)
rlQosQueueShapeProfilePointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosQueueShapeProfilePointer.setStatus("current")
_RlQosAclDefaultAction_Type = AclDefaultAction
_RlQosAclDefaultAction_Object = MibTableColumn
rlQosAclDefaultAction = _RlQosAclDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 13, 1, 12),
    _RlQosAclDefaultAction_Type()
)
rlQosAclDefaultAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAclDefaultAction.setStatus("current")
_RlQosIfPolicyMapStatus_Type = RowStatus
_RlQosIfPolicyMapStatus_Object = MibTableColumn
rlQosIfPolicyMapStatus = _RlQosIfPolicyMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 13, 1, 13),
    _RlQosIfPolicyMapStatus_Type()
)
rlQosIfPolicyMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosIfPolicyMapStatus.setStatus("current")


class _RlQosIfAclIn_Type(Integer32):
    """Custom type rlQosIfAclIn based on Integer32"""
    defaultValue = 0


_RlQosIfAclIn_Object = MibTableColumn
rlQosIfAclIn = _RlQosIfAclIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 13, 1, 14),
    _RlQosIfAclIn_Type()
)
rlQosIfAclIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosIfAclIn.setStatus("current")


class _RlQosIfAclOut_Type(Integer32):
    """Custom type rlQosIfAclOut based on Integer32"""
    defaultValue = 0


_RlQosIfAclOut_Object = MibTableColumn
rlQosIfAclOut = _RlQosIfAclOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 13, 1, 15),
    _RlQosIfAclOut_Type()
)
rlQosIfAclOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosIfAclOut.setStatus("current")


class _RlQosIfPolicerIn_Type(Integer32):
    """Custom type rlQosIfPolicerIn based on Integer32"""
    defaultValue = 0


_RlQosIfPolicerIn_Object = MibTableColumn
rlQosIfPolicerIn = _RlQosIfPolicerIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 13, 1, 16),
    _RlQosIfPolicerIn_Type()
)
rlQosIfPolicerIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosIfPolicerIn.setStatus("current")


class _RlQosPortRateLimitStatus_Type(BinaryStatus):
    """Custom type rlQosPortRateLimitStatus based on BinaryStatus"""


_RlQosPortRateLimitStatus_Object = MibTableColumn
rlQosPortRateLimitStatus = _RlQosPortRateLimitStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 13, 1, 17),
    _RlQosPortRateLimitStatus_Type()
)
rlQosPortRateLimitStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPortRateLimitStatus.setStatus("current")


class _RlQosCirPortRateLimit_Type(Integer32):
    """Custom type rlQosCirPortRateLimit based on Integer32"""
    defaultValue = 0


_RlQosCirPortRateLimit_Object = MibTableColumn
rlQosCirPortRateLimit = _RlQosCirPortRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 13, 1, 18),
    _RlQosCirPortRateLimit_Type()
)
rlQosCirPortRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCirPortRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    rlQosCirPortRateLimit.setUnits("bps")


class _RlQosCbsPortRateLimit_Type(Integer32):
    """Custom type rlQosCbsPortRateLimit based on Integer32"""
    defaultValue = 0


_RlQosCbsPortRateLimit_Object = MibTableColumn
rlQosCbsPortRateLimit = _RlQosCbsPortRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 13, 1, 19),
    _RlQosCbsPortRateLimit_Type()
)
rlQosCbsPortRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCbsPortRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    rlQosCbsPortRateLimit.setUnits("bytes")


class _RlQosIfIpv6AclIn_Type(Integer32):
    """Custom type rlQosIfIpv6AclIn based on Integer32"""
    defaultValue = 0


_RlQosIfIpv6AclIn_Object = MibTableColumn
rlQosIfIpv6AclIn = _RlQosIfIpv6AclIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 13, 1, 20),
    _RlQosIfIpv6AclIn_Type()
)
rlQosIfIpv6AclIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosIfIpv6AclIn.setStatus("current")


class _RlQosIfIpv6AclOut_Type(Integer32):
    """Custom type rlQosIfIpv6AclOut based on Integer32"""
    defaultValue = 0


_RlQosIfIpv6AclOut_Object = MibTableColumn
rlQosIfIpv6AclOut = _RlQosIfIpv6AclOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 13, 1, 21),
    _RlQosIfIpv6AclOut_Type()
)
rlQosIfIpv6AclOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosIfIpv6AclOut.setStatus("current")
_RlQosIfProfileCfgTable_Object = MibTable
rlQosIfProfileCfgTable = _RlQosIfProfileCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 14)
)
if mibBuilder.loadTexts:
    rlQosIfProfileCfgTable.setStatus("current")
_RlQosIfProfileCfgEntry_Object = MibTableRow
rlQosIfProfileCfgEntry = _RlQosIfProfileCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 14, 1)
)
rlQosIfProfileCfgEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlIfProfileName"),
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosQueueId"),
)
if mibBuilder.loadTexts:
    rlQosIfProfileCfgEntry.setStatus("current")


class _RlIfProfileName_Type(DisplayString):
    """Custom type rlIfProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlIfProfileName_Type.__name__ = "DisplayString"
_RlIfProfileName_Object = MibTableColumn
rlIfProfileName = _RlIfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 14, 1, 1),
    _RlIfProfileName_Type()
)
rlIfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIfProfileName.setStatus("current")


class _RlQosQueueId_Type(Integer32):
    """Custom type rlQosQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RlQosQueueId_Type.__name__ = "Integer32"
_RlQosQueueId_Object = MibTableColumn
rlQosQueueId = _RlQosQueueId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 14, 1, 2),
    _RlQosQueueId_Type()
)
rlQosQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosQueueId.setStatus("current")


class _RlQosTdThersholdDp0_Type(Integer32):
    """Custom type rlQosTdThersholdDp0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlQosTdThersholdDp0_Type.__name__ = "Integer32"
_RlQosTdThersholdDp0_Object = MibTableColumn
rlQosTdThersholdDp0 = _RlQosTdThersholdDp0_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 14, 1, 3),
    _RlQosTdThersholdDp0_Type()
)
rlQosTdThersholdDp0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosTdThersholdDp0.setStatus("current")
if mibBuilder.loadTexts:
    rlQosTdThersholdDp0.setUnits("percent")


class _RlQosTdThersholdDp1_Type(Integer32):
    """Custom type rlQosTdThersholdDp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlQosTdThersholdDp1_Type.__name__ = "Integer32"
_RlQosTdThersholdDp1_Object = MibTableColumn
rlQosTdThersholdDp1 = _RlQosTdThersholdDp1_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 14, 1, 4),
    _RlQosTdThersholdDp1_Type()
)
rlQosTdThersholdDp1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosTdThersholdDp1.setStatus("current")
if mibBuilder.loadTexts:
    rlQosTdThersholdDp1.setUnits("percent")


class _RlQosTdThersholdDp2_Type(Integer32):
    """Custom type rlQosTdThersholdDp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlQosTdThersholdDp2_Type.__name__ = "Integer32"
_RlQosTdThersholdDp2_Object = MibTableColumn
rlQosTdThersholdDp2 = _RlQosTdThersholdDp2_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 14, 1, 5),
    _RlQosTdThersholdDp2_Type()
)
rlQosTdThersholdDp2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosTdThersholdDp2.setStatus("current")
if mibBuilder.loadTexts:
    rlQosTdThersholdDp2.setUnits("percent")


class _RlQosRedMinDp0_Type(Integer32):
    """Custom type rlQosRedMinDp0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlQosRedMinDp0_Type.__name__ = "Integer32"
_RlQosRedMinDp0_Object = MibTableColumn
rlQosRedMinDp0 = _RlQosRedMinDp0_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 14, 1, 6),
    _RlQosRedMinDp0_Type()
)
rlQosRedMinDp0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosRedMinDp0.setStatus("current")
if mibBuilder.loadTexts:
    rlQosRedMinDp0.setUnits("percent")


class _RlQosRedMaxDp0_Type(Integer32):
    """Custom type rlQosRedMaxDp0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlQosRedMaxDp0_Type.__name__ = "Integer32"
_RlQosRedMaxDp0_Object = MibTableColumn
rlQosRedMaxDp0 = _RlQosRedMaxDp0_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 14, 1, 7),
    _RlQosRedMaxDp0_Type()
)
rlQosRedMaxDp0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosRedMaxDp0.setStatus("current")
if mibBuilder.loadTexts:
    rlQosRedMaxDp0.setUnits("percent")
_RlQosRedProbDp0_Type = Integer32
_RlQosRedProbDp0_Object = MibTableColumn
rlQosRedProbDp0 = _RlQosRedProbDp0_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 14, 1, 8),
    _RlQosRedProbDp0_Type()
)
rlQosRedProbDp0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosRedProbDp0.setStatus("current")


class _RlQosRedMinDp1_Type(Integer32):
    """Custom type rlQosRedMinDp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlQosRedMinDp1_Type.__name__ = "Integer32"
_RlQosRedMinDp1_Object = MibTableColumn
rlQosRedMinDp1 = _RlQosRedMinDp1_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 14, 1, 9),
    _RlQosRedMinDp1_Type()
)
rlQosRedMinDp1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosRedMinDp1.setStatus("current")
if mibBuilder.loadTexts:
    rlQosRedMinDp1.setUnits("percent")


class _RlQosRedMaxDp1_Type(Integer32):
    """Custom type rlQosRedMaxDp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlQosRedMaxDp1_Type.__name__ = "Integer32"
_RlQosRedMaxDp1_Object = MibTableColumn
rlQosRedMaxDp1 = _RlQosRedMaxDp1_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 14, 1, 10),
    _RlQosRedMaxDp1_Type()
)
rlQosRedMaxDp1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosRedMaxDp1.setStatus("current")
if mibBuilder.loadTexts:
    rlQosRedMaxDp1.setUnits("percent")
_RlQosRedProbDp1_Type = Integer32
_RlQosRedProbDp1_Object = MibTableColumn
rlQosRedProbDp1 = _RlQosRedProbDp1_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 14, 1, 11),
    _RlQosRedProbDp1_Type()
)
rlQosRedProbDp1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosRedProbDp1.setStatus("current")


class _RlQosRedMinDp2_Type(Integer32):
    """Custom type rlQosRedMinDp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlQosRedMinDp2_Type.__name__ = "Integer32"
_RlQosRedMinDp2_Object = MibTableColumn
rlQosRedMinDp2 = _RlQosRedMinDp2_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 14, 1, 12),
    _RlQosRedMinDp2_Type()
)
rlQosRedMinDp2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosRedMinDp2.setStatus("current")
if mibBuilder.loadTexts:
    rlQosRedMinDp2.setUnits("percent")


class _RlQosRedMaxDp2_Type(Integer32):
    """Custom type rlQosRedMaxDp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlQosRedMaxDp2_Type.__name__ = "Integer32"
_RlQosRedMaxDp2_Object = MibTableColumn
rlQosRedMaxDp2 = _RlQosRedMaxDp2_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 14, 1, 13),
    _RlQosRedMaxDp2_Type()
)
rlQosRedMaxDp2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosRedMaxDp2.setStatus("current")
if mibBuilder.loadTexts:
    rlQosRedMaxDp2.setUnits("percent")
_RlQosRedProbDp2_Type = Integer32
_RlQosRedProbDp2_Object = MibTableColumn
rlQosRedProbDp2 = _RlQosRedProbDp2_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 14, 1, 14),
    _RlQosRedProbDp2_Type()
)
rlQosRedProbDp2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosRedProbDp2.setStatus("current")
_RlQosRedQweight_Type = Integer32
_RlQosRedQweight_Object = MibTableColumn
rlQosRedQweight = _RlQosRedQweight_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 14, 1, 15),
    _RlQosRedQweight_Type()
)
rlQosRedQweight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosRedQweight.setStatus("current")
_RlQosIfprofileStatus_Type = RowStatus
_RlQosIfprofileStatus_Object = MibTableColumn
rlQosIfprofileStatus = _RlQosIfprofileStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 14, 1, 16),
    _RlQosIfprofileStatus_Type()
)
rlQosIfprofileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosIfprofileStatus.setStatus("current")
_RlQosDscpMutationTable_Object = MibTable
rlQosDscpMutationTable = _RlQosDscpMutationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 15)
)
if mibBuilder.loadTexts:
    rlQosDscpMutationTable.setStatus("current")
_RlQosDscpMutationEntry_Object = MibTableRow
rlQosDscpMutationEntry = _RlQosDscpMutationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 15, 1)
)
rlQosDscpMutationEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosOldDscp"),
)
if mibBuilder.loadTexts:
    rlQosDscpMutationEntry.setStatus("current")


class _RlQosOldDscp_Type(Integer32):
    """Custom type rlQosOldDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RlQosOldDscp_Type.__name__ = "Integer32"
_RlQosOldDscp_Object = MibTableColumn
rlQosOldDscp = _RlQosOldDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 15, 1, 1),
    _RlQosOldDscp_Type()
)
rlQosOldDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosOldDscp.setStatus("current")


class _RlQosNewDscp_Type(Integer32):
    """Custom type rlQosNewDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RlQosNewDscp_Type.__name__ = "Integer32"
_RlQosNewDscp_Object = MibTableColumn
rlQosNewDscp = _RlQosNewDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 15, 1, 2),
    _RlQosNewDscp_Type()
)
rlQosNewDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosNewDscp.setStatus("current")
_RlQosDscpRemarkTable_Object = MibTable
rlQosDscpRemarkTable = _RlQosDscpRemarkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 16)
)
if mibBuilder.loadTexts:
    rlQosDscpRemarkTable.setStatus("current")
_RlQosDscpRemarkEntry_Object = MibTableRow
rlQosDscpRemarkEntry = _RlQosDscpRemarkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 16, 1)
)
rlQosDscpRemarkEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosRmOldDscp"),
)
if mibBuilder.loadTexts:
    rlQosDscpRemarkEntry.setStatus("current")


class _RlQosRmOldDscp_Type(Integer32):
    """Custom type rlQosRmOldDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RlQosRmOldDscp_Type.__name__ = "Integer32"
_RlQosRmOldDscp_Object = MibTableColumn
rlQosRmOldDscp = _RlQosRmOldDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 16, 1, 1),
    _RlQosRmOldDscp_Type()
)
rlQosRmOldDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosRmOldDscp.setStatus("current")


class _RlQosRmNewDscp_Type(Integer32):
    """Custom type rlQosRmNewDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RlQosRmNewDscp_Type.__name__ = "Integer32"
_RlQosRmNewDscp_Object = MibTableColumn
rlQosRmNewDscp = _RlQosRmNewDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 16, 1, 2),
    _RlQosRmNewDscp_Type()
)
rlQosRmNewDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosRmNewDscp.setStatus("current")
_RlQosCosQueueTable_Object = MibTable
rlQosCosQueueTable = _RlQosCosQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 17)
)
if mibBuilder.loadTexts:
    rlQosCosQueueTable.setStatus("current")
_RlQosCosQueueEntry_Object = MibTableRow
rlQosCosQueueEntry = _RlQosCosQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 17, 1)
)
rlQosCosQueueEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosCosIndex"),
)
if mibBuilder.loadTexts:
    rlQosCosQueueEntry.setStatus("current")


class _RlQosCosIndex_Type(Integer32):
    """Custom type rlQosCosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RlQosCosIndex_Type.__name__ = "Integer32"
_RlQosCosIndex_Object = MibTableColumn
rlQosCosIndex = _RlQosCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 17, 1, 1),
    _RlQosCosIndex_Type()
)
rlQosCosIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosCosIndex.setStatus("current")


class _RlQosCosQueueId_Type(Integer32):
    """Custom type rlQosCosQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RlQosCosQueueId_Type.__name__ = "Integer32"
_RlQosCosQueueId_Object = MibTableColumn
rlQosCosQueueId = _RlQosCosQueueId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 17, 1, 2),
    _RlQosCosQueueId_Type()
)
rlQosCosQueueId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCosQueueId.setStatus("current")
_RlQosDscpQueueTable_Object = MibTable
rlQosDscpQueueTable = _RlQosDscpQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 18)
)
if mibBuilder.loadTexts:
    rlQosDscpQueueTable.setStatus("current")
_RlQosDscpQueueEntry_Object = MibTableRow
rlQosDscpQueueEntry = _RlQosDscpQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 18, 1)
)
rlQosDscpQueueEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosDscpIndex"),
)
if mibBuilder.loadTexts:
    rlQosDscpQueueEntry.setStatus("current")


class _RlQosDscpIndex_Type(Integer32):
    """Custom type rlQosDscpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RlQosDscpIndex_Type.__name__ = "Integer32"
_RlQosDscpIndex_Object = MibTableColumn
rlQosDscpIndex = _RlQosDscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 18, 1, 1),
    _RlQosDscpIndex_Type()
)
rlQosDscpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosDscpIndex.setStatus("current")


class _RlQosQueueNum_Type(Integer32):
    """Custom type rlQosQueueNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RlQosQueueNum_Type.__name__ = "Integer32"
_RlQosQueueNum_Object = MibTableColumn
rlQosQueueNum = _RlQosQueueNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 18, 1, 2),
    _RlQosQueueNum_Type()
)
rlQosQueueNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosQueueNum.setStatus("current")
_RlQosTcpPortQueueTable_Object = MibTable
rlQosTcpPortQueueTable = _RlQosTcpPortQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 19)
)
if mibBuilder.loadTexts:
    rlQosTcpPortQueueTable.setStatus("current")
_RlQosTcpPortQueueEntry_Object = MibTableRow
rlQosTcpPortQueueEntry = _RlQosTcpPortQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 19, 1)
)
rlQosTcpPortQueueEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosTcpPort"),
)
if mibBuilder.loadTexts:
    rlQosTcpPortQueueEntry.setStatus("current")
_RlQosTcpPort_Type = Integer32
_RlQosTcpPort_Object = MibTableColumn
rlQosTcpPort = _RlQosTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 19, 1, 1),
    _RlQosTcpPort_Type()
)
rlQosTcpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosTcpPort.setStatus("current")


class _RlQosTcpQueueValue_Type(Integer32):
    """Custom type rlQosTcpQueueValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RlQosTcpQueueValue_Type.__name__ = "Integer32"
_RlQosTcpQueueValue_Object = MibTableColumn
rlQosTcpQueueValue = _RlQosTcpQueueValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 19, 1, 2),
    _RlQosTcpQueueValue_Type()
)
rlQosTcpQueueValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosTcpQueueValue.setStatus("current")
_RlQosTcpPortQueueStatus_Type = RowStatus
_RlQosTcpPortQueueStatus_Object = MibTableColumn
rlQosTcpPortQueueStatus = _RlQosTcpPortQueueStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 19, 1, 3),
    _RlQosTcpPortQueueStatus_Type()
)
rlQosTcpPortQueueStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosTcpPortQueueStatus.setStatus("current")
_RlQosUdpPortQueueTable_Object = MibTable
rlQosUdpPortQueueTable = _RlQosUdpPortQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 20)
)
if mibBuilder.loadTexts:
    rlQosUdpPortQueueTable.setStatus("current")
_RlQosUdpPortQueueEntry_Object = MibTableRow
rlQosUdpPortQueueEntry = _RlQosUdpPortQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 20, 1)
)
rlQosUdpPortQueueEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosUdpPort"),
)
if mibBuilder.loadTexts:
    rlQosUdpPortQueueEntry.setStatus("current")
_RlQosUdpPort_Type = Integer32
_RlQosUdpPort_Object = MibTableColumn
rlQosUdpPort = _RlQosUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 20, 1, 1),
    _RlQosUdpPort_Type()
)
rlQosUdpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosUdpPort.setStatus("current")


class _RlQosUdpQueueValue_Type(Integer32):
    """Custom type rlQosUdpQueueValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RlQosUdpQueueValue_Type.__name__ = "Integer32"
_RlQosUdpQueueValue_Object = MibTableColumn
rlQosUdpQueueValue = _RlQosUdpQueueValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 20, 1, 2),
    _RlQosUdpQueueValue_Type()
)
rlQosUdpQueueValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosUdpQueueValue.setStatus("current")
_RlQosUdpPortQueueStatus_Type = RowStatus
_RlQosUdpPortQueueStatus_Object = MibTableColumn
rlQosUdpPortQueueStatus = _RlQosUdpPortQueueStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 20, 1, 3),
    _RlQosUdpPortQueueStatus_Type()
)
rlQosUdpPortQueueStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosUdpPortQueueStatus.setStatus("current")
_RlQosEfManageTable_Object = MibTable
rlQosEfManageTable = _RlQosEfManageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 21)
)
if mibBuilder.loadTexts:
    rlQosEfManageTable.setStatus("current")
_RlQosEfManageEntry_Object = MibTableRow
rlQosEfManageEntry = _RlQosEfManageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 21, 1)
)
rlQosEfManageEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosEfQueueId"),
)
if mibBuilder.loadTexts:
    rlQosEfManageEntry.setStatus("current")


class _RlQosEfQueueId_Type(Integer32):
    """Custom type rlQosEfQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RlQosEfQueueId_Type.__name__ = "Integer32"
_RlQosEfQueueId_Object = MibTableColumn
rlQosEfQueueId = _RlQosEfQueueId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 21, 1, 1),
    _RlQosEfQueueId_Type()
)
rlQosEfQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosEfQueueId.setStatus("current")
_RlQosEfState_Type = BinaryStatus
_RlQosEfState_Object = MibTableColumn
rlQosEfState = _RlQosEfState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 21, 1, 2),
    _RlQosEfState_Type()
)
rlQosEfState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosEfState.setStatus("current")


class _RlQosEfPriority_Type(Integer32):
    """Custom type rlQosEfPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RlQosEfPriority_Type.__name__ = "Integer32"
_RlQosEfPriority_Object = MibTableColumn
rlQosEfPriority = _RlQosEfPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 21, 1, 3),
    _RlQosEfPriority_Type()
)
rlQosEfPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosEfPriority.setStatus("current")
_RlQosQueueProfileTable_Object = MibTable
rlQosQueueProfileTable = _RlQosQueueProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 22)
)
if mibBuilder.loadTexts:
    rlQosQueueProfileTable.setStatus("current")
_RlQosQueueProfileEntry_Object = MibTableRow
rlQosQueueProfileEntry = _RlQosQueueProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 22, 1)
)
rlQosQueueProfileEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQueueProfileName"),
)
if mibBuilder.loadTexts:
    rlQosQueueProfileEntry.setStatus("current")


class _RlQueueProfileName_Type(DisplayString):
    """Custom type rlQueueProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlQueueProfileName_Type.__name__ = "DisplayString"
_RlQueueProfileName_Object = MibTableColumn
rlQueueProfileName = _RlQueueProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 22, 1, 1),
    _RlQueueProfileName_Type()
)
rlQueueProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQueueProfileName.setStatus("current")
_RlQosTypeQueue1_Type = QueueType
_RlQosTypeQueue1_Object = MibTableColumn
rlQosTypeQueue1 = _RlQosTypeQueue1_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 22, 1, 2),
    _RlQosTypeQueue1_Type()
)
rlQosTypeQueue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosTypeQueue1.setStatus("current")
_RlQosValueQueue1_Type = Integer32
_RlQosValueQueue1_Object = MibTableColumn
rlQosValueQueue1 = _RlQosValueQueue1_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 22, 1, 3),
    _RlQosValueQueue1_Type()
)
rlQosValueQueue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosValueQueue1.setStatus("current")
_RlQosTypeQueue2_Type = QueueType
_RlQosTypeQueue2_Object = MibTableColumn
rlQosTypeQueue2 = _RlQosTypeQueue2_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 22, 1, 4),
    _RlQosTypeQueue2_Type()
)
rlQosTypeQueue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosTypeQueue2.setStatus("current")
_RlQosValueQueue2_Type = Integer32
_RlQosValueQueue2_Object = MibTableColumn
rlQosValueQueue2 = _RlQosValueQueue2_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 22, 1, 5),
    _RlQosValueQueue2_Type()
)
rlQosValueQueue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosValueQueue2.setStatus("current")
_RlQosTypeQueue3_Type = QueueType
_RlQosTypeQueue3_Object = MibTableColumn
rlQosTypeQueue3 = _RlQosTypeQueue3_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 22, 1, 6),
    _RlQosTypeQueue3_Type()
)
rlQosTypeQueue3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosTypeQueue3.setStatus("current")
_RlQosValueQueue3_Type = Integer32
_RlQosValueQueue3_Object = MibTableColumn
rlQosValueQueue3 = _RlQosValueQueue3_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 22, 1, 7),
    _RlQosValueQueue3_Type()
)
rlQosValueQueue3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosValueQueue3.setStatus("current")
_RlQosTypeQueue4_Type = QueueType
_RlQosTypeQueue4_Object = MibTableColumn
rlQosTypeQueue4 = _RlQosTypeQueue4_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 22, 1, 8),
    _RlQosTypeQueue4_Type()
)
rlQosTypeQueue4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosTypeQueue4.setStatus("current")
_RlQosValueQueue4_Type = Integer32
_RlQosValueQueue4_Object = MibTableColumn
rlQosValueQueue4 = _RlQosValueQueue4_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 22, 1, 9),
    _RlQosValueQueue4_Type()
)
rlQosValueQueue4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosValueQueue4.setStatus("current")
_RlQosTypeQueue5_Type = QueueType
_RlQosTypeQueue5_Object = MibTableColumn
rlQosTypeQueue5 = _RlQosTypeQueue5_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 22, 1, 10),
    _RlQosTypeQueue5_Type()
)
rlQosTypeQueue5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosTypeQueue5.setStatus("current")
_RlQosValueQueue5_Type = Integer32
_RlQosValueQueue5_Object = MibTableColumn
rlQosValueQueue5 = _RlQosValueQueue5_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 22, 1, 11),
    _RlQosValueQueue5_Type()
)
rlQosValueQueue5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosValueQueue5.setStatus("current")
_RlQosTypeQueue6_Type = QueueType
_RlQosTypeQueue6_Object = MibTableColumn
rlQosTypeQueue6 = _RlQosTypeQueue6_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 22, 1, 12),
    _RlQosTypeQueue6_Type()
)
rlQosTypeQueue6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosTypeQueue6.setStatus("current")
_RlQosValueQueue6_Type = Integer32
_RlQosValueQueue6_Object = MibTableColumn
rlQosValueQueue6 = _RlQosValueQueue6_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 22, 1, 13),
    _RlQosValueQueue6_Type()
)
rlQosValueQueue6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosValueQueue6.setStatus("current")
_RlQosTypeQueue7_Type = QueueType
_RlQosTypeQueue7_Object = MibTableColumn
rlQosTypeQueue7 = _RlQosTypeQueue7_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 22, 1, 14),
    _RlQosTypeQueue7_Type()
)
rlQosTypeQueue7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosTypeQueue7.setStatus("current")
_RlQosValueQueue7_Type = Integer32
_RlQosValueQueue7_Object = MibTableColumn
rlQosValueQueue7 = _RlQosValueQueue7_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 22, 1, 15),
    _RlQosValueQueue7_Type()
)
rlQosValueQueue7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosValueQueue7.setStatus("current")
_RlQosTypeQueue8_Type = QueueType
_RlQosTypeQueue8_Object = MibTableColumn
rlQosTypeQueue8 = _RlQosTypeQueue8_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 22, 1, 16),
    _RlQosTypeQueue8_Type()
)
rlQosTypeQueue8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosTypeQueue8.setStatus("current")
_RlQosValueQueue8_Type = Integer32
_RlQosValueQueue8_Object = MibTableColumn
rlQosValueQueue8 = _RlQosValueQueue8_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 22, 1, 17),
    _RlQosValueQueue8_Type()
)
rlQosValueQueue8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosValueQueue8.setStatus("current")
_RlQosQueueProfileStatus_Type = RowStatus
_RlQosQueueProfileStatus_Object = MibTableColumn
rlQosQueueProfileStatus = _RlQosQueueProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 22, 1, 18),
    _RlQosQueueProfileStatus_Type()
)
rlQosQueueProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosQueueProfileStatus.setStatus("current")
_RlQosNumOfIfConnections_Type = Integer32
_RlQosNumOfIfConnections_Object = MibTableColumn
rlQosNumOfIfConnections = _RlQosNumOfIfConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 22, 1, 19),
    _RlQosNumOfIfConnections_Type()
)
rlQosNumOfIfConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosNumOfIfConnections.setStatus("current")
_RlQosQueueShapeProfileTable_Object = MibTable
rlQosQueueShapeProfileTable = _RlQosQueueShapeProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 23)
)
if mibBuilder.loadTexts:
    rlQosQueueShapeProfileTable.setStatus("current")
_RlQosQueueShapeProfileEntry_Object = MibTableRow
rlQosQueueShapeProfileEntry = _RlQosQueueShapeProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 23, 1)
)
rlQosQueueShapeProfileEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosQueueShapeIndex"),
)
if mibBuilder.loadTexts:
    rlQosQueueShapeProfileEntry.setStatus("current")
_RlQosQueueShapeIndex_Type = Integer32
_RlQosQueueShapeIndex_Object = MibTableColumn
rlQosQueueShapeIndex = _RlQosQueueShapeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 23, 1, 1),
    _RlQosQueueShapeIndex_Type()
)
rlQosQueueShapeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosQueueShapeIndex.setStatus("current")
_RlQosCirQueue1_Type = Integer32
_RlQosCirQueue1_Object = MibTableColumn
rlQosCirQueue1 = _RlQosCirQueue1_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 23, 1, 2),
    _RlQosCirQueue1_Type()
)
rlQosCirQueue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCirQueue1.setStatus("current")
_RlQosCbsQueue1_Type = Integer32
_RlQosCbsQueue1_Object = MibTableColumn
rlQosCbsQueue1 = _RlQosCbsQueue1_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 23, 1, 3),
    _RlQosCbsQueue1_Type()
)
rlQosCbsQueue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCbsQueue1.setStatus("current")
_RlQosCirQueue2_Type = Integer32
_RlQosCirQueue2_Object = MibTableColumn
rlQosCirQueue2 = _RlQosCirQueue2_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 23, 1, 4),
    _RlQosCirQueue2_Type()
)
rlQosCirQueue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCirQueue2.setStatus("current")
_RlQosCbsQueue2_Type = Integer32
_RlQosCbsQueue2_Object = MibTableColumn
rlQosCbsQueue2 = _RlQosCbsQueue2_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 23, 1, 5),
    _RlQosCbsQueue2_Type()
)
rlQosCbsQueue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCbsQueue2.setStatus("current")
_RlQosCirQueue3_Type = Integer32
_RlQosCirQueue3_Object = MibTableColumn
rlQosCirQueue3 = _RlQosCirQueue3_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 23, 1, 6),
    _RlQosCirQueue3_Type()
)
rlQosCirQueue3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCirQueue3.setStatus("current")
_RlQosCbsQueue3_Type = Integer32
_RlQosCbsQueue3_Object = MibTableColumn
rlQosCbsQueue3 = _RlQosCbsQueue3_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 23, 1, 7),
    _RlQosCbsQueue3_Type()
)
rlQosCbsQueue3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCbsQueue3.setStatus("current")
_RlQosCirQueue4_Type = Integer32
_RlQosCirQueue4_Object = MibTableColumn
rlQosCirQueue4 = _RlQosCirQueue4_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 23, 1, 8),
    _RlQosCirQueue4_Type()
)
rlQosCirQueue4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCirQueue4.setStatus("current")
_RlQosCbsQueue4_Type = Integer32
_RlQosCbsQueue4_Object = MibTableColumn
rlQosCbsQueue4 = _RlQosCbsQueue4_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 23, 1, 9),
    _RlQosCbsQueue4_Type()
)
rlQosCbsQueue4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCbsQueue4.setStatus("current")
_RlQosCirQueue5_Type = Integer32
_RlQosCirQueue5_Object = MibTableColumn
rlQosCirQueue5 = _RlQosCirQueue5_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 23, 1, 10),
    _RlQosCirQueue5_Type()
)
rlQosCirQueue5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCirQueue5.setStatus("current")
_RlQosCbsQueue5_Type = Integer32
_RlQosCbsQueue5_Object = MibTableColumn
rlQosCbsQueue5 = _RlQosCbsQueue5_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 23, 1, 11),
    _RlQosCbsQueue5_Type()
)
rlQosCbsQueue5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCbsQueue5.setStatus("current")
_RlQosCirQueue6_Type = Integer32
_RlQosCirQueue6_Object = MibTableColumn
rlQosCirQueue6 = _RlQosCirQueue6_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 23, 1, 12),
    _RlQosCirQueue6_Type()
)
rlQosCirQueue6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCirQueue6.setStatus("current")
_RlQosCbsQueue6_Type = Integer32
_RlQosCbsQueue6_Object = MibTableColumn
rlQosCbsQueue6 = _RlQosCbsQueue6_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 23, 1, 13),
    _RlQosCbsQueue6_Type()
)
rlQosCbsQueue6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCbsQueue6.setStatus("current")
_RlQosCirQueue7_Type = Integer32
_RlQosCirQueue7_Object = MibTableColumn
rlQosCirQueue7 = _RlQosCirQueue7_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 23, 1, 14),
    _RlQosCirQueue7_Type()
)
rlQosCirQueue7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCirQueue7.setStatus("current")
_RlQosCbsQueue7_Type = Integer32
_RlQosCbsQueue7_Object = MibTableColumn
rlQosCbsQueue7 = _RlQosCbsQueue7_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 23, 1, 15),
    _RlQosCbsQueue7_Type()
)
rlQosCbsQueue7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCbsQueue7.setStatus("current")
_RlQosCirQueue8_Type = Integer32
_RlQosCirQueue8_Object = MibTableColumn
rlQosCirQueue8 = _RlQosCirQueue8_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 23, 1, 16),
    _RlQosCirQueue8_Type()
)
rlQosCirQueue8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCirQueue8.setStatus("current")
_RlQosCbsQueue8_Type = Integer32
_RlQosCbsQueue8_Object = MibTableColumn
rlQosCbsQueue8 = _RlQosCbsQueue8_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 23, 1, 17),
    _RlQosCbsQueue8_Type()
)
rlQosCbsQueue8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosCbsQueue8.setStatus("current")
_RlQosQueueShapeProfileStatus_Type = RowStatus
_RlQosQueueShapeProfileStatus_Object = MibTableColumn
rlQosQueueShapeProfileStatus = _RlQosQueueShapeProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 23, 1, 18),
    _RlQosQueueShapeProfileStatus_Type()
)
rlQosQueueShapeProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosQueueShapeProfileStatus.setStatus("current")
_RlQosAclCounterTable_Object = MibTable
rlQosAclCounterTable = _RlQosAclCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 24)
)
if mibBuilder.loadTexts:
    rlQosAclCounterTable.setStatus("current")
_RlQosAclCounterEntry_Object = MibTableRow
rlQosAclCounterEntry = _RlQosAclCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 24, 1)
)
rlQosAclCounterEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosAclCounterInterface"),
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosAclCounterAclIndex"),
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosAclCounterAceIndex"),
)
if mibBuilder.loadTexts:
    rlQosAclCounterEntry.setStatus("current")
_RlQosAclCounterInterface_Type = InterfaceIndex
_RlQosAclCounterInterface_Object = MibTableColumn
rlQosAclCounterInterface = _RlQosAclCounterInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 24, 1, 1),
    _RlQosAclCounterInterface_Type()
)
rlQosAclCounterInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosAclCounterInterface.setStatus("current")
_RlQosAclCounterAclIndex_Type = Integer32
_RlQosAclCounterAclIndex_Object = MibTableColumn
rlQosAclCounterAclIndex = _RlQosAclCounterAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 24, 1, 2),
    _RlQosAclCounterAclIndex_Type()
)
rlQosAclCounterAclIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosAclCounterAclIndex.setStatus("current")
_RlQosAclCounterAceIndex_Type = Integer32
_RlQosAclCounterAceIndex_Object = MibTableColumn
rlQosAclCounterAceIndex = _RlQosAclCounterAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 24, 1, 3),
    _RlQosAclCounterAceIndex_Type()
)
rlQosAclCounterAceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosAclCounterAceIndex.setStatus("current")
_RlQosAclCounterValue_Type = Counter32
_RlQosAclCounterValue_Object = MibTableColumn
rlQosAclCounterValue = _RlQosAclCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 24, 1, 4),
    _RlQosAclCounterValue_Type()
)
rlQosAclCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosAclCounterValue.setStatus("current")
_RlQosFreeIndexesTable_Object = MibTable
rlQosFreeIndexesTable = _RlQosFreeIndexesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 25)
)
if mibBuilder.loadTexts:
    rlQosFreeIndexesTable.setStatus("current")
_RlQosFreeIndexesEntry_Object = MibTableRow
rlQosFreeIndexesEntry = _RlQosFreeIndexesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 25, 1)
)
rlQosFreeIndexesEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosFreeIndexesTableId"),
)
if mibBuilder.loadTexts:
    rlQosFreeIndexesEntry.setStatus("current")


class _RlQosFreeIndexesTableId_Type(Integer32):
    """Custom type rlQosFreeIndexesTableId based on Integer32"""
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
        *(("ace", 3),
          ("acl", 4),
          ("class", 5),
          ("offset", 2),
          ("policer", 7),
          ("policy", 6),
          ("shaper", 8),
          ("tuple", 1))
    )


_RlQosFreeIndexesTableId_Type.__name__ = "Integer32"
_RlQosFreeIndexesTableId_Object = MibTableColumn
rlQosFreeIndexesTableId = _RlQosFreeIndexesTableId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 25, 1, 1),
    _RlQosFreeIndexesTableId_Type()
)
rlQosFreeIndexesTableId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosFreeIndexesTableId.setStatus("current")
_RlQosFreeIndexesValue_Type = Integer32
_RlQosFreeIndexesValue_Object = MibTableColumn
rlQosFreeIndexesValue = _RlQosFreeIndexesValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 25, 1, 2),
    _RlQosFreeIndexesValue_Type()
)
rlQosFreeIndexesValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosFreeIndexesValue.setStatus("current")
_RlQosNamesToIndexesTable_Object = MibTable
rlQosNamesToIndexesTable = _RlQosNamesToIndexesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 26)
)
if mibBuilder.loadTexts:
    rlQosNamesToIndexesTable.setStatus("current")
_RlQosNamesToIndexesEntry_Object = MibTableRow
rlQosNamesToIndexesEntry = _RlQosNamesToIndexesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 26, 1)
)
rlQosNamesToIndexesEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosNamesToIndexesTableId"),
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosNamesToIndexesName"),
)
if mibBuilder.loadTexts:
    rlQosNamesToIndexesEntry.setStatus("current")


class _RlQosNamesToIndexesTableId_Type(Integer32):
    """Custom type rlQosNamesToIndexesTableId based on Integer32"""
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
        *(("acl", 1),
          ("class", 2),
          ("policer", 4),
          ("policy", 3))
    )


_RlQosNamesToIndexesTableId_Type.__name__ = "Integer32"
_RlQosNamesToIndexesTableId_Object = MibTableColumn
rlQosNamesToIndexesTableId = _RlQosNamesToIndexesTableId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 26, 1, 1),
    _RlQosNamesToIndexesTableId_Type()
)
rlQosNamesToIndexesTableId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosNamesToIndexesTableId.setStatus("current")


class _RlQosNamesToIndexesName_Type(DisplayString):
    """Custom type rlQosNamesToIndexesName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlQosNamesToIndexesName_Type.__name__ = "DisplayString"
_RlQosNamesToIndexesName_Object = MibTableColumn
rlQosNamesToIndexesName = _RlQosNamesToIndexesName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 26, 1, 2),
    _RlQosNamesToIndexesName_Type()
)
rlQosNamesToIndexesName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosNamesToIndexesName.setStatus("current")
_RlQosNamesToIndexesValue_Type = Integer32
_RlQosNamesToIndexesValue_Object = MibTableColumn
rlQosNamesToIndexesValue = _RlQosNamesToIndexesValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 26, 1, 3),
    _RlQosNamesToIndexesValue_Type()
)
rlQosNamesToIndexesValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosNamesToIndexesValue.setStatus("current")
_RlQosStackControlQueue_Type = Integer32
_RlQosStackControlQueue_Object = MibScalar
rlQosStackControlQueue = _RlQosStackControlQueue_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 27),
    _RlQosStackControlQueue_Type()
)
rlQosStackControlQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosStackControlQueue.setStatus("current")
_RlQosStackControlCos_Type = Integer32
_RlQosStackControlCos_Object = MibScalar
rlQosStackControlCos = _RlQosStackControlCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 28),
    _RlQosStackControlCos_Type()
)
rlQosStackControlCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosStackControlCos.setStatus("current")
_RlQosCosQueueDefaultMapTable_Object = MibTable
rlQosCosQueueDefaultMapTable = _RlQosCosQueueDefaultMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 29)
)
if mibBuilder.loadTexts:
    rlQosCosQueueDefaultMapTable.setStatus("current")
_RlQosCosQueueDefaultMapEntry_Object = MibTableRow
rlQosCosQueueDefaultMapEntry = _RlQosCosQueueDefaultMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 29, 1)
)
rlQosCosQueueDefaultMapEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosCosQueueDefaultMapVpt"),
)
if mibBuilder.loadTexts:
    rlQosCosQueueDefaultMapEntry.setStatus("current")


class _RlQosCosQueueDefaultMapVpt_Type(Integer32):
    """Custom type rlQosCosQueueDefaultMapVpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RlQosCosQueueDefaultMapVpt_Type.__name__ = "Integer32"
_RlQosCosQueueDefaultMapVpt_Object = MibTableColumn
rlQosCosQueueDefaultMapVpt = _RlQosCosQueueDefaultMapVpt_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 29, 1, 1),
    _RlQosCosQueueDefaultMapVpt_Type()
)
rlQosCosQueueDefaultMapVpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosCosQueueDefaultMapVpt.setStatus("current")


class _RlQosCosQueueDefaultMapQueueId_Type(Integer32):
    """Custom type rlQosCosQueueDefaultMapQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RlQosCosQueueDefaultMapQueueId_Type.__name__ = "Integer32"
_RlQosCosQueueDefaultMapQueueId_Object = MibTableColumn
rlQosCosQueueDefaultMapQueueId = _RlQosCosQueueDefaultMapQueueId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 29, 1, 2),
    _RlQosCosQueueDefaultMapQueueId_Type()
)
rlQosCosQueueDefaultMapQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosCosQueueDefaultMapQueueId.setStatus("current")
_RlQosPredefBlockAclTable_Object = MibTable
rlQosPredefBlockAclTable = _RlQosPredefBlockAclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 30)
)
if mibBuilder.loadTexts:
    rlQosPredefBlockAclTable.setStatus("current")
_RlQosPredefBlockAclEntry_Object = MibTableRow
rlQosPredefBlockAclEntry = _RlQosPredefBlockAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 30, 1)
)
rlQosPredefBlockAclEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosPredefBlockAclIfIndex"),
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosPredefBlockAclIfType"),
)
if mibBuilder.loadTexts:
    rlQosPredefBlockAclEntry.setStatus("current")
_RlQosPredefBlockAclIfIndex_Type = InterfaceIndex
_RlQosPredefBlockAclIfIndex_Object = MibTableColumn
rlQosPredefBlockAclIfIndex = _RlQosPredefBlockAclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 30, 1, 1),
    _RlQosPredefBlockAclIfIndex_Type()
)
rlQosPredefBlockAclIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosPredefBlockAclIfIndex.setStatus("current")
_RlQosPredefBlockAclIfType_Type = InterfaceType
_RlQosPredefBlockAclIfType_Object = MibTableColumn
rlQosPredefBlockAclIfType = _RlQosPredefBlockAclIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 30, 1, 2),
    _RlQosPredefBlockAclIfType_Type()
)
rlQosPredefBlockAclIfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosPredefBlockAclIfType.setStatus("current")


class _RlQosPredefBlockAclMask_Type(OctetString):
    """Custom type rlQosPredefBlockAclMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_RlQosPredefBlockAclMask_Type.__name__ = "OctetString"
_RlQosPredefBlockAclMask_Object = MibTableColumn
rlQosPredefBlockAclMask = _RlQosPredefBlockAclMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 30, 1, 3),
    _RlQosPredefBlockAclMask_Type()
)
rlQosPredefBlockAclMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPredefBlockAclMask.setStatus("current")
_RlQosPredefBlockAclStatus_Type = RowStatus
_RlQosPredefBlockAclStatus_Object = MibTableColumn
rlQosPredefBlockAclStatus = _RlQosPredefBlockAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 30, 1, 4),
    _RlQosPredefBlockAclStatus_Type()
)
rlQosPredefBlockAclStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPredefBlockAclStatus.setStatus("current")
_RlQosAceTidxTable_Object = MibTable
rlQosAceTidxTable = _RlQosAceTidxTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 31)
)
if mibBuilder.loadTexts:
    rlQosAceTidxTable.setStatus("current")
_RlQosAceTidxEntry_Object = MibTableRow
rlQosAceTidxEntry = _RlQosAceTidxEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 31, 1)
)
rlQosAceTidxEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosAceTidxAclIndex"),
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosAceTidxIndex"),
)
if mibBuilder.loadTexts:
    rlQosAceTidxEntry.setStatus("current")
_RlQosAceTidxAclIndex_Type = Integer32
_RlQosAceTidxAclIndex_Object = MibTableColumn
rlQosAceTidxAclIndex = _RlQosAceTidxAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 31, 1, 1),
    _RlQosAceTidxAclIndex_Type()
)
rlQosAceTidxAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosAceTidxAclIndex.setStatus("current")
_RlQosAceTidxIndex_Type = Integer32
_RlQosAceTidxIndex_Object = MibTableColumn
rlQosAceTidxIndex = _RlQosAceTidxIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 31, 1, 2),
    _RlQosAceTidxIndex_Type()
)
rlQosAceTidxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosAceTidxIndex.setStatus("current")
_RlQosAceTidxAction_Type = AceActionType
_RlQosAceTidxAction_Object = MibTableColumn
rlQosAceTidxAction = _RlQosAceTidxAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 31, 1, 3),
    _RlQosAceTidxAction_Type()
)
rlQosAceTidxAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTidxAction.setStatus("current")
_RlQosAceTidxType_Type = AceObjectType
_RlQosAceTidxType_Object = MibTableColumn
rlQosAceTidxType = _RlQosAceTidxType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 31, 1, 4),
    _RlQosAceTidxType_Type()
)
rlQosAceTidxType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTidxType.setStatus("current")
_RlQosAceTidxTuple1_Type = Integer32
_RlQosAceTidxTuple1_Object = MibTableColumn
rlQosAceTidxTuple1 = _RlQosAceTidxTuple1_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 31, 1, 5),
    _RlQosAceTidxTuple1_Type()
)
rlQosAceTidxTuple1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTidxTuple1.setStatus("current")
_RlQosAceTidxTuple2_Type = Integer32
_RlQosAceTidxTuple2_Object = MibTableColumn
rlQosAceTidxTuple2 = _RlQosAceTidxTuple2_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 31, 1, 6),
    _RlQosAceTidxTuple2_Type()
)
rlQosAceTidxTuple2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTidxTuple2.setStatus("current")
_RlQosAceTidxTuple3_Type = Integer32
_RlQosAceTidxTuple3_Object = MibTableColumn
rlQosAceTidxTuple3 = _RlQosAceTidxTuple3_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 31, 1, 7),
    _RlQosAceTidxTuple3_Type()
)
rlQosAceTidxTuple3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTidxTuple3.setStatus("current")
_RlQosAceTidxTuple4_Type = Integer32
_RlQosAceTidxTuple4_Object = MibTableColumn
rlQosAceTidxTuple4 = _RlQosAceTidxTuple4_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 31, 1, 8),
    _RlQosAceTidxTuple4_Type()
)
rlQosAceTidxTuple4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTidxTuple4.setStatus("current")
_RlQosAceTidxTuple5_Type = Integer32
_RlQosAceTidxTuple5_Object = MibTableColumn
rlQosAceTidxTuple5 = _RlQosAceTidxTuple5_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 31, 1, 9),
    _RlQosAceTidxTuple5_Type()
)
rlQosAceTidxTuple5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTidxTuple5.setStatus("current")
_RlQosAceTidxTuple6_Type = Integer32
_RlQosAceTidxTuple6_Object = MibTableColumn
rlQosAceTidxTuple6 = _RlQosAceTidxTuple6_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 31, 1, 10),
    _RlQosAceTidxTuple6_Type()
)
rlQosAceTidxTuple6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTidxTuple6.setStatus("current")
_RlQosAceTidxTuple7_Type = Integer32
_RlQosAceTidxTuple7_Object = MibTableColumn
rlQosAceTidxTuple7 = _RlQosAceTidxTuple7_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 31, 1, 11),
    _RlQosAceTidxTuple7_Type()
)
rlQosAceTidxTuple7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTidxTuple7.setStatus("current")
_RlQosAceTidxTuple8_Type = Integer32
_RlQosAceTidxTuple8_Object = MibTableColumn
rlQosAceTidxTuple8 = _RlQosAceTidxTuple8_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 31, 1, 12),
    _RlQosAceTidxTuple8_Type()
)
rlQosAceTidxTuple8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTidxTuple8.setStatus("current")
_RlQosAceTidxAccount_Type = BinaryStatus
_RlQosAceTidxAccount_Object = MibTableColumn
rlQosAceTidxAccount = _RlQosAceTidxAccount_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 31, 1, 13),
    _RlQosAceTidxAccount_Type()
)
rlQosAceTidxAccount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTidxAccount.setStatus("current")
_RlQosAceTidxStatus_Type = RowStatus
_RlQosAceTidxStatus_Object = MibTableColumn
rlQosAceTidxStatus = _RlQosAceTidxStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 31, 1, 14),
    _RlQosAceTidxStatus_Type()
)
rlQosAceTidxStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTidxStatus.setStatus("current")


class _RlQosAceTidxTimeRange_Type(DisplayString):
    """Custom type rlQosAceTidxTimeRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlQosAceTidxTimeRange_Type.__name__ = "DisplayString"
_RlQosAceTidxTimeRange_Object = MibTableColumn
rlQosAceTidxTimeRange = _RlQosAceTidxTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 31, 1, 15),
    _RlQosAceTidxTimeRange_Type()
)
rlQosAceTidxTimeRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTidxTimeRange.setStatus("current")
_RlQosAceTidxTimeRangeIsActive_Type = TruthValue
_RlQosAceTidxTimeRangeIsActive_Object = MibTableColumn
rlQosAceTidxTimeRangeIsActive = _RlQosAceTidxTimeRangeIsActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 31, 1, 16),
    _RlQosAceTidxTimeRangeIsActive_Type()
)
rlQosAceTidxTimeRangeIsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosAceTidxTimeRangeIsActive.setStatus("current")
_RlQosAceTidxTuple9_Type = Integer32
_RlQosAceTidxTuple9_Object = MibTableColumn
rlQosAceTidxTuple9 = _RlQosAceTidxTuple9_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 31, 1, 17),
    _RlQosAceTidxTuple9_Type()
)
rlQosAceTidxTuple9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTidxTuple9.setStatus("current")
_RlQosAceTidxTuple10_Type = Integer32
_RlQosAceTidxTuple10_Object = MibTableColumn
rlQosAceTidxTuple10 = _RlQosAceTidxTuple10_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 31, 1, 18),
    _RlQosAceTidxTuple10_Type()
)
rlQosAceTidxTuple10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTidxTuple10.setStatus("current")
_RlQosAceTidxTuple11_Type = Integer32
_RlQosAceTidxTuple11_Object = MibTableColumn
rlQosAceTidxTuple11 = _RlQosAceTidxTuple11_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 31, 1, 19),
    _RlQosAceTidxTuple11_Type()
)
rlQosAceTidxTuple11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTidxTuple11.setStatus("current")
_RlQosAceTidxActionDropType_Type = RlQosAceTidxActionDropType
_RlQosAceTidxActionDropType_Object = MibTableColumn
rlQosAceTidxActionDropType = _RlQosAceTidxActionDropType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 31, 1, 20),
    _RlQosAceTidxActionDropType_Type()
)
rlQosAceTidxActionDropType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosAceTidxActionDropType.setStatus("current")
_RlQosMibVersion_Type = Integer32
_RlQosMibVersion_Object = MibScalar
rlQosMibVersion = _RlQosMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 32),
    _RlQosMibVersion_Type()
)
rlQosMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosMibVersion.setStatus("current")
_RlQosDscpQueueDefaultMapTable_Object = MibTable
rlQosDscpQueueDefaultMapTable = _RlQosDscpQueueDefaultMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 33)
)
if mibBuilder.loadTexts:
    rlQosDscpQueueDefaultMapTable.setStatus("current")
_RlQosDscpQueueDefaultMapEntry_Object = MibTableRow
rlQosDscpQueueDefaultMapEntry = _RlQosDscpQueueDefaultMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 33, 1)
)
rlQosDscpQueueDefaultMapEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosDscpQueueDefaultMapDscp"),
)
if mibBuilder.loadTexts:
    rlQosDscpQueueDefaultMapEntry.setStatus("current")


class _RlQosDscpQueueDefaultMapDscp_Type(Integer32):
    """Custom type rlQosDscpQueueDefaultMapDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RlQosDscpQueueDefaultMapDscp_Type.__name__ = "Integer32"
_RlQosDscpQueueDefaultMapDscp_Object = MibTableColumn
rlQosDscpQueueDefaultMapDscp = _RlQosDscpQueueDefaultMapDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 33, 1, 1),
    _RlQosDscpQueueDefaultMapDscp_Type()
)
rlQosDscpQueueDefaultMapDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosDscpQueueDefaultMapDscp.setStatus("current")


class _RlQosDscpQueueDefaultMapQueueId_Type(Integer32):
    """Custom type rlQosDscpQueueDefaultMapQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RlQosDscpQueueDefaultMapQueueId_Type.__name__ = "Integer32"
_RlQosDscpQueueDefaultMapQueueId_Object = MibTableColumn
rlQosDscpQueueDefaultMapQueueId = _RlQosDscpQueueDefaultMapQueueId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 33, 1, 2),
    _RlQosDscpQueueDefaultMapQueueId_Type()
)
rlQosDscpQueueDefaultMapQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosDscpQueueDefaultMapQueueId.setStatus("current")
_RlQosDscpToDpTable_Object = MibTable
rlQosDscpToDpTable = _RlQosDscpToDpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 34)
)
if mibBuilder.loadTexts:
    rlQosDscpToDpTable.setStatus("current")
_RlQosDscpToDpEntry_Object = MibTableRow
rlQosDscpToDpEntry = _RlQosDscpToDpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 34, 1)
)
rlQosDscpToDpEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosDscp"),
)
if mibBuilder.loadTexts:
    rlQosDscpToDpEntry.setStatus("current")


class _RlQosDscp_Type(Integer32):
    """Custom type rlQosDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RlQosDscp_Type.__name__ = "Integer32"
_RlQosDscp_Object = MibTableColumn
rlQosDscp = _RlQosDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 34, 1, 1),
    _RlQosDscp_Type()
)
rlQosDscp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosDscp.setStatus("current")


class _RlQosDp_Type(Integer32):
    """Custom type rlQosDp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_RlQosDp_Type.__name__ = "Integer32"
_RlQosDp_Object = MibTableColumn
rlQosDp = _RlQosDp_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 34, 1, 2),
    _RlQosDp_Type()
)
rlQosDp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosDp.setStatus("current")
_RlQosStatistics_ObjectIdentity = ObjectIdentity
rlQosStatistics = _RlQosStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35)
)
_RlQosPortPolicyStatisticsTable_Object = MibTable
rlQosPortPolicyStatisticsTable = _RlQosPortPolicyStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 1)
)
if mibBuilder.loadTexts:
    rlQosPortPolicyStatisticsTable.setStatus("current")
_RlQosPortPolicyStatisticsEntry_Object = MibTableRow
rlQosPortPolicyStatisticsEntry = _RlQosPortPolicyStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 1, 1)
)
rlQosPortPolicyStatisticsEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlIfIndex"),
    (0, "CISCOSB-QOS-CLI-MIB", "rlIfType"),
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosPortPolicyStatisticsCntrType"),
)
if mibBuilder.loadTexts:
    rlQosPortPolicyStatisticsEntry.setStatus("current")
_RlQosPortPolicyStatisticsCntrType_Type = StatisticsCntrType
_RlQosPortPolicyStatisticsCntrType_Object = MibTableColumn
rlQosPortPolicyStatisticsCntrType = _RlQosPortPolicyStatisticsCntrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 1, 1, 1),
    _RlQosPortPolicyStatisticsCntrType_Type()
)
rlQosPortPolicyStatisticsCntrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosPortPolicyStatisticsCntrType.setStatus("current")
_RlQosPortPolicyStatisticsCntrNumOfBits_Type = StatisticsCntrNumOfBitsType
_RlQosPortPolicyStatisticsCntrNumOfBits_Object = MibTableColumn
rlQosPortPolicyStatisticsCntrNumOfBits = _RlQosPortPolicyStatisticsCntrNumOfBits_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 1, 1, 2),
    _RlQosPortPolicyStatisticsCntrNumOfBits_Type()
)
rlQosPortPolicyStatisticsCntrNumOfBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosPortPolicyStatisticsCntrNumOfBits.setStatus("current")


class _RlQosPortPolicyStatisticsEnableCounting_Type(TruthValue):
    """Custom type rlQosPortPolicyStatisticsEnableCounting based on TruthValue"""


_RlQosPortPolicyStatisticsEnableCounting_Object = MibTableColumn
rlQosPortPolicyStatisticsEnableCounting = _RlQosPortPolicyStatisticsEnableCounting_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 1, 1, 3),
    _RlQosPortPolicyStatisticsEnableCounting_Type()
)
rlQosPortPolicyStatisticsEnableCounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosPortPolicyStatisticsEnableCounting.setStatus("current")
_RlQosPortPolicyStatisticsCounterValue_Type = Counter64
_RlQosPortPolicyStatisticsCounterValue_Object = MibTableColumn
rlQosPortPolicyStatisticsCounterValue = _RlQosPortPolicyStatisticsCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 1, 1, 4),
    _RlQosPortPolicyStatisticsCounterValue_Type()
)
rlQosPortPolicyStatisticsCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosPortPolicyStatisticsCounterValue.setStatus("current")
_RlQosSinglePolicerStatisticsTable_Object = MibTable
rlQosSinglePolicerStatisticsTable = _RlQosSinglePolicerStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 2)
)
if mibBuilder.loadTexts:
    rlQosSinglePolicerStatisticsTable.setStatus("current")
_RlQosSinglePolicerStatisticsEntry_Object = MibTableRow
rlQosSinglePolicerStatisticsEntry = _RlQosSinglePolicerStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 2, 1)
)
rlQosSinglePolicerStatisticsEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlIfIndex"),
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosPolicerIndex"),
)
if mibBuilder.loadTexts:
    rlQosSinglePolicerStatisticsEntry.setStatus("current")
_RlQosSinglePolicerStatisticsInProfileCounterValue_Type = Counter64
_RlQosSinglePolicerStatisticsInProfileCounterValue_Object = MibTableColumn
rlQosSinglePolicerStatisticsInProfileCounterValue = _RlQosSinglePolicerStatisticsInProfileCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 2, 1, 1),
    _RlQosSinglePolicerStatisticsInProfileCounterValue_Type()
)
rlQosSinglePolicerStatisticsInProfileCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosSinglePolicerStatisticsInProfileCounterValue.setStatus("current")
_RlQosSinglePolicerStatisticsInProfileCntrNumOfBits_Type = StatisticsCntrNumOfBitsType
_RlQosSinglePolicerStatisticsInProfileCntrNumOfBits_Object = MibTableColumn
rlQosSinglePolicerStatisticsInProfileCntrNumOfBits = _RlQosSinglePolicerStatisticsInProfileCntrNumOfBits_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 2, 1, 2),
    _RlQosSinglePolicerStatisticsInProfileCntrNumOfBits_Type()
)
rlQosSinglePolicerStatisticsInProfileCntrNumOfBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosSinglePolicerStatisticsInProfileCntrNumOfBits.setStatus("current")
_RlQosSinglePolicerStatisticsOutProfileCounterValue_Type = Counter64
_RlQosSinglePolicerStatisticsOutProfileCounterValue_Object = MibTableColumn
rlQosSinglePolicerStatisticsOutProfileCounterValue = _RlQosSinglePolicerStatisticsOutProfileCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 2, 1, 3),
    _RlQosSinglePolicerStatisticsOutProfileCounterValue_Type()
)
rlQosSinglePolicerStatisticsOutProfileCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosSinglePolicerStatisticsOutProfileCounterValue.setStatus("current")
_RlQosSinglePolicerStatisticsOutProfileCntrNumOfBits_Type = StatisticsCntrNumOfBitsType
_RlQosSinglePolicerStatisticsOutProfileCntrNumOfBits_Object = MibTableColumn
rlQosSinglePolicerStatisticsOutProfileCntrNumOfBits = _RlQosSinglePolicerStatisticsOutProfileCntrNumOfBits_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 2, 1, 4),
    _RlQosSinglePolicerStatisticsOutProfileCntrNumOfBits_Type()
)
rlQosSinglePolicerStatisticsOutProfileCntrNumOfBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosSinglePolicerStatisticsOutProfileCntrNumOfBits.setStatus("current")
_RlQosSinglePolicerStatisticsStatus_Type = RowStatus
_RlQosSinglePolicerStatisticsStatus_Object = MibTableColumn
rlQosSinglePolicerStatisticsStatus = _RlQosSinglePolicerStatisticsStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 2, 1, 5),
    _RlQosSinglePolicerStatisticsStatus_Type()
)
rlQosSinglePolicerStatisticsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosSinglePolicerStatisticsStatus.setStatus("current")
_RlQosAggregatePolicerStatisticsTable_Object = MibTable
rlQosAggregatePolicerStatisticsTable = _RlQosAggregatePolicerStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 3)
)
if mibBuilder.loadTexts:
    rlQosAggregatePolicerStatisticsTable.setStatus("current")
_RlQosAggregatePolicerStatisticsEntry_Object = MibTableRow
rlQosAggregatePolicerStatisticsEntry = _RlQosAggregatePolicerStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 3, 1)
)
rlQosAggregatePolicerStatisticsEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosPolicerIndex"),
)
if mibBuilder.loadTexts:
    rlQosAggregatePolicerStatisticsEntry.setStatus("current")
_RlQosAggregatePolicerStatisticsInProfileCounterValue_Type = Counter64
_RlQosAggregatePolicerStatisticsInProfileCounterValue_Object = MibTableColumn
rlQosAggregatePolicerStatisticsInProfileCounterValue = _RlQosAggregatePolicerStatisticsInProfileCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 3, 1, 1),
    _RlQosAggregatePolicerStatisticsInProfileCounterValue_Type()
)
rlQosAggregatePolicerStatisticsInProfileCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosAggregatePolicerStatisticsInProfileCounterValue.setStatus("current")
_RlQosAggregatePolicerStatisticsInProfileCntrNumOfBits_Type = StatisticsCntrNumOfBitsType
_RlQosAggregatePolicerStatisticsInProfileCntrNumOfBits_Object = MibTableColumn
rlQosAggregatePolicerStatisticsInProfileCntrNumOfBits = _RlQosAggregatePolicerStatisticsInProfileCntrNumOfBits_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 3, 1, 2),
    _RlQosAggregatePolicerStatisticsInProfileCntrNumOfBits_Type()
)
rlQosAggregatePolicerStatisticsInProfileCntrNumOfBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosAggregatePolicerStatisticsInProfileCntrNumOfBits.setStatus("current")
_RlQosAggregatePolicerStatisticsOutProfileCounterValue_Type = Counter64
_RlQosAggregatePolicerStatisticsOutProfileCounterValue_Object = MibTableColumn
rlQosAggregatePolicerStatisticsOutProfileCounterValue = _RlQosAggregatePolicerStatisticsOutProfileCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 3, 1, 3),
    _RlQosAggregatePolicerStatisticsOutProfileCounterValue_Type()
)
rlQosAggregatePolicerStatisticsOutProfileCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosAggregatePolicerStatisticsOutProfileCounterValue.setStatus("current")
_RlQosAggregatePolicerStatisticsOutProfileCntrNumOfBits_Type = StatisticsCntrNumOfBitsType
_RlQosAggregatePolicerStatisticsOutProfileCntrNumOfBits_Object = MibTableColumn
rlQosAggregatePolicerStatisticsOutProfileCntrNumOfBits = _RlQosAggregatePolicerStatisticsOutProfileCntrNumOfBits_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 3, 1, 4),
    _RlQosAggregatePolicerStatisticsOutProfileCntrNumOfBits_Type()
)
rlQosAggregatePolicerStatisticsOutProfileCntrNumOfBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosAggregatePolicerStatisticsOutProfileCntrNumOfBits.setStatus("current")
_RlQosAggregatePolicerStatisticsStatus_Type = RowStatus
_RlQosAggregatePolicerStatisticsStatus_Object = MibTableColumn
rlQosAggregatePolicerStatisticsStatus = _RlQosAggregatePolicerStatisticsStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 3, 1, 5),
    _RlQosAggregatePolicerStatisticsStatus_Type()
)
rlQosAggregatePolicerStatisticsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosAggregatePolicerStatisticsStatus.setStatus("current")
_RlQosOutQueueStatisticsTable_Object = MibTable
rlQosOutQueueStatisticsTable = _RlQosOutQueueStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 4)
)
if mibBuilder.loadTexts:
    rlQosOutQueueStatisticsTable.setStatus("current")
_RlQosOutQueueStatisticsEntry_Object = MibTableRow
rlQosOutQueueStatisticsEntry = _RlQosOutQueueStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 4, 1)
)
rlQosOutQueueStatisticsEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosOutQueueStatisticsCountrID"),
)
if mibBuilder.loadTexts:
    rlQosOutQueueStatisticsEntry.setStatus("current")
_RlQosOutQueueStatisticsCountrID_Type = Integer32
_RlQosOutQueueStatisticsCountrID_Object = MibTableColumn
rlQosOutQueueStatisticsCountrID = _RlQosOutQueueStatisticsCountrID_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 4, 1, 1),
    _RlQosOutQueueStatisticsCountrID_Type()
)
rlQosOutQueueStatisticsCountrID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosOutQueueStatisticsCountrID.setStatus("current")
_RlQosOutQueueStatisticsIfIndexList_Type = PortList
_RlQosOutQueueStatisticsIfIndexList_Object = MibTableColumn
rlQosOutQueueStatisticsIfIndexList = _RlQosOutQueueStatisticsIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 4, 1, 2),
    _RlQosOutQueueStatisticsIfIndexList_Type()
)
rlQosOutQueueStatisticsIfIndexList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosOutQueueStatisticsIfIndexList.setStatus("current")
_RlQosOutQueueStatisticsPortAll_Type = TruthValue
_RlQosOutQueueStatisticsPortAll_Object = MibTableColumn
rlQosOutQueueStatisticsPortAll = _RlQosOutQueueStatisticsPortAll_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 4, 1, 3),
    _RlQosOutQueueStatisticsPortAll_Type()
)
rlQosOutQueueStatisticsPortAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosOutQueueStatisticsPortAll.setStatus("current")
_RlQosOutQueueStatisticsVlan_Type = Integer32
_RlQosOutQueueStatisticsVlan_Object = MibTableColumn
rlQosOutQueueStatisticsVlan = _RlQosOutQueueStatisticsVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 4, 1, 4),
    _RlQosOutQueueStatisticsVlan_Type()
)
rlQosOutQueueStatisticsVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosOutQueueStatisticsVlan.setStatus("current")
_RlQosOutQueueStatisticsVlanAll_Type = TruthValue
_RlQosOutQueueStatisticsVlanAll_Object = MibTableColumn
rlQosOutQueueStatisticsVlanAll = _RlQosOutQueueStatisticsVlanAll_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 4, 1, 5),
    _RlQosOutQueueStatisticsVlanAll_Type()
)
rlQosOutQueueStatisticsVlanAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosOutQueueStatisticsVlanAll.setStatus("current")


class _RlQosOutQueueStatisticsQueue_Type(Integer32):
    """Custom type rlQosOutQueueStatisticsQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RlQosOutQueueStatisticsQueue_Type.__name__ = "Integer32"
_RlQosOutQueueStatisticsQueue_Object = MibTableColumn
rlQosOutQueueStatisticsQueue = _RlQosOutQueueStatisticsQueue_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 4, 1, 6),
    _RlQosOutQueueStatisticsQueue_Type()
)
rlQosOutQueueStatisticsQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosOutQueueStatisticsQueue.setStatus("current")
_RlQosOutQueueStatisticsQueueAll_Type = TruthValue
_RlQosOutQueueStatisticsQueueAll_Object = MibTableColumn
rlQosOutQueueStatisticsQueueAll = _RlQosOutQueueStatisticsQueueAll_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 4, 1, 7),
    _RlQosOutQueueStatisticsQueueAll_Type()
)
rlQosOutQueueStatisticsQueueAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosOutQueueStatisticsQueueAll.setStatus("current")
_RlQosOutQueueStatisticsDP_Type = StatisticsDPType
_RlQosOutQueueStatisticsDP_Object = MibTableColumn
rlQosOutQueueStatisticsDP = _RlQosOutQueueStatisticsDP_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 4, 1, 8),
    _RlQosOutQueueStatisticsDP_Type()
)
rlQosOutQueueStatisticsDP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosOutQueueStatisticsDP.setStatus("current")
_RlQosOutQueueStatisticsDPAll_Type = TruthValue
_RlQosOutQueueStatisticsDPAll_Object = MibTableColumn
rlQosOutQueueStatisticsDPAll = _RlQosOutQueueStatisticsDPAll_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 4, 1, 9),
    _RlQosOutQueueStatisticsDPAll_Type()
)
rlQosOutQueueStatisticsDPAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosOutQueueStatisticsDPAll.setStatus("current")
_RlQosOutQueueStatisticsCounterTailDropValue_Type = Counter64
_RlQosOutQueueStatisticsCounterTailDropValue_Object = MibTableColumn
rlQosOutQueueStatisticsCounterTailDropValue = _RlQosOutQueueStatisticsCounterTailDropValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 4, 1, 10),
    _RlQosOutQueueStatisticsCounterTailDropValue_Type()
)
rlQosOutQueueStatisticsCounterTailDropValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosOutQueueStatisticsCounterTailDropValue.setStatus("current")
_RlQosOutQueueStatisticsCounterAllValue_Type = Counter64
_RlQosOutQueueStatisticsCounterAllValue_Object = MibTableColumn
rlQosOutQueueStatisticsCounterAllValue = _RlQosOutQueueStatisticsCounterAllValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 4, 1, 11),
    _RlQosOutQueueStatisticsCounterAllValue_Type()
)
rlQosOutQueueStatisticsCounterAllValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosOutQueueStatisticsCounterAllValue.setStatus("current")
_RlQosOutQueueStatisticsCntrNumOfBits_Type = StatisticsCntrNumOfBitsType
_RlQosOutQueueStatisticsCntrNumOfBits_Object = MibTableColumn
rlQosOutQueueStatisticsCntrNumOfBits = _RlQosOutQueueStatisticsCntrNumOfBits_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 4, 1, 12),
    _RlQosOutQueueStatisticsCntrNumOfBits_Type()
)
rlQosOutQueueStatisticsCntrNumOfBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosOutQueueStatisticsCntrNumOfBits.setStatus("current")
_RlQosOutQueueStatisticsStatus_Type = RowStatus
_RlQosOutQueueStatisticsStatus_Object = MibTableColumn
rlQosOutQueueStatisticsStatus = _RlQosOutQueueStatisticsStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 4, 1, 13),
    _RlQosOutQueueStatisticsStatus_Type()
)
rlQosOutQueueStatisticsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosOutQueueStatisticsStatus.setStatus("current")
_RlQosGlobalStatisticsCntrsTable_Object = MibTable
rlQosGlobalStatisticsCntrsTable = _RlQosGlobalStatisticsCntrsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 5)
)
if mibBuilder.loadTexts:
    rlQosGlobalStatisticsCntrsTable.setStatus("current")
_RlQosGlobalStatisticsCntrsEntry_Object = MibTableRow
rlQosGlobalStatisticsCntrsEntry = _RlQosGlobalStatisticsCntrsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 5, 1)
)
rlQosGlobalStatisticsCntrsEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosGlobalStatisticsCntrsType"),
)
if mibBuilder.loadTexts:
    rlQosGlobalStatisticsCntrsEntry.setStatus("current")
_RlQosGlobalStatisticsCntrsType_Type = StatisticsCntrType
_RlQosGlobalStatisticsCntrsType_Object = MibTableColumn
rlQosGlobalStatisticsCntrsType = _RlQosGlobalStatisticsCntrsType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 5, 1, 1),
    _RlQosGlobalStatisticsCntrsType_Type()
)
rlQosGlobalStatisticsCntrsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosGlobalStatisticsCntrsType.setStatus("current")
_RlQosGlobalStatisticsCntrsNumOfBits_Type = StatisticsCntrNumOfBitsType
_RlQosGlobalStatisticsCntrsNumOfBits_Object = MibTableColumn
rlQosGlobalStatisticsCntrsNumOfBits = _RlQosGlobalStatisticsCntrsNumOfBits_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 5, 1, 2),
    _RlQosGlobalStatisticsCntrsNumOfBits_Type()
)
rlQosGlobalStatisticsCntrsNumOfBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosGlobalStatisticsCntrsNumOfBits.setStatus("current")
_RlQosGlobalStatisticsCntrsCounterValue_Type = Counter64
_RlQosGlobalStatisticsCntrsCounterValue_Object = MibTableColumn
rlQosGlobalStatisticsCntrsCounterValue = _RlQosGlobalStatisticsCntrsCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 5, 1, 3),
    _RlQosGlobalStatisticsCntrsCounterValue_Type()
)
rlQosGlobalStatisticsCntrsCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosGlobalStatisticsCntrsCounterValue.setStatus("current")
_RlQosGlobalStatisticsStatus_Type = RowStatus
_RlQosGlobalStatisticsStatus_Object = MibTableColumn
rlQosGlobalStatisticsStatus = _RlQosGlobalStatisticsStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 5, 1, 4),
    _RlQosGlobalStatisticsStatus_Type()
)
rlQosGlobalStatisticsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosGlobalStatisticsStatus.setStatus("current")
_RlQosClearCounters_Type = Integer32
_RlQosClearCounters_Object = MibScalar
rlQosClearCounters = _RlQosClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 35, 6),
    _RlQosClearCounters_Type()
)
rlQosClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosClearCounters.setStatus("current")
_RlQosClassifierUtilization_ObjectIdentity = ObjectIdentity
rlQosClassifierUtilization = _RlQosClassifierUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 36)
)
_RlQosClassifierUtilizationTable_Object = MibTable
rlQosClassifierUtilizationTable = _RlQosClassifierUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 36, 1)
)
if mibBuilder.loadTexts:
    rlQosClassifierUtilizationTable.setStatus("current")
_RlQosClassifierUtilizationEntry_Object = MibTableRow
rlQosClassifierUtilizationEntry = _RlQosClassifierUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 36, 1, 1)
)
rlQosClassifierUtilizationEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosClassifierUtilizationUnitId"),
)
if mibBuilder.loadTexts:
    rlQosClassifierUtilizationEntry.setStatus("current")


class _RlQosClassifierUtilizationUnitId_Type(Unsigned32):
    """Custom type rlQosClassifierUtilizationUnitId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RlQosClassifierUtilizationUnitId_Type.__name__ = "Unsigned32"
_RlQosClassifierUtilizationUnitId_Object = MibTableColumn
rlQosClassifierUtilizationUnitId = _RlQosClassifierUtilizationUnitId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 36, 1, 1, 1),
    _RlQosClassifierUtilizationUnitId_Type()
)
rlQosClassifierUtilizationUnitId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosClassifierUtilizationUnitId.setStatus("current")


class _RlQosClassifierUtilizationPercent_Type(Unsigned32):
    """Custom type rlQosClassifierUtilizationPercent based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlQosClassifierUtilizationPercent_Type.__name__ = "Unsigned32"
_RlQosClassifierUtilizationPercent_Object = MibTableColumn
rlQosClassifierUtilizationPercent = _RlQosClassifierUtilizationPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 36, 1, 1, 2),
    _RlQosClassifierUtilizationPercent_Type()
)
rlQosClassifierUtilizationPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosClassifierUtilizationPercent.setStatus("current")


class _RlQosClassifierUtilizationRulesNumber_Type(Unsigned32):
    """Custom type rlQosClassifierUtilizationRulesNumber based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RlQosClassifierUtilizationRulesNumber_Type.__name__ = "Unsigned32"
_RlQosClassifierUtilizationRulesNumber_Object = MibTableColumn
rlQosClassifierUtilizationRulesNumber = _RlQosClassifierUtilizationRulesNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 36, 1, 1, 3),
    _RlQosClassifierUtilizationRulesNumber_Type()
)
rlQosClassifierUtilizationRulesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosClassifierUtilizationRulesNumber.setStatus("current")


class _RlQosClassifierUtilizationFreeRulesNumber_Type(Unsigned32):
    """Custom type rlQosClassifierUtilizationFreeRulesNumber based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RlQosClassifierUtilizationFreeRulesNumber_Type.__name__ = "Unsigned32"
_RlQosClassifierUtilizationFreeRulesNumber_Object = MibTableColumn
rlQosClassifierUtilizationFreeRulesNumber = _RlQosClassifierUtilizationFreeRulesNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 36, 1, 1, 4),
    _RlQosClassifierUtilizationFreeRulesNumber_Type()
)
rlQosClassifierUtilizationFreeRulesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosClassifierUtilizationFreeRulesNumber.setStatus("current")


class _RlQosClassifierUtilizationSystem_Type(Unsigned32):
    """Custom type rlQosClassifierUtilizationSystem based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RlQosClassifierUtilizationSystem_Type.__name__ = "Unsigned32"
_RlQosClassifierUtilizationSystem_Object = MibScalar
rlQosClassifierUtilizationSystem = _RlQosClassifierUtilizationSystem_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 36, 2),
    _RlQosClassifierUtilizationSystem_Type()
)
rlQosClassifierUtilizationSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosClassifierUtilizationSystem.setStatus("current")
_RlQosClassifierRulesNumberUtilizationSystem_Type = Unsigned32
_RlQosClassifierRulesNumberUtilizationSystem_Object = MibScalar
rlQosClassifierRulesNumberUtilizationSystem = _RlQosClassifierRulesNumberUtilizationSystem_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 36, 3),
    _RlQosClassifierRulesNumberUtilizationSystem_Type()
)
rlQosClassifierRulesNumberUtilizationSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosClassifierRulesNumberUtilizationSystem.setStatus("current")
_RlQosPortToProfileMappingTable_Object = MibTable
rlQosPortToProfileMappingTable = _RlQosPortToProfileMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 37)
)
if mibBuilder.loadTexts:
    rlQosPortToProfileMappingTable.setStatus("current")
_RlQosPortToProfileMappingEntry_Object = MibTableRow
rlQosPortToProfileMappingEntry = _RlQosPortToProfileMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 37, 1)
)
rlQosPortToProfileMappingEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosPort"),
)
if mibBuilder.loadTexts:
    rlQosPortToProfileMappingEntry.setStatus("current")
_RlQosPort_Type = Integer32
_RlQosPort_Object = MibTableColumn
rlQosPort = _RlQosPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 37, 1, 1),
    _RlQosPort_Type()
)
rlQosPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosPort.setStatus("current")
_RlQosProfileName_Type = DisplayString
_RlQosProfileName_Object = MibTableColumn
rlQosProfileName = _RlQosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 37, 1, 2),
    _RlQosProfileName_Type()
)
rlQosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosProfileName.setStatus("current")
_RlQosCPUSafeGuardEnable_Type = Integer32
_RlQosCPUSafeGuardEnable_Object = MibScalar
rlQosCPUSafeGuardEnable = _RlQosCPUSafeGuardEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 38),
    _RlQosCPUSafeGuardEnable_Type()
)
rlQosCPUSafeGuardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosCPUSafeGuardEnable.setStatus("current")
_RlQosPolicyClassPriorityRefTable_Object = MibTable
rlQosPolicyClassPriorityRefTable = _RlQosPolicyClassPriorityRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 39)
)
if mibBuilder.loadTexts:
    rlQosPolicyClassPriorityRefTable.setStatus("current")
_RlQosPolicyClassPriorityRefEntry_Object = MibTableRow
rlQosPolicyClassPriorityRefEntry = _RlQosPolicyClassPriorityRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 39, 1)
)
rlQosPolicyClassPriorityRefEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosPolicyClassPriorityRefPriority"),
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosPolicyClassPriorityRefClassPointer"),
)
if mibBuilder.loadTexts:
    rlQosPolicyClassPriorityRefEntry.setStatus("current")
_RlQosPolicyClassPriorityRefPriority_Type = Integer32
_RlQosPolicyClassPriorityRefPriority_Object = MibTableColumn
rlQosPolicyClassPriorityRefPriority = _RlQosPolicyClassPriorityRefPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 39, 1, 1),
    _RlQosPolicyClassPriorityRefPriority_Type()
)
rlQosPolicyClassPriorityRefPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosPolicyClassPriorityRefPriority.setStatus("current")
_RlQosPolicyClassPriorityRefClassPointer_Type = Integer32
_RlQosPolicyClassPriorityRefClassPointer_Object = MibTableColumn
rlQosPolicyClassPriorityRefClassPointer = _RlQosPolicyClassPriorityRefClassPointer_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 39, 1, 2),
    _RlQosPolicyClassPriorityRefClassPointer_Type()
)
rlQosPolicyClassPriorityRefClassPointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPolicyClassPriorityRefClassPointer.setStatus("current")
_RlQosPolicyClassPriorityRefPolicyPointer_Type = Integer32
_RlQosPolicyClassPriorityRefPolicyPointer_Object = MibTableColumn
rlQosPolicyClassPriorityRefPolicyPointer = _RlQosPolicyClassPriorityRefPolicyPointer_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 39, 1, 3),
    _RlQosPolicyClassPriorityRefPolicyPointer_Type()
)
rlQosPolicyClassPriorityRefPolicyPointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPolicyClassPriorityRefPolicyPointer.setStatus("current")
_RlQosPolicyClassPriorityRefStatus_Type = RowStatus
_RlQosPolicyClassPriorityRefStatus_Object = MibTableColumn
rlQosPolicyClassPriorityRefStatus = _RlQosPolicyClassPriorityRefStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 39, 1, 4),
    _RlQosPolicyClassPriorityRefStatus_Type()
)
rlQosPolicyClassPriorityRefStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlQosPolicyClassPriorityRefStatus.setStatus("current")
_RlQosDenyAceStatisticsTable_Object = MibTable
rlQosDenyAceStatisticsTable = _RlQosDenyAceStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 42)
)
if mibBuilder.loadTexts:
    rlQosDenyAceStatisticsTable.setStatus("current")
_RlQosDenyAceStatisticsEntry_Object = MibTableRow
rlQosDenyAceStatisticsEntry = _RlQosDenyAceStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 42, 1)
)
rlQosDenyAceStatisticsEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosDenyAceStatisticsIfIndex"),
)
if mibBuilder.loadTexts:
    rlQosDenyAceStatisticsEntry.setStatus("current")
_RlQosDenyAceStatisticsIfIndex_Type = Integer32
_RlQosDenyAceStatisticsIfIndex_Object = MibTableColumn
rlQosDenyAceStatisticsIfIndex = _RlQosDenyAceStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 42, 1, 1),
    _RlQosDenyAceStatisticsIfIndex_Type()
)
rlQosDenyAceStatisticsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosDenyAceStatisticsIfIndex.setStatus("current")
_RlQosDenyAceStatisticsIfCounter_Type = Integer32
_RlQosDenyAceStatisticsIfCounter_Object = MibTableColumn
rlQosDenyAceStatisticsIfCounter = _RlQosDenyAceStatisticsIfCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 42, 1, 2),
    _RlQosDenyAceStatisticsIfCounter_Type()
)
rlQosDenyAceStatisticsIfCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosDenyAceStatisticsIfCounter.setStatus("current")
_RlQosDenyAceStatisticsOtherFlowCounter_Type = Integer32
_RlQosDenyAceStatisticsOtherFlowCounter_Object = MibScalar
rlQosDenyAceStatisticsOtherFlowCounter = _RlQosDenyAceStatisticsOtherFlowCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 43),
    _RlQosDenyAceStatisticsOtherFlowCounter_Type()
)
rlQosDenyAceStatisticsOtherFlowCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosDenyAceStatisticsOtherFlowCounter.setStatus("current")
_RlQosDenyAceStatisticsClearIfCounters_Type = PortList
_RlQosDenyAceStatisticsClearIfCounters_Object = MibScalar
rlQosDenyAceStatisticsClearIfCounters = _RlQosDenyAceStatisticsClearIfCounters_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 44),
    _RlQosDenyAceStatisticsClearIfCounters_Type()
)
rlQosDenyAceStatisticsClearIfCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosDenyAceStatisticsClearIfCounters.setStatus("current")
_RlQosDenyAceStatisticsClearOtherFlowCounter_Type = Integer32
_RlQosDenyAceStatisticsClearOtherFlowCounter_Object = MibScalar
rlQosDenyAceStatisticsClearOtherFlowCounter = _RlQosDenyAceStatisticsClearOtherFlowCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 45),
    _RlQosDenyAceStatisticsClearOtherFlowCounter_Type()
)
rlQosDenyAceStatisticsClearOtherFlowCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosDenyAceStatisticsClearOtherFlowCounter.setStatus("current")
_RlQosModeGlobalCfgTable_Object = MibTable
rlQosModeGlobalCfgTable = _RlQosModeGlobalCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 46)
)
if mibBuilder.loadTexts:
    rlQosModeGlobalCfgTable.setStatus("current")
_RlQosModeGlobalCfgEntry_Object = MibTableRow
rlQosModeGlobalCfgEntry = _RlQosModeGlobalCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 46, 1)
)
rlQosModeGlobalCfgEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosGlobalIndex"),
)
if mibBuilder.loadTexts:
    rlQosModeGlobalCfgEntry.setStatus("current")
_RlQosGlobalIndex_Type = Integer32
_RlQosGlobalIndex_Object = MibTableColumn
rlQosGlobalIndex = _RlQosGlobalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 46, 1, 1),
    _RlQosGlobalIndex_Type()
)
rlQosGlobalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosGlobalIndex.setStatus("current")
_RlQosGlobalQoSMode_Type = QosGlobalMode
_RlQosGlobalQoSMode_Object = MibTableColumn
rlQosGlobalQoSMode = _RlQosGlobalQoSMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 46, 1, 2),
    _RlQosGlobalQoSMode_Type()
)
rlQosGlobalQoSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosGlobalQoSMode.setStatus("current")
_RlQosBasicGlobalTrustMode_Type = QosTrustMode
_RlQosBasicGlobalTrustMode_Object = MibTableColumn
rlQosBasicGlobalTrustMode = _RlQosBasicGlobalTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 46, 1, 3),
    _RlQosBasicGlobalTrustMode_Type()
)
rlQosBasicGlobalTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosBasicGlobalTrustMode.setStatus("current")
_RlQosAdvcGlobalTrustMode_Type = QosTrustMode
_RlQosAdvcGlobalTrustMode_Object = MibTableColumn
rlQosAdvcGlobalTrustMode = _RlQosAdvcGlobalTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 46, 1, 4),
    _RlQosAdvcGlobalTrustMode_Type()
)
rlQosAdvcGlobalTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosAdvcGlobalTrustMode.setStatus("current")


class _RlQoSPortTrustAdvancedMode_Type(TruthValue):
    """Custom type rlQoSPortTrustAdvancedMode based on TruthValue"""


_RlQoSPortTrustAdvancedMode_Object = MibTableColumn
rlQoSPortTrustAdvancedMode = _RlQoSPortTrustAdvancedMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 46, 1, 5),
    _RlQoSPortTrustAdvancedMode_Type()
)
rlQoSPortTrustAdvancedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQoSPortTrustAdvancedMode.setStatus("current")


class _RlQosDscpMutationEnable_Type(TruthValue):
    """Custom type rlQosDscpMutationEnable based on TruthValue"""


_RlQosDscpMutationEnable_Object = MibTableColumn
rlQosDscpMutationEnable = _RlQosDscpMutationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 46, 1, 6),
    _RlQosDscpMutationEnable_Type()
)
rlQosDscpMutationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosDscpMutationEnable.setStatus("current")
_RlQosModeGlobalCfgStatus_Type = RowStatus
_RlQosModeGlobalCfgStatus_Object = MibTableColumn
rlQosModeGlobalCfgStatus = _RlQosModeGlobalCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 46, 1, 7),
    _RlQosModeGlobalCfgStatus_Type()
)
rlQosModeGlobalCfgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQosModeGlobalCfgStatus.setStatus("current")
_RlQosClassMapCounterTable_Object = MibTable
rlQosClassMapCounterTable = _RlQosClassMapCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 47)
)
if mibBuilder.loadTexts:
    rlQosClassMapCounterTable.setStatus("current")
_RlQosClassMapCounterEntry_Object = MibTableRow
rlQosClassMapCounterEntry = _RlQosClassMapCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 47, 1)
)
rlQosClassMapCounterEntry.setIndexNames(
    (0, "CISCOSB-QOS-CLI-MIB", "rlQosClassMapIndex"),
)
if mibBuilder.loadTexts:
    rlQosClassMapCounterEntry.setStatus("current")
_RlQosClassMapCounterValue_Type = Counter64
_RlQosClassMapCounterValue_Object = MibTableColumn
rlQosClassMapCounterValue = _RlQosClassMapCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 47, 1, 2),
    _RlQosClassMapCounterValue_Type()
)
rlQosClassMapCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosClassMapCounterValue.setStatus("current")
_RlQosApplicationTrapIdTable_Object = MibTable
rlQosApplicationTrapIdTable = _RlQosApplicationTrapIdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 48)
)
if mibBuilder.loadTexts:
    rlQosApplicationTrapIdTable.setStatus("current")
_RlQosApplicationTrapIdEntry_Object = MibTableRow
rlQosApplicationTrapIdEntry = _RlQosApplicationTrapIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 48, 1)
)
rlQosApplicationTrapIdEntry.setIndexNames(
    (1, "CISCOSB-QOS-CLI-MIB", "rlQosApplicationName"),
)
if mibBuilder.loadTexts:
    rlQosApplicationTrapIdEntry.setStatus("current")


class _RlQosApplicationName_Type(DisplayString):
    """Custom type rlQosApplicationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlQosApplicationName_Type.__name__ = "DisplayString"
_RlQosApplicationName_Object = MibTableColumn
rlQosApplicationName = _RlQosApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 48, 1, 1),
    _RlQosApplicationName_Type()
)
rlQosApplicationName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlQosApplicationName.setStatus("current")
_RlQosApplicationTrapId_Type = Integer32
_RlQosApplicationTrapId_Object = MibTableColumn
rlQosApplicationTrapId = _RlQosApplicationTrapId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 48, 1, 2),
    _RlQosApplicationTrapId_Type()
)
rlQosApplicationTrapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlQosApplicationTrapId.setStatus("current")
_RlQoSApplicationDefaultAction_Type = RlQosApplicationDefaultActionType
_RlQoSApplicationDefaultAction_Object = MibScalar
rlQoSApplicationDefaultAction = _RlQoSApplicationDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 88, 49),
    _RlQoSApplicationDefaultAction_Type()
)
rlQoSApplicationDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlQoSApplicationDefaultAction.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-QOS-CLI-MIB",
    **{"ClassOffsetType": ClassOffsetType,
       "ClassTupleType": ClassTupleType,
       "AceActionType": AceActionType,
       "AceObjectType": AceObjectType,
       "AclObjectType": AclObjectType,
       "ClassMapType": ClassMapType,
       "ClassMapAction": ClassMapAction,
       "MarkVlanAction": MarkVlanAction,
       "RedirectAction": RedirectAction,
       "PolicerType": PolicerType,
       "PolicerAction": PolicerAction,
       "QosGlobalMode": QosGlobalMode,
       "QosTrustMode": QosTrustMode,
       "BinaryStatus": BinaryStatus,
       "QueueType": QueueType,
       "AclDefaultAction": AclDefaultAction,
       "InterfaceType": InterfaceType,
       "StatisticsCntrNumOfBitsType": StatisticsCntrNumOfBitsType,
       "StatisticsCntrType": StatisticsCntrType,
       "RlQosTimeBasedAclWeekPeriodicList": RlQosTimeBasedAclWeekPeriodicList,
       "RlQosAceTidxActionDropType": RlQosAceTidxActionDropType,
       "RlQosApplicationDefaultActionType": RlQosApplicationDefaultActionType,
       "rlQosCliMib": rlQosCliMib,
       "rlQosCliQosMode": rlQosCliQosMode,
       "rlQosCliBasicModeCfg": rlQosCliBasicModeCfg,
       "rlQosMaxNumOfAce": rlQosMaxNumOfAce,
       "rlQosOffsetTable": rlQosOffsetTable,
       "rlQosOffsetEntry": rlQosOffsetEntry,
       "rlQosOffsetIndex": rlQosOffsetIndex,
       "rlQosOffsetType": rlQosOffsetType,
       "rlQosOffsetValue": rlQosOffsetValue,
       "rlQosOffsetMask": rlQosOffsetMask,
       "rlQosOffsetPattern": rlQosOffsetPattern,
       "rlQosOffsetTuplePointer": rlQosOffsetTuplePointer,
       "rlQosOffsetStatus": rlQosOffsetStatus,
       "rlQosTupleTable": rlQosTupleTable,
       "rlQosTupleEntry": rlQosTupleEntry,
       "rlQosTupleIndex": rlQosTupleIndex,
       "rlQosTupleType": rlQosTupleType,
       "rlQosTupleValue1": rlQosTupleValue1,
       "rlQosTupleValue2": rlQosTupleValue2,
       "rlQosTupleStatus": rlQosTupleStatus,
       "rlQosAceTable": rlQosAceTable,
       "rlQosAceEntry": rlQosAceEntry,
       "rlQosAceIndex": rlQosAceIndex,
       "rlQosAceAction": rlQosAceAction,
       "rlQosAceType": rlQosAceType,
       "rlQosAceTuple1": rlQosAceTuple1,
       "rlQosAceTuple2": rlQosAceTuple2,
       "rlQosAceTuple3": rlQosAceTuple3,
       "rlQosAceTuple4": rlQosAceTuple4,
       "rlQosAceTuple5": rlQosAceTuple5,
       "rlQosAceTuple6": rlQosAceTuple6,
       "rlQosAceTuple7": rlQosAceTuple7,
       "rlQosAceTuple8": rlQosAceTuple8,
       "rlQosAceAccount": rlQosAceAccount,
       "rlQosAceStatus": rlQosAceStatus,
       "rlQosAclTable": rlQosAclTable,
       "rlQosAclEntry": rlQosAclEntry,
       "rlQosAclIndex": rlQosAclIndex,
       "rlQosAclName": rlQosAclName,
       "rlQosAclType": rlQosAclType,
       "rlQosAclStatus": rlQosAclStatus,
       "rlQosAclNumOfAces": rlQosAclNumOfAces,
       "rlQosAclAceRefTable": rlQosAclAceRefTable,
       "rlQosAclAceRefEntry": rlQosAclAceRefEntry,
       "rlQosAclAceRefAcePointer": rlQosAclAceRefAcePointer,
       "rlQosAclAceRefAclPointer": rlQosAclAceRefAclPointer,
       "rlQosAclAceRefStatus": rlQosAclAceRefStatus,
       "rlQosClassMapTable": rlQosClassMapTable,
       "rlQosClassMapEntry": rlQosClassMapEntry,
       "rlQosClassMapIndex": rlQosClassMapIndex,
       "rlQosClassMapName": rlQosClassMapName,
       "rlQosClassMapType": rlQosClassMapType,
       "rlQosClassMapAction": rlQosClassMapAction,
       "rlQosClassMapMarkValue": rlQosClassMapMarkValue,
       "rlQosClassMapPolicer": rlQosClassMapPolicer,
       "rlQosClassMapMatch1": rlQosClassMapMatch1,
       "rlQosClassMapMatch2": rlQosClassMapMatch2,
       "rlQosClassMapMarkVlan": rlQosClassMapMarkVlan,
       "rlQosClassMapNewVlan": rlQosClassMapNewVlan,
       "rlQosClassMapRedirectAction": rlQosClassMapRedirectAction,
       "rlQosClassMapDestInterface": rlQosClassMapDestInterface,
       "rlQosClassMapStatus": rlQosClassMapStatus,
       "rlQosClassMapMatch3": rlQosClassMapMatch3,
       "rlQosClassMapTrapId": rlQosClassMapTrapId,
       "rlQosClassMapCounterEnable": rlQosClassMapCounterEnable,
       "rlQosClassMapTunnelIdx": rlQosClassMapTunnelIdx,
       "rlQosPolicerTable": rlQosPolicerTable,
       "rlQosPolicerEntry": rlQosPolicerEntry,
       "rlQosPolicerIndex": rlQosPolicerIndex,
       "rlQosPolicerName": rlQosPolicerName,
       "rlQosPolicerType": rlQosPolicerType,
       "rlQosPolicerCir": rlQosPolicerCir,
       "rlQosPolicerCbs": rlQosPolicerCbs,
       "rlQosPolicerAction": rlQosPolicerAction,
       "rlQosPolicerCasPointerRemVal": rlQosPolicerCasPointerRemVal,
       "rlQosPolicerStatus": rlQosPolicerStatus,
       "rlQosPolicyMapTable": rlQosPolicyMapTable,
       "rlQosPolicyMapEntry": rlQosPolicyMapEntry,
       "rlQosPolicyMapIndex": rlQosPolicyMapIndex,
       "rlQosPolicyMapName": rlQosPolicyMapName,
       "rlQosPolicyMapStatus": rlQosPolicyMapStatus,
       "rlQosPolicyClassRefTable": rlQosPolicyClassRefTable,
       "rlQosPolicyClassRefEntry": rlQosPolicyClassRefEntry,
       "rlQosPolicyClassRefClassPointer": rlQosPolicyClassRefClassPointer,
       "rlQosPolicyClassRefPolicyPointer": rlQosPolicyClassRefPolicyPointer,
       "rlQosPolicyClassRefStatus": rlQosPolicyClassRefStatus,
       "rlQosIfPolicyTable": rlQosIfPolicyTable,
       "rlQosIfPolicyEntry": rlQosIfPolicyEntry,
       "rlIfIndex": rlIfIndex,
       "rlIfType": rlIfType,
       "rlQosIfPolicyMapPointerIn": rlQosIfPolicyMapPointerIn,
       "rlQosIfPolicyMapPointerOut": rlQosIfPolicyMapPointerOut,
       "rlQosIfTrustActive": rlQosIfTrustActive,
       "rlQosPortShaperStatus": rlQosPortShaperStatus,
       "rlQosCirPortShaper": rlQosCirPortShaper,
       "rlQosCbsPortShaper": rlQosCbsPortShaper,
       "rlQosIfProfilePointer": rlQosIfProfilePointer,
       "rlQosQueueProfilePointer": rlQosQueueProfilePointer,
       "rlQosQueueShapeProfilePointer": rlQosQueueShapeProfilePointer,
       "rlQosAclDefaultAction": rlQosAclDefaultAction,
       "rlQosIfPolicyMapStatus": rlQosIfPolicyMapStatus,
       "rlQosIfAclIn": rlQosIfAclIn,
       "rlQosIfAclOut": rlQosIfAclOut,
       "rlQosIfPolicerIn": rlQosIfPolicerIn,
       "rlQosPortRateLimitStatus": rlQosPortRateLimitStatus,
       "rlQosCirPortRateLimit": rlQosCirPortRateLimit,
       "rlQosCbsPortRateLimit": rlQosCbsPortRateLimit,
       "rlQosIfIpv6AclIn": rlQosIfIpv6AclIn,
       "rlQosIfIpv6AclOut": rlQosIfIpv6AclOut,
       "rlQosIfProfileCfgTable": rlQosIfProfileCfgTable,
       "rlQosIfProfileCfgEntry": rlQosIfProfileCfgEntry,
       "rlIfProfileName": rlIfProfileName,
       "rlQosQueueId": rlQosQueueId,
       "rlQosTdThersholdDp0": rlQosTdThersholdDp0,
       "rlQosTdThersholdDp1": rlQosTdThersholdDp1,
       "rlQosTdThersholdDp2": rlQosTdThersholdDp2,
       "rlQosRedMinDp0": rlQosRedMinDp0,
       "rlQosRedMaxDp0": rlQosRedMaxDp0,
       "rlQosRedProbDp0": rlQosRedProbDp0,
       "rlQosRedMinDp1": rlQosRedMinDp1,
       "rlQosRedMaxDp1": rlQosRedMaxDp1,
       "rlQosRedProbDp1": rlQosRedProbDp1,
       "rlQosRedMinDp2": rlQosRedMinDp2,
       "rlQosRedMaxDp2": rlQosRedMaxDp2,
       "rlQosRedProbDp2": rlQosRedProbDp2,
       "rlQosRedQweight": rlQosRedQweight,
       "rlQosIfprofileStatus": rlQosIfprofileStatus,
       "rlQosDscpMutationTable": rlQosDscpMutationTable,
       "rlQosDscpMutationEntry": rlQosDscpMutationEntry,
       "rlQosOldDscp": rlQosOldDscp,
       "rlQosNewDscp": rlQosNewDscp,
       "rlQosDscpRemarkTable": rlQosDscpRemarkTable,
       "rlQosDscpRemarkEntry": rlQosDscpRemarkEntry,
       "rlQosRmOldDscp": rlQosRmOldDscp,
       "rlQosRmNewDscp": rlQosRmNewDscp,
       "rlQosCosQueueTable": rlQosCosQueueTable,
       "rlQosCosQueueEntry": rlQosCosQueueEntry,
       "rlQosCosIndex": rlQosCosIndex,
       "rlQosCosQueueId": rlQosCosQueueId,
       "rlQosDscpQueueTable": rlQosDscpQueueTable,
       "rlQosDscpQueueEntry": rlQosDscpQueueEntry,
       "rlQosDscpIndex": rlQosDscpIndex,
       "rlQosQueueNum": rlQosQueueNum,
       "rlQosTcpPortQueueTable": rlQosTcpPortQueueTable,
       "rlQosTcpPortQueueEntry": rlQosTcpPortQueueEntry,
       "rlQosTcpPort": rlQosTcpPort,
       "rlQosTcpQueueValue": rlQosTcpQueueValue,
       "rlQosTcpPortQueueStatus": rlQosTcpPortQueueStatus,
       "rlQosUdpPortQueueTable": rlQosUdpPortQueueTable,
       "rlQosUdpPortQueueEntry": rlQosUdpPortQueueEntry,
       "rlQosUdpPort": rlQosUdpPort,
       "rlQosUdpQueueValue": rlQosUdpQueueValue,
       "rlQosUdpPortQueueStatus": rlQosUdpPortQueueStatus,
       "rlQosEfManageTable": rlQosEfManageTable,
       "rlQosEfManageEntry": rlQosEfManageEntry,
       "rlQosEfQueueId": rlQosEfQueueId,
       "rlQosEfState": rlQosEfState,
       "rlQosEfPriority": rlQosEfPriority,
       "rlQosQueueProfileTable": rlQosQueueProfileTable,
       "rlQosQueueProfileEntry": rlQosQueueProfileEntry,
       "rlQueueProfileName": rlQueueProfileName,
       "rlQosTypeQueue1": rlQosTypeQueue1,
       "rlQosValueQueue1": rlQosValueQueue1,
       "rlQosTypeQueue2": rlQosTypeQueue2,
       "rlQosValueQueue2": rlQosValueQueue2,
       "rlQosTypeQueue3": rlQosTypeQueue3,
       "rlQosValueQueue3": rlQosValueQueue3,
       "rlQosTypeQueue4": rlQosTypeQueue4,
       "rlQosValueQueue4": rlQosValueQueue4,
       "rlQosTypeQueue5": rlQosTypeQueue5,
       "rlQosValueQueue5": rlQosValueQueue5,
       "rlQosTypeQueue6": rlQosTypeQueue6,
       "rlQosValueQueue6": rlQosValueQueue6,
       "rlQosTypeQueue7": rlQosTypeQueue7,
       "rlQosValueQueue7": rlQosValueQueue7,
       "rlQosTypeQueue8": rlQosTypeQueue8,
       "rlQosValueQueue8": rlQosValueQueue8,
       "rlQosQueueProfileStatus": rlQosQueueProfileStatus,
       "rlQosNumOfIfConnections": rlQosNumOfIfConnections,
       "rlQosQueueShapeProfileTable": rlQosQueueShapeProfileTable,
       "rlQosQueueShapeProfileEntry": rlQosQueueShapeProfileEntry,
       "rlQosQueueShapeIndex": rlQosQueueShapeIndex,
       "rlQosCirQueue1": rlQosCirQueue1,
       "rlQosCbsQueue1": rlQosCbsQueue1,
       "rlQosCirQueue2": rlQosCirQueue2,
       "rlQosCbsQueue2": rlQosCbsQueue2,
       "rlQosCirQueue3": rlQosCirQueue3,
       "rlQosCbsQueue3": rlQosCbsQueue3,
       "rlQosCirQueue4": rlQosCirQueue4,
       "rlQosCbsQueue4": rlQosCbsQueue4,
       "rlQosCirQueue5": rlQosCirQueue5,
       "rlQosCbsQueue5": rlQosCbsQueue5,
       "rlQosCirQueue6": rlQosCirQueue6,
       "rlQosCbsQueue6": rlQosCbsQueue6,
       "rlQosCirQueue7": rlQosCirQueue7,
       "rlQosCbsQueue7": rlQosCbsQueue7,
       "rlQosCirQueue8": rlQosCirQueue8,
       "rlQosCbsQueue8": rlQosCbsQueue8,
       "rlQosQueueShapeProfileStatus": rlQosQueueShapeProfileStatus,
       "rlQosAclCounterTable": rlQosAclCounterTable,
       "rlQosAclCounterEntry": rlQosAclCounterEntry,
       "rlQosAclCounterInterface": rlQosAclCounterInterface,
       "rlQosAclCounterAclIndex": rlQosAclCounterAclIndex,
       "rlQosAclCounterAceIndex": rlQosAclCounterAceIndex,
       "rlQosAclCounterValue": rlQosAclCounterValue,
       "rlQosFreeIndexesTable": rlQosFreeIndexesTable,
       "rlQosFreeIndexesEntry": rlQosFreeIndexesEntry,
       "rlQosFreeIndexesTableId": rlQosFreeIndexesTableId,
       "rlQosFreeIndexesValue": rlQosFreeIndexesValue,
       "rlQosNamesToIndexesTable": rlQosNamesToIndexesTable,
       "rlQosNamesToIndexesEntry": rlQosNamesToIndexesEntry,
       "rlQosNamesToIndexesTableId": rlQosNamesToIndexesTableId,
       "rlQosNamesToIndexesName": rlQosNamesToIndexesName,
       "rlQosNamesToIndexesValue": rlQosNamesToIndexesValue,
       "rlQosStackControlQueue": rlQosStackControlQueue,
       "rlQosStackControlCos": rlQosStackControlCos,
       "rlQosCosQueueDefaultMapTable": rlQosCosQueueDefaultMapTable,
       "rlQosCosQueueDefaultMapEntry": rlQosCosQueueDefaultMapEntry,
       "rlQosCosQueueDefaultMapVpt": rlQosCosQueueDefaultMapVpt,
       "rlQosCosQueueDefaultMapQueueId": rlQosCosQueueDefaultMapQueueId,
       "rlQosPredefBlockAclTable": rlQosPredefBlockAclTable,
       "rlQosPredefBlockAclEntry": rlQosPredefBlockAclEntry,
       "rlQosPredefBlockAclIfIndex": rlQosPredefBlockAclIfIndex,
       "rlQosPredefBlockAclIfType": rlQosPredefBlockAclIfType,
       "rlQosPredefBlockAclMask": rlQosPredefBlockAclMask,
       "rlQosPredefBlockAclStatus": rlQosPredefBlockAclStatus,
       "rlQosAceTidxTable": rlQosAceTidxTable,
       "rlQosAceTidxEntry": rlQosAceTidxEntry,
       "rlQosAceTidxAclIndex": rlQosAceTidxAclIndex,
       "rlQosAceTidxIndex": rlQosAceTidxIndex,
       "rlQosAceTidxAction": rlQosAceTidxAction,
       "rlQosAceTidxType": rlQosAceTidxType,
       "rlQosAceTidxTuple1": rlQosAceTidxTuple1,
       "rlQosAceTidxTuple2": rlQosAceTidxTuple2,
       "rlQosAceTidxTuple3": rlQosAceTidxTuple3,
       "rlQosAceTidxTuple4": rlQosAceTidxTuple4,
       "rlQosAceTidxTuple5": rlQosAceTidxTuple5,
       "rlQosAceTidxTuple6": rlQosAceTidxTuple6,
       "rlQosAceTidxTuple7": rlQosAceTidxTuple7,
       "rlQosAceTidxTuple8": rlQosAceTidxTuple8,
       "rlQosAceTidxAccount": rlQosAceTidxAccount,
       "rlQosAceTidxStatus": rlQosAceTidxStatus,
       "rlQosAceTidxTimeRange": rlQosAceTidxTimeRange,
       "rlQosAceTidxTimeRangeIsActive": rlQosAceTidxTimeRangeIsActive,
       "rlQosAceTidxTuple9": rlQosAceTidxTuple9,
       "rlQosAceTidxTuple10": rlQosAceTidxTuple10,
       "rlQosAceTidxTuple11": rlQosAceTidxTuple11,
       "rlQosAceTidxActionDropType": rlQosAceTidxActionDropType,
       "rlQosMibVersion": rlQosMibVersion,
       "rlQosDscpQueueDefaultMapTable": rlQosDscpQueueDefaultMapTable,
       "rlQosDscpQueueDefaultMapEntry": rlQosDscpQueueDefaultMapEntry,
       "rlQosDscpQueueDefaultMapDscp": rlQosDscpQueueDefaultMapDscp,
       "rlQosDscpQueueDefaultMapQueueId": rlQosDscpQueueDefaultMapQueueId,
       "rlQosDscpToDpTable": rlQosDscpToDpTable,
       "rlQosDscpToDpEntry": rlQosDscpToDpEntry,
       "rlQosDscp": rlQosDscp,
       "rlQosDp": rlQosDp,
       "rlQosStatistics": rlQosStatistics,
       "rlQosPortPolicyStatisticsTable": rlQosPortPolicyStatisticsTable,
       "rlQosPortPolicyStatisticsEntry": rlQosPortPolicyStatisticsEntry,
       "rlQosPortPolicyStatisticsCntrType": rlQosPortPolicyStatisticsCntrType,
       "rlQosPortPolicyStatisticsCntrNumOfBits": rlQosPortPolicyStatisticsCntrNumOfBits,
       "rlQosPortPolicyStatisticsEnableCounting": rlQosPortPolicyStatisticsEnableCounting,
       "rlQosPortPolicyStatisticsCounterValue": rlQosPortPolicyStatisticsCounterValue,
       "rlQosSinglePolicerStatisticsTable": rlQosSinglePolicerStatisticsTable,
       "rlQosSinglePolicerStatisticsEntry": rlQosSinglePolicerStatisticsEntry,
       "rlQosSinglePolicerStatisticsInProfileCounterValue": rlQosSinglePolicerStatisticsInProfileCounterValue,
       "rlQosSinglePolicerStatisticsInProfileCntrNumOfBits": rlQosSinglePolicerStatisticsInProfileCntrNumOfBits,
       "rlQosSinglePolicerStatisticsOutProfileCounterValue": rlQosSinglePolicerStatisticsOutProfileCounterValue,
       "rlQosSinglePolicerStatisticsOutProfileCntrNumOfBits": rlQosSinglePolicerStatisticsOutProfileCntrNumOfBits,
       "rlQosSinglePolicerStatisticsStatus": rlQosSinglePolicerStatisticsStatus,
       "rlQosAggregatePolicerStatisticsTable": rlQosAggregatePolicerStatisticsTable,
       "rlQosAggregatePolicerStatisticsEntry": rlQosAggregatePolicerStatisticsEntry,
       "rlQosAggregatePolicerStatisticsInProfileCounterValue": rlQosAggregatePolicerStatisticsInProfileCounterValue,
       "rlQosAggregatePolicerStatisticsInProfileCntrNumOfBits": rlQosAggregatePolicerStatisticsInProfileCntrNumOfBits,
       "rlQosAggregatePolicerStatisticsOutProfileCounterValue": rlQosAggregatePolicerStatisticsOutProfileCounterValue,
       "rlQosAggregatePolicerStatisticsOutProfileCntrNumOfBits": rlQosAggregatePolicerStatisticsOutProfileCntrNumOfBits,
       "rlQosAggregatePolicerStatisticsStatus": rlQosAggregatePolicerStatisticsStatus,
       "rlQosOutQueueStatisticsTable": rlQosOutQueueStatisticsTable,
       "rlQosOutQueueStatisticsEntry": rlQosOutQueueStatisticsEntry,
       "rlQosOutQueueStatisticsCountrID": rlQosOutQueueStatisticsCountrID,
       "rlQosOutQueueStatisticsIfIndexList": rlQosOutQueueStatisticsIfIndexList,
       "rlQosOutQueueStatisticsPortAll": rlQosOutQueueStatisticsPortAll,
       "rlQosOutQueueStatisticsVlan": rlQosOutQueueStatisticsVlan,
       "rlQosOutQueueStatisticsVlanAll": rlQosOutQueueStatisticsVlanAll,
       "rlQosOutQueueStatisticsQueue": rlQosOutQueueStatisticsQueue,
       "rlQosOutQueueStatisticsQueueAll": rlQosOutQueueStatisticsQueueAll,
       "rlQosOutQueueStatisticsDP": rlQosOutQueueStatisticsDP,
       "rlQosOutQueueStatisticsDPAll": rlQosOutQueueStatisticsDPAll,
       "rlQosOutQueueStatisticsCounterTailDropValue": rlQosOutQueueStatisticsCounterTailDropValue,
       "rlQosOutQueueStatisticsCounterAllValue": rlQosOutQueueStatisticsCounterAllValue,
       "rlQosOutQueueStatisticsCntrNumOfBits": rlQosOutQueueStatisticsCntrNumOfBits,
       "rlQosOutQueueStatisticsStatus": rlQosOutQueueStatisticsStatus,
       "rlQosGlobalStatisticsCntrsTable": rlQosGlobalStatisticsCntrsTable,
       "rlQosGlobalStatisticsCntrsEntry": rlQosGlobalStatisticsCntrsEntry,
       "rlQosGlobalStatisticsCntrsType": rlQosGlobalStatisticsCntrsType,
       "rlQosGlobalStatisticsCntrsNumOfBits": rlQosGlobalStatisticsCntrsNumOfBits,
       "rlQosGlobalStatisticsCntrsCounterValue": rlQosGlobalStatisticsCntrsCounterValue,
       "rlQosGlobalStatisticsStatus": rlQosGlobalStatisticsStatus,
       "rlQosClearCounters": rlQosClearCounters,
       "rlQosClassifierUtilization": rlQosClassifierUtilization,
       "rlQosClassifierUtilizationTable": rlQosClassifierUtilizationTable,
       "rlQosClassifierUtilizationEntry": rlQosClassifierUtilizationEntry,
       "rlQosClassifierUtilizationUnitId": rlQosClassifierUtilizationUnitId,
       "rlQosClassifierUtilizationPercent": rlQosClassifierUtilizationPercent,
       "rlQosClassifierUtilizationRulesNumber": rlQosClassifierUtilizationRulesNumber,
       "rlQosClassifierUtilizationFreeRulesNumber": rlQosClassifierUtilizationFreeRulesNumber,
       "rlQosClassifierUtilizationSystem": rlQosClassifierUtilizationSystem,
       "rlQosClassifierRulesNumberUtilizationSystem": rlQosClassifierRulesNumberUtilizationSystem,
       "rlQosPortToProfileMappingTable": rlQosPortToProfileMappingTable,
       "rlQosPortToProfileMappingEntry": rlQosPortToProfileMappingEntry,
       "rlQosPort": rlQosPort,
       "rlQosProfileName": rlQosProfileName,
       "rlQosCPUSafeGuardEnable": rlQosCPUSafeGuardEnable,
       "rlQosPolicyClassPriorityRefTable": rlQosPolicyClassPriorityRefTable,
       "rlQosPolicyClassPriorityRefEntry": rlQosPolicyClassPriorityRefEntry,
       "rlQosPolicyClassPriorityRefPriority": rlQosPolicyClassPriorityRefPriority,
       "rlQosPolicyClassPriorityRefClassPointer": rlQosPolicyClassPriorityRefClassPointer,
       "rlQosPolicyClassPriorityRefPolicyPointer": rlQosPolicyClassPriorityRefPolicyPointer,
       "rlQosPolicyClassPriorityRefStatus": rlQosPolicyClassPriorityRefStatus,
       "rlQosDenyAceStatisticsTable": rlQosDenyAceStatisticsTable,
       "rlQosDenyAceStatisticsEntry": rlQosDenyAceStatisticsEntry,
       "rlQosDenyAceStatisticsIfIndex": rlQosDenyAceStatisticsIfIndex,
       "rlQosDenyAceStatisticsIfCounter": rlQosDenyAceStatisticsIfCounter,
       "rlQosDenyAceStatisticsOtherFlowCounter": rlQosDenyAceStatisticsOtherFlowCounter,
       "rlQosDenyAceStatisticsClearIfCounters": rlQosDenyAceStatisticsClearIfCounters,
       "rlQosDenyAceStatisticsClearOtherFlowCounter": rlQosDenyAceStatisticsClearOtherFlowCounter,
       "rlQosModeGlobalCfgTable": rlQosModeGlobalCfgTable,
       "rlQosModeGlobalCfgEntry": rlQosModeGlobalCfgEntry,
       "rlQosGlobalIndex": rlQosGlobalIndex,
       "rlQosGlobalQoSMode": rlQosGlobalQoSMode,
       "rlQosBasicGlobalTrustMode": rlQosBasicGlobalTrustMode,
       "rlQosAdvcGlobalTrustMode": rlQosAdvcGlobalTrustMode,
       "rlQoSPortTrustAdvancedMode": rlQoSPortTrustAdvancedMode,
       "rlQosDscpMutationEnable": rlQosDscpMutationEnable,
       "rlQosModeGlobalCfgStatus": rlQosModeGlobalCfgStatus,
       "rlQosClassMapCounterTable": rlQosClassMapCounterTable,
       "rlQosClassMapCounterEntry": rlQosClassMapCounterEntry,
       "rlQosClassMapCounterValue": rlQosClassMapCounterValue,
       "rlQosApplicationTrapIdTable": rlQosApplicationTrapIdTable,
       "rlQosApplicationTrapIdEntry": rlQosApplicationTrapIdEntry,
       "rlQosApplicationName": rlQosApplicationName,
       "rlQosApplicationTrapId": rlQosApplicationTrapId,
       "rlQoSApplicationDefaultAction": rlQoSApplicationDefaultAction}
)
