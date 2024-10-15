# SNMP MIB module (BIANCA-BRICK-L2TP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-L2TP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:32 2024
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

_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Vpn_ObjectIdentity = ObjectIdentity
vpn = _Vpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 23)
)
_L2tp_ObjectIdentity = ObjectIdentity
l2tp = _L2tp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8)
)
_L2tpGlobals_ObjectIdentity = ObjectIdentity
l2tpGlobals = _L2tpGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 10)
)


class _L2tpGlobUdpPort_Type(Integer32):
    """Custom type l2tpGlobUdpPort based on Integer32"""
    defaultValue = 1701

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_L2tpGlobUdpPort_Type.__name__ = "Integer32"
_L2tpGlobUdpPort_Object = MibScalar
l2tpGlobUdpPort = _L2tpGlobUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 10, 10),
    _L2tpGlobUdpPort_Type()
)
l2tpGlobUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpGlobUdpPort.setStatus("mandatory")


class _L2tpGlobPortUsage_Type(Integer32):
    """Custom type l2tpGlobPortUsage based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("floating", 2),
          ("single", 1))
    )


_L2tpGlobPortUsage_Type.__name__ = "Integer32"
_L2tpGlobPortUsage_Object = MibScalar
l2tpGlobPortUsage = _L2tpGlobPortUsage_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 10, 20),
    _L2tpGlobPortUsage_Type()
)
l2tpGlobPortUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpGlobPortUsage.setStatus("mandatory")
_L2tpTunnelProfileTable_Object = MibTable
l2tpTunnelProfileTable = _L2tpTunnelProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 20)
)
if mibBuilder.loadTexts:
    l2tpTunnelProfileTable.setStatus("mandatory")
_L2tpTunnelProfileEntry_Object = MibTableRow
l2tpTunnelProfileEntry = _L2tpTunnelProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 20, 10)
)
l2tpTunnelProfileEntry.setIndexNames(
    (0, "BIANCA-BRICK-L2TP-MIB", "l2tpTunnelProfileIndex"),
)
if mibBuilder.loadTexts:
    l2tpTunnelProfileEntry.setStatus("mandatory")


class _L2tpTunnelProfileIndex_Type(Integer32):
    """Custom type l2tpTunnelProfileIndex based on Integer32"""
    defaultValue = 0


_L2tpTunnelProfileIndex_Object = MibTableColumn
l2tpTunnelProfileIndex = _L2tpTunnelProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 20, 10, 10),
    _L2tpTunnelProfileIndex_Type()
)
l2tpTunnelProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelProfileIndex.setStatus("mandatory")


class _L2tpTunnelProfileName_Type(DisplayString):
    """Custom type l2tpTunnelProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_L2tpTunnelProfileName_Type.__name__ = "DisplayString"
_L2tpTunnelProfileName_Object = MibTableColumn
l2tpTunnelProfileName = _L2tpTunnelProfileName_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 20, 10, 15),
    _L2tpTunnelProfileName_Type()
)
l2tpTunnelProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelProfileName.setStatus("mandatory")
_L2tpTunnelProfileRemoteIpAddress_Type = IpAddress
_L2tpTunnelProfileRemoteIpAddress_Object = MibTableColumn
l2tpTunnelProfileRemoteIpAddress = _L2tpTunnelProfileRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 20, 10, 20),
    _L2tpTunnelProfileRemoteIpAddress_Type()
)
l2tpTunnelProfileRemoteIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelProfileRemoteIpAddress.setStatus("mandatory")
_L2tpTunnelProfileRemoteIpAddressBackup_Type = IpAddress
_L2tpTunnelProfileRemoteIpAddressBackup_Object = MibTableColumn
l2tpTunnelProfileRemoteIpAddressBackup = _L2tpTunnelProfileRemoteIpAddressBackup_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 20, 10, 25),
    _L2tpTunnelProfileRemoteIpAddressBackup_Type()
)
l2tpTunnelProfileRemoteIpAddressBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelProfileRemoteIpAddressBackup.setStatus("mandatory")


class _L2tpTunnelProfileRemoteUdpPort_Type(Integer32):
    """Custom type l2tpTunnelProfileRemoteUdpPort based on Integer32"""
    defaultValue = 1701

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpTunnelProfileRemoteUdpPort_Type.__name__ = "Integer32"
_L2tpTunnelProfileRemoteUdpPort_Object = MibTableColumn
l2tpTunnelProfileRemoteUdpPort = _L2tpTunnelProfileRemoteUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 20, 10, 30),
    _L2tpTunnelProfileRemoteUdpPort_Type()
)
l2tpTunnelProfileRemoteUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelProfileRemoteUdpPort.setStatus("mandatory")


