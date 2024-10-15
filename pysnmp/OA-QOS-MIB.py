# SNMP MIB module (OA-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OA-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:30 2024
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

(oacExpIMIp,) = mibBuilder.importSymbols(
    "ONEACCESS-GLOBAL-REG",
    "oacExpIMIp")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

oacQOS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class QosObjectType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("classmap", 2),
          ("matchStatement", 3),
          ("police", 7),
          ("policymap", 1),
          ("queueing", 4),
          ("randomDetect", 5),
          ("set", 8))
    )



class TrafficDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )



class QosClassInfo(Integer32, TextualConvention):
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
        *(("matchAll", 2),
          ("matchAny", 3),
          ("none", 1))
    )



class QosMatchInfo(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("matchNot", 2),
          ("none", 1))
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
        *(("mainInterface", 1),
          ("subInterface", 2))
    )



class QueueingBandwidthUnits(Integer32, TextualConvention):
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
        *(("kbps", 1),
          ("percentage", 2),
          ("percentageRemaining", 3))
    )



class PoliceAction(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("drop", 5),
          ("setAtmClp", 6),
          ("setDiscardClass", 7),
          ("setIpDSCP", 2),
          ("setIpPrecedence", 3),
          ("setQosGroup", 4),
          ("transmit", 1))
    )



class SetFeatureType(Bits, TextualConvention):
    status = "current"


class WREDMechanism(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dscp", 2),
          ("precedence", 1))
    )



class QosQueueUnitType(Integer32, TextualConvention):
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
        *(("bytes", 3),
          ("cells", 2),
          ("packets", 1))
    )



class QosQueueDepth(Gauge32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_OacQosServicePolicyTable_Object = MibTable
oacQosServicePolicyTable = _OacQosServicePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    oacQosServicePolicyTable.setStatus("current")
_OacQosServicePolicyEntry_Object = MibTableRow
oacQosServicePolicyEntry = _OacQosServicePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 1, 1)
)
oacQosServicePolicyEntry.setIndexNames(
    (0, "OA-QOS-MIB", "oacQosPolicyIndex"),
)
if mibBuilder.loadTexts:
    oacQosServicePolicyEntry.setStatus("current")
_OacQosPolicyIndex_Type = Gauge32
_OacQosPolicyIndex_Object = MibTableColumn
oacQosPolicyIndex = _OacQosPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 1, 1, 1),
    _OacQosPolicyIndex_Type()
)
oacQosPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacQosPolicyIndex.setStatus("current")
_OacQosIfIndex_Type = InterfaceIndex
_OacQosIfIndex_Object = MibTableColumn
oacQosIfIndex = _OacQosIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 1, 1, 2),
    _OacQosIfIndex_Type()
)
oacQosIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosIfIndex.setStatus("current")
_OacQosIfType_Type = InterfaceType
_OacQosIfType_Object = MibTableColumn
oacQosIfType = _OacQosIfType_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 1, 1, 3),
    _OacQosIfType_Type()
)
oacQosIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosIfType.setStatus("current")
_OacQosPolicyDirection_Type = TrafficDirection
_OacQosPolicyDirection_Object = MibTableColumn
oacQosPolicyDirection = _OacQosPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 1, 1, 4),
    _OacQosPolicyDirection_Type()
)
oacQosPolicyDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPolicyDirection.setStatus("current")
_OacQosInterfacePolicyTable_Object = MibTable
oacQosInterfacePolicyTable = _OacQosInterfacePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    oacQosInterfacePolicyTable.setStatus("current")
_OacQosInterfacePolicyEntry_Object = MibTableRow
oacQosInterfacePolicyEntry = _OacQosInterfacePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 2, 1)
)
oacQosInterfacePolicyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "OA-QOS-MIB", "oacQosPolicyDirection"),
)
if mibBuilder.loadTexts:
    oacQosInterfacePolicyEntry.setStatus("current")
_OacQosInterfacePolicyIndex_Type = Gauge32
_OacQosInterfacePolicyIndex_Object = MibTableColumn
oacQosInterfacePolicyIndex = _OacQosInterfacePolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 2, 1, 1),
    _OacQosInterfacePolicyIndex_Type()
)
oacQosInterfacePolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosInterfacePolicyIndex.setStatus("current")
_OacQosObjectsTable_Object = MibTable
oacQosObjectsTable = _OacQosObjectsTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    oacQosObjectsTable.setStatus("current")
_OacQosObjectsEntry_Object = MibTableRow
oacQosObjectsEntry = _OacQosObjectsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 3, 1)
)
oacQosObjectsEntry.setIndexNames(
    (0, "OA-QOS-MIB", "oacQosPolicyIndex"),
    (0, "OA-QOS-MIB", "oacQosObjectsIndex"),
)
if mibBuilder.loadTexts:
    oacQosObjectsEntry.setStatus("current")
_OacQosObjectsIndex_Type = Gauge32
_OacQosObjectsIndex_Object = MibTableColumn
oacQosObjectsIndex = _OacQosObjectsIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 3, 1, 1),
    _OacQosObjectsIndex_Type()
)
oacQosObjectsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacQosObjectsIndex.setStatus("current")
_OacQosConfigIndex_Type = Gauge32
_OacQosConfigIndex_Object = MibTableColumn
oacQosConfigIndex = _OacQosConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 3, 1, 2),
    _OacQosConfigIndex_Type()
)
oacQosConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosConfigIndex.setStatus("current")
_OacQosObjectsType_Type = QosObjectType
_OacQosObjectsType_Object = MibTableColumn
oacQosObjectsType = _OacQosObjectsType_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 3, 1, 3),
    _OacQosObjectsType_Type()
)
oacQosObjectsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosObjectsType.setStatus("current")
_OacQosParentObjectsIndex_Type = Gauge32
_OacQosParentObjectsIndex_Object = MibTableColumn
oacQosParentObjectsIndex = _OacQosParentObjectsIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 3, 1, 4),
    _OacQosParentObjectsIndex_Type()
)
oacQosParentObjectsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosParentObjectsIndex.setStatus("current")
_OacQosPolicyMapConfigTable_Object = MibTable
oacQosPolicyMapConfigTable = _OacQosPolicyMapConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 4)
)
if mibBuilder.loadTexts:
    oacQosPolicyMapConfigTable.setStatus("current")
_OacQosPolicyMapConfigEntry_Object = MibTableRow
oacQosPolicyMapConfigEntry = _OacQosPolicyMapConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 4, 1)
)
oacQosPolicyMapConfigEntry.setIndexNames(
    (0, "OA-QOS-MIB", "oacQosConfigIndex"),
)
if mibBuilder.loadTexts:
    oacQosPolicyMapConfigEntry.setStatus("current")
_OacQosPolicyMapName_Type = DisplayString
_OacQosPolicyMapName_Object = MibTableColumn
oacQosPolicyMapName = _OacQosPolicyMapName_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 4, 1, 1),
    _OacQosPolicyMapName_Type()
)
oacQosPolicyMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPolicyMapName.setStatus("current")
_OacQosClassMapConfigTable_Object = MibTable
oacQosClassMapConfigTable = _OacQosClassMapConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 5)
)
if mibBuilder.loadTexts:
    oacQosClassMapConfigTable.setStatus("current")
_OacQosClassMapConfigEntry_Object = MibTableRow
oacQosClassMapConfigEntry = _OacQosClassMapConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 5, 1)
)
oacQosClassMapConfigEntry.setIndexNames(
    (0, "OA-QOS-MIB", "oacQosConfigIndex"),
)
if mibBuilder.loadTexts:
    oacQosClassMapConfigEntry.setStatus("current")
_OacQosClassMapName_Type = DisplayString
_OacQosClassMapName_Object = MibTableColumn
oacQosClassMapName = _OacQosClassMapName_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 5, 1, 1),
    _OacQosClassMapName_Type()
)
oacQosClassMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosClassMapName.setStatus("current")
_OacQosClassMapInfo_Type = QosClassInfo
_OacQosClassMapInfo_Object = MibTableColumn
oacQosClassMapInfo = _OacQosClassMapInfo_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 5, 1, 2),
    _OacQosClassMapInfo_Type()
)
oacQosClassMapInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosClassMapInfo.setStatus("current")
_OacQosClassMapStatsTable_Object = MibTable
oacQosClassMapStatsTable = _OacQosClassMapStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 6)
)
if mibBuilder.loadTexts:
    oacQosClassMapStatsTable.setStatus("current")
_OacQosClassMapStatsEntry_Object = MibTableRow
oacQosClassMapStatsEntry = _OacQosClassMapStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 6, 1)
)
oacQosClassMapStatsEntry.setIndexNames(
    (0, "OA-QOS-MIB", "oacQosPolicyIndex"),
    (0, "OA-QOS-MIB", "oacQosObjectsIndex"),
)
if mibBuilder.loadTexts:
    oacQosClassMapStatsEntry.setStatus("current")
