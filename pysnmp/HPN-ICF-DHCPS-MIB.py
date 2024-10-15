# SNMP MIB module (HPN-ICF-DHCPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-DHCPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:42 2024
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

(hpnicfRhw,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfRhw")

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

hpnicfDHCPServerMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfDhcpSEnabledStatus(Integer32, TextualConvention):
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

_HpnicfDHCPServerMibObject_ObjectIdentity = ObjectIdentity
hpnicfDHCPServerMibObject = _HpnicfDHCPServerMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1)
)
_HpnicfDHCPSGlobalPoolTable_Object = MibTable
hpnicfDHCPSGlobalPoolTable = _HpnicfDHCPSGlobalPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolTable.setStatus("current")
_HpnicfDHCPSGlobalPoolEntry_Object = MibTableRow
hpnicfDHCPSGlobalPoolEntry = _HpnicfDHCPSGlobalPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 1, 1)
)
hpnicfDHCPSGlobalPoolEntry.setIndexNames(
    (0, "HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolName"),
)
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolEntry.setStatus("current")


class _HpnicfDHCPSGlobalPoolName_Type(OctetString):
    """Custom type hpnicfDHCPSGlobalPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfDHCPSGlobalPoolName_Type.__name__ = "OctetString"
_HpnicfDHCPSGlobalPoolName_Object = MibTableColumn
hpnicfDHCPSGlobalPoolName = _HpnicfDHCPSGlobalPoolName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 1, 1, 1),
    _HpnicfDHCPSGlobalPoolName_Type()
)
hpnicfDHCPSGlobalPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolName.setStatus("current")
_HpnicfDHCPSGlobalPoolRowStatus_Type = RowStatus
_HpnicfDHCPSGlobalPoolRowStatus_Object = MibTableColumn
hpnicfDHCPSGlobalPoolRowStatus = _HpnicfDHCPSGlobalPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 1, 1, 2),
    _HpnicfDHCPSGlobalPoolRowStatus_Type()
)
hpnicfDHCPSGlobalPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolRowStatus.setStatus("current")
_HpnicfDHCPSGlobalPoolConfigTable_Object = MibTable
hpnicfDHCPSGlobalPoolConfigTable = _HpnicfDHCPSGlobalPoolConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolConfigTable.setStatus("current")
_HpnicfDHCPSGlobalPoolConfigEntry_Object = MibTableRow
hpnicfDHCPSGlobalPoolConfigEntry = _HpnicfDHCPSGlobalPoolConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 2, 1)
)
hpnicfDHCPSGlobalPoolConfigEntry.setIndexNames(
    (0, "HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolName"),
)
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolConfigEntry.setStatus("current")


class _HpnicfDHCPSGlobalPoolType_Type(Integer32):
    """Custom type hpnicfDHCPSGlobalPoolType based on Integer32"""
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


_HpnicfDHCPSGlobalPoolType_Type.__name__ = "Integer32"
_HpnicfDHCPSGlobalPoolType_Object = MibTableColumn
hpnicfDHCPSGlobalPoolType = _HpnicfDHCPSGlobalPoolType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 2, 1, 1),
    _HpnicfDHCPSGlobalPoolType_Type()
)
hpnicfDHCPSGlobalPoolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolType.setStatus("current")
_HpnicfDHCPSGlobalPoolNetwork_Type = IpAddress
_HpnicfDHCPSGlobalPoolNetwork_Object = MibTableColumn
hpnicfDHCPSGlobalPoolNetwork = _HpnicfDHCPSGlobalPoolNetwork_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 2, 1, 2),
    _HpnicfDHCPSGlobalPoolNetwork_Type()
)
hpnicfDHCPSGlobalPoolNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolNetwork.setStatus("current")
_HpnicfDHCPSGlobalPoolNetworkMask_Type = IpAddress
_HpnicfDHCPSGlobalPoolNetworkMask_Object = MibTableColumn
hpnicfDHCPSGlobalPoolNetworkMask = _HpnicfDHCPSGlobalPoolNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 2, 1, 3),
    _HpnicfDHCPSGlobalPoolNetworkMask_Type()
)
hpnicfDHCPSGlobalPoolNetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolNetworkMask.setStatus("current")
_HpnicfDHCPSGlobalPoolHostIPAddr_Type = IpAddress
_HpnicfDHCPSGlobalPoolHostIPAddr_Object = MibTableColumn
hpnicfDHCPSGlobalPoolHostIPAddr = _HpnicfDHCPSGlobalPoolHostIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 2, 1, 4),
    _HpnicfDHCPSGlobalPoolHostIPAddr_Type()
)
hpnicfDHCPSGlobalPoolHostIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolHostIPAddr.setStatus("current")
_HpnicfDHCPSGlobalPoolHostMask_Type = IpAddress
_HpnicfDHCPSGlobalPoolHostMask_Object = MibTableColumn
hpnicfDHCPSGlobalPoolHostMask = _HpnicfDHCPSGlobalPoolHostMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 2, 1, 5),
    _HpnicfDHCPSGlobalPoolHostMask_Type()
)
hpnicfDHCPSGlobalPoolHostMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolHostMask.setStatus("current")
_HpnicfDHCPSGlobalPoolHostHAddr_Type = MacAddress
_HpnicfDHCPSGlobalPoolHostHAddr_Object = MibTableColumn
hpnicfDHCPSGlobalPoolHostHAddr = _HpnicfDHCPSGlobalPoolHostHAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 2, 1, 6),
    _HpnicfDHCPSGlobalPoolHostHAddr_Type()
)
hpnicfDHCPSGlobalPoolHostHAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolHostHAddr.setStatus("current")


class _HpnicfDHCPSGlobalPoolConfigUndoFlag_Type(Integer32):
    """Custom type hpnicfDHCPSGlobalPoolConfigUndoFlag based on Integer32"""
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


_HpnicfDHCPSGlobalPoolConfigUndoFlag_Type.__name__ = "Integer32"
_HpnicfDHCPSGlobalPoolConfigUndoFlag_Object = MibTableColumn
hpnicfDHCPSGlobalPoolConfigUndoFlag = _HpnicfDHCPSGlobalPoolConfigUndoFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 2, 1, 7),
    _HpnicfDHCPSGlobalPoolConfigUndoFlag_Type()
)
hpnicfDHCPSGlobalPoolConfigUndoFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolConfigUndoFlag.setStatus("current")
_HpnicfDHCPSGlobalPoolParaTable_Object = MibTable
hpnicfDHCPSGlobalPoolParaTable = _HpnicfDHCPSGlobalPoolParaTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolParaTable.setStatus("current")
_HpnicfDHCPSGlobalPoolParaEntry_Object = MibTableRow
hpnicfDHCPSGlobalPoolParaEntry = _HpnicfDHCPSGlobalPoolParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 3, 1)
)
hpnicfDHCPSGlobalPoolParaEntry.setIndexNames(
    (0, "HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolName"),
)
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolParaEntry.setStatus("current")


class _HpnicfDHCPSGlobalPoolLeaseDay_Type(Integer32):
    """Custom type hpnicfDHCPSGlobalPoolLeaseDay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_HpnicfDHCPSGlobalPoolLeaseDay_Type.__name__ = "Integer32"
_HpnicfDHCPSGlobalPoolLeaseDay_Object = MibTableColumn
hpnicfDHCPSGlobalPoolLeaseDay = _HpnicfDHCPSGlobalPoolLeaseDay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 3, 1, 1),
    _HpnicfDHCPSGlobalPoolLeaseDay_Type()
)
hpnicfDHCPSGlobalPoolLeaseDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolLeaseDay.setStatus("current")


class _HpnicfDHCPSGlobalPoolLeaseHour_Type(Integer32):
    """Custom type hpnicfDHCPSGlobalPoolLeaseHour based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_HpnicfDHCPSGlobalPoolLeaseHour_Type.__name__ = "Integer32"
_HpnicfDHCPSGlobalPoolLeaseHour_Object = MibTableColumn
hpnicfDHCPSGlobalPoolLeaseHour = _HpnicfDHCPSGlobalPoolLeaseHour_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 3, 1, 2),
    _HpnicfDHCPSGlobalPoolLeaseHour_Type()
)
hpnicfDHCPSGlobalPoolLeaseHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolLeaseHour.setStatus("current")


class _HpnicfDHCPSGlobalPoolLeaseMinute_Type(Integer32):
    """Custom type hpnicfDHCPSGlobalPoolLeaseMinute based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_HpnicfDHCPSGlobalPoolLeaseMinute_Type.__name__ = "Integer32"
_HpnicfDHCPSGlobalPoolLeaseMinute_Object = MibTableColumn
hpnicfDHCPSGlobalPoolLeaseMinute = _HpnicfDHCPSGlobalPoolLeaseMinute_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 3, 1, 3),
    _HpnicfDHCPSGlobalPoolLeaseMinute_Type()
)
hpnicfDHCPSGlobalPoolLeaseMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolLeaseMinute.setStatus("current")


class _HpnicfDHCPSGlobalPoolLeaseUnlimited_Type(Integer32):
    """Custom type hpnicfDHCPSGlobalPoolLeaseUnlimited based on Integer32"""
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


_HpnicfDHCPSGlobalPoolLeaseUnlimited_Type.__name__ = "Integer32"
_HpnicfDHCPSGlobalPoolLeaseUnlimited_Object = MibTableColumn
hpnicfDHCPSGlobalPoolLeaseUnlimited = _HpnicfDHCPSGlobalPoolLeaseUnlimited_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 3, 1, 4),
    _HpnicfDHCPSGlobalPoolLeaseUnlimited_Type()
)
hpnicfDHCPSGlobalPoolLeaseUnlimited.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolLeaseUnlimited.setStatus("current")


class _HpnicfDHCPSGlobalPoolDomainName_Type(OctetString):
    """Custom type hpnicfDHCPSGlobalPoolDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfDHCPSGlobalPoolDomainName_Type.__name__ = "OctetString"
_HpnicfDHCPSGlobalPoolDomainName_Object = MibTableColumn
hpnicfDHCPSGlobalPoolDomainName = _HpnicfDHCPSGlobalPoolDomainName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 3, 1, 5),
    _HpnicfDHCPSGlobalPoolDomainName_Type()
)
hpnicfDHCPSGlobalPoolDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolDomainName.setStatus("current")


class _HpnicfDHCPSGlobalPoolClientGatewayIPString_Type(OctetString):
    """Custom type hpnicfDHCPSGlobalPoolClientGatewayIPString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_HpnicfDHCPSGlobalPoolClientGatewayIPString_Type.__name__ = "OctetString"
_HpnicfDHCPSGlobalPoolClientGatewayIPString_Object = MibTableColumn
hpnicfDHCPSGlobalPoolClientGatewayIPString = _HpnicfDHCPSGlobalPoolClientGatewayIPString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 3, 1, 6),
    _HpnicfDHCPSGlobalPoolClientGatewayIPString_Type()
)
hpnicfDHCPSGlobalPoolClientGatewayIPString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolClientGatewayIPString.setStatus("current")
_HpnicfDHCPSGlobalPoolClientGatewayIPUndo_Type = IpAddress
_HpnicfDHCPSGlobalPoolClientGatewayIPUndo_Object = MibTableColumn
hpnicfDHCPSGlobalPoolClientGatewayIPUndo = _HpnicfDHCPSGlobalPoolClientGatewayIPUndo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 3, 1, 7),
    _HpnicfDHCPSGlobalPoolClientGatewayIPUndo_Type()
)
hpnicfDHCPSGlobalPoolClientGatewayIPUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolClientGatewayIPUndo.setStatus("current")


