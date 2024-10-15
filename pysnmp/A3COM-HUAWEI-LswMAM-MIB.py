# SNMP MIB module (A3COM-HUAWEI-LswMAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-LswMAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:25 2024
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

(hwdot1qVlanIndex,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-LswVLAN-MIB",
    "hwdot1qVlanIndex")

(lswCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "lswCommon")

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

hwLswMacPort = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3)
)
hwLswMacPort.setRevisions(
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

_Hwdot1qMacSearchTable_Object = MibTable
hwdot1qMacSearchTable = _Hwdot1qMacSearchTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hwdot1qMacSearchTable.setStatus("current")
_Hwdot1qMacSearchEntry_Object = MibTableRow
hwdot1qMacSearchEntry = _Hwdot1qMacSearchEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 1, 1)
)
hwdot1qMacSearchEntry.setIndexNames(
    (0, "A3COM-HUAWEI-LswMAM-MIB", "hwdot1qMacSearchAddress"),
    (0, "A3COM-HUAWEI-LswMAM-MIB", "hwdot1qMacSearchVlanID"),
)
if mibBuilder.loadTexts:
    hwdot1qMacSearchEntry.setStatus("current")
_Hwdot1qMacSearchAddress_Type = MacAddress
_Hwdot1qMacSearchAddress_Object = MibTableColumn
hwdot1qMacSearchAddress = _Hwdot1qMacSearchAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 1, 1, 1),
    _Hwdot1qMacSearchAddress_Type()
)
hwdot1qMacSearchAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1qMacSearchAddress.setStatus("current")


