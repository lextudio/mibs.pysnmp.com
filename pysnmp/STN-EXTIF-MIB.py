# SNMP MIB module (STN-EXTIF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STN-EXTIF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:05 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(stnExtensions,
 stnNotification) = mibBuilder.importSymbols(
    "SPRING-TIDE-NETWORKS-SMI",
    "stnExtensions",
    "stnNotification")


# MODULE-IDENTITY

stnExtIf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_StnExtIfObjects_ObjectIdentity = ObjectIdentity
stnExtIfObjects = _StnExtIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 3, 1, 1)
)
_StnExtIfL2Table_Object = MibTable
stnExtIfL2Table = _StnExtIfL2Table_Object(
    (1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    stnExtIfL2Table.setStatus("current")
_StnExtIfL2Entry_Object = MibTableRow
stnExtIfL2Entry = _StnExtIfL2Entry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 1, 1)
)
stnExtIfL2Entry.setIndexNames(
    (0, "STN-EXTIF-MIB", "stnExtIfL2IfName"),
)
if mibBuilder.loadTexts:
    stnExtIfL2Entry.setStatus("current")
_StnExtIfL2IfName_Type = DisplayString
_StnExtIfL2IfName_Object = MibTableColumn
stnExtIfL2IfName = _StnExtIfL2IfName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 1, 1, 1),
    _StnExtIfL2IfName_Type()
)
stnExtIfL2IfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnExtIfL2IfName.setStatus("current")
_StnExtIfL2IfIndex_Type = InterfaceIndex
_StnExtIfL2IfIndex_Object = MibTableColumn
stnExtIfL2IfIndex = _StnExtIfL2IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 1, 1, 2),
    _StnExtIfL2IfIndex_Type()
)
stnExtIfL2IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnExtIfL2IfIndex.setStatus("current")
_StnExtIfL3Table_Object = MibTable
stnExtIfL3Table = _StnExtIfL3Table_Object(
    (1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    stnExtIfL3Table.setStatus("current")
_StnExtIfL3Entry_Object = MibTableRow
stnExtIfL3Entry = _StnExtIfL3Entry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 2, 1)
)
stnExtIfL3Entry.setIndexNames(
    (0, "STN-EXTIF-MIB", "stnExtIfL3IfName"),
)
if mibBuilder.loadTexts:
    stnExtIfL3Entry.setStatus("current")
_StnExtIfL3IfName_Type = DisplayString
_StnExtIfL3IfName_Object = MibTableColumn
stnExtIfL3IfName = _StnExtIfL3IfName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 2, 1, 1),
    _StnExtIfL3IfName_Type()
)
stnExtIfL3IfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnExtIfL3IfName.setStatus("current")
_StnExtIfL3IfIndex_Type = InterfaceIndex
_StnExtIfL3IfIndex_Object = MibTableColumn
stnExtIfL3IfIndex = _StnExtIfL3IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 2, 1, 2),
    _StnExtIfL3IfIndex_Type()
)
stnExtIfL3IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnExtIfL3IfIndex.setStatus("current")
_StnExtIfL3SubnetIfInstance_Type = Integer32
_StnExtIfL3SubnetIfInstance_Object = MibTableColumn
stnExtIfL3SubnetIfInstance = _StnExtIfL3SubnetIfInstance_Object(
    (1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 2, 1, 3),
    _StnExtIfL3SubnetIfInstance_Type()
)
stnExtIfL3SubnetIfInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnExtIfL3SubnetIfInstance.setStatus("current")
_StnExtIfL3IpAddress_Type = IpAddress
_StnExtIfL3IpAddress_Object = MibTableColumn
stnExtIfL3IpAddress = _StnExtIfL3IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 2, 1, 4),
    _StnExtIfL3IpAddress_Type()
)
stnExtIfL3IpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnExtIfL3IpAddress.setStatus("current")
_StnExtIfL3IpMask_Type = IpAddress
_StnExtIfL3IpMask_Object = MibTableColumn
stnExtIfL3IpMask = _StnExtIfL3IpMask_Object(
    (1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 2, 1, 5),
    _StnExtIfL3IpMask_Type()
)
stnExtIfL3IpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnExtIfL3IpMask.setStatus("current")
_StnExtIpAddrL3Table_Object = MibTable
stnExtIpAddrL3Table = _StnExtIpAddrL3Table_Object(
    (1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    stnExtIpAddrL3Table.setStatus("current")
_StnExtIpAddrL3Entry_Object = MibTableRow
stnExtIpAddrL3Entry = _StnExtIpAddrL3Entry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 3, 1)
)
stnExtIpAddrL3Entry.setIndexNames(
    (0, "STN-EXTIF-MIB", "stnExtIpAddrL3IpAddress"),
)
if mibBuilder.loadTexts:
    stnExtIpAddrL3Entry.setStatus("current")
