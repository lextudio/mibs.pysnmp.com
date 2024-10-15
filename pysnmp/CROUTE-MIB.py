# SNMP MIB module (CROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CROUTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:58 2024
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

(lannet,) = mibBuilder.importSymbols(
    "GEN-MIB",
    "lannet")

(OwnerString,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
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





class NetNum(Integer32):
    """Custom type NetNum based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Croute_ObjectIdentity = ObjectIdentity
croute = _Croute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31)
)
_IpRoute_ObjectIdentity = ObjectIdentity
ipRoute = _IpRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 1)
)
_IpGlobals_ObjectIdentity = ObjectIdentity
ipGlobals = _IpGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 1)
)


class _IpGlobalsBOOTPRelayStatus_Type(Integer32):
    """Custom type ipGlobalsBOOTPRelayStatus based on Integer32"""
    defaultValue = 2

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
        *(("activeBackup", 4),
          ("backup", 3),
          ("disable", 2),
          ("enable", 1))
    )


_IpGlobalsBOOTPRelayStatus_Type.__name__ = "Integer32"
_IpGlobalsBOOTPRelayStatus_Object = MibScalar
ipGlobalsBOOTPRelayStatus = _IpGlobalsBOOTPRelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 1, 1),
    _IpGlobalsBOOTPRelayStatus_Type()
)
ipGlobalsBOOTPRelayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalsBOOTPRelayStatus.setStatus("mandatory")


class _IpGlobalsICMPErrMsgEnable_Type(Integer32):
    """Custom type ipGlobalsICMPErrMsgEnable based on Integer32"""
    defaultValue = 1

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


_IpGlobalsICMPErrMsgEnable_Type.__name__ = "Integer32"
_IpGlobalsICMPErrMsgEnable_Object = MibScalar
ipGlobalsICMPErrMsgEnable = _IpGlobalsICMPErrMsgEnable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 1, 2),
    _IpGlobalsICMPErrMsgEnable_Type()
)
ipGlobalsICMPErrMsgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalsICMPErrMsgEnable.setStatus("mandatory")


class _IpGlobalsARPInactiveTimeout_Type(Integer32):
    """Custom type ipGlobalsARPInactiveTimeout based on Integer32"""
    defaultValue = 14400


_IpGlobalsARPInactiveTimeout_Object = MibScalar
ipGlobalsARPInactiveTimeout = _IpGlobalsARPInactiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 1, 3),
    _IpGlobalsARPInactiveTimeout_Type()
)
ipGlobalsARPInactiveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalsARPInactiveTimeout.setStatus("mandatory")
_IpInterfaceTable_Object = MibTable
ipInterfaceTable = _IpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2)
)
if mibBuilder.loadTexts:
    ipInterfaceTable.setStatus("mandatory")
_IpInterfaceEntry_Object = MibTableRow
ipInterfaceEntry = _IpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1)
)
ipInterfaceEntry.setIndexNames(
    (0, "CROUTE-MIB", "ipInterfaceAddr"),
)
if mibBuilder.loadTexts:
    ipInterfaceEntry.setStatus("mandatory")
_IpInterfaceAddr_Type = IpAddress
_IpInterfaceAddr_Object = MibTableColumn
ipInterfaceAddr = _IpInterfaceAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 1),
    _IpInterfaceAddr_Type()
)
ipInterfaceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInterfaceAddr.setStatus("mandatory")
_IpInterfaceNetMask_Type = IpAddress
_IpInterfaceNetMask_Object = MibTableColumn
ipInterfaceNetMask = _IpInterfaceNetMask_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 2),
    _IpInterfaceNetMask_Type()
)
ipInterfaceNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceNetMask.setStatus("mandatory")


class _IpInterfaceLowerIfAlias_Type(DisplayString):
    """Custom type ipInterfaceLowerIfAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_IpInterfaceLowerIfAlias_Type.__name__ = "DisplayString"
_IpInterfaceLowerIfAlias_Object = MibTableColumn
ipInterfaceLowerIfAlias = _IpInterfaceLowerIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 3),
    _IpInterfaceLowerIfAlias_Type()
)
ipInterfaceLowerIfAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceLowerIfAlias.setStatus("mandatory")


class _IpInterfaceType_Type(Integer32):
    """Custom type ipInterfaceType based on Integer32"""
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
        *(("broadcast", 1),
          ("nBMA", 2),
          ("ptp", 3))
    )


_IpInterfaceType_Type.__name__ = "Integer32"
_IpInterfaceType_Object = MibTableColumn
ipInterfaceType = _IpInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 4),
    _IpInterfaceType_Type()
)
ipInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceType.setStatus("mandatory")


class _IpInterfaceForwardIpBroadcast_Type(Integer32):
    """Custom type ipInterfaceForwardIpBroadcast based on Integer32"""
    defaultValue = 1

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


_IpInterfaceForwardIpBroadcast_Type.__name__ = "Integer32"
_IpInterfaceForwardIpBroadcast_Object = MibTableColumn
ipInterfaceForwardIpBroadcast = _IpInterfaceForwardIpBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 5),
    _IpInterfaceForwardIpBroadcast_Type()
)
ipInterfaceForwardIpBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceForwardIpBroadcast.setStatus("mandatory")


class _IpInterfaceBroadcastAddr_Type(Integer32):
    """Custom type ipInterfaceBroadcastAddr based on Integer32"""
    defaultValue = 1


_IpInterfaceBroadcastAddr_Object = MibTableColumn
ipInterfaceBroadcastAddr = _IpInterfaceBroadcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 6),
    _IpInterfaceBroadcastAddr_Type()
)
ipInterfaceBroadcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceBroadcastAddr.setStatus("mandatory")


class _IpInterfaceProxyArp_Type(Integer32):
    """Custom type ipInterfaceProxyArp based on Integer32"""
    defaultValue = 2

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


_IpInterfaceProxyArp_Type.__name__ = "Integer32"
_IpInterfaceProxyArp_Object = MibTableColumn
ipInterfaceProxyArp = _IpInterfaceProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 7),
    _IpInterfaceProxyArp_Type()
)
ipInterfaceProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProxyArp.setStatus("mandatory")
_IpInterfaceStatus_Type = RowStatus
_IpInterfaceStatus_Object = MibTableColumn
ipInterfaceStatus = _IpInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 8),
    _IpInterfaceStatus_Type()
)
ipInterfaceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceStatus.setStatus("mandatory")
_IpInterfaceMainRouterAddr_Type = IpAddress
_IpInterfaceMainRouterAddr_Object = MibTableColumn
ipInterfaceMainRouterAddr = _IpInterfaceMainRouterAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 9),
    _IpInterfaceMainRouterAddr_Type()
)
ipInterfaceMainRouterAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceMainRouterAddr.setStatus("mandatory")


class _IpInterfaceARPServerStatus_Type(Integer32):
    """Custom type ipInterfaceARPServerStatus based on Integer32"""
    defaultValue = 2

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


_IpInterfaceARPServerStatus_Type.__name__ = "Integer32"
_IpInterfaceARPServerStatus_Object = MibTableColumn
ipInterfaceARPServerStatus = _IpInterfaceARPServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 10),
    _IpInterfaceARPServerStatus_Type()
)
ipInterfaceARPServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceARPServerStatus.setStatus("mandatory")


class _IpInterfaceName_Type(DisplayString):
    """Custom type ipInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpInterfaceName_Type.__name__ = "DisplayString"
_IpInterfaceName_Object = MibTableColumn
ipInterfaceName = _IpInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 11),
    _IpInterfaceName_Type()
)
ipInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceName.setStatus("mandatory")


class _IpInterfaceNetbiosRebroadcast_Type(Integer32):
    """Custom type ipInterfaceNetbiosRebroadcast based on Integer32"""
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
        *(("both", 3),
          ("disable", 4),
          ("inbound", 1),
          ("outbound", 2))
    )


_IpInterfaceNetbiosRebroadcast_Type.__name__ = "Integer32"
_IpInterfaceNetbiosRebroadcast_Object = MibTableColumn
ipInterfaceNetbiosRebroadcast = _IpInterfaceNetbiosRebroadcast_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 12),
    _IpInterfaceNetbiosRebroadcast_Type()
)
ipInterfaceNetbiosRebroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceNetbiosRebroadcast.setStatus("mandatory")


class _IpInterfaceIcmpRedirects_Type(Integer32):
    """Custom type ipInterfaceIcmpRedirects based on Integer32"""
    defaultValue = 1

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


_IpInterfaceIcmpRedirects_Type.__name__ = "Integer32"
_IpInterfaceIcmpRedirects_Object = MibTableColumn
ipInterfaceIcmpRedirects = _IpInterfaceIcmpRedirects_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 13),
    _IpInterfaceIcmpRedirects_Type()
)
ipInterfaceIcmpRedirects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceIcmpRedirects.setStatus("mandatory")
_RipGlobals_ObjectIdentity = ObjectIdentity
ripGlobals = _RipGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 3)
)


class _RipGlobalsRIPEnable_Type(Integer32):
    """Custom type ripGlobalsRIPEnable based on Integer32"""
    defaultValue = 1

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


_RipGlobalsRIPEnable_Type.__name__ = "Integer32"
_RipGlobalsRIPEnable_Object = MibScalar
ripGlobalsRIPEnable = _RipGlobalsRIPEnable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 3, 1),
    _RipGlobalsRIPEnable_Type()
)
ripGlobalsRIPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripGlobalsRIPEnable.setStatus("mandatory")


class _RipGlobalsLeakOSPFIntoRIP_Type(Integer32):
    """Custom type ripGlobalsLeakOSPFIntoRIP based on Integer32"""
    defaultValue = 2

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


_RipGlobalsLeakOSPFIntoRIP_Type.__name__ = "Integer32"
_RipGlobalsLeakOSPFIntoRIP_Object = MibScalar
ripGlobalsLeakOSPFIntoRIP = _RipGlobalsLeakOSPFIntoRIP_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 3, 2),
    _RipGlobalsLeakOSPFIntoRIP_Type()
)
ripGlobalsLeakOSPFIntoRIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripGlobalsLeakOSPFIntoRIP.setStatus("mandatory")


class _RipGlobalsLeakStaticIntoRIP_Type(Integer32):
    """Custom type ripGlobalsLeakStaticIntoRIP based on Integer32"""
    defaultValue = 1

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


_RipGlobalsLeakStaticIntoRIP_Type.__name__ = "Integer32"
_RipGlobalsLeakStaticIntoRIP_Object = MibScalar
ripGlobalsLeakStaticIntoRIP = _RipGlobalsLeakStaticIntoRIP_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 3, 3),
    _RipGlobalsLeakStaticIntoRIP_Type()
)
ripGlobalsLeakStaticIntoRIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripGlobalsLeakStaticIntoRIP.setStatus("mandatory")
_RipInterfaceTable_Object = MibTable
ripInterfaceTable = _RipInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 4)
)
if mibBuilder.loadTexts:
    ripInterfaceTable.setStatus("mandatory")
_RipInterfaceEntry_Object = MibTableRow
ripInterfaceEntry = _RipInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 4, 1)
)
ripInterfaceEntry.setIndexNames(
    (0, "CROUTE-MIB", "ripInterfaceAddr"),
)
if mibBuilder.loadTexts:
    ripInterfaceEntry.setStatus("mandatory")
_RipInterfaceAddr_Type = IpAddress
_RipInterfaceAddr_Object = MibTableColumn
ripInterfaceAddr = _RipInterfaceAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 4, 1, 1),
    _RipInterfaceAddr_Type()
)
ripInterfaceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInterfaceAddr.setStatus("mandatory")


class _RipInterfaceMetric_Type(Integer32):
    """Custom type ripInterfaceMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RipInterfaceMetric_Type.__name__ = "Integer32"