class _Hwdot1qMacSearchVlanID_Type(Integer32):
    """Custom type hwdot1qMacSearchVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 4096),
    )


_Hwdot1qMacSearchVlanID_Type.__name__ = "Integer32"
_Hwdot1qMacSearchVlanID_Object = MibTableColumn
hwdot1qMacSearchVlanID = _Hwdot1qMacSearchVlanID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 1, 1, 2),
    _Hwdot1qMacSearchVlanID_Type()
)
hwdot1qMacSearchVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1qMacSearchVlanID.setStatus("current")
_Hwdot1qMacSearchPort_Type = InterfaceIndex
_Hwdot1qMacSearchPort_Object = MibTableColumn
hwdot1qMacSearchPort = _Hwdot1qMacSearchPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 1, 1, 3),
    _Hwdot1qMacSearchPort_Type()
)
hwdot1qMacSearchPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1qMacSearchPort.setStatus("current")
_Hwdot1qMacSearchAgeTime_Type = Integer32
_Hwdot1qMacSearchAgeTime_Object = MibTableColumn
hwdot1qMacSearchAgeTime = _Hwdot1qMacSearchAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 1, 1, 4),
    _Hwdot1qMacSearchAgeTime_Type()
)
hwdot1qMacSearchAgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1qMacSearchAgeTime.setStatus("current")
_Hwdot1qTpFdbSetTable_Object = MibTable
hwdot1qTpFdbSetTable = _Hwdot1qTpFdbSetTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hwdot1qTpFdbSetTable.setStatus("current")
_Hwdot1qTpFdbSetEntry_Object = MibTableRow
hwdot1qTpFdbSetEntry = _Hwdot1qTpFdbSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 2, 1)
)
hwdot1qTpFdbSetEntry.setIndexNames(
    (0, "A3COM-HUAWEI-LswVLAN-MIB", "hwdot1qVlanIndex"),
    (0, "A3COM-HUAWEI-LswMAM-MIB", "hwdot1qTpFdbSetAddress"),
)
if mibBuilder.loadTexts:
    hwdot1qTpFdbSetEntry.setStatus("current")
_Hwdot1qTpFdbSetAddress_Type = MacAddress
_Hwdot1qTpFdbSetAddress_Object = MibTableColumn
hwdot1qTpFdbSetAddress = _Hwdot1qTpFdbSetAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 2, 1, 1),
    _Hwdot1qTpFdbSetAddress_Type()
)
hwdot1qTpFdbSetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwdot1qTpFdbSetAddress.setStatus("current")
_Hwdot1qTpFdbSetPort_Type = InterfaceIndex
_Hwdot1qTpFdbSetPort_Object = MibTableColumn
hwdot1qTpFdbSetPort = _Hwdot1qTpFdbSetPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 2, 1, 2),
    _Hwdot1qTpFdbSetPort_Type()
)
hwdot1qTpFdbSetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1qTpFdbSetPort.setStatus("current")


class _Hwdot1qTpFdbSetStatus_Type(Integer32):
    """Custom type hwdot1qTpFdbSetStatus based on Integer32"""
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


_Hwdot1qTpFdbSetStatus_Type.__name__ = "Integer32"
_Hwdot1qTpFdbSetStatus_Object = MibTableColumn
hwdot1qTpFdbSetStatus = _Hwdot1qTpFdbSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 2, 1, 3),
    _Hwdot1qTpFdbSetStatus_Type()
)
hwdot1qTpFdbSetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1qTpFdbSetStatus.setStatus("current")


class _Hwdot1qTpFdbSetOperate_Type(Integer32):
    """Custom type hwdot1qTpFdbSetOperate based on Integer32"""
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


_Hwdot1qTpFdbSetOperate_Type.__name__ = "Integer32"
_Hwdot1qTpFdbSetOperate_Object = MibTableColumn
hwdot1qTpFdbSetOperate = _Hwdot1qTpFdbSetOperate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 2, 1, 4),
    _Hwdot1qTpFdbSetOperate_Type()
)
hwdot1qTpFdbSetOperate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1qTpFdbSetOperate.setStatus("current")
_Hwdot1qTpFdbGroupSetTable_Object = MibTable
hwdot1qTpFdbGroupSetTable = _Hwdot1qTpFdbGroupSetTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hwdot1qTpFdbGroupSetTable.setStatus("current")
_Hwdot1qTpFdbGroupSetEntry_Object = MibTableRow
hwdot1qTpFdbGroupSetEntry = _Hwdot1qTpFdbGroupSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 3, 1)
)
hwdot1qTpFdbGroupSetEntry.setIndexNames(
    (0, "A3COM-HUAWEI-LswVLAN-MIB", "hwdot1qVlanIndex"),
    (0, "A3COM-HUAWEI-LswMAM-MIB", "hwdot1qTpFdbGroupSetAddress"),
)
if mibBuilder.loadTexts:
    hwdot1qTpFdbGroupSetEntry.setStatus("current")
_Hwdot1qTpFdbGroupSetAddress_Type = MacAddress
_Hwdot1qTpFdbGroupSetAddress_Object = MibTableColumn
hwdot1qTpFdbGroupSetAddress = _Hwdot1qTpFdbGroupSetAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 3, 1, 1),
    _Hwdot1qTpFdbGroupSetAddress_Type()
)
hwdot1qTpFdbGroupSetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwdot1qTpFdbGroupSetAddress.setStatus("current")
_Hwdot1qTpFdbGroupSetPort_Type = PortList
_Hwdot1qTpFdbGroupSetPort_Object = MibTableColumn
hwdot1qTpFdbGroupSetPort = _Hwdot1qTpFdbGroupSetPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 3, 1, 2),
    _Hwdot1qTpFdbGroupSetPort_Type()
)
hwdot1qTpFdbGroupSetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1qTpFdbGroupSetPort.setStatus("current")


class _Hwdot1qTpFdbGroupSetOperate_Type(Integer32):
    """Custom type hwdot1qTpFdbGroupSetOperate based on Integer32"""
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


_Hwdot1qTpFdbGroupSetOperate_Type.__name__ = "Integer32"
_Hwdot1qTpFdbGroupSetOperate_Object = MibTableColumn
hwdot1qTpFdbGroupSetOperate = _Hwdot1qTpFdbGroupSetOperate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 3, 3, 1, 3),
    _Hwdot1qTpFdbGroupSetOperate_Type()
)
hwdot1qTpFdbGroupSetOperate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1qTpFdbGroupSetOperate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-LswMAM-MIB",
    **{"InterfaceIndex": InterfaceIndex,
       "PortList": PortList,
       "hwLswMacPort": hwLswMacPort,
       "hwdot1qMacSearchTable": hwdot1qMacSearchTable,
       "hwdot1qMacSearchEntry": hwdot1qMacSearchEntry,
       "hwdot1qMacSearchAddress": hwdot1qMacSearchAddress,
       "hwdot1qMacSearchVlanID": hwdot1qMacSearchVlanID,
       "hwdot1qMacSearchPort": hwdot1qMacSearchPort,
       "hwdot1qMacSearchAgeTime": hwdot1qMacSearchAgeTime,
       "hwdot1qTpFdbSetTable": hwdot1qTpFdbSetTable,
       "hwdot1qTpFdbSetEntry": hwdot1qTpFdbSetEntry,
       "hwdot1qTpFdbSetAddress": hwdot1qTpFdbSetAddress,
       "hwdot1qTpFdbSetPort": hwdot1qTpFdbSetPort,
       "hwdot1qTpFdbSetStatus": hwdot1qTpFdbSetStatus,
       "hwdot1qTpFdbSetOperate": hwdot1qTpFdbSetOperate,
       "hwdot1qTpFdbGroupSetTable": hwdot1qTpFdbGroupSetTable,
       "hwdot1qTpFdbGroupSetEntry": hwdot1qTpFdbGroupSetEntry,
       "hwdot1qTpFdbGroupSetAddress": hwdot1qTpFdbGroupSetAddress,
       "hwdot1qTpFdbGroupSetPort": hwdot1qTpFdbGroupSetPort,
       "hwdot1qTpFdbGroupSetOperate": hwdot1qTpFdbGroupSetOperate}
)