_OacQosClassMapPreExecutePkt_Type = Counter32
_OacQosClassMapPreExecutePkt_Object = MibTableColumn
oacQosClassMapPreExecutePkt = _OacQosClassMapPreExecutePkt_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 6, 1, 1),
    _OacQosClassMapPreExecutePkt_Type()
)
oacQosClassMapPreExecutePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosClassMapPreExecutePkt.setStatus("current")
_OacQosClassMapPreExecutePkt64_Type = Counter64
_OacQosClassMapPreExecutePkt64_Object = MibTableColumn
oacQosClassMapPreExecutePkt64 = _OacQosClassMapPreExecutePkt64_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 6, 1, 2),
    _OacQosClassMapPreExecutePkt64_Type()
)
oacQosClassMapPreExecutePkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosClassMapPreExecutePkt64.setStatus("current")
_OacQosClassMapPreExecuteByte_Type = Counter32
_OacQosClassMapPreExecuteByte_Object = MibTableColumn
oacQosClassMapPreExecuteByte = _OacQosClassMapPreExecuteByte_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 6, 1, 3),
    _OacQosClassMapPreExecuteByte_Type()
)
oacQosClassMapPreExecuteByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosClassMapPreExecuteByte.setStatus("current")
_OacQosClassMapPreExecuteByte64_Type = Counter64
_OacQosClassMapPreExecuteByte64_Object = MibTableColumn
oacQosClassMapPreExecuteByte64 = _OacQosClassMapPreExecuteByte64_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 6, 1, 4),
    _OacQosClassMapPreExecuteByte64_Type()
)
oacQosClassMapPreExecuteByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosClassMapPreExecuteByte64.setStatus("current")
_OacQosClassMapPreExecuteBitRate_Type = Gauge32
_OacQosClassMapPreExecuteBitRate_Object = MibTableColumn
oacQosClassMapPreExecuteBitRate = _OacQosClassMapPreExecuteBitRate_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 6, 1, 5),
    _OacQosClassMapPreExecuteBitRate_Type()
)
oacQosClassMapPreExecuteBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosClassMapPreExecuteBitRate.setStatus("current")
if mibBuilder.loadTexts:
    oacQosClassMapPreExecuteBitRate.setUnits("bits per second")
_OacQosClassMapPostExecuteByte_Type = Counter32
_OacQosClassMapPostExecuteByte_Object = MibTableColumn
oacQosClassMapPostExecuteByte = _OacQosClassMapPostExecuteByte_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 6, 1, 6),
    _OacQosClassMapPostExecuteByte_Type()
)
oacQosClassMapPostExecuteByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosClassMapPostExecuteByte.setStatus("current")
_OacQosClassMapPostExecuteByte64_Type = Counter64
_OacQosClassMapPostExecuteByte64_Object = MibTableColumn
oacQosClassMapPostExecuteByte64 = _OacQosClassMapPostExecuteByte64_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 6, 1, 7),
    _OacQosClassMapPostExecuteByte64_Type()
)
oacQosClassMapPostExecuteByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosClassMapPostExecuteByte64.setStatus("current")
_OacQosClassMapPostExecuteBitRate_Type = Gauge32
_OacQosClassMapPostExecuteBitRate_Object = MibTableColumn
oacQosClassMapPostExecuteBitRate = _OacQosClassMapPostExecuteBitRate_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 6, 1, 8),
    _OacQosClassMapPostExecuteBitRate_Type()
)
oacQosClassMapPostExecuteBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosClassMapPostExecuteBitRate.setStatus("current")
if mibBuilder.loadTexts:
    oacQosClassMapPostExecuteBitRate.setUnits("bits per second")
_OacQosClassMapDropPkt_Type = Counter32
_OacQosClassMapDropPkt_Object = MibTableColumn
oacQosClassMapDropPkt = _OacQosClassMapDropPkt_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 6, 1, 9),
    _OacQosClassMapDropPkt_Type()
)
oacQosClassMapDropPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosClassMapDropPkt.setStatus("current")
_OacQosClassMapDropPkt64_Type = Counter64
_OacQosClassMapDropPkt64_Object = MibTableColumn
oacQosClassMapDropPkt64 = _OacQosClassMapDropPkt64_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 6, 1, 10),
    _OacQosClassMapDropPkt64_Type()
)
oacQosClassMapDropPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosClassMapDropPkt64.setStatus("current")
_OacQosClassMapDropByte_Type = Counter32
_OacQosClassMapDropByte_Object = MibTableColumn
oacQosClassMapDropByte = _OacQosClassMapDropByte_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 6, 1, 11),
    _OacQosClassMapDropByte_Type()
)
oacQosClassMapDropByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosClassMapDropByte.setStatus("current")
_OacQosClassMapDropByte64_Type = Counter64
_OacQosClassMapDropByte64_Object = MibTableColumn
oacQosClassMapDropByte64 = _OacQosClassMapDropByte64_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 6, 1, 12),
    _OacQosClassMapDropByte64_Type()
)
oacQosClassMapDropByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosClassMapDropByte64.setStatus("current")
_OacQosClassMapDropBitRate_Type = Gauge32
_OacQosClassMapDropBitRate_Object = MibTableColumn
oacQosClassMapDropBitRate = _OacQosClassMapDropBitRate_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 6, 1, 13),
    _OacQosClassMapDropBitRate_Type()
)
oacQosClassMapDropBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosClassMapDropBitRate.setStatus("current")
if mibBuilder.loadTexts:
    oacQosClassMapDropBitRate.setUnits("bits per second")
_OacQosClassMapRemarkedPkt_Type = Counter32
_OacQosClassMapRemarkedPkt_Object = MibTableColumn
oacQosClassMapRemarkedPkt = _OacQosClassMapRemarkedPkt_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 6, 1, 14),
    _OacQosClassMapRemarkedPkt_Type()
)
oacQosClassMapRemarkedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosClassMapRemarkedPkt.setStatus("current")
_OacQosClassMapRemarkedPkt64_Type = Counter64
_OacQosClassMapRemarkedPkt64_Object = MibTableColumn
oacQosClassMapRemarkedPkt64 = _OacQosClassMapRemarkedPkt64_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 6, 1, 15),
    _OacQosClassMapRemarkedPkt64_Type()
)
oacQosClassMapRemarkedPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosClassMapRemarkedPkt64.setStatus("current")
_OacQosClassMapRemarkedByte_Type = Counter32
_OacQosClassMapRemarkedByte_Object = MibTableColumn
oacQosClassMapRemarkedByte = _OacQosClassMapRemarkedByte_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 6, 1, 16),
    _OacQosClassMapRemarkedByte_Type()
)
oacQosClassMapRemarkedByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosClassMapRemarkedByte.setStatus("current")
_OacQosClassMapRemarkedByte64_Type = Counter64
_OacQosClassMapRemarkedByte64_Object = MibTableColumn
oacQosClassMapRemarkedByte64 = _OacQosClassMapRemarkedByte64_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 6, 1, 17),
    _OacQosClassMapRemarkedByte64_Type()
)
oacQosClassMapRemarkedByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosClassMapRemarkedByte64.setStatus("current")
_OacQosMatchConfigTable_Object = MibTable
oacQosMatchConfigTable = _OacQosMatchConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 7)
)
if mibBuilder.loadTexts:
    oacQosMatchConfigTable.setStatus("current")
_OacQosMatchConfigEntry_Object = MibTableRow
oacQosMatchConfigEntry = _OacQosMatchConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 7, 1)
)
oacQosMatchConfigEntry.setIndexNames(
    (0, "OA-QOS-MIB", "oacQosConfigIndex"),
)
if mibBuilder.loadTexts:
    oacQosMatchConfigEntry.setStatus("current")
_OacQosMatchName_Type = DisplayString
_OacQosMatchName_Object = MibTableColumn
oacQosMatchName = _OacQosMatchName_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 7, 1, 1),
    _OacQosMatchName_Type()
)
oacQosMatchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosMatchName.setStatus("current")
_OacQosMatchInfo_Type = QosMatchInfo
_OacQosMatchInfo_Object = MibTableColumn
oacQosMatchInfo = _OacQosMatchInfo_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 7, 1, 2),
    _OacQosMatchInfo_Type()
)
oacQosMatchInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosMatchInfo.setStatus("current")
_OacQosMatchStatsTable_Object = MibTable
oacQosMatchStatsTable = _OacQosMatchStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 8)
)
if mibBuilder.loadTexts:
    oacQosMatchStatsTable.setStatus("current")
_OacQosMatchStatsEntry_Object = MibTableRow
oacQosMatchStatsEntry = _OacQosMatchStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 8, 1)
)
oacQosMatchStatsEntry.setIndexNames(
    (0, "OA-QOS-MIB", "oacQosPolicyIndex"),
    (0, "OA-QOS-MIB", "oacQosObjectsIndex"),
)
if mibBuilder.loadTexts:
    oacQosMatchStatsEntry.setStatus("current")
_OacQosMatchPreExecutePkt_Type = Counter32
_OacQosMatchPreExecutePkt_Object = MibTableColumn
oacQosMatchPreExecutePkt = _OacQosMatchPreExecutePkt_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 8, 1, 1),
    _OacQosMatchPreExecutePkt_Type()
)
oacQosMatchPreExecutePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosMatchPreExecutePkt.setStatus("current")
_OacQosMatchPreExecutePkt64_Type = Counter64
_OacQosMatchPreExecutePkt64_Object = MibTableColumn
oacQosMatchPreExecutePkt64 = _OacQosMatchPreExecutePkt64_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 8, 1, 2),
    _OacQosMatchPreExecutePkt64_Type()
)
oacQosMatchPreExecutePkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosMatchPreExecutePkt64.setStatus("current")
_OacQosMatchPreExecuteByte_Type = Counter32
_OacQosMatchPreExecuteByte_Object = MibTableColumn
oacQosMatchPreExecuteByte = _OacQosMatchPreExecuteByte_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 8, 1, 3),
    _OacQosMatchPreExecuteByte_Type()
)
oacQosMatchPreExecuteByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosMatchPreExecuteByte.setStatus("current")
_OacQosMatchPreExecuteByte64_Type = Counter64
_OacQosMatchPreExecuteByte64_Object = MibTableColumn
oacQosMatchPreExecuteByte64 = _OacQosMatchPreExecuteByte64_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 8, 1, 4),
    _OacQosMatchPreExecuteByte64_Type()
)
oacQosMatchPreExecuteByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosMatchPreExecuteByte64.setStatus("current")
_OacQosMatchPreExecuteBitRate_Type = Gauge32
_OacQosMatchPreExecuteBitRate_Object = MibTableColumn
oacQosMatchPreExecuteBitRate = _OacQosMatchPreExecuteBitRate_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 8, 1, 5),
    _OacQosMatchPreExecuteBitRate_Type()
)
oacQosMatchPreExecuteBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosMatchPreExecuteBitRate.setStatus("current")
if mibBuilder.loadTexts:
    oacQosMatchPreExecuteBitRate.setUnits("bits per second")
