# SNMP MIB module (INTEL-L3TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-L3TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:52 2024
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

(mib2ext,) = mibBuilder.importSymbols(
    "INTEL-GEN-MIB",
    "mib2ext")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_L3tcache_ObjectIdentity = ObjectIdentity
l3tcache = _L3tcache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 37)
)
_L3tcFrontPorts_ObjectIdentity = ObjectIdentity
l3tcFrontPorts = _L3tcFrontPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 37, 1)
)
_L3tcFrontPortsTable_Object = MibTable
l3tcFrontPortsTable = _L3tcFrontPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 37, 1, 1)
)
if mibBuilder.loadTexts:
    l3tcFrontPortsTable.setStatus("mandatory")
_L3tcFrontPortsEntry_Object = MibTableRow
l3tcFrontPortsEntry = _L3tcFrontPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 37, 1, 1, 1)
)
l3tcFrontPortsEntry.setIndexNames(
    (0, "INTEL-L3TC-MIB", "l3tcFrontPortsNumber"),
)
if mibBuilder.loadTexts:
    l3tcFrontPortsEntry.setStatus("mandatory")
_L3tcFrontPortsNumber_Type = Integer32
_L3tcFrontPortsNumber_Object = MibTableColumn
l3tcFrontPortsNumber = _L3tcFrontPortsNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 37, 1, 1, 1, 1),
    _L3tcFrontPortsNumber_Type()
)
l3tcFrontPortsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3tcFrontPortsNumber.setStatus("mandatory")


class _L3tcFrontPortsMode_Type(Integer32):
    """Custom type l3tcFrontPortsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("client", 2),
          ("normal", 1),
          ("server", 3))
    )


_L3tcFrontPortsMode_Type.__name__ = "Integer32"
_L3tcFrontPortsMode_Object = MibTableColumn
l3tcFrontPortsMode = _L3tcFrontPortsMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 37, 1, 1, 1, 2),
    _L3tcFrontPortsMode_Type()
)
l3tcFrontPortsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3tcFrontPortsMode.setStatus("mandatory")
_L3tcServers_ObjectIdentity = ObjectIdentity
l3tcServers = _L3tcServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 37, 2)
)
_L3tcServersTable_Object = MibTable
l3tcServersTable = _L3tcServersTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 37, 2, 1)
)
if mibBuilder.loadTexts:
    l3tcServersTable.setStatus("mandatory")
_L3tcServersEntry_Object = MibTableRow
l3tcServersEntry = _L3tcServersEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 37, 2, 1, 1)
)
l3tcServersEntry.setIndexNames(
    (0, "INTEL-L3TC-MIB", "l3tcServersIndex"),
)
if mibBuilder.loadTexts:
    l3tcServersEntry.setStatus("mandatory")
_L3tcServersIndex_Type = Integer32
_L3tcServersIndex_Object = MibTableColumn
l3tcServersIndex = _L3tcServersIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 37, 2, 1, 1, 1),
    _L3tcServersIndex_Type()
)
l3tcServersIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3tcServersIndex.setStatus("mandatory")
_L3tcServersIpAddress_Type = IpAddress
_L3tcServersIpAddress_Object = MibTableColumn
l3tcServersIpAddress = _L3tcServersIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 37, 2, 1, 1, 2),
    _L3tcServersIpAddress_Type()
)
l3tcServersIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3tcServersIpAddress.setStatus("mandatory")
_L3tcServersDeleteEntry_Type = Integer32
_L3tcServersDeleteEntry_Object = MibTableColumn
l3tcServersDeleteEntry = _L3tcServersDeleteEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 37, 2, 1, 1, 3),
    _L3tcServersDeleteEntry_Type()
)
l3tcServersDeleteEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3tcServersDeleteEntry.setStatus("mandatory")
_L3tcServersPortNumber_Type = Integer32
_L3tcServersPortNumber_Object = MibTableColumn
l3tcServersPortNumber = _L3tcServersPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 37, 2, 1, 1, 4),
    _L3tcServersPortNumber_Type()
)
l3tcServersPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3tcServersPortNumber.setStatus("mandatory")


class _L3tcServersHeartBeatUrl_Type(DisplayString):
    """Custom type l3tcServersHeartBeatUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(80, 80),
    )


