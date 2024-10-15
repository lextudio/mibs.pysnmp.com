# SNMP MIB module (ENTERASYS-TACACS-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-TACACS-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:38 2024
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
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

etsysTacacsClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58)
)
etsysTacacsClientMIB.setRevisions(
        ("2010-02-01 17:02",
         "2005-02-10 17:57")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysTacacsClientObjects_ObjectIdentity = ObjectIdentity
etsysTacacsClientObjects = _EtsysTacacsClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1)
)
_EtsysTacacsClientControl_ObjectIdentity = ObjectIdentity
etsysTacacsClientControl = _EtsysTacacsClientControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 1)
)


class _EtsysTacacsClientSesnAuthEnabled_Type(EnabledStatus):
    """Custom type etsysTacacsClientSesnAuthEnabled based on EnabledStatus"""


_EtsysTacacsClientSesnAuthEnabled_Object = MibScalar
etsysTacacsClientSesnAuthEnabled = _EtsysTacacsClientSesnAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 1, 1),
    _EtsysTacacsClientSesnAuthEnabled_Type()
)
etsysTacacsClientSesnAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTacacsClientSesnAuthEnabled.setStatus("current")


class _EtsysTacacsClientSesnAcctEnabled_Type(EnabledStatus):
    """Custom type etsysTacacsClientSesnAcctEnabled based on EnabledStatus"""


_EtsysTacacsClientSesnAcctEnabled_Object = MibScalar
etsysTacacsClientSesnAcctEnabled = _EtsysTacacsClientSesnAcctEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 1, 2),
    _EtsysTacacsClientSesnAcctEnabled_Type()
)
etsysTacacsClientSesnAcctEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTacacsClientSesnAcctEnabled.setStatus("current")


class _EtsysTacacsClientCmdAuthEnabled_Type(EnabledStatus):
    """Custom type etsysTacacsClientCmdAuthEnabled based on EnabledStatus"""


_EtsysTacacsClientCmdAuthEnabled_Object = MibScalar
etsysTacacsClientCmdAuthEnabled = _EtsysTacacsClientCmdAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 1, 3),
    _EtsysTacacsClientCmdAuthEnabled_Type()
)
etsysTacacsClientCmdAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTacacsClientCmdAuthEnabled.setStatus("current")


class _EtsysTacacsClientCmdAcctEnabled_Type(EnabledStatus):
    """Custom type etsysTacacsClientCmdAcctEnabled based on EnabledStatus"""


_EtsysTacacsClientCmdAcctEnabled_Object = MibScalar
etsysTacacsClientCmdAcctEnabled = _EtsysTacacsClientCmdAcctEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 1, 4),
    _EtsysTacacsClientCmdAcctEnabled_Type()
)
etsysTacacsClientCmdAcctEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTacacsClientCmdAcctEnabled.setStatus("current")


class _EtsysTacacsClientSingleConnection_Type(EnabledStatus):
    """Custom type etsysTacacsClientSingleConnection based on EnabledStatus"""


_EtsysTacacsClientSingleConnection_Object = MibScalar
etsysTacacsClientSingleConnection = _EtsysTacacsClientSingleConnection_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 1, 5),
    _EtsysTacacsClientSingleConnection_Type()
)
etsysTacacsClientSingleConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTacacsClientSingleConnection.setStatus("current")
_EtsysTacacsClientSesnAuth_ObjectIdentity = ObjectIdentity
etsysTacacsClientSesnAuth = _EtsysTacacsClientSesnAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 2)
)


class _EtsysTacacsClientSesnAuthService_Type(SnmpAdminString):
    """Custom type etsysTacacsClientSesnAuthService based on SnmpAdminString"""
    defaultValue = OctetString("enable")


_EtsysTacacsClientSesnAuthService_Object = MibScalar
etsysTacacsClientSesnAuthService = _EtsysTacacsClientSesnAuthService_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 2, 1),
    _EtsysTacacsClientSesnAuthService_Type()
)
etsysTacacsClientSesnAuthService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTacacsClientSesnAuthService.setStatus("current")
_EtsysTacacsClientSesnAuthTable_Object = MibTable
etsysTacacsClientSesnAuthTable = _EtsysTacacsClientSesnAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 2, 2)
)
if mibBuilder.loadTexts:
    etsysTacacsClientSesnAuthTable.setStatus("current")
