# SNMP MIB module (TOS-SYSINFO) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TOS-SYSINFO
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:39 2024
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge,
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
 Opaque,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge",
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")

(tosMib,) = mibBuilder.importSymbols(
    "TOS-SMI",
    "tosMib")


# MODULE-IDENTITY

sysInfo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3)
)
sysInfo.setRevisions(
        ("1970-01-01 00:00",
         "1970-01-01 00:00",
         "1970-01-01 00:00",
         "1970-01-01 00:00",
         "1970-01-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _SysProductSN_Type(DisplayString):
    """Custom type sysProductSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysProductSN_Type.__name__ = "DisplayString"
_SysProductSN_Object = MibScalar
sysProductSN = _SysProductSN_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 1),
    _SysProductSN_Type()
)
sysProductSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysProductSN.setStatus("current")


class _SysProductType_Type(DisplayString):
    """Custom type sysProductType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysProductType_Type.__name__ = "DisplayString"
_SysProductType_Object = MibScalar
sysProductType = _SysProductType_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 2),
    _SysProductType_Type()
)
sysProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysProductType.setStatus("current")


class _SysSoftwareVersion_Type(DisplayString):
    """Custom type sysSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysSoftwareVersion_Type.__name__ = "DisplayString"
_SysSoftwareVersion_Object = MibScalar
sysSoftwareVersion = _SysSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 3),
    _SysSoftwareVersion_Type()
)
sysSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSoftwareVersion.setStatus("current")


class _SysHardwareId_Type(DisplayString):
    """Custom type sysHardwareId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysHardwareId_Type.__name__ = "DisplayString"
_SysHardwareId_Object = MibScalar
sysHardwareId = _SysHardwareId_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 4),
    _SysHardwareId_Type()
)
sysHardwareId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHardwareId.setStatus("current")
_SysSnmpVersion_Type = DisplayString
_SysSnmpVersion_Object = MibScalar
sysSnmpVersion = _SysSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 5),
    _SysSnmpVersion_Type()
)
sysSnmpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSnmpVersion.setStatus("current")


class _SysVpnEngine_Type(DisplayString):
    """Custom type sysVpnEngine based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysVpnEngine_Type.__name__ = "DisplayString"
_SysVpnEngine_Object = MibScalar
sysVpnEngine = _SysVpnEngine_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 6),
    _SysVpnEngine_Type()
)
sysVpnEngine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVpnEngine.setStatus("current")


class _SysAntiVirusEngine_Type(DisplayString):
    """Custom type sysAntiVirusEngine based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysAntiVirusEngine_Type.__name__ = "DisplayString"
_SysAntiVirusEngine_Object = MibScalar
sysAntiVirusEngine = _SysAntiVirusEngine_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 7),
    _SysAntiVirusEngine_Type()
)
sysAntiVirusEngine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAntiVirusEngine.setStatus("current")


class _SysAntiVirusLibrary_Type(DisplayString):
    """Custom type sysAntiVirusLibrary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysAntiVirusLibrary_Type.__name__ = "DisplayString"
_SysAntiVirusLibrary_Object = MibScalar
sysAntiVirusLibrary = _SysAntiVirusLibrary_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 8),
    _SysAntiVirusLibrary_Type()
)
sysAntiVirusLibrary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAntiVirusLibrary.setStatus("current")


class _SysSecurityEngine_Type(DisplayString):
    """Custom type sysSecurityEngine based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysSecurityEngine_Type.__name__ = "DisplayString"
_SysSecurityEngine_Object = MibScalar
sysSecurityEngine = _SysSecurityEngine_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 9),
    _SysSecurityEngine_Type()
)
sysSecurityEngine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSecurityEngine.setStatus("current")


class _SysDpiSupport_Type(DisplayString):
    """Custom type sysDpiSupport based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysDpiSupport_Type.__name__ = "DisplayString"
_SysDpiSupport_Object = MibScalar
sysDpiSupport = _SysDpiSupport_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 10),
    _SysDpiSupport_Type()
)
sysDpiSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDpiSupport.setStatus("current")


class _SysNatSupport_Type(DisplayString):
    """Custom type sysNatSupport based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysNatSupport_Type.__name__ = "DisplayString"
_SysNatSupport_Object = MibScalar
sysNatSupport = _SysNatSupport_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 11),
    _SysNatSupport_Type()
)
sysNatSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysNatSupport.setStatus("current")


class _SysAuthenticationSupport_Type(DisplayString):
    """Custom type sysAuthenticationSupport based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysAuthenticationSupport_Type.__name__ = "DisplayString"
_SysAuthenticationSupport_Object = MibScalar
sysAuthenticationSupport = _SysAuthenticationSupport_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 12),
    _SysAuthenticationSupport_Type()
)
sysAuthenticationSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAuthenticationSupport.setStatus("current")


class _SysService_Type(DisplayString):
    """Custom type sysService based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysService_Type.__name__ = "DisplayString"
_SysService_Object = MibScalar
sysService = _SysService_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 13),
    _SysService_Type()
)
sysService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysService.setStatus("current")


class _SysDynamicRoutingProtocol_Type(DisplayString):
    """Custom type sysDynamicRoutingProtocol based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysDynamicRoutingProtocol_Type.__name__ = "DisplayString"
_SysDynamicRoutingProtocol_Object = MibScalar
sysDynamicRoutingProtocol = _SysDynamicRoutingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 14),
    _SysDynamicRoutingProtocol_Type()
)
sysDynamicRoutingProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDynamicRoutingProtocol.setStatus("current")
_SysMaxSession_Type = Integer32
_SysMaxSession_Object = MibScalar
sysMaxSession = _SysMaxSession_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 15),
    _SysMaxSession_Type()
)
sysMaxSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMaxSession.setStatus("current")
_SysMaxVrcClient_Type = Integer32
_SysMaxVrcClient_Object = MibScalar
sysMaxVrcClient = _SysMaxVrcClient_Object(
    (1, 3, 6, 1, 4, 1, 14331, 5, 5, 1, 3, 16),
    _SysMaxVrcClient_Type()
)
sysMaxVrcClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMaxVrcClient.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TOS-SYSINFO",
    **{"sysInfo": sysInfo,
       "sysProductSN": sysProductSN,
       "sysProductType": sysProductType,
       "sysSoftwareVersion": sysSoftwareVersion,
       "sysHardwareId": sysHardwareId,
       "sysSnmpVersion": sysSnmpVersion,
       "sysVpnEngine": sysVpnEngine,
       "sysAntiVirusEngine": sysAntiVirusEngine,
       "sysAntiVirusLibrary": sysAntiVirusLibrary,
       "sysSecurityEngine": sysSecurityEngine,
       "sysDpiSupport": sysDpiSupport,
       "sysNatSupport": sysNatSupport,
       "sysAuthenticationSupport": sysAuthenticationSupport,
       "sysService": sysService,
       "sysDynamicRoutingProtocol": sysDynamicRoutingProtocol,
       "sysMaxSession": sysMaxSession,
       "sysMaxVrcClient": sysMaxVrcClient}
)
