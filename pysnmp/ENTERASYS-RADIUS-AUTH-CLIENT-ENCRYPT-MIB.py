# SNMP MIB module (ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:26 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

etsysRadiusAuthClientEncryptMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 5)
)
etsysRadiusAuthClientEncryptMIB.setRevisions(
        ("2002-11-11 15:56",
         "2002-01-24 16:06",
         "2000-11-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RadiusEncryptedString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_EtsysRadiusAuthClientEncryptMIBObjects_ObjectIdentity = ObjectIdentity
etsysRadiusAuthClientEncryptMIBObjects = _EtsysRadiusAuthClientEncryptMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 1)
)
_EtsysRadiusAuthClientRetryTimeoutEncrypt_Type = RadiusEncryptedString
_EtsysRadiusAuthClientRetryTimeoutEncrypt_Object = MibScalar
etsysRadiusAuthClientRetryTimeoutEncrypt = _EtsysRadiusAuthClientRetryTimeoutEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 1, 1),
    _EtsysRadiusAuthClientRetryTimeoutEncrypt_Type()
)
etsysRadiusAuthClientRetryTimeoutEncrypt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRadiusAuthClientRetryTimeoutEncrypt.setStatus("obsolete")
_EtsysRadiusAuthClientRetriesEncrypt_Type = RadiusEncryptedString
_EtsysRadiusAuthClientRetriesEncrypt_Object = MibScalar
etsysRadiusAuthClientRetriesEncrypt = _EtsysRadiusAuthClientRetriesEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 1, 2),
    _EtsysRadiusAuthClientRetriesEncrypt_Type()
)
etsysRadiusAuthClientRetriesEncrypt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRadiusAuthClientRetriesEncrypt.setStatus("obsolete")
_EtsysRadiusAuthClientEnableEncrypt_Type = RadiusEncryptedString
_EtsysRadiusAuthClientEnableEncrypt_Object = MibScalar
etsysRadiusAuthClientEnableEncrypt = _EtsysRadiusAuthClientEnableEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 1, 3),
    _EtsysRadiusAuthClientEnableEncrypt_Type()
)
etsysRadiusAuthClientEnableEncrypt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRadiusAuthClientEnableEncrypt.setStatus("obsolete")
_EtsysRadiusAuthClientAuthTypeEncrypt_Type = RadiusEncryptedString
_EtsysRadiusAuthClientAuthTypeEncrypt_Object = MibScalar
etsysRadiusAuthClientAuthTypeEncrypt = _EtsysRadiusAuthClientAuthTypeEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 1, 4),
    _EtsysRadiusAuthClientAuthTypeEncrypt_Type()
)
etsysRadiusAuthClientAuthTypeEncrypt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRadiusAuthClientAuthTypeEncrypt.setStatus("obsolete")
_EtsysRadiusAuthClientManageAuthKeyEncrypt_Type = RadiusEncryptedString
_EtsysRadiusAuthClientManageAuthKeyEncrypt_Object = MibScalar
etsysRadiusAuthClientManageAuthKeyEncrypt = _EtsysRadiusAuthClientManageAuthKeyEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 1, 5),
    _EtsysRadiusAuthClientManageAuthKeyEncrypt_Type()
)
etsysRadiusAuthClientManageAuthKeyEncrypt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRadiusAuthClientManageAuthKeyEncrypt.setStatus("obsolete")
_EtsysRadiusAuthServerEncryptTable_Object = MibTable
etsysRadiusAuthServerEncryptTable = _EtsysRadiusAuthServerEncryptTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 1, 6)
)
if mibBuilder.loadTexts:
    etsysRadiusAuthServerEncryptTable.setStatus("obsolete")
_EtsysRadiusAuthServerEncryptEntry_Object = MibTableRow
etsysRadiusAuthServerEncryptEntry = _EtsysRadiusAuthServerEncryptEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 1, 6, 1)
)
etsysRadiusAuthServerEncryptEntry.setIndexNames(
    (0, "ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB", "etsysRadiusAuthServerIndexEncrypt"),
)
if mibBuilder.loadTexts:
    etsysRadiusAuthServerEncryptEntry.setStatus("obsolete")


