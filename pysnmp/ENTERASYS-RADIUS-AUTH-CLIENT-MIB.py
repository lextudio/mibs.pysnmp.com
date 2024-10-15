# SNMP MIB module (ENTERASYS-RADIUS-AUTH-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-RADIUS-AUTH-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:27 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

etsysRadiusAuthClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4)
)
etsysRadiusAuthClientMIB.setRevisions(
        ("2011-06-29 17:14",
         "2009-08-06 18:38",
         "2005-07-29 13:48",
         "2004-07-27 19:53",
         "2003-11-06 18:23",
         "2002-01-24 15:57",
         "2000-11-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysRadiusAuthClientMIBObjects_ObjectIdentity = ObjectIdentity
etsysRadiusAuthClientMIBObjects = _EtsysRadiusAuthClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1)
)


class _EtsysRadiusAuthClientRetryTimeout_Type(Integer32):
    """Custom type etsysRadiusAuthClientRetryTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EtsysRadiusAuthClientRetryTimeout_Type.__name__ = "Integer32"
_EtsysRadiusAuthClientRetryTimeout_Object = MibScalar
etsysRadiusAuthClientRetryTimeout = _EtsysRadiusAuthClientRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 1),
    _EtsysRadiusAuthClientRetryTimeout_Type()
)
etsysRadiusAuthClientRetryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRadiusAuthClientRetryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysRadiusAuthClientRetryTimeout.setUnits("seconds")


class _EtsysRadiusAuthClientRetries_Type(Integer32):
    """Custom type etsysRadiusAuthClientRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EtsysRadiusAuthClientRetries_Type.__name__ = "Integer32"
_EtsysRadiusAuthClientRetries_Object = MibScalar
etsysRadiusAuthClientRetries = _EtsysRadiusAuthClientRetries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 2),
    _EtsysRadiusAuthClientRetries_Type()
)
etsysRadiusAuthClientRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRadiusAuthClientRetries.setStatus("current")


class _EtsysRadiusAuthClientEnable_Type(Integer32):
    """Custom type etsysRadiusAuthClientEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_EtsysRadiusAuthClientEnable_Type.__name__ = "Integer32"
_EtsysRadiusAuthClientEnable_Object = MibScalar
etsysRadiusAuthClientEnable = _EtsysRadiusAuthClientEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 3),
    _EtsysRadiusAuthClientEnable_Type()
)
etsysRadiusAuthClientEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRadiusAuthClientEnable.setStatus("current")


class _EtsysRadiusAuthClientAuthType_Type(Integer32):
    """Custom type etsysRadiusAuthClientAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eapol", 2),
          ("mac", 1))
    )


_EtsysRadiusAuthClientAuthType_Type.__name__ = "Integer32"
_EtsysRadiusAuthClientAuthType_Object = MibScalar
etsysRadiusAuthClientAuthType = _EtsysRadiusAuthClientAuthType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 4),
    _EtsysRadiusAuthClientAuthType_Type()
)
etsysRadiusAuthClientAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRadiusAuthClientAuthType.setStatus("deprecated")
_EtsysRadiusAuthServerTable_Object = MibTable
etsysRadiusAuthServerTable = _EtsysRadiusAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 5)
)
if mibBuilder.loadTexts:
    etsysRadiusAuthServerTable.setStatus("current")
_EtsysRadiusAuthServerEntry_Object = MibTableRow
etsysRadiusAuthServerEntry = _EtsysRadiusAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 5, 1)
)
etsysRadiusAuthServerEntry.setIndexNames(
    (0, "ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthServerIndex"),
)
if mibBuilder.loadTexts:
    etsysRadiusAuthServerEntry.setStatus("current")


