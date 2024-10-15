# SNMP MIB module (SUBNETVLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SUBNETVLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:29 2024
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


# MODULE-IDENTITY

swSubnetVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 75)
)


# Types definitions



class VlanId(Integer32):
    """Custom type VlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )




# TEXTUAL-CONVENTIONS



class Ipv6Address(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



# MIB Managed Objects in the order of their OIDs

_SwSubnetVlanCtrl_ObjectIdentity = ObjectIdentity
swSubnetVlanCtrl = _SwSubnetVlanCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 75, 1)
)
_SwSubnetVlanInfo_ObjectIdentity = ObjectIdentity
swSubnetVlanInfo = _SwSubnetVlanInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 75, 2)
)
_SwSubnetVlanMgmt_ObjectIdentity = ObjectIdentity
swSubnetVlanMgmt = _SwSubnetVlanMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 75, 3)
)
_SwVlanPrecedenceTable_Object = MibTable
swVlanPrecedenceTable = _SwVlanPrecedenceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 1)
)
if mibBuilder.loadTexts:
    swVlanPrecedenceTable.setStatus("current")
_SwVlanPrecedenceEntry_Object = MibTableRow
swVlanPrecedenceEntry = _SwVlanPrecedenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 1, 1)
)
swVlanPrecedenceEntry.setIndexNames(
    (0, "SUBNETVLAN-MIB", "swVlanPrecedencePortIndex"),
)
if mibBuilder.loadTexts:
    swVlanPrecedenceEntry.setStatus("current")


class _SwVlanPrecedencePortIndex_Type(Integer32):
    """Custom type swVlanPrecedencePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwVlanPrecedencePortIndex_Type.__name__ = "Integer32"
_SwVlanPrecedencePortIndex_Object = MibTableColumn
swVlanPrecedencePortIndex = _SwVlanPrecedencePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 1, 1, 1),
    _SwVlanPrecedencePortIndex_Type()
)
swVlanPrecedencePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVlanPrecedencePortIndex.setStatus("current")


class _SwVlanPrecedenceClassification_Type(Integer32):
    """Custom type swVlanPrecedenceClassification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("macBased", 1),
          ("subnetBased", 2))
    )


_SwVlanPrecedenceClassification_Type.__name__ = "Integer32"
_SwVlanPrecedenceClassification_Object = MibTableColumn
swVlanPrecedenceClassification = _SwVlanPrecedenceClassification_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 1, 1, 2),
    _SwVlanPrecedenceClassification_Type()
)
swVlanPrecedenceClassification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swVlanPrecedenceClassification.setStatus("current")
_SwSubnetVLANTable_Object = MibTable
swSubnetVLANTable = _SwSubnetVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 2)
)
if mibBuilder.loadTexts:
    swSubnetVLANTable.setStatus("current")
_SwSubnetVLANEntry_Object = MibTableRow
swSubnetVLANEntry = _SwSubnetVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 2, 1)
)
swSubnetVLANEntry.setIndexNames(
    (0, "SUBNETVLAN-MIB", "swSubnetVLANIPAddress"),
    (0, "SUBNETVLAN-MIB", "swSubnetVLANIPMask"),
)
if mibBuilder.loadTexts:
    swSubnetVLANEntry.setStatus("current")
_SwSubnetVLANIPAddress_Type = IpAddress
_SwSubnetVLANIPAddress_Object = MibTableColumn
swSubnetVLANIPAddress = _SwSubnetVLANIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 2, 1, 1),
    _SwSubnetVLANIPAddress_Type()
)
swSubnetVLANIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSubnetVLANIPAddress.setStatus("current")
_SwSubnetVLANIPMask_Type = IpAddress
_SwSubnetVLANIPMask_Object = MibTableColumn
swSubnetVLANIPMask = _SwSubnetVLANIPMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 2, 1, 2),
    _SwSubnetVLANIPMask_Type()
)
swSubnetVLANIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSubnetVLANIPMask.setStatus("current")
_SwSubnetVLANID_Type = VlanId
_SwSubnetVLANID_Object = MibTableColumn
swSubnetVLANID = _SwSubnetVLANID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 2, 1, 3),
    _SwSubnetVLANID_Type()
)
swSubnetVLANID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSubnetVLANID.setStatus("current")


class _SwSubnetVLANPriority_Type(Integer32):
    """Custom type swSubnetVLANPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwSubnetVLANPriority_Type.__name__ = "Integer32"
_SwSubnetVLANPriority_Object = MibTableColumn
swSubnetVLANPriority = _SwSubnetVLANPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 2, 1, 4),
    _SwSubnetVLANPriority_Type()
)
swSubnetVLANPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSubnetVLANPriority.setStatus("current")
_SwSubnetVLANRowStatus_Type = RowStatus
_SwSubnetVLANRowStatus_Object = MibTableColumn
swSubnetVLANRowStatus = _SwSubnetVLANRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 2, 1, 5),
    _SwSubnetVLANRowStatus_Type()
)
swSubnetVLANRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSubnetVLANRowStatus.setStatus("current")
_SwSubnetVLANIPv6Table_Object = MibTable
swSubnetVLANIPv6Table = _SwSubnetVLANIPv6Table_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 3)
)
if mibBuilder.loadTexts:
    swSubnetVLANIPv6Table.setStatus("current")
