# SNMP MIB module (HH3C-IFQOS2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-IFQOS2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:32 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cIfQos2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1)
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

_Hh3cQos2_ObjectIdentity = ObjectIdentity
hh3cQos2 = _Hh3cQos2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65)
)
_Hh3cIfQoSHardwareQueueObjects_ObjectIdentity = ObjectIdentity
hh3cIfQoSHardwareQueueObjects = _Hh3cIfQoSHardwareQueueObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1)
)
_Hh3cIfQoSHardwareQueueConfigGroup_ObjectIdentity = ObjectIdentity
hh3cIfQoSHardwareQueueConfigGroup = _Hh3cIfQoSHardwareQueueConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 1)
)
_Hh3cIfQoSQSModeTable_Object = MibTable
hh3cIfQoSQSModeTable = _Hh3cIfQoSQSModeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cIfQoSQSModeTable.setStatus("current")
_Hh3cIfQoSQSModeEntry_Object = MibTableRow
hh3cIfQoSQSModeEntry = _Hh3cIfQoSQSModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 1, 1, 1)
)
hh3cIfQoSQSModeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSQSModeEntry.setStatus("current")


class _Hh3cIfQoSQSMode_Type(Integer32):
    """Custom type hh3cIfQoSQSMode based on Integer32"""
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
        *(("hh3cfq", 6),
          ("sp", 1),
          ("sp0", 2),
          ("sp1", 3),
          ("sp2", 4),
          ("wrr", 5),
          ("wrr-sp", 7))
    )


_Hh3cIfQoSQSMode_Type.__name__ = "Integer32"
_Hh3cIfQoSQSMode_Object = MibTableColumn
hh3cIfQoSQSMode = _Hh3cIfQoSQSMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 1, 1, 1, 1),
    _Hh3cIfQoSQSMode_Type()
)
hh3cIfQoSQSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfQoSQSMode.setStatus("current")
_Hh3cIfQoSQSWeightTable_Object = MibTable
hh3cIfQoSQSWeightTable = _Hh3cIfQoSQSWeightTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cIfQoSQSWeightTable.setStatus("current")
_Hh3cIfQoSQSWeightEntry_Object = MibTableRow
hh3cIfQoSQSWeightEntry = _Hh3cIfQoSQSWeightEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 1, 2, 1)
)
hh3cIfQoSQSWeightEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSQueueID"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSQSWeightEntry.setStatus("current")
_Hh3cIfQoSQueueID_Type = Integer32
_Hh3cIfQoSQueueID_Object = MibTableColumn
hh3cIfQoSQueueID = _Hh3cIfQoSQueueID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 1, 2, 1, 1),
    _Hh3cIfQoSQueueID_Type()
)
hh3cIfQoSQueueID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfQoSQueueID.setStatus("current")


class _Hh3cIfQoSQueueGroupType_Type(Integer32):
    """Custom type hh3cIfQoSQueueGroupType based on Integer32"""
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


_Hh3cIfQoSQueueGroupType_Type.__name__ = "Integer32"
_Hh3cIfQoSQueueGroupType_Object = MibTableColumn
hh3cIfQoSQueueGroupType = _Hh3cIfQoSQueueGroupType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 1, 2, 1, 2),
    _Hh3cIfQoSQueueGroupType_Type()
)
hh3cIfQoSQueueGroupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfQoSQueueGroupType.setStatus("current")


class _Hh3cIfQoSQSType_Type(Integer32):
    """Custom type hh3cIfQoSQSType based on Integer32"""
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


_Hh3cIfQoSQSType_Type.__name__ = "Integer32"
_Hh3cIfQoSQSType_Object = MibTableColumn
hh3cIfQoSQSType = _Hh3cIfQoSQSType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 1, 2, 1, 3),
    _Hh3cIfQoSQSType_Type()
)
hh3cIfQoSQSType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfQoSQSType.setStatus("current")
_Hh3cIfQoSQSValue_Type = Integer32
_Hh3cIfQoSQSValue_Object = MibTableColumn
hh3cIfQoSQSValue = _Hh3cIfQoSQSValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 1, 2, 1, 4),
    _Hh3cIfQoSQSValue_Type()
)
hh3cIfQoSQSValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfQoSQSValue.setStatus("current")


class _Hh3cIfQoSQSMaxDelay_Type(Integer32):
    """Custom type hh3cIfQoSQSMaxDelay based on Integer32"""
    defaultValue = 9


_Hh3cIfQoSQSMaxDelay_Object = MibTableColumn
hh3cIfQoSQSMaxDelay = _Hh3cIfQoSQSMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 1, 2, 1, 5),
    _Hh3cIfQoSQSMaxDelay_Type()
)
hh3cIfQoSQSMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfQoSQSMaxDelay.setStatus("current")
_Hh3cIfQoSHardwareQueueRunInfoGroup_ObjectIdentity = ObjectIdentity
hh3cIfQoSHardwareQueueRunInfoGroup = _Hh3cIfQoSHardwareQueueRunInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2)
)
_Hh3cIfQoSHardwareQueueRunInfoTable_Object = MibTable
hh3cIfQoSHardwareQueueRunInfoTable = _Hh3cIfQoSHardwareQueueRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cIfQoSHardwareQueueRunInfoTable.setStatus("current")
_Hh3cIfQoSHardwareQueueRunInfoEntry_Object = MibTableRow
hh3cIfQoSHardwareQueueRunInfoEntry = _Hh3cIfQoSHardwareQueueRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 1, 1)
)
hh3cIfQoSHardwareQueueRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSQueueID"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSHardwareQueueRunInfoEntry.setStatus("current")
_Hh3cIfQoSPassPackets_Type = Counter64
_Hh3cIfQoSPassPackets_Object = MibTableColumn
hh3cIfQoSPassPackets = _Hh3cIfQoSPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 1, 1, 1),
    _Hh3cIfQoSPassPackets_Type()
)
hh3cIfQoSPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSPassPackets.setStatus("current")
_Hh3cIfQoSDropPackets_Type = Counter64
_Hh3cIfQoSDropPackets_Object = MibTableColumn
hh3cIfQoSDropPackets = _Hh3cIfQoSDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 1, 1, 2),
    _Hh3cIfQoSDropPackets_Type()
)
hh3cIfQoSDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSDropPackets.setStatus("current")
_Hh3cIfQoSPassBytes_Type = Counter64
_Hh3cIfQoSPassBytes_Object = MibTableColumn
hh3cIfQoSPassBytes = _Hh3cIfQoSPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 1, 1, 3),
    _Hh3cIfQoSPassBytes_Type()
)
hh3cIfQoSPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSPassBytes.setStatus("current")
_Hh3cIfQoSPassPPS_Type = Unsigned32
_Hh3cIfQoSPassPPS_Object = MibTableColumn
hh3cIfQoSPassPPS = _Hh3cIfQoSPassPPS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 1, 1, 4),
    _Hh3cIfQoSPassPPS_Type()
)
hh3cIfQoSPassPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSPassPPS.setStatus("current")
_Hh3cIfQoSPassBPS_Type = Unsigned32
_Hh3cIfQoSPassBPS_Object = MibTableColumn
hh3cIfQoSPassBPS = _Hh3cIfQoSPassBPS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 1, 1, 5),
    _Hh3cIfQoSPassBPS_Type()
)
hh3cIfQoSPassBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSPassBPS.setStatus("current")
_Hh3cIfQoSDropBytes_Type = Counter64
_Hh3cIfQoSDropBytes_Object = MibTableColumn
hh3cIfQoSDropBytes = _Hh3cIfQoSDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 1, 1, 6),
    _Hh3cIfQoSDropBytes_Type()
)
hh3cIfQoSDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSDropBytes.setStatus("current")
_Hh3cIfQoSQueueLengthInPkts_Type = Unsigned32
_Hh3cIfQoSQueueLengthInPkts_Object = MibTableColumn
hh3cIfQoSQueueLengthInPkts = _Hh3cIfQoSQueueLengthInPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 1, 1, 7),
    _Hh3cIfQoSQueueLengthInPkts_Type()
)
hh3cIfQoSQueueLengthInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSQueueLengthInPkts.setStatus("current")
_Hh3cIfQoSQueueLengthInBytes_Type = Unsigned32
_Hh3cIfQoSQueueLengthInBytes_Object = MibTableColumn
hh3cIfQoSQueueLengthInBytes = _Hh3cIfQoSQueueLengthInBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 1, 1, 8),
    _Hh3cIfQoSQueueLengthInBytes_Type()
)
hh3cIfQoSQueueLengthInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSQueueLengthInBytes.setStatus("current")
_Hh3cIfQoSCurQueuePkts_Type = Unsigned32
_Hh3cIfQoSCurQueuePkts_Object = MibTableColumn
hh3cIfQoSCurQueuePkts = _Hh3cIfQoSCurQueuePkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 1, 1, 9),
    _Hh3cIfQoSCurQueuePkts_Type()
)
hh3cIfQoSCurQueuePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSCurQueuePkts.setStatus("current")
_Hh3cIfQoSCurQueueBytes_Type = Unsigned32
_Hh3cIfQoSCurQueueBytes_Object = MibTableColumn
hh3cIfQoSCurQueueBytes = _Hh3cIfQoSCurQueueBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 1, 1, 10),
    _Hh3cIfQoSCurQueueBytes_Type()
)
hh3cIfQoSCurQueueBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSCurQueueBytes.setStatus("current")
_Hh3cIfQoSCurQueuePPS_Type = Unsigned32
_Hh3cIfQoSCurQueuePPS_Object = MibTableColumn
hh3cIfQoSCurQueuePPS = _Hh3cIfQoSCurQueuePPS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 1, 1, 11),
    _Hh3cIfQoSCurQueuePPS_Type()
)
hh3cIfQoSCurQueuePPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSCurQueuePPS.setStatus("current")
_Hh3cIfQoSCurQueueBPS_Type = Unsigned32
_Hh3cIfQoSCurQueueBPS_Object = MibTableColumn
hh3cIfQoSCurQueueBPS = _Hh3cIfQoSCurQueueBPS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 1, 1, 12),
    _Hh3cIfQoSCurQueueBPS_Type()
)
hh3cIfQoSCurQueueBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSCurQueueBPS.setStatus("current")
_Hh3cIfQoSTailDropPkts_Type = Counter64
_Hh3cIfQoSTailDropPkts_Object = MibTableColumn
hh3cIfQoSTailDropPkts = _Hh3cIfQoSTailDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 1, 1, 13),
    _Hh3cIfQoSTailDropPkts_Type()
)
hh3cIfQoSTailDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSTailDropPkts.setStatus("current")
_Hh3cIfQoSTailDropBytes_Type = Counter64
_Hh3cIfQoSTailDropBytes_Object = MibTableColumn
hh3cIfQoSTailDropBytes = _Hh3cIfQoSTailDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 1, 1, 14),
    _Hh3cIfQoSTailDropBytes_Type()
)
hh3cIfQoSTailDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSTailDropBytes.setStatus("current")
_Hh3cIfQoSTailDropPPS_Type = Unsigned32
_Hh3cIfQoSTailDropPPS_Object = MibTableColumn
hh3cIfQoSTailDropPPS = _Hh3cIfQoSTailDropPPS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 1, 1, 15),
    _Hh3cIfQoSTailDropPPS_Type()
)
hh3cIfQoSTailDropPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSTailDropPPS.setStatus("current")
_Hh3cIfQoSTailDropBPS_Type = Unsigned32
_Hh3cIfQoSTailDropBPS_Object = MibTableColumn
hh3cIfQoSTailDropBPS = _Hh3cIfQoSTailDropBPS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 1, 1, 16),
    _Hh3cIfQoSTailDropBPS_Type()
)
hh3cIfQoSTailDropBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSTailDropBPS.setStatus("current")
_Hh3cIfQoSWredDropPkts_Type = Counter64
_Hh3cIfQoSWredDropPkts_Object = MibTableColumn
hh3cIfQoSWredDropPkts = _Hh3cIfQoSWredDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 1, 1, 17),
    _Hh3cIfQoSWredDropPkts_Type()
)
hh3cIfQoSWredDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWredDropPkts.setStatus("current")
_Hh3cIfQoSWredDropBytes_Type = Counter64
_Hh3cIfQoSWredDropBytes_Object = MibTableColumn
hh3cIfQoSWredDropBytes = _Hh3cIfQoSWredDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 1, 1, 18),
    _Hh3cIfQoSWredDropBytes_Type()
)
hh3cIfQoSWredDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWredDropBytes.setStatus("current")
_Hh3cIfQoSWredDropPPS_Type = Unsigned32
_Hh3cIfQoSWredDropPPS_Object = MibTableColumn
hh3cIfQoSWredDropPPS = _Hh3cIfQoSWredDropPPS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 1, 1, 19),
    _Hh3cIfQoSWredDropPPS_Type()
)
hh3cIfQoSWredDropPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWredDropPPS.setStatus("current")
_Hh3cIfQoSWredDropBPS_Type = Unsigned32
_Hh3cIfQoSWredDropBPS_Object = MibTableColumn
hh3cIfQoSWredDropBPS = _Hh3cIfQoSWredDropBPS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 1, 1, 20),
    _Hh3cIfQoSWredDropBPS_Type()
)
hh3cIfQoSWredDropBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWredDropBPS.setStatus("current")
_Hh3cIfQoSHQueueTcpRunInfoTable_Object = MibTable
hh3cIfQoSHQueueTcpRunInfoTable = _Hh3cIfQoSHQueueTcpRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cIfQoSHQueueTcpRunInfoTable.setStatus("current")
_Hh3cIfQoSHQueueTcpRunInfoEntry_Object = MibTableRow
hh3cIfQoSHQueueTcpRunInfoEntry = _Hh3cIfQoSHQueueTcpRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 2, 1)
)
hh3cIfQoSHQueueTcpRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSQueueID"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSHQueueTcpRunInfoEntry.setStatus("current")
_Hh3cIfQoSWredDropLPreNTcpPkts_Type = Counter64
_Hh3cIfQoSWredDropLPreNTcpPkts_Object = MibTableColumn
hh3cIfQoSWredDropLPreNTcpPkts = _Hh3cIfQoSWredDropLPreNTcpPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 2, 1, 1),
    _Hh3cIfQoSWredDropLPreNTcpPkts_Type()
)
hh3cIfQoSWredDropLPreNTcpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWredDropLPreNTcpPkts.setStatus("current")
_Hh3cIfQoSWredDropLPreNTcpBytes_Type = Counter64
_Hh3cIfQoSWredDropLPreNTcpBytes_Object = MibTableColumn
hh3cIfQoSWredDropLPreNTcpBytes = _Hh3cIfQoSWredDropLPreNTcpBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 2, 1, 2),
    _Hh3cIfQoSWredDropLPreNTcpBytes_Type()
)
hh3cIfQoSWredDropLPreNTcpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWredDropLPreNTcpBytes.setStatus("current")
_Hh3cIfQoSWredDropLPreNTcpPPS_Type = Unsigned32
_Hh3cIfQoSWredDropLPreNTcpPPS_Object = MibTableColumn
hh3cIfQoSWredDropLPreNTcpPPS = _Hh3cIfQoSWredDropLPreNTcpPPS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 2, 1, 3),
    _Hh3cIfQoSWredDropLPreNTcpPPS_Type()
)
hh3cIfQoSWredDropLPreNTcpPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWredDropLPreNTcpPPS.setStatus("current")
_Hh3cIfQoSWredDropLPreNTcpBPS_Type = Unsigned32
_Hh3cIfQoSWredDropLPreNTcpBPS_Object = MibTableColumn
hh3cIfQoSWredDropLPreNTcpBPS = _Hh3cIfQoSWredDropLPreNTcpBPS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 2, 1, 4),
    _Hh3cIfQoSWredDropLPreNTcpBPS_Type()
)
hh3cIfQoSWredDropLPreNTcpBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWredDropLPreNTcpBPS.setStatus("current")
_Hh3cIfQoSWredDropLPreTcpPkts_Type = Counter64
_Hh3cIfQoSWredDropLPreTcpPkts_Object = MibTableColumn
hh3cIfQoSWredDropLPreTcpPkts = _Hh3cIfQoSWredDropLPreTcpPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 2, 1, 5),
    _Hh3cIfQoSWredDropLPreTcpPkts_Type()
)
hh3cIfQoSWredDropLPreTcpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWredDropLPreTcpPkts.setStatus("current")
_Hh3cIfQoSWredDropLPreTcpBytes_Type = Counter64
_Hh3cIfQoSWredDropLPreTcpBytes_Object = MibTableColumn
hh3cIfQoSWredDropLPreTcpBytes = _Hh3cIfQoSWredDropLPreTcpBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 2, 1, 6),
    _Hh3cIfQoSWredDropLPreTcpBytes_Type()
)
hh3cIfQoSWredDropLPreTcpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWredDropLPreTcpBytes.setStatus("current")
_Hh3cIfQoSWredDropLPreTcpPPS_Type = Unsigned32
_Hh3cIfQoSWredDropLPreTcpPPS_Object = MibTableColumn
hh3cIfQoSWredDropLPreTcpPPS = _Hh3cIfQoSWredDropLPreTcpPPS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 2, 1, 7),
    _Hh3cIfQoSWredDropLPreTcpPPS_Type()
)
hh3cIfQoSWredDropLPreTcpPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWredDropLPreTcpPPS.setStatus("current")
_Hh3cIfQoSWredDropLPreTcpBPS_Type = Unsigned32
_Hh3cIfQoSWredDropLPreTcpBPS_Object = MibTableColumn
hh3cIfQoSWredDropLPreTcpBPS = _Hh3cIfQoSWredDropLPreTcpBPS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 2, 1, 8),
    _Hh3cIfQoSWredDropLPreTcpBPS_Type()
)
hh3cIfQoSWredDropLPreTcpBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWredDropLPreTcpBPS.setStatus("current")
_Hh3cIfQoSWredDropHPreNTcpPkts_Type = Counter64
_Hh3cIfQoSWredDropHPreNTcpPkts_Object = MibTableColumn
hh3cIfQoSWredDropHPreNTcpPkts = _Hh3cIfQoSWredDropHPreNTcpPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 2, 1, 9),
    _Hh3cIfQoSWredDropHPreNTcpPkts_Type()
)
hh3cIfQoSWredDropHPreNTcpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWredDropHPreNTcpPkts.setStatus("current")
_Hh3cIfQoSWredDropHPreNTcpBytes_Type = Counter64
_Hh3cIfQoSWredDropHPreNTcpBytes_Object = MibTableColumn
hh3cIfQoSWredDropHPreNTcpBytes = _Hh3cIfQoSWredDropHPreNTcpBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 2, 1, 10),
    _Hh3cIfQoSWredDropHPreNTcpBytes_Type()
)
hh3cIfQoSWredDropHPreNTcpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWredDropHPreNTcpBytes.setStatus("current")
_Hh3cIfQoSWredDropHPreNTcpPPS_Type = Unsigned32
_Hh3cIfQoSWredDropHPreNTcpPPS_Object = MibTableColumn
hh3cIfQoSWredDropHPreNTcpPPS = _Hh3cIfQoSWredDropHPreNTcpPPS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 2, 1, 11),
    _Hh3cIfQoSWredDropHPreNTcpPPS_Type()
)
hh3cIfQoSWredDropHPreNTcpPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWredDropHPreNTcpPPS.setStatus("current")
_Hh3cIfQoSWredDropHPreNTcpBPS_Type = Unsigned32
_Hh3cIfQoSWredDropHPreNTcpBPS_Object = MibTableColumn
hh3cIfQoSWredDropHPreNTcpBPS = _Hh3cIfQoSWredDropHPreNTcpBPS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 2, 1, 12),
    _Hh3cIfQoSWredDropHPreNTcpBPS_Type()
)
hh3cIfQoSWredDropHPreNTcpBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWredDropHPreNTcpBPS.setStatus("current")
_Hh3cIfQoSWredDropHPreTcpPkts_Type = Counter64
_Hh3cIfQoSWredDropHPreTcpPkts_Object = MibTableColumn
hh3cIfQoSWredDropHPreTcpPkts = _Hh3cIfQoSWredDropHPreTcpPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 2, 1, 13),
    _Hh3cIfQoSWredDropHPreTcpPkts_Type()
)
hh3cIfQoSWredDropHPreTcpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWredDropHPreTcpPkts.setStatus("current")
_Hh3cIfQoSWredDropHPreTcpBytes_Type = Counter64
_Hh3cIfQoSWredDropHPreTcpBytes_Object = MibTableColumn
hh3cIfQoSWredDropHPreTcpBytes = _Hh3cIfQoSWredDropHPreTcpBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 2, 1, 14),
    _Hh3cIfQoSWredDropHPreTcpBytes_Type()
)
hh3cIfQoSWredDropHPreTcpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWredDropHPreTcpBytes.setStatus("current")
_Hh3cIfQoSWredDropHPreTcpPPS_Type = Unsigned32
_Hh3cIfQoSWredDropHPreTcpPPS_Object = MibTableColumn
hh3cIfQoSWredDropHPreTcpPPS = _Hh3cIfQoSWredDropHPreTcpPPS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 2, 1, 15),
    _Hh3cIfQoSWredDropHPreTcpPPS_Type()
)
hh3cIfQoSWredDropHPreTcpPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWredDropHPreTcpPPS.setStatus("current")
_Hh3cIfQoSWredDropHPreTcpBPS_Type = Unsigned32
_Hh3cIfQoSWredDropHPreTcpBPS_Object = MibTableColumn
hh3cIfQoSWredDropHPreTcpBPS = _Hh3cIfQoSWredDropHPreTcpBPS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 1, 2, 2, 1, 16),
    _Hh3cIfQoSWredDropHPreTcpBPS_Type()
)
hh3cIfQoSWredDropHPreTcpBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWredDropHPreTcpBPS.setStatus("current")
_Hh3cIfQoSSoftwareQueueObjects_ObjectIdentity = ObjectIdentity
hh3cIfQoSSoftwareQueueObjects = _Hh3cIfQoSSoftwareQueueObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2)
)
_Hh3cIfQoSFIFOObject_ObjectIdentity = ObjectIdentity
hh3cIfQoSFIFOObject = _Hh3cIfQoSFIFOObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 1)
)
_Hh3cIfQoSFIFOConfigTable_Object = MibTable
hh3cIfQoSFIFOConfigTable = _Hh3cIfQoSFIFOConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cIfQoSFIFOConfigTable.setStatus("current")
_Hh3cIfQoSFIFOConfigEntry_Object = MibTableRow
hh3cIfQoSFIFOConfigEntry = _Hh3cIfQoSFIFOConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 1, 1, 1)
)
hh3cIfQoSFIFOConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSFIFOConfigEntry.setStatus("current")
_Hh3cIfQoSFIFOMaxQueueLen_Type = Integer32
_Hh3cIfQoSFIFOMaxQueueLen_Object = MibTableColumn
hh3cIfQoSFIFOMaxQueueLen = _Hh3cIfQoSFIFOMaxQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 1, 1, 1, 1),
    _Hh3cIfQoSFIFOMaxQueueLen_Type()
)
hh3cIfQoSFIFOMaxQueueLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfQoSFIFOMaxQueueLen.setStatus("current")
_Hh3cIfQoSFIFORunInfoTable_Object = MibTable
hh3cIfQoSFIFORunInfoTable = _Hh3cIfQoSFIFORunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cIfQoSFIFORunInfoTable.setStatus("current")
_Hh3cIfQoSFIFORunInfoEntry_Object = MibTableRow
hh3cIfQoSFIFORunInfoEntry = _Hh3cIfQoSFIFORunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 1, 2, 1)
)
hh3cIfQoSFIFORunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSFIFORunInfoEntry.setStatus("current")
_Hh3cIfQoSFIFOSize_Type = Integer32
_Hh3cIfQoSFIFOSize_Object = MibTableColumn
hh3cIfQoSFIFOSize = _Hh3cIfQoSFIFOSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 1, 2, 1, 1),
    _Hh3cIfQoSFIFOSize_Type()
)
hh3cIfQoSFIFOSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSFIFOSize.setStatus("current")
_Hh3cIfQoSFIFODiscardPackets_Type = Counter64
_Hh3cIfQoSFIFODiscardPackets_Object = MibTableColumn
hh3cIfQoSFIFODiscardPackets = _Hh3cIfQoSFIFODiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 1, 2, 1, 2),
    _Hh3cIfQoSFIFODiscardPackets_Type()
)
hh3cIfQoSFIFODiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSFIFODiscardPackets.setStatus("current")
_Hh3cIfQoSPQObject_ObjectIdentity = ObjectIdentity
hh3cIfQoSPQObject = _Hh3cIfQoSPQObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 2)
)
_Hh3cIfQoSPQConfigGroup_ObjectIdentity = ObjectIdentity
hh3cIfQoSPQConfigGroup = _Hh3cIfQoSPQConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 2, 1)
)
_Hh3cIfQoSPQDefaultTable_Object = MibTable
hh3cIfQoSPQDefaultTable = _Hh3cIfQoSPQDefaultTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cIfQoSPQDefaultTable.setStatus("current")
_Hh3cIfQoSPQDefaultEntry_Object = MibTableRow
hh3cIfQoSPQDefaultEntry = _Hh3cIfQoSPQDefaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 2, 1, 1, 1)
)
hh3cIfQoSPQDefaultEntry.setIndexNames(
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSPQListNumber"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSPQDefaultEntry.setStatus("current")


class _Hh3cIfQoSPQListNumber_Type(Integer32):
    """Custom type hh3cIfQoSPQListNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Hh3cIfQoSPQListNumber_Type.__name__ = "Integer32"
_Hh3cIfQoSPQListNumber_Object = MibTableColumn
hh3cIfQoSPQListNumber = _Hh3cIfQoSPQListNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 2, 1, 1, 1, 1),
    _Hh3cIfQoSPQListNumber_Type()
)
hh3cIfQoSPQListNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfQoSPQListNumber.setStatus("current")
_Hh3cIfQoSPQDefaultQueueType_Type = PriorityQueue
_Hh3cIfQoSPQDefaultQueueType_Object = MibTableColumn
hh3cIfQoSPQDefaultQueueType = _Hh3cIfQoSPQDefaultQueueType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 2, 1, 1, 1, 2),
    _Hh3cIfQoSPQDefaultQueueType_Type()
)
hh3cIfQoSPQDefaultQueueType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfQoSPQDefaultQueueType.setStatus("current")
_Hh3cIfQoSPQQueueLengthTable_Object = MibTable
hh3cIfQoSPQQueueLengthTable = _Hh3cIfQoSPQQueueLengthTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cIfQoSPQQueueLengthTable.setStatus("current")
_Hh3cIfQoSPQQueueLengthEntry_Object = MibTableRow
hh3cIfQoSPQQueueLengthEntry = _Hh3cIfQoSPQQueueLengthEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 2, 1, 2, 1)
)
hh3cIfQoSPQQueueLengthEntry.setIndexNames(
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSPQListNumber"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSPQQueueLengthType"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSPQQueueLengthEntry.setStatus("current")
_Hh3cIfQoSPQQueueLengthType_Type = PriorityQueue
_Hh3cIfQoSPQQueueLengthType_Object = MibTableColumn
hh3cIfQoSPQQueueLengthType = _Hh3cIfQoSPQQueueLengthType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 2, 1, 2, 1, 1),
    _Hh3cIfQoSPQQueueLengthType_Type()
)
hh3cIfQoSPQQueueLengthType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfQoSPQQueueLengthType.setStatus("current")


class _Hh3cIfQoSPQQueueLengthValue_Type(Integer32):
    """Custom type hh3cIfQoSPQQueueLengthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Hh3cIfQoSPQQueueLengthValue_Type.__name__ = "Integer32"
_Hh3cIfQoSPQQueueLengthValue_Object = MibTableColumn
hh3cIfQoSPQQueueLengthValue = _Hh3cIfQoSPQQueueLengthValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 2, 1, 2, 1, 2),
    _Hh3cIfQoSPQQueueLengthValue_Type()
)
hh3cIfQoSPQQueueLengthValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfQoSPQQueueLengthValue.setStatus("current")
_Hh3cIfQoSPQClassRuleTable_Object = MibTable
hh3cIfQoSPQClassRuleTable = _Hh3cIfQoSPQClassRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cIfQoSPQClassRuleTable.setStatus("current")
_Hh3cIfQoSPQClassRuleEntry_Object = MibTableRow
hh3cIfQoSPQClassRuleEntry = _Hh3cIfQoSPQClassRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 2, 1, 3, 1)
)
hh3cIfQoSPQClassRuleEntry.setIndexNames(
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSPQListNumber"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSPQClassRuleType"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSPQClassRuleValue"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSPQClassRuleEntry.setStatus("current")


class _Hh3cIfQoSPQClassRuleType_Type(Integer32):
    """Custom type hh3cIfQoSPQClassRuleType based on Integer32"""
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


_Hh3cIfQoSPQClassRuleType_Type.__name__ = "Integer32"
_Hh3cIfQoSPQClassRuleType_Object = MibTableColumn
hh3cIfQoSPQClassRuleType = _Hh3cIfQoSPQClassRuleType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 2, 1, 3, 1, 1),
    _Hh3cIfQoSPQClassRuleType_Type()
)
hh3cIfQoSPQClassRuleType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfQoSPQClassRuleType.setStatus("current")
_Hh3cIfQoSPQClassRuleValue_Type = Integer32
_Hh3cIfQoSPQClassRuleValue_Object = MibTableColumn
hh3cIfQoSPQClassRuleValue = _Hh3cIfQoSPQClassRuleValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 2, 1, 3, 1, 2),
    _Hh3cIfQoSPQClassRuleValue_Type()
)
hh3cIfQoSPQClassRuleValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfQoSPQClassRuleValue.setStatus("current")
_Hh3cIfQoSPQClassRuleQueueType_Type = PriorityQueue
_Hh3cIfQoSPQClassRuleQueueType_Object = MibTableColumn
hh3cIfQoSPQClassRuleQueueType = _Hh3cIfQoSPQClassRuleQueueType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 2, 1, 3, 1, 3),
    _Hh3cIfQoSPQClassRuleQueueType_Type()
)
hh3cIfQoSPQClassRuleQueueType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSPQClassRuleQueueType.setStatus("current")
_Hh3cIfQoSPQClassRowStatus_Type = RowStatus
_Hh3cIfQoSPQClassRowStatus_Object = MibTableColumn
hh3cIfQoSPQClassRowStatus = _Hh3cIfQoSPQClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 2, 1, 3, 1, 4),
    _Hh3cIfQoSPQClassRowStatus_Type()
)
hh3cIfQoSPQClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSPQClassRowStatus.setStatus("current")
_Hh3cIfQoSPQApplyTable_Object = MibTable
hh3cIfQoSPQApplyTable = _Hh3cIfQoSPQApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cIfQoSPQApplyTable.setStatus("current")
_Hh3cIfQoSPQApplyEntry_Object = MibTableRow
hh3cIfQoSPQApplyEntry = _Hh3cIfQoSPQApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 2, 1, 4, 1)
)
hh3cIfQoSPQApplyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSPQApplyEntry.setStatus("current")