_OacQosSetConfigTable_Object = MibTable
oacQosSetConfigTable = _OacQosSetConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 9)
)
if mibBuilder.loadTexts:
    oacQosSetConfigTable.setStatus("current")
_OacQosSetConfigEntry_Object = MibTableRow
oacQosSetConfigEntry = _OacQosSetConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 9, 1)
)
oacQosSetConfigEntry.setIndexNames(
    (0, "OA-QOS-MIB", "oacQosConfigIndex"),
)
if mibBuilder.loadTexts:
    oacQosSetConfigEntry.setStatus("current")
_OacQosSetConfigFeature_Type = SetFeatureType
_OacQosSetConfigFeature_Object = MibTableColumn
oacQosSetConfigFeature = _OacQosSetConfigFeature_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 9, 1, 1),
    _OacQosSetConfigFeature_Type()
)
oacQosSetConfigFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosSetConfigFeature.setStatus("current")


class _OacQosSetConfigIpDSCPValue_Type(Integer32):
    """Custom type oacQosSetConfigIpDSCPValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_OacQosSetConfigIpDSCPValue_Type.__name__ = "Integer32"
_OacQosSetConfigIpDSCPValue_Object = MibTableColumn
oacQosSetConfigIpDSCPValue = _OacQosSetConfigIpDSCPValue_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 9, 1, 2),
    _OacQosSetConfigIpDSCPValue_Type()
)
oacQosSetConfigIpDSCPValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosSetConfigIpDSCPValue.setStatus("current")


class _OacQosSetConfigIpPrecedenceValue_Type(Integer32):
    """Custom type oacQosSetConfigIpPrecedenceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_OacQosSetConfigIpPrecedenceValue_Type.__name__ = "Integer32"
_OacQosSetConfigIpPrecedenceValue_Object = MibTableColumn
oacQosSetConfigIpPrecedenceValue = _OacQosSetConfigIpPrecedenceValue_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 9, 1, 3),
    _OacQosSetConfigIpPrecedenceValue_Type()
)
oacQosSetConfigIpPrecedenceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosSetConfigIpPrecedenceValue.setStatus("current")


class _OacQosSetConfigQosGroupValue_Type(Integer32):
    """Custom type oacQosSetConfigQosGroupValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_OacQosSetConfigQosGroupValue_Type.__name__ = "Integer32"
_OacQosSetConfigQosGroupValue_Object = MibTableColumn
oacQosSetConfigQosGroupValue = _OacQosSetConfigQosGroupValue_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 9, 1, 4),
    _OacQosSetConfigQosGroupValue_Type()
)
oacQosSetConfigQosGroupValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosSetConfigQosGroupValue.setStatus("current")


class _OacQosSetConfigDiscardClassValue_Type(Gauge32):
    """Custom type oacQosSetConfigDiscardClassValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_OacQosSetConfigDiscardClassValue_Type.__name__ = "Gauge32"
_OacQosSetConfigDiscardClassValue_Object = MibTableColumn
oacQosSetConfigDiscardClassValue = _OacQosSetConfigDiscardClassValue_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 9, 1, 5),
    _OacQosSetConfigDiscardClassValue_Type()
)
oacQosSetConfigDiscardClassValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosSetConfigDiscardClassValue.setStatus("current")
_OacQosPoliceConfigTable_Object = MibTable
oacQosPoliceConfigTable = _OacQosPoliceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 10)
)
if mibBuilder.loadTexts:
    oacQosPoliceConfigTable.setStatus("current")
_OacQosPoliceConfigEntry_Object = MibTableRow
oacQosPoliceConfigEntry = _OacQosPoliceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 10, 1)
)
oacQosPoliceConfigEntry.setIndexNames(
    (0, "OA-QOS-MIB", "oacQosConfigIndex"),
)
if mibBuilder.loadTexts:
    oacQosPoliceConfigEntry.setStatus("current")


class _OacQosPoliceConfigCir_Type(Gauge32):
    """Custom type oacQosPoliceConfigCir based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8000, 2000000000),
    )


_OacQosPoliceConfigCir_Type.__name__ = "Gauge32"
_OacQosPoliceConfigCir_Object = MibTableColumn
oacQosPoliceConfigCir = _OacQosPoliceConfigCir_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 10, 1, 1),
    _OacQosPoliceConfigCir_Type()
)
oacQosPoliceConfigCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceConfigCir.setStatus("current")
if mibBuilder.loadTexts:
    oacQosPoliceConfigCir.setUnits("bits/second")
_OacQosPoliceConfigCir64_Type = Counter64
_OacQosPoliceConfigCir64_Object = MibTableColumn
oacQosPoliceConfigCir64 = _OacQosPoliceConfigCir64_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 10, 1, 2),
    _OacQosPoliceConfigCir64_Type()
)
oacQosPoliceConfigCir64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceConfigCir64.setStatus("current")
if mibBuilder.loadTexts:
    oacQosPoliceConfigCir64.setUnits("bits/second")


class _OacQosPoliceConfigConformBurstSize_Type(Gauge32):
    """Custom type oacQosPoliceConfigConformBurstSize based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 512000000),
    )


_OacQosPoliceConfigConformBurstSize_Type.__name__ = "Gauge32"
_OacQosPoliceConfigConformBurstSize_Object = MibTableColumn
oacQosPoliceConfigConformBurstSize = _OacQosPoliceConfigConformBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 10, 1, 3),
    _OacQosPoliceConfigConformBurstSize_Type()
)
oacQosPoliceConfigConformBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceConfigConformBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    oacQosPoliceConfigConformBurstSize.setUnits("Octets")


class _OacQosPoliceConfigPir_Type(Gauge32):
    """Custom type oacQosPoliceConfigPir based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8000, 2000000000),
    )


_OacQosPoliceConfigPir_Type.__name__ = "Gauge32"
_OacQosPoliceConfigPir_Object = MibTableColumn
oacQosPoliceConfigPir = _OacQosPoliceConfigPir_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 10, 1, 4),
    _OacQosPoliceConfigPir_Type()
)
oacQosPoliceConfigPir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceConfigPir.setStatus("current")
if mibBuilder.loadTexts:
    oacQosPoliceConfigPir.setUnits("bits/second")


class _OacQosPoliceConfigPeakBurstSize_Type(Gauge32):
    """Custom type oacQosPoliceConfigPeakBurstSize based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 512000000),
    )


_OacQosPoliceConfigPeakBurstSize_Type.__name__ = "Gauge32"
_OacQosPoliceConfigPeakBurstSize_Object = MibTableColumn
oacQosPoliceConfigPeakBurstSize = _OacQosPoliceConfigPeakBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 10, 1, 5),
    _OacQosPoliceConfigPeakBurstSize_Type()
)
oacQosPoliceConfigPeakBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceConfigPeakBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    oacQosPoliceConfigPeakBurstSize.setUnits("Octets")
_OacQosPoliceConfigConformAction_Type = PoliceAction
_OacQosPoliceConfigConformAction_Object = MibTableColumn
oacQosPoliceConfigConformAction = _OacQosPoliceConfigConformAction_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 10, 1, 6),
    _OacQosPoliceConfigConformAction_Type()
)
oacQosPoliceConfigConformAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceConfigConformAction.setStatus("deprecated")


class _OacQosPoliceConfigConformSetValue_Type(Gauge32):
    """Custom type oacQosPoliceConfigConformSetValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_OacQosPoliceConfigConformSetValue_Type.__name__ = "Gauge32"
_OacQosPoliceConfigConformSetValue_Object = MibTableColumn
oacQosPoliceConfigConformSetValue = _OacQosPoliceConfigConformSetValue_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 10, 1, 7),
    _OacQosPoliceConfigConformSetValue_Type()
)
oacQosPoliceConfigConformSetValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceConfigConformSetValue.setStatus("deprecated")
_OacQosPoliceConfigExceedAction_Type = PoliceAction
_OacQosPoliceConfigExceedAction_Object = MibTableColumn
oacQosPoliceConfigExceedAction = _OacQosPoliceConfigExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 10, 1, 8),
    _OacQosPoliceConfigExceedAction_Type()
)
oacQosPoliceConfigExceedAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceConfigExceedAction.setStatus("deprecated")


class _OacQosPoliceConfigExceedSetValue_Type(Gauge32):
    """Custom type oacQosPoliceConfigExceedSetValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_OacQosPoliceConfigExceedSetValue_Type.__name__ = "Gauge32"
_OacQosPoliceConfigExceedSetValue_Object = MibTableColumn
oacQosPoliceConfigExceedSetValue = _OacQosPoliceConfigExceedSetValue_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 10, 1, 9),
    _OacQosPoliceConfigExceedSetValue_Type()
)
oacQosPoliceConfigExceedSetValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceConfigExceedSetValue.setStatus("deprecated")
_OacQosPoliceConfigViolateAction_Type = PoliceAction
_OacQosPoliceConfigViolateAction_Object = MibTableColumn
oacQosPoliceConfigViolateAction = _OacQosPoliceConfigViolateAction_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 10, 1, 10),
    _OacQosPoliceConfigViolateAction_Type()
)
oacQosPoliceConfigViolateAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceConfigViolateAction.setStatus("deprecated")


