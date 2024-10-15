# SNMP MIB module (HH3C-LswMAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-LswMAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:57 2024
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

(hh3cdot1qVlanIndex,) = mibBuilder.importSymbols(
    "HH3C-LswVLAN-MIB",
    "hh3cdot1qVlanIndex")

(hh3clswCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3clswCommon")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

hh3cLswMacPort = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 3)
)
hh3cLswMacPort.setRevisions(
        ("2001-06-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"


class PortList(OctetString, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Hh3cdot1qMacSearchTable_Object = MibTable
hh3cdot1qMacSearchTable = _Hh3cdot1qMacSearchTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cdot1qMacSearchTable.setStatus("current")
_Hh3cdot1qMacSearchEntry_Object = MibTableRow
hh3cdot1qMacSearchEntry = _Hh3cdot1qMacSearchEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 1, 1)
)
hh3cdot1qMacSearchEntry.setIndexNames(
    (0, "HH3C-LswMAM-MIB", "hh3cdot1qMacSearchAddress"),
    (0, "HH3C-LswMAM-MIB", "hh3cdot1qMacSearchVlanID"),
)
if mibBuilder.loadTexts:
    hh3cdot1qMacSearchEntry.setStatus("current")
_Hh3cdot1qMacSearchAddress_Type = MacAddress
_Hh3cdot1qMacSearchAddress_Object = MibTableColumn
hh3cdot1qMacSearchAddress = _Hh3cdot1qMacSearchAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 1, 1, 1),
    _Hh3cdot1qMacSearchAddress_Type()
)
hh3cdot1qMacSearchAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1qMacSearchAddress.setStatus("current")


class _Hh3cdot1qMacSearchVlanID_Type(Integer32):
    """Custom type hh3cdot1qMacSearchVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 4096),
    )


_Hh3cdot1qMacSearchVlanID_Type.__name__ = "Integer32"
_Hh3cdot1qMacSearchVlanID_Object = MibTableColumn
hh3cdot1qMacSearchVlanID = _Hh3cdot1qMacSearchVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 1, 1, 2),
    _Hh3cdot1qMacSearchVlanID_Type()
)
hh3cdot1qMacSearchVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1qMacSearchVlanID.setStatus("current")
_Hh3cdot1qMacSearchPort_Type = InterfaceIndex
_Hh3cdot1qMacSearchPort_Object = MibTableColumn
hh3cdot1qMacSearchPort = _Hh3cdot1qMacSearchPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 1, 1, 3),
    _Hh3cdot1qMacSearchPort_Type()
)
hh3cdot1qMacSearchPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1qMacSearchPort.setStatus("current")
_Hh3cdot1qMacSearchAgeTime_Type = Integer32
_Hh3cdot1qMacSearchAgeTime_Object = MibTableColumn
hh3cdot1qMacSearchAgeTime = _Hh3cdot1qMacSearchAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 1, 1, 4),
    _Hh3cdot1qMacSearchAgeTime_Type()
)
hh3cdot1qMacSearchAgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1qMacSearchAgeTime.setStatus("current")
_Hh3cdot1qTpFdbSetTable_Object = MibTable
hh3cdot1qTpFdbSetTable = _Hh3cdot1qTpFdbSetTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cdot1qTpFdbSetTable.setStatus("current")
_Hh3cdot1qTpFdbSetEntry_Object = MibTableRow
hh3cdot1qTpFdbSetEntry = _Hh3cdot1qTpFdbSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 2, 1)
)
hh3cdot1qTpFdbSetEntry.setIndexNames(
    (0, "HH3C-LswVLAN-MIB", "hh3cdot1qVlanIndex"),
    (0, "HH3C-LswMAM-MIB", "hh3cdot1qTpFdbSetAddress"),
)
if mibBuilder.loadTexts:
    hh3cdot1qTpFdbSetEntry.setStatus("current")
_Hh3cdot1qTpFdbSetAddress_Type = MacAddress
_Hh3cdot1qTpFdbSetAddress_Object = MibTableColumn
hh3cdot1qTpFdbSetAddress = _Hh3cdot1qTpFdbSetAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 2, 1, 1),
    _Hh3cdot1qTpFdbSetAddress_Type()
)
hh3cdot1qTpFdbSetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cdot1qTpFdbSetAddress.setStatus("current")
_Hh3cdot1qTpFdbSetPort_Type = InterfaceIndex
_Hh3cdot1qTpFdbSetPort_Object = MibTableColumn
hh3cdot1qTpFdbSetPort = _Hh3cdot1qTpFdbSetPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 2, 1, 2),
    _Hh3cdot1qTpFdbSetPort_Type()
)
hh3cdot1qTpFdbSetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1qTpFdbSetPort.setStatus("current")


class _Hh3cdot1qTpFdbSetStatus_Type(Integer32):
    """Custom type hh3cdot1qTpFdbSetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              6,
              7,
              9,
              11)
        )
    )
    namedValues = NamedValues(
        *(("blackhole", 9),
          ("dynamic", 7),
          ("learned", 3),
          ("other", 1),
          ("security", 11),
          ("static", 6))
    )


_Hh3cdot1qTpFdbSetStatus_Type.__name__ = "Integer32"
_Hh3cdot1qTpFdbSetStatus_Object = MibTableColumn
hh3cdot1qTpFdbSetStatus = _Hh3cdot1qTpFdbSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 2, 1, 3),
    _Hh3cdot1qTpFdbSetStatus_Type()
)
hh3cdot1qTpFdbSetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1qTpFdbSetStatus.setStatus("current")


