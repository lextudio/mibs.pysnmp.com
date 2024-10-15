# SNMP MIB module (HPN-ICF-IFQOS2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-IFQOS2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:32 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddressIPv6,
 InetAddressPrefixLength) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6",
    "InetAddressPrefixLength")

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

hpnicfIfQos2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1)
)
hpnicfIfQos2.setRevisions(
        ("2013-11-28 00:00",)
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

_HpnicfQos2_ObjectIdentity = ObjectIdentity
hpnicfQos2 = _HpnicfQos2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65)
)
_HpnicfIfQoSHardwareQueueObjects_ObjectIdentity = ObjectIdentity
hpnicfIfQoSHardwareQueueObjects = _HpnicfIfQoSHardwareQueueObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1)
)
_HpnicfIfQoSHardwareQueueConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfIfQoSHardwareQueueConfigGroup = _HpnicfIfQoSHardwareQueueConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 1)
)
_HpnicfIfQoSQSModeTable_Object = MibTable
hpnicfIfQoSQSModeTable = _HpnicfIfQoSQSModeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSQSModeTable.setStatus("current")
_HpnicfIfQoSQSModeEntry_Object = MibTableRow
hpnicfIfQoSQSModeEntry = _HpnicfIfQoSQSModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 1, 1, 1)
)
hpnicfIfQoSQSModeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSQSModeEntry.setStatus("current")


class _HpnicfIfQoSQSMode_Type(Integer32):
    """Custom type hpnicfIfQoSQSMode based on Integer32"""
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
        *(("byteCountWfq", 9),
          ("byteCountWrr", 8),
          ("gmb", 10),
          ("hpnicffq", 6),
          ("sp", 1),
          ("sp0", 2),
          ("sp1", 3),
          ("sp2", 4),
          ("wrr", 5),
          ("wrr-sp", 7))
    )


_HpnicfIfQoSQSMode_Type.__name__ = "Integer32"
_HpnicfIfQoSQSMode_Object = MibTableColumn
hpnicfIfQoSQSMode = _HpnicfIfQoSQSMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 1, 1, 1, 1),
    _HpnicfIfQoSQSMode_Type()
)
hpnicfIfQoSQSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIfQoSQSMode.setStatus("current")
_HpnicfIfQoSQSWeightTable_Object = MibTable
hpnicfIfQoSQSWeightTable = _HpnicfIfQoSQSWeightTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSQSWeightTable.setStatus("current")
_HpnicfIfQoSQSWeightEntry_Object = MibTableRow
hpnicfIfQoSQSWeightEntry = _HpnicfIfQoSQSWeightEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 1, 2, 1)
)
hpnicfIfQoSQSWeightEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSQueueID"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSQSWeightEntry.setStatus("current")
_HpnicfIfQoSQueueID_Type = Integer32
_HpnicfIfQoSQueueID_Object = MibTableColumn
hpnicfIfQoSQueueID = _HpnicfIfQoSQueueID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 1, 2, 1, 1),
    _HpnicfIfQoSQueueID_Type()
)
hpnicfIfQoSQueueID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSQueueID.setStatus("current")


class _HpnicfIfQoSQueueGroupType_Type(Integer32):
    """Custom type hpnicfIfQoSQueueGroupType based on Integer32"""
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


_HpnicfIfQoSQueueGroupType_Type.__name__ = "Integer32"
_HpnicfIfQoSQueueGroupType_Object = MibTableColumn
hpnicfIfQoSQueueGroupType = _HpnicfIfQoSQueueGroupType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 1, 2, 1, 2),
    _HpnicfIfQoSQueueGroupType_Type()
)
hpnicfIfQoSQueueGroupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIfQoSQueueGroupType.setStatus("current")


class _HpnicfIfQoSQSType_Type(Integer32):
    """Custom type hpnicfIfQoSQSType based on Integer32"""
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


_HpnicfIfQoSQSType_Type.__name__ = "Integer32"
_HpnicfIfQoSQSType_Object = MibTableColumn
hpnicfIfQoSQSType = _HpnicfIfQoSQSType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 1, 2, 1, 3),
    _HpnicfIfQoSQSType_Type()
)
hpnicfIfQoSQSType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIfQoSQSType.setStatus("current")
_HpnicfIfQoSQSValue_Type = Integer32
_HpnicfIfQoSQSValue_Object = MibTableColumn
hpnicfIfQoSQSValue = _HpnicfIfQoSQSValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 1, 2, 1, 4),
    _HpnicfIfQoSQSValue_Type()
)
hpnicfIfQoSQSValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIfQoSQSValue.setStatus("current")


class _HpnicfIfQoSQSMaxDelay_Type(Integer32):
    """Custom type hpnicfIfQoSQSMaxDelay based on Integer32"""
    defaultValue = 9


_HpnicfIfQoSQSMaxDelay_Object = MibTableColumn
hpnicfIfQoSQSMaxDelay = _HpnicfIfQoSQSMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 1, 2, 1, 5),
    _HpnicfIfQoSQSMaxDelay_Type()
)
hpnicfIfQoSQSMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIfQoSQSMaxDelay.setStatus("current")
_HpnicfIfQoSQSMinBandwidth_Type = Integer32
_HpnicfIfQoSQSMinBandwidth_Object = MibTableColumn
hpnicfIfQoSQSMinBandwidth = _HpnicfIfQoSQSMinBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 1, 2, 1, 6),
    _HpnicfIfQoSQSMinBandwidth_Type()
)
hpnicfIfQoSQSMinBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIfQoSQSMinBandwidth.setStatus("current")


class _HpnicfIfQoSQSMinBandwidthPercent_Type(Unsigned32):
    """Custom type hpnicfIfQoSQSMinBandwidthPercent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
        ValueRangeConstraint(255, 255),
    )


_HpnicfIfQoSQSMinBandwidthPercent_Type.__name__ = "Unsigned32"
_HpnicfIfQoSQSMinBandwidthPercent_Object = MibTableColumn
hpnicfIfQoSQSMinBandwidthPercent = _HpnicfIfQoSQSMinBandwidthPercent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 1, 2, 1, 7),
    _HpnicfIfQoSQSMinBandwidthPercent_Type()
)
hpnicfIfQoSQSMinBandwidthPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIfQoSQSMinBandwidthPercent.setStatus("current")
_HpnicfIfQoSHardwareQueueRunInfoGroup_ObjectIdentity = ObjectIdentity
hpnicfIfQoSHardwareQueueRunInfoGroup = _HpnicfIfQoSHardwareQueueRunInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2)
)
_HpnicfIfQoSHardwareQueueRunInfoTable_Object = MibTable
hpnicfIfQoSHardwareQueueRunInfoTable = _HpnicfIfQoSHardwareQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSHardwareQueueRunInfoTable.setStatus("current")
_HpnicfIfQoSHardwareQueueRunInfoEntry_Object = MibTableRow
hpnicfIfQoSHardwareQueueRunInfoEntry = _HpnicfIfQoSHardwareQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 1, 1)
)
hpnicfIfQoSHardwareQueueRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSQueueID"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSHardwareQueueRunInfoEntry.setStatus("current")
_HpnicfIfQoSPassPackets_Type = Counter64
_HpnicfIfQoSPassPackets_Object = MibTableColumn
hpnicfIfQoSPassPackets = _HpnicfIfQoSPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 1, 1, 1),
    _HpnicfIfQoSPassPackets_Type()
)
hpnicfIfQoSPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSPassPackets.setStatus("current")
_HpnicfIfQoSDropPackets_Type = Counter64
_HpnicfIfQoSDropPackets_Object = MibTableColumn
hpnicfIfQoSDropPackets = _HpnicfIfQoSDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 1, 1, 2),
    _HpnicfIfQoSDropPackets_Type()
)
hpnicfIfQoSDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSDropPackets.setStatus("current")
_HpnicfIfQoSPassBytes_Type = Counter64
_HpnicfIfQoSPassBytes_Object = MibTableColumn
hpnicfIfQoSPassBytes = _HpnicfIfQoSPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 1, 1, 3),
    _HpnicfIfQoSPassBytes_Type()
)
hpnicfIfQoSPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSPassBytes.setStatus("current")
_HpnicfIfQoSPassPPS_Type = Unsigned32
_HpnicfIfQoSPassPPS_Object = MibTableColumn
hpnicfIfQoSPassPPS = _HpnicfIfQoSPassPPS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 1, 1, 4),
    _HpnicfIfQoSPassPPS_Type()
)
hpnicfIfQoSPassPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSPassPPS.setStatus("current")
_HpnicfIfQoSPassBPS_Type = Unsigned32
_HpnicfIfQoSPassBPS_Object = MibTableColumn
hpnicfIfQoSPassBPS = _HpnicfIfQoSPassBPS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 1, 1, 5),
    _HpnicfIfQoSPassBPS_Type()
)
hpnicfIfQoSPassBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSPassBPS.setStatus("current")
_HpnicfIfQoSDropBytes_Type = Counter64
_HpnicfIfQoSDropBytes_Object = MibTableColumn
hpnicfIfQoSDropBytes = _HpnicfIfQoSDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 1, 1, 6),
    _HpnicfIfQoSDropBytes_Type()
)
hpnicfIfQoSDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSDropBytes.setStatus("current")
_HpnicfIfQoSQueueLengthInPkts_Type = Unsigned32
_HpnicfIfQoSQueueLengthInPkts_Object = MibTableColumn
hpnicfIfQoSQueueLengthInPkts = _HpnicfIfQoSQueueLengthInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 1, 1, 7),
    _HpnicfIfQoSQueueLengthInPkts_Type()
)
hpnicfIfQoSQueueLengthInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSQueueLengthInPkts.setStatus("current")
_HpnicfIfQoSQueueLengthInBytes_Type = Unsigned32
_HpnicfIfQoSQueueLengthInBytes_Object = MibTableColumn
hpnicfIfQoSQueueLengthInBytes = _HpnicfIfQoSQueueLengthInBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 1, 1, 8),
    _HpnicfIfQoSQueueLengthInBytes_Type()
)
hpnicfIfQoSQueueLengthInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSQueueLengthInBytes.setStatus("current")
_HpnicfIfQoSCurQueuePkts_Type = Unsigned32
_HpnicfIfQoSCurQueuePkts_Object = MibTableColumn
hpnicfIfQoSCurQueuePkts = _HpnicfIfQoSCurQueuePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 1, 1, 9),
    _HpnicfIfQoSCurQueuePkts_Type()
)
hpnicfIfQoSCurQueuePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSCurQueuePkts.setStatus("current")
_HpnicfIfQoSCurQueueBytes_Type = Unsigned32
_HpnicfIfQoSCurQueueBytes_Object = MibTableColumn
hpnicfIfQoSCurQueueBytes = _HpnicfIfQoSCurQueueBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 1, 1, 10),
    _HpnicfIfQoSCurQueueBytes_Type()
)
hpnicfIfQoSCurQueueBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSCurQueueBytes.setStatus("current")
_HpnicfIfQoSCurQueuePPS_Type = Unsigned32
_HpnicfIfQoSCurQueuePPS_Object = MibTableColumn
hpnicfIfQoSCurQueuePPS = _HpnicfIfQoSCurQueuePPS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 1, 1, 11),
    _HpnicfIfQoSCurQueuePPS_Type()
)
hpnicfIfQoSCurQueuePPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSCurQueuePPS.setStatus("current")
_HpnicfIfQoSCurQueueBPS_Type = Unsigned32
_HpnicfIfQoSCurQueueBPS_Object = MibTableColumn
hpnicfIfQoSCurQueueBPS = _HpnicfIfQoSCurQueueBPS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 1, 1, 12),
    _HpnicfIfQoSCurQueueBPS_Type()
)
hpnicfIfQoSCurQueueBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSCurQueueBPS.setStatus("current")
_HpnicfIfQoSTailDropPkts_Type = Counter64
_HpnicfIfQoSTailDropPkts_Object = MibTableColumn
hpnicfIfQoSTailDropPkts = _HpnicfIfQoSTailDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 1, 1, 13),
    _HpnicfIfQoSTailDropPkts_Type()
)
hpnicfIfQoSTailDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSTailDropPkts.setStatus("current")
_HpnicfIfQoSTailDropBytes_Type = Counter64
_HpnicfIfQoSTailDropBytes_Object = MibTableColumn
hpnicfIfQoSTailDropBytes = _HpnicfIfQoSTailDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 1, 1, 14),
    _HpnicfIfQoSTailDropBytes_Type()
)
hpnicfIfQoSTailDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSTailDropBytes.setStatus("current")
_HpnicfIfQoSTailDropPPS_Type = Unsigned32
_HpnicfIfQoSTailDropPPS_Object = MibTableColumn
hpnicfIfQoSTailDropPPS = _HpnicfIfQoSTailDropPPS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 1, 1, 15),
    _HpnicfIfQoSTailDropPPS_Type()
)
hpnicfIfQoSTailDropPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSTailDropPPS.setStatus("current")
_HpnicfIfQoSTailDropBPS_Type = Unsigned32
_HpnicfIfQoSTailDropBPS_Object = MibTableColumn
hpnicfIfQoSTailDropBPS = _HpnicfIfQoSTailDropBPS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 1, 1, 16),
    _HpnicfIfQoSTailDropBPS_Type()
)
hpnicfIfQoSTailDropBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSTailDropBPS.setStatus("current")
_HpnicfIfQoSWredDropPkts_Type = Counter64
_HpnicfIfQoSWredDropPkts_Object = MibTableColumn
hpnicfIfQoSWredDropPkts = _HpnicfIfQoSWredDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 1, 1, 17),
    _HpnicfIfQoSWredDropPkts_Type()
)
hpnicfIfQoSWredDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredDropPkts.setStatus("current")
_HpnicfIfQoSWredDropBytes_Type = Counter64
_HpnicfIfQoSWredDropBytes_Object = MibTableColumn
hpnicfIfQoSWredDropBytes = _HpnicfIfQoSWredDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 1, 1, 18),
    _HpnicfIfQoSWredDropBytes_Type()
)
hpnicfIfQoSWredDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredDropBytes.setStatus("current")
_HpnicfIfQoSWredDropPPS_Type = Unsigned32
_HpnicfIfQoSWredDropPPS_Object = MibTableColumn
hpnicfIfQoSWredDropPPS = _HpnicfIfQoSWredDropPPS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 1, 1, 19),
    _HpnicfIfQoSWredDropPPS_Type()
)
hpnicfIfQoSWredDropPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredDropPPS.setStatus("current")
_HpnicfIfQoSWredDropBPS_Type = Unsigned32
_HpnicfIfQoSWredDropBPS_Object = MibTableColumn
hpnicfIfQoSWredDropBPS = _HpnicfIfQoSWredDropBPS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 1, 1, 20),
    _HpnicfIfQoSWredDropBPS_Type()
)
hpnicfIfQoSWredDropBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredDropBPS.setStatus("current")
_HpnicfIfQoSHQueueTcpRunInfoTable_Object = MibTable
hpnicfIfQoSHQueueTcpRunInfoTable = _HpnicfIfQoSHQueueTcpRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSHQueueTcpRunInfoTable.setStatus("current")
_HpnicfIfQoSHQueueTcpRunInfoEntry_Object = MibTableRow
hpnicfIfQoSHQueueTcpRunInfoEntry = _HpnicfIfQoSHQueueTcpRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 2, 1)
)
hpnicfIfQoSHQueueTcpRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSQueueID"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSHQueueTcpRunInfoEntry.setStatus("current")
_HpnicfIfQoSWredDropLPreNTcpPkts_Type = Counter64
_HpnicfIfQoSWredDropLPreNTcpPkts_Object = MibTableColumn
hpnicfIfQoSWredDropLPreNTcpPkts = _HpnicfIfQoSWredDropLPreNTcpPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 2, 1, 1),
    _HpnicfIfQoSWredDropLPreNTcpPkts_Type()
)
hpnicfIfQoSWredDropLPreNTcpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredDropLPreNTcpPkts.setStatus("current")
_HpnicfIfQoSWredDropLPreNTcpBytes_Type = Counter64
_HpnicfIfQoSWredDropLPreNTcpBytes_Object = MibTableColumn
hpnicfIfQoSWredDropLPreNTcpBytes = _HpnicfIfQoSWredDropLPreNTcpBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 2, 1, 2),
    _HpnicfIfQoSWredDropLPreNTcpBytes_Type()
)
hpnicfIfQoSWredDropLPreNTcpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredDropLPreNTcpBytes.setStatus("current")
_HpnicfIfQoSWredDropLPreNTcpPPS_Type = Unsigned32
_HpnicfIfQoSWredDropLPreNTcpPPS_Object = MibTableColumn
hpnicfIfQoSWredDropLPreNTcpPPS = _HpnicfIfQoSWredDropLPreNTcpPPS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 2, 1, 3),
    _HpnicfIfQoSWredDropLPreNTcpPPS_Type()
)
hpnicfIfQoSWredDropLPreNTcpPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredDropLPreNTcpPPS.setStatus("current")
_HpnicfIfQoSWredDropLPreNTcpBPS_Type = Unsigned32
_HpnicfIfQoSWredDropLPreNTcpBPS_Object = MibTableColumn
hpnicfIfQoSWredDropLPreNTcpBPS = _HpnicfIfQoSWredDropLPreNTcpBPS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 2, 1, 4),
    _HpnicfIfQoSWredDropLPreNTcpBPS_Type()
)
hpnicfIfQoSWredDropLPreNTcpBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredDropLPreNTcpBPS.setStatus("current")
_HpnicfIfQoSWredDropLPreTcpPkts_Type = Counter64
_HpnicfIfQoSWredDropLPreTcpPkts_Object = MibTableColumn
hpnicfIfQoSWredDropLPreTcpPkts = _HpnicfIfQoSWredDropLPreTcpPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 2, 1, 5),
    _HpnicfIfQoSWredDropLPreTcpPkts_Type()
)
hpnicfIfQoSWredDropLPreTcpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredDropLPreTcpPkts.setStatus("current")
_HpnicfIfQoSWredDropLPreTcpBytes_Type = Counter64
_HpnicfIfQoSWredDropLPreTcpBytes_Object = MibTableColumn
hpnicfIfQoSWredDropLPreTcpBytes = _HpnicfIfQoSWredDropLPreTcpBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 2, 1, 6),
    _HpnicfIfQoSWredDropLPreTcpBytes_Type()
)
hpnicfIfQoSWredDropLPreTcpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredDropLPreTcpBytes.setStatus("current")
_HpnicfIfQoSWredDropLPreTcpPPS_Type = Unsigned32
_HpnicfIfQoSWredDropLPreTcpPPS_Object = MibTableColumn
hpnicfIfQoSWredDropLPreTcpPPS = _HpnicfIfQoSWredDropLPreTcpPPS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 2, 1, 7),
    _HpnicfIfQoSWredDropLPreTcpPPS_Type()
)
hpnicfIfQoSWredDropLPreTcpPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredDropLPreTcpPPS.setStatus("current")
_HpnicfIfQoSWredDropLPreTcpBPS_Type = Unsigned32
_HpnicfIfQoSWredDropLPreTcpBPS_Object = MibTableColumn
hpnicfIfQoSWredDropLPreTcpBPS = _HpnicfIfQoSWredDropLPreTcpBPS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 2, 1, 8),
    _HpnicfIfQoSWredDropLPreTcpBPS_Type()
)
hpnicfIfQoSWredDropLPreTcpBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredDropLPreTcpBPS.setStatus("current")
_HpnicfIfQoSWredDropHPreNTcpPkts_Type = Counter64
_HpnicfIfQoSWredDropHPreNTcpPkts_Object = MibTableColumn
hpnicfIfQoSWredDropHPreNTcpPkts = _HpnicfIfQoSWredDropHPreNTcpPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 2, 1, 9),
    _HpnicfIfQoSWredDropHPreNTcpPkts_Type()
)
hpnicfIfQoSWredDropHPreNTcpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredDropHPreNTcpPkts.setStatus("current")
_HpnicfIfQoSWredDropHPreNTcpBytes_Type = Counter64
_HpnicfIfQoSWredDropHPreNTcpBytes_Object = MibTableColumn
hpnicfIfQoSWredDropHPreNTcpBytes = _HpnicfIfQoSWredDropHPreNTcpBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 2, 1, 10),
    _HpnicfIfQoSWredDropHPreNTcpBytes_Type()
)
hpnicfIfQoSWredDropHPreNTcpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredDropHPreNTcpBytes.setStatus("current")
_HpnicfIfQoSWredDropHPreNTcpPPS_Type = Unsigned32
_HpnicfIfQoSWredDropHPreNTcpPPS_Object = MibTableColumn
hpnicfIfQoSWredDropHPreNTcpPPS = _HpnicfIfQoSWredDropHPreNTcpPPS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 2, 1, 11),
    _HpnicfIfQoSWredDropHPreNTcpPPS_Type()
)
hpnicfIfQoSWredDropHPreNTcpPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredDropHPreNTcpPPS.setStatus("current")
_HpnicfIfQoSWredDropHPreNTcpBPS_Type = Unsigned32
_HpnicfIfQoSWredDropHPreNTcpBPS_Object = MibTableColumn
hpnicfIfQoSWredDropHPreNTcpBPS = _HpnicfIfQoSWredDropHPreNTcpBPS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 2, 1, 12),
    _HpnicfIfQoSWredDropHPreNTcpBPS_Type()
)
hpnicfIfQoSWredDropHPreNTcpBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredDropHPreNTcpBPS.setStatus("current")
_HpnicfIfQoSWredDropHPreTcpPkts_Type = Counter64
_HpnicfIfQoSWredDropHPreTcpPkts_Object = MibTableColumn
hpnicfIfQoSWredDropHPreTcpPkts = _HpnicfIfQoSWredDropHPreTcpPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 2, 1, 13),
    _HpnicfIfQoSWredDropHPreTcpPkts_Type()
)
hpnicfIfQoSWredDropHPreTcpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredDropHPreTcpPkts.setStatus("current")
_HpnicfIfQoSWredDropHPreTcpBytes_Type = Counter64
_HpnicfIfQoSWredDropHPreTcpBytes_Object = MibTableColumn
hpnicfIfQoSWredDropHPreTcpBytes = _HpnicfIfQoSWredDropHPreTcpBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 2, 1, 14),
    _HpnicfIfQoSWredDropHPreTcpBytes_Type()
)
hpnicfIfQoSWredDropHPreTcpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredDropHPreTcpBytes.setStatus("current")
_HpnicfIfQoSWredDropHPreTcpPPS_Type = Unsigned32
_HpnicfIfQoSWredDropHPreTcpPPS_Object = MibTableColumn
hpnicfIfQoSWredDropHPreTcpPPS = _HpnicfIfQoSWredDropHPreTcpPPS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 2, 1, 15),
    _HpnicfIfQoSWredDropHPreTcpPPS_Type()
)
hpnicfIfQoSWredDropHPreTcpPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredDropHPreTcpPPS.setStatus("current")
_HpnicfIfQoSWredDropHPreTcpBPS_Type = Unsigned32
_HpnicfIfQoSWredDropHPreTcpBPS_Object = MibTableColumn
hpnicfIfQoSWredDropHPreTcpBPS = _HpnicfIfQoSWredDropHPreTcpBPS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 1, 2, 2, 1, 16),
    _HpnicfIfQoSWredDropHPreTcpBPS_Type()
)
hpnicfIfQoSWredDropHPreTcpBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredDropHPreTcpBPS.setStatus("current")
_HpnicfIfQoSSoftwareQueueObjects_ObjectIdentity = ObjectIdentity
hpnicfIfQoSSoftwareQueueObjects = _HpnicfIfQoSSoftwareQueueObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2)
)
_HpnicfIfQoSFIFOObject_ObjectIdentity = ObjectIdentity
hpnicfIfQoSFIFOObject = _HpnicfIfQoSFIFOObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 1)
)
_HpnicfIfQoSFIFOConfigTable_Object = MibTable
hpnicfIfQoSFIFOConfigTable = _HpnicfIfQoSFIFOConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSFIFOConfigTable.setStatus("current")
_HpnicfIfQoSFIFOConfigEntry_Object = MibTableRow
hpnicfIfQoSFIFOConfigEntry = _HpnicfIfQoSFIFOConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 1, 1, 1)
)
hpnicfIfQoSFIFOConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSFIFOConfigEntry.setStatus("current")
_HpnicfIfQoSFIFOMaxQueueLen_Type = Integer32
_HpnicfIfQoSFIFOMaxQueueLen_Object = MibTableColumn
hpnicfIfQoSFIFOMaxQueueLen = _HpnicfIfQoSFIFOMaxQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 1, 1, 1, 1),
    _HpnicfIfQoSFIFOMaxQueueLen_Type()
)
hpnicfIfQoSFIFOMaxQueueLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIfQoSFIFOMaxQueueLen.setStatus("current")
_HpnicfIfQoSFIFORunInfoTable_Object = MibTable
hpnicfIfQoSFIFORunInfoTable = _HpnicfIfQoSFIFORunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSFIFORunInfoTable.setStatus("current")
_HpnicfIfQoSFIFORunInfoEntry_Object = MibTableRow
hpnicfIfQoSFIFORunInfoEntry = _HpnicfIfQoSFIFORunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 1, 2, 1)
)
hpnicfIfQoSFIFORunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSFIFORunInfoEntry.setStatus("current")
_HpnicfIfQoSFIFOSize_Type = Integer32
_HpnicfIfQoSFIFOSize_Object = MibTableColumn
hpnicfIfQoSFIFOSize = _HpnicfIfQoSFIFOSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 1, 2, 1, 1),
    _HpnicfIfQoSFIFOSize_Type()
)
hpnicfIfQoSFIFOSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSFIFOSize.setStatus("current")
_HpnicfIfQoSFIFODiscardPackets_Type = Counter64
_HpnicfIfQoSFIFODiscardPackets_Object = MibTableColumn
hpnicfIfQoSFIFODiscardPackets = _HpnicfIfQoSFIFODiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 1, 2, 1, 2),
    _HpnicfIfQoSFIFODiscardPackets_Type()
)
hpnicfIfQoSFIFODiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSFIFODiscardPackets.setStatus("current")
_HpnicfIfQoSPQObject_ObjectIdentity = ObjectIdentity
hpnicfIfQoSPQObject = _HpnicfIfQoSPQObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 2)
)
_HpnicfIfQoSPQConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfIfQoSPQConfigGroup = _HpnicfIfQoSPQConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 2, 1)
)
_HpnicfIfQoSPQDefaultTable_Object = MibTable
hpnicfIfQoSPQDefaultTable = _HpnicfIfQoSPQDefaultTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSPQDefaultTable.setStatus("current")
_HpnicfIfQoSPQDefaultEntry_Object = MibTableRow
hpnicfIfQoSPQDefaultEntry = _HpnicfIfQoSPQDefaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 2, 1, 1, 1)
)
hpnicfIfQoSPQDefaultEntry.setIndexNames(
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSPQListNumber"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSPQDefaultEntry.setStatus("current")


class _HpnicfIfQoSPQListNumber_Type(Integer32):
    """Custom type hpnicfIfQoSPQListNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpnicfIfQoSPQListNumber_Type.__name__ = "Integer32"