class _OacQosPoliceConfigViolateSetValue_Type(Gauge32):
    """Custom type oacQosPoliceConfigViolateSetValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_OacQosPoliceConfigViolateSetValue_Type.__name__ = "Gauge32"
_OacQosPoliceConfigViolateSetValue_Object = MibTableColumn
oacQosPoliceConfigViolateSetValue = _OacQosPoliceConfigViolateSetValue_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 10, 1, 11),
    _OacQosPoliceConfigViolateSetValue_Type()
)
oacQosPoliceConfigViolateSetValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceConfigViolateSetValue.setStatus("deprecated")
_OacQosPoliceActionConfigTable_Object = MibTable
oacQosPoliceActionConfigTable = _OacQosPoliceActionConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 11)
)
if mibBuilder.loadTexts:
    oacQosPoliceActionConfigTable.setStatus("current")
_OacQosPoliceActionConfigEntry_Object = MibTableRow
oacQosPoliceActionConfigEntry = _OacQosPoliceActionConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 11, 1)
)
oacQosPoliceActionConfigEntry.setIndexNames(
    (0, "OA-QOS-MIB", "oacQosConfigIndex"),
    (0, "OA-QOS-MIB", "oacQosPoliceActionConfigIndex"),
)
if mibBuilder.loadTexts:
    oacQosPoliceActionConfigEntry.setStatus("current")
_OacQosPoliceActionConfigIndex_Type = Gauge32
_OacQosPoliceActionConfigIndex_Object = MibTableColumn
oacQosPoliceActionConfigIndex = _OacQosPoliceActionConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 11, 1, 1),
    _OacQosPoliceActionConfigIndex_Type()
)
oacQosPoliceActionConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacQosPoliceActionConfigIndex.setStatus("current")
_OacQosPoliceActionConfigConform_Type = PoliceAction
_OacQosPoliceActionConfigConform_Object = MibTableColumn
oacQosPoliceActionConfigConform = _OacQosPoliceActionConfigConform_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 11, 1, 2),
    _OacQosPoliceActionConfigConform_Type()
)
oacQosPoliceActionConfigConform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceActionConfigConform.setStatus("current")


class _OacQosPoliceActionConfigConformSetValue_Type(Gauge32):
    """Custom type oacQosPoliceActionConfigConformSetValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_OacQosPoliceActionConfigConformSetValue_Type.__name__ = "Gauge32"
_OacQosPoliceActionConfigConformSetValue_Object = MibTableColumn
oacQosPoliceActionConfigConformSetValue = _OacQosPoliceActionConfigConformSetValue_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 11, 1, 3),
    _OacQosPoliceActionConfigConformSetValue_Type()
)
oacQosPoliceActionConfigConformSetValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceActionConfigConformSetValue.setStatus("current")
_OacQosPoliceActionConfigExceed_Type = PoliceAction
_OacQosPoliceActionConfigExceed_Object = MibTableColumn
oacQosPoliceActionConfigExceed = _OacQosPoliceActionConfigExceed_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 11, 1, 4),
    _OacQosPoliceActionConfigExceed_Type()
)
oacQosPoliceActionConfigExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceActionConfigExceed.setStatus("current")


class _OacQosPoliceActionConfigExceedSetValue_Type(Gauge32):
    """Custom type oacQosPoliceActionConfigExceedSetValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_OacQosPoliceActionConfigExceedSetValue_Type.__name__ = "Gauge32"
_OacQosPoliceActionConfigExceedSetValue_Object = MibTableColumn
oacQosPoliceActionConfigExceedSetValue = _OacQosPoliceActionConfigExceedSetValue_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 11, 1, 5),
    _OacQosPoliceActionConfigExceedSetValue_Type()
)
oacQosPoliceActionConfigExceedSetValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceActionConfigExceedSetValue.setStatus("current")
_OacQosPoliceActionConfigViolate_Type = PoliceAction
_OacQosPoliceActionConfigViolate_Object = MibTableColumn
oacQosPoliceActionConfigViolate = _OacQosPoliceActionConfigViolate_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 11, 1, 6),
    _OacQosPoliceActionConfigViolate_Type()
)
oacQosPoliceActionConfigViolate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceActionConfigViolate.setStatus("current")


class _OacQosPoliceActionConfigViolateSetValue_Type(Gauge32):
    """Custom type oacQosPoliceActionConfigViolateSetValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_OacQosPoliceActionConfigViolateSetValue_Type.__name__ = "Gauge32"
_OacQosPoliceActionConfigViolateSetValue_Object = MibTableColumn
oacQosPoliceActionConfigViolateSetValue = _OacQosPoliceActionConfigViolateSetValue_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 11, 1, 7),
    _OacQosPoliceActionConfigViolateSetValue_Type()
)
oacQosPoliceActionConfigViolateSetValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceActionConfigViolateSetValue.setStatus("current")
_OacQosPoliceStatsTable_Object = MibTable
oacQosPoliceStatsTable = _OacQosPoliceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 12)
)
if mibBuilder.loadTexts:
    oacQosPoliceStatsTable.setStatus("current")
_OacQosPoliceStatsEntry_Object = MibTableRow
oacQosPoliceStatsEntry = _OacQosPoliceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 12, 1)
)
oacQosPoliceStatsEntry.setIndexNames(
    (0, "OA-QOS-MIB", "oacQosPolicyIndex"),
    (0, "OA-QOS-MIB", "oacQosObjectsIndex"),
)
if mibBuilder.loadTexts:
    oacQosPoliceStatsEntry.setStatus("current")
_OacQosPoliceConformPkt_Type = Counter32
_OacQosPoliceConformPkt_Object = MibTableColumn
oacQosPoliceConformPkt = _OacQosPoliceConformPkt_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 12, 1, 1),
    _OacQosPoliceConformPkt_Type()
)
oacQosPoliceConformPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceConformPkt.setStatus("current")
if mibBuilder.loadTexts:
    oacQosPoliceConformPkt.setUnits("Packets")
_OacQosPoliceConformPkt64_Type = Counter64
_OacQosPoliceConformPkt64_Object = MibTableColumn
oacQosPoliceConformPkt64 = _OacQosPoliceConformPkt64_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 12, 1, 2),
    _OacQosPoliceConformPkt64_Type()
)
oacQosPoliceConformPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceConformPkt64.setStatus("current")
if mibBuilder.loadTexts:
    oacQosPoliceConformPkt64.setUnits("Packets")
_OacQosPoliceConformByte_Type = Counter32
_OacQosPoliceConformByte_Object = MibTableColumn
oacQosPoliceConformByte = _OacQosPoliceConformByte_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 12, 1, 3),
    _OacQosPoliceConformByte_Type()
)
oacQosPoliceConformByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceConformByte.setStatus("current")
if mibBuilder.loadTexts:
    oacQosPoliceConformByte.setUnits("Octets")
_OacQosPoliceConformByte64_Type = Counter64
_OacQosPoliceConformByte64_Object = MibTableColumn
oacQosPoliceConformByte64 = _OacQosPoliceConformByte64_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 12, 1, 4),
    _OacQosPoliceConformByte64_Type()
)
oacQosPoliceConformByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceConformByte64.setStatus("current")
if mibBuilder.loadTexts:
    oacQosPoliceConformByte64.setUnits("Octets")
_OacQosPoliceConformBitRate_Type = Gauge32
_OacQosPoliceConformBitRate_Object = MibTableColumn
oacQosPoliceConformBitRate = _OacQosPoliceConformBitRate_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 12, 1, 5),
    _OacQosPoliceConformBitRate_Type()
)
oacQosPoliceConformBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceConformBitRate.setStatus("current")
if mibBuilder.loadTexts:
    oacQosPoliceConformBitRate.setUnits("bits per second")
_OacQosPoliceExceedPkt_Type = Counter32
_OacQosPoliceExceedPkt_Object = MibTableColumn
oacQosPoliceExceedPkt = _OacQosPoliceExceedPkt_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 12, 1, 6),
    _OacQosPoliceExceedPkt_Type()
)
oacQosPoliceExceedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceExceedPkt.setStatus("current")
if mibBuilder.loadTexts:
    oacQosPoliceExceedPkt.setUnits("Packets")
_OacQosPoliceExceedPkt64_Type = Counter64
_OacQosPoliceExceedPkt64_Object = MibTableColumn
oacQosPoliceExceedPkt64 = _OacQosPoliceExceedPkt64_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 12, 1, 7),
    _OacQosPoliceExceedPkt64_Type()
)
oacQosPoliceExceedPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceExceedPkt64.setStatus("current")
if mibBuilder.loadTexts:
    oacQosPoliceExceedPkt64.setUnits("Packets")
_OacQosPoliceExceedByte_Type = Counter32
_OacQosPoliceExceedByte_Object = MibTableColumn
oacQosPoliceExceedByte = _OacQosPoliceExceedByte_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 12, 1, 8),
    _OacQosPoliceExceedByte_Type()
)
oacQosPoliceExceedByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceExceedByte.setStatus("current")
if mibBuilder.loadTexts:
    oacQosPoliceExceedByte.setUnits("Octets")
_OacQosPoliceExceedByte64_Type = Counter64
_OacQosPoliceExceedByte64_Object = MibTableColumn
oacQosPoliceExceedByte64 = _OacQosPoliceExceedByte64_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 12, 1, 9),
    _OacQosPoliceExceedByte64_Type()
)
oacQosPoliceExceedByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceExceedByte64.setStatus("current")
if mibBuilder.loadTexts:
    oacQosPoliceExceedByte64.setUnits("Octets")
_OacQosPoliceExceedBitRate_Type = Gauge32
_OacQosPoliceExceedBitRate_Object = MibTableColumn
oacQosPoliceExceedBitRate = _OacQosPoliceExceedBitRate_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 12, 1, 10),
    _OacQosPoliceExceedBitRate_Type()
)
oacQosPoliceExceedBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceExceedBitRate.setStatus("current")
if mibBuilder.loadTexts:
    oacQosPoliceExceedBitRate.setUnits("bits per second")
