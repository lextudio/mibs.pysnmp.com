# SNMP MIB module (HH3C-DHCPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-DHCPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:43 2024
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

(hh3cRhw,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cRhw")

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

hh3cDHCPServerMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cDhcpSEnabledStatus(Integer32, TextualConvention):
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

_Hh3cDHCPServerMibObject_ObjectIdentity = ObjectIdentity
hh3cDHCPServerMibObject = _Hh3cDHCPServerMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1)
)
_Hh3cDHCPSGlobalPoolTable_Object = MibTable
hh3cDHCPSGlobalPoolTable = _Hh3cDHCPSGlobalPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolTable.setStatus("current")
_Hh3cDHCPSGlobalPoolEntry_Object = MibTableRow
hh3cDHCPSGlobalPoolEntry = _Hh3cDHCPSGlobalPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 1, 1)
)
hh3cDHCPSGlobalPoolEntry.setIndexNames(
    (0, "HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolName"),
)
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolEntry.setStatus("current")


class _Hh3cDHCPSGlobalPoolName_Type(OctetString):
    """Custom type hh3cDHCPSGlobalPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDHCPSGlobalPoolName_Type.__name__ = "OctetString"
_Hh3cDHCPSGlobalPoolName_Object = MibTableColumn
hh3cDHCPSGlobalPoolName = _Hh3cDHCPSGlobalPoolName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 1, 1, 1),
    _Hh3cDHCPSGlobalPoolName_Type()
)
hh3cDHCPSGlobalPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolName.setStatus("current")
_Hh3cDHCPSGlobalPoolRowStatus_Type = RowStatus
_Hh3cDHCPSGlobalPoolRowStatus_Object = MibTableColumn
hh3cDHCPSGlobalPoolRowStatus = _Hh3cDHCPSGlobalPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 1, 1, 2),
    _Hh3cDHCPSGlobalPoolRowStatus_Type()
)
hh3cDHCPSGlobalPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolRowStatus.setStatus("current")
_Hh3cDHCPSGlobalPoolConfigTable_Object = MibTable
hh3cDHCPSGlobalPoolConfigTable = _Hh3cDHCPSGlobalPoolConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolConfigTable.setStatus("current")
_Hh3cDHCPSGlobalPoolConfigEntry_Object = MibTableRow
hh3cDHCPSGlobalPoolConfigEntry = _Hh3cDHCPSGlobalPoolConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 2, 1)
)
hh3cDHCPSGlobalPoolConfigEntry.setIndexNames(
    (0, "HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolName"),
)
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolConfigEntry.setStatus("current")


class _Hh3cDHCPSGlobalPoolType_Type(Integer32):
    """Custom type hh3cDHCPSGlobalPoolType based on Integer32"""
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


_Hh3cDHCPSGlobalPoolType_Type.__name__ = "Integer32"
_Hh3cDHCPSGlobalPoolType_Object = MibTableColumn
hh3cDHCPSGlobalPoolType = _Hh3cDHCPSGlobalPoolType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 2, 1, 1),
    _Hh3cDHCPSGlobalPoolType_Type()
)
hh3cDHCPSGlobalPoolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolType.setStatus("current")
_Hh3cDHCPSGlobalPoolNetwork_Type = IpAddress
_Hh3cDHCPSGlobalPoolNetwork_Object = MibTableColumn
hh3cDHCPSGlobalPoolNetwork = _Hh3cDHCPSGlobalPoolNetwork_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 2, 1, 2),
    _Hh3cDHCPSGlobalPoolNetwork_Type()
)
hh3cDHCPSGlobalPoolNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolNetwork.setStatus("current")
_Hh3cDHCPSGlobalPoolNetworkMask_Type = IpAddress
_Hh3cDHCPSGlobalPoolNetworkMask_Object = MibTableColumn
hh3cDHCPSGlobalPoolNetworkMask = _Hh3cDHCPSGlobalPoolNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 2, 1, 3),
    _Hh3cDHCPSGlobalPoolNetworkMask_Type()
)
hh3cDHCPSGlobalPoolNetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolNetworkMask.setStatus("current")
_Hh3cDHCPSGlobalPoolHostIPAddr_Type = IpAddress
_Hh3cDHCPSGlobalPoolHostIPAddr_Object = MibTableColumn
hh3cDHCPSGlobalPoolHostIPAddr = _Hh3cDHCPSGlobalPoolHostIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 2, 1, 4),
    _Hh3cDHCPSGlobalPoolHostIPAddr_Type()
)
hh3cDHCPSGlobalPoolHostIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolHostIPAddr.setStatus("current")
_Hh3cDHCPSGlobalPoolHostMask_Type = IpAddress
_Hh3cDHCPSGlobalPoolHostMask_Object = MibTableColumn
hh3cDHCPSGlobalPoolHostMask = _Hh3cDHCPSGlobalPoolHostMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 2, 1, 5),
    _Hh3cDHCPSGlobalPoolHostMask_Type()
)
hh3cDHCPSGlobalPoolHostMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolHostMask.setStatus("current")
_Hh3cDHCPSGlobalPoolHostHAddr_Type = MacAddress
_Hh3cDHCPSGlobalPoolHostHAddr_Object = MibTableColumn
hh3cDHCPSGlobalPoolHostHAddr = _Hh3cDHCPSGlobalPoolHostHAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 2, 1, 6),
    _Hh3cDHCPSGlobalPoolHostHAddr_Type()
)
hh3cDHCPSGlobalPoolHostHAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolHostHAddr.setStatus("current")


class _Hh3cDHCPSGlobalPoolConfigUndoFlag_Type(Integer32):
    """Custom type hh3cDHCPSGlobalPoolConfigUndoFlag based on Integer32"""
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


_Hh3cDHCPSGlobalPoolConfigUndoFlag_Type.__name__ = "Integer32"
_Hh3cDHCPSGlobalPoolConfigUndoFlag_Object = MibTableColumn
hh3cDHCPSGlobalPoolConfigUndoFlag = _Hh3cDHCPSGlobalPoolConfigUndoFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 2, 1, 7),
    _Hh3cDHCPSGlobalPoolConfigUndoFlag_Type()
)
hh3cDHCPSGlobalPoolConfigUndoFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolConfigUndoFlag.setStatus("current")
_Hh3cDHCPSGlobalPoolParaTable_Object = MibTable
hh3cDHCPSGlobalPoolParaTable = _Hh3cDHCPSGlobalPoolParaTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolParaTable.setStatus("current")
_Hh3cDHCPSGlobalPoolParaEntry_Object = MibTableRow
hh3cDHCPSGlobalPoolParaEntry = _Hh3cDHCPSGlobalPoolParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 3, 1)
)
hh3cDHCPSGlobalPoolParaEntry.setIndexNames(
    (0, "HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolName"),
)
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolParaEntry.setStatus("current")


class _Hh3cDHCPSGlobalPoolLeaseDay_Type(Integer32):
    """Custom type hh3cDHCPSGlobalPoolLeaseDay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_Hh3cDHCPSGlobalPoolLeaseDay_Type.__name__ = "Integer32"
_Hh3cDHCPSGlobalPoolLeaseDay_Object = MibTableColumn
hh3cDHCPSGlobalPoolLeaseDay = _Hh3cDHCPSGlobalPoolLeaseDay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 3, 1, 1),
    _Hh3cDHCPSGlobalPoolLeaseDay_Type()
)
hh3cDHCPSGlobalPoolLeaseDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolLeaseDay.setStatus("current")


class _Hh3cDHCPSGlobalPoolLeaseHour_Type(Integer32):
    """Custom type hh3cDHCPSGlobalPoolLeaseHour based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Hh3cDHCPSGlobalPoolLeaseHour_Type.__name__ = "Integer32"
_Hh3cDHCPSGlobalPoolLeaseHour_Object = MibTableColumn
hh3cDHCPSGlobalPoolLeaseHour = _Hh3cDHCPSGlobalPoolLeaseHour_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 3, 1, 2),
    _Hh3cDHCPSGlobalPoolLeaseHour_Type()
)
hh3cDHCPSGlobalPoolLeaseHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolLeaseHour.setStatus("current")


class _Hh3cDHCPSGlobalPoolLeaseMinute_Type(Integer32):
    """Custom type hh3cDHCPSGlobalPoolLeaseMinute based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Hh3cDHCPSGlobalPoolLeaseMinute_Type.__name__ = "Integer32"
_Hh3cDHCPSGlobalPoolLeaseMinute_Object = MibTableColumn
hh3cDHCPSGlobalPoolLeaseMinute = _Hh3cDHCPSGlobalPoolLeaseMinute_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 3, 1, 3),
    _Hh3cDHCPSGlobalPoolLeaseMinute_Type()
)
hh3cDHCPSGlobalPoolLeaseMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolLeaseMinute.setStatus("current")


class _Hh3cDHCPSGlobalPoolLeaseUnlimited_Type(Integer32):
    """Custom type hh3cDHCPSGlobalPoolLeaseUnlimited based on Integer32"""
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


_Hh3cDHCPSGlobalPoolLeaseUnlimited_Type.__name__ = "Integer32"
_Hh3cDHCPSGlobalPoolLeaseUnlimited_Object = MibTableColumn
hh3cDHCPSGlobalPoolLeaseUnlimited = _Hh3cDHCPSGlobalPoolLeaseUnlimited_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 3, 1, 4),
    _Hh3cDHCPSGlobalPoolLeaseUnlimited_Type()
)
hh3cDHCPSGlobalPoolLeaseUnlimited.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolLeaseUnlimited.setStatus("current")


class _Hh3cDHCPSGlobalPoolDomainName_Type(OctetString):
    """Custom type hh3cDHCPSGlobalPoolDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDHCPSGlobalPoolDomainName_Type.__name__ = "OctetString"
_Hh3cDHCPSGlobalPoolDomainName_Object = MibTableColumn
hh3cDHCPSGlobalPoolDomainName = _Hh3cDHCPSGlobalPoolDomainName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 3, 1, 5),
    _Hh3cDHCPSGlobalPoolDomainName_Type()
)
hh3cDHCPSGlobalPoolDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolDomainName.setStatus("current")


class _Hh3cDHCPSGlobalPoolClientGatewayIPString_Type(OctetString):
    """Custom type hh3cDHCPSGlobalPoolClientGatewayIPString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_Hh3cDHCPSGlobalPoolClientGatewayIPString_Type.__name__ = "OctetString"
_Hh3cDHCPSGlobalPoolClientGatewayIPString_Object = MibTableColumn
hh3cDHCPSGlobalPoolClientGatewayIPString = _Hh3cDHCPSGlobalPoolClientGatewayIPString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 3, 1, 6),
    _Hh3cDHCPSGlobalPoolClientGatewayIPString_Type()
)
hh3cDHCPSGlobalPoolClientGatewayIPString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolClientGatewayIPString.setStatus("current")
_Hh3cDHCPSGlobalPoolClientGatewayIPUndo_Type = IpAddress
_Hh3cDHCPSGlobalPoolClientGatewayIPUndo_Object = MibTableColumn
hh3cDHCPSGlobalPoolClientGatewayIPUndo = _Hh3cDHCPSGlobalPoolClientGatewayIPUndo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 3, 1, 7),
    _Hh3cDHCPSGlobalPoolClientGatewayIPUndo_Type()
)
hh3cDHCPSGlobalPoolClientGatewayIPUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolClientGatewayIPUndo.setStatus("current")


