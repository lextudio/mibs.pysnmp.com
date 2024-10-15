# SNMP MIB module (ENTERASYS-MULTI-AUTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-MULTI-AUTH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:15 2024
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

(StationAddress,
 StationAddressType) = mibBuilder.importSymbols(
    "ENTERASYS-UPN-TC-MIB",
    "StationAddress",
    "StationAddressType")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

etsysMultiAuthMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46)
)
etsysMultiAuthMIB.setRevisions(
        ("2008-02-05 18:40",
         "2006-03-23 13:32",
         "2006-02-03 19:15",
         "2005-04-06 18:10",
         "2004-08-30 13:43",
         "2004-07-20 19:43",
         "2004-03-10 13:56")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EtsysMultiAuthTypes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cep", 4),
          ("ieee8021x", 1),
          ("macAuth", 3),
          ("pwa", 2),
          ("radiusSnooping", 5))
    )



class EtsysMultiAuthTypePrecedence(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d "
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class EtsysMultiAuthStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("authFailed", 2),
          ("authInProgress", 3),
          ("authServerTimeout", 4),
          ("authSuccess", 1),
          ("authTerminated", 5))
    )



# MIB Managed Objects in the order of their OIDs

_EtsysMultiAuthObjects_ObjectIdentity = ObjectIdentity
etsysMultiAuthObjects = _EtsysMultiAuthObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1)
)
_EtsysMultiAuthNotification_ObjectIdentity = ObjectIdentity
etsysMultiAuthNotification = _EtsysMultiAuthNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 0)
)
_EtsysMultiAuthSystem_ObjectIdentity = ObjectIdentity
etsysMultiAuthSystem = _EtsysMultiAuthSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1)
)


class _EtsysMultiAuthSystemSupportedTypes_Type(Bits):
    """Custom type etsysMultiAuthSystemSupportedTypes based on Bits"""
    namedValues = NamedValues(
        *(("cep", 3),
          ("ieee8021x", 0),
          ("macAuth", 2),
          ("pwa", 1),
          ("radiusSnooping", 4))
    )

_EtsysMultiAuthSystemSupportedTypes_Type.__name__ = "Bits"
_EtsysMultiAuthSystemSupportedTypes_Object = MibScalar
etsysMultiAuthSystemSupportedTypes = _EtsysMultiAuthSystemSupportedTypes_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 1),
    _EtsysMultiAuthSystemSupportedTypes_Type()
)
etsysMultiAuthSystemSupportedTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSystemSupportedTypes.setStatus("current")
_EtsysMultiAuthSystemMaxNumUsers_Type = Unsigned32
_EtsysMultiAuthSystemMaxNumUsers_Object = MibScalar
etsysMultiAuthSystemMaxNumUsers = _EtsysMultiAuthSystemMaxNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 2),
    _EtsysMultiAuthSystemMaxNumUsers_Type()
)
etsysMultiAuthSystemMaxNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSystemMaxNumUsers.setStatus("current")
_EtsysMultiAuthSystemCurrentNumUsers_Type = Gauge32
_EtsysMultiAuthSystemCurrentNumUsers_Object = MibScalar
etsysMultiAuthSystemCurrentNumUsers = _EtsysMultiAuthSystemCurrentNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 3),
    _EtsysMultiAuthSystemCurrentNumUsers_Type()
)
etsysMultiAuthSystemCurrentNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSystemCurrentNumUsers.setStatus("current")


class _EtsysMultiAuthSystemMode_Type(Integer32):
    """Custom type etsysMultiAuthSystemMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("etsysMultiAuth", 2),
          ("strictIeee8021x", 1))
    )


_EtsysMultiAuthSystemMode_Type.__name__ = "Integer32"
_EtsysMultiAuthSystemMode_Object = MibScalar
etsysMultiAuthSystemMode = _EtsysMultiAuthSystemMode_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 4),
    _EtsysMultiAuthSystemMode_Type()
)
etsysMultiAuthSystemMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMultiAuthSystemMode.setStatus("current")


class _EtsysMultiAuthSystemDefaultPrecedence_Type(EtsysMultiAuthTypePrecedence):
    """Custom type etsysMultiAuthSystemDefaultPrecedence based on EtsysMultiAuthTypePrecedence"""
    defaultHexValue = "0102030405"


_EtsysMultiAuthSystemDefaultPrecedence_Object = MibScalar
etsysMultiAuthSystemDefaultPrecedence = _EtsysMultiAuthSystemDefaultPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 5),
    _EtsysMultiAuthSystemDefaultPrecedence_Type()
)
etsysMultiAuthSystemDefaultPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSystemDefaultPrecedence.setStatus("current")


class _EtsysMultiAuthSystemAdminPrecedence_Type(EtsysMultiAuthTypePrecedence):
    """Custom type etsysMultiAuthSystemAdminPrecedence based on EtsysMultiAuthTypePrecedence"""
    defaultHexValue = ""


_EtsysMultiAuthSystemAdminPrecedence_Object = MibScalar
etsysMultiAuthSystemAdminPrecedence = _EtsysMultiAuthSystemAdminPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 6),
    _EtsysMultiAuthSystemAdminPrecedence_Type()
)
etsysMultiAuthSystemAdminPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMultiAuthSystemAdminPrecedence.setStatus("current")
_EtsysMultiAuthSystemOperPrecedence_Type = EtsysMultiAuthTypePrecedence
_EtsysMultiAuthSystemOperPrecedence_Object = MibScalar
etsysMultiAuthSystemOperPrecedence = _EtsysMultiAuthSystemOperPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 7),
    _EtsysMultiAuthSystemOperPrecedence_Type()
)
etsysMultiAuthSystemOperPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSystemOperPrecedence.setStatus("current")
_EtsysMultiAuthTypePropertiesTable_Object = MibTable
etsysMultiAuthTypePropertiesTable = _EtsysMultiAuthTypePropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 8)
)
if mibBuilder.loadTexts:
    etsysMultiAuthTypePropertiesTable.setStatus("current")
_EtsysMultiAuthTypePropertiesEntry_Object = MibTableRow
etsysMultiAuthTypePropertiesEntry = _EtsysMultiAuthTypePropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 8, 1)
)
etsysMultiAuthTypePropertiesEntry.setIndexNames(
    (0, "ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthType"),
)
if mibBuilder.loadTexts:
    etsysMultiAuthTypePropertiesEntry.setStatus("current")
_EtsysMultiAuthType_Type = EtsysMultiAuthTypes
_EtsysMultiAuthType_Object = MibTableColumn
etsysMultiAuthType = _EtsysMultiAuthType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 8, 1, 1),
    _EtsysMultiAuthType_Type()
)
etsysMultiAuthType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysMultiAuthType.setStatus("current")


class _EtsysMultiAuthSessionTimeout_Type(Unsigned32):
    """Custom type etsysMultiAuthSessionTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysMultiAuthSessionTimeout_Type.__name__ = "Unsigned32"