_L3tcServersHeartBeatUrl_Type.__name__ = "DisplayString"
_L3tcServersHeartBeatUrl_Object = MibTableColumn
l3tcServersHeartBeatUrl = _L3tcServersHeartBeatUrl_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 37, 2, 1, 1, 5),
    _L3tcServersHeartBeatUrl_Type()
)
l3tcServersHeartBeatUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3tcServersHeartBeatUrl.setStatus("mandatory")


class _L3tcServersName_Type(DisplayString):
    """Custom type l3tcServersName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_L3tcServersName_Type.__name__ = "DisplayString"
_L3tcServersName_Object = MibTableColumn
l3tcServersName = _L3tcServersName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 37, 2, 1, 1, 6),
    _L3tcServersName_Type()
)
l3tcServersName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3tcServersName.setStatus("mandatory")


class _L3tcServersHeartBeatStatus_Type(Integer32):
    """Custom type l3tcServersHeartBeatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noResponse", 3),
          ("ok", 1),
          ("retrying", 2))
    )


_L3tcServersHeartBeatStatus_Type.__name__ = "Integer32"
_L3tcServersHeartBeatStatus_Object = MibTableColumn
l3tcServersHeartBeatStatus = _L3tcServersHeartBeatStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 37, 2, 1, 1, 7),
    _L3tcServersHeartBeatStatus_Type()
)
l3tcServersHeartBeatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3tcServersHeartBeatStatus.setStatus("mandatory")
_L3tcTcpPorts_ObjectIdentity = ObjectIdentity
l3tcTcpPorts = _L3tcTcpPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 37, 3)
)
_L3tcTcpPortsTable_Object = MibTable
l3tcTcpPortsTable = _L3tcTcpPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 37, 3, 1)
)
if mibBuilder.loadTexts:
    l3tcTcpPortsTable.setStatus("mandatory")
_L3tcTcpPortsEntry_Object = MibTableRow
l3tcTcpPortsEntry = _L3tcTcpPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 37, 3, 1, 1)
)
l3tcTcpPortsEntry.setIndexNames(
    (0, "INTEL-L3TC-MIB", "l3tcTcpPortsNumber"),
)
if mibBuilder.loadTexts:
    l3tcTcpPortsEntry.setStatus("mandatory")
_L3tcTcpPortsNumber_Type = Integer32
_L3tcTcpPortsNumber_Object = MibTableColumn
l3tcTcpPortsNumber = _L3tcTcpPortsNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 37, 3, 1, 1, 1),
    _L3tcTcpPortsNumber_Type()
)
l3tcTcpPortsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3tcTcpPortsNumber.setStatus("mandatory")
_L3tcTcpPortsDeleteEntry_Type = Integer32
_L3tcTcpPortsDeleteEntry_Object = MibTableColumn
l3tcTcpPortsDeleteEntry = _L3tcTcpPortsDeleteEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 37, 3, 1, 1, 2),
    _L3tcTcpPortsDeleteEntry_Type()
)
l3tcTcpPortsDeleteEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3tcTcpPortsDeleteEntry.setStatus("mandatory")
_L3tcStaticIPs_ObjectIdentity = ObjectIdentity
l3tcStaticIPs = _L3tcStaticIPs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 37, 4)
)
_L3tcStaticIPsTable_Object = MibTable
l3tcStaticIPsTable = _L3tcStaticIPsTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 37, 4, 1)
)
if mibBuilder.loadTexts:
    l3tcStaticIPsTable.setStatus("mandatory")
_L3tcStaticIPsEntry_Object = MibTableRow
l3tcStaticIPsEntry = _L3tcStaticIPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 37, 4, 1, 1)
)
l3tcStaticIPsEntry.setIndexNames(
    (0, "INTEL-L3TC-MIB", "l3tcStaticIPsPacketDestIP"),
)
if mibBuilder.loadTexts:
    l3tcStaticIPsEntry.setStatus("mandatory")
