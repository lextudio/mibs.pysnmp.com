# SNMP MIB module (HM2-DHCPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-DHCPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:52 2024
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

(HmEnabledStatus,
 hm2ConfigurationMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus",
    "hm2ConfigurationMibs")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

hm2DhcpsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 91)
)
hm2DhcpsMib.setRevisions(
        ("2012-03-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2DHCPServerMibNotifications_ObjectIdentity = ObjectIdentity
hm2DHCPServerMibNotifications = _Hm2DHCPServerMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 0)
)
_Hm2DHCPServerMibObjects_ObjectIdentity = ObjectIdentity
hm2DHCPServerMibObjects = _Hm2DHCPServerMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1)
)
_Hm2DHCPServerGroup_ObjectIdentity = ObjectIdentity
hm2DHCPServerGroup = _Hm2DHCPServerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1)
)
_Hm2DHCPServerConfigGroup_ObjectIdentity = ObjectIdentity
hm2DHCPServerConfigGroup = _Hm2DHCPServerConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 1)
)


class _Hm2DHCPServerMode_Type(HmEnabledStatus):
    """Custom type hm2DHCPServerMode based on HmEnabledStatus"""


_Hm2DHCPServerMode_Object = MibScalar
hm2DHCPServerMode = _Hm2DHCPServerMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 1, 1),
    _Hm2DHCPServerMode_Type()
)
hm2DHCPServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DHCPServerMode.setStatus("current")
_Hm2DHCPServerMaxPoolEntries_Type = Unsigned32
_Hm2DHCPServerMaxPoolEntries_Object = MibScalar
hm2DHCPServerMaxPoolEntries = _Hm2DHCPServerMaxPoolEntries_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 1, 2),
    _Hm2DHCPServerMaxPoolEntries_Type()
)
hm2DHCPServerMaxPoolEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerMaxPoolEntries.setStatus("current")
_Hm2DHCPServerMaxLeaseEntries_Type = Unsigned32
_Hm2DHCPServerMaxLeaseEntries_Object = MibScalar
hm2DHCPServerMaxLeaseEntries = _Hm2DHCPServerMaxLeaseEntries_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 1, 3),
    _Hm2DHCPServerMaxLeaseEntries_Type()
)
hm2DHCPServerMaxLeaseEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerMaxLeaseEntries.setStatus("current")
_Hm2DHCPServerPoolTable_Object = MibTable
hm2DHCPServerPoolTable = _Hm2DHCPServerPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hm2DHCPServerPoolTable.setStatus("current")
_Hm2DHCPServerPoolEntry_Object = MibTableRow
hm2DHCPServerPoolEntry = _Hm2DHCPServerPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 1, 5, 1)
)
hm2DHCPServerPoolEntry.setIndexNames(
    (0, "HM2-DHCPS-MIB", "hm2DHCPServerPoolIndex"),
)
if mibBuilder.loadTexts:
    hm2DHCPServerPoolEntry.setStatus("current")


