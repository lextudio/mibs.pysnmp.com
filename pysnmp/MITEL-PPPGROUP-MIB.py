# SNMP MIB module (MITEL-PPPGROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MITEL-PPPGROUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:27 2024
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

mitelRouterPppGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 2)
)
mitelRouterPppGroup.setRevisions(
        ("2003-03-24 10:33",
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
_MitelPppGrpGlobalGroup_ObjectIdentity = ObjectIdentity
mitelPppGrpGlobalGroup = _MitelPppGrpGlobalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 2, 1)
)


class _MitelGblGrpNegotiateFirst_Type(Integer32):
    """Custom type mitelGblGrpNegotiateFirst based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chap", 1),
          ("mschap", 3),
          ("pap", 2))
    )


_MitelGblGrpNegotiateFirst_Type.__name__ = "Integer32"
_MitelGblGrpNegotiateFirst_Object = MibScalar
mitelGblGrpNegotiateFirst = _MitelGblGrpNegotiateFirst_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 2, 1, 1),
    _MitelGblGrpNegotiateFirst_Type()
)
mitelGblGrpNegotiateFirst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelGblGrpNegotiateFirst.setStatus("current")
_MitelGblGrpDynamicIpAddr_Type = IpAddress
_MitelGblGrpDynamicIpAddr_Object = MibScalar
mitelGblGrpDynamicIpAddr = _MitelGblGrpDynamicIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 2, 1, 2),
    _MitelGblGrpDynamicIpAddr_Type()
)
mitelGblGrpDynamicIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelGblGrpDynamicIpAddr.setStatus("current")


class _MitelGblGrpNumDynamicIpAddr_Type(Integer32):
    """Custom type mitelGblGrpNumDynamicIpAddr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_MitelGblGrpNumDynamicIpAddr_Type.__name__ = "Integer32"
_MitelGblGrpNumDynamicIpAddr_Object = MibScalar
mitelGblGrpNumDynamicIpAddr = _MitelGblGrpNumDynamicIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 2, 1, 3),
    _MitelGblGrpNumDynamicIpAddr_Type()
)
mitelGblGrpNumDynamicIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelGblGrpNumDynamicIpAddr.setStatus("current")


class _MitelGblGrpDynamicIpAdrrHoldoff_Type(Integer32):
    """Custom type mitelGblGrpDynamicIpAdrrHoldoff based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_MitelGblGrpDynamicIpAdrrHoldoff_Type.__name__ = "Integer32"
_MitelGblGrpDynamicIpAdrrHoldoff_Object = MibScalar
mitelGblGrpDynamicIpAdrrHoldoff = _MitelGblGrpDynamicIpAdrrHoldoff_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 2, 1, 4),
    _MitelGblGrpDynamicIpAdrrHoldoff_Type()
)
mitelGblGrpDynamicIpAdrrHoldoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelGblGrpDynamicIpAdrrHoldoff.setStatus("current")


class _MitelGblGrpRemDnsIpAddrHandling_Type(Integer32):
    """Custom type mitelGblGrpRemDnsIpAddrHandling based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("override", 2),
          ("overridewith", 3))
    )


_MitelGblGrpRemDnsIpAddrHandling_Type.__name__ = "Integer32"
_MitelGblGrpRemDnsIpAddrHandling_Object = MibScalar
mitelGblGrpRemDnsIpAddrHandling = _MitelGblGrpRemDnsIpAddrHandling_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 2, 1, 5),
    _MitelGblGrpRemDnsIpAddrHandling_Type()
)
mitelGblGrpRemDnsIpAddrHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelGblGrpRemDnsIpAddrHandling.setStatus("current")
_MitelGblGrpPrimaryWinsServerIpAddr_Type = IpAddress
_MitelGblGrpPrimaryWinsServerIpAddr_Object = MibScalar
mitelGblGrpPrimaryWinsServerIpAddr = _MitelGblGrpPrimaryWinsServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 2, 1, 6),
    _MitelGblGrpPrimaryWinsServerIpAddr_Type()
)
mitelGblGrpPrimaryWinsServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelGblGrpPrimaryWinsServerIpAddr.setStatus("current")
_MitelGblGrpSecondaryWinsServerIpAddr_Type = IpAddress
_MitelGblGrpSecondaryWinsServerIpAddr_Object = MibScalar
mitelGblGrpSecondaryWinsServerIpAddr = _MitelGblGrpSecondaryWinsServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 2, 1, 7),
    _MitelGblGrpSecondaryWinsServerIpAddr_Type()
)
mitelGblGrpSecondaryWinsServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelGblGrpSecondaryWinsServerIpAddr.setStatus("current")
_MitelPppGrpRemoteConfigTable_Object = MibTable
mitelPppGrpRemoteConfigTable = _MitelPppGrpRemoteConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mitelPppGrpRemoteConfigTable.setStatus("current")
_MitelPppGrpRemoteConfigEntry_Object = MibTableRow
mitelPppGrpRemoteConfigEntry = _MitelPppGrpRemoteConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 2, 2, 1)
)
mitelPppGrpRemoteConfigEntry.setIndexNames(
    (0, "MITEL-PPPGROUP-MIB", "mitelRmtCfgTableIndex"),
)
if mibBuilder.loadTexts:
    mitelPppGrpRemoteConfigEntry.setStatus("current")