class _Hh3cIfQoSPQApplyListNumber_Type(Integer32):
    """Custom type hh3cIfQoSPQApplyListNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Hh3cIfQoSPQApplyListNumber_Type.__name__ = "Integer32"
_Hh3cIfQoSPQApplyListNumber_Object = MibTableColumn
hh3cIfQoSPQApplyListNumber = _Hh3cIfQoSPQApplyListNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 2, 1, 4, 1, 1),
    _Hh3cIfQoSPQApplyListNumber_Type()
)
hh3cIfQoSPQApplyListNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSPQApplyListNumber.setStatus("current")
_Hh3cIfQoSPQApplyRowStatus_Type = RowStatus
_Hh3cIfQoSPQApplyRowStatus_Object = MibTableColumn
hh3cIfQoSPQApplyRowStatus = _Hh3cIfQoSPQApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 2, 1, 4, 1, 2),
    _Hh3cIfQoSPQApplyRowStatus_Type()
)
hh3cIfQoSPQApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSPQApplyRowStatus.setStatus("current")
_Hh3cIfQoSPQRunInfoGroup_ObjectIdentity = ObjectIdentity
hh3cIfQoSPQRunInfoGroup = _Hh3cIfQoSPQRunInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 2, 2)
)
_Hh3cIfQoSPQRunInfoTable_Object = MibTable
hh3cIfQoSPQRunInfoTable = _Hh3cIfQoSPQRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cIfQoSPQRunInfoTable.setStatus("current")
_Hh3cIfQoSPQRunInfoEntry_Object = MibTableRow
hh3cIfQoSPQRunInfoEntry = _Hh3cIfQoSPQRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 2, 2, 1, 1)
)
hh3cIfQoSPQRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSPQType"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSPQRunInfoEntry.setStatus("current")
_Hh3cIfQoSPQType_Type = PriorityQueue
_Hh3cIfQoSPQType_Object = MibTableColumn
hh3cIfQoSPQType = _Hh3cIfQoSPQType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 2, 2, 1, 1, 1),
    _Hh3cIfQoSPQType_Type()
)
hh3cIfQoSPQType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfQoSPQType.setStatus("current")
_Hh3cIfQoSPQSize_Type = Integer32
_Hh3cIfQoSPQSize_Object = MibTableColumn
hh3cIfQoSPQSize = _Hh3cIfQoSPQSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 2, 2, 1, 1, 2),
    _Hh3cIfQoSPQSize_Type()
)
hh3cIfQoSPQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSPQSize.setStatus("current")
_Hh3cIfQoSPQLength_Type = Integer32
_Hh3cIfQoSPQLength_Object = MibTableColumn
hh3cIfQoSPQLength = _Hh3cIfQoSPQLength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 2, 2, 1, 1, 3),
    _Hh3cIfQoSPQLength_Type()
)
hh3cIfQoSPQLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSPQLength.setStatus("current")
_Hh3cIfQoSPQDiscardPackets_Type = Counter64
_Hh3cIfQoSPQDiscardPackets_Object = MibTableColumn
hh3cIfQoSPQDiscardPackets = _Hh3cIfQoSPQDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 2, 2, 1, 1, 4),
    _Hh3cIfQoSPQDiscardPackets_Type()
)
hh3cIfQoSPQDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSPQDiscardPackets.setStatus("current")
_Hh3cIfQoSCQObject_ObjectIdentity = ObjectIdentity
hh3cIfQoSCQObject = _Hh3cIfQoSCQObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 3)
)
_Hh3cIfQoSCQConfigGroup_ObjectIdentity = ObjectIdentity
hh3cIfQoSCQConfigGroup = _Hh3cIfQoSCQConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 3, 1)
)
_Hh3cIfQoSCQDefaultTable_Object = MibTable
hh3cIfQoSCQDefaultTable = _Hh3cIfQoSCQDefaultTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cIfQoSCQDefaultTable.setStatus("current")
_Hh3cIfQoSCQDefaultEntry_Object = MibTableRow
hh3cIfQoSCQDefaultEntry = _Hh3cIfQoSCQDefaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 3, 1, 1, 1)
)
hh3cIfQoSCQDefaultEntry.setIndexNames(
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSCQListNumber"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSCQDefaultEntry.setStatus("current")


class _Hh3cIfQoSCQListNumber_Type(Integer32):
    """Custom type hh3cIfQoSCQListNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Hh3cIfQoSCQListNumber_Type.__name__ = "Integer32"
_Hh3cIfQoSCQListNumber_Object = MibTableColumn
hh3cIfQoSCQListNumber = _Hh3cIfQoSCQListNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 3, 1, 1, 1, 1),
    _Hh3cIfQoSCQListNumber_Type()
)
hh3cIfQoSCQListNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfQoSCQListNumber.setStatus("current")


class _Hh3cIfQoSCQDefaultQueueID_Type(Integer32):
    """Custom type hh3cIfQoSCQDefaultQueueID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Hh3cIfQoSCQDefaultQueueID_Type.__name__ = "Integer32"
_Hh3cIfQoSCQDefaultQueueID_Object = MibTableColumn
hh3cIfQoSCQDefaultQueueID = _Hh3cIfQoSCQDefaultQueueID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 3, 1, 1, 1, 2),
    _Hh3cIfQoSCQDefaultQueueID_Type()
)
hh3cIfQoSCQDefaultQueueID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfQoSCQDefaultQueueID.setStatus("current")
_Hh3cIfQoSCQQueueLengthTable_Object = MibTable
hh3cIfQoSCQQueueLengthTable = _Hh3cIfQoSCQQueueLengthTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cIfQoSCQQueueLengthTable.setStatus("current")
_Hh3cIfQoSCQQueueLengthEntry_Object = MibTableRow
hh3cIfQoSCQQueueLengthEntry = _Hh3cIfQoSCQQueueLengthEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 3, 1, 2, 1)
)
hh3cIfQoSCQQueueLengthEntry.setIndexNames(
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSCQListNumber"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSCQQueueID"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSCQQueueLengthEntry.setStatus("current")


class _Hh3cIfQoSCQQueueID_Type(Integer32):
    """Custom type hh3cIfQoSCQQueueID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Hh3cIfQoSCQQueueID_Type.__name__ = "Integer32"
_Hh3cIfQoSCQQueueID_Object = MibTableColumn
hh3cIfQoSCQQueueID = _Hh3cIfQoSCQQueueID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 3, 1, 2, 1, 1),
    _Hh3cIfQoSCQQueueID_Type()
)
hh3cIfQoSCQQueueID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfQoSCQQueueID.setStatus("current")


class _Hh3cIfQoSCQQueueLength_Type(Integer32):
    """Custom type hh3cIfQoSCQQueueLength based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Hh3cIfQoSCQQueueLength_Type.__name__ = "Integer32"
_Hh3cIfQoSCQQueueLength_Object = MibTableColumn
hh3cIfQoSCQQueueLength = _Hh3cIfQoSCQQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 3, 1, 2, 1, 2),
    _Hh3cIfQoSCQQueueLength_Type()
)
hh3cIfQoSCQQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfQoSCQQueueLength.setStatus("current")


class _Hh3cIfQoSCQQueueServing_Type(Integer32):
    """Custom type hh3cIfQoSCQQueueServing based on Integer32"""
    defaultValue = 1500


_Hh3cIfQoSCQQueueServing_Object = MibTableColumn
hh3cIfQoSCQQueueServing = _Hh3cIfQoSCQQueueServing_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 3, 1, 2, 1, 3),
    _Hh3cIfQoSCQQueueServing_Type()
)
hh3cIfQoSCQQueueServing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfQoSCQQueueServing.setStatus("current")
_Hh3cIfQoSCQClassRuleTable_Object = MibTable
hh3cIfQoSCQClassRuleTable = _Hh3cIfQoSCQClassRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 3, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cIfQoSCQClassRuleTable.setStatus("current")
_Hh3cIfQoSCQClassRuleEntry_Object = MibTableRow
hh3cIfQoSCQClassRuleEntry = _Hh3cIfQoSCQClassRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 3, 1, 3, 1)
)
hh3cIfQoSCQClassRuleEntry.setIndexNames(
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSCQListNumber"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSCQClassRuleType"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSCQClassRuleValue"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSCQClassRuleEntry.setStatus("current")


class _Hh3cIfQoSCQClassRuleType_Type(Integer32):
    """Custom type hh3cIfQoSCQClassRuleType based on Integer32"""
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


_Hh3cIfQoSCQClassRuleType_Type.__name__ = "Integer32"
_Hh3cIfQoSCQClassRuleType_Object = MibTableColumn
hh3cIfQoSCQClassRuleType = _Hh3cIfQoSCQClassRuleType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 3, 1, 3, 1, 1),
    _Hh3cIfQoSCQClassRuleType_Type()
)
hh3cIfQoSCQClassRuleType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfQoSCQClassRuleType.setStatus("current")
_Hh3cIfQoSCQClassRuleValue_Type = Integer32
_Hh3cIfQoSCQClassRuleValue_Object = MibTableColumn
hh3cIfQoSCQClassRuleValue = _Hh3cIfQoSCQClassRuleValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 3, 1, 3, 1, 2),
    _Hh3cIfQoSCQClassRuleValue_Type()
)
hh3cIfQoSCQClassRuleValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfQoSCQClassRuleValue.setStatus("current")


class _Hh3cIfQoSCQClassRuleQueueID_Type(Integer32):
    """Custom type hh3cIfQoSCQClassRuleQueueID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Hh3cIfQoSCQClassRuleQueueID_Type.__name__ = "Integer32"
_Hh3cIfQoSCQClassRuleQueueID_Object = MibTableColumn
hh3cIfQoSCQClassRuleQueueID = _Hh3cIfQoSCQClassRuleQueueID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 3, 1, 3, 1, 3),
    _Hh3cIfQoSCQClassRuleQueueID_Type()
)
hh3cIfQoSCQClassRuleQueueID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSCQClassRuleQueueID.setStatus("current")
_Hh3cIfQoSCQClassRowStatus_Type = RowStatus
_Hh3cIfQoSCQClassRowStatus_Object = MibTableColumn
hh3cIfQoSCQClassRowStatus = _Hh3cIfQoSCQClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 3, 1, 3, 1, 4),
    _Hh3cIfQoSCQClassRowStatus_Type()
)
hh3cIfQoSCQClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSCQClassRowStatus.setStatus("current")
_Hh3cIfQoSCQApplyTable_Object = MibTable
hh3cIfQoSCQApplyTable = _Hh3cIfQoSCQApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 3, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cIfQoSCQApplyTable.setStatus("current")
_Hh3cIfQoSCQApplyEntry_Object = MibTableRow
hh3cIfQoSCQApplyEntry = _Hh3cIfQoSCQApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 3, 1, 4, 1)
)
hh3cIfQoSCQApplyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSCQApplyEntry.setStatus("current")


class _Hh3cIfQoSCQApplyListNumber_Type(Integer32):
    """Custom type hh3cIfQoSCQApplyListNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Hh3cIfQoSCQApplyListNumber_Type.__name__ = "Integer32"
_Hh3cIfQoSCQApplyListNumber_Object = MibTableColumn
hh3cIfQoSCQApplyListNumber = _Hh3cIfQoSCQApplyListNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 3, 1, 4, 1, 1),
    _Hh3cIfQoSCQApplyListNumber_Type()
)
hh3cIfQoSCQApplyListNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSCQApplyListNumber.setStatus("current")
_Hh3cIfQoSCQApplyRowStatus_Type = RowStatus
_Hh3cIfQoSCQApplyRowStatus_Object = MibTableColumn
hh3cIfQoSCQApplyRowStatus = _Hh3cIfQoSCQApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 3, 1, 4, 1, 2),
    _Hh3cIfQoSCQApplyRowStatus_Type()
)
hh3cIfQoSCQApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSCQApplyRowStatus.setStatus("current")
_Hh3cIfQoSCQRunInfoGroup_ObjectIdentity = ObjectIdentity
hh3cIfQoSCQRunInfoGroup = _Hh3cIfQoSCQRunInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 3, 2)
)
_Hh3cIfQoSCQRunInfoTable_Object = MibTable
hh3cIfQoSCQRunInfoTable = _Hh3cIfQoSCQRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cIfQoSCQRunInfoTable.setStatus("current")
_Hh3cIfQoSCQRunInfoEntry_Object = MibTableRow
hh3cIfQoSCQRunInfoEntry = _Hh3cIfQoSCQRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 3, 2, 1, 1)
)
hh3cIfQoSCQRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSCQQueueID"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSCQRunInfoEntry.setStatus("current")
_Hh3cIfQoSCQRunInfoSize_Type = Integer32
_Hh3cIfQoSCQRunInfoSize_Object = MibTableColumn
hh3cIfQoSCQRunInfoSize = _Hh3cIfQoSCQRunInfoSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 3, 2, 1, 1, 1),
    _Hh3cIfQoSCQRunInfoSize_Type()
)
hh3cIfQoSCQRunInfoSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSCQRunInfoSize.setStatus("current")
_Hh3cIfQoSCQRunInfoLength_Type = Integer32
_Hh3cIfQoSCQRunInfoLength_Object = MibTableColumn
hh3cIfQoSCQRunInfoLength = _Hh3cIfQoSCQRunInfoLength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 3, 2, 1, 1, 2),
    _Hh3cIfQoSCQRunInfoLength_Type()
)
hh3cIfQoSCQRunInfoLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSCQRunInfoLength.setStatus("current")
_Hh3cIfQoSCQRunInfoDiscardPackets_Type = Counter64
_Hh3cIfQoSCQRunInfoDiscardPackets_Object = MibTableColumn
hh3cIfQoSCQRunInfoDiscardPackets = _Hh3cIfQoSCQRunInfoDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 3, 2, 1, 1, 3),
    _Hh3cIfQoSCQRunInfoDiscardPackets_Type()
)
hh3cIfQoSCQRunInfoDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSCQRunInfoDiscardPackets.setStatus("current")
_Hh3cIfQoSWFQObject_ObjectIdentity = ObjectIdentity
hh3cIfQoSWFQObject = _Hh3cIfQoSWFQObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 4)
)
_Hh3cIfQoSWFQConfigGroup_ObjectIdentity = ObjectIdentity
hh3cIfQoSWFQConfigGroup = _Hh3cIfQoSWFQConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 4, 1)
)
_Hh3cIfQoSWFQTable_Object = MibTable
hh3cIfQoSWFQTable = _Hh3cIfQoSWFQTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cIfQoSWFQTable.setStatus("current")
_Hh3cIfQoSWFQEntry_Object = MibTableRow
hh3cIfQoSWFQEntry = _Hh3cIfQoSWFQEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 4, 1, 1, 1)
)
hh3cIfQoSWFQEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSWFQEntry.setStatus("current")


class _Hh3cIfQoSWFQQueueLength_Type(Integer32):
    """Custom type hh3cIfQoSWFQQueueLength based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Hh3cIfQoSWFQQueueLength_Type.__name__ = "Integer32"
