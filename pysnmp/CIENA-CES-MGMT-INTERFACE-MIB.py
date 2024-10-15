# SNMP MIB module (CIENA-CES-MGMT-INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CIENA-CES-MGMT-INTERFACE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:00 2024
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

(cienaGlobalMacAddress,
 cienaGlobalSeverity) = mibBuilder.importSymbols(
    "CIENA-GLOBAL-MIB",
    "cienaGlobalMacAddress",
    "cienaGlobalSeverity")

(cienaCesConfig,
 cienaCesNotifications) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications")

(CienaGlobalState,) = mibBuilder.importSymbols(
    "CIENA-TC",
    "CienaGlobalState")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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

cienaCesMgmtInterfaceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27)
)
cienaCesMgmtInterfaceMIB.setRevisions(
        ("2015-05-15 00:00",
         "2015-04-23 00:00",
         "2015-04-06 00:00",
         "2014-11-18 00:00",
         "2014-10-07 00:00",
         "2013-06-17 00:00",
         "2012-04-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaCesMgmtInterfaceMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesMgmtInterfaceMIBObjects = _CienaCesMgmtInterfaceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1)
)
_CienaCesMgmtInterface_ObjectIdentity = ObjectIdentity
cienaCesMgmtInterface = _CienaCesMgmtInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1)
)
_CienaCesInetMgmtInterfaceTable_Object = MibTable
cienaCesInetMgmtInterfaceTable = _CienaCesInetMgmtInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cienaCesInetMgmtInterfaceTable.setStatus("current")
_CienaCesInetMgmtInterfaceEntry_Object = MibTableRow
cienaCesInetMgmtInterfaceEntry = _CienaCesInetMgmtInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 1, 1)
)
cienaCesInetMgmtInterfaceEntry.setIndexNames(
    (0, "CIENA-CES-MGMT-INTERFACE-MIB", "cienaCesInetMgmtInterfaceIndex"),
    (0, "CIENA-CES-MGMT-INTERFACE-MIB", "cienaCesInetMgmtInterfaceAddrType"),
    (0, "CIENA-CES-MGMT-INTERFACE-MIB", "cienaCesInetMgmtInterfaceAddr"),
)
if mibBuilder.loadTexts:
    cienaCesInetMgmtInterfaceEntry.setStatus("current")


class _CienaCesInetMgmtInterfaceIndex_Type(Integer32):
    """Custom type cienaCesInetMgmtInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CienaCesInetMgmtInterfaceIndex_Type.__name__ = "Integer32"
_CienaCesInetMgmtInterfaceIndex_Object = MibTableColumn
cienaCesInetMgmtInterfaceIndex = _CienaCesInetMgmtInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 1, 1, 1),
    _CienaCesInetMgmtInterfaceIndex_Type()
)
cienaCesInetMgmtInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesInetMgmtInterfaceIndex.setStatus("current")
_CienaCesInetMgmtInterfaceAddrType_Type = InetAddressType
_CienaCesInetMgmtInterfaceAddrType_Object = MibTableColumn
cienaCesInetMgmtInterfaceAddrType = _CienaCesInetMgmtInterfaceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 1, 1, 2),
    _CienaCesInetMgmtInterfaceAddrType_Type()
)
cienaCesInetMgmtInterfaceAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesInetMgmtInterfaceAddrType.setStatus("current")
_CienaCesInetMgmtInterfaceAddr_Type = InetAddress
_CienaCesInetMgmtInterfaceAddr_Object = MibTableColumn
cienaCesInetMgmtInterfaceAddr = _CienaCesInetMgmtInterfaceAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 1, 1, 3),
    _CienaCesInetMgmtInterfaceAddr_Type()
)
cienaCesInetMgmtInterfaceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesInetMgmtInterfaceAddr.setStatus("current")
_CienaCesInetMgmtInterfaceAddrPrefixLength_Type = InetAddressPrefixLength
_CienaCesInetMgmtInterfaceAddrPrefixLength_Object = MibTableColumn
cienaCesInetMgmtInterfaceAddrPrefixLength = _CienaCesInetMgmtInterfaceAddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 1, 1, 4),
    _CienaCesInetMgmtInterfaceAddrPrefixLength_Type()
)
cienaCesInetMgmtInterfaceAddrPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInetMgmtInterfaceAddrPrefixLength.setStatus("current")


class _CienaCesInetMgmtInterfaceName_Type(DisplayString):
    """Custom type cienaCesInetMgmtInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CienaCesInetMgmtInterfaceName_Type.__name__ = "DisplayString"