class _EtsysRadiusAuthServerIndexEncrypt_Type(Integer32):
    """Custom type etsysRadiusAuthServerIndexEncrypt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EtsysRadiusAuthServerIndexEncrypt_Type.__name__ = "Integer32"
_EtsysRadiusAuthServerIndexEncrypt_Object = MibTableColumn
etsysRadiusAuthServerIndexEncrypt = _EtsysRadiusAuthServerIndexEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 1, 6, 1, 1),
    _EtsysRadiusAuthServerIndexEncrypt_Type()
)
etsysRadiusAuthServerIndexEncrypt.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysRadiusAuthServerIndexEncrypt.setStatus("obsolete")
_EtsysRadiusAuthClientServerAddressEncrypt_Type = RadiusEncryptedString
_EtsysRadiusAuthClientServerAddressEncrypt_Object = MibTableColumn
etsysRadiusAuthClientServerAddressEncrypt = _EtsysRadiusAuthClientServerAddressEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 1, 6, 1, 2),
    _EtsysRadiusAuthClientServerAddressEncrypt_Type()
)
etsysRadiusAuthClientServerAddressEncrypt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusAuthClientServerAddressEncrypt.setStatus("obsolete")
_EtsysRadiusAuthClientServerPortNumberEncrypt_Type = RadiusEncryptedString
_EtsysRadiusAuthClientServerPortNumberEncrypt_Object = MibTableColumn
etsysRadiusAuthClientServerPortNumberEncrypt = _EtsysRadiusAuthClientServerPortNumberEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 1, 6, 1, 3),
    _EtsysRadiusAuthClientServerPortNumberEncrypt_Type()
)
etsysRadiusAuthClientServerPortNumberEncrypt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusAuthClientServerPortNumberEncrypt.setStatus("obsolete")
_EtsysRadiusAuthClientServerSecretEncrypt_Type = RadiusEncryptedString
_EtsysRadiusAuthClientServerSecretEncrypt_Object = MibTableColumn
etsysRadiusAuthClientServerSecretEncrypt = _EtsysRadiusAuthClientServerSecretEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 1, 6, 1, 4),
    _EtsysRadiusAuthClientServerSecretEncrypt_Type()
)
etsysRadiusAuthClientServerSecretEncrypt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusAuthClientServerSecretEncrypt.setStatus("obsolete")
_EtsysRadiusAuthClientServerSecretEnteredEncrypt_Type = RadiusEncryptedString
_EtsysRadiusAuthClientServerSecretEnteredEncrypt_Object = MibTableColumn
etsysRadiusAuthClientServerSecretEnteredEncrypt = _EtsysRadiusAuthClientServerSecretEnteredEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 1, 6, 1, 5),
    _EtsysRadiusAuthClientServerSecretEnteredEncrypt_Type()
)
etsysRadiusAuthClientServerSecretEnteredEncrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysRadiusAuthClientServerSecretEnteredEncrypt.setStatus("obsolete")
_EtsysRadiusAuthClientServerClearTimeEncrypt_Type = RadiusEncryptedString
_EtsysRadiusAuthClientServerClearTimeEncrypt_Object = MibTableColumn
etsysRadiusAuthClientServerClearTimeEncrypt = _EtsysRadiusAuthClientServerClearTimeEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 1, 6, 1, 6),
    _EtsysRadiusAuthClientServerClearTimeEncrypt_Type()
)
etsysRadiusAuthClientServerClearTimeEncrypt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusAuthClientServerClearTimeEncrypt.setStatus("obsolete")
_EtsysRadiusAuthClientServerStatusEncrypt_Type = RowStatus
_EtsysRadiusAuthClientServerStatusEncrypt_Object = MibTableColumn
etsysRadiusAuthClientServerStatusEncrypt = _EtsysRadiusAuthClientServerStatusEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 1, 6, 1, 7),
    _EtsysRadiusAuthClientServerStatusEncrypt_Type()
)
etsysRadiusAuthClientServerStatusEncrypt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusAuthClientServerStatusEncrypt.setStatus("obsolete")
_EtsysRadiusAuthClientEncryptMIBConformance_ObjectIdentity = ObjectIdentity
etsysRadiusAuthClientEncryptMIBConformance = _EtsysRadiusAuthClientEncryptMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 2)
)
_EtsysRadiusAuthClientEncryptMIBCompliances_ObjectIdentity = ObjectIdentity
etsysRadiusAuthClientEncryptMIBCompliances = _EtsysRadiusAuthClientEncryptMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 2, 1)
)
_EtsysRadiusAuthClientEncryptMIBGroups_ObjectIdentity = ObjectIdentity
etsysRadiusAuthClientEncryptMIBGroups = _EtsysRadiusAuthClientEncryptMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 2, 2)
)

# Managed Objects groups

etsysRadiusAuthClientEncryptMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 2, 2, 1)
)
etsysRadiusAuthClientEncryptMIBGroup.setObjects(
      *(("ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB", "etsysRadiusAuthClientRetryTimeoutEncrypt"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB", "etsysRadiusAuthClientRetriesEncrypt"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB", "etsysRadiusAuthClientEnableEncrypt"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB", "etsysRadiusAuthClientAuthTypeEncrypt"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB", "etsysRadiusAuthClientManageAuthKeyEncrypt"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB", "etsysRadiusAuthClientServerAddressEncrypt"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB", "etsysRadiusAuthClientServerPortNumberEncrypt"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB", "etsysRadiusAuthClientServerSecretEncrypt"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB", "etsysRadiusAuthClientServerSecretEnteredEncrypt"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB", "etsysRadiusAuthClientServerClearTimeEncrypt"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB", "etsysRadiusAuthClientServerStatusEncrypt"))
)
if mibBuilder.loadTexts:
    etsysRadiusAuthClientEncryptMIBGroup.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysRadiusClientEncryptMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    etsysRadiusClientEncryptMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB",
    **{"RadiusEncryptedString": RadiusEncryptedString,
       "etsysRadiusAuthClientEncryptMIB": etsysRadiusAuthClientEncryptMIB,
       "etsysRadiusAuthClientEncryptMIBObjects": etsysRadiusAuthClientEncryptMIBObjects,
       "etsysRadiusAuthClientRetryTimeoutEncrypt": etsysRadiusAuthClientRetryTimeoutEncrypt,
       "etsysRadiusAuthClientRetriesEncrypt": etsysRadiusAuthClientRetriesEncrypt,
       "etsysRadiusAuthClientEnableEncrypt": etsysRadiusAuthClientEnableEncrypt,
       "etsysRadiusAuthClientAuthTypeEncrypt": etsysRadiusAuthClientAuthTypeEncrypt,
       "etsysRadiusAuthClientManageAuthKeyEncrypt": etsysRadiusAuthClientManageAuthKeyEncrypt,
       "etsysRadiusAuthServerEncryptTable": etsysRadiusAuthServerEncryptTable,
       "etsysRadiusAuthServerEncryptEntry": etsysRadiusAuthServerEncryptEntry,
       "etsysRadiusAuthServerIndexEncrypt": etsysRadiusAuthServerIndexEncrypt,
       "etsysRadiusAuthClientServerAddressEncrypt": etsysRadiusAuthClientServerAddressEncrypt,
       "etsysRadiusAuthClientServerPortNumberEncrypt": etsysRadiusAuthClientServerPortNumberEncrypt,
       "etsysRadiusAuthClientServerSecretEncrypt": etsysRadiusAuthClientServerSecretEncrypt,
       "etsysRadiusAuthClientServerSecretEnteredEncrypt": etsysRadiusAuthClientServerSecretEnteredEncrypt,
       "etsysRadiusAuthClientServerClearTimeEncrypt": etsysRadiusAuthClientServerClearTimeEncrypt,
       "etsysRadiusAuthClientServerStatusEncrypt": etsysRadiusAuthClientServerStatusEncrypt,
       "etsysRadiusAuthClientEncryptMIBConformance": etsysRadiusAuthClientEncryptMIBConformance,
       "etsysRadiusAuthClientEncryptMIBCompliances": etsysRadiusAuthClientEncryptMIBCompliances,
       "etsysRadiusClientEncryptMIBCompliance": etsysRadiusClientEncryptMIBCompliance,
       "etsysRadiusAuthClientEncryptMIBGroups": etsysRadiusAuthClientEncryptMIBGroups,
       "etsysRadiusAuthClientEncryptMIBGroup": etsysRadiusAuthClientEncryptMIBGroup}
)