class _HpnicfDHCPSGlobalPoolClientDNSIPString_Type(OctetString):
    """Custom type hpnicfDHCPSGlobalPoolClientDNSIPString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_HpnicfDHCPSGlobalPoolClientDNSIPString_Type.__name__ = "OctetString"
_HpnicfDHCPSGlobalPoolClientDNSIPString_Object = MibTableColumn
hpnicfDHCPSGlobalPoolClientDNSIPString = _HpnicfDHCPSGlobalPoolClientDNSIPString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 3, 1, 8),
    _HpnicfDHCPSGlobalPoolClientDNSIPString_Type()
)
hpnicfDHCPSGlobalPoolClientDNSIPString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolClientDNSIPString.setStatus("current")
_HpnicfDHCPSGlobalPoolClientDNSIPUndo_Type = IpAddress
_HpnicfDHCPSGlobalPoolClientDNSIPUndo_Object = MibTableColumn
hpnicfDHCPSGlobalPoolClientDNSIPUndo = _HpnicfDHCPSGlobalPoolClientDNSIPUndo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 3, 1, 9),
    _HpnicfDHCPSGlobalPoolClientDNSIPUndo_Type()
)
hpnicfDHCPSGlobalPoolClientDNSIPUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolClientDNSIPUndo.setStatus("current")


class _HpnicfDHCPSGlobalPoolClientNetbiosType_Type(Integer32):
    """Custom type hpnicfDHCPSGlobalPoolClientNetbiosType based on Integer32"""
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


_HpnicfDHCPSGlobalPoolClientNetbiosType_Type.__name__ = "Integer32"
_HpnicfDHCPSGlobalPoolClientNetbiosType_Object = MibTableColumn
hpnicfDHCPSGlobalPoolClientNetbiosType = _HpnicfDHCPSGlobalPoolClientNetbiosType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 3, 1, 10),
    _HpnicfDHCPSGlobalPoolClientNetbiosType_Type()
)
hpnicfDHCPSGlobalPoolClientNetbiosType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolClientNetbiosType.setStatus("current")


class _HpnicfDHCPSGlobalPoolClientNbnsIPString_Type(OctetString):
    """Custom type hpnicfDHCPSGlobalPoolClientNbnsIPString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_HpnicfDHCPSGlobalPoolClientNbnsIPString_Type.__name__ = "OctetString"
_HpnicfDHCPSGlobalPoolClientNbnsIPString_Object = MibTableColumn
hpnicfDHCPSGlobalPoolClientNbnsIPString = _HpnicfDHCPSGlobalPoolClientNbnsIPString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 3, 1, 11),
    _HpnicfDHCPSGlobalPoolClientNbnsIPString_Type()
)
hpnicfDHCPSGlobalPoolClientNbnsIPString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolClientNbnsIPString.setStatus("current")
_HpnicfDHCPSGlobalPoolClientNbnsIPUndo_Type = IpAddress
_HpnicfDHCPSGlobalPoolClientNbnsIPUndo_Object = MibTableColumn
hpnicfDHCPSGlobalPoolClientNbnsIPUndo = _HpnicfDHCPSGlobalPoolClientNbnsIPUndo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 3, 1, 12),
    _HpnicfDHCPSGlobalPoolClientNbnsIPUndo_Type()
)
hpnicfDHCPSGlobalPoolClientNbnsIPUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolClientNbnsIPUndo.setStatus("current")


class _HpnicfDHCPSGlobalPoolParaUndoFlag_Type(Integer32):
    """Custom type hpnicfDHCPSGlobalPoolParaUndoFlag based on Integer32"""
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


_HpnicfDHCPSGlobalPoolParaUndoFlag_Type.__name__ = "Integer32"
_HpnicfDHCPSGlobalPoolParaUndoFlag_Object = MibTableColumn
hpnicfDHCPSGlobalPoolParaUndoFlag = _HpnicfDHCPSGlobalPoolParaUndoFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 3, 1, 13),
    _HpnicfDHCPSGlobalPoolParaUndoFlag_Type()
)
hpnicfDHCPSGlobalPoolParaUndoFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolParaUndoFlag.setStatus("current")


class _HpnicfDHCPSGlobalPoolIPInUseReset_Type(Integer32):
    """Custom type hpnicfDHCPSGlobalPoolIPInUseReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HpnicfDHCPSGlobalPoolIPInUseReset_Type.__name__ = "Integer32"
_HpnicfDHCPSGlobalPoolIPInUseReset_Object = MibTableColumn
hpnicfDHCPSGlobalPoolIPInUseReset = _HpnicfDHCPSGlobalPoolIPInUseReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 3, 1, 14),
    _HpnicfDHCPSGlobalPoolIPInUseReset_Type()
)
hpnicfDHCPSGlobalPoolIPInUseReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolIPInUseReset.setStatus("current")
_HpnicfDHCPSGlobalPoolOptionTable_Object = MibTable
hpnicfDHCPSGlobalPoolOptionTable = _HpnicfDHCPSGlobalPoolOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolOptionTable.setStatus("current")
_HpnicfDHCPSGlobalPoolOptionEntry_Object = MibTableRow
hpnicfDHCPSGlobalPoolOptionEntry = _HpnicfDHCPSGlobalPoolOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 4, 1)
)
hpnicfDHCPSGlobalPoolOptionEntry.setIndexNames(
    (0, "HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolName"),
    (0, "HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolOptionCode"),
)
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolOptionEntry.setStatus("current")


class _HpnicfDHCPSGlobalPoolOptionCode_Type(Integer32):
    """Custom type hpnicfDHCPSGlobalPoolOptionCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_HpnicfDHCPSGlobalPoolOptionCode_Type.__name__ = "Integer32"
_HpnicfDHCPSGlobalPoolOptionCode_Object = MibTableColumn
hpnicfDHCPSGlobalPoolOptionCode = _HpnicfDHCPSGlobalPoolOptionCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 4, 1, 1),
    _HpnicfDHCPSGlobalPoolOptionCode_Type()
)
hpnicfDHCPSGlobalPoolOptionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolOptionCode.setStatus("current")


class _HpnicfDHCPSGlobalPoolOptionType_Type(Integer32):
    """Custom type hpnicfDHCPSGlobalPoolOptionType based on Integer32"""
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


_HpnicfDHCPSGlobalPoolOptionType_Type.__name__ = "Integer32"
_HpnicfDHCPSGlobalPoolOptionType_Object = MibTableColumn
hpnicfDHCPSGlobalPoolOptionType = _HpnicfDHCPSGlobalPoolOptionType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 4, 1, 2),
    _HpnicfDHCPSGlobalPoolOptionType_Type()
)
hpnicfDHCPSGlobalPoolOptionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolOptionType.setStatus("current")


class _HpnicfDHCPSGlobalPoolOptionAscii_Type(OctetString):
    """Custom type hpnicfDHCPSGlobalPoolOptionAscii based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpnicfDHCPSGlobalPoolOptionAscii_Type.__name__ = "OctetString"
_HpnicfDHCPSGlobalPoolOptionAscii_Object = MibTableColumn
hpnicfDHCPSGlobalPoolOptionAscii = _HpnicfDHCPSGlobalPoolOptionAscii_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 4, 1, 3),
    _HpnicfDHCPSGlobalPoolOptionAscii_Type()
)
hpnicfDHCPSGlobalPoolOptionAscii.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolOptionAscii.setStatus("current")


class _HpnicfDHCPSGlobalPoolOptionHexString_Type(OctetString):
    """Custom type hpnicfDHCPSGlobalPoolOptionHexString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 143),
    )


_HpnicfDHCPSGlobalPoolOptionHexString_Type.__name__ = "OctetString"
_HpnicfDHCPSGlobalPoolOptionHexString_Object = MibTableColumn
hpnicfDHCPSGlobalPoolOptionHexString = _HpnicfDHCPSGlobalPoolOptionHexString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 4, 1, 4),
    _HpnicfDHCPSGlobalPoolOptionHexString_Type()
)
hpnicfDHCPSGlobalPoolOptionHexString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolOptionHexString.setStatus("current")


class _HpnicfDHCPSGlobalPoolOptionIPString_Type(OctetString):
    """Custom type hpnicfDHCPSGlobalPoolOptionIPString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_HpnicfDHCPSGlobalPoolOptionIPString_Type.__name__ = "OctetString"
_HpnicfDHCPSGlobalPoolOptionIPString_Object = MibTableColumn
hpnicfDHCPSGlobalPoolOptionIPString = _HpnicfDHCPSGlobalPoolOptionIPString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 4, 1, 5),
    _HpnicfDHCPSGlobalPoolOptionIPString_Type()
)
hpnicfDHCPSGlobalPoolOptionIPString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolOptionIPString.setStatus("current")
_HpnicfDHCPSGlobalPoolOptionRowStatus_Type = RowStatus
_HpnicfDHCPSGlobalPoolOptionRowStatus_Object = MibTableColumn
hpnicfDHCPSGlobalPoolOptionRowStatus = _HpnicfDHCPSGlobalPoolOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 4, 1, 6),
    _HpnicfDHCPSGlobalPoolOptionRowStatus_Type()
)
hpnicfDHCPSGlobalPoolOptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolOptionRowStatus.setStatus("current")
_HpnicfDHCPSGlobalTreeTable_Object = MibTable
hpnicfDHCPSGlobalTreeTable = _HpnicfDHCPSGlobalTreeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 5)
)
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalTreeTable.setStatus("current")
_HpnicfDHCPSGlobalTreeEntry_Object = MibTableRow
hpnicfDHCPSGlobalTreeEntry = _HpnicfDHCPSGlobalTreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 5, 1)
)
hpnicfDHCPSGlobalTreeEntry.setIndexNames(
    (0, "HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolName"),
)
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalTreeEntry.setStatus("current")


class _HpnicfDHCPSGlobalTreeParentNodeName_Type(OctetString):
    """Custom type hpnicfDHCPSGlobalTreeParentNodeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfDHCPSGlobalTreeParentNodeName_Type.__name__ = "OctetString"
_HpnicfDHCPSGlobalTreeParentNodeName_Object = MibTableColumn
hpnicfDHCPSGlobalTreeParentNodeName = _HpnicfDHCPSGlobalTreeParentNodeName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 5, 1, 1),
    _HpnicfDHCPSGlobalTreeParentNodeName_Type()
)
hpnicfDHCPSGlobalTreeParentNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalTreeParentNodeName.setStatus("current")