_Hh3cIfQoSWFQQueueLength_Object = MibTableColumn
hh3cIfQoSWFQQueueLength = _Hh3cIfQoSWFQQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 4, 1, 1, 1, 1),
    _Hh3cIfQoSWFQQueueLength_Type()
)
hh3cIfQoSWFQQueueLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSWFQQueueLength.setStatus("current")


class _Hh3cIfQoSWFQQueueNumber_Type(Integer32):
    """Custom type hh3cIfQoSWFQQueueNumber based on Integer32"""
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


_Hh3cIfQoSWFQQueueNumber_Type.__name__ = "Integer32"
_Hh3cIfQoSWFQQueueNumber_Object = MibTableColumn
hh3cIfQoSWFQQueueNumber = _Hh3cIfQoSWFQQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 4, 1, 1, 1, 2),
    _Hh3cIfQoSWFQQueueNumber_Type()
)
hh3cIfQoSWFQQueueNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSWFQQueueNumber.setStatus("current")
_Hh3cIfQoSWFQRowStatus_Type = RowStatus
_Hh3cIfQoSWFQRowStatus_Object = MibTableColumn
hh3cIfQoSWFQRowStatus = _Hh3cIfQoSWFQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 4, 1, 1, 1, 3),
    _Hh3cIfQoSWFQRowStatus_Type()
)
hh3cIfQoSWFQRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSWFQRowStatus.setStatus("current")


class _Hh3cIfQoSWFQType_Type(Integer32):
    """Custom type hh3cIfQoSWFQType based on Integer32"""
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


_Hh3cIfQoSWFQType_Type.__name__ = "Integer32"
_Hh3cIfQoSWFQType_Object = MibTableColumn
hh3cIfQoSWFQType = _Hh3cIfQoSWFQType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 4, 1, 1, 1, 4),
    _Hh3cIfQoSWFQType_Type()
)
hh3cIfQoSWFQType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSWFQType.setStatus("current")
_Hh3cIfQoSWFQRunInfoGroup_ObjectIdentity = ObjectIdentity
hh3cIfQoSWFQRunInfoGroup = _Hh3cIfQoSWFQRunInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 4, 2)
)
_Hh3cIfQoSWFQRunInfoTable_Object = MibTable
hh3cIfQoSWFQRunInfoTable = _Hh3cIfQoSWFQRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cIfQoSWFQRunInfoTable.setStatus("current")
_Hh3cIfQoSWFQRunInfoEntry_Object = MibTableRow
hh3cIfQoSWFQRunInfoEntry = _Hh3cIfQoSWFQRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 4, 2, 1, 1)
)
hh3cIfQoSWFQRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSWFQRunInfoEntry.setStatus("current")
_Hh3cIfQoSWFQSize_Type = Integer32
_Hh3cIfQoSWFQSize_Object = MibTableColumn
hh3cIfQoSWFQSize = _Hh3cIfQoSWFQSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 4, 2, 1, 1, 1),
    _Hh3cIfQoSWFQSize_Type()
)
hh3cIfQoSWFQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWFQSize.setStatus("current")
_Hh3cIfQoSWFQLength_Type = Integer32
_Hh3cIfQoSWFQLength_Object = MibTableColumn
hh3cIfQoSWFQLength = _Hh3cIfQoSWFQLength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 4, 2, 1, 1, 2),
    _Hh3cIfQoSWFQLength_Type()
)
hh3cIfQoSWFQLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWFQLength.setStatus("current")
_Hh3cIfQoSWFQDiscardPackets_Type = Counter64
_Hh3cIfQoSWFQDiscardPackets_Object = MibTableColumn
hh3cIfQoSWFQDiscardPackets = _Hh3cIfQoSWFQDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 4, 2, 1, 1, 3),
    _Hh3cIfQoSWFQDiscardPackets_Type()
)
hh3cIfQoSWFQDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWFQDiscardPackets.setStatus("current")
_Hh3cIfQoSWFQHashedActiveQueues_Type = Integer32
_Hh3cIfQoSWFQHashedActiveQueues_Object = MibTableColumn
hh3cIfQoSWFQHashedActiveQueues = _Hh3cIfQoSWFQHashedActiveQueues_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 4, 2, 1, 1, 4),
    _Hh3cIfQoSWFQHashedActiveQueues_Type()
)
hh3cIfQoSWFQHashedActiveQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWFQHashedActiveQueues.setStatus("current")
_Hh3cIfQoSWFQHashedMaxActiveQueues_Type = Integer32
_Hh3cIfQoSWFQHashedMaxActiveQueues_Object = MibTableColumn
hh3cIfQoSWFQHashedMaxActiveQueues = _Hh3cIfQoSWFQHashedMaxActiveQueues_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 4, 2, 1, 1, 5),
    _Hh3cIfQoSWFQHashedMaxActiveQueues_Type()
)
hh3cIfQoSWFQHashedMaxActiveQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWFQHashedMaxActiveQueues.setStatus("current")
_Hh3cIfQosWFQhashedTotalQueues_Type = Integer32
_Hh3cIfQosWFQhashedTotalQueues_Object = MibTableColumn
hh3cIfQosWFQhashedTotalQueues = _Hh3cIfQosWFQhashedTotalQueues_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 4, 2, 1, 1, 6),
    _Hh3cIfQosWFQhashedTotalQueues_Type()
)
hh3cIfQosWFQhashedTotalQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQosWFQhashedTotalQueues.setStatus("current")
_Hh3cIfQoSBandwidthGroup_ObjectIdentity = ObjectIdentity
hh3cIfQoSBandwidthGroup = _Hh3cIfQoSBandwidthGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 5)
)
_Hh3cIfQoSBandwidthTable_Object = MibTable
hh3cIfQoSBandwidthTable = _Hh3cIfQoSBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    hh3cIfQoSBandwidthTable.setStatus("current")
_Hh3cIfQoSBandwidthEntry_Object = MibTableRow
hh3cIfQoSBandwidthEntry = _Hh3cIfQoSBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 5, 1, 1)
)
hh3cIfQoSBandwidthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSBandwidthEntry.setStatus("current")
_Hh3cIfQoSMaxBandwidth_Type = Integer32
_Hh3cIfQoSMaxBandwidth_Object = MibTableColumn
hh3cIfQoSMaxBandwidth = _Hh3cIfQoSMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 5, 1, 1, 1),
    _Hh3cIfQoSMaxBandwidth_Type()
)
hh3cIfQoSMaxBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSMaxBandwidth.setStatus("current")


class _Hh3cIfQoSReservedBandwidthPct_Type(Integer32):
    """Custom type hh3cIfQoSReservedBandwidthPct based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Hh3cIfQoSReservedBandwidthPct_Type.__name__ = "Integer32"
_Hh3cIfQoSReservedBandwidthPct_Object = MibTableColumn
hh3cIfQoSReservedBandwidthPct = _Hh3cIfQoSReservedBandwidthPct_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 5, 1, 1, 2),
    _Hh3cIfQoSReservedBandwidthPct_Type()
)
hh3cIfQoSReservedBandwidthPct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSReservedBandwidthPct.setStatus("current")
_Hh3cIfQoSBandwidthRowStatus_Type = RowStatus
_Hh3cIfQoSBandwidthRowStatus_Object = MibTableColumn
hh3cIfQoSBandwidthRowStatus = _Hh3cIfQoSBandwidthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 5, 1, 1, 3),
    _Hh3cIfQoSBandwidthRowStatus_Type()
)
hh3cIfQoSBandwidthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSBandwidthRowStatus.setStatus("current")
_Hh3cIfQoSQmtokenGroup_ObjectIdentity = ObjectIdentity
hh3cIfQoSQmtokenGroup = _Hh3cIfQoSQmtokenGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 6)
)
_Hh3cIfQoSQmtokenTable_Object = MibTable
hh3cIfQoSQmtokenTable = _Hh3cIfQoSQmtokenTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    hh3cIfQoSQmtokenTable.setStatus("current")
_Hh3cIfQoSQmtokenEntry_Object = MibTableRow
hh3cIfQoSQmtokenEntry = _Hh3cIfQoSQmtokenEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 6, 1, 1)
)
hh3cIfQoSQmtokenEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSQmtokenEntry.setStatus("current")


class _Hh3cIfQoSQmtokenNumber_Type(Integer32):
    """Custom type hh3cIfQoSQmtokenNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_Hh3cIfQoSQmtokenNumber_Type.__name__ = "Integer32"
_Hh3cIfQoSQmtokenNumber_Object = MibTableColumn
hh3cIfQoSQmtokenNumber = _Hh3cIfQoSQmtokenNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 6, 1, 1, 1),
    _Hh3cIfQoSQmtokenNumber_Type()
)
hh3cIfQoSQmtokenNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSQmtokenNumber.setStatus("current")
_Hh3cIfQoSQmtokenRosStatus_Type = RowStatus
_Hh3cIfQoSQmtokenRosStatus_Object = MibTableColumn
hh3cIfQoSQmtokenRosStatus = _Hh3cIfQoSQmtokenRosStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 6, 1, 1, 2),
    _Hh3cIfQoSQmtokenRosStatus_Type()
)
hh3cIfQoSQmtokenRosStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSQmtokenRosStatus.setStatus("current")
_Hh3cIfQoSRTPQObject_ObjectIdentity = ObjectIdentity
hh3cIfQoSRTPQObject = _Hh3cIfQoSRTPQObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 7)
)
_Hh3cIfQoSRTPQConfigGroup_ObjectIdentity = ObjectIdentity
hh3cIfQoSRTPQConfigGroup = _Hh3cIfQoSRTPQConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 7, 1)
)
_Hh3cIfQoSRTPQConfigTable_Object = MibTable
hh3cIfQoSRTPQConfigTable = _Hh3cIfQoSRTPQConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cIfQoSRTPQConfigTable.setStatus("current")
_Hh3cIfQoSRTPQConfigEntry_Object = MibTableRow
hh3cIfQoSRTPQConfigEntry = _Hh3cIfQoSRTPQConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 7, 1, 1, 1)
)
hh3cIfQoSRTPQConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSRTPQConfigEntry.setStatus("current")


class _Hh3cIfQoSRTPQStartPort_Type(Integer32):
    """Custom type hh3cIfQoSRTPQStartPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 65535),
    )


_Hh3cIfQoSRTPQStartPort_Type.__name__ = "Integer32"
_Hh3cIfQoSRTPQStartPort_Object = MibTableColumn
hh3cIfQoSRTPQStartPort = _Hh3cIfQoSRTPQStartPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 7, 1, 1, 1, 1),
    _Hh3cIfQoSRTPQStartPort_Type()
)
hh3cIfQoSRTPQStartPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSRTPQStartPort.setStatus("current")


class _Hh3cIfQoSRTPQEndPort_Type(Integer32):
    """Custom type hh3cIfQoSRTPQEndPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 65535),
    )


_Hh3cIfQoSRTPQEndPort_Type.__name__ = "Integer32"
_Hh3cIfQoSRTPQEndPort_Object = MibTableColumn
hh3cIfQoSRTPQEndPort = _Hh3cIfQoSRTPQEndPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 7, 1, 1, 1, 2),
    _Hh3cIfQoSRTPQEndPort_Type()
)
hh3cIfQoSRTPQEndPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSRTPQEndPort.setStatus("current")
_Hh3cIfQoSRTPQReservedBandwidth_Type = Integer32
_Hh3cIfQoSRTPQReservedBandwidth_Object = MibTableColumn
hh3cIfQoSRTPQReservedBandwidth = _Hh3cIfQoSRTPQReservedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 7, 1, 1, 1, 3),
    _Hh3cIfQoSRTPQReservedBandwidth_Type()
)
hh3cIfQoSRTPQReservedBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSRTPQReservedBandwidth.setStatus("current")
_Hh3cIfQoSRTPQCbs_Type = Unsigned32
_Hh3cIfQoSRTPQCbs_Object = MibTableColumn
hh3cIfQoSRTPQCbs = _Hh3cIfQoSRTPQCbs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 7, 1, 1, 1, 4),
    _Hh3cIfQoSRTPQCbs_Type()
)
hh3cIfQoSRTPQCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSRTPQCbs.setStatus("current")
_Hh3cIfQoSRTPQRowStatus_Type = RowStatus
_Hh3cIfQoSRTPQRowStatus_Object = MibTableColumn
hh3cIfQoSRTPQRowStatus = _Hh3cIfQoSRTPQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 7, 1, 1, 1, 5),
    _Hh3cIfQoSRTPQRowStatus_Type()
)
hh3cIfQoSRTPQRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSRTPQRowStatus.setStatus("current")
_Hh3cIfQoSRTPQRunInfoGroup_ObjectIdentity = ObjectIdentity
hh3cIfQoSRTPQRunInfoGroup = _Hh3cIfQoSRTPQRunInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 7, 2)
)
_Hh3cIfQoSRTPQRunInfoTable_Object = MibTable
hh3cIfQoSRTPQRunInfoTable = _Hh3cIfQoSRTPQRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 7, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cIfQoSRTPQRunInfoTable.setStatus("current")
_Hh3cIfQoSRTPQRunInfoEntry_Object = MibTableRow
hh3cIfQoSRTPQRunInfoEntry = _Hh3cIfQoSRTPQRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 7, 2, 1, 1)
)
hh3cIfQoSRTPQRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSRTPQRunInfoEntry.setStatus("current")
_Hh3cIfQoSRTPQPacketNumber_Type = Integer32
_Hh3cIfQoSRTPQPacketNumber_Object = MibTableColumn
hh3cIfQoSRTPQPacketNumber = _Hh3cIfQoSRTPQPacketNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 7, 2, 1, 1, 1),
    _Hh3cIfQoSRTPQPacketNumber_Type()
)
hh3cIfQoSRTPQPacketNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSRTPQPacketNumber.setStatus("current")
_Hh3cIfQoSRTPQPacketSize_Type = Integer32
_Hh3cIfQoSRTPQPacketSize_Object = MibTableColumn
hh3cIfQoSRTPQPacketSize = _Hh3cIfQoSRTPQPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 7, 2, 1, 1, 2),
    _Hh3cIfQoSRTPQPacketSize_Type()
)
hh3cIfQoSRTPQPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSRTPQPacketSize.setStatus("current")
_Hh3cIfQoSRTPQOutputPackets_Type = Counter64
_Hh3cIfQoSRTPQOutputPackets_Object = MibTableColumn
hh3cIfQoSRTPQOutputPackets = _Hh3cIfQoSRTPQOutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 7, 2, 1, 1, 3),
    _Hh3cIfQoSRTPQOutputPackets_Type()
)
hh3cIfQoSRTPQOutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSRTPQOutputPackets.setStatus("current")
_Hh3cIfQoSRTPQDiscardPackets_Type = Counter64
_Hh3cIfQoSRTPQDiscardPackets_Object = MibTableColumn
hh3cIfQoSRTPQDiscardPackets = _Hh3cIfQoSRTPQDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 7, 2, 1, 1, 4),
    _Hh3cIfQoSRTPQDiscardPackets_Type()
)
hh3cIfQoSRTPQDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSRTPQDiscardPackets.setStatus("current")
_Hh3cIfQoSCarListObject_ObjectIdentity = ObjectIdentity
hh3cIfQoSCarListObject = _Hh3cIfQoSCarListObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 8)
)
_Hh3cIfQoCarListGroup_ObjectIdentity = ObjectIdentity
hh3cIfQoCarListGroup = _Hh3cIfQoCarListGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 8, 1)
)
_Hh3cIfQoSCarlTable_Object = MibTable
hh3cIfQoSCarlTable = _Hh3cIfQoSCarlTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 8, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cIfQoSCarlTable.setStatus("current")
_Hh3cIfQoSCarlEntry_Object = MibTableRow
hh3cIfQoSCarlEntry = _Hh3cIfQoSCarlEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 8, 1, 1, 1)
)
hh3cIfQoSCarlEntry.setIndexNames(
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSCarlListNum"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSCarlEntry.setStatus("current")
_Hh3cIfQoSCarlListNum_Type = Integer32
_Hh3cIfQoSCarlListNum_Object = MibTableColumn
hh3cIfQoSCarlListNum = _Hh3cIfQoSCarlListNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 8, 1, 1, 1, 1),
    _Hh3cIfQoSCarlListNum_Type()
)
hh3cIfQoSCarlListNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfQoSCarlListNum.setStatus("current")


class _Hh3cIfQoSCarlParaType_Type(Integer32):
    """Custom type hh3cIfQoSCarlParaType based on Integer32"""
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


_Hh3cIfQoSCarlParaType_Type.__name__ = "Integer32"
_Hh3cIfQoSCarlParaType_Object = MibTableColumn
hh3cIfQoSCarlParaType = _Hh3cIfQoSCarlParaType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 8, 1, 1, 1, 2),
    _Hh3cIfQoSCarlParaType_Type()
)
hh3cIfQoSCarlParaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSCarlParaType.setStatus("current")
_Hh3cIfQoSCarlParaValue_Type = OctetString
_Hh3cIfQoSCarlParaValue_Object = MibTableColumn
hh3cIfQoSCarlParaValue = _Hh3cIfQoSCarlParaValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 8, 1, 1, 1, 3),
    _Hh3cIfQoSCarlParaValue_Type()
)
hh3cIfQoSCarlParaValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSCarlParaValue.setStatus("current")
_Hh3cIfQoSCarlRowStatus_Type = RowStatus
_Hh3cIfQoSCarlRowStatus_Object = MibTableColumn
hh3cIfQoSCarlRowStatus = _Hh3cIfQoSCarlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 2, 8, 1, 1, 1, 4),
    _Hh3cIfQoSCarlRowStatus_Type()
)
hh3cIfQoSCarlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSCarlRowStatus.setStatus("current")
_Hh3cIfQoSLineRateObjects_ObjectIdentity = ObjectIdentity
hh3cIfQoSLineRateObjects = _Hh3cIfQoSLineRateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 3)
)
_Hh3cIfQoSLRConfigTable_Object = MibTable
hh3cIfQoSLRConfigTable = _Hh3cIfQoSLRConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cIfQoSLRConfigTable.setStatus("current")
_Hh3cIfQoSLRConfigEntry_Object = MibTableRow
hh3cIfQoSLRConfigEntry = _Hh3cIfQoSLRConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 3, 1, 1)
)
hh3cIfQoSLRConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSLRDirection"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSLRConfigEntry.setStatus("current")
_Hh3cIfQoSLRDirection_Type = Direction
_Hh3cIfQoSLRDirection_Object = MibTableColumn
hh3cIfQoSLRDirection = _Hh3cIfQoSLRDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 3, 1, 1, 1),
    _Hh3cIfQoSLRDirection_Type()
)
hh3cIfQoSLRDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfQoSLRDirection.setStatus("current")
_Hh3cIfQoSLRCir_Type = Unsigned32
_Hh3cIfQoSLRCir_Object = MibTableColumn
hh3cIfQoSLRCir = _Hh3cIfQoSLRCir_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 3, 1, 1, 2),
    _Hh3cIfQoSLRCir_Type()
)
hh3cIfQoSLRCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSLRCir.setStatus("current")
_Hh3cIfQoSLRCbs_Type = Unsigned32
_Hh3cIfQoSLRCbs_Object = MibTableColumn
hh3cIfQoSLRCbs = _Hh3cIfQoSLRCbs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 3, 1, 1, 3),
    _Hh3cIfQoSLRCbs_Type()
)
hh3cIfQoSLRCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSLRCbs.setStatus("current")
_Hh3cIfQoSLREbs_Type = Unsigned32
_Hh3cIfQoSLREbs_Object = MibTableColumn
hh3cIfQoSLREbs = _Hh3cIfQoSLREbs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 3, 1, 1, 4),
    _Hh3cIfQoSLREbs_Type()
)
hh3cIfQoSLREbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSLREbs.setStatus("current")
_Hh3cIfQoSRowStatus_Type = RowStatus
_Hh3cIfQoSRowStatus_Object = MibTableColumn
hh3cIfQoSRowStatus = _Hh3cIfQoSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 3, 1, 1, 5),
    _Hh3cIfQoSRowStatus_Type()
)
hh3cIfQoSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSRowStatus.setStatus("current")
_Hh3cIfQoSLRRunInfoTable_Object = MibTable
hh3cIfQoSLRRunInfoTable = _Hh3cIfQoSLRRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cIfQoSLRRunInfoTable.setStatus("current")
_Hh3cIfQoSLRRunInfoEntry_Object = MibTableRow
hh3cIfQoSLRRunInfoEntry = _Hh3cIfQoSLRRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 3, 2, 1)
)
hh3cIfQoSLRRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSLRDirection"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSLRRunInfoEntry.setStatus("current")
_Hh3cIfQoSLRRunInfoPassedPackets_Type = Counter64
_Hh3cIfQoSLRRunInfoPassedPackets_Object = MibTableColumn
hh3cIfQoSLRRunInfoPassedPackets = _Hh3cIfQoSLRRunInfoPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 3, 2, 1, 1),
    _Hh3cIfQoSLRRunInfoPassedPackets_Type()
)
hh3cIfQoSLRRunInfoPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSLRRunInfoPassedPackets.setStatus("current")
_Hh3cIfQoSLRRunInfoPassedBytes_Type = Counter64
_Hh3cIfQoSLRRunInfoPassedBytes_Object = MibTableColumn
hh3cIfQoSLRRunInfoPassedBytes = _Hh3cIfQoSLRRunInfoPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 3, 2, 1, 2),
    _Hh3cIfQoSLRRunInfoPassedBytes_Type()
)
hh3cIfQoSLRRunInfoPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSLRRunInfoPassedBytes.setStatus("current")
_Hh3cIfQoSLRRunInfoDelayedPackets_Type = Counter64
_Hh3cIfQoSLRRunInfoDelayedPackets_Object = MibTableColumn
hh3cIfQoSLRRunInfoDelayedPackets = _Hh3cIfQoSLRRunInfoDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 3, 2, 1, 3),
    _Hh3cIfQoSLRRunInfoDelayedPackets_Type()
)
hh3cIfQoSLRRunInfoDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSLRRunInfoDelayedPackets.setStatus("current")
_Hh3cIfQoSLRRunInfoDelayedBytes_Type = Counter64
_Hh3cIfQoSLRRunInfoDelayedBytes_Object = MibTableColumn
hh3cIfQoSLRRunInfoDelayedBytes = _Hh3cIfQoSLRRunInfoDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 3, 2, 1, 4),
    _Hh3cIfQoSLRRunInfoDelayedBytes_Type()
)
hh3cIfQoSLRRunInfoDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSLRRunInfoDelayedBytes.setStatus("current")