class _Hm2DHCPServerPoolIndex_Type(Unsigned32):
    """Custom type hm2DHCPServerPoolIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Hm2DHCPServerPoolIndex_Type.__name__ = "Unsigned32"
_Hm2DHCPServerPoolIndex_Object = MibTableColumn
hm2DHCPServerPoolIndex = _Hm2DHCPServerPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 1, 5, 1, 1),
    _Hm2DHCPServerPoolIndex_Type()
)
hm2DHCPServerPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerPoolIndex.setStatus("current")
_Hm2DHCPServerPoolStartIpAddress_Type = IpAddress
_Hm2DHCPServerPoolStartIpAddress_Object = MibTableColumn
hm2DHCPServerPoolStartIpAddress = _Hm2DHCPServerPoolStartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 1, 5, 1, 2),
    _Hm2DHCPServerPoolStartIpAddress_Type()
)
hm2DHCPServerPoolStartIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DHCPServerPoolStartIpAddress.setStatus("current")
_Hm2DHCPServerPoolEndIpAddress_Type = IpAddress
_Hm2DHCPServerPoolEndIpAddress_Object = MibTableColumn
hm2DHCPServerPoolEndIpAddress = _Hm2DHCPServerPoolEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 1, 5, 1, 3),
    _Hm2DHCPServerPoolEndIpAddress_Type()
)
hm2DHCPServerPoolEndIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DHCPServerPoolEndIpAddress.setStatus("current")


class _Hm2DHCPServerPoolLeaseTime_Type(Unsigned32):
    """Custom type hm2DHCPServerPoolLeaseTime based on Unsigned32"""
    defaultValue = 86400


_Hm2DHCPServerPoolLeaseTime_Object = MibTableColumn
hm2DHCPServerPoolLeaseTime = _Hm2DHCPServerPoolLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 1, 5, 1, 4),
    _Hm2DHCPServerPoolLeaseTime_Type()
)
hm2DHCPServerPoolLeaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DHCPServerPoolLeaseTime.setStatus("current")


class _Hm2DHCPServerPoolFlags_Type(Bits):
    """Custom type hm2DHCPServerPoolFlags based on Bits"""
    namedValues = NamedValues(
        *(("circuitid", 5),
          ("clientid", 3),
          ("dynamic", 6),
          ("gateway", 2),
          ("interface", 0),
          ("mac", 1),
          ("remoteid", 4),
          ("vlanid", 7))
    )

_Hm2DHCPServerPoolFlags_Type.__name__ = "Bits"
_Hm2DHCPServerPoolFlags_Object = MibTableColumn
hm2DHCPServerPoolFlags = _Hm2DHCPServerPoolFlags_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 1, 5, 1, 5),
    _Hm2DHCPServerPoolFlags_Type()
)
hm2DHCPServerPoolFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DHCPServerPoolFlags.setStatus("current")
_Hm2DHCPServerPoolIfIndex_Type = Integer32
_Hm2DHCPServerPoolIfIndex_Object = MibTableColumn
hm2DHCPServerPoolIfIndex = _Hm2DHCPServerPoolIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 1, 5, 1, 6),
    _Hm2DHCPServerPoolIfIndex_Type()
)
hm2DHCPServerPoolIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DHCPServerPoolIfIndex.setStatus("current")
_Hm2DHCPServerPoolMacAddress_Type = MacAddress
_Hm2DHCPServerPoolMacAddress_Object = MibTableColumn
hm2DHCPServerPoolMacAddress = _Hm2DHCPServerPoolMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 1, 5, 1, 7),
    _Hm2DHCPServerPoolMacAddress_Type()
)
hm2DHCPServerPoolMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DHCPServerPoolMacAddress.setStatus("current")
_Hm2DHCPServerPoolGateway_Type = IpAddress
_Hm2DHCPServerPoolGateway_Object = MibTableColumn
hm2DHCPServerPoolGateway = _Hm2DHCPServerPoolGateway_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 1, 5, 1, 8),
    _Hm2DHCPServerPoolGateway_Type()
)
hm2DHCPServerPoolGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DHCPServerPoolGateway.setStatus("current")
_Hm2DHCPServerPoolClientId_Type = OctetString
_Hm2DHCPServerPoolClientId_Object = MibTableColumn
hm2DHCPServerPoolClientId = _Hm2DHCPServerPoolClientId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 1, 5, 1, 9),
    _Hm2DHCPServerPoolClientId_Type()
)
hm2DHCPServerPoolClientId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DHCPServerPoolClientId.setStatus("current")
_Hm2DHCPServerPoolRemoteId_Type = OctetString
_Hm2DHCPServerPoolRemoteId_Object = MibTableColumn
hm2DHCPServerPoolRemoteId = _Hm2DHCPServerPoolRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 1, 5, 1, 10),
    _Hm2DHCPServerPoolRemoteId_Type()
)
hm2DHCPServerPoolRemoteId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DHCPServerPoolRemoteId.setStatus("current")
_Hm2DHCPServerPoolCircuitId_Type = OctetString
_Hm2DHCPServerPoolCircuitId_Object = MibTableColumn
hm2DHCPServerPoolCircuitId = _Hm2DHCPServerPoolCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 1, 5, 1, 11),
    _Hm2DHCPServerPoolCircuitId_Type()
)
hm2DHCPServerPoolCircuitId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DHCPServerPoolCircuitId.setStatus("current")


class _Hm2DHCPServerPoolHirschmannClient_Type(HmEnabledStatus):
    """Custom type hm2DHCPServerPoolHirschmannClient based on HmEnabledStatus"""


_Hm2DHCPServerPoolHirschmannClient_Object = MibTableColumn
hm2DHCPServerPoolHirschmannClient = _Hm2DHCPServerPoolHirschmannClient_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 1, 5, 1, 12),
    _Hm2DHCPServerPoolHirschmannClient_Type()
)
hm2DHCPServerPoolHirschmannClient.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DHCPServerPoolHirschmannClient.setStatus("current")
_Hm2DHCPServerPoolVlanId_Type = Integer32
_Hm2DHCPServerPoolVlanId_Object = MibTableColumn
hm2DHCPServerPoolVlanId = _Hm2DHCPServerPoolVlanId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 1, 5, 1, 13),
    _Hm2DHCPServerPoolVlanId_Type()
)
hm2DHCPServerPoolVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DHCPServerPoolVlanId.setStatus("current")


class _Hm2DHCPServerPoolOptionConfFileName_Type(DisplayString):
    """Custom type hm2DHCPServerPoolOptionConfFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_Hm2DHCPServerPoolOptionConfFileName_Type.__name__ = "DisplayString"
_Hm2DHCPServerPoolOptionConfFileName_Object = MibTableColumn
hm2DHCPServerPoolOptionConfFileName = _Hm2DHCPServerPoolOptionConfFileName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 1, 5, 1, 30),
    _Hm2DHCPServerPoolOptionConfFileName_Type()
)
hm2DHCPServerPoolOptionConfFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DHCPServerPoolOptionConfFileName.setStatus("current")
_Hm2DHCPServerPoolOptionGateway_Type = IpAddress
_Hm2DHCPServerPoolOptionGateway_Object = MibTableColumn
hm2DHCPServerPoolOptionGateway = _Hm2DHCPServerPoolOptionGateway_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 1, 5, 1, 31),
    _Hm2DHCPServerPoolOptionGateway_Type()
)
hm2DHCPServerPoolOptionGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DHCPServerPoolOptionGateway.setStatus("current")
_Hm2DHCPServerPoolOptionNetmask_Type = IpAddress
_Hm2DHCPServerPoolOptionNetmask_Object = MibTableColumn
hm2DHCPServerPoolOptionNetmask = _Hm2DHCPServerPoolOptionNetmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 1, 5, 1, 32),
    _Hm2DHCPServerPoolOptionNetmask_Type()
)
hm2DHCPServerPoolOptionNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DHCPServerPoolOptionNetmask.setStatus("current")
_Hm2DHCPServerPoolOptionWINS_Type = IpAddress
_Hm2DHCPServerPoolOptionWINS_Object = MibTableColumn
hm2DHCPServerPoolOptionWINS = _Hm2DHCPServerPoolOptionWINS_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 1, 5, 1, 33),
    _Hm2DHCPServerPoolOptionWINS_Type()
)
hm2DHCPServerPoolOptionWINS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DHCPServerPoolOptionWINS.setStatus("current")
_Hm2DHCPServerPoolOptionDNS_Type = IpAddress
_Hm2DHCPServerPoolOptionDNS_Object = MibTableColumn
hm2DHCPServerPoolOptionDNS = _Hm2DHCPServerPoolOptionDNS_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 1, 5, 1, 34),
    _Hm2DHCPServerPoolOptionDNS_Type()
)
hm2DHCPServerPoolOptionDNS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DHCPServerPoolOptionDNS.setStatus("current")


