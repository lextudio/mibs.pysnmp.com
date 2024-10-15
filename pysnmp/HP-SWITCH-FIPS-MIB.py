# SNMP MIB module (HP-SWITCH-FIPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-SWITCH-FIPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:03 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

hpSwitchFipSnoopingMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78)
)
hpSwitchFipSnoopingMib.setRevisions(
        ("2010-06-03 15:39",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpSwitchFipsConfigObjects_ObjectIdentity = ObjectIdentity
hpSwitchFipsConfigObjects = _HpSwitchFipsConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 1)
)
_HpSwitchFipsScalars_ObjectIdentity = ObjectIdentity
hpSwitchFipsScalars = _HpSwitchFipsScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 1, 1)
)


class _HpSwitchFipsAdminStatus_Type(Integer32):
    """Custom type hpSwitchFipsAdminStatus based on Integer32"""
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


_HpSwitchFipsAdminStatus_Type.__name__ = "Integer32"
_HpSwitchFipsAdminStatus_Object = MibScalar
hpSwitchFipsAdminStatus = _HpSwitchFipsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 1, 1, 1),
    _HpSwitchFipsAdminStatus_Type()
)
hpSwitchFipsAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchFipsAdminStatus.setStatus("current")
_HpSwitchFipsTables_ObjectIdentity = ObjectIdentity
hpSwitchFipsTables = _HpSwitchFipsTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 1, 2)
)
_HpSwitchFipsFcMapTable_Object = MibTable
hpSwitchFipsFcMapTable = _HpSwitchFipsFcMapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpSwitchFipsFcMapTable.setStatus("current")
_HpSwitchFipsFcMapEntry_Object = MibTableRow
hpSwitchFipsFcMapEntry = _HpSwitchFipsFcMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 1, 2, 1, 1)
)
hpSwitchFipsFcMapEntry.setIndexNames(
    (0, "HP-SWITCH-FIPS-MIB", "hpSwitchFipsFcMapIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchFipsFcMapEntry.setStatus("current")


class _HpSwitchFipsFcMapIndex_Type(Integer32):
    """Custom type hpSwitchFipsFcMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HpSwitchFipsFcMapIndex_Type.__name__ = "Integer32"
_HpSwitchFipsFcMapIndex_Object = MibTableColumn
hpSwitchFipsFcMapIndex = _HpSwitchFipsFcMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 1, 2, 1, 1, 1),
    _HpSwitchFipsFcMapIndex_Type()
)
hpSwitchFipsFcMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchFipsFcMapIndex.setStatus("current")


class _HpSwitchFipsFcMap_Type(OctetString):
    """Custom type hpSwitchFipsFcMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_HpSwitchFipsFcMap_Type.__name__ = "OctetString"
_HpSwitchFipsFcMap_Object = MibTableColumn
hpSwitchFipsFcMap = _HpSwitchFipsFcMap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 1, 2, 1, 1, 2),
    _HpSwitchFipsFcMap_Type()
)
hpSwitchFipsFcMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchFipsFcMap.setStatus("current")
_HpSwitchFipsFcfMacAddressTable_Object = MibTable
hpSwitchFipsFcfMacAddressTable = _HpSwitchFipsFcfMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hpSwitchFipsFcfMacAddressTable.setStatus("current")
_HpSwitchFipsFcfMacAddressEntry_Object = MibTableRow
hpSwitchFipsFcfMacAddressEntry = _HpSwitchFipsFcfMacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 1, 2, 2, 1)
)
hpSwitchFipsFcfMacAddressEntry.setIndexNames(
    (0, "HP-SWITCH-FIPS-MIB", "hpSwitchFipsVirtualFabricInterfaceIndex"),
    (0, "HP-SWITCH-FIPS-MIB", "hpSwitchFipsFcfMacAddress"),
)
if mibBuilder.loadTexts:
    hpSwitchFipsFcfMacAddressEntry.setStatus("current")
