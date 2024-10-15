# SNMP MIB module (HH3C-ATM-DXI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-ATM-DXI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:30 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hh3cAtmDxi = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 49)
)
hh3cAtmDxi.setRevisions(
        ("2005-04-14 15:18",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cAtmDxiScalarGroup_ObjectIdentity = ObjectIdentity
hh3cAtmDxiScalarGroup = _Hh3cAtmDxiScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 49, 1)
)


class _Hh3cAtmDxiConfMode_Type(Integer32):
    """Custom type hh3cAtmDxiConfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mode1a", 1),
          ("mode1b", 2),
          ("mode2", 3))
    )


_Hh3cAtmDxiConfMode_Type.__name__ = "Integer32"
_Hh3cAtmDxiConfMode_Object = MibScalar
hh3cAtmDxiConfMode = _Hh3cAtmDxiConfMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 49, 1, 1),
    _Hh3cAtmDxiConfMode_Type()
)
hh3cAtmDxiConfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAtmDxiConfMode.setStatus("current")
_Hh3cAtmDxiIfObjects_ObjectIdentity = ObjectIdentity
hh3cAtmDxiIfObjects = _Hh3cAtmDxiIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 49, 2)
)
_Hh3cAtmDxiPvcTable_Object = MibTable
hh3cAtmDxiPvcTable = _Hh3cAtmDxiPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cAtmDxiPvcTable.setStatus("current")
_Hh3cAtmDxiPvcEntry_Object = MibTableRow
hh3cAtmDxiPvcEntry = _Hh3cAtmDxiPvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 1, 1)
)
hh3cAtmDxiPvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-ATM-DXI-MIB", "hh3cAtmDxiPvcVpi"),
    (0, "HH3C-ATM-DXI-MIB", "hh3cAtmDxiPvcVci"),
)
if mibBuilder.loadTexts:
    hh3cAtmDxiPvcEntry.setStatus("current")


class _Hh3cAtmDxiPvcVpi_Type(Integer32):
    """Custom type hh3cAtmDxiPvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Hh3cAtmDxiPvcVpi_Type.__name__ = "Integer32"
_Hh3cAtmDxiPvcVpi_Object = MibTableColumn
hh3cAtmDxiPvcVpi = _Hh3cAtmDxiPvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 1, 1, 1),
    _Hh3cAtmDxiPvcVpi_Type()
)
hh3cAtmDxiPvcVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAtmDxiPvcVpi.setStatus("current")


class _Hh3cAtmDxiPvcVci_Type(Integer32):
    """Custom type hh3cAtmDxiPvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Hh3cAtmDxiPvcVci_Type.__name__ = "Integer32"
_Hh3cAtmDxiPvcVci_Object = MibTableColumn
hh3cAtmDxiPvcVci = _Hh3cAtmDxiPvcVci_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 1, 1, 2),
    _Hh3cAtmDxiPvcVci_Type()
)
hh3cAtmDxiPvcVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAtmDxiPvcVci.setStatus("current")
_Hh3cAtmDxiPvcDFA_Type = Integer32
_Hh3cAtmDxiPvcDFA_Object = MibTableColumn
hh3cAtmDxiPvcDFA = _Hh3cAtmDxiPvcDFA_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 1, 1, 3),
    _Hh3cAtmDxiPvcDFA_Type()
)
hh3cAtmDxiPvcDFA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAtmDxiPvcDFA.setStatus("current")


class _Hh3cAtmDxiPvcEncType_Type(Integer32):
    """Custom type hh3cAtmDxiPvcEncType based on Integer32"""
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
        *(("mux", 3),
          ("nlpid", 2),
          ("snap", 1))
    )


_Hh3cAtmDxiPvcEncType_Type.__name__ = "Integer32"
_Hh3cAtmDxiPvcEncType_Object = MibTableColumn
hh3cAtmDxiPvcEncType = _Hh3cAtmDxiPvcEncType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 1, 1, 4),
    _Hh3cAtmDxiPvcEncType_Type()
)
hh3cAtmDxiPvcEncType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAtmDxiPvcEncType.setStatus("current")


class _Hh3cAtmDxiPvcMapCount_Type(Integer32):
    """Custom type hh3cAtmDxiPvcMapCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Hh3cAtmDxiPvcMapCount_Type.__name__ = "Integer32"