class _Hh3cIfQoSLRRunInfoActiveShaping_Type(Integer32):
    """Custom type hh3cIfQoSLRRunInfoActiveShaping based on Integer32"""
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


_Hh3cIfQoSLRRunInfoActiveShaping_Type.__name__ = "Integer32"
_Hh3cIfQoSLRRunInfoActiveShaping_Object = MibTableColumn
hh3cIfQoSLRRunInfoActiveShaping = _Hh3cIfQoSLRRunInfoActiveShaping_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 3, 2, 1, 5),
    _Hh3cIfQoSLRRunInfoActiveShaping_Type()
)
hh3cIfQoSLRRunInfoActiveShaping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSLRRunInfoActiveShaping.setStatus("current")
_Hh3cIfQoSCARObjects_ObjectIdentity = ObjectIdentity
hh3cIfQoSCARObjects = _Hh3cIfQoSCARObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4)
)
_Hh3cIfQoSAggregativeCarGroup_ObjectIdentity = ObjectIdentity
hh3cIfQoSAggregativeCarGroup = _Hh3cIfQoSAggregativeCarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1)
)
_Hh3cIfQoSAggregativeCarNextIndex_Type = Integer32
_Hh3cIfQoSAggregativeCarNextIndex_Object = MibScalar
hh3cIfQoSAggregativeCarNextIndex = _Hh3cIfQoSAggregativeCarNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 1),
    _Hh3cIfQoSAggregativeCarNextIndex_Type()
)
hh3cIfQoSAggregativeCarNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarNextIndex.setStatus("current")
_Hh3cIfQoSAggregativeCarConfigTable_Object = MibTable
hh3cIfQoSAggregativeCarConfigTable = _Hh3cIfQoSAggregativeCarConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarConfigTable.setStatus("current")
_Hh3cIfQoSAggregativeCarConfigEntry_Object = MibTableRow
hh3cIfQoSAggregativeCarConfigEntry = _Hh3cIfQoSAggregativeCarConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 2, 1)
)
hh3cIfQoSAggregativeCarConfigEntry.setIndexNames(
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSAggregativeCarIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarConfigEntry.setStatus("current")


class _Hh3cIfQoSAggregativeCarIndex_Type(Integer32):
    """Custom type hh3cIfQoSAggregativeCarIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_Hh3cIfQoSAggregativeCarIndex_Type.__name__ = "Integer32"
_Hh3cIfQoSAggregativeCarIndex_Object = MibTableColumn
hh3cIfQoSAggregativeCarIndex = _Hh3cIfQoSAggregativeCarIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 2, 1, 1),
    _Hh3cIfQoSAggregativeCarIndex_Type()
)
hh3cIfQoSAggregativeCarIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarIndex.setStatus("current")


class _Hh3cIfQoSAggregativeCarName_Type(OctetString):
    """Custom type hh3cIfQoSAggregativeCarName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cIfQoSAggregativeCarName_Type.__name__ = "OctetString"
_Hh3cIfQoSAggregativeCarName_Object = MibTableColumn
hh3cIfQoSAggregativeCarName = _Hh3cIfQoSAggregativeCarName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 2, 1, 2),
    _Hh3cIfQoSAggregativeCarName_Type()
)
hh3cIfQoSAggregativeCarName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarName.setStatus("current")
_Hh3cIfQoSAggregativeCarCir_Type = Unsigned32
_Hh3cIfQoSAggregativeCarCir_Object = MibTableColumn
hh3cIfQoSAggregativeCarCir = _Hh3cIfQoSAggregativeCarCir_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 2, 1, 3),
    _Hh3cIfQoSAggregativeCarCir_Type()
)
hh3cIfQoSAggregativeCarCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarCir.setStatus("current")
_Hh3cIfQoSAggregativeCarCbs_Type = Unsigned32
_Hh3cIfQoSAggregativeCarCbs_Object = MibTableColumn
hh3cIfQoSAggregativeCarCbs = _Hh3cIfQoSAggregativeCarCbs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 2, 1, 4),
    _Hh3cIfQoSAggregativeCarCbs_Type()
)
hh3cIfQoSAggregativeCarCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarCbs.setStatus("current")
_Hh3cIfQoSAggregativeCarEbs_Type = Unsigned32
_Hh3cIfQoSAggregativeCarEbs_Object = MibTableColumn
hh3cIfQoSAggregativeCarEbs = _Hh3cIfQoSAggregativeCarEbs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 2, 1, 5),
    _Hh3cIfQoSAggregativeCarEbs_Type()
)
hh3cIfQoSAggregativeCarEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarEbs.setStatus("current")
_Hh3cIfQoSAggregativeCarPir_Type = Unsigned32
_Hh3cIfQoSAggregativeCarPir_Object = MibTableColumn
hh3cIfQoSAggregativeCarPir = _Hh3cIfQoSAggregativeCarPir_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 2, 1, 6),
    _Hh3cIfQoSAggregativeCarPir_Type()
)
hh3cIfQoSAggregativeCarPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarPir.setStatus("current")


class _Hh3cIfQoSAggregativeCarGreenActionType_Type(CarAction):
    """Custom type hh3cIfQoSAggregativeCarGreenActionType based on CarAction"""


_Hh3cIfQoSAggregativeCarGreenActionType_Object = MibTableColumn
hh3cIfQoSAggregativeCarGreenActionType = _Hh3cIfQoSAggregativeCarGreenActionType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 2, 1, 7),
    _Hh3cIfQoSAggregativeCarGreenActionType_Type()
)
hh3cIfQoSAggregativeCarGreenActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarGreenActionType.setStatus("current")


class _Hh3cIfQoSAggregativeCarGreenActionValue_Type(Integer32):
    """Custom type hh3cIfQoSAggregativeCarGreenActionValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_Hh3cIfQoSAggregativeCarGreenActionValue_Type.__name__ = "Integer32"
_Hh3cIfQoSAggregativeCarGreenActionValue_Object = MibTableColumn
hh3cIfQoSAggregativeCarGreenActionValue = _Hh3cIfQoSAggregativeCarGreenActionValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 2, 1, 8),
    _Hh3cIfQoSAggregativeCarGreenActionValue_Type()
)
hh3cIfQoSAggregativeCarGreenActionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarGreenActionValue.setStatus("current")
_Hh3cIfQoSAggregativeCarYellowActionType_Type = CarAction
_Hh3cIfQoSAggregativeCarYellowActionType_Object = MibTableColumn
hh3cIfQoSAggregativeCarYellowActionType = _Hh3cIfQoSAggregativeCarYellowActionType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 2, 1, 9),
    _Hh3cIfQoSAggregativeCarYellowActionType_Type()
)
hh3cIfQoSAggregativeCarYellowActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarYellowActionType.setStatus("current")


class _Hh3cIfQoSAggregativeCarYellowActionValue_Type(Integer32):
    """Custom type hh3cIfQoSAggregativeCarYellowActionValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_Hh3cIfQoSAggregativeCarYellowActionValue_Type.__name__ = "Integer32"
_Hh3cIfQoSAggregativeCarYellowActionValue_Object = MibTableColumn
hh3cIfQoSAggregativeCarYellowActionValue = _Hh3cIfQoSAggregativeCarYellowActionValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 2, 1, 10),
    _Hh3cIfQoSAggregativeCarYellowActionValue_Type()
)
hh3cIfQoSAggregativeCarYellowActionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarYellowActionValue.setStatus("current")
_Hh3cIfQoSAggregativeCarRedActionType_Type = CarAction
_Hh3cIfQoSAggregativeCarRedActionType_Object = MibTableColumn
hh3cIfQoSAggregativeCarRedActionType = _Hh3cIfQoSAggregativeCarRedActionType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 2, 1, 11),
    _Hh3cIfQoSAggregativeCarRedActionType_Type()
)
hh3cIfQoSAggregativeCarRedActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarRedActionType.setStatus("current")
_Hh3cIfQoSAggregativeCarRedActionValue_Type = Integer32
_Hh3cIfQoSAggregativeCarRedActionValue_Object = MibTableColumn
hh3cIfQoSAggregativeCarRedActionValue = _Hh3cIfQoSAggregativeCarRedActionValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 2, 1, 12),
    _Hh3cIfQoSAggregativeCarRedActionValue_Type()
)
hh3cIfQoSAggregativeCarRedActionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarRedActionValue.setStatus("current")


class _Hh3cIfQoSAggregativeCarType_Type(Integer32):
    """Custom type hh3cIfQoSAggregativeCarType based on Integer32"""
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


_Hh3cIfQoSAggregativeCarType_Type.__name__ = "Integer32"
_Hh3cIfQoSAggregativeCarType_Object = MibTableColumn
hh3cIfQoSAggregativeCarType = _Hh3cIfQoSAggregativeCarType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 2, 1, 13),
    _Hh3cIfQoSAggregativeCarType_Type()
)
hh3cIfQoSAggregativeCarType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarType.setStatus("current")
_Hh3cIfQoSAggregativeCarRowStatus_Type = RowStatus
_Hh3cIfQoSAggregativeCarRowStatus_Object = MibTableColumn
hh3cIfQoSAggregativeCarRowStatus = _Hh3cIfQoSAggregativeCarRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 2, 1, 14),
    _Hh3cIfQoSAggregativeCarRowStatus_Type()
)
hh3cIfQoSAggregativeCarRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarRowStatus.setStatus("current")
_Hh3cIfQoSAggregativeCarApplyTable_Object = MibTable
hh3cIfQoSAggregativeCarApplyTable = _Hh3cIfQoSAggregativeCarApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarApplyTable.setStatus("current")
_Hh3cIfQoSAggregativeCarApplyEntry_Object = MibTableRow
hh3cIfQoSAggregativeCarApplyEntry = _Hh3cIfQoSAggregativeCarApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 3, 1)
)
hh3cIfQoSAggregativeCarApplyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSAggregativeCarApplyDirection"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSAggregativeCarApplyRuleType"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSAggregativeCarApplyRuleValue"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarApplyEntry.setStatus("current")
_Hh3cIfQoSAggregativeCarApplyDirection_Type = Direction
_Hh3cIfQoSAggregativeCarApplyDirection_Object = MibTableColumn
hh3cIfQoSAggregativeCarApplyDirection = _Hh3cIfQoSAggregativeCarApplyDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 3, 1, 1),
    _Hh3cIfQoSAggregativeCarApplyDirection_Type()
)
hh3cIfQoSAggregativeCarApplyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarApplyDirection.setStatus("current")


class _Hh3cIfQoSAggregativeCarApplyRuleType_Type(Integer32):
    """Custom type hh3cIfQoSAggregativeCarApplyRuleType based on Integer32"""
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


_Hh3cIfQoSAggregativeCarApplyRuleType_Type.__name__ = "Integer32"
_Hh3cIfQoSAggregativeCarApplyRuleType_Object = MibTableColumn
hh3cIfQoSAggregativeCarApplyRuleType = _Hh3cIfQoSAggregativeCarApplyRuleType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 3, 1, 2),
    _Hh3cIfQoSAggregativeCarApplyRuleType_Type()
)
hh3cIfQoSAggregativeCarApplyRuleType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarApplyRuleType.setStatus("current")
_Hh3cIfQoSAggregativeCarApplyRuleValue_Type = Integer32
_Hh3cIfQoSAggregativeCarApplyRuleValue_Object = MibTableColumn
hh3cIfQoSAggregativeCarApplyRuleValue = _Hh3cIfQoSAggregativeCarApplyRuleValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 3, 1, 3),
    _Hh3cIfQoSAggregativeCarApplyRuleValue_Type()
)
hh3cIfQoSAggregativeCarApplyRuleValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarApplyRuleValue.setStatus("current")
_Hh3cIfQoSAggregativeCarApplyCarIndex_Type = Integer32
_Hh3cIfQoSAggregativeCarApplyCarIndex_Object = MibTableColumn
hh3cIfQoSAggregativeCarApplyCarIndex = _Hh3cIfQoSAggregativeCarApplyCarIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 3, 1, 4),
    _Hh3cIfQoSAggregativeCarApplyCarIndex_Type()
)
hh3cIfQoSAggregativeCarApplyCarIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarApplyCarIndex.setStatus("current")
_Hh3cIfQoSAggregativeCarApplyRowStatus_Type = RowStatus
_Hh3cIfQoSAggregativeCarApplyRowStatus_Object = MibTableColumn
hh3cIfQoSAggregativeCarApplyRowStatus = _Hh3cIfQoSAggregativeCarApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 3, 1, 5),
    _Hh3cIfQoSAggregativeCarApplyRowStatus_Type()
)
hh3cIfQoSAggregativeCarApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarApplyRowStatus.setStatus("current")
_Hh3cIfQoSAggregativeCarRunInfoTable_Object = MibTable
hh3cIfQoSAggregativeCarRunInfoTable = _Hh3cIfQoSAggregativeCarRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarRunInfoTable.setStatus("current")
_Hh3cIfQoSAggregativeCarRunInfoEntry_Object = MibTableRow
hh3cIfQoSAggregativeCarRunInfoEntry = _Hh3cIfQoSAggregativeCarRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 4, 1)
)
hh3cIfQoSAggregativeCarRunInfoEntry.setIndexNames(
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSAggregativeCarIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarRunInfoEntry.setStatus("current")
_Hh3cIfQoSAggregativeCarGreenPackets_Type = Counter64
_Hh3cIfQoSAggregativeCarGreenPackets_Object = MibTableColumn
hh3cIfQoSAggregativeCarGreenPackets = _Hh3cIfQoSAggregativeCarGreenPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 4, 1, 1),
    _Hh3cIfQoSAggregativeCarGreenPackets_Type()
)
hh3cIfQoSAggregativeCarGreenPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarGreenPackets.setStatus("current")
_Hh3cIfQoSAggregativeCarGreenBytes_Type = Counter64
_Hh3cIfQoSAggregativeCarGreenBytes_Object = MibTableColumn
hh3cIfQoSAggregativeCarGreenBytes = _Hh3cIfQoSAggregativeCarGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 4, 1, 2),
    _Hh3cIfQoSAggregativeCarGreenBytes_Type()
)
hh3cIfQoSAggregativeCarGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarGreenBytes.setStatus("current")
_Hh3cIfQoSAggregativeCarYellowPackets_Type = Counter64
_Hh3cIfQoSAggregativeCarYellowPackets_Object = MibTableColumn
hh3cIfQoSAggregativeCarYellowPackets = _Hh3cIfQoSAggregativeCarYellowPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 4, 1, 3),
    _Hh3cIfQoSAggregativeCarYellowPackets_Type()
)
hh3cIfQoSAggregativeCarYellowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarYellowPackets.setStatus("current")
_Hh3cIfQoSAggregativeCarYellowBytes_Type = Counter64
_Hh3cIfQoSAggregativeCarYellowBytes_Object = MibTableColumn
hh3cIfQoSAggregativeCarYellowBytes = _Hh3cIfQoSAggregativeCarYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 4, 1, 4),
    _Hh3cIfQoSAggregativeCarYellowBytes_Type()
)
hh3cIfQoSAggregativeCarYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarYellowBytes.setStatus("current")
_Hh3cIfQoSAggregativeCarRedPackets_Type = Counter64
_Hh3cIfQoSAggregativeCarRedPackets_Object = MibTableColumn
hh3cIfQoSAggregativeCarRedPackets = _Hh3cIfQoSAggregativeCarRedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 4, 1, 5),
    _Hh3cIfQoSAggregativeCarRedPackets_Type()
)
hh3cIfQoSAggregativeCarRedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarRedPackets.setStatus("current")
_Hh3cIfQoSAggregativeCarRedBytes_Type = Counter64
_Hh3cIfQoSAggregativeCarRedBytes_Object = MibTableColumn
hh3cIfQoSAggregativeCarRedBytes = _Hh3cIfQoSAggregativeCarRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 1, 4, 1, 6),
    _Hh3cIfQoSAggregativeCarRedBytes_Type()
)
hh3cIfQoSAggregativeCarRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSAggregativeCarRedBytes.setStatus("current")
_Hh3cIfQoSTricolorCarGroup_ObjectIdentity = ObjectIdentity
hh3cIfQoSTricolorCarGroup = _Hh3cIfQoSTricolorCarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 2)
)
_Hh3cIfQoSTricolorCarConfigTable_Object = MibTable
hh3cIfQoSTricolorCarConfigTable = _Hh3cIfQoSTricolorCarConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cIfQoSTricolorCarConfigTable.setStatus("current")
_Hh3cIfQoSTricolorCarConfigEntry_Object = MibTableRow
hh3cIfQoSTricolorCarConfigEntry = _Hh3cIfQoSTricolorCarConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 2, 1, 1)
)
hh3cIfQoSTricolorCarConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSTricolorCarDirection"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSTricolorCarType"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSTricolorCarValue"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSTricolorCarConfigEntry.setStatus("current")
_Hh3cIfQoSTricolorCarDirection_Type = Direction
_Hh3cIfQoSTricolorCarDirection_Object = MibTableColumn
hh3cIfQoSTricolorCarDirection = _Hh3cIfQoSTricolorCarDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 2, 1, 1, 1),
    _Hh3cIfQoSTricolorCarDirection_Type()
)
hh3cIfQoSTricolorCarDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfQoSTricolorCarDirection.setStatus("current")


class _Hh3cIfQoSTricolorCarType_Type(Integer32):
    """Custom type hh3cIfQoSTricolorCarType based on Integer32"""
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


_Hh3cIfQoSTricolorCarType_Type.__name__ = "Integer32"
_Hh3cIfQoSTricolorCarType_Object = MibTableColumn
hh3cIfQoSTricolorCarType = _Hh3cIfQoSTricolorCarType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 2, 1, 1, 2),
    _Hh3cIfQoSTricolorCarType_Type()
)
hh3cIfQoSTricolorCarType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfQoSTricolorCarType.setStatus("current")
_Hh3cIfQoSTricolorCarValue_Type = Integer32
_Hh3cIfQoSTricolorCarValue_Object = MibTableColumn
hh3cIfQoSTricolorCarValue = _Hh3cIfQoSTricolorCarValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 2, 1, 1, 3),
    _Hh3cIfQoSTricolorCarValue_Type()
)
hh3cIfQoSTricolorCarValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfQoSTricolorCarValue.setStatus("current")
_Hh3cIfQoSTricolorCarCir_Type = Unsigned32
_Hh3cIfQoSTricolorCarCir_Object = MibTableColumn
hh3cIfQoSTricolorCarCir = _Hh3cIfQoSTricolorCarCir_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 2, 1, 1, 4),
    _Hh3cIfQoSTricolorCarCir_Type()
)
hh3cIfQoSTricolorCarCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSTricolorCarCir.setStatus("current")
_Hh3cIfQoSTricolorCarCbs_Type = Unsigned32
_Hh3cIfQoSTricolorCarCbs_Object = MibTableColumn
hh3cIfQoSTricolorCarCbs = _Hh3cIfQoSTricolorCarCbs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 2, 1, 1, 5),
    _Hh3cIfQoSTricolorCarCbs_Type()
)
hh3cIfQoSTricolorCarCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSTricolorCarCbs.setStatus("current")
_Hh3cIfQoSTricolorCarEbs_Type = Unsigned32
_Hh3cIfQoSTricolorCarEbs_Object = MibTableColumn
hh3cIfQoSTricolorCarEbs = _Hh3cIfQoSTricolorCarEbs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 2, 1, 1, 6),
    _Hh3cIfQoSTricolorCarEbs_Type()
)
hh3cIfQoSTricolorCarEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSTricolorCarEbs.setStatus("current")
_Hh3cIfQoSTricolorCarPir_Type = Unsigned32
_Hh3cIfQoSTricolorCarPir_Object = MibTableColumn
hh3cIfQoSTricolorCarPir = _Hh3cIfQoSTricolorCarPir_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 2, 1, 1, 7),
    _Hh3cIfQoSTricolorCarPir_Type()
)
hh3cIfQoSTricolorCarPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSTricolorCarPir.setStatus("current")


class _Hh3cIfQoSTricolorCarGreenActionType_Type(CarAction):
    """Custom type hh3cIfQoSTricolorCarGreenActionType based on CarAction"""


_Hh3cIfQoSTricolorCarGreenActionType_Object = MibTableColumn
hh3cIfQoSTricolorCarGreenActionType = _Hh3cIfQoSTricolorCarGreenActionType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 2, 1, 1, 8),
    _Hh3cIfQoSTricolorCarGreenActionType_Type()
)
hh3cIfQoSTricolorCarGreenActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSTricolorCarGreenActionType.setStatus("current")


