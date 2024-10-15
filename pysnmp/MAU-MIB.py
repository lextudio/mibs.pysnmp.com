# SNMP MIB module (MAU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MAU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:15 2024
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

(IANAifJackType,
 IANAifMauAutoNegCapBits,
 IANAifMauMediaAvailable,
 IANAifMauTypeListBits) = mibBuilder.importSymbols(
    "IANA-MAU-MIB",
    "IANAifJackType",
    "IANAifMauAutoNegCapBits",
    "IANAifMauMediaAvailable",
    "IANAifMauTypeListBits")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 mib_2) = mibBuilder.importSymbols(
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
    "mib-2")

(AutonomousType,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mauMod = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 26, 6)
)
mauMod.setRevisions(
        ("2007-04-21 00:00",
         "2003-09-19 00:00",
         "1999-08-24 04:00",
         "1997-10-31 00:00",
         "1993-09-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JackType(Integer32, TextualConvention):
    status = "deprecated"
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("bnc", 5),
          ("db9", 4),
          ("fAUI", 6),
          ("fiberLC", 14),
          ("fiberMIC", 9),
          ("fiberSC", 8),
          ("fiberST", 10),
          ("hssdc", 13),
          ("mAUI", 7),
          ("mtrj", 12),
          ("other", 1),
          ("rj45", 2),
          ("rj45S", 3),
          ("telco", 11))
    )



# MIB Managed Objects in the order of their OIDs

_SnmpDot3MauMgt_ObjectIdentity = ObjectIdentity
snmpDot3MauMgt = _SnmpDot3MauMgt_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26)
)
_SnmpDot3MauTraps_ObjectIdentity = ObjectIdentity
snmpDot3MauTraps = _SnmpDot3MauTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 0)
)
_Dot3RpMauBasicGroup_ObjectIdentity = ObjectIdentity
dot3RpMauBasicGroup = _Dot3RpMauBasicGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 1)
)
_RpMauTable_Object = MibTable
rpMauTable = _RpMauTable_Object(
    (1, 3, 6, 1, 2, 1, 26, 1, 1)
)
if mibBuilder.loadTexts:
    rpMauTable.setStatus("current")
_RpMauEntry_Object = MibTableRow
rpMauEntry = _RpMauEntry_Object(
    (1, 3, 6, 1, 2, 1, 26, 1, 1, 1)
)
rpMauEntry.setIndexNames(
    (0, "MAU-MIB", "rpMauGroupIndex"),
    (0, "MAU-MIB", "rpMauPortIndex"),
    (0, "MAU-MIB", "rpMauIndex"),
)
if mibBuilder.loadTexts:
    rpMauEntry.setStatus("current")


class _RpMauGroupIndex_Type(Integer32):
    """Custom type rpMauGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RpMauGroupIndex_Type.__name__ = "Integer32"
_RpMauGroupIndex_Object = MibTableColumn
rpMauGroupIndex = _RpMauGroupIndex_Object(
    (1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 1),
    _RpMauGroupIndex_Type()
)
rpMauGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauGroupIndex.setStatus("current")


class _RpMauPortIndex_Type(Integer32):
    """Custom type rpMauPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RpMauPortIndex_Type.__name__ = "Integer32"
_RpMauPortIndex_Object = MibTableColumn
rpMauPortIndex = _RpMauPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 2),
    _RpMauPortIndex_Type()
)
rpMauPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauPortIndex.setStatus("current")


