# SNMP MIB module (HMDHCPS-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HMDHCPS-SNMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:37 2024
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

(hmConfiguration,) = mibBuilder.importSymbols(
    "HMPRIV-MGMT-SNMP-MIB",
    "hmConfiguration")

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

hmDhcps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 16)
)
hmDhcps.setRevisions(
        ("2013-04-18 12:00",
         "2011-12-20 12:00",
         "2007-10-16 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HmDHCPServerGroup_ObjectIdentity = ObjectIdentity
hmDHCPServerGroup = _HmDHCPServerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1)
)
_HmDHCPServerConfigGroup_ObjectIdentity = ObjectIdentity
hmDHCPServerConfigGroup = _HmDHCPServerConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1)
)


class _HmDHCPServerMode_Type(Integer32):
    """Custom type hmDHCPServerMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HmDHCPServerMode_Type.__name__ = "Integer32"
_HmDHCPServerMode_Object = MibScalar
hmDHCPServerMode = _HmDHCPServerMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 1),
    _HmDHCPServerMode_Type()
)
hmDHCPServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmDHCPServerMode.setStatus("current")
_HmDHCPServerMaxPoolEntries_Type = Unsigned32
_HmDHCPServerMaxPoolEntries_Object = MibScalar
hmDHCPServerMaxPoolEntries = _HmDHCPServerMaxPoolEntries_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 2),
    _HmDHCPServerMaxPoolEntries_Type()
)
hmDHCPServerMaxPoolEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerMaxPoolEntries.setStatus("current")
_HmDHCPServerMaxLeaseEntries_Type = Unsigned32
_HmDHCPServerMaxLeaseEntries_Object = MibScalar
hmDHCPServerMaxLeaseEntries = _HmDHCPServerMaxLeaseEntries_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 3),
    _HmDHCPServerMaxLeaseEntries_Type()
)
hmDHCPServerMaxLeaseEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerMaxLeaseEntries.setStatus("current")


class _HmDHCPServerAddrProbe_Type(Integer32):
    """Custom type hmDHCPServerAddrProbe based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HmDHCPServerAddrProbe_Type.__name__ = "Integer32"
_HmDHCPServerAddrProbe_Object = MibScalar
hmDHCPServerAddrProbe = _HmDHCPServerAddrProbe_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 4),
    _HmDHCPServerAddrProbe_Type()
)
hmDHCPServerAddrProbe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmDHCPServerAddrProbe.setStatus("current")
_HmDHCPServerPoolTable_Object = MibTable
hmDHCPServerPoolTable = _HmDHCPServerPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hmDHCPServerPoolTable.setStatus("current")
_HmDHCPServerPoolEntry_Object = MibTableRow
hmDHCPServerPoolEntry = _HmDHCPServerPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1)
)
hmDHCPServerPoolEntry.setIndexNames(
    (0, "HMDHCPS-SNMP-MIB", "hmDHCPServerPoolIndex"),
)
if mibBuilder.loadTexts:
    hmDHCPServerPoolEntry.setStatus("current")
_HmDHCPServerPoolIndex_Type = Unsigned32
_HmDHCPServerPoolIndex_Object = MibTableColumn
hmDHCPServerPoolIndex = _HmDHCPServerPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 1),
    _HmDHCPServerPoolIndex_Type()
)
hmDHCPServerPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerPoolIndex.setStatus("current")
_HmDHCPServerPoolStartIpAddress_Type = IpAddress
_HmDHCPServerPoolStartIpAddress_Object = MibTableColumn
hmDHCPServerPoolStartIpAddress = _HmDHCPServerPoolStartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 2),
    _HmDHCPServerPoolStartIpAddress_Type()
)
hmDHCPServerPoolStartIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmDHCPServerPoolStartIpAddress.setStatus("current")
_HmDHCPServerPoolEndIpAddress_Type = IpAddress
_HmDHCPServerPoolEndIpAddress_Object = MibTableColumn
hmDHCPServerPoolEndIpAddress = _HmDHCPServerPoolEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 3),
    _HmDHCPServerPoolEndIpAddress_Type()
)
hmDHCPServerPoolEndIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmDHCPServerPoolEndIpAddress.setStatus("current")


class _HmDHCPServerPoolLeaseTime_Type(Unsigned32):
    """Custom type hmDHCPServerPoolLeaseTime based on Unsigned32"""
    defaultValue = 86400


_HmDHCPServerPoolLeaseTime_Object = MibTableColumn
hmDHCPServerPoolLeaseTime = _HmDHCPServerPoolLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 4),
    _HmDHCPServerPoolLeaseTime_Type()
)
hmDHCPServerPoolLeaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmDHCPServerPoolLeaseTime.setStatus("current")


class _HmDHCPServerPoolFlags_Type(Bits):
    """Custom type hmDHCPServerPoolFlags based on Bits"""
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

