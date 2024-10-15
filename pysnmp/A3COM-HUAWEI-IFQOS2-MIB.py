# SNMP MIB module (A3COM-HUAWEI-IFQOS2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-IFQOS2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:06 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cIfQos2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CarAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("continue", 2),
          ("discard", 3),
          ("invalid", 0),
          ("pass", 1),
          ("remark", 4),
          ("remark-atm-clp-continue", 13),
          ("remark-atm-clp-pass", 14),
          ("remark-dot1p-continue", 11),
          ("remark-dot1p-pass", 12),
          ("remark-dscp-continue", 9),
          ("remark-dscp-pass", 10),
          ("remark-fr-de-continue", 15),
          ("remark-fr-de-pass", 16),
          ("remark-ip-continue", 5),
          ("remark-ip-pass", 6),
          ("remark-mplsexp-continue", 7),
          ("remark-mplsexp-pass", 8))
    )



class PriorityQueue(Integer32, TextualConvention):
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
        *(("bottom", 4),
          ("middle", 2),
          ("normal", 3),
          ("top", 1))
    )



class Direction(Integer32, TextualConvention):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_H3cQos2_ObjectIdentity = ObjectIdentity
h3cQos2 = _H3cQos2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65)
)
_H3cIfQoSHardwareQueueObjects_ObjectIdentity = ObjectIdentity
h3cIfQoSHardwareQueueObjects = _H3cIfQoSHardwareQueueObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1)
)
_H3cIfQoSHardwareQueueConfigGroup_ObjectIdentity = ObjectIdentity
h3cIfQoSHardwareQueueConfigGroup = _H3cIfQoSHardwareQueueConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 1)
)
_H3cIfQoSQSModeTable_Object = MibTable
h3cIfQoSQSModeTable = _H3cIfQoSQSModeTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cIfQoSQSModeTable.setStatus("current")
_H3cIfQoSQSModeEntry_Object = MibTableRow
h3cIfQoSQSModeEntry = _H3cIfQoSQSModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 1, 1, 1)
)
h3cIfQoSQSModeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cIfQoSQSModeEntry.setStatus("current")


class _H3cIfQoSQSMode_Type(Integer32):
    """Custom type h3cIfQoSQSMode based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("byteCountWfq", 9),
          ("byteCountWrr", 8),
          ("hwfq", 6),
          ("sp", 1),
          ("sp0", 2),
          ("sp1", 3),
          ("sp2", 4),
          ("wrr", 5),
          ("wrr-sp", 7))
    )


_H3cIfQoSQSMode_Type.__name__ = "Integer32"
_H3cIfQoSQSMode_Object = MibTableColumn
h3cIfQoSQSMode = _H3cIfQoSQSMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 1, 1, 1, 1),
    _H3cIfQoSQSMode_Type()
)
h3cIfQoSQSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfQoSQSMode.setStatus("current")
_H3cIfQoSQSWeightTable_Object = MibTable
h3cIfQoSQSWeightTable = _H3cIfQoSQSWeightTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    h3cIfQoSQSWeightTable.setStatus("current")
_H3cIfQoSQSWeightEntry_Object = MibTableRow
h3cIfQoSQSWeightEntry = _H3cIfQoSQSWeightEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 1, 2, 1)
)
h3cIfQoSQSWeightEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSQueueID"),
)
if mibBuilder.loadTexts:
    h3cIfQoSQSWeightEntry.setStatus("current")
_H3cIfQoSQueueID_Type = Integer32
_H3cIfQoSQueueID_Object = MibTableColumn
h3cIfQoSQueueID = _H3cIfQoSQueueID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 1, 2, 1, 1),
    _H3cIfQoSQueueID_Type()
)
h3cIfQoSQueueID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfQoSQueueID.setStatus("current")


class _H3cIfQoSQueueGroupType_Type(Integer32):
    """Custom type h3cIfQoSQueueGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("group0", 1),
          ("group1", 2),
          ("group2", 3))
    )


_H3cIfQoSQueueGroupType_Type.__name__ = "Integer32"
_H3cIfQoSQueueGroupType_Object = MibTableColumn
h3cIfQoSQueueGroupType = _H3cIfQoSQueueGroupType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 1, 2, 1, 2),
    _H3cIfQoSQueueGroupType_Type()
)
h3cIfQoSQueueGroupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfQoSQueueGroupType.setStatus("current")


class _H3cIfQoSQSType_Type(Integer32):
    """Custom type h3cIfQoSQSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("byte-count", 2),
          ("weight", 1))
    )


_H3cIfQoSQSType_Type.__name__ = "Integer32"
_H3cIfQoSQSType_Object = MibTableColumn
h3cIfQoSQSType = _H3cIfQoSQSType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 1, 2, 1, 3),
    _H3cIfQoSQSType_Type()
)
h3cIfQoSQSType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfQoSQSType.setStatus("current")
_H3cIfQoSQSValue_Type = Integer32
_H3cIfQoSQSValue_Object = MibTableColumn
h3cIfQoSQSValue = _H3cIfQoSQSValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 1, 2, 1, 4),
    _H3cIfQoSQSValue_Type()
)
h3cIfQoSQSValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfQoSQSValue.setStatus("current")


class _H3cIfQoSQSMaxDelay_Type(Integer32):
    """Custom type h3cIfQoSQSMaxDelay based on Integer32"""
    defaultValue = 9


_H3cIfQoSQSMaxDelay_Object = MibTableColumn
h3cIfQoSQSMaxDelay = _H3cIfQoSQSMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 1, 2, 1, 5),
    _H3cIfQoSQSMaxDelay_Type()
)
h3cIfQoSQSMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfQoSQSMaxDelay.setStatus("current")
_H3cIfQoSQSMinBandwidth_Type = Integer32
_H3cIfQoSQSMinBandwidth_Object = MibTableColumn
h3cIfQoSQSMinBandwidth = _H3cIfQoSQSMinBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 1, 2, 1, 6),
    _H3cIfQoSQSMinBandwidth_Type()
)
h3cIfQoSQSMinBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfQoSQSMinBandwidth.setStatus("current")
_H3cIfQoSHardwareQueueRunInfoGroup_ObjectIdentity = ObjectIdentity
h3cIfQoSHardwareQueueRunInfoGroup = _H3cIfQoSHardwareQueueRunInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2)
)
_H3cIfQoSHardwareQueueRunInfoTable_Object = MibTable
h3cIfQoSHardwareQueueRunInfoTable = _H3cIfQoSHardwareQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3cIfQoSHardwareQueueRunInfoTable.setStatus("current")
_H3cIfQoSHardwareQueueRunInfoEntry_Object = MibTableRow
h3cIfQoSHardwareQueueRunInfoEntry = _H3cIfQoSHardwareQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 1, 1)
)
h3cIfQoSHardwareQueueRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSQueueID"),
)
if mibBuilder.loadTexts:
    h3cIfQoSHardwareQueueRunInfoEntry.setStatus("current")
_H3cIfQoSPassPackets_Type = Counter64
_H3cIfQoSPassPackets_Object = MibTableColumn
h3cIfQoSPassPackets = _H3cIfQoSPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 1, 1, 1),
    _H3cIfQoSPassPackets_Type()
)
h3cIfQoSPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSPassPackets.setStatus("current")
_H3cIfQoSDropPackets_Type = Counter64
_H3cIfQoSDropPackets_Object = MibTableColumn
h3cIfQoSDropPackets = _H3cIfQoSDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 1, 1, 2),
    _H3cIfQoSDropPackets_Type()
)
h3cIfQoSDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSDropPackets.setStatus("current")
_H3cIfQoSPassBytes_Type = Counter64
_H3cIfQoSPassBytes_Object = MibTableColumn
h3cIfQoSPassBytes = _H3cIfQoSPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 1, 1, 3),
    _H3cIfQoSPassBytes_Type()
)
h3cIfQoSPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSPassBytes.setStatus("current")
_H3cIfQoSPassPPS_Type = Unsigned32
_H3cIfQoSPassPPS_Object = MibTableColumn
h3cIfQoSPassPPS = _H3cIfQoSPassPPS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 1, 1, 4),
    _H3cIfQoSPassPPS_Type()
)
h3cIfQoSPassPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSPassPPS.setStatus("current")
_H3cIfQoSPassBPS_Type = Unsigned32
_H3cIfQoSPassBPS_Object = MibTableColumn
h3cIfQoSPassBPS = _H3cIfQoSPassBPS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 1, 1, 5),
    _H3cIfQoSPassBPS_Type()
)
h3cIfQoSPassBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSPassBPS.setStatus("current")
_H3cIfQoSDropBytes_Type = Counter64
_H3cIfQoSDropBytes_Object = MibTableColumn
h3cIfQoSDropBytes = _H3cIfQoSDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 1, 1, 6),
    _H3cIfQoSDropBytes_Type()
)
h3cIfQoSDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSDropBytes.setStatus("current")
_H3cIfQoSQueueLengthInPkts_Type = Unsigned32
_H3cIfQoSQueueLengthInPkts_Object = MibTableColumn
h3cIfQoSQueueLengthInPkts = _H3cIfQoSQueueLengthInPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 1, 1, 7),
    _H3cIfQoSQueueLengthInPkts_Type()
)
h3cIfQoSQueueLengthInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSQueueLengthInPkts.setStatus("current")
_H3cIfQoSQueueLengthInBytes_Type = Unsigned32
_H3cIfQoSQueueLengthInBytes_Object = MibTableColumn
h3cIfQoSQueueLengthInBytes = _H3cIfQoSQueueLengthInBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 1, 1, 8),
    _H3cIfQoSQueueLengthInBytes_Type()
)
h3cIfQoSQueueLengthInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSQueueLengthInBytes.setStatus("current")
_H3cIfQoSCurQueuePkts_Type = Unsigned32
_H3cIfQoSCurQueuePkts_Object = MibTableColumn
h3cIfQoSCurQueuePkts = _H3cIfQoSCurQueuePkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 1, 1, 9),
    _H3cIfQoSCurQueuePkts_Type()
)
h3cIfQoSCurQueuePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSCurQueuePkts.setStatus("current")
_H3cIfQoSCurQueueBytes_Type = Unsigned32
_H3cIfQoSCurQueueBytes_Object = MibTableColumn
h3cIfQoSCurQueueBytes = _H3cIfQoSCurQueueBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 1, 1, 10),
    _H3cIfQoSCurQueueBytes_Type()
)
h3cIfQoSCurQueueBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSCurQueueBytes.setStatus("current")
_H3cIfQoSCurQueuePPS_Type = Unsigned32
_H3cIfQoSCurQueuePPS_Object = MibTableColumn
h3cIfQoSCurQueuePPS = _H3cIfQoSCurQueuePPS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 1, 1, 11),
    _H3cIfQoSCurQueuePPS_Type()
)
h3cIfQoSCurQueuePPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSCurQueuePPS.setStatus("current")
_H3cIfQoSCurQueueBPS_Type = Unsigned32
_H3cIfQoSCurQueueBPS_Object = MibTableColumn
h3cIfQoSCurQueueBPS = _H3cIfQoSCurQueueBPS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 1, 1, 12),
    _H3cIfQoSCurQueueBPS_Type()
)
h3cIfQoSCurQueueBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSCurQueueBPS.setStatus("current")
_H3cIfQoSTailDropPkts_Type = Counter64
_H3cIfQoSTailDropPkts_Object = MibTableColumn
h3cIfQoSTailDropPkts = _H3cIfQoSTailDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 1, 1, 13),
    _H3cIfQoSTailDropPkts_Type()
)
h3cIfQoSTailDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSTailDropPkts.setStatus("current")
_H3cIfQoSTailDropBytes_Type = Counter64
_H3cIfQoSTailDropBytes_Object = MibTableColumn
h3cIfQoSTailDropBytes = _H3cIfQoSTailDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 1, 1, 14),
    _H3cIfQoSTailDropBytes_Type()
)
h3cIfQoSTailDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSTailDropBytes.setStatus("current")
_H3cIfQoSTailDropPPS_Type = Unsigned32
_H3cIfQoSTailDropPPS_Object = MibTableColumn
h3cIfQoSTailDropPPS = _H3cIfQoSTailDropPPS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 1, 1, 15),
    _H3cIfQoSTailDropPPS_Type()
)
h3cIfQoSTailDropPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSTailDropPPS.setStatus("current")
_H3cIfQoSTailDropBPS_Type = Unsigned32
_H3cIfQoSTailDropBPS_Object = MibTableColumn
h3cIfQoSTailDropBPS = _H3cIfQoSTailDropBPS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 1, 1, 16),
    _H3cIfQoSTailDropBPS_Type()
)
h3cIfQoSTailDropBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSTailDropBPS.setStatus("current")
_H3cIfQoSWredDropPkts_Type = Counter64
_H3cIfQoSWredDropPkts_Object = MibTableColumn
h3cIfQoSWredDropPkts = _H3cIfQoSWredDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 1, 1, 17),
    _H3cIfQoSWredDropPkts_Type()
)
h3cIfQoSWredDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWredDropPkts.setStatus("current")
_H3cIfQoSWredDropBytes_Type = Counter64
_H3cIfQoSWredDropBytes_Object = MibTableColumn
h3cIfQoSWredDropBytes = _H3cIfQoSWredDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 1, 1, 18),
    _H3cIfQoSWredDropBytes_Type()
)
h3cIfQoSWredDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWredDropBytes.setStatus("current")
_H3cIfQoSWredDropPPS_Type = Unsigned32
_H3cIfQoSWredDropPPS_Object = MibTableColumn
h3cIfQoSWredDropPPS = _H3cIfQoSWredDropPPS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 1, 1, 19),
    _H3cIfQoSWredDropPPS_Type()
)
h3cIfQoSWredDropPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWredDropPPS.setStatus("current")
_H3cIfQoSWredDropBPS_Type = Unsigned32
_H3cIfQoSWredDropBPS_Object = MibTableColumn
h3cIfQoSWredDropBPS = _H3cIfQoSWredDropBPS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 1, 1, 20),
    _H3cIfQoSWredDropBPS_Type()
)
h3cIfQoSWredDropBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWredDropBPS.setStatus("current")
_H3cIfQoSHQueueTcpRunInfoTable_Object = MibTable
h3cIfQoSHQueueTcpRunInfoTable = _H3cIfQoSHQueueTcpRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    h3cIfQoSHQueueTcpRunInfoTable.setStatus("current")
_H3cIfQoSHQueueTcpRunInfoEntry_Object = MibTableRow
h3cIfQoSHQueueTcpRunInfoEntry = _H3cIfQoSHQueueTcpRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 2, 1)
)
h3cIfQoSHQueueTcpRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSQueueID"),
)
if mibBuilder.loadTexts:
    h3cIfQoSHQueueTcpRunInfoEntry.setStatus("current")
_H3cIfQoSWredDropLPreNTcpPkts_Type = Counter64
_H3cIfQoSWredDropLPreNTcpPkts_Object = MibTableColumn
h3cIfQoSWredDropLPreNTcpPkts = _H3cIfQoSWredDropLPreNTcpPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 2, 1, 1),
    _H3cIfQoSWredDropLPreNTcpPkts_Type()
)
h3cIfQoSWredDropLPreNTcpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWredDropLPreNTcpPkts.setStatus("current")
_H3cIfQoSWredDropLPreNTcpBytes_Type = Counter64
_H3cIfQoSWredDropLPreNTcpBytes_Object = MibTableColumn
h3cIfQoSWredDropLPreNTcpBytes = _H3cIfQoSWredDropLPreNTcpBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 2, 1, 2),
    _H3cIfQoSWredDropLPreNTcpBytes_Type()
)
h3cIfQoSWredDropLPreNTcpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWredDropLPreNTcpBytes.setStatus("current")
_H3cIfQoSWredDropLPreNTcpPPS_Type = Unsigned32
_H3cIfQoSWredDropLPreNTcpPPS_Object = MibTableColumn
h3cIfQoSWredDropLPreNTcpPPS = _H3cIfQoSWredDropLPreNTcpPPS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 2, 1, 3),
    _H3cIfQoSWredDropLPreNTcpPPS_Type()
)
h3cIfQoSWredDropLPreNTcpPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWredDropLPreNTcpPPS.setStatus("current")
_H3cIfQoSWredDropLPreNTcpBPS_Type = Unsigned32
_H3cIfQoSWredDropLPreNTcpBPS_Object = MibTableColumn
h3cIfQoSWredDropLPreNTcpBPS = _H3cIfQoSWredDropLPreNTcpBPS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 2, 1, 4),
    _H3cIfQoSWredDropLPreNTcpBPS_Type()
)
h3cIfQoSWredDropLPreNTcpBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWredDropLPreNTcpBPS.setStatus("current")
_H3cIfQoSWredDropLPreTcpPkts_Type = Counter64
_H3cIfQoSWredDropLPreTcpPkts_Object = MibTableColumn
h3cIfQoSWredDropLPreTcpPkts = _H3cIfQoSWredDropLPreTcpPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 2, 1, 5),
    _H3cIfQoSWredDropLPreTcpPkts_Type()
)
h3cIfQoSWredDropLPreTcpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWredDropLPreTcpPkts.setStatus("current")
_H3cIfQoSWredDropLPreTcpBytes_Type = Counter64
_H3cIfQoSWredDropLPreTcpBytes_Object = MibTableColumn
h3cIfQoSWredDropLPreTcpBytes = _H3cIfQoSWredDropLPreTcpBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 2, 1, 6),
    _H3cIfQoSWredDropLPreTcpBytes_Type()
)
h3cIfQoSWredDropLPreTcpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWredDropLPreTcpBytes.setStatus("current")
_H3cIfQoSWredDropLPreTcpPPS_Type = Unsigned32
_H3cIfQoSWredDropLPreTcpPPS_Object = MibTableColumn
h3cIfQoSWredDropLPreTcpPPS = _H3cIfQoSWredDropLPreTcpPPS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 2, 1, 7),
    _H3cIfQoSWredDropLPreTcpPPS_Type()
)
h3cIfQoSWredDropLPreTcpPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWredDropLPreTcpPPS.setStatus("current")
_H3cIfQoSWredDropLPreTcpBPS_Type = Unsigned32
_H3cIfQoSWredDropLPreTcpBPS_Object = MibTableColumn
h3cIfQoSWredDropLPreTcpBPS = _H3cIfQoSWredDropLPreTcpBPS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 2, 1, 8),
    _H3cIfQoSWredDropLPreTcpBPS_Type()
)
h3cIfQoSWredDropLPreTcpBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWredDropLPreTcpBPS.setStatus("current")
_H3cIfQoSWredDropHPreNTcpPkts_Type = Counter64
_H3cIfQoSWredDropHPreNTcpPkts_Object = MibTableColumn
h3cIfQoSWredDropHPreNTcpPkts = _H3cIfQoSWredDropHPreNTcpPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 2, 1, 9),
    _H3cIfQoSWredDropHPreNTcpPkts_Type()
)
h3cIfQoSWredDropHPreNTcpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWredDropHPreNTcpPkts.setStatus("current")
_H3cIfQoSWredDropHPreNTcpBytes_Type = Counter64
_H3cIfQoSWredDropHPreNTcpBytes_Object = MibTableColumn
h3cIfQoSWredDropHPreNTcpBytes = _H3cIfQoSWredDropHPreNTcpBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 2, 1, 10),
    _H3cIfQoSWredDropHPreNTcpBytes_Type()
)
h3cIfQoSWredDropHPreNTcpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWredDropHPreNTcpBytes.setStatus("current")
_H3cIfQoSWredDropHPreNTcpPPS_Type = Unsigned32
_H3cIfQoSWredDropHPreNTcpPPS_Object = MibTableColumn
h3cIfQoSWredDropHPreNTcpPPS = _H3cIfQoSWredDropHPreNTcpPPS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 2, 1, 11),
    _H3cIfQoSWredDropHPreNTcpPPS_Type()
)
h3cIfQoSWredDropHPreNTcpPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWredDropHPreNTcpPPS.setStatus("current")
_H3cIfQoSWredDropHPreNTcpBPS_Type = Unsigned32
_H3cIfQoSWredDropHPreNTcpBPS_Object = MibTableColumn
h3cIfQoSWredDropHPreNTcpBPS = _H3cIfQoSWredDropHPreNTcpBPS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 2, 1, 12),
    _H3cIfQoSWredDropHPreNTcpBPS_Type()
)
h3cIfQoSWredDropHPreNTcpBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWredDropHPreNTcpBPS.setStatus("current")
_H3cIfQoSWredDropHPreTcpPkts_Type = Counter64
_H3cIfQoSWredDropHPreTcpPkts_Object = MibTableColumn
h3cIfQoSWredDropHPreTcpPkts = _H3cIfQoSWredDropHPreTcpPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 2, 1, 13),
    _H3cIfQoSWredDropHPreTcpPkts_Type()
)
h3cIfQoSWredDropHPreTcpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWredDropHPreTcpPkts.setStatus("current")
_H3cIfQoSWredDropHPreTcpBytes_Type = Counter64
_H3cIfQoSWredDropHPreTcpBytes_Object = MibTableColumn
h3cIfQoSWredDropHPreTcpBytes = _H3cIfQoSWredDropHPreTcpBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 2, 1, 14),
    _H3cIfQoSWredDropHPreTcpBytes_Type()
)
h3cIfQoSWredDropHPreTcpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWredDropHPreTcpBytes.setStatus("current")
_H3cIfQoSWredDropHPreTcpPPS_Type = Unsigned32
_H3cIfQoSWredDropHPreTcpPPS_Object = MibTableColumn
h3cIfQoSWredDropHPreTcpPPS = _H3cIfQoSWredDropHPreTcpPPS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 2, 1, 15),
    _H3cIfQoSWredDropHPreTcpPPS_Type()
)
h3cIfQoSWredDropHPreTcpPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWredDropHPreTcpPPS.setStatus("current")
_H3cIfQoSWredDropHPreTcpBPS_Type = Unsigned32
_H3cIfQoSWredDropHPreTcpBPS_Object = MibTableColumn
h3cIfQoSWredDropHPreTcpBPS = _H3cIfQoSWredDropHPreTcpBPS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 1, 2, 2, 1, 16),
    _H3cIfQoSWredDropHPreTcpBPS_Type()
)
h3cIfQoSWredDropHPreTcpBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWredDropHPreTcpBPS.setStatus("current")
_H3cIfQoSSoftwareQueueObjects_ObjectIdentity = ObjectIdentity
h3cIfQoSSoftwareQueueObjects = _H3cIfQoSSoftwareQueueObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2)
)
_H3cIfQoSFIFOObject_ObjectIdentity = ObjectIdentity
h3cIfQoSFIFOObject = _H3cIfQoSFIFOObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 1)
)
_H3cIfQoSFIFOConfigTable_Object = MibTable
h3cIfQoSFIFOConfigTable = _H3cIfQoSFIFOConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    h3cIfQoSFIFOConfigTable.setStatus("current")
_H3cIfQoSFIFOConfigEntry_Object = MibTableRow
h3cIfQoSFIFOConfigEntry = _H3cIfQoSFIFOConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 1, 1, 1)
)
h3cIfQoSFIFOConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cIfQoSFIFOConfigEntry.setStatus("current")
_H3cIfQoSFIFOMaxQueueLen_Type = Integer32
_H3cIfQoSFIFOMaxQueueLen_Object = MibTableColumn
h3cIfQoSFIFOMaxQueueLen = _H3cIfQoSFIFOMaxQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 1, 1, 1, 1),
    _H3cIfQoSFIFOMaxQueueLen_Type()
)
h3cIfQoSFIFOMaxQueueLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfQoSFIFOMaxQueueLen.setStatus("current")
_H3cIfQoSFIFORunInfoTable_Object = MibTable
h3cIfQoSFIFORunInfoTable = _H3cIfQoSFIFORunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    h3cIfQoSFIFORunInfoTable.setStatus("current")
_H3cIfQoSFIFORunInfoEntry_Object = MibTableRow
h3cIfQoSFIFORunInfoEntry = _H3cIfQoSFIFORunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 1, 2, 1)
)
h3cIfQoSFIFORunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cIfQoSFIFORunInfoEntry.setStatus("current")
_H3cIfQoSFIFOSize_Type = Integer32
_H3cIfQoSFIFOSize_Object = MibTableColumn
h3cIfQoSFIFOSize = _H3cIfQoSFIFOSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 1, 2, 1, 1),
    _H3cIfQoSFIFOSize_Type()
)
h3cIfQoSFIFOSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSFIFOSize.setStatus("current")
_H3cIfQoSFIFODiscardPackets_Type = Counter64
_H3cIfQoSFIFODiscardPackets_Object = MibTableColumn
h3cIfQoSFIFODiscardPackets = _H3cIfQoSFIFODiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 1, 2, 1, 2),
    _H3cIfQoSFIFODiscardPackets_Type()
)
h3cIfQoSFIFODiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSFIFODiscardPackets.setStatus("current")
_H3cIfQoSPQObject_ObjectIdentity = ObjectIdentity
h3cIfQoSPQObject = _H3cIfQoSPQObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 2)
)
_H3cIfQoSPQConfigGroup_ObjectIdentity = ObjectIdentity
h3cIfQoSPQConfigGroup = _H3cIfQoSPQConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 2, 1)
)
_H3cIfQoSPQDefaultTable_Object = MibTable
h3cIfQoSPQDefaultTable = _H3cIfQoSPQDefaultTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    h3cIfQoSPQDefaultTable.setStatus("current")
_H3cIfQoSPQDefaultEntry_Object = MibTableRow
h3cIfQoSPQDefaultEntry = _H3cIfQoSPQDefaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 2, 1, 1, 1)
)
h3cIfQoSPQDefaultEntry.setIndexNames(
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSPQListNumber"),
)
if mibBuilder.loadTexts:
    h3cIfQoSPQDefaultEntry.setStatus("current")


class _H3cIfQoSPQListNumber_Type(Integer32):
    """Custom type h3cIfQoSPQListNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cIfQoSPQListNumber_Type.__name__ = "Integer32"
