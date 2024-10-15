# SNMP MIB module (HH3C-LswTRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-LswTRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:02 2024
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

(hh3cLswCpuIndex,
 hh3cLswFrameIndex,
 hh3cLswSlotIndex,
 hh3cLswSubslotIndex) = mibBuilder.importSymbols(
    "HH3C-LSW-DEV-ADM-MIB",
    "hh3cLswCpuIndex",
    "hh3cLswFrameIndex",
    "hh3cLswSlotIndex",
    "hh3cLswSubslotIndex")

(hh3cDevMFanNum,
 hh3cDevMFirstTrapTime,
 hh3cDevMPowerNum) = mibBuilder.importSymbols(
    "HH3C-LswDEVM-MIB",
    "hh3cDevMFanNum",
    "hh3cDevMFirstTrapTime",
    "hh3cDevMPowerNum")

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

hh3cLswTrapMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12)
)
hh3cLswTrapMib.setRevisions(
        ("2011-11-26 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3csLswTRAPMibObject_ObjectIdentity = ObjectIdentity
hh3csLswTRAPMibObject = _Hh3csLswTRAPMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1)
)
_Hh3cNetworkHealthMonitorFailure_ObjectIdentity = ObjectIdentity
hh3cNetworkHealthMonitorFailure = _Hh3cNetworkHealthMonitorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 98)
)
_Hh3cNetworkHealthMonitorNormal_ObjectIdentity = ObjectIdentity
hh3cNetworkHealthMonitorNormal = _Hh3cNetworkHealthMonitorNormal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 99)
)

# Managed Objects groups


# Notification objects

hh3cpowerfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 1)
)
hh3cpowerfailure.setObjects(
      *(("HH3C-LswDEVM-MIB", "hh3cDevMPowerNum"),
        ("HH3C-LswDEVM-MIB", "hh3cDevMFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hh3cpowerfailure.setStatus(
        "current"
    )

hh3cPowerNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 2)
)
hh3cPowerNormal.setObjects(
      *(("HH3C-LswDEVM-MIB", "hh3cDevMPowerNum"),
        ("HH3C-LswDEVM-MIB", "hh3cDevMFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hh3cPowerNormal.setStatus(
        "current"
    )

hh3cMasterPowerNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 3)
)
hh3cMasterPowerNormal.setObjects(
    ("HH3C-LswDEVM-MIB", "hh3cDevMPowerNum")
)
if mibBuilder.loadTexts:
    hh3cMasterPowerNormal.setStatus(
        "current"
    )

hh3cSlavePowerNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 4)
)
hh3cSlavePowerNormal.setObjects(
    ("HH3C-LswDEVM-MIB", "hh3cDevMPowerNum")
)
if mibBuilder.loadTexts:
    hh3cSlavePowerNormal.setStatus(
        "current"
    )

hh3cPowerRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 5)
)
hh3cPowerRemoved.setObjects(
    ("HH3C-LswDEVM-MIB", "hh3cDevMPowerNum")
)
if mibBuilder.loadTexts:
    hh3cPowerRemoved.setStatus(
        "current"
    )

hh3cfanfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 6)
)
hh3cfanfailure.setObjects(
    ("HH3C-LswDEVM-MIB", "hh3cDevMFanNum")
)
if mibBuilder.loadTexts:
    hh3cfanfailure.setStatus(
        "current"
    )

hh3cFanNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 7)
)
hh3cFanNormal.setObjects(
    ("HH3C-LswDEVM-MIB", "hh3cDevMFanNum")
)
if mibBuilder.loadTexts:
    hh3cFanNormal.setStatus(
        "current"
    )

hh3cBoardRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 8)
)
hh3cBoardRemoved.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hh3cBoardRemoved.setStatus(
        "current"
    )

hh3cBoardInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 9)
)
hh3cBoardInserted.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hh3cBoardInserted.setStatus(
        "current"
    )

hh3cBoardFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 10)
)
hh3cBoardFailure.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hh3cBoardFailure.setStatus(
        "current"
    )

hh3cBoardNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 11)
)
hh3cBoardNormal.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hh3cBoardNormal.setStatus(
        "current"
    )

hh3cSubcardRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 12)
)
hh3cSubcardRemove.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSubslotIndex"))
)
if mibBuilder.loadTexts:
    hh3cSubcardRemove.setStatus(
        "current"
    )

hh3cSubcardInsert = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 13)
)
hh3cSubcardInsert.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSubslotIndex"))
)
if mibBuilder.loadTexts:
    hh3cSubcardInsert.setStatus(
        "current"
    )

hh3cBoardTemperatureLower = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 14)
)
hh3cBoardTemperatureLower.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hh3cBoardTemperatureLower.setStatus(
        "current"
    )

hh3cBoardTemperatureFromLowerToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 15)
)
hh3cBoardTemperatureFromLowerToNormal.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hh3cBoardTemperatureFromLowerToNormal.setStatus(
        "current"
    )