_EtsysTacacsClientSesnAuthEntry_Object = MibTableRow
etsysTacacsClientSesnAuthEntry = _EtsysTacacsClientSesnAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 2, 2, 1)
)
etsysTacacsClientSesnAuthEntry.setIndexNames(
    (0, "ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientSesnAuthLevel"),
)
if mibBuilder.loadTexts:
    etsysTacacsClientSesnAuthEntry.setStatus("current")


class _EtsysTacacsClientSesnAuthLevel_Type(Integer32):
    """Custom type etsysTacacsClientSesnAuthLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("debug", 4),
          ("readonly", 1),
          ("readwrite", 2),
          ("superuser", 3))
    )


_EtsysTacacsClientSesnAuthLevel_Type.__name__ = "Integer32"
_EtsysTacacsClientSesnAuthLevel_Object = MibTableColumn
etsysTacacsClientSesnAuthLevel = _EtsysTacacsClientSesnAuthLevel_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 2, 2, 1, 1),
    _EtsysTacacsClientSesnAuthLevel_Type()
)
etsysTacacsClientSesnAuthLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysTacacsClientSesnAuthLevel.setStatus("current")


class _EtsysTacacsClientSesnAuthAttribute_Type(SnmpAdminString):
    """Custom type etsysTacacsClientSesnAuthAttribute based on SnmpAdminString"""
    defaultValue = OctetString("priv-lvl")


_EtsysTacacsClientSesnAuthAttribute_Object = MibTableColumn
etsysTacacsClientSesnAuthAttribute = _EtsysTacacsClientSesnAuthAttribute_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 2, 2, 1, 2),
    _EtsysTacacsClientSesnAuthAttribute_Type()
)
etsysTacacsClientSesnAuthAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTacacsClientSesnAuthAttribute.setStatus("current")
_EtsysTacacsClientSesnAuthValue_Type = SnmpAdminString
_EtsysTacacsClientSesnAuthValue_Object = MibTableColumn
etsysTacacsClientSesnAuthValue = _EtsysTacacsClientSesnAuthValue_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 2, 2, 1, 3),
    _EtsysTacacsClientSesnAuthValue_Type()
)
etsysTacacsClientSesnAuthValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTacacsClientSesnAuthValue.setStatus("current")
_EtsysTacacsClientServer_ObjectIdentity = ObjectIdentity
etsysTacacsClientServer = _EtsysTacacsClientServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 3)
)
_EtsysTacacsClientServerTable_Object = MibTable
etsysTacacsClientServerTable = _EtsysTacacsClientServerTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 3, 1)
)
if mibBuilder.loadTexts:
    etsysTacacsClientServerTable.setStatus("current")
_EtsysTacacsClientServerEntry_Object = MibTableRow
etsysTacacsClientServerEntry = _EtsysTacacsClientServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 3, 1, 1)
)
etsysTacacsClientServerEntry.setIndexNames(
    (0, "ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientServerIndex"),
)
if mibBuilder.loadTexts:
    etsysTacacsClientServerEntry.setStatus("current")


class _EtsysTacacsClientServerIndex_Type(Integer32):
    """Custom type etsysTacacsClientServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EtsysTacacsClientServerIndex_Type.__name__ = "Integer32"
_EtsysTacacsClientServerIndex_Object = MibTableColumn
etsysTacacsClientServerIndex = _EtsysTacacsClientServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 3, 1, 1, 1),
    _EtsysTacacsClientServerIndex_Type()
)
etsysTacacsClientServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysTacacsClientServerIndex.setStatus("current")


class _EtsysTacacsClientServerAddressType_Type(InetAddressType):
    """Custom type etsysTacacsClientServerAddressType based on InetAddressType"""


_EtsysTacacsClientServerAddressType_Object = MibTableColumn
etsysTacacsClientServerAddressType = _EtsysTacacsClientServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 3, 1, 1, 2),
    _EtsysTacacsClientServerAddressType_Type()
)
etsysTacacsClientServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTacacsClientServerAddressType.setStatus("current")


