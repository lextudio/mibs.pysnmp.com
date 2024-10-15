# SNMP MIB module (HPICF-SAVI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPICF-SAVI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:21 2024
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

(hpSwitchExperimental,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitchExperimental")

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

hpicfSaviMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1)
)
hpicfSaviMIB.setRevisions(
        ("2017-11-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfSaviObjects_ObjectIdentity = ObjectIdentity
hpicfSaviObjects = _HpicfSaviObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1)
)
_HpicfSaviObjectsPortTable_Object = MibTable
hpicfSaviObjectsPortTable = _HpicfSaviObjectsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfSaviObjectsPortTable.setStatus("current")
_HpicfSaviObjectsPortEntry_Object = MibTableRow
hpicfSaviObjectsPortEntry = _HpicfSaviObjectsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 1, 1)
)
hpicfSaviObjectsPortEntry.setIndexNames(
    (0, "HPICF-SAVI-MIB", "hpicfSaviObjectsPortIPVersion"),
    (0, "HPICF-SAVI-MIB", "hpicfSaviObjectsPortIfIndex"),
)
if mibBuilder.loadTexts:
    hpicfSaviObjectsPortEntry.setStatus("current")
_HpicfSaviObjectsPortIPVersion_Type = InetVersion
_HpicfSaviObjectsPortIPVersion_Object = MibTableColumn
hpicfSaviObjectsPortIPVersion = _HpicfSaviObjectsPortIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 1, 1, 1),
    _HpicfSaviObjectsPortIPVersion_Type()
)
hpicfSaviObjectsPortIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfSaviObjectsPortIPVersion.setStatus("current")
_HpicfSaviObjectsPortIfIndex_Type = InterfaceIndex
_HpicfSaviObjectsPortIfIndex_Object = MibTableColumn
hpicfSaviObjectsPortIfIndex = _HpicfSaviObjectsPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 1, 1, 2),
    _HpicfSaviObjectsPortIfIndex_Type()
)
hpicfSaviObjectsPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfSaviObjectsPortIfIndex.setStatus("current")


class _HpicfSaviObjPortDhcpTrustAttr_Type(Integer32):
    """Custom type hpicfSaviObjPortDhcpTrustAttr based on Integer32"""
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


_HpicfSaviObjPortDhcpTrustAttr_Type.__name__ = "Integer32"
_HpicfSaviObjPortDhcpTrustAttr_Object = MibTableColumn
hpicfSaviObjPortDhcpTrustAttr = _HpicfSaviObjPortDhcpTrustAttr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 1, 1, 3),
    _HpicfSaviObjPortDhcpTrustAttr_Type()
)
hpicfSaviObjPortDhcpTrustAttr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSaviObjPortDhcpTrustAttr.setStatus("current")
_HpicfSaviObjectsPortFilteringNum_Type = Unsigned32
_HpicfSaviObjectsPortFilteringNum_Object = MibTableColumn
hpicfSaviObjectsPortFilteringNum = _HpicfSaviObjectsPortFilteringNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 1, 1, 4),
    _HpicfSaviObjectsPortFilteringNum_Type()
)
hpicfSaviObjectsPortFilteringNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSaviObjectsPortFilteringNum.setStatus("current")
_HpicfSaviObjectsBindingTable_Object = MibTable
hpicfSaviObjectsBindingTable = _HpicfSaviObjectsBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfSaviObjectsBindingTable.setStatus("current")
_HpicfSaviObjectsBindingEntry_Object = MibTableRow
hpicfSaviObjectsBindingEntry = _HpicfSaviObjectsBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 2, 1)
)
hpicfSaviObjectsBindingEntry.setIndexNames(
    (0, "HPICF-SAVI-MIB", "hpicfSaviObjBindingIpAddrType"),
    (0, "HPICF-SAVI-MIB", "hpicfSaviObjectsBindingType"),
    (0, "HPICF-SAVI-MIB", "hpicfSaviObjectsBindingIfIndex"),
    (0, "HPICF-SAVI-MIB", "hpicfSaviObjectsBindingIpAddress"),
)
if mibBuilder.loadTexts:
    hpicfSaviObjectsBindingEntry.setStatus("current")
_HpicfSaviObjBindingIpAddrType_Type = InetAddressType
_HpicfSaviObjBindingIpAddrType_Object = MibTableColumn
hpicfSaviObjBindingIpAddrType = _HpicfSaviObjBindingIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 2, 1, 1),
    _HpicfSaviObjBindingIpAddrType_Type()
)
hpicfSaviObjBindingIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfSaviObjBindingIpAddrType.setStatus("current")


class _HpicfSaviObjectsBindingType_Type(Integer32):
    """Custom type hpicfSaviObjectsBindingType based on Integer32"""
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
        *(("dhcp", 3),
          ("manual", 1),
          ("send", 4),
          ("slaac", 2))
    )


