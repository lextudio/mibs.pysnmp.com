# SNMP MIB module (AT-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-DHCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:01 2024
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

(DisplayStringUnsized,
 modules) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "DisplayStringUnsized",
    "modules")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dhcp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70)
)
dhcp.setRevisions(
        ("2009-04-01 02:00",
         "2006-06-28 12:22")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DhcpTraps_ObjectIdentity = ObjectIdentity
dhcpTraps = _DhcpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 0)
)
_DhcpRangeTable_Object = MibTable
dhcpRangeTable = _DhcpRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 1)
)
if mibBuilder.loadTexts:
    dhcpRangeTable.setStatus("current")
_DhcpRangeEntry_Object = MibTableRow
dhcpRangeEntry = _DhcpRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 1, 1)
)
dhcpRangeEntry.setIndexNames(
    (0, "AT-DHCP-MIB", "dhcpRangeIndex"),
)
if mibBuilder.loadTexts:
    dhcpRangeEntry.setStatus("current")
_DhcpRangeIndex_Type = Integer32
_DhcpRangeIndex_Object = MibTableColumn
dhcpRangeIndex = _DhcpRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 1, 1, 1),
    _DhcpRangeIndex_Type()
)
dhcpRangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRangeIndex.setStatus("current")


class _DhcpRangeName_Type(DisplayStringUnsized):
    """Custom type dhcpRangeName based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_DhcpRangeName_Type.__name__ = "DisplayStringUnsized"
_DhcpRangeName_Object = MibTableColumn
dhcpRangeName = _DhcpRangeName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 1, 1, 2),
    _DhcpRangeName_Type()
)
dhcpRangeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRangeName.setStatus("current")
_DhcpRangeBaseAddress_Type = IpAddress
_DhcpRangeBaseAddress_Object = MibTableColumn
dhcpRangeBaseAddress = _DhcpRangeBaseAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 1, 1, 3),
    _DhcpRangeBaseAddress_Type()
)
dhcpRangeBaseAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRangeBaseAddress.setStatus("current")


class _DhcpRangeNumberOfAddresses_Type(Integer32):
    """Custom type dhcpRangeNumberOfAddresses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_DhcpRangeNumberOfAddresses_Type.__name__ = "Integer32"
_DhcpRangeNumberOfAddresses_Object = MibTableColumn
dhcpRangeNumberOfAddresses = _DhcpRangeNumberOfAddresses_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 1, 1, 4),
    _DhcpRangeNumberOfAddresses_Type()
)
dhcpRangeNumberOfAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRangeNumberOfAddresses.setStatus("current")
_DhcpRangeGateway_Type = IpAddress
_DhcpRangeGateway_Object = MibTableColumn
dhcpRangeGateway = _DhcpRangeGateway_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 1, 1, 5),
    _DhcpRangeGateway_Type()
)
dhcpRangeGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRangeGateway.setStatus("current")
_DhcpTrapVariable_ObjectIdentity = ObjectIdentity
dhcpTrapVariable = _DhcpTrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 2)
)
_DhcpRangeExhaustedGateway_Type = IpAddress
_DhcpRangeExhaustedGateway_Object = MibScalar
dhcpRangeExhaustedGateway = _DhcpRangeExhaustedGateway_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 2, 1),
    _DhcpRangeExhaustedGateway_Type()
)
dhcpRangeExhaustedGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRangeExhaustedGateway.setStatus("current")
_DhcpRangeExhaustedInterface_Type = IpAddress
_DhcpRangeExhaustedInterface_Object = MibScalar
dhcpRangeExhaustedInterface = _DhcpRangeExhaustedInterface_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 2, 2),
    _DhcpRangeExhaustedInterface_Type()
)
dhcpRangeExhaustedInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRangeExhaustedInterface.setStatus("current")


class _DhcpRangeExceededRange_Type(DisplayStringUnsized):
    """Custom type dhcpRangeExceededRange based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_DhcpRangeExceededRange_Type.__name__ = "DisplayStringUnsized"
_DhcpRangeExceededRange_Object = MibScalar
dhcpRangeExceededRange = _DhcpRangeExceededRange_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 2, 3),
    _DhcpRangeExceededRange_Type()
)
dhcpRangeExceededRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRangeExceededRange.setStatus("current")


class _DhcpRangeExceededClients_Type(Integer32):
    """Custom type dhcpRangeExceededClients based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_DhcpRangeExceededClients_Type.__name__ = "Integer32"
_DhcpRangeExceededClients_Object = MibScalar
dhcpRangeExceededClients = _DhcpRangeExceededClients_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 2, 4),
    _DhcpRangeExceededClients_Type()
)
dhcpRangeExceededClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRangeExceededClients.setStatus("current")


class _DhcpRangeExceededRemaining_Type(Integer32):
    """Custom type dhcpRangeExceededRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_DhcpRangeExceededRemaining_Type.__name__ = "Integer32"
_DhcpRangeExceededRemaining_Object = MibScalar
dhcpRangeExceededRemaining = _DhcpRangeExceededRemaining_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 2, 5),
    _DhcpRangeExceededRemaining_Type()
)
dhcpRangeExceededRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRangeExceededRemaining.setStatus("current")


class _DhcpRangeExceededPercentage_Type(Integer32):
    """Custom type dhcpRangeExceededPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DhcpRangeExceededPercentage_Type.__name__ = "Integer32"
_DhcpRangeExceededPercentage_Object = MibScalar
dhcpRangeExceededPercentage = _DhcpRangeExceededPercentage_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 2, 6),
    _DhcpRangeExceededPercentage_Type()
)
dhcpRangeExceededPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRangeExceededPercentage.setStatus("current")
_DhcpClientTable_Object = MibTable
dhcpClientTable = _DhcpClientTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 3)
)
if mibBuilder.loadTexts:
    dhcpClientTable.setStatus("current")