_CienaCesInetMgmtInterfaceName_Object = MibTableColumn
cienaCesInetMgmtInterfaceName = _CienaCesInetMgmtInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 1, 1, 5),
    _CienaCesInetMgmtInterfaceName_Type()
)
cienaCesInetMgmtInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInetMgmtInterfaceName.setStatus("current")
_CienaCesInetMgmtInterfaceAdminState_Type = CienaGlobalState
_CienaCesInetMgmtInterfaceAdminState_Object = MibTableColumn
cienaCesInetMgmtInterfaceAdminState = _CienaCesInetMgmtInterfaceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 1, 1, 6),
    _CienaCesInetMgmtInterfaceAdminState_Type()
)
cienaCesInetMgmtInterfaceAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInetMgmtInterfaceAdminState.setStatus("current")
_CienaCesInetMgmtInterfaceOperState_Type = CienaGlobalState
_CienaCesInetMgmtInterfaceOperState_Object = MibTableColumn
cienaCesInetMgmtInterfaceOperState = _CienaCesInetMgmtInterfaceOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 1, 1, 7),
    _CienaCesInetMgmtInterfaceOperState_Type()
)
cienaCesInetMgmtInterfaceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInetMgmtInterfaceOperState.setStatus("current")


class _CienaCesInetMgmtInterfaceDomain_Type(Integer32):
    """Custom type cienaCesInetMgmtInterfaceDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("vlan", 3),
          ("vs", 2))
    )


_CienaCesInetMgmtInterfaceDomain_Type.__name__ = "Integer32"
_CienaCesInetMgmtInterfaceDomain_Object = MibTableColumn
cienaCesInetMgmtInterfaceDomain = _CienaCesInetMgmtInterfaceDomain_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 1, 1, 8),
    _CienaCesInetMgmtInterfaceDomain_Type()
)
cienaCesInetMgmtInterfaceDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInetMgmtInterfaceDomain.setStatus("current")
_CienaCesInetMgmtInterfaceDomainId_Type = Integer32
_CienaCesInetMgmtInterfaceDomainId_Object = MibTableColumn
cienaCesInetMgmtInterfaceDomainId = _CienaCesInetMgmtInterfaceDomainId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 1, 1, 9),
    _CienaCesInetMgmtInterfaceDomainId_Type()
)
cienaCesInetMgmtInterfaceDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInetMgmtInterfaceDomainId.setStatus("current")


class _CienaCesInetMgmtInterfacePktPriority_Type(Integer32):
    """Custom type cienaCesInetMgmtInterfacePktPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesInetMgmtInterfacePktPriority_Type.__name__ = "Integer32"
_CienaCesInetMgmtInterfacePktPriority_Object = MibTableColumn
cienaCesInetMgmtInterfacePktPriority = _CienaCesInetMgmtInterfacePktPriority_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 1, 1, 10),
    _CienaCesInetMgmtInterfacePktPriority_Type()
)
cienaCesInetMgmtInterfacePktPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInetMgmtInterfacePktPriority.setStatus("current")
_CienaCesInetMgmtInterfaceMtu_Type = Unsigned32
_CienaCesInetMgmtInterfaceMtu_Object = MibTableColumn
cienaCesInetMgmtInterfaceMtu = _CienaCesInetMgmtInterfaceMtu_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 1, 1, 11),
    _CienaCesInetMgmtInterfaceMtu_Type()
)
cienaCesInetMgmtInterfaceMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInetMgmtInterfaceMtu.setStatus("current")
_CienaCesInetMgmtInterfaceNotifIndex_Type = Integer32
_CienaCesInetMgmtInterfaceNotifIndex_Object = MibTableColumn
cienaCesInetMgmtInterfaceNotifIndex = _CienaCesInetMgmtInterfaceNotifIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 1, 1, 12),
    _CienaCesInetMgmtInterfaceNotifIndex_Type()
)
cienaCesInetMgmtInterfaceNotifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInetMgmtInterfaceNotifIndex.setStatus("current")
_CienaCesInetMgmtInterfaceNotifAddrType_Type = InetAddressType
_CienaCesInetMgmtInterfaceNotifAddrType_Object = MibTableColumn
cienaCesInetMgmtInterfaceNotifAddrType = _CienaCesInetMgmtInterfaceNotifAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 1, 1, 13),
    _CienaCesInetMgmtInterfaceNotifAddrType_Type()
)
cienaCesInetMgmtInterfaceNotifAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInetMgmtInterfaceNotifAddrType.setStatus("current")
_CienaCesInetMgmtInterfaceNotifAddr_Type = InetAddress
_CienaCesInetMgmtInterfaceNotifAddr_Object = MibTableColumn
cienaCesInetMgmtInterfaceNotifAddr = _CienaCesInetMgmtInterfaceNotifAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 1, 1, 14),
    _CienaCesInetMgmtInterfaceNotifAddr_Type()
)
cienaCesInetMgmtInterfaceNotifAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInetMgmtInterfaceNotifAddr.setStatus("current")


