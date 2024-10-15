# SNMP MIB module (HPN-ICF-LswMAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-LswMAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:56 2024
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

(hpnicfdot1qVlanIndex,) = mibBuilder.importSymbols(
    "HPN-ICF-LswVLAN-MIB",
    "hpnicfdot1qVlanIndex")

(hpnicflswCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicflswCommon")

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

hpnicfLswMacPort = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3)
)
hpnicfLswMacPort.setRevisions(
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

_Hpnicfdot1qMacSearchTable_Object = MibTable
hpnicfdot1qMacSearchTable = _Hpnicfdot1qMacSearchTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 1)
)
if mibBuilder.loadTexts:
    hpnicfdot1qMacSearchTable.setStatus("current")
_Hpnicfdot1qMacSearchEntry_Object = MibTableRow
hpnicfdot1qMacSearchEntry = _Hpnicfdot1qMacSearchEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 1, 1)
)
hpnicfdot1qMacSearchEntry.setIndexNames(
    (0, "HPN-ICF-LswMAM-MIB", "hpnicfdot1qMacSearchAddress"),
    (0, "HPN-ICF-LswMAM-MIB", "hpnicfdot1qMacSearchVlanID"),
)
if mibBuilder.loadTexts:
    hpnicfdot1qMacSearchEntry.setStatus("current")
_Hpnicfdot1qMacSearchAddress_Type = MacAddress
_Hpnicfdot1qMacSearchAddress_Object = MibTableColumn
hpnicfdot1qMacSearchAddress = _Hpnicfdot1qMacSearchAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 1, 1, 1),
    _Hpnicfdot1qMacSearchAddress_Type()
)
hpnicfdot1qMacSearchAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1qMacSearchAddress.setStatus("current")