class _L2tpTunnelProfileRemoteHostname_Type(DisplayString):
    """Custom type l2tpTunnelProfileRemoteHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_L2tpTunnelProfileRemoteHostname_Type.__name__ = "DisplayString"
_L2tpTunnelProfileRemoteHostname_Object = MibTableColumn
l2tpTunnelProfileRemoteHostname = _L2tpTunnelProfileRemoteHostname_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 20, 10, 40),
    _L2tpTunnelProfileRemoteHostname_Type()
)
l2tpTunnelProfileRemoteHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelProfileRemoteHostname.setStatus("mandatory")
_L2tpTunnelProfileLocalIpAddress_Type = IpAddress
_L2tpTunnelProfileLocalIpAddress_Object = MibTableColumn
l2tpTunnelProfileLocalIpAddress = _L2tpTunnelProfileLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 20, 10, 50),
    _L2tpTunnelProfileLocalIpAddress_Type()
)
l2tpTunnelProfileLocalIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelProfileLocalIpAddress.setStatus("mandatory")


class _L2tpTunnelProfileLocalUdpPort_Type(Integer32):
    """Custom type l2tpTunnelProfileLocalUdpPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpTunnelProfileLocalUdpPort_Type.__name__ = "Integer32"
_L2tpTunnelProfileLocalUdpPort_Object = MibTableColumn
l2tpTunnelProfileLocalUdpPort = _L2tpTunnelProfileLocalUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 20, 10, 60),
    _L2tpTunnelProfileLocalUdpPort_Type()
)
l2tpTunnelProfileLocalUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelProfileLocalUdpPort.setStatus("mandatory")


class _L2tpTunnelProfileLocalHostname_Type(DisplayString):
    """Custom type l2tpTunnelProfileLocalHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_L2tpTunnelProfileLocalHostname_Type.__name__ = "DisplayString"
_L2tpTunnelProfileLocalHostname_Object = MibTableColumn
l2tpTunnelProfileLocalHostname = _L2tpTunnelProfileLocalHostname_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 20, 10, 70),
    _L2tpTunnelProfileLocalHostname_Type()
)
l2tpTunnelProfileLocalHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelProfileLocalHostname.setStatus("mandatory")


class _L2tpTunnelProfilePassword_Type(DisplayString):
    """Custom type l2tpTunnelProfilePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_L2tpTunnelProfilePassword_Type.__name__ = "DisplayString"
_L2tpTunnelProfilePassword_Object = MibTableColumn
l2tpTunnelProfilePassword = _L2tpTunnelProfilePassword_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 20, 10, 80),
    _L2tpTunnelProfilePassword_Type()
)
l2tpTunnelProfilePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelProfilePassword.setStatus("mandatory")


class _L2tpTunnelProfileReceiveWindowSize_Type(Integer32):
    """Custom type l2tpTunnelProfileReceiveWindowSize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_L2tpTunnelProfileReceiveWindowSize_Type.__name__ = "Integer32"
_L2tpTunnelProfileReceiveWindowSize_Object = MibTableColumn
l2tpTunnelProfileReceiveWindowSize = _L2tpTunnelProfileReceiveWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 20, 10, 90),
    _L2tpTunnelProfileReceiveWindowSize_Type()
)
l2tpTunnelProfileReceiveWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelProfileReceiveWindowSize.setStatus("mandatory")


class _L2tpTunnelProfileHelloInterval_Type(Integer32):
    """Custom type l2tpTunnelProfileHelloInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_L2tpTunnelProfileHelloInterval_Type.__name__ = "Integer32"
_L2tpTunnelProfileHelloInterval_Object = MibTableColumn
l2tpTunnelProfileHelloInterval = _L2tpTunnelProfileHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 20, 10, 100),
    _L2tpTunnelProfileHelloInterval_Type()
)
l2tpTunnelProfileHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelProfileHelloInterval.setStatus("mandatory")


class _L2tpTunnelProfileSessionDataSequencing_Type(Integer32):
    """Custom type l2tpTunnelProfileSessionDataSequencing based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_L2tpTunnelProfileSessionDataSequencing_Type.__name__ = "Integer32"
_L2tpTunnelProfileSessionDataSequencing_Object = MibTableColumn
l2tpTunnelProfileSessionDataSequencing = _L2tpTunnelProfileSessionDataSequencing_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 20, 10, 110),
    _L2tpTunnelProfileSessionDataSequencing_Type()
)
l2tpTunnelProfileSessionDataSequencing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelProfileSessionDataSequencing.setStatus("mandatory")


class _L2tpTunnelProfileMinRetryTime_Type(Integer32):
    """Custom type l2tpTunnelProfileMinRetryTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_L2tpTunnelProfileMinRetryTime_Type.__name__ = "Integer32"
_L2tpTunnelProfileMinRetryTime_Object = MibTableColumn
l2tpTunnelProfileMinRetryTime = _L2tpTunnelProfileMinRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 20, 10, 120),
    _L2tpTunnelProfileMinRetryTime_Type()
)
l2tpTunnelProfileMinRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelProfileMinRetryTime.setStatus("mandatory")


