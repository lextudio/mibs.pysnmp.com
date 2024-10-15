# SNMP MIB module (SALIX-DS1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SALIX-DS1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:24 2024
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

(atmfM4TrapAlarmSeverity,) = mibBuilder.importSymbols(
    "ATM-FORUM-M4-MIB",
    "atmfM4TrapAlarmSeverity")

(dsx1ConfigEntry,) = mibBuilder.importSymbols(
    "DS1-MIB",
    "dsx1ConfigEntry")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(DateAndTime,) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "DateAndTime")

(salixGeneric,) = mibBuilder.importSymbols(
    "SALIX-MIB",
    "salixGeneric")

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

salixDsx1MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SalixDsx1MIBObjects_ObjectIdentity = ObjectIdentity
salixDsx1MIBObjects = _SalixDsx1MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 7, 1)
)
_SalixDsx1ConfigTable_Object = MibTable
salixDsx1ConfigTable = _SalixDsx1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    salixDsx1ConfigTable.setStatus("current")
_SalixDsx1ConfigEntry_Object = MibTableRow
salixDsx1ConfigEntry = _SalixDsx1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    salixDsx1ConfigEntry.setStatus("current")


class _SalixDsx1ContinuityTestType_Type(Integer32):
    """Custom type salixDsx1ContinuityTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopback", 1),
          ("transponder", 2))
    )


_SalixDsx1ContinuityTestType_Type.__name__ = "Integer32"
_SalixDsx1ContinuityTestType_Object = MibTableColumn
salixDsx1ContinuityTestType = _SalixDsx1ContinuityTestType_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 7, 1, 1, 1, 1),
    _SalixDsx1ContinuityTestType_Type()
)
salixDsx1ContinuityTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixDsx1ContinuityTestType.setStatus("current")


class _SalixDsx1DChannelPresent_Type(TruthValue):
    """Custom type salixDsx1DChannelPresent based on TruthValue"""


_SalixDsx1DChannelPresent_Object = MibTableColumn
salixDsx1DChannelPresent = _SalixDsx1DChannelPresent_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 7, 1, 1, 1, 2),
    _SalixDsx1DChannelPresent_Type()
)
salixDsx1DChannelPresent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixDsx1DChannelPresent.setStatus("current")


class _SalixDsx1AutoInitiateState_Type(TruthValue):
    """Custom type salixDsx1AutoInitiateState based on TruthValue"""


_SalixDsx1AutoInitiateState_Object = MibTableColumn
salixDsx1AutoInitiateState = _SalixDsx1AutoInitiateState_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 7, 1, 1, 1, 3),
    _SalixDsx1AutoInitiateState_Type()
)
salixDsx1AutoInitiateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixDsx1AutoInitiateState.setStatus("current")


class _SalixDsx1DChannelMode_Type(Integer32):
    """Custom type salixDsx1DChannelMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("networkMode", 2),
          ("userMode", 1))
    )


_SalixDsx1DChannelMode_Type.__name__ = "Integer32"
_SalixDsx1DChannelMode_Object = MibTableColumn
salixDsx1DChannelMode = _SalixDsx1DChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 7, 1, 1, 1, 4),
    _SalixDsx1DChannelMode_Type()
)
salixDsx1DChannelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixDsx1DChannelMode.setStatus("current")


class _SalixDsx1RobbedBitSignalling_Type(Integer32):
    """Custom type salixDsx1RobbedBitSignalling based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("offHook", 2),
          ("onHook", 1),
          ("ringing", 3))
    )


_SalixDsx1RobbedBitSignalling_Type.__name__ = "Integer32"
_SalixDsx1RobbedBitSignalling_Object = MibTableColumn
salixDsx1RobbedBitSignalling = _SalixDsx1RobbedBitSignalling_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 7, 1, 1, 1, 5),
    _SalixDsx1RobbedBitSignalling_Type()
)
salixDsx1RobbedBitSignalling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixDsx1RobbedBitSignalling.setStatus("current")


class _SalixDsx1TDMEchoCancellation_Type(Integer32):
    """Custom type salixDsx1TDMEchoCancellation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("echoCancel16ms", 1),
          ("echoCancel32ms", 2),
          ("echoCancel63ms", 3),
          ("none", 0))
    )


_SalixDsx1TDMEchoCancellation_Type.__name__ = "Integer32"
_SalixDsx1TDMEchoCancellation_Object = MibTableColumn
salixDsx1TDMEchoCancellation = _SalixDsx1TDMEchoCancellation_Object(
    (1, 3, 6, 1, 4, 1, 2158, 2, 7, 1, 1, 1, 7),
    _SalixDsx1TDMEchoCancellation_Type()
)
salixDsx1TDMEchoCancellation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salixDsx1TDMEchoCancellation.setStatus("current")
_SalixDsx1MIBTraps_ObjectIdentity = ObjectIdentity
salixDsx1MIBTraps = _SalixDsx1MIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 7, 2)
)
_SalixDsx1MIBTrapPrefix_ObjectIdentity = ObjectIdentity
salixDsx1MIBTrapPrefix = _SalixDsx1MIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 7, 2, 0)
)
_SalixDsx1MIBCompliance_ObjectIdentity = ObjectIdentity
salixDsx1MIBCompliance = _SalixDsx1MIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 7, 3)
)
_SalixDs1Groups_ObjectIdentity = ObjectIdentity
salixDs1Groups = _SalixDs1Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 7, 3, 1)
)
_SalixDs1Compliances_ObjectIdentity = ObjectIdentity
salixDs1Compliances = _SalixDs1Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2158, 2, 7, 3, 2)
)
dsx1ConfigEntry.registerAugmentions(
    ("SALIX-DS1-MIB",
     "salixDsx1ConfigEntry")
)
salixDsx1ConfigEntry.setIndexNames(*dsx1ConfigEntry.getIndexNames())

# Managed Objects groups

salixDs1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2158, 2, 7, 3, 1, 1)
)
salixDs1Group.setObjects(
    ("SALIX-DS1-MIB", "salixDsx1ContinuityTestType")
)
if mibBuilder.loadTexts:
    salixDs1Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

salixDs1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2158, 2, 7, 3, 2, 1)
)
if mibBuilder.loadTexts:
    salixDs1Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SALIX-DS1-MIB",
    **{"salixDsx1MIB": salixDsx1MIB,
       "salixDsx1MIBObjects": salixDsx1MIBObjects,
       "salixDsx1ConfigTable": salixDsx1ConfigTable,
       "salixDsx1ConfigEntry": salixDsx1ConfigEntry,
       "salixDsx1ContinuityTestType": salixDsx1ContinuityTestType,
       "salixDsx1DChannelPresent": salixDsx1DChannelPresent,
       "salixDsx1AutoInitiateState": salixDsx1AutoInitiateState,
       "salixDsx1DChannelMode": salixDsx1DChannelMode,
       "salixDsx1RobbedBitSignalling": salixDsx1RobbedBitSignalling,
       "salixDsx1TDMEchoCancellation": salixDsx1TDMEchoCancellation,
       "salixDsx1MIBTraps": salixDsx1MIBTraps,
       "salixDsx1MIBTrapPrefix": salixDsx1MIBTrapPrefix,
       "salixDsx1MIBCompliance": salixDsx1MIBCompliance,
       "salixDs1Groups": salixDs1Groups,
       "salixDs1Group": salixDs1Group,
       "salixDs1Compliances": salixDs1Compliances,
       "salixDs1Compliance": salixDs1Compliance}
)
