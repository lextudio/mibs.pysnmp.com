# SNMP MIB module (DEVSERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DEVSERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:11 2024
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

(device,) = mibBuilder.importSymbols(
    "ANIROOT-MIB",
    "device")

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

aniDevServer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 2, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AniDevTftpServer_Type = IpAddress
_AniDevTftpServer_Object = MibScalar
aniDevTftpServer = _AniDevTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 5, 1),
    _AniDevTftpServer_Type()
)
aniDevTftpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevTftpServer.setStatus("current")
_AniDevDhcpServer_Type = IpAddress
_AniDevDhcpServer_Object = MibScalar
aniDevDhcpServer = _AniDevDhcpServer_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 5, 2),
    _AniDevDhcpServer_Type()
)
aniDevDhcpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevDhcpServer.setStatus("current")


class _AniDevDhcpLeaseExpiration_Type(DisplayString):
    """Custom type aniDevDhcpLeaseExpiration based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_AniDevDhcpLeaseExpiration_Type.__name__ = "DisplayString"
_AniDevDhcpLeaseExpiration_Object = MibScalar
aniDevDhcpLeaseExpiration = _AniDevDhcpLeaseExpiration_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 5, 3),
    _AniDevDhcpLeaseExpiration_Type()
)
aniDevDhcpLeaseExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevDhcpLeaseExpiration.setStatus("current")
_AniDevSuDhcpServer_Type = IpAddress
_AniDevSuDhcpServer_Object = MibScalar
aniDevSuDhcpServer = _AniDevSuDhcpServer_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 5, 4),
    _AniDevSuDhcpServer_Type()
)
aniDevSuDhcpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevSuDhcpServer.setStatus("current")
_AniDevTimeServer_Type = IpAddress
_AniDevTimeServer_Object = MibScalar
aniDevTimeServer = _AniDevTimeServer_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 5, 5),
    _AniDevTimeServer_Type()
)
aniDevTimeServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevTimeServer.setStatus("current")
_AniDevSyslogServer_Type = IpAddress
_AniDevSyslogServer_Object = MibScalar
aniDevSyslogServer = _AniDevSyslogServer_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 5, 6),
    _AniDevSyslogServer_Type()
)
aniDevSyslogServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniDevSyslogServer.setStatus("current")
_AniDevSmtpServer_Type = IpAddress
_AniDevSmtpServer_Object = MibScalar
aniDevSmtpServer = _AniDevSmtpServer_Object(
    (1, 3, 6, 1, 4, 1, 4325, 2, 5, 7),
    _AniDevSmtpServer_Type()
)
aniDevSmtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniDevSmtpServer.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DEVSERVER-MIB",
    **{"aniDevServer": aniDevServer,
       "aniDevTftpServer": aniDevTftpServer,
       "aniDevDhcpServer": aniDevDhcpServer,
       "aniDevDhcpLeaseExpiration": aniDevDhcpLeaseExpiration,
       "aniDevSuDhcpServer": aniDevSuDhcpServer,
       "aniDevTimeServer": aniDevTimeServer,
       "aniDevSyslogServer": aniDevSyslogServer,
       "aniDevSmtpServer": aniDevSmtpServer}
)