_EtsysMultiAuthSessionTimeout_Object = MibTableColumn
etsysMultiAuthSessionTimeout = _EtsysMultiAuthSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 8, 1, 2),
    _EtsysMultiAuthSessionTimeout_Type()
)
etsysMultiAuthSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionTimeout.setUnits("seconds")


class _EtsysMultiAuthIdleTimeout_Type(Unsigned32):
    """Custom type etsysMultiAuthIdleTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysMultiAuthIdleTimeout_Type.__name__ = "Unsigned32"
_EtsysMultiAuthIdleTimeout_Object = MibTableColumn
etsysMultiAuthIdleTimeout = _EtsysMultiAuthIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 8, 1, 3),
    _EtsysMultiAuthIdleTimeout_Type()
)
etsysMultiAuthIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMultiAuthIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysMultiAuthIdleTimeout.setUnits("seconds")
_EtsysMultiAuthCurrentNumUsers_Type = Gauge32
_EtsysMultiAuthCurrentNumUsers_Object = MibTableColumn
etsysMultiAuthCurrentNumUsers = _EtsysMultiAuthCurrentNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 8, 1, 4),
    _EtsysMultiAuthCurrentNumUsers_Type()
)
etsysMultiAuthCurrentNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthCurrentNumUsers.setStatus("current")


class _EtsysMultiAuthSystemMaxNumUsersReachedTrapEnable_Type(EnabledStatus):
    """Custom type etsysMultiAuthSystemMaxNumUsersReachedTrapEnable based on EnabledStatus"""


_EtsysMultiAuthSystemMaxNumUsersReachedTrapEnable_Object = MibScalar
etsysMultiAuthSystemMaxNumUsersReachedTrapEnable = _EtsysMultiAuthSystemMaxNumUsersReachedTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 1, 9),
    _EtsysMultiAuthSystemMaxNumUsersReachedTrapEnable_Type()
)
etsysMultiAuthSystemMaxNumUsersReachedTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMultiAuthSystemMaxNumUsersReachedTrapEnable.setStatus("current")
_EtsysMultiAuthPort_ObjectIdentity = ObjectIdentity
etsysMultiAuthPort = _EtsysMultiAuthPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 2)
)
_EtsysMultiAuthPortTable_Object = MibTable
etsysMultiAuthPortTable = _EtsysMultiAuthPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysMultiAuthPortTable.setStatus("current")
_EtsysMultiAuthPortEntry_Object = MibTableRow
etsysMultiAuthPortEntry = _EtsysMultiAuthPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 2, 1, 1)
)
etsysMultiAuthPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysMultiAuthPortEntry.setStatus("current")


class _EtsysMultiAuthPortMode_Type(Integer32):
    """Custom type etsysMultiAuthPortMode based on Integer32"""
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
        *(("authOptional", 3),
          ("authRequired", 4),
          ("forceAuthorized", 2),
          ("forceUnauthorized", 1))
    )


_EtsysMultiAuthPortMode_Type.__name__ = "Integer32"
_EtsysMultiAuthPortMode_Object = MibTableColumn
etsysMultiAuthPortMode = _EtsysMultiAuthPortMode_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 2, 1, 1, 1),
    _EtsysMultiAuthPortMode_Type()
)
etsysMultiAuthPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMultiAuthPortMode.setStatus("current")
_EtsysMultiAuthPortMaxNumUsers_Type = Unsigned32
_EtsysMultiAuthPortMaxNumUsers_Object = MibTableColumn
etsysMultiAuthPortMaxNumUsers = _EtsysMultiAuthPortMaxNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 2, 1, 1, 2),
    _EtsysMultiAuthPortMaxNumUsers_Type()
)
etsysMultiAuthPortMaxNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthPortMaxNumUsers.setStatus("current")
_EtsysMultiAuthPortNumUsersAllowed_Type = Unsigned32
_EtsysMultiAuthPortNumUsersAllowed_Object = MibTableColumn
etsysMultiAuthPortNumUsersAllowed = _EtsysMultiAuthPortNumUsersAllowed_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 2, 1, 1, 3),
    _EtsysMultiAuthPortNumUsersAllowed_Type()
)
etsysMultiAuthPortNumUsersAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMultiAuthPortNumUsersAllowed.setStatus("current")
_EtsysMultiAuthPortCurrentNumUsers_Type = Gauge32
_EtsysMultiAuthPortCurrentNumUsers_Object = MibTableColumn
etsysMultiAuthPortCurrentNumUsers = _EtsysMultiAuthPortCurrentNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 2, 1, 1, 4),
    _EtsysMultiAuthPortCurrentNumUsers_Type()
)
etsysMultiAuthPortCurrentNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthPortCurrentNumUsers.setStatus("current")


class _EtsysMultiAuthPortClearUsers_Type(TruthValue):
    """Custom type etsysMultiAuthPortClearUsers based on TruthValue"""


_EtsysMultiAuthPortClearUsers_Object = MibTableColumn
etsysMultiAuthPortClearUsers = _EtsysMultiAuthPortClearUsers_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 2, 1, 1, 5),
    _EtsysMultiAuthPortClearUsers_Type()
)
etsysMultiAuthPortClearUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMultiAuthPortClearUsers.setStatus("current")


class _EtsysMultiAuthPortTrapEnable_Type(Bits):
    """Custom type etsysMultiAuthPortTrapEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("authFailedTrap", 1),
          ("authSuccessTrap", 0),
          ("authTerminatedTrap", 2),
          ("maxNumUsersReachedTrap", 3))
    )

