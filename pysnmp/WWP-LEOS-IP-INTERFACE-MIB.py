# SNMP MIB module (WWP-LEOS-IP-INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-IP-INTERFACE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:54 2024
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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosIpInterfaceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24)
)
wwpLeosIpInterfaceMIB.setRevisions(
        ("2008-05-14 00:00",
         "2003-05-02 00:00",
         "2001-04-03 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



# MIB Managed Objects in the order of their OIDs

_WwpLeosIpInterfaceMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosIpInterfaceMIBObjects = _WwpLeosIpInterfaceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1)
)
_WwpLeosIpInterface_ObjectIdentity = ObjectIdentity
wwpLeosIpInterface = _WwpLeosIpInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1)
)
_WwpLeosIpInterfaceTable_Object = MibTable
wwpLeosIpInterfaceTable = _WwpLeosIpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wwpLeosIpInterfaceTable.setStatus("current")
_WwpLeosIpInterfaceEntry_Object = MibTableRow
wwpLeosIpInterfaceEntry = _WwpLeosIpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 1, 1)
)
wwpLeosIpInterfaceEntry.setIndexNames(
    (0, "WWP-LEOS-IP-INTERFACE-MIB", "wwpLeosIpInterfaceIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosIpInterfaceEntry.setStatus("current")


class _WwpLeosIpInterfaceIndex_Type(Integer32):
    """Custom type wwpLeosIpInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_WwpLeosIpInterfaceIndex_Type.__name__ = "Integer32"
_WwpLeosIpInterfaceIndex_Object = MibTableColumn
wwpLeosIpInterfaceIndex = _WwpLeosIpInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 1, 1, 1),
    _WwpLeosIpInterfaceIndex_Type()
)
wwpLeosIpInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosIpInterfaceIndex.setStatus("current")


class _WwpLeosIpInterfaceName_Type(DisplayString):
    """Custom type wwpLeosIpInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WwpLeosIpInterfaceName_Type.__name__ = "DisplayString"
_WwpLeosIpInterfaceName_Object = MibTableColumn
wwpLeosIpInterfaceName = _WwpLeosIpInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 1, 1, 2),
    _WwpLeosIpInterfaceName_Type()
)
wwpLeosIpInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosIpInterfaceName.setStatus("current")
_WwpLeosIpInterfaceIpAddr_Type = IpAddress
_WwpLeosIpInterfaceIpAddr_Object = MibTableColumn
wwpLeosIpInterfaceIpAddr = _WwpLeosIpInterfaceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 1, 1, 3),
    _WwpLeosIpInterfaceIpAddr_Type()
)
wwpLeosIpInterfaceIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosIpInterfaceIpAddr.setStatus("current")
_WwpLeosIpInterfaceSubnet_Type = IpAddress
_WwpLeosIpInterfaceSubnet_Object = MibTableColumn
wwpLeosIpInterfaceSubnet = _WwpLeosIpInterfaceSubnet_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 1, 1, 4),
    _WwpLeosIpInterfaceSubnet_Type()
)
wwpLeosIpInterfaceSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosIpInterfaceSubnet.setStatus("current")


