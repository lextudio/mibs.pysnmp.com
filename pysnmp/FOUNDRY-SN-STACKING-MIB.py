# SNMP MIB module (FOUNDRY-SN-STACKING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FOUNDRY-SN-STACKING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:01 2024
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

(DisplayString,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-AGENT-MIB",
    "DisplayString")

(snSwitch,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-SWITCH-GROUP-MIB",
    "snSwitch")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

snStacking = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31)
)
snStacking.setRevisions(
        ("2010-06-02 00:00",
         "2008-05-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnStackingGlobalObjects_ObjectIdentity = ObjectIdentity
snStackingGlobalObjects = _SnStackingGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 1)
)


class _SnStackingGlobalConfigState_Type(Integer32):
    """Custom type snStackingGlobalConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("none", 0))
    )


_SnStackingGlobalConfigState_Type.__name__ = "Integer32"
_SnStackingGlobalConfigState_Object = MibScalar
snStackingGlobalConfigState = _SnStackingGlobalConfigState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 1, 1),
    _SnStackingGlobalConfigState_Type()
)
snStackingGlobalConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snStackingGlobalConfigState.setStatus("current")
_SnStackingGlobalMacAddress_Type = MacAddress
_SnStackingGlobalMacAddress_Object = MibScalar
snStackingGlobalMacAddress = _SnStackingGlobalMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 1, 2),
    _SnStackingGlobalMacAddress_Type()
)
snStackingGlobalMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snStackingGlobalMacAddress.setStatus("current")


class _SnStackingGlobalPersistentMacTimerState_Type(Integer32):
    """Custom type snStackingGlobalPersistentMacTimerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_SnStackingGlobalPersistentMacTimerState_Type.__name__ = "Integer32"
_SnStackingGlobalPersistentMacTimerState_Object = MibScalar
snStackingGlobalPersistentMacTimerState = _SnStackingGlobalPersistentMacTimerState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 1, 3),
    _SnStackingGlobalPersistentMacTimerState_Type()
)
snStackingGlobalPersistentMacTimerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snStackingGlobalPersistentMacTimerState.setStatus("current")
_SnStackingGlobalPersistentMacTimer_Type = Integer32
_SnStackingGlobalPersistentMacTimer_Object = MibScalar
snStackingGlobalPersistentMacTimer = _SnStackingGlobalPersistentMacTimer_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 1, 4),
    _SnStackingGlobalPersistentMacTimer_Type()
)
snStackingGlobalPersistentMacTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snStackingGlobalPersistentMacTimer.setStatus("current")


class _SnStackingGlobalTopology_Type(Integer32):
    """Custom type snStackingGlobalTopology based on Integer32"""
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
        *(("chain", 2),
          ("other", 1),
          ("ring", 3),
          ("standalone", 4))
    )


_SnStackingGlobalTopology_Type.__name__ = "Integer32"
_SnStackingGlobalTopology_Object = MibScalar
snStackingGlobalTopology = _SnStackingGlobalTopology_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 1, 5),
    _SnStackingGlobalTopology_Type()
)
snStackingGlobalTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackingGlobalTopology.setStatus("current")


class _SnStackingGlobalMode_Type(Integer32):
    """Custom type snStackingGlobalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonStackingMode", 2),
          ("stackingMode", 1))
    )


_SnStackingGlobalMode_Type.__name__ = "Integer32"
_SnStackingGlobalMode_Object = MibScalar
snStackingGlobalMode = _SnStackingGlobalMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 1, 6),
    _SnStackingGlobalMode_Type()
)
snStackingGlobalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackingGlobalMode.setStatus("current")


class _SnStackingGlobalMixedMode_Type(Integer32):
    """Custom type snStackingGlobalMixedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("classicStackingMode", 2),
          ("mixedStackingMode", 1))
    )


