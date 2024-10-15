# SNMP MIB module (ENTERASYS-ENCR-8021X-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-ENCR-8021X-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:48 2024
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

(etsysDot1xAuthStationAddress,) = mibBuilder.importSymbols(
    "ENTERASYS-8021X-EXTENSIONS-MIB",
    "etsysDot1xAuthStationAddress")

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(dot1xPaePortNumber,) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "dot1xPaePortNumber")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

etsysEncr8021xConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 19)
)
etsysEncr8021xConfigMIB.setRevisions(
        ("2002-03-14 20:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysEncrDot1xConfigObjects_ObjectIdentity = ObjectIdentity
etsysEncrDot1xConfigObjects = _EtsysEncrDot1xConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 19, 1)
)
_EtsysEncrDot1xAuthConfigBranch_ObjectIdentity = ObjectIdentity
etsysEncrDot1xAuthConfigBranch = _EtsysEncrDot1xAuthConfigBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 19, 1, 1)
)
_EtsysEncrDot1xAuthPortConfigTable_Object = MibTable
etsysEncrDot1xAuthPortConfigTable = _EtsysEncrDot1xAuthPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 19, 1, 1, 1)
)
if mibBuilder.loadTexts:
    etsysEncrDot1xAuthPortConfigTable.setStatus("current")
_EtsysEncrDot1xAuthPortConfigEntry_Object = MibTableRow
etsysEncrDot1xAuthPortConfigEntry = _EtsysEncrDot1xAuthPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 19, 1, 1, 1, 1)
)
etsysEncrDot1xAuthPortConfigEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    etsysEncrDot1xAuthPortConfigEntry.setStatus("current")


class _EtsysEncrDot1xAuthAdminControlledDirections_Type(OctetString):
    """Custom type etsysEncrDot1xAuthAdminControlledDirections based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EtsysEncrDot1xAuthAdminControlledDirections_Type.__name__ = "OctetString"
_EtsysEncrDot1xAuthAdminControlledDirections_Object = MibTableColumn
etsysEncrDot1xAuthAdminControlledDirections = _EtsysEncrDot1xAuthAdminControlledDirections_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 19, 1, 1, 1, 1, 1),
    _EtsysEncrDot1xAuthAdminControlledDirections_Type()
)
etsysEncrDot1xAuthAdminControlledDirections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysEncrDot1xAuthAdminControlledDirections.setStatus("current")


class _EtsysEncrDot1xAuthControlledPortControl_Type(OctetString):
    """Custom type etsysEncrDot1xAuthControlledPortControl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EtsysEncrDot1xAuthControlledPortControl_Type.__name__ = "OctetString"
_EtsysEncrDot1xAuthControlledPortControl_Object = MibTableColumn
etsysEncrDot1xAuthControlledPortControl = _EtsysEncrDot1xAuthControlledPortControl_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 19, 1, 1, 1, 1, 2),
    _EtsysEncrDot1xAuthControlledPortControl_Type()
)
etsysEncrDot1xAuthControlledPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysEncrDot1xAuthControlledPortControl.setStatus("current")


class _EtsysEncrDot1xAuthQuietPeriod_Type(OctetString):
    """Custom type etsysEncrDot1xAuthQuietPeriod based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EtsysEncrDot1xAuthQuietPeriod_Type.__name__ = "OctetString"
_EtsysEncrDot1xAuthQuietPeriod_Object = MibTableColumn
etsysEncrDot1xAuthQuietPeriod = _EtsysEncrDot1xAuthQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 19, 1, 1, 1, 1, 3),
    _EtsysEncrDot1xAuthQuietPeriod_Type()
)
etsysEncrDot1xAuthQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysEncrDot1xAuthQuietPeriod.setStatus("current")


class _EtsysEncrDot1xAuthTxPeriod_Type(OctetString):
    """Custom type etsysEncrDot1xAuthTxPeriod based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EtsysEncrDot1xAuthTxPeriod_Type.__name__ = "OctetString"
_EtsysEncrDot1xAuthTxPeriod_Object = MibTableColumn
etsysEncrDot1xAuthTxPeriod = _EtsysEncrDot1xAuthTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 19, 1, 1, 1, 1, 4),
    _EtsysEncrDot1xAuthTxPeriod_Type()
)
etsysEncrDot1xAuthTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysEncrDot1xAuthTxPeriod.setStatus("current")