class _Hh3cdot1qTpFdbSetOperate_Type(Integer32):
    """Custom type hh3cdot1qTpFdbSetOperate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )


_Hh3cdot1qTpFdbSetOperate_Type.__name__ = "Integer32"
_Hh3cdot1qTpFdbSetOperate_Object = MibTableColumn
hh3cdot1qTpFdbSetOperate = _Hh3cdot1qTpFdbSetOperate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 2, 1, 4),
    _Hh3cdot1qTpFdbSetOperate_Type()
)
hh3cdot1qTpFdbSetOperate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1qTpFdbSetOperate.setStatus("current")
_Hh3cdot1qTpFdbGroupSetTable_Object = MibTable
hh3cdot1qTpFdbGroupSetTable = _Hh3cdot1qTpFdbGroupSetTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 3)
)
if mibBuilder.loadTexts:
    hh3cdot1qTpFdbGroupSetTable.setStatus("current")
_Hh3cdot1qTpFdbGroupSetEntry_Object = MibTableRow
hh3cdot1qTpFdbGroupSetEntry = _Hh3cdot1qTpFdbGroupSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 3, 1)
)
hh3cdot1qTpFdbGroupSetEntry.setIndexNames(
    (0, "HH3C-LswVLAN-MIB", "hh3cdot1qVlanIndex"),
    (0, "HH3C-LswMAM-MIB", "hh3cdot1qTpFdbGroupSetAddress"),
)
if mibBuilder.loadTexts:
    hh3cdot1qTpFdbGroupSetEntry.setStatus("current")
_Hh3cdot1qTpFdbGroupSetAddress_Type = MacAddress
_Hh3cdot1qTpFdbGroupSetAddress_Object = MibTableColumn
hh3cdot1qTpFdbGroupSetAddress = _Hh3cdot1qTpFdbGroupSetAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 3, 1, 1),
    _Hh3cdot1qTpFdbGroupSetAddress_Type()
)
hh3cdot1qTpFdbGroupSetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cdot1qTpFdbGroupSetAddress.setStatus("current")
_Hh3cdot1qTpFdbGroupSetPort_Type = PortList
_Hh3cdot1qTpFdbGroupSetPort_Object = MibTableColumn
hh3cdot1qTpFdbGroupSetPort = _Hh3cdot1qTpFdbGroupSetPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 3, 1, 2),
    _Hh3cdot1qTpFdbGroupSetPort_Type()
)
hh3cdot1qTpFdbGroupSetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1qTpFdbGroupSetPort.setStatus("current")


class _Hh3cdot1qTpFdbGroupSetOperate_Type(Integer32):
    """Custom type hh3cdot1qTpFdbGroupSetOperate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )


_Hh3cdot1qTpFdbGroupSetOperate_Type.__name__ = "Integer32"
_Hh3cdot1qTpFdbGroupSetOperate_Object = MibTableColumn
hh3cdot1qTpFdbGroupSetOperate = _Hh3cdot1qTpFdbGroupSetOperate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 3, 3, 1, 3),
    _Hh3cdot1qTpFdbGroupSetOperate_Type()
)
hh3cdot1qTpFdbGroupSetOperate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1qTpFdbGroupSetOperate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-LswMAM-MIB",
    **{"InterfaceIndex": InterfaceIndex,
       "PortList": PortList,
       "hh3cLswMacPort": hh3cLswMacPort,
       "hh3cdot1qMacSearchTable": hh3cdot1qMacSearchTable,
       "hh3cdot1qMacSearchEntry": hh3cdot1qMacSearchEntry,
       "hh3cdot1qMacSearchAddress": hh3cdot1qMacSearchAddress,
       "hh3cdot1qMacSearchVlanID": hh3cdot1qMacSearchVlanID,
       "hh3cdot1qMacSearchPort": hh3cdot1qMacSearchPort,
       "hh3cdot1qMacSearchAgeTime": hh3cdot1qMacSearchAgeTime,
       "hh3cdot1qTpFdbSetTable": hh3cdot1qTpFdbSetTable,
       "hh3cdot1qTpFdbSetEntry": hh3cdot1qTpFdbSetEntry,
       "hh3cdot1qTpFdbSetAddress": hh3cdot1qTpFdbSetAddress,
       "hh3cdot1qTpFdbSetPort": hh3cdot1qTpFdbSetPort,
       "hh3cdot1qTpFdbSetStatus": hh3cdot1qTpFdbSetStatus,
       "hh3cdot1qTpFdbSetOperate": hh3cdot1qTpFdbSetOperate,
       "hh3cdot1qTpFdbGroupSetTable": hh3cdot1qTpFdbGroupSetTable,
       "hh3cdot1qTpFdbGroupSetEntry": hh3cdot1qTpFdbGroupSetEntry,
       "hh3cdot1qTpFdbGroupSetAddress": hh3cdot1qTpFdbGroupSetAddress,
       "hh3cdot1qTpFdbGroupSetPort": hh3cdot1qTpFdbGroupSetPort,
       "hh3cdot1qTpFdbGroupSetOperate": hh3cdot1qTpFdbGroupSetOperate}
)