_SnStackingGlobalMixedMode_Type.__name__ = "Integer32"
_SnStackingGlobalMixedMode_Object = MibScalar
snStackingGlobalMixedMode = _SnStackingGlobalMixedMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 1, 7),
    _SnStackingGlobalMixedMode_Type()
)
snStackingGlobalMixedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackingGlobalMixedMode.setStatus("current")
_SnStackingTableObjects_ObjectIdentity = ObjectIdentity
snStackingTableObjects = _SnStackingTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2)
)
_SnStackingConfigUnitTable_Object = MibTable
snStackingConfigUnitTable = _SnStackingConfigUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 1)
)
if mibBuilder.loadTexts:
    snStackingConfigUnitTable.setStatus("current")
_SnStackingConfigUnitEntry_Object = MibTableRow
snStackingConfigUnitEntry = _SnStackingConfigUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 1, 1)
)
snStackingConfigUnitEntry.setIndexNames(
    (0, "FOUNDRY-SN-STACKING-MIB", "snStackingConfigUnitIndex"),
)
if mibBuilder.loadTexts:
    snStackingConfigUnitEntry.setStatus("current")
_SnStackingConfigUnitIndex_Type = Integer32
_SnStackingConfigUnitIndex_Object = MibTableColumn
snStackingConfigUnitIndex = _SnStackingConfigUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 1, 1, 1),
    _SnStackingConfigUnitIndex_Type()
)
snStackingConfigUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snStackingConfigUnitIndex.setStatus("current")


class _SnStackingConfigUnitPriority_Type(Integer32):
    """Custom type snStackingConfigUnitPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnStackingConfigUnitPriority_Type.__name__ = "Integer32"
_SnStackingConfigUnitPriority_Object = MibTableColumn
snStackingConfigUnitPriority = _SnStackingConfigUnitPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 1, 1, 2),
    _SnStackingConfigUnitPriority_Type()
)
snStackingConfigUnitPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snStackingConfigUnitPriority.setStatus("current")
_SnStackingConfigUnitConfigStackPort_Type = InterfaceIndexOrZero
_SnStackingConfigUnitConfigStackPort_Object = MibTableColumn
snStackingConfigUnitConfigStackPort = _SnStackingConfigUnitConfigStackPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 1, 1, 3),
    _SnStackingConfigUnitConfigStackPort_Type()
)
snStackingConfigUnitConfigStackPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snStackingConfigUnitConfigStackPort.setStatus("current")


class _SnStackingConfigUnitRowStatus_Type(Integer32):
    """Custom type snStackingConfigUnitRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("other", 1),
          ("valid", 2))
    )


_SnStackingConfigUnitRowStatus_Type.__name__ = "Integer32"
_SnStackingConfigUnitRowStatus_Object = MibTableColumn
snStackingConfigUnitRowStatus = _SnStackingConfigUnitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 1, 1, 4),
    _SnStackingConfigUnitRowStatus_Type()
)
snStackingConfigUnitRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snStackingConfigUnitRowStatus.setStatus("current")
_SnStackingConfigUnitType_Type = DisplayString
_SnStackingConfigUnitType_Object = MibTableColumn
snStackingConfigUnitType = _SnStackingConfigUnitType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 1, 1, 5),
    _SnStackingConfigUnitType_Type()
)
snStackingConfigUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackingConfigUnitType.setStatus("current")


class _SnStackingConfigUnitState_Type(Integer32):
    """Custom type snStackingConfigUnitState based on Integer32"""
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
        *(("empty", 4),
          ("local", 1),
          ("remote", 2),
          ("reserved", 3))
    )