class _Hh3cDHCPSGlobalPoolClientDNSIPString_Type(OctetString):
    """Custom type hh3cDHCPSGlobalPoolClientDNSIPString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_Hh3cDHCPSGlobalPoolClientDNSIPString_Type.__name__ = "OctetString"
_Hh3cDHCPSGlobalPoolClientDNSIPString_Object = MibTableColumn
hh3cDHCPSGlobalPoolClientDNSIPString = _Hh3cDHCPSGlobalPoolClientDNSIPString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 3, 1, 8),
    _Hh3cDHCPSGlobalPoolClientDNSIPString_Type()
)
hh3cDHCPSGlobalPoolClientDNSIPString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolClientDNSIPString.setStatus("current")
_Hh3cDHCPSGlobalPoolClientDNSIPUndo_Type = IpAddress
_Hh3cDHCPSGlobalPoolClientDNSIPUndo_Object = MibTableColumn
hh3cDHCPSGlobalPoolClientDNSIPUndo = _Hh3cDHCPSGlobalPoolClientDNSIPUndo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 3, 1, 9),
    _Hh3cDHCPSGlobalPoolClientDNSIPUndo_Type()
)
hh3cDHCPSGlobalPoolClientDNSIPUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolClientDNSIPUndo.setStatus("current")


class _Hh3cDHCPSGlobalPoolClientNetbiosType_Type(Integer32):
    """Custom type hh3cDHCPSGlobalPoolClientNetbiosType based on Integer32"""
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


_Hh3cDHCPSGlobalPoolClientNetbiosType_Type.__name__ = "Integer32"
_Hh3cDHCPSGlobalPoolClientNetbiosType_Object = MibTableColumn
hh3cDHCPSGlobalPoolClientNetbiosType = _Hh3cDHCPSGlobalPoolClientNetbiosType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 3, 1, 10),
    _Hh3cDHCPSGlobalPoolClientNetbiosType_Type()
)
hh3cDHCPSGlobalPoolClientNetbiosType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolClientNetbiosType.setStatus("current")


class _Hh3cDHCPSGlobalPoolClientNbnsIPString_Type(OctetString):
    """Custom type hh3cDHCPSGlobalPoolClientNbnsIPString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_Hh3cDHCPSGlobalPoolClientNbnsIPString_Type.__name__ = "OctetString"
_Hh3cDHCPSGlobalPoolClientNbnsIPString_Object = MibTableColumn
hh3cDHCPSGlobalPoolClientNbnsIPString = _Hh3cDHCPSGlobalPoolClientNbnsIPString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 3, 1, 11),
    _Hh3cDHCPSGlobalPoolClientNbnsIPString_Type()
)
hh3cDHCPSGlobalPoolClientNbnsIPString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolClientNbnsIPString.setStatus("current")
_Hh3cDHCPSGlobalPoolClientNbnsIPUndo_Type = IpAddress
_Hh3cDHCPSGlobalPoolClientNbnsIPUndo_Object = MibTableColumn
hh3cDHCPSGlobalPoolClientNbnsIPUndo = _Hh3cDHCPSGlobalPoolClientNbnsIPUndo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 3, 1, 12),
    _Hh3cDHCPSGlobalPoolClientNbnsIPUndo_Type()
)
hh3cDHCPSGlobalPoolClientNbnsIPUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolClientNbnsIPUndo.setStatus("current")


class _Hh3cDHCPSGlobalPoolParaUndoFlag_Type(Integer32):
    """Custom type hh3cDHCPSGlobalPoolParaUndoFlag based on Integer32"""
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


_Hh3cDHCPSGlobalPoolParaUndoFlag_Type.__name__ = "Integer32"
_Hh3cDHCPSGlobalPoolParaUndoFlag_Object = MibTableColumn
hh3cDHCPSGlobalPoolParaUndoFlag = _Hh3cDHCPSGlobalPoolParaUndoFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 3, 1, 13),
    _Hh3cDHCPSGlobalPoolParaUndoFlag_Type()
)
hh3cDHCPSGlobalPoolParaUndoFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolParaUndoFlag.setStatus("current")


class _Hh3cDHCPSGlobalPoolIPInUseReset_Type(Integer32):
    """Custom type hh3cDHCPSGlobalPoolIPInUseReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Hh3cDHCPSGlobalPoolIPInUseReset_Type.__name__ = "Integer32"
_Hh3cDHCPSGlobalPoolIPInUseReset_Object = MibTableColumn
hh3cDHCPSGlobalPoolIPInUseReset = _Hh3cDHCPSGlobalPoolIPInUseReset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 3, 1, 14),
    _Hh3cDHCPSGlobalPoolIPInUseReset_Type()
)
hh3cDHCPSGlobalPoolIPInUseReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolIPInUseReset.setStatus("current")
_Hh3cDHCPSGlobalPoolOptionTable_Object = MibTable
hh3cDHCPSGlobalPoolOptionTable = _Hh3cDHCPSGlobalPoolOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolOptionTable.setStatus("current")
_Hh3cDHCPSGlobalPoolOptionEntry_Object = MibTableRow
hh3cDHCPSGlobalPoolOptionEntry = _Hh3cDHCPSGlobalPoolOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 4, 1)
)
hh3cDHCPSGlobalPoolOptionEntry.setIndexNames(
    (0, "HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolName"),
    (0, "HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolOptionCode"),
)
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolOptionEntry.setStatus("current")


class _Hh3cDHCPSGlobalPoolOptionCode_Type(Integer32):
    """Custom type hh3cDHCPSGlobalPoolOptionCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_Hh3cDHCPSGlobalPoolOptionCode_Type.__name__ = "Integer32"
_Hh3cDHCPSGlobalPoolOptionCode_Object = MibTableColumn
hh3cDHCPSGlobalPoolOptionCode = _Hh3cDHCPSGlobalPoolOptionCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 4, 1, 1),
    _Hh3cDHCPSGlobalPoolOptionCode_Type()
)
hh3cDHCPSGlobalPoolOptionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolOptionCode.setStatus("current")


class _Hh3cDHCPSGlobalPoolOptionType_Type(Integer32):
    """Custom type hh3cDHCPSGlobalPoolOptionType based on Integer32"""
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


_Hh3cDHCPSGlobalPoolOptionType_Type.__name__ = "Integer32"
_Hh3cDHCPSGlobalPoolOptionType_Object = MibTableColumn
hh3cDHCPSGlobalPoolOptionType = _Hh3cDHCPSGlobalPoolOptionType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 4, 1, 2),
    _Hh3cDHCPSGlobalPoolOptionType_Type()
)
hh3cDHCPSGlobalPoolOptionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolOptionType.setStatus("current")


class _Hh3cDHCPSGlobalPoolOptionAscii_Type(OctetString):
    """Custom type hh3cDHCPSGlobalPoolOptionAscii based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cDHCPSGlobalPoolOptionAscii_Type.__name__ = "OctetString"
_Hh3cDHCPSGlobalPoolOptionAscii_Object = MibTableColumn
hh3cDHCPSGlobalPoolOptionAscii = _Hh3cDHCPSGlobalPoolOptionAscii_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 4, 1, 3),
    _Hh3cDHCPSGlobalPoolOptionAscii_Type()
)
hh3cDHCPSGlobalPoolOptionAscii.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolOptionAscii.setStatus("current")


class _Hh3cDHCPSGlobalPoolOptionHexString_Type(OctetString):
    """Custom type hh3cDHCPSGlobalPoolOptionHexString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 143),
    )


_Hh3cDHCPSGlobalPoolOptionHexString_Type.__name__ = "OctetString"
_Hh3cDHCPSGlobalPoolOptionHexString_Object = MibTableColumn
hh3cDHCPSGlobalPoolOptionHexString = _Hh3cDHCPSGlobalPoolOptionHexString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 4, 1, 4),
    _Hh3cDHCPSGlobalPoolOptionHexString_Type()
)
hh3cDHCPSGlobalPoolOptionHexString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolOptionHexString.setStatus("current")


class _Hh3cDHCPSGlobalPoolOptionIPString_Type(OctetString):
    """Custom type hh3cDHCPSGlobalPoolOptionIPString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_Hh3cDHCPSGlobalPoolOptionIPString_Type.__name__ = "OctetString"
_Hh3cDHCPSGlobalPoolOptionIPString_Object = MibTableColumn
hh3cDHCPSGlobalPoolOptionIPString = _Hh3cDHCPSGlobalPoolOptionIPString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 4, 1, 5),
    _Hh3cDHCPSGlobalPoolOptionIPString_Type()
)
hh3cDHCPSGlobalPoolOptionIPString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolOptionIPString.setStatus("current")
_Hh3cDHCPSGlobalPoolOptionRowStatus_Type = RowStatus
_Hh3cDHCPSGlobalPoolOptionRowStatus_Object = MibTableColumn
hh3cDHCPSGlobalPoolOptionRowStatus = _Hh3cDHCPSGlobalPoolOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 4, 1, 6),
    _Hh3cDHCPSGlobalPoolOptionRowStatus_Type()
)
hh3cDHCPSGlobalPoolOptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolOptionRowStatus.setStatus("current")
_Hh3cDHCPSGlobalTreeTable_Object = MibTable
hh3cDHCPSGlobalTreeTable = _Hh3cDHCPSGlobalTreeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalTreeTable.setStatus("current")
_Hh3cDHCPSGlobalTreeEntry_Object = MibTableRow
hh3cDHCPSGlobalTreeEntry = _Hh3cDHCPSGlobalTreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 5, 1)
)
hh3cDHCPSGlobalTreeEntry.setIndexNames(
    (0, "HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolName"),
)
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalTreeEntry.setStatus("current")


class _Hh3cDHCPSGlobalTreeParentNodeName_Type(OctetString):
    """Custom type hh3cDHCPSGlobalTreeParentNodeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDHCPSGlobalTreeParentNodeName_Type.__name__ = "OctetString"
_Hh3cDHCPSGlobalTreeParentNodeName_Object = MibTableColumn
hh3cDHCPSGlobalTreeParentNodeName = _Hh3cDHCPSGlobalTreeParentNodeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 5, 1, 1),
    _Hh3cDHCPSGlobalTreeParentNodeName_Type()
)
hh3cDHCPSGlobalTreeParentNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalTreeParentNodeName.setStatus("current")


