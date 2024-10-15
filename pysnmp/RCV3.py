# SNMP MIB module (RCV3) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RCV3
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:57 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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



class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )





class PbeShaEncryptedObject(OctetString):
    """Custom type PbeShaEncryptedObject based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RedCreek_ObjectIdentity = ObjectIdentity
redCreek = _RedCreek_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958, 1)
)
_RcRavlin_ObjectIdentity = ObjectIdentity
rcRavlin = _RcRavlin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1)
)
_RcAdmin_ObjectIdentity = ObjectIdentity
rcAdmin = _RcAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 1)
)
_RcSecure_ObjectIdentity = ObjectIdentity
rcSecure = _RcSecure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 2)
)
_RcBoot_ObjectIdentity = ObjectIdentity
rcBoot = _RcBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 3)
)
_RcStatus_ObjectIdentity = ObjectIdentity
rcStatus = _RcStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 4)
)
_RcTrap_ObjectIdentity = ObjectIdentity
rcTrap = _RcTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 5)
)
_RcDebug_ObjectIdentity = ObjectIdentity
rcDebug = _RcDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 6)
)
_RcEsp_ObjectIdentity = ObjectIdentity
rcEsp = _RcEsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 7)
)
_RcMgmt_ObjectIdentity = ObjectIdentity
rcMgmt = _RcMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8)
)
_Rc3System_ObjectIdentity = ObjectIdentity
rc3System = _Rc3System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 1)
)


class _Rc3BootRomVer_Type(DisplayString):
    """Custom type rc3BootRomVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_Rc3BootRomVer_Type.__name__ = "DisplayString"
_Rc3BootRomVer_Object = MibScalar
rc3BootRomVer = _Rc3BootRomVer_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 1, 1),
    _Rc3BootRomVer_Type()
)
rc3BootRomVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3BootRomVer.setStatus("mandatory")


class _Rc3FirmwareVer_Type(DisplayString):
    """Custom type rc3FirmwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_Rc3FirmwareVer_Type.__name__ = "DisplayString"
_Rc3FirmwareVer_Object = MibScalar
rc3FirmwareVer = _Rc3FirmwareVer_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 1, 2),
    _Rc3FirmwareVer_Type()
)
rc3FirmwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3FirmwareVer.setStatus("mandatory")


class _Rc3FirmwareID_Type(DisplayString):
    """Custom type rc3FirmwareID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Rc3FirmwareID_Type.__name__ = "DisplayString"
_Rc3FirmwareID_Object = MibScalar
rc3FirmwareID = _Rc3FirmwareID_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 1, 3),
    _Rc3FirmwareID_Type()
)
rc3FirmwareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3FirmwareID.setStatus("mandatory")


class _Rc3HardwareVer_Type(DisplayString):
    """Custom type rc3HardwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_Rc3HardwareVer_Type.__name__ = "DisplayString"
_Rc3HardwareVer_Object = MibScalar
rc3HardwareVer = _Rc3HardwareVer_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 1, 4),
    _Rc3HardwareVer_Type()
)
rc3HardwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3HardwareVer.setStatus("mandatory")
_Rc3DistinguishedName_Type = DisplayString
_Rc3DistinguishedName_Object = MibScalar
rc3DistinguishedName = _Rc3DistinguishedName_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 1, 5),
    _Rc3DistinguishedName_Type()
)
rc3DistinguishedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3DistinguishedName.setStatus("mandatory")


class _Rc3HostName_Type(DisplayString):
    """Custom type rc3HostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Rc3HostName_Type.__name__ = "DisplayString"
_Rc3HostName_Object = MibScalar
rc3HostName = _Rc3HostName_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 1, 6),
    _Rc3HostName_Type()
)
rc3HostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3HostName.setStatus("mandatory")
_Rc3Network_ObjectIdentity = ObjectIdentity
rc3Network = _Rc3Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 2)
)
_Rc3InterfaceTable_Object = MibTable
rc3InterfaceTable = _Rc3InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 2, 1)
)
if mibBuilder.loadTexts:
    rc3InterfaceTable.setStatus("mandatory")
_Rc3InterfaceEntry_Object = MibTableRow
rc3InterfaceEntry = _Rc3InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 2, 1, 1)
)
rc3InterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rc3InterfaceEntry.setStatus("mandatory")
_Rc3InterfaceIp_Type = IpAddress
_Rc3InterfaceIp_Object = MibTableColumn
rc3InterfaceIp = _Rc3InterfaceIp_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 2, 1, 1, 2),
    _Rc3InterfaceIp_Type()
)
rc3InterfaceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3InterfaceIp.setStatus("mandatory")
_Rc3InterfaceMask_Type = IpAddress
_Rc3InterfaceMask_Object = MibTableColumn
rc3InterfaceMask = _Rc3InterfaceMask_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 2, 1, 1, 3),
    _Rc3InterfaceMask_Type()
)
rc3InterfaceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3InterfaceMask.setStatus("mandatory")
_Rc3InterfaceMac_Type = OctetString
_Rc3InterfaceMac_Object = MibTableColumn
rc3InterfaceMac = _Rc3InterfaceMac_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 2, 1, 1, 4),
    _Rc3InterfaceMac_Type()
)
rc3InterfaceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3InterfaceMac.setStatus("mandatory")
_Rc3IpRouteTable_Object = MibTable
rc3IpRouteTable = _Rc3IpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 2, 2)
)
if mibBuilder.loadTexts:
    rc3IpRouteTable.setStatus("mandatory")
_Rc3IpRouteEntry_Object = MibTableRow
rc3IpRouteEntry = _Rc3IpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 2, 2, 1)
)
rc3IpRouteEntry.setIndexNames(
    (0, "RCV3", "rc3IpRouteDest"),
    (0, "RCV3", "rc3IpRouteMask"),
)
if mibBuilder.loadTexts:
    rc3IpRouteEntry.setStatus("mandatory")
_Rc3IpRouteDest_Type = IpAddress
_Rc3IpRouteDest_Object = MibTableColumn
rc3IpRouteDest = _Rc3IpRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 2, 2, 1, 1),
    _Rc3IpRouteDest_Type()
)
rc3IpRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rc3IpRouteDest.setStatus("mandatory")
_Rc3IpRouteMask_Type = IpAddress
_Rc3IpRouteMask_Object = MibTableColumn
rc3IpRouteMask = _Rc3IpRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 2, 2, 1, 2),
    _Rc3IpRouteMask_Type()
)
rc3IpRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rc3IpRouteMask.setStatus("mandatory")
_Rc3IpRouteIfIndex_Type = Integer32
_Rc3IpRouteIfIndex_Object = MibTableColumn
rc3IpRouteIfIndex = _Rc3IpRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 2, 2, 1, 3),
    _Rc3IpRouteIfIndex_Type()
)
rc3IpRouteIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3IpRouteIfIndex.setStatus("mandatory")
_Rc3IpRouteNextHop_Type = IpAddress
_Rc3IpRouteNextHop_Object = MibTableColumn
rc3IpRouteNextHop = _Rc3IpRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 2, 2, 1, 4),
    _Rc3IpRouteNextHop_Type()
)
rc3IpRouteNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3IpRouteNextHop.setStatus("mandatory")
_Rc3IpRouteMetric_Type = Integer32
_Rc3IpRouteMetric_Object = MibTableColumn
rc3IpRouteMetric = _Rc3IpRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 2, 2, 1, 5),
    _Rc3IpRouteMetric_Type()
)
rc3IpRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3IpRouteMetric.setStatus("mandatory")


class _Rc3IpRouteProto_Type(Integer32):
    """Custom type rc3IpRouteProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("bbnSpfIgp", 12),
          ("bgp", 14),
          ("ciscoIgrp", 11),
          ("egp", 5),
          ("es-is", 10),
          ("ggp", 6),
          ("hello", 7),
          ("icmp", 4),
          ("is-is", 9),
          ("local", 2),
          ("netmgmt", 3),
          ("ospf", 13),
          ("other", 1),
          ("rip", 8))
    )


_Rc3IpRouteProto_Type.__name__ = "Integer32"
_Rc3IpRouteProto_Object = MibTableColumn
rc3IpRouteProto = _Rc3IpRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 2, 2, 1, 6),
    _Rc3IpRouteProto_Type()
)
rc3IpRouteProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3IpRouteProto.setStatus("mandatory")
_Rc3IpRouteAge_Type = Integer32
_Rc3IpRouteAge_Object = MibTableColumn
rc3IpRouteAge = _Rc3IpRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 2, 2, 1, 7),
    _Rc3IpRouteAge_Type()
)
rc3IpRouteAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3IpRouteAge.setStatus("mandatory")
_Rc3IpRouteRowStatus_Type = RowStatus
_Rc3IpRouteRowStatus_Object = MibTableColumn
rc3IpRouteRowStatus = _Rc3IpRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 2, 2, 1, 8),
    _Rc3IpRouteRowStatus_Type()
)
rc3IpRouteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3IpRouteRowStatus.setStatus("mandatory")
_Rc3PacketHandlingOptions_Type = Integer32
_Rc3PacketHandlingOptions_Object = MibScalar
rc3PacketHandlingOptions = _Rc3PacketHandlingOptions_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 2, 3),
    _Rc3PacketHandlingOptions_Type()
)
rc3PacketHandlingOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PacketHandlingOptions.setStatus("mandatory")


class _Rc3PPPoEUserName_Type(DisplayString):
    """Custom type rc3PPPoEUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Rc3PPPoEUserName_Type.__name__ = "DisplayString"
_Rc3PPPoEUserName_Object = MibScalar
rc3PPPoEUserName = _Rc3PPPoEUserName_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 2, 4),
    _Rc3PPPoEUserName_Type()
)
rc3PPPoEUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PPPoEUserName.setStatus("mandatory")


class _Rc3PPPoEUserPassword_Type(DisplayString):
    """Custom type rc3PPPoEUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Rc3PPPoEUserPassword_Type.__name__ = "DisplayString"
_Rc3PPPoEUserPassword_Object = MibScalar
rc3PPPoEUserPassword = _Rc3PPPoEUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 2, 5),
    _Rc3PPPoEUserPassword_Type()
)
rc3PPPoEUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PPPoEUserPassword.setStatus("mandatory")


class _Rc3PPPoEServiceName_Type(DisplayString):
    """Custom type rc3PPPoEServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Rc3PPPoEServiceName_Type.__name__ = "DisplayString"
_Rc3PPPoEServiceName_Object = MibScalar
rc3PPPoEServiceName = _Rc3PPPoEServiceName_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 2, 6),
    _Rc3PPPoEServiceName_Type()
)
rc3PPPoEServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PPPoEServiceName.setStatus("mandatory")


class _Rc3PPPoEConcentratorName_Type(DisplayString):
    """Custom type rc3PPPoEConcentratorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Rc3PPPoEConcentratorName_Type.__name__ = "DisplayString"
_Rc3PPPoEConcentratorName_Object = MibScalar
rc3PPPoEConcentratorName = _Rc3PPPoEConcentratorName_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 2, 7),
    _Rc3PPPoEConcentratorName_Type()
)
rc3PPPoEConcentratorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PPPoEConcentratorName.setStatus("mandatory")
_Rc3PPPoEIdleTimeout_Type = Integer32
_Rc3PPPoEIdleTimeout_Object = MibScalar
rc3PPPoEIdleTimeout = _Rc3PPPoEIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 2, 8),
    _Rc3PPPoEIdleTimeout_Type()
)
rc3PPPoEIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PPPoEIdleTimeout.setStatus("mandatory")
_Rc3PPPoERetryCount_Type = Integer32
_Rc3PPPoERetryCount_Object = MibScalar
rc3PPPoERetryCount = _Rc3PPPoERetryCount_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 2, 9),
    _Rc3PPPoERetryCount_Type()
)
rc3PPPoERetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PPPoERetryCount.setStatus("mandatory")
_Rc3PPPoEDnsServer1_Type = IpAddress
_Rc3PPPoEDnsServer1_Object = MibScalar
rc3PPPoEDnsServer1 = _Rc3PPPoEDnsServer1_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 2, 10),
    _Rc3PPPoEDnsServer1_Type()
)
rc3PPPoEDnsServer1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3PPPoEDnsServer1.setStatus("mandatory")
_Rc3PPPoEDnsServer2_Type = IpAddress
_Rc3PPPoEDnsServer2_Object = MibScalar
rc3PPPoEDnsServer2 = _Rc3PPPoEDnsServer2_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 2, 11),
    _Rc3PPPoEDnsServer2_Type()
)
rc3PPPoEDnsServer2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3PPPoEDnsServer2.setStatus("mandatory")
_Rc3Control_ObjectIdentity = ObjectIdentity
rc3Control = _Rc3Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 3)
)


class _Rc3Reset_Type(Integer32):
    """Custom type rc3Reset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("clearARPcache", 4),
          ("clearallactiveSA", 3),
          ("clearmessagetable", 5),
          ("disablebox", 9),
          ("eraseflash", 8),
          ("other", 1),
          ("resettodefaults", 6),
          ("resettofactorydefaults", 7),
          ("warmstart", 2))
    )


_Rc3Reset_Type.__name__ = "Integer32"
_Rc3Reset_Object = MibScalar
rc3Reset = _Rc3Reset_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 3, 1),
    _Rc3Reset_Type()
)
rc3Reset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3Reset.setStatus("mandatory")
_Rc3ArpCacheCleanupInterval_Type = Integer32
_Rc3ArpCacheCleanupInterval_Object = MibScalar
rc3ArpCacheCleanupInterval = _Rc3ArpCacheCleanupInterval_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 3, 2),
    _Rc3ArpCacheCleanupInterval_Type()
)
rc3ArpCacheCleanupInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3ArpCacheCleanupInterval.setStatus("mandatory")