_SnStackingConfigUnitState_Type.__name__ = "Integer32"
_SnStackingConfigUnitState_Object = MibTableColumn
snStackingConfigUnitState = _SnStackingConfigUnitState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 1, 1, 6),
    _SnStackingConfigUnitState_Type()
)
snStackingConfigUnitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackingConfigUnitState.setStatus("current")
_SnStackingConfigUnitStackPort1_Type = InterfaceIndexOrZero
_SnStackingConfigUnitStackPort1_Object = MibTableColumn
snStackingConfigUnitStackPort1 = _SnStackingConfigUnitStackPort1_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 1, 1, 7),
    _SnStackingConfigUnitStackPort1_Type()
)
snStackingConfigUnitStackPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackingConfigUnitStackPort1.setStatus("current")
_SnStackingConfigUnitStackPort2_Type = InterfaceIndexOrZero
_SnStackingConfigUnitStackPort2_Object = MibTableColumn
snStackingConfigUnitStackPort2 = _SnStackingConfigUnitStackPort2_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 1, 1, 8),
    _SnStackingConfigUnitStackPort2_Type()
)
snStackingConfigUnitStackPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackingConfigUnitStackPort2.setStatus("current")
_SnStackingConfigUnitConnectPort1_Type = InterfaceIndexOrZero
_SnStackingConfigUnitConnectPort1_Object = MibTableColumn
snStackingConfigUnitConnectPort1 = _SnStackingConfigUnitConnectPort1_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 1, 1, 9),
    _SnStackingConfigUnitConnectPort1_Type()
)
snStackingConfigUnitConnectPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snStackingConfigUnitConnectPort1.setStatus("current")
_SnStackingConfigUnitConnectPort2_Type = InterfaceIndexOrZero
_SnStackingConfigUnitConnectPort2_Object = MibTableColumn
snStackingConfigUnitConnectPort2 = _SnStackingConfigUnitConnectPort2_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 1, 1, 10),
    _SnStackingConfigUnitConnectPort2_Type()
)
snStackingConfigUnitConnectPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snStackingConfigUnitConnectPort2.setStatus("current")
_SnStackingOperUnitTable_Object = MibTable
snStackingOperUnitTable = _SnStackingOperUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2)
)
if mibBuilder.loadTexts:
    snStackingOperUnitTable.setStatus("current")
_SnStackingOperUnitEntry_Object = MibTableRow
snStackingOperUnitEntry = _SnStackingOperUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2, 1)
)
snStackingOperUnitEntry.setIndexNames(
    (0, "FOUNDRY-SN-STACKING-MIB", "snStackingOperUnitIndex"),
)
if mibBuilder.loadTexts:
    snStackingOperUnitEntry.setStatus("current")
_SnStackingOperUnitIndex_Type = Integer32
_SnStackingOperUnitIndex_Object = MibTableColumn
snStackingOperUnitIndex = _SnStackingOperUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2, 1, 1),
    _SnStackingOperUnitIndex_Type()
)
snStackingOperUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snStackingOperUnitIndex.setStatus("current")


class _SnStackingOperUnitRole_Type(Integer32):
    """Custom type snStackingOperUnitRole based on Integer32"""
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
        *(("active", 2),
          ("member", 4),
          ("other", 1),
          ("standalone", 5),
          ("standby", 3))
    )


_SnStackingOperUnitRole_Type.__name__ = "Integer32"
_SnStackingOperUnitRole_Object = MibTableColumn
snStackingOperUnitRole = _SnStackingOperUnitRole_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2, 1, 2),
    _SnStackingOperUnitRole_Type()
)
snStackingOperUnitRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackingOperUnitRole.setStatus("current")
_SnStackingOperUnitMac_Type = MacAddress
_SnStackingOperUnitMac_Object = MibTableColumn
snStackingOperUnitMac = _SnStackingOperUnitMac_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2, 1, 3),
    _SnStackingOperUnitMac_Type()
)
snStackingOperUnitMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackingOperUnitMac.setStatus("current")


class _SnStackingOperUnitPriority_Type(Integer32):
    """Custom type snStackingOperUnitPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnStackingOperUnitPriority_Type.__name__ = "Integer32"
_SnStackingOperUnitPriority_Object = MibTableColumn
snStackingOperUnitPriority = _SnStackingOperUnitPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2, 1, 4),
    _SnStackingOperUnitPriority_Type()
)
snStackingOperUnitPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackingOperUnitPriority.setStatus("current")


class _SnStackingOperUnitState_Type(Integer32):
    """Custom type snStackingOperUnitState based on Integer32"""
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
        *(("empty", 4),
          ("local", 1),
          ("remote", 2),
          ("reserved", 3))
    )


_SnStackingOperUnitState_Type.__name__ = "Integer32"
_SnStackingOperUnitState_Object = MibTableColumn
snStackingOperUnitState = _SnStackingOperUnitState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2, 1, 5),
    _SnStackingOperUnitState_Type()
)
snStackingOperUnitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackingOperUnitState.setStatus("current")


class _SnStackingOperUnitDescription_Type(DisplayString):
    """Custom type snStackingOperUnitDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnStackingOperUnitDescription_Type.__name__ = "DisplayString"