_HmDHCPServerPoolFlags_Type.__name__ = "Bits"
_HmDHCPServerPoolFlags_Object = MibTableColumn
hmDHCPServerPoolFlags = _HmDHCPServerPoolFlags_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 5),
    _HmDHCPServerPoolFlags_Type()
)
hmDHCPServerPoolFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmDHCPServerPoolFlags.setStatus("current")
_HmDHCPServerPoolIfIndex_Type = Integer32
_HmDHCPServerPoolIfIndex_Object = MibTableColumn
hmDHCPServerPoolIfIndex = _HmDHCPServerPoolIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 6),
    _HmDHCPServerPoolIfIndex_Type()
)
hmDHCPServerPoolIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmDHCPServerPoolIfIndex.setStatus("current")
_HmDHCPServerPoolMacAddress_Type = MacAddress
_HmDHCPServerPoolMacAddress_Object = MibTableColumn
hmDHCPServerPoolMacAddress = _HmDHCPServerPoolMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 7),
    _HmDHCPServerPoolMacAddress_Type()
)
hmDHCPServerPoolMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmDHCPServerPoolMacAddress.setStatus("current")
_HmDHCPServerPoolGateway_Type = IpAddress
_HmDHCPServerPoolGateway_Object = MibTableColumn
hmDHCPServerPoolGateway = _HmDHCPServerPoolGateway_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 8),
    _HmDHCPServerPoolGateway_Type()
)
hmDHCPServerPoolGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmDHCPServerPoolGateway.setStatus("current")
_HmDHCPServerPoolClientId_Type = OctetString
_HmDHCPServerPoolClientId_Object = MibTableColumn
hmDHCPServerPoolClientId = _HmDHCPServerPoolClientId_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 9),
    _HmDHCPServerPoolClientId_Type()
)
hmDHCPServerPoolClientId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmDHCPServerPoolClientId.setStatus("current")
_HmDHCPServerPoolRemoteId_Type = OctetString
_HmDHCPServerPoolRemoteId_Object = MibTableColumn
hmDHCPServerPoolRemoteId = _HmDHCPServerPoolRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 10),
    _HmDHCPServerPoolRemoteId_Type()
)
hmDHCPServerPoolRemoteId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmDHCPServerPoolRemoteId.setStatus("current")
_HmDHCPServerPoolCircuitId_Type = OctetString
_HmDHCPServerPoolCircuitId_Object = MibTableColumn
hmDHCPServerPoolCircuitId = _HmDHCPServerPoolCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 11),
    _HmDHCPServerPoolCircuitId_Type()
)
hmDHCPServerPoolCircuitId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmDHCPServerPoolCircuitId.setStatus("current")


class _HmDHCPServerPoolHirschmannClient_Type(Integer32):
    """Custom type hmDHCPServerPoolHirschmannClient based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HmDHCPServerPoolHirschmannClient_Type.__name__ = "Integer32"
_HmDHCPServerPoolHirschmannClient_Object = MibTableColumn
hmDHCPServerPoolHirschmannClient = _HmDHCPServerPoolHirschmannClient_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 12),
    _HmDHCPServerPoolHirschmannClient_Type()
)
hmDHCPServerPoolHirschmannClient.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmDHCPServerPoolHirschmannClient.setStatus("current")
_HmDHCPServerPoolVlanId_Type = Integer32
_HmDHCPServerPoolVlanId_Object = MibTableColumn
hmDHCPServerPoolVlanId = _HmDHCPServerPoolVlanId_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 13),
    _HmDHCPServerPoolVlanId_Type()
)
hmDHCPServerPoolVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmDHCPServerPoolVlanId.setStatus("current")


class _HmDHCPServerPoolOptionConfFileName_Type(DisplayString):
    """Custom type hmDHCPServerPoolOptionConfFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_HmDHCPServerPoolOptionConfFileName_Type.__name__ = "DisplayString"