_H3cIfQoSPQListNumber_Object = MibTableColumn
h3cIfQoSPQListNumber = _H3cIfQoSPQListNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 2, 1, 1, 1, 1),
    _H3cIfQoSPQListNumber_Type()
)
h3cIfQoSPQListNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfQoSPQListNumber.setStatus("current")
_H3cIfQoSPQDefaultQueueType_Type = PriorityQueue
_H3cIfQoSPQDefaultQueueType_Object = MibTableColumn
h3cIfQoSPQDefaultQueueType = _H3cIfQoSPQDefaultQueueType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 2, 1, 1, 1, 2),
    _H3cIfQoSPQDefaultQueueType_Type()
)
h3cIfQoSPQDefaultQueueType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfQoSPQDefaultQueueType.setStatus("current")
_H3cIfQoSPQQueueLengthTable_Object = MibTable
h3cIfQoSPQQueueLengthTable = _H3cIfQoSPQQueueLengthTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    h3cIfQoSPQQueueLengthTable.setStatus("current")
_H3cIfQoSPQQueueLengthEntry_Object = MibTableRow
h3cIfQoSPQQueueLengthEntry = _H3cIfQoSPQQueueLengthEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 2, 1, 2, 1)
)
h3cIfQoSPQQueueLengthEntry.setIndexNames(
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSPQListNumber"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSPQQueueLengthType"),
)
if mibBuilder.loadTexts:
    h3cIfQoSPQQueueLengthEntry.setStatus("current")
_H3cIfQoSPQQueueLengthType_Type = PriorityQueue
_H3cIfQoSPQQueueLengthType_Object = MibTableColumn
h3cIfQoSPQQueueLengthType = _H3cIfQoSPQQueueLengthType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 2, 1, 2, 1, 1),
    _H3cIfQoSPQQueueLengthType_Type()
)
h3cIfQoSPQQueueLengthType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfQoSPQQueueLengthType.setStatus("current")


class _H3cIfQoSPQQueueLengthValue_Type(Integer32):
    """Custom type h3cIfQoSPQQueueLengthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_H3cIfQoSPQQueueLengthValue_Type.__name__ = "Integer32"
_H3cIfQoSPQQueueLengthValue_Object = MibTableColumn
h3cIfQoSPQQueueLengthValue = _H3cIfQoSPQQueueLengthValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 2, 1, 2, 1, 2),
    _H3cIfQoSPQQueueLengthValue_Type()
)
h3cIfQoSPQQueueLengthValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfQoSPQQueueLengthValue.setStatus("current")
_H3cIfQoSPQClassRuleTable_Object = MibTable
h3cIfQoSPQClassRuleTable = _H3cIfQoSPQClassRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    h3cIfQoSPQClassRuleTable.setStatus("current")
_H3cIfQoSPQClassRuleEntry_Object = MibTableRow
h3cIfQoSPQClassRuleEntry = _H3cIfQoSPQClassRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 2, 1, 3, 1)
)
h3cIfQoSPQClassRuleEntry.setIndexNames(
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSPQListNumber"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSPQClassRuleType"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSPQClassRuleValue"),
)
if mibBuilder.loadTexts:
    h3cIfQoSPQClassRuleEntry.setStatus("current")


class _H3cIfQoSPQClassRuleType_Type(Integer32):
    """Custom type h3cIfQoSPQClassRuleType based on Integer32"""
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
        *(("fragments", 4),
          ("greater-than", 5),
          ("interface", 1),
          ("ipall", 9),
          ("ipv4acl", 2),
          ("ipv6acl", 3),
          ("less-than", 6),
          ("mpls", 10),
          ("tcp", 7),
          ("udp", 8))
    )


_H3cIfQoSPQClassRuleType_Type.__name__ = "Integer32"
_H3cIfQoSPQClassRuleType_Object = MibTableColumn
h3cIfQoSPQClassRuleType = _H3cIfQoSPQClassRuleType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 2, 1, 3, 1, 1),
    _H3cIfQoSPQClassRuleType_Type()
)
h3cIfQoSPQClassRuleType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfQoSPQClassRuleType.setStatus("current")
_H3cIfQoSPQClassRuleValue_Type = Integer32
_H3cIfQoSPQClassRuleValue_Object = MibTableColumn
h3cIfQoSPQClassRuleValue = _H3cIfQoSPQClassRuleValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 2, 1, 3, 1, 2),
    _H3cIfQoSPQClassRuleValue_Type()
)
h3cIfQoSPQClassRuleValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfQoSPQClassRuleValue.setStatus("current")
_H3cIfQoSPQClassRuleQueueType_Type = PriorityQueue
_H3cIfQoSPQClassRuleQueueType_Object = MibTableColumn
h3cIfQoSPQClassRuleQueueType = _H3cIfQoSPQClassRuleQueueType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 2, 1, 3, 1, 3),
    _H3cIfQoSPQClassRuleQueueType_Type()
)
h3cIfQoSPQClassRuleQueueType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSPQClassRuleQueueType.setStatus("current")
_H3cIfQoSPQClassRowStatus_Type = RowStatus
_H3cIfQoSPQClassRowStatus_Object = MibTableColumn
h3cIfQoSPQClassRowStatus = _H3cIfQoSPQClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 2, 1, 3, 1, 4),
    _H3cIfQoSPQClassRowStatus_Type()
)
h3cIfQoSPQClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSPQClassRowStatus.setStatus("current")
_H3cIfQoSPQApplyTable_Object = MibTable
h3cIfQoSPQApplyTable = _H3cIfQoSPQApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 2, 1, 4)
)
if mibBuilder.loadTexts:
    h3cIfQoSPQApplyTable.setStatus("current")
_H3cIfQoSPQApplyEntry_Object = MibTableRow
h3cIfQoSPQApplyEntry = _H3cIfQoSPQApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 2, 1, 4, 1)
)
h3cIfQoSPQApplyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cIfQoSPQApplyEntry.setStatus("current")


class _H3cIfQoSPQApplyListNumber_Type(Integer32):
    """Custom type h3cIfQoSPQApplyListNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cIfQoSPQApplyListNumber_Type.__name__ = "Integer32"
_H3cIfQoSPQApplyListNumber_Object = MibTableColumn
h3cIfQoSPQApplyListNumber = _H3cIfQoSPQApplyListNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 2, 1, 4, 1, 1),
    _H3cIfQoSPQApplyListNumber_Type()
)
h3cIfQoSPQApplyListNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSPQApplyListNumber.setStatus("current")
_H3cIfQoSPQApplyRowStatus_Type = RowStatus
_H3cIfQoSPQApplyRowStatus_Object = MibTableColumn
h3cIfQoSPQApplyRowStatus = _H3cIfQoSPQApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 2, 1, 4, 1, 2),
    _H3cIfQoSPQApplyRowStatus_Type()
)
h3cIfQoSPQApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSPQApplyRowStatus.setStatus("current")
_H3cIfQoSPQRunInfoGroup_ObjectIdentity = ObjectIdentity
h3cIfQoSPQRunInfoGroup = _H3cIfQoSPQRunInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 2, 2)
)
_H3cIfQoSPQRunInfoTable_Object = MibTable
h3cIfQoSPQRunInfoTable = _H3cIfQoSPQRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    h3cIfQoSPQRunInfoTable.setStatus("current")
_H3cIfQoSPQRunInfoEntry_Object = MibTableRow
h3cIfQoSPQRunInfoEntry = _H3cIfQoSPQRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 2, 2, 1, 1)
)
h3cIfQoSPQRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSPQType"),
)
if mibBuilder.loadTexts:
    h3cIfQoSPQRunInfoEntry.setStatus("current")
_H3cIfQoSPQType_Type = PriorityQueue
_H3cIfQoSPQType_Object = MibTableColumn
h3cIfQoSPQType = _H3cIfQoSPQType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 2, 2, 1, 1, 1),
    _H3cIfQoSPQType_Type()
)
h3cIfQoSPQType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfQoSPQType.setStatus("current")
_H3cIfQoSPQSize_Type = Integer32
_H3cIfQoSPQSize_Object = MibTableColumn
h3cIfQoSPQSize = _H3cIfQoSPQSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 2, 2, 1, 1, 2),
    _H3cIfQoSPQSize_Type()
)
h3cIfQoSPQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSPQSize.setStatus("current")
_H3cIfQoSPQLength_Type = Integer32
_H3cIfQoSPQLength_Object = MibTableColumn
h3cIfQoSPQLength = _H3cIfQoSPQLength_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 2, 2, 1, 1, 3),
    _H3cIfQoSPQLength_Type()
)
h3cIfQoSPQLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSPQLength.setStatus("current")
_H3cIfQoSPQDiscardPackets_Type = Counter64
_H3cIfQoSPQDiscardPackets_Object = MibTableColumn
h3cIfQoSPQDiscardPackets = _H3cIfQoSPQDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 2, 2, 1, 1, 4),
    _H3cIfQoSPQDiscardPackets_Type()
)
h3cIfQoSPQDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSPQDiscardPackets.setStatus("current")
_H3cIfQoSCQObject_ObjectIdentity = ObjectIdentity
h3cIfQoSCQObject = _H3cIfQoSCQObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 3)
)
_H3cIfQoSCQConfigGroup_ObjectIdentity = ObjectIdentity
h3cIfQoSCQConfigGroup = _H3cIfQoSCQConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 3, 1)
)
_H3cIfQoSCQDefaultTable_Object = MibTable
h3cIfQoSCQDefaultTable = _H3cIfQoSCQDefaultTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    h3cIfQoSCQDefaultTable.setStatus("current")
_H3cIfQoSCQDefaultEntry_Object = MibTableRow
h3cIfQoSCQDefaultEntry = _H3cIfQoSCQDefaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 3, 1, 1, 1)
)
h3cIfQoSCQDefaultEntry.setIndexNames(
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSCQListNumber"),
)
if mibBuilder.loadTexts:
    h3cIfQoSCQDefaultEntry.setStatus("current")


class _H3cIfQoSCQListNumber_Type(Integer32):
    """Custom type h3cIfQoSCQListNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cIfQoSCQListNumber_Type.__name__ = "Integer32"
_H3cIfQoSCQListNumber_Object = MibTableColumn
h3cIfQoSCQListNumber = _H3cIfQoSCQListNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 3, 1, 1, 1, 1),
    _H3cIfQoSCQListNumber_Type()
)
h3cIfQoSCQListNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfQoSCQListNumber.setStatus("current")


class _H3cIfQoSCQDefaultQueueID_Type(Integer32):
    """Custom type h3cIfQoSCQDefaultQueueID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_H3cIfQoSCQDefaultQueueID_Type.__name__ = "Integer32"
_H3cIfQoSCQDefaultQueueID_Object = MibTableColumn
h3cIfQoSCQDefaultQueueID = _H3cIfQoSCQDefaultQueueID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 3, 1, 1, 1, 2),
    _H3cIfQoSCQDefaultQueueID_Type()
)
h3cIfQoSCQDefaultQueueID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfQoSCQDefaultQueueID.setStatus("current")
_H3cIfQoSCQQueueLengthTable_Object = MibTable
h3cIfQoSCQQueueLengthTable = _H3cIfQoSCQQueueLengthTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    h3cIfQoSCQQueueLengthTable.setStatus("current")
_H3cIfQoSCQQueueLengthEntry_Object = MibTableRow
h3cIfQoSCQQueueLengthEntry = _H3cIfQoSCQQueueLengthEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 3, 1, 2, 1)
)
h3cIfQoSCQQueueLengthEntry.setIndexNames(
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSCQListNumber"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSCQQueueID"),
)
if mibBuilder.loadTexts:
    h3cIfQoSCQQueueLengthEntry.setStatus("current")


class _H3cIfQoSCQQueueID_Type(Integer32):
    """Custom type h3cIfQoSCQQueueID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cIfQoSCQQueueID_Type.__name__ = "Integer32"
_H3cIfQoSCQQueueID_Object = MibTableColumn
h3cIfQoSCQQueueID = _H3cIfQoSCQQueueID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 3, 1, 2, 1, 1),
    _H3cIfQoSCQQueueID_Type()
)
h3cIfQoSCQQueueID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfQoSCQQueueID.setStatus("current")


class _H3cIfQoSCQQueueLength_Type(Integer32):
    """Custom type h3cIfQoSCQQueueLength based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_H3cIfQoSCQQueueLength_Type.__name__ = "Integer32"
_H3cIfQoSCQQueueLength_Object = MibTableColumn
h3cIfQoSCQQueueLength = _H3cIfQoSCQQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 3, 1, 2, 1, 2),
    _H3cIfQoSCQQueueLength_Type()
)
h3cIfQoSCQQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfQoSCQQueueLength.setStatus("current")


class _H3cIfQoSCQQueueServing_Type(Integer32):
    """Custom type h3cIfQoSCQQueueServing based on Integer32"""
    defaultValue = 1500


_H3cIfQoSCQQueueServing_Object = MibTableColumn
h3cIfQoSCQQueueServing = _H3cIfQoSCQQueueServing_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 3, 1, 2, 1, 3),
    _H3cIfQoSCQQueueServing_Type()
)
h3cIfQoSCQQueueServing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfQoSCQQueueServing.setStatus("current")
_H3cIfQoSCQClassRuleTable_Object = MibTable
h3cIfQoSCQClassRuleTable = _H3cIfQoSCQClassRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 3, 1, 3)
)
if mibBuilder.loadTexts:
    h3cIfQoSCQClassRuleTable.setStatus("current")
_H3cIfQoSCQClassRuleEntry_Object = MibTableRow
h3cIfQoSCQClassRuleEntry = _H3cIfQoSCQClassRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 3, 1, 3, 1)
)
h3cIfQoSCQClassRuleEntry.setIndexNames(
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSCQListNumber"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSCQClassRuleType"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSCQClassRuleValue"),
)
if mibBuilder.loadTexts:
    h3cIfQoSCQClassRuleEntry.setStatus("current")


class _H3cIfQoSCQClassRuleType_Type(Integer32):
    """Custom type h3cIfQoSCQClassRuleType based on Integer32"""
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
        *(("fragments", 4),
          ("greater-than", 5),
          ("interface", 1),
          ("ipall", 9),
          ("ipv4acl", 2),
          ("ipv6acl", 3),
          ("less-than", 6),
          ("mpls", 10),
          ("tcp", 7),
          ("udp", 8))
    )


_H3cIfQoSCQClassRuleType_Type.__name__ = "Integer32"
_H3cIfQoSCQClassRuleType_Object = MibTableColumn
h3cIfQoSCQClassRuleType = _H3cIfQoSCQClassRuleType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 3, 1, 3, 1, 1),
    _H3cIfQoSCQClassRuleType_Type()
)
h3cIfQoSCQClassRuleType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfQoSCQClassRuleType.setStatus("current")
_H3cIfQoSCQClassRuleValue_Type = Integer32
_H3cIfQoSCQClassRuleValue_Object = MibTableColumn
h3cIfQoSCQClassRuleValue = _H3cIfQoSCQClassRuleValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 3, 1, 3, 1, 2),
    _H3cIfQoSCQClassRuleValue_Type()
)
h3cIfQoSCQClassRuleValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfQoSCQClassRuleValue.setStatus("current")


class _H3cIfQoSCQClassRuleQueueID_Type(Integer32):
    """Custom type h3cIfQoSCQClassRuleQueueID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cIfQoSCQClassRuleQueueID_Type.__name__ = "Integer32"
_H3cIfQoSCQClassRuleQueueID_Object = MibTableColumn
h3cIfQoSCQClassRuleQueueID = _H3cIfQoSCQClassRuleQueueID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 3, 1, 3, 1, 3),
    _H3cIfQoSCQClassRuleQueueID_Type()
)
h3cIfQoSCQClassRuleQueueID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSCQClassRuleQueueID.setStatus("current")
_H3cIfQoSCQClassRowStatus_Type = RowStatus
_H3cIfQoSCQClassRowStatus_Object = MibTableColumn
h3cIfQoSCQClassRowStatus = _H3cIfQoSCQClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 3, 1, 3, 1, 4),
    _H3cIfQoSCQClassRowStatus_Type()
)
h3cIfQoSCQClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSCQClassRowStatus.setStatus("current")
_H3cIfQoSCQApplyTable_Object = MibTable
h3cIfQoSCQApplyTable = _H3cIfQoSCQApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 3, 1, 4)
)
if mibBuilder.loadTexts:
    h3cIfQoSCQApplyTable.setStatus("current")
_H3cIfQoSCQApplyEntry_Object = MibTableRow
h3cIfQoSCQApplyEntry = _H3cIfQoSCQApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 3, 1, 4, 1)
)
h3cIfQoSCQApplyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cIfQoSCQApplyEntry.setStatus("current")


class _H3cIfQoSCQApplyListNumber_Type(Integer32):
    """Custom type h3cIfQoSCQApplyListNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cIfQoSCQApplyListNumber_Type.__name__ = "Integer32"
_H3cIfQoSCQApplyListNumber_Object = MibTableColumn
h3cIfQoSCQApplyListNumber = _H3cIfQoSCQApplyListNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 3, 1, 4, 1, 1),
    _H3cIfQoSCQApplyListNumber_Type()
)
h3cIfQoSCQApplyListNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSCQApplyListNumber.setStatus("current")
_H3cIfQoSCQApplyRowStatus_Type = RowStatus
_H3cIfQoSCQApplyRowStatus_Object = MibTableColumn
h3cIfQoSCQApplyRowStatus = _H3cIfQoSCQApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 3, 1, 4, 1, 2),
    _H3cIfQoSCQApplyRowStatus_Type()
)
h3cIfQoSCQApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSCQApplyRowStatus.setStatus("current")
_H3cIfQoSCQRunInfoGroup_ObjectIdentity = ObjectIdentity
h3cIfQoSCQRunInfoGroup = _H3cIfQoSCQRunInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 3, 2)
)
_H3cIfQoSCQRunInfoTable_Object = MibTable
h3cIfQoSCQRunInfoTable = _H3cIfQoSCQRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    h3cIfQoSCQRunInfoTable.setStatus("current")
_H3cIfQoSCQRunInfoEntry_Object = MibTableRow
h3cIfQoSCQRunInfoEntry = _H3cIfQoSCQRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 3, 2, 1, 1)
)
h3cIfQoSCQRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSCQQueueID"),
)
if mibBuilder.loadTexts:
    h3cIfQoSCQRunInfoEntry.setStatus("current")