class _WwpLeosIpInterfaceIfIndexXref_Type(Integer32):
    """Custom type wwpLeosIpInterfaceIfIndexXref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_WwpLeosIpInterfaceIfIndexXref_Type.__name__ = "Integer32"
_WwpLeosIpInterfaceIfIndexXref_Object = MibTableColumn
wwpLeosIpInterfaceIfIndexXref = _WwpLeosIpInterfaceIfIndexXref_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 1, 1, 5),
    _WwpLeosIpInterfaceIfIndexXref_Type()
)
wwpLeosIpInterfaceIfIndexXref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosIpInterfaceIfIndexXref.setStatus("current")
_WwpLeosIpExtInterfaceTable_Object = MibTable
wwpLeosIpExtInterfaceTable = _WwpLeosIpExtInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wwpLeosIpExtInterfaceTable.setStatus("current")
_WwpLeosIpExtInterfaceEntry_Object = MibTableRow
wwpLeosIpExtInterfaceEntry = _WwpLeosIpExtInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wwpLeosIpExtInterfaceEntry.setStatus("current")
_WwpLeosIpInterfaceEnable_Type = TruthValue
_WwpLeosIpInterfaceEnable_Object = MibTableColumn
wwpLeosIpInterfaceEnable = _WwpLeosIpInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 2, 1, 1),
    _WwpLeosIpInterfaceEnable_Type()
)
wwpLeosIpInterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosIpInterfaceEnable.setStatus("current")
_WwpLeosIpInterfaceVlanId_Type = VlanId
_WwpLeosIpInterfaceVlanId_Object = MibTableColumn
wwpLeosIpInterfaceVlanId = _WwpLeosIpInterfaceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 2, 1, 2),
    _WwpLeosIpInterfaceVlanId_Type()
)
wwpLeosIpInterfaceVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosIpInterfaceVlanId.setStatus("current")


class _WwpLeosIpInterfaceMgmtPktPriority_Type(Integer32):
    """Custom type wwpLeosIpInterfaceMgmtPktPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosIpInterfaceMgmtPktPriority_Type.__name__ = "Integer32"
_WwpLeosIpInterfaceMgmtPktPriority_Object = MibTableColumn
wwpLeosIpInterfaceMgmtPktPriority = _WwpLeosIpInterfaceMgmtPktPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 2, 1, 3),
    _WwpLeosIpInterfaceMgmtPktPriority_Type()
)
wwpLeosIpInterfaceMgmtPktPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosIpInterfaceMgmtPktPriority.setStatus("current")


class _WwpLeosIpInterfaceAddrNotifEnabled_Type(TruthValue):
    """Custom type wwpLeosIpInterfaceAddrNotifEnabled based on TruthValue"""


_WwpLeosIpInterfaceAddrNotifEnabled_Object = MibScalar
wwpLeosIpInterfaceAddrNotifEnabled = _WwpLeosIpInterfaceAddrNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 3),
    _WwpLeosIpInterfaceAddrNotifEnabled_Type()
)
wwpLeosIpInterfaceAddrNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosIpInterfaceAddrNotifEnabled.setStatus("current")
_WwpLeosIpDataInterfaceTable_Object = MibTable
wwpLeosIpDataInterfaceTable = _WwpLeosIpDataInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 4)
)
if mibBuilder.loadTexts:
    wwpLeosIpDataInterfaceTable.setStatus("current")
_WwpLeosIpDataInterfaceEntry_Object = MibTableRow
wwpLeosIpDataInterfaceEntry = _WwpLeosIpDataInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 4, 1)
)
wwpLeosIpDataInterfaceEntry.setIndexNames(
    (0, "WWP-LEOS-IP-INTERFACE-MIB", "wwpLeosIpDataInterfaceIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosIpDataInterfaceEntry.setStatus("current")


class _WwpLeosIpDataInterfaceIndex_Type(Integer32):
    """Custom type wwpLeosIpDataInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_WwpLeosIpDataInterfaceIndex_Type.__name__ = "Integer32"
_WwpLeosIpDataInterfaceIndex_Object = MibTableColumn
wwpLeosIpDataInterfaceIndex = _WwpLeosIpDataInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 4, 1, 1),
    _WwpLeosIpDataInterfaceIndex_Type()
)
wwpLeosIpDataInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosIpDataInterfaceIndex.setStatus("current")


class _WwpLeosIpDataInterfaceName_Type(DisplayString):
    """Custom type wwpLeosIpDataInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_WwpLeosIpDataInterfaceName_Type.__name__ = "DisplayString"
_WwpLeosIpDataInterfaceName_Object = MibTableColumn
wwpLeosIpDataInterfaceName = _WwpLeosIpDataInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 4, 1, 2),
    _WwpLeosIpDataInterfaceName_Type()
)
wwpLeosIpDataInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosIpDataInterfaceName.setStatus("current")
_WwpLeosIpDataInterfaceIpAddr_Type = IpAddress
_WwpLeosIpDataInterfaceIpAddr_Object = MibTableColumn
wwpLeosIpDataInterfaceIpAddr = _WwpLeosIpDataInterfaceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 4, 1, 3),
    _WwpLeosIpDataInterfaceIpAddr_Type()
)
wwpLeosIpDataInterfaceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosIpDataInterfaceIpAddr.setStatus("current")
_WwpLeosIpDataInterfaceMask_Type = IpAddress
_WwpLeosIpDataInterfaceMask_Object = MibTableColumn
wwpLeosIpDataInterfaceMask = _WwpLeosIpDataInterfaceMask_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 4, 1, 4),
    _WwpLeosIpDataInterfaceMask_Type()
)
wwpLeosIpDataInterfaceMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosIpDataInterfaceMask.setStatus("current")
_WwpLeosIpDataInterfaceVlanId_Type = VlanId
_WwpLeosIpDataInterfaceVlanId_Object = MibTableColumn
wwpLeosIpDataInterfaceVlanId = _WwpLeosIpDataInterfaceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 4, 1, 5),
    _WwpLeosIpDataInterfaceVlanId_Type()
)
wwpLeosIpDataInterfaceVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosIpDataInterfaceVlanId.setStatus("current")