class _CienaCesInetMgmtInterfaceDomainVsName_Type(DisplayString):
    """Custom type cienaCesInetMgmtInterfaceDomainVsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesInetMgmtInterfaceDomainVsName_Type.__name__ = "DisplayString"
_CienaCesInetMgmtInterfaceDomainVsName_Object = MibTableColumn
cienaCesInetMgmtInterfaceDomainVsName = _CienaCesInetMgmtInterfaceDomainVsName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 1, 1, 15),
    _CienaCesInetMgmtInterfaceDomainVsName_Type()
)
cienaCesInetMgmtInterfaceDomainVsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInetMgmtInterfaceDomainVsName.setStatus("current")


class _CienaCesInetMgmtInterfaceIngressAclProfId_Type(Unsigned32):
    """Custom type cienaCesInetMgmtInterfaceIngressAclProfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CienaCesInetMgmtInterfaceIngressAclProfId_Type.__name__ = "Unsigned32"
_CienaCesInetMgmtInterfaceIngressAclProfId_Object = MibTableColumn
cienaCesInetMgmtInterfaceIngressAclProfId = _CienaCesInetMgmtInterfaceIngressAclProfId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 1, 1, 16),
    _CienaCesInetMgmtInterfaceIngressAclProfId_Type()
)
cienaCesInetMgmtInterfaceIngressAclProfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInetMgmtInterfaceIngressAclProfId.setStatus("current")
_CienaCesInetGatewayTable_Object = MibTable
cienaCesInetGatewayTable = _CienaCesInetGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cienaCesInetGatewayTable.setStatus("current")
_CienaCesInetGatewayEntry_Object = MibTableRow
cienaCesInetGatewayEntry = _CienaCesInetGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 2, 1)
)
cienaCesInetGatewayEntry.setIndexNames(
    (0, "CIENA-CES-MGMT-INTERFACE-MIB", "cienaCesInetGatewayAddrType"),
    (0, "CIENA-CES-MGMT-INTERFACE-MIB", "cienaCesInetGatewayAddr"),
)
if mibBuilder.loadTexts:
    cienaCesInetGatewayEntry.setStatus("current")
_CienaCesInetGatewayAddrType_Type = InetAddressType
_CienaCesInetGatewayAddrType_Object = MibTableColumn
cienaCesInetGatewayAddrType = _CienaCesInetGatewayAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 2, 1, 2),
    _CienaCesInetGatewayAddrType_Type()
)
cienaCesInetGatewayAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesInetGatewayAddrType.setStatus("current")
_CienaCesInetGatewayAddr_Type = InetAddress
_CienaCesInetGatewayAddr_Object = MibTableColumn
cienaCesInetGatewayAddr = _CienaCesInetGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 2, 1, 3),
    _CienaCesInetGatewayAddr_Type()
)
cienaCesInetGatewayAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesInetGatewayAddr.setStatus("current")


class _CienaCesInetGatewaySource_Type(Integer32):
    """Custom type cienaCesInetGatewaySource based on Integer32"""
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
        *(("auto", 5),
          ("dhcpv4", 2),
          ("unknown", 1),
          ("userConfiguredBackup", 4),
          ("userConfiguredPrimary", 3))
    )