class _HpnicfDHCPSGlobalTreeChildNodeName_Type(OctetString):
    """Custom type hpnicfDHCPSGlobalTreeChildNodeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfDHCPSGlobalTreeChildNodeName_Type.__name__ = "OctetString"
_HpnicfDHCPSGlobalTreeChildNodeName_Object = MibTableColumn
hpnicfDHCPSGlobalTreeChildNodeName = _HpnicfDHCPSGlobalTreeChildNodeName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 5, 1, 2),
    _HpnicfDHCPSGlobalTreeChildNodeName_Type()
)
hpnicfDHCPSGlobalTreeChildNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalTreeChildNodeName.setStatus("current")


class _HpnicfDHCPSGlobalTreePreSiblingNodeName_Type(OctetString):
    """Custom type hpnicfDHCPSGlobalTreePreSiblingNodeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfDHCPSGlobalTreePreSiblingNodeName_Type.__name__ = "OctetString"
_HpnicfDHCPSGlobalTreePreSiblingNodeName_Object = MibTableColumn
hpnicfDHCPSGlobalTreePreSiblingNodeName = _HpnicfDHCPSGlobalTreePreSiblingNodeName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 5, 1, 3),
    _HpnicfDHCPSGlobalTreePreSiblingNodeName_Type()
)
hpnicfDHCPSGlobalTreePreSiblingNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalTreePreSiblingNodeName.setStatus("current")


class _HpnicfDHCPSGlobalTreeSiblingNodeName_Type(OctetString):
    """Custom type hpnicfDHCPSGlobalTreeSiblingNodeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfDHCPSGlobalTreeSiblingNodeName_Type.__name__ = "OctetString"
_HpnicfDHCPSGlobalTreeSiblingNodeName_Object = MibTableColumn
hpnicfDHCPSGlobalTreeSiblingNodeName = _HpnicfDHCPSGlobalTreeSiblingNodeName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 5, 1, 4),
    _HpnicfDHCPSGlobalTreeSiblingNodeName_Type()
)
hpnicfDHCPSGlobalTreeSiblingNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalTreeSiblingNodeName.setStatus("current")
_HpnicfDHCPSInterfacePoolParaTable_Object = MibTable
hpnicfDHCPSInterfacePoolParaTable = _HpnicfDHCPSInterfacePoolParaTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 6)
)
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolParaTable.setStatus("current")
_HpnicfDHCPSInterfacePoolParaEntry_Object = MibTableRow
hpnicfDHCPSInterfacePoolParaEntry = _HpnicfDHCPSInterfacePoolParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 6, 1)
)
hpnicfDHCPSInterfacePoolParaEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolParaEntry.setStatus("current")


class _HpnicfDHCPSInterfacePoolLeaseDay_Type(Integer32):
    """Custom type hpnicfDHCPSInterfacePoolLeaseDay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_HpnicfDHCPSInterfacePoolLeaseDay_Type.__name__ = "Integer32"
_HpnicfDHCPSInterfacePoolLeaseDay_Object = MibTableColumn
hpnicfDHCPSInterfacePoolLeaseDay = _HpnicfDHCPSInterfacePoolLeaseDay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 6, 1, 1),
    _HpnicfDHCPSInterfacePoolLeaseDay_Type()
)
hpnicfDHCPSInterfacePoolLeaseDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolLeaseDay.setStatus("current")


class _HpnicfDHCPSInterfacePoolLeaseHour_Type(Integer32):
    """Custom type hpnicfDHCPSInterfacePoolLeaseHour based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_HpnicfDHCPSInterfacePoolLeaseHour_Type.__name__ = "Integer32"
_HpnicfDHCPSInterfacePoolLeaseHour_Object = MibTableColumn
hpnicfDHCPSInterfacePoolLeaseHour = _HpnicfDHCPSInterfacePoolLeaseHour_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 6, 1, 2),
    _HpnicfDHCPSInterfacePoolLeaseHour_Type()
)
hpnicfDHCPSInterfacePoolLeaseHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolLeaseHour.setStatus("current")


class _HpnicfDHCPSInterfacePoolLeaseMinute_Type(Integer32):
    """Custom type hpnicfDHCPSInterfacePoolLeaseMinute based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_HpnicfDHCPSInterfacePoolLeaseMinute_Type.__name__ = "Integer32"
_HpnicfDHCPSInterfacePoolLeaseMinute_Object = MibTableColumn
hpnicfDHCPSInterfacePoolLeaseMinute = _HpnicfDHCPSInterfacePoolLeaseMinute_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 6, 1, 3),
    _HpnicfDHCPSInterfacePoolLeaseMinute_Type()
)
hpnicfDHCPSInterfacePoolLeaseMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolLeaseMinute.setStatus("current")


class _HpnicfDHCPSInterfacePoolLeaseUnlimited_Type(Integer32):
    """Custom type hpnicfDHCPSInterfacePoolLeaseUnlimited based on Integer32"""
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


_HpnicfDHCPSInterfacePoolLeaseUnlimited_Type.__name__ = "Integer32"
_HpnicfDHCPSInterfacePoolLeaseUnlimited_Object = MibTableColumn
hpnicfDHCPSInterfacePoolLeaseUnlimited = _HpnicfDHCPSInterfacePoolLeaseUnlimited_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 6, 1, 4),
    _HpnicfDHCPSInterfacePoolLeaseUnlimited_Type()
)
hpnicfDHCPSInterfacePoolLeaseUnlimited.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolLeaseUnlimited.setStatus("current")


class _HpnicfDHCPSInterfacePoolDomainName_Type(OctetString):
    """Custom type hpnicfDHCPSInterfacePoolDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfDHCPSInterfacePoolDomainName_Type.__name__ = "OctetString"
_HpnicfDHCPSInterfacePoolDomainName_Object = MibTableColumn
hpnicfDHCPSInterfacePoolDomainName = _HpnicfDHCPSInterfacePoolDomainName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 6, 1, 5),
    _HpnicfDHCPSInterfacePoolDomainName_Type()
)
hpnicfDHCPSInterfacePoolDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolDomainName.setStatus("current")


class _HpnicfDHCPSInterfacePoolClientDNSIPString_Type(OctetString):
    """Custom type hpnicfDHCPSInterfacePoolClientDNSIPString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_HpnicfDHCPSInterfacePoolClientDNSIPString_Type.__name__ = "OctetString"
_HpnicfDHCPSInterfacePoolClientDNSIPString_Object = MibTableColumn
hpnicfDHCPSInterfacePoolClientDNSIPString = _HpnicfDHCPSInterfacePoolClientDNSIPString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 6, 1, 6),
    _HpnicfDHCPSInterfacePoolClientDNSIPString_Type()
)
hpnicfDHCPSInterfacePoolClientDNSIPString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolClientDNSIPString.setStatus("current")
_HpnicfDHCPSInterfacePoolClientDNSIPUndo_Type = IpAddress
_HpnicfDHCPSInterfacePoolClientDNSIPUndo_Object = MibTableColumn
hpnicfDHCPSInterfacePoolClientDNSIPUndo = _HpnicfDHCPSInterfacePoolClientDNSIPUndo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 6, 1, 7),
    _HpnicfDHCPSInterfacePoolClientDNSIPUndo_Type()
)
hpnicfDHCPSInterfacePoolClientDNSIPUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolClientDNSIPUndo.setStatus("current")


class _HpnicfDHCPSInterfacePoolClientNetbiosType_Type(Integer32):
    """Custom type hpnicfDHCPSInterfacePoolClientNetbiosType based on Integer32"""
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


_HpnicfDHCPSInterfacePoolClientNetbiosType_Type.__name__ = "Integer32"
_HpnicfDHCPSInterfacePoolClientNetbiosType_Object = MibTableColumn
hpnicfDHCPSInterfacePoolClientNetbiosType = _HpnicfDHCPSInterfacePoolClientNetbiosType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 6, 1, 8),
    _HpnicfDHCPSInterfacePoolClientNetbiosType_Type()
)
hpnicfDHCPSInterfacePoolClientNetbiosType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolClientNetbiosType.setStatus("current")


class _HpnicfDHCPSInterfacePoolClientNbnsIPString_Type(OctetString):
    """Custom type hpnicfDHCPSInterfacePoolClientNbnsIPString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_HpnicfDHCPSInterfacePoolClientNbnsIPString_Type.__name__ = "OctetString"
_HpnicfDHCPSInterfacePoolClientNbnsIPString_Object = MibTableColumn
hpnicfDHCPSInterfacePoolClientNbnsIPString = _HpnicfDHCPSInterfacePoolClientNbnsIPString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 6, 1, 9),
    _HpnicfDHCPSInterfacePoolClientNbnsIPString_Type()
)
hpnicfDHCPSInterfacePoolClientNbnsIPString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolClientNbnsIPString.setStatus("current")
_HpnicfDHCPSInterfacePoolClientNbnsIPUndo_Type = IpAddress
_HpnicfDHCPSInterfacePoolClientNbnsIPUndo_Object = MibTableColumn
hpnicfDHCPSInterfacePoolClientNbnsIPUndo = _HpnicfDHCPSInterfacePoolClientNbnsIPUndo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 6, 1, 10),
    _HpnicfDHCPSInterfacePoolClientNbnsIPUndo_Type()
)
hpnicfDHCPSInterfacePoolClientNbnsIPUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolClientNbnsIPUndo.setStatus("current")


class _HpnicfDHCPSInterfacePoolParaUndoFlag_Type(Integer32):
    """Custom type hpnicfDHCPSInterfacePoolParaUndoFlag based on Integer32"""
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


_HpnicfDHCPSInterfacePoolParaUndoFlag_Type.__name__ = "Integer32"
_HpnicfDHCPSInterfacePoolParaUndoFlag_Object = MibTableColumn
hpnicfDHCPSInterfacePoolParaUndoFlag = _HpnicfDHCPSInterfacePoolParaUndoFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 6, 1, 11),
    _HpnicfDHCPSInterfacePoolParaUndoFlag_Type()
)
hpnicfDHCPSInterfacePoolParaUndoFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolParaUndoFlag.setStatus("current")


class _HpnicfDHCPSInterfacePoolIPInUseReset_Type(Integer32):
    """Custom type hpnicfDHCPSInterfacePoolIPInUseReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HpnicfDHCPSInterfacePoolIPInUseReset_Type.__name__ = "Integer32"
_HpnicfDHCPSInterfacePoolIPInUseReset_Object = MibTableColumn
hpnicfDHCPSInterfacePoolIPInUseReset = _HpnicfDHCPSInterfacePoolIPInUseReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 6, 1, 12),
    _HpnicfDHCPSInterfacePoolIPInUseReset_Type()
)
hpnicfDHCPSInterfacePoolIPInUseReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolIPInUseReset.setStatus("current")
_HpnicfDHCPSInterfacePoolOptionTable_Object = MibTable
hpnicfDHCPSInterfacePoolOptionTable = _HpnicfDHCPSInterfacePoolOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 7)
)
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolOptionTable.setStatus("current")
_HpnicfDHCPSInterfacePoolOptionEntry_Object = MibTableRow
hpnicfDHCPSInterfacePoolOptionEntry = _HpnicfDHCPSInterfacePoolOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 7, 1)
)
hpnicfDHCPSInterfacePoolOptionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-DHCPS-MIB", "hpnicfDHCPSInterfacePoolOptionCode"),
)
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolOptionEntry.setStatus("current")