_EtsysMultiAuthPortTrapEnable_Type.__name__ = "Bits"
_EtsysMultiAuthPortTrapEnable_Object = MibTableColumn
etsysMultiAuthPortTrapEnable = _EtsysMultiAuthPortTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 2, 1, 1, 6),
    _EtsysMultiAuthPortTrapEnable_Type()
)
etsysMultiAuthPortTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMultiAuthPortTrapEnable.setStatus("current")
_EtsysMultiAuthPortTypeTable_Object = MibTable
etsysMultiAuthPortTypeTable = _EtsysMultiAuthPortTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 2, 2)
)
if mibBuilder.loadTexts:
    etsysMultiAuthPortTypeTable.setStatus("current")
_EtsysMultiAuthPortTypeEntry_Object = MibTableRow
etsysMultiAuthPortTypeEntry = _EtsysMultiAuthPortTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 2, 2, 1)
)
etsysMultiAuthPortTypeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthType"),
)
if mibBuilder.loadTexts:
    etsysMultiAuthPortTypeEntry.setStatus("current")
_EtsysMultiAuthPortTypeCurrentNumUsers_Type = Gauge32
_EtsysMultiAuthPortTypeCurrentNumUsers_Object = MibTableColumn
etsysMultiAuthPortTypeCurrentNumUsers = _EtsysMultiAuthPortTypeCurrentNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 2, 2, 1, 1),
    _EtsysMultiAuthPortTypeCurrentNumUsers_Type()
)
etsysMultiAuthPortTypeCurrentNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthPortTypeCurrentNumUsers.setStatus("current")
_EtsysMultiAuthStation_ObjectIdentity = ObjectIdentity
etsysMultiAuthStation = _EtsysMultiAuthStation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 3)
)
_EtsysMultiAuthStationTable_Object = MibTable
etsysMultiAuthStationTable = _EtsysMultiAuthStationTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 3, 1)
)
if mibBuilder.loadTexts:
    etsysMultiAuthStationTable.setStatus("current")
_EtsysMultiAuthStationEntry_Object = MibTableRow
etsysMultiAuthStationEntry = _EtsysMultiAuthStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 3, 1, 1)
)
etsysMultiAuthStationEntry.setIndexNames(
    (0, "ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationAddrType"),
    (0, "ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationAddr"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysMultiAuthStationEntry.setStatus("current")
_EtsysMultiAuthStationAddrType_Type = StationAddressType
_EtsysMultiAuthStationAddrType_Object = MibTableColumn
etsysMultiAuthStationAddrType = _EtsysMultiAuthStationAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 3, 1, 1, 1),
    _EtsysMultiAuthStationAddrType_Type()
)
etsysMultiAuthStationAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysMultiAuthStationAddrType.setStatus("current")
_EtsysMultiAuthStationAddr_Type = StationAddress
_EtsysMultiAuthStationAddr_Object = MibTableColumn
etsysMultiAuthStationAddr = _EtsysMultiAuthStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 3, 1, 1, 2),
    _EtsysMultiAuthStationAddr_Type()
)
etsysMultiAuthStationAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysMultiAuthStationAddr.setStatus("current")


class _EtsysMultiAuthStationClearUsers_Type(TruthValue):
    """Custom type etsysMultiAuthStationClearUsers based on TruthValue"""


_EtsysMultiAuthStationClearUsers_Object = MibTableColumn
etsysMultiAuthStationClearUsers = _EtsysMultiAuthStationClearUsers_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 3, 1, 1, 3),
    _EtsysMultiAuthStationClearUsers_Type()
)
etsysMultiAuthStationClearUsers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMultiAuthStationClearUsers.setStatus("current")
_EtsysMultiAuthSession_ObjectIdentity = ObjectIdentity
etsysMultiAuthSession = _EtsysMultiAuthSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4)
)
_EtsysMultiAuthSessionStationTable_Object = MibTable
etsysMultiAuthSessionStationTable = _EtsysMultiAuthSessionStationTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1)
)
if mibBuilder.loadTexts:
    etsysMultiAuthSessionStationTable.setStatus("current")