_CienaCesInetGatewaySource_Type.__name__ = "Integer32"
_CienaCesInetGatewaySource_Object = MibTableColumn
cienaCesInetGatewaySource = _CienaCesInetGatewaySource_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 2, 1, 4),
    _CienaCesInetGatewaySource_Type()
)
cienaCesInetGatewaySource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInetGatewaySource.setStatus("current")


class _CienaCesInetGatewayOperState_Type(Integer32):
    """Custom type cienaCesInetGatewayOperState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("selected", 1),
          ("standby", 5),
          ("unavailable", 4))
    )


_CienaCesInetGatewayOperState_Type.__name__ = "Integer32"
_CienaCesInetGatewayOperState_Object = MibTableColumn
cienaCesInetGatewayOperState = _CienaCesInetGatewayOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 2, 1, 5),
    _CienaCesInetGatewayOperState_Type()
)
cienaCesInetGatewayOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInetGatewayOperState.setStatus("current")
_CienaCesInetGatewayNotifAddrType_Type = InetAddressType
_CienaCesInetGatewayNotifAddrType_Object = MibTableColumn
cienaCesInetGatewayNotifAddrType = _CienaCesInetGatewayNotifAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 2, 1, 6),
    _CienaCesInetGatewayNotifAddrType_Type()
)
cienaCesInetGatewayNotifAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInetGatewayNotifAddrType.setStatus("current")
_CienaCesInetGatewayNotifAddr_Type = InetAddress
_CienaCesInetGatewayNotifAddr_Object = MibTableColumn
cienaCesInetGatewayNotifAddr = _CienaCesInetGatewayNotifAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 2, 1, 7),
    _CienaCesInetGatewayNotifAddr_Type()
)
cienaCesInetGatewayNotifAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInetGatewayNotifAddr.setStatus("current")
_CienaCesInetStackTable_Object = MibTable
cienaCesInetStackTable = _CienaCesInetStackTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cienaCesInetStackTable.setStatus("current")
_CienaCesInetStackEntry_Object = MibTableRow
cienaCesInetStackEntry = _CienaCesInetStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 3, 1)
)
cienaCesInetStackEntry.setIndexNames(
    (0, "CIENA-CES-MGMT-INTERFACE-MIB", "cienaCesInetAddrType"),
)
if mibBuilder.loadTexts:
    cienaCesInetStackEntry.setStatus("current")
_CienaCesInetAddrType_Type = InetAddressType
_CienaCesInetAddrType_Object = MibTableColumn
cienaCesInetAddrType = _CienaCesInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 3, 1, 1),
    _CienaCesInetAddrType_Type()
)
cienaCesInetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesInetAddrType.setStatus("current")


class _CienaCesInetForwardingState_Type(Integer32):
    """Custom type cienaCesInetForwardingState based on Integer32"""
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


_CienaCesInetForwardingState_Type.__name__ = "Integer32"
_CienaCesInetForwardingState_Object = MibTableColumn
cienaCesInetForwardingState = _CienaCesInetForwardingState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 3, 1, 2),
    _CienaCesInetForwardingState_Type()
)
cienaCesInetForwardingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInetForwardingState.setStatus("current")
_CienaCesInetDefaultDscp_Type = Unsigned32
_CienaCesInetDefaultDscp_Object = MibTableColumn
cienaCesInetDefaultDscp = _CienaCesInetDefaultDscp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 3, 1, 3),
    _CienaCesInetDefaultDscp_Type()
)
cienaCesInetDefaultDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInetDefaultDscp.setStatus("current")


class _CienaCesInetIcmpAcceptRedirects_Type(Integer32):
    """Custom type cienaCesInetIcmpAcceptRedirects based on Integer32"""
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


_CienaCesInetIcmpAcceptRedirects_Type.__name__ = "Integer32"
_CienaCesInetIcmpAcceptRedirects_Object = MibTableColumn
cienaCesInetIcmpAcceptRedirects = _CienaCesInetIcmpAcceptRedirects_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 3, 1, 4),
    _CienaCesInetIcmpAcceptRedirects_Type()
)
cienaCesInetIcmpAcceptRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInetIcmpAcceptRedirects.setStatus("current")


class _CienaCesInetIcmpEchoIgnoreBroadcasts_Type(Integer32):
    """Custom type cienaCesInetIcmpEchoIgnoreBroadcasts based on Integer32"""
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


_CienaCesInetIcmpEchoIgnoreBroadcasts_Type.__name__ = "Integer32"
_CienaCesInetIcmpEchoIgnoreBroadcasts_Object = MibTableColumn
cienaCesInetIcmpEchoIgnoreBroadcasts = _CienaCesInetIcmpEchoIgnoreBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 3, 1, 5),
    _CienaCesInetIcmpEchoIgnoreBroadcasts_Type()
)
cienaCesInetIcmpEchoIgnoreBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInetIcmpEchoIgnoreBroadcasts.setStatus("current")


class _CienaCesInetIcmpPortUnreachable_Type(Integer32):
    """Custom type cienaCesInetIcmpPortUnreachable based on Integer32"""
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


_CienaCesInetIcmpPortUnreachable_Type.__name__ = "Integer32"
_CienaCesInetIcmpPortUnreachable_Object = MibTableColumn
cienaCesInetIcmpPortUnreachable = _CienaCesInetIcmpPortUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 3, 1, 6),
    _CienaCesInetIcmpPortUnreachable_Type()
)
cienaCesInetIcmpPortUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInetIcmpPortUnreachable.setStatus("current")
_CienaCesInetTcpStack_ObjectIdentity = ObjectIdentity
cienaCesInetTcpStack = _CienaCesInetTcpStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 4)
)


class _CienaCesInetTcpTimestamps_Type(Integer32):
    """Custom type cienaCesInetTcpTimestamps based on Integer32"""
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


_CienaCesInetTcpTimestamps_Type.__name__ = "Integer32"
_CienaCesInetTcpTimestamps_Object = MibScalar
cienaCesInetTcpTimestamps = _CienaCesInetTcpTimestamps_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 4, 1),
    _CienaCesInetTcpTimestamps_Type()
)
cienaCesInetTcpTimestamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInetTcpTimestamps.setStatus("current")
_CienaCesInetMgmtPort_ObjectIdentity = ObjectIdentity
cienaCesInetMgmtPort = _CienaCesInetMgmtPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 5)
)


class _CienaCesInetMgmtPortInterface_Type(Integer32):
    """Custom type cienaCesInetMgmtPortInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_CienaCesInetMgmtPortInterface_Type.__name__ = "Integer32"
