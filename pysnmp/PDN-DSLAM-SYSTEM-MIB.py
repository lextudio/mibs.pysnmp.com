# SNMP MIB module (PDN-DSLAM-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-DSLAM-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:36 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(pdn_dslam,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-dslam")

(IdslClockMode,
 SwitchState) = mibBuilder.importSymbols(
    "PDN-TC",
    "IdslClockMode",
    "SwitchState")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysObjectID,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysObjectID")

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
 RowStatus,
 TAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SysDevDslamMIBObjects_ObjectIdentity = ObjectIdentity
sysDevDslamMIBObjects = _SysDevDslamMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1)
)
_SysDevStats_ObjectIdentity = ObjectIdentity
sysDevStats = _SysDevStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1)
)
_LoginHistTable_Object = MibTable
loginHistTable = _LoginHistTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 1)
)
if mibBuilder.loadTexts:
    loginHistTable.setStatus("mandatory")
_LoginHistTableEntry_Object = MibTableRow
loginHistTableEntry = _LoginHistTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 1, 1)
)
loginHistTableEntry.setIndexNames(
    (0, "PDN-DSLAM-SYSTEM-MIB", "loginUserId"),
    (0, "PDN-DSLAM-SYSTEM-MIB", "loginTime"),
)
if mibBuilder.loadTexts:
    loginHistTableEntry.setStatus("mandatory")
_LoginUserId_Type = DisplayString
_LoginUserId_Object = MibTableColumn
loginUserId = _LoginUserId_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 1, 1, 1),
    _LoginUserId_Type()
)
loginUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginUserId.setStatus("mandatory")
_LoginTime_Type = TimeTicks
_LoginTime_Object = MibTableColumn
loginTime = _LoginTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 1, 1, 2),
    _LoginTime_Type()
)
loginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginTime.setStatus("mandatory")


class _LoginAccessApp_Type(Integer32):
    """Custom type loginAccessApp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("console", 1),
          ("ftp", 3),
          ("telnet", 2))
    )


_LoginAccessApp_Type.__name__ = "Integer32"
_LoginAccessApp_Object = MibTableColumn
loginAccessApp = _LoginAccessApp_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 1, 1, 3),
    _LoginAccessApp_Type()
)
loginAccessApp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginAccessApp.setStatus("mandatory")
_LoginAccessHost_Type = IpAddress
_LoginAccessHost_Object = MibTableColumn
loginAccessHost = _LoginAccessHost_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 1, 1, 4),
    _LoginAccessHost_Type()
)
loginAccessHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginAccessHost.setStatus("mandatory")


class _LoginUserPriv_Type(Integer32):
    """Custom type loginUserPriv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("administrator", 1),
          ("operator", 2))
    )


_LoginUserPriv_Type.__name__ = "Integer32"
_LoginUserPriv_Object = MibTableColumn
loginUserPriv = _LoginUserPriv_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 1, 1, 5),
    _LoginUserPriv_Type()
)
loginUserPriv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginUserPriv.setStatus("mandatory")


class _LoginStatus_Type(Integer32):
    """Custom type loginStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_LoginStatus_Type.__name__ = "Integer32"
_LoginStatus_Object = MibTableColumn
loginStatus = _LoginStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 1, 1, 6),
    _LoginStatus_Type()
)
loginStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginStatus.setStatus("mandatory")
_LoginFailureCountTable_Object = MibTable
loginFailureCountTable = _LoginFailureCountTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 2)
)
if mibBuilder.loadTexts:
    loginFailureCountTable.setStatus("mandatory")
_LoginFailureCountTableEntry_Object = MibTableRow
loginFailureCountTableEntry = _LoginFailureCountTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 2, 1)
)
loginFailureCountTableEntry.setIndexNames(
    (0, "PDN-DSLAM-SYSTEM-MIB", "loginFailureAccessApp"),
)
if mibBuilder.loadTexts:
    loginFailureCountTableEntry.setStatus("mandatory")


class _LoginFailureAccessApp_Type(Integer32):
    """Custom type loginFailureAccessApp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("console", 1),
          ("ftp", 3),
          ("telnet", 2))
    )


