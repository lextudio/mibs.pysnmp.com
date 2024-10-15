# SNMP MIB module (COLUBRIS-802DOT1X-ACCESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COLUBRIS-802DOT1X-ACCESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:10 2024
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

(colubrisMgmtV2,) = mibBuilder.importSymbols(
    "COLUBRIS-SMI",
    "colubrisMgmtV2")

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

colubris802Dot1xMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CoPaeMIBObjects_ObjectIdentity = ObjectIdentity
coPaeMIBObjects = _CoPaeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 8, 1)
)
_CoDot1xPaeSystem_ObjectIdentity = ObjectIdentity
coDot1xPaeSystem = _CoDot1xPaeSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 1)
)


class _CoDot1xPaeSystemModifyKey_Type(TruthValue):
    """Custom type coDot1xPaeSystemModifyKey based on TruthValue"""


_CoDot1xPaeSystemModifyKey_Object = MibScalar
coDot1xPaeSystemModifyKey = _CoDot1xPaeSystemModifyKey_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 1, 1),
    _CoDot1xPaeSystemModifyKey_Type()
)
coDot1xPaeSystemModifyKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot1xPaeSystemModifyKey.setStatus("current")


class _CoDot1xPaeSystemModifyKeyInterval_Type(Unsigned32):
    """Custom type coDot1xPaeSystemModifyKeyInterval based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 65535),
    )


_CoDot1xPaeSystemModifyKeyInterval_Type.__name__ = "Unsigned32"
_CoDot1xPaeSystemModifyKeyInterval_Object = MibScalar
coDot1xPaeSystemModifyKeyInterval = _CoDot1xPaeSystemModifyKeyInterval_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 1, 2),
    _CoDot1xPaeSystemModifyKeyInterval_Type()
)
coDot1xPaeSystemModifyKeyInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot1xPaeSystemModifyKeyInterval.setStatus("current")
if mibBuilder.loadTexts:
    coDot1xPaeSystemModifyKeyInterval.setUnits("seconds")
_CoDot1xPaeAuthenticator_ObjectIdentity = ObjectIdentity
coDot1xPaeAuthenticator = _CoDot1xPaeAuthenticator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 2)
)


class _CoDot1xAuthQuietPeriod_Type(Unsigned32):
    """Custom type coDot1xAuthQuietPeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CoDot1xAuthQuietPeriod_Type.__name__ = "Unsigned32"
_CoDot1xAuthQuietPeriod_Object = MibScalar
coDot1xAuthQuietPeriod = _CoDot1xAuthQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 2, 1),
    _CoDot1xAuthQuietPeriod_Type()
)
coDot1xAuthQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot1xAuthQuietPeriod.setStatus("current")
if mibBuilder.loadTexts:
    coDot1xAuthQuietPeriod.setUnits("seconds")


class _CoDot1xAuthTxPeriod_Type(Unsigned32):
    """Custom type coDot1xAuthTxPeriod based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CoDot1xAuthTxPeriod_Type.__name__ = "Unsigned32"
_CoDot1xAuthTxPeriod_Object = MibScalar
coDot1xAuthTxPeriod = _CoDot1xAuthTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 2, 2),
    _CoDot1xAuthTxPeriod_Type()
)
coDot1xAuthTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot1xAuthTxPeriod.setStatus("current")
if mibBuilder.loadTexts:
    coDot1xAuthTxPeriod.setUnits("seconds")


class _CoDot1xAuthSuppTimeout_Type(Unsigned32):
    """Custom type coDot1xAuthSuppTimeout based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CoDot1xAuthSuppTimeout_Type.__name__ = "Unsigned32"
_CoDot1xAuthSuppTimeout_Object = MibScalar
coDot1xAuthSuppTimeout = _CoDot1xAuthSuppTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 2, 3),
    _CoDot1xAuthSuppTimeout_Type()
)
coDot1xAuthSuppTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot1xAuthSuppTimeout.setStatus("current")
if mibBuilder.loadTexts:
    coDot1xAuthSuppTimeout.setUnits("seconds")


class _CoDot1xAuthServerTimeout_Type(Unsigned32):
    """Custom type coDot1xAuthServerTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CoDot1xAuthServerTimeout_Type.__name__ = "Unsigned32"
_CoDot1xAuthServerTimeout_Object = MibScalar
coDot1xAuthServerTimeout = _CoDot1xAuthServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 2, 4),
    _CoDot1xAuthServerTimeout_Type()
)
coDot1xAuthServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot1xAuthServerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    coDot1xAuthServerTimeout.setUnits("seconds")


class _CoDot1xAuthMaxReq_Type(Unsigned32):
    """Custom type coDot1xAuthMaxReq based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CoDot1xAuthMaxReq_Type.__name__ = "Unsigned32"
_CoDot1xAuthMaxReq_Object = MibScalar
coDot1xAuthMaxReq = _CoDot1xAuthMaxReq_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 2, 5),
    _CoDot1xAuthMaxReq_Type()
)
coDot1xAuthMaxReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot1xAuthMaxReq.setStatus("current")