_OacQosPoliceViolatePkt_Type = Counter32
_OacQosPoliceViolatePkt_Object = MibTableColumn
oacQosPoliceViolatePkt = _OacQosPoliceViolatePkt_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 12, 1, 11),
    _OacQosPoliceViolatePkt_Type()
)
oacQosPoliceViolatePkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceViolatePkt.setStatus("current")
if mibBuilder.loadTexts:
    oacQosPoliceViolatePkt.setUnits("Packets")
_OacQosPoliceViolatePkt64_Type = Counter64
_OacQosPoliceViolatePkt64_Object = MibTableColumn
oacQosPoliceViolatePkt64 = _OacQosPoliceViolatePkt64_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 12, 1, 12),
    _OacQosPoliceViolatePkt64_Type()
)
oacQosPoliceViolatePkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceViolatePkt64.setStatus("current")
if mibBuilder.loadTexts:
    oacQosPoliceViolatePkt64.setUnits("Packets")
_OacQosPoliceViolateByte_Type = Counter32
_OacQosPoliceViolateByte_Object = MibTableColumn
oacQosPoliceViolateByte = _OacQosPoliceViolateByte_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 12, 1, 13),
    _OacQosPoliceViolateByte_Type()
)
oacQosPoliceViolateByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceViolateByte.setStatus("current")
if mibBuilder.loadTexts:
    oacQosPoliceViolateByte.setUnits("Octets")
_OacQosPoliceViolateByte64_Type = Counter64
_OacQosPoliceViolateByte64_Object = MibTableColumn
oacQosPoliceViolateByte64 = _OacQosPoliceViolateByte64_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 12, 1, 14),
    _OacQosPoliceViolateByte64_Type()
)
oacQosPoliceViolateByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceViolateByte64.setStatus("current")
if mibBuilder.loadTexts:
    oacQosPoliceViolateByte64.setUnits("Octets")
_OacQosPoliceViolateBitRate_Type = Gauge32
_OacQosPoliceViolateBitRate_Object = MibTableColumn
oacQosPoliceViolateBitRate = _OacQosPoliceViolateBitRate_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 12, 1, 15),
    _OacQosPoliceViolateBitRate_Type()
)
oacQosPoliceViolateBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosPoliceViolateBitRate.setStatus("current")
if mibBuilder.loadTexts:
    oacQosPoliceViolateBitRate.setUnits("bits per second")
_OacQosWREDConfigTable_Object = MibTable
oacQosWREDConfigTable = _OacQosWREDConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 13)
)
if mibBuilder.loadTexts:
    oacQosWREDConfigTable.setStatus("current")
_OacQosWREDConfigEntry_Object = MibTableRow
oacQosWREDConfigEntry = _OacQosWREDConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 13, 1)
)
oacQosWREDConfigEntry.setIndexNames(
    (0, "OA-QOS-MIB", "oacQosConfigIndex"),
)
if mibBuilder.loadTexts:
    oacQosWREDConfigEntry.setStatus("current")


class _OacQosWREDConfigExponentialWeight_Type(Integer32):
    """Custom type oacQosWREDConfigExponentialWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_OacQosWREDConfigExponentialWeight_Type.__name__ = "Integer32"
_OacQosWREDConfigExponentialWeight_Object = MibTableColumn
oacQosWREDConfigExponentialWeight = _OacQosWREDConfigExponentialWeight_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 13, 1, 1),
    _OacQosWREDConfigExponentialWeight_Type()
)
oacQosWREDConfigExponentialWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosWREDConfigExponentialWeight.setStatus("current")
_OacQosWREDConfigDscpPrecQosGroup_Type = WREDMechanism
_OacQosWREDConfigDscpPrecQosGroup_Object = MibTableColumn
oacQosWREDConfigDscpPrecQosGroup = _OacQosWREDConfigDscpPrecQosGroup_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 13, 1, 2),
    _OacQosWREDConfigDscpPrecQosGroup_Type()
)
oacQosWREDConfigDscpPrecQosGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosWREDConfigDscpPrecQosGroup.setStatus("current")
_OacQosWREDConfigECNEnabled_Type = TruthValue
_OacQosWREDConfigECNEnabled_Object = MibTableColumn
oacQosWREDConfigECNEnabled = _OacQosWREDConfigECNEnabled_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 13, 1, 3),
    _OacQosWREDConfigECNEnabled_Type()
)
oacQosWREDConfigECNEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosWREDConfigECNEnabled.setStatus("current")
_OacQosWREDClassConfigTable_Object = MibTable
oacQosWREDClassConfigTable = _OacQosWREDClassConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 14)
)
if mibBuilder.loadTexts:
    oacQosWREDClassConfigTable.setStatus("current")
_OacQosWREDClassConfigEntry_Object = MibTableRow
oacQosWREDClassConfigEntry = _OacQosWREDClassConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 14, 1)
)
oacQosWREDClassConfigEntry.setIndexNames(
    (0, "OA-QOS-MIB", "oacQosConfigIndex"),
    (0, "OA-QOS-MIB", "oacQosWREDValue"),
)
if mibBuilder.loadTexts:
    oacQosWREDClassConfigEntry.setStatus("current")


class _OacQosWREDValue_Type(Integer32):
    """Custom type oacQosWREDValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_OacQosWREDValue_Type.__name__ = "Integer32"
_OacQosWREDValue_Object = MibTableColumn
oacQosWREDValue = _OacQosWREDValue_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 14, 1, 1),
    _OacQosWREDValue_Type()
)
oacQosWREDValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacQosWREDValue.setStatus("current")