_HpnicfIfQoSPQListNumber_Object = MibTableColumn
hpnicfIfQoSPQListNumber = _HpnicfIfQoSPQListNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 2, 1, 1, 1, 1),
    _HpnicfIfQoSPQListNumber_Type()
)
hpnicfIfQoSPQListNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSPQListNumber.setStatus("current")
_HpnicfIfQoSPQDefaultQueueType_Type = PriorityQueue
_HpnicfIfQoSPQDefaultQueueType_Object = MibTableColumn
hpnicfIfQoSPQDefaultQueueType = _HpnicfIfQoSPQDefaultQueueType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 2, 1, 1, 1, 2),
    _HpnicfIfQoSPQDefaultQueueType_Type()
)
hpnicfIfQoSPQDefaultQueueType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIfQoSPQDefaultQueueType.setStatus("current")
_HpnicfIfQoSPQQueueLengthTable_Object = MibTable
hpnicfIfQoSPQQueueLengthTable = _HpnicfIfQoSPQQueueLengthTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSPQQueueLengthTable.setStatus("current")
_HpnicfIfQoSPQQueueLengthEntry_Object = MibTableRow
hpnicfIfQoSPQQueueLengthEntry = _HpnicfIfQoSPQQueueLengthEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 2, 1, 2, 1)
)
hpnicfIfQoSPQQueueLengthEntry.setIndexNames(
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSPQListNumber"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSPQQueueLengthType"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSPQQueueLengthEntry.setStatus("current")
_HpnicfIfQoSPQQueueLengthType_Type = PriorityQueue
_HpnicfIfQoSPQQueueLengthType_Object = MibTableColumn
hpnicfIfQoSPQQueueLengthType = _HpnicfIfQoSPQQueueLengthType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 2, 1, 2, 1, 1),
    _HpnicfIfQoSPQQueueLengthType_Type()
)
hpnicfIfQoSPQQueueLengthType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSPQQueueLengthType.setStatus("current")


class _HpnicfIfQoSPQQueueLengthValue_Type(Integer32):
    """Custom type hpnicfIfQoSPQQueueLengthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HpnicfIfQoSPQQueueLengthValue_Type.__name__ = "Integer32"
_HpnicfIfQoSPQQueueLengthValue_Object = MibTableColumn
hpnicfIfQoSPQQueueLengthValue = _HpnicfIfQoSPQQueueLengthValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 2, 1, 2, 1, 2),
    _HpnicfIfQoSPQQueueLengthValue_Type()
)
hpnicfIfQoSPQQueueLengthValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIfQoSPQQueueLengthValue.setStatus("current")
_HpnicfIfQoSPQClassRuleTable_Object = MibTable
hpnicfIfQoSPQClassRuleTable = _HpnicfIfQoSPQClassRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSPQClassRuleTable.setStatus("current")
_HpnicfIfQoSPQClassRuleEntry_Object = MibTableRow
hpnicfIfQoSPQClassRuleEntry = _HpnicfIfQoSPQClassRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 2, 1, 3, 1)
)
hpnicfIfQoSPQClassRuleEntry.setIndexNames(
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSPQListNumber"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSPQClassRuleType"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSPQClassRuleValue"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSPQClassRuleEntry.setStatus("current")


class _HpnicfIfQoSPQClassRuleType_Type(Integer32):
    """Custom type hpnicfIfQoSPQClassRuleType based on Integer32"""
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


_HpnicfIfQoSPQClassRuleType_Type.__name__ = "Integer32"
_HpnicfIfQoSPQClassRuleType_Object = MibTableColumn
hpnicfIfQoSPQClassRuleType = _HpnicfIfQoSPQClassRuleType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 2, 1, 3, 1, 1),
    _HpnicfIfQoSPQClassRuleType_Type()
)
hpnicfIfQoSPQClassRuleType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSPQClassRuleType.setStatus("current")
_HpnicfIfQoSPQClassRuleValue_Type = Integer32
_HpnicfIfQoSPQClassRuleValue_Object = MibTableColumn
hpnicfIfQoSPQClassRuleValue = _HpnicfIfQoSPQClassRuleValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 2, 1, 3, 1, 2),
    _HpnicfIfQoSPQClassRuleValue_Type()
)
hpnicfIfQoSPQClassRuleValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSPQClassRuleValue.setStatus("current")
_HpnicfIfQoSPQClassRuleQueueType_Type = PriorityQueue
_HpnicfIfQoSPQClassRuleQueueType_Object = MibTableColumn
hpnicfIfQoSPQClassRuleQueueType = _HpnicfIfQoSPQClassRuleQueueType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 2, 1, 3, 1, 3),
    _HpnicfIfQoSPQClassRuleQueueType_Type()
)
hpnicfIfQoSPQClassRuleQueueType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSPQClassRuleQueueType.setStatus("current")
_HpnicfIfQoSPQClassRowStatus_Type = RowStatus
_HpnicfIfQoSPQClassRowStatus_Object = MibTableColumn
hpnicfIfQoSPQClassRowStatus = _HpnicfIfQoSPQClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 2, 1, 3, 1, 4),
    _HpnicfIfQoSPQClassRowStatus_Type()
)
hpnicfIfQoSPQClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSPQClassRowStatus.setStatus("current")
_HpnicfIfQoSPQApplyTable_Object = MibTable
hpnicfIfQoSPQApplyTable = _HpnicfIfQoSPQApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSPQApplyTable.setStatus("current")
_HpnicfIfQoSPQApplyEntry_Object = MibTableRow
hpnicfIfQoSPQApplyEntry = _HpnicfIfQoSPQApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 2, 1, 4, 1)
)
hpnicfIfQoSPQApplyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSPQApplyEntry.setStatus("current")


class _HpnicfIfQoSPQApplyListNumber_Type(Integer32):
    """Custom type hpnicfIfQoSPQApplyListNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpnicfIfQoSPQApplyListNumber_Type.__name__ = "Integer32"
_HpnicfIfQoSPQApplyListNumber_Object = MibTableColumn
hpnicfIfQoSPQApplyListNumber = _HpnicfIfQoSPQApplyListNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 2, 1, 4, 1, 1),
    _HpnicfIfQoSPQApplyListNumber_Type()
)
hpnicfIfQoSPQApplyListNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSPQApplyListNumber.setStatus("current")
_HpnicfIfQoSPQApplyRowStatus_Type = RowStatus
_HpnicfIfQoSPQApplyRowStatus_Object = MibTableColumn
hpnicfIfQoSPQApplyRowStatus = _HpnicfIfQoSPQApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 2, 1, 4, 1, 2),
    _HpnicfIfQoSPQApplyRowStatus_Type()
)
hpnicfIfQoSPQApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSPQApplyRowStatus.setStatus("current")
_HpnicfIfQoSPQRunInfoGroup_ObjectIdentity = ObjectIdentity
hpnicfIfQoSPQRunInfoGroup = _HpnicfIfQoSPQRunInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 2, 2)
)
_HpnicfIfQoSPQRunInfoTable_Object = MibTable
hpnicfIfQoSPQRunInfoTable = _HpnicfIfQoSPQRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSPQRunInfoTable.setStatus("current")
_HpnicfIfQoSPQRunInfoEntry_Object = MibTableRow
hpnicfIfQoSPQRunInfoEntry = _HpnicfIfQoSPQRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 2, 2, 1, 1)
)
hpnicfIfQoSPQRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSPQType"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSPQRunInfoEntry.setStatus("current")
_HpnicfIfQoSPQType_Type = PriorityQueue
_HpnicfIfQoSPQType_Object = MibTableColumn
hpnicfIfQoSPQType = _HpnicfIfQoSPQType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 2, 2, 1, 1, 1),
    _HpnicfIfQoSPQType_Type()
)
hpnicfIfQoSPQType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSPQType.setStatus("current")
_HpnicfIfQoSPQSize_Type = Integer32
_HpnicfIfQoSPQSize_Object = MibTableColumn
hpnicfIfQoSPQSize = _HpnicfIfQoSPQSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 2, 2, 1, 1, 2),
    _HpnicfIfQoSPQSize_Type()
)
hpnicfIfQoSPQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSPQSize.setStatus("current")
_HpnicfIfQoSPQLength_Type = Integer32
_HpnicfIfQoSPQLength_Object = MibTableColumn
hpnicfIfQoSPQLength = _HpnicfIfQoSPQLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 2, 2, 1, 1, 3),
    _HpnicfIfQoSPQLength_Type()
)
hpnicfIfQoSPQLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSPQLength.setStatus("current")
_HpnicfIfQoSPQDiscardPackets_Type = Counter64
_HpnicfIfQoSPQDiscardPackets_Object = MibTableColumn
hpnicfIfQoSPQDiscardPackets = _HpnicfIfQoSPQDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 2, 2, 1, 1, 4),
    _HpnicfIfQoSPQDiscardPackets_Type()
)
hpnicfIfQoSPQDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSPQDiscardPackets.setStatus("current")
_HpnicfIfQoSCQObject_ObjectIdentity = ObjectIdentity
hpnicfIfQoSCQObject = _HpnicfIfQoSCQObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 3)
)
_HpnicfIfQoSCQConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfIfQoSCQConfigGroup = _HpnicfIfQoSCQConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 3, 1)
)
_HpnicfIfQoSCQDefaultTable_Object = MibTable
hpnicfIfQoSCQDefaultTable = _HpnicfIfQoSCQDefaultTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSCQDefaultTable.setStatus("current")
_HpnicfIfQoSCQDefaultEntry_Object = MibTableRow
hpnicfIfQoSCQDefaultEntry = _HpnicfIfQoSCQDefaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 3, 1, 1, 1)
)
hpnicfIfQoSCQDefaultEntry.setIndexNames(
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSCQListNumber"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSCQDefaultEntry.setStatus("current")


class _HpnicfIfQoSCQListNumber_Type(Integer32):
    """Custom type hpnicfIfQoSCQListNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpnicfIfQoSCQListNumber_Type.__name__ = "Integer32"
_HpnicfIfQoSCQListNumber_Object = MibTableColumn
hpnicfIfQoSCQListNumber = _HpnicfIfQoSCQListNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 3, 1, 1, 1, 1),
    _HpnicfIfQoSCQListNumber_Type()
)
hpnicfIfQoSCQListNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSCQListNumber.setStatus("current")


class _HpnicfIfQoSCQDefaultQueueID_Type(Integer32):
    """Custom type hpnicfIfQoSCQDefaultQueueID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_HpnicfIfQoSCQDefaultQueueID_Type.__name__ = "Integer32"
_HpnicfIfQoSCQDefaultQueueID_Object = MibTableColumn
hpnicfIfQoSCQDefaultQueueID = _HpnicfIfQoSCQDefaultQueueID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 3, 1, 1, 1, 2),
    _HpnicfIfQoSCQDefaultQueueID_Type()
)
hpnicfIfQoSCQDefaultQueueID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIfQoSCQDefaultQueueID.setStatus("current")
_HpnicfIfQoSCQQueueLengthTable_Object = MibTable
hpnicfIfQoSCQQueueLengthTable = _HpnicfIfQoSCQQueueLengthTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSCQQueueLengthTable.setStatus("current")
_HpnicfIfQoSCQQueueLengthEntry_Object = MibTableRow
hpnicfIfQoSCQQueueLengthEntry = _HpnicfIfQoSCQQueueLengthEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 3, 1, 2, 1)
)
hpnicfIfQoSCQQueueLengthEntry.setIndexNames(
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSCQListNumber"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSCQQueueID"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSCQQueueLengthEntry.setStatus("current")


class _HpnicfIfQoSCQQueueID_Type(Integer32):
    """Custom type hpnicfIfQoSCQQueueID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpnicfIfQoSCQQueueID_Type.__name__ = "Integer32"
_HpnicfIfQoSCQQueueID_Object = MibTableColumn
hpnicfIfQoSCQQueueID = _HpnicfIfQoSCQQueueID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 3, 1, 2, 1, 1),
    _HpnicfIfQoSCQQueueID_Type()
)
hpnicfIfQoSCQQueueID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSCQQueueID.setStatus("current")


class _HpnicfIfQoSCQQueueLength_Type(Integer32):
    """Custom type hpnicfIfQoSCQQueueLength based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HpnicfIfQoSCQQueueLength_Type.__name__ = "Integer32"
_HpnicfIfQoSCQQueueLength_Object = MibTableColumn
hpnicfIfQoSCQQueueLength = _HpnicfIfQoSCQQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 3, 1, 2, 1, 2),
    _HpnicfIfQoSCQQueueLength_Type()
)
hpnicfIfQoSCQQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIfQoSCQQueueLength.setStatus("current")


class _HpnicfIfQoSCQQueueServing_Type(Integer32):
    """Custom type hpnicfIfQoSCQQueueServing based on Integer32"""
    defaultValue = 1500


_HpnicfIfQoSCQQueueServing_Object = MibTableColumn
hpnicfIfQoSCQQueueServing = _HpnicfIfQoSCQQueueServing_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 3, 1, 2, 1, 3),
    _HpnicfIfQoSCQQueueServing_Type()
)
hpnicfIfQoSCQQueueServing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIfQoSCQQueueServing.setStatus("current")
_HpnicfIfQoSCQClassRuleTable_Object = MibTable
hpnicfIfQoSCQClassRuleTable = _HpnicfIfQoSCQClassRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 3, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSCQClassRuleTable.setStatus("current")
_HpnicfIfQoSCQClassRuleEntry_Object = MibTableRow
hpnicfIfQoSCQClassRuleEntry = _HpnicfIfQoSCQClassRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 3, 1, 3, 1)
)
hpnicfIfQoSCQClassRuleEntry.setIndexNames(
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSCQListNumber"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSCQClassRuleType"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSCQClassRuleValue"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSCQClassRuleEntry.setStatus("current")


class _HpnicfIfQoSCQClassRuleType_Type(Integer32):
    """Custom type hpnicfIfQoSCQClassRuleType based on Integer32"""
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


_HpnicfIfQoSCQClassRuleType_Type.__name__ = "Integer32"
_HpnicfIfQoSCQClassRuleType_Object = MibTableColumn
hpnicfIfQoSCQClassRuleType = _HpnicfIfQoSCQClassRuleType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 3, 1, 3, 1, 1),
    _HpnicfIfQoSCQClassRuleType_Type()
)
hpnicfIfQoSCQClassRuleType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSCQClassRuleType.setStatus("current")
_HpnicfIfQoSCQClassRuleValue_Type = Integer32
_HpnicfIfQoSCQClassRuleValue_Object = MibTableColumn
hpnicfIfQoSCQClassRuleValue = _HpnicfIfQoSCQClassRuleValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 3, 1, 3, 1, 2),
    _HpnicfIfQoSCQClassRuleValue_Type()
)
hpnicfIfQoSCQClassRuleValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSCQClassRuleValue.setStatus("current")


class _HpnicfIfQoSCQClassRuleQueueID_Type(Integer32):
    """Custom type hpnicfIfQoSCQClassRuleQueueID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpnicfIfQoSCQClassRuleQueueID_Type.__name__ = "Integer32"
_HpnicfIfQoSCQClassRuleQueueID_Object = MibTableColumn
hpnicfIfQoSCQClassRuleQueueID = _HpnicfIfQoSCQClassRuleQueueID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 3, 1, 3, 1, 3),
    _HpnicfIfQoSCQClassRuleQueueID_Type()
)
hpnicfIfQoSCQClassRuleQueueID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSCQClassRuleQueueID.setStatus("current")
_HpnicfIfQoSCQClassRowStatus_Type = RowStatus
_HpnicfIfQoSCQClassRowStatus_Object = MibTableColumn
hpnicfIfQoSCQClassRowStatus = _HpnicfIfQoSCQClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 3, 1, 3, 1, 4),
    _HpnicfIfQoSCQClassRowStatus_Type()
)
hpnicfIfQoSCQClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSCQClassRowStatus.setStatus("current")
_HpnicfIfQoSCQApplyTable_Object = MibTable
hpnicfIfQoSCQApplyTable = _HpnicfIfQoSCQApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 3, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSCQApplyTable.setStatus("current")
_HpnicfIfQoSCQApplyEntry_Object = MibTableRow
hpnicfIfQoSCQApplyEntry = _HpnicfIfQoSCQApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 3, 1, 4, 1)
)
hpnicfIfQoSCQApplyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSCQApplyEntry.setStatus("current")


class _HpnicfIfQoSCQApplyListNumber_Type(Integer32):
    """Custom type hpnicfIfQoSCQApplyListNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpnicfIfQoSCQApplyListNumber_Type.__name__ = "Integer32"
_HpnicfIfQoSCQApplyListNumber_Object = MibTableColumn
hpnicfIfQoSCQApplyListNumber = _HpnicfIfQoSCQApplyListNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 3, 1, 4, 1, 1),
    _HpnicfIfQoSCQApplyListNumber_Type()
)
hpnicfIfQoSCQApplyListNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSCQApplyListNumber.setStatus("current")
_HpnicfIfQoSCQApplyRowStatus_Type = RowStatus
_HpnicfIfQoSCQApplyRowStatus_Object = MibTableColumn
hpnicfIfQoSCQApplyRowStatus = _HpnicfIfQoSCQApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 3, 1, 4, 1, 2),
    _HpnicfIfQoSCQApplyRowStatus_Type()
)
hpnicfIfQoSCQApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSCQApplyRowStatus.setStatus("current")
_HpnicfIfQoSCQRunInfoGroup_ObjectIdentity = ObjectIdentity
hpnicfIfQoSCQRunInfoGroup = _HpnicfIfQoSCQRunInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 3, 2)
)
_HpnicfIfQoSCQRunInfoTable_Object = MibTable
hpnicfIfQoSCQRunInfoTable = _HpnicfIfQoSCQRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSCQRunInfoTable.setStatus("current")
_HpnicfIfQoSCQRunInfoEntry_Object = MibTableRow
hpnicfIfQoSCQRunInfoEntry = _HpnicfIfQoSCQRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 3, 2, 1, 1)
)
hpnicfIfQoSCQRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSCQQueueID"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSCQRunInfoEntry.setStatus("current")
_HpnicfIfQoSCQRunInfoSize_Type = Integer32
_HpnicfIfQoSCQRunInfoSize_Object = MibTableColumn
hpnicfIfQoSCQRunInfoSize = _HpnicfIfQoSCQRunInfoSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 3, 2, 1, 1, 1),
    _HpnicfIfQoSCQRunInfoSize_Type()
)
hpnicfIfQoSCQRunInfoSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSCQRunInfoSize.setStatus("current")
_HpnicfIfQoSCQRunInfoLength_Type = Integer32
_HpnicfIfQoSCQRunInfoLength_Object = MibTableColumn
hpnicfIfQoSCQRunInfoLength = _HpnicfIfQoSCQRunInfoLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 3, 2, 1, 1, 2),
    _HpnicfIfQoSCQRunInfoLength_Type()
)
hpnicfIfQoSCQRunInfoLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSCQRunInfoLength.setStatus("current")
_HpnicfIfQoSCQRunInfoDiscardPackets_Type = Counter64
_HpnicfIfQoSCQRunInfoDiscardPackets_Object = MibTableColumn
hpnicfIfQoSCQRunInfoDiscardPackets = _HpnicfIfQoSCQRunInfoDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 3, 2, 1, 1, 3),
    _HpnicfIfQoSCQRunInfoDiscardPackets_Type()
)
hpnicfIfQoSCQRunInfoDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSCQRunInfoDiscardPackets.setStatus("current")
_HpnicfIfQoSWFQObject_ObjectIdentity = ObjectIdentity
hpnicfIfQoSWFQObject = _HpnicfIfQoSWFQObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 4)
)
_HpnicfIfQoSWFQConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfIfQoSWFQConfigGroup = _HpnicfIfQoSWFQConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 4, 1)
)
_HpnicfIfQoSWFQTable_Object = MibTable
hpnicfIfQoSWFQTable = _HpnicfIfQoSWFQTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSWFQTable.setStatus("current")
_HpnicfIfQoSWFQEntry_Object = MibTableRow
hpnicfIfQoSWFQEntry = _HpnicfIfQoSWFQEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 4, 1, 1, 1)
)
hpnicfIfQoSWFQEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSWFQEntry.setStatus("current")


class _HpnicfIfQoSWFQQueueLength_Type(Integer32):
    """Custom type hpnicfIfQoSWFQQueueLength based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HpnicfIfQoSWFQQueueLength_Type.__name__ = "Integer32"
_HpnicfIfQoSWFQQueueLength_Object = MibTableColumn
hpnicfIfQoSWFQQueueLength = _HpnicfIfQoSWFQQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 4, 1, 1, 1, 1),
    _HpnicfIfQoSWFQQueueLength_Type()
)
hpnicfIfQoSWFQQueueLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSWFQQueueLength.setStatus("current")


class _HpnicfIfQoSWFQQueueNumber_Type(Integer32):
    """Custom type hpnicfIfQoSWFQQueueNumber based on Integer32"""
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


_HpnicfIfQoSWFQQueueNumber_Type.__name__ = "Integer32"
_HpnicfIfQoSWFQQueueNumber_Object = MibTableColumn
hpnicfIfQoSWFQQueueNumber = _HpnicfIfQoSWFQQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 4, 1, 1, 1, 2),
    _HpnicfIfQoSWFQQueueNumber_Type()
)
hpnicfIfQoSWFQQueueNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSWFQQueueNumber.setStatus("current")
_HpnicfIfQoSWFQRowStatus_Type = RowStatus
_HpnicfIfQoSWFQRowStatus_Object = MibTableColumn
hpnicfIfQoSWFQRowStatus = _HpnicfIfQoSWFQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 4, 1, 1, 1, 3),
    _HpnicfIfQoSWFQRowStatus_Type()
)
hpnicfIfQoSWFQRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSWFQRowStatus.setStatus("current")


class _HpnicfIfQoSWFQType_Type(Integer32):
    """Custom type hpnicfIfQoSWFQType based on Integer32"""
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


_HpnicfIfQoSWFQType_Type.__name__ = "Integer32"
_HpnicfIfQoSWFQType_Object = MibTableColumn
hpnicfIfQoSWFQType = _HpnicfIfQoSWFQType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 4, 1, 1, 1, 4),
    _HpnicfIfQoSWFQType_Type()
)
hpnicfIfQoSWFQType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSWFQType.setStatus("current")
_HpnicfIfQoSWFQRunInfoGroup_ObjectIdentity = ObjectIdentity
hpnicfIfQoSWFQRunInfoGroup = _HpnicfIfQoSWFQRunInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 4, 2)
)
_HpnicfIfQoSWFQRunInfoTable_Object = MibTable
hpnicfIfQoSWFQRunInfoTable = _HpnicfIfQoSWFQRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSWFQRunInfoTable.setStatus("current")
_HpnicfIfQoSWFQRunInfoEntry_Object = MibTableRow
hpnicfIfQoSWFQRunInfoEntry = _HpnicfIfQoSWFQRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 4, 2, 1, 1)
)
hpnicfIfQoSWFQRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSWFQRunInfoEntry.setStatus("current")
_HpnicfIfQoSWFQSize_Type = Integer32
_HpnicfIfQoSWFQSize_Object = MibTableColumn
hpnicfIfQoSWFQSize = _HpnicfIfQoSWFQSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 4, 2, 1, 1, 1),
    _HpnicfIfQoSWFQSize_Type()
)
hpnicfIfQoSWFQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWFQSize.setStatus("current")
_HpnicfIfQoSWFQLength_Type = Integer32
_HpnicfIfQoSWFQLength_Object = MibTableColumn
hpnicfIfQoSWFQLength = _HpnicfIfQoSWFQLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 4, 2, 1, 1, 2),
    _HpnicfIfQoSWFQLength_Type()
)
hpnicfIfQoSWFQLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWFQLength.setStatus("current")
_HpnicfIfQoSWFQDiscardPackets_Type = Counter64
_HpnicfIfQoSWFQDiscardPackets_Object = MibTableColumn
hpnicfIfQoSWFQDiscardPackets = _HpnicfIfQoSWFQDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 4, 2, 1, 1, 3),
    _HpnicfIfQoSWFQDiscardPackets_Type()
)
hpnicfIfQoSWFQDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWFQDiscardPackets.setStatus("current")
_HpnicfIfQoSWFQHashedActiveQueues_Type = Integer32
_HpnicfIfQoSWFQHashedActiveQueues_Object = MibTableColumn
hpnicfIfQoSWFQHashedActiveQueues = _HpnicfIfQoSWFQHashedActiveQueues_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 4, 2, 1, 1, 4),
    _HpnicfIfQoSWFQHashedActiveQueues_Type()
)
hpnicfIfQoSWFQHashedActiveQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWFQHashedActiveQueues.setStatus("current")
_HpnicfIfQoSWFQHashedMaxActiveQueues_Type = Integer32
_HpnicfIfQoSWFQHashedMaxActiveQueues_Object = MibTableColumn
hpnicfIfQoSWFQHashedMaxActiveQueues = _HpnicfIfQoSWFQHashedMaxActiveQueues_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 4, 2, 1, 1, 5),
    _HpnicfIfQoSWFQHashedMaxActiveQueues_Type()
)
hpnicfIfQoSWFQHashedMaxActiveQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWFQHashedMaxActiveQueues.setStatus("current")
_HpnicfIfQosWFQhashedTotalQueues_Type = Integer32
_HpnicfIfQosWFQhashedTotalQueues_Object = MibTableColumn
hpnicfIfQosWFQhashedTotalQueues = _HpnicfIfQosWFQhashedTotalQueues_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 4, 2, 1, 1, 6),
    _HpnicfIfQosWFQhashedTotalQueues_Type()
)
hpnicfIfQosWFQhashedTotalQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQosWFQhashedTotalQueues.setStatus("current")
_HpnicfIfQoSBandwidthGroup_ObjectIdentity = ObjectIdentity
hpnicfIfQoSBandwidthGroup = _HpnicfIfQoSBandwidthGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 5)
)
_HpnicfIfQoSBandwidthTable_Object = MibTable
hpnicfIfQoSBandwidthTable = _HpnicfIfQoSBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSBandwidthTable.setStatus("current")
_HpnicfIfQoSBandwidthEntry_Object = MibTableRow
hpnicfIfQoSBandwidthEntry = _HpnicfIfQoSBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 5, 1, 1)
)
hpnicfIfQoSBandwidthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSBandwidthEntry.setStatus("current")
_HpnicfIfQoSMaxBandwidth_Type = Integer32
_HpnicfIfQoSMaxBandwidth_Object = MibTableColumn
hpnicfIfQoSMaxBandwidth = _HpnicfIfQoSMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 5, 1, 1, 1),
    _HpnicfIfQoSMaxBandwidth_Type()
)
hpnicfIfQoSMaxBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSMaxBandwidth.setStatus("current")


class _HpnicfIfQoSReservedBandwidthPct_Type(Integer32):
    """Custom type hpnicfIfQoSReservedBandwidthPct based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HpnicfIfQoSReservedBandwidthPct_Type.__name__ = "Integer32"