_SnStackingOperUnitDescription_Object = MibTableColumn
snStackingOperUnitDescription = _SnStackingOperUnitDescription_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2, 1, 6),
    _SnStackingOperUnitDescription_Type()
)
snStackingOperUnitDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackingOperUnitDescription.setStatus("current")
_SnStackingOperUnitStackPort1_Type = InterfaceIndexOrZero
_SnStackingOperUnitStackPort1_Object = MibTableColumn
snStackingOperUnitStackPort1 = _SnStackingOperUnitStackPort1_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2, 1, 7),
    _SnStackingOperUnitStackPort1_Type()
)
snStackingOperUnitStackPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackingOperUnitStackPort1.setStatus("current")


class _SnStackingOperUnitStackPort1State_Type(Integer32):
    """Custom type snStackingOperUnitStackPort1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("other", 1),
          ("up", 2))
    )


_SnStackingOperUnitStackPort1State_Type.__name__ = "Integer32"
_SnStackingOperUnitStackPort1State_Object = MibTableColumn
snStackingOperUnitStackPort1State = _SnStackingOperUnitStackPort1State_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2, 1, 8),
    _SnStackingOperUnitStackPort1State_Type()
)
snStackingOperUnitStackPort1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackingOperUnitStackPort1State.setStatus("current")
_SnStackingOperUnitStackPort2_Type = InterfaceIndexOrZero
_SnStackingOperUnitStackPort2_Object = MibTableColumn
snStackingOperUnitStackPort2 = _SnStackingOperUnitStackPort2_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2, 1, 9),
    _SnStackingOperUnitStackPort2_Type()
)
snStackingOperUnitStackPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackingOperUnitStackPort2.setStatus("current")


class _SnStackingOperUnitStackPort2State_Type(Integer32):
    """Custom type snStackingOperUnitStackPort2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("other", 1),
          ("up", 2))
    )


_SnStackingOperUnitStackPort2State_Type.__name__ = "Integer32"
_SnStackingOperUnitStackPort2State_Object = MibTableColumn
snStackingOperUnitStackPort2State = _SnStackingOperUnitStackPort2State_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2, 1, 10),
    _SnStackingOperUnitStackPort2State_Type()
)
snStackingOperUnitStackPort2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackingOperUnitStackPort2State.setStatus("current")
_SnStackingOperUnitNeighbor1_Type = Integer32
_SnStackingOperUnitNeighbor1_Object = MibTableColumn
snStackingOperUnitNeighbor1 = _SnStackingOperUnitNeighbor1_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2, 1, 11),
    _SnStackingOperUnitNeighbor1_Type()
)
snStackingOperUnitNeighbor1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackingOperUnitNeighbor1.setStatus("current")
_SnStackingOperUnitNeighbor2_Type = Integer32
_SnStackingOperUnitNeighbor2_Object = MibTableColumn
snStackingOperUnitNeighbor2 = _SnStackingOperUnitNeighbor2_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2, 1, 12),
    _SnStackingOperUnitNeighbor2_Type()
)
snStackingOperUnitNeighbor2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackingOperUnitNeighbor2.setStatus("current")


class _SnStackingOperUnitImgVer_Type(DisplayString):
    """Custom type snStackingOperUnitImgVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnStackingOperUnitImgVer_Type.__name__ = "DisplayString"
_SnStackingOperUnitImgVer_Object = MibTableColumn
snStackingOperUnitImgVer = _SnStackingOperUnitImgVer_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2, 1, 13),
    _SnStackingOperUnitImgVer_Type()
)
snStackingOperUnitImgVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackingOperUnitImgVer.setStatus("current")


class _SnStackingOperUnitBuildlVer_Type(DisplayString):
    """Custom type snStackingOperUnitBuildlVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnStackingOperUnitBuildlVer_Type.__name__ = "DisplayString"
