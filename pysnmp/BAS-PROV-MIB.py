# SNMP MIB module (BAS-PROV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-PROV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:30 2024
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

(basProvInfo,) = mibBuilder.importSymbols(
    "BAS-MIB",
    "basProvInfo")

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

basProvInfoMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 4, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BasProvObjects_ObjectIdentity = ObjectIdentity
basProvObjects = _BasProvObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 4, 1, 1)
)
_BasProvServerId_Type = Integer32
_BasProvServerId_Object = MibScalar
basProvServerId = _BasProvServerId_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 4, 1, 1, 1),
    _BasProvServerId_Type()
)
basProvServerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basProvServerId.setStatus("current")
_BasProvInfoLdapServerIpAddr_Type = IpAddress
_BasProvInfoLdapServerIpAddr_Object = MibScalar
basProvInfoLdapServerIpAddr = _BasProvInfoLdapServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 4, 1, 1, 2),
    _BasProvInfoLdapServerIpAddr_Type()
)
basProvInfoLdapServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basProvInfoLdapServerIpAddr.setStatus("current")


class _BasProvInfoLdapServerPort_Type(Integer32):
    """Custom type basProvInfoLdapServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BasProvInfoLdapServerPort_Type.__name__ = "Integer32"
_BasProvInfoLdapServerPort_Object = MibScalar
basProvInfoLdapServerPort = _BasProvInfoLdapServerPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 4, 1, 1, 3),
    _BasProvInfoLdapServerPort_Type()
)
basProvInfoLdapServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basProvInfoLdapServerPort.setStatus("current")


class _BasProvInfoLdapServerUserName_Type(OctetString):
    """Custom type basProvInfoLdapServerUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BasProvInfoLdapServerUserName_Type.__name__ = "OctetString"
_BasProvInfoLdapServerUserName_Object = MibScalar
basProvInfoLdapServerUserName = _BasProvInfoLdapServerUserName_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 4, 1, 1, 4),
    _BasProvInfoLdapServerUserName_Type()
)
basProvInfoLdapServerUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basProvInfoLdapServerUserName.setStatus("current")


class _BasProvInfoLdapServerPassword_Type(OctetString):
    """Custom type basProvInfoLdapServerPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BasProvInfoLdapServerPassword_Type.__name__ = "OctetString"
_BasProvInfoLdapServerPassword_Object = MibScalar
basProvInfoLdapServerPassword = _BasProvInfoLdapServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 4, 1, 1, 5),
    _BasProvInfoLdapServerPassword_Type()
)
basProvInfoLdapServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basProvInfoLdapServerPassword.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-PROV-MIB",
    **{"basProvInfoMib": basProvInfoMib,
       "basProvObjects": basProvObjects,
       "basProvServerId": basProvServerId,
       "basProvInfoLdapServerIpAddr": basProvInfoLdapServerIpAddr,
       "basProvInfoLdapServerPort": basProvInfoLdapServerPort,
       "basProvInfoLdapServerUserName": basProvInfoLdapServerUserName,
       "basProvInfoLdapServerPassword": basProvInfoLdapServerPassword}
)
