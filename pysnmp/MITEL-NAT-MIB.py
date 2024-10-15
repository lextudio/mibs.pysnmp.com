# SNMP MIB module (MITEL-NAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MITEL-NAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:26 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

mitelIpGrpNatGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2)
)
mitelIpGrpNatGroup.setRevisions(
        ("2003-03-24 10:01",
         "1999-03-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mitel_ObjectIdentity = ObjectIdentity
mitel = _Mitel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027)
)
_MitelProprietary_ObjectIdentity = ObjectIdentity
mitelProprietary = _MitelProprietary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4)
)
_MitelPropIpNetworking_ObjectIdentity = ObjectIdentity
mitelPropIpNetworking = _MitelPropIpNetworking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8)
)
_MitelIpNetRouter_ObjectIdentity = ObjectIdentity
mitelIpNetRouter = _MitelIpNetRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1)
)
_MitelRouterIpGroup_ObjectIdentity = ObjectIdentity
mitelRouterIpGroup = _MitelRouterIpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1)
)
_MitelNatGrpIfTable_Object = MibTable
mitelNatGrpIfTable = _MitelNatGrpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mitelNatGrpIfTable.setStatus("current")
_MitelNatGrpIfEntry_Object = MibTableRow
mitelNatGrpIfEntry = _MitelNatGrpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 1, 1)
)
mitelNatGrpIfEntry.setIndexNames(
    (0, "MITEL-NAT-MIB", "mitelNatGrpIfAddr"),
)
if mibBuilder.loadTexts:
    mitelNatGrpIfEntry.setStatus("current")
_MitelNatGrpIfAddr_Type = IpAddress
_MitelNatGrpIfAddr_Object = MibTableColumn
mitelNatGrpIfAddr = _MitelNatGrpIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 1, 1, 1),
    _MitelNatGrpIfAddr_Type()
)
mitelNatGrpIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelNatGrpIfAddr.setStatus("current")


