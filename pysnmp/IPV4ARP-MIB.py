# SNMP MIB module (IPV4ARP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPV4ARP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:21 2024
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

(apIpv4Arp,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "apIpv4Arp")

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

ipv4ArpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 4, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ApIpv4ArpAddressMax_Type(Integer32):
    """Custom type apIpv4ArpAddressMax based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ApIpv4ArpAddressMax_Type.__name__ = "Integer32"
_ApIpv4ArpAddressMax_Object = MibScalar
apIpv4ArpAddressMax = _ApIpv4ArpAddressMax_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 4, 2),
    _ApIpv4ArpAddressMax_Type()
)
apIpv4ArpAddressMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4ArpAddressMax.setStatus("current")


class _ApIpv4ArpResponseWait_Type(Integer32):
    """Custom type apIpv4ArpResponseWait based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_ApIpv4ArpResponseWait_Type.__name__ = "Integer32"
_ApIpv4ArpResponseWait_Object = MibScalar
apIpv4ArpResponseWait = _ApIpv4ArpResponseWait_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 4, 3),
    _ApIpv4ArpResponseWait_Type()
)
apIpv4ArpResponseWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4ArpResponseWait.setStatus("current")


class _ApIpv4ArpFlushTime_Type(Integer32):
    """Custom type apIpv4ArpFlushTime based on Integer32"""
    defaultValue = 14400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86401),
    )


_ApIpv4ArpFlushTime_Type.__name__ = "Integer32"
_ApIpv4ArpFlushTime_Object = MibScalar
apIpv4ArpFlushTime = _ApIpv4ArpFlushTime_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 4, 4),
    _ApIpv4ArpFlushTime_Type()
)
apIpv4ArpFlushTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4ArpFlushTime.setStatus("current")
_ApIpv4StaticArpTable_Object = MibTable
apIpv4StaticArpTable = _ApIpv4StaticArpTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 4, 5)
)
if mibBuilder.loadTexts:
    apIpv4StaticArpTable.setStatus("current")
_ApIpv4StaticArpEntry_Object = MibTableRow
apIpv4StaticArpEntry = _ApIpv4StaticArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 4, 5, 1)
)
apIpv4StaticArpEntry.setIndexNames(
    (0, "IPV4ARP-MIB", "apIpv4ArpIpAddress"),
)
if mibBuilder.loadTexts:
    apIpv4StaticArpEntry.setStatus("current")
_ApIpv4StaticArpIpAddress_Type = IpAddress
_ApIpv4StaticArpIpAddress_Object = MibTableColumn
apIpv4StaticArpIpAddress = _ApIpv4StaticArpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 4, 5, 1, 1),
    _ApIpv4StaticArpIpAddress_Type()
)
apIpv4StaticArpIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4StaticArpIpAddress.setStatus("current")
_ApIpv4StaticArpMacAddress_Type = MacAddress
_ApIpv4StaticArpMacAddress_Object = MibTableColumn
apIpv4StaticArpMacAddress = _ApIpv4StaticArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 4, 5, 1, 2),
    _ApIpv4StaticArpMacAddress_Type()
)
apIpv4StaticArpMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4StaticArpMacAddress.setStatus("current")
_ApIpv4StaticArpStatus_Type = RowStatus
_ApIpv4StaticArpStatus_Object = MibTableColumn
apIpv4StaticArpStatus = _ApIpv4StaticArpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 4, 5, 1, 3),
    _ApIpv4StaticArpStatus_Type()
)
apIpv4StaticArpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4StaticArpStatus.setStatus("current")