_SnStackingOperUnitBuildlVer_Object = MibTableColumn
snStackingOperUnitBuildlVer = _SnStackingOperUnitBuildlVer_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 2, 1, 14),
    _SnStackingOperUnitBuildlVer_Type()
)
snStackingOperUnitBuildlVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackingOperUnitBuildlVer.setStatus("current")
_SnStackingConfigStackTrunkTable_Object = MibTable
snStackingConfigStackTrunkTable = _SnStackingConfigStackTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 3)
)
if mibBuilder.loadTexts:
    snStackingConfigStackTrunkTable.setStatus("current")
_SnStackingConfigStackTrunkEntry_Object = MibTableRow
snStackingConfigStackTrunkEntry = _SnStackingConfigStackTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 3, 1)
)
snStackingConfigStackTrunkEntry.setIndexNames(
    (0, "FOUNDRY-SN-STACKING-MIB", "snStackingConfigStackTrunkUnit"),
    (0, "FOUNDRY-SN-STACKING-MIB", "snStackingConfigStackTrunkPort1"),
    (0, "FOUNDRY-SN-STACKING-MIB", "snStackingConfigStackTrunkPort2"),
)
if mibBuilder.loadTexts:
    snStackingConfigStackTrunkEntry.setStatus("current")
_SnStackingConfigStackTrunkUnit_Type = Integer32
_SnStackingConfigStackTrunkUnit_Object = MibTableColumn
snStackingConfigStackTrunkUnit = _SnStackingConfigStackTrunkUnit_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 3, 1, 1),
    _SnStackingConfigStackTrunkUnit_Type()
)
snStackingConfigStackTrunkUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snStackingConfigStackTrunkUnit.setStatus("current")
_SnStackingConfigStackTrunkPort1_Type = InterfaceIndexOrZero
_SnStackingConfigStackTrunkPort1_Object = MibTableColumn
snStackingConfigStackTrunkPort1 = _SnStackingConfigStackTrunkPort1_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 3, 1, 2),
    _SnStackingConfigStackTrunkPort1_Type()
)
snStackingConfigStackTrunkPort1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snStackingConfigStackTrunkPort1.setStatus("current")
_SnStackingConfigStackTrunkPort2_Type = InterfaceIndexOrZero
_SnStackingConfigStackTrunkPort2_Object = MibTableColumn
snStackingConfigStackTrunkPort2 = _SnStackingConfigStackTrunkPort2_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 3, 1, 3),
    _SnStackingConfigStackTrunkPort2_Type()
)
snStackingConfigStackTrunkPort2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snStackingConfigStackTrunkPort2.setStatus("current")