_HpicfSaviObjectsBindingType_Type.__name__ = "Integer32"
_HpicfSaviObjectsBindingType_Object = MibTableColumn
hpicfSaviObjectsBindingType = _HpicfSaviObjectsBindingType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 2, 1, 2),
    _HpicfSaviObjectsBindingType_Type()
)
hpicfSaviObjectsBindingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfSaviObjectsBindingType.setStatus("current")
_HpicfSaviObjectsBindingIfIndex_Type = InterfaceIndex
_HpicfSaviObjectsBindingIfIndex_Object = MibTableColumn
hpicfSaviObjectsBindingIfIndex = _HpicfSaviObjectsBindingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 2, 1, 3),
    _HpicfSaviObjectsBindingIfIndex_Type()
)
hpicfSaviObjectsBindingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfSaviObjectsBindingIfIndex.setStatus("current")


class _HpicfSaviObjectsBindingIpAddress_Type(InetAddress):
    """Custom type hpicfSaviObjectsBindingIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_HpicfSaviObjectsBindingIpAddress_Type.__name__ = "InetAddress"
_HpicfSaviObjectsBindingIpAddress_Object = MibTableColumn
hpicfSaviObjectsBindingIpAddress = _HpicfSaviObjectsBindingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 2, 1, 4),
    _HpicfSaviObjectsBindingIpAddress_Type()
)
hpicfSaviObjectsBindingIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfSaviObjectsBindingIpAddress.setStatus("current")
_HpicfSaviObjectsBindingMacAddr_Type = MacAddress
_HpicfSaviObjectsBindingMacAddr_Object = MibTableColumn
hpicfSaviObjectsBindingMacAddr = _HpicfSaviObjectsBindingMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 2, 1, 5),
    _HpicfSaviObjectsBindingMacAddr_Type()
)
hpicfSaviObjectsBindingMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSaviObjectsBindingMacAddr.setStatus("current")
_HpicfSaviObjectsBindingLifetime_Type = TimeInterval
_HpicfSaviObjectsBindingLifetime_Object = MibTableColumn
hpicfSaviObjectsBindingLifetime = _HpicfSaviObjectsBindingLifetime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 2, 1, 6),
    _HpicfSaviObjectsBindingLifetime_Type()
)
hpicfSaviObjectsBindingLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSaviObjectsBindingLifetime.setStatus("current")
_HpicfSaviObjectsBindingRowStatus_Type = RowStatus
_HpicfSaviObjectsBindingRowStatus_Object = MibTableColumn
hpicfSaviObjectsBindingRowStatus = _HpicfSaviObjectsBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 2, 1, 7),
    _HpicfSaviObjectsBindingRowStatus_Type()
)
hpicfSaviObjectsBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSaviObjectsBindingRowStatus.setStatus("current")
_HpicfSaviObjectsFilteringTable_Object = MibTable
hpicfSaviObjectsFilteringTable = _HpicfSaviObjectsFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfSaviObjectsFilteringTable.setStatus("current")
_HpicfSaviObjectsFilteringEntry_Object = MibTableRow
hpicfSaviObjectsFilteringEntry = _HpicfSaviObjectsFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 3, 1)
)
hpicfSaviObjectsFilteringEntry.setIndexNames(
    (0, "HPICF-SAVI-MIB", "hpicfSaviObjFilteringIpAddrType"),
    (0, "HPICF-SAVI-MIB", "hpicfSaviObjectsFilteringIfIndex"),
    (0, "HPICF-SAVI-MIB", "hpicfSaviObjFilteringIpAddr"),
)
if mibBuilder.loadTexts:
    hpicfSaviObjectsFilteringEntry.setStatus("current")
_HpicfSaviObjFilteringIpAddrType_Type = InetAddressType
_HpicfSaviObjFilteringIpAddrType_Object = MibTableColumn
hpicfSaviObjFilteringIpAddrType = _HpicfSaviObjFilteringIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 3, 1, 1),
    _HpicfSaviObjFilteringIpAddrType_Type()
)
hpicfSaviObjFilteringIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfSaviObjFilteringIpAddrType.setStatus("current")
_HpicfSaviObjectsFilteringIfIndex_Type = InterfaceIndex
_HpicfSaviObjectsFilteringIfIndex_Object = MibTableColumn
hpicfSaviObjectsFilteringIfIndex = _HpicfSaviObjectsFilteringIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 3, 1, 2),
    _HpicfSaviObjectsFilteringIfIndex_Type()
)
hpicfSaviObjectsFilteringIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfSaviObjectsFilteringIfIndex.setStatus("current")


class _HpicfSaviObjFilteringIpAddr_Type(InetAddress):
    """Custom type hpicfSaviObjFilteringIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_HpicfSaviObjFilteringIpAddr_Type.__name__ = "InetAddress"