class _WwpLeosIpDataInterfaceType_Type(Integer32):
    """Custom type wwpLeosIpDataInterfaceType based on Integer32"""
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
          ("loopBack", 3),
          ("pointToPoint", 2))
    )


_WwpLeosIpDataInterfaceType_Type.__name__ = "Integer32"
_WwpLeosIpDataInterfaceType_Object = MibTableColumn
wwpLeosIpDataInterfaceType = _WwpLeosIpDataInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 4, 1, 6),
    _WwpLeosIpDataInterfaceType_Type()
)
wwpLeosIpDataInterfaceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosIpDataInterfaceType.setStatus("current")
_WwpLeosIpDataInterfaceIfIndex_Type = Integer32
_WwpLeosIpDataInterfaceIfIndex_Object = MibTableColumn
wwpLeosIpDataInterfaceIfIndex = _WwpLeosIpDataInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 4, 1, 7),
    _WwpLeosIpDataInterfaceIfIndex_Type()
)
wwpLeosIpDataInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosIpDataInterfaceIfIndex.setStatus("current")
_WwpLeosIpDataInterfaceMac_Type = MacAddress
_WwpLeosIpDataInterfaceMac_Object = MibTableColumn
wwpLeosIpDataInterfaceMac = _WwpLeosIpDataInterfaceMac_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 4, 1, 8),
    _WwpLeosIpDataInterfaceMac_Type()
)
wwpLeosIpDataInterfaceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosIpDataInterfaceMac.setStatus("current")


class _WwpLeosIpDataInterfaceIfMtu_Type(Integer32):
    """Custom type wwpLeosIpDataInterfaceIfMtu based on Integer32"""
    defaultValue = 1500


_WwpLeosIpDataInterfaceIfMtu_Object = MibTableColumn
wwpLeosIpDataInterfaceIfMtu = _WwpLeosIpDataInterfaceIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 4, 1, 9),
    _WwpLeosIpDataInterfaceIfMtu_Type()
)
wwpLeosIpDataInterfaceIfMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosIpDataInterfaceIfMtu.setStatus("current")
_WwpLeosIpDataInterfaceRowStatus_Type = RowStatus
_WwpLeosIpDataInterfaceRowStatus_Object = MibTableColumn
wwpLeosIpDataInterfaceRowStatus = _WwpLeosIpDataInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 4, 1, 10),
    _WwpLeosIpDataInterfaceRowStatus_Type()
)
wwpLeosIpDataInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosIpDataInterfaceRowStatus.setStatus("current")
_WwpLeosIpInterfaceOperationalGateway_Type = IpAddress
_WwpLeosIpInterfaceOperationalGateway_Object = MibScalar
wwpLeosIpInterfaceOperationalGateway = _WwpLeosIpInterfaceOperationalGateway_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 1, 5),
    _WwpLeosIpInterfaceOperationalGateway_Type()
)
wwpLeosIpInterfaceOperationalGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosIpInterfaceOperationalGateway.setStatus("current")
_WwpLeosIpAclGlobal_ObjectIdentity = ObjectIdentity
wwpLeosIpAclGlobal = _WwpLeosIpAclGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 2)
)