_EtsysMultiAuthSessionStationEntry_Object = MibTableRow
etsysMultiAuthSessionStationEntry = _EtsysMultiAuthSessionStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1)
)
etsysMultiAuthSessionStationEntry.setIndexNames(
    (0, "ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationAddrType"),
    (0, "ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationAddr"),
    (0, "IF-MIB", "ifIndex"),
    (0, "ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAgentType"),
)
if mibBuilder.loadTexts:
    etsysMultiAuthSessionStationEntry.setStatus("current")
_EtsysMultiAuthSessionAgentType_Type = EtsysMultiAuthTypes
_EtsysMultiAuthSessionAgentType_Object = MibTableColumn
etsysMultiAuthSessionAgentType = _EtsysMultiAuthSessionAgentType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1, 1),
    _EtsysMultiAuthSessionAgentType_Type()
)
etsysMultiAuthSessionAgentType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionAgentType.setStatus("current")
_EtsysMultiAuthSessionStationAuthStatus_Type = EtsysMultiAuthStatus
_EtsysMultiAuthSessionStationAuthStatus_Object = MibTableColumn
etsysMultiAuthSessionStationAuthStatus = _EtsysMultiAuthSessionStationAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1, 2),
    _EtsysMultiAuthSessionStationAuthStatus_Type()
)
etsysMultiAuthSessionStationAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionStationAuthStatus.setStatus("current")
_EtsysMultiAuthSessionAuthAttemptTime_Type = TimeStamp
_EtsysMultiAuthSessionAuthAttemptTime_Object = MibTableColumn
etsysMultiAuthSessionAuthAttemptTime = _EtsysMultiAuthSessionAuthAttemptTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1, 3),
    _EtsysMultiAuthSessionAuthAttemptTime_Type()
)
etsysMultiAuthSessionAuthAttemptTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionAuthAttemptTime.setStatus("current")


class _EtsysMultiAuthSessionAuthServerType_Type(Integer32):
    """Custom type etsysMultiAuthSessionAuthServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("radius", 1))
    )


_EtsysMultiAuthSessionAuthServerType_Type.__name__ = "Integer32"
_EtsysMultiAuthSessionAuthServerType_Object = MibTableColumn
etsysMultiAuthSessionAuthServerType = _EtsysMultiAuthSessionAuthServerType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1, 4),
    _EtsysMultiAuthSessionAuthServerType_Type()
)
etsysMultiAuthSessionAuthServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionAuthServerType.setStatus("current")
_EtsysMultiAuthSessionAuthServerAddrType_Type = InetAddressType
_EtsysMultiAuthSessionAuthServerAddrType_Object = MibTableColumn
etsysMultiAuthSessionAuthServerAddrType = _EtsysMultiAuthSessionAuthServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1, 5),
    _EtsysMultiAuthSessionAuthServerAddrType_Type()
)
etsysMultiAuthSessionAuthServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionAuthServerAddrType.setStatus("current")
_EtsysMultiAuthSessionAuthServerAddr_Type = InetAddress
_EtsysMultiAuthSessionAuthServerAddr_Object = MibTableColumn
etsysMultiAuthSessionAuthServerAddr = _EtsysMultiAuthSessionAuthServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1, 6),
    _EtsysMultiAuthSessionAuthServerAddr_Type()
)
etsysMultiAuthSessionAuthServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionAuthServerAddr.setStatus("current")


class _EtsysMultiAuthSessionPolicyIndex_Type(Integer32):
    """Custom type etsysMultiAuthSessionPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysMultiAuthSessionPolicyIndex_Type.__name__ = "Integer32"
_EtsysMultiAuthSessionPolicyIndex_Object = MibTableColumn
etsysMultiAuthSessionPolicyIndex = _EtsysMultiAuthSessionPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1, 7),
    _EtsysMultiAuthSessionPolicyIndex_Type()
)
etsysMultiAuthSessionPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionPolicyIndex.setStatus("current")
_EtsysMultiAuthSessionIsApplied_Type = TruthValue
_EtsysMultiAuthSessionIsApplied_Object = MibTableColumn
etsysMultiAuthSessionIsApplied = _EtsysMultiAuthSessionIsApplied_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1, 8),
    _EtsysMultiAuthSessionIsApplied_Type()
)
etsysMultiAuthSessionIsApplied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionIsApplied.setStatus("current")


class _EtsysMultiAuthSessionTerminationTime_Type(DateAndTime):
    """Custom type etsysMultiAuthSessionTerminationTime based on DateAndTime"""
    defaultHexValue = "00000000"

    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_EtsysMultiAuthSessionTerminationTime_Type.__name__ = "DateAndTime"
_EtsysMultiAuthSessionTerminationTime_Object = MibTableColumn
etsysMultiAuthSessionTerminationTime = _EtsysMultiAuthSessionTerminationTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1, 9),
    _EtsysMultiAuthSessionTerminationTime_Type()
)
etsysMultiAuthSessionTerminationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionTerminationTime.setStatus("current")


class _EtsysMultiAuthSessionSessionTimeout_Type(Unsigned32):
    """Custom type etsysMultiAuthSessionSessionTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysMultiAuthSessionSessionTimeout_Type.__name__ = "Unsigned32"
_EtsysMultiAuthSessionSessionTimeout_Object = MibTableColumn
etsysMultiAuthSessionSessionTimeout = _EtsysMultiAuthSessionSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1, 10),
    _EtsysMultiAuthSessionSessionTimeout_Type()
)
etsysMultiAuthSessionSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionSessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionSessionTimeout.setUnits("seconds")


class _EtsysMultiAuthSessionIdleTimeout_Type(Unsigned32):
    """Custom type etsysMultiAuthSessionIdleTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_EtsysMultiAuthSessionIdleTimeout_Type.__name__ = "Unsigned32"
