# SNMP MIB module (FMS100-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FMS100-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:12 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1)
)
_Hub_ObjectIdentity = ObjectIdentity
hub = _Hub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8)
)
_LinkBuilderFMS100_ObjectIdentity = ObjectIdentity
linkBuilderFMS100 = _LinkBuilderFMS100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 20)
)
_Cards_ObjectIdentity = ObjectIdentity
cards = _Cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9)
)
_LinkBuilderFMS100_cards_ObjectIdentity = ObjectIdentity
linkBuilderFMS100_cards = _LinkBuilderFMS100_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 10)
)
_LinkBuilderFMS100_cards_12utp_ObjectIdentity = ObjectIdentity
linkBuilderFMS100_cards_12utp = _LinkBuilderFMS100_cards_12utp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 10, 1)
)
_LinkBuilderFMS100_mib_ObjectIdentity = ObjectIdentity
linkBuilderFMS100_mib = _LinkBuilderFMS100_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 19)
)
_HubEnviroObject_ObjectIdentity = ObjectIdentity
hubEnviroObject = _HubEnviroObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 19, 2)
)
_HubEnviroGroupTable_Object = MibTable
hubEnviroGroupTable = _HubEnviroGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 19, 2, 1)
)
if mibBuilder.loadTexts:
    hubEnviroGroupTable.setStatus("mandatory")
_HubEnviroGroupEntry_Object = MibTableRow
hubEnviroGroupEntry = _HubEnviroGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 19, 2, 1, 1)
)
hubEnviroGroupEntry.setIndexNames(
    (0, "FMS100-MIB", "hubServiceId"),
    (0, "FMS100-MIB", "hubGroupIndex"),
)
if mibBuilder.loadTexts:
    hubEnviroGroupEntry.setStatus("mandatory")
_HubServiceId_Type = Integer32
_HubServiceId_Object = MibTableColumn
hubServiceId = _HubServiceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 19, 2, 1, 1, 1),
    _HubServiceId_Type()
)
hubServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubServiceId.setStatus("mandatory")


class _HubGroupIndex_Type(Integer32):
    """Custom type hubGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HubGroupIndex_Type.__name__ = "Integer32"
_HubGroupIndex_Object = MibTableColumn
hubGroupIndex = _HubGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 19, 2, 1, 1, 2),
    _HubGroupIndex_Type()
)
hubGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubGroupIndex.setStatus("mandatory")


class _HubHighTemp_Type(Integer32):
    """Custom type hubHighTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HubHighTemp_Type.__name__ = "Integer32"
_HubHighTemp_Object = MibTableColumn
hubHighTemp = _HubHighTemp_Object(
    (1, 3, 6, 1, 4, 1, 43, 19, 2, 1, 1, 3),
    _HubHighTemp_Type()
)
hubHighTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubHighTemp.setStatus("mandatory")


class _HubFanFailed_Type(Integer32):
    """Custom type hubFanFailed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HubFanFailed_Type.__name__ = "Integer32"
_HubFanFailed_Object = MibTableColumn
hubFanFailed = _HubFanFailed_Object(
    (1, 3, 6, 1, 4, 1, 43, 19, 2, 1, 1, 4),
    _HubFanFailed_Type()
)
hubFanFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubFanFailed.setStatus("mandatory")
_Pa100RptrSpecific_ObjectIdentity = ObjectIdentity
pa100RptrSpecific = _Pa100RptrSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 19, 3)
)
_Pa100RptrInfo_ObjectIdentity = ObjectIdentity
pa100RptrInfo = _Pa100RptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 19, 3, 1)
)
_Pa100RptrTable_Object = MibTable
pa100RptrTable = _Pa100RptrTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 19, 3, 1, 1)
)
if mibBuilder.loadTexts:
    pa100RptrTable.setStatus("mandatory")
_Pa100RptrEntry_Object = MibTableRow
pa100RptrEntry = _Pa100RptrEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 19, 3, 1, 1, 1)
)
pa100RptrEntry.setIndexNames(
    (0, "FMS100-MIB", "pa100RptrServiceId"),
)
if mibBuilder.loadTexts:
    pa100RptrEntry.setStatus("mandatory")
_Pa100RptrServiceId_Type = Integer32
_Pa100RptrServiceId_Object = MibTableColumn
pa100RptrServiceId = _Pa100RptrServiceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 19, 3, 1, 1, 1, 1),
    _Pa100RptrServiceId_Type()
)
pa100RptrServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pa100RptrServiceId.setStatus("mandatory")


class _Pa100RptrClass_Type(Integer32):
    """Custom type pa100RptrClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("classI", 1),
          ("classII", 2),
          ("unknown", 3))
    )


_Pa100RptrClass_Type.__name__ = "Integer32"
_Pa100RptrClass_Object = MibTableColumn
pa100RptrClass = _Pa100RptrClass_Object(
    (1, 3, 6, 1, 4, 1, 43, 19, 3, 1, 1, 1, 2),
    _Pa100RptrClass_Type()
)
pa100RptrClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pa100RptrClass.setStatus("mandatory")


