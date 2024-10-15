# SNMP MIB module (Wellfleet-GRE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-GRE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:18 2024
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

(wfGreGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfGreGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfGreInterfaceTable_Object = MibTable
wfGreInterfaceTable = _WfGreInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 1)
)
if mibBuilder.loadTexts:
    wfGreInterfaceTable.setStatus("mandatory")
_WfGreInterfaceEntry_Object = MibTableRow
wfGreInterfaceEntry = _WfGreInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 1, 1)
)
wfGreInterfaceEntry.setIndexNames(
    (0, "Wellfleet-GRE-MIB", "wfGreIntfIpAddr"),
    (0, "Wellfleet-GRE-MIB", "wfGreIntfCct"),
)
if mibBuilder.loadTexts:
    wfGreInterfaceEntry.setStatus("mandatory")


class _WfGreIntfCreate_Type(Integer32):
    """Custom type wfGreIntfCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfGreIntfCreate_Type.__name__ = "Integer32"
_WfGreIntfCreate_Object = MibTableColumn
wfGreIntfCreate = _WfGreIntfCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 1, 1, 1),
    _WfGreIntfCreate_Type()
)
wfGreIntfCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfGreIntfCreate.setStatus("mandatory")


class _WfGreIntfEnable_Type(Integer32):
    """Custom type wfGreIntfEnable based on Integer32"""
    defaultValue = 1

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


_WfGreIntfEnable_Type.__name__ = "Integer32"
_WfGreIntfEnable_Object = MibTableColumn
wfGreIntfEnable = _WfGreIntfEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 1, 1, 2),
    _WfGreIntfEnable_Type()
)
wfGreIntfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfGreIntfEnable.setStatus("mandatory")


class _WfGreIntfState_Type(Integer32):
    """Custom type wfGreIntfState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpres", 4),
          ("up", 1))
    )


_WfGreIntfState_Type.__name__ = "Integer32"
_WfGreIntfState_Object = MibTableColumn
wfGreIntfState = _WfGreIntfState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 1, 1, 3),
    _WfGreIntfState_Type()
)
wfGreIntfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfGreIntfState.setStatus("mandatory")
_WfGreIntfIpAddr_Type = IpAddress
_WfGreIntfIpAddr_Object = MibTableColumn
wfGreIntfIpAddr = _WfGreIntfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 1, 1, 4),
    _WfGreIntfIpAddr_Type()
)
wfGreIntfIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfGreIntfIpAddr.setStatus("mandatory")
_WfGreIntfCct_Type = Integer32
_WfGreIntfCct_Object = MibTableColumn
wfGreIntfCct = _WfGreIntfCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 1, 1, 5),
    _WfGreIntfCct_Type()
)
wfGreIntfCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfGreIntfCct.setStatus("mandatory")


class _WfGreIntfStatsEnable_Type(Integer32):
    """Custom type wfGreIntfStatsEnable based on Integer32"""
    defaultValue = 1

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


_WfGreIntfStatsEnable_Type.__name__ = "Integer32"
_WfGreIntfStatsEnable_Object = MibTableColumn
wfGreIntfStatsEnable = _WfGreIntfStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 1, 1, 6),
    _WfGreIntfStatsEnable_Type()
)
wfGreIntfStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfGreIntfStatsEnable.setStatus("mandatory")
_WfGreIntfDebugLevel_Type = Integer32
_WfGreIntfDebugLevel_Object = MibTableColumn
wfGreIntfDebugLevel = _WfGreIntfDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 1, 1, 7),
    _WfGreIntfDebugLevel_Type()
)
wfGreIntfDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfGreIntfDebugLevel.setStatus("mandatory")
_WfGreTunnelTable_Object = MibTable
wfGreTunnelTable = _WfGreTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2)
)
if mibBuilder.loadTexts:
    wfGreTunnelTable.setStatus("mandatory")
_WfGreTunnelEntry_Object = MibTableRow
wfGreTunnelEntry = _WfGreTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1)
)
wfGreTunnelEntry.setIndexNames(
    (0, "Wellfleet-GRE-MIB", "wfGreTunnelLocalAddr"),
    (0, "Wellfleet-GRE-MIB", "wfGreTunnelPeerAddress"),
    (0, "Wellfleet-GRE-MIB", "wfGreTunnelLocalIndex"),
)
if mibBuilder.loadTexts:
    wfGreTunnelEntry.setStatus("mandatory")