class _Hpnicfdot1qMacSearchVlanID_Type(Integer32):
    """Custom type hpnicfdot1qMacSearchVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 4096),
    )


_Hpnicfdot1qMacSearchVlanID_Type.__name__ = "Integer32"
_Hpnicfdot1qMacSearchVlanID_Object = MibTableColumn
hpnicfdot1qMacSearchVlanID = _Hpnicfdot1qMacSearchVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 1, 1, 2),
    _Hpnicfdot1qMacSearchVlanID_Type()
)
hpnicfdot1qMacSearchVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1qMacSearchVlanID.setStatus("current")
_Hpnicfdot1qMacSearchPort_Type = InterfaceIndex
_Hpnicfdot1qMacSearchPort_Object = MibTableColumn
hpnicfdot1qMacSearchPort = _Hpnicfdot1qMacSearchPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 1, 1, 3),
    _Hpnicfdot1qMacSearchPort_Type()
)
hpnicfdot1qMacSearchPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1qMacSearchPort.setStatus("current")
_Hpnicfdot1qMacSearchAgeTime_Type = Integer32
_Hpnicfdot1qMacSearchAgeTime_Object = MibTableColumn
hpnicfdot1qMacSearchAgeTime = _Hpnicfdot1qMacSearchAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 1, 1, 4),
    _Hpnicfdot1qMacSearchAgeTime_Type()
)
hpnicfdot1qMacSearchAgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1qMacSearchAgeTime.setStatus("current")
_Hpnicfdot1qTpFdbSetTable_Object = MibTable
hpnicfdot1qTpFdbSetTable = _Hpnicfdot1qTpFdbSetTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 2)
)
if mibBuilder.loadTexts:
    hpnicfdot1qTpFdbSetTable.setStatus("current")
_Hpnicfdot1qTpFdbSetEntry_Object = MibTableRow
hpnicfdot1qTpFdbSetEntry = _Hpnicfdot1qTpFdbSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 2, 1)
)
hpnicfdot1qTpFdbSetEntry.setIndexNames(
    (0, "HPN-ICF-LswVLAN-MIB", "hpnicfdot1qVlanIndex"),
    (0, "HPN-ICF-LswMAM-MIB", "hpnicfdot1qTpFdbSetAddress"),
)
if mibBuilder.loadTexts:
    hpnicfdot1qTpFdbSetEntry.setStatus("current")
_Hpnicfdot1qTpFdbSetAddress_Type = MacAddress
_Hpnicfdot1qTpFdbSetAddress_Object = MibTableColumn
hpnicfdot1qTpFdbSetAddress = _Hpnicfdot1qTpFdbSetAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 2, 1, 1),
    _Hpnicfdot1qTpFdbSetAddress_Type()
)
hpnicfdot1qTpFdbSetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfdot1qTpFdbSetAddress.setStatus("current")
_Hpnicfdot1qTpFdbSetPort_Type = InterfaceIndex
_Hpnicfdot1qTpFdbSetPort_Object = MibTableColumn
hpnicfdot1qTpFdbSetPort = _Hpnicfdot1qTpFdbSetPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 2, 1, 2),
    _Hpnicfdot1qTpFdbSetPort_Type()
)
hpnicfdot1qTpFdbSetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1qTpFdbSetPort.setStatus("current")


class _Hpnicfdot1qTpFdbSetStatus_Type(Integer32):
    """Custom type hpnicfdot1qTpFdbSetStatus based on Integer32"""
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


_Hpnicfdot1qTpFdbSetStatus_Type.__name__ = "Integer32"
_Hpnicfdot1qTpFdbSetStatus_Object = MibTableColumn
hpnicfdot1qTpFdbSetStatus = _Hpnicfdot1qTpFdbSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 2, 1, 3),
    _Hpnicfdot1qTpFdbSetStatus_Type()
)
hpnicfdot1qTpFdbSetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1qTpFdbSetStatus.setStatus("current")


class _Hpnicfdot1qTpFdbSetOperate_Type(Integer32):
    """Custom type hpnicfdot1qTpFdbSetOperate based on Integer32"""
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


_Hpnicfdot1qTpFdbSetOperate_Type.__name__ = "Integer32"
_Hpnicfdot1qTpFdbSetOperate_Object = MibTableColumn
hpnicfdot1qTpFdbSetOperate = _Hpnicfdot1qTpFdbSetOperate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 2, 1, 4),
    _Hpnicfdot1qTpFdbSetOperate_Type()
)
hpnicfdot1qTpFdbSetOperate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1qTpFdbSetOperate.setStatus("current")
_Hpnicfdot1qTpFdbGroupSetTable_Object = MibTable
hpnicfdot1qTpFdbGroupSetTable = _Hpnicfdot1qTpFdbGroupSetTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 3)
)
if mibBuilder.loadTexts:
    hpnicfdot1qTpFdbGroupSetTable.setStatus("current")
_Hpnicfdot1qTpFdbGroupSetEntry_Object = MibTableRow
hpnicfdot1qTpFdbGroupSetEntry = _Hpnicfdot1qTpFdbGroupSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 3, 1)
)
hpnicfdot1qTpFdbGroupSetEntry.setIndexNames(
    (0, "HPN-ICF-LswVLAN-MIB", "hpnicfdot1qVlanIndex"),
    (0, "HPN-ICF-LswMAM-MIB", "hpnicfdot1qTpFdbGroupSetAddress"),
)
if mibBuilder.loadTexts:
    hpnicfdot1qTpFdbGroupSetEntry.setStatus("current")
_Hpnicfdot1qTpFdbGroupSetAddress_Type = MacAddress
_Hpnicfdot1qTpFdbGroupSetAddress_Object = MibTableColumn
hpnicfdot1qTpFdbGroupSetAddress = _Hpnicfdot1qTpFdbGroupSetAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 3, 1, 1),
    _Hpnicfdot1qTpFdbGroupSetAddress_Type()
)
hpnicfdot1qTpFdbGroupSetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfdot1qTpFdbGroupSetAddress.setStatus("current")
_Hpnicfdot1qTpFdbGroupSetPort_Type = PortList
_Hpnicfdot1qTpFdbGroupSetPort_Object = MibTableColumn
hpnicfdot1qTpFdbGroupSetPort = _Hpnicfdot1qTpFdbGroupSetPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 3, 1, 2),
    _Hpnicfdot1qTpFdbGroupSetPort_Type()
)
hpnicfdot1qTpFdbGroupSetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1qTpFdbGroupSetPort.setStatus("current")


class _Hpnicfdot1qTpFdbGroupSetOperate_Type(Integer32):
    """Custom type hpnicfdot1qTpFdbGroupSetOperate based on Integer32"""
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


_Hpnicfdot1qTpFdbGroupSetOperate_Type.__name__ = "Integer32"
_Hpnicfdot1qTpFdbGroupSetOperate_Object = MibTableColumn
hpnicfdot1qTpFdbGroupSetOperate = _Hpnicfdot1qTpFdbGroupSetOperate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 3, 3, 1, 3),
    _Hpnicfdot1qTpFdbGroupSetOperate_Type()
)
hpnicfdot1qTpFdbGroupSetOperate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1qTpFdbGroupSetOperate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-LswMAM-MIB",
    **{"InterfaceIndex": InterfaceIndex,
       "PortList": PortList,
       "hpnicfLswMacPort": hpnicfLswMacPort,
       "hpnicfdot1qMacSearchTable": hpnicfdot1qMacSearchTable,
       "hpnicfdot1qMacSearchEntry": hpnicfdot1qMacSearchEntry,
       "hpnicfdot1qMacSearchAddress": hpnicfdot1qMacSearchAddress,
       "hpnicfdot1qMacSearchVlanID": hpnicfdot1qMacSearchVlanID,
       "hpnicfdot1qMacSearchPort": hpnicfdot1qMacSearchPort,
       "hpnicfdot1qMacSearchAgeTime": hpnicfdot1qMacSearchAgeTime,
       "hpnicfdot1qTpFdbSetTable": hpnicfdot1qTpFdbSetTable,
       "hpnicfdot1qTpFdbSetEntry": hpnicfdot1qTpFdbSetEntry,
       "hpnicfdot1qTpFdbSetAddress": hpnicfdot1qTpFdbSetAddress,
       "hpnicfdot1qTpFdbSetPort": hpnicfdot1qTpFdbSetPort,
       "hpnicfdot1qTpFdbSetStatus": hpnicfdot1qTpFdbSetStatus,
       "hpnicfdot1qTpFdbSetOperate": hpnicfdot1qTpFdbSetOperate,
       "hpnicfdot1qTpFdbGroupSetTable": hpnicfdot1qTpFdbGroupSetTable,
       "hpnicfdot1qTpFdbGroupSetEntry": hpnicfdot1qTpFdbGroupSetEntry,
       "hpnicfdot1qTpFdbGroupSetAddress": hpnicfdot1qTpFdbGroupSetAddress,
       "hpnicfdot1qTpFdbGroupSetPort": hpnicfdot1qTpFdbGroupSetPort,
       "hpnicfdot1qTpFdbGroupSetOperate": hpnicfdot1qTpFdbGroupSetOperate}
)