class _Rc3Password_Type(OctetString):
    """Custom type rc3Password based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Rc3Password_Type.__name__ = "OctetString"
_Rc3Password_Object = MibScalar
rc3Password = _Rc3Password_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 3, 3),
    _Rc3Password_Type()
)
rc3Password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3Password.setStatus("deprecated")


class _Rc3OperationalMode_Type(Integer32):
    """Custom type rc3OperationalMode based on Integer32"""
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
        *(("blockall", 2),
          ("passall", 1),
          ("standby", 4),
          ("vpnready", 3))
    )


_Rc3OperationalMode_Type.__name__ = "Integer32"
_Rc3OperationalMode_Object = MibScalar
rc3OperationalMode = _Rc3OperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 3, 4),
    _Rc3OperationalMode_Type()
)
rc3OperationalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3OperationalMode.setStatus("mandatory")
_Rc3InactiveClientTimeout_Type = Integer32
_Rc3InactiveClientTimeout_Object = MibScalar
rc3InactiveClientTimeout = _Rc3InactiveClientTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 3, 5),
    _Rc3InactiveClientTimeout_Type()
)
rc3InactiveClientTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3InactiveClientTimeout.setStatus("mandatory")
_Rc3DHCPServerIP_Type = IpAddress
_Rc3DHCPServerIP_Object = MibScalar
rc3DHCPServerIP = _Rc3DHCPServerIP_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 3, 6),
    _Rc3DHCPServerIP_Type()
)
rc3DHCPServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3DHCPServerIP.setStatus("mandatory")
_Rc3DHCPRequest_Type = Integer32
_Rc3DHCPRequest_Object = MibScalar
rc3DHCPRequest = _Rc3DHCPRequest_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 3, 7),
    _Rc3DHCPRequest_Type()
)
rc3DHCPRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3DHCPRequest.setStatus("mandatory")
_Rc3PasswordFips_Type = PbeShaEncryptedObject
_Rc3PasswordFips_Object = MibScalar
rc3PasswordFips = _Rc3PasswordFips_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 3, 8),
    _Rc3PasswordFips_Type()
)
rc3PasswordFips.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PasswordFips.setStatus("mandatory")
_Rc3DHCPRelayIpAddr_Type = IpAddress
_Rc3DHCPRelayIpAddr_Object = MibScalar
rc3DHCPRelayIpAddr = _Rc3DHCPRelayIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 3, 9),
    _Rc3DHCPRelayIpAddr_Type()
)
rc3DHCPRelayIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3DHCPRelayIpAddr.setStatus("mandatory")
_Rc3SysPerfTimeBetweenPolls_Type = Integer32
_Rc3SysPerfTimeBetweenPolls_Object = MibScalar
rc3SysPerfTimeBetweenPolls = _Rc3SysPerfTimeBetweenPolls_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 3, 10),
    _Rc3SysPerfTimeBetweenPolls_Type()
)
rc3SysPerfTimeBetweenPolls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3SysPerfTimeBetweenPolls.setStatus("mandatory")
_Rc3SysPerfTimeBetweenReports_Type = Integer32
_Rc3SysPerfTimeBetweenReports_Object = MibScalar
rc3SysPerfTimeBetweenReports = _Rc3SysPerfTimeBetweenReports_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 3, 11),
    _Rc3SysPerfTimeBetweenReports_Type()
)
rc3SysPerfTimeBetweenReports.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3SysPerfTimeBetweenReports.setStatus("mandatory")
_Rc3SysPerfTrapThreshold_Type = Integer32
_Rc3SysPerfTrapThreshold_Object = MibScalar
rc3SysPerfTrapThreshold = _Rc3SysPerfTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 3, 12),
    _Rc3SysPerfTrapThreshold_Type()
)
rc3SysPerfTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3SysPerfTrapThreshold.setStatus("mandatory")


class _Rc3DHCPBroadcastIntf_Type(Integer32):
    """Custom type rc3DHCPBroadcastIntf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("notApplicable", 3),
          ("remote", 2))
    )


_Rc3DHCPBroadcastIntf_Type.__name__ = "Integer32"
_Rc3DHCPBroadcastIntf_Object = MibScalar
rc3DHCPBroadcastIntf = _Rc3DHCPBroadcastIntf_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 3, 13),
    _Rc3DHCPBroadcastIntf_Type()
)
rc3DHCPBroadcastIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3DHCPBroadcastIntf.setStatus("mandatory")


class _Rc3StateLessDHCP_Type(Integer32):
    """Custom type rc3StateLessDHCP based on Integer32"""
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


_Rc3StateLessDHCP_Type.__name__ = "Integer32"
_Rc3StateLessDHCP_Object = MibScalar
rc3StateLessDHCP = _Rc3StateLessDHCP_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 3, 14),
    _Rc3StateLessDHCP_Type()
)
rc3StateLessDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3StateLessDHCP.setStatus("mandatory")
_Rc3Stat_ObjectIdentity = ObjectIdentity
rc3Stat = _Rc3Stat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 4)
)
_Rc3ActiveSAcount_Type = Integer32
_Rc3ActiveSAcount_Object = MibScalar
rc3ActiveSAcount = _Rc3ActiveSAcount_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 4, 1),
    _Rc3ActiveSAcount_Type()
)
rc3ActiveSAcount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3ActiveSAcount.setStatus("mandatory")
_Rc3PendingSAcount_Type = Integer32
_Rc3PendingSAcount_Object = MibScalar
rc3PendingSAcount = _Rc3PendingSAcount_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 4, 2),
    _Rc3PendingSAcount_Type()
)
rc3PendingSAcount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3PendingSAcount.setStatus("mandatory")
_Rc3SigFailCount_Type = Integer32
_Rc3SigFailCount_Object = MibScalar
rc3SigFailCount = _Rc3SigFailCount_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 4, 3),
    _Rc3SigFailCount_Type()
)
rc3SigFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3SigFailCount.setStatus("mandatory")
_Rc3StatusMsgTable_Object = MibTable
rc3StatusMsgTable = _Rc3StatusMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 4, 4)
)
if mibBuilder.loadTexts:
    rc3StatusMsgTable.setStatus("mandatory")
_Rc3StatusMsgEntry_Object = MibTableRow
rc3StatusMsgEntry = _Rc3StatusMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 4, 4, 1)
)
rc3StatusMsgEntry.setIndexNames(
    (0, "RCV3", "rc3StatusMsgIndex"),
)
if mibBuilder.loadTexts:
    rc3StatusMsgEntry.setStatus("mandatory")
_Rc3StatusMsgIndex_Type = Integer32
_Rc3StatusMsgIndex_Object = MibTableColumn
rc3StatusMsgIndex = _Rc3StatusMsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 4, 4, 1, 1),
    _Rc3StatusMsgIndex_Type()
)
rc3StatusMsgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rc3StatusMsgIndex.setStatus("mandatory")
_Rc3FirstInTimeStamp_Type = Integer32
_Rc3FirstInTimeStamp_Object = MibTableColumn
rc3FirstInTimeStamp = _Rc3FirstInTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 4, 4, 1, 2),
    _Rc3FirstInTimeStamp_Type()
)
rc3FirstInTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3FirstInTimeStamp.setStatus("mandatory")
_Rc3LastInTimeStamp_Type = Integer32
_Rc3LastInTimeStamp_Object = MibTableColumn
rc3LastInTimeStamp = _Rc3LastInTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 4, 4, 1, 3),
    _Rc3LastInTimeStamp_Type()
)
rc3LastInTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3LastInTimeStamp.setStatus("mandatory")
_Rc3EventCode_Type = Integer32
_Rc3EventCode_Object = MibTableColumn
rc3EventCode = _Rc3EventCode_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 4, 4, 1, 4),
    _Rc3EventCode_Type()
)
rc3EventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3EventCode.setStatus("mandatory")
_Rc3EventCodeRepetitions_Type = Integer32
_Rc3EventCodeRepetitions_Object = MibTableColumn
rc3EventCodeRepetitions = _Rc3EventCodeRepetitions_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 4, 4, 1, 5),
    _Rc3EventCodeRepetitions_Type()
)
rc3EventCodeRepetitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3EventCodeRepetitions.setStatus("mandatory")
_Rc3EventSpecificDescr1_Type = OctetString
_Rc3EventSpecificDescr1_Object = MibTableColumn
rc3EventSpecificDescr1 = _Rc3EventSpecificDescr1_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 4, 4, 1, 6),
    _Rc3EventSpecificDescr1_Type()
)
rc3EventSpecificDescr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3EventSpecificDescr1.setStatus("mandatory")
_Rc3EventSpecificDescr2_Type = OctetString
_Rc3EventSpecificDescr2_Object = MibTableColumn
rc3EventSpecificDescr2 = _Rc3EventSpecificDescr2_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 4, 4, 1, 7),
    _Rc3EventSpecificDescr2_Type()
)
rc3EventSpecificDescr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3EventSpecificDescr2.setStatus("mandatory")
_Rc3SysLogServerIP_Type = IpAddress
_Rc3SysLogServerIP_Object = MibScalar
rc3SysLogServerIP = _Rc3SysLogServerIP_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 4, 5),
    _Rc3SysLogServerIP_Type()
)
rc3SysLogServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3SysLogServerIP.setStatus("deprecated")
_Rc3SysLogPortNum_Type = Integer32
_Rc3SysLogPortNum_Object = MibScalar
rc3SysLogPortNum = _Rc3SysLogPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 4, 6),
    _Rc3SysLogPortNum_Type()
)
rc3SysLogPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3SysLogPortNum.setStatus("deprecated")


class _Rc3SysLogMsgLevel_Type(Integer32):
    """Custom type rc3SysLogMsgLevel based on Integer32"""
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
        *(("critical", 1),
          ("debug", 6),
          ("error", 3),
          ("invalid", 7),
          ("normal", 5),
          ("severe", 2),
          ("warning", 4))
    )


_Rc3SysLogMsgLevel_Type.__name__ = "Integer32"
_Rc3SysLogMsgLevel_Object = MibScalar
rc3SysLogMsgLevel = _Rc3SysLogMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 4, 7),
    _Rc3SysLogMsgLevel_Type()
)
rc3SysLogMsgLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3SysLogMsgLevel.setStatus("deprecated")
_Rc3SysLogServerTable_Object = MibTable
rc3SysLogServerTable = _Rc3SysLogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 4, 8)
)
if mibBuilder.loadTexts:
    rc3SysLogServerTable.setStatus("mandatory")
_Rc3SysLogServerEntry_Object = MibTableRow
rc3SysLogServerEntry = _Rc3SysLogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 4, 8, 1)
)
rc3SysLogServerEntry.setIndexNames(
    (0, "RCV3", "rc3SysLogServerIp"),
    (0, "RCV3", "rc3SysLogServerPort"),
)
if mibBuilder.loadTexts:
    rc3SysLogServerEntry.setStatus("mandatory")
_Rc3SysLogServerIp_Type = IpAddress
_Rc3SysLogServerIp_Object = MibTableColumn
rc3SysLogServerIp = _Rc3SysLogServerIp_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 4, 8, 1, 1),
    _Rc3SysLogServerIp_Type()
)
rc3SysLogServerIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rc3SysLogServerIp.setStatus("mandatory")
_Rc3SysLogServerPort_Type = Integer32
_Rc3SysLogServerPort_Object = MibTableColumn
rc3SysLogServerPort = _Rc3SysLogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 4, 8, 1, 2),
    _Rc3SysLogServerPort_Type()
)
rc3SysLogServerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rc3SysLogServerPort.setStatus("mandatory")


class _Rc3SysLogPriorityLevel_Type(Integer32):
    """Custom type rc3SysLogPriorityLevel based on Integer32"""
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
        *(("critical", 1),
          ("debug", 6),
          ("error", 3),
          ("normal", 5),
          ("severe", 2),
          ("warning", 4))
    )


_Rc3SysLogPriorityLevel_Type.__name__ = "Integer32"
_Rc3SysLogPriorityLevel_Object = MibTableColumn
rc3SysLogPriorityLevel = _Rc3SysLogPriorityLevel_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 4, 8, 1, 3),
    _Rc3SysLogPriorityLevel_Type()
)
rc3SysLogPriorityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3SysLogPriorityLevel.setStatus("mandatory")
_Rc3SysLogMsgStatus_Type = RowStatus
_Rc3SysLogMsgStatus_Object = MibTableColumn
rc3SysLogMsgStatus = _Rc3SysLogMsgStatus_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 4, 8, 1, 4),
    _Rc3SysLogMsgStatus_Type()
)
rc3SysLogMsgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3SysLogMsgStatus.setStatus("mandatory")
_Rc3Snmp_ObjectIdentity = ObjectIdentity
rc3Snmp = _Rc3Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 5)
)


class _Rc3ReadCommunityString_Type(DisplayString):
    """Custom type rc3ReadCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Rc3ReadCommunityString_Type.__name__ = "DisplayString"
_Rc3ReadCommunityString_Object = MibScalar
rc3ReadCommunityString = _Rc3ReadCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 5, 1),
    _Rc3ReadCommunityString_Type()
)
rc3ReadCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3ReadCommunityString.setStatus("deprecated")


class _Rc3WriteCommunityString_Type(DisplayString):
    """Custom type rc3WriteCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Rc3WriteCommunityString_Type.__name__ = "DisplayString"
_Rc3WriteCommunityString_Object = MibScalar
rc3WriteCommunityString = _Rc3WriteCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 5, 2),
    _Rc3WriteCommunityString_Type()
)
rc3WriteCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3WriteCommunityString.setStatus("deprecated")
_Rc3TrapRcvrTable_Object = MibTable
rc3TrapRcvrTable = _Rc3TrapRcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 5, 3)
)
if mibBuilder.loadTexts:
    rc3TrapRcvrTable.setStatus("mandatory")
_Rc3TrapRcvrEntry_Object = MibTableRow
rc3TrapRcvrEntry = _Rc3TrapRcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 5, 3, 1)
)
rc3TrapRcvrEntry.setIndexNames(
    (0, "RCV3", "rc3TrapRcvrIpAddr"),
)
if mibBuilder.loadTexts:
    rc3TrapRcvrEntry.setStatus("mandatory")
_Rc3TrapRcvrIpAddr_Type = IpAddress
_Rc3TrapRcvrIpAddr_Object = MibTableColumn
rc3TrapRcvrIpAddr = _Rc3TrapRcvrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 5, 3, 1, 1),
    _Rc3TrapRcvrIpAddr_Type()
)
rc3TrapRcvrIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rc3TrapRcvrIpAddr.setStatus("mandatory")


