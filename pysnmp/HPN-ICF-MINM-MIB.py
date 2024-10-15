# SNMP MIB module (HPN-ICF-MINM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-MINM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:06 2024
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

(hpnicfVsiIndex,) = mibBuilder.importSymbols(
    "HPN-ICF-VSI-MIB",
    "hpnicfVsiIndex")

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

hpnicfMinm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107)
)
hpnicfMinm.setRevisions(
        ("2009-08-08 10:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfMinmEnabledStatus(Integer32, TextualConvention):
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

_HpnicfMinmObjects_ObjectIdentity = ObjectIdentity
hpnicfMinmObjects = _HpnicfMinmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1)
)
_HpnicfMinmScalarGroup_ObjectIdentity = ObjectIdentity
hpnicfMinmScalarGroup = _HpnicfMinmScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 1)
)


class _HpnicfMinmCapabilities_Type(Bits):
    """Custom type hpnicfMinmCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("reEncapsulation", 0),
          ("uplink", 1),
          ("vsiShareConnection", 2))
    )

_HpnicfMinmCapabilities_Type.__name__ = "Bits"
_HpnicfMinmCapabilities_Object = MibScalar
hpnicfMinmCapabilities = _HpnicfMinmCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 1, 1),
    _HpnicfMinmCapabilities_Type()
)
hpnicfMinmCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMinmCapabilities.setStatus("current")
_HpnicfMinmBmac_Type = MacAddress
_HpnicfMinmBmac_Object = MibScalar
hpnicfMinmBmac = _HpnicfMinmBmac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 1, 2),
    _HpnicfMinmBmac_Type()
)
hpnicfMinmBmac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMinmBmac.setStatus("current")
_HpnicfMinmVsiTable_Object = MibTable
hpnicfMinmVsiTable = _HpnicfMinmVsiTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfMinmVsiTable.setStatus("current")
_HpnicfMinmVsiEntry_Object = MibTableRow
hpnicfMinmVsiEntry = _HpnicfMinmVsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 2, 1)
)
hpnicfMinmVsiEntry.setIndexNames(
    (0, "HPN-ICF-VSI-MIB", "hpnicfVsiIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMinmVsiEntry.setStatus("current")


class _HpnicfMinmVsiBvlan_Type(Integer32):
    """Custom type hpnicfMinmVsiBvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_HpnicfMinmVsiBvlan_Type.__name__ = "Integer32"
_HpnicfMinmVsiBvlan_Object = MibTableColumn
hpnicfMinmVsiBvlan = _HpnicfMinmVsiBvlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 2, 1, 1),
    _HpnicfMinmVsiBvlan_Type()
)
hpnicfMinmVsiBvlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMinmVsiBvlan.setStatus("current")
_HpnicfMinmVsiReEncapsulation_Type = HpnicfMinmEnabledStatus
_HpnicfMinmVsiReEncapsulation_Object = MibTableColumn
hpnicfMinmVsiReEncapsulation = _HpnicfMinmVsiReEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 2, 1, 2),
    _HpnicfMinmVsiReEncapsulation_Type()
)
hpnicfMinmVsiReEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMinmVsiReEncapsulation.setStatus("current")
_HpnicfMinmVsiNextAvailableLinkId_Type = Unsigned32
_HpnicfMinmVsiNextAvailableLinkId_Object = MibTableColumn
hpnicfMinmVsiNextAvailableLinkId = _HpnicfMinmVsiNextAvailableLinkId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 2, 1, 3),
    _HpnicfMinmVsiNextAvailableLinkId_Type()
)
hpnicfMinmVsiNextAvailableLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMinmVsiNextAvailableLinkId.setStatus("current")
_HpnicfMinmUplinkTable_Object = MibTable
hpnicfMinmUplinkTable = _HpnicfMinmUplinkTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfMinmUplinkTable.setStatus("current")
_HpnicfMinmUplinkEntry_Object = MibTableRow
hpnicfMinmUplinkEntry = _HpnicfMinmUplinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 3, 1)
)
hpnicfMinmUplinkEntry.setIndexNames(
    (0, "HPN-ICF-VSI-MIB", "hpnicfVsiIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMinmUplinkEntry.setStatus("current")
_HpnicfMinmUplinkRowStatus_Type = RowStatus
_HpnicfMinmUplinkRowStatus_Object = MibTableColumn
hpnicfMinmUplinkRowStatus = _HpnicfMinmUplinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 3, 1, 1),
    _HpnicfMinmUplinkRowStatus_Type()
)
hpnicfMinmUplinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMinmUplinkRowStatus.setStatus("current")
_HpnicfMinmConnectionTable_Object = MibTable
hpnicfMinmConnectionTable = _HpnicfMinmConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfMinmConnectionTable.setStatus("current")
_HpnicfMinmConnectionEntry_Object = MibTableRow
hpnicfMinmConnectionEntry = _HpnicfMinmConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 4, 1)
)
hpnicfMinmConnectionEntry.setIndexNames(
    (0, "HPN-ICF-VSI-MIB", "hpnicfVsiIndex"),
    (0, "HPN-ICF-MINM-MIB", "hpnicfMinmConnectionLinkId"),
)
if mibBuilder.loadTexts:
    hpnicfMinmConnectionEntry.setStatus("current")