class _Hh3cDHCPSGlobalTreeChildNodeName_Type(OctetString):
    """Custom type hh3cDHCPSGlobalTreeChildNodeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDHCPSGlobalTreeChildNodeName_Type.__name__ = "OctetString"
_Hh3cDHCPSGlobalTreeChildNodeName_Object = MibTableColumn
hh3cDHCPSGlobalTreeChildNodeName = _Hh3cDHCPSGlobalTreeChildNodeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 5, 1, 2),
    _Hh3cDHCPSGlobalTreeChildNodeName_Type()
)
hh3cDHCPSGlobalTreeChildNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalTreeChildNodeName.setStatus("current")


class _Hh3cDHCPSGlobalTreePreSiblingNodeName_Type(OctetString):
    """Custom type hh3cDHCPSGlobalTreePreSiblingNodeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDHCPSGlobalTreePreSiblingNodeName_Type.__name__ = "OctetString"
_Hh3cDHCPSGlobalTreePreSiblingNodeName_Object = MibTableColumn
hh3cDHCPSGlobalTreePreSiblingNodeName = _Hh3cDHCPSGlobalTreePreSiblingNodeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 5, 1, 3),
    _Hh3cDHCPSGlobalTreePreSiblingNodeName_Type()
)
hh3cDHCPSGlobalTreePreSiblingNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalTreePreSiblingNodeName.setStatus("current")


class _Hh3cDHCPSGlobalTreeSiblingNodeName_Type(OctetString):
    """Custom type hh3cDHCPSGlobalTreeSiblingNodeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDHCPSGlobalTreeSiblingNodeName_Type.__name__ = "OctetString"
_Hh3cDHCPSGlobalTreeSiblingNodeName_Object = MibTableColumn
hh3cDHCPSGlobalTreeSiblingNodeName = _Hh3cDHCPSGlobalTreeSiblingNodeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 5, 1, 4),
    _Hh3cDHCPSGlobalTreeSiblingNodeName_Type()
)
hh3cDHCPSGlobalTreeSiblingNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalTreeSiblingNodeName.setStatus("current")
_Hh3cDHCPSInterfacePoolParaTable_Object = MibTable
hh3cDHCPSInterfacePoolParaTable = _Hh3cDHCPSInterfacePoolParaTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolParaTable.setStatus("current")
_Hh3cDHCPSInterfacePoolParaEntry_Object = MibTableRow
hh3cDHCPSInterfacePoolParaEntry = _Hh3cDHCPSInterfacePoolParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 6, 1)
)
hh3cDHCPSInterfacePoolParaEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolParaEntry.setStatus("current")


class _Hh3cDHCPSInterfacePoolLeaseDay_Type(Integer32):
    """Custom type hh3cDHCPSInterfacePoolLeaseDay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_Hh3cDHCPSInterfacePoolLeaseDay_Type.__name__ = "Integer32"
_Hh3cDHCPSInterfacePoolLeaseDay_Object = MibTableColumn
hh3cDHCPSInterfacePoolLeaseDay = _Hh3cDHCPSInterfacePoolLeaseDay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 6, 1, 1),
    _Hh3cDHCPSInterfacePoolLeaseDay_Type()
)
hh3cDHCPSInterfacePoolLeaseDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolLeaseDay.setStatus("current")


class _Hh3cDHCPSInterfacePoolLeaseHour_Type(Integer32):
    """Custom type hh3cDHCPSInterfacePoolLeaseHour based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Hh3cDHCPSInterfacePoolLeaseHour_Type.__name__ = "Integer32"
_Hh3cDHCPSInterfacePoolLeaseHour_Object = MibTableColumn
hh3cDHCPSInterfacePoolLeaseHour = _Hh3cDHCPSInterfacePoolLeaseHour_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 6, 1, 2),
    _Hh3cDHCPSInterfacePoolLeaseHour_Type()
)
hh3cDHCPSInterfacePoolLeaseHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolLeaseHour.setStatus("current")


class _Hh3cDHCPSInterfacePoolLeaseMinute_Type(Integer32):
    """Custom type hh3cDHCPSInterfacePoolLeaseMinute based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_Hh3cDHCPSInterfacePoolLeaseMinute_Type.__name__ = "Integer32"
_Hh3cDHCPSInterfacePoolLeaseMinute_Object = MibTableColumn
hh3cDHCPSInterfacePoolLeaseMinute = _Hh3cDHCPSInterfacePoolLeaseMinute_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 6, 1, 3),
    _Hh3cDHCPSInterfacePoolLeaseMinute_Type()
)
hh3cDHCPSInterfacePoolLeaseMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolLeaseMinute.setStatus("current")


class _Hh3cDHCPSInterfacePoolLeaseUnlimited_Type(Integer32):
    """Custom type hh3cDHCPSInterfacePoolLeaseUnlimited based on Integer32"""
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


_Hh3cDHCPSInterfacePoolLeaseUnlimited_Type.__name__ = "Integer32"
_Hh3cDHCPSInterfacePoolLeaseUnlimited_Object = MibTableColumn
hh3cDHCPSInterfacePoolLeaseUnlimited = _Hh3cDHCPSInterfacePoolLeaseUnlimited_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 6, 1, 4),
    _Hh3cDHCPSInterfacePoolLeaseUnlimited_Type()
)
hh3cDHCPSInterfacePoolLeaseUnlimited.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolLeaseUnlimited.setStatus("current")


class _Hh3cDHCPSInterfacePoolDomainName_Type(OctetString):
    """Custom type hh3cDHCPSInterfacePoolDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDHCPSInterfacePoolDomainName_Type.__name__ = "OctetString"
_Hh3cDHCPSInterfacePoolDomainName_Object = MibTableColumn
hh3cDHCPSInterfacePoolDomainName = _Hh3cDHCPSInterfacePoolDomainName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 6, 1, 5),
    _Hh3cDHCPSInterfacePoolDomainName_Type()
)
hh3cDHCPSInterfacePoolDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolDomainName.setStatus("current")


class _Hh3cDHCPSInterfacePoolClientDNSIPString_Type(OctetString):
    """Custom type hh3cDHCPSInterfacePoolClientDNSIPString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_Hh3cDHCPSInterfacePoolClientDNSIPString_Type.__name__ = "OctetString"
_Hh3cDHCPSInterfacePoolClientDNSIPString_Object = MibTableColumn
hh3cDHCPSInterfacePoolClientDNSIPString = _Hh3cDHCPSInterfacePoolClientDNSIPString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 6, 1, 6),
    _Hh3cDHCPSInterfacePoolClientDNSIPString_Type()
)
hh3cDHCPSInterfacePoolClientDNSIPString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolClientDNSIPString.setStatus("current")
_Hh3cDHCPSInterfacePoolClientDNSIPUndo_Type = IpAddress
_Hh3cDHCPSInterfacePoolClientDNSIPUndo_Object = MibTableColumn
hh3cDHCPSInterfacePoolClientDNSIPUndo = _Hh3cDHCPSInterfacePoolClientDNSIPUndo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 6, 1, 7),
    _Hh3cDHCPSInterfacePoolClientDNSIPUndo_Type()
)
hh3cDHCPSInterfacePoolClientDNSIPUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolClientDNSIPUndo.setStatus("current")


class _Hh3cDHCPSInterfacePoolClientNetbiosType_Type(Integer32):
    """Custom type hh3cDHCPSInterfacePoolClientNetbiosType based on Integer32"""
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


_Hh3cDHCPSInterfacePoolClientNetbiosType_Type.__name__ = "Integer32"
_Hh3cDHCPSInterfacePoolClientNetbiosType_Object = MibTableColumn
hh3cDHCPSInterfacePoolClientNetbiosType = _Hh3cDHCPSInterfacePoolClientNetbiosType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 6, 1, 8),
    _Hh3cDHCPSInterfacePoolClientNetbiosType_Type()
)
hh3cDHCPSInterfacePoolClientNetbiosType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolClientNetbiosType.setStatus("current")


class _Hh3cDHCPSInterfacePoolClientNbnsIPString_Type(OctetString):
    """Custom type hh3cDHCPSInterfacePoolClientNbnsIPString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_Hh3cDHCPSInterfacePoolClientNbnsIPString_Type.__name__ = "OctetString"
_Hh3cDHCPSInterfacePoolClientNbnsIPString_Object = MibTableColumn
hh3cDHCPSInterfacePoolClientNbnsIPString = _Hh3cDHCPSInterfacePoolClientNbnsIPString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 6, 1, 9),
    _Hh3cDHCPSInterfacePoolClientNbnsIPString_Type()
)
hh3cDHCPSInterfacePoolClientNbnsIPString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolClientNbnsIPString.setStatus("current")
_Hh3cDHCPSInterfacePoolClientNbnsIPUndo_Type = IpAddress
_Hh3cDHCPSInterfacePoolClientNbnsIPUndo_Object = MibTableColumn
hh3cDHCPSInterfacePoolClientNbnsIPUndo = _Hh3cDHCPSInterfacePoolClientNbnsIPUndo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 6, 1, 10),
    _Hh3cDHCPSInterfacePoolClientNbnsIPUndo_Type()
)
hh3cDHCPSInterfacePoolClientNbnsIPUndo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolClientNbnsIPUndo.setStatus("current")


class _Hh3cDHCPSInterfacePoolParaUndoFlag_Type(Integer32):
    """Custom type hh3cDHCPSInterfacePoolParaUndoFlag based on Integer32"""
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


_Hh3cDHCPSInterfacePoolParaUndoFlag_Type.__name__ = "Integer32"
_Hh3cDHCPSInterfacePoolParaUndoFlag_Object = MibTableColumn
hh3cDHCPSInterfacePoolParaUndoFlag = _Hh3cDHCPSInterfacePoolParaUndoFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 6, 1, 11),
    _Hh3cDHCPSInterfacePoolParaUndoFlag_Type()
)
hh3cDHCPSInterfacePoolParaUndoFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolParaUndoFlag.setStatus("current")


class _Hh3cDHCPSInterfacePoolIPInUseReset_Type(Integer32):
    """Custom type hh3cDHCPSInterfacePoolIPInUseReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Hh3cDHCPSInterfacePoolIPInUseReset_Type.__name__ = "Integer32"
_Hh3cDHCPSInterfacePoolIPInUseReset_Object = MibTableColumn
hh3cDHCPSInterfacePoolIPInUseReset = _Hh3cDHCPSInterfacePoolIPInUseReset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 6, 1, 12),
    _Hh3cDHCPSInterfacePoolIPInUseReset_Type()
)
hh3cDHCPSInterfacePoolIPInUseReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolIPInUseReset.setStatus("current")
_Hh3cDHCPSInterfacePoolOptionTable_Object = MibTable
hh3cDHCPSInterfacePoolOptionTable = _Hh3cDHCPSInterfacePoolOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 7)
)
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolOptionTable.setStatus("current")
_Hh3cDHCPSInterfacePoolOptionEntry_Object = MibTableRow
hh3cDHCPSInterfacePoolOptionEntry = _Hh3cDHCPSInterfacePoolOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 7, 1)
)
hh3cDHCPSInterfacePoolOptionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-DHCPS-MIB", "hh3cDHCPSInterfacePoolOptionCode"),
)
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolOptionEntry.setStatus("current")