class _WwpLeosIpAclState_Type(Integer32):
    """Custom type wwpLeosIpAclState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosIpAclState_Type.__name__ = "Integer32"
_WwpLeosIpAclState_Object = MibScalar
wwpLeosIpAclState = _WwpLeosIpAclState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 2, 1),
    _WwpLeosIpAclState_Type()
)
wwpLeosIpAclState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosIpAclState.setStatus("current")
_WwpLeosIpAclCacheHit_Type = Counter32
_WwpLeosIpAclCacheHit_Object = MibScalar
wwpLeosIpAclCacheHit = _WwpLeosIpAclCacheHit_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 2, 2),
    _WwpLeosIpAclCacheHit_Type()
)
wwpLeosIpAclCacheHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosIpAclCacheHit.setStatus("current")
_WwpLeosIpAclNoHit_Type = Counter32
_WwpLeosIpAclNoHit_Object = MibScalar
wwpLeosIpAclNoHit = _WwpLeosIpAclNoHit_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 2, 3),
    _WwpLeosIpAclNoHit_Type()
)
wwpLeosIpAclNoHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosIpAclNoHit.setStatus("current")
_WwpLeosIpAclBadPort_Type = Counter32
_WwpLeosIpAclBadPort_Object = MibScalar
wwpLeosIpAclBadPort = _WwpLeosIpAclBadPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 2, 4),
    _WwpLeosIpAclBadPort_Type()
)
wwpLeosIpAclBadPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosIpAclBadPort.setStatus("current")
_WwpLeosIpAclClearStats_Type = RowStatus
_WwpLeosIpAclClearStats_Object = MibScalar
wwpLeosIpAclClearStats = _WwpLeosIpAclClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 2, 5),
    _WwpLeosIpAclClearStats_Type()
)
wwpLeosIpAclClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosIpAclClearStats.setStatus("current")
_WwpLeosIpAclBadDscp_Type = Counter32
_WwpLeosIpAclBadDscp_Object = MibScalar
wwpLeosIpAclBadDscp = _WwpLeosIpAclBadDscp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 2, 6),
    _WwpLeosIpAclBadDscp_Type()
)
wwpLeosIpAclBadDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosIpAclBadDscp.setStatus("current")


class _WwpLeosIpAclOperState_Type(Integer32):
    """Custom type wwpLeosIpAclOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosIpAclOperState_Type.__name__ = "Integer32"
_WwpLeosIpAclOperState_Object = MibScalar
wwpLeosIpAclOperState = _WwpLeosIpAclOperState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 2, 7),
    _WwpLeosIpAclOperState_Type()
)
wwpLeosIpAclOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosIpAclOperState.setStatus("current")
_WwpLeosIpAclInUseEntries_Type = Counter32
_WwpLeosIpAclInUseEntries_Object = MibScalar
wwpLeosIpAclInUseEntries = _WwpLeosIpAclInUseEntries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 2, 8),
    _WwpLeosIpAclInUseEntries_Type()
)
wwpLeosIpAclInUseEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosIpAclInUseEntries.setStatus("current")
_WwpLeosIpAclMaxEntries_Type = Counter32
_WwpLeosIpAclMaxEntries_Object = MibScalar
wwpLeosIpAclMaxEntries = _WwpLeosIpAclMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 2, 9),
    _WwpLeosIpAclMaxEntries_Type()
)
wwpLeosIpAclMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosIpAclMaxEntries.setStatus("current")
_WwpLeosIpAclRules_ObjectIdentity = ObjectIdentity
wwpLeosIpAclRules = _WwpLeosIpAclRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 3)
)
_WwpLeosIpAclTable_Object = MibTable
wwpLeosIpAclTable = _WwpLeosIpAclTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 3, 1)
)
if mibBuilder.loadTexts:
    wwpLeosIpAclTable.setStatus("current")