class _CoDot1xAuthReAuthPeriod_Type(Unsigned32):
    """Custom type coDot1xAuthReAuthPeriod based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CoDot1xAuthReAuthPeriod_Type.__name__ = "Unsigned32"
_CoDot1xAuthReAuthPeriod_Object = MibScalar
coDot1xAuthReAuthPeriod = _CoDot1xAuthReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 2, 6),
    _CoDot1xAuthReAuthPeriod_Type()
)
coDot1xAuthReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot1xAuthReAuthPeriod.setStatus("current")
if mibBuilder.loadTexts:
    coDot1xAuthReAuthPeriod.setUnits("seconds")


class _CoDot1xAuthReAuthEnabled_Type(TruthValue):
    """Custom type coDot1xAuthReAuthEnabled based on TruthValue"""


_CoDot1xAuthReAuthEnabled_Object = MibScalar
coDot1xAuthReAuthEnabled = _CoDot1xAuthReAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 2, 7),
    _CoDot1xAuthReAuthEnabled_Type()
)
coDot1xAuthReAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot1xAuthReAuthEnabled.setStatus("current")


class _CoDot1xAuthKeyTxEnabled_Type(TruthValue):
    """Custom type coDot1xAuthKeyTxEnabled based on TruthValue"""


_CoDot1xAuthKeyTxEnabled_Object = MibScalar
coDot1xAuthKeyTxEnabled = _CoDot1xAuthKeyTxEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 2, 8),
    _CoDot1xAuthKeyTxEnabled_Type()
)
coDot1xAuthKeyTxEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot1xAuthKeyTxEnabled.setStatus("current")


class _CoDot1xAuthReAuthMax_Type(Unsigned32):
    """Custom type coDot1xAuthReAuthMax based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CoDot1xAuthReAuthMax_Type.__name__ = "Unsigned32"
_CoDot1xAuthReAuthMax_Object = MibScalar
coDot1xAuthReAuthMax = _CoDot1xAuthReAuthMax_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 8, 1, 2, 9),
    _CoDot1xAuthReAuthMax_Type()
)
coDot1xAuthReAuthMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot1xAuthReAuthMax.setStatus("current")
_CoDot1xPaeConformance_ObjectIdentity = ObjectIdentity
coDot1xPaeConformance = _CoDot1xPaeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 8, 2)
)
_CoDot1xPaeGroups_ObjectIdentity = ObjectIdentity
coDot1xPaeGroups = _CoDot1xPaeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 8, 2, 1)
)
_CoDot1xPaeCompliances_ObjectIdentity = ObjectIdentity
coDot1xPaeCompliances = _CoDot1xPaeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 8, 2, 2)
)

# Managed Objects groups

coDot1xPaeSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 8, 2, 1, 1)
)
coDot1xPaeSystemGroup.setObjects(
      *(("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xPaeSystemModifyKey"),
        ("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xPaeSystemModifyKeyInterval"))
)
if mibBuilder.loadTexts:
    coDot1xPaeSystemGroup.setStatus("current")

coDot1xPaeAuthenticatorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 8, 2, 1, 2)
)
coDot1xPaeAuthenticatorGroup.setObjects(
      *(("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xAuthQuietPeriod"),
        ("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xAuthTxPeriod"),
        ("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xAuthSuppTimeout"),
        ("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xAuthServerTimeout"),
        ("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xAuthMaxReq"),
        ("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xAuthReAuthPeriod"),
        ("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xAuthReAuthEnabled"),
        ("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xAuthKeyTxEnabled"),
        ("COLUBRIS-802DOT1X-ACCESS-MIB", "coDot1xAuthReAuthMax"))
)
if mibBuilder.loadTexts:
    coDot1xPaeAuthenticatorGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

coDot1xPaeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8744, 5, 8, 2, 2, 1)
)
if mibBuilder.loadTexts:
    coDot1xPaeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COLUBRIS-802DOT1X-ACCESS-MIB",
    **{"colubris802Dot1xMIB": colubris802Dot1xMIB,
       "coPaeMIBObjects": coPaeMIBObjects,
       "coDot1xPaeSystem": coDot1xPaeSystem,
       "coDot1xPaeSystemModifyKey": coDot1xPaeSystemModifyKey,
       "coDot1xPaeSystemModifyKeyInterval": coDot1xPaeSystemModifyKeyInterval,
       "coDot1xPaeAuthenticator": coDot1xPaeAuthenticator,
       "coDot1xAuthQuietPeriod": coDot1xAuthQuietPeriod,
       "coDot1xAuthTxPeriod": coDot1xAuthTxPeriod,
       "coDot1xAuthSuppTimeout": coDot1xAuthSuppTimeout,
       "coDot1xAuthServerTimeout": coDot1xAuthServerTimeout,
       "coDot1xAuthMaxReq": coDot1xAuthMaxReq,
       "coDot1xAuthReAuthPeriod": coDot1xAuthReAuthPeriod,
       "coDot1xAuthReAuthEnabled": coDot1xAuthReAuthEnabled,
       "coDot1xAuthKeyTxEnabled": coDot1xAuthKeyTxEnabled,
       "coDot1xAuthReAuthMax": coDot1xAuthReAuthMax,
       "coDot1xPaeConformance": coDot1xPaeConformance,
       "coDot1xPaeGroups": coDot1xPaeGroups,
       "coDot1xPaeSystemGroup": coDot1xPaeSystemGroup,
       "coDot1xPaeAuthenticatorGroup": coDot1xPaeAuthenticatorGroup,
       "coDot1xPaeCompliances": coDot1xPaeCompliances,
       "coDot1xPaeCompliance": coDot1xPaeCompliance}
)