_HpSwitchFipsVirtualFabricInterfaceIndex_Type = InterfaceIndex
_HpSwitchFipsVirtualFabricInterfaceIndex_Object = MibTableColumn
hpSwitchFipsVirtualFabricInterfaceIndex = _HpSwitchFipsVirtualFabricInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 1, 2, 2, 1, 1),
    _HpSwitchFipsVirtualFabricInterfaceIndex_Type()
)
hpSwitchFipsVirtualFabricInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchFipsVirtualFabricInterfaceIndex.setStatus("current")
_HpSwitchFipsFcfMacAddress_Type = MacAddress
_HpSwitchFipsFcfMacAddress_Object = MibTableColumn
hpSwitchFipsFcfMacAddress = _HpSwitchFipsFcfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 1, 2, 2, 1, 2),
    _HpSwitchFipsFcfMacAddress_Type()
)
hpSwitchFipsFcfMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchFipsFcfMacAddress.setStatus("current")
_HpSwitchFipsFcoeVlanId_Type = Integer32
_HpSwitchFipsFcoeVlanId_Object = MibTableColumn
hpSwitchFipsFcoeVlanId = _HpSwitchFipsFcoeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 1, 2, 2, 1, 3),
    _HpSwitchFipsFcoeVlanId_Type()
)
hpSwitchFipsFcoeVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFipsFcoeVlanId.setStatus("current")


class _HpSwitchFipsFcfFcMap_Type(OctetString):
    """Custom type hpSwitchFipsFcfFcMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_HpSwitchFipsFcfFcMap_Type.__name__ = "OctetString"
_HpSwitchFipsFcfFcMap_Object = MibTableColumn
hpSwitchFipsFcfFcMap = _HpSwitchFipsFcfFcMap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 1, 2, 2, 1, 4),
    _HpSwitchFipsFcfFcMap_Type()
)
hpSwitchFipsFcfFcMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFipsFcfFcMap.setStatus("current")
_HpSwitchFipsFcfEnodeLoginCount_Type = Integer32
_HpSwitchFipsFcfEnodeLoginCount_Object = MibTableColumn
hpSwitchFipsFcfEnodeLoginCount = _HpSwitchFipsFcfEnodeLoginCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 1, 2, 2, 1, 5),
    _HpSwitchFipsFcfEnodeLoginCount_Type()
)
hpSwitchFipsFcfEnodeLoginCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFipsFcfEnodeLoginCount.setStatus("current")


class _HpSwitchFipsFcfNameId_Type(OctetString):
    """Custom type hpSwitchFipsFcfNameId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HpSwitchFipsFcfNameId_Type.__name__ = "OctetString"
_HpSwitchFipsFcfNameId_Object = MibTableColumn
hpSwitchFipsFcfNameId = _HpSwitchFipsFcfNameId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 1, 2, 2, 1, 6),
    _HpSwitchFipsFcfNameId_Type()
)
hpSwitchFipsFcfNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFipsFcfNameId.setStatus("current")


