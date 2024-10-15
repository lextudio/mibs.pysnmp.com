# SNMP MIB module (DS0-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DS0-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:29 2024
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
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

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
 transmission) = mibBuilder.importSymbols(
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
    "transmission")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ds0 = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 81)
)
ds0.setRevisions(
        ("1998-05-24 20:10",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dsx0ConfigTable_Object = MibTable
dsx0ConfigTable = _Dsx0ConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 81, 1)
)
if mibBuilder.loadTexts:
    dsx0ConfigTable.setStatus("current")
_Dsx0ConfigEntry_Object = MibTableRow
dsx0ConfigEntry = _Dsx0ConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 81, 1, 1)
)
dsx0ConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dsx0ConfigEntry.setStatus("current")


class _Dsx0Ds0ChannelNumber_Type(Integer32):
    """Custom type dsx0Ds0ChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Dsx0Ds0ChannelNumber_Type.__name__ = "Integer32"
_Dsx0Ds0ChannelNumber_Object = MibTableColumn
dsx0Ds0ChannelNumber = _Dsx0Ds0ChannelNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 81, 1, 1, 1),
    _Dsx0Ds0ChannelNumber_Type()
)
dsx0Ds0ChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx0Ds0ChannelNumber.setStatus("current")
_Dsx0RobbedBitSignalling_Type = TruthValue
_Dsx0RobbedBitSignalling_Object = MibTableColumn
dsx0RobbedBitSignalling = _Dsx0RobbedBitSignalling_Object(
    (1, 3, 6, 1, 2, 1, 10, 81, 1, 1, 2),
    _Dsx0RobbedBitSignalling_Type()
)
dsx0RobbedBitSignalling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx0RobbedBitSignalling.setStatus("current")


class _Dsx0CircuitIdentifier_Type(DisplayString):
    """Custom type dsx0CircuitIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Dsx0CircuitIdentifier_Type.__name__ = "DisplayString"
_Dsx0CircuitIdentifier_Object = MibTableColumn
dsx0CircuitIdentifier = _Dsx0CircuitIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 10, 81, 1, 1, 3),
    _Dsx0CircuitIdentifier_Type()
)
dsx0CircuitIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx0CircuitIdentifier.setStatus("current")


class _Dsx0IdleCode_Type(Integer32):
    """Custom type dsx0IdleCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Dsx0IdleCode_Type.__name__ = "Integer32"
_Dsx0IdleCode_Object = MibTableColumn
dsx0IdleCode = _Dsx0IdleCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 81, 1, 1, 4),
    _Dsx0IdleCode_Type()
)
dsx0IdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx0IdleCode.setStatus("current")


class _Dsx0SeizedCode_Type(Integer32):
    """Custom type dsx0SeizedCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Dsx0SeizedCode_Type.__name__ = "Integer32"
_Dsx0SeizedCode_Object = MibTableColumn
dsx0SeizedCode = _Dsx0SeizedCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 81, 1, 1, 5),
    _Dsx0SeizedCode_Type()
)
dsx0SeizedCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx0SeizedCode.setStatus("current")


