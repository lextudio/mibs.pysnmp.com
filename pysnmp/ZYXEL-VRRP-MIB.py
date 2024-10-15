# SNMP MIB module (ZYXEL-VRRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-VRRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:23:07 2024
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")

(zyRouteDomainIpAddress,
 zyRouteDomainIpMaskBits) = mibBuilder.importSymbols(
    "ZYXEL-IP-FORWARD-MIB",
    "zyRouteDomainIpAddress",
    "zyRouteDomainIpMaskBits")


# MODULE-IDENTITY

zyxelVrrp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 91)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelVrrpSetup_ObjectIdentity = ObjectIdentity
zyxelVrrpSetup = _ZyxelVrrpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 91, 1)
)
_ZyVrrpMaxNumberOfVirtualRouters_Type = Integer32
_ZyVrrpMaxNumberOfVirtualRouters_Object = MibScalar
zyVrrpMaxNumberOfVirtualRouters = _ZyVrrpMaxNumberOfVirtualRouters_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 91, 1, 1),
    _ZyVrrpMaxNumberOfVirtualRouters_Type()
)
zyVrrpMaxNumberOfVirtualRouters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyVrrpMaxNumberOfVirtualRouters.setStatus("current")
_ZyxelVrrpTable_Object = MibTable
zyxelVrrpTable = _ZyxelVrrpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 91, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelVrrpTable.setStatus("current")
_ZyxelVrrpEntry_Object = MibTableRow
zyxelVrrpEntry = _ZyxelVrrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 91, 1, 2, 1)
)
zyxelVrrpEntry.setIndexNames(
    (0, "ZYXEL-IP-FORWARD-MIB", "zyRouteDomainIpAddress"),
    (0, "ZYXEL-IP-FORWARD-MIB", "zyRouteDomainIpMaskBits"),
    (0, "ZYXEL-VRRP-MIB", "zyVrrpVirtualId"),
    (0, "ZYXEL-VRRP-MIB", "zyVrrpUplinkGateway"),
)
if mibBuilder.loadTexts:
    zyxelVrrpEntry.setStatus("current")
_ZyVrrpVirtualId_Type = Integer32
_ZyVrrpVirtualId_Object = MibTableColumn
zyVrrpVirtualId = _ZyVrrpVirtualId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 91, 1, 2, 1, 1),
    _ZyVrrpVirtualId_Type()
)
zyVrrpVirtualId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyVrrpVirtualId.setStatus("current")
_ZyVrrpUplinkGateway_Type = IpAddress
_ZyVrrpUplinkGateway_Object = MibTableColumn
zyVrrpUplinkGateway = _ZyVrrpUplinkGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 91, 1, 2, 1, 2),
    _ZyVrrpUplinkGateway_Type()
)
zyVrrpUplinkGateway.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyVrrpUplinkGateway.setStatus("current")
_ZyVrrpPreemptState_Type = EnabledStatus
_ZyVrrpPreemptState_Object = MibTableColumn
zyVrrpPreemptState = _ZyVrrpPreemptState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 91, 1, 2, 1, 3),
    _ZyVrrpPreemptState_Type()
)
zyVrrpPreemptState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyVrrpPreemptState.setStatus("current")
_ZyVrrpInterval_Type = Integer32
_ZyVrrpInterval_Object = MibTableColumn
zyVrrpInterval = _ZyVrrpInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 91, 1, 2, 1, 4),
    _ZyVrrpInterval_Type()
)
zyVrrpInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyVrrpInterval.setStatus("current")
_ZyVrrpPriority_Type = Integer32
_ZyVrrpPriority_Object = MibTableColumn
zyVrrpPriority = _ZyVrrpPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 91, 1, 2, 1, 5),
    _ZyVrrpPriority_Type()
)
zyVrrpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyVrrpPriority.setStatus("current")
_ZyVrrpPrimaryVirtualpAddress_Type = IpAddress
_ZyVrrpPrimaryVirtualpAddress_Object = MibTableColumn
zyVrrpPrimaryVirtualpAddress = _ZyVrrpPrimaryVirtualpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 91, 1, 2, 1, 6),
    _ZyVrrpPrimaryVirtualpAddress_Type()
)
zyVrrpPrimaryVirtualpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyVrrpPrimaryVirtualpAddress.setStatus("current")
_ZyVrrpName_Type = DisplayString
_ZyVrrpName_Object = MibTableColumn
zyVrrpName = _ZyVrrpName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 91, 1, 2, 1, 7),
    _ZyVrrpName_Type()
)
zyVrrpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyVrrpName.setStatus("current")
_ZyVrrpSecondaryVirtualIpAddress_Type = IpAddress
_ZyVrrpSecondaryVirtualIpAddress_Object = MibTableColumn
zyVrrpSecondaryVirtualIpAddress = _ZyVrrpSecondaryVirtualIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 91, 1, 2, 1, 8),
    _ZyVrrpSecondaryVirtualIpAddress_Type()
)
zyVrrpSecondaryVirtualIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyVrrpSecondaryVirtualIpAddress.setStatus("current")
_ZyVrrpPingState_Type = EnabledStatus
_ZyVrrpPingState_Object = MibTableColumn
zyVrrpPingState = _ZyVrrpPingState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 91, 1, 2, 1, 9),
    _ZyVrrpPingState_Type()
)
zyVrrpPingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyVrrpPingState.setStatus("current")
_ZyVrrpRowStatus_Type = RowStatus
_ZyVrrpRowStatus_Object = MibTableColumn
zyVrrpRowStatus = _ZyVrrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 91, 1, 2, 1, 10),
    _ZyVrrpRowStatus_Type()
)
zyVrrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyVrrpRowStatus.setStatus("current")
_ZyxelVrrpDomainTable_Object = MibTable
zyxelVrrpDomainTable = _ZyxelVrrpDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 91, 1, 3)
)
if mibBuilder.loadTexts:
    zyxelVrrpDomainTable.setStatus("current")