_RipInterfaceMetric_Object = MibTableColumn
ripInterfaceMetric = _RipInterfaceMetric_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 4, 1, 2),
    _RipInterfaceMetric_Type()
)
ripInterfaceMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripInterfaceMetric.setStatus("mandatory")


class _RipInterfaceSplitHorizon_Type(Integer32):
    """Custom type ripInterfaceSplitHorizon based on Integer32"""
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
        *(("none", 3),
          ("poisonReverse", 1),
          ("splitHorizon", 2))
    )


_RipInterfaceSplitHorizon_Type.__name__ = "Integer32"
_RipInterfaceSplitHorizon_Object = MibTableColumn
ripInterfaceSplitHorizon = _RipInterfaceSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 4, 1, 3),
    _RipInterfaceSplitHorizon_Type()
)
ripInterfaceSplitHorizon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripInterfaceSplitHorizon.setStatus("mandatory")


class _RipInterfaceAcceptDefaultRoute_Type(Integer32):
    """Custom type ripInterfaceAcceptDefaultRoute based on Integer32"""
    defaultValue = 1

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


_RipInterfaceAcceptDefaultRoute_Type.__name__ = "Integer32"
_RipInterfaceAcceptDefaultRoute_Object = MibTableColumn
ripInterfaceAcceptDefaultRoute = _RipInterfaceAcceptDefaultRoute_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 4, 1, 4),
    _RipInterfaceAcceptDefaultRoute_Type()
)
ripInterfaceAcceptDefaultRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripInterfaceAcceptDefaultRoute.setStatus("mandatory")


class _RipInterfaceSendDefaultRoute_Type(Integer32):
    """Custom type ripInterfaceSendDefaultRoute based on Integer32"""
    defaultValue = 2

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


_RipInterfaceSendDefaultRoute_Type.__name__ = "Integer32"
_RipInterfaceSendDefaultRoute_Object = MibTableColumn
ripInterfaceSendDefaultRoute = _RipInterfaceSendDefaultRoute_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 4, 1, 5),
    _RipInterfaceSendDefaultRoute_Type()
)
ripInterfaceSendDefaultRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripInterfaceSendDefaultRoute.setStatus("mandatory")


class _RipInterfaceState_Type(Integer32):
    """Custom type ripInterfaceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RipInterfaceState_Type.__name__ = "Integer32"
_RipInterfaceState_Object = MibTableColumn
ripInterfaceState = _RipInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 4, 1, 6),
    _RipInterfaceState_Type()
)
ripInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInterfaceState.setStatus("mandatory")


class _RipInterfaceSendMode_Type(Integer32):
    """Custom type ripInterfaceSendMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("defaultOnly", 2),
          ("doNotSend", 3))
    )


_RipInterfaceSendMode_Type.__name__ = "Integer32"
_RipInterfaceSendMode_Object = MibTableColumn
ripInterfaceSendMode = _RipInterfaceSendMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 4, 1, 7),
    _RipInterfaceSendMode_Type()
)
ripInterfaceSendMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripInterfaceSendMode.setStatus("mandatory")


class _RipInterfaceVersion_Type(Integer32):
    """Custom type ripInterfaceVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rip1", 1),
          ("rip2", 2))
    )


_RipInterfaceVersion_Type.__name__ = "Integer32"
_RipInterfaceVersion_Object = MibTableColumn
ripInterfaceVersion = _RipInterfaceVersion_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 4, 1, 8),
    _RipInterfaceVersion_Type()
)
ripInterfaceVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripInterfaceVersion.setStatus("mandatory")
_OspfGlobals_ObjectIdentity = ObjectIdentity
ospfGlobals = _OspfGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 5)
)


class _OspfGlobalsLeakRIPIntoOSPF_Type(Integer32):
    """Custom type ospfGlobalsLeakRIPIntoOSPF based on Integer32"""
    defaultValue = 2

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


_OspfGlobalsLeakRIPIntoOSPF_Type.__name__ = "Integer32"
_OspfGlobalsLeakRIPIntoOSPF_Object = MibScalar
ospfGlobalsLeakRIPIntoOSPF = _OspfGlobalsLeakRIPIntoOSPF_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 5, 1),
    _OspfGlobalsLeakRIPIntoOSPF_Type()
)
ospfGlobalsLeakRIPIntoOSPF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfGlobalsLeakRIPIntoOSPF.setStatus("mandatory")


class _OspfGlobalsLeakStaticIntoOSPF_Type(Integer32):
    """Custom type ospfGlobalsLeakStaticIntoOSPF based on Integer32"""
    defaultValue = 1

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


_OspfGlobalsLeakStaticIntoOSPF_Type.__name__ = "Integer32"
_OspfGlobalsLeakStaticIntoOSPF_Object = MibScalar
ospfGlobalsLeakStaticIntoOSPF = _OspfGlobalsLeakStaticIntoOSPF_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 5, 2),
    _OspfGlobalsLeakStaticIntoOSPF_Type()
)
ospfGlobalsLeakStaticIntoOSPF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfGlobalsLeakStaticIntoOSPF.setStatus("mandatory")


class _OspfGlobalsLeakDirectIntoOSPF_Type(Integer32):
    """Custom type ospfGlobalsLeakDirectIntoOSPF based on Integer32"""
    defaultValue = 1

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


_OspfGlobalsLeakDirectIntoOSPF_Type.__name__ = "Integer32"
_OspfGlobalsLeakDirectIntoOSPF_Object = MibScalar
ospfGlobalsLeakDirectIntoOSPF = _OspfGlobalsLeakDirectIntoOSPF_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 5, 3),
    _OspfGlobalsLeakDirectIntoOSPF_Type()
)
ospfGlobalsLeakDirectIntoOSPF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfGlobalsLeakDirectIntoOSPF.setStatus("mandatory")
_RelayTable_Object = MibTable
relayTable = _RelayTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 6)
)
if mibBuilder.loadTexts:
    relayTable.setStatus("mandatory")
_RelayEntry_Object = MibTableRow
relayEntry = _RelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 6, 1)
)
relayEntry.setIndexNames(
    (0, "CROUTE-MIB", "relayVlIndex"),
)
if mibBuilder.loadTexts:
    relayEntry.setStatus("mandatory")
_RelayVlIndex_Type = Integer32
_RelayVlIndex_Object = MibTableColumn
relayVlIndex = _RelayVlIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 6, 1, 1),
    _RelayVlIndex_Type()
)
relayVlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayVlIndex.setStatus("mandatory")
_RelayVlPrimaryServerAddr_Type = IpAddress
_RelayVlPrimaryServerAddr_Object = MibTableColumn
relayVlPrimaryServerAddr = _RelayVlPrimaryServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 6, 1, 2),
    _RelayVlPrimaryServerAddr_Type()
)
relayVlPrimaryServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayVlPrimaryServerAddr.setStatus("mandatory")
_RelayVlSeconderyServerAddr_Type = IpAddress
_RelayVlSeconderyServerAddr_Object = MibTableColumn
relayVlSeconderyServerAddr = _RelayVlSeconderyServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 6, 1, 3),
    _RelayVlSeconderyServerAddr_Type()
)
relayVlSeconderyServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayVlSeconderyServerAddr.setStatus("mandatory")
_RelayVlStatus_Type = RowStatus
_RelayVlStatus_Object = MibTableColumn
relayVlStatus = _RelayVlStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 6, 1, 4),
    _RelayVlStatus_Type()
)
relayVlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayVlStatus.setStatus("mandatory")
_RelayVlRelayAddr_Type = IpAddress
_RelayVlRelayAddr_Object = MibTableColumn
relayVlRelayAddr = _RelayVlRelayAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 6, 1, 5),
    _RelayVlRelayAddr_Type()
)
relayVlRelayAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayVlRelayAddr.setStatus("mandatory")
_IpAccessGlobals_ObjectIdentity = ObjectIdentity
ipAccessGlobals = _IpAccessGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 7)
)


class _IpAccessControlEnable_Type(Integer32):
    """Custom type ipAccessControlEnable based on Integer32"""
    defaultValue = 2

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


_IpAccessControlEnable_Type.__name__ = "Integer32"
_IpAccessControlEnable_Object = MibScalar
ipAccessControlEnable = _IpAccessControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 7, 1),
    _IpAccessControlEnable_Type()
)
ipAccessControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAccessControlEnable.setStatus("mandatory")
_IpAccessControlTable_Object = MibTable
ipAccessControlTable = _IpAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 8)
)
if mibBuilder.loadTexts:
    ipAccessControlTable.setStatus("mandatory")
_IpAccessControlEntry_Object = MibTableRow
ipAccessControlEntry = _IpAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 8, 1)
)
ipAccessControlEntry.setIndexNames(
    (0, "CROUTE-MIB", "ipAccessControlIndex"),
)
if mibBuilder.loadTexts:
    ipAccessControlEntry.setStatus("mandatory")
_IpAccessControlIndex_Type = Integer32
_IpAccessControlIndex_Object = MibTableColumn
ipAccessControlIndex = _IpAccessControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 8, 1, 1),
    _IpAccessControlIndex_Type()
)
ipAccessControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAccessControlIndex.setStatus("mandatory")
_IpAccessControlSrcAddr_Type = IpAddress
_IpAccessControlSrcAddr_Object = MibTableColumn
ipAccessControlSrcAddr = _IpAccessControlSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 8, 1, 2),
    _IpAccessControlSrcAddr_Type()
)
ipAccessControlSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAccessControlSrcAddr.setStatus("mandatory")
_IpAccessControlSrcMask_Type = IpAddress
_IpAccessControlSrcMask_Object = MibTableColumn
ipAccessControlSrcMask = _IpAccessControlSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 8, 1, 3),
    _IpAccessControlSrcMask_Type()
)
ipAccessControlSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAccessControlSrcMask.setStatus("mandatory")
_IpAccessControlDstAddr_Type = IpAddress
_IpAccessControlDstAddr_Object = MibTableColumn
ipAccessControlDstAddr = _IpAccessControlDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 8, 1, 4),
    _IpAccessControlDstAddr_Type()
)
ipAccessControlDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAccessControlDstAddr.setStatus("mandatory")
_IpAccessControlDstMask_Type = IpAddress
_IpAccessControlDstMask_Object = MibTableColumn
ipAccessControlDstMask = _IpAccessControlDstMask_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 8, 1, 5),
    _IpAccessControlDstMask_Type()
)
ipAccessControlDstMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAccessControlDstMask.setStatus("mandatory")


class _IpAccessControlOperation_Type(Integer32):
    """Custom type ipAccessControlOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("blockAndReport", 3),
          ("forward", 1))
    )


_IpAccessControlOperation_Type.__name__ = "Integer32"
_IpAccessControlOperation_Object = MibTableColumn
ipAccessControlOperation = _IpAccessControlOperation_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 8, 1, 6),
    _IpAccessControlOperation_Type()
)
ipAccessControlOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAccessControlOperation.setStatus("mandatory")


class _IpAccessControlActivation_Type(Integer32):
    """Custom type ipAccessControlActivation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("regular", 2),
          ("wire-speed", 1))
    )


_IpAccessControlActivation_Type.__name__ = "Integer32"
_IpAccessControlActivation_Object = MibTableColumn
ipAccessControlActivation = _IpAccessControlActivation_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 8, 1, 7),
    _IpAccessControlActivation_Type()
)
ipAccessControlActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAccessControlActivation.setStatus("mandatory")


class _IpAccessControlProtocol_Type(Integer32):
    """Custom type ipAccessControlProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              17,
              256)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("none", 256),
          ("tcp", 6),
          ("udp", 17))
    )


