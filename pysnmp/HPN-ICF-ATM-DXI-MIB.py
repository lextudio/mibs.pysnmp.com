# SNMP MIB module (HPN-ICF-ATM-DXI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-ATM-DXI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:30 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfAtmDxi = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 49)
)
hpnicfAtmDxi.setRevisions(
        ("2005-04-14 15:18",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfAtmDxiScalarGroup_ObjectIdentity = ObjectIdentity
hpnicfAtmDxiScalarGroup = _HpnicfAtmDxiScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 49, 1)
)


class _HpnicfAtmDxiConfMode_Type(Integer32):
    """Custom type hpnicfAtmDxiConfMode based on Integer32"""
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


_HpnicfAtmDxiConfMode_Type.__name__ = "Integer32"
_HpnicfAtmDxiConfMode_Object = MibScalar
hpnicfAtmDxiConfMode = _HpnicfAtmDxiConfMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 49, 1, 1),
    _HpnicfAtmDxiConfMode_Type()
)
hpnicfAtmDxiConfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAtmDxiConfMode.setStatus("current")
_HpnicfAtmDxiIfObjects_ObjectIdentity = ObjectIdentity
hpnicfAtmDxiIfObjects = _HpnicfAtmDxiIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 49, 2)
)
_HpnicfAtmDxiPvcTable_Object = MibTable
hpnicfAtmDxiPvcTable = _HpnicfAtmDxiPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 49, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfAtmDxiPvcTable.setStatus("current")
_HpnicfAtmDxiPvcEntry_Object = MibTableRow
hpnicfAtmDxiPvcEntry = _HpnicfAtmDxiPvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 49, 2, 1, 1)
)
hpnicfAtmDxiPvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-ATM-DXI-MIB", "hpnicfAtmDxiPvcVpi"),
    (0, "HPN-ICF-ATM-DXI-MIB", "hpnicfAtmDxiPvcVci"),
)
if mibBuilder.loadTexts:
    hpnicfAtmDxiPvcEntry.setStatus("current")


class _HpnicfAtmDxiPvcVpi_Type(Integer32):
    """Custom type hpnicfAtmDxiPvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HpnicfAtmDxiPvcVpi_Type.__name__ = "Integer32"
_HpnicfAtmDxiPvcVpi_Object = MibTableColumn
hpnicfAtmDxiPvcVpi = _HpnicfAtmDxiPvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 49, 2, 1, 1, 1),
    _HpnicfAtmDxiPvcVpi_Type()
)
hpnicfAtmDxiPvcVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAtmDxiPvcVpi.setStatus("current")


class _HpnicfAtmDxiPvcVci_Type(Integer32):
    """Custom type hpnicfAtmDxiPvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HpnicfAtmDxiPvcVci_Type.__name__ = "Integer32"
_HpnicfAtmDxiPvcVci_Object = MibTableColumn
hpnicfAtmDxiPvcVci = _HpnicfAtmDxiPvcVci_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 49, 2, 1, 1, 2),
    _HpnicfAtmDxiPvcVci_Type()
)
hpnicfAtmDxiPvcVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAtmDxiPvcVci.setStatus("current")
_HpnicfAtmDxiPvcDFA_Type = Integer32
_HpnicfAtmDxiPvcDFA_Object = MibTableColumn
hpnicfAtmDxiPvcDFA = _HpnicfAtmDxiPvcDFA_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 49, 2, 1, 1, 3),
    _HpnicfAtmDxiPvcDFA_Type()
)
hpnicfAtmDxiPvcDFA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAtmDxiPvcDFA.setStatus("current")


class _HpnicfAtmDxiPvcEncType_Type(Integer32):
    """Custom type hpnicfAtmDxiPvcEncType based on Integer32"""
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


_HpnicfAtmDxiPvcEncType_Type.__name__ = "Integer32"
_HpnicfAtmDxiPvcEncType_Object = MibTableColumn
hpnicfAtmDxiPvcEncType = _HpnicfAtmDxiPvcEncType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 49, 2, 1, 1, 4),
    _HpnicfAtmDxiPvcEncType_Type()
)
hpnicfAtmDxiPvcEncType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAtmDxiPvcEncType.setStatus("current")


