# SNMP MIB module (PDN-MGMT-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-MGMT-IP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:51 2024
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

(AtmVcIdentifier,
 AtmVpIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmVcIdentifier",
    "AtmVpIdentifier")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(pdn_interfaces,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-interfaces")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

pdnMgmtIpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdnMgmtIpConfObjects_ObjectIdentity = ObjectIdentity
pdnMgmtIpConfObjects = _PdnMgmtIpConfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1)
)
_PdnMgmtIpPortTable_Object = MibTable
pdnMgmtIpPortTable = _PdnMgmtIpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 1)
)
if mibBuilder.loadTexts:
    pdnMgmtIpPortTable.setStatus("current")
_PdnMgmtIpPortEntry_Object = MibTableRow
pdnMgmtIpPortEntry = _PdnMgmtIpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 1, 1)
)
pdnMgmtIpPortEntry.setIndexNames(
    (0, "PDN-MGMT-IP-MIB", "pdnMgmtIpPortIndex"),
)
if mibBuilder.loadTexts:
    pdnMgmtIpPortEntry.setStatus("current")
_PdnMgmtIpPortIndex_Type = InterfaceIndex
_PdnMgmtIpPortIndex_Object = MibTableColumn
pdnMgmtIpPortIndex = _PdnMgmtIpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 1, 1, 1),
    _PdnMgmtIpPortIndex_Type()
)
pdnMgmtIpPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnMgmtIpPortIndex.setStatus("current")
_PdnMgmtIpAddress_Type = IpAddress
_PdnMgmtIpAddress_Object = MibTableColumn
pdnMgmtIpAddress = _PdnMgmtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 1, 1, 2),
    _PdnMgmtIpAddress_Type()
)
pdnMgmtIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnMgmtIpAddress.setStatus("current")
_PdnMgmtIpNetMask_Type = IpAddress
_PdnMgmtIpNetMask_Object = MibTableColumn
pdnMgmtIpNetMask = _PdnMgmtIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 1, 1, 3),
    _PdnMgmtIpNetMask_Type()
)
pdnMgmtIpNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnMgmtIpNetMask.setStatus("current")
_PdnMgmtIpEthGateway_Type = IpAddress
_PdnMgmtIpEthGateway_Object = MibTableColumn
pdnMgmtIpEthGateway = _PdnMgmtIpEthGateway_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 1, 1, 4),
    _PdnMgmtIpEthGateway_Type()
)
pdnMgmtIpEthGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnMgmtIpEthGateway.setStatus("current")
_PdnMgmtIpPhysAddress_Type = PhysAddress
_PdnMgmtIpPhysAddress_Object = MibTableColumn
pdnMgmtIpPhysAddress = _PdnMgmtIpPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 1, 1, 5),
    _PdnMgmtIpPhysAddress_Type()
)
pdnMgmtIpPhysAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnMgmtIpPhysAddress.setStatus("current")