class _RpMauIndex_Type(Integer32):
    """Custom type rpMauIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RpMauIndex_Type.__name__ = "Integer32"
_RpMauIndex_Object = MibTableColumn
rpMauIndex = _RpMauIndex_Object(
    (1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 3),
    _RpMauIndex_Type()
)
rpMauIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauIndex.setStatus("current")
_RpMauType_Type = AutonomousType
_RpMauType_Object = MibTableColumn
rpMauType = _RpMauType_Object(
    (1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 4),
    _RpMauType_Type()
)
rpMauType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauType.setStatus("current")


class _RpMauStatus_Type(Integer32):
    """Custom type rpMauStatus based on Integer32"""
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
        *(("operational", 3),
          ("other", 1),
          ("reset", 6),
          ("shutdown", 5),
          ("standby", 4),
          ("unknown", 2))
    )


_RpMauStatus_Type.__name__ = "Integer32"
_RpMauStatus_Object = MibTableColumn
rpMauStatus = _RpMauStatus_Object(
    (1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 5),
    _RpMauStatus_Type()
)
rpMauStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rpMauStatus.setStatus("current")
_RpMauMediaAvailable_Type = IANAifMauMediaAvailable
_RpMauMediaAvailable_Object = MibTableColumn
rpMauMediaAvailable = _RpMauMediaAvailable_Object(
    (1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 6),
    _RpMauMediaAvailable_Type()
)
rpMauMediaAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauMediaAvailable.setStatus("current")
_RpMauMediaAvailableStateExits_Type = Counter32
_RpMauMediaAvailableStateExits_Object = MibTableColumn
rpMauMediaAvailableStateExits = _RpMauMediaAvailableStateExits_Object(
    (1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 7),
    _RpMauMediaAvailableStateExits_Type()
)
rpMauMediaAvailableStateExits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauMediaAvailableStateExits.setStatus("current")


class _RpMauJabberState_Type(Integer32):
    """Custom type rpMauJabberState based on Integer32"""
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
        *(("jabbering", 4),
          ("noJabber", 3),
          ("other", 1),
          ("unknown", 2))
    )


_RpMauJabberState_Type.__name__ = "Integer32"
_RpMauJabberState_Object = MibTableColumn
rpMauJabberState = _RpMauJabberState_Object(
    (1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 8),
    _RpMauJabberState_Type()
)
rpMauJabberState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauJabberState.setStatus("current")
_RpMauJabberingStateEnters_Type = Counter32
_RpMauJabberingStateEnters_Object = MibTableColumn
rpMauJabberingStateEnters = _RpMauJabberingStateEnters_Object(
    (1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 9),
    _RpMauJabberingStateEnters_Type()
)
rpMauJabberingStateEnters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauJabberingStateEnters.setStatus("current")
_RpMauFalseCarriers_Type = Counter32
_RpMauFalseCarriers_Object = MibTableColumn
rpMauFalseCarriers = _RpMauFalseCarriers_Object(
    (1, 3, 6, 1, 2, 1, 26, 1, 1, 1, 10),
    _RpMauFalseCarriers_Type()
)
rpMauFalseCarriers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpMauFalseCarriers.setStatus("current")
_RpJackTable_Object = MibTable
rpJackTable = _RpJackTable_Object(
    (1, 3, 6, 1, 2, 1, 26, 1, 2)
)
if mibBuilder.loadTexts:
    rpJackTable.setStatus("current")
_RpJackEntry_Object = MibTableRow
rpJackEntry = _RpJackEntry_Object(
    (1, 3, 6, 1, 2, 1, 26, 1, 2, 1)
)
rpJackEntry.setIndexNames(
    (0, "MAU-MIB", "rpMauGroupIndex"),
    (0, "MAU-MIB", "rpMauPortIndex"),
    (0, "MAU-MIB", "rpMauIndex"),
    (0, "MAU-MIB", "rpJackIndex"),
)
if mibBuilder.loadTexts:
    rpJackEntry.setStatus("current")


class _RpJackIndex_Type(Integer32):
    """Custom type rpJackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RpJackIndex_Type.__name__ = "Integer32"
_RpJackIndex_Object = MibTableColumn
rpJackIndex = _RpJackIndex_Object(
    (1, 3, 6, 1, 2, 1, 26, 1, 2, 1, 1),
    _RpJackIndex_Type()
)
rpJackIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rpJackIndex.setStatus("current")
_RpJackType_Type = IANAifJackType
_RpJackType_Object = MibTableColumn
rpJackType = _RpJackType_Object(
    (1, 3, 6, 1, 2, 1, 26, 1, 2, 1, 2),
    _RpJackType_Type()
)
rpJackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpJackType.setStatus("current")
_Dot3IfMauBasicGroup_ObjectIdentity = ObjectIdentity
dot3IfMauBasicGroup = _Dot3IfMauBasicGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 2)
)
_IfMauTable_Object = MibTable
ifMauTable = _IfMauTable_Object(
    (1, 3, 6, 1, 2, 1, 26, 2, 1)
)
if mibBuilder.loadTexts:
    ifMauTable.setStatus("current")
_IfMauEntry_Object = MibTableRow
ifMauEntry = _IfMauEntry_Object(
    (1, 3, 6, 1, 2, 1, 26, 2, 1, 1)
)
ifMauEntry.setIndexNames(
    (0, "MAU-MIB", "ifMauIfIndex"),
    (0, "MAU-MIB", "ifMauIndex"),
)
if mibBuilder.loadTexts:
    ifMauEntry.setStatus("current")
_IfMauIfIndex_Type = InterfaceIndex
_IfMauIfIndex_Object = MibTableColumn
ifMauIfIndex = _IfMauIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 1),
    _IfMauIfIndex_Type()
)
ifMauIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauIfIndex.setStatus("current")