class _Hh3cIfQoSTricolorCarGreenActionValue_Type(Integer32):
    """Custom type hh3cIfQoSTricolorCarGreenActionValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_Hh3cIfQoSTricolorCarGreenActionValue_Type.__name__ = "Integer32"
_Hh3cIfQoSTricolorCarGreenActionValue_Object = MibTableColumn
hh3cIfQoSTricolorCarGreenActionValue = _Hh3cIfQoSTricolorCarGreenActionValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 2, 1, 1, 9),
    _Hh3cIfQoSTricolorCarGreenActionValue_Type()
)
hh3cIfQoSTricolorCarGreenActionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSTricolorCarGreenActionValue.setStatus("current")


class _Hh3cIfQoSTricolorCarYellowActionType_Type(CarAction):
    """Custom type hh3cIfQoSTricolorCarYellowActionType based on CarAction"""


_Hh3cIfQoSTricolorCarYellowActionType_Object = MibTableColumn
hh3cIfQoSTricolorCarYellowActionType = _Hh3cIfQoSTricolorCarYellowActionType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 2, 1, 1, 10),
    _Hh3cIfQoSTricolorCarYellowActionType_Type()
)
hh3cIfQoSTricolorCarYellowActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSTricolorCarYellowActionType.setStatus("current")


class _Hh3cIfQoSTricolorCarYellowActionValue_Type(Integer32):
    """Custom type hh3cIfQoSTricolorCarYellowActionValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_Hh3cIfQoSTricolorCarYellowActionValue_Type.__name__ = "Integer32"
_Hh3cIfQoSTricolorCarYellowActionValue_Object = MibTableColumn
hh3cIfQoSTricolorCarYellowActionValue = _Hh3cIfQoSTricolorCarYellowActionValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 2, 1, 1, 11),
    _Hh3cIfQoSTricolorCarYellowActionValue_Type()
)
hh3cIfQoSTricolorCarYellowActionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSTricolorCarYellowActionValue.setStatus("current")


class _Hh3cIfQoSTricolorCarRedActionType_Type(CarAction):
    """Custom type hh3cIfQoSTricolorCarRedActionType based on CarAction"""


_Hh3cIfQoSTricolorCarRedActionType_Object = MibTableColumn
hh3cIfQoSTricolorCarRedActionType = _Hh3cIfQoSTricolorCarRedActionType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 2, 1, 1, 12),
    _Hh3cIfQoSTricolorCarRedActionType_Type()
)
hh3cIfQoSTricolorCarRedActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSTricolorCarRedActionType.setStatus("current")


class _Hh3cIfQoSTricolorCarRedActionValue_Type(Integer32):
    """Custom type hh3cIfQoSTricolorCarRedActionValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_Hh3cIfQoSTricolorCarRedActionValue_Type.__name__ = "Integer32"
_Hh3cIfQoSTricolorCarRedActionValue_Object = MibTableColumn
hh3cIfQoSTricolorCarRedActionValue = _Hh3cIfQoSTricolorCarRedActionValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 2, 1, 1, 13),
    _Hh3cIfQoSTricolorCarRedActionValue_Type()
)
hh3cIfQoSTricolorCarRedActionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSTricolorCarRedActionValue.setStatus("current")
_Hh3cIfQoSTricolorCarRowStatus_Type = RowStatus
_Hh3cIfQoSTricolorCarRowStatus_Object = MibTableColumn
hh3cIfQoSTricolorCarRowStatus = _Hh3cIfQoSTricolorCarRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 2, 1, 1, 14),
    _Hh3cIfQoSTricolorCarRowStatus_Type()
)
hh3cIfQoSTricolorCarRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSTricolorCarRowStatus.setStatus("current")
_Hh3cIfQoSTricolorCarRunInfoTable_Object = MibTable
hh3cIfQoSTricolorCarRunInfoTable = _Hh3cIfQoSTricolorCarRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cIfQoSTricolorCarRunInfoTable.setStatus("current")
_Hh3cIfQoSTricolorCarRunInfoEntry_Object = MibTableRow
hh3cIfQoSTricolorCarRunInfoEntry = _Hh3cIfQoSTricolorCarRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 2, 2, 1)
)
hh3cIfQoSTricolorCarRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSTricolorCarDirection"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSTricolorCarType"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSTricolorCarValue"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSTricolorCarRunInfoEntry.setStatus("current")
_Hh3cIfQoSTricolorCarGreenPackets_Type = Counter64
_Hh3cIfQoSTricolorCarGreenPackets_Object = MibTableColumn
hh3cIfQoSTricolorCarGreenPackets = _Hh3cIfQoSTricolorCarGreenPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 2, 2, 1, 1),
    _Hh3cIfQoSTricolorCarGreenPackets_Type()
)
hh3cIfQoSTricolorCarGreenPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSTricolorCarGreenPackets.setStatus("current")
_Hh3cIfQoSTricolorCarGreenBytes_Type = Counter64
_Hh3cIfQoSTricolorCarGreenBytes_Object = MibTableColumn
hh3cIfQoSTricolorCarGreenBytes = _Hh3cIfQoSTricolorCarGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 2, 2, 1, 2),
    _Hh3cIfQoSTricolorCarGreenBytes_Type()
)
hh3cIfQoSTricolorCarGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSTricolorCarGreenBytes.setStatus("current")
_Hh3cIfQoSTricolorCarYellowPackets_Type = Counter64
_Hh3cIfQoSTricolorCarYellowPackets_Object = MibTableColumn
hh3cIfQoSTricolorCarYellowPackets = _Hh3cIfQoSTricolorCarYellowPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 2, 2, 1, 3),
    _Hh3cIfQoSTricolorCarYellowPackets_Type()
)
hh3cIfQoSTricolorCarYellowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSTricolorCarYellowPackets.setStatus("current")
_Hh3cIfQoSTricolorCarYellowBytes_Type = Counter64
_Hh3cIfQoSTricolorCarYellowBytes_Object = MibTableColumn
hh3cIfQoSTricolorCarYellowBytes = _Hh3cIfQoSTricolorCarYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 2, 2, 1, 4),
    _Hh3cIfQoSTricolorCarYellowBytes_Type()
)
hh3cIfQoSTricolorCarYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSTricolorCarYellowBytes.setStatus("current")
_Hh3cIfQoSTricolorCarRedPackets_Type = Counter64
_Hh3cIfQoSTricolorCarRedPackets_Object = MibTableColumn
hh3cIfQoSTricolorCarRedPackets = _Hh3cIfQoSTricolorCarRedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 2, 2, 1, 5),
    _Hh3cIfQoSTricolorCarRedPackets_Type()
)
hh3cIfQoSTricolorCarRedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSTricolorCarRedPackets.setStatus("current")
_Hh3cIfQoSTricolorCarRedBytes_Type = Counter64
_Hh3cIfQoSTricolorCarRedBytes_Object = MibTableColumn
hh3cIfQoSTricolorCarRedBytes = _Hh3cIfQoSTricolorCarRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 4, 2, 2, 1, 6),
    _Hh3cIfQoSTricolorCarRedBytes_Type()
)
hh3cIfQoSTricolorCarRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSTricolorCarRedBytes.setStatus("current")
_Hh3cIfQoSGTSObjects_ObjectIdentity = ObjectIdentity
hh3cIfQoSGTSObjects = _Hh3cIfQoSGTSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 5)
)
_Hh3cIfQoSGTSConfigTable_Object = MibTable
hh3cIfQoSGTSConfigTable = _Hh3cIfQoSGTSConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hh3cIfQoSGTSConfigTable.setStatus("current")
_Hh3cIfQoSGTSConfigEntry_Object = MibTableRow
hh3cIfQoSGTSConfigEntry = _Hh3cIfQoSGTSConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 5, 1, 1)
)
hh3cIfQoSGTSConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSGTSClassRuleType"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSGTSClassRuleValue"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSGTSConfigEntry.setStatus("current")


class _Hh3cIfQoSGTSClassRuleType_Type(Integer32):
    """Custom type hh3cIfQoSGTSClassRuleType based on Integer32"""
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


_Hh3cIfQoSGTSClassRuleType_Type.__name__ = "Integer32"
_Hh3cIfQoSGTSClassRuleType_Object = MibTableColumn
hh3cIfQoSGTSClassRuleType = _Hh3cIfQoSGTSClassRuleType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 5, 1, 1, 1),
    _Hh3cIfQoSGTSClassRuleType_Type()
)
hh3cIfQoSGTSClassRuleType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfQoSGTSClassRuleType.setStatus("current")
_Hh3cIfQoSGTSClassRuleValue_Type = Integer32
_Hh3cIfQoSGTSClassRuleValue_Object = MibTableColumn
hh3cIfQoSGTSClassRuleValue = _Hh3cIfQoSGTSClassRuleValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 5, 1, 1, 2),
    _Hh3cIfQoSGTSClassRuleValue_Type()
)
hh3cIfQoSGTSClassRuleValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfQoSGTSClassRuleValue.setStatus("current")
_Hh3cIfQoSGTSCir_Type = Unsigned32
_Hh3cIfQoSGTSCir_Object = MibTableColumn
hh3cIfQoSGTSCir = _Hh3cIfQoSGTSCir_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 5, 1, 1, 3),
    _Hh3cIfQoSGTSCir_Type()
)
hh3cIfQoSGTSCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSGTSCir.setStatus("current")
_Hh3cIfQoSGTSCbs_Type = Unsigned32
_Hh3cIfQoSGTSCbs_Object = MibTableColumn
hh3cIfQoSGTSCbs = _Hh3cIfQoSGTSCbs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 5, 1, 1, 4),
    _Hh3cIfQoSGTSCbs_Type()
)
hh3cIfQoSGTSCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSGTSCbs.setStatus("current")
_Hh3cIfQoSGTSEbs_Type = Unsigned32
_Hh3cIfQoSGTSEbs_Object = MibTableColumn
hh3cIfQoSGTSEbs = _Hh3cIfQoSGTSEbs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 5, 1, 1, 5),
    _Hh3cIfQoSGTSEbs_Type()
)
hh3cIfQoSGTSEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSGTSEbs.setStatus("current")
_Hh3cIfQoSGTSQueueLength_Type = Integer32
_Hh3cIfQoSGTSQueueLength_Object = MibTableColumn
hh3cIfQoSGTSQueueLength = _Hh3cIfQoSGTSQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 5, 1, 1, 6),
    _Hh3cIfQoSGTSQueueLength_Type()
)
hh3cIfQoSGTSQueueLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSGTSQueueLength.setStatus("current")
_Hh3cIfQoSGTSConfigRowStatus_Type = RowStatus
_Hh3cIfQoSGTSConfigRowStatus_Object = MibTableColumn
hh3cIfQoSGTSConfigRowStatus = _Hh3cIfQoSGTSConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 5, 1, 1, 7),
    _Hh3cIfQoSGTSConfigRowStatus_Type()
)
hh3cIfQoSGTSConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSGTSConfigRowStatus.setStatus("current")
_Hh3cIfQoSGTSRunInfoTable_Object = MibTable
hh3cIfQoSGTSRunInfoTable = _Hh3cIfQoSGTSRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 5, 2)
)
if mibBuilder.loadTexts:
    hh3cIfQoSGTSRunInfoTable.setStatus("current")
_Hh3cIfQoSGTSRunInfoEntry_Object = MibTableRow
hh3cIfQoSGTSRunInfoEntry = _Hh3cIfQoSGTSRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 5, 2, 1)
)
hh3cIfQoSGTSRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSGTSClassRuleType"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSGTSClassRuleValue"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSGTSRunInfoEntry.setStatus("current")
_Hh3cIfQoSGTSQueueSize_Type = Integer32
_Hh3cIfQoSGTSQueueSize_Object = MibTableColumn
hh3cIfQoSGTSQueueSize = _Hh3cIfQoSGTSQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 5, 2, 1, 1),
    _Hh3cIfQoSGTSQueueSize_Type()
)
hh3cIfQoSGTSQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSGTSQueueSize.setStatus("current")
_Hh3cIfQoSGTSPassedPackets_Type = Counter64
_Hh3cIfQoSGTSPassedPackets_Object = MibTableColumn
hh3cIfQoSGTSPassedPackets = _Hh3cIfQoSGTSPassedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 5, 2, 1, 2),
    _Hh3cIfQoSGTSPassedPackets_Type()
)
hh3cIfQoSGTSPassedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSGTSPassedPackets.setStatus("current")
_Hh3cIfQoSGTSPassedBytes_Type = Counter64
_Hh3cIfQoSGTSPassedBytes_Object = MibTableColumn
hh3cIfQoSGTSPassedBytes = _Hh3cIfQoSGTSPassedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 5, 2, 1, 3),
    _Hh3cIfQoSGTSPassedBytes_Type()
)
hh3cIfQoSGTSPassedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSGTSPassedBytes.setStatus("current")
_Hh3cIfQoSGTSDiscardPackets_Type = Counter64
_Hh3cIfQoSGTSDiscardPackets_Object = MibTableColumn
hh3cIfQoSGTSDiscardPackets = _Hh3cIfQoSGTSDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 5, 2, 1, 4),
    _Hh3cIfQoSGTSDiscardPackets_Type()
)
hh3cIfQoSGTSDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSGTSDiscardPackets.setStatus("current")
_Hh3cIfQoSGTSDiscardBytes_Type = Counter64
_Hh3cIfQoSGTSDiscardBytes_Object = MibTableColumn
hh3cIfQoSGTSDiscardBytes = _Hh3cIfQoSGTSDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 5, 2, 1, 5),
    _Hh3cIfQoSGTSDiscardBytes_Type()
)
hh3cIfQoSGTSDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSGTSDiscardBytes.setStatus("current")
_Hh3cIfQoSGTSDelayedPackets_Type = Counter64
_Hh3cIfQoSGTSDelayedPackets_Object = MibTableColumn
hh3cIfQoSGTSDelayedPackets = _Hh3cIfQoSGTSDelayedPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 5, 2, 1, 6),
    _Hh3cIfQoSGTSDelayedPackets_Type()
)
hh3cIfQoSGTSDelayedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSGTSDelayedPackets.setStatus("current")
_Hh3cIfQoSGTSDelayedBytes_Type = Counter64
_Hh3cIfQoSGTSDelayedBytes_Object = MibTableColumn
hh3cIfQoSGTSDelayedBytes = _Hh3cIfQoSGTSDelayedBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 5, 2, 1, 7),
    _Hh3cIfQoSGTSDelayedBytes_Type()
)
hh3cIfQoSGTSDelayedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSGTSDelayedBytes.setStatus("current")
_Hh3cIfQoSWREDObjects_ObjectIdentity = ObjectIdentity
hh3cIfQoSWREDObjects = _Hh3cIfQoSWREDObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6)
)
_Hh3cIfQoSWredGroupGroup_ObjectIdentity = ObjectIdentity
hh3cIfQoSWredGroupGroup = _Hh3cIfQoSWredGroupGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 1)
)
_Hh3cIfQoSWredGroupNextIndex_Type = Integer32
_Hh3cIfQoSWredGroupNextIndex_Object = MibScalar
hh3cIfQoSWredGroupNextIndex = _Hh3cIfQoSWredGroupNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 1, 1),
    _Hh3cIfQoSWredGroupNextIndex_Type()
)
hh3cIfQoSWredGroupNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWredGroupNextIndex.setStatus("current")
_Hh3cIfQoSWredGroupTable_Object = MibTable
hh3cIfQoSWredGroupTable = _Hh3cIfQoSWredGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cIfQoSWredGroupTable.setStatus("current")
_Hh3cIfQoSWredGroupEntry_Object = MibTableRow
hh3cIfQoSWredGroupEntry = _Hh3cIfQoSWredGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 1, 2, 1)
)
hh3cIfQoSWredGroupEntry.setIndexNames(
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSWredGroupIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSWredGroupEntry.setStatus("current")
_Hh3cIfQoSWredGroupIndex_Type = Integer32
_Hh3cIfQoSWredGroupIndex_Object = MibTableColumn
hh3cIfQoSWredGroupIndex = _Hh3cIfQoSWredGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 1, 2, 1, 1),
    _Hh3cIfQoSWredGroupIndex_Type()
)
hh3cIfQoSWredGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfQoSWredGroupIndex.setStatus("current")


class _Hh3cIfQoSWredGroupName_Type(OctetString):
    """Custom type hh3cIfQoSWredGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cIfQoSWredGroupName_Type.__name__ = "OctetString"
_Hh3cIfQoSWredGroupName_Object = MibTableColumn
hh3cIfQoSWredGroupName = _Hh3cIfQoSWredGroupName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 1, 2, 1, 2),
    _Hh3cIfQoSWredGroupName_Type()
)
hh3cIfQoSWredGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSWredGroupName.setStatus("current")


class _Hh3cIfQoSWredGroupType_Type(Integer32):
    """Custom type hh3cIfQoSWredGroupType based on Integer32"""
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


_Hh3cIfQoSWredGroupType_Type.__name__ = "Integer32"
_Hh3cIfQoSWredGroupType_Object = MibTableColumn
hh3cIfQoSWredGroupType = _Hh3cIfQoSWredGroupType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 1, 2, 1, 3),
    _Hh3cIfQoSWredGroupType_Type()
)
hh3cIfQoSWredGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSWredGroupType.setStatus("current")


class _Hh3cIfQoSWredGroupWeightingConstant_Type(Integer32):
    """Custom type hh3cIfQoSWredGroupWeightingConstant based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Hh3cIfQoSWredGroupWeightingConstant_Type.__name__ = "Integer32"
_Hh3cIfQoSWredGroupWeightingConstant_Object = MibTableColumn
hh3cIfQoSWredGroupWeightingConstant = _Hh3cIfQoSWredGroupWeightingConstant_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 1, 2, 1, 4),
    _Hh3cIfQoSWredGroupWeightingConstant_Type()
)
hh3cIfQoSWredGroupWeightingConstant.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSWredGroupWeightingConstant.setStatus("current")
_Hh3cIfQoSWredGroupRowStatus_Type = RowStatus
_Hh3cIfQoSWredGroupRowStatus_Object = MibTableColumn
hh3cIfQoSWredGroupRowStatus = _Hh3cIfQoSWredGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 1, 2, 1, 6),
    _Hh3cIfQoSWredGroupRowStatus_Type()
)
hh3cIfQoSWredGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSWredGroupRowStatus.setStatus("current")
_Hh3cIfQoSWredGroupContentTable_Object = MibTable
hh3cIfQoSWredGroupContentTable = _Hh3cIfQoSWredGroupContentTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cIfQoSWredGroupContentTable.setStatus("current")
_Hh3cIfQoSWredGroupContentEntry_Object = MibTableRow
hh3cIfQoSWredGroupContentEntry = _Hh3cIfQoSWredGroupContentEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 1, 3, 1)
)
hh3cIfQoSWredGroupContentEntry.setIndexNames(
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSWredGroupIndex"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSWredGroupContentIndex"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSWredGroupContentSubIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSWredGroupContentEntry.setStatus("current")


class _Hh3cIfQoSWredGroupContentIndex_Type(Integer32):
    """Custom type hh3cIfQoSWredGroupContentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Hh3cIfQoSWredGroupContentIndex_Type.__name__ = "Integer32"
_Hh3cIfQoSWredGroupContentIndex_Object = MibTableColumn
hh3cIfQoSWredGroupContentIndex = _Hh3cIfQoSWredGroupContentIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 1, 3, 1, 1),
    _Hh3cIfQoSWredGroupContentIndex_Type()
)
hh3cIfQoSWredGroupContentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfQoSWredGroupContentIndex.setStatus("current")


class _Hh3cIfQoSWredGroupContentSubIndex_Type(Integer32):
    """Custom type hh3cIfQoSWredGroupContentSubIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Hh3cIfQoSWredGroupContentSubIndex_Type.__name__ = "Integer32"
_Hh3cIfQoSWredGroupContentSubIndex_Object = MibTableColumn
hh3cIfQoSWredGroupContentSubIndex = _Hh3cIfQoSWredGroupContentSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 1, 3, 1, 2),
    _Hh3cIfQoSWredGroupContentSubIndex_Type()
)
hh3cIfQoSWredGroupContentSubIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfQoSWredGroupContentSubIndex.setStatus("current")
_Hh3cIfQoSWredLowLimit_Type = Integer32
_Hh3cIfQoSWredLowLimit_Object = MibTableColumn
hh3cIfQoSWredLowLimit = _Hh3cIfQoSWredLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 1, 3, 1, 3),
    _Hh3cIfQoSWredLowLimit_Type()
)
hh3cIfQoSWredLowLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSWredLowLimit.setStatus("current")
_Hh3cIfQoSWredHighLimit_Type = Integer32
_Hh3cIfQoSWredHighLimit_Object = MibTableColumn
hh3cIfQoSWredHighLimit = _Hh3cIfQoSWredHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 1, 3, 1, 4),
    _Hh3cIfQoSWredHighLimit_Type()
)
hh3cIfQoSWredHighLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSWredHighLimit.setStatus("current")
_Hh3cIfQoSWredDiscardProb_Type = Integer32
_Hh3cIfQoSWredDiscardProb_Object = MibTableColumn
hh3cIfQoSWredDiscardProb = _Hh3cIfQoSWredDiscardProb_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 1, 3, 1, 5),
    _Hh3cIfQoSWredDiscardProb_Type()
)
hh3cIfQoSWredDiscardProb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSWredDiscardProb.setStatus("current")


class _Hh3cIfQoSWredGroupExponent_Type(Integer32):
    """Custom type hh3cIfQoSWredGroupExponent based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Hh3cIfQoSWredGroupExponent_Type.__name__ = "Integer32"
_Hh3cIfQoSWredGroupExponent_Object = MibTableColumn
hh3cIfQoSWredGroupExponent = _Hh3cIfQoSWredGroupExponent_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 1, 3, 1, 6),
    _Hh3cIfQoSWredGroupExponent_Type()
)
hh3cIfQoSWredGroupExponent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSWredGroupExponent.setStatus("current")
_Hh3cIfQoSWredRowStatus_Type = RowStatus
_Hh3cIfQoSWredRowStatus_Object = MibTableColumn
hh3cIfQoSWredRowStatus = _Hh3cIfQoSWredRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 1, 3, 1, 7),
    _Hh3cIfQoSWredRowStatus_Type()
)
hh3cIfQoSWredRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSWredRowStatus.setStatus("current")
_Hh3cIfQoSWredGroupApplyIfTable_Object = MibTable
hh3cIfQoSWredGroupApplyIfTable = _Hh3cIfQoSWredGroupApplyIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cIfQoSWredGroupApplyIfTable.setStatus("current")
_Hh3cIfQoSWredGroupApplyIfEntry_Object = MibTableRow
hh3cIfQoSWredGroupApplyIfEntry = _Hh3cIfQoSWredGroupApplyIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 1, 4, 1)
)
hh3cIfQoSWredGroupApplyIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSWredGroupApplyIfEntry.setStatus("current")