_LoginFailureAccessApp_Type.__name__ = "Integer32"
_LoginFailureAccessApp_Object = MibTableColumn
loginFailureAccessApp = _LoginFailureAccessApp_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 2, 1, 1),
    _LoginFailureAccessApp_Type()
)
loginFailureAccessApp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginFailureAccessApp.setStatus("mandatory")
_LoginFailureCount_Type = Counter32
_LoginFailureCount_Object = MibTableColumn
loginFailureCount = _LoginFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 2, 1, 2),
    _LoginFailureCount_Type()
)
loginFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginFailureCount.setStatus("mandatory")
_SysDevConfig_ObjectIdentity = ObjectIdentity
sysDevConfig = _SysDevConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2)
)


class _EnablePowerSourceFailureAlarm_Type(Integer32):
    """Custom type enablePowerSourceFailureAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_EnablePowerSourceFailureAlarm_Type.__name__ = "Integer32"
_EnablePowerSourceFailureAlarm_Object = MibScalar
enablePowerSourceFailureAlarm = _EnablePowerSourceFailureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 1),
    _EnablePowerSourceFailureAlarm_Type()
)
enablePowerSourceFailureAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enablePowerSourceFailureAlarm.setStatus("mandatory")
_DevIfTable_Object = MibTable
devIfTable = _DevIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 2)
)
if mibBuilder.loadTexts:
    devIfTable.setStatus("mandatory")
_DevIfTableEntry_Object = MibTableRow
devIfTableEntry = _DevIfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 2, 1)
)
devIfTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    devIfTableEntry.setStatus("mandatory")


class _DevPacketDiscardPolicy_Type(Integer32):
    """Custom type devPacketDiscardPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lrrp", 3),
          ("mrrp", 2),
          ("noOp", 1))
    )


_DevPacketDiscardPolicy_Type.__name__ = "Integer32"
_DevPacketDiscardPolicy_Object = MibTableColumn
devPacketDiscardPolicy = _DevPacketDiscardPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 2, 1, 1),
    _DevPacketDiscardPolicy_Type()
)
devPacketDiscardPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devPacketDiscardPolicy.setStatus("mandatory")


class _DevLinkIntegrity_Type(Integer32):
    """Custom type devLinkIntegrity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("none", 3))
    )


_DevLinkIntegrity_Type.__name__ = "Integer32"
_DevLinkIntegrity_Object = MibTableColumn
devLinkIntegrity = _DevLinkIntegrity_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 2, 1, 2),
    _DevLinkIntegrity_Type()
)
devLinkIntegrity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devLinkIntegrity.setStatus("mandatory")
_CommunityTrapAddressInfoTable_Object = MibTable
communityTrapAddressInfoTable = _CommunityTrapAddressInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 3)
)
if mibBuilder.loadTexts:
    communityTrapAddressInfoTable.setStatus("mandatory")
_CommunityTrapAddressInfoTableEntry_Object = MibTableRow
communityTrapAddressInfoTableEntry = _CommunityTrapAddressInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 3, 1)
)
communityTrapAddressInfoTableEntry.setIndexNames(
    (0, "PDN-DSLAM-SYSTEM-MIB", "trapCommunityName"),
    (0, "PDN-DSLAM-SYSTEM-MIB", "trapDestAndPort"),
)
if mibBuilder.loadTexts:
    communityTrapAddressInfoTableEntry.setStatus("mandatory")


class _TrapCommunityName_Type(DisplayString):
    """Custom type trapCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TrapCommunityName_Type.__name__ = "DisplayString"