_MitelRmtCfgTableIndex_Type = Integer32
_MitelRmtCfgTableIndex_Object = MibTableColumn
mitelRmtCfgTableIndex = _MitelRmtCfgTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 2, 2, 1, 1),
    _MitelRmtCfgTableIndex_Type()
)
mitelRmtCfgTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelRmtCfgTableIndex.setStatus("current")


class _MitelRmtCfgTableIpAddrHandling_Type(Integer32):
    """Custom type mitelRmtCfgTableIpAddrHandling based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("assign", 3),
          ("override", 2))
    )


_MitelRmtCfgTableIpAddrHandling_Type.__name__ = "Integer32"
_MitelRmtCfgTableIpAddrHandling_Object = MibTableColumn
mitelRmtCfgTableIpAddrHandling = _MitelRmtCfgTableIpAddrHandling_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 2, 2, 1, 2),
    _MitelRmtCfgTableIpAddrHandling_Type()
)
mitelRmtCfgTableIpAddrHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelRmtCfgTableIpAddrHandling.setStatus("current")
_MitelRmtCfgTableRemIpAddr_Type = IpAddress
_MitelRmtCfgTableRemIpAddr_Object = MibTableColumn
mitelRmtCfgTableRemIpAddr = _MitelRmtCfgTableRemIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 2, 2, 1, 3),
    _MitelRmtCfgTableRemIpAddr_Type()
)
mitelRmtCfgTableRemIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelRmtCfgTableRemIpAddr.setStatus("current")
_MitelRmtCfgTableStatus_Type = RowStatus
_MitelRmtCfgTableStatus_Object = MibTableColumn
mitelRmtCfgTableStatus = _MitelRmtCfgTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 2, 2, 1, 4),
    _MitelRmtCfgTableStatus_Type()
)
mitelRmtCfgTableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mitelRmtCfgTableStatus.setStatus("current")


class _MitelRmtCfgTablePppMode_Type(Integer32):
    """Custom type mitelRmtCfgTablePppMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("server", 2))
    )


_MitelRmtCfgTablePppMode_Type.__name__ = "Integer32"
_MitelRmtCfgTablePppMode_Object = MibTableColumn
mitelRmtCfgTablePppMode = _MitelRmtCfgTablePppMode_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 2, 2, 1, 5),
    _MitelRmtCfgTablePppMode_Type()
)
mitelRmtCfgTablePppMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelRmtCfgTablePppMode.setStatus("current")
_MitelPppGrpPppOverEthernetTable_Object = MibTable
mitelPppGrpPppOverEthernetTable = _MitelPppGrpPppOverEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mitelPppGrpPppOverEthernetTable.setStatus("current")
_MitelPppGrpPppOverEthernetEntry_Object = MibTableRow
mitelPppGrpPppOverEthernetEntry = _MitelPppGrpPppOverEthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 2, 3, 1)
)
mitelPppGrpPppOverEthernetEntry.setIndexNames(
    (0, "MITEL-PPPGROUP-MIB", "mitelPppOEthTableIndex"),
)
if mibBuilder.loadTexts:
    mitelPppGrpPppOverEthernetEntry.setStatus("current")
_MitelPppOEthTableIndex_Type = Integer32
_MitelPppOEthTableIndex_Object = MibTableColumn
mitelPppOEthTableIndex = _MitelPppOEthTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 2, 3, 1, 1),
    _MitelPppOEthTableIndex_Type()
)
mitelPppOEthTableIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelPppOEthTableIndex.setStatus("current")


class _MitelPppOEthTableEnabled_Type(Integer32):
    """Custom type mitelPppOEthTableEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MitelPppOEthTableEnabled_Type.__name__ = "Integer32"
_MitelPppOEthTableEnabled_Object = MibTableColumn
mitelPppOEthTableEnabled = _MitelPppOEthTableEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 2, 3, 1, 2),
    _MitelPppOEthTableEnabled_Type()
)
mitelPppOEthTableEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelPppOEthTableEnabled.setStatus("current")


class _MitelPppOEthTablePacketTimeout_Type(Integer32):
    """Custom type mitelPppOEthTablePacketTimeout based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MitelPppOEthTablePacketTimeout_Type.__name__ = "Integer32"
_MitelPppOEthTablePacketTimeout_Object = MibTableColumn
mitelPppOEthTablePacketTimeout = _MitelPppOEthTablePacketTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 2, 3, 1, 3),
    _MitelPppOEthTablePacketTimeout_Type()
)
mitelPppOEthTablePacketTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelPppOEthTablePacketTimeout.setStatus("current")