class _L2tpTunnelProfileMaxRetryTime_Type(Integer32):
    """Custom type l2tpTunnelProfileMaxRetryTime based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 255),
    )


_L2tpTunnelProfileMaxRetryTime_Type.__name__ = "Integer32"
_L2tpTunnelProfileMaxRetryTime_Object = MibTableColumn
l2tpTunnelProfileMaxRetryTime = _L2tpTunnelProfileMaxRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 20, 10, 130),
    _L2tpTunnelProfileMaxRetryTime_Type()
)
l2tpTunnelProfileMaxRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelProfileMaxRetryTime.setStatus("mandatory")


class _L2tpTunnelProfileMaxRetries_Type(Integer32):
    """Custom type l2tpTunnelProfileMaxRetries based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_L2tpTunnelProfileMaxRetries_Type.__name__ = "Integer32"
_L2tpTunnelProfileMaxRetries_Object = MibTableColumn
l2tpTunnelProfileMaxRetries = _L2tpTunnelProfileMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 20, 10, 140),
    _L2tpTunnelProfileMaxRetries_Type()
)
l2tpTunnelProfileMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelProfileMaxRetries.setStatus("mandatory")


class _L2tpTunnelProfileRadiusAssignment_Type(Integer32):
    """Custom type l2tpTunnelProfileRadiusAssignment based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_L2tpTunnelProfileRadiusAssignment_Type.__name__ = "Integer32"
_L2tpTunnelProfileRadiusAssignment_Object = MibTableColumn
l2tpTunnelProfileRadiusAssignment = _L2tpTunnelProfileRadiusAssignment_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 20, 10, 150),
    _L2tpTunnelProfileRadiusAssignment_Type()
)
l2tpTunnelProfileRadiusAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelProfileRadiusAssignment.setStatus("mandatory")


class _L2tpTunnelProfileRadiusGroupId_Type(Integer32):
    """Custom type l2tpTunnelProfileRadiusGroupId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_L2tpTunnelProfileRadiusGroupId_Type.__name__ = "Integer32"
_L2tpTunnelProfileRadiusGroupId_Object = MibTableColumn
l2tpTunnelProfileRadiusGroupId = _L2tpTunnelProfileRadiusGroupId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 20, 10, 160),
    _L2tpTunnelProfileRadiusGroupId_Type()
)
l2tpTunnelProfileRadiusGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelProfileRadiusGroupId.setStatus("mandatory")
_L2tpTunnelTable_Object = MibTable
l2tpTunnelTable = _L2tpTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 30)
)
if mibBuilder.loadTexts:
    l2tpTunnelTable.setStatus("mandatory")
_L2tpTunnelEntry_Object = MibTableRow
l2tpTunnelEntry = _L2tpTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 30, 10)
)
l2tpTunnelEntry.setIndexNames(
    (0, "BIANCA-BRICK-L2TP-MIB", "l2tpTunnelLocalTunnelId"),
)
if mibBuilder.loadTexts:
    l2tpTunnelEntry.setStatus("mandatory")
_L2tpTunnelRemoteIpAddress_Type = IpAddress
_L2tpTunnelRemoteIpAddress_Object = MibTableColumn
l2tpTunnelRemoteIpAddress = _L2tpTunnelRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 30, 10, 10),
    _L2tpTunnelRemoteIpAddress_Type()
)
l2tpTunnelRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelRemoteIpAddress.setStatus("mandatory")


class _L2tpTunnelRemoteUdpPort_Type(Integer32):
    """Custom type l2tpTunnelRemoteUdpPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpTunnelRemoteUdpPort_Type.__name__ = "Integer32"
_L2tpTunnelRemoteUdpPort_Object = MibTableColumn
l2tpTunnelRemoteUdpPort = _L2tpTunnelRemoteUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 30, 10, 20),
    _L2tpTunnelRemoteUdpPort_Type()
)
l2tpTunnelRemoteUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelRemoteUdpPort.setStatus("mandatory")


class _L2tpTunnelRemoteTunnelId_Type(Integer32):
    """Custom type l2tpTunnelRemoteTunnelId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpTunnelRemoteTunnelId_Type.__name__ = "Integer32"
_L2tpTunnelRemoteTunnelId_Object = MibTableColumn
l2tpTunnelRemoteTunnelId = _L2tpTunnelRemoteTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 30, 10, 30),
    _L2tpTunnelRemoteTunnelId_Type()
)
l2tpTunnelRemoteTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelRemoteTunnelId.setStatus("mandatory")