_IpAccessControlProtocol_Type.__name__ = "Integer32"
_IpAccessControlProtocol_Object = MibTableColumn
ipAccessControlProtocol = _IpAccessControlProtocol_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 8, 1, 8),
    _IpAccessControlProtocol_Type()
)
ipAccessControlProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAccessControlProtocol.setStatus("mandatory")


class _IpAccessControlApplication_Type(Integer32):
    """Custom type ipAccessControlApplication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(21,
              23,
              25,
              80,
              110,
              161,
              162,
              65536,
              65537)
        )
    )
    namedValues = NamedValues(
        *(("above1023", 65536),
          ("ftp", 21),
          ("http", 80),
          ("none", 65537),
          ("pop3", 110),
          ("smtp", 25),
          ("snmp", 161),
          ("snmpTrap", 162),
          ("telnet", 23))
    )


_IpAccessControlApplication_Type.__name__ = "Integer32"
_IpAccessControlApplication_Object = MibTableColumn
ipAccessControlApplication = _IpAccessControlApplication_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 8, 1, 9),
    _IpAccessControlApplication_Type()
)
ipAccessControlApplication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAccessControlApplication.setStatus("mandatory")
_IpAccessControlStatus_Type = RowStatus
_IpAccessControlStatus_Object = MibTableColumn
ipAccessControlStatus = _IpAccessControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 8, 1, 10),
    _IpAccessControlStatus_Type()
)
ipAccessControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAccessControlStatus.setStatus("mandatory")
_IpRedundancyGlobals_ObjectIdentity = ObjectIdentity
ipRedundancyGlobals = _IpRedundancyGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 9)
)


class _IpRedundancyStatus_Type(Integer32):
    """Custom type ipRedundancyStatus based on Integer32"""
    defaultValue = 2

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
        *(("active", 4),
          ("disable", 2),
          ("enable", 1),
          ("inactive", 3))
    )


_IpRedundancyStatus_Type.__name__ = "Integer32"
_IpRedundancyStatus_Object = MibScalar
ipRedundancyStatus = _IpRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 9, 1),
    _IpRedundancyStatus_Type()
)
ipRedundancyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRedundancyStatus.setStatus("mandatory")


class _IpRedundancyTimeout_Type(Integer32):
    """Custom type ipRedundancyTimeout based on Integer32"""
    defaultValue = 12


_IpRedundancyTimeout_Object = MibScalar
ipRedundancyTimeout = _IpRedundancyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 9, 2),
    _IpRedundancyTimeout_Type()
)
ipRedundancyTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRedundancyTimeout.setStatus("mandatory")


class _IpRedundancyPollingInterval_Type(Integer32):
    """Custom type ipRedundancyPollingInterval based on Integer32"""
    defaultValue = 3


_IpRedundancyPollingInterval_Object = MibScalar
ipRedundancyPollingInterval = _IpRedundancyPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 9, 3),
    _IpRedundancyPollingInterval_Type()
)
ipRedundancyPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRedundancyPollingInterval.setStatus("mandatory")
_IpShortcutGlobals_ObjectIdentity = ObjectIdentity
ipShortcutGlobals = _IpShortcutGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 10)
)


class _IpShortcutARPServerStatus_Type(Integer32):
    """Custom type ipShortcutARPServerStatus based on Integer32"""
    defaultValue = 2

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


_IpShortcutARPServerStatus_Type.__name__ = "Integer32"
_IpShortcutARPServerStatus_Object = MibScalar
ipShortcutARPServerStatus = _IpShortcutARPServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 10, 1),
    _IpShortcutARPServerStatus_Type()
)
ipShortcutARPServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipShortcutARPServerStatus.setStatus("mandatory")
_IpMulticastInterfaceTable_Object = MibTable
ipMulticastInterfaceTable = _IpMulticastInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 11)
)
if mibBuilder.loadTexts:
    ipMulticastInterfaceTable.setStatus("mandatory")
_IpMulticastInterfaceEntry_Object = MibTableRow
ipMulticastInterfaceEntry = _IpMulticastInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 11, 1)
)
ipMulticastInterfaceEntry.setIndexNames(
    (0, "CROUTE-MIB", "ipMulticastInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    ipMulticastInterfaceEntry.setStatus("mandatory")
_IpMulticastInterfaceIfIndex_Type = Integer32
_IpMulticastInterfaceIfIndex_Object = MibTableColumn
ipMulticastInterfaceIfIndex = _IpMulticastInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 11, 1, 1),
    _IpMulticastInterfaceIfIndex_Type()
)
ipMulticastInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMulticastInterfaceIfIndex.setStatus("mandatory")


class _IpMulticastInterfaceSendAll_Type(Integer32):
    """Custom type ipMulticastInterfaceSendAll based on Integer32"""
    defaultValue = 2

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


_IpMulticastInterfaceSendAll_Type.__name__ = "Integer32"
_IpMulticastInterfaceSendAll_Object = MibTableColumn
ipMulticastInterfaceSendAll = _IpMulticastInterfaceSendAll_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 11, 1, 2),
    _IpMulticastInterfaceSendAll_Type()
)
ipMulticastInterfaceSendAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMulticastInterfaceSendAll.setStatus("mandatory")


class _IpMulticastInterfaceState_Type(Integer32):
    """Custom type ipMulticastInterfaceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_IpMulticastInterfaceState_Type.__name__ = "Integer32"
_IpMulticastInterfaceState_Object = MibTableColumn
ipMulticastInterfaceState = _IpMulticastInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 11, 1, 3),
    _IpMulticastInterfaceState_Type()
)
ipMulticastInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMulticastInterfaceState.setStatus("mandatory")


class _IpMulticastInterfaceStatus_Type(RowStatus):
    """Custom type ipMulticastInterfaceStatus based on RowStatus"""


_IpMulticastInterfaceStatus_Object = MibTableColumn
ipMulticastInterfaceStatus = _IpMulticastInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 11, 1, 4),
    _IpMulticastInterfaceStatus_Type()
)
ipMulticastInterfaceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMulticastInterfaceStatus.setStatus("mandatory")
_IpEZ2RouteMgmt_ObjectIdentity = ObjectIdentity
ipEZ2RouteMgmt = _IpEZ2RouteMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 13)
)
_IpEZ2BoostRouterTable_Object = MibTable
ipEZ2BoostRouterTable = _IpEZ2BoostRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 13, 1)
)
if mibBuilder.loadTexts:
    ipEZ2BoostRouterTable.setStatus("mandatory")
_IpEZ2BoostRouterEntry_Object = MibTableRow
ipEZ2BoostRouterEntry = _IpEZ2BoostRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 13, 1, 1)
)
ipEZ2BoostRouterEntry.setIndexNames(
    (0, "CROUTE-MIB", "ipEZ2BoostRouterSlot"),
    (0, "CROUTE-MIB", "ipEZ2BoostRouterBRAddress"),
)
if mibBuilder.loadTexts:
    ipEZ2BoostRouterEntry.setStatus("mandatory")
_IpEZ2BoostRouterSlot_Type = Integer32
_IpEZ2BoostRouterSlot_Object = MibTableColumn
ipEZ2BoostRouterSlot = _IpEZ2BoostRouterSlot_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 13, 1, 1, 1),
    _IpEZ2BoostRouterSlot_Type()
)
ipEZ2BoostRouterSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipEZ2BoostRouterSlot.setStatus("mandatory")
_IpEZ2BoostRouterBRAddress_Type = IpAddress
_IpEZ2BoostRouterBRAddress_Object = MibTableColumn
ipEZ2BoostRouterBRAddress = _IpEZ2BoostRouterBRAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 13, 1, 1, 2),
    _IpEZ2BoostRouterBRAddress_Type()
)
ipEZ2BoostRouterBRAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipEZ2BoostRouterBRAddress.setStatus("mandatory")


class _IpEZ2BoostRouterType_Type(Integer32):
    """Custom type ipEZ2BoostRouterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_IpEZ2BoostRouterType_Type.__name__ = "Integer32"
_IpEZ2BoostRouterType_Object = MibTableColumn
ipEZ2BoostRouterType = _IpEZ2BoostRouterType_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 13, 1, 1, 3),
    _IpEZ2BoostRouterType_Type()
)
ipEZ2BoostRouterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipEZ2BoostRouterType.setStatus("mandatory")
_IpEZ2BoostRouterStatus_Type = RowStatus
_IpEZ2BoostRouterStatus_Object = MibTableColumn
ipEZ2BoostRouterStatus = _IpEZ2BoostRouterStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 13, 1, 1, 4),
    _IpEZ2BoostRouterStatus_Type()
)
ipEZ2BoostRouterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipEZ2BoostRouterStatus.setStatus("mandatory")
_IpEZ2RControlTable_Object = MibTable
ipEZ2RControlTable = _IpEZ2RControlTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 13, 2)
)
if mibBuilder.loadTexts:
    ipEZ2RControlTable.setStatus("mandatory")
_IpEZ2RControlEntry_Object = MibTableRow
ipEZ2RControlEntry = _IpEZ2RControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 13, 2, 1)
)
ipEZ2RControlEntry.setIndexNames(
    (0, "CROUTE-MIB", "ipEZ2RControlSlot"),
)
if mibBuilder.loadTexts:
    ipEZ2RControlEntry.setStatus("mandatory")
_IpEZ2RControlSlot_Type = Integer32
_IpEZ2RControlSlot_Object = MibTableColumn
ipEZ2RControlSlot = _IpEZ2RControlSlot_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 13, 2, 1, 1),
    _IpEZ2RControlSlot_Type()
)
ipEZ2RControlSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipEZ2RControlSlot.setStatus("mandatory")


class _IpEZ2RControlBoostedRoutersTimeout_Type(Integer32):
    """Custom type ipEZ2RControlBoostedRoutersTimeout based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 9999999),
    )


_IpEZ2RControlBoostedRoutersTimeout_Type.__name__ = "Integer32"
_IpEZ2RControlBoostedRoutersTimeout_Object = MibTableColumn
ipEZ2RControlBoostedRoutersTimeout = _IpEZ2RControlBoostedRoutersTimeout_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 13, 2, 1, 2),
    _IpEZ2RControlBoostedRoutersTimeout_Type()
)
ipEZ2RControlBoostedRoutersTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipEZ2RControlBoostedRoutersTimeout.setStatus("mandatory")


class _IpEZ2RControlHostsTimeout_Type(Integer32):
    """Custom type ipEZ2RControlHostsTimeout based on Integer32"""
    defaultValue = 14400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 9999999),
    )


_IpEZ2RControlHostsTimeout_Type.__name__ = "Integer32"
_IpEZ2RControlHostsTimeout_Object = MibTableColumn
ipEZ2RControlHostsTimeout = _IpEZ2RControlHostsTimeout_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 13, 2, 1, 3),
    _IpEZ2RControlHostsTimeout_Type()
)
ipEZ2RControlHostsTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipEZ2RControlHostsTimeout.setStatus("mandatory")


class _IpEZ2RControlAutoLearnMode_Type(Integer32):
    """Custom type ipEZ2RControlAutoLearnMode based on Integer32"""
    defaultValue = 1

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