class _IfMauIndex_Type(Integer32):
    """Custom type ifMauIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IfMauIndex_Type.__name__ = "Integer32"
_IfMauIndex_Object = MibTableColumn
ifMauIndex = _IfMauIndex_Object(
    (1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 2),
    _IfMauIndex_Type()
)
ifMauIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauIndex.setStatus("current")
_IfMauType_Type = AutonomousType
_IfMauType_Object = MibTableColumn
ifMauType = _IfMauType_Object(
    (1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 3),
    _IfMauType_Type()
)
ifMauType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauType.setStatus("current")


class _IfMauStatus_Type(Integer32):
    """Custom type ifMauStatus based on Integer32"""
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
        *(("operational", 3),
          ("other", 1),
          ("reset", 6),
          ("shutdown", 5),
          ("standby", 4),
          ("unknown", 2))
    )


_IfMauStatus_Type.__name__ = "Integer32"
_IfMauStatus_Object = MibTableColumn
ifMauStatus = _IfMauStatus_Object(
    (1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 4),
    _IfMauStatus_Type()
)
ifMauStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMauStatus.setStatus("current")
_IfMauMediaAvailable_Type = IANAifMauMediaAvailable
_IfMauMediaAvailable_Object = MibTableColumn
ifMauMediaAvailable = _IfMauMediaAvailable_Object(
    (1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 5),
    _IfMauMediaAvailable_Type()
)
ifMauMediaAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauMediaAvailable.setStatus("current")
_IfMauMediaAvailableStateExits_Type = Counter32
_IfMauMediaAvailableStateExits_Object = MibTableColumn
ifMauMediaAvailableStateExits = _IfMauMediaAvailableStateExits_Object(
    (1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 6),
    _IfMauMediaAvailableStateExits_Type()
)
ifMauMediaAvailableStateExits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauMediaAvailableStateExits.setStatus("current")


class _IfMauJabberState_Type(Integer32):
    """Custom type ifMauJabberState based on Integer32"""
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
        *(("jabbering", 4),
          ("noJabber", 3),
          ("other", 1),
          ("unknown", 2))
    )


_IfMauJabberState_Type.__name__ = "Integer32"
_IfMauJabberState_Object = MibTableColumn
ifMauJabberState = _IfMauJabberState_Object(
    (1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 7),
    _IfMauJabberState_Type()
)
ifMauJabberState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauJabberState.setStatus("current")
_IfMauJabberingStateEnters_Type = Counter32
_IfMauJabberingStateEnters_Object = MibTableColumn
ifMauJabberingStateEnters = _IfMauJabberingStateEnters_Object(
    (1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 8),
    _IfMauJabberingStateEnters_Type()
)
ifMauJabberingStateEnters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauJabberingStateEnters.setStatus("current")
_IfMauFalseCarriers_Type = Counter32
_IfMauFalseCarriers_Object = MibTableColumn
ifMauFalseCarriers = _IfMauFalseCarriers_Object(
    (1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 9),
    _IfMauFalseCarriers_Type()
)
ifMauFalseCarriers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauFalseCarriers.setStatus("current")
_IfMauTypeList_Type = Integer32
_IfMauTypeList_Object = MibTableColumn
ifMauTypeList = _IfMauTypeList_Object(
    (1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 10),
    _IfMauTypeList_Type()
)
ifMauTypeList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauTypeList.setStatus("deprecated")
_IfMauDefaultType_Type = AutonomousType
_IfMauDefaultType_Object = MibTableColumn
ifMauDefaultType = _IfMauDefaultType_Object(
    (1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 11),
    _IfMauDefaultType_Type()
)
ifMauDefaultType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMauDefaultType.setStatus("current")
_IfMauAutoNegSupported_Type = TruthValue
_IfMauAutoNegSupported_Object = MibTableColumn
ifMauAutoNegSupported = _IfMauAutoNegSupported_Object(
    (1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 12),
    _IfMauAutoNegSupported_Type()
)
ifMauAutoNegSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauAutoNegSupported.setStatus("current")
_IfMauTypeListBits_Type = IANAifMauTypeListBits
_IfMauTypeListBits_Object = MibTableColumn
ifMauTypeListBits = _IfMauTypeListBits_Object(
    (1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 13),
    _IfMauTypeListBits_Type()
)
ifMauTypeListBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauTypeListBits.setStatus("current")
_IfMauHCFalseCarriers_Type = Counter64
_IfMauHCFalseCarriers_Object = MibTableColumn
ifMauHCFalseCarriers = _IfMauHCFalseCarriers_Object(
    (1, 3, 6, 1, 2, 1, 26, 2, 1, 1, 14),
    _IfMauHCFalseCarriers_Type()
)
ifMauHCFalseCarriers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauHCFalseCarriers.setStatus("current")
_IfJackTable_Object = MibTable
ifJackTable = _IfJackTable_Object(
    (1, 3, 6, 1, 2, 1, 26, 2, 2)
)
if mibBuilder.loadTexts:
    ifJackTable.setStatus("current")
_IfJackEntry_Object = MibTableRow
ifJackEntry = _IfJackEntry_Object(
    (1, 3, 6, 1, 2, 1, 26, 2, 2, 1)
)
ifJackEntry.setIndexNames(
    (0, "MAU-MIB", "ifMauIfIndex"),
    (0, "MAU-MIB", "ifMauIndex"),
    (0, "MAU-MIB", "ifJackIndex"),
)
if mibBuilder.loadTexts:
    ifJackEntry.setStatus("current")


class _IfJackIndex_Type(Integer32):
    """Custom type ifJackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IfJackIndex_Type.__name__ = "Integer32"
