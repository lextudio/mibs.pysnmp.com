# SNMP MIB module (AT-BRI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-BRI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:59 2024
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

(DisplayStringUnsized,
 modules) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "DisplayStringUnsized",
    "modules")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

bri = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 41)
)
bri.setRevisions(
        ("2006-06-28 12:22",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BriIntTable_Object = MibTable
briIntTable = _BriIntTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 41, 1)
)
if mibBuilder.loadTexts:
    briIntTable.setStatus("current")
_BriIntEntry_Object = MibTableRow
briIntEntry = _BriIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 41, 1, 1)
)
briIntEntry.setIndexNames(
    (0, "AT-BRI-MIB", "briIntIndex"),
)
if mibBuilder.loadTexts:
    briIntEntry.setStatus("current")
_BriIntIndex_Type = Integer32
_BriIntIndex_Object = MibTableColumn
briIntIndex = _BriIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 41, 1, 1, 1),
    _BriIntIndex_Type()
)
briIntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briIntIndex.setStatus("current")
_BriIntBoardIndex_Type = Integer32
_BriIntBoardIndex_Object = MibTableColumn
briIntBoardIndex = _BriIntBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 41, 1, 1, 2),
    _BriIntBoardIndex_Type()
)
briIntBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briIntBoardIndex.setStatus("current")
_BriIntBoardPosition_Type = Integer32
_BriIntBoardPosition_Object = MibTableColumn
briIntBoardPosition = _BriIntBoardPosition_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 41, 1, 1, 3),
    _BriIntBoardPosition_Type()
)
briIntBoardPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briIntBoardPosition.setStatus("current")


class _BriIntMode_Type(Integer32):
    """Custom type briIntMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("isdn", 1),
          ("mixed", 3),
          ("tdm", 2))
    )


_BriIntMode_Type.__name__ = "Integer32"
_BriIntMode_Object = MibTableColumn
briIntMode = _BriIntMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 41, 1, 1, 4),
    _BriIntMode_Type()
)
briIntMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briIntMode.setStatus("current")
_BriIntTdmChannelMap_Type = Integer32
_BriIntTdmChannelMap_Object = MibTableColumn
briIntTdmChannelMap = _BriIntTdmChannelMap_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 41, 1, 1, 5),
    _BriIntTdmChannelMap_Type()
)
briIntTdmChannelMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briIntTdmChannelMap.setStatus("current")
_BriIntIsdnChannelMap_Type = Integer32
_BriIntIsdnChannelMap_Object = MibTableColumn
briIntIsdnChannelMap = _BriIntIsdnChannelMap_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 41, 1, 1, 6),
    _BriIntIsdnChannelMap_Type()
)
briIntIsdnChannelMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briIntIsdnChannelMap.setStatus("current")
_BriChanTable_Object = MibTable
briChanTable = _BriChanTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 41, 2)
)
if mibBuilder.loadTexts:
    briChanTable.setStatus("current")
_BriChanEntry_Object = MibTableRow
briChanEntry = _BriChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 41, 2, 1)
)
briChanEntry.setIndexNames(
    (0, "AT-BRI-MIB", "briChanIntIndex"),
    (0, "AT-BRI-MIB", "briChanChannelIndex"),
)
if mibBuilder.loadTexts:
    briChanEntry.setStatus("current")
_BriChanIntIndex_Type = Integer32
_BriChanIntIndex_Object = MibTableColumn
briChanIntIndex = _BriChanIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 41, 2, 1, 1),
    _BriChanIntIndex_Type()
)
briChanIntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briChanIntIndex.setStatus("current")


class _BriChanChannelIndex_Type(Integer32):
    """Custom type briChanChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_BriChanChannelIndex_Type.__name__ = "Integer32"
_BriChanChannelIndex_Object = MibTableColumn
briChanChannelIndex = _BriChanChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 41, 2, 1, 2),
    _BriChanChannelIndex_Type()
)
briChanChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briChanChannelIndex.setStatus("current")


class _BriChanMode_Type(Integer32):
    """Custom type briChanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("isdn", 1),
          ("none", 3),
          ("tdm", 2))
    )


_BriChanMode_Type.__name__ = "Integer32"
_BriChanMode_Object = MibTableColumn
briChanMode = _BriChanMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 41, 2, 1, 3),
    _BriChanMode_Type()
)
briChanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briChanMode.setStatus("current")


class _BriChanState_Type(Integer32):
    """Custom type briChanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_BriChanState_Type.__name__ = "Integer32"
_BriChanState_Object = MibTableColumn
briChanState = _BriChanState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 41, 2, 1, 4),
    _BriChanState_Type()
)
briChanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briChanState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-BRI-MIB",
    **{"bri": bri,
       "briIntTable": briIntTable,
       "briIntEntry": briIntEntry,
       "briIntIndex": briIntIndex,
       "briIntBoardIndex": briIntBoardIndex,
       "briIntBoardPosition": briIntBoardPosition,
       "briIntMode": briIntMode,
       "briIntTdmChannelMap": briIntTdmChannelMap,
       "briIntIsdnChannelMap": briIntIsdnChannelMap,
       "briChanTable": briChanTable,
       "briChanEntry": briChanEntry,
       "briChanIntIndex": briChanIntIndex,
       "briChanChannelIndex": briChanChannelIndex,
       "briChanMode": briChanMode,
       "briChanState": briChanState}
)