class _L2tpTunnelRemoteReceiveWindowSize_Type(Integer32):
    """Custom type l2tpTunnelRemoteReceiveWindowSize based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_L2tpTunnelRemoteReceiveWindowSize_Type.__name__ = "Integer32"
_L2tpTunnelRemoteReceiveWindowSize_Object = MibTableColumn
l2tpTunnelRemoteReceiveWindowSize = _L2tpTunnelRemoteReceiveWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 30, 10, 35),
    _L2tpTunnelRemoteReceiveWindowSize_Type()
)
l2tpTunnelRemoteReceiveWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelRemoteReceiveWindowSize.setStatus("mandatory")


class _L2tpTunnelRemoteHostname_Type(DisplayString):
    """Custom type l2tpTunnelRemoteHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_L2tpTunnelRemoteHostname_Type.__name__ = "DisplayString"
_L2tpTunnelRemoteHostname_Object = MibTableColumn
l2tpTunnelRemoteHostname = _L2tpTunnelRemoteHostname_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 30, 10, 40),
    _L2tpTunnelRemoteHostname_Type()
)
l2tpTunnelRemoteHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelRemoteHostname.setStatus("mandatory")


class _L2tpTunnelRemoteVendorName_Type(DisplayString):
    """Custom type l2tpTunnelRemoteVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_L2tpTunnelRemoteVendorName_Type.__name__ = "DisplayString"
_L2tpTunnelRemoteVendorName_Object = MibTableColumn
l2tpTunnelRemoteVendorName = _L2tpTunnelRemoteVendorName_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 30, 10, 50),
    _L2tpTunnelRemoteVendorName_Type()
)
l2tpTunnelRemoteVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelRemoteVendorName.setStatus("mandatory")
_L2tpTunnelLocalIpAddress_Type = IpAddress
_L2tpTunnelLocalIpAddress_Object = MibTableColumn
l2tpTunnelLocalIpAddress = _L2tpTunnelLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 30, 10, 60),
    _L2tpTunnelLocalIpAddress_Type()
)
l2tpTunnelLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelLocalIpAddress.setStatus("mandatory")


class _L2tpTunnelLocalUdpPort_Type(Integer32):
    """Custom type l2tpTunnelLocalUdpPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpTunnelLocalUdpPort_Type.__name__ = "Integer32"
_L2tpTunnelLocalUdpPort_Object = MibTableColumn
l2tpTunnelLocalUdpPort = _L2tpTunnelLocalUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 30, 10, 70),
    _L2tpTunnelLocalUdpPort_Type()
)
l2tpTunnelLocalUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelLocalUdpPort.setStatus("mandatory")


class _L2tpTunnelLocalTunnelId_Type(Integer32):
    """Custom type l2tpTunnelLocalTunnelId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpTunnelLocalTunnelId_Type.__name__ = "Integer32"
_L2tpTunnelLocalTunnelId_Object = MibTableColumn
l2tpTunnelLocalTunnelId = _L2tpTunnelLocalTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 30, 10, 80),
    _L2tpTunnelLocalTunnelId_Type()
)
l2tpTunnelLocalTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelLocalTunnelId.setStatus("mandatory")


class _L2tpTunnelLocalReceiveWindowSize_Type(Integer32):
    """Custom type l2tpTunnelLocalReceiveWindowSize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_L2tpTunnelLocalReceiveWindowSize_Type.__name__ = "Integer32"
_L2tpTunnelLocalReceiveWindowSize_Object = MibTableColumn
l2tpTunnelLocalReceiveWindowSize = _L2tpTunnelLocalReceiveWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 30, 10, 85),
    _L2tpTunnelLocalReceiveWindowSize_Type()
)
l2tpTunnelLocalReceiveWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelLocalReceiveWindowSize.setStatus("mandatory")


class _L2tpTunnelLocalHostname_Type(DisplayString):
    """Custom type l2tpTunnelLocalHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_L2tpTunnelLocalHostname_Type.__name__ = "DisplayString"
_L2tpTunnelLocalHostname_Object = MibTableColumn
l2tpTunnelLocalHostname = _L2tpTunnelLocalHostname_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 30, 10, 90),
    _L2tpTunnelLocalHostname_Type()
)
l2tpTunnelLocalHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelLocalHostname.setStatus("mandatory")


class _L2tpTunnelPassword_Type(DisplayString):
    """Custom type l2tpTunnelPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_L2tpTunnelPassword_Type.__name__ = "DisplayString"
_L2tpTunnelPassword_Object = MibTableColumn
l2tpTunnelPassword = _L2tpTunnelPassword_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 30, 10, 100),
    _L2tpTunnelPassword_Type()
)
l2tpTunnelPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTunnelPassword.setStatus("mandatory")


class _L2tpTunnelHelloInterval_Type(Integer32):
    """Custom type l2tpTunnelHelloInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_L2tpTunnelHelloInterval_Type.__name__ = "Integer32"
_L2tpTunnelHelloInterval_Object = MibTableColumn
l2tpTunnelHelloInterval = _L2tpTunnelHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 30, 10, 120),
    _L2tpTunnelHelloInterval_Type()
)
l2tpTunnelHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelHelloInterval.setStatus("mandatory")


class _L2tpTunnelSessionDataSequencing_Type(Integer32):
    """Custom type l2tpTunnelSessionDataSequencing based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_L2tpTunnelSessionDataSequencing_Type.__name__ = "Integer32"