_ZyxelVrrpDomainEntry_Object = MibTableRow
zyxelVrrpDomainEntry = _ZyxelVrrpDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 91, 1, 3, 1)
)
zyxelVrrpDomainEntry.setIndexNames(
    (0, "ZYXEL-IP-FORWARD-MIB", "zyRouteDomainIpAddress"),
    (0, "ZYXEL-IP-FORWARD-MIB", "zyRouteDomainIpMaskBits"),
)
if mibBuilder.loadTexts:
    zyxelVrrpDomainEntry.setStatus("current")


class _ZyVrrpDomainAuthenticationType_Type(Integer32):
    """Custom type zyVrrpDomainAuthenticationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("simple", 1))
    )


_ZyVrrpDomainAuthenticationType_Type.__name__ = "Integer32"
_ZyVrrpDomainAuthenticationType_Object = MibTableColumn
zyVrrpDomainAuthenticationType = _ZyVrrpDomainAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 91, 1, 3, 1, 1),
    _ZyVrrpDomainAuthenticationType_Type()
)
zyVrrpDomainAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyVrrpDomainAuthenticationType.setStatus("current")
_ZyVrrpDomainAuthenticationKey_Type = DisplayString
_ZyVrrpDomainAuthenticationKey_Object = MibTableColumn
zyVrrpDomainAuthenticationKey = _ZyVrrpDomainAuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 91, 1, 3, 1, 2),
    _ZyVrrpDomainAuthenticationKey_Type()
)
zyVrrpDomainAuthenticationKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyVrrpDomainAuthenticationKey.setStatus("current")
_ZyxelVrrpStatus_ObjectIdentity = ObjectIdentity
zyxelVrrpStatus = _ZyxelVrrpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 91, 2)
)
_ZyxelVrrpInfoTable_Object = MibTable
zyxelVrrpInfoTable = _ZyxelVrrpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 91, 2, 1)
)
if mibBuilder.loadTexts:
    zyxelVrrpInfoTable.setStatus("current")
_ZyxelVrrpInfoEntry_Object = MibTableRow
zyxelVrrpInfoEntry = _ZyxelVrrpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 91, 2, 1, 1)
)
zyxelVrrpInfoEntry.setIndexNames(
    (0, "ZYXEL-VRRP-MIB", "zyVrrpInfoIpAddress"),
    (0, "ZYXEL-VRRP-MIB", "zyVrrpInfoIpMaskBits"),
    (0, "ZYXEL-VRRP-MIB", "zyVrrpInfoVirtualId"),
)
if mibBuilder.loadTexts:
    zyxelVrrpInfoEntry.setStatus("current")
_ZyVrrpInfoIpAddress_Type = IpAddress
_ZyVrrpInfoIpAddress_Object = MibTableColumn
zyVrrpInfoIpAddress = _ZyVrrpInfoIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 91, 2, 1, 1, 1),
    _ZyVrrpInfoIpAddress_Type()
)
zyVrrpInfoIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyVrrpInfoIpAddress.setStatus("current")
_ZyVrrpInfoIpMaskBits_Type = Integer32
_ZyVrrpInfoIpMaskBits_Object = MibTableColumn
zyVrrpInfoIpMaskBits = _ZyVrrpInfoIpMaskBits_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 91, 2, 1, 1, 2),
    _ZyVrrpInfoIpMaskBits_Type()
)
zyVrrpInfoIpMaskBits.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyVrrpInfoIpMaskBits.setStatus("current")
_ZyVrrpInfoVirtualId_Type = Integer32
_ZyVrrpInfoVirtualId_Object = MibTableColumn
zyVrrpInfoVirtualId = _ZyVrrpInfoVirtualId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 91, 2, 1, 1, 3),
    _ZyVrrpInfoVirtualId_Type()
)
zyVrrpInfoVirtualId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyVrrpInfoVirtualId.setStatus("current")
_ZyVrrpInfoVirtualRouterStatus_Type = DisplayString
_ZyVrrpInfoVirtualRouterStatus_Object = MibTableColumn
zyVrrpInfoVirtualRouterStatus = _ZyVrrpInfoVirtualRouterStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 91, 2, 1, 1, 4),
    _ZyVrrpInfoVirtualRouterStatus_Type()
)
zyVrrpInfoVirtualRouterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyVrrpInfoVirtualRouterStatus.setStatus("current")
_ZyVrrpInfoUplinkStatus_Type = DisplayString
_ZyVrrpInfoUplinkStatus_Object = MibTableColumn
zyVrrpInfoUplinkStatus = _ZyVrrpInfoUplinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 91, 2, 1, 1, 5),
    _ZyVrrpInfoUplinkStatus_Type()
)
zyVrrpInfoUplinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyVrrpInfoUplinkStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-VRRP-MIB",
    **{"zyxelVrrp": zyxelVrrp,
       "zyxelVrrpSetup": zyxelVrrpSetup,
       "zyVrrpMaxNumberOfVirtualRouters": zyVrrpMaxNumberOfVirtualRouters,
       "zyxelVrrpTable": zyxelVrrpTable,
       "zyxelVrrpEntry": zyxelVrrpEntry,
       "zyVrrpVirtualId": zyVrrpVirtualId,
       "zyVrrpUplinkGateway": zyVrrpUplinkGateway,
       "zyVrrpPreemptState": zyVrrpPreemptState,
       "zyVrrpInterval": zyVrrpInterval,
       "zyVrrpPriority": zyVrrpPriority,
       "zyVrrpPrimaryVirtualpAddress": zyVrrpPrimaryVirtualpAddress,
       "zyVrrpName": zyVrrpName,
       "zyVrrpSecondaryVirtualIpAddress": zyVrrpSecondaryVirtualIpAddress,
       "zyVrrpPingState": zyVrrpPingState,
       "zyVrrpRowStatus": zyVrrpRowStatus,
       "zyxelVrrpDomainTable": zyxelVrrpDomainTable,
       "zyxelVrrpDomainEntry": zyxelVrrpDomainEntry,
       "zyVrrpDomainAuthenticationType": zyVrrpDomainAuthenticationType,
       "zyVrrpDomainAuthenticationKey": zyVrrpDomainAuthenticationKey,
       "zyxelVrrpStatus": zyxelVrrpStatus,
       "zyxelVrrpInfoTable": zyxelVrrpInfoTable,
       "zyxelVrrpInfoEntry": zyxelVrrpInfoEntry,
       "zyVrrpInfoIpAddress": zyVrrpInfoIpAddress,
       "zyVrrpInfoIpMaskBits": zyVrrpInfoIpMaskBits,
       "zyVrrpInfoVirtualId": zyVrrpInfoVirtualId,
       "zyVrrpInfoVirtualRouterStatus": zyVrrpInfoVirtualRouterStatus,
       "zyVrrpInfoUplinkStatus": zyVrrpInfoUplinkStatus}
)
