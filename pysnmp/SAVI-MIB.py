# SNMP MIB module (SAVI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SAVI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:45 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType,
 InetVersion) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetVersion")

(ip,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ip")

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
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

saviMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 4, 40)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SaviObjects_ObjectIdentity = ObjectIdentity
saviObjects = _SaviObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4, 40, 1)
)
_SaviObjectsSystemTable_Object = MibTable
saviObjectsSystemTable = _SaviObjectsSystemTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 1)
)
if mibBuilder.loadTexts:
    saviObjectsSystemTable.setStatus("current")
_SaviObjectsSystemEntry_Object = MibTableRow
saviObjectsSystemEntry = _SaviObjectsSystemEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 1, 1)
)
saviObjectsSystemEntry.setIndexNames(
    (0, "SAVI-MIB", "saviObjectsSystemIPVersion"),
)
if mibBuilder.loadTexts:
    saviObjectsSystemEntry.setStatus("current")
_SaviObjectsSystemIPVersion_Type = InetVersion
_SaviObjectsSystemIPVersion_Object = MibTableColumn
saviObjectsSystemIPVersion = _SaviObjectsSystemIPVersion_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 1, 1, 1),
    _SaviObjectsSystemIPVersion_Type()
)
saviObjectsSystemIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saviObjectsSystemIPVersion.setStatus("current")


class _SaviObjectsSystemMode_Type(Integer32):
    """Custom type saviObjectsSystemMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("savi-default", 2),
          ("savi-dhcp-only", 3),
          ("savi-dhcp-slaac-mix", 5),
          ("savi-disable", 1),
          ("savi-slaac-only", 4))
    )


_SaviObjectsSystemMode_Type.__name__ = "Integer32"
_SaviObjectsSystemMode_Object = MibTableColumn
saviObjectsSystemMode = _SaviObjectsSystemMode_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 1, 1, 2),
    _SaviObjectsSystemMode_Type()
)
saviObjectsSystemMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saviObjectsSystemMode.setStatus("current")
_SaviObjectsSystemMaxDadDelay_Type = TimeInterval
_SaviObjectsSystemMaxDadDelay_Object = MibTableColumn
saviObjectsSystemMaxDadDelay = _SaviObjectsSystemMaxDadDelay_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 1, 1, 3),
    _SaviObjectsSystemMaxDadDelay_Type()
)
saviObjectsSystemMaxDadDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saviObjectsSystemMaxDadDelay.setStatus("current")
_SaviObjectsSystemMaxDadPrepareDelay_Type = TimeInterval
_SaviObjectsSystemMaxDadPrepareDelay_Object = MibTableColumn
saviObjectsSystemMaxDadPrepareDelay = _SaviObjectsSystemMaxDadPrepareDelay_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 1, 1, 4),
    _SaviObjectsSystemMaxDadPrepareDelay_Type()
)
saviObjectsSystemMaxDadPrepareDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saviObjectsSystemMaxDadPrepareDelay.setStatus("current")
_SaviObjectsIfTable_Object = MibTable
saviObjectsIfTable = _SaviObjectsIfTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 2)
)
if mibBuilder.loadTexts:
    saviObjectsIfTable.setStatus("current")
_SaviObjectsIfEntry_Object = MibTableRow
saviObjectsIfEntry = _SaviObjectsIfEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 2, 1)
)
saviObjectsIfEntry.setIndexNames(
    (0, "SAVI-MIB", "saviObjectsIfIPVersion"),
    (0, "SAVI-MIB", "saviObjectsIfIfIndex"),
)
if mibBuilder.loadTexts:
    saviObjectsIfEntry.setStatus("current")
_SaviObjectsIfIPVersion_Type = InetVersion
_SaviObjectsIfIPVersion_Object = MibTableColumn
saviObjectsIfIPVersion = _SaviObjectsIfIPVersion_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 2, 1, 1),
    _SaviObjectsIfIPVersion_Type()
)
saviObjectsIfIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saviObjectsIfIPVersion.setStatus("current")
_SaviObjectsIfIfIndex_Type = InterfaceIndex
_SaviObjectsIfIfIndex_Object = MibTableColumn
saviObjectsIfIfIndex = _SaviObjectsIfIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 2, 1, 2),
    _SaviObjectsIfIfIndex_Type()
)
saviObjectsIfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saviObjectsIfIfIndex.setStatus("current")


class _SaviObjectsIfValidationStatus_Type(Integer32):
    """Custom type saviObjectsIfValidationStatus based on Integer32"""
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


_SaviObjectsIfValidationStatus_Type.__name__ = "Integer32"
_SaviObjectsIfValidationStatus_Object = MibTableColumn
saviObjectsIfValidationStatus = _SaviObjectsIfValidationStatus_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 2, 1, 3),
    _SaviObjectsIfValidationStatus_Type()
)
saviObjectsIfValidationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saviObjectsIfValidationStatus.setStatus("current")


class _SaviObjectsIfTrustStatus_Type(Integer32):
    """Custom type saviObjectsIfTrustStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dhcp-ra-trust", 4),
          ("dhcp-trust", 2),
          ("no-trust", 1),
          ("ra-trust", 3))
    )