_HmDHCPServerPoolOptionConfFileName_Object = MibTableColumn
hmDHCPServerPoolOptionConfFileName = _HmDHCPServerPoolOptionConfFileName_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 30),
    _HmDHCPServerPoolOptionConfFileName_Type()
)
hmDHCPServerPoolOptionConfFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmDHCPServerPoolOptionConfFileName.setStatus("current")
_HmDHCPServerPoolOptionGateway_Type = IpAddress
_HmDHCPServerPoolOptionGateway_Object = MibTableColumn
hmDHCPServerPoolOptionGateway = _HmDHCPServerPoolOptionGateway_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 31),
    _HmDHCPServerPoolOptionGateway_Type()
)
hmDHCPServerPoolOptionGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmDHCPServerPoolOptionGateway.setStatus("current")
_HmDHCPServerPoolOptionNetmask_Type = IpAddress
_HmDHCPServerPoolOptionNetmask_Object = MibTableColumn
hmDHCPServerPoolOptionNetmask = _HmDHCPServerPoolOptionNetmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 32),
    _HmDHCPServerPoolOptionNetmask_Type()
)
hmDHCPServerPoolOptionNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmDHCPServerPoolOptionNetmask.setStatus("current")
_HmDHCPServerPoolOptionWINS_Type = IpAddress
_HmDHCPServerPoolOptionWINS_Object = MibTableColumn
hmDHCPServerPoolOptionWINS = _HmDHCPServerPoolOptionWINS_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 33),
    _HmDHCPServerPoolOptionWINS_Type()
)
hmDHCPServerPoolOptionWINS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmDHCPServerPoolOptionWINS.setStatus("current")
_HmDHCPServerPoolOptionDNS_Type = IpAddress
_HmDHCPServerPoolOptionDNS_Object = MibTableColumn
hmDHCPServerPoolOptionDNS = _HmDHCPServerPoolOptionDNS_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 34),
    _HmDHCPServerPoolOptionDNS_Type()
)
hmDHCPServerPoolOptionDNS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmDHCPServerPoolOptionDNS.setStatus("current")
_HmDHCPServerPoolOptionHostname_Type = DisplayString
_HmDHCPServerPoolOptionHostname_Object = MibTableColumn
hmDHCPServerPoolOptionHostname = _HmDHCPServerPoolOptionHostname_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 35),
    _HmDHCPServerPoolOptionHostname_Type()
)
hmDHCPServerPoolOptionHostname.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmDHCPServerPoolOptionHostname.setStatus("current")


class _HmDHCPServerPoolOptionVendor_Type(OctetString):
    """Custom type hmDHCPServerPoolOptionVendor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HmDHCPServerPoolOptionVendor_Type.__name__ = "OctetString"
_HmDHCPServerPoolOptionVendor_Object = MibTableColumn
hmDHCPServerPoolOptionVendor = _HmDHCPServerPoolOptionVendor_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 36),
    _HmDHCPServerPoolOptionVendor_Type()
)
hmDHCPServerPoolOptionVendor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmDHCPServerPoolOptionVendor.setStatus("current")
_HmDHCPServerPoolErrorStatus_Type = Unsigned32
_HmDHCPServerPoolErrorStatus_Object = MibTableColumn
hmDHCPServerPoolErrorStatus = _HmDHCPServerPoolErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 99),
    _HmDHCPServerPoolErrorStatus_Type()
)
hmDHCPServerPoolErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerPoolErrorStatus.setStatus("current")
_HmDHCPServerPoolRowStatus_Type = RowStatus
_HmDHCPServerPoolRowStatus_Object = MibTableColumn
hmDHCPServerPoolRowStatus = _HmDHCPServerPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 1, 5, 1, 100),
    _HmDHCPServerPoolRowStatus_Type()
)
hmDHCPServerPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hmDHCPServerPoolRowStatus.setStatus("current")
_HmDHCPServerLeaseGroup_ObjectIdentity = ObjectIdentity
hmDHCPServerLeaseGroup = _HmDHCPServerLeaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2)
)
_HmDHCPServerLeaseTable_Object = MibTable
hmDHCPServerLeaseTable = _HmDHCPServerLeaseTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hmDHCPServerLeaseTable.setStatus("current")
_HmDHCPServerLeaseEntry_Object = MibTableRow
hmDHCPServerLeaseEntry = _HmDHCPServerLeaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2, 1, 1)
)
hmDHCPServerLeaseEntry.setIndexNames(
    (0, "HMDHCPS-SNMP-MIB", "hmDHCPServerLeasePoolIndex"),
    (0, "HMDHCPS-SNMP-MIB", "hmDHCPServerLeaseIpAddress"),
)
if mibBuilder.loadTexts:
    hmDHCPServerLeaseEntry.setStatus("current")
_HmDHCPServerLeasePoolIndex_Type = Unsigned32
_HmDHCPServerLeasePoolIndex_Object = MibTableColumn
hmDHCPServerLeasePoolIndex = _HmDHCPServerLeasePoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2, 1, 1, 1),
    _HmDHCPServerLeasePoolIndex_Type()
)
hmDHCPServerLeasePoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerLeasePoolIndex.setStatus("current")
_HmDHCPServerLeaseIpAddress_Type = IpAddress
_HmDHCPServerLeaseIpAddress_Object = MibTableColumn
hmDHCPServerLeaseIpAddress = _HmDHCPServerLeaseIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2, 1, 1, 2),
    _HmDHCPServerLeaseIpAddress_Type()
)
hmDHCPServerLeaseIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerLeaseIpAddress.setStatus("current")


class _HmDHCPServerLeaseState_Type(Integer32):
    """Custom type hmDHCPServerLeaseState based on Integer32"""
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


_HmDHCPServerLeaseState_Type.__name__ = "Integer32"
_HmDHCPServerLeaseState_Object = MibTableColumn
hmDHCPServerLeaseState = _HmDHCPServerLeaseState_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2, 1, 1, 3),
    _HmDHCPServerLeaseState_Type()
)
hmDHCPServerLeaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerLeaseState.setStatus("current")
_HmDHCPServerLeaseTimeRemaining_Type = Unsigned32
_HmDHCPServerLeaseTimeRemaining_Object = MibTableColumn
hmDHCPServerLeaseTimeRemaining = _HmDHCPServerLeaseTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2, 1, 1, 4),
    _HmDHCPServerLeaseTimeRemaining_Type()
)
hmDHCPServerLeaseTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerLeaseTimeRemaining.setStatus("current")
_HmDHCPServerLeaseIfIndex_Type = Integer32
_HmDHCPServerLeaseIfIndex_Object = MibTableColumn
hmDHCPServerLeaseIfIndex = _HmDHCPServerLeaseIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2, 1, 1, 5),
    _HmDHCPServerLeaseIfIndex_Type()
)
hmDHCPServerLeaseIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerLeaseIfIndex.setStatus("current")
_HmDHCPServerLeaseClientMacAddress_Type = MacAddress
_HmDHCPServerLeaseClientMacAddress_Object = MibTableColumn
hmDHCPServerLeaseClientMacAddress = _HmDHCPServerLeaseClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2, 1, 1, 6),
    _HmDHCPServerLeaseClientMacAddress_Type()
)
hmDHCPServerLeaseClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerLeaseClientMacAddress.setStatus("current")
_HmDHCPServerLeaseGateway_Type = IpAddress
_HmDHCPServerLeaseGateway_Object = MibTableColumn
hmDHCPServerLeaseGateway = _HmDHCPServerLeaseGateway_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2, 1, 1, 7),
    _HmDHCPServerLeaseGateway_Type()
)
hmDHCPServerLeaseGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerLeaseGateway.setStatus("current")


class _HmDHCPServerLeaseClientId_Type(OctetString):
    """Custom type hmDHCPServerLeaseClientId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HmDHCPServerLeaseClientId_Type.__name__ = "OctetString"
