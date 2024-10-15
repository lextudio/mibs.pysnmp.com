# SNMP MIB module (HH3C-PPPOE-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-PPPOE-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:33 2024
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

hh3cPPPoEServer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 102)
)
hh3cPPPoEServer.setRevisions(
        ("2009-05-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cPPPoEServerObject_ObjectIdentity = ObjectIdentity
hh3cPPPoEServerObject = _Hh3cPPPoEServerObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 102, 1)
)
_Hh3cPPPoEServerMaxSessions_Type = Integer32
_Hh3cPPPoEServerMaxSessions_Object = MibScalar
hh3cPPPoEServerMaxSessions = _Hh3cPPPoEServerMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 102, 1, 1),
    _Hh3cPPPoEServerMaxSessions_Type()
)
hh3cPPPoEServerMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPPPoEServerMaxSessions.setStatus("current")
_Hh3cPPPoEServerCurrSessions_Type = Integer32
_Hh3cPPPoEServerCurrSessions_Object = MibScalar
hh3cPPPoEServerCurrSessions = _Hh3cPPPoEServerCurrSessions_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 102, 1, 2),
    _Hh3cPPPoEServerCurrSessions_Type()
)
hh3cPPPoEServerCurrSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPPPoEServerCurrSessions.setStatus("current")
_Hh3cPPPoEServerAuthRequests_Type = Counter32
_Hh3cPPPoEServerAuthRequests_Object = MibScalar
hh3cPPPoEServerAuthRequests = _Hh3cPPPoEServerAuthRequests_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 102, 1, 3),
    _Hh3cPPPoEServerAuthRequests_Type()
)
hh3cPPPoEServerAuthRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPPPoEServerAuthRequests.setStatus("current")
_Hh3cPPPoEServerAuthSuccesses_Type = Counter32
_Hh3cPPPoEServerAuthSuccesses_Object = MibScalar
hh3cPPPoEServerAuthSuccesses = _Hh3cPPPoEServerAuthSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 102, 1, 4),
    _Hh3cPPPoEServerAuthSuccesses_Type()
)
hh3cPPPoEServerAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPPPoEServerAuthSuccesses.setStatus("current")
_Hh3cPPPoEServerAuthFailures_Type = Counter32
_Hh3cPPPoEServerAuthFailures_Object = MibScalar
hh3cPPPoEServerAuthFailures = _Hh3cPPPoEServerAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 102, 1, 5),
    _Hh3cPPPoEServerAuthFailures_Type()
)
hh3cPPPoEServerAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPPPoEServerAuthFailures.setStatus("current")


class _Hh3cPPPoESAbnormOffsThreshold_Type(Integer32):
    """Custom type hh3cPPPoESAbnormOffsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cPPPoESAbnormOffsThreshold_Type.__name__ = "Integer32"
_Hh3cPPPoESAbnormOffsThreshold_Object = MibScalar
hh3cPPPoESAbnormOffsThreshold = _Hh3cPPPoESAbnormOffsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 102, 1, 6),
    _Hh3cPPPoESAbnormOffsThreshold_Type()
)
hh3cPPPoESAbnormOffsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPPPoESAbnormOffsThreshold.setStatus("current")


class _Hh3cPPPoESAbnormOffPerThreshold_Type(Integer32):
    """Custom type hh3cPPPoESAbnormOffPerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cPPPoESAbnormOffPerThreshold_Type.__name__ = "Integer32"
_Hh3cPPPoESAbnormOffPerThreshold_Object = MibScalar
hh3cPPPoESAbnormOffPerThreshold = _Hh3cPPPoESAbnormOffPerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 102, 1, 7),
    _Hh3cPPPoESAbnormOffPerThreshold_Type()
)
hh3cPPPoESAbnormOffPerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPPPoESAbnormOffPerThreshold.setStatus("current")


class _Hh3cPPPoESNormOffPerThreshold_Type(Integer32):
    """Custom type hh3cPPPoESNormOffPerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cPPPoESNormOffPerThreshold_Type.__name__ = "Integer32"
_Hh3cPPPoESNormOffPerThreshold_Object = MibScalar
hh3cPPPoESNormOffPerThreshold = _Hh3cPPPoESNormOffPerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 102, 1, 8),
    _Hh3cPPPoESNormOffPerThreshold_Type()
)
hh3cPPPoESNormOffPerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPPPoESNormOffPerThreshold.setStatus("current")
_Hh3cPPPoEServerTraps_ObjectIdentity = ObjectIdentity
hh3cPPPoEServerTraps = _Hh3cPPPoEServerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 102, 2)
)
_Hh3cPPPoeServerTrapPrefix_ObjectIdentity = ObjectIdentity
hh3cPPPoeServerTrapPrefix = _Hh3cPPPoeServerTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 102, 2, 0)
)

# Managed Objects groups


# Notification objects

hh3cPPPoESAbnormOffsAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 102, 2, 0, 1)
)
if mibBuilder.loadTexts:
    hh3cPPPoESAbnormOffsAlarm.setStatus(
        "current"
    )

hh3cPPPoESAbnormOffPerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 102, 2, 0, 2)
)
if mibBuilder.loadTexts:
    hh3cPPPoESAbnormOffPerAlarm.setStatus(
        "current"
    )

hh3cPPPoESNormOffPerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 102, 2, 0, 3)
)
if mibBuilder.loadTexts:
    hh3cPPPoESNormOffPerAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-PPPOE-SERVER-MIB",
    **{"hh3cPPPoEServer": hh3cPPPoEServer,
       "hh3cPPPoEServerObject": hh3cPPPoEServerObject,
       "hh3cPPPoEServerMaxSessions": hh3cPPPoEServerMaxSessions,
       "hh3cPPPoEServerCurrSessions": hh3cPPPoEServerCurrSessions,
       "hh3cPPPoEServerAuthRequests": hh3cPPPoEServerAuthRequests,
       "hh3cPPPoEServerAuthSuccesses": hh3cPPPoEServerAuthSuccesses,
       "hh3cPPPoEServerAuthFailures": hh3cPPPoEServerAuthFailures,
       "hh3cPPPoESAbnormOffsThreshold": hh3cPPPoESAbnormOffsThreshold,
       "hh3cPPPoESAbnormOffPerThreshold": hh3cPPPoESAbnormOffPerThreshold,
       "hh3cPPPoESNormOffPerThreshold": hh3cPPPoESNormOffPerThreshold,
       "hh3cPPPoEServerTraps": hh3cPPPoEServerTraps,
       "hh3cPPPoeServerTrapPrefix": hh3cPPPoeServerTrapPrefix,
       "hh3cPPPoESAbnormOffsAlarm": hh3cPPPoESAbnormOffsAlarm,
       "hh3cPPPoESAbnormOffPerAlarm": hh3cPPPoESAbnormOffPerAlarm,
       "hh3cPPPoESNormOffPerAlarm": hh3cPPPoESNormOffPerAlarm}
)