_SaviObjectsIfTrustStatus_Type.__name__ = "Integer32"
_SaviObjectsIfTrustStatus_Object = MibTableColumn
saviObjectsIfTrustStatus = _SaviObjectsIfTrustStatus_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 2, 1, 4),
    _SaviObjectsIfTrustStatus_Type()
)
saviObjectsIfTrustStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saviObjectsIfTrustStatus.setStatus("current")
_SaviObjectsIfFilteringNum_Type = Unsigned32
_SaviObjectsIfFilteringNum_Object = MibTableColumn
saviObjectsIfFilteringNum = _SaviObjectsIfFilteringNum_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 2, 1, 5),
    _SaviObjectsIfFilteringNum_Type()
)
saviObjectsIfFilteringNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saviObjectsIfFilteringNum.setStatus("current")
_SaviObjectsBindingTable_Object = MibTable
saviObjectsBindingTable = _SaviObjectsBindingTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 3)
)
if mibBuilder.loadTexts:
    saviObjectsBindingTable.setStatus("current")
_SaviObjectsBindingEntry_Object = MibTableRow
saviObjectsBindingEntry = _SaviObjectsBindingEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 3, 1)
)
saviObjectsBindingEntry.setIndexNames(
    (0, "SAVI-MIB", "saviObjectsBindingIpAddressType"),
    (0, "SAVI-MIB", "saviObjectsBindingType"),
    (0, "SAVI-MIB", "saviObjectsBindingIfIndex"),
    (0, "SAVI-MIB", "saviObjectsBindingIpAddress"),
)
if mibBuilder.loadTexts:
    saviObjectsBindingEntry.setStatus("current")
_SaviObjectsBindingIpAddressType_Type = InetAddressType
_SaviObjectsBindingIpAddressType_Object = MibTableColumn
saviObjectsBindingIpAddressType = _SaviObjectsBindingIpAddressType_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 3, 1, 1),
    _SaviObjectsBindingIpAddressType_Type()
)
saviObjectsBindingIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saviObjectsBindingIpAddressType.setStatus("current")


class _SaviObjectsBindingType_Type(Integer32):
    """Custom type saviObjectsBindingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 3),
          ("slaac", 2),
          ("static", 1))
    )


_SaviObjectsBindingType_Type.__name__ = "Integer32"
_SaviObjectsBindingType_Object = MibTableColumn
saviObjectsBindingType = _SaviObjectsBindingType_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 3, 1, 2),
    _SaviObjectsBindingType_Type()
)
saviObjectsBindingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saviObjectsBindingType.setStatus("current")
_SaviObjectsBindingIfIndex_Type = InterfaceIndex
_SaviObjectsBindingIfIndex_Object = MibTableColumn
saviObjectsBindingIfIndex = _SaviObjectsBindingIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 3, 1, 3),
    _SaviObjectsBindingIfIndex_Type()
)
saviObjectsBindingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saviObjectsBindingIfIndex.setStatus("current")
_SaviObjectsBindingIpAddress_Type = InetAddress
_SaviObjectsBindingIpAddress_Object = MibTableColumn
saviObjectsBindingIpAddress = _SaviObjectsBindingIpAddress_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 3, 1, 4),
    _SaviObjectsBindingIpAddress_Type()
)
saviObjectsBindingIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saviObjectsBindingIpAddress.setStatus("current")
_SaviObjectsBindingMacAddr_Type = MacAddress
_SaviObjectsBindingMacAddr_Object = MibTableColumn
saviObjectsBindingMacAddr = _SaviObjectsBindingMacAddr_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 3, 1, 5),
    _SaviObjectsBindingMacAddr_Type()
)
saviObjectsBindingMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    saviObjectsBindingMacAddr.setStatus("current")


class _SaviObjectsBindingState_Type(Integer32):
    """Custom type saviObjectsBindingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("bound", 5),
          ("detection", 3),
          ("live", 2),
          ("query", 4),
          ("start", 1))
    )