_HmDHCPServerLeaseClientId_Object = MibTableColumn
hmDHCPServerLeaseClientId = _HmDHCPServerLeaseClientId_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2, 1, 1, 8),
    _HmDHCPServerLeaseClientId_Type()
)
hmDHCPServerLeaseClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerLeaseClientId.setStatus("current")


class _HmDHCPServerLeaseRemoteId_Type(OctetString):
    """Custom type hmDHCPServerLeaseRemoteId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HmDHCPServerLeaseRemoteId_Type.__name__ = "OctetString"
_HmDHCPServerLeaseRemoteId_Object = MibTableColumn
hmDHCPServerLeaseRemoteId = _HmDHCPServerLeaseRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2, 1, 1, 9),
    _HmDHCPServerLeaseRemoteId_Type()
)
hmDHCPServerLeaseRemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerLeaseRemoteId.setStatus("current")


class _HmDHCPServerLeaseCircuitId_Type(OctetString):
    """Custom type hmDHCPServerLeaseCircuitId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HmDHCPServerLeaseCircuitId_Type.__name__ = "OctetString"
_HmDHCPServerLeaseCircuitId_Object = MibTableColumn
hmDHCPServerLeaseCircuitId = _HmDHCPServerLeaseCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2, 1, 1, 10),
    _HmDHCPServerLeaseCircuitId_Type()
)
hmDHCPServerLeaseCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerLeaseCircuitId.setStatus("current")
_HmDHCPServerLeaseStartTime_Type = Unsigned32
_HmDHCPServerLeaseStartTime_Object = MibTableColumn
hmDHCPServerLeaseStartTime = _HmDHCPServerLeaseStartTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2, 1, 1, 11),
    _HmDHCPServerLeaseStartTime_Type()
)
hmDHCPServerLeaseStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerLeaseStartTime.setStatus("current")


class _HmDHCPServerLeaseAction_Type(Integer32):
    """Custom type hmDHCPServerLeaseAction based on Integer32"""
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