class _OacQosWREDConfigPktDropProb_Type(Integer32):
    """Custom type oacQosWREDConfigPktDropProb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_OacQosWREDConfigPktDropProb_Type.__name__ = "Integer32"
_OacQosWREDConfigPktDropProb_Object = MibTableColumn
oacQosWREDConfigPktDropProb = _OacQosWREDConfigPktDropProb_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 14, 1, 2),
    _OacQosWREDConfigPktDropProb_Type()
)
oacQosWREDConfigPktDropProb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosWREDConfigPktDropProb.setStatus("current")
_OacQosWREDClassConfigThresholdUnit_Type = QosQueueUnitType
_OacQosWREDClassConfigThresholdUnit_Object = MibTableColumn
oacQosWREDClassConfigThresholdUnit = _OacQosWREDClassConfigThresholdUnit_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 14, 1, 3),
    _OacQosWREDClassConfigThresholdUnit_Type()
)
oacQosWREDClassConfigThresholdUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosWREDClassConfigThresholdUnit.setStatus("current")
_OacQosWREDClassConfigMinThreshold_Type = QosQueueDepth
_OacQosWREDClassConfigMinThreshold_Object = MibTableColumn
oacQosWREDClassConfigMinThreshold = _OacQosWREDClassConfigMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 14, 1, 4),
    _OacQosWREDClassConfigMinThreshold_Type()
)
oacQosWREDClassConfigMinThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosWREDClassConfigMinThreshold.setStatus("current")
_OacQosWREDClassConfigMaxThreshold_Type = QosQueueDepth
_OacQosWREDClassConfigMaxThreshold_Object = MibTableColumn
oacQosWREDClassConfigMaxThreshold = _OacQosWREDClassConfigMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 14, 1, 5),
    _OacQosWREDClassConfigMaxThreshold_Type()
)
oacQosWREDClassConfigMaxThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosWREDClassConfigMaxThreshold.setStatus("current")
_OacQosWREDClassStatsTable_Object = MibTable
oacQosWREDClassStatsTable = _OacQosWREDClassStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 15)
)
if mibBuilder.loadTexts:
    oacQosWREDClassStatsTable.setStatus("current")
_OacQosWREDClassStatsEntry_Object = MibTableRow
oacQosWREDClassStatsEntry = _OacQosWREDClassStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 15, 1)
)
oacQosWREDClassStatsEntry.setIndexNames(
    (0, "OA-QOS-MIB", "oacQosPolicyIndex"),
    (0, "OA-QOS-MIB", "oacQosObjectsIndex"),
    (0, "OA-QOS-MIB", "oacQosWREDValue"),
)
if mibBuilder.loadTexts:
    oacQosWREDClassStatsEntry.setStatus("current")
_OacQosWREDAverageQueueSizeUnits_Type = QosQueueUnitType
_OacQosWREDAverageQueueSizeUnits_Object = MibTableColumn
oacQosWREDAverageQueueSizeUnits = _OacQosWREDAverageQueueSizeUnits_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 15, 1, 1),
    _OacQosWREDAverageQueueSizeUnits_Type()
)
oacQosWREDAverageQueueSizeUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosWREDAverageQueueSizeUnits.setStatus("current")
_OacQosWREDAverageQueueSize_Type = QosQueueDepth
_OacQosWREDAverageQueueSize_Object = MibTableColumn
oacQosWREDAverageQueueSize = _OacQosWREDAverageQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 15, 1, 2),
    _OacQosWREDAverageQueueSize_Type()
)
oacQosWREDAverageQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosWREDAverageQueueSize.setStatus("current")
_OacQosWREDRandomDropPkt_Type = Counter32
_OacQosWREDRandomDropPkt_Object = MibTableColumn
oacQosWREDRandomDropPkt = _OacQosWREDRandomDropPkt_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 15, 1, 3),
    _OacQosWREDRandomDropPkt_Type()
)
oacQosWREDRandomDropPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosWREDRandomDropPkt.setStatus("current")
if mibBuilder.loadTexts:
    oacQosWREDRandomDropPkt.setUnits("Packets")
_OacQosWREDRandomDropPkt64_Type = Counter64
_OacQosWREDRandomDropPkt64_Object = MibTableColumn
oacQosWREDRandomDropPkt64 = _OacQosWREDRandomDropPkt64_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 15, 1, 4),
    _OacQosWREDRandomDropPkt64_Type()
)
oacQosWREDRandomDropPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosWREDRandomDropPkt64.setStatus("current")
if mibBuilder.loadTexts:
    oacQosWREDRandomDropPkt64.setUnits("Packets")
_OacQosWREDRandomDropByte_Type = Counter32
_OacQosWREDRandomDropByte_Object = MibTableColumn
oacQosWREDRandomDropByte = _OacQosWREDRandomDropByte_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 15, 1, 5),
    _OacQosWREDRandomDropByte_Type()
)
oacQosWREDRandomDropByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosWREDRandomDropByte.setStatus("current")
if mibBuilder.loadTexts:
    oacQosWREDRandomDropByte.setUnits("Octets")
_OacQosWREDRandomDropByte64_Type = Counter64
_OacQosWREDRandomDropByte64_Object = MibTableColumn
oacQosWREDRandomDropByte64 = _OacQosWREDRandomDropByte64_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 15, 1, 6),
    _OacQosWREDRandomDropByte64_Type()
)
oacQosWREDRandomDropByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosWREDRandomDropByte64.setStatus("current")
if mibBuilder.loadTexts:
    oacQosWREDRandomDropByte64.setUnits("Octets")
_OacQosWREDTailDropPkt_Type = Counter32
_OacQosWREDTailDropPkt_Object = MibTableColumn
oacQosWREDTailDropPkt = _OacQosWREDTailDropPkt_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 15, 1, 7),
    _OacQosWREDTailDropPkt_Type()
)
oacQosWREDTailDropPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosWREDTailDropPkt.setStatus("current")
if mibBuilder.loadTexts:
    oacQosWREDTailDropPkt.setUnits("Packets")
_OacQosWREDTailDropPkt64_Type = Counter64
_OacQosWREDTailDropPkt64_Object = MibTableColumn
oacQosWREDTailDropPkt64 = _OacQosWREDTailDropPkt64_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 15, 1, 8),
    _OacQosWREDTailDropPkt64_Type()
)
oacQosWREDTailDropPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosWREDTailDropPkt64.setStatus("current")
if mibBuilder.loadTexts:
    oacQosWREDTailDropPkt64.setUnits("Packets")
_OacQosWREDTailDropByte_Type = Counter32
_OacQosWREDTailDropByte_Object = MibTableColumn
oacQosWREDTailDropByte = _OacQosWREDTailDropByte_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 15, 1, 9),
    _OacQosWREDTailDropByte_Type()
)
oacQosWREDTailDropByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosWREDTailDropByte.setStatus("current")
if mibBuilder.loadTexts:
    oacQosWREDTailDropByte.setUnits("Octets")
_OacQosWREDTailDropByte64_Type = Counter64
_OacQosWREDTailDropByte64_Object = MibTableColumn
oacQosWREDTailDropByte64 = _OacQosWREDTailDropByte64_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 15, 1, 10),
    _OacQosWREDTailDropByte64_Type()
)
oacQosWREDTailDropByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosWREDTailDropByte64.setStatus("current")
if mibBuilder.loadTexts:
    oacQosWREDTailDropByte64.setUnits("Octets")
_OacQosWREDTransmitPkt_Type = Counter32
_OacQosWREDTransmitPkt_Object = MibTableColumn
oacQosWREDTransmitPkt = _OacQosWREDTransmitPkt_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 15, 1, 11),
    _OacQosWREDTransmitPkt_Type()
)
oacQosWREDTransmitPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosWREDTransmitPkt.setStatus("current")
if mibBuilder.loadTexts:
    oacQosWREDTransmitPkt.setUnits("Packets")
_OacQosWREDTransmitPkt64_Type = Counter64
_OacQosWREDTransmitPkt64_Object = MibTableColumn
oacQosWREDTransmitPkt64 = _OacQosWREDTransmitPkt64_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 15, 1, 12),
    _OacQosWREDTransmitPkt64_Type()
)
oacQosWREDTransmitPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosWREDTransmitPkt64.setStatus("current")
if mibBuilder.loadTexts:
    oacQosWREDTransmitPkt64.setUnits("Packets")
_OacQosWREDTransmitByte_Type = Counter32
_OacQosWREDTransmitByte_Object = MibTableColumn
oacQosWREDTransmitByte = _OacQosWREDTransmitByte_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 15, 1, 13),
    _OacQosWREDTransmitByte_Type()
)
oacQosWREDTransmitByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosWREDTransmitByte.setStatus("current")
if mibBuilder.loadTexts:
    oacQosWREDTransmitByte.setUnits("Octets")
_OacQosWREDTransmitByte64_Type = Counter64
_OacQosWREDTransmitByte64_Object = MibTableColumn
oacQosWREDTransmitByte64 = _OacQosWREDTransmitByte64_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 15, 1, 14),
    _OacQosWREDTransmitByte64_Type()
)
oacQosWREDTransmitByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosWREDTransmitByte64.setStatus("current")
if mibBuilder.loadTexts:
    oacQosWREDTransmitByte64.setUnits("Octets")
_OacQosWREDECNMarkPkt_Type = Counter32
_OacQosWREDECNMarkPkt_Object = MibTableColumn
oacQosWREDECNMarkPkt = _OacQosWREDECNMarkPkt_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 15, 1, 15),
    _OacQosWREDECNMarkPkt_Type()
)
oacQosWREDECNMarkPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosWREDECNMarkPkt.setStatus("current")
if mibBuilder.loadTexts:
    oacQosWREDECNMarkPkt.setUnits("Packets")
_OacQosWREDECNMarkPkt64_Type = Counter64
_OacQosWREDECNMarkPkt64_Object = MibTableColumn
oacQosWREDECNMarkPkt64 = _OacQosWREDECNMarkPkt64_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 15, 1, 16),
    _OacQosWREDECNMarkPkt64_Type()
)
oacQosWREDECNMarkPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosWREDECNMarkPkt64.setStatus("current")
if mibBuilder.loadTexts:
    oacQosWREDECNMarkPkt64.setUnits("Packets")
_OacQosWREDECNMarkByte_Type = Counter32
_OacQosWREDECNMarkByte_Object = MibTableColumn
oacQosWREDECNMarkByte = _OacQosWREDECNMarkByte_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 15, 1, 17),
    _OacQosWREDECNMarkByte_Type()
)
oacQosWREDECNMarkByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosWREDECNMarkByte.setStatus("current")
if mibBuilder.loadTexts:
    oacQosWREDECNMarkByte.setUnits("Octets")
_OacQosWREDECNMarkByte64_Type = Counter64
_OacQosWREDECNMarkByte64_Object = MibTableColumn
oacQosWREDECNMarkByte64 = _OacQosWREDECNMarkByte64_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 15, 1, 18),
    _OacQosWREDECNMarkByte64_Type()
)
oacQosWREDECNMarkByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosWREDECNMarkByte64.setStatus("current")
if mibBuilder.loadTexts:
    oacQosWREDECNMarkByte64.setUnits("Octets")
_OacQosQueueConfigTable_Object = MibTable
oacQosQueueConfigTable = _OacQosQueueConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 16)
)
if mibBuilder.loadTexts:
    oacQosQueueConfigTable.setStatus("current")
_OacQosQueueConfigEntry_Object = MibTableRow
oacQosQueueConfigEntry = _OacQosQueueConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 16, 1)
)
oacQosQueueConfigEntry.setIndexNames(
    (0, "OA-QOS-MIB", "oacQosConfigIndex"),
)
if mibBuilder.loadTexts:
    oacQosQueueConfigEntry.setStatus("current")
_OacQosQueueConfigFlowBasedEnabled_Type = TruthValue
_OacQosQueueConfigFlowBasedEnabled_Object = MibTableColumn
oacQosQueueConfigFlowBasedEnabled = _OacQosQueueConfigFlowBasedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 16, 1, 1),
    _OacQosQueueConfigFlowBasedEnabled_Type()
)
oacQosQueueConfigFlowBasedEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosQueueConfigFlowBasedEnabled.setStatus("current")
_OacQosQueueConfigPriorityEnabled_Type = TruthValue
_OacQosQueueConfigPriorityEnabled_Object = MibTableColumn
oacQosQueueConfigPriorityEnabled = _OacQosQueueConfigPriorityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 16, 1, 2),
    _OacQosQueueConfigPriorityEnabled_Type()
)
oacQosQueueConfigPriorityEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosQueueConfigPriorityEnabled.setStatus("current")


class _OacQosQueueConfigBandwidth_Type(Integer32):
    """Custom type oacQosQueueConfigBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000000),
    )


_OacQosQueueConfigBandwidth_Type.__name__ = "Integer32"
_OacQosQueueConfigBandwidth_Object = MibTableColumn
oacQosQueueConfigBandwidth = _OacQosQueueConfigBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 16, 1, 3),
    _OacQosQueueConfigBandwidth_Type()
)
oacQosQueueConfigBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosQueueConfigBandwidth.setStatus("current")
_OacQosQueueConfigBandwidthUnits_Type = QueueingBandwidthUnits
_OacQosQueueConfigBandwidthUnits_Object = MibTableColumn
oacQosQueueConfigBandwidthUnits = _OacQosQueueConfigBandwidthUnits_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 16, 1, 4),
    _OacQosQueueConfigBandwidthUnits_Type()
)
oacQosQueueConfigBandwidthUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosQueueConfigBandwidthUnits.setStatus("current")