_HpnicfIfQoSReservedBandwidthPct_Object = MibTableColumn
hpnicfIfQoSReservedBandwidthPct = _HpnicfIfQoSReservedBandwidthPct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 5, 1, 1, 2),
    _HpnicfIfQoSReservedBandwidthPct_Type()
)
hpnicfIfQoSReservedBandwidthPct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSReservedBandwidthPct.setStatus("current")
_HpnicfIfQoSBandwidthRowStatus_Type = RowStatus
_HpnicfIfQoSBandwidthRowStatus_Object = MibTableColumn
hpnicfIfQoSBandwidthRowStatus = _HpnicfIfQoSBandwidthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 5, 1, 1, 3),
    _HpnicfIfQoSBandwidthRowStatus_Type()
)
hpnicfIfQoSBandwidthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSBandwidthRowStatus.setStatus("current")
_HpnicfIfQoSQmtokenGroup_ObjectIdentity = ObjectIdentity
hpnicfIfQoSQmtokenGroup = _HpnicfIfQoSQmtokenGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 6)
)
_HpnicfIfQoSQmtokenTable_Object = MibTable
hpnicfIfQoSQmtokenTable = _HpnicfIfQoSQmtokenTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSQmtokenTable.setStatus("current")
_HpnicfIfQoSQmtokenEntry_Object = MibTableRow
hpnicfIfQoSQmtokenEntry = _HpnicfIfQoSQmtokenEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 6, 1, 1)
)
hpnicfIfQoSQmtokenEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSQmtokenEntry.setStatus("current")


class _HpnicfIfQoSQmtokenNumber_Type(Integer32):
    """Custom type hpnicfIfQoSQmtokenNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_HpnicfIfQoSQmtokenNumber_Type.__name__ = "Integer32"
_HpnicfIfQoSQmtokenNumber_Object = MibTableColumn
hpnicfIfQoSQmtokenNumber = _HpnicfIfQoSQmtokenNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 6, 1, 1, 1),
    _HpnicfIfQoSQmtokenNumber_Type()
)
hpnicfIfQoSQmtokenNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSQmtokenNumber.setStatus("current")
_HpnicfIfQoSQmtokenRosStatus_Type = RowStatus
_HpnicfIfQoSQmtokenRosStatus_Object = MibTableColumn
hpnicfIfQoSQmtokenRosStatus = _HpnicfIfQoSQmtokenRosStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 6, 1, 1, 2),
    _HpnicfIfQoSQmtokenRosStatus_Type()
)
hpnicfIfQoSQmtokenRosStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSQmtokenRosStatus.setStatus("current")
_HpnicfIfQoSRTPQObject_ObjectIdentity = ObjectIdentity
hpnicfIfQoSRTPQObject = _HpnicfIfQoSRTPQObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 7)
)
_HpnicfIfQoSRTPQConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfIfQoSRTPQConfigGroup = _HpnicfIfQoSRTPQConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 7, 1)
)
_HpnicfIfQoSRTPQConfigTable_Object = MibTable
hpnicfIfQoSRTPQConfigTable = _HpnicfIfQoSRTPQConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSRTPQConfigTable.setStatus("current")
_HpnicfIfQoSRTPQConfigEntry_Object = MibTableRow
hpnicfIfQoSRTPQConfigEntry = _HpnicfIfQoSRTPQConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 7, 1, 1, 1)
)
hpnicfIfQoSRTPQConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSRTPQConfigEntry.setStatus("current")


class _HpnicfIfQoSRTPQStartPort_Type(Integer32):
    """Custom type hpnicfIfQoSRTPQStartPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 65535),
    )


_HpnicfIfQoSRTPQStartPort_Type.__name__ = "Integer32"
_HpnicfIfQoSRTPQStartPort_Object = MibTableColumn
hpnicfIfQoSRTPQStartPort = _HpnicfIfQoSRTPQStartPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 7, 1, 1, 1, 1),
    _HpnicfIfQoSRTPQStartPort_Type()
)
hpnicfIfQoSRTPQStartPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSRTPQStartPort.setStatus("current")


class _HpnicfIfQoSRTPQEndPort_Type(Integer32):
    """Custom type hpnicfIfQoSRTPQEndPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 65535),
    )


_HpnicfIfQoSRTPQEndPort_Type.__name__ = "Integer32"
_HpnicfIfQoSRTPQEndPort_Object = MibTableColumn
hpnicfIfQoSRTPQEndPort = _HpnicfIfQoSRTPQEndPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 7, 1, 1, 1, 2),
    _HpnicfIfQoSRTPQEndPort_Type()
)
hpnicfIfQoSRTPQEndPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSRTPQEndPort.setStatus("current")
_HpnicfIfQoSRTPQReservedBandwidth_Type = Integer32
_HpnicfIfQoSRTPQReservedBandwidth_Object = MibTableColumn
hpnicfIfQoSRTPQReservedBandwidth = _HpnicfIfQoSRTPQReservedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 7, 1, 1, 1, 3),
    _HpnicfIfQoSRTPQReservedBandwidth_Type()
)
hpnicfIfQoSRTPQReservedBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSRTPQReservedBandwidth.setStatus("current")
_HpnicfIfQoSRTPQCbs_Type = Unsigned32
_HpnicfIfQoSRTPQCbs_Object = MibTableColumn
hpnicfIfQoSRTPQCbs = _HpnicfIfQoSRTPQCbs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 7, 1, 1, 1, 4),
    _HpnicfIfQoSRTPQCbs_Type()
)
hpnicfIfQoSRTPQCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSRTPQCbs.setStatus("current")
_HpnicfIfQoSRTPQRowStatus_Type = RowStatus
_HpnicfIfQoSRTPQRowStatus_Object = MibTableColumn
hpnicfIfQoSRTPQRowStatus = _HpnicfIfQoSRTPQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 7, 1, 1, 1, 5),
    _HpnicfIfQoSRTPQRowStatus_Type()
)
hpnicfIfQoSRTPQRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSRTPQRowStatus.setStatus("current")
_HpnicfIfQoSRTPQRunInfoGroup_ObjectIdentity = ObjectIdentity
hpnicfIfQoSRTPQRunInfoGroup = _HpnicfIfQoSRTPQRunInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 7, 2)
)
_HpnicfIfQoSRTPQRunInfoTable_Object = MibTable
hpnicfIfQoSRTPQRunInfoTable = _HpnicfIfQoSRTPQRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 7, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSRTPQRunInfoTable.setStatus("current")
_HpnicfIfQoSRTPQRunInfoEntry_Object = MibTableRow
hpnicfIfQoSRTPQRunInfoEntry = _HpnicfIfQoSRTPQRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 7, 2, 1, 1)
)
hpnicfIfQoSRTPQRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSRTPQRunInfoEntry.setStatus("current")
_HpnicfIfQoSRTPQPacketNumber_Type = Integer32
_HpnicfIfQoSRTPQPacketNumber_Object = MibTableColumn
hpnicfIfQoSRTPQPacketNumber = _HpnicfIfQoSRTPQPacketNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 7, 2, 1, 1, 1),
    _HpnicfIfQoSRTPQPacketNumber_Type()
)
hpnicfIfQoSRTPQPacketNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSRTPQPacketNumber.setStatus("current")
_HpnicfIfQoSRTPQPacketSize_Type = Integer32
_HpnicfIfQoSRTPQPacketSize_Object = MibTableColumn
hpnicfIfQoSRTPQPacketSize = _HpnicfIfQoSRTPQPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 7, 2, 1, 1, 2),
    _HpnicfIfQoSRTPQPacketSize_Type()
)
hpnicfIfQoSRTPQPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSRTPQPacketSize.setStatus("current")
_HpnicfIfQoSRTPQOutputPackets_Type = Counter64
_HpnicfIfQoSRTPQOutputPackets_Object = MibTableColumn
hpnicfIfQoSRTPQOutputPackets = _HpnicfIfQoSRTPQOutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 7, 2, 1, 1, 3),
    _HpnicfIfQoSRTPQOutputPackets_Type()
)
hpnicfIfQoSRTPQOutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSRTPQOutputPackets.setStatus("current")
_HpnicfIfQoSRTPQDiscardPackets_Type = Counter64
_HpnicfIfQoSRTPQDiscardPackets_Object = MibTableColumn
hpnicfIfQoSRTPQDiscardPackets = _HpnicfIfQoSRTPQDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 7, 2, 1, 1, 4),
    _HpnicfIfQoSRTPQDiscardPackets_Type()
)
hpnicfIfQoSRTPQDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSRTPQDiscardPackets.setStatus("current")
_HpnicfIfQoSCarListObject_ObjectIdentity = ObjectIdentity
hpnicfIfQoSCarListObject = _HpnicfIfQoSCarListObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 8)
)
_HpnicfIfQoCarListGroup_ObjectIdentity = ObjectIdentity
hpnicfIfQoCarListGroup = _HpnicfIfQoCarListGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 8, 1)
)
_HpnicfIfQoSCarlTable_Object = MibTable
hpnicfIfQoSCarlTable = _HpnicfIfQoSCarlTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 8, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSCarlTable.setStatus("current")
_HpnicfIfQoSCarlEntry_Object = MibTableRow
hpnicfIfQoSCarlEntry = _HpnicfIfQoSCarlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 8, 1, 1, 1)
)
hpnicfIfQoSCarlEntry.setIndexNames(
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSCarlListNum"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSCarlEntry.setStatus("current")
_HpnicfIfQoSCarlListNum_Type = Integer32
_HpnicfIfQoSCarlListNum_Object = MibTableColumn
hpnicfIfQoSCarlListNum = _HpnicfIfQoSCarlListNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 8, 1, 1, 1, 1),
    _HpnicfIfQoSCarlListNum_Type()
)
hpnicfIfQoSCarlListNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSCarlListNum.setStatus("current")


class _HpnicfIfQoSCarlParaType_Type(Integer32):
    """Custom type hpnicfIfQoSCarlParaType based on Integer32"""
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


_HpnicfIfQoSCarlParaType_Type.__name__ = "Integer32"
_HpnicfIfQoSCarlParaType_Object = MibTableColumn
hpnicfIfQoSCarlParaType = _HpnicfIfQoSCarlParaType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 8, 1, 1, 1, 2),
    _HpnicfIfQoSCarlParaType_Type()
)
hpnicfIfQoSCarlParaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSCarlParaType.setStatus("current")
_HpnicfIfQoSCarlParaValue_Type = OctetString
_HpnicfIfQoSCarlParaValue_Object = MibTableColumn
hpnicfIfQoSCarlParaValue = _HpnicfIfQoSCarlParaValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 8, 1, 1, 1, 3),
    _HpnicfIfQoSCarlParaValue_Type()
)
hpnicfIfQoSCarlParaValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSCarlParaValue.setStatus("current")
_HpnicfIfQoSCarlRowStatus_Type = RowStatus
_HpnicfIfQoSCarlRowStatus_Object = MibTableColumn
hpnicfIfQoSCarlRowStatus = _HpnicfIfQoSCarlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 2, 8, 1, 1, 1, 4),
    _HpnicfIfQoSCarlRowStatus_Type()
)
hpnicfIfQoSCarlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSCarlRowStatus.setStatus("current")
_HpnicfIfQoSLineRateObjects_ObjectIdentity = ObjectIdentity
hpnicfIfQoSLineRateObjects = _HpnicfIfQoSLineRateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 3)
)
_HpnicfIfQoSLRConfigTable_Object = MibTable
hpnicfIfQoSLRConfigTable = _HpnicfIfQoSLRConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSLRConfigTable.setStatus("current")
_HpnicfIfQoSLRConfigEntry_Object = MibTableRow
hpnicfIfQoSLRConfigEntry = _HpnicfIfQoSLRConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 3, 1, 1)
)
hpnicfIfQoSLRConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSLRDirection"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSLRConfigEntry.setStatus("current")
_HpnicfIfQoSLRDirection_Type = Direction
_HpnicfIfQoSLRDirection_Object = MibTableColumn
hpnicfIfQoSLRDirection = _HpnicfIfQoSLRDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 3, 1, 1, 1),
    _HpnicfIfQoSLRDirection_Type()
)
hpnicfIfQoSLRDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSLRDirection.setStatus("current")
_HpnicfIfQoSLRCir_Type = Unsigned32
_HpnicfIfQoSLRCir_Object = MibTableColumn
hpnicfIfQoSLRCir = _HpnicfIfQoSLRCir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 3, 1, 1, 2),
    _HpnicfIfQoSLRCir_Type()
)
hpnicfIfQoSLRCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSLRCir.setStatus("current")
_HpnicfIfQoSLRCbs_Type = Unsigned32
_HpnicfIfQoSLRCbs_Object = MibTableColumn
hpnicfIfQoSLRCbs = _HpnicfIfQoSLRCbs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 3, 1, 1, 3),
    _HpnicfIfQoSLRCbs_Type()
)
hpnicfIfQoSLRCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSLRCbs.setStatus("current")
_HpnicfIfQoSLREbs_Type = Unsigned32
_HpnicfIfQoSLREbs_Object = MibTableColumn
hpnicfIfQoSLREbs = _HpnicfIfQoSLREbs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 3, 1, 1, 4),
    _HpnicfIfQoSLREbs_Type()
)
hpnicfIfQoSLREbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSLREbs.setStatus("current")
_HpnicfIfQoSRowStatus_Type = RowStatus
_HpnicfIfQoSRowStatus_Object = MibTableColumn
hpnicfIfQoSRowStatus = _HpnicfIfQoSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 3, 1, 1, 5),
    _HpnicfIfQoSRowStatus_Type()
)
hpnicfIfQoSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSRowStatus.setStatus("current")
_HpnicfIfQoSLRPir_Type = Unsigned32
_HpnicfIfQoSLRPir_Object = MibTableColumn
hpnicfIfQoSLRPir = _HpnicfIfQoSLRPir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 3, 1, 1, 6),
    _HpnicfIfQoSLRPir_Type()
)
hpnicfIfQoSLRPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSLRPir.setStatus("current")


class _HpnicfIfQoSLRUnit_Type(Integer32):
    """Custom type hpnicfIfQoSLRUnit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unitAbsolute", 1),
          ("unitPercent", 2))
    )


_HpnicfIfQoSLRUnit_Type.__name__ = "Integer32"
_HpnicfIfQoSLRUnit_Object = MibTableColumn
hpnicfIfQoSLRUnit = _HpnicfIfQoSLRUnit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 3, 1, 1, 7),
    _HpnicfIfQoSLRUnit_Type()
)
hpnicfIfQoSLRUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSLRUnit.setStatus("current")
_HpnicfIfQoSLRRunInfoTable_Object = MibTable
hpnicfIfQoSLRRunInfoTable = _HpnicfIfQoSLRRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSLRRunInfoTable.setStatus("current")
_HpnicfIfQoSLRRunInfoEntry_Object = MibTableRow
hpnicfIfQoSLRRunInfoEntry = _HpnicfIfQoSLRRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 3, 2, 1)
)
hpnicfIfQoSLRRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSLRDirection"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSLRRunInfoEntry.setStatus("current")
_HpnicfIfQoSLRRunInfoPassedPackets_Type = Counter64
_HpnicfIfQoSLRRunInfoPassedPackets_Object = MibTableColumn
hpnicfIfQoSLRRunInfoPassedPackets = _HpnicfIfQoSLRRunInfoPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 3, 2, 1, 1),
    _HpnicfIfQoSLRRunInfoPassedPackets_Type()
)
hpnicfIfQoSLRRunInfoPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSLRRunInfoPassedPackets.setStatus("current")
_HpnicfIfQoSLRRunInfoPassedBytes_Type = Counter64
_HpnicfIfQoSLRRunInfoPassedBytes_Object = MibTableColumn
hpnicfIfQoSLRRunInfoPassedBytes = _HpnicfIfQoSLRRunInfoPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 3, 2, 1, 2),
    _HpnicfIfQoSLRRunInfoPassedBytes_Type()
)
hpnicfIfQoSLRRunInfoPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSLRRunInfoPassedBytes.setStatus("current")
_HpnicfIfQoSLRRunInfoDelayedPackets_Type = Counter64
_HpnicfIfQoSLRRunInfoDelayedPackets_Object = MibTableColumn
hpnicfIfQoSLRRunInfoDelayedPackets = _HpnicfIfQoSLRRunInfoDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 3, 2, 1, 3),
    _HpnicfIfQoSLRRunInfoDelayedPackets_Type()
)
hpnicfIfQoSLRRunInfoDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSLRRunInfoDelayedPackets.setStatus("current")
_HpnicfIfQoSLRRunInfoDelayedBytes_Type = Counter64
_HpnicfIfQoSLRRunInfoDelayedBytes_Object = MibTableColumn
hpnicfIfQoSLRRunInfoDelayedBytes = _HpnicfIfQoSLRRunInfoDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 3, 2, 1, 4),
    _HpnicfIfQoSLRRunInfoDelayedBytes_Type()
)
hpnicfIfQoSLRRunInfoDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSLRRunInfoDelayedBytes.setStatus("current")


class _HpnicfIfQoSLRRunInfoActiveShaping_Type(Integer32):
    """Custom type hpnicfIfQoSLRRunInfoActiveShaping based on Integer32"""
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


_HpnicfIfQoSLRRunInfoActiveShaping_Type.__name__ = "Integer32"
_HpnicfIfQoSLRRunInfoActiveShaping_Object = MibTableColumn
hpnicfIfQoSLRRunInfoActiveShaping = _HpnicfIfQoSLRRunInfoActiveShaping_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 3, 2, 1, 5),
    _HpnicfIfQoSLRRunInfoActiveShaping_Type()
)
hpnicfIfQoSLRRunInfoActiveShaping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSLRRunInfoActiveShaping.setStatus("current")
_HpnicfIfQoSCARObjects_ObjectIdentity = ObjectIdentity
hpnicfIfQoSCARObjects = _HpnicfIfQoSCARObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4)
)
_HpnicfIfQoSAggregativeCarGroup_ObjectIdentity = ObjectIdentity
hpnicfIfQoSAggregativeCarGroup = _HpnicfIfQoSAggregativeCarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1)
)
_HpnicfIfQoSAggregativeCarNextIndex_Type = Integer32
_HpnicfIfQoSAggregativeCarNextIndex_Object = MibScalar
hpnicfIfQoSAggregativeCarNextIndex = _HpnicfIfQoSAggregativeCarNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 1),
    _HpnicfIfQoSAggregativeCarNextIndex_Type()
)
hpnicfIfQoSAggregativeCarNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarNextIndex.setStatus("current")
_HpnicfIfQoSAggregativeCarConfigTable_Object = MibTable
hpnicfIfQoSAggregativeCarConfigTable = _HpnicfIfQoSAggregativeCarConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarConfigTable.setStatus("current")
_HpnicfIfQoSAggregativeCarConfigEntry_Object = MibTableRow
hpnicfIfQoSAggregativeCarConfigEntry = _HpnicfIfQoSAggregativeCarConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 2, 1)
)
hpnicfIfQoSAggregativeCarConfigEntry.setIndexNames(
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSAggregativeCarIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarConfigEntry.setStatus("current")


class _HpnicfIfQoSAggregativeCarIndex_Type(Integer32):
    """Custom type hpnicfIfQoSAggregativeCarIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_HpnicfIfQoSAggregativeCarIndex_Type.__name__ = "Integer32"
_HpnicfIfQoSAggregativeCarIndex_Object = MibTableColumn
hpnicfIfQoSAggregativeCarIndex = _HpnicfIfQoSAggregativeCarIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 2, 1, 1),
    _HpnicfIfQoSAggregativeCarIndex_Type()
)
hpnicfIfQoSAggregativeCarIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarIndex.setStatus("current")


class _HpnicfIfQoSAggregativeCarName_Type(OctetString):
    """Custom type hpnicfIfQoSAggregativeCarName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HpnicfIfQoSAggregativeCarName_Type.__name__ = "OctetString"
_HpnicfIfQoSAggregativeCarName_Object = MibTableColumn
hpnicfIfQoSAggregativeCarName = _HpnicfIfQoSAggregativeCarName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 2, 1, 2),
    _HpnicfIfQoSAggregativeCarName_Type()
)
hpnicfIfQoSAggregativeCarName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarName.setStatus("current")
_HpnicfIfQoSAggregativeCarCir_Type = Unsigned32
_HpnicfIfQoSAggregativeCarCir_Object = MibTableColumn
hpnicfIfQoSAggregativeCarCir = _HpnicfIfQoSAggregativeCarCir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 2, 1, 3),
    _HpnicfIfQoSAggregativeCarCir_Type()
)
hpnicfIfQoSAggregativeCarCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarCir.setStatus("current")
_HpnicfIfQoSAggregativeCarCbs_Type = Unsigned32
_HpnicfIfQoSAggregativeCarCbs_Object = MibTableColumn
hpnicfIfQoSAggregativeCarCbs = _HpnicfIfQoSAggregativeCarCbs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 2, 1, 4),
    _HpnicfIfQoSAggregativeCarCbs_Type()
)
hpnicfIfQoSAggregativeCarCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarCbs.setStatus("current")
_HpnicfIfQoSAggregativeCarEbs_Type = Unsigned32
_HpnicfIfQoSAggregativeCarEbs_Object = MibTableColumn
hpnicfIfQoSAggregativeCarEbs = _HpnicfIfQoSAggregativeCarEbs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 2, 1, 5),
    _HpnicfIfQoSAggregativeCarEbs_Type()
)
hpnicfIfQoSAggregativeCarEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarEbs.setStatus("current")
_HpnicfIfQoSAggregativeCarPir_Type = Unsigned32
_HpnicfIfQoSAggregativeCarPir_Object = MibTableColumn
hpnicfIfQoSAggregativeCarPir = _HpnicfIfQoSAggregativeCarPir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 2, 1, 6),
    _HpnicfIfQoSAggregativeCarPir_Type()
)
hpnicfIfQoSAggregativeCarPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarPir.setStatus("current")


class _HpnicfIfQoSAggregativeCarGreenActionType_Type(CarAction):
    """Custom type hpnicfIfQoSAggregativeCarGreenActionType based on CarAction"""


_HpnicfIfQoSAggregativeCarGreenActionType_Object = MibTableColumn
hpnicfIfQoSAggregativeCarGreenActionType = _HpnicfIfQoSAggregativeCarGreenActionType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 2, 1, 7),
    _HpnicfIfQoSAggregativeCarGreenActionType_Type()
)
hpnicfIfQoSAggregativeCarGreenActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarGreenActionType.setStatus("current")


class _HpnicfIfQoSAggregativeCarGreenActionValue_Type(Integer32):
    """Custom type hpnicfIfQoSAggregativeCarGreenActionValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HpnicfIfQoSAggregativeCarGreenActionValue_Type.__name__ = "Integer32"
_HpnicfIfQoSAggregativeCarGreenActionValue_Object = MibTableColumn
hpnicfIfQoSAggregativeCarGreenActionValue = _HpnicfIfQoSAggregativeCarGreenActionValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 2, 1, 8),
    _HpnicfIfQoSAggregativeCarGreenActionValue_Type()
)
hpnicfIfQoSAggregativeCarGreenActionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarGreenActionValue.setStatus("current")
_HpnicfIfQoSAggregativeCarYellowActionType_Type = CarAction
_HpnicfIfQoSAggregativeCarYellowActionType_Object = MibTableColumn
hpnicfIfQoSAggregativeCarYellowActionType = _HpnicfIfQoSAggregativeCarYellowActionType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 2, 1, 9),
    _HpnicfIfQoSAggregativeCarYellowActionType_Type()
)
hpnicfIfQoSAggregativeCarYellowActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarYellowActionType.setStatus("current")


class _HpnicfIfQoSAggregativeCarYellowActionValue_Type(Integer32):
    """Custom type hpnicfIfQoSAggregativeCarYellowActionValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HpnicfIfQoSAggregativeCarYellowActionValue_Type.__name__ = "Integer32"
_HpnicfIfQoSAggregativeCarYellowActionValue_Object = MibTableColumn
hpnicfIfQoSAggregativeCarYellowActionValue = _HpnicfIfQoSAggregativeCarYellowActionValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 2, 1, 10),
    _HpnicfIfQoSAggregativeCarYellowActionValue_Type()
)
hpnicfIfQoSAggregativeCarYellowActionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarYellowActionValue.setStatus("current")
_HpnicfIfQoSAggregativeCarRedActionType_Type = CarAction
_HpnicfIfQoSAggregativeCarRedActionType_Object = MibTableColumn
hpnicfIfQoSAggregativeCarRedActionType = _HpnicfIfQoSAggregativeCarRedActionType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 2, 1, 11),
    _HpnicfIfQoSAggregativeCarRedActionType_Type()
)
hpnicfIfQoSAggregativeCarRedActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarRedActionType.setStatus("current")
_HpnicfIfQoSAggregativeCarRedActionValue_Type = Integer32
_HpnicfIfQoSAggregativeCarRedActionValue_Object = MibTableColumn
hpnicfIfQoSAggregativeCarRedActionValue = _HpnicfIfQoSAggregativeCarRedActionValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 2, 1, 12),
    _HpnicfIfQoSAggregativeCarRedActionValue_Type()
)
hpnicfIfQoSAggregativeCarRedActionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarRedActionValue.setStatus("current")


class _HpnicfIfQoSAggregativeCarType_Type(Integer32):
    """Custom type hpnicfIfQoSAggregativeCarType based on Integer32"""
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


_HpnicfIfQoSAggregativeCarType_Type.__name__ = "Integer32"
_HpnicfIfQoSAggregativeCarType_Object = MibTableColumn
hpnicfIfQoSAggregativeCarType = _HpnicfIfQoSAggregativeCarType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 2, 1, 13),
    _HpnicfIfQoSAggregativeCarType_Type()
)
hpnicfIfQoSAggregativeCarType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarType.setStatus("current")
_HpnicfIfQoSAggregativeCarRowStatus_Type = RowStatus
_HpnicfIfQoSAggregativeCarRowStatus_Object = MibTableColumn
hpnicfIfQoSAggregativeCarRowStatus = _HpnicfIfQoSAggregativeCarRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 2, 1, 14),
    _HpnicfIfQoSAggregativeCarRowStatus_Type()
)
hpnicfIfQoSAggregativeCarRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarRowStatus.setStatus("current")
_HpnicfIfQoSAggregativeCarApplyTable_Object = MibTable
hpnicfIfQoSAggregativeCarApplyTable = _HpnicfIfQoSAggregativeCarApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarApplyTable.setStatus("current")
_HpnicfIfQoSAggregativeCarApplyEntry_Object = MibTableRow
hpnicfIfQoSAggregativeCarApplyEntry = _HpnicfIfQoSAggregativeCarApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 3, 1)
)
hpnicfIfQoSAggregativeCarApplyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSAggregativeCarApplyDirection"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSAggregativeCarApplyRuleType"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSAggregativeCarApplyRuleValue"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarApplyEntry.setStatus("current")
_HpnicfIfQoSAggregativeCarApplyDirection_Type = Direction
_HpnicfIfQoSAggregativeCarApplyDirection_Object = MibTableColumn
hpnicfIfQoSAggregativeCarApplyDirection = _HpnicfIfQoSAggregativeCarApplyDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 3, 1, 1),
    _HpnicfIfQoSAggregativeCarApplyDirection_Type()
)
hpnicfIfQoSAggregativeCarApplyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarApplyDirection.setStatus("current")


class _HpnicfIfQoSAggregativeCarApplyRuleType_Type(Integer32):
    """Custom type hpnicfIfQoSAggregativeCarApplyRuleType based on Integer32"""
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