_IfJackIndex_Object = MibTableColumn
ifJackIndex = _IfJackIndex_Object(
    (1, 3, 6, 1, 2, 1, 26, 2, 2, 1, 1),
    _IfJackIndex_Type()
)
ifJackIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifJackIndex.setStatus("current")
_IfJackType_Type = IANAifJackType
_IfJackType_Object = MibTableColumn
ifJackType = _IfJackType_Object(
    (1, 3, 6, 1, 2, 1, 26, 2, 2, 1, 2),
    _IfJackType_Type()
)
ifJackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifJackType.setStatus("current")
_Dot3BroadMauBasicGroup_ObjectIdentity = ObjectIdentity
dot3BroadMauBasicGroup = _Dot3BroadMauBasicGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 3)
)
_BroadMauBasicTable_Object = MibTable
broadMauBasicTable = _BroadMauBasicTable_Object(
    (1, 3, 6, 1, 2, 1, 26, 3, 1)
)
if mibBuilder.loadTexts:
    broadMauBasicTable.setStatus("deprecated")
_BroadMauBasicEntry_Object = MibTableRow
broadMauBasicEntry = _BroadMauBasicEntry_Object(
    (1, 3, 6, 1, 2, 1, 26, 3, 1, 1)
)
broadMauBasicEntry.setIndexNames(
    (0, "MAU-MIB", "broadMauIfIndex"),
    (0, "MAU-MIB", "broadMauIndex"),
)
if mibBuilder.loadTexts:
    broadMauBasicEntry.setStatus("deprecated")
_BroadMauIfIndex_Type = InterfaceIndex
_BroadMauIfIndex_Object = MibTableColumn
broadMauIfIndex = _BroadMauIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 26, 3, 1, 1, 1),
    _BroadMauIfIndex_Type()
)
broadMauIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    broadMauIfIndex.setStatus("deprecated")


class _BroadMauIndex_Type(Integer32):
    """Custom type broadMauIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BroadMauIndex_Type.__name__ = "Integer32"
_BroadMauIndex_Object = MibTableColumn
broadMauIndex = _BroadMauIndex_Object(
    (1, 3, 6, 1, 2, 1, 26, 3, 1, 1, 2),
    _BroadMauIndex_Type()
)
broadMauIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    broadMauIndex.setStatus("deprecated")


class _BroadMauXmtRcvSplitType_Type(Integer32):
    """Custom type broadMauXmtRcvSplitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dual", 3),
          ("other", 1),
          ("single", 2))
    )


_BroadMauXmtRcvSplitType_Type.__name__ = "Integer32"
_BroadMauXmtRcvSplitType_Object = MibTableColumn
broadMauXmtRcvSplitType = _BroadMauXmtRcvSplitType_Object(
    (1, 3, 6, 1, 2, 1, 26, 3, 1, 1, 3),
    _BroadMauXmtRcvSplitType_Type()
)
broadMauXmtRcvSplitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    broadMauXmtRcvSplitType.setStatus("deprecated")
_BroadMauXmtCarrierFreq_Type = Integer32
_BroadMauXmtCarrierFreq_Object = MibTableColumn
broadMauXmtCarrierFreq = _BroadMauXmtCarrierFreq_Object(
    (1, 3, 6, 1, 2, 1, 26, 3, 1, 1, 4),
    _BroadMauXmtCarrierFreq_Type()
)
broadMauXmtCarrierFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    broadMauXmtCarrierFreq.setStatus("deprecated")
_BroadMauTranslationFreq_Type = Integer32
_BroadMauTranslationFreq_Object = MibTableColumn
broadMauTranslationFreq = _BroadMauTranslationFreq_Object(
    (1, 3, 6, 1, 2, 1, 26, 3, 1, 1, 5),
    _BroadMauTranslationFreq_Type()
)
broadMauTranslationFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    broadMauTranslationFreq.setStatus("deprecated")
_Dot3IfMauAutoNegGroup_ObjectIdentity = ObjectIdentity
dot3IfMauAutoNegGroup = _Dot3IfMauAutoNegGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 5)
)
_IfMauAutoNegTable_Object = MibTable
ifMauAutoNegTable = _IfMauAutoNegTable_Object(
    (1, 3, 6, 1, 2, 1, 26, 5, 1)
)
if mibBuilder.loadTexts:
    ifMauAutoNegTable.setStatus("current")
_IfMauAutoNegEntry_Object = MibTableRow
ifMauAutoNegEntry = _IfMauAutoNegEntry_Object(
    (1, 3, 6, 1, 2, 1, 26, 5, 1, 1)
)
ifMauAutoNegEntry.setIndexNames(
    (0, "MAU-MIB", "ifMauIfIndex"),
    (0, "MAU-MIB", "ifMauIndex"),
)
if mibBuilder.loadTexts:
    ifMauAutoNegEntry.setStatus("current")


class _IfMauAutoNegAdminStatus_Type(Integer32):
    """Custom type ifMauAutoNegAdminStatus based on Integer32"""
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


_IfMauAutoNegAdminStatus_Type.__name__ = "Integer32"
_IfMauAutoNegAdminStatus_Object = MibTableColumn
ifMauAutoNegAdminStatus = _IfMauAutoNegAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 1),
    _IfMauAutoNegAdminStatus_Type()
)
ifMauAutoNegAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMauAutoNegAdminStatus.setStatus("current")