_CienaCesInetMgmtPortInterface_Object = MibScalar
cienaCesInetMgmtPortInterface = _CienaCesInetMgmtPortInterface_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 1, 1, 5, 1),
    _CienaCesInetMgmtPortInterface_Type()
)
cienaCesInetMgmtPortInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesInetMgmtPortInterface.setStatus("current")
_CienaCesMgmtInterfaceMIBConformance_ObjectIdentity = ObjectIdentity
cienaCesMgmtInterfaceMIBConformance = _CienaCesMgmtInterfaceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 3)
)
_CienaCesMgmtInterfaceMIBCompliances_ObjectIdentity = ObjectIdentity
cienaCesMgmtInterfaceMIBCompliances = _CienaCesMgmtInterfaceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 3, 1)
)
_CienaCesMgmtInterfaceMIBGroups_ObjectIdentity = ObjectIdentity
cienaCesMgmtInterfaceMIBGroups = _CienaCesMgmtInterfaceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 27, 3, 2)
)
_CienaCesMgmtInterfaceMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesMgmtInterfaceMIBNotificationPrefix = _CienaCesMgmtInterfaceMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 27)
)
_CienaCesMgmtInterfaceMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesMgmtInterfaceMIBNotifications = _CienaCesMgmtInterfaceMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 27, 0)
)

# Managed Objects groups


# Notification objects

cienaCesInetMgmtAddrChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 27, 0, 1)
)
cienaCesInetMgmtAddrChangeNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MGMT-INTERFACE-MIB", "cienaCesInetMgmtInterfaceNotifIndex"),
        ("CIENA-CES-MGMT-INTERFACE-MIB", "cienaCesInetMgmtInterfaceNotifAddrType"),
        ("CIENA-CES-MGMT-INTERFACE-MIB", "cienaCesInetMgmtInterfaceNotifAddr"),
        ("CIENA-CES-MGMT-INTERFACE-MIB", "cienaCesInetMgmtInterfaceAddrPrefixLength"),
        ("CIENA-CES-MGMT-INTERFACE-MIB", "cienaCesInetMgmtInterfaceName"))
)
if mibBuilder.loadTexts:
    cienaCesInetMgmtAddrChangeNotification.setStatus(
        "current"
    )

cienaCesInetMgmtAddrAddedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 27, 0, 2)
)
cienaCesInetMgmtAddrAddedNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MGMT-INTERFACE-MIB", "cienaCesInetMgmtInterfaceNotifIndex"),
        ("CIENA-CES-MGMT-INTERFACE-MIB", "cienaCesInetMgmtInterfaceNotifAddrType"),
        ("CIENA-CES-MGMT-INTERFACE-MIB", "cienaCesInetMgmtInterfaceNotifAddr"),
        ("CIENA-CES-MGMT-INTERFACE-MIB", "cienaCesInetMgmtInterfaceAddrPrefixLength"),
        ("CIENA-CES-MGMT-INTERFACE-MIB", "cienaCesInetMgmtInterfaceName"))
)
if mibBuilder.loadTexts:
    cienaCesInetMgmtAddrAddedNotification.setStatus(
        "current"
    )

cienaCesInetMgmtAddrRemovedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 27, 0, 3)
)
cienaCesInetMgmtAddrRemovedNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MGMT-INTERFACE-MIB", "cienaCesInetMgmtInterfaceNotifIndex"),
        ("CIENA-CES-MGMT-INTERFACE-MIB", "cienaCesInetMgmtInterfaceNotifAddrType"),
        ("CIENA-CES-MGMT-INTERFACE-MIB", "cienaCesInetMgmtInterfaceNotifAddr"),
        ("CIENA-CES-MGMT-INTERFACE-MIB", "cienaCesInetMgmtInterfaceAddrPrefixLength"),
        ("CIENA-CES-MGMT-INTERFACE-MIB", "cienaCesInetMgmtInterfaceName"))
)
if mibBuilder.loadTexts:
    cienaCesInetMgmtAddrRemovedNotification.setStatus(
        "current"
    )

cienaCesInetGatewayAddrChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 27, 0, 4)
)
cienaCesInetGatewayAddrChangeNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MGMT-INTERFACE-MIB", "cienaCesInetGatewayNotifAddrType"),
        ("CIENA-CES-MGMT-INTERFACE-MIB", "cienaCesInetGatewayNotifAddr"))
)
if mibBuilder.loadTexts:
    cienaCesInetGatewayAddrChangeNotification.setStatus(
        "current"
    )

cienaCesInetGatewayAddedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 27, 0, 5)
)
cienaCesInetGatewayAddedNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MGMT-INTERFACE-MIB", "cienaCesInetGatewayNotifAddrType"),
        ("CIENA-CES-MGMT-INTERFACE-MIB", "cienaCesInetGatewayNotifAddr"))
)
if mibBuilder.loadTexts:
    cienaCesInetGatewayAddedNotification.setStatus(
        "current"
    )

cienaCesInetGatewayRemovedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 27, 0, 6)
)
cienaCesInetGatewayRemovedNotification.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-MGMT-INTERFACE-MIB", "cienaCesInetGatewayNotifAddrType"),
        ("CIENA-CES-MGMT-INTERFACE-MIB", "cienaCesInetGatewayNotifAddr"))
)
if mibBuilder.loadTexts:
    cienaCesInetGatewayRemovedNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-MGMT-INTERFACE-MIB",
    **{"cienaCesMgmtInterfaceMIB": cienaCesMgmtInterfaceMIB,
       "cienaCesMgmtInterfaceMIBObjects": cienaCesMgmtInterfaceMIBObjects,
       "cienaCesMgmtInterface": cienaCesMgmtInterface,
       "cienaCesInetMgmtInterfaceTable": cienaCesInetMgmtInterfaceTable,
       "cienaCesInetMgmtInterfaceEntry": cienaCesInetMgmtInterfaceEntry,
       "cienaCesInetMgmtInterfaceIndex": cienaCesInetMgmtInterfaceIndex,
       "cienaCesInetMgmtInterfaceAddrType": cienaCesInetMgmtInterfaceAddrType,
       "cienaCesInetMgmtInterfaceAddr": cienaCesInetMgmtInterfaceAddr,
       "cienaCesInetMgmtInterfaceAddrPrefixLength": cienaCesInetMgmtInterfaceAddrPrefixLength,
       "cienaCesInetMgmtInterfaceName": cienaCesInetMgmtInterfaceName,
       "cienaCesInetMgmtInterfaceAdminState": cienaCesInetMgmtInterfaceAdminState,
       "cienaCesInetMgmtInterfaceOperState": cienaCesInetMgmtInterfaceOperState,
       "cienaCesInetMgmtInterfaceDomain": cienaCesInetMgmtInterfaceDomain,
       "cienaCesInetMgmtInterfaceDomainId": cienaCesInetMgmtInterfaceDomainId,
       "cienaCesInetMgmtInterfacePktPriority": cienaCesInetMgmtInterfacePktPriority,
       "cienaCesInetMgmtInterfaceMtu": cienaCesInetMgmtInterfaceMtu,
       "cienaCesInetMgmtInterfaceNotifIndex": cienaCesInetMgmtInterfaceNotifIndex,
       "cienaCesInetMgmtInterfaceNotifAddrType": cienaCesInetMgmtInterfaceNotifAddrType,
       "cienaCesInetMgmtInterfaceNotifAddr": cienaCesInetMgmtInterfaceNotifAddr,
       "cienaCesInetMgmtInterfaceDomainVsName": cienaCesInetMgmtInterfaceDomainVsName,
       "cienaCesInetMgmtInterfaceIngressAclProfId": cienaCesInetMgmtInterfaceIngressAclProfId,
       "cienaCesInetGatewayTable": cienaCesInetGatewayTable,
       "cienaCesInetGatewayEntry": cienaCesInetGatewayEntry,
       "cienaCesInetGatewayAddrType": cienaCesInetGatewayAddrType,
       "cienaCesInetGatewayAddr": cienaCesInetGatewayAddr,
       "cienaCesInetGatewaySource": cienaCesInetGatewaySource,
       "cienaCesInetGatewayOperState": cienaCesInetGatewayOperState,
       "cienaCesInetGatewayNotifAddrType": cienaCesInetGatewayNotifAddrType,
       "cienaCesInetGatewayNotifAddr": cienaCesInetGatewayNotifAddr,
       "cienaCesInetStackTable": cienaCesInetStackTable,
       "cienaCesInetStackEntry": cienaCesInetStackEntry,
       "cienaCesInetAddrType": cienaCesInetAddrType,
       "cienaCesInetForwardingState": cienaCesInetForwardingState,
       "cienaCesInetDefaultDscp": cienaCesInetDefaultDscp,
       "cienaCesInetIcmpAcceptRedirects": cienaCesInetIcmpAcceptRedirects,
       "cienaCesInetIcmpEchoIgnoreBroadcasts": cienaCesInetIcmpEchoIgnoreBroadcasts,
       "cienaCesInetIcmpPortUnreachable": cienaCesInetIcmpPortUnreachable,
       "cienaCesInetTcpStack": cienaCesInetTcpStack,
       "cienaCesInetTcpTimestamps": cienaCesInetTcpTimestamps,
       "cienaCesInetMgmtPort": cienaCesInetMgmtPort,
       "cienaCesInetMgmtPortInterface": cienaCesInetMgmtPortInterface,
       "cienaCesMgmtInterfaceMIBConformance": cienaCesMgmtInterfaceMIBConformance,
       "cienaCesMgmtInterfaceMIBCompliances": cienaCesMgmtInterfaceMIBCompliances,
       "cienaCesMgmtInterfaceMIBGroups": cienaCesMgmtInterfaceMIBGroups,
       "cienaCesMgmtInterfaceMIBNotificationPrefix": cienaCesMgmtInterfaceMIBNotificationPrefix,
       "cienaCesMgmtInterfaceMIBNotifications": cienaCesMgmtInterfaceMIBNotifications,
       "cienaCesInetMgmtAddrChangeNotification": cienaCesInetMgmtAddrChangeNotification,
       "cienaCesInetMgmtAddrAddedNotification": cienaCesInetMgmtAddrAddedNotification,
       "cienaCesInetMgmtAddrRemovedNotification": cienaCesInetMgmtAddrRemovedNotification,
       "cienaCesInetGatewayAddrChangeNotification": cienaCesInetGatewayAddrChangeNotification,
       "cienaCesInetGatewayAddedNotification": cienaCesInetGatewayAddedNotification,
       "cienaCesInetGatewayRemovedNotification": cienaCesInetGatewayRemovedNotification}
)