class _Hh3cDHCPSInterfacePoolOptionCode_Type(Integer32):
    """Custom type hh3cDHCPSInterfacePoolOptionCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_Hh3cDHCPSInterfacePoolOptionCode_Type.__name__ = "Integer32"
_Hh3cDHCPSInterfacePoolOptionCode_Object = MibTableColumn
hh3cDHCPSInterfacePoolOptionCode = _Hh3cDHCPSInterfacePoolOptionCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 7, 1, 1),
    _Hh3cDHCPSInterfacePoolOptionCode_Type()
)
hh3cDHCPSInterfacePoolOptionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolOptionCode.setStatus("current")


class _Hh3cDHCPSInterfacePoolOptionType_Type(Integer32):
    """Custom type hh3cDHCPSInterfacePoolOptionType based on Integer32"""
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


_Hh3cDHCPSInterfacePoolOptionType_Type.__name__ = "Integer32"
_Hh3cDHCPSInterfacePoolOptionType_Object = MibTableColumn
hh3cDHCPSInterfacePoolOptionType = _Hh3cDHCPSInterfacePoolOptionType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 7, 1, 2),
    _Hh3cDHCPSInterfacePoolOptionType_Type()
)
hh3cDHCPSInterfacePoolOptionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolOptionType.setStatus("current")


class _Hh3cDHCPSInterfacePoolOptionAscii_Type(OctetString):
    """Custom type hh3cDHCPSInterfacePoolOptionAscii based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cDHCPSInterfacePoolOptionAscii_Type.__name__ = "OctetString"
_Hh3cDHCPSInterfacePoolOptionAscii_Object = MibTableColumn
hh3cDHCPSInterfacePoolOptionAscii = _Hh3cDHCPSInterfacePoolOptionAscii_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 7, 1, 3),
    _Hh3cDHCPSInterfacePoolOptionAscii_Type()
)
hh3cDHCPSInterfacePoolOptionAscii.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolOptionAscii.setStatus("current")


class _Hh3cDHCPSInterfacePoolOptionHexString_Type(OctetString):
    """Custom type hh3cDHCPSInterfacePoolOptionHexString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 143),
    )


_Hh3cDHCPSInterfacePoolOptionHexString_Type.__name__ = "OctetString"
_Hh3cDHCPSInterfacePoolOptionHexString_Object = MibTableColumn
hh3cDHCPSInterfacePoolOptionHexString = _Hh3cDHCPSInterfacePoolOptionHexString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 7, 1, 4),
    _Hh3cDHCPSInterfacePoolOptionHexString_Type()
)
hh3cDHCPSInterfacePoolOptionHexString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolOptionHexString.setStatus("current")


class _Hh3cDHCPSInterfacePoolOptionIPString_Type(OctetString):
    """Custom type hh3cDHCPSInterfacePoolOptionIPString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 129),
    )


_Hh3cDHCPSInterfacePoolOptionIPString_Type.__name__ = "OctetString"
_Hh3cDHCPSInterfacePoolOptionIPString_Object = MibTableColumn
hh3cDHCPSInterfacePoolOptionIPString = _Hh3cDHCPSInterfacePoolOptionIPString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 7, 1, 5),
    _Hh3cDHCPSInterfacePoolOptionIPString_Type()
)
hh3cDHCPSInterfacePoolOptionIPString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolOptionIPString.setStatus("current")
_Hh3cDHCPSInterfacePoolOptionRowStatus_Type = RowStatus
_Hh3cDHCPSInterfacePoolOptionRowStatus_Object = MibTableColumn
hh3cDHCPSInterfacePoolOptionRowStatus = _Hh3cDHCPSInterfacePoolOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 7, 1, 6),
    _Hh3cDHCPSInterfacePoolOptionRowStatus_Type()
)
hh3cDHCPSInterfacePoolOptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolOptionRowStatus.setStatus("current")
_Hh3cDHCPSInterfacePoolStaticBindTable_Object = MibTable
hh3cDHCPSInterfacePoolStaticBindTable = _Hh3cDHCPSInterfacePoolStaticBindTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 8)
)
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolStaticBindTable.setStatus("current")
_Hh3cDHCPSInterfacePoolStaticBindEntry_Object = MibTableRow
hh3cDHCPSInterfacePoolStaticBindEntry = _Hh3cDHCPSInterfacePoolStaticBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 8, 1)
)
hh3cDHCPSInterfacePoolStaticBindEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-DHCPS-MIB", "hh3cDHCPSInterfacePoolStaticBindIP"),
)
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolStaticBindEntry.setStatus("current")
_Hh3cDHCPSInterfacePoolStaticBindIP_Type = IpAddress
_Hh3cDHCPSInterfacePoolStaticBindIP_Object = MibTableColumn
hh3cDHCPSInterfacePoolStaticBindIP = _Hh3cDHCPSInterfacePoolStaticBindIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 8, 1, 1),
    _Hh3cDHCPSInterfacePoolStaticBindIP_Type()
)
hh3cDHCPSInterfacePoolStaticBindIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolStaticBindIP.setStatus("current")
_Hh3cDHCPSInterfacePoolStaticBindMac_Type = MacAddress
_Hh3cDHCPSInterfacePoolStaticBindMac_Object = MibTableColumn
hh3cDHCPSInterfacePoolStaticBindMac = _Hh3cDHCPSInterfacePoolStaticBindMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 8, 1, 2),
    _Hh3cDHCPSInterfacePoolStaticBindMac_Type()
)
hh3cDHCPSInterfacePoolStaticBindMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolStaticBindMac.setStatus("current")
_Hh3cDHCPSInterfacePoolStaticBindRowStatus_Type = RowStatus
_Hh3cDHCPSInterfacePoolStaticBindRowStatus_Object = MibTableColumn
hh3cDHCPSInterfacePoolStaticBindRowStatus = _Hh3cDHCPSInterfacePoolStaticBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 8, 1, 3),
    _Hh3cDHCPSInterfacePoolStaticBindRowStatus_Type()
)
hh3cDHCPSInterfacePoolStaticBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolStaticBindRowStatus.setStatus("current")
_Hh3cDHCPSIPInUseTable_Object = MibTable
hh3cDHCPSIPInUseTable = _Hh3cDHCPSIPInUseTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 9)
)
if mibBuilder.loadTexts:
    hh3cDHCPSIPInUseTable.setStatus("deprecated")
_Hh3cDHCPSIPInUseEntry_Object = MibTableRow
hh3cDHCPSIPInUseEntry = _Hh3cDHCPSIPInUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 9, 1)
)
hh3cDHCPSIPInUseEntry.setIndexNames(
    (0, "HH3C-DHCPS-MIB", "hh3cDHCPSIPInUseHAddr"),
)
if mibBuilder.loadTexts:
    hh3cDHCPSIPInUseEntry.setStatus("deprecated")
_Hh3cDHCPSIPInUseHAddr_Type = MacAddress
_Hh3cDHCPSIPInUseHAddr_Object = MibTableColumn
hh3cDHCPSIPInUseHAddr = _Hh3cDHCPSIPInUseHAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 9, 1, 1),
    _Hh3cDHCPSIPInUseHAddr_Type()
)
hh3cDHCPSIPInUseHAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSIPInUseHAddr.setStatus("deprecated")
_Hh3cDHCPSIPInUseIP_Type = IpAddress
_Hh3cDHCPSIPInUseIP_Object = MibTableColumn
hh3cDHCPSIPInUseIP = _Hh3cDHCPSIPInUseIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 9, 1, 2),
    _Hh3cDHCPSIPInUseIP_Type()
)
hh3cDHCPSIPInUseIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSIPInUseIP.setStatus("deprecated")


class _Hh3cDHCPSIPInUseEndLease_Type(OctetString):
    """Custom type hh3cDHCPSIPInUseEndLease based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Hh3cDHCPSIPInUseEndLease_Type.__name__ = "OctetString"
_Hh3cDHCPSIPInUseEndLease_Object = MibTableColumn
hh3cDHCPSIPInUseEndLease = _Hh3cDHCPSIPInUseEndLease_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 9, 1, 3),
    _Hh3cDHCPSIPInUseEndLease_Type()
)
hh3cDHCPSIPInUseEndLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSIPInUseEndLease.setStatus("deprecated")


class _Hh3cDHCPSIPInUseType_Type(Integer32):
    """Custom type hh3cDHCPSIPInUseType based on Integer32"""
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


_Hh3cDHCPSIPInUseType_Type.__name__ = "Integer32"
_Hh3cDHCPSIPInUseType_Object = MibTableColumn
hh3cDHCPSIPInUseType = _Hh3cDHCPSIPInUseType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 9, 1, 4),
    _Hh3cDHCPSIPInUseType_Type()
)
hh3cDHCPSIPInUseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSIPInUseType.setStatus("deprecated")


class _Hh3cDHCPSIPInUsePoolName_Type(OctetString):
    """Custom type hh3cDHCPSIPInUsePoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Hh3cDHCPSIPInUsePoolName_Type.__name__ = "OctetString"
_Hh3cDHCPSIPInUsePoolName_Object = MibTableColumn
hh3cDHCPSIPInUsePoolName = _Hh3cDHCPSIPInUsePoolName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 9, 1, 5),
    _Hh3cDHCPSIPInUsePoolName_Type()
)
hh3cDHCPSIPInUsePoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSIPInUsePoolName.setStatus("deprecated")
_Hh3cDHCPSIPInUseInterface_Type = Integer32
_Hh3cDHCPSIPInUseInterface_Object = MibTableColumn
hh3cDHCPSIPInUseInterface = _Hh3cDHCPSIPInUseInterface_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 9, 1, 6),
    _Hh3cDHCPSIPInUseInterface_Type()
)
hh3cDHCPSIPInUseInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSIPInUseInterface.setStatus("deprecated")


