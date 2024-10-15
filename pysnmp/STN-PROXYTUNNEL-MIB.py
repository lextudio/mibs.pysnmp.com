# SNMP MIB module (STN-PROXYTUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STN-PROXYTUNNEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:15 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(stnNotification,) = mibBuilder.importSymbols(
    "SPRING-TIDE-NETWORKS-SMI",
    "stnNotification")

(stnPMProxyTunnel,) = mibBuilder.importSymbols(
    "STN-POLICY-MIB",
    "stnPMProxyTunnel")


# MODULE-IDENTITY

stnProxyTunnel = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_StnProxyTunnelObjects_ObjectIdentity = ObjectIdentity
stnProxyTunnelObjects = _StnProxyTunnelObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1)
)
_StnProxyTunnelTable_Object = MibTable
stnProxyTunnelTable = _StnProxyTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1)
)
if mibBuilder.loadTexts:
    stnProxyTunnelTable.setStatus("current")
_StnProxyTunnelEntry_Object = MibTableRow
stnProxyTunnelEntry = _StnProxyTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1)
)
stnProxyTunnelEntry.setIndexNames(
    (0, "STN-PROXYTUNNEL-MIB", "stnProxyTunnelSerialNumber"),
    (0, "STN-PROXYTUNNEL-MIB", "stnProxyTunnelRouterInstance"),
)
if mibBuilder.loadTexts:
    stnProxyTunnelEntry.setStatus("current")
_StnProxyTunnelSerialNumber_Type = Integer32
_StnProxyTunnelSerialNumber_Object = MibTableColumn
stnProxyTunnelSerialNumber = _StnProxyTunnelSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 1),
    _StnProxyTunnelSerialNumber_Type()
)
stnProxyTunnelSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnProxyTunnelSerialNumber.setStatus("current")
_StnProxyTunnelRouterInstance_Type = Integer32
_StnProxyTunnelRouterInstance_Object = MibTableColumn
stnProxyTunnelRouterInstance = _StnProxyTunnelRouterInstance_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 2),
    _StnProxyTunnelRouterInstance_Type()
)
stnProxyTunnelRouterInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnProxyTunnelRouterInstance.setStatus("current")
_StnProxyTunnelConnIdleTimeOut_Type = Integer32
_StnProxyTunnelConnIdleTimeOut_Object = MibTableColumn
stnProxyTunnelConnIdleTimeOut = _StnProxyTunnelConnIdleTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 3),
    _StnProxyTunnelConnIdleTimeOut_Type()
)
stnProxyTunnelConnIdleTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnProxyTunnelConnIdleTimeOut.setStatus("current")
_StnProxyTunnelPolicyInstance_Type = Integer32
_StnProxyTunnelPolicyInstance_Object = MibTableColumn
stnProxyTunnelPolicyInstance = _StnProxyTunnelPolicyInstance_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 4),
    _StnProxyTunnelPolicyInstance_Type()
)
stnProxyTunnelPolicyInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnProxyTunnelPolicyInstance.setStatus("current")
_StnProxyTunnelPolicyName_Type = DisplayString
_StnProxyTunnelPolicyName_Object = MibTableColumn
stnProxyTunnelPolicyName = _StnProxyTunnelPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 5),
    _StnProxyTunnelPolicyName_Type()
)
stnProxyTunnelPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnProxyTunnelPolicyName.setStatus("current")