_HpicfSaviObjFilteringIpAddr_Object = MibTableColumn
hpicfSaviObjFilteringIpAddr = _HpicfSaviObjFilteringIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 3, 1, 3),
    _HpicfSaviObjFilteringIpAddr_Type()
)
hpicfSaviObjFilteringIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfSaviObjFilteringIpAddr.setStatus("current")
_HpicfSaviObjectsFilteringMacAddr_Type = MacAddress
_HpicfSaviObjectsFilteringMacAddr_Object = MibTableColumn
hpicfSaviObjectsFilteringMacAddr = _HpicfSaviObjectsFilteringMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 1, 3, 1, 4),
    _HpicfSaviObjectsFilteringMacAddr_Type()
)
hpicfSaviObjectsFilteringMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSaviObjectsFilteringMacAddr.setStatus("current")
_HpicfSaviConformance_ObjectIdentity = ObjectIdentity
hpicfSaviConformance = _HpicfSaviConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 2)
)
_HpicfSaviCompliances_ObjectIdentity = ObjectIdentity
hpicfSaviCompliances = _HpicfSaviCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 2, 1)
)
_HpicfSaviGroups_ObjectIdentity = ObjectIdentity
hpicfSaviGroups = _HpicfSaviGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 2, 2)
)

# Managed Objects groups

hpicfSaviportGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 2, 2, 1)
)
hpicfSaviportGroup.setObjects(
      *(("HPICF-SAVI-MIB", "hpicfSaviObjPortDhcpTrustAttr"),
        ("HPICF-SAVI-MIB", "hpicfSaviObjectsPortFilteringNum"))
)
if mibBuilder.loadTexts:
    hpicfSaviportGroup.setStatus("current")

hpicfSavibindingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 2, 2, 2)
)
hpicfSavibindingGroup.setObjects(
      *(("HPICF-SAVI-MIB", "hpicfSaviObjectsBindingMacAddr"),
        ("HPICF-SAVI-MIB", "hpicfSaviObjectsBindingLifetime"),
        ("HPICF-SAVI-MIB", "hpicfSaviObjectsBindingRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfSavibindingGroup.setStatus("current")

hpicfSavifilteringGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 2, 2, 3)
)
hpicfSavifilteringGroup.setObjects(
    ("HPICF-SAVI-MIB", "hpicfSaviObjectsFilteringMacAddr")
)
if mibBuilder.loadTexts:
    hpicfSavifilteringGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfSaviCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfSaviCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPICF-SAVI-MIB",
    **{"hpicfSaviMIB": hpicfSaviMIB,
       "hpicfSaviObjects": hpicfSaviObjects,
       "hpicfSaviObjectsPortTable": hpicfSaviObjectsPortTable,
       "hpicfSaviObjectsPortEntry": hpicfSaviObjectsPortEntry,
       "hpicfSaviObjectsPortIPVersion": hpicfSaviObjectsPortIPVersion,
       "hpicfSaviObjectsPortIfIndex": hpicfSaviObjectsPortIfIndex,
       "hpicfSaviObjPortDhcpTrustAttr": hpicfSaviObjPortDhcpTrustAttr,
       "hpicfSaviObjectsPortFilteringNum": hpicfSaviObjectsPortFilteringNum,
       "hpicfSaviObjectsBindingTable": hpicfSaviObjectsBindingTable,
       "hpicfSaviObjectsBindingEntry": hpicfSaviObjectsBindingEntry,
       "hpicfSaviObjBindingIpAddrType": hpicfSaviObjBindingIpAddrType,
       "hpicfSaviObjectsBindingType": hpicfSaviObjectsBindingType,
       "hpicfSaviObjectsBindingIfIndex": hpicfSaviObjectsBindingIfIndex,
       "hpicfSaviObjectsBindingIpAddress": hpicfSaviObjectsBindingIpAddress,
       "hpicfSaviObjectsBindingMacAddr": hpicfSaviObjectsBindingMacAddr,
       "hpicfSaviObjectsBindingLifetime": hpicfSaviObjectsBindingLifetime,
       "hpicfSaviObjectsBindingRowStatus": hpicfSaviObjectsBindingRowStatus,
       "hpicfSaviObjectsFilteringTable": hpicfSaviObjectsFilteringTable,
       "hpicfSaviObjectsFilteringEntry": hpicfSaviObjectsFilteringEntry,
       "hpicfSaviObjFilteringIpAddrType": hpicfSaviObjFilteringIpAddrType,
       "hpicfSaviObjectsFilteringIfIndex": hpicfSaviObjectsFilteringIfIndex,
       "hpicfSaviObjFilteringIpAddr": hpicfSaviObjFilteringIpAddr,
       "hpicfSaviObjectsFilteringMacAddr": hpicfSaviObjectsFilteringMacAddr,
       "hpicfSaviConformance": hpicfSaviConformance,
       "hpicfSaviCompliances": hpicfSaviCompliances,
       "hpicfSaviCompliance": hpicfSaviCompliance,
       "hpicfSaviGroups": hpicfSaviGroups,
       "hpicfSaviportGroup": hpicfSaviportGroup,
       "hpicfSavibindingGroup": hpicfSavibindingGroup,
       "hpicfSavifilteringGroup": hpicfSavifilteringGroup}
)