class _PdnMgmtIpConfigMode_Type(Integer32):
    """Custom type pdnMgmtIpConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 3),
          ("dhcp", 2),
          ("manual", 1))
    )


_PdnMgmtIpConfigMode_Type.__name__ = "Integer32"
_PdnMgmtIpConfigMode_Object = MibTableColumn
pdnMgmtIpConfigMode = _PdnMgmtIpConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 1, 1, 6),
    _PdnMgmtIpConfigMode_Type()
)
pdnMgmtIpConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnMgmtIpConfigMode.setStatus("current")
_PdnMgmtBootIfIndex_Type = InterfaceIndex
_PdnMgmtBootIfIndex_Object = MibTableColumn
pdnMgmtBootIfIndex = _PdnMgmtBootIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 1, 1, 7),
    _PdnMgmtBootIfIndex_Type()
)
pdnMgmtBootIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnMgmtBootIfIndex.setStatus("current")
_PdnMgmtBootVpi_Type = AtmVpIdentifier
_PdnMgmtBootVpi_Object = MibTableColumn
pdnMgmtBootVpi = _PdnMgmtBootVpi_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 1, 1, 8),
    _PdnMgmtBootVpi_Type()
)
pdnMgmtBootVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnMgmtBootVpi.setStatus("current")
_PdnMgmtBootVci_Type = AtmVcIdentifier
_PdnMgmtBootVci_Object = MibTableColumn
pdnMgmtBootVci = _PdnMgmtBootVci_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 1, 1, 9),
    _PdnMgmtBootVci_Type()
)
pdnMgmtBootVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnMgmtBootVci.setStatus("current")


class _PdnMgmtIpAdminStatus_Type(Integer32):
    """Custom type pdnMgmtIpAdminStatus based on Integer32"""
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


_PdnMgmtIpAdminStatus_Type.__name__ = "Integer32"
_PdnMgmtIpAdminStatus_Object = MibTableColumn
pdnMgmtIpAdminStatus = _PdnMgmtIpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 1, 1, 10),
    _PdnMgmtIpAdminStatus_Type()
)
pdnMgmtIpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnMgmtIpAdminStatus.setStatus("current")
_PdnMgmtAtmInvArpTable_Object = MibTable
pdnMgmtAtmInvArpTable = _PdnMgmtAtmInvArpTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 2)
)
if mibBuilder.loadTexts:
    pdnMgmtAtmInvArpTable.setStatus("current")
_PdnMgmtAtmInvArpEntry_Object = MibTableRow
pdnMgmtAtmInvArpEntry = _PdnMgmtAtmInvArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 2, 1)
)
pdnMgmtAtmInvArpEntry.setIndexNames(
    (0, "PDN-MGMT-IP-MIB", "pdnMgmtAtmIfIndex"),
    (0, "PDN-MGMT-IP-MIB", "pdnMgmtAtmVpi"),
    (0, "PDN-MGMT-IP-MIB", "pdnMgmtAtmVci"),
)
if mibBuilder.loadTexts:
    pdnMgmtAtmInvArpEntry.setStatus("current")
_PdnMgmtAtmIfIndex_Type = InterfaceIndex
_PdnMgmtAtmIfIndex_Object = MibTableColumn
pdnMgmtAtmIfIndex = _PdnMgmtAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 2, 1, 1),
    _PdnMgmtAtmIfIndex_Type()
)
pdnMgmtAtmIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnMgmtAtmIfIndex.setStatus("current")
_PdnMgmtAtmVpi_Type = AtmVpIdentifier
_PdnMgmtAtmVpi_Object = MibTableColumn
pdnMgmtAtmVpi = _PdnMgmtAtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 2, 1, 2),
    _PdnMgmtAtmVpi_Type()
)
pdnMgmtAtmVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnMgmtAtmVpi.setStatus("current")
_PdnMgmtAtmVci_Type = AtmVcIdentifier
_PdnMgmtAtmVci_Object = MibTableColumn
pdnMgmtAtmVci = _PdnMgmtAtmVci_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 2, 1, 3),
    _PdnMgmtAtmVci_Type()
)
pdnMgmtAtmVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnMgmtAtmVci.setStatus("current")
_PdnMgmtIpPortIfIndex_Type = InterfaceIndex
_PdnMgmtIpPortIfIndex_Object = MibTableColumn
pdnMgmtIpPortIfIndex = _PdnMgmtIpPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 2, 1, 4),
    _PdnMgmtIpPortIfIndex_Type()
)
pdnMgmtIpPortIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnMgmtIpPortIfIndex.setStatus("current")
_PdnMgmtNextHopIp_Type = IpAddress
_PdnMgmtNextHopIp_Object = MibTableColumn
pdnMgmtNextHopIp = _PdnMgmtNextHopIp_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 2, 1, 5),
    _PdnMgmtNextHopIp_Type()
)
pdnMgmtNextHopIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnMgmtNextHopIp.setStatus("current")
_PdnMgmtAtmInvArpRowStatus_Type = RowStatus
_PdnMgmtAtmInvArpRowStatus_Object = MibTableColumn
pdnMgmtAtmInvArpRowStatus = _PdnMgmtAtmInvArpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 2, 1, 6),
    _PdnMgmtAtmInvArpRowStatus_Type()
)
pdnMgmtAtmInvArpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnMgmtAtmInvArpRowStatus.setStatus("current")
_PdnMgmtIpDefaultRouter_Type = IpAddress
_PdnMgmtIpDefaultRouter_Object = MibScalar
pdnMgmtIpDefaultRouter = _PdnMgmtIpDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 1, 3),
    _PdnMgmtIpDefaultRouter_Type()
)
pdnMgmtIpDefaultRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnMgmtIpDefaultRouter.setStatus("current")
_PdnMgmtIpConformance_ObjectIdentity = ObjectIdentity
pdnMgmtIpConformance = _PdnMgmtIpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 2)
)
_PdnMgmtIpGroups_ObjectIdentity = ObjectIdentity
pdnMgmtIpGroups = _PdnMgmtIpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 2, 1)
)
_PdnMgmtIpCompliances_ObjectIdentity = ObjectIdentity
pdnMgmtIpCompliances = _PdnMgmtIpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 2, 2)
)

# Managed Objects groups

pdnMgmtIpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 2, 1, 1)
)
pdnMgmtIpConfigGroup.setObjects(
      *(("PDN-MGMT-IP-MIB", "pdnMgmtIpAddress"),
        ("PDN-MGMT-IP-MIB", "pdnMgmtIpNetMask"),
        ("PDN-MGMT-IP-MIB", "pdnMgmtIpEthGateway"),
        ("PDN-MGMT-IP-MIB", "pdnMgmtIpPhysAddress"),
        ("PDN-MGMT-IP-MIB", "pdnMgmtIpConfigMode"),
        ("PDN-MGMT-IP-MIB", "pdnMgmtBootIfIndex"),
        ("PDN-MGMT-IP-MIB", "pdnMgmtBootVpi"),
        ("PDN-MGMT-IP-MIB", "pdnMgmtBootVci"),
        ("PDN-MGMT-IP-MIB", "pdnMgmtIpAdminStatus"),
        ("PDN-MGMT-IP-MIB", "pdnMgmtIpPortIfIndex"),
        ("PDN-MGMT-IP-MIB", "pdnMgmtNextHopIp"),
        ("PDN-MGMT-IP-MIB", "pdnMgmtAtmInvArpRowStatus"),
        ("PDN-MGMT-IP-MIB", "pdnMgmtIpDefaultRouter"))
)
if mibBuilder.loadTexts:
    pdnMgmtIpConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pdnMgmtIpConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 21, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pdnMgmtIpConfigCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-MGMT-IP-MIB",
    **{"pdnMgmtIpMIB": pdnMgmtIpMIB,
       "pdnMgmtIpConfObjects": pdnMgmtIpConfObjects,
       "pdnMgmtIpPortTable": pdnMgmtIpPortTable,
       "pdnMgmtIpPortEntry": pdnMgmtIpPortEntry,
       "pdnMgmtIpPortIndex": pdnMgmtIpPortIndex,
       "pdnMgmtIpAddress": pdnMgmtIpAddress,
       "pdnMgmtIpNetMask": pdnMgmtIpNetMask,
       "pdnMgmtIpEthGateway": pdnMgmtIpEthGateway,
       "pdnMgmtIpPhysAddress": pdnMgmtIpPhysAddress,
       "pdnMgmtIpConfigMode": pdnMgmtIpConfigMode,
       "pdnMgmtBootIfIndex": pdnMgmtBootIfIndex,
       "pdnMgmtBootVpi": pdnMgmtBootVpi,
       "pdnMgmtBootVci": pdnMgmtBootVci,
       "pdnMgmtIpAdminStatus": pdnMgmtIpAdminStatus,
       "pdnMgmtAtmInvArpTable": pdnMgmtAtmInvArpTable,
       "pdnMgmtAtmInvArpEntry": pdnMgmtAtmInvArpEntry,
       "pdnMgmtAtmIfIndex": pdnMgmtAtmIfIndex,
       "pdnMgmtAtmVpi": pdnMgmtAtmVpi,
       "pdnMgmtAtmVci": pdnMgmtAtmVci,
       "pdnMgmtIpPortIfIndex": pdnMgmtIpPortIfIndex,
       "pdnMgmtNextHopIp": pdnMgmtNextHopIp,
       "pdnMgmtAtmInvArpRowStatus": pdnMgmtAtmInvArpRowStatus,
       "pdnMgmtIpDefaultRouter": pdnMgmtIpDefaultRouter,
       "pdnMgmtIpConformance": pdnMgmtIpConformance,
       "pdnMgmtIpGroups": pdnMgmtIpGroups,
       "pdnMgmtIpConfigGroup": pdnMgmtIpConfigGroup,
       "pdnMgmtIpCompliances": pdnMgmtIpCompliances,
       "pdnMgmtIpConfigCompliance": pdnMgmtIpConfigCompliance}
)