_L2tpTunnelSessionDataSequencing_Object = MibTableColumn
l2tpTunnelSessionDataSequencing = _L2tpTunnelSessionDataSequencing_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 30, 10, 130),
    _L2tpTunnelSessionDataSequencing_Type()
)
l2tpTunnelSessionDataSequencing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelSessionDataSequencing.setStatus("mandatory")


class _L2tpTunnelMinRetryTime_Type(Integer32):
    """Custom type l2tpTunnelMinRetryTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_L2tpTunnelMinRetryTime_Type.__name__ = "Integer32"
_L2tpTunnelMinRetryTime_Object = MibTableColumn
l2tpTunnelMinRetryTime = _L2tpTunnelMinRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 30, 10, 140),
    _L2tpTunnelMinRetryTime_Type()
)
l2tpTunnelMinRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelMinRetryTime.setStatus("mandatory")


class _L2tpTunnelMaxRetryTime_Type(Integer32):
    """Custom type l2tpTunnelMaxRetryTime based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 255),
    )


_L2tpTunnelMaxRetryTime_Type.__name__ = "Integer32"
_L2tpTunnelMaxRetryTime_Object = MibTableColumn
l2tpTunnelMaxRetryTime = _L2tpTunnelMaxRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 30, 10, 150),
    _L2tpTunnelMaxRetryTime_Type()
)
l2tpTunnelMaxRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelMaxRetryTime.setStatus("mandatory")


class _L2tpTunnelMaxRetries_Type(Integer32):
    """Custom type l2tpTunnelMaxRetries based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_L2tpTunnelMaxRetries_Type.__name__ = "Integer32"
_L2tpTunnelMaxRetries_Object = MibTableColumn
l2tpTunnelMaxRetries = _L2tpTunnelMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 30, 10, 160),
    _L2tpTunnelMaxRetries_Type()
)
l2tpTunnelMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelMaxRetries.setStatus("mandatory")


class _L2tpTunnelState_Type(Integer32):
    """Custom type l2tpTunnelState based on Integer32"""
    defaultValue = 1

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
        *(("established", 4),
          ("idle", 1),
          ("shutdown", 5),
          ("waitctlconn", 3),
          ("waitctlreply", 2))
    )


_L2tpTunnelState_Type.__name__ = "Integer32"
_L2tpTunnelState_Object = MibTableColumn
l2tpTunnelState = _L2tpTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 30, 10, 170),
    _L2tpTunnelState_Type()
)
l2tpTunnelState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTunnelState.setStatus("mandatory")
_L2tpSessionTable_Object = MibTable
l2tpSessionTable = _L2tpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 40)
)
if mibBuilder.loadTexts:
    l2tpSessionTable.setStatus("mandatory")
_L2tpSessionEntry_Object = MibTableRow
l2tpSessionEntry = _L2tpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 40, 10)
)
l2tpSessionEntry.setIndexNames(
    (0, "BIANCA-BRICK-L2TP-MIB", "l2tpSessionLocalSessionId"),
)
if mibBuilder.loadTexts:
    l2tpSessionEntry.setStatus("mandatory")
_L2tpSessionRemoteIpAddress_Type = IpAddress
_L2tpSessionRemoteIpAddress_Object = MibTableColumn
l2tpSessionRemoteIpAddress = _L2tpSessionRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 40, 10, 10),
    _L2tpSessionRemoteIpAddress_Type()
)
l2tpSessionRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionRemoteIpAddress.setStatus("mandatory")


class _L2tpSessionRemoteUdpPort_Type(Integer32):
    """Custom type l2tpSessionRemoteUdpPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpSessionRemoteUdpPort_Type.__name__ = "Integer32"
_L2tpSessionRemoteUdpPort_Object = MibTableColumn
l2tpSessionRemoteUdpPort = _L2tpSessionRemoteUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 40, 10, 20),
    _L2tpSessionRemoteUdpPort_Type()
)
l2tpSessionRemoteUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionRemoteUdpPort.setStatus("mandatory")


class _L2tpSessionRemoteTunnelId_Type(Integer32):
    """Custom type l2tpSessionRemoteTunnelId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpSessionRemoteTunnelId_Type.__name__ = "Integer32"
_L2tpSessionRemoteTunnelId_Object = MibTableColumn
l2tpSessionRemoteTunnelId = _L2tpSessionRemoteTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 40, 10, 30),
    _L2tpSessionRemoteTunnelId_Type()
)
l2tpSessionRemoteTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionRemoteTunnelId.setStatus("mandatory")


class _L2tpSessionRemoteSessionId_Type(Integer32):
    """Custom type l2tpSessionRemoteSessionId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpSessionRemoteSessionId_Type.__name__ = "Integer32"
