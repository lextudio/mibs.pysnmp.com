# SNMP MIB module (Novell-License-Server-Trap-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Novell-License-Server-Trap-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:27 2024
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

(InternationalDisplayString,) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "InternationalDisplayString")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Novell_ObjectIdentity = ObjectIdentity
novell = _Novell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23)
)
_MibDoc_ObjectIdentity = ObjectIdentity
mibDoc = _MibDoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2)
)
_Nlstrap_mib_ObjectIdentity = ObjectIdentity
nlstrap_mib = _Nlstrap_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 73)
)
_Trapinfo_ObjectIdentity = ObjectIdentity
trapinfo = _Trapinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 1)
)


class _ServerName_Type(InternationalDisplayString):
    """Custom type serverName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_ServerName_Type.__name__ = "InternationalDisplayString"
_ServerName_Object = MibScalar
serverName = _ServerName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 1, 1),
    _ServerName_Type()
)
serverName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    serverName.setStatus("mandatory")
_TrapTime_Type = Integer32
_TrapTime_Object = MibScalar
trapTime = _TrapTime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 1, 2),
    _TrapTime_Type()
)
trapTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapTime.setStatus("mandatory")


class _AppName_Type(InternationalDisplayString):
    """Custom type appName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_AppName_Type.__name__ = "InternationalDisplayString"
_AppName_Object = MibScalar
appName = _AppName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 1, 3),
    _AppName_Type()
)
appName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appName.setStatus("mandatory")


class _UserName_Type(InternationalDisplayString):
    """Custom type userName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_UserName_Type.__name__ = "InternationalDisplayString"
_UserName_Object = MibScalar
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 1, 4),
    _UserName_Type()
)
userName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userName.setStatus("mandatory")


class _NetworkAddress_Type(OctetString):
    """Custom type networkAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_NetworkAddress_Type.__name__ = "OctetString"
_NetworkAddress_Object = MibScalar
networkAddress = _NetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 1, 5),
    _NetworkAddress_Type()
)
networkAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    networkAddress.setStatus("mandatory")