class _SnStackingConfigStackTrunkRowStatus_Type(Integer32):
    """Custom type snStackingConfigStackTrunkRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("other", 1),
          ("valid", 2))
    )


_SnStackingConfigStackTrunkRowStatus_Type.__name__ = "Integer32"
_SnStackingConfigStackTrunkRowStatus_Object = MibTableColumn
snStackingConfigStackTrunkRowStatus = _SnStackingConfigStackTrunkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 3, 1, 4),
    _SnStackingConfigStackTrunkRowStatus_Type()
)
snStackingConfigStackTrunkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snStackingConfigStackTrunkRowStatus.setStatus("current")
_SnStackingConfigStackTrunkNumPort1_Type = Integer32
_SnStackingConfigStackTrunkNumPort1_Object = MibTableColumn
snStackingConfigStackTrunkNumPort1 = _SnStackingConfigStackTrunkNumPort1_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 3, 1, 5),
    _SnStackingConfigStackTrunkNumPort1_Type()
)
snStackingConfigStackTrunkNumPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackingConfigStackTrunkNumPort1.setStatus("current")
_SnStackingConfigStackTrunkNumPort2_Type = Integer32
_SnStackingConfigStackTrunkNumPort2_Object = MibTableColumn
snStackingConfigStackTrunkNumPort2 = _SnStackingConfigStackTrunkNumPort2_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 3, 1, 6),
    _SnStackingConfigStackTrunkNumPort2_Type()
)
snStackingConfigStackTrunkNumPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackingConfigStackTrunkNumPort2.setStatus("current")
_SnStackingConfigPeriPortTable_Object = MibTable
snStackingConfigPeriPortTable = _SnStackingConfigPeriPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 4)
)
if mibBuilder.loadTexts:
    snStackingConfigPeriPortTable.setStatus("current")
_SnStackingConfigPeriPortEntry_Object = MibTableRow
snStackingConfigPeriPortEntry = _SnStackingConfigPeriPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 4, 1)
)
snStackingConfigPeriPortEntry.setIndexNames(
    (0, "FOUNDRY-SN-STACKING-MIB", "snStackingConfigPeriPortUnit"),
    (0, "FOUNDRY-SN-STACKING-MIB", "snStackingConfigPeriPortPort"),
)
if mibBuilder.loadTexts:
    snStackingConfigPeriPortEntry.setStatus("current")
_SnStackingConfigPeriPortUnit_Type = Integer32
_SnStackingConfigPeriPortUnit_Object = MibTableColumn
snStackingConfigPeriPortUnit = _SnStackingConfigPeriPortUnit_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 4, 1, 1),
    _SnStackingConfigPeriPortUnit_Type()
)
snStackingConfigPeriPortUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snStackingConfigPeriPortUnit.setStatus("current")
_SnStackingConfigPeriPortPort_Type = InterfaceIndexOrZero
_SnStackingConfigPeriPortPort_Object = MibTableColumn
snStackingConfigPeriPortPort = _SnStackingConfigPeriPortPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 4, 1, 2),
    _SnStackingConfigPeriPortPort_Type()
)
snStackingConfigPeriPortPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snStackingConfigPeriPortPort.setStatus("current")


class _SnStackingConfigPeriPortRowStatus_Type(Integer32):
    """Custom type snStackingConfigPeriPortRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("other", 1),
          ("valid", 2))
    )


_SnStackingConfigPeriPortRowStatus_Type.__name__ = "Integer32"
_SnStackingConfigPeriPortRowStatus_Object = MibTableColumn
snStackingConfigPeriPortRowStatus = _SnStackingConfigPeriPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 4, 1, 3),
    _SnStackingConfigPeriPortRowStatus_Type()
)
snStackingConfigPeriPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snStackingConfigPeriPortRowStatus.setStatus("current")
_SnStackingConfigPeriTrunkTable_Object = MibTable
snStackingConfigPeriTrunkTable = _SnStackingConfigPeriTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 5)
)
if mibBuilder.loadTexts:
    snStackingConfigPeriTrunkTable.setStatus("current")
_SnStackingConfigPeriTrunkEntry_Object = MibTableRow
snStackingConfigPeriTrunkEntry = _SnStackingConfigPeriTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 5, 1)
)
snStackingConfigPeriTrunkEntry.setIndexNames(
    (0, "FOUNDRY-SN-STACKING-MIB", "snStackingConfigPeriTrunkUnit"),
    (0, "FOUNDRY-SN-STACKING-MIB", "snStackingConfigPeriTrunkPort1"),
    (0, "FOUNDRY-SN-STACKING-MIB", "snStackingConfigPeriTrunkPort2"),
)
if mibBuilder.loadTexts:
    snStackingConfigPeriTrunkEntry.setStatus("current")
_SnStackingConfigPeriTrunkUnit_Type = Integer32
_SnStackingConfigPeriTrunkUnit_Object = MibTableColumn
snStackingConfigPeriTrunkUnit = _SnStackingConfigPeriTrunkUnit_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 5, 1, 1),
    _SnStackingConfigPeriTrunkUnit_Type()
)
snStackingConfigPeriTrunkUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snStackingConfigPeriTrunkUnit.setStatus("current")
_SnStackingConfigPeriTrunkPort1_Type = InterfaceIndexOrZero
_SnStackingConfigPeriTrunkPort1_Object = MibTableColumn
snStackingConfigPeriTrunkPort1 = _SnStackingConfigPeriTrunkPort1_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 5, 1, 2),
    _SnStackingConfigPeriTrunkPort1_Type()
)
snStackingConfigPeriTrunkPort1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snStackingConfigPeriTrunkPort1.setStatus("current")
_SnStackingConfigPeriTrunkPort2_Type = InterfaceIndexOrZero
_SnStackingConfigPeriTrunkPort2_Object = MibTableColumn
snStackingConfigPeriTrunkPort2 = _SnStackingConfigPeriTrunkPort2_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 5, 1, 3),
    _SnStackingConfigPeriTrunkPort2_Type()
)
snStackingConfigPeriTrunkPort2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snStackingConfigPeriTrunkPort2.setStatus("current")