class _EtsysRadiusAuthServerIndex_Type(Integer32):
    """Custom type etsysRadiusAuthServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EtsysRadiusAuthServerIndex_Type.__name__ = "Integer32"
_EtsysRadiusAuthServerIndex_Object = MibTableColumn
etsysRadiusAuthServerIndex = _EtsysRadiusAuthServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 5, 1, 1),
    _EtsysRadiusAuthServerIndex_Type()
)
etsysRadiusAuthServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysRadiusAuthServerIndex.setStatus("current")


class _EtsysRadiusAuthClientServerAddressType_Type(InetAddressType):
    """Custom type etsysRadiusAuthClientServerAddressType based on InetAddressType"""


_EtsysRadiusAuthClientServerAddressType_Object = MibTableColumn
etsysRadiusAuthClientServerAddressType = _EtsysRadiusAuthClientServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 5, 1, 2),
    _EtsysRadiusAuthClientServerAddressType_Type()
)
etsysRadiusAuthClientServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusAuthClientServerAddressType.setStatus("current")


class _EtsysRadiusAuthClientServerAddress_Type(InetAddress):
    """Custom type etsysRadiusAuthClientServerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EtsysRadiusAuthClientServerAddress_Type.__name__ = "InetAddress"
_EtsysRadiusAuthClientServerAddress_Object = MibTableColumn
etsysRadiusAuthClientServerAddress = _EtsysRadiusAuthClientServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 5, 1, 3),
    _EtsysRadiusAuthClientServerAddress_Type()
)
etsysRadiusAuthClientServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusAuthClientServerAddress.setStatus("current")


class _EtsysRadiusAuthClientServerPortNumber_Type(Integer32):
    """Custom type etsysRadiusAuthClientServerPortNumber based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EtsysRadiusAuthClientServerPortNumber_Type.__name__ = "Integer32"
_EtsysRadiusAuthClientServerPortNumber_Object = MibTableColumn
etsysRadiusAuthClientServerPortNumber = _EtsysRadiusAuthClientServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 5, 1, 4),
    _EtsysRadiusAuthClientServerPortNumber_Type()
)
etsysRadiusAuthClientServerPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusAuthClientServerPortNumber.setStatus("current")


class _EtsysRadiusAuthClientServerSecret_Type(OctetString):
    """Custom type etsysRadiusAuthClientServerSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EtsysRadiusAuthClientServerSecret_Type.__name__ = "OctetString"
_EtsysRadiusAuthClientServerSecret_Object = MibTableColumn
etsysRadiusAuthClientServerSecret = _EtsysRadiusAuthClientServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 5, 1, 5),
    _EtsysRadiusAuthClientServerSecret_Type()
)
etsysRadiusAuthClientServerSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusAuthClientServerSecret.setStatus("current")
_EtsysRadiusAuthClientServerSecretEntered_Type = TruthValue
_EtsysRadiusAuthClientServerSecretEntered_Object = MibTableColumn
etsysRadiusAuthClientServerSecretEntered = _EtsysRadiusAuthClientServerSecretEntered_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 5, 1, 6),
    _EtsysRadiusAuthClientServerSecretEntered_Type()
)
etsysRadiusAuthClientServerSecretEntered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysRadiusAuthClientServerSecretEntered.setStatus("current")


class _EtsysRadiusAuthClientServerClearTime_Type(Integer32):
    """Custom type etsysRadiusAuthClientServerClearTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EtsysRadiusAuthClientServerClearTime_Type.__name__ = "Integer32"
_EtsysRadiusAuthClientServerClearTime_Object = MibTableColumn
etsysRadiusAuthClientServerClearTime = _EtsysRadiusAuthClientServerClearTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 5, 1, 7),
    _EtsysRadiusAuthClientServerClearTime_Type()
)
etsysRadiusAuthClientServerClearTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusAuthClientServerClearTime.setStatus("deprecated")
if mibBuilder.loadTexts:
    etsysRadiusAuthClientServerClearTime.setUnits("seconds")
_EtsysRadiusAuthClientServerStatus_Type = RowStatus
_EtsysRadiusAuthClientServerStatus_Object = MibTableColumn
etsysRadiusAuthClientServerStatus = _EtsysRadiusAuthClientServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 5, 1, 8),
    _EtsysRadiusAuthClientServerStatus_Type()
)
etsysRadiusAuthClientServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusAuthClientServerStatus.setStatus("current")


class _EtsysRadiusAuthClientServerRealmType_Type(Integer32):
    """Custom type etsysRadiusAuthClientServerRealmType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("mgmtAccess", 2),
          ("networkAccess", 3))
    )


_EtsysRadiusAuthClientServerRealmType_Type.__name__ = "Integer32"
_EtsysRadiusAuthClientServerRealmType_Object = MibTableColumn
etsysRadiusAuthClientServerRealmType = _EtsysRadiusAuthClientServerRealmType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 5, 1, 9),
    _EtsysRadiusAuthClientServerRealmType_Type()
)
etsysRadiusAuthClientServerRealmType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusAuthClientServerRealmType.setStatus("current")