class _OacQosQueueConfigFlowBasedQSize_Type(Integer32):
    """Custom type oacQosQueueConfigFlowBasedQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32768),
    )


_OacQosQueueConfigFlowBasedQSize_Type.__name__ = "Integer32"
_OacQosQueueConfigFlowBasedQSize_Object = MibTableColumn
oacQosQueueConfigFlowBasedQSize = _OacQosQueueConfigFlowBasedQSize_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 16, 1, 5),
    _OacQosQueueConfigFlowBasedQSize_Type()
)
oacQosQueueConfigFlowBasedQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosQueueConfigFlowBasedQSize.setStatus("current")
if mibBuilder.loadTexts:
    oacQosQueueConfigFlowBasedQSize.setUnits("Packets")


class _OacQosQueueConfigFlowBasedQNumber_Type(Integer32):
    """Custom type oacQosQueueConfigFlowBasedQNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32768),
    )


_OacQosQueueConfigFlowBasedQNumber_Type.__name__ = "Integer32"
_OacQosQueueConfigFlowBasedQNumber_Object = MibTableColumn
oacQosQueueConfigFlowBasedQNumber = _OacQosQueueConfigFlowBasedQNumber_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 16, 1, 6),
    _OacQosQueueConfigFlowBasedQNumber_Type()
)
oacQosQueueConfigFlowBasedQNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosQueueConfigFlowBasedQNumber.setStatus("current")


