# SNMP MIB module (A3COM-HUAWEI-DHCPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-DHCPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:31 2024
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

(huaweiMgmt,
 hwDhcp) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "huaweiMgmt",
    "hwDhcp")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwDHCPServerMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )



# MIB Managed Objects in the order of their OIDs

_HwDHCPServerMibObject_ObjectIdentity = ObjectIdentity
hwDHCPServerMibObject = _HwDHCPServerMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1)
)
_HwDHCPSGlobalPoolTable_Object = MibTable
hwDHCPSGlobalPoolTable = _HwDHCPSGlobalPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolTable.setStatus("current")
_HwDHCPSGlobalPoolEntry_Object = MibTableRow
hwDHCPSGlobalPoolEntry = _HwDHCPSGlobalPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 1, 1)
)
hwDHCPSGlobalPoolEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolName"),
)
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolEntry.setStatus("current")


class _HwDHCPSGlobalPoolName_Type(OctetString):
    """Custom type hwDHCPSGlobalPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwDHCPSGlobalPoolName_Type.__name__ = "OctetString"
_HwDHCPSGlobalPoolName_Object = MibTableColumn
hwDHCPSGlobalPoolName = _HwDHCPSGlobalPoolName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 1, 1, 1),
    _HwDHCPSGlobalPoolName_Type()
)
hwDHCPSGlobalPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolName.setStatus("current")
_HwDHCPSGlobalPoolRowStatus_Type = RowStatus
_HwDHCPSGlobalPoolRowStatus_Object = MibTableColumn
hwDHCPSGlobalPoolRowStatus = _HwDHCPSGlobalPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 1, 1, 2),
    _HwDHCPSGlobalPoolRowStatus_Type()
)
hwDHCPSGlobalPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolRowStatus.setStatus("current")
_HwDHCPSGlobalPoolConfigTable_Object = MibTable
hwDHCPSGlobalPoolConfigTable = _HwDHCPSGlobalPoolConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolConfigTable.setStatus("current")
_HwDHCPSGlobalPoolConfigEntry_Object = MibTableRow
hwDHCPSGlobalPoolConfigEntry = _HwDHCPSGlobalPoolConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 2, 1)
)
hwDHCPSGlobalPoolConfigEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolName"),
)
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolConfigEntry.setStatus("current")


class _HwDHCPSGlobalPoolType_Type(Integer32):
    """Custom type hwDHCPSGlobalPoolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("network", 2),
          ("null", 0))
    )


_HwDHCPSGlobalPoolType_Type.__name__ = "Integer32"
_HwDHCPSGlobalPoolType_Object = MibTableColumn
hwDHCPSGlobalPoolType = _HwDHCPSGlobalPoolType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 2, 1, 1),
    _HwDHCPSGlobalPoolType_Type()
)
hwDHCPSGlobalPoolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolType.setStatus("current")
_HwDHCPSGlobalPoolNetwork_Type = IpAddress
_HwDHCPSGlobalPoolNetwork_Object = MibTableColumn
hwDHCPSGlobalPoolNetwork = _HwDHCPSGlobalPoolNetwork_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 2, 1, 2),
    _HwDHCPSGlobalPoolNetwork_Type()
)
hwDHCPSGlobalPoolNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolNetwork.setStatus("current")
_HwDHCPSGlobalPoolNetworkMask_Type = IpAddress
_HwDHCPSGlobalPoolNetworkMask_Object = MibTableColumn
hwDHCPSGlobalPoolNetworkMask = _HwDHCPSGlobalPoolNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 2, 1, 3),
    _HwDHCPSGlobalPoolNetworkMask_Type()
)
hwDHCPSGlobalPoolNetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolNetworkMask.setStatus("current")
_HwDHCPSGlobalPoolHostIPAddr_Type = IpAddress
_HwDHCPSGlobalPoolHostIPAddr_Object = MibTableColumn
hwDHCPSGlobalPoolHostIPAddr = _HwDHCPSGlobalPoolHostIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 2, 1, 4),
    _HwDHCPSGlobalPoolHostIPAddr_Type()
)
hwDHCPSGlobalPoolHostIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolHostIPAddr.setStatus("current")
_HwDHCPSGlobalPoolHostMask_Type = IpAddress
_HwDHCPSGlobalPoolHostMask_Object = MibTableColumn
hwDHCPSGlobalPoolHostMask = _HwDHCPSGlobalPoolHostMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 2, 1, 5),
    _HwDHCPSGlobalPoolHostMask_Type()
)
hwDHCPSGlobalPoolHostMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolHostMask.setStatus("current")
_HwDHCPSGlobalPoolHostHAddr_Type = MacAddress
_HwDHCPSGlobalPoolHostHAddr_Object = MibTableColumn
hwDHCPSGlobalPoolHostHAddr = _HwDHCPSGlobalPoolHostHAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 2, 1, 6),
    _HwDHCPSGlobalPoolHostHAddr_Type()
)
hwDHCPSGlobalPoolHostHAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolHostHAddr.setStatus("current")


class _HwDHCPSGlobalPoolConfigUndoFlag_Type(Integer32):
    """Custom type hwDHCPSGlobalPoolConfigUndoFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undohosthaddr", 3),
          ("undohostip", 2),
          ("undonetworkip", 1))
    )


_HwDHCPSGlobalPoolConfigUndoFlag_Type.__name__ = "Integer32"
_HwDHCPSGlobalPoolConfigUndoFlag_Object = MibTableColumn
hwDHCPSGlobalPoolConfigUndoFlag = _HwDHCPSGlobalPoolConfigUndoFlag_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 2, 1, 7),
    _HwDHCPSGlobalPoolConfigUndoFlag_Type()
)
hwDHCPSGlobalPoolConfigUndoFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolConfigUndoFlag.setStatus("current")
_HwDHCPSGlobalPoolParaTable_Object = MibTable
hwDHCPSGlobalPoolParaTable = _HwDHCPSGlobalPoolParaTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolParaTable.setStatus("current")
_HwDHCPSGlobalPoolParaEntry_Object = MibTableRow
hwDHCPSGlobalPoolParaEntry = _HwDHCPSGlobalPoolParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 3, 1)
)
hwDHCPSGlobalPoolParaEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolName"),
)
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolParaEntry.setStatus("current")


class _HwDHCPSGlobalPoolLeaseDay_Type(Integer32):
    """Custom type hwDHCPSGlobalPoolLeaseDay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_HwDHCPSGlobalPoolLeaseDay_Type.__name__ = "Integer32"
_HwDHCPSGlobalPoolLeaseDay_Object = MibTableColumn
hwDHCPSGlobalPoolLeaseDay = _HwDHCPSGlobalPoolLeaseDay_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 3, 1, 1),
    _HwDHCPSGlobalPoolLeaseDay_Type()
)
hwDHCPSGlobalPoolLeaseDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolLeaseDay.setStatus("current")


class _HwDHCPSGlobalPoolLeaseHour_Type(Integer32):
    """Custom type hwDHCPSGlobalPoolLeaseHour based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_HwDHCPSGlobalPoolLeaseHour_Type.__name__ = "Integer32"
_HwDHCPSGlobalPoolLeaseHour_Object = MibTableColumn
hwDHCPSGlobalPoolLeaseHour = _HwDHCPSGlobalPoolLeaseHour_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 3, 1, 2),
    _HwDHCPSGlobalPoolLeaseHour_Type()
)
hwDHCPSGlobalPoolLeaseHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolLeaseHour.setStatus("current")


class _HwDHCPSGlobalPoolLeaseMinute_Type(Integer32):
    """Custom type hwDHCPSGlobalPoolLeaseMinute based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_HwDHCPSGlobalPoolLeaseMinute_Type.__name__ = "Integer32"
_HwDHCPSGlobalPoolLeaseMinute_Object = MibTableColumn
hwDHCPSGlobalPoolLeaseMinute = _HwDHCPSGlobalPoolLeaseMinute_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 3, 1, 3),
    _HwDHCPSGlobalPoolLeaseMinute_Type()
)
hwDHCPSGlobalPoolLeaseMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolLeaseMinute.setStatus("current")


class _HwDHCPSGlobalPoolLeaseUnlimited_Type(Integer32):
    """Custom type hwDHCPSGlobalPoolLeaseUnlimited based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("unlimited", 1))
    )


_HwDHCPSGlobalPoolLeaseUnlimited_Type.__name__ = "Integer32"
_HwDHCPSGlobalPoolLeaseUnlimited_Object = MibTableColumn
hwDHCPSGlobalPoolLeaseUnlimited = _HwDHCPSGlobalPoolLeaseUnlimited_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 3, 1, 4),
    _HwDHCPSGlobalPoolLeaseUnlimited_Type()
)
hwDHCPSGlobalPoolLeaseUnlimited.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolLeaseUnlimited.setStatus("current")


class _HwDHCPSGlobalPoolDomainName_Type(OctetString):
    """Custom type hwDHCPSGlobalPoolDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwDHCPSGlobalPoolDomainName_Type.__name__ = "OctetString"
_HwDHCPSGlobalPoolDomainName_Object = MibTableColumn
hwDHCPSGlobalPoolDomainName = _HwDHCPSGlobalPoolDomainName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 3, 1, 5),
    _HwDHCPSGlobalPoolDomainName_Type()
)
hwDHCPSGlobalPoolDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolDomainName.setStatus("current")


class _HwDHCPSGlobalPoolClientGatewayIPString_Type(OctetString):
    """Custom type hwDHCPSGlobalPoolClientGatewayIPString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_HwDHCPSGlobalPoolClientGatewayIPString_Type.__name__ = "OctetString"
_HwDHCPSGlobalPoolClientGatewayIPString_Object = MibTableColumn
hwDHCPSGlobalPoolClientGatewayIPString = _HwDHCPSGlobalPoolClientGatewayIPString_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 3, 1, 6),
    _HwDHCPSGlobalPoolClientGatewayIPString_Type()
)
hwDHCPSGlobalPoolClientGatewayIPString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolClientGatewayIPString.setStatus("current")
_HwDHCPSGlobalPoolClientGatewayIPUndo_Type = IpAddress
_HwDHCPSGlobalPoolClientGatewayIPUndo_Object = MibTableColumn
hwDHCPSGlobalPoolClientGatewayIPUndo = _HwDHCPSGlobalPoolClientGatewayIPUndo_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 3, 1, 7),
    _HwDHCPSGlobalPoolClientGatewayIPUndo_Type()
)
hwDHCPSGlobalPoolClientGatewayIPUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolClientGatewayIPUndo.setStatus("current")


class _HwDHCPSGlobalPoolClientDNSIPString_Type(OctetString):
    """Custom type hwDHCPSGlobalPoolClientDNSIPString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_HwDHCPSGlobalPoolClientDNSIPString_Type.__name__ = "OctetString"