_HpnicfIfQoSAggregativeCarApplyRuleType_Type.__name__ = "Integer32"
_HpnicfIfQoSAggregativeCarApplyRuleType_Object = MibTableColumn
hpnicfIfQoSAggregativeCarApplyRuleType = _HpnicfIfQoSAggregativeCarApplyRuleType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 3, 1, 2),
    _HpnicfIfQoSAggregativeCarApplyRuleType_Type()
)
hpnicfIfQoSAggregativeCarApplyRuleType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarApplyRuleType.setStatus("current")
_HpnicfIfQoSAggregativeCarApplyRuleValue_Type = Integer32
_HpnicfIfQoSAggregativeCarApplyRuleValue_Object = MibTableColumn
hpnicfIfQoSAggregativeCarApplyRuleValue = _HpnicfIfQoSAggregativeCarApplyRuleValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 3, 1, 3),
    _HpnicfIfQoSAggregativeCarApplyRuleValue_Type()
)
hpnicfIfQoSAggregativeCarApplyRuleValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarApplyRuleValue.setStatus("current")
_HpnicfIfQoSAggregativeCarApplyCarIndex_Type = Integer32
_HpnicfIfQoSAggregativeCarApplyCarIndex_Object = MibTableColumn
hpnicfIfQoSAggregativeCarApplyCarIndex = _HpnicfIfQoSAggregativeCarApplyCarIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 3, 1, 4),
    _HpnicfIfQoSAggregativeCarApplyCarIndex_Type()
)
hpnicfIfQoSAggregativeCarApplyCarIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarApplyCarIndex.setStatus("current")
_HpnicfIfQoSAggregativeCarApplyRowStatus_Type = RowStatus
_HpnicfIfQoSAggregativeCarApplyRowStatus_Object = MibTableColumn
hpnicfIfQoSAggregativeCarApplyRowStatus = _HpnicfIfQoSAggregativeCarApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 3, 1, 5),
    _HpnicfIfQoSAggregativeCarApplyRowStatus_Type()
)
hpnicfIfQoSAggregativeCarApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarApplyRowStatus.setStatus("current")
_HpnicfIfQoSAggregativeCarRunInfoTable_Object = MibTable
hpnicfIfQoSAggregativeCarRunInfoTable = _HpnicfIfQoSAggregativeCarRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarRunInfoTable.setStatus("current")
_HpnicfIfQoSAggregativeCarRunInfoEntry_Object = MibTableRow
hpnicfIfQoSAggregativeCarRunInfoEntry = _HpnicfIfQoSAggregativeCarRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 4, 1)
)
hpnicfIfQoSAggregativeCarRunInfoEntry.setIndexNames(
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSAggregativeCarIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarRunInfoEntry.setStatus("current")
_HpnicfIfQoSAggregativeCarGreenPackets_Type = Counter64
_HpnicfIfQoSAggregativeCarGreenPackets_Object = MibTableColumn
hpnicfIfQoSAggregativeCarGreenPackets = _HpnicfIfQoSAggregativeCarGreenPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 4, 1, 1),
    _HpnicfIfQoSAggregativeCarGreenPackets_Type()
)
hpnicfIfQoSAggregativeCarGreenPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarGreenPackets.setStatus("current")
_HpnicfIfQoSAggregativeCarGreenBytes_Type = Counter64
_HpnicfIfQoSAggregativeCarGreenBytes_Object = MibTableColumn
hpnicfIfQoSAggregativeCarGreenBytes = _HpnicfIfQoSAggregativeCarGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 4, 1, 2),
    _HpnicfIfQoSAggregativeCarGreenBytes_Type()
)
hpnicfIfQoSAggregativeCarGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarGreenBytes.setStatus("current")
_HpnicfIfQoSAggregativeCarYellowPackets_Type = Counter64
_HpnicfIfQoSAggregativeCarYellowPackets_Object = MibTableColumn
hpnicfIfQoSAggregativeCarYellowPackets = _HpnicfIfQoSAggregativeCarYellowPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 4, 1, 3),
    _HpnicfIfQoSAggregativeCarYellowPackets_Type()
)
hpnicfIfQoSAggregativeCarYellowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarYellowPackets.setStatus("current")
_HpnicfIfQoSAggregativeCarYellowBytes_Type = Counter64
_HpnicfIfQoSAggregativeCarYellowBytes_Object = MibTableColumn
hpnicfIfQoSAggregativeCarYellowBytes = _HpnicfIfQoSAggregativeCarYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 4, 1, 4),
    _HpnicfIfQoSAggregativeCarYellowBytes_Type()
)
hpnicfIfQoSAggregativeCarYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarYellowBytes.setStatus("current")
_HpnicfIfQoSAggregativeCarRedPackets_Type = Counter64
_HpnicfIfQoSAggregativeCarRedPackets_Object = MibTableColumn
hpnicfIfQoSAggregativeCarRedPackets = _HpnicfIfQoSAggregativeCarRedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 4, 1, 5),
    _HpnicfIfQoSAggregativeCarRedPackets_Type()
)
hpnicfIfQoSAggregativeCarRedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarRedPackets.setStatus("current")
_HpnicfIfQoSAggregativeCarRedBytes_Type = Counter64
_HpnicfIfQoSAggregativeCarRedBytes_Object = MibTableColumn
hpnicfIfQoSAggregativeCarRedBytes = _HpnicfIfQoSAggregativeCarRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 1, 4, 1, 6),
    _HpnicfIfQoSAggregativeCarRedBytes_Type()
)
hpnicfIfQoSAggregativeCarRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSAggregativeCarRedBytes.setStatus("current")
_HpnicfIfQoSTricolorCarGroup_ObjectIdentity = ObjectIdentity
hpnicfIfQoSTricolorCarGroup = _HpnicfIfQoSTricolorCarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 2)
)
_HpnicfIfQoSTricolorCarConfigTable_Object = MibTable
hpnicfIfQoSTricolorCarConfigTable = _HpnicfIfQoSTricolorCarConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSTricolorCarConfigTable.setStatus("current")
_HpnicfIfQoSTricolorCarConfigEntry_Object = MibTableRow
hpnicfIfQoSTricolorCarConfigEntry = _HpnicfIfQoSTricolorCarConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 2, 1, 1)
)
hpnicfIfQoSTricolorCarConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSTricolorCarDirection"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSTricolorCarType"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSTricolorCarValue"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSTricolorCarConfigEntry.setStatus("current")
_HpnicfIfQoSTricolorCarDirection_Type = Direction
_HpnicfIfQoSTricolorCarDirection_Object = MibTableColumn
hpnicfIfQoSTricolorCarDirection = _HpnicfIfQoSTricolorCarDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 2, 1, 1, 1),
    _HpnicfIfQoSTricolorCarDirection_Type()
)
hpnicfIfQoSTricolorCarDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSTricolorCarDirection.setStatus("current")


class _HpnicfIfQoSTricolorCarType_Type(Integer32):
    """Custom type hpnicfIfQoSTricolorCarType based on Integer32"""
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


_HpnicfIfQoSTricolorCarType_Type.__name__ = "Integer32"
_HpnicfIfQoSTricolorCarType_Object = MibTableColumn
hpnicfIfQoSTricolorCarType = _HpnicfIfQoSTricolorCarType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 2, 1, 1, 2),
    _HpnicfIfQoSTricolorCarType_Type()
)
hpnicfIfQoSTricolorCarType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSTricolorCarType.setStatus("current")
_HpnicfIfQoSTricolorCarValue_Type = Integer32
_HpnicfIfQoSTricolorCarValue_Object = MibTableColumn
hpnicfIfQoSTricolorCarValue = _HpnicfIfQoSTricolorCarValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 2, 1, 1, 3),
    _HpnicfIfQoSTricolorCarValue_Type()
)
hpnicfIfQoSTricolorCarValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSTricolorCarValue.setStatus("current")
_HpnicfIfQoSTricolorCarCir_Type = Unsigned32
_HpnicfIfQoSTricolorCarCir_Object = MibTableColumn
hpnicfIfQoSTricolorCarCir = _HpnicfIfQoSTricolorCarCir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 2, 1, 1, 4),
    _HpnicfIfQoSTricolorCarCir_Type()
)
hpnicfIfQoSTricolorCarCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSTricolorCarCir.setStatus("current")
_HpnicfIfQoSTricolorCarCbs_Type = Unsigned32
_HpnicfIfQoSTricolorCarCbs_Object = MibTableColumn
hpnicfIfQoSTricolorCarCbs = _HpnicfIfQoSTricolorCarCbs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 2, 1, 1, 5),
    _HpnicfIfQoSTricolorCarCbs_Type()
)
hpnicfIfQoSTricolorCarCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSTricolorCarCbs.setStatus("current")
_HpnicfIfQoSTricolorCarEbs_Type = Unsigned32
_HpnicfIfQoSTricolorCarEbs_Object = MibTableColumn
hpnicfIfQoSTricolorCarEbs = _HpnicfIfQoSTricolorCarEbs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 2, 1, 1, 6),
    _HpnicfIfQoSTricolorCarEbs_Type()
)
hpnicfIfQoSTricolorCarEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSTricolorCarEbs.setStatus("current")
_HpnicfIfQoSTricolorCarPir_Type = Unsigned32
_HpnicfIfQoSTricolorCarPir_Object = MibTableColumn
hpnicfIfQoSTricolorCarPir = _HpnicfIfQoSTricolorCarPir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 2, 1, 1, 7),
    _HpnicfIfQoSTricolorCarPir_Type()
)
hpnicfIfQoSTricolorCarPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSTricolorCarPir.setStatus("current")


class _HpnicfIfQoSTricolorCarGreenActionType_Type(CarAction):
    """Custom type hpnicfIfQoSTricolorCarGreenActionType based on CarAction"""


_HpnicfIfQoSTricolorCarGreenActionType_Object = MibTableColumn
hpnicfIfQoSTricolorCarGreenActionType = _HpnicfIfQoSTricolorCarGreenActionType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 2, 1, 1, 8),
    _HpnicfIfQoSTricolorCarGreenActionType_Type()
)
hpnicfIfQoSTricolorCarGreenActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSTricolorCarGreenActionType.setStatus("current")


class _HpnicfIfQoSTricolorCarGreenActionValue_Type(Integer32):
    """Custom type hpnicfIfQoSTricolorCarGreenActionValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HpnicfIfQoSTricolorCarGreenActionValue_Type.__name__ = "Integer32"
_HpnicfIfQoSTricolorCarGreenActionValue_Object = MibTableColumn
hpnicfIfQoSTricolorCarGreenActionValue = _HpnicfIfQoSTricolorCarGreenActionValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 2, 1, 1, 9),
    _HpnicfIfQoSTricolorCarGreenActionValue_Type()
)
hpnicfIfQoSTricolorCarGreenActionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSTricolorCarGreenActionValue.setStatus("current")


class _HpnicfIfQoSTricolorCarYellowActionType_Type(CarAction):
    """Custom type hpnicfIfQoSTricolorCarYellowActionType based on CarAction"""


_HpnicfIfQoSTricolorCarYellowActionType_Object = MibTableColumn
hpnicfIfQoSTricolorCarYellowActionType = _HpnicfIfQoSTricolorCarYellowActionType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 2, 1, 1, 10),
    _HpnicfIfQoSTricolorCarYellowActionType_Type()
)
hpnicfIfQoSTricolorCarYellowActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSTricolorCarYellowActionType.setStatus("current")


class _HpnicfIfQoSTricolorCarYellowActionValue_Type(Integer32):
    """Custom type hpnicfIfQoSTricolorCarYellowActionValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HpnicfIfQoSTricolorCarYellowActionValue_Type.__name__ = "Integer32"
_HpnicfIfQoSTricolorCarYellowActionValue_Object = MibTableColumn
hpnicfIfQoSTricolorCarYellowActionValue = _HpnicfIfQoSTricolorCarYellowActionValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 2, 1, 1, 11),
    _HpnicfIfQoSTricolorCarYellowActionValue_Type()
)
hpnicfIfQoSTricolorCarYellowActionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSTricolorCarYellowActionValue.setStatus("current")


class _HpnicfIfQoSTricolorCarRedActionType_Type(CarAction):
    """Custom type hpnicfIfQoSTricolorCarRedActionType based on CarAction"""


_HpnicfIfQoSTricolorCarRedActionType_Object = MibTableColumn
hpnicfIfQoSTricolorCarRedActionType = _HpnicfIfQoSTricolorCarRedActionType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 2, 1, 1, 12),
    _HpnicfIfQoSTricolorCarRedActionType_Type()
)
hpnicfIfQoSTricolorCarRedActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSTricolorCarRedActionType.setStatus("current")


class _HpnicfIfQoSTricolorCarRedActionValue_Type(Integer32):
    """Custom type hpnicfIfQoSTricolorCarRedActionValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HpnicfIfQoSTricolorCarRedActionValue_Type.__name__ = "Integer32"
_HpnicfIfQoSTricolorCarRedActionValue_Object = MibTableColumn
hpnicfIfQoSTricolorCarRedActionValue = _HpnicfIfQoSTricolorCarRedActionValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 2, 1, 1, 13),
    _HpnicfIfQoSTricolorCarRedActionValue_Type()
)
hpnicfIfQoSTricolorCarRedActionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSTricolorCarRedActionValue.setStatus("current")
_HpnicfIfQoSTricolorCarRowStatus_Type = RowStatus
_HpnicfIfQoSTricolorCarRowStatus_Object = MibTableColumn
hpnicfIfQoSTricolorCarRowStatus = _HpnicfIfQoSTricolorCarRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 2, 1, 1, 14),
    _HpnicfIfQoSTricolorCarRowStatus_Type()
)
hpnicfIfQoSTricolorCarRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSTricolorCarRowStatus.setStatus("current")
_HpnicfIfQoSTricolorCarRunInfoTable_Object = MibTable
hpnicfIfQoSTricolorCarRunInfoTable = _HpnicfIfQoSTricolorCarRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSTricolorCarRunInfoTable.setStatus("current")
_HpnicfIfQoSTricolorCarRunInfoEntry_Object = MibTableRow
hpnicfIfQoSTricolorCarRunInfoEntry = _HpnicfIfQoSTricolorCarRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 2, 2, 1)
)
hpnicfIfQoSTricolorCarRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSTricolorCarDirection"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSTricolorCarType"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSTricolorCarValue"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSTricolorCarRunInfoEntry.setStatus("current")
_HpnicfIfQoSTricolorCarGreenPackets_Type = Counter64
_HpnicfIfQoSTricolorCarGreenPackets_Object = MibTableColumn
hpnicfIfQoSTricolorCarGreenPackets = _HpnicfIfQoSTricolorCarGreenPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 2, 2, 1, 1),
    _HpnicfIfQoSTricolorCarGreenPackets_Type()
)
hpnicfIfQoSTricolorCarGreenPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSTricolorCarGreenPackets.setStatus("current")
_HpnicfIfQoSTricolorCarGreenBytes_Type = Counter64
_HpnicfIfQoSTricolorCarGreenBytes_Object = MibTableColumn
hpnicfIfQoSTricolorCarGreenBytes = _HpnicfIfQoSTricolorCarGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 2, 2, 1, 2),
    _HpnicfIfQoSTricolorCarGreenBytes_Type()
)
hpnicfIfQoSTricolorCarGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSTricolorCarGreenBytes.setStatus("current")
_HpnicfIfQoSTricolorCarYellowPackets_Type = Counter64
_HpnicfIfQoSTricolorCarYellowPackets_Object = MibTableColumn
hpnicfIfQoSTricolorCarYellowPackets = _HpnicfIfQoSTricolorCarYellowPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 2, 2, 1, 3),
    _HpnicfIfQoSTricolorCarYellowPackets_Type()
)
hpnicfIfQoSTricolorCarYellowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSTricolorCarYellowPackets.setStatus("current")
_HpnicfIfQoSTricolorCarYellowBytes_Type = Counter64
_HpnicfIfQoSTricolorCarYellowBytes_Object = MibTableColumn
hpnicfIfQoSTricolorCarYellowBytes = _HpnicfIfQoSTricolorCarYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 2, 2, 1, 4),
    _HpnicfIfQoSTricolorCarYellowBytes_Type()
)
hpnicfIfQoSTricolorCarYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSTricolorCarYellowBytes.setStatus("current")
_HpnicfIfQoSTricolorCarRedPackets_Type = Counter64
_HpnicfIfQoSTricolorCarRedPackets_Object = MibTableColumn
hpnicfIfQoSTricolorCarRedPackets = _HpnicfIfQoSTricolorCarRedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 2, 2, 1, 5),
    _HpnicfIfQoSTricolorCarRedPackets_Type()
)
hpnicfIfQoSTricolorCarRedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSTricolorCarRedPackets.setStatus("current")
_HpnicfIfQoSTricolorCarRedBytes_Type = Counter64
_HpnicfIfQoSTricolorCarRedBytes_Object = MibTableColumn
hpnicfIfQoSTricolorCarRedBytes = _HpnicfIfQoSTricolorCarRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 4, 2, 2, 1, 6),
    _HpnicfIfQoSTricolorCarRedBytes_Type()
)
hpnicfIfQoSTricolorCarRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSTricolorCarRedBytes.setStatus("current")
_HpnicfIfQoSGTSObjects_ObjectIdentity = ObjectIdentity
hpnicfIfQoSGTSObjects = _HpnicfIfQoSGTSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 5)
)
_HpnicfIfQoSGTSConfigTable_Object = MibTable
hpnicfIfQoSGTSConfigTable = _HpnicfIfQoSGTSConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSGTSConfigTable.setStatus("current")
_HpnicfIfQoSGTSConfigEntry_Object = MibTableRow
hpnicfIfQoSGTSConfigEntry = _HpnicfIfQoSGTSConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 5, 1, 1)
)
hpnicfIfQoSGTSConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSGTSClassRuleType"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSGTSClassRuleValue"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSGTSConfigEntry.setStatus("current")


class _HpnicfIfQoSGTSClassRuleType_Type(Integer32):
    """Custom type hpnicfIfQoSGTSClassRuleType based on Integer32"""
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


_HpnicfIfQoSGTSClassRuleType_Type.__name__ = "Integer32"
_HpnicfIfQoSGTSClassRuleType_Object = MibTableColumn
hpnicfIfQoSGTSClassRuleType = _HpnicfIfQoSGTSClassRuleType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 5, 1, 1, 1),
    _HpnicfIfQoSGTSClassRuleType_Type()
)
hpnicfIfQoSGTSClassRuleType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSGTSClassRuleType.setStatus("current")
_HpnicfIfQoSGTSClassRuleValue_Type = Integer32
_HpnicfIfQoSGTSClassRuleValue_Object = MibTableColumn
hpnicfIfQoSGTSClassRuleValue = _HpnicfIfQoSGTSClassRuleValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 5, 1, 1, 2),
    _HpnicfIfQoSGTSClassRuleValue_Type()
)
hpnicfIfQoSGTSClassRuleValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSGTSClassRuleValue.setStatus("current")
_HpnicfIfQoSGTSCir_Type = Unsigned32
_HpnicfIfQoSGTSCir_Object = MibTableColumn
hpnicfIfQoSGTSCir = _HpnicfIfQoSGTSCir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 5, 1, 1, 3),
    _HpnicfIfQoSGTSCir_Type()
)
hpnicfIfQoSGTSCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSGTSCir.setStatus("current")
_HpnicfIfQoSGTSCbs_Type = Unsigned32
_HpnicfIfQoSGTSCbs_Object = MibTableColumn
hpnicfIfQoSGTSCbs = _HpnicfIfQoSGTSCbs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 5, 1, 1, 4),
    _HpnicfIfQoSGTSCbs_Type()
)
hpnicfIfQoSGTSCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSGTSCbs.setStatus("current")
_HpnicfIfQoSGTSEbs_Type = Unsigned32
_HpnicfIfQoSGTSEbs_Object = MibTableColumn
hpnicfIfQoSGTSEbs = _HpnicfIfQoSGTSEbs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 5, 1, 1, 5),
    _HpnicfIfQoSGTSEbs_Type()
)
hpnicfIfQoSGTSEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSGTSEbs.setStatus("current")
_HpnicfIfQoSGTSQueueLength_Type = Integer32
_HpnicfIfQoSGTSQueueLength_Object = MibTableColumn
hpnicfIfQoSGTSQueueLength = _HpnicfIfQoSGTSQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 5, 1, 1, 6),
    _HpnicfIfQoSGTSQueueLength_Type()
)
hpnicfIfQoSGTSQueueLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSGTSQueueLength.setStatus("current")
_HpnicfIfQoSGTSConfigRowStatus_Type = RowStatus
_HpnicfIfQoSGTSConfigRowStatus_Object = MibTableColumn
hpnicfIfQoSGTSConfigRowStatus = _HpnicfIfQoSGTSConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 5, 1, 1, 7),
    _HpnicfIfQoSGTSConfigRowStatus_Type()
)
hpnicfIfQoSGTSConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSGTSConfigRowStatus.setStatus("current")
_HpnicfIfQoSGTSRunInfoTable_Object = MibTable
hpnicfIfQoSGTSRunInfoTable = _HpnicfIfQoSGTSRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 5, 2)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSGTSRunInfoTable.setStatus("current")
_HpnicfIfQoSGTSRunInfoEntry_Object = MibTableRow
hpnicfIfQoSGTSRunInfoEntry = _HpnicfIfQoSGTSRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 5, 2, 1)
)
hpnicfIfQoSGTSRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSGTSClassRuleType"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSGTSClassRuleValue"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSGTSRunInfoEntry.setStatus("current")
_HpnicfIfQoSGTSQueueSize_Type = Integer32
_HpnicfIfQoSGTSQueueSize_Object = MibTableColumn
hpnicfIfQoSGTSQueueSize = _HpnicfIfQoSGTSQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 5, 2, 1, 1),
    _HpnicfIfQoSGTSQueueSize_Type()
)
hpnicfIfQoSGTSQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSGTSQueueSize.setStatus("current")
_HpnicfIfQoSGTSPassedPackets_Type = Counter64
_HpnicfIfQoSGTSPassedPackets_Object = MibTableColumn
hpnicfIfQoSGTSPassedPackets = _HpnicfIfQoSGTSPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 5, 2, 1, 2),
    _HpnicfIfQoSGTSPassedPackets_Type()
)
hpnicfIfQoSGTSPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSGTSPassedPackets.setStatus("current")
_HpnicfIfQoSGTSPassedBytes_Type = Counter64
_HpnicfIfQoSGTSPassedBytes_Object = MibTableColumn
hpnicfIfQoSGTSPassedBytes = _HpnicfIfQoSGTSPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 5, 2, 1, 3),
    _HpnicfIfQoSGTSPassedBytes_Type()
)
hpnicfIfQoSGTSPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSGTSPassedBytes.setStatus("current")
_HpnicfIfQoSGTSDiscardPackets_Type = Counter64
_HpnicfIfQoSGTSDiscardPackets_Object = MibTableColumn
hpnicfIfQoSGTSDiscardPackets = _HpnicfIfQoSGTSDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 5, 2, 1, 4),
    _HpnicfIfQoSGTSDiscardPackets_Type()
)
hpnicfIfQoSGTSDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSGTSDiscardPackets.setStatus("current")
_HpnicfIfQoSGTSDiscardBytes_Type = Counter64
_HpnicfIfQoSGTSDiscardBytes_Object = MibTableColumn
hpnicfIfQoSGTSDiscardBytes = _HpnicfIfQoSGTSDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 5, 2, 1, 5),
    _HpnicfIfQoSGTSDiscardBytes_Type()
)
hpnicfIfQoSGTSDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSGTSDiscardBytes.setStatus("current")
_HpnicfIfQoSGTSDelayedPackets_Type = Counter64
_HpnicfIfQoSGTSDelayedPackets_Object = MibTableColumn
hpnicfIfQoSGTSDelayedPackets = _HpnicfIfQoSGTSDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 5, 2, 1, 6),
    _HpnicfIfQoSGTSDelayedPackets_Type()
)
hpnicfIfQoSGTSDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSGTSDelayedPackets.setStatus("current")
_HpnicfIfQoSGTSDelayedBytes_Type = Counter64
_HpnicfIfQoSGTSDelayedBytes_Object = MibTableColumn
hpnicfIfQoSGTSDelayedBytes = _HpnicfIfQoSGTSDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 5, 2, 1, 7),
    _HpnicfIfQoSGTSDelayedBytes_Type()
)
hpnicfIfQoSGTSDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSGTSDelayedBytes.setStatus("current")
_HpnicfIfQoSWREDObjects_ObjectIdentity = ObjectIdentity
hpnicfIfQoSWREDObjects = _HpnicfIfQoSWREDObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6)
)
_HpnicfIfQoSWredGroupGroup_ObjectIdentity = ObjectIdentity
hpnicfIfQoSWredGroupGroup = _HpnicfIfQoSWredGroupGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 1)
)
_HpnicfIfQoSWredGroupNextIndex_Type = Integer32
_HpnicfIfQoSWredGroupNextIndex_Object = MibScalar
hpnicfIfQoSWredGroupNextIndex = _HpnicfIfQoSWredGroupNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 1, 1),
    _HpnicfIfQoSWredGroupNextIndex_Type()
)
hpnicfIfQoSWredGroupNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredGroupNextIndex.setStatus("current")
_HpnicfIfQoSWredGroupTable_Object = MibTable
hpnicfIfQoSWredGroupTable = _HpnicfIfQoSWredGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSWredGroupTable.setStatus("current")
_HpnicfIfQoSWredGroupEntry_Object = MibTableRow
hpnicfIfQoSWredGroupEntry = _HpnicfIfQoSWredGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 1, 2, 1)
)
hpnicfIfQoSWredGroupEntry.setIndexNames(
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSWredGroupIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSWredGroupEntry.setStatus("current")
_HpnicfIfQoSWredGroupIndex_Type = Integer32
_HpnicfIfQoSWredGroupIndex_Object = MibTableColumn
hpnicfIfQoSWredGroupIndex = _HpnicfIfQoSWredGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 1, 2, 1, 1),
    _HpnicfIfQoSWredGroupIndex_Type()
)
hpnicfIfQoSWredGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredGroupIndex.setStatus("current")


class _HpnicfIfQoSWredGroupName_Type(OctetString):
    """Custom type hpnicfIfQoSWredGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfIfQoSWredGroupName_Type.__name__ = "OctetString"
_HpnicfIfQoSWredGroupName_Object = MibTableColumn
hpnicfIfQoSWredGroupName = _HpnicfIfQoSWredGroupName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 1, 2, 1, 2),
    _HpnicfIfQoSWredGroupName_Type()
)
hpnicfIfQoSWredGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredGroupName.setStatus("current")


class _HpnicfIfQoSWredGroupType_Type(Integer32):
    """Custom type hpnicfIfQoSWredGroupType based on Integer32"""
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


_HpnicfIfQoSWredGroupType_Type.__name__ = "Integer32"
_HpnicfIfQoSWredGroupType_Object = MibTableColumn
hpnicfIfQoSWredGroupType = _HpnicfIfQoSWredGroupType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 1, 2, 1, 3),
    _HpnicfIfQoSWredGroupType_Type()
)
hpnicfIfQoSWredGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredGroupType.setStatus("current")


