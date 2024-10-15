# SNMP MIB module (HUAWEI-LswMix-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-LswMix-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:44 2024
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

(lswCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "lswCommon")

(hwLswFrameIndex,
 hwLswSlotIndex) = mibBuilder.importSymbols(
    "HUAWEI-LSW-DEV-ADM-MIB",
    "hwLswFrameIndex",
    "hwLswSlotIndex")

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

hwLswMix = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 17)
)
hwLswMix.setRevisions(
        ("2001-06-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwLswLastSwitchDate_Type = Integer32
_HwLswLastSwitchDate_Object = MibScalar
hwLswLastSwitchDate = _HwLswLastSwitchDate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 17, 1),
    _HwLswLastSwitchDate_Type()
)
hwLswLastSwitchDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswLastSwitchDate.setStatus("current")
_HwLswLastSwitchTime_Type = Integer32
_HwLswLastSwitchTime_Object = MibScalar
hwLswLastSwitchTime = _HwLswLastSwitchTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 17, 2),
    _HwLswLastSwitchTime_Type()
)
hwLswLastSwitchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswLastSwitchTime.setStatus("current")
_HwLswMpuSwitchsNum_Type = Integer32
_HwLswMpuSwitchsNum_Object = MibScalar
hwLswMpuSwitchsNum = _HwLswMpuSwitchsNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 17, 3),
    _HwLswMpuSwitchsNum_Type()
)
hwLswMpuSwitchsNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswMpuSwitchsNum.setStatus("current")


class _HwLswMpuSwitch_Type(Integer32):
    """Custom type hwLswMpuSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("switch", 1)
    )


_HwLswMpuSwitch_Type.__name__ = "Integer32"
_HwLswMpuSwitch_Object = MibScalar
hwLswMpuSwitch = _HwLswMpuSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 17, 4),
    _HwLswMpuSwitch_Type()
)
hwLswMpuSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLswMpuSwitch.setStatus("current")
_HwLswXSlotTable_Object = MibTable
hwLswXSlotTable = _HwLswXSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 17, 5)
)
if mibBuilder.loadTexts:
    hwLswXSlotTable.setStatus("current")
_HwLswXSlotEntry_Object = MibTableRow
hwLswXSlotEntry = _HwLswXSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 17, 5, 1)
)
hwLswXSlotEntry.setIndexNames(
    (0, "HUAWEI-LSW-DEV-ADM-MIB", "hwLswFrameIndex"),
    (0, "HUAWEI-LSW-DEV-ADM-MIB", "hwLswSlotIndex"),
)
if mibBuilder.loadTexts:
    hwLswXSlotEntry.setStatus("current")


class _HwLswMainCardBoardStatus_Type(Integer32):
    """Custom type hwLswMainCardBoardStatus based on Integer32"""
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


_HwLswMainCardBoardStatus_Type.__name__ = "Integer32"
_HwLswMainCardBoardStatus_Object = MibTableColumn
hwLswMainCardBoardStatus = _HwLswMainCardBoardStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 17, 5, 1, 1),
    _HwLswMainCardBoardStatus_Type()
)
hwLswMainCardBoardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswMainCardBoardStatus.setStatus("current")


class _HwLswCrossBarStatus_Type(Integer32):
    """Custom type hwLswCrossBarStatus based on Integer32"""
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


_HwLswCrossBarStatus_Type.__name__ = "Integer32"
_HwLswCrossBarStatus_Object = MibTableColumn
hwLswCrossBarStatus = _HwLswCrossBarStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 17, 5, 1, 2),
    _HwLswCrossBarStatus_Type()
)
hwLswCrossBarStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswCrossBarStatus.setStatus("current")
_HwsMixTrapMib_ObjectIdentity = ObjectIdentity
hwsMixTrapMib = _HwsMixTrapMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 17, 10)
)

# Managed Objects groups


# Notification objects

hwSlaveSwitchOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 17, 10, 1)
)
if mibBuilder.loadTexts:
    hwSlaveSwitchOver.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-LswMix-MIB",
    **{"hwLswMix": hwLswMix,
       "hwLswLastSwitchDate": hwLswLastSwitchDate,
       "hwLswLastSwitchTime": hwLswLastSwitchTime,
       "hwLswMpuSwitchsNum": hwLswMpuSwitchsNum,
       "hwLswMpuSwitch": hwLswMpuSwitch,
       "hwLswXSlotTable": hwLswXSlotTable,
       "hwLswXSlotEntry": hwLswXSlotEntry,
       "hwLswMainCardBoardStatus": hwLswMainCardBoardStatus,
       "hwLswCrossBarStatus": hwLswCrossBarStatus,
       "hwsMixTrapMib": hwsMixTrapMib,
       "hwSlaveSwitchOver": hwSlaveSwitchOver}
)