_H3cIfQoSCQRunInfoSize_Type = Integer32
_H3cIfQoSCQRunInfoSize_Object = MibTableColumn
h3cIfQoSCQRunInfoSize = _H3cIfQoSCQRunInfoSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 3, 2, 1, 1, 1),
    _H3cIfQoSCQRunInfoSize_Type()
)
h3cIfQoSCQRunInfoSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSCQRunInfoSize.setStatus("current")
_H3cIfQoSCQRunInfoLength_Type = Integer32
_H3cIfQoSCQRunInfoLength_Object = MibTableColumn
h3cIfQoSCQRunInfoLength = _H3cIfQoSCQRunInfoLength_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 3, 2, 1, 1, 2),
    _H3cIfQoSCQRunInfoLength_Type()
)
h3cIfQoSCQRunInfoLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSCQRunInfoLength.setStatus("current")
_H3cIfQoSCQRunInfoDiscardPackets_Type = Counter64
_H3cIfQoSCQRunInfoDiscardPackets_Object = MibTableColumn
h3cIfQoSCQRunInfoDiscardPackets = _H3cIfQoSCQRunInfoDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 3, 2, 1, 1, 3),
    _H3cIfQoSCQRunInfoDiscardPackets_Type()
)
h3cIfQoSCQRunInfoDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSCQRunInfoDiscardPackets.setStatus("current")
_H3cIfQoSWFQObject_ObjectIdentity = ObjectIdentity
h3cIfQoSWFQObject = _H3cIfQoSWFQObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 4)
)
_H3cIfQoSWFQConfigGroup_ObjectIdentity = ObjectIdentity
h3cIfQoSWFQConfigGroup = _H3cIfQoSWFQConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 4, 1)
)
_H3cIfQoSWFQTable_Object = MibTable
h3cIfQoSWFQTable = _H3cIfQoSWFQTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    h3cIfQoSWFQTable.setStatus("current")
_H3cIfQoSWFQEntry_Object = MibTableRow
h3cIfQoSWFQEntry = _H3cIfQoSWFQEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 4, 1, 1, 1)
)
h3cIfQoSWFQEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cIfQoSWFQEntry.setStatus("current")


class _H3cIfQoSWFQQueueLength_Type(Integer32):
    """Custom type h3cIfQoSWFQQueueLength based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_H3cIfQoSWFQQueueLength_Type.__name__ = "Integer32"
_H3cIfQoSWFQQueueLength_Object = MibTableColumn
h3cIfQoSWFQQueueLength = _H3cIfQoSWFQQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 4, 1, 1, 1, 1),
    _H3cIfQoSWFQQueueLength_Type()
)
h3cIfQoSWFQQueueLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSWFQQueueLength.setStatus("current")


class _H3cIfQoSWFQQueueNumber_Type(Integer32):
    """Custom type h3cIfQoSWFQQueueNumber based on Integer32"""
    defaultValue = 5

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
              9)
        )
    )
    namedValues = NamedValues(
        *(("size1024", 7),
          ("size128", 4),
          ("size16", 1),
          ("size2048", 8),
          ("size256", 5),
          ("size32", 2),
          ("size4096", 9),
          ("size512", 6),
          ("size64", 3))
    )


_H3cIfQoSWFQQueueNumber_Type.__name__ = "Integer32"
_H3cIfQoSWFQQueueNumber_Object = MibTableColumn
h3cIfQoSWFQQueueNumber = _H3cIfQoSWFQQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 4, 1, 1, 1, 2),
    _H3cIfQoSWFQQueueNumber_Type()
)
h3cIfQoSWFQQueueNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSWFQQueueNumber.setStatus("current")
_H3cIfQoSWFQRowStatus_Type = RowStatus
_H3cIfQoSWFQRowStatus_Object = MibTableColumn
h3cIfQoSWFQRowStatus = _H3cIfQoSWFQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 4, 1, 1, 1, 3),
    _H3cIfQoSWFQRowStatus_Type()
)
h3cIfQoSWFQRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSWFQRowStatus.setStatus("current")


class _H3cIfQoSWFQType_Type(Integer32):
    """Custom type h3cIfQoSWFQType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dscp", 2),
          ("ip-precedence", 1))
    )


_H3cIfQoSWFQType_Type.__name__ = "Integer32"
_H3cIfQoSWFQType_Object = MibTableColumn
h3cIfQoSWFQType = _H3cIfQoSWFQType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 4, 1, 1, 1, 4),
    _H3cIfQoSWFQType_Type()
)
h3cIfQoSWFQType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSWFQType.setStatus("current")
_H3cIfQoSWFQRunInfoGroup_ObjectIdentity = ObjectIdentity
h3cIfQoSWFQRunInfoGroup = _H3cIfQoSWFQRunInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 4, 2)
)
_H3cIfQoSWFQRunInfoTable_Object = MibTable
h3cIfQoSWFQRunInfoTable = _H3cIfQoSWFQRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    h3cIfQoSWFQRunInfoTable.setStatus("current")
_H3cIfQoSWFQRunInfoEntry_Object = MibTableRow
h3cIfQoSWFQRunInfoEntry = _H3cIfQoSWFQRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 4, 2, 1, 1)
)
h3cIfQoSWFQRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cIfQoSWFQRunInfoEntry.setStatus("current")
_H3cIfQoSWFQSize_Type = Integer32
_H3cIfQoSWFQSize_Object = MibTableColumn
h3cIfQoSWFQSize = _H3cIfQoSWFQSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 4, 2, 1, 1, 1),
    _H3cIfQoSWFQSize_Type()
)
h3cIfQoSWFQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWFQSize.setStatus("current")
_H3cIfQoSWFQLength_Type = Integer32
_H3cIfQoSWFQLength_Object = MibTableColumn
h3cIfQoSWFQLength = _H3cIfQoSWFQLength_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 4, 2, 1, 1, 2),
    _H3cIfQoSWFQLength_Type()
)
h3cIfQoSWFQLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWFQLength.setStatus("current")
_H3cIfQoSWFQDiscardPackets_Type = Counter64
_H3cIfQoSWFQDiscardPackets_Object = MibTableColumn
h3cIfQoSWFQDiscardPackets = _H3cIfQoSWFQDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 4, 2, 1, 1, 3),
    _H3cIfQoSWFQDiscardPackets_Type()
)
h3cIfQoSWFQDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWFQDiscardPackets.setStatus("current")
_H3cIfQoSWFQHashedActiveQueues_Type = Integer32
_H3cIfQoSWFQHashedActiveQueues_Object = MibTableColumn
h3cIfQoSWFQHashedActiveQueues = _H3cIfQoSWFQHashedActiveQueues_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 4, 2, 1, 1, 4),
    _H3cIfQoSWFQHashedActiveQueues_Type()
)
h3cIfQoSWFQHashedActiveQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWFQHashedActiveQueues.setStatus("current")
_H3cIfQoSWFQHashedMaxActiveQueues_Type = Integer32
_H3cIfQoSWFQHashedMaxActiveQueues_Object = MibTableColumn
h3cIfQoSWFQHashedMaxActiveQueues = _H3cIfQoSWFQHashedMaxActiveQueues_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 4, 2, 1, 1, 5),
    _H3cIfQoSWFQHashedMaxActiveQueues_Type()
)
h3cIfQoSWFQHashedMaxActiveQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWFQHashedMaxActiveQueues.setStatus("current")
_H3fIfQosWFQhashedTotalQueues_Type = Integer32
_H3fIfQosWFQhashedTotalQueues_Object = MibTableColumn
h3fIfQosWFQhashedTotalQueues = _H3fIfQosWFQhashedTotalQueues_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 4, 2, 1, 1, 6),
    _H3fIfQosWFQhashedTotalQueues_Type()
)
h3fIfQosWFQhashedTotalQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3fIfQosWFQhashedTotalQueues.setStatus("current")
_H3cIfQoSBandwidthGroup_ObjectIdentity = ObjectIdentity
h3cIfQoSBandwidthGroup = _H3cIfQoSBandwidthGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 5)
)
_H3cIfQoSBandwidthTable_Object = MibTable
h3cIfQoSBandwidthTable = _H3cIfQoSBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    h3cIfQoSBandwidthTable.setStatus("current")
_H3cIfQoSBandwidthEntry_Object = MibTableRow
h3cIfQoSBandwidthEntry = _H3cIfQoSBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 5, 1, 1)
)
h3cIfQoSBandwidthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cIfQoSBandwidthEntry.setStatus("current")
_H3cIfQoSMaxBandwidth_Type = Integer32
_H3cIfQoSMaxBandwidth_Object = MibTableColumn
h3cIfQoSMaxBandwidth = _H3cIfQoSMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 5, 1, 1, 1),
    _H3cIfQoSMaxBandwidth_Type()
)
h3cIfQoSMaxBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSMaxBandwidth.setStatus("current")


class _H3cIfQoSReservedBandwidthPct_Type(Integer32):
    """Custom type h3cIfQoSReservedBandwidthPct based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_H3cIfQoSReservedBandwidthPct_Type.__name__ = "Integer32"
_H3cIfQoSReservedBandwidthPct_Object = MibTableColumn
h3cIfQoSReservedBandwidthPct = _H3cIfQoSReservedBandwidthPct_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 5, 1, 1, 2),
    _H3cIfQoSReservedBandwidthPct_Type()
)
h3cIfQoSReservedBandwidthPct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSReservedBandwidthPct.setStatus("current")
_H3cIfQoSBandwidthRowStatus_Type = RowStatus
_H3cIfQoSBandwidthRowStatus_Object = MibTableColumn
h3cIfQoSBandwidthRowStatus = _H3cIfQoSBandwidthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 5, 1, 1, 3),
    _H3cIfQoSBandwidthRowStatus_Type()
)
h3cIfQoSBandwidthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSBandwidthRowStatus.setStatus("current")
_H3cIfQoSQmtokenGroup_ObjectIdentity = ObjectIdentity
h3cIfQoSQmtokenGroup = _H3cIfQoSQmtokenGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 6)
)
_H3cIfQoSQmtokenTable_Object = MibTable
h3cIfQoSQmtokenTable = _H3cIfQoSQmtokenTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    h3cIfQoSQmtokenTable.setStatus("current")
_H3cIfQoSQmtokenEntry_Object = MibTableRow
h3cIfQoSQmtokenEntry = _H3cIfQoSQmtokenEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 6, 1, 1)
)
h3cIfQoSQmtokenEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cIfQoSQmtokenEntry.setStatus("current")


class _H3cIfQoSQmtokenNumber_Type(Integer32):
    """Custom type h3cIfQoSQmtokenNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_H3cIfQoSQmtokenNumber_Type.__name__ = "Integer32"
_H3cIfQoSQmtokenNumber_Object = MibTableColumn
h3cIfQoSQmtokenNumber = _H3cIfQoSQmtokenNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 6, 1, 1, 1),
    _H3cIfQoSQmtokenNumber_Type()
)
h3cIfQoSQmtokenNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSQmtokenNumber.setStatus("current")
_H3cIfQoSQmtokenRosStatus_Type = RowStatus
_H3cIfQoSQmtokenRosStatus_Object = MibTableColumn
h3cIfQoSQmtokenRosStatus = _H3cIfQoSQmtokenRosStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 6, 1, 1, 2),
    _H3cIfQoSQmtokenRosStatus_Type()
)
h3cIfQoSQmtokenRosStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSQmtokenRosStatus.setStatus("current")
_H3cIfQoSRTPQObject_ObjectIdentity = ObjectIdentity
h3cIfQoSRTPQObject = _H3cIfQoSRTPQObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 7)
)
_H3cIfQoSRTPQConfigGroup_ObjectIdentity = ObjectIdentity
h3cIfQoSRTPQConfigGroup = _H3cIfQoSRTPQConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 7, 1)
)
_H3cIfQoSRTPQConfigTable_Object = MibTable
h3cIfQoSRTPQConfigTable = _H3cIfQoSRTPQConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    h3cIfQoSRTPQConfigTable.setStatus("current")
_H3cIfQoSRTPQConfigEntry_Object = MibTableRow
h3cIfQoSRTPQConfigEntry = _H3cIfQoSRTPQConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 7, 1, 1, 1)
)
h3cIfQoSRTPQConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cIfQoSRTPQConfigEntry.setStatus("current")


class _H3cIfQoSRTPQStartPort_Type(Integer32):
    """Custom type h3cIfQoSRTPQStartPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 65535),
    )


_H3cIfQoSRTPQStartPort_Type.__name__ = "Integer32"
_H3cIfQoSRTPQStartPort_Object = MibTableColumn
h3cIfQoSRTPQStartPort = _H3cIfQoSRTPQStartPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 7, 1, 1, 1, 1),
    _H3cIfQoSRTPQStartPort_Type()
)
h3cIfQoSRTPQStartPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSRTPQStartPort.setStatus("current")


class _H3cIfQoSRTPQEndPort_Type(Integer32):
    """Custom type h3cIfQoSRTPQEndPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 65535),
    )


_H3cIfQoSRTPQEndPort_Type.__name__ = "Integer32"
_H3cIfQoSRTPQEndPort_Object = MibTableColumn
h3cIfQoSRTPQEndPort = _H3cIfQoSRTPQEndPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 7, 1, 1, 1, 2),
    _H3cIfQoSRTPQEndPort_Type()
)
h3cIfQoSRTPQEndPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSRTPQEndPort.setStatus("current")
_H3cIfQoSRTPQReservedBandwidth_Type = Integer32
_H3cIfQoSRTPQReservedBandwidth_Object = MibTableColumn
h3cIfQoSRTPQReservedBandwidth = _H3cIfQoSRTPQReservedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 7, 1, 1, 1, 3),
    _H3cIfQoSRTPQReservedBandwidth_Type()
)
h3cIfQoSRTPQReservedBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSRTPQReservedBandwidth.setStatus("current")
_H3cIfQoSRTPQCbs_Type = Unsigned32
_H3cIfQoSRTPQCbs_Object = MibTableColumn
h3cIfQoSRTPQCbs = _H3cIfQoSRTPQCbs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 7, 1, 1, 1, 4),
    _H3cIfQoSRTPQCbs_Type()
)
h3cIfQoSRTPQCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSRTPQCbs.setStatus("current")
_H3cIfQoSRTPQRowStatus_Type = RowStatus
_H3cIfQoSRTPQRowStatus_Object = MibTableColumn
h3cIfQoSRTPQRowStatus = _H3cIfQoSRTPQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 7, 1, 1, 1, 5),
    _H3cIfQoSRTPQRowStatus_Type()
)
h3cIfQoSRTPQRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSRTPQRowStatus.setStatus("current")
_H3cIfQoSRTPQRunInfoGroup_ObjectIdentity = ObjectIdentity
h3cIfQoSRTPQRunInfoGroup = _H3cIfQoSRTPQRunInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 7, 2)
)
_H3cIfQoSRTPQRunInfoTable_Object = MibTable
h3cIfQoSRTPQRunInfoTable = _H3cIfQoSRTPQRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 7, 2, 1)
)
if mibBuilder.loadTexts:
    h3cIfQoSRTPQRunInfoTable.setStatus("current")
_H3cIfQoSRTPQRunInfoEntry_Object = MibTableRow
h3cIfQoSRTPQRunInfoEntry = _H3cIfQoSRTPQRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 7, 2, 1, 1)
)
h3cIfQoSRTPQRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cIfQoSRTPQRunInfoEntry.setStatus("current")
_H3cIfQoSRTPQPacketNumber_Type = Integer32
_H3cIfQoSRTPQPacketNumber_Object = MibTableColumn
h3cIfQoSRTPQPacketNumber = _H3cIfQoSRTPQPacketNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 7, 2, 1, 1, 1),
    _H3cIfQoSRTPQPacketNumber_Type()
)
h3cIfQoSRTPQPacketNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSRTPQPacketNumber.setStatus("current")
_H3cIfQoSRTPQPacketSize_Type = Integer32
_H3cIfQoSRTPQPacketSize_Object = MibTableColumn
h3cIfQoSRTPQPacketSize = _H3cIfQoSRTPQPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 7, 2, 1, 1, 2),
    _H3cIfQoSRTPQPacketSize_Type()
)
h3cIfQoSRTPQPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSRTPQPacketSize.setStatus("current")
_H3cIfQoSRTPQOutputPackets_Type = Counter64
_H3cIfQoSRTPQOutputPackets_Object = MibTableColumn
h3cIfQoSRTPQOutputPackets = _H3cIfQoSRTPQOutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 7, 2, 1, 1, 3),
    _H3cIfQoSRTPQOutputPackets_Type()
)
h3cIfQoSRTPQOutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSRTPQOutputPackets.setStatus("current")
_H3cIfQoSRTPQDiscardPackets_Type = Counter64
_H3cIfQoSRTPQDiscardPackets_Object = MibTableColumn
h3cIfQoSRTPQDiscardPackets = _H3cIfQoSRTPQDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 7, 2, 1, 1, 4),
    _H3cIfQoSRTPQDiscardPackets_Type()
)
h3cIfQoSRTPQDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSRTPQDiscardPackets.setStatus("current")
_H3cIfQoSCarListObject_ObjectIdentity = ObjectIdentity
h3cIfQoSCarListObject = _H3cIfQoSCarListObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 8)
)
_H3cIfQoCarListGroup_ObjectIdentity = ObjectIdentity
h3cIfQoCarListGroup = _H3cIfQoCarListGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 8, 1)
)
_H3cIfQoSCarlTable_Object = MibTable
h3cIfQoSCarlTable = _H3cIfQoSCarlTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 8, 1, 1)
)
if mibBuilder.loadTexts:
    h3cIfQoSCarlTable.setStatus("current")
_H3cIfQoSCarlEntry_Object = MibTableRow
h3cIfQoSCarlEntry = _H3cIfQoSCarlEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 8, 1, 1, 1)
)
h3cIfQoSCarlEntry.setIndexNames(
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSCarlListNum"),
)
if mibBuilder.loadTexts:
    h3cIfQoSCarlEntry.setStatus("current")
_H3cIfQoSCarlListNum_Type = Integer32
_H3cIfQoSCarlListNum_Object = MibTableColumn
h3cIfQoSCarlListNum = _H3cIfQoSCarlListNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 8, 1, 1, 1, 1),
    _H3cIfQoSCarlListNum_Type()
)
h3cIfQoSCarlListNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfQoSCarlListNum.setStatus("current")


class _H3cIfQoSCarlParaType_Type(Integer32):
    """Custom type h3cIfQoSCarlParaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dscpMask", 3),
          ("macAddress", 1),
          ("precMask", 2))
    )


_H3cIfQoSCarlParaType_Type.__name__ = "Integer32"
_H3cIfQoSCarlParaType_Object = MibTableColumn
h3cIfQoSCarlParaType = _H3cIfQoSCarlParaType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 8, 1, 1, 1, 2),
    _H3cIfQoSCarlParaType_Type()
)
h3cIfQoSCarlParaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSCarlParaType.setStatus("current")
_H3cIfQoSCarlParaValue_Type = OctetString
_H3cIfQoSCarlParaValue_Object = MibTableColumn
h3cIfQoSCarlParaValue = _H3cIfQoSCarlParaValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 8, 1, 1, 1, 3),
    _H3cIfQoSCarlParaValue_Type()
)
h3cIfQoSCarlParaValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSCarlParaValue.setStatus("current")
_H3cIfQoSCarlRowStatus_Type = RowStatus
_H3cIfQoSCarlRowStatus_Object = MibTableColumn
h3cIfQoSCarlRowStatus = _H3cIfQoSCarlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 2, 8, 1, 1, 1, 4),
    _H3cIfQoSCarlRowStatus_Type()
)
h3cIfQoSCarlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSCarlRowStatus.setStatus("current")
_H3cIfQoSLineRateObjects_ObjectIdentity = ObjectIdentity
h3cIfQoSLineRateObjects = _H3cIfQoSLineRateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 3)
)
_H3cIfQoSLRConfigTable_Object = MibTable
h3cIfQoSLRConfigTable = _H3cIfQoSLRConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 3, 1)
)
if mibBuilder.loadTexts:
    h3cIfQoSLRConfigTable.setStatus("current")
_H3cIfQoSLRConfigEntry_Object = MibTableRow
h3cIfQoSLRConfigEntry = _H3cIfQoSLRConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 3, 1, 1)
)
h3cIfQoSLRConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSLRDirection"),
)
if mibBuilder.loadTexts:
    h3cIfQoSLRConfigEntry.setStatus("current")
_H3cIfQoSLRDirection_Type = Direction
_H3cIfQoSLRDirection_Object = MibTableColumn
h3cIfQoSLRDirection = _H3cIfQoSLRDirection_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 3, 1, 1, 1),
    _H3cIfQoSLRDirection_Type()
)
h3cIfQoSLRDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfQoSLRDirection.setStatus("current")
_H3cIfQoSLRCir_Type = Unsigned32
_H3cIfQoSLRCir_Object = MibTableColumn
h3cIfQoSLRCir = _H3cIfQoSLRCir_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 3, 1, 1, 2),
    _H3cIfQoSLRCir_Type()
)
h3cIfQoSLRCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSLRCir.setStatus("current")
_H3cIfQoSLRCbs_Type = Unsigned32
_H3cIfQoSLRCbs_Object = MibTableColumn
h3cIfQoSLRCbs = _H3cIfQoSLRCbs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 3, 1, 1, 3),
    _H3cIfQoSLRCbs_Type()
)
h3cIfQoSLRCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSLRCbs.setStatus("current")
_H3cIfQoSLREbs_Type = Unsigned32
_H3cIfQoSLREbs_Object = MibTableColumn
h3cIfQoSLREbs = _H3cIfQoSLREbs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 3, 1, 1, 4),
    _H3cIfQoSLREbs_Type()
)
h3cIfQoSLREbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSLREbs.setStatus("current")
_H3cIfQoSRowStatus_Type = RowStatus
_H3cIfQoSRowStatus_Object = MibTableColumn
h3cIfQoSRowStatus = _H3cIfQoSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 3, 1, 1, 5),
    _H3cIfQoSRowStatus_Type()
)
h3cIfQoSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSRowStatus.setStatus("current")
_H3cIfQoSLRPir_Type = Unsigned32
_H3cIfQoSLRPir_Object = MibTableColumn
h3cIfQoSLRPir = _H3cIfQoSLRPir_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 3, 1, 1, 6),
    _H3cIfQoSLRPir_Type()
)
h3cIfQoSLRPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSLRPir.setStatus("current")
_H3cIfQoSLRRunInfoTable_Object = MibTable
h3cIfQoSLRRunInfoTable = _H3cIfQoSLRRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 3, 2)
)
if mibBuilder.loadTexts:
    h3cIfQoSLRRunInfoTable.setStatus("current")
_H3cIfQoSLRRunInfoEntry_Object = MibTableRow
h3cIfQoSLRRunInfoEntry = _H3cIfQoSLRRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 3, 2, 1)
)
h3cIfQoSLRRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSLRDirection"),
)
if mibBuilder.loadTexts:
    h3cIfQoSLRRunInfoEntry.setStatus("current")
_H3cIfQoSLRRunInfoPassedPackets_Type = Counter64
_H3cIfQoSLRRunInfoPassedPackets_Object = MibTableColumn
h3cIfQoSLRRunInfoPassedPackets = _H3cIfQoSLRRunInfoPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 3, 2, 1, 1),
    _H3cIfQoSLRRunInfoPassedPackets_Type()
)
h3cIfQoSLRRunInfoPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSLRRunInfoPassedPackets.setStatus("current")
_H3cIfQoSLRRunInfoPassedBytes_Type = Counter64
_H3cIfQoSLRRunInfoPassedBytes_Object = MibTableColumn
h3cIfQoSLRRunInfoPassedBytes = _H3cIfQoSLRRunInfoPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 3, 2, 1, 2),
    _H3cIfQoSLRRunInfoPassedBytes_Type()
)
h3cIfQoSLRRunInfoPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSLRRunInfoPassedBytes.setStatus("current")
_H3cIfQoSLRRunInfoDelayedPackets_Type = Counter64
_H3cIfQoSLRRunInfoDelayedPackets_Object = MibTableColumn
h3cIfQoSLRRunInfoDelayedPackets = _H3cIfQoSLRRunInfoDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 3, 2, 1, 3),
    _H3cIfQoSLRRunInfoDelayedPackets_Type()
)
h3cIfQoSLRRunInfoDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSLRRunInfoDelayedPackets.setStatus("current")
_H3cIfQoSLRRunInfoDelayedBytes_Type = Counter64
_H3cIfQoSLRRunInfoDelayedBytes_Object = MibTableColumn
h3cIfQoSLRRunInfoDelayedBytes = _H3cIfQoSLRRunInfoDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 3, 2, 1, 4),
    _H3cIfQoSLRRunInfoDelayedBytes_Type()
)
h3cIfQoSLRRunInfoDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSLRRunInfoDelayedBytes.setStatus("current")


class _H3cIfQoSLRRunInfoActiveShaping_Type(Integer32):
    """Custom type h3cIfQoSLRRunInfoActiveShaping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_H3cIfQoSLRRunInfoActiveShaping_Type.__name__ = "Integer32"