_IpEZ2RControlAutoLearnMode_Type.__name__ = "Integer32"
_IpEZ2RControlAutoLearnMode_Object = MibTableColumn
ipEZ2RControlAutoLearnMode = _IpEZ2RControlAutoLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 13, 2, 1, 5),
    _IpEZ2RControlAutoLearnMode_Type()
)
ipEZ2RControlAutoLearnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipEZ2RControlAutoLearnMode.setStatus("mandatory")
_IpVRRP_ObjectIdentity = ObjectIdentity
ipVRRP = _IpVRRP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 14)
)


class _IpVRRPAdminStatus_Type(Integer32):
    """Custom type ipVRRPAdminStatus based on Integer32"""
    defaultValue = 2

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


_IpVRRPAdminStatus_Type.__name__ = "Integer32"
_IpVRRPAdminStatus_Object = MibScalar
ipVRRPAdminStatus = _IpVRRPAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 14, 1),
    _IpVRRPAdminStatus_Type()
)
ipVRRPAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipVRRPAdminStatus.setStatus("mandatory")
_IpxRoute_ObjectIdentity = ObjectIdentity
ipxRoute = _IpxRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 2)
)
_IpxCircTable_Object = MibTable
ipxCircTable = _IpxCircTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1)
)
if mibBuilder.loadTexts:
    ipxCircTable.setStatus("mandatory")
_IpxCircEntry_Object = MibTableRow
ipxCircEntry = _IpxCircEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1)
)
ipxCircEntry.setIndexNames(
    (0, "CROUTE-MIB", "ipxCircIndex"),
)
if mibBuilder.loadTexts:
    ipxCircEntry.setStatus("mandatory")
_IpxCircIndex_Type = Integer32
_IpxCircIndex_Object = MibTableColumn
ipxCircIndex = _IpxCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1, 1),
    _IpxCircIndex_Type()
)
ipxCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircIndex.setStatus("mandatory")
_IpxCircNetNumber_Type = NetNum
_IpxCircNetNumber_Object = MibTableColumn
ipxCircNetNumber = _IpxCircNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1, 2),
    _IpxCircNetNumber_Type()
)
ipxCircNetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircNetNumber.setStatus("mandatory")


class _IpxCircLowerIfAlias_Type(DisplayString):
    """Custom type ipxCircLowerIfAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_IpxCircLowerIfAlias_Type.__name__ = "DisplayString"
_IpxCircLowerIfAlias_Object = MibTableColumn
ipxCircLowerIfAlias = _IpxCircLowerIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1, 3),
    _IpxCircLowerIfAlias_Type()
)
ipxCircLowerIfAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircLowerIfAlias.setStatus("mandatory")


class _IpxCircEncapsulation_Type(Integer32):
    """Custom type ipxCircEncapsulation based on Integer32"""
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
        *(("ethernet", 3),
          ("llc", 4),
          ("novell", 2),
          ("other", 1),
          ("snap", 5))
    )


_IpxCircEncapsulation_Type.__name__ = "Integer32"
_IpxCircEncapsulation_Object = MibTableColumn
ipxCircEncapsulation = _IpxCircEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1, 4),
    _IpxCircEncapsulation_Type()
)
ipxCircEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircEncapsulation.setStatus("mandatory")


class _IpxCircNetbios_Type(Integer32):
    """Custom type ipxCircNetbios based on Integer32"""
    defaultValue = 1

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


_IpxCircNetbios_Type.__name__ = "Integer32"
_IpxCircNetbios_Object = MibTableColumn
ipxCircNetbios = _IpxCircNetbios_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1, 5),
    _IpxCircNetbios_Type()
)
ipxCircNetbios.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircNetbios.setStatus("mandatory")
_IpxCircStatus_Type = RowStatus
_IpxCircStatus_Object = MibTableColumn
ipxCircStatus = _IpxCircStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1, 6),
    _IpxCircStatus_Type()
)
ipxCircStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircStatus.setStatus("mandatory")


class _IpxCircRipUpdate_Type(Integer32):
    """Custom type ipxCircRipUpdate based on Integer32"""
    defaultValue = 60


_IpxCircRipUpdate_Object = MibTableColumn
ipxCircRipUpdate = _IpxCircRipUpdate_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1, 7),
    _IpxCircRipUpdate_Type()
)
ipxCircRipUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircRipUpdate.setStatus("mandatory")


class _IpxCircRipAgeMultiplier_Type(Integer32):
    """Custom type ipxCircRipAgeMultiplier based on Integer32"""
    defaultValue = 4


_IpxCircRipAgeMultiplier_Object = MibTableColumn
ipxCircRipAgeMultiplier = _IpxCircRipAgeMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1, 8),
    _IpxCircRipAgeMultiplier_Type()
)
ipxCircRipAgeMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircRipAgeMultiplier.setStatus("mandatory")


class _IpxCircRipStatus_Type(Integer32):
    """Custom type ipxCircRipStatus based on Integer32"""
    defaultValue = 1

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


_IpxCircRipStatus_Type.__name__ = "Integer32"
_IpxCircRipStatus_Object = MibTableColumn
ipxCircRipStatus = _IpxCircRipStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1, 9),
    _IpxCircRipStatus_Type()
)
ipxCircRipStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircRipStatus.setStatus("mandatory")


class _IpxCircSapUpdate_Type(Integer32):
    """Custom type ipxCircSapUpdate based on Integer32"""
    defaultValue = 60


_IpxCircSapUpdate_Object = MibTableColumn
ipxCircSapUpdate = _IpxCircSapUpdate_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1, 10),
    _IpxCircSapUpdate_Type()
)
ipxCircSapUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircSapUpdate.setStatus("mandatory")


class _IpxCircSapAgeMultiplier_Type(Integer32):
    """Custom type ipxCircSapAgeMultiplier based on Integer32"""
    defaultValue = 4


_IpxCircSapAgeMultiplier_Object = MibTableColumn
ipxCircSapAgeMultiplier = _IpxCircSapAgeMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1, 11),
    _IpxCircSapAgeMultiplier_Type()
)
ipxCircSapAgeMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircSapAgeMultiplier.setStatus("mandatory")


class _IpxCircGetNearestServerReply_Type(Integer32):
    """Custom type ipxCircGetNearestServerReply based on Integer32"""
    defaultValue = 1

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


_IpxCircGetNearestServerReply_Type.__name__ = "Integer32"
_IpxCircGetNearestServerReply_Object = MibTableColumn
ipxCircGetNearestServerReply = _IpxCircGetNearestServerReply_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1, 12),
    _IpxCircGetNearestServerReply_Type()
)
ipxCircGetNearestServerReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircGetNearestServerReply.setStatus("mandatory")


class _IpxCircSapStatus_Type(Integer32):
    """Custom type ipxCircSapStatus based on Integer32"""
    defaultValue = 1

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


_IpxCircSapStatus_Type.__name__ = "Integer32"
_IpxCircSapStatus_Object = MibTableColumn
ipxCircSapStatus = _IpxCircSapStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1, 13),
    _IpxCircSapStatus_Type()
)
ipxCircSapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircSapStatus.setStatus("mandatory")


class _IpxCircRipState_Type(Integer32):
    """Custom type ipxCircRipState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_IpxCircRipState_Type.__name__ = "Integer32"
_IpxCircRipState_Object = MibTableColumn
ipxCircRipState = _IpxCircRipState_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1, 14),
    _IpxCircRipState_Type()
)
ipxCircRipState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircRipState.setStatus("mandatory")


class _IpxCircSapState_Type(Integer32):
    """Custom type ipxCircSapState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_IpxCircSapState_Type.__name__ = "Integer32"
_IpxCircSapState_Object = MibTableColumn
ipxCircSapState = _IpxCircSapState_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1, 15),
    _IpxCircSapState_Type()
)
ipxCircSapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircSapState.setStatus("mandatory")
_IpxDestTable_Object = MibTable
ipxDestTable = _IpxDestTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 2)
)
if mibBuilder.loadTexts:
    ipxDestTable.setStatus("mandatory")
_IpxDestEntry_Object = MibTableRow
ipxDestEntry = _IpxDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 2, 1)
)
ipxDestEntry.setIndexNames(
    (0, "CROUTE-MIB", "ipxDestNetNum"),
)
if mibBuilder.loadTexts:
    ipxDestEntry.setStatus("mandatory")
_IpxDestNetNum_Type = NetNum
_IpxDestNetNum_Object = MibTableColumn
ipxDestNetNum = _IpxDestNetNum_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 2, 1, 1),
    _IpxDestNetNum_Type()
)
ipxDestNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestNetNum.setStatus("mandatory")


class _IpxDestProtocol_Type(Integer32):
    """Custom type ipxDestProtocol based on Integer32"""
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
        *(("local", 2),
          ("nlsp", 4),
          ("other", 1),
          ("rip", 3),
          ("static", 5))
    )


_IpxDestProtocol_Type.__name__ = "Integer32"
_IpxDestProtocol_Object = MibTableColumn
ipxDestProtocol = _IpxDestProtocol_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 2, 1, 2),
    _IpxDestProtocol_Type()
)
ipxDestProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestProtocol.setStatus("mandatory")
_IpxDestTicks_Type = Integer32
_IpxDestTicks_Object = MibTableColumn
ipxDestTicks = _IpxDestTicks_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 2, 1, 3),
    _IpxDestTicks_Type()
)
ipxDestTicks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestTicks.setStatus("mandatory")
_IpxDestHopCount_Type = Integer32
_IpxDestHopCount_Object = MibTableColumn
ipxDestHopCount = _IpxDestHopCount_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 2, 1, 4),
    _IpxDestHopCount_Type()
)
ipxDestHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestHopCount.setStatus("mandatory")
_IpxDestNextHopCircIndex_Type = Integer32
_IpxDestNextHopCircIndex_Object = MibTableColumn
ipxDestNextHopCircIndex = _IpxDestNextHopCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 2, 1, 5),
    _IpxDestNextHopCircIndex_Type()
)
ipxDestNextHopCircIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestNextHopCircIndex.setStatus("mandatory")
_IpxDestNextHopNICAddress_Type = PhysAddress
_IpxDestNextHopNICAddress_Object = MibTableColumn
ipxDestNextHopNICAddress = _IpxDestNextHopNICAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 2, 1, 6),
    _IpxDestNextHopNICAddress_Type()
)
ipxDestNextHopNICAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestNextHopNICAddress.setStatus("mandatory")
_IpxDestNextHopNetNum_Type = NetNum
_IpxDestNextHopNetNum_Object = MibTableColumn
ipxDestNextHopNetNum = _IpxDestNextHopNetNum_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 2, 1, 7),
    _IpxDestNextHopNetNum_Type()
)
ipxDestNextHopNetNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestNextHopNetNum.setStatus("mandatory")
_IpxDestStatus_Type = RowStatus
_IpxDestStatus_Object = MibTableColumn
ipxDestStatus = _IpxDestStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 2, 1, 8),
    _IpxDestStatus_Type()
)
ipxDestStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestStatus.setStatus("mandatory")
_IpxDestAge_Type = Integer32
_IpxDestAge_Object = MibTableColumn
ipxDestAge = _IpxDestAge_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 2, 1, 9),
    _IpxDestAge_Type()
)
ipxDestAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestAge.setStatus("mandatory")
_IpxServTable_Object = MibTable
ipxServTable = _IpxServTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 3)
)
if mibBuilder.loadTexts:
    ipxServTable.setStatus("mandatory")
_IpxServEntry_Object = MibTableRow
ipxServEntry = _IpxServEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 3, 1)
)
ipxServEntry.setIndexNames(
    (0, "CROUTE-MIB", "ipxServType"),
    (0, "CROUTE-MIB", "ipxServName"),
)
if mibBuilder.loadTexts:
    ipxServEntry.setStatus("mandatory")
_IpxServType_Type = Integer32
_IpxServType_Object = MibTableColumn
ipxServType = _IpxServType_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 3, 1, 1),
    _IpxServType_Type()
)
ipxServType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServType.setStatus("mandatory")


class _IpxServName_Type(DisplayString):
    """Custom type ipxServName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_IpxServName_Type.__name__ = "DisplayString"
