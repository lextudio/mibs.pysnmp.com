# SNMP MIB module (ALCATEL-IND1-DOT1Q-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-DOT1Q-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:53 2024
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

(softentIND1Dot1Q,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Dot1Q")

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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1Dot1QMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1)
)
alcatelIND1Dot1QMIB.setRevisions(
        ("2007-04-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1Dot1QMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1Dot1QMIBObjects = _AlcatelIND1Dot1QMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1Dot1QMIBObjects.setStatus("current")
_V8021Q_ObjectIdentity = ObjectIdentity
v8021Q = _V8021Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1)
)
_QPortVlanTable_Object = MibTable
qPortVlanTable = _QPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    qPortVlanTable.setStatus("current")
_QPortVlanEntry_Object = MibTableRow
qPortVlanEntry = _QPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 1, 1)
)
qPortVlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-DOT1Q-MIB", "qPortVlanSlot"),
    (0, "ALCATEL-IND1-DOT1Q-MIB", "qPortVlanPort"),
    (0, "ALCATEL-IND1-DOT1Q-MIB", "qPortVlanTagValue"),
)
if mibBuilder.loadTexts:
    qPortVlanEntry.setStatus("current")


class _QPortVlanSlot_Type(Integer32):
    """Custom type qPortVlanSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_QPortVlanSlot_Type.__name__ = "Integer32"
_QPortVlanSlot_Object = MibTableColumn
qPortVlanSlot = _QPortVlanSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 1, 1, 1),
    _QPortVlanSlot_Type()
)
qPortVlanSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPortVlanSlot.setStatus("current")


class _QPortVlanPort_Type(Integer32):
    """Custom type qPortVlanPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_QPortVlanPort_Type.__name__ = "Integer32"
_QPortVlanPort_Object = MibTableColumn
qPortVlanPort = _QPortVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 1, 1, 2),
    _QPortVlanPort_Type()
)
qPortVlanPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPortVlanPort.setStatus("current")


class _QPortVlanTagValue_Type(Integer32):
    """Custom type qPortVlanTagValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_QPortVlanTagValue_Type.__name__ = "Integer32"
_QPortVlanTagValue_Object = MibTableColumn
qPortVlanTagValue = _QPortVlanTagValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 1, 1, 3),
    _QPortVlanTagValue_Type()
)
qPortVlanTagValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPortVlanTagValue.setStatus("current")
_QPortVlanStatus_Type = RowStatus
_QPortVlanStatus_Object = MibTableColumn
qPortVlanStatus = _QPortVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 1, 1, 4),
    _QPortVlanStatus_Type()
)
qPortVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPortVlanStatus.setStatus("current")


class _QPortVlanDescription_Type(DisplayString):
    """Custom type qPortVlanDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_QPortVlanDescription_Type.__name__ = "DisplayString"
_QPortVlanDescription_Object = MibTableColumn
qPortVlanDescription = _QPortVlanDescription_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 1, 1, 5),
    _QPortVlanDescription_Type()
)
qPortVlanDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPortVlanDescription.setStatus("current")


class _QPortVlanForceTagInternal_Type(Integer32):
    """Custom type qPortVlanForceTagInternal based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 2),
          ("off", 0),
          ("on", 1))
    )


_QPortVlanForceTagInternal_Type.__name__ = "Integer32"
_QPortVlanForceTagInternal_Object = MibTableColumn
qPortVlanForceTagInternal = _QPortVlanForceTagInternal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 1, 1, 6),
    _QPortVlanForceTagInternal_Type()
)
qPortVlanForceTagInternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qPortVlanForceTagInternal.setStatus("current")
_QAggregateVlanTable_Object = MibTable
qAggregateVlanTable = _QAggregateVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    qAggregateVlanTable.setStatus("current")
_QAggregateVlanEntry_Object = MibTableRow
qAggregateVlanEntry = _QAggregateVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 2, 1)
)
qAggregateVlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-DOT1Q-MIB", "qAggregateVlanAggregateId"),
    (0, "ALCATEL-IND1-DOT1Q-MIB", "qAggregateVlanTagValue"),
)
if mibBuilder.loadTexts:
    qAggregateVlanEntry.setStatus("current")


class _QAggregateVlanAggregateId_Type(Integer32):
    """Custom type qAggregateVlanAggregateId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_QAggregateVlanAggregateId_Type.__name__ = "Integer32"