_H3cIfQoSLRRunInfoActiveShaping_Object = MibTableColumn
h3cIfQoSLRRunInfoActiveShaping = _H3cIfQoSLRRunInfoActiveShaping_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 3, 2, 1, 5),
    _H3cIfQoSLRRunInfoActiveShaping_Type()
)
h3cIfQoSLRRunInfoActiveShaping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSLRRunInfoActiveShaping.setStatus("current")
_H3cIfQoSCARObjects_ObjectIdentity = ObjectIdentity
h3cIfQoSCARObjects = _H3cIfQoSCARObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4)
)
_H3cIfQoSAggregativeCarGroup_ObjectIdentity = ObjectIdentity
h3cIfQoSAggregativeCarGroup = _H3cIfQoSAggregativeCarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1)
)
_H3cIfQoSAggregativeCarNextIndex_Type = Integer32
_H3cIfQoSAggregativeCarNextIndex_Object = MibScalar
h3cIfQoSAggregativeCarNextIndex = _H3cIfQoSAggregativeCarNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 1),
    _H3cIfQoSAggregativeCarNextIndex_Type()
)
h3cIfQoSAggregativeCarNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarNextIndex.setStatus("current")
_H3cIfQoSAggregativeCarConfigTable_Object = MibTable
h3cIfQoSAggregativeCarConfigTable = _H3cIfQoSAggregativeCarConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarConfigTable.setStatus("current")
_H3cIfQoSAggregativeCarConfigEntry_Object = MibTableRow
h3cIfQoSAggregativeCarConfigEntry = _H3cIfQoSAggregativeCarConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 2, 1)
)
h3cIfQoSAggregativeCarConfigEntry.setIndexNames(
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSAggregativeCarIndex"),
)
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarConfigEntry.setStatus("current")


class _H3cIfQoSAggregativeCarIndex_Type(Integer32):
    """Custom type h3cIfQoSAggregativeCarIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_H3cIfQoSAggregativeCarIndex_Type.__name__ = "Integer32"
_H3cIfQoSAggregativeCarIndex_Object = MibTableColumn
h3cIfQoSAggregativeCarIndex = _H3cIfQoSAggregativeCarIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 2, 1, 1),
    _H3cIfQoSAggregativeCarIndex_Type()
)
h3cIfQoSAggregativeCarIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarIndex.setStatus("current")


class _H3cIfQoSAggregativeCarName_Type(OctetString):
    """Custom type h3cIfQoSAggregativeCarName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cIfQoSAggregativeCarName_Type.__name__ = "OctetString"
_H3cIfQoSAggregativeCarName_Object = MibTableColumn
h3cIfQoSAggregativeCarName = _H3cIfQoSAggregativeCarName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 2, 1, 2),
    _H3cIfQoSAggregativeCarName_Type()
)
h3cIfQoSAggregativeCarName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarName.setStatus("current")
_H3cIfQoSAggregativeCarCir_Type = Unsigned32
_H3cIfQoSAggregativeCarCir_Object = MibTableColumn
h3cIfQoSAggregativeCarCir = _H3cIfQoSAggregativeCarCir_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 2, 1, 3),
    _H3cIfQoSAggregativeCarCir_Type()
)
h3cIfQoSAggregativeCarCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarCir.setStatus("current")
_H3cIfQoSAggregativeCarCbs_Type = Unsigned32
_H3cIfQoSAggregativeCarCbs_Object = MibTableColumn
h3cIfQoSAggregativeCarCbs = _H3cIfQoSAggregativeCarCbs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 2, 1, 4),
    _H3cIfQoSAggregativeCarCbs_Type()
)
h3cIfQoSAggregativeCarCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarCbs.setStatus("current")
_H3cIfQoSAggregativeCarEbs_Type = Unsigned32
_H3cIfQoSAggregativeCarEbs_Object = MibTableColumn
h3cIfQoSAggregativeCarEbs = _H3cIfQoSAggregativeCarEbs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 2, 1, 5),
    _H3cIfQoSAggregativeCarEbs_Type()
)
h3cIfQoSAggregativeCarEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarEbs.setStatus("current")
_H3cIfQoSAggregativeCarPir_Type = Unsigned32
_H3cIfQoSAggregativeCarPir_Object = MibTableColumn
h3cIfQoSAggregativeCarPir = _H3cIfQoSAggregativeCarPir_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 2, 1, 6),
    _H3cIfQoSAggregativeCarPir_Type()
)
h3cIfQoSAggregativeCarPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarPir.setStatus("current")


class _H3cIfQoSAggregativeCarGreenActionType_Type(CarAction):
    """Custom type h3cIfQoSAggregativeCarGreenActionType based on CarAction"""


_H3cIfQoSAggregativeCarGreenActionType_Object = MibTableColumn
h3cIfQoSAggregativeCarGreenActionType = _H3cIfQoSAggregativeCarGreenActionType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 2, 1, 7),
    _H3cIfQoSAggregativeCarGreenActionType_Type()
)
h3cIfQoSAggregativeCarGreenActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarGreenActionType.setStatus("current")


class _H3cIfQoSAggregativeCarGreenActionValue_Type(Integer32):
    """Custom type h3cIfQoSAggregativeCarGreenActionValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_H3cIfQoSAggregativeCarGreenActionValue_Type.__name__ = "Integer32"
_H3cIfQoSAggregativeCarGreenActionValue_Object = MibTableColumn
h3cIfQoSAggregativeCarGreenActionValue = _H3cIfQoSAggregativeCarGreenActionValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 2, 1, 8),
    _H3cIfQoSAggregativeCarGreenActionValue_Type()
)
h3cIfQoSAggregativeCarGreenActionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarGreenActionValue.setStatus("current")
_H3cIfQoSAggregativeCarYellowActionType_Type = CarAction
_H3cIfQoSAggregativeCarYellowActionType_Object = MibTableColumn
h3cIfQoSAggregativeCarYellowActionType = _H3cIfQoSAggregativeCarYellowActionType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 2, 1, 9),
    _H3cIfQoSAggregativeCarYellowActionType_Type()
)
h3cIfQoSAggregativeCarYellowActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarYellowActionType.setStatus("current")


class _H3cIfQoSAggregativeCarYellowActionValue_Type(Integer32):
    """Custom type h3cIfQoSAggregativeCarYellowActionValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_H3cIfQoSAggregativeCarYellowActionValue_Type.__name__ = "Integer32"
_H3cIfQoSAggregativeCarYellowActionValue_Object = MibTableColumn
h3cIfQoSAggregativeCarYellowActionValue = _H3cIfQoSAggregativeCarYellowActionValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 2, 1, 10),
    _H3cIfQoSAggregativeCarYellowActionValue_Type()
)
h3cIfQoSAggregativeCarYellowActionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarYellowActionValue.setStatus("current")
_H3cIfQoSAggregativeCarRedActionType_Type = CarAction
_H3cIfQoSAggregativeCarRedActionType_Object = MibTableColumn
h3cIfQoSAggregativeCarRedActionType = _H3cIfQoSAggregativeCarRedActionType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 2, 1, 11),
    _H3cIfQoSAggregativeCarRedActionType_Type()
)
h3cIfQoSAggregativeCarRedActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarRedActionType.setStatus("current")
_H3cIfQoSAggregativeCarRedActionValue_Type = Integer32
_H3cIfQoSAggregativeCarRedActionValue_Object = MibTableColumn
h3cIfQoSAggregativeCarRedActionValue = _H3cIfQoSAggregativeCarRedActionValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 2, 1, 12),
    _H3cIfQoSAggregativeCarRedActionValue_Type()
)
h3cIfQoSAggregativeCarRedActionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarRedActionValue.setStatus("current")


class _H3cIfQoSAggregativeCarType_Type(Integer32):
    """Custom type h3cIfQoSAggregativeCarType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggregative", 1),
          ("notAggregative", 2))
    )


_H3cIfQoSAggregativeCarType_Type.__name__ = "Integer32"
_H3cIfQoSAggregativeCarType_Object = MibTableColumn
h3cIfQoSAggregativeCarType = _H3cIfQoSAggregativeCarType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 2, 1, 13),
    _H3cIfQoSAggregativeCarType_Type()
)
h3cIfQoSAggregativeCarType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarType.setStatus("current")
_H3cIfQoSAggregativeCarRowStatus_Type = RowStatus
_H3cIfQoSAggregativeCarRowStatus_Object = MibTableColumn
h3cIfQoSAggregativeCarRowStatus = _H3cIfQoSAggregativeCarRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 2, 1, 14),
    _H3cIfQoSAggregativeCarRowStatus_Type()
)
h3cIfQoSAggregativeCarRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarRowStatus.setStatus("current")
_H3cIfQoSAggregativeCarApplyTable_Object = MibTable
h3cIfQoSAggregativeCarApplyTable = _H3cIfQoSAggregativeCarApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarApplyTable.setStatus("current")
_H3cIfQoSAggregativeCarApplyEntry_Object = MibTableRow
h3cIfQoSAggregativeCarApplyEntry = _H3cIfQoSAggregativeCarApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 3, 1)
)
h3cIfQoSAggregativeCarApplyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSAggregativeCarApplyDirection"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSAggregativeCarApplyRuleType"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSAggregativeCarApplyRuleValue"),
)
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarApplyEntry.setStatus("current")
_H3cIfQoSAggregativeCarApplyDirection_Type = Direction
_H3cIfQoSAggregativeCarApplyDirection_Object = MibTableColumn
h3cIfQoSAggregativeCarApplyDirection = _H3cIfQoSAggregativeCarApplyDirection_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 3, 1, 1),
    _H3cIfQoSAggregativeCarApplyDirection_Type()
)
h3cIfQoSAggregativeCarApplyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarApplyDirection.setStatus("current")


class _H3cIfQoSAggregativeCarApplyRuleType_Type(Integer32):
    """Custom type h3cIfQoSAggregativeCarApplyRuleType based on Integer32"""
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
        *(("any", 4),
          ("carl", 3),
          ("ipv4acl", 1),
          ("ipv6acl", 2))
    )


_H3cIfQoSAggregativeCarApplyRuleType_Type.__name__ = "Integer32"
_H3cIfQoSAggregativeCarApplyRuleType_Object = MibTableColumn
h3cIfQoSAggregativeCarApplyRuleType = _H3cIfQoSAggregativeCarApplyRuleType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 3, 1, 2),
    _H3cIfQoSAggregativeCarApplyRuleType_Type()
)
h3cIfQoSAggregativeCarApplyRuleType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarApplyRuleType.setStatus("current")
_H3cIfQoSAggregativeCarApplyRuleValue_Type = Integer32
_H3cIfQoSAggregativeCarApplyRuleValue_Object = MibTableColumn
h3cIfQoSAggregativeCarApplyRuleValue = _H3cIfQoSAggregativeCarApplyRuleValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 3, 1, 3),
    _H3cIfQoSAggregativeCarApplyRuleValue_Type()
)
h3cIfQoSAggregativeCarApplyRuleValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarApplyRuleValue.setStatus("current")
_H3cIfQoSAggregativeCarApplyCarIndex_Type = Integer32
_H3cIfQoSAggregativeCarApplyCarIndex_Object = MibTableColumn
h3cIfQoSAggregativeCarApplyCarIndex = _H3cIfQoSAggregativeCarApplyCarIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 3, 1, 4),
    _H3cIfQoSAggregativeCarApplyCarIndex_Type()
)
h3cIfQoSAggregativeCarApplyCarIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarApplyCarIndex.setStatus("current")
_H3cIfQoSAggregativeCarApplyRowStatus_Type = RowStatus
_H3cIfQoSAggregativeCarApplyRowStatus_Object = MibTableColumn
h3cIfQoSAggregativeCarApplyRowStatus = _H3cIfQoSAggregativeCarApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 3, 1, 5),
    _H3cIfQoSAggregativeCarApplyRowStatus_Type()
)
h3cIfQoSAggregativeCarApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarApplyRowStatus.setStatus("current")
_H3cIfQoSAggregativeCarRunInfoTable_Object = MibTable
h3cIfQoSAggregativeCarRunInfoTable = _H3cIfQoSAggregativeCarRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 4)
)
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarRunInfoTable.setStatus("current")
_H3cIfQoSAggregativeCarRunInfoEntry_Object = MibTableRow
h3cIfQoSAggregativeCarRunInfoEntry = _H3cIfQoSAggregativeCarRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 4, 1)
)
h3cIfQoSAggregativeCarRunInfoEntry.setIndexNames(
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSAggregativeCarIndex"),
)
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarRunInfoEntry.setStatus("current")
_H3cIfQoSAggregativeCarGreenPackets_Type = Counter64
_H3cIfQoSAggregativeCarGreenPackets_Object = MibTableColumn
h3cIfQoSAggregativeCarGreenPackets = _H3cIfQoSAggregativeCarGreenPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 4, 1, 1),
    _H3cIfQoSAggregativeCarGreenPackets_Type()
)
h3cIfQoSAggregativeCarGreenPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarGreenPackets.setStatus("current")
_H3cIfQoSAggregativeCarGreenBytes_Type = Counter64
_H3cIfQoSAggregativeCarGreenBytes_Object = MibTableColumn
h3cIfQoSAggregativeCarGreenBytes = _H3cIfQoSAggregativeCarGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 4, 1, 2),
    _H3cIfQoSAggregativeCarGreenBytes_Type()
)
h3cIfQoSAggregativeCarGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarGreenBytes.setStatus("current")
_H3cIfQoSAggregativeCarYellowPackets_Type = Counter64
_H3cIfQoSAggregativeCarYellowPackets_Object = MibTableColumn
h3cIfQoSAggregativeCarYellowPackets = _H3cIfQoSAggregativeCarYellowPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 4, 1, 3),
    _H3cIfQoSAggregativeCarYellowPackets_Type()
)
h3cIfQoSAggregativeCarYellowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarYellowPackets.setStatus("current")
_H3cIfQoSAggregativeCarYellowBytes_Type = Counter64
_H3cIfQoSAggregativeCarYellowBytes_Object = MibTableColumn
h3cIfQoSAggregativeCarYellowBytes = _H3cIfQoSAggregativeCarYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 4, 1, 4),
    _H3cIfQoSAggregativeCarYellowBytes_Type()
)
h3cIfQoSAggregativeCarYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarYellowBytes.setStatus("current")
_H3cIfQoSAggregativeCarRedPackets_Type = Counter64
_H3cIfQoSAggregativeCarRedPackets_Object = MibTableColumn
h3cIfQoSAggregativeCarRedPackets = _H3cIfQoSAggregativeCarRedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 4, 1, 5),
    _H3cIfQoSAggregativeCarRedPackets_Type()
)
h3cIfQoSAggregativeCarRedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarRedPackets.setStatus("current")
_H3cIfQoSAggregativeCarRedBytes_Type = Counter64
_H3cIfQoSAggregativeCarRedBytes_Object = MibTableColumn
h3cIfQoSAggregativeCarRedBytes = _H3cIfQoSAggregativeCarRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 1, 4, 1, 6),
    _H3cIfQoSAggregativeCarRedBytes_Type()
)
h3cIfQoSAggregativeCarRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSAggregativeCarRedBytes.setStatus("current")
_H3cIfQoSTricolorCarGroup_ObjectIdentity = ObjectIdentity
h3cIfQoSTricolorCarGroup = _H3cIfQoSTricolorCarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 2)
)
_H3cIfQoSTricolorCarConfigTable_Object = MibTable
h3cIfQoSTricolorCarConfigTable = _H3cIfQoSTricolorCarConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    h3cIfQoSTricolorCarConfigTable.setStatus("current")
_H3cIfQoSTricolorCarConfigEntry_Object = MibTableRow
h3cIfQoSTricolorCarConfigEntry = _H3cIfQoSTricolorCarConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 2, 1, 1)
)
h3cIfQoSTricolorCarConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSTricolorCarDirection"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSTricolorCarType"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSTricolorCarValue"),
)
if mibBuilder.loadTexts:
    h3cIfQoSTricolorCarConfigEntry.setStatus("current")
_H3cIfQoSTricolorCarDirection_Type = Direction
_H3cIfQoSTricolorCarDirection_Object = MibTableColumn
h3cIfQoSTricolorCarDirection = _H3cIfQoSTricolorCarDirection_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 2, 1, 1, 1),
    _H3cIfQoSTricolorCarDirection_Type()
)
h3cIfQoSTricolorCarDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfQoSTricolorCarDirection.setStatus("current")


class _H3cIfQoSTricolorCarType_Type(Integer32):
    """Custom type h3cIfQoSTricolorCarType based on Integer32"""
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
        *(("any", 4),
          ("carl", 3),
          ("ipv4acl", 1),
          ("ipv6acl", 2))
    )


_H3cIfQoSTricolorCarType_Type.__name__ = "Integer32"
_H3cIfQoSTricolorCarType_Object = MibTableColumn
h3cIfQoSTricolorCarType = _H3cIfQoSTricolorCarType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 2, 1, 1, 2),
    _H3cIfQoSTricolorCarType_Type()
)
h3cIfQoSTricolorCarType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfQoSTricolorCarType.setStatus("current")
_H3cIfQoSTricolorCarValue_Type = Integer32
_H3cIfQoSTricolorCarValue_Object = MibTableColumn
h3cIfQoSTricolorCarValue = _H3cIfQoSTricolorCarValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 2, 1, 1, 3),
    _H3cIfQoSTricolorCarValue_Type()
)
h3cIfQoSTricolorCarValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfQoSTricolorCarValue.setStatus("current")
_H3cIfQoSTricolorCarCir_Type = Unsigned32
_H3cIfQoSTricolorCarCir_Object = MibTableColumn
h3cIfQoSTricolorCarCir = _H3cIfQoSTricolorCarCir_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 2, 1, 1, 4),
    _H3cIfQoSTricolorCarCir_Type()
)
h3cIfQoSTricolorCarCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSTricolorCarCir.setStatus("current")
_H3cIfQoSTricolorCarCbs_Type = Unsigned32
_H3cIfQoSTricolorCarCbs_Object = MibTableColumn
h3cIfQoSTricolorCarCbs = _H3cIfQoSTricolorCarCbs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 2, 1, 1, 5),
    _H3cIfQoSTricolorCarCbs_Type()
)
h3cIfQoSTricolorCarCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSTricolorCarCbs.setStatus("current")
_H3cIfQoSTricolorCarEbs_Type = Unsigned32
_H3cIfQoSTricolorCarEbs_Object = MibTableColumn
h3cIfQoSTricolorCarEbs = _H3cIfQoSTricolorCarEbs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 2, 1, 1, 6),
    _H3cIfQoSTricolorCarEbs_Type()
)
h3cIfQoSTricolorCarEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSTricolorCarEbs.setStatus("current")
_H3cIfQoSTricolorCarPir_Type = Unsigned32
_H3cIfQoSTricolorCarPir_Object = MibTableColumn
h3cIfQoSTricolorCarPir = _H3cIfQoSTricolorCarPir_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 2, 1, 1, 7),
    _H3cIfQoSTricolorCarPir_Type()
)
h3cIfQoSTricolorCarPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSTricolorCarPir.setStatus("current")


class _H3cIfQoSTricolorCarGreenActionType_Type(CarAction):
    """Custom type h3cIfQoSTricolorCarGreenActionType based on CarAction"""


_H3cIfQoSTricolorCarGreenActionType_Object = MibTableColumn
h3cIfQoSTricolorCarGreenActionType = _H3cIfQoSTricolorCarGreenActionType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 2, 1, 1, 8),
    _H3cIfQoSTricolorCarGreenActionType_Type()
)
h3cIfQoSTricolorCarGreenActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSTricolorCarGreenActionType.setStatus("current")


class _H3cIfQoSTricolorCarGreenActionValue_Type(Integer32):
    """Custom type h3cIfQoSTricolorCarGreenActionValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_H3cIfQoSTricolorCarGreenActionValue_Type.__name__ = "Integer32"