class _Hm2DHCPServerPoolOptionHostname_Type(DisplayString):
    """Custom type hm2DHCPServerPoolOptionHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hm2DHCPServerPoolOptionHostname_Type.__name__ = "DisplayString"
_Hm2DHCPServerPoolOptionHostname_Object = MibTableColumn
hm2DHCPServerPoolOptionHostname = _Hm2DHCPServerPoolOptionHostname_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 1, 5, 1, 35),
    _Hm2DHCPServerPoolOptionHostname_Type()
)
hm2DHCPServerPoolOptionHostname.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DHCPServerPoolOptionHostname.setStatus("current")


class _Hm2DHCPServerPoolMethod_Type(Integer32):
    """Custom type hm2DHCPServerPoolMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("config", 2),
          ("none", 1),
          ("ttdp", 3))
    )


_Hm2DHCPServerPoolMethod_Type.__name__ = "Integer32"
_Hm2DHCPServerPoolMethod_Object = MibTableColumn
hm2DHCPServerPoolMethod = _Hm2DHCPServerPoolMethod_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 1, 5, 1, 36),
    _Hm2DHCPServerPoolMethod_Type()
)
hm2DHCPServerPoolMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DHCPServerPoolMethod.setStatus("current")
_Hm2DHCPServerPoolErrorStatus_Type = Unsigned32
_Hm2DHCPServerPoolErrorStatus_Object = MibTableColumn
hm2DHCPServerPoolErrorStatus = _Hm2DHCPServerPoolErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 1, 5, 1, 99),
    _Hm2DHCPServerPoolErrorStatus_Type()
)
hm2DHCPServerPoolErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerPoolErrorStatus.setStatus("current")
_Hm2DHCPServerPoolRowStatus_Type = RowStatus
_Hm2DHCPServerPoolRowStatus_Object = MibTableColumn
hm2DHCPServerPoolRowStatus = _Hm2DHCPServerPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 1, 5, 1, 100),
    _Hm2DHCPServerPoolRowStatus_Type()
)
hm2DHCPServerPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2DHCPServerPoolRowStatus.setStatus("current")
_Hm2DHCPServerLeaseGroup_ObjectIdentity = ObjectIdentity
hm2DHCPServerLeaseGroup = _Hm2DHCPServerLeaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 2)
)
_Hm2DHCPServerLeaseTable_Object = MibTable
hm2DHCPServerLeaseTable = _Hm2DHCPServerLeaseTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hm2DHCPServerLeaseTable.setStatus("current")
_Hm2DHCPServerLeaseEntry_Object = MibTableRow
hm2DHCPServerLeaseEntry = _Hm2DHCPServerLeaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 2, 1, 1)
)
hm2DHCPServerLeaseEntry.setIndexNames(
    (0, "HM2-DHCPS-MIB", "hm2DHCPServerLeasePoolIndex"),
    (0, "HM2-DHCPS-MIB", "hm2DHCPServerLeaseIpAddress"),
)
if mibBuilder.loadTexts:
    hm2DHCPServerLeaseEntry.setStatus("current")


class _Hm2DHCPServerLeasePoolIndex_Type(Unsigned32):
    """Custom type hm2DHCPServerLeasePoolIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Hm2DHCPServerLeasePoolIndex_Type.__name__ = "Unsigned32"
_Hm2DHCPServerLeasePoolIndex_Object = MibTableColumn
hm2DHCPServerLeasePoolIndex = _Hm2DHCPServerLeasePoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 2, 1, 1, 1),
    _Hm2DHCPServerLeasePoolIndex_Type()
)
hm2DHCPServerLeasePoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerLeasePoolIndex.setStatus("current")
_Hm2DHCPServerLeaseIpAddress_Type = IpAddress
_Hm2DHCPServerLeaseIpAddress_Object = MibTableColumn
hm2DHCPServerLeaseIpAddress = _Hm2DHCPServerLeaseIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 2, 1, 1, 2),
    _Hm2DHCPServerLeaseIpAddress_Type()
)
hm2DHCPServerLeaseIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerLeaseIpAddress.setStatus("current")


class _Hm2DHCPServerLeaseState_Type(Integer32):
    """Custom type hm2DHCPServerLeaseState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 1),
          ("bound", 4),
          ("declined", 7),
          ("offering", 2),
          ("rebinding", 6),
          ("released", 8),
          ("renewing", 5),
          ("requesting", 3))
    )