class _HpSwitchFipsFabricName_Type(OctetString):
    """Custom type hpSwitchFipsFabricName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HpSwitchFipsFabricName_Type.__name__ = "OctetString"
_HpSwitchFipsFabricName_Object = MibTableColumn
hpSwitchFipsFabricName = _HpSwitchFipsFabricName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 1, 2, 2, 1, 7),
    _HpSwitchFipsFabricName_Type()
)
hpSwitchFipsFabricName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFipsFabricName.setStatus("current")
_HpSwitchFipsFcfMacTableRowStatus_Type = RowStatus
_HpSwitchFipsFcfMacTableRowStatus_Object = MibTableColumn
hpSwitchFipsFcfMacTableRowStatus = _HpSwitchFipsFcfMacTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 1, 2, 2, 1, 8),
    _HpSwitchFipsFcfMacTableRowStatus_Type()
)
hpSwitchFipsFcfMacTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchFipsFcfMacTableRowStatus.setStatus("current")
_HpSwitchFipsSessionTable_Object = MibTable
hpSwitchFipsSessionTable = _HpSwitchFipsSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hpSwitchFipsSessionTable.setStatus("current")
_HpSwitchFipsSessionEntry_Object = MibTableRow
hpSwitchFipsSessionEntry = _HpSwitchFipsSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 1, 2, 3, 1)
)
hpSwitchFipsSessionEntry.setIndexNames(
    (0, "HP-SWITCH-FIPS-MIB", "hpSwitchFipsSessEnodeInterfaceIndex"),
    (0, "HP-SWITCH-FIPS-MIB", "hpSwitchFipsSessEnodeFPMAMacAddress"),
)
if mibBuilder.loadTexts:
    hpSwitchFipsSessionEntry.setStatus("current")
_HpSwitchFipsSessEnodeInterfaceIndex_Type = InterfaceIndex
_HpSwitchFipsSessEnodeInterfaceIndex_Object = MibTableColumn
hpSwitchFipsSessEnodeInterfaceIndex = _HpSwitchFipsSessEnodeInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 1, 2, 3, 1, 1),
    _HpSwitchFipsSessEnodeInterfaceIndex_Type()
)
hpSwitchFipsSessEnodeInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchFipsSessEnodeInterfaceIndex.setStatus("current")
_HpSwitchFipsSessEnodeFPMAMacAddress_Type = MacAddress
_HpSwitchFipsSessEnodeFPMAMacAddress_Object = MibTableColumn
hpSwitchFipsSessEnodeFPMAMacAddress = _HpSwitchFipsSessEnodeFPMAMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 1, 2, 3, 1, 2),
    _HpSwitchFipsSessEnodeFPMAMacAddress_Type()
)
hpSwitchFipsSessEnodeFPMAMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchFipsSessEnodeFPMAMacAddress.setStatus("current")
_HpSwitchFipsSessEnodeMacAddress_Type = MacAddress
_HpSwitchFipsSessEnodeMacAddress_Object = MibTableColumn
hpSwitchFipsSessEnodeMacAddress = _HpSwitchFipsSessEnodeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 1, 2, 3, 1, 3),
    _HpSwitchFipsSessEnodeMacAddress_Type()
)
hpSwitchFipsSessEnodeMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFipsSessEnodeMacAddress.setStatus("current")


class _HpSwitchFipsSessEnodeNportId_Type(OctetString):
    """Custom type hpSwitchFipsSessEnodeNportId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_HpSwitchFipsSessEnodeNportId_Type.__name__ = "OctetString"
_HpSwitchFipsSessEnodeNportId_Object = MibTableColumn
hpSwitchFipsSessEnodeNportId = _HpSwitchFipsSessEnodeNportId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 1, 2, 3, 1, 4),
    _HpSwitchFipsSessEnodeNportId_Type()
)
hpSwitchFipsSessEnodeNportId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFipsSessEnodeNportId.setStatus("current")


class _HpSwitchFipsSessEnodeNportIdType_Type(Integer32):
    """Custom type hpSwitchFipsSessEnodeNportIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flogi", 1),
          ("npivfdisc", 2))
    )


_HpSwitchFipsSessEnodeNportIdType_Type.__name__ = "Integer32"
_HpSwitchFipsSessEnodeNportIdType_Object = MibTableColumn
hpSwitchFipsSessEnodeNportIdType = _HpSwitchFipsSessEnodeNportIdType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 1, 2, 3, 1, 5),
    _HpSwitchFipsSessEnodeNportIdType_Type()
)
hpSwitchFipsSessEnodeNportIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFipsSessEnodeNportIdType.setStatus("current")
_HpSwitchFipsSessFcfMacAddress_Type = MacAddress
_HpSwitchFipsSessFcfMacAddress_Object = MibTableColumn
hpSwitchFipsSessFcfMacAddress = _HpSwitchFipsSessFcfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 1, 2, 3, 1, 6),
    _HpSwitchFipsSessFcfMacAddress_Type()
)
hpSwitchFipsSessFcfMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFipsSessFcfMacAddress.setStatus("current")


class _HpSwitchFipsSessFcMap_Type(OctetString):
    """Custom type hpSwitchFipsSessFcMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_HpSwitchFipsSessFcMap_Type.__name__ = "OctetString"
_HpSwitchFipsSessFcMap_Object = MibTableColumn
hpSwitchFipsSessFcMap = _HpSwitchFipsSessFcMap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 1, 2, 3, 1, 7),
    _HpSwitchFipsSessFcMap_Type()
)
hpSwitchFipsSessFcMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFipsSessFcMap.setStatus("current")
_HpSwitchFipsSessVlanId_Type = Integer32
_HpSwitchFipsSessVlanId_Object = MibTableColumn
hpSwitchFipsSessVlanId = _HpSwitchFipsSessVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 1, 2, 3, 1, 8),
    _HpSwitchFipsSessVlanId_Type()
)
hpSwitchFipsSessVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFipsSessVlanId.setStatus("current")