_H3cIfQoSTricolorCarGreenActionValue_Object = MibTableColumn
h3cIfQoSTricolorCarGreenActionValue = _H3cIfQoSTricolorCarGreenActionValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 2, 1, 1, 9),
    _H3cIfQoSTricolorCarGreenActionValue_Type()
)
h3cIfQoSTricolorCarGreenActionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSTricolorCarGreenActionValue.setStatus("current")


class _H3cIfQoSTricolorCarYellowActionType_Type(CarAction):
    """Custom type h3cIfQoSTricolorCarYellowActionType based on CarAction"""


_H3cIfQoSTricolorCarYellowActionType_Object = MibTableColumn
h3cIfQoSTricolorCarYellowActionType = _H3cIfQoSTricolorCarYellowActionType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 2, 1, 1, 10),
    _H3cIfQoSTricolorCarYellowActionType_Type()
)
h3cIfQoSTricolorCarYellowActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSTricolorCarYellowActionType.setStatus("current")


class _H3cIfQoSTricolorCarYellowActionValue_Type(Integer32):
    """Custom type h3cIfQoSTricolorCarYellowActionValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_H3cIfQoSTricolorCarYellowActionValue_Type.__name__ = "Integer32"
_H3cIfQoSTricolorCarYellowActionValue_Object = MibTableColumn
h3cIfQoSTricolorCarYellowActionValue = _H3cIfQoSTricolorCarYellowActionValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 2, 1, 1, 11),
    _H3cIfQoSTricolorCarYellowActionValue_Type()
)
h3cIfQoSTricolorCarYellowActionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSTricolorCarYellowActionValue.setStatus("current")


class _H3cIfQoSTricolorCarRedActionType_Type(CarAction):
    """Custom type h3cIfQoSTricolorCarRedActionType based on CarAction"""


_H3cIfQoSTricolorCarRedActionType_Object = MibTableColumn
h3cIfQoSTricolorCarRedActionType = _H3cIfQoSTricolorCarRedActionType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 2, 1, 1, 12),
    _H3cIfQoSTricolorCarRedActionType_Type()
)
h3cIfQoSTricolorCarRedActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSTricolorCarRedActionType.setStatus("current")


class _H3cIfQoSTricolorCarRedActionValue_Type(Integer32):
    """Custom type h3cIfQoSTricolorCarRedActionValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_H3cIfQoSTricolorCarRedActionValue_Type.__name__ = "Integer32"
_H3cIfQoSTricolorCarRedActionValue_Object = MibTableColumn
h3cIfQoSTricolorCarRedActionValue = _H3cIfQoSTricolorCarRedActionValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 2, 1, 1, 13),
    _H3cIfQoSTricolorCarRedActionValue_Type()
)
h3cIfQoSTricolorCarRedActionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSTricolorCarRedActionValue.setStatus("current")
_H3cIfQoSTricolorCarRowStatus_Type = RowStatus
_H3cIfQoSTricolorCarRowStatus_Object = MibTableColumn
h3cIfQoSTricolorCarRowStatus = _H3cIfQoSTricolorCarRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 2, 1, 1, 14),
    _H3cIfQoSTricolorCarRowStatus_Type()
)
h3cIfQoSTricolorCarRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSTricolorCarRowStatus.setStatus("current")
_H3cIfQoSTricolorCarRunInfoTable_Object = MibTable
h3cIfQoSTricolorCarRunInfoTable = _H3cIfQoSTricolorCarRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    h3cIfQoSTricolorCarRunInfoTable.setStatus("current")
_H3cIfQoSTricolorCarRunInfoEntry_Object = MibTableRow
h3cIfQoSTricolorCarRunInfoEntry = _H3cIfQoSTricolorCarRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 2, 2, 1)
)
h3cIfQoSTricolorCarRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSTricolorCarDirection"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSTricolorCarType"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSTricolorCarValue"),
)
if mibBuilder.loadTexts:
    h3cIfQoSTricolorCarRunInfoEntry.setStatus("current")
_H3cIfQoSTricolorCarGreenPackets_Type = Counter64
_H3cIfQoSTricolorCarGreenPackets_Object = MibTableColumn
h3cIfQoSTricolorCarGreenPackets = _H3cIfQoSTricolorCarGreenPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 2, 2, 1, 1),
    _H3cIfQoSTricolorCarGreenPackets_Type()
)
h3cIfQoSTricolorCarGreenPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSTricolorCarGreenPackets.setStatus("current")
_H3cIfQoSTricolorCarGreenBytes_Type = Counter64
_H3cIfQoSTricolorCarGreenBytes_Object = MibTableColumn
h3cIfQoSTricolorCarGreenBytes = _H3cIfQoSTricolorCarGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 2, 2, 1, 2),
    _H3cIfQoSTricolorCarGreenBytes_Type()
)
h3cIfQoSTricolorCarGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSTricolorCarGreenBytes.setStatus("current")
_H3cIfQoSTricolorCarYellowPackets_Type = Counter64
_H3cIfQoSTricolorCarYellowPackets_Object = MibTableColumn
h3cIfQoSTricolorCarYellowPackets = _H3cIfQoSTricolorCarYellowPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 2, 2, 1, 3),
    _H3cIfQoSTricolorCarYellowPackets_Type()
)
h3cIfQoSTricolorCarYellowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSTricolorCarYellowPackets.setStatus("current")
_H3cIfQoSTricolorCarYellowBytes_Type = Counter64
_H3cIfQoSTricolorCarYellowBytes_Object = MibTableColumn
h3cIfQoSTricolorCarYellowBytes = _H3cIfQoSTricolorCarYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 2, 2, 1, 4),
    _H3cIfQoSTricolorCarYellowBytes_Type()
)
h3cIfQoSTricolorCarYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSTricolorCarYellowBytes.setStatus("current")
_H3cIfQoSTricolorCarRedPackets_Type = Counter64
_H3cIfQoSTricolorCarRedPackets_Object = MibTableColumn
h3cIfQoSTricolorCarRedPackets = _H3cIfQoSTricolorCarRedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 2, 2, 1, 5),
    _H3cIfQoSTricolorCarRedPackets_Type()
)
h3cIfQoSTricolorCarRedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSTricolorCarRedPackets.setStatus("current")
_H3cIfQoSTricolorCarRedBytes_Type = Counter64
_H3cIfQoSTricolorCarRedBytes_Object = MibTableColumn
h3cIfQoSTricolorCarRedBytes = _H3cIfQoSTricolorCarRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 4, 2, 2, 1, 6),
    _H3cIfQoSTricolorCarRedBytes_Type()
)
h3cIfQoSTricolorCarRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSTricolorCarRedBytes.setStatus("current")
_H3cIfQoSGTSObjects_ObjectIdentity = ObjectIdentity
h3cIfQoSGTSObjects = _H3cIfQoSGTSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 5)
)
_H3cIfQoSGTSConfigTable_Object = MibTable
h3cIfQoSGTSConfigTable = _H3cIfQoSGTSConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 5, 1)
)
if mibBuilder.loadTexts:
    h3cIfQoSGTSConfigTable.setStatus("current")
_H3cIfQoSGTSConfigEntry_Object = MibTableRow
h3cIfQoSGTSConfigEntry = _H3cIfQoSGTSConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 5, 1, 1)
)
h3cIfQoSGTSConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSGTSClassRuleType"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSGTSClassRuleValue"),
)
if mibBuilder.loadTexts:
    h3cIfQoSGTSConfigEntry.setStatus("current")


class _H3cIfQoSGTSClassRuleType_Type(Integer32):
    """Custom type h3cIfQoSGTSClassRuleType based on Integer32"""
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
        *(("any", 1),
          ("ipv4acl", 2),
          ("ipv6acl", 3),
          ("queue", 4))
    )


_H3cIfQoSGTSClassRuleType_Type.__name__ = "Integer32"
_H3cIfQoSGTSClassRuleType_Object = MibTableColumn
h3cIfQoSGTSClassRuleType = _H3cIfQoSGTSClassRuleType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 5, 1, 1, 1),
    _H3cIfQoSGTSClassRuleType_Type()
)
h3cIfQoSGTSClassRuleType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfQoSGTSClassRuleType.setStatus("current")
_H3cIfQoSGTSClassRuleValue_Type = Integer32
_H3cIfQoSGTSClassRuleValue_Object = MibTableColumn
h3cIfQoSGTSClassRuleValue = _H3cIfQoSGTSClassRuleValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 5, 1, 1, 2),
    _H3cIfQoSGTSClassRuleValue_Type()
)
h3cIfQoSGTSClassRuleValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfQoSGTSClassRuleValue.setStatus("current")
_H3cIfQoSGTSCir_Type = Unsigned32
_H3cIfQoSGTSCir_Object = MibTableColumn
h3cIfQoSGTSCir = _H3cIfQoSGTSCir_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 5, 1, 1, 3),
    _H3cIfQoSGTSCir_Type()
)
h3cIfQoSGTSCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSGTSCir.setStatus("current")
_H3cIfQoSGTSCbs_Type = Unsigned32
_H3cIfQoSGTSCbs_Object = MibTableColumn
h3cIfQoSGTSCbs = _H3cIfQoSGTSCbs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 5, 1, 1, 4),
    _H3cIfQoSGTSCbs_Type()
)
h3cIfQoSGTSCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSGTSCbs.setStatus("current")
_H3cIfQoSGTSEbs_Type = Unsigned32
_H3cIfQoSGTSEbs_Object = MibTableColumn
h3cIfQoSGTSEbs = _H3cIfQoSGTSEbs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 5, 1, 1, 5),
    _H3cIfQoSGTSEbs_Type()
)
h3cIfQoSGTSEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSGTSEbs.setStatus("current")
_H3cIfQoSGTSQueueLength_Type = Integer32
_H3cIfQoSGTSQueueLength_Object = MibTableColumn
h3cIfQoSGTSQueueLength = _H3cIfQoSGTSQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 5, 1, 1, 6),
    _H3cIfQoSGTSQueueLength_Type()
)
h3cIfQoSGTSQueueLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSGTSQueueLength.setStatus("current")
_H3cIfQoSGTSConfigRowStatus_Type = RowStatus
_H3cIfQoSGTSConfigRowStatus_Object = MibTableColumn
h3cIfQoSGTSConfigRowStatus = _H3cIfQoSGTSConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 5, 1, 1, 7),
    _H3cIfQoSGTSConfigRowStatus_Type()
)
h3cIfQoSGTSConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSGTSConfigRowStatus.setStatus("current")
_H3cIfQoSGTSRunInfoTable_Object = MibTable
h3cIfQoSGTSRunInfoTable = _H3cIfQoSGTSRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 5, 2)
)
if mibBuilder.loadTexts:
    h3cIfQoSGTSRunInfoTable.setStatus("current")
_H3cIfQoSGTSRunInfoEntry_Object = MibTableRow
h3cIfQoSGTSRunInfoEntry = _H3cIfQoSGTSRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 5, 2, 1)
)
h3cIfQoSGTSRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSGTSClassRuleType"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSGTSClassRuleValue"),
)
if mibBuilder.loadTexts:
    h3cIfQoSGTSRunInfoEntry.setStatus("current")
_H3cIfQoSGTSQueueSize_Type = Integer32
_H3cIfQoSGTSQueueSize_Object = MibTableColumn
h3cIfQoSGTSQueueSize = _H3cIfQoSGTSQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 5, 2, 1, 1),
    _H3cIfQoSGTSQueueSize_Type()
)
h3cIfQoSGTSQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSGTSQueueSize.setStatus("current")
_H3cIfQoSGTSPassedPackets_Type = Counter64
_H3cIfQoSGTSPassedPackets_Object = MibTableColumn
h3cIfQoSGTSPassedPackets = _H3cIfQoSGTSPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 5, 2, 1, 2),
    _H3cIfQoSGTSPassedPackets_Type()
)
h3cIfQoSGTSPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSGTSPassedPackets.setStatus("current")
_H3cIfQoSGTSPassedBytes_Type = Counter64
_H3cIfQoSGTSPassedBytes_Object = MibTableColumn
h3cIfQoSGTSPassedBytes = _H3cIfQoSGTSPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 5, 2, 1, 3),
    _H3cIfQoSGTSPassedBytes_Type()
)
h3cIfQoSGTSPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSGTSPassedBytes.setStatus("current")
_H3cIfQoSGTSDiscardPackets_Type = Counter64
_H3cIfQoSGTSDiscardPackets_Object = MibTableColumn
h3cIfQoSGTSDiscardPackets = _H3cIfQoSGTSDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 5, 2, 1, 4),
    _H3cIfQoSGTSDiscardPackets_Type()
)
h3cIfQoSGTSDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSGTSDiscardPackets.setStatus("current")
_H3cIfQoSGTSDiscardBytes_Type = Counter64
_H3cIfQoSGTSDiscardBytes_Object = MibTableColumn
h3cIfQoSGTSDiscardBytes = _H3cIfQoSGTSDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 5, 2, 1, 5),
    _H3cIfQoSGTSDiscardBytes_Type()
)
h3cIfQoSGTSDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSGTSDiscardBytes.setStatus("current")
_H3cIfQoSGTSDelayedPackets_Type = Counter64
_H3cIfQoSGTSDelayedPackets_Object = MibTableColumn
h3cIfQoSGTSDelayedPackets = _H3cIfQoSGTSDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 5, 2, 1, 6),
    _H3cIfQoSGTSDelayedPackets_Type()
)
h3cIfQoSGTSDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSGTSDelayedPackets.setStatus("current")
_H3cIfQoSGTSDelayedBytes_Type = Counter64
_H3cIfQoSGTSDelayedBytes_Object = MibTableColumn
h3cIfQoSGTSDelayedBytes = _H3cIfQoSGTSDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 5, 2, 1, 7),
    _H3cIfQoSGTSDelayedBytes_Type()
)
h3cIfQoSGTSDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSGTSDelayedBytes.setStatus("current")
_H3cIfQoSWREDObjects_ObjectIdentity = ObjectIdentity
h3cIfQoSWREDObjects = _H3cIfQoSWREDObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6)
)
_H3cIfQoSWredGroupGroup_ObjectIdentity = ObjectIdentity
h3cIfQoSWredGroupGroup = _H3cIfQoSWredGroupGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 1)
)
_H3cIfQoSWredGroupNextIndex_Type = Integer32
_H3cIfQoSWredGroupNextIndex_Object = MibScalar
h3cIfQoSWredGroupNextIndex = _H3cIfQoSWredGroupNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 1, 1),
    _H3cIfQoSWredGroupNextIndex_Type()
)
h3cIfQoSWredGroupNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWredGroupNextIndex.setStatus("current")
_H3cIfQoSWredGroupTable_Object = MibTable
h3cIfQoSWredGroupTable = _H3cIfQoSWredGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    h3cIfQoSWredGroupTable.setStatus("current")
_H3cIfQoSWredGroupEntry_Object = MibTableRow
h3cIfQoSWredGroupEntry = _H3cIfQoSWredGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 1, 2, 1)
)
h3cIfQoSWredGroupEntry.setIndexNames(
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSWredGroupIndex"),
)
if mibBuilder.loadTexts:
    h3cIfQoSWredGroupEntry.setStatus("current")
_H3cIfQoSWredGroupIndex_Type = Integer32
_H3cIfQoSWredGroupIndex_Object = MibTableColumn
h3cIfQoSWredGroupIndex = _H3cIfQoSWredGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 1, 2, 1, 1),
    _H3cIfQoSWredGroupIndex_Type()
)
h3cIfQoSWredGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfQoSWredGroupIndex.setStatus("current")


class _H3cIfQoSWredGroupName_Type(OctetString):
    """Custom type h3cIfQoSWredGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_H3cIfQoSWredGroupName_Type.__name__ = "OctetString"
_H3cIfQoSWredGroupName_Object = MibTableColumn
h3cIfQoSWredGroupName = _H3cIfQoSWredGroupName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 1, 2, 1, 2),
    _H3cIfQoSWredGroupName_Type()
)
h3cIfQoSWredGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSWredGroupName.setStatus("current")


class _H3cIfQoSWredGroupType_Type(Integer32):
    """Custom type h3cIfQoSWredGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("atmclp", 5),
          ("dot1p", 1),
          ("dropLevel", 9),
          ("dscp", 3),
          ("exp", 7),
          ("frde", 6),
          ("ippre", 2),
          ("localpre", 4),
          ("queue", 8),
          ("userdefined", 0))
    )


_H3cIfQoSWredGroupType_Type.__name__ = "Integer32"
_H3cIfQoSWredGroupType_Object = MibTableColumn
h3cIfQoSWredGroupType = _H3cIfQoSWredGroupType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 1, 2, 1, 3),
    _H3cIfQoSWredGroupType_Type()
)
h3cIfQoSWredGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSWredGroupType.setStatus("current")


class _H3cIfQoSWredGroupWeightingConstant_Type(Integer32):
    """Custom type h3cIfQoSWredGroupWeightingConstant based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_H3cIfQoSWredGroupWeightingConstant_Type.__name__ = "Integer32"
_H3cIfQoSWredGroupWeightingConstant_Object = MibTableColumn
h3cIfQoSWredGroupWeightingConstant = _H3cIfQoSWredGroupWeightingConstant_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 1, 2, 1, 4),
    _H3cIfQoSWredGroupWeightingConstant_Type()
)
h3cIfQoSWredGroupWeightingConstant.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSWredGroupWeightingConstant.setStatus("current")
_H3cIfQoSWredGroupRowStatus_Type = RowStatus
_H3cIfQoSWredGroupRowStatus_Object = MibTableColumn
h3cIfQoSWredGroupRowStatus = _H3cIfQoSWredGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 1, 2, 1, 6),
    _H3cIfQoSWredGroupRowStatus_Type()
)
h3cIfQoSWredGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSWredGroupRowStatus.setStatus("current")
_H3cIfQoSWredGroupContentTable_Object = MibTable
h3cIfQoSWredGroupContentTable = _H3cIfQoSWredGroupContentTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 1, 3)
)
if mibBuilder.loadTexts:
    h3cIfQoSWredGroupContentTable.setStatus("current")
_H3cIfQoSWredGroupContentEntry_Object = MibTableRow
h3cIfQoSWredGroupContentEntry = _H3cIfQoSWredGroupContentEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 1, 3, 1)
)
h3cIfQoSWredGroupContentEntry.setIndexNames(
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSWredGroupIndex"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSWredGroupContentIndex"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSWredGroupContentSubIndex"),
)
if mibBuilder.loadTexts:
    h3cIfQoSWredGroupContentEntry.setStatus("current")


class _H3cIfQoSWredGroupContentIndex_Type(Integer32):
    """Custom type h3cIfQoSWredGroupContentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_H3cIfQoSWredGroupContentIndex_Type.__name__ = "Integer32"
_H3cIfQoSWredGroupContentIndex_Object = MibTableColumn
h3cIfQoSWredGroupContentIndex = _H3cIfQoSWredGroupContentIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 1, 3, 1, 1),
    _H3cIfQoSWredGroupContentIndex_Type()
)
h3cIfQoSWredGroupContentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfQoSWredGroupContentIndex.setStatus("current")


class _H3cIfQoSWredGroupContentSubIndex_Type(Integer32):
    """Custom type h3cIfQoSWredGroupContentSubIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_H3cIfQoSWredGroupContentSubIndex_Type.__name__ = "Integer32"
_H3cIfQoSWredGroupContentSubIndex_Object = MibTableColumn
h3cIfQoSWredGroupContentSubIndex = _H3cIfQoSWredGroupContentSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 1, 3, 1, 2),
    _H3cIfQoSWredGroupContentSubIndex_Type()
)
h3cIfQoSWredGroupContentSubIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfQoSWredGroupContentSubIndex.setStatus("current")
_H3cIfQoSWredLowLimit_Type = Integer32
_H3cIfQoSWredLowLimit_Object = MibTableColumn
h3cIfQoSWredLowLimit = _H3cIfQoSWredLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 1, 3, 1, 3),
    _H3cIfQoSWredLowLimit_Type()
)
h3cIfQoSWredLowLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSWredLowLimit.setStatus("current")
_H3cIfQoSWredHighLimit_Type = Integer32
_H3cIfQoSWredHighLimit_Object = MibTableColumn
h3cIfQoSWredHighLimit = _H3cIfQoSWredHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 1, 3, 1, 4),
    _H3cIfQoSWredHighLimit_Type()
)
h3cIfQoSWredHighLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSWredHighLimit.setStatus("current")
_H3cIfQoSWredDiscardProb_Type = Integer32
_H3cIfQoSWredDiscardProb_Object = MibTableColumn
h3cIfQoSWredDiscardProb = _H3cIfQoSWredDiscardProb_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 1, 3, 1, 5),
    _H3cIfQoSWredDiscardProb_Type()
)
h3cIfQoSWredDiscardProb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSWredDiscardProb.setStatus("current")


class _H3cIfQoSWredGroupExponent_Type(Integer32):
    """Custom type h3cIfQoSWredGroupExponent based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_H3cIfQoSWredGroupExponent_Type.__name__ = "Integer32"
_H3cIfQoSWredGroupExponent_Object = MibTableColumn
h3cIfQoSWredGroupExponent = _H3cIfQoSWredGroupExponent_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 1, 3, 1, 6),
    _H3cIfQoSWredGroupExponent_Type()
)
h3cIfQoSWredGroupExponent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSWredGroupExponent.setStatus("current")
_H3cIfQoSWredRowStatus_Type = RowStatus
_H3cIfQoSWredRowStatus_Object = MibTableColumn
h3cIfQoSWredRowStatus = _H3cIfQoSWredRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 1, 3, 1, 7),
    _H3cIfQoSWredRowStatus_Type()
)
h3cIfQoSWredRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSWredRowStatus.setStatus("current")
_H3cIfQoSWredGroupApplyIfTable_Object = MibTable
h3cIfQoSWredGroupApplyIfTable = _H3cIfQoSWredGroupApplyIfTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 1, 4)
)
if mibBuilder.loadTexts:
    h3cIfQoSWredGroupApplyIfTable.setStatus("current")