class _Rc3TrapRcvrComm_Type(OctetString):
    """Custom type rc3TrapRcvrComm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Rc3TrapRcvrComm_Type.__name__ = "OctetString"
_Rc3TrapRcvrComm_Object = MibTableColumn
rc3TrapRcvrComm = _Rc3TrapRcvrComm_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 5, 3, 1, 2),
    _Rc3TrapRcvrComm_Type()
)
rc3TrapRcvrComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3TrapRcvrComm.setStatus("mandatory")
_Rc3TrapRcvrType_Type = Integer32
_Rc3TrapRcvrType_Object = MibTableColumn
rc3TrapRcvrType = _Rc3TrapRcvrType_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 5, 3, 1, 3),
    _Rc3TrapRcvrType_Type()
)
rc3TrapRcvrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3TrapRcvrType.setStatus("mandatory")
_Rc3TrapRcvrStatus_Type = RowStatus
_Rc3TrapRcvrStatus_Object = MibTableColumn
rc3TrapRcvrStatus = _Rc3TrapRcvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 5, 3, 1, 4),
    _Rc3TrapRcvrStatus_Type()
)
rc3TrapRcvrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3TrapRcvrStatus.setStatus("mandatory")
_Rc3SnmpErrorCode_Type = Integer32
_Rc3SnmpErrorCode_Object = MibScalar
rc3SnmpErrorCode = _Rc3SnmpErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 5, 4),
    _Rc3SnmpErrorCode_Type()
)
rc3SnmpErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3SnmpErrorCode.setStatus("mandatory")
_Rc3ReadCommunityStringFips_Type = PbeShaEncryptedObject
_Rc3ReadCommunityStringFips_Object = MibScalar
rc3ReadCommunityStringFips = _Rc3ReadCommunityStringFips_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 5, 5),
    _Rc3ReadCommunityStringFips_Type()
)
rc3ReadCommunityStringFips.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3ReadCommunityStringFips.setStatus("mandatory")
_Rc3WriteCommunityStringFips_Type = PbeShaEncryptedObject
_Rc3WriteCommunityStringFips_Object = MibScalar
rc3WriteCommunityStringFips = _Rc3WriteCommunityStringFips_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 5, 6),
    _Rc3WriteCommunityStringFips_Type()
)
rc3WriteCommunityStringFips.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3WriteCommunityStringFips.setStatus("mandatory")
_Rc3ClientCfg_ObjectIdentity = ObjectIdentity
rc3ClientCfg = _Rc3ClientCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 6)
)


class _Rc3ClientAuthentication_Type(Integer32):
    """Custom type rc3ClientAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disableAuthentication", 2),
          ("enableLocal", 3),
          ("enableRadius", 1))
    )


_Rc3ClientAuthentication_Type.__name__ = "Integer32"
_Rc3ClientAuthentication_Object = MibScalar
rc3ClientAuthentication = _Rc3ClientAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 6, 1),
    _Rc3ClientAuthentication_Type()
)
rc3ClientAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3ClientAuthentication.setStatus("mandatory")
_Rc3ActiveRadiusServer_Type = IpAddress
_Rc3ActiveRadiusServer_Object = MibScalar
rc3ActiveRadiusServer = _Rc3ActiveRadiusServer_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 6, 2),
    _Rc3ActiveRadiusServer_Type()
)
rc3ActiveRadiusServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3ActiveRadiusServer.setStatus("mandatory")


class _Rc3RadiusPriority_Type(OctetString):
    """Custom type rc3RadiusPriority based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 3),
    )


_Rc3RadiusPriority_Type.__name__ = "OctetString"
_Rc3RadiusPriority_Object = MibScalar
rc3RadiusPriority = _Rc3RadiusPriority_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 6, 3),
    _Rc3RadiusPriority_Type()
)
rc3RadiusPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3RadiusPriority.setStatus("mandatory")
_Rc3RadiusAuthServerTable_Object = MibTable
rc3RadiusAuthServerTable = _Rc3RadiusAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 6, 4)
)
if mibBuilder.loadTexts:
    rc3RadiusAuthServerTable.setStatus("mandatory")
_Rc3RadiusAuthServerEntry_Object = MibTableRow
rc3RadiusAuthServerEntry = _Rc3RadiusAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 6, 4, 1)
)
rc3RadiusAuthServerEntry.setIndexNames(
    (0, "RCV3", "rc3RadiusAuthServerEntryIndx"),
)
if mibBuilder.loadTexts:
    rc3RadiusAuthServerEntry.setStatus("mandatory")


class _Rc3RadiusAuthServerEntryIndx_Type(Integer32):
    """Custom type rc3RadiusAuthServerEntryIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Rc3RadiusAuthServerEntryIndx_Type.__name__ = "Integer32"
_Rc3RadiusAuthServerEntryIndx_Object = MibTableColumn
rc3RadiusAuthServerEntryIndx = _Rc3RadiusAuthServerEntryIndx_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 6, 4, 1, 1),
    _Rc3RadiusAuthServerEntryIndx_Type()
)
rc3RadiusAuthServerEntryIndx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rc3RadiusAuthServerEntryIndx.setStatus("mandatory")
_Rc3RadiusAuthServerIP_Type = IpAddress
_Rc3RadiusAuthServerIP_Object = MibTableColumn
rc3RadiusAuthServerIP = _Rc3RadiusAuthServerIP_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 6, 4, 1, 2),
    _Rc3RadiusAuthServerIP_Type()
)
rc3RadiusAuthServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3RadiusAuthServerIP.setStatus("mandatory")
_Rc3RadiusAuthServerPort_Type = Integer32
_Rc3RadiusAuthServerPort_Object = MibTableColumn
rc3RadiusAuthServerPort = _Rc3RadiusAuthServerPort_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 6, 4, 1, 3),
    _Rc3RadiusAuthServerPort_Type()
)
rc3RadiusAuthServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3RadiusAuthServerPort.setStatus("mandatory")
_Rc3RadiusAttributeOffset_Type = Integer32
_Rc3RadiusAttributeOffset_Object = MibTableColumn
rc3RadiusAttributeOffset = _Rc3RadiusAttributeOffset_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 6, 4, 1, 4),
    _Rc3RadiusAttributeOffset_Type()
)
rc3RadiusAttributeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3RadiusAttributeOffset.setStatus("mandatory")
_Rc3RadiusAuthServerSharedSecret_Type = OctetString
_Rc3RadiusAuthServerSharedSecret_Object = MibTableColumn
rc3RadiusAuthServerSharedSecret = _Rc3RadiusAuthServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 6, 4, 1, 5),
    _Rc3RadiusAuthServerSharedSecret_Type()
)
rc3RadiusAuthServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3RadiusAuthServerSharedSecret.setStatus("deprecated")
_Rc3RadiusAuthServerRetries_Type = Integer32
_Rc3RadiusAuthServerRetries_Object = MibTableColumn
rc3RadiusAuthServerRetries = _Rc3RadiusAuthServerRetries_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 6, 4, 1, 6),
    _Rc3RadiusAuthServerRetries_Type()
)
rc3RadiusAuthServerRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3RadiusAuthServerRetries.setStatus("mandatory")
_Rc3RadiusAuthServerSharedSecretFips_Type = PbeShaEncryptedObject
_Rc3RadiusAuthServerSharedSecretFips_Object = MibTableColumn
rc3RadiusAuthServerSharedSecretFips = _Rc3RadiusAuthServerSharedSecretFips_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 6, 4, 1, 7),
    _Rc3RadiusAuthServerSharedSecretFips_Type()
)
rc3RadiusAuthServerSharedSecretFips.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3RadiusAuthServerSharedSecretFips.setStatus("mandatory")
_Rc3LocalAuthTable_Object = MibTable
rc3LocalAuthTable = _Rc3LocalAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 6, 5)
)
if mibBuilder.loadTexts:
    rc3LocalAuthTable.setStatus("mandatory")
_Rc3LocalAuthEntry_Object = MibTableRow
rc3LocalAuthEntry = _Rc3LocalAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 6, 5, 1)
)
rc3LocalAuthEntry.setIndexNames(
    (0, "RCV3", "rc3LocalAuthId"),
)
if mibBuilder.loadTexts:
    rc3LocalAuthEntry.setStatus("mandatory")
_Rc3LocalAuthId_Type = Integer32
_Rc3LocalAuthId_Object = MibTableColumn
rc3LocalAuthId = _Rc3LocalAuthId_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 6, 5, 1, 1),
    _Rc3LocalAuthId_Type()
)
rc3LocalAuthId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rc3LocalAuthId.setStatus("mandatory")


class _Rc3LocalAuthName_Type(DisplayString):
    """Custom type rc3LocalAuthName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Rc3LocalAuthName_Type.__name__ = "DisplayString"
_Rc3LocalAuthName_Object = MibTableColumn
rc3LocalAuthName = _Rc3LocalAuthName_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 6, 5, 1, 2),
    _Rc3LocalAuthName_Type()
)
rc3LocalAuthName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3LocalAuthName.setStatus("mandatory")
_Rc3LocalAuthPassword_Type = PbeShaEncryptedObject
_Rc3LocalAuthPassword_Object = MibTableColumn
rc3LocalAuthPassword = _Rc3LocalAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 6, 5, 1, 3),
    _Rc3LocalAuthPassword_Type()
)
rc3LocalAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3LocalAuthPassword.setStatus("mandatory")
_Rc3LocalAuthIpAddr_Type = IpAddress
_Rc3LocalAuthIpAddr_Object = MibTableColumn
rc3LocalAuthIpAddr = _Rc3LocalAuthIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 6, 5, 1, 4),
    _Rc3LocalAuthIpAddr_Type()
)
rc3LocalAuthIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3LocalAuthIpAddr.setStatus("mandatory")
_Rc3LocalAuthIpMask_Type = IpAddress
_Rc3LocalAuthIpMask_Object = MibTableColumn
rc3LocalAuthIpMask = _Rc3LocalAuthIpMask_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 6, 5, 1, 5),
    _Rc3LocalAuthIpMask_Type()
)
rc3LocalAuthIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3LocalAuthIpMask.setStatus("mandatory")
_Rc3LocalAuthRowStatus_Type = RowStatus
_Rc3LocalAuthRowStatus_Object = MibTableColumn
rc3LocalAuthRowStatus = _Rc3LocalAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 6, 5, 1, 6),
    _Rc3LocalAuthRowStatus_Type()
)
rc3LocalAuthRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3LocalAuthRowStatus.setStatus("mandatory")
_Rc3Download_ObjectIdentity = ObjectIdentity
rc3Download = _Rc3Download_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 7)
)
_Rc3ImageSize_Type = Integer32
_Rc3ImageSize_Object = MibScalar
rc3ImageSize = _Rc3ImageSize_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 7, 1),
    _Rc3ImageSize_Type()
)
rc3ImageSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3ImageSize.setStatus("mandatory")
_Rc3SoftwareBlock_Type = OctetString
_Rc3SoftwareBlock_Object = MibScalar
rc3SoftwareBlock = _Rc3SoftwareBlock_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 7, 2),
    _Rc3SoftwareBlock_Type()
)
rc3SoftwareBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3SoftwareBlock.setStatus("mandatory")
_Rc3SoftwareBlockNumber_Type = Integer32
_Rc3SoftwareBlockNumber_Object = MibScalar
rc3SoftwareBlockNumber = _Rc3SoftwareBlockNumber_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 7, 3),
    _Rc3SoftwareBlockNumber_Type()
)
rc3SoftwareBlockNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3SoftwareBlockNumber.setStatus("mandatory")
_Rc3Misc_ObjectIdentity = ObjectIdentity
rc3Misc = _Rc3Misc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 8)
)
_Rc3RandomNumber_Type = Integer32
_Rc3RandomNumber_Object = MibScalar
rc3RandomNumber = _Rc3RandomNumber_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 8, 1),
    _Rc3RandomNumber_Type()
)
rc3RandomNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3RandomNumber.setStatus("mandatory")
_Rc3HashObject_Type = OctetString
_Rc3HashObject_Object = MibScalar
rc3HashObject = _Rc3HashObject_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 8, 2),
    _Rc3HashObject_Type()
)
rc3HashObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3HashObject.setStatus("mandatory")
_Rc3UlaAuthenticationTimer_Type = Integer32
_Rc3UlaAuthenticationTimer_Object = MibScalar
rc3UlaAuthenticationTimer = _Rc3UlaAuthenticationTimer_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 8, 3),
    _Rc3UlaAuthenticationTimer_Type()
)
rc3UlaAuthenticationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3UlaAuthenticationTimer.setStatus("mandatory")
_Rc3UlaAuthenticationPort_Type = Integer32
_Rc3UlaAuthenticationPort_Object = MibScalar
rc3UlaAuthenticationPort = _Rc3UlaAuthenticationPort_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 8, 4),
    _Rc3UlaAuthenticationPort_Type()
)
rc3UlaAuthenticationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3UlaAuthenticationPort.setStatus("mandatory")
_Rc3SystemTime_Type = Integer32
_Rc3SystemTime_Object = MibScalar
rc3SystemTime = _Rc3SystemTime_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 8, 5),
    _Rc3SystemTime_Type()
)
rc3SystemTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3SystemTime.setStatus("mandatory")
_Rc3Cert_ObjectIdentity = ObjectIdentity
rc3Cert = _Rc3Cert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 9)
)
_Rc3CACertTable_Object = MibTable
rc3CACertTable = _Rc3CACertTable_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 9, 1)
)
if mibBuilder.loadTexts:
    rc3CACertTable.setStatus("mandatory")
_Rc3CACertEntry_Object = MibTableRow
rc3CACertEntry = _Rc3CACertEntry_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 9, 1, 1)
)
rc3CACertEntry.setIndexNames(
    (0, "RCV3", "rc3CACertIndex"),
)
if mibBuilder.loadTexts:
    rc3CACertEntry.setStatus("mandatory")
_Rc3CACertIndex_Type = Integer32
_Rc3CACertIndex_Object = MibTableColumn
rc3CACertIndex = _Rc3CACertIndex_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 9, 1, 1, 1),
    _Rc3CACertIndex_Type()
)
rc3CACertIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rc3CACertIndex.setStatus("mandatory")


class _Rc3CACertName_Type(DisplayString):
    """Custom type rc3CACertName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Rc3CACertName_Type.__name__ = "DisplayString"
_Rc3CACertName_Object = MibTableColumn
rc3CACertName = _Rc3CACertName_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 9, 1, 1, 2),
    _Rc3CACertName_Type()
)
rc3CACertName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3CACertName.setStatus("mandatory")
_Rc3CACertData_Type = OctetString
_Rc3CACertData_Object = MibTableColumn
rc3CACertData = _Rc3CACertData_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 9, 1, 1, 3),
    _Rc3CACertData_Type()
)
rc3CACertData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3CACertData.setStatus("mandatory")
_Rc3CACertStatus_Type = RowStatus
_Rc3CACertStatus_Object = MibTableColumn
rc3CACertStatus = _Rc3CACertStatus_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 9, 1, 1, 4),
    _Rc3CACertStatus_Type()
)
rc3CACertStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3CACertStatus.setStatus("mandatory")
_Rc3UserCertTable_Object = MibTable
rc3UserCertTable = _Rc3UserCertTable_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 9, 2)
)
if mibBuilder.loadTexts:
    rc3UserCertTable.setStatus("mandatory")
_Rc3UserCertEntry_Object = MibTableRow
rc3UserCertEntry = _Rc3UserCertEntry_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 9, 2, 1)
)
rc3UserCertEntry.setIndexNames(
    (0, "RCV3", "rc3UserCertIndex"),
)
if mibBuilder.loadTexts:
    rc3UserCertEntry.setStatus("mandatory")
