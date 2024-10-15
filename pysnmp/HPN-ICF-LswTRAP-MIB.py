# SNMP MIB module (HPN-ICF-LswTRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-LswTRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:01 2024
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

(hpnicfLswFrameIndex,
 hpnicfLswSlotIndex,
 hpnicfLswSubslotIndex) = mibBuilder.importSymbols(
    "HPN-ICF-LSW-DEV-ADM-MIB",
    "hpnicfLswFrameIndex",
    "hpnicfLswSlotIndex",
    "hpnicfLswSubslotIndex")

(hpnicfDevMFanNum,
 hpnicfDevMFirstTrapTime,
 hpnicfDevMPowerNum) = mibBuilder.importSymbols(
    "HPN-ICF-LswDEVM-MIB",
    "hpnicfDevMFanNum",
    "hpnicfDevMFirstTrapTime",
    "hpnicfDevMPowerNum")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hpnicfLswTrapMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12)
)
hpnicfLswTrapMib.setRevisions(
        ("2011-11-26 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfsLswTRAPMibObject_ObjectIdentity = ObjectIdentity
hpnicfsLswTRAPMibObject = _HpnicfsLswTRAPMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1)
)
_HpnicfNetworkHealthMonitorFailure_ObjectIdentity = ObjectIdentity
hpnicfNetworkHealthMonitorFailure = _HpnicfNetworkHealthMonitorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 98)
)
_HpnicfNetworkHealthMonitorNormal_ObjectIdentity = ObjectIdentity
hpnicfNetworkHealthMonitorNormal = _HpnicfNetworkHealthMonitorNormal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 99)
)

# Managed Objects groups


# Notification objects

hpnicfpowerfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 1)
)
hpnicfpowerfailure.setObjects(
      *(("HPN-ICF-LswDEVM-MIB", "hpnicfDevMPowerNum"),
        ("HPN-ICF-LswDEVM-MIB", "hpnicfDevMFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hpnicfpowerfailure.setStatus(
        "current"
    )

hpnicfPowerNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 2)
)
hpnicfPowerNormal.setObjects(
      *(("HPN-ICF-LswDEVM-MIB", "hpnicfDevMPowerNum"),
        ("HPN-ICF-LswDEVM-MIB", "hpnicfDevMFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hpnicfPowerNormal.setStatus(
        "current"
    )

hpnicfMasterPowerNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 3)
)
hpnicfMasterPowerNormal.setObjects(
    ("HPN-ICF-LswDEVM-MIB", "hpnicfDevMPowerNum")
)
if mibBuilder.loadTexts:
    hpnicfMasterPowerNormal.setStatus(
        "current"
    )

hpnicfSlavePowerNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 4)
)
hpnicfSlavePowerNormal.setObjects(
    ("HPN-ICF-LswDEVM-MIB", "hpnicfDevMPowerNum")
)
if mibBuilder.loadTexts:
    hpnicfSlavePowerNormal.setStatus(
        "current"
    )

hpnicfPowerRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 5)
)
hpnicfPowerRemoved.setObjects(
    ("HPN-ICF-LswDEVM-MIB", "hpnicfDevMPowerNum")
)
if mibBuilder.loadTexts:
    hpnicfPowerRemoved.setStatus(
        "current"
    )

hpnicffanfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 6)
)
hpnicffanfailure.setObjects(
    ("HPN-ICF-LswDEVM-MIB", "hpnicfDevMFanNum")
)
if mibBuilder.loadTexts:
    hpnicffanfailure.setStatus(
        "current"
    )

hpnicfFanNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 7)
)
hpnicfFanNormal.setObjects(
    ("HPN-ICF-LswDEVM-MIB", "hpnicfDevMFanNum")
)
if mibBuilder.loadTexts:
    hpnicfFanNormal.setStatus(
        "current"
    )

hpnicfBoardRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 8)
)
hpnicfBoardRemoved.setObjects(
      *(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"),
        ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hpnicfBoardRemoved.setStatus(
        "current"
    )

hpnicfBoardInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 9)
)
hpnicfBoardInserted.setObjects(
      *(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"),
        ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hpnicfBoardInserted.setStatus(
        "current"
    )

hpnicfBoardFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 10)
)
hpnicfBoardFailure.setObjects(
      *(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"),
        ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hpnicfBoardFailure.setStatus(
        "current"
    )

hpnicfBoardNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 11)
)
hpnicfBoardNormal.setObjects(
      *(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"),
        ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hpnicfBoardNormal.setStatus(
        "current"
    )

hpnicfSubcardRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 12)
)
hpnicfSubcardRemove.setObjects(
      *(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"),
        ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"),
        ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSubslotIndex"))
)
if mibBuilder.loadTexts:
    hpnicfSubcardRemove.setStatus(
        "current"
    )

hpnicfSubcardInsert = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 13)
)
hpnicfSubcardInsert.setObjects(
      *(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"),
        ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"),
        ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSubslotIndex"))
)
if mibBuilder.loadTexts:
    hpnicfSubcardInsert.setStatus(
        "current"
    )

hpnicfBoardTemperatureLower = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 14)
)
hpnicfBoardTemperatureLower.setObjects(
      *(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"),
        ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hpnicfBoardTemperatureLower.setStatus(
        "current"
    )

hpnicfBoardTemperatureFromLowerToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 15)
)
hpnicfBoardTemperatureFromLowerToNormal.setObjects(
      *(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"),
        ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hpnicfBoardTemperatureFromLowerToNormal.setStatus(
        "current"
    )

hpnicfBoardTemperatureHigher = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 16)
)
hpnicfBoardTemperatureHigher.setObjects(
      *(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"),
        ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hpnicfBoardTemperatureHigher.setStatus(
        "current"
    )

hpnicfBoardTemperatureFormHigherToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 17)
)
hpnicfBoardTemperatureFormHigherToNormal.setObjects(
      *(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"),
        ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hpnicfBoardTemperatureFormHigherToNormal.setStatus(
        "current"
    )

hpnicfRequestLoading = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 18)
)
hpnicfRequestLoading.setObjects(
      *(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"),
        ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hpnicfRequestLoading.setStatus(
        "current"
    )

hpnicfLoadFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 19)
)
hpnicfLoadFailure.setObjects(
      *(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"),
        ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hpnicfLoadFailure.setStatus(
        "current"
    )

hpnicfLoadFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 20)
)
hpnicfLoadFinished.setObjects(
      *(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"),
        ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hpnicfLoadFinished.setStatus(
        "current"
    )

hpnicfBackBoardModeSetFuilure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 21)
)
hpnicfBackBoardModeSetFuilure.setObjects(
    ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex")
)
if mibBuilder.loadTexts:
    hpnicfBackBoardModeSetFuilure.setStatus(
        "current"
    )

hpnicfBackBoardModeSetOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 22)
)
hpnicfBackBoardModeSetOK.setObjects(
    ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex")
)
if mibBuilder.loadTexts:
    hpnicfBackBoardModeSetOK.setStatus(
        "current"
    )

hpnicfPowerInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 23)
)
hpnicfPowerInserted.setObjects(
    ("HPN-ICF-LswDEVM-MIB", "hpnicfDevMPowerNum")
)
if mibBuilder.loadTexts:
    hpnicfPowerInserted.setStatus(
        "current"
    )

hpnicfBootImageUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 12, 1, 24)
)
hpnicfBootImageUpdated.setObjects(
      *(("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswFrameIndex"),
        ("HPN-ICF-LSW-DEV-ADM-MIB", "hpnicfLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hpnicfBootImageUpdated.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-LswTRAP-MIB",
    **{"hpnicfLswTrapMib": hpnicfLswTrapMib,
       "hpnicfsLswTRAPMibObject": hpnicfsLswTRAPMibObject,
       "hpnicfpowerfailure": hpnicfpowerfailure,
       "hpnicfPowerNormal": hpnicfPowerNormal,
       "hpnicfMasterPowerNormal": hpnicfMasterPowerNormal,
       "hpnicfSlavePowerNormal": hpnicfSlavePowerNormal,
       "hpnicfPowerRemoved": hpnicfPowerRemoved,
       "hpnicffanfailure": hpnicffanfailure,
       "hpnicfFanNormal": hpnicfFanNormal,
       "hpnicfBoardRemoved": hpnicfBoardRemoved,
       "hpnicfBoardInserted": hpnicfBoardInserted,
       "hpnicfBoardFailure": hpnicfBoardFailure,
       "hpnicfBoardNormal": hpnicfBoardNormal,
       "hpnicfSubcardRemove": hpnicfSubcardRemove,
       "hpnicfSubcardInsert": hpnicfSubcardInsert,
       "hpnicfBoardTemperatureLower": hpnicfBoardTemperatureLower,
       "hpnicfBoardTemperatureFromLowerToNormal": hpnicfBoardTemperatureFromLowerToNormal,
       "hpnicfBoardTemperatureHigher": hpnicfBoardTemperatureHigher,
       "hpnicfBoardTemperatureFormHigherToNormal": hpnicfBoardTemperatureFormHigherToNormal,
       "hpnicfRequestLoading": hpnicfRequestLoading,
       "hpnicfLoadFailure": hpnicfLoadFailure,
       "hpnicfLoadFinished": hpnicfLoadFinished,
       "hpnicfBackBoardModeSetFuilure": hpnicfBackBoardModeSetFuilure,
       "hpnicfBackBoardModeSetOK": hpnicfBackBoardModeSetOK,
       "hpnicfPowerInserted": hpnicfPowerInserted,
       "hpnicfBootImageUpdated": hpnicfBootImageUpdated,
       "hpnicfNetworkHealthMonitorFailure": hpnicfNetworkHealthMonitorFailure,
       "hpnicfNetworkHealthMonitorNormal": hpnicfNetworkHealthMonitorNormal}
)
