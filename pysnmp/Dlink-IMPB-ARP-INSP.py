# SNMP MIB module (Dlink-IMPB-ARP-INSP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Dlink-IMPB-ARP-INSP
# Produced by pysmi-1.5.4 at Mon Oct 14 21:35:52 2024
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

(rnd,) = mibBuilder.importSymbols(
    "DLINK-3100-MIB",
    "rnd")

(rlImpbArpInspection,) = mibBuilder.importSymbols(
    "Dlink-IMPB-FEATURES",
    "rlImpbArpInspection")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(PortList,
 VlanId) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlIMPBArpInspectionStationTable_Object = MibTable
rlIMPBArpInspectionStationTable = _RlIMPBArpInspectionStationTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 2, 1)
)
if mibBuilder.loadTexts:
    rlIMPBArpInspectionStationTable.setStatus("current")
_RlIMPBArpInspectionStationEntry_Object = MibTableRow
rlIMPBArpInspectionStationEntry = _RlIMPBArpInspectionStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 2, 1, 1)
)
rlIMPBArpInspectionStationEntry.setIndexNames(
    (0, "Dlink-IMPB-ARP-INSP", "rlIMPBArpInspectionStationIPAddress"),
)
if mibBuilder.loadTexts:
    rlIMPBArpInspectionStationEntry.setStatus("current")
_RlIMPBArpInspectionStationIPAddress_Type = IpAddress
_RlIMPBArpInspectionStationIPAddress_Object = MibTableColumn
rlIMPBArpInspectionStationIPAddress = _RlIMPBArpInspectionStationIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 2, 1, 1, 1),
    _RlIMPBArpInspectionStationIPAddress_Type()
)
rlIMPBArpInspectionStationIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIMPBArpInspectionStationIPAddress.setStatus("current")
_RlIMPBArpInspectionStationMACAddress_Type = MacAddress
_RlIMPBArpInspectionStationMACAddress_Object = MibTableColumn
rlIMPBArpInspectionStationMACAddress = _RlIMPBArpInspectionStationMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 2, 1, 1, 2),
    _RlIMPBArpInspectionStationMACAddress_Type()
)
rlIMPBArpInspectionStationMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIMPBArpInspectionStationMACAddress.setStatus("current")
_RlIMPBArpInspectionStationPortList_Type = PortList
_RlIMPBArpInspectionStationPortList_Object = MibTableColumn
rlIMPBArpInspectionStationPortList = _RlIMPBArpInspectionStationPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 2, 1, 1, 3),
    _RlIMPBArpInspectionStationPortList_Type()
)
rlIMPBArpInspectionStationPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIMPBArpInspectionStationPortList.setStatus("current")
_RlIMPBArpInspectionStationRowStatus_Type = RowStatus
_RlIMPBArpInspectionStationRowStatus_Object = MibTableColumn
rlIMPBArpInspectionStationRowStatus = _RlIMPBArpInspectionStationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 2, 1, 1, 4),
    _RlIMPBArpInspectionStationRowStatus_Type()
)
rlIMPBArpInspectionStationRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIMPBArpInspectionStationRowStatus.setStatus("current")
_RlIMPBArpInspectionClearAction_Type = TruthValue
_RlIMPBArpInspectionClearAction_Object = MibScalar
rlIMPBArpInspectionClearAction = _RlIMPBArpInspectionClearAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 2, 2),
    _RlIMPBArpInspectionClearAction_Type()
)
rlIMPBArpInspectionClearAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIMPBArpInspectionClearAction.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Dlink-IMPB-ARP-INSP",
    **{"rlIMPBArpInspectionStationTable": rlIMPBArpInspectionStationTable,
       "rlIMPBArpInspectionStationEntry": rlIMPBArpInspectionStationEntry,
       "rlIMPBArpInspectionStationIPAddress": rlIMPBArpInspectionStationIPAddress,
       "rlIMPBArpInspectionStationMACAddress": rlIMPBArpInspectionStationMACAddress,
       "rlIMPBArpInspectionStationPortList": rlIMPBArpInspectionStationPortList,
       "rlIMPBArpInspectionStationRowStatus": rlIMPBArpInspectionStationRowStatus,
       "rlIMPBArpInspectionClearAction": rlIMPBArpInspectionClearAction}
)