_SwSubnetVLANIPv6Entry_Object = MibTableRow
swSubnetVLANIPv6Entry = _SwSubnetVLANIPv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 3, 1)
)
swSubnetVLANIPv6Entry.setIndexNames(
    (0, "SUBNETVLAN-MIB", "swSubnetVLANIPv6Address"),
    (0, "SUBNETVLAN-MIB", "swSubnetVLANIPv6PrefixLength"),
)
if mibBuilder.loadTexts:
    swSubnetVLANIPv6Entry.setStatus("current")
_SwSubnetVLANIPv6Address_Type = Ipv6Address
_SwSubnetVLANIPv6Address_Object = MibTableColumn
swSubnetVLANIPv6Address = _SwSubnetVLANIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 3, 1, 1),
    _SwSubnetVLANIPv6Address_Type()
)
swSubnetVLANIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSubnetVLANIPv6Address.setStatus("current")
_SwSubnetVLANIPv6PrefixLength_Type = Integer32
_SwSubnetVLANIPv6PrefixLength_Object = MibTableColumn
swSubnetVLANIPv6PrefixLength = _SwSubnetVLANIPv6PrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 3, 1, 2),
    _SwSubnetVLANIPv6PrefixLength_Type()
)
swSubnetVLANIPv6PrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSubnetVLANIPv6PrefixLength.setStatus("current")
_SwSubnetVLANIPv6VID_Type = VlanId
_SwSubnetVLANIPv6VID_Object = MibTableColumn
swSubnetVLANIPv6VID = _SwSubnetVLANIPv6VID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 3, 1, 3),
    _SwSubnetVLANIPv6VID_Type()
)
swSubnetVLANIPv6VID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSubnetVLANIPv6VID.setStatus("current")


class _SwSubnetVLANIPv6Priority_Type(Integer32):
    """Custom type swSubnetVLANIPv6Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwSubnetVLANIPv6Priority_Type.__name__ = "Integer32"
_SwSubnetVLANIPv6Priority_Object = MibTableColumn
swSubnetVLANIPv6Priority = _SwSubnetVLANIPv6Priority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 3, 1, 4),
    _SwSubnetVLANIPv6Priority_Type()
)
swSubnetVLANIPv6Priority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSubnetVLANIPv6Priority.setStatus("current")
_SwSubnetVLANIPv6RowStatus_Type = RowStatus
_SwSubnetVLANIPv6RowStatus_Object = MibTableColumn
swSubnetVLANIPv6RowStatus = _SwSubnetVLANIPv6RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 75, 3, 3, 1, 5),
    _SwSubnetVLANIPv6RowStatus_Type()
)
swSubnetVLANIPv6RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSubnetVLANIPv6RowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUBNETVLAN-MIB",
    **{"VlanId": VlanId,
       "Ipv6Address": Ipv6Address,
       "swSubnetVlanMIB": swSubnetVlanMIB,
       "swSubnetVlanCtrl": swSubnetVlanCtrl,
       "swSubnetVlanInfo": swSubnetVlanInfo,
       "swSubnetVlanMgmt": swSubnetVlanMgmt,
       "swVlanPrecedenceTable": swVlanPrecedenceTable,
       "swVlanPrecedenceEntry": swVlanPrecedenceEntry,
       "swVlanPrecedencePortIndex": swVlanPrecedencePortIndex,
       "swVlanPrecedenceClassification": swVlanPrecedenceClassification,
       "swSubnetVLANTable": swSubnetVLANTable,
       "swSubnetVLANEntry": swSubnetVLANEntry,
       "swSubnetVLANIPAddress": swSubnetVLANIPAddress,
       "swSubnetVLANIPMask": swSubnetVLANIPMask,
       "swSubnetVLANID": swSubnetVLANID,
       "swSubnetVLANPriority": swSubnetVLANPriority,
       "swSubnetVLANRowStatus": swSubnetVLANRowStatus,
       "swSubnetVLANIPv6Table": swSubnetVLANIPv6Table,
       "swSubnetVLANIPv6Entry": swSubnetVLANIPv6Entry,
       "swSubnetVLANIPv6Address": swSubnetVLANIPv6Address,
       "swSubnetVLANIPv6PrefixLength": swSubnetVLANIPv6PrefixLength,
       "swSubnetVLANIPv6VID": swSubnetVLANIPv6VID,
       "swSubnetVLANIPv6Priority": swSubnetVLANIPv6Priority,
       "swSubnetVLANIPv6RowStatus": swSubnetVLANIPv6RowStatus}
)
