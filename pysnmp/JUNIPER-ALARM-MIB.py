# SNMP MIB module (JUNIPER-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-ALARM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:46 2024
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

(jnxMibs,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

jnxAlarms = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxCraftAlarms_ObjectIdentity = ObjectIdentity
jnxCraftAlarms = _JnxCraftAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 4, 2)
)


class _JnxAlarmRelayMode_Type(Integer32):
    """Custom type jnxAlarmRelayMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cutOff", 3),
          ("other", 1),
          ("passOn", 2))
    )


_JnxAlarmRelayMode_Type.__name__ = "Integer32"
_JnxAlarmRelayMode_Object = MibScalar
jnxAlarmRelayMode = _JnxAlarmRelayMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 4, 2, 1),
    _JnxAlarmRelayMode_Type()
)
jnxAlarmRelayMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAlarmRelayMode.setStatus("current")
_JnxYellowAlarms_ObjectIdentity = ObjectIdentity
jnxYellowAlarms = _JnxYellowAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 4, 2, 2)
)


class _JnxYellowAlarmState_Type(Integer32):
    """Custom type jnxYellowAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3),
          ("other", 1))
    )


_JnxYellowAlarmState_Type.__name__ = "Integer32"
_JnxYellowAlarmState_Object = MibScalar
jnxYellowAlarmState = _JnxYellowAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 4, 2, 2, 1),
    _JnxYellowAlarmState_Type()
)
jnxYellowAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxYellowAlarmState.setStatus("current")
_JnxYellowAlarmCount_Type = Gauge32
_JnxYellowAlarmCount_Object = MibScalar
jnxYellowAlarmCount = _JnxYellowAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 4, 2, 2, 2),
    _JnxYellowAlarmCount_Type()
)
jnxYellowAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxYellowAlarmCount.setStatus("current")
_JnxYellowAlarmLastChange_Type = TimeStamp
_JnxYellowAlarmLastChange_Object = MibScalar
jnxYellowAlarmLastChange = _JnxYellowAlarmLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 4, 2, 2, 3),
    _JnxYellowAlarmLastChange_Type()
)
jnxYellowAlarmLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxYellowAlarmLastChange.setStatus("current")
_JnxRedAlarms_ObjectIdentity = ObjectIdentity
jnxRedAlarms = _JnxRedAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 4, 2, 3)
)


class _JnxRedAlarmState_Type(Integer32):
    """Custom type jnxRedAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3),
          ("other", 1))
    )


_JnxRedAlarmState_Type.__name__ = "Integer32"
_JnxRedAlarmState_Object = MibScalar
jnxRedAlarmState = _JnxRedAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 4, 2, 3, 1),
    _JnxRedAlarmState_Type()
)
jnxRedAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRedAlarmState.setStatus("current")
_JnxRedAlarmCount_Type = Gauge32
_JnxRedAlarmCount_Object = MibScalar
jnxRedAlarmCount = _JnxRedAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 4, 2, 3, 2),
    _JnxRedAlarmCount_Type()
)
jnxRedAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRedAlarmCount.setStatus("current")
_JnxRedAlarmLastChange_Type = TimeStamp
_JnxRedAlarmLastChange_Object = MibScalar
jnxRedAlarmLastChange = _JnxRedAlarmLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 4, 2, 3, 3),
    _JnxRedAlarmLastChange_Type()
)
jnxRedAlarmLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRedAlarmLastChange.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-ALARM-MIB",
    **{"jnxAlarms": jnxAlarms,
       "jnxCraftAlarms": jnxCraftAlarms,
       "jnxAlarmRelayMode": jnxAlarmRelayMode,
       "jnxYellowAlarms": jnxYellowAlarms,
       "jnxYellowAlarmState": jnxYellowAlarmState,
       "jnxYellowAlarmCount": jnxYellowAlarmCount,
       "jnxYellowAlarmLastChange": jnxYellowAlarmLastChange,
       "jnxRedAlarms": jnxRedAlarms,
       "jnxRedAlarmState": jnxRedAlarmState,
       "jnxRedAlarmCount": jnxRedAlarmCount,
       "jnxRedAlarmLastChange": jnxRedAlarmLastChange}
)