class _SnStackingConfigPeriTrunkRowStatus_Type(Integer32):
    """Custom type snStackingConfigPeriTrunkRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("other", 1),
          ("valid", 2))
    )


_SnStackingConfigPeriTrunkRowStatus_Type.__name__ = "Integer32"
_SnStackingConfigPeriTrunkRowStatus_Object = MibTableColumn
snStackingConfigPeriTrunkRowStatus = _SnStackingConfigPeriTrunkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 5, 1, 4),
    _SnStackingConfigPeriTrunkRowStatus_Type()
)
snStackingConfigPeriTrunkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snStackingConfigPeriTrunkRowStatus.setStatus("current")
_SnStackingNeighborPortTable_Object = MibTable
snStackingNeighborPortTable = _SnStackingNeighborPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 6)
)
if mibBuilder.loadTexts:
    snStackingNeighborPortTable.setStatus("current")
_SnStackingNeighborPortEntry_Object = MibTableRow
snStackingNeighborPortEntry = _SnStackingNeighborPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 6, 1)
)
snStackingNeighborPortEntry.setIndexNames(
    (0, "FOUNDRY-SN-STACKING-MIB", "snStackingNeighborPortUnit"),
    (0, "FOUNDRY-SN-STACKING-MIB", "snStackingNeighborPortStackPort"),
)
if mibBuilder.loadTexts:
    snStackingNeighborPortEntry.setStatus("current")
_SnStackingNeighborPortUnit_Type = Integer32
_SnStackingNeighborPortUnit_Object = MibTableColumn
snStackingNeighborPortUnit = _SnStackingNeighborPortUnit_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 6, 1, 1),
    _SnStackingNeighborPortUnit_Type()
)
snStackingNeighborPortUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snStackingNeighborPortUnit.setStatus("current")
_SnStackingNeighborPortStackPort_Type = InterfaceIndexOrZero
_SnStackingNeighborPortStackPort_Object = MibTableColumn
snStackingNeighborPortStackPort = _SnStackingNeighborPortStackPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 6, 1, 2),
    _SnStackingNeighborPortStackPort_Type()
)
snStackingNeighborPortStackPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snStackingNeighborPortStackPort.setStatus("current")
_SnStackingNeighborPortNeighborPort_Type = InterfaceIndexOrZero
_SnStackingNeighborPortNeighborPort_Object = MibTableColumn
snStackingNeighborPortNeighborPort = _SnStackingNeighborPortNeighborPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 31, 2, 6, 1, 3),
    _SnStackingNeighborPortNeighborPort_Type()
)
snStackingNeighborPortNeighborPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snStackingNeighborPortNeighborPort.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-SN-STACKING-MIB",
    **{"snStacking": snStacking,
       "snStackingGlobalObjects": snStackingGlobalObjects,
       "snStackingGlobalConfigState": snStackingGlobalConfigState,
       "snStackingGlobalMacAddress": snStackingGlobalMacAddress,
       "snStackingGlobalPersistentMacTimerState": snStackingGlobalPersistentMacTimerState,
       "snStackingGlobalPersistentMacTimer": snStackingGlobalPersistentMacTimer,
       "snStackingGlobalTopology": snStackingGlobalTopology,
       "snStackingGlobalMode": snStackingGlobalMode,
       "snStackingGlobalMixedMode": snStackingGlobalMixedMode,
       "snStackingTableObjects": snStackingTableObjects,
       "snStackingConfigUnitTable": snStackingConfigUnitTable,
       "snStackingConfigUnitEntry": snStackingConfigUnitEntry,
       "snStackingConfigUnitIndex": snStackingConfigUnitIndex,
       "snStackingConfigUnitPriority": snStackingConfigUnitPriority,
       "snStackingConfigUnitConfigStackPort": snStackingConfigUnitConfigStackPort,
       "snStackingConfigUnitRowStatus": snStackingConfigUnitRowStatus,
       "snStackingConfigUnitType": snStackingConfigUnitType,
       "snStackingConfigUnitState": snStackingConfigUnitState,
       "snStackingConfigUnitStackPort1": snStackingConfigUnitStackPort1,
       "snStackingConfigUnitStackPort2": snStackingConfigUnitStackPort2,
       "snStackingConfigUnitConnectPort1": snStackingConfigUnitConnectPort1,
       "snStackingConfigUnitConnectPort2": snStackingConfigUnitConnectPort2,
       "snStackingOperUnitTable": snStackingOperUnitTable,
       "snStackingOperUnitEntry": snStackingOperUnitEntry,
       "snStackingOperUnitIndex": snStackingOperUnitIndex,
       "snStackingOperUnitRole": snStackingOperUnitRole,
       "snStackingOperUnitMac": snStackingOperUnitMac,
       "snStackingOperUnitPriority": snStackingOperUnitPriority,
       "snStackingOperUnitState": snStackingOperUnitState,
       "snStackingOperUnitDescription": snStackingOperUnitDescription,
       "snStackingOperUnitStackPort1": snStackingOperUnitStackPort1,
       "snStackingOperUnitStackPort1State": snStackingOperUnitStackPort1State,
       "snStackingOperUnitStackPort2": snStackingOperUnitStackPort2,
       "snStackingOperUnitStackPort2State": snStackingOperUnitStackPort2State,
       "snStackingOperUnitNeighbor1": snStackingOperUnitNeighbor1,
       "snStackingOperUnitNeighbor2": snStackingOperUnitNeighbor2,
       "snStackingOperUnitImgVer": snStackingOperUnitImgVer,
       "snStackingOperUnitBuildlVer": snStackingOperUnitBuildlVer,
       "snStackingConfigStackTrunkTable": snStackingConfigStackTrunkTable,
       "snStackingConfigStackTrunkEntry": snStackingConfigStackTrunkEntry,
       "snStackingConfigStackTrunkUnit": snStackingConfigStackTrunkUnit,
       "snStackingConfigStackTrunkPort1": snStackingConfigStackTrunkPort1,
       "snStackingConfigStackTrunkPort2": snStackingConfigStackTrunkPort2,
       "snStackingConfigStackTrunkRowStatus": snStackingConfigStackTrunkRowStatus,
       "snStackingConfigStackTrunkNumPort1": snStackingConfigStackTrunkNumPort1,
       "snStackingConfigStackTrunkNumPort2": snStackingConfigStackTrunkNumPort2,
       "snStackingConfigPeriPortTable": snStackingConfigPeriPortTable,
       "snStackingConfigPeriPortEntry": snStackingConfigPeriPortEntry,
       "snStackingConfigPeriPortUnit": snStackingConfigPeriPortUnit,
       "snStackingConfigPeriPortPort": snStackingConfigPeriPortPort,
       "snStackingConfigPeriPortRowStatus": snStackingConfigPeriPortRowStatus,
       "snStackingConfigPeriTrunkTable": snStackingConfigPeriTrunkTable,
       "snStackingConfigPeriTrunkEntry": snStackingConfigPeriTrunkEntry,
       "snStackingConfigPeriTrunkUnit": snStackingConfigPeriTrunkUnit,
       "snStackingConfigPeriTrunkPort1": snStackingConfigPeriTrunkPort1,
       "snStackingConfigPeriTrunkPort2": snStackingConfigPeriTrunkPort2,
       "snStackingConfigPeriTrunkRowStatus": snStackingConfigPeriTrunkRowStatus,
       "snStackingNeighborPortTable": snStackingNeighborPortTable,
       "snStackingNeighborPortEntry": snStackingNeighborPortEntry,
       "snStackingNeighborPortUnit": snStackingNeighborPortUnit,
       "snStackingNeighborPortStackPort": snStackingNeighborPortStackPort,
       "snStackingNeighborPortNeighborPort": snStackingNeighborPortNeighborPort}
)