class _HpnicfDHCPSInterfacePoolOptionCode_Type(Integer32):
    """Custom type hpnicfDHCPSInterfacePoolOptionCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_HpnicfDHCPSInterfacePoolOptionCode_Type.__name__ = "Integer32"
_HpnicfDHCPSInterfacePoolOptionCode_Object = MibTableColumn
hpnicfDHCPSInterfacePoolOptionCode = _HpnicfDHCPSInterfacePoolOptionCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 7, 1, 1),
    _HpnicfDHCPSInterfacePoolOptionCode_Type()
)
hpnicfDHCPSInterfacePoolOptionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolOptionCode.setStatus("current")


class _HpnicfDHCPSInterfacePoolOptionType_Type(Integer32):
    """Custom type hpnicfDHCPSInterfacePoolOptionType based on Integer32"""
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


_HpnicfDHCPSInterfacePoolOptionType_Type.__name__ = "Integer32"
_HpnicfDHCPSInterfacePoolOptionType_Object = MibTableColumn
hpnicfDHCPSInterfacePoolOptionType = _HpnicfDHCPSInterfacePoolOptionType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 7, 1, 2),
    _HpnicfDHCPSInterfacePoolOptionType_Type()
)
hpnicfDHCPSInterfacePoolOptionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolOptionType.setStatus("current")


class _HpnicfDHCPSInterfacePoolOptionAscii_Type(OctetString):
    """Custom type hpnicfDHCPSInterfacePoolOptionAscii based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpnicfDHCPSInterfacePoolOptionAscii_Type.__name__ = "OctetString"
_HpnicfDHCPSInterfacePoolOptionAscii_Object = MibTableColumn
hpnicfDHCPSInterfacePoolOptionAscii = _HpnicfDHCPSInterfacePoolOptionAscii_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 7, 1, 3),
    _HpnicfDHCPSInterfacePoolOptionAscii_Type()
)
hpnicfDHCPSInterfacePoolOptionAscii.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolOptionAscii.setStatus("current")


class _HpnicfDHCPSInterfacePoolOptionHexString_Type(OctetString):
    """Custom type hpnicfDHCPSInterfacePoolOptionHexString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 143),
    )


_HpnicfDHCPSInterfacePoolOptionHexString_Type.__name__ = "OctetString"
_HpnicfDHCPSInterfacePoolOptionHexString_Object = MibTableColumn
hpnicfDHCPSInterfacePoolOptionHexString = _HpnicfDHCPSInterfacePoolOptionHexString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 7, 1, 4),
    _HpnicfDHCPSInterfacePoolOptionHexString_Type()
)
hpnicfDHCPSInterfacePoolOptionHexString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolOptionHexString.setStatus("current")


class _HpnicfDHCPSInterfacePoolOptionIPString_Type(OctetString):
    """Custom type hpnicfDHCPSInterfacePoolOptionIPString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_HpnicfDHCPSInterfacePoolOptionIPString_Type.__name__ = "OctetString"
_HpnicfDHCPSInterfacePoolOptionIPString_Object = MibTableColumn
hpnicfDHCPSInterfacePoolOptionIPString = _HpnicfDHCPSInterfacePoolOptionIPString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 7, 1, 5),
    _HpnicfDHCPSInterfacePoolOptionIPString_Type()
)
hpnicfDHCPSInterfacePoolOptionIPString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolOptionIPString.setStatus("current")
_HpnicfDHCPSInterfacePoolOptionRowStatus_Type = RowStatus
_HpnicfDHCPSInterfacePoolOptionRowStatus_Object = MibTableColumn
hpnicfDHCPSInterfacePoolOptionRowStatus = _HpnicfDHCPSInterfacePoolOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 7, 1, 6),
    _HpnicfDHCPSInterfacePoolOptionRowStatus_Type()
)
hpnicfDHCPSInterfacePoolOptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolOptionRowStatus.setStatus("current")
_HpnicfDHCPSInterfacePoolStaticBindTable_Object = MibTable
hpnicfDHCPSInterfacePoolStaticBindTable = _HpnicfDHCPSInterfacePoolStaticBindTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 8)
)
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolStaticBindTable.setStatus("current")
_HpnicfDHCPSInterfacePoolStaticBindEntry_Object = MibTableRow
hpnicfDHCPSInterfacePoolStaticBindEntry = _HpnicfDHCPSInterfacePoolStaticBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 8, 1)
)
hpnicfDHCPSInterfacePoolStaticBindEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-DHCPS-MIB", "hpnicfDHCPSInterfacePoolStaticBindIP"),
)
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolStaticBindEntry.setStatus("current")
_HpnicfDHCPSInterfacePoolStaticBindIP_Type = IpAddress
_HpnicfDHCPSInterfacePoolStaticBindIP_Object = MibTableColumn
hpnicfDHCPSInterfacePoolStaticBindIP = _HpnicfDHCPSInterfacePoolStaticBindIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 8, 1, 1),
    _HpnicfDHCPSInterfacePoolStaticBindIP_Type()
)
hpnicfDHCPSInterfacePoolStaticBindIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolStaticBindIP.setStatus("current")
_HpnicfDHCPSInterfacePoolStaticBindMac_Type = MacAddress
_HpnicfDHCPSInterfacePoolStaticBindMac_Object = MibTableColumn
hpnicfDHCPSInterfacePoolStaticBindMac = _HpnicfDHCPSInterfacePoolStaticBindMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 8, 1, 2),
    _HpnicfDHCPSInterfacePoolStaticBindMac_Type()
)
hpnicfDHCPSInterfacePoolStaticBindMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolStaticBindMac.setStatus("current")
_HpnicfDHCPSInterfacePoolStaticBindRowStatus_Type = RowStatus
_HpnicfDHCPSInterfacePoolStaticBindRowStatus_Object = MibTableColumn
hpnicfDHCPSInterfacePoolStaticBindRowStatus = _HpnicfDHCPSInterfacePoolStaticBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 8, 1, 3),
    _HpnicfDHCPSInterfacePoolStaticBindRowStatus_Type()
)
hpnicfDHCPSInterfacePoolStaticBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolStaticBindRowStatus.setStatus("current")
_HpnicfDHCPSIPInUseTable_Object = MibTable
hpnicfDHCPSIPInUseTable = _HpnicfDHCPSIPInUseTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 9)
)
if mibBuilder.loadTexts:
    hpnicfDHCPSIPInUseTable.setStatus("deprecated")
_HpnicfDHCPSIPInUseEntry_Object = MibTableRow
hpnicfDHCPSIPInUseEntry = _HpnicfDHCPSIPInUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 9, 1)
)
hpnicfDHCPSIPInUseEntry.setIndexNames(
    (0, "HPN-ICF-DHCPS-MIB", "hpnicfDHCPSIPInUseHAddr"),
)
if mibBuilder.loadTexts:
    hpnicfDHCPSIPInUseEntry.setStatus("deprecated")
_HpnicfDHCPSIPInUseHAddr_Type = MacAddress
_HpnicfDHCPSIPInUseHAddr_Object = MibTableColumn
hpnicfDHCPSIPInUseHAddr = _HpnicfDHCPSIPInUseHAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 9, 1, 1),
    _HpnicfDHCPSIPInUseHAddr_Type()
)
hpnicfDHCPSIPInUseHAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSIPInUseHAddr.setStatus("deprecated")
_HpnicfDHCPSIPInUseIP_Type = IpAddress
_HpnicfDHCPSIPInUseIP_Object = MibTableColumn
hpnicfDHCPSIPInUseIP = _HpnicfDHCPSIPInUseIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 9, 1, 2),
    _HpnicfDHCPSIPInUseIP_Type()
)
hpnicfDHCPSIPInUseIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSIPInUseIP.setStatus("deprecated")


class _HpnicfDHCPSIPInUseEndLease_Type(OctetString):
    """Custom type hpnicfDHCPSIPInUseEndLease based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_HpnicfDHCPSIPInUseEndLease_Type.__name__ = "OctetString"
_HpnicfDHCPSIPInUseEndLease_Object = MibTableColumn
hpnicfDHCPSIPInUseEndLease = _HpnicfDHCPSIPInUseEndLease_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 9, 1, 3),
    _HpnicfDHCPSIPInUseEndLease_Type()
)
hpnicfDHCPSIPInUseEndLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSIPInUseEndLease.setStatus("deprecated")


class _HpnicfDHCPSIPInUseType_Type(Integer32):
    """Custom type hpnicfDHCPSIPInUseType based on Integer32"""
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


_HpnicfDHCPSIPInUseType_Type.__name__ = "Integer32"
_HpnicfDHCPSIPInUseType_Object = MibTableColumn
hpnicfDHCPSIPInUseType = _HpnicfDHCPSIPInUseType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 9, 1, 4),
    _HpnicfDHCPSIPInUseType_Type()
)
hpnicfDHCPSIPInUseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSIPInUseType.setStatus("deprecated")


class _HpnicfDHCPSIPInUsePoolName_Type(OctetString):
    """Custom type hpnicfDHCPSIPInUsePoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HpnicfDHCPSIPInUsePoolName_Type.__name__ = "OctetString"
_HpnicfDHCPSIPInUsePoolName_Object = MibTableColumn
hpnicfDHCPSIPInUsePoolName = _HpnicfDHCPSIPInUsePoolName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 9, 1, 5),
    _HpnicfDHCPSIPInUsePoolName_Type()
)
hpnicfDHCPSIPInUsePoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSIPInUsePoolName.setStatus("deprecated")
_HpnicfDHCPSIPInUseInterface_Type = Integer32
_HpnicfDHCPSIPInUseInterface_Object = MibTableColumn
hpnicfDHCPSIPInUseInterface = _HpnicfDHCPSIPInUseInterface_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 9, 1, 6),
    _HpnicfDHCPSIPInUseInterface_Type()
)
hpnicfDHCPSIPInUseInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSIPInUseInterface.setStatus("deprecated")


