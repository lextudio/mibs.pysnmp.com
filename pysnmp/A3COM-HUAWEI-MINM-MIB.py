# SNMP MIB module (A3COM-HUAWEI-MINM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-MINM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:33 2024
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
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

(h3cVsiIndex,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-VSI-MIB",
    "h3cVsiIndex")

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

h3cMinm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107)
)
h3cMinm.setRevisions(
        ("2009-08-08 10:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cMinmEnabledStatus(Integer32, TextualConvention):
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

_H3cMinmObjects_ObjectIdentity = ObjectIdentity
h3cMinmObjects = _H3cMinmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1)
)
_H3cMinmScalarGroup_ObjectIdentity = ObjectIdentity
h3cMinmScalarGroup = _H3cMinmScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 1)
)


class _H3cMinmCapabilities_Type(Bits):
    """Custom type h3cMinmCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("reEncapsulation", 0),
          ("uplink", 1),
          ("vsiShareConnection", 2))
    )

_H3cMinmCapabilities_Type.__name__ = "Bits"
_H3cMinmCapabilities_Object = MibScalar
h3cMinmCapabilities = _H3cMinmCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 1, 1),
    _H3cMinmCapabilities_Type()
)
h3cMinmCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMinmCapabilities.setStatus("current")
_H3cMinmBmac_Type = MacAddress
_H3cMinmBmac_Object = MibScalar
h3cMinmBmac = _H3cMinmBmac_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 1, 2),
    _H3cMinmBmac_Type()
)
h3cMinmBmac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMinmBmac.setStatus("current")
_H3cMinmVsiTable_Object = MibTable
h3cMinmVsiTable = _H3cMinmVsiTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 2)
)
if mibBuilder.loadTexts:
    h3cMinmVsiTable.setStatus("current")
_H3cMinmVsiEntry_Object = MibTableRow
h3cMinmVsiEntry = _H3cMinmVsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 2, 1)
)
h3cMinmVsiEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VSI-MIB", "h3cVsiIndex"),
)
if mibBuilder.loadTexts:
    h3cMinmVsiEntry.setStatus("current")


class _H3cMinmVsiBvlan_Type(Integer32):
    """Custom type h3cMinmVsiBvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_H3cMinmVsiBvlan_Type.__name__ = "Integer32"
_H3cMinmVsiBvlan_Object = MibTableColumn
h3cMinmVsiBvlan = _H3cMinmVsiBvlan_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 2, 1, 1),
    _H3cMinmVsiBvlan_Type()
)
h3cMinmVsiBvlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMinmVsiBvlan.setStatus("current")
_H3cMinmVsiReEncapsulation_Type = H3cMinmEnabledStatus
_H3cMinmVsiReEncapsulation_Object = MibTableColumn
h3cMinmVsiReEncapsulation = _H3cMinmVsiReEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 2, 1, 2),
    _H3cMinmVsiReEncapsulation_Type()
)
h3cMinmVsiReEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMinmVsiReEncapsulation.setStatus("current")
_H3cMinmVsiNextAvailableLinkId_Type = Unsigned32
_H3cMinmVsiNextAvailableLinkId_Object = MibTableColumn
h3cMinmVsiNextAvailableLinkId = _H3cMinmVsiNextAvailableLinkId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 2, 1, 3),
    _H3cMinmVsiNextAvailableLinkId_Type()
)
h3cMinmVsiNextAvailableLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMinmVsiNextAvailableLinkId.setStatus("current")
_H3cMinmUplinkTable_Object = MibTable
h3cMinmUplinkTable = _H3cMinmUplinkTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 3)
)
if mibBuilder.loadTexts:
    h3cMinmUplinkTable.setStatus("current")
_H3cMinmUplinkEntry_Object = MibTableRow
h3cMinmUplinkEntry = _H3cMinmUplinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 3, 1)
)
h3cMinmUplinkEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VSI-MIB", "h3cVsiIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cMinmUplinkEntry.setStatus("current")
_H3cMinmUplinkRowStatus_Type = RowStatus
_H3cMinmUplinkRowStatus_Object = MibTableColumn
h3cMinmUplinkRowStatus = _H3cMinmUplinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 3, 1, 1),
    _H3cMinmUplinkRowStatus_Type()
)
h3cMinmUplinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMinmUplinkRowStatus.setStatus("current")
_H3cMinmConnectionTable_Object = MibTable
h3cMinmConnectionTable = _H3cMinmConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 4)
)
if mibBuilder.loadTexts:
    h3cMinmConnectionTable.setStatus("current")
_H3cMinmConnectionEntry_Object = MibTableRow
h3cMinmConnectionEntry = _H3cMinmConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 4, 1)
)
h3cMinmConnectionEntry.setIndexNames(
    (0, "A3COM-HUAWEI-VSI-MIB", "h3cVsiIndex"),
    (0, "A3COM-HUAWEI-MINM-MIB", "h3cMinmConnectionLinkId"),
)
if mibBuilder.loadTexts:
    h3cMinmConnectionEntry.setStatus("current")