hh3cBoardTemperatureHigher = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 16)
)
hh3cBoardTemperatureHigher.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hh3cBoardTemperatureHigher.setStatus(
        "current"
    )

hh3cBoardTemperatureFormHigherToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 17)
)
hh3cBoardTemperatureFormHigherToNormal.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hh3cBoardTemperatureFormHigherToNormal.setStatus(
        "current"
    )

hh3cRequestLoading = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 18)
)
hh3cRequestLoading.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hh3cRequestLoading.setStatus(
        "current"
    )

hh3cLoadFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 19)
)
hh3cLoadFailure.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hh3cLoadFailure.setStatus(
        "current"
    )

hh3cLoadFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 20)
)
hh3cLoadFinished.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hh3cLoadFinished.setStatus(
        "current"
    )

hh3cBackBoardModeSetFuilure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 21)
)
hh3cBackBoardModeSetFuilure.setObjects(
    ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex")
)
if mibBuilder.loadTexts:
    hh3cBackBoardModeSetFuilure.setStatus(
        "current"
    )

hh3cBackBoardModeSetOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 22)
)
hh3cBackBoardModeSetOK.setObjects(
    ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex")
)
if mibBuilder.loadTexts:
    hh3cBackBoardModeSetOK.setStatus(
        "current"
    )

hh3cPowerInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 23)
)
hh3cPowerInserted.setObjects(
    ("HH3C-LswDEVM-MIB", "hh3cDevMPowerNum")
)
if mibBuilder.loadTexts:
    hh3cPowerInserted.setStatus(
        "current"
    )

hh3cBootImageUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 24)
)
hh3cBootImageUpdated.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hh3cBootImageUpdated.setStatus(
        "current"
    )

hh3cCpuRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 25)
)
hh3cCpuRemoved.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuIndex"))
)
if mibBuilder.loadTexts:
    hh3cCpuRemoved.setStatus(
        "current"
    )

hh3cCpuFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 26)
)
hh3cCpuFailure.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuIndex"))
)
if mibBuilder.loadTexts:
    hh3cCpuFailure.setStatus(
        "current"
    )

hh3cCpuNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 27)
)
hh3cCpuNormal.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuIndex"))
)
if mibBuilder.loadTexts:
    hh3cCpuNormal.setStatus(
        "current"
    )

hh3cPowerIncompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 28)
)
hh3cPowerIncompatible.setObjects(
    ("HH3C-LswDEVM-MIB", "hh3cDevMPowerNum")
)
if mibBuilder.loadTexts:
    hh3cPowerIncompatible.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-LswTRAP-MIB",
    **{"hh3cLswTrapMib": hh3cLswTrapMib,
       "hh3csLswTRAPMibObject": hh3csLswTRAPMibObject,
       "hh3cpowerfailure": hh3cpowerfailure,
       "hh3cPowerNormal": hh3cPowerNormal,
       "hh3cMasterPowerNormal": hh3cMasterPowerNormal,
       "hh3cSlavePowerNormal": hh3cSlavePowerNormal,
       "hh3cPowerRemoved": hh3cPowerRemoved,
       "hh3cfanfailure": hh3cfanfailure,
       "hh3cFanNormal": hh3cFanNormal,
       "hh3cBoardRemoved": hh3cBoardRemoved,
       "hh3cBoardInserted": hh3cBoardInserted,
       "hh3cBoardFailure": hh3cBoardFailure,
       "hh3cBoardNormal": hh3cBoardNormal,
       "hh3cSubcardRemove": hh3cSubcardRemove,
       "hh3cSubcardInsert": hh3cSubcardInsert,
       "hh3cBoardTemperatureLower": hh3cBoardTemperatureLower,
       "hh3cBoardTemperatureFromLowerToNormal": hh3cBoardTemperatureFromLowerToNormal,
       "hh3cBoardTemperatureHigher": hh3cBoardTemperatureHigher,
       "hh3cBoardTemperatureFormHigherToNormal": hh3cBoardTemperatureFormHigherToNormal,
       "hh3cRequestLoading": hh3cRequestLoading,
       "hh3cLoadFailure": hh3cLoadFailure,
       "hh3cLoadFinished": hh3cLoadFinished,
       "hh3cBackBoardModeSetFuilure": hh3cBackBoardModeSetFuilure,
       "hh3cBackBoardModeSetOK": hh3cBackBoardModeSetOK,
       "hh3cPowerInserted": hh3cPowerInserted,
       "hh3cBootImageUpdated": hh3cBootImageUpdated,
       "hh3cCpuRemoved": hh3cCpuRemoved,
       "hh3cCpuFailure": hh3cCpuFailure,
       "hh3cCpuNormal": hh3cCpuNormal,
       "hh3cPowerIncompatible": hh3cPowerIncompatible,
       "hh3cNetworkHealthMonitorFailure": hh3cNetworkHealthMonitorFailure,
       "hh3cNetworkHealthMonitorNormal": hh3cNetworkHealthMonitorNormal}
)