_HwDHCPSGlobalPoolClientDNSIPString_Object = MibTableColumn
hwDHCPSGlobalPoolClientDNSIPString = _HwDHCPSGlobalPoolClientDNSIPString_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 3, 1, 8),
    _HwDHCPSGlobalPoolClientDNSIPString_Type()
)
hwDHCPSGlobalPoolClientDNSIPString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolClientDNSIPString.setStatus("current")
_HwDHCPSGlobalPoolClientDNSIPUndo_Type = IpAddress
_HwDHCPSGlobalPoolClientDNSIPUndo_Object = MibTableColumn
hwDHCPSGlobalPoolClientDNSIPUndo = _HwDHCPSGlobalPoolClientDNSIPUndo_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 3, 1, 9),
    _HwDHCPSGlobalPoolClientDNSIPUndo_Type()
)
hwDHCPSGlobalPoolClientDNSIPUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolClientDNSIPUndo.setStatus("current")


class _HwDHCPSGlobalPoolClientNetbiosType_Type(Integer32):
    """Custom type hwDHCPSGlobalPoolClientNetbiosType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("bnode", 1),
          ("hnode", 8),
          ("mnode", 4),
          ("null", 0),
          ("pnode", 2))
    )


_HwDHCPSGlobalPoolClientNetbiosType_Type.__name__ = "Integer32"
_HwDHCPSGlobalPoolClientNetbiosType_Object = MibTableColumn
hwDHCPSGlobalPoolClientNetbiosType = _HwDHCPSGlobalPoolClientNetbiosType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 3, 1, 10),
    _HwDHCPSGlobalPoolClientNetbiosType_Type()
)
hwDHCPSGlobalPoolClientNetbiosType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolClientNetbiosType.setStatus("current")


class _HwDHCPSGlobalPoolClientNbnsIPString_Type(OctetString):
    """Custom type hwDHCPSGlobalPoolClientNbnsIPString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_HwDHCPSGlobalPoolClientNbnsIPString_Type.__name__ = "OctetString"
_HwDHCPSGlobalPoolClientNbnsIPString_Object = MibTableColumn
hwDHCPSGlobalPoolClientNbnsIPString = _HwDHCPSGlobalPoolClientNbnsIPString_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 3, 1, 11),
    _HwDHCPSGlobalPoolClientNbnsIPString_Type()
)
hwDHCPSGlobalPoolClientNbnsIPString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolClientNbnsIPString.setStatus("current")
_HwDHCPSGlobalPoolClientNbnsIPUndo_Type = IpAddress
_HwDHCPSGlobalPoolClientNbnsIPUndo_Object = MibTableColumn
hwDHCPSGlobalPoolClientNbnsIPUndo = _HwDHCPSGlobalPoolClientNbnsIPUndo_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 3, 1, 12),
    _HwDHCPSGlobalPoolClientNbnsIPUndo_Type()
)
hwDHCPSGlobalPoolClientNbnsIPUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolClientNbnsIPUndo.setStatus("current")


class _HwDHCPSGlobalPoolParaUndoFlag_Type(Integer32):
    """Custom type hwDHCPSGlobalPoolParaUndoFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("undoDns", 4),
          ("undoDomain", 1),
          ("undoGateway", 3),
          ("undoLease", 2),
          ("undoNbType", 6),
          ("undoNbns", 5))
    )


_HwDHCPSGlobalPoolParaUndoFlag_Type.__name__ = "Integer32"
_HwDHCPSGlobalPoolParaUndoFlag_Object = MibTableColumn
hwDHCPSGlobalPoolParaUndoFlag = _HwDHCPSGlobalPoolParaUndoFlag_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 3, 1, 13),
    _HwDHCPSGlobalPoolParaUndoFlag_Type()
)
hwDHCPSGlobalPoolParaUndoFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolParaUndoFlag.setStatus("current")


class _HwDHCPSGlobalPoolIPInUseReset_Type(Integer32):
    """Custom type hwDHCPSGlobalPoolIPInUseReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HwDHCPSGlobalPoolIPInUseReset_Type.__name__ = "Integer32"
_HwDHCPSGlobalPoolIPInUseReset_Object = MibTableColumn
hwDHCPSGlobalPoolIPInUseReset = _HwDHCPSGlobalPoolIPInUseReset_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 3, 1, 14),
    _HwDHCPSGlobalPoolIPInUseReset_Type()
)
hwDHCPSGlobalPoolIPInUseReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolIPInUseReset.setStatus("current")
_HwDHCPSGlobalPoolOptionTable_Object = MibTable
hwDHCPSGlobalPoolOptionTable = _HwDHCPSGlobalPoolOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolOptionTable.setStatus("current")
_HwDHCPSGlobalPoolOptionEntry_Object = MibTableRow
hwDHCPSGlobalPoolOptionEntry = _HwDHCPSGlobalPoolOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 4, 1)
)
hwDHCPSGlobalPoolOptionEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolName"),
    (0, "A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolOptionCode"),
)
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolOptionEntry.setStatus("current")


class _HwDHCPSGlobalPoolOptionCode_Type(Integer32):
    """Custom type hwDHCPSGlobalPoolOptionCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_HwDHCPSGlobalPoolOptionCode_Type.__name__ = "Integer32"
_HwDHCPSGlobalPoolOptionCode_Object = MibTableColumn
hwDHCPSGlobalPoolOptionCode = _HwDHCPSGlobalPoolOptionCode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 4, 1, 1),
    _HwDHCPSGlobalPoolOptionCode_Type()
)
hwDHCPSGlobalPoolOptionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolOptionCode.setStatus("current")


class _HwDHCPSGlobalPoolOptionType_Type(Integer32):
    """Custom type hwDHCPSGlobalPoolOptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("hex", 2),
          ("ip", 3))
    )


_HwDHCPSGlobalPoolOptionType_Type.__name__ = "Integer32"
_HwDHCPSGlobalPoolOptionType_Object = MibTableColumn
hwDHCPSGlobalPoolOptionType = _HwDHCPSGlobalPoolOptionType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 4, 1, 2),
    _HwDHCPSGlobalPoolOptionType_Type()
)
hwDHCPSGlobalPoolOptionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolOptionType.setStatus("current")


class _HwDHCPSGlobalPoolOptionAscii_Type(OctetString):
    """Custom type hwDHCPSGlobalPoolOptionAscii based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwDHCPSGlobalPoolOptionAscii_Type.__name__ = "OctetString"
_HwDHCPSGlobalPoolOptionAscii_Object = MibTableColumn
hwDHCPSGlobalPoolOptionAscii = _HwDHCPSGlobalPoolOptionAscii_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 4, 1, 3),
    _HwDHCPSGlobalPoolOptionAscii_Type()
)
hwDHCPSGlobalPoolOptionAscii.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolOptionAscii.setStatus("current")


class _HwDHCPSGlobalPoolOptionHexString_Type(OctetString):
    """Custom type hwDHCPSGlobalPoolOptionHexString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 143),
    )


_HwDHCPSGlobalPoolOptionHexString_Type.__name__ = "OctetString"
_HwDHCPSGlobalPoolOptionHexString_Object = MibTableColumn
hwDHCPSGlobalPoolOptionHexString = _HwDHCPSGlobalPoolOptionHexString_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 4, 1, 4),
    _HwDHCPSGlobalPoolOptionHexString_Type()
)
hwDHCPSGlobalPoolOptionHexString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolOptionHexString.setStatus("current")


class _HwDHCPSGlobalPoolOptionIPString_Type(OctetString):
    """Custom type hwDHCPSGlobalPoolOptionIPString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_HwDHCPSGlobalPoolOptionIPString_Type.__name__ = "OctetString"
_HwDHCPSGlobalPoolOptionIPString_Object = MibTableColumn
hwDHCPSGlobalPoolOptionIPString = _HwDHCPSGlobalPoolOptionIPString_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 4, 1, 5),
    _HwDHCPSGlobalPoolOptionIPString_Type()
)
hwDHCPSGlobalPoolOptionIPString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolOptionIPString.setStatus("current")
_HwDHCPSGlobalPoolOptionRowStatus_Type = RowStatus
_HwDHCPSGlobalPoolOptionRowStatus_Object = MibTableColumn
hwDHCPSGlobalPoolOptionRowStatus = _HwDHCPSGlobalPoolOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 4, 1, 6),
    _HwDHCPSGlobalPoolOptionRowStatus_Type()
)
hwDHCPSGlobalPoolOptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolOptionRowStatus.setStatus("current")
_HwDHCPSGlobalTreeTable_Object = MibTable
hwDHCPSGlobalTreeTable = _HwDHCPSGlobalTreeTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 5)
)
if mibBuilder.loadTexts:
    hwDHCPSGlobalTreeTable.setStatus("current")
_HwDHCPSGlobalTreeEntry_Object = MibTableRow
hwDHCPSGlobalTreeEntry = _HwDHCPSGlobalTreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 5, 1)
)
hwDHCPSGlobalTreeEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolName"),
)
if mibBuilder.loadTexts:
    hwDHCPSGlobalTreeEntry.setStatus("current")


class _HwDHCPSGlobalTreeParentNodeName_Type(OctetString):
    """Custom type hwDHCPSGlobalTreeParentNodeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwDHCPSGlobalTreeParentNodeName_Type.__name__ = "OctetString"
_HwDHCPSGlobalTreeParentNodeName_Object = MibTableColumn
hwDHCPSGlobalTreeParentNodeName = _HwDHCPSGlobalTreeParentNodeName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 5, 1, 1),
    _HwDHCPSGlobalTreeParentNodeName_Type()
)
hwDHCPSGlobalTreeParentNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSGlobalTreeParentNodeName.setStatus("current")