_Rc3UserCertIndex_Type = Integer32
_Rc3UserCertIndex_Object = MibTableColumn
rc3UserCertIndex = _Rc3UserCertIndex_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 9, 2, 1, 1),
    _Rc3UserCertIndex_Type()
)
rc3UserCertIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rc3UserCertIndex.setStatus("mandatory")
_Rc3UserCertName_Type = OctetString
_Rc3UserCertName_Object = MibTableColumn
rc3UserCertName = _Rc3UserCertName_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 9, 2, 1, 2),
    _Rc3UserCertName_Type()
)
rc3UserCertName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3UserCertName.setStatus("mandatory")
_Rc3UserCertData_Type = OctetString
_Rc3UserCertData_Object = MibTableColumn
rc3UserCertData = _Rc3UserCertData_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 9, 2, 1, 3),
    _Rc3UserCertData_Type()
)
rc3UserCertData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3UserCertData.setStatus("mandatory")
_Rc3UserCertStatus_Type = RowStatus
_Rc3UserCertStatus_Object = MibTableColumn
rc3UserCertStatus = _Rc3UserCertStatus_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 9, 2, 1, 4),
    _Rc3UserCertStatus_Type()
)
rc3UserCertStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3UserCertStatus.setStatus("mandatory")
_Rc3UserCertRDN_Type = OctetString
_Rc3UserCertRDN_Object = MibScalar
rc3UserCertRDN = _Rc3UserCertRDN_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 9, 3),
    _Rc3UserCertRDN_Type()
)
rc3UserCertRDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3UserCertRDN.setStatus("mandatory")
_Rc3UserCertAlgoId_Type = Integer32
_Rc3UserCertAlgoId_Object = MibScalar
rc3UserCertAlgoId = _Rc3UserCertAlgoId_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 9, 4),
    _Rc3UserCertAlgoId_Type()
)
rc3UserCertAlgoId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3UserCertAlgoId.setStatus("mandatory")
_Rc3GenerateKeyPair_Type = Integer32
_Rc3GenerateKeyPair_Object = MibScalar
rc3GenerateKeyPair = _Rc3GenerateKeyPair_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 9, 5),
    _Rc3GenerateKeyPair_Type()
)
rc3GenerateKeyPair.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3GenerateKeyPair.setStatus("mandatory")
_Rc3UserCertGetPkcs10_Type = OctetString
_Rc3UserCertGetPkcs10_Object = MibScalar
rc3UserCertGetPkcs10 = _Rc3UserCertGetPkcs10_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 8, 9, 6),
    _Rc3UserCertGetPkcs10_Type()
)
rc3UserCertGetPkcs10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3UserCertGetPkcs10.setStatus("mandatory")
_RcPolicy_ObjectIdentity = ObjectIdentity
rcPolicy = _RcPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9)
)
_Rc3Proposals_ObjectIdentity = ObjectIdentity
rc3Proposals = _Rc3Proposals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 1)
)
_Rc3IsakmpProposalTable_Object = MibTable
rc3IsakmpProposalTable = _Rc3IsakmpProposalTable_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    rc3IsakmpProposalTable.setStatus("mandatory")
_Rc3IsakmpProposalEntry_Object = MibTableRow
rc3IsakmpProposalEntry = _Rc3IsakmpProposalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 1, 1, 1)
)
rc3IsakmpProposalEntry.setIndexNames(
    (0, "RCV3", "rc3IsakmpProposalIndx"),
)
if mibBuilder.loadTexts:
    rc3IsakmpProposalEntry.setStatus("mandatory")
_Rc3IsakmpProposalIndx_Type = Integer32
_Rc3IsakmpProposalIndx_Object = MibTableColumn
rc3IsakmpProposalIndx = _Rc3IsakmpProposalIndx_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 1, 1, 1, 1),
    _Rc3IsakmpProposalIndx_Type()
)
rc3IsakmpProposalIndx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rc3IsakmpProposalIndx.setStatus("mandatory")


class _Rc3IsakmpProposalEncryption_Type(Integer32):
    """Custom type rc3IsakmpProposalEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              249)
        )
    )
    namedValues = NamedValues(
        *(("des-cbc", 1),
          ("des-cbc-40", 249),
          ("triple-des-cbc", 5))
    )


_Rc3IsakmpProposalEncryption_Type.__name__ = "Integer32"
_Rc3IsakmpProposalEncryption_Object = MibTableColumn
rc3IsakmpProposalEncryption = _Rc3IsakmpProposalEncryption_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 1, 1, 1, 2),
    _Rc3IsakmpProposalEncryption_Type()
)
rc3IsakmpProposalEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3IsakmpProposalEncryption.setStatus("mandatory")


class _Rc3IsakmpProposalHash_Type(Integer32):
    """Custom type rc3IsakmpProposalHash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha", 2))
    )


_Rc3IsakmpProposalHash_Type.__name__ = "Integer32"
_Rc3IsakmpProposalHash_Object = MibTableColumn
rc3IsakmpProposalHash = _Rc3IsakmpProposalHash_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 1, 1, 1, 3),
    _Rc3IsakmpProposalHash_Type()
)
rc3IsakmpProposalHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3IsakmpProposalHash.setStatus("mandatory")


class _Rc3IsakmpProposalAuthMode_Type(Integer32):
    """Custom type rc3IsakmpProposalAuthMode based on Integer32"""
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
        *(("dss-signature", 2),
          ("pre-sharedkey", 1),
          ("rsa-encryption", 4),
          ("rsa-signature", 3))
    )


_Rc3IsakmpProposalAuthMode_Type.__name__ = "Integer32"
_Rc3IsakmpProposalAuthMode_Object = MibTableColumn
rc3IsakmpProposalAuthMode = _Rc3IsakmpProposalAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 1, 1, 1, 4),
    _Rc3IsakmpProposalAuthMode_Type()
)
rc3IsakmpProposalAuthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3IsakmpProposalAuthMode.setStatus("mandatory")


class _Rc3IsakmpProposalDhGroup_Type(Integer32):
    """Custom type rc3IsakmpProposalDhGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("group", 2),
          ("group1", 1))
    )


_Rc3IsakmpProposalDhGroup_Type.__name__ = "Integer32"
_Rc3IsakmpProposalDhGroup_Object = MibTableColumn
rc3IsakmpProposalDhGroup = _Rc3IsakmpProposalDhGroup_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 1, 1, 1, 5),
    _Rc3IsakmpProposalDhGroup_Type()
)
rc3IsakmpProposalDhGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3IsakmpProposalDhGroup.setStatus("mandatory")
_Rc3EspProposalTable_Object = MibTable
rc3EspProposalTable = _Rc3EspProposalTable_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    rc3EspProposalTable.setStatus("mandatory")
_Rc3EspProposalEntry_Object = MibTableRow
rc3EspProposalEntry = _Rc3EspProposalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 1, 2, 1)
)
rc3EspProposalEntry.setIndexNames(
    (0, "RCV3", "rc3EspProposalIndx"),
)
if mibBuilder.loadTexts:
    rc3EspProposalEntry.setStatus("mandatory")
_Rc3EspProposalIndx_Type = Integer32
_Rc3EspProposalIndx_Object = MibTableColumn
rc3EspProposalIndx = _Rc3EspProposalIndx_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 1, 2, 1, 1),
    _Rc3EspProposalIndx_Type()
)
rc3EspProposalIndx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rc3EspProposalIndx.setStatus("mandatory")


class _Rc3EspProposalCipherAlgo_Type(Integer32):
    """Custom type rc3EspProposalCipherAlgo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              249)
        )
    )
    namedValues = NamedValues(
        *(("esp-3des", 3),
          ("esp-40des", 249),
          ("esp-des", 2),
          ("esp-null", 0))
    )


_Rc3EspProposalCipherAlgo_Type.__name__ = "Integer32"
_Rc3EspProposalCipherAlgo_Object = MibTableColumn
rc3EspProposalCipherAlgo = _Rc3EspProposalCipherAlgo_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 1, 2, 1, 2),
    _Rc3EspProposalCipherAlgo_Type()
)
rc3EspProposalCipherAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3EspProposalCipherAlgo.setStatus("mandatory")


class _Rc3EspProposalEncapsulation_Type(Integer32):
    """Custom type rc3EspProposalEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transport", 2),
          ("tunnel", 1))
    )


_Rc3EspProposalEncapsulation_Type.__name__ = "Integer32"
_Rc3EspProposalEncapsulation_Object = MibTableColumn
rc3EspProposalEncapsulation = _Rc3EspProposalEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 1, 2, 1, 3),
    _Rc3EspProposalEncapsulation_Type()
)
rc3EspProposalEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3EspProposalEncapsulation.setStatus("mandatory")


class _Rc3EspProposalAuth_Type(Integer32):
    """Custom type rc3EspProposalAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("des-mac", 3),
          ("hmac-md5", 1),
          ("hmac-sha-1", 2),
          ("no-auth", 0))
    )


_Rc3EspProposalAuth_Type.__name__ = "Integer32"
_Rc3EspProposalAuth_Object = MibTableColumn
rc3EspProposalAuth = _Rc3EspProposalAuth_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 1, 2, 1, 4),
    _Rc3EspProposalAuth_Type()
)
rc3EspProposalAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3EspProposalAuth.setStatus("mandatory")


class _Rc3EspProposalGroup_Type(Integer32):
    """Custom type rc3EspProposalGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("group", 2),
          ("group1", 1))
    )


_Rc3EspProposalGroup_Type.__name__ = "Integer32"
_Rc3EspProposalGroup_Object = MibTableColumn
rc3EspProposalGroup = _Rc3EspProposalGroup_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 1, 2, 1, 5),
    _Rc3EspProposalGroup_Type()
)
rc3EspProposalGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3EspProposalGroup.setStatus("deprecated")
_Rc3AhProposalTable_Object = MibTable
rc3AhProposalTable = _Rc3AhProposalTable_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 1, 3)
)
if mibBuilder.loadTexts:
    rc3AhProposalTable.setStatus("mandatory")
_Rc3AhProposalEntry_Object = MibTableRow
rc3AhProposalEntry = _Rc3AhProposalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 1, 3, 1)
)
rc3AhProposalEntry.setIndexNames(
    (0, "RCV3", "rc3AhProposalIndx"),
)
if mibBuilder.loadTexts:
    rc3AhProposalEntry.setStatus("mandatory")
_Rc3AhProposalIndx_Type = Integer32
_Rc3AhProposalIndx_Object = MibTableColumn
rc3AhProposalIndx = _Rc3AhProposalIndx_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 1, 3, 1, 1),
    _Rc3AhProposalIndx_Type()
)
rc3AhProposalIndx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rc3AhProposalIndx.setStatus("mandatory")


class _Rc3AhProposalAuth_Type(Integer32):
    """Custom type rc3AhProposalAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ah-md5", 2),
          ("ah-sha", 3),
          ("reserved", 1))
    )


_Rc3AhProposalAuth_Type.__name__ = "Integer32"
_Rc3AhProposalAuth_Object = MibTableColumn
rc3AhProposalAuth = _Rc3AhProposalAuth_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 1, 3, 1, 2),
    _Rc3AhProposalAuth_Type()
)
rc3AhProposalAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3AhProposalAuth.setStatus("mandatory")


class _Rc3AhProposalEncapsulation_Type(Integer32):
    """Custom type rc3AhProposalEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transport", 2),
          ("tunnel", 1))
    )


_Rc3AhProposalEncapsulation_Type.__name__ = "Integer32"
_Rc3AhProposalEncapsulation_Object = MibTableColumn
rc3AhProposalEncapsulation = _Rc3AhProposalEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 1, 3, 1, 3),
    _Rc3AhProposalEncapsulation_Type()
)
rc3AhProposalEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3AhProposalEncapsulation.setStatus("mandatory")


class _Rc3AhProposalGroup_Type(Integer32):
    """Custom type rc3AhProposalGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("group", 2),
          ("group1", 1))
    )


_Rc3AhProposalGroup_Type.__name__ = "Integer32"
_Rc3AhProposalGroup_Object = MibTableColumn
rc3AhProposalGroup = _Rc3AhProposalGroup_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 1, 3, 1, 4),
    _Rc3AhProposalGroup_Type()
)
rc3AhProposalGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3AhProposalGroup.setStatus("deprecated")
_Rc3EipProposalTable_Object = MibTable
rc3EipProposalTable = _Rc3EipProposalTable_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 1, 4)
)
if mibBuilder.loadTexts:
    rc3EipProposalTable.setStatus("deprecated")
_Rc3EipProposalEntry_Object = MibTableRow
rc3EipProposalEntry = _Rc3EipProposalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 1, 4, 1)
)
rc3EipProposalEntry.setIndexNames(
    (0, "RCV3", "rc3EipProposalIndx"),
)
if mibBuilder.loadTexts:
    rc3EipProposalEntry.setStatus("deprecated")
_Rc3EipProposalIndx_Type = Integer32
_Rc3EipProposalIndx_Object = MibTableColumn
rc3EipProposalIndx = _Rc3EipProposalIndx_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 1, 4, 1, 1),
    _Rc3EipProposalIndx_Type()
)
rc3EipProposalIndx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rc3EipProposalIndx.setStatus("deprecated")


