# SNMP MIB module (HPN-ICF-LswDHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-LswDHCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:53 2024
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

(hpnicflswCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicflswCommon")

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

hpnicfLswDhcpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8)
)
hpnicfLswDhcpMib.setRevisions(
        ("2001-06-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfLswDhcpMibObject_ObjectIdentity = ObjectIdentity
hpnicfLswDhcpMibObject = _HpnicfLswDhcpMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1)
)
_HpnicfDhcpGroupTable_Object = MibTable
hpnicfDhcpGroupTable = _HpnicfDhcpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfDhcpGroupTable.setStatus("current")
_HpnicfDhcpGroupEntry_Object = MibTableRow
hpnicfDhcpGroupEntry = _HpnicfDhcpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 1, 1)
)
hpnicfDhcpGroupEntry.setIndexNames(
    (0, "HPN-ICF-LswDHCP-MIB", "hpnicfDhcpGroupID"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpGroupEntry.setStatus("current")


class _HpnicfDhcpGroupID_Type(Integer32):
    """Custom type hpnicfDhcpGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_HpnicfDhcpGroupID_Type.__name__ = "Integer32"
_HpnicfDhcpGroupID_Object = MibTableColumn
hpnicfDhcpGroupID = _HpnicfDhcpGroupID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 1, 1, 1),
    _HpnicfDhcpGroupID_Type()
)
hpnicfDhcpGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpGroupID.setStatus("current")
_HpnicfIpDhcpServerAddress1_Type = IpAddress
_HpnicfIpDhcpServerAddress1_Object = MibTableColumn
hpnicfIpDhcpServerAddress1 = _HpnicfIpDhcpServerAddress1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 1, 1, 2),
    _HpnicfIpDhcpServerAddress1_Type()
)
hpnicfIpDhcpServerAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIpDhcpServerAddress1.setStatus("current")
_HpnicfIpDhcpServerAddress2_Type = IpAddress
_HpnicfIpDhcpServerAddress2_Object = MibTableColumn
hpnicfIpDhcpServerAddress2 = _HpnicfIpDhcpServerAddress2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 1, 1, 3),
    _HpnicfIpDhcpServerAddress2_Type()
)
hpnicfIpDhcpServerAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIpDhcpServerAddress2.setStatus("current")
_HpnicfDhcpRowStatus_Type = RowStatus
_HpnicfDhcpRowStatus_Object = MibTableColumn
hpnicfDhcpRowStatus = _HpnicfDhcpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 1, 1, 4),
    _HpnicfDhcpRowStatus_Type()
)
hpnicfDhcpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpRowStatus.setStatus("current")
_HpnicfDhcpSecurityTable_Object = MibTable
hpnicfDhcpSecurityTable = _HpnicfDhcpSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfDhcpSecurityTable.setStatus("current")
_HpnicfDhcpSecurityEntry_Object = MibTableRow
hpnicfDhcpSecurityEntry = _HpnicfDhcpSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 2, 1)
)
hpnicfDhcpSecurityEntry.setIndexNames(
    (0, "HPN-ICF-LswDHCP-MIB", "hpnicfDhcpClientIpAddress"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpSecurityEntry.setStatus("current")
_HpnicfDhcpClientIpAddress_Type = IpAddress
_HpnicfDhcpClientIpAddress_Object = MibTableColumn
hpnicfDhcpClientIpAddress = _HpnicfDhcpClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 2, 1, 1),
    _HpnicfDhcpClientIpAddress_Type()
)
hpnicfDhcpClientIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpClientIpAddress.setStatus("current")
_HpnicfDhcpClientMacAddress_Type = MacAddress
_HpnicfDhcpClientMacAddress_Object = MibTableColumn
hpnicfDhcpClientMacAddress = _HpnicfDhcpClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 2, 1, 2),
    _HpnicfDhcpClientMacAddress_Type()
)
hpnicfDhcpClientMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpClientMacAddress.setStatus("current")


class _HpnicfDhcpClientProperty_Type(Integer32):
    """Custom type hpnicfDhcpClientProperty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_HpnicfDhcpClientProperty_Type.__name__ = "Integer32"
_HpnicfDhcpClientProperty_Object = MibTableColumn
hpnicfDhcpClientProperty = _HpnicfDhcpClientProperty_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 2, 1, 3),
    _HpnicfDhcpClientProperty_Type()
)
hpnicfDhcpClientProperty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpClientProperty.setStatus("current")
_HpnicfDhcpClientRowStatus_Type = RowStatus
_HpnicfDhcpClientRowStatus_Object = MibTableColumn
hpnicfDhcpClientRowStatus = _HpnicfDhcpClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 2, 1, 4),
    _HpnicfDhcpClientRowStatus_Type()
)
hpnicfDhcpClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpClientRowStatus.setStatus("current")
_HpnicfDhcpToL3IfTable_Object = MibTable
hpnicfDhcpToL3IfTable = _HpnicfDhcpToL3IfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfDhcpToL3IfTable.setStatus("current")
_HpnicfDhcpToL3IfEntry_Object = MibTableRow
hpnicfDhcpToL3IfEntry = _HpnicfDhcpToL3IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 3, 1)
)
hpnicfDhcpToL3IfEntry.setIndexNames(
    (0, "HPN-ICF-LswDHCP-MIB", "hpnicfDhcpToL3VlanIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpToL3IfEntry.setStatus("current")
_HpnicfDhcpToL3VlanIfIndex_Type = Integer32
_HpnicfDhcpToL3VlanIfIndex_Object = MibTableColumn
hpnicfDhcpToL3VlanIfIndex = _HpnicfDhcpToL3VlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 3, 1, 1),
    _HpnicfDhcpToL3VlanIfIndex_Type()
)
hpnicfDhcpToL3VlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpToL3VlanIfIndex.setStatus("current")