class _HwDHCPSGlobalTreeChildNodeName_Type(OctetString):
    """Custom type hwDHCPSGlobalTreeChildNodeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwDHCPSGlobalTreeChildNodeName_Type.__name__ = "OctetString"
_HwDHCPSGlobalTreeChildNodeName_Object = MibTableColumn
hwDHCPSGlobalTreeChildNodeName = _HwDHCPSGlobalTreeChildNodeName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 5, 1, 2),
    _HwDHCPSGlobalTreeChildNodeName_Type()
)
hwDHCPSGlobalTreeChildNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSGlobalTreeChildNodeName.setStatus("current")


class _HwDHCPSGlobalTreePreSiblingNodeName_Type(OctetString):
    """Custom type hwDHCPSGlobalTreePreSiblingNodeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwDHCPSGlobalTreePreSiblingNodeName_Type.__name__ = "OctetString"
_HwDHCPSGlobalTreePreSiblingNodeName_Object = MibTableColumn
hwDHCPSGlobalTreePreSiblingNodeName = _HwDHCPSGlobalTreePreSiblingNodeName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 5, 1, 3),
    _HwDHCPSGlobalTreePreSiblingNodeName_Type()
)
hwDHCPSGlobalTreePreSiblingNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSGlobalTreePreSiblingNodeName.setStatus("current")


class _HwDHCPSGlobalTreeSiblingNodeName_Type(OctetString):
    """Custom type hwDHCPSGlobalTreeSiblingNodeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwDHCPSGlobalTreeSiblingNodeName_Type.__name__ = "OctetString"
_HwDHCPSGlobalTreeSiblingNodeName_Object = MibTableColumn
hwDHCPSGlobalTreeSiblingNodeName = _HwDHCPSGlobalTreeSiblingNodeName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 5, 1, 4),
    _HwDHCPSGlobalTreeSiblingNodeName_Type()
)
hwDHCPSGlobalTreeSiblingNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSGlobalTreeSiblingNodeName.setStatus("current")
_HwDHCPSInterfacePoolParaTable_Object = MibTable
hwDHCPSInterfacePoolParaTable = _HwDHCPSInterfacePoolParaTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 6)
)
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolParaTable.setStatus("current")
_HwDHCPSInterfacePoolParaEntry_Object = MibTableRow
hwDHCPSInterfacePoolParaEntry = _HwDHCPSInterfacePoolParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 6, 1)
)
hwDHCPSInterfacePoolParaEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolParaEntry.setStatus("current")


class _HwDHCPSInterfacePoolLeaseDay_Type(Integer32):
    """Custom type hwDHCPSInterfacePoolLeaseDay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_HwDHCPSInterfacePoolLeaseDay_Type.__name__ = "Integer32"
_HwDHCPSInterfacePoolLeaseDay_Object = MibTableColumn
hwDHCPSInterfacePoolLeaseDay = _HwDHCPSInterfacePoolLeaseDay_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 6, 1, 1),
    _HwDHCPSInterfacePoolLeaseDay_Type()
)
hwDHCPSInterfacePoolLeaseDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolLeaseDay.setStatus("current")


class _HwDHCPSInterfacePoolLeaseHour_Type(Integer32):
    """Custom type hwDHCPSInterfacePoolLeaseHour based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_HwDHCPSInterfacePoolLeaseHour_Type.__name__ = "Integer32"
_HwDHCPSInterfacePoolLeaseHour_Object = MibTableColumn
hwDHCPSInterfacePoolLeaseHour = _HwDHCPSInterfacePoolLeaseHour_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 6, 1, 2),
    _HwDHCPSInterfacePoolLeaseHour_Type()
)
hwDHCPSInterfacePoolLeaseHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolLeaseHour.setStatus("current")


class _HwDHCPSInterfacePoolLeaseMinute_Type(Integer32):
    """Custom type hwDHCPSInterfacePoolLeaseMinute based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_HwDHCPSInterfacePoolLeaseMinute_Type.__name__ = "Integer32"
_HwDHCPSInterfacePoolLeaseMinute_Object = MibTableColumn
hwDHCPSInterfacePoolLeaseMinute = _HwDHCPSInterfacePoolLeaseMinute_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 6, 1, 3),
    _HwDHCPSInterfacePoolLeaseMinute_Type()
)
hwDHCPSInterfacePoolLeaseMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolLeaseMinute.setStatus("current")


class _HwDHCPSInterfacePoolLeaseUnlimited_Type(Integer32):
    """Custom type hwDHCPSInterfacePoolLeaseUnlimited based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("unlimited", 1))
    )


_HwDHCPSInterfacePoolLeaseUnlimited_Type.__name__ = "Integer32"
_HwDHCPSInterfacePoolLeaseUnlimited_Object = MibTableColumn
hwDHCPSInterfacePoolLeaseUnlimited = _HwDHCPSInterfacePoolLeaseUnlimited_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 6, 1, 4),
    _HwDHCPSInterfacePoolLeaseUnlimited_Type()
)
hwDHCPSInterfacePoolLeaseUnlimited.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolLeaseUnlimited.setStatus("current")


class _HwDHCPSInterfacePoolDomainName_Type(OctetString):
    """Custom type hwDHCPSInterfacePoolDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwDHCPSInterfacePoolDomainName_Type.__name__ = "OctetString"
_HwDHCPSInterfacePoolDomainName_Object = MibTableColumn
hwDHCPSInterfacePoolDomainName = _HwDHCPSInterfacePoolDomainName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 6, 1, 5),
    _HwDHCPSInterfacePoolDomainName_Type()
)
hwDHCPSInterfacePoolDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolDomainName.setStatus("current")


class _HwDHCPSInterfacePoolClientDNSIPString_Type(OctetString):
    """Custom type hwDHCPSInterfacePoolClientDNSIPString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_HwDHCPSInterfacePoolClientDNSIPString_Type.__name__ = "OctetString"
_HwDHCPSInterfacePoolClientDNSIPString_Object = MibTableColumn
hwDHCPSInterfacePoolClientDNSIPString = _HwDHCPSInterfacePoolClientDNSIPString_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 6, 1, 6),
    _HwDHCPSInterfacePoolClientDNSIPString_Type()
)
hwDHCPSInterfacePoolClientDNSIPString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolClientDNSIPString.setStatus("current")
_HwDHCPSInterfacePoolClientDNSIPUndo_Type = IpAddress
_HwDHCPSInterfacePoolClientDNSIPUndo_Object = MibTableColumn
hwDHCPSInterfacePoolClientDNSIPUndo = _HwDHCPSInterfacePoolClientDNSIPUndo_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 6, 1, 7),
    _HwDHCPSInterfacePoolClientDNSIPUndo_Type()
)
hwDHCPSInterfacePoolClientDNSIPUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolClientDNSIPUndo.setStatus("current")


class _HwDHCPSInterfacePoolClientNetbiosType_Type(Integer32):
    """Custom type hwDHCPSInterfacePoolClientNetbiosType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("bnode", 1),
          ("hnode", 8),
          ("mnode", 4),
          ("null", 0),
          ("pnode", 2))
    )


_HwDHCPSInterfacePoolClientNetbiosType_Type.__name__ = "Integer32"
_HwDHCPSInterfacePoolClientNetbiosType_Object = MibTableColumn
hwDHCPSInterfacePoolClientNetbiosType = _HwDHCPSInterfacePoolClientNetbiosType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 6, 1, 8),
    _HwDHCPSInterfacePoolClientNetbiosType_Type()
)
hwDHCPSInterfacePoolClientNetbiosType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolClientNetbiosType.setStatus("current")


class _HwDHCPSInterfacePoolClientNbnsIPString_Type(OctetString):
    """Custom type hwDHCPSInterfacePoolClientNbnsIPString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_HwDHCPSInterfacePoolClientNbnsIPString_Type.__name__ = "OctetString"
_HwDHCPSInterfacePoolClientNbnsIPString_Object = MibTableColumn
hwDHCPSInterfacePoolClientNbnsIPString = _HwDHCPSInterfacePoolClientNbnsIPString_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 6, 1, 9),
    _HwDHCPSInterfacePoolClientNbnsIPString_Type()
)
hwDHCPSInterfacePoolClientNbnsIPString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolClientNbnsIPString.setStatus("current")
_HwDHCPSInterfacePoolClientNbnsIPUndo_Type = IpAddress
_HwDHCPSInterfacePoolClientNbnsIPUndo_Object = MibTableColumn
hwDHCPSInterfacePoolClientNbnsIPUndo = _HwDHCPSInterfacePoolClientNbnsIPUndo_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 6, 1, 10),
    _HwDHCPSInterfacePoolClientNbnsIPUndo_Type()
)
hwDHCPSInterfacePoolClientNbnsIPUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolClientNbnsIPUndo.setStatus("current")


class _HwDHCPSInterfacePoolParaUndoFlag_Type(Integer32):
    """Custom type hwDHCPSInterfacePoolParaUndoFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("undoDns", 4),
          ("undoDomain", 1),
          ("undoLease", 2),
          ("undoNbType", 6),
          ("undoNbns", 5))
    )


_HwDHCPSInterfacePoolParaUndoFlag_Type.__name__ = "Integer32"
_HwDHCPSInterfacePoolParaUndoFlag_Object = MibTableColumn
hwDHCPSInterfacePoolParaUndoFlag = _HwDHCPSInterfacePoolParaUndoFlag_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 6, 1, 11),
    _HwDHCPSInterfacePoolParaUndoFlag_Type()
)
hwDHCPSInterfacePoolParaUndoFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolParaUndoFlag.setStatus("current")