class _Rc3EipProposalCipherAlgo_Type(Integer32):
    """Custom type rc3EipProposalCipherAlgo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              249)
        )
    )
    namedValues = NamedValues(
        *(("eip-3des", 3),
          ("eip-40des", 249),
          ("eip-des", 2))
    )


_Rc3EipProposalCipherAlgo_Type.__name__ = "Integer32"
_Rc3EipProposalCipherAlgo_Object = MibTableColumn
rc3EipProposalCipherAlgo = _Rc3EipProposalCipherAlgo_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 1, 4, 1, 2),
    _Rc3EipProposalCipherAlgo_Type()
)
rc3EipProposalCipherAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3EipProposalCipherAlgo.setStatus("deprecated")
_Rc3Pde_ObjectIdentity = ObjectIdentity
rc3Pde = _Rc3Pde_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2)
)
_Rc3PdePeerInfoTable_Object = MibTable
rc3PdePeerInfoTable = _Rc3PdePeerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 1)
)
if mibBuilder.loadTexts:
    rc3PdePeerInfoTable.setStatus("mandatory")
_Rc3PdePeerInfoEntry_Object = MibTableRow
rc3PdePeerInfoEntry = _Rc3PdePeerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 1, 1)
)
rc3PdePeerInfoEntry.setIndexNames(
    (0, "RCV3", "rc3PdePeerIndx"),
)
if mibBuilder.loadTexts:
    rc3PdePeerInfoEntry.setStatus("mandatory")
_Rc3PdePeerIndx_Type = Integer32
_Rc3PdePeerIndx_Object = MibTableColumn
rc3PdePeerIndx = _Rc3PdePeerIndx_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 1, 1, 1),
    _Rc3PdePeerIndx_Type()
)
rc3PdePeerIndx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rc3PdePeerIndx.setStatus("mandatory")


class _Rc3PdePeerType_Type(Integer32):
    """Custom type rc3PdePeerType based on Integer32"""
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
        *(("bypassboth", 3),
          ("bypassoutbound", 4),
          ("gateway", 2),
          ("host", 1))
    )


_Rc3PdePeerType_Type.__name__ = "Integer32"
_Rc3PdePeerType_Object = MibTableColumn
rc3PdePeerType = _Rc3PdePeerType_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 1, 1, 2),
    _Rc3PdePeerType_Type()
)
rc3PdePeerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdePeerType.setStatus("mandatory")
_Rc3PdePeerAddr_Type = IpAddress
_Rc3PdePeerAddr_Object = MibTableColumn
rc3PdePeerAddr = _Rc3PdePeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 1, 1, 3),
    _Rc3PdePeerAddr_Type()
)
rc3PdePeerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdePeerAddr.setStatus("mandatory")
_Rc3PdePeerDN_Type = OctetString
_Rc3PdePeerDN_Object = MibTableColumn
rc3PdePeerDN = _Rc3PdePeerDN_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 1, 1, 4),
    _Rc3PdePeerDN_Type()
)
rc3PdePeerDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdePeerDN.setStatus("mandatory")
_Rc3PdePeerIssuerDN_Type = OctetString
_Rc3PdePeerIssuerDN_Object = MibTableColumn
rc3PdePeerIssuerDN = _Rc3PdePeerIssuerDN_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 1, 1, 5),
    _Rc3PdePeerIssuerDN_Type()
)
rc3PdePeerIssuerDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdePeerIssuerDN.setStatus("deprecated")
_Rc3PdePeerLocalCertIndx_Type = Integer32
_Rc3PdePeerLocalCertIndx_Object = MibTableColumn
rc3PdePeerLocalCertIndx = _Rc3PdePeerLocalCertIndx_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 1, 1, 6),
    _Rc3PdePeerLocalCertIndx_Type()
)
rc3PdePeerLocalCertIndx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdePeerLocalCertIndx.setStatus("mandatory")


class _Rc3PdePeerKeyMgmtType_Type(Integer32):
    """Custom type rc3PdePeerKeyMgmtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isakmp", 2),
          ("manual", 1))
    )


_Rc3PdePeerKeyMgmtType_Type.__name__ = "Integer32"
_Rc3PdePeerKeyMgmtType_Object = MibTableColumn
rc3PdePeerKeyMgmtType = _Rc3PdePeerKeyMgmtType_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 1, 1, 7),
    _Rc3PdePeerKeyMgmtType_Type()
)
rc3PdePeerKeyMgmtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdePeerKeyMgmtType.setStatus("mandatory")
_Rc3PdePeerKeyMgmtIndx_Type = Integer32
_Rc3PdePeerKeyMgmtIndx_Object = MibTableColumn
rc3PdePeerKeyMgmtIndx = _Rc3PdePeerKeyMgmtIndx_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 1, 1, 8),
    _Rc3PdePeerKeyMgmtIndx_Type()
)
rc3PdePeerKeyMgmtIndx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdePeerKeyMgmtIndx.setStatus("mandatory")
_Rc3PdePeerIpsecProtocolIndx_Type = Integer32
_Rc3PdePeerIpsecProtocolIndx_Object = MibTableColumn
rc3PdePeerIpsecProtocolIndx = _Rc3PdePeerIpsecProtocolIndx_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 1, 1, 9),
    _Rc3PdePeerIpsecProtocolIndx_Type()
)
rc3PdePeerIpsecProtocolIndx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdePeerIpsecProtocolIndx.setStatus("mandatory")


class _Rc3PdePeerIfIndex_Type(Integer32):
    """Custom type rc3PdePeerIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("remote", 3))
    )


_Rc3PdePeerIfIndex_Type.__name__ = "Integer32"
_Rc3PdePeerIfIndex_Object = MibTableColumn
rc3PdePeerIfIndex = _Rc3PdePeerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 1, 1, 10),
    _Rc3PdePeerIfIndex_Type()
)
rc3PdePeerIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdePeerIfIndex.setStatus("mandatory")
_Rc3PdePeerNextHop_Type = IpAddress
_Rc3PdePeerNextHop_Object = MibTableColumn
rc3PdePeerNextHop = _Rc3PdePeerNextHop_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 1, 1, 11),
    _Rc3PdePeerNextHop_Type()
)
rc3PdePeerNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdePeerNextHop.setStatus("mandatory")


class _Rc3PdePeerContinue_Type(Integer32):
    """Custom type rc3PdePeerContinue based on Integer32"""
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


_Rc3PdePeerContinue_Type.__name__ = "Integer32"
_Rc3PdePeerContinue_Object = MibTableColumn
rc3PdePeerContinue = _Rc3PdePeerContinue_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 1, 1, 12),
    _Rc3PdePeerContinue_Type()
)
rc3PdePeerContinue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdePeerContinue.setStatus("deprecated")


class _Rc3PdePeerIsakmpLifeType_Type(Integer32):
    """Custom type rc3PdePeerIsakmpLifeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("seconds", 1)
    )


_Rc3PdePeerIsakmpLifeType_Type.__name__ = "Integer32"
_Rc3PdePeerIsakmpLifeType_Object = MibTableColumn
rc3PdePeerIsakmpLifeType = _Rc3PdePeerIsakmpLifeType_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 1, 1, 13),
    _Rc3PdePeerIsakmpLifeType_Type()
)
rc3PdePeerIsakmpLifeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdePeerIsakmpLifeType.setStatus("mandatory")
_Rc3PdePeerIsakmpLifeTimeSeconds_Type = Integer32
_Rc3PdePeerIsakmpLifeTimeSeconds_Object = MibTableColumn
rc3PdePeerIsakmpLifeTimeSeconds = _Rc3PdePeerIsakmpLifeTimeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 1, 1, 14),
    _Rc3PdePeerIsakmpLifeTimeSeconds_Type()
)
rc3PdePeerIsakmpLifeTimeSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdePeerIsakmpLifeTimeSeconds.setStatus("mandatory")
_Rc3PdePeerIsakmpLifeTimeKiloBytes_Type = Integer32
_Rc3PdePeerIsakmpLifeTimeKiloBytes_Object = MibTableColumn
rc3PdePeerIsakmpLifeTimeKiloBytes = _Rc3PdePeerIsakmpLifeTimeKiloBytes_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 1, 1, 15),
    _Rc3PdePeerIsakmpLifeTimeKiloBytes_Type()
)
rc3PdePeerIsakmpLifeTimeKiloBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdePeerIsakmpLifeTimeKiloBytes.setStatus("mandatory")


class _Rc3PdePeerIpsecLifeType_Type(Integer32):
    """Custom type rc3PdePeerIpsecLifeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("seconds", 1)
    )


_Rc3PdePeerIpsecLifeType_Type.__name__ = "Integer32"
_Rc3PdePeerIpsecLifeType_Object = MibTableColumn
rc3PdePeerIpsecLifeType = _Rc3PdePeerIpsecLifeType_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 1, 1, 16),
    _Rc3PdePeerIpsecLifeType_Type()
)
rc3PdePeerIpsecLifeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdePeerIpsecLifeType.setStatus("mandatory")
_Rc3PdePeerIpsecLifeTimeSeconds_Type = Integer32
_Rc3PdePeerIpsecLifeTimeSeconds_Object = MibTableColumn
rc3PdePeerIpsecLifeTimeSeconds = _Rc3PdePeerIpsecLifeTimeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 1, 1, 17),
    _Rc3PdePeerIpsecLifeTimeSeconds_Type()
)
rc3PdePeerIpsecLifeTimeSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdePeerIpsecLifeTimeSeconds.setStatus("mandatory")
_Rc3PdePeerIpsecLifeTimeKiloBytes_Type = Integer32
_Rc3PdePeerIpsecLifeTimeKiloBytes_Object = MibTableColumn
rc3PdePeerIpsecLifeTimeKiloBytes = _Rc3PdePeerIpsecLifeTimeKiloBytes_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 1, 1, 18),
    _Rc3PdePeerIpsecLifeTimeKiloBytes_Type()
)
rc3PdePeerIpsecLifeTimeKiloBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdePeerIpsecLifeTimeKiloBytes.setStatus("mandatory")
_Rc3PdePeerRowStatus_Type = RowStatus
_Rc3PdePeerRowStatus_Object = MibTableColumn
rc3PdePeerRowStatus = _Rc3PdePeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 1, 1, 19),
    _Rc3PdePeerRowStatus_Type()
)
rc3PdePeerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdePeerRowStatus.setStatus("mandatory")
_Rc3PdeFilterProtocol_Type = Integer32
_Rc3PdeFilterProtocol_Object = MibTableColumn
rc3PdeFilterProtocol = _Rc3PdeFilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 1, 1, 20),
    _Rc3PdeFilterProtocol_Type()
)
rc3PdeFilterProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdeFilterProtocol.setStatus("deprecated")
_Rc3PdeLocalPort_Type = Integer32
_Rc3PdeLocalPort_Object = MibTableColumn
rc3PdeLocalPort = _Rc3PdeLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 1, 1, 21),
    _Rc3PdeLocalPort_Type()
)
rc3PdeLocalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdeLocalPort.setStatus("deprecated")
_Rc3PdeRemotePort_Type = Integer32
_Rc3PdeRemotePort_Object = MibTableColumn
rc3PdeRemotePort = _Rc3PdeRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 1, 1, 22),
    _Rc3PdeRemotePort_Type()
)
rc3PdeRemotePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdeRemotePort.setStatus("deprecated")


class _Rc3PdeName_Type(DisplayString):
    """Custom type rc3PdeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_Rc3PdeName_Type.__name__ = "DisplayString"
_Rc3PdeName_Object = MibTableColumn
rc3PdeName = _Rc3PdeName_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 1, 1, 23),
    _Rc3PdeName_Type()
)
rc3PdeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdeName.setStatus("mandatory")


class _Rc3PdeULA_Type(Integer32):
    """Custom type rc3PdeULA based on Integer32"""
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


_Rc3PdeULA_Type.__name__ = "Integer32"
_Rc3PdeULA_Object = MibTableColumn
rc3PdeULA = _Rc3PdeULA_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 1, 1, 24),
    _Rc3PdeULA_Type()
)
rc3PdeULA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdeULA.setStatus("mandatory")
_Rc3PdePeerLocalInterfaceIpAddr_Type = IpAddress
_Rc3PdePeerLocalInterfaceIpAddr_Object = MibTableColumn
rc3PdePeerLocalInterfaceIpAddr = _Rc3PdePeerLocalInterfaceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 1, 1, 25),
    _Rc3PdePeerLocalInterfaceIpAddr_Type()
)
rc3PdePeerLocalInterfaceIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdePeerLocalInterfaceIpAddr.setStatus("mandatory")
_Rc3PdeLocalNetworkTable_Object = MibTable
rc3PdeLocalNetworkTable = _Rc3PdeLocalNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 2)
)
if mibBuilder.loadTexts:
    rc3PdeLocalNetworkTable.setStatus("mandatory")
_Rc3PdeLocalNetworkEntry_Object = MibTableRow
rc3PdeLocalNetworkEntry = _Rc3PdeLocalNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 2, 1)
)
rc3PdeLocalNetworkEntry.setIndexNames(
    (0, "RCV3", "rc3PdePeerIndx"),
    (0, "RCV3", "rc3PdeLocalNetworkNumber"),
    (0, "RCV3", "rc3PdeLocalNetworkMask"),
)
if mibBuilder.loadTexts:
    rc3PdeLocalNetworkEntry.setStatus("mandatory")
_Rc3PdeLocalNetworkNumber_Type = IpAddress
_Rc3PdeLocalNetworkNumber_Object = MibTableColumn
rc3PdeLocalNetworkNumber = _Rc3PdeLocalNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 2, 1, 1),
    _Rc3PdeLocalNetworkNumber_Type()
)
rc3PdeLocalNetworkNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rc3PdeLocalNetworkNumber.setStatus("mandatory")
_Rc3PdeLocalNetworkMask_Type = IpAddress
_Rc3PdeLocalNetworkMask_Object = MibTableColumn
rc3PdeLocalNetworkMask = _Rc3PdeLocalNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 2, 1, 2),
    _Rc3PdeLocalNetworkMask_Type()
)
rc3PdeLocalNetworkMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rc3PdeLocalNetworkMask.setStatus("mandatory")
_Rc3PdeLocalNetworkRowStatus_Type = RowStatus
_Rc3PdeLocalNetworkRowStatus_Object = MibTableColumn
rc3PdeLocalNetworkRowStatus = _Rc3PdeLocalNetworkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 2, 1, 3),
    _Rc3PdeLocalNetworkRowStatus_Type()
)
rc3PdeLocalNetworkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdeLocalNetworkRowStatus.setStatus("mandatory")
_Rc3PdeRemoteNetworkTable_Object = MibTable
rc3PdeRemoteNetworkTable = _Rc3PdeRemoteNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 3)
)
if mibBuilder.loadTexts:
    rc3PdeRemoteNetworkTable.setStatus("mandatory")
_Rc3PdeRemoteNetworkEntry_Object = MibTableRow
rc3PdeRemoteNetworkEntry = _Rc3PdeRemoteNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 3, 1)
)
rc3PdeRemoteNetworkEntry.setIndexNames(
    (0, "RCV3", "rc3PdePeerIndx"),
    (0, "RCV3", "rc3PdeRemoteNetworkNumber"),
    (0, "RCV3", "rc3PdeRemoteNetworkMask"),
)
if mibBuilder.loadTexts:
    rc3PdeRemoteNetworkEntry.setStatus("mandatory")