class _IfMauAutoNegRemoteSignaling_Type(Integer32):
    """Custom type ifMauAutoNegRemoteSignaling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detected", 1),
          ("notdetected", 2))
    )


_IfMauAutoNegRemoteSignaling_Type.__name__ = "Integer32"
_IfMauAutoNegRemoteSignaling_Object = MibTableColumn
ifMauAutoNegRemoteSignaling = _IfMauAutoNegRemoteSignaling_Object(
    (1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 2),
    _IfMauAutoNegRemoteSignaling_Type()
)
ifMauAutoNegRemoteSignaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauAutoNegRemoteSignaling.setStatus("current")


class _IfMauAutoNegConfig_Type(Integer32):
    """Custom type ifMauAutoNegConfig based on Integer32"""
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
        *(("complete", 3),
          ("configuring", 2),
          ("disabled", 4),
          ("other", 1),
          ("parallelDetectFail", 5))
    )


_IfMauAutoNegConfig_Type.__name__ = "Integer32"
_IfMauAutoNegConfig_Object = MibTableColumn
ifMauAutoNegConfig = _IfMauAutoNegConfig_Object(
    (1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 4),
    _IfMauAutoNegConfig_Type()
)
ifMauAutoNegConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauAutoNegConfig.setStatus("current")
_IfMauAutoNegCapability_Type = Integer32
_IfMauAutoNegCapability_Object = MibTableColumn
ifMauAutoNegCapability = _IfMauAutoNegCapability_Object(
    (1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 5),
    _IfMauAutoNegCapability_Type()
)
ifMauAutoNegCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauAutoNegCapability.setStatus("deprecated")
_IfMauAutoNegCapAdvertised_Type = Integer32
_IfMauAutoNegCapAdvertised_Object = MibTableColumn
ifMauAutoNegCapAdvertised = _IfMauAutoNegCapAdvertised_Object(
    (1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 6),
    _IfMauAutoNegCapAdvertised_Type()
)
ifMauAutoNegCapAdvertised.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMauAutoNegCapAdvertised.setStatus("deprecated")
_IfMauAutoNegCapReceived_Type = Integer32
_IfMauAutoNegCapReceived_Object = MibTableColumn
ifMauAutoNegCapReceived = _IfMauAutoNegCapReceived_Object(
    (1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 7),
    _IfMauAutoNegCapReceived_Type()
)
ifMauAutoNegCapReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauAutoNegCapReceived.setStatus("deprecated")


class _IfMauAutoNegRestart_Type(Integer32):
    """Custom type ifMauAutoNegRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norestart", 2),
          ("restart", 1))
    )


_IfMauAutoNegRestart_Type.__name__ = "Integer32"
_IfMauAutoNegRestart_Object = MibTableColumn
ifMauAutoNegRestart = _IfMauAutoNegRestart_Object(
    (1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 8),
    _IfMauAutoNegRestart_Type()
)
ifMauAutoNegRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMauAutoNegRestart.setStatus("current")
_IfMauAutoNegCapabilityBits_Type = IANAifMauAutoNegCapBits
_IfMauAutoNegCapabilityBits_Object = MibTableColumn
ifMauAutoNegCapabilityBits = _IfMauAutoNegCapabilityBits_Object(
    (1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 9),
    _IfMauAutoNegCapabilityBits_Type()
)
ifMauAutoNegCapabilityBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauAutoNegCapabilityBits.setStatus("current")
_IfMauAutoNegCapAdvertisedBits_Type = IANAifMauAutoNegCapBits
_IfMauAutoNegCapAdvertisedBits_Object = MibTableColumn
ifMauAutoNegCapAdvertisedBits = _IfMauAutoNegCapAdvertisedBits_Object(
    (1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 10),
    _IfMauAutoNegCapAdvertisedBits_Type()
)
ifMauAutoNegCapAdvertisedBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMauAutoNegCapAdvertisedBits.setStatus("current")
_IfMauAutoNegCapReceivedBits_Type = IANAifMauAutoNegCapBits
_IfMauAutoNegCapReceivedBits_Object = MibTableColumn
ifMauAutoNegCapReceivedBits = _IfMauAutoNegCapReceivedBits_Object(
    (1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 11),
    _IfMauAutoNegCapReceivedBits_Type()
)
ifMauAutoNegCapReceivedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauAutoNegCapReceivedBits.setStatus("current")


class _IfMauAutoNegRemoteFaultAdvertised_Type(Integer32):
    """Custom type ifMauAutoNegRemoteFaultAdvertised based on Integer32"""
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
        *(("autoNegError", 4),
          ("linkFailure", 3),
          ("noError", 1),
          ("offline", 2))
    )