class _OacQosQueueConfigPrioBurstSize_Type(Gauge32):
    """Custom type oacQosQueueConfigPrioBurstSize based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 64000000),
    )


_OacQosQueueConfigPrioBurstSize_Type.__name__ = "Gauge32"
_OacQosQueueConfigPrioBurstSize_Object = MibTableColumn
oacQosQueueConfigPrioBurstSize = _OacQosQueueConfigPrioBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 16, 1, 7),
    _OacQosQueueConfigPrioBurstSize_Type()
)
oacQosQueueConfigPrioBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosQueueConfigPrioBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    oacQosQueueConfigPrioBurstSize.setUnits("Bytes")
_OacQosQueueConfigQueueLimitUnits_Type = QosQueueUnitType
_OacQosQueueConfigQueueLimitUnits_Object = MibTableColumn
oacQosQueueConfigQueueLimitUnits = _OacQosQueueConfigQueueLimitUnits_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 16, 1, 8),
    _OacQosQueueConfigQueueLimitUnits_Type()
)
oacQosQueueConfigQueueLimitUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosQueueConfigQueueLimitUnits.setStatus("current")
_OacQosQueueConfigQueueLimit_Type = QosQueueDepth
_OacQosQueueConfigQueueLimit_Object = MibTableColumn
oacQosQueueConfigQueueLimit = _OacQosQueueConfigQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 16, 1, 9),
    _OacQosQueueConfigQueueLimit_Type()
)
oacQosQueueConfigQueueLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosQueueConfigQueueLimit.setStatus("current")
_OacQosQueueStatsTable_Object = MibTable
oacQosQueueStatsTable = _OacQosQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 17)
)
if mibBuilder.loadTexts:
    oacQosQueueStatsTable.setStatus("current")
_OacQosQueueStatsEntry_Object = MibTableRow
oacQosQueueStatsEntry = _OacQosQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 17, 1)
)
oacQosQueueStatsEntry.setIndexNames(
    (0, "OA-QOS-MIB", "oacQosPolicyIndex"),
    (0, "OA-QOS-MIB", "oacQosObjectsIndex"),
)
if mibBuilder.loadTexts:
    oacQosQueueStatsEntry.setStatus("current")
_OacQosQueueDiscardByte_Type = Counter32
_OacQosQueueDiscardByte_Object = MibTableColumn
oacQosQueueDiscardByte = _OacQosQueueDiscardByte_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 17, 1, 1),
    _OacQosQueueDiscardByte_Type()
)
oacQosQueueDiscardByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosQueueDiscardByte.setStatus("current")
if mibBuilder.loadTexts:
    oacQosQueueDiscardByte.setUnits("Octets")
_OacQosQueueDiscardByte64_Type = Counter64
_OacQosQueueDiscardByte64_Object = MibTableColumn
oacQosQueueDiscardByte64 = _OacQosQueueDiscardByte64_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 17, 1, 2),
    _OacQosQueueDiscardByte64_Type()
)
oacQosQueueDiscardByte64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosQueueDiscardByte64.setStatus("current")
if mibBuilder.loadTexts:
    oacQosQueueDiscardByte64.setUnits("Octets")
_OacQosQueueDiscardPkt_Type = Counter32
_OacQosQueueDiscardPkt_Object = MibTableColumn
oacQosQueueDiscardPkt = _OacQosQueueDiscardPkt_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 17, 1, 3),
    _OacQosQueueDiscardPkt_Type()
)
oacQosQueueDiscardPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosQueueDiscardPkt.setStatus("current")
if mibBuilder.loadTexts:
    oacQosQueueDiscardPkt.setUnits("Packets")
_OacQosQueueDiscardPkt64_Type = Counter64
_OacQosQueueDiscardPkt64_Object = MibTableColumn
oacQosQueueDiscardPkt64 = _OacQosQueueDiscardPkt64_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 17, 1, 4),
    _OacQosQueueDiscardPkt64_Type()
)
oacQosQueueDiscardPkt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosQueueDiscardPkt64.setStatus("current")
if mibBuilder.loadTexts:
    oacQosQueueDiscardPkt64.setUnits("Packets")
_OacQosQueueCurrentQDepth_Type = Gauge32
_OacQosQueueCurrentQDepth_Object = MibTableColumn
oacQosQueueCurrentQDepth = _OacQosQueueCurrentQDepth_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 17, 1, 5),
    _OacQosQueueCurrentQDepth_Type()
)
oacQosQueueCurrentQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosQueueCurrentQDepth.setStatus("current")
if mibBuilder.loadTexts:
    oacQosQueueCurrentQDepth.setUnits("Octets")
_OacQosQueueMaxQDepth_Type = Gauge32
_OacQosQueueMaxQDepth_Object = MibTableColumn
oacQosQueueMaxQDepth = _OacQosQueueMaxQDepth_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 3, 17, 1, 6),
    _OacQosQueueMaxQDepth_Type()
)
oacQosQueueMaxQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacQosQueueMaxQDepth.setStatus("current")
if mibBuilder.loadTexts:
    oacQosQueueMaxQDepth.setUnits("Octets")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OA-QOS-MIB",
    **{"QosObjectType": QosObjectType,
       "TrafficDirection": TrafficDirection,
       "QosClassInfo": QosClassInfo,
       "QosMatchInfo": QosMatchInfo,
       "InterfaceType": InterfaceType,
       "QueueingBandwidthUnits": QueueingBandwidthUnits,
       "PoliceAction": PoliceAction,
       "SetFeatureType": SetFeatureType,
       "WREDMechanism": WREDMechanism,
       "QosQueueUnitType": QosQueueUnitType,
       "QosQueueDepth": QosQueueDepth,
       "oacQOS": oacQOS,
       "oacQosServicePolicyTable": oacQosServicePolicyTable,
       "oacQosServicePolicyEntry": oacQosServicePolicyEntry,
       "oacQosPolicyIndex": oacQosPolicyIndex,
       "oacQosIfIndex": oacQosIfIndex,
       "oacQosIfType": oacQosIfType,
       "oacQosPolicyDirection": oacQosPolicyDirection,
       "oacQosInterfacePolicyTable": oacQosInterfacePolicyTable,
       "oacQosInterfacePolicyEntry": oacQosInterfacePolicyEntry,
       "oacQosInterfacePolicyIndex": oacQosInterfacePolicyIndex,
       "oacQosObjectsTable": oacQosObjectsTable,
       "oacQosObjectsEntry": oacQosObjectsEntry,
       "oacQosObjectsIndex": oacQosObjectsIndex,
       "oacQosConfigIndex": oacQosConfigIndex,
       "oacQosObjectsType": oacQosObjectsType,
       "oacQosParentObjectsIndex": oacQosParentObjectsIndex,
       "oacQosPolicyMapConfigTable": oacQosPolicyMapConfigTable,
       "oacQosPolicyMapConfigEntry": oacQosPolicyMapConfigEntry,
       "oacQosPolicyMapName": oacQosPolicyMapName,
       "oacQosClassMapConfigTable": oacQosClassMapConfigTable,
       "oacQosClassMapConfigEntry": oacQosClassMapConfigEntry,
       "oacQosClassMapName": oacQosClassMapName,
       "oacQosClassMapInfo": oacQosClassMapInfo,
       "oacQosClassMapStatsTable": oacQosClassMapStatsTable,
       "oacQosClassMapStatsEntry": oacQosClassMapStatsEntry,
       "oacQosClassMapPreExecutePkt": oacQosClassMapPreExecutePkt,
       "oacQosClassMapPreExecutePkt64": oacQosClassMapPreExecutePkt64,
       "oacQosClassMapPreExecuteByte": oacQosClassMapPreExecuteByte,
       "oacQosClassMapPreExecuteByte64": oacQosClassMapPreExecuteByte64,
       "oacQosClassMapPreExecuteBitRate": oacQosClassMapPreExecuteBitRate,
       "oacQosClassMapPostExecuteByte": oacQosClassMapPostExecuteByte,
       "oacQosClassMapPostExecuteByte64": oacQosClassMapPostExecuteByte64,
       "oacQosClassMapPostExecuteBitRate": oacQosClassMapPostExecuteBitRate,
       "oacQosClassMapDropPkt": oacQosClassMapDropPkt,
       "oacQosClassMapDropPkt64": oacQosClassMapDropPkt64,
       "oacQosClassMapDropByte": oacQosClassMapDropByte,
       "oacQosClassMapDropByte64": oacQosClassMapDropByte64,
       "oacQosClassMapDropBitRate": oacQosClassMapDropBitRate,
       "oacQosClassMapRemarkedPkt": oacQosClassMapRemarkedPkt,
       "oacQosClassMapRemarkedPkt64": oacQosClassMapRemarkedPkt64,
       "oacQosClassMapRemarkedByte": oacQosClassMapRemarkedByte,
       "oacQosClassMapRemarkedByte64": oacQosClassMapRemarkedByte64,
       "oacQosMatchConfigTable": oacQosMatchConfigTable,
       "oacQosMatchConfigEntry": oacQosMatchConfigEntry,
       "oacQosMatchName": oacQosMatchName,
       "oacQosMatchInfo": oacQosMatchInfo,
       "oacQosMatchStatsTable": oacQosMatchStatsTable,
       "oacQosMatchStatsEntry": oacQosMatchStatsEntry,
       "oacQosMatchPreExecutePkt": oacQosMatchPreExecutePkt,
       "oacQosMatchPreExecutePkt64": oacQosMatchPreExecutePkt64,
       "oacQosMatchPreExecuteByte": oacQosMatchPreExecuteByte,
       "oacQosMatchPreExecuteByte64": oacQosMatchPreExecuteByte64,
       "oacQosMatchPreExecuteBitRate": oacQosMatchPreExecuteBitRate,
       "oacQosSetConfigTable": oacQosSetConfigTable,
       "oacQosSetConfigEntry": oacQosSetConfigEntry,
       "oacQosSetConfigFeature": oacQosSetConfigFeature,
       "oacQosSetConfigIpDSCPValue": oacQosSetConfigIpDSCPValue,
       "oacQosSetConfigIpPrecedenceValue": oacQosSetConfigIpPrecedenceValue,
       "oacQosSetConfigQosGroupValue": oacQosSetConfigQosGroupValue,
       "oacQosSetConfigDiscardClassValue": oacQosSetConfigDiscardClassValue,
       "oacQosPoliceConfigTable": oacQosPoliceConfigTable,
       "oacQosPoliceConfigEntry": oacQosPoliceConfigEntry,
       "oacQosPoliceConfigCir": oacQosPoliceConfigCir,
       "oacQosPoliceConfigCir64": oacQosPoliceConfigCir64,
       "oacQosPoliceConfigConformBurstSize": oacQosPoliceConfigConformBurstSize,
       "oacQosPoliceConfigPir": oacQosPoliceConfigPir,
       "oacQosPoliceConfigPeakBurstSize": oacQosPoliceConfigPeakBurstSize,
       "oacQosPoliceConfigConformAction": oacQosPoliceConfigConformAction,
       "oacQosPoliceConfigConformSetValue": oacQosPoliceConfigConformSetValue,
       "oacQosPoliceConfigExceedAction": oacQosPoliceConfigExceedAction,
       "oacQosPoliceConfigExceedSetValue": oacQosPoliceConfigExceedSetValue,
       "oacQosPoliceConfigViolateAction": oacQosPoliceConfigViolateAction,
       "oacQosPoliceConfigViolateSetValue": oacQosPoliceConfigViolateSetValue,
       "oacQosPoliceActionConfigTable": oacQosPoliceActionConfigTable,
       "oacQosPoliceActionConfigEntry": oacQosPoliceActionConfigEntry,
       "oacQosPoliceActionConfigIndex": oacQosPoliceActionConfigIndex,
       "oacQosPoliceActionConfigConform": oacQosPoliceActionConfigConform,
       "oacQosPoliceActionConfigConformSetValue": oacQosPoliceActionConfigConformSetValue,
       "oacQosPoliceActionConfigExceed": oacQosPoliceActionConfigExceed,
       "oacQosPoliceActionConfigExceedSetValue": oacQosPoliceActionConfigExceedSetValue,
       "oacQosPoliceActionConfigViolate": oacQosPoliceActionConfigViolate,
       "oacQosPoliceActionConfigViolateSetValue": oacQosPoliceActionConfigViolateSetValue,
       "oacQosPoliceStatsTable": oacQosPoliceStatsTable,
       "oacQosPoliceStatsEntry": oacQosPoliceStatsEntry,
       "oacQosPoliceConformPkt": oacQosPoliceConformPkt,
       "oacQosPoliceConformPkt64": oacQosPoliceConformPkt64,
       "oacQosPoliceConformByte": oacQosPoliceConformByte,
       "oacQosPoliceConformByte64": oacQosPoliceConformByte64,
       "oacQosPoliceConformBitRate": oacQosPoliceConformBitRate,
       "oacQosPoliceExceedPkt": oacQosPoliceExceedPkt,
       "oacQosPoliceExceedPkt64": oacQosPoliceExceedPkt64,
       "oacQosPoliceExceedByte": oacQosPoliceExceedByte,
       "oacQosPoliceExceedByte64": oacQosPoliceExceedByte64,
       "oacQosPoliceExceedBitRate": oacQosPoliceExceedBitRate,
       "oacQosPoliceViolatePkt": oacQosPoliceViolatePkt,
       "oacQosPoliceViolatePkt64": oacQosPoliceViolatePkt64,
       "oacQosPoliceViolateByte": oacQosPoliceViolateByte,
       "oacQosPoliceViolateByte64": oacQosPoliceViolateByte64,
       "oacQosPoliceViolateBitRate": oacQosPoliceViolateBitRate,
       "oacQosWREDConfigTable": oacQosWREDConfigTable,
       "oacQosWREDConfigEntry": oacQosWREDConfigEntry,
       "oacQosWREDConfigExponentialWeight": oacQosWREDConfigExponentialWeight,
       "oacQosWREDConfigDscpPrecQosGroup": oacQosWREDConfigDscpPrecQosGroup,
       "oacQosWREDConfigECNEnabled": oacQosWREDConfigECNEnabled,
       "oacQosWREDClassConfigTable": oacQosWREDClassConfigTable,
       "oacQosWREDClassConfigEntry": oacQosWREDClassConfigEntry,
       "oacQosWREDValue": oacQosWREDValue,
       "oacQosWREDConfigPktDropProb": oacQosWREDConfigPktDropProb,
       "oacQosWREDClassConfigThresholdUnit": oacQosWREDClassConfigThresholdUnit,
       "oacQosWREDClassConfigMinThreshold": oacQosWREDClassConfigMinThreshold,
       "oacQosWREDClassConfigMaxThreshold": oacQosWREDClassConfigMaxThreshold,
       "oacQosWREDClassStatsTable": oacQosWREDClassStatsTable,
       "oacQosWREDClassStatsEntry": oacQosWREDClassStatsEntry,
       "oacQosWREDAverageQueueSizeUnits": oacQosWREDAverageQueueSizeUnits,
       "oacQosWREDAverageQueueSize": oacQosWREDAverageQueueSize,
       "oacQosWREDRandomDropPkt": oacQosWREDRandomDropPkt,
       "oacQosWREDRandomDropPkt64": oacQosWREDRandomDropPkt64,
       "oacQosWREDRandomDropByte": oacQosWREDRandomDropByte,
       "oacQosWREDRandomDropByte64": oacQosWREDRandomDropByte64,
       "oacQosWREDTailDropPkt": oacQosWREDTailDropPkt,
       "oacQosWREDTailDropPkt64": oacQosWREDTailDropPkt64,
       "oacQosWREDTailDropByte": oacQosWREDTailDropByte,
       "oacQosWREDTailDropByte64": oacQosWREDTailDropByte64,
       "oacQosWREDTransmitPkt": oacQosWREDTransmitPkt,
       "oacQosWREDTransmitPkt64": oacQosWREDTransmitPkt64,
       "oacQosWREDTransmitByte": oacQosWREDTransmitByte,
       "oacQosWREDTransmitByte64": oacQosWREDTransmitByte64,
       "oacQosWREDECNMarkPkt": oacQosWREDECNMarkPkt,
       "oacQosWREDECNMarkPkt64": oacQosWREDECNMarkPkt64,
       "oacQosWREDECNMarkByte": oacQosWREDECNMarkByte,
       "oacQosWREDECNMarkByte64": oacQosWREDECNMarkByte64,
       "oacQosQueueConfigTable": oacQosQueueConfigTable,
       "oacQosQueueConfigEntry": oacQosQueueConfigEntry,
       "oacQosQueueConfigFlowBasedEnabled": oacQosQueueConfigFlowBasedEnabled,
       "oacQosQueueConfigPriorityEnabled": oacQosQueueConfigPriorityEnabled,
       "oacQosQueueConfigBandwidth": oacQosQueueConfigBandwidth,
       "oacQosQueueConfigBandwidthUnits": oacQosQueueConfigBandwidthUnits,
       "oacQosQueueConfigFlowBasedQSize": oacQosQueueConfigFlowBasedQSize,
       "oacQosQueueConfigFlowBasedQNumber": oacQosQueueConfigFlowBasedQNumber,
       "oacQosQueueConfigPrioBurstSize": oacQosQueueConfigPrioBurstSize,
       "oacQosQueueConfigQueueLimitUnits": oacQosQueueConfigQueueLimitUnits,
       "oacQosQueueConfigQueueLimit": oacQosQueueConfigQueueLimit,
       "oacQosQueueStatsTable": oacQosQueueStatsTable,
       "oacQosQueueStatsEntry": oacQosQueueStatsEntry,
       "oacQosQueueDiscardByte": oacQosQueueDiscardByte,
       "oacQosQueueDiscardByte64": oacQosQueueDiscardByte64,
       "oacQosQueueDiscardPkt": oacQosQueueDiscardPkt,
       "oacQosQueueDiscardPkt64": oacQosQueueDiscardPkt64,
       "oacQosQueueCurrentQDepth": oacQosQueueCurrentQDepth,
       "oacQosQueueMaxQDepth": oacQosQueueMaxQDepth}
)