class _Hh3cIfQoSWredGroupApplyIndex_Type(Integer32):
    """Custom type hh3cIfQoSWredGroupApplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Hh3cIfQoSWredGroupApplyIndex_Type.__name__ = "Integer32"
_Hh3cIfQoSWredGroupApplyIndex_Object = MibTableColumn
hh3cIfQoSWredGroupApplyIndex = _Hh3cIfQoSWredGroupApplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 1, 4, 1, 1),
    _Hh3cIfQoSWredGroupApplyIndex_Type()
)
hh3cIfQoSWredGroupApplyIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSWredGroupApplyIndex.setStatus("current")
_Hh3cIfQoSWredGroupApplyName_Type = OctetString
_Hh3cIfQoSWredGroupApplyName_Object = MibTableColumn
hh3cIfQoSWredGroupApplyName = _Hh3cIfQoSWredGroupApplyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 1, 4, 1, 2),
    _Hh3cIfQoSWredGroupApplyName_Type()
)
hh3cIfQoSWredGroupApplyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWredGroupApplyName.setStatus("current")
_Hh3cIfQoSWredGroupIfRowStatus_Type = RowStatus
_Hh3cIfQoSWredGroupIfRowStatus_Object = MibTableColumn
hh3cIfQoSWredGroupIfRowStatus = _Hh3cIfQoSWredGroupIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 1, 4, 1, 3),
    _Hh3cIfQoSWredGroupIfRowStatus_Type()
)
hh3cIfQoSWredGroupIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSWredGroupIfRowStatus.setStatus("current")
_Hh3cIfQoSWredApplyIfRunInfoTable_Object = MibTable
hh3cIfQoSWredApplyIfRunInfoTable = _Hh3cIfQoSWredApplyIfRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cIfQoSWredApplyIfRunInfoTable.setStatus("current")
_Hh3cIfQoSWredApplyIfRunInfoEntry_Object = MibTableRow
hh3cIfQoSWredApplyIfRunInfoEntry = _Hh3cIfQoSWredApplyIfRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 1, 5, 1)
)
hh3cIfQoSWredApplyIfRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSWredGroupIndex"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSWredGroupContentIndex"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSWredGroupContentSubIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSWredApplyIfRunInfoEntry.setStatus("current")
_Hh3cIfQoSWredPreRandomDropNum_Type = Counter64
_Hh3cIfQoSWredPreRandomDropNum_Object = MibTableColumn
hh3cIfQoSWredPreRandomDropNum = _Hh3cIfQoSWredPreRandomDropNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 1, 5, 1, 1),
    _Hh3cIfQoSWredPreRandomDropNum_Type()
)
hh3cIfQoSWredPreRandomDropNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWredPreRandomDropNum.setStatus("current")
_Hh3cIfQoSWredPreTailDropNum_Type = Counter64
_Hh3cIfQoSWredPreTailDropNum_Object = MibTableColumn
hh3cIfQoSWredPreTailDropNum = _Hh3cIfQoSWredPreTailDropNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 1, 5, 1, 2),
    _Hh3cIfQoSWredPreTailDropNum_Type()
)
hh3cIfQoSWredPreTailDropNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWredPreTailDropNum.setStatus("current")
_Hh3cIfQoSPortWredGroup_ObjectIdentity = ObjectIdentity
hh3cIfQoSPortWredGroup = _Hh3cIfQoSPortWredGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 2)
)
_Hh3cIfQoSPortWredWeightConstantTable_Object = MibTable
hh3cIfQoSPortWredWeightConstantTable = _Hh3cIfQoSPortWredWeightConstantTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cIfQoSPortWredWeightConstantTable.setStatus("current")
_Hh3cIfQoSPortWredWeightConstantEntry_Object = MibTableRow
hh3cIfQoSPortWredWeightConstantEntry = _Hh3cIfQoSPortWredWeightConstantEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 2, 1, 1)
)
hh3cIfQoSPortWredWeightConstantEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSPortWredWeightConstantEntry.setStatus("current")
_Hh3cIfQoSPortWredEnable_Type = TruthValue
_Hh3cIfQoSPortWredEnable_Object = MibTableColumn
hh3cIfQoSPortWredEnable = _Hh3cIfQoSPortWredEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 2, 1, 1, 1),
    _Hh3cIfQoSPortWredEnable_Type()
)
hh3cIfQoSPortWredEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSPortWredEnable.setStatus("current")


class _Hh3cIfQoSPortWredWeightConstant_Type(Integer32):
    """Custom type hh3cIfQoSPortWredWeightConstant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Hh3cIfQoSPortWredWeightConstant_Type.__name__ = "Integer32"
_Hh3cIfQoSPortWredWeightConstant_Object = MibTableColumn
hh3cIfQoSPortWredWeightConstant = _Hh3cIfQoSPortWredWeightConstant_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 2, 1, 1, 2),
    _Hh3cIfQoSPortWredWeightConstant_Type()
)
hh3cIfQoSPortWredWeightConstant.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSPortWredWeightConstant.setStatus("current")
_Hh3cIfQoSPortWredWeightConstantRowStatus_Type = RowStatus
_Hh3cIfQoSPortWredWeightConstantRowStatus_Object = MibTableColumn
hh3cIfQoSPortWredWeightConstantRowStatus = _Hh3cIfQoSPortWredWeightConstantRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 2, 1, 1, 3),
    _Hh3cIfQoSPortWredWeightConstantRowStatus_Type()
)
hh3cIfQoSPortWredWeightConstantRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSPortWredWeightConstantRowStatus.setStatus("current")
_Hh3cIfQoSPortWredPreConfigTable_Object = MibTable
hh3cIfQoSPortWredPreConfigTable = _Hh3cIfQoSPortWredPreConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cIfQoSPortWredPreConfigTable.setStatus("current")
_Hh3cIfQoSPortWredPreConfigEntry_Object = MibTableRow
hh3cIfQoSPortWredPreConfigEntry = _Hh3cIfQoSPortWredPreConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 2, 2, 1)
)
hh3cIfQoSPortWredPreConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSPortWredPreID"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSPortWredPreConfigEntry.setStatus("current")
_Hh3cIfQoSPortWredPreID_Type = Integer32
_Hh3cIfQoSPortWredPreID_Object = MibTableColumn
hh3cIfQoSPortWredPreID = _Hh3cIfQoSPortWredPreID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 2, 2, 1, 1),
    _Hh3cIfQoSPortWredPreID_Type()
)
hh3cIfQoSPortWredPreID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfQoSPortWredPreID.setStatus("current")
_Hh3cIfQoSPortWredPreLowLimit_Type = Integer32
_Hh3cIfQoSPortWredPreLowLimit_Object = MibTableColumn
hh3cIfQoSPortWredPreLowLimit = _Hh3cIfQoSPortWredPreLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 2, 2, 1, 2),
    _Hh3cIfQoSPortWredPreLowLimit_Type()
)
hh3cIfQoSPortWredPreLowLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSPortWredPreLowLimit.setStatus("current")
_Hh3cIfQoSPortWredPreHighLimit_Type = Integer32
_Hh3cIfQoSPortWredPreHighLimit_Object = MibTableColumn
hh3cIfQoSPortWredPreHighLimit = _Hh3cIfQoSPortWredPreHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 2, 2, 1, 3),
    _Hh3cIfQoSPortWredPreHighLimit_Type()
)
hh3cIfQoSPortWredPreHighLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSPortWredPreHighLimit.setStatus("current")
_Hh3cIfQoSPortWredPreDiscardProbability_Type = Integer32
_Hh3cIfQoSPortWredPreDiscardProbability_Object = MibTableColumn
hh3cIfQoSPortWredPreDiscardProbability = _Hh3cIfQoSPortWredPreDiscardProbability_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 2, 2, 1, 4),
    _Hh3cIfQoSPortWredPreDiscardProbability_Type()
)
hh3cIfQoSPortWredPreDiscardProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSPortWredPreDiscardProbability.setStatus("current")
_Hh3cIfQoSPortWredPreRowStatus_Type = RowStatus
_Hh3cIfQoSPortWredPreRowStatus_Object = MibTableColumn
hh3cIfQoSPortWredPreRowStatus = _Hh3cIfQoSPortWredPreRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 2, 2, 1, 5),
    _Hh3cIfQoSPortWredPreRowStatus_Type()
)
hh3cIfQoSPortWredPreRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSPortWredPreRowStatus.setStatus("current")
_Hh3cIfQoSPortWredRunInfoTable_Object = MibTable
hh3cIfQoSPortWredRunInfoTable = _Hh3cIfQoSPortWredRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cIfQoSPortWredRunInfoTable.setStatus("current")
_Hh3cIfQoSPortWredRunInfoEntry_Object = MibTableRow
hh3cIfQoSPortWredRunInfoEntry = _Hh3cIfQoSPortWredRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 2, 3, 1)
)
hh3cIfQoSPortWredRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSPortWredPreID"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSPortWredRunInfoEntry.setStatus("current")
_Hh3cIfQoSWREDTailDropNum_Type = Counter64
_Hh3cIfQoSWREDTailDropNum_Object = MibTableColumn
hh3cIfQoSWREDTailDropNum = _Hh3cIfQoSWREDTailDropNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 2, 3, 1, 1),
    _Hh3cIfQoSWREDTailDropNum_Type()
)
hh3cIfQoSWREDTailDropNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWREDTailDropNum.setStatus("current")
_Hh3cIfQoSWREDRandomDropNum_Type = Counter64
_Hh3cIfQoSWREDRandomDropNum_Object = MibTableColumn
hh3cIfQoSWREDRandomDropNum = _Hh3cIfQoSWREDRandomDropNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 6, 2, 3, 1, 2),
    _Hh3cIfQoSWREDRandomDropNum_Type()
)
hh3cIfQoSWREDRandomDropNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSWREDRandomDropNum.setStatus("current")
_Hh3cIfQoSPortPriorityObjects_ObjectIdentity = ObjectIdentity
hh3cIfQoSPortPriorityObjects = _Hh3cIfQoSPortPriorityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 7)
)
_Hh3cIfQoSPortPriorityConfigGroup_ObjectIdentity = ObjectIdentity
hh3cIfQoSPortPriorityConfigGroup = _Hh3cIfQoSPortPriorityConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 7, 1)
)
_Hh3cIfQoSPortPriorityTable_Object = MibTable
hh3cIfQoSPortPriorityTable = _Hh3cIfQoSPortPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cIfQoSPortPriorityTable.setStatus("current")
_Hh3cIfQoSPortPriorityEntry_Object = MibTableRow
hh3cIfQoSPortPriorityEntry = _Hh3cIfQoSPortPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 7, 1, 1, 1)
)
hh3cIfQoSPortPriorityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSPortPriorityEntry.setStatus("current")


class _Hh3cIfQoSPortPriorityValue_Type(Integer32):
    """Custom type hh3cIfQoSPortPriorityValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cIfQoSPortPriorityValue_Type.__name__ = "Integer32"
_Hh3cIfQoSPortPriorityValue_Object = MibTableColumn
hh3cIfQoSPortPriorityValue = _Hh3cIfQoSPortPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 7, 1, 1, 1, 1),
    _Hh3cIfQoSPortPriorityValue_Type()
)
hh3cIfQoSPortPriorityValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfQoSPortPriorityValue.setStatus("current")
_Hh3cIfQoSPortPirorityTrustTable_Object = MibTable
hh3cIfQoSPortPirorityTrustTable = _Hh3cIfQoSPortPirorityTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 7, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cIfQoSPortPirorityTrustTable.setStatus("current")
_Hh3cIfQoSPortPirorityTrustEntry_Object = MibTableRow
hh3cIfQoSPortPirorityTrustEntry = _Hh3cIfQoSPortPirorityTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 7, 1, 2, 1)
)
hh3cIfQoSPortPirorityTrustEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSPortPirorityTrustEntry.setStatus("current")


class _Hh3cIfQoSPortPriorityTrustTrustType_Type(Integer32):
    """Custom type hh3cIfQoSPortPriorityTrustTrustType based on Integer32"""
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


_Hh3cIfQoSPortPriorityTrustTrustType_Type.__name__ = "Integer32"
_Hh3cIfQoSPortPriorityTrustTrustType_Object = MibTableColumn
hh3cIfQoSPortPriorityTrustTrustType = _Hh3cIfQoSPortPriorityTrustTrustType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 7, 1, 2, 1, 1),
    _Hh3cIfQoSPortPriorityTrustTrustType_Type()
)
hh3cIfQoSPortPriorityTrustTrustType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfQoSPortPriorityTrustTrustType.setStatus("current")


class _Hh3cIfQoSPortPriorityTrustOvercastType_Type(Integer32):
    """Custom type hh3cIfQoSPortPriorityTrustOvercastType based on Integer32"""
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


_Hh3cIfQoSPortPriorityTrustOvercastType_Type.__name__ = "Integer32"
_Hh3cIfQoSPortPriorityTrustOvercastType_Object = MibTableColumn
hh3cIfQoSPortPriorityTrustOvercastType = _Hh3cIfQoSPortPriorityTrustOvercastType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 7, 1, 2, 1, 2),
    _Hh3cIfQoSPortPriorityTrustOvercastType_Type()
)
hh3cIfQoSPortPriorityTrustOvercastType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfQoSPortPriorityTrustOvercastType.setStatus("current")
_Hh3cIfQoSMapObjects_ObjectIdentity = ObjectIdentity
hh3cIfQoSMapObjects = _Hh3cIfQoSMapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 9)
)
_Hh3cIfQoSPriMapConfigGroup_ObjectIdentity = ObjectIdentity
hh3cIfQoSPriMapConfigGroup = _Hh3cIfQoSPriMapConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 9, 1)
)
_Hh3cIfQoSPriMapGroupNextIndex_Type = Integer32
_Hh3cIfQoSPriMapGroupNextIndex_Object = MibScalar
hh3cIfQoSPriMapGroupNextIndex = _Hh3cIfQoSPriMapGroupNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 9, 1, 1),
    _Hh3cIfQoSPriMapGroupNextIndex_Type()
)
hh3cIfQoSPriMapGroupNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfQoSPriMapGroupNextIndex.setStatus("current")
_Hh3cIfQoSPriMapGroupTable_Object = MibTable
hh3cIfQoSPriMapGroupTable = _Hh3cIfQoSPriMapGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cIfQoSPriMapGroupTable.setStatus("current")
_Hh3cIfQoSPriMapGroupEntry_Object = MibTableRow
hh3cIfQoSPriMapGroupEntry = _Hh3cIfQoSPriMapGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 9, 1, 2, 1)
)
hh3cIfQoSPriMapGroupEntry.setIndexNames(
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSPriMapGroupIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSPriMapGroupEntry.setStatus("current")
_Hh3cIfQoSPriMapGroupIndex_Type = Integer32
_Hh3cIfQoSPriMapGroupIndex_Object = MibTableColumn
hh3cIfQoSPriMapGroupIndex = _Hh3cIfQoSPriMapGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 9, 1, 2, 1, 1),
    _Hh3cIfQoSPriMapGroupIndex_Type()
)
hh3cIfQoSPriMapGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfQoSPriMapGroupIndex.setStatus("current")


class _Hh3cIfQoSPriMapGroupType_Type(Integer32):
    """Custom type hh3cIfQoSPriMapGroupType based on Integer32"""
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


_Hh3cIfQoSPriMapGroupType_Type.__name__ = "Integer32"
_Hh3cIfQoSPriMapGroupType_Object = MibTableColumn
hh3cIfQoSPriMapGroupType = _Hh3cIfQoSPriMapGroupType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 9, 1, 2, 1, 2),
    _Hh3cIfQoSPriMapGroupType_Type()
)
hh3cIfQoSPriMapGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSPriMapGroupType.setStatus("current")


class _Hh3cIfQoSPriMapGroupName_Type(OctetString):
    """Custom type hh3cIfQoSPriMapGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cIfQoSPriMapGroupName_Type.__name__ = "OctetString"
_Hh3cIfQoSPriMapGroupName_Object = MibTableColumn
hh3cIfQoSPriMapGroupName = _Hh3cIfQoSPriMapGroupName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 9, 1, 2, 1, 3),
    _Hh3cIfQoSPriMapGroupName_Type()
)
hh3cIfQoSPriMapGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSPriMapGroupName.setStatus("current")
_Hh3cIfQoSPriMapGroupRowStatus_Type = RowStatus
_Hh3cIfQoSPriMapGroupRowStatus_Object = MibTableColumn
hh3cIfQoSPriMapGroupRowStatus = _Hh3cIfQoSPriMapGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 9, 1, 2, 1, 4),
    _Hh3cIfQoSPriMapGroupRowStatus_Type()
)
hh3cIfQoSPriMapGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSPriMapGroupRowStatus.setStatus("current")
_Hh3cIfQoSPriMapContentTable_Object = MibTable
hh3cIfQoSPriMapContentTable = _Hh3cIfQoSPriMapContentTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 9, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cIfQoSPriMapContentTable.setStatus("current")
_Hh3cIfQoSPriMapContentEntry_Object = MibTableRow
hh3cIfQoSPriMapContentEntry = _Hh3cIfQoSPriMapContentEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 9, 1, 3, 1)
)
hh3cIfQoSPriMapContentEntry.setIndexNames(
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSPriMapGroupIndex"),
    (0, "HH3C-IFQOS2-MIB", "hh3cIfQoSPriMapGroupImportValue"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSPriMapContentEntry.setStatus("current")


class _Hh3cIfQoSPriMapGroupImportValue_Type(Integer32):
    """Custom type hh3cIfQoSPriMapGroupImportValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Hh3cIfQoSPriMapGroupImportValue_Type.__name__ = "Integer32"
_Hh3cIfQoSPriMapGroupImportValue_Object = MibTableColumn
hh3cIfQoSPriMapGroupImportValue = _Hh3cIfQoSPriMapGroupImportValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 9, 1, 3, 1, 1),
    _Hh3cIfQoSPriMapGroupImportValue_Type()
)
hh3cIfQoSPriMapGroupImportValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfQoSPriMapGroupImportValue.setStatus("current")


class _Hh3cIfQoSPriMapGroupExportValue_Type(Integer32):
    """Custom type hh3cIfQoSPriMapGroupExportValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Hh3cIfQoSPriMapGroupExportValue_Type.__name__ = "Integer32"
_Hh3cIfQoSPriMapGroupExportValue_Object = MibTableColumn
hh3cIfQoSPriMapGroupExportValue = _Hh3cIfQoSPriMapGroupExportValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 9, 1, 3, 1, 2),
    _Hh3cIfQoSPriMapGroupExportValue_Type()
)
hh3cIfQoSPriMapGroupExportValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSPriMapGroupExportValue.setStatus("current")
_Hh3cIfQoSPriMapContentRowStatus_Type = RowStatus
_Hh3cIfQoSPriMapContentRowStatus_Object = MibTableColumn
hh3cIfQoSPriMapContentRowStatus = _Hh3cIfQoSPriMapContentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 9, 1, 3, 1, 3),
    _Hh3cIfQoSPriMapContentRowStatus_Type()
)
hh3cIfQoSPriMapContentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSPriMapContentRowStatus.setStatus("current")
_Hh3cIfQoSL3PlusObjects_ObjectIdentity = ObjectIdentity
hh3cIfQoSL3PlusObjects = _Hh3cIfQoSL3PlusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 10)
)
_Hh3cIfQoSPortBindingGroup_ObjectIdentity = ObjectIdentity
hh3cIfQoSPortBindingGroup = _Hh3cIfQoSPortBindingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 10, 1)
)
_Hh3cIfQoSPortBindingTable_Object = MibTable
hh3cIfQoSPortBindingTable = _Hh3cIfQoSPortBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 10, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cIfQoSPortBindingTable.setStatus("current")
_Hh3cIfQoSPortBindingEntry_Object = MibTableRow
hh3cIfQoSPortBindingEntry = _Hh3cIfQoSPortBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 10, 1, 1, 1)
)
hh3cIfQoSPortBindingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfQoSPortBindingEntry.setStatus("current")
_Hh3cIfQoSBindingIf_Type = Integer32
_Hh3cIfQoSBindingIf_Object = MibTableColumn
hh3cIfQoSBindingIf = _Hh3cIfQoSBindingIf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 10, 1, 1, 1, 1),
    _Hh3cIfQoSBindingIf_Type()
)
hh3cIfQoSBindingIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSBindingIf.setStatus("current")
_Hh3cIfQoSBindingRowStatus_Type = RowStatus
_Hh3cIfQoSBindingRowStatus_Object = MibTableColumn
hh3cIfQoSBindingRowStatus = _Hh3cIfQoSBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 10, 1, 1, 1, 2),
    _Hh3cIfQoSBindingRowStatus_Type()
)
hh3cIfQoSBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIfQoSBindingRowStatus.setStatus("current")
_Hh3cQoSTraStaObjects_ObjectIdentity = ObjectIdentity
hh3cQoSTraStaObjects = _Hh3cQoSTraStaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 11)
)
_Hh3cQoSTraStaConfigGroup_ObjectIdentity = ObjectIdentity
hh3cQoSTraStaConfigGroup = _Hh3cQoSTraStaConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 11, 1)
)
_Hh3cQoSIfTraStaConfigInfoTable_Object = MibTable
hh3cQoSIfTraStaConfigInfoTable = _Hh3cQoSIfTraStaConfigInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 11, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cQoSIfTraStaConfigInfoTable.setStatus("current")
_Hh3cQoSIfTraStaConfigInfoEntry_Object = MibTableRow
hh3cQoSIfTraStaConfigInfoEntry = _Hh3cQoSIfTraStaConfigInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 11, 1, 1, 1)
)
hh3cQoSIfTraStaConfigInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-IFQOS2-MIB", "hh3cQoSIfTraStaConfigDirection"),
)
if mibBuilder.loadTexts:
    hh3cQoSIfTraStaConfigInfoEntry.setStatus("current")
_Hh3cQoSIfTraStaConfigDirection_Type = Direction
_Hh3cQoSIfTraStaConfigDirection_Object = MibTableColumn
hh3cQoSIfTraStaConfigDirection = _Hh3cQoSIfTraStaConfigDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 11, 1, 1, 1, 1),
    _Hh3cQoSIfTraStaConfigDirection_Type()
)
hh3cQoSIfTraStaConfigDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQoSIfTraStaConfigDirection.setStatus("current")


class _Hh3cQoSIfTraStaConfigQueue_Type(OctetString):
    """Custom type hh3cQoSIfTraStaConfigQueue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Hh3cQoSIfTraStaConfigQueue_Type.__name__ = "OctetString"
_Hh3cQoSIfTraStaConfigQueue_Object = MibTableColumn
hh3cQoSIfTraStaConfigQueue = _Hh3cQoSIfTraStaConfigQueue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 11, 1, 1, 1, 2),
    _Hh3cQoSIfTraStaConfigQueue_Type()
)
hh3cQoSIfTraStaConfigQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSIfTraStaConfigQueue.setStatus("current")


class _Hh3cQoSIfTraStaConfigDot1p_Type(OctetString):
    """Custom type hh3cQoSIfTraStaConfigDot1p based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Hh3cQoSIfTraStaConfigDot1p_Type.__name__ = "OctetString"
