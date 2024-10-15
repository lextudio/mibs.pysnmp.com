# SNMP MIB module (H3C-PPPOE-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-PPPOE-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:11 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cPPPoEServer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 102)
)
h3cPPPoEServer.setRevisions(
        ("2009-05-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cPPPoEServerObject_ObjectIdentity = ObjectIdentity
h3cPPPoEServerObject = _H3cPPPoEServerObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 102, 1)
)
_H3cPPPoEServerMaxSessions_Type = Integer32
_H3cPPPoEServerMaxSessions_Object = MibScalar
h3cPPPoEServerMaxSessions = _H3cPPPoEServerMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 102, 1, 1),
    _H3cPPPoEServerMaxSessions_Type()
)
h3cPPPoEServerMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPPPoEServerMaxSessions.setStatus("current")
_H3cPPPoEServerCurrSessions_Type = Integer32
_H3cPPPoEServerCurrSessions_Object = MibScalar
h3cPPPoEServerCurrSessions = _H3cPPPoEServerCurrSessions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 102, 1, 2),
    _H3cPPPoEServerCurrSessions_Type()
)
h3cPPPoEServerCurrSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPPPoEServerCurrSessions.setStatus("current")
_H3cPPPoEServerAuthRequests_Type = Counter32
_H3cPPPoEServerAuthRequests_Object = MibScalar
h3cPPPoEServerAuthRequests = _H3cPPPoEServerAuthRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 102, 1, 3),
    _H3cPPPoEServerAuthRequests_Type()
)
h3cPPPoEServerAuthRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPPPoEServerAuthRequests.setStatus("current")
_H3cPPPoEServerAuthSuccesses_Type = Counter32
_H3cPPPoEServerAuthSuccesses_Object = MibScalar
h3cPPPoEServerAuthSuccesses = _H3cPPPoEServerAuthSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 102, 1, 4),
    _H3cPPPoEServerAuthSuccesses_Type()
)
h3cPPPoEServerAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPPPoEServerAuthSuccesses.setStatus("current")
_H3cPPPoEServerAuthFailures_Type = Counter32
_H3cPPPoEServerAuthFailures_Object = MibScalar
h3cPPPoEServerAuthFailures = _H3cPPPoEServerAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 102, 1, 5),
    _H3cPPPoEServerAuthFailures_Type()
)
h3cPPPoEServerAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPPPoEServerAuthFailures.setStatus("current")


class _H3cPPPoESAbnormOffsThreshold_Type(Integer32):
    """Custom type h3cPPPoESAbnormOffsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cPPPoESAbnormOffsThreshold_Type.__name__ = "Integer32"
_H3cPPPoESAbnormOffsThreshold_Object = MibScalar
h3cPPPoESAbnormOffsThreshold = _H3cPPPoESAbnormOffsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 102, 1, 6),
    _H3cPPPoESAbnormOffsThreshold_Type()
)
h3cPPPoESAbnormOffsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPPPoESAbnormOffsThreshold.setStatus("current")


class _H3cPPPoESAbnormOffPerThreshold_Type(Integer32):
    """Custom type h3cPPPoESAbnormOffPerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cPPPoESAbnormOffPerThreshold_Type.__name__ = "Integer32"
_H3cPPPoESAbnormOffPerThreshold_Object = MibScalar
h3cPPPoESAbnormOffPerThreshold = _H3cPPPoESAbnormOffPerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 102, 1, 7),
    _H3cPPPoESAbnormOffPerThreshold_Type()
)
h3cPPPoESAbnormOffPerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPPPoESAbnormOffPerThreshold.setStatus("current")


class _H3cPPPoESNormOffPerThreshold_Type(Integer32):
    """Custom type h3cPPPoESNormOffPerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cPPPoESNormOffPerThreshold_Type.__name__ = "Integer32"
_H3cPPPoESNormOffPerThreshold_Object = MibScalar
h3cPPPoESNormOffPerThreshold = _H3cPPPoESNormOffPerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 102, 1, 8),
    _H3cPPPoESNormOffPerThreshold_Type()
)
h3cPPPoESNormOffPerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPPPoESNormOffPerThreshold.setStatus("current")
_H3cPPPoEServerTraps_ObjectIdentity = ObjectIdentity
h3cPPPoEServerTraps = _H3cPPPoEServerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 102, 2)
)
_H3cPPPoeServerTrapPrefix_ObjectIdentity = ObjectIdentity
h3cPPPoeServerTrapPrefix = _H3cPPPoeServerTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 102, 2, 0)
)

# Managed Objects groups


# Notification objects

h3cPPPoESAbnormOffsAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 102, 2, 0, 1)
)
if mibBuilder.loadTexts:
    h3cPPPoESAbnormOffsAlarm.setStatus(
        "current"
    )

h3cPPPoESAbnormOffPerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 102, 2, 0, 2)
)
if mibBuilder.loadTexts:
    h3cPPPoESAbnormOffPerAlarm.setStatus(
        "current"
    )

h3cPPPoESNormOffPerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 102, 2, 0, 3)
)
if mibBuilder.loadTexts:
    h3cPPPoESNormOffPerAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-PPPOE-SERVER-MIB",
    **{"h3cPPPoEServer": h3cPPPoEServer,
       "h3cPPPoEServerObject": h3cPPPoEServerObject,
       "h3cPPPoEServerMaxSessions": h3cPPPoEServerMaxSessions,
       "h3cPPPoEServerCurrSessions": h3cPPPoEServerCurrSessions,
       "h3cPPPoEServerAuthRequests": h3cPPPoEServerAuthRequests,
       "h3cPPPoEServerAuthSuccesses": h3cPPPoEServerAuthSuccesses,
       "h3cPPPoEServerAuthFailures": h3cPPPoEServerAuthFailures,
       "h3cPPPoESAbnormOffsThreshold": h3cPPPoESAbnormOffsThreshold,
       "h3cPPPoESAbnormOffPerThreshold": h3cPPPoESAbnormOffPerThreshold,
       "h3cPPPoESNormOffPerThreshold": h3cPPPoESNormOffPerThreshold,
       "h3cPPPoEServerTraps": h3cPPPoEServerTraps,
       "h3cPPPoeServerTrapPrefix": h3cPPPoeServerTrapPrefix,
       "h3cPPPoESAbnormOffsAlarm": h3cPPPoESAbnormOffsAlarm,
       "h3cPPPoESAbnormOffPerAlarm": h3cPPPoESAbnormOffPerAlarm,
       "h3cPPPoESNormOffPerAlarm": h3cPPPoESNormOffPerAlarm}
)