_Hh3cAtmDxiPvcMapCount_Object = MibTableColumn
hh3cAtmDxiPvcMapCount = _Hh3cAtmDxiPvcMapCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 1, 1, 5),
    _Hh3cAtmDxiPvcMapCount_Type()
)
hh3cAtmDxiPvcMapCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAtmDxiPvcMapCount.setStatus("current")
_Hh3cAtmDxiPvcRowStatus_Type = RowStatus
_Hh3cAtmDxiPvcRowStatus_Object = MibTableColumn
hh3cAtmDxiPvcRowStatus = _Hh3cAtmDxiPvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 1, 1, 6),
    _Hh3cAtmDxiPvcRowStatus_Type()
)
hh3cAtmDxiPvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAtmDxiPvcRowStatus.setStatus("current")
_Hh3cAtmDxiMapTable_Object = MibTable
hh3cAtmDxiMapTable = _Hh3cAtmDxiMapTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cAtmDxiMapTable.setStatus("current")
_Hh3cAtmDxiMapEntry_Object = MibTableRow
hh3cAtmDxiMapEntry = _Hh3cAtmDxiMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 2, 1)
)
hh3cAtmDxiMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-ATM-DXI-MIB", "hh3cAtmDxiMapPeerIpType"),
    (0, "HH3C-ATM-DXI-MIB", "hh3cAtmDxiMapPeerIp"),
    (0, "HH3C-ATM-DXI-MIB", "hh3cAtmDxiMapPvcVpi"),
    (0, "HH3C-ATM-DXI-MIB", "hh3cAtmDxiMapPvcVci"),
    (0, "HH3C-ATM-DXI-MIB", "hh3cAtmDxiMapType"),
)
if mibBuilder.loadTexts:
    hh3cAtmDxiMapEntry.setStatus("current")
_Hh3cAtmDxiMapPeerIpType_Type = InetAddressType
_Hh3cAtmDxiMapPeerIpType_Object = MibTableColumn
hh3cAtmDxiMapPeerIpType = _Hh3cAtmDxiMapPeerIpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 2, 1, 1),
    _Hh3cAtmDxiMapPeerIpType_Type()
)
hh3cAtmDxiMapPeerIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAtmDxiMapPeerIpType.setStatus("current")
_Hh3cAtmDxiMapPeerIp_Type = InetAddress
_Hh3cAtmDxiMapPeerIp_Object = MibTableColumn
hh3cAtmDxiMapPeerIp = _Hh3cAtmDxiMapPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 2, 1, 2),
    _Hh3cAtmDxiMapPeerIp_Type()
)
hh3cAtmDxiMapPeerIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAtmDxiMapPeerIp.setStatus("current")


class _Hh3cAtmDxiMapPvcVpi_Type(Integer32):
    """Custom type hh3cAtmDxiMapPvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Hh3cAtmDxiMapPvcVpi_Type.__name__ = "Integer32"
_Hh3cAtmDxiMapPvcVpi_Object = MibTableColumn
hh3cAtmDxiMapPvcVpi = _Hh3cAtmDxiMapPvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 2, 1, 3),
    _Hh3cAtmDxiMapPvcVpi_Type()
)
hh3cAtmDxiMapPvcVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAtmDxiMapPvcVpi.setStatus("current")


class _Hh3cAtmDxiMapPvcVci_Type(Integer32):
    """Custom type hh3cAtmDxiMapPvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Hh3cAtmDxiMapPvcVci_Type.__name__ = "Integer32"
_Hh3cAtmDxiMapPvcVci_Object = MibTableColumn
hh3cAtmDxiMapPvcVci = _Hh3cAtmDxiMapPvcVci_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 2, 1, 4),
    _Hh3cAtmDxiMapPvcVci_Type()
)
hh3cAtmDxiMapPvcVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAtmDxiMapPvcVci.setStatus("current")


class _Hh3cAtmDxiMapType_Type(Integer32):
    """Custom type hh3cAtmDxiMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("address", 1),
          ("default", 3),
          ("inarp", 2))
    )


_Hh3cAtmDxiMapType_Type.__name__ = "Integer32"
_Hh3cAtmDxiMapType_Object = MibTableColumn
hh3cAtmDxiMapType = _Hh3cAtmDxiMapType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 2, 1, 5),
    _Hh3cAtmDxiMapType_Type()
)
hh3cAtmDxiMapType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAtmDxiMapType.setStatus("current")


class _Hh3cAtmDxiMapInarpTime_Type(Integer32):
    """Custom type hh3cAtmDxiMapInarpTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 10),
    )


_Hh3cAtmDxiMapInarpTime_Type.__name__ = "Integer32"
_Hh3cAtmDxiMapInarpTime_Object = MibTableColumn
hh3cAtmDxiMapInarpTime = _Hh3cAtmDxiMapInarpTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 2, 1, 6),
    _Hh3cAtmDxiMapInarpTime_Type()
)
hh3cAtmDxiMapInarpTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAtmDxiMapInarpTime.setStatus("current")


class _Hh3cAtmDxiMapBroEnable_Type(Integer32):
    """Custom type hh3cAtmDxiMapBroEnable based on Integer32"""
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


