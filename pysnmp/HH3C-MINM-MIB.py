# SNMP MIB module (HH3C-MINM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-MINM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:07 2024
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

(hh3cVsiIndex,) = mibBuilder.importSymbols(
    "HH3C-VSI-MIB",
    "hh3cVsiIndex")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hh3cMinm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 107)
)
hh3cMinm.setRevisions(
        ("2009-08-08 10:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cMinmEnabledStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cMinmObjects_ObjectIdentity = ObjectIdentity
hh3cMinmObjects = _Hh3cMinmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 107, 1)
)
_Hh3cMinmScalarGroup_ObjectIdentity = ObjectIdentity
hh3cMinmScalarGroup = _Hh3cMinmScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 107, 1, 1)
)


class _Hh3cMinmCapabilities_Type(Bits):
    """Custom type hh3cMinmCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("reEncapsulation", 0),
          ("uplink", 1),
          ("vsiShareConnection", 2))
    )

_Hh3cMinmCapabilities_Type.__name__ = "Bits"
_Hh3cMinmCapabilities_Object = MibScalar
hh3cMinmCapabilities = _Hh3cMinmCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 107, 1, 1, 1),
    _Hh3cMinmCapabilities_Type()
)
hh3cMinmCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMinmCapabilities.setStatus("current")
_Hh3cMinmBmac_Type = MacAddress
_Hh3cMinmBmac_Object = MibScalar
hh3cMinmBmac = _Hh3cMinmBmac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 107, 1, 1, 2),
    _Hh3cMinmBmac_Type()
)
hh3cMinmBmac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMinmBmac.setStatus("current")
_Hh3cMinmVsiTable_Object = MibTable
hh3cMinmVsiTable = _Hh3cMinmVsiTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 107, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cMinmVsiTable.setStatus("current")
_Hh3cMinmVsiEntry_Object = MibTableRow
hh3cMinmVsiEntry = _Hh3cMinmVsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 107, 1, 2, 1)
)
hh3cMinmVsiEntry.setIndexNames(
    (0, "HH3C-VSI-MIB", "hh3cVsiIndex"),
)
if mibBuilder.loadTexts:
    hh3cMinmVsiEntry.setStatus("current")


class _Hh3cMinmVsiBvlan_Type(Integer32):
    """Custom type hh3cMinmVsiBvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cMinmVsiBvlan_Type.__name__ = "Integer32"
_Hh3cMinmVsiBvlan_Object = MibTableColumn
hh3cMinmVsiBvlan = _Hh3cMinmVsiBvlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 107, 1, 2, 1, 1),
    _Hh3cMinmVsiBvlan_Type()
)
hh3cMinmVsiBvlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMinmVsiBvlan.setStatus("current")
_Hh3cMinmVsiReEncapsulation_Type = Hh3cMinmEnabledStatus
_Hh3cMinmVsiReEncapsulation_Object = MibTableColumn
hh3cMinmVsiReEncapsulation = _Hh3cMinmVsiReEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 107, 1, 2, 1, 2),
    _Hh3cMinmVsiReEncapsulation_Type()
)
hh3cMinmVsiReEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMinmVsiReEncapsulation.setStatus("current")
_Hh3cMinmVsiNextAvailableLinkId_Type = Unsigned32
_Hh3cMinmVsiNextAvailableLinkId_Object = MibTableColumn
hh3cMinmVsiNextAvailableLinkId = _Hh3cMinmVsiNextAvailableLinkId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 107, 1, 2, 1, 3),
    _Hh3cMinmVsiNextAvailableLinkId_Type()
)
hh3cMinmVsiNextAvailableLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMinmVsiNextAvailableLinkId.setStatus("current")
_Hh3cMinmUplinkTable_Object = MibTable
hh3cMinmUplinkTable = _Hh3cMinmUplinkTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 107, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cMinmUplinkTable.setStatus("current")
_Hh3cMinmUplinkEntry_Object = MibTableRow
hh3cMinmUplinkEntry = _Hh3cMinmUplinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 107, 1, 3, 1)
)
hh3cMinmUplinkEntry.setIndexNames(
    (0, "HH3C-VSI-MIB", "hh3cVsiIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cMinmUplinkEntry.setStatus("current")
_Hh3cMinmUplinkRowStatus_Type = RowStatus
_Hh3cMinmUplinkRowStatus_Object = MibTableColumn
hh3cMinmUplinkRowStatus = _Hh3cMinmUplinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 107, 1, 3, 1, 1),
    _Hh3cMinmUplinkRowStatus_Type()
)
hh3cMinmUplinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMinmUplinkRowStatus.setStatus("current")
_Hh3cMinmConnectionTable_Object = MibTable
hh3cMinmConnectionTable = _Hh3cMinmConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 107, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cMinmConnectionTable.setStatus("current")
_Hh3cMinmConnectionEntry_Object = MibTableRow
hh3cMinmConnectionEntry = _Hh3cMinmConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 107, 1, 4, 1)
)
hh3cMinmConnectionEntry.setIndexNames(
    (0, "HH3C-VSI-MIB", "hh3cVsiIndex"),
    (0, "HH3C-MINM-MIB", "hh3cMinmConnectionLinkId"),
)
if mibBuilder.loadTexts:
    hh3cMinmConnectionEntry.setStatus("current")