_WfGreTunnelLocalAddr_Type = IpAddress
_WfGreTunnelLocalAddr_Object = MibTableColumn
wfGreTunnelLocalAddr = _WfGreTunnelLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 1),
    _WfGreTunnelLocalAddr_Type()
)
wfGreTunnelLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfGreTunnelLocalAddr.setStatus("mandatory")


class _WfGreTunnelLocalIndex_Type(Integer32):
    """Custom type wfGreTunnelLocalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfGreTunnelLocalIndex_Type.__name__ = "Integer32"
_WfGreTunnelLocalIndex_Object = MibTableColumn
wfGreTunnelLocalIndex = _WfGreTunnelLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 2),
    _WfGreTunnelLocalIndex_Type()
)
wfGreTunnelLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfGreTunnelLocalIndex.setStatus("mandatory")


class _WfGreTunnelType_Type(Integer32):
    """Custom type wfGreTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("generic", 1),
          ("udas", 2))
    )


_WfGreTunnelType_Type.__name__ = "Integer32"
_WfGreTunnelType_Object = MibTableColumn
wfGreTunnelType = _WfGreTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 3),
    _WfGreTunnelType_Type()
)
wfGreTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfGreTunnelType.setStatus("mandatory")


class _WfGreTunnelId_Type(Integer32):
    """Custom type wfGreTunnelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfGreTunnelId_Type.__name__ = "Integer32"
_WfGreTunnelId_Object = MibTableColumn
wfGreTunnelId = _WfGreTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 4),
    _WfGreTunnelId_Type()
)
wfGreTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfGreTunnelId.setStatus("mandatory")
_WfGreTunnelPeerAddress_Type = IpAddress
_WfGreTunnelPeerAddress_Object = MibTableColumn
wfGreTunnelPeerAddress = _WfGreTunnelPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 5),
    _WfGreTunnelPeerAddress_Type()
)
wfGreTunnelPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfGreTunnelPeerAddress.setStatus("mandatory")


class _WfGreRemotePayloadAddress_Type(OctetString):
    """Custom type wfGreRemotePayloadAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_WfGreRemotePayloadAddress_Type.__name__ = "OctetString"
_WfGreRemotePayloadAddress_Object = MibTableColumn
wfGreRemotePayloadAddress = _WfGreRemotePayloadAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 6),
    _WfGreRemotePayloadAddress_Type()
)
wfGreRemotePayloadAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfGreRemotePayloadAddress.setStatus("deprecated")