class _StnProxyTunnelEncapsType_Type(Integer32):
    """Custom type stnProxyTunnelEncapsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stnProxyTunEncapsIpGre", 2),
          ("stnProxyTunEncapsIpIp", 1),
          ("stnProxyTunEncapsIpsec", 3))
    )


_StnProxyTunnelEncapsType_Type.__name__ = "Integer32"
_StnProxyTunnelEncapsType_Object = MibTableColumn
stnProxyTunnelEncapsType = _StnProxyTunnelEncapsType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 6),
    _StnProxyTunnelEncapsType_Type()
)
stnProxyTunnelEncapsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnProxyTunnelEncapsType.setStatus("current")


class _StnProxyTunnelState_Type(Integer32):
    """Custom type stnProxyTunnelState based on Integer32"""
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


_StnProxyTunnelState_Type.__name__ = "Integer32"
_StnProxyTunnelState_Object = MibTableColumn
stnProxyTunnelState = _StnProxyTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 7),
    _StnProxyTunnelState_Type()
)
stnProxyTunnelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnProxyTunnelState.setStatus("current")
_StnProxyTunnelL3IfaceTx_Type = InterfaceIndex
_StnProxyTunnelL3IfaceTx_Object = MibTableColumn
stnProxyTunnelL3IfaceTx = _StnProxyTunnelL3IfaceTx_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 8),
    _StnProxyTunnelL3IfaceTx_Type()
)
stnProxyTunnelL3IfaceTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnProxyTunnelL3IfaceTx.setStatus("current")
_StnProxyTunnelLocalTunnelAddr_Type = IpAddress
_StnProxyTunnelLocalTunnelAddr_Object = MibTableColumn
stnProxyTunnelLocalTunnelAddr = _StnProxyTunnelLocalTunnelAddr_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 9),
    _StnProxyTunnelLocalTunnelAddr_Type()
)
stnProxyTunnelLocalTunnelAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnProxyTunnelLocalTunnelAddr.setStatus("current")
_StnProxyTunnelRemoteTunnelAddr_Type = IpAddress
_StnProxyTunnelRemoteTunnelAddr_Object = MibTableColumn
stnProxyTunnelRemoteTunnelAddr = _StnProxyTunnelRemoteTunnelAddr_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 10),
    _StnProxyTunnelRemoteTunnelAddr_Type()
)
stnProxyTunnelRemoteTunnelAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnProxyTunnelRemoteTunnelAddr.setStatus("current")


class _StnProxyTunnelInESPSPIs_Type(OctetString):
    """Custom type stnProxyTunnelInESPSPIs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_StnProxyTunnelInESPSPIs_Type.__name__ = "OctetString"
_StnProxyTunnelInESPSPIs_Object = MibTableColumn
stnProxyTunnelInESPSPIs = _StnProxyTunnelInESPSPIs_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 11),
    _StnProxyTunnelInESPSPIs_Type()
)
stnProxyTunnelInESPSPIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnProxyTunnelInESPSPIs.setStatus("current")


class _StnProxyTunnelOutESPSPIs_Type(OctetString):
    """Custom type stnProxyTunnelOutESPSPIs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_StnProxyTunnelOutESPSPIs_Type.__name__ = "OctetString"
_StnProxyTunnelOutESPSPIs_Object = MibTableColumn
stnProxyTunnelOutESPSPIs = _StnProxyTunnelOutESPSPIs_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 12),
    _StnProxyTunnelOutESPSPIs_Type()
)
stnProxyTunnelOutESPSPIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnProxyTunnelOutESPSPIs.setStatus("current")


class _StnProxyTunnelInAHSPIs_Type(OctetString):
    """Custom type stnProxyTunnelInAHSPIs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_StnProxyTunnelInAHSPIs_Type.__name__ = "OctetString"
_StnProxyTunnelInAHSPIs_Object = MibTableColumn
stnProxyTunnelInAHSPIs = _StnProxyTunnelInAHSPIs_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 13),
    _StnProxyTunnelInAHSPIs_Type()
)
stnProxyTunnelInAHSPIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnProxyTunnelInAHSPIs.setStatus("current")