class _HpnicfDHCPSIPInUseVlan_Type(Integer32):
    """Custom type hpnicfDHCPSIPInUseVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpnicfDHCPSIPInUseVlan_Type.__name__ = "Integer32"
_HpnicfDHCPSIPInUseVlan_Object = MibTableColumn
hpnicfDHCPSIPInUseVlan = _HpnicfDHCPSIPInUseVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 9, 1, 7),
    _HpnicfDHCPSIPInUseVlan_Type()
)
hpnicfDHCPSIPInUseVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSIPInUseVlan.setStatus("deprecated")
_HpnicfDHCPSIPInUseAtmpvc_Type = Integer32
_HpnicfDHCPSIPInUseAtmpvc_Object = MibTableColumn
hpnicfDHCPSIPInUseAtmpvc = _HpnicfDHCPSIPInUseAtmpvc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 9, 1, 8),
    _HpnicfDHCPSIPInUseAtmpvc_Type()
)
hpnicfDHCPSIPInUseAtmpvc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSIPInUseAtmpvc.setStatus("deprecated")
_HpnicfDHCPSForbiddenIPTable_Object = MibTable
hpnicfDHCPSForbiddenIPTable = _HpnicfDHCPSForbiddenIPTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 10)
)
if mibBuilder.loadTexts:
    hpnicfDHCPSForbiddenIPTable.setStatus("current")
_HpnicfDHCPSForbiddenIPEntry_Object = MibTableRow
hpnicfDHCPSForbiddenIPEntry = _HpnicfDHCPSForbiddenIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 10, 1)
)
hpnicfDHCPSForbiddenIPEntry.setIndexNames(
    (0, "HPN-ICF-DHCPS-MIB", "hpnicfDHCPSForbiddenIPStart"),
    (0, "HPN-ICF-DHCPS-MIB", "hpnicfDHCPSForbiddenIPEnd"),
)
if mibBuilder.loadTexts:
    hpnicfDHCPSForbiddenIPEntry.setStatus("current")
_HpnicfDHCPSForbiddenIPStart_Type = IpAddress
_HpnicfDHCPSForbiddenIPStart_Object = MibTableColumn
hpnicfDHCPSForbiddenIPStart = _HpnicfDHCPSForbiddenIPStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 10, 1, 1),
    _HpnicfDHCPSForbiddenIPStart_Type()
)
hpnicfDHCPSForbiddenIPStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSForbiddenIPStart.setStatus("current")
_HpnicfDHCPSForbiddenIPEnd_Type = IpAddress
_HpnicfDHCPSForbiddenIPEnd_Object = MibTableColumn
hpnicfDHCPSForbiddenIPEnd = _HpnicfDHCPSForbiddenIPEnd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 10, 1, 2),
    _HpnicfDHCPSForbiddenIPEnd_Type()
)
hpnicfDHCPSForbiddenIPEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSForbiddenIPEnd.setStatus("current")
_HpnicfDHCPSForbiddenIPRowStatus_Type = RowStatus
_HpnicfDHCPSForbiddenIPRowStatus_Object = MibTableColumn
hpnicfDHCPSForbiddenIPRowStatus = _HpnicfDHCPSForbiddenIPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 10, 1, 3),
    _HpnicfDHCPSForbiddenIPRowStatus_Type()
)
hpnicfDHCPSForbiddenIPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPSForbiddenIPRowStatus.setStatus("current")
_HpnicfDHCPSConflictIPTable_Object = MibTable
hpnicfDHCPSConflictIPTable = _HpnicfDHCPSConflictIPTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 11)
)
if mibBuilder.loadTexts:
    hpnicfDHCPSConflictIPTable.setStatus("current")
_HpnicfDHCPSConflictIPEntry_Object = MibTableRow
hpnicfDHCPSConflictIPEntry = _HpnicfDHCPSConflictIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 11, 1)
)
hpnicfDHCPSConflictIPEntry.setIndexNames(
    (0, "HPN-ICF-DHCPS-MIB", "hpnicfDHCPSConflictIP"),
)
if mibBuilder.loadTexts:
    hpnicfDHCPSConflictIPEntry.setStatus("current")
_HpnicfDHCPSConflictIP_Type = IpAddress
_HpnicfDHCPSConflictIP_Object = MibTableColumn
hpnicfDHCPSConflictIP = _HpnicfDHCPSConflictIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 11, 1, 1),
    _HpnicfDHCPSConflictIP_Type()
)
hpnicfDHCPSConflictIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSConflictIP.setStatus("current")


class _HpnicfDHCPSConflictIPType_Type(Integer32):
    """Custom type hpnicfDHCPSConflictIPType based on Integer32"""
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


_HpnicfDHCPSConflictIPType_Type.__name__ = "Integer32"
_HpnicfDHCPSConflictIPType_Object = MibTableColumn
hpnicfDHCPSConflictIPType = _HpnicfDHCPSConflictIPType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 11, 1, 2),
    _HpnicfDHCPSConflictIPType_Type()
)
hpnicfDHCPSConflictIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSConflictIPType.setStatus("current")


class _HpnicfDHCPSConflictIPDetectTime_Type(OctetString):
    """Custom type hpnicfDHCPSConflictIPDetectTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_HpnicfDHCPSConflictIPDetectTime_Type.__name__ = "OctetString"
_HpnicfDHCPSConflictIPDetectTime_Object = MibTableColumn
hpnicfDHCPSConflictIPDetectTime = _HpnicfDHCPSConflictIPDetectTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 11, 1, 3),
    _HpnicfDHCPSConflictIPDetectTime_Type()
)
hpnicfDHCPSConflictIPDetectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSConflictIPDetectTime.setStatus("current")


class _HpnicfDHCPSServiceStatus_Type(HpnicfDhcpSEnabledStatus):
    """Custom type hpnicfDHCPSServiceStatus based on HpnicfDhcpSEnabledStatus"""


_HpnicfDHCPSServiceStatus_Object = MibScalar
hpnicfDHCPSServiceStatus = _HpnicfDHCPSServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 12),
    _HpnicfDHCPSServiceStatus_Type()
)
hpnicfDHCPSServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSServiceStatus.setStatus("current")


class _HpnicfDHCPSDetectingServerStatus_Type(HpnicfDhcpSEnabledStatus):
    """Custom type hpnicfDHCPSDetectingServerStatus based on HpnicfDhcpSEnabledStatus"""


_HpnicfDHCPSDetectingServerStatus_Object = MibScalar
hpnicfDHCPSDetectingServerStatus = _HpnicfDHCPSDetectingServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 13),
    _HpnicfDHCPSDetectingServerStatus_Type()
)
hpnicfDHCPSDetectingServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSDetectingServerStatus.setStatus("current")


class _HpnicfDHCPSPingNum_Type(Integer32):
    """Custom type hpnicfDHCPSPingNum based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_HpnicfDHCPSPingNum_Type.__name__ = "Integer32"
_HpnicfDHCPSPingNum_Object = MibScalar
hpnicfDHCPSPingNum = _HpnicfDHCPSPingNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 14),
    _HpnicfDHCPSPingNum_Type()
)
hpnicfDHCPSPingNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSPingNum.setStatus("current")


class _HpnicfDHCPSPingTimeout_Type(Integer32):
    """Custom type hpnicfDHCPSPingTimeout based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HpnicfDHCPSPingTimeout_Type.__name__ = "Integer32"
_HpnicfDHCPSPingTimeout_Object = MibScalar
hpnicfDHCPSPingTimeout = _HpnicfDHCPSPingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 15),
    _HpnicfDHCPSPingTimeout_Type()
)
hpnicfDHCPSPingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSPingTimeout.setStatus("current")


class _HpnicfDHCPSWriteDataStatus_Type(HpnicfDhcpSEnabledStatus):
    """Custom type hpnicfDHCPSWriteDataStatus based on HpnicfDhcpSEnabledStatus"""


_HpnicfDHCPSWriteDataStatus_Object = MibScalar
hpnicfDHCPSWriteDataStatus = _HpnicfDHCPSWriteDataStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 16),
    _HpnicfDHCPSWriteDataStatus_Type()
)
hpnicfDHCPSWriteDataStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSWriteDataStatus.setStatus("current")


class _HpnicfDHCPSWriteDataDirection_Type(OctetString):
    """Custom type hpnicfDHCPSWriteDataDirection based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HpnicfDHCPSWriteDataDirection_Type.__name__ = "OctetString"
_HpnicfDHCPSWriteDataDirection_Object = MibScalar
hpnicfDHCPSWriteDataDirection = _HpnicfDHCPSWriteDataDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 17),
    _HpnicfDHCPSWriteDataDirection_Type()
)
hpnicfDHCPSWriteDataDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSWriteDataDirection.setStatus("current")


class _HpnicfDHCPSWriteDataDelay_Type(Integer32):
    """Custom type hpnicfDHCPSWriteDataDelay based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 86400),
    )


_HpnicfDHCPSWriteDataDelay_Type.__name__ = "Integer32"
_HpnicfDHCPSWriteDataDelay_Object = MibScalar
hpnicfDHCPSWriteDataDelay = _HpnicfDHCPSWriteDataDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 18),
    _HpnicfDHCPSWriteDataDelay_Type()
)
hpnicfDHCPSWriteDataDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSWriteDataDelay.setStatus("current")
_HpnicfDHCPSWriteDataRecover_Type = HpnicfDhcpSEnabledStatus
_HpnicfDHCPSWriteDataRecover_Object = MibScalar
hpnicfDHCPSWriteDataRecover = _HpnicfDHCPSWriteDataRecover_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 19),
    _HpnicfDHCPSWriteDataRecover_Type()
)
hpnicfDHCPSWriteDataRecover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSWriteDataRecover.setStatus("current")
_HpnicfDHCPSIPInUseResetIP_Type = IpAddress
_HpnicfDHCPSIPInUseResetIP_Object = MibScalar
hpnicfDHCPSIPInUseResetIP = _HpnicfDHCPSIPInUseResetIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 20),
    _HpnicfDHCPSIPInUseResetIP_Type()
)
hpnicfDHCPSIPInUseResetIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSIPInUseResetIP.setStatus("current")
_HpnicfDHCPSConflictIPResetIP_Type = IpAddress
_HpnicfDHCPSConflictIPResetIP_Object = MibScalar
hpnicfDHCPSConflictIPResetIP = _HpnicfDHCPSConflictIPResetIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 21),
    _HpnicfDHCPSConflictIPResetIP_Type()
)
hpnicfDHCPSConflictIPResetIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSConflictIPResetIP.setStatus("current")


class _HpnicfDHCPSIPResetFlag_Type(Integer32):
    """Custom type hpnicfDHCPSIPResetFlag based on Integer32"""
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


