# SNMP MIB module (ARP-Spoofing-Prevent-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ARP-Spoofing-Prevent-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:31 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swARPSpoofingPreventMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 62)
)


# Types definitions



class PortList(OctetString):
    """Custom type PortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwARPSpoofingPreventCtrl_ObjectIdentity = ObjectIdentity
swARPSpoofingPreventCtrl = _SwARPSpoofingPreventCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 62, 1)
)
_SwARPSpoofingPreventInfo_ObjectIdentity = ObjectIdentity
swARPSpoofingPreventInfo = _SwARPSpoofingPreventInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 62, 2)
)
_SwARPSpoofingPreventMgmt_ObjectIdentity = ObjectIdentity
swARPSpoofingPreventMgmt = _SwARPSpoofingPreventMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 62, 3)
)
_SwARPSpoofingPreventMgmtTable_Object = MibTable
swARPSpoofingPreventMgmtTable = _SwARPSpoofingPreventMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 62, 3, 1)
)
if mibBuilder.loadTexts:
    swARPSpoofingPreventMgmtTable.setStatus("current")
_SwARPSpoofingPreventMgmtEntry_Object = MibTableRow
swARPSpoofingPreventMgmtEntry = _SwARPSpoofingPreventMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 62, 3, 1, 1)
)
swARPSpoofingPreventMgmtEntry.setIndexNames(
    (0, "ARP-Spoofing-Prevent-MIB", "swARPSpoofingPreventMgmtGatewayIP"),
    (0, "ARP-Spoofing-Prevent-MIB", "swARPSpoofingPreventMgmtGatewayMAC"),
)
if mibBuilder.loadTexts:
    swARPSpoofingPreventMgmtEntry.setStatus("current")
_SwARPSpoofingPreventMgmtGatewayIP_Type = IpAddress
_SwARPSpoofingPreventMgmtGatewayIP_Object = MibTableColumn
swARPSpoofingPreventMgmtGatewayIP = _SwARPSpoofingPreventMgmtGatewayIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 62, 3, 1, 1, 1),
    _SwARPSpoofingPreventMgmtGatewayIP_Type()
)
swARPSpoofingPreventMgmtGatewayIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swARPSpoofingPreventMgmtGatewayIP.setStatus("current")
_SwARPSpoofingPreventMgmtGatewayMAC_Type = MacAddress
_SwARPSpoofingPreventMgmtGatewayMAC_Object = MibTableColumn
swARPSpoofingPreventMgmtGatewayMAC = _SwARPSpoofingPreventMgmtGatewayMAC_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 62, 3, 1, 1, 2),
    _SwARPSpoofingPreventMgmtGatewayMAC_Type()
)
swARPSpoofingPreventMgmtGatewayMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swARPSpoofingPreventMgmtGatewayMAC.setStatus("current")
_SwARPSpoofingPreventMgmtPorts_Type = PortList
_SwARPSpoofingPreventMgmtPorts_Object = MibTableColumn
swARPSpoofingPreventMgmtPorts = _SwARPSpoofingPreventMgmtPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 62, 3, 1, 1, 3),
    _SwARPSpoofingPreventMgmtPorts_Type()
)
swARPSpoofingPreventMgmtPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swARPSpoofingPreventMgmtPorts.setStatus("current")
_SwARPSpoofingPreventMgmtStatus_Type = RowStatus
_SwARPSpoofingPreventMgmtStatus_Object = MibTableColumn
swARPSpoofingPreventMgmtStatus = _SwARPSpoofingPreventMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 62, 3, 1, 1, 4),
    _SwARPSpoofingPreventMgmtStatus_Type()
)
swARPSpoofingPreventMgmtStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swARPSpoofingPreventMgmtStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARP-Spoofing-Prevent-MIB",
    **{"PortList": PortList,
       "swARPSpoofingPreventMIB": swARPSpoofingPreventMIB,
       "swARPSpoofingPreventCtrl": swARPSpoofingPreventCtrl,
       "swARPSpoofingPreventInfo": swARPSpoofingPreventInfo,
       "swARPSpoofingPreventMgmt": swARPSpoofingPreventMgmt,
       "swARPSpoofingPreventMgmtTable": swARPSpoofingPreventMgmtTable,
       "swARPSpoofingPreventMgmtEntry": swARPSpoofingPreventMgmtEntry,
       "swARPSpoofingPreventMgmtGatewayIP": swARPSpoofingPreventMgmtGatewayIP,
       "swARPSpoofingPreventMgmtGatewayMAC": swARPSpoofingPreventMgmtGatewayMAC,
       "swARPSpoofingPreventMgmtPorts": swARPSpoofingPreventMgmtPorts,
       "swARPSpoofingPreventMgmtStatus": swARPSpoofingPreventMgmtStatus}
)