class _EtsysTacacsClientServerAddress_Type(InetAddress):
    """Custom type etsysTacacsClientServerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EtsysTacacsClientServerAddress_Type.__name__ = "InetAddress"
_EtsysTacacsClientServerAddress_Object = MibTableColumn
etsysTacacsClientServerAddress = _EtsysTacacsClientServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 3, 1, 1, 3),
    _EtsysTacacsClientServerAddress_Type()
)
etsysTacacsClientServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTacacsClientServerAddress.setStatus("current")


class _EtsysTacacsClientServerPortNumber_Type(InetPortNumber):
    """Custom type etsysTacacsClientServerPortNumber based on InetPortNumber"""
    defaultValue = 49


_EtsysTacacsClientServerPortNumber_Object = MibTableColumn
etsysTacacsClientServerPortNumber = _EtsysTacacsClientServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 3, 1, 1, 4),
    _EtsysTacacsClientServerPortNumber_Type()
)
etsysTacacsClientServerPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTacacsClientServerPortNumber.setStatus("current")


class _EtsysTacacsClientServerTimeout_Type(Integer32):
    """Custom type etsysTacacsClientServerTimeout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_EtsysTacacsClientServerTimeout_Type.__name__ = "Integer32"
_EtsysTacacsClientServerTimeout_Object = MibTableColumn
etsysTacacsClientServerTimeout = _EtsysTacacsClientServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 3, 1, 1, 5),
    _EtsysTacacsClientServerTimeout_Type()
)
etsysTacacsClientServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysTacacsClientServerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysTacacsClientServerTimeout.setUnits("seconds")