_L2tpSessionRemoteSessionId_Object = MibTableColumn
l2tpSessionRemoteSessionId = _L2tpSessionRemoteSessionId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 40, 10, 40),
    _L2tpSessionRemoteSessionId_Type()
)
l2tpSessionRemoteSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionRemoteSessionId.setStatus("mandatory")


class _L2tpSessionRemoteHostname_Type(DisplayString):
    """Custom type l2tpSessionRemoteHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_L2tpSessionRemoteHostname_Type.__name__ = "DisplayString"
_L2tpSessionRemoteHostname_Object = MibTableColumn
l2tpSessionRemoteHostname = _L2tpSessionRemoteHostname_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 40, 10, 50),
    _L2tpSessionRemoteHostname_Type()
)
l2tpSessionRemoteHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionRemoteHostname.setStatus("mandatory")
_L2tpSessionLocalIpAddress_Type = IpAddress
_L2tpSessionLocalIpAddress_Object = MibTableColumn
l2tpSessionLocalIpAddress = _L2tpSessionLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 40, 10, 60),
    _L2tpSessionLocalIpAddress_Type()
)
l2tpSessionLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionLocalIpAddress.setStatus("mandatory")


class _L2tpSessionLocalUdpPort_Type(Integer32):
    """Custom type l2tpSessionLocalUdpPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpSessionLocalUdpPort_Type.__name__ = "Integer32"
_L2tpSessionLocalUdpPort_Object = MibTableColumn
l2tpSessionLocalUdpPort = _L2tpSessionLocalUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 40, 10, 70),
    _L2tpSessionLocalUdpPort_Type()
)
l2tpSessionLocalUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionLocalUdpPort.setStatus("mandatory")


class _L2tpSessionLocalTunnelId_Type(Integer32):
    """Custom type l2tpSessionLocalTunnelId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpSessionLocalTunnelId_Type.__name__ = "Integer32"
_L2tpSessionLocalTunnelId_Object = MibTableColumn
l2tpSessionLocalTunnelId = _L2tpSessionLocalTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 40, 10, 80),
    _L2tpSessionLocalTunnelId_Type()
)
l2tpSessionLocalTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionLocalTunnelId.setStatus("mandatory")


class _L2tpSessionLocalSessionId_Type(Integer32):
    """Custom type l2tpSessionLocalSessionId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpSessionLocalSessionId_Type.__name__ = "Integer32"
_L2tpSessionLocalSessionId_Object = MibTableColumn
l2tpSessionLocalSessionId = _L2tpSessionLocalSessionId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 40, 10, 90),
    _L2tpSessionLocalSessionId_Type()
)
l2tpSessionLocalSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionLocalSessionId.setStatus("mandatory")


class _L2tpSessionLocalHostname_Type(DisplayString):
    """Custom type l2tpSessionLocalHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_L2tpSessionLocalHostname_Type.__name__ = "DisplayString"
_L2tpSessionLocalHostname_Object = MibTableColumn
l2tpSessionLocalHostname = _L2tpSessionLocalHostname_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 40, 10, 100),
    _L2tpSessionLocalHostname_Type()
)
l2tpSessionLocalHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionLocalHostname.setStatus("mandatory")


class _L2tpSessionCallSerialNumber_Type(Integer32):
    """Custom type l2tpSessionCallSerialNumber based on Integer32"""
    defaultValue = 0


_L2tpSessionCallSerialNumber_Object = MibTableColumn
l2tpSessionCallSerialNumber = _L2tpSessionCallSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 40, 10, 110),
    _L2tpSessionCallSerialNumber_Type()
)
l2tpSessionCallSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionCallSerialNumber.setStatus("mandatory")


class _L2tpSessionDataSequencing_Type(Integer32):
    """Custom type l2tpSessionDataSequencing based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_L2tpSessionDataSequencing_Type.__name__ = "Integer32"
_L2tpSessionDataSequencing_Object = MibTableColumn
l2tpSessionDataSequencing = _L2tpSessionDataSequencing_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 40, 10, 120),
    _L2tpSessionDataSequencing_Type()
)
l2tpSessionDataSequencing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpSessionDataSequencing.setStatus("mandatory")


class _L2tpSessionState_Type(Integer32):
    """Custom type l2tpSessionState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("established", 6),
          ("idle", 1),
          ("shutdown", 7),
          ("waitconnect", 5),
          ("waitcsanswer", 3),
          ("waitreply", 4),
          ("waittunnel", 2))
    )


_L2tpSessionState_Type.__name__ = "Integer32"
_L2tpSessionState_Object = MibTableColumn
l2tpSessionState = _L2tpSessionState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 40, 10, 130),
    _L2tpSessionState_Type()
)
l2tpSessionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpSessionState.setStatus("mandatory")


class _L2tpSessionInfo_Type(DisplayString):
    """Custom type l2tpSessionInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_L2tpSessionInfo_Type.__name__ = "DisplayString"