_Hh3cMinmConnectionLinkId_Type = Unsigned32
_Hh3cMinmConnectionLinkId_Object = MibTableColumn
hh3cMinmConnectionLinkId = _Hh3cMinmConnectionLinkId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 107, 1, 4, 1, 1),
    _Hh3cMinmConnectionLinkId_Type()
)
hh3cMinmConnectionLinkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMinmConnectionLinkId.setStatus("current")
_Hh3cMinmConnectionBmac_Type = MacAddress
_Hh3cMinmConnectionBmac_Object = MibTableColumn
hh3cMinmConnectionBmac = _Hh3cMinmConnectionBmac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 107, 1, 4, 1, 2),
    _Hh3cMinmConnectionBmac_Type()
)
hh3cMinmConnectionBmac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMinmConnectionBmac.setStatus("current")


class _Hh3cMinmConnectionBvlan_Type(Integer32):
    """Custom type hh3cMinmConnectionBvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cMinmConnectionBvlan_Type.__name__ = "Integer32"
_Hh3cMinmConnectionBvlan_Object = MibTableColumn
hh3cMinmConnectionBvlan = _Hh3cMinmConnectionBvlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 107, 1, 4, 1, 3),
    _Hh3cMinmConnectionBvlan_Type()
)
hh3cMinmConnectionBvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMinmConnectionBvlan.setStatus("current")
_Hh3cMinmConnectionPort_Type = Integer32
_Hh3cMinmConnectionPort_Object = MibTableColumn
hh3cMinmConnectionPort = _Hh3cMinmConnectionPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 107, 1, 4, 1, 4),
    _Hh3cMinmConnectionPort_Type()
)
hh3cMinmConnectionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMinmConnectionPort.setStatus("current")


class _Hh3cMinmConnectionStatus_Type(Integer32):
    """Custom type hh3cMinmConnectionStatus based on Integer32"""
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
        *(("blackhole", 4),
          ("configDynamic", 2),
          ("configStatic", 3),
          ("learned", 1))
    )


_Hh3cMinmConnectionStatus_Type.__name__ = "Integer32"
_Hh3cMinmConnectionStatus_Object = MibTableColumn
hh3cMinmConnectionStatus = _Hh3cMinmConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 107, 1, 4, 1, 5),
    _Hh3cMinmConnectionStatus_Type()
)
hh3cMinmConnectionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMinmConnectionStatus.setStatus("current")


class _Hh3cMinmConnectionAgingStatus_Type(Integer32):
    """Custom type hh3cMinmConnectionAgingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aging", 1),
          ("noAged", 2))
    )


_Hh3cMinmConnectionAgingStatus_Type.__name__ = "Integer32"
_Hh3cMinmConnectionAgingStatus_Object = MibTableColumn
hh3cMinmConnectionAgingStatus = _Hh3cMinmConnectionAgingStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 107, 1, 4, 1, 6),
    _Hh3cMinmConnectionAgingStatus_Type()
)
hh3cMinmConnectionAgingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMinmConnectionAgingStatus.setStatus("current")
_Hh3cMinmConnectionRowStatus_Type = RowStatus
_Hh3cMinmConnectionRowStatus_Object = MibTableColumn
hh3cMinmConnectionRowStatus = _Hh3cMinmConnectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 107, 1, 4, 1, 7),
    _Hh3cMinmConnectionRowStatus_Type()
)
hh3cMinmConnectionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMinmConnectionRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-MINM-MIB",
    **{"Hh3cMinmEnabledStatus": Hh3cMinmEnabledStatus,
       "hh3cMinm": hh3cMinm,
       "hh3cMinmObjects": hh3cMinmObjects,
       "hh3cMinmScalarGroup": hh3cMinmScalarGroup,
       "hh3cMinmCapabilities": hh3cMinmCapabilities,
       "hh3cMinmBmac": hh3cMinmBmac,
       "hh3cMinmVsiTable": hh3cMinmVsiTable,
       "hh3cMinmVsiEntry": hh3cMinmVsiEntry,
       "hh3cMinmVsiBvlan": hh3cMinmVsiBvlan,
       "hh3cMinmVsiReEncapsulation": hh3cMinmVsiReEncapsulation,
       "hh3cMinmVsiNextAvailableLinkId": hh3cMinmVsiNextAvailableLinkId,
       "hh3cMinmUplinkTable": hh3cMinmUplinkTable,
       "hh3cMinmUplinkEntry": hh3cMinmUplinkEntry,
       "hh3cMinmUplinkRowStatus": hh3cMinmUplinkRowStatus,
       "hh3cMinmConnectionTable": hh3cMinmConnectionTable,
       "hh3cMinmConnectionEntry": hh3cMinmConnectionEntry,
       "hh3cMinmConnectionLinkId": hh3cMinmConnectionLinkId,
       "hh3cMinmConnectionBmac": hh3cMinmConnectionBmac,
       "hh3cMinmConnectionBvlan": hh3cMinmConnectionBvlan,
       "hh3cMinmConnectionPort": hh3cMinmConnectionPort,
       "hh3cMinmConnectionStatus": hh3cMinmConnectionStatus,
       "hh3cMinmConnectionAgingStatus": hh3cMinmConnectionAgingStatus,
       "hh3cMinmConnectionRowStatus": hh3cMinmConnectionRowStatus}
)