_WwpLeosIpAclEntry_Object = MibTableRow
wwpLeosIpAclEntry = _WwpLeosIpAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 3, 1, 1)
)
wwpLeosIpAclEntry.setIndexNames(
    (0, "WWP-LEOS-IP-INTERFACE-MIB", "wwpLeosIpAclEntryIpAddr"),
    (0, "WWP-LEOS-IP-INTERFACE-MIB", "wwpLeosIpAclEntryIpMask"),
)
if mibBuilder.loadTexts:
    wwpLeosIpAclEntry.setStatus("current")
_WwpLeosIpAclEntryIpAddr_Type = IpAddress
_WwpLeosIpAclEntryIpAddr_Object = MibTableColumn
wwpLeosIpAclEntryIpAddr = _WwpLeosIpAclEntryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 3, 1, 1, 1),
    _WwpLeosIpAclEntryIpAddr_Type()
)
wwpLeosIpAclEntryIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosIpAclEntryIpAddr.setStatus("current")
_WwpLeosIpAclEntryIpMask_Type = IpAddress
_WwpLeosIpAclEntryIpMask_Object = MibTableColumn
wwpLeosIpAclEntryIpMask = _WwpLeosIpAclEntryIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 3, 1, 1, 2),
    _WwpLeosIpAclEntryIpMask_Type()
)
wwpLeosIpAclEntryIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosIpAclEntryIpMask.setStatus("current")
_WwpLeosIpAclEntryPortMask_Type = Unsigned32
_WwpLeosIpAclEntryPortMask_Object = MibTableColumn
wwpLeosIpAclEntryPortMask = _WwpLeosIpAclEntryPortMask_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 3, 1, 1, 3),
    _WwpLeosIpAclEntryPortMask_Type()
)
wwpLeosIpAclEntryPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosIpAclEntryPortMask.setStatus("deprecated")
_WwpLeosIpAclEntryHits_Type = Counter32
_WwpLeosIpAclEntryHits_Object = MibTableColumn
wwpLeosIpAclEntryHits = _WwpLeosIpAclEntryHits_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 3, 1, 1, 4),
    _WwpLeosIpAclEntryHits_Type()
)
wwpLeosIpAclEntryHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosIpAclEntryHits.setStatus("current")
_WwpLeosIpAclEntryBadPort_Type = Counter32
_WwpLeosIpAclEntryBadPort_Object = MibTableColumn
wwpLeosIpAclEntryBadPort = _WwpLeosIpAclEntryBadPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 3, 1, 1, 5),
    _WwpLeosIpAclEntryBadPort_Type()
)
wwpLeosIpAclEntryBadPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosIpAclEntryBadPort.setStatus("current")
_WwpLeosIpAclEntryStatus_Type = RowStatus
_WwpLeosIpAclEntryStatus_Object = MibTableColumn
wwpLeosIpAclEntryStatus = _WwpLeosIpAclEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 3, 1, 1, 6),
    _WwpLeosIpAclEntryStatus_Type()
)
wwpLeosIpAclEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosIpAclEntryStatus.setStatus("current")


class _WwpLeosIpAclEntryDscpMask_Type(OctetString):
    """Custom type wwpLeosIpAclEntryDscpMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_WwpLeosIpAclEntryDscpMask_Type.__name__ = "OctetString"
_WwpLeosIpAclEntryDscpMask_Object = MibTableColumn
wwpLeosIpAclEntryDscpMask = _WwpLeosIpAclEntryDscpMask_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 3, 1, 1, 7),
    _WwpLeosIpAclEntryDscpMask_Type()
)
wwpLeosIpAclEntryDscpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosIpAclEntryDscpMask.setStatus("current")
_WwpLeosIpAclEntryBadDscp_Type = Counter32
_WwpLeosIpAclEntryBadDscp_Object = MibTableColumn
wwpLeosIpAclEntryBadDscp = _WwpLeosIpAclEntryBadDscp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 3, 1, 1, 8),
    _WwpLeosIpAclEntryBadDscp_Type()
)
wwpLeosIpAclEntryBadDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosIpAclEntryBadDscp.setStatus("current")


class _WwpLeosIpAclEntryPortBitMask_Type(OctetString):
    """Custom type wwpLeosIpAclEntryPortBitMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_WwpLeosIpAclEntryPortBitMask_Type.__name__ = "OctetString"