class _HpSwitchFipsSessFcfNameId_Type(OctetString):
    """Custom type hpSwitchFipsSessFcfNameId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HpSwitchFipsSessFcfNameId_Type.__name__ = "OctetString"
_HpSwitchFipsSessFcfNameId_Object = MibTableColumn
hpSwitchFipsSessFcfNameId = _HpSwitchFipsSessFcfNameId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 1, 2, 3, 1, 9),
    _HpSwitchFipsSessFcfNameId_Type()
)
hpSwitchFipsSessFcfNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFipsSessFcfNameId.setStatus("current")
_HpSwitchFipsStatistics_ObjectIdentity = ObjectIdentity
hpSwitchFipsStatistics = _HpSwitchFipsStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 2)
)
_HpSwitchFipsGlobalStats_ObjectIdentity = ObjectIdentity
hpSwitchFipsGlobalStats = _HpSwitchFipsGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 2, 1)
)
_HpSwitchFipsFipDropPkts_Type = Counter64
_HpSwitchFipsFipDropPkts_Object = MibScalar
hpSwitchFipsFipDropPkts = _HpSwitchFipsFipDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 2, 1, 1),
    _HpSwitchFipsFipDropPkts_Type()
)
hpSwitchFipsFipDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFipsFipDropPkts.setStatus("current")
_HpSwitchFipsFcoeDropPkts_Type = Counter64
_HpSwitchFipsFcoeDropPkts_Object = MibScalar
hpSwitchFipsFcoeDropPkts = _HpSwitchFipsFcoeDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 2, 1, 2),
    _HpSwitchFipsFcoeDropPkts_Type()
)
hpSwitchFipsFcoeDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFipsFcoeDropPkts.setStatus("current")
_HpSwitchFipsSessStats_ObjectIdentity = ObjectIdentity
hpSwitchFipsSessStats = _HpSwitchFipsSessStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 2, 2)
)
_HpSwitchFipsSessStatsTable_Object = MibTable
hpSwitchFipsSessStatsTable = _HpSwitchFipsSessStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpSwitchFipsSessStatsTable.setStatus("current")
_HpSwitchFipsSessStatsEntry_Object = MibTableRow
hpSwitchFipsSessStatsEntry = _HpSwitchFipsSessStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 2, 2, 1, 1)
)
hpSwitchFipsSessStatsEntry.setIndexNames(
    (0, "HP-SWITCH-FIPS-MIB", "hpSwitchFipsStatsSessEnodeIfIndex"),
    (0, "HP-SWITCH-FIPS-MIB", "hpSwitchFipsStatsSessFPMAMacAddress"),
)
if mibBuilder.loadTexts:
    hpSwitchFipsSessStatsEntry.setStatus("current")
_HpSwitchFipsStatsSessEnodeIfIndex_Type = InterfaceIndex
_HpSwitchFipsStatsSessEnodeIfIndex_Object = MibTableColumn
hpSwitchFipsStatsSessEnodeIfIndex = _HpSwitchFipsStatsSessEnodeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 2, 2, 1, 1, 1),
    _HpSwitchFipsStatsSessEnodeIfIndex_Type()
)
hpSwitchFipsStatsSessEnodeIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchFipsStatsSessEnodeIfIndex.setStatus("current")
_HpSwitchFipsStatsSessFPMAMacAddress_Type = MacAddress
_HpSwitchFipsStatsSessFPMAMacAddress_Object = MibTableColumn
hpSwitchFipsStatsSessFPMAMacAddress = _HpSwitchFipsStatsSessFPMAMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 2, 2, 1, 1, 2),
    _HpSwitchFipsStatsSessFPMAMacAddress_Type()
)
hpSwitchFipsStatsSessFPMAMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchFipsStatsSessFPMAMacAddress.setStatus("current")
_HpSwitchFipsStatsSessFcfMacAddress_Type = MacAddress
_HpSwitchFipsStatsSessFcfMacAddress_Object = MibTableColumn
hpSwitchFipsStatsSessFcfMacAddress = _HpSwitchFipsStatsSessFcfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 2, 2, 1, 1, 3),
    _HpSwitchFipsStatsSessFcfMacAddress_Type()
)
hpSwitchFipsStatsSessFcfMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFipsStatsSessFcfMacAddress.setStatus("current")
_HpSwitchFipsStatsSessFcoePermitPkts_Type = Counter64
_HpSwitchFipsStatsSessFcoePermitPkts_Object = MibTableColumn
hpSwitchFipsStatsSessFcoePermitPkts = _HpSwitchFipsStatsSessFcoePermitPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 2, 2, 1, 1, 4),
    _HpSwitchFipsStatsSessFcoePermitPkts_Type()
)
hpSwitchFipsStatsSessFcoePermitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchFipsStatsSessFcoePermitPkts.setStatus("current")
_HpSwitchFipsConformance_ObjectIdentity = ObjectIdentity
hpSwitchFipsConformance = _HpSwitchFipsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 3)
)
_HpSwitchFipsCompliances_ObjectIdentity = ObjectIdentity
hpSwitchFipsCompliances = _HpSwitchFipsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 3, 1)
)
_HpSwitchFipsGroups_ObjectIdentity = ObjectIdentity
hpSwitchFipsGroups = _HpSwitchFipsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 3, 2)
)

# Managed Objects groups

hpSwitchFipsConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 3, 2, 1)
)
hpSwitchFipsConfigGroup.setObjects(
      *(("HP-SWITCH-FIPS-MIB", "hpSwitchFipsAdminStatus"),
        ("HP-SWITCH-FIPS-MIB", "hpSwitchFipsFcMap"),
        ("HP-SWITCH-FIPS-MIB", "hpSwitchFipsFcoeVlanId"),
        ("HP-SWITCH-FIPS-MIB", "hpSwitchFipsFcfFcMap"),
        ("HP-SWITCH-FIPS-MIB", "hpSwitchFipsFcfEnodeLoginCount"),
        ("HP-SWITCH-FIPS-MIB", "hpSwitchFipsFcfNameId"),
        ("HP-SWITCH-FIPS-MIB", "hpSwitchFipsFabricName"),
        ("HP-SWITCH-FIPS-MIB", "hpSwitchFipsFcfMacTableRowStatus"))
)
if mibBuilder.loadTexts:
    hpSwitchFipsConfigGroup.setStatus("current")

hpSwitchFipsSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 3, 2, 2)
)
hpSwitchFipsSessionGroup.setObjects(
      *(("HP-SWITCH-FIPS-MIB", "hpSwitchFipsSessEnodeMacAddress"),
        ("HP-SWITCH-FIPS-MIB", "hpSwitchFipsSessEnodeNportId"),
        ("HP-SWITCH-FIPS-MIB", "hpSwitchFipsSessEnodeNportIdType"),
        ("HP-SWITCH-FIPS-MIB", "hpSwitchFipsSessFcfMacAddress"),
        ("HP-SWITCH-FIPS-MIB", "hpSwitchFipsSessFcMap"),
        ("HP-SWITCH-FIPS-MIB", "hpSwitchFipsSessVlanId"),
        ("HP-SWITCH-FIPS-MIB", "hpSwitchFipsSessFcfNameId"))
)
if mibBuilder.loadTexts:
    hpSwitchFipsSessionGroup.setStatus("current")

hpSwitchFipsStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 3, 2, 3)
)
hpSwitchFipsStatisticsGroup.setObjects(
      *(("HP-SWITCH-FIPS-MIB", "hpSwitchFipsFipDropPkts"),
        ("HP-SWITCH-FIPS-MIB", "hpSwitchFipsFcoeDropPkts"),
        ("HP-SWITCH-FIPS-MIB", "hpSwitchFipsStatsSessFcfMacAddress"),
        ("HP-SWITCH-FIPS-MIB", "hpSwitchFipsStatsSessFcoePermitPkts"))
)
if mibBuilder.loadTexts:
    hpSwitchFipsStatisticsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpSwitchFipsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 78, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpSwitchFipsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-SWITCH-FIPS-MIB",
    **{"hpSwitchFipSnoopingMib": hpSwitchFipSnoopingMib,
       "hpSwitchFipsConfigObjects": hpSwitchFipsConfigObjects,
       "hpSwitchFipsScalars": hpSwitchFipsScalars,
       "hpSwitchFipsAdminStatus": hpSwitchFipsAdminStatus,
       "hpSwitchFipsTables": hpSwitchFipsTables,
       "hpSwitchFipsFcMapTable": hpSwitchFipsFcMapTable,
       "hpSwitchFipsFcMapEntry": hpSwitchFipsFcMapEntry,
       "hpSwitchFipsFcMapIndex": hpSwitchFipsFcMapIndex,
       "hpSwitchFipsFcMap": hpSwitchFipsFcMap,
       "hpSwitchFipsFcfMacAddressTable": hpSwitchFipsFcfMacAddressTable,
       "hpSwitchFipsFcfMacAddressEntry": hpSwitchFipsFcfMacAddressEntry,
       "hpSwitchFipsVirtualFabricInterfaceIndex": hpSwitchFipsVirtualFabricInterfaceIndex,
       "hpSwitchFipsFcfMacAddress": hpSwitchFipsFcfMacAddress,
       "hpSwitchFipsFcoeVlanId": hpSwitchFipsFcoeVlanId,
       "hpSwitchFipsFcfFcMap": hpSwitchFipsFcfFcMap,
       "hpSwitchFipsFcfEnodeLoginCount": hpSwitchFipsFcfEnodeLoginCount,
       "hpSwitchFipsFcfNameId": hpSwitchFipsFcfNameId,
       "hpSwitchFipsFabricName": hpSwitchFipsFabricName,
       "hpSwitchFipsFcfMacTableRowStatus": hpSwitchFipsFcfMacTableRowStatus,
       "hpSwitchFipsSessionTable": hpSwitchFipsSessionTable,
       "hpSwitchFipsSessionEntry": hpSwitchFipsSessionEntry,
       "hpSwitchFipsSessEnodeInterfaceIndex": hpSwitchFipsSessEnodeInterfaceIndex,
       "hpSwitchFipsSessEnodeFPMAMacAddress": hpSwitchFipsSessEnodeFPMAMacAddress,
       "hpSwitchFipsSessEnodeMacAddress": hpSwitchFipsSessEnodeMacAddress,
       "hpSwitchFipsSessEnodeNportId": hpSwitchFipsSessEnodeNportId,
       "hpSwitchFipsSessEnodeNportIdType": hpSwitchFipsSessEnodeNportIdType,
       "hpSwitchFipsSessFcfMacAddress": hpSwitchFipsSessFcfMacAddress,
       "hpSwitchFipsSessFcMap": hpSwitchFipsSessFcMap,
       "hpSwitchFipsSessVlanId": hpSwitchFipsSessVlanId,
       "hpSwitchFipsSessFcfNameId": hpSwitchFipsSessFcfNameId,
       "hpSwitchFipsStatistics": hpSwitchFipsStatistics,
       "hpSwitchFipsGlobalStats": hpSwitchFipsGlobalStats,
       "hpSwitchFipsFipDropPkts": hpSwitchFipsFipDropPkts,
       "hpSwitchFipsFcoeDropPkts": hpSwitchFipsFcoeDropPkts,
       "hpSwitchFipsSessStats": hpSwitchFipsSessStats,
       "hpSwitchFipsSessStatsTable": hpSwitchFipsSessStatsTable,
       "hpSwitchFipsSessStatsEntry": hpSwitchFipsSessStatsEntry,
       "hpSwitchFipsStatsSessEnodeIfIndex": hpSwitchFipsStatsSessEnodeIfIndex,
       "hpSwitchFipsStatsSessFPMAMacAddress": hpSwitchFipsStatsSessFPMAMacAddress,
       "hpSwitchFipsStatsSessFcfMacAddress": hpSwitchFipsStatsSessFcfMacAddress,
       "hpSwitchFipsStatsSessFcoePermitPkts": hpSwitchFipsStatsSessFcoePermitPkts,
       "hpSwitchFipsConformance": hpSwitchFipsConformance,
       "hpSwitchFipsCompliances": hpSwitchFipsCompliances,
       "hpSwitchFipsCompliance": hpSwitchFipsCompliance,
       "hpSwitchFipsGroups": hpSwitchFipsGroups,
       "hpSwitchFipsConfigGroup": hpSwitchFipsConfigGroup,
       "hpSwitchFipsSessionGroup": hpSwitchFipsSessionGroup,
       "hpSwitchFipsStatisticsGroup": hpSwitchFipsStatisticsGroup}
)