class _HpnicfAtmDxiPvcMapCount_Type(Integer32):
    """Custom type hpnicfAtmDxiPvcMapCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_HpnicfAtmDxiPvcMapCount_Type.__name__ = "Integer32"
_HpnicfAtmDxiPvcMapCount_Object = MibTableColumn
hpnicfAtmDxiPvcMapCount = _HpnicfAtmDxiPvcMapCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 49, 2, 1, 1, 5),
    _HpnicfAtmDxiPvcMapCount_Type()
)
hpnicfAtmDxiPvcMapCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAtmDxiPvcMapCount.setStatus("current")
_HpnicfAtmDxiPvcRowStatus_Type = RowStatus
_HpnicfAtmDxiPvcRowStatus_Object = MibTableColumn
hpnicfAtmDxiPvcRowStatus = _HpnicfAtmDxiPvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 49, 2, 1, 1, 6),
    _HpnicfAtmDxiPvcRowStatus_Type()
)
hpnicfAtmDxiPvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAtmDxiPvcRowStatus.setStatus("current")
_HpnicfAtmDxiMapTable_Object = MibTable
hpnicfAtmDxiMapTable = _HpnicfAtmDxiMapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 49, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfAtmDxiMapTable.setStatus("current")
_HpnicfAtmDxiMapEntry_Object = MibTableRow
hpnicfAtmDxiMapEntry = _HpnicfAtmDxiMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 49, 2, 2, 1)
)
hpnicfAtmDxiMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-ATM-DXI-MIB", "hpnicfAtmDxiMapPeerIpType"),
    (0, "HPN-ICF-ATM-DXI-MIB", "hpnicfAtmDxiMapPeerIp"),
    (0, "HPN-ICF-ATM-DXI-MIB", "hpnicfAtmDxiMapPvcVpi"),
    (0, "HPN-ICF-ATM-DXI-MIB", "hpnicfAtmDxiMapPvcVci"),
    (0, "HPN-ICF-ATM-DXI-MIB", "hpnicfAtmDxiMapType"),
)
if mibBuilder.loadTexts:
    hpnicfAtmDxiMapEntry.setStatus("current")
_HpnicfAtmDxiMapPeerIpType_Type = InetAddressType
_HpnicfAtmDxiMapPeerIpType_Object = MibTableColumn
hpnicfAtmDxiMapPeerIpType = _HpnicfAtmDxiMapPeerIpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 49, 2, 2, 1, 1),
    _HpnicfAtmDxiMapPeerIpType_Type()
)
hpnicfAtmDxiMapPeerIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAtmDxiMapPeerIpType.setStatus("current")
_HpnicfAtmDxiMapPeerIp_Type = InetAddress
_HpnicfAtmDxiMapPeerIp_Object = MibTableColumn
hpnicfAtmDxiMapPeerIp = _HpnicfAtmDxiMapPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 49, 2, 2, 1, 2),
    _HpnicfAtmDxiMapPeerIp_Type()
)
hpnicfAtmDxiMapPeerIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAtmDxiMapPeerIp.setStatus("current")


class _HpnicfAtmDxiMapPvcVpi_Type(Integer32):
    """Custom type hpnicfAtmDxiMapPvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HpnicfAtmDxiMapPvcVpi_Type.__name__ = "Integer32"
_HpnicfAtmDxiMapPvcVpi_Object = MibTableColumn
hpnicfAtmDxiMapPvcVpi = _HpnicfAtmDxiMapPvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 49, 2, 2, 1, 3),
    _HpnicfAtmDxiMapPvcVpi_Type()
)
hpnicfAtmDxiMapPvcVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAtmDxiMapPvcVpi.setStatus("current")


class _HpnicfAtmDxiMapPvcVci_Type(Integer32):
    """Custom type hpnicfAtmDxiMapPvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HpnicfAtmDxiMapPvcVci_Type.__name__ = "Integer32"
_HpnicfAtmDxiMapPvcVci_Object = MibTableColumn
hpnicfAtmDxiMapPvcVci = _HpnicfAtmDxiMapPvcVci_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 49, 2, 2, 1, 4),
    _HpnicfAtmDxiMapPvcVci_Type()
)
hpnicfAtmDxiMapPvcVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAtmDxiMapPvcVci.setStatus("current")


class _HpnicfAtmDxiMapType_Type(Integer32):
    """Custom type hpnicfAtmDxiMapType based on Integer32"""
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


_HpnicfAtmDxiMapType_Type.__name__ = "Integer32"
_HpnicfAtmDxiMapType_Object = MibTableColumn
hpnicfAtmDxiMapType = _HpnicfAtmDxiMapType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 49, 2, 2, 1, 5),
    _HpnicfAtmDxiMapType_Type()
)
hpnicfAtmDxiMapType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAtmDxiMapType.setStatus("current")


class _HpnicfAtmDxiMapInarpTime_Type(Integer32):
    """Custom type hpnicfAtmDxiMapInarpTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 10),
    )


_HpnicfAtmDxiMapInarpTime_Type.__name__ = "Integer32"
_HpnicfAtmDxiMapInarpTime_Object = MibTableColumn
hpnicfAtmDxiMapInarpTime = _HpnicfAtmDxiMapInarpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 49, 2, 2, 1, 6),
    _HpnicfAtmDxiMapInarpTime_Type()
)
hpnicfAtmDxiMapInarpTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAtmDxiMapInarpTime.setStatus("current")


class _HpnicfAtmDxiMapBroEnable_Type(Integer32):
    """Custom type hpnicfAtmDxiMapBroEnable based on Integer32"""
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