_StnExtIpAddrL3IpAddress_Type = IpAddress
_StnExtIpAddrL3IpAddress_Object = MibTableColumn
stnExtIpAddrL3IpAddress = _StnExtIpAddrL3IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 3, 1, 1),
    _StnExtIpAddrL3IpAddress_Type()
)
stnExtIpAddrL3IpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnExtIpAddrL3IpAddress.setStatus("current")
_StnExtIpAddrL3IfIndex_Type = InterfaceIndex
_StnExtIpAddrL3IfIndex_Object = MibTableColumn
stnExtIpAddrL3IfIndex = _StnExtIpAddrL3IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 3, 1, 2),
    _StnExtIpAddrL3IfIndex_Type()
)
stnExtIpAddrL3IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnExtIpAddrL3IfIndex.setStatus("current")
_StnExtIpAddrL3SubnetIfInstance_Type = Integer32
_StnExtIpAddrL3SubnetIfInstance_Object = MibTableColumn
stnExtIpAddrL3SubnetIfInstance = _StnExtIpAddrL3SubnetIfInstance_Object(
    (1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 3, 1, 3),
    _StnExtIpAddrL3SubnetIfInstance_Type()
)
stnExtIpAddrL3SubnetIfInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnExtIpAddrL3SubnetIfInstance.setStatus("current")
_StnExtIpAddrL3IfName_Type = DisplayString
_StnExtIpAddrL3IfName_Object = MibTableColumn
stnExtIpAddrL3IfName = _StnExtIpAddrL3IfName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 3, 1, 4),
    _StnExtIpAddrL3IfName_Type()
)
stnExtIpAddrL3IfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnExtIpAddrL3IfName.setStatus("current")
_StnExtIpAddrL3IpMask_Type = IpAddress
_StnExtIpAddrL3IpMask_Object = MibTableColumn
stnExtIpAddrL3IpMask = _StnExtIpAddrL3IpMask_Object(
    (1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 3, 1, 5),
    _StnExtIpAddrL3IpMask_Type()
)
stnExtIpAddrL3IpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnExtIpAddrL3IpMask.setStatus("current")
_StnExtSubnetL3Table_Object = MibTable
stnExtSubnetL3Table = _StnExtSubnetL3Table_Object(
    (1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    stnExtSubnetL3Table.setStatus("current")
_StnExtSubnetL3Entry_Object = MibTableRow
stnExtSubnetL3Entry = _StnExtSubnetL3Entry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 4, 1)
)
stnExtSubnetL3Entry.setIndexNames(
    (0, "STN-EXTIF-MIB", "stnExtSubnetL3SubnetIfInstance"),
)
if mibBuilder.loadTexts:
    stnExtSubnetL3Entry.setStatus("current")
