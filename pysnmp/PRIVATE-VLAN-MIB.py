# SNMP MIB module (PRIVATE-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PRIVATE-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:45 2024
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

(PortList,
 VlanId,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId",
    "VlanIdOrNone")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swPrivateVLANMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 69)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SecondaryVlanType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("community", 2),
          ("isolated", 1))
    )



# MIB Managed Objects in the order of their OIDs

_SwPrivateVlanCtrl_ObjectIdentity = ObjectIdentity
swPrivateVlanCtrl = _SwPrivateVlanCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 69, 1)
)
_SwPrivateVlanInfo_ObjectIdentity = ObjectIdentity
swPrivateVlanInfo = _SwPrivateVlanInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 69, 2)
)
_SwPrivateVlanMgmt_ObjectIdentity = ObjectIdentity
swPrivateVlanMgmt = _SwPrivateVlanMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 69, 3)
)
_SwPrivateVlanTable_Object = MibTable
swPrivateVlanTable = _SwPrivateVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 69, 3, 1)
)
if mibBuilder.loadTexts:
    swPrivateVlanTable.setStatus("current")
_SwPrivateVlanEntry_Object = MibTableRow
swPrivateVlanEntry = _SwPrivateVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 69, 3, 1, 1)
)
swPrivateVlanEntry.setIndexNames(
    (0, "PRIVATE-VLAN-MIB", "swPrivateVlanId"),
)
if mibBuilder.loadTexts:
    swPrivateVlanEntry.setStatus("current")
_SwPrivateVlanId_Type = VlanId
_SwPrivateVlanId_Object = MibTableColumn
swPrivateVlanId = _SwPrivateVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 69, 3, 1, 1, 1),
    _SwPrivateVlanId_Type()
)
swPrivateVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPrivateVlanId.setStatus("current")
_SwPrivateVlanName_Type = DisplayString
_SwPrivateVlanName_Object = MibTableColumn
swPrivateVlanName = _SwPrivateVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 69, 3, 1, 1, 2),
    _SwPrivateVlanName_Type()
)
swPrivateVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swPrivateVlanName.setStatus("current")
_SwPrivateVlanPromiscuousPorts_Type = PortList
_SwPrivateVlanPromiscuousPorts_Object = MibTableColumn
swPrivateVlanPromiscuousPorts = _SwPrivateVlanPromiscuousPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 69, 3, 1, 1, 3),
    _SwPrivateVlanPromiscuousPorts_Type()
)
swPrivateVlanPromiscuousPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPrivateVlanPromiscuousPorts.setStatus("current")
_SwPrivateVlanTrunkPorts_Type = PortList
_SwPrivateVlanTrunkPorts_Object = MibTableColumn
swPrivateVlanTrunkPorts = _SwPrivateVlanTrunkPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 69, 3, 1, 1, 4),
    _SwPrivateVlanTrunkPorts_Type()
)
swPrivateVlanTrunkPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPrivateVlanTrunkPorts.setStatus("current")
_SwPrivateVlanRowStatus_Type = RowStatus
_SwPrivateVlanRowStatus_Object = MibTableColumn
swPrivateVlanRowStatus = _SwPrivateVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 69, 3, 1, 1, 5),
    _SwPrivateVlanRowStatus_Type()
)
swPrivateVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swPrivateVlanRowStatus.setStatus("current")
_SwSecondaryVlanTable_Object = MibTable
swSecondaryVlanTable = _SwSecondaryVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 69, 3, 2)
)
if mibBuilder.loadTexts:
    swSecondaryVlanTable.setStatus("current")
_SwSecondaryVlanEntry_Object = MibTableRow
swSecondaryVlanEntry = _SwSecondaryVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 69, 3, 2, 1)
)
swSecondaryVlanEntry.setIndexNames(
    (0, "PRIVATE-VLAN-MIB", "swPrivateVlanId"),
    (0, "PRIVATE-VLAN-MIB", "swSecondaryVlanId"),
)
if mibBuilder.loadTexts:
    swSecondaryVlanEntry.setStatus("current")
_SwSecondaryVlanId_Type = VlanId
_SwSecondaryVlanId_Object = MibTableColumn
swSecondaryVlanId = _SwSecondaryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 69, 3, 2, 1, 1),
    _SwSecondaryVlanId_Type()
)
swSecondaryVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSecondaryVlanId.setStatus("current")
_SwSecondaryVlanType_Type = SecondaryVlanType
_SwSecondaryVlanType_Object = MibTableColumn
swSecondaryVlanType = _SwSecondaryVlanType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 69, 3, 2, 1, 2),
    _SwSecondaryVlanType_Type()
)
swSecondaryVlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSecondaryVlanType.setStatus("current")
_SwSecondaryVlanPorts_Type = PortList
_SwSecondaryVlanPorts_Object = MibTableColumn
swSecondaryVlanPorts = _SwSecondaryVlanPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 69, 3, 2, 1, 3),
    _SwSecondaryVlanPorts_Type()
)
swSecondaryVlanPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSecondaryVlanPorts.setStatus("current")
_SwSecondaryVlanRowStatus_Type = RowStatus
_SwSecondaryVlanRowStatus_Object = MibTableColumn
swSecondaryVlanRowStatus = _SwSecondaryVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 69, 3, 2, 1, 4),
    _SwSecondaryVlanRowStatus_Type()
)
swSecondaryVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSecondaryVlanRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRIVATE-VLAN-MIB",
    **{"SecondaryVlanType": SecondaryVlanType,
       "swPrivateVLANMIB": swPrivateVLANMIB,
       "swPrivateVlanCtrl": swPrivateVlanCtrl,
       "swPrivateVlanInfo": swPrivateVlanInfo,
       "swPrivateVlanMgmt": swPrivateVlanMgmt,
       "swPrivateVlanTable": swPrivateVlanTable,
       "swPrivateVlanEntry": swPrivateVlanEntry,
       "swPrivateVlanId": swPrivateVlanId,
       "swPrivateVlanName": swPrivateVlanName,
       "swPrivateVlanPromiscuousPorts": swPrivateVlanPromiscuousPorts,
       "swPrivateVlanTrunkPorts": swPrivateVlanTrunkPorts,
       "swPrivateVlanRowStatus": swPrivateVlanRowStatus,
       "swSecondaryVlanTable": swSecondaryVlanTable,
       "swSecondaryVlanEntry": swSecondaryVlanEntry,
       "swSecondaryVlanId": swSecondaryVlanId,
       "swSecondaryVlanType": swSecondaryVlanType,
       "swSecondaryVlanPorts": swSecondaryVlanPorts,
       "swSecondaryVlanRowStatus": swSecondaryVlanRowStatus}
)