_Rc3PdeRemoteNetworkNumber_Type = IpAddress
_Rc3PdeRemoteNetworkNumber_Object = MibTableColumn
rc3PdeRemoteNetworkNumber = _Rc3PdeRemoteNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 3, 1, 1),
    _Rc3PdeRemoteNetworkNumber_Type()
)
rc3PdeRemoteNetworkNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rc3PdeRemoteNetworkNumber.setStatus("mandatory")
_Rc3PdeRemoteNetworkMask_Type = IpAddress
_Rc3PdeRemoteNetworkMask_Object = MibTableColumn
rc3PdeRemoteNetworkMask = _Rc3PdeRemoteNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 3, 1, 2),
    _Rc3PdeRemoteNetworkMask_Type()
)
rc3PdeRemoteNetworkMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rc3PdeRemoteNetworkMask.setStatus("mandatory")
_Rc3PdeRemoteNetworkRowStatus_Type = RowStatus
_Rc3PdeRemoteNetworkRowStatus_Object = MibTableColumn
rc3PdeRemoteNetworkRowStatus = _Rc3PdeRemoteNetworkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 3, 1, 3),
    _Rc3PdeRemoteNetworkRowStatus_Type()
)
rc3PdeRemoteNetworkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdeRemoteNetworkRowStatus.setStatus("mandatory")
_Rc3SAStatTable_Object = MibTable
rc3SAStatTable = _Rc3SAStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 4)
)
if mibBuilder.loadTexts:
    rc3SAStatTable.setStatus("mandatory")
_Rc3SAStatEntry_Object = MibTableRow
rc3SAStatEntry = _Rc3SAStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 4, 1)
)
rc3SAStatEntry.setIndexNames(
    (0, "RCV3", "rc3PdePeerIndx"),
    (0, "RCV3", "rc3SAStatPeerAddr"),
)
if mibBuilder.loadTexts:
    rc3SAStatEntry.setStatus("mandatory")
_Rc3SAStatPeerAddr_Type = IpAddress
_Rc3SAStatPeerAddr_Object = MibTableColumn
rc3SAStatPeerAddr = _Rc3SAStatPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 4, 1, 1),
    _Rc3SAStatPeerAddr_Type()
)
rc3SAStatPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rc3SAStatPeerAddr.setStatus("mandatory")


class _Rc3SAStatConnStatus_Type(Integer32):
    """Custom type rc3SAStatConnStatus based on Integer32"""
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
        *(("active", 2),
          ("block", 5),
          ("failed", 4),
          ("inactive", 1),
          ("pending", 3),
          ("rebuild", 6))
    )


_Rc3SAStatConnStatus_Type.__name__ = "Integer32"
_Rc3SAStatConnStatus_Object = MibTableColumn
rc3SAStatConnStatus = _Rc3SAStatConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 4, 1, 2),
    _Rc3SAStatConnStatus_Type()
)
rc3SAStatConnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3SAStatConnStatus.setStatus("mandatory")
_Rc3SAStatCreateTime_Type = Integer32
_Rc3SAStatCreateTime_Object = MibTableColumn
rc3SAStatCreateTime = _Rc3SAStatCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 4, 1, 3),
    _Rc3SAStatCreateTime_Type()
)
rc3SAStatCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3SAStatCreateTime.setStatus("mandatory")
_Rc3SAStatEncryptPktCount_Type = Counter32
_Rc3SAStatEncryptPktCount_Object = MibTableColumn
rc3SAStatEncryptPktCount = _Rc3SAStatEncryptPktCount_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 4, 1, 4),
    _Rc3SAStatEncryptPktCount_Type()
)
rc3SAStatEncryptPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3SAStatEncryptPktCount.setStatus("mandatory")
_Rc3SAStatEncryptByteCount_Type = Counter32
_Rc3SAStatEncryptByteCount_Object = MibTableColumn
rc3SAStatEncryptByteCount = _Rc3SAStatEncryptByteCount_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 4, 1, 5),
    _Rc3SAStatEncryptByteCount_Type()
)
rc3SAStatEncryptByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3SAStatEncryptByteCount.setStatus("mandatory")
_Rc3SAStatDecryptPktCount_Type = Counter32
_Rc3SAStatDecryptPktCount_Object = MibTableColumn
rc3SAStatDecryptPktCount = _Rc3SAStatDecryptPktCount_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 4, 1, 6),
    _Rc3SAStatDecryptPktCount_Type()
)
rc3SAStatDecryptPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3SAStatDecryptPktCount.setStatus("mandatory")
_Rc3SAStatDecryptByteCount_Type = Counter32
_Rc3SAStatDecryptByteCount_Object = MibTableColumn
rc3SAStatDecryptByteCount = _Rc3SAStatDecryptByteCount_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 4, 1, 7),
    _Rc3SAStatDecryptByteCount_Type()
)
rc3SAStatDecryptByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3SAStatDecryptByteCount.setStatus("mandatory")
_Rc3SAStatFragPktCount_Type = Counter32
_Rc3SAStatFragPktCount_Object = MibTableColumn
rc3SAStatFragPktCount = _Rc3SAStatFragPktCount_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 4, 1, 8),
    _Rc3SAStatFragPktCount_Type()
)
rc3SAStatFragPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3SAStatFragPktCount.setStatus("mandatory")


class _Rc3SAStatReset_Type(Integer32):
    """Custom type rc3SAStatReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_Rc3SAStatReset_Type.__name__ = "Integer32"
_Rc3SAStatReset_Object = MibTableColumn
rc3SAStatReset = _Rc3SAStatReset_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 4, 1, 9),
    _Rc3SAStatReset_Type()
)
rc3SAStatReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3SAStatReset.setStatus("mandatory")
_Rc3SAStatUserName_Type = DisplayString
_Rc3SAStatUserName_Object = MibTableColumn
rc3SAStatUserName = _Rc3SAStatUserName_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 4, 1, 10),
    _Rc3SAStatUserName_Type()
)
rc3SAStatUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3SAStatUserName.setStatus("mandatory")
_Rc3SAStatPollsSent_Type = Counter32
_Rc3SAStatPollsSent_Object = MibTableColumn
rc3SAStatPollsSent = _Rc3SAStatPollsSent_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 4, 1, 11),
    _Rc3SAStatPollsSent_Type()
)
rc3SAStatPollsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3SAStatPollsSent.setStatus("mandatory")
_Rc3SAStatPollsReceived_Type = Counter32
_Rc3SAStatPollsReceived_Object = MibTableColumn
rc3SAStatPollsReceived = _Rc3SAStatPollsReceived_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 4, 1, 12),
    _Rc3SAStatPollsReceived_Type()
)
rc3SAStatPollsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3SAStatPollsReceived.setStatus("mandatory")
_Rc3SAStatPollsAverageTime_Type = Integer32
_Rc3SAStatPollsAverageTime_Object = MibTableColumn
rc3SAStatPollsAverageTime = _Rc3SAStatPollsAverageTime_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 4, 1, 13),
    _Rc3SAStatPollsAverageTime_Type()
)
rc3SAStatPollsAverageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3SAStatPollsAverageTime.setStatus("mandatory")
_Rc3SAStatPollsMaxTime_Type = Integer32
_Rc3SAStatPollsMaxTime_Object = MibTableColumn
rc3SAStatPollsMaxTime = _Rc3SAStatPollsMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 4, 1, 14),
    _Rc3SAStatPollsMaxTime_Type()
)
rc3SAStatPollsMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3SAStatPollsMaxTime.setStatus("mandatory")
_Rc3SAStatPollsMinTime_Type = Integer32
_Rc3SAStatPollsMinTime_Object = MibTableColumn
rc3SAStatPollsMinTime = _Rc3SAStatPollsMinTime_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 4, 1, 15),
    _Rc3SAStatPollsMinTime_Type()
)
rc3SAStatPollsMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3SAStatPollsMinTime.setStatus("mandatory")
_Rc3PdeManualKeyMgmtTable_Object = MibTable
rc3PdeManualKeyMgmtTable = _Rc3PdeManualKeyMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 5)
)
if mibBuilder.loadTexts:
    rc3PdeManualKeyMgmtTable.setStatus("mandatory")
_Rc3PdeManualKeyMgmtEntry_Object = MibTableRow
rc3PdeManualKeyMgmtEntry = _Rc3PdeManualKeyMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 5, 1)
)
rc3PdeManualKeyMgmtEntry.setIndexNames(
    (0, "RCV3", "rc3PdeManualKeyMgmtIndx"),
)
if mibBuilder.loadTexts:
    rc3PdeManualKeyMgmtEntry.setStatus("mandatory")
_Rc3PdeManualKeyMgmtIndx_Type = Integer32
_Rc3PdeManualKeyMgmtIndx_Object = MibTableColumn
rc3PdeManualKeyMgmtIndx = _Rc3PdeManualKeyMgmtIndx_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 5, 1, 1),
    _Rc3PdeManualKeyMgmtIndx_Type()
)
rc3PdeManualKeyMgmtIndx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rc3PdeManualKeyMgmtIndx.setStatus("mandatory")
_Rc3PdeManualInboundEncryptKey_Type = OctetString
_Rc3PdeManualInboundEncryptKey_Object = MibTableColumn
rc3PdeManualInboundEncryptKey = _Rc3PdeManualInboundEncryptKey_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 5, 1, 2),
    _Rc3PdeManualInboundEncryptKey_Type()
)
rc3PdeManualInboundEncryptKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdeManualInboundEncryptKey.setStatus("deprecated")
_Rc3PdeManualOutboundEncryptKey_Type = OctetString
_Rc3PdeManualOutboundEncryptKey_Object = MibTableColumn
rc3PdeManualOutboundEncryptKey = _Rc3PdeManualOutboundEncryptKey_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 5, 1, 3),
    _Rc3PdeManualOutboundEncryptKey_Type()
)
rc3PdeManualOutboundEncryptKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdeManualOutboundEncryptKey.setStatus("deprecated")
_Rc3PdeManualInboundAuthKey_Type = OctetString
_Rc3PdeManualInboundAuthKey_Object = MibTableColumn
rc3PdeManualInboundAuthKey = _Rc3PdeManualInboundAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 5, 1, 4),
    _Rc3PdeManualInboundAuthKey_Type()
)
rc3PdeManualInboundAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdeManualInboundAuthKey.setStatus("deprecated")
_Rc3PdeManualOutboundAuthKey_Type = OctetString
_Rc3PdeManualOutboundAuthKey_Object = MibTableColumn
rc3PdeManualOutboundAuthKey = _Rc3PdeManualOutboundAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 5, 1, 5),
    _Rc3PdeManualOutboundAuthKey_Type()
)
rc3PdeManualOutboundAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdeManualOutboundAuthKey.setStatus("deprecated")
_Rc3PdeManualInboundSpi_Type = Integer32
_Rc3PdeManualInboundSpi_Object = MibTableColumn
rc3PdeManualInboundSpi = _Rc3PdeManualInboundSpi_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 5, 1, 6),
    _Rc3PdeManualInboundSpi_Type()
)
rc3PdeManualInboundSpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdeManualInboundSpi.setStatus("mandatory")
_Rc3PdeManualOutboundSpi_Type = Integer32
_Rc3PdeManualOutboundSpi_Object = MibTableColumn
rc3PdeManualOutboundSpi = _Rc3PdeManualOutboundSpi_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 5, 1, 7),
    _Rc3PdeManualOutboundSpi_Type()
)
rc3PdeManualOutboundSpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdeManualOutboundSpi.setStatus("mandatory")
_Rc3PdeManualKeyMgmtRowStatus_Type = RowStatus
_Rc3PdeManualKeyMgmtRowStatus_Object = MibTableColumn
rc3PdeManualKeyMgmtRowStatus = _Rc3PdeManualKeyMgmtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 5, 1, 8),
    _Rc3PdeManualKeyMgmtRowStatus_Type()
)
rc3PdeManualKeyMgmtRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdeManualKeyMgmtRowStatus.setStatus("mandatory")
_Rc3PdeManualInboundEncryptKeyFips_Type = PbeShaEncryptedObject
_Rc3PdeManualInboundEncryptKeyFips_Object = MibTableColumn
rc3PdeManualInboundEncryptKeyFips = _Rc3PdeManualInboundEncryptKeyFips_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 5, 1, 9),
    _Rc3PdeManualInboundEncryptKeyFips_Type()
)
rc3PdeManualInboundEncryptKeyFips.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdeManualInboundEncryptKeyFips.setStatus("mandatory")
_Rc3PdeManualOutboundEncryptKeyFips_Type = PbeShaEncryptedObject
_Rc3PdeManualOutboundEncryptKeyFips_Object = MibTableColumn
rc3PdeManualOutboundEncryptKeyFips = _Rc3PdeManualOutboundEncryptKeyFips_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 5, 1, 10),
    _Rc3PdeManualOutboundEncryptKeyFips_Type()
)
rc3PdeManualOutboundEncryptKeyFips.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdeManualOutboundEncryptKeyFips.setStatus("mandatory")
_Rc3PdeManualInboundAuthKeyFips_Type = PbeShaEncryptedObject
_Rc3PdeManualInboundAuthKeyFips_Object = MibTableColumn
rc3PdeManualInboundAuthKeyFips = _Rc3PdeManualInboundAuthKeyFips_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 5, 1, 11),
    _Rc3PdeManualInboundAuthKeyFips_Type()
)
rc3PdeManualInboundAuthKeyFips.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdeManualInboundAuthKeyFips.setStatus("mandatory")
_Rc3PdeManualOutboundAuthKeyFips_Type = PbeShaEncryptedObject
_Rc3PdeManualOutboundAuthKeyFips_Object = MibTableColumn
rc3PdeManualOutboundAuthKeyFips = _Rc3PdeManualOutboundAuthKeyFips_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 5, 1, 12),
    _Rc3PdeManualOutboundAuthKeyFips_Type()
)
rc3PdeManualOutboundAuthKeyFips.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdeManualOutboundAuthKeyFips.setStatus("mandatory")
_Rc3PdeIsakmpKeyMgmtTable_Object = MibTable
rc3PdeIsakmpKeyMgmtTable = _Rc3PdeIsakmpKeyMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 6)
)
if mibBuilder.loadTexts:
    rc3PdeIsakmpKeyMgmtTable.setStatus("mandatory")
_Rc3PdeIsakmpKeyMgmtEntry_Object = MibTableRow
rc3PdeIsakmpKeyMgmtEntry = _Rc3PdeIsakmpKeyMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 6, 1)
)
rc3PdeIsakmpKeyMgmtEntry.setIndexNames(
    (0, "RCV3", "rc3PdeIsakmpIndx"),
)
if mibBuilder.loadTexts:
    rc3PdeIsakmpKeyMgmtEntry.setStatus("mandatory")
_Rc3PdeIsakmpIndx_Type = Integer32
_Rc3PdeIsakmpIndx_Object = MibTableColumn
rc3PdeIsakmpIndx = _Rc3PdeIsakmpIndx_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 6, 1, 1),
    _Rc3PdeIsakmpIndx_Type()
)
rc3PdeIsakmpIndx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rc3PdeIsakmpIndx.setStatus("mandatory")


class _Rc3PdeIsakmpProposals_Type(OctetString):
    """Custom type rc3PdeIsakmpProposals based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Rc3PdeIsakmpProposals_Type.__name__ = "OctetString"
