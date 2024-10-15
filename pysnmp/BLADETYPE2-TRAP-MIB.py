# SNMP MIB module (BLADETYPE2-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BLADETYPE2-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:07 2024
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

(ipCurCfgGwAddr,
 ipCurCfgGwIndex,
 vrrpCurCfgIfIndx,
 vrrpCurCfgIfPasswd,
 vrrpCurCfgVirtRtrAddr,
 vrrpCurCfgVirtRtrIndx) = mibBuilder.importSymbols(
    "BLADETYPE2-NETWORK-MIB",
    "ipCurCfgGwAddr",
    "ipCurCfgGwIndex",
    "vrrpCurCfgIfIndx",
    "vrrpCurCfgIfPasswd",
    "vrrpCurCfgVirtRtrAddr",
    "vrrpCurCfgVirtRtrIndx")

(stgCurCfgIndex,) = mibBuilder.importSymbols(
    "BLADETYPE2-PHYSICAL-MIB",
    "stgCurCfgIndex")

(agChassis,
 agRackId,
 agSlotNumber) = mibBuilder.importSymbols(
    "BLADETYPE2-SWITCH-MIB",
    "agChassis",
    "agRackId",
    "agSlotNumber")

(hpSwitchBladeType2_Mgmt,) = mibBuilder.importSymbols(
    "HP-SWITCH-PL-MIB",
    "hpSwitchBladeType2-Mgmt")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysContact,
 sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysContact",
    "sysLocation",
    "sysName")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
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

_Bt2Traps_ObjectIdentity = ObjectIdentity
bt2Traps = _Bt2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7)
)