_Hh3cAtmDxiMapBroEnable_Type.__name__ = "Integer32"
_Hh3cAtmDxiMapBroEnable_Object = MibTableColumn
hh3cAtmDxiMapBroEnable = _Hh3cAtmDxiMapBroEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 2, 1, 7),
    _Hh3cAtmDxiMapBroEnable_Type()
)
hh3cAtmDxiMapBroEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAtmDxiMapBroEnable.setStatus("current")
_Hh3cAtmDxiMapRowStatus_Type = RowStatus
_Hh3cAtmDxiMapRowStatus_Object = MibTableColumn
hh3cAtmDxiMapRowStatus = _Hh3cAtmDxiMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 49, 2, 2, 1, 8),
    _Hh3cAtmDxiMapRowStatus_Type()
)
hh3cAtmDxiMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAtmDxiMapRowStatus.setStatus("current")
_Hh3cAtmDxiConformance_ObjectIdentity = ObjectIdentity
hh3cAtmDxiConformance = _Hh3cAtmDxiConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 49, 3)
)
_Hh3cAtmDxiCompliances_ObjectIdentity = ObjectIdentity
hh3cAtmDxiCompliances = _Hh3cAtmDxiCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 49, 3, 1)
)
_Hh3cAtmDxiGroup_ObjectIdentity = ObjectIdentity
hh3cAtmDxiGroup = _Hh3cAtmDxiGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 49, 3, 2)
)

# Managed Objects groups

hh3cPVCMAPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 49, 3, 2, 1)
)
hh3cPVCMAPGroup.setObjects(
      *(("HH3C-ATM-DXI-MIB", "hh3cAtmDxiPvcDFA"),
        ("HH3C-ATM-DXI-MIB", "hh3cAtmDxiPvcEncType"),
        ("HH3C-ATM-DXI-MIB", "hh3cAtmDxiPvcMapCount"),
        ("HH3C-ATM-DXI-MIB", "hh3cAtmDxiPvcRowStatus"),
        ("HH3C-ATM-DXI-MIB", "hh3cAtmDxiMapBroEnable"),
        ("HH3C-ATM-DXI-MIB", "hh3cAtmDxiMapInarpTime"),
        ("HH3C-ATM-DXI-MIB", "hh3cAtmDxiMapRowStatus"))
)
if mibBuilder.loadTexts:
    hh3cPVCMAPGroup.setStatus("current")

hh3cAtmDxiGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 49, 3, 2, 2)
)
hh3cAtmDxiGeneralGroup.setObjects(
    ("HH3C-ATM-DXI-MIB", "hh3cAtmDxiConfMode")
)
if mibBuilder.loadTexts:
    hh3cAtmDxiGeneralGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hh3cAtmDxiCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 2, 49, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cAtmDxiCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-ATM-DXI-MIB",
    **{"hh3cAtmDxi": hh3cAtmDxi,
       "hh3cAtmDxiScalarGroup": hh3cAtmDxiScalarGroup,
       "hh3cAtmDxiConfMode": hh3cAtmDxiConfMode,
       "hh3cAtmDxiIfObjects": hh3cAtmDxiIfObjects,
       "hh3cAtmDxiPvcTable": hh3cAtmDxiPvcTable,
       "hh3cAtmDxiPvcEntry": hh3cAtmDxiPvcEntry,
       "hh3cAtmDxiPvcVpi": hh3cAtmDxiPvcVpi,
       "hh3cAtmDxiPvcVci": hh3cAtmDxiPvcVci,
       "hh3cAtmDxiPvcDFA": hh3cAtmDxiPvcDFA,
       "hh3cAtmDxiPvcEncType": hh3cAtmDxiPvcEncType,
       "hh3cAtmDxiPvcMapCount": hh3cAtmDxiPvcMapCount,
       "hh3cAtmDxiPvcRowStatus": hh3cAtmDxiPvcRowStatus,
       "hh3cAtmDxiMapTable": hh3cAtmDxiMapTable,
       "hh3cAtmDxiMapEntry": hh3cAtmDxiMapEntry,
       "hh3cAtmDxiMapPeerIpType": hh3cAtmDxiMapPeerIpType,
       "hh3cAtmDxiMapPeerIp": hh3cAtmDxiMapPeerIp,
       "hh3cAtmDxiMapPvcVpi": hh3cAtmDxiMapPvcVpi,
       "hh3cAtmDxiMapPvcVci": hh3cAtmDxiMapPvcVci,
       "hh3cAtmDxiMapType": hh3cAtmDxiMapType,
       "hh3cAtmDxiMapInarpTime": hh3cAtmDxiMapInarpTime,
       "hh3cAtmDxiMapBroEnable": hh3cAtmDxiMapBroEnable,
       "hh3cAtmDxiMapRowStatus": hh3cAtmDxiMapRowStatus,
       "hh3cAtmDxiConformance": hh3cAtmDxiConformance,
       "hh3cAtmDxiCompliances": hh3cAtmDxiCompliances,
       "hh3cAtmDxiCompliance": hh3cAtmDxiCompliance,
       "hh3cAtmDxiGroup": hh3cAtmDxiGroup,
       "hh3cPVCMAPGroup": hh3cPVCMAPGroup,
       "hh3cAtmDxiGeneralGroup": hh3cAtmDxiGeneralGroup}
)
