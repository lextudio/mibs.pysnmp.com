# SNMP MIB module (HPN-ICF-PPPOE-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-PPPOE-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:31 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfPPPoEServer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102)
)
hpnicfPPPoEServer.setRevisions(
        ("2009-05-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfPPPoEServerObject_ObjectIdentity = ObjectIdentity
hpnicfPPPoEServerObject = _HpnicfPPPoEServerObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102, 1)
)
_HpnicfPPPoEServerMaxSessions_Type = Integer32
_HpnicfPPPoEServerMaxSessions_Object = MibScalar
hpnicfPPPoEServerMaxSessions = _HpnicfPPPoEServerMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102, 1, 1),
    _HpnicfPPPoEServerMaxSessions_Type()
)
hpnicfPPPoEServerMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPPPoEServerMaxSessions.setStatus("current")
_HpnicfPPPoEServerCurrSessions_Type = Integer32
_HpnicfPPPoEServerCurrSessions_Object = MibScalar
hpnicfPPPoEServerCurrSessions = _HpnicfPPPoEServerCurrSessions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102, 1, 2),
    _HpnicfPPPoEServerCurrSessions_Type()
)
hpnicfPPPoEServerCurrSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPPPoEServerCurrSessions.setStatus("current")
_HpnicfPPPoEServerAuthRequests_Type = Counter32
_HpnicfPPPoEServerAuthRequests_Object = MibScalar
hpnicfPPPoEServerAuthRequests = _HpnicfPPPoEServerAuthRequests_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102, 1, 3),
    _HpnicfPPPoEServerAuthRequests_Type()
)
hpnicfPPPoEServerAuthRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPPPoEServerAuthRequests.setStatus("current")
_HpnicfPPPoEServerAuthSuccesses_Type = Counter32
_HpnicfPPPoEServerAuthSuccesses_Object = MibScalar
hpnicfPPPoEServerAuthSuccesses = _HpnicfPPPoEServerAuthSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102, 1, 4),
    _HpnicfPPPoEServerAuthSuccesses_Type()
)
hpnicfPPPoEServerAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPPPoEServerAuthSuccesses.setStatus("current")
_HpnicfPPPoEServerAuthFailures_Type = Counter32
_HpnicfPPPoEServerAuthFailures_Object = MibScalar
hpnicfPPPoEServerAuthFailures = _HpnicfPPPoEServerAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102, 1, 5),
    _HpnicfPPPoEServerAuthFailures_Type()
)
hpnicfPPPoEServerAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPPPoEServerAuthFailures.setStatus("current")


class _HpnicfPPPoESAbnormOffsThreshold_Type(Integer32):
    """Custom type hpnicfPPPoESAbnormOffsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfPPPoESAbnormOffsThreshold_Type.__name__ = "Integer32"
_HpnicfPPPoESAbnormOffsThreshold_Object = MibScalar
hpnicfPPPoESAbnormOffsThreshold = _HpnicfPPPoESAbnormOffsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102, 1, 6),
    _HpnicfPPPoESAbnormOffsThreshold_Type()
)
hpnicfPPPoESAbnormOffsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPPPoESAbnormOffsThreshold.setStatus("current")


class _HpnicfPPPoESAbnormOffPerThreshold_Type(Integer32):
    """Custom type hpnicfPPPoESAbnormOffPerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfPPPoESAbnormOffPerThreshold_Type.__name__ = "Integer32"
_HpnicfPPPoESAbnormOffPerThreshold_Object = MibScalar
hpnicfPPPoESAbnormOffPerThreshold = _HpnicfPPPoESAbnormOffPerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102, 1, 7),
    _HpnicfPPPoESAbnormOffPerThreshold_Type()
)
hpnicfPPPoESAbnormOffPerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPPPoESAbnormOffPerThreshold.setStatus("current")


class _HpnicfPPPoESNormOffPerThreshold_Type(Integer32):
    """Custom type hpnicfPPPoESNormOffPerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfPPPoESNormOffPerThreshold_Type.__name__ = "Integer32"
_HpnicfPPPoESNormOffPerThreshold_Object = MibScalar
hpnicfPPPoESNormOffPerThreshold = _HpnicfPPPoESNormOffPerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102, 1, 8),
    _HpnicfPPPoESNormOffPerThreshold_Type()
)
hpnicfPPPoESNormOffPerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPPPoESNormOffPerThreshold.setStatus("current")
_HpnicfPPPoEServerTraps_ObjectIdentity = ObjectIdentity
hpnicfPPPoEServerTraps = _HpnicfPPPoEServerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102, 2)
)
_HpnicfPPPoeServerTrapPrefix_ObjectIdentity = ObjectIdentity
hpnicfPPPoeServerTrapPrefix = _HpnicfPPPoeServerTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102, 2, 0)
)

# Managed Objects groups


# Notification objects

hpnicfPPPoESAbnormOffsAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102, 2, 0, 1)
)
if mibBuilder.loadTexts:
    hpnicfPPPoESAbnormOffsAlarm.setStatus(
        "current"
    )

hpnicfPPPoESAbnormOffPerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102, 2, 0, 2)
)
if mibBuilder.loadTexts:
    hpnicfPPPoESAbnormOffPerAlarm.setStatus(
        "current"
    )

hpnicfPPPoESNormOffPerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 102, 2, 0, 3)
)
if mibBuilder.loadTexts:
    hpnicfPPPoESNormOffPerAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-PPPOE-SERVER-MIB",
    **{"hpnicfPPPoEServer": hpnicfPPPoEServer,
       "hpnicfPPPoEServerObject": hpnicfPPPoEServerObject,
       "hpnicfPPPoEServerMaxSessions": hpnicfPPPoEServerMaxSessions,
       "hpnicfPPPoEServerCurrSessions": hpnicfPPPoEServerCurrSessions,
       "hpnicfPPPoEServerAuthRequests": hpnicfPPPoEServerAuthRequests,
       "hpnicfPPPoEServerAuthSuccesses": hpnicfPPPoEServerAuthSuccesses,
       "hpnicfPPPoEServerAuthFailures": hpnicfPPPoEServerAuthFailures,
       "hpnicfPPPoESAbnormOffsThreshold": hpnicfPPPoESAbnormOffsThreshold,
       "hpnicfPPPoESAbnormOffPerThreshold": hpnicfPPPoESAbnormOffPerThreshold,
       "hpnicfPPPoESNormOffPerThreshold": hpnicfPPPoESNormOffPerThreshold,
       "hpnicfPPPoEServerTraps": hpnicfPPPoEServerTraps,
       "hpnicfPPPoeServerTrapPrefix": hpnicfPPPoeServerTrapPrefix,
       "hpnicfPPPoESAbnormOffsAlarm": hpnicfPPPoESAbnormOffsAlarm,
       "hpnicfPPPoESAbnormOffPerAlarm": hpnicfPPPoESAbnormOffPerAlarm,
       "hpnicfPPPoESNormOffPerAlarm": hpnicfPPPoESNormOffPerAlarm}
)