class _HwDHCPSInterfacePoolIPInUseReset_Type(Integer32):
    """Custom type hwDHCPSInterfacePoolIPInUseReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HwDHCPSInterfacePoolIPInUseReset_Type.__name__ = "Integer32"
_HwDHCPSInterfacePoolIPInUseReset_Object = MibTableColumn
hwDHCPSInterfacePoolIPInUseReset = _HwDHCPSInterfacePoolIPInUseReset_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 6, 1, 12),
    _HwDHCPSInterfacePoolIPInUseReset_Type()
)
hwDHCPSInterfacePoolIPInUseReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolIPInUseReset.setStatus("current")
_HwDHCPSInterfacePoolOptionTable_Object = MibTable
hwDHCPSInterfacePoolOptionTable = _HwDHCPSInterfacePoolOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 7)
)
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolOptionTable.setStatus("current")
_HwDHCPSInterfacePoolOptionEntry_Object = MibTableRow
hwDHCPSInterfacePoolOptionEntry = _HwDHCPSInterfacePoolOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 7, 1)
)
hwDHCPSInterfacePoolOptionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSInterfacePoolOptionCode"),
)
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolOptionEntry.setStatus("current")


class _HwDHCPSInterfacePoolOptionCode_Type(Integer32):
    """Custom type hwDHCPSInterfacePoolOptionCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_HwDHCPSInterfacePoolOptionCode_Type.__name__ = "Integer32"
_HwDHCPSInterfacePoolOptionCode_Object = MibTableColumn
hwDHCPSInterfacePoolOptionCode = _HwDHCPSInterfacePoolOptionCode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 7, 1, 1),
    _HwDHCPSInterfacePoolOptionCode_Type()
)
hwDHCPSInterfacePoolOptionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolOptionCode.setStatus("current")


class _HwDHCPSInterfacePoolOptionType_Type(Integer32):
    """Custom type hwDHCPSInterfacePoolOptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("hex", 2),
          ("ip", 3))
    )


_HwDHCPSInterfacePoolOptionType_Type.__name__ = "Integer32"
_HwDHCPSInterfacePoolOptionType_Object = MibTableColumn
hwDHCPSInterfacePoolOptionType = _HwDHCPSInterfacePoolOptionType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 7, 1, 2),
    _HwDHCPSInterfacePoolOptionType_Type()
)
hwDHCPSInterfacePoolOptionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolOptionType.setStatus("current")


class _HwDHCPSInterfacePoolOptionAscii_Type(OctetString):
    """Custom type hwDHCPSInterfacePoolOptionAscii based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwDHCPSInterfacePoolOptionAscii_Type.__name__ = "OctetString"
_HwDHCPSInterfacePoolOptionAscii_Object = MibTableColumn
hwDHCPSInterfacePoolOptionAscii = _HwDHCPSInterfacePoolOptionAscii_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 7, 1, 3),
    _HwDHCPSInterfacePoolOptionAscii_Type()
)
hwDHCPSInterfacePoolOptionAscii.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolOptionAscii.setStatus("current")


class _HwDHCPSInterfacePoolOptionHexString_Type(OctetString):
    """Custom type hwDHCPSInterfacePoolOptionHexString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 143),
    )


_HwDHCPSInterfacePoolOptionHexString_Type.__name__ = "OctetString"
_HwDHCPSInterfacePoolOptionHexString_Object = MibTableColumn
hwDHCPSInterfacePoolOptionHexString = _HwDHCPSInterfacePoolOptionHexString_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 7, 1, 4),
    _HwDHCPSInterfacePoolOptionHexString_Type()
)
hwDHCPSInterfacePoolOptionHexString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolOptionHexString.setStatus("current")


class _HwDHCPSInterfacePoolOptionIPString_Type(OctetString):
    """Custom type hwDHCPSInterfacePoolOptionIPString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_HwDHCPSInterfacePoolOptionIPString_Type.__name__ = "OctetString"
_HwDHCPSInterfacePoolOptionIPString_Object = MibTableColumn
hwDHCPSInterfacePoolOptionIPString = _HwDHCPSInterfacePoolOptionIPString_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 7, 1, 5),
    _HwDHCPSInterfacePoolOptionIPString_Type()
)
hwDHCPSInterfacePoolOptionIPString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolOptionIPString.setStatus("current")
_HwDHCPSInterfacePoolOptionRowStatus_Type = RowStatus
_HwDHCPSInterfacePoolOptionRowStatus_Object = MibTableColumn
hwDHCPSInterfacePoolOptionRowStatus = _HwDHCPSInterfacePoolOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 7, 1, 6),
    _HwDHCPSInterfacePoolOptionRowStatus_Type()
)
hwDHCPSInterfacePoolOptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolOptionRowStatus.setStatus("current")
_HwDHCPSInterfacePoolStaticBindTable_Object = MibTable
hwDHCPSInterfacePoolStaticBindTable = _HwDHCPSInterfacePoolStaticBindTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 8)
)
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolStaticBindTable.setStatus("current")
_HwDHCPSInterfacePoolStaticBindEntry_Object = MibTableRow
hwDHCPSInterfacePoolStaticBindEntry = _HwDHCPSInterfacePoolStaticBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 8, 1)
)
hwDHCPSInterfacePoolStaticBindEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSInterfacePoolStaticBindIP"),
)
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolStaticBindEntry.setStatus("current")
_HwDHCPSInterfacePoolStaticBindIP_Type = IpAddress
_HwDHCPSInterfacePoolStaticBindIP_Object = MibTableColumn
hwDHCPSInterfacePoolStaticBindIP = _HwDHCPSInterfacePoolStaticBindIP_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 8, 1, 1),
    _HwDHCPSInterfacePoolStaticBindIP_Type()
)
hwDHCPSInterfacePoolStaticBindIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolStaticBindIP.setStatus("current")
_HwDHCPSInterfacePoolStaticBindMac_Type = MacAddress
_HwDHCPSInterfacePoolStaticBindMac_Object = MibTableColumn
hwDHCPSInterfacePoolStaticBindMac = _HwDHCPSInterfacePoolStaticBindMac_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 8, 1, 2),
    _HwDHCPSInterfacePoolStaticBindMac_Type()
)
hwDHCPSInterfacePoolStaticBindMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolStaticBindMac.setStatus("current")
_HwDHCPSInterfacePoolStaticBindRowStatus_Type = RowStatus
_HwDHCPSInterfacePoolStaticBindRowStatus_Object = MibTableColumn
hwDHCPSInterfacePoolStaticBindRowStatus = _HwDHCPSInterfacePoolStaticBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 8, 1, 3),
    _HwDHCPSInterfacePoolStaticBindRowStatus_Type()
)
hwDHCPSInterfacePoolStaticBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolStaticBindRowStatus.setStatus("current")
_HwDHCPSIPInUseTable_Object = MibTable
hwDHCPSIPInUseTable = _HwDHCPSIPInUseTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 9)
)
if mibBuilder.loadTexts:
    hwDHCPSIPInUseTable.setStatus("deprecated")
_HwDHCPSIPInUseEntry_Object = MibTableRow
hwDHCPSIPInUseEntry = _HwDHCPSIPInUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 9, 1)
)
hwDHCPSIPInUseEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSIPInUseHAddr"),
)
if mibBuilder.loadTexts:
    hwDHCPSIPInUseEntry.setStatus("deprecated")
_HwDHCPSIPInUseHAddr_Type = MacAddress
_HwDHCPSIPInUseHAddr_Object = MibTableColumn
hwDHCPSIPInUseHAddr = _HwDHCPSIPInUseHAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 9, 1, 1),
    _HwDHCPSIPInUseHAddr_Type()
)
hwDHCPSIPInUseHAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSIPInUseHAddr.setStatus("deprecated")
_HwDHCPSIPInUseIP_Type = IpAddress
_HwDHCPSIPInUseIP_Object = MibTableColumn
hwDHCPSIPInUseIP = _HwDHCPSIPInUseIP_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 9, 1, 2),
    _HwDHCPSIPInUseIP_Type()
)
hwDHCPSIPInUseIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSIPInUseIP.setStatus("deprecated")


class _HwDHCPSIPInUseEndLease_Type(OctetString):
    """Custom type hwDHCPSIPInUseEndLease based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_HwDHCPSIPInUseEndLease_Type.__name__ = "OctetString"
_HwDHCPSIPInUseEndLease_Object = MibTableColumn
hwDHCPSIPInUseEndLease = _HwDHCPSIPInUseEndLease_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 9, 1, 3),
    _HwDHCPSIPInUseEndLease_Type()
)
hwDHCPSIPInUseEndLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSIPInUseEndLease.setStatus("deprecated")


class _HwDHCPSIPInUseType_Type(Integer32):
    """Custom type hwDHCPSIPInUseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("manual", 1),
          ("release", 3))
    )


_HwDHCPSIPInUseType_Type.__name__ = "Integer32"
_HwDHCPSIPInUseType_Object = MibTableColumn
hwDHCPSIPInUseType = _HwDHCPSIPInUseType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 9, 1, 4),
    _HwDHCPSIPInUseType_Type()
)
hwDHCPSIPInUseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSIPInUseType.setStatus("deprecated")


class _HwDHCPSIPInUsePoolName_Type(OctetString):
    """Custom type hwDHCPSIPInUsePoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwDHCPSIPInUsePoolName_Type.__name__ = "OctetString"
_HwDHCPSIPInUsePoolName_Object = MibTableColumn
hwDHCPSIPInUsePoolName = _HwDHCPSIPInUsePoolName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 9, 1, 5),
    _HwDHCPSIPInUsePoolName_Type()
)
hwDHCPSIPInUsePoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSIPInUsePoolName.setStatus("deprecated")
_HwDHCPSIPInUseInterface_Type = Integer32
_HwDHCPSIPInUseInterface_Object = MibTableColumn
hwDHCPSIPInUseInterface = _HwDHCPSIPInUseInterface_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 9, 1, 6),
    _HwDHCPSIPInUseInterface_Type()
)
hwDHCPSIPInUseInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSIPInUseInterface.setStatus("deprecated")


class _HwDHCPSIPInUseVlan_Type(Integer32):
    """Custom type hwDHCPSIPInUseVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwDHCPSIPInUseVlan_Type.__name__ = "Integer32"
