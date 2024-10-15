# SNMP MIB module (A3COM-HUAWEI-LswTRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-LswTRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:29 2024
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

(hwLswFrameIndex,
 hwLswSlotIndex,
 hwLswSubslotIndex) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-DEVICE-MIB",
    "hwLswFrameIndex",
    "hwLswSlotIndex",
    "hwLswSubslotIndex")

(hwDevMFanNum,
 hwDevMFirstTrapTime,
 hwDevMPowerNum) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-LswDEVM-MIB",
    "hwDevMFanNum",
    "hwDevMFirstTrapTime",
    "hwDevMPowerNum")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hwsLswTrapMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 12)
)
hwsLswTrapMib.setRevisions(
        ("2011-11-26 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwsLswTRAPMibObject_ObjectIdentity = ObjectIdentity
hwsLswTRAPMibObject = _HwsLswTRAPMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 12, 1)
)

# Managed Objects groups


# Notification objects

powerfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 12, 1, 1)
)
powerfailure.setObjects(
      *(("A3COM-HUAWEI-LswDEVM-MIB", "hwDevMPowerNum"),
        ("A3COM-HUAWEI-LswDEVM-MIB", "hwDevMFirstTrapTime"))
)
if mibBuilder.loadTexts:
    powerfailure.setStatus(
        "current"
    )

hwPowerNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 12, 1, 2)
)
hwPowerNormal.setObjects(
      *(("A3COM-HUAWEI-LswDEVM-MIB", "hwDevMPowerNum"),
        ("A3COM-HUAWEI-LswDEVM-MIB", "hwDevMFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hwPowerNormal.setStatus(
        "current"
    )

hwMasterPowerNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 12, 1, 3)
)
hwMasterPowerNormal.setObjects(
    ("A3COM-HUAWEI-LswDEVM-MIB", "hwDevMPowerNum")
)
if mibBuilder.loadTexts:
    hwMasterPowerNormal.setStatus(
        "current"
    )

hwSlavePowerNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 12, 1, 4)
)
hwSlavePowerNormal.setObjects(
    ("A3COM-HUAWEI-LswDEVM-MIB", "hwDevMPowerNum")
)
if mibBuilder.loadTexts:
    hwSlavePowerNormal.setStatus(
        "current"
    )

hwPowerRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 12, 1, 5)
)
hwPowerRemoved.setObjects(
    ("A3COM-HUAWEI-LswDEVM-MIB", "hwDevMPowerNum")
)
if mibBuilder.loadTexts:
    hwPowerRemoved.setStatus(
        "current"
    )

fanfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 12, 1, 6)
)
fanfailure.setObjects(
    ("A3COM-HUAWEI-LswDEVM-MIB", "hwDevMFanNum")
)
if mibBuilder.loadTexts:
    fanfailure.setStatus(
        "current"
    )

hwFanNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 12, 1, 7)
)
hwFanNormal.setObjects(
    ("A3COM-HUAWEI-LswDEVM-MIB", "hwDevMFanNum")
)
if mibBuilder.loadTexts:
    hwFanNormal.setStatus(
        "current"
    )

hwBoardRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 12, 1, 8)
)
hwBoardRemoved.setObjects(
      *(("A3COM-HUAWEI-DEVICE-MIB", "hwLswFrameIndex"),
        ("A3COM-HUAWEI-DEVICE-MIB", "hwLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hwBoardRemoved.setStatus(
        "current"
    )

hwBoardInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 12, 1, 9)
)
hwBoardInserted.setObjects(
      *(("A3COM-HUAWEI-DEVICE-MIB", "hwLswFrameIndex"),
        ("A3COM-HUAWEI-DEVICE-MIB", "hwLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hwBoardInserted.setStatus(
        "current"
    )

hwBoardFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 12, 1, 10)
)
hwBoardFailure.setObjects(
      *(("A3COM-HUAWEI-DEVICE-MIB", "hwLswFrameIndex"),
        ("A3COM-HUAWEI-DEVICE-MIB", "hwLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hwBoardFailure.setStatus(
        "current"
    )

hwBoardNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 12, 1, 11)
)
hwBoardNormal.setObjects(
      *(("A3COM-HUAWEI-DEVICE-MIB", "hwLswFrameIndex"),
        ("A3COM-HUAWEI-DEVICE-MIB", "hwLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hwBoardNormal.setStatus(
        "current"
    )

hwSubcardRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 12, 1, 12)
)
hwSubcardRemove.setObjects(
      *(("A3COM-HUAWEI-DEVICE-MIB", "hwLswFrameIndex"),
        ("A3COM-HUAWEI-DEVICE-MIB", "hwLswSlotIndex"),
        ("A3COM-HUAWEI-DEVICE-MIB", "hwLswSubslotIndex"))
)
if mibBuilder.loadTexts:
    hwSubcardRemove.setStatus(
        "current"
    )

hwSubcardInsert = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 12, 1, 13)
)
hwSubcardInsert.setObjects(
      *(("A3COM-HUAWEI-DEVICE-MIB", "hwLswFrameIndex"),
        ("A3COM-HUAWEI-DEVICE-MIB", "hwLswSlotIndex"),
        ("A3COM-HUAWEI-DEVICE-MIB", "hwLswSubslotIndex"))
)
if mibBuilder.loadTexts:
    hwSubcardInsert.setStatus(
        "current"
    )