_L2tpSessionInfo_Object = MibTableColumn
l2tpSessionInfo = _L2tpSessionInfo_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 40, 10, 140),
    _L2tpSessionInfo_Type()
)
l2tpSessionInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionInfo.setStatus("mandatory")


class _L2tpSessionClientPPPCrcErrors_Type(Integer32):
    """Custom type l2tpSessionClientPPPCrcErrors based on Integer32"""
    defaultValue = 0


_L2tpSessionClientPPPCrcErrors_Object = MibTableColumn
l2tpSessionClientPPPCrcErrors = _L2tpSessionClientPPPCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 40, 10, 150),
    _L2tpSessionClientPPPCrcErrors_Type()
)
l2tpSessionClientPPPCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionClientPPPCrcErrors.setStatus("mandatory")


class _L2tpSessionClientPPPFramingErrors_Type(Integer32):
    """Custom type l2tpSessionClientPPPFramingErrors based on Integer32"""
    defaultValue = 0


_L2tpSessionClientPPPFramingErrors_Object = MibTableColumn
l2tpSessionClientPPPFramingErrors = _L2tpSessionClientPPPFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 40, 10, 160),
    _L2tpSessionClientPPPFramingErrors_Type()
)
l2tpSessionClientPPPFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionClientPPPFramingErrors.setStatus("mandatory")


class _L2tpSessionClientPPPHardwareOverruns_Type(Integer32):
    """Custom type l2tpSessionClientPPPHardwareOverruns based on Integer32"""
    defaultValue = 0


_L2tpSessionClientPPPHardwareOverruns_Object = MibTableColumn
l2tpSessionClientPPPHardwareOverruns = _L2tpSessionClientPPPHardwareOverruns_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 40, 10, 170),
    _L2tpSessionClientPPPHardwareOverruns_Type()
)
l2tpSessionClientPPPHardwareOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionClientPPPHardwareOverruns.setStatus("mandatory")


class _L2tpSessionClientPPPBufferOverruns_Type(Integer32):
    """Custom type l2tpSessionClientPPPBufferOverruns based on Integer32"""
    defaultValue = 0


_L2tpSessionClientPPPBufferOverruns_Object = MibTableColumn
l2tpSessionClientPPPBufferOverruns = _L2tpSessionClientPPPBufferOverruns_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 40, 10, 180),
    _L2tpSessionClientPPPBufferOverruns_Type()
)
l2tpSessionClientPPPBufferOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionClientPPPBufferOverruns.setStatus("mandatory")


class _L2tpSessionClientPPPTimeoutErrors_Type(Integer32):
    """Custom type l2tpSessionClientPPPTimeoutErrors based on Integer32"""
    defaultValue = 0


_L2tpSessionClientPPPTimeoutErrors_Object = MibTableColumn
l2tpSessionClientPPPTimeoutErrors = _L2tpSessionClientPPPTimeoutErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 40, 10, 190),
    _L2tpSessionClientPPPTimeoutErrors_Type()
)
l2tpSessionClientPPPTimeoutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionClientPPPTimeoutErrors.setStatus("mandatory")


class _L2tpSessionClientPPPAlignmentErrors_Type(Integer32):
    """Custom type l2tpSessionClientPPPAlignmentErrors based on Integer32"""
    defaultValue = 0