class _EtsysEncrDot1xAuthSuppTimeout_Type(OctetString):
    """Custom type etsysEncrDot1xAuthSuppTimeout based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EtsysEncrDot1xAuthSuppTimeout_Type.__name__ = "OctetString"
_EtsysEncrDot1xAuthSuppTimeout_Object = MibTableColumn
etsysEncrDot1xAuthSuppTimeout = _EtsysEncrDot1xAuthSuppTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 19, 1, 1, 1, 1, 5),
    _EtsysEncrDot1xAuthSuppTimeout_Type()
)
etsysEncrDot1xAuthSuppTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysEncrDot1xAuthSuppTimeout.setStatus("current")


class _EtsysEncrDot1xAuthServerTimeout_Type(OctetString):
    """Custom type etsysEncrDot1xAuthServerTimeout based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EtsysEncrDot1xAuthServerTimeout_Type.__name__ = "OctetString"
_EtsysEncrDot1xAuthServerTimeout_Object = MibTableColumn
etsysEncrDot1xAuthServerTimeout = _EtsysEncrDot1xAuthServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 19, 1, 1, 1, 1, 6),
    _EtsysEncrDot1xAuthServerTimeout_Type()
)
etsysEncrDot1xAuthServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysEncrDot1xAuthServerTimeout.setStatus("current")


class _EtsysEncrDot1xAuthMaxReq_Type(OctetString):
    """Custom type etsysEncrDot1xAuthMaxReq based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EtsysEncrDot1xAuthMaxReq_Type.__name__ = "OctetString"
_EtsysEncrDot1xAuthMaxReq_Object = MibTableColumn
etsysEncrDot1xAuthMaxReq = _EtsysEncrDot1xAuthMaxReq_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 19, 1, 1, 1, 1, 7),
    _EtsysEncrDot1xAuthMaxReq_Type()
)
etsysEncrDot1xAuthMaxReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysEncrDot1xAuthMaxReq.setStatus("current")


class _EtsysEncrDot1xAuthReAuthPeriod_Type(OctetString):
    """Custom type etsysEncrDot1xAuthReAuthPeriod based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EtsysEncrDot1xAuthReAuthPeriod_Type.__name__ = "OctetString"
_EtsysEncrDot1xAuthReAuthPeriod_Object = MibTableColumn
etsysEncrDot1xAuthReAuthPeriod = _EtsysEncrDot1xAuthReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 19, 1, 1, 1, 1, 8),
    _EtsysEncrDot1xAuthReAuthPeriod_Type()
)
etsysEncrDot1xAuthReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysEncrDot1xAuthReAuthPeriod.setStatus("current")


class _EtsysEncrDot1xAuthReAuthEnabled_Type(OctetString):
    """Custom type etsysEncrDot1xAuthReAuthEnabled based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EtsysEncrDot1xAuthReAuthEnabled_Type.__name__ = "OctetString"
_EtsysEncrDot1xAuthReAuthEnabled_Object = MibTableColumn
etsysEncrDot1xAuthReAuthEnabled = _EtsysEncrDot1xAuthReAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 19, 1, 1, 1, 1, 9),
    _EtsysEncrDot1xAuthReAuthEnabled_Type()
)
etsysEncrDot1xAuthReAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysEncrDot1xAuthReAuthEnabled.setStatus("current")


class _EtsysEncrDot1xAuthKeyTxEnabled_Type(OctetString):
    """Custom type etsysEncrDot1xAuthKeyTxEnabled based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EtsysEncrDot1xAuthKeyTxEnabled_Type.__name__ = "OctetString"
_EtsysEncrDot1xAuthKeyTxEnabled_Object = MibTableColumn
etsysEncrDot1xAuthKeyTxEnabled = _EtsysEncrDot1xAuthKeyTxEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 19, 1, 1, 1, 1, 10),
    _EtsysEncrDot1xAuthKeyTxEnabled_Type()
)
etsysEncrDot1xAuthKeyTxEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysEncrDot1xAuthKeyTxEnabled.setStatus("current")
_EtsysEncrDot1xAuthPortInitTable_Object = MibTable
etsysEncrDot1xAuthPortInitTable = _EtsysEncrDot1xAuthPortInitTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 19, 1, 1, 2)
)
if mibBuilder.loadTexts:
    etsysEncrDot1xAuthPortInitTable.setStatus("current")
_EtsysEncrDot1xAuthPortInitEntry_Object = MibTableRow
etsysEncrDot1xAuthPortInitEntry = _EtsysEncrDot1xAuthPortInitEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 19, 1, 1, 2, 1)
)
etsysEncrDot1xAuthPortInitEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    etsysEncrDot1xAuthPortInitEntry.setStatus("current")


