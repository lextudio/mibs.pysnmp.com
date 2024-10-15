# SNMP MIB module (MERU-WLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MERU-WLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:17 2024
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

(mwApNodeId,) = mibBuilder.importSymbols(
    "MERU-CONFIG-AP-MIB",
    "mwApNodeId")

(mwWncVarsHostName,) = mibBuilder.importSymbols(
    "MERU-CONFIG-CONTROLLER-MIB",
    "mwWncVarsHostName")

(mwTopoStaapApId,
 mwTopoStaapStaId) = mibBuilder.importSymbols(
    "MERU-TOPOLOGY-MIB",
    "mwTopoStaapApId",
    "mwTopoStaapStaId")

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

meruWlanMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 1)
)
meruWlanMibModule.setRevisions(
        ("2005-11-01 00:00",
         "2003-01-28 18:51")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ActionStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("actionStatusDone", 5),
          ("actionStatusInError", 4),
          ("actionStatusInProgress", 3),
          ("actionStatusStart", 1),
          ("actionStatusStop", 2))
    )



class UpgradeState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("upgradeStateDone", 4),
          ("upgradeStateFailed", 3),
          ("upgradeStateInProgress", 2),
          ("upgradeStateStart", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Meru_ObjectIdentity = ObjectIdentity
meru = _Meru_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983)
)
if mibBuilder.loadTexts:
    meru.setStatus("current")
_Meru_reg_ObjectIdentity = ObjectIdentity
meru_reg = _Meru_reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1)
)
_Meru_wlan_ObjectIdentity = ObjectIdentity
meru_wlan = _Meru_wlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1)
)
if mibBuilder.loadTexts:
    meru_wlan.setStatus("current")
_MwlWncNodeReg_ObjectIdentity = ObjectIdentity
mwlWncNodeReg = _MwlWncNodeReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 2)
)
_Meru_generic_ObjectIdentity = ObjectIdentity
meru_generic = _Meru_generic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 2)
)
_Meru_products_ObjectIdentity = ObjectIdentity
meru_products = _Meru_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 3)
)
_Meru_wlan_MIB_ObjectIdentity = ObjectIdentity
meru_wlan_MIB = _Meru_wlan_MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1)
)
_Meru_wlan_conf_ObjectIdentity = ObjectIdentity
meru_wlan_conf = _Meru_wlan_conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 1)
)
_Meru_wlan_groups_ObjectIdentity = ObjectIdentity
meru_wlan_groups = _Meru_wlan_groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 1, 1)
)
_Meru_wlan_compls_ObjectIdentity = ObjectIdentity
meru_wlan_compls = _Meru_wlan_compls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 1, 2)
)
_MeruWlanApObjects_ObjectIdentity = ObjectIdentity
meruWlanApObjects = _MeruWlanApObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 1, 3)
)
_Meru_wlan_objs_ObjectIdentity = ObjectIdentity
meru_wlan_objs = _Meru_wlan_objs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 2)
)
_MwlGlobalObjects_ObjectIdentity = ObjectIdentity
mwlGlobalObjects = _MwlGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 2, 1)
)
_MwlGlobalReboot_Type = ActionStatus
_MwlGlobalReboot_Object = MibScalar
mwlGlobalReboot = _MwlGlobalReboot_Object(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 2, 1, 6),
    _MwlGlobalReboot_Type()
)
mwlGlobalReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwlGlobalReboot.setStatus("current")
_MwlTrapContent_Type = DisplayString
_MwlTrapContent_Object = MibScalar
mwlTrapContent = _MwlTrapContent_Object(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 2, 1, 14),
    _MwlTrapContent_Type()
)
mwlTrapContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwlTrapContent.setStatus("current")
_MwlGlobalSave_Type = ActionStatus
_MwlGlobalSave_Object = MibScalar
mwlGlobalSave = _MwlGlobalSave_Object(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 2, 1, 16),
    _MwlGlobalSave_Type()
)
mwlGlobalSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwlGlobalSave.setStatus("current")
_Meru_wlan_events_ObjectIdentity = ObjectIdentity
meru_wlan_events = _Meru_wlan_events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3)
)
_Meru_caps_ObjectIdentity = ObjectIdentity
meru_caps = _Meru_caps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 4)
)
_Meru_reqs_Type = Integer32
_Meru_reqs_Object = MibScalar
meru_reqs = _Meru_reqs_Object(
    (1, 3, 6, 1, 4, 1, 15983, 5),
    _Meru_reqs_Type()
)
meru_reqs.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    meru_reqs.setStatus("obsolete")
_Meru_expr_ObjectIdentity = ObjectIdentity
meru_expr = _Meru_expr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 6)
)