_IpxServName_Object = MibTableColumn
ipxServName = _IpxServName_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 3, 1, 2),
    _IpxServName_Type()
)
ipxServName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServName.setStatus("mandatory")


class _IpxServProtocol_Type(Integer32):
    """Custom type ipxServProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("nlsp", 4),
          ("other", 1),
          ("sap", 6),
          ("static", 5))
    )


_IpxServProtocol_Type.__name__ = "Integer32"
_IpxServProtocol_Object = MibTableColumn
ipxServProtocol = _IpxServProtocol_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 3, 1, 3),
    _IpxServProtocol_Type()
)
ipxServProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServProtocol.setStatus("mandatory")
_IpxServNetNum_Type = NetNum
_IpxServNetNum_Object = MibTableColumn
ipxServNetNum = _IpxServNetNum_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 3, 1, 4),
    _IpxServNetNum_Type()
)
ipxServNetNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServNetNum.setStatus("mandatory")


class _IpxServNode_Type(OctetString):
    """Custom type ipxServNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxServNode_Type.__name__ = "OctetString"
_IpxServNode_Object = MibTableColumn
ipxServNode = _IpxServNode_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 3, 1, 5),
    _IpxServNode_Type()
)
ipxServNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServNode.setStatus("mandatory")
_IpxServSocket_Type = Integer32
_IpxServSocket_Object = MibTableColumn
ipxServSocket = _IpxServSocket_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 3, 1, 6),
    _IpxServSocket_Type()
)
ipxServSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServSocket.setStatus("mandatory")
_IpxServHopCount_Type = Integer32
_IpxServHopCount_Object = MibTableColumn
ipxServHopCount = _IpxServHopCount_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 3, 1, 7),
    _IpxServHopCount_Type()
)
ipxServHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServHopCount.setStatus("mandatory")
_IpxServStatus_Type = RowStatus
_IpxServStatus_Object = MibTableColumn
ipxServStatus = _IpxServStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 3, 1, 8),
    _IpxServStatus_Type()
)
ipxServStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServStatus.setStatus("mandatory")
_IpxServAge_Type = Integer32
_IpxServAge_Object = MibTableColumn
ipxServAge = _IpxServAge_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 3, 1, 9),
    _IpxServAge_Type()
)
ipxServAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServAge.setStatus("mandatory")
_IpxAccessGlobals_ObjectIdentity = ObjectIdentity
ipxAccessGlobals = _IpxAccessGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 4)
)


class _IpxAccessControlEnable_Type(Integer32):
    """Custom type ipxAccessControlEnable based on Integer32"""
    defaultValue = 2

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


_IpxAccessControlEnable_Type.__name__ = "Integer32"
_IpxAccessControlEnable_Object = MibScalar
ipxAccessControlEnable = _IpxAccessControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 4, 1),
    _IpxAccessControlEnable_Type()
)
ipxAccessControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAccessControlEnable.setStatus("mandatory")
_IpxAccessControlTable_Object = MibTable
ipxAccessControlTable = _IpxAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 5)
)
if mibBuilder.loadTexts:
    ipxAccessControlTable.setStatus("mandatory")
_IpxAccessControlEntry_Object = MibTableRow
ipxAccessControlEntry = _IpxAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 5, 1)
)
ipxAccessControlEntry.setIndexNames(
    (0, "CROUTE-MIB", "ipxAccessControlIndex"),
)
if mibBuilder.loadTexts:
    ipxAccessControlEntry.setStatus("mandatory")
_IpxAccessControlIndex_Type = Integer32
_IpxAccessControlIndex_Object = MibTableColumn
ipxAccessControlIndex = _IpxAccessControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 5, 1, 1),
    _IpxAccessControlIndex_Type()
)
ipxAccessControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAccessControlIndex.setStatus("mandatory")
_IpxAccessControlSrcAddr_Type = NetNum
_IpxAccessControlSrcAddr_Object = MibTableColumn
ipxAccessControlSrcAddr = _IpxAccessControlSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 5, 1, 2),
    _IpxAccessControlSrcAddr_Type()
)
ipxAccessControlSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAccessControlSrcAddr.setStatus("mandatory")
_IpxAccessControlDstAddr_Type = NetNum
_IpxAccessControlDstAddr_Object = MibTableColumn
ipxAccessControlDstAddr = _IpxAccessControlDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 5, 1, 3),
    _IpxAccessControlDstAddr_Type()
)
ipxAccessControlDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAccessControlDstAddr.setStatus("mandatory")


class _IpxAccessControlOperation_Type(Integer32):
    """Custom type ipxAccessControlOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("blockAndReport", 3),
          ("forward", 1))
    )


_IpxAccessControlOperation_Type.__name__ = "Integer32"
_IpxAccessControlOperation_Object = MibTableColumn
ipxAccessControlOperation = _IpxAccessControlOperation_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 5, 1, 4),
    _IpxAccessControlOperation_Type()
)
ipxAccessControlOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAccessControlOperation.setStatus("mandatory")


class _IpxAccessControlActivation_Type(Integer32):
    """Custom type ipxAccessControlActivation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("regular", 2),
          ("wire-speed", 1))
    )


_IpxAccessControlActivation_Type.__name__ = "Integer32"
_IpxAccessControlActivation_Object = MibTableColumn
ipxAccessControlActivation = _IpxAccessControlActivation_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 5, 1, 5),
    _IpxAccessControlActivation_Type()
)
ipxAccessControlActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAccessControlActivation.setStatus("mandatory")
_IpxAccessControlStatus_Type = RowStatus
_IpxAccessControlStatus_Object = MibTableColumn
ipxAccessControlStatus = _IpxAccessControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 5, 1, 6),
    _IpxAccessControlStatus_Type()
)
ipxAccessControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAccessControlStatus.setStatus("mandatory")
_IpxSapFilterGlobals_ObjectIdentity = ObjectIdentity
ipxSapFilterGlobals = _IpxSapFilterGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 6)
)


class _IpxSapFilterEnable_Type(Integer32):
    """Custom type ipxSapFilterEnable based on Integer32"""
    defaultValue = 2

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


_IpxSapFilterEnable_Type.__name__ = "Integer32"
_IpxSapFilterEnable_Object = MibScalar
ipxSapFilterEnable = _IpxSapFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 6, 1),
    _IpxSapFilterEnable_Type()
)
ipxSapFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSapFilterEnable.setStatus("mandatory")
_IpxSapFilterTable_Object = MibTable
ipxSapFilterTable = _IpxSapFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 7)
)
if mibBuilder.loadTexts:
    ipxSapFilterTable.setStatus("mandatory")
_IpxSapFilterEntry_Object = MibTableRow
ipxSapFilterEntry = _IpxSapFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 7, 1)
)
ipxSapFilterEntry.setIndexNames(
    (0, "CROUTE-MIB", "ipxSapFilterID"),
)
if mibBuilder.loadTexts:
    ipxSapFilterEntry.setStatus("mandatory")
_IpxSapFilterID_Type = Integer32
_IpxSapFilterID_Object = MibTableColumn
ipxSapFilterID = _IpxSapFilterID_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 7, 1, 1),
    _IpxSapFilterID_Type()
)
ipxSapFilterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapFilterID.setStatus("mandatory")
_IpxSapFilterCircIndex_Type = Integer32
_IpxSapFilterCircIndex_Object = MibTableColumn
ipxSapFilterCircIndex = _IpxSapFilterCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 7, 1, 2),
    _IpxSapFilterCircIndex_Type()
)
ipxSapFilterCircIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSapFilterCircIndex.setStatus("mandatory")
_IpxSapFilterServiceNetNumber_Type = NetNum
_IpxSapFilterServiceNetNumber_Object = MibTableColumn
ipxSapFilterServiceNetNumber = _IpxSapFilterServiceNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 7, 1, 3),
    _IpxSapFilterServiceNetNumber_Type()
)
ipxSapFilterServiceNetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSapFilterServiceNetNumber.setStatus("mandatory")
_IpxSapFilterServiceType_Type = Integer32
_IpxSapFilterServiceType_Object = MibTableColumn
ipxSapFilterServiceType = _IpxSapFilterServiceType_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 7, 1, 4),
    _IpxSapFilterServiceType_Type()
)
ipxSapFilterServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSapFilterServiceType.setStatus("mandatory")


class _IpxSapFilterServerName_Type(DisplayString):
    """Custom type ipxSapFilterServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_IpxSapFilterServerName_Type.__name__ = "DisplayString"
_IpxSapFilterServerName_Object = MibTableColumn
ipxSapFilterServerName = _IpxSapFilterServerName_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 7, 1, 5),
    _IpxSapFilterServerName_Type()
)
ipxSapFilterServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSapFilterServerName.setStatus("mandatory")


class _IpxSapFilterDirection_Type(Integer32):
    """Custom type ipxSapFilterDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_IpxSapFilterDirection_Type.__name__ = "Integer32"
_IpxSapFilterDirection_Object = MibTableColumn
ipxSapFilterDirection = _IpxSapFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 7, 1, 6),
    _IpxSapFilterDirection_Type()
)
ipxSapFilterDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSapFilterDirection.setStatus("mandatory")


class _IpxSapFilterAction_Type(Integer32):
    """Custom type ipxSapFilterAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_IpxSapFilterAction_Type.__name__ = "Integer32"
_IpxSapFilterAction_Object = MibTableColumn
ipxSapFilterAction = _IpxSapFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 7, 1, 7),
    _IpxSapFilterAction_Type()
)
ipxSapFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSapFilterAction.setStatus("mandatory")
_IpxSapFilterStatus_Type = RowStatus
_IpxSapFilterStatus_Object = MibTableColumn
ipxSapFilterStatus = _IpxSapFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 7, 1, 8),
    _IpxSapFilterStatus_Type()
)
ipxSapFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSapFilterStatus.setStatus("mandatory")
_Layer2_ObjectIdentity = ObjectIdentity
layer2 = _Layer2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 3)
)
_VlConfTable_Object = MibTable
vlConfTable = _VlConfTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 3, 1)
)
if mibBuilder.loadTexts:
    vlConfTable.setStatus("mandatory")
_VlConfEntry_Object = MibTableRow
vlConfEntry = _VlConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 3, 1, 1)
)
vlConfEntry.setIndexNames(
    (0, "CROUTE-MIB", "vlConfIndex"),
)
if mibBuilder.loadTexts:
    vlConfEntry.setStatus("mandatory")
_VlConfIndex_Type = Integer32
_VlConfIndex_Object = MibTableColumn
vlConfIndex = _VlConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 3, 1, 1, 1),
    _VlConfIndex_Type()
)
vlConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlConfIndex.setStatus("mandatory")


class _VlConfAlias_Type(DisplayString):
    """Custom type vlConfAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VlConfAlias_Type.__name__ = "DisplayString"