_Hm2DHCPServerLeaseState_Type.__name__ = "Integer32"
_Hm2DHCPServerLeaseState_Object = MibTableColumn
hm2DHCPServerLeaseState = _Hm2DHCPServerLeaseState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 2, 1, 1, 3),
    _Hm2DHCPServerLeaseState_Type()
)
hm2DHCPServerLeaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerLeaseState.setStatus("current")
_Hm2DHCPServerLeaseTimeRemaining_Type = Unsigned32
_Hm2DHCPServerLeaseTimeRemaining_Object = MibTableColumn
hm2DHCPServerLeaseTimeRemaining = _Hm2DHCPServerLeaseTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 2, 1, 1, 4),
    _Hm2DHCPServerLeaseTimeRemaining_Type()
)
hm2DHCPServerLeaseTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerLeaseTimeRemaining.setStatus("current")
_Hm2DHCPServerLeaseIfIndex_Type = Integer32
_Hm2DHCPServerLeaseIfIndex_Object = MibTableColumn
hm2DHCPServerLeaseIfIndex = _Hm2DHCPServerLeaseIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 2, 1, 1, 5),
    _Hm2DHCPServerLeaseIfIndex_Type()
)
hm2DHCPServerLeaseIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerLeaseIfIndex.setStatus("current")
_Hm2DHCPServerLeaseClientMacAddress_Type = MacAddress
_Hm2DHCPServerLeaseClientMacAddress_Object = MibTableColumn
hm2DHCPServerLeaseClientMacAddress = _Hm2DHCPServerLeaseClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 2, 1, 1, 6),
    _Hm2DHCPServerLeaseClientMacAddress_Type()
)
hm2DHCPServerLeaseClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerLeaseClientMacAddress.setStatus("current")
_Hm2DHCPServerLeaseGateway_Type = IpAddress
_Hm2DHCPServerLeaseGateway_Object = MibTableColumn
hm2DHCPServerLeaseGateway = _Hm2DHCPServerLeaseGateway_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 2, 1, 1, 7),
    _Hm2DHCPServerLeaseGateway_Type()
)
hm2DHCPServerLeaseGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerLeaseGateway.setStatus("current")


class _Hm2DHCPServerLeaseClientId_Type(OctetString):
    """Custom type hm2DHCPServerLeaseClientId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hm2DHCPServerLeaseClientId_Type.__name__ = "OctetString"
_Hm2DHCPServerLeaseClientId_Object = MibTableColumn
hm2DHCPServerLeaseClientId = _Hm2DHCPServerLeaseClientId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 2, 1, 1, 8),
    _Hm2DHCPServerLeaseClientId_Type()
)
hm2DHCPServerLeaseClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerLeaseClientId.setStatus("current")


class _Hm2DHCPServerLeaseRemoteId_Type(OctetString):
    """Custom type hm2DHCPServerLeaseRemoteId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hm2DHCPServerLeaseRemoteId_Type.__name__ = "OctetString"
_Hm2DHCPServerLeaseRemoteId_Object = MibTableColumn
hm2DHCPServerLeaseRemoteId = _Hm2DHCPServerLeaseRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 2, 1, 1, 9),
    _Hm2DHCPServerLeaseRemoteId_Type()
)
hm2DHCPServerLeaseRemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerLeaseRemoteId.setStatus("current")


class _Hm2DHCPServerLeaseCircuitId_Type(OctetString):
    """Custom type hm2DHCPServerLeaseCircuitId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hm2DHCPServerLeaseCircuitId_Type.__name__ = "OctetString"
_Hm2DHCPServerLeaseCircuitId_Object = MibTableColumn
hm2DHCPServerLeaseCircuitId = _Hm2DHCPServerLeaseCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 2, 1, 1, 10),
    _Hm2DHCPServerLeaseCircuitId_Type()
)
hm2DHCPServerLeaseCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerLeaseCircuitId.setStatus("current")
_Hm2DHCPServerLeaseStartTime_Type = Unsigned32
_Hm2DHCPServerLeaseStartTime_Object = MibTableColumn
hm2DHCPServerLeaseStartTime = _Hm2DHCPServerLeaseStartTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 2, 1, 1, 11),
    _Hm2DHCPServerLeaseStartTime_Type()
)
hm2DHCPServerLeaseStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerLeaseStartTime.setStatus("current")


class _Hm2DHCPServerLeaseAction_Type(Integer32):
    """Custom type hm2DHCPServerLeaseAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("release", 2))
    )


_Hm2DHCPServerLeaseAction_Type.__name__ = "Integer32"
_Hm2DHCPServerLeaseAction_Object = MibTableColumn
hm2DHCPServerLeaseAction = _Hm2DHCPServerLeaseAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 2, 1, 1, 12),
    _Hm2DHCPServerLeaseAction_Type()
)
hm2DHCPServerLeaseAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DHCPServerLeaseAction.setStatus("current")
_Hm2DHCPServerLeaseVlanId_Type = Integer32
_Hm2DHCPServerLeaseVlanId_Object = MibTableColumn
hm2DHCPServerLeaseVlanId = _Hm2DHCPServerLeaseVlanId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 2, 1, 1, 13),
    _Hm2DHCPServerLeaseVlanId_Type()
)
hm2DHCPServerLeaseVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerLeaseVlanId.setStatus("current")
_Hm2DHCPServerInterfaceGroup_ObjectIdentity = ObjectIdentity
hm2DHCPServerInterfaceGroup = _Hm2DHCPServerInterfaceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 3)
)
_Hm2DHCPServerIfConfigTable_Object = MibTable
hm2DHCPServerIfConfigTable = _Hm2DHCPServerIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hm2DHCPServerIfConfigTable.setStatus("current")
_Hm2DHCPServerIfConfigEntry_Object = MibTableRow
hm2DHCPServerIfConfigEntry = _Hm2DHCPServerIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 3, 1, 1)
)
hm2DHCPServerIfConfigEntry.setIndexNames(
    (0, "HM2-DHCPS-MIB", "hm2DHCPServerIfConfigIndex"),
)
if mibBuilder.loadTexts:
    hm2DHCPServerIfConfigEntry.setStatus("current")