_WwpLeosIpAclEntryPortBitMask_Object = MibTableColumn
wwpLeosIpAclEntryPortBitMask = _WwpLeosIpAclEntryPortBitMask_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 1, 3, 1, 1, 9),
    _WwpLeosIpAclEntryPortBitMask_Type()
)
wwpLeosIpAclEntryPortBitMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosIpAclEntryPortBitMask.setStatus("current")
_WwpLeosIpInterfaceMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosIpInterfaceMIBNotificationPrefix = _WwpLeosIpInterfaceMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 2)
)
_WwpLeosIpInterfaceMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLeosIpInterfaceMIBNotifications = _WwpLeosIpInterfaceMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 2, 0)
)
_WwpLeosIpInterfaceMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosIpInterfaceMIBConformance = _WwpLeosIpInterfaceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 3)
)
_WwpLeosIpInterfaceMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosIpInterfaceMIBCompliances = _WwpLeosIpInterfaceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 3, 1)
)
_WwpLeosIpInterfaceMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosIpInterfaceMIBGroups = _WwpLeosIpInterfaceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 3, 2)
)
wwpLeosIpInterfaceEntry.registerAugmentions(
    ("WWP-LEOS-IP-INTERFACE-MIB",
     "wwpLeosIpExtInterfaceEntry")
)
wwpLeosIpExtInterfaceEntry.setIndexNames(*wwpLeosIpInterfaceEntry.getIndexNames())

# Managed Objects groups


# Notification objects

wwpLeosIpInterfaceAddrChgNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 2, 0, 1)
)
wwpLeosIpInterfaceAddrChgNotification.setObjects(
      *(("WWP-LEOS-IP-INTERFACE-MIB", "wwpLeosIpInterfaceName"),
        ("WWP-LEOS-IP-INTERFACE-MIB", "wwpLeosIpInterfaceIpAddr"),
        ("WWP-LEOS-IP-INTERFACE-MIB", "wwpLeosIpInterfaceSubnet"))
)
if mibBuilder.loadTexts:
    wwpLeosIpInterfaceAddrChgNotification.setStatus(
        "current"
    )