_SaviObjectsBindingState_Type.__name__ = "Integer32"
_SaviObjectsBindingState_Object = MibTableColumn
saviObjectsBindingState = _SaviObjectsBindingState_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 3, 1, 6),
    _SaviObjectsBindingState_Type()
)
saviObjectsBindingState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    saviObjectsBindingState.setStatus("current")
_SaviObjectsBindingLifetime_Type = TimeInterval
_SaviObjectsBindingLifetime_Object = MibTableColumn
saviObjectsBindingLifetime = _SaviObjectsBindingLifetime_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 3, 1, 7),
    _SaviObjectsBindingLifetime_Type()
)
saviObjectsBindingLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    saviObjectsBindingLifetime.setStatus("current")
_SaviObjectsBindingRowStatus_Type = RowStatus
_SaviObjectsBindingRowStatus_Object = MibTableColumn
saviObjectsBindingRowStatus = _SaviObjectsBindingRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 3, 1, 8),
    _SaviObjectsBindingRowStatus_Type()
)
saviObjectsBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    saviObjectsBindingRowStatus.setStatus("current")
_SaviObjectsFilteringTable_Object = MibTable
saviObjectsFilteringTable = _SaviObjectsFilteringTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 4)
)
if mibBuilder.loadTexts:
    saviObjectsFilteringTable.setStatus("current")
_SaviObjectsFilteringEntry_Object = MibTableRow
saviObjectsFilteringEntry = _SaviObjectsFilteringEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 4, 1)
)
saviObjectsFilteringEntry.setIndexNames(
    (0, "SAVI-MIB", "saviObjectsFilteringIpAddressType"),
    (0, "SAVI-MIB", "saviObjectsFilteringIfIndex"),
    (0, "SAVI-MIB", "saviObjectsFilteringIpAddress"),
)
if mibBuilder.loadTexts:
    saviObjectsFilteringEntry.setStatus("current")
_SaviObjectsFilteringIpAddressType_Type = InetAddressType
_SaviObjectsFilteringIpAddressType_Object = MibTableColumn
saviObjectsFilteringIpAddressType = _SaviObjectsFilteringIpAddressType_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 4, 1, 1),
    _SaviObjectsFilteringIpAddressType_Type()
)
saviObjectsFilteringIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saviObjectsFilteringIpAddressType.setStatus("current")
_SaviObjectsFilteringIfIndex_Type = InterfaceIndex
_SaviObjectsFilteringIfIndex_Object = MibTableColumn
saviObjectsFilteringIfIndex = _SaviObjectsFilteringIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 4, 1, 2),
    _SaviObjectsFilteringIfIndex_Type()
)
saviObjectsFilteringIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saviObjectsFilteringIfIndex.setStatus("current")
_SaviObjectsFilteringIpAddress_Type = InetAddress
_SaviObjectsFilteringIpAddress_Object = MibTableColumn
saviObjectsFilteringIpAddress = _SaviObjectsFilteringIpAddress_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 4, 1, 3),
    _SaviObjectsFilteringIpAddress_Type()
)
saviObjectsFilteringIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    saviObjectsFilteringIpAddress.setStatus("current")
_SaviObjectsFilteringMacAddr_Type = MacAddress
_SaviObjectsFilteringMacAddr_Object = MibTableColumn
saviObjectsFilteringMacAddr = _SaviObjectsFilteringMacAddr_Object(
    (1, 3, 6, 1, 2, 1, 4, 40, 1, 4, 1, 4),
    _SaviObjectsFilteringMacAddr_Type()
)
saviObjectsFilteringMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saviObjectsFilteringMacAddr.setStatus("current")
_SaviConformance_ObjectIdentity = ObjectIdentity
saviConformance = _SaviConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4, 40, 2)
)
_SaviCompliances_ObjectIdentity = ObjectIdentity
saviCompliances = _SaviCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4, 40, 2, 1)
)
_SaviGroups_ObjectIdentity = ObjectIdentity
saviGroups = _SaviGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4, 40, 2, 2)
)