_IfMauAutoNegRemoteFaultAdvertised_Type.__name__ = "Integer32"
_IfMauAutoNegRemoteFaultAdvertised_Object = MibTableColumn
ifMauAutoNegRemoteFaultAdvertised = _IfMauAutoNegRemoteFaultAdvertised_Object(
    (1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 12),
    _IfMauAutoNegRemoteFaultAdvertised_Type()
)
ifMauAutoNegRemoteFaultAdvertised.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMauAutoNegRemoteFaultAdvertised.setStatus("current")


class _IfMauAutoNegRemoteFaultReceived_Type(Integer32):
    """Custom type ifMauAutoNegRemoteFaultReceived based on Integer32"""
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
        *(("autoNegError", 4),
          ("linkFailure", 3),
          ("noError", 1),
          ("offline", 2))
    )


_IfMauAutoNegRemoteFaultReceived_Type.__name__ = "Integer32"
_IfMauAutoNegRemoteFaultReceived_Object = MibTableColumn
ifMauAutoNegRemoteFaultReceived = _IfMauAutoNegRemoteFaultReceived_Object(
    (1, 3, 6, 1, 2, 1, 26, 5, 1, 1, 13),
    _IfMauAutoNegRemoteFaultReceived_Type()
)
ifMauAutoNegRemoteFaultReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMauAutoNegRemoteFaultReceived.setStatus("current")
_MauModConf_ObjectIdentity = ObjectIdentity
mauModConf = _MauModConf_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 6, 1)
)
_MauModCompls_ObjectIdentity = ObjectIdentity
mauModCompls = _MauModCompls_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 6, 1, 1)
)
_MauModObjGrps_ObjectIdentity = ObjectIdentity
mauModObjGrps = _MauModObjGrps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 6, 1, 2)
)
_MauModNotGrps_ObjectIdentity = ObjectIdentity
mauModNotGrps = _MauModNotGrps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 26, 6, 1, 3)
)

# Managed Objects groups

mauRpGrpBasic = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 1)
)
mauRpGrpBasic.setObjects(
      *(("MAU-MIB", "rpMauGroupIndex"),
        ("MAU-MIB", "rpMauPortIndex"),
        ("MAU-MIB", "rpMauIndex"),
        ("MAU-MIB", "rpMauType"),
        ("MAU-MIB", "rpMauStatus"),
        ("MAU-MIB", "rpMauMediaAvailable"),
        ("MAU-MIB", "rpMauMediaAvailableStateExits"),
        ("MAU-MIB", "rpMauJabberState"),
        ("MAU-MIB", "rpMauJabberingStateEnters"))
)
if mibBuilder.loadTexts:
    mauRpGrpBasic.setStatus("current")

mauRpGrp100Mbs = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 2)
)
mauRpGrp100Mbs.setObjects(
    ("MAU-MIB", "rpMauFalseCarriers")
)
if mibBuilder.loadTexts:
    mauRpGrp100Mbs.setStatus("current")

mauRpGrpJack = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 3)
)
mauRpGrpJack.setObjects(
    ("MAU-MIB", "rpJackType")
)
if mibBuilder.loadTexts:
    mauRpGrpJack.setStatus("current")

mauIfGrpBasic = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 4)
)
mauIfGrpBasic.setObjects(
      *(("MAU-MIB", "ifMauIfIndex"),
        ("MAU-MIB", "ifMauIndex"),
        ("MAU-MIB", "ifMauType"),
        ("MAU-MIB", "ifMauStatus"),
        ("MAU-MIB", "ifMauMediaAvailable"),
        ("MAU-MIB", "ifMauMediaAvailableStateExits"),
        ("MAU-MIB", "ifMauJabberState"),
        ("MAU-MIB", "ifMauJabberingStateEnters"))
)
if mibBuilder.loadTexts:
    mauIfGrpBasic.setStatus("current")

mauIfGrp100Mbs = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 5)
)
mauIfGrp100Mbs.setObjects(
      *(("MAU-MIB", "ifMauFalseCarriers"),
        ("MAU-MIB", "ifMauTypeList"),
        ("MAU-MIB", "ifMauDefaultType"),
        ("MAU-MIB", "ifMauAutoNegSupported"))
)
if mibBuilder.loadTexts:
    mauIfGrp100Mbs.setStatus("deprecated")

mauIfGrpJack = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 6)
)
mauIfGrpJack.setObjects(
    ("MAU-MIB", "ifJackType")
)
if mibBuilder.loadTexts:
    mauIfGrpJack.setStatus("current")

mauIfGrpAutoNeg = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 7)
)
mauIfGrpAutoNeg.setObjects(
      *(("MAU-MIB", "ifMauAutoNegAdminStatus"),
        ("MAU-MIB", "ifMauAutoNegRemoteSignaling"),
        ("MAU-MIB", "ifMauAutoNegConfig"),
        ("MAU-MIB", "ifMauAutoNegCapability"),
        ("MAU-MIB", "ifMauAutoNegCapAdvertised"),
        ("MAU-MIB", "ifMauAutoNegCapReceived"),
        ("MAU-MIB", "ifMauAutoNegRestart"))
)
if mibBuilder.loadTexts:
    mauIfGrpAutoNeg.setStatus("deprecated")