_HpnicfDHCPSIPResetFlag_Type.__name__ = "Integer32"
_HpnicfDHCPSIPResetFlag_Object = MibScalar
hpnicfDHCPSIPResetFlag = _HpnicfDHCPSIPResetFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 22),
    _HpnicfDHCPSIPResetFlag_Type()
)
hpnicfDHCPSIPResetFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSIPResetFlag.setStatus("current")
_HpnicfDHCPSGlobalPoolNumber_Type = Integer32
_HpnicfDHCPSGlobalPoolNumber_Object = MibScalar
hpnicfDHCPSGlobalPoolNumber = _HpnicfDHCPSGlobalPoolNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 23),
    _HpnicfDHCPSGlobalPoolNumber_Type()
)
hpnicfDHCPSGlobalPoolNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolNumber.setStatus("current")
_HpnicfDHCPSGlobalPoolAutoBindingNum_Type = Integer32
_HpnicfDHCPSGlobalPoolAutoBindingNum_Object = MibScalar
hpnicfDHCPSGlobalPoolAutoBindingNum = _HpnicfDHCPSGlobalPoolAutoBindingNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 24),
    _HpnicfDHCPSGlobalPoolAutoBindingNum_Type()
)
hpnicfDHCPSGlobalPoolAutoBindingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolAutoBindingNum.setStatus("current")
_HpnicfDHCPSGlobalPoolManualBindingNum_Type = Integer32
_HpnicfDHCPSGlobalPoolManualBindingNum_Object = MibScalar
hpnicfDHCPSGlobalPoolManualBindingNum = _HpnicfDHCPSGlobalPoolManualBindingNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 25),
    _HpnicfDHCPSGlobalPoolManualBindingNum_Type()
)
hpnicfDHCPSGlobalPoolManualBindingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolManualBindingNum.setStatus("current")
_HpnicfDHCPSGlobalPoolExpiredBindingNum_Type = Integer32
_HpnicfDHCPSGlobalPoolExpiredBindingNum_Object = MibScalar
hpnicfDHCPSGlobalPoolExpiredBindingNum = _HpnicfDHCPSGlobalPoolExpiredBindingNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 26),
    _HpnicfDHCPSGlobalPoolExpiredBindingNum_Type()
)
hpnicfDHCPSGlobalPoolExpiredBindingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSGlobalPoolExpiredBindingNum.setStatus("current")
_HpnicfDHCPSInterfacePoolNumber_Type = Integer32
_HpnicfDHCPSInterfacePoolNumber_Object = MibScalar
hpnicfDHCPSInterfacePoolNumber = _HpnicfDHCPSInterfacePoolNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 27),
    _HpnicfDHCPSInterfacePoolNumber_Type()
)
hpnicfDHCPSInterfacePoolNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolNumber.setStatus("current")
_HpnicfDHCPSInterfacePoolAutoBindingNum_Type = Integer32
_HpnicfDHCPSInterfacePoolAutoBindingNum_Object = MibScalar
hpnicfDHCPSInterfacePoolAutoBindingNum = _HpnicfDHCPSInterfacePoolAutoBindingNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 28),
    _HpnicfDHCPSInterfacePoolAutoBindingNum_Type()
)
hpnicfDHCPSInterfacePoolAutoBindingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolAutoBindingNum.setStatus("current")
_HpnicfDHCPSInterfacePoolManualBindingNum_Type = Integer32
_HpnicfDHCPSInterfacePoolManualBindingNum_Object = MibScalar
hpnicfDHCPSInterfacePoolManualBindingNum = _HpnicfDHCPSInterfacePoolManualBindingNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 29),
    _HpnicfDHCPSInterfacePoolManualBindingNum_Type()
)
hpnicfDHCPSInterfacePoolManualBindingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolManualBindingNum.setStatus("current")
_HpnicfDHCPSInterfacePoolExpiredBindingNum_Type = Integer32
_HpnicfDHCPSInterfacePoolExpiredBindingNum_Object = MibScalar
hpnicfDHCPSInterfacePoolExpiredBindingNum = _HpnicfDHCPSInterfacePoolExpiredBindingNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 30),
    _HpnicfDHCPSInterfacePoolExpiredBindingNum_Type()
)
hpnicfDHCPSInterfacePoolExpiredBindingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSInterfacePoolExpiredBindingNum.setStatus("current")
_HpnicfDHCPSBadPktNum_Type = Integer32
_HpnicfDHCPSBadPktNum_Object = MibScalar
hpnicfDHCPSBadPktNum = _HpnicfDHCPSBadPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 31),
    _HpnicfDHCPSBadPktNum_Type()
)
hpnicfDHCPSBadPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSBadPktNum.setStatus("current")
_HpnicfDHCPSBootRequestPktNum_Type = Integer32
_HpnicfDHCPSBootRequestPktNum_Object = MibScalar
hpnicfDHCPSBootRequestPktNum = _HpnicfDHCPSBootRequestPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 32),
    _HpnicfDHCPSBootRequestPktNum_Type()
)
hpnicfDHCPSBootRequestPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSBootRequestPktNum.setStatus("current")
_HpnicfDHCPSDiscoverPktNum_Type = Integer32
_HpnicfDHCPSDiscoverPktNum_Object = MibScalar
hpnicfDHCPSDiscoverPktNum = _HpnicfDHCPSDiscoverPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 33),
    _HpnicfDHCPSDiscoverPktNum_Type()
)
hpnicfDHCPSDiscoverPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSDiscoverPktNum.setStatus("current")
_HpnicfDHCPSRequestPktNum_Type = Integer32
_HpnicfDHCPSRequestPktNum_Object = MibScalar
hpnicfDHCPSRequestPktNum = _HpnicfDHCPSRequestPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 34),
    _HpnicfDHCPSRequestPktNum_Type()
)
hpnicfDHCPSRequestPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSRequestPktNum.setStatus("current")
_HpnicfDHCPSDeclinePktNum_Type = Integer32
_HpnicfDHCPSDeclinePktNum_Object = MibScalar
hpnicfDHCPSDeclinePktNum = _HpnicfDHCPSDeclinePktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 35),
    _HpnicfDHCPSDeclinePktNum_Type()
)
hpnicfDHCPSDeclinePktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSDeclinePktNum.setStatus("current")
_HpnicfDHCPSReleasePktNum_Type = Integer32
_HpnicfDHCPSReleasePktNum_Object = MibScalar
hpnicfDHCPSReleasePktNum = _HpnicfDHCPSReleasePktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 36),
    _HpnicfDHCPSReleasePktNum_Type()
)
hpnicfDHCPSReleasePktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSReleasePktNum.setStatus("current")
_HpnicfDHCPSInformPktNum_Type = Integer32
_HpnicfDHCPSInformPktNum_Object = MibScalar
hpnicfDHCPSInformPktNum = _HpnicfDHCPSInformPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 37),
    _HpnicfDHCPSInformPktNum_Type()
)
hpnicfDHCPSInformPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSInformPktNum.setStatus("current")
_HpnicfDHCPSBootReplyPktNum_Type = Integer32
_HpnicfDHCPSBootReplyPktNum_Object = MibScalar
hpnicfDHCPSBootReplyPktNum = _HpnicfDHCPSBootReplyPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 38),
    _HpnicfDHCPSBootReplyPktNum_Type()
)
hpnicfDHCPSBootReplyPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSBootReplyPktNum.setStatus("current")
_HpnicfDHCPSOfferPktNum_Type = Integer32
_HpnicfDHCPSOfferPktNum_Object = MibScalar
hpnicfDHCPSOfferPktNum = _HpnicfDHCPSOfferPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 39),
    _HpnicfDHCPSOfferPktNum_Type()
)
hpnicfDHCPSOfferPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSOfferPktNum.setStatus("current")
_HpnicfDHCPSAckPktNum_Type = Integer32
_HpnicfDHCPSAckPktNum_Object = MibScalar
hpnicfDHCPSAckPktNum = _HpnicfDHCPSAckPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 40),
    _HpnicfDHCPSAckPktNum_Type()
)
hpnicfDHCPSAckPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSAckPktNum.setStatus("current")
_HpnicfDHCPSNakPktNum_Type = Integer32
_HpnicfDHCPSNakPktNum_Object = MibScalar
hpnicfDHCPSNakPktNum = _HpnicfDHCPSNakPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 41),
    _HpnicfDHCPSNakPktNum_Type()
)
hpnicfDHCPSNakPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSNakPktNum.setStatus("current")


class _HpnicfDHCPSStatisticsReset_Type(Integer32):
    """Custom type hpnicfDHCPSStatisticsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HpnicfDHCPSStatisticsReset_Type.__name__ = "Integer32"
_HpnicfDHCPSStatisticsReset_Object = MibScalar
hpnicfDHCPSStatisticsReset = _HpnicfDHCPSStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 42),
    _HpnicfDHCPSStatisticsReset_Type()
)
hpnicfDHCPSStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPSStatisticsReset.setStatus("current")
_HpnicfDHCPSIPInUseExTable_Object = MibTable
hpnicfDHCPSIPInUseExTable = _HpnicfDHCPSIPInUseExTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 43)
)
if mibBuilder.loadTexts:
    hpnicfDHCPSIPInUseExTable.setStatus("current")
_HpnicfDHCPSIPInUseExEntry_Object = MibTableRow
hpnicfDHCPSIPInUseExEntry = _HpnicfDHCPSIPInUseExEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 43, 1)
)
hpnicfDHCPSIPInUseExEntry.setIndexNames(
    (0, "HPN-ICF-DHCPS-MIB", "hpnicfDHCPSIPInUseHAddrEx"),
    (0, "HPN-ICF-DHCPS-MIB", "hpnicfDHCPSIPInUseVlanIdEx"),
)
if mibBuilder.loadTexts:
    hpnicfDHCPSIPInUseExEntry.setStatus("current")
_HpnicfDHCPSIPInUseHAddrEx_Type = MacAddress
_HpnicfDHCPSIPInUseHAddrEx_Object = MibTableColumn
hpnicfDHCPSIPInUseHAddrEx = _HpnicfDHCPSIPInUseHAddrEx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 43, 1, 1),
    _HpnicfDHCPSIPInUseHAddrEx_Type()
)
hpnicfDHCPSIPInUseHAddrEx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDHCPSIPInUseHAddrEx.setStatus("current")


class _HpnicfDHCPSIPInUseVlanIdEx_Type(Integer32):
    """Custom type hpnicfDHCPSIPInUseVlanIdEx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(60000, 60000),
    )


_HpnicfDHCPSIPInUseVlanIdEx_Type.__name__ = "Integer32"
_HpnicfDHCPSIPInUseVlanIdEx_Object = MibTableColumn
hpnicfDHCPSIPInUseVlanIdEx = _HpnicfDHCPSIPInUseVlanIdEx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 43, 1, 2),
    _HpnicfDHCPSIPInUseVlanIdEx_Type()
)
hpnicfDHCPSIPInUseVlanIdEx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDHCPSIPInUseVlanIdEx.setStatus("current")
_HpnicfDHCPSIPInUseIPEx_Type = IpAddress
_HpnicfDHCPSIPInUseIPEx_Object = MibTableColumn
hpnicfDHCPSIPInUseIPEx = _HpnicfDHCPSIPInUseIPEx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 43, 1, 3),
    _HpnicfDHCPSIPInUseIPEx_Type()
)
hpnicfDHCPSIPInUseIPEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSIPInUseIPEx.setStatus("current")


class _HpnicfDHCPSIPInUseEndLeaseEx_Type(OctetString):
    """Custom type hpnicfDHCPSIPInUseEndLeaseEx based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_HpnicfDHCPSIPInUseEndLeaseEx_Type.__name__ = "OctetString"
_HpnicfDHCPSIPInUseEndLeaseEx_Object = MibTableColumn
hpnicfDHCPSIPInUseEndLeaseEx = _HpnicfDHCPSIPInUseEndLeaseEx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 43, 1, 4),
    _HpnicfDHCPSIPInUseEndLeaseEx_Type()
)
hpnicfDHCPSIPInUseEndLeaseEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSIPInUseEndLeaseEx.setStatus("current")


class _HpnicfDHCPSIPInUseTypeEx_Type(Integer32):
    """Custom type hpnicfDHCPSIPInUseTypeEx based on Integer32"""
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


_HpnicfDHCPSIPInUseTypeEx_Type.__name__ = "Integer32"
_HpnicfDHCPSIPInUseTypeEx_Object = MibTableColumn
hpnicfDHCPSIPInUseTypeEx = _HpnicfDHCPSIPInUseTypeEx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 43, 1, 5),
    _HpnicfDHCPSIPInUseTypeEx_Type()
)
hpnicfDHCPSIPInUseTypeEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSIPInUseTypeEx.setStatus("current")


class _HpnicfDHCPSIPInUsePoolNameEx_Type(OctetString):
    """Custom type hpnicfDHCPSIPInUsePoolNameEx based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HpnicfDHCPSIPInUsePoolNameEx_Type.__name__ = "OctetString"