class _EtsysEncrDot1xAuthInitialize_Type(OctetString):
    """Custom type etsysEncrDot1xAuthInitialize based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EtsysEncrDot1xAuthInitialize_Type.__name__ = "OctetString"
_EtsysEncrDot1xAuthInitialize_Object = MibTableColumn
etsysEncrDot1xAuthInitialize = _EtsysEncrDot1xAuthInitialize_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 19, 1, 1, 2, 1, 1),
    _EtsysEncrDot1xAuthInitialize_Type()
)
etsysEncrDot1xAuthInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysEncrDot1xAuthInitialize.setStatus("current")


class _EtsysEncrDot1xAuthReauthenticate_Type(OctetString):
    """Custom type etsysEncrDot1xAuthReauthenticate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EtsysEncrDot1xAuthReauthenticate_Type.__name__ = "OctetString"
_EtsysEncrDot1xAuthReauthenticate_Object = MibTableColumn
etsysEncrDot1xAuthReauthenticate = _EtsysEncrDot1xAuthReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 19, 1, 1, 2, 1, 2),
    _EtsysEncrDot1xAuthReauthenticate_Type()
)
etsysEncrDot1xAuthReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysEncrDot1xAuthReauthenticate.setStatus("current")
_EtsysEncrDot1xAuthStationInitTable_Object = MibTable
etsysEncrDot1xAuthStationInitTable = _EtsysEncrDot1xAuthStationInitTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 19, 1, 1, 3)
)
if mibBuilder.loadTexts:
    etsysEncrDot1xAuthStationInitTable.setStatus("current")
_EtsysEncrDot1xAuthStationInitEntry_Object = MibTableRow
etsysEncrDot1xAuthStationInitEntry = _EtsysEncrDot1xAuthStationInitEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 19, 1, 1, 3, 1)
)
etsysEncrDot1xAuthStationInitEntry.setIndexNames(
    (0, "ENTERASYS-8021X-EXTENSIONS-MIB", "etsysDot1xAuthStationAddress"),
)
if mibBuilder.loadTexts:
    etsysEncrDot1xAuthStationInitEntry.setStatus("current")


class _EtsysEncrDot1xAuthStationInitialize_Type(OctetString):
    """Custom type etsysEncrDot1xAuthStationInitialize based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EtsysEncrDot1xAuthStationInitialize_Type.__name__ = "OctetString"
_EtsysEncrDot1xAuthStationInitialize_Object = MibTableColumn
etsysEncrDot1xAuthStationInitialize = _EtsysEncrDot1xAuthStationInitialize_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 19, 1, 1, 3, 1, 1),
    _EtsysEncrDot1xAuthStationInitialize_Type()
)
etsysEncrDot1xAuthStationInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysEncrDot1xAuthStationInitialize.setStatus("current")


class _EtsysEncrDot1xAuthStationReauthenticate_Type(OctetString):
    """Custom type etsysEncrDot1xAuthStationReauthenticate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EtsysEncrDot1xAuthStationReauthenticate_Type.__name__ = "OctetString"
_EtsysEncrDot1xAuthStationReauthenticate_Object = MibTableColumn
etsysEncrDot1xAuthStationReauthenticate = _EtsysEncrDot1xAuthStationReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 19, 1, 1, 3, 1, 2),
    _EtsysEncrDot1xAuthStationReauthenticate_Type()
)
etsysEncrDot1xAuthStationReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysEncrDot1xAuthStationReauthenticate.setStatus("current")
_EtsysEncrDot1xConfigConformance_ObjectIdentity = ObjectIdentity
etsysEncrDot1xConfigConformance = _EtsysEncrDot1xConfigConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 19, 2)
)
_EtsysEncrDot1xConfigGroups_ObjectIdentity = ObjectIdentity
etsysEncrDot1xConfigGroups = _EtsysEncrDot1xConfigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 19, 2, 1)
)
_EtsysEncrDot1xConfigCompliances_ObjectIdentity = ObjectIdentity
etsysEncrDot1xConfigCompliances = _EtsysEncrDot1xConfigCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 19, 2, 2)
)

# Managed Objects groups

etsysEncrDot1xAuthConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 19, 2, 1, 1)
)
etsysEncrDot1xAuthConfigGroup.setObjects(
      *(("ENTERASYS-ENCR-8021X-CONFIG-MIB", "etsysEncrDot1xAuthAdminControlledDirections"),
        ("ENTERASYS-ENCR-8021X-CONFIG-MIB", "etsysEncrDot1xAuthControlledPortControl"),
        ("ENTERASYS-ENCR-8021X-CONFIG-MIB", "etsysEncrDot1xAuthQuietPeriod"),
        ("ENTERASYS-ENCR-8021X-CONFIG-MIB", "etsysEncrDot1xAuthTxPeriod"),
        ("ENTERASYS-ENCR-8021X-CONFIG-MIB", "etsysEncrDot1xAuthSuppTimeout"),
        ("ENTERASYS-ENCR-8021X-CONFIG-MIB", "etsysEncrDot1xAuthServerTimeout"),
        ("ENTERASYS-ENCR-8021X-CONFIG-MIB", "etsysEncrDot1xAuthMaxReq"),
        ("ENTERASYS-ENCR-8021X-CONFIG-MIB", "etsysEncrDot1xAuthReAuthPeriod"),
        ("ENTERASYS-ENCR-8021X-CONFIG-MIB", "etsysEncrDot1xAuthReAuthEnabled"),
        ("ENTERASYS-ENCR-8021X-CONFIG-MIB", "etsysEncrDot1xAuthKeyTxEnabled"))
)
if mibBuilder.loadTexts:
    etsysEncrDot1xAuthConfigGroup.setStatus("current")