# Managed Objects groups

systemGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 4, 40, 2, 2, 1)
)
systemGroup.setObjects(
      *(("SAVI-MIB", "saviObjectsSystemMode"),
        ("SAVI-MIB", "saviObjectsSystemMaxDadDelay"),
        ("SAVI-MIB", "saviObjectsSystemMaxDadPrepareDelay"))
)
if mibBuilder.loadTexts:
    systemGroup.setStatus("current")

ifGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 4, 40, 2, 2, 2)
)
ifGroup.setObjects(
      *(("SAVI-MIB", "saviObjectsIfValidationStatus"),
        ("SAVI-MIB", "saviObjectsIfTrustStatus"),
        ("SAVI-MIB", "saviObjectsIfFilteringNum"))
)
if mibBuilder.loadTexts:
    ifGroup.setStatus("current")

bindingGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 4, 40, 2, 2, 3)
)
bindingGroup.setObjects(
      *(("SAVI-MIB", "saviObjectsBindingMacAddr"),
        ("SAVI-MIB", "saviObjectsBindingState"),
        ("SAVI-MIB", "saviObjectsBindingLifetime"),
        ("SAVI-MIB", "saviObjectsBindingRowStatus"))
)
if mibBuilder.loadTexts:
    bindingGroup.setStatus("current")

filteringGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 4, 40, 2, 2, 4)
)
filteringGroup.setObjects(
    ("SAVI-MIB", "saviObjectsFilteringMacAddr")
)
if mibBuilder.loadTexts:
    filteringGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

saviCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 4, 40, 2, 1, 1)
)
if mibBuilder.loadTexts:
    saviCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SAVI-MIB",
    **{"saviMIB": saviMIB,
       "saviObjects": saviObjects,
       "saviObjectsSystemTable": saviObjectsSystemTable,
       "saviObjectsSystemEntry": saviObjectsSystemEntry,
       "saviObjectsSystemIPVersion": saviObjectsSystemIPVersion,
       "saviObjectsSystemMode": saviObjectsSystemMode,
       "saviObjectsSystemMaxDadDelay": saviObjectsSystemMaxDadDelay,
       "saviObjectsSystemMaxDadPrepareDelay": saviObjectsSystemMaxDadPrepareDelay,
       "saviObjectsIfTable": saviObjectsIfTable,
       "saviObjectsIfEntry": saviObjectsIfEntry,
       "saviObjectsIfIPVersion": saviObjectsIfIPVersion,
       "saviObjectsIfIfIndex": saviObjectsIfIfIndex,
       "saviObjectsIfValidationStatus": saviObjectsIfValidationStatus,
       "saviObjectsIfTrustStatus": saviObjectsIfTrustStatus,
       "saviObjectsIfFilteringNum": saviObjectsIfFilteringNum,
       "saviObjectsBindingTable": saviObjectsBindingTable,
       "saviObjectsBindingEntry": saviObjectsBindingEntry,
       "saviObjectsBindingIpAddressType": saviObjectsBindingIpAddressType,
       "saviObjectsBindingType": saviObjectsBindingType,
       "saviObjectsBindingIfIndex": saviObjectsBindingIfIndex,
       "saviObjectsBindingIpAddress": saviObjectsBindingIpAddress,
       "saviObjectsBindingMacAddr": saviObjectsBindingMacAddr,
       "saviObjectsBindingState": saviObjectsBindingState,
       "saviObjectsBindingLifetime": saviObjectsBindingLifetime,
       "saviObjectsBindingRowStatus": saviObjectsBindingRowStatus,
       "saviObjectsFilteringTable": saviObjectsFilteringTable,
       "saviObjectsFilteringEntry": saviObjectsFilteringEntry,
       "saviObjectsFilteringIpAddressType": saviObjectsFilteringIpAddressType,
       "saviObjectsFilteringIfIndex": saviObjectsFilteringIfIndex,
       "saviObjectsFilteringIpAddress": saviObjectsFilteringIpAddress,
       "saviObjectsFilteringMacAddr": saviObjectsFilteringMacAddr,
       "saviConformance": saviConformance,
       "saviCompliances": saviCompliances,
       "saviCompliance": saviCompliance,
       "saviGroups": saviGroups,
       "systemGroup": systemGroup,
       "ifGroup": ifGroup,
       "bindingGroup": bindingGroup,
       "filteringGroup": filteringGroup}
)