_DhcpClientEntry_Object = MibTableRow
dhcpClientEntry = _DhcpClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 3, 1)
)
dhcpClientEntry.setIndexNames(
    (0, "AT-DHCP-MIB", "dhcpRangeIndex"),
    (0, "AT-DHCP-MIB", "dhcpClientIpAddress"),
)
if mibBuilder.loadTexts:
    dhcpClientEntry.setStatus("current")
_DhcpClientIpAddress_Type = IpAddress
_DhcpClientIpAddress_Object = MibTableColumn
dhcpClientIpAddress = _DhcpClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 3, 1, 1),
    _DhcpClientIpAddress_Type()
)
dhcpClientIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientIpAddress.setStatus("current")
_DhcpClientID_Type = OctetString
_DhcpClientID_Object = MibTableColumn
dhcpClientID = _DhcpClientID_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 3, 1, 2),
    _DhcpClientID_Type()
)
dhcpClientID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientID.setStatus("current")


class _DhcpClientState_Type(Integer32):
    """Custom type dhcpClientState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inuse", 2),
          ("offered", 3),
          ("reclaiming", 1),
          ("unused", 0))
    )


_DhcpClientState_Type.__name__ = "Integer32"
_DhcpClientState_Object = MibTableColumn
dhcpClientState = _DhcpClientState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 3, 1, 3),
    _DhcpClientState_Type()
)
dhcpClientState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientState.setStatus("current")


class _DhcpClientType_Type(Integer32):
    """Custom type dhcpClientType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("dyn", 2),
          ("static", 3))
    )


_DhcpClientType_Type.__name__ = "Integer32"
_DhcpClientType_Object = MibTableColumn
dhcpClientType = _DhcpClientType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 3, 1, 4),
    _DhcpClientType_Type()
)
dhcpClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientType.setStatus("current")
_DhcpClientExpiry_Type = OctetString
_DhcpClientExpiry_Object = MibTableColumn
dhcpClientExpiry = _DhcpClientExpiry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 3, 1, 5),
    _DhcpClientExpiry_Type()
)
dhcpClientExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientExpiry.setStatus("current")

# Managed Objects groups


# Notification objects

dhcpRangeExhaustedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 0, 1)
)
dhcpRangeExhaustedTrap.setObjects(
      *(("AT-DHCP-MIB", "dhcpRangeExhaustedGateway"),
        ("AT-DHCP-MIB", "dhcpRangeExhaustedInterface"))
)
if mibBuilder.loadTexts:
    dhcpRangeExhaustedTrap.setStatus(
        "current"
    )

dhcpRangeExceededThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 0, 2)
)
dhcpRangeExceededThresholdTrap.setObjects(
      *(("AT-DHCP-MIB", "dhcpRangeExhaustedInterface"),
        ("AT-DHCP-MIB", "dhcpRangeExceededRange"),
        ("AT-DHCP-MIB", "dhcpRangeExceededClients"),
        ("AT-DHCP-MIB", "dhcpRangeExceededRemaining"),
        ("AT-DHCP-MIB", "dhcpRangeExceededPercentage"))
)
if mibBuilder.loadTexts:
    dhcpRangeExceededThresholdTrap.setStatus(
        "current"
    )

dhcpRangeExceededThresholdClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 70, 0, 3)
)
dhcpRangeExceededThresholdClearTrap.setObjects(
      *(("AT-DHCP-MIB", "dhcpRangeExhaustedInterface"),
        ("AT-DHCP-MIB", "dhcpRangeExceededRange"),
        ("AT-DHCP-MIB", "dhcpRangeExceededClients"),
        ("AT-DHCP-MIB", "dhcpRangeExceededRemaining"),
        ("AT-DHCP-MIB", "dhcpRangeExceededPercentage"))
)
if mibBuilder.loadTexts:
    dhcpRangeExceededThresholdClearTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-DHCP-MIB",
    **{"dhcp": dhcp,
       "dhcpTraps": dhcpTraps,
       "dhcpRangeExhaustedTrap": dhcpRangeExhaustedTrap,
       "dhcpRangeExceededThresholdTrap": dhcpRangeExceededThresholdTrap,
       "dhcpRangeExceededThresholdClearTrap": dhcpRangeExceededThresholdClearTrap,
       "dhcpRangeTable": dhcpRangeTable,
       "dhcpRangeEntry": dhcpRangeEntry,
       "dhcpRangeIndex": dhcpRangeIndex,
       "dhcpRangeName": dhcpRangeName,
       "dhcpRangeBaseAddress": dhcpRangeBaseAddress,
       "dhcpRangeNumberOfAddresses": dhcpRangeNumberOfAddresses,
       "dhcpRangeGateway": dhcpRangeGateway,
       "dhcpTrapVariable": dhcpTrapVariable,
       "dhcpRangeExhaustedGateway": dhcpRangeExhaustedGateway,
       "dhcpRangeExhaustedInterface": dhcpRangeExhaustedInterface,
       "dhcpRangeExceededRange": dhcpRangeExceededRange,
       "dhcpRangeExceededClients": dhcpRangeExceededClients,
       "dhcpRangeExceededRemaining": dhcpRangeExceededRemaining,
       "dhcpRangeExceededPercentage": dhcpRangeExceededPercentage,
       "dhcpClientTable": dhcpClientTable,
       "dhcpClientEntry": dhcpClientEntry,
       "dhcpClientIpAddress": dhcpClientIpAddress,
       "dhcpClientID": dhcpClientID,
       "dhcpClientState": dhcpClientState,
       "dhcpClientType": dhcpClientType,
       "dhcpClientExpiry": dhcpClientExpiry}
)