class _HpnicfIfQoSWredGroupWeightingConstant_Type(Integer32):
    """Custom type hpnicfIfQoSWredGroupWeightingConstant based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HpnicfIfQoSWredGroupWeightingConstant_Type.__name__ = "Integer32"
_HpnicfIfQoSWredGroupWeightingConstant_Object = MibTableColumn
hpnicfIfQoSWredGroupWeightingConstant = _HpnicfIfQoSWredGroupWeightingConstant_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 1, 2, 1, 4),
    _HpnicfIfQoSWredGroupWeightingConstant_Type()
)
hpnicfIfQoSWredGroupWeightingConstant.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredGroupWeightingConstant.setStatus("current")
_HpnicfIfQoSWredGroupRowStatus_Type = RowStatus
_HpnicfIfQoSWredGroupRowStatus_Object = MibTableColumn
hpnicfIfQoSWredGroupRowStatus = _HpnicfIfQoSWredGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 1, 2, 1, 6),
    _HpnicfIfQoSWredGroupRowStatus_Type()
)
hpnicfIfQoSWredGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredGroupRowStatus.setStatus("current")
_HpnicfIfQoSWredGroupContentTable_Object = MibTable
hpnicfIfQoSWredGroupContentTable = _HpnicfIfQoSWredGroupContentTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSWredGroupContentTable.setStatus("current")
_HpnicfIfQoSWredGroupContentEntry_Object = MibTableRow
hpnicfIfQoSWredGroupContentEntry = _HpnicfIfQoSWredGroupContentEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 1, 3, 1)
)
hpnicfIfQoSWredGroupContentEntry.setIndexNames(
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSWredGroupIndex"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSWredGroupContentIndex"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSWredGroupContentSubIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSWredGroupContentEntry.setStatus("current")


class _HpnicfIfQoSWredGroupContentIndex_Type(Integer32):
    """Custom type hpnicfIfQoSWredGroupContentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HpnicfIfQoSWredGroupContentIndex_Type.__name__ = "Integer32"
_HpnicfIfQoSWredGroupContentIndex_Object = MibTableColumn
hpnicfIfQoSWredGroupContentIndex = _HpnicfIfQoSWredGroupContentIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 1, 3, 1, 1),
    _HpnicfIfQoSWredGroupContentIndex_Type()
)
hpnicfIfQoSWredGroupContentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredGroupContentIndex.setStatus("current")


class _HpnicfIfQoSWredGroupContentSubIndex_Type(Integer32):
    """Custom type hpnicfIfQoSWredGroupContentSubIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HpnicfIfQoSWredGroupContentSubIndex_Type.__name__ = "Integer32"
_HpnicfIfQoSWredGroupContentSubIndex_Object = MibTableColumn
hpnicfIfQoSWredGroupContentSubIndex = _HpnicfIfQoSWredGroupContentSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 1, 3, 1, 2),
    _HpnicfIfQoSWredGroupContentSubIndex_Type()
)
hpnicfIfQoSWredGroupContentSubIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredGroupContentSubIndex.setStatus("current")
_HpnicfIfQoSWredLowLimit_Type = Integer32
_HpnicfIfQoSWredLowLimit_Object = MibTableColumn
hpnicfIfQoSWredLowLimit = _HpnicfIfQoSWredLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 1, 3, 1, 3),
    _HpnicfIfQoSWredLowLimit_Type()
)
hpnicfIfQoSWredLowLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredLowLimit.setStatus("current")
_HpnicfIfQoSWredHighLimit_Type = Integer32
_HpnicfIfQoSWredHighLimit_Object = MibTableColumn
hpnicfIfQoSWredHighLimit = _HpnicfIfQoSWredHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 1, 3, 1, 4),
    _HpnicfIfQoSWredHighLimit_Type()
)
hpnicfIfQoSWredHighLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredHighLimit.setStatus("current")
_HpnicfIfQoSWredDiscardProb_Type = Integer32
_HpnicfIfQoSWredDiscardProb_Object = MibTableColumn
hpnicfIfQoSWredDiscardProb = _HpnicfIfQoSWredDiscardProb_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 1, 3, 1, 5),
    _HpnicfIfQoSWredDiscardProb_Type()
)
hpnicfIfQoSWredDiscardProb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredDiscardProb.setStatus("current")


class _HpnicfIfQoSWredGroupExponent_Type(Integer32):
    """Custom type hpnicfIfQoSWredGroupExponent based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HpnicfIfQoSWredGroupExponent_Type.__name__ = "Integer32"
_HpnicfIfQoSWredGroupExponent_Object = MibTableColumn
hpnicfIfQoSWredGroupExponent = _HpnicfIfQoSWredGroupExponent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 1, 3, 1, 6),
    _HpnicfIfQoSWredGroupExponent_Type()
)
hpnicfIfQoSWredGroupExponent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredGroupExponent.setStatus("current")
_HpnicfIfQoSWredRowStatus_Type = RowStatus
_HpnicfIfQoSWredRowStatus_Object = MibTableColumn
hpnicfIfQoSWredRowStatus = _HpnicfIfQoSWredRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 1, 3, 1, 7),
    _HpnicfIfQoSWredRowStatus_Type()
)
hpnicfIfQoSWredRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredRowStatus.setStatus("current")
_HpnicfIfQoSWredGroupApplyIfTable_Object = MibTable
hpnicfIfQoSWredGroupApplyIfTable = _HpnicfIfQoSWredGroupApplyIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSWredGroupApplyIfTable.setStatus("current")
_HpnicfIfQoSWredGroupApplyIfEntry_Object = MibTableRow
hpnicfIfQoSWredGroupApplyIfEntry = _HpnicfIfQoSWredGroupApplyIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 1, 4, 1)
)
hpnicfIfQoSWredGroupApplyIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSWredGroupApplyIfEntry.setStatus("current")


class _HpnicfIfQoSWredGroupApplyIndex_Type(Integer32):
    """Custom type hpnicfIfQoSWredGroupApplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_HpnicfIfQoSWredGroupApplyIndex_Type.__name__ = "Integer32"
_HpnicfIfQoSWredGroupApplyIndex_Object = MibTableColumn
hpnicfIfQoSWredGroupApplyIndex = _HpnicfIfQoSWredGroupApplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 1, 4, 1, 1),
    _HpnicfIfQoSWredGroupApplyIndex_Type()
)
hpnicfIfQoSWredGroupApplyIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredGroupApplyIndex.setStatus("current")
_HpnicfIfQoSWredGroupApplyName_Type = OctetString
_HpnicfIfQoSWredGroupApplyName_Object = MibTableColumn
hpnicfIfQoSWredGroupApplyName = _HpnicfIfQoSWredGroupApplyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 1, 4, 1, 2),
    _HpnicfIfQoSWredGroupApplyName_Type()
)
hpnicfIfQoSWredGroupApplyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredGroupApplyName.setStatus("current")
_HpnicfIfQoSWredGroupIfRowStatus_Type = RowStatus
_HpnicfIfQoSWredGroupIfRowStatus_Object = MibTableColumn
hpnicfIfQoSWredGroupIfRowStatus = _HpnicfIfQoSWredGroupIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 1, 4, 1, 3),
    _HpnicfIfQoSWredGroupIfRowStatus_Type()
)
hpnicfIfQoSWredGroupIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredGroupIfRowStatus.setStatus("current")
_HpnicfIfQoSWredApplyIfRunInfoTable_Object = MibTable
hpnicfIfQoSWredApplyIfRunInfoTable = _HpnicfIfQoSWredApplyIfRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 1, 5)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSWredApplyIfRunInfoTable.setStatus("current")
_HpnicfIfQoSWredApplyIfRunInfoEntry_Object = MibTableRow
hpnicfIfQoSWredApplyIfRunInfoEntry = _HpnicfIfQoSWredApplyIfRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 1, 5, 1)
)
hpnicfIfQoSWredApplyIfRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSWredGroupIndex"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSWredGroupContentIndex"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSWredGroupContentSubIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSWredApplyIfRunInfoEntry.setStatus("current")
_HpnicfIfQoSWredPreRandomDropNum_Type = Counter64
_HpnicfIfQoSWredPreRandomDropNum_Object = MibTableColumn
hpnicfIfQoSWredPreRandomDropNum = _HpnicfIfQoSWredPreRandomDropNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 1, 5, 1, 1),
    _HpnicfIfQoSWredPreRandomDropNum_Type()
)
hpnicfIfQoSWredPreRandomDropNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredPreRandomDropNum.setStatus("current")
_HpnicfIfQoSWredPreTailDropNum_Type = Counter64
_HpnicfIfQoSWredPreTailDropNum_Object = MibTableColumn
hpnicfIfQoSWredPreTailDropNum = _HpnicfIfQoSWredPreTailDropNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 1, 5, 1, 2),
    _HpnicfIfQoSWredPreTailDropNum_Type()
)
hpnicfIfQoSWredPreTailDropNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWredPreTailDropNum.setStatus("current")
_HpnicfIfQoSPortWredGroup_ObjectIdentity = ObjectIdentity
hpnicfIfQoSPortWredGroup = _HpnicfIfQoSPortWredGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 2)
)
_HpnicfIfQoSPortWredWeightConstantTable_Object = MibTable
hpnicfIfQoSPortWredWeightConstantTable = _HpnicfIfQoSPortWredWeightConstantTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSPortWredWeightConstantTable.setStatus("current")
_HpnicfIfQoSPortWredWeightConstantEntry_Object = MibTableRow
hpnicfIfQoSPortWredWeightConstantEntry = _HpnicfIfQoSPortWredWeightConstantEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 2, 1, 1)
)
hpnicfIfQoSPortWredWeightConstantEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSPortWredWeightConstantEntry.setStatus("current")
_HpnicfIfQoSPortWredEnable_Type = TruthValue
_HpnicfIfQoSPortWredEnable_Object = MibTableColumn
hpnicfIfQoSPortWredEnable = _HpnicfIfQoSPortWredEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 2, 1, 1, 1),
    _HpnicfIfQoSPortWredEnable_Type()
)
hpnicfIfQoSPortWredEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSPortWredEnable.setStatus("current")


class _HpnicfIfQoSPortWredWeightConstant_Type(Integer32):
    """Custom type hpnicfIfQoSPortWredWeightConstant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpnicfIfQoSPortWredWeightConstant_Type.__name__ = "Integer32"
_HpnicfIfQoSPortWredWeightConstant_Object = MibTableColumn
hpnicfIfQoSPortWredWeightConstant = _HpnicfIfQoSPortWredWeightConstant_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 2, 1, 1, 2),
    _HpnicfIfQoSPortWredWeightConstant_Type()
)
hpnicfIfQoSPortWredWeightConstant.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSPortWredWeightConstant.setStatus("current")
_HpnicfIfQoSPortWredWeightConstantRowStatus_Type = RowStatus
_HpnicfIfQoSPortWredWeightConstantRowStatus_Object = MibTableColumn
hpnicfIfQoSPortWredWeightConstantRowStatus = _HpnicfIfQoSPortWredWeightConstantRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 2, 1, 1, 3),
    _HpnicfIfQoSPortWredWeightConstantRowStatus_Type()
)
hpnicfIfQoSPortWredWeightConstantRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSPortWredWeightConstantRowStatus.setStatus("current")
_HpnicfIfQoSPortWredPreConfigTable_Object = MibTable
hpnicfIfQoSPortWredPreConfigTable = _HpnicfIfQoSPortWredPreConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSPortWredPreConfigTable.setStatus("current")
_HpnicfIfQoSPortWredPreConfigEntry_Object = MibTableRow
hpnicfIfQoSPortWredPreConfigEntry = _HpnicfIfQoSPortWredPreConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 2, 2, 1)
)
hpnicfIfQoSPortWredPreConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSPortWredPreID"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSPortWredPreConfigEntry.setStatus("current")
_HpnicfIfQoSPortWredPreID_Type = Integer32
_HpnicfIfQoSPortWredPreID_Object = MibTableColumn
hpnicfIfQoSPortWredPreID = _HpnicfIfQoSPortWredPreID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 2, 2, 1, 1),
    _HpnicfIfQoSPortWredPreID_Type()
)
hpnicfIfQoSPortWredPreID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSPortWredPreID.setStatus("current")
_HpnicfIfQoSPortWredPreLowLimit_Type = Integer32
_HpnicfIfQoSPortWredPreLowLimit_Object = MibTableColumn
hpnicfIfQoSPortWredPreLowLimit = _HpnicfIfQoSPortWredPreLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 2, 2, 1, 2),
    _HpnicfIfQoSPortWredPreLowLimit_Type()
)
hpnicfIfQoSPortWredPreLowLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSPortWredPreLowLimit.setStatus("current")
_HpnicfIfQoSPortWredPreHighLimit_Type = Integer32
_HpnicfIfQoSPortWredPreHighLimit_Object = MibTableColumn
hpnicfIfQoSPortWredPreHighLimit = _HpnicfIfQoSPortWredPreHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 2, 2, 1, 3),
    _HpnicfIfQoSPortWredPreHighLimit_Type()
)
hpnicfIfQoSPortWredPreHighLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSPortWredPreHighLimit.setStatus("current")
_HpnicfIfQoSPortWredPreDiscardProbability_Type = Integer32
_HpnicfIfQoSPortWredPreDiscardProbability_Object = MibTableColumn
hpnicfIfQoSPortWredPreDiscardProbability = _HpnicfIfQoSPortWredPreDiscardProbability_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 2, 2, 1, 4),
    _HpnicfIfQoSPortWredPreDiscardProbability_Type()
)
hpnicfIfQoSPortWredPreDiscardProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSPortWredPreDiscardProbability.setStatus("current")
_HpnicfIfQoSPortWredPreRowStatus_Type = RowStatus
_HpnicfIfQoSPortWredPreRowStatus_Object = MibTableColumn
hpnicfIfQoSPortWredPreRowStatus = _HpnicfIfQoSPortWredPreRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 2, 2, 1, 5),
    _HpnicfIfQoSPortWredPreRowStatus_Type()
)
hpnicfIfQoSPortWredPreRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSPortWredPreRowStatus.setStatus("current")
_HpnicfIfQoSPortWredRunInfoTable_Object = MibTable
hpnicfIfQoSPortWredRunInfoTable = _HpnicfIfQoSPortWredRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSPortWredRunInfoTable.setStatus("current")
_HpnicfIfQoSPortWredRunInfoEntry_Object = MibTableRow
hpnicfIfQoSPortWredRunInfoEntry = _HpnicfIfQoSPortWredRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 2, 3, 1)
)
hpnicfIfQoSPortWredRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSPortWredPreID"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSPortWredRunInfoEntry.setStatus("current")
_HpnicfIfQoSWREDTailDropNum_Type = Counter64
_HpnicfIfQoSWREDTailDropNum_Object = MibTableColumn
hpnicfIfQoSWREDTailDropNum = _HpnicfIfQoSWREDTailDropNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 2, 3, 1, 1),
    _HpnicfIfQoSWREDTailDropNum_Type()
)
hpnicfIfQoSWREDTailDropNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWREDTailDropNum.setStatus("current")
_HpnicfIfQoSWREDRandomDropNum_Type = Counter64
_HpnicfIfQoSWREDRandomDropNum_Object = MibTableColumn
hpnicfIfQoSWREDRandomDropNum = _HpnicfIfQoSWREDRandomDropNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 6, 2, 3, 1, 2),
    _HpnicfIfQoSWREDRandomDropNum_Type()
)
hpnicfIfQoSWREDRandomDropNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSWREDRandomDropNum.setStatus("current")
_HpnicfIfQoSPortPriorityObjects_ObjectIdentity = ObjectIdentity
hpnicfIfQoSPortPriorityObjects = _HpnicfIfQoSPortPriorityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 7)
)
_HpnicfIfQoSPortPriorityConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfIfQoSPortPriorityConfigGroup = _HpnicfIfQoSPortPriorityConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 7, 1)
)
_HpnicfIfQoSPortPriorityTable_Object = MibTable
hpnicfIfQoSPortPriorityTable = _HpnicfIfQoSPortPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSPortPriorityTable.setStatus("current")
_HpnicfIfQoSPortPriorityEntry_Object = MibTableRow
hpnicfIfQoSPortPriorityEntry = _HpnicfIfQoSPortPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 7, 1, 1, 1)
)
hpnicfIfQoSPortPriorityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSPortPriorityEntry.setStatus("current")


class _HpnicfIfQoSPortPriorityValue_Type(Integer32):
    """Custom type hpnicfIfQoSPortPriorityValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfIfQoSPortPriorityValue_Type.__name__ = "Integer32"
_HpnicfIfQoSPortPriorityValue_Object = MibTableColumn
hpnicfIfQoSPortPriorityValue = _HpnicfIfQoSPortPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 7, 1, 1, 1, 1),
    _HpnicfIfQoSPortPriorityValue_Type()
)
hpnicfIfQoSPortPriorityValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIfQoSPortPriorityValue.setStatus("current")
_HpnicfIfQoSPortPirorityTrustTable_Object = MibTable
hpnicfIfQoSPortPirorityTrustTable = _HpnicfIfQoSPortPirorityTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 7, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSPortPirorityTrustTable.setStatus("current")
_HpnicfIfQoSPortPirorityTrustEntry_Object = MibTableRow
hpnicfIfQoSPortPirorityTrustEntry = _HpnicfIfQoSPortPirorityTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 7, 1, 2, 1)
)
hpnicfIfQoSPortPirorityTrustEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSPortPirorityTrustEntry.setStatus("current")


class _HpnicfIfQoSPortPriorityTrustTrustType_Type(Integer32):
    """Custom type hpnicfIfQoSPortPriorityTrustTrustType based on Integer32"""
    defaultValue = 1

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
        *(("auto", 7),
          ("dot11e", 6),
          ("dot1p", 2),
          ("dscp", 3),
          ("exp", 4),
          ("ipPrecedence", 5),
          ("untrust", 1))
    )


_HpnicfIfQoSPortPriorityTrustTrustType_Type.__name__ = "Integer32"
_HpnicfIfQoSPortPriorityTrustTrustType_Object = MibTableColumn
hpnicfIfQoSPortPriorityTrustTrustType = _HpnicfIfQoSPortPriorityTrustTrustType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 7, 1, 2, 1, 1),
    _HpnicfIfQoSPortPriorityTrustTrustType_Type()
)
hpnicfIfQoSPortPriorityTrustTrustType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIfQoSPortPriorityTrustTrustType.setStatus("current")


class _HpnicfIfQoSPortPriorityTrustOvercastType_Type(Integer32):
    """Custom type hpnicfIfQoSPortPriorityTrustOvercastType based on Integer32"""
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
        *(("noOvercast", 1),
          ("overcast", 4),
          ("overcastCOS", 3),
          ("overcastDSCP", 2))
    )


_HpnicfIfQoSPortPriorityTrustOvercastType_Type.__name__ = "Integer32"
_HpnicfIfQoSPortPriorityTrustOvercastType_Object = MibTableColumn
hpnicfIfQoSPortPriorityTrustOvercastType = _HpnicfIfQoSPortPriorityTrustOvercastType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 7, 1, 2, 1, 2),
    _HpnicfIfQoSPortPriorityTrustOvercastType_Type()
)
hpnicfIfQoSPortPriorityTrustOvercastType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIfQoSPortPriorityTrustOvercastType.setStatus("current")
_HpnicfIfQoSMapObjects_ObjectIdentity = ObjectIdentity
hpnicfIfQoSMapObjects = _HpnicfIfQoSMapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 9)
)
_HpnicfIfQoSPriMapConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfIfQoSPriMapConfigGroup = _HpnicfIfQoSPriMapConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 9, 1)
)
_HpnicfIfQoSPriMapGroupNextIndex_Type = Integer32
_HpnicfIfQoSPriMapGroupNextIndex_Object = MibScalar
hpnicfIfQoSPriMapGroupNextIndex = _HpnicfIfQoSPriMapGroupNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 9, 1, 1),
    _HpnicfIfQoSPriMapGroupNextIndex_Type()
)
hpnicfIfQoSPriMapGroupNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIfQoSPriMapGroupNextIndex.setStatus("current")
_HpnicfIfQoSPriMapGroupTable_Object = MibTable
hpnicfIfQoSPriMapGroupTable = _HpnicfIfQoSPriMapGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSPriMapGroupTable.setStatus("current")
_HpnicfIfQoSPriMapGroupEntry_Object = MibTableRow
hpnicfIfQoSPriMapGroupEntry = _HpnicfIfQoSPriMapGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 9, 1, 2, 1)
)
hpnicfIfQoSPriMapGroupEntry.setIndexNames(
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSPriMapGroupIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSPriMapGroupEntry.setStatus("current")
_HpnicfIfQoSPriMapGroupIndex_Type = Integer32
_HpnicfIfQoSPriMapGroupIndex_Object = MibTableColumn
hpnicfIfQoSPriMapGroupIndex = _HpnicfIfQoSPriMapGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 9, 1, 2, 1, 1),
    _HpnicfIfQoSPriMapGroupIndex_Type()
)
hpnicfIfQoSPriMapGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSPriMapGroupIndex.setStatus("current")


class _HpnicfIfQoSPriMapGroupType_Type(Integer32):
    """Custom type hpnicfIfQoSPriMapGroupType based on Integer32"""
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


_HpnicfIfQoSPriMapGroupType_Type.__name__ = "Integer32"
_HpnicfIfQoSPriMapGroupType_Object = MibTableColumn
hpnicfIfQoSPriMapGroupType = _HpnicfIfQoSPriMapGroupType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 9, 1, 2, 1, 2),
    _HpnicfIfQoSPriMapGroupType_Type()
)
hpnicfIfQoSPriMapGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSPriMapGroupType.setStatus("current")


class _HpnicfIfQoSPriMapGroupName_Type(OctetString):
    """Custom type hpnicfIfQoSPriMapGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfIfQoSPriMapGroupName_Type.__name__ = "OctetString"
_HpnicfIfQoSPriMapGroupName_Object = MibTableColumn
hpnicfIfQoSPriMapGroupName = _HpnicfIfQoSPriMapGroupName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 9, 1, 2, 1, 3),
    _HpnicfIfQoSPriMapGroupName_Type()
)
hpnicfIfQoSPriMapGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSPriMapGroupName.setStatus("current")
_HpnicfIfQoSPriMapGroupRowStatus_Type = RowStatus
_HpnicfIfQoSPriMapGroupRowStatus_Object = MibTableColumn
hpnicfIfQoSPriMapGroupRowStatus = _HpnicfIfQoSPriMapGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 9, 1, 2, 1, 4),
    _HpnicfIfQoSPriMapGroupRowStatus_Type()
)
hpnicfIfQoSPriMapGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSPriMapGroupRowStatus.setStatus("current")
_HpnicfIfQoSPriMapContentTable_Object = MibTable
hpnicfIfQoSPriMapContentTable = _HpnicfIfQoSPriMapContentTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 9, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSPriMapContentTable.setStatus("current")
_HpnicfIfQoSPriMapContentEntry_Object = MibTableRow
hpnicfIfQoSPriMapContentEntry = _HpnicfIfQoSPriMapContentEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 9, 1, 3, 1)
)
hpnicfIfQoSPriMapContentEntry.setIndexNames(
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSPriMapGroupIndex"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSPriMapGroupImportValue"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSPriMapContentEntry.setStatus("current")


class _HpnicfIfQoSPriMapGroupImportValue_Type(Integer32):
    """Custom type hpnicfIfQoSPriMapGroupImportValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HpnicfIfQoSPriMapGroupImportValue_Type.__name__ = "Integer32"
_HpnicfIfQoSPriMapGroupImportValue_Object = MibTableColumn
hpnicfIfQoSPriMapGroupImportValue = _HpnicfIfQoSPriMapGroupImportValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 9, 1, 3, 1, 1),
    _HpnicfIfQoSPriMapGroupImportValue_Type()
)
hpnicfIfQoSPriMapGroupImportValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSPriMapGroupImportValue.setStatus("current")


class _HpnicfIfQoSPriMapGroupExportValue_Type(Integer32):
    """Custom type hpnicfIfQoSPriMapGroupExportValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HpnicfIfQoSPriMapGroupExportValue_Type.__name__ = "Integer32"
_HpnicfIfQoSPriMapGroupExportValue_Object = MibTableColumn
hpnicfIfQoSPriMapGroupExportValue = _HpnicfIfQoSPriMapGroupExportValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 9, 1, 3, 1, 2),
    _HpnicfIfQoSPriMapGroupExportValue_Type()
)
hpnicfIfQoSPriMapGroupExportValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSPriMapGroupExportValue.setStatus("current")
_HpnicfIfQoSPriMapContentRowStatus_Type = RowStatus
_HpnicfIfQoSPriMapContentRowStatus_Object = MibTableColumn
hpnicfIfQoSPriMapContentRowStatus = _HpnicfIfQoSPriMapContentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 9, 1, 3, 1, 3),
    _HpnicfIfQoSPriMapContentRowStatus_Type()
)
hpnicfIfQoSPriMapContentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSPriMapContentRowStatus.setStatus("current")
_HpnicfIfQoSPrePriMapTable_Object = MibTable
hpnicfIfQoSPrePriMapTable = _HpnicfIfQoSPrePriMapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 9, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSPrePriMapTable.setStatus("current")
_HpnicfIfQoSPrePriMapEntry_Object = MibTableRow
hpnicfIfQoSPrePriMapEntry = _HpnicfIfQoSPrePriMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 9, 1, 4, 1)
)
hpnicfIfQoSPrePriMapEntry.setIndexNames(
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSPrePriMapTableType"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSPrePriMapTableColor"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSPrePriMapTableDirection"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfIfQoSPrePriMapTableImportValue"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSPrePriMapEntry.setStatus("current")


class _HpnicfIfQoSPrePriMapTableType_Type(Integer32):
    """Custom type hpnicfIfQoSPrePriMapTableType based on Integer32"""
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
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("dot11eToLp", 27),
          ("dot1pToDot1p", 34),
          ("dot1pToDp", 2),
          ("dot1pToDscp", 8),
          ("dot1pToExp", 30),
          ("dot1pToLp", 1),
          ("dot1pToRpr", 15),
          ("dscpToDot1p", 7),
          ("dscpToDp", 6),
          ("dscpToDscp", 9),
          ("dscpToExp", 10),
          ("dscpToLp", 4),
          ("dscpToRpr", 16),
          ("expToDot1p", 12),
          ("expToDp", 5),
          ("expToDscp", 11),
          ("expToExp", 13),
          ("expToLp", 3),
          ("expToRpr", 17),
          ("ippreToRpr", 18),
          ("lpToDot11e", 28),
          ("lpToDot1p", 14),
          ("lpToDp", 32),
          ("lpToExp", 31),
          ("lpToLp", 29),
          ("lpTodscp", 26),
          ("upToDot1p", 19),
          ("upToDp", 22),
          ("upToDscp", 20),
          ("upToExp", 21),
          ("upToFc", 25),
          ("upToLp", 23),
          ("upToRpr", 24),
          ("upToUp", 33))
    )


_HpnicfIfQoSPrePriMapTableType_Type.__name__ = "Integer32"
_HpnicfIfQoSPrePriMapTableType_Object = MibTableColumn
hpnicfIfQoSPrePriMapTableType = _HpnicfIfQoSPrePriMapTableType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 9, 1, 4, 1, 1),
    _HpnicfIfQoSPrePriMapTableType_Type()
)
hpnicfIfQoSPrePriMapTableType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSPrePriMapTableType.setStatus("current")


class _HpnicfIfQoSPrePriMapTableColor_Type(Integer32):
    """Custom type hpnicfIfQoSPrePriMapTableColor based on Integer32"""
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
        *(("green", 2),
          ("noColor", 1),
          ("red", 4),
          ("yellow", 3))
    )


_HpnicfIfQoSPrePriMapTableColor_Type.__name__ = "Integer32"
_HpnicfIfQoSPrePriMapTableColor_Object = MibTableColumn
hpnicfIfQoSPrePriMapTableColor = _HpnicfIfQoSPrePriMapTableColor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 9, 1, 4, 1, 2),
    _HpnicfIfQoSPrePriMapTableColor_Type()
)
hpnicfIfQoSPrePriMapTableColor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSPrePriMapTableColor.setStatus("current")