# Managed Objects groups


# Notification objects

mwlTopoStaAtsAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 7)
)
mwlTopoStaAtsAdd.setObjects(
      *(("MERU-TOPOLOGY-MIB", "mwTopoStaapApId"),
        ("MERU-TOPOLOGY-MIB", "mwTopoStaapStaId"))
)
if mibBuilder.loadTexts:
    mwlTopoStaAtsAdd.setStatus(
        "current"
    )

mwlTopoStaAtsRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 8)
)
mwlTopoStaAtsRemove.setObjects(
      *(("MERU-TOPOLOGY-MIB", "mwTopoStaapApId"),
        ("MERU-TOPOLOGY-MIB", "mwTopoStaapStaId"))
)
if mibBuilder.loadTexts:
    mwlTopoStaAtsRemove.setStatus(
        "current"
    )

mwlTopoStaAtsModify = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 9)
)
mwlTopoStaAtsModify.setObjects(
      *(("MERU-TOPOLOGY-MIB", "mwTopoStaapApId"),
        ("MERU-TOPOLOGY-MIB", "mwTopoStaapStaId"))
)
if mibBuilder.loadTexts:
    mwlTopoStaAtsModify.setStatus(
        "current"
    )

mwlRogueApDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 13)
)
mwlRogueApDetected.setObjects(
    ("MERU-WLAN-MIB", "mwlTrapContent")
)
if mibBuilder.loadTexts:
    mwlRogueApDetected.setStatus(
        "current"
    )

mwlRogueApRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 14)
)
mwlRogueApRemoved.setObjects(
    ("MERU-WLAN-MIB", "mwlTrapContent")
)
if mibBuilder.loadTexts:
    mwlRogueApRemoved.setStatus(
        "current"
    )

mwlAtsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 18)
)
mwlAtsDown.setObjects(
      *(("MERU-CONFIG-AP-MIB", "mwApNodeId"),
        ("MERU-WLAN-MIB", "mwlTrapContent"))
)
if mibBuilder.loadTexts:
    mwlAtsDown.setStatus(
        "current"
    )

mwlAtsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 19)
)
mwlAtsUp.setObjects(
      *(("MERU-CONFIG-AP-MIB", "mwApNodeId"),
        ("MERU-WLAN-MIB", "mwlTrapContent"))
)
if mibBuilder.loadTexts:
    mwlAtsUp.setStatus(
        "current"
    )

mwlWatchdogFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 22)
)
mwlWatchdogFailure.setObjects(
      *(("MERU-CONFIG-CONTROLLER-MIB", "mwWncVarsHostName"),
        ("MERU-WLAN-MIB", "mwlTrapContent"))
)
if mibBuilder.loadTexts:
    mwlWatchdogFailure.setStatus(
        "current"
    )

mwlWatchdogUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 23)
)
mwlWatchdogUp.setObjects(
      *(("MERU-CONFIG-CONTROLLER-MIB", "mwWncVarsHostName"),
        ("MERU-WLAN-MIB", "mwlTrapContent"))
)
if mibBuilder.loadTexts:
    mwlWatchdogUp.setStatus(
        "current"
    )

mwlCertificateError = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 24)
)
mwlCertificateError.setObjects(
    ("MERU-WLAN-MIB", "mwlTrapContent")
)
if mibBuilder.loadTexts:
    mwlCertificateError.setStatus(
        "current"
    )

mwlCertificateInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 25)
)
mwlCertificateInstalled.setObjects(
    ("MERU-WLAN-MIB", "mwlTrapContent")
)
if mibBuilder.loadTexts:
    mwlCertificateInstalled.setStatus(
        "current"
    )

mwlApSoftwareVersionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 26)
)
mwlApSoftwareVersionMismatch.setObjects(
      *(("MERU-CONFIG-AP-MIB", "mwApNodeId"),
        ("MERU-WLAN-MIB", "mwlTrapContent"))
)
if mibBuilder.loadTexts:
    mwlApSoftwareVersionMismatch.setStatus(
        "current"
    )

mwlApSoftwareVersionMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 27)
)
mwlApSoftwareVersionMatch.setObjects(
      *(("MERU-CONFIG-AP-MIB", "mwApNodeId"),
        ("MERU-WLAN-MIB", "mwlTrapContent"))
)
if mibBuilder.loadTexts:
    mwlApSoftwareVersionMatch.setStatus(
        "current"
    )

mwlApInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 28)
)
mwlApInitFailure.setObjects(
      *(("MERU-CONFIG-AP-MIB", "mwApNodeId"),
        ("MERU-WLAN-MIB", "mwlTrapContent"))
)
if mibBuilder.loadTexts:
    mwlApInitFailure.setStatus(
        "current"
    )

mwlApInitFailureCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 29)
)
mwlApInitFailureCleared.setObjects(
      *(("MERU-CONFIG-AP-MIB", "mwApNodeId"),
        ("MERU-WLAN-MIB", "mwlTrapContent"))
)
if mibBuilder.loadTexts:
    mwlApInitFailureCleared.setStatus(
        "current"
    )

mwlApRadioCardFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 30)
)
mwlApRadioCardFailure.setObjects(
      *(("MERU-CONFIG-AP-MIB", "mwApNodeId"),
        ("MERU-WLAN-MIB", "mwlTrapContent"))
)
if mibBuilder.loadTexts:
    mwlApRadioCardFailure.setStatus(
        "current"
    )

mwlApRadioCardFailureCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 31)
)
mwlApRadioCardFailureCleared.setObjects(
      *(("MERU-CONFIG-AP-MIB", "mwApNodeId"),
        ("MERU-WLAN-MIB", "mwlTrapContent"))
)
if mibBuilder.loadTexts:
    mwlApRadioCardFailureCleared.setStatus(
        "current"
    )

mwlAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 32)
)
mwlAuthFailure.setObjects(
    ("MERU-WLAN-MIB", "mwlTrapContent")
)
if mibBuilder.loadTexts:
    mwlAuthFailure.setStatus(
        "current"
    )

mwlRadiusServerSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 33)
)
mwlRadiusServerSwitchover.setObjects(
    ("MERU-WLAN-MIB", "mwlTrapContent")
)
if mibBuilder.loadTexts:
    mwlRadiusServerSwitchover.setStatus(
        "current"
    )

mwlRadiusServerSwitchoverFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 34)
)
mwlRadiusServerSwitchoverFailure.setObjects(
    ("MERU-WLAN-MIB", "mwlTrapContent")
)
if mibBuilder.loadTexts:
    mwlRadiusServerSwitchoverFailure.setStatus(
        "current"
    )

mwlRadiusServerRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 35)
)
mwlRadiusServerRestored.setObjects(
    ("MERU-WLAN-MIB", "mwlTrapContent")
)
if mibBuilder.loadTexts:
    mwlRadiusServerRestored.setStatus(
        "current"
    )

mwlAcctRadiusServerSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 36)
)
mwlAcctRadiusServerSwitchover.setObjects(
    ("MERU-WLAN-MIB", "mwlTrapContent")
)
if mibBuilder.loadTexts:
    mwlAcctRadiusServerSwitchover.setStatus(
        "current"
    )

mwlAcctRadiusServerSwitchoverFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 37)
)
mwlAcctRadiusServerSwitchoverFailure.setObjects(
    ("MERU-WLAN-MIB", "mwlTrapContent")
)
if mibBuilder.loadTexts:
    mwlAcctRadiusServerSwitchoverFailure.setStatus(
        "current"
    )

mwlMicFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 38)
)
mwlMicFailure.setObjects(
      *(("MERU-CONFIG-AP-MIB", "mwApNodeId"),
        ("MERU-WLAN-MIB", "mwlTrapContent"))
)
if mibBuilder.loadTexts:
    mwlMicFailure.setStatus(
        "current"
    )

mwlMicCounterMeasureActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 39)
)
mwlMicCounterMeasureActivated.setObjects(
      *(("MERU-CONFIG-AP-MIB", "mwApNodeId"),
        ("MERU-WLAN-MIB", "mwlTrapContent"))
)
if mibBuilder.loadTexts:
    mwlMicCounterMeasureActivated.setStatus(
        "current"
    )

mwlMasterDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 40)
)
mwlMasterDown.setObjects(
      *(("MERU-CONFIG-CONTROLLER-MIB", "mwWncVarsHostName"),
        ("MERU-WLAN-MIB", "mwlTrapContent"))
)
if mibBuilder.loadTexts:
    mwlMasterDown.setStatus(
        "current"
    )

mwlMasterUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 41)
)
mwlMasterUp.setObjects(
      *(("MERU-CONFIG-CONTROLLER-MIB", "mwWncVarsHostName"),
        ("MERU-WLAN-MIB", "mwlTrapContent"))
)
if mibBuilder.loadTexts:
    mwlMasterUp.setStatus(
        "current"
    )

mwlAtsNeighborLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 42)
)
mwlAtsNeighborLoss.setObjects(
    ("MERU-CONFIG-AP-MIB", "mwApNodeId")
)
if mibBuilder.loadTexts:
    mwlAtsNeighborLoss.setStatus(
        "current"
    )

mwlAtsNeighborLossCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 43)
)
mwlAtsNeighborLossCleared.setObjects(
    ("MERU-CONFIG-AP-MIB", "mwApNodeId")
)
if mibBuilder.loadTexts:
    mwlAtsNeighborLossCleared.setStatus(
        "current"
    )

mwlHandoffFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 44)
)
mwlHandoffFail.setObjects(
    ("MERU-CONFIG-AP-MIB", "mwApNodeId")
)
if mibBuilder.loadTexts:
    mwlHandoffFail.setStatus(
        "current"
    )

mwlHandoffFailCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 45)
)
mwlHandoffFailCleared.setObjects(
    ("MERU-CONFIG-AP-MIB", "mwApNodeId")
)
if mibBuilder.loadTexts:
    mwlHandoffFailCleared.setStatus(
        "current"
    )

mwlResourceThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 46)
)
mwlResourceThresholdExceed.setObjects(
    ("MERU-CONFIG-CONTROLLER-MIB", "mwWncVarsHostName")
)
if mibBuilder.loadTexts:
    mwlResourceThresholdExceed.setStatus(
        "current"
    )

mwlResourceThresholdExceedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 47)
)
mwlResourceThresholdExceedCleared.setObjects(
    ("MERU-CONFIG-CONTROLLER-MIB", "mwWncVarsHostName")
)
if mibBuilder.loadTexts:
    mwlResourceThresholdExceedCleared.setStatus(
        "current"
    )

mwlSystemFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 48)
)
mwlSystemFailure.setObjects(
    ("MERU-CONFIG-CONTROLLER-MIB", "mwWncVarsHostName")
)
if mibBuilder.loadTexts:
    mwlSystemFailure.setStatus(
        "current"
    )

mwlSystemFailureCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 49)
)
mwlSystemFailureCleared.setObjects(
    ("MERU-CONFIG-CONTROLLER-MIB", "mwWncVarsHostName")
)
if mibBuilder.loadTexts:
    mwlSystemFailureCleared.setStatus(
        "current"
    )

mwlApBootimageVersionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 50)
)
mwlApBootimageVersionMismatch.setObjects(
      *(("MERU-CONFIG-AP-MIB", "mwApNodeId"),
        ("MERU-WLAN-MIB", "mwlTrapContent"))
)
if mibBuilder.loadTexts:
    mwlApBootimageVersionMismatch.setStatus(
        "current"
    )

mwlApBootimageVersionMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 51)
)
mwlApBootimageVersionMatch.setObjects(
      *(("MERU-CONFIG-AP-MIB", "mwApNodeId"),
        ("MERU-WLAN-MIB", "mwlTrapContent"))
)
if mibBuilder.loadTexts:
    mwlApBootimageVersionMatch.setStatus(
        "current"
    )

mwlMacFilterDeny = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 52)
)
mwlMacFilterDeny.setObjects(
    ("MERU-WLAN-MIB", "mwlTrapContent")
)
if mibBuilder.loadTexts:
    mwlMacFilterDeny.setStatus(
        "current"
    )

mwlMacFilterDenyCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 53)
)
mwlMacFilterDenyCleared.setObjects(
    ("MERU-WLAN-MIB", "mwlTrapContent")
)
if mibBuilder.loadTexts:
    mwlMacFilterDenyCleared.setStatus(
        "current"
    )

mwlSoftwareLicenseExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 54)
)
mwlSoftwareLicenseExpired.setObjects(
    ("MERU-WLAN-MIB", "mwlTrapContent")
)
if mibBuilder.loadTexts:
    mwlSoftwareLicenseExpired.setStatus(
        "current"
    )

mwlSoftwareLicenseInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 55)
)
mwlSoftwareLicenseInstalled.setObjects(
    ("MERU-WLAN-MIB", "mwlTrapContent")
)
if mibBuilder.loadTexts:
    mwlSoftwareLicenseInstalled.setStatus(
        "current"
    )

mwlApTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 56)
)
mwlApTemperature.setObjects(
      *(("MERU-CONFIG-AP-MIB", "mwApNodeId"),
        ("MERU-WLAN-MIB", "mwlTrapContent"))
)
if mibBuilder.loadTexts:
    mwlApTemperature.setStatus(
        "current"
    )

mwlApTemperatureCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 57)
)
mwlApTemperatureCleared.setObjects(
      *(("MERU-CONFIG-AP-MIB", "mwApNodeId"),
        ("MERU-WLAN-MIB", "mwlTrapContent"))
)
if mibBuilder.loadTexts:
    mwlApTemperatureCleared.setStatus(
        "current"
    )

mwlHardwareDiagnostic = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 58)
)
mwlHardwareDiagnostic.setObjects(
    ("MERU-CONFIG-CONTROLLER-MIB", "mwWncVarsHostName")
)
if mibBuilder.loadTexts:
    mwlHardwareDiagnostic.setStatus(
        "current"
    )

mwlHardwareDiagnosticCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 59)
)
mwlHardwareDiagnosticCleared.setObjects(
    ("MERU-CONFIG-CONTROLLER-MIB", "mwWncVarsHostName")
)
if mibBuilder.loadTexts:
    mwlHardwareDiagnosticCleared.setStatus(
        "current"
    )

mwlCacLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 60)
)
mwlCacLimitReached.setObjects(
    ("MERU-WLAN-MIB", "mwlTrapContent")
)
if mibBuilder.loadTexts:
    mwlCacLimitReached.setStatus(
        "current"
    )

mwlRadarDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 61)
)
mwlRadarDetected.setObjects(
    ("MERU-WLAN-MIB", "mwlTrapContent")
)
if mibBuilder.loadTexts:
    mwlRadarDetected.setStatus(
        "current"
    )

mwlOperationalChannelChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 62)
)
mwlOperationalChannelChange.setObjects(
    ("MERU-WLAN-MIB", "mwlTrapContent")
)
if mibBuilder.loadTexts:
    mwlOperationalChannelChange.setStatus(
        "current"
    )

mwlLicensingServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 63)
)
mwlLicensingServerDown.setObjects(
    ("MERU-WLAN-MIB", "mwlTrapContent")
)
if mibBuilder.loadTexts:
    mwlLicensingServerDown.setStatus(
        "current"
    )

mwlNUpgradeLicenseCheckoutFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 64)
)
mwlNUpgradeLicenseCheckoutFail.setObjects(
    ("MERU-WLAN-MIB", "mwlTrapContent")
)
if mibBuilder.loadTexts:
    mwlNUpgradeLicenseCheckoutFail.setStatus(
        "current"
    )

mwlNoLicenseEnforcementExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 65)
)
mwlNoLicenseEnforcementExpired.setObjects(
    ("MERU-WLAN-MIB", "mwlTrapContent")
)
if mibBuilder.loadTexts:
    mwlNoLicenseEnforcementExpired.setStatus(
        "current"
    )

mwlAtsRuntimeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 66)
)
mwlAtsRuntimeError.setObjects(
      *(("MERU-CONFIG-AP-MIB", "mwApNodeId"),
        ("MERU-WLAN-MIB", "mwlTrapContent"))
)
if mibBuilder.loadTexts:
    mwlAtsRuntimeError.setStatus(
        "current"
    )

mwlAtsRuntimeErrorCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 15983, 3, 1, 3, 67)
)
mwlAtsRuntimeErrorCleared.setObjects(
      *(("MERU-CONFIG-AP-MIB", "mwApNodeId"),
        ("MERU-WLAN-MIB", "mwlTrapContent"))
)
if mibBuilder.loadTexts:
    mwlAtsRuntimeErrorCleared.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-WLAN-MIB",
    **{"ActionStatus": ActionStatus,
       "UpgradeState": UpgradeState,
       "meru": meru,
       "meru-reg": meru_reg,
       "meru-wlan": meru_wlan,
       "meruWlanMibModule": meruWlanMibModule,
       "mwlWncNodeReg": mwlWncNodeReg,
       "meru-generic": meru_generic,
       "meru-products": meru_products,
       "meru-wlan-MIB": meru_wlan_MIB,
       "meru-wlan-conf": meru_wlan_conf,
       "meru-wlan-groups": meru_wlan_groups,
       "meru-wlan-compls": meru_wlan_compls,
       "meruWlanApObjects": meruWlanApObjects,
       "meru-wlan-objs": meru_wlan_objs,
       "mwlGlobalObjects": mwlGlobalObjects,
       "mwlGlobalReboot": mwlGlobalReboot,
       "mwlTrapContent": mwlTrapContent,
       "mwlGlobalSave": mwlGlobalSave,
       "meru-wlan-events": meru_wlan_events,
       "mwlTopoStaAtsAdd": mwlTopoStaAtsAdd,
       "mwlTopoStaAtsRemove": mwlTopoStaAtsRemove,
       "mwlTopoStaAtsModify": mwlTopoStaAtsModify,
       "mwlRogueApDetected": mwlRogueApDetected,
       "mwlRogueApRemoved": mwlRogueApRemoved,
       "mwlAtsDown": mwlAtsDown,
       "mwlAtsUp": mwlAtsUp,
       "mwlWatchdogFailure": mwlWatchdogFailure,
       "mwlWatchdogUp": mwlWatchdogUp,
       "mwlCertificateError": mwlCertificateError,
       "mwlCertificateInstalled": mwlCertificateInstalled,
       "mwlApSoftwareVersionMismatch": mwlApSoftwareVersionMismatch,
       "mwlApSoftwareVersionMatch": mwlApSoftwareVersionMatch,
       "mwlApInitFailure": mwlApInitFailure,
       "mwlApInitFailureCleared": mwlApInitFailureCleared,
       "mwlApRadioCardFailure": mwlApRadioCardFailure,
       "mwlApRadioCardFailureCleared": mwlApRadioCardFailureCleared,
       "mwlAuthFailure": mwlAuthFailure,
       "mwlRadiusServerSwitchover": mwlRadiusServerSwitchover,
       "mwlRadiusServerSwitchoverFailure": mwlRadiusServerSwitchoverFailure,
       "mwlRadiusServerRestored": mwlRadiusServerRestored,
       "mwlAcctRadiusServerSwitchover": mwlAcctRadiusServerSwitchover,
       "mwlAcctRadiusServerSwitchoverFailure": mwlAcctRadiusServerSwitchoverFailure,
       "mwlMicFailure": mwlMicFailure,
       "mwlMicCounterMeasureActivated": mwlMicCounterMeasureActivated,
       "mwlMasterDown": mwlMasterDown,
       "mwlMasterUp": mwlMasterUp,
       "mwlAtsNeighborLoss": mwlAtsNeighborLoss,
       "mwlAtsNeighborLossCleared": mwlAtsNeighborLossCleared,
       "mwlHandoffFail": mwlHandoffFail,
       "mwlHandoffFailCleared": mwlHandoffFailCleared,
       "mwlResourceThresholdExceed": mwlResourceThresholdExceed,
       "mwlResourceThresholdExceedCleared": mwlResourceThresholdExceedCleared,
       "mwlSystemFailure": mwlSystemFailure,
       "mwlSystemFailureCleared": mwlSystemFailureCleared,
       "mwlApBootimageVersionMismatch": mwlApBootimageVersionMismatch,
       "mwlApBootimageVersionMatch": mwlApBootimageVersionMatch,
       "mwlMacFilterDeny": mwlMacFilterDeny,
       "mwlMacFilterDenyCleared": mwlMacFilterDenyCleared,
       "mwlSoftwareLicenseExpired": mwlSoftwareLicenseExpired,
       "mwlSoftwareLicenseInstalled": mwlSoftwareLicenseInstalled,
       "mwlApTemperature": mwlApTemperature,
       "mwlApTemperatureCleared": mwlApTemperatureCleared,
       "mwlHardwareDiagnostic": mwlHardwareDiagnostic,
       "mwlHardwareDiagnosticCleared": mwlHardwareDiagnosticCleared,
       "mwlCacLimitReached": mwlCacLimitReached,
       "mwlRadarDetected": mwlRadarDetected,
       "mwlOperationalChannelChange": mwlOperationalChannelChange,
       "mwlLicensingServerDown": mwlLicensingServerDown,
       "mwlNUpgradeLicenseCheckoutFail": mwlNUpgradeLicenseCheckoutFail,
       "mwlNoLicenseEnforcementExpired": mwlNoLicenseEnforcementExpired,
       "mwlAtsRuntimeError": mwlAtsRuntimeError,
       "mwlAtsRuntimeErrorCleared": mwlAtsRuntimeErrorCleared,
       "meru-caps": meru_caps,
       "meru-reqs": meru_reqs,
       "meru-expr": meru_expr}
)