_H3cIfQoSWredGroupApplyIfEntry_Object = MibTableRow
h3cIfQoSWredGroupApplyIfEntry = _H3cIfQoSWredGroupApplyIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 1, 4, 1)
)
h3cIfQoSWredGroupApplyIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cIfQoSWredGroupApplyIfEntry.setStatus("current")


class _H3cIfQoSWredGroupApplyIndex_Type(Integer32):
    """Custom type h3cIfQoSWredGroupApplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_H3cIfQoSWredGroupApplyIndex_Type.__name__ = "Integer32"
_H3cIfQoSWredGroupApplyIndex_Object = MibTableColumn
h3cIfQoSWredGroupApplyIndex = _H3cIfQoSWredGroupApplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 1, 4, 1, 1),
    _H3cIfQoSWredGroupApplyIndex_Type()
)
h3cIfQoSWredGroupApplyIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSWredGroupApplyIndex.setStatus("current")
_H3cIfQoSWredGroupApplyName_Type = OctetString
_H3cIfQoSWredGroupApplyName_Object = MibTableColumn
h3cIfQoSWredGroupApplyName = _H3cIfQoSWredGroupApplyName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 1, 4, 1, 2),
    _H3cIfQoSWredGroupApplyName_Type()
)
h3cIfQoSWredGroupApplyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWredGroupApplyName.setStatus("current")
_H3cIfQoSWredGroupIfRowStatus_Type = RowStatus
_H3cIfQoSWredGroupIfRowStatus_Object = MibTableColumn
h3cIfQoSWredGroupIfRowStatus = _H3cIfQoSWredGroupIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 1, 4, 1, 3),
    _H3cIfQoSWredGroupIfRowStatus_Type()
)
h3cIfQoSWredGroupIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSWredGroupIfRowStatus.setStatus("current")
_H3cIfQoSWredApplyIfRunInfoTable_Object = MibTable
h3cIfQoSWredApplyIfRunInfoTable = _H3cIfQoSWredApplyIfRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 1, 5)
)
if mibBuilder.loadTexts:
    h3cIfQoSWredApplyIfRunInfoTable.setStatus("current")
_H3cIfQoSWredApplyIfRunInfoEntry_Object = MibTableRow
h3cIfQoSWredApplyIfRunInfoEntry = _H3cIfQoSWredApplyIfRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 1, 5, 1)
)
h3cIfQoSWredApplyIfRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSWredGroupIndex"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSWredGroupContentIndex"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSWredGroupContentSubIndex"),
)
if mibBuilder.loadTexts:
    h3cIfQoSWredApplyIfRunInfoEntry.setStatus("current")
_H3cIfQoSWredPreRandomDropNum_Type = Counter64
_H3cIfQoSWredPreRandomDropNum_Object = MibTableColumn
h3cIfQoSWredPreRandomDropNum = _H3cIfQoSWredPreRandomDropNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 1, 5, 1, 1),
    _H3cIfQoSWredPreRandomDropNum_Type()
)
h3cIfQoSWredPreRandomDropNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWredPreRandomDropNum.setStatus("current")
_H3cIfQoSWredPreTailDropNum_Type = Counter64
_H3cIfQoSWredPreTailDropNum_Object = MibTableColumn
h3cIfQoSWredPreTailDropNum = _H3cIfQoSWredPreTailDropNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 1, 5, 1, 2),
    _H3cIfQoSWredPreTailDropNum_Type()
)
h3cIfQoSWredPreTailDropNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWredPreTailDropNum.setStatus("current")
_H3cIfQoSPortWredGroup_ObjectIdentity = ObjectIdentity
h3cIfQoSPortWredGroup = _H3cIfQoSPortWredGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 2)
)
_H3cIfQoSPortWredWeightConstantTable_Object = MibTable
h3cIfQoSPortWredWeightConstantTable = _H3cIfQoSPortWredWeightConstantTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    h3cIfQoSPortWredWeightConstantTable.setStatus("current")
_H3cIfQoSPortWredWeightConstantEntry_Object = MibTableRow
h3cIfQoSPortWredWeightConstantEntry = _H3cIfQoSPortWredWeightConstantEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 2, 1, 1)
)
h3cIfQoSPortWredWeightConstantEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cIfQoSPortWredWeightConstantEntry.setStatus("current")
_H3cIfQoSPortWredEnable_Type = TruthValue
_H3cIfQoSPortWredEnable_Object = MibTableColumn
h3cIfQoSPortWredEnable = _H3cIfQoSPortWredEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 2, 1, 1, 1),
    _H3cIfQoSPortWredEnable_Type()
)
h3cIfQoSPortWredEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSPortWredEnable.setStatus("current")


class _H3cIfQoSPortWredWeightConstant_Type(Integer32):
    """Custom type h3cIfQoSPortWredWeightConstant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_H3cIfQoSPortWredWeightConstant_Type.__name__ = "Integer32"
_H3cIfQoSPortWredWeightConstant_Object = MibTableColumn
h3cIfQoSPortWredWeightConstant = _H3cIfQoSPortWredWeightConstant_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 2, 1, 1, 2),
    _H3cIfQoSPortWredWeightConstant_Type()
)
h3cIfQoSPortWredWeightConstant.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSPortWredWeightConstant.setStatus("current")
_H3cIfQoSPortWredWeightConstantRowStatus_Type = RowStatus
_H3cIfQoSPortWredWeightConstantRowStatus_Object = MibTableColumn
h3cIfQoSPortWredWeightConstantRowStatus = _H3cIfQoSPortWredWeightConstantRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 2, 1, 1, 3),
    _H3cIfQoSPortWredWeightConstantRowStatus_Type()
)
h3cIfQoSPortWredWeightConstantRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSPortWredWeightConstantRowStatus.setStatus("current")
_H3cIfQoSPortWredPreConfigTable_Object = MibTable
h3cIfQoSPortWredPreConfigTable = _H3cIfQoSPortWredPreConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 2, 2)
)
if mibBuilder.loadTexts:
    h3cIfQoSPortWredPreConfigTable.setStatus("current")
_H3cIfQoSPortWredPreConfigEntry_Object = MibTableRow
h3cIfQoSPortWredPreConfigEntry = _H3cIfQoSPortWredPreConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 2, 2, 1)
)
h3cIfQoSPortWredPreConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSPortWredPreID"),
)
if mibBuilder.loadTexts:
    h3cIfQoSPortWredPreConfigEntry.setStatus("current")
_H3cIfQoSPortWredPreID_Type = Integer32
_H3cIfQoSPortWredPreID_Object = MibTableColumn
h3cIfQoSPortWredPreID = _H3cIfQoSPortWredPreID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 2, 2, 1, 1),
    _H3cIfQoSPortWredPreID_Type()
)
h3cIfQoSPortWredPreID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfQoSPortWredPreID.setStatus("current")
_H3cIfQoSPortWredPreLowLimit_Type = Integer32
_H3cIfQoSPortWredPreLowLimit_Object = MibTableColumn
h3cIfQoSPortWredPreLowLimit = _H3cIfQoSPortWredPreLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 2, 2, 1, 2),
    _H3cIfQoSPortWredPreLowLimit_Type()
)
h3cIfQoSPortWredPreLowLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSPortWredPreLowLimit.setStatus("current")
_H3cIfQoSPortWredPreHighLimit_Type = Integer32
_H3cIfQoSPortWredPreHighLimit_Object = MibTableColumn
h3cIfQoSPortWredPreHighLimit = _H3cIfQoSPortWredPreHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 2, 2, 1, 3),
    _H3cIfQoSPortWredPreHighLimit_Type()
)
h3cIfQoSPortWredPreHighLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSPortWredPreHighLimit.setStatus("current")
_H3cIfQoSPortWredPreDiscardProbability_Type = Integer32
_H3cIfQoSPortWredPreDiscardProbability_Object = MibTableColumn
h3cIfQoSPortWredPreDiscardProbability = _H3cIfQoSPortWredPreDiscardProbability_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 2, 2, 1, 4),
    _H3cIfQoSPortWredPreDiscardProbability_Type()
)
h3cIfQoSPortWredPreDiscardProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSPortWredPreDiscardProbability.setStatus("current")
_H3cIfQoSPortWredPreRowStatus_Type = RowStatus
_H3cIfQoSPortWredPreRowStatus_Object = MibTableColumn
h3cIfQoSPortWredPreRowStatus = _H3cIfQoSPortWredPreRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 2, 2, 1, 5),
    _H3cIfQoSPortWredPreRowStatus_Type()
)
h3cIfQoSPortWredPreRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSPortWredPreRowStatus.setStatus("current")
_H3cIfQoSPortWredRunInfoTable_Object = MibTable
h3cIfQoSPortWredRunInfoTable = _H3cIfQoSPortWredRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 2, 3)
)
if mibBuilder.loadTexts:
    h3cIfQoSPortWredRunInfoTable.setStatus("current")
_H3cIfQoSPortWredRunInfoEntry_Object = MibTableRow
h3cIfQoSPortWredRunInfoEntry = _H3cIfQoSPortWredRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 2, 3, 1)
)
h3cIfQoSPortWredRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSPortWredPreID"),
)
if mibBuilder.loadTexts:
    h3cIfQoSPortWredRunInfoEntry.setStatus("current")
_H3cIfQoSWREDTailDropNum_Type = Counter64
_H3cIfQoSWREDTailDropNum_Object = MibTableColumn
h3cIfQoSWREDTailDropNum = _H3cIfQoSWREDTailDropNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 2, 3, 1, 1),
    _H3cIfQoSWREDTailDropNum_Type()
)
h3cIfQoSWREDTailDropNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWREDTailDropNum.setStatus("current")
_H3cIfQoSWREDRandomDropNum_Type = Counter64
_H3cIfQoSWREDRandomDropNum_Object = MibTableColumn
h3cIfQoSWREDRandomDropNum = _H3cIfQoSWREDRandomDropNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 6, 2, 3, 1, 2),
    _H3cIfQoSWREDRandomDropNum_Type()
)
h3cIfQoSWREDRandomDropNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSWREDRandomDropNum.setStatus("current")
_H3cIfQoSPortPriorityObjects_ObjectIdentity = ObjectIdentity
h3cIfQoSPortPriorityObjects = _H3cIfQoSPortPriorityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 7)
)
_H3cIfQoSPortPriorityConfigGroup_ObjectIdentity = ObjectIdentity
h3cIfQoSPortPriorityConfigGroup = _H3cIfQoSPortPriorityConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 7, 1)
)
_H3cIfQoSPortPriorityTable_Object = MibTable
h3cIfQoSPortPriorityTable = _H3cIfQoSPortPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    h3cIfQoSPortPriorityTable.setStatus("current")
_H3cIfQoSPortPriorityEntry_Object = MibTableRow
h3cIfQoSPortPriorityEntry = _H3cIfQoSPortPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 7, 1, 1, 1)
)
h3cIfQoSPortPriorityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cIfQoSPortPriorityEntry.setStatus("current")


class _H3cIfQoSPortPriorityValue_Type(Integer32):
    """Custom type h3cIfQoSPortPriorityValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_H3cIfQoSPortPriorityValue_Type.__name__ = "Integer32"
_H3cIfQoSPortPriorityValue_Object = MibTableColumn
h3cIfQoSPortPriorityValue = _H3cIfQoSPortPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 7, 1, 1, 1, 1),
    _H3cIfQoSPortPriorityValue_Type()
)
h3cIfQoSPortPriorityValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfQoSPortPriorityValue.setStatus("current")
_H3cIfQoSPortPirorityTrustTable_Object = MibTable
h3cIfQoSPortPirorityTrustTable = _H3cIfQoSPortPirorityTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 7, 1, 2)
)
if mibBuilder.loadTexts:
    h3cIfQoSPortPirorityTrustTable.setStatus("current")
_H3cIfQoSPortPirorityTrustEntry_Object = MibTableRow
h3cIfQoSPortPirorityTrustEntry = _H3cIfQoSPortPirorityTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 7, 1, 2, 1)
)
h3cIfQoSPortPirorityTrustEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cIfQoSPortPirorityTrustEntry.setStatus("current")


class _H3cIfQoSPortPriorityTrustTrustType_Type(Integer32):
    """Custom type h3cIfQoSPortPriorityTrustTrustType based on Integer32"""
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
        *(("dot1p", 2),
          ("dscp", 3),
          ("exp", 4),
          ("untrust", 1))
    )


_H3cIfQoSPortPriorityTrustTrustType_Type.__name__ = "Integer32"
_H3cIfQoSPortPriorityTrustTrustType_Object = MibTableColumn
h3cIfQoSPortPriorityTrustTrustType = _H3cIfQoSPortPriorityTrustTrustType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 7, 1, 2, 1, 1),
    _H3cIfQoSPortPriorityTrustTrustType_Type()
)
h3cIfQoSPortPriorityTrustTrustType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfQoSPortPriorityTrustTrustType.setStatus("current")


class _H3cIfQoSPortPriorityTrustOvercastType_Type(Integer32):
    """Custom type h3cIfQoSPortPriorityTrustOvercastType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOvercast", 1),
          ("overcastCOS", 3),
          ("overcastDSCP", 2))
    )


_H3cIfQoSPortPriorityTrustOvercastType_Type.__name__ = "Integer32"
_H3cIfQoSPortPriorityTrustOvercastType_Object = MibTableColumn
h3cIfQoSPortPriorityTrustOvercastType = _H3cIfQoSPortPriorityTrustOvercastType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 7, 1, 2, 1, 2),
    _H3cIfQoSPortPriorityTrustOvercastType_Type()
)
h3cIfQoSPortPriorityTrustOvercastType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIfQoSPortPriorityTrustOvercastType.setStatus("current")
_H3cIfQoSMapObjects_ObjectIdentity = ObjectIdentity
h3cIfQoSMapObjects = _H3cIfQoSMapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 9)
)
_H3cIfQoSPriMapConfigGroup_ObjectIdentity = ObjectIdentity
h3cIfQoSPriMapConfigGroup = _H3cIfQoSPriMapConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 9, 1)
)
_H3cIfQoSPriMapGroupNextIndex_Type = Integer32
_H3cIfQoSPriMapGroupNextIndex_Object = MibScalar
h3cIfQoSPriMapGroupNextIndex = _H3cIfQoSPriMapGroupNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 9, 1, 1),
    _H3cIfQoSPriMapGroupNextIndex_Type()
)
h3cIfQoSPriMapGroupNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIfQoSPriMapGroupNextIndex.setStatus("current")
_H3cIfQoSPriMapGroupTable_Object = MibTable
h3cIfQoSPriMapGroupTable = _H3cIfQoSPriMapGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    h3cIfQoSPriMapGroupTable.setStatus("current")
_H3cIfQoSPriMapGroupEntry_Object = MibTableRow
h3cIfQoSPriMapGroupEntry = _H3cIfQoSPriMapGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 9, 1, 2, 1)
)
h3cIfQoSPriMapGroupEntry.setIndexNames(
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSPriMapGroupIndex"),
)
if mibBuilder.loadTexts:
    h3cIfQoSPriMapGroupEntry.setStatus("current")
_H3cIfQoSPriMapGroupIndex_Type = Integer32
_H3cIfQoSPriMapGroupIndex_Object = MibTableColumn
h3cIfQoSPriMapGroupIndex = _H3cIfQoSPriMapGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 9, 1, 2, 1, 1),
    _H3cIfQoSPriMapGroupIndex_Type()
)
h3cIfQoSPriMapGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfQoSPriMapGroupIndex.setStatus("current")


class _H3cIfQoSPriMapGroupType_Type(Integer32):
    """Custom type h3cIfQoSPriMapGroupType based on Integer32"""
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
        *(("dot1p-dp", 2),
          ("dot1p-dscp", 3),
          ("dot1p-lp", 4),
          ("dscp-dot1p", 5),
          ("dscp-dp", 6),
          ("dscp-dscp", 7),
          ("dscp-lp", 8),
          ("exp-dp", 9),
          ("exp-lp", 10),
          ("userdefined", 1))
    )


_H3cIfQoSPriMapGroupType_Type.__name__ = "Integer32"
_H3cIfQoSPriMapGroupType_Object = MibTableColumn
h3cIfQoSPriMapGroupType = _H3cIfQoSPriMapGroupType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 9, 1, 2, 1, 2),
    _H3cIfQoSPriMapGroupType_Type()
)
h3cIfQoSPriMapGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSPriMapGroupType.setStatus("current")


class _H3cIfQoSPriMapGroupName_Type(OctetString):
    """Custom type h3cIfQoSPriMapGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_H3cIfQoSPriMapGroupName_Type.__name__ = "OctetString"
_H3cIfQoSPriMapGroupName_Object = MibTableColumn
h3cIfQoSPriMapGroupName = _H3cIfQoSPriMapGroupName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 9, 1, 2, 1, 3),
    _H3cIfQoSPriMapGroupName_Type()
)
h3cIfQoSPriMapGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSPriMapGroupName.setStatus("current")
_H3cIfQoSPriMapGroupRowStatus_Type = RowStatus
_H3cIfQoSPriMapGroupRowStatus_Object = MibTableColumn
h3cIfQoSPriMapGroupRowStatus = _H3cIfQoSPriMapGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 9, 1, 2, 1, 4),
    _H3cIfQoSPriMapGroupRowStatus_Type()
)
h3cIfQoSPriMapGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSPriMapGroupRowStatus.setStatus("current")
_H3cIfQoSPriMapContentTable_Object = MibTable
h3cIfQoSPriMapContentTable = _H3cIfQoSPriMapContentTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 9, 1, 3)
)
if mibBuilder.loadTexts:
    h3cIfQoSPriMapContentTable.setStatus("current")
_H3cIfQoSPriMapContentEntry_Object = MibTableRow
h3cIfQoSPriMapContentEntry = _H3cIfQoSPriMapContentEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 9, 1, 3, 1)
)
h3cIfQoSPriMapContentEntry.setIndexNames(
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSPriMapGroupIndex"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cIfQoSPriMapGroupImportValue"),
)
if mibBuilder.loadTexts:
    h3cIfQoSPriMapContentEntry.setStatus("current")


class _H3cIfQoSPriMapGroupImportValue_Type(Integer32):
    """Custom type h3cIfQoSPriMapGroupImportValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_H3cIfQoSPriMapGroupImportValue_Type.__name__ = "Integer32"
_H3cIfQoSPriMapGroupImportValue_Object = MibTableColumn
h3cIfQoSPriMapGroupImportValue = _H3cIfQoSPriMapGroupImportValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 9, 1, 3, 1, 1),
    _H3cIfQoSPriMapGroupImportValue_Type()
)
h3cIfQoSPriMapGroupImportValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIfQoSPriMapGroupImportValue.setStatus("current")


class _H3cIfQoSPriMapGroupExportValue_Type(Integer32):
    """Custom type h3cIfQoSPriMapGroupExportValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_H3cIfQoSPriMapGroupExportValue_Type.__name__ = "Integer32"
_H3cIfQoSPriMapGroupExportValue_Object = MibTableColumn
h3cIfQoSPriMapGroupExportValue = _H3cIfQoSPriMapGroupExportValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 9, 1, 3, 1, 2),
    _H3cIfQoSPriMapGroupExportValue_Type()
)
h3cIfQoSPriMapGroupExportValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSPriMapGroupExportValue.setStatus("current")
_H3cIfQoSPriMapContentRowStatus_Type = RowStatus
_H3cIfQoSPriMapContentRowStatus_Object = MibTableColumn
h3cIfQoSPriMapContentRowStatus = _H3cIfQoSPriMapContentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 9, 1, 3, 1, 3),
    _H3cIfQoSPriMapContentRowStatus_Type()
)
h3cIfQoSPriMapContentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSPriMapContentRowStatus.setStatus("current")
_H3cIfQoSL3PlusObjects_ObjectIdentity = ObjectIdentity
h3cIfQoSL3PlusObjects = _H3cIfQoSL3PlusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 10)
)
_H3cIfQoSPortBindingGroup_ObjectIdentity = ObjectIdentity
h3cIfQoSPortBindingGroup = _H3cIfQoSPortBindingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 10, 1)
)
_H3cIfQoSPortBindingTable_Object = MibTable
h3cIfQoSPortBindingTable = _H3cIfQoSPortBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 10, 1, 1)
)
if mibBuilder.loadTexts:
    h3cIfQoSPortBindingTable.setStatus("current")
_H3cIfQoSPortBindingEntry_Object = MibTableRow
h3cIfQoSPortBindingEntry = _H3cIfQoSPortBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 10, 1, 1, 1)
)
h3cIfQoSPortBindingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cIfQoSPortBindingEntry.setStatus("current")
_H3cIfQoSBindingIf_Type = Integer32
_H3cIfQoSBindingIf_Object = MibTableColumn
h3cIfQoSBindingIf = _H3cIfQoSBindingIf_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 10, 1, 1, 1, 1),
    _H3cIfQoSBindingIf_Type()
)
h3cIfQoSBindingIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSBindingIf.setStatus("current")
_H3cIfQoSBindingRowStatus_Type = RowStatus
_H3cIfQoSBindingRowStatus_Object = MibTableColumn
h3cIfQoSBindingRowStatus = _H3cIfQoSBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 10, 1, 1, 1, 2),
    _H3cIfQoSBindingRowStatus_Type()
)
h3cIfQoSBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIfQoSBindingRowStatus.setStatus("current")
_H3cQoSTraStaObjects_ObjectIdentity = ObjectIdentity
h3cQoSTraStaObjects = _H3cQoSTraStaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 11)
)
_H3cQoSTraStaConfigGroup_ObjectIdentity = ObjectIdentity
h3cQoSTraStaConfigGroup = _H3cQoSTraStaConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 11, 1)
)
_H3cQoSIfTraStaConfigInfoTable_Object = MibTable
h3cQoSIfTraStaConfigInfoTable = _H3cQoSIfTraStaConfigInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 11, 1, 1)
)
if mibBuilder.loadTexts:
    h3cQoSIfTraStaConfigInfoTable.setStatus("current")
_H3cQoSIfTraStaConfigInfoEntry_Object = MibTableRow
h3cQoSIfTraStaConfigInfoEntry = _H3cQoSIfTraStaConfigInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 11, 1, 1, 1)
)
h3cQoSIfTraStaConfigInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cQoSIfTraStaConfigDirection"),
)
if mibBuilder.loadTexts:
    h3cQoSIfTraStaConfigInfoEntry.setStatus("current")
_H3cQoSIfTraStaConfigDirection_Type = Direction
_H3cQoSIfTraStaConfigDirection_Object = MibTableColumn
h3cQoSIfTraStaConfigDirection = _H3cQoSIfTraStaConfigDirection_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 11, 1, 1, 1, 1),
    _H3cQoSIfTraStaConfigDirection_Type()
)
h3cQoSIfTraStaConfigDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQoSIfTraStaConfigDirection.setStatus("current")


class _H3cQoSIfTraStaConfigQueue_Type(OctetString):
    """Custom type h3cQoSIfTraStaConfigQueue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_H3cQoSIfTraStaConfigQueue_Type.__name__ = "OctetString"