class _EtsysRadiusAuthClientServerTimeout_Type(Integer32):
    """Custom type etsysRadiusAuthClientServerTimeout based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 60),
    )


_EtsysRadiusAuthClientServerTimeout_Type.__name__ = "Integer32"
_EtsysRadiusAuthClientServerTimeout_Object = MibTableColumn
etsysRadiusAuthClientServerTimeout = _EtsysRadiusAuthClientServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 5, 1, 10),
    _EtsysRadiusAuthClientServerTimeout_Type()
)
etsysRadiusAuthClientServerTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusAuthClientServerTimeout.setStatus("current")


class _EtsysRadiusAuthClientServerRetries_Type(Integer32):
    """Custom type etsysRadiusAuthClientServerRetries based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 10),
    )


_EtsysRadiusAuthClientServerRetries_Type.__name__ = "Integer32"
_EtsysRadiusAuthClientServerRetries_Object = MibTableColumn
etsysRadiusAuthClientServerRetries = _EtsysRadiusAuthClientServerRetries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 5, 1, 11),
    _EtsysRadiusAuthClientServerRetries_Type()
)
etsysRadiusAuthClientServerRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusAuthClientServerRetries.setStatus("current")


class _EtsysRadiusAuthClientAttrMgmtPassword_Type(Integer32):
    """Custom type etsysRadiusAuthClientAttrMgmtPassword based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mschapv2", 2),
          ("standard", 1))
    )


_EtsysRadiusAuthClientAttrMgmtPassword_Type.__name__ = "Integer32"
_EtsysRadiusAuthClientAttrMgmtPassword_Object = MibScalar
etsysRadiusAuthClientAttrMgmtPassword = _EtsysRadiusAuthClientAttrMgmtPassword_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 6),
    _EtsysRadiusAuthClientAttrMgmtPassword_Type()
)
etsysRadiusAuthClientAttrMgmtPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRadiusAuthClientAttrMgmtPassword.setStatus("current")
_EtsysRadiusAuthClientMIBConformance_ObjectIdentity = ObjectIdentity
etsysRadiusAuthClientMIBConformance = _EtsysRadiusAuthClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 2)
)
_EtsysRadiusAuthClientMIBCompliances_ObjectIdentity = ObjectIdentity
etsysRadiusAuthClientMIBCompliances = _EtsysRadiusAuthClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 2, 1)
)
_EtsysRadiusAuthClientMIBGroups_ObjectIdentity = ObjectIdentity
etsysRadiusAuthClientMIBGroups = _EtsysRadiusAuthClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 2, 2)
)

# Managed Objects groups

etsysRadiusAuthClientMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 2, 2, 1)
)
etsysRadiusAuthClientMIBGroup.setObjects(
      *(("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientRetryTimeout"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientRetries"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientEnable"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientAuthType"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerAddressType"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerAddress"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerPortNumber"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerSecret"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerSecretEntered"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerClearTime"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerStatus"))
)
if mibBuilder.loadTexts:
    etsysRadiusAuthClientMIBGroup.setStatus("deprecated")

etsysRadiusAuthClientMIBGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 2, 2, 2)
)
etsysRadiusAuthClientMIBGroupV2.setObjects(
      *(("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientRetryTimeout"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientRetries"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientEnable"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerAddressType"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerAddress"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerPortNumber"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerSecret"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerSecretEntered"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerStatus"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerRealmType"))
)
if mibBuilder.loadTexts:
    etsysRadiusAuthClientMIBGroupV2.setStatus("deprecated")

etsysRadiusAuthClientMIBGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 2, 2, 3)
)
etsysRadiusAuthClientMIBGroupV3.setObjects(
      *(("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientRetryTimeout"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientRetries"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientEnable"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerAddressType"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerAddress"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerPortNumber"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerSecret"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerSecretEntered"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerStatus"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerRealmType"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerTimeout"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerRetries"))
)
if mibBuilder.loadTexts:
    etsysRadiusAuthClientMIBGroupV3.setStatus("deprecated")

etsysRadiusAuthClientMIBGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 2, 2, 4)
)
etsysRadiusAuthClientMIBGroupV4.setObjects(
      *(("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientRetryTimeout"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientRetries"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientEnable"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerAddressType"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerAddress"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerPortNumber"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerSecret"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerSecretEntered"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerStatus"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerRealmType"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerTimeout"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerRetries"),
        ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientAttrMgmtPassword"))
)
if mibBuilder.loadTexts:
    etsysRadiusAuthClientMIBGroupV4.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysRadiusClientMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    etsysRadiusClientMIBCompliance.setStatus(
        "deprecated"
    )

etsysRadiusClientMIBComplianceV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 2, 1, 2)
)
if mibBuilder.loadTexts:
    etsysRadiusClientMIBComplianceV2.setStatus(
        "deprecated"
    )

etsysRadiusClientMIBComplianceV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 2, 1, 3)
)
if mibBuilder.loadTexts:
    etsysRadiusClientMIBComplianceV3.setStatus(
        "deprecated"
    )

etsysRadiusClientMIBComplianceV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 2, 1, 4)
)
if mibBuilder.loadTexts:
    etsysRadiusClientMIBComplianceV4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-RADIUS-AUTH-CLIENT-MIB",
    **{"etsysRadiusAuthClientMIB": etsysRadiusAuthClientMIB,
       "etsysRadiusAuthClientMIBObjects": etsysRadiusAuthClientMIBObjects,
       "etsysRadiusAuthClientRetryTimeout": etsysRadiusAuthClientRetryTimeout,
       "etsysRadiusAuthClientRetries": etsysRadiusAuthClientRetries,
       "etsysRadiusAuthClientEnable": etsysRadiusAuthClientEnable,
       "etsysRadiusAuthClientAuthType": etsysRadiusAuthClientAuthType,
       "etsysRadiusAuthServerTable": etsysRadiusAuthServerTable,
       "etsysRadiusAuthServerEntry": etsysRadiusAuthServerEntry,
       "etsysRadiusAuthServerIndex": etsysRadiusAuthServerIndex,
       "etsysRadiusAuthClientServerAddressType": etsysRadiusAuthClientServerAddressType,
       "etsysRadiusAuthClientServerAddress": etsysRadiusAuthClientServerAddress,
       "etsysRadiusAuthClientServerPortNumber": etsysRadiusAuthClientServerPortNumber,
       "etsysRadiusAuthClientServerSecret": etsysRadiusAuthClientServerSecret,
       "etsysRadiusAuthClientServerSecretEntered": etsysRadiusAuthClientServerSecretEntered,
       "etsysRadiusAuthClientServerClearTime": etsysRadiusAuthClientServerClearTime,
       "etsysRadiusAuthClientServerStatus": etsysRadiusAuthClientServerStatus,
       "etsysRadiusAuthClientServerRealmType": etsysRadiusAuthClientServerRealmType,
       "etsysRadiusAuthClientServerTimeout": etsysRadiusAuthClientServerTimeout,
       "etsysRadiusAuthClientServerRetries": etsysRadiusAuthClientServerRetries,
       "etsysRadiusAuthClientAttrMgmtPassword": etsysRadiusAuthClientAttrMgmtPassword,
       "etsysRadiusAuthClientMIBConformance": etsysRadiusAuthClientMIBConformance,
       "etsysRadiusAuthClientMIBCompliances": etsysRadiusAuthClientMIBCompliances,
       "etsysRadiusClientMIBCompliance": etsysRadiusClientMIBCompliance,
       "etsysRadiusClientMIBComplianceV2": etsysRadiusClientMIBComplianceV2,
       "etsysRadiusClientMIBComplianceV3": etsysRadiusClientMIBComplianceV3,
       "etsysRadiusClientMIBComplianceV4": etsysRadiusClientMIBComplianceV4,
       "etsysRadiusAuthClientMIBGroups": etsysRadiusAuthClientMIBGroups,
       "etsysRadiusAuthClientMIBGroup": etsysRadiusAuthClientMIBGroup,
       "etsysRadiusAuthClientMIBGroupV2": etsysRadiusAuthClientMIBGroupV2,
       "etsysRadiusAuthClientMIBGroupV3": etsysRadiusAuthClientMIBGroupV3,
       "etsysRadiusAuthClientMIBGroupV4": etsysRadiusAuthClientMIBGroupV4}
)