class _HpnicfIfQoSPrePriMapTableDirection_Type(Integer32):
    """Custom type hpnicfIfQoSPrePriMapTableDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 2),
          ("noDirection", 1),
          ("outbound", 3))
    )


_HpnicfIfQoSPrePriMapTableDirection_Type.__name__ = "Integer32"
_HpnicfIfQoSPrePriMapTableDirection_Object = MibTableColumn
hpnicfIfQoSPrePriMapTableDirection = _HpnicfIfQoSPrePriMapTableDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 9, 1, 4, 1, 3),
    _HpnicfIfQoSPrePriMapTableDirection_Type()
)
hpnicfIfQoSPrePriMapTableDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSPrePriMapTableDirection.setStatus("current")


class _HpnicfIfQoSPrePriMapTableImportValue_Type(Integer32):
    """Custom type hpnicfIfQoSPrePriMapTableImportValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HpnicfIfQoSPrePriMapTableImportValue_Type.__name__ = "Integer32"
_HpnicfIfQoSPrePriMapTableImportValue_Object = MibTableColumn
hpnicfIfQoSPrePriMapTableImportValue = _HpnicfIfQoSPrePriMapTableImportValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 9, 1, 4, 1, 4),
    _HpnicfIfQoSPrePriMapTableImportValue_Type()
)
hpnicfIfQoSPrePriMapTableImportValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIfQoSPrePriMapTableImportValue.setStatus("current")


class _HpnicfIfQoSPrePriMapTableExportValue_Type(Integer32):
    """Custom type hpnicfIfQoSPrePriMapTableExportValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HpnicfIfQoSPrePriMapTableExportValue_Type.__name__ = "Integer32"
_HpnicfIfQoSPrePriMapTableExportValue_Object = MibTableColumn
hpnicfIfQoSPrePriMapTableExportValue = _HpnicfIfQoSPrePriMapTableExportValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 9, 1, 4, 1, 5),
    _HpnicfIfQoSPrePriMapTableExportValue_Type()
)
hpnicfIfQoSPrePriMapTableExportValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIfQoSPrePriMapTableExportValue.setStatus("current")
_HpnicfIfQoSL3PlusObjects_ObjectIdentity = ObjectIdentity
hpnicfIfQoSL3PlusObjects = _HpnicfIfQoSL3PlusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 10)
)
_HpnicfIfQoSPortBindingGroup_ObjectIdentity = ObjectIdentity
hpnicfIfQoSPortBindingGroup = _HpnicfIfQoSPortBindingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 10, 1)
)
_HpnicfIfQoSPortBindingTable_Object = MibTable
hpnicfIfQoSPortBindingTable = _HpnicfIfQoSPortBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 10, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfIfQoSPortBindingTable.setStatus("current")
_HpnicfIfQoSPortBindingEntry_Object = MibTableRow
hpnicfIfQoSPortBindingEntry = _HpnicfIfQoSPortBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 10, 1, 1, 1)
)
hpnicfIfQoSPortBindingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIfQoSPortBindingEntry.setStatus("current")
_HpnicfIfQoSBindingIf_Type = Integer32
_HpnicfIfQoSBindingIf_Object = MibTableColumn
hpnicfIfQoSBindingIf = _HpnicfIfQoSBindingIf_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 10, 1, 1, 1, 1),
    _HpnicfIfQoSBindingIf_Type()
)
hpnicfIfQoSBindingIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSBindingIf.setStatus("current")
_HpnicfIfQoSBindingRowStatus_Type = RowStatus
_HpnicfIfQoSBindingRowStatus_Object = MibTableColumn
hpnicfIfQoSBindingRowStatus = _HpnicfIfQoSBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 10, 1, 1, 1, 2),
    _HpnicfIfQoSBindingRowStatus_Type()
)
hpnicfIfQoSBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIfQoSBindingRowStatus.setStatus("current")
_HpnicfQoSTraStaObjects_ObjectIdentity = ObjectIdentity
hpnicfQoSTraStaObjects = _HpnicfQoSTraStaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 11)
)
_HpnicfQoSTraStaConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfQoSTraStaConfigGroup = _HpnicfQoSTraStaConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 11, 1)
)
_HpnicfQoSIfTraStaConfigInfoTable_Object = MibTable
hpnicfQoSIfTraStaConfigInfoTable = _HpnicfQoSIfTraStaConfigInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 11, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfQoSIfTraStaConfigInfoTable.setStatus("current")
_HpnicfQoSIfTraStaConfigInfoEntry_Object = MibTableRow
hpnicfQoSIfTraStaConfigInfoEntry = _HpnicfQoSIfTraStaConfigInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 11, 1, 1, 1)
)
hpnicfQoSIfTraStaConfigInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfQoSIfTraStaConfigDirection"),
)
if mibBuilder.loadTexts:
    hpnicfQoSIfTraStaConfigInfoEntry.setStatus("current")
_HpnicfQoSIfTraStaConfigDirection_Type = Direction
_HpnicfQoSIfTraStaConfigDirection_Object = MibTableColumn
hpnicfQoSIfTraStaConfigDirection = _HpnicfQoSIfTraStaConfigDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 11, 1, 1, 1, 1),
    _HpnicfQoSIfTraStaConfigDirection_Type()
)
hpnicfQoSIfTraStaConfigDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSIfTraStaConfigDirection.setStatus("current")


class _HpnicfQoSIfTraStaConfigQueue_Type(OctetString):
    """Custom type hpnicfQoSIfTraStaConfigQueue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_HpnicfQoSIfTraStaConfigQueue_Type.__name__ = "OctetString"
_HpnicfQoSIfTraStaConfigQueue_Object = MibTableColumn
hpnicfQoSIfTraStaConfigQueue = _HpnicfQoSIfTraStaConfigQueue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 11, 1, 1, 1, 2),
    _HpnicfQoSIfTraStaConfigQueue_Type()
)
hpnicfQoSIfTraStaConfigQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSIfTraStaConfigQueue.setStatus("current")


class _HpnicfQoSIfTraStaConfigDot1p_Type(OctetString):
    """Custom type hpnicfQoSIfTraStaConfigDot1p based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_HpnicfQoSIfTraStaConfigDot1p_Type.__name__ = "OctetString"
_HpnicfQoSIfTraStaConfigDot1p_Object = MibTableColumn
hpnicfQoSIfTraStaConfigDot1p = _HpnicfQoSIfTraStaConfigDot1p_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 11, 1, 1, 1, 3),
    _HpnicfQoSIfTraStaConfigDot1p_Type()
)
hpnicfQoSIfTraStaConfigDot1p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSIfTraStaConfigDot1p.setStatus("current")


class _HpnicfQoSIfTraStaConfigDscp_Type(OctetString):
    """Custom type hpnicfQoSIfTraStaConfigDscp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HpnicfQoSIfTraStaConfigDscp_Type.__name__ = "OctetString"
_HpnicfQoSIfTraStaConfigDscp_Object = MibTableColumn
hpnicfQoSIfTraStaConfigDscp = _HpnicfQoSIfTraStaConfigDscp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 11, 1, 1, 1, 4),
    _HpnicfQoSIfTraStaConfigDscp_Type()
)
hpnicfQoSIfTraStaConfigDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSIfTraStaConfigDscp.setStatus("current")


class _HpnicfQoSIfTraStaConfigVlan_Type(OctetString):
    """Custom type hpnicfQoSIfTraStaConfigVlan based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )


_HpnicfQoSIfTraStaConfigVlan_Type.__name__ = "OctetString"
_HpnicfQoSIfTraStaConfigVlan_Object = MibTableColumn
hpnicfQoSIfTraStaConfigVlan = _HpnicfQoSIfTraStaConfigVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 11, 1, 1, 1, 5),
    _HpnicfQoSIfTraStaConfigVlan_Type()
)
hpnicfQoSIfTraStaConfigVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSIfTraStaConfigVlan.setStatus("current")
_HpnicfQoSIfTraStaConfigStatus_Type = RowStatus
_HpnicfQoSIfTraStaConfigStatus_Object = MibTableColumn
hpnicfQoSIfTraStaConfigStatus = _HpnicfQoSIfTraStaConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 11, 1, 1, 1, 6),
    _HpnicfQoSIfTraStaConfigStatus_Type()
)
hpnicfQoSIfTraStaConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSIfTraStaConfigStatus.setStatus("current")
_HpnicfQoSTraStaRunGroup_ObjectIdentity = ObjectIdentity
hpnicfQoSTraStaRunGroup = _HpnicfQoSTraStaRunGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 11, 2)
)
_HpnicfQoSIfTraStaRunInfoTable_Object = MibTable
hpnicfQoSIfTraStaRunInfoTable = _HpnicfQoSIfTraStaRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 11, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfQoSIfTraStaRunInfoTable.setStatus("current")
_HpnicfQoSIfTraStaRunInfoEntry_Object = MibTableRow
hpnicfQoSIfTraStaRunInfoEntry = _HpnicfQoSIfTraStaRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 11, 2, 1, 1)
)
hpnicfQoSIfTraStaRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfQoSIfTraStaRunObjectType"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfQoSIfTraStaRunObjectValue"),
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfQoSIfTraStaRunDirection"),
)
if mibBuilder.loadTexts:
    hpnicfQoSIfTraStaRunInfoEntry.setStatus("current")


class _HpnicfQoSIfTraStaRunObjectType_Type(Integer32):
    """Custom type hpnicfQoSIfTraStaRunObjectType based on Integer32"""
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


_HpnicfQoSIfTraStaRunObjectType_Type.__name__ = "Integer32"
_HpnicfQoSIfTraStaRunObjectType_Object = MibTableColumn
hpnicfQoSIfTraStaRunObjectType = _HpnicfQoSIfTraStaRunObjectType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 11, 2, 1, 1, 1),
    _HpnicfQoSIfTraStaRunObjectType_Type()
)
hpnicfQoSIfTraStaRunObjectType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSIfTraStaRunObjectType.setStatus("current")
_HpnicfQoSIfTraStaRunObjectValue_Type = Integer32
_HpnicfQoSIfTraStaRunObjectValue_Object = MibTableColumn
hpnicfQoSIfTraStaRunObjectValue = _HpnicfQoSIfTraStaRunObjectValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 11, 2, 1, 1, 2),
    _HpnicfQoSIfTraStaRunObjectValue_Type()
)
hpnicfQoSIfTraStaRunObjectValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSIfTraStaRunObjectValue.setStatus("current")
_HpnicfQoSIfTraStaRunDirection_Type = Direction
_HpnicfQoSIfTraStaRunDirection_Object = MibTableColumn
hpnicfQoSIfTraStaRunDirection = _HpnicfQoSIfTraStaRunDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 11, 2, 1, 1, 3),
    _HpnicfQoSIfTraStaRunDirection_Type()
)
hpnicfQoSIfTraStaRunDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSIfTraStaRunDirection.setStatus("current")
_HpnicfQoSIfTraStaRunPassPackets_Type = Counter64
_HpnicfQoSIfTraStaRunPassPackets_Object = MibTableColumn
hpnicfQoSIfTraStaRunPassPackets = _HpnicfQoSIfTraStaRunPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 11, 2, 1, 1, 4),
    _HpnicfQoSIfTraStaRunPassPackets_Type()
)
hpnicfQoSIfTraStaRunPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfQoSIfTraStaRunPassPackets.setStatus("current")
_HpnicfQoSIfTraStaRunDropPackets_Type = Counter64
_HpnicfQoSIfTraStaRunDropPackets_Object = MibTableColumn
hpnicfQoSIfTraStaRunDropPackets = _HpnicfQoSIfTraStaRunDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 11, 2, 1, 1, 5),
    _HpnicfQoSIfTraStaRunDropPackets_Type()
)
hpnicfQoSIfTraStaRunDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfQoSIfTraStaRunDropPackets.setStatus("current")
_HpnicfQoSIfTraStaRunPassBytes_Type = Counter64
_HpnicfQoSIfTraStaRunPassBytes_Object = MibTableColumn
hpnicfQoSIfTraStaRunPassBytes = _HpnicfQoSIfTraStaRunPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 11, 2, 1, 1, 6),
    _HpnicfQoSIfTraStaRunPassBytes_Type()
)
hpnicfQoSIfTraStaRunPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfQoSIfTraStaRunPassBytes.setStatus("current")
_HpnicfQoSIfTraStaRunDropBytes_Type = Counter64
_HpnicfQoSIfTraStaRunDropBytes_Object = MibTableColumn
hpnicfQoSIfTraStaRunDropBytes = _HpnicfQoSIfTraStaRunDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 11, 2, 1, 1, 7),
    _HpnicfQoSIfTraStaRunDropBytes_Type()
)
hpnicfQoSIfTraStaRunDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfQoSIfTraStaRunDropBytes.setStatus("current")
_HpnicfQoSIfTraStaRunPassPPS_Type = Counter64
_HpnicfQoSIfTraStaRunPassPPS_Object = MibTableColumn
hpnicfQoSIfTraStaRunPassPPS = _HpnicfQoSIfTraStaRunPassPPS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 11, 2, 1, 1, 8),
    _HpnicfQoSIfTraStaRunPassPPS_Type()
)
hpnicfQoSIfTraStaRunPassPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfQoSIfTraStaRunPassPPS.setStatus("current")
_HpnicfQoSIfTraStaRunPassBPS_Type = Counter64
_HpnicfQoSIfTraStaRunPassBPS_Object = MibTableColumn
hpnicfQoSIfTraStaRunPassBPS = _HpnicfQoSIfTraStaRunPassBPS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 11, 2, 1, 1, 9),
    _HpnicfQoSIfTraStaRunPassBPS_Type()
)
hpnicfQoSIfTraStaRunPassBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfQoSIfTraStaRunPassBPS.setStatus("current")
_HpnicfQoSGlobalPriorityObject_ObjectIdentity = ObjectIdentity
hpnicfQoSGlobalPriorityObject = _HpnicfQoSGlobalPriorityObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12)
)
_HpnicfQoSRemarkTcpPortPriTable_Object = MibTable
hpnicfQoSRemarkTcpPortPriTable = _HpnicfQoSRemarkTcpPortPriTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 1)
)
if mibBuilder.loadTexts:
    hpnicfQoSRemarkTcpPortPriTable.setStatus("current")
_HpnicfQoSRemarkTcpPortPriEntry_Object = MibTableRow
hpnicfQoSRemarkTcpPortPriEntry = _HpnicfQoSRemarkTcpPortPriEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 1, 1)
)
hpnicfQoSRemarkTcpPortPriEntry.setIndexNames(
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfQoSRemarkTcpPortStart"),
)
if mibBuilder.loadTexts:
    hpnicfQoSRemarkTcpPortPriEntry.setStatus("current")


class _HpnicfQoSRemarkTcpPortStart_Type(Integer32):
    """Custom type hpnicfQoSRemarkTcpPortStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfQoSRemarkTcpPortStart_Type.__name__ = "Integer32"
_HpnicfQoSRemarkTcpPortStart_Object = MibTableColumn
hpnicfQoSRemarkTcpPortStart = _HpnicfQoSRemarkTcpPortStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 1, 1, 1),
    _HpnicfQoSRemarkTcpPortStart_Type()
)
hpnicfQoSRemarkTcpPortStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkTcpPortStart.setStatus("current")


class _HpnicfQoSRemarkTcpPortEnd_Type(Integer32):
    """Custom type hpnicfQoSRemarkTcpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfQoSRemarkTcpPortEnd_Type.__name__ = "Integer32"
_HpnicfQoSRemarkTcpPortEnd_Object = MibTableColumn
hpnicfQoSRemarkTcpPortEnd = _HpnicfQoSRemarkTcpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 1, 1, 2),
    _HpnicfQoSRemarkTcpPortEnd_Type()
)
hpnicfQoSRemarkTcpPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkTcpPortEnd.setStatus("current")


class _HpnicfQoSRemarkTcpPortType_Type(Integer32):
    """Custom type hpnicfQoSRemarkTcpPortType based on Integer32"""
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
        *(("ipAll", 1),
          ("ipv4", 2),
          ("ipv6", 3))
    )


_HpnicfQoSRemarkTcpPortType_Type.__name__ = "Integer32"
_HpnicfQoSRemarkTcpPortType_Object = MibTableColumn
hpnicfQoSRemarkTcpPortType = _HpnicfQoSRemarkTcpPortType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 1, 1, 3),
    _HpnicfQoSRemarkTcpPortType_Type()
)
hpnicfQoSRemarkTcpPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkTcpPortType.setStatus("current")


class _HpnicfQoSRemarkTcpPortDot1p_Type(Unsigned32):
    """Custom type hpnicfQoSRemarkTcpPortDot1p based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfQoSRemarkTcpPortDot1p_Type.__name__ = "Unsigned32"
_HpnicfQoSRemarkTcpPortDot1p_Object = MibTableColumn
hpnicfQoSRemarkTcpPortDot1p = _HpnicfQoSRemarkTcpPortDot1p_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 1, 1, 4),
    _HpnicfQoSRemarkTcpPortDot1p_Type()
)
hpnicfQoSRemarkTcpPortDot1p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkTcpPortDot1p.setStatus("current")


class _HpnicfQoSRemarkTcpPortDscp_Type(Unsigned32):
    """Custom type hpnicfQoSRemarkTcpPortDscp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HpnicfQoSRemarkTcpPortDscp_Type.__name__ = "Unsigned32"
_HpnicfQoSRemarkTcpPortDscp_Object = MibTableColumn
hpnicfQoSRemarkTcpPortDscp = _HpnicfQoSRemarkTcpPortDscp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 1, 1, 5),
    _HpnicfQoSRemarkTcpPortDscp_Type()
)
hpnicfQoSRemarkTcpPortDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkTcpPortDscp.setStatus("current")
_HpnicfQoSRemarkTcpPortRowStatus_Type = RowStatus
_HpnicfQoSRemarkTcpPortRowStatus_Object = MibTableColumn
hpnicfQoSRemarkTcpPortRowStatus = _HpnicfQoSRemarkTcpPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 1, 1, 6),
    _HpnicfQoSRemarkTcpPortRowStatus_Type()
)
hpnicfQoSRemarkTcpPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkTcpPortRowStatus.setStatus("current")
_HpnicfQoSRemarkUdpPortPriTable_Object = MibTable
hpnicfQoSRemarkUdpPortPriTable = _HpnicfQoSRemarkUdpPortPriTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 2)
)
if mibBuilder.loadTexts:
    hpnicfQoSRemarkUdpPortPriTable.setStatus("current")
_HpnicfQoSRemarkUdpPortPriEntry_Object = MibTableRow
hpnicfQoSRemarkUdpPortPriEntry = _HpnicfQoSRemarkUdpPortPriEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 2, 1)
)
hpnicfQoSRemarkUdpPortPriEntry.setIndexNames(
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfQoSRemarkUdpPortStart"),
)
if mibBuilder.loadTexts:
    hpnicfQoSRemarkUdpPortPriEntry.setStatus("current")


class _HpnicfQoSRemarkUdpPortStart_Type(Integer32):
    """Custom type hpnicfQoSRemarkUdpPortStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfQoSRemarkUdpPortStart_Type.__name__ = "Integer32"
_HpnicfQoSRemarkUdpPortStart_Object = MibTableColumn
hpnicfQoSRemarkUdpPortStart = _HpnicfQoSRemarkUdpPortStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 2, 1, 1),
    _HpnicfQoSRemarkUdpPortStart_Type()
)
hpnicfQoSRemarkUdpPortStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkUdpPortStart.setStatus("current")


class _HpnicfQoSRemarkUdpPortEnd_Type(Integer32):
    """Custom type hpnicfQoSRemarkUdpPortEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfQoSRemarkUdpPortEnd_Type.__name__ = "Integer32"
_HpnicfQoSRemarkUdpPortEnd_Object = MibTableColumn
hpnicfQoSRemarkUdpPortEnd = _HpnicfQoSRemarkUdpPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 2, 1, 2),
    _HpnicfQoSRemarkUdpPortEnd_Type()
)
hpnicfQoSRemarkUdpPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkUdpPortEnd.setStatus("current")


class _HpnicfQoSRemarkUdpPortType_Type(Integer32):
    """Custom type hpnicfQoSRemarkUdpPortType based on Integer32"""
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
        *(("ipAll", 1),
          ("ipv4", 2),
          ("ipv6", 3))
    )


_HpnicfQoSRemarkUdpPortType_Type.__name__ = "Integer32"
_HpnicfQoSRemarkUdpPortType_Object = MibTableColumn
hpnicfQoSRemarkUdpPortType = _HpnicfQoSRemarkUdpPortType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 2, 1, 3),
    _HpnicfQoSRemarkUdpPortType_Type()
)
hpnicfQoSRemarkUdpPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkUdpPortType.setStatus("current")


class _HpnicfQoSRemarkUdpPortDot1p_Type(Unsigned32):
    """Custom type hpnicfQoSRemarkUdpPortDot1p based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfQoSRemarkUdpPortDot1p_Type.__name__ = "Unsigned32"
_HpnicfQoSRemarkUdpPortDot1p_Object = MibTableColumn
hpnicfQoSRemarkUdpPortDot1p = _HpnicfQoSRemarkUdpPortDot1p_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 2, 1, 4),
    _HpnicfQoSRemarkUdpPortDot1p_Type()
)
hpnicfQoSRemarkUdpPortDot1p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkUdpPortDot1p.setStatus("current")


class _HpnicfQoSRemarkUdpPortDscp_Type(Unsigned32):
    """Custom type hpnicfQoSRemarkUdpPortDscp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HpnicfQoSRemarkUdpPortDscp_Type.__name__ = "Unsigned32"
_HpnicfQoSRemarkUdpPortDscp_Object = MibTableColumn
hpnicfQoSRemarkUdpPortDscp = _HpnicfQoSRemarkUdpPortDscp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 2, 1, 5),
    _HpnicfQoSRemarkUdpPortDscp_Type()
)
hpnicfQoSRemarkUdpPortDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkUdpPortDscp.setStatus("current")
_HpnicfQoSRemarkUdpPortRowStatus_Type = RowStatus
_HpnicfQoSRemarkUdpPortRowStatus_Object = MibTableColumn
hpnicfQoSRemarkUdpPortRowStatus = _HpnicfQoSRemarkUdpPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 2, 1, 6),
    _HpnicfQoSRemarkUdpPortRowStatus_Type()
)
hpnicfQoSRemarkUdpPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkUdpPortRowStatus.setStatus("current")
_HpnicfQoSRemarkIPv4AddrPriTable_Object = MibTable
hpnicfQoSRemarkIPv4AddrPriTable = _HpnicfQoSRemarkIPv4AddrPriTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 3)
)
if mibBuilder.loadTexts:
    hpnicfQoSRemarkIPv4AddrPriTable.setStatus("current")
_HpnicfQoSRemarkIPv4AddrPriEntry_Object = MibTableRow
hpnicfQoSRemarkIPv4AddrPriEntry = _HpnicfQoSRemarkIPv4AddrPriEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 3, 1)
)
hpnicfQoSRemarkIPv4AddrPriEntry.setIndexNames(
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfQoSRemarkIPv4AddrValue"),
)
if mibBuilder.loadTexts:
    hpnicfQoSRemarkIPv4AddrPriEntry.setStatus("current")
_HpnicfQoSRemarkIPv4AddrValue_Type = IpAddress
_HpnicfQoSRemarkIPv4AddrValue_Object = MibTableColumn
hpnicfQoSRemarkIPv4AddrValue = _HpnicfQoSRemarkIPv4AddrValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 3, 1, 1),
    _HpnicfQoSRemarkIPv4AddrValue_Type()
)
hpnicfQoSRemarkIPv4AddrValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkIPv4AddrValue.setStatus("current")
_HpnicfQoSRemarkIPv4AddrMask_Type = IpAddress
_HpnicfQoSRemarkIPv4AddrMask_Object = MibTableColumn
hpnicfQoSRemarkIPv4AddrMask = _HpnicfQoSRemarkIPv4AddrMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 3, 1, 2),
    _HpnicfQoSRemarkIPv4AddrMask_Type()
)
hpnicfQoSRemarkIPv4AddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkIPv4AddrMask.setStatus("current")


class _HpnicfQoSRemarkIPv4AddrMaskLength_Type(Unsigned32):
    """Custom type hpnicfQoSRemarkIPv4AddrMaskLength based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_HpnicfQoSRemarkIPv4AddrMaskLength_Type.__name__ = "Unsigned32"
_HpnicfQoSRemarkIPv4AddrMaskLength_Object = MibTableColumn
hpnicfQoSRemarkIPv4AddrMaskLength = _HpnicfQoSRemarkIPv4AddrMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 3, 1, 3),
    _HpnicfQoSRemarkIPv4AddrMaskLength_Type()
)
hpnicfQoSRemarkIPv4AddrMaskLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkIPv4AddrMaskLength.setStatus("current")


class _HpnicfQoSRemarkIPv4AddrDot1p_Type(Unsigned32):
    """Custom type hpnicfQoSRemarkIPv4AddrDot1p based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfQoSRemarkIPv4AddrDot1p_Type.__name__ = "Unsigned32"
_HpnicfQoSRemarkIPv4AddrDot1p_Object = MibTableColumn
hpnicfQoSRemarkIPv4AddrDot1p = _HpnicfQoSRemarkIPv4AddrDot1p_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 3, 1, 4),
    _HpnicfQoSRemarkIPv4AddrDot1p_Type()
)
hpnicfQoSRemarkIPv4AddrDot1p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkIPv4AddrDot1p.setStatus("current")


class _HpnicfQoSRemarkIPv4AddrDscp_Type(Unsigned32):
    """Custom type hpnicfQoSRemarkIPv4AddrDscp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HpnicfQoSRemarkIPv4AddrDscp_Type.__name__ = "Unsigned32"
_HpnicfQoSRemarkIPv4AddrDscp_Object = MibTableColumn
hpnicfQoSRemarkIPv4AddrDscp = _HpnicfQoSRemarkIPv4AddrDscp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 3, 1, 5),
    _HpnicfQoSRemarkIPv4AddrDscp_Type()
)
hpnicfQoSRemarkIPv4AddrDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkIPv4AddrDscp.setStatus("current")
_HpnicfQoSRemarkIPv4AddrRowStatus_Type = RowStatus
_HpnicfQoSRemarkIPv4AddrRowStatus_Object = MibTableColumn
hpnicfQoSRemarkIPv4AddrRowStatus = _HpnicfQoSRemarkIPv4AddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 3, 1, 6),
    _HpnicfQoSRemarkIPv4AddrRowStatus_Type()
)
hpnicfQoSRemarkIPv4AddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkIPv4AddrRowStatus.setStatus("current")
_HpnicfQoSRemarkIPv6AddrPriTable_Object = MibTable
hpnicfQoSRemarkIPv6AddrPriTable = _HpnicfQoSRemarkIPv6AddrPriTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 4)
)
if mibBuilder.loadTexts:
    hpnicfQoSRemarkIPv6AddrPriTable.setStatus("current")
_HpnicfQoSRemarkIPv6AddrPriEntry_Object = MibTableRow
hpnicfQoSRemarkIPv6AddrPriEntry = _HpnicfQoSRemarkIPv6AddrPriEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 4, 1)
)
hpnicfQoSRemarkIPv6AddrPriEntry.setIndexNames(
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfQoSRemarkIPv6AddrValue"),
)
if mibBuilder.loadTexts:
    hpnicfQoSRemarkIPv6AddrPriEntry.setStatus("current")