_H3cQoSIfTraStaConfigQueue_Object = MibTableColumn
h3cQoSIfTraStaConfigQueue = _H3cQoSIfTraStaConfigQueue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 11, 1, 1, 1, 2),
    _H3cQoSIfTraStaConfigQueue_Type()
)
h3cQoSIfTraStaConfigQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSIfTraStaConfigQueue.setStatus("current")


class _H3cQoSIfTraStaConfigDot1p_Type(OctetString):
    """Custom type h3cQoSIfTraStaConfigDot1p based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_H3cQoSIfTraStaConfigDot1p_Type.__name__ = "OctetString"
_H3cQoSIfTraStaConfigDot1p_Object = MibTableColumn
h3cQoSIfTraStaConfigDot1p = _H3cQoSIfTraStaConfigDot1p_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 11, 1, 1, 1, 3),
    _H3cQoSIfTraStaConfigDot1p_Type()
)
h3cQoSIfTraStaConfigDot1p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSIfTraStaConfigDot1p.setStatus("current")


class _H3cQoSIfTraStaConfigDscp_Type(OctetString):
    """Custom type h3cQoSIfTraStaConfigDscp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_H3cQoSIfTraStaConfigDscp_Type.__name__ = "OctetString"
_H3cQoSIfTraStaConfigDscp_Object = MibTableColumn
h3cQoSIfTraStaConfigDscp = _H3cQoSIfTraStaConfigDscp_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 11, 1, 1, 1, 4),
    _H3cQoSIfTraStaConfigDscp_Type()
)
h3cQoSIfTraStaConfigDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSIfTraStaConfigDscp.setStatus("current")