_Hh3cQoSIfTraStaConfigDot1p_Object = MibTableColumn
hh3cQoSIfTraStaConfigDot1p = _Hh3cQoSIfTraStaConfigDot1p_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 11, 1, 1, 1, 3),
    _Hh3cQoSIfTraStaConfigDot1p_Type()
)
hh3cQoSIfTraStaConfigDot1p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSIfTraStaConfigDot1p.setStatus("current")


class _Hh3cQoSIfTraStaConfigDscp_Type(OctetString):
    """Custom type hh3cQoSIfTraStaConfigDscp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Hh3cQoSIfTraStaConfigDscp_Type.__name__ = "OctetString"
_Hh3cQoSIfTraStaConfigDscp_Object = MibTableColumn
hh3cQoSIfTraStaConfigDscp = _Hh3cQoSIfTraStaConfigDscp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 11, 1, 1, 1, 4),
    _Hh3cQoSIfTraStaConfigDscp_Type()
)
hh3cQoSIfTraStaConfigDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSIfTraStaConfigDscp.setStatus("current")


class _Hh3cQoSIfTraStaConfigVlan_Type(OctetString):
    """Custom type hh3cQoSIfTraStaConfigVlan based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )


_Hh3cQoSIfTraStaConfigVlan_Type.__name__ = "OctetString"
_Hh3cQoSIfTraStaConfigVlan_Object = MibTableColumn
hh3cQoSIfTraStaConfigVlan = _Hh3cQoSIfTraStaConfigVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 11, 1, 1, 1, 5),
    _Hh3cQoSIfTraStaConfigVlan_Type()
)
hh3cQoSIfTraStaConfigVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSIfTraStaConfigVlan.setStatus("current")
_Hh3cQoSIfTraStaConfigStatus_Type = RowStatus
_Hh3cQoSIfTraStaConfigStatus_Object = MibTableColumn
hh3cQoSIfTraStaConfigStatus = _Hh3cQoSIfTraStaConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 11, 1, 1, 1, 6),
    _Hh3cQoSIfTraStaConfigStatus_Type()
)
hh3cQoSIfTraStaConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cQoSIfTraStaConfigStatus.setStatus("current")
_Hh3cQoSTraStaRunGroup_ObjectIdentity = ObjectIdentity
hh3cQoSTraStaRunGroup = _Hh3cQoSTraStaRunGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 11, 2)
)
_Hh3cQoSIfTraStaRunInfoTable_Object = MibTable
hh3cQoSIfTraStaRunInfoTable = _Hh3cQoSIfTraStaRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 11, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cQoSIfTraStaRunInfoTable.setStatus("current")
_Hh3cQoSIfTraStaRunInfoEntry_Object = MibTableRow
hh3cQoSIfTraStaRunInfoEntry = _Hh3cQoSIfTraStaRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 11, 2, 1, 1)
)
hh3cQoSIfTraStaRunInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-IFQOS2-MIB", "hh3cQoSIfTraStaRunObjectType"),
    (0, "HH3C-IFQOS2-MIB", "hh3cQoSIfTraStaRunObjectValue"),
    (0, "HH3C-IFQOS2-MIB", "hh3cQoSIfTraStaRunDirection"),
)
if mibBuilder.loadTexts:
    hh3cQoSIfTraStaRunInfoEntry.setStatus("current")


class _Hh3cQoSIfTraStaRunObjectType_Type(Integer32):
    """Custom type hh3cQoSIfTraStaRunObjectType based on Integer32"""
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