class _HpnicfDhcpToL3GroupId_Type(Integer32):
    """Custom type hpnicfDhcpToL3GroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_HpnicfDhcpToL3GroupId_Type.__name__ = "Integer32"
_HpnicfDhcpToL3GroupId_Object = MibTableColumn
hpnicfDhcpToL3GroupId = _HpnicfDhcpToL3GroupId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 3, 1, 2),
    _HpnicfDhcpToL3GroupId_Type()
)
hpnicfDhcpToL3GroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpToL3GroupId.setStatus("current")


class _HpnicfDhcpToL3AddressCheck_Type(Integer32):
    """Custom type hpnicfDhcpToL3AddressCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpnicfDhcpToL3AddressCheck_Type.__name__ = "Integer32"
_HpnicfDhcpToL3AddressCheck_Object = MibTableColumn
hpnicfDhcpToL3AddressCheck = _HpnicfDhcpToL3AddressCheck_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 3, 1, 3),
    _HpnicfDhcpToL3AddressCheck_Type()
)
hpnicfDhcpToL3AddressCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpToL3AddressCheck.setStatus("current")
_HpnicfDhcpToL3RowStatus_Type = RowStatus
_HpnicfDhcpToL3RowStatus_Object = MibTableColumn
hpnicfDhcpToL3RowStatus = _HpnicfDhcpToL3RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 3, 1, 4),
    _HpnicfDhcpToL3RowStatus_Type()
)
hpnicfDhcpToL3RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpToL3RowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-LswDHCP-MIB",
    **{"hpnicfLswDhcpMib": hpnicfLswDhcpMib,
       "hpnicfLswDhcpMibObject": hpnicfLswDhcpMibObject,
       "hpnicfDhcpGroupTable": hpnicfDhcpGroupTable,
       "hpnicfDhcpGroupEntry": hpnicfDhcpGroupEntry,
       "hpnicfDhcpGroupID": hpnicfDhcpGroupID,
       "hpnicfIpDhcpServerAddress1": hpnicfIpDhcpServerAddress1,
       "hpnicfIpDhcpServerAddress2": hpnicfIpDhcpServerAddress2,
       "hpnicfDhcpRowStatus": hpnicfDhcpRowStatus,
       "hpnicfDhcpSecurityTable": hpnicfDhcpSecurityTable,
       "hpnicfDhcpSecurityEntry": hpnicfDhcpSecurityEntry,
       "hpnicfDhcpClientIpAddress": hpnicfDhcpClientIpAddress,
       "hpnicfDhcpClientMacAddress": hpnicfDhcpClientMacAddress,
       "hpnicfDhcpClientProperty": hpnicfDhcpClientProperty,
       "hpnicfDhcpClientRowStatus": hpnicfDhcpClientRowStatus,
       "hpnicfDhcpToL3IfTable": hpnicfDhcpToL3IfTable,
       "hpnicfDhcpToL3IfEntry": hpnicfDhcpToL3IfEntry,
       "hpnicfDhcpToL3VlanIfIndex": hpnicfDhcpToL3VlanIfIndex,
       "hpnicfDhcpToL3GroupId": hpnicfDhcpToL3GroupId,
       "hpnicfDhcpToL3AddressCheck": hpnicfDhcpToL3AddressCheck,
       "hpnicfDhcpToL3RowStatus": hpnicfDhcpToL3RowStatus}
)
