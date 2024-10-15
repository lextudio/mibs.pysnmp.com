# SNMP MIB module (H3C-ATM-DXI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-ATM-DXI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:55 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cAtmDxi = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 49)
)
h3cAtmDxi.setRevisions(
        ("2005-04-14 15:18",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cAtmDxiScalarGroup_ObjectIdentity = ObjectIdentity
h3cAtmDxiScalarGroup = _H3cAtmDxiScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 49, 1)
)


class _H3cAtmDxiConfMode_Type(Integer32):
    """Custom type h3cAtmDxiConfMode based on Integer32"""
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


_H3cAtmDxiConfMode_Type.__name__ = "Integer32"
_H3cAtmDxiConfMode_Object = MibScalar
h3cAtmDxiConfMode = _H3cAtmDxiConfMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 49, 1, 1),
    _H3cAtmDxiConfMode_Type()
)
h3cAtmDxiConfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAtmDxiConfMode.setStatus("current")
_H3cAtmDxiIfObjects_ObjectIdentity = ObjectIdentity
h3cAtmDxiIfObjects = _H3cAtmDxiIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 49, 2)
)
_H3cAtmDxiPvcTable_Object = MibTable
h3cAtmDxiPvcTable = _H3cAtmDxiPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 49, 2, 1)
)
if mibBuilder.loadTexts:
    h3cAtmDxiPvcTable.setStatus("current")
_H3cAtmDxiPvcEntry_Object = MibTableRow
h3cAtmDxiPvcEntry = _H3cAtmDxiPvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 49, 2, 1, 1)
)
h3cAtmDxiPvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-ATM-DXI-MIB", "h3cAtmDxiPvcVpi"),
    (0, "H3C-ATM-DXI-MIB", "h3cAtmDxiPvcVci"),
)
if mibBuilder.loadTexts:
    h3cAtmDxiPvcEntry.setStatus("current")


class _H3cAtmDxiPvcVpi_Type(Integer32):
    """Custom type h3cAtmDxiPvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_H3cAtmDxiPvcVpi_Type.__name__ = "Integer32"
_H3cAtmDxiPvcVpi_Object = MibTableColumn
h3cAtmDxiPvcVpi = _H3cAtmDxiPvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 49, 2, 1, 1, 1),
    _H3cAtmDxiPvcVpi_Type()
)
h3cAtmDxiPvcVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAtmDxiPvcVpi.setStatus("current")


class _H3cAtmDxiPvcVci_Type(Integer32):
    """Custom type h3cAtmDxiPvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_H3cAtmDxiPvcVci_Type.__name__ = "Integer32"
_H3cAtmDxiPvcVci_Object = MibTableColumn
h3cAtmDxiPvcVci = _H3cAtmDxiPvcVci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 49, 2, 1, 1, 2),
    _H3cAtmDxiPvcVci_Type()
)
h3cAtmDxiPvcVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAtmDxiPvcVci.setStatus("current")
_H3cAtmDxiPvcDFA_Type = Integer32
_H3cAtmDxiPvcDFA_Object = MibTableColumn
h3cAtmDxiPvcDFA = _H3cAtmDxiPvcDFA_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 49, 2, 1, 1, 3),
    _H3cAtmDxiPvcDFA_Type()
)
h3cAtmDxiPvcDFA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAtmDxiPvcDFA.setStatus("current")


class _H3cAtmDxiPvcEncType_Type(Integer32):
    """Custom type h3cAtmDxiPvcEncType based on Integer32"""
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


_H3cAtmDxiPvcEncType_Type.__name__ = "Integer32"
_H3cAtmDxiPvcEncType_Object = MibTableColumn
h3cAtmDxiPvcEncType = _H3cAtmDxiPvcEncType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 49, 2, 1, 1, 4),
    _H3cAtmDxiPvcEncType_Type()
)
h3cAtmDxiPvcEncType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAtmDxiPvcEncType.setStatus("current")


