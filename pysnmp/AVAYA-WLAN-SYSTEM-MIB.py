# SNMP MIB module (AVAYA-WLAN-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AVAYA-WLAN-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:38 2024
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(avayaWlanMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "avayaWlanMibs")


# MODULE-IDENTITY

avayaWlanSystemMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 7, 16)
)
avayaWlanSystemMib.setRevisions(
        ("2010-05-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AvWlanSystemObjects_ObjectIdentity = ObjectIdentity
avWlanSystemObjects = _AvWlanSystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 7, 16, 1)
)
_AvWlanSystemConfig_ObjectIdentity = ObjectIdentity
avWlanSystemConfig = _AvWlanSystemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 7, 16, 1, 1)
)
_AvWlanSystemConfigScalars_ObjectIdentity = ObjectIdentity
avWlanSystemConfigScalars = _AvWlanSystemConfigScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 7, 16, 1, 1, 1)
)


class _AvWlanSystemConfigWirelessEnabled_Type(TruthValue):
    """Custom type avWlanSystemConfigWirelessEnabled based on TruthValue"""


_AvWlanSystemConfigWirelessEnabled_Object = MibScalar
avWlanSystemConfigWirelessEnabled = _AvWlanSystemConfigWirelessEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 16, 1, 1, 1, 1),
    _AvWlanSystemConfigWirelessEnabled_Type()
)
avWlanSystemConfigWirelessEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avWlanSystemConfigWirelessEnabled.setStatus("current")
_AvWlanSystemConfigSystemInetAddressType_Type = InetAddressType
_AvWlanSystemConfigSystemInetAddressType_Object = MibScalar
avWlanSystemConfigSystemInetAddressType = _AvWlanSystemConfigSystemInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 16, 1, 1, 1, 2),
    _AvWlanSystemConfigSystemInetAddressType_Type()
)
avWlanSystemConfigSystemInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avWlanSystemConfigSystemInetAddressType.setStatus("current")
_AvWlanSystemConfigSystemInetAddress_Type = InetAddress
_AvWlanSystemConfigSystemInetAddress_Object = MibScalar
avWlanSystemConfigSystemInetAddress = _AvWlanSystemConfigSystemInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 16, 1, 1, 1, 3),
    _AvWlanSystemConfigSystemInetAddress_Type()
)
avWlanSystemConfigSystemInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avWlanSystemConfigSystemInetAddress.setStatus("current")


class _AvWlanSystemConfigTcpUdpBasePort_Type(InetPortNumber):
    """Custom type avWlanSystemConfigTcpUdpBasePort based on InetPortNumber"""
    defaultValue = 61000

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(49152, 64983),
    )


_AvWlanSystemConfigTcpUdpBasePort_Type.__name__ = "InetPortNumber"
_AvWlanSystemConfigTcpUdpBasePort_Object = MibScalar
avWlanSystemConfigTcpUdpBasePort = _AvWlanSystemConfigTcpUdpBasePort_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 16, 1, 1, 1, 4),
    _AvWlanSystemConfigTcpUdpBasePort_Type()
)
avWlanSystemConfigTcpUdpBasePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avWlanSystemConfigTcpUdpBasePort.setStatus("current")
_AvWlanSystemStatus_ObjectIdentity = ObjectIdentity
avWlanSystemStatus = _AvWlanSystemStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 7, 16, 1, 2)
)
_AvWlanSystemStatusScalars_ObjectIdentity = ObjectIdentity
avWlanSystemStatusScalars = _AvWlanSystemStatusScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 7, 16, 1, 2, 1)
)


class _AvWlanSystemStatusOperationalStatus_Type(Integer32):
    """Custom type avWlanSystemStatusOperationalStatus based on Integer32"""
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
        *(("disablePending", 4),
          ("disabled", 3),
          ("enablePending", 2),
          ("enabled", 1))
    )


_AvWlanSystemStatusOperationalStatus_Type.__name__ = "Integer32"
_AvWlanSystemStatusOperationalStatus_Object = MibScalar
avWlanSystemStatusOperationalStatus = _AvWlanSystemStatusOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 16, 1, 2, 1, 1),
    _AvWlanSystemStatusOperationalStatus_Type()
)
avWlanSystemStatusOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avWlanSystemStatusOperationalStatus.setStatus("current")