class _Hh3cDHCPSIPInUseVlan_Type(Integer32):
    """Custom type hh3cDHCPSIPInUseVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cDHCPSIPInUseVlan_Type.__name__ = "Integer32"
_Hh3cDHCPSIPInUseVlan_Object = MibTableColumn
hh3cDHCPSIPInUseVlan = _Hh3cDHCPSIPInUseVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 9, 1, 7),
    _Hh3cDHCPSIPInUseVlan_Type()
)
hh3cDHCPSIPInUseVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSIPInUseVlan.setStatus("deprecated")
_Hh3cDHCPSIPInUseAtmpvc_Type = Integer32
_Hh3cDHCPSIPInUseAtmpvc_Object = MibTableColumn
hh3cDHCPSIPInUseAtmpvc = _Hh3cDHCPSIPInUseAtmpvc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 9, 1, 8),
    _Hh3cDHCPSIPInUseAtmpvc_Type()
)
hh3cDHCPSIPInUseAtmpvc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSIPInUseAtmpvc.setStatus("deprecated")
_Hh3cDHCPSForbiddenIPTable_Object = MibTable
hh3cDHCPSForbiddenIPTable = _Hh3cDHCPSForbiddenIPTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 10)
)
if mibBuilder.loadTexts:
    hh3cDHCPSForbiddenIPTable.setStatus("current")
_Hh3cDHCPSForbiddenIPEntry_Object = MibTableRow
hh3cDHCPSForbiddenIPEntry = _Hh3cDHCPSForbiddenIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 10, 1)
)
hh3cDHCPSForbiddenIPEntry.setIndexNames(
    (0, "HH3C-DHCPS-MIB", "hh3cDHCPSForbiddenIPStart"),
    (0, "HH3C-DHCPS-MIB", "hh3cDHCPSForbiddenIPEnd"),
)
if mibBuilder.loadTexts:
    hh3cDHCPSForbiddenIPEntry.setStatus("current")
_Hh3cDHCPSForbiddenIPStart_Type = IpAddress
_Hh3cDHCPSForbiddenIPStart_Object = MibTableColumn
hh3cDHCPSForbiddenIPStart = _Hh3cDHCPSForbiddenIPStart_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 10, 1, 1),
    _Hh3cDHCPSForbiddenIPStart_Type()
)
hh3cDHCPSForbiddenIPStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSForbiddenIPStart.setStatus("current")
_Hh3cDHCPSForbiddenIPEnd_Type = IpAddress
_Hh3cDHCPSForbiddenIPEnd_Object = MibTableColumn
hh3cDHCPSForbiddenIPEnd = _Hh3cDHCPSForbiddenIPEnd_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 10, 1, 2),
    _Hh3cDHCPSForbiddenIPEnd_Type()
)
hh3cDHCPSForbiddenIPEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSForbiddenIPEnd.setStatus("current")
_Hh3cDHCPSForbiddenIPRowStatus_Type = RowStatus
_Hh3cDHCPSForbiddenIPRowStatus_Object = MibTableColumn
hh3cDHCPSForbiddenIPRowStatus = _Hh3cDHCPSForbiddenIPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 10, 1, 3),
    _Hh3cDHCPSForbiddenIPRowStatus_Type()
)
hh3cDHCPSForbiddenIPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPSForbiddenIPRowStatus.setStatus("current")
_Hh3cDHCPSConflictIPTable_Object = MibTable
hh3cDHCPSConflictIPTable = _Hh3cDHCPSConflictIPTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 11)
)
if mibBuilder.loadTexts:
    hh3cDHCPSConflictIPTable.setStatus("current")
_Hh3cDHCPSConflictIPEntry_Object = MibTableRow
hh3cDHCPSConflictIPEntry = _Hh3cDHCPSConflictIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 11, 1)
)
hh3cDHCPSConflictIPEntry.setIndexNames(
    (0, "HH3C-DHCPS-MIB", "hh3cDHCPSConflictIP"),
)
if mibBuilder.loadTexts:
    hh3cDHCPSConflictIPEntry.setStatus("current")
_Hh3cDHCPSConflictIP_Type = IpAddress
_Hh3cDHCPSConflictIP_Object = MibTableColumn
hh3cDHCPSConflictIP = _Hh3cDHCPSConflictIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 11, 1, 1),
    _Hh3cDHCPSConflictIP_Type()
)
hh3cDHCPSConflictIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSConflictIP.setStatus("current")


class _Hh3cDHCPSConflictIPType_Type(Integer32):
    """Custom type hh3cDHCPSConflictIPType based on Integer32"""
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


_Hh3cDHCPSConflictIPType_Type.__name__ = "Integer32"
_Hh3cDHCPSConflictIPType_Object = MibTableColumn
hh3cDHCPSConflictIPType = _Hh3cDHCPSConflictIPType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 11, 1, 2),
    _Hh3cDHCPSConflictIPType_Type()
)
hh3cDHCPSConflictIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSConflictIPType.setStatus("current")


class _Hh3cDHCPSConflictIPDetectTime_Type(OctetString):
    """Custom type hh3cDHCPSConflictIPDetectTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Hh3cDHCPSConflictIPDetectTime_Type.__name__ = "OctetString"
_Hh3cDHCPSConflictIPDetectTime_Object = MibTableColumn
hh3cDHCPSConflictIPDetectTime = _Hh3cDHCPSConflictIPDetectTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 11, 1, 3),
    _Hh3cDHCPSConflictIPDetectTime_Type()
)
hh3cDHCPSConflictIPDetectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSConflictIPDetectTime.setStatus("current")


class _Hh3cDHCPSServiceStatus_Type(Hh3cDhcpSEnabledStatus):
    """Custom type hh3cDHCPSServiceStatus based on Hh3cDhcpSEnabledStatus"""


_Hh3cDHCPSServiceStatus_Object = MibScalar
hh3cDHCPSServiceStatus = _Hh3cDHCPSServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 12),
    _Hh3cDHCPSServiceStatus_Type()
)
hh3cDHCPSServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSServiceStatus.setStatus("current")


class _Hh3cDHCPSDetectingServerStatus_Type(Hh3cDhcpSEnabledStatus):
    """Custom type hh3cDHCPSDetectingServerStatus based on Hh3cDhcpSEnabledStatus"""


_Hh3cDHCPSDetectingServerStatus_Object = MibScalar
hh3cDHCPSDetectingServerStatus = _Hh3cDHCPSDetectingServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 13),
    _Hh3cDHCPSDetectingServerStatus_Type()
)
hh3cDHCPSDetectingServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSDetectingServerStatus.setStatus("current")


class _Hh3cDHCPSPingNum_Type(Integer32):
    """Custom type hh3cDHCPSPingNum based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Hh3cDHCPSPingNum_Type.__name__ = "Integer32"
_Hh3cDHCPSPingNum_Object = MibScalar
hh3cDHCPSPingNum = _Hh3cDHCPSPingNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 14),
    _Hh3cDHCPSPingNum_Type()
)
hh3cDHCPSPingNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSPingNum.setStatus("current")


class _Hh3cDHCPSPingTimeout_Type(Integer32):
    """Custom type hh3cDHCPSPingTimeout based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Hh3cDHCPSPingTimeout_Type.__name__ = "Integer32"
_Hh3cDHCPSPingTimeout_Object = MibScalar
hh3cDHCPSPingTimeout = _Hh3cDHCPSPingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 15),
    _Hh3cDHCPSPingTimeout_Type()
)
hh3cDHCPSPingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSPingTimeout.setStatus("current")


class _Hh3cDHCPSWriteDataStatus_Type(Hh3cDhcpSEnabledStatus):
    """Custom type hh3cDHCPSWriteDataStatus based on Hh3cDhcpSEnabledStatus"""


_Hh3cDHCPSWriteDataStatus_Object = MibScalar
hh3cDHCPSWriteDataStatus = _Hh3cDHCPSWriteDataStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 16),
    _Hh3cDHCPSWriteDataStatus_Type()
)
hh3cDHCPSWriteDataStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSWriteDataStatus.setStatus("current")


class _Hh3cDHCPSWriteDataDirection_Type(OctetString):
    """Custom type hh3cDHCPSWriteDataDirection based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Hh3cDHCPSWriteDataDirection_Type.__name__ = "OctetString"
_Hh3cDHCPSWriteDataDirection_Object = MibScalar
hh3cDHCPSWriteDataDirection = _Hh3cDHCPSWriteDataDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 17),
    _Hh3cDHCPSWriteDataDirection_Type()
)
hh3cDHCPSWriteDataDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSWriteDataDirection.setStatus("current")


class _Hh3cDHCPSWriteDataDelay_Type(Integer32):
    """Custom type hh3cDHCPSWriteDataDelay based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 86400),
    )


_Hh3cDHCPSWriteDataDelay_Type.__name__ = "Integer32"
_Hh3cDHCPSWriteDataDelay_Object = MibScalar
hh3cDHCPSWriteDataDelay = _Hh3cDHCPSWriteDataDelay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 18),
    _Hh3cDHCPSWriteDataDelay_Type()
)
hh3cDHCPSWriteDataDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSWriteDataDelay.setStatus("current")
_Hh3cDHCPSWriteDataRecover_Type = Hh3cDhcpSEnabledStatus
_Hh3cDHCPSWriteDataRecover_Object = MibScalar
hh3cDHCPSWriteDataRecover = _Hh3cDHCPSWriteDataRecover_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 19),
    _Hh3cDHCPSWriteDataRecover_Type()
)
hh3cDHCPSWriteDataRecover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSWriteDataRecover.setStatus("current")
_Hh3cDHCPSIPInUseResetIP_Type = IpAddress
_Hh3cDHCPSIPInUseResetIP_Object = MibScalar
hh3cDHCPSIPInUseResetIP = _Hh3cDHCPSIPInUseResetIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 20),
    _Hh3cDHCPSIPInUseResetIP_Type()
)
hh3cDHCPSIPInUseResetIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSIPInUseResetIP.setStatus("current")
_Hh3cDHCPSConflictIPResetIP_Type = IpAddress
_Hh3cDHCPSConflictIPResetIP_Object = MibScalar
hh3cDHCPSConflictIPResetIP = _Hh3cDHCPSConflictIPResetIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 21),
    _Hh3cDHCPSConflictIPResetIP_Type()
)
hh3cDHCPSConflictIPResetIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSConflictIPResetIP.setStatus("current")


class _Hh3cDHCPSIPResetFlag_Type(Integer32):
    """Custom type hh3cDHCPSIPResetFlag based on Integer32"""
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