class _H3cAtmDxiPvcMapCount_Type(Integer32):
    """Custom type h3cAtmDxiPvcMapCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_H3cAtmDxiPvcMapCount_Type.__name__ = "Integer32"
_H3cAtmDxiPvcMapCount_Object = MibTableColumn
h3cAtmDxiPvcMapCount = _H3cAtmDxiPvcMapCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 49, 2, 1, 1, 5),
    _H3cAtmDxiPvcMapCount_Type()
)
h3cAtmDxiPvcMapCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAtmDxiPvcMapCount.setStatus("current")
_H3cAtmDxiPvcRowStatus_Type = RowStatus
_H3cAtmDxiPvcRowStatus_Object = MibTableColumn
h3cAtmDxiPvcRowStatus = _H3cAtmDxiPvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 49, 2, 1, 1, 6),
    _H3cAtmDxiPvcRowStatus_Type()
)
h3cAtmDxiPvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAtmDxiPvcRowStatus.setStatus("current")
_H3cAtmDxiMapTable_Object = MibTable
h3cAtmDxiMapTable = _H3cAtmDxiMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 49, 2, 2)
)
if mibBuilder.loadTexts:
    h3cAtmDxiMapTable.setStatus("current")
_H3cAtmDxiMapEntry_Object = MibTableRow
h3cAtmDxiMapEntry = _H3cAtmDxiMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 49, 2, 2, 1)
)
h3cAtmDxiMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-ATM-DXI-MIB", "h3cAtmDxiMapPeerIpType"),
    (0, "H3C-ATM-DXI-MIB", "h3cAtmDxiMapPeerIp"),
    (0, "H3C-ATM-DXI-MIB", "h3cAtmDxiMapPvcVpi"),
    (0, "H3C-ATM-DXI-MIB", "h3cAtmDxiMapPvcVci"),
    (0, "H3C-ATM-DXI-MIB", "h3cAtmDxiMapType"),
)
if mibBuilder.loadTexts:
    h3cAtmDxiMapEntry.setStatus("current")
_H3cAtmDxiMapPeerIpType_Type = InetAddressType
_H3cAtmDxiMapPeerIpType_Object = MibTableColumn
h3cAtmDxiMapPeerIpType = _H3cAtmDxiMapPeerIpType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 49, 2, 2, 1, 1),
    _H3cAtmDxiMapPeerIpType_Type()
)
h3cAtmDxiMapPeerIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAtmDxiMapPeerIpType.setStatus("current")
_H3cAtmDxiMapPeerIp_Type = InetAddress
_H3cAtmDxiMapPeerIp_Object = MibTableColumn
h3cAtmDxiMapPeerIp = _H3cAtmDxiMapPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 49, 2, 2, 1, 2),
    _H3cAtmDxiMapPeerIp_Type()
)
h3cAtmDxiMapPeerIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAtmDxiMapPeerIp.setStatus("current")


class _H3cAtmDxiMapPvcVpi_Type(Integer32):
    """Custom type h3cAtmDxiMapPvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_H3cAtmDxiMapPvcVpi_Type.__name__ = "Integer32"
_H3cAtmDxiMapPvcVpi_Object = MibTableColumn
h3cAtmDxiMapPvcVpi = _H3cAtmDxiMapPvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 49, 2, 2, 1, 3),
    _H3cAtmDxiMapPvcVpi_Type()
)
h3cAtmDxiMapPvcVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAtmDxiMapPvcVpi.setStatus("current")


class _H3cAtmDxiMapPvcVci_Type(Integer32):
    """Custom type h3cAtmDxiMapPvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_H3cAtmDxiMapPvcVci_Type.__name__ = "Integer32"
_H3cAtmDxiMapPvcVci_Object = MibTableColumn
h3cAtmDxiMapPvcVci = _H3cAtmDxiMapPvcVci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 49, 2, 2, 1, 4),
    _H3cAtmDxiMapPvcVci_Type()
)
h3cAtmDxiMapPvcVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAtmDxiMapPvcVci.setStatus("current")


class _H3cAtmDxiMapType_Type(Integer32):
    """Custom type h3cAtmDxiMapType based on Integer32"""
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


_H3cAtmDxiMapType_Type.__name__ = "Integer32"
_H3cAtmDxiMapType_Object = MibTableColumn
h3cAtmDxiMapType = _H3cAtmDxiMapType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 49, 2, 2, 1, 5),
    _H3cAtmDxiMapType_Type()
)
h3cAtmDxiMapType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAtmDxiMapType.setStatus("current")


class _H3cAtmDxiMapInarpTime_Type(Integer32):
    """Custom type h3cAtmDxiMapInarpTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 10),
    )


_H3cAtmDxiMapInarpTime_Type.__name__ = "Integer32"
_H3cAtmDxiMapInarpTime_Object = MibTableColumn
h3cAtmDxiMapInarpTime = _H3cAtmDxiMapInarpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 49, 2, 2, 1, 6),
    _H3cAtmDxiMapInarpTime_Type()
)
h3cAtmDxiMapInarpTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAtmDxiMapInarpTime.setStatus("current")


class _H3cAtmDxiMapBroEnable_Type(Integer32):
    """Custom type h3cAtmDxiMapBroEnable based on Integer32"""
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