_VlConfAlias_Object = MibTableColumn
vlConfAlias = _VlConfAlias_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 3, 1, 1, 2),
    _VlConfAlias_Type()
)
vlConfAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlConfAlias.setStatus("mandatory")
_VlConfStatus_Type = RowStatus
_VlConfStatus_Object = MibTableColumn
vlConfStatus = _VlConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 3, 1, 1, 3),
    _VlConfStatus_Type()
)
vlConfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlConfStatus.setStatus("mandatory")
_VlBridgeTable_Object = MibTable
vlBridgeTable = _VlBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 3, 2)
)
if mibBuilder.loadTexts:
    vlBridgeTable.setStatus("mandatory")
_VlBridgeEntry_Object = MibTableRow
vlBridgeEntry = _VlBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 3, 2, 1)
)
vlBridgeEntry.setIndexNames(
    (0, "CROUTE-MIB", "vlBridgeProtocol"),
    (0, "CROUTE-MIB", "vlBridgeGroupIndex"),
    (0, "CROUTE-MIB", "vlBridgeIndex"),
)
if mibBuilder.loadTexts:
    vlBridgeEntry.setStatus("mandatory")


class _VlBridgeProtocol_Type(Integer32):
    """Custom type vlBridgeProtocol based on Integer32"""
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
        *(("appleTalk", 4),
          ("dec", 2),
          ("ipx", 6),
          ("netBios", 3),
          ("other", 1),
          ("sna", 5))
    )


_VlBridgeProtocol_Type.__name__ = "Integer32"
_VlBridgeProtocol_Object = MibTableColumn
vlBridgeProtocol = _VlBridgeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 3, 2, 1, 1),
    _VlBridgeProtocol_Type()
)
vlBridgeProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlBridgeProtocol.setStatus("mandatory")
_VlBridgeGroupIndex_Type = Integer32
_VlBridgeGroupIndex_Object = MibTableColumn
vlBridgeGroupIndex = _VlBridgeGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 3, 2, 1, 2),
    _VlBridgeGroupIndex_Type()
)
vlBridgeGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlBridgeGroupIndex.setStatus("mandatory")
_VlBridgeIndex_Type = Integer32
_VlBridgeIndex_Object = MibTableColumn
vlBridgeIndex = _VlBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 3, 2, 1, 3),
    _VlBridgeIndex_Type()
)
vlBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlBridgeIndex.setStatus("mandatory")
_VlBridgeStatus_Type = RowStatus
_VlBridgeStatus_Object = MibTableColumn
vlBridgeStatus = _VlBridgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 3, 2, 1, 4),
    _VlBridgeStatus_Type()
)
vlBridgeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlBridgeStatus.setStatus("mandatory")
_Layer2Globals_ObjectIdentity = ObjectIdentity
layer2Globals = _Layer2Globals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 3, 3)
)


class _Layer2GlobalsBridgeEnable_Type(Integer32):
    """Custom type layer2GlobalsBridgeEnable based on Integer32"""
    defaultValue = 2

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
        *(("activeBackup", 4),
          ("backup", 3),
          ("disable", 2),
          ("enable", 1))
    )


_Layer2GlobalsBridgeEnable_Type.__name__ = "Integer32"
_Layer2GlobalsBridgeEnable_Object = MibScalar
layer2GlobalsBridgeEnable = _Layer2GlobalsBridgeEnable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 3, 3, 1),
    _Layer2GlobalsBridgeEnable_Type()
)
layer2GlobalsBridgeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer2GlobalsBridgeEnable.setStatus("mandatory")
_RouteGroupMgmt_ObjectIdentity = ObjectIdentity
routeGroupMgmt = _RouteGroupMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 4)
)
_RouteGroupTable_Object = MibTable
routeGroupTable = _RouteGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 4, 1)
)
if mibBuilder.loadTexts:
    routeGroupTable.setStatus("mandatory")
_RouteGroupEntry_Object = MibTableRow
routeGroupEntry = _RouteGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 4, 1, 1)
)
routeGroupEntry.setIndexNames(
    (0, "CROUTE-MIB", "routeGroupId"),
)
if mibBuilder.loadTexts:
    routeGroupEntry.setStatus("mandatory")
_RouteGroupId_Type = Integer32
_RouteGroupId_Object = MibTableColumn
routeGroupId = _RouteGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 4, 1, 1, 1),
    _RouteGroupId_Type()
)
routeGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeGroupId.setStatus("mandatory")


class _RouteGroupRouteMode_Type(Integer32):
    """Custom type routeGroupRouteMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              21,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ez2route", 3),
          ("notSupported", 255),
          ("router", 5),
          ("routerAndWebSwitch", 21),
          ("secondLayer", 1))
    )


_RouteGroupRouteMode_Type.__name__ = "Integer32"
_RouteGroupRouteMode_Object = MibTableColumn
routeGroupRouteMode = _RouteGroupRouteMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 4, 1, 1, 2),
    _RouteGroupRouteMode_Type()
)
routeGroupRouteMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeGroupRouteMode.setStatus("mandatory")
_DrLayer2_ObjectIdentity = ObjectIdentity
drLayer2 = _DrLayer2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 5)
)
_DrVlConfTable_Object = MibTable
drVlConfTable = _DrVlConfTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 5, 1)
)
if mibBuilder.loadTexts:
    drVlConfTable.setStatus("mandatory")
_DrVlConfEntry_Object = MibTableRow
drVlConfEntry = _DrVlConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 5, 1, 1)
)
drVlConfEntry.setIndexNames(
    (0, "CROUTE-MIB", "drVlConfSlot"),
    (0, "CROUTE-MIB", "drVlConfIndex"),
)
if mibBuilder.loadTexts:
    drVlConfEntry.setStatus("mandatory")
_DrVlConfSlot_Type = Integer32
_DrVlConfSlot_Object = MibTableColumn
drVlConfSlot = _DrVlConfSlot_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 5, 1, 1, 1),
    _DrVlConfSlot_Type()
)
drVlConfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drVlConfSlot.setStatus("mandatory")
_DrVlConfIndex_Type = Integer32
_DrVlConfIndex_Object = MibTableColumn
drVlConfIndex = _DrVlConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 5, 1, 1, 2),
    _DrVlConfIndex_Type()
)
drVlConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drVlConfIndex.setStatus("mandatory")


class _DrVlConfAlias_Type(DisplayString):
    """Custom type drVlConfAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DrVlConfAlias_Type.__name__ = "DisplayString"
_DrVlConfAlias_Object = MibTableColumn
drVlConfAlias = _DrVlConfAlias_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 5, 1, 1, 3),
    _DrVlConfAlias_Type()
)
drVlConfAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drVlConfAlias.setStatus("mandatory")
_DrVlConfStatus_Type = RowStatus
_DrVlConfStatus_Object = MibTableColumn
drVlConfStatus = _DrVlConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 5, 1, 1, 4),
    _DrVlConfStatus_Type()
)
drVlConfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drVlConfStatus.setStatus("mandatory")
_DrIpRoute_ObjectIdentity = ObjectIdentity
drIpRoute = _DrIpRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 6)
)
_DrIpInterfaceTable_Object = MibTable
drIpInterfaceTable = _DrIpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1)
)
if mibBuilder.loadTexts:
    drIpInterfaceTable.setStatus("mandatory")
_DrIpInterfaceEntry_Object = MibTableRow
drIpInterfaceEntry = _DrIpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1)
)
drIpInterfaceEntry.setIndexNames(
    (0, "CROUTE-MIB", "drIpInterfaceSlot"),
    (0, "CROUTE-MIB", "drIpInterfaceAddr"),
)
if mibBuilder.loadTexts:
    drIpInterfaceEntry.setStatus("mandatory")
_DrIpInterfaceSlot_Type = Integer32
_DrIpInterfaceSlot_Object = MibTableColumn
drIpInterfaceSlot = _DrIpInterfaceSlot_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1, 1),
    _DrIpInterfaceSlot_Type()
)
drIpInterfaceSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drIpInterfaceSlot.setStatus("mandatory")
_DrIpInterfaceAddr_Type = IpAddress
_DrIpInterfaceAddr_Object = MibTableColumn
drIpInterfaceAddr = _DrIpInterfaceAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1, 2),
    _DrIpInterfaceAddr_Type()
)
drIpInterfaceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drIpInterfaceAddr.setStatus("mandatory")
_DrIpInterfaceNetMask_Type = IpAddress
_DrIpInterfaceNetMask_Object = MibTableColumn
drIpInterfaceNetMask = _DrIpInterfaceNetMask_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1, 3),
    _DrIpInterfaceNetMask_Type()
)
drIpInterfaceNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drIpInterfaceNetMask.setStatus("mandatory")


class _DrIpInterfaceLowerIfAlias_Type(DisplayString):
    """Custom type drIpInterfaceLowerIfAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DrIpInterfaceLowerIfAlias_Type.__name__ = "DisplayString"
_DrIpInterfaceLowerIfAlias_Object = MibTableColumn
drIpInterfaceLowerIfAlias = _DrIpInterfaceLowerIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1, 4),
    _DrIpInterfaceLowerIfAlias_Type()
)
drIpInterfaceLowerIfAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drIpInterfaceLowerIfAlias.setStatus("mandatory")


class _DrIpInterfaceType_Type(Integer32):
    """Custom type drIpInterfaceType based on Integer32"""
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
        *(("broadcast", 1),
          ("nBMA", 2),
          ("ptp", 3))
    )


_DrIpInterfaceType_Type.__name__ = "Integer32"
_DrIpInterfaceType_Object = MibTableColumn
drIpInterfaceType = _DrIpInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1, 5),
    _DrIpInterfaceType_Type()
)
drIpInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drIpInterfaceType.setStatus("mandatory")


class _DrIpInterfaceForwardIpBroadcast_Type(Integer32):
    """Custom type drIpInterfaceForwardIpBroadcast based on Integer32"""
    defaultValue = 1

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


_DrIpInterfaceForwardIpBroadcast_Type.__name__ = "Integer32"
_DrIpInterfaceForwardIpBroadcast_Object = MibTableColumn
drIpInterfaceForwardIpBroadcast = _DrIpInterfaceForwardIpBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1, 6),
    _DrIpInterfaceForwardIpBroadcast_Type()
)
drIpInterfaceForwardIpBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drIpInterfaceForwardIpBroadcast.setStatus("mandatory")


class _DrIpInterfaceBroadcastAddr_Type(Integer32):
    """Custom type drIpInterfaceBroadcastAddr based on Integer32"""
    defaultValue = 1


_DrIpInterfaceBroadcastAddr_Object = MibTableColumn
drIpInterfaceBroadcastAddr = _DrIpInterfaceBroadcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1, 7),
    _DrIpInterfaceBroadcastAddr_Type()
)
drIpInterfaceBroadcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drIpInterfaceBroadcastAddr.setStatus("mandatory")


class _DrIpInterfaceProxyArp_Type(Integer32):
    """Custom type drIpInterfaceProxyArp based on Integer32"""
    defaultValue = 2

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


_DrIpInterfaceProxyArp_Type.__name__ = "Integer32"
_DrIpInterfaceProxyArp_Object = MibTableColumn
drIpInterfaceProxyArp = _DrIpInterfaceProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1, 8),
    _DrIpInterfaceProxyArp_Type()
)
drIpInterfaceProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drIpInterfaceProxyArp.setStatus("mandatory")
_DrIpInterfaceStatus_Type = RowStatus
_DrIpInterfaceStatus_Object = MibTableColumn
drIpInterfaceStatus = _DrIpInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1, 9),
    _DrIpInterfaceStatus_Type()
)
drIpInterfaceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drIpInterfaceStatus.setStatus("mandatory")
_DrIpInterfaceMainRouterAddr_Type = IpAddress
_DrIpInterfaceMainRouterAddr_Object = MibTableColumn
drIpInterfaceMainRouterAddr = _DrIpInterfaceMainRouterAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1, 10),
    _DrIpInterfaceMainRouterAddr_Type()
)
drIpInterfaceMainRouterAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drIpInterfaceMainRouterAddr.setStatus("mandatory")


class _DrIpInterfaceARPServerStatus_Type(Integer32):
    """Custom type drIpInterfaceARPServerStatus based on Integer32"""
    defaultValue = 2

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


_DrIpInterfaceARPServerStatus_Type.__name__ = "Integer32"
_DrIpInterfaceARPServerStatus_Object = MibTableColumn
drIpInterfaceARPServerStatus = _DrIpInterfaceARPServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1, 11),
    _DrIpInterfaceARPServerStatus_Type()
)
drIpInterfaceARPServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drIpInterfaceARPServerStatus.setStatus("mandatory")


class _DrIpInterfaceName_Type(DisplayString):
    """Custom type drIpInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DrIpInterfaceName_Type.__name__ = "DisplayString"