_HpnicfQoSRemarkIPv6AddrValue_Type = InetAddressIPv6
_HpnicfQoSRemarkIPv6AddrValue_Object = MibTableColumn
hpnicfQoSRemarkIPv6AddrValue = _HpnicfQoSRemarkIPv6AddrValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 4, 1, 1),
    _HpnicfQoSRemarkIPv6AddrValue_Type()
)
hpnicfQoSRemarkIPv6AddrValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkIPv6AddrValue.setStatus("current")


class _HpnicfQoSRemarkIPv6AddrPrefixLength_Type(InetAddressPrefixLength):
    """Custom type hpnicfQoSRemarkIPv6AddrPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 128


_HpnicfQoSRemarkIPv6AddrPrefixLength_Object = MibTableColumn
hpnicfQoSRemarkIPv6AddrPrefixLength = _HpnicfQoSRemarkIPv6AddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 4, 1, 2),
    _HpnicfQoSRemarkIPv6AddrPrefixLength_Type()
)
hpnicfQoSRemarkIPv6AddrPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkIPv6AddrPrefixLength.setStatus("current")


class _HpnicfQoSRemarkIPv6AddrDot1p_Type(Unsigned32):
    """Custom type hpnicfQoSRemarkIPv6AddrDot1p based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfQoSRemarkIPv6AddrDot1p_Type.__name__ = "Unsigned32"
_HpnicfQoSRemarkIPv6AddrDot1p_Object = MibTableColumn
hpnicfQoSRemarkIPv6AddrDot1p = _HpnicfQoSRemarkIPv6AddrDot1p_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 4, 1, 3),
    _HpnicfQoSRemarkIPv6AddrDot1p_Type()
)
hpnicfQoSRemarkIPv6AddrDot1p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkIPv6AddrDot1p.setStatus("current")


class _HpnicfQoSRemarkIPv6AddrDscp_Type(Unsigned32):
    """Custom type hpnicfQoSRemarkIPv6AddrDscp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HpnicfQoSRemarkIPv6AddrDscp_Type.__name__ = "Unsigned32"
_HpnicfQoSRemarkIPv6AddrDscp_Object = MibTableColumn
hpnicfQoSRemarkIPv6AddrDscp = _HpnicfQoSRemarkIPv6AddrDscp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 4, 1, 4),
    _HpnicfQoSRemarkIPv6AddrDscp_Type()
)
hpnicfQoSRemarkIPv6AddrDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkIPv6AddrDscp.setStatus("current")
_HpnicfQoSRemarkIPv6AddrRowStatus_Type = RowStatus
_HpnicfQoSRemarkIPv6AddrRowStatus_Object = MibTableColumn
hpnicfQoSRemarkIPv6AddrRowStatus = _HpnicfQoSRemarkIPv6AddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 4, 1, 5),
    _HpnicfQoSRemarkIPv6AddrRowStatus_Type()
)
hpnicfQoSRemarkIPv6AddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkIPv6AddrRowStatus.setStatus("current")
_HpnicfQoSRemarkProtocolPriTable_Object = MibTable
hpnicfQoSRemarkProtocolPriTable = _HpnicfQoSRemarkProtocolPriTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 5)
)
if mibBuilder.loadTexts:
    hpnicfQoSRemarkProtocolPriTable.setStatus("current")
_HpnicfQoSRemarkProtocolPriEntry_Object = MibTableRow
hpnicfQoSRemarkProtocolPriEntry = _HpnicfQoSRemarkProtocolPriEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 5, 1)
)
hpnicfQoSRemarkProtocolPriEntry.setIndexNames(
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfQoSRemarkProtocolValue"),
)
if mibBuilder.loadTexts:
    hpnicfQoSRemarkProtocolPriEntry.setStatus("current")


class _HpnicfQoSRemarkProtocolValue_Type(Integer32):
    """Custom type hpnicfQoSRemarkProtocolValue based on Integer32"""
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
        *(("appletalk", 4),
          ("arp", 3),
          ("ip", 1),
          ("ipx", 2),
          ("netbeui", 6),
          ("sna", 5))
    )


_HpnicfQoSRemarkProtocolValue_Type.__name__ = "Integer32"
_HpnicfQoSRemarkProtocolValue_Object = MibTableColumn
hpnicfQoSRemarkProtocolValue = _HpnicfQoSRemarkProtocolValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 5, 1, 1),
    _HpnicfQoSRemarkProtocolValue_Type()
)
hpnicfQoSRemarkProtocolValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkProtocolValue.setStatus("current")


class _HpnicfQoSRemarkProtocolDot1p_Type(Unsigned32):
    """Custom type hpnicfQoSRemarkProtocolDot1p based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfQoSRemarkProtocolDot1p_Type.__name__ = "Unsigned32"
_HpnicfQoSRemarkProtocolDot1p_Object = MibTableColumn
hpnicfQoSRemarkProtocolDot1p = _HpnicfQoSRemarkProtocolDot1p_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 5, 1, 2),
    _HpnicfQoSRemarkProtocolDot1p_Type()
)
hpnicfQoSRemarkProtocolDot1p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkProtocolDot1p.setStatus("current")
_HpnicfQoSRemarkProtocolRowStatus_Type = RowStatus
_HpnicfQoSRemarkProtocolRowStatus_Object = MibTableColumn
hpnicfQoSRemarkProtocolRowStatus = _HpnicfQoSRemarkProtocolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 5, 1, 3),
    _HpnicfQoSRemarkProtocolRowStatus_Type()
)
hpnicfQoSRemarkProtocolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkProtocolRowStatus.setStatus("current")
_HpnicfQoSRemarkVlanPriTable_Object = MibTable
hpnicfQoSRemarkVlanPriTable = _HpnicfQoSRemarkVlanPriTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 6)
)
if mibBuilder.loadTexts:
    hpnicfQoSRemarkVlanPriTable.setStatus("current")
_HpnicfQoSRemarkVlanPriEntry_Object = MibTableRow
hpnicfQoSRemarkVlanPriEntry = _HpnicfQoSRemarkVlanPriEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 6, 1)
)
hpnicfQoSRemarkVlanPriEntry.setIndexNames(
    (0, "HPN-ICF-IFQOS2-MIB", "hpnicfQoSRemarkVlanStart"),
)
if mibBuilder.loadTexts:
    hpnicfQoSRemarkVlanPriEntry.setStatus("current")


class _HpnicfQoSRemarkVlanStart_Type(Integer32):
    """Custom type hpnicfQoSRemarkVlanStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpnicfQoSRemarkVlanStart_Type.__name__ = "Integer32"
_HpnicfQoSRemarkVlanStart_Object = MibTableColumn
hpnicfQoSRemarkVlanStart = _HpnicfQoSRemarkVlanStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 6, 1, 1),
    _HpnicfQoSRemarkVlanStart_Type()
)
hpnicfQoSRemarkVlanStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkVlanStart.setStatus("current")


class _HpnicfQoSRemarkVlanEnd_Type(Integer32):
    """Custom type hpnicfQoSRemarkVlanEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpnicfQoSRemarkVlanEnd_Type.__name__ = "Integer32"
_HpnicfQoSRemarkVlanEnd_Object = MibTableColumn
hpnicfQoSRemarkVlanEnd = _HpnicfQoSRemarkVlanEnd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 6, 1, 2),
    _HpnicfQoSRemarkVlanEnd_Type()
)
hpnicfQoSRemarkVlanEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkVlanEnd.setStatus("current")


class _HpnicfQoSRemarkVlanDot1p_Type(Unsigned32):
    """Custom type hpnicfQoSRemarkVlanDot1p based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfQoSRemarkVlanDot1p_Type.__name__ = "Unsigned32"
_HpnicfQoSRemarkVlanDot1p_Object = MibTableColumn
hpnicfQoSRemarkVlanDot1p = _HpnicfQoSRemarkVlanDot1p_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 6, 1, 3),
    _HpnicfQoSRemarkVlanDot1p_Type()
)
hpnicfQoSRemarkVlanDot1p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkVlanDot1p.setStatus("current")


class _HpnicfQoSRemarkVlanDscp_Type(Unsigned32):
    """Custom type hpnicfQoSRemarkVlanDscp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HpnicfQoSRemarkVlanDscp_Type.__name__ = "Unsigned32"
_HpnicfQoSRemarkVlanDscp_Object = MibTableColumn
hpnicfQoSRemarkVlanDscp = _HpnicfQoSRemarkVlanDscp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 6, 1, 4),
    _HpnicfQoSRemarkVlanDscp_Type()
)
hpnicfQoSRemarkVlanDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkVlanDscp.setStatus("current")
_HpnicfQoSRemarkVlanRowStatus_Type = RowStatus
_HpnicfQoSRemarkVlanRowStatus_Object = MibTableColumn
hpnicfQoSRemarkVlanRowStatus = _HpnicfQoSRemarkVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 6, 1, 5),
    _HpnicfQoSRemarkVlanRowStatus_Type()
)
hpnicfQoSRemarkVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfQoSRemarkVlanRowStatus.setStatus("current")
_HpnicfQoSTypeOfServiceObjects_ObjectIdentity = ObjectIdentity
hpnicfQoSTypeOfServiceObjects = _HpnicfQoSTypeOfServiceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 7)
)


class _HpnicfQoSTypeOfServiceMode_Type(Integer32):
    """Custom type hpnicfQoSTypeOfServiceMode based on Integer32"""
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
        *(("disabled", 1),
          ("dscp", 3),
          ("ipPrecedence", 2))
    )


