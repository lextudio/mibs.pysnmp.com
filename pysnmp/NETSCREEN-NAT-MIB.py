# SNMP MIB module (NETSCREEN-NAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-NAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:46 2024
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

(netscreenNAT,) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenNAT")

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

netscreenNATMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 11, 0)
)
netscreenNATMibModule.setRevisions(
        ("2005-03-03 00:00",
         "2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-06-03 00:00",
         "2001-05-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsNatMipTable_Object = MibTable
nsNatMipTable = _NsNatMipTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 1)
)
if mibBuilder.loadTexts:
    nsNatMipTable.setStatus("current")
_NsNatMipEntry_Object = MibTableRow
nsNatMipEntry = _NsNatMipEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 1, 1)
)
nsNatMipEntry.setIndexNames(
    (0, "NETSCREEN-NAT-MIB", "nsNatMipIndex"),
)
if mibBuilder.loadTexts:
    nsNatMipEntry.setStatus("current")


class _NsNatMipIndex_Type(Integer32):
    """Custom type nsNatMipIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsNatMipIndex_Type.__name__ = "Integer32"
_NsNatMipIndex_Object = MibTableColumn
nsNatMipIndex = _NsNatMipIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 1, 1, 1),
    _NsNatMipIndex_Type()
)
nsNatMipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNatMipIndex.setStatus("current")
_NsNatMipIp_Type = IpAddress
_NsNatMipIp_Object = MibTableColumn
nsNatMipIp = _NsNatMipIp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 1, 1, 2),
    _NsNatMipIp_Type()
)
nsNatMipIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNatMipIp.setStatus("current")
_NsNatMipNetmask_Type = IpAddress
_NsNatMipNetmask_Object = MibTableColumn
nsNatMipNetmask = _NsNatMipNetmask_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 1, 1, 3),
    _NsNatMipNetmask_Type()
)
nsNatMipNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNatMipNetmask.setStatus("current")
_NsNatMipHost_Type = IpAddress
_NsNatMipHost_Object = MibTableColumn
nsNatMipHost = _NsNatMipHost_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 1, 1, 4),
    _NsNatMipHost_Type()
)
nsNatMipHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNatMipHost.setStatus("current")
_NsNatMipIfIp_Type = IpAddress
_NsNatMipIfIp_Object = MibTableColumn
nsNatMipIfIp = _NsNatMipIfIp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 1, 1, 5),
    _NsNatMipIfIp_Type()
)
nsNatMipIfIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNatMipIfIp.setStatus("current")
_NsNatMipIfNetmask_Type = IpAddress
_NsNatMipIfNetmask_Object = MibTableColumn
nsNatMipIfNetmask = _NsNatMipIfNetmask_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 1, 1, 6),
    _NsNatMipIfNetmask_Type()
)
nsNatMipIfNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNatMipIfNetmask.setStatus("current")
_NsNatMipVsys_Type = Integer32
_NsNatMipVsys_Object = MibTableColumn
nsNatMipVsys = _NsNatMipVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 1, 1, 7),
    _NsNatMipVsys_Type()
)
nsNatMipVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNatMipVsys.setStatus("current")
_NsNatDipTable_Object = MibTable
nsNatDipTable = _NsNatDipTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 2)
)
if mibBuilder.loadTexts:
    nsNatDipTable.setStatus("current")
_NsNatDipEntry_Object = MibTableRow
nsNatDipEntry = _NsNatDipEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 2, 1)
)
nsNatDipEntry.setIndexNames(
    (0, "NETSCREEN-NAT-MIB", "nsNatDipIndex"),
)
if mibBuilder.loadTexts:
    nsNatDipEntry.setStatus("current")


class _NsNatDipIndex_Type(Integer32):
    """Custom type nsNatDipIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsNatDipIndex_Type.__name__ = "Integer32"