class _H3cQoSIfTraStaConfigVlan_Type(OctetString):
    """Custom type h3cQoSIfTraStaConfigVlan based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )


_H3cQoSIfTraStaConfigVlan_Type.__name__ = "OctetString"
_H3cQoSIfTraStaConfigVlan_Object = MibTableColumn
h3cQoSIfTraStaConfigVlan = _H3cQoSIfTraStaConfigVlan_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 11, 1, 1, 1, 5),
    _H3cQoSIfTraStaConfigVlan_Type()
)
h3cQoSIfTraStaConfigVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSIfTraStaConfigVlan.setStatus("current")
_H3cQoSIfTraStaConfigStatus_Type = RowStatus
_H3cQoSIfTraStaConfigStatus_Object = MibTableColumn
h3cQoSIfTraStaConfigStatus = _H3cQoSIfTraStaConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 11, 1, 1, 1, 6),
    _H3cQoSIfTraStaConfigStatus_Type()
)
h3cQoSIfTraStaConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cQoSIfTraStaConfigStatus.setStatus("current")
_H3cQoSTraStaRunGroup_ObjectIdentity = ObjectIdentity
h3cQoSTraStaRunGroup = _H3cQoSTraStaRunGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 11, 2)
)
_H3cQoSIfTraStaRunInfoTable_Object = MibTable
h3cQoSIfTraStaRunInfoTable = _H3cQoSIfTraStaRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 11, 2, 1)
)
if mibBuilder.loadTexts:
    h3cQoSIfTraStaRunInfoTable.setStatus("current")
_H3cQoSIfTraStaRunInfoEntry_Object = MibTableRow
h3cQoSIfTraStaRunInfoEntry = _H3cQoSIfTraStaRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 11, 2, 1, 1)
)
h3cQoSIfTraStaRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cQoSIfTraStaRunObjectType"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cQoSIfTraStaRunObjectValue"),
    (0, "A3COM-HUAWEI-IFQOS2-MIB", "h3cQoSIfTraStaRunDirection"),
)
if mibBuilder.loadTexts:
    h3cQoSIfTraStaRunInfoEntry.setStatus("current")


class _H3cQoSIfTraStaRunObjectType_Type(Integer32):
    """Custom type h3cQoSIfTraStaRunObjectType based on Integer32"""
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
        *(("dot1p", 2),
          ("dscp", 3),
          ("queue", 1),
          ("vlanID", 4))
    )


_H3cQoSIfTraStaRunObjectType_Type.__name__ = "Integer32"
_H3cQoSIfTraStaRunObjectType_Object = MibTableColumn
h3cQoSIfTraStaRunObjectType = _H3cQoSIfTraStaRunObjectType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 11, 2, 1, 1, 1),
    _H3cQoSIfTraStaRunObjectType_Type()
)
h3cQoSIfTraStaRunObjectType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQoSIfTraStaRunObjectType.setStatus("current")
_H3cQoSIfTraStaRunObjectValue_Type = Integer32
_H3cQoSIfTraStaRunObjectValue_Object = MibTableColumn
h3cQoSIfTraStaRunObjectValue = _H3cQoSIfTraStaRunObjectValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 11, 2, 1, 1, 2),
    _H3cQoSIfTraStaRunObjectValue_Type()
)
h3cQoSIfTraStaRunObjectValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQoSIfTraStaRunObjectValue.setStatus("current")
_H3cQoSIfTraStaRunDirection_Type = Direction
_H3cQoSIfTraStaRunDirection_Object = MibTableColumn
h3cQoSIfTraStaRunDirection = _H3cQoSIfTraStaRunDirection_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 11, 2, 1, 1, 3),
    _H3cQoSIfTraStaRunDirection_Type()
)
h3cQoSIfTraStaRunDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cQoSIfTraStaRunDirection.setStatus("current")
_H3cQoSIfTraStaRunPassPackets_Type = Counter64
_H3cQoSIfTraStaRunPassPackets_Object = MibTableColumn
h3cQoSIfTraStaRunPassPackets = _H3cQoSIfTraStaRunPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 11, 2, 1, 1, 4),
    _H3cQoSIfTraStaRunPassPackets_Type()
)
h3cQoSIfTraStaRunPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cQoSIfTraStaRunPassPackets.setStatus("current")
_H3cQoSIfTraStaRunDropPackets_Type = Counter64
_H3cQoSIfTraStaRunDropPackets_Object = MibTableColumn
h3cQoSIfTraStaRunDropPackets = _H3cQoSIfTraStaRunDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 11, 2, 1, 1, 5),
    _H3cQoSIfTraStaRunDropPackets_Type()
)
h3cQoSIfTraStaRunDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cQoSIfTraStaRunDropPackets.setStatus("current")
_H3cQoSIfTraStaRunPassBytes_Type = Counter64
_H3cQoSIfTraStaRunPassBytes_Object = MibTableColumn
h3cQoSIfTraStaRunPassBytes = _H3cQoSIfTraStaRunPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 11, 2, 1, 1, 6),
    _H3cQoSIfTraStaRunPassBytes_Type()
)
h3cQoSIfTraStaRunPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cQoSIfTraStaRunPassBytes.setStatus("current")
_H3cQoSIfTraStaRunDropBytes_Type = Counter64
_H3cQoSIfTraStaRunDropBytes_Object = MibTableColumn
h3cQoSIfTraStaRunDropBytes = _H3cQoSIfTraStaRunDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 11, 2, 1, 1, 7),
    _H3cQoSIfTraStaRunDropBytes_Type()
)
h3cQoSIfTraStaRunDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cQoSIfTraStaRunDropBytes.setStatus("current")
_H3cQoSIfTraStaRunPassPPS_Type = Counter64
_H3cQoSIfTraStaRunPassPPS_Object = MibTableColumn
h3cQoSIfTraStaRunPassPPS = _H3cQoSIfTraStaRunPassPPS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 11, 2, 1, 1, 8),
    _H3cQoSIfTraStaRunPassPPS_Type()
)
h3cQoSIfTraStaRunPassPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cQoSIfTraStaRunPassPPS.setStatus("current")
_H3cQoSIfTraStaRunPassBPS_Type = Counter64
_H3cQoSIfTraStaRunPassBPS_Object = MibTableColumn
h3cQoSIfTraStaRunPassBPS = _H3cQoSIfTraStaRunPassBPS_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 65, 1, 11, 2, 1, 1, 9),
    _H3cQoSIfTraStaRunPassBPS_Type()
)
h3cQoSIfTraStaRunPassBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cQoSIfTraStaRunPassBPS.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-IFQOS2-MIB",
    **{"CarAction": CarAction,
       "PriorityQueue": PriorityQueue,
       "Direction": Direction,
       "h3cQos2": h3cQos2,
       "h3cIfQos2": h3cIfQos2,
       "h3cIfQoSHardwareQueueObjects": h3cIfQoSHardwareQueueObjects,
       "h3cIfQoSHardwareQueueConfigGroup": h3cIfQoSHardwareQueueConfigGroup,
       "h3cIfQoSQSModeTable": h3cIfQoSQSModeTable,
       "h3cIfQoSQSModeEntry": h3cIfQoSQSModeEntry,
       "h3cIfQoSQSMode": h3cIfQoSQSMode,
       "h3cIfQoSQSWeightTable": h3cIfQoSQSWeightTable,
       "h3cIfQoSQSWeightEntry": h3cIfQoSQSWeightEntry,
       "h3cIfQoSQueueID": h3cIfQoSQueueID,
       "h3cIfQoSQueueGroupType": h3cIfQoSQueueGroupType,
       "h3cIfQoSQSType": h3cIfQoSQSType,
       "h3cIfQoSQSValue": h3cIfQoSQSValue,
       "h3cIfQoSQSMaxDelay": h3cIfQoSQSMaxDelay,
       "h3cIfQoSQSMinBandwidth": h3cIfQoSQSMinBandwidth,
       "h3cIfQoSHardwareQueueRunInfoGroup": h3cIfQoSHardwareQueueRunInfoGroup,
       "h3cIfQoSHardwareQueueRunInfoTable": h3cIfQoSHardwareQueueRunInfoTable,
       "h3cIfQoSHardwareQueueRunInfoEntry": h3cIfQoSHardwareQueueRunInfoEntry,
       "h3cIfQoSPassPackets": h3cIfQoSPassPackets,
       "h3cIfQoSDropPackets": h3cIfQoSDropPackets,
       "h3cIfQoSPassBytes": h3cIfQoSPassBytes,
       "h3cIfQoSPassPPS": h3cIfQoSPassPPS,
       "h3cIfQoSPassBPS": h3cIfQoSPassBPS,
       "h3cIfQoSDropBytes": h3cIfQoSDropBytes,
       "h3cIfQoSQueueLengthInPkts": h3cIfQoSQueueLengthInPkts,
       "h3cIfQoSQueueLengthInBytes": h3cIfQoSQueueLengthInBytes,
       "h3cIfQoSCurQueuePkts": h3cIfQoSCurQueuePkts,
       "h3cIfQoSCurQueueBytes": h3cIfQoSCurQueueBytes,
       "h3cIfQoSCurQueuePPS": h3cIfQoSCurQueuePPS,
       "h3cIfQoSCurQueueBPS": h3cIfQoSCurQueueBPS,
       "h3cIfQoSTailDropPkts": h3cIfQoSTailDropPkts,
       "h3cIfQoSTailDropBytes": h3cIfQoSTailDropBytes,
       "h3cIfQoSTailDropPPS": h3cIfQoSTailDropPPS,
       "h3cIfQoSTailDropBPS": h3cIfQoSTailDropBPS,
       "h3cIfQoSWredDropPkts": h3cIfQoSWredDropPkts,
       "h3cIfQoSWredDropBytes": h3cIfQoSWredDropBytes,
       "h3cIfQoSWredDropPPS": h3cIfQoSWredDropPPS,
       "h3cIfQoSWredDropBPS": h3cIfQoSWredDropBPS,
       "h3cIfQoSHQueueTcpRunInfoTable": h3cIfQoSHQueueTcpRunInfoTable,
       "h3cIfQoSHQueueTcpRunInfoEntry": h3cIfQoSHQueueTcpRunInfoEntry,
       "h3cIfQoSWredDropLPreNTcpPkts": h3cIfQoSWredDropLPreNTcpPkts,
       "h3cIfQoSWredDropLPreNTcpBytes": h3cIfQoSWredDropLPreNTcpBytes,
       "h3cIfQoSWredDropLPreNTcpPPS": h3cIfQoSWredDropLPreNTcpPPS,
       "h3cIfQoSWredDropLPreNTcpBPS": h3cIfQoSWredDropLPreNTcpBPS,
       "h3cIfQoSWredDropLPreTcpPkts": h3cIfQoSWredDropLPreTcpPkts,
       "h3cIfQoSWredDropLPreTcpBytes": h3cIfQoSWredDropLPreTcpBytes,
       "h3cIfQoSWredDropLPreTcpPPS": h3cIfQoSWredDropLPreTcpPPS,
       "h3cIfQoSWredDropLPreTcpBPS": h3cIfQoSWredDropLPreTcpBPS,
       "h3cIfQoSWredDropHPreNTcpPkts": h3cIfQoSWredDropHPreNTcpPkts,
       "h3cIfQoSWredDropHPreNTcpBytes": h3cIfQoSWredDropHPreNTcpBytes,
       "h3cIfQoSWredDropHPreNTcpPPS": h3cIfQoSWredDropHPreNTcpPPS,
       "h3cIfQoSWredDropHPreNTcpBPS": h3cIfQoSWredDropHPreNTcpBPS,
       "h3cIfQoSWredDropHPreTcpPkts": h3cIfQoSWredDropHPreTcpPkts,
       "h3cIfQoSWredDropHPreTcpBytes": h3cIfQoSWredDropHPreTcpBytes,
       "h3cIfQoSWredDropHPreTcpPPS": h3cIfQoSWredDropHPreTcpPPS,
       "h3cIfQoSWredDropHPreTcpBPS": h3cIfQoSWredDropHPreTcpBPS,
       "h3cIfQoSSoftwareQueueObjects": h3cIfQoSSoftwareQueueObjects,
       "h3cIfQoSFIFOObject": h3cIfQoSFIFOObject,
       "h3cIfQoSFIFOConfigTable": h3cIfQoSFIFOConfigTable,
       "h3cIfQoSFIFOConfigEntry": h3cIfQoSFIFOConfigEntry,
       "h3cIfQoSFIFOMaxQueueLen": h3cIfQoSFIFOMaxQueueLen,
       "h3cIfQoSFIFORunInfoTable": h3cIfQoSFIFORunInfoTable,
       "h3cIfQoSFIFORunInfoEntry": h3cIfQoSFIFORunInfoEntry,
       "h3cIfQoSFIFOSize": h3cIfQoSFIFOSize,
       "h3cIfQoSFIFODiscardPackets": h3cIfQoSFIFODiscardPackets,
       "h3cIfQoSPQObject": h3cIfQoSPQObject,
       "h3cIfQoSPQConfigGroup": h3cIfQoSPQConfigGroup,
       "h3cIfQoSPQDefaultTable": h3cIfQoSPQDefaultTable,
       "h3cIfQoSPQDefaultEntry": h3cIfQoSPQDefaultEntry,
       "h3cIfQoSPQListNumber": h3cIfQoSPQListNumber,
       "h3cIfQoSPQDefaultQueueType": h3cIfQoSPQDefaultQueueType,
       "h3cIfQoSPQQueueLengthTable": h3cIfQoSPQQueueLengthTable,
       "h3cIfQoSPQQueueLengthEntry": h3cIfQoSPQQueueLengthEntry,
       "h3cIfQoSPQQueueLengthType": h3cIfQoSPQQueueLengthType,
       "h3cIfQoSPQQueueLengthValue": h3cIfQoSPQQueueLengthValue,
       "h3cIfQoSPQClassRuleTable": h3cIfQoSPQClassRuleTable,
       "h3cIfQoSPQClassRuleEntry": h3cIfQoSPQClassRuleEntry,
       "h3cIfQoSPQClassRuleType": h3cIfQoSPQClassRuleType,
       "h3cIfQoSPQClassRuleValue": h3cIfQoSPQClassRuleValue,
       "h3cIfQoSPQClassRuleQueueType": h3cIfQoSPQClassRuleQueueType,
       "h3cIfQoSPQClassRowStatus": h3cIfQoSPQClassRowStatus,
       "h3cIfQoSPQApplyTable": h3cIfQoSPQApplyTable,
       "h3cIfQoSPQApplyEntry": h3cIfQoSPQApplyEntry,
       "h3cIfQoSPQApplyListNumber": h3cIfQoSPQApplyListNumber,
       "h3cIfQoSPQApplyRowStatus": h3cIfQoSPQApplyRowStatus,
       "h3cIfQoSPQRunInfoGroup": h3cIfQoSPQRunInfoGroup,
       "h3cIfQoSPQRunInfoTable": h3cIfQoSPQRunInfoTable,
       "h3cIfQoSPQRunInfoEntry": h3cIfQoSPQRunInfoEntry,
       "h3cIfQoSPQType": h3cIfQoSPQType,
       "h3cIfQoSPQSize": h3cIfQoSPQSize,
       "h3cIfQoSPQLength": h3cIfQoSPQLength,
       "h3cIfQoSPQDiscardPackets": h3cIfQoSPQDiscardPackets,
       "h3cIfQoSCQObject": h3cIfQoSCQObject,
       "h3cIfQoSCQConfigGroup": h3cIfQoSCQConfigGroup,
       "h3cIfQoSCQDefaultTable": h3cIfQoSCQDefaultTable,
       "h3cIfQoSCQDefaultEntry": h3cIfQoSCQDefaultEntry,
       "h3cIfQoSCQListNumber": h3cIfQoSCQListNumber,
       "h3cIfQoSCQDefaultQueueID": h3cIfQoSCQDefaultQueueID,
       "h3cIfQoSCQQueueLengthTable": h3cIfQoSCQQueueLengthTable,
       "h3cIfQoSCQQueueLengthEntry": h3cIfQoSCQQueueLengthEntry,
       "h3cIfQoSCQQueueID": h3cIfQoSCQQueueID,
       "h3cIfQoSCQQueueLength": h3cIfQoSCQQueueLength,
       "h3cIfQoSCQQueueServing": h3cIfQoSCQQueueServing,
       "h3cIfQoSCQClassRuleTable": h3cIfQoSCQClassRuleTable,
       "h3cIfQoSCQClassRuleEntry": h3cIfQoSCQClassRuleEntry,
       "h3cIfQoSCQClassRuleType": h3cIfQoSCQClassRuleType,
       "h3cIfQoSCQClassRuleValue": h3cIfQoSCQClassRuleValue,
       "h3cIfQoSCQClassRuleQueueID": h3cIfQoSCQClassRuleQueueID,
       "h3cIfQoSCQClassRowStatus": h3cIfQoSCQClassRowStatus,
       "h3cIfQoSCQApplyTable": h3cIfQoSCQApplyTable,
       "h3cIfQoSCQApplyEntry": h3cIfQoSCQApplyEntry,
       "h3cIfQoSCQApplyListNumber": h3cIfQoSCQApplyListNumber,
       "h3cIfQoSCQApplyRowStatus": h3cIfQoSCQApplyRowStatus,
       "h3cIfQoSCQRunInfoGroup": h3cIfQoSCQRunInfoGroup,
       "h3cIfQoSCQRunInfoTable": h3cIfQoSCQRunInfoTable,
       "h3cIfQoSCQRunInfoEntry": h3cIfQoSCQRunInfoEntry,
       "h3cIfQoSCQRunInfoSize": h3cIfQoSCQRunInfoSize,
       "h3cIfQoSCQRunInfoLength": h3cIfQoSCQRunInfoLength,
       "h3cIfQoSCQRunInfoDiscardPackets": h3cIfQoSCQRunInfoDiscardPackets,
       "h3cIfQoSWFQObject": h3cIfQoSWFQObject,
       "h3cIfQoSWFQConfigGroup": h3cIfQoSWFQConfigGroup,
       "h3cIfQoSWFQTable": h3cIfQoSWFQTable,
       "h3cIfQoSWFQEntry": h3cIfQoSWFQEntry,
       "h3cIfQoSWFQQueueLength": h3cIfQoSWFQQueueLength,
       "h3cIfQoSWFQQueueNumber": h3cIfQoSWFQQueueNumber,
       "h3cIfQoSWFQRowStatus": h3cIfQoSWFQRowStatus,
       "h3cIfQoSWFQType": h3cIfQoSWFQType,
       "h3cIfQoSWFQRunInfoGroup": h3cIfQoSWFQRunInfoGroup,
       "h3cIfQoSWFQRunInfoTable": h3cIfQoSWFQRunInfoTable,
       "h3cIfQoSWFQRunInfoEntry": h3cIfQoSWFQRunInfoEntry,
       "h3cIfQoSWFQSize": h3cIfQoSWFQSize,
       "h3cIfQoSWFQLength": h3cIfQoSWFQLength,
       "h3cIfQoSWFQDiscardPackets": h3cIfQoSWFQDiscardPackets,
       "h3cIfQoSWFQHashedActiveQueues": h3cIfQoSWFQHashedActiveQueues,
       "h3cIfQoSWFQHashedMaxActiveQueues": h3cIfQoSWFQHashedMaxActiveQueues,
       "h3fIfQosWFQhashedTotalQueues": h3fIfQosWFQhashedTotalQueues,
       "h3cIfQoSBandwidthGroup": h3cIfQoSBandwidthGroup,
       "h3cIfQoSBandwidthTable": h3cIfQoSBandwidthTable,
       "h3cIfQoSBandwidthEntry": h3cIfQoSBandwidthEntry,
       "h3cIfQoSMaxBandwidth": h3cIfQoSMaxBandwidth,
       "h3cIfQoSReservedBandwidthPct": h3cIfQoSReservedBandwidthPct,
       "h3cIfQoSBandwidthRowStatus": h3cIfQoSBandwidthRowStatus,
       "h3cIfQoSQmtokenGroup": h3cIfQoSQmtokenGroup,
       "h3cIfQoSQmtokenTable": h3cIfQoSQmtokenTable,
       "h3cIfQoSQmtokenEntry": h3cIfQoSQmtokenEntry,
       "h3cIfQoSQmtokenNumber": h3cIfQoSQmtokenNumber,
       "h3cIfQoSQmtokenRosStatus": h3cIfQoSQmtokenRosStatus,
       "h3cIfQoSRTPQObject": h3cIfQoSRTPQObject,
       "h3cIfQoSRTPQConfigGroup": h3cIfQoSRTPQConfigGroup,
       "h3cIfQoSRTPQConfigTable": h3cIfQoSRTPQConfigTable,
       "h3cIfQoSRTPQConfigEntry": h3cIfQoSRTPQConfigEntry,
       "h3cIfQoSRTPQStartPort": h3cIfQoSRTPQStartPort,
       "h3cIfQoSRTPQEndPort": h3cIfQoSRTPQEndPort,
       "h3cIfQoSRTPQReservedBandwidth": h3cIfQoSRTPQReservedBandwidth,
       "h3cIfQoSRTPQCbs": h3cIfQoSRTPQCbs,
       "h3cIfQoSRTPQRowStatus": h3cIfQoSRTPQRowStatus,
       "h3cIfQoSRTPQRunInfoGroup": h3cIfQoSRTPQRunInfoGroup,
       "h3cIfQoSRTPQRunInfoTable": h3cIfQoSRTPQRunInfoTable,
       "h3cIfQoSRTPQRunInfoEntry": h3cIfQoSRTPQRunInfoEntry,
       "h3cIfQoSRTPQPacketNumber": h3cIfQoSRTPQPacketNumber,
       "h3cIfQoSRTPQPacketSize": h3cIfQoSRTPQPacketSize,
       "h3cIfQoSRTPQOutputPackets": h3cIfQoSRTPQOutputPackets,
       "h3cIfQoSRTPQDiscardPackets": h3cIfQoSRTPQDiscardPackets,
       "h3cIfQoSCarListObject": h3cIfQoSCarListObject,
       "h3cIfQoCarListGroup": h3cIfQoCarListGroup,
       "h3cIfQoSCarlTable": h3cIfQoSCarlTable,
       "h3cIfQoSCarlEntry": h3cIfQoSCarlEntry,
       "h3cIfQoSCarlListNum": h3cIfQoSCarlListNum,
       "h3cIfQoSCarlParaType": h3cIfQoSCarlParaType,
       "h3cIfQoSCarlParaValue": h3cIfQoSCarlParaValue,
       "h3cIfQoSCarlRowStatus": h3cIfQoSCarlRowStatus,
       "h3cIfQoSLineRateObjects": h3cIfQoSLineRateObjects,
       "h3cIfQoSLRConfigTable": h3cIfQoSLRConfigTable,
       "h3cIfQoSLRConfigEntry": h3cIfQoSLRConfigEntry,
       "h3cIfQoSLRDirection": h3cIfQoSLRDirection,
       "h3cIfQoSLRCir": h3cIfQoSLRCir,
       "h3cIfQoSLRCbs": h3cIfQoSLRCbs,
       "h3cIfQoSLREbs": h3cIfQoSLREbs,
       "h3cIfQoSRowStatus": h3cIfQoSRowStatus,
       "h3cIfQoSLRPir": h3cIfQoSLRPir,
       "h3cIfQoSLRRunInfoTable": h3cIfQoSLRRunInfoTable,
       "h3cIfQoSLRRunInfoEntry": h3cIfQoSLRRunInfoEntry,
       "h3cIfQoSLRRunInfoPassedPackets": h3cIfQoSLRRunInfoPassedPackets,
       "h3cIfQoSLRRunInfoPassedBytes": h3cIfQoSLRRunInfoPassedBytes,
       "h3cIfQoSLRRunInfoDelayedPackets": h3cIfQoSLRRunInfoDelayedPackets,
       "h3cIfQoSLRRunInfoDelayedBytes": h3cIfQoSLRRunInfoDelayedBytes,
       "h3cIfQoSLRRunInfoActiveShaping": h3cIfQoSLRRunInfoActiveShaping,
       "h3cIfQoSCARObjects": h3cIfQoSCARObjects,
       "h3cIfQoSAggregativeCarGroup": h3cIfQoSAggregativeCarGroup,
       "h3cIfQoSAggregativeCarNextIndex": h3cIfQoSAggregativeCarNextIndex,
       "h3cIfQoSAggregativeCarConfigTable": h3cIfQoSAggregativeCarConfigTable,
       "h3cIfQoSAggregativeCarConfigEntry": h3cIfQoSAggregativeCarConfigEntry,
       "h3cIfQoSAggregativeCarIndex": h3cIfQoSAggregativeCarIndex,
       "h3cIfQoSAggregativeCarName": h3cIfQoSAggregativeCarName,
       "h3cIfQoSAggregativeCarCir": h3cIfQoSAggregativeCarCir,
       "h3cIfQoSAggregativeCarCbs": h3cIfQoSAggregativeCarCbs,
       "h3cIfQoSAggregativeCarEbs": h3cIfQoSAggregativeCarEbs,
       "h3cIfQoSAggregativeCarPir": h3cIfQoSAggregativeCarPir,
       "h3cIfQoSAggregativeCarGreenActionType": h3cIfQoSAggregativeCarGreenActionType,
       "h3cIfQoSAggregativeCarGreenActionValue": h3cIfQoSAggregativeCarGreenActionValue,
       "h3cIfQoSAggregativeCarYellowActionType": h3cIfQoSAggregativeCarYellowActionType,
       "h3cIfQoSAggregativeCarYellowActionValue": h3cIfQoSAggregativeCarYellowActionValue,
       "h3cIfQoSAggregativeCarRedActionType": h3cIfQoSAggregativeCarRedActionType,
       "h3cIfQoSAggregativeCarRedActionValue": h3cIfQoSAggregativeCarRedActionValue,
       "h3cIfQoSAggregativeCarType": h3cIfQoSAggregativeCarType,
       "h3cIfQoSAggregativeCarRowStatus": h3cIfQoSAggregativeCarRowStatus,
       "h3cIfQoSAggregativeCarApplyTable": h3cIfQoSAggregativeCarApplyTable,
       "h3cIfQoSAggregativeCarApplyEntry": h3cIfQoSAggregativeCarApplyEntry,
       "h3cIfQoSAggregativeCarApplyDirection": h3cIfQoSAggregativeCarApplyDirection,
       "h3cIfQoSAggregativeCarApplyRuleType": h3cIfQoSAggregativeCarApplyRuleType,
       "h3cIfQoSAggregativeCarApplyRuleValue": h3cIfQoSAggregativeCarApplyRuleValue,
       "h3cIfQoSAggregativeCarApplyCarIndex": h3cIfQoSAggregativeCarApplyCarIndex,
       "h3cIfQoSAggregativeCarApplyRowStatus": h3cIfQoSAggregativeCarApplyRowStatus,
       "h3cIfQoSAggregativeCarRunInfoTable": h3cIfQoSAggregativeCarRunInfoTable,
       "h3cIfQoSAggregativeCarRunInfoEntry": h3cIfQoSAggregativeCarRunInfoEntry,
       "h3cIfQoSAggregativeCarGreenPackets": h3cIfQoSAggregativeCarGreenPackets,
       "h3cIfQoSAggregativeCarGreenBytes": h3cIfQoSAggregativeCarGreenBytes,
       "h3cIfQoSAggregativeCarYellowPackets": h3cIfQoSAggregativeCarYellowPackets,
       "h3cIfQoSAggregativeCarYellowBytes": h3cIfQoSAggregativeCarYellowBytes,
       "h3cIfQoSAggregativeCarRedPackets": h3cIfQoSAggregativeCarRedPackets,
       "h3cIfQoSAggregativeCarRedBytes": h3cIfQoSAggregativeCarRedBytes,
       "h3cIfQoSTricolorCarGroup": h3cIfQoSTricolorCarGroup,
       "h3cIfQoSTricolorCarConfigTable": h3cIfQoSTricolorCarConfigTable,
       "h3cIfQoSTricolorCarConfigEntry": h3cIfQoSTricolorCarConfigEntry,
       "h3cIfQoSTricolorCarDirection": h3cIfQoSTricolorCarDirection,
       "h3cIfQoSTricolorCarType": h3cIfQoSTricolorCarType,
       "h3cIfQoSTricolorCarValue": h3cIfQoSTricolorCarValue,
       "h3cIfQoSTricolorCarCir": h3cIfQoSTricolorCarCir,
       "h3cIfQoSTricolorCarCbs": h3cIfQoSTricolorCarCbs,
       "h3cIfQoSTricolorCarEbs": h3cIfQoSTricolorCarEbs,
       "h3cIfQoSTricolorCarPir": h3cIfQoSTricolorCarPir,
       "h3cIfQoSTricolorCarGreenActionType": h3cIfQoSTricolorCarGreenActionType,
       "h3cIfQoSTricolorCarGreenActionValue": h3cIfQoSTricolorCarGreenActionValue,
       "h3cIfQoSTricolorCarYellowActionType": h3cIfQoSTricolorCarYellowActionType,
       "h3cIfQoSTricolorCarYellowActionValue": h3cIfQoSTricolorCarYellowActionValue,
       "h3cIfQoSTricolorCarRedActionType": h3cIfQoSTricolorCarRedActionType,
       "h3cIfQoSTricolorCarRedActionValue": h3cIfQoSTricolorCarRedActionValue,
       "h3cIfQoSTricolorCarRowStatus": h3cIfQoSTricolorCarRowStatus,
       "h3cIfQoSTricolorCarRunInfoTable": h3cIfQoSTricolorCarRunInfoTable,
       "h3cIfQoSTricolorCarRunInfoEntry": h3cIfQoSTricolorCarRunInfoEntry,
       "h3cIfQoSTricolorCarGreenPackets": h3cIfQoSTricolorCarGreenPackets,
       "h3cIfQoSTricolorCarGreenBytes": h3cIfQoSTricolorCarGreenBytes,
       "h3cIfQoSTricolorCarYellowPackets": h3cIfQoSTricolorCarYellowPackets,
       "h3cIfQoSTricolorCarYellowBytes": h3cIfQoSTricolorCarYellowBytes,
       "h3cIfQoSTricolorCarRedPackets": h3cIfQoSTricolorCarRedPackets,
       "h3cIfQoSTricolorCarRedBytes": h3cIfQoSTricolorCarRedBytes,
       "h3cIfQoSGTSObjects": h3cIfQoSGTSObjects,
       "h3cIfQoSGTSConfigTable": h3cIfQoSGTSConfigTable,
       "h3cIfQoSGTSConfigEntry": h3cIfQoSGTSConfigEntry,
       "h3cIfQoSGTSClassRuleType": h3cIfQoSGTSClassRuleType,
       "h3cIfQoSGTSClassRuleValue": h3cIfQoSGTSClassRuleValue,
       "h3cIfQoSGTSCir": h3cIfQoSGTSCir,
       "h3cIfQoSGTSCbs": h3cIfQoSGTSCbs,
       "h3cIfQoSGTSEbs": h3cIfQoSGTSEbs,
       "h3cIfQoSGTSQueueLength": h3cIfQoSGTSQueueLength,
       "h3cIfQoSGTSConfigRowStatus": h3cIfQoSGTSConfigRowStatus,
       "h3cIfQoSGTSRunInfoTable": h3cIfQoSGTSRunInfoTable,
       "h3cIfQoSGTSRunInfoEntry": h3cIfQoSGTSRunInfoEntry,
       "h3cIfQoSGTSQueueSize": h3cIfQoSGTSQueueSize,
       "h3cIfQoSGTSPassedPackets": h3cIfQoSGTSPassedPackets,
       "h3cIfQoSGTSPassedBytes": h3cIfQoSGTSPassedBytes,
       "h3cIfQoSGTSDiscardPackets": h3cIfQoSGTSDiscardPackets,
       "h3cIfQoSGTSDiscardBytes": h3cIfQoSGTSDiscardBytes,
       "h3cIfQoSGTSDelayedPackets": h3cIfQoSGTSDelayedPackets,
       "h3cIfQoSGTSDelayedBytes": h3cIfQoSGTSDelayedBytes,
       "h3cIfQoSWREDObjects": h3cIfQoSWREDObjects,
       "h3cIfQoSWredGroupGroup": h3cIfQoSWredGroupGroup,
       "h3cIfQoSWredGroupNextIndex": h3cIfQoSWredGroupNextIndex,
       "h3cIfQoSWredGroupTable": h3cIfQoSWredGroupTable,
       "h3cIfQoSWredGroupEntry": h3cIfQoSWredGroupEntry,
       "h3cIfQoSWredGroupIndex": h3cIfQoSWredGroupIndex,
       "h3cIfQoSWredGroupName": h3cIfQoSWredGroupName,
       "h3cIfQoSWredGroupType": h3cIfQoSWredGroupType,
       "h3cIfQoSWredGroupWeightingConstant": h3cIfQoSWredGroupWeightingConstant,
       "h3cIfQoSWredGroupRowStatus": h3cIfQoSWredGroupRowStatus,
       "h3cIfQoSWredGroupContentTable": h3cIfQoSWredGroupContentTable,
       "h3cIfQoSWredGroupContentEntry": h3cIfQoSWredGroupContentEntry,
       "h3cIfQoSWredGroupContentIndex": h3cIfQoSWredGroupContentIndex,
       "h3cIfQoSWredGroupContentSubIndex": h3cIfQoSWredGroupContentSubIndex,
       "h3cIfQoSWredLowLimit": h3cIfQoSWredLowLimit,
       "h3cIfQoSWredHighLimit": h3cIfQoSWredHighLimit,
       "h3cIfQoSWredDiscardProb": h3cIfQoSWredDiscardProb,
       "h3cIfQoSWredGroupExponent": h3cIfQoSWredGroupExponent,
       "h3cIfQoSWredRowStatus": h3cIfQoSWredRowStatus,
       "h3cIfQoSWredGroupApplyIfTable": h3cIfQoSWredGroupApplyIfTable,
       "h3cIfQoSWredGroupApplyIfEntry": h3cIfQoSWredGroupApplyIfEntry,
       "h3cIfQoSWredGroupApplyIndex": h3cIfQoSWredGroupApplyIndex,
       "h3cIfQoSWredGroupApplyName": h3cIfQoSWredGroupApplyName,
       "h3cIfQoSWredGroupIfRowStatus": h3cIfQoSWredGroupIfRowStatus,
       "h3cIfQoSWredApplyIfRunInfoTable": h3cIfQoSWredApplyIfRunInfoTable,
       "h3cIfQoSWredApplyIfRunInfoEntry": h3cIfQoSWredApplyIfRunInfoEntry,
       "h3cIfQoSWredPreRandomDropNum": h3cIfQoSWredPreRandomDropNum,
       "h3cIfQoSWredPreTailDropNum": h3cIfQoSWredPreTailDropNum,
       "h3cIfQoSPortWredGroup": h3cIfQoSPortWredGroup,
       "h3cIfQoSPortWredWeightConstantTable": h3cIfQoSPortWredWeightConstantTable,
       "h3cIfQoSPortWredWeightConstantEntry": h3cIfQoSPortWredWeightConstantEntry,
       "h3cIfQoSPortWredEnable": h3cIfQoSPortWredEnable,
       "h3cIfQoSPortWredWeightConstant": h3cIfQoSPortWredWeightConstant,
       "h3cIfQoSPortWredWeightConstantRowStatus": h3cIfQoSPortWredWeightConstantRowStatus,
       "h3cIfQoSPortWredPreConfigTable": h3cIfQoSPortWredPreConfigTable,
       "h3cIfQoSPortWredPreConfigEntry": h3cIfQoSPortWredPreConfigEntry,
       "h3cIfQoSPortWredPreID": h3cIfQoSPortWredPreID,
       "h3cIfQoSPortWredPreLowLimit": h3cIfQoSPortWredPreLowLimit,
       "h3cIfQoSPortWredPreHighLimit": h3cIfQoSPortWredPreHighLimit,
       "h3cIfQoSPortWredPreDiscardProbability": h3cIfQoSPortWredPreDiscardProbability,
       "h3cIfQoSPortWredPreRowStatus": h3cIfQoSPortWredPreRowStatus,
       "h3cIfQoSPortWredRunInfoTable": h3cIfQoSPortWredRunInfoTable,
       "h3cIfQoSPortWredRunInfoEntry": h3cIfQoSPortWredRunInfoEntry,
       "h3cIfQoSWREDTailDropNum": h3cIfQoSWREDTailDropNum,
       "h3cIfQoSWREDRandomDropNum": h3cIfQoSWREDRandomDropNum,
       "h3cIfQoSPortPriorityObjects": h3cIfQoSPortPriorityObjects,
       "h3cIfQoSPortPriorityConfigGroup": h3cIfQoSPortPriorityConfigGroup,
       "h3cIfQoSPortPriorityTable": h3cIfQoSPortPriorityTable,
       "h3cIfQoSPortPriorityEntry": h3cIfQoSPortPriorityEntry,
       "h3cIfQoSPortPriorityValue": h3cIfQoSPortPriorityValue,
       "h3cIfQoSPortPirorityTrustTable": h3cIfQoSPortPirorityTrustTable,
       "h3cIfQoSPortPirorityTrustEntry": h3cIfQoSPortPirorityTrustEntry,
       "h3cIfQoSPortPriorityTrustTrustType": h3cIfQoSPortPriorityTrustTrustType,
       "h3cIfQoSPortPriorityTrustOvercastType": h3cIfQoSPortPriorityTrustOvercastType,
       "h3cIfQoSMapObjects": h3cIfQoSMapObjects,
       "h3cIfQoSPriMapConfigGroup": h3cIfQoSPriMapConfigGroup,
       "h3cIfQoSPriMapGroupNextIndex": h3cIfQoSPriMapGroupNextIndex,
       "h3cIfQoSPriMapGroupTable": h3cIfQoSPriMapGroupTable,
       "h3cIfQoSPriMapGroupEntry": h3cIfQoSPriMapGroupEntry,
       "h3cIfQoSPriMapGroupIndex": h3cIfQoSPriMapGroupIndex,
       "h3cIfQoSPriMapGroupType": h3cIfQoSPriMapGroupType,
       "h3cIfQoSPriMapGroupName": h3cIfQoSPriMapGroupName,
       "h3cIfQoSPriMapGroupRowStatus": h3cIfQoSPriMapGroupRowStatus,
       "h3cIfQoSPriMapContentTable": h3cIfQoSPriMapContentTable,
       "h3cIfQoSPriMapContentEntry": h3cIfQoSPriMapContentEntry,
       "h3cIfQoSPriMapGroupImportValue": h3cIfQoSPriMapGroupImportValue,
       "h3cIfQoSPriMapGroupExportValue": h3cIfQoSPriMapGroupExportValue,
       "h3cIfQoSPriMapContentRowStatus": h3cIfQoSPriMapContentRowStatus,
       "h3cIfQoSL3PlusObjects": h3cIfQoSL3PlusObjects,
       "h3cIfQoSPortBindingGroup": h3cIfQoSPortBindingGroup,
       "h3cIfQoSPortBindingTable": h3cIfQoSPortBindingTable,
       "h3cIfQoSPortBindingEntry": h3cIfQoSPortBindingEntry,
       "h3cIfQoSBindingIf": h3cIfQoSBindingIf,
       "h3cIfQoSBindingRowStatus": h3cIfQoSBindingRowStatus,
       "h3cQoSTraStaObjects": h3cQoSTraStaObjects,
       "h3cQoSTraStaConfigGroup": h3cQoSTraStaConfigGroup,
       "h3cQoSIfTraStaConfigInfoTable": h3cQoSIfTraStaConfigInfoTable,
       "h3cQoSIfTraStaConfigInfoEntry": h3cQoSIfTraStaConfigInfoEntry,
       "h3cQoSIfTraStaConfigDirection": h3cQoSIfTraStaConfigDirection,
       "h3cQoSIfTraStaConfigQueue": h3cQoSIfTraStaConfigQueue,
       "h3cQoSIfTraStaConfigDot1p": h3cQoSIfTraStaConfigDot1p,
       "h3cQoSIfTraStaConfigDscp": h3cQoSIfTraStaConfigDscp,
       "h3cQoSIfTraStaConfigVlan": h3cQoSIfTraStaConfigVlan,
       "h3cQoSIfTraStaConfigStatus": h3cQoSIfTraStaConfigStatus,
       "h3cQoSTraStaRunGroup": h3cQoSTraStaRunGroup,
       "h3cQoSIfTraStaRunInfoTable": h3cQoSIfTraStaRunInfoTable,
       "h3cQoSIfTraStaRunInfoEntry": h3cQoSIfTraStaRunInfoEntry,
       "h3cQoSIfTraStaRunObjectType": h3cQoSIfTraStaRunObjectType,
       "h3cQoSIfTraStaRunObjectValue": h3cQoSIfTraStaRunObjectValue,
       "h3cQoSIfTraStaRunDirection": h3cQoSIfTraStaRunDirection,
       "h3cQoSIfTraStaRunPassPackets": h3cQoSIfTraStaRunPassPackets,
       "h3cQoSIfTraStaRunDropPackets": h3cQoSIfTraStaRunDropPackets,
       "h3cQoSIfTraStaRunPassBytes": h3cQoSIfTraStaRunPassBytes,
       "h3cQoSIfTraStaRunDropBytes": h3cQoSIfTraStaRunDropBytes,
       "h3cQoSIfTraStaRunPassPPS": h3cQoSIfTraStaRunPassPPS,
       "h3cQoSIfTraStaRunPassBPS": h3cQoSIfTraStaRunPassBPS}
)