_HpnicfDHCPSIPInUsePoolNameEx_Object = MibTableColumn
hpnicfDHCPSIPInUsePoolNameEx = _HpnicfDHCPSIPInUsePoolNameEx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 43, 1, 6),
    _HpnicfDHCPSIPInUsePoolNameEx_Type()
)
hpnicfDHCPSIPInUsePoolNameEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSIPInUsePoolNameEx.setStatus("current")
_HpnicfDHCPSIPInUseIfIndexEx_Type = Integer32
_HpnicfDHCPSIPInUseIfIndexEx_Object = MibTableColumn
hpnicfDHCPSIPInUseIfIndexEx = _HpnicfDHCPSIPInUseIfIndexEx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 43, 1, 7),
    _HpnicfDHCPSIPInUseIfIndexEx_Type()
)
hpnicfDHCPSIPInUseIfIndexEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSIPInUseIfIndexEx.setStatus("current")


class _HpnicfDHCPSIPInUseServerPortVlanIdEx_Type(Integer32):
    """Custom type hpnicfDHCPSIPInUseServerPortVlanIdEx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpnicfDHCPSIPInUseServerPortVlanIdEx_Type.__name__ = "Integer32"
_HpnicfDHCPSIPInUseServerPortVlanIdEx_Object = MibTableColumn
hpnicfDHCPSIPInUseServerPortVlanIdEx = _HpnicfDHCPSIPInUseServerPortVlanIdEx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 43, 1, 8),
    _HpnicfDHCPSIPInUseServerPortVlanIdEx_Type()
)
hpnicfDHCPSIPInUseServerPortVlanIdEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSIPInUseServerPortVlanIdEx.setStatus("current")
_HpnicfDHCPSIPInUseAtmpvcEx_Type = Integer32
_HpnicfDHCPSIPInUseAtmpvcEx_Object = MibTableColumn
hpnicfDHCPSIPInUseAtmpvcEx = _HpnicfDHCPSIPInUseAtmpvcEx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 1, 43, 1, 9),
    _HpnicfDHCPSIPInUseAtmpvcEx_Type()
)
hpnicfDHCPSIPInUseAtmpvcEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPSIPInUseAtmpvcEx.setStatus("current")
_HpnicfDHCPServerMIBConformance_ObjectIdentity = ObjectIdentity
hpnicfDHCPServerMIBConformance = _HpnicfDHCPServerMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 2)
)
_HpnicfDHCPServerMIBCompliances_ObjectIdentity = ObjectIdentity
hpnicfDHCPServerMIBCompliances = _HpnicfDHCPServerMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 2, 1)
)
_HpnicfDHCPServerMIBGroups_ObjectIdentity = ObjectIdentity
hpnicfDHCPServerMIBGroups = _HpnicfDHCPServerMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 2, 2)
)

# Managed Objects groups

hpnicfDHCPServerMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 2, 2, 2, 1)
)
hpnicfDHCPServerMIBGroup.setObjects(
      *(("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolName"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolRowStatus"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolType"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolNetwork"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolNetworkMask"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolHostIPAddr"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolHostMask"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolHostHAddr"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolConfigUndoFlag"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolLeaseDay"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolLeaseHour"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolLeaseMinute"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolLeaseUnlimited"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolDomainName"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolClientGatewayIPString"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolClientGatewayIPUndo"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolClientDNSIPString"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolClientDNSIPUndo"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolClientNetbiosType"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolClientNbnsIPString"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolClientNbnsIPUndo"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolParaUndoFlag"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolIPInUseReset"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolOptionCode"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolOptionType"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolOptionAscii"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolOptionHexString"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolOptionIPString"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolOptionRowStatus"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalTreeParentNodeName"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalTreeChildNodeName"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalTreePreSiblingNodeName"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalTreeSiblingNodeName"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSInterfacePoolLeaseDay"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSInterfacePoolLeaseHour"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSInterfacePoolLeaseMinute"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSInterfacePoolLeaseUnlimited"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSInterfacePoolDomainName"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSInterfacePoolClientDNSIPString"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSInterfacePoolClientDNSIPUndo"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSInterfacePoolClientNetbiosType"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSInterfacePoolClientNbnsIPString"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSInterfacePoolClientNbnsIPUndo"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSInterfacePoolParaUndoFlag"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSInterfacePoolIPInUseReset"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSInterfacePoolOptionCode"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSInterfacePoolOptionType"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSInterfacePoolOptionAscii"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSInterfacePoolOptionHexString"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSInterfacePoolOptionIPString"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSInterfacePoolOptionRowStatus"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSInterfacePoolStaticBindIP"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSInterfacePoolStaticBindMac"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSInterfacePoolStaticBindRowStatus"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSIPInUseHAddr"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSIPInUseIP"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSIPInUseEndLease"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSIPInUseType"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSIPInUsePoolName"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSIPInUseInterface"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSIPInUseVlan"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSIPInUseAtmpvc"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSForbiddenIPStart"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSForbiddenIPEnd"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSForbiddenIPRowStatus"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSConflictIP"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSConflictIPType"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSConflictIPDetectTime"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSServiceStatus"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSDetectingServerStatus"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSPingNum"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSPingTimeout"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSWriteDataStatus"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSWriteDataDirection"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSWriteDataDelay"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSWriteDataRecover"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSIPInUseResetIP"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSConflictIPResetIP"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSIPResetFlag"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolNumber"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolAutoBindingNum"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolManualBindingNum"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSGlobalPoolExpiredBindingNum"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSInterfacePoolNumber"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSInterfacePoolAutoBindingNum"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSInterfacePoolManualBindingNum"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSInterfacePoolExpiredBindingNum"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSBadPktNum"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSBootRequestPktNum"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSDiscoverPktNum"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSRequestPktNum"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSDeclinePktNum"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSReleasePktNum"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSInformPktNum"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSBootReplyPktNum"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSOfferPktNum"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSAckPktNum"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSNakPktNum"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSStatisticsReset"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSIPInUseHAddrEx"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSIPInUseVlanIdEx"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSIPInUseIPEx"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSIPInUseEndLeaseEx"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSIPInUseTypeEx"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSIPInUsePoolNameEx"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSIPInUseIfIndexEx"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSIPInUseServerPortVlanIdEx"),
        ("HPN-ICF-DHCPS-MIB", "hpnicfDHCPSIPInUseAtmpvcEx"))
)
if mibBuilder.loadTexts:
    hpnicfDHCPServerMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-DHCPS-MIB",
    **{"HpnicfDhcpSEnabledStatus": HpnicfDhcpSEnabledStatus,
       "hpnicfDHCPServerMib": hpnicfDHCPServerMib,
       "hpnicfDHCPServerMibObject": hpnicfDHCPServerMibObject,
       "hpnicfDHCPSGlobalPoolTable": hpnicfDHCPSGlobalPoolTable,
       "hpnicfDHCPSGlobalPoolEntry": hpnicfDHCPSGlobalPoolEntry,
       "hpnicfDHCPSGlobalPoolName": hpnicfDHCPSGlobalPoolName,
       "hpnicfDHCPSGlobalPoolRowStatus": hpnicfDHCPSGlobalPoolRowStatus,
       "hpnicfDHCPSGlobalPoolConfigTable": hpnicfDHCPSGlobalPoolConfigTable,
       "hpnicfDHCPSGlobalPoolConfigEntry": hpnicfDHCPSGlobalPoolConfigEntry,
       "hpnicfDHCPSGlobalPoolType": hpnicfDHCPSGlobalPoolType,
       "hpnicfDHCPSGlobalPoolNetwork": hpnicfDHCPSGlobalPoolNetwork,
       "hpnicfDHCPSGlobalPoolNetworkMask": hpnicfDHCPSGlobalPoolNetworkMask,
       "hpnicfDHCPSGlobalPoolHostIPAddr": hpnicfDHCPSGlobalPoolHostIPAddr,
       "hpnicfDHCPSGlobalPoolHostMask": hpnicfDHCPSGlobalPoolHostMask,
       "hpnicfDHCPSGlobalPoolHostHAddr": hpnicfDHCPSGlobalPoolHostHAddr,
       "hpnicfDHCPSGlobalPoolConfigUndoFlag": hpnicfDHCPSGlobalPoolConfigUndoFlag,
       "hpnicfDHCPSGlobalPoolParaTable": hpnicfDHCPSGlobalPoolParaTable,
       "hpnicfDHCPSGlobalPoolParaEntry": hpnicfDHCPSGlobalPoolParaEntry,
       "hpnicfDHCPSGlobalPoolLeaseDay": hpnicfDHCPSGlobalPoolLeaseDay,
       "hpnicfDHCPSGlobalPoolLeaseHour": hpnicfDHCPSGlobalPoolLeaseHour,
       "hpnicfDHCPSGlobalPoolLeaseMinute": hpnicfDHCPSGlobalPoolLeaseMinute,
       "hpnicfDHCPSGlobalPoolLeaseUnlimited": hpnicfDHCPSGlobalPoolLeaseUnlimited,
       "hpnicfDHCPSGlobalPoolDomainName": hpnicfDHCPSGlobalPoolDomainName,
       "hpnicfDHCPSGlobalPoolClientGatewayIPString": hpnicfDHCPSGlobalPoolClientGatewayIPString,
       "hpnicfDHCPSGlobalPoolClientGatewayIPUndo": hpnicfDHCPSGlobalPoolClientGatewayIPUndo,
       "hpnicfDHCPSGlobalPoolClientDNSIPString": hpnicfDHCPSGlobalPoolClientDNSIPString,
       "hpnicfDHCPSGlobalPoolClientDNSIPUndo": hpnicfDHCPSGlobalPoolClientDNSIPUndo,
       "hpnicfDHCPSGlobalPoolClientNetbiosType": hpnicfDHCPSGlobalPoolClientNetbiosType,
       "hpnicfDHCPSGlobalPoolClientNbnsIPString": hpnicfDHCPSGlobalPoolClientNbnsIPString,
       "hpnicfDHCPSGlobalPoolClientNbnsIPUndo": hpnicfDHCPSGlobalPoolClientNbnsIPUndo,
       "hpnicfDHCPSGlobalPoolParaUndoFlag": hpnicfDHCPSGlobalPoolParaUndoFlag,
       "hpnicfDHCPSGlobalPoolIPInUseReset": hpnicfDHCPSGlobalPoolIPInUseReset,
       "hpnicfDHCPSGlobalPoolOptionTable": hpnicfDHCPSGlobalPoolOptionTable,
       "hpnicfDHCPSGlobalPoolOptionEntry": hpnicfDHCPSGlobalPoolOptionEntry,
       "hpnicfDHCPSGlobalPoolOptionCode": hpnicfDHCPSGlobalPoolOptionCode,
       "hpnicfDHCPSGlobalPoolOptionType": hpnicfDHCPSGlobalPoolOptionType,
       "hpnicfDHCPSGlobalPoolOptionAscii": hpnicfDHCPSGlobalPoolOptionAscii,
       "hpnicfDHCPSGlobalPoolOptionHexString": hpnicfDHCPSGlobalPoolOptionHexString,
       "hpnicfDHCPSGlobalPoolOptionIPString": hpnicfDHCPSGlobalPoolOptionIPString,
       "hpnicfDHCPSGlobalPoolOptionRowStatus": hpnicfDHCPSGlobalPoolOptionRowStatus,
       "hpnicfDHCPSGlobalTreeTable": hpnicfDHCPSGlobalTreeTable,
       "hpnicfDHCPSGlobalTreeEntry": hpnicfDHCPSGlobalTreeEntry,
       "hpnicfDHCPSGlobalTreeParentNodeName": hpnicfDHCPSGlobalTreeParentNodeName,
       "hpnicfDHCPSGlobalTreeChildNodeName": hpnicfDHCPSGlobalTreeChildNodeName,
       "hpnicfDHCPSGlobalTreePreSiblingNodeName": hpnicfDHCPSGlobalTreePreSiblingNodeName,
       "hpnicfDHCPSGlobalTreeSiblingNodeName": hpnicfDHCPSGlobalTreeSiblingNodeName,
       "hpnicfDHCPSInterfacePoolParaTable": hpnicfDHCPSInterfacePoolParaTable,
       "hpnicfDHCPSInterfacePoolParaEntry": hpnicfDHCPSInterfacePoolParaEntry,
       "hpnicfDHCPSInterfacePoolLeaseDay": hpnicfDHCPSInterfacePoolLeaseDay,
       "hpnicfDHCPSInterfacePoolLeaseHour": hpnicfDHCPSInterfacePoolLeaseHour,
       "hpnicfDHCPSInterfacePoolLeaseMinute": hpnicfDHCPSInterfacePoolLeaseMinute,
       "hpnicfDHCPSInterfacePoolLeaseUnlimited": hpnicfDHCPSInterfacePoolLeaseUnlimited,
       "hpnicfDHCPSInterfacePoolDomainName": hpnicfDHCPSInterfacePoolDomainName,
       "hpnicfDHCPSInterfacePoolClientDNSIPString": hpnicfDHCPSInterfacePoolClientDNSIPString,
       "hpnicfDHCPSInterfacePoolClientDNSIPUndo": hpnicfDHCPSInterfacePoolClientDNSIPUndo,
       "hpnicfDHCPSInterfacePoolClientNetbiosType": hpnicfDHCPSInterfacePoolClientNetbiosType,
       "hpnicfDHCPSInterfacePoolClientNbnsIPString": hpnicfDHCPSInterfacePoolClientNbnsIPString,
       "hpnicfDHCPSInterfacePoolClientNbnsIPUndo": hpnicfDHCPSInterfacePoolClientNbnsIPUndo,
       "hpnicfDHCPSInterfacePoolParaUndoFlag": hpnicfDHCPSInterfacePoolParaUndoFlag,
       "hpnicfDHCPSInterfacePoolIPInUseReset": hpnicfDHCPSInterfacePoolIPInUseReset,
       "hpnicfDHCPSInterfacePoolOptionTable": hpnicfDHCPSInterfacePoolOptionTable,
       "hpnicfDHCPSInterfacePoolOptionEntry": hpnicfDHCPSInterfacePoolOptionEntry,
       "hpnicfDHCPSInterfacePoolOptionCode": hpnicfDHCPSInterfacePoolOptionCode,
       "hpnicfDHCPSInterfacePoolOptionType": hpnicfDHCPSInterfacePoolOptionType,
       "hpnicfDHCPSInterfacePoolOptionAscii": hpnicfDHCPSInterfacePoolOptionAscii,
       "hpnicfDHCPSInterfacePoolOptionHexString": hpnicfDHCPSInterfacePoolOptionHexString,
       "hpnicfDHCPSInterfacePoolOptionIPString": hpnicfDHCPSInterfacePoolOptionIPString,
       "hpnicfDHCPSInterfacePoolOptionRowStatus": hpnicfDHCPSInterfacePoolOptionRowStatus,
       "hpnicfDHCPSInterfacePoolStaticBindTable": hpnicfDHCPSInterfacePoolStaticBindTable,
       "hpnicfDHCPSInterfacePoolStaticBindEntry": hpnicfDHCPSInterfacePoolStaticBindEntry,
       "hpnicfDHCPSInterfacePoolStaticBindIP": hpnicfDHCPSInterfacePoolStaticBindIP,
       "hpnicfDHCPSInterfacePoolStaticBindMac": hpnicfDHCPSInterfacePoolStaticBindMac,
       "hpnicfDHCPSInterfacePoolStaticBindRowStatus": hpnicfDHCPSInterfacePoolStaticBindRowStatus,
       "hpnicfDHCPSIPInUseTable": hpnicfDHCPSIPInUseTable,
       "hpnicfDHCPSIPInUseEntry": hpnicfDHCPSIPInUseEntry,
       "hpnicfDHCPSIPInUseHAddr": hpnicfDHCPSIPInUseHAddr,
       "hpnicfDHCPSIPInUseIP": hpnicfDHCPSIPInUseIP,
       "hpnicfDHCPSIPInUseEndLease": hpnicfDHCPSIPInUseEndLease,
       "hpnicfDHCPSIPInUseType": hpnicfDHCPSIPInUseType,
       "hpnicfDHCPSIPInUsePoolName": hpnicfDHCPSIPInUsePoolName,
       "hpnicfDHCPSIPInUseInterface": hpnicfDHCPSIPInUseInterface,
       "hpnicfDHCPSIPInUseVlan": hpnicfDHCPSIPInUseVlan,
       "hpnicfDHCPSIPInUseAtmpvc": hpnicfDHCPSIPInUseAtmpvc,
       "hpnicfDHCPSForbiddenIPTable": hpnicfDHCPSForbiddenIPTable,
       "hpnicfDHCPSForbiddenIPEntry": hpnicfDHCPSForbiddenIPEntry,
       "hpnicfDHCPSForbiddenIPStart": hpnicfDHCPSForbiddenIPStart,
       "hpnicfDHCPSForbiddenIPEnd": hpnicfDHCPSForbiddenIPEnd,
       "hpnicfDHCPSForbiddenIPRowStatus": hpnicfDHCPSForbiddenIPRowStatus,
       "hpnicfDHCPSConflictIPTable": hpnicfDHCPSConflictIPTable,
       "hpnicfDHCPSConflictIPEntry": hpnicfDHCPSConflictIPEntry,
       "hpnicfDHCPSConflictIP": hpnicfDHCPSConflictIP,
       "hpnicfDHCPSConflictIPType": hpnicfDHCPSConflictIPType,
       "hpnicfDHCPSConflictIPDetectTime": hpnicfDHCPSConflictIPDetectTime,
       "hpnicfDHCPSServiceStatus": hpnicfDHCPSServiceStatus,
       "hpnicfDHCPSDetectingServerStatus": hpnicfDHCPSDetectingServerStatus,
       "hpnicfDHCPSPingNum": hpnicfDHCPSPingNum,
       "hpnicfDHCPSPingTimeout": hpnicfDHCPSPingTimeout,
       "hpnicfDHCPSWriteDataStatus": hpnicfDHCPSWriteDataStatus,
       "hpnicfDHCPSWriteDataDirection": hpnicfDHCPSWriteDataDirection,
       "hpnicfDHCPSWriteDataDelay": hpnicfDHCPSWriteDataDelay,
       "hpnicfDHCPSWriteDataRecover": hpnicfDHCPSWriteDataRecover,
       "hpnicfDHCPSIPInUseResetIP": hpnicfDHCPSIPInUseResetIP,
       "hpnicfDHCPSConflictIPResetIP": hpnicfDHCPSConflictIPResetIP,
       "hpnicfDHCPSIPResetFlag": hpnicfDHCPSIPResetFlag,
       "hpnicfDHCPSGlobalPoolNumber": hpnicfDHCPSGlobalPoolNumber,
       "hpnicfDHCPSGlobalPoolAutoBindingNum": hpnicfDHCPSGlobalPoolAutoBindingNum,
       "hpnicfDHCPSGlobalPoolManualBindingNum": hpnicfDHCPSGlobalPoolManualBindingNum,
       "hpnicfDHCPSGlobalPoolExpiredBindingNum": hpnicfDHCPSGlobalPoolExpiredBindingNum,
       "hpnicfDHCPSInterfacePoolNumber": hpnicfDHCPSInterfacePoolNumber,
       "hpnicfDHCPSInterfacePoolAutoBindingNum": hpnicfDHCPSInterfacePoolAutoBindingNum,
       "hpnicfDHCPSInterfacePoolManualBindingNum": hpnicfDHCPSInterfacePoolManualBindingNum,
       "hpnicfDHCPSInterfacePoolExpiredBindingNum": hpnicfDHCPSInterfacePoolExpiredBindingNum,
       "hpnicfDHCPSBadPktNum": hpnicfDHCPSBadPktNum,
       "hpnicfDHCPSBootRequestPktNum": hpnicfDHCPSBootRequestPktNum,
       "hpnicfDHCPSDiscoverPktNum": hpnicfDHCPSDiscoverPktNum,
       "hpnicfDHCPSRequestPktNum": hpnicfDHCPSRequestPktNum,
       "hpnicfDHCPSDeclinePktNum": hpnicfDHCPSDeclinePktNum,
       "hpnicfDHCPSReleasePktNum": hpnicfDHCPSReleasePktNum,
       "hpnicfDHCPSInformPktNum": hpnicfDHCPSInformPktNum,
       "hpnicfDHCPSBootReplyPktNum": hpnicfDHCPSBootReplyPktNum,
       "hpnicfDHCPSOfferPktNum": hpnicfDHCPSOfferPktNum,
       "hpnicfDHCPSAckPktNum": hpnicfDHCPSAckPktNum,
       "hpnicfDHCPSNakPktNum": hpnicfDHCPSNakPktNum,
       "hpnicfDHCPSStatisticsReset": hpnicfDHCPSStatisticsReset,
       "hpnicfDHCPSIPInUseExTable": hpnicfDHCPSIPInUseExTable,
       "hpnicfDHCPSIPInUseExEntry": hpnicfDHCPSIPInUseExEntry,
       "hpnicfDHCPSIPInUseHAddrEx": hpnicfDHCPSIPInUseHAddrEx,
       "hpnicfDHCPSIPInUseVlanIdEx": hpnicfDHCPSIPInUseVlanIdEx,
       "hpnicfDHCPSIPInUseIPEx": hpnicfDHCPSIPInUseIPEx,
       "hpnicfDHCPSIPInUseEndLeaseEx": hpnicfDHCPSIPInUseEndLeaseEx,
       "hpnicfDHCPSIPInUseTypeEx": hpnicfDHCPSIPInUseTypeEx,
       "hpnicfDHCPSIPInUsePoolNameEx": hpnicfDHCPSIPInUsePoolNameEx,
       "hpnicfDHCPSIPInUseIfIndexEx": hpnicfDHCPSIPInUseIfIndexEx,
       "hpnicfDHCPSIPInUseServerPortVlanIdEx": hpnicfDHCPSIPInUseServerPortVlanIdEx,
       "hpnicfDHCPSIPInUseAtmpvcEx": hpnicfDHCPSIPInUseAtmpvcEx,
       "hpnicfDHCPServerMIBConformance": hpnicfDHCPServerMIBConformance,
       "hpnicfDHCPServerMIBCompliances": hpnicfDHCPServerMIBCompliances,
       "hpnicfDHCPServerMIBGroups": hpnicfDHCPServerMIBGroups,
       "hpnicfDHCPServerMIBGroup": hpnicfDHCPServerMIBGroup}
)