class _ApIpv4StaticArpIfIndex_Type(Integer32):
    """Custom type apIpv4StaticArpIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApIpv4StaticArpIfIndex_Type.__name__ = "Integer32"
_ApIpv4StaticArpIfIndex_Object = MibTableColumn
apIpv4StaticArpIfIndex = _ApIpv4StaticArpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 4, 5, 1, 4),
    _ApIpv4StaticArpIfIndex_Type()
)
apIpv4StaticArpIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4StaticArpIfIndex.setStatus("current")
_ApIpv4ArpTable_Object = MibTable
apIpv4ArpTable = _ApIpv4ArpTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 4, 6)
)
if mibBuilder.loadTexts:
    apIpv4ArpTable.setStatus("current")
_ApIpv4ArpEntry_Object = MibTableRow
apIpv4ArpEntry = _ApIpv4ArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 4, 6, 1)
)
apIpv4ArpEntry.setIndexNames(
    (0, "IPV4ARP-MIB", "apIpv4ArpIpAddress"),
)
if mibBuilder.loadTexts:
    apIpv4ArpEntry.setStatus("current")
_ApIpv4ArpIpAddress_Type = IpAddress
_ApIpv4ArpIpAddress_Object = MibTableColumn
apIpv4ArpIpAddress = _ApIpv4ArpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 4, 6, 1, 1),
    _ApIpv4ArpIpAddress_Type()
)
apIpv4ArpIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4ArpIpAddress.setStatus("current")
_ApIpv4ArpMacAddress_Type = MacAddress
_ApIpv4ArpMacAddress_Object = MibTableColumn
apIpv4ArpMacAddress = _ApIpv4ArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 4, 6, 1, 2),
    _ApIpv4ArpMacAddress_Type()
)
apIpv4ArpMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4ArpMacAddress.setStatus("current")


class _ApIpv4ArpResolutionType_Type(Integer32):
    """Custom type apIpv4ArpResolutionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_ApIpv4ArpResolutionType_Type.__name__ = "Integer32"
_ApIpv4ArpResolutionType_Object = MibTableColumn
apIpv4ArpResolutionType = _ApIpv4ArpResolutionType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 4, 6, 1, 3),
    _ApIpv4ArpResolutionType_Type()
)
apIpv4ArpResolutionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4ArpResolutionType.setStatus("current")
_ApIpv4ArpSlotLearned_Type = Integer32
_ApIpv4ArpSlotLearned_Object = MibTableColumn
apIpv4ArpSlotLearned = _ApIpv4ArpSlotLearned_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 4, 6, 1, 4),
    _ApIpv4ArpSlotLearned_Type()
)
apIpv4ArpSlotLearned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4ArpSlotLearned.setStatus("current")
_ApIpv4ArpPortLearned_Type = Integer32
_ApIpv4ArpPortLearned_Object = MibTableColumn
apIpv4ArpPortLearned = _ApIpv4ArpPortLearned_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 4, 6, 1, 5),
    _ApIpv4ArpPortLearned_Type()
)
apIpv4ArpPortLearned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4ArpPortLearned.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPV4ARP-MIB",
    **{"ipv4ArpMib": ipv4ArpMib,
       "apIpv4ArpAddressMax": apIpv4ArpAddressMax,
       "apIpv4ArpResponseWait": apIpv4ArpResponseWait,
       "apIpv4ArpFlushTime": apIpv4ArpFlushTime,
       "apIpv4StaticArpTable": apIpv4StaticArpTable,
       "apIpv4StaticArpEntry": apIpv4StaticArpEntry,
       "apIpv4StaticArpIpAddress": apIpv4StaticArpIpAddress,
       "apIpv4StaticArpMacAddress": apIpv4StaticArpMacAddress,
       "apIpv4StaticArpStatus": apIpv4StaticArpStatus,
       "apIpv4StaticArpIfIndex": apIpv4StaticArpIfIndex,
       "apIpv4ArpTable": apIpv4ArpTable,
       "apIpv4ArpEntry": apIpv4ArpEntry,
       "apIpv4ArpIpAddress": apIpv4ArpIpAddress,
       "apIpv4ArpMacAddress": apIpv4ArpMacAddress,
       "apIpv4ArpResolutionType": apIpv4ArpResolutionType,
       "apIpv4ArpSlotLearned": apIpv4ArpSlotLearned,
       "apIpv4ArpPortLearned": apIpv4ArpPortLearned}
)