class _MitelPppOEthTablePacketRetries_Type(Integer32):
    """Custom type mitelPppOEthTablePacketRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MitelPppOEthTablePacketRetries_Type.__name__ = "Integer32"
_MitelPppOEthTablePacketRetries_Object = MibTableColumn
mitelPppOEthTablePacketRetries = _MitelPppOEthTablePacketRetries_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 2, 3, 1, 4),
    _MitelPppOEthTablePacketRetries_Type()
)
mitelPppOEthTablePacketRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelPppOEthTablePacketRetries.setStatus("current")


class _MitelPppOEthTableTotalRetries_Type(Integer32):
    """Custom type mitelPppOEthTableTotalRetries based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MitelPppOEthTableTotalRetries_Type.__name__ = "Integer32"
_MitelPppOEthTableTotalRetries_Object = MibTableColumn
mitelPppOEthTableTotalRetries = _MitelPppOEthTableTotalRetries_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 2, 3, 1, 5),
    _MitelPppOEthTableTotalRetries_Type()
)
mitelPppOEthTableTotalRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelPppOEthTableTotalRetries.setStatus("current")


class _MitelPppOEthTableServiceName_Type(OctetString):
    """Custom type mitelPppOEthTableServiceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_MitelPppOEthTableServiceName_Type.__name__ = "OctetString"
_MitelPppOEthTableServiceName_Object = MibTableColumn
mitelPppOEthTableServiceName = _MitelPppOEthTableServiceName_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 2, 3, 1, 6),
    _MitelPppOEthTableServiceName_Type()
)
mitelPppOEthTableServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelPppOEthTableServiceName.setStatus("current")


class _MitelPppOEthTableACName_Type(OctetString):
    """Custom type mitelPppOEthTableACName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_MitelPppOEthTableACName_Type.__name__ = "OctetString"
_MitelPppOEthTableACName_Object = MibTableColumn
mitelPppOEthTableACName = _MitelPppOEthTableACName_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 2, 3, 1, 7),
    _MitelPppOEthTableACName_Type()
)
mitelPppOEthTableACName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelPppOEthTableACName.setStatus("current")
_MitelPppOEthTableStatus_Type = RowStatus
_MitelPppOEthTableStatus_Object = MibTableColumn
mitelPppOEthTableStatus = _MitelPppOEthTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 2, 3, 1, 8),
    _MitelPppOEthTableStatus_Type()
)
mitelPppOEthTableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mitelPppOEthTableStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MITEL-PPPGROUP-MIB",
    **{"mitel": mitel,
       "mitelProprietary": mitelProprietary,
       "mitelPropIpNetworking": mitelPropIpNetworking,
       "mitelIpNetRouter": mitelIpNetRouter,
       "mitelRouterPppGroup": mitelRouterPppGroup,
       "mitelPppGrpGlobalGroup": mitelPppGrpGlobalGroup,
       "mitelGblGrpNegotiateFirst": mitelGblGrpNegotiateFirst,
       "mitelGblGrpDynamicIpAddr": mitelGblGrpDynamicIpAddr,
       "mitelGblGrpNumDynamicIpAddr": mitelGblGrpNumDynamicIpAddr,
       "mitelGblGrpDynamicIpAdrrHoldoff": mitelGblGrpDynamicIpAdrrHoldoff,
       "mitelGblGrpRemDnsIpAddrHandling": mitelGblGrpRemDnsIpAddrHandling,
       "mitelGblGrpPrimaryWinsServerIpAddr": mitelGblGrpPrimaryWinsServerIpAddr,
       "mitelGblGrpSecondaryWinsServerIpAddr": mitelGblGrpSecondaryWinsServerIpAddr,
       "mitelPppGrpRemoteConfigTable": mitelPppGrpRemoteConfigTable,
       "mitelPppGrpRemoteConfigEntry": mitelPppGrpRemoteConfigEntry,
       "mitelRmtCfgTableIndex": mitelRmtCfgTableIndex,
       "mitelRmtCfgTableIpAddrHandling": mitelRmtCfgTableIpAddrHandling,
       "mitelRmtCfgTableRemIpAddr": mitelRmtCfgTableRemIpAddr,
       "mitelRmtCfgTableStatus": mitelRmtCfgTableStatus,
       "mitelRmtCfgTablePppMode": mitelRmtCfgTablePppMode,
       "mitelPppGrpPppOverEthernetTable": mitelPppGrpPppOverEthernetTable,
       "mitelPppGrpPppOverEthernetEntry": mitelPppGrpPppOverEthernetEntry,
       "mitelPppOEthTableIndex": mitelPppOEthTableIndex,
       "mitelPppOEthTableEnabled": mitelPppOEthTableEnabled,
       "mitelPppOEthTablePacketTimeout": mitelPppOEthTablePacketTimeout,
       "mitelPppOEthTablePacketRetries": mitelPppOEthTablePacketRetries,
       "mitelPppOEthTableTotalRetries": mitelPppOEthTableTotalRetries,
       "mitelPppOEthTableServiceName": mitelPppOEthTableServiceName,
       "mitelPppOEthTableACName": mitelPppOEthTableACName,
       "mitelPppOEthTableStatus": mitelPppOEthTableStatus}
)