_HpnicfAtmDxiMapBroEnable_Type.__name__ = "Integer32"
_HpnicfAtmDxiMapBroEnable_Object = MibTableColumn
hpnicfAtmDxiMapBroEnable = _HpnicfAtmDxiMapBroEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 49, 2, 2, 1, 7),
    _HpnicfAtmDxiMapBroEnable_Type()
)
hpnicfAtmDxiMapBroEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAtmDxiMapBroEnable.setStatus("current")
_HpnicfAtmDxiMapRowStatus_Type = RowStatus
_HpnicfAtmDxiMapRowStatus_Object = MibTableColumn
hpnicfAtmDxiMapRowStatus = _HpnicfAtmDxiMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 49, 2, 2, 1, 8),
    _HpnicfAtmDxiMapRowStatus_Type()
)
hpnicfAtmDxiMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfAtmDxiMapRowStatus.setStatus("current")
_HpnicfAtmDxiConformance_ObjectIdentity = ObjectIdentity
hpnicfAtmDxiConformance = _HpnicfAtmDxiConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 49, 3)
)
_HpnicfAtmDxiCompliances_ObjectIdentity = ObjectIdentity
hpnicfAtmDxiCompliances = _HpnicfAtmDxiCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 49, 3, 1)
)
_HpnicfAtmDxiGroup_ObjectIdentity = ObjectIdentity
hpnicfAtmDxiGroup = _HpnicfAtmDxiGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 49, 3, 2)
)

# Managed Objects groups

hpnicfPVCMAPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 49, 3, 2, 1)
)
hpnicfPVCMAPGroup.setObjects(
      *(("HPN-ICF-ATM-DXI-MIB", "hpnicfAtmDxiPvcDFA"),
        ("HPN-ICF-ATM-DXI-MIB", "hpnicfAtmDxiPvcEncType"),
        ("HPN-ICF-ATM-DXI-MIB", "hpnicfAtmDxiPvcMapCount"),
        ("HPN-ICF-ATM-DXI-MIB", "hpnicfAtmDxiPvcRowStatus"),
        ("HPN-ICF-ATM-DXI-MIB", "hpnicfAtmDxiMapBroEnable"),
        ("HPN-ICF-ATM-DXI-MIB", "hpnicfAtmDxiMapInarpTime"),
        ("HPN-ICF-ATM-DXI-MIB", "hpnicfAtmDxiMapRowStatus"))
)
if mibBuilder.loadTexts:
    hpnicfPVCMAPGroup.setStatus("current")

hpnicfAtmDxiGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 49, 3, 2, 2)
)
hpnicfAtmDxiGeneralGroup.setObjects(
    ("HPN-ICF-ATM-DXI-MIB", "hpnicfAtmDxiConfMode")
)
if mibBuilder.loadTexts:
    hpnicfAtmDxiGeneralGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpnicfAtmDxiCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 49, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfAtmDxiCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-ATM-DXI-MIB",
    **{"hpnicfAtmDxi": hpnicfAtmDxi,
       "hpnicfAtmDxiScalarGroup": hpnicfAtmDxiScalarGroup,
       "hpnicfAtmDxiConfMode": hpnicfAtmDxiConfMode,
       "hpnicfAtmDxiIfObjects": hpnicfAtmDxiIfObjects,
       "hpnicfAtmDxiPvcTable": hpnicfAtmDxiPvcTable,
       "hpnicfAtmDxiPvcEntry": hpnicfAtmDxiPvcEntry,
       "hpnicfAtmDxiPvcVpi": hpnicfAtmDxiPvcVpi,
       "hpnicfAtmDxiPvcVci": hpnicfAtmDxiPvcVci,
       "hpnicfAtmDxiPvcDFA": hpnicfAtmDxiPvcDFA,
       "hpnicfAtmDxiPvcEncType": hpnicfAtmDxiPvcEncType,
       "hpnicfAtmDxiPvcMapCount": hpnicfAtmDxiPvcMapCount,
       "hpnicfAtmDxiPvcRowStatus": hpnicfAtmDxiPvcRowStatus,
       "hpnicfAtmDxiMapTable": hpnicfAtmDxiMapTable,
       "hpnicfAtmDxiMapEntry": hpnicfAtmDxiMapEntry,
       "hpnicfAtmDxiMapPeerIpType": hpnicfAtmDxiMapPeerIpType,
       "hpnicfAtmDxiMapPeerIp": hpnicfAtmDxiMapPeerIp,
       "hpnicfAtmDxiMapPvcVpi": hpnicfAtmDxiMapPvcVpi,
       "hpnicfAtmDxiMapPvcVci": hpnicfAtmDxiMapPvcVci,
       "hpnicfAtmDxiMapType": hpnicfAtmDxiMapType,
       "hpnicfAtmDxiMapInarpTime": hpnicfAtmDxiMapInarpTime,
       "hpnicfAtmDxiMapBroEnable": hpnicfAtmDxiMapBroEnable,
       "hpnicfAtmDxiMapRowStatus": hpnicfAtmDxiMapRowStatus,
       "hpnicfAtmDxiConformance": hpnicfAtmDxiConformance,
       "hpnicfAtmDxiCompliances": hpnicfAtmDxiCompliances,
       "hpnicfAtmDxiCompliance": hpnicfAtmDxiCompliance,
       "hpnicfAtmDxiGroup": hpnicfAtmDxiGroup,
       "hpnicfPVCMAPGroup": hpnicfPVCMAPGroup,
       "hpnicfAtmDxiGeneralGroup": hpnicfAtmDxiGeneralGroup}
)