class _AvWlanSystemStatusOperationalStatusDisableReason_Type(Integer32):
    """Custom type avWlanSystemStatusOperationalStatusDisableReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("adminDisabled", 2),
          ("badSystemInetAddress", 4),
          ("badTcpUdpBasePort", 5),
          ("none", 1),
          ("routingDisabled", 3),
          ("wirelessSystemError", 6))
    )


_AvWlanSystemStatusOperationalStatusDisableReason_Type.__name__ = "Integer32"
_AvWlanSystemStatusOperationalStatusDisableReason_Object = MibScalar
avWlanSystemStatusOperationalStatusDisableReason = _AvWlanSystemStatusOperationalStatusDisableReason_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 16, 1, 2, 1, 2),
    _AvWlanSystemStatusOperationalStatusDisableReason_Type()
)
avWlanSystemStatusOperationalStatusDisableReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avWlanSystemStatusOperationalStatusDisableReason.setStatus("current")
_AvWlanSystemStatusWlanSystemAddrType_Type = InetAddressType
_AvWlanSystemStatusWlanSystemAddrType_Object = MibScalar
avWlanSystemStatusWlanSystemAddrType = _AvWlanSystemStatusWlanSystemAddrType_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 16, 1, 2, 1, 3),
    _AvWlanSystemStatusWlanSystemAddrType_Type()
)
avWlanSystemStatusWlanSystemAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avWlanSystemStatusWlanSystemAddrType.setStatus("current")


class _AvWlanSystemStatusWlanSystemAddr_Type(InetAddress):
    """Custom type avWlanSystemStatusWlanSystemAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AvWlanSystemStatusWlanSystemAddr_Type.__name__ = "InetAddress"
_AvWlanSystemStatusWlanSystemAddr_Object = MibScalar
avWlanSystemStatusWlanSystemAddr = _AvWlanSystemStatusWlanSystemAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 16, 1, 2, 1, 4),
    _AvWlanSystemStatusWlanSystemAddr_Type()
)
avWlanSystemStatusWlanSystemAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avWlanSystemStatusWlanSystemAddr.setStatus("current")


class _AvWlanSystemStatusOperationalRole_Type(Integer32):
    """Custom type avWlanSystemStatusOperationalRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wcp", 1),
          ("wcpAndwsp", 3),
          ("wsp", 2))
    )


_AvWlanSystemStatusOperationalRole_Type.__name__ = "Integer32"
_AvWlanSystemStatusOperationalRole_Object = MibScalar
avWlanSystemStatusOperationalRole = _AvWlanSystemStatusOperationalRole_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 16, 1, 2, 1, 5),
    _AvWlanSystemStatusOperationalRole_Type()
)
avWlanSystemStatusOperationalRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avWlanSystemStatusOperationalRole.setStatus("current")
_AvWlanSystemStatusWlanVersion_Type = DisplayString
_AvWlanSystemStatusWlanVersion_Object = MibScalar
avWlanSystemStatusWlanVersion = _AvWlanSystemStatusWlanVersion_Object(
    (1, 3, 6, 1, 4, 1, 45, 7, 16, 1, 2, 1, 6),
    _AvWlanSystemStatusWlanVersion_Type()
)
avWlanSystemStatusWlanVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avWlanSystemStatusWlanVersion.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVAYA-WLAN-SYSTEM-MIB",
    **{"avayaWlanSystemMib": avayaWlanSystemMib,
       "avWlanSystemObjects": avWlanSystemObjects,
       "avWlanSystemConfig": avWlanSystemConfig,
       "avWlanSystemConfigScalars": avWlanSystemConfigScalars,
       "avWlanSystemConfigWirelessEnabled": avWlanSystemConfigWirelessEnabled,
       "avWlanSystemConfigSystemInetAddressType": avWlanSystemConfigSystemInetAddressType,
       "avWlanSystemConfigSystemInetAddress": avWlanSystemConfigSystemInetAddress,
       "avWlanSystemConfigTcpUdpBasePort": avWlanSystemConfigTcpUdpBasePort,
       "avWlanSystemStatus": avWlanSystemStatus,
       "avWlanSystemStatusScalars": avWlanSystemStatusScalars,
       "avWlanSystemStatusOperationalStatus": avWlanSystemStatusOperationalStatus,
       "avWlanSystemStatusOperationalStatusDisableReason": avWlanSystemStatusOperationalStatusDisableReason,
       "avWlanSystemStatusWlanSystemAddrType": avWlanSystemStatusWlanSystemAddrType,
       "avWlanSystemStatusWlanSystemAddr": avWlanSystemStatusWlanSystemAddr,
       "avWlanSystemStatusOperationalRole": avWlanSystemStatusOperationalRole,
       "avWlanSystemStatusWlanVersion": avWlanSystemStatusWlanVersion}
)