class _WfGreTunnelState_Type(Integer32):
    """Custom type wfGreTunnelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_WfGreTunnelState_Type.__name__ = "Integer32"
_WfGreTunnelState_Object = MibTableColumn
wfGreTunnelState = _WfGreTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 7),
    _WfGreTunnelState_Type()
)
wfGreTunnelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfGreTunnelState.setStatus("mandatory")


class _WfGreVersion_Type(Integer32):
    """Custom type wfGreVersion based on Integer32"""
    defaultValue = 0


_WfGreVersion_Object = MibTableColumn
wfGreVersion = _WfGreVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 8),
    _WfGreVersion_Type()
)
wfGreVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfGreVersion.setStatus("mandatory")
_WfGreProtoMap_Type = OctetString
_WfGreProtoMap_Object = MibTableColumn
wfGreProtoMap = _WfGreProtoMap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 9),
    _WfGreProtoMap_Type()
)
wfGreProtoMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfGreProtoMap.setStatus("mandatory")
_WfGreTunnelPktsTx_Type = Counter32
_WfGreTunnelPktsTx_Object = MibTableColumn
wfGreTunnelPktsTx = _WfGreTunnelPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 10),
    _WfGreTunnelPktsTx_Type()
)
wfGreTunnelPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfGreTunnelPktsTx.setStatus("mandatory")
_WfGreTunnelPktsRx_Type = Counter32
_WfGreTunnelPktsRx_Object = MibTableColumn
wfGreTunnelPktsRx = _WfGreTunnelPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 11),
    _WfGreTunnelPktsRx_Type()
)
wfGreTunnelPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfGreTunnelPktsRx.setStatus("mandatory")
_WfGreTunnelBytesTx_Type = Counter32
_WfGreTunnelBytesTx_Object = MibTableColumn
wfGreTunnelBytesTx = _WfGreTunnelBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 12),
    _WfGreTunnelBytesTx_Type()
)
wfGreTunnelBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfGreTunnelBytesTx.setStatus("mandatory")
_WfGreTunnelBytesRx_Type = Counter32
_WfGreTunnelBytesRx_Object = MibTableColumn
wfGreTunnelBytesRx = _WfGreTunnelBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 13),
    _WfGreTunnelBytesRx_Type()
)
wfGreTunnelBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfGreTunnelBytesRx.setStatus("mandatory")
_WfGreTunnelPktsTxDropped_Type = Counter32
_WfGreTunnelPktsTxDropped_Object = MibTableColumn
wfGreTunnelPktsTxDropped = _WfGreTunnelPktsTxDropped_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 14),
    _WfGreTunnelPktsTxDropped_Type()
)
wfGreTunnelPktsTxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfGreTunnelPktsTxDropped.setStatus("mandatory")
_WfGreTunnelPktsRxDropped_Type = Counter32
_WfGreTunnelPktsRxDropped_Object = MibTableColumn
wfGreTunnelPktsRxDropped = _WfGreTunnelPktsRxDropped_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 15),
    _WfGreTunnelPktsRxDropped_Type()
)
wfGreTunnelPktsRxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfGreTunnelPktsRxDropped.setStatus("mandatory")
_WfGreTunnelXsumErr_Type = Counter32
_WfGreTunnelXsumErr_Object = MibTableColumn
wfGreTunnelXsumErr = _WfGreTunnelXsumErr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 16),
    _WfGreTunnelXsumErr_Type()
)
wfGreTunnelXsumErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfGreTunnelXsumErr.setStatus("mandatory")
_WfGreTunnelSeqNumErr_Type = Counter32
_WfGreTunnelSeqNumErr_Object = MibTableColumn
wfGreTunnelSeqNumErr = _WfGreTunnelSeqNumErr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 17),
    _WfGreTunnelSeqNumErr_Type()
)
wfGreTunnelSeqNumErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfGreTunnelSeqNumErr.setStatus("mandatory")


class _WfGreTunnelMtu_Type(Integer32):
    """Custom type wfGreTunnelMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4500),
    )


_WfGreTunnelMtu_Type.__name__ = "Integer32"
_WfGreTunnelMtu_Object = MibTableColumn
wfGreTunnelMtu = _WfGreTunnelMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 18),
    _WfGreTunnelMtu_Type()
)
wfGreTunnelMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfGreTunnelMtu.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-GRE-MIB",
    **{"wfGreInterfaceTable": wfGreInterfaceTable,
       "wfGreInterfaceEntry": wfGreInterfaceEntry,
       "wfGreIntfCreate": wfGreIntfCreate,
       "wfGreIntfEnable": wfGreIntfEnable,
       "wfGreIntfState": wfGreIntfState,
       "wfGreIntfIpAddr": wfGreIntfIpAddr,
       "wfGreIntfCct": wfGreIntfCct,
       "wfGreIntfStatsEnable": wfGreIntfStatsEnable,
       "wfGreIntfDebugLevel": wfGreIntfDebugLevel,
       "wfGreTunnelTable": wfGreTunnelTable,
       "wfGreTunnelEntry": wfGreTunnelEntry,
       "wfGreTunnelLocalAddr": wfGreTunnelLocalAddr,
       "wfGreTunnelLocalIndex": wfGreTunnelLocalIndex,
       "wfGreTunnelType": wfGreTunnelType,
       "wfGreTunnelId": wfGreTunnelId,
       "wfGreTunnelPeerAddress": wfGreTunnelPeerAddress,
       "wfGreRemotePayloadAddress": wfGreRemotePayloadAddress,
       "wfGreTunnelState": wfGreTunnelState,
       "wfGreVersion": wfGreVersion,
       "wfGreProtoMap": wfGreProtoMap,
       "wfGreTunnelPktsTx": wfGreTunnelPktsTx,
       "wfGreTunnelPktsRx": wfGreTunnelPktsRx,
       "wfGreTunnelBytesTx": wfGreTunnelBytesTx,
       "wfGreTunnelBytesRx": wfGreTunnelBytesRx,
       "wfGreTunnelPktsTxDropped": wfGreTunnelPktsTxDropped,
       "wfGreTunnelPktsRxDropped": wfGreTunnelPktsRxDropped,
       "wfGreTunnelXsumErr": wfGreTunnelXsumErr,
       "wfGreTunnelSeqNumErr": wfGreTunnelSeqNumErr,
       "wfGreTunnelMtu": wfGreTunnelMtu}
)