_HwDHCPSIPInUseVlan_Object = MibTableColumn
hwDHCPSIPInUseVlan = _HwDHCPSIPInUseVlan_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 9, 1, 7),
    _HwDHCPSIPInUseVlan_Type()
)
hwDHCPSIPInUseVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSIPInUseVlan.setStatus("deprecated")
_HwDHCPSIPInUseAtmpvc_Type = Integer32
_HwDHCPSIPInUseAtmpvc_Object = MibTableColumn
hwDHCPSIPInUseAtmpvc = _HwDHCPSIPInUseAtmpvc_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 9, 1, 8),
    _HwDHCPSIPInUseAtmpvc_Type()
)
hwDHCPSIPInUseAtmpvc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSIPInUseAtmpvc.setStatus("deprecated")
_HwDHCPSForbiddenIPTable_Object = MibTable
hwDHCPSForbiddenIPTable = _HwDHCPSForbiddenIPTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 10)
)
if mibBuilder.loadTexts:
    hwDHCPSForbiddenIPTable.setStatus("current")
_HwDHCPSForbiddenIPEntry_Object = MibTableRow
hwDHCPSForbiddenIPEntry = _HwDHCPSForbiddenIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 10, 1)
)
hwDHCPSForbiddenIPEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSForbiddenIPStart"),
    (0, "A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSForbiddenIPEnd"),
)
if mibBuilder.loadTexts:
    hwDHCPSForbiddenIPEntry.setStatus("current")
_HwDHCPSForbiddenIPStart_Type = IpAddress
_HwDHCPSForbiddenIPStart_Object = MibTableColumn
hwDHCPSForbiddenIPStart = _HwDHCPSForbiddenIPStart_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 10, 1, 1),
    _HwDHCPSForbiddenIPStart_Type()
)
hwDHCPSForbiddenIPStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSForbiddenIPStart.setStatus("current")
_HwDHCPSForbiddenIPEnd_Type = IpAddress
_HwDHCPSForbiddenIPEnd_Object = MibTableColumn
hwDHCPSForbiddenIPEnd = _HwDHCPSForbiddenIPEnd_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 10, 1, 2),
    _HwDHCPSForbiddenIPEnd_Type()
)
hwDHCPSForbiddenIPEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSForbiddenIPEnd.setStatus("current")
_HwDHCPSForbiddenIPRowStatus_Type = RowStatus
_HwDHCPSForbiddenIPRowStatus_Object = MibTableColumn
hwDHCPSForbiddenIPRowStatus = _HwDHCPSForbiddenIPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 10, 1, 3),
    _HwDHCPSForbiddenIPRowStatus_Type()
)
hwDHCPSForbiddenIPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDHCPSForbiddenIPRowStatus.setStatus("current")
_HwDHCPSConflictIPTable_Object = MibTable
hwDHCPSConflictIPTable = _HwDHCPSConflictIPTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 11)
)
if mibBuilder.loadTexts:
    hwDHCPSConflictIPTable.setStatus("current")
_HwDHCPSConflictIPEntry_Object = MibTableRow
hwDHCPSConflictIPEntry = _HwDHCPSConflictIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 11, 1)
)
hwDHCPSConflictIPEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSConflictIP"),
)
if mibBuilder.loadTexts:
    hwDHCPSConflictIPEntry.setStatus("current")
_HwDHCPSConflictIP_Type = IpAddress
_HwDHCPSConflictIP_Object = MibTableColumn
hwDHCPSConflictIP = _HwDHCPSConflictIP_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 11, 1, 1),
    _HwDHCPSConflictIP_Type()
)
hwDHCPSConflictIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSConflictIP.setStatus("current")


class _HwDHCPSConflictIPType_Type(Integer32):
    """Custom type hwDHCPSConflictIPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("arp", 2),
          ("ping", 1))
    )


_HwDHCPSConflictIPType_Type.__name__ = "Integer32"
_HwDHCPSConflictIPType_Object = MibTableColumn
hwDHCPSConflictIPType = _HwDHCPSConflictIPType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 11, 1, 2),
    _HwDHCPSConflictIPType_Type()
)
hwDHCPSConflictIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSConflictIPType.setStatus("current")


class _HwDHCPSConflictIPDetectTime_Type(OctetString):
    """Custom type hwDHCPSConflictIPDetectTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_HwDHCPSConflictIPDetectTime_Type.__name__ = "OctetString"
_HwDHCPSConflictIPDetectTime_Object = MibTableColumn
hwDHCPSConflictIPDetectTime = _HwDHCPSConflictIPDetectTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 11, 1, 3),
    _HwDHCPSConflictIPDetectTime_Type()
)
hwDHCPSConflictIPDetectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSConflictIPDetectTime.setStatus("current")


class _HwDHCPSServiceStatus_Type(EnabledStatus):
    """Custom type hwDHCPSServiceStatus based on EnabledStatus"""


_HwDHCPSServiceStatus_Object = MibScalar
hwDHCPSServiceStatus = _HwDHCPSServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 12),
    _HwDHCPSServiceStatus_Type()
)
hwDHCPSServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSServiceStatus.setStatus("current")


class _HwDHCPSDetectingServerStatus_Type(EnabledStatus):
    """Custom type hwDHCPSDetectingServerStatus based on EnabledStatus"""


_HwDHCPSDetectingServerStatus_Object = MibScalar
hwDHCPSDetectingServerStatus = _HwDHCPSDetectingServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 13),
    _HwDHCPSDetectingServerStatus_Type()
)
hwDHCPSDetectingServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSDetectingServerStatus.setStatus("current")


class _HwDHCPSPingNum_Type(Integer32):
    """Custom type hwDHCPSPingNum based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_HwDHCPSPingNum_Type.__name__ = "Integer32"
_HwDHCPSPingNum_Object = MibScalar
hwDHCPSPingNum = _HwDHCPSPingNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 14),
    _HwDHCPSPingNum_Type()
)
hwDHCPSPingNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSPingNum.setStatus("current")


class _HwDHCPSPingTimeout_Type(Integer32):
    """Custom type hwDHCPSPingTimeout based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HwDHCPSPingTimeout_Type.__name__ = "Integer32"
_HwDHCPSPingTimeout_Object = MibScalar
hwDHCPSPingTimeout = _HwDHCPSPingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 15),
    _HwDHCPSPingTimeout_Type()
)
hwDHCPSPingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSPingTimeout.setStatus("current")


class _HwDHCPSWriteDataStatus_Type(EnabledStatus):
    """Custom type hwDHCPSWriteDataStatus based on EnabledStatus"""


_HwDHCPSWriteDataStatus_Object = MibScalar
hwDHCPSWriteDataStatus = _HwDHCPSWriteDataStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 16),
    _HwDHCPSWriteDataStatus_Type()
)
hwDHCPSWriteDataStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSWriteDataStatus.setStatus("current")


class _HwDHCPSWriteDataDirection_Type(OctetString):
    """Custom type hwDHCPSWriteDataDirection based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwDHCPSWriteDataDirection_Type.__name__ = "OctetString"
_HwDHCPSWriteDataDirection_Object = MibScalar
hwDHCPSWriteDataDirection = _HwDHCPSWriteDataDirection_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 17),
    _HwDHCPSWriteDataDirection_Type()
)
hwDHCPSWriteDataDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSWriteDataDirection.setStatus("current")


class _HwDHCPSWriteDataDelay_Type(Integer32):
    """Custom type hwDHCPSWriteDataDelay based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 86400),
    )


_HwDHCPSWriteDataDelay_Type.__name__ = "Integer32"
_HwDHCPSWriteDataDelay_Object = MibScalar
hwDHCPSWriteDataDelay = _HwDHCPSWriteDataDelay_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 18),
    _HwDHCPSWriteDataDelay_Type()
)
hwDHCPSWriteDataDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSWriteDataDelay.setStatus("current")
_HwDHCPSWriteDataRecover_Type = EnabledStatus
_HwDHCPSWriteDataRecover_Object = MibScalar
hwDHCPSWriteDataRecover = _HwDHCPSWriteDataRecover_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 19),
    _HwDHCPSWriteDataRecover_Type()
)
hwDHCPSWriteDataRecover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSWriteDataRecover.setStatus("current")
_HwDHCPSIPInUseResetIP_Type = IpAddress
_HwDHCPSIPInUseResetIP_Object = MibScalar
hwDHCPSIPInUseResetIP = _HwDHCPSIPInUseResetIP_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 20),
    _HwDHCPSIPInUseResetIP_Type()
)
hwDHCPSIPInUseResetIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSIPInUseResetIP.setStatus("current")
_HwDHCPSConflictIPResetIP_Type = IpAddress
_HwDHCPSConflictIPResetIP_Object = MibScalar
hwDHCPSConflictIPResetIP = _HwDHCPSConflictIPResetIP_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 21),
    _HwDHCPSConflictIPResetIP_Type()
)
hwDHCPSConflictIPResetIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSConflictIPResetIP.setStatus("current")