class _EtsysTacacsClientServerSecret_Type(OctetString):
    """Custom type etsysTacacsClientServerSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EtsysTacacsClientServerSecret_Type.__name__ = "OctetString"
_EtsysTacacsClientServerSecret_Object = MibTableColumn
etsysTacacsClientServerSecret = _EtsysTacacsClientServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 3, 1, 1, 6),
    _EtsysTacacsClientServerSecret_Type()
)
etsysTacacsClientServerSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTacacsClientServerSecret.setStatus("current")
_EtsysTacacsClientServerSecretEntered_Type = TruthValue
_EtsysTacacsClientServerSecretEntered_Object = MibTableColumn
etsysTacacsClientServerSecretEntered = _EtsysTacacsClientServerSecretEntered_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 3, 1, 1, 7),
    _EtsysTacacsClientServerSecretEntered_Type()
)
etsysTacacsClientServerSecretEntered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysTacacsClientServerSecretEntered.setStatus("current")
_EtsysTacacsClientServerStatus_Type = RowStatus
_EtsysTacacsClientServerStatus_Object = MibTableColumn
etsysTacacsClientServerStatus = _EtsysTacacsClientServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 1, 3, 1, 1, 8),
    _EtsysTacacsClientServerStatus_Type()
)
etsysTacacsClientServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysTacacsClientServerStatus.setStatus("current")
_EtsysTacacsClientConformance_ObjectIdentity = ObjectIdentity
etsysTacacsClientConformance = _EtsysTacacsClientConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 2)
)
_EtsysTacacsClientCompliances_ObjectIdentity = ObjectIdentity
etsysTacacsClientCompliances = _EtsysTacacsClientCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 2, 1)
)
_EtsysTacacsClientGroups_ObjectIdentity = ObjectIdentity
etsysTacacsClientGroups = _EtsysTacacsClientGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 2, 2)
)

# Managed Objects groups

etsysTacacsClientSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 2, 2, 1)
)
etsysTacacsClientSessionGroup.setObjects(
      *(("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientSesnAuthEnabled"),
        ("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientSesnAcctEnabled"),
        ("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientSingleConnection"),
        ("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientServerAddressType"),
        ("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientServerAddress"),
        ("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientServerPortNumber"),
        ("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientServerTimeout"),
        ("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientServerSecret"),
        ("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientServerSecretEntered"),
        ("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientServerStatus"))
)
if mibBuilder.loadTexts:
    etsysTacacsClientSessionGroup.setStatus("current")

etsysTacacsClientCmdAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 2, 2, 2)
)
etsysTacacsClientCmdAuthGroup.setObjects(
    ("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientCmdAuthEnabled")
)
if mibBuilder.loadTexts:
    etsysTacacsClientCmdAuthGroup.setStatus("current")

etsysTacacsClientCmdAcctGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 2, 2, 3)
)
etsysTacacsClientCmdAcctGroup.setObjects(
    ("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientCmdAcctEnabled")
)
if mibBuilder.loadTexts:
    etsysTacacsClientCmdAcctGroup.setStatus("current")

etsysTacacsClientSesnAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 2, 2, 4)
)
etsysTacacsClientSesnAuthGroup.setObjects(
      *(("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientSesnAuthService"),
        ("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientSesnAuthAttribute"),
        ("ENTERASYS-TACACS-CLIENT-MIB", "etsysTacacsClientSesnAuthValue"))
)
if mibBuilder.loadTexts:
    etsysTacacsClientSesnAuthGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysTacacsClientCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 58, 2, 1, 1)
)
if mibBuilder.loadTexts:
    etsysTacacsClientCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-TACACS-CLIENT-MIB",
    **{"etsysTacacsClientMIB": etsysTacacsClientMIB,
       "etsysTacacsClientObjects": etsysTacacsClientObjects,
       "etsysTacacsClientControl": etsysTacacsClientControl,
       "etsysTacacsClientSesnAuthEnabled": etsysTacacsClientSesnAuthEnabled,
       "etsysTacacsClientSesnAcctEnabled": etsysTacacsClientSesnAcctEnabled,
       "etsysTacacsClientCmdAuthEnabled": etsysTacacsClientCmdAuthEnabled,
       "etsysTacacsClientCmdAcctEnabled": etsysTacacsClientCmdAcctEnabled,
       "etsysTacacsClientSingleConnection": etsysTacacsClientSingleConnection,
       "etsysTacacsClientSesnAuth": etsysTacacsClientSesnAuth,
       "etsysTacacsClientSesnAuthService": etsysTacacsClientSesnAuthService,
       "etsysTacacsClientSesnAuthTable": etsysTacacsClientSesnAuthTable,
       "etsysTacacsClientSesnAuthEntry": etsysTacacsClientSesnAuthEntry,
       "etsysTacacsClientSesnAuthLevel": etsysTacacsClientSesnAuthLevel,
       "etsysTacacsClientSesnAuthAttribute": etsysTacacsClientSesnAuthAttribute,
       "etsysTacacsClientSesnAuthValue": etsysTacacsClientSesnAuthValue,
       "etsysTacacsClientServer": etsysTacacsClientServer,
       "etsysTacacsClientServerTable": etsysTacacsClientServerTable,
       "etsysTacacsClientServerEntry": etsysTacacsClientServerEntry,
       "etsysTacacsClientServerIndex": etsysTacacsClientServerIndex,
       "etsysTacacsClientServerAddressType": etsysTacacsClientServerAddressType,
       "etsysTacacsClientServerAddress": etsysTacacsClientServerAddress,
       "etsysTacacsClientServerPortNumber": etsysTacacsClientServerPortNumber,
       "etsysTacacsClientServerTimeout": etsysTacacsClientServerTimeout,
       "etsysTacacsClientServerSecret": etsysTacacsClientServerSecret,
       "etsysTacacsClientServerSecretEntered": etsysTacacsClientServerSecretEntered,
       "etsysTacacsClientServerStatus": etsysTacacsClientServerStatus,
       "etsysTacacsClientConformance": etsysTacacsClientConformance,
       "etsysTacacsClientCompliances": etsysTacacsClientCompliances,
       "etsysTacacsClientCompliance": etsysTacacsClientCompliance,
       "etsysTacacsClientGroups": etsysTacacsClientGroups,
       "etsysTacacsClientSessionGroup": etsysTacacsClientSessionGroup,
       "etsysTacacsClientCmdAuthGroup": etsysTacacsClientCmdAuthGroup,
       "etsysTacacsClientCmdAcctGroup": etsysTacacsClientCmdAcctGroup,
       "etsysTacacsClientSesnAuthGroup": etsysTacacsClientSesnAuthGroup}
)