_Hm2DHCPServerIfConfigIndex_Type = InterfaceIndex
_Hm2DHCPServerIfConfigIndex_Object = MibTableColumn
hm2DHCPServerIfConfigIndex = _Hm2DHCPServerIfConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 3, 1, 1, 1),
    _Hm2DHCPServerIfConfigIndex_Type()
)
hm2DHCPServerIfConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerIfConfigIndex.setStatus("current")


class _Hm2DHCPServerIfConfigMode_Type(HmEnabledStatus):
    """Custom type hm2DHCPServerIfConfigMode based on HmEnabledStatus"""


_Hm2DHCPServerIfConfigMode_Object = MibTableColumn
hm2DHCPServerIfConfigMode = _Hm2DHCPServerIfConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 3, 1, 1, 2),
    _Hm2DHCPServerIfConfigMode_Type()
)
hm2DHCPServerIfConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2DHCPServerIfConfigMode.setStatus("current")
_Hm2DHCPServerCounterGroup_ObjectIdentity = ObjectIdentity
hm2DHCPServerCounterGroup = _Hm2DHCPServerCounterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 4)
)
_Hm2DHCPServerCounterIfTable_Object = MibTable
hm2DHCPServerCounterIfTable = _Hm2DHCPServerCounterIfTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hm2DHCPServerCounterIfTable.setStatus("current")
_Hm2DHCPServerCounterIfEntry_Object = MibTableRow
hm2DHCPServerCounterIfEntry = _Hm2DHCPServerCounterIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 4, 2, 1)
)
hm2DHCPServerCounterIfEntry.setIndexNames(
    (0, "HM2-DHCPS-MIB", "hm2DHCPServerCounterIfIndex"),
)
if mibBuilder.loadTexts:
    hm2DHCPServerCounterIfEntry.setStatus("current")