_TrapCommunityName_Object = MibTableColumn
trapCommunityName = _TrapCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 3, 1, 1),
    _TrapCommunityName_Type()
)
trapCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapCommunityName.setStatus("mandatory")
_TrapDestAndPort_Type = TAddress
_TrapDestAndPort_Object = MibTableColumn
trapDestAndPort = _TrapDestAndPort_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 3, 1, 2),
    _TrapDestAndPort_Type()
)
trapDestAndPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDestAndPort.setStatus("mandatory")


class _TrapsEnable_Type(Integer32):
    """Custom type trapsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_TrapsEnable_Type.__name__ = "Integer32"
_TrapsEnable_Object = MibTableColumn
trapsEnable = _TrapsEnable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 3, 1, 3),
    _TrapsEnable_Type()
)
trapsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapsEnable.setStatus("mandatory")
_TrapRowStatus_Type = RowStatus
_TrapRowStatus_Object = MibTableColumn
trapRowStatus = _TrapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 3, 1, 4),
    _TrapRowStatus_Type()
)
trapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapRowStatus.setStatus("mandatory")
_EntCommunityTable_Object = MibTable
entCommunityTable = _EntCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 4)
)
if mibBuilder.loadTexts:
    entCommunityTable.setStatus("mandatory")
_EntCommunityTableEntry_Object = MibTableRow
entCommunityTableEntry = _EntCommunityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 4, 1)
)
entCommunityTableEntry.setIndexNames(
    (0, "PDN-DSLAM-SYSTEM-MIB", "entCommunityName"),
)
if mibBuilder.loadTexts:
    entCommunityTableEntry.setStatus("mandatory")


class _EntCommunityName_Type(DisplayString):
    """Custom type entCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EntCommunityName_Type.__name__ = "DisplayString"
_EntCommunityName_Object = MibTableColumn
entCommunityName = _EntCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 4, 1, 1),
    _EntCommunityName_Type()
)
entCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entCommunityName.setStatus("mandatory")


class _EntCommunityType_Type(Integer32):
    """Custom type entCommunityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_EntCommunityType_Type.__name__ = "Integer32"
_EntCommunityType_Object = MibTableColumn
entCommunityType = _EntCommunityType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 4, 1, 2),
    _EntCommunityType_Type()
)
entCommunityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entCommunityType.setStatus("mandatory")
_EntCommunityRowStatus_Type = RowStatus
_EntCommunityRowStatus_Object = MibTableColumn
entCommunityRowStatus = _EntCommunityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 4, 1, 3),
    _EntCommunityRowStatus_Type()
)
entCommunityRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entCommunityRowStatus.setStatus("mandatory")
_SysDevUserAccountTable_Object = MibTable
sysDevUserAccountTable = _SysDevUserAccountTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 5)
)
if mibBuilder.loadTexts:
    sysDevUserAccountTable.setStatus("mandatory")
_SysDevUserAccountEntry_Object = MibTableRow
sysDevUserAccountEntry = _SysDevUserAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 5, 1)
)
sysDevUserAccountEntry.setIndexNames(
    (0, "PDN-DSLAM-SYSTEM-MIB", "sysDevUserAccountUserId"),
)
if mibBuilder.loadTexts:
    sysDevUserAccountEntry.setStatus("mandatory")


class _SysDevUserAccountUserId_Type(DisplayString):
    """Custom type sysDevUserAccountUserId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 15),
    )


_SysDevUserAccountUserId_Type.__name__ = "DisplayString"
_SysDevUserAccountUserId_Object = MibTableColumn
sysDevUserAccountUserId = _SysDevUserAccountUserId_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 5, 1, 1),
    _SysDevUserAccountUserId_Type()
)
sysDevUserAccountUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevUserAccountUserId.setStatus("mandatory")


class _SysDevUserAccountPrivilege_Type(Integer32):
    """Custom type sysDevUserAccountPrivilege based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("administrator", 2),
          ("operator", 1))
    )


_SysDevUserAccountPrivilege_Type.__name__ = "Integer32"
_SysDevUserAccountPrivilege_Object = MibTableColumn
sysDevUserAccountPrivilege = _SysDevUserAccountPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 5, 1, 2),
    _SysDevUserAccountPrivilege_Type()
)
sysDevUserAccountPrivilege.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevUserAccountPrivilege.setStatus("mandatory")


class _SysDevUserAccountUserPassword_Type(DisplayString):
    """Custom type sysDevUserAccountUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 15),
    )