_QAggregateVlanAggregateId_Object = MibTableColumn
qAggregateVlanAggregateId = _QAggregateVlanAggregateId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 2, 1, 1),
    _QAggregateVlanAggregateId_Type()
)
qAggregateVlanAggregateId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qAggregateVlanAggregateId.setStatus("current")


class _QAggregateVlanTagValue_Type(Integer32):
    """Custom type qAggregateVlanTagValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_QAggregateVlanTagValue_Type.__name__ = "Integer32"
_QAggregateVlanTagValue_Object = MibTableColumn
qAggregateVlanTagValue = _QAggregateVlanTagValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 2, 1, 2),
    _QAggregateVlanTagValue_Type()
)
qAggregateVlanTagValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qAggregateVlanTagValue.setStatus("current")
_QAggregateVlanStatus_Type = RowStatus
_QAggregateVlanStatus_Object = MibTableColumn
qAggregateVlanStatus = _QAggregateVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 2, 1, 3),
    _QAggregateVlanStatus_Type()
)
qAggregateVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qAggregateVlanStatus.setStatus("current")


class _QAggregateVlanDescription_Type(DisplayString):
    """Custom type qAggregateVlanDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_QAggregateVlanDescription_Type.__name__ = "DisplayString"
_QAggregateVlanDescription_Object = MibTableColumn
qAggregateVlanDescription = _QAggregateVlanDescription_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 2, 1, 4),
    _QAggregateVlanDescription_Type()
)
qAggregateVlanDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qAggregateVlanDescription.setStatus("current")
_QAtmIfIndexVpiVciTable_Object = MibTable
qAtmIfIndexVpiVciTable = _QAtmIfIndexVpiVciTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    qAtmIfIndexVpiVciTable.setStatus("current")
_QAtmIfIndexVpiVciEntry_Object = MibTableRow
qAtmIfIndexVpiVciEntry = _QAtmIfIndexVpiVciEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 3, 1)
)
qAtmIfIndexVpiVciEntry.setIndexNames(
    (0, "ALCATEL-IND1-DOT1Q-MIB", "qAtmIfIndex"),
    (0, "ALCATEL-IND1-DOT1Q-MIB", "qAtmVpiValue"),
    (0, "ALCATEL-IND1-DOT1Q-MIB", "qAtmVciValue"),
    (0, "ALCATEL-IND1-DOT1Q-MIB", "qAtmIfIndexVpiVciVlanTagValue"),
)
if mibBuilder.loadTexts:
    qAtmIfIndexVpiVciEntry.setStatus("current")


class _QAtmIfIndex_Type(Integer32):
    """Custom type qAtmIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4259841, 2147483647),
    )


_QAtmIfIndex_Type.__name__ = "Integer32"
_QAtmIfIndex_Object = MibTableColumn
qAtmIfIndex = _QAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 3, 1, 1),
    _QAtmIfIndex_Type()
)
qAtmIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qAtmIfIndex.setStatus("current")


class _QAtmVpiValue_Type(Integer32):
    """Custom type qAtmVpiValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_QAtmVpiValue_Type.__name__ = "Integer32"
_QAtmVpiValue_Object = MibTableColumn
qAtmVpiValue = _QAtmVpiValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 3, 1, 2),
    _QAtmVpiValue_Type()
)
qAtmVpiValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qAtmVpiValue.setStatus("current")


class _QAtmVciValue_Type(Integer32):
    """Custom type qAtmVciValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QAtmVciValue_Type.__name__ = "Integer32"
_QAtmVciValue_Object = MibTableColumn
qAtmVciValue = _QAtmVciValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 3, 1, 3),
    _QAtmVciValue_Type()
)
qAtmVciValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qAtmVciValue.setStatus("current")


class _QAtmIfIndexVpiVciVlanTagValue_Type(Integer32):
    """Custom type qAtmIfIndexVpiVciVlanTagValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_QAtmIfIndexVpiVciVlanTagValue_Type.__name__ = "Integer32"