mauBroadBasic = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 8)
)
mauBroadBasic.setObjects(
      *(("MAU-MIB", "broadMauIfIndex"),
        ("MAU-MIB", "broadMauIndex"),
        ("MAU-MIB", "broadMauXmtRcvSplitType"),
        ("MAU-MIB", "broadMauXmtCarrierFreq"),
        ("MAU-MIB", "broadMauTranslationFreq"))
)
if mibBuilder.loadTexts:
    mauBroadBasic.setStatus("deprecated")

mauIfGrpHighCapacity = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 9)
)
mauIfGrpHighCapacity.setObjects(
      *(("MAU-MIB", "ifMauFalseCarriers"),
        ("MAU-MIB", "ifMauTypeListBits"),
        ("MAU-MIB", "ifMauDefaultType"),
        ("MAU-MIB", "ifMauAutoNegSupported"))
)
if mibBuilder.loadTexts:
    mauIfGrpHighCapacity.setStatus("current")

mauIfGrpAutoNeg2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 10)
)
mauIfGrpAutoNeg2.setObjects(
      *(("MAU-MIB", "ifMauAutoNegAdminStatus"),
        ("MAU-MIB", "ifMauAutoNegRemoteSignaling"),
        ("MAU-MIB", "ifMauAutoNegConfig"),
        ("MAU-MIB", "ifMauAutoNegCapabilityBits"),
        ("MAU-MIB", "ifMauAutoNegCapAdvertisedBits"),
        ("MAU-MIB", "ifMauAutoNegCapReceivedBits"),
        ("MAU-MIB", "ifMauAutoNegRestart"))
)
if mibBuilder.loadTexts:
    mauIfGrpAutoNeg2.setStatus("current")

mauIfGrpAutoNeg1000Mbps = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 11)
)
mauIfGrpAutoNeg1000Mbps.setObjects(
      *(("MAU-MIB", "ifMauAutoNegRemoteFaultAdvertised"),
        ("MAU-MIB", "ifMauAutoNegRemoteFaultReceived"))
)
if mibBuilder.loadTexts:
    mauIfGrpAutoNeg1000Mbps.setStatus("current")

mauIfGrpHCStats = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 26, 6, 1, 2, 12)
)
mauIfGrpHCStats.setObjects(
    ("MAU-MIB", "ifMauHCFalseCarriers")
)
if mibBuilder.loadTexts:
    mauIfGrpHCStats.setStatus("current")


# Notification objects

rpMauJabberTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 26, 0, 1)
)
rpMauJabberTrap.setObjects(
    ("MAU-MIB", "rpMauJabberState")
)
if mibBuilder.loadTexts:
    rpMauJabberTrap.setStatus(
        "current"
    )

ifMauJabberTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 26, 0, 2)
)
ifMauJabberTrap.setObjects(
    ("MAU-MIB", "ifMauJabberState")
)
if mibBuilder.loadTexts:
    ifMauJabberTrap.setStatus(
        "current"
    )


# Notifications groups

rpMauNotifications = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 26, 6, 1, 3, 1)
)
rpMauNotifications.setObjects(
    ("MAU-MIB", "rpMauJabberTrap")
)
if mibBuilder.loadTexts:
    rpMauNotifications.setStatus(
        "current"
    )

ifMauNotifications = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 26, 6, 1, 3, 2)
)
ifMauNotifications.setObjects(
    ("MAU-MIB", "ifMauJabberTrap")
)
if mibBuilder.loadTexts:
    ifMauNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mauModRpCompl = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 26, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mauModRpCompl.setStatus(
        "deprecated"
    )

mauModIfCompl = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 26, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mauModIfCompl.setStatus(
        "deprecated"
    )

mauModIfCompl2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 26, 6, 1, 1, 3)
)
if mibBuilder.loadTexts:
    mauModIfCompl2.setStatus(
        "deprecated"
    )

mauModRpCompl2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 26, 6, 1, 1, 4)
)
if mibBuilder.loadTexts:
    mauModRpCompl2.setStatus(
        "current"
    )