_HmDHCPServerLeaseAction_Type.__name__ = "Integer32"
_HmDHCPServerLeaseAction_Object = MibTableColumn
hmDHCPServerLeaseAction = _HmDHCPServerLeaseAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2, 1, 1, 12),
    _HmDHCPServerLeaseAction_Type()
)
hmDHCPServerLeaseAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmDHCPServerLeaseAction.setStatus("current")
_HmDHCPServerLeaseVlanId_Type = Integer32
_HmDHCPServerLeaseVlanId_Object = MibTableColumn
hmDHCPServerLeaseVlanId = _HmDHCPServerLeaseVlanId_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 2, 1, 1, 13),
    _HmDHCPServerLeaseVlanId_Type()
)
hmDHCPServerLeaseVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerLeaseVlanId.setStatus("current")
_HmDHCPServerInterfaceGroup_ObjectIdentity = ObjectIdentity
hmDHCPServerInterfaceGroup = _HmDHCPServerInterfaceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 3)
)
_HmDHCPServerIfConfigTable_Object = MibTable
hmDHCPServerIfConfigTable = _HmDHCPServerIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hmDHCPServerIfConfigTable.setStatus("current")
_HmDHCPServerIfConfigEntry_Object = MibTableRow
hmDHCPServerIfConfigEntry = _HmDHCPServerIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 3, 1, 1)
)
hmDHCPServerIfConfigEntry.setIndexNames(
    (0, "HMDHCPS-SNMP-MIB", "hmDHCPServerIfConfigIndex"),
)
if mibBuilder.loadTexts:
    hmDHCPServerIfConfigEntry.setStatus("current")
_HmDHCPServerIfConfigIndex_Type = Integer32
_HmDHCPServerIfConfigIndex_Object = MibTableColumn
hmDHCPServerIfConfigIndex = _HmDHCPServerIfConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 3, 1, 1, 1),
    _HmDHCPServerIfConfigIndex_Type()
)
hmDHCPServerIfConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerIfConfigIndex.setStatus("current")


class _HmDHCPServerIfConfigMode_Type(Integer32):
    """Custom type hmDHCPServerIfConfigMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HmDHCPServerIfConfigMode_Type.__name__ = "Integer32"
_HmDHCPServerIfConfigMode_Object = MibTableColumn
hmDHCPServerIfConfigMode = _HmDHCPServerIfConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 3, 1, 1, 2),
    _HmDHCPServerIfConfigMode_Type()
)
hmDHCPServerIfConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmDHCPServerIfConfigMode.setStatus("current")
_HmDHCPServerCounterGroup_ObjectIdentity = ObjectIdentity
hmDHCPServerCounterGroup = _HmDHCPServerCounterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4)
)
_HmDHCPServerCounterIfTable_Object = MibTable
hmDHCPServerCounterIfTable = _HmDHCPServerCounterIfTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hmDHCPServerCounterIfTable.setStatus("current")
_HmDHCPServerCounterIfEntry_Object = MibTableRow
hmDHCPServerCounterIfEntry = _HmDHCPServerCounterIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1)
)
hmDHCPServerCounterIfEntry.setIndexNames(
    (0, "HMDHCPS-SNMP-MIB", "hmDHCPServerCounterIfIndex"),
)
if mibBuilder.loadTexts:
    hmDHCPServerCounterIfEntry.setStatus("current")


class _HmDHCPServerCounterIfIndex_Type(Integer32):
    """Custom type hmDHCPServerCounterIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HmDHCPServerCounterIfIndex_Type.__name__ = "Integer32"