_DrIpInterfaceName_Object = MibTableColumn
drIpInterfaceName = _DrIpInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1, 12),
    _DrIpInterfaceName_Type()
)
drIpInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drIpInterfaceName.setStatus("mandatory")


class _DrIpInterfaceNetbiosRebroadcast_Type(Integer32):
    """Custom type drIpInterfaceNetbiosRebroadcast based on Integer32"""
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
        *(("both", 3),
          ("disable", 4),
          ("inbound", 1),
          ("outbound", 2))
    )


_DrIpInterfaceNetbiosRebroadcast_Type.__name__ = "Integer32"
_DrIpInterfaceNetbiosRebroadcast_Object = MibTableColumn
drIpInterfaceNetbiosRebroadcast = _DrIpInterfaceNetbiosRebroadcast_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1, 13),
    _DrIpInterfaceNetbiosRebroadcast_Type()
)
drIpInterfaceNetbiosRebroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drIpInterfaceNetbiosRebroadcast.setStatus("mandatory")


class _DrIpInterfaceIcmpRedirects_Type(Integer32):
    """Custom type drIpInterfaceIcmpRedirects based on Integer32"""
    defaultValue = 1

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


_DrIpInterfaceIcmpRedirects_Type.__name__ = "Integer32"
_DrIpInterfaceIcmpRedirects_Object = MibTableColumn
drIpInterfaceIcmpRedirects = _DrIpInterfaceIcmpRedirects_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1, 14),
    _DrIpInterfaceIcmpRedirects_Type()
)
drIpInterfaceIcmpRedirects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drIpInterfaceIcmpRedirects.setStatus("mandatory")
_DrStaticCidr_ObjectIdentity = ObjectIdentity
drStaticCidr = _DrStaticCidr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 7)
)
_DrStaticCidrTable_Object = MibTable
drStaticCidrTable = _DrStaticCidrTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1)
)
if mibBuilder.loadTexts:
    drStaticCidrTable.setStatus("mandatory")
_DrStaticCidrEntry_Object = MibTableRow
drStaticCidrEntry = _DrStaticCidrEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1, 1)
)
drStaticCidrEntry.setIndexNames(
    (0, "CROUTE-MIB", "drStaticCidrEntID"),
    (0, "CROUTE-MIB", "drStaticCidrDest"),
    (0, "CROUTE-MIB", "drStaticCidrMask"),
    (0, "CROUTE-MIB", "drStaticCidrTos"),
    (0, "CROUTE-MIB", "drStaticCidrNextHop"),
)
if mibBuilder.loadTexts:
    drStaticCidrEntry.setStatus("mandatory")


class _DrStaticCidrEntID_Type(Integer32):
    """Custom type drStaticCidrEntID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DrStaticCidrEntID_Type.__name__ = "Integer32"
_DrStaticCidrEntID_Object = MibTableColumn
drStaticCidrEntID = _DrStaticCidrEntID_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1, 1, 1),
    _DrStaticCidrEntID_Type()
)
drStaticCidrEntID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drStaticCidrEntID.setStatus("mandatory")
_DrStaticCidrDest_Type = IpAddress
_DrStaticCidrDest_Object = MibTableColumn
drStaticCidrDest = _DrStaticCidrDest_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1, 1, 2),
    _DrStaticCidrDest_Type()
)
drStaticCidrDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drStaticCidrDest.setStatus("mandatory")
_DrStaticCidrMask_Type = IpAddress
_DrStaticCidrMask_Object = MibTableColumn
drStaticCidrMask = _DrStaticCidrMask_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1, 1, 3),
    _DrStaticCidrMask_Type()
)
drStaticCidrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drStaticCidrMask.setStatus("mandatory")


class _DrStaticCidrTos_Type(Integer32):
    """Custom type drStaticCidrTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_DrStaticCidrTos_Type.__name__ = "Integer32"
_DrStaticCidrTos_Object = MibTableColumn
drStaticCidrTos = _DrStaticCidrTos_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1, 1, 4),
    _DrStaticCidrTos_Type()
)
drStaticCidrTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drStaticCidrTos.setStatus("mandatory")
_DrStaticCidrNextHop_Type = IpAddress
_DrStaticCidrNextHop_Object = MibTableColumn
drStaticCidrNextHop = _DrStaticCidrNextHop_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1, 1, 5),
    _DrStaticCidrNextHop_Type()
)
drStaticCidrNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drStaticCidrNextHop.setStatus("mandatory")


class _DrStaticCidrIfIndex_Type(Integer32):
    """Custom type drStaticCidrIfIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_DrStaticCidrIfIndex_Type.__name__ = "Integer32"
_DrStaticCidrIfIndex_Object = MibTableColumn
drStaticCidrIfIndex = _DrStaticCidrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1, 1, 6),
    _DrStaticCidrIfIndex_Type()
)
drStaticCidrIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drStaticCidrIfIndex.setStatus("mandatory")


class _DrStaticCidrType_Type(Integer32):
    """Custom type drStaticCidrType based on Integer32"""
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
        *(("local", 3),
          ("other", 1),
          ("reject", 2),
          ("remote", 4))
    )


_DrStaticCidrType_Type.__name__ = "Integer32"
_DrStaticCidrType_Object = MibTableColumn
drStaticCidrType = _DrStaticCidrType_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1, 1, 7),
    _DrStaticCidrType_Type()
)
drStaticCidrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drStaticCidrType.setStatus("mandatory")


class _DrStaticCidrMetric1_Type(Integer32):
    """Custom type drStaticCidrMetric1 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_DrStaticCidrMetric1_Type.__name__ = "Integer32"
_DrStaticCidrMetric1_Object = MibTableColumn
drStaticCidrMetric1 = _DrStaticCidrMetric1_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1, 1, 8),
    _DrStaticCidrMetric1_Type()
)
drStaticCidrMetric1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drStaticCidrMetric1.setStatus("mandatory")


class _DrStaticCidrPrecedence_Type(Integer32):
    """Custom type drStaticCidrPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DrStaticCidrPrecedence_Type.__name__ = "Integer32"
_DrStaticCidrPrecedence_Object = MibTableColumn
drStaticCidrPrecedence = _DrStaticCidrPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1, 1, 9),
    _DrStaticCidrPrecedence_Type()
)
drStaticCidrPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drStaticCidrPrecedence.setStatus("mandatory")


class _DrStaticCidrCRPType_Type(Integer32):
    """Custom type drStaticCidrCRPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bridgingFWLB", 2),
          ("regularStatic", 3),
          ("routingFWLB", 1))
    )


_DrStaticCidrCRPType_Type.__name__ = "Integer32"
_DrStaticCidrCRPType_Object = MibTableColumn
drStaticCidrCRPType = _DrStaticCidrCRPType_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1, 1, 10),
    _DrStaticCidrCRPType_Type()
)
drStaticCidrCRPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drStaticCidrCRPType.setStatus("mandatory")


class _DrStaticCidrOperStatus_Type(Integer32):
    """Custom type drStaticCidrOperStatus based on Integer32"""
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


_DrStaticCidrOperStatus_Type.__name__ = "Integer32"
_DrStaticCidrOperStatus_Object = MibTableColumn
drStaticCidrOperStatus = _DrStaticCidrOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1, 1, 11),
    _DrStaticCidrOperStatus_Type()
)
drStaticCidrOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drStaticCidrOperStatus.setStatus("mandatory")