_H3cMinmConnectionLinkId_Type = Unsigned32
_H3cMinmConnectionLinkId_Object = MibTableColumn
h3cMinmConnectionLinkId = _H3cMinmConnectionLinkId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 4, 1, 1),
    _H3cMinmConnectionLinkId_Type()
)
h3cMinmConnectionLinkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMinmConnectionLinkId.setStatus("current")
_H3cMinmConnectionBmac_Type = MacAddress
_H3cMinmConnectionBmac_Object = MibTableColumn
h3cMinmConnectionBmac = _H3cMinmConnectionBmac_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 4, 1, 2),
    _H3cMinmConnectionBmac_Type()
)
h3cMinmConnectionBmac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMinmConnectionBmac.setStatus("current")


class _H3cMinmConnectionBvlan_Type(Integer32):
    """Custom type h3cMinmConnectionBvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_H3cMinmConnectionBvlan_Type.__name__ = "Integer32"
_H3cMinmConnectionBvlan_Object = MibTableColumn
h3cMinmConnectionBvlan = _H3cMinmConnectionBvlan_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 4, 1, 3),
    _H3cMinmConnectionBvlan_Type()
)
h3cMinmConnectionBvlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMinmConnectionBvlan.setStatus("current")
_H3cMinmConnectionPort_Type = Integer32
_H3cMinmConnectionPort_Object = MibTableColumn
h3cMinmConnectionPort = _H3cMinmConnectionPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 4, 1, 4),
    _H3cMinmConnectionPort_Type()
)
h3cMinmConnectionPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMinmConnectionPort.setStatus("current")


class _H3cMinmConnectionStatus_Type(Integer32):
    """Custom type h3cMinmConnectionStatus based on Integer32"""
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


_H3cMinmConnectionStatus_Type.__name__ = "Integer32"
_H3cMinmConnectionStatus_Object = MibTableColumn
h3cMinmConnectionStatus = _H3cMinmConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 4, 1, 5),
    _H3cMinmConnectionStatus_Type()
)
h3cMinmConnectionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMinmConnectionStatus.setStatus("current")


class _H3cMinmConnectionAgingStatus_Type(Integer32):
    """Custom type h3cMinmConnectionAgingStatus based on Integer32"""
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


_H3cMinmConnectionAgingStatus_Type.__name__ = "Integer32"
_H3cMinmConnectionAgingStatus_Object = MibTableColumn
h3cMinmConnectionAgingStatus = _H3cMinmConnectionAgingStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 4, 1, 6),
    _H3cMinmConnectionAgingStatus_Type()
)
h3cMinmConnectionAgingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMinmConnectionAgingStatus.setStatus("current")
_H3cMinmConnectionRowStatus_Type = RowStatus
_H3cMinmConnectionRowStatus_Object = MibTableColumn
h3cMinmConnectionRowStatus = _H3cMinmConnectionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 107, 1, 4, 1, 7),
    _H3cMinmConnectionRowStatus_Type()
)
h3cMinmConnectionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMinmConnectionRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-MINM-MIB",
    **{"H3cMinmEnabledStatus": H3cMinmEnabledStatus,
       "h3cMinm": h3cMinm,
       "h3cMinmObjects": h3cMinmObjects,
       "h3cMinmScalarGroup": h3cMinmScalarGroup,
       "h3cMinmCapabilities": h3cMinmCapabilities,
       "h3cMinmBmac": h3cMinmBmac,
       "h3cMinmVsiTable": h3cMinmVsiTable,
       "h3cMinmVsiEntry": h3cMinmVsiEntry,
       "h3cMinmVsiBvlan": h3cMinmVsiBvlan,
       "h3cMinmVsiReEncapsulation": h3cMinmVsiReEncapsulation,
       "h3cMinmVsiNextAvailableLinkId": h3cMinmVsiNextAvailableLinkId,
       "h3cMinmUplinkTable": h3cMinmUplinkTable,
       "h3cMinmUplinkEntry": h3cMinmUplinkEntry,
       "h3cMinmUplinkRowStatus": h3cMinmUplinkRowStatus,
       "h3cMinmConnectionTable": h3cMinmConnectionTable,
       "h3cMinmConnectionEntry": h3cMinmConnectionEntry,
       "h3cMinmConnectionLinkId": h3cMinmConnectionLinkId,
       "h3cMinmConnectionBmac": h3cMinmConnectionBmac,
       "h3cMinmConnectionBvlan": h3cMinmConnectionBvlan,
       "h3cMinmConnectionPort": h3cMinmConnectionPort,
       "h3cMinmConnectionStatus": h3cMinmConnectionStatus,
       "h3cMinmConnectionAgingStatus": h3cMinmConnectionAgingStatus,
       "h3cMinmConnectionRowStatus": h3cMinmConnectionRowStatus}
)