class _MacAddress_Type(OctetString):
    """Custom type macAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MacAddress_Type.__name__ = "OctetString"
_MacAddress_Object = MibScalar
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 1, 6),
    _MacAddress_Type()
)
macAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    macAddress.setStatus("mandatory")

# Managed Objects groups


# Notification objects

lsRequestSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 1)
)
lsRequestSuccess.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"),
        ("Novell-License-Server-Trap-MIB", "userName"),
        ("Novell-License-Server-Trap-MIB", "networkAddress"),
        ("Novell-License-Server-Trap-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    lsRequestSuccess.setStatus(
        ""
    )

lsRequestSystemError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 2)
)
lsRequestSystemError.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"),
        ("Novell-License-Server-Trap-MIB", "userName"),
        ("Novell-License-Server-Trap-MIB", "networkAddress"),
        ("Novell-License-Server-Trap-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    lsRequestSystemError.setStatus(
        ""
    )

lsRequestResourceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 3)
)
lsRequestResourceError.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"),
        ("Novell-License-Server-Trap-MIB", "userName"),
        ("Novell-License-Server-Trap-MIB", "networkAddress"),
        ("Novell-License-Server-Trap-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    lsRequestResourceError.setStatus(
        ""
    )

lsRequestAuthError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 4)
)
lsRequestAuthError.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"),
        ("Novell-License-Server-Trap-MIB", "userName"),
        ("Novell-License-Server-Trap-MIB", "networkAddress"),
        ("Novell-License-Server-Trap-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    lsRequestAuthError.setStatus(
        ""
    )

lsRequestBadArg = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 5)
)
lsRequestBadArg.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"),
        ("Novell-License-Server-Trap-MIB", "userName"),
        ("Novell-License-Server-Trap-MIB", "networkAddress"),
        ("Novell-License-Server-Trap-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    lsRequestBadArg.setStatus(
        ""
    )

lsRequestInsuffUnits = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 6)
)
lsRequestInsuffUnits.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"),
        ("Novell-License-Server-Trap-MIB", "userName"),
        ("Novell-License-Server-Trap-MIB", "networkAddress"),
        ("Novell-License-Server-Trap-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    lsRequestInsuffUnits.setStatus(
        ""
    )

lsRequestLicUnavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 7)
)
lsRequestLicUnavail.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"),
        ("Novell-License-Server-Trap-MIB", "userName"),
        ("Novell-License-Server-Trap-MIB", "networkAddress"),
        ("Novell-License-Server-Trap-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    lsRequestLicUnavail.setStatus(
        ""
    )

lsRequestNetUnavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 8)
)
lsRequestNetUnavail.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"),
        ("Novell-License-Server-Trap-MIB", "userName"),
        ("Novell-License-Server-Trap-MIB", "networkAddress"),
        ("Novell-License-Server-Trap-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    lsRequestNetUnavail.setStatus(
        ""
    )

lsRelSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 9)
)
lsRelSuccess.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"),
        ("Novell-License-Server-Trap-MIB", "userName"),
        ("Novell-License-Server-Trap-MIB", "networkAddress"),
        ("Novell-License-Server-Trap-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    lsRelSuccess.setStatus(
        ""
    )

lsRelSystemError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 10)
)
lsRelSystemError.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"),
        ("Novell-License-Server-Trap-MIB", "userName"),
        ("Novell-License-Server-Trap-MIB", "networkAddress"),
        ("Novell-License-Server-Trap-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    lsRelSystemError.setStatus(
        ""
    )

lsRelResouceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 11)
)
lsRelResouceError.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"),
        ("Novell-License-Server-Trap-MIB", "userName"),
        ("Novell-License-Server-Trap-MIB", "networkAddress"),
        ("Novell-License-Server-Trap-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    lsRelResouceError.setStatus(
        ""
    )

lsRelAuthError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 12)
)
lsRelAuthError.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"),
        ("Novell-License-Server-Trap-MIB", "userName"),
        ("Novell-License-Server-Trap-MIB", "networkAddress"),
        ("Novell-License-Server-Trap-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    lsRelAuthError.setStatus(
        ""
    )

lsRelBadArg = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 13)
)
lsRelBadArg.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"),
        ("Novell-License-Server-Trap-MIB", "userName"),
        ("Novell-License-Server-Trap-MIB", "networkAddress"),
        ("Novell-License-Server-Trap-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    lsRelBadArg.setStatus(
        ""
    )

lsRelBadHandle = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 14)
)
lsRelBadHandle.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"),
        ("Novell-License-Server-Trap-MIB", "userName"),
        ("Novell-License-Server-Trap-MIB", "networkAddress"),
        ("Novell-License-Server-Trap-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    lsRelBadHandle.setStatus(
        ""
    )

lsUpdateSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 15)
)
lsUpdateSuccess.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"),
        ("Novell-License-Server-Trap-MIB", "userName"),
        ("Novell-License-Server-Trap-MIB", "networkAddress"),
        ("Novell-License-Server-Trap-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    lsUpdateSuccess.setStatus(
        ""
    )

lsUpdateSystemError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 16)
)
lsUpdateSystemError.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"),
        ("Novell-License-Server-Trap-MIB", "userName"),
        ("Novell-License-Server-Trap-MIB", "networkAddress"),
        ("Novell-License-Server-Trap-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    lsUpdateSystemError.setStatus(
        ""
    )

lsUpdateResouceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 17)
)
lsUpdateResouceError.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"),
        ("Novell-License-Server-Trap-MIB", "userName"),
        ("Novell-License-Server-Trap-MIB", "networkAddress"),
        ("Novell-License-Server-Trap-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    lsUpdateResouceError.setStatus(
        ""
    )

lsUpdateAuthError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 18)
)
lsUpdateAuthError.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"),
        ("Novell-License-Server-Trap-MIB", "userName"),
        ("Novell-License-Server-Trap-MIB", "networkAddress"),
        ("Novell-License-Server-Trap-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    lsUpdateAuthError.setStatus(
        ""
    )

lsUpdateBadArg = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 19)
)
lsUpdateBadArg.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"),
        ("Novell-License-Server-Trap-MIB", "userName"),
        ("Novell-License-Server-Trap-MIB", "networkAddress"),
        ("Novell-License-Server-Trap-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    lsUpdateBadArg.setStatus(
        ""
    )

lsUpdateBadHandle = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 20)
)
lsUpdateBadHandle.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"),
        ("Novell-License-Server-Trap-MIB", "userName"),
        ("Novell-License-Server-Trap-MIB", "networkAddress"),
        ("Novell-License-Server-Trap-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    lsUpdateBadHandle.setStatus(
        ""
    )

lsUpdateInsuffUnits = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 21)
)
lsUpdateInsuffUnits.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"),
        ("Novell-License-Server-Trap-MIB", "userName"),
        ("Novell-License-Server-Trap-MIB", "networkAddress"),
        ("Novell-License-Server-Trap-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    lsUpdateInsuffUnits.setStatus(
        ""
    )

lsUpdateLicUnavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 22)
)
lsUpdateLicUnavail.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"),
        ("Novell-License-Server-Trap-MIB", "userName"),
        ("Novell-License-Server-Trap-MIB", "networkAddress"),
        ("Novell-License-Server-Trap-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    lsUpdateLicUnavail.setStatus(
        ""
    )

lsUpdateLicTerm = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 23)
)
lsUpdateLicTerm.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"),
        ("Novell-License-Server-Trap-MIB", "userName"),
        ("Novell-License-Server-Trap-MIB", "networkAddress"),
        ("Novell-License-Server-Trap-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    lsUpdateLicTerm.setStatus(
        ""
    )

lsUpdateLicExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 24)
)
lsUpdateLicExpired.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"),
        ("Novell-License-Server-Trap-MIB", "userName"),
        ("Novell-License-Server-Trap-MIB", "networkAddress"),
        ("Novell-License-Server-Trap-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    lsUpdateLicExpired.setStatus(
        ""
    )

addAssignSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 25)
)
addAssignSuccess.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"))
)
if mibBuilder.loadTexts:
    addAssignSuccess.setStatus(
        ""
    )

addAssignSystemError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 26)
)
addAssignSystemError.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"))
)
if mibBuilder.loadTexts:
    addAssignSystemError.setStatus(
        ""
    )

addAssignResourceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 27)
)
addAssignResourceError.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"))
)
if mibBuilder.loadTexts:
    addAssignResourceError.setStatus(
        ""
    )

addAssignAuthError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 28)
)
addAssignAuthError.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"))
)
if mibBuilder.loadTexts:
    addAssignAuthError.setStatus(
        ""
    )

addAssignBadArg = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 29)
)
addAssignBadArg.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"))
)
if mibBuilder.loadTexts:
    addAssignBadArg.setStatus(
        ""
    )

removeAssignSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 30)
)
removeAssignSuccess.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"))
)
if mibBuilder.loadTexts:
    removeAssignSuccess.setStatus(
        ""
    )

removeAssignSystemError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 31)
)
removeAssignSystemError.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"))
)
if mibBuilder.loadTexts:
    removeAssignSystemError.setStatus(
        ""
    )

removeAssignResourceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 32)
)
removeAssignResourceError.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"))
)
if mibBuilder.loadTexts:
    removeAssignResourceError.setStatus(
        ""
    )

removeAssignAuthError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 33)
)
removeAssignAuthError.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"))
)
if mibBuilder.loadTexts:
    removeAssignAuthError.setStatus(
        ""
    )

removeAssignBadArg = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 34)
)
removeAssignBadArg.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"))
)
if mibBuilder.loadTexts:
    removeAssignBadArg.setStatus(
        ""
    )

installCertifSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 35)
)
installCertifSuccess.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"))
)
if mibBuilder.loadTexts:
    installCertifSuccess.setStatus(
        ""
    )

installCertifSystemError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 36)
)
installCertifSystemError.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"))
)
if mibBuilder.loadTexts:
    installCertifSystemError.setStatus(
        ""
    )

installCertifResourceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 37)
)
installCertifResourceError.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"))
)
if mibBuilder.loadTexts:
    installCertifResourceError.setStatus(
        ""
    )

installCertifAuthError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 38)
)
installCertifAuthError.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"))
)
if mibBuilder.loadTexts:
    installCertifAuthError.setStatus(
        ""
    )

installCertifBadArg = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 39)
)
installCertifBadArg.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"))
)
if mibBuilder.loadTexts:
    installCertifBadArg.setStatus(
        ""
    )

deleteCertifSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 40)
)
deleteCertifSuccess.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"))
)
if mibBuilder.loadTexts:
    deleteCertifSuccess.setStatus(
        ""
    )

deleteCertifSystemError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 41)
)
deleteCertifSystemError.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"))
)
if mibBuilder.loadTexts:
    deleteCertifSystemError.setStatus(
        ""
    )

deleteCertifResourceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 42)
)
deleteCertifResourceError.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"))
)
if mibBuilder.loadTexts:
    deleteCertifResourceError.setStatus(
        ""
    )

deleteCertifAuthError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 43)
)
deleteCertifAuthError.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"))
)
if mibBuilder.loadTexts:
    deleteCertifAuthError.setStatus(
        ""
    )

deleteCertifBadArg = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 44)
)
deleteCertifBadArg.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"))
)
if mibBuilder.loadTexts:
    deleteCertifBadArg.setStatus(
        ""
    )

transOwnerSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 45)
)
transOwnerSuccess.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"))
)
if mibBuilder.loadTexts:
    transOwnerSuccess.setStatus(
        ""
    )

transOwnerSystemError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 46)
)
transOwnerSystemError.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"))
)
if mibBuilder.loadTexts:
    transOwnerSystemError.setStatus(
        ""
    )

transOwnerResourceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 47)
)
transOwnerResourceError.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"))
)
if mibBuilder.loadTexts:
    transOwnerResourceError.setStatus(
        ""
    )

transOwnerAuthError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 48)
)
transOwnerAuthError.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"))
)
if mibBuilder.loadTexts:
    transOwnerAuthError.setStatus(
        ""
    )

transOwnerBadArg = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 49)
)
transOwnerBadArg.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"))
)
if mibBuilder.loadTexts:
    transOwnerBadArg.setStatus(
        ""
    )

addProdInfoSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 50)
)
addProdInfoSuccess.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"))
)
if mibBuilder.loadTexts:
    addProdInfoSuccess.setStatus(
        ""
    )

addProdInfoSystemError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 51)
)
addProdInfoSystemError.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"))
)
if mibBuilder.loadTexts:
    addProdInfoSystemError.setStatus(
        ""
    )

addProdInfoResourceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 52)
)
addProdInfoResourceError.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"))
)
if mibBuilder.loadTexts:
    addProdInfoResourceError.setStatus(
        ""
    )

addProdInfoAuthError = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 53)
)
addProdInfoAuthError.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"))
)
if mibBuilder.loadTexts:
    addProdInfoAuthError.setStatus(
        ""
    )

addProdInfoBadArg = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 54)
)
addProdInfoBadArg.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"),
        ("Novell-License-Server-Trap-MIB", "appName"))
)
if mibBuilder.loadTexts:
    addProdInfoBadArg.setStatus(
        ""
    )

nlsTrapLoaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 98)
)
nlsTrapLoaded.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    nlsTrapLoaded.setStatus(
        ""
    )

nlsTrapUnloaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 73, 0, 99)
)
nlsTrapUnloaded.setObjects(
      *(("Novell-License-Server-Trap-MIB", "serverName"),
        ("Novell-License-Server-Trap-MIB", "trapTime"))
)
if mibBuilder.loadTexts:
    nlsTrapUnloaded.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Novell-License-Server-Trap-MIB",
    **{"novell": novell,
       "mibDoc": mibDoc,
       "nlstrap-mib": nlstrap_mib,
       "lsRequestSuccess": lsRequestSuccess,
       "lsRequestSystemError": lsRequestSystemError,
       "lsRequestResourceError": lsRequestResourceError,
       "lsRequestAuthError": lsRequestAuthError,
       "lsRequestBadArg": lsRequestBadArg,
       "lsRequestInsuffUnits": lsRequestInsuffUnits,
       "lsRequestLicUnavail": lsRequestLicUnavail,
       "lsRequestNetUnavail": lsRequestNetUnavail,
       "lsRelSuccess": lsRelSuccess,
       "lsRelSystemError": lsRelSystemError,
       "lsRelResouceError": lsRelResouceError,
       "lsRelAuthError": lsRelAuthError,
       "lsRelBadArg": lsRelBadArg,
       "lsRelBadHandle": lsRelBadHandle,
       "lsUpdateSuccess": lsUpdateSuccess,
       "lsUpdateSystemError": lsUpdateSystemError,
       "lsUpdateResouceError": lsUpdateResouceError,
       "lsUpdateAuthError": lsUpdateAuthError,
       "lsUpdateBadArg": lsUpdateBadArg,
       "lsUpdateBadHandle": lsUpdateBadHandle,
       "lsUpdateInsuffUnits": lsUpdateInsuffUnits,
       "lsUpdateLicUnavail": lsUpdateLicUnavail,
       "lsUpdateLicTerm": lsUpdateLicTerm,
       "lsUpdateLicExpired": lsUpdateLicExpired,
       "addAssignSuccess": addAssignSuccess,
       "addAssignSystemError": addAssignSystemError,
       "addAssignResourceError": addAssignResourceError,
       "addAssignAuthError": addAssignAuthError,
       "addAssignBadArg": addAssignBadArg,
       "removeAssignSuccess": removeAssignSuccess,
       "removeAssignSystemError": removeAssignSystemError,
       "removeAssignResourceError": removeAssignResourceError,
       "removeAssignAuthError": removeAssignAuthError,
       "removeAssignBadArg": removeAssignBadArg,
       "installCertifSuccess": installCertifSuccess,
       "installCertifSystemError": installCertifSystemError,
       "installCertifResourceError": installCertifResourceError,
       "installCertifAuthError": installCertifAuthError,
       "installCertifBadArg": installCertifBadArg,
       "deleteCertifSuccess": deleteCertifSuccess,
       "deleteCertifSystemError": deleteCertifSystemError,
       "deleteCertifResourceError": deleteCertifResourceError,
       "deleteCertifAuthError": deleteCertifAuthError,
       "deleteCertifBadArg": deleteCertifBadArg,
       "transOwnerSuccess": transOwnerSuccess,
       "transOwnerSystemError": transOwnerSystemError,
       "transOwnerResourceError": transOwnerResourceError,
       "transOwnerAuthError": transOwnerAuthError,
       "transOwnerBadArg": transOwnerBadArg,
       "addProdInfoSuccess": addProdInfoSuccess,
       "addProdInfoSystemError": addProdInfoSystemError,
       "addProdInfoResourceError": addProdInfoResourceError,
       "addProdInfoAuthError": addProdInfoAuthError,
       "addProdInfoBadArg": addProdInfoBadArg,
       "nlsTrapLoaded": nlsTrapLoaded,
       "nlsTrapUnloaded": nlsTrapUnloaded,
       "trapinfo": trapinfo,
       "serverName": serverName,
       "trapTime": trapTime,
       "appName": appName,
       "userName": userName,
       "networkAddress": networkAddress,
       "macAddress": macAddress}
)