class _StnProxyTunnelOutAHSPIs_Type(OctetString):
    """Custom type stnProxyTunnelOutAHSPIs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_StnProxyTunnelOutAHSPIs_Type.__name__ = "OctetString"
_StnProxyTunnelOutAHSPIs_Object = MibTableColumn
stnProxyTunnelOutAHSPIs = _StnProxyTunnelOutAHSPIs_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 14),
    _StnProxyTunnelOutAHSPIs_Type()
)
stnProxyTunnelOutAHSPIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnProxyTunnelOutAHSPIs.setStatus("current")
_StnProxyTunnelEncapsIndex_Type = Integer32
_StnProxyTunnelEncapsIndex_Object = MibTableColumn
stnProxyTunnelEncapsIndex = _StnProxyTunnelEncapsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 15),
    _StnProxyTunnelEncapsIndex_Type()
)
stnProxyTunnelEncapsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnProxyTunnelEncapsIndex.setStatus("current")
_StnProxyTunnelInPkts_Type = Counter64
_StnProxyTunnelInPkts_Object = MibTableColumn
stnProxyTunnelInPkts = _StnProxyTunnelInPkts_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 16),
    _StnProxyTunnelInPkts_Type()
)
stnProxyTunnelInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnProxyTunnelInPkts.setStatus("current")
_StnProxyTunnelInErrPkts_Type = Counter64
_StnProxyTunnelInErrPkts_Object = MibTableColumn
stnProxyTunnelInErrPkts = _StnProxyTunnelInErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 17),
    _StnProxyTunnelInErrPkts_Type()
)
stnProxyTunnelInErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnProxyTunnelInErrPkts.setStatus("current")
_StnProxyTunnelOutPkts_Type = Counter64
_StnProxyTunnelOutPkts_Object = MibTableColumn
stnProxyTunnelOutPkts = _StnProxyTunnelOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 18),
    _StnProxyTunnelOutPkts_Type()
)
stnProxyTunnelOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnProxyTunnelOutPkts.setStatus("current")
_StnProxyTunnelOutErrPkts_Type = Counter64
_StnProxyTunnelOutErrPkts_Object = MibTableColumn
stnProxyTunnelOutErrPkts = _StnProxyTunnelOutErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 11, 1, 16, 1, 1, 1, 1, 19),
    _StnProxyTunnelOutErrPkts_Type()
)
stnProxyTunnelOutErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnProxyTunnelOutErrPkts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STN-PROXYTUNNEL-MIB",
    **{"stnProxyTunnel": stnProxyTunnel,
       "stnProxyTunnelObjects": stnProxyTunnelObjects,
       "stnProxyTunnelTable": stnProxyTunnelTable,
       "stnProxyTunnelEntry": stnProxyTunnelEntry,
       "stnProxyTunnelSerialNumber": stnProxyTunnelSerialNumber,
       "stnProxyTunnelRouterInstance": stnProxyTunnelRouterInstance,
       "stnProxyTunnelConnIdleTimeOut": stnProxyTunnelConnIdleTimeOut,
       "stnProxyTunnelPolicyInstance": stnProxyTunnelPolicyInstance,
       "stnProxyTunnelPolicyName": stnProxyTunnelPolicyName,
       "stnProxyTunnelEncapsType": stnProxyTunnelEncapsType,
       "stnProxyTunnelState": stnProxyTunnelState,
       "stnProxyTunnelL3IfaceTx": stnProxyTunnelL3IfaceTx,
       "stnProxyTunnelLocalTunnelAddr": stnProxyTunnelLocalTunnelAddr,
       "stnProxyTunnelRemoteTunnelAddr": stnProxyTunnelRemoteTunnelAddr,
       "stnProxyTunnelInESPSPIs": stnProxyTunnelInESPSPIs,
       "stnProxyTunnelOutESPSPIs": stnProxyTunnelOutESPSPIs,
       "stnProxyTunnelInAHSPIs": stnProxyTunnelInAHSPIs,
       "stnProxyTunnelOutAHSPIs": stnProxyTunnelOutAHSPIs,
       "stnProxyTunnelEncapsIndex": stnProxyTunnelEncapsIndex,
       "stnProxyTunnelInPkts": stnProxyTunnelInPkts,
       "stnProxyTunnelInErrPkts": stnProxyTunnelInErrPkts,
       "stnProxyTunnelOutPkts": stnProxyTunnelOutPkts,
       "stnProxyTunnelOutErrPkts": stnProxyTunnelOutErrPkts}
)
