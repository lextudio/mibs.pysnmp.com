# SNMP MIB module (SCA-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SCA-TUNNEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:55 2024
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

(scanet,) = mibBuilder.importSymbols(
    "SCANET-MIB",
    "scanet")

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

_Tunnel_ObjectIdentity = ObjectIdentity
tunnel = _Tunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 52)
)
_TunnelInfo_ObjectIdentity = ObjectIdentity
tunnelInfo = _TunnelInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 52, 1)
)
_TunnelInfoTable_Object = MibTable
tunnelInfoTable = _TunnelInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 52, 1, 1)
)
if mibBuilder.loadTexts:
    tunnelInfoTable.setStatus("mandatory")
_TunnelInfoEntry_Object = MibTableRow
tunnelInfoEntry = _TunnelInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 52, 1, 1, 1)
)
tunnelInfoEntry.setIndexNames(
    (0, "SCA-TUNNEL-MIB", "tunnelInfoIfIndex"),
)
if mibBuilder.loadTexts:
    tunnelInfoEntry.setStatus("mandatory")
_TunnelInfoIfIndex_Type = Integer32
_TunnelInfoIfIndex_Object = MibTableColumn
tunnelInfoIfIndex = _TunnelInfoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 52, 1, 1, 1, 1),
    _TunnelInfoIfIndex_Type()
)
tunnelInfoIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelInfoIfIndex.setStatus("mandatory")


class _TunnelInfoState_Type(Integer32):
    """Custom type tunnelInfoState based on Integer32"""
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
        *(("call", 5),
          ("closed", 3),
          ("create", 2),
          ("destroy", 6),
          ("openclosing", 4),
          ("void", 1))
    )


_TunnelInfoState_Type.__name__ = "Integer32"
_TunnelInfoState_Object = MibTableColumn
tunnelInfoState = _TunnelInfoState_Object(
    (1, 3, 6, 1, 4, 1, 208, 52, 1, 1, 1, 2),
    _TunnelInfoState_Type()
)
tunnelInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelInfoState.setStatus("mandatory")


class _TunnelInfoDirection_Type(Integer32):
    """Custom type tunnelInfoDirection based on Integer32"""
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


_TunnelInfoDirection_Type.__name__ = "Integer32"
_TunnelInfoDirection_Object = MibTableColumn
tunnelInfoDirection = _TunnelInfoDirection_Object(
    (1, 3, 6, 1, 4, 1, 208, 52, 1, 1, 1, 3),
    _TunnelInfoDirection_Type()
)
tunnelInfoDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelInfoDirection.setStatus("mandatory")
_TunnelInfoLocalAddress_Type = IpAddress
_TunnelInfoLocalAddress_Object = MibTableColumn
tunnelInfoLocalAddress = _TunnelInfoLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 208, 52, 1, 1, 1, 4),
    _TunnelInfoLocalAddress_Type()
)
tunnelInfoLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelInfoLocalAddress.setStatus("mandatory")
_TunnelInfoRemoteAddress_Type = IpAddress
_TunnelInfoRemoteAddress_Object = MibTableColumn
tunnelInfoRemoteAddress = _TunnelInfoRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 208, 52, 1, 1, 1, 5),
    _TunnelInfoRemoteAddress_Type()
)
tunnelInfoRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelInfoRemoteAddress.setStatus("mandatory")
_TunnelInfoLocalPort_Type = Integer32
_TunnelInfoLocalPort_Object = MibTableColumn
tunnelInfoLocalPort = _TunnelInfoLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 208, 52, 1, 1, 1, 6),
    _TunnelInfoLocalPort_Type()
)
tunnelInfoLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelInfoLocalPort.setStatus("mandatory")
_TunnelInfoRemotePort_Type = Integer32
_TunnelInfoRemotePort_Object = MibTableColumn
tunnelInfoRemotePort = _TunnelInfoRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 208, 52, 1, 1, 1, 7),
    _TunnelInfoRemotePort_Type()
)
tunnelInfoRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelInfoRemotePort.setStatus("mandatory")
_TunnelInfoReceiveQueueSize_Type = Integer32
_TunnelInfoReceiveQueueSize_Object = MibTableColumn
tunnelInfoReceiveQueueSize = _TunnelInfoReceiveQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 208, 52, 1, 1, 1, 8),
    _TunnelInfoReceiveQueueSize_Type()
)
tunnelInfoReceiveQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelInfoReceiveQueueSize.setStatus("mandatory")
_TunnelInfoTransmitQueueSize_Type = Integer32
_TunnelInfoTransmitQueueSize_Object = MibTableColumn
tunnelInfoTransmitQueueSize = _TunnelInfoTransmitQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 208, 52, 1, 1, 1, 9),
    _TunnelInfoTransmitQueueSize_Type()
)
tunnelInfoTransmitQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelInfoTransmitQueueSize.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCA-TUNNEL-MIB",
    **{"tunnel": tunnel,
       "tunnelInfo": tunnelInfo,
       "tunnelInfoTable": tunnelInfoTable,
       "tunnelInfoEntry": tunnelInfoEntry,
       "tunnelInfoIfIndex": tunnelInfoIfIndex,
       "tunnelInfoState": tunnelInfoState,
       "tunnelInfoDirection": tunnelInfoDirection,
       "tunnelInfoLocalAddress": tunnelInfoLocalAddress,
       "tunnelInfoRemoteAddress": tunnelInfoRemoteAddress,
       "tunnelInfoLocalPort": tunnelInfoLocalPort,
       "tunnelInfoRemotePort": tunnelInfoRemotePort,
       "tunnelInfoReceiveQueueSize": tunnelInfoReceiveQueueSize,
       "tunnelInfoTransmitQueueSize": tunnelInfoTransmitQueueSize}
)