_NsNatDipIndex_Object = MibTableColumn
nsNatDipIndex = _NsNatDipIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 2, 1, 1),
    _NsNatDipIndex_Type()
)
nsNatDipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNatDipIndex.setStatus("current")
_NsNatDipId_Type = Integer32
_NsNatDipId_Object = MibTableColumn
nsNatDipId = _NsNatDipId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 2, 1, 2),
    _NsNatDipId_Type()
)
nsNatDipId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNatDipId.setStatus("current")
_NsNatDipLow_Type = IpAddress
_NsNatDipLow_Object = MibTableColumn
nsNatDipLow = _NsNatDipLow_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 2, 1, 3),
    _NsNatDipLow_Type()
)
nsNatDipLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNatDipLow.setStatus("current")
_NsNatDipHigh_Type = IpAddress
_NsNatDipHigh_Object = MibTableColumn
nsNatDipHigh = _NsNatDipHigh_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 2, 1, 4),
    _NsNatDipHigh_Type()
)
nsNatDipHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNatDipHigh.setStatus("current")
_NsNatDipIfIp_Type = IpAddress
_NsNatDipIfIp_Object = MibTableColumn
nsNatDipIfIp = _NsNatDipIfIp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 2, 1, 5),
    _NsNatDipIfIp_Type()
)
nsNatDipIfIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNatDipIfIp.setStatus("current")
_NsNatDipIfNetmask_Type = IpAddress
_NsNatDipIfNetmask_Object = MibTableColumn
nsNatDipIfNetmask = _NsNatDipIfNetmask_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 2, 1, 6),
    _NsNatDipIfNetmask_Type()
)
nsNatDipIfNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNatDipIfNetmask.setStatus("current")


class _NsNatDipPTEnable_Type(Integer32):
    """Custom type nsNatDipPTEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_NsNatDipPTEnable_Type.__name__ = "Integer32"
_NsNatDipPTEnable_Object = MibTableColumn
nsNatDipPTEnable = _NsNatDipPTEnable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 2, 1, 7),
    _NsNatDipPTEnable_Type()
)
nsNatDipPTEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNatDipPTEnable.setStatus("current")
_NsNatDipVsys_Type = Integer32
_NsNatDipVsys_Object = MibTableColumn
nsNatDipVsys = _NsNatDipVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 2, 1, 8),
    _NsNatDipVsys_Type()
)
nsNatDipVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNatDipVsys.setStatus("current")
_NsNatDipUtil_Type = Integer32
_NsNatDipUtil_Object = MibTableColumn
nsNatDipUtil = _NsNatDipUtil_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 2, 1, 9),
    _NsNatDipUtil_Type()
)
nsNatDipUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNatDipUtil.setStatus("current")
_NsNatVip_ObjectIdentity = ObjectIdentity
nsNatVip = _NsNatVip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 11, 3)
)
_NsNatVipCfgTable_Object = MibTable
nsNatVipCfgTable = _NsNatVipCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 3, 1)
)
if mibBuilder.loadTexts:
    nsNatVipCfgTable.setStatus("current")
_NsNatVipCfgEntry_Object = MibTableRow
nsNatVipCfgEntry = _NsNatVipCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 3, 1, 1)
)
nsNatVipCfgEntry.setIndexNames(
    (0, "NETSCREEN-NAT-MIB", "nsNatVipCfgIndex"),
)
if mibBuilder.loadTexts:
    nsNatVipCfgEntry.setStatus("current")


class _NsNatVipCfgIndex_Type(Integer32):
    """Custom type nsNatVipCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsNatVipCfgIndex_Type.__name__ = "Integer32"
_NsNatVipCfgIndex_Object = MibTableColumn
nsNatVipCfgIndex = _NsNatVipCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 3, 1, 1, 1),
    _NsNatVipCfgIndex_Type()
)
nsNatVipCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNatVipCfgIndex.setStatus("current")
_NsNatVipCfgIp_Type = IpAddress
_NsNatVipCfgIp_Object = MibTableColumn
nsNatVipCfgIp = _NsNatVipCfgIp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 3, 1, 1, 2),
    _NsNatVipCfgIp_Type()
)
nsNatVipCfgIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNatVipCfgIp.setStatus("current")
_NsNatVipCfgPort_Type = Integer32
_NsNatVipCfgPort_Object = MibTableColumn
nsNatVipCfgPort = _NsNatVipCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 3, 1, 1, 3),
    _NsNatVipCfgPort_Type()
)
nsNatVipCfgPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNatVipCfgPort.setStatus("current")