_HpnicfMinmConnectionLinkId_Type = Unsigned32
_HpnicfMinmConnectionLinkId_Object = MibTableColumn
hpnicfMinmConnectionLinkId = _HpnicfMinmConnectionLinkId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 4, 1, 1),
    _HpnicfMinmConnectionLinkId_Type()
)
hpnicfMinmConnectionLinkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMinmConnectionLinkId.setStatus("current")
_HpnicfMinmConnectionBmac_Type = MacAddress
_HpnicfMinmConnectionBmac_Object = MibTableColumn
hpnicfMinmConnectionBmac = _HpnicfMinmConnectionBmac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 4, 1, 2),
    _HpnicfMinmConnectionBmac_Type()
)
hpnicfMinmConnectionBmac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMinmConnectionBmac.setStatus("current")


class _HpnicfMinmConnectionBvlan_Type(Integer32):
    """Custom type hpnicfMinmConnectionBvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpnicfMinmConnectionBvlan_Type.__name__ = "Integer32"
_HpnicfMinmConnectionBvlan_Object = MibTableColumn
hpnicfMinmConnectionBvlan = _HpnicfMinmConnectionBvlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 4, 1, 3),
    _HpnicfMinmConnectionBvlan_Type()
)
hpnicfMinmConnectionBvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMinmConnectionBvlan.setStatus("current")
_HpnicfMinmConnectionPort_Type = Integer32
_HpnicfMinmConnectionPort_Object = MibTableColumn
hpnicfMinmConnectionPort = _HpnicfMinmConnectionPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 4, 1, 4),
    _HpnicfMinmConnectionPort_Type()
)
hpnicfMinmConnectionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMinmConnectionPort.setStatus("current")


class _HpnicfMinmConnectionStatus_Type(Integer32):
    """Custom type hpnicfMinmConnectionStatus based on Integer32"""
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


_HpnicfMinmConnectionStatus_Type.__name__ = "Integer32"
_HpnicfMinmConnectionStatus_Object = MibTableColumn
hpnicfMinmConnectionStatus = _HpnicfMinmConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 4, 1, 5),
    _HpnicfMinmConnectionStatus_Type()
)
hpnicfMinmConnectionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMinmConnectionStatus.setStatus("current")


class _HpnicfMinmConnectionAgingStatus_Type(Integer32):
    """Custom type hpnicfMinmConnectionAgingStatus based on Integer32"""
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


_HpnicfMinmConnectionAgingStatus_Type.__name__ = "Integer32"
_HpnicfMinmConnectionAgingStatus_Object = MibTableColumn
hpnicfMinmConnectionAgingStatus = _HpnicfMinmConnectionAgingStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 4, 1, 6),
    _HpnicfMinmConnectionAgingStatus_Type()
)
hpnicfMinmConnectionAgingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMinmConnectionAgingStatus.setStatus("current")
_HpnicfMinmConnectionRowStatus_Type = RowStatus
_HpnicfMinmConnectionRowStatus_Object = MibTableColumn
hpnicfMinmConnectionRowStatus = _HpnicfMinmConnectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 107, 1, 4, 1, 7),
    _HpnicfMinmConnectionRowStatus_Type()
)
hpnicfMinmConnectionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMinmConnectionRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-MINM-MIB",
    **{"HpnicfMinmEnabledStatus": HpnicfMinmEnabledStatus,
       "hpnicfMinm": hpnicfMinm,
       "hpnicfMinmObjects": hpnicfMinmObjects,
       "hpnicfMinmScalarGroup": hpnicfMinmScalarGroup,
       "hpnicfMinmCapabilities": hpnicfMinmCapabilities,
       "hpnicfMinmBmac": hpnicfMinmBmac,
       "hpnicfMinmVsiTable": hpnicfMinmVsiTable,
       "hpnicfMinmVsiEntry": hpnicfMinmVsiEntry,
       "hpnicfMinmVsiBvlan": hpnicfMinmVsiBvlan,
       "hpnicfMinmVsiReEncapsulation": hpnicfMinmVsiReEncapsulation,
       "hpnicfMinmVsiNextAvailableLinkId": hpnicfMinmVsiNextAvailableLinkId,
       "hpnicfMinmUplinkTable": hpnicfMinmUplinkTable,
       "hpnicfMinmUplinkEntry": hpnicfMinmUplinkEntry,
       "hpnicfMinmUplinkRowStatus": hpnicfMinmUplinkRowStatus,
       "hpnicfMinmConnectionTable": hpnicfMinmConnectionTable,
       "hpnicfMinmConnectionEntry": hpnicfMinmConnectionEntry,
       "hpnicfMinmConnectionLinkId": hpnicfMinmConnectionLinkId,
       "hpnicfMinmConnectionBmac": hpnicfMinmConnectionBmac,
       "hpnicfMinmConnectionBvlan": hpnicfMinmConnectionBvlan,
       "hpnicfMinmConnectionPort": hpnicfMinmConnectionPort,
       "hpnicfMinmConnectionStatus": hpnicfMinmConnectionStatus,
       "hpnicfMinmConnectionAgingStatus": hpnicfMinmConnectionAgingStatus,
       "hpnicfMinmConnectionRowStatus": hpnicfMinmConnectionRowStatus}
)