_L2tpSessionClientPPPAlignmentErrors_Object = MibTableColumn
l2tpSessionClientPPPAlignmentErrors = _L2tpSessionClientPPPAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 23, 8, 40, 10, 200),
    _L2tpSessionClientPPPAlignmentErrors_Type()
)
l2tpSessionClientPPPAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionClientPPPAlignmentErrors.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-L2TP-MIB",
    **{"bintec": bintec,
       "bibo": bibo,
       "vpn": vpn,
       "l2tp": l2tp,
       "l2tpGlobals": l2tpGlobals,
       "l2tpGlobUdpPort": l2tpGlobUdpPort,
       "l2tpGlobPortUsage": l2tpGlobPortUsage,
       "l2tpTunnelProfileTable": l2tpTunnelProfileTable,
       "l2tpTunnelProfileEntry": l2tpTunnelProfileEntry,
       "l2tpTunnelProfileIndex": l2tpTunnelProfileIndex,
       "l2tpTunnelProfileName": l2tpTunnelProfileName,
       "l2tpTunnelProfileRemoteIpAddress": l2tpTunnelProfileRemoteIpAddress,
       "l2tpTunnelProfileRemoteIpAddressBackup": l2tpTunnelProfileRemoteIpAddressBackup,
       "l2tpTunnelProfileRemoteUdpPort": l2tpTunnelProfileRemoteUdpPort,
       "l2tpTunnelProfileRemoteHostname": l2tpTunnelProfileRemoteHostname,
       "l2tpTunnelProfileLocalIpAddress": l2tpTunnelProfileLocalIpAddress,
       "l2tpTunnelProfileLocalUdpPort": l2tpTunnelProfileLocalUdpPort,
       "l2tpTunnelProfileLocalHostname": l2tpTunnelProfileLocalHostname,
       "l2tpTunnelProfilePassword": l2tpTunnelProfilePassword,
       "l2tpTunnelProfileReceiveWindowSize": l2tpTunnelProfileReceiveWindowSize,
       "l2tpTunnelProfileHelloInterval": l2tpTunnelProfileHelloInterval,
       "l2tpTunnelProfileSessionDataSequencing": l2tpTunnelProfileSessionDataSequencing,
       "l2tpTunnelProfileMinRetryTime": l2tpTunnelProfileMinRetryTime,
       "l2tpTunnelProfileMaxRetryTime": l2tpTunnelProfileMaxRetryTime,
       "l2tpTunnelProfileMaxRetries": l2tpTunnelProfileMaxRetries,
       "l2tpTunnelProfileRadiusAssignment": l2tpTunnelProfileRadiusAssignment,
       "l2tpTunnelProfileRadiusGroupId": l2tpTunnelProfileRadiusGroupId,
       "l2tpTunnelTable": l2tpTunnelTable,
       "l2tpTunnelEntry": l2tpTunnelEntry,
       "l2tpTunnelRemoteIpAddress": l2tpTunnelRemoteIpAddress,
       "l2tpTunnelRemoteUdpPort": l2tpTunnelRemoteUdpPort,
       "l2tpTunnelRemoteTunnelId": l2tpTunnelRemoteTunnelId,
       "l2tpTunnelRemoteReceiveWindowSize": l2tpTunnelRemoteReceiveWindowSize,
       "l2tpTunnelRemoteHostname": l2tpTunnelRemoteHostname,
       "l2tpTunnelRemoteVendorName": l2tpTunnelRemoteVendorName,
       "l2tpTunnelLocalIpAddress": l2tpTunnelLocalIpAddress,
       "l2tpTunnelLocalUdpPort": l2tpTunnelLocalUdpPort,
       "l2tpTunnelLocalTunnelId": l2tpTunnelLocalTunnelId,
       "l2tpTunnelLocalReceiveWindowSize": l2tpTunnelLocalReceiveWindowSize,
       "l2tpTunnelLocalHostname": l2tpTunnelLocalHostname,
       "l2tpTunnelPassword": l2tpTunnelPassword,
       "l2tpTunnelHelloInterval": l2tpTunnelHelloInterval,
       "l2tpTunnelSessionDataSequencing": l2tpTunnelSessionDataSequencing,
       "l2tpTunnelMinRetryTime": l2tpTunnelMinRetryTime,
       "l2tpTunnelMaxRetryTime": l2tpTunnelMaxRetryTime,
       "l2tpTunnelMaxRetries": l2tpTunnelMaxRetries,
       "l2tpTunnelState": l2tpTunnelState,
       "l2tpSessionTable": l2tpSessionTable,
       "l2tpSessionEntry": l2tpSessionEntry,
       "l2tpSessionRemoteIpAddress": l2tpSessionRemoteIpAddress,
       "l2tpSessionRemoteUdpPort": l2tpSessionRemoteUdpPort,
       "l2tpSessionRemoteTunnelId": l2tpSessionRemoteTunnelId,
       "l2tpSessionRemoteSessionId": l2tpSessionRemoteSessionId,
       "l2tpSessionRemoteHostname": l2tpSessionRemoteHostname,
       "l2tpSessionLocalIpAddress": l2tpSessionLocalIpAddress,
       "l2tpSessionLocalUdpPort": l2tpSessionLocalUdpPort,
       "l2tpSessionLocalTunnelId": l2tpSessionLocalTunnelId,
       "l2tpSessionLocalSessionId": l2tpSessionLocalSessionId,
       "l2tpSessionLocalHostname": l2tpSessionLocalHostname,
       "l2tpSessionCallSerialNumber": l2tpSessionCallSerialNumber,
       "l2tpSessionDataSequencing": l2tpSessionDataSequencing,
       "l2tpSessionState": l2tpSessionState,
       "l2tpSessionInfo": l2tpSessionInfo,
       "l2tpSessionClientPPPCrcErrors": l2tpSessionClientPPPCrcErrors,
       "l2tpSessionClientPPPFramingErrors": l2tpSessionClientPPPFramingErrors,
       "l2tpSessionClientPPPHardwareOverruns": l2tpSessionClientPPPHardwareOverruns,
       "l2tpSessionClientPPPBufferOverruns": l2tpSessionClientPPPBufferOverruns,
       "l2tpSessionClientPPPTimeoutErrors": l2tpSessionClientPPPTimeoutErrors,
       "l2tpSessionClientPPPAlignmentErrors": l2tpSessionClientPPPAlignmentErrors}
)