_Hh3cQoSIfTraStaRunObjectType_Type.__name__ = "Integer32"
_Hh3cQoSIfTraStaRunObjectType_Object = MibTableColumn
hh3cQoSIfTraStaRunObjectType = _Hh3cQoSIfTraStaRunObjectType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 11, 2, 1, 1, 1),
    _Hh3cQoSIfTraStaRunObjectType_Type()
)
hh3cQoSIfTraStaRunObjectType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQoSIfTraStaRunObjectType.setStatus("current")
_Hh3cQoSIfTraStaRunObjectValue_Type = Integer32
_Hh3cQoSIfTraStaRunObjectValue_Object = MibTableColumn
hh3cQoSIfTraStaRunObjectValue = _Hh3cQoSIfTraStaRunObjectValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 11, 2, 1, 1, 2),
    _Hh3cQoSIfTraStaRunObjectValue_Type()
)
hh3cQoSIfTraStaRunObjectValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQoSIfTraStaRunObjectValue.setStatus("current")
_Hh3cQoSIfTraStaRunDirection_Type = Direction
_Hh3cQoSIfTraStaRunDirection_Object = MibTableColumn
hh3cQoSIfTraStaRunDirection = _Hh3cQoSIfTraStaRunDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 11, 2, 1, 1, 3),
    _Hh3cQoSIfTraStaRunDirection_Type()
)
hh3cQoSIfTraStaRunDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQoSIfTraStaRunDirection.setStatus("current")
_Hh3cQoSIfTraStaRunPassPackets_Type = Counter64
_Hh3cQoSIfTraStaRunPassPackets_Object = MibTableColumn
hh3cQoSIfTraStaRunPassPackets = _Hh3cQoSIfTraStaRunPassPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 11, 2, 1, 1, 4),
    _Hh3cQoSIfTraStaRunPassPackets_Type()
)
hh3cQoSIfTraStaRunPassPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cQoSIfTraStaRunPassPackets.setStatus("current")
_Hh3cQoSIfTraStaRunDropPackets_Type = Counter64
_Hh3cQoSIfTraStaRunDropPackets_Object = MibTableColumn
hh3cQoSIfTraStaRunDropPackets = _Hh3cQoSIfTraStaRunDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 11, 2, 1, 1, 5),
    _Hh3cQoSIfTraStaRunDropPackets_Type()
)
hh3cQoSIfTraStaRunDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cQoSIfTraStaRunDropPackets.setStatus("current")
_Hh3cQoSIfTraStaRunPassBytes_Type = Counter64
_Hh3cQoSIfTraStaRunPassBytes_Object = MibTableColumn
hh3cQoSIfTraStaRunPassBytes = _Hh3cQoSIfTraStaRunPassBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 11, 2, 1, 1, 6),
    _Hh3cQoSIfTraStaRunPassBytes_Type()
)
hh3cQoSIfTraStaRunPassBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cQoSIfTraStaRunPassBytes.setStatus("current")
_Hh3cQoSIfTraStaRunDropBytes_Type = Counter64
_Hh3cQoSIfTraStaRunDropBytes_Object = MibTableColumn
hh3cQoSIfTraStaRunDropBytes = _Hh3cQoSIfTraStaRunDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 11, 2, 1, 1, 7),
    _Hh3cQoSIfTraStaRunDropBytes_Type()
)
hh3cQoSIfTraStaRunDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cQoSIfTraStaRunDropBytes.setStatus("current")
_Hh3cQoSIfTraStaRunPassPPS_Type = Counter64
_Hh3cQoSIfTraStaRunPassPPS_Object = MibTableColumn
hh3cQoSIfTraStaRunPassPPS = _Hh3cQoSIfTraStaRunPassPPS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 11, 2, 1, 1, 8),
    _Hh3cQoSIfTraStaRunPassPPS_Type()
)
hh3cQoSIfTraStaRunPassPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cQoSIfTraStaRunPassPPS.setStatus("current")
_Hh3cQoSIfTraStaRunPassBPS_Type = Counter64
_Hh3cQoSIfTraStaRunPassBPS_Object = MibTableColumn
hh3cQoSIfTraStaRunPassBPS = _Hh3cQoSIfTraStaRunPassBPS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 65, 1, 11, 2, 1, 1, 9),
    _Hh3cQoSIfTraStaRunPassBPS_Type()
)
hh3cQoSIfTraStaRunPassBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cQoSIfTraStaRunPassBPS.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-IFQOS2-MIB",
    **{"CarAction": CarAction,
       "PriorityQueue": PriorityQueue,
       "Direction": Direction,
       "hh3cQos2": hh3cQos2,
       "hh3cIfQos2": hh3cIfQos2,
       "hh3cIfQoSHardwareQueueObjects": hh3cIfQoSHardwareQueueObjects,
       "hh3cIfQoSHardwareQueueConfigGroup": hh3cIfQoSHardwareQueueConfigGroup,
       "hh3cIfQoSQSModeTable": hh3cIfQoSQSModeTable,
       "hh3cIfQoSQSModeEntry": hh3cIfQoSQSModeEntry,
       "hh3cIfQoSQSMode": hh3cIfQoSQSMode,
       "hh3cIfQoSQSWeightTable": hh3cIfQoSQSWeightTable,
       "hh3cIfQoSQSWeightEntry": hh3cIfQoSQSWeightEntry,
       "hh3cIfQoSQueueID": hh3cIfQoSQueueID,
       "hh3cIfQoSQueueGroupType": hh3cIfQoSQueueGroupType,
       "hh3cIfQoSQSType": hh3cIfQoSQSType,
       "hh3cIfQoSQSValue": hh3cIfQoSQSValue,
       "hh3cIfQoSQSMaxDelay": hh3cIfQoSQSMaxDelay,
       "hh3cIfQoSHardwareQueueRunInfoGroup": hh3cIfQoSHardwareQueueRunInfoGroup,
       "hh3cIfQoSHardwareQueueRunInfoTable": hh3cIfQoSHardwareQueueRunInfoTable,
       "hh3cIfQoSHardwareQueueRunInfoEntry": hh3cIfQoSHardwareQueueRunInfoEntry,
       "hh3cIfQoSPassPackets": hh3cIfQoSPassPackets,
       "hh3cIfQoSDropPackets": hh3cIfQoSDropPackets,
       "hh3cIfQoSPassBytes": hh3cIfQoSPassBytes,
       "hh3cIfQoSPassPPS": hh3cIfQoSPassPPS,
       "hh3cIfQoSPassBPS": hh3cIfQoSPassBPS,
       "hh3cIfQoSDropBytes": hh3cIfQoSDropBytes,
       "hh3cIfQoSQueueLengthInPkts": hh3cIfQoSQueueLengthInPkts,
       "hh3cIfQoSQueueLengthInBytes": hh3cIfQoSQueueLengthInBytes,
       "hh3cIfQoSCurQueuePkts": hh3cIfQoSCurQueuePkts,
       "hh3cIfQoSCurQueueBytes": hh3cIfQoSCurQueueBytes,
       "hh3cIfQoSCurQueuePPS": hh3cIfQoSCurQueuePPS,
       "hh3cIfQoSCurQueueBPS": hh3cIfQoSCurQueueBPS,
       "hh3cIfQoSTailDropPkts": hh3cIfQoSTailDropPkts,
       "hh3cIfQoSTailDropBytes": hh3cIfQoSTailDropBytes,
       "hh3cIfQoSTailDropPPS": hh3cIfQoSTailDropPPS,
       "hh3cIfQoSTailDropBPS": hh3cIfQoSTailDropBPS,
       "hh3cIfQoSWredDropPkts": hh3cIfQoSWredDropPkts,
       "hh3cIfQoSWredDropBytes": hh3cIfQoSWredDropBytes,
       "hh3cIfQoSWredDropPPS": hh3cIfQoSWredDropPPS,
       "hh3cIfQoSWredDropBPS": hh3cIfQoSWredDropBPS,
       "hh3cIfQoSHQueueTcpRunInfoTable": hh3cIfQoSHQueueTcpRunInfoTable,
       "hh3cIfQoSHQueueTcpRunInfoEntry": hh3cIfQoSHQueueTcpRunInfoEntry,
       "hh3cIfQoSWredDropLPreNTcpPkts": hh3cIfQoSWredDropLPreNTcpPkts,
       "hh3cIfQoSWredDropLPreNTcpBytes": hh3cIfQoSWredDropLPreNTcpBytes,
       "hh3cIfQoSWredDropLPreNTcpPPS": hh3cIfQoSWredDropLPreNTcpPPS,
       "hh3cIfQoSWredDropLPreNTcpBPS": hh3cIfQoSWredDropLPreNTcpBPS,
       "hh3cIfQoSWredDropLPreTcpPkts": hh3cIfQoSWredDropLPreTcpPkts,
       "hh3cIfQoSWredDropLPreTcpBytes": hh3cIfQoSWredDropLPreTcpBytes,
       "hh3cIfQoSWredDropLPreTcpPPS": hh3cIfQoSWredDropLPreTcpPPS,
       "hh3cIfQoSWredDropLPreTcpBPS": hh3cIfQoSWredDropLPreTcpBPS,
       "hh3cIfQoSWredDropHPreNTcpPkts": hh3cIfQoSWredDropHPreNTcpPkts,
       "hh3cIfQoSWredDropHPreNTcpBytes": hh3cIfQoSWredDropHPreNTcpBytes,
       "hh3cIfQoSWredDropHPreNTcpPPS": hh3cIfQoSWredDropHPreNTcpPPS,
       "hh3cIfQoSWredDropHPreNTcpBPS": hh3cIfQoSWredDropHPreNTcpBPS,
       "hh3cIfQoSWredDropHPreTcpPkts": hh3cIfQoSWredDropHPreTcpPkts,
       "hh3cIfQoSWredDropHPreTcpBytes": hh3cIfQoSWredDropHPreTcpBytes,
       "hh3cIfQoSWredDropHPreTcpPPS": hh3cIfQoSWredDropHPreTcpPPS,
       "hh3cIfQoSWredDropHPreTcpBPS": hh3cIfQoSWredDropHPreTcpBPS,
       "hh3cIfQoSSoftwareQueueObjects": hh3cIfQoSSoftwareQueueObjects,
       "hh3cIfQoSFIFOObject": hh3cIfQoSFIFOObject,
       "hh3cIfQoSFIFOConfigTable": hh3cIfQoSFIFOConfigTable,
       "hh3cIfQoSFIFOConfigEntry": hh3cIfQoSFIFOConfigEntry,
       "hh3cIfQoSFIFOMaxQueueLen": hh3cIfQoSFIFOMaxQueueLen,
       "hh3cIfQoSFIFORunInfoTable": hh3cIfQoSFIFORunInfoTable,
       "hh3cIfQoSFIFORunInfoEntry": hh3cIfQoSFIFORunInfoEntry,
       "hh3cIfQoSFIFOSize": hh3cIfQoSFIFOSize,
       "hh3cIfQoSFIFODiscardPackets": hh3cIfQoSFIFODiscardPackets,
       "hh3cIfQoSPQObject": hh3cIfQoSPQObject,
       "hh3cIfQoSPQConfigGroup": hh3cIfQoSPQConfigGroup,
       "hh3cIfQoSPQDefaultTable": hh3cIfQoSPQDefaultTable,
       "hh3cIfQoSPQDefaultEntry": hh3cIfQoSPQDefaultEntry,
       "hh3cIfQoSPQListNumber": hh3cIfQoSPQListNumber,
       "hh3cIfQoSPQDefaultQueueType": hh3cIfQoSPQDefaultQueueType,
       "hh3cIfQoSPQQueueLengthTable": hh3cIfQoSPQQueueLengthTable,
       "hh3cIfQoSPQQueueLengthEntry": hh3cIfQoSPQQueueLengthEntry,
       "hh3cIfQoSPQQueueLengthType": hh3cIfQoSPQQueueLengthType,
       "hh3cIfQoSPQQueueLengthValue": hh3cIfQoSPQQueueLengthValue,
       "hh3cIfQoSPQClassRuleTable": hh3cIfQoSPQClassRuleTable,
       "hh3cIfQoSPQClassRuleEntry": hh3cIfQoSPQClassRuleEntry,
       "hh3cIfQoSPQClassRuleType": hh3cIfQoSPQClassRuleType,
       "hh3cIfQoSPQClassRuleValue": hh3cIfQoSPQClassRuleValue,
       "hh3cIfQoSPQClassRuleQueueType": hh3cIfQoSPQClassRuleQueueType,
       "hh3cIfQoSPQClassRowStatus": hh3cIfQoSPQClassRowStatus,
       "hh3cIfQoSPQApplyTable": hh3cIfQoSPQApplyTable,
       "hh3cIfQoSPQApplyEntry": hh3cIfQoSPQApplyEntry,
       "hh3cIfQoSPQApplyListNumber": hh3cIfQoSPQApplyListNumber,
       "hh3cIfQoSPQApplyRowStatus": hh3cIfQoSPQApplyRowStatus,
       "hh3cIfQoSPQRunInfoGroup": hh3cIfQoSPQRunInfoGroup,
       "hh3cIfQoSPQRunInfoTable": hh3cIfQoSPQRunInfoTable,
       "hh3cIfQoSPQRunInfoEntry": hh3cIfQoSPQRunInfoEntry,
       "hh3cIfQoSPQType": hh3cIfQoSPQType,
       "hh3cIfQoSPQSize": hh3cIfQoSPQSize,
       "hh3cIfQoSPQLength": hh3cIfQoSPQLength,
       "hh3cIfQoSPQDiscardPackets": hh3cIfQoSPQDiscardPackets,
       "hh3cIfQoSCQObject": hh3cIfQoSCQObject,
       "hh3cIfQoSCQConfigGroup": hh3cIfQoSCQConfigGroup,
       "hh3cIfQoSCQDefaultTable": hh3cIfQoSCQDefaultTable,
       "hh3cIfQoSCQDefaultEntry": hh3cIfQoSCQDefaultEntry,
       "hh3cIfQoSCQListNumber": hh3cIfQoSCQListNumber,
       "hh3cIfQoSCQDefaultQueueID": hh3cIfQoSCQDefaultQueueID,
       "hh3cIfQoSCQQueueLengthTable": hh3cIfQoSCQQueueLengthTable,
       "hh3cIfQoSCQQueueLengthEntry": hh3cIfQoSCQQueueLengthEntry,
       "hh3cIfQoSCQQueueID": hh3cIfQoSCQQueueID,
       "hh3cIfQoSCQQueueLength": hh3cIfQoSCQQueueLength,
       "hh3cIfQoSCQQueueServing": hh3cIfQoSCQQueueServing,
       "hh3cIfQoSCQClassRuleTable": hh3cIfQoSCQClassRuleTable,
       "hh3cIfQoSCQClassRuleEntry": hh3cIfQoSCQClassRuleEntry,
       "hh3cIfQoSCQClassRuleType": hh3cIfQoSCQClassRuleType,
       "hh3cIfQoSCQClassRuleValue": hh3cIfQoSCQClassRuleValue,
       "hh3cIfQoSCQClassRuleQueueID": hh3cIfQoSCQClassRuleQueueID,
       "hh3cIfQoSCQClassRowStatus": hh3cIfQoSCQClassRowStatus,
       "hh3cIfQoSCQApplyTable": hh3cIfQoSCQApplyTable,
       "hh3cIfQoSCQApplyEntry": hh3cIfQoSCQApplyEntry,
       "hh3cIfQoSCQApplyListNumber": hh3cIfQoSCQApplyListNumber,
       "hh3cIfQoSCQApplyRowStatus": hh3cIfQoSCQApplyRowStatus,
       "hh3cIfQoSCQRunInfoGroup": hh3cIfQoSCQRunInfoGroup,
       "hh3cIfQoSCQRunInfoTable": hh3cIfQoSCQRunInfoTable,
       "hh3cIfQoSCQRunInfoEntry": hh3cIfQoSCQRunInfoEntry,
       "hh3cIfQoSCQRunInfoSize": hh3cIfQoSCQRunInfoSize,
       "hh3cIfQoSCQRunInfoLength": hh3cIfQoSCQRunInfoLength,
       "hh3cIfQoSCQRunInfoDiscardPackets": hh3cIfQoSCQRunInfoDiscardPackets,
       "hh3cIfQoSWFQObject": hh3cIfQoSWFQObject,
       "hh3cIfQoSWFQConfigGroup": hh3cIfQoSWFQConfigGroup,
       "hh3cIfQoSWFQTable": hh3cIfQoSWFQTable,
       "hh3cIfQoSWFQEntry": hh3cIfQoSWFQEntry,
       "hh3cIfQoSWFQQueueLength": hh3cIfQoSWFQQueueLength,
       "hh3cIfQoSWFQQueueNumber": hh3cIfQoSWFQQueueNumber,
       "hh3cIfQoSWFQRowStatus": hh3cIfQoSWFQRowStatus,
       "hh3cIfQoSWFQType": hh3cIfQoSWFQType,
       "hh3cIfQoSWFQRunInfoGroup": hh3cIfQoSWFQRunInfoGroup,
       "hh3cIfQoSWFQRunInfoTable": hh3cIfQoSWFQRunInfoTable,
       "hh3cIfQoSWFQRunInfoEntry": hh3cIfQoSWFQRunInfoEntry,
       "hh3cIfQoSWFQSize": hh3cIfQoSWFQSize,
       "hh3cIfQoSWFQLength": hh3cIfQoSWFQLength,
       "hh3cIfQoSWFQDiscardPackets": hh3cIfQoSWFQDiscardPackets,
       "hh3cIfQoSWFQHashedActiveQueues": hh3cIfQoSWFQHashedActiveQueues,
       "hh3cIfQoSWFQHashedMaxActiveQueues": hh3cIfQoSWFQHashedMaxActiveQueues,
       "hh3cIfQosWFQhashedTotalQueues": hh3cIfQosWFQhashedTotalQueues,
       "hh3cIfQoSBandwidthGroup": hh3cIfQoSBandwidthGroup,
       "hh3cIfQoSBandwidthTable": hh3cIfQoSBandwidthTable,
       "hh3cIfQoSBandwidthEntry": hh3cIfQoSBandwidthEntry,
       "hh3cIfQoSMaxBandwidth": hh3cIfQoSMaxBandwidth,
       "hh3cIfQoSReservedBandwidthPct": hh3cIfQoSReservedBandwidthPct,
       "hh3cIfQoSBandwidthRowStatus": hh3cIfQoSBandwidthRowStatus,
       "hh3cIfQoSQmtokenGroup": hh3cIfQoSQmtokenGroup,
       "hh3cIfQoSQmtokenTable": hh3cIfQoSQmtokenTable,
       "hh3cIfQoSQmtokenEntry": hh3cIfQoSQmtokenEntry,
       "hh3cIfQoSQmtokenNumber": hh3cIfQoSQmtokenNumber,
       "hh3cIfQoSQmtokenRosStatus": hh3cIfQoSQmtokenRosStatus,
       "hh3cIfQoSRTPQObject": hh3cIfQoSRTPQObject,
       "hh3cIfQoSRTPQConfigGroup": hh3cIfQoSRTPQConfigGroup,
       "hh3cIfQoSRTPQConfigTable": hh3cIfQoSRTPQConfigTable,
       "hh3cIfQoSRTPQConfigEntry": hh3cIfQoSRTPQConfigEntry,
       "hh3cIfQoSRTPQStartPort": hh3cIfQoSRTPQStartPort,
       "hh3cIfQoSRTPQEndPort": hh3cIfQoSRTPQEndPort,
       "hh3cIfQoSRTPQReservedBandwidth": hh3cIfQoSRTPQReservedBandwidth,
       "hh3cIfQoSRTPQCbs": hh3cIfQoSRTPQCbs,
       "hh3cIfQoSRTPQRowStatus": hh3cIfQoSRTPQRowStatus,
       "hh3cIfQoSRTPQRunInfoGroup": hh3cIfQoSRTPQRunInfoGroup,
       "hh3cIfQoSRTPQRunInfoTable": hh3cIfQoSRTPQRunInfoTable,
       "hh3cIfQoSRTPQRunInfoEntry": hh3cIfQoSRTPQRunInfoEntry,
       "hh3cIfQoSRTPQPacketNumber": hh3cIfQoSRTPQPacketNumber,
       "hh3cIfQoSRTPQPacketSize": hh3cIfQoSRTPQPacketSize,
       "hh3cIfQoSRTPQOutputPackets": hh3cIfQoSRTPQOutputPackets,
       "hh3cIfQoSRTPQDiscardPackets": hh3cIfQoSRTPQDiscardPackets,
       "hh3cIfQoSCarListObject": hh3cIfQoSCarListObject,
       "hh3cIfQoCarListGroup": hh3cIfQoCarListGroup,
       "hh3cIfQoSCarlTable": hh3cIfQoSCarlTable,
       "hh3cIfQoSCarlEntry": hh3cIfQoSCarlEntry,
       "hh3cIfQoSCarlListNum": hh3cIfQoSCarlListNum,
       "hh3cIfQoSCarlParaType": hh3cIfQoSCarlParaType,
       "hh3cIfQoSCarlParaValue": hh3cIfQoSCarlParaValue,
       "hh3cIfQoSCarlRowStatus": hh3cIfQoSCarlRowStatus,
       "hh3cIfQoSLineRateObjects": hh3cIfQoSLineRateObjects,
       "hh3cIfQoSLRConfigTable": hh3cIfQoSLRConfigTable,
       "hh3cIfQoSLRConfigEntry": hh3cIfQoSLRConfigEntry,
       "hh3cIfQoSLRDirection": hh3cIfQoSLRDirection,
       "hh3cIfQoSLRCir": hh3cIfQoSLRCir,
       "hh3cIfQoSLRCbs": hh3cIfQoSLRCbs,
       "hh3cIfQoSLREbs": hh3cIfQoSLREbs,
       "hh3cIfQoSRowStatus": hh3cIfQoSRowStatus,
       "hh3cIfQoSLRRunInfoTable": hh3cIfQoSLRRunInfoTable,
       "hh3cIfQoSLRRunInfoEntry": hh3cIfQoSLRRunInfoEntry,
       "hh3cIfQoSLRRunInfoPassedPackets": hh3cIfQoSLRRunInfoPassedPackets,
       "hh3cIfQoSLRRunInfoPassedBytes": hh3cIfQoSLRRunInfoPassedBytes,
       "hh3cIfQoSLRRunInfoDelayedPackets": hh3cIfQoSLRRunInfoDelayedPackets,
       "hh3cIfQoSLRRunInfoDelayedBytes": hh3cIfQoSLRRunInfoDelayedBytes,
       "hh3cIfQoSLRRunInfoActiveShaping": hh3cIfQoSLRRunInfoActiveShaping,
       "hh3cIfQoSCARObjects": hh3cIfQoSCARObjects,
       "hh3cIfQoSAggregativeCarGroup": hh3cIfQoSAggregativeCarGroup,
       "hh3cIfQoSAggregativeCarNextIndex": hh3cIfQoSAggregativeCarNextIndex,
       "hh3cIfQoSAggregativeCarConfigTable": hh3cIfQoSAggregativeCarConfigTable,
       "hh3cIfQoSAggregativeCarConfigEntry": hh3cIfQoSAggregativeCarConfigEntry,
       "hh3cIfQoSAggregativeCarIndex": hh3cIfQoSAggregativeCarIndex,
       "hh3cIfQoSAggregativeCarName": hh3cIfQoSAggregativeCarName,
       "hh3cIfQoSAggregativeCarCir": hh3cIfQoSAggregativeCarCir,
       "hh3cIfQoSAggregativeCarCbs": hh3cIfQoSAggregativeCarCbs,
       "hh3cIfQoSAggregativeCarEbs": hh3cIfQoSAggregativeCarEbs,
       "hh3cIfQoSAggregativeCarPir": hh3cIfQoSAggregativeCarPir,
       "hh3cIfQoSAggregativeCarGreenActionType": hh3cIfQoSAggregativeCarGreenActionType,
       "hh3cIfQoSAggregativeCarGreenActionValue": hh3cIfQoSAggregativeCarGreenActionValue,
       "hh3cIfQoSAggregativeCarYellowActionType": hh3cIfQoSAggregativeCarYellowActionType,
       "hh3cIfQoSAggregativeCarYellowActionValue": hh3cIfQoSAggregativeCarYellowActionValue,
       "hh3cIfQoSAggregativeCarRedActionType": hh3cIfQoSAggregativeCarRedActionType,
       "hh3cIfQoSAggregativeCarRedActionValue": hh3cIfQoSAggregativeCarRedActionValue,
       "hh3cIfQoSAggregativeCarType": hh3cIfQoSAggregativeCarType,
       "hh3cIfQoSAggregativeCarRowStatus": hh3cIfQoSAggregativeCarRowStatus,
       "hh3cIfQoSAggregativeCarApplyTable": hh3cIfQoSAggregativeCarApplyTable,
       "hh3cIfQoSAggregativeCarApplyEntry": hh3cIfQoSAggregativeCarApplyEntry,
       "hh3cIfQoSAggregativeCarApplyDirection": hh3cIfQoSAggregativeCarApplyDirection,
       "hh3cIfQoSAggregativeCarApplyRuleType": hh3cIfQoSAggregativeCarApplyRuleType,
       "hh3cIfQoSAggregativeCarApplyRuleValue": hh3cIfQoSAggregativeCarApplyRuleValue,
       "hh3cIfQoSAggregativeCarApplyCarIndex": hh3cIfQoSAggregativeCarApplyCarIndex,
       "hh3cIfQoSAggregativeCarApplyRowStatus": hh3cIfQoSAggregativeCarApplyRowStatus,
       "hh3cIfQoSAggregativeCarRunInfoTable": hh3cIfQoSAggregativeCarRunInfoTable,
       "hh3cIfQoSAggregativeCarRunInfoEntry": hh3cIfQoSAggregativeCarRunInfoEntry,
       "hh3cIfQoSAggregativeCarGreenPackets": hh3cIfQoSAggregativeCarGreenPackets,
       "hh3cIfQoSAggregativeCarGreenBytes": hh3cIfQoSAggregativeCarGreenBytes,
       "hh3cIfQoSAggregativeCarYellowPackets": hh3cIfQoSAggregativeCarYellowPackets,
       "hh3cIfQoSAggregativeCarYellowBytes": hh3cIfQoSAggregativeCarYellowBytes,
       "hh3cIfQoSAggregativeCarRedPackets": hh3cIfQoSAggregativeCarRedPackets,
       "hh3cIfQoSAggregativeCarRedBytes": hh3cIfQoSAggregativeCarRedBytes,
       "hh3cIfQoSTricolorCarGroup": hh3cIfQoSTricolorCarGroup,
       "hh3cIfQoSTricolorCarConfigTable": hh3cIfQoSTricolorCarConfigTable,
       "hh3cIfQoSTricolorCarConfigEntry": hh3cIfQoSTricolorCarConfigEntry,
       "hh3cIfQoSTricolorCarDirection": hh3cIfQoSTricolorCarDirection,
       "hh3cIfQoSTricolorCarType": hh3cIfQoSTricolorCarType,
       "hh3cIfQoSTricolorCarValue": hh3cIfQoSTricolorCarValue,
       "hh3cIfQoSTricolorCarCir": hh3cIfQoSTricolorCarCir,
       "hh3cIfQoSTricolorCarCbs": hh3cIfQoSTricolorCarCbs,
       "hh3cIfQoSTricolorCarEbs": hh3cIfQoSTricolorCarEbs,
       "hh3cIfQoSTricolorCarPir": hh3cIfQoSTricolorCarPir,
       "hh3cIfQoSTricolorCarGreenActionType": hh3cIfQoSTricolorCarGreenActionType,
       "hh3cIfQoSTricolorCarGreenActionValue": hh3cIfQoSTricolorCarGreenActionValue,
       "hh3cIfQoSTricolorCarYellowActionType": hh3cIfQoSTricolorCarYellowActionType,
       "hh3cIfQoSTricolorCarYellowActionValue": hh3cIfQoSTricolorCarYellowActionValue,
       "hh3cIfQoSTricolorCarRedActionType": hh3cIfQoSTricolorCarRedActionType,
       "hh3cIfQoSTricolorCarRedActionValue": hh3cIfQoSTricolorCarRedActionValue,
       "hh3cIfQoSTricolorCarRowStatus": hh3cIfQoSTricolorCarRowStatus,
       "hh3cIfQoSTricolorCarRunInfoTable": hh3cIfQoSTricolorCarRunInfoTable,
       "hh3cIfQoSTricolorCarRunInfoEntry": hh3cIfQoSTricolorCarRunInfoEntry,
       "hh3cIfQoSTricolorCarGreenPackets": hh3cIfQoSTricolorCarGreenPackets,
       "hh3cIfQoSTricolorCarGreenBytes": hh3cIfQoSTricolorCarGreenBytes,
       "hh3cIfQoSTricolorCarYellowPackets": hh3cIfQoSTricolorCarYellowPackets,
       "hh3cIfQoSTricolorCarYellowBytes": hh3cIfQoSTricolorCarYellowBytes,
       "hh3cIfQoSTricolorCarRedPackets": hh3cIfQoSTricolorCarRedPackets,
       "hh3cIfQoSTricolorCarRedBytes": hh3cIfQoSTricolorCarRedBytes,
       "hh3cIfQoSGTSObjects": hh3cIfQoSGTSObjects,
       "hh3cIfQoSGTSConfigTable": hh3cIfQoSGTSConfigTable,
       "hh3cIfQoSGTSConfigEntry": hh3cIfQoSGTSConfigEntry,
       "hh3cIfQoSGTSClassRuleType": hh3cIfQoSGTSClassRuleType,
       "hh3cIfQoSGTSClassRuleValue": hh3cIfQoSGTSClassRuleValue,
       "hh3cIfQoSGTSCir": hh3cIfQoSGTSCir,
       "hh3cIfQoSGTSCbs": hh3cIfQoSGTSCbs,
       "hh3cIfQoSGTSEbs": hh3cIfQoSGTSEbs,
       "hh3cIfQoSGTSQueueLength": hh3cIfQoSGTSQueueLength,
       "hh3cIfQoSGTSConfigRowStatus": hh3cIfQoSGTSConfigRowStatus,
       "hh3cIfQoSGTSRunInfoTable": hh3cIfQoSGTSRunInfoTable,
       "hh3cIfQoSGTSRunInfoEntry": hh3cIfQoSGTSRunInfoEntry,
       "hh3cIfQoSGTSQueueSize": hh3cIfQoSGTSQueueSize,
       "hh3cIfQoSGTSPassedPackets": hh3cIfQoSGTSPassedPackets,
       "hh3cIfQoSGTSPassedBytes": hh3cIfQoSGTSPassedBytes,
       "hh3cIfQoSGTSDiscardPackets": hh3cIfQoSGTSDiscardPackets,
       "hh3cIfQoSGTSDiscardBytes": hh3cIfQoSGTSDiscardBytes,
       "hh3cIfQoSGTSDelayedPackets": hh3cIfQoSGTSDelayedPackets,
       "hh3cIfQoSGTSDelayedBytes": hh3cIfQoSGTSDelayedBytes,
       "hh3cIfQoSWREDObjects": hh3cIfQoSWREDObjects,
       "hh3cIfQoSWredGroupGroup": hh3cIfQoSWredGroupGroup,
       "hh3cIfQoSWredGroupNextIndex": hh3cIfQoSWredGroupNextIndex,
       "hh3cIfQoSWredGroupTable": hh3cIfQoSWredGroupTable,
       "hh3cIfQoSWredGroupEntry": hh3cIfQoSWredGroupEntry,
       "hh3cIfQoSWredGroupIndex": hh3cIfQoSWredGroupIndex,
       "hh3cIfQoSWredGroupName": hh3cIfQoSWredGroupName,
       "hh3cIfQoSWredGroupType": hh3cIfQoSWredGroupType,
       "hh3cIfQoSWredGroupWeightingConstant": hh3cIfQoSWredGroupWeightingConstant,
       "hh3cIfQoSWredGroupRowStatus": hh3cIfQoSWredGroupRowStatus,
       "hh3cIfQoSWredGroupContentTable": hh3cIfQoSWredGroupContentTable,
       "hh3cIfQoSWredGroupContentEntry": hh3cIfQoSWredGroupContentEntry,
       "hh3cIfQoSWredGroupContentIndex": hh3cIfQoSWredGroupContentIndex,
       "hh3cIfQoSWredGroupContentSubIndex": hh3cIfQoSWredGroupContentSubIndex,
       "hh3cIfQoSWredLowLimit": hh3cIfQoSWredLowLimit,
       "hh3cIfQoSWredHighLimit": hh3cIfQoSWredHighLimit,
       "hh3cIfQoSWredDiscardProb": hh3cIfQoSWredDiscardProb,
       "hh3cIfQoSWredGroupExponent": hh3cIfQoSWredGroupExponent,
       "hh3cIfQoSWredRowStatus": hh3cIfQoSWredRowStatus,
       "hh3cIfQoSWredGroupApplyIfTable": hh3cIfQoSWredGroupApplyIfTable,
       "hh3cIfQoSWredGroupApplyIfEntry": hh3cIfQoSWredGroupApplyIfEntry,
       "hh3cIfQoSWredGroupApplyIndex": hh3cIfQoSWredGroupApplyIndex,
       "hh3cIfQoSWredGroupApplyName": hh3cIfQoSWredGroupApplyName,
       "hh3cIfQoSWredGroupIfRowStatus": hh3cIfQoSWredGroupIfRowStatus,
       "hh3cIfQoSWredApplyIfRunInfoTable": hh3cIfQoSWredApplyIfRunInfoTable,
       "hh3cIfQoSWredApplyIfRunInfoEntry": hh3cIfQoSWredApplyIfRunInfoEntry,
       "hh3cIfQoSWredPreRandomDropNum": hh3cIfQoSWredPreRandomDropNum,
       "hh3cIfQoSWredPreTailDropNum": hh3cIfQoSWredPreTailDropNum,
       "hh3cIfQoSPortWredGroup": hh3cIfQoSPortWredGroup,
       "hh3cIfQoSPortWredWeightConstantTable": hh3cIfQoSPortWredWeightConstantTable,
       "hh3cIfQoSPortWredWeightConstantEntry": hh3cIfQoSPortWredWeightConstantEntry,
       "hh3cIfQoSPortWredEnable": hh3cIfQoSPortWredEnable,
       "hh3cIfQoSPortWredWeightConstant": hh3cIfQoSPortWredWeightConstant,
       "hh3cIfQoSPortWredWeightConstantRowStatus": hh3cIfQoSPortWredWeightConstantRowStatus,
       "hh3cIfQoSPortWredPreConfigTable": hh3cIfQoSPortWredPreConfigTable,
       "hh3cIfQoSPortWredPreConfigEntry": hh3cIfQoSPortWredPreConfigEntry,
       "hh3cIfQoSPortWredPreID": hh3cIfQoSPortWredPreID,
       "hh3cIfQoSPortWredPreLowLimit": hh3cIfQoSPortWredPreLowLimit,
       "hh3cIfQoSPortWredPreHighLimit": hh3cIfQoSPortWredPreHighLimit,
       "hh3cIfQoSPortWredPreDiscardProbability": hh3cIfQoSPortWredPreDiscardProbability,
       "hh3cIfQoSPortWredPreRowStatus": hh3cIfQoSPortWredPreRowStatus,
       "hh3cIfQoSPortWredRunInfoTable": hh3cIfQoSPortWredRunInfoTable,
       "hh3cIfQoSPortWredRunInfoEntry": hh3cIfQoSPortWredRunInfoEntry,
       "hh3cIfQoSWREDTailDropNum": hh3cIfQoSWREDTailDropNum,
       "hh3cIfQoSWREDRandomDropNum": hh3cIfQoSWREDRandomDropNum,
       "hh3cIfQoSPortPriorityObjects": hh3cIfQoSPortPriorityObjects,
       "hh3cIfQoSPortPriorityConfigGroup": hh3cIfQoSPortPriorityConfigGroup,
       "hh3cIfQoSPortPriorityTable": hh3cIfQoSPortPriorityTable,
       "hh3cIfQoSPortPriorityEntry": hh3cIfQoSPortPriorityEntry,
       "hh3cIfQoSPortPriorityValue": hh3cIfQoSPortPriorityValue,
       "hh3cIfQoSPortPirorityTrustTable": hh3cIfQoSPortPirorityTrustTable,
       "hh3cIfQoSPortPirorityTrustEntry": hh3cIfQoSPortPirorityTrustEntry,
       "hh3cIfQoSPortPriorityTrustTrustType": hh3cIfQoSPortPriorityTrustTrustType,
       "hh3cIfQoSPortPriorityTrustOvercastType": hh3cIfQoSPortPriorityTrustOvercastType,
       "hh3cIfQoSMapObjects": hh3cIfQoSMapObjects,
       "hh3cIfQoSPriMapConfigGroup": hh3cIfQoSPriMapConfigGroup,
       "hh3cIfQoSPriMapGroupNextIndex": hh3cIfQoSPriMapGroupNextIndex,
       "hh3cIfQoSPriMapGroupTable": hh3cIfQoSPriMapGroupTable,
       "hh3cIfQoSPriMapGroupEntry": hh3cIfQoSPriMapGroupEntry,
       "hh3cIfQoSPriMapGroupIndex": hh3cIfQoSPriMapGroupIndex,
       "hh3cIfQoSPriMapGroupType": hh3cIfQoSPriMapGroupType,
       "hh3cIfQoSPriMapGroupName": hh3cIfQoSPriMapGroupName,
       "hh3cIfQoSPriMapGroupRowStatus": hh3cIfQoSPriMapGroupRowStatus,
       "hh3cIfQoSPriMapContentTable": hh3cIfQoSPriMapContentTable,
       "hh3cIfQoSPriMapContentEntry": hh3cIfQoSPriMapContentEntry,
       "hh3cIfQoSPriMapGroupImportValue": hh3cIfQoSPriMapGroupImportValue,
       "hh3cIfQoSPriMapGroupExportValue": hh3cIfQoSPriMapGroupExportValue,
       "hh3cIfQoSPriMapContentRowStatus": hh3cIfQoSPriMapContentRowStatus,
       "hh3cIfQoSL3PlusObjects": hh3cIfQoSL3PlusObjects,
       "hh3cIfQoSPortBindingGroup": hh3cIfQoSPortBindingGroup,
       "hh3cIfQoSPortBindingTable": hh3cIfQoSPortBindingTable,
       "hh3cIfQoSPortBindingEntry": hh3cIfQoSPortBindingEntry,
       "hh3cIfQoSBindingIf": hh3cIfQoSBindingIf,
       "hh3cIfQoSBindingRowStatus": hh3cIfQoSBindingRowStatus,
       "hh3cQoSTraStaObjects": hh3cQoSTraStaObjects,
       "hh3cQoSTraStaConfigGroup": hh3cQoSTraStaConfigGroup,
       "hh3cQoSIfTraStaConfigInfoTable": hh3cQoSIfTraStaConfigInfoTable,
       "hh3cQoSIfTraStaConfigInfoEntry": hh3cQoSIfTraStaConfigInfoEntry,
       "hh3cQoSIfTraStaConfigDirection": hh3cQoSIfTraStaConfigDirection,
       "hh3cQoSIfTraStaConfigQueue": hh3cQoSIfTraStaConfigQueue,
       "hh3cQoSIfTraStaConfigDot1p": hh3cQoSIfTraStaConfigDot1p,
       "hh3cQoSIfTraStaConfigDscp": hh3cQoSIfTraStaConfigDscp,
       "hh3cQoSIfTraStaConfigVlan": hh3cQoSIfTraStaConfigVlan,
       "hh3cQoSIfTraStaConfigStatus": hh3cQoSIfTraStaConfigStatus,
       "hh3cQoSTraStaRunGroup": hh3cQoSTraStaRunGroup,
       "hh3cQoSIfTraStaRunInfoTable": hh3cQoSIfTraStaRunInfoTable,
       "hh3cQoSIfTraStaRunInfoEntry": hh3cQoSIfTraStaRunInfoEntry,
       "hh3cQoSIfTraStaRunObjectType": hh3cQoSIfTraStaRunObjectType,
       "hh3cQoSIfTraStaRunObjectValue": hh3cQoSIfTraStaRunObjectValue,
       "hh3cQoSIfTraStaRunDirection": hh3cQoSIfTraStaRunDirection,
       "hh3cQoSIfTraStaRunPassPackets": hh3cQoSIfTraStaRunPassPackets,
       "hh3cQoSIfTraStaRunDropPackets": hh3cQoSIfTraStaRunDropPackets,
       "hh3cQoSIfTraStaRunPassBytes": hh3cQoSIfTraStaRunPassBytes,
       "hh3cQoSIfTraStaRunDropBytes": hh3cQoSIfTraStaRunDropBytes,
       "hh3cQoSIfTraStaRunPassPPS": hh3cQoSIfTraStaRunPassPPS,
       "hh3cQoSIfTraStaRunPassBPS": hh3cQoSIfTraStaRunPassBPS}
)