_HpnicfQoSTypeOfServiceMode_Type.__name__ = "Integer32"
_HpnicfQoSTypeOfServiceMode_Object = MibScalar
hpnicfQoSTypeOfServiceMode = _HpnicfQoSTypeOfServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 65, 1, 12, 7, 1),
    _HpnicfQoSTypeOfServiceMode_Type()
)
hpnicfQoSTypeOfServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfQoSTypeOfServiceMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-IFQOS2-MIB",
    **{"CarAction": CarAction,
       "PriorityQueue": PriorityQueue,
       "Direction": Direction,
       "hpnicfQos2": hpnicfQos2,
       "hpnicfIfQos2": hpnicfIfQos2,
       "hpnicfIfQoSHardwareQueueObjects": hpnicfIfQoSHardwareQueueObjects,
       "hpnicfIfQoSHardwareQueueConfigGroup": hpnicfIfQoSHardwareQueueConfigGroup,
       "hpnicfIfQoSQSModeTable": hpnicfIfQoSQSModeTable,
       "hpnicfIfQoSQSModeEntry": hpnicfIfQoSQSModeEntry,
       "hpnicfIfQoSQSMode": hpnicfIfQoSQSMode,
       "hpnicfIfQoSQSWeightTable": hpnicfIfQoSQSWeightTable,
       "hpnicfIfQoSQSWeightEntry": hpnicfIfQoSQSWeightEntry,
       "hpnicfIfQoSQueueID": hpnicfIfQoSQueueID,
       "hpnicfIfQoSQueueGroupType": hpnicfIfQoSQueueGroupType,
       "hpnicfIfQoSQSType": hpnicfIfQoSQSType,
       "hpnicfIfQoSQSValue": hpnicfIfQoSQSValue,
       "hpnicfIfQoSQSMaxDelay": hpnicfIfQoSQSMaxDelay,
       "hpnicfIfQoSQSMinBandwidth": hpnicfIfQoSQSMinBandwidth,
       "hpnicfIfQoSQSMinBandwidthPercent": hpnicfIfQoSQSMinBandwidthPercent,
       "hpnicfIfQoSHardwareQueueRunInfoGroup": hpnicfIfQoSHardwareQueueRunInfoGroup,
       "hpnicfIfQoSHardwareQueueRunInfoTable": hpnicfIfQoSHardwareQueueRunInfoTable,
       "hpnicfIfQoSHardwareQueueRunInfoEntry": hpnicfIfQoSHardwareQueueRunInfoEntry,
       "hpnicfIfQoSPassPackets": hpnicfIfQoSPassPackets,
       "hpnicfIfQoSDropPackets": hpnicfIfQoSDropPackets,
       "hpnicfIfQoSPassBytes": hpnicfIfQoSPassBytes,
       "hpnicfIfQoSPassPPS": hpnicfIfQoSPassPPS,
       "hpnicfIfQoSPassBPS": hpnicfIfQoSPassBPS,
       "hpnicfIfQoSDropBytes": hpnicfIfQoSDropBytes,
       "hpnicfIfQoSQueueLengthInPkts": hpnicfIfQoSQueueLengthInPkts,
       "hpnicfIfQoSQueueLengthInBytes": hpnicfIfQoSQueueLengthInBytes,
       "hpnicfIfQoSCurQueuePkts": hpnicfIfQoSCurQueuePkts,
       "hpnicfIfQoSCurQueueBytes": hpnicfIfQoSCurQueueBytes,
       "hpnicfIfQoSCurQueuePPS": hpnicfIfQoSCurQueuePPS,
       "hpnicfIfQoSCurQueueBPS": hpnicfIfQoSCurQueueBPS,
       "hpnicfIfQoSTailDropPkts": hpnicfIfQoSTailDropPkts,
       "hpnicfIfQoSTailDropBytes": hpnicfIfQoSTailDropBytes,
       "hpnicfIfQoSTailDropPPS": hpnicfIfQoSTailDropPPS,
       "hpnicfIfQoSTailDropBPS": hpnicfIfQoSTailDropBPS,
       "hpnicfIfQoSWredDropPkts": hpnicfIfQoSWredDropPkts,
       "hpnicfIfQoSWredDropBytes": hpnicfIfQoSWredDropBytes,
       "hpnicfIfQoSWredDropPPS": hpnicfIfQoSWredDropPPS,
       "hpnicfIfQoSWredDropBPS": hpnicfIfQoSWredDropBPS,
       "hpnicfIfQoSHQueueTcpRunInfoTable": hpnicfIfQoSHQueueTcpRunInfoTable,
       "hpnicfIfQoSHQueueTcpRunInfoEntry": hpnicfIfQoSHQueueTcpRunInfoEntry,
       "hpnicfIfQoSWredDropLPreNTcpPkts": hpnicfIfQoSWredDropLPreNTcpPkts,
       "hpnicfIfQoSWredDropLPreNTcpBytes": hpnicfIfQoSWredDropLPreNTcpBytes,
       "hpnicfIfQoSWredDropLPreNTcpPPS": hpnicfIfQoSWredDropLPreNTcpPPS,
       "hpnicfIfQoSWredDropLPreNTcpBPS": hpnicfIfQoSWredDropLPreNTcpBPS,
       "hpnicfIfQoSWredDropLPreTcpPkts": hpnicfIfQoSWredDropLPreTcpPkts,
       "hpnicfIfQoSWredDropLPreTcpBytes": hpnicfIfQoSWredDropLPreTcpBytes,
       "hpnicfIfQoSWredDropLPreTcpPPS": hpnicfIfQoSWredDropLPreTcpPPS,
       "hpnicfIfQoSWredDropLPreTcpBPS": hpnicfIfQoSWredDropLPreTcpBPS,
       "hpnicfIfQoSWredDropHPreNTcpPkts": hpnicfIfQoSWredDropHPreNTcpPkts,
       "hpnicfIfQoSWredDropHPreNTcpBytes": hpnicfIfQoSWredDropHPreNTcpBytes,
       "hpnicfIfQoSWredDropHPreNTcpPPS": hpnicfIfQoSWredDropHPreNTcpPPS,
       "hpnicfIfQoSWredDropHPreNTcpBPS": hpnicfIfQoSWredDropHPreNTcpBPS,
       "hpnicfIfQoSWredDropHPreTcpPkts": hpnicfIfQoSWredDropHPreTcpPkts,
       "hpnicfIfQoSWredDropHPreTcpBytes": hpnicfIfQoSWredDropHPreTcpBytes,
       "hpnicfIfQoSWredDropHPreTcpPPS": hpnicfIfQoSWredDropHPreTcpPPS,
       "hpnicfIfQoSWredDropHPreTcpBPS": hpnicfIfQoSWredDropHPreTcpBPS,
       "hpnicfIfQoSSoftwareQueueObjects": hpnicfIfQoSSoftwareQueueObjects,
       "hpnicfIfQoSFIFOObject": hpnicfIfQoSFIFOObject,
       "hpnicfIfQoSFIFOConfigTable": hpnicfIfQoSFIFOConfigTable,
       "hpnicfIfQoSFIFOConfigEntry": hpnicfIfQoSFIFOConfigEntry,
       "hpnicfIfQoSFIFOMaxQueueLen": hpnicfIfQoSFIFOMaxQueueLen,
       "hpnicfIfQoSFIFORunInfoTable": hpnicfIfQoSFIFORunInfoTable,
       "hpnicfIfQoSFIFORunInfoEntry": hpnicfIfQoSFIFORunInfoEntry,
       "hpnicfIfQoSFIFOSize": hpnicfIfQoSFIFOSize,
       "hpnicfIfQoSFIFODiscardPackets": hpnicfIfQoSFIFODiscardPackets,
       "hpnicfIfQoSPQObject": hpnicfIfQoSPQObject,
       "hpnicfIfQoSPQConfigGroup": hpnicfIfQoSPQConfigGroup,
       "hpnicfIfQoSPQDefaultTable": hpnicfIfQoSPQDefaultTable,
       "hpnicfIfQoSPQDefaultEntry": hpnicfIfQoSPQDefaultEntry,
       "hpnicfIfQoSPQListNumber": hpnicfIfQoSPQListNumber,
       "hpnicfIfQoSPQDefaultQueueType": hpnicfIfQoSPQDefaultQueueType,
       "hpnicfIfQoSPQQueueLengthTable": hpnicfIfQoSPQQueueLengthTable,
       "hpnicfIfQoSPQQueueLengthEntry": hpnicfIfQoSPQQueueLengthEntry,
       "hpnicfIfQoSPQQueueLengthType": hpnicfIfQoSPQQueueLengthType,
       "hpnicfIfQoSPQQueueLengthValue": hpnicfIfQoSPQQueueLengthValue,
       "hpnicfIfQoSPQClassRuleTable": hpnicfIfQoSPQClassRuleTable,
       "hpnicfIfQoSPQClassRuleEntry": hpnicfIfQoSPQClassRuleEntry,
       "hpnicfIfQoSPQClassRuleType": hpnicfIfQoSPQClassRuleType,
       "hpnicfIfQoSPQClassRuleValue": hpnicfIfQoSPQClassRuleValue,
       "hpnicfIfQoSPQClassRuleQueueType": hpnicfIfQoSPQClassRuleQueueType,
       "hpnicfIfQoSPQClassRowStatus": hpnicfIfQoSPQClassRowStatus,
       "hpnicfIfQoSPQApplyTable": hpnicfIfQoSPQApplyTable,
       "hpnicfIfQoSPQApplyEntry": hpnicfIfQoSPQApplyEntry,
       "hpnicfIfQoSPQApplyListNumber": hpnicfIfQoSPQApplyListNumber,
       "hpnicfIfQoSPQApplyRowStatus": hpnicfIfQoSPQApplyRowStatus,
       "hpnicfIfQoSPQRunInfoGroup": hpnicfIfQoSPQRunInfoGroup,
       "hpnicfIfQoSPQRunInfoTable": hpnicfIfQoSPQRunInfoTable,
       "hpnicfIfQoSPQRunInfoEntry": hpnicfIfQoSPQRunInfoEntry,
       "hpnicfIfQoSPQType": hpnicfIfQoSPQType,
       "hpnicfIfQoSPQSize": hpnicfIfQoSPQSize,
       "hpnicfIfQoSPQLength": hpnicfIfQoSPQLength,
       "hpnicfIfQoSPQDiscardPackets": hpnicfIfQoSPQDiscardPackets,
       "hpnicfIfQoSCQObject": hpnicfIfQoSCQObject,
       "hpnicfIfQoSCQConfigGroup": hpnicfIfQoSCQConfigGroup,
       "hpnicfIfQoSCQDefaultTable": hpnicfIfQoSCQDefaultTable,
       "hpnicfIfQoSCQDefaultEntry": hpnicfIfQoSCQDefaultEntry,
       "hpnicfIfQoSCQListNumber": hpnicfIfQoSCQListNumber,
       "hpnicfIfQoSCQDefaultQueueID": hpnicfIfQoSCQDefaultQueueID,
       "hpnicfIfQoSCQQueueLengthTable": hpnicfIfQoSCQQueueLengthTable,
       "hpnicfIfQoSCQQueueLengthEntry": hpnicfIfQoSCQQueueLengthEntry,
       "hpnicfIfQoSCQQueueID": hpnicfIfQoSCQQueueID,
       "hpnicfIfQoSCQQueueLength": hpnicfIfQoSCQQueueLength,
       "hpnicfIfQoSCQQueueServing": hpnicfIfQoSCQQueueServing,
       "hpnicfIfQoSCQClassRuleTable": hpnicfIfQoSCQClassRuleTable,
       "hpnicfIfQoSCQClassRuleEntry": hpnicfIfQoSCQClassRuleEntry,
       "hpnicfIfQoSCQClassRuleType": hpnicfIfQoSCQClassRuleType,
       "hpnicfIfQoSCQClassRuleValue": hpnicfIfQoSCQClassRuleValue,
       "hpnicfIfQoSCQClassRuleQueueID": hpnicfIfQoSCQClassRuleQueueID,
       "hpnicfIfQoSCQClassRowStatus": hpnicfIfQoSCQClassRowStatus,
       "hpnicfIfQoSCQApplyTable": hpnicfIfQoSCQApplyTable,
       "hpnicfIfQoSCQApplyEntry": hpnicfIfQoSCQApplyEntry,
       "hpnicfIfQoSCQApplyListNumber": hpnicfIfQoSCQApplyListNumber,
       "hpnicfIfQoSCQApplyRowStatus": hpnicfIfQoSCQApplyRowStatus,
       "hpnicfIfQoSCQRunInfoGroup": hpnicfIfQoSCQRunInfoGroup,
       "hpnicfIfQoSCQRunInfoTable": hpnicfIfQoSCQRunInfoTable,
       "hpnicfIfQoSCQRunInfoEntry": hpnicfIfQoSCQRunInfoEntry,
       "hpnicfIfQoSCQRunInfoSize": hpnicfIfQoSCQRunInfoSize,
       "hpnicfIfQoSCQRunInfoLength": hpnicfIfQoSCQRunInfoLength,
       "hpnicfIfQoSCQRunInfoDiscardPackets": hpnicfIfQoSCQRunInfoDiscardPackets,
       "hpnicfIfQoSWFQObject": hpnicfIfQoSWFQObject,
       "hpnicfIfQoSWFQConfigGroup": hpnicfIfQoSWFQConfigGroup,
       "hpnicfIfQoSWFQTable": hpnicfIfQoSWFQTable,
       "hpnicfIfQoSWFQEntry": hpnicfIfQoSWFQEntry,
       "hpnicfIfQoSWFQQueueLength": hpnicfIfQoSWFQQueueLength,
       "hpnicfIfQoSWFQQueueNumber": hpnicfIfQoSWFQQueueNumber,
       "hpnicfIfQoSWFQRowStatus": hpnicfIfQoSWFQRowStatus,
       "hpnicfIfQoSWFQType": hpnicfIfQoSWFQType,
       "hpnicfIfQoSWFQRunInfoGroup": hpnicfIfQoSWFQRunInfoGroup,
       "hpnicfIfQoSWFQRunInfoTable": hpnicfIfQoSWFQRunInfoTable,
       "hpnicfIfQoSWFQRunInfoEntry": hpnicfIfQoSWFQRunInfoEntry,
       "hpnicfIfQoSWFQSize": hpnicfIfQoSWFQSize,
       "hpnicfIfQoSWFQLength": hpnicfIfQoSWFQLength,
       "hpnicfIfQoSWFQDiscardPackets": hpnicfIfQoSWFQDiscardPackets,
       "hpnicfIfQoSWFQHashedActiveQueues": hpnicfIfQoSWFQHashedActiveQueues,
       "hpnicfIfQoSWFQHashedMaxActiveQueues": hpnicfIfQoSWFQHashedMaxActiveQueues,
       "hpnicfIfQosWFQhashedTotalQueues": hpnicfIfQosWFQhashedTotalQueues,
       "hpnicfIfQoSBandwidthGroup": hpnicfIfQoSBandwidthGroup,
       "hpnicfIfQoSBandwidthTable": hpnicfIfQoSBandwidthTable,
       "hpnicfIfQoSBandwidthEntry": hpnicfIfQoSBandwidthEntry,
       "hpnicfIfQoSMaxBandwidth": hpnicfIfQoSMaxBandwidth,
       "hpnicfIfQoSReservedBandwidthPct": hpnicfIfQoSReservedBandwidthPct,
       "hpnicfIfQoSBandwidthRowStatus": hpnicfIfQoSBandwidthRowStatus,
       "hpnicfIfQoSQmtokenGroup": hpnicfIfQoSQmtokenGroup,
       "hpnicfIfQoSQmtokenTable": hpnicfIfQoSQmtokenTable,
       "hpnicfIfQoSQmtokenEntry": hpnicfIfQoSQmtokenEntry,
       "hpnicfIfQoSQmtokenNumber": hpnicfIfQoSQmtokenNumber,
       "hpnicfIfQoSQmtokenRosStatus": hpnicfIfQoSQmtokenRosStatus,
       "hpnicfIfQoSRTPQObject": hpnicfIfQoSRTPQObject,
       "hpnicfIfQoSRTPQConfigGroup": hpnicfIfQoSRTPQConfigGroup,
       "hpnicfIfQoSRTPQConfigTable": hpnicfIfQoSRTPQConfigTable,
       "hpnicfIfQoSRTPQConfigEntry": hpnicfIfQoSRTPQConfigEntry,
       "hpnicfIfQoSRTPQStartPort": hpnicfIfQoSRTPQStartPort,
       "hpnicfIfQoSRTPQEndPort": hpnicfIfQoSRTPQEndPort,
       "hpnicfIfQoSRTPQReservedBandwidth": hpnicfIfQoSRTPQReservedBandwidth,
       "hpnicfIfQoSRTPQCbs": hpnicfIfQoSRTPQCbs,
       "hpnicfIfQoSRTPQRowStatus": hpnicfIfQoSRTPQRowStatus,
       "hpnicfIfQoSRTPQRunInfoGroup": hpnicfIfQoSRTPQRunInfoGroup,
       "hpnicfIfQoSRTPQRunInfoTable": hpnicfIfQoSRTPQRunInfoTable,
       "hpnicfIfQoSRTPQRunInfoEntry": hpnicfIfQoSRTPQRunInfoEntry,
       "hpnicfIfQoSRTPQPacketNumber": hpnicfIfQoSRTPQPacketNumber,
       "hpnicfIfQoSRTPQPacketSize": hpnicfIfQoSRTPQPacketSize,
       "hpnicfIfQoSRTPQOutputPackets": hpnicfIfQoSRTPQOutputPackets,
       "hpnicfIfQoSRTPQDiscardPackets": hpnicfIfQoSRTPQDiscardPackets,
       "hpnicfIfQoSCarListObject": hpnicfIfQoSCarListObject,
       "hpnicfIfQoCarListGroup": hpnicfIfQoCarListGroup,
       "hpnicfIfQoSCarlTable": hpnicfIfQoSCarlTable,
       "hpnicfIfQoSCarlEntry": hpnicfIfQoSCarlEntry,
       "hpnicfIfQoSCarlListNum": hpnicfIfQoSCarlListNum,
       "hpnicfIfQoSCarlParaType": hpnicfIfQoSCarlParaType,
       "hpnicfIfQoSCarlParaValue": hpnicfIfQoSCarlParaValue,
       "hpnicfIfQoSCarlRowStatus": hpnicfIfQoSCarlRowStatus,
       "hpnicfIfQoSLineRateObjects": hpnicfIfQoSLineRateObjects,
       "hpnicfIfQoSLRConfigTable": hpnicfIfQoSLRConfigTable,
       "hpnicfIfQoSLRConfigEntry": hpnicfIfQoSLRConfigEntry,
       "hpnicfIfQoSLRDirection": hpnicfIfQoSLRDirection,
       "hpnicfIfQoSLRCir": hpnicfIfQoSLRCir,
       "hpnicfIfQoSLRCbs": hpnicfIfQoSLRCbs,
       "hpnicfIfQoSLREbs": hpnicfIfQoSLREbs,
       "hpnicfIfQoSRowStatus": hpnicfIfQoSRowStatus,
       "hpnicfIfQoSLRPir": hpnicfIfQoSLRPir,
       "hpnicfIfQoSLRUnit": hpnicfIfQoSLRUnit,
       "hpnicfIfQoSLRRunInfoTable": hpnicfIfQoSLRRunInfoTable,
       "hpnicfIfQoSLRRunInfoEntry": hpnicfIfQoSLRRunInfoEntry,
       "hpnicfIfQoSLRRunInfoPassedPackets": hpnicfIfQoSLRRunInfoPassedPackets,
       "hpnicfIfQoSLRRunInfoPassedBytes": hpnicfIfQoSLRRunInfoPassedBytes,
       "hpnicfIfQoSLRRunInfoDelayedPackets": hpnicfIfQoSLRRunInfoDelayedPackets,
       "hpnicfIfQoSLRRunInfoDelayedBytes": hpnicfIfQoSLRRunInfoDelayedBytes,
       "hpnicfIfQoSLRRunInfoActiveShaping": hpnicfIfQoSLRRunInfoActiveShaping,
       "hpnicfIfQoSCARObjects": hpnicfIfQoSCARObjects,
       "hpnicfIfQoSAggregativeCarGroup": hpnicfIfQoSAggregativeCarGroup,
       "hpnicfIfQoSAggregativeCarNextIndex": hpnicfIfQoSAggregativeCarNextIndex,
       "hpnicfIfQoSAggregativeCarConfigTable": hpnicfIfQoSAggregativeCarConfigTable,
       "hpnicfIfQoSAggregativeCarConfigEntry": hpnicfIfQoSAggregativeCarConfigEntry,
       "hpnicfIfQoSAggregativeCarIndex": hpnicfIfQoSAggregativeCarIndex,
       "hpnicfIfQoSAggregativeCarName": hpnicfIfQoSAggregativeCarName,
       "hpnicfIfQoSAggregativeCarCir": hpnicfIfQoSAggregativeCarCir,
       "hpnicfIfQoSAggregativeCarCbs": hpnicfIfQoSAggregativeCarCbs,
       "hpnicfIfQoSAggregativeCarEbs": hpnicfIfQoSAggregativeCarEbs,
       "hpnicfIfQoSAggregativeCarPir": hpnicfIfQoSAggregativeCarPir,
       "hpnicfIfQoSAggregativeCarGreenActionType": hpnicfIfQoSAggregativeCarGreenActionType,
       "hpnicfIfQoSAggregativeCarGreenActionValue": hpnicfIfQoSAggregativeCarGreenActionValue,
       "hpnicfIfQoSAggregativeCarYellowActionType": hpnicfIfQoSAggregativeCarYellowActionType,
       "hpnicfIfQoSAggregativeCarYellowActionValue": hpnicfIfQoSAggregativeCarYellowActionValue,
       "hpnicfIfQoSAggregativeCarRedActionType": hpnicfIfQoSAggregativeCarRedActionType,
       "hpnicfIfQoSAggregativeCarRedActionValue": hpnicfIfQoSAggregativeCarRedActionValue,
       "hpnicfIfQoSAggregativeCarType": hpnicfIfQoSAggregativeCarType,
       "hpnicfIfQoSAggregativeCarRowStatus": hpnicfIfQoSAggregativeCarRowStatus,
       "hpnicfIfQoSAggregativeCarApplyTable": hpnicfIfQoSAggregativeCarApplyTable,
       "hpnicfIfQoSAggregativeCarApplyEntry": hpnicfIfQoSAggregativeCarApplyEntry,
       "hpnicfIfQoSAggregativeCarApplyDirection": hpnicfIfQoSAggregativeCarApplyDirection,
       "hpnicfIfQoSAggregativeCarApplyRuleType": hpnicfIfQoSAggregativeCarApplyRuleType,
       "hpnicfIfQoSAggregativeCarApplyRuleValue": hpnicfIfQoSAggregativeCarApplyRuleValue,
       "hpnicfIfQoSAggregativeCarApplyCarIndex": hpnicfIfQoSAggregativeCarApplyCarIndex,
       "hpnicfIfQoSAggregativeCarApplyRowStatus": hpnicfIfQoSAggregativeCarApplyRowStatus,
       "hpnicfIfQoSAggregativeCarRunInfoTable": hpnicfIfQoSAggregativeCarRunInfoTable,
       "hpnicfIfQoSAggregativeCarRunInfoEntry": hpnicfIfQoSAggregativeCarRunInfoEntry,
       "hpnicfIfQoSAggregativeCarGreenPackets": hpnicfIfQoSAggregativeCarGreenPackets,
       "hpnicfIfQoSAggregativeCarGreenBytes": hpnicfIfQoSAggregativeCarGreenBytes,
       "hpnicfIfQoSAggregativeCarYellowPackets": hpnicfIfQoSAggregativeCarYellowPackets,
       "hpnicfIfQoSAggregativeCarYellowBytes": hpnicfIfQoSAggregativeCarYellowBytes,
       "hpnicfIfQoSAggregativeCarRedPackets": hpnicfIfQoSAggregativeCarRedPackets,
       "hpnicfIfQoSAggregativeCarRedBytes": hpnicfIfQoSAggregativeCarRedBytes,
       "hpnicfIfQoSTricolorCarGroup": hpnicfIfQoSTricolorCarGroup,
       "hpnicfIfQoSTricolorCarConfigTable": hpnicfIfQoSTricolorCarConfigTable,
       "hpnicfIfQoSTricolorCarConfigEntry": hpnicfIfQoSTricolorCarConfigEntry,
       "hpnicfIfQoSTricolorCarDirection": hpnicfIfQoSTricolorCarDirection,
       "hpnicfIfQoSTricolorCarType": hpnicfIfQoSTricolorCarType,
       "hpnicfIfQoSTricolorCarValue": hpnicfIfQoSTricolorCarValue,
       "hpnicfIfQoSTricolorCarCir": hpnicfIfQoSTricolorCarCir,
       "hpnicfIfQoSTricolorCarCbs": hpnicfIfQoSTricolorCarCbs,
       "hpnicfIfQoSTricolorCarEbs": hpnicfIfQoSTricolorCarEbs,
       "hpnicfIfQoSTricolorCarPir": hpnicfIfQoSTricolorCarPir,
       "hpnicfIfQoSTricolorCarGreenActionType": hpnicfIfQoSTricolorCarGreenActionType,
       "hpnicfIfQoSTricolorCarGreenActionValue": hpnicfIfQoSTricolorCarGreenActionValue,
       "hpnicfIfQoSTricolorCarYellowActionType": hpnicfIfQoSTricolorCarYellowActionType,
       "hpnicfIfQoSTricolorCarYellowActionValue": hpnicfIfQoSTricolorCarYellowActionValue,
       "hpnicfIfQoSTricolorCarRedActionType": hpnicfIfQoSTricolorCarRedActionType,
       "hpnicfIfQoSTricolorCarRedActionValue": hpnicfIfQoSTricolorCarRedActionValue,
       "hpnicfIfQoSTricolorCarRowStatus": hpnicfIfQoSTricolorCarRowStatus,
       "hpnicfIfQoSTricolorCarRunInfoTable": hpnicfIfQoSTricolorCarRunInfoTable,
       "hpnicfIfQoSTricolorCarRunInfoEntry": hpnicfIfQoSTricolorCarRunInfoEntry,
       "hpnicfIfQoSTricolorCarGreenPackets": hpnicfIfQoSTricolorCarGreenPackets,
       "hpnicfIfQoSTricolorCarGreenBytes": hpnicfIfQoSTricolorCarGreenBytes,
       "hpnicfIfQoSTricolorCarYellowPackets": hpnicfIfQoSTricolorCarYellowPackets,
       "hpnicfIfQoSTricolorCarYellowBytes": hpnicfIfQoSTricolorCarYellowBytes,
       "hpnicfIfQoSTricolorCarRedPackets": hpnicfIfQoSTricolorCarRedPackets,
       "hpnicfIfQoSTricolorCarRedBytes": hpnicfIfQoSTricolorCarRedBytes,
       "hpnicfIfQoSGTSObjects": hpnicfIfQoSGTSObjects,
       "hpnicfIfQoSGTSConfigTable": hpnicfIfQoSGTSConfigTable,
       "hpnicfIfQoSGTSConfigEntry": hpnicfIfQoSGTSConfigEntry,
       "hpnicfIfQoSGTSClassRuleType": hpnicfIfQoSGTSClassRuleType,
       "hpnicfIfQoSGTSClassRuleValue": hpnicfIfQoSGTSClassRuleValue,
       "hpnicfIfQoSGTSCir": hpnicfIfQoSGTSCir,
       "hpnicfIfQoSGTSCbs": hpnicfIfQoSGTSCbs,
       "hpnicfIfQoSGTSEbs": hpnicfIfQoSGTSEbs,
       "hpnicfIfQoSGTSQueueLength": hpnicfIfQoSGTSQueueLength,
       "hpnicfIfQoSGTSConfigRowStatus": hpnicfIfQoSGTSConfigRowStatus,
       "hpnicfIfQoSGTSRunInfoTable": hpnicfIfQoSGTSRunInfoTable,
       "hpnicfIfQoSGTSRunInfoEntry": hpnicfIfQoSGTSRunInfoEntry,
       "hpnicfIfQoSGTSQueueSize": hpnicfIfQoSGTSQueueSize,
       "hpnicfIfQoSGTSPassedPackets": hpnicfIfQoSGTSPassedPackets,
       "hpnicfIfQoSGTSPassedBytes": hpnicfIfQoSGTSPassedBytes,
       "hpnicfIfQoSGTSDiscardPackets": hpnicfIfQoSGTSDiscardPackets,
       "hpnicfIfQoSGTSDiscardBytes": hpnicfIfQoSGTSDiscardBytes,
       "hpnicfIfQoSGTSDelayedPackets": hpnicfIfQoSGTSDelayedPackets,
       "hpnicfIfQoSGTSDelayedBytes": hpnicfIfQoSGTSDelayedBytes,
       "hpnicfIfQoSWREDObjects": hpnicfIfQoSWREDObjects,
       "hpnicfIfQoSWredGroupGroup": hpnicfIfQoSWredGroupGroup,
       "hpnicfIfQoSWredGroupNextIndex": hpnicfIfQoSWredGroupNextIndex,
       "hpnicfIfQoSWredGroupTable": hpnicfIfQoSWredGroupTable,
       "hpnicfIfQoSWredGroupEntry": hpnicfIfQoSWredGroupEntry,
       "hpnicfIfQoSWredGroupIndex": hpnicfIfQoSWredGroupIndex,
       "hpnicfIfQoSWredGroupName": hpnicfIfQoSWredGroupName,
       "hpnicfIfQoSWredGroupType": hpnicfIfQoSWredGroupType,
       "hpnicfIfQoSWredGroupWeightingConstant": hpnicfIfQoSWredGroupWeightingConstant,
       "hpnicfIfQoSWredGroupRowStatus": hpnicfIfQoSWredGroupRowStatus,
       "hpnicfIfQoSWredGroupContentTable": hpnicfIfQoSWredGroupContentTable,
       "hpnicfIfQoSWredGroupContentEntry": hpnicfIfQoSWredGroupContentEntry,
       "hpnicfIfQoSWredGroupContentIndex": hpnicfIfQoSWredGroupContentIndex,
       "hpnicfIfQoSWredGroupContentSubIndex": hpnicfIfQoSWredGroupContentSubIndex,
       "hpnicfIfQoSWredLowLimit": hpnicfIfQoSWredLowLimit,
       "hpnicfIfQoSWredHighLimit": hpnicfIfQoSWredHighLimit,
       "hpnicfIfQoSWredDiscardProb": hpnicfIfQoSWredDiscardProb,
       "hpnicfIfQoSWredGroupExponent": hpnicfIfQoSWredGroupExponent,
       "hpnicfIfQoSWredRowStatus": hpnicfIfQoSWredRowStatus,
       "hpnicfIfQoSWredGroupApplyIfTable": hpnicfIfQoSWredGroupApplyIfTable,
       "hpnicfIfQoSWredGroupApplyIfEntry": hpnicfIfQoSWredGroupApplyIfEntry,
       "hpnicfIfQoSWredGroupApplyIndex": hpnicfIfQoSWredGroupApplyIndex,
       "hpnicfIfQoSWredGroupApplyName": hpnicfIfQoSWredGroupApplyName,
       "hpnicfIfQoSWredGroupIfRowStatus": hpnicfIfQoSWredGroupIfRowStatus,
       "hpnicfIfQoSWredApplyIfRunInfoTable": hpnicfIfQoSWredApplyIfRunInfoTable,
       "hpnicfIfQoSWredApplyIfRunInfoEntry": hpnicfIfQoSWredApplyIfRunInfoEntry,
       "hpnicfIfQoSWredPreRandomDropNum": hpnicfIfQoSWredPreRandomDropNum,
       "hpnicfIfQoSWredPreTailDropNum": hpnicfIfQoSWredPreTailDropNum,
       "hpnicfIfQoSPortWredGroup": hpnicfIfQoSPortWredGroup,
       "hpnicfIfQoSPortWredWeightConstantTable": hpnicfIfQoSPortWredWeightConstantTable,
       "hpnicfIfQoSPortWredWeightConstantEntry": hpnicfIfQoSPortWredWeightConstantEntry,
       "hpnicfIfQoSPortWredEnable": hpnicfIfQoSPortWredEnable,
       "hpnicfIfQoSPortWredWeightConstant": hpnicfIfQoSPortWredWeightConstant,
       "hpnicfIfQoSPortWredWeightConstantRowStatus": hpnicfIfQoSPortWredWeightConstantRowStatus,
       "hpnicfIfQoSPortWredPreConfigTable": hpnicfIfQoSPortWredPreConfigTable,
       "hpnicfIfQoSPortWredPreConfigEntry": hpnicfIfQoSPortWredPreConfigEntry,
       "hpnicfIfQoSPortWredPreID": hpnicfIfQoSPortWredPreID,
       "hpnicfIfQoSPortWredPreLowLimit": hpnicfIfQoSPortWredPreLowLimit,
       "hpnicfIfQoSPortWredPreHighLimit": hpnicfIfQoSPortWredPreHighLimit,
       "hpnicfIfQoSPortWredPreDiscardProbability": hpnicfIfQoSPortWredPreDiscardProbability,
       "hpnicfIfQoSPortWredPreRowStatus": hpnicfIfQoSPortWredPreRowStatus,
       "hpnicfIfQoSPortWredRunInfoTable": hpnicfIfQoSPortWredRunInfoTable,
       "hpnicfIfQoSPortWredRunInfoEntry": hpnicfIfQoSPortWredRunInfoEntry,
       "hpnicfIfQoSWREDTailDropNum": hpnicfIfQoSWREDTailDropNum,
       "hpnicfIfQoSWREDRandomDropNum": hpnicfIfQoSWREDRandomDropNum,
       "hpnicfIfQoSPortPriorityObjects": hpnicfIfQoSPortPriorityObjects,
       "hpnicfIfQoSPortPriorityConfigGroup": hpnicfIfQoSPortPriorityConfigGroup,
       "hpnicfIfQoSPortPriorityTable": hpnicfIfQoSPortPriorityTable,
       "hpnicfIfQoSPortPriorityEntry": hpnicfIfQoSPortPriorityEntry,
       "hpnicfIfQoSPortPriorityValue": hpnicfIfQoSPortPriorityValue,
       "hpnicfIfQoSPortPirorityTrustTable": hpnicfIfQoSPortPirorityTrustTable,
       "hpnicfIfQoSPortPirorityTrustEntry": hpnicfIfQoSPortPirorityTrustEntry,
       "hpnicfIfQoSPortPriorityTrustTrustType": hpnicfIfQoSPortPriorityTrustTrustType,
       "hpnicfIfQoSPortPriorityTrustOvercastType": hpnicfIfQoSPortPriorityTrustOvercastType,
       "hpnicfIfQoSMapObjects": hpnicfIfQoSMapObjects,
       "hpnicfIfQoSPriMapConfigGroup": hpnicfIfQoSPriMapConfigGroup,
       "hpnicfIfQoSPriMapGroupNextIndex": hpnicfIfQoSPriMapGroupNextIndex,
       "hpnicfIfQoSPriMapGroupTable": hpnicfIfQoSPriMapGroupTable,
       "hpnicfIfQoSPriMapGroupEntry": hpnicfIfQoSPriMapGroupEntry,
       "hpnicfIfQoSPriMapGroupIndex": hpnicfIfQoSPriMapGroupIndex,
       "hpnicfIfQoSPriMapGroupType": hpnicfIfQoSPriMapGroupType,
       "hpnicfIfQoSPriMapGroupName": hpnicfIfQoSPriMapGroupName,
       "hpnicfIfQoSPriMapGroupRowStatus": hpnicfIfQoSPriMapGroupRowStatus,
       "hpnicfIfQoSPriMapContentTable": hpnicfIfQoSPriMapContentTable,
       "hpnicfIfQoSPriMapContentEntry": hpnicfIfQoSPriMapContentEntry,
       "hpnicfIfQoSPriMapGroupImportValue": hpnicfIfQoSPriMapGroupImportValue,
       "hpnicfIfQoSPriMapGroupExportValue": hpnicfIfQoSPriMapGroupExportValue,
       "hpnicfIfQoSPriMapContentRowStatus": hpnicfIfQoSPriMapContentRowStatus,
       "hpnicfIfQoSPrePriMapTable": hpnicfIfQoSPrePriMapTable,
       "hpnicfIfQoSPrePriMapEntry": hpnicfIfQoSPrePriMapEntry,
       "hpnicfIfQoSPrePriMapTableType": hpnicfIfQoSPrePriMapTableType,
       "hpnicfIfQoSPrePriMapTableColor": hpnicfIfQoSPrePriMapTableColor,
       "hpnicfIfQoSPrePriMapTableDirection": hpnicfIfQoSPrePriMapTableDirection,
       "hpnicfIfQoSPrePriMapTableImportValue": hpnicfIfQoSPrePriMapTableImportValue,
       "hpnicfIfQoSPrePriMapTableExportValue": hpnicfIfQoSPrePriMapTableExportValue,
       "hpnicfIfQoSL3PlusObjects": hpnicfIfQoSL3PlusObjects,
       "hpnicfIfQoSPortBindingGroup": hpnicfIfQoSPortBindingGroup,
       "hpnicfIfQoSPortBindingTable": hpnicfIfQoSPortBindingTable,
       "hpnicfIfQoSPortBindingEntry": hpnicfIfQoSPortBindingEntry,
       "hpnicfIfQoSBindingIf": hpnicfIfQoSBindingIf,
       "hpnicfIfQoSBindingRowStatus": hpnicfIfQoSBindingRowStatus,
       "hpnicfQoSTraStaObjects": hpnicfQoSTraStaObjects,
       "hpnicfQoSTraStaConfigGroup": hpnicfQoSTraStaConfigGroup,
       "hpnicfQoSIfTraStaConfigInfoTable": hpnicfQoSIfTraStaConfigInfoTable,
       "hpnicfQoSIfTraStaConfigInfoEntry": hpnicfQoSIfTraStaConfigInfoEntry,
       "hpnicfQoSIfTraStaConfigDirection": hpnicfQoSIfTraStaConfigDirection,
       "hpnicfQoSIfTraStaConfigQueue": hpnicfQoSIfTraStaConfigQueue,
       "hpnicfQoSIfTraStaConfigDot1p": hpnicfQoSIfTraStaConfigDot1p,
       "hpnicfQoSIfTraStaConfigDscp": hpnicfQoSIfTraStaConfigDscp,
       "hpnicfQoSIfTraStaConfigVlan": hpnicfQoSIfTraStaConfigVlan,
       "hpnicfQoSIfTraStaConfigStatus": hpnicfQoSIfTraStaConfigStatus,
       "hpnicfQoSTraStaRunGroup": hpnicfQoSTraStaRunGroup,
       "hpnicfQoSIfTraStaRunInfoTable": hpnicfQoSIfTraStaRunInfoTable,
       "hpnicfQoSIfTraStaRunInfoEntry": hpnicfQoSIfTraStaRunInfoEntry,
       "hpnicfQoSIfTraStaRunObjectType": hpnicfQoSIfTraStaRunObjectType,
       "hpnicfQoSIfTraStaRunObjectValue": hpnicfQoSIfTraStaRunObjectValue,
       "hpnicfQoSIfTraStaRunDirection": hpnicfQoSIfTraStaRunDirection,
       "hpnicfQoSIfTraStaRunPassPackets": hpnicfQoSIfTraStaRunPassPackets,
       "hpnicfQoSIfTraStaRunDropPackets": hpnicfQoSIfTraStaRunDropPackets,
       "hpnicfQoSIfTraStaRunPassBytes": hpnicfQoSIfTraStaRunPassBytes,
       "hpnicfQoSIfTraStaRunDropBytes": hpnicfQoSIfTraStaRunDropBytes,
       "hpnicfQoSIfTraStaRunPassPPS": hpnicfQoSIfTraStaRunPassPPS,
       "hpnicfQoSIfTraStaRunPassBPS": hpnicfQoSIfTraStaRunPassBPS,
       "hpnicfQoSGlobalPriorityObject": hpnicfQoSGlobalPriorityObject,
       "hpnicfQoSRemarkTcpPortPriTable": hpnicfQoSRemarkTcpPortPriTable,
       "hpnicfQoSRemarkTcpPortPriEntry": hpnicfQoSRemarkTcpPortPriEntry,
       "hpnicfQoSRemarkTcpPortStart": hpnicfQoSRemarkTcpPortStart,
       "hpnicfQoSRemarkTcpPortEnd": hpnicfQoSRemarkTcpPortEnd,
       "hpnicfQoSRemarkTcpPortType": hpnicfQoSRemarkTcpPortType,
       "hpnicfQoSRemarkTcpPortDot1p": hpnicfQoSRemarkTcpPortDot1p,
       "hpnicfQoSRemarkTcpPortDscp": hpnicfQoSRemarkTcpPortDscp,
       "hpnicfQoSRemarkTcpPortRowStatus": hpnicfQoSRemarkTcpPortRowStatus,
       "hpnicfQoSRemarkUdpPortPriTable": hpnicfQoSRemarkUdpPortPriTable,
       "hpnicfQoSRemarkUdpPortPriEntry": hpnicfQoSRemarkUdpPortPriEntry,
       "hpnicfQoSRemarkUdpPortStart": hpnicfQoSRemarkUdpPortStart,
       "hpnicfQoSRemarkUdpPortEnd": hpnicfQoSRemarkUdpPortEnd,
       "hpnicfQoSRemarkUdpPortType": hpnicfQoSRemarkUdpPortType,
       "hpnicfQoSRemarkUdpPortDot1p": hpnicfQoSRemarkUdpPortDot1p,
       "hpnicfQoSRemarkUdpPortDscp": hpnicfQoSRemarkUdpPortDscp,
       "hpnicfQoSRemarkUdpPortRowStatus": hpnicfQoSRemarkUdpPortRowStatus,
       "hpnicfQoSRemarkIPv4AddrPriTable": hpnicfQoSRemarkIPv4AddrPriTable,
       "hpnicfQoSRemarkIPv4AddrPriEntry": hpnicfQoSRemarkIPv4AddrPriEntry,
       "hpnicfQoSRemarkIPv4AddrValue": hpnicfQoSRemarkIPv4AddrValue,
       "hpnicfQoSRemarkIPv4AddrMask": hpnicfQoSRemarkIPv4AddrMask,
       "hpnicfQoSRemarkIPv4AddrMaskLength": hpnicfQoSRemarkIPv4AddrMaskLength,
       "hpnicfQoSRemarkIPv4AddrDot1p": hpnicfQoSRemarkIPv4AddrDot1p,
       "hpnicfQoSRemarkIPv4AddrDscp": hpnicfQoSRemarkIPv4AddrDscp,
       "hpnicfQoSRemarkIPv4AddrRowStatus": hpnicfQoSRemarkIPv4AddrRowStatus,
       "hpnicfQoSRemarkIPv6AddrPriTable": hpnicfQoSRemarkIPv6AddrPriTable,
       "hpnicfQoSRemarkIPv6AddrPriEntry": hpnicfQoSRemarkIPv6AddrPriEntry,
       "hpnicfQoSRemarkIPv6AddrValue": hpnicfQoSRemarkIPv6AddrValue,
       "hpnicfQoSRemarkIPv6AddrPrefixLength": hpnicfQoSRemarkIPv6AddrPrefixLength,
       "hpnicfQoSRemarkIPv6AddrDot1p": hpnicfQoSRemarkIPv6AddrDot1p,
       "hpnicfQoSRemarkIPv6AddrDscp": hpnicfQoSRemarkIPv6AddrDscp,
       "hpnicfQoSRemarkIPv6AddrRowStatus": hpnicfQoSRemarkIPv6AddrRowStatus,
       "hpnicfQoSRemarkProtocolPriTable": hpnicfQoSRemarkProtocolPriTable,
       "hpnicfQoSRemarkProtocolPriEntry": hpnicfQoSRemarkProtocolPriEntry,
       "hpnicfQoSRemarkProtocolValue": hpnicfQoSRemarkProtocolValue,
       "hpnicfQoSRemarkProtocolDot1p": hpnicfQoSRemarkProtocolDot1p,
       "hpnicfQoSRemarkProtocolRowStatus": hpnicfQoSRemarkProtocolRowStatus,
       "hpnicfQoSRemarkVlanPriTable": hpnicfQoSRemarkVlanPriTable,
       "hpnicfQoSRemarkVlanPriEntry": hpnicfQoSRemarkVlanPriEntry,
       "hpnicfQoSRemarkVlanStart": hpnicfQoSRemarkVlanStart,
       "hpnicfQoSRemarkVlanEnd": hpnicfQoSRemarkVlanEnd,
       "hpnicfQoSRemarkVlanDot1p": hpnicfQoSRemarkVlanDot1p,
       "hpnicfQoSRemarkVlanDscp": hpnicfQoSRemarkVlanDscp,
       "hpnicfQoSRemarkVlanRowStatus": hpnicfQoSRemarkVlanRowStatus,
       "hpnicfQoSTypeOfServiceObjects": hpnicfQoSTypeOfServiceObjects,
       "hpnicfQoSTypeOfServiceMode": hpnicfQoSTypeOfServiceMode}
)