wwpLeosIpInterfaceOperationalGatewayChgNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 24, 2, 0, 2)
)
wwpLeosIpInterfaceOperationalGatewayChgNotification.setObjects(
    ("WWP-LEOS-IP-INTERFACE-MIB", "wwpLeosIpInterfaceOperationalGateway")
)
if mibBuilder.loadTexts:
    wwpLeosIpInterfaceOperationalGatewayChgNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-IP-INTERFACE-MIB",
    **{"VlanId": VlanId,
       "wwpLeosIpInterfaceMIB": wwpLeosIpInterfaceMIB,
       "wwpLeosIpInterfaceMIBObjects": wwpLeosIpInterfaceMIBObjects,
       "wwpLeosIpInterface": wwpLeosIpInterface,
       "wwpLeosIpInterfaceTable": wwpLeosIpInterfaceTable,
       "wwpLeosIpInterfaceEntry": wwpLeosIpInterfaceEntry,
       "wwpLeosIpInterfaceIndex": wwpLeosIpInterfaceIndex,
       "wwpLeosIpInterfaceName": wwpLeosIpInterfaceName,
       "wwpLeosIpInterfaceIpAddr": wwpLeosIpInterfaceIpAddr,
       "wwpLeosIpInterfaceSubnet": wwpLeosIpInterfaceSubnet,
       "wwpLeosIpInterfaceIfIndexXref": wwpLeosIpInterfaceIfIndexXref,
       "wwpLeosIpExtInterfaceTable": wwpLeosIpExtInterfaceTable,
       "wwpLeosIpExtInterfaceEntry": wwpLeosIpExtInterfaceEntry,
       "wwpLeosIpInterfaceEnable": wwpLeosIpInterfaceEnable,
       "wwpLeosIpInterfaceVlanId": wwpLeosIpInterfaceVlanId,
       "wwpLeosIpInterfaceMgmtPktPriority": wwpLeosIpInterfaceMgmtPktPriority,
       "wwpLeosIpInterfaceAddrNotifEnabled": wwpLeosIpInterfaceAddrNotifEnabled,
       "wwpLeosIpDataInterfaceTable": wwpLeosIpDataInterfaceTable,
       "wwpLeosIpDataInterfaceEntry": wwpLeosIpDataInterfaceEntry,
       "wwpLeosIpDataInterfaceIndex": wwpLeosIpDataInterfaceIndex,
       "wwpLeosIpDataInterfaceName": wwpLeosIpDataInterfaceName,
       "wwpLeosIpDataInterfaceIpAddr": wwpLeosIpDataInterfaceIpAddr,
       "wwpLeosIpDataInterfaceMask": wwpLeosIpDataInterfaceMask,
       "wwpLeosIpDataInterfaceVlanId": wwpLeosIpDataInterfaceVlanId,
       "wwpLeosIpDataInterfaceType": wwpLeosIpDataInterfaceType,
       "wwpLeosIpDataInterfaceIfIndex": wwpLeosIpDataInterfaceIfIndex,
       "wwpLeosIpDataInterfaceMac": wwpLeosIpDataInterfaceMac,
       "wwpLeosIpDataInterfaceIfMtu": wwpLeosIpDataInterfaceIfMtu,
       "wwpLeosIpDataInterfaceRowStatus": wwpLeosIpDataInterfaceRowStatus,
       "wwpLeosIpInterfaceOperationalGateway": wwpLeosIpInterfaceOperationalGateway,
       "wwpLeosIpAclGlobal": wwpLeosIpAclGlobal,
       "wwpLeosIpAclState": wwpLeosIpAclState,
       "wwpLeosIpAclCacheHit": wwpLeosIpAclCacheHit,
       "wwpLeosIpAclNoHit": wwpLeosIpAclNoHit,
       "wwpLeosIpAclBadPort": wwpLeosIpAclBadPort,
       "wwpLeosIpAclClearStats": wwpLeosIpAclClearStats,
       "wwpLeosIpAclBadDscp": wwpLeosIpAclBadDscp,
       "wwpLeosIpAclOperState": wwpLeosIpAclOperState,
       "wwpLeosIpAclInUseEntries": wwpLeosIpAclInUseEntries,
       "wwpLeosIpAclMaxEntries": wwpLeosIpAclMaxEntries,
       "wwpLeosIpAclRules": wwpLeosIpAclRules,
       "wwpLeosIpAclTable": wwpLeosIpAclTable,
       "wwpLeosIpAclEntry": wwpLeosIpAclEntry,
       "wwpLeosIpAclEntryIpAddr": wwpLeosIpAclEntryIpAddr,
       "wwpLeosIpAclEntryIpMask": wwpLeosIpAclEntryIpMask,
       "wwpLeosIpAclEntryPortMask": wwpLeosIpAclEntryPortMask,
       "wwpLeosIpAclEntryHits": wwpLeosIpAclEntryHits,
       "wwpLeosIpAclEntryBadPort": wwpLeosIpAclEntryBadPort,
       "wwpLeosIpAclEntryStatus": wwpLeosIpAclEntryStatus,
       "wwpLeosIpAclEntryDscpMask": wwpLeosIpAclEntryDscpMask,
       "wwpLeosIpAclEntryBadDscp": wwpLeosIpAclEntryBadDscp,
       "wwpLeosIpAclEntryPortBitMask": wwpLeosIpAclEntryPortBitMask,
       "wwpLeosIpInterfaceMIBNotificationPrefix": wwpLeosIpInterfaceMIBNotificationPrefix,
       "wwpLeosIpInterfaceMIBNotifications": wwpLeosIpInterfaceMIBNotifications,
       "wwpLeosIpInterfaceAddrChgNotification": wwpLeosIpInterfaceAddrChgNotification,
       "wwpLeosIpInterfaceOperationalGatewayChgNotification": wwpLeosIpInterfaceOperationalGatewayChgNotification,
       "wwpLeosIpInterfaceMIBConformance": wwpLeosIpInterfaceMIBConformance,
       "wwpLeosIpInterfaceMIBCompliances": wwpLeosIpInterfaceMIBCompliances,
       "wwpLeosIpInterfaceMIBGroups": wwpLeosIpInterfaceMIBGroups}
)