_Hm2DHCPServerCounterIfIndex_Type = InterfaceIndex
_Hm2DHCPServerCounterIfIndex_Object = MibTableColumn
hm2DHCPServerCounterIfIndex = _Hm2DHCPServerCounterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 4, 2, 1, 1),
    _Hm2DHCPServerCounterIfIndex_Type()
)
hm2DHCPServerCounterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerCounterIfIndex.setStatus("current")
_Hm2DHCPServerCounterBootpRequests_Type = Counter32
_Hm2DHCPServerCounterBootpRequests_Object = MibTableColumn
hm2DHCPServerCounterBootpRequests = _Hm2DHCPServerCounterBootpRequests_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 4, 2, 1, 2),
    _Hm2DHCPServerCounterBootpRequests_Type()
)
hm2DHCPServerCounterBootpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerCounterBootpRequests.setStatus("current")
_Hm2DHCPServerCounterBootpInvalids_Type = Counter32
_Hm2DHCPServerCounterBootpInvalids_Object = MibTableColumn
hm2DHCPServerCounterBootpInvalids = _Hm2DHCPServerCounterBootpInvalids_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 4, 2, 1, 3),
    _Hm2DHCPServerCounterBootpInvalids_Type()
)
hm2DHCPServerCounterBootpInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerCounterBootpInvalids.setStatus("current")
_Hm2DHCPServerCounterBootpReplies_Type = Counter32
_Hm2DHCPServerCounterBootpReplies_Object = MibTableColumn
hm2DHCPServerCounterBootpReplies = _Hm2DHCPServerCounterBootpReplies_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 4, 2, 1, 4),
    _Hm2DHCPServerCounterBootpReplies_Type()
)
hm2DHCPServerCounterBootpReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerCounterBootpReplies.setStatus("current")
_Hm2DHCPServerCounterBootpDroppedUnknownClients_Type = Counter32
_Hm2DHCPServerCounterBootpDroppedUnknownClients_Object = MibTableColumn
hm2DHCPServerCounterBootpDroppedUnknownClients = _Hm2DHCPServerCounterBootpDroppedUnknownClients_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 4, 2, 1, 5),
    _Hm2DHCPServerCounterBootpDroppedUnknownClients_Type()
)
hm2DHCPServerCounterBootpDroppedUnknownClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerCounterBootpDroppedUnknownClients.setStatus("current")
_Hm2DHCPServerCounterBootpDroppedNotServingSubnet_Type = Counter32
_Hm2DHCPServerCounterBootpDroppedNotServingSubnet_Object = MibTableColumn
hm2DHCPServerCounterBootpDroppedNotServingSubnet = _Hm2DHCPServerCounterBootpDroppedNotServingSubnet_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 4, 2, 1, 6),
    _Hm2DHCPServerCounterBootpDroppedNotServingSubnet_Type()
)
hm2DHCPServerCounterBootpDroppedNotServingSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerCounterBootpDroppedNotServingSubnet.setStatus("current")
_Hm2DHCPServerCounterDhcpv4Discovers_Type = Counter32
_Hm2DHCPServerCounterDhcpv4Discovers_Object = MibTableColumn
hm2DHCPServerCounterDhcpv4Discovers = _Hm2DHCPServerCounterDhcpv4Discovers_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 4, 2, 1, 20),
    _Hm2DHCPServerCounterDhcpv4Discovers_Type()
)
hm2DHCPServerCounterDhcpv4Discovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerCounterDhcpv4Discovers.setStatus("current")
_Hm2DHCPServerCounterDhcpv4Offers_Type = Counter32
_Hm2DHCPServerCounterDhcpv4Offers_Object = MibTableColumn
hm2DHCPServerCounterDhcpv4Offers = _Hm2DHCPServerCounterDhcpv4Offers_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 4, 2, 1, 21),
    _Hm2DHCPServerCounterDhcpv4Offers_Type()
)
hm2DHCPServerCounterDhcpv4Offers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerCounterDhcpv4Offers.setStatus("current")
_Hm2DHCPServerCounterDhcpv4Requests_Type = Counter32
_Hm2DHCPServerCounterDhcpv4Requests_Object = MibTableColumn
hm2DHCPServerCounterDhcpv4Requests = _Hm2DHCPServerCounterDhcpv4Requests_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 4, 2, 1, 22),
    _Hm2DHCPServerCounterDhcpv4Requests_Type()
)
hm2DHCPServerCounterDhcpv4Requests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerCounterDhcpv4Requests.setStatus("current")
_Hm2DHCPServerCounterDhcpv4Declines_Type = Counter32
_Hm2DHCPServerCounterDhcpv4Declines_Object = MibTableColumn
hm2DHCPServerCounterDhcpv4Declines = _Hm2DHCPServerCounterDhcpv4Declines_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 4, 2, 1, 23),
    _Hm2DHCPServerCounterDhcpv4Declines_Type()
)
hm2DHCPServerCounterDhcpv4Declines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerCounterDhcpv4Declines.setStatus("current")
_Hm2DHCPServerCounterDhcpv4Acks_Type = Counter32
_Hm2DHCPServerCounterDhcpv4Acks_Object = MibTableColumn
hm2DHCPServerCounterDhcpv4Acks = _Hm2DHCPServerCounterDhcpv4Acks_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 4, 2, 1, 24),
    _Hm2DHCPServerCounterDhcpv4Acks_Type()
)
hm2DHCPServerCounterDhcpv4Acks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerCounterDhcpv4Acks.setStatus("current")
_Hm2DHCPServerCounterDhcpv4Naks_Type = Counter32
_Hm2DHCPServerCounterDhcpv4Naks_Object = MibTableColumn
hm2DHCPServerCounterDhcpv4Naks = _Hm2DHCPServerCounterDhcpv4Naks_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 4, 2, 1, 25),
    _Hm2DHCPServerCounterDhcpv4Naks_Type()
)
hm2DHCPServerCounterDhcpv4Naks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerCounterDhcpv4Naks.setStatus("current")
_Hm2DHCPServerCounterDhcpv4Releases_Type = Counter32
_Hm2DHCPServerCounterDhcpv4Releases_Object = MibTableColumn
hm2DHCPServerCounterDhcpv4Releases = _Hm2DHCPServerCounterDhcpv4Releases_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 4, 2, 1, 26),
    _Hm2DHCPServerCounterDhcpv4Releases_Type()
)
hm2DHCPServerCounterDhcpv4Releases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerCounterDhcpv4Releases.setStatus("current")
_Hm2DHCPServerCounterDhcpv4Informs_Type = Counter32
_Hm2DHCPServerCounterDhcpv4Informs_Object = MibTableColumn
hm2DHCPServerCounterDhcpv4Informs = _Hm2DHCPServerCounterDhcpv4Informs_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 4, 2, 1, 27),
    _Hm2DHCPServerCounterDhcpv4Informs_Type()
)
hm2DHCPServerCounterDhcpv4Informs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerCounterDhcpv4Informs.setStatus("current")
_Hm2DHCPServerCounterDhcpv4ForcedRenews_Type = Counter32
_Hm2DHCPServerCounterDhcpv4ForcedRenews_Object = MibTableColumn
hm2DHCPServerCounterDhcpv4ForcedRenews = _Hm2DHCPServerCounterDhcpv4ForcedRenews_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 4, 2, 1, 28),
    _Hm2DHCPServerCounterDhcpv4ForcedRenews_Type()
)
hm2DHCPServerCounterDhcpv4ForcedRenews.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerCounterDhcpv4ForcedRenews.setStatus("current")
_Hm2DHCPServerCounterDhcpv4Invalids_Type = Counter32
_Hm2DHCPServerCounterDhcpv4Invalids_Object = MibTableColumn
hm2DHCPServerCounterDhcpv4Invalids = _Hm2DHCPServerCounterDhcpv4Invalids_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 4, 2, 1, 29),
    _Hm2DHCPServerCounterDhcpv4Invalids_Type()
)
hm2DHCPServerCounterDhcpv4Invalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerCounterDhcpv4Invalids.setStatus("current")
_Hm2DHCPServerCounterDhcpv4DroppedUnknownClient_Type = Counter32
_Hm2DHCPServerCounterDhcpv4DroppedUnknownClient_Object = MibTableColumn
hm2DHCPServerCounterDhcpv4DroppedUnknownClient = _Hm2DHCPServerCounterDhcpv4DroppedUnknownClient_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 4, 2, 1, 30),
    _Hm2DHCPServerCounterDhcpv4DroppedUnknownClient_Type()
)
hm2DHCPServerCounterDhcpv4DroppedUnknownClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerCounterDhcpv4DroppedUnknownClient.setStatus("current")
_Hm2DHCPServerCounterDhcpv4DroppedNotServingSubnet_Type = Counter32
_Hm2DHCPServerCounterDhcpv4DroppedNotServingSubnet_Object = MibTableColumn
hm2DHCPServerCounterDhcpv4DroppedNotServingSubnet = _Hm2DHCPServerCounterDhcpv4DroppedNotServingSubnet_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 4, 2, 1, 31),
    _Hm2DHCPServerCounterDhcpv4DroppedNotServingSubnet_Type()
)
hm2DHCPServerCounterDhcpv4DroppedNotServingSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerCounterDhcpv4DroppedNotServingSubnet.setStatus("current")
_Hm2DHCPServerCounterMiscOtherDhcpServer_Type = Counter32
_Hm2DHCPServerCounterMiscOtherDhcpServer_Object = MibTableColumn
hm2DHCPServerCounterMiscOtherDhcpServer = _Hm2DHCPServerCounterMiscOtherDhcpServer_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 1, 1, 4, 2, 1, 40),
    _Hm2DHCPServerCounterMiscOtherDhcpServer_Type()
)
hm2DHCPServerCounterMiscOtherDhcpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2DHCPServerCounterMiscOtherDhcpServer.setStatus("current")
_Hm2DHCPServerSNMPExtensionGroup_ObjectIdentity = ObjectIdentity
hm2DHCPServerSNMPExtensionGroup = _Hm2DHCPServerSNMPExtensionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 3)
)
_Hm2DHCPServerRowStatusInvalidConfigurationErrorReturn_ObjectIdentity = ObjectIdentity
hm2DHCPServerRowStatusInvalidConfigurationErrorReturn = _Hm2DHCPServerRowStatusInvalidConfigurationErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 3, 1)
)
if mibBuilder.loadTexts:
    hm2DHCPServerRowStatusInvalidConfigurationErrorReturn.setStatus("current")