etsysEncrDot1xAuthInitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 19, 2, 1, 2)
)
etsysEncrDot1xAuthInitGroup.setObjects(
      *(("ENTERASYS-ENCR-8021X-CONFIG-MIB", "etsysEncrDot1xAuthInitialize"),
        ("ENTERASYS-ENCR-8021X-CONFIG-MIB", "etsysEncrDot1xAuthReauthenticate"),
        ("ENTERASYS-ENCR-8021X-CONFIG-MIB", "etsysEncrDot1xAuthStationInitialize"),
        ("ENTERASYS-ENCR-8021X-CONFIG-MIB", "etsysEncrDot1xAuthStationReauthenticate"))
)
if mibBuilder.loadTexts:
    etsysEncrDot1xAuthInitGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysEncrDot1xConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 19, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysEncrDot1xConfigCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-ENCR-8021X-CONFIG-MIB",
    **{"etsysEncr8021xConfigMIB": etsysEncr8021xConfigMIB,
       "etsysEncrDot1xConfigObjects": etsysEncrDot1xConfigObjects,
       "etsysEncrDot1xAuthConfigBranch": etsysEncrDot1xAuthConfigBranch,
       "etsysEncrDot1xAuthPortConfigTable": etsysEncrDot1xAuthPortConfigTable,
       "etsysEncrDot1xAuthPortConfigEntry": etsysEncrDot1xAuthPortConfigEntry,
       "etsysEncrDot1xAuthAdminControlledDirections": etsysEncrDot1xAuthAdminControlledDirections,
       "etsysEncrDot1xAuthControlledPortControl": etsysEncrDot1xAuthControlledPortControl,
       "etsysEncrDot1xAuthQuietPeriod": etsysEncrDot1xAuthQuietPeriod,
       "etsysEncrDot1xAuthTxPeriod": etsysEncrDot1xAuthTxPeriod,
       "etsysEncrDot1xAuthSuppTimeout": etsysEncrDot1xAuthSuppTimeout,
       "etsysEncrDot1xAuthServerTimeout": etsysEncrDot1xAuthServerTimeout,
       "etsysEncrDot1xAuthMaxReq": etsysEncrDot1xAuthMaxReq,
       "etsysEncrDot1xAuthReAuthPeriod": etsysEncrDot1xAuthReAuthPeriod,
       "etsysEncrDot1xAuthReAuthEnabled": etsysEncrDot1xAuthReAuthEnabled,
       "etsysEncrDot1xAuthKeyTxEnabled": etsysEncrDot1xAuthKeyTxEnabled,
       "etsysEncrDot1xAuthPortInitTable": etsysEncrDot1xAuthPortInitTable,
       "etsysEncrDot1xAuthPortInitEntry": etsysEncrDot1xAuthPortInitEntry,
       "etsysEncrDot1xAuthInitialize": etsysEncrDot1xAuthInitialize,
       "etsysEncrDot1xAuthReauthenticate": etsysEncrDot1xAuthReauthenticate,
       "etsysEncrDot1xAuthStationInitTable": etsysEncrDot1xAuthStationInitTable,
       "etsysEncrDot1xAuthStationInitEntry": etsysEncrDot1xAuthStationInitEntry,
       "etsysEncrDot1xAuthStationInitialize": etsysEncrDot1xAuthStationInitialize,
       "etsysEncrDot1xAuthStationReauthenticate": etsysEncrDot1xAuthStationReauthenticate,
       "etsysEncrDot1xConfigConformance": etsysEncrDot1xConfigConformance,
       "etsysEncrDot1xConfigGroups": etsysEncrDot1xConfigGroups,
       "etsysEncrDot1xAuthConfigGroup": etsysEncrDot1xAuthConfigGroup,
       "etsysEncrDot1xAuthInitGroup": etsysEncrDot1xAuthInitGroup,
       "etsysEncrDot1xConfigCompliances": etsysEncrDot1xConfigCompliances,
       "etsysEncrDot1xConfigCompliance": etsysEncrDot1xConfigCompliance}
)
