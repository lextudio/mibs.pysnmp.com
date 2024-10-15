# SNMP MIB module (ONEACCESS-SSH-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ONEACCESS-SSH-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:04 2024
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

(oacExpIMIpAcl,
 oacExpIMManagement,
 oacMIBModules) = mibBuilder.importSymbols(
    "ONEACCESS-GLOBAL-REG",
    "oacExpIMIpAcl",
    "oacExpIMManagement",
    "oacMIBModules")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

oacSshConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 100, 2004)
)
oacSshConfigMIB.setRevisions(
        ("2011-07-26 00:00",
         "2011-06-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OacSshConfig_ObjectIdentity = ObjectIdentity
oacSshConfig = _OacSshConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 22)
)
_OacSshConfigObjects_ObjectIdentity = ObjectIdentity
oacSshConfigObjects = _OacSshConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 22, 1)
)


class _OacSshDsaKey_Type(Integer32):
    """Custom type oacSshDsaKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              256,
              512,
              1024,
              2048)
        )
    )
    namedValues = NamedValues(
        *(("keysize-0bits", 0),
          ("keysize-1024bits", 1024),
          ("keysize-2048bits", 2048),
          ("keysize-256bits", 256),
          ("keysize-512bits", 512))
    )


_OacSshDsaKey_Type.__name__ = "Integer32"
_OacSshDsaKey_Object = MibScalar
oacSshDsaKey = _OacSshDsaKey_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 22, 1, 1),
    _OacSshDsaKey_Type()
)
oacSshDsaKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacSshDsaKey.setStatus("current")


class _OacSshEnabled_Type(TruthValue):
    """Custom type oacSshEnabled based on TruthValue"""


_OacSshEnabled_Object = MibScalar
oacSshEnabled = _OacSshEnabled_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 22, 1, 2),
    _OacSshEnabled_Type()
)
oacSshEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacSshEnabled.setStatus("current")


class _OacSshIdleTimeout_Type(Unsigned32):
    """Custom type oacSshIdleTimeout based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 4294967295),
    )


_OacSshIdleTimeout_Type.__name__ = "Unsigned32"
_OacSshIdleTimeout_Object = MibScalar
oacSshIdleTimeout = _OacSshIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 22, 1, 3),
    _OacSshIdleTimeout_Type()
)
oacSshIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacSshIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    oacSshIdleTimeout.setUnits("seconds")


class _OacSshAuthTimeout_Type(Integer32):
    """Custom type oacSshAuthTimeout based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 120),
    )


_OacSshAuthTimeout_Type.__name__ = "Integer32"
_OacSshAuthTimeout_Object = MibScalar
oacSshAuthTimeout = _OacSshAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 22, 1, 4),
    _OacSshAuthTimeout_Type()
)
oacSshAuthTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacSshAuthTimeout.setStatus("current")
if mibBuilder.loadTexts:
    oacSshAuthTimeout.setUnits("seconds")


class _OacSshAuthRetries_Type(Integer32):
    """Custom type oacSshAuthRetries based on Integer32"""
    defaultValue = 3


_OacSshAuthRetries_Object = MibScalar
oacSshAuthRetries = _OacSshAuthRetries_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 22, 1, 5),
    _OacSshAuthRetries_Type()
)
oacSshAuthRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacSshAuthRetries.setStatus("current")


class _OacSshBindInterface_Type(OctetString):
    """Custom type oacSshBindInterface based on OctetString"""
    defaultValue = OctetString("any")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_OacSshBindInterface_Type.__name__ = "OctetString"
_OacSshBindInterface_Object = MibScalar
oacSshBindInterface = _OacSshBindInterface_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 22, 1, 6),
    _OacSshBindInterface_Type()
)
oacSshBindInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacSshBindInterface.setStatus("current")


class _OacSshBindAcl_Type(OctetString):
    """Custom type oacSshBindAcl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OacSshBindAcl_Type.__name__ = "OctetString"
_OacSshBindAcl_Object = MibScalar
oacSshBindAcl = _OacSshBindAcl_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 22, 1, 7),
    _OacSshBindAcl_Type()
)
oacSshBindAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacSshBindAcl.setStatus("current")


class _OacSshMaxSessions_Type(Integer32):
    """Custom type oacSshMaxSessions based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_OacSshMaxSessions_Type.__name__ = "Integer32"
_OacSshMaxSessions_Object = MibScalar
oacSshMaxSessions = _OacSshMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 22, 1, 8),
    _OacSshMaxSessions_Type()
)
oacSshMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacSshMaxSessions.setStatus("current")


class _OacSshMaxSessionChannels_Type(Integer32):
    """Custom type oacSshMaxSessionChannels based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_OacSshMaxSessionChannels_Type.__name__ = "Integer32"
_OacSshMaxSessionChannels_Object = MibScalar
oacSshMaxSessionChannels = _OacSshMaxSessionChannels_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 22, 1, 9),
    _OacSshMaxSessionChannels_Type()
)
oacSshMaxSessionChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacSshMaxSessionChannels.setStatus("current")
_OacSshConfigConformance_ObjectIdentity = ObjectIdentity
oacSshConfigConformance = _OacSshConfigConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 22, 2)
)
_OacSshConfigGroups_ObjectIdentity = ObjectIdentity
oacSshConfigGroups = _OacSshConfigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 22, 2, 1)
)
_OacSshCompls_ObjectIdentity = ObjectIdentity
oacSshCompls = _OacSshCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 22, 2, 2)
)

# Managed Objects groups

oacSshConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 22, 2, 1, 1)
)
oacSshConfigGroup.setObjects(
    ("ONEACCESS-SSH-CONFIG-MIB", "oacSshEnabled")
)
if mibBuilder.loadTexts:
    oacSshConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONEACCESS-SSH-CONFIG-MIB",
    **{"oacSshConfigMIB": oacSshConfigMIB,
       "oacSshConfig": oacSshConfig,
       "oacSshConfigObjects": oacSshConfigObjects,
       "oacSshDsaKey": oacSshDsaKey,
       "oacSshEnabled": oacSshEnabled,
       "oacSshIdleTimeout": oacSshIdleTimeout,
       "oacSshAuthTimeout": oacSshAuthTimeout,
       "oacSshAuthRetries": oacSshAuthRetries,
       "oacSshBindInterface": oacSshBindInterface,
       "oacSshBindAcl": oacSshBindAcl,
       "oacSshMaxSessions": oacSshMaxSessions,
       "oacSshMaxSessionChannels": oacSshMaxSessionChannels,
       "oacSshConfigConformance": oacSshConfigConformance,
       "oacSshConfigGroups": oacSshConfigGroups,
       "oacSshConfigGroup": oacSshConfigGroup,
       "oacSshCompls": oacSshCompls}
)