_Rc3PdeIsakmpProposals_Object = MibTableColumn
rc3PdeIsakmpProposals = _Rc3PdeIsakmpProposals_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 6, 1, 2),
    _Rc3PdeIsakmpProposals_Type()
)
rc3PdeIsakmpProposals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdeIsakmpProposals.setStatus("mandatory")
_Rc3PdeIsakmpRetries_Type = Integer32
_Rc3PdeIsakmpRetries_Object = MibTableColumn
rc3PdeIsakmpRetries = _Rc3PdeIsakmpRetries_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 6, 1, 3),
    _Rc3PdeIsakmpRetries_Type()
)
rc3PdeIsakmpRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdeIsakmpRetries.setStatus("mandatory")
_Rc3PdeIsakmpAuthPresharedKey_Type = OctetString
_Rc3PdeIsakmpAuthPresharedKey_Object = MibTableColumn
rc3PdeIsakmpAuthPresharedKey = _Rc3PdeIsakmpAuthPresharedKey_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 6, 1, 4),
    _Rc3PdeIsakmpAuthPresharedKey_Type()
)
rc3PdeIsakmpAuthPresharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdeIsakmpAuthPresharedKey.setStatus("deprecated")
_Rc3PdeIsakmpPfs_Type = Integer32
_Rc3PdeIsakmpPfs_Object = MibTableColumn
rc3PdeIsakmpPfs = _Rc3PdeIsakmpPfs_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 6, 1, 5),
    _Rc3PdeIsakmpPfs_Type()
)
rc3PdeIsakmpPfs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdeIsakmpPfs.setStatus("mandatory")
_Rc3PdeIsakmpRowStatus_Type = RowStatus
_Rc3PdeIsakmpRowStatus_Object = MibTableColumn
rc3PdeIsakmpRowStatus = _Rc3PdeIsakmpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 6, 1, 6),
    _Rc3PdeIsakmpRowStatus_Type()
)
rc3PdeIsakmpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdeIsakmpRowStatus.setStatus("mandatory")
_Rc3PdeIsakmpAuthPresharedKeyFips_Type = PbeShaEncryptedObject
_Rc3PdeIsakmpAuthPresharedKeyFips_Object = MibTableColumn
rc3PdeIsakmpAuthPresharedKeyFips = _Rc3PdeIsakmpAuthPresharedKeyFips_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 6, 1, 7),
    _Rc3PdeIsakmpAuthPresharedKeyFips_Type()
)
rc3PdeIsakmpAuthPresharedKeyFips.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdeIsakmpAuthPresharedKeyFips.setStatus("mandatory")
_Rc3PdeIpsecProtocolTable_Object = MibTable
rc3PdeIpsecProtocolTable = _Rc3PdeIpsecProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 7)
)
if mibBuilder.loadTexts:
    rc3PdeIpsecProtocolTable.setStatus("mandatory")
_Rc3PdeIpsecProtocolEntry_Object = MibTableRow
rc3PdeIpsecProtocolEntry = _Rc3PdeIpsecProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 7, 1)
)
rc3PdeIpsecProtocolEntry.setIndexNames(
    (0, "RCV3", "rc3PdeIpsecProtocolIndx"),
)
if mibBuilder.loadTexts:
    rc3PdeIpsecProtocolEntry.setStatus("mandatory")
_Rc3PdeIpsecProtocolIndx_Type = Integer32
_Rc3PdeIpsecProtocolIndx_Object = MibTableColumn
rc3PdeIpsecProtocolIndx = _Rc3PdeIpsecProtocolIndx_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 7, 1, 1),
    _Rc3PdeIpsecProtocolIndx_Type()
)
rc3PdeIpsecProtocolIndx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rc3PdeIpsecProtocolIndx.setStatus("mandatory")


class _Rc3PdeIpsecProtocolType_Type(Integer32):
    """Custom type rc3PdeIpsecProtocolType based on Integer32"""
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
        *(("ah", 1),
          ("esp", 2),
          ("mixed", 3),
          ("proprietaryeip", 4))
    )


_Rc3PdeIpsecProtocolType_Type.__name__ = "Integer32"
_Rc3PdeIpsecProtocolType_Object = MibTableColumn
rc3PdeIpsecProtocolType = _Rc3PdeIpsecProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 7, 1, 2),
    _Rc3PdeIpsecProtocolType_Type()
)
rc3PdeIpsecProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdeIpsecProtocolType.setStatus("mandatory")


class _Rc3PdeIpsecProposals_Type(OctetString):
    """Custom type rc3PdeIpsecProposals based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Rc3PdeIpsecProposals_Type.__name__ = "OctetString"
_Rc3PdeIpsecProposals_Object = MibTableColumn
rc3PdeIpsecProposals = _Rc3PdeIpsecProposals_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 7, 1, 3),
    _Rc3PdeIpsecProposals_Type()
)
rc3PdeIpsecProposals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdeIpsecProposals.setStatus("mandatory")
_Rc3PdeIpsecProtocolRowStatus_Type = RowStatus
_Rc3PdeIpsecProtocolRowStatus_Object = MibTableColumn
rc3PdeIpsecProtocolRowStatus = _Rc3PdeIpsecProtocolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 7, 1, 4),
    _Rc3PdeIpsecProtocolRowStatus_Type()
)
rc3PdeIpsecProtocolRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdeIpsecProtocolRowStatus.setStatus("mandatory")
_Rc3PdeSelectProtocolTable_Object = MibTable
rc3PdeSelectProtocolTable = _Rc3PdeSelectProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 8)
)
if mibBuilder.loadTexts:
    rc3PdeSelectProtocolTable.setStatus("deprecated")
_Rc3PdeSelectProtocolTableEntry_Object = MibTableRow
rc3PdeSelectProtocolTableEntry = _Rc3PdeSelectProtocolTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 8, 1)
)
rc3PdeSelectProtocolTableEntry.setIndexNames(
    (0, "RCV3", "rc3PdePeerIndx"),
    (0, "RCV3", "rc3PdeSelectProtocol"),
    (0, "RCV3", "rc3PdeSelectPort"),
)
if mibBuilder.loadTexts:
    rc3PdeSelectProtocolTableEntry.setStatus("deprecated")
_Rc3PdeSelectProtocol_Type = Integer32
_Rc3PdeSelectProtocol_Object = MibTableColumn
rc3PdeSelectProtocol = _Rc3PdeSelectProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 8, 1, 1),
    _Rc3PdeSelectProtocol_Type()
)
rc3PdeSelectProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rc3PdeSelectProtocol.setStatus("deprecated")
_Rc3PdeSelectPort_Type = Integer32
_Rc3PdeSelectPort_Object = MibTableColumn
rc3PdeSelectPort = _Rc3PdeSelectPort_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 8, 1, 2),
    _Rc3PdeSelectPort_Type()
)
rc3PdeSelectPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rc3PdeSelectPort.setStatus("deprecated")


class _Rc3PdeSelectAction_Type(Integer32):
    """Custom type rc3PdeSelectAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("operational", 3),
          ("pass", 2))
    )