mauModIfCompl3 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 26, 6, 1, 1, 5)
)
if mibBuilder.loadTexts:
    mauModIfCompl3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MAU-MIB",
    **{"JackType": JackType,
       "snmpDot3MauMgt": snmpDot3MauMgt,
       "snmpDot3MauTraps": snmpDot3MauTraps,
       "rpMauJabberTrap": rpMauJabberTrap,
       "ifMauJabberTrap": ifMauJabberTrap,
       "dot3RpMauBasicGroup": dot3RpMauBasicGroup,
       "rpMauTable": rpMauTable,
       "rpMauEntry": rpMauEntry,
       "rpMauGroupIndex": rpMauGroupIndex,
       "rpMauPortIndex": rpMauPortIndex,
       "rpMauIndex": rpMauIndex,
       "rpMauType": rpMauType,
       "rpMauStatus": rpMauStatus,
       "rpMauMediaAvailable": rpMauMediaAvailable,
       "rpMauMediaAvailableStateExits": rpMauMediaAvailableStateExits,
       "rpMauJabberState": rpMauJabberState,
       "rpMauJabberingStateEnters": rpMauJabberingStateEnters,
       "rpMauFalseCarriers": rpMauFalseCarriers,
       "rpJackTable": rpJackTable,
       "rpJackEntry": rpJackEntry,
       "rpJackIndex": rpJackIndex,
       "rpJackType": rpJackType,
       "dot3IfMauBasicGroup": dot3IfMauBasicGroup,
       "ifMauTable": ifMauTable,
       "ifMauEntry": ifMauEntry,
       "ifMauIfIndex": ifMauIfIndex,
       "ifMauIndex": ifMauIndex,
       "ifMauType": ifMauType,
       "ifMauStatus": ifMauStatus,
       "ifMauMediaAvailable": ifMauMediaAvailable,
       "ifMauMediaAvailableStateExits": ifMauMediaAvailableStateExits,
       "ifMauJabberState": ifMauJabberState,
       "ifMauJabberingStateEnters": ifMauJabberingStateEnters,
       "ifMauFalseCarriers": ifMauFalseCarriers,
       "ifMauTypeList": ifMauTypeList,
       "ifMauDefaultType": ifMauDefaultType,
       "ifMauAutoNegSupported": ifMauAutoNegSupported,
       "ifMauTypeListBits": ifMauTypeListBits,
       "ifMauHCFalseCarriers": ifMauHCFalseCarriers,
       "ifJackTable": ifJackTable,
       "ifJackEntry": ifJackEntry,
       "ifJackIndex": ifJackIndex,
       "ifJackType": ifJackType,
       "dot3BroadMauBasicGroup": dot3BroadMauBasicGroup,
       "broadMauBasicTable": broadMauBasicTable,
       "broadMauBasicEntry": broadMauBasicEntry,
       "broadMauIfIndex": broadMauIfIndex,
       "broadMauIndex": broadMauIndex,
       "broadMauXmtRcvSplitType": broadMauXmtRcvSplitType,
       "broadMauXmtCarrierFreq": broadMauXmtCarrierFreq,
       "broadMauTranslationFreq": broadMauTranslationFreq,
       "dot3IfMauAutoNegGroup": dot3IfMauAutoNegGroup,
       "ifMauAutoNegTable": ifMauAutoNegTable,
       "ifMauAutoNegEntry": ifMauAutoNegEntry,
       "ifMauAutoNegAdminStatus": ifMauAutoNegAdminStatus,
       "ifMauAutoNegRemoteSignaling": ifMauAutoNegRemoteSignaling,
       "ifMauAutoNegConfig": ifMauAutoNegConfig,
       "ifMauAutoNegCapability": ifMauAutoNegCapability,
       "ifMauAutoNegCapAdvertised": ifMauAutoNegCapAdvertised,
       "ifMauAutoNegCapReceived": ifMauAutoNegCapReceived,
       "ifMauAutoNegRestart": ifMauAutoNegRestart,
       "ifMauAutoNegCapabilityBits": ifMauAutoNegCapabilityBits,
       "ifMauAutoNegCapAdvertisedBits": ifMauAutoNegCapAdvertisedBits,
       "ifMauAutoNegCapReceivedBits": ifMauAutoNegCapReceivedBits,
       "ifMauAutoNegRemoteFaultAdvertised": ifMauAutoNegRemoteFaultAdvertised,
       "ifMauAutoNegRemoteFaultReceived": ifMauAutoNegRemoteFaultReceived,
       "mauMod": mauMod,
       "mauModConf": mauModConf,
       "mauModCompls": mauModCompls,
       "mauModRpCompl": mauModRpCompl,
       "mauModIfCompl": mauModIfCompl,
       "mauModIfCompl2": mauModIfCompl2,
       "mauModRpCompl2": mauModRpCompl2,
       "mauModIfCompl3": mauModIfCompl3,
       "mauModObjGrps": mauModObjGrps,
       "mauRpGrpBasic": mauRpGrpBasic,
       "mauRpGrp100Mbs": mauRpGrp100Mbs,
       "mauRpGrpJack": mauRpGrpJack,
       "mauIfGrpBasic": mauIfGrpBasic,
       "mauIfGrp100Mbs": mauIfGrp100Mbs,
       "mauIfGrpJack": mauIfGrpJack,
       "mauIfGrpAutoNeg": mauIfGrpAutoNeg,
       "mauBroadBasic": mauBroadBasic,
       "mauIfGrpHighCapacity": mauIfGrpHighCapacity,
       "mauIfGrpAutoNeg2": mauIfGrpAutoNeg2,
       "mauIfGrpAutoNeg1000Mbps": mauIfGrpAutoNeg1000Mbps,
       "mauIfGrpHCStats": mauIfGrpHCStats,
       "mauModNotGrps": mauModNotGrps,
       "rpMauNotifications": rpMauNotifications,
       "ifMauNotifications": ifMauNotifications}
)