class _Bt2SwTrapDisplayString_Type(DisplayString):
    """Custom type bt2SwTrapDisplayString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Bt2SwTrapDisplayString_Type.__name__ = "DisplayString"
_Bt2SwTrapDisplayString_Object = MibScalar
bt2SwTrapDisplayString = _Bt2SwTrapDisplayString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 1000),
    _Bt2SwTrapDisplayString_Type()
)
bt2SwTrapDisplayString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bt2SwTrapDisplayString.setStatus("mandatory")

# Managed Objects groups


# Notification objects

bt2SwPrimaryPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 1)
)
if mibBuilder.loadTexts:
    bt2SwPrimaryPowerSupplyFailure.setStatus(
        ""
    )

bt2SwDefGwUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 2)
)
bt2SwDefGwUp.setObjects(
      *(("BLADETYPE2-NETWORK-MIB", "ipCurCfgGwIndex"),
        ("BLADETYPE2-NETWORK-MIB", "ipCurCfgGwAddr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwDefGwUp.setStatus(
        ""
    )

bt2SwDefGwDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 3)
)
bt2SwDefGwDown.setObjects(
      *(("BLADETYPE2-NETWORK-MIB", "ipCurCfgGwIndex"),
        ("BLADETYPE2-NETWORK-MIB", "ipCurCfgGwAddr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwDefGwDown.setStatus(
        ""
    )

bt2SwDefGwInService = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 4)
)
bt2SwDefGwInService.setObjects(
      *(("BLADETYPE2-NETWORK-MIB", "ipCurCfgGwIndex"),
        ("BLADETYPE2-NETWORK-MIB", "ipCurCfgGwAddr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwDefGwInService.setStatus(
        ""
    )

bt2SwDefGwNotInService = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 5)
)
bt2SwDefGwNotInService.setObjects(
      *(("BLADETYPE2-NETWORK-MIB", "ipCurCfgGwIndex"),
        ("BLADETYPE2-NETWORK-MIB", "ipCurCfgGwAddr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwDefGwNotInService.setStatus(
        ""
    )

bt2SwVrrpNewMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 16)
)
bt2SwVrrpNewMaster.setObjects(
      *(("BLADETYPE2-NETWORK-MIB", "vrrpCurCfgVirtRtrIndx"),
        ("BLADETYPE2-NETWORK-MIB", "vrrpCurCfgVirtRtrAddr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwVrrpNewMaster.setStatus(
        ""
    )

bt2SwVrrpNewBackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 17)
)
bt2SwVrrpNewBackup.setObjects(
      *(("BLADETYPE2-NETWORK-MIB", "vrrpCurCfgVirtRtrIndx"),
        ("BLADETYPE2-NETWORK-MIB", "vrrpCurCfgVirtRtrAddr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwVrrpNewBackup.setStatus(
        ""
    )

bt2SwVrrpAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 18)
)
bt2SwVrrpAuthFailure.setObjects(
      *(("BLADETYPE2-NETWORK-MIB", "vrrpCurCfgIfIndx"),
        ("BLADETYPE2-NETWORK-MIB", "vrrpCurCfgIfPasswd"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwVrrpAuthFailure.setStatus(
        ""
    )

bt2SwLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 19)
)
bt2SwLoginFailure.setObjects(
      *(("BLADETYPE2-TRAP-MIB", "bt2SwTrapDisplayString"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwLoginFailure.setStatus(
        ""
    )

bt2SwTempExceedThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 22)
)
bt2SwTempExceedThreshold.setObjects(
      *(("BLADETYPE2-TRAP-MIB", "bt2SwTrapDisplayString"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwTempExceedThreshold.setStatus(
        ""
    )

bt2SwRackLocationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 26)
)
bt2SwRackLocationChange.setObjects(
      *(("BLADETYPE2-SWITCH-MIB", "agRackId"),
        ("BLADETYPE2-SWITCH-MIB", "agChassis"),
        ("BLADETYPE2-SWITCH-MIB", "agSlotNumber"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwRackLocationChange.setStatus(
        ""
    )

bt2SwApplyComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 27)
)
bt2SwApplyComplete.setObjects(
      *(("BLADETYPE2-TRAP-MIB", "bt2SwTrapDisplayString"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwApplyComplete.setStatus(
        ""
    )

bt2SwSaveComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 28)
)
bt2SwSaveComplete.setObjects(
      *(("BLADETYPE2-TRAP-MIB", "bt2SwTrapDisplayString"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwSaveComplete.setStatus(
        ""
    )

bt2SwFwDownloadSucess = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 29)
)
bt2SwFwDownloadSucess.setObjects(
      *(("BLADETYPE2-TRAP-MIB", "bt2SwTrapDisplayString"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwFwDownloadSucess.setStatus(
        ""
    )

bt2SwFwDownloadFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 30)
)
bt2SwFwDownloadFailure.setObjects(
      *(("BLADETYPE2-TRAP-MIB", "bt2SwTrapDisplayString"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwFwDownloadFailure.setStatus(
        ""
    )

bt2SwTempReturnThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 31)
)
bt2SwTempReturnThreshold.setObjects(
      *(("BLADETYPE2-TRAP-MIB", "bt2SwTrapDisplayString"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwTempReturnThreshold.setStatus(
        ""
    )

bt2SwFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 32)
)
bt2SwFanFailure.setObjects(
      *(("BLADETYPE2-TRAP-MIB", "bt2SwTrapDisplayString"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwFanFailure.setStatus(
        ""
    )

bt2SwFanFailureFixed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 33)
)
bt2SwFanFailureFixed.setObjects(
      *(("BLADETYPE2-TRAP-MIB", "bt2SwTrapDisplayString"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwFanFailureFixed.setStatus(
        ""
    )

bt2SwUfdfoLtMFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 34)
)
bt2SwUfdfoLtMFailure.setObjects(
      *(("BLADETYPE2-TRAP-MIB", "bt2SwTrapDisplayString"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwUfdfoLtMFailure.setStatus(
        ""
    )

bt2SwUfdfoLtMUP = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 35)
)
bt2SwUfdfoLtMUP.setObjects(
      *(("BLADETYPE2-TRAP-MIB", "bt2SwTrapDisplayString"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwUfdfoLtMUP.setStatus(
        ""
    )

bt2SwUfdfoGlobalEna = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 36)
)
bt2SwUfdfoGlobalEna.setObjects(
      *(("BLADETYPE2-TRAP-MIB", "bt2SwTrapDisplayString"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwUfdfoGlobalEna.setStatus(
        ""
    )

bt2SwUfdfoGlobalDis = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 37)
)
bt2SwUfdfoGlobalDis.setObjects(
      *(("BLADETYPE2-TRAP-MIB", "bt2SwTrapDisplayString"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwUfdfoGlobalDis.setStatus(
        ""
    )

bt2SwUfdfoLtDAutoEna = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 38)
)
bt2SwUfdfoLtDAutoEna.setObjects(
      *(("BLADETYPE2-TRAP-MIB", "bt2SwTrapDisplayString"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwUfdfoLtDAutoEna.setStatus(
        ""
    )

bt2SwUfdfoLtDAutoDis = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 39)
)
bt2SwUfdfoLtDAutoDis.setObjects(
      *(("BLADETYPE2-TRAP-MIB", "bt2SwTrapDisplayString"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwUfdfoLtDAutoDis.setStatus(
        ""
    )

bt2SwCubeInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 40)
)
bt2SwCubeInserted.setObjects(
      *(("BLADETYPE2-TRAP-MIB", "bt2SwTrapDisplayString"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwCubeInserted.setStatus(
        ""
    )

bt2SwCubeRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 41)
)
bt2SwCubeRemoved.setObjects(
      *(("BLADETYPE2-TRAP-MIB", "bt2SwTrapDisplayString"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwCubeRemoved.setStatus(
        ""
    )

bt2SwStgNewRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 42)
)
bt2SwStgNewRoot.setObjects(
      *(("BLADETYPE2-TRAP-MIB", "bt2SwTrapDisplayString"),
        ("BLADETYPE2-PHYSICAL-MIB", "stgCurCfgIndex"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwStgNewRoot.setStatus(
        ""
    )

bt2SwCistNewRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 43)
)
bt2SwCistNewRoot.setObjects(
      *(("BLADETYPE2-TRAP-MIB", "bt2SwTrapDisplayString"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwCistNewRoot.setStatus(
        ""
    )

bt2SwStgTopologyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 44)
)
bt2SwStgTopologyChanged.setObjects(
      *(("BLADETYPE2-TRAP-MIB", "bt2SwTrapDisplayString"),
        ("BLADETYPE2-PHYSICAL-MIB", "stgCurCfgIndex"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwStgTopologyChanged.setStatus(
        ""
    )

bt2SwCistTopologyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 45)
)
bt2SwCistTopologyChanged.setObjects(
      *(("BLADETYPE2-TRAP-MIB", "bt2SwTrapDisplayString"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwCistTopologyChanged.setStatus(
        ""
    )

bt2SwHotlinksMasterUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 46)
)
bt2SwHotlinksMasterUp.setObjects(
      *(("BLADETYPE2-TRAP-MIB", "bt2SwTrapDisplayString"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwHotlinksMasterUp.setStatus(
        ""
    )

bt2SwHotlinksMasterDn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 47)
)
bt2SwHotlinksMasterDn.setObjects(
      *(("BLADETYPE2-TRAP-MIB", "bt2SwTrapDisplayString"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwHotlinksMasterDn.setStatus(
        ""
    )

bt2SwHotlinksBackupUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 48)
)
bt2SwHotlinksBackupUp.setObjects(
      *(("BLADETYPE2-TRAP-MIB", "bt2SwTrapDisplayString"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwHotlinksBackupUp.setStatus(
        ""
    )

bt2SwHotlinksBackupDn = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 49)
)
bt2SwHotlinksBackupDn.setObjects(
      *(("BLADETYPE2-TRAP-MIB", "bt2SwTrapDisplayString"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwHotlinksBackupDn.setStatus(
        ""
    )

bt2SwHotlinksNone = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33, 1, 2, 7, 0, 50)
)
bt2SwHotlinksNone.setObjects(
      *(("BLADETYPE2-TRAP-MIB", "bt2SwTrapDisplayString"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("SNMPv2-MIB", "sysContact"))
)
if mibBuilder.loadTexts:
    bt2SwHotlinksNone.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLADETYPE2-TRAP-MIB",
    **{"bt2Traps": bt2Traps,
       "bt2SwPrimaryPowerSupplyFailure": bt2SwPrimaryPowerSupplyFailure,
       "bt2SwDefGwUp": bt2SwDefGwUp,
       "bt2SwDefGwDown": bt2SwDefGwDown,
       "bt2SwDefGwInService": bt2SwDefGwInService,
       "bt2SwDefGwNotInService": bt2SwDefGwNotInService,
       "bt2SwVrrpNewMaster": bt2SwVrrpNewMaster,
       "bt2SwVrrpNewBackup": bt2SwVrrpNewBackup,
       "bt2SwVrrpAuthFailure": bt2SwVrrpAuthFailure,
       "bt2SwLoginFailure": bt2SwLoginFailure,
       "bt2SwTempExceedThreshold": bt2SwTempExceedThreshold,
       "bt2SwRackLocationChange": bt2SwRackLocationChange,
       "bt2SwApplyComplete": bt2SwApplyComplete,
       "bt2SwSaveComplete": bt2SwSaveComplete,
       "bt2SwFwDownloadSucess": bt2SwFwDownloadSucess,
       "bt2SwFwDownloadFailure": bt2SwFwDownloadFailure,
       "bt2SwTempReturnThreshold": bt2SwTempReturnThreshold,
       "bt2SwFanFailure": bt2SwFanFailure,
       "bt2SwFanFailureFixed": bt2SwFanFailureFixed,
       "bt2SwUfdfoLtMFailure": bt2SwUfdfoLtMFailure,
       "bt2SwUfdfoLtMUP": bt2SwUfdfoLtMUP,
       "bt2SwUfdfoGlobalEna": bt2SwUfdfoGlobalEna,
       "bt2SwUfdfoGlobalDis": bt2SwUfdfoGlobalDis,
       "bt2SwUfdfoLtDAutoEna": bt2SwUfdfoLtDAutoEna,
       "bt2SwUfdfoLtDAutoDis": bt2SwUfdfoLtDAutoDis,
       "bt2SwCubeInserted": bt2SwCubeInserted,
       "bt2SwCubeRemoved": bt2SwCubeRemoved,
       "bt2SwStgNewRoot": bt2SwStgNewRoot,
       "bt2SwCistNewRoot": bt2SwCistNewRoot,
       "bt2SwStgTopologyChanged": bt2SwStgTopologyChanged,
       "bt2SwCistTopologyChanged": bt2SwCistTopologyChanged,
       "bt2SwHotlinksMasterUp": bt2SwHotlinksMasterUp,
       "bt2SwHotlinksMasterDn": bt2SwHotlinksMasterDn,
       "bt2SwHotlinksBackupUp": bt2SwHotlinksBackupUp,
       "bt2SwHotlinksBackupDn": bt2SwHotlinksBackupDn,
       "bt2SwHotlinksNone": bt2SwHotlinksNone,
       "bt2SwTrapDisplayString": bt2SwTrapDisplayString}
)