class _NsNatVipCfgService_Type(DisplayString):
    """Custom type nsNatVipCfgService based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NsNatVipCfgService_Type.__name__ = "DisplayString"
_NsNatVipCfgService_Object = MibTableColumn
nsNatVipCfgService = _NsNatVipCfgService_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 3, 1, 1, 4),
    _NsNatVipCfgService_Type()
)
nsNatVipCfgService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNatVipCfgService.setStatus("current")


class _NsNatVipCfgStatus_Type(Integer32):
    """Custom type nsNatVipCfgStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("not-available", 0))
    )


_NsNatVipCfgStatus_Type.__name__ = "Integer32"
_NsNatVipCfgStatus_Object = MibTableColumn
nsNatVipCfgStatus = _NsNatVipCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 3, 1, 1, 5),
    _NsNatVipCfgStatus_Type()
)
nsNatVipCfgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNatVipCfgStatus.setStatus("current")


class _NsNatVipCfgLoadBalance_Type(Integer32):
    """Custom type nsNatVipCfgLoadBalance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("least-conns", 3),
          ("null", 0),
          ("round-robin", 1),
          ("weighted-least-conns", 4),
          ("weighted-round-robin", 2))
    )


_NsNatVipCfgLoadBalance_Type.__name__ = "Integer32"
_NsNatVipCfgLoadBalance_Object = MibTableColumn
nsNatVipCfgLoadBalance = _NsNatVipCfgLoadBalance_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 3, 1, 1, 6),
    _NsNatVipCfgLoadBalance_Type()
)
nsNatVipCfgLoadBalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNatVipCfgLoadBalance.setStatus("current")
_NsNatVipServerTable_Object = MibTable
nsNatVipServerTable = _NsNatVipServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 3, 2)
)
if mibBuilder.loadTexts:
    nsNatVipServerTable.setStatus("current")
_NsNatVipServerEntry_Object = MibTableRow
nsNatVipServerEntry = _NsNatVipServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 3, 2, 1)
)
nsNatVipServerEntry.setIndexNames(
    (0, "NETSCREEN-NAT-MIB", "nsNatVipServerIndex"),
)
if mibBuilder.loadTexts:
    nsNatVipServerEntry.setStatus("current")


class _NsNatVipServerIndex_Type(Integer32):
    """Custom type nsNatVipServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsNatVipServerIndex_Type.__name__ = "Integer32"
_NsNatVipServerIndex_Object = MibTableColumn
nsNatVipServerIndex = _NsNatVipServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 3, 2, 1, 1),
    _NsNatVipServerIndex_Type()
)
nsNatVipServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNatVipServerIndex.setStatus("current")
_NsNatVipServerVIP_Type = IpAddress
_NsNatVipServerVIP_Object = MibTableColumn
nsNatVipServerVIP = _NsNatVipServerVIP_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 3, 2, 1, 2),
    _NsNatVipServerVIP_Type()
)
nsNatVipServerVIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNatVipServerVIP.setStatus("current")
_NsNatVipServerService_Type = Integer32
_NsNatVipServerService_Object = MibTableColumn
nsNatVipServerService = _NsNatVipServerService_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 3, 2, 1, 3),
    _NsNatVipServerService_Type()
)
nsNatVipServerService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNatVipServerService.setStatus("current")