_SysDevUserAccountUserPassword_Type.__name__ = "DisplayString"
_SysDevUserAccountUserPassword_Object = MibTableColumn
sysDevUserAccountUserPassword = _SysDevUserAccountUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 5, 1, 3),
    _SysDevUserAccountUserPassword_Type()
)
sysDevUserAccountUserPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevUserAccountUserPassword.setStatus("mandatory")


class _SysDevUserAccountAccessPartition_Type(DisplayString):
    """Custom type sysDevUserAccountAccessPartition based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SysDevUserAccountAccessPartition_Type.__name__ = "DisplayString"
_SysDevUserAccountAccessPartition_Object = MibTableColumn
sysDevUserAccountAccessPartition = _SysDevUserAccountAccessPartition_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 5, 1, 4),
    _SysDevUserAccountAccessPartition_Type()
)
sysDevUserAccountAccessPartition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevUserAccountAccessPartition.setStatus("mandatory")
_SysDevUserAccountRowStatus_Type = RowStatus
_SysDevUserAccountRowStatus_Object = MibTableColumn
sysDevUserAccountRowStatus = _SysDevUserAccountRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 5, 1, 5),
    _SysDevUserAccountRowStatus_Type()
)
sysDevUserAccountRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevUserAccountRowStatus.setStatus("mandatory")
_SysDevIDSLConfigTable_Object = MibTable
sysDevIDSLConfigTable = _SysDevIDSLConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 6)
)
if mibBuilder.loadTexts:
    sysDevIDSLConfigTable.setStatus("mandatory")
_SysDevIDSLConfigEntry_Object = MibTableRow
sysDevIDSLConfigEntry = _SysDevIDSLConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 6, 1)
)
sysDevIDSLConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    sysDevIDSLConfigEntry.setStatus("mandatory")


class _SysDevIDSLConfigPrimaryNetClockMode_Type(IdslClockMode):
    """Custom type sysDevIDSLConfigPrimaryNetClockMode based on IdslClockMode"""


_SysDevIDSLConfigPrimaryNetClockMode_Object = MibTableColumn
sysDevIDSLConfigPrimaryNetClockMode = _SysDevIDSLConfigPrimaryNetClockMode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 6, 1, 1),
    _SysDevIDSLConfigPrimaryNetClockMode_Type()
)
sysDevIDSLConfigPrimaryNetClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIDSLConfigPrimaryNetClockMode.setStatus("mandatory")


class _SysDevIDSLConfigSecondaryNetClockMode_Type(IdslClockMode):
    """Custom type sysDevIDSLConfigSecondaryNetClockMode based on IdslClockMode"""


_SysDevIDSLConfigSecondaryNetClockMode_Object = MibTableColumn
sysDevIDSLConfigSecondaryNetClockMode = _SysDevIDSLConfigSecondaryNetClockMode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 6, 1, 2),
    _SysDevIDSLConfigSecondaryNetClockMode_Type()
)
sysDevIDSLConfigSecondaryNetClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevIDSLConfigSecondaryNetClockMode.setStatus("mandatory")
_SysDevDslamSyslog_ObjectIdentity = ObjectIdentity
sysDevDslamSyslog = _SysDevDslamSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 7)
)


class _SysDevSyslogFtpServerXferStatsEnable_Type(SwitchState):
    """Custom type sysDevSyslogFtpServerXferStatsEnable based on SwitchState"""


_SysDevSyslogFtpServerXferStatsEnable_Object = MibScalar
sysDevSyslogFtpServerXferStatsEnable = _SysDevSyslogFtpServerXferStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 7, 1),
    _SysDevSyslogFtpServerXferStatsEnable_Type()
)
sysDevSyslogFtpServerXferStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevSyslogFtpServerXferStatsEnable.setStatus("mandatory")


class _SysDevSyslogTftpServerXferStatsEnable_Type(SwitchState):
    """Custom type sysDevSyslogTftpServerXferStatsEnable based on SwitchState"""


_SysDevSyslogTftpServerXferStatsEnable_Object = MibScalar
sysDevSyslogTftpServerXferStatsEnable = _SysDevSyslogTftpServerXferStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 7, 2),
    _SysDevSyslogTftpServerXferStatsEnable_Type()
)
sysDevSyslogTftpServerXferStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevSyslogTftpServerXferStatsEnable.setStatus("mandatory")
_SysDevDslamMIBTraps_ObjectIdentity = ObjectIdentity
sysDevDslamMIBTraps = _SysDevDslamMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2)
)

# Managed Objects groups


# Notification objects

cCN = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 0, 7)
)
cCN.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    cCN.setStatus(
        ""
    )

authenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 0, 8)
)
authenticationFailure.setObjects(
      *(("PDN-DSLAM-SYSTEM-MIB", "loginFailureAccessApp"),
        ("PDN-DSLAM-SYSTEM-MIB", "loginFailureCount"))
)
if mibBuilder.loadTexts:
    authenticationFailure.setStatus(
        ""
    )

fanModuleFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 0, 9)
)
if mibBuilder.loadTexts:
    fanModuleFailure.setStatus(
        ""
    )

powerSourceAFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 0, 10)
)
if mibBuilder.loadTexts:
    powerSourceAFailure.setStatus(
        ""
    )

slotPollFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 0, 11)
)
slotPollFailure.setObjects(
    ("ENTITY-MIB", "entPhysicalIndex")
)
if mibBuilder.loadTexts:
    slotPollFailure.setStatus(
        ""
    )

ethernetJabber = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 0, 12)
)
ethernetJabber.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ethernetJabber.setStatus(
        ""
    )

ethernetJumbos = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 0, 13)
)
ethernetJumbos.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ethernetJumbos.setStatus(
        ""
    )

ethernetRunts = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 0, 14)
)
ethernetRunts.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ethernetRunts.setStatus(
        ""
    )

powerSourceBFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 0, 17)
)
if mibBuilder.loadTexts:
    powerSourceBFailure.setStatus(
        ""
    )

nonIpConservativeCardDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 0, 18)
)
nonIpConservativeCardDetected.setObjects(
    ("ENTITY-MIB", "entPhysicalIndex")
)
if mibBuilder.loadTexts:
    nonIpConservativeCardDetected.setStatus(
        ""
    )

nonSupportedMCC = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 0, 20)
)
nonSupportedMCC.setObjects(
    ("SNMPv2-MIB", "sysObjectID")
)
if mibBuilder.loadTexts:
    nonSupportedMCC.setStatus(
        ""
    )

nonSupportedChassis = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 0, 21)
)
nonSupportedChassis.setObjects(
    ("SNMPv2-MIB", "sysObjectID")
)
if mibBuilder.loadTexts:
    nonSupportedChassis.setStatus(
        ""
    )

fanModuleOperational = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 0, 109)
)
if mibBuilder.loadTexts:
    fanModuleOperational.setStatus(
        ""
    )

powerSourceAOperational = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 0, 110)
)
if mibBuilder.loadTexts:
    powerSourceAOperational.setStatus(
        ""
    )

newCardDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 0, 111)
)
newCardDetected.setObjects(
    ("ENTITY-MIB", "entPhysicalIndex")
)
if mibBuilder.loadTexts:
    newCardDetected.setStatus(
        ""
    )

ethernetJabberClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 0, 112)
)
ethernetJabberClear.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ethernetJabberClear.setStatus(
        ""
    )

powerSourceBOperational = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 0, 117)
)
if mibBuilder.loadTexts:
    powerSourceBOperational.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-DSLAM-SYSTEM-MIB",
    **{"sysDevDslamMIBObjects": sysDevDslamMIBObjects,
       "sysDevStats": sysDevStats,
       "loginHistTable": loginHistTable,
       "loginHistTableEntry": loginHistTableEntry,
       "loginUserId": loginUserId,
       "loginTime": loginTime,
       "loginAccessApp": loginAccessApp,
       "loginAccessHost": loginAccessHost,
       "loginUserPriv": loginUserPriv,
       "loginStatus": loginStatus,
       "loginFailureCountTable": loginFailureCountTable,
       "loginFailureCountTableEntry": loginFailureCountTableEntry,
       "loginFailureAccessApp": loginFailureAccessApp,
       "loginFailureCount": loginFailureCount,
       "sysDevConfig": sysDevConfig,
       "enablePowerSourceFailureAlarm": enablePowerSourceFailureAlarm,
       "devIfTable": devIfTable,
       "devIfTableEntry": devIfTableEntry,
       "devPacketDiscardPolicy": devPacketDiscardPolicy,
       "devLinkIntegrity": devLinkIntegrity,
       "communityTrapAddressInfoTable": communityTrapAddressInfoTable,
       "communityTrapAddressInfoTableEntry": communityTrapAddressInfoTableEntry,
       "trapCommunityName": trapCommunityName,
       "trapDestAndPort": trapDestAndPort,
       "trapsEnable": trapsEnable,
       "trapRowStatus": trapRowStatus,
       "entCommunityTable": entCommunityTable,
       "entCommunityTableEntry": entCommunityTableEntry,
       "entCommunityName": entCommunityName,
       "entCommunityType": entCommunityType,
       "entCommunityRowStatus": entCommunityRowStatus,
       "sysDevUserAccountTable": sysDevUserAccountTable,
       "sysDevUserAccountEntry": sysDevUserAccountEntry,
       "sysDevUserAccountUserId": sysDevUserAccountUserId,
       "sysDevUserAccountPrivilege": sysDevUserAccountPrivilege,
       "sysDevUserAccountUserPassword": sysDevUserAccountUserPassword,
       "sysDevUserAccountAccessPartition": sysDevUserAccountAccessPartition,
       "sysDevUserAccountRowStatus": sysDevUserAccountRowStatus,
       "sysDevIDSLConfigTable": sysDevIDSLConfigTable,
       "sysDevIDSLConfigEntry": sysDevIDSLConfigEntry,
       "sysDevIDSLConfigPrimaryNetClockMode": sysDevIDSLConfigPrimaryNetClockMode,
       "sysDevIDSLConfigSecondaryNetClockMode": sysDevIDSLConfigSecondaryNetClockMode,
       "sysDevDslamSyslog": sysDevDslamSyslog,
       "sysDevSyslogFtpServerXferStatsEnable": sysDevSyslogFtpServerXferStatsEnable,
       "sysDevSyslogTftpServerXferStatsEnable": sysDevSyslogTftpServerXferStatsEnable,
       "sysDevDslamMIBTraps": sysDevDslamMIBTraps,
       "cCN": cCN,
       "authenticationFailure": authenticationFailure,
       "fanModuleFailure": fanModuleFailure,
       "powerSourceAFailure": powerSourceAFailure,
       "slotPollFailure": slotPollFailure,
       "ethernetJabber": ethernetJabber,
       "ethernetJumbos": ethernetJumbos,
       "ethernetRunts": ethernetRunts,
       "powerSourceBFailure": powerSourceBFailure,
       "nonIpConservativeCardDetected": nonIpConservativeCardDetected,
       "nonSupportedMCC": nonSupportedMCC,
       "nonSupportedChassis": nonSupportedChassis,
       "fanModuleOperational": fanModuleOperational,
       "powerSourceAOperational": powerSourceAOperational,
       "newCardDetected": newCardDetected,
       "ethernetJabberClear": ethernetJabberClear,
       "powerSourceBOperational": powerSourceBOperational}
)