hwBoaardTemperatureLower = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 12, 1, 14)
)
hwBoaardTemperatureLower.setObjects(
      *(("A3COM-HUAWEI-DEVICE-MIB", "hwLswFrameIndex"),
        ("A3COM-HUAWEI-DEVICE-MIB", "hwLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hwBoaardTemperatureLower.setStatus(
        "current"
    )

hwBoaardTemperatureFromLowerToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 12, 1, 15)
)
hwBoaardTemperatureFromLowerToNormal.setObjects(
      *(("A3COM-HUAWEI-DEVICE-MIB", "hwLswFrameIndex"),
        ("A3COM-HUAWEI-DEVICE-MIB", "hwLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hwBoaardTemperatureFromLowerToNormal.setStatus(
        "current"
    )

hwBoaardTemperatureHigher = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 12, 1, 16)
)
hwBoaardTemperatureHigher.setObjects(
      *(("A3COM-HUAWEI-DEVICE-MIB", "hwLswFrameIndex"),
        ("A3COM-HUAWEI-DEVICE-MIB", "hwLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hwBoaardTemperatureHigher.setStatus(
        "current"
    )

hwBoaardTemperatureFormHigherToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 12, 1, 17)
)
hwBoaardTemperatureFormHigherToNormal.setObjects(
      *(("A3COM-HUAWEI-DEVICE-MIB", "hwLswFrameIndex"),
        ("A3COM-HUAWEI-DEVICE-MIB", "hwLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hwBoaardTemperatureFormHigherToNormal.setStatus(
        "current"
    )

hwRequestLoading = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 12, 1, 18)
)
hwRequestLoading.setObjects(
      *(("A3COM-HUAWEI-DEVICE-MIB", "hwLswFrameIndex"),
        ("A3COM-HUAWEI-DEVICE-MIB", "hwLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hwRequestLoading.setStatus(
        "current"
    )

hwLoadFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 12, 1, 19)
)
hwLoadFailure.setObjects(
      *(("A3COM-HUAWEI-DEVICE-MIB", "hwLswFrameIndex"),
        ("A3COM-HUAWEI-DEVICE-MIB", "hwLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hwLoadFailure.setStatus(
        "current"
    )

hwLoadFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 12, 1, 20)
)
hwLoadFinished.setObjects(
      *(("A3COM-HUAWEI-DEVICE-MIB", "hwLswFrameIndex"),
        ("A3COM-HUAWEI-DEVICE-MIB", "hwLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hwLoadFinished.setStatus(
        "current"
    )

hwBackBoardModeSetFuilure = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 12, 1, 21)
)
hwBackBoardModeSetFuilure.setObjects(
    ("A3COM-HUAWEI-DEVICE-MIB", "hwLswFrameIndex")
)
if mibBuilder.loadTexts:
    hwBackBoardModeSetFuilure.setStatus(
        "current"
    )

hwBackBoardModeSetOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 12, 1, 22)
)
hwBackBoardModeSetOK.setObjects(
    ("A3COM-HUAWEI-DEVICE-MIB", "hwLswFrameIndex")
)
if mibBuilder.loadTexts:
    hwBackBoardModeSetOK.setStatus(
        "current"
    )

hwPowerInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 12, 1, 23)
)
hwPowerInserted.setObjects(
    ("A3COM-HUAWEI-LswDEVM-MIB", "hwDevMPowerNum")
)
if mibBuilder.loadTexts:
    hwPowerInserted.setStatus(
        "current"
    )

hwBootImageUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 12, 1, 24)
)
hwBootImageUpdated.setObjects(
      *(("A3COM-HUAWEI-DEVICE-MIB", "hwLswFrameIndex"),
        ("A3COM-HUAWEI-DEVICE-MIB", "hwLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hwBootImageUpdated.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-LswTRAP-MIB",
    **{"hwsLswTrapMib": hwsLswTrapMib,
       "hwsLswTRAPMibObject": hwsLswTRAPMibObject,
       "powerfailure": powerfailure,
       "hwPowerNormal": hwPowerNormal,
       "hwMasterPowerNormal": hwMasterPowerNormal,
       "hwSlavePowerNormal": hwSlavePowerNormal,
       "hwPowerRemoved": hwPowerRemoved,
       "fanfailure": fanfailure,
       "hwFanNormal": hwFanNormal,
       "hwBoardRemoved": hwBoardRemoved,
       "hwBoardInserted": hwBoardInserted,
       "hwBoardFailure": hwBoardFailure,
       "hwBoardNormal": hwBoardNormal,
       "hwSubcardRemove": hwSubcardRemove,
       "hwSubcardInsert": hwSubcardInsert,
       "hwBoaardTemperatureLower": hwBoaardTemperatureLower,
       "hwBoaardTemperatureFromLowerToNormal": hwBoaardTemperatureFromLowerToNormal,
       "hwBoaardTemperatureHigher": hwBoaardTemperatureHigher,
       "hwBoaardTemperatureFormHigherToNormal": hwBoaardTemperatureFormHigherToNormal,
       "hwRequestLoading": hwRequestLoading,
       "hwLoadFailure": hwLoadFailure,
       "hwLoadFinished": hwLoadFinished,
       "hwBackBoardModeSetFuilure": hwBackBoardModeSetFuilure,
       "hwBackBoardModeSetOK": hwBackBoardModeSetOK,
       "hwPowerInserted": hwPowerInserted,
       "hwBootImageUpdated": hwBootImageUpdated}
)