_EtsysMultiAuthSessionIdleTimeout_Object = MibTableColumn
etsysMultiAuthSessionIdleTimeout = _EtsysMultiAuthSessionIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1, 11),
    _EtsysMultiAuthSessionIdleTimeout_Type()
)
etsysMultiAuthSessionIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionIdleTimeout.setUnits("seconds")
_EtsysMultiAuthSessionDuration_Type = Gauge32
_EtsysMultiAuthSessionDuration_Object = MibTableColumn
etsysMultiAuthSessionDuration = _EtsysMultiAuthSessionDuration_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1, 12),
    _EtsysMultiAuthSessionDuration_Type()
)
etsysMultiAuthSessionDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionDuration.setStatus("current")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionDuration.setUnits("seconds")
_EtsysMultiAuthSessionIdleTime_Type = Gauge32
_EtsysMultiAuthSessionIdleTime_Object = MibTableColumn
etsysMultiAuthSessionIdleTime = _EtsysMultiAuthSessionIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1, 13),
    _EtsysMultiAuthSessionIdleTime_Type()
)
etsysMultiAuthSessionIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionIdleTime.setUnits("seconds")


class _EtsysMultiAuthSessionVlanTunnelAttribute_Type(Integer32):
    """Custom type etsysMultiAuthSessionVlanTunnelAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4095, 4095),
    )


_EtsysMultiAuthSessionVlanTunnelAttribute_Type.__name__ = "Integer32"
_EtsysMultiAuthSessionVlanTunnelAttribute_Object = MibTableColumn
etsysMultiAuthSessionVlanTunnelAttribute = _EtsysMultiAuthSessionVlanTunnelAttribute_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 1, 1, 14),
    _EtsysMultiAuthSessionVlanTunnelAttribute_Type()
)
etsysMultiAuthSessionVlanTunnelAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionVlanTunnelAttribute.setStatus("current")
_EtsysMultiAuthSessionPortTable_Object = MibTable
etsysMultiAuthSessionPortTable = _EtsysMultiAuthSessionPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 2)
)
if mibBuilder.loadTexts:
    etsysMultiAuthSessionPortTable.setStatus("current")
_EtsysMultiAuthSessionPortEntry_Object = MibTableRow
etsysMultiAuthSessionPortEntry = _EtsysMultiAuthSessionPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 2, 1)
)
etsysMultiAuthSessionPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationAddrType"),
    (0, "ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationAddr"),
    (0, "ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAgentType"),
)
if mibBuilder.loadTexts:
    etsysMultiAuthSessionPortEntry.setStatus("current")
_EtsysMultiAuthSessionPortAuthStatus_Type = EtsysMultiAuthStatus
_EtsysMultiAuthSessionPortAuthStatus_Object = MibTableColumn
etsysMultiAuthSessionPortAuthStatus = _EtsysMultiAuthSessionPortAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 4, 2, 1, 1),
    _EtsysMultiAuthSessionPortAuthStatus_Type()
)
etsysMultiAuthSessionPortAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthSessionPortAuthStatus.setStatus("current")
_EtsysMultiAuthModule_ObjectIdentity = ObjectIdentity
etsysMultiAuthModule = _EtsysMultiAuthModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 5)
)
_EtsysMultiAuthModuleTable_Object = MibTable
etsysMultiAuthModuleTable = _EtsysMultiAuthModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 5, 1)
)
if mibBuilder.loadTexts:
    etsysMultiAuthModuleTable.setStatus("current")
_EtsysMultiAuthModuleEntry_Object = MibTableRow
etsysMultiAuthModuleEntry = _EtsysMultiAuthModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 5, 1, 1)
)
etsysMultiAuthModuleEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    etsysMultiAuthModuleEntry.setStatus("current")
_EtsysMultiAuthModuleMaxNumUsers_Type = Unsigned32
_EtsysMultiAuthModuleMaxNumUsers_Object = MibTableColumn
etsysMultiAuthModuleMaxNumUsers = _EtsysMultiAuthModuleMaxNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 5, 1, 1, 1),
    _EtsysMultiAuthModuleMaxNumUsers_Type()
)
etsysMultiAuthModuleMaxNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthModuleMaxNumUsers.setStatus("current")
_EtsysMultiAuthModuleCurrentNumUsers_Type = Gauge32
_EtsysMultiAuthModuleCurrentNumUsers_Object = MibTableColumn
etsysMultiAuthModuleCurrentNumUsers = _EtsysMultiAuthModuleCurrentNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 5, 1, 1, 2),
    _EtsysMultiAuthModuleCurrentNumUsers_Type()
)
etsysMultiAuthModuleCurrentNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMultiAuthModuleCurrentNumUsers.setStatus("current")


class _EtsysMultiAuthModuleMaxNumUsersReachedTrapEnable_Type(EnabledStatus):
    """Custom type etsysMultiAuthModuleMaxNumUsersReachedTrapEnable based on EnabledStatus"""


_EtsysMultiAuthModuleMaxNumUsersReachedTrapEnable_Object = MibScalar
etsysMultiAuthModuleMaxNumUsersReachedTrapEnable = _EtsysMultiAuthModuleMaxNumUsersReachedTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 5, 2),
    _EtsysMultiAuthModuleMaxNumUsersReachedTrapEnable_Type()
)
etsysMultiAuthModuleMaxNumUsersReachedTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMultiAuthModuleMaxNumUsersReachedTrapEnable.setStatus("current")
_EtsysMultiAuthConformance_ObjectIdentity = ObjectIdentity
etsysMultiAuthConformance = _EtsysMultiAuthConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2)
)
_EtsysMultiAuthGroups_ObjectIdentity = ObjectIdentity
etsysMultiAuthGroups = _EtsysMultiAuthGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1)
)
_EtsysMultiAuthCompliances_ObjectIdentity = ObjectIdentity
etsysMultiAuthCompliances = _EtsysMultiAuthCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 2)
)

# Managed Objects groups

etsysMultiAuthSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 1)
)
etsysMultiAuthSystemGroup.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemSupportedTypes"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemMaxNumUsers"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemCurrentNumUsers"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemMode"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemDefaultPrecedence"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemAdminPrecedence"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemOperPrecedence"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthSystemGroup.setStatus("current")

etsysMultiAuthPortBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 2)
)
etsysMultiAuthPortBaseGroup.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthPortMode"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthPortMaxNumUsers"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthPortNumUsersAllowed"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthPortCurrentNumUsers"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthPortClearUsers"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthPortBaseGroup.setStatus("current")

etsysMultiAuthPortTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 3)
)
etsysMultiAuthPortTrapGroup.setObjects(
    ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthPortTrapEnable")
)
if mibBuilder.loadTexts:
    etsysMultiAuthPortTrapGroup.setStatus("current")

etsysMultiAuthStationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 4)
)
etsysMultiAuthStationGroup.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationAddrType"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationAddr"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationClearUsers"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthStationGroup.setStatus("current")

etsysMultiAuthSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 5)
)
etsysMultiAuthSessionGroup.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAgentType"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionStationAuthStatus"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAuthAttemptTime"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAuthServerType"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAuthServerAddrType"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAuthServerAddr"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionPolicyIndex"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionIsApplied"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionPortAuthStatus"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthSessionGroup.setStatus("deprecated")

etsysMultiAuthModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 7)
)
etsysMultiAuthModuleGroup.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthModuleMaxNumUsers"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthModuleCurrentNumUsers"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthModuleGroup.setStatus("current")

etsysMultiAuthSessionGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 8)
)
etsysMultiAuthSessionGroup2.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAgentType"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionStationAuthStatus"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAuthAttemptTime"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAuthServerType"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAuthServerAddrType"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAuthServerAddr"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionPolicyIndex"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionIsApplied"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionTerminationTime"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionPortAuthStatus"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthSessionGroup2.setStatus("current")

etsysMultiAuthTimeoutGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 9)
)
etsysMultiAuthTimeoutGroup.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthType"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionTimeout"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthIdleTimeout"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionSessionTimeout"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionIdleTimeout"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionDuration"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionIdleTime"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthTimeoutGroup.setStatus("current")

etsysMultiAuthCurrentNumUsersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 10)
)
etsysMultiAuthCurrentNumUsersGroup.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthCurrentNumUsers"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthPortTypeCurrentNumUsers"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthCurrentNumUsersGroup.setStatus("current")

etsysMultiAuthModuleTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 11)
)
etsysMultiAuthModuleTrapGroup.setObjects(
    ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthModuleMaxNumUsersReachedTrapEnable")
)
if mibBuilder.loadTexts:
    etsysMultiAuthModuleTrapGroup.setStatus("current")

etsysMultiAuthSystemTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 12)
)
etsysMultiAuthSystemTrapGroup.setObjects(
    ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemMaxNumUsersReachedTrapEnable")
)
if mibBuilder.loadTexts:
    etsysMultiAuthSystemTrapGroup.setStatus("current")

etsysMultiAuthTunnelAttributeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 15)
)
etsysMultiAuthTunnelAttributeGroup.setObjects(
    ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionVlanTunnelAttribute")
)
if mibBuilder.loadTexts:
    etsysMultiAuthTunnelAttributeGroup.setStatus("current")


# Notification objects

etsysMultiAuthSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 0, 1)
)
etsysMultiAuthSuccess.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationAddrType"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationAddr"),
        ("IF-MIB", "ifIndex"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAgentType"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthSuccess.setStatus(
        "current"
    )

etsysMultiAuthFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 0, 2)
)
etsysMultiAuthFailed.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationAddrType"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationAddr"),
        ("IF-MIB", "ifIndex"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAgentType"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthFailed.setStatus(
        "current"
    )

etsysMultiAuthTerminated = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 0, 3)
)
etsysMultiAuthTerminated.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationAddrType"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthStationAddr"),
        ("IF-MIB", "ifIndex"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSessionAgentType"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthTerminated.setStatus(
        "current"
    )

etsysMultiAuthMaxNumUsersReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 0, 4)
)
etsysMultiAuthMaxNumUsersReached.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    etsysMultiAuthMaxNumUsersReached.setStatus(
        "current"
    )

etsysMultiAuthModuleMaxNumUsersReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 0, 5)
)
etsysMultiAuthModuleMaxNumUsersReached.setObjects(
    ("ENTITY-MIB", "entPhysicalIndex")
)
if mibBuilder.loadTexts:
    etsysMultiAuthModuleMaxNumUsersReached.setStatus(
        "current"
    )

etsysMultiAuthSystemMaxNumUsersReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 1, 0, 6)
)
if mibBuilder.loadTexts:
    etsysMultiAuthSystemMaxNumUsersReached.setStatus(
        "current"
    )


# Notifications groups

etsysMultiAuthNotificationPortGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 6)
)
etsysMultiAuthNotificationPortGroup.setObjects(
      *(("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSuccess"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthFailed"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthTerminated"),
        ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthMaxNumUsersReached"))
)
if mibBuilder.loadTexts:
    etsysMultiAuthNotificationPortGroup.setStatus(
        "current"
    )

etsysMultiAuthNotificationModuleGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 13)
)
etsysMultiAuthNotificationModuleGroup.setObjects(
    ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthModuleMaxNumUsersReached")
)
if mibBuilder.loadTexts:
    etsysMultiAuthNotificationModuleGroup.setStatus(
        "current"
    )

etsysMultiAuthNotificationSystemGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 1, 14)
)
etsysMultiAuthNotificationSystemGroup.setObjects(
    ("ENTERASYS-MULTI-AUTH-MIB", "etsysMultiAuthSystemMaxNumUsersReached")
)
if mibBuilder.loadTexts:
    etsysMultiAuthNotificationSystemGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

etsysMultiAuthCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysMultiAuthCompliance.setStatus(
        "deprecated"
    )

etsysMultiAuthCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 2, 2)
)
if mibBuilder.loadTexts:
    etsysMultiAuthCompliance2.setStatus(
        "deprecated"
    )

etsysMultiAuthCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 2, 3)
)
if mibBuilder.loadTexts:
    etsysMultiAuthCompliance3.setStatus(
        "deprecated"
    )

etsysMultiAuthTimeoutCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 2, 4)
)
if mibBuilder.loadTexts:
    etsysMultiAuthTimeoutCompliance.setStatus(
        "current"
    )

etsysMultiAuthCurrentNumUserCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 2, 5)
)
if mibBuilder.loadTexts:
    etsysMultiAuthCurrentNumUserCompliance.setStatus(
        "current"
    )

etsysMultiAuthCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 2, 6)
)
if mibBuilder.loadTexts:
    etsysMultiAuthCompliance4.setStatus(
        "current"
    )

etsysMultiTunnelAttributeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 46, 2, 2, 7)
)
if mibBuilder.loadTexts:
    etsysMultiTunnelAttributeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-MULTI-AUTH-MIB",
    **{"EtsysMultiAuthTypes": EtsysMultiAuthTypes,
       "EtsysMultiAuthTypePrecedence": EtsysMultiAuthTypePrecedence,
       "EtsysMultiAuthStatus": EtsysMultiAuthStatus,
       "etsysMultiAuthMIB": etsysMultiAuthMIB,
       "etsysMultiAuthObjects": etsysMultiAuthObjects,
       "etsysMultiAuthNotification": etsysMultiAuthNotification,
       "etsysMultiAuthSuccess": etsysMultiAuthSuccess,
       "etsysMultiAuthFailed": etsysMultiAuthFailed,
       "etsysMultiAuthTerminated": etsysMultiAuthTerminated,
       "etsysMultiAuthMaxNumUsersReached": etsysMultiAuthMaxNumUsersReached,
       "etsysMultiAuthModuleMaxNumUsersReached": etsysMultiAuthModuleMaxNumUsersReached,
       "etsysMultiAuthSystemMaxNumUsersReached": etsysMultiAuthSystemMaxNumUsersReached,
       "etsysMultiAuthSystem": etsysMultiAuthSystem,
       "etsysMultiAuthSystemSupportedTypes": etsysMultiAuthSystemSupportedTypes,
       "etsysMultiAuthSystemMaxNumUsers": etsysMultiAuthSystemMaxNumUsers,
       "etsysMultiAuthSystemCurrentNumUsers": etsysMultiAuthSystemCurrentNumUsers,
       "etsysMultiAuthSystemMode": etsysMultiAuthSystemMode,
       "etsysMultiAuthSystemDefaultPrecedence": etsysMultiAuthSystemDefaultPrecedence,
       "etsysMultiAuthSystemAdminPrecedence": etsysMultiAuthSystemAdminPrecedence,
       "etsysMultiAuthSystemOperPrecedence": etsysMultiAuthSystemOperPrecedence,
       "etsysMultiAuthTypePropertiesTable": etsysMultiAuthTypePropertiesTable,
       "etsysMultiAuthTypePropertiesEntry": etsysMultiAuthTypePropertiesEntry,
       "etsysMultiAuthType": etsysMultiAuthType,
       "etsysMultiAuthSessionTimeout": etsysMultiAuthSessionTimeout,
       "etsysMultiAuthIdleTimeout": etsysMultiAuthIdleTimeout,
       "etsysMultiAuthCurrentNumUsers": etsysMultiAuthCurrentNumUsers,
       "etsysMultiAuthSystemMaxNumUsersReachedTrapEnable": etsysMultiAuthSystemMaxNumUsersReachedTrapEnable,
       "etsysMultiAuthPort": etsysMultiAuthPort,
       "etsysMultiAuthPortTable": etsysMultiAuthPortTable,
       "etsysMultiAuthPortEntry": etsysMultiAuthPortEntry,
       "etsysMultiAuthPortMode": etsysMultiAuthPortMode,
       "etsysMultiAuthPortMaxNumUsers": etsysMultiAuthPortMaxNumUsers,
       "etsysMultiAuthPortNumUsersAllowed": etsysMultiAuthPortNumUsersAllowed,
       "etsysMultiAuthPortCurrentNumUsers": etsysMultiAuthPortCurrentNumUsers,
       "etsysMultiAuthPortClearUsers": etsysMultiAuthPortClearUsers,
       "etsysMultiAuthPortTrapEnable": etsysMultiAuthPortTrapEnable,
       "etsysMultiAuthPortTypeTable": etsysMultiAuthPortTypeTable,
       "etsysMultiAuthPortTypeEntry": etsysMultiAuthPortTypeEntry,
       "etsysMultiAuthPortTypeCurrentNumUsers": etsysMultiAuthPortTypeCurrentNumUsers,
       "etsysMultiAuthStation": etsysMultiAuthStation,
       "etsysMultiAuthStationTable": etsysMultiAuthStationTable,
       "etsysMultiAuthStationEntry": etsysMultiAuthStationEntry,
       "etsysMultiAuthStationAddrType": etsysMultiAuthStationAddrType,
       "etsysMultiAuthStationAddr": etsysMultiAuthStationAddr,
       "etsysMultiAuthStationClearUsers": etsysMultiAuthStationClearUsers,
       "etsysMultiAuthSession": etsysMultiAuthSession,
       "etsysMultiAuthSessionStationTable": etsysMultiAuthSessionStationTable,
       "etsysMultiAuthSessionStationEntry": etsysMultiAuthSessionStationEntry,
       "etsysMultiAuthSessionAgentType": etsysMultiAuthSessionAgentType,
       "etsysMultiAuthSessionStationAuthStatus": etsysMultiAuthSessionStationAuthStatus,
       "etsysMultiAuthSessionAuthAttemptTime": etsysMultiAuthSessionAuthAttemptTime,
       "etsysMultiAuthSessionAuthServerType": etsysMultiAuthSessionAuthServerType,
       "etsysMultiAuthSessionAuthServerAddrType": etsysMultiAuthSessionAuthServerAddrType,
       "etsysMultiAuthSessionAuthServerAddr": etsysMultiAuthSessionAuthServerAddr,
       "etsysMultiAuthSessionPolicyIndex": etsysMultiAuthSessionPolicyIndex,
       "etsysMultiAuthSessionIsApplied": etsysMultiAuthSessionIsApplied,
       "etsysMultiAuthSessionTerminationTime": etsysMultiAuthSessionTerminationTime,
       "etsysMultiAuthSessionSessionTimeout": etsysMultiAuthSessionSessionTimeout,
       "etsysMultiAuthSessionIdleTimeout": etsysMultiAuthSessionIdleTimeout,
       "etsysMultiAuthSessionDuration": etsysMultiAuthSessionDuration,
       "etsysMultiAuthSessionIdleTime": etsysMultiAuthSessionIdleTime,
       "etsysMultiAuthSessionVlanTunnelAttribute": etsysMultiAuthSessionVlanTunnelAttribute,
       "etsysMultiAuthSessionPortTable": etsysMultiAuthSessionPortTable,
       "etsysMultiAuthSessionPortEntry": etsysMultiAuthSessionPortEntry,
       "etsysMultiAuthSessionPortAuthStatus": etsysMultiAuthSessionPortAuthStatus,
       "etsysMultiAuthModule": etsysMultiAuthModule,
       "etsysMultiAuthModuleTable": etsysMultiAuthModuleTable,
       "etsysMultiAuthModuleEntry": etsysMultiAuthModuleEntry,
       "etsysMultiAuthModuleMaxNumUsers": etsysMultiAuthModuleMaxNumUsers,
       "etsysMultiAuthModuleCurrentNumUsers": etsysMultiAuthModuleCurrentNumUsers,
       "etsysMultiAuthModuleMaxNumUsersReachedTrapEnable": etsysMultiAuthModuleMaxNumUsersReachedTrapEnable,
       "etsysMultiAuthConformance": etsysMultiAuthConformance,
       "etsysMultiAuthGroups": etsysMultiAuthGroups,
       "etsysMultiAuthSystemGroup": etsysMultiAuthSystemGroup,
       "etsysMultiAuthPortBaseGroup": etsysMultiAuthPortBaseGroup,
       "etsysMultiAuthPortTrapGroup": etsysMultiAuthPortTrapGroup,
       "etsysMultiAuthStationGroup": etsysMultiAuthStationGroup,
       "etsysMultiAuthSessionGroup": etsysMultiAuthSessionGroup,
       "etsysMultiAuthNotificationPortGroup": etsysMultiAuthNotificationPortGroup,
       "etsysMultiAuthModuleGroup": etsysMultiAuthModuleGroup,
       "etsysMultiAuthSessionGroup2": etsysMultiAuthSessionGroup2,
       "etsysMultiAuthTimeoutGroup": etsysMultiAuthTimeoutGroup,
       "etsysMultiAuthCurrentNumUsersGroup": etsysMultiAuthCurrentNumUsersGroup,
       "etsysMultiAuthModuleTrapGroup": etsysMultiAuthModuleTrapGroup,
       "etsysMultiAuthSystemTrapGroup": etsysMultiAuthSystemTrapGroup,
       "etsysMultiAuthNotificationModuleGroup": etsysMultiAuthNotificationModuleGroup,
       "etsysMultiAuthNotificationSystemGroup": etsysMultiAuthNotificationSystemGroup,
       "etsysMultiAuthTunnelAttributeGroup": etsysMultiAuthTunnelAttributeGroup,
       "etsysMultiAuthCompliances": etsysMultiAuthCompliances,
       "etsysMultiAuthCompliance": etsysMultiAuthCompliance,
       "etsysMultiAuthCompliance2": etsysMultiAuthCompliance2,
       "etsysMultiAuthCompliance3": etsysMultiAuthCompliance3,
       "etsysMultiAuthTimeoutCompliance": etsysMultiAuthTimeoutCompliance,
       "etsysMultiAuthCurrentNumUserCompliance": etsysMultiAuthCurrentNumUserCompliance,
       "etsysMultiAuthCompliance4": etsysMultiAuthCompliance4,
       "etsysMultiTunnelAttributeCompliance": etsysMultiTunnelAttributeCompliance}
)
