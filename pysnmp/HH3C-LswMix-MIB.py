# SNMP MIB module (HH3C-LswMix-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-LswMix-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:59 2024
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

(hh3cLswFrameIndex,
 hh3cLswSlotIndex) = mibBuilder.importSymbols(
    "HH3C-LSW-DEV-ADM-MIB",
    "hh3cLswFrameIndex",
    "hh3cLswSlotIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hh3cLswMix = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 17)
)
hh3cLswMix.setRevisions(
        ("2001-06-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cLswLastSwitchDate_Type = Integer32
_Hh3cLswLastSwitchDate_Object = MibScalar
hh3cLswLastSwitchDate = _Hh3cLswLastSwitchDate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 17, 1),
    _Hh3cLswLastSwitchDate_Type()
)
hh3cLswLastSwitchDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswLastSwitchDate.setStatus("current")
_Hh3cLswLastSwitchTime_Type = Integer32
_Hh3cLswLastSwitchTime_Object = MibScalar
hh3cLswLastSwitchTime = _Hh3cLswLastSwitchTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 17, 2),
    _Hh3cLswLastSwitchTime_Type()
)
hh3cLswLastSwitchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswLastSwitchTime.setStatus("current")
_Hh3cLswMpuSwitchsNum_Type = Integer32
_Hh3cLswMpuSwitchsNum_Object = MibScalar
hh3cLswMpuSwitchsNum = _Hh3cLswMpuSwitchsNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 17, 3),
    _Hh3cLswMpuSwitchsNum_Type()
)
hh3cLswMpuSwitchsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswMpuSwitchsNum.setStatus("current")


class _Hh3cLswMpuSwitch_Type(Integer32):
    """Custom type hh3cLswMpuSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("switch", 1)
    )


_Hh3cLswMpuSwitch_Type.__name__ = "Integer32"
_Hh3cLswMpuSwitch_Object = MibScalar
hh3cLswMpuSwitch = _Hh3cLswMpuSwitch_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 17, 4),
    _Hh3cLswMpuSwitch_Type()
)
hh3cLswMpuSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLswMpuSwitch.setStatus("current")
_Hh3cLswXSlotTable_Object = MibTable
hh3cLswXSlotTable = _Hh3cLswXSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 17, 5)
)
if mibBuilder.loadTexts:
    hh3cLswXSlotTable.setStatus("current")
_Hh3cLswXSlotEntry_Object = MibTableRow
hh3cLswXSlotEntry = _Hh3cLswXSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 17, 5, 1)
)
hh3cLswXSlotEntry.setIndexNames(
    (0, "HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
    (0, "HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
)
if mibBuilder.loadTexts:
    hh3cLswXSlotEntry.setStatus("current")


class _Hh3cLswMainCardBoardStatus_Type(Integer32):
    """Custom type hh3cLswMainCardBoardStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("process", 3),
          ("standby", 2))
    )


_Hh3cLswMainCardBoardStatus_Type.__name__ = "Integer32"
_Hh3cLswMainCardBoardStatus_Object = MibTableColumn
hh3cLswMainCardBoardStatus = _Hh3cLswMainCardBoardStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 17, 5, 1, 1),
    _Hh3cLswMainCardBoardStatus_Type()
)
hh3cLswMainCardBoardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswMainCardBoardStatus.setStatus("current")


class _Hh3cLswCrossBarStatus_Type(Integer32):
    """Custom type hh3cLswCrossBarStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("standby", 2))
    )


_Hh3cLswCrossBarStatus_Type.__name__ = "Integer32"
_Hh3cLswCrossBarStatus_Object = MibTableColumn
hh3cLswCrossBarStatus = _Hh3cLswCrossBarStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 17, 5, 1, 2),
    _Hh3cLswCrossBarStatus_Type()
)
hh3cLswCrossBarStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswCrossBarStatus.setStatus("current")
_Hh3csMixTrapMib_ObjectIdentity = ObjectIdentity
hh3csMixTrapMib = _Hh3csMixTrapMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 17, 10)
)

# Managed Objects groups


# Notification objects

hh3cSlaveSwitchOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 17, 10, 1)
)
if mibBuilder.loadTexts:
    hh3cSlaveSwitchOver.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-LswMix-MIB",
    **{"hh3cLswMix": hh3cLswMix,
       "hh3cLswLastSwitchDate": hh3cLswLastSwitchDate,
       "hh3cLswLastSwitchTime": hh3cLswLastSwitchTime,
       "hh3cLswMpuSwitchsNum": hh3cLswMpuSwitchsNum,
       "hh3cLswMpuSwitch": hh3cLswMpuSwitch,
       "hh3cLswXSlotTable": hh3cLswXSlotTable,
       "hh3cLswXSlotEntry": hh3cLswXSlotEntry,
       "hh3cLswMainCardBoardStatus": hh3cLswMainCardBoardStatus,
       "hh3cLswCrossBarStatus": hh3cLswCrossBarStatus,
       "hh3csMixTrapMib": hh3csMixTrapMib,
       "hh3cSlaveSwitchOver": hh3cSlaveSwitchOver}
)