class _NsNatVipServerLoadBalance_Type(Integer32):
    """Custom type nsNatVipServerLoadBalance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("least-conns", 3),
          ("null", 0),
          ("round-robin", 1),
          ("weighted-least-conns", 4),
          ("weighted-round-robin", 2))
    )


_NsNatVipServerLoadBalance_Type.__name__ = "Integer32"
_NsNatVipServerLoadBalance_Object = MibTableColumn
nsNatVipServerLoadBalance = _NsNatVipServerLoadBalance_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 3, 2, 1, 4),
    _NsNatVipServerLoadBalance_Type()
)
nsNatVipServerLoadBalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNatVipServerLoadBalance.setStatus("current")
_NsNatVipServerIp_Type = IpAddress
_NsNatVipServerIp_Object = MibTableColumn
nsNatVipServerIp = _NsNatVipServerIp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 3, 2, 1, 5),
    _NsNatVipServerIp_Type()
)
nsNatVipServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNatVipServerIp.setStatus("current")
_NsNatVipServerWeight_Type = Integer32
_NsNatVipServerWeight_Object = MibTableColumn
nsNatVipServerWeight = _NsNatVipServerWeight_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 3, 2, 1, 6),
    _NsNatVipServerWeight_Type()
)
nsNatVipServerWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNatVipServerWeight.setStatus("current")


class _NsNatVipServerStatus_Type(Integer32):
    """Custom type nsNatVipServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_NsNatVipServerStatus_Type.__name__ = "Integer32"
_NsNatVipServerStatus_Object = MibTableColumn
nsNatVipServerStatus = _NsNatVipServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 11, 3, 2, 1, 7),
    _NsNatVipServerStatus_Type()
)
nsNatVipServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsNatVipServerStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-NAT-MIB",
    **{"netscreenNATMibModule": netscreenNATMibModule,
       "nsNatMipTable": nsNatMipTable,
       "nsNatMipEntry": nsNatMipEntry,
       "nsNatMipIndex": nsNatMipIndex,
       "nsNatMipIp": nsNatMipIp,
       "nsNatMipNetmask": nsNatMipNetmask,
       "nsNatMipHost": nsNatMipHost,
       "nsNatMipIfIp": nsNatMipIfIp,
       "nsNatMipIfNetmask": nsNatMipIfNetmask,
       "nsNatMipVsys": nsNatMipVsys,
       "nsNatDipTable": nsNatDipTable,
       "nsNatDipEntry": nsNatDipEntry,
       "nsNatDipIndex": nsNatDipIndex,
       "nsNatDipId": nsNatDipId,
       "nsNatDipLow": nsNatDipLow,
       "nsNatDipHigh": nsNatDipHigh,
       "nsNatDipIfIp": nsNatDipIfIp,
       "nsNatDipIfNetmask": nsNatDipIfNetmask,
       "nsNatDipPTEnable": nsNatDipPTEnable,
       "nsNatDipVsys": nsNatDipVsys,
       "nsNatDipUtil": nsNatDipUtil,
       "nsNatVip": nsNatVip,
       "nsNatVipCfgTable": nsNatVipCfgTable,
       "nsNatVipCfgEntry": nsNatVipCfgEntry,
       "nsNatVipCfgIndex": nsNatVipCfgIndex,
       "nsNatVipCfgIp": nsNatVipCfgIp,
       "nsNatVipCfgPort": nsNatVipCfgPort,
       "nsNatVipCfgService": nsNatVipCfgService,
       "nsNatVipCfgStatus": nsNatVipCfgStatus,
       "nsNatVipCfgLoadBalance": nsNatVipCfgLoadBalance,
       "nsNatVipServerTable": nsNatVipServerTable,
       "nsNatVipServerEntry": nsNatVipServerEntry,
       "nsNatVipServerIndex": nsNatVipServerIndex,
       "nsNatVipServerVIP": nsNatVipServerVIP,
       "nsNatVipServerService": nsNatVipServerService,
       "nsNatVipServerLoadBalance": nsNatVipServerLoadBalance,
       "nsNatVipServerIp": nsNatVipServerIp,
       "nsNatVipServerWeight": nsNatVipServerWeight,
       "nsNatVipServerStatus": nsNatVipServerStatus}
)
