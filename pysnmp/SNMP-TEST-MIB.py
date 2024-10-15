# SNMP MIB module (SNMP-TEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SNMP-TEST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:04 2024
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

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(rlSnmpTestSimulatedVariables,) = mibBuilder.importSymbols(
    "RADLAN-rndApplications",
    "rlSnmpTestSimulatedVariables")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class KeyBits(Bits, TextualConvention):
    status = "current"


class FieldBits(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_RlSnmpTestMibVersion_Type = Integer32
_RlSnmpTestMibVersion_Object = MibScalar
rlSnmpTestMibVersion = _RlSnmpTestMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 1),
    _RlSnmpTestMibVersion_Type()
)
rlSnmpTestMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlSnmpTestMibVersion.setStatus("current")
_RlSetsTestTable_Object = MibTable
rlSetsTestTable = _RlSetsTestTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2)
)
if mibBuilder.loadTexts:
    rlSetsTestTable.setStatus("current")
_RlSetsTestEntry_Object = MibTableRow
rlSetsTestEntry = _RlSetsTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2, 1)
)
rlSetsTestEntry.setIndexNames(
    (0, "SNMP-TEST-MIB", "rlSetsEntryBitsKey"),
    (0, "SNMP-TEST-MIB", "rlSetsEntryPortListKey"),
)
if mibBuilder.loadTexts:
    rlSetsTestEntry.setStatus("current")


class _RlSetsEntryBitsKey_Type(KeyBits):
    """Custom type rlSetsEntryBitsKey based on KeyBits"""
    subtypeSpec = KeyBits.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fifthKey", 4),
          ("firstKey", 0),
          ("secondKey", 1),
          ("thirdKey", 2))
    )


_RlSetsEntryBitsKey_Type.__name__ = "KeyBits"
_RlSetsEntryBitsKey_Object = MibTableColumn
rlSetsEntryBitsKey = _RlSetsEntryBitsKey_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2, 1, 1),
    _RlSetsEntryBitsKey_Type()
)
rlSetsEntryBitsKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSetsEntryBitsKey.setStatus("current")
_RlSetsEntryPortListKey_Type = PortList
_RlSetsEntryPortListKey_Object = MibTableColumn
rlSetsEntryPortListKey = _RlSetsEntryPortListKey_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2, 1, 2),
    _RlSetsEntryPortListKey_Type()
)
rlSetsEntryPortListKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlSetsEntryPortListKey.setStatus("current")


class _RlSetsEntryBitsField_Type(FieldBits):
    """Custom type rlSetsEntryBitsField based on FieldBits"""
    subtypeSpec = FieldBits.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fifthField", 4),
          ("firstField", 0),
          ("secondField", 1),
          ("thirdField", 2))
    )


_RlSetsEntryBitsField_Type.__name__ = "FieldBits"
_RlSetsEntryBitsField_Object = MibTableColumn
rlSetsEntryBitsField = _RlSetsEntryBitsField_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2, 1, 3),
    _RlSetsEntryBitsField_Type()
)
rlSetsEntryBitsField.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlSetsEntryBitsField.setStatus("current")
_RlSetsEntryPortListField_Type = PortList
_RlSetsEntryPortListField_Object = MibTableColumn
rlSetsEntryPortListField = _RlSetsEntryPortListField_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2, 1, 4),
    _RlSetsEntryPortListField_Type()
)
rlSetsEntryPortListField.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlSetsEntryPortListField.setStatus("current")
_RlSetsEntryCounter64Field_Type = Counter64
_RlSetsEntryCounter64Field_Object = MibTableColumn
rlSetsEntryCounter64Field = _RlSetsEntryCounter64Field_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2, 1, 5),
    _RlSetsEntryCounter64Field_Type()
)
rlSetsEntryCounter64Field.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlSetsEntryCounter64Field.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMP-TEST-MIB",
    **{"KeyBits": KeyBits,
       "FieldBits": FieldBits,
       "rlSnmpTestMibVersion": rlSnmpTestMibVersion,
       "rlSetsTestTable": rlSetsTestTable,
       "rlSetsTestEntry": rlSetsTestEntry,
       "rlSetsEntryBitsKey": rlSetsEntryBitsKey,
       "rlSetsEntryPortListKey": rlSetsEntryPortListKey,
       "rlSetsEntryBitsField": rlSetsEntryBitsField,
       "rlSetsEntryPortListField": rlSetsEntryPortListField,
       "rlSetsEntryCounter64Field": rlSetsEntryCounter64Field}
)