_L3tcStaticIPsPacketDestIP_Type = IpAddress
_L3tcStaticIPsPacketDestIP_Object = MibTableColumn
l3tcStaticIPsPacketDestIP = _L3tcStaticIPsPacketDestIP_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 37, 4, 1, 1, 1),
    _L3tcStaticIPsPacketDestIP_Type()
)
l3tcStaticIPsPacketDestIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3tcStaticIPsPacketDestIP.setStatus("mandatory")
_L3tcStaticIPsDeleteEntry_Type = Integer32
_L3tcStaticIPsDeleteEntry_Object = MibTableColumn
l3tcStaticIPsDeleteEntry = _L3tcStaticIPsDeleteEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 37, 4, 1, 1, 2),
    _L3tcStaticIPsDeleteEntry_Type()
)
l3tcStaticIPsDeleteEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3tcStaticIPsDeleteEntry.setStatus("mandatory")
_L3tcStaticIPsServerIndex_Type = Integer32
_L3tcStaticIPsServerIndex_Object = MibTableColumn
l3tcStaticIPsServerIndex = _L3tcStaticIPsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 37, 4, 1, 1, 3),
    _L3tcStaticIPsServerIndex_Type()
)
l3tcStaticIPsServerIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3tcStaticIPsServerIndex.setStatus("mandatory")
_L3tcSingleAttrs_ObjectIdentity = ObjectIdentity
l3tcSingleAttrs = _L3tcSingleAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 37, 5)
)
_L3tcPollingInterval_Type = Integer32
_L3tcPollingInterval_Object = MibScalar
l3tcPollingInterval = _L3tcPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 37, 5, 1),
    _L3tcPollingInterval_Type()
)
l3tcPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3tcPollingInterval.setStatus("mandatory")


class _L3tcEnabled_Type(Integer32):
    """Custom type l3tcEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_L3tcEnabled_Type.__name__ = "Integer32"
_L3tcEnabled_Object = MibScalar
l3tcEnabled = _L3tcEnabled_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 37, 5, 2),
    _L3tcEnabled_Type()
)
l3tcEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3tcEnabled.setStatus("mandatory")
_L3tcRevertToDefaults_Type = Integer32
_L3tcRevertToDefaults_Object = MibScalar
l3tcRevertToDefaults = _L3tcRevertToDefaults_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 37, 5, 3),
    _L3tcRevertToDefaults_Type()
)
l3tcRevertToDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3tcRevertToDefaults.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-L3TC-MIB",
    **{"l3tcache": l3tcache,
       "l3tcFrontPorts": l3tcFrontPorts,
       "l3tcFrontPortsTable": l3tcFrontPortsTable,
       "l3tcFrontPortsEntry": l3tcFrontPortsEntry,
       "l3tcFrontPortsNumber": l3tcFrontPortsNumber,
       "l3tcFrontPortsMode": l3tcFrontPortsMode,
       "l3tcServers": l3tcServers,
       "l3tcServersTable": l3tcServersTable,
       "l3tcServersEntry": l3tcServersEntry,
       "l3tcServersIndex": l3tcServersIndex,
       "l3tcServersIpAddress": l3tcServersIpAddress,
       "l3tcServersDeleteEntry": l3tcServersDeleteEntry,
       "l3tcServersPortNumber": l3tcServersPortNumber,
       "l3tcServersHeartBeatUrl": l3tcServersHeartBeatUrl,
       "l3tcServersName": l3tcServersName,
       "l3tcServersHeartBeatStatus": l3tcServersHeartBeatStatus,
       "l3tcTcpPorts": l3tcTcpPorts,
       "l3tcTcpPortsTable": l3tcTcpPortsTable,
       "l3tcTcpPortsEntry": l3tcTcpPortsEntry,
       "l3tcTcpPortsNumber": l3tcTcpPortsNumber,
       "l3tcTcpPortsDeleteEntry": l3tcTcpPortsDeleteEntry,
       "l3tcStaticIPs": l3tcStaticIPs,
       "l3tcStaticIPsTable": l3tcStaticIPsTable,
       "l3tcStaticIPsEntry": l3tcStaticIPsEntry,
       "l3tcStaticIPsPacketDestIP": l3tcStaticIPsPacketDestIP,
       "l3tcStaticIPsDeleteEntry": l3tcStaticIPsDeleteEntry,
       "l3tcStaticIPsServerIndex": l3tcStaticIPsServerIndex,
       "l3tcSingleAttrs": l3tcSingleAttrs,
       "l3tcPollingInterval": l3tcPollingInterval,
       "l3tcEnabled": l3tcEnabled,
       "l3tcRevertToDefaults": l3tcRevertToDefaults}
)