class _Pa100RptrStackCardTypeInfo_Type(OctetString):
    """Custom type pa100RptrStackCardTypeInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Pa100RptrStackCardTypeInfo_Type.__name__ = "OctetString"
_Pa100RptrStackCardTypeInfo_Object = MibTableColumn
pa100RptrStackCardTypeInfo = _Pa100RptrStackCardTypeInfo_Object(
    (1, 3, 6, 1, 4, 1, 43, 19, 3, 1, 1, 1, 3),
    _Pa100RptrStackCardTypeInfo_Type()
)
pa100RptrStackCardTypeInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pa100RptrStackCardTypeInfo.setStatus("mandatory")
_Pa100GroupInfo_ObjectIdentity = ObjectIdentity
pa100GroupInfo = _Pa100GroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 19, 3, 2)
)
_Pa100PortInfo_ObjectIdentity = ObjectIdentity
pa100PortInfo = _Pa100PortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 19, 3, 3)
)
_Pa100PortTable_Object = MibTable
pa100PortTable = _Pa100PortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 19, 3, 3, 1)
)
if mibBuilder.loadTexts:
    pa100PortTable.setStatus("mandatory")
_Pa100PortEntry_Object = MibTableRow
pa100PortEntry = _Pa100PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 19, 3, 3, 1, 1)
)
pa100PortEntry.setIndexNames(
    (0, "FMS100-MIB", "pa100PortServiceId"),
    (0, "FMS100-MIB", "pa100PortGroupIndex"),
    (0, "FMS100-MIB", "pa100PortIndex"),
)
if mibBuilder.loadTexts:
    pa100PortEntry.setStatus("mandatory")
_Pa100PortServiceId_Type = Integer32
_Pa100PortServiceId_Object = MibTableColumn
pa100PortServiceId = _Pa100PortServiceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 19, 3, 3, 1, 1, 1),
    _Pa100PortServiceId_Type()
)
pa100PortServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pa100PortServiceId.setStatus("mandatory")


class _Pa100PortGroupIndex_Type(Integer32):
    """Custom type pa100PortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Pa100PortGroupIndex_Type.__name__ = "Integer32"
_Pa100PortGroupIndex_Object = MibTableColumn
pa100PortGroupIndex = _Pa100PortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 19, 3, 3, 1, 1, 2),
    _Pa100PortGroupIndex_Type()
)
pa100PortGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pa100PortGroupIndex.setStatus("mandatory")


class _Pa100PortIndex_Type(Integer32):
    """Custom type pa100PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Pa100PortIndex_Type.__name__ = "Integer32"
_Pa100PortIndex_Object = MibTableColumn
pa100PortIndex = _Pa100PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 19, 3, 3, 1, 1, 3),
    _Pa100PortIndex_Type()
)
pa100PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pa100PortIndex.setStatus("mandatory")
_Pa100PortIsolate_Type = Counter32
_Pa100PortIsolate_Object = MibTableColumn
pa100PortIsolate = _Pa100PortIsolate_Object(
    (1, 3, 6, 1, 4, 1, 43, 19, 3, 3, 1, 1, 4),
    _Pa100PortIsolate_Type()
)
pa100PortIsolate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pa100PortIsolate.setStatus("mandatory")
_Pa100PortSymbolErrorDuringPacket_Type = Counter32
_Pa100PortSymbolErrorDuringPacket_Object = MibTableColumn
pa100PortSymbolErrorDuringPacket = _Pa100PortSymbolErrorDuringPacket_Object(
    (1, 3, 6, 1, 4, 1, 43, 19, 3, 3, 1, 1, 5),
    _Pa100PortSymbolErrorDuringPacket_Type()
)
pa100PortSymbolErrorDuringPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pa100PortSymbolErrorDuringPacket.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FMS100-MIB",
    **{"a3Com": a3Com,
       "products": products,
       "hub": hub,
       "linkBuilderFMS100": linkBuilderFMS100,
       "cards": cards,
       "linkBuilderFMS100-cards": linkBuilderFMS100_cards,
       "linkBuilderFMS100-cards-12utp": linkBuilderFMS100_cards_12utp,
       "linkBuilderFMS100-mib": linkBuilderFMS100_mib,
       "hubEnviroObject": hubEnviroObject,
       "hubEnviroGroupTable": hubEnviroGroupTable,
       "hubEnviroGroupEntry": hubEnviroGroupEntry,
       "hubServiceId": hubServiceId,
       "hubGroupIndex": hubGroupIndex,
       "hubHighTemp": hubHighTemp,
       "hubFanFailed": hubFanFailed,
       "pa100RptrSpecific": pa100RptrSpecific,
       "pa100RptrInfo": pa100RptrInfo,
       "pa100RptrTable": pa100RptrTable,
       "pa100RptrEntry": pa100RptrEntry,
       "pa100RptrServiceId": pa100RptrServiceId,
       "pa100RptrClass": pa100RptrClass,
       "pa100RptrStackCardTypeInfo": pa100RptrStackCardTypeInfo,
       "pa100GroupInfo": pa100GroupInfo,
       "pa100PortInfo": pa100PortInfo,
       "pa100PortTable": pa100PortTable,
       "pa100PortEntry": pa100PortEntry,
       "pa100PortServiceId": pa100PortServiceId,
       "pa100PortGroupIndex": pa100PortGroupIndex,
       "pa100PortIndex": pa100PortIndex,
       "pa100PortIsolate": pa100PortIsolate,
       "pa100PortSymbolErrorDuringPacket": pa100PortSymbolErrorDuringPacket}
)