_Hh3cDHCPSIPResetFlag_Type.__name__ = "Integer32"
_Hh3cDHCPSIPResetFlag_Object = MibScalar
hh3cDHCPSIPResetFlag = _Hh3cDHCPSIPResetFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 22),
    _Hh3cDHCPSIPResetFlag_Type()
)
hh3cDHCPSIPResetFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSIPResetFlag.setStatus("current")
_Hh3cDHCPSGlobalPoolNumber_Type = Integer32
_Hh3cDHCPSGlobalPoolNumber_Object = MibScalar
hh3cDHCPSGlobalPoolNumber = _Hh3cDHCPSGlobalPoolNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 23),
    _Hh3cDHCPSGlobalPoolNumber_Type()
)
hh3cDHCPSGlobalPoolNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolNumber.setStatus("current")
_Hh3cDHCPSGlobalPoolAutoBindingNum_Type = Integer32
_Hh3cDHCPSGlobalPoolAutoBindingNum_Object = MibScalar
hh3cDHCPSGlobalPoolAutoBindingNum = _Hh3cDHCPSGlobalPoolAutoBindingNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 24),
    _Hh3cDHCPSGlobalPoolAutoBindingNum_Type()
)
hh3cDHCPSGlobalPoolAutoBindingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolAutoBindingNum.setStatus("current")
_Hh3cDHCPSGlobalPoolManualBindingNum_Type = Integer32
_Hh3cDHCPSGlobalPoolManualBindingNum_Object = MibScalar
hh3cDHCPSGlobalPoolManualBindingNum = _Hh3cDHCPSGlobalPoolManualBindingNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 25),
    _Hh3cDHCPSGlobalPoolManualBindingNum_Type()
)
hh3cDHCPSGlobalPoolManualBindingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolManualBindingNum.setStatus("current")
_Hh3cDHCPSGlobalPoolExpiredBindingNum_Type = Integer32
_Hh3cDHCPSGlobalPoolExpiredBindingNum_Object = MibScalar
hh3cDHCPSGlobalPoolExpiredBindingNum = _Hh3cDHCPSGlobalPoolExpiredBindingNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 26),
    _Hh3cDHCPSGlobalPoolExpiredBindingNum_Type()
)
hh3cDHCPSGlobalPoolExpiredBindingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSGlobalPoolExpiredBindingNum.setStatus("current")
_Hh3cDHCPSInterfacePoolNumber_Type = Integer32
_Hh3cDHCPSInterfacePoolNumber_Object = MibScalar
hh3cDHCPSInterfacePoolNumber = _Hh3cDHCPSInterfacePoolNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 27),
    _Hh3cDHCPSInterfacePoolNumber_Type()
)
hh3cDHCPSInterfacePoolNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolNumber.setStatus("current")
_Hh3cDHCPSInterfacePoolAutoBindingNum_Type = Integer32
_Hh3cDHCPSInterfacePoolAutoBindingNum_Object = MibScalar
hh3cDHCPSInterfacePoolAutoBindingNum = _Hh3cDHCPSInterfacePoolAutoBindingNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 28),
    _Hh3cDHCPSInterfacePoolAutoBindingNum_Type()
)
hh3cDHCPSInterfacePoolAutoBindingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolAutoBindingNum.setStatus("current")
_Hh3cDHCPSInterfacePoolManualBindingNum_Type = Integer32
_Hh3cDHCPSInterfacePoolManualBindingNum_Object = MibScalar
hh3cDHCPSInterfacePoolManualBindingNum = _Hh3cDHCPSInterfacePoolManualBindingNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 29),
    _Hh3cDHCPSInterfacePoolManualBindingNum_Type()
)
hh3cDHCPSInterfacePoolManualBindingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolManualBindingNum.setStatus("current")
_Hh3cDHCPSInterfacePoolExpiredBindingNum_Type = Integer32
_Hh3cDHCPSInterfacePoolExpiredBindingNum_Object = MibScalar
hh3cDHCPSInterfacePoolExpiredBindingNum = _Hh3cDHCPSInterfacePoolExpiredBindingNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 30),
    _Hh3cDHCPSInterfacePoolExpiredBindingNum_Type()
)
hh3cDHCPSInterfacePoolExpiredBindingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSInterfacePoolExpiredBindingNum.setStatus("current")
_Hh3cDHCPSBadPktNum_Type = Integer32
_Hh3cDHCPSBadPktNum_Object = MibScalar
hh3cDHCPSBadPktNum = _Hh3cDHCPSBadPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 31),
    _Hh3cDHCPSBadPktNum_Type()
)
hh3cDHCPSBadPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSBadPktNum.setStatus("current")
_Hh3cDHCPSBootRequestPktNum_Type = Integer32
_Hh3cDHCPSBootRequestPktNum_Object = MibScalar
hh3cDHCPSBootRequestPktNum = _Hh3cDHCPSBootRequestPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 32),
    _Hh3cDHCPSBootRequestPktNum_Type()
)
hh3cDHCPSBootRequestPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSBootRequestPktNum.setStatus("current")
_Hh3cDHCPSDiscoverPktNum_Type = Integer32
_Hh3cDHCPSDiscoverPktNum_Object = MibScalar
hh3cDHCPSDiscoverPktNum = _Hh3cDHCPSDiscoverPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 33),
    _Hh3cDHCPSDiscoverPktNum_Type()
)
hh3cDHCPSDiscoverPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSDiscoverPktNum.setStatus("current")
_Hh3cDHCPSRequestPktNum_Type = Integer32
_Hh3cDHCPSRequestPktNum_Object = MibScalar
hh3cDHCPSRequestPktNum = _Hh3cDHCPSRequestPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 34),
    _Hh3cDHCPSRequestPktNum_Type()
)
hh3cDHCPSRequestPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSRequestPktNum.setStatus("current")
_Hh3cDHCPSDeclinePktNum_Type = Integer32
_Hh3cDHCPSDeclinePktNum_Object = MibScalar
hh3cDHCPSDeclinePktNum = _Hh3cDHCPSDeclinePktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 35),
    _Hh3cDHCPSDeclinePktNum_Type()
)
hh3cDHCPSDeclinePktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSDeclinePktNum.setStatus("current")
_Hh3cDHCPSReleasePktNum_Type = Integer32
_Hh3cDHCPSReleasePktNum_Object = MibScalar
hh3cDHCPSReleasePktNum = _Hh3cDHCPSReleasePktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 36),
    _Hh3cDHCPSReleasePktNum_Type()
)
hh3cDHCPSReleasePktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSReleasePktNum.setStatus("current")
_Hh3cDHCPSInformPktNum_Type = Integer32
_Hh3cDHCPSInformPktNum_Object = MibScalar
hh3cDHCPSInformPktNum = _Hh3cDHCPSInformPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 37),
    _Hh3cDHCPSInformPktNum_Type()
)
hh3cDHCPSInformPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSInformPktNum.setStatus("current")
_Hh3cDHCPSBootReplyPktNum_Type = Integer32
_Hh3cDHCPSBootReplyPktNum_Object = MibScalar
hh3cDHCPSBootReplyPktNum = _Hh3cDHCPSBootReplyPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 38),
    _Hh3cDHCPSBootReplyPktNum_Type()
)
hh3cDHCPSBootReplyPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSBootReplyPktNum.setStatus("current")
_Hh3cDHCPSOfferPktNum_Type = Integer32
_Hh3cDHCPSOfferPktNum_Object = MibScalar
hh3cDHCPSOfferPktNum = _Hh3cDHCPSOfferPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 39),
    _Hh3cDHCPSOfferPktNum_Type()
)
hh3cDHCPSOfferPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSOfferPktNum.setStatus("current")
_Hh3cDHCPSAckPktNum_Type = Integer32
_Hh3cDHCPSAckPktNum_Object = MibScalar
hh3cDHCPSAckPktNum = _Hh3cDHCPSAckPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 40),
    _Hh3cDHCPSAckPktNum_Type()
)
hh3cDHCPSAckPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSAckPktNum.setStatus("current")
_Hh3cDHCPSNakPktNum_Type = Integer32
_Hh3cDHCPSNakPktNum_Object = MibScalar
hh3cDHCPSNakPktNum = _Hh3cDHCPSNakPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 41),
    _Hh3cDHCPSNakPktNum_Type()
)
hh3cDHCPSNakPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSNakPktNum.setStatus("current")


class _Hh3cDHCPSStatisticsReset_Type(Integer32):
    """Custom type hh3cDHCPSStatisticsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Hh3cDHCPSStatisticsReset_Type.__name__ = "Integer32"
_Hh3cDHCPSStatisticsReset_Object = MibScalar
hh3cDHCPSStatisticsReset = _Hh3cDHCPSStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 42),
    _Hh3cDHCPSStatisticsReset_Type()
)
hh3cDHCPSStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPSStatisticsReset.setStatus("current")
_Hh3cDHCPSIPInUseExTable_Object = MibTable
hh3cDHCPSIPInUseExTable = _Hh3cDHCPSIPInUseExTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 43)
)
if mibBuilder.loadTexts:
    hh3cDHCPSIPInUseExTable.setStatus("current")
_Hh3cDHCPSIPInUseExEntry_Object = MibTableRow
hh3cDHCPSIPInUseExEntry = _Hh3cDHCPSIPInUseExEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 43, 1)
)
hh3cDHCPSIPInUseExEntry.setIndexNames(
    (0, "HH3C-DHCPS-MIB", "hh3cDHCPSIPInUseHAddrEx"),
    (0, "HH3C-DHCPS-MIB", "hh3cDHCPSIPInUseVlanIdEx"),
)
if mibBuilder.loadTexts:
    hh3cDHCPSIPInUseExEntry.setStatus("current")
_Hh3cDHCPSIPInUseHAddrEx_Type = MacAddress
_Hh3cDHCPSIPInUseHAddrEx_Object = MibTableColumn
hh3cDHCPSIPInUseHAddrEx = _Hh3cDHCPSIPInUseHAddrEx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 43, 1, 1),
    _Hh3cDHCPSIPInUseHAddrEx_Type()
)
hh3cDHCPSIPInUseHAddrEx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDHCPSIPInUseHAddrEx.setStatus("current")


class _Hh3cDHCPSIPInUseVlanIdEx_Type(Integer32):
    """Custom type hh3cDHCPSIPInUseVlanIdEx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(60000, 60000),
    )


_Hh3cDHCPSIPInUseVlanIdEx_Type.__name__ = "Integer32"
_Hh3cDHCPSIPInUseVlanIdEx_Object = MibTableColumn
hh3cDHCPSIPInUseVlanIdEx = _Hh3cDHCPSIPInUseVlanIdEx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 43, 1, 2),
    _Hh3cDHCPSIPInUseVlanIdEx_Type()
)
hh3cDHCPSIPInUseVlanIdEx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDHCPSIPInUseVlanIdEx.setStatus("current")
_Hh3cDHCPSIPInUseIPEx_Type = IpAddress
_Hh3cDHCPSIPInUseIPEx_Object = MibTableColumn
hh3cDHCPSIPInUseIPEx = _Hh3cDHCPSIPInUseIPEx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 43, 1, 3),
    _Hh3cDHCPSIPInUseIPEx_Type()
)
hh3cDHCPSIPInUseIPEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSIPInUseIPEx.setStatus("current")


class _Hh3cDHCPSIPInUseEndLeaseEx_Type(OctetString):
    """Custom type hh3cDHCPSIPInUseEndLeaseEx based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Hh3cDHCPSIPInUseEndLeaseEx_Type.__name__ = "OctetString"
_Hh3cDHCPSIPInUseEndLeaseEx_Object = MibTableColumn
hh3cDHCPSIPInUseEndLeaseEx = _Hh3cDHCPSIPInUseEndLeaseEx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 43, 1, 4),
    _Hh3cDHCPSIPInUseEndLeaseEx_Type()
)
hh3cDHCPSIPInUseEndLeaseEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSIPInUseEndLeaseEx.setStatus("current")


class _Hh3cDHCPSIPInUseTypeEx_Type(Integer32):
    """Custom type hh3cDHCPSIPInUseTypeEx based on Integer32"""
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


_Hh3cDHCPSIPInUseTypeEx_Type.__name__ = "Integer32"
_Hh3cDHCPSIPInUseTypeEx_Object = MibTableColumn
hh3cDHCPSIPInUseTypeEx = _Hh3cDHCPSIPInUseTypeEx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 43, 1, 5),
    _Hh3cDHCPSIPInUseTypeEx_Type()
)
hh3cDHCPSIPInUseTypeEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSIPInUseTypeEx.setStatus("current")


class _Hh3cDHCPSIPInUsePoolNameEx_Type(OctetString):
    """Custom type hh3cDHCPSIPInUsePoolNameEx based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Hh3cDHCPSIPInUsePoolNameEx_Type.__name__ = "OctetString"