_Hm2DHCPServerConflictDHCPRrelayErrorReturn_ObjectIdentity = ObjectIdentity
hm2DHCPServerConflictDHCPRrelayErrorReturn = _Hm2DHCPServerConflictDHCPRrelayErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 91, 3, 2)
)
if mibBuilder.loadTexts:
    hm2DHCPServerConflictDHCPRrelayErrorReturn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-DHCPS-MIB",
    **{"hm2DhcpsMib": hm2DhcpsMib,
       "hm2DHCPServerMibNotifications": hm2DHCPServerMibNotifications,
       "hm2DHCPServerMibObjects": hm2DHCPServerMibObjects,
       "hm2DHCPServerGroup": hm2DHCPServerGroup,
       "hm2DHCPServerConfigGroup": hm2DHCPServerConfigGroup,
       "hm2DHCPServerMode": hm2DHCPServerMode,
       "hm2DHCPServerMaxPoolEntries": hm2DHCPServerMaxPoolEntries,
       "hm2DHCPServerMaxLeaseEntries": hm2DHCPServerMaxLeaseEntries,
       "hm2DHCPServerPoolTable": hm2DHCPServerPoolTable,
       "hm2DHCPServerPoolEntry": hm2DHCPServerPoolEntry,
       "hm2DHCPServerPoolIndex": hm2DHCPServerPoolIndex,
       "hm2DHCPServerPoolStartIpAddress": hm2DHCPServerPoolStartIpAddress,
       "hm2DHCPServerPoolEndIpAddress": hm2DHCPServerPoolEndIpAddress,
       "hm2DHCPServerPoolLeaseTime": hm2DHCPServerPoolLeaseTime,
       "hm2DHCPServerPoolFlags": hm2DHCPServerPoolFlags,
       "hm2DHCPServerPoolIfIndex": hm2DHCPServerPoolIfIndex,
       "hm2DHCPServerPoolMacAddress": hm2DHCPServerPoolMacAddress,
       "hm2DHCPServerPoolGateway": hm2DHCPServerPoolGateway,
       "hm2DHCPServerPoolClientId": hm2DHCPServerPoolClientId,
       "hm2DHCPServerPoolRemoteId": hm2DHCPServerPoolRemoteId,
       "hm2DHCPServerPoolCircuitId": hm2DHCPServerPoolCircuitId,
       "hm2DHCPServerPoolHirschmannClient": hm2DHCPServerPoolHirschmannClient,
       "hm2DHCPServerPoolVlanId": hm2DHCPServerPoolVlanId,
       "hm2DHCPServerPoolOptionConfFileName": hm2DHCPServerPoolOptionConfFileName,
       "hm2DHCPServerPoolOptionGateway": hm2DHCPServerPoolOptionGateway,
       "hm2DHCPServerPoolOptionNetmask": hm2DHCPServerPoolOptionNetmask,
       "hm2DHCPServerPoolOptionWINS": hm2DHCPServerPoolOptionWINS,
       "hm2DHCPServerPoolOptionDNS": hm2DHCPServerPoolOptionDNS,
       "hm2DHCPServerPoolOptionHostname": hm2DHCPServerPoolOptionHostname,
       "hm2DHCPServerPoolMethod": hm2DHCPServerPoolMethod,
       "hm2DHCPServerPoolErrorStatus": hm2DHCPServerPoolErrorStatus,
       "hm2DHCPServerPoolRowStatus": hm2DHCPServerPoolRowStatus,
       "hm2DHCPServerLeaseGroup": hm2DHCPServerLeaseGroup,
       "hm2DHCPServerLeaseTable": hm2DHCPServerLeaseTable,
       "hm2DHCPServerLeaseEntry": hm2DHCPServerLeaseEntry,
       "hm2DHCPServerLeasePoolIndex": hm2DHCPServerLeasePoolIndex,
       "hm2DHCPServerLeaseIpAddress": hm2DHCPServerLeaseIpAddress,
       "hm2DHCPServerLeaseState": hm2DHCPServerLeaseState,
       "hm2DHCPServerLeaseTimeRemaining": hm2DHCPServerLeaseTimeRemaining,
       "hm2DHCPServerLeaseIfIndex": hm2DHCPServerLeaseIfIndex,
       "hm2DHCPServerLeaseClientMacAddress": hm2DHCPServerLeaseClientMacAddress,
       "hm2DHCPServerLeaseGateway": hm2DHCPServerLeaseGateway,
       "hm2DHCPServerLeaseClientId": hm2DHCPServerLeaseClientId,
       "hm2DHCPServerLeaseRemoteId": hm2DHCPServerLeaseRemoteId,
       "hm2DHCPServerLeaseCircuitId": hm2DHCPServerLeaseCircuitId,
       "hm2DHCPServerLeaseStartTime": hm2DHCPServerLeaseStartTime,
       "hm2DHCPServerLeaseAction": hm2DHCPServerLeaseAction,
       "hm2DHCPServerLeaseVlanId": hm2DHCPServerLeaseVlanId,
       "hm2DHCPServerInterfaceGroup": hm2DHCPServerInterfaceGroup,
       "hm2DHCPServerIfConfigTable": hm2DHCPServerIfConfigTable,
       "hm2DHCPServerIfConfigEntry": hm2DHCPServerIfConfigEntry,
       "hm2DHCPServerIfConfigIndex": hm2DHCPServerIfConfigIndex,
       "hm2DHCPServerIfConfigMode": hm2DHCPServerIfConfigMode,
       "hm2DHCPServerCounterGroup": hm2DHCPServerCounterGroup,
       "hm2DHCPServerCounterIfTable": hm2DHCPServerCounterIfTable,
       "hm2DHCPServerCounterIfEntry": hm2DHCPServerCounterIfEntry,
       "hm2DHCPServerCounterIfIndex": hm2DHCPServerCounterIfIndex,
       "hm2DHCPServerCounterBootpRequests": hm2DHCPServerCounterBootpRequests,
       "hm2DHCPServerCounterBootpInvalids": hm2DHCPServerCounterBootpInvalids,
       "hm2DHCPServerCounterBootpReplies": hm2DHCPServerCounterBootpReplies,
       "hm2DHCPServerCounterBootpDroppedUnknownClients": hm2DHCPServerCounterBootpDroppedUnknownClients,
       "hm2DHCPServerCounterBootpDroppedNotServingSubnet": hm2DHCPServerCounterBootpDroppedNotServingSubnet,
       "hm2DHCPServerCounterDhcpv4Discovers": hm2DHCPServerCounterDhcpv4Discovers,
       "hm2DHCPServerCounterDhcpv4Offers": hm2DHCPServerCounterDhcpv4Offers,
       "hm2DHCPServerCounterDhcpv4Requests": hm2DHCPServerCounterDhcpv4Requests,
       "hm2DHCPServerCounterDhcpv4Declines": hm2DHCPServerCounterDhcpv4Declines,
       "hm2DHCPServerCounterDhcpv4Acks": hm2DHCPServerCounterDhcpv4Acks,
       "hm2DHCPServerCounterDhcpv4Naks": hm2DHCPServerCounterDhcpv4Naks,
       "hm2DHCPServerCounterDhcpv4Releases": hm2DHCPServerCounterDhcpv4Releases,
       "hm2DHCPServerCounterDhcpv4Informs": hm2DHCPServerCounterDhcpv4Informs,
       "hm2DHCPServerCounterDhcpv4ForcedRenews": hm2DHCPServerCounterDhcpv4ForcedRenews,
       "hm2DHCPServerCounterDhcpv4Invalids": hm2DHCPServerCounterDhcpv4Invalids,
       "hm2DHCPServerCounterDhcpv4DroppedUnknownClient": hm2DHCPServerCounterDhcpv4DroppedUnknownClient,
       "hm2DHCPServerCounterDhcpv4DroppedNotServingSubnet": hm2DHCPServerCounterDhcpv4DroppedNotServingSubnet,
       "hm2DHCPServerCounterMiscOtherDhcpServer": hm2DHCPServerCounterMiscOtherDhcpServer,
       "hm2DHCPServerSNMPExtensionGroup": hm2DHCPServerSNMPExtensionGroup,
       "hm2DHCPServerRowStatusInvalidConfigurationErrorReturn": hm2DHCPServerRowStatusInvalidConfigurationErrorReturn,
       "hm2DHCPServerConflictDHCPRrelayErrorReturn": hm2DHCPServerConflictDHCPRrelayErrorReturn}
)