_HmDHCPServerCounterIfIndex_Object = MibTableColumn
hmDHCPServerCounterIfIndex = _HmDHCPServerCounterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 1),
    _HmDHCPServerCounterIfIndex_Type()
)
hmDHCPServerCounterIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerCounterIfIndex.setStatus("current")
_HmDHCPServerCounterBootpRequests_Type = Counter32
_HmDHCPServerCounterBootpRequests_Object = MibTableColumn
hmDHCPServerCounterBootpRequests = _HmDHCPServerCounterBootpRequests_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 2),
    _HmDHCPServerCounterBootpRequests_Type()
)
hmDHCPServerCounterBootpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerCounterBootpRequests.setStatus("current")
_HmDHCPServerCounterBootpInvalids_Type = Counter32
_HmDHCPServerCounterBootpInvalids_Object = MibTableColumn
hmDHCPServerCounterBootpInvalids = _HmDHCPServerCounterBootpInvalids_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 3),
    _HmDHCPServerCounterBootpInvalids_Type()
)
hmDHCPServerCounterBootpInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerCounterBootpInvalids.setStatus("current")
_HmDHCPServerCounterBootpReplies_Type = Counter32
_HmDHCPServerCounterBootpReplies_Object = MibTableColumn
hmDHCPServerCounterBootpReplies = _HmDHCPServerCounterBootpReplies_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 4),
    _HmDHCPServerCounterBootpReplies_Type()
)
hmDHCPServerCounterBootpReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerCounterBootpReplies.setStatus("current")
_HmDHCPServerCounterBootpDroppedUnknownClients_Type = Counter32
_HmDHCPServerCounterBootpDroppedUnknownClients_Object = MibTableColumn
hmDHCPServerCounterBootpDroppedUnknownClients = _HmDHCPServerCounterBootpDroppedUnknownClients_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 5),
    _HmDHCPServerCounterBootpDroppedUnknownClients_Type()
)
hmDHCPServerCounterBootpDroppedUnknownClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerCounterBootpDroppedUnknownClients.setStatus("current")
_HmDHCPServerCounterBootpDroppedNotServingSubnet_Type = Counter32
_HmDHCPServerCounterBootpDroppedNotServingSubnet_Object = MibTableColumn
hmDHCPServerCounterBootpDroppedNotServingSubnet = _HmDHCPServerCounterBootpDroppedNotServingSubnet_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 6),
    _HmDHCPServerCounterBootpDroppedNotServingSubnet_Type()
)
hmDHCPServerCounterBootpDroppedNotServingSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerCounterBootpDroppedNotServingSubnet.setStatus("current")
_HmDHCPServerCounterDhcpv4Discovers_Type = Counter32
_HmDHCPServerCounterDhcpv4Discovers_Object = MibTableColumn
hmDHCPServerCounterDhcpv4Discovers = _HmDHCPServerCounterDhcpv4Discovers_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 20),
    _HmDHCPServerCounterDhcpv4Discovers_Type()
)
hmDHCPServerCounterDhcpv4Discovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerCounterDhcpv4Discovers.setStatus("current")
_HmDHCPServerCounterDhcpv4Offers_Type = Counter32
_HmDHCPServerCounterDhcpv4Offers_Object = MibTableColumn
hmDHCPServerCounterDhcpv4Offers = _HmDHCPServerCounterDhcpv4Offers_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 21),
    _HmDHCPServerCounterDhcpv4Offers_Type()
)
hmDHCPServerCounterDhcpv4Offers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerCounterDhcpv4Offers.setStatus("current")
_HmDHCPServerCounterDhcpv4Requests_Type = Counter32
_HmDHCPServerCounterDhcpv4Requests_Object = MibTableColumn
hmDHCPServerCounterDhcpv4Requests = _HmDHCPServerCounterDhcpv4Requests_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 22),
    _HmDHCPServerCounterDhcpv4Requests_Type()
)
hmDHCPServerCounterDhcpv4Requests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerCounterDhcpv4Requests.setStatus("current")
_HmDHCPServerCounterDhcpv4Declines_Type = Counter32
_HmDHCPServerCounterDhcpv4Declines_Object = MibTableColumn
hmDHCPServerCounterDhcpv4Declines = _HmDHCPServerCounterDhcpv4Declines_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 23),
    _HmDHCPServerCounterDhcpv4Declines_Type()
)
hmDHCPServerCounterDhcpv4Declines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerCounterDhcpv4Declines.setStatus("current")
_HmDHCPServerCounterDhcpv4Acks_Type = Counter32
_HmDHCPServerCounterDhcpv4Acks_Object = MibTableColumn
hmDHCPServerCounterDhcpv4Acks = _HmDHCPServerCounterDhcpv4Acks_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 24),
    _HmDHCPServerCounterDhcpv4Acks_Type()
)
hmDHCPServerCounterDhcpv4Acks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerCounterDhcpv4Acks.setStatus("current")
_HmDHCPServerCounterDhcpv4Naks_Type = Counter32
_HmDHCPServerCounterDhcpv4Naks_Object = MibTableColumn
hmDHCPServerCounterDhcpv4Naks = _HmDHCPServerCounterDhcpv4Naks_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 25),
    _HmDHCPServerCounterDhcpv4Naks_Type()
)
hmDHCPServerCounterDhcpv4Naks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerCounterDhcpv4Naks.setStatus("current")
_HmDHCPServerCounterDhcpv4Releases_Type = Counter32
_HmDHCPServerCounterDhcpv4Releases_Object = MibTableColumn
hmDHCPServerCounterDhcpv4Releases = _HmDHCPServerCounterDhcpv4Releases_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 26),
    _HmDHCPServerCounterDhcpv4Releases_Type()
)
hmDHCPServerCounterDhcpv4Releases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerCounterDhcpv4Releases.setStatus("current")
_HmDHCPServerCounterDhcpv4Informs_Type = Counter32
_HmDHCPServerCounterDhcpv4Informs_Object = MibTableColumn
hmDHCPServerCounterDhcpv4Informs = _HmDHCPServerCounterDhcpv4Informs_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 27),
    _HmDHCPServerCounterDhcpv4Informs_Type()
)
hmDHCPServerCounterDhcpv4Informs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerCounterDhcpv4Informs.setStatus("current")
_HmDHCPServerCounterDhcpv4ForcedRenews_Type = Counter32
_HmDHCPServerCounterDhcpv4ForcedRenews_Object = MibTableColumn
hmDHCPServerCounterDhcpv4ForcedRenews = _HmDHCPServerCounterDhcpv4ForcedRenews_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 28),
    _HmDHCPServerCounterDhcpv4ForcedRenews_Type()
)
hmDHCPServerCounterDhcpv4ForcedRenews.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerCounterDhcpv4ForcedRenews.setStatus("current")
_HmDHCPServerCounterDhcpv4Invalids_Type = Counter32
_HmDHCPServerCounterDhcpv4Invalids_Object = MibTableColumn
hmDHCPServerCounterDhcpv4Invalids = _HmDHCPServerCounterDhcpv4Invalids_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 29),
    _HmDHCPServerCounterDhcpv4Invalids_Type()
)
hmDHCPServerCounterDhcpv4Invalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerCounterDhcpv4Invalids.setStatus("current")
_HmDHCPServerCounterDhcpv4DroppedUnknownClient_Type = Counter32
_HmDHCPServerCounterDhcpv4DroppedUnknownClient_Object = MibTableColumn
hmDHCPServerCounterDhcpv4DroppedUnknownClient = _HmDHCPServerCounterDhcpv4DroppedUnknownClient_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 30),
    _HmDHCPServerCounterDhcpv4DroppedUnknownClient_Type()
)
hmDHCPServerCounterDhcpv4DroppedUnknownClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerCounterDhcpv4DroppedUnknownClient.setStatus("current")
_HmDHCPServerCounterDhcpv4DroppedNotServingSubnet_Type = Counter32
_HmDHCPServerCounterDhcpv4DroppedNotServingSubnet_Object = MibTableColumn
hmDHCPServerCounterDhcpv4DroppedNotServingSubnet = _HmDHCPServerCounterDhcpv4DroppedNotServingSubnet_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 31),
    _HmDHCPServerCounterDhcpv4DroppedNotServingSubnet_Type()
)
hmDHCPServerCounterDhcpv4DroppedNotServingSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerCounterDhcpv4DroppedNotServingSubnet.setStatus("current")
_HmDHCPServerCounterMiscOtherDhcpServer_Type = Counter32
_HmDHCPServerCounterMiscOtherDhcpServer_Object = MibTableColumn
hmDHCPServerCounterMiscOtherDhcpServer = _HmDHCPServerCounterMiscOtherDhcpServer_Object(
    (1, 3, 6, 1, 4, 1, 248, 14, 16, 1, 4, 2, 1, 40),
    _HmDHCPServerCounterMiscOtherDhcpServer_Type()
)
hmDHCPServerCounterMiscOtherDhcpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmDHCPServerCounterMiscOtherDhcpServer.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HMDHCPS-SNMP-MIB",
    **{"hmDhcps": hmDhcps,
       "hmDHCPServerGroup": hmDHCPServerGroup,
       "hmDHCPServerConfigGroup": hmDHCPServerConfigGroup,
       "hmDHCPServerMode": hmDHCPServerMode,
       "hmDHCPServerMaxPoolEntries": hmDHCPServerMaxPoolEntries,
       "hmDHCPServerMaxLeaseEntries": hmDHCPServerMaxLeaseEntries,
       "hmDHCPServerAddrProbe": hmDHCPServerAddrProbe,
       "hmDHCPServerPoolTable": hmDHCPServerPoolTable,
       "hmDHCPServerPoolEntry": hmDHCPServerPoolEntry,
       "hmDHCPServerPoolIndex": hmDHCPServerPoolIndex,
       "hmDHCPServerPoolStartIpAddress": hmDHCPServerPoolStartIpAddress,
       "hmDHCPServerPoolEndIpAddress": hmDHCPServerPoolEndIpAddress,
       "hmDHCPServerPoolLeaseTime": hmDHCPServerPoolLeaseTime,
       "hmDHCPServerPoolFlags": hmDHCPServerPoolFlags,
       "hmDHCPServerPoolIfIndex": hmDHCPServerPoolIfIndex,
       "hmDHCPServerPoolMacAddress": hmDHCPServerPoolMacAddress,
       "hmDHCPServerPoolGateway": hmDHCPServerPoolGateway,
       "hmDHCPServerPoolClientId": hmDHCPServerPoolClientId,
       "hmDHCPServerPoolRemoteId": hmDHCPServerPoolRemoteId,
       "hmDHCPServerPoolCircuitId": hmDHCPServerPoolCircuitId,
       "hmDHCPServerPoolHirschmannClient": hmDHCPServerPoolHirschmannClient,
       "hmDHCPServerPoolVlanId": hmDHCPServerPoolVlanId,
       "hmDHCPServerPoolOptionConfFileName": hmDHCPServerPoolOptionConfFileName,
       "hmDHCPServerPoolOptionGateway": hmDHCPServerPoolOptionGateway,
       "hmDHCPServerPoolOptionNetmask": hmDHCPServerPoolOptionNetmask,
       "hmDHCPServerPoolOptionWINS": hmDHCPServerPoolOptionWINS,
       "hmDHCPServerPoolOptionDNS": hmDHCPServerPoolOptionDNS,
       "hmDHCPServerPoolOptionHostname": hmDHCPServerPoolOptionHostname,
       "hmDHCPServerPoolOptionVendor": hmDHCPServerPoolOptionVendor,
       "hmDHCPServerPoolErrorStatus": hmDHCPServerPoolErrorStatus,
       "hmDHCPServerPoolRowStatus": hmDHCPServerPoolRowStatus,
       "hmDHCPServerLeaseGroup": hmDHCPServerLeaseGroup,
       "hmDHCPServerLeaseTable": hmDHCPServerLeaseTable,
       "hmDHCPServerLeaseEntry": hmDHCPServerLeaseEntry,
       "hmDHCPServerLeasePoolIndex": hmDHCPServerLeasePoolIndex,
       "hmDHCPServerLeaseIpAddress": hmDHCPServerLeaseIpAddress,
       "hmDHCPServerLeaseState": hmDHCPServerLeaseState,
       "hmDHCPServerLeaseTimeRemaining": hmDHCPServerLeaseTimeRemaining,
       "hmDHCPServerLeaseIfIndex": hmDHCPServerLeaseIfIndex,
       "hmDHCPServerLeaseClientMacAddress": hmDHCPServerLeaseClientMacAddress,
       "hmDHCPServerLeaseGateway": hmDHCPServerLeaseGateway,
       "hmDHCPServerLeaseClientId": hmDHCPServerLeaseClientId,
       "hmDHCPServerLeaseRemoteId": hmDHCPServerLeaseRemoteId,
       "hmDHCPServerLeaseCircuitId": hmDHCPServerLeaseCircuitId,
       "hmDHCPServerLeaseStartTime": hmDHCPServerLeaseStartTime,
       "hmDHCPServerLeaseAction": hmDHCPServerLeaseAction,
       "hmDHCPServerLeaseVlanId": hmDHCPServerLeaseVlanId,
       "hmDHCPServerInterfaceGroup": hmDHCPServerInterfaceGroup,
       "hmDHCPServerIfConfigTable": hmDHCPServerIfConfigTable,
       "hmDHCPServerIfConfigEntry": hmDHCPServerIfConfigEntry,
       "hmDHCPServerIfConfigIndex": hmDHCPServerIfConfigIndex,
       "hmDHCPServerIfConfigMode": hmDHCPServerIfConfigMode,
       "hmDHCPServerCounterGroup": hmDHCPServerCounterGroup,
       "hmDHCPServerCounterIfTable": hmDHCPServerCounterIfTable,
       "hmDHCPServerCounterIfEntry": hmDHCPServerCounterIfEntry,
       "hmDHCPServerCounterIfIndex": hmDHCPServerCounterIfIndex,
       "hmDHCPServerCounterBootpRequests": hmDHCPServerCounterBootpRequests,
       "hmDHCPServerCounterBootpInvalids": hmDHCPServerCounterBootpInvalids,
       "hmDHCPServerCounterBootpReplies": hmDHCPServerCounterBootpReplies,
       "hmDHCPServerCounterBootpDroppedUnknownClients": hmDHCPServerCounterBootpDroppedUnknownClients,
       "hmDHCPServerCounterBootpDroppedNotServingSubnet": hmDHCPServerCounterBootpDroppedNotServingSubnet,
       "hmDHCPServerCounterDhcpv4Discovers": hmDHCPServerCounterDhcpv4Discovers,
       "hmDHCPServerCounterDhcpv4Offers": hmDHCPServerCounterDhcpv4Offers,
       "hmDHCPServerCounterDhcpv4Requests": hmDHCPServerCounterDhcpv4Requests,
       "hmDHCPServerCounterDhcpv4Declines": hmDHCPServerCounterDhcpv4Declines,
       "hmDHCPServerCounterDhcpv4Acks": hmDHCPServerCounterDhcpv4Acks,
       "hmDHCPServerCounterDhcpv4Naks": hmDHCPServerCounterDhcpv4Naks,
       "hmDHCPServerCounterDhcpv4Releases": hmDHCPServerCounterDhcpv4Releases,
       "hmDHCPServerCounterDhcpv4Informs": hmDHCPServerCounterDhcpv4Informs,
       "hmDHCPServerCounterDhcpv4ForcedRenews": hmDHCPServerCounterDhcpv4ForcedRenews,
       "hmDHCPServerCounterDhcpv4Invalids": hmDHCPServerCounterDhcpv4Invalids,
       "hmDHCPServerCounterDhcpv4DroppedUnknownClient": hmDHCPServerCounterDhcpv4DroppedUnknownClient,
       "hmDHCPServerCounterDhcpv4DroppedNotServingSubnet": hmDHCPServerCounterDhcpv4DroppedNotServingSubnet,
       "hmDHCPServerCounterMiscOtherDhcpServer": hmDHCPServerCounterMiscOtherDhcpServer}
)