_H3cAtmDxiMapBroEnable_Type.__name__ = "Integer32"
_H3cAtmDxiMapBroEnable_Object = MibTableColumn
h3cAtmDxiMapBroEnable = _H3cAtmDxiMapBroEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 49, 2, 2, 1, 7),
    _H3cAtmDxiMapBroEnable_Type()
)
h3cAtmDxiMapBroEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAtmDxiMapBroEnable.setStatus("current")
_H3cAtmDxiMapRowStatus_Type = RowStatus
_H3cAtmDxiMapRowStatus_Object = MibTableColumn
h3cAtmDxiMapRowStatus = _H3cAtmDxiMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 49, 2, 2, 1, 8),
    _H3cAtmDxiMapRowStatus_Type()
)
h3cAtmDxiMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cAtmDxiMapRowStatus.setStatus("current")
_H3cAtmDxiConformance_ObjectIdentity = ObjectIdentity
h3cAtmDxiConformance = _H3cAtmDxiConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 49, 3)
)
_H3cAtmDxiCompliances_ObjectIdentity = ObjectIdentity
h3cAtmDxiCompliances = _H3cAtmDxiCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 49, 3, 1)
)
_H3cAtmDxiGroup_ObjectIdentity = ObjectIdentity
h3cAtmDxiGroup = _H3cAtmDxiGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 49, 3, 2)
)

# Managed Objects groups

h3cPVCMAPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 49, 3, 2, 1)
)
h3cPVCMAPGroup.setObjects(
      *(("H3C-ATM-DXI-MIB", "h3cAtmDxiPvcDFA"),
        ("H3C-ATM-DXI-MIB", "h3cAtmDxiPvcEncType"),
        ("H3C-ATM-DXI-MIB", "h3cAtmDxiPvcMapCount"),
        ("H3C-ATM-DXI-MIB", "h3cAtmDxiPvcRowStatus"),
        ("H3C-ATM-DXI-MIB", "h3cAtmDxiMapBroEnable"),
        ("H3C-ATM-DXI-MIB", "h3cAtmDxiMapInarpTime"),
        ("H3C-ATM-DXI-MIB", "h3cAtmDxiMapRowStatus"))
)
if mibBuilder.loadTexts:
    h3cPVCMAPGroup.setStatus("current")

h3cAtmDxiGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 49, 3, 2, 2)
)
h3cAtmDxiGeneralGroup.setObjects(
    ("H3C-ATM-DXI-MIB", "h3cAtmDxiConfMode")
)
if mibBuilder.loadTexts:
    h3cAtmDxiGeneralGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

h3cAtmDxiCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 49, 3, 1, 1)
)
if mibBuilder.loadTexts:
    h3cAtmDxiCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-ATM-DXI-MIB",
    **{"h3cAtmDxi": h3cAtmDxi,
       "h3cAtmDxiScalarGroup": h3cAtmDxiScalarGroup,
       "h3cAtmDxiConfMode": h3cAtmDxiConfMode,
       "h3cAtmDxiIfObjects": h3cAtmDxiIfObjects,
       "h3cAtmDxiPvcTable": h3cAtmDxiPvcTable,
       "h3cAtmDxiPvcEntry": h3cAtmDxiPvcEntry,
       "h3cAtmDxiPvcVpi": h3cAtmDxiPvcVpi,
       "h3cAtmDxiPvcVci": h3cAtmDxiPvcVci,
       "h3cAtmDxiPvcDFA": h3cAtmDxiPvcDFA,
       "h3cAtmDxiPvcEncType": h3cAtmDxiPvcEncType,
       "h3cAtmDxiPvcMapCount": h3cAtmDxiPvcMapCount,
       "h3cAtmDxiPvcRowStatus": h3cAtmDxiPvcRowStatus,
       "h3cAtmDxiMapTable": h3cAtmDxiMapTable,
       "h3cAtmDxiMapEntry": h3cAtmDxiMapEntry,
       "h3cAtmDxiMapPeerIpType": h3cAtmDxiMapPeerIpType,
       "h3cAtmDxiMapPeerIp": h3cAtmDxiMapPeerIp,
       "h3cAtmDxiMapPvcVpi": h3cAtmDxiMapPvcVpi,
       "h3cAtmDxiMapPvcVci": h3cAtmDxiMapPvcVci,
       "h3cAtmDxiMapType": h3cAtmDxiMapType,
       "h3cAtmDxiMapInarpTime": h3cAtmDxiMapInarpTime,
       "h3cAtmDxiMapBroEnable": h3cAtmDxiMapBroEnable,
       "h3cAtmDxiMapRowStatus": h3cAtmDxiMapRowStatus,
       "h3cAtmDxiConformance": h3cAtmDxiConformance,
       "h3cAtmDxiCompliances": h3cAtmDxiCompliances,
       "h3cAtmDxiCompliance": h3cAtmDxiCompliance,
       "h3cAtmDxiGroup": h3cAtmDxiGroup,
       "h3cPVCMAPGroup": h3cPVCMAPGroup,
       "h3cAtmDxiGeneralGroup": h3cAtmDxiGeneralGroup}
)
