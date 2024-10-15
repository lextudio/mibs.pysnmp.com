# SNMP MIB module (MERU-CONFIG-GRE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MERU-CONFIG-GRE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:01 2024
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(mwConfiguration,) = mibBuilder.importSymbols(
    "MERU-SMI",
    "mwConfiguration")

(MwlOnOffSwitch,
 MwlProfileOwner) = mibBuilder.importSymbols(
    "MERU-TC",
    "MwlOnOffSwitch",
    "MwlProfileOwner")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mwConfigGRE = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MwGreTable_Object = MibTable
mwGreTable = _MwGreTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 15, 1)
)
if mibBuilder.loadTexts:
    mwGreTable.setStatus("current")
_MwGreEntry_Object = MibTableRow
mwGreEntry = _MwGreEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 15, 1, 1)
)
mwGreEntry.setIndexNames(
    (0, "MERU-CONFIG-GRE-MIB", "mwGreTableIndex"),
)
if mibBuilder.loadTexts:
    mwGreEntry.setStatus("current")
_MwGreTableIndex_Type = Integer32
_MwGreTableIndex_Object = MibTableColumn
mwGreTableIndex = _MwGreTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 15, 1, 1, 1),
    _MwGreTableIndex_Type()
)
mwGreTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwGreTableIndex.setStatus("current")


class _MwGreName_Type(DisplayString):
    """Custom type mwGreName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MwGreName_Type.__name__ = "DisplayString"
_MwGreName_Object = MibTableColumn
mwGreName = _MwGreName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 15, 1, 1, 2),
    _MwGreName_Type()
)
mwGreName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwGreName.setStatus("current")
_MwGreInterfaceIndex_Type = Unsigned32
_MwGreInterfaceIndex_Object = MibTableColumn
mwGreInterfaceIndex = _MwGreInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 15, 1, 1, 3),
    _MwGreInterfaceIndex_Type()
)
mwGreInterfaceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwGreInterfaceIndex.setStatus("current")
_MwGreDHCPServerIpAddress_Type = IpAddress
_MwGreDHCPServerIpAddress_Object = MibTableColumn
mwGreDHCPServerIpAddress = _MwGreDHCPServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 15, 1, 1, 4),
    _MwGreDHCPServerIpAddress_Type()
)
mwGreDHCPServerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwGreDHCPServerIpAddress.setStatus("current")
_MwGreLocalInternalAddress_Type = IpAddress
_MwGreLocalInternalAddress_Object = MibTableColumn
mwGreLocalInternalAddress = _MwGreLocalInternalAddress_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 15, 1, 1, 5),
    _MwGreLocalInternalAddress_Type()
)
mwGreLocalInternalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwGreLocalInternalAddress.setStatus("current")
_MwGreLocalInternalNetmask_Type = IpAddress
_MwGreLocalInternalNetmask_Object = MibTableColumn
mwGreLocalInternalNetmask = _MwGreLocalInternalNetmask_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 15, 1, 1, 6),
    _MwGreLocalInternalNetmask_Type()
)
mwGreLocalInternalNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwGreLocalInternalNetmask.setStatus("current")
_MwGreRemoteEndpointAddress_Type = IpAddress
_MwGreRemoteEndpointAddress_Object = MibTableColumn
mwGreRemoteEndpointAddress = _MwGreRemoteEndpointAddress_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 15, 1, 1, 7),
    _MwGreRemoteEndpointAddress_Type()
)
mwGreRemoteEndpointAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwGreRemoteEndpointAddress.setStatus("current")
_MwGreOverrideDefaultDHCPServer_Type = MwlOnOffSwitch
_MwGreOverrideDefaultDHCPServer_Object = MibTableColumn
mwGreOverrideDefaultDHCPServer = _MwGreOverrideDefaultDHCPServer_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 15, 1, 1, 8),
    _MwGreOverrideDefaultDHCPServer_Type()
)
mwGreOverrideDefaultDHCPServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwGreOverrideDefaultDHCPServer.setStatus("current")
_MwGreOwner_Type = MwlProfileOwner
_MwGreOwner_Object = MibTableColumn
mwGreOwner = _MwGreOwner_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 15, 1, 1, 9),
    _MwGreOwner_Type()
)
mwGreOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwGreOwner.setStatus("current")
_MwGreRowStatus_Type = RowStatus
_MwGreRowStatus_Object = MibTableColumn
mwGreRowStatus = _MwGreRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 15, 1, 1, 17),
    _MwGreRowStatus_Type()
)
mwGreRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwGreRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-CONFIG-GRE-MIB",
    **{"mwConfigGRE": mwConfigGRE,
       "mwGreTable": mwGreTable,
       "mwGreEntry": mwGreEntry,
       "mwGreTableIndex": mwGreTableIndex,
       "mwGreName": mwGreName,
       "mwGreInterfaceIndex": mwGreInterfaceIndex,
       "mwGreDHCPServerIpAddress": mwGreDHCPServerIpAddress,
       "mwGreLocalInternalAddress": mwGreLocalInternalAddress,
       "mwGreLocalInternalNetmask": mwGreLocalInternalNetmask,
       "mwGreRemoteEndpointAddress": mwGreRemoteEndpointAddress,
       "mwGreOverrideDefaultDHCPServer": mwGreOverrideDefaultDHCPServer,
       "mwGreOwner": mwGreOwner,
       "mwGreRowStatus": mwGreRowStatus}
)