class _HwDHCPSIPResetFlag_Type(Integer32):
    """Custom type hwDHCPSIPResetFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("conflictIp", 2),
          ("invalid", 0),
          ("ipInUse", 1))
    )


_HwDHCPSIPResetFlag_Type.__name__ = "Integer32"
_HwDHCPSIPResetFlag_Object = MibScalar
hwDHCPSIPResetFlag = _HwDHCPSIPResetFlag_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 22),
    _HwDHCPSIPResetFlag_Type()
)
hwDHCPSIPResetFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSIPResetFlag.setStatus("current")
_HwDHCPSGlobalPoolNumber_Type = Integer32
_HwDHCPSGlobalPoolNumber_Object = MibScalar
hwDHCPSGlobalPoolNumber = _HwDHCPSGlobalPoolNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 23),
    _HwDHCPSGlobalPoolNumber_Type()
)
hwDHCPSGlobalPoolNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolNumber.setStatus("current")
_HwDHCPSGlobalPoolAutoBindingNum_Type = Integer32
_HwDHCPSGlobalPoolAutoBindingNum_Object = MibScalar
hwDHCPSGlobalPoolAutoBindingNum = _HwDHCPSGlobalPoolAutoBindingNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 24),
    _HwDHCPSGlobalPoolAutoBindingNum_Type()
)
hwDHCPSGlobalPoolAutoBindingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolAutoBindingNum.setStatus("current")
_HwDHCPSGlobalPoolManualBindingNum_Type = Integer32
_HwDHCPSGlobalPoolManualBindingNum_Object = MibScalar
hwDHCPSGlobalPoolManualBindingNum = _HwDHCPSGlobalPoolManualBindingNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 25),
    _HwDHCPSGlobalPoolManualBindingNum_Type()
)
hwDHCPSGlobalPoolManualBindingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolManualBindingNum.setStatus("current")
_HwDHCPSGlobalPoolExpiredBindingNum_Type = Integer32
_HwDHCPSGlobalPoolExpiredBindingNum_Object = MibScalar
hwDHCPSGlobalPoolExpiredBindingNum = _HwDHCPSGlobalPoolExpiredBindingNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 26),
    _HwDHCPSGlobalPoolExpiredBindingNum_Type()
)
hwDHCPSGlobalPoolExpiredBindingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSGlobalPoolExpiredBindingNum.setStatus("current")
_HwDHCPSInterfacePoolNumber_Type = Integer32
_HwDHCPSInterfacePoolNumber_Object = MibScalar
hwDHCPSInterfacePoolNumber = _HwDHCPSInterfacePoolNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 27),
    _HwDHCPSInterfacePoolNumber_Type()
)
hwDHCPSInterfacePoolNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolNumber.setStatus("current")
_HwDHCPSInterfacePoolAutoBindingNum_Type = Integer32
_HwDHCPSInterfacePoolAutoBindingNum_Object = MibScalar
hwDHCPSInterfacePoolAutoBindingNum = _HwDHCPSInterfacePoolAutoBindingNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 28),
    _HwDHCPSInterfacePoolAutoBindingNum_Type()
)
hwDHCPSInterfacePoolAutoBindingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolAutoBindingNum.setStatus("current")
_HwDHCPSInterfacePoolManualBindingNum_Type = Integer32
_HwDHCPSInterfacePoolManualBindingNum_Object = MibScalar
hwDHCPSInterfacePoolManualBindingNum = _HwDHCPSInterfacePoolManualBindingNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 29),
    _HwDHCPSInterfacePoolManualBindingNum_Type()
)
hwDHCPSInterfacePoolManualBindingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolManualBindingNum.setStatus("current")
_HwDHCPSInterfacePoolExpiredBindingNum_Type = Integer32
_HwDHCPSInterfacePoolExpiredBindingNum_Object = MibScalar
hwDHCPSInterfacePoolExpiredBindingNum = _HwDHCPSInterfacePoolExpiredBindingNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 30),
    _HwDHCPSInterfacePoolExpiredBindingNum_Type()
)
hwDHCPSInterfacePoolExpiredBindingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSInterfacePoolExpiredBindingNum.setStatus("current")
_HwDHCPSBadPktNum_Type = Integer32
_HwDHCPSBadPktNum_Object = MibScalar
hwDHCPSBadPktNum = _HwDHCPSBadPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 31),
    _HwDHCPSBadPktNum_Type()
)
hwDHCPSBadPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSBadPktNum.setStatus("current")
_HwDHCPSBootRequestPktNum_Type = Integer32
_HwDHCPSBootRequestPktNum_Object = MibScalar
hwDHCPSBootRequestPktNum = _HwDHCPSBootRequestPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 32),
    _HwDHCPSBootRequestPktNum_Type()
)
hwDHCPSBootRequestPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSBootRequestPktNum.setStatus("current")
_HwDHCPSDiscoverPktNum_Type = Integer32
_HwDHCPSDiscoverPktNum_Object = MibScalar
hwDHCPSDiscoverPktNum = _HwDHCPSDiscoverPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 33),
    _HwDHCPSDiscoverPktNum_Type()
)
hwDHCPSDiscoverPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSDiscoverPktNum.setStatus("current")
_HwDHCPSRequestPktNum_Type = Integer32
_HwDHCPSRequestPktNum_Object = MibScalar
hwDHCPSRequestPktNum = _HwDHCPSRequestPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 34),
    _HwDHCPSRequestPktNum_Type()
)
hwDHCPSRequestPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSRequestPktNum.setStatus("current")
_HwDHCPSDeclinePktNum_Type = Integer32
_HwDHCPSDeclinePktNum_Object = MibScalar
hwDHCPSDeclinePktNum = _HwDHCPSDeclinePktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 35),
    _HwDHCPSDeclinePktNum_Type()
)
hwDHCPSDeclinePktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSDeclinePktNum.setStatus("current")
_HwDHCPSReleasePktNum_Type = Integer32
_HwDHCPSReleasePktNum_Object = MibScalar
hwDHCPSReleasePktNum = _HwDHCPSReleasePktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 36),
    _HwDHCPSReleasePktNum_Type()
)
hwDHCPSReleasePktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSReleasePktNum.setStatus("current")
_HwDHCPSInformPktNum_Type = Integer32
_HwDHCPSInformPktNum_Object = MibScalar
hwDHCPSInformPktNum = _HwDHCPSInformPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 37),
    _HwDHCPSInformPktNum_Type()
)
hwDHCPSInformPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSInformPktNum.setStatus("current")
_HwDHCPSBootReplyPktNum_Type = Integer32
_HwDHCPSBootReplyPktNum_Object = MibScalar
hwDHCPSBootReplyPktNum = _HwDHCPSBootReplyPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 38),
    _HwDHCPSBootReplyPktNum_Type()
)
hwDHCPSBootReplyPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSBootReplyPktNum.setStatus("current")
_HwDHCPSOfferPktNum_Type = Integer32
_HwDHCPSOfferPktNum_Object = MibScalar
hwDHCPSOfferPktNum = _HwDHCPSOfferPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 39),
    _HwDHCPSOfferPktNum_Type()
)
hwDHCPSOfferPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSOfferPktNum.setStatus("current")
_HwDHCPSAckPktNum_Type = Integer32
_HwDHCPSAckPktNum_Object = MibScalar
hwDHCPSAckPktNum = _HwDHCPSAckPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 40),
    _HwDHCPSAckPktNum_Type()
)
hwDHCPSAckPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSAckPktNum.setStatus("current")
_HwDHCPSNakPktNum_Type = Integer32
_HwDHCPSNakPktNum_Object = MibScalar
hwDHCPSNakPktNum = _HwDHCPSNakPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 41),
    _HwDHCPSNakPktNum_Type()
)
hwDHCPSNakPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSNakPktNum.setStatus("current")


class _HwDHCPSStatisticsReset_Type(Integer32):
    """Custom type hwDHCPSStatisticsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HwDHCPSStatisticsReset_Type.__name__ = "Integer32"
_HwDHCPSStatisticsReset_Object = MibScalar
hwDHCPSStatisticsReset = _HwDHCPSStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 42),
    _HwDHCPSStatisticsReset_Type()
)
hwDHCPSStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDHCPSStatisticsReset.setStatus("current")
_HwDHCPSIPInUseExTable_Object = MibTable
hwDHCPSIPInUseExTable = _HwDHCPSIPInUseExTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 43)
)
if mibBuilder.loadTexts:
    hwDHCPSIPInUseExTable.setStatus("current")
_HwDHCPSIPInUseExEntry_Object = MibTableRow
hwDHCPSIPInUseExEntry = _HwDHCPSIPInUseExEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 43, 1)
)
hwDHCPSIPInUseExEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSIPInUseHAddrEx"),
    (0, "A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSIPInUseVlanIdEx"),
)
if mibBuilder.loadTexts:
    hwDHCPSIPInUseExEntry.setStatus("current")
_HwDHCPSIPInUseHAddrEx_Type = MacAddress
_HwDHCPSIPInUseHAddrEx_Object = MibTableColumn
hwDHCPSIPInUseHAddrEx = _HwDHCPSIPInUseHAddrEx_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 43, 1, 1),
    _HwDHCPSIPInUseHAddrEx_Type()
)
hwDHCPSIPInUseHAddrEx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwDHCPSIPInUseHAddrEx.setStatus("current")


class _HwDHCPSIPInUseVlanIdEx_Type(Integer32):
    """Custom type hwDHCPSIPInUseVlanIdEx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(60000, 60000),
    )


_HwDHCPSIPInUseVlanIdEx_Type.__name__ = "Integer32"
_HwDHCPSIPInUseVlanIdEx_Object = MibTableColumn
hwDHCPSIPInUseVlanIdEx = _HwDHCPSIPInUseVlanIdEx_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 43, 1, 2),
    _HwDHCPSIPInUseVlanIdEx_Type()
)
hwDHCPSIPInUseVlanIdEx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwDHCPSIPInUseVlanIdEx.setStatus("current")
_HwDHCPSIPInUseIPEx_Type = IpAddress
_HwDHCPSIPInUseIPEx_Object = MibTableColumn
hwDHCPSIPInUseIPEx = _HwDHCPSIPInUseIPEx_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 43, 1, 3),
    _HwDHCPSIPInUseIPEx_Type()
)
hwDHCPSIPInUseIPEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSIPInUseIPEx.setStatus("current")


class _HwDHCPSIPInUseEndLeaseEx_Type(OctetString):
    """Custom type hwDHCPSIPInUseEndLeaseEx based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_HwDHCPSIPInUseEndLeaseEx_Type.__name__ = "OctetString"
_HwDHCPSIPInUseEndLeaseEx_Object = MibTableColumn
hwDHCPSIPInUseEndLeaseEx = _HwDHCPSIPInUseEndLeaseEx_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 43, 1, 4),
    _HwDHCPSIPInUseEndLeaseEx_Type()
)
hwDHCPSIPInUseEndLeaseEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSIPInUseEndLeaseEx.setStatus("current")


class _HwDHCPSIPInUseTypeEx_Type(Integer32):
    """Custom type hwDHCPSIPInUseTypeEx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("manual", 1),
          ("release", 3))
    )


_HwDHCPSIPInUseTypeEx_Type.__name__ = "Integer32"
_HwDHCPSIPInUseTypeEx_Object = MibTableColumn
hwDHCPSIPInUseTypeEx = _HwDHCPSIPInUseTypeEx_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 43, 1, 5),
    _HwDHCPSIPInUseTypeEx_Type()
)
hwDHCPSIPInUseTypeEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSIPInUseTypeEx.setStatus("current")


class _HwDHCPSIPInUsePoolNameEx_Type(OctetString):
    """Custom type hwDHCPSIPInUsePoolNameEx based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwDHCPSIPInUsePoolNameEx_Type.__name__ = "OctetString"