_StnExtSubnetL3SubnetIfInstance_Type = Integer32
_StnExtSubnetL3SubnetIfInstance_Object = MibTableColumn
stnExtSubnetL3SubnetIfInstance = _StnExtSubnetL3SubnetIfInstance_Object(
    (1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 4, 1, 1),
    _StnExtSubnetL3SubnetIfInstance_Type()
)
stnExtSubnetL3SubnetIfInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnExtSubnetL3SubnetIfInstance.setStatus("current")
_StnExtSubnetL3IfIndex_Type = InterfaceIndex
_StnExtSubnetL3IfIndex_Object = MibTableColumn
stnExtSubnetL3IfIndex = _StnExtSubnetL3IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 4, 1, 2),
    _StnExtSubnetL3IfIndex_Type()
)
stnExtSubnetL3IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnExtSubnetL3IfIndex.setStatus("current")
_StnExtSubnetL3IfName_Type = DisplayString
_StnExtSubnetL3IfName_Object = MibTableColumn
stnExtSubnetL3IfName = _StnExtSubnetL3IfName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 4, 1, 3),
    _StnExtSubnetL3IfName_Type()
)
stnExtSubnetL3IfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnExtSubnetL3IfName.setStatus("current")
_StnExtSubnetL3IpAddress_Type = IpAddress
_StnExtSubnetL3IpAddress_Object = MibTableColumn
stnExtSubnetL3IpAddress = _StnExtSubnetL3IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 4, 1, 4),
    _StnExtSubnetL3IpAddress_Type()
)
stnExtSubnetL3IpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnExtSubnetL3IpAddress.setStatus("current")
_StnExtSubnetL3IpMask_Type = IpAddress
_StnExtSubnetL3IpMask_Object = MibTableColumn
stnExtSubnetL3IpMask = _StnExtSubnetL3IpMask_Object(
    (1, 3, 6, 1, 4, 1, 3551, 3, 1, 1, 4, 1, 5),
    _StnExtSubnetL3IpMask_Type()
)
stnExtSubnetL3IpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnExtSubnetL3IpMask.setStatus("current")
_StnExtIfMibConformance_ObjectIdentity = ObjectIdentity
stnExtIfMibConformance = _StnExtIfMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 3, 1, 2)
)
_StnExtIfMibTraps_ObjectIdentity = ObjectIdentity
stnExtIfMibTraps = _StnExtIfMibTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 3, 1, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STN-EXTIF-MIB",
    **{"stnExtIf": stnExtIf,
       "stnExtIfObjects": stnExtIfObjects,
       "stnExtIfL2Table": stnExtIfL2Table,
       "stnExtIfL2Entry": stnExtIfL2Entry,
       "stnExtIfL2IfName": stnExtIfL2IfName,
       "stnExtIfL2IfIndex": stnExtIfL2IfIndex,
       "stnExtIfL3Table": stnExtIfL3Table,
       "stnExtIfL3Entry": stnExtIfL3Entry,
       "stnExtIfL3IfName": stnExtIfL3IfName,
       "stnExtIfL3IfIndex": stnExtIfL3IfIndex,
       "stnExtIfL3SubnetIfInstance": stnExtIfL3SubnetIfInstance,
       "stnExtIfL3IpAddress": stnExtIfL3IpAddress,
       "stnExtIfL3IpMask": stnExtIfL3IpMask,
       "stnExtIpAddrL3Table": stnExtIpAddrL3Table,
       "stnExtIpAddrL3Entry": stnExtIpAddrL3Entry,
       "stnExtIpAddrL3IpAddress": stnExtIpAddrL3IpAddress,
       "stnExtIpAddrL3IfIndex": stnExtIpAddrL3IfIndex,
       "stnExtIpAddrL3SubnetIfInstance": stnExtIpAddrL3SubnetIfInstance,
       "stnExtIpAddrL3IfName": stnExtIpAddrL3IfName,
       "stnExtIpAddrL3IpMask": stnExtIpAddrL3IpMask,
       "stnExtSubnetL3Table": stnExtSubnetL3Table,
       "stnExtSubnetL3Entry": stnExtSubnetL3Entry,
       "stnExtSubnetL3SubnetIfInstance": stnExtSubnetL3SubnetIfInstance,
       "stnExtSubnetL3IfIndex": stnExtSubnetL3IfIndex,
       "stnExtSubnetL3IfName": stnExtSubnetL3IfName,
       "stnExtSubnetL3IpAddress": stnExtSubnetL3IpAddress,
       "stnExtSubnetL3IpMask": stnExtSubnetL3IpMask,
       "stnExtIfMibConformance": stnExtIfMibConformance,
       "stnExtIfMibTraps": stnExtIfMibTraps}
)