class _MitelNatGrpIfEnable_Type(Integer32):
    """Custom type mitelNatGrpIfEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MitelNatGrpIfEnable_Type.__name__ = "Integer32"
_MitelNatGrpIfEnable_Object = MibTableColumn
mitelNatGrpIfEnable = _MitelNatGrpIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 1, 1, 2),
    _MitelNatGrpIfEnable_Type()
)
mitelNatGrpIfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelNatGrpIfEnable.setStatus("current")


class _MitelNatGrpIfUdpLifetime_Type(Integer32):
    """Custom type mitelNatGrpIfUdpLifetime based on Integer32"""
    defaultValue = 900


_MitelNatGrpIfUdpLifetime_Object = MibTableColumn
mitelNatGrpIfUdpLifetime = _MitelNatGrpIfUdpLifetime_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 1, 1, 3),
    _MitelNatGrpIfUdpLifetime_Type()
)
mitelNatGrpIfUdpLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelNatGrpIfUdpLifetime.setStatus("current")


class _MitelNatGrpIfTcpLifetime_Type(Integer32):
    """Custom type mitelNatGrpIfTcpLifetime based on Integer32"""
    defaultValue = 900


_MitelNatGrpIfTcpLifetime_Object = MibTableColumn
mitelNatGrpIfTcpLifetime = _MitelNatGrpIfTcpLifetime_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 1, 1, 4),
    _MitelNatGrpIfTcpLifetime_Type()
)
mitelNatGrpIfTcpLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelNatGrpIfTcpLifetime.setStatus("current")


class _MitelNatGrpIfTcpFinLifetime_Type(Integer32):
    """Custom type mitelNatGrpIfTcpFinLifetime based on Integer32"""
    defaultValue = 120


_MitelNatGrpIfTcpFinLifetime_Object = MibTableColumn
mitelNatGrpIfTcpFinLifetime = _MitelNatGrpIfTcpFinLifetime_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 1, 1, 5),
    _MitelNatGrpIfTcpFinLifetime_Type()
)
mitelNatGrpIfTcpFinLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelNatGrpIfTcpFinLifetime.setStatus("current")


class _MitelNatGrpIfTcpRstLifetime_Type(Integer32):
    """Custom type mitelNatGrpIfTcpRstLifetime based on Integer32"""
    defaultValue = 120


_MitelNatGrpIfTcpRstLifetime_Object = MibTableColumn
mitelNatGrpIfTcpRstLifetime = _MitelNatGrpIfTcpRstLifetime_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 1, 1, 6),
    _MitelNatGrpIfTcpRstLifetime_Type()
)
mitelNatGrpIfTcpRstLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelNatGrpIfTcpRstLifetime.setStatus("current")


class _MitelNatGrpIfPingLifetime_Type(Integer32):
    """Custom type mitelNatGrpIfPingLifetime based on Integer32"""
    defaultValue = 120


_MitelNatGrpIfPingLifetime_Object = MibTableColumn
mitelNatGrpIfPingLifetime = _MitelNatGrpIfPingLifetime_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 1, 1, 7),
    _MitelNatGrpIfPingLifetime_Type()
)
mitelNatGrpIfPingLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelNatGrpIfPingLifetime.setStatus("current")
_MitelNatGrpIfStatus_Type = RowStatus
_MitelNatGrpIfStatus_Object = MibTableColumn
mitelNatGrpIfStatus = _MitelNatGrpIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 1, 1, 8),
    _MitelNatGrpIfStatus_Type()
)
mitelNatGrpIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mitelNatGrpIfStatus.setStatus("current")
_MitelNatGrpIfIndex_Type = Integer32
_MitelNatGrpIfIndex_Object = MibTableColumn
mitelNatGrpIfIndex = _MitelNatGrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 1, 1, 9),
    _MitelNatGrpIfIndex_Type()
)
mitelNatGrpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelNatGrpIfIndex.setStatus("current")
_MitelNatGrpRedirTable_Object = MibTable
mitelNatGrpRedirTable = _MitelNatGrpRedirTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mitelNatGrpRedirTable.setStatus("current")
_MitelNatGrpRedirEntry_Object = MibTableRow
mitelNatGrpRedirEntry = _MitelNatGrpRedirEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 2, 1)
)
mitelNatGrpRedirEntry.setIndexNames(
    (0, "MITEL-NAT-MIB", "mitelNatGrpRedirOldAddr"),
    (0, "MITEL-NAT-MIB", "mitelNatGrpRedirProto"),
    (0, "MITEL-NAT-MIB", "mitelNatGrpRedirOldPort"),
)
if mibBuilder.loadTexts:
    mitelNatGrpRedirEntry.setStatus("current")
_MitelNatGrpRedirOldAddr_Type = IpAddress
_MitelNatGrpRedirOldAddr_Object = MibTableColumn
mitelNatGrpRedirOldAddr = _MitelNatGrpRedirOldAddr_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 2, 1, 1),
    _MitelNatGrpRedirOldAddr_Type()
)
mitelNatGrpRedirOldAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelNatGrpRedirOldAddr.setStatus("current")
_MitelNatGrpRedirProto_Type = Integer32
_MitelNatGrpRedirProto_Object = MibTableColumn
mitelNatGrpRedirProto = _MitelNatGrpRedirProto_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 2, 1, 2),
    _MitelNatGrpRedirProto_Type()
)
mitelNatGrpRedirProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelNatGrpRedirProto.setStatus("current")
_MitelNatGrpRedirOldPort_Type = Integer32
_MitelNatGrpRedirOldPort_Object = MibTableColumn
mitelNatGrpRedirOldPort = _MitelNatGrpRedirOldPort_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 2, 1, 3),
    _MitelNatGrpRedirOldPort_Type()
)
mitelNatGrpRedirOldPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelNatGrpRedirOldPort.setStatus("current")
_MitelNatGrpRedirNewAddr_Type = IpAddress
_MitelNatGrpRedirNewAddr_Object = MibTableColumn
mitelNatGrpRedirNewAddr = _MitelNatGrpRedirNewAddr_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 2, 1, 4),
    _MitelNatGrpRedirNewAddr_Type()
)
mitelNatGrpRedirNewAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelNatGrpRedirNewAddr.setStatus("current")


class _MitelNatGrpRedirNewPort_Type(Integer32):
    """Custom type mitelNatGrpRedirNewPort based on Integer32"""
    defaultValue = 0


_MitelNatGrpRedirNewPort_Object = MibTableColumn
mitelNatGrpRedirNewPort = _MitelNatGrpRedirNewPort_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 2, 1, 5),
    _MitelNatGrpRedirNewPort_Type()
)
mitelNatGrpRedirNewPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelNatGrpRedirNewPort.setStatus("current")
_MitelNatGrpRedirStatus_Type = RowStatus
_MitelNatGrpRedirStatus_Object = MibTableColumn
mitelNatGrpRedirStatus = _MitelNatGrpRedirStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2, 2, 1, 6),
    _MitelNatGrpRedirStatus_Type()
)
mitelNatGrpRedirStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mitelNatGrpRedirStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MITEL-NAT-MIB",
    **{"mitel": mitel,
       "mitelProprietary": mitelProprietary,
       "mitelPropIpNetworking": mitelPropIpNetworking,
       "mitelIpNetRouter": mitelIpNetRouter,
       "mitelRouterIpGroup": mitelRouterIpGroup,
       "mitelIpGrpNatGroup": mitelIpGrpNatGroup,
       "mitelNatGrpIfTable": mitelNatGrpIfTable,
       "mitelNatGrpIfEntry": mitelNatGrpIfEntry,
       "mitelNatGrpIfAddr": mitelNatGrpIfAddr,
       "mitelNatGrpIfEnable": mitelNatGrpIfEnable,
       "mitelNatGrpIfUdpLifetime": mitelNatGrpIfUdpLifetime,
       "mitelNatGrpIfTcpLifetime": mitelNatGrpIfTcpLifetime,
       "mitelNatGrpIfTcpFinLifetime": mitelNatGrpIfTcpFinLifetime,
       "mitelNatGrpIfTcpRstLifetime": mitelNatGrpIfTcpRstLifetime,
       "mitelNatGrpIfPingLifetime": mitelNatGrpIfPingLifetime,
       "mitelNatGrpIfStatus": mitelNatGrpIfStatus,
       "mitelNatGrpIfIndex": mitelNatGrpIfIndex,
       "mitelNatGrpRedirTable": mitelNatGrpRedirTable,
       "mitelNatGrpRedirEntry": mitelNatGrpRedirEntry,
       "mitelNatGrpRedirOldAddr": mitelNatGrpRedirOldAddr,
       "mitelNatGrpRedirProto": mitelNatGrpRedirProto,
       "mitelNatGrpRedirOldPort": mitelNatGrpRedirOldPort,
       "mitelNatGrpRedirNewAddr": mitelNatGrpRedirNewAddr,
       "mitelNatGrpRedirNewPort": mitelNatGrpRedirNewPort,
       "mitelNatGrpRedirStatus": mitelNatGrpRedirStatus}
)