class _DrStaticCidrName_Type(DisplayString):
    """Custom type drStaticCidrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DrStaticCidrName_Type.__name__ = "DisplayString"
_DrStaticCidrName_Object = MibTableColumn
drStaticCidrName = _DrStaticCidrName_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1, 1, 12),
    _DrStaticCidrName_Type()
)
drStaticCidrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drStaticCidrName.setStatus("mandatory")


class _DrStaticOwner_Type(OwnerString):
    """Custom type drStaticOwner based on OwnerString"""
    subtypeSpec = OwnerString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrStaticOwner_Type.__name__ = "OwnerString"
_DrStaticOwner_Object = MibTableColumn
drStaticOwner = _DrStaticOwner_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1, 1, 13),
    _DrStaticOwner_Type()
)
drStaticOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drStaticOwner.setStatus("mandatory")
_DrStaticCidrStatus_Type = RowStatus
_DrStaticCidrStatus_Object = MibTableColumn
drStaticCidrStatus = _DrStaticCidrStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1, 1, 14),
    _DrStaticCidrStatus_Type()
)
drStaticCidrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drStaticCidrStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CROUTE-MIB",
    **{"RowStatus": RowStatus,
       "NetNum": NetNum,
       "croute": croute,
       "ipRoute": ipRoute,
       "ipGlobals": ipGlobals,
       "ipGlobalsBOOTPRelayStatus": ipGlobalsBOOTPRelayStatus,
       "ipGlobalsICMPErrMsgEnable": ipGlobalsICMPErrMsgEnable,
       "ipGlobalsARPInactiveTimeout": ipGlobalsARPInactiveTimeout,
       "ipInterfaceTable": ipInterfaceTable,
       "ipInterfaceEntry": ipInterfaceEntry,
       "ipInterfaceAddr": ipInterfaceAddr,
       "ipInterfaceNetMask": ipInterfaceNetMask,
       "ipInterfaceLowerIfAlias": ipInterfaceLowerIfAlias,
       "ipInterfaceType": ipInterfaceType,
       "ipInterfaceForwardIpBroadcast": ipInterfaceForwardIpBroadcast,
       "ipInterfaceBroadcastAddr": ipInterfaceBroadcastAddr,
       "ipInterfaceProxyArp": ipInterfaceProxyArp,
       "ipInterfaceStatus": ipInterfaceStatus,
       "ipInterfaceMainRouterAddr": ipInterfaceMainRouterAddr,
       "ipInterfaceARPServerStatus": ipInterfaceARPServerStatus,
       "ipInterfaceName": ipInterfaceName,
       "ipInterfaceNetbiosRebroadcast": ipInterfaceNetbiosRebroadcast,
       "ipInterfaceIcmpRedirects": ipInterfaceIcmpRedirects,
       "ripGlobals": ripGlobals,
       "ripGlobalsRIPEnable": ripGlobalsRIPEnable,
       "ripGlobalsLeakOSPFIntoRIP": ripGlobalsLeakOSPFIntoRIP,
       "ripGlobalsLeakStaticIntoRIP": ripGlobalsLeakStaticIntoRIP,
       "ripInterfaceTable": ripInterfaceTable,
       "ripInterfaceEntry": ripInterfaceEntry,
       "ripInterfaceAddr": ripInterfaceAddr,
       "ripInterfaceMetric": ripInterfaceMetric,
       "ripInterfaceSplitHorizon": ripInterfaceSplitHorizon,
       "ripInterfaceAcceptDefaultRoute": ripInterfaceAcceptDefaultRoute,
       "ripInterfaceSendDefaultRoute": ripInterfaceSendDefaultRoute,
       "ripInterfaceState": ripInterfaceState,
       "ripInterfaceSendMode": ripInterfaceSendMode,
       "ripInterfaceVersion": ripInterfaceVersion,
       "ospfGlobals": ospfGlobals,
       "ospfGlobalsLeakRIPIntoOSPF": ospfGlobalsLeakRIPIntoOSPF,
       "ospfGlobalsLeakStaticIntoOSPF": ospfGlobalsLeakStaticIntoOSPF,
       "ospfGlobalsLeakDirectIntoOSPF": ospfGlobalsLeakDirectIntoOSPF,
       "relayTable": relayTable,
       "relayEntry": relayEntry,
       "relayVlIndex": relayVlIndex,
       "relayVlPrimaryServerAddr": relayVlPrimaryServerAddr,
       "relayVlSeconderyServerAddr": relayVlSeconderyServerAddr,
       "relayVlStatus": relayVlStatus,
       "relayVlRelayAddr": relayVlRelayAddr,
       "ipAccessGlobals": ipAccessGlobals,
       "ipAccessControlEnable": ipAccessControlEnable,
       "ipAccessControlTable": ipAccessControlTable,
       "ipAccessControlEntry": ipAccessControlEntry,
       "ipAccessControlIndex": ipAccessControlIndex,
       "ipAccessControlSrcAddr": ipAccessControlSrcAddr,
       "ipAccessControlSrcMask": ipAccessControlSrcMask,
       "ipAccessControlDstAddr": ipAccessControlDstAddr,
       "ipAccessControlDstMask": ipAccessControlDstMask,
       "ipAccessControlOperation": ipAccessControlOperation,
       "ipAccessControlActivation": ipAccessControlActivation,
       "ipAccessControlProtocol": ipAccessControlProtocol,
       "ipAccessControlApplication": ipAccessControlApplication,
       "ipAccessControlStatus": ipAccessControlStatus,
       "ipRedundancyGlobals": ipRedundancyGlobals,
       "ipRedundancyStatus": ipRedundancyStatus,
       "ipRedundancyTimeout": ipRedundancyTimeout,
       "ipRedundancyPollingInterval": ipRedundancyPollingInterval,
       "ipShortcutGlobals": ipShortcutGlobals,
       "ipShortcutARPServerStatus": ipShortcutARPServerStatus,
       "ipMulticastInterfaceTable": ipMulticastInterfaceTable,
       "ipMulticastInterfaceEntry": ipMulticastInterfaceEntry,
       "ipMulticastInterfaceIfIndex": ipMulticastInterfaceIfIndex,
       "ipMulticastInterfaceSendAll": ipMulticastInterfaceSendAll,
       "ipMulticastInterfaceState": ipMulticastInterfaceState,
       "ipMulticastInterfaceStatus": ipMulticastInterfaceStatus,
       "ipEZ2RouteMgmt": ipEZ2RouteMgmt,
       "ipEZ2BoostRouterTable": ipEZ2BoostRouterTable,
       "ipEZ2BoostRouterEntry": ipEZ2BoostRouterEntry,
       "ipEZ2BoostRouterSlot": ipEZ2BoostRouterSlot,
       "ipEZ2BoostRouterBRAddress": ipEZ2BoostRouterBRAddress,
       "ipEZ2BoostRouterType": ipEZ2BoostRouterType,
       "ipEZ2BoostRouterStatus": ipEZ2BoostRouterStatus,
       "ipEZ2RControlTable": ipEZ2RControlTable,
       "ipEZ2RControlEntry": ipEZ2RControlEntry,
       "ipEZ2RControlSlot": ipEZ2RControlSlot,
       "ipEZ2RControlBoostedRoutersTimeout": ipEZ2RControlBoostedRoutersTimeout,
       "ipEZ2RControlHostsTimeout": ipEZ2RControlHostsTimeout,
       "ipEZ2RControlAutoLearnMode": ipEZ2RControlAutoLearnMode,
       "ipVRRP": ipVRRP,
       "ipVRRPAdminStatus": ipVRRPAdminStatus,
       "ipxRoute": ipxRoute,
       "ipxCircTable": ipxCircTable,
       "ipxCircEntry": ipxCircEntry,
       "ipxCircIndex": ipxCircIndex,
       "ipxCircNetNumber": ipxCircNetNumber,
       "ipxCircLowerIfAlias": ipxCircLowerIfAlias,
       "ipxCircEncapsulation": ipxCircEncapsulation,
       "ipxCircNetbios": ipxCircNetbios,
       "ipxCircStatus": ipxCircStatus,
       "ipxCircRipUpdate": ipxCircRipUpdate,
       "ipxCircRipAgeMultiplier": ipxCircRipAgeMultiplier,
       "ipxCircRipStatus": ipxCircRipStatus,
       "ipxCircSapUpdate": ipxCircSapUpdate,
       "ipxCircSapAgeMultiplier": ipxCircSapAgeMultiplier,
       "ipxCircGetNearestServerReply": ipxCircGetNearestServerReply,
       "ipxCircSapStatus": ipxCircSapStatus,
       "ipxCircRipState": ipxCircRipState,
       "ipxCircSapState": ipxCircSapState,
       "ipxDestTable": ipxDestTable,
       "ipxDestEntry": ipxDestEntry,
       "ipxDestNetNum": ipxDestNetNum,
       "ipxDestProtocol": ipxDestProtocol,
       "ipxDestTicks": ipxDestTicks,
       "ipxDestHopCount": ipxDestHopCount,
       "ipxDestNextHopCircIndex": ipxDestNextHopCircIndex,
       "ipxDestNextHopNICAddress": ipxDestNextHopNICAddress,
       "ipxDestNextHopNetNum": ipxDestNextHopNetNum,
       "ipxDestStatus": ipxDestStatus,
       "ipxDestAge": ipxDestAge,
       "ipxServTable": ipxServTable,
       "ipxServEntry": ipxServEntry,
       "ipxServType": ipxServType,
       "ipxServName": ipxServName,
       "ipxServProtocol": ipxServProtocol,
       "ipxServNetNum": ipxServNetNum,
       "ipxServNode": ipxServNode,
       "ipxServSocket": ipxServSocket,
       "ipxServHopCount": ipxServHopCount,
       "ipxServStatus": ipxServStatus,
       "ipxServAge": ipxServAge,
       "ipxAccessGlobals": ipxAccessGlobals,
       "ipxAccessControlEnable": ipxAccessControlEnable,
       "ipxAccessControlTable": ipxAccessControlTable,
       "ipxAccessControlEntry": ipxAccessControlEntry,
       "ipxAccessControlIndex": ipxAccessControlIndex,
       "ipxAccessControlSrcAddr": ipxAccessControlSrcAddr,
       "ipxAccessControlDstAddr": ipxAccessControlDstAddr,
       "ipxAccessControlOperation": ipxAccessControlOperation,
       "ipxAccessControlActivation": ipxAccessControlActivation,
       "ipxAccessControlStatus": ipxAccessControlStatus,
       "ipxSapFilterGlobals": ipxSapFilterGlobals,
       "ipxSapFilterEnable": ipxSapFilterEnable,
       "ipxSapFilterTable": ipxSapFilterTable,
       "ipxSapFilterEntry": ipxSapFilterEntry,
       "ipxSapFilterID": ipxSapFilterID,
       "ipxSapFilterCircIndex": ipxSapFilterCircIndex,
       "ipxSapFilterServiceNetNumber": ipxSapFilterServiceNetNumber,
       "ipxSapFilterServiceType": ipxSapFilterServiceType,
       "ipxSapFilterServerName": ipxSapFilterServerName,
       "ipxSapFilterDirection": ipxSapFilterDirection,
       "ipxSapFilterAction": ipxSapFilterAction,
       "ipxSapFilterStatus": ipxSapFilterStatus,
       "layer2": layer2,
       "vlConfTable": vlConfTable,
       "vlConfEntry": vlConfEntry,
       "vlConfIndex": vlConfIndex,
       "vlConfAlias": vlConfAlias,
       "vlConfStatus": vlConfStatus,
       "vlBridgeTable": vlBridgeTable,
       "vlBridgeEntry": vlBridgeEntry,
       "vlBridgeProtocol": vlBridgeProtocol,
       "vlBridgeGroupIndex": vlBridgeGroupIndex,
       "vlBridgeIndex": vlBridgeIndex,
       "vlBridgeStatus": vlBridgeStatus,
       "layer2Globals": layer2Globals,
       "layer2GlobalsBridgeEnable": layer2GlobalsBridgeEnable,
       "routeGroupMgmt": routeGroupMgmt,
       "routeGroupTable": routeGroupTable,
       "routeGroupEntry": routeGroupEntry,
       "routeGroupId": routeGroupId,
       "routeGroupRouteMode": routeGroupRouteMode,
       "drLayer2": drLayer2,
       "drVlConfTable": drVlConfTable,
       "drVlConfEntry": drVlConfEntry,
       "drVlConfSlot": drVlConfSlot,
       "drVlConfIndex": drVlConfIndex,
       "drVlConfAlias": drVlConfAlias,
       "drVlConfStatus": drVlConfStatus,
       "drIpRoute": drIpRoute,
       "drIpInterfaceTable": drIpInterfaceTable,
       "drIpInterfaceEntry": drIpInterfaceEntry,
       "drIpInterfaceSlot": drIpInterfaceSlot,
       "drIpInterfaceAddr": drIpInterfaceAddr,
       "drIpInterfaceNetMask": drIpInterfaceNetMask,
       "drIpInterfaceLowerIfAlias": drIpInterfaceLowerIfAlias,
       "drIpInterfaceType": drIpInterfaceType,
       "drIpInterfaceForwardIpBroadcast": drIpInterfaceForwardIpBroadcast,
       "drIpInterfaceBroadcastAddr": drIpInterfaceBroadcastAddr,
       "drIpInterfaceProxyArp": drIpInterfaceProxyArp,
       "drIpInterfaceStatus": drIpInterfaceStatus,
       "drIpInterfaceMainRouterAddr": drIpInterfaceMainRouterAddr,
       "drIpInterfaceARPServerStatus": drIpInterfaceARPServerStatus,
       "drIpInterfaceName": drIpInterfaceName,
       "drIpInterfaceNetbiosRebroadcast": drIpInterfaceNetbiosRebroadcast,
       "drIpInterfaceIcmpRedirects": drIpInterfaceIcmpRedirects,
       "drStaticCidr": drStaticCidr,
       "drStaticCidrTable": drStaticCidrTable,
       "drStaticCidrEntry": drStaticCidrEntry,
       "drStaticCidrEntID": drStaticCidrEntID,
       "drStaticCidrDest": drStaticCidrDest,
       "drStaticCidrMask": drStaticCidrMask,
       "drStaticCidrTos": drStaticCidrTos,
       "drStaticCidrNextHop": drStaticCidrNextHop,
       "drStaticCidrIfIndex": drStaticCidrIfIndex,
       "drStaticCidrType": drStaticCidrType,
       "drStaticCidrMetric1": drStaticCidrMetric1,
       "drStaticCidrPrecedence": drStaticCidrPrecedence,
       "drStaticCidrCRPType": drStaticCidrCRPType,
       "drStaticCidrOperStatus": drStaticCidrOperStatus,
       "drStaticCidrName": drStaticCidrName,
       "drStaticOwner": drStaticOwner,
       "drStaticCidrStatus": drStaticCidrStatus}
)