_HwDHCPSIPInUsePoolNameEx_Object = MibTableColumn
hwDHCPSIPInUsePoolNameEx = _HwDHCPSIPInUsePoolNameEx_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 43, 1, 6),
    _HwDHCPSIPInUsePoolNameEx_Type()
)
hwDHCPSIPInUsePoolNameEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSIPInUsePoolNameEx.setStatus("current")
_HwDHCPSIPInUseIfIndexEx_Type = Integer32
_HwDHCPSIPInUseIfIndexEx_Object = MibTableColumn
hwDHCPSIPInUseIfIndexEx = _HwDHCPSIPInUseIfIndexEx_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 43, 1, 7),
    _HwDHCPSIPInUseIfIndexEx_Type()
)
hwDHCPSIPInUseIfIndexEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSIPInUseIfIndexEx.setStatus("current")


class _HwDHCPSIPInUseServerPortVlanIdEx_Type(Integer32):
    """Custom type hwDHCPSIPInUseServerPortVlanIdEx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwDHCPSIPInUseServerPortVlanIdEx_Type.__name__ = "Integer32"
_HwDHCPSIPInUseServerPortVlanIdEx_Object = MibTableColumn
hwDHCPSIPInUseServerPortVlanIdEx = _HwDHCPSIPInUseServerPortVlanIdEx_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 43, 1, 8),
    _HwDHCPSIPInUseServerPortVlanIdEx_Type()
)
hwDHCPSIPInUseServerPortVlanIdEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSIPInUseServerPortVlanIdEx.setStatus("current")
_HwDHCPSIPInUseAtmpvcEx_Type = Integer32
_HwDHCPSIPInUseAtmpvcEx_Object = MibTableColumn
hwDHCPSIPInUseAtmpvcEx = _HwDHCPSIPInUseAtmpvcEx_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 1, 43, 1, 9),
    _HwDHCPSIPInUseAtmpvcEx_Type()
)
hwDHCPSIPInUseAtmpvcEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDHCPSIPInUseAtmpvcEx.setStatus("current")
_HwDHCPServerMIBConformance_ObjectIdentity = ObjectIdentity
hwDHCPServerMIBConformance = _HwDHCPServerMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 2)
)
_HwDHCPServerMIBCompliances_ObjectIdentity = ObjectIdentity
hwDHCPServerMIBCompliances = _HwDHCPServerMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 2, 1)
)
_HwDHCPServerMIBGroups_ObjectIdentity = ObjectIdentity
hwDHCPServerMIBGroups = _HwDHCPServerMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 2, 2)
)

# Managed Objects groups

hwDHCPServerMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 7, 2, 2, 2, 1)
)
hwDHCPServerMIBGroup.setObjects(
      *(("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolName"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolRowStatus"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolType"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolNetwork"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolNetworkMask"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolHostIPAddr"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolHostMask"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolHostHAddr"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolConfigUndoFlag"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolLeaseDay"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolLeaseHour"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolLeaseMinute"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolLeaseUnlimited"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolDomainName"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolClientGatewayIPString"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolClientGatewayIPUndo"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolClientDNSIPString"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolClientDNSIPUndo"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolClientNetbiosType"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolClientNbnsIPString"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolClientNbnsIPUndo"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolParaUndoFlag"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolIPInUseReset"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolOptionCode"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolOptionType"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolOptionAscii"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolOptionHexString"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolOptionIPString"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolOptionRowStatus"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalTreeParentNodeName"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalTreeChildNodeName"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalTreePreSiblingNodeName"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalTreeSiblingNodeName"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSInterfacePoolLeaseDay"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSInterfacePoolLeaseHour"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSInterfacePoolLeaseMinute"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSInterfacePoolLeaseUnlimited"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSInterfacePoolDomainName"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSInterfacePoolClientDNSIPString"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSInterfacePoolClientDNSIPUndo"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSInterfacePoolClientNetbiosType"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSInterfacePoolClientNbnsIPString"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSInterfacePoolClientNbnsIPUndo"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSInterfacePoolParaUndoFlag"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSInterfacePoolIPInUseReset"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSInterfacePoolOptionCode"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSInterfacePoolOptionType"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSInterfacePoolOptionAscii"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSInterfacePoolOptionHexString"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSInterfacePoolOptionIPString"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSInterfacePoolOptionRowStatus"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSInterfacePoolStaticBindIP"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSInterfacePoolStaticBindMac"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSInterfacePoolStaticBindRowStatus"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSIPInUseHAddr"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSIPInUseIP"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSIPInUseEndLease"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSIPInUseType"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSIPInUsePoolName"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSIPInUseInterface"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSIPInUseVlan"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSIPInUseAtmpvc"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSForbiddenIPStart"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSForbiddenIPEnd"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSForbiddenIPRowStatus"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSConflictIP"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSConflictIPType"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSConflictIPDetectTime"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSServiceStatus"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSDetectingServerStatus"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSPingNum"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSPingTimeout"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSWriteDataStatus"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSWriteDataDirection"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSWriteDataDelay"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSWriteDataRecover"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSIPInUseResetIP"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSConflictIPResetIP"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSIPResetFlag"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolNumber"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolAutoBindingNum"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolManualBindingNum"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSGlobalPoolExpiredBindingNum"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSInterfacePoolNumber"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSInterfacePoolAutoBindingNum"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSInterfacePoolManualBindingNum"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSInterfacePoolExpiredBindingNum"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSBadPktNum"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSBootRequestPktNum"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSDiscoverPktNum"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSRequestPktNum"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSDeclinePktNum"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSReleasePktNum"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSInformPktNum"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSBootReplyPktNum"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSOfferPktNum"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSAckPktNum"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSNakPktNum"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSStatisticsReset"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSIPInUseHAddrEx"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSIPInUseVlanIdEx"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSIPInUseIPEx"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSIPInUseEndLeaseEx"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSIPInUseTypeEx"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSIPInUsePoolNameEx"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSIPInUseIfIndexEx"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSIPInUseServerPortVlanIdEx"),
        ("A3COM-HUAWEI-DHCPS-MIB", "hwDHCPSIPInUseAtmpvcEx"))
)
if mibBuilder.loadTexts:
    hwDHCPServerMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-DHCPS-MIB",
    **{"EnabledStatus": EnabledStatus,
       "hwDHCPServerMib": hwDHCPServerMib,
       "hwDHCPServerMibObject": hwDHCPServerMibObject,
       "hwDHCPSGlobalPoolTable": hwDHCPSGlobalPoolTable,
       "hwDHCPSGlobalPoolEntry": hwDHCPSGlobalPoolEntry,
       "hwDHCPSGlobalPoolName": hwDHCPSGlobalPoolName,
       "hwDHCPSGlobalPoolRowStatus": hwDHCPSGlobalPoolRowStatus,
       "hwDHCPSGlobalPoolConfigTable": hwDHCPSGlobalPoolConfigTable,
       "hwDHCPSGlobalPoolConfigEntry": hwDHCPSGlobalPoolConfigEntry,
       "hwDHCPSGlobalPoolType": hwDHCPSGlobalPoolType,
       "hwDHCPSGlobalPoolNetwork": hwDHCPSGlobalPoolNetwork,
       "hwDHCPSGlobalPoolNetworkMask": hwDHCPSGlobalPoolNetworkMask,
       "hwDHCPSGlobalPoolHostIPAddr": hwDHCPSGlobalPoolHostIPAddr,
       "hwDHCPSGlobalPoolHostMask": hwDHCPSGlobalPoolHostMask,
       "hwDHCPSGlobalPoolHostHAddr": hwDHCPSGlobalPoolHostHAddr,
       "hwDHCPSGlobalPoolConfigUndoFlag": hwDHCPSGlobalPoolConfigUndoFlag,
       "hwDHCPSGlobalPoolParaTable": hwDHCPSGlobalPoolParaTable,
       "hwDHCPSGlobalPoolParaEntry": hwDHCPSGlobalPoolParaEntry,
       "hwDHCPSGlobalPoolLeaseDay": hwDHCPSGlobalPoolLeaseDay,
       "hwDHCPSGlobalPoolLeaseHour": hwDHCPSGlobalPoolLeaseHour,
       "hwDHCPSGlobalPoolLeaseMinute": hwDHCPSGlobalPoolLeaseMinute,
       "hwDHCPSGlobalPoolLeaseUnlimited": hwDHCPSGlobalPoolLeaseUnlimited,
       "hwDHCPSGlobalPoolDomainName": hwDHCPSGlobalPoolDomainName,
       "hwDHCPSGlobalPoolClientGatewayIPString": hwDHCPSGlobalPoolClientGatewayIPString,
       "hwDHCPSGlobalPoolClientGatewayIPUndo": hwDHCPSGlobalPoolClientGatewayIPUndo,
       "hwDHCPSGlobalPoolClientDNSIPString": hwDHCPSGlobalPoolClientDNSIPString,
       "hwDHCPSGlobalPoolClientDNSIPUndo": hwDHCPSGlobalPoolClientDNSIPUndo,
       "hwDHCPSGlobalPoolClientNetbiosType": hwDHCPSGlobalPoolClientNetbiosType,
       "hwDHCPSGlobalPoolClientNbnsIPString": hwDHCPSGlobalPoolClientNbnsIPString,
       "hwDHCPSGlobalPoolClientNbnsIPUndo": hwDHCPSGlobalPoolClientNbnsIPUndo,
       "hwDHCPSGlobalPoolParaUndoFlag": hwDHCPSGlobalPoolParaUndoFlag,
       "hwDHCPSGlobalPoolIPInUseReset": hwDHCPSGlobalPoolIPInUseReset,
       "hwDHCPSGlobalPoolOptionTable": hwDHCPSGlobalPoolOptionTable,
       "hwDHCPSGlobalPoolOptionEntry": hwDHCPSGlobalPoolOptionEntry,
       "hwDHCPSGlobalPoolOptionCode": hwDHCPSGlobalPoolOptionCode,
       "hwDHCPSGlobalPoolOptionType": hwDHCPSGlobalPoolOptionType,
       "hwDHCPSGlobalPoolOptionAscii": hwDHCPSGlobalPoolOptionAscii,
       "hwDHCPSGlobalPoolOptionHexString": hwDHCPSGlobalPoolOptionHexString,
       "hwDHCPSGlobalPoolOptionIPString": hwDHCPSGlobalPoolOptionIPString,
       "hwDHCPSGlobalPoolOptionRowStatus": hwDHCPSGlobalPoolOptionRowStatus,
       "hwDHCPSGlobalTreeTable": hwDHCPSGlobalTreeTable,
       "hwDHCPSGlobalTreeEntry": hwDHCPSGlobalTreeEntry,
       "hwDHCPSGlobalTreeParentNodeName": hwDHCPSGlobalTreeParentNodeName,
       "hwDHCPSGlobalTreeChildNodeName": hwDHCPSGlobalTreeChildNodeName,
       "hwDHCPSGlobalTreePreSiblingNodeName": hwDHCPSGlobalTreePreSiblingNodeName,
       "hwDHCPSGlobalTreeSiblingNodeName": hwDHCPSGlobalTreeSiblingNodeName,
       "hwDHCPSInterfacePoolParaTable": hwDHCPSInterfacePoolParaTable,
       "hwDHCPSInterfacePoolParaEntry": hwDHCPSInterfacePoolParaEntry,
       "hwDHCPSInterfacePoolLeaseDay": hwDHCPSInterfacePoolLeaseDay,
       "hwDHCPSInterfacePoolLeaseHour": hwDHCPSInterfacePoolLeaseHour,
       "hwDHCPSInterfacePoolLeaseMinute": hwDHCPSInterfacePoolLeaseMinute,
       "hwDHCPSInterfacePoolLeaseUnlimited": hwDHCPSInterfacePoolLeaseUnlimited,
       "hwDHCPSInterfacePoolDomainName": hwDHCPSInterfacePoolDomainName,
       "hwDHCPSInterfacePoolClientDNSIPString": hwDHCPSInterfacePoolClientDNSIPString,
       "hwDHCPSInterfacePoolClientDNSIPUndo": hwDHCPSInterfacePoolClientDNSIPUndo,
       "hwDHCPSInterfacePoolClientNetbiosType": hwDHCPSInterfacePoolClientNetbiosType,
       "hwDHCPSInterfacePoolClientNbnsIPString": hwDHCPSInterfacePoolClientNbnsIPString,
       "hwDHCPSInterfacePoolClientNbnsIPUndo": hwDHCPSInterfacePoolClientNbnsIPUndo,
       "hwDHCPSInterfacePoolParaUndoFlag": hwDHCPSInterfacePoolParaUndoFlag,
       "hwDHCPSInterfacePoolIPInUseReset": hwDHCPSInterfacePoolIPInUseReset,
       "hwDHCPSInterfacePoolOptionTable": hwDHCPSInterfacePoolOptionTable,
       "hwDHCPSInterfacePoolOptionEntry": hwDHCPSInterfacePoolOptionEntry,
       "hwDHCPSInterfacePoolOptionCode": hwDHCPSInterfacePoolOptionCode,
       "hwDHCPSInterfacePoolOptionType": hwDHCPSInterfacePoolOptionType,
       "hwDHCPSInterfacePoolOptionAscii": hwDHCPSInterfacePoolOptionAscii,
       "hwDHCPSInterfacePoolOptionHexString": hwDHCPSInterfacePoolOptionHexString,
       "hwDHCPSInterfacePoolOptionIPString": hwDHCPSInterfacePoolOptionIPString,
       "hwDHCPSInterfacePoolOptionRowStatus": hwDHCPSInterfacePoolOptionRowStatus,
       "hwDHCPSInterfacePoolStaticBindTable": hwDHCPSInterfacePoolStaticBindTable,
       "hwDHCPSInterfacePoolStaticBindEntry": hwDHCPSInterfacePoolStaticBindEntry,
       "hwDHCPSInterfacePoolStaticBindIP": hwDHCPSInterfacePoolStaticBindIP,
       "hwDHCPSInterfacePoolStaticBindMac": hwDHCPSInterfacePoolStaticBindMac,
       "hwDHCPSInterfacePoolStaticBindRowStatus": hwDHCPSInterfacePoolStaticBindRowStatus,
       "hwDHCPSIPInUseTable": hwDHCPSIPInUseTable,
       "hwDHCPSIPInUseEntry": hwDHCPSIPInUseEntry,
       "hwDHCPSIPInUseHAddr": hwDHCPSIPInUseHAddr,
       "hwDHCPSIPInUseIP": hwDHCPSIPInUseIP,
       "hwDHCPSIPInUseEndLease": hwDHCPSIPInUseEndLease,
       "hwDHCPSIPInUseType": hwDHCPSIPInUseType,
       "hwDHCPSIPInUsePoolName": hwDHCPSIPInUsePoolName,
       "hwDHCPSIPInUseInterface": hwDHCPSIPInUseInterface,
       "hwDHCPSIPInUseVlan": hwDHCPSIPInUseVlan,
       "hwDHCPSIPInUseAtmpvc": hwDHCPSIPInUseAtmpvc,
       "hwDHCPSForbiddenIPTable": hwDHCPSForbiddenIPTable,
       "hwDHCPSForbiddenIPEntry": hwDHCPSForbiddenIPEntry,
       "hwDHCPSForbiddenIPStart": hwDHCPSForbiddenIPStart,
       "hwDHCPSForbiddenIPEnd": hwDHCPSForbiddenIPEnd,
       "hwDHCPSForbiddenIPRowStatus": hwDHCPSForbiddenIPRowStatus,
       "hwDHCPSConflictIPTable": hwDHCPSConflictIPTable,
       "hwDHCPSConflictIPEntry": hwDHCPSConflictIPEntry,
       "hwDHCPSConflictIP": hwDHCPSConflictIP,
       "hwDHCPSConflictIPType": hwDHCPSConflictIPType,
       "hwDHCPSConflictIPDetectTime": hwDHCPSConflictIPDetectTime,
       "hwDHCPSServiceStatus": hwDHCPSServiceStatus,
       "hwDHCPSDetectingServerStatus": hwDHCPSDetectingServerStatus,
       "hwDHCPSPingNum": hwDHCPSPingNum,
       "hwDHCPSPingTimeout": hwDHCPSPingTimeout,
       "hwDHCPSWriteDataStatus": hwDHCPSWriteDataStatus,
       "hwDHCPSWriteDataDirection": hwDHCPSWriteDataDirection,
       "hwDHCPSWriteDataDelay": hwDHCPSWriteDataDelay,
       "hwDHCPSWriteDataRecover": hwDHCPSWriteDataRecover,
       "hwDHCPSIPInUseResetIP": hwDHCPSIPInUseResetIP,
       "hwDHCPSConflictIPResetIP": hwDHCPSConflictIPResetIP,
       "hwDHCPSIPResetFlag": hwDHCPSIPResetFlag,
       "hwDHCPSGlobalPoolNumber": hwDHCPSGlobalPoolNumber,
       "hwDHCPSGlobalPoolAutoBindingNum": hwDHCPSGlobalPoolAutoBindingNum,
       "hwDHCPSGlobalPoolManualBindingNum": hwDHCPSGlobalPoolManualBindingNum,
       "hwDHCPSGlobalPoolExpiredBindingNum": hwDHCPSGlobalPoolExpiredBindingNum,
       "hwDHCPSInterfacePoolNumber": hwDHCPSInterfacePoolNumber,
       "hwDHCPSInterfacePoolAutoBindingNum": hwDHCPSInterfacePoolAutoBindingNum,
       "hwDHCPSInterfacePoolManualBindingNum": hwDHCPSInterfacePoolManualBindingNum,
       "hwDHCPSInterfacePoolExpiredBindingNum": hwDHCPSInterfacePoolExpiredBindingNum,
       "hwDHCPSBadPktNum": hwDHCPSBadPktNum,
       "hwDHCPSBootRequestPktNum": hwDHCPSBootRequestPktNum,
       "hwDHCPSDiscoverPktNum": hwDHCPSDiscoverPktNum,
       "hwDHCPSRequestPktNum": hwDHCPSRequestPktNum,
       "hwDHCPSDeclinePktNum": hwDHCPSDeclinePktNum,
       "hwDHCPSReleasePktNum": hwDHCPSReleasePktNum,
       "hwDHCPSInformPktNum": hwDHCPSInformPktNum,
       "hwDHCPSBootReplyPktNum": hwDHCPSBootReplyPktNum,
       "hwDHCPSOfferPktNum": hwDHCPSOfferPktNum,
       "hwDHCPSAckPktNum": hwDHCPSAckPktNum,
       "hwDHCPSNakPktNum": hwDHCPSNakPktNum,
       "hwDHCPSStatisticsReset": hwDHCPSStatisticsReset,
       "hwDHCPSIPInUseExTable": hwDHCPSIPInUseExTable,
       "hwDHCPSIPInUseExEntry": hwDHCPSIPInUseExEntry,
       "hwDHCPSIPInUseHAddrEx": hwDHCPSIPInUseHAddrEx,
       "hwDHCPSIPInUseVlanIdEx": hwDHCPSIPInUseVlanIdEx,
       "hwDHCPSIPInUseIPEx": hwDHCPSIPInUseIPEx,
       "hwDHCPSIPInUseEndLeaseEx": hwDHCPSIPInUseEndLeaseEx,
       "hwDHCPSIPInUseTypeEx": hwDHCPSIPInUseTypeEx,
       "hwDHCPSIPInUsePoolNameEx": hwDHCPSIPInUsePoolNameEx,
       "hwDHCPSIPInUseIfIndexEx": hwDHCPSIPInUseIfIndexEx,
       "hwDHCPSIPInUseServerPortVlanIdEx": hwDHCPSIPInUseServerPortVlanIdEx,
       "hwDHCPSIPInUseAtmpvcEx": hwDHCPSIPInUseAtmpvcEx,
       "hwDHCPServerMIBConformance": hwDHCPServerMIBConformance,
       "hwDHCPServerMIBCompliances": hwDHCPServerMIBCompliances,
       "hwDHCPServerMIBGroups": hwDHCPServerMIBGroups,
       "hwDHCPServerMIBGroup": hwDHCPServerMIBGroup}
)