_QAtmIfIndexVpiVciVlanTagValue_Object = MibTableColumn
qAtmIfIndexVpiVciVlanTagValue = _QAtmIfIndexVpiVciVlanTagValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 3, 1, 4),
    _QAtmIfIndexVpiVciVlanTagValue_Type()
)
qAtmIfIndexVpiVciVlanTagValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qAtmIfIndexVpiVciVlanTagValue.setStatus("current")
_QAtmIfIndexVpiVciVlanAction_Type = RowStatus
_QAtmIfIndexVpiVciVlanAction_Object = MibTableColumn
qAtmIfIndexVpiVciVlanAction = _QAtmIfIndexVpiVciVlanAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 3, 1, 5),
    _QAtmIfIndexVpiVciVlanAction_Type()
)
qAtmIfIndexVpiVciVlanAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qAtmIfIndexVpiVciVlanAction.setStatus("current")


class _QAtmIfIndexVpiVciVlanDescription_Type(DisplayString):
    """Custom type qAtmIfIndexVpiVciVlanDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_QAtmIfIndexVpiVciVlanDescription_Type.__name__ = "DisplayString"
_QAtmIfIndexVpiVciVlanDescription_Object = MibTableColumn
qAtmIfIndexVpiVciVlanDescription = _QAtmIfIndexVpiVciVlanDescription_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 3, 1, 6),
    _QAtmIfIndexVpiVciVlanDescription_Type()
)
qAtmIfIndexVpiVciVlanDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qAtmIfIndexVpiVciVlanDescription.setStatus("current")


class _QAtmIfIndexVpiVciAcceptableFrameTypes_Type(Integer32):
    """Custom type qAtmIfIndexVpiVciAcceptableFrameTypes based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("admitAll", 1),
          ("admitOnlyVlanTagged", 2))
    )


_QAtmIfIndexVpiVciAcceptableFrameTypes_Type.__name__ = "Integer32"
_QAtmIfIndexVpiVciAcceptableFrameTypes_Object = MibTableColumn
qAtmIfIndexVpiVciAcceptableFrameTypes = _QAtmIfIndexVpiVciAcceptableFrameTypes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 3, 1, 7),
    _QAtmIfIndexVpiVciAcceptableFrameTypes_Type()
)
qAtmIfIndexVpiVciAcceptableFrameTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qAtmIfIndexVpiVciAcceptableFrameTypes.setStatus("current")