_Hh3cDHCPSIPInUsePoolNameEx_Object = MibTableColumn
hh3cDHCPSIPInUsePoolNameEx = _Hh3cDHCPSIPInUsePoolNameEx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 43, 1, 6),
    _Hh3cDHCPSIPInUsePoolNameEx_Type()
)
hh3cDHCPSIPInUsePoolNameEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSIPInUsePoolNameEx.setStatus("current")
_Hh3cDHCPSIPInUseIfIndexEx_Type = Integer32
_Hh3cDHCPSIPInUseIfIndexEx_Object = MibTableColumn
hh3cDHCPSIPInUseIfIndexEx = _Hh3cDHCPSIPInUseIfIndexEx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 43, 1, 7),
    _Hh3cDHCPSIPInUseIfIndexEx_Type()
)
hh3cDHCPSIPInUseIfIndexEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSIPInUseIfIndexEx.setStatus("current")


class _Hh3cDHCPSIPInUseServerPortVlanIdEx_Type(Integer32):
    """Custom type hh3cDHCPSIPInUseServerPortVlanIdEx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cDHCPSIPInUseServerPortVlanIdEx_Type.__name__ = "Integer32"
_Hh3cDHCPSIPInUseServerPortVlanIdEx_Object = MibTableColumn
hh3cDHCPSIPInUseServerPortVlanIdEx = _Hh3cDHCPSIPInUseServerPortVlanIdEx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 43, 1, 8),
    _Hh3cDHCPSIPInUseServerPortVlanIdEx_Type()
)
hh3cDHCPSIPInUseServerPortVlanIdEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSIPInUseServerPortVlanIdEx.setStatus("current")
_Hh3cDHCPSIPInUseAtmpvcEx_Type = Integer32
_Hh3cDHCPSIPInUseAtmpvcEx_Object = MibTableColumn
hh3cDHCPSIPInUseAtmpvcEx = _Hh3cDHCPSIPInUseAtmpvcEx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 1, 43, 1, 9),
    _Hh3cDHCPSIPInUseAtmpvcEx_Type()
)
hh3cDHCPSIPInUseAtmpvcEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPSIPInUseAtmpvcEx.setStatus("current")
_Hh3cDHCPServerMIBConformance_ObjectIdentity = ObjectIdentity
hh3cDHCPServerMIBConformance = _Hh3cDHCPServerMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 2)
)
_Hh3cDHCPServerMIBCompliances_ObjectIdentity = ObjectIdentity
hh3cDHCPServerMIBCompliances = _Hh3cDHCPServerMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 2, 1)
)
_Hh3cDHCPServerMIBGroups_ObjectIdentity = ObjectIdentity
hh3cDHCPServerMIBGroups = _Hh3cDHCPServerMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 2, 2)
)

# Managed Objects groups

hh3cDHCPServerMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 8, 2, 2, 2, 1)
)
hh3cDHCPServerMIBGroup.setObjects(
      *(("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolName"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolRowStatus"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolType"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolNetwork"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolNetworkMask"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolHostIPAddr"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolHostMask"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolHostHAddr"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolConfigUndoFlag"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolLeaseDay"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolLeaseHour"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolLeaseMinute"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolLeaseUnlimited"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolDomainName"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolClientGatewayIPString"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolClientGatewayIPUndo"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolClientDNSIPString"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolClientDNSIPUndo"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolClientNetbiosType"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolClientNbnsIPString"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolClientNbnsIPUndo"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolParaUndoFlag"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolIPInUseReset"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolOptionCode"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolOptionType"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolOptionAscii"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolOptionHexString"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolOptionIPString"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolOptionRowStatus"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalTreeParentNodeName"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalTreeChildNodeName"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalTreePreSiblingNodeName"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalTreeSiblingNodeName"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSInterfacePoolLeaseDay"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSInterfacePoolLeaseHour"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSInterfacePoolLeaseMinute"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSInterfacePoolLeaseUnlimited"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSInterfacePoolDomainName"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSInterfacePoolClientDNSIPString"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSInterfacePoolClientDNSIPUndo"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSInterfacePoolClientNetbiosType"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSInterfacePoolClientNbnsIPString"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSInterfacePoolClientNbnsIPUndo"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSInterfacePoolParaUndoFlag"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSInterfacePoolIPInUseReset"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSInterfacePoolOptionCode"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSInterfacePoolOptionType"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSInterfacePoolOptionAscii"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSInterfacePoolOptionHexString"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSInterfacePoolOptionIPString"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSInterfacePoolOptionRowStatus"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSInterfacePoolStaticBindIP"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSInterfacePoolStaticBindMac"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSInterfacePoolStaticBindRowStatus"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSIPInUseHAddr"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSIPInUseIP"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSIPInUseEndLease"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSIPInUseType"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSIPInUsePoolName"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSIPInUseInterface"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSIPInUseVlan"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSIPInUseAtmpvc"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSForbiddenIPStart"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSForbiddenIPEnd"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSForbiddenIPRowStatus"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSConflictIP"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSConflictIPType"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSConflictIPDetectTime"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSServiceStatus"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSDetectingServerStatus"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSPingNum"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSPingTimeout"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSWriteDataStatus"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSWriteDataDirection"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSWriteDataDelay"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSWriteDataRecover"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSIPInUseResetIP"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSConflictIPResetIP"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSIPResetFlag"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolNumber"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolAutoBindingNum"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolManualBindingNum"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSGlobalPoolExpiredBindingNum"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSInterfacePoolNumber"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSInterfacePoolAutoBindingNum"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSInterfacePoolManualBindingNum"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSInterfacePoolExpiredBindingNum"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSBadPktNum"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSBootRequestPktNum"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSDiscoverPktNum"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSRequestPktNum"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSDeclinePktNum"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSReleasePktNum"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSInformPktNum"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSBootReplyPktNum"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSOfferPktNum"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSAckPktNum"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSNakPktNum"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSStatisticsReset"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSIPInUseHAddrEx"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSIPInUseVlanIdEx"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSIPInUseIPEx"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSIPInUseEndLeaseEx"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSIPInUseTypeEx"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSIPInUsePoolNameEx"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSIPInUseIfIndexEx"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSIPInUseServerPortVlanIdEx"),
        ("HH3C-DHCPS-MIB", "hh3cDHCPSIPInUseAtmpvcEx"))
)
if mibBuilder.loadTexts:
    hh3cDHCPServerMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DHCPS-MIB",
    **{"Hh3cDhcpSEnabledStatus": Hh3cDhcpSEnabledStatus,
       "hh3cDHCPServerMib": hh3cDHCPServerMib,
       "hh3cDHCPServerMibObject": hh3cDHCPServerMibObject,
       "hh3cDHCPSGlobalPoolTable": hh3cDHCPSGlobalPoolTable,
       "hh3cDHCPSGlobalPoolEntry": hh3cDHCPSGlobalPoolEntry,
       "hh3cDHCPSGlobalPoolName": hh3cDHCPSGlobalPoolName,
       "hh3cDHCPSGlobalPoolRowStatus": hh3cDHCPSGlobalPoolRowStatus,
       "hh3cDHCPSGlobalPoolConfigTable": hh3cDHCPSGlobalPoolConfigTable,
       "hh3cDHCPSGlobalPoolConfigEntry": hh3cDHCPSGlobalPoolConfigEntry,
       "hh3cDHCPSGlobalPoolType": hh3cDHCPSGlobalPoolType,
       "hh3cDHCPSGlobalPoolNetwork": hh3cDHCPSGlobalPoolNetwork,
       "hh3cDHCPSGlobalPoolNetworkMask": hh3cDHCPSGlobalPoolNetworkMask,
       "hh3cDHCPSGlobalPoolHostIPAddr": hh3cDHCPSGlobalPoolHostIPAddr,
       "hh3cDHCPSGlobalPoolHostMask": hh3cDHCPSGlobalPoolHostMask,
       "hh3cDHCPSGlobalPoolHostHAddr": hh3cDHCPSGlobalPoolHostHAddr,
       "hh3cDHCPSGlobalPoolConfigUndoFlag": hh3cDHCPSGlobalPoolConfigUndoFlag,
       "hh3cDHCPSGlobalPoolParaTable": hh3cDHCPSGlobalPoolParaTable,
       "hh3cDHCPSGlobalPoolParaEntry": hh3cDHCPSGlobalPoolParaEntry,
       "hh3cDHCPSGlobalPoolLeaseDay": hh3cDHCPSGlobalPoolLeaseDay,
       "hh3cDHCPSGlobalPoolLeaseHour": hh3cDHCPSGlobalPoolLeaseHour,
       "hh3cDHCPSGlobalPoolLeaseMinute": hh3cDHCPSGlobalPoolLeaseMinute,
       "hh3cDHCPSGlobalPoolLeaseUnlimited": hh3cDHCPSGlobalPoolLeaseUnlimited,
       "hh3cDHCPSGlobalPoolDomainName": hh3cDHCPSGlobalPoolDomainName,
       "hh3cDHCPSGlobalPoolClientGatewayIPString": hh3cDHCPSGlobalPoolClientGatewayIPString,
       "hh3cDHCPSGlobalPoolClientGatewayIPUndo": hh3cDHCPSGlobalPoolClientGatewayIPUndo,
       "hh3cDHCPSGlobalPoolClientDNSIPString": hh3cDHCPSGlobalPoolClientDNSIPString,
       "hh3cDHCPSGlobalPoolClientDNSIPUndo": hh3cDHCPSGlobalPoolClientDNSIPUndo,
       "hh3cDHCPSGlobalPoolClientNetbiosType": hh3cDHCPSGlobalPoolClientNetbiosType,
       "hh3cDHCPSGlobalPoolClientNbnsIPString": hh3cDHCPSGlobalPoolClientNbnsIPString,
       "hh3cDHCPSGlobalPoolClientNbnsIPUndo": hh3cDHCPSGlobalPoolClientNbnsIPUndo,
       "hh3cDHCPSGlobalPoolParaUndoFlag": hh3cDHCPSGlobalPoolParaUndoFlag,
       "hh3cDHCPSGlobalPoolIPInUseReset": hh3cDHCPSGlobalPoolIPInUseReset,
       "hh3cDHCPSGlobalPoolOptionTable": hh3cDHCPSGlobalPoolOptionTable,
       "hh3cDHCPSGlobalPoolOptionEntry": hh3cDHCPSGlobalPoolOptionEntry,
       "hh3cDHCPSGlobalPoolOptionCode": hh3cDHCPSGlobalPoolOptionCode,
       "hh3cDHCPSGlobalPoolOptionType": hh3cDHCPSGlobalPoolOptionType,
       "hh3cDHCPSGlobalPoolOptionAscii": hh3cDHCPSGlobalPoolOptionAscii,
       "hh3cDHCPSGlobalPoolOptionHexString": hh3cDHCPSGlobalPoolOptionHexString,
       "hh3cDHCPSGlobalPoolOptionIPString": hh3cDHCPSGlobalPoolOptionIPString,
       "hh3cDHCPSGlobalPoolOptionRowStatus": hh3cDHCPSGlobalPoolOptionRowStatus,
       "hh3cDHCPSGlobalTreeTable": hh3cDHCPSGlobalTreeTable,
       "hh3cDHCPSGlobalTreeEntry": hh3cDHCPSGlobalTreeEntry,
       "hh3cDHCPSGlobalTreeParentNodeName": hh3cDHCPSGlobalTreeParentNodeName,
       "hh3cDHCPSGlobalTreeChildNodeName": hh3cDHCPSGlobalTreeChildNodeName,
       "hh3cDHCPSGlobalTreePreSiblingNodeName": hh3cDHCPSGlobalTreePreSiblingNodeName,
       "hh3cDHCPSGlobalTreeSiblingNodeName": hh3cDHCPSGlobalTreeSiblingNodeName,
       "hh3cDHCPSInterfacePoolParaTable": hh3cDHCPSInterfacePoolParaTable,
       "hh3cDHCPSInterfacePoolParaEntry": hh3cDHCPSInterfacePoolParaEntry,
       "hh3cDHCPSInterfacePoolLeaseDay": hh3cDHCPSInterfacePoolLeaseDay,
       "hh3cDHCPSInterfacePoolLeaseHour": hh3cDHCPSInterfacePoolLeaseHour,
       "hh3cDHCPSInterfacePoolLeaseMinute": hh3cDHCPSInterfacePoolLeaseMinute,
       "hh3cDHCPSInterfacePoolLeaseUnlimited": hh3cDHCPSInterfacePoolLeaseUnlimited,
       "hh3cDHCPSInterfacePoolDomainName": hh3cDHCPSInterfacePoolDomainName,
       "hh3cDHCPSInterfacePoolClientDNSIPString": hh3cDHCPSInterfacePoolClientDNSIPString,
       "hh3cDHCPSInterfacePoolClientDNSIPUndo": hh3cDHCPSInterfacePoolClientDNSIPUndo,
       "hh3cDHCPSInterfacePoolClientNetbiosType": hh3cDHCPSInterfacePoolClientNetbiosType,
       "hh3cDHCPSInterfacePoolClientNbnsIPString": hh3cDHCPSInterfacePoolClientNbnsIPString,
       "hh3cDHCPSInterfacePoolClientNbnsIPUndo": hh3cDHCPSInterfacePoolClientNbnsIPUndo,
       "hh3cDHCPSInterfacePoolParaUndoFlag": hh3cDHCPSInterfacePoolParaUndoFlag,
       "hh3cDHCPSInterfacePoolIPInUseReset": hh3cDHCPSInterfacePoolIPInUseReset,
       "hh3cDHCPSInterfacePoolOptionTable": hh3cDHCPSInterfacePoolOptionTable,
       "hh3cDHCPSInterfacePoolOptionEntry": hh3cDHCPSInterfacePoolOptionEntry,
       "hh3cDHCPSInterfacePoolOptionCode": hh3cDHCPSInterfacePoolOptionCode,
       "hh3cDHCPSInterfacePoolOptionType": hh3cDHCPSInterfacePoolOptionType,
       "hh3cDHCPSInterfacePoolOptionAscii": hh3cDHCPSInterfacePoolOptionAscii,
       "hh3cDHCPSInterfacePoolOptionHexString": hh3cDHCPSInterfacePoolOptionHexString,
       "hh3cDHCPSInterfacePoolOptionIPString": hh3cDHCPSInterfacePoolOptionIPString,
       "hh3cDHCPSInterfacePoolOptionRowStatus": hh3cDHCPSInterfacePoolOptionRowStatus,
       "hh3cDHCPSInterfacePoolStaticBindTable": hh3cDHCPSInterfacePoolStaticBindTable,
       "hh3cDHCPSInterfacePoolStaticBindEntry": hh3cDHCPSInterfacePoolStaticBindEntry,
       "hh3cDHCPSInterfacePoolStaticBindIP": hh3cDHCPSInterfacePoolStaticBindIP,
       "hh3cDHCPSInterfacePoolStaticBindMac": hh3cDHCPSInterfacePoolStaticBindMac,
       "hh3cDHCPSInterfacePoolStaticBindRowStatus": hh3cDHCPSInterfacePoolStaticBindRowStatus,
       "hh3cDHCPSIPInUseTable": hh3cDHCPSIPInUseTable,
       "hh3cDHCPSIPInUseEntry": hh3cDHCPSIPInUseEntry,
       "hh3cDHCPSIPInUseHAddr": hh3cDHCPSIPInUseHAddr,
       "hh3cDHCPSIPInUseIP": hh3cDHCPSIPInUseIP,
       "hh3cDHCPSIPInUseEndLease": hh3cDHCPSIPInUseEndLease,
       "hh3cDHCPSIPInUseType": hh3cDHCPSIPInUseType,
       "hh3cDHCPSIPInUsePoolName": hh3cDHCPSIPInUsePoolName,
       "hh3cDHCPSIPInUseInterface": hh3cDHCPSIPInUseInterface,
       "hh3cDHCPSIPInUseVlan": hh3cDHCPSIPInUseVlan,
       "hh3cDHCPSIPInUseAtmpvc": hh3cDHCPSIPInUseAtmpvc,
       "hh3cDHCPSForbiddenIPTable": hh3cDHCPSForbiddenIPTable,
       "hh3cDHCPSForbiddenIPEntry": hh3cDHCPSForbiddenIPEntry,
       "hh3cDHCPSForbiddenIPStart": hh3cDHCPSForbiddenIPStart,
       "hh3cDHCPSForbiddenIPEnd": hh3cDHCPSForbiddenIPEnd,
       "hh3cDHCPSForbiddenIPRowStatus": hh3cDHCPSForbiddenIPRowStatus,
       "hh3cDHCPSConflictIPTable": hh3cDHCPSConflictIPTable,
       "hh3cDHCPSConflictIPEntry": hh3cDHCPSConflictIPEntry,
       "hh3cDHCPSConflictIP": hh3cDHCPSConflictIP,
       "hh3cDHCPSConflictIPType": hh3cDHCPSConflictIPType,
       "hh3cDHCPSConflictIPDetectTime": hh3cDHCPSConflictIPDetectTime,
       "hh3cDHCPSServiceStatus": hh3cDHCPSServiceStatus,
       "hh3cDHCPSDetectingServerStatus": hh3cDHCPSDetectingServerStatus,
       "hh3cDHCPSPingNum": hh3cDHCPSPingNum,
       "hh3cDHCPSPingTimeout": hh3cDHCPSPingTimeout,
       "hh3cDHCPSWriteDataStatus": hh3cDHCPSWriteDataStatus,
       "hh3cDHCPSWriteDataDirection": hh3cDHCPSWriteDataDirection,
       "hh3cDHCPSWriteDataDelay": hh3cDHCPSWriteDataDelay,
       "hh3cDHCPSWriteDataRecover": hh3cDHCPSWriteDataRecover,
       "hh3cDHCPSIPInUseResetIP": hh3cDHCPSIPInUseResetIP,
       "hh3cDHCPSConflictIPResetIP": hh3cDHCPSConflictIPResetIP,
       "hh3cDHCPSIPResetFlag": hh3cDHCPSIPResetFlag,
       "hh3cDHCPSGlobalPoolNumber": hh3cDHCPSGlobalPoolNumber,
       "hh3cDHCPSGlobalPoolAutoBindingNum": hh3cDHCPSGlobalPoolAutoBindingNum,
       "hh3cDHCPSGlobalPoolManualBindingNum": hh3cDHCPSGlobalPoolManualBindingNum,
       "hh3cDHCPSGlobalPoolExpiredBindingNum": hh3cDHCPSGlobalPoolExpiredBindingNum,
       "hh3cDHCPSInterfacePoolNumber": hh3cDHCPSInterfacePoolNumber,
       "hh3cDHCPSInterfacePoolAutoBindingNum": hh3cDHCPSInterfacePoolAutoBindingNum,
       "hh3cDHCPSInterfacePoolManualBindingNum": hh3cDHCPSInterfacePoolManualBindingNum,
       "hh3cDHCPSInterfacePoolExpiredBindingNum": hh3cDHCPSInterfacePoolExpiredBindingNum,
       "hh3cDHCPSBadPktNum": hh3cDHCPSBadPktNum,
       "hh3cDHCPSBootRequestPktNum": hh3cDHCPSBootRequestPktNum,
       "hh3cDHCPSDiscoverPktNum": hh3cDHCPSDiscoverPktNum,
       "hh3cDHCPSRequestPktNum": hh3cDHCPSRequestPktNum,
       "hh3cDHCPSDeclinePktNum": hh3cDHCPSDeclinePktNum,
       "hh3cDHCPSReleasePktNum": hh3cDHCPSReleasePktNum,
       "hh3cDHCPSInformPktNum": hh3cDHCPSInformPktNum,
       "hh3cDHCPSBootReplyPktNum": hh3cDHCPSBootReplyPktNum,
       "hh3cDHCPSOfferPktNum": hh3cDHCPSOfferPktNum,
       "hh3cDHCPSAckPktNum": hh3cDHCPSAckPktNum,
       "hh3cDHCPSNakPktNum": hh3cDHCPSNakPktNum,
       "hh3cDHCPSStatisticsReset": hh3cDHCPSStatisticsReset,
       "hh3cDHCPSIPInUseExTable": hh3cDHCPSIPInUseExTable,
       "hh3cDHCPSIPInUseExEntry": hh3cDHCPSIPInUseExEntry,
       "hh3cDHCPSIPInUseHAddrEx": hh3cDHCPSIPInUseHAddrEx,
       "hh3cDHCPSIPInUseVlanIdEx": hh3cDHCPSIPInUseVlanIdEx,
       "hh3cDHCPSIPInUseIPEx": hh3cDHCPSIPInUseIPEx,
       "hh3cDHCPSIPInUseEndLeaseEx": hh3cDHCPSIPInUseEndLeaseEx,
       "hh3cDHCPSIPInUseTypeEx": hh3cDHCPSIPInUseTypeEx,
       "hh3cDHCPSIPInUsePoolNameEx": hh3cDHCPSIPInUsePoolNameEx,
       "hh3cDHCPSIPInUseIfIndexEx": hh3cDHCPSIPInUseIfIndexEx,
       "hh3cDHCPSIPInUseServerPortVlanIdEx": hh3cDHCPSIPInUseServerPortVlanIdEx,
       "hh3cDHCPSIPInUseAtmpvcEx": hh3cDHCPSIPInUseAtmpvcEx,
       "hh3cDHCPServerMIBConformance": hh3cDHCPServerMIBConformance,
       "hh3cDHCPServerMIBCompliances": hh3cDHCPServerMIBCompliances,
       "hh3cDHCPServerMIBGroups": hh3cDHCPServerMIBGroups,
       "hh3cDHCPServerMIBGroup": hh3cDHCPServerMIBGroup}
)