_Rc3PdeSelectAction_Type.__name__ = "Integer32"
_Rc3PdeSelectAction_Object = MibTableColumn
rc3PdeSelectAction = _Rc3PdeSelectAction_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 8, 1, 3),
    _Rc3PdeSelectAction_Type()
)
rc3PdeSelectAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdeSelectAction.setStatus("deprecated")
_Rc3PdeSelectRowStatus_Type = RowStatus
_Rc3PdeSelectRowStatus_Object = MibTableColumn
rc3PdeSelectRowStatus = _Rc3PdeSelectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 2, 8, 1, 4),
    _Rc3PdeSelectRowStatus_Type()
)
rc3PdeSelectRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdeSelectRowStatus.setStatus("deprecated")
_Rc3PdMisc_ObjectIdentity = ObjectIdentity
rc3PdMisc = _Rc3PdMisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 3)
)
_Rc3PdeCount_Type = Integer32
_Rc3PdeCount_Object = MibScalar
rc3PdeCount = _Rc3PdeCount_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 3, 1),
    _Rc3PdeCount_Type()
)
rc3PdeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3PdeCount.setStatus("mandatory")
_Rc3PdePeerPreference_Type = OctetString
_Rc3PdePeerPreference_Object = MibScalar
rc3PdePeerPreference = _Rc3PdePeerPreference_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 3, 2),
    _Rc3PdePeerPreference_Type()
)
rc3PdePeerPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rc3PdePeerPreference.setStatus("deprecated")
_Rc3PdeNextAvailableIndx_Type = Integer32
_Rc3PdeNextAvailableIndx_Object = MibScalar
rc3PdeNextAvailableIndx = _Rc3PdeNextAvailableIndx_Object(
    (1, 3, 6, 1, 4, 1, 1958, 1, 1, 9, 3, 3),
    _Rc3PdeNextAvailableIndx_Type()
)
rc3PdeNextAvailableIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rc3PdeNextAvailableIndx.setStatus("mandatory")
_Registration_ObjectIdentity = ObjectIdentity
registration = _Registration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958, 2)
)
_RcRavlin10_ObjectIdentity = ObjectIdentity
rcRavlin10 = _RcRavlin10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958, 2, 1)
)
_RcRavlin4_ObjectIdentity = ObjectIdentity
rcRavlin4 = _RcRavlin4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958, 2, 2)
)
_RcPCI_ObjectIdentity = ObjectIdentity
rcPCI = _RcPCI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958, 2, 3)
)
_RcRavlin10Ver3_ObjectIdentity = ObjectIdentity
rcRavlin10Ver3 = _RcRavlin10Ver3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958, 2, 4)
)
_RcRavlin4Ver3_ObjectIdentity = ObjectIdentity
rcRavlin4Ver3 = _RcRavlin4Ver3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958, 2, 5)
)
_RcPCIVer3_ObjectIdentity = ObjectIdentity
rcPCIVer3 = _RcPCIVer3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1958, 2, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RCV3",
    **{"RowStatus": RowStatus,
       "PbeShaEncryptedObject": PbeShaEncryptedObject,
       "redCreek": redCreek,
       "products": products,
       "rcRavlin": rcRavlin,
       "rcAdmin": rcAdmin,
       "rcSecure": rcSecure,
       "rcBoot": rcBoot,
       "rcStatus": rcStatus,
       "rcTrap": rcTrap,
       "rcDebug": rcDebug,
       "rcEsp": rcEsp,
       "rcMgmt": rcMgmt,
       "rc3System": rc3System,
       "rc3BootRomVer": rc3BootRomVer,
       "rc3FirmwareVer": rc3FirmwareVer,
       "rc3FirmwareID": rc3FirmwareID,
       "rc3HardwareVer": rc3HardwareVer,
       "rc3DistinguishedName": rc3DistinguishedName,
       "rc3HostName": rc3HostName,
       "rc3Network": rc3Network,
       "rc3InterfaceTable": rc3InterfaceTable,
       "rc3InterfaceEntry": rc3InterfaceEntry,
       "rc3InterfaceIp": rc3InterfaceIp,
       "rc3InterfaceMask": rc3InterfaceMask,
       "rc3InterfaceMac": rc3InterfaceMac,
       "rc3IpRouteTable": rc3IpRouteTable,
       "rc3IpRouteEntry": rc3IpRouteEntry,
       "rc3IpRouteDest": rc3IpRouteDest,
       "rc3IpRouteMask": rc3IpRouteMask,
       "rc3IpRouteIfIndex": rc3IpRouteIfIndex,
       "rc3IpRouteNextHop": rc3IpRouteNextHop,
       "rc3IpRouteMetric": rc3IpRouteMetric,
       "rc3IpRouteProto": rc3IpRouteProto,
       "rc3IpRouteAge": rc3IpRouteAge,
       "rc3IpRouteRowStatus": rc3IpRouteRowStatus,
       "rc3PacketHandlingOptions": rc3PacketHandlingOptions,
       "rc3PPPoEUserName": rc3PPPoEUserName,
       "rc3PPPoEUserPassword": rc3PPPoEUserPassword,
       "rc3PPPoEServiceName": rc3PPPoEServiceName,
       "rc3PPPoEConcentratorName": rc3PPPoEConcentratorName,
       "rc3PPPoEIdleTimeout": rc3PPPoEIdleTimeout,
       "rc3PPPoERetryCount": rc3PPPoERetryCount,
       "rc3PPPoEDnsServer1": rc3PPPoEDnsServer1,
       "rc3PPPoEDnsServer2": rc3PPPoEDnsServer2,
       "rc3Control": rc3Control,
       "rc3Reset": rc3Reset,
       "rc3ArpCacheCleanupInterval": rc3ArpCacheCleanupInterval,
       "rc3Password": rc3Password,
       "rc3OperationalMode": rc3OperationalMode,
       "rc3InactiveClientTimeout": rc3InactiveClientTimeout,
       "rc3DHCPServerIP": rc3DHCPServerIP,
       "rc3DHCPRequest": rc3DHCPRequest,
       "rc3PasswordFips": rc3PasswordFips,
       "rc3DHCPRelayIpAddr": rc3DHCPRelayIpAddr,
       "rc3SysPerfTimeBetweenPolls": rc3SysPerfTimeBetweenPolls,
       "rc3SysPerfTimeBetweenReports": rc3SysPerfTimeBetweenReports,
       "rc3SysPerfTrapThreshold": rc3SysPerfTrapThreshold,
       "rc3DHCPBroadcastIntf": rc3DHCPBroadcastIntf,
       "rc3StateLessDHCP": rc3StateLessDHCP,
       "rc3Stat": rc3Stat,
       "rc3ActiveSAcount": rc3ActiveSAcount,
       "rc3PendingSAcount": rc3PendingSAcount,
       "rc3SigFailCount": rc3SigFailCount,
       "rc3StatusMsgTable": rc3StatusMsgTable,
       "rc3StatusMsgEntry": rc3StatusMsgEntry,
       "rc3StatusMsgIndex": rc3StatusMsgIndex,
       "rc3FirstInTimeStamp": rc3FirstInTimeStamp,
       "rc3LastInTimeStamp": rc3LastInTimeStamp,
       "rc3EventCode": rc3EventCode,
       "rc3EventCodeRepetitions": rc3EventCodeRepetitions,
       "rc3EventSpecificDescr1": rc3EventSpecificDescr1,
       "rc3EventSpecificDescr2": rc3EventSpecificDescr2,
       "rc3SysLogServerIP": rc3SysLogServerIP,
       "rc3SysLogPortNum": rc3SysLogPortNum,
       "rc3SysLogMsgLevel": rc3SysLogMsgLevel,
       "rc3SysLogServerTable": rc3SysLogServerTable,
       "rc3SysLogServerEntry": rc3SysLogServerEntry,
       "rc3SysLogServerIp": rc3SysLogServerIp,
       "rc3SysLogServerPort": rc3SysLogServerPort,
       "rc3SysLogPriorityLevel": rc3SysLogPriorityLevel,
       "rc3SysLogMsgStatus": rc3SysLogMsgStatus,
       "rc3Snmp": rc3Snmp,
       "rc3ReadCommunityString": rc3ReadCommunityString,
       "rc3WriteCommunityString": rc3WriteCommunityString,
       "rc3TrapRcvrTable": rc3TrapRcvrTable,
       "rc3TrapRcvrEntry": rc3TrapRcvrEntry,
       "rc3TrapRcvrIpAddr": rc3TrapRcvrIpAddr,
       "rc3TrapRcvrComm": rc3TrapRcvrComm,
       "rc3TrapRcvrType": rc3TrapRcvrType,
       "rc3TrapRcvrStatus": rc3TrapRcvrStatus,
       "rc3SnmpErrorCode": rc3SnmpErrorCode,
       "rc3ReadCommunityStringFips": rc3ReadCommunityStringFips,
       "rc3WriteCommunityStringFips": rc3WriteCommunityStringFips,
       "rc3ClientCfg": rc3ClientCfg,
       "rc3ClientAuthentication": rc3ClientAuthentication,
       "rc3ActiveRadiusServer": rc3ActiveRadiusServer,
       "rc3RadiusPriority": rc3RadiusPriority,
       "rc3RadiusAuthServerTable": rc3RadiusAuthServerTable,
       "rc3RadiusAuthServerEntry": rc3RadiusAuthServerEntry,
       "rc3RadiusAuthServerEntryIndx": rc3RadiusAuthServerEntryIndx,
       "rc3RadiusAuthServerIP": rc3RadiusAuthServerIP,
       "rc3RadiusAuthServerPort": rc3RadiusAuthServerPort,
       "rc3RadiusAttributeOffset": rc3RadiusAttributeOffset,
       "rc3RadiusAuthServerSharedSecret": rc3RadiusAuthServerSharedSecret,
       "rc3RadiusAuthServerRetries": rc3RadiusAuthServerRetries,
       "rc3RadiusAuthServerSharedSecretFips": rc3RadiusAuthServerSharedSecretFips,
       "rc3LocalAuthTable": rc3LocalAuthTable,
       "rc3LocalAuthEntry": rc3LocalAuthEntry,
       "rc3LocalAuthId": rc3LocalAuthId,
       "rc3LocalAuthName": rc3LocalAuthName,
       "rc3LocalAuthPassword": rc3LocalAuthPassword,
       "rc3LocalAuthIpAddr": rc3LocalAuthIpAddr,
       "rc3LocalAuthIpMask": rc3LocalAuthIpMask,
       "rc3LocalAuthRowStatus": rc3LocalAuthRowStatus,
       "rc3Download": rc3Download,
       "rc3ImageSize": rc3ImageSize,
       "rc3SoftwareBlock": rc3SoftwareBlock,
       "rc3SoftwareBlockNumber": rc3SoftwareBlockNumber,
       "rc3Misc": rc3Misc,
       "rc3RandomNumber": rc3RandomNumber,
       "rc3HashObject": rc3HashObject,
       "rc3UlaAuthenticationTimer": rc3UlaAuthenticationTimer,
       "rc3UlaAuthenticationPort": rc3UlaAuthenticationPort,
       "rc3SystemTime": rc3SystemTime,
       "rc3Cert": rc3Cert,
       "rc3CACertTable": rc3CACertTable,
       "rc3CACertEntry": rc3CACertEntry,
       "rc3CACertIndex": rc3CACertIndex,
       "rc3CACertName": rc3CACertName,
       "rc3CACertData": rc3CACertData,
       "rc3CACertStatus": rc3CACertStatus,
       "rc3UserCertTable": rc3UserCertTable,
       "rc3UserCertEntry": rc3UserCertEntry,
       "rc3UserCertIndex": rc3UserCertIndex,
       "rc3UserCertName": rc3UserCertName,
       "rc3UserCertData": rc3UserCertData,
       "rc3UserCertStatus": rc3UserCertStatus,
       "rc3UserCertRDN": rc3UserCertRDN,
       "rc3UserCertAlgoId": rc3UserCertAlgoId,
       "rc3GenerateKeyPair": rc3GenerateKeyPair,
       "rc3UserCertGetPkcs10": rc3UserCertGetPkcs10,
       "rcPolicy": rcPolicy,
       "rc3Proposals": rc3Proposals,
       "rc3IsakmpProposalTable": rc3IsakmpProposalTable,
       "rc3IsakmpProposalEntry": rc3IsakmpProposalEntry,
       "rc3IsakmpProposalIndx": rc3IsakmpProposalIndx,
       "rc3IsakmpProposalEncryption": rc3IsakmpProposalEncryption,
       "rc3IsakmpProposalHash": rc3IsakmpProposalHash,
       "rc3IsakmpProposalAuthMode": rc3IsakmpProposalAuthMode,
       "rc3IsakmpProposalDhGroup": rc3IsakmpProposalDhGroup,
       "rc3EspProposalTable": rc3EspProposalTable,
       "rc3EspProposalEntry": rc3EspProposalEntry,
       "rc3EspProposalIndx": rc3EspProposalIndx,
       "rc3EspProposalCipherAlgo": rc3EspProposalCipherAlgo,
       "rc3EspProposalEncapsulation": rc3EspProposalEncapsulation,
       "rc3EspProposalAuth": rc3EspProposalAuth,
       "rc3EspProposalGroup": rc3EspProposalGroup,
       "rc3AhProposalTable": rc3AhProposalTable,
       "rc3AhProposalEntry": rc3AhProposalEntry,
       "rc3AhProposalIndx": rc3AhProposalIndx,
       "rc3AhProposalAuth": rc3AhProposalAuth,
       "rc3AhProposalEncapsulation": rc3AhProposalEncapsulation,
       "rc3AhProposalGroup": rc3AhProposalGroup,
       "rc3EipProposalTable": rc3EipProposalTable,
       "rc3EipProposalEntry": rc3EipProposalEntry,
       "rc3EipProposalIndx": rc3EipProposalIndx,
       "rc3EipProposalCipherAlgo": rc3EipProposalCipherAlgo,
       "rc3Pde": rc3Pde,
       "rc3PdePeerInfoTable": rc3PdePeerInfoTable,
       "rc3PdePeerInfoEntry": rc3PdePeerInfoEntry,
       "rc3PdePeerIndx": rc3PdePeerIndx,
       "rc3PdePeerType": rc3PdePeerType,
       "rc3PdePeerAddr": rc3PdePeerAddr,
       "rc3PdePeerDN": rc3PdePeerDN,
       "rc3PdePeerIssuerDN": rc3PdePeerIssuerDN,
       "rc3PdePeerLocalCertIndx": rc3PdePeerLocalCertIndx,
       "rc3PdePeerKeyMgmtType": rc3PdePeerKeyMgmtType,
       "rc3PdePeerKeyMgmtIndx": rc3PdePeerKeyMgmtIndx,
       "rc3PdePeerIpsecProtocolIndx": rc3PdePeerIpsecProtocolIndx,
       "rc3PdePeerIfIndex": rc3PdePeerIfIndex,
       "rc3PdePeerNextHop": rc3PdePeerNextHop,
       "rc3PdePeerContinue": rc3PdePeerContinue,
       "rc3PdePeerIsakmpLifeType": rc3PdePeerIsakmpLifeType,
       "rc3PdePeerIsakmpLifeTimeSeconds": rc3PdePeerIsakmpLifeTimeSeconds,
       "rc3PdePeerIsakmpLifeTimeKiloBytes": rc3PdePeerIsakmpLifeTimeKiloBytes,
       "rc3PdePeerIpsecLifeType": rc3PdePeerIpsecLifeType,
       "rc3PdePeerIpsecLifeTimeSeconds": rc3PdePeerIpsecLifeTimeSeconds,
       "rc3PdePeerIpsecLifeTimeKiloBytes": rc3PdePeerIpsecLifeTimeKiloBytes,
       "rc3PdePeerRowStatus": rc3PdePeerRowStatus,
       "rc3PdeFilterProtocol": rc3PdeFilterProtocol,
       "rc3PdeLocalPort": rc3PdeLocalPort,
       "rc3PdeRemotePort": rc3PdeRemotePort,
       "rc3PdeName": rc3PdeName,
       "rc3PdeULA": rc3PdeULA,
       "rc3PdePeerLocalInterfaceIpAddr": rc3PdePeerLocalInterfaceIpAddr,
       "rc3PdeLocalNetworkTable": rc3PdeLocalNetworkTable,
       "rc3PdeLocalNetworkEntry": rc3PdeLocalNetworkEntry,
       "rc3PdeLocalNetworkNumber": rc3PdeLocalNetworkNumber,
       "rc3PdeLocalNetworkMask": rc3PdeLocalNetworkMask,
       "rc3PdeLocalNetworkRowStatus": rc3PdeLocalNetworkRowStatus,
       "rc3PdeRemoteNetworkTable": rc3PdeRemoteNetworkTable,
       "rc3PdeRemoteNetworkEntry": rc3PdeRemoteNetworkEntry,
       "rc3PdeRemoteNetworkNumber": rc3PdeRemoteNetworkNumber,
       "rc3PdeRemoteNetworkMask": rc3PdeRemoteNetworkMask,
       "rc3PdeRemoteNetworkRowStatus": rc3PdeRemoteNetworkRowStatus,
       "rc3SAStatTable": rc3SAStatTable,
       "rc3SAStatEntry": rc3SAStatEntry,
       "rc3SAStatPeerAddr": rc3SAStatPeerAddr,
       "rc3SAStatConnStatus": rc3SAStatConnStatus,
       "rc3SAStatCreateTime": rc3SAStatCreateTime,
       "rc3SAStatEncryptPktCount": rc3SAStatEncryptPktCount,
       "rc3SAStatEncryptByteCount": rc3SAStatEncryptByteCount,
       "rc3SAStatDecryptPktCount": rc3SAStatDecryptPktCount,
       "rc3SAStatDecryptByteCount": rc3SAStatDecryptByteCount,
       "rc3SAStatFragPktCount": rc3SAStatFragPktCount,
       "rc3SAStatReset": rc3SAStatReset,
       "rc3SAStatUserName": rc3SAStatUserName,
       "rc3SAStatPollsSent": rc3SAStatPollsSent,
       "rc3SAStatPollsReceived": rc3SAStatPollsReceived,
       "rc3SAStatPollsAverageTime": rc3SAStatPollsAverageTime,
       "rc3SAStatPollsMaxTime": rc3SAStatPollsMaxTime,
       "rc3SAStatPollsMinTime": rc3SAStatPollsMinTime,
       "rc3PdeManualKeyMgmtTable": rc3PdeManualKeyMgmtTable,
       "rc3PdeManualKeyMgmtEntry": rc3PdeManualKeyMgmtEntry,
       "rc3PdeManualKeyMgmtIndx": rc3PdeManualKeyMgmtIndx,
       "rc3PdeManualInboundEncryptKey": rc3PdeManualInboundEncryptKey,
       "rc3PdeManualOutboundEncryptKey": rc3PdeManualOutboundEncryptKey,
       "rc3PdeManualInboundAuthKey": rc3PdeManualInboundAuthKey,
       "rc3PdeManualOutboundAuthKey": rc3PdeManualOutboundAuthKey,
       "rc3PdeManualInboundSpi": rc3PdeManualInboundSpi,
       "rc3PdeManualOutboundSpi": rc3PdeManualOutboundSpi,
       "rc3PdeManualKeyMgmtRowStatus": rc3PdeManualKeyMgmtRowStatus,
       "rc3PdeManualInboundEncryptKeyFips": rc3PdeManualInboundEncryptKeyFips,
       "rc3PdeManualOutboundEncryptKeyFips": rc3PdeManualOutboundEncryptKeyFips,
       "rc3PdeManualInboundAuthKeyFips": rc3PdeManualInboundAuthKeyFips,
       "rc3PdeManualOutboundAuthKeyFips": rc3PdeManualOutboundAuthKeyFips,
       "rc3PdeIsakmpKeyMgmtTable": rc3PdeIsakmpKeyMgmtTable,
       "rc3PdeIsakmpKeyMgmtEntry": rc3PdeIsakmpKeyMgmtEntry,
       "rc3PdeIsakmpIndx": rc3PdeIsakmpIndx,
       "rc3PdeIsakmpProposals": rc3PdeIsakmpProposals,
       "rc3PdeIsakmpRetries": rc3PdeIsakmpRetries,
       "rc3PdeIsakmpAuthPresharedKey": rc3PdeIsakmpAuthPresharedKey,
       "rc3PdeIsakmpPfs": rc3PdeIsakmpPfs,
       "rc3PdeIsakmpRowStatus": rc3PdeIsakmpRowStatus,
       "rc3PdeIsakmpAuthPresharedKeyFips": rc3PdeIsakmpAuthPresharedKeyFips,
       "rc3PdeIpsecProtocolTable": rc3PdeIpsecProtocolTable,
       "rc3PdeIpsecProtocolEntry": rc3PdeIpsecProtocolEntry,
       "rc3PdeIpsecProtocolIndx": rc3PdeIpsecProtocolIndx,
       "rc3PdeIpsecProtocolType": rc3PdeIpsecProtocolType,
       "rc3PdeIpsecProposals": rc3PdeIpsecProposals,
       "rc3PdeIpsecProtocolRowStatus": rc3PdeIpsecProtocolRowStatus,
       "rc3PdeSelectProtocolTable": rc3PdeSelectProtocolTable,
       "rc3PdeSelectProtocolTableEntry": rc3PdeSelectProtocolTableEntry,
       "rc3PdeSelectProtocol": rc3PdeSelectProtocol,
       "rc3PdeSelectPort": rc3PdeSelectPort,
       "rc3PdeSelectAction": rc3PdeSelectAction,
       "rc3PdeSelectRowStatus": rc3PdeSelectRowStatus,
       "rc3PdMisc": rc3PdMisc,
       "rc3PdeCount": rc3PdeCount,
       "rc3PdePeerPreference": rc3PdePeerPreference,
       "rc3PdeNextAvailableIndx": rc3PdeNextAvailableIndx,
       "registration": registration,
       "rcRavlin10": rcRavlin10,
       "rcRavlin4": rcRavlin4,
       "rcPCI": rcPCI,
       "rcRavlin10Ver3": rcRavlin10Ver3,
       "rcRavlin4Ver3": rcRavlin4Ver3,
       "rcPCIVer3": rcPCIVer3}
)