class _Dsx0ReceivedCode_Type(Integer32):
    """Custom type dsx0ReceivedCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Dsx0ReceivedCode_Type.__name__ = "Integer32"
_Dsx0ReceivedCode_Object = MibTableColumn
dsx0ReceivedCode = _Dsx0ReceivedCode_Object(
    (1, 3, 6, 1, 2, 1, 10, 81, 1, 1, 6),
    _Dsx0ReceivedCode_Type()
)
dsx0ReceivedCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx0ReceivedCode.setStatus("current")
_Dsx0TransmitCodesEnable_Type = TruthValue
_Dsx0TransmitCodesEnable_Object = MibTableColumn
dsx0TransmitCodesEnable = _Dsx0TransmitCodesEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 81, 1, 1, 7),
    _Dsx0TransmitCodesEnable_Type()
)
dsx0TransmitCodesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx0TransmitCodesEnable.setStatus("current")
_Dsx0Ds0BundleMappedIfIndex_Type = InterfaceIndexOrZero
_Dsx0Ds0BundleMappedIfIndex_Object = MibTableColumn
dsx0Ds0BundleMappedIfIndex = _Dsx0Ds0BundleMappedIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 81, 1, 1, 8),
    _Dsx0Ds0BundleMappedIfIndex_Type()
)
dsx0Ds0BundleMappedIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx0Ds0BundleMappedIfIndex.setStatus("current")
_Ds0Conformance_ObjectIdentity = ObjectIdentity
ds0Conformance = _Ds0Conformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 81, 2)
)
_Ds0Groups_ObjectIdentity = ObjectIdentity
ds0Groups = _Ds0Groups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 81, 2, 1)
)
_Ds0Compliances_ObjectIdentity = ObjectIdentity
ds0Compliances = _Ds0Compliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 81, 2, 2)
)
_Dsx0ChanMappingTable_Object = MibTable
dsx0ChanMappingTable = _Dsx0ChanMappingTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 81, 3)
)
if mibBuilder.loadTexts:
    dsx0ChanMappingTable.setStatus("current")
_Dsx0ChanMappingEntry_Object = MibTableRow
dsx0ChanMappingEntry = _Dsx0ChanMappingEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 81, 3, 1)
)
dsx0ChanMappingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DS0-MIB", "dsx0Ds0ChannelNumber"),
)
if mibBuilder.loadTexts:
    dsx0ChanMappingEntry.setStatus("current")
_Dsx0ChanMappedIfIndex_Type = InterfaceIndex
_Dsx0ChanMappedIfIndex_Object = MibTableColumn
dsx0ChanMappedIfIndex = _Dsx0ChanMappedIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 81, 3, 1, 1),
    _Dsx0ChanMappedIfIndex_Type()
)
dsx0ChanMappedIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx0ChanMappedIfIndex.setStatus("current")

# Managed Objects groups

ds0ConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 81, 2, 1, 1)
)
ds0ConfigGroup.setObjects(
      *(("DS0-MIB", "dsx0Ds0ChannelNumber"),
        ("DS0-MIB", "dsx0RobbedBitSignalling"),
        ("DS0-MIB", "dsx0CircuitIdentifier"),
        ("DS0-MIB", "dsx0IdleCode"),
        ("DS0-MIB", "dsx0SeizedCode"),
        ("DS0-MIB", "dsx0ReceivedCode"),
        ("DS0-MIB", "dsx0TransmitCodesEnable"),
        ("DS0-MIB", "dsx0Ds0BundleMappedIfIndex"),
        ("DS0-MIB", "dsx0ChanMappedIfIndex"))
)
if mibBuilder.loadTexts:
    ds0ConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ds0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 81, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ds0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DS0-MIB",
    **{"ds0": ds0,
       "dsx0ConfigTable": dsx0ConfigTable,
       "dsx0ConfigEntry": dsx0ConfigEntry,
       "dsx0Ds0ChannelNumber": dsx0Ds0ChannelNumber,
       "dsx0RobbedBitSignalling": dsx0RobbedBitSignalling,
       "dsx0CircuitIdentifier": dsx0CircuitIdentifier,
       "dsx0IdleCode": dsx0IdleCode,
       "dsx0SeizedCode": dsx0SeizedCode,
       "dsx0ReceivedCode": dsx0ReceivedCode,
       "dsx0TransmitCodesEnable": dsx0TransmitCodesEnable,
       "dsx0Ds0BundleMappedIfIndex": dsx0Ds0BundleMappedIfIndex,
       "ds0Conformance": ds0Conformance,
       "ds0Groups": ds0Groups,
       "ds0ConfigGroup": ds0ConfigGroup,
       "ds0Compliances": ds0Compliances,
       "ds0Compliance": ds0Compliance,
       "dsx0ChanMappingTable": dsx0ChanMappingTable,
       "dsx0ChanMappingEntry": dsx0ChanMappingEntry,
       "dsx0ChanMappedIfIndex": dsx0ChanMappedIfIndex}
)