class _QAtmIfIndexVpiVciForceTagInternal_Type(Integer32):
    """Custom type qAtmIfIndexVpiVciForceTagInternal based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 2),
          ("off", 0),
          ("on", 1))
    )


_QAtmIfIndexVpiVciForceTagInternal_Type.__name__ = "Integer32"
_QAtmIfIndexVpiVciForceTagInternal_Object = MibTableColumn
qAtmIfIndexVpiVciForceTagInternal = _QAtmIfIndexVpiVciForceTagInternal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 1, 1, 3, 1, 8),
    _QAtmIfIndexVpiVciForceTagInternal_Type()
)
qAtmIfIndexVpiVciForceTagInternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qAtmIfIndexVpiVciForceTagInternal.setStatus("current")
_AlcatelIND1Dot1QMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1Dot1QMIBConformance = _AlcatelIND1Dot1QMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1Dot1QMIBConformance.setStatus("current")
_AlcatelIND1Dot1QMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1Dot1QMIBGroups = _AlcatelIND1Dot1QMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1Dot1QMIBGroups.setStatus("current")
_AlcatelIND1Dot1QMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1Dot1QMIBCompliances = _AlcatelIND1Dot1QMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1Dot1QMIBCompliances.setStatus("current")

# Managed Objects groups

dot1qPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 2, 1, 1)
)
dot1qPortGroup.setObjects(
      *(("ALCATEL-IND1-DOT1Q-MIB", "qPortVlanSlot"),
        ("ALCATEL-IND1-DOT1Q-MIB", "qPortVlanPort"),
        ("ALCATEL-IND1-DOT1Q-MIB", "qPortVlanTagValue"),
        ("ALCATEL-IND1-DOT1Q-MIB", "qPortVlanStatus"),
        ("ALCATEL-IND1-DOT1Q-MIB", "qPortVlanDescription"),
        ("ALCATEL-IND1-DOT1Q-MIB", "qPortVlanForceTagInternal"))
)
if mibBuilder.loadTexts:
    dot1qPortGroup.setStatus("current")

dot1qAggregateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 2, 1, 2)
)
dot1qAggregateGroup.setObjects(
      *(("ALCATEL-IND1-DOT1Q-MIB", "qAggregateVlanAggregateId"),
        ("ALCATEL-IND1-DOT1Q-MIB", "qAggregateVlanTagValue"),
        ("ALCATEL-IND1-DOT1Q-MIB", "qAggregateVlanStatus"),
        ("ALCATEL-IND1-DOT1Q-MIB", "qAggregateVlanDescription"))
)
if mibBuilder.loadTexts:
    dot1qAggregateGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1Dot1QMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 21, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1Dot1QMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-DOT1Q-MIB",
    **{"alcatelIND1Dot1QMIB": alcatelIND1Dot1QMIB,
       "alcatelIND1Dot1QMIBObjects": alcatelIND1Dot1QMIBObjects,
       "v8021Q": v8021Q,
       "qPortVlanTable": qPortVlanTable,
       "qPortVlanEntry": qPortVlanEntry,
       "qPortVlanSlot": qPortVlanSlot,
       "qPortVlanPort": qPortVlanPort,
       "qPortVlanTagValue": qPortVlanTagValue,
       "qPortVlanStatus": qPortVlanStatus,
       "qPortVlanDescription": qPortVlanDescription,
       "qPortVlanForceTagInternal": qPortVlanForceTagInternal,
       "qAggregateVlanTable": qAggregateVlanTable,
       "qAggregateVlanEntry": qAggregateVlanEntry,
       "qAggregateVlanAggregateId": qAggregateVlanAggregateId,
       "qAggregateVlanTagValue": qAggregateVlanTagValue,
       "qAggregateVlanStatus": qAggregateVlanStatus,
       "qAggregateVlanDescription": qAggregateVlanDescription,
       "qAtmIfIndexVpiVciTable": qAtmIfIndexVpiVciTable,
       "qAtmIfIndexVpiVciEntry": qAtmIfIndexVpiVciEntry,
       "qAtmIfIndex": qAtmIfIndex,
       "qAtmVpiValue": qAtmVpiValue,
       "qAtmVciValue": qAtmVciValue,
       "qAtmIfIndexVpiVciVlanTagValue": qAtmIfIndexVpiVciVlanTagValue,
       "qAtmIfIndexVpiVciVlanAction": qAtmIfIndexVpiVciVlanAction,
       "qAtmIfIndexVpiVciVlanDescription": qAtmIfIndexVpiVciVlanDescription,
       "qAtmIfIndexVpiVciAcceptableFrameTypes": qAtmIfIndexVpiVciAcceptableFrameTypes,
       "qAtmIfIndexVpiVciForceTagInternal": qAtmIfIndexVpiVciForceTagInternal,
       "alcatelIND1Dot1QMIBConformance": alcatelIND1Dot1QMIBConformance,
       "alcatelIND1Dot1QMIBGroups": alcatelIND1Dot1QMIBGroups,
       "dot1qPortGroup": dot1qPortGroup,
       "dot1qAggregateGroup": dot1qAggregateGroup,
       "alcatelIND1Dot1QMIBCompliances": alcatelIND1Dot1QMIBCompliances,
       "alcatelIND1Dot1QMIBCompliance": alcatelIND1Dot1QMIBCompliance}
)
